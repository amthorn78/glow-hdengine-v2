import hashlib, json, os, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ENV={**os.environ,'SAFE_MODE':'1','ALLOW_NETWORK':'0','LC_ALL':'C','LANG':'C','TZ':'UTC'}
def run(args): return subprocess.run(['python',*args],cwd=ROOT,env=ENV,check=True,capture_output=True,text=True)
def assert_lf(p):
    b=(ROOT/p).read_bytes(); assert b.endswith(b'\n') and not b.endswith(b'\n\n') and b'\r\n' not in b
def test_db_runtime_outputs_and_check_residue():
    proof=ROOT/'artifacts/db/boundary_view.readonly.proof.txt.path_proof.txt'; before=proof.read_bytes() if proof.exists() else b''
    run(['tools/evidence/generate_db_runtime_posture.py'])
    after=proof.read_bytes() if proof.exists() else b''; assert before==after
    paths=['artifacts/db/ddl_fingerprint.json','artifacts/db/grants.txt','artifacts/db/check_schema.txt','artifacts/db/check_constraints.txt','artifacts/db/boundary_view.readonly.proof.txt','artifacts/runtime/env_connectivity.snapshot.json','artifacts/runtime/env_connectivity.nondev_failure.json']
    h1={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    run(['tools/evidence/generate_db_runtime_posture.py']); h2={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}; assert h1==h2
    run(['tools/evidence/generate_db_runtime_posture.py','--check']); h3={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}; assert h2==h3
    for p in paths: assert_lf(p)
    assert (ROOT/'artifacts/db/check_schema.txt').read_text()=='hde, public\n'
    assert 'PASS constraint unique_body_graph_identity' in (ROOT/'artifacts/db/check_constraints.txt').read_text()
    boundary=(ROOT/'artifacts/db/boundary_view.readonly.proof.txt').read_text(); assert 'is_updatable: NO' in boundary and 'is_insertable_into: NO' in boundary
    non=json.loads((ROOT/'artifacts/runtime/env_connectivity.nondev_failure.json').read_text()); assert non['selection_order']==['psycopg','bridge']; assert non['total_failure']['typed_error']['class']=='BridgeUnavailable'

def test_db_bridge_false_pass_and_fixture_separation():
    run(['tools/evidence/generate_db_bridge_parity.py'])
    p=json.loads((ROOT/'artifacts/db_bridge/provider_parity.proof.json').read_text())
    assert p['fixture_parity']['status']=='pass'
    assert p['live_provider_parity']['parity_status']!='pass'
    bad={'missing','skip','unavailable','not_exercised','error'}
    assert any(row['parity'] in bad or row['direct']['status'] in bad or row['bridge']['status'] in bad for row in p['capabilities'])
    run(['tools/evidence/generate_db_bridge_parity.py','--check'])
    assert (ROOT/'artifacts/bodygraph/vendor_upsert.epic038_synthetic.json').exists()
    assert (ROOT/'artifacts/bodygraph/db_resolve.epic038_synthetic.json').exists()
