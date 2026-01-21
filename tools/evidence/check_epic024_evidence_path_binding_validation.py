#!/usr/bin/env python3
"""Deterministic EPIC024 evidence path binding validation."""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence.check_po_006_token_registry_validity import (
    TokenSets,
    extract_acceptance_map_tokens,
    extract_registry_tokens,
    load_token_sets,
    normalize_tokens,
)
from tools.evidence import update_evidence_index
from tools.qa.step_log_header import append_output, create_header, write_header

DEFAULT_ACCEPTANCE_MAP = ROOT / "docs/acceptance_map_epic024.json"
DEFAULT_MATRIX = ROOT / "audit/qa/hde-epic024/token_evidence_matrix.md"
DEFAULT_INDEX = ROOT / "docs/evidence/INDEX.json"
DEFAULT_MIRROR = ROOT / "artifacts/evidence_index.jsonl"
DEFAULT_REGISTRY_EXPORT = ROOT / "reports/qa_acceptance_tokens.json"
DEFAULT_TOKEN_SETS = (
    ROOT
    / "audit/qa/hde-epic024/remediation/s1_token_registry_discovery/token_sets.json"
)
DEFAULT_CHECK_DIR = ROOT / "audit/qa/hde-epic024/checks/epic024_evidence_path_binding_validation"
DEFAULT_REVIEW_DIR = (
    ROOT / "audit/qa/hde-epic024/remediation/s2_dev_acceptance_artifacts"
)
REPORT_NAME = "evidence_path_binding_validation_report.json"
SCOPE_NAME = "token_evidence_matrix_scope.md"
GOVERNED_ROOTS = {"artifacts", "audit", "docs", "catalog", "schemas"}


@dataclass(frozen=True)
class MatrixEntry:
    token: str
    evidence: list[str]
    status: str


def _read_json(path: Path) -> object:
    return json.loads(path.read_text(encoding="utf-8"))


def _relative(path: Path, root: Path) -> str:
    if path.is_relative_to(root):
        return path.relative_to(root).as_posix()
    return path.as_posix()


def _unique_sorted(items: Iterable[str]) -> list[str]:
    return sorted(set(items))


def _normalize_status(value: str) -> str:
    return value.strip().lower().replace("-", "_").replace(" ", "_")


def _is_implemented(status: str) -> bool:
    normalized = _normalize_status(status)
    return normalized.startswith("implemented") or normalized.startswith("covered") or normalized in {
        "done",
        "green",
        "ready",
        "pass",
    }


def _looks_like_repo_path(entry: str) -> bool:
    if not entry or entry.startswith("python "):
        return False
    if "::" in entry or " " in entry:
        return False
    if entry.startswith("/") or entry.startswith("~"):
        return False
    return True


def _parse_matrix(path: Path) -> tuple[dict[str, MatrixEntry], list[str]]:
    tokens: dict[str, MatrixEntry] = {}
    duplicates: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().split("|") if part.strip()]
        if len(parts) < 6:
            continue
        first_cell = " ".join(parts[0].split()).lower()
        if first_cell in {"token name", "token_name"} or first_cell.replace(" ", "_") == "token_name":
            continue
        if all(not cell.strip() or set(cell.strip()) <= {"-", ":"} for cell in parts):
            continue
        token = parts[0]
        evidence = [item.strip() for item in parts[2].split(";") if item.strip()]
        status = parts[5]
        if token in tokens:
            duplicates.append(token)
        tokens[token] = MatrixEntry(token=token, evidence=evidence, status=status)
    return tokens, _unique_sorted(duplicates)


def _parse_acceptance_map(path: Path) -> tuple[dict[str, dict[str, object]], list[str]]:
    payload = _read_json(path)
    if not isinstance(payload, dict):
        raise ValueError("acceptance map payload must be a JSON object")
    entries = payload.get("tokens")
    if not isinstance(entries, list):
        raise ValueError("acceptance map tokens must be a list")
    tokens: dict[str, dict[str, object]] = {}
    duplicates: list[str] = []
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        name = entry.get("name")
        if not isinstance(name, str) or not name.strip():
            continue
        name = name.strip()
        if name in tokens:
            duplicates.append(name)
        tokens[name] = entry
    return tokens, _unique_sorted(duplicates)


