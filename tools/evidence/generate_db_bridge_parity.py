#!/usr/bin/env python3
"""Generate deterministic HDE-EPIC032 PR-03 DB bridge evidence."""
from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.db.adapter import DBAccess, Statement
from engine.db.errors import AdapterError, PrimaryUnavailable
from engine.db.providers.bridge_provider import BridgeProvider
from engine.runtime.determinism_env import ensure_determinism_env

ADAPTER_SELECTION_PATH = ROOT / "artifacts/db_bridge/adapter_selection.snapshot.json"
PROVIDER_PARITY_PATH = ROOT / "artifacts/db_bridge/provider_parity.proof.json"
ENV_CONNECTIVITY_PATH = ROOT / "artifacts/runtime/env_connectivity.snapshot.json"
NONDEV_FAILURE_PATH = ROOT / "artifacts/runtime/env_connectivity.nondev_failure.json"

PRODUCED_AT_UTC = "2026-05-18T00:00:00Z"
REDACTED_DSN = "redacted_database_url_present"
REDACTED_BRIDGE = "https://db-bridge.invalid"


class HarnessProvider:
    """Deterministic provider used by the PR-03 evidence harness."""

    def __init__(self, name: str, *, fail_health: bool = False):
        self.name = name
        self._fail_health = fail_health

    def health(self) -> None:
        if self._fail_health:
            raise PrimaryUnavailable("primary_connect_failed", code="primary_connect_failed")

    def query(self, sql: str, params: Any = None) -> list[Sequence[Any]]:
        normalized = " ".join(sql.split()).lower()
        if normalized == "select 1":
            return [(1,)]
        if "current_setting('server_version')" in normalized:
            return [("harness-postgres",)]
        if normalized == "show search_path":
            return [("hde, public",)]
        return []

    def exec(self, sql: str, params: Any = None) -> None:
        return None

    def tx(self, statements: Sequence[Statement]) -> list[Sequence[Any] | None]:
        results: list[Sequence[Any] | None] = []
        for statement in statements:
            results.append(self.query(statement.sql, statement.params) if statement.fetch else None)
        return results

    def introspect(self, kind: str) -> Any:
        if kind == "search_path":
            return {"status": "ok", "search_path": "hde, public"}
        if kind == "version":
            return {"status": "ok", "version": "harness-postgres"}
        if kind == "fingerprint":
            return {
                "objects": {
                    "hde.body_graphs": {
                        "columns": [
                            {"data_type": "uuid", "name": "user_id", "nullable": False},
                            {"data_type": "text", "name": "vendor", "nullable": False},
                        ],
                        "constraints": [],
                    },
                    "hde.body_graphs_current": {"definition": "select deterministic"},
                    "public.hde_body_graphs_current": {"definition": "select deterministic"},
                },
                "schema": "hde",
                "status": "ok",
                "version": 1,
            }
        if kind == "grants":
            return {
                "default_privileges": ["(none)"],
                "flags": {"rolcreatedb": False, "rolcreaterole": False, "rolsuper": False},
                "grants": [("reader", "hde.body_graphs", "SELECT")],
                "status": "ok",
            }
        raise AssertionError(kind)


def _canonical_json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, separators=(",", ":"), sort_keys=True) + "\n").encode("utf-8")


