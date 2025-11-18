#!/usr/bin/env python3
"""Capture EPIC011 DB posture, provider parity, and env connectivity evidence."""
from __future__ import annotations

import contextlib
import datetime as dt
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter import db_access as resolver
from engine.db.errors import AdapterError

from scripts.db import _util
DEV_TAGS = {"", "dev", "development", "test", "testing"}
FINGERPRINT_OBJECTS: tuple[tuple[str, str], ...] = (
    ("hde.body_graphs", "table"),
    ("hde.body_graphs_current", "view"),
    ("public.hde_body_graphs_current", "view"),
)
GRANT_OBJECTS = {name for name, _ in FINGERPRINT_OBJECTS}
PARTITION_TABLES = ("hde.public_results", "hde.pair_evaluation")
FALLBACK_RULES = (
    "Attempt DATABASE_URL first via psycopg with search_path pin and health check",
    "If DATABASE_URL is missing or psycopg health fails, try HTTPS DB_BRIDGE_URL",
    "Bridge path is allowed only when rails are open or DB_FORCE_BRIDGE=1",
)


@dataclass(frozen=True)
class CapabilityProbe:
    name: str
    func: Callable[["DBAccess"], Any]


def _now() -> dt.datetime:
    return dt.datetime.now(tz=dt.timezone.utc).replace(microsecond=0)


def _iso(ts: dt.datetime) -> str:
    return ts.isoformat().replace("+00:00", "Z")


def _artifact_path(rel: str) -> Path:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _write_path_proof(path: Path) -> None:
    stat = path.stat()
    sha = _sha256(path.read_bytes())
    mtime = dt.datetime.fromtimestamp(stat.st_mtime, tz=dt.timezone.utc).replace(microsecond=0)
    proof = "\n".join(
        (
            f"path: {path.relative_to(ROOT)}",
            f"sha256: {sha}",
            f"size_bytes: {stat.st_size}",
            f"mtime_utc: {_iso(mtime)}",
            "",
        )
    )
    proof_path = Path(f"{path}.path_proof.txt")
    proof_path.write_text(proof, encoding="utf-8")


def _write_bytes(rel: str, data: bytes) -> None:
    path = _artifact_path(rel)
    path.write_bytes(data)
    _write_path_proof(path)


def _write_text(rel: str, text: str) -> None:
    if not text.endswith("\n"):
        text = text + "\n"
    _write_bytes(rel, text.encode("utf-8"))


def _write_json(rel: str, payload: Mapping[str, Any]) -> None:
    text = json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n"
    _write_bytes(rel, text.encode("utf-8"))


def _sha256(data: bytes) -> str:
    import hashlib

    return hashlib.sha256(data).hexdigest()


def _env_tag() -> str:
    value = (os.getenv("APP_ENV") or os.getenv("ENGINE_ENV") or "").strip().lower()
    return value


def _rails_open() -> bool:
    return os.getenv("SAFE_MODE", "1") == "0" and os.getenv("ALLOW_NETWORK", "0") == "1"


def _search_path_value(db: "DBAccess") -> str:
    payload = db.introspect_search_path()
    if isinstance(payload, Mapping):
        value = str(payload.get("search_path", ""))
    else:
        value = str(payload)
    return value.strip()


def _fingerprint_objects(db: "DBAccess") -> List[Dict[str, Any]]:
    payload = db.introspect_fingerprint() or {}
    objects_raw = payload.get("objects") if isinstance(payload, Mapping) else None
    lookup: Dict[str, Mapping[str, Any]] = {}
    if isinstance(objects_raw, Mapping):
        lookup = {str(key): value for key, value in objects_raw.items() if isinstance(value, Mapping)}
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
            record["columns"] = entry.get("columns", []) if isinstance(entry, Mapping) else []
            record["constraints"] = entry.get("constraints", []) if isinstance(entry, Mapping) else []
        else:
            record["definition"] = entry.get("definition", "") if isinstance(entry, Mapping) else ""
        normalized.append(record)
    return normalized


def _grant_lines(db: "DBAccess") -> List[str]:
    payload = db.introspect("grants") or {}
    grants = payload.get("grants", []) if isinstance(payload, Mapping) else []
    lines: List[str] = []
    for entry in grants:
        if isinstance(entry, Mapping):
            grantee = str(entry.get("role") or entry.get("grantee") or "").strip()
            obj = str(entry.get("object") or entry.get("table") or "").strip()
            priv = str(entry.get("priv") or entry.get("privilege") or entry.get("privilege_type") or "").strip()
        else:
            try:
                grantee, obj, priv = entry
            except Exception:
                continue
            grantee = str(grantee).strip()
            obj = str(obj).strip()
            priv = str(priv).strip()
        if not (grantee and obj and priv):
            continue
        if obj not in GRANT_OBJECTS:
            continue
        lines.append(f"{grantee} {obj} {priv}")
    deduped = sorted(dict.fromkeys(lines))
    return deduped


