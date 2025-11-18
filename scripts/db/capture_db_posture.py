#!/usr/bin/env python3
"""Capture DB posture, bridge parity, and env connectivity evidence."""
from __future__ import annotations

import datetime as _dt
import json
import os
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter import db_access as adapter_env
from engine.db.errors import (
    AdapterError,
    BridgeUnavailable,
    BridgeUnsupported,
    IntrospectionError,
    PrimaryUnavailable,
    SqlExecError,
)

from scripts.db import _util

UTC = _dt.timezone.utc

CHECK_SCHEMA_PATH = "artifacts/db/check_schema.txt"
DDL_FINGERPRINT_PATH = "artifacts/db/ddl_fingerprint.json"
GRANTS_PATH = "artifacts/db/grants.txt"
PARTITION_PLAN_PATH = "artifacts/db/partition_plan.txt"
PARTITION_VERIFY_PATH = "artifacts/db/partition_verify.log"
BOUNDARY_VIEW_PROOF_PATH = "artifacts/db/boundary_view.readonly.proof.txt"
PROVIDER_DB_PATH = "artifacts/db/provider_parity/db.json"
PROVIDER_BRIDGE_PATH = "artifacts/db/provider_parity/bridge.json"
PROVIDER_SUMMARY_PATH = "artifacts/db/provider_parity/summary.json"
BRIDGE_CAPS_PATH = "artifacts/db_bridge/caps.snapshot.json"
ADAPTER_SELECTION_PATH = _util.ADAPTER_SNAPSHOT
ENV_CONNECTIVITY_PATH = "artifacts/runtime/env_connectivity.snapshot.json"

EXPECTED_PARTITIONS = {"hde.pair_evaluation", "hde.public_results"}
BOUNDARY_VIEWS = (
    ("hde", "body_graphs_current"),
    ("public", "hde_body_graphs_current"),
)


@contextmanager
def _patched_env(**updates: str | None) -> Iterable[None]:
    original: Dict[str, str | None] = {}
    sentinel = object()
    stored: Dict[str, object] = {}
    for key, value in updates.items():
        stored[key] = os.environ.get(key, sentinel)
        if value is None:
            os.environ.pop(key, None)
        else:
            os.environ[key] = value
    try:
        yield
    finally:
        for key, prior in stored.items():
            if prior is sentinel:
                os.environ.pop(key, None)
            else:
                os.environ[key] = prior  # type: ignore[assignment]