def _load_index(path: Path) -> list[dict[str, object]]:
    payload = _read_json(path)
    if not isinstance(payload, list):
        raise ValueError("INDEX.json payload must be a list")
    return [entry for entry in payload if isinstance(entry, dict)]


def _load_mirror(path: Path) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        if isinstance(entry, dict):
            records.append(entry)
    return records


def _index_by_path(entries: Iterable[dict[str, object]]) -> dict[str, list[dict[str, object]]]:
    by_path: dict[str, list[dict[str, object]]] = {}
    for entry in entries:
        path = entry.get("discovered_physical_path")
        if isinstance(path, str) and path:
            by_path.setdefault(path, []).append(entry)
    return by_path


def build_report(
    *,
    acceptance_map_path: Path,
    matrix_path: Path,
    index_path: Path,
    mirror_path: Path,
    root: Path,
    determinism_ok: bool,
    determinism_error: str | None,
) -> tuple[dict[str, object], str]:
    issues: list[str] = []
    acceptance_tokens, acceptance_duplicates = _parse_acceptance_map(acceptance_map_path)
    matrix_tokens, matrix_duplicates = _parse_matrix(matrix_path)

    if acceptance_duplicates:
        for token in acceptance_duplicates:
            issues.append(f"DUPLICATE_ACCEPTANCE_TOKEN:{token}")
    if matrix_duplicates:
        for token in matrix_duplicates:
            issues.append(f"DUPLICATE_MATRIX_TOKEN:{token}")

    if set(acceptance_tokens) != set(matrix_tokens):
        issues.append("TOKEN_SET_MISMATCH")

    index_entries = _load_index(index_path)
    mirror_entries = _load_mirror(mirror_path)
    index_by_path = _index_by_path(index_entries)
    mirror_by_path = _index_by_path(mirror_entries)

    token_issues: dict[str, list[str]] = {}
    for token_name in sorted(set(acceptance_tokens) | set(matrix_tokens)):
        map_entry = acceptance_tokens.get(token_name)
        matrix_entry = matrix_tokens.get(token_name)
        per_token: list[str] = []
        if map_entry is None:
            per_token.append("MISSING_IN_ACCEPTANCE_MAP")
        if matrix_entry is None:
            per_token.append("MISSING_IN_MATRIX")
        if map_entry is None or matrix_entry is None:
            token_issues[token_name] = per_token
            continue

        if _normalize_status(matrix_entry.status) != _normalize_status(
            str(map_entry.get("status", ""))
        ):
            per_token.append("STATUS_MISMATCH")

        evidence_items: list[str] = []
        evidence_items.extend(matrix_entry.evidence)
        evidence_items.extend(map_entry.get("evidence_titles") or [])

        if _is_implemented(matrix_entry.status) and not evidence_items:
            per_token.append("MISSING_EVIDENCE")

        for evidence in evidence_items:
            if not isinstance(evidence, str) or not evidence.strip():
                continue
            if evidence.endswith(".path_proof.txt"):
                per_token.append(f"PATH_PROOF_USED:{evidence}")
            if evidence.startswith("/") or evidence.startswith("~"):
                per_token.append(f"ABSOLUTE_PATH:{evidence}")
                continue
            if ".." in Path(evidence).parts:
                per_token.append(f"PARENT_PATH:{evidence}")
                continue
            if _looks_like_repo_path(evidence):
                parts = Path(evidence).parts
                if not parts or parts[0] not in GOVERNED_ROOTS:
                    per_token.append(f"OUTSIDE_GOVERNED_ROOTS:{evidence}")
                if not (root / evidence).exists():
                    per_token.append(f"MISSING_EVIDENCE:{evidence}")
                if evidence not in index_by_path:
                    per_token.append(f"MISSING_INDEX_ENTRY:{evidence}")
                if evidence not in mirror_by_path:
                    per_token.append(f"MISSING_MIRROR_ENTRY:{evidence}")
                for rec in mirror_by_path.get(evidence, []):
                    if not rec.get("proof_anchor"):
                        per_token.append(f"MISSING_MIRROR_PROOF_ANCHOR:{evidence}")

        if per_token:
            token_issues[token_name] = _unique_sorted(per_token)
            issues.extend(per_token)

    status = "PASS"
    if not determinism_ok:
        status = "TOOLING_BLOCKED"
    elif issues:
        status = "FAIL_BEHAVIOR"

    report = {
        "schema": "epic024.evidence_path_binding_validation.v1",
        "status": status,
        "inputs": {
            "acceptance_map": _relative(acceptance_map_path, root),
            "token_matrix": _relative(matrix_path, root),
            "evidence_index": _relative(index_path, root),
            "evidence_mirror": _relative(mirror_path, root),
        },
        "determinism_env": {
            "ok": determinism_ok,
            "error": determinism_error,
        },
        "summary": {
            "token_count": len(set(acceptance_tokens) | set(matrix_tokens)),
            "issue_count": len(_unique_sorted(issues)),
        },
        "token_issues": token_issues,
        "issues": _unique_sorted(issues),
    }
    return report, status