def _strip_strategy_prefix(raw: str) -> str:
    parts = (raw or "").split(maxsplit=1)
    if len(parts) == 2:
        return parts[1]
    return raw or ""


def _partition_plan(db: "DBAccess") -> tuple[List[str], List[str]]:
    sql = """
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
        WHERE (ns.nspname = 'hde' AND c.relname IN ('public_results', 'pair_evaluation'))
        ORDER BY table_name
    """
    rows = db.query(sql)
    if not rows:
        raise SystemExit("partition plan query returned no rows")
    plan_lines: List[str] = []
    observed: List[str] = []
    strategy_lookup = {"r": "RANGE", "R": "RANGE", "l": "LIST", "L": "LIST", "h": "HASH", "H": "HASH"}
    for table_name, strategy, raw_key in rows:
        name = str(table_name)
        observed.append(name)
        strategy_label = strategy_lookup.get(str(strategy), str(strategy))
        key_expr = _strip_strategy_prefix(str(raw_key or "")).strip()
        if key_expr and not key_expr.startswith("("):
            key_expr = f"({key_expr})"
        plan_lines.append(f"{name} {strategy_label} {key_expr if key_expr else ''}".strip())
    return plan_lines, observed


def _partition_verify_lines(observed: Sequence[str]) -> List[str]:
    expected = list(PARTITION_TABLES)
    observed_sorted = sorted(observed)
    missing = [name for name in expected if name not in observed_sorted]
    extra = [name for name in observed_sorted if name not in expected]
    if missing or extra:
        mismatch = ", ".join(
            filter(
                None,
                (
                    f"missing: {', '.join(missing)}" if missing else "",
                    f"extra: {', '.join(extra)}" if extra else "",
                ),
            )
        )
        raise SystemExit(f"partition plan mismatch: {mismatch}")
    return [
        f"expected: {', '.join(expected)}",
        f"observed: {', '.join(observed_sorted)}",
        "result: PARTITION_PLAN_OK",
    ]


def _boundary_view_lines(db: "DBAccess") -> List[str]:
    sql = """
        SELECT table_schema, table_name, is_updatable, is_insertable_into, is_trigger_updatable
        FROM information_schema.views
        WHERE (table_schema = 'hde' AND table_name = 'body_graphs_current')
           OR (table_schema = 'public' AND table_name = 'hde_body_graphs_current')
        ORDER BY table_schema, table_name
    """
    rows = db.query(sql)
    if len(rows) != len(FINGERPRINT_OBJECTS) - 1:
        raise SystemExit("unexpected boundary view metadata result set")
    lines: List[str] = []
    for schema, name, updatable, insertable, trigger_updatable in rows:
        lines.append(f"view: {schema}.{name}")
        lines.append(f"is_updatable: {updatable}")
        lines.append(f"is_insertable_into: {insertable}")
        lines.append(f"is_trigger_updatable: {trigger_updatable}")
        lines.append("")
    if lines and lines[-1] == "":
        lines.pop()
    return lines


def _select_one(db: "DBAccess") -> int:
    rows = db.query("SELECT 1::int")
    if not rows:
        raise SystemExit("SELECT 1 returned no rows")
    return int(rows[0][0])


CAPABILITIES: tuple[CapabilityProbe, ...] = (
    CapabilityProbe("search_path", lambda db: _search_path_value(db)),
    CapabilityProbe("ddl_fingerprint", lambda db: _fingerprint_objects(db)),
    CapabilityProbe("grants", lambda db: _grant_lines(db)),
    CapabilityProbe("select_one", _select_one),
)


