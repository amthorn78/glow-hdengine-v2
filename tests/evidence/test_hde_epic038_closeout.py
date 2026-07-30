from __future__ import annotations

import hashlib
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

from tools.evidence import generate_hde_epic038_closeout as closeout

ROOT = Path(__file__).resolve().parents[2]


def test_roster_is_exact_and_unique() -> None:
    rows = closeout.validate_rows(closeout.build_rows())
    assert len(rows) == len({row.token for row in rows}) == 33
    assert tuple(row.token for row in rows) == closeout.TOKENS
    assert not ({row.token for row in rows} & closeout.PROHIBITED)

@pytest.mark.parametrize("mutation,match", [
    (lambda r: r[:-1], "token set mismatch"),
    (lambda r: r + (r[0],), "duplicate token"),
    (lambda r: (replace(r[0], token="TEST_PASS_OK"),) + r[1:], "token set mismatch"),
    (lambda r: (replace(r[0], token="DEV_DB_BRIDGE_FALLBACK_OK"),) + r[1:], "token set mismatch"),
])
def test_rejects_missing_duplicate_unexpected_retired_and_near_match(mutation, match: str) -> None:
    with pytest.raises(ValueError, match=match): closeout.validate_rows(mutation(closeout.build_rows()))

@pytest.mark.parametrize("label", sorted(closeout.PROHIBITED - {"DEV_DB_BRIDGE_FALLBACK_OK"}))
def test_rejects_every_non_token_proof_label(label: str) -> None:
    rows = closeout.build_rows()
    with pytest.raises(ValueError, match="token set mismatch"):
        closeout.validate_rows((replace(rows[0], token=label),) + rows[1:])

@pytest.mark.parametrize("field,value,match", [
    ("test_binding", "", "empty field"),
    ("posture", "TBD", "placeholder"),
    ("test_binding", "tests/evidence/*", "missing existing path"),
    ("acceptance_token", "TEST_PASS_OK", "token alias"),
    ("primary_evidence", ("missing/existing.json",), "missing existing path"),
    ("artifact_keys", ("guessed.key",), "unregistered artifact key"),
])
def test_rejects_incomplete_placeholder_wildcard_alias_and_guesses(field, value, match: str) -> None:
    rows = closeout.build_rows(); changed = replace(rows[7], **{field: value})
    with pytest.raises(ValueError, match=match): closeout.validate_rows(rows[:7] + (changed,) + rows[8:])


def test_rejects_inexact_planned_binding() -> None:
    rows = closeout.build_rows(); changed = replace(rows[0], classification="planned-new", primary_evidence=("audit/EPIC-038-close-report.md",), proof_anchors=("audit/EPIC-038-close-report.md.path_proof.txt",))
    with pytest.raises(ValueError, match="unauthorized planned path"):
        closeout.validate_rows((changed,) + rows[1:])


def test_render_is_deterministic_lf_terminated_and_never_claims_pass() -> None:
    first = closeout.render(); second = closeout.render()
    assert first == second and first.endswith(b"\n") and b"\r" not in first
    assert first.count(b"- Canonical governance token:") == 33
    assert b"all 33 tokens are UNCLAIMED" in first
    assert b"status=PASS" not in first and b"CLAIMED: PASS" not in first


def test_check_mode_is_read_only_for_matrix_and_unrelated_file() -> None:
    watched = [ROOT / closeout.OUTPUT, ROOT / "catalog/manifest.json", ROOT / "docs/evidence/INDEX.json"]
    before = {path: hashlib.sha256(path.read_bytes()).digest() for path in watched}
    result = subprocess.run([sys.executable, str(ROOT / "tools/evidence/generate_hde_epic038_closeout.py"), "--check-token-matrix"], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert before == {path: hashlib.sha256(path.read_bytes()).digest() for path in watched}


def test_release_identity_binding_is_exact_and_unclaimed() -> None:
    row = next(r for r in closeout.build_rows() if r.token == "RELEASE_ID_RECOMPUTE_OK")
    assert row.primary_evidence == ("catalog/manifest.json", "artifacts/identity/release_id.json", "artifacts/identity/release_id_recompute.log")
    assert row.artifact_keys == ("epic038.pr01.identity_release_id", "epic038.pr01.identity_release_id_recompute")
    assert row.proof_anchors == ("artifacts/identity/release_id.json.path_proof.txt", "artifacts/identity/release_id_recompute.log.path_proof.txt")
    assert "scripts/release_id_recompute.py" in row.test_binding
    assert "tools/evidence/generate_identity_provenance.py" in row.test_binding
    assert "tests/evidence/test_identity_provenance.py" in row.test_binding
    assert row.acceptance_token == row.manifest_token == row.token
    assert row.posture.startswith("UNCLAIMED:")
