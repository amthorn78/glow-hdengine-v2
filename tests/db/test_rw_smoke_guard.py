import importlib

import pytest


@pytest.mark.epic006
def test_smoke_skips_without_required(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://example")
    monkeypatch.setenv("DB_REQUIRED", "0")
    import adapter.db_access as db_access

    importlib.reload(db_access)
    status, detail = db_access.db_rw_smoke()
    assert status == "skip"
    assert detail == "DB_REQUIRED=0"
