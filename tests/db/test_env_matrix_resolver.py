from __future__ import annotations

import json

from adapter import db_access


def _snapshot(monkeypatch, database_url: str | None, bridge_url: str | None):
    if database_url is None:
        monkeypatch.delenv("DATABASE_URL", raising=False)
    else:
        monkeypatch.setenv("DATABASE_URL", database_url)

    if bridge_url is None:
        monkeypatch.delenv("DB_BRIDGE_URL", raising=False)
    else:
        monkeypatch.setenv("DB_BRIDGE_URL", bridge_url)

    ok, payload = db_access.resolve_env_matrix()
    return ok, json.loads(json.dumps(payload))  # ensure JSON-safe


def test_env_matrix_prefers_database_url(monkeypatch):
    ok, payload = _snapshot(monkeypatch, "postgresql://primary", "postgresql://bridge")
    assert ok is True
    assert payload["result"] == {"which": "DATABASE_URL"}
    assert payload["checks"] == [
        {"name": "DATABASE_URL", "value_kind": "dsn_redacted"},
        {"name": "DB_BRIDGE_URL", "value_kind": "dsn_redacted"},
    ]


def test_env_matrix_falls_back_to_bridge(monkeypatch):
    ok, payload = _snapshot(monkeypatch, None, "postgresql://bridge")
    assert ok is True
    assert payload["result"] == {"which": "DB_BRIDGE_URL"}
    assert payload["checks"][0]["value_kind"] == "unset"
    assert payload["checks"][1]["value_kind"] == "dsn_redacted"


def test_env_matrix_typed_error(monkeypatch):
    ok, payload = _snapshot(monkeypatch, None, None)
    assert ok is False
    assert payload == {
        "schema": "v1",
        "ok": False,
        "code": "missing_db_config",
        "error": "database configuration not found",
    }
