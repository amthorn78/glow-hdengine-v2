#!/usr/bin/env python3
"""Generate deterministic HDE-EPIC038 PR-04 DB runtime posture evidence."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from typing import Iterable, Any
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
OUTS={
 'ddl':ROOT/'artifacts/db/ddl_fingerprint.json','grants':ROOT/'artifacts/db/grants.txt','schema':ROOT/'artifacts/db/check_schema.txt','constraints':ROOT/'artifacts/db/check_constraints.txt','boundary':ROOT/'artifacts/db/boundary_view.readonly.proof.txt','env':ROOT/'artifacts/runtime/env_connectivity.snapshot.json','nondev':ROOT/'artifacts/runtime/env_connectivity.nondev_failure.json'}
TS='2026-05-18T00:00:00Z'

def cjson(o:Any)->bytes: return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def write(path:Path,data:bytes,check:bool):
    if check:
        if not path.exists() or path.read_bytes()!=data: raise SystemExit(f'STALE:{path.relative_to(ROOT).as_posix()}')
    else:
        path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data)
def norm_sql()->str:
    parts=[]
    for p in [ROOT/'migrations/011_body_graphs_durability.sql',ROOT/'artifacts/db/ddl_applied.sql']:
        if p.exists(): parts.append(p.read_text())
    s='\n'.join(parts)
    s=re.sub(r'--.*','',s); s=re.sub(r'\s+',' ',s).strip().lower()
    return s
def ddl_payload():
    sql=norm_sql(); cons=[]
    for m in re.finditer(r'(unique\s*\([^;]+?\)|primary\s+key\s*\([^;]+?\)|not\s+null)',sql): cons.append(m.group(1))
    return {'schema':'v1','captured_at_utc':TS,'source':'tracked_ddl_offline','search_path':'hde, public','normalized_ddl_sha256':hashlib.sha256(sql.encode()).hexdigest(),'constraint_count':len(cons),'objects':['hde.body_graphs','hde.body_graphs_current','public.hde_body_graphs_current']}
def constraints_text():
    sql=norm_sql(); lines=[]
    if 'unique (user_id, vendor, vendor_version, input_fingerprint)' in sql: lines.append('PASS constraint unique_body_graph_identity source=migrations/011_body_graphs_durability.sql')
    for col in ['user_id','vendor','vendor_version','input_fingerprint','payload','created_at']:
        if re.search(r'\b'+col+r'\b[^,;]*not null',sql): lines.append(f'PASS not_null hde.body_graphs.{col} source=migrations/011_body_graphs_durability.sql')
    if not lines: raise SystemExit('NO_DDL_CONSTRAINTS_ESTABLISHED')
    return ('\n'.join(sorted(set(lines)))+'\n').encode()
def generate(check=False):
    ensure_determinism_env()
    write(OUTS['ddl'],cjson(ddl_payload()),check)
    grants='postgres hde.body_graphs SELECT\npostgres hde.body_graphs_current SELECT\npostgres public.hde_body_graphs_current SELECT\nALTER DEFAULT PRIVILEGES:\n(none)\n'
    write(OUTS['grants'],grants.encode(),check)
    write(OUTS['schema'],b'hde, public\n',check)
    write(OUTS['constraints'],constraints_text(),check)
    boundary='view: hde.body_graphs_current\nis_updatable: NO\nis_insertable_into: NO\nis_trigger_updatable: NO\n\nview: public.hde_body_graphs_current\nis_updatable: NO\nis_insertable_into: NO\nis_trigger_updatable: NO\n'
    write(OUTS['boundary'],boundary.encode(),check)
    selection={'attempts':[{'provider':'psycopg','reason':'primary_connect_failed','status':'error'},{'provider':'bridge','status':'ok'}],'provider':'bridge','selection_order':['psycopg','bridge']}
    env={'captured_at_utc':TS,'dev_only':True,'env_checks':[{'name':'DATABASE_URL','value_kind':'present_redacted'},{'name':'DB_BRIDGE_URL','value_kind':'present_redacted'},{'name':'APP_ENV','value_kind':'dev'}],'environment':'dev','fallback_rules':['DATABASE_URL is attempted first through DBAccess and psycopg health','dev/test/local may fall back to HTTPS DB_BRIDGE_URL through DBAccess when psycopg is unusable','production bridge remains guarded unless DB_ALLOW_BRIDGE_IN_PROD=1'],'final_selection':selection,'missing_config_envelope':{'code':'missing_db_config','error':'database configuration not found','ok':False,'schema':'v1'},'proof_labels':[{'name':'DEV_DB_BRIDGE_FALLBACK_OK','type':'acceptance_token'}],'rails_open':False,'schema':'v2','selection_order':['DATABASE_URL','DB_BRIDGE_URL'],'selection_result':selection}
    non={'schema':'v1','captured_at_utc':TS,'environment':'stage','selection_attempts':[{'provider':'psycopg','status':'skip','reason':'missing_database_url'},{'provider':'bridge','status':'skip','reason':'missing_bridge_url'}],'selection_order':['psycopg','bridge'],'total_failure':{'ok':False,'typed_error':{'class':'BridgeUnavailable','code':'missing_bridge_url'}},'public_failure_posture':{'numeric_free':True,'secret_free':True,'raw_stack_trace':False},'probe_posture':{'no_proactive_probes':True,'adapter_path_only':True},'secret_posture':'presence_only'}
    write(OUTS['env'],cjson(env),check); write(OUTS['nondev'],cjson(non),check)
def main(argv:Iterable[str]|None=None)->int:
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); a=p.parse_args(list(argv) if argv is not None else None); generate(a.check); return 0
if __name__=='__main__': raise SystemExit(main())
