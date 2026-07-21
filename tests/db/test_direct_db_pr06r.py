import pytest
from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS, Statement, retired_db_transport_keys_present
from engine.db.errors import PrimaryUnavailable, RetiredBridgeConfiguration, TxError
from engine.db.providers.psycopg_provider import PsycopgProvider

class Provider:
    name='psycopg'
    def __init__(self): self.health_calls=0
    def health(self): self.health_calls += 1
    def query(self,*a,**k): return []
    def exec(self,*a,**k): pass
    def tx(self,*a,**k): return []
    def readonly_tx(self,*a,**k): return []
    def introspect(self,*a,**k): return {}

def test_retired_keys_are_membership_sorted_and_block_factory():
    calls=[]
    env={'DATABASE_URL':'secret','DB_FORCE_BRIDGE':'','DB_BRIDGE_URL':'0','DB_ALLOW_BRIDGE_IN_PROD':' '}
    assert retired_db_transport_keys_present(env) == RETIRED_DB_TRANSPORT_KEYS
    with pytest.raises(RetiredBridgeConfiguration) as exc:
        DBAccess.for_current_env(environ=env, psycopg_factory=lambda dsn: calls.append(dsn) or Provider())
    assert exc.value.retired_keys == RETIRED_DB_TRANSPORT_KEYS
    assert calls == []
    assert str(exc.value) == 'retired_bridge_configuration:DB_ALLOW_BRIDGE_IN_PROD,DB_BRIDGE_URL,DB_FORCE_BRIDGE'

def test_direct_success_has_one_health_and_selection_evidence():
    p=Provider(); db=DBAccess.for_current_env(environ={'DATABASE_URL':'secret'}, psycopg_factory=lambda dsn:p)
    assert p.health_calls == 1
    assert db.provider_name == 'psycopg'
    assert db.selection_evidence()['alternate_transport_attempts'] == 0
    assert list(db.attempts) == [{'provider':'psycopg','status':'ok','reason':None}]

def test_missing_database_url_fails_closed():
    with pytest.raises(PrimaryUnavailable) as exc:
        DBAccess.for_current_env(environ={}, psycopg_factory=lambda dsn: Provider())
    assert exc.value.code == 'missing_database_url'

def test_readonly_tx_rejects_bad_first_and_mutation():
    provider = PsycopgProvider('postgresql://example', connection_factory=lambda dsn: object())
    with pytest.raises(TxError):
        provider.readonly_tx([Statement('SELECT 1', fetch=True)])
    with pytest.raises(TxError):
        provider.readonly_tx([Statement('SET TRANSACTION READ ONLY'), Statement('DELETE FROM x')])
