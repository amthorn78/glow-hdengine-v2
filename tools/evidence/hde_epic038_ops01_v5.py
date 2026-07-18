#!/usr/bin/env python3
"""Dormant read-only HDE-EPIC038 OPS-01 v5 validators."""
from __future__ import annotations

import argparse, dataclasses, hashlib, json, os, stat, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Type, TypeVar

from engine.db.ddl_identity_projection import DDL_IDENTITY_PROJECTION_FIELDS, DDL_IDENTITY_PROJECTION_SCHEMA, DDL_IDENTITY_UNEXAMINED_FIELDS
from tools.evidence.retained_evidence_safety import validate_retained_text_safety

@dataclass(frozen=True)
class Ops01V5ValidationResult:
    valid: bool
    errors: tuple[str, ...]

@dataclass(frozen=True)
class Ops01V5ExpectedIdentity:
    authorization_sha256: str; candidate_ledger_sha256: str; commands_sha256: str; discovery_identity_sha256: str; expected_call_counts_sha256: str; literal_staging_root: str; live_post_staging_manifest_sha256: str; live_pre_staging_manifest_sha256: str; preflight_identity_sha256: str; projector_sha256: str; runner_sha256: str; source_commit: str; source_manifest_sha256: str; validator_sha256: str
@dataclass(frozen=True)
class Ops01RPreflightExpectedIdentity:
    source_commit: str; source_manifest_sha256: str; pre_staging_manifest_sha256: str; literal_staging_root: str; runner_sha256: str; validator_sha256: str; projector_sha256: str; interpreter_sha256: str; railway_executable_sha256: str; preflight_identity_sha256: str
@dataclass(frozen=True)
class Ops01RDiscoveryAuthorizationExpectedIdentity:
    discovery_authorization_sha256: str; discovery_entry_point_sha256: str; literal_staging_root: str; pre_staging_manifest_sha256: str; preflight_identity_sha256: str; railway_executable_sha256: str; source_commit: str; source_manifest_sha256: str
@dataclass(frozen=True)
class Ops01RLiveAuthorizationExpectedIdentity:
    authorization_sha256: str; discovery_identity_sha256: str; interpreter_sha256: str; live_pre_staging_manifest_sha256: str; literal_staging_root: str; preflight_identity_sha256: str; projector_sha256: str; railway_executable_sha256: str; runner_sha256: str; source_commit: str; source_manifest_sha256: str; validator_sha256: str

V5_PRIMARY_FILES=("commands.txt","stdout.log","stderr.log","exit_code.txt","env_presence.json","db_posture_summary.json","provider_parity.proof.json","bridge_consistency.result.json","nonclaims.json","result_summary.json","checksums.sha256")
CALL_COUNT_FIELDS=("bodygraph_reads","bridge_http_requests","bridge_provider_selections","direct_connection_attempts","direct_provider_selections","direct_sql_statements","fallbacks","logical_observations","retries","vendor_requests")
FIXED_COUNTS={"logical_observations":10,"bodygraph_reads":2,"direct_provider_selections":1,"bridge_provider_selections":1,"vendor_requests":0,"retries":0,"fallbacks":0}
T=TypeVar('T')

def _result(errors:set[str])->Ops01V5ValidationResult: return Ops01V5ValidationResult(not errors, tuple(sorted(errors)))
def _canon(v:object)->bytes: return (json.dumps(v, ensure_ascii=True, sort_keys=True, separators=(",",":"))+"\n").encode('ascii')
def _read_json(path:Path):
    return json.loads(path.read_text('utf-8'), object_pairs_hook=lambda pairs: (_ for _ in ()).throw(ValueError('duplicate key')) if len({k for k,_ in pairs})!=len(pairs) else dict(pairs))
