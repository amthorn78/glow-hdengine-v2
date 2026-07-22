import importlib

from copy import deepcopy

import pytest

from engine.db.errors import PrimaryUnavailable


def _reload():
    import sys

    sys.modules.pop("adapter.db_access", None)
    import adapter.db_access as module

    return importlib.reload(module)


class _DirectDB:
    provider_name = "psycopg"
    attempts = ({"provider": "psycopg", "status": "ok", "reason": None},)


def test_compatibility_resolver_reports_one_direct_attempt(monkeypatch):
    module = _reload()
    monkeypatch.setattr(
        module.DBAccess,
        "for_current_env",
        staticmethod(lambda: _DirectDB()),
    )

    result = module.db_resolve()

    assert result == {
        "schema": "hde.db.resolve.v2",
        "active": "psycopg",
        "attempts": [
            {"provider": "psycopg", "status": "ok", "reason": None}
        ],
        "error": None,
    }
    assert "dsn" not in result
    assert "bridge" not in result


def test_compatibility_resolver_refuses_retired_bridge_configuration(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://must-not-leak")
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    module = _reload()

    result = module.db_resolve()

    assert result == {
        "schema": "hde.db.resolve.v2",
        "active": "none",
        "attempts": [],
        "error": {
            "class": "RetiredBridgeConfiguration",
            "code": "retired_bridge_configuration",
            "retired_keys": ["DB_BRIDGE_URL"],
        },
    }
    assert "must-not-leak" not in repr(result)
    assert "bridge.example" not in repr(result)


def test_compatibility_resolver_missing_direct_has_one_skip_attempt(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for name in ("DB_ALLOW_BRIDGE_IN_PROD", "DB_BRIDGE_URL", "DB_FORCE_BRIDGE"):
        monkeypatch.delenv(name, raising=False)
    module = _reload()

    assert module.db_resolve() == {
        "schema": "hde.db.resolve.v2",
        "active": "none",
        "attempts": [
            {
                "provider": "psycopg",
                "status": "skip",
                "reason": "missing_database_url",
            }
        ],
        "error": {
            "class": "PrimaryUnavailable",
            "code": "missing_database_url",
            "retired_keys": [],
        },
    }


def test_compatibility_resolver_normalizes_untrusted_error_codes(monkeypatch):
    module = _reload()

    def refuse():
        raise PrimaryUnavailable(
            "postgresql://must-not-leak",
            code="postgresql://must-not-leak",
        )

    monkeypatch.setattr(module.DBAccess, "for_current_env", refuse)

    result = module.db_resolve()

    assert result["attempts"] == [
        {
            "provider": "psycopg",
            "status": "error",
            "reason": "primary_unavailable",
        }
    ]
    assert result["error"] == {
        "class": "PrimaryUnavailable",
        "code": "primary_unavailable",
        "retired_keys": [],
    }
    assert "must-not-leak" not in repr(result)


def test_compatibility_resolver_contract_rejects_unknown_keys_and_drift(monkeypatch):
    module = _reload()
    monkeypatch.setattr(
        module.DBAccess,
        "for_current_env",
        staticmethod(lambda: _DirectDB()),
    )
    valid = module.db_resolve()

    mutations = []
    unknown_top = deepcopy(valid)
    unknown_top["unexpected"] = True
    mutations.append(unknown_top)
    unknown_attempt = deepcopy(valid)
    unknown_attempt["attempts"][0]["unexpected"] = True
    mutations.append(unknown_attempt)
    missing_attempt_key = deepcopy(valid)
    del missing_attempt_key["attempts"][0]["reason"]
    mutations.append(missing_attempt_key)
    inconsistent_active = deepcopy(valid)
    inconsistent_active["active"] = "none"
    mutations.append(inconsistent_active)

    for mutation in mutations:
        with pytest.raises(ValueError):
            module._validate_db_resolve_payload(mutation)


def test_retired_preference_argument_is_not_executable():
    module = _reload()

    with pytest.raises(TypeError):
        module.db_resolve("dsn")
