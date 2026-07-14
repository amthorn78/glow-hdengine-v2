import hashlib,json,os,subprocess,pytest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ENV={**os.environ,'SAFE_MODE':'1','ALLOW_NETWORK':'0','LC_ALL':'C','LANG':'C','TZ':'UTC'}
def run(a): return subprocess.run(['python',*a],cwd=ROOT,env=ENV,check=True,capture_output=True,text=True)
def test_architecture_snapshot_taxonomy_schema_and_check():
    paths=['artifacts/architecture/architecture_snapshot.keys_only.json','schemas/architecture_snapshot.keys_only.v1.json']
    run(['tools/evidence/generate_architecture_snapshot.py']); h1={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    run(['tools/evidence/generate_architecture_snapshot.py']); h2={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}; assert h1==h2
    run(['tools/evidence/generate_architecture_snapshot.py','--check']); assert h2=={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    p=json.loads((ROOT/paths[0]).read_text()); assert set(p['taxonomy'])=={'allowed','forbidden','unknown','out_of_scope'}; assert p['verdict']==p['analyzer_verdict']=='pass'; assert p['unknown_count']==0
    raw=(ROOT/paths[0]).read_text(); assert 'DATABASE_URL' not in raw and 'birthdate' not in raw and 'Authorization' not in raw

def test_architecture_unknown_fail_closed():
    import tools.evidence.generate_architecture_snapshot as g
    payload=g.analyze(); payload['unknown_count']=1
    with pytest.raises(SystemExit): g.validate(payload)
    payload=g.analyze(); payload['findings'][0]['classification']='mystery'
    with pytest.raises(SystemExit): g.validate(payload)
