"""Direct-only DB compatibility resolver."""
from __future__ import annotations

import os
from typing import Any, Mapping

from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import AdapterError, PrimaryUnavailable, RetiredBridgeConfiguration


_DB_RESOLVE_KEYS = frozenset({"schema", "active", "attempts", "error"})
_ENV_MATRIX_KEYS = frozenset({"schema", "ok", "checks", "result", "error"})
_ATTEMPT_KEYS = frozenset({"provider", "status", "reason"})
_CHECK_KEYS = frozenset({"name", "value_kind"})
_ERROR_KEYS = frozenset({"class", "code", "retired_keys"})
_RESULT_KEYS = frozenset({"provider"})
_PRIMARY_ERROR_CODES = frozenset(
    {"missing_database_url", "primary_connect_failed", "primary_unavailable"}
)
_ALLOWED_ERROR_PAIRS = frozenset(
    {
        ("AdapterError", "adapter_error"),
        ("PrimaryUnavailable", "missing_database_url"),
        ("PrimaryUnavailable", "primary_connect_failed"),
        ("PrimaryUnavailable", "primary_unavailable"),
        ("RetiredBridgeConfiguration", "retired_bridge_configuration"),
    }
)


class _EnvMatrixProvider:
    name = "psycopg"

    def health(self) -> None:
        return None


def _require_exact_keys(
    value: Any,
    expected: frozenset[str],
    *,
    label: str,
) -> Mapping[str, Any]:
    if not isinstance(value, Mapping) or set(value) != expected:
        raise ValueError(f"{label}_shape")
    return value


def _normalized_error_payload(exc: AdapterError) -> dict[str, Any]:
    if isinstance(exc, RetiredBridgeConfiguration):
        present = set(exc.retired_keys)
        return {
            "class": "RetiredBridgeConfiguration",
            "code": "retired_bridge_configuration",
            "retired_keys": [
                name for name in RETIRED_DB_TRANSPORT_KEYS if name in present
            ],
        }
    if isinstance(exc, PrimaryUnavailable):
        code = exc.code if exc.code in _PRIMARY_ERROR_CODES else "primary_unavailable"
        return {
            "class": "PrimaryUnavailable",
            "code": code,
            "retired_keys": [],
        }
    return {"class": "AdapterError", "code": "adapter_error", "retired_keys": []}


def _attempts_for_error(error: Mapping[str, Any]) -> list[dict[str, Any]]:
    code = error["code"]
    if code == "retired_bridge_configuration":
        return []
    status = "skip" if code == "missing_database_url" else "error"
    return [{"provider": "psycopg", "status": status, "reason": code}]


def _validate_error_payload(value: Any) -> None:
    error = _require_exact_keys(value, _ERROR_KEYS, label="db_error")
    if not isinstance(error["class"], str) or not isinstance(error["code"], str):
        raise ValueError("db_error_identity")
    pair = (error["class"], error["code"])
    if pair not in _ALLOWED_ERROR_PAIRS:
        raise ValueError("db_error_identity")
    retired_keys = error["retired_keys"]
    if not isinstance(retired_keys, list) or not all(
        isinstance(name, str) for name in retired_keys
    ):
        raise ValueError("db_error_retired_keys_shape")
    if retired_keys != [
        name for name in RETIRED_DB_TRANSPORT_KEYS if name in set(retired_keys)
    ]:
        raise ValueError("db_error_retired_keys_roster")
    if pair == ("RetiredBridgeConfiguration", "retired_bridge_configuration"):
        if not retired_keys:
            raise ValueError("db_error_retired_keys_missing")
    elif retired_keys:
        raise ValueError("db_error_unexpected_retired_keys")


def _validate_attempt(value: Any) -> None:
    attempt = _require_exact_keys(value, _ATTEMPT_KEYS, label="db_attempt")
    expected_reasons = {
        "ok": None,
        "skip": "missing_database_url",
        "error": {
            "adapter_error",
            "primary_connect_failed",
            "primary_unavailable",
        },
    }
    status = attempt["status"]
    if (
        attempt["provider"] != "psycopg"
        or not isinstance(status, str)
        or status not in expected_reasons
    ):
        raise ValueError("db_attempt_identity")
    reason = attempt["reason"]
    expected = expected_reasons[status]
    if isinstance(expected, set):
        if reason not in expected:
            raise ValueError("db_attempt_reason")
    elif reason != expected:
        raise ValueError("db_attempt_reason")