def _canonicalize_tokens(tokens: Iterable[str], token_sets: TokenSets) -> list[str]:
    return _unique_sorted(normalize_tokens(tokens, token_sets.alias_map))


def render_scope(
    *,
    acceptance_tokens: Sequence[str],
    registry_tokens: Sequence[str],
    token_sets: TokenSets,
    acceptance_map_path: Path,
    registry_path: Path,
    token_sets_path: Path,
    root: Path,
) -> str:
    canonical_acceptance = _canonicalize_tokens(acceptance_tokens, token_sets)
    canonical_registry = _canonicalize_tokens(registry_tokens, token_sets)
    deprecated_used = sorted(
        token for token in acceptance_tokens if token in token_sets.deprecated_spellings
    )
    alias_replacements = {
        token: token_sets.alias_map[token]
        for token in deprecated_used
        if token in token_sets.alias_map
    }

    lines = [
        "# HDE-EPIC024 token evidence matrix scope",
        "",
        "## Scope",
        "- cleanup_scope: only docs/acceptance_map_epic024.json cleaned",
        f"- acceptance_map: {_relative(acceptance_map_path, root)}",
        f"- registry_export: {_relative(registry_path, root)}",
        f"- token_sets: {_relative(token_sets_path, root)}",
        "",
        "## Deprecated spellings",
    ]
    if deprecated_used:
        lines.append("- deprecated_spellings_found:")
        lines.extend(f"  - {token}" for token in deprecated_used)
        lines.append("- canonical_replacements:")
        for token, replacement in sorted(alias_replacements.items()):
            lines.append(f"  - {token} -> {replacement}")
    else:
        lines.append("- deprecated_spellings_found: none")
        lines.append("- canonical_replacements: none")

    lines.extend(
        [
            "",
            "## Acceptance tokens (canonicalized)",
            f"- token_count: {len(canonical_acceptance)}",
            "",
            "| token | in_registry_export | in_canonical_tokens |",
            "| --- | --- | --- |",
        ]
    )
    for token in canonical_acceptance:
        in_registry = "yes" if token in canonical_registry else "no"
        in_canonical = "yes" if token in token_sets.canonical_tokens else "no"
        lines.append(f"| {token} | {in_registry} | {in_canonical} |")

    return "\n".join(lines) + "\n"


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def _write_report(path: Path, report: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(sercanon(report, sort_keys=True))


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def _sha256_path(path: Path) -> str:
    return update_evidence_index._sha256_path(path)


def _write_path_proof(path: Path, *, produced_at: str) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime),
        produced_at=produced_at,
        default_produced_at=produced_at,
        check=False,
        stat_mtime=stat.st_mtime,
    )


def _validate_report(path: Path, expected: bytes) -> list[str]:
    if not path.exists():
        return [f"missing_output:{path}"]
    if path.read_bytes() != expected:
        return [f"mismatch_output:{path}"]
    return []