def _sha(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def _check_expected_values(obj, exp):
    errs=set()
    for f in dataclasses.fields(exp):
        if obj.get(f.name)!=getattr(exp,f.name): errs.add(f"OPS01_V5_{f.name.upper()}_MISMATCH")
    return errs

def _parse_expected_stdin(cls:Type[T])->T:
    try:
        st=os.fstat(0)
        if os.isatty(0) or not stat.S_ISFIFO(st.st_mode): raise ValueError
        data=os.read(0,16385)
        if len(data)>16384 or os.read(0,1)!=b"": raise ValueError
        if data.startswith(b"\xef\xbb\xbf") or b"\r" in data or data.count(b"\n")!=1 or not data.endswith(b"\n"): raise ValueError
        data.decode('ascii')
        obj=json.loads(data.decode('ascii'), object_pairs_hook=lambda pairs: (_ for _ in ()).throw(ValueError()) if len({k for k,_ in pairs})!=len(pairs) else dict(pairs))
        keys=tuple(f.name for f in dataclasses.fields(cls))
        if set(obj)!=set(keys) or any(not isinstance(obj[k],str) for k in keys): raise ValueError
        if _canon(obj)!=data: raise ValueError
        return cls(**obj)
    except Exception as exc:
        raise SystemExit("OPS01_V5_EXPECTED_INPUT_INVALID") from exc

def validate_ops01_v5_package(root: Path, *, expected: Ops01V5ExpectedIdentity)->Ops01V5ValidationResult:
    errors=set(); files=tuple(p.name for p in root.iterdir() if p.is_file()) if root.exists() else ()
    if set(files)!=set(V5_PRIMARY_FILES): errors.add('OPS01_V5_WRITE_SET_MISMATCH')
    for name in V5_PRIMARY_FILES:
        if name!='checksums.sha256' and (root/name).exists():
            for e in validate_retained_text_safety(root/name,(root/name).read_bytes()): errors.add(e)
    try:
        ledger=(root/'checksums.sha256').read_text('ascii').splitlines()
        expected_lines=[f"{_sha((root/n).read_bytes())}  {n}" for n in sorted(V5_PRIMARY_FILES) if n!='checksums.sha256']
        if ledger!=expected_lines: errors.add('OPS01_V5_WRITE_SET_MISMATCH')
    except Exception: errors.add('OPS01_V5_WRITE_SET_MISMATCH')
    try:
        proof=_read_json(root/'provider_parity.proof.json')
        if proof.get('schema')!='hde_epic038.ops01.provider_parity.v5': errors.add('OPS01_V5_SCHEMA_INVALID')
        if proof.get('status')!='PASS' or proof.get('selected')!='psycopg' or proof.get('environment')!='dev' or proof.get('rails_open') is not False or proof.get('full_ddl_semantic_parity_claimed') is not False: errors.add('OPS01_V5_PROVIDER_PROOF_INVALID')
        cc=proof.get('comparison_contract') or proof.get('ddl_identity_projection_contract') or {}
        if cc and (cc.get('schema')!=DDL_IDENTITY_PROJECTION_SCHEMA or tuple(cc.get('included_fields',()))!=DDL_IDENTITY_PROJECTION_FIELDS or tuple(cc.get('unexamined_fields',()))!=DDL_IDENTITY_UNEXAMINED_FIELDS): errors.add('OPS01_V5_PROVIDER_PROOF_INVALID')
    except Exception: errors.add('OPS01_V5_PROVIDER_PROOF_INVALID')
    try:
        summary=_read_json(root/'result_summary.json')
        if summary.get('schema')!='hde_epic038.ops01.result_summary.v4' or summary.get('full_ddl_semantic_parity_claimed') is not False: errors.add('OPS01_V5_RESULT_SUMMARY_INVALID')
        for field, val in (summary.get('actual_call_counts') or {}).items():
            if field in CALL_COUNT_FIELDS and (type(val) is not int or val<0): errors.add('OPS01_V5_RESULT_SUMMARY_INVALID')
    except Exception: errors.add('OPS01_V5_RESULT_SUMMARY_INVALID')
    return _result(errors)

def validate_ops01r_preflight(path:Path,*,expected:Ops01RPreflightExpectedIdentity):
    e=set();
    try: obj=_read_json(path); e|=_check_expected_values(obj.get('expected_identity',obj),expected); e.add('PREFLIGHT_STATUS_INVALID') if obj.get('status')!='PASS' else None
    except Exception: e.add('PREFLIGHT_JSON_INVALID')
    return _result(e)
def validate_ops01r_discovery_authorization(path:Path,*,expected:Ops01RDiscoveryAuthorizationExpectedIdentity):
    try: return _result(_check_expected_values(_read_json(path).get('expected_identity',_read_json(path)), expected))
    except Exception: return _result({'DISCOVERY_AUTHORIZATION_JSON_INVALID'})
def validate_ops01r_discovery_dispatch(authorization_path:Path,*,stage:str,prior_results:object,rendered_argv:tuple[str,...]):
    bad={'add','connect','delete','deploy','disconnect','down','link','logs','redeploy','remove','restart','set','shell','ssh','unlink','unset','up','variables'}
    return _result({'DISCOVERY_DISPATCH_PROHIBITED_TOKEN'} if any(x.lstrip('-').casefold() in bad for x in rendered_argv) else set())
def validate_ops01r_discovery_result(path:Path,*,authorization_path:Path,expected:Ops01RDiscoveryAuthorizationExpectedIdentity):
    try: obj=_read_json(path); return _result(set() if obj.get('schema')=='hde_epic038.ops01r.discovery.v1' else {'DISCOVERY_RESULT_SCHEMA_INVALID'})
    except Exception: return _result({'DISCOVERY_RESULT_JSON_INVALID'})
def validate_ops01r_live_authorization(path:Path,*,expected:Ops01RLiveAuthorizationExpectedIdentity):
    try: return _result(_check_expected_values(_read_json(path).get('expected_identity',_read_json(path)), expected))
    except Exception: return _result({'OPS01_AUTH_EXPECTED_INPUT_INVALID'})
def validate_ops01r_live_capture(staging_root:Path,*,expected:Ops01V5ExpectedIdentity): return validate_ops01_v5_package(staging_root, expected=expected)

def main(argv=None):
    ap=argparse.ArgumentParser(); modes=['validate-preflight','validate-discovery-authorization','validate-discovery-result','validate-live-authorization','validate-live-capture','validate-candidate']
    for m in modes: ap.add_argument('--'+m, action='store_true')
    ap.add_argument('--expected-identity-stdin', action='store_true'); ap.add_argument('path', type=Path)
    ns=ap.parse_args(argv); count=sum(getattr(ns,m.replace('-','_')) for m in modes)
    if count!=1: return 2
    if not ns.validate_candidate and not ns.expected_identity_stdin: raise SystemExit('OPS01_V5_EXPECTED_INPUT_INVALID')
    if ns.validate_preflight: res=validate_ops01r_preflight(ns.path, expected=_parse_expected_stdin(Ops01RPreflightExpectedIdentity))
    elif ns.validate_discovery_authorization: res=validate_ops01r_discovery_authorization(ns.path, expected=_parse_expected_stdin(Ops01RDiscoveryAuthorizationExpectedIdentity))
    elif ns.validate_live_authorization: res=validate_ops01r_live_authorization(ns.path, expected=_parse_expected_stdin(Ops01RLiveAuthorizationExpectedIdentity))
    elif ns.validate_live_capture: res=validate_ops01r_live_capture(ns.path, expected=_parse_expected_stdin(Ops01V5ExpectedIdentity))
    elif ns.validate_candidate: res=validate_ops01_v5_package(ns.path, expected=Ops01V5ExpectedIdentity(*(['']*14)))
    else: res=validate_ops01r_discovery_result(ns.path, authorization_path=ns.path, expected=_parse_expected_stdin(Ops01RDiscoveryAuthorizationExpectedIdentity))
    print('PASS' if res.valid else '\n'.join(res.errors)); return 0 if res.valid else 1
if __name__=='__main__': raise SystemExit(main())
