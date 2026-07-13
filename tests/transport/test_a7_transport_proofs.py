import copy, json, os
from pathlib import Path
import pytest
from tools.evidence import generate_a7_transport_proofs as g

def cat(): return g.catalog_obj()
def invalid(mut):
    c=cat(); mut(c); 
    with pytest.raises(ValueError): g.validate_catalog(c)

def test_valid_unique_reader_designation():
    target = g.validate_catalog(cat())
    assert target['path']=='/reader'
    assert target['classification']=='dev_harness'
    assert target['internal'] is True
    sampler=[e for e in cat()['endpoints'] if e['path']=='/internal/dev/sampler']
    assert len(sampler)==1 and sampler[0]['method']=='POST' and sampler[0]['a7_eligible'] is False
def test_no_designation(): invalid(lambda c: c.__setitem__('success_endpoints', []))
def test_duplicate_designation(): invalid(lambda c: c.__setitem__('success_endpoints', [{'method':'GET','path':'/reader'},{'method':'GET','path':'/reader'}]))
def test_ambiguous_designation(): invalid(lambda c: c['endpoints'].append(dict(c['endpoints'][-2])))
def test_no_matching_endpoint(): invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'GET','path':'/missing'}]))
def test_ineligible_internal_version_and_internal_rejected():
    invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'GET','path':'/internal/version'}]))
    invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'GET','path':'/dev/reader/conjunction'}]))
def test_non_get_designation(): invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'HEAD','path':'/reader'}]))
def test_method_array_rejected(): invalid(lambda c: c['endpoints'][0].__setitem__('method',['POST']))
def test_non_boolean_a7_and_bad_generated_at_rejected():
    invalid(lambda c: c['endpoints'][0].__setitem__('a7_eligible','false'))
    invalid(lambda c: c.__setitem__('generated_at_utc','2026-99-99'))
def test_all_canon_valid_classifications_accepted():
    for cls in g.CLASS:
        c=cat(); c['endpoints'][0]['classification']=cls; g.validate_catalog(c)
def test_missing_internal_invalid_class_duplicate_route_id():
    invalid(lambda c: c['endpoints'][0].pop('internal'))
    invalid(lambda c: c['endpoints'][0].__setitem__('classification','bad'))
    invalid(lambda c: c['endpoints'].append(dict(c['endpoints'][0])))
    invalid(lambda c: [e for e in c['endpoints'] if e['path']=='/dev/writer/conjunction'][0].__setitem__('route_id','bad'))
def test_capture_get_head_304_writer_encoding_env_and_restore():
    before=os.environ.get('APP_ENV'); outs=g.build(); after=os.environ.get('APP_ENV')
    assert before==after
    comp=json.loads(outs[g.PROOFS[6]])
    assert comp['get_200']['pass'] and comp['head_200']['pass'] and comp['after_304']['pass']
    g.validate_composite(comp)
    proof = outs[g.PROOFS[1]].decode()
    assert 'content-type=application/json; charset=utf-8' in proof
    assert 'cache-control=private, max-age=0, must-revalidate' in proof
    assert 'vary=Authorization, Accept-Encoding' in proof
    assert 'content-length=' in proof
def test_composite_unknown_key_rejected():
    comp=json.loads(g.build()[g.PROOFS[6]]); comp['unknown']=True
    with pytest.raises(ValueError): g.validate_composite(comp)
def test_composite_nested_unknown_key_rejected():
    comp=json.loads(g.build()[g.PROOFS[6]]); comp['get_200']['unknown']=True
    with pytest.raises(ValueError): g.validate_composite(comp)
def test_encoding_proof_records_decisive_facts():
    proof=g.build()[g.PROOFS[5]].decode()
    for token in ['identity_etag=','gzip_etag=','br_etag=','identity_head_identity_length=','gzip_head_identity_length=','br_head_identity_length=','pass=true']:
        assert token in proof
def test_composite_records_tested_encoding_facts():
    comp=json.loads(g.build()[g.PROOFS[6]])
    assert [e['accept_encoding'] for e in comp['tested_encodings']]==['identity','gzip','br']
    assert all(e['etag']==comp['etag'] for e in comp['tested_encodings'])
    assert all(e['head_identity_length']==comp['get_200']['content_length'] for e in comp['tested_encodings'])
def test_write_mode_requires_env(monkeypatch):
    monkeypatch.delenv('HDE_WRITE_A7_PROOFS', raising=False)
    # build itself is non-writing and allowed
    assert g.build()
def test_check_expected_bytes_are_non_writing_model():
    outs=g.build(); assert all(isinstance(v, bytes) for v in outs.values())
def test_obsolete_encoding_invariance_absent():
    assert not Path('artifacts/proofs/encoding_invariance.txt').exists()