def _write_or_check(path: Path, payload: object, *, check: bool) -> None:
    data = _canonical_json_bytes(payload)
    if check:
        if not path.exists():
            raise SystemExit(f"MISSING:{path.relative_to(ROOT).as_posix()}")
        existing = path.read_bytes()
        if existing != data:
            raise SystemExit(f"STALE:{path.relative_to(ROOT).as_posix()}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)


@contextmanager
def _patched_env(values: Mapping[str, str]):
    keys = set(values) | {
        "APP_ENV",
        "ENGINE_ENV",
        "DATABASE_URL",
        "DB_BRIDGE_URL",
        "DB_FORCE_PG",
        "DB_FORCE_BRIDGE",
        "DB_ALLOW_BRIDGE_IN_PROD",
    }
    old = {key: os.environ.get(key) for key in keys}
    try:
        for key in keys:
            os.environ.pop(key, None)
        for key, value in values.items():
            os.environ[key] = value
        yield
    finally:
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _run_dev_fallback_adapter(*, snapshot_path: Path = ADAPTER_SELECTION_PATH) -> DBAccess:
    with _patched_env(
        {
            "APP_ENV": "dev",
            "DATABASE_URL": REDACTED_DSN,
            "DB_BRIDGE_URL": REDACTED_BRIDGE,
        }
    ):
        return DBAccess.for_current_env(
            snapshot_path=str(snapshot_path),
            psycopg_factory=lambda _dsn: HarnessProvider("psycopg", fail_health=True),
            bridge_factory=lambda _url: HarnessProvider("bridge"),
        )


def _selection_payload(db: DBAccess) -> dict[str, Any]:
    attempts = list(db.attempts)
    return {
        "attempts": attempts,
        "provider": db.provider_name,
        "selection_order": [attempt["provider"] for attempt in attempts if isinstance(attempt, dict) and "provider" in attempt],
    }




def _selection_order_from_attempts(attempts: Any) -> list[str]:
    if not isinstance(attempts, list):
        return []
    return [
        attempt["provider"]
        for attempt in attempts
        if isinstance(attempt, dict) and "provider" in attempt
    ]


def _ensure_structural_selection_order(payload: dict[str, Any]) -> dict[str, Any]:
    derived = _selection_order_from_attempts(payload.get("attempts"))
    observed = payload.get("selection_order")
    if observed is None:
        payload["selection_order"] = derived
        return payload
    if not isinstance(observed, list):
        raise SystemExit("SELECTION_ORDER_NOT_ARRAY")
    if observed != derived:
        raise SystemExit(f"SELECTION_ORDER_MISMATCH:{observed!r}:{derived!r}")
    return payload

def _bridge_capability_payload() -> dict[str, Any]:
    required_methods = ["health", "query", "exec", "tx", "introspect"]
    provider = BridgeProvider(REDACTED_BRIDGE, request=lambda *_args: None)  # type: ignore[arg-type]
    return {
        "capability_status": "ok",
        "https_required": True,
        "provider": provider.name,
        "required_methods": [
            {"name": name, "present": callable(getattr(provider, name, None))}
            for name in required_methods
        ],
        "proof_label": "DB_BRIDGE_CAPS_OK",
        "proof_label_type": "non_token",
    }


def _normalise(value: Any) -> Any:
    if isinstance(value, tuple):
        return [_normalise(item) for item in value]
    if isinstance(value, list):
        return [_normalise(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _normalise(val) for key, val in sorted(value.items())}
    return value


def _compare_case(name: str, direct: DBAccess, bridge: DBAccess) -> dict[str, Any]:
    if name == "select_one":
        direct_value = direct.query("SELECT 1")
        bridge_value = bridge.query("SELECT 1")
    elif name == "search_path":
        direct_value = direct.introspect_search_path()
        bridge_value = bridge.introspect_search_path()
    elif name == "version":
        direct_value = direct.introspect_version()
        bridge_value = bridge.introspect_version()
    elif name == "tx_select_one":
        direct_value = direct.tx([Statement(sql="SELECT 1", fetch=True)])
        bridge_value = bridge.tx([Statement(sql="SELECT 1", fetch=True)])
    else:  # pragma: no cover - corpus is local and fixed
        raise AssertionError(name)

    direct_norm = _normalise(direct_value)
    bridge_norm = _normalise(bridge_value)
    return {
        "bridge": {"status": "ok", "value": bridge_norm},
        "direct": {"status": "ok", "value": direct_norm},
        "name": name,
        "parity": "pass" if direct_norm == bridge_norm else "fail",
    }


def _deterministic_harness_payload() -> dict[str, Any]:
    direct = DBAccess(HarnessProvider("psycopg"))
    bridge = DBAccess(HarnessProvider("bridge"))
    cases = [_compare_case(name, direct, bridge) for name in ("select_one", "search_path", "version", "tx_select_one")]
    return {
        "cases": cases,
        "corpus": "hde_epic032_pr03_canonical_corpus_v1",
        "status": "pass" if all(case["parity"] == "pass" for case in cases) else "fail",
    }


def _live_unavailable_capabilities() -> list[dict[str, Any]]:
    return [
        {
            "bridge": {"status": "not_exercised", "reason": "closed_rails_no_secret_backed_bridge"},
            "direct": {"status": "missing", "reason": "database_url_not_used_by_coding_agent"},
            "name": name,
            "parity": "skip",
            "parity_reason": "direct_unavailable",
        }
        for name in ("select_one", "search_path", "version", "tx_select_one")
    ]


def _env_connectivity_payload(db: DBAccess) -> dict[str, Any]:
    selection = _selection_payload(db)
    return {
        "captured_at_utc": PRODUCED_AT_UTC,
        "dev_only": True,
        "env_checks": [
            {"name": "DATABASE_URL", "value_kind": "present_redacted"},
            {"name": "DB_BRIDGE_URL", "value_kind": "present_redacted"},
            {"name": "APP_ENV", "value_kind": "dev"},
        ],
        "environment": "dev",
        "fallback_rules": [
            "DATABASE_URL is attempted first through DBAccess and psycopg health",
            "dev/test/local may fall back to HTTPS DB_BRIDGE_URL through DBAccess when psycopg is unusable",
            "production bridge remains guarded unless DB_ALLOW_BRIDGE_IN_PROD=1",
        ],
        "final_selection": selection,
        "missing_config_envelope": {
            "code": "missing_db_config",
            "error": "database configuration not found",
            "ok": False,
            "schema": "v1",
        },
        "proof_labels": [{"name": "DEV_DB_BRIDGE_FALLBACK_OK", "type": "acceptance_token"}],
        "rails_open": False,
        "schema": "v2",
        "selection_order": ["DATABASE_URL", "DB_BRIDGE_URL"],
        "selection_result": selection,
    }


def _provider_parity_payload(db: DBAccess) -> dict[str, Any]:
    return {
        "attempts": list(db.attempts),
        "bridge_capability": _bridge_capability_payload(),
        "capabilities": _live_unavailable_capabilities(),
        "captured_at_utc": PRODUCED_AT_UTC,
        "deterministic_harness": _deterministic_harness_payload(),
        "environment": "dev",
        "live_provider_parity": {
            "direct_provider_rows": "unavailable",
            "parity_status": "unavailable",
            "reason": "coding_agent_closed_rails_no_secret_backed_database_url",
        },
        "proof_labels": [
            {"name": "DB_PROVIDER_PARITY_OK", "status": "not_claimed", "type": "non_token"},
            {"name": "DB_BRIDGE_CAPS_OK", "status": "proven_by_bridge_capability", "type": "non_token"},
        ],
        "rails_open": False,
        "schema": "v2",
        "selected": db.provider_name,
    }


def _nondev_total_failure_payload() -> dict[str, Any]:
    with tempfile.TemporaryDirectory() as tmpdir:
        snapshot_path = Path(tmpdir) / "nondev.adapter_selection.snapshot.json"
        with _patched_env({"APP_ENV": "stage"}):
            try:
                DBAccess.for_current_env(
                    snapshot_path=str(snapshot_path),
                    psycopg_factory=lambda _dsn: HarnessProvider("psycopg"),
                    bridge_factory=lambda _url: HarnessProvider("bridge"),
                )
            except AdapterError as exc:
                err = {"class": exc.__class__.__name__, "code": exc.code}
                if err["class"] != "BridgeUnavailable" or err["code"] != "missing_bridge_url":
                    raise SystemExit(f"NONDEV_TYPED_ERROR_UNEXPECTED:{err['class']}:{err['code']}")
            else:
                raise SystemExit("NONDEV_TYPED_ERROR_UNEXPECTED:unexpected_success")

            if not snapshot_path.exists():
                raise SystemExit("NONDEV_SELECTION_SNAPSHOT_MISSING")
            attempts = json.loads(snapshot_path.read_text(encoding="utf-8")).get("attempts", [])

    expected_attempts = [
        {"provider": "psycopg", "status": "skip", "reason": "missing_database_url"},
        {"provider": "bridge", "status": "skip", "reason": "missing_bridge_url"},
    ]
    if attempts != expected_attempts:
        raise SystemExit(f"NONDEV_SELECTION_ORDER_UNEXPECTED:{attempts}")

    return {
        "schema": "v1",
        "captured_at_utc": PRODUCED_AT_UTC,
        "environment": "stage",
        "selection_attempts": attempts,
        "selection_order": [attempt["provider"] for attempt in attempts],
        "total_failure": {"ok": False, "typed_error": err},
        "public_failure_posture": {"numeric_free": True, "secret_free": True, "raw_stack_trace": False},
        "probe_posture": {"no_proactive_probes": True, "adapter_path_only": True},
        "secret_posture": "presence_only",
    }

def generate(*, check: bool = False) -> None:
    ensure_determinism_env()
    if check:
        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_adapter = Path(tmpdir) / "adapter_selection.snapshot.json"
            db = _run_dev_fallback_adapter(snapshot_path=tmp_adapter)
            adapter_payload = json.loads(tmp_adapter.read_text(encoding="utf-8"))
    else:
        db = _run_dev_fallback_adapter(snapshot_path=ADAPTER_SELECTION_PATH)
        adapter_payload = json.loads(ADAPTER_SELECTION_PATH.read_text(encoding="utf-8"))
    adapter_payload = _ensure_structural_selection_order(adapter_payload)
    env_payload = _env_connectivity_payload(db)
    parity_payload = _provider_parity_payload(db)

    _write_or_check(ADAPTER_SELECTION_PATH, adapter_payload, check=check)
    _write_or_check(ENV_CONNECTIVITY_PATH, env_payload, check=check)
    nondev_payload = _nondev_total_failure_payload()

    _write_or_check(PROVIDER_PARITY_PATH, parity_payload, check=check)
    _write_or_check(NONDEV_FAILURE_PATH, nondev_payload, check=check)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated evidence bytes differ")
    args = parser.parse_args(list(argv) if argv is not None else None)
    generate(check=args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
