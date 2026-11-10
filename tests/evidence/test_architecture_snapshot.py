import json
import os
import shutil
import subprocess
import sys
from pathlib import Path
import pytest

from tools.evidence import generate_architecture_snapshot as architecture

ROOT=Path(__file__).resolve().parents[2]
def test_current_architecture_analysis_is_read_only_and_fail_closed():
    frozen=ROOT/'artifacts/architecture/architecture_snapshot.keys_only.json'
    before=frozen.read_bytes()
    p=architecture.analyze(); architecture.validate(p)
    assert frozen.read_bytes()==before
    assert set(p['taxonomy'])=={'allowed','forbidden','unknown','out_of_scope'}; assert p['verdict']==p['analyzer_verdict']=='pass'; assert p['unknown_count']==0
    compat=[r for r in p['routes'] if r['path']=='engine/http/compat_handler.py']
    assert compat and compat[0]['classification']=='allowed'
    raw=json.dumps(p, sort_keys=True); assert 'DATABASE_URL' not in raw and 'birthdate' not in raw and 'Authorization' not in raw
    wsgi=[row for row in p['routes'] if row['path']=='adapter/wsgi.py']
    assert {(row['method'], row['route_path']) for row in wsgi} >= {
        ('get','/internal/healthz'), ('get','/internal/readyz')
    }
    registrations=[row for row in p['registrations'] if row['path']=='adapter/wsgi.py']
    assert {row['blueprint_symbol'] for row in registrations} >= {'reader_bp','compat_blueprint'}
    selected_registrations=[row for row in p['registrations'] if row['path']=='adapter/factory.py']
    assert {row['blueprint_symbol'] for row in selected_registrations} >= {'bp','compat_blueprint'}
    assert not [row for row in p['routes'] if row['path']=='engine/db/providers/bridge_provider.py']

def test_architecture_unknown_fail_closed():
    import tools.evidence.generate_architecture_snapshot as g
    payload=g.analyze(); payload['routes'].append({'path':'fixture.py','classification':'unknown'})
    with pytest.raises(SystemExit): g.validate(payload)
    payload=g.analyze(); payload['findings'][0]['classification']='mystery'
    with pytest.raises(SystemExit): g.validate(payload)

@pytest.mark.parametrize('missing_symbol', ['bp', 'compat_blueprint'])
def test_selected_factory_blueprint_registration_fails_closed(missing_symbol):
    import tools.evidence.generate_architecture_snapshot as g
    payload=g.analyze()
    payload['registrations']=[
        row for row in payload['registrations']
        if not (
            row.get('path') == 'adapter/factory.py'
            and row.get('blueprint_symbol') == missing_symbol
        )
    ]
    with pytest.raises(SystemExit, match='SELECTED_FACTORY_BLUEPRINT_REGISTRATION_MISSING'):
        g.validate(payload)

def test_architecture_route_symbol_analysis_excludes_ordinary_get_and_fails_unknown():
    import tools.evidence.generate_architecture_snapshot as g
    source='''\nfrom flask import Flask, Blueprint\napp = Flask(__name__)\nbp = Blueprint("bp", __name__)\nvalue = mapping.get("key")\nclient.get("/not-a-decorator")\n@app.get("/healthz")\ndef healthz(): pass\n@bp.post("/items")\ndef items(): pass\napp.add_url_rule("/readyz", endpoint="readyz")\napp.register_blueprint(bp)\n@unknown.get("/mystery")\ndef mystery(): pass\n'''
    result=g.analyze_source('fixture.py', source)
    assert len(result.routes)==4
    assert [row for row in result.routes if row['classification']=='unknown'] == [
        next(row for row in result.routes if row['route_path']=='/mystery')
    ]
    assert len(result.registrations)==1


# HDE-CRD-0003 S12: a change that leaves the stored snapshot stale fails --check.
# The generator binds ROOT, ART, SCHEMA and tracked() to its own location, so the
# proof runs the generator inside a repository copy, regenerated first. It never
# compares this checkout's stored snapshot (HDE Build Notes 2.1 R-3).
_GENERATOR = 'tools/evidence/generate_architecture_snapshot.py'
_ART = 'artifacts/architecture/architecture_snapshot.keys_only.json'
_SCHEMA = 'schemas/architecture_snapshot.keys_only.v1.json'


def _run_generator(copy, *args):
    env = {key: value for key, value in os.environ.items() if key != 'PYTHONPATH'}
    env.update(LC_ALL='C', LANG='C', TZ='UTC', SAFE_MODE='1', ALLOW_NETWORK='0', PYTHONDONTWRITEBYTECODE='1')
    return subprocess.run(
        [sys.executable, str(copy / _GENERATOR), *args],
        cwd=copy, env=env, capture_output=True, text=True, check=False,
    )


@pytest.fixture(scope='module')
def regenerated_copy(tmp_path_factory):
    copy = tmp_path_factory.mktemp('architecture_copy') / 'repo'
    listed = subprocess.run(
        ['git', 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
        cwd=ROOT, capture_output=True, check=True,
    ).stdout.decode('utf-8').split('\0')
    for rel in filter(None, listed):
        source = ROOT / rel
        if not source.is_symlink() and not source.is_file():
            continue
        target = copy / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target, follow_symlinks=False)
    subprocess.run(['git', 'init', '-q', str(copy)], check=True)
    written = _run_generator(copy)
    assert (written.returncode, written.stdout, written.stderr) == (0, '', '')
    # The copy's snapshot is this checkout's current analysis.
    assert (copy / _ART).read_bytes() == architecture.cjson(architecture.analyze())
    assert (copy / _SCHEMA).read_bytes() == architecture.cjson(architecture.schema_payload())
    current = _run_generator(copy, '--check')
    assert (current.returncode, current.stdout, current.stderr) == (0, '', '')
    return copy


def _add_module(copy):
    (copy / 'engine/s12_unregenerated_module.py').write_text('import json\n', encoding='utf-8')


def _add_import(copy):
    path = copy / 'engine/runtime/determinism_env.py'
    path.write_text(path.read_text(encoding='utf-8') + 'import socket\n', encoding='utf-8')


def _remove_module(copy):
    removable = [
        p for p in architecture.tracked()
        if p != architecture.SELECTED_FACTORY and not p.startswith('engine/runtime/') and not p.endswith('__init__.py')
    ]
    (copy / removable[0]).unlink()


def _edit_snapshot(copy):
    (copy / _ART).write_bytes(b'{}\n')


def _edit_schema(copy):
    (copy / _SCHEMA).write_bytes(b'{}\n')


@pytest.mark.parametrize(('make_stale', 'stale_path'), [
    (_add_module, _ART),
    (_add_import, _ART),
    (_remove_module, _ART),
    (_edit_snapshot, _ART),
    (_edit_schema, _SCHEMA),
])
def test_stale_snapshot_fails_check(regenerated_copy, tmp_path, make_stale, stale_path):
    copy = tmp_path / 'repo'
    shutil.copytree(regenerated_copy, copy, symlinks=True)
    make_stale(copy)
    stored = {rel: (copy / rel).read_bytes() for rel in (_ART, _SCHEMA)}
    result = _run_generator(copy, '--check')
    assert result.returncode == 1
    assert result.stdout == ''
    assert result.stderr == f'STALE:{stale_path}\n'
    assert {rel: (copy / rel).read_bytes() for rel in (_ART, _SCHEMA)} == stored
