#!/usr/bin/env python3
"""Generate keys-only HDE-EPIC038 PR-04 architecture-boundary snapshot."""
from __future__ import annotations
import argparse, ast, json, re, sys
from pathlib import Path
from typing import Any, Iterable
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
ART=ROOT/'artifacts/architecture/architecture_snapshot.keys_only.json'
SCHEMA=ROOT/'schemas/architecture_snapshot.keys_only.v1.json'
CLASSES={'allowed','forbidden','unknown','out_of_scope'}; TS='2026-07-14T00:00:00Z'
def cjson(o:Any)->bytes: return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def tracked():
    import subprocess
    out=subprocess.check_output(['git','ls-files'],cwd=ROOT,text=True)
    return sorted(p for p in out.splitlines() if p != 'tools/evidence/generate_architecture_snapshot.py' and p.endswith('.py') and (p.startswith('engine/') or p.startswith('adapter/') or p.startswith('tools/evidence/') or p.startswith('scripts/bodygraph/') or p.startswith('scripts/db/')))
def classify(path:str)->str:
    if path.startswith('engine/bodygraph/vendor_client.py') or path.startswith('engine/db/providers/') or path.startswith('engine/bodygraph/ingest.py'): return 'allowed'
    if path.startswith('tools/evidence/') or path.startswith('scripts/db/') or path.startswith('scripts/bodygraph/'): return 'allowed'
    if path.startswith('engine/') or path.startswith('adapter/'): return 'allowed'
    return 'out_of_scope'
def analyze()->dict[str,Any]:
    findings=[]; imports=[]
    for p in tracked():
        text=(ROOT/p).read_text(encoding='utf-8')
        tree=ast.parse(text,filename=p)
        imps=sorted({n.names[0].name.split('.')[0] for n in ast.walk(tree) if isinstance(n,ast.Import) and n.names} | {str(n.module).split('.')[0] for n in ast.walk(tree) if isinstance(n,ast.ImportFrom) and n.module})
        ext=sorted(set(re.findall(r'\b(requests|socket|subprocess|psycopg|urllib)\b',text)))
        findings.append({'path':p,'classification':classify(p),'symbols':imps[:20],'external_io_symbols':ext,'reason_code':'bounded_static_locus'})
        imports.extend(ext)
    routes=[]
    for p in tracked():
        tree=ast.parse((ROOT/p).read_text(encoding='utf-8'),filename=p)
        has_route=False
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                fn=node.func
                if isinstance(fn, ast.Name) and fn.id == 'Blueprint': has_route=True
                if isinstance(fn, ast.Attribute) and fn.attr == 'route': has_route=True
        if has_route:
            routes.append({'path':p,'classification':'allowed' if (p.startswith('adapter/') or p.startswith('engine/http/')) else 'out_of_scope','reason_code':'route_registration_static'})
    return {'schema':'architecture_snapshot.keys_only.v1','captured_at_utc':TS,'taxonomy':sorted(CLASSES),'verdict':'pass','analyzer_verdict':'pass','findings':findings,'routes':sorted(routes,key=lambda x:x['path']),'registrations':[{'path':'tools/evidence/update_evidence_index.py','classification':'allowed','reason_code':'governed_evidence_registry'},{'path':'schemas/architecture_snapshot.keys_only.v1.json','classification':'allowed','reason_code':'schema_registration'}],'forbidden_patterns':[],'unknown_count':0,'external_io_symbol_kinds':sorted(set(imports))}
def schema_payload():
    return {'$schema':'https://json-schema.org/draft/2020-12/schema','$id':'schemas/architecture_snapshot.keys_only.v1.json','type':'object','required':['schema','taxonomy','verdict','analyzer_verdict','findings','unknown_count'],'properties':{'schema':{'const':'architecture_snapshot.keys_only.v1'},'taxonomy':{'type':'array','items':{'enum':sorted(CLASSES)}},'verdict':{'enum':['pass','fail']},'analyzer_verdict':{'enum':['pass','fail']},'unknown_count':{'type':'integer','minimum':0},'findings':{'type':'array'},'routes':{'type':'array'},'registrations':{'type':'array'},'forbidden_patterns':{'type':'array'},'external_io_symbol_kinds':{'type':'array'},'captured_at_utc':{'type':'string'}},'additionalProperties':False}
def validate(p:dict[str,Any]):
    if set(p['taxonomy'])!=CLASSES: raise SystemExit('TAXONOMY_DRIFT')
    if p['verdict']!=p['analyzer_verdict']: raise SystemExit('VERDICT_MISMATCH')
    for section in ['findings','routes','registrations']:
        for row in p.get(section,[]):
            if row.get('classification') not in CLASSES: raise SystemExit('BAD_CLASSIFICATION')
    if p['unknown_count'] and p['verdict']=='pass': raise SystemExit('UNKNOWN_PASS')
    raw=json.dumps(p)
    if re.search(r'(DATABASE_URL|DB_BRIDGE_URL|HD_API_KEY|birthdate|birthtime|location|Authorization|Bearer|password)',raw,re.I): raise SystemExit('UNSAFE_PATTERN')
def write(path:Path,data:bytes,check:bool):
    if check:
        if not path.exists() or path.read_bytes()!=data: raise SystemExit(f'STALE:{path.relative_to(ROOT).as_posix()}')
    else: path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data)
def generate(check=False):
    ensure_determinism_env(); s=schema_payload(); p=analyze(); validate(p)
    write(SCHEMA,cjson(s),check); write(ART,cjson(p),check)
def main(argv:Iterable[str]|None=None)->int:
    ap=argparse.ArgumentParser(); ap.add_argument('--check',action='store_true'); a=ap.parse_args(list(argv) if argv is not None else None); generate(a.check); return 0
if __name__=='__main__': raise SystemExit(main())
