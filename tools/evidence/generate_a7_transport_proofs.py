#!/usr/bin/env python3
from __future__ import annotations
import argparse, copy, hashlib, json, os, re, sys
from pathlib import Path
import jsonschema
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
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Internal dev sampler harness endpoint','env_gate':'APP_ENV in {dev,test,local}','internal':True,'method':'POST','path':'/internal/dev/sampler','rails_profile':'internal dev-harness writer no-store'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'internal_identity','description':'Internal version endpoint for ops evidence','env_gate':'operator-network-only','internal':True,'method':'GET','path':'/internal/version','rails_profile':'ops-only no-store'},
 {'a7_eligible':False,'blueprint_module':'adapter.http_reader','classification':'internal_identity','description':'Internal version endpoint for ops evidence','env_gate':'operator-network-only','internal':True,'method':'HEAD','path':'/internal/version','rails_profile':'ops-only no-store'},
 {'a7_eligible':True,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Reader success route (dev-only governed A7 proof surface)','env_gate':'APP_ENV=dev','internal':True,'method':'GET','path':'/reader','rails_profile':'dev-harness reader a7'},
 {'a7_eligible':True,'blueprint_module':'adapter.http_reader','classification':'dev_harness','description':'Reader success route (dev-only governed A7 proof surface)','env_gate':'APP_ENV=dev','internal':True,'method':'HEAD','path':'/reader','rails_profile':'dev-harness reader a7'},]
 return {'endpoints':eps,'generated_at_utc':TS,'success_endpoints':[{'method':'GET','path':'/reader'}]}
