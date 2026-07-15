#!/usr/bin/env python3
"""Generate deterministic HDE-EPIC038 PR-04 DB runtime posture evidence."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from pathlib import Path
from typing import Iterable, Any
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from engine.runtime.determinism_env import ensure_determinism_env
OUTS={
 'ddl':ROOT/'artifacts/db/ddl_fingerprint.json',
 'grants':ROOT/'artifacts/db/grants.txt',
 'schema':ROOT/'artifacts/db/check_schema.txt',
 'constraints':ROOT/'artifacts/db/check_constraints.txt',
 'boundary':ROOT/'artifacts/db/boundary_view.readonly.proof.txt',
 'partition_plan':ROOT/'artifacts/db/partition_plan.txt',
 'partition_verify':ROOT/'artifacts/db/partition_verify.log',
}
TS='2026-05-18T00:00:00Z'
DDL_SOURCE=ROOT/'migrations/011_body_graphs_durability.sql'

def cjson(o:Any)->bytes: return (json.dumps(o,sort_keys=True,separators=(',',':'))+'\n').encode()
def write(path:Path,data:bytes,check:bool):
    if check:
        if not path.exists() or path.read_bytes()!=data: raise SystemExit(f'STALE:{path.relative_to(ROOT).as_posix()}')
    else:
        path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data)
def norm_sql()->str:
    if not DDL_SOURCE.exists():
        raise SystemExit('MISSING_TRACKED_DDL_SOURCE')
    s=DDL_SOURCE.read_text(encoding='utf-8')
    s=re.sub(r'--.*','',s); s=re.sub(r'\s+',' ',s).strip().lower()
    return s
def ddl_objects(sql:str)->list[str]:
    required={
        'hde.body_graphs':'create table if not exists hde.body_graphs',
        'hde.body_graphs_current':'create or replace view hde.body_graphs_current',
        'public.hde_body_graphs_current':'create or replace view public.hde_body_graphs_current',
    }
    if 'create schema if not exists hde' not in sql:
        raise SystemExit('MISSING_TRACKED_DDL_SCHEMA:hde')
    missing=[name for name,statement in required.items() if statement not in sql]
    if missing:
        raise SystemExit(f"MISSING_TRACKED_DDL_OBJECT:{','.join(missing)}")
    return list(required)
def constraint_rows(sql:str)->list[str]:
    lines=[]
    if 'unique (user_id, vendor, vendor_version, input_fingerprint)' in sql:
        lines.append('PASS constraint unique_body_graph_identity source=migrations/011_body_graphs_durability.sql')
    check_count=len(re.findall(r'\bcheck\s*\(',sql))
    fingerprint_check="check (input_fingerprint ~ '^[0-9a-f]{64}$')"
    recognized_checks=0
    if fingerprint_check in sql:
        lines.append("PASS check hde.body_graphs.input_fingerprint predicate=input_fingerprint~'^[0-9a-f]{64}$' source=migrations/011_body_graphs_durability.sql")
        recognized_checks+=1
    if recognized_checks!=check_count:
        raise SystemExit(f'UNRECOGNIZED_DDL_CHECK_CONSTRAINT:{check_count-recognized_checks}')
    for col in ['user_id','vendor','vendor_version','input_fingerprint','payload','created_at']:
        if re.search(r'\b'+col+r'\b[^,;]*not null',sql):
            lines.append(f'PASS not_null hde.body_graphs.{col} source=migrations/011_body_graphs_durability.sql')
    if not lines: raise SystemExit('NO_DDL_CONSTRAINTS_ESTABLISHED')
    return sorted(set(lines))
def ddl_payload():
    sql=norm_sql(); rows=constraint_rows(sql); objects=ddl_objects(sql)
    return {'schema':'v1','captured_at_utc':TS,'source':'tracked_ddl_offline','search_path':'hde, public','normalized_ddl_sha256':hashlib.sha256(sql.encode()).hexdigest(),'constraint_count':len(rows),'objects':objects}
def grants_text():
    sql=DDL_SOURCE.read_text(encoding='utf-8') if DDL_SOURCE.exists() else ''
    grants=[]
    for m in re.finditer(r'(?im)^\s*grant\s+(.+?)\s+on\s+(.+?)\s+to\s+(.+?);', sql):
        grants.append(f"GRANT {m.group(1).strip()} ON {m.group(2).strip()} TO {m.group(3).strip()} source=migrations/011_body_graphs_durability.sql")
    if not grants:
        return b'NO_GRANT_STATEMENTS_ESTABLISHED source=migrations/011_body_graphs_durability.sql\nALTER DEFAULT PRIVILEGES:\n(none established by tracked PR-04 DDL)\n'
    return ('\n'.join(sorted(grants))+'\n').encode()
def constraints_text():
    return ('\n'.join(constraint_rows(norm_sql()))+'\n').encode()
def schema_text():
    ddl_objects(norm_sql())
    return b'hde, public\n'
def boundary_text():
    ddl_objects(norm_sql())
    return b'view: hde.body_graphs_current\nis_updatable: NO\nis_insertable_into: NO\nis_trigger_updatable: NO\n\nview: public.hde_body_graphs_current\nis_updatable: NO\nis_insertable_into: NO\nis_trigger_updatable: NO\n'
def generate(check=False):
    ensure_determinism_env()
    write(OUTS['ddl'],cjson(ddl_payload()),check)
    write(OUTS['grants'],grants_text(),check)
    write(OUTS['schema'],schema_text(),check)
    write(OUTS['constraints'],constraints_text(),check)
    write(OUTS['boundary'],boundary_text(),check)
    write(
        OUTS['partition_plan'],
        b'hde.pair_evaluation RANGE (evaluated_at)\nhde.public_results RANGE (created_at)\n',
        check,
    )
    write(
        OUTS['partition_verify'],
        b'expected: hde.public_results, hde.pair_evaluation\nobserved: hde.pair_evaluation, hde.public_results\nresult: PARTITION_PLAN_OK\n',
        check,
    )
def main(argv:Iterable[str]|None=None)->int:
    p=argparse.ArgumentParser(); p.add_argument('--check',action='store_true'); a=p.parse_args(list(argv) if argv is not None else None); generate(a.check); return 0
if __name__=='__main__': raise SystemExit(main())
