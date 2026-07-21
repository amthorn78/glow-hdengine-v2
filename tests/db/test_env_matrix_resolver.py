from adapter.db_access import resolve_env_matrix

def test_env_matrix_direct_success(monkeypatch):
    monkeypatch.setenv('DATABASE_URL','postgresql://secret')
    for k in ('DB_ALLOW_BRIDGE_IN_PROD','DB_BRIDGE_URL','DB_FORCE_BRIDGE'): monkeypatch.delenv(k, raising=False)
    ok,payload=resolve_env_matrix()
    assert ok is True
    assert payload['schema']=='hde.db.env_selection.v2'
    assert payload['result']=={'provider':'psycopg'}
    assert payload['error'] is None

def test_env_matrix_retired_key_refusal(monkeypatch):
    monkeypatch.setenv('DATABASE_URL','postgresql://secret')
    monkeypatch.setenv('DB_BRIDGE_URL','')
    ok,payload=resolve_env_matrix()
    assert ok is False
    assert payload['error']=={'class':'RetiredBridgeConfiguration','code':'retired_bridge_configuration','retired_keys':['DB_BRIDGE_URL']}

def test_env_matrix_missing_direct(monkeypatch):
    monkeypatch.delenv('DATABASE_URL', raising=False)
    for k in ('DB_ALLOW_BRIDGE_IN_PROD','DB_BRIDGE_URL','DB_FORCE_BRIDGE'): monkeypatch.delenv(k, raising=False)
    ok,payload=resolve_env_matrix()
    assert ok is False
    assert payload['result'] is None
    assert payload['error']['code']=='missing_database_url'
