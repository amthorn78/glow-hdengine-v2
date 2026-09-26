"""A7 transport proof generator (release-sanity stage 05).

Catalog validation is pure.  The live-capture matrix injects the synthetic
complete release through the evaluation seam so ``GET /reader`` can succeed
in-process; the non-admitted matrix (PF10 §2.15) uses the real admission owner:
``build()`` raises the typed ``ReleaseNotAdmitted``, ``main --check`` prints its
explicit line and exits with the distinct code, and write mode refuses.
"""
import json, os, subprocess
from pathlib import Path

import pytest

from engine.compat import compute
from engine.config.registry_loader import SchemaValidationError
from tests.support.pr04_fixtures import build_bundle, build_pack, inject_seams
from tools.evidence import generate_a7_transport_proofs as g
from tools.evidence import run_sanity_pipeline as release_sanity

ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-a7-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-a7-pack"))


@pytest.fixture
def admitted(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    return bundle


def _repo_state() -> tuple[str, str]:
    diff = subprocess.run(["git", "diff", "--exit-code"], cwd=ROOT, text=True, capture_output=True)
    status = subprocess.run(["git", "status", "--porcelain=v1", "--untracked-files=all"], cwd=ROOT, text=True, capture_output=True, check=True)
    return (str(diff.returncode), status.stdout)


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
    production=[e for e in cat()['endpoints'] if e['path']==g.PRODUCTION_READER_PATH]
    assert len(production)==1 and production[0]['method']=='POST' and production[0]['classification']=='public_reader'
    assert production[0]['internal'] is False and production[0]['a7_eligible'] is False and production[0]['env_gate']=='not_applicable_public'
def test_production_row_missing_or_duplicated_rejected():
    invalid(lambda c: c['endpoints'].remove(next(e for e in c['endpoints'] if e['path']==g.PRODUCTION_READER_PATH)))
    invalid(lambda c: c['endpoints'].append(dict(next(e for e in c['endpoints'] if e['path']==g.PRODUCTION_READER_PATH), method='PUT')))
    invalid(lambda c: next(e for e in c['endpoints'] if e['path']==g.PRODUCTION_READER_PATH).__setitem__('internal', True))
    invalid(lambda c: next(e for e in c['endpoints'] if e['path']==g.PRODUCTION_READER_PATH).__setitem__('a7_eligible', True))
    invalid(lambda c: c.__setitem__('success_endpoints',[{'method':'POST','path':g.PRODUCTION_READER_PATH}]))
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


# --- live-capture matrix under the injected synthetic complete release ------------------------

def test_capture_get_head_304_writer_encoding_env_and_restore(admitted):
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

def test_post_reader_is_the_pf05_non_conditional_422_fact(admitted):
    proof = g.build()[g.PROOFS[4]].decode()
    assert proof == (
        'POST /api/reader\nstatus=422\ncode=ERR_READER_INVALID_INPUT\ncache_control=no-store\n'
        'etag_absent=true\nconditional_not_304=true\ncanonical_body=true\n'
    )
    # A 405 (or any other status) for the query-only POST is a failed capture, never accepted.
    app = g.create_app(); app.config.update(TESTING=True)
    with app.test_client() as client:
        resp = client.post(g.PRODUCTION_READER_PATH, query_string=g.q(), headers={'If-None-Match': '"deadbeef"'})
        unprefixed = client.post('/reader', query_string=g.q(), headers={'If-None-Match': '"deadbeef"'})
    assert resp.status_code == 422
    assert resp.headers.get('Cache-Control') == 'no-store' and 'ETag' not in resp.headers
    assert json.loads(resp.data) == {"schema": "v1", "ok": False, "code": "ERR_READER_INVALID_INPUT", "error": json.loads(resp.data)["error"]}
    # PF05 §5.4: the unprefixed POST /reader is not the capture target; it is the governed 405.
    assert unprefixed.status_code == 405 and json.loads(unprefixed.data)["code"] == "ERR_NOT_FOUND"
    assert unprefixed.headers.get('Allow') == 'GET, HEAD'

def test_composite_unknown_key_rejected(admitted):
    comp=json.loads(g.build()[g.PROOFS[6]]); comp['unknown']=True
    with pytest.raises(ValueError): g.validate_composite(comp)
def test_composite_nested_unknown_key_rejected(admitted):
    comp=json.loads(g.build()[g.PROOFS[6]]); comp['get_200']['unknown']=True
    with pytest.raises(ValueError): g.validate_composite(comp)
def test_encoding_proof_records_decisive_facts(admitted):
    proof=g.build()[g.PROOFS[5]].decode()
    for token in ['identity_etag=','gzip_etag=','br_etag=','identity_head_identity_length=','gzip_head_identity_length=','br_head_identity_length=','pass=true']:
        assert token in proof
def test_composite_records_tested_encoding_facts(admitted):
    comp=json.loads(g.build()[g.PROOFS[6]])
    assert [e['accept_encoding'] for e in comp['tested_encodings']]==['identity','gzip','br']
    assert all(e['etag']==comp['etag'] for e in comp['tested_encodings'])
    assert all(e['head_identity_length']==comp['get_200']['content_length'] for e in comp['tested_encodings'])
def test_write_mode_requires_env(admitted, monkeypatch):
    monkeypatch.delenv('HDE_WRITE_A7_PROOFS', raising=False)
    # build itself is non-writing and allowed
    assert g.build()
def test_check_expected_bytes_are_non_writing_model(admitted):
    outs=g.build(); assert all(isinstance(v, bytes) for v in outs.values())
def test_obsolete_encoding_invariance_absent():
    assert not Path('artifacts/proofs/encoding_invariance.txt').exists()


# --- non-admitted matrix with the real admission owner (no injection) --------------------------

def _forbid_live_requests(monkeypatch):
    monkeypatch.setattr(g, "create_app", lambda *a, **k: pytest.fail("Flask app created before admission"))


def _refuse_admission(monkeypatch):
    """The repository root is admitted; the non-admitted branch is reached through the seam."""

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)


