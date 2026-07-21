#!/usr/bin/env python3
"""Fixture-only independent OPS-03 validator."""
from __future__ import annotations
import argparse,hashlib,json,re,sys
from pathlib import Path
SCHEMA_RECEIPT='hde_epic038.ops03.validation_receipt.v1'; SCHEMA_FAILURE='hde_epic038.ops03.failure_receipt.v1'
PRIMARY=('commands.txt','db_posture_summary.json','env_presence.json','exit_code.txt','nonclaims.json','result_summary.json','stderr.log','stdout.log')
PREDS=('authorization_valid','source_identity_valid','schemas_valid','canonical_bytes_valid','inventory_valid','counts_valid','secret_scan_valid','nonclaims_valid')
def canon(o): return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p): return json.loads(Path(p).read_text())
def validate_packet(auth,candidate):
 a=load(auth); c=Path(candidate); run=a['run_id']
 ok=all((c/n).exists() for n in PRIMARY) and (c/'stderr.log').read_text()=='' and (c/'exit_code.txt').read_text()=='0\n'
 if sorted(x.name for x in c.iterdir() if x.name!='checksums.sha256' and x.name!='validation_receipt.json') != sorted(PRIMARY): ok=False
 preds={k:ok for k in PREDS}
 return {'schema':SCHEMA_RECEIPT,'run_id':run,'authorization_sha256':sha(auth),'validated_files':list(PRIMARY),'predicates':preds,'result':'PASS' if all(preds.values()) else 'FAIL'}
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--emit-receipt',action='store_true'); ap.add_argument('--validate',action='store_true'); ap.add_argument('--authorization',required=True); ap.add_argument('--candidate',required=True)
 ns=ap.parse_args(argv); rec=validate_packet(ns.authorization,ns.candidate)
 if ns.emit_receipt: (Path(ns.candidate)/'validation_receipt.json').write_bytes(canon(rec))
 return 0 if rec['result']=='PASS' else 1
if __name__=='__main__': raise SystemExit(main())
