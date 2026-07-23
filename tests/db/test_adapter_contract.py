import pytest
from engine.db.adapter import DBAccess, Statement
from engine.db.errors import IntrospectionError, TxError
from engine.db.providers.psycopg_provider import PsycopgProvider
from scripts.ops.hde_epic038_ops03 import QUERY_STATEMENTS

class Cursor:
    def __init__(self, fail=False): self.executed=[]; self.fail=fail
    def __enter__(self): return self
    def __exit__(self,*a): return False
    def execute(self, sql, params=None):
        self.executed.append(sql)
        if self.fail and sql.startswith('SELECT'): raise RuntimeError('boom')
    def fetchall(self): return [(1,)]
class Conn:
    def __init__(self, fail=False): self.cur=Cursor(fail); self.commits=0; self.rollbacks=0; self.closed=0
    def cursor(self): return self.cur
    def commit(self): self.commits += 1
    def rollback(self): self.rollbacks += 1
    def close(self): self.closed += 1

def test_readonly_tx_rolls_back_and_does_not_commit():
    conn=Conn(); provider=PsycopgProvider('postgresql://secret', connection_factory=lambda dsn: conn)
    result=provider.readonly_tx(QUERY_STATEMENTS)
    assert len(result) == len(QUERY_STATEMENTS)
    assert conn.commits == 0
    assert conn.rollbacks == 1
    assert conn.closed == 1

def test_readonly_tx_rolls_back_on_error():
    conn=Conn(fail=True); provider=PsycopgProvider('postgresql://secret', connection_factory=lambda dsn: conn)
    with pytest.raises(TxError):
        provider.readonly_tx(QUERY_STATEMENTS)
    assert conn.commits == 0
    assert conn.rollbacks == 1

def test_readonly_tx_rejects_mutation_before_connection():
    called=[]; provider=PsycopgProvider('postgresql://secret', connection_factory=lambda dsn: called.append(1) or Conn())
    with pytest.raises(TxError):
        provider.readonly_tx([Statement('SET TRANSACTION READ ONLY'), Statement('UPDATE x SET y=1')])
    assert called == []


class IntrospectionCursor:
    def __init__(self, *, fetchone_values=(), fetchall_values=()):
        self._fetchone_values = list(fetchone_values)
        self._fetchall_values = list(fetchall_values)

    def __enter__(self):
        return self

    def __exit__(self, *_args):
        return False

    def execute(self, _sql, _params=None):
        return None

    def fetchone(self):
        return self._fetchone_values.pop(0) if self._fetchone_values else None

    def fetchall(self):
        return self._fetchall_values.pop(0) if self._fetchall_values else []


class IntrospectionConnection:
    def __init__(self, cursor):
        self._cursor = cursor
        self.closed = False

    def cursor(self):
        return self._cursor

    def commit(self):
        return None

    def rollback(self):
        return None

    def close(self):
        self.closed = True


def test_psycopg_tx_returns_tuples():
    connection = IntrospectionConnection(
        IntrospectionCursor(fetchall_values=[[['x', 'y']]])
    )
    provider = PsycopgProvider(
        "not-serialized", connection_factory=lambda _dsn: connection
    )

    assert provider.tx([Statement(sql="SELECT 1", fetch=True)]) == [[("x", "y")]]
    assert connection.closed is True


def test_direct_introspect_grants_shape():
    cursor = IntrospectionCursor(
        fetchone_values=[(False, False, False)],
        fetchall_values=[
            [
                ("reader", "hde", "body_graphs", "SELECT"),
                ("reader", "public", "hde_body_graphs_current", "SELECT"),
            ],
            [("hde_migrator", "hde", "r", "reader", "SELECT", False)],
        ],
    )
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: IntrospectionConnection(cursor),
    )

    assert provider.introspect("grants") == {
        "flags": {
            "rolsuper": False,
            "rolcreatedb": False,
            "rolcreaterole": False,
        },
        "grants": [
            ("reader", "hde.body_graphs", "SELECT"),
            ("reader", "public.hde_body_graphs_current", "SELECT"),
        ],
        "default_privileges": [
            "hde_migrator hde TABLE reader SELECT",
        ],
    }


def test_direct_introspect_fingerprint_shape():
    cursor = IntrospectionCursor(
        fetchone_values=[("SELECT 1",), ("SELECT 2",)],
        fetchall_values=[
            [
                ("user_id", "uuid", "NO", None),
                ("vendor", "text", "NO", None),
            ],
            [("constraint_name", "UNIQUE (vendor)")],
        ],
    )
    provider = PsycopgProvider(
        "not-serialized",
        connection_factory=lambda _dsn: IntrospectionConnection(cursor),
    )

    assert provider.introspect("fingerprint") == {
        "schema": "hde",
        "version": 1,
        "objects": {
            "hde.body_graphs": {
                "columns": [
                    {
                        "name": "user_id",
                        "data_type": "uuid",
                        "nullable": False,
                        "default": "",
                    },
                    {
                        "name": "vendor",
                        "data_type": "text",
                        "nullable": False,
                        "default": "",
                    },
                ],
                "constraints": [
                    {
                        "name": "constraint_name",
                        "definition": "UNIQUE (vendor)",
                    }
                ],
            },
            "hde.body_graphs_current": {"definition": "SELECT 1"},
            "public.hde_body_graphs_current": {"definition": "SELECT 2"},
        },
    }


def test_dbaccess_introspect_wrappers_normalize_payloads():
    class StubProvider:
        name = "psycopg"

        def introspect(self, kind):
            if kind == "search_path":
                return "hde, public"
            if kind == "fingerprint":
                return {"objects": [1, 2, 3]}
            if kind == "version":
                return {"status": "ok", "version": "15.4"}
            raise AssertionError(kind)

    db = DBAccess(StubProvider())

    assert db.introspect_search_path() == {
        "status": "ok",
        "search_path": "hde, public",
    }
    assert db.introspect_fingerprint() == {
        "status": "ok",
        "objects": [1, 2, 3],
    }
    assert db.introspect_version() == {"status": "ok", "version": "15.4"}


def test_dbaccess_introspect_wrappers_propagate_errors():
    class FailingProvider:
        name = "psycopg"

        def introspect(self, _kind):
            raise IntrospectionError("bounded", code="bounded")

    db = DBAccess(FailingProvider())

    with pytest.raises(IntrospectionError, match="bounded"):
        db.introspect_version()


def test_dbaccess_tx_preserves_provider_contract_without_validator_keyword():
    calls = []

    class LegacyCompatibleProvider:
        name = "psycopg"

        def tx(self, statements):
            calls.append(statements)
            return [[("ok",)]]

    statements = [Statement("SELECT 1", fetch=True)]
    db = DBAccess(LegacyCompatibleProvider())

    assert db.tx(statements) == [[("ok",)]]
    assert calls == [statements]
