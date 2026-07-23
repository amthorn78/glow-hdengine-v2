import hashlib
import json
from pathlib import Path

import pytest

from engine.runtime.identity import identity_admin
from tools.evidence import generate_release_bindings as generator


def _assert_bindings(data: dict) -> None:
    assert [row["path"] for row in data["bindings"]] == sorted(generator.INPUTS)
    for item in data["bindings"]:
        path = Path(item["path"])
        assert item["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
        assert item["size_bytes"] == path.stat().st_size


def test_release_bindings_integrity_and_check_nonwriting(monkeypatch):
    for name, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }.items():
        monkeypatch.setenv(name, value)
    path = Path("artifacts/bodygraph/release_bindings.json")
    before = path.read_bytes()

    current = json.loads(generator._expected())
    assert current["release_id"] == identity_admin()["release_id"]
    _assert_bindings(current)

    frozen = json.loads(before)
    assert len(frozen["release_id"]) == 64
    _assert_bindings(frozen)
    assert path.read_bytes() == before

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
