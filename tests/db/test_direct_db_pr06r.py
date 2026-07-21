from __future__ import annotations

import sys
from types import SimpleNamespace

import pytest

from adapter import db_access as compatibility
from engine.db.adapter import (
    DBAccess,
    RETIRED_DB_TRANSPORT_KEYS,
    Statement,
    retired_db_transport_keys_present,
)
from engine.db.errors import PrimaryUnavailable, RetiredBridgeConfiguration, TxError
from engine.db.providers.psycopg_provider import PsycopgProvider


class Provider:
    name = "psycopg"

    def __init__(self, *, fail_health: bool = False):
        self.health_calls = 0
        self.fail_health = fail_health

    def health(self):
        self.health_calls += 1
        if self.fail_health:
            raise RuntimeError("not serialized")

    def query(self, *_args, **_kwargs):
        return []

    def exec(self, *_args, **_kwargs):
        return None

    def tx(self, *_args, **_kwargs):
        return []

    def readonly_tx(self, *_args, **_kwargs):
        return []

    def introspect(self, *_args, **_kwargs):
        return {}


def test_retired_keys_are_membership_sorted_and_block_factory_without_value_leak():
    calls = []
    env = {
        "DATABASE_URL": "postgresql://must-not-leak",
        "DB_FORCE_BRIDGE": "",
        "DB_BRIDGE_URL": "0",
        "DB_ALLOW_BRIDGE_IN_PROD": " ",
    }
    assert retired_db_transport_keys_present(env) == RETIRED_DB_TRANSPORT_KEYS
    with pytest.raises(RetiredBridgeConfiguration) as exc:
        DBAccess.for_current_env(
            environ=env,
            psycopg_factory=lambda dsn: calls.append(dsn) or Provider(),
        )
    assert exc.value.retired_keys == RETIRED_DB_TRANSPORT_KEYS
    assert calls == []
    assert str(exc.value) == (
        "retired_bridge_configuration:"
        "DB_ALLOW_BRIDGE_IN_PROD,DB_BRIDGE_URL,DB_FORCE_BRIDGE"
    )
    assert "must-not-leak" not in str(exc.value)


def test_direct_success_has_one_health_and_one_selection_attempt():
    provider = Provider()
    db = DBAccess.for_current_env(
        environ={"APP_ENV": "dev", "DATABASE_URL": "not-serialized"},
        psycopg_factory=lambda _dsn: provider,
    )
    assert provider.health_calls == 1
    assert db.provider_name == "psycopg"
    assert list(db.attempts) == [{"provider": "psycopg", "status": "ok", "reason": None}]
    assert db.selection_evidence() == {
        "case": "healthy_direct",
        "app_env": "dev",
        "database_url_presence": "present_redacted",
        "retired_keys_present": [],
        "attempts": [{"provider": "psycopg", "status": "ok", "reason": None}],
        "selected": "psycopg",
        "error": None,
        "alternate_transport_attempts": 0,
        "result": "PASS",
    }


def test_missing_and_unavailable_database_url_fail_closed_with_stable_codes():
    calls = []
    with pytest.raises(PrimaryUnavailable) as missing:
        DBAccess.for_current_env(environ={}, psycopg_factory=lambda dsn: calls.append(dsn))
    assert missing.value.code == "missing_database_url"
    assert calls == []

    provider = Provider(fail_health=True)
    with pytest.raises(PrimaryUnavailable) as unavailable:
        DBAccess.for_current_env(
            environ={"DATABASE_URL": "not-serialized"},
            psycopg_factory=lambda _dsn: provider,
        )
    assert unavailable.value.code == "primary_connect_failed"
    assert provider.health_calls == 1
    assert "not-serialized" not in str(unavailable.value)


