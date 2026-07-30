from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

import pytest

from tools.evidence import generate_hde_epic038_closeout as closeout

ROOT = Path(__file__).resolve().parents[2]


def test_roster_is_exact_unique_and_ordered() -> None:
    rows = closeout.validate_rows(closeout.build_rows())
    assert len(rows) == len({row.token for row in rows}) == 33
    assert tuple(row.token for row in rows) == closeout.TOKENS
    assert not ({row.token for row in rows} & closeout.PROHIBITED)


@pytest.mark.parametrize(
    "mutation,match",
    [
        (lambda rows: rows[:-1], "token set mismatch"),
        (lambda rows: rows + (rows[0],), "duplicate token"),
        (
            lambda rows: (replace(rows[0], token="TEST_PASS_OK"),) + rows[1:],
            "token set mismatch",
        ),
        (
            lambda rows: (
                replace(rows[0], token="DEV_DB_BRIDGE_FALLBACK_OK"),
            )
            + rows[1:],
            "token set mismatch",
        ),
        (
            lambda rows: (rows[1], rows[0], *rows[2:]),
            "token order mismatch",
        ),
    ],
)
def test_rejects_missing_duplicate_unexpected_retired_near_match_and_reordering(
    mutation, match: str
) -> None:
    with pytest.raises(ValueError, match=match):
        closeout.validate_rows(mutation(closeout.build_rows()))


@pytest.mark.parametrize(
    "label",
    sorted(closeout.PROHIBITED - {"DEV_DB_BRIDGE_FALLBACK_OK"}),
)
def test_rejects_every_non_token_proof_label(label: str) -> None:
    rows = closeout.build_rows()
    with pytest.raises(ValueError, match="token set mismatch"):
        closeout.validate_rows((replace(rows[0], token=label),) + rows[1:])


@pytest.mark.parametrize(
    "field,value,match",
    [
        ("test_binding", "", "empty field"),
        ("posture", "TBD", "placeholder"),
        ("test_binding", "tests/evidence/*", "missing existing path"),
        ("acceptance_token", "TEST_PASS_OK", "token alias"),
        ("primary_evidence", ("missing/existing.json",), "missing existing path"),
        ("artifact_keys", ("guessed.key",), "unregistered artifact key"),
        ("primary_evidence", (), "empty structured field"),
        ("artifact_keys", (), "empty structured field"),
        ("proof_anchors", (), "empty structured field"),
    ],
)
def test_rejects_incomplete_placeholder_wildcard_alias_guesses_and_empty_tuples(
    field, value, match: str
) -> None:
    rows = closeout.build_rows()
    changed = replace(rows[7], **{field: value})
    with pytest.raises(ValueError, match=match):
        closeout.validate_rows(rows[:7] + (changed,) + rows[8:])


@pytest.mark.parametrize(
    "field,value",
    [
        ("primary_evidence", ("docs/evidence/INDEX.json", "docs/evidence/INDEX.sha256")),
        ("artifact_keys", ("index.human_index", "docs.evidence.INDEX.sha256")),
        (
            "proof_anchors",
            (
                "docs/evidence/INDEX.json.path_proof.txt",
                "docs/evidence/INDEX.sha256.path_proof.txt",
            ),
        ),
    ],
)
def test_rejects_every_evidence_binding_count_mismatch(field, value) -> None:
    rows = closeout.build_rows()
    changed = replace(rows[23], **{field: value})
    with pytest.raises(ValueError, match="evidence binding count mismatch"):
        closeout.validate_rows(rows[:23] + (changed,) + rows[24:])


def test_planned_rows_are_exact_owned_absent_and_unclaimed() -> None:
    rows = {row.token: row for row in closeout.validate_rows(closeout.build_rows())}
    assert set(closeout.PLANNED_BINDINGS) == {
        "TESTS_PASS_OK",
        "DOC_DELTA_PRESENT_OK",
        "QA_PRECOMMIT_CHECKLIST_OK",
        "QA_POSTCOMMIT_CHECKLIST_OK",
    }
    for token, (path, key, owner) in closeout.PLANNED_BINDINGS.items():
        row = rows[token]
        assert row.classification == "planned-new"
        assert row.primary_evidence == (path,)
        assert row.artifact_keys == (key,)
        assert row.proof_anchors == (f"{path}.path_proof.txt",)
        assert row.owner_task == owner
        assert row.live_qa.startswith("N/A:")
        assert "UNCLAIMED" in row.posture
        assert "has not been executed" in row.posture
        assert not (ROOT / path).exists()
        assert not (ROOT / f"{path}.path_proof.txt").exists()


