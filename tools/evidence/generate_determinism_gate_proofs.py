#!/usr/bin/env python3
"""Reader-to-CLI, AB-to-BA, two-run and preimage determinism proofs (release-sanity stage 04).

The fixed corpus is the two complete mapped fixture charts under
``fixtures/charts/``; both surfaces resolve them through the CLI file path
(``engine.cli.main._normalize_party`` + ``_resolve_party``) and evaluate through
``engine.compat.compute.evaluate_pair`` before the single Reader emitter.

PF10 — HDE Build Notes §2.15 (HDE-EPIC040-PR04 F01 overlay): ``build()`` probes
the admission owner first.  While the active release is not admitted it raises
``ReleaseNotAdmitted`` before any live Reader envelope or CLI subprocess; the
CLI prints ``DETERMINISM_GATE_CHECK:RELEASE_NOT_ADMITTED`` and exits with the
distinct code, and write mode writes none of its six outputs.  Nothing here
presents a frozen capture as a live result.
"""
from __future__ import annotations
import argparse, hashlib, json, os, subprocess, sys, tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
from engine.presenter import emitter
from engine.cli import main as cli_main
from engine.compat.compute import evaluate_pair, evaluation_party, harmony_band, is_ineligible_carrier
from engine.runtime.public import emit_reader_public_envelope
from engine.runtime.identity import identity_meta
from engine.serializer import canon
from tools.evidence.run_sanity_pipeline import RELEASE_NOT_ADMITTED_EXIT_CODE, ReleaseNotAdmitted, probe_release_admission
TS=json.loads((ROOT/'catalog/manifest.json').read_text()).get('built_at_utc','2026-01-01T00:00:00Z')
AB=ROOT/'audit/gates/parity/reader_cli/ab.json'; BA=ROOT/'audit/gates/parity/reader_cli/ba.json'; SUM=ROOT/'audit/gates/parity/reader_cli/summary.json'; ABB=ROOT/'audit/gates/determinism/abba.bytes'; TWO=ROOT/'audit/gates/determinism/tworun_identity.sha256'; ID=ROOT/'artifacts/cards/a3/IDENTITY_OK.txt'
OUTS=[AB,BA,SUM,ABB,TWO,ID]
NOT_ADMITTED_LINE='DETERMINISM_GATE_CHECK:RELEASE_NOT_ADMITTED'
LEFT_REL='fixtures/charts/alice.json'; RIGHT_REL='fixtures/charts/bob.json'
LEFT=json.loads((ROOT/LEFT_REL).read_text(encoding='utf-8'))
RIGHT=json.loads((ROOT/RIGHT_REL).read_text(encoding='utf-8'))
def sha(b): return hashlib.sha256(b).hexdigest()
def cjson(o): return json.dumps(o,separators=(',',':'),sort_keys=True).encode()+b'\n'
def env():
 e=os.environ.copy(); e.update({'SAFE_MODE':'1','ALLOW_NETWORK':'0','LC_ALL':'C','LANG':'C','TZ':'UTC','APP_ENV':'test','PIP_NO_INDEX':'1'}); ensure_determinism_env(environ=e); return e
def _resolved(party, label):
 return cli_main._resolve_party(cli_main._normalize_party(dict(party), label), source_policy='local')
def reader_envelope_bytes(left_resolved, right_resolved):
 result=evaluate_pair(evaluation_party(left_resolved), evaluation_party(right_resolved)); eligible=not is_ineligible_carrier(result); m=identity_meta()
 return emit_reader_public_envelope(None,None,engine_tag=m['engine_tag'],invocation_tag=m['invocation_tag'],release_id=str(result['release_id']) if eligible else m['release_id'],eligible=eligible,harmony_band=harmony_band(result) if eligible else None)[0]
def runtime_bytes(l=LEFT,r=RIGHT):
 return reader_envelope_bytes(_resolved(l,'left'), _resolved(r,'right'))
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
 stable_command='python tools/evidence/run_canonical_json_gate.py --check-only'
 cmd=[sys.executable,'tools/evidence/run_canonical_json_gate.py','--check-only']
 p=runner(cmd,cwd=ROOT,env=env(),capture_output=True,text=True)
 return {'command':stable_command,'returncode':p.returncode,'stdout_sha256':sha((p.stdout or '').encode()),'stderr_sha256':sha((p.stderr or '').encode()),'passed':p.returncode==0}
def build(*, canon_gate=None, ba_override=None):
 probe_release_admission()  # raises ReleaseNotAdmitted before any live Reader envelope or CLI subprocess
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
 summary={'artifact_kind':'hde_epic038_pr02_determinism_proof','generated_at_utc':TS,'fixed_corpus':'hde-epic040-pr04-complete-fixture-charts','fixtures':{'left':LEFT_REL,'right':RIGHT_REL},'sources':{'runtime':'engine.compat.compute.evaluate_pair -> engine.runtime.public.emit_reader_public_envelope','cli':'python -m engine.cli showcompat --dump-reader'},'canonical_gate':canon_gate,'hashes':{'ab_sha256':sha(rb),'ba_sha256':sha(bab),'reader_sha256':sha(rb),'cli_sha256':sha(cb),'two_run_1_sha256':sha(rb),'two_run_2_sha256':sha(run2)},'idempotence_hash':{'stored':stored,'recomputed':recomputed},'predicates':preds,'top_level_pass':top,'acceptance_token_satisfied':False}
 outs={AB:rb,BA:bab,SUM:cjson(summary),ABB:(f"ab_sha256={sha(rb)}\nba_sha256={sha(bab)}\nbyte_identity={str(rb==bab).lower()}\n").encode(),TWO:(f"run1_sha256={sha(rb)}\nrun2_sha256={sha(run2)}\nbyte_identity={str(rb==run2).lower()}\n").encode(),ID:("IDENTITY_OK\nHDE-EPIC038 PR-02 deterministic predicate evidence only; no acceptance token satisfaction claimed.\n").encode()}
 return top, outs
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); ns=ap.parse_args(argv); ensure_determinism_env()
 try:
  top, outs=build()
 except ReleaseNotAdmitted:
  # PF10 §2.15: no live capture happened and nothing is written; the distinct code is never 0.
  print(NOT_ADMITTED_LINE); raise SystemExit(RELEASE_NOT_ADMITTED_EXIT_CODE)
 if not top: raise SystemExit('DETERMINISM_PREDICATES_FAILED')
 if ns.check:
  bad=[str(p.relative_to(ROOT)) for p,b in outs.items() if not p.exists() or p.read_bytes()!=b]
  if bad: raise SystemExit('DRIFT:'+','.join(bad))
  print('determinism gate proofs check ok'); return
 for p,b in outs.items(): p.parent.mkdir(parents=True,exist_ok=True); p.write_bytes(b)
 print('determinism gate proofs written')
if __name__=='__main__': main()