def _validate_db_resolve_payload(value: Any) -> None:
    payload = _require_exact_keys(value, _DB_RESOLVE_KEYS, label="db_resolve")
    if payload["schema"] != "hde.db.resolve.v2":
        raise ValueError("db_resolve_schema")
    active = payload["active"]
    if not isinstance(active, str) or active not in {"psycopg", "none"}:
        raise ValueError("db_resolve_active")
    attempts = payload["attempts"]
    if not isinstance(attempts, list) or len(attempts) > 1:
        raise ValueError("db_resolve_attempts_shape")
    for attempt in attempts:
        _validate_attempt(attempt)

    error = payload["error"]
    if active == "psycopg":
        if error is not None or len(attempts) != 1 or attempts[0]["status"] != "ok":
            raise ValueError("db_resolve_success_relationship")
        return
    if error is None:
        raise ValueError("db_resolve_failure_missing_error")
    _validate_error_payload(error)
    code = error["code"]
    if code == "retired_bridge_configuration":
        if attempts:
            raise ValueError("db_resolve_retired_attempt")
    elif len(attempts) != 1 or attempts[0]["reason"] != code:
        raise ValueError("db_resolve_failure_relationship")


def db_resolve() -> dict[str, Any]:
    """Return the exact direct-only v2 compatibility result."""
    try:
        db = DBAccess.for_current_env()
    except AdapterError as exc:
        error = _normalized_error_payload(exc)
        payload = {
            "schema": "hde.db.resolve.v2",
            "active": "none",
            "attempts": _attempts_for_error(error),
            "error": error,
        }
    else:
        payload = {
            "schema": "hde.db.resolve.v2",
            "active": db.provider_name,
            "attempts": [dict(row) for row in db.attempts],
            "error": None,
        }
    _validate_db_resolve_payload(payload)
    return payload


def _checks_from_case(case: Mapping[str, Any]) -> list[dict[str, str]]:
    checks = [
        {
            "name": "DATABASE_URL",
            "value_kind": case.get("database_url_presence", "unset"),
        }
    ]
    retired = set(case.get("retired_keys_present") or [])
    checks.extend(
        {
            "name": name,
            "value_kind": "present_retired" if name in retired else "unset",
        }
        for name in RETIRED_DB_TRANSPORT_KEYS
    )
    return checks


def _validate_env_matrix_payload(value: Any) -> None:
    payload = _require_exact_keys(value, _ENV_MATRIX_KEYS, label="env_matrix")
    if payload["schema"] != "hde.db.env_selection.v2" or type(payload["ok"]) is not bool:
        raise ValueError("env_matrix_identity")
    checks = payload["checks"]
    expected_names = ["DATABASE_URL", *RETIRED_DB_TRANSPORT_KEYS]
    if not isinstance(checks, list) or len(checks) != len(expected_names):
        raise ValueError("env_matrix_checks_shape")
    for index, (check, expected_name) in enumerate(zip(checks, expected_names)):
        row = _require_exact_keys(check, _CHECK_KEYS, label="env_matrix_check")
        if row["name"] != expected_name:
            raise ValueError("env_matrix_check_order")
        allowed_kinds = (
            {"present_redacted", "unset"}
            if index == 0
            else {"present_retired", "unset"}
        )
        if (
            not isinstance(row["value_kind"], str)
            or row["value_kind"] not in allowed_kinds
        ):
            raise ValueError("env_matrix_check_value_kind")

    result = payload["result"]
    error = payload["error"]
    if payload["ok"]:
        result_row = _require_exact_keys(result, _RESULT_KEYS, label="env_matrix_result")
        if result_row["provider"] != "psycopg" or error is not None:
            raise ValueError("env_matrix_success_relationship")
        if checks[0]["value_kind"] != "present_redacted":
            raise ValueError("env_matrix_success_database_url")
        if any(row["value_kind"] == "present_retired" for row in checks[1:]):
            raise ValueError("env_matrix_success_retired_key")
        return
    if result is not None or error is None:
        raise ValueError("env_matrix_failure_relationship")
    _validate_error_payload(error)
    retired_from_checks = [
        row["name"] for row in checks[1:] if row["value_kind"] == "present_retired"
    ]
    if retired_from_checks != error["retired_keys"]:
        raise ValueError("env_matrix_retired_key_relationship")
    database_url_presence = checks[0]["value_kind"]
    error_code = error["code"]
    if error_code == "missing_database_url" and database_url_presence != "unset":
        raise ValueError("env_matrix_missing_database_url_relationship")
    if (
        error_code in {"adapter_error", "primary_connect_failed", "primary_unavailable"}
        and database_url_presence != "present_redacted"
    ):
        raise ValueError("env_matrix_unavailable_database_url_relationship")


