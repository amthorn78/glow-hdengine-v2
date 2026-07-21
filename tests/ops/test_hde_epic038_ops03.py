import hashlib,json,sys
from pathlib import Path
from scripts.ops import hde_epic038_ops03 as runner
from tools.evidence import hde_epic038_ops03 as validator

def _auth(tmp_path, run='ops03-fixture-run-0001'):
    cand=Path('/tmp/hde-epic038-ops03')/run/'candidate'
    data={'schema':'hde_epic038.ops03.authorization.v1','run_id':run,'authorized_at_utc':'2026-07-20T00:00:00Z','expires_at_utc':'2026-07-21T00:00:00Z','source_commit':'de061a8097c43dc7dc61093b82c0b1602f3117ce','runner_sha256':'0'*64,'validator_sha256':'0'*64,'interpreter':{'resolved_path':sys.executable,'sha256':'0'*64},'target':{'app_env':'dev','database_schema':'hde','search_path':['hde','public']},'rails':{'safe_mode':'1','allow_network':'0','allow_db_write':'0','db_read_authorized':True},'retired_keys_required_absent':['DB_ALLOW_BRIDGE_IN_PROD','DB_BRIDGE_URL','DB_FORCE_BRIDGE'],'ordered_query_ids':list(runner.ORDERED_QUERY_IDS),'expected_counts':runner.EXPECTED_COUNTS,'candidate_root':cand.as_posix()+'/','exact_argv':{'capture':[],'receipt':[],'validate':[]},'one_attempt':True}
    p=tmp_path/'auth.json'; p.write_text(json.dumps(data,sort_keys=True,separators=(',',':'))+'\n'); return p,cand

def test_ops03_fixture_packet_and_receipt(tmp_path):
    auth,cand=_auth(tmp_path)
    assert runner.main(['--authorization',str(auth),'--fixture']) == 0
    assert (cand/'checksums.sha256').exists()
    assert validator.main(['--emit-receipt','--authorization',str(auth),'--candidate',str(cand)]) == 0
    receipt=json.loads((cand/'validation_receipt.json').read_text())
    assert receipt['result']=='PASS'
    assert receipt['schema']=='hde_epic038.ops03.validation_receipt.v1'

def test_ops03_non_fixture_failure_is_inadmissible(tmp_path):
    auth,cand=_auth(tmp_path, 'ops03-fixture-run-0002')
    assert runner.main(['--authorization',str(auth)]) == 1
    fail=Path('/tmp/hde-epic038-ops03/ops03-fixture-run-0002/failure/failure_receipt.json')
    data=json.loads(fail.read_text())
    assert data['candidate_admissible'] is False
    assert data['launch_consumed'] is True
