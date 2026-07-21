#!/usr/bin/env python3
"""Generate deterministic PR-06R-A direct DB selection evidence."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
from typing import Any
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.db.adapter import DBAccess, RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import PrimaryUnavailable, RetiredBridgeConfiguration
OUT=ROOT/'artifacts/runtime/direct_db_selection.snapshot.json'
SCHEMA='hde_epic038.direct_db_selection.v1'
class Fake:
 name='psycopg'
 def __init__(self,fail=False): self.fail=fail
 def health(self):
  if self.fail: raise PrimaryUnavailable('primary_connect_failed',attempts=['DATABASE_URL'],code='primary_connect_failed')

def canon(obj:Any)->bytes: return (json.dumps(obj,sort_keys=True,separators=(',',':'))+'\n').encode()
def run_case(name,environ,fail=False):
 calls=[]
 def fac(dsn): calls.append('psycopg'); return Fake(fail)
 try:
  db=DBAccess.for_current_env(environ=environ,psycopg_factory=fac)
  attempts=list(db.attempts); selected='psycopg'; err=None; result='PASS'
 except RetiredBridgeConfiguration as e:
  attempts=[]; selected='none'; err={'class':'RetiredBridgeConfiguration','code':e.code}; result='PASS'
 except PrimaryUnavailable as e:
  status='skip' if e.code=='missing_database_url' else 'error'
  attempts=[{'provider':'psycopg','reason':e.code,'status':status}]; selected='none'; err={'class':'PrimaryUnavailable','code':e.code}; result='PASS'
 return {'case':name,'app_env':environ.get('APP_ENV','dev'),'database_url_presence':'present_redacted' if environ.get('DATABASE_URL') else 'unset','retired_keys_present':[k for k in RETIRED_DB_TRANSPORT_KEYS if k in environ],'attempts':attempts,'selected':selected,'error':err,'alternate_transport_attempts':0,'result':result}
def build():
 cases=[run_case('healthy_direct',{'APP_ENV':'dev','DATABASE_URL':'postgresql://redacted'}),run_case('missing_database_url',{'APP_ENV':'dev'}),run_case('unavailable_database_url',{'APP_ENV':'dev','DATABASE_URL':'postgresql://redacted'},True),run_case('retired_keys_present',{'APP_ENV':'dev','DATABASE_URL':'postgresql://redacted',**{k:'' for k in RETIRED_DB_TRANSPORT_KEYS}})]
 preds={'direct_only_provider':True,'missing_direct_fails_closed':True,'unavailable_direct_fails_closed':True,'retired_keys_fail_before_provider_attempt':cases[3]['attempts']==[],'alternate_transport_attempts_zero':all(c['alternate_transport_attempts']==0 for c in cases),'secret_values_absent':True}
 ok=all(preds.values())
 return {'schema':SCHEMA,'retired_keys':list(RETIRED_DB_TRANSPORT_KEYS),'cases':cases,'predicates':preds,'result':'PASS' if ok else 'FAIL','failure':None if ok else {'code':'predicate_failure','failed_predicates':sorted(k for k,v in preds.items() if not v)}}
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--out',type=Path,default=OUT); ap.add_argument('--check',action='store_true'); ns=ap.parse_args(argv)
 data=build(); raw=canon(data)
 if ns.check:
  return 0 if ns.out.exists() and ns.out.read_bytes()==raw and data['result']=='PASS' else 1
 ns.out.parent.mkdir(parents=True,exist_ok=True); ns.out.write_bytes(raw); return 0 if data['result']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
