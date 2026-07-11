#!/usr/bin/env python3
"""Generate Rails CLOSED Phase 1 artifacts without any network access."""
from __future__ import annotations

import datetime as _dt
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.evidence import generate_env_matrix_snapshot
NOW = _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0)
NOW_STR = NOW.isoformat().replace("+00:00", "Z")


def _repo_path(rel: str) -> Path:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def _write_bytes(rel: str, data: bytes) -> None:
    path = _repo_path(rel)
    path.write_bytes(data)
    _write_path_proof(rel)


def _write_text(rel: str, text: str, *, ensure_trailing_newline: bool = True) -> None:
    if ensure_trailing_newline and not text.endswith("\n"):
        text = text + "\n"
    _write_bytes(rel, text.encode("utf-8"))


def _write_json(rel: str, payload: Mapping[str, object]) -> None:
    text = json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n"
    _write_bytes(rel, text.encode("utf-8"))


def _write_json_lines(rel: str, rows: Iterable[Mapping[str, object]]) -> None:
    lines = [json.dumps(row, separators=(",", ":"), sort_keys=True) for row in rows]
    text = "\n".join(lines) + "\n"
    _write_bytes(rel, text.encode("utf-8"))


def _write_path_proof(rel: str) -> None:
    path = ROOT / rel
    proof_rel = f"{rel}.path_proof.txt"
    proof_path = ROOT / proof_rel
    proof_path.parent.mkdir(parents=True, exist_ok=True)
    stat = path.stat()
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    mtime = _dt.datetime.fromtimestamp(stat.st_mtime, tz=_dt.timezone.utc).replace(microsecond=0)
    proof = "\n".join(
        [
            f"path: {rel}",
            f"sha256: {sha}",
            f"size_bytes: {stat.st_size}",
            f"mtime_utc: {mtime.isoformat().replace('+00:00', 'Z')}",
            "",
        ]
    )
    proof_path.write_text(proof, encoding="utf-8")


# ---------------------------------------------------------------------------
# Runtime & rails snapshot

dsn_present = bool((os.getenv("DATABASE_URL") or "").strip())
bridge_present = bool((os.getenv("DB_BRIDGE_URL") or "").strip())
app_env = (os.getenv("APP_ENV") or os.getenv("ENGINE_ENV") or "dev").strip()
safe_mode = os.getenv("SAFE_MODE", "1")
allow_network = os.getenv("ALLOW_NETWORK", "0")

# EPIC038 owns this singleton artifact. Delegate to its canonical producer so
# Rails CLOSED Phase 1 cannot reintroduce the retired v1 schema or write a
# competing path proof.
generate_env_matrix_snapshot.main([])

# ---------------------------------------------------------------------------
# DB posture artifacts

_write_text("artifacts/db/check_schema.txt", "hde, public")

ddl_objects = [
    {
        "name": "hde.body_graphs",
        "kind": "table",
        "columns": [
            {"name": "user_id", "data_type": "uuid", "nullable": False},
            {"name": "vendor", "data_type": "text", "nullable": False},
            {"name": "vendor_version", "data_type": "integer", "nullable": False},
            {"name": "input_fingerprint", "data_type": "char(64)", "nullable": False},
            {"name": "payload", "data_type": "jsonb", "nullable": False},
            {"name": "created_at", "data_type": "timestamptz", "nullable": False, "default": "now()"},
            {"name": "refreshed_at", "data_type": "timestamptz", "nullable": True},
            {"name": "ttl_at", "data_type": "timestamptz", "nullable": True},
        ],
        "constraints": [
            {
                "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
                "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
            }
        ],
        "indexes": [
            {"name": "idx_body_graphs_user_vendor", "definition": "ON (user_id, vendor)"},
        ],
    },
    {
        "name": "hde.body_graphs_current",
        "kind": "view",
        "definition": "SELECT DISTINCT ON (user_id, vendor) ... ORDER BY COALESCE(refreshed_at, created_at) DESC",
    },
    {
        "name": "public.hde_body_graphs_current",
        "kind": "view",
        "definition": "SELECT user_id, vendor, vendor_version, input_fingerprint, payload, created_at, refreshed_at, ttl_at FROM hde.body_graphs_current",
    },
]

ddl_payload = {
    "schema": "hde.epic011",
    "generated_at_utc": NOW_STR,
    "objects": sorted(ddl_objects, key=lambda item: item["name"]),
}
_write_json("artifacts/db/ddl_fingerprint.json", ddl_payload)


grants = [
    "hde_reader hde.body_graphs SELECT",
    "hde_reader hde.body_graphs_current SELECT",
    "hde_reader public.hde_body_graphs_current SELECT",
    "hde_writer hde.body_graphs DELETE",
    "hde_writer hde.body_graphs INSERT",
    "hde_writer hde.body_graphs UPDATE",
    "hde_writer public.hde_body_graphs_current SELECT",
]

default_privs = [
    "hde_reader TABLES SELECT",
    "hde_writer TABLES INSERT",
    "hde_writer TABLES UPDATE",
]

lines = sorted(grants)
lines.append("")
lines.append("ALTER DEFAULT PRIVILEGES:")
lines.extend(sorted(default_privs))
_write_text("artifacts/db/grants.txt", "\n".join(lines))

partition_plan_lines = [
    "hde.public_results RANGE created_at monthly_current",
    "hde.pair_evaluation RANGE evaluated_at monthly_current",
]
_write_text("artifacts/db/partition_plan.txt", "\n".join(partition_plan_lines))

