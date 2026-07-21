import importlib


def _reload():
    import sys

    sys.modules.pop("adapter.db_access", None)
    import adapter.db_access as module

    return importlib.reload(module)


class _DirectDB:
    attempts = ({"provider": "psycopg", "status": "ok", "reason": None},)


def test_compatibility_resolver_reports_one_direct_attempt(monkeypatch):
    module = _reload()
    monkeypatch.setattr(
        module.DBAccess,
        "for_current_env",
        staticmethod(lambda: _DirectDB()),
    )

    result = module.db_resolve("dsn")

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

    result = module.db_resolve("dsn")

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
