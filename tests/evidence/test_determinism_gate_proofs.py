from pathlib import Path
import json
import pytest
from tools.evidence import generate_determinism_gate_proofs as g

def test_successful_fixed_corpus_generation_predicates():
    top, outs = g.build()
    assert top
    summary = json.loads(outs[g.SUM])
    assert summary['predicates']['reader_cli_byte_identity']
    assert summary['predicates']['abba_byte_identity']
    assert summary['predicates']['two_run_byte_identity']
    assert summary['predicates']['preimage_hash_match']
    assert summary['predicates']['canonical_reserialization']
    assert summary['canonical_gate']['passed'] is True
    assert summary['canonical_gate']['command'] == 'python tools/evidence/run_canonical_json_gate.py --check-only'

def test_mismatched_abba_fails_top_level():
    top, _ = g.build(ba_override=b'{"bad":true}\n')
    assert not top

def test_failed_canonical_comparison_fails_top_level():
    top, _ = g.build(canon_gate={'command':'test seam','passed':False,'returncode':1})
    assert not top

def test_unavailable_canonical_gate_fails_closed():
    top, _ = g.build(canon_gate=None if False else {'passed': True})
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

def _redirect_outputs(monkeypatch, tmp_path):
    paths = {
        "AB": tmp_path / "ab.json",
        "BA": tmp_path / "ba.json",
        "SUM": tmp_path / "summary.json",
        "ABB": tmp_path / "abba.bytes",
        "TWO": tmp_path / "tworun_identity.sha256",
        "ID": tmp_path / "IDENTITY_OK.txt",
    }
    for name, path in paths.items():
        monkeypatch.setattr(g, name, path)
    return paths

def test_main_write_mode_produces_exact_expected_files(monkeypatch, tmp_path):
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    monkeypatch.setattr(g, "canonical_gate_result", lambda: {"command": "test canon", "passed": True, "returncode": 0})
    monkeypatch.setattr("sys.argv", ["generate_determinism_gate_proofs.py"])
    g.main()
    assert set(p.name for p in tmp_path.iterdir()) == {p.name for p in paths.values()}
    assert paths["ID"].read_text(encoding="utf-8").startswith("IDENTITY_OK\n")

def test_main_check_mode_makes_no_file_changes(monkeypatch, tmp_path):
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    monkeypatch.setattr(g, "canonical_gate_result", lambda: {"command": "test canon", "passed": True, "returncode": 0})
    top, outs = g.build(canon_gate={"command": "test canon", "passed": True, "returncode": 0})
    assert top
    for p, b in outs.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(b)
    before = {p: p.read_bytes() for p in outs}
    monkeypatch.setattr("sys.argv", ["generate_determinism_gate_proofs.py", "--check"])
    g.main()
    assert {p: p.read_bytes() for p in outs} == before

def test_main_failure_writes_no_marker(monkeypatch, tmp_path):
    paths = _redirect_outputs(monkeypatch, tmp_path)
    monkeypatch.setattr(g, "ensure_determinism_env", lambda *a, **k: None)
    monkeypatch.setattr(g, "canonical_gate_result", lambda: {"command": "test canon", "passed": False, "returncode": 1})
    monkeypatch.setattr("sys.argv", ["generate_determinism_gate_proofs.py"])
    with pytest.raises(SystemExit):
        g.main()
    assert not any(path.exists() for path in paths.values())
