import json, subprocess
from pathlib import Path

import pytest

from tools.evidence import generate_env_matrix_snapshot as generator

PINS = {'ALLOW_NETWORK':'0','LANG':'C','LC_ALL':'C','SAFE_MODE':'1','TZ':'UTC'}
OPTIONAL_DB_ENV = ('DATABASE_URL','DB_BRIDGE_URL','DB_ALLOW_BRIDGE_IN_PROD')


def _set_closed_rails(monkeypatch):
    for key, value in PINS.items():
        monkeypatch.setenv(key, value)


def test_env_matrix_v3_write_is_independent_of_optional_db_env(tmp_path, monkeypatch):
    _set_closed_rails(monkeypatch)
    out = tmp_path / 'env_matrix.snapshot.json'
    monkeypatch.setattr(generator, 'OUT', out)

    for key in OPTIONAL_DB_ENV:
        monkeypatch.delenv(key, raising=False)
    assert generator.main([]) == 0
    without_optional_env = out.read_bytes()

    for key in OPTIONAL_DB_ENV:
        monkeypatch.setenv(key, 'operator-specific-value')
    assert generator.main([]) == 0

    assert out.read_bytes() == without_optional_env
    assert json.loads(without_optional_env) == {'schema_version': 3, 'rails': PINS}


def test_env_matrix_v3_check_is_exact_and_nonwriting(monkeypatch):
    _set_closed_rails(monkeypatch)
    for key in OPTIONAL_DB_ENV:
        monkeypatch.setenv(key, 'operator-specific-value')

    path = Path('artifacts/runtime/env_matrix.snapshot.json')
    before = path.read_bytes()
    subprocess.run(['python','tools/evidence/generate_env_matrix_snapshot.py','--check'], check=True)

    assert path.read_bytes() == before
    assert before.endswith(b'\n') and b'\n' not in before[:-1]
    assert json.loads(before) == {'schema_version': 3, 'rails': PINS}
    assert all(key.encode() not in before for key in OPTIONAL_DB_ENV)


def test_env_matrix_v3_check_rejects_operator_specific_presence(tmp_path, monkeypatch):
    _set_closed_rails(monkeypatch)
    out = tmp_path / 'env_matrix.snapshot.json'
    monkeypatch.setattr(generator, 'OUT', out)
    drift = {
        'schema_version': 3,
        'rails': PINS,
        'presence': {key: True for key in OPTIONAL_DB_ENV},
    }
    out.write_text(json.dumps(drift, sort_keys=True, separators=(',', ':')) + '\n', encoding='utf-8')

    with pytest.raises(SystemExit) as exc:
        generator.main(['--check'])
    assert str(exc.value).startswith('DRIFT:')


def test_rails_closed_phase1_delegates_env_matrix_ownership():
    source = Path('tools/evidence/generate_rails_closed_phase1.py').read_text(
        encoding='utf-8'
    )

    assert 'generate_env_matrix_snapshot.main([])' in source
    assert 'db_access.resolve_env_matrix()' not in source
    assert '_write_json("artifacts/runtime/env_matrix.snapshot.json"' not in source
