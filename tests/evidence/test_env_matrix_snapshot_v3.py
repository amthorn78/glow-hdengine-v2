import json, subprocess
from pathlib import Path

def test_env_matrix_v3_presence_only_and_check_nonwriting(monkeypatch):
    path = Path('artifacts/runtime/env_matrix.snapshot.json')
    before = path.read_bytes() if path.exists() else b''
    subprocess.run(['python','tools/evidence/generate_env_matrix_snapshot.py','--check'], check=True)
    assert path.read_bytes() == before
    assert before.endswith(b'\n') and b'\n' not in before[:-1]
    data = json.loads(before)
    assert data['schema_version'] == 3
    assert data['rails'] == {'ALLOW_NETWORK':'0','LANG':'C','LC_ALL':'C','SAFE_MODE':'1','TZ':'UTC'}
    assert set(data['presence']) == {'DATABASE_URL','DB_BRIDGE_URL','DB_ALLOW_BRIDGE_IN_PROD'}
    assert all(isinstance(v, bool) for v in data['presence'].values())
