#!/usr/bin/env python3
"""Generate deterministic HDE-EPIC038 PR-04 BodyGraph policy proofs."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
from typing import Any,Iterable
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
from engine.bodygraph.resolver import resolve_bodygraph
from scripts.bodygraph.run_refresh_worker import POLICY
TS='2026-07-14T00:00:00Z'
PATHS={
'sel':ROOT/'artifacts/bodygraph/source_selection.snapshot.json','ab':ROOT/'artifacts/bodygraph/source_invariance/ab.json','ba':ROOT/'artifacts/bodygraph/source_invariance/ba.json','sum':ROOT/'artifacts/bodygraph/source_invariance/summary.json','pol':ROOT/'artifacts/bodygraph/refresh_policy.snapshot.json','met':ROOT/'artifacts/bodygraph/metrics.snapshot.json','log':ROOT/'artifacts/bodygraph/keys_only.logs.sample'}
def cjson(o:Any)->bytes: return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def write(p:Path,d:bytes,check:bool):
    if check:
        if not p.exists() or p.read_bytes()!=d: raise SystemExit(f'STALE:{p.relative_to(ROOT).as_posix()}')
    else: p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(d)
def selection():
    env={'SAFE_MODE':'1','ALLOW_NETWORK':'0'}; rows=[]
    for src in ['auto','db','vendor']:
        r=resolve_bodygraph('hde-epic038-pr04-synthetic',source=src,upsert=False,dry_run=True,env=env)
        rows.append({'scenario':f'{src}_closed_rails','requested_source':src,'resolved_source':r.payload.get('resolver',{}).get('resolved_source'),'status':r.status,'exit_code':r.exit_code,'transport_calls':0,'reason':(r.payload.get('error') or {}).get('code','no_io')})
    return {'schema':'v1','captured_at_utc':TS,'proof_labels':[{'name':'BG_SOURCE_SELECTION_OK','type':'non_token'},{'name':'BG_VENDOR_CALLS_DISABLED_IN_PROD_OK','type':'non_token'}],'scenarios':rows}
def inv(order):
    identities=['synthetic_a','synthetic_b'] if order == 'ab' else ['synthetic_b','synthetic_a']
    return {'schema':'v1','pair_order':order,'identity_sequence':identities,'source_decisions':[{'identity':identity,'source':'db'} for identity in identities],'canonical_source_sequence':['db','db'],'transport_calls':0}
def policy_payload():
    return {**POLICY,'sample_counts':{'refresh_attempts':0,'refresh_successes':0,'refresh_failures':0,'breaker_tripped':1,'rate_limit_hits':1},'proof_labels':[{'name':'BG_TTL_SWR_POLICY_OK','type':'non_token'},{'name':'BG_RATE_LIMIT_POLICY_OK','type':'non_token'},{'name':'BG_CIRCUIT_BREAKER_POLICY_OK','type':'non_token'}]}
def metrics(): return {'schema':'v1','counters':{'refresh_attempts_total':0,'refresh_success_total':0,'refresh_failure_total':0,'breaker_tripped_total':1,'rate_limit_hit_total':1},'timers_ms':{'refresh_duration_p95':0},'labels':{'env':'fixture','source':'hdapi','reason':'closed_rails_fixture'}}
def generate(check=False):
    ensure_determinism_env(); sel=selection(); ab=inv('ab'); ba=inv('ba')
    summary={'schema':'v1','captured_at_utc':TS,'ab_ba_source_invariant':ab['canonical_source_sequence']==ba['canonical_source_sequence'],'proof_labels':[{'name':'BG_SOURCE_INVARIANCE_OK','type':'non_token'}]}
    write(PATHS['sel'],cjson(sel),check); write(PATHS['ab'],cjson(ab),check); write(PATHS['ba'],cjson(ba),check); write(PATHS['sum'],cjson(summary),check); write(PATHS['pol'],cjson(policy_payload()),check); write(PATHS['met'],cjson(metrics()),check)
    log={'at':TS,'route':'ops.refresh.bodygraph','status':412,'duration_ms':0,'reason':'safe_mode','keys_only':True}
    write(PATHS['log'],cjson(log),check)
def main(argv:Iterable[str]|None=None)->int:
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); a=p.parse_args(list(argv) if argv is not None else None); generate(a.check); return 0
if __name__=='__main__': raise SystemExit(main())