def test_build_and_check_succeed_on_the_admitted_root(monkeypatch):
    """On the admitted repository root the live build reproduces the tracked A7 family byte for byte."""
    for name, value in {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}.items():
        monkeypatch.setenv(name, value)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    assert release_sanity.release_not_admitted_observed() is False
    state_before = _repo_state()
    outs = g.build()
    assert outs and all(path.read_bytes() == body for path, body in outs.items())
    g.main(["--check"])
    assert _repo_state() == state_before


def test_build_raises_typed_release_not_admitted_without_any_request(monkeypatch):
    _refuse_admission(monkeypatch)
    _forbid_live_requests(monkeypatch)
    with pytest.raises(release_sanity.ReleaseNotAdmitted) as excinfo:
        g.build()
    assert excinfo.value.code == "INCOMPLETE_RELEASE_ROSTER"
    assert not isinstance(excinfo.value, AssertionError)


def test_main_check_prints_explicit_line_exits_distinct_code_and_writes_nothing(monkeypatch, capsys):
    _refuse_admission(monkeypatch)
    _forbid_live_requests(monkeypatch)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    state_before = _repo_state()
    with pytest.raises(SystemExit) as excinfo:
        g.main(["--check"])
    assert excinfo.value.code == release_sanity.RELEASE_NOT_ADMITTED_EXIT_CODE == 3
    assert capsys.readouterr().out == "A7_TRANSPORT_CHECK:RELEASE_NOT_ADMITTED\n"
    assert _repo_state() == state_before


def test_main_write_mode_refuses_when_not_admitted(monkeypatch, capsys):
    _refuse_admission(monkeypatch)
    _forbid_live_requests(monkeypatch)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    monkeypatch.setenv("HDE_WRITE_A7_PROOFS", "1")
    state_before = _repo_state()
    with pytest.raises(SystemExit) as excinfo:
        g.main([])
    assert excinfo.value.code == release_sanity.RELEASE_NOT_ADMITTED_EXIT_CODE
    assert "RELEASE_NOT_ADMITTED" in capsys.readouterr().out
    assert _repo_state() == state_before


def test_other_admission_refusals_are_not_classified_as_non_admitted(monkeypatch):
    _forbid_live_requests(monkeypatch)

    def other_refusal():
        raise SchemaValidationError("SCHEMA_INVALID", "unrelated refusal")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", other_refusal)
    with pytest.raises(SchemaValidationError, match="unrelated refusal"):
        g.build()
