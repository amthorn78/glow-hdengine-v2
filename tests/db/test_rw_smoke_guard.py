import importlib

import pytest

from engine.db.errors import PrimaryUnavailable, RetiredBridgeConfiguration


@pytest.mark.epic006
def test_smoke_skips_without_required(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql://example")
    monkeypatch.setenv("DB_REQUIRED", "0")
    import adapter.db_access as db_access

    importlib.reload(db_access)
    status, detail = db_access.db_rw_smoke()
    assert status == "skip"
    assert detail == "db_rw_smoke_disabled"


def test_db_rw_smoke_uses_dbaccess_not_raw_psycopg(monkeypatch):
    import adapter.db_access as db_access

    calls = []

    class FakeDB:
        def tx(self, statements, *, validate=None):
            calls.append(tuple((stmt.sql, stmt.params, stmt.fetch) for stmt in statements))
            smoke_id = "00000000-0000-4000-8000-000000000001"
            results = [None, [(smoke_id,)], [(smoke_id,)], [(smoke_id,)]]
            assert validate is not None
            validate(results)
            return results

    monkeypatch.setenv("DB_REQUIRED", "1")
    monkeypatch.setattr(db_access.DBAccess, "for_current_env", classmethod(lambda cls: FakeDB()))
    status, detail = db_access.db_rw_smoke()
    assert (status, detail) == ("ok", "db_rw_smoke_ok")
    assert len(calls) == 1
    statements = calls[0]
    assert len(statements) == 4
    assert "set_config" in statements[1][0]
    assert statements[1][2] is True
    assert "INSERT INTO hde.public_results" in statements[2][0]
    assert "DELETE FROM hde.public_results" in statements[3][0]
    assert "WITH inserted AS" not in statements[2][0]
    assert "WITH inserted AS" not in statements[3][0]
    assert "psycopg.connect" not in db_access.db_rw_smoke.__code__.co_names


def test_db_rw_smoke_rejects_missing_cleanup_before_success(monkeypatch):
    import adapter.db_access as db_access

    validated = []

    class FakeDB:
        def tx(self, statements, *, validate=None):
            smoke_id = "00000000-0000-4000-8000-000000000001"
            results = [None, [(smoke_id,)], [(smoke_id,)], []]
            assert validate is not None
            validated.append(True)
            validate(results)
            pytest.fail("cleanup validation unexpectedly returned")

    monkeypatch.setenv("DB_REQUIRED", "1")
    monkeypatch.setattr(db_access.DBAccess, "for_current_env", classmethod(lambda cls: FakeDB()))
    assert db_access.db_rw_smoke() == ("error", "db_rw_smoke_failed")
    assert validated == [True]


def test_db_rw_smoke_preserves_retired_configuration_failure(monkeypatch):
    import adapter.db_access as db_access

    def refuse():
        raise RetiredBridgeConfiguration(("DB_BRIDGE_URL",))

    monkeypatch.setenv("DB_REQUIRED", "1")
    monkeypatch.setattr(db_access.DBAccess, "for_current_env", refuse)

    assert db_access.db_rw_smoke() == (
        "error",
        "retired_bridge_configuration",
    )


@pytest.mark.parametrize(
    ("code", "expected"),
    [
        ("missing_database_url", "missing_database_url"),
        ("primary_connect_failed", "primary_connect_failed"),
        ("postgresql://must-not-leak", "primary_unavailable"),
    ],
)
def test_db_rw_smoke_returns_stable_primary_codes(monkeypatch, code, expected):
    import adapter.db_access as db_access

    def refuse():
        raise PrimaryUnavailable("postgresql://must-not-leak", code=code)

    monkeypatch.setenv("DB_REQUIRED", "1")
    monkeypatch.setattr(db_access.DBAccess, "for_current_env", refuse)

    result = db_access.db_rw_smoke()

    assert result == ("skip", expected)
    assert "must-not-leak" not in repr(result)


def test_db_rw_smoke_retired_preference_argument_is_not_executable():
    import adapter.db_access as db_access

    with pytest.raises(TypeError):
        db_access.db_rw_smoke("dsn")