def test_rejects_inexact_planned_binding() -> None:
    rows = closeout.build_rows()
    changed = replace(
        rows[0],
        primary_evidence=("audit/EPIC-038-close-report.md",),
        proof_anchors=("audit/EPIC-038-close-report.md.path_proof.txt",),
    )
    with pytest.raises(ValueError, match="inexact planned binding"):
        closeout.validate_rows((changed,) + rows[1:])


def test_database_tokens_bind_admitted_ops03_posture_semantics() -> None:
    rows = {row.token: row for row in closeout.validate_rows(closeout.build_rows())}
    for token in (
        "DB_RUNTIME_SEARCH_PATH_OK",
        "DB_ROLE_OK",
        "DB_SCHEMA_FINGERPRINT_OK",
    ):
        row = rows[token]
        assert row.primary_evidence == (closeout.DB_POSTURE_PATH,)
        assert row.artifact_keys == (closeout.DB_POSTURE_KEY,)
        assert row.test_binding == "tests/ops/test_hde_epic038_ops03.py"
        assert row.live_qa == "qa-22-po-022"
    conn = rows["DB_CONN_ENV_OK"]
    assert conn.primary_evidence == (
        "artifacts/runtime/direct_db_selection.snapshot.json",
    )
    assert conn.artifact_keys == ("epic038.pr06r.direct_db_selection",)


@pytest.mark.parametrize(
    "token,mutation",
    [
        (
            "DB_RUNTIME_SEARCH_PATH_OK",
            lambda payload: payload["observations"].__setitem__(
                "search_path", ["public"]
            ),
        ),
        (
            "DB_ROLE_OK",
            lambda payload: payload["observations"]["runtime_role_flags"].__setitem__(
                "rolsuper", True
            ),
        ),
        (
            "DB_SCHEMA_FINGERPRINT_OK",
            lambda payload: payload["predicates"].__setitem__(
                "ddl_identity_valid", False
            ),
        ),
    ],
)
def test_database_posture_regressions_fail_closed(token, mutation) -> None:
    payload = json.loads((ROOT / closeout.DB_POSTURE_PATH).read_text(encoding="utf-8"))
    mutation(payload)
    with pytest.raises(ValueError, match="database posture predicate mismatch"):
        closeout.validate_db_posture_payload(token, payload)


def test_preimage_row_binds_idempotence_recompute_evidence() -> None:
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "PREIMAGE_RECOMPUTE_OK"
    )
    assert row.primary_evidence == (
        closeout.PREIMAGE_PATH,
        closeout.PREIMAGE_SOURCE_PATH,
    )
    assert row.artifact_keys == (
        closeout.PREIMAGE_KEY,
        closeout.PREIMAGE_SOURCE_KEY,
    )
    assert row.proof_anchors == (
        f"{closeout.PREIMAGE_PATH}.path_proof.txt",
        f"{closeout.PREIMAGE_SOURCE_PATH}.path_proof.txt",
    )
    assert set(row.test_binding.split("; ")) == {
        "tests/evidence/test_determinism_gate_proofs.py",
        "tests/evidence/test_hde_epic038_closeout.py",
    }
    assert row.live_qa == "qa-04-po-004"
    assert "UNCLAIMED" in row.posture


@pytest.mark.parametrize(
    "mutation",
    [
        lambda payload: payload["idempotence_hash"].__setitem__(
            "recomputed", "0" * 64
        ),
        lambda payload: payload["predicates"].__setitem__(
            "preimage_hash_match", False
        ),
        lambda payload: payload.__setitem__(
            "acceptance_token_satisfied", True
        ),
        lambda payload: payload.__setitem__("idempotence_hash", {}),
    ],
)
def test_preimage_recompute_regressions_fail_closed(mutation) -> None:
    payload = json.loads(
        (ROOT / closeout.PREIMAGE_PATH).read_text(encoding="utf-8")
    )
    mutation(payload)
    with pytest.raises(ValueError, match="preimage recompute"):
        closeout.validate_preimage_payload(
            payload,
            (ROOT / closeout.PREIMAGE_SOURCE_PATH).read_bytes(),
        )


def test_preimage_recompute_rejects_matching_forged_hash_pair() -> None:
    payload = json.loads(
        (ROOT / closeout.PREIMAGE_PATH).read_text(encoding="utf-8")
    )
    payload["idempotence_hash"]["stored"] = "0" * 64
    payload["idempotence_hash"]["recomputed"] = "0" * 64
    payload["predicates"]["preimage_hash_match"] = True
    with pytest.raises(ValueError, match="preimage recompute predicate mismatch"):
        closeout.validate_preimage_payload(
            payload,
            (ROOT / closeout.PREIMAGE_SOURCE_PATH).read_bytes(),
        )


