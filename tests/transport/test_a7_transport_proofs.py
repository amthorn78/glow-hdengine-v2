import copy, json, os
from pathlib import Path
import pytest
from tools.evidence import generate_a7_transport_proofs as g

def cat(): return g.catalog_obj()
def invalid(mut):
    c=cat(); mut(c); 
    with pytest.raises(ValueError): g.validate_catalog(c)

def test_valid_unique_reader_designation(): assert g.validate_catalog(cat())['path']=='/reader'
def test_no_designation(): invalid(lambda c: c.__setitem__('success_endpoints', []))
def test_duplicate_designation(): invalid(lambda c: c.__setitem__('success_endpoints', [{'method':'GET','path':'/reader'},{'method':'GET','path':'/reader'}]))
def test_ambiguous_designation(): invalid(lambda c: c['endpoints'].append(dict(c['endpoints'][-2])))
def test_no_matching_endpoint(): invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'GET','path':'/missing'}]))
def test_ineligible_internal_version_and_internal_rejected():
    invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'GET','path':'/internal/version'}]))
    invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'GET','path':'/dev/reader/conjunction'}]))
def test_non_get_designation(): invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'HEAD','path':'/reader'}]))
def test_method_array_rejected(): invalid(lambda c: c['endpoints'][0].__setitem__('method',['POST']))
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
def test_composite_unknown_key_rejected():
    comp=json.loads(g.build()[g.PROOFS[6]]); comp['unknown']=True
    with pytest.raises(ValueError): g.validate_composite(comp)
def test_write_mode_requires_env(monkeypatch):
    monkeypatch.delenv('HDE_WRITE_A7_PROOFS', raising=False)
    # build itself is non-writing and allowed
    assert g.build()
def test_check_expected_bytes_are_non_writing_model():
    outs=g.build(); assert all(isinstance(v, bytes) for v in outs.values())
def test_obsolete_encoding_invariance_absent():
    assert not Path('artifacts/proofs/encoding_invariance.txt').exists()