@pytest.mark.parametrize(
    "statements",
    [
        [Statement("SELECT 1", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("DELETE FROM x")],
        [Statement("SET TRANSACTION READ ONLY; SET TRANSACTION READ WRITE")],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT 1; UPDATE x SET y=1")],
        [Statement("SET TRANSACTION READ ONLY -- comment")],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SET TRANSACTION READ WRITE")],
    ],
)
def test_readonly_tx_rejects_wrong_first_mutation_batching_and_comments(statements):
    connection_calls = []
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda dsn: connection_calls.append(dsn) or object(),
    )
    with pytest.raises(TxError):
        provider.readonly_tx(statements)
    assert connection_calls == []


class Cursor:
    def __init__(self, *, fail_on_select: bool = False):
        self.fail_on_select = fail_on_select
        self.statements = []

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def execute(self, sql, params=None):
        self.statements.append((sql, params))
        if self.fail_on_select and sql == "SELECT 1":
            raise RuntimeError("query failed")

    def fetchall(self):
        return [(1,)]


class Connection:
    def __init__(self, *, fail_on_select: bool = False, fail_rollback: bool = False):
        self.cursor_object = Cursor(fail_on_select=fail_on_select)
        self.rollback_calls = 0
        self.commit_calls = 0
        self.close_calls = 0
        self.fail_rollback = fail_rollback
        self.closed = False

    def cursor(self):
        return self.cursor_object

    def rollback(self):
        if self.closed:
            raise RuntimeError("rollback after close")
        self.rollback_calls += 1
        if self.fail_rollback:
            raise RuntimeError("rollback failed")

    def commit(self):
        self.commit_calls += 1

    def close(self):
        self.close_calls += 1
        self.closed = True


def test_readonly_tx_rolls_back_without_commit_on_success_and_failure():
    success = Connection()
    provider = PsycopgProvider("not-serialized", connection_factory=lambda _dsn: success)
    result = provider.readonly_tx(
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT 1", fetch=True)]
    )
    assert result == [None, [(1,)]]
    assert success.rollback_calls == 1
    assert success.commit_calls == 0
    assert success.close_calls == 1

    failure = Connection(fail_on_select=True)
    provider = PsycopgProvider("not-serialized", connection_factory=lambda _dsn: failure)
    with pytest.raises(TxError) as exc:
        provider.readonly_tx(
            [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT 1", fetch=True)]
        )
    assert exc.value.code == "readonly_tx_failed"
    assert failure.rollback_calls == 1
    assert failure.commit_calls == 0
    assert failure.close_calls == 1


def test_readonly_tx_surfaces_rollback_failure_after_success():
    connection = Connection(fail_rollback=True)
    provider = PsycopgProvider("not-serialized", connection_factory=lambda _dsn: connection)
    with pytest.raises(TxError) as exc:
        provider.readonly_tx([Statement("SET TRANSACTION READ ONLY")])
    assert exc.value.code == "readonly_tx_rollback_failed"


def test_write_smoke_deletes_only_the_inserted_row(monkeypatch):
    inserted_id = "00000000-0000-4000-8000-000000000001"

    class SmokeCursor:
        def __init__(self):
            self.calls = []

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def execute(self, sql, params=None):
            self.calls.append((" ".join(sql.split()), params))

        def fetchone(self):
            return (inserted_id,)

    class SmokeConnection:
        def __init__(self):
            self.cursor_object = SmokeCursor()

        def __enter__(self):
            return self

        def __exit__(self, *_args):
            return False

        def cursor(self):
            return self.cursor_object

    connection = SmokeConnection()
    monkeypatch.setenv("DB_REQUIRED", "1")

    class FakeDB:
        def tx(self, statements):
            for stmt in statements:
                connection.cursor_object.execute(stmt.sql, stmt.params)
            return [None, [(inserted_id,)]]

    monkeypatch.setattr(compatibility.DBAccess, "for_current_env", classmethod(lambda cls: FakeDB()))
    assert compatibility.db_rw_smoke() == ("ok", "db_rw_smoke_ok")
    cleanup_sql, cleanup_params = connection.cursor_object.calls[-1]
    assert "WITH inserted AS" in cleanup_sql
    assert "DELETE FROM hde.public_results WHERE id IN (SELECT id FROM inserted)" in cleanup_sql
    assert cleanup_params is None
