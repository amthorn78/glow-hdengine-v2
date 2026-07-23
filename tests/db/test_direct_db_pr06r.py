from __future__ import annotations

import sys
import traceback
from collections.abc import Mapping
from types import SimpleNamespace

import pytest

from adapter import db_access as compatibility
from engine.db.adapter import (
    DBAccess,
    RETIRED_DB_TRANSPORT_KEYS,
    Statement,
    retired_db_transport_keys_present,
)
from engine.db.errors import (
    IntrospectionError,
    PrimaryUnavailable,
    RetiredBridgeConfiguration,
    TxError,
)
from engine.db.providers.psycopg_provider import PsycopgProvider
from scripts.ops.hde_epic038_ops03 import QUERY_STATEMENTS


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


@pytest.mark.parametrize("key", RETIRED_DB_TRANSPORT_KEYS)
@pytest.mark.parametrize("value", ["", "0", " ", "set"])
def test_each_retired_key_value_is_refused_by_membership(key, value):
    calls = []
    env = {"DATABASE_URL": "not-serialized", key: value}
    assert retired_db_transport_keys_present(env) == (key,)
    with pytest.raises(RetiredBridgeConfiguration) as caught:
        DBAccess.for_current_env(
            environ=env,
            psycopg_factory=lambda dsn: calls.append(dsn) or Provider(),
        )
    assert caught.value.retired_keys == (key,)
    assert calls == []


def test_retired_keys_raise_before_database_url_value_access():
    class EndpointTrap(Mapping):
        def __init__(self, values):
            self._values = dict(values)
            self.accessed = []

        def __iter__(self):
            return iter(self._values)

        def __len__(self):
            return len(self._values)

        def __getitem__(self, key):
            self.accessed.append(key)
            if key == "DATABASE_URL":
                raise AssertionError("DATABASE_URL value was read")
            return self._values[key]

    calls = []
    env = EndpointTrap(
        {
            "APP_ENV": "dev",
            "DATABASE_URL": "postgresql://must-not-read",
            "DB_BRIDGE_URL": "https://must-not-read",
        }
    )
    with pytest.raises(RetiredBridgeConfiguration) as exc:
        DBAccess.for_current_env(
            environ=env,
            psycopg_factory=lambda dsn: calls.append(dsn) or Provider(),
        )
    assert calls == []
    assert "DATABASE_URL" not in env.accessed
    assert exc.value.selection_case["database_url_presence"] == "present_redacted"
    assert exc.value.selection_case["retired_keys_present"] == ["DB_BRIDGE_URL"]


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


def test_selection_evidence_is_pure_and_does_not_touch_filesystem(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    db = DBAccess.for_current_env(
        environ={"APP_ENV": "dev", "DATABASE_URL": "not-serialized"},
        psycopg_factory=lambda _dsn: Provider(),
    )
    before = tuple(tmp_path.iterdir())
    assert db.selection_evidence()["selected"] == "psycopg"
    assert tuple(tmp_path.iterdir()) == before


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


def test_direct_failure_normalizes_injected_primary_error_and_never_serializes_it():
    secret = "postgresql://user:password@host/db"

    class HostileProvider(Provider):
        def health(self):
            self.health_calls += 1
            raise PrimaryUnavailable(secret, code=secret)

    provider = HostileProvider()
    with pytest.raises(PrimaryUnavailable) as caught:
        DBAccess.for_current_env(
            environ={"APP_ENV": secret, "DATABASE_URL": "not-serialized"},
            psycopg_factory=lambda _dsn: provider,
        )

    assert str(caught.value) == "primary_connect_failed"
    assert caught.value.code == "primary_connect_failed"
    assert caught.value.attempt_rows == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"}
    ]
    assert caught.value.selection_case["app_env"] == "unknown"
    assert secret not in repr(caught.value.selection_case)
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert secret not in "".join(
        traceback.format_exception(
            type(caught.value), caught.value, caught.value.__traceback__
        )
    )


def test_provider_failure_traceback_drops_raw_connection_exception():
    secret = "postgresql://user:password@host/db"
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: (_ for _ in ()).throw(RuntimeError(secret)),
    )

    with pytest.raises(PrimaryUnavailable) as caught:
        provider.health()

    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert secret not in "".join(
        traceback.format_exception(
            type(caught.value), caught.value, caught.value.__traceback__
        )
    )


def test_non_psycopg_factory_result_is_rejected_before_health():
    class AlternateProvider(Provider):
        name = "bridge"

    provider = AlternateProvider()
    with pytest.raises(PrimaryUnavailable) as caught:
        DBAccess.for_current_env(
            environ={"DATABASE_URL": "not-serialized"},
            psycopg_factory=lambda _dsn: provider,
        )

    assert caught.value.code == "primary_connect_failed"
    assert provider.health_calls == 0
    assert caught.value.attempt_rows == [
        {"provider": "psycopg", "status": "error", "reason": "primary_connect_failed"}
    ]