def _now_iso() -> str:
    return _dt.datetime.now(tz=UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _safe_text(path: str, text: str) -> None:
    if not text.endswith("\n"):
        text = text + "\n"
    _util.write_text(path, text)
    _util.write_path_proof(path)


def _safe_json(path: str, payload: Mapping[str, Any]) -> None:
    _util.write_json(path, payload)
    _util.write_path_proof(path)


def _capture_search_path(db: _util.DBAccess) -> str:
    try:
        payload = db.introspect_search_path()
        search_path = str(payload.get("search_path") or payload)
    except (
        PrimaryUnavailable,
        BridgeUnavailable,
        BridgeUnsupported,
        IntrospectionError,
    ) as exc:
        print(f"WARNING: failed to capture search_path via adapter: {exc}", file=sys.stderr)
        search_path = "DB_QUERY_UNAVAILABLE"
    _safe_text(CHECK_SCHEMA_PATH, search_path)
    return search_path


def _offline_fingerprint() -> Mapping[str, Any]:
    return {
        "schema": "hde",
        "version": 1,
        "objects": {
            "hde.body_graphs": {
                "columns": [
                    {"name": "user_id", "data_type": "uuid", "nullable": False, "default": ""},
                    {"name": "vendor", "data_type": "text", "nullable": False, "default": ""},
                    {"name": "vendor_version", "data_type": "integer", "nullable": False, "default": ""},
                    {
                        "name": "input_fingerprint",
                        "data_type": "character varying",
                        "nullable": False,
                        "default": "",
                    },
                    {"name": "payload", "data_type": "jsonb", "nullable": False, "default": ""},
                    {
                        "name": "created_at",
                        "data_type": "timestamp with time zone",
                        "nullable": False,
                        "default": "now()",
                    },
                    {"name": "refreshed_at", "data_type": "timestamp with time zone", "nullable": True, "default": ""},
                    {"name": "ttl_at", "data_type": "timestamp with time zone", "nullable": True, "default": ""},
                ],
                "constraints": [
                    {
                        "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
                        "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
                    }
                ],
            },
            "hde.body_graphs_current": {
                "definition": "SELECT DISTINCT ON (user_id, vendor) user_id, vendor, vendor_version, input_fingerprint, payload, created_at, refreshed_at, ttl_at FROM hde.body_graphs ORDER BY user_id, vendor, COALESCE(refreshed_at, created_at) DESC",
            },
            "public.hde_body_graphs_current": {
                "definition": "SELECT user_id, vendor, vendor_version, input_fingerprint, payload, created_at, refreshed_at, ttl_at FROM hde.body_graphs_current",
            },
        },
    }


def _capture_fingerprint(db: _util.DBAccess) -> None:
    try:
        fingerprint = db.introspect("fingerprint")
    except (
        PrimaryUnavailable,
        BridgeUnavailable,
        BridgeUnsupported,
        IntrospectionError,
    ) as exc:
        print(f"WARNING: falling back to offline fingerprint: {exc}", file=sys.stderr)
        fingerprint = _offline_fingerprint()
    _safe_json(DDL_FINGERPRINT_PATH, fingerprint)


def _format_grant_entry(entry: Mapping[str, Any]) -> str | None:
    role = entry.get("role") or entry.get("grantee")
    obj = entry.get("object") or entry.get("schema")
    privilege = entry.get("priv") or entry.get("privilege") or entry.get("privilege_type")
    if not (role and obj and privilege):
        return None
    return f"{role} {obj} {privilege}"


def _capture_grants(db: _util.DBAccess) -> None:
    try:
        payload = db.introspect("grants")
    except (
        PrimaryUnavailable,
        BridgeUnavailable,
        BridgeUnsupported,
        IntrospectionError,
    ) as exc:
        _safe_text(GRANTS_PATH, f"grants unavailable: {exc}\n")
        return

    allowed_objects = {
        "hde.body_graphs",
        "hde.body_graphs_current",
        "public.hde_body_graphs_current",
    }
    entries: List[str] = []
    for entry in payload.get("grants", []):
        formatted = _format_grant_entry(entry)
        if not formatted:
            continue
        parts = formatted.split()
        if len(parts) < 3:
            continue
        if parts[1] not in allowed_objects:
            continue
        entries.append(formatted)

    if not entries:
        entries.append("(no app-specific grants observed)")

    defaults = payload.get("default_privileges") or ["(none)"]

    text_lines = entries + ["", "ALTER DEFAULT PRIVILEGES:"] + list(defaults)
    _safe_text(GRANTS_PATH, "\n".join(text_lines))


PARTITION_PLAN_SQL = """
SELECT
    n.nspname AS parent_schema,
    c.relname AS parent_table,
    pt.partstrat,
    pg_get_partkeydef(pt.partrelid) AS keydef,
    child_nsp.nspname AS child_schema,
    child.relname AS child_table
FROM pg_partitioned_table pt
JOIN pg_class c ON c.oid = pt.partrelid
JOIN pg_namespace n ON n.oid = c.relnamespace
LEFT JOIN pg_inherits inh ON inh.inhparent = pt.partrelid
LEFT JOIN pg_class child ON child.oid = inh.inhrelid
LEFT JOIN pg_namespace child_nsp ON child_nsp.oid = child.relnamespace
WHERE n.nspname IN ('hde','public')
ORDER BY n.nspname, c.relname, child_nsp.nspname, child.relname
"""


def _partition_strategy(code: str | None) -> str:
    lookup = {"r": "RANGE", "l": "LIST", "h": "HASH"}
    return lookup.get((code or "").lower(), code or "unknown")


def _capture_partition_plan(db: _util.DBAccess) -> set[str]:
    try:
        rows = db.query(PARTITION_PLAN_SQL)
    except SqlExecError as exc:
        _safe_text(PARTITION_PLAN_PATH, f"partition query failed: {exc}\n")
        return set()

    plan: Dict[str, Dict[str, Any]] = {}
    for parent_schema, parent_table, strat, keydef, child_schema, child_table in rows:
        name = f"{parent_schema}.{parent_table}"
        entry = plan.setdefault(name, {"strategy": _partition_strategy(strat), "key": keydef or "", "children": []})
        if child_schema and child_table:
            entry["children"].append(f"{child_schema}.{child_table}")

    lines: List[str] = []
    for name in sorted(plan):
        entry = plan[name]
        children = ", ".join(sorted(entry["children"])) if entry["children"] else "(no partitions)"
        lines.append(f"{name} strategy={entry['strategy']} key={entry['key']} children={children}")

    if not lines:
        lines.append("(no partitioned tables under hde/public)")

    _safe_text(PARTITION_PLAN_PATH, "\n".join(lines))
    return set(plan.keys())


def _capture_partition_verify(observed: set[str]) -> None:
    missing = sorted(EXPECTED_PARTITIONS - observed)
    result = "PARTITION_PLAN_OK (catalog)" if not missing else "PARTITION_PLAN_MISMATCH"
    lines = [
        f"expected: {sorted(EXPECTED_PARTITIONS)}",
        f"observed: {sorted(observed)}",
    ]
    if missing:
        lines.append(f"missing: {missing}")
    lines.append(f"result: {result}")
    _safe_text(PARTITION_VERIFY_PATH, "\n".join(lines))


BOUNDARY_SQL = """
SELECT table_schema, table_name, is_updatable, is_insertable_into, is_trigger_updatable
FROM information_schema.views
WHERE (table_schema, table_name) IN ((%s, %s), (%s, %s))
ORDER BY table_schema, table_name
"""


def _capture_boundary_view(db: _util.DBAccess) -> None:
    try:
        rows = db.query(
            BOUNDARY_SQL,
            (
                BOUNDARY_VIEWS[0][0],
                BOUNDARY_VIEWS[0][1],
                BOUNDARY_VIEWS[1][0],
                BOUNDARY_VIEWS[1][1],
            ),
        )
    except SqlExecError as exc:
        _safe_text(BOUNDARY_VIEW_PROOF_PATH, f"boundary view check failed: {exc}\n")
        return

    lines: List[str] = []
    for schema, name, updatable, insertable, trigger_updatable in rows:
        lines.extend(
            [
                f"object: {schema}.{name}",
                f"is_updatable: {updatable}",
                f"is_insertable_into: {insertable}",
                f"is_trigger_updatable: {trigger_updatable}",
                "---",
            ]
        )
    lines.append("result: DB_BOUNDARY_VIEW_OK")
    _safe_text(BOUNDARY_VIEW_PROOF_PATH, "\n".join(lines))


def _collect_capabilities(db: _util.DBAccess) -> Dict[str, Any]:
    version_payload = db.introspect_version()
    search_payload = db.introspect_search_path()
    version = str(version_payload.get("version", ""))
    search_path = str(search_payload.get("search_path", ""))
    role_rows = db.query("SELECT current_user")
    role = str(role_rows[0][0]) if role_rows else ""
    select_rows = db.query("SELECT 1")
    select_one = int(select_rows[0][0]) if select_rows else None
    bg_rows = db.query("SELECT COUNT(*) FROM hde.body_graphs")
    bg_count = int(bg_rows[0][0]) if bg_rows else 0
    return {
        "server_version": version,
        "search_path": search_path,
        "role": role,
        "select_1": select_one,
        "body_graphs_rows": bg_count,
    }


def _provider_snapshot(*, force_pg: bool = False, force_bridge: bool = False) -> Dict[str, Any]:
    updates: Dict[str, str | None] = {}
    if force_pg:
        updates["DB_FORCE_PG"] = "1"
        updates["DB_FORCE_BRIDGE"] = "0"
    elif force_bridge:
        updates["DB_FORCE_BRIDGE"] = "1"
        updates["DB_FORCE_PG"] = "0"
    else:
        updates["DB_FORCE_PG"] = None
        updates["DB_FORCE_BRIDGE"] = None

    with _patched_env(**updates):
        try:
            db = _util.DBAccess.for_current_env(snapshot_path=None)
        except AdapterError as exc:
            return {
                "provider": "psycopg" if force_pg else "bridge",
                "status": "error",
                "error": exc.code,
                "attempts": [
                    {
                        "provider": "psycopg" if force_pg else "bridge",
                        "status": "error",
                        "reason": exc.code,
                    }
                ],
                "capabilities": {},
            }

    capabilities = _collect_capabilities(db)
    return {
        "provider": db.provider_name,
        "status": "ok",
        "attempts": list(db.attempts),
        "capabilities": capabilities,
    }


def _capture_provider_parity(now_iso: str) -> Dict[str, Dict[str, Any]]:
    direct = _provider_snapshot(force_pg=True)
    bridge = _provider_snapshot(force_bridge=True)

    direct_payload = {
        "schema": "v1",
        "captured_at_utc": now_iso,
        **direct,
    }
    bridge_payload = {
        "schema": "v1",
        "captured_at_utc": now_iso,
        **bridge,
    }

    _safe_json(PROVIDER_DB_PATH, direct_payload)
    _safe_json(PROVIDER_BRIDGE_PATH, bridge_payload)

    summary_entries: List[Dict[str, Any]] = []
    keys = set(direct.get("capabilities", {}).keys()) | set(bridge.get("capabilities", {}).keys())
    for key in sorted(keys):
        direct_value = direct.get("capabilities", {}).get(key)
        bridge_value = bridge.get("capabilities", {}).get(key)
        if direct.get("status") != "ok":
            parity = "skip"
            reason = direct.get("error", "direct_unavailable")
        elif bridge.get("status") != "ok":
            parity = "skip"
            reason = bridge.get("error", "bridge_unavailable")
        else:
            parity = "match" if direct_value == bridge_value else "diff"
            reason = None
        entry: Dict[str, Any] = {
            "capability": key,
            "direct": direct_value,
            "bridge": bridge_value,
            "parity": parity,
        }
        if reason:
            entry["reason"] = reason
        summary_entries.append(entry)

    overall = "match"
    if direct.get("status") != "ok" or bridge.get("status") != "ok":
        overall = "partial"
    elif any(item["parity"] != "match" for item in summary_entries):
        overall = "diff"

    summary_payload = {
        "schema": "v1",
        "captured_at_utc": now_iso,
        "overall": overall,
        "attempts": {
            "direct": direct.get("attempts", []),
            "bridge": bridge.get("attempts", []),
        },
        "parity": summary_entries,
    }
    _safe_json(PROVIDER_SUMMARY_PATH, summary_payload)

    return {"direct": direct, "bridge": bridge}


def _capture_bridge_caps(now_iso: str, snapshots: Dict[str, Dict[str, Any]]) -> None:
    providers: List[Dict[str, Any]] = []
    for label in ("direct", "bridge"):
        info = snapshots.get(label, {})
        providers.append(
            {
                "name": info.get("provider", label),
                "status": info.get("status", "unknown"),
                "attempts": info.get("attempts", []),
                "capabilities": info.get("capabilities", {}),
                "error": info.get("error"),
            }
        )
    payload = {
        "schema": "v1",
        "captured_at_utc": now_iso,
        "providers": providers,
    }
    _safe_json(BRIDGE_CAPS_PATH, payload)


def _is_dev_env() -> bool:
    tag = (os.getenv("APP_ENV") or os.getenv("ENGINE_ENV") or "").strip().lower()
    return tag in {"", "dev", "development", "test", "testing"}


def _capture_env_connectivity(now_iso: str, selected_provider: str, attempts: Sequence[Mapping[str, Any]]) -> None:
    if not _is_dev_env():
        print("Skipping env connectivity snapshot outside dev/test", file=sys.stderr)
        return

    dsn_present = bool((os.getenv("DATABASE_URL") or "").strip())
    bridge_present = bool((os.getenv("DB_BRIDGE_URL") or "").strip())
    force_pg = os.getenv("DB_FORCE_PG") == "1"
    force_bridge = os.getenv("DB_FORCE_BRIDGE") == "1"

    if force_bridge:
        selection_order = ["DB_BRIDGE_URL"]
    elif force_pg:
        selection_order = ["DATABASE_URL"]
    else:
        selection_order = ["DATABASE_URL", "DB_BRIDGE_URL"]

    env_checks = [
        {"name": "DATABASE_URL", "value_kind": "dsn_redacted" if dsn_present else "unset"},
        {"name": "DB_BRIDGE_URL", "value_kind": "dsn_redacted" if bridge_present else "unset"},
    ]

    resolver_ok, snapshot = adapter_env.resolve_env_matrix()

    payload = {
        "schema": "v1",
        "captured_at_utc": now_iso,
        "env": (os.getenv("APP_ENV") or os.getenv("ENGINE_ENV") or "unset").strip() or "unset",
        "env_checks": env_checks,
        "selection_order": selection_order,
        "fallback_rules": [
            "Attempt DATABASE_URL first via psycopg when configured.",
            "Fallback to DB_BRIDGE_URL when rails are open or DB_FORCE_BRIDGE=1.",
            "Bridge access remains dev-only unless DB_ALLOW_BRIDGE_IN_PROD=1.",
        ],
        "resolver": {"ok": resolver_ok, "snapshot": snapshot},
        "selection_result": {
            "selected_provider": selected_provider,
            "attempts": list(attempts),
            "dsn_present": dsn_present,
            "bridge_present": bridge_present,
            "rails_open": os.getenv("SAFE_MODE", "1") == "0" and os.getenv("ALLOW_NETWORK", "0") == "1",
        },
        "failure_envelope": adapter_env.MISSING_DB_CONFIG,
    }
    _safe_json(ENV_CONNECTIVITY_PATH, payload)


def main() -> int:
    now_iso = _now_iso()
    db = _util.db_access()

    _capture_search_path(db)
    _capture_fingerprint(db)
    _capture_grants(db)
    observed_partitions = _capture_partition_plan(db)
    _capture_partition_verify(observed_partitions)
    _capture_boundary_view(db)

    parity_snapshots = _capture_provider_parity(now_iso)
    _capture_bridge_caps(now_iso, parity_snapshots)
    _capture_env_connectivity(now_iso, db.provider_name, db.attempts)

    _util.write_path_proof(ADAPTER_SELECTION_PATH)

    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
