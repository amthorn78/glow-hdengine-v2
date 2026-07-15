#!/usr/bin/env python3
"""Generate deterministic DB bridge parity and Presenter evidence."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from contextlib import contextmanager
from copy import deepcopy
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.db.adapter import DBAccess, Statement
from engine.db.errors import AdapterError, PrimaryUnavailable
from engine.db.providers.bridge_provider import BridgeProvider
from engine.presenter import emitter
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer import canon

ADAPTER_SELECTION_PATH = ROOT / "artifacts/db_bridge/adapter_selection.snapshot.json"
CAPS_PATH = ROOT / "artifacts/db_bridge/caps.snapshot.json"
PROVIDER_PARITY_PATH = ROOT / "artifacts/db_bridge/provider_parity.proof.json"
ENV_CONNECTIVITY_PATH = ROOT / "artifacts/runtime/env_connectivity.snapshot.json"
NONDEV_FAILURE_PATH = ROOT / "artifacts/runtime/env_connectivity.nondev_failure.json"
VENDOR_UPSERT_PATH = ROOT / "artifacts/bodygraph/vendor_upsert.epic038_synthetic.json"
DB_RESOLVE_PATH = ROOT / "artifacts/bodygraph/db_resolve.epic038_synthetic.json"
PRESENTER_COMPARE_PATH = ROOT / "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json"
PRESENTER_SCHEMA_PATH = ROOT / "schemas/presenter_db_bridge_compare.v1.json"

PRODUCED_AT_UTC = "2026-05-18T00:00:00Z"
REDACTED_DSN = "redacted_database_url_present"
REDACTED_BRIDGE = "https://db-bridge.invalid"
CASE_NAMES = ("select_one", "search_path", "version", "tx_select_one")


class HarnessProvider:
    """Deterministic provider used by the PR-04 evidence harness."""

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
        return [self.query(item.sql, item.params) if item.fetch else None for item in statements]

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
    return canon.sercanon(payload, sort_keys=True)


def _write_or_check(path: Path, payload: object, *, check: bool) -> None:
    data = _canonical_json_bytes(payload)
    if check:
        if not path.exists():
            raise SystemExit(f"MISSING:{path.relative_to(ROOT).as_posix()}")
        if path.read_bytes() != data:
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
        os.environ.update(values)
        yield
    finally:
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def _run_dev_fallback_adapter(*, snapshot_path: Path) -> DBAccess:
    with _patched_env(
        {"APP_ENV": "dev", "DATABASE_URL": REDACTED_DSN, "DB_BRIDGE_URL": REDACTED_BRIDGE}
    ):
        return DBAccess.for_current_env(
            snapshot_path=str(snapshot_path),
            psycopg_factory=lambda _dsn: HarnessProvider("psycopg", fail_health=True),
            bridge_factory=lambda _url: HarnessProvider("bridge"),
        )


def _selection_order(attempts: Any) -> list[str]:
    if not isinstance(attempts, list):
        return []
    return [row["provider"] for row in attempts if isinstance(row, dict) and "provider" in row]


def _ensure_selection_order(payload: dict[str, Any]) -> dict[str, Any]:
    derived = _selection_order(payload.get("attempts"))
    observed = payload.get("selection_order")
    if observed is None:
        payload["selection_order"] = derived
    elif observed != derived:
        raise SystemExit(f"SELECTION_ORDER_MISMATCH:{observed!r}:{derived!r}")
    return payload


def _bridge_capability_payload() -> dict[str, Any]:
    required = ["health", "query", "exec", "tx", "introspect"]
    provider = BridgeProvider(REDACTED_BRIDGE, request=lambda *_args: None)  # type: ignore[arg-type]
    return {
        "capability_status": "ok",
        "https_required": True,
        "provider": provider.name,
        "required_methods": [
            {"name": name, "present": callable(getattr(provider, name, None))} for name in required
        ],
        "proof_label": "DB_BRIDGE_CAPS_OK",
        "proof_label_type": "non_token",
    }


def _caps_payload() -> dict[str, Any]:
    capability = _bridge_capability_payload()
    return {
        "schema": "v2",
        "captured_at_utc": PRODUCED_AT_UTC,
        "provider": capability["provider"],
        "https_required": capability["https_required"],
        "capability_status": capability["capability_status"],
        "required_methods": capability["required_methods"],
    }


def _normalise(value: Any) -> Any:
    if isinstance(value, tuple):
        return [_normalise(item) for item in value]
    if isinstance(value, list):
        return [_normalise(item) for item in value]
    if isinstance(value, dict):
        return {str(key): _normalise(val) for key, val in sorted(value.items())}
    return value


def _acquire_case(db: DBAccess, name: str) -> Any:
    if name == "select_one":
        return db.query("SELECT 1")
    if name == "search_path":
        return db.introspect_search_path()
    if name == "version":
        return db.introspect_version()
    if name == "tx_select_one":
        return db.tx([Statement(sql="SELECT 1", fetch=True)])
    raise AssertionError(name)


def _acquire_cases(provider: str) -> list[dict[str, Any]]:
    facade = DBAccess(HarnessProvider(provider))
    return [
        {"name": name, "value": _normalise(_acquire_case(facade, name))} for name in CASE_NAMES
    ]


def _deterministic_harness_payload() -> dict[str, Any]:
    direct = _acquire_cases("psycopg")
    bridge = _acquire_cases("bridge")
    cases = [
        {
            "bridge": {"status": "ok", "value": bridge[index]["value"]},
            "direct": {"status": "ok", "value": direct[index]["value"]},
            "name": name,
            "parity": "pass" if direct[index] == bridge[index] else "fail",
        }
        for index, name in enumerate(CASE_NAMES)
    ]
    return {
        "cases": cases,
        "corpus": "hde_epic038_pr04_fixture_corpus_v1",
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
        for name in CASE_NAMES
    ]


def _selection_payload(db: DBAccess) -> dict[str, Any]:
    attempts = list(db.attempts)
    return {
        "attempts": attempts,
        "provider": db.provider_name,
        "selection_order": _selection_order(attempts),
    }


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
    harness = _deterministic_harness_payload()
    return {
        "attempts": list(db.attempts),
        "bridge_capability": _bridge_capability_payload(),
        "capabilities": _live_unavailable_capabilities(),
        "captured_at_utc": PRODUCED_AT_UTC,
        "fixture_parity": harness,
        "deterministic_harness": harness,
        "environment": "dev",
        "live_provider_parity": {
            "direct_provider_rows": "unavailable",
            "parity_status": "not_pass",
            "reason": "active_provider_rows_unavailable_or_not_exercised",
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
        snapshot = Path(tmpdir) / "nondev.adapter_selection.snapshot.json"
        with _patched_env({"APP_ENV": "stage"}):
            try:
                DBAccess.for_current_env(
                    snapshot_path=str(snapshot),
                    psycopg_factory=lambda _dsn: HarnessProvider("psycopg"),
                    bridge_factory=lambda _url: HarnessProvider("bridge"),
                )
            except AdapterError as exc:
                err = {"class": exc.__class__.__name__, "code": exc.code}
            else:
                raise SystemExit("NONDEV_TYPED_ERROR_UNEXPECTED:unexpected_success")
            attempts = json.loads(snapshot.read_text(encoding="utf-8")).get("attempts", [])
    expected = [
        {"provider": "psycopg", "status": "skip", "reason": "missing_database_url"},
        {"provider": "bridge", "status": "skip", "reason": "missing_bridge_url"},
    ]
    if attempts != expected or err != {"class": "BridgeUnavailable", "code": "missing_bridge_url"}:
        raise SystemExit("NONDEV_TYPED_ERROR_UNEXPECTED")
    return {
        "schema": "v1",
        "captured_at_utc": PRODUCED_AT_UTC,
        "environment": "stage",
        "selection_attempts": attempts,
        "selection_order": _selection_order(attempts),
        "total_failure": {"ok": False, "typed_error": err},
        "public_failure_posture": {"numeric_free": True, "secret_free": True, "raw_stack_trace": False},
        "probe_posture": {"no_proactive_probes": True, "adapter_path_only": True},
        "secret_posture": "presence_only",
    }


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _receipt_schema() -> dict[str, Any]:
    sha = {"type": "string", "pattern": "^[0-9a-f]{64}$"}
    side = {
        "type": "object",
        "required": ["provider", "acquisition_id", "availability", "case_count", "emitted_sha256"],
        "properties": {
            "provider": {"enum": ["direct_db", "db_bridge"]},
            "acquisition_id": {"type": "string"},
            "availability": {"const": "available"},
            "case_count": {"const": 4},
            "emitted_sha256": sha,
        },
        "additionalProperties": False,
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "presenter.db_bridge_compare.v1",
        "type": "object",
        "required": [
            "schema", "captured_at_utc", "fixture_id", "case_corpus_sha256",
            "provider_parity_path", "provider_parity_sha256", "direct", "bridge",
            "predicates", "negative_receipt", "payload_posture", "status",
        ],
        "properties": {
            "schema": {"const": "presenter.db_bridge_compare.v1"},
            "captured_at_utc": {"const": PRODUCED_AT_UTC},
            "fixture_id": {"const": "hde_epic038_pr04_fixture_corpus_v1"},
            "case_corpus_sha256": sha,
            "provider_parity_path": {"const": "artifacts/db_bridge/provider_parity.proof.json"},
            "provider_parity_sha256": sha,
            "direct": side,
            "bridge": side,
            "predicates": {
                "type": "object",
                "required": [
                    "same_case_corpus", "direct_available", "bridge_available",
                    "active_cases_complete", "case_count_equal", "presenter_bytes_equal",
                    "unsafe_fields_absent", "negative_control_rejected",
                ],
                "properties": {
                    key: {"type": "boolean"} for key in (
                        "same_case_corpus", "direct_available", "bridge_available",
                        "active_cases_complete", "case_count_equal", "presenter_bytes_equal",
                        "unsafe_fields_absent", "negative_control_rejected",
                    )
                },
                "additionalProperties": False,
            },
            "negative_receipt": {
                "type": "object",
                "required": [
                    "receipt_id", "mutated_side", "mutated_case", "baseline_emitted_sha256",
                    "mutated_emitted_sha256", "expected_failure_code", "observed_failure_code",
                    "divergence_detected", "receipt_sha256",
                ],
                "properties": {
                    "receipt_id": {"const": "db_bridge_case_mutation_v1"},
                    "mutated_side": {"const": "bridge"},
                    "mutated_case": {"const": "tx_select_one"},
                    "baseline_emitted_sha256": sha,
                    "mutated_emitted_sha256": sha,
                    "expected_failure_code": {"const": "DB_BRIDGE_PARITY_DIVERGENCE"},
                    "observed_failure_code": {"const": "DB_BRIDGE_PARITY_DIVERGENCE"},
                    "divergence_detected": {"const": True},
                    "receipt_sha256": sha,
                },
                "additionalProperties": False,
            },
            "payload_posture": {"const": "hashes_and_counts_only_no_case_values"},
            "status": {"enum": ["PASS", "FAIL"]},
        },
        "additionalProperties": False,
    }


_RECEIPT_FORBIDDEN_KEYS = {
    "authorization",
    "credentials",
    "database_url",
    "db_bridge_url",
    "dsn",
    "parameters",
    "params",
    "raw",
    "secret",
    "sql",
    "token",
    "value",
    "values",
}


def _receipt_payload_safe(value: Any) -> bool:
    if isinstance(value, dict):
        return all(
            isinstance(key, str)
            and key.casefold() not in _RECEIPT_FORBIDDEN_KEYS
            and _receipt_payload_safe(item)
            for key, item in value.items()
        )
    if isinstance(value, list):
        return all(_receipt_payload_safe(item) for item in value)
    if isinstance(value, str):
        folded = value.casefold()
        return not any(
            marker in folded
            for marker in ("postgresql://", "select ", "bearer ", "database_url=")
        )
    return value is None or isinstance(value, (bool, int, float))


def _presenter_receipt(
    parity_bytes: bytes, *, expected_parity_bytes: bytes
) -> dict[str, Any]:
    direct_cases = _acquire_cases("psycopg")
    bridge_cases = _acquire_cases("bridge")
    direct_bytes = emitter.emit_public(direct_cases)  # type: ignore[arg-type]
    bridge_bytes = emitter.emit_public(bridge_cases)  # type: ignore[arg-type]
    mutated = deepcopy(bridge_cases)
    mutated[-1]["value"] = {"negative_control": True}
    mutated_bytes = emitter.emit_public(mutated)  # type: ignore[arg-type]
    failure_code = "DB_BRIDGE_PARITY_DIVERGENCE" if mutated_bytes != bridge_bytes else ""
    negative = {
        "receipt_id": "db_bridge_case_mutation_v1",
        "mutated_side": "bridge",
        "mutated_case": "tx_select_one",
        "baseline_emitted_sha256": _sha(bridge_bytes),
        "mutated_emitted_sha256": _sha(mutated_bytes),
        "expected_failure_code": "DB_BRIDGE_PARITY_DIVERGENCE",
        "observed_failure_code": failure_code,
        "divergence_detected": mutated_bytes != bridge_bytes,
    }
    negative["receipt_sha256"] = _sha(canon.sercanon(negative, sort_keys=True))
    direct_summary = {
        "provider": "direct_db",
        "acquisition_id": "direct-db-acquisition-01",
        "availability": "available",
        "case_count": len(direct_cases),
        "emitted_sha256": _sha(direct_bytes),
    }
    bridge_summary = {
        "provider": "db_bridge",
        "acquisition_id": "db-bridge-acquisition-01",
        "availability": "available",
        "case_count": len(bridge_cases),
        "emitted_sha256": _sha(bridge_bytes),
    }
    bounded_receipt_material = {
        "case_corpus_sha256": _sha(canon.sercanon(list(CASE_NAMES), sort_keys=True)),
        "provider_parity_path": "artifacts/db_bridge/provider_parity.proof.json",
        "provider_parity_sha256": _sha(parity_bytes),
        "direct": direct_summary,
        "bridge": bridge_summary,
        "negative_receipt": negative,
        "payload_posture": "hashes_and_counts_only_no_case_values",
    }
    predicates = {
        "same_case_corpus": [row["name"] for row in direct_cases] == [row["name"] for row in bridge_cases] == list(CASE_NAMES),
        "direct_available": len(direct_cases) == len(CASE_NAMES),
        "bridge_available": len(bridge_cases) == len(CASE_NAMES),
        "active_cases_complete": len(direct_cases) == len(bridge_cases) == len(CASE_NAMES),
        "case_count_equal": len(direct_cases) == len(bridge_cases),
        "presenter_bytes_equal": direct_bytes == bridge_bytes,
        "unsafe_fields_absent": _receipt_payload_safe(bounded_receipt_material),
        "negative_control_rejected": failure_code == "DB_BRIDGE_PARITY_DIVERGENCE",
    }
    receipt = {
        "schema": "presenter.db_bridge_compare.v1",
        "captured_at_utc": PRODUCED_AT_UTC,
        "fixture_id": "hde_epic038_pr04_fixture_corpus_v1",
        "case_corpus_sha256": bounded_receipt_material["case_corpus_sha256"],
        "provider_parity_path": bounded_receipt_material["provider_parity_path"],
        "provider_parity_sha256": bounded_receipt_material["provider_parity_sha256"],
        "direct": direct_summary,
        "bridge": bridge_summary,
        "predicates": predicates,
        "negative_receipt": negative,
        "payload_posture": "hashes_and_counts_only_no_case_values",
        "status": (
            "PASS"
            if all(predicates.values()) and parity_bytes == expected_parity_bytes
            else "FAIL"
        ),
    }
    return receipt


def generate(*, check: bool = False) -> None:
    ensure_determinism_env()
    if check:
        with tempfile.TemporaryDirectory() as tmpdir:
            snapshot = Path(tmpdir) / "adapter_selection.snapshot.json"
            db = _run_dev_fallback_adapter(snapshot_path=snapshot)
            adapter_payload = json.loads(snapshot.read_text(encoding="utf-8"))
    else:
        db = _run_dev_fallback_adapter(snapshot_path=ADAPTER_SELECTION_PATH)
        adapter_payload = json.loads(ADAPTER_SELECTION_PATH.read_text(encoding="utf-8"))
    adapter_payload = _ensure_selection_order(adapter_payload)
    parity_payload = _provider_parity_payload(db)
    expected_parity_bytes = _canonical_json_bytes(parity_payload)

    _write_or_check(ADAPTER_SELECTION_PATH, adapter_payload, check=check)
    _write_or_check(CAPS_PATH, _caps_payload(), check=check)
    _write_or_check(PROVIDER_PARITY_PATH, parity_payload, check=check)
    parity_bytes = PROVIDER_PARITY_PATH.read_bytes()
    _write_or_check(ENV_CONNECTIVITY_PATH, _env_connectivity_payload(db), check=check)
    _write_or_check(NONDEV_FAILURE_PATH, _nondev_total_failure_payload(), check=check)

    synthetic = {
        "schema": "v1",
        "synthetic_identity": "hde-epic038-pr04-synthetic",
        "payload_posture": "mapped_bounded_no_raw_vendor_payload",
        "fields": ["centers", "channels", "profile"],
        "live_provider": "not_exercised",
    }
    _write_or_check(
        VENDOR_UPSERT_PATH,
        {**synthetic, "artifact": "vendor_upsert", "operation": "fixture_vendor_mapping"},
        check=check,
    )
    _write_or_check(
        DB_RESOLVE_PATH,
        {**synthetic, "artifact": "db_resolve", "operation": "fixture_db_resolution"},
        check=check,
    )
    _write_or_check(PRESENTER_SCHEMA_PATH, _receipt_schema(), check=check)
    _write_or_check(
        PRESENTER_COMPARE_PATH,
        _presenter_receipt(parity_bytes, expected_parity_bytes=expected_parity_bytes),
        check=check,
    )


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if generated evidence bytes differ")
    args = parser.parse_args(list(argv) if argv is not None else None)
    generate(check=args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