@pytest.mark.parametrize("scenario", ["success", "missing", "unavailable", "retired"])
def test_selection_evidence_never_serializes_hostile_app_env(scenario):
    secret = "postgresql://user:password@host/db"
    env = {"APP_ENV": secret}
    provider = Provider(fail_health=scenario == "unavailable")
    if scenario != "missing":
        env["DATABASE_URL"] = "not-serialized"
    if scenario == "retired":
        env["DB_FORCE_BRIDGE"] = ""

    try:
        db = DBAccess.for_current_env(
            environ=env,
            psycopg_factory=lambda _dsn: provider,
        )
        receipt = db.selection_evidence()
    except (PrimaryUnavailable, RetiredBridgeConfiguration) as exc:
        receipt = DBAccess.selection_failure_evidence(exc)

    assert receipt["app_env"] == "unknown"
    assert secret not in repr(receipt)


@pytest.mark.parametrize(
    "statements",
    [
        [Statement("SELECT 1", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("DELETE FROM x")],
        [Statement("SET TRANSACTION READ ONLY; SET TRANSACTION READ WRITE")],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT 1; UPDATE x SET y=1")],
        [Statement("SET TRANSACTION READ ONLY -- comment")],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SET TRANSACTION READ WRITE")],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT nextval('seq')", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT pg_advisory_lock(1)", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT set_config('x','y',false)", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT * FROM hde.body_graphs FOR SHARE", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT value INTO temp_copy FROM hde.body_graphs", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT pg_read_file('/etc/passwd')", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT pg_file_write('/tmp/x','x',false)", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT lo_export(1,'/tmp/x')", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT pg_reload_conf()", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SELECT custom_side_effect()", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), Statement("SHOW ALL", fetch=True)],
        [Statement("SET TRANSACTION READ ONLY"), *[Statement("SELECT 1", fetch=True) for _ in range(10)]],
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


@pytest.mark.parametrize("index", range(len(QUERY_STATEMENTS)))
def test_readonly_tx_rejects_each_exact_roster_sql_mutation_before_connection(index):
    connection_calls = []
    statements = list(QUERY_STATEMENTS)
    original = statements[index]
    statements[index] = Statement(
        f"{original.sql} || ''",
        fetch=original.fetch,
    )
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda dsn: connection_calls.append(dsn) or object(),
    )

    with pytest.raises(TxError, match="readonly_tx_roster_mismatch"):
        provider.readonly_tx(statements)

    assert connection_calls == []


@pytest.mark.parametrize(
    "index",
    tuple(
        index
        for index, statement in enumerate(QUERY_STATEMENTS)
        if "'hde'" in statement.sql
    ),
)
def test_readonly_tx_rejects_literal_case_mutation_before_connection(index):
    connection_calls = []
    statements = list(QUERY_STATEMENTS)
    original = statements[index]
    statements[index] = Statement(
        original.sql.replace("'hde'", "'HDE'", 1),
        fetch=original.fetch,
    )
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda dsn: connection_calls.append(dsn) or object(),
    )

    with pytest.raises(TxError, match="readonly_tx_roster_mismatch"):
        provider.readonly_tx(statements)

    assert connection_calls == []


@pytest.mark.parametrize("mutation", ["params", "fetch"])
def test_readonly_tx_rejects_non_sql_roster_mutation_before_connection(mutation):
    connection_calls = []
    statements = list(QUERY_STATEMENTS)
    original = statements[0]
    statements[0] = Statement(
        original.sql,
        params=("unexpected",) if mutation == "params" else None,
        fetch=True if mutation == "fetch" else original.fetch,
    )
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda dsn: connection_calls.append(dsn) or object(),
    )

    with pytest.raises(TxError, match="readonly_tx_roster_mismatch"):
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
        if self.fail_on_select and sql.startswith("SELECT"):
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
        QUERY_STATEMENTS
    )
    assert len(result) == len(QUERY_STATEMENTS)
    assert success.rollback_calls == 1
    assert success.commit_calls == 0
    assert success.close_calls == 1

    failure = Connection(fail_on_select=True)
    provider = PsycopgProvider("not-serialized", connection_factory=lambda _dsn: failure)
    with pytest.raises(TxError) as exc:
        provider.readonly_tx(
            QUERY_STATEMENTS
        )
    assert exc.value.code == "readonly_tx_failed"
    assert failure.rollback_calls == 1
    assert failure.commit_calls == 0
    assert failure.close_calls == 1