def test_no_io_row_binds_explicit_zero_call_log_and_manifest() -> None:
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "NO_EXTERNAL_IO_ON_REFUSAL_OK"
    )
    assert row.primary_evidence == (
        closeout.REFUSAL_PATH,
        closeout.REFUSAL_MANIFEST_PATH,
    )
    assert row.artifact_keys == (
        closeout.REFUSAL_KEY,
        closeout.REFUSAL_MANIFEST_KEY,
    )
    assert row.live_qa == "qa-16-po-016"


@pytest.mark.parametrize(
    "log_mutation,manifest_mutation",
    [
        (lambda text: text.replace("vendor_calls=0", "vendor_calls=1"), None),
        (lambda text: text.replace("db_calls=0", "db_calls=1"), None),
        (
            None,
            lambda payload: payload["predicates"].__setitem__(
                "closed_rails_zero_io", False
            ),
        ),
    ],
)
def test_no_io_regressions_fail_closed(log_mutation, manifest_mutation) -> None:
    log_text = (ROOT / closeout.REFUSAL_PATH).read_text(encoding="utf-8")
    manifest = json.loads(
        (ROOT / closeout.REFUSAL_MANIFEST_PATH).read_text(encoding="utf-8")
    )
    if log_mutation is not None:
        log_text = log_mutation(log_text)
    if manifest_mutation is not None:
        manifest_mutation(manifest)
    with pytest.raises(ValueError, match="closed-rails"):
        closeout.validate_no_io_payloads(log_text, manifest)


def test_final_lf_row_binds_hash_bound_qa19_gate_execution() -> None:
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "CI_CHECK_FINAL_LF_OK"
    )
    assert row.primary_evidence == (closeout.QA_MANIFEST_PATH,)
    assert row.artifact_keys == (closeout.QA_MANIFEST_KEY,)
    assert row.proof_anchors == (
        f"{closeout.QA_MANIFEST_PATH}.path_proof.txt",
    )
    assert set(row.test_binding.split("; ")) == {
        "ci/checks/check_final_lf.sh",
        "tests/evidence/test_hde_epic038_closeout.py",
    }
    assert row.ci_binding == closeout.FINAL_LF_CI_JOB
    assert row.live_qa == closeout.FINAL_LF_CHECK_ID
    assert "UNCLAIMED" in row.posture


@pytest.mark.parametrize(
    "manifest_mutation,log_mutation",
    [
        (
            lambda manifest: manifest[closeout.FINAL_LF_CHECK_ID].__setitem__(
                "sha256", "0" * 64
            ),
            None,
        ),
        (
            None,
            lambda text: text.replace(
                '"exit_code": 0', '"exit_code": 1', 1
            ),
        ),
        (
            None,
            lambda text: text.replace(
                "bash ci/checks/check_final_lf.sh",
                "bash ci/checks/check_mirror_schema.sh",
            ),
        ),
        (
            None,
            lambda text: text.replace(
                "BEHAVIOR_EXIT_CODE=0", "BEHAVIOR_EXIT_CODE=1"
            ),
        ),
    ],
)
def test_final_lf_evidence_regressions_fail_closed(
    manifest_mutation, log_mutation
) -> None:
    manifest = json.loads(
        (ROOT / closeout.QA_MANIFEST_PATH).read_text(encoding="utf-8")
    )
    log_text = (ROOT / closeout.FINAL_LF_LOG_PATH).read_text(encoding="utf-8")
    if manifest_mutation is not None:
        manifest_mutation(manifest)
    if log_mutation is not None:
        log_text = log_mutation(log_text)
    with pytest.raises(ValueError, match="final-LF"):
        closeout.validate_final_lf_evidence(manifest, log_text)


def test_final_lf_script_covers_current_and_planned_closeout_outputs() -> None:
    script_text = (ROOT / closeout.FINAL_LF_SCRIPT_PATH).read_text(
        encoding="utf-8"
    )
    closeout.validate_final_lf_script(script_text)


@pytest.mark.parametrize(
    "path",
    [
        "audit/qa/hde-epic038/token_evidence_matrix.md",
        "audit/EPIC-038_close_report.md",
        "audit/EPIC-038_MANIFEST.json",
    ],
)
def test_final_lf_script_rejects_missing_target_coverage(path: str) -> None:
    script_text = (ROOT / closeout.FINAL_LF_SCRIPT_PATH).read_text(
        encoding="utf-8"
    )
    with pytest.raises(ValueError, match="final-LF target coverage"):
        closeout.validate_final_lf_script(script_text.replace(f"  {path}\n", ""))


