import hashlib, json, subprocess
from pathlib import Path
import pytest
from engine.runtime.identity import identity_admin
from tools.evidence import generate_release_bindings as generator

def test_release_bindings_integrity_and_check_nonwriting():
    path = Path('artifacts/bodygraph/release_bindings.json')
    before = path.read_bytes() if path.exists() else b''
    subprocess.run(['python','tools/evidence/generate_release_bindings.py','--check'], check=True)
    assert path.read_bytes() == before
    data = json.loads(path.read_text())
    assert data['release_id'] == identity_admin()['release_id']
    assert [row['path'] for row in data['bindings']] == sorted(generator.INPUTS)
    for item in data['bindings']:
        p = Path(item['path'])
        assert item['sha256'] == hashlib.sha256(p.read_bytes()).hexdigest()
        assert item['size_bytes'] == p.stat().st_size

def test_release_bindings_fail_closed_for_missing_stale_unsorted_and_premature(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, 'ROOT', tmp_path)
    monkeypatch.setattr(generator, 'OUT', tmp_path/'release.json')
    for rel in generator.INPUTS:
        path=tmp_path/rel; path.parent.mkdir(parents=True, exist_ok=True)
        if rel.endswith('summary.json'):
            path.write_text('{"schema":"bodygraph.source_invariance.summary.v2","top_level_pass":true}\n')
        else:
            path.write_text('{}\n')
    generator.main([])
    (tmp_path/generator.INPUTS[0]).write_text('{"drift":true}\n')
    with pytest.raises(SystemExit, match='DRIFT:'):
        generator.main(['--check'])
    (tmp_path/generator.INPUTS[0]).unlink()
    with pytest.raises(SystemExit, match='MISSING:'):
        generator.main([])
    monkeypatch.setattr(generator, 'INPUTS', tuple(reversed(generator.INPUTS)))
    with pytest.raises(SystemExit, match='UNSORTED_BINDING_INPUTS'):
        generator.main([])

def test_release_bindings_reject_premature_source_invariance(tmp_path, monkeypatch):
    monkeypatch.setattr(generator, 'ROOT', tmp_path)
    monkeypatch.setattr(generator, 'OUT', tmp_path/'release.json')
    for rel in generator.INPUTS:
        path=tmp_path/rel; path.parent.mkdir(parents=True, exist_ok=True); path.write_text('{}\n')
    with pytest.raises(SystemExit, match='SOURCE_INVARIANCE_NOT_FINAL'):
        generator.main([])
