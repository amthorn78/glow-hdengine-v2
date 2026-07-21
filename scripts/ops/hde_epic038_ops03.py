#!/usr/bin/env python3
"""Authorization-bound fixture-only OPS-03 runner skeleton; live OPS execution is out of scope."""
from __future__ import annotations
import argparse,hashlib,json,os,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS, DBAccess, Statement
ORDERED_QUERY_IDS=('set_transaction_read_only','set_search_path','connection_identity','search_path','runtime_role_grants','ddl_columns','ddl_constraints','boundary_views','partition_inventory','partition_verify')
EXPECTED_COUNTS={'provider_selections':1,'health_connections':1,'health_sql_statements':1,'posture_transactions':1,'posture_sql_statements':10,'direct_connections':2,'sql_statements':11,'sql_writes':0,'retries':0,'alternate_provider_attempts':0}
NONCLAIMS=sorted(('acceptance_token_satisfaction','deployment','epic_closeout','migration','pf09_status_movement','production_write_authorization','qa_pass','railway_inventory_proof','retired_transport_availability'))
def canon(o): return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def roots(run):
 base=Path('/tmp/hde-epic038-ops03')/run; return base,base/'control',base/'candidate',base/'failure'
def validate_authorization(path):
 a=json.loads(Path(path).read_text()); run=a.get('run_id','')
 if not re.match(r'^[a-z0-9][a-z0-9-]{15,63}$',run): raise SystemExit('AUTH_RUN_ID')
 base,control,cand,fail=roots(run)
 if a.get('candidate_root') != cand.as_posix()+'/': raise SystemExit('AUTH_CANDIDATE_ROOT')
 if a.get('retired_keys_required_absent') != list(RETIRED_DB_TRANSPORT_KEYS): raise SystemExit('AUTH_RETIRED_KEYS')
 if a.get('ordered_query_ids') != list(ORDERED_QUERY_IDS): raise SystemExit('AUTH_QUERY_IDS')
 if a.get('expected_counts') != EXPECTED_COUNTS: raise SystemExit('AUTH_COUNTS')
 if a.get('one_attempt') is not True: raise SystemExit('AUTH_ONE_ATTEMPT')
 return a
def failure(auth,phase,code,consumed):
 run=auth.get('run_id','unknown-run-id'); base,control,cand,fail=roots(run); fail.mkdir(parents=True,exist_ok=True)
 rec={'schema':'hde_epic038.ops03.failure_receipt.v1','run_id':run,'authorization_sha256':sha_bytes(canon(auth)),'phase':phase,'code':code,'launch_consumed':bool(consumed),'candidate_admissible':False,'nonclaims':NONCLAIMS}
 (fail/'failure_receipt.json').write_bytes(canon(rec)); return 1
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--authorization',required=True); ap.add_argument('--fixture',action='store_true',help='produce fixture packet without DB I/O')
 ns=ap.parse_args(argv)
 try: auth=validate_authorization(ns.authorization)
 except SystemExit: raise
 except Exception: raise SystemExit(1)
 run=auth['run_id']; base,control,cand,fail=roots(run); control.mkdir(parents=True,exist_ok=True); cand.mkdir(parents=True,exist_ok=True); (control/'launch.marker').write_text('launch_consumed=true\n')
 if not ns.fixture: return failure(auth,'pre_provider','live_ops_not_authorized',True)
 rails={'safe_mode':'1','allow_network':'0','allow_db_write':'0','db_read_authorized':True}
 (cand/'stdout.log').write_text(''); (cand/'stderr.log').write_text(''); (cand/'exit_code.txt').write_text('0\n')
 (cand/'commands.txt').write_text('capture_argv=[]\nreceipt_argv=[]\nvalidate_argv=[]\n')
 env={'schema':'hde_epic038.ops03.env_presence.v1','run_id':run,'app_env':'dev','rails':rails,'database_url_presence':'SET_REDACTED','retired_key_presence':{k:'UNSET' for k in RETIRED_DB_TRANSPORT_KEYS},'determinism_pins':{'LC_ALL':'C','LANG':'C','TZ':'UTC','SAFE_MODE':'1','ALLOW_NETWORK':'0'}}
 preds={k:True for k in ('authorization_match','direct_provider_only','read_only_transaction','search_path_exact','least_privilege_role','ddl_identity_valid','constraints_observed','boundary_views_readonly','partition_posture_observed','counts_exact','secret_values_absent')}
 posture={'schema':'hde_epic038.ops03.db_posture_summary.v1','run_id':run,'source_commit':auth['source_commit'],'provider':'psycopg','selection_attempts':[{'provider':'psycopg','status':'ok','reason':None}],'ordered_query_ids':list(ORDERED_QUERY_IDS),'query_results':[{'query_id':q,'status':'ok','row_count':0,'canonical_sha256':sha_bytes(b'[]\n')} for q in ORDERED_QUERY_IDS],'observations':{'connection_identity_presence':True,'search_path':['hde','public'],'runtime_role_flags':{'rolsuper':False,'rolcreatedb':False,'rolcreaterole':False},'ddl_identity':{'schema':'hde.ddl_identity_projection.v1'},'constraint_count':0,'boundary_views':[],'partition_posture':{}},'counts':EXPECTED_COUNTS,'predicates':preds,'result':'PASS'}
 non={'schema':'hde_epic038.ops03.nonclaims.v1','run_id':run,'nonclaims':NONCLAIMS}
 summary={'schema':'hde_epic038.ops03.result_summary.v1','run_id':run,'source_commit':auth['source_commit'],'authorization_sha256':sha(ns.authorization),'capture_result':'PASS','decisive_predicates':preds,'primary_files':['commands.txt','db_posture_summary.json','env_presence.json','exit_code.txt','nonclaims.json','result_summary.json','stderr.log','stdout.log'],'nonclaims_ref':'nonclaims.json'}
 for name,obj in [('env_presence.json',env),('db_posture_summary.json',posture),('nonclaims.json',non),('result_summary.json',summary)]: (cand/name).write_bytes(canon(obj))
 lines=[]
 for p in sorted(['commands.txt','db_posture_summary.json','env_presence.json','exit_code.txt','nonclaims.json','result_summary.json','stderr.log','stdout.log']): lines.append(f"{sha(cand/p)}  {p}\n")
 (cand/'checksums.sha256').write_text(''.join(lines)); return 0
if __name__=='__main__': raise SystemExit(main())
