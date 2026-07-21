import pytest
from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import PrimaryUnavailable, RetiredBridgeConfiguration

class FakeProvider:
    name='psycopg'
    def __init__(self): self.health_count=0
    def health(self): self.health_count += 1
    def query(self,*a,**k): return []
    def exec(self,*a,**k): pass
    def tx(self,*a,**k): return []
    def readonly_tx(self,*a,**k): return []
    def introspect(self,*a,**k): return {}

def test_selects_direct_psycopg_only():
    provider=FakeProvider()
    db=DBAccess.for_current_env(environ={'DATABASE_URL':'postgresql://secret'}, psycopg_factory=lambda dsn: provider)
    assert db.provider_name == 'psycopg'
    assert provider.health_count == 1
    assert list(db.attempts) == [{'provider':'psycopg','status':'ok','reason':None}]

def test_missing_database_url_raises_primary_unavailable():
    with pytest.raises(PrimaryUnavailable) as exc:
        DBAccess.for_current_env(environ={})
    assert exc.value.code == 'missing_database_url'

def test_retired_keys_raise_before_factory():
    calls=[]
    env={'DATABASE_URL':'postgresql://secret', **{k:'' for k in RETIRED_DB_TRANSPORT_KEYS}}
    with pytest.raises(RetiredBridgeConfiguration):
        DBAccess.for_current_env(environ=env, psycopg_factory=lambda dsn: calls.append(dsn) or FakeProvider())
    assert calls == []
