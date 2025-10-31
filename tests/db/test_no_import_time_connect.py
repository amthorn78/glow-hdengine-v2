import importlib

import pytest


@pytest.mark.epic006
def test_import_service_without_db_env(monkeypatch):
    monkeypatch.delenv("DATABASE_URL", raising=False)
    module = importlib.import_module("adapter.http_reader")
    assert module is not None