def validate_catalog(cat):
 if set(cat)!={'endpoints','generated_at_utc','success_endpoints'}: raise ValueError('catalog top-level keys invalid')
 if not isinstance(cat['generated_at_utc'],str) or not re.fullmatch(r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z',cat['generated_at_utc']): raise ValueError('invalid generated_at_utc')
 if not isinstance(cat['endpoints'],list) or not isinstance(cat['success_endpoints'],list): raise ValueError('catalog lists invalid')
 seen=set()
 for e in cat['endpoints']:
  for k in ['a7_eligible','blueprint_module','classification','description','env_gate','internal','method','path','rails_profile']:
   if k not in e: raise ValueError(f'missing {k}')
  if set(e)-{'a7_eligible','blueprint_module','classification','description','env_gate','internal','method','path','rails_profile','route_id'}: raise ValueError('unknown endpoint key')
  if not isinstance(e['method'],str) or e['method']!=e['method'].upper(): raise ValueError('method must be uppercase string')
  if not all(isinstance(e[k],str) for k in ['blueprint_module','classification','description','env_gate','path','rails_profile']): raise ValueError('endpoint string fields required')
  if not isinstance(e['internal'],bool): raise ValueError('internal boolean required')
  if not isinstance(e['a7_eligible'],bool): raise ValueError('a7_eligible boolean required')
  if e['classification'] not in CLASS: raise ValueError('invalid classification')
  key=(e['method'],e['path'])
  if key in seen: raise ValueError('duplicate method/path')
  seen.add(key)
  if 'writer' in e['path'] and e['path']=='/dev/writer/conjunction' and e.get('route_id')!='dev.writer.conjunction.v1': raise ValueError('writer route_id invalid')
 sampler=[e for e in cat['endpoints'] if e['path']=='/internal/dev/sampler']
 if len(sampler)!=1 or sampler[0]['method']!='POST' or sampler[0]['classification']!='dev_harness' or sampler[0]['internal'] is not True or sampler[0]['a7_eligible'] is not False or sampler[0]['env_gate']!='APP_ENV in {dev,test,local}': raise ValueError('internal dev sampler catalog invalid')
 if any(e['path']=='/internal/dev/sampler' and e['method']=='GET' for e in cat['endpoints']): raise ValueError('GET internal dev sampler must not be cataloged')
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
  head=c.head(target['path'],query_string=q(),headers={'Accept-Encoding':'identity'}); hh=headers(head); require(head.status_code==200 and head.data==b'','head'); require(hh.get('etag')==et and hh.get('content-length')==str(len(body)) and hh.get('content-type')==hb.get('content-type') and hh.get('cache-control')==hb.get('cache-control') and hh.get('vary')==hb.get('vary'),'head parity')
  r304=c.get(target['path'],query_string=q(),headers={'If-None-Match':et}); h304=headers(r304); require(r304.status_code==304 and r304.data==b'','304'); require(h304.get('etag')==et and h304.get('cache-control')==hb.get('cache-control') and h304.get('vary')==hb.get('vary') and 'content-type' not in h304 and 'content-length' not in h304,'304 headers')
  post=c.post(target['path'],query_string=q(),headers={'If-None-Match':et}); hp=headers(post); require(post.status_code==405 and hp.get('cache-control')=='no-store' and 'etag' not in hp and post.data.endswith(b'\n') and canon.sercanon(json.loads(post.data))==post.data,'writer')
  enc=[]
  for ae in ['identity','gzip','br']:
   r=c.get(target['path'],query_string=q(),headers={'Accept-Encoding':ae}); hr=headers(r); require(hr.get('etag')==et,'encoding etag')
   h=c.head(target['path'],query_string=q(),headers={'Accept-Encoding':ae}); hhr=headers(h); require(hhr.get('etag')==et and hhr.get('content-length')==str(len(body)),'encoding head')
   enc.append({'accept_encoding':ae,'content_encoding':hr.get('content-encoding','identity'),'etag':hr.get('etag'),'head_identity_length':int(hhr.get('content-length','-1'))})
 finally:
  if old is None: os.environ.pop('APP_ENV',None)
  else: os.environ['APP_ENV']=old
 old=os.environ.get('APP_ENV'); os.environ['APP_ENV']='prod'
 try:
  prod=c.get('/reader',query_string=q()); ph=headers(prod); require(prod.status_code!=200 and ph.get('cache-control')=='no-store' and 'etag' not in ph,'env gate')
 finally:
  if old is None: os.environ.pop('APP_ENV',None)
  else: os.environ['APP_ENV']=old
 comp={'route_path':'/reader','env_gate':{'app_env':'prod','cache_control':ph.get('cache-control'),'etag_absent':'etag' not in ph,'pass':prod.status_code!=200,'proof_path':'artifacts/proofs/endpoints_env_gate_proof.log','status':prod.status_code},'get_200':{'body_sha256':sha(body),'cache_control':hb.get('cache-control'),'content_length':len(body),'content_type':hb.get('content-type'),'etag':et,'pass':True,'status':200,'vary':hb.get('vary')},'head_200':{'body_empty':True,'cache_control':hh.get('cache-control'),'content_length':len(body),'content_type':hh.get('content-type'),'etag':hh.get('etag'),'pass':True,'status':200,'vary':hh.get('vary')},'after_304':{'body_empty':True,'cache_control':h304.get('cache-control'),'content_length_absent':'content-length' not in h304,'content_type_absent':'content-type' not in h304,'entity_headers_absent':'content-type' not in h304 and 'content-length' not in h304,'etag':h304.get('etag'),'pass':True,'status':304,'vary':h304.get('vary')},'vary_flags':{'authorization':True,'accept_encoding':True},'etag':et}
 comp['_encodings']=enc
 return cat, body, comp
def validate_composite(obj):
 schema=json.loads((ROOT/'schemas/proofs.reader_success.v1.json').read_text())
 try:
  jsonschema.Draft202012Validator(schema).validate(obj)
 except jsonschema.ValidationError as exc:
  raise ValueError('composite schema validation failed') from exc
 def check(node, sch, path='root'):
  if sch.get('type')=='object':
   if not isinstance(node,dict): raise ValueError(f'{path} object required')
   if sch.get('additionalProperties') is False and set(node)-set(sch.get('properties',{})): raise ValueError(f'{path} unknown keys')
   for k in sch.get('required',[]):
    if k not in node: raise ValueError(f'{path}.{k} missing')
   for k,ks in sch.get('properties',{}).items():
    if k in node: check(node[k],ks,f'{path}.{k}')
  if 'const' in sch and node!=sch['const']: raise ValueError(f'{path} const')
  if sch.get('type')=='string' and not isinstance(node,str): raise ValueError(f'{path} string')
  if sch.get('type')=='integer' and not isinstance(node,int): raise ValueError(f'{path} integer')
  if sch.get('type')=='boolean' and not isinstance(node,bool): raise ValueError(f'{path} boolean')
  if 'pattern' in sch and not re.fullmatch(sch['pattern'],node): raise ValueError(f'{path} pattern')
  if 'minimum' in sch and node < sch['minimum']: raise ValueError(f'{path} minimum')
 check(obj,schema)
 if obj['get_200']['etag']!=obj['etag'] or obj['head_200']['etag']!=obj['etag'] or obj['after_304']['etag']!=obj['etag']: raise ValueError('etag drift')
def build():
 cat, body, comp=capture(); enc=comp.pop('_encodings'); validate_composite(comp); catb=cjson(cat); snap=cjson({'endpoints':['GET /reader'],'envelope_keys':['categories','eligible','idempotence_hash','meta','reader_version','release_id'],'generated_at_utc':TS})
 enc_equal=all(e['etag']==comp['etag'] and e['head_identity_length']==comp['get_200']['content_length'] for e in enc)
 enc_text="ENCODING_INVARIANCE\n"+"\n".join(f"{e['accept_encoding']}_etag={e['etag']}\n{e['accept_encoding']}_head_identity_length={e['head_identity_length']}" for e in enc)+f"\netag_equal=true\nhead_identity_length_equal={str(enc_equal).lower()}\npass={str(enc_equal).lower()}\n"
 outs={DOC:catb,DOCSHA:(f"{sha(catb)}  docs/ENDPOINTS_CATALOG.json\n").encode(),AUD:catb,AUDSHA:(f"{sha(catb)}  artifacts/audit/ENDPOINTS_CATALOG.json\n").encode(),SNAP:snap,PROOFS[0]:b'APP_ENV=prod\n/reader_success_unreachable=true\ncache_control=no-store\netag_absent=true\n',PROOFS[1]:(f"status=200\nbody_sha256={comp['get_200']['body_sha256']}\netag={comp['etag']}\ncontent-type={comp['get_200']['content_type']}\ncache-control={comp['get_200']['cache_control']}\nvary={comp['get_200']['vary']}\ncontent-length={comp['get_200']['content_length']}\n").encode(),PROOFS[2]:(f"status=200\nbody_empty=true\ncontent_length={comp['head_200']['content_length']}\netag={comp['etag']}\ncontent-type={comp['head_200']['content_type']}\ncache-control={comp['head_200']['cache_control']}\nvary={comp['head_200']['vary']}\ncontent-length={comp['head_200']['content_length']}\n").encode(),PROOFS[3]:(f"status=304\nbody_empty=true\ncontent_type_absent=true\ncontent_length_absent=true\netag={comp['etag']}\ncache-control={comp['after_304']['cache_control']}\nvary={comp['after_304']['vary']}\n").encode(),PROOFS[4]:b'POST /reader\nstatus=405\ncache_control=no-store\netag_absent=true\nconditional_not_304=true\ncanonical_body=true\n',PROOFS[5]:enc_text.encode(),PROOFS[6]:cjson(comp)}
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
