#!/usr/bin/env python3
"""Capture the direct PostgreSQL EPIC011 posture into OPS diagnostics."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
CAPTURE_ROOT = ROOT
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.db import _util

FINGERPRINT_OBJECTS: tuple[tuple[str, str], ...] = (
    ("hde.body_graphs", "table"),
    ("hde.body_graphs_current", "view"),
    ("public.hde_body_graphs_current", "view"),
)
GRANT_OBJECTS = {name for name, _ in FINGERPRINT_OBJECTS}
PARTITION_TABLES = ("hde.public_results", "hde.pair_evaluation")


def _now() -> dt.datetime:
    return dt.datetime.now(tz=dt.timezone.utc).replace(microsecond=0)


def _iso(timestamp: dt.datetime) -> str:
    return timestamp.isoformat().replace("+00:00", "Z")


def _artifact_path(relative_path: str) -> Path:
    requested = Path(relative_path)
    try:
        requested.relative_to("artifacts")
    except ValueError as exc:
        raise ValueError(f"capture path must be under artifacts/: {relative_path}") from exc
    path = CAPTURE_ROOT / requested
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _write_path_proof(path: Path) -> None:
    stat = path.stat()
    mtime = dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc).replace(
        microsecond=0
    )
    proof = "\n".join(
        (
            f"path: {path.relative_to(ROOT)}",
            f"sha256: {hashlib.sha256(path.read_bytes()).hexdigest()}",
            f"size_bytes: {stat.st_size}",
            f"mtime_utc: {_iso(mtime)}",
            "",
        )
    )
    Path(f"{path}.path_proof.txt").write_text(proof, encoding="utf-8")


def _write_bytes(relative_path: str, data: bytes) -> None:
    path = _artifact_path(relative_path)
    path.write_bytes(data)
    _write_path_proof(path)


def _write_text(relative_path: str, text: str) -> None:
    if not text.endswith("\n"):
        text += "\n"
    _write_bytes(relative_path, text.encode("utf-8"))


def _write_json(relative_path: str, payload: Mapping[str, Any]) -> None:
    data = (json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")
    _write_bytes(relative_path, data)


def _search_path_value(db: "DBAccess") -> str:
    payload = db.introspect_search_path()
    value = payload.get("search_path", "") if isinstance(payload, Mapping) else payload
    return str(value).strip()


def _fingerprint_objects(db: "DBAccess") -> List[Dict[str, Any]]:
    payload = db.introspect_fingerprint() or {}
    objects_raw = payload.get("objects") if isinstance(payload, Mapping) else None
    lookup: Dict[str, Mapping[str, Any]] = {}
    if isinstance(objects_raw, Mapping):
        lookup = {
            str(key): value
            for key, value in objects_raw.items()
            if isinstance(value, Mapping)
        }
    elif isinstance(objects_raw, list):
        for entry in objects_raw:
            if not isinstance(entry, Mapping):
                continue
            schema = entry.get("schema")
            name = entry.get("name")
            key = entry.get("object") or (f"{schema}.{name}" if schema and name else name)
            if key:
                lookup[str(key)] = entry
    normalized: List[Dict[str, Any]] = []
    for name, kind in FINGERPRINT_OBJECTS:
        entry = lookup.get(name, {})
        record: Dict[str, Any] = {"name": name, "kind": kind}
        if kind == "table":
            record["columns"] = entry.get("columns", [])
            record["constraints"] = entry.get("constraints", [])
        else:
            record["definition"] = entry.get("definition", "")
        normalized.append(record)
    return normalized


def _grant_payload(db: "DBAccess") -> Mapping[str, Any]:
    payload = db.introspect("grants")
    return payload if isinstance(payload, Mapping) else {}


def _grant_lines(payload: Mapping[str, Any]) -> List[str]:
    grants = payload.get("grants", [])
    lines: List[str] = []
    for entry in grants:
        if isinstance(entry, Mapping):
            grantee = str(entry.get("role") or entry.get("grantee") or "").strip()
            obj = str(entry.get("object") or entry.get("table") or "").strip()
            privilege = str(
                entry.get("priv") or entry.get("privilege") or entry.get("privilege_type") or ""
            ).strip()
        else:
            try:
                grantee, obj, privilege = entry
            except Exception:
                continue
            grantee, obj, privilege = str(grantee).strip(), str(obj).strip(), str(privilege).strip()
        if grantee and obj in GRANT_OBJECTS and privilege:
            lines.append(f"{grantee} {obj} {privilege}")
    return sorted(dict.fromkeys(lines))


def _default_privilege_lines(payload: Mapping[str, Any]) -> List[str]:
    lines: List[str] = []
    for entry in payload.get("default_privileges", []):
        if isinstance(entry, str):
            text = entry.strip()
        elif isinstance(entry, Mapping):
            text = " ".join(
                str(value).strip()
                for value in (
                    entry.get("owner"),
                    entry.get("schema"),
                    entry.get("type"),
                    entry.get("grantee"),
                    entry.get("privilege"),
                )
                if value
            ).strip()
        else:
            text = str(entry or "").strip()
        if text:
            lines.append(text)
    return lines or ["(none)"]


def _strip_strategy_prefix(raw: str) -> str:
    parts = (raw or "").split(maxsplit=1)
    return parts[1] if len(parts) == 2 else raw or ""


def _partition_plan(db: "DBAccess") -> tuple[List[str], List[str]]:
    rows = db.query(
        """
        SELECT
            ns.nspname || '.' || c.relname AS table_name,
            CASE
                WHEN pt.partstrat IN ('r', 'R') THEN 'RANGE'
                WHEN pt.partstrat IN ('l', 'L') THEN 'LIST'
                WHEN pt.partstrat IN ('h', 'H') THEN 'HASH'
                ELSE pt.partstrat
            END AS strategy,
            pg_get_partkeydef(pt.partrelid) AS part_key
        FROM pg_partitioned_table pt
        JOIN pg_class c ON c.oid = pt.partrelid
        JOIN pg_namespace ns ON ns.oid = c.relnamespace
        WHERE ns.nspname = 'hde' AND c.relname IN ('public_results', 'pair_evaluation')
        ORDER BY table_name
        """
    )
    if not rows:
        raise SystemExit("partition plan query returned no rows")
    strategy_lookup = {
        "r": "RANGE",
        "R": "RANGE",
        "l": "LIST",
        "L": "LIST",
        "h": "HASH",
        "H": "HASH",
    }
    plan: List[str] = []
    observed: List[str] = []
    for table_name, strategy, raw_key in rows:
        name = str(table_name)
        observed.append(name)
        key_expression = _strip_strategy_prefix(str(raw_key or "")).strip()
        if key_expression and not key_expression.startswith("("):
            key_expression = f"({key_expression})"
        plan.append(
            f"{name} {strategy_lookup.get(str(strategy), str(strategy))} {key_expression}".strip()
        )
    return plan, observed


def _partition_verify_lines(observed: Sequence[str]) -> List[str]:
    expected = list(PARTITION_TABLES)
    observed_sorted = sorted(observed)
    missing = [name for name in expected if name not in observed_sorted]
    extra = [name for name in observed_sorted if name not in expected]
    if missing or extra:
        details = ", ".join(
            item
            for item in (
                f"missing: {', '.join(missing)}" if missing else "",
                f"extra: {', '.join(extra)}" if extra else "",
            )
            if item
        )
        raise SystemExit(f"partition plan mismatch: {details}")
    return [
        f"expected: {', '.join(expected)}",
        f"observed: {', '.join(observed_sorted)}",
        "result: PARTITION_PLAN_OK",
    ]


def _boundary_view_lines(db: "DBAccess") -> List[str]:
    rows = db.query(
        """
        SELECT table_schema, table_name, is_updatable, is_insertable_into, is_trigger_updatable
        FROM information_schema.views
        WHERE (table_schema = 'hde' AND table_name = 'body_graphs_current')
           OR (table_schema = 'public' AND table_name = 'hde_body_graphs_current')
        ORDER BY table_schema, table_name
        """
    )
    if len(rows) != len(FINGERPRINT_OBJECTS) - 1:
        raise SystemExit("unexpected boundary view metadata result set")
    lines: List[str] = []
    for schema, name, updatable, insertable, trigger_updatable in rows:
        lines.extend(
            (
                f"view: {schema}.{name}",
                f"is_updatable: {updatable}",
                f"is_insertable_into: {insertable}",
                f"is_trigger_updatable: {trigger_updatable}",
                "",
            )
        )
    if lines:
        lines.pop()
    return lines


def main() -> None:
    captured_at = _iso(_now())
    db = _util.db_access()
    if db.provider_name != "psycopg":
        raise SystemExit("direct PostgreSQL provider required")

    search_path = _search_path_value(db)
    if search_path != "hde, public":
        raise SystemExit(f"unexpected search_path: {search_path!r}")
    _write_text("artifacts/db/check_schema.txt", search_path)

    _write_json(
        "artifacts/db/ddl_fingerprint.json",
        {
            "schema": "hde",
            "captured_at_utc": captured_at,
            "objects": _fingerprint_objects(db),
        },
    )

    grant_payload = _grant_payload(db)
    grants = _grant_lines(grant_payload)
    if not grants:
        raise SystemExit("no grants captured for EPIC011 objects")
    _write_text(
        "artifacts/db/grants.txt",
        "\n".join([*grants, "", "ALTER DEFAULT PRIVILEGES:", *_default_privilege_lines(grant_payload)]),
    )

    partition_plan, observed = _partition_plan(db)
    _write_text("artifacts/db/partition_plan.txt", "\n".join(partition_plan))
    _write_text(
        "artifacts/db/partition_verify.log",
        "\n".join(_partition_verify_lines(observed)),
    )
    _write_text(
        "artifacts/db/boundary_view.readonly.proof.txt",
        "\n".join(_boundary_view_lines(db)),
    )


if __name__ == "__main__":
    main()
