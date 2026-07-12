import hashlib, json, subprocess
from pathlib import Path
from engine.runtime.identity import identity_admin

def test_release_bindings_integrity_and_check_nonwriting():
    path = Path('artifacts/bodygraph/release_bindings.json')
    before = path.read_bytes() if path.exists() else b''
    subprocess.run(['python','tools/evidence/generate_release_bindings.py','--check'], check=True)
    assert path.read_bytes() == before
    data = json.loads(path.read_text())
    assert data['release_id'] == identity_admin()['release_id']
    for item in data['bindings']:
        p = Path(item['path'])
        assert item['sha256'] == hashlib.sha256(p.read_bytes()).hexdigest()
        assert item['size_bytes'] == p.stat().st_size