@contextlib.contextmanager
def _temporary_env(overrides: Mapping[str, str | None]):
    original: Dict[str, str | None] = {}
    try:
        for key, value in overrides.items():
            original[key] = os.environ.get(key)
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value
        yield
    finally:
        for key, value in original.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _capture_provider(label: str, captured_at: str) -> Dict[str, Any]:
    if label not in {"direct", "bridge"}:
        raise ValueError(f"unknown provider label: {label}")
    overrides: Dict[str, str | None] = {}
    provider_name = "psycopg" if label == "direct" else "bridge"
    if label == "direct":
        overrides["DB_FORCE_PG"] = "1"
        overrides["DB_FORCE_BRIDGE"] = None
    else:
        overrides["DB_FORCE_BRIDGE"] = "1"
        overrides["DB_FORCE_PG"] = None
    capture: Dict[str, Any] = {
        "schema": "v1",
        "provider": label,
        "captured_at_utc": captured_at,
    }
    with _temporary_env(overrides):
        try:
            db = _util.DBAccess.for_current_env(snapshot_path=None)
        except AdapterError as exc:
            capture.update(
                {
                    "status": "error",
                    "reason": exc.code,
                    "attempts": [
                        {"provider": provider_name, "status": "error", "reason": exc.code}
                    ],
                }
            )
            return capture
    capture["status"] = "ok"
    capture["provider_name"] = provider_name
    capture["attempts"] = list(db.attempts)
    results: List[Dict[str, Any]] = []
    for probe in CAPABILITIES:
        try:
            value = probe.func(db)
        except AdapterError as exc:
            results.append({"name": probe.name, "status": "error", "reason": exc.code})
        except Exception as exc:  # pragma: no cover - unexpected failure surface
            results.append({"name": probe.name, "status": "error", "reason": "unexpected_error", "detail": str(exc)})
        else:
            results.append({"name": probe.name, "status": "ok", "value": value})
    capture["capabilities"] = results
    return capture


def _cap_map(capture: Mapping[str, Any]) -> Dict[str, Mapping[str, Any]]:
    entries = capture.get("capabilities", []) if isinstance(capture, Mapping) else []
    return {entry.get("name"): entry for entry in entries if isinstance(entry, Mapping) and entry.get("name")}


def _canonical_value(value: Any) -> str:
    return json.dumps(value, separators=(",", ":"), sort_keys=True)


def _parity_summary(
    direct_capture: Mapping[str, Any],
    bridge_capture: Mapping[str, Any],
    attempts: Sequence[Mapping[str, Any]],
    selected: str,
    env_tag: str,
    captured_at: str,
) -> Dict[str, Any]:
    direct_caps = _cap_map(direct_capture)
    bridge_caps = _cap_map(bridge_capture)
    capability_names = sorted(set(direct_caps) | set(bridge_caps))
    summary_caps: List[Dict[str, Any]] = []
    for name in capability_names:
        direct_entry = direct_caps.get(name)
        bridge_entry = bridge_caps.get(name)
        entry: Dict[str, Any] = {"name": name}
        if direct_entry:
            entry["direct"] = {k: v for k, v in direct_entry.items() if k in {"status", "value", "reason"}}
        else:
            entry["direct"] = {"status": "missing"}
        if bridge_entry:
            entry["bridge"] = {k: v for k, v in bridge_entry.items() if k in {"status", "value", "reason"}}
        else:
            entry["bridge"] = {"status": "missing"}
        parity = "skip"
        reason = "direct_unavailable"
        if direct_entry and direct_entry.get("status") == "ok" and bridge_entry and bridge_entry.get("status") == "ok":
            parity = "match" if _canonical_value(direct_entry.get("value")) == _canonical_value(bridge_entry.get("value")) else "diff"
            reason = "" if parity == "match" else "value_mismatch"
        entry["parity"] = parity
        if reason:
            entry["parity_reason"] = reason
        summary_caps.append(entry)
    return {
        "schema": "v1",
        "captured_at_utc": captured_at,
        "environment": env_tag or "unset",
        "selected": selected,
        "attempts": list(attempts),
        "capabilities": summary_caps,
    }


def _caps_snapshot(direct_capture: Mapping[str, Any], bridge_capture: Mapping[str, Any], captured_at: str) -> Dict[str, Any]:
    providers: List[Dict[str, Any]] = []
    for capture in (direct_capture, bridge_capture):
        entry: Dict[str, Any] = {
            "name": capture.get("provider"),
            "status": capture.get("status"),
        }
        if capture.get("reason"):
            entry["reason"] = capture.get("reason")
        capabilities = []
        for cap in capture.get("capabilities", []):
            if isinstance(cap, Mapping):
                capabilities.append({"name": cap.get("name"), "status": cap.get("status")})
        if capabilities:
            entry["capabilities"] = capabilities
        providers.append(entry)
    return {
        "schema": "v1",
        "captured_at_utc": captured_at,
        "providers": providers,
    }


