import json, os, subprocess, sys
from dataclasses import asdict
from pathlib import Path
from tools.evidence.hde_epic038_ops01_v5 import Ops01RPreflightExpectedIdentity, validate_ops01r_discovery_dispatch

def test_discovery_dispatch_rejects_mutating_tokens(tmp_path):
    res=validate_ops01r_discovery_dispatch(tmp_path/'a', stage='cli_version', prior_results={}, rendered_argv=('railway','deploy'))
    assert not res.valid and 'DISCOVERY_DISPATCH_PROHIBITED_TOKEN' in res.errors

def test_expected_identity_requires_pipe(tmp_path):
    p=tmp_path/'preflight.json'; p.write_text('{}\n')
    exp=Ops01RPreflightExpectedIdentity(*(['x']*10))
    data=(json.dumps(asdict(exp), ensure_ascii=True, sort_keys=True, separators=(',',':'))+'\n').encode()
    proc=subprocess.run([sys.executable,'tools/evidence/hde_epic038_ops01_v5.py','--validate-preflight','--expected-identity-stdin',str(p)], input=data, capture_output=True)
    assert proc.returncode != 0

def test_runner_dormant_modes_do_not_run_external_ops():
    proc=subprocess.run([sys.executable,'scripts/ops/hde_epic038_ops01r.py','--live-child'], capture_output=True, text=True)
    assert proc.returncode != 0
    assert 'dormant' in proc.stderr
