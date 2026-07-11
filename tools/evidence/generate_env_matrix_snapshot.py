#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, sys
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
PRES=('DATABASE_URL','DB_BRIDGE_URL','DB_ALLOW_BRIDGE_IN_PROD')
def _expected():
    require_closed_rails()
    payload={'schema_version':3,'rails':PINS,'presence':{k: bool(os.environ.get(k)) for k in PRES}}
    return canon.sercanon(payload, sort_keys=True)
def _validate_snapshot(body):
    try:
        payload=json.loads(body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        raise SystemExit('DRIFT:'+OUT.as_posix())
    presence=payload.get('presence') if isinstance(payload,dict) else None
    valid=(
        isinstance(payload,dict)
        and set(payload)=={'schema_version','rails','presence'}
        and payload.get('schema_version')==3
        and payload.get('rails')==PINS
        and isinstance(presence,dict)
        and set(presence)==set(PRES)
        and all(type(value) is bool for value in presence.values())
    )
    if not valid or canon.sercanon(payload,sort_keys=True)!=body:
        raise SystemExit('DRIFT:'+OUT.as_posix())
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(argv)
    if a.check:
        require_closed_rails()
        if not OUT.exists(): raise SystemExit('DRIFT:'+OUT.as_posix())
        _validate_snapshot(OUT.read_bytes())
        return 0
    b=_expected()
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_bytes(b); return 0
if __name__=='__main__': raise SystemExit(main())
