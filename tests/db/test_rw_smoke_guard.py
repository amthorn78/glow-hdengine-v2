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


def test_db_rw_smoke_uses_dbaccess_not_raw_psycopg(monkeypatch):
    import adapter.db_access as db_access

    calls = []

    class FakeDB:
        def tx(self, statements):
            calls.append(tuple((stmt.sql, stmt.params, stmt.fetch) for stmt in statements))
            return [None, [("id",)]]

    monkeypatch.setenv("DB_REQUIRED", "1")
    monkeypatch.setattr(db_access.DBAccess, "for_current_env", classmethod(lambda cls: FakeDB()))
    status, detail = db_access.db_rw_smoke()
    assert (status, detail) == ("ok", "db_rw_smoke_ok")
    assert calls and "INSERT INTO hde.public_results" in calls[0][1][0]
    assert "DELETE FROM hde.public_results" in calls[0][1][0]
    assert "psycopg.connect" not in db_access.db_rw_smoke.__code__.co_names
