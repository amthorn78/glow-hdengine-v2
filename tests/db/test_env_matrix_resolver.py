from __future__ import annotations

from copy import deepcopy

import pytest

from adapter import db_access
from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import PrimaryUnavailable


def _clear_retired_keys(monkeypatch) -> None:
    for name in RETIRED_DB_TRANSPORT_KEYS:
        monkeypatch.delenv(name, raising=False)


def test_env_matrix_direct_success_has_exact_v2_shape(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://must-not-leak")
    _clear_retired_keys(monkeypatch)

    ok, payload = db_access.resolve_env_matrix()

    assert ok is True
    assert payload == {
        "schema": "hde.db.env_selection.v2",
        "ok": True,
        "checks": [
            {"name": "DATABASE_URL", "value_kind": "present_redacted"},
            {"name": "DB_ALLOW_BRIDGE_IN_PROD", "value_kind": "unset"},
            {"name": "DB_BRIDGE_URL", "value_kind": "unset"},
            {"name": "DB_FORCE_BRIDGE", "value_kind": "unset"},
        ],
        "result": {"provider": "psycopg"},
        "error": None,
    }
    assert "must-not-leak" not in repr(payload)


def test_env_matrix_empty_retired_key_refuses_with_names_only(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://must-not-leak")
    _clear_retired_keys(monkeypatch)
    monkeypatch.setenv("DB_BRIDGE_URL", "")

    ok, payload = db_access.resolve_env_matrix()

    assert ok is False
    assert payload == {
        "schema": "hde.db.env_selection.v2",
        "ok": False,
        "checks": [
            {"name": "DATABASE_URL", "value_kind": "present_redacted"},
            {"name": "DB_ALLOW_BRIDGE_IN_PROD", "value_kind": "unset"},
            {"name": "DB_BRIDGE_URL", "value_kind": "present_retired"},
            {"name": "DB_FORCE_BRIDGE", "value_kind": "unset"},
        ],
        "result": None,
        "error": {
            "class": "RetiredBridgeConfiguration",
            "code": "retired_bridge_configuration",
            "retired_keys": ["DB_BRIDGE_URL"],
        },
    }
    assert "must-not-leak" not in repr(payload)


def test_env_matrix_missing_direct_has_exact_v2_failure_shape(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    _clear_retired_keys(monkeypatch)

    ok, payload = db_access.resolve_env_matrix()

    assert ok is False
    assert payload == {
        "schema": "hde.db.env_selection.v2",
        "ok": False,
        "checks": [
            {"name": "DATABASE_URL", "value_kind": "unset"},
            {"name": "DB_ALLOW_BRIDGE_IN_PROD", "value_kind": "unset"},
            {"name": "DB_BRIDGE_URL", "value_kind": "unset"},
            {"name": "DB_FORCE_BRIDGE", "value_kind": "unset"},
        ],
        "result": None,
        "error": {
            "class": "PrimaryUnavailable",
            "code": "missing_database_url",
            "retired_keys": [],
        },
    }


def test_env_matrix_normalizes_untrusted_error_codes(monkeypatch):
    def refuse(**_kwargs):
        raise PrimaryUnavailable(
            "postgresql://must-not-leak",
            code="postgresql://must-not-leak",
        )

    monkeypatch.setattr(db_access.DBAccess, "for_current_env", refuse)

    ok, payload = db_access.resolve_env_matrix()

    assert ok is False
    assert payload["error"] == {
        "class": "PrimaryUnavailable",
        "code": "primary_unavailable",
        "retired_keys": [],
    }
    assert "must-not-leak" not in repr(payload)


def test_env_matrix_contract_validator_rejects_unknown_keys_and_drift(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://redacted")
    _clear_retired_keys(monkeypatch)
    _, valid = db_access.resolve_env_matrix()

    mutations = []
    unknown_top = deepcopy(valid)
    unknown_top["unexpected"] = True
    mutations.append(unknown_top)
    unknown_check = deepcopy(valid)
    unknown_check["checks"][0]["unexpected"] = True
    mutations.append(unknown_check)
    unknown_result = deepcopy(valid)
    unknown_result["result"]["unexpected"] = True
    mutations.append(unknown_result)
    wrong_order = deepcopy(valid)
    wrong_order["checks"][0], wrong_order["checks"][1] = (
        wrong_order["checks"][1],
        wrong_order["checks"][0],
    )
    mutations.append(wrong_order)
    inconsistent = deepcopy(valid)
    inconsistent["ok"] = False
    mutations.append(inconsistent)

    for mutation in mutations:
        with pytest.raises(ValueError):
            db_access._validate_env_matrix_payload(mutation)


def test_stale_missing_config_constant_is_removed():
    assert not hasattr(db_access, "MISSING_DB_CONFIG")