def test_readonly_tx_surfaces_rollback_failure_after_success():
    connection = Connection(fail_rollback=True)
    provider = PsycopgProvider("not-serialized", connection_factory=lambda _dsn: connection)
    with pytest.raises(TxError) as exc:
        provider.readonly_tx(QUERY_STATEMENTS)
    assert exc.value.code == "readonly_tx_rollback_failed"


def test_readonly_tx_rolls_back_and_closes_on_base_exception():
    connection = Connection()

    def interrupt(_sql, _params=None):
        raise KeyboardInterrupt

    connection.cursor_object.execute = interrupt
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: connection,
    )

    with pytest.raises(KeyboardInterrupt):
        provider.readonly_tx(QUERY_STATEMENTS)

    assert connection.rollback_calls == 1
    assert connection.commit_calls == 0
    assert connection.close_calls == 1


def test_write_smoke_deletes_only_the_inserted_row(monkeypatch):
    inserted_id = "00000000-0000-4000-8000-000000000001"

    class SmokeCursor:
        def __init__(self):
            self.calls = []

        def execute(self, sql, params=None):
            self.calls.append((" ".join(sql.split()), params))

    cursor = SmokeCursor()
    monkeypatch.setenv("DB_REQUIRED", "1")

    class FakeDB:
        def tx(self, statements, *, validate=None):
            for stmt in statements:
                cursor.execute(stmt.sql, stmt.params)
            results = [
                None,
                [(inserted_id,)],
                [(inserted_id,)],
                [(inserted_id,)],
            ]
            assert validate is not None
            validate(results)
            return results

    monkeypatch.setattr(compatibility.DBAccess, "for_current_env", classmethod(lambda cls: FakeDB()))
    assert compatibility.db_rw_smoke() == ("ok", "db_rw_smoke_ok")
    assert len(cursor.calls) == 4
    insert_sql, insert_params = cursor.calls[2]
    cleanup_sql, cleanup_params = cursor.calls[3]
    assert insert_sql.startswith("INSERT INTO hde.public_results")
    assert cleanup_sql.startswith("DELETE FROM hde.public_results")
    assert "current_setting('hde.qa_smoke_id')::uuid" in insert_sql
    assert "current_setting('hde.qa_smoke_id')::uuid" in cleanup_sql
    assert "WITH inserted AS" not in insert_sql
    assert "WITH inserted AS" not in cleanup_sql
    assert insert_params is None
    assert cleanup_params is None


def test_write_tx_validator_runs_before_commit_and_rolls_back_on_failure():
    connection = Connection()
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: connection,
    )
    validator_calls = []

    def reject(results):
        assert connection.commit_calls == 0
        validator_calls.append(tuple(results))
        raise RuntimeError("cleanup validation failed")

    with pytest.raises(TxError) as exc:
        provider.tx([Statement("SELECT 1", fetch=True)], validate=reject)

    assert exc.value.code == "tx_failed"
    assert validator_calls == [([(1,)],)]
    assert connection.commit_calls == 0
    assert connection.rollback_calls == 1
    assert connection.close_calls == 1


@pytest.mark.parametrize(
    ("operation", "expected_type", "expected_code"),
    [
        (
            lambda provider: provider.tx([Statement("SELECT 1", fetch=True)]),
            TxError,
            "tx_failed",
        ),
        (
            lambda provider: provider.introspect("grants"),
            IntrospectionError,
            "grants_unavailable",
        ),
        (
            lambda provider: provider.introspect("fingerprint"),
            IntrospectionError,
            "fingerprint_unavailable",
        ),
        (
            lambda provider: provider.introspect("version"),
            IntrospectionError,
            "version_unavailable",
        ),
    ],
)
def test_provider_operations_drop_hostile_connection_exception(
    operation, expected_type, expected_code
):
    secret = "postgresql://user:password@host/private"
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: (_ for _ in ()).throw(RuntimeError(secret)),
    )

    with pytest.raises(expected_type) as caught:
        operation(provider)

    assert caught.value.code == expected_code
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert secret not in "".join(
        traceback.format_exception(
            type(caught.value), caught.value, caught.value.__traceback__
        )
    )


def test_write_tx_rollback_failure_drops_hostile_exceptions():
    secret = "postgresql://user:password@host/private"

    class HostileRollbackConnection(Connection):
        def rollback(self):
            self.rollback_calls += 1
            raise RuntimeError(secret)

    connection = HostileRollbackConnection()
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: connection,
    )

    with pytest.raises(TxError) as caught:
        provider.tx(
            [Statement("SELECT 1", fetch=True)],
            validate=lambda _results: (_ for _ in ()).throw(RuntimeError(secret)),
        )

    assert caught.value.code == "tx_rollback_failed"
    assert caught.value.__cause__ is None
    assert caught.value.__context__ is None
    assert secret not in "".join(
        traceback.format_exception(
            type(caught.value), caught.value, caught.value.__traceback__
        )
    )
