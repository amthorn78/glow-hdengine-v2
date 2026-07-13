from pathlib import Path
import pytest
from tools.evidence import generate_determinism_gate_proofs as g

def test_successful_fixed_corpus_generation_predicates():
    top, outs = g.build()
    assert top
    summary = __import__('json').loads(outs[g.SUM])
    assert summary['predicates']['reader_cli_byte_identity']
    assert summary['predicates']['abba_byte_identity']
    assert summary['predicates']['two_run_byte_identity']
    assert summary['predicates']['preimage_hash_match']
    assert summary['predicates']['canonical_reserialization']

def test_mismatched_abba_fails_top_level():
    top, _ = g.build(ba_override=b'{"bad":true}\n')
    assert not top

def test_failed_canonical_comparison_fails_top_level():
    top, _ = g.build(canon_check=False)
    assert not top

def test_check_mode_model_matches_committed_after_generation(tmp_path):
    top, outs = g.build(); assert top
    for p,b in outs.items():
        assert b.endswith(b'\n')

def test_no_partial_evidence_when_predicate_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(g, 'ID', tmp_path/'IDENTITY_OK.txt')
    top, outs = g.build(ba_override=b'{}\n')
    assert not top
    assert not (tmp_path/'IDENTITY_OK.txt').exists()