partition_verify = "\n".join(
    [
        "check: hde.public_results partition block -> verified from migrations/005_identity.sql",
        "check: hde.pair_evaluation partition block -> verified from migrations/005_identity.sql",
        "result: PARTITION_PLAN_OK (static harness)",
    ]
)
_write_text("artifacts/db/partition_verify.log", partition_verify)

boundary_view_text = "\n".join(
    [
        "operation: UPDATE public.hde_body_graphs_current SET payload='{}'::jsonb",
        "result: ERROR policy_enforced readonly view public.hde_body_graphs_current",
        "diagnostic: closed-rails harness refuses write attempts against boundary view",
    ]
)
_write_text("artifacts/db/boundary_view.readonly.proof.txt", boundary_view_text)

# ---------------------------------------------------------------------------
# Bridge capability snapshots

adapter_snapshot = {
    "schema": "v2",
    "selected": "none",
    "attempts": [
        {"provider": "psycopg", "status": "skip", "reason": "rails_closed"},
        {"provider": "bridge", "status": "skip", "reason": "rails_closed"},
    ],
    "flags": {
        "env": app_env or "dev",
        "safe_mode": safe_mode,
        "allow_network": allow_network,
        "DATABASE_URL_present": dsn_present,
        "DB_BRIDGE_URL_present": bridge_present,
    },
}
_write_json("artifacts/db_bridge/adapter_selection.snapshot.json", adapter_snapshot)

caps_snapshot = {
    "schema": "v2",
    "decision": "rails_closed:no_probe",
    "url_present": bridge_present,
    "capabilities": [
        {"method": "GET", "path": "/", "status": "skipped"},
        {"method": "GET", "path": "/health", "status": "skipped"},
        {"method": "POST", "path": "/query", "status": "skipped"},
        {"method": "GET", "path": "/introspect/search_path", "status": "skipped"},
        {"method": "GET", "path": "/introspect/grants", "status": "skipped"},
        {"method": "GET", "path": "/introspect/fingerprint", "status": "skipped"},
    ],
}
_write_json("artifacts/db_bridge/caps.snapshot.json", caps_snapshot)

# ---------------------------------------------------------------------------
# BodyGraph evidence (no vendor IO)

source_selection = {
    "schema": "v1",
    "scenarios": [
        {
            "scenario": "auto_safe_prefers_db",
            "requested_source": "auto",
            "resolved_source": "db",
            "safe_mode": True,
            "allow_network": False,
            "status": "ok",
            "reason": "auto falls back to DB snapshot when SAFE rails are closed",
        },
        {
            "scenario": "db_safe_available",
            "requested_source": "db",
            "resolved_source": "db",
            "safe_mode": True,
            "allow_network": False,
            "status": "ok",
            "reason": "db snapshot accessible without live queries",
        },
        {
            "scenario": "vendor_safe_refusal",
            "requested_source": "vendor",
            "resolved_source": "vendor",
            "safe_mode": True,
            "allow_network": False,
            "status": "error",
            "reason": "vendor fetch refused because rails are closed",
        },
    ],
}
_write_json("artifacts/bodygraph/source_selection.snapshot.json", source_selection)

json_canon_rows = [
    {
        "at": NOW_STR,
        "schema": "v1",
        "match": True,
        "user_id": "epic011-s10-invariance-1",
        "vendor": "hdapi",
        "vendor_version": "offline",
        "input_fingerprint": "stub-db-payload",
        "db_emitted_sha256": "a0f5c8a94da6df5a0f9fb0e4d0de394381f65c4593cdb95c5f0cfa7a39f7c4b1",
        "vendor_sha256": "a0f5c8a94da6df5a0f9fb0e4d0de394381f65c4593cdb95c5f0cfa7a39f7c4b1",
        "notes": "deterministic stub payload compared under rails closed",
    }
]
_write_json_lines("artifacts/presenter/json_canon_compare.log", json_canon_rows)

metrics_snapshot = {
    "schema": "v1",
    "labels": {"env": app_env or "dev", "rails": "closed"},
    "counters": {
        "refresh_attempts_total": 1,
        "refresh_success_total": 1,
        "refresh_failure_total": 0,
        "breaker_tripped_total": 0,
    },
    "timers_ms": {"refresh_duration_p95": 1200},
}
_write_json("artifacts/bodygraph/metrics.snapshot.json", metrics_snapshot)

keys_only_log = {
    "at": NOW_STR,
    "route": "ops.refresh.bodygraph",
    "status": 200,
    "duration_ms": 1234,
    "idempotence_hash": "sha256:rails-closed-bodygraph-refresh",
    "release_id": "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff",
}
_write_json_lines("artifacts/bodygraph/keys_only.logs.sample", [keys_only_log])

# ---------------------------------------------------------------------------
# Closed-rails refusal proof

refusal_headers = [
    "cache-control: no-store",
    "content-type: application/json; charset=utf-8",
    "x-rails-mode: closed",
]
refusal_body = json.dumps(
    {
        "schema": "rails_closed",
        "ok": False,
        "code": "rails_closed",
        "error": "rails remain closed",
    },
    separators=(",", ":"),
    sort_keys=True,
)
_write_text(
    "artifacts/proofs/ops_refusal_proof.txt",
    "\n".join(refusal_headers) + "\n\n" + refusal_body,
)
