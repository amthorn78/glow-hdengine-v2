#!/usr/bin/env python3
"""Generate the keys-only, fail-closed PR-04 architecture snapshot."""
from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env

ART = ROOT / "artifacts/architecture/architecture_snapshot.keys_only.json"
SCHEMA = ROOT / "schemas/architecture_snapshot.keys_only.v1.json"
CLASSES = {"allowed", "forbidden", "unknown", "out_of_scope"}
ROUTE_METHODS = {"route", "get", "post", "put", "patch", "delete", "head", "options"}
TS = "2026-07-14T00:00:00Z"


def cjson(payload: Any) -> bytes:
    return (json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n").encode()


def tracked() -> list[str]:
    output = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True
    )
    prefixes = ("engine/", "adapter/", "tools/evidence/", "scripts/bodygraph/", "scripts/db/")
    return sorted(
        path
        for path in set(output.splitlines())
        if path != "tools/evidence/generate_architecture_snapshot.py"
        and path.endswith(".py")
        and path.startswith(prefixes)
    )


def classify(path: str) -> str:
    if path.startswith(("engine/", "adapter/", "tools/evidence/", "scripts/db/", "scripts/bodygraph/")):
        return "allowed"
    return "out_of_scope"


def _name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    return None


def _call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
        return f"{node.value.id}.{node.attr}"
    return None


def _literal_path(call: ast.Call) -> str | None:
    if call.args and isinstance(call.args[0], ast.Constant) and isinstance(call.args[0].value, str):
        return call.args[0].value
    return None


@dataclass(frozen=True)
class RouteAnalysis:
    routes: list[dict[str, Any]]
    registrations: list[dict[str, Any]]


def analyze_source(path: str, source: str) -> RouteAnalysis:
    tree = ast.parse(source, filename=path)
    flask_factories = {"Flask"}
    blueprint_factories = {"Blueprint"}
    flask_modules: set[str] = set()
    owners: dict[str, str] = {}

    for node in ast.walk(tree):
        if isinstance(node, ast.ImportFrom) and node.module == "flask":
            for alias in node.names:
                if alias.name == "Flask":
                    flask_factories.add(alias.asname or alias.name)
                elif alias.name == "Blueprint":
                    blueprint_factories.add(alias.asname or alias.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name == "flask":
                    flask_modules.add(alias.asname or alias.name)

    for node in ast.walk(tree):
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        value = node.value
        if not isinstance(value, ast.Call):
            continue
        factory = _call_name(value.func)
        target_nodes = node.targets if isinstance(node, ast.Assign) else [node.target]
        target_names = [name for target in target_nodes if (name := _name(target))]
        kind: str | None = None
        if factory in flask_factories or factory in {f"{module}.Flask" for module in flask_modules}:
            kind = "flask"
        elif factory in blueprint_factories or factory in {f"{module}.Blueprint" for module in flask_modules}:
            kind = "blueprint"
        if kind:
            for target in target_names:
                owners[target] = kind

    routes: list[dict[str, Any]] = []
    registrations: list[dict[str, Any]] = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for decorator in node.decorator_list:
                if not isinstance(decorator, ast.Call) or not isinstance(decorator.func, ast.Attribute):
                    continue
                method = decorator.func.attr
                if method not in ROUTE_METHODS:
                    continue
                receiver = _name(decorator.func.value)
                known = receiver is not None and receiver in owners
                routes.append(
                    {
                        "path": path,
                        "line": decorator.lineno,
                        "receiver": receiver or "<expression>",
                        "receiver_kind": owners.get(receiver, "unknown"),
                        "method": method,
                        "route_path": _literal_path(decorator),
                        "classification": classify(path) if known else "unknown",
                        "reason_code": "known_flask_route_decorator" if known else "unclassified_route_decorator_receiver",
                    }
                )
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Attribute):
            continue
        method = node.func.attr
        if method not in {"add_url_rule", "register_blueprint"}:
            continue
        receiver = _name(node.func.value)
        known = receiver is not None and owners.get(receiver) == "flask"
        row: dict[str, Any] = {
            "path": path,
            "line": node.lineno,
            "receiver": receiver or "<expression>",
            "method": method,
            "classification": classify(path) if known else "unknown",
            "reason_code": "known_flask_registration" if known else "unclassified_route_registration_receiver",
        }
        if method == "add_url_rule":
            row["route_path"] = _literal_path(node)
            routes.append(row)
        else:
            row["blueprint_symbol"] = _name(node.args[0]) if node.args else None
            registrations.append(row)

    return RouteAnalysis(
        routes=sorted(routes, key=lambda row: (row["line"], row["method"])),
        registrations=sorted(registrations, key=lambda row: (row["line"], row["method"])),
    )


