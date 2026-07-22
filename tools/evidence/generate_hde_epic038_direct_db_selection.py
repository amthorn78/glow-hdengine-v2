#!/usr/bin/env python3
"""Generate deterministic PR-06R-A direct DB selection evidence."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Mapping

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import PrimaryUnavailable, RetiredBridgeConfiguration
from tools.evidence.retained_evidence_safety import validate_retained_text_safety

OUT = ROOT / "artifacts/runtime/direct_db_selection.snapshot.json"
SCHEMA_PATH = ROOT / "schemas/hde_epic038_direct_db_selection.v1.json"
SCHEMA = "hde_epic038.direct_db_selection.v1"
PREDICATE_ORDER = (
    "direct_only_provider",
    "missing_direct_fails_closed",
    "unavailable_direct_fails_closed",
    "retired_keys_fail_before_provider_attempt",
    "alternate_transport_attempts_zero",
    "secret_values_absent",
)


class FakeProvider:
    name = "psycopg"

    def __init__(self, *, fail: bool = False):
        self.fail = fail

    def health(self) -> None:
        if self.fail:
            raise PrimaryUnavailable(
                "primary_connect_failed",
                attempts=["DATABASE_URL"],
                code="primary_connect_failed",
            )


def canonical_bytes(obj: Any) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _expected_attempt(code: str) -> list[dict[str, object]]:
    return [{
        "provider": "psycopg",
        "status": "skip" if code == "missing_database_url" else "error",
        "reason": code,
    }]


def _database_url_presence(environ: Mapping[str, str]) -> str:
    """Classify DATABASE_URL by membership without reading its value."""
    return "present_redacted" if "DATABASE_URL" in environ else "unset"


def run_case(name: str, environ: Mapping[str, str], *, fail: bool = False) -> dict[str, object]:
    calls: list[str] = []

    def factory(_dsn: str) -> FakeProvider:
        calls.append("psycopg")
        return FakeProvider(fail=fail)

    try:
        db = DBAccess.for_current_env(environ=environ, psycopg_factory=factory)
        row = dict(db.selection_evidence())
        row["case"] = name
        row["result"] = "PASS" if calls == ["psycopg"] else "FAIL"
        return row
    except RetiredBridgeConfiguration as exc:
        return {
            "case": name,
            "app_env": (environ.get("APP_ENV") or "dev").strip() or "dev",
            "database_url_presence": _database_url_presence(environ),
            "retired_keys_present": list(exc.retired_keys),
            "attempts": [],
            "selected": "none",
            "error": {"class": "RetiredBridgeConfiguration", "code": exc.code},
            "alternate_transport_attempts": 0,
            "result": "PASS" if calls == [] else "FAIL",
        }
    except PrimaryUnavailable as exc:
        expected_calls = [] if exc.code == "missing_database_url" else ["psycopg"]
        return {
            "case": name,
            "app_env": (environ.get("APP_ENV") or "dev").strip() or "dev",
            "database_url_presence": "present_redacted" if environ.get("DATABASE_URL") else "unset",
            "retired_keys_present": [],
            "attempts": _expected_attempt(exc.code),
            "selected": "none",
            "error": {"class": "PrimaryUnavailable", "code": exc.code},
            "alternate_transport_attempts": 0,
            "result": "PASS" if calls == expected_calls else "FAIL",
        }


def _expected_cases() -> list[dict[str, object]]:
    return [
        {"case": "healthy_direct", "app_env": "dev", "database_url_presence": "present_redacted", "retired_keys_present": [], "attempts": [{"provider": "psycopg", "status": "ok", "reason": None}], "selected": "psycopg", "error": None, "alternate_transport_attempts": 0, "result": "PASS"},
        {"case": "missing_database_url", "app_env": "dev", "database_url_presence": "unset", "retired_keys_present": [], "attempts": _expected_attempt("missing_database_url"), "selected": "none", "error": {"class": "PrimaryUnavailable", "code": "missing_database_url"}, "alternate_transport_attempts": 0, "result": "PASS"},
        {"case": "unavailable_database_url", "app_env": "dev", "database_url_presence": "present_redacted", "retired_keys_present": [], "attempts": _expected_attempt("primary_connect_failed"), "selected": "none", "error": {"class": "PrimaryUnavailable", "code": "primary_connect_failed"}, "alternate_transport_attempts": 0, "result": "PASS"},
        {"case": "retired_keys_present", "app_env": "dev", "database_url_presence": "present_redacted", "retired_keys_present": list(RETIRED_DB_TRANSPORT_KEYS), "attempts": [], "selected": "none", "error": {"class": "RetiredBridgeConfiguration", "code": "retired_bridge_configuration"}, "alternate_transport_attempts": 0, "result": "PASS"},
    ]


def _case_is(actual: Mapping[str, object], expected: Mapping[str, object]) -> bool:
    return dict(actual) == dict(expected)


def validate_contract(payload: Mapping[str, object]) -> tuple[str, ...]:
    errors: list[str] = []
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    if list(Draft202012Validator(schema).iter_errors(payload)):
        errors.append("schema_invalid")
    cases = payload.get("cases")
    expected = _expected_cases()
    if not isinstance(cases, list) or len(cases) != len(expected):
        errors.append("case_inventory_invalid")
        derived_predicates = None
    else:
        derived_predicates = {
            "direct_only_provider": _case_is(cases[0], expected[0]),
            "missing_direct_fails_closed": _case_is(cases[1], expected[1]),
            "unavailable_direct_fails_closed": _case_is(cases[2], expected[2]),
            "retired_keys_fail_before_provider_attempt": _case_is(cases[3], expected[3]),
            "alternate_transport_attempts_zero": all(
                isinstance(case, Mapping)
                and case.get("alternate_transport_attempts") == 0
                for case in cases
            ),
            "secret_values_absent": not any(
                validate_retained_text_safety(OUT, canonical_bytes(case))
                for case in cases
            ),
        }
    predicates = payload.get("predicates")
    if not isinstance(predicates, Mapping) or set(predicates) != set(PREDICATE_ORDER):
        errors.append("predicate_inventory_invalid")
    else:
        if derived_predicates is None or dict(predicates) != derived_predicates:
            errors.append("predicate_value_invalid")
        failed = sorted(name for name in PREDICATE_ORDER if predicates.get(name) is not True)
        expected_result = "FAIL" if failed else "PASS"
        expected_failure = (
            {"code": "predicate_failure", "failed_predicates": failed}
            if failed
            else None
        )
        if payload.get("result") != expected_result:
            errors.append("result_predicate_mismatch")
        if payload.get("failure") != expected_failure:
            errors.append("failure_receipt_invalid")
    if validate_retained_text_safety(OUT, canonical_bytes(payload)):
        errors.append("secret_values_present")
    return tuple(sorted(set(errors)))


def build() -> dict[str, object]:
    cases = [
        run_case("healthy_direct", {"APP_ENV": "dev", "DATABASE_URL": "set-redacted"}),
        run_case("missing_database_url", {"APP_ENV": "dev"}),
        run_case("unavailable_database_url", {"APP_ENV": "dev", "DATABASE_URL": "set-redacted"}, fail=True),
        run_case("retired_keys_present", {"APP_ENV": "dev", "DATABASE_URL": "set-redacted", **{name: "" for name in RETIRED_DB_TRANSPORT_KEYS}}),
    ]
    expected = _expected_cases()
    predicates = {
        "direct_only_provider": _case_is(cases[0], expected[0]),
        "missing_direct_fails_closed": _case_is(cases[1], expected[1]),
        "unavailable_direct_fails_closed": _case_is(cases[2], expected[2]),
        "retired_keys_fail_before_provider_attempt": _case_is(cases[3], expected[3]),
        "alternate_transport_attempts_zero": all(case.get("alternate_transport_attempts") == 0 for case in cases),
        "secret_values_absent": not any(validate_retained_text_safety(OUT, canonical_bytes(case)) for case in cases),
    }
    ok = all(predicates.values())
    payload: dict[str, object] = {
        "schema": SCHEMA,
        "retired_keys": list(RETIRED_DB_TRANSPORT_KEYS),
        "cases": cases,
        "predicates": predicates,
        "result": "PASS" if ok else "FAIL",
        "failure": None if ok else {"code": "predicate_failure", "failed_predicates": sorted(name for name, value in predicates.items() if not value)},
    }
    if validate_contract(payload):
        predicates["secret_values_absent"] = False
        payload["result"] = "FAIL"
        payload["failure"] = {"code": "predicate_failure", "failed_predicates": sorted(name for name, value in predicates.items() if not value)}
    return payload


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=OUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    data = build()
    raw = canonical_bytes(data)
    if args.check:
        return 0 if args.out.exists() and args.out.read_bytes() == raw and data["result"] == "PASS" else 1
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_bytes(raw)
    return 0 if data["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
