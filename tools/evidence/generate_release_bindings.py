#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.identity import identity_admin
from engine.serializer import canon
def require_closed_rails():
    expected={"SAFE_MODE":"1","ALLOW_NETWORK":"0","LC_ALL":"C","LANG":"C","TZ":"UTC"}
    bad=[k for k,v in expected.items() if os.environ.get(k)!=v]
    if bad: raise SystemExit("DETERMINISM_ENV:"+",".join(bad))

OUT=ROOT/'artifacts/bodygraph/release_bindings.json'
INPUTS=('artifacts/bodygraph/source_selection.snapshot.json','artifacts/bodygraph/refresh_policy.snapshot.json')
def _expected():
    require_closed_rails(); arts=[]
    for rel in INPUTS:
        p=ROOT/rel
        if not p.exists(): raise SystemExit('MISSING:'+rel)
        arts.append({'path':rel,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'size_bytes':p.stat().st_size})
    return canon.sercanon({'release_id':identity_admin()['release_id'],'bindings':arts,'schema_version':1}, sort_keys=True)
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(argv); b=_expected()
    if a.check:
        if not OUT.exists() or OUT.read_bytes()!=b: raise SystemExit('DRIFT:'+OUT.as_posix())
        return 0
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_bytes(b); return 0
if __name__=='__main__': raise SystemExit(main())
