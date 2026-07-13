#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
from engine.presenter import emitter
from engine.cli.main import _normalize_party,_party_from_normalized
from engine.runtime.public import emit_reader_public_envelope
from engine.runtime.identity import identity_meta
from engine.serializer import canon
TS=json.loads((ROOT/'catalog/manifest.json').read_text()).get('built_at_utc','2026-01-01T00:00:00Z')
AB=ROOT/'audit/gates/parity/reader_cli/ab.json'; BA=ROOT/'audit/gates/parity/reader_cli/ba.json'; SUM=ROOT/'audit/gates/parity/reader_cli/summary.json'; ABB=ROOT/'audit/gates/determinism/abba.bytes'; TWO=ROOT/'audit/gates/determinism/tworun_identity.sha256'; ID=ROOT/'artifacts/cards/a3/IDENTITY_OK.txt'
OUTS=[AB,BA,SUM,ABB,TWO,ID]
LEFT={'person_uid':'hde-pr02-a','birthdate':'1990-01-10','birthtime':'14:05','location':'Chicago, US','tz':'America/Chicago'}
RIGHT={'person_uid':'hde-pr02-b','birthdate':'1992-03-04','birthtime':'08:15','location':'Berlin, DE','tz':'Europe/Berlin'}
def sha(b): return hashlib.sha256(b).hexdigest()
def cjson(o): return json.dumps(o,separators=(',',':'),sort_keys=True).encode()+b'\n'
def env():
 e=os.environ.copy(); e.update({'SAFE_MODE':'1','ALLOW_NETWORK':'0','LC_ALL':'C','LANG':'C','TZ':'UTC','APP_ENV':'test','PIP_NO_INDEX':'1'}); ensure_determinism_env(environ=e); return e
def runtime_bytes(l=LEFT,r=RIGHT):
 lp=_normalize_party(dict(l),'left'); rp=_normalize_party(dict(r),'right')
 _,ac=_party_from_normalized(lp); _,bc=_party_from_normalized(rp)
 m=identity_meta(); return emit_reader_public_envelope(ac,bc,engine_tag=m['engine_tag'],invocation_tag=m['invocation_tag'],release_id=m['release_id'])[0]
def cli_bytes(l=LEFT,r=RIGHT):
 with tempfile.TemporaryDirectory() as td:
  td=Path(td); af=td/'a.json'; bf=td/'b.json'; dump=td/'reader.json'; af.write_bytes(cjson(l)); bf.write_bytes(cjson(r))
  p=subprocess.run([sys.executable,'-m','engine.cli','showcompat','--a-file',str(af),'--b-file',str(bf),'--dump-reader',str(dump)],cwd=ROOT,env=env(),capture_output=True)
  if p.returncode or p.stderr: raise RuntimeError(f'cli failed rc={p.returncode} stderr={p.stderr!r}')
  return dump.read_bytes()
def canonical_ok(b):
 if b.startswith(b'\xef\xbb\xbf') or b'\r\n' in b or not b.endswith(b'\n') or b.endswith(b'\n\n'): return False
 return canon.sercanon(json.loads(b))==b
def canonical_gate_result(runner=None):
 runner = runner or subprocess.run
 cmd=[sys.executable,'tools/evidence/run_canonical_json_gate.py','--check-only']
 p=runner(cmd,cwd=ROOT,env=env(),capture_output=True,text=True)
 return {'command':' '.join(cmd),'returncode':p.returncode,'stdout_sha256':sha((p.stdout or '').encode()),'stderr_sha256':sha((p.stderr or '').encode()),'passed':p.returncode==0}
def build(*, canon_gate=None, ba_override=None):
 rb=runtime_bytes(); cb=cli_bytes(); bab=ba_override if ba_override is not None else runtime_bytes(RIGHT,LEFT); run2=runtime_bytes()
 envj=json.loads(rb); pre=dict(envj); stored=pre.pop('idempotence_hash',None); recomputed=sha(emitter.emit_public(pre))
 if canon_gate is None:
  canon_gate=canonical_gate_result()
 if not isinstance(canon_gate,dict) or 'command' not in canon_gate or canon_gate.get('passed') is not True:
  canon_gate=dict(canon_gate or {})
  canon_gate.setdefault('passed',False)
 preds={'reader_cli_byte_identity': rb==cb, 'abba_byte_identity': rb==bab, 'two_run_byte_identity': rb==run2, 'preimage_hash_match': stored==recomputed, 'canonical_gate_check': canon_gate.get('passed') is True and 'command' in canon_gate}
 preds['canonical_reserialization'] = all(canonical_ok(x) for x in [rb,bab,cb,run2])
 top=all(preds.values())
 summary={'artifact_kind':'hde_epic038_pr02_determinism_proof','generated_at_utc':TS,'fixed_corpus':'hde-epic038-pr02-synthetic-ab','sources':{'runtime':'engine.runtime.public.emit_reader_public_envelope','cli':'python -m engine.cli showcompat --dump-reader'},'canonical_gate':canon_gate,'hashes':{'ab_sha256':sha(rb),'ba_sha256':sha(bab),'reader_sha256':sha(rb),'cli_sha256':sha(cb),'two_run_1_sha256':sha(rb),'two_run_2_sha256':sha(run2)},'idempotence_hash':{'stored':stored,'recomputed':recomputed},'predicates':preds,'top_level_pass':top,'acceptance_token_satisfied':False}
 outs={AB:rb,BA:bab,SUM:cjson(summary),ABB:(f"ab_sha256={sha(rb)}\nba_sha256={sha(bab)}\nbyte_identity={str(rb==bab).lower()}\n").encode(),TWO:(f"run1_sha256={sha(rb)}\nrun2_sha256={sha(run2)}\nbyte_identity={str(rb==run2).lower()}\n").encode(),ID:("IDENTITY_OK\nHDE-EPIC038 PR-02 deterministic predicate evidence only; no acceptance token satisfaction claimed.\n").encode()}
 return top, outs
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ns=ap.parse_args(); ensure_determinism_env()
 top, outs=build()
 if not top: raise SystemExit('DETERMINISM_PREDICATES_FAILED')
 if ns.check:
  bad=[str(p.relative_to(ROOT)) for p,b in outs.items() if not p.exists() or p.read_bytes()!=b]
  if bad: raise SystemExit('DRIFT:'+','.join(bad))
  print('determinism gate proofs check ok'); return
 for p,b in outs.items(): p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
 print('determinism gate proofs written')
if __name__=='__main__': main()