def test_final_lf_gate_checks_each_present_planned_output(tmp_path) -> None:
    for relative_path in closeout.FINAL_LF_REQUIRED_PATHS:
        target = tmp_path / relative_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"required\n")

    command = ["bash", str(ROOT / closeout.FINAL_LF_SCRIPT_PATH)]
    initial = subprocess.run(
        command,
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert initial.returncode == 0, initial.stdout + initial.stderr

    planned = tmp_path / closeout.FINAL_LF_PLANNED_PATHS[0]
    planned.parent.mkdir(parents=True, exist_ok=True)
    planned.write_bytes(b"missing-final-lf")
    rejected = subprocess.run(
        command,
        cwd=tmp_path,
        capture_output=True,
        text=True,
    )
    assert rejected.returncode == 1
    assert f"MISSING_FINAL_LF: {closeout.FINAL_LF_PLANNED_PATHS[0]}" in (
        rejected.stderr
    )


def _release_attestation(
    source_commit: str, manifest_sha256: str
) -> dict[str, object]:
    return {
        "schema": "hde.release_attestation.v1",
        "source_commit": source_commit,
        "source_commit_exact": True,
        "manifest_sha256": manifest_sha256,
        "release_id": manifest_sha256,
        "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS",
        "pipeline_stop": None,
    }


def test_release_identity_binding_uses_current_source_and_external_attestation() -> None:
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "RELEASE_ID_RECOMPUTE_OK"
    )
    manifest_sha256 = hashlib.sha256(
        (ROOT / closeout.RELEASE_MANIFEST_PATH).read_bytes()
    ).hexdigest()
    assert row.primary_evidence == (closeout.RELEASE_MANIFEST_PATH,)
    assert row.artifact_keys == (closeout.RELEASE_MANIFEST_KEY,)
    assert row.proof_anchors == (
        f"{closeout.RELEASE_MANIFEST_PATH}.path_proof.txt",
    )
    assert not any(
        path.startswith("artifacts/identity/") for path in row.primary_evidence
    )
    assert "tools/evidence/build_release_attestation.py" in row.test_binding
    assert "tests/evidence/test_release_attestation.py" in row.test_binding
    assert row.ci_binding == closeout.RELEASE_CI_JOB
    assert row.live_qa == "qa-21-po-021"
    assert f"`manifest_sha256={manifest_sha256}`" in row.future_claim
    assert row.posture.startswith("UNCLAIMED:")


@pytest.mark.parametrize(
    "mutation,match",
    [
        (
            lambda payload: payload.__setitem__("source_commit", "b" * 40),
            "source_commit",
        ),
        (
            lambda payload: payload.__setitem__("source_commit_exact", False),
            "source_commit_exact",
        ),
        (
            lambda payload: payload.__setitem__("release_id", "e" * 64),
            "release_id",
        ),
        (
            lambda payload: payload.__setitem__("manifest_sha256", "e" * 64),
            "manifest_sha256",
        ),
    ],
)
def test_release_attestation_rejects_stale_or_source_mismatched_identity(
    mutation, match: str
) -> None:
    source_commit = "a" * 40
    manifest_sha256 = "d" * 64
    payload = _release_attestation(source_commit, manifest_sha256)
    mutation(payload)
    with pytest.raises(ValueError, match=match):
        closeout.validate_release_attestation_payload(
            payload,
            expected_source_commit=source_commit,
            manifest_sha256=manifest_sha256,
        )


def test_render_is_deterministic_lf_terminated_and_never_claims_pass() -> None:
    first = closeout.render()
    second = closeout.render()
    assert first == second and first.endswith(b"\n") and b"\r" not in first
    assert first.count(b"- Canonical governance token:") == 33
    assert first.count(b"- Owning task:") == 33
    assert b"all 33 tokens are UNCLAIMED" in first
    assert b"status=PASS" not in first and b"CLAIMED: PASS" not in first


def test_check_mode_is_read_only_for_matrix_and_unrelated_file() -> None:
    watched = [
        ROOT / closeout.OUTPUT,
        ROOT / "catalog/manifest.json",
        ROOT / "docs/evidence/INDEX.json",
    ]
    before = {
        path: hashlib.sha256(path.read_bytes()).digest() for path in watched
    }
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/evidence/generate_hde_epic038_closeout.py"),
            "--check-token-matrix",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert before == {
        path: hashlib.sha256(path.read_bytes()).digest() for path in watched
    }