def analyze() -> dict[str, Any]:
    findings: list[dict[str, Any]] = []
    routes: list[dict[str, Any]] = []
    registrations: list[dict[str, Any]] = []
    imports: list[str] = []
    for path in tracked():
        source_path = ROOT / path
        if not source_path.exists():
            continue
        text = source_path.read_text(encoding="utf-8")
        tree = ast.parse(text, filename=path)
        imported = sorted(
            {node.names[0].name.split(".")[0] for node in ast.walk(tree) if isinstance(node, ast.Import) and node.names}
            | {
                str(node.module).split(".")[0]
                for node in ast.walk(tree)
                if isinstance(node, ast.ImportFrom) and node.module
            }
        )
        external = sorted(set(re.findall(r"\b(requests|socket|subprocess|psycopg|urllib)\b", text)))
        findings.append(
            {
                "path": path,
                "classification": classify(path),
                "symbols": imported[:20],
                "external_io_symbols": external,
                "reason_code": "bounded_static_locus",
            }
        )
        imports.extend(external)
        route_analysis = analyze_source(path, text)
        routes.extend(route_analysis.routes)
        registrations.extend(route_analysis.registrations)

    registrations.extend(
        [
            {
                "path": "tools/evidence/update_evidence_index.py",
                "classification": "allowed",
                "reason_code": "governed_evidence_registry",
            },
            {
                "path": "schemas/architecture_snapshot.keys_only.v1.json",
                "classification": "allowed",
                "reason_code": "schema_registration",
            },
        ]
    )
    analyzed_rows = [*findings, *routes, *registrations]
    unknown_count = sum(row.get("classification") == "unknown" for row in analyzed_rows)
    forbidden_count = sum(row.get("classification") == "forbidden" for row in analyzed_rows)
    analyzer_verdict = "fail" if unknown_count or forbidden_count else "pass"
    return {
        "schema": "architecture_snapshot.keys_only.v1",
        "captured_at_utc": TS,
        "taxonomy": sorted(CLASSES),
        "verdict": analyzer_verdict,
        "analyzer_verdict": analyzer_verdict,
        "findings": findings,
        "routes": sorted(routes, key=lambda row: (row["path"], row["line"], row["method"])),
        "registrations": sorted(registrations, key=lambda row: (row["path"], row.get("line", 0))),
        "forbidden_patterns": [],
        "unknown_count": unknown_count,
        "external_io_symbol_kinds": sorted(set(imports)),
    }


def schema_payload() -> dict[str, Any]:
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "schemas/architecture_snapshot.keys_only.v1.json",
        "type": "object",
        "required": ["schema", "taxonomy", "verdict", "analyzer_verdict", "findings", "unknown_count"],
        "properties": {
            "schema": {"const": "architecture_snapshot.keys_only.v1"},
            "taxonomy": {"type": "array", "items": {"enum": sorted(CLASSES)}},
            "verdict": {"enum": ["pass", "fail"]},
            "analyzer_verdict": {"enum": ["pass", "fail"]},
            "unknown_count": {"type": "integer", "minimum": 0},
            "findings": {"type": "array"},
            "routes": {"type": "array"},
            "registrations": {"type": "array"},
            "forbidden_patterns": {"type": "array"},
            "external_io_symbol_kinds": {"type": "array"},
            "captured_at_utc": {"type": "string"},
        },
        "additionalProperties": False,
    }


def validate(payload: dict[str, Any]) -> None:
    if set(payload["taxonomy"]) != CLASSES:
        raise SystemExit("TAXONOMY_DRIFT")
    rows = [*payload.get("findings", []), *payload.get("routes", []), *payload.get("registrations", [])]
    if any(row.get("classification") not in CLASSES for row in rows):
        raise SystemExit("BAD_CLASSIFICATION")
    derived_unknown = sum(row.get("classification") == "unknown" for row in rows)
    derived_forbidden = sum(row.get("classification") == "forbidden" for row in rows)
    derived_verdict = "fail" if derived_unknown or derived_forbidden else "pass"
    if payload["unknown_count"] != derived_unknown:
        raise SystemExit("UNKNOWN_COUNT_MISMATCH")
    if payload["analyzer_verdict"] != derived_verdict or payload["verdict"] != derived_verdict:
        raise SystemExit("VERDICT_MISMATCH")
    raw = json.dumps(payload)
    if re.search(
        r"(DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|birthdate|birthtime|location|Authorization|Bearer|password)",
        raw,
        re.I,
    ):
        raise SystemExit("UNSAFE_PATTERN")


def write(path: Path, data: bytes, check: bool) -> None:
    if check:
        if not path.exists() or path.read_bytes() != data:
            raise SystemExit(f"STALE:{path.relative_to(ROOT).as_posix()}")
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)


def generate(check: bool = False) -> None:
    ensure_determinism_env()
    schema = schema_payload()
    payload = analyze()
    validate(payload)
    write(SCHEMA, cjson(schema), check)
    write(ART, cjson(payload), check)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    generate(args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
