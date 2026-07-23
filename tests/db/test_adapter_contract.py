import pytest
from engine.db.adapter import Statement
from engine.db.errors import TxError
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
