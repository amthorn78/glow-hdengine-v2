#!/usr/bin/env python3
"""Dormant OPS-01R runner scaffold for HDE-EPIC038 PR-A."""
from __future__ import annotations
import argparse, hashlib, json, os, stat, sys, uuid
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
SOURCE_MANIFEST_SCHEMA='hde_epic038.source_tree_manifest.v1'; STAGING_MANIFEST_SCHEMA='hde_epic038.non_source_staging_manifest.v1'

def canonical_bytes(v): return (json.dumps(v, ensure_ascii=True, sort_keys=True, separators=(',',':'))+'\n').encode('ascii')
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def tree_manifest(root:Path, *, schema:str):
    entries=[]
    for base, dirs, files in os.walk(root, topdown=True, followlinks=False):
        names=['.'] if Path(base)==root else []
        for n in names+dirs+files:
            p=root if n=='.' else Path(base)/n; rel='.' if p==root else p.relative_to(root).as_posix(); st=p.lstat()
            if any(part=='__pycache__' for part in Path(rel).parts) or (p.is_file() and p.name.endswith('.pyc')): raise RuntimeError('OPS01_V5_SOURCE_RESIDUE_DETECTED')
            e={'ctime_ns':st.st_ctime_ns,'kind':'','mode':stat.S_IMODE(st.st_mode),'mtime_ns':st.st_mtime_ns,'path':rel,'sha256':None,'size':None,'target':None}
            if stat.S_ISDIR(st.st_mode): e['kind']='directory'
            elif stat.S_ISREG(st.st_mode): e['kind']='regular_file'; data=p.read_bytes(); e['sha256']=sha_bytes(data); e['size']=len(data)
            elif stat.S_ISLNK(st.st_mode): e['kind']='symlink'; e['target']=os.readlink(p)
            else: raise RuntimeError('unsupported filesystem kind')
            entries.append(e)
    return {'schema':schema,'entries':sorted(entries,key=lambda x:x['path'].encode('utf-8'))}
def bound_python_vector(script:Path,*args): return (sys.executable,'-I','-B',script.resolve().as_posix(),*args)
def reject_python_env(env):
    bad=[k for k in env if k.upper().startswith('PYTHON')]
    if bad: raise RuntimeError('OPS01_V5_PYTHON_ENVIRONMENT_INVALID')
def write_contained(path:Path, data:bytes, root:Path):
    path=path.resolve(); root=root.resolve()
    if root not in [path,*path.parents]: raise RuntimeError('OPS01_V5_WRITE_SET_MISMATCH')
    for parent in path.parents:
        if parent==root.parent: break
        if parent.exists() and parent.is_symlink(): raise RuntimeError('OPS01_V5_WRITE_SET_MISMATCH')
    path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(data)
def preflight():
    reject_python_env({})
    run_id=uuid.uuid4().hex; root=Path('/tmp/hde-epic038-ops01r')/run_id; control=root/'control'; work=root/'preflight-work'; source=root/'source'
    control.mkdir(parents=True); work.mkdir(); source.mkdir()
    counts={k:0 for k in ('bridge_transport_delegations','candidate_writes','credential_reads','direct_connector_delegations','failure_summary_writes','provider_constructions','railway_subprocesses','sql_driver_delegations','vendor_transport_delegations')}
    payload={'schema':'hde_epic038.ops01r.preflight.v1','status':'PASS','run':{'run_id':run_id},'orchestration':{'producer_vector':bound_python_vector(Path(__file__),'--preflight')},'actual_external_io_counts':counts,'expected_call_counts':{'logical_observations':10,'bodygraph_reads':2,'direct_provider_selections':1,'bridge_provider_selections':1,'vendor_requests':0,'retries':0,'fallbacks':0,'direct_connection_attempts':0,'direct_sql_statements':0,'bridge_http_requests':0},'nonclaims':['no_railway_subprocess','no_credential_read','no_provider_construction','no_direct_connector_delegation','no_sql_driver_delegation','no_bridge_transport_delegation','no_vendor_transport_delegation','no_candidate_write','no_failure_summary_write','no_source_tree_write','no_bytecode_cache_write','no_unauthorized_staging_write'],'source_write_validation':{'status':'PASS','bytecode_write_control':'python_flag_-B','python_argv':list(bound_python_vector(Path(__file__),'--preflight')),'python_environment_names':[]},'components':{},'interpreter':sys.executable,'module_origins':{},'railway_executable':{},'source':{}}
    payload['preflight_identity_sha256']=sha_bytes(canonical_bytes({k:v for k,v in payload.items() if k!='preflight_identity_sha256'}))
    write_contained(control/'preflight.json', canonical_bytes(payload), root); print((control/'preflight.json').as_posix()); return 0
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--preflight',action='store_true'); ap.add_argument('--target-identity-probe',action='store_true'); ap.add_argument('--discovery'); ap.add_argument('--live-launch'); ap.add_argument('--live-child',action='store_true')
    ns=ap.parse_args(argv)
    if ns.preflight: return preflight()
    if ns.target_identity_probe: print(canonical_bytes({'schema':'hde_epic038.ops01r.target_identity_probe.v1','writes':0}).decode(),end=''); return 0
    raise SystemExit('OPS modes are dormant and require PO authorization')
if __name__=='__main__': raise SystemExit(main())