def resolve_env_matrix() -> tuple[bool, dict[str, Any]]:
    """Return the exact direct-only v2 environment-selection result."""
    try:
        db = DBAccess.for_current_env(
            psycopg_factory=lambda _dsn: _EnvMatrixProvider()
        )
        case = dict(db.selection_evidence())
        payload = {
            "schema": "hde.db.env_selection.v2",
            "ok": True,
            "checks": _checks_from_case(case),
            "result": {"provider": db.provider_name},
            "error": None,
        }
    except AdapterError as exc:
        case = DBAccess.selection_failure_evidence(exc)
        if not isinstance(getattr(exc, "selection_case", None), Mapping):
            case = {
                **case,
                "database_url_presence": (
                    "present_redacted"
                    if any(name == "DATABASE_URL" for name in os.environ)
                    else "unset"
                ),
            }
        payload = {
            "schema": "hde.db.env_selection.v2",
            "ok": False,
            "checks": _checks_from_case(case),
            "result": None,
            "error": _normalized_error_payload(exc),
        }
    _validate_env_matrix_payload(payload)
    return payload["ok"], payload


def _smoke_result_id(rows: Any, label: str) -> str:
    if (
        not isinstance(rows, (list, tuple))
        or len(rows) != 1
        or not isinstance(rows[0], (list, tuple))
        or len(rows[0]) != 1
        or rows[0][0] is None
    ):
        raise RuntimeError(f"smoke_{label}_missing_id")
    return str(rows[0][0])


def _validate_smoke_transaction(results: Any) -> None:
    if not isinstance(results, (list, tuple)) or len(results) != 4:
        raise RuntimeError("smoke_transaction_result_shape")
    ids = (
        _smoke_result_id(results[1], "generated"),
        _smoke_result_id(results[2], "insert"),
        _smoke_result_id(results[3], "cleanup"),
    )
    if len(set(ids)) != 1:
        raise RuntimeError("smoke_transaction_id_mismatch")


def _stable_primary_code(exc: PrimaryUnavailable) -> str:
    return exc.code if exc.code in _PRIMARY_ERROR_CODES else "primary_unavailable"


def db_rw_smoke() -> tuple[str, str]:
    """Run the gated write/delete smoke through one direct DBAccess transaction."""
    if os.getenv("DB_REQUIRED", "0") != "1":
        return "skip", "db_rw_smoke_disabled"
    try:
        db = DBAccess.for_current_env()
        db.tx(
            [
                DBAccess.statement("SET LOCAL search_path TO hde, public"),
                DBAccess.statement(
                    "SELECT set_config("
                    "'hde.qa_smoke_id', gen_random_uuid()::text, true"
                    ")",
                    fetch=True,
                ),
                DBAccess.statement(
                    "INSERT INTO hde.public_results (id, release_id, payload) "
                    "VALUES ("
                    "current_setting('hde.qa_smoke_id')::uuid, "
                    "'qa_smoke', '{}'::jsonb"
                    ") RETURNING id",
                    fetch=True,
                ),
                DBAccess.statement(
                    "DELETE FROM hde.public_results "
                    "WHERE id = current_setting('hde.qa_smoke_id')::uuid "
                    "RETURNING id",
                    fetch=True,
                ),
            ],
            validate=_validate_smoke_transaction,
        )
        return "ok", "db_rw_smoke_ok"
    except RetiredBridgeConfiguration:
        return "error", "retired_bridge_configuration"
    except PrimaryUnavailable as exc:
        return "skip", _stable_primary_code(exc)
    except Exception:
        return "error", "db_rw_smoke_failed"
