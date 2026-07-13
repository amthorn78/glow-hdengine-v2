#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json, os, re, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer import canon
from adapter.http_reader import create_app
TS=json.loads((ROOT/'catalog/manifest.json').read_text()).get('built_at_utc','2026-01-01T00:00:00Z')
DOC=ROOT/'docs/ENDPOINTS_CATALOG.json'; DOCSHA=ROOT/'docs/ENDPOINTS_CATALOG.json.sha256'; AUD=ROOT/'artifacts/audit/ENDPOINTS_CATALOG.json'; AUDSHA=ROOT/'artifacts/audit/ENDPOINTS_CATALOG.json.sha256'; SNAP=ROOT/'artifacts/reader/endpoints_snapshot.json'
PROOFS=[ROOT/'artifacts/proofs/endpoints_env_gate_proof.log',ROOT/'artifacts/proofs/success_get.txt',ROOT/'artifacts/proofs/success_head.txt',ROOT/'artifacts/proofs/success_304.txt',ROOT/'artifacts/proofs/success_writers_errors.txt',ROOT/'artifacts/proofs/success_encoding_invariance.txt',ROOT/'artifacts/proofs/reader_success_get_head_304.json']
ALL=[DOC,DOCSHA,AUD,AUDSHA,SNAP,*PROOFS]
CLASS={'internal_admin','dev_harness','internal_identity','public_reader'}
def sha(b): return hashlib.sha256(b).hexdigest()
def cjson(o): return json.dumps(o,separators=(',',':'),sort_keys=True).encode()+b'\n'
def catalog_obj():
 eps=[
 {'a7_eligible':False,'blueprint_module':'engine.http.compat_handler','classification':'internal_admin','description':'Compat pair endpoint (internal admin)','env_gate':'APP_ENV!=prod','internal':True,'method':'POST','path':'/api/compat/v1','rails_profile':'internal-admin writer no-store'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Conjunction reader preview route (dev-only)','env_gate':'APP_ENV in {dev,test,local}','internal':True,'method':'GET','path':'/dev/reader/conjunction','rails_profile':'dev-harness closed-by-default SAFE rails'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Conjunction writer preview route (dev-only)','env_gate':'APP_ENV in {dev,test,local}','internal':True,'method':'GET','path':'/dev/writer/conjunction','rails_profile':'dev-harness closed-by-default SAFE rails','route_id':'dev.writer.conjunction.v1'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Conjunction sampler preview route (dev-only)','env_gate':'APP_ENV in {dev,test,local}','internal':True,'method':'GET','path':'/dev/sampler/conjunction','rails_profile':'dev-harness closed-by-default SAFE rails'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'internal_identity','description':'Internal version endpoint for ops evidence','env_gate':'operator-network-only','internal':True,'method':'GET','path':'/internal/version','rails_profile':'ops-only no-store'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'internal_identity','description':'Internal version endpoint for ops evidence','env_gate':'operator-network-only','internal':True,'method':'HEAD','path':'/internal/version','rails_profile':'ops-only no-store'},
 {'a7_eligible':True,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Reader success route (dev-only governed A7 proof surface)','env_gate':'APP_ENV=dev','internal':True,'method':'GET','path':'/reader','rails_profile':'dev-harness reader a7'},
 {'a7_eligible':True,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Reader success route (dev-only governed A7 proof surface)','env_gate':'APP_ENV=dev','internal':True,'method':'HEAD','path':'/reader','rails_profile':'dev-harness reader a7'},]
 return {'endpoints':eps,'generated_at_utc':TS,'success_endpoints':[{'method':'GET','path':'/reader'}]}
def validate_catalog(cat):
 if set(cat)!={'endpoints','generated_at_utc','success_endpoints'}: raise ValueError('catalog top-level keys invalid')
 if not isinstance(cat['endpoints'],list) or not isinstance(cat['success_endpoints'],list): raise ValueError('catalog lists invalid')
 seen=set()
 for e in cat['endpoints']:
  for k in ['a7_eligible','blueprint_module','classification','description','env_gate','internal','method','path','rails_profile']:
   if k not in e: raise ValueError(f'missing {k}')
  if not isinstance(e['method'],str) or e['method']!=e['method'].upper(): raise ValueError('method must be uppercase string')
  if not isinstance(e['internal'],bool): raise ValueError('internal boolean required')
  if e['classification'] not in CLASS: raise ValueError('invalid classification')
  key=(e['method'],e['path'])
  if key in seen: raise ValueError('duplicate method/path')
  seen.add(key)
  if 'writer' in e['path'] and e['path']=='/dev/writer/conjunction' and e.get('route_id')!='dev.writer.conjunction.v1': raise ValueError('writer route_id invalid')
 des=cat['success_endpoints']
 if len(des)!=1: raise ValueError('exactly one success designation required')
 d=des[0]
 if set(d)!={'method','path'}: raise ValueError('invalid success designation shape')
 if d.get('path')=='/internal/version': raise ValueError('/internal/version rejected as A7 target')
 if d.get('method')!='GET': raise ValueError('A7 designation must be GET')
 matches=[e for e in cat['endpoints'] if e['method']==d['method'] and e['path']==d['path']]
 if len(matches)!=1: raise ValueError('success designation unresolved or ambiguous')
 e=matches[0]
 if e['path']!='/reader' or not e['a7_eligible'] or e['classification']!='dev_harness' or e['internal'] is not True: raise ValueError('invalid A7 target')
 return e
def headers(resp): return {k.lower():v for k,v in resp.headers.items()}
def q():
 return {'v':'1','a':str((ROOT/'fixtures/charts/alice.json').resolve()),'b':str((ROOT/'fixtures/charts/bob.json').resolve()),'a_tz':'UTC','b_tz':'UTC'}
def require(cond,msg):
 if not cond: raise AssertionError(msg)
def capture(client_factory=create_app):
 cat=catalog_obj(); target=validate_catalog(cat); app=client_factory(); c=app.test_client(); old=os.environ.get('APP_ENV')
 os.environ['APP_ENV']='dev'
 try:
  get=c.get(target['path'],query_string=q(),headers={'Accept-Encoding':'identity'}); hb=headers(get); body=get.data; et='"'+sha(body)+'"'
  require(get.status_code==200,'get status'); require(body.endswith(b'\n') and body,'get canonical body'); require(hb.get('content-type')=='application/json; charset=utf-8','ct'); require(hb.get('cache-control')=='private, max-age=0, must-revalidate','cache'); require('Authorization' in hb.get('vary','') and 'Accept-Encoding' in hb.get('vary',''),'vary'); require(hb.get('etag')==et,'etag'); require(hb.get('content-length')==str(len(body)),'cl')
  head=c.head(target['path'],query_string=q(),headers={'Accept-Encoding':'identity'}); hh=headers(head); require(head.status_code==200 and head.data==b'','head'); require(hh.get('etag')==et and hh.get('content-length')==str(len(body)) and hh.get('content-type')==hb.get('content-type'),'head parity')
  r304=c.get(target['path'],query_string=q(),headers={'If-None-Match':et}); h304=headers(r304); require(r304.status_code==304 and r304.data==b'','304'); require(h304.get('etag')==et and 'content-type' not in h304 and 'content-length' not in h304,'304 headers')
  post=c.post(target['path'],query_string=q(),headers={'If-None-Match':et}); hp=headers(post); require(post.status_code==405 and hp.get('cache-control')=='no-store' and 'etag' not in hp,'writer')
  enc=[]
  for ae in ['identity','gzip','br']:
   r=c.get(target['path'],query_string=q(),headers={'Accept-Encoding':ae}); hr=headers(r); require(hr.get('etag')==et,'encoding etag'); enc.append({'accept_encoding':ae,'content_encoding':hr.get('content-encoding','identity'),'etag':hr.get('etag')})
 finally:
  if old is None: os.environ.pop('APP_ENV',None)
  else: os.environ['APP_ENV']=old
 old=os.environ.get('APP_ENV'); os.environ['APP_ENV']='prod'
 try:
  prod=c.get('/reader',query_string=q()); ph=headers(prod); require(prod.status_code!=200 and ph.get('cache-control')=='no-store' and 'etag' not in ph,'env gate')
 finally:
  if old is None: os.environ.pop('APP_ENV',None)
  else: os.environ['APP_ENV']=old
 comp={'route_path':'/reader','captured_at_utc':TS,'env_gate':{'pass':True,'proof_path':'artifacts/proofs/endpoints_env_gate_proof.log','status':prod.status_code},'get_200':{'pass':True,'body_sha256':sha(body),'content_length':len(body),'headers':hb},'head_200':{'pass':True,'content_length':len(body),'headers':hh},'after_304':{'pass':True,'headers':h304,'status':304},'vary_flags':{'authorization':True,'accept_encoding':True},'etag':et,'tested_encodings':enc}
 return cat, body, comp
def validate_composite(obj):
 allowed={'route_path','captured_at_utc','env_gate','get_200','head_200','after_304','vary_flags','etag','tested_encodings'}
 if set(obj)!=allowed: raise ValueError('unknown or missing composite keys')
 if obj['route_path']!='/reader' or not re.fullmatch(r'"[0-9a-f]{64}"',obj['etag']): raise ValueError('bad composite')
 if obj['env_gate']['proof_path']!='artifacts/proofs/endpoints_env_gate_proof.log': raise ValueError('bad env proof')
 if not re.fullmatch(r'[0-9a-f]{64}',obj['get_200']['body_sha256']): raise ValueError('bad body sha')
 if [e['accept_encoding'] for e in obj['tested_encodings']]!=['identity','gzip','br']: raise ValueError('bad encodings')
def build():
 cat, body, comp=capture(); validate_composite(comp); catb=cjson(cat); snap=cjson({'json_success':[{'method':'GET','path':'/reader'}]})
 gh=comp['get_200']['headers']; hh=comp['head_200']['headers']
 outs={DOC:catb,DOCSHA:(f"{sha(catb)}  docs/ENDPOINTS_CATALOG.json\n").encode(),AUD:catb,AUDSHA:(f"{sha(catb)}  artifacts/audit/ENDPOINTS_CATALOG.json\n").encode(),SNAP:snap,PROOFS[0]:b'APP_ENV=prod\n/reader_success_unreachable=true\ncache_control=no-store\netag_absent=true\n',PROOFS[1]:(f"status=200\nbody_sha256={comp['get_200']['body_sha256']}\netag={comp['etag']}\ncontent-type={gh.get('content-type')}\ncache-control={gh.get('cache-control')}\nvary={gh.get('vary')}\ncontent-length={gh.get('content-length')}\n").encode(),PROOFS[2]:(f"status=200\nbody_empty=true\ncontent_length={comp['head_200']['content_length']}\netag={comp['etag']}\ncontent-type={hh.get('content-type')}\ncache-control={hh.get('cache-control')}\nvary={hh.get('vary')}\ncontent-length={hh.get('content-length')}\n").encode(),PROOFS[3]:(f"status=304\nbody_empty=true\ncontent_type_absent=true\ncontent_length_absent=true\netag={comp['etag']}\ncache-control={comp['after_304']['headers'].get('cache-control')}\nvary={comp['after_304']['headers'].get('vary')}\n").encode(),PROOFS[4]:b'POST /reader\nstatus=405\ncache_control=no-store\netag_absent=true\nconditional_not_304=true\n',PROOFS[5]:cjson({'tested_encodings':['identity','gzip','br'],'identity_etag':comp['etag'],'compression_claimed':False,'pass':True}),PROOFS[6]:cjson(comp)}
 return outs
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ns=ap.parse_args(); ensure_determinism_env(); outs=build()
 if ns.check:
  bad=[str(p.relative_to(ROOT)) for p,b in outs.items() if not p.exists() or p.read_bytes()!=b]
  if bad: raise SystemExit('DRIFT:'+','.join(bad))
  print('a7 transport proofs check ok'); return
 if os.environ.get('HDE_WRITE_A7_PROOFS')!='1': raise SystemExit('HDE_WRITE_A7_PROOFS_REQUIRED')
 for p,b in outs.items(): p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
 print('a7 transport proofs written')
if __name__=='__main__': main()