def _write_primary_log(
    output_dir: Path,
    *,
    status: str,
    command: str,
    exit_code: int,
    evidence_outputs: Sequence[str],
    summary: str,
) -> None:
    log_path = output_dir / "primary.log"
    header = create_header(
        check_id="epic024_evidence_path_binding_validation",
        command=command,
        status=status,
        pf_refs=["PF12 §Path Proofs", "PF19 §4.4.4"],
        intended_tokens=[],
        claimed_tokens=[],
    )
    header["exit_code"] = exit_code
    header["evidence_outputs"] = list(evidence_outputs)
    write_header(log_path, header)
    append_output(log_path, summary)


def run_report_mode(args: argparse.Namespace) -> int:
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        return 2

    produced_at = _utc_now()
    token_sets_path = Path(args.token_sets)
    token_sets = load_token_sets(token_sets_path)
    acceptance_tokens = extract_acceptance_map_tokens(Path(args.acceptance_map))
    registry_tokens = extract_registry_tokens(Path(args.registry_export))
    scope = render_scope(
        acceptance_tokens=acceptance_tokens.tokens,
        registry_tokens=registry_tokens.tokens,
        token_sets=token_sets,
        acceptance_map_path=Path(args.acceptance_map),
        registry_path=Path(args.registry_export),
        token_sets_path=token_sets_path,
        root=ROOT,
    )
    review_dir = Path(args.review_dir)
    scope_path = review_dir / SCOPE_NAME
    _write_text(scope_path, scope)
    _write_path_proof(scope_path, produced_at=produced_at)
    return 0


def run_check_mode(args: argparse.Namespace) -> int:
    determinism_ok = True
    determinism_error = None
    try:
        ensure_determinism_env()
    except DeterminismEnvError as exc:
        determinism_ok = False
        determinism_error = str(exc)

    if not determinism_ok:
        return 2

    report, status = build_report(
        acceptance_map_path=Path(args.acceptance_map),
        matrix_path=Path(args.matrix),
        index_path=Path(args.evidence_index),
        mirror_path=Path(args.evidence_mirror),
        root=ROOT,
        determinism_ok=determinism_ok,
        determinism_error=determinism_error,
    )
    report_bytes = sercanon(report, sort_keys=True)
    report_path = Path(args.output_dir) / REPORT_NAME

    if args.check:
        issues = _validate_report(report_path, report_bytes)
        if issues:
            status = "FAIL_BEHAVIOR"
        return 0 if status == "PASS" else 1

    _write_report(report_path, report)
    evidence_outputs = [_relative(report_path, ROOT)]
    summary = f"status: {status}\nissues: {len(report['issues'])}\n"
    exit_code = 0 if status == "PASS" else 1
    _write_primary_log(
        report_path.parent,
        status=status,
        command=args.command,
        exit_code=exit_code,
        evidence_outputs=evidence_outputs,
        summary=summary,
    )
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic EPIC024 evidence path binding validation."
    )
    subparsers = parser.add_subparsers(dest="mode")

    check_parser = subparsers.add_parser("check", help="Run or validate check outputs")
    check_parser.add_argument("--acceptance-map", default=DEFAULT_ACCEPTANCE_MAP)
    check_parser.add_argument("--matrix", default=DEFAULT_MATRIX)
    check_parser.add_argument("--evidence-index", default=DEFAULT_INDEX)
    check_parser.add_argument("--evidence-mirror", default=DEFAULT_MIRROR)
    check_parser.add_argument("--output-dir", default=DEFAULT_CHECK_DIR)
    check_parser.add_argument("--check", action="store_true", help="validate outputs only")
    check_parser.add_argument(
        "--command",
        default="python tools/evidence/check_epic024_evidence_path_binding_validation.py check",
    )
    check_parser.set_defaults(func=run_check_mode)

    report_parser = subparsers.add_parser(
        "report", help="Write remediation review artifacts"
    )
    report_parser.add_argument("--acceptance-map", default=DEFAULT_ACCEPTANCE_MAP)
    report_parser.add_argument("--registry-export", default=DEFAULT_REGISTRY_EXPORT)
    report_parser.add_argument("--token-sets", default=DEFAULT_TOKEN_SETS)
    report_parser.add_argument("--review-dir", default=DEFAULT_REVIEW_DIR)
    report_parser.set_defaults(func=run_report_mode)

    args = parser.parse_args()
    if not getattr(args, "func", None):
        parser.print_help()
        return 2
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
