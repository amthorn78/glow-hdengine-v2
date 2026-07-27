import hashlib,json,os,subprocess,pytest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ENV={**os.environ,'SAFE_MODE':'1','ALLOW_NETWORK':'0','LC_ALL':'C','LANG':'C','TZ':'UTC'}
def run(a): return subprocess.run(['python',*a],cwd=ROOT,env=ENV,check=True,capture_output=True,text=True)
def test_architecture_snapshot_taxonomy_schema_and_check():
    paths=['artifacts/architecture/architecture_snapshot.keys_only.json','schemas/architecture_snapshot.keys_only.v1.json']
    run(['tools/evidence/generate_architecture_snapshot.py','--check'])
    run(['tools/evidence/generate_architecture_snapshot.py']); h1={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    run(['tools/evidence/generate_architecture_snapshot.py']); h2={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}; assert h1==h2
    run(['tools/evidence/generate_architecture_snapshot.py','--check']); assert h2=={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    p=json.loads((ROOT/paths[0]).read_text()); assert set(p['taxonomy'])=={'allowed','forbidden','unknown','out_of_scope'}; assert p['verdict']==p['analyzer_verdict']=='pass'; assert p['unknown_count']==0
    compat=[r for r in p['routes'] if r['path']=='engine/http/compat_handler.py']
    assert compat and compat[0]['classification']=='allowed'
    raw=(ROOT/paths[0]).read_text(); assert 'DATABASE_URL' not in raw and 'birthdate' not in raw and 'Authorization' not in raw
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
