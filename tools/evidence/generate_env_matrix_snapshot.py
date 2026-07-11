#!/usr/bin/env python3
from __future__ import annotations
import argparse, os, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.serializer import canon
def require_closed_rails():
    expected={"SAFE_MODE":"1","ALLOW_NETWORK":"0","LC_ALL":"C","LANG":"C","TZ":"UTC"}
    bad=[k for k,v in expected.items() if os.environ.get(k)!=v]
    if bad: raise SystemExit("DETERMINISM_ENV:"+",".join(bad))

OUT=ROOT/'artifacts/runtime/env_matrix.snapshot.json'
PINS={'ALLOW_NETWORK':'0','LANG':'C','LC_ALL':'C','SAFE_MODE':'1','TZ':'UTC'}
def _expected():
    require_closed_rails()
    payload={'schema_version':3,'rails':PINS}
    return canon.sercanon(payload, sort_keys=True)
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(argv)
    b=_expected()
    if a.check:
        if not OUT.exists() or OUT.read_bytes()!=b:
            raise SystemExit('DRIFT:'+OUT.as_posix())
        return 0
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_bytes(b); return 0
if __name__=='__main__': raise SystemExit(main())
