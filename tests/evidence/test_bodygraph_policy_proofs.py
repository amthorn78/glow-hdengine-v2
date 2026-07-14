import hashlib,json,os,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
ENV={**os.environ,'SAFE_MODE':'1','ALLOW_NETWORK':'0','LC_ALL':'C','LANG':'C','TZ':'UTC'}
def run(a): return subprocess.run(['python',*a],cwd=ROOT,env=ENV,check=True,capture_output=True,text=True)
def test_bodygraph_policy_deterministic_and_closed_rails():
    paths=['artifacts/bodygraph/source_selection.snapshot.json','artifacts/bodygraph/source_invariance/ab.json','artifacts/bodygraph/source_invariance/ba.json','artifacts/bodygraph/source_invariance/summary.json','artifacts/bodygraph/refresh_policy.snapshot.json','artifacts/bodygraph/metrics.snapshot.json','artifacts/bodygraph/keys_only.logs.sample']
    run(['tools/evidence/generate_bodygraph_policy_proofs.py']); h1={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    run(['tools/evidence/generate_bodygraph_policy_proofs.py']); h2={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}; assert h1==h2
    run(['tools/evidence/generate_bodygraph_policy_proofs.py','--check']); h3={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}; assert h2==h3
    sel=json.loads((ROOT/paths[0]).read_text()); vendor=[r for r in sel['scenarios'] if r['requested_source']=='vendor'][0]; assert vendor['transport_calls']==0 and vendor['reason']=='PROVIDER_REFUSED'
    summary=json.loads((ROOT/paths[3]).read_text()); assert summary['ab_ba_source_invariant'] is True
    pol=json.loads((ROOT/paths[4]).read_text()); assert pol['ttl_s'] and pol['swr_s'] and pol['rate_limit']['requests_per_window'] and pol['circuit_breaker']['fail_threshold']
    assert 'birth' not in (ROOT/paths[6]).read_text().lower()
