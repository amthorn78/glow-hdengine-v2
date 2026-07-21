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
        provider_name = "psycopg"
        attempts = ({"provider": "psycopg", "status": "ok", "reason": None},)

        def exec(self, sql, params=None):
            calls.append((sql, params))

        def query(self, sql, params=None):
            calls.append((sql, params))
            return [("id",)]

    monkeypatch.setenv("DB_REQUIRED", "1")
    monkeypatch.setattr(db_access.DBAccess, "for_current_env", classmethod(lambda cls: FakeDB()))
    status, detail = db_access.db_rw_smoke()
    assert (status, detail) == ("ok", "db_rw_smoke_ok")
    assert calls and "INSERT INTO hde.public_results" in calls[1][0]
    assert calls[-1] == ("DELETE FROM hde.public_results WHERE id=%s", ("id",))
    assert "psycopg.connect" not in db_access.db_rw_smoke.__code__.co_names