def _adapter_snapshot(db: "DBAccess", env_tag: str, captured_at: str) -> Dict[str, Any]:
    return {
        "schema": "v2",
        "captured_at_utc": captured_at,
        "selected": db.provider_name,
        "attempts": list(db.attempts),
        "flags": {
            "env": env_tag or "unset",
            "DATABASE_URL_present": bool(os.getenv("DATABASE_URL")),
            "DB_BRIDGE_URL_present": bool(os.getenv("DB_BRIDGE_URL")),
            "rails_open": _rails_open(),
            "force_pg": os.getenv("DB_FORCE_PG") == "1",
            "force_bridge": os.getenv("DB_FORCE_BRIDGE") == "1",
            "allow_bridge_prod": os.getenv("DB_ALLOW_BRIDGE_IN_PROD") == "1",
        },
    }


def _env_connectivity_payload(env_tag: str, attempts: Sequence[Mapping[str, Any]], selected: str, captured_at: str) -> Dict[str, Any] | None:
    if env_tag not in DEV_TAGS:
        return None
    matrix_ok, snapshot = resolver.resolve_env_matrix()
    env_checks = [
        {
            "name": "DATABASE_URL",
            "value_kind": "dsn_redacted" if (os.getenv("DATABASE_URL") or "").strip() else "unset",
        },
        {
            "name": "DB_BRIDGE_URL",
            "value_kind": "dsn_redacted" if (os.getenv("DB_BRIDGE_URL") or "").strip() else "unset",
        },
    ]
    return {
        "schema": "v2",
        "captured_at_utc": captured_at,
        "environment": env_tag or "unset",
        "dev_only": True,
        "rails_open": _rails_open(),
        "env_checks": env_checks,
        "selection_order": ["DATABASE_URL", "DB_BRIDGE_URL"],
        "fallback_rules": list(FALLBACK_RULES),
        "resolver_ok": matrix_ok,
        "resolver_snapshot": snapshot,
        "final_selection": {"provider": selected, "attempts": list(attempts)},
        "missing_config_envelope": resolver.MISSING_DB_CONFIG,
    }


def _parity_proof(summary: Mapping[str, Any], captured_at: str) -> Dict[str, Any]:
    return {
        "schema": "v2",
        "captured_at_utc": captured_at,
        "environment": summary.get("environment"),
        "rails_open": _rails_open(),
        "attempts": summary.get("attempts", []),
        "selected": summary.get("selected"),
        "capabilities": summary.get("capabilities", []),
    }


def main() -> None:
    env_tag = _env_tag()
    timestamp = _now()
    captured_at = _iso(timestamp)
    db = _util.db_access()

    search_path = _search_path_value(db)
    if search_path != "hde, public":
        raise SystemExit(f"unexpected search_path: {search_path!r}")
    _write_text("artifacts/db/check_schema.txt", search_path)

    fingerprint_objects = _fingerprint_objects(db)
    _write_json(
        "artifacts/db/ddl_fingerprint.json",
        {"schema": "hde", "captured_at_utc": captured_at, "objects": fingerprint_objects},
    )

    grants = _grant_lines(db)
    if not grants:
        raise SystemExit("no grants captured for EPIC011 objects")
    _write_text("artifacts/db/grants.txt", "\n".join(grants))

    plan_lines, observed = _partition_plan(db)
    _write_text("artifacts/db/partition_plan.txt", "\n".join(plan_lines))
    verify_lines = _partition_verify_lines(observed)
    _write_text("artifacts/db/partition_verify.log", "\n".join(verify_lines))

    boundary_lines = _boundary_view_lines(db)
    _write_text("artifacts/db/boundary_view.readonly.proof.txt", "\n".join(boundary_lines))

    direct_capture = _capture_provider("direct", captured_at)
    bridge_capture = _capture_provider("bridge", captured_at)
    _write_json("artifacts/db/provider_parity/direct.json", direct_capture)
    _write_json("artifacts/db/provider_parity/bridge.json", bridge_capture)

    summary = _parity_summary(direct_capture, bridge_capture, db.attempts, db.provider_name, env_tag, captured_at)
    _write_json("artifacts/db/provider_parity/summary.json", summary)
    _write_json("artifacts/db_bridge/caps.snapshot.json", _caps_snapshot(direct_capture, bridge_capture, captured_at))
    _write_json("artifacts/db_bridge/adapter_selection.snapshot.json", _adapter_snapshot(db, env_tag, captured_at))
    _write_json("artifacts/db_bridge/provider_parity.proof.json", _parity_proof(summary, captured_at))

    env_payload = _env_connectivity_payload(env_tag, db.attempts, db.provider_name, captured_at)
    if env_payload:
        _write_json("artifacts/runtime/env_connectivity.snapshot.json", env_payload)


if __name__ == "__main__":
    main()
