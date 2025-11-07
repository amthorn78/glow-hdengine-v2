import importlib

import importlib

import pytest


def _reload():
    import sys

    sys.modules.pop("adapter.db_access", None)
    import adapter.db_access as module

    return importlib.reload(module)


@pytest.mark.epic006
def test_attempt_both_dsn_first(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://example")
    monkeypatch.delenv("DB_BRIDGE_URL", raising=False)
    module = _reload()
    res = module.db_resolve("dsn")
    assert res["dsn"]["status"] in {"ok", "unreachable", "skip"}
    assert res["bridge"]["status"] in {"ok", "unreachable", "skip"}


@pytest.mark.epic006
def test_attempt_both_bridge_then_dsn(monkeypatch):
    monkeypatch.setenv("DB_BRIDGE_URL", "https://bridge.example")
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.delenv("DATABASE_URL", raising=False)
    module = _reload()
    res = module.db_resolve("dsn")
    assert res["bridge"]["status"] in {"ok", "unreachable", "skip"}
    assert res["dsn"]["status"] in {"ok", "unreachable", "skip"}
