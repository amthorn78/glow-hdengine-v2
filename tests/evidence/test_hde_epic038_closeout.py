from __future__ import annotations

import hashlib
import io
import json
import os
import runpy
import shutil
import stat
import subprocess
import sys
import zipfile
from dataclasses import replace
from pathlib import Path
from typing import Callable, Mapping

import pytest

from tools.evidence import generate_hde_epic038_closeout as closeout
from tools.evidence import update_evidence_index as updater

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND = (
    "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC "
    "python tools/evidence/generate_hde_epic038_closeout.py"
)
EXPECTED_PLAN_CLOSEOUT_CHECK_COMMAND = (
    "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC "
    "python tools/evidence/generate_hde_epic038_closeout.py --check"
)
EXPECTED_PLANNED_CI_BINDING = (
    "test (.github/workflows/ci.yml); planned commands: "
    "python tools/evidence/check_hde_epic038_qa_current_state.py "
    "--require-finalized; "
    "python tools/evidence/generate_hde_epic038_closeout.py --check; "
    "python -m pytest -q tests/evidence/test_hde_epic038_closeout.py"
)
EXPECTED_CHECKLIST_BINDINGS = {
    "QA_PRECOMMIT_CHECKLIST_OK": (
        "audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log",
        "epic038.qa_precommit_checklist",
        "DEV-03",
    ),
    "QA_POSTCOMMIT_CHECKLIST_OK": (
        "audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log",
        "epic038.qa_postcommit_checklist",
        "DEV-03",
    ),
}
EXPECTED_DOC_DELTA_BYTES = (
    b"# HDE-EPIC038 QA Doc Deltas\n"
    b"\n"
    b"## SURFACE BINDING\n"
    b"- Draft/staging surface (primary token-evidence binding): "
    b"`audit/docdeltas/hde-epic038_doc_deltas.md`\n"
    b"- Epic-scoped capture surface (stable QA record): "
    b"`audit/qa/hde-epic038/00_meta/doc_deltas.md`\n"
    b"\n"
    b"## BLOCKERS\n"
    b"- None identified by Step-0 route discovery.\n"
    b"\n"
    b"## CAVEATS\n"
    b"- DOC-CAVEAT-001: Implementation, repository, release, and operational "
    b"evidence do not independently establish Live QA acceptance or epic "
    b"closeout.\n"
)
EXPECTED_HISTORICAL_DOC_DELTA_BYTES = (
    b"# HDE-EPIC038 QA Doc Deltas\n"
    b"\n"
    b"## BLOCKERS\n"
    b"- None identified by Step-0 route discovery.\n"
    b"\n"
    b"## CAVEATS\n"
    b"- DOC-CAVEAT-001: Implementation, repository, release, and operational "
    b"evidence do not independently establish Live QA acceptance or epic "
    b"closeout.\n"
)
EXPECTED_DOC_DELTA_WRITE_COMMAND = (
    "python tools/evidence/generate_hde_epic038_closeout.py --doc-deltas"
)
EXPECTED_DOC_DELTA_CHECK_COMMAND = (
    "python tools/evidence/generate_hde_epic038_closeout.py --check-doc-deltas"
)
EXPECTED_DEV_REQUIREMENTS_INSTALL_COMMAND = (
    "python -m pip install -r requirements-dev.txt"
)
EXPECTED_RUNTIME_REQUIREMENTS_INSTALL_COMMAND = (
    "python -m pip install -r requirements.txt"
)
EXPECTED_PYTEST_READINESS_COMMAND = "python -m pytest --version"
EXPECTED_DEV_REQUIREMENTS_BYTES = (
    b"# Test-only deps\n"
    b"jsonschema==4.23.0\n"
    b"\n"
    b"# Testing framework\n"
    b"pytest>=7.4,<9.0\n"
    b"pytest-cov>=4.1,<5.0\n"
    b"pytest-mock>=3.12,<4.0\n"
)
EXPECTED_DEV_REQUIREMENTS_SHA256 = (
    "2e286c3451a45472dd54ef356895110f6ec320ebe19d488b6348572c3863e04e"
)
EXPECTED_DOC_DELTA_CURRENT_SHA256 = (
    "322db8191bcadf82df5231697d32b66d615e7a9ed88813c596c887d31ae55c4a"
)
EXPECTED_DOC_DELTA_HISTORICAL_SHA256 = (
    "7372dcd1d04e7762a0b826d505c43530578e654bd9fc7a51db5a217685d4bdde"
)
EXPECTED_DOC_DELTA_INDEX_ROLES = {
    "epic038.doc_deltas": (
        "audit/docdeltas/hde-epic038_doc_deltas.md",
        "epic038_doc_delta",
        (
            "Primary draft/staging binding for DOC_DELTA_PRESENT_OK; governed "
            "presence is nonclaiming"
        ),
    ),
    "epic038.qa_meta_doc_deltas": (
        "audit/qa/hde-epic038/00_meta/doc_deltas.md",
        "epic038_doc_delta_capture",
        (
            "Supporting QA capture for the HDE-EPIC038 doc-delta pair; not the "
            "primary token surface and not a token claim"
        ),
    ),
}


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
    changed = replace(rows[7], **{field: value})
    with pytest.raises(ValueError, match="evidence binding count mismatch"):
        closeout.validate_rows(rows[:7] + (changed,) + rows[8:])


def test_every_row_has_the_positive_nonclaiming_contract() -> None:
    assert set(closeout.NONCLAIMING_TEXT_SHA256) == set(closeout.TOKENS)
    for row in closeout.build_rows():
        assert row.posture.startswith(closeout.CURRENT_POSTURE_PREFIX)
        assert row.future_claim.startswith(closeout.FUTURE_CLAIM_PREFIXES)
        digest = hashlib.sha256(
            f"{row.posture}\0{row.future_claim}".encode("utf-8")
        ).hexdigest()
        assert digest == closeout.NONCLAIMING_TEXT_SHA256[row.token]
    row_contract = json.dumps(
        [vars(row) for row in closeout.build_rows()],
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    assert hashlib.sha256(row_contract).hexdigest() == closeout.ROW_CONTRACT_SHA256


@pytest.mark.parametrize("row_index", [0, 7], ids=["planned-new", "existing-reused"])
@pytest.mark.parametrize(
    "field,mutation",
    [
        pytest.param("posture", lambda _value: "CLAIMED", id="claimed-posture"),
        pytest.param(
            "posture",
            lambda value: f"{value} Current status is CLAIMED.",
            id="appended-posture-claim",
        ),
        pytest.param(
            "future_claim",
            lambda _value: "Acceptance is complete.",
            id="affirmative-future-field",
        ),
        pytest.param(
            "future_claim",
            lambda value: f"{value} Current status is CLAIMED.",
            id="appended-future-claim",
        ),
    ],
)
def test_generic_affirmative_claim_language_fails_closed(
    monkeypatch, row_index, field, mutation
) -> None:
    rows = closeout.build_rows()
    row = rows[row_index]
    changed = replace(row, **{field: mutation(getattr(row, field))})
    changed_rows = rows[:row_index] + (changed,) + rows[row_index + 1 :]
    monkeypatch.setattr(closeout, "build_rows", lambda: changed_rows)
    with pytest.raises(ValueError, match="nonclaiming posture contract"):
        closeout.validate_rows(closeout.build_rows())


@pytest.mark.parametrize(
    "row_index,match",
    [(0, "inexact planned command"), (7, "independent row contract drift")],
    ids=["planned-new", "existing-reused"],
)
def test_generic_claim_in_other_rendered_field_fails_closed(
    monkeypatch, row_index, match
) -> None:
    rows = closeout.build_rows()
    row = rows[row_index]
    changed = replace(
        row,
        ci_binding=(
            f"{row.ci_binding} Current status is CLAIMED and acceptance is complete."
        ),
    )
    changed_rows = rows[:row_index] + (changed,) + rows[row_index + 1 :]
    monkeypatch.setattr(closeout, "build_rows", lambda: changed_rows)
    with pytest.raises(ValueError, match=match):
        closeout.validate_rows(closeout.build_rows())


def test_evidence_integrity_rows_bind_actual_surfaces_and_enforcement() -> None:
    rows = {row.token: row for row in closeout.validate_rows(closeout.build_rows())}

    mirror = rows["EVIDENCE_INDEX_MIRROR_OK"]
    assert mirror.primary_evidence == (
        closeout.HUMAN_INDEX_PATH,
        closeout.MACHINE_MIRROR_PATH,
        closeout.QA_MANIFEST_PATH,
    )
    assert mirror.artifact_keys == (
        closeout.HUMAN_INDEX_KEY,
        closeout.MACHINE_MIRROR_KEY,
        closeout.QA_MANIFEST_KEY,
    )
    assert set(mirror.test_binding.split("; ")) == {
        "tools/evidence/update_evidence_index.py",
        closeout.MIRROR_SCHEMA_VALIDATOR_PATH,
        "tests/evidence/test_hde_epic038_closeout.py",
    }
    assert mirror.ci_binding == closeout.EVIDENCE_INDEX_MIRROR_CI_JOB

    paths = rows["EVIDENCE_PATHS_VALIDATED_OK"]
    assert paths.primary_evidence == (
        closeout.MACHINE_MIRROR_PATH,
        closeout.QA_MANIFEST_PATH,
    )
    assert paths.artifact_keys == (
        closeout.MACHINE_MIRROR_KEY,
        closeout.QA_MANIFEST_KEY,
    )
    assert set(paths.test_binding.split("; ")) == {
        closeout.EVIDENCE_PATH_VALIDATOR_PATH,
        "tests/evidence/test_hde_epic038_closeout.py",
    }
    assert paths.ci_binding == closeout.EVIDENCE_PATHS_CI_JOB

    proofs = rows["EVIDENCE_PATH_PROOFS_OK"]
    assert proofs.primary_evidence == (
        closeout.MACHINE_MIRROR_PATH,
        closeout.QA_MANIFEST_PATH,
    )
    assert proofs.artifact_keys == (
        closeout.MACHINE_MIRROR_KEY,
        closeout.QA_MANIFEST_KEY,
    )
    assert set(proofs.test_binding.split("; ")) == {
        closeout.MIRROR_SCHEMA_VALIDATOR_PATH,
        "tests/evidence/test_hde_epic038_closeout.py",
    }
    assert proofs.ci_binding == closeout.EVIDENCE_PATH_PROOFS_CI_JOB

    for row in (mirror, paths, proofs):
        assert row.live_qa == closeout.EVIDENCE_INTEGRITY_CHECK_ID
        assert "UNCLAIMED" in row.posture


@pytest.mark.parametrize(
    "surface,mutation,match",
    [
        (
            "human",
            lambda items: items[:-1],
            "topology mismatch",
        ),
        (
            "mirror",
            lambda items: items + (items[0],),
            "duplicate pair",
        ),
        (
            "mirror",
            lambda items: (items[1], items[0], *items[2:]),
            "topology mismatch",
        ),
    ],
)
def test_index_mirror_topology_regressions_fail_closed(
    surface, mutation, match: str
) -> None:
    human = closeout._human_items()
    mirror = closeout._mirror_items()
    if surface == "human":
        human = mutation(human)
    else:
        mirror = mutation(mirror)
    with pytest.raises(ValueError, match=match):
        closeout.validate_index_mirror_topology(human, mirror)


@pytest.mark.parametrize(
    "path,match",
    [
        ("/tmp/outside", "absolute path"),
        ("../outside", "path traversal"),
        ("missing/evidence.json", "missing file"),
    ],
)
def test_whole_mirror_path_validation_rejects_unsafe_or_missing_paths(
    path: str, match: str
) -> None:
    record = dict(closeout._mirror_items()[0])
    record["discovered_physical_path"] = path
    with pytest.raises(ValueError, match=match):
        closeout.validate_mirror_paths((record,))


def test_whole_mirror_path_validation_rejects_symlink_escape(
    tmp_path, monkeypatch
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    outside = tmp_path / "outside"
    outside.write_text("outside\n", encoding="utf-8")
    (repo / "escape").symlink_to(outside)
    monkeypatch.setattr(closeout, "ROOT", repo)
    with pytest.raises(ValueError, match="outside repository"):
        closeout.validate_mirror_paths(
            ({"discovered_physical_path": "escape"},)
        )


def test_every_mirror_record_and_proof_anchor_is_validated() -> None:
    closeout.validate_all_mirror_proofs()
    items = list(closeout._mirror_items())
    first = dict(items[0])
    second = items[1]

    wrong_proof = dict(first)
    wrong_proof["proof_anchor"] = second["proof_anchor"]
    with pytest.raises(ValueError, match="proof path mismatch"):
        closeout.validate_all_mirror_proofs(
            (wrong_proof, *items[1:])
        )

    wrong_sha = dict(first)
    wrong_sha["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="record binding mismatch"):
        closeout.validate_all_mirror_proofs((wrong_sha, *items[1:]))

    wrong_size = dict(first)
    wrong_size["size_bytes"] = int(first["size_bytes"]) + 1
    with pytest.raises(ValueError, match="record binding mismatch"):
        closeout.validate_all_mirror_proofs((wrong_size, *items[1:]))

    with pytest.raises(ValueError, match="duplicate pair"):
        closeout.validate_all_mirror_proofs((*items, items[0]))


def test_duplicate_and_extra_proof_fields_fail_closed(tmp_path) -> None:
    proof = tmp_path / "artifact.path_proof.txt"
    proof.write_text(
        "path: ../outside\n"
        "path: artifact\n"
        "size_bytes: 1\n"
        f"sha256: {'0' * 64}\n"
        "mtime_utc: 2026-07-31T00:00:00Z\n"
        "produced_at_utc: 2026-07-31T00:00:00Z\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="duplicate"):
        closeout._proof_fields(proof)
    with pytest.raises(SystemExit, match="PROOF_DUPLICATE_FIELD"):
        updater._load_existing_proof(proof)
    mirror_checker = runpy.run_path(
        str(ROOT / "ci/checks/check_mirror_schema.sh"),
        run_name="hde_epic038_mirror_checker_test",
    )
    with pytest.raises(ValueError, match="duplicate"):
        mirror_checker["load_proof"](proof)

    proof.write_text(
        "path: artifact\n"
        "size_bytes: 1\n"
        f"sha256: {'0' * 64}\n"
        "mtime_utc: 2026-07-31T00:00:00Z\n"
        "produced_at_utc: 2026-07-31T00:00:00Z\n"
        "unexpected: contradiction\n",
        encoding="utf-8",
    )
    expected = frozenset(
        {"path", "size_bytes", "sha256", "mtime_utc", "produced_at_utc"}
    )
    with pytest.raises(ValueError, match="roster mismatch"):
        closeout._proof_fields(proof, expected)


def test_integrity_qa19_rejects_missing_path_validator_execution() -> None:
    manifest = json.loads(
        (ROOT / closeout.QA_MANIFEST_PATH).read_text(encoding="utf-8")
    )
    log_text = (
        ROOT / closeout.EVIDENCE_INTEGRITY_LOG_PATH
    ).read_text(encoding="utf-8")
    changed_log = log_text.replace(
        "python tools/evidence/validate_evidence_paths.py",
        "python tools/evidence/orientation_demo.py --check",
    )
    record = manifest[closeout.EVIDENCE_INTEGRITY_CHECK_ID]
    record["sha256"] = hashlib.sha256(changed_log.encode("utf-8")).hexdigest()
    record["size_bytes"] = len(changed_log.encode("utf-8"))
    with pytest.raises(ValueError, match="execution predicate mismatch"):
        closeout.validate_integrity_qa19_evidence(manifest, changed_log)


@pytest.mark.parametrize(
    "validator",
    [closeout.validate_integrity_qa19_evidence, closeout.validate_final_lf_evidence],
    ids=["integrity", "final-lf"],
)
def test_qa19_rejects_command_name_substitution_and_duplicate_receipts(
    validator,
) -> None:
    manifest_bytes = (ROOT / closeout.QA_MANIFEST_PATH).read_text(encoding="utf-8")
    original_lines = (
        ROOT / closeout.EVIDENCE_INTEGRITY_LOG_PATH
    ).read_text(encoding="utf-8").splitlines()
    header = json.loads(original_lines[0])
    header["command"] = (
        "printf '%s' 'python tools/evidence/update_evidence_index.py --check "
        "python tools/evidence/validate_evidence_paths.py "
        "python ci/checks/check_mirror_schema.sh bash ci/checks/check_final_lf.sh'; "
        "true"
    )
    substituted_lines = [json.dumps(header), *original_lines[1:]]
    behavior_index = next(
        index
        for index, line in enumerate(substituted_lines)
        if line.startswith("[behavior command] ")
    )
    substituted_lines[behavior_index] = "[behavior command] true"

    duplicate_receipt_lines = [*original_lines, "BEHAVIOR_EXIT_CODE=0"]
    duplicate_header_lines = [*original_lines]
    duplicate_header_lines[0] = duplicate_header_lines[0].replace(
        '"command":', '"command":"true","command":', 1
    )

    for changed_lines in (
        substituted_lines,
        duplicate_receipt_lines,
        duplicate_header_lines,
    ):
        changed_log = "\n".join(changed_lines) + "\n"
        manifest = json.loads(manifest_bytes)
        record = manifest[closeout.EVIDENCE_INTEGRITY_CHECK_ID]
        record["sha256"] = hashlib.sha256(changed_log.encode("utf-8")).hexdigest()
        record["size_bytes"] = len(changed_log.encode("utf-8"))
        with pytest.raises(ValueError, match="execution (header invalid|predicate mismatch)"):
            validator(manifest, changed_log)


@pytest.mark.parametrize(
    "token,primary,keys,proofs,match",
    [
        (
            "EVIDENCE_INDEX_MIRROR_OK",
            (closeout.HUMAN_INDEX_PATH,),
            (closeout.HUMAN_INDEX_KEY,),
            (f"{closeout.HUMAN_INDEX_PATH}.path_proof.txt",),
            "index/mirror binding mismatch",
        ),
        (
            "EVIDENCE_PATHS_VALIDATED_OK",
            (closeout.HUMAN_INDEX_PATH, closeout.QA_MANIFEST_PATH),
            (closeout.HUMAN_INDEX_KEY, closeout.QA_MANIFEST_KEY),
            (
                f"{closeout.HUMAN_INDEX_PATH}.path_proof.txt",
                f"{closeout.QA_MANIFEST_PATH}.path_proof.txt",
            ),
            "path-validation binding mismatch",
        ),
        (
            "EVIDENCE_PATH_PROOFS_OK",
            (closeout.HUMAN_INDEX_PATH, closeout.QA_MANIFEST_PATH),
            (closeout.HUMAN_INDEX_KEY, closeout.QA_MANIFEST_KEY),
            (
                f"{closeout.HUMAN_INDEX_PATH}.path_proof.txt",
                f"{closeout.QA_MANIFEST_PATH}.path_proof.txt",
            ),
            "path-proof binding mismatch",
        ),
    ],
)
def test_evidence_integrity_rows_reject_human_index_only_bindings(
    token, primary, keys, proofs, match: str
) -> None:
    rows = closeout.build_rows()
    index = next(i for i, row in enumerate(rows) if row.token == token)
    changed = replace(
        rows[index],
        primary_evidence=primary,
        artifact_keys=keys,
        proof_anchors=proofs,
    )
    with pytest.raises(ValueError, match=match):
        closeout.validate_rows(rows[:index] + (changed,) + rows[index + 1 :])


def test_ci_runs_canonical_path_validator_before_mirror_schema() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    path_step = (
        "- name: Validate governed evidence paths\n"
        "        run: python tools/evidence/validate_evidence_paths.py"
    )
    mirror_step = "- run: ci/checks/check_mirror_schema.sh"
    assert path_step in workflow
    assert workflow.index(path_step) < workflow.index(mirror_step)


def test_planned_rows_are_exact_owned_and_source_contract_stays_unclaimed() -> None:
    rows = {row.token: row for row in closeout.validate_rows(closeout.build_rows())}
    assert set(closeout.PLANNED_BINDINGS) == {
        "TESTS_PASS_OK",
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

    assert closeout.PLANNED_BINDINGS["QA_PRECOMMIT_CHECKLIST_OK"] == (
        "audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log",
        "epic038.qa_precommit_checklist",
        "DEV-03",
    )
    assert closeout.PLANNED_BINDINGS["QA_POSTCOMMIT_CHECKLIST_OK"] == (
        "audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log",
        "epic038.qa_postcommit_checklist",
        "DEV-03",
    )
    assert (
        closeout.PLAN_CLOSEOUT_WRITE_COMMAND
        == EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND
    )
    assert (
        closeout.PLAN_CLOSEOUT_CHECK_COMMAND
        == EXPECTED_PLAN_CLOSEOUT_CHECK_COMMAND
    )
    assert closeout.PLANNED_CI_BINDING == EXPECTED_PLANNED_CI_BINDING
    assert {
        token: closeout.PLANNED_BINDINGS[token]
        for token in EXPECTED_CHECKLIST_BINDINGS
    } == EXPECTED_CHECKLIST_BINDINGS
    for token in ("QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"):
        row = rows[token]
        path, key, owner = EXPECTED_CHECKLIST_BINDINGS[token]
        expected_future_claim = (
            "Future status may become CLAIMED only after DEV-02 implements "
            "the plan-authorized deterministic default write invocation "
            f"`{EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND}` and read-only check "
            f"invocation `{EXPECTED_PLAN_CLOSEOUT_CHECK_COMMAND}`, then "
            f"{owner} produces `{path}`, registers exact key `{key}` and its "
            "updater-owned proof, the planned exact-head `test` job commands "
            "succeed, and independent Gate B records PASS."
        )
        assert set(row.test_binding.split("; ")) == {
            "tools/evidence/generate_hde_epic038_closeout.py",
            "tests/evidence/test_hde_epic038_closeout.py",
        }
        assert row.ci_binding == EXPECTED_PLANNED_CI_BINDING
        assert row.future_claim == expected_future_claim
        assert "--closeout" not in row.future_claim


@pytest.mark.parametrize(
    "token",
    ("QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"),
)
@pytest.mark.parametrize(
    "mutation",
    [
        pytest.param(
            lambda text: text.replace(
                f"`{EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND}`",
                f"`{EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND} --closeout`",
            ),
            id="unapproved-closeout-mode",
        ),
        pytest.param(
            lambda text: text.replace(
                f"`{EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND}`",
                "`python tools/evidence/generate_hde_epic038_closeout.py`",
            ),
            id="write-command-missing-rails",
        ),
        pytest.param(
            lambda text: text.replace(
                f"`{EXPECTED_PLAN_CLOSEOUT_CHECK_COMMAND}`",
                (
                    "`SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C "
                    "TZ=UTC python tools/evidence/generate_hde_epic038_closeout.py "
                    "--check-token-matrix`"
                ),
            ),
            id="wrong-read-only-mode",
        ),
        pytest.param(
            lambda text: text.replace(
                "read-only check invocation",
                "check invocation",
            ),
            id="missing-read-only-contract",
        ),
        pytest.param(
            lambda text: text.replace(
                "plan-authorized deterministic default write invocation",
                "read-only check invocation",
            ),
            id="swapped-write-label",
        ),
        pytest.param(
            lambda text: f"{text} The future mode is `--closeout`.",
            id="appended-unapproved-mode",
        ),
        pytest.param(
            lambda text: f"{text} The future mode is `--future-write`.",
            id="appended-extra-mode",
        ),
    ],
)
def test_checklist_rows_reject_inexact_future_command_contract(
    token, mutation
) -> None:
    row = next(row for row in closeout.build_rows() if row.token == token)
    changed = replace(row, future_claim=mutation(row.future_claim))
    assert changed.future_claim != row.future_claim
    with pytest.raises(ValueError, match="checklist planned binding mismatch"):
        closeout._validate_special_semantics(changed)
    rows = closeout.build_rows()
    index = next(index for index, row in enumerate(rows) if row.token == token)
    with pytest.raises(ValueError):
        closeout.validate_rows(rows[:index] + (changed,) + rows[index + 1 :])


@pytest.mark.parametrize(
    "token",
    ("TESTS_PASS_OK", "QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"),
)
def test_planned_rows_reject_appended_write_command_in_ci_binding(token) -> None:
    rows = closeout.build_rows()
    index = next(index for index, row in enumerate(rows) if row.token == token)
    changed = replace(
        rows[index],
        ci_binding=(
            f"{rows[index].ci_binding}; {EXPECTED_PLAN_CLOSEOUT_WRITE_COMMAND}"
        ),
    )
    with pytest.raises(ValueError, match="inexact planned command"):
        closeout.validate_rows(rows[:index] + (changed,) + rows[index + 1 :])


def test_rejects_inexact_planned_binding() -> None:
    rows = closeout.build_rows()
    changed = replace(
        rows[0],
        primary_evidence=("audit/EPIC-038-close-report.md",),
        proof_anchors=("audit/EPIC-038-close-report.md.path_proof.txt",),
    )
    with pytest.raises(ValueError, match="inexact planned binding"):
        closeout.validate_rows((changed,) + rows[1:])


@pytest.mark.parametrize(
    "token,path,key",
    [
        (
            "QA_PRECOMMIT_CHECKLIST_OK",
            "audit/qa/hde-epic038/acceptance_map_viability.log",
            "epic038.acceptance_map_viability",
        ),
        (
            "QA_POSTCOMMIT_CHECKLIST_OK",
            "audit/EPIC-038_MANIFEST.json",
            "epic038.manifest",
        ),
    ],
)
def test_checklist_rows_reject_pr379_substitutions(token, path, key) -> None:
    rows = closeout.build_rows()
    index = next(index for index, row in enumerate(rows) if row.token == token)
    changed = replace(
        rows[index],
        primary_evidence=(path,),
        artifact_keys=(key,),
        proof_anchors=(f"{path}.path_proof.txt",),
    )
    with pytest.raises(ValueError, match="inexact planned binding"):
        closeout.validate_rows(rows[:index] + (changed,) + rows[index + 1 :])


def test_doc_delta_row_binds_primary_staging_and_supporting_capture() -> None:
    primary_path = "audit/docdeltas/hde-epic038_doc_deltas.md"
    primary_key = "epic038.doc_deltas"
    capture_path = "audit/qa/hde-epic038/00_meta/doc_deltas.md"
    capture_key = "epic038.qa_meta_doc_deltas"
    historical_check = "qa-00-step-0-discovery"
    historical_log = (
        "audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log"
    )
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "DOC_DELTA_PRESENT_OK"
    )
    assert row.classification == "existing/reused"
    assert row.primary_evidence == (primary_path,)
    assert row.artifact_keys == (primary_key,)
    assert row.proof_anchors == (f"{primary_path}.path_proof.txt",)
    assert capture_path not in row.primary_evidence
    assert capture_path in row.posture
    assert capture_key in row.posture
    assert historical_log in row.posture
    assert "explicitly names the staging path" in row.posture
    assert EXPECTED_DOC_DELTA_WRITE_COMMAND in row.posture
    assert EXPECTED_DOC_DELTA_CHECK_COMMAND in row.posture
    assert EXPECTED_DOC_DELTA_CURRENT_SHA256 in row.posture
    assert EXPECTED_DOC_DELTA_HISTORICAL_SHA256 in row.posture
    assert "it did not produce the current normalized bytes" in row.posture
    assert "pair-identity predicate" in row.future_claim
    assert "never current-byte production" in row.future_claim
    assert row.live_qa == historical_check
    assert set(row.test_binding.split("; ")) == {
        "tools/evidence/generate_hde_epic038_closeout.py",
        "tests/evidence/test_hde_epic038_closeout.py",
    }
    assert row.ci_binding == (
        "test (.github/workflows/ci.yml): "
        "Check HDE-EPIC038 DEV-01 doc-delta pair"
    )

    primary = (ROOT / primary_path).read_bytes()
    capture = (ROOT / capture_path).read_bytes()
    assert primary == capture == EXPECTED_DOC_DELTA_BYTES
    assert closeout.render_doc_delta_pair() == EXPECTED_DOC_DELTA_BYTES
    assert (
        closeout.render_historical_doc_delta_pair()
        == EXPECTED_HISTORICAL_DOC_DELTA_BYTES
    )
    assert EXPECTED_HISTORICAL_DOC_DELTA_BYTES != EXPECTED_DOC_DELTA_BYTES
    closeout.validate_doc_delta_surface(primary, surface="staging")
    closeout.validate_doc_delta_surface(capture, surface="capture")
    closeout.validate_doc_delta_pair_identity(primary, capture)

    records = closeout._mirror_records()
    assert (
        primary_key,
        primary_path,
        f"{primary_path}.path_proof.txt",
    ) in records
    assert (
        capture_key,
        capture_path,
        f"{capture_path}.path_proof.txt",
    ) in records
    for items, is_mirror in (
        (closeout._human_items(), False),
        (closeout._mirror_items(), True),
    ):
        for key, (path, record_type, notes) in EXPECTED_DOC_DELTA_INDEX_ROLES.items():
            record = next(item for item in items if item.get("artifact_key") == key)
            assert record["discovered_physical_path"] == path
            assert record["epic_id"] == "HDE-EPIC038"
            assert record["record_type"] == record_type
            assert record["schema_version"] == "1.0"
            assert record["notes"] == notes
            if is_mirror:
                assert record["role"] == "snapshot"
                assert record["proof_anchor"] == f"{path}.path_proof.txt"
    closeout.validate_doc_delta_evidence()


def test_doc_delta_writer_is_exact_bounded_and_byte_idempotent(
    tmp_path, monkeypatch
) -> None:
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    historical_validations = []
    monkeypatch.setattr(
        closeout,
        "validate_doc_delta_historical_origin",
        lambda: historical_validations.append(True),
    )
    staging = tmp_path / closeout.DOC_DELTA_PRIMARY_PATH
    capture = tmp_path / closeout.DOC_DELTA_CAPTURE_PATH
    historical_log = tmp_path / closeout.DOC_DELTA_HISTORICAL_LOG_PATH
    unrelated = tmp_path / "audit/qa/hde-epic038/00_meta/unrelated.txt"
    for path, data in (
        (staging, b"stale staging\n"),
        (capture, b"stale capture\n"),
        (historical_log, b"immutable historical receipt\n"),
        (unrelated, b"unrelated\n"),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    protected_before = {
        path: path.read_bytes() for path in (historical_log, unrelated)
    }

    closeout.write_doc_delta_pair()
    first = (staging.read_bytes(), capture.read_bytes())
    closeout.write_doc_delta_pair()
    second = (staging.read_bytes(), capture.read_bytes())

    assert first == second == (EXPECTED_DOC_DELTA_BYTES,) * 2
    assert historical_validations == [True, True]
    assert protected_before == {
        path: path.read_bytes() for path in (historical_log, unrelated)
    }
    assert sorted(
        str(path.relative_to(tmp_path))
        for path in tmp_path.rglob("*")
        if path.is_file()
    ) == sorted(
        (
            closeout.DOC_DELTA_PRIMARY_PATH,
            closeout.DOC_DELTA_CAPTURE_PATH,
            closeout.DOC_DELTA_HISTORICAL_LOG_PATH,
            "audit/qa/hde-epic038/00_meta/unrelated.txt",
        )
    )


@pytest.mark.parametrize("failed_replace", (1, 2), ids=("first", "second"))
def test_doc_delta_writer_restores_both_originals_after_replace_failure(
    tmp_path, monkeypatch, failed_replace
) -> None:
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    monkeypatch.setattr(
        closeout,
        "validate_doc_delta_historical_origin",
        lambda: None,
    )
    targets = [
        tmp_path / closeout.DOC_DELTA_PRIMARY_PATH,
        tmp_path / closeout.DOC_DELTA_CAPTURE_PATH,
    ]
    originals = (b"original staging\n", b"original capture\n")
    for target, data in zip(targets, originals):
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)

    real_replace = closeout.Path.replace
    replace_count = 0

    def fail_one_replace(source, destination):
        nonlocal replace_count
        replace_count += 1
        if replace_count == failed_replace:
            raise OSError("injected replace failure")
        return real_replace(source, destination)

    monkeypatch.setattr(closeout.Path, "replace", fail_one_replace)
    with pytest.raises(OSError, match="injected replace failure"):
        closeout.write_doc_delta_pair()

    assert tuple(target.read_bytes() for target in targets) == originals
    assert not tuple(tmp_path.rglob("*.tmp"))


def test_doc_delta_check_helper_is_read_only_and_rejects_either_side_drift(
    tmp_path, monkeypatch
) -> None:
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    paths = [
        tmp_path / closeout.DOC_DELTA_PRIMARY_PATH,
        tmp_path / closeout.DOC_DELTA_CAPTURE_PATH,
    ]
    for path in paths:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(EXPECTED_DOC_DELTA_BYTES)
    before = {
        path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths
    }
    closeout.check_doc_delta_pair()
    assert before == {
        path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths
    }

    for path in paths:
        path.write_bytes(EXPECTED_DOC_DELTA_BYTES + b"drift\n")
        with pytest.raises(ValueError, match="current producer drift"):
            closeout.check_doc_delta_pair()
        path.write_bytes(EXPECTED_DOC_DELTA_BYTES)


def test_doc_delta_ci_binds_one_read_only_check_and_never_the_writer() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    closeout.validate_doc_delta_ci(workflow)
    test_job = workflow[
        workflow.index("  test:\n") : workflow.index(
            "\n  compat-conj-pr01-closure:", workflow.index("  test:\n")
        )
    ]
    assert test_job.count(f"run: {EXPECTED_DOC_DELTA_CHECK_COMMAND}") == 1
    assert test_job.count(f"          {EXPECTED_DEV_REQUIREMENTS_INSTALL_COMMAND}\n") == 1
    assert (
        test_job.count(
            f"          {EXPECTED_RUNTIME_REQUIREMENTS_INSTALL_COMMAND}\n"
        )
        == 1
    )
    assert test_job.count(f"          {EXPECTED_PYTEST_READINESS_COMMAND}\n") == 1
    assert EXPECTED_DOC_DELTA_WRITE_COMMAND not in workflow
    requirements_path = ROOT / "requirements-dev.txt"
    assert not requirements_path.is_symlink()
    assert requirements_path.read_bytes() == EXPECTED_DEV_REQUIREMENTS_BYTES
    assert (
        hashlib.sha256(EXPECTED_DEV_REQUIREMENTS_BYTES).hexdigest()
        == EXPECTED_DEV_REQUIREMENTS_SHA256
        == closeout.DEV_REQUIREMENTS_SHA256
    )
    check_line = f"run: {EXPECTED_DOC_DELTA_CHECK_COMMAND}"
    step_name = "      - name: Check HDE-EPIC038 DEV-01 doc-delta pair"
    indented_check = f"        {check_line}"
    explicit_shell = "        shell: bash"
    focused_step_name = "      - name: Run HDE-EPIC038 DEV-01 focused tests"
    strict_shell = "          set -euo pipefail"
    dev_install = f"          {EXPECTED_DEV_REQUIREMENTS_INSTALL_COMMAND}"
    runtime_install = f"          {EXPECTED_RUNTIME_REQUIREMENTS_INSTALL_COMMAND}"
    pytest_readiness = f"          {EXPECTED_PYTEST_READINESS_COMMAND}"
    focused_run = (
        "          python -m pytest -q "
        "tests/evidence/test_hde_epic038_closeout.py"
    )
    focused_step = "\n".join(
        (
            focused_step_name,
            explicit_shell,
            "        run: |",
            strict_shell,
            dev_install,
            runtime_install,
            pytest_readiness,
            focused_run,
        )
    )
    assert test_job.index(dev_install) < test_job.index(pytest_readiness)
    assert test_job.index(dev_install) < test_job.index(runtime_install)
    assert test_job.index(runtime_install) < test_job.index(pytest_readiness)
    assert test_job.index(pytest_readiness) < test_job.index(focused_run)
    assert "      - run: python -m pip install pytest\n" not in test_job
    assert (
        "test -f requirements-dev.txt && python -m pip install "
        "-r requirements-dev.txt || true"
    ) not in test_job
    job_anchor = "  test:\n"
    mutations = (
        workflow.replace(check_line, check_line + "; echo appended"),
        workflow + (
            "\nrun: python tools/evidence/generate_hde_epic038_closeout.py  "
            "--doc-deltas\n"
        ),
        workflow + (
            "\nrun: python ./tools/evidence/generate_hde_epic038_closeout.py "
            "--doc-deltas\n"
        ),
        workflow + (
            "\nrun: python -m tools.evidence.generate_hde_epic038_closeout "
            "--doc-deltas\n"
        ),
        workflow + (
            "\nrun: |\n  python tools/evidence/"
            "generate_hde_epic038_closeout.py \\\n    --doc-deltas\n"
        ),
        workflow.replace(step_name, f"      # {step_name.strip()}", 1),
        workflow.replace(
            indented_check,
            "        if: ${{ false }}\n" + indented_check,
            1,
        ),
        workflow.replace(
            focused_run,
            focused_run + "\n        if: ${{ false }}",
            1,
        ),
        workflow.replace(
            focused_run,
            focused_run + "\n        continue-on-error: true",
            1,
        ),
        workflow.replace(
            focused_run,
            focused_run + "\n        shell: /usr/bin/true {0}",
            1,
        ),
        workflow.replace(
            focused_run,
            focused_run + "\n        env:\n          PYTEST_ADDOPTS: --collect-only",
            1,
        ),
        workflow.replace(
            dev_install,
            "          python -m pip install pytest",
            1,
        ),
        workflow.replace(
            dev_install,
            "          test -f requirements-dev.txt && "
            + EXPECTED_DEV_REQUIREMENTS_INSTALL_COMMAND
            + " || true",
            1,
        ),
        workflow.replace(
            dev_install,
            "          python -m pip install -r requirements.txt",
            1,
        ),
        workflow.replace(
            dev_install,
            dev_install + " --no-deps",
            1,
        ),
        workflow.replace(
            focused_step,
            focused_step.replace(runtime_install + "\n", "", 1),
            1,
        ),
        workflow.replace(
            pytest_readiness,
            "          python -m pytest --help",
            1,
        ),
        workflow.replace(
            dev_install
            + "\n"
            + runtime_install
            + "\n"
            + pytest_readiness
            + "\n"
            + focused_run,
            dev_install
            + "\n"
            + runtime_install
            + "\n"
            + focused_run
            + "\n"
            + pytest_readiness,
            1,
        ),
        workflow.replace(
            focused_step,
            focused_step.replace(strict_shell + "\n", "", 1),
            1,
        ),
        workflow.replace(
            dev_install,
            dev_install + "\n          echo /tmp/pr382-shim >> \"$GITHUB_PATH\"",
            1,
        ),
        workflow.replace(
            dev_install,
            dev_install + "\n          export PATH=/tmp/pr382-shim:$PATH",
            1,
        ),
        workflow.replace(
            dev_install,
            dev_install + "\n          alias python=true",
            1,
        ),
        workflow.replace(
            dev_install,
            dev_install + "\n          python() { :; }",
            1,
        ),
        workflow.replace(
            focused_step,
            focused_step.replace(
                dev_install, dev_install + " || true", 1
            ),
            1,
        ),
        workflow.replace(
            focused_step,
            focused_step.replace(
                dev_install, dev_install + "; true", 1
            ),
            1,
        ),
        workflow.replace(
            focused_step,
            focused_step.replace(
                pytest_readiness,
                "          pytest --version",
                1,
            ),
            1,
        ),
        workflow.replace(
            focused_step,
            focused_step.replace(
                explicit_shell,
                "        shell: /usr/bin/true {0}",
                1,
            ),
            1,
        ),
        workflow.replace(
            pytest_readiness + "\n" + focused_run,
            focused_run + "\n" + pytest_readiness,
            1,
        ),
        workflow.replace(
            pytest_readiness,
            pytest_readiness + " || true",
            1,
        ),
        workflow.replace(
            pytest_readiness,
            pytest_readiness + "\n        if: ${{ false }}",
            1,
        ),
        workflow.replace(
            pytest_readiness,
            pytest_readiness + "\n        continue-on-error: true",
            1,
        ),
        workflow.replace(
            pytest_readiness,
            pytest_readiness + "\n        shell: /usr/bin/true {0}",
            1,
        ),
        workflow.replace(
            indented_check,
            "        continue-on-error: true\n" + indented_check,
            1,
        ),
        workflow.replace(
            explicit_shell,
            "        shell: /usr/bin/true {0}",
            1,
        ),
        workflow.replace(job_anchor, job_anchor + "    if: ${{ false }}\n", 1),
        workflow.replace(
            job_anchor,
            job_anchor + "    continue-on-error: true\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + "    \"if\": ${{ false }}\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + "    'if': ${{ false }}\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + "    if : ${{ false }}\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + "    \"continue-on-error\": true\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + "    continue-on-error : true\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + '    "\\u0069f": ${{ false }}\n',
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + '    "\\x69f": ${{ false }}\n',
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor + "    <<: *suppress\n",
            1,
        ),
        workflow.replace(
            job_anchor,
            job_anchor
            + "    defaults:\n"
            + "      run:\n"
            + "        shell: /usr/bin/true {0}\n",
            1,
        ),
        workflow.replace(
            "jobs:\n",
            "defaults:\n"
            + "  run:\n"
            + "    shell: /usr/bin/true {0}\n"
            + "jobs:\n",
            1,
        ),
        workflow.replace(
            "on: [push, pull_request]",
            "on: workflow_dispatch",
            1,
        ),
        workflow.replace("jobs:\n", "jobs: {}\n", 1),
        workflow + "\n  test :\n    runs-on: ubuntu-latest\n    steps: []\n",
        workflow + "\n  'test':\n    runs-on: ubuntu-latest\n    steps: []\n",
        workflow + '\n  "test":\n    runs-on: ubuntu-latest\n    steps: []\n',
        workflow + '\n  "\\u0074est":\n    runs-on: ubuntu-latest\n    steps: []\n',
        workflow.replace(
            step_name,
            "      - name: Shadow Python before the governed check\n"
            + "        shell: bash\n"
            + "        run: |\n"
            + "          mkdir -p /tmp/pr382-shim\n"
            + "          printf '#!/bin/sh\\nexit 0\\n' > /tmp/pr382-shim/python\n"
            + "          chmod +x /tmp/pr382-shim/python\n"
            + "          echo /tmp/pr382-shim >> \"$GITHUB_PATH\"\n"
            + step_name,
            1,
        ),
        workflow.replace(
            indented_check,
            indented_check
            + "\n      - name: Shadow Python after the implementation check\n"
            + "        shell: bash\n"
            + "        run: |\n"
            + "          mkdir -p /tmp/pr382-shim\n"
            + "          printf '#!/bin/sh\\nexit 0\\n' > /tmp/pr382-shim/python\n"
            + "          chmod +x /tmp/pr382-shim/python\n"
            + "          echo /tmp/pr382-shim >> \"$GITHUB_PATH\"",
            1,
        ),
    )
    for changed in mutations:
        assert changed != workflow
        with pytest.raises(ValueError, match="CI command binding mismatch"):
            closeout.validate_doc_delta_ci(changed)


def test_private_receipt_ci_is_exact_head_external_and_authenticated() -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    closeout.validate_doc_delta_ci(workflow)
    test_job = workflow[
        workflow.index("  test:\n") : workflow.index(
            "\n  compat-conj-pr01-closure:", workflow.index("  test:\n")
        )
    ]
    expected_needs = (
        "    needs:\n"
        "      - compat-conj-pr01-closure\n"
        "      - epic020\n"
        "      - compat-http-epic020\n"
        "      - epic020-evidence-bundles\n"
        "      - rails-policy-gates\n"
        "      - sanity-pipeline\n"
    )
    assert expected_needs in test_job
    assert "    permissions:\n      actions: read\n      contents: read\n" in test_job
    assert '      PYTHONDONTWRITEBYTECODE: "1"\n' in test_job
    assert (
        "          ref: ${{ github.event.pull_request.head.sha || github.sha }}\n"
        in test_job
    )
    assert (
        "name: hde-release-attestation-${{ github.event.pull_request.head.sha || github.sha }}"
        in test_job
    )
    assert (
        "name: hde-epic038-execution-receipt-"
        "${{ github.event.pull_request.head.sha || github.sha }}-"
        "${{ github.run_id }}-${{ github.run_attempt }}"
        in test_job
    )
    assert "path: ${{ runner.temp }}/hde-epic038-private-receipt" in test_job
    assert f"audit/{closeout.PRIVATE_CI_RECEIPT_NAME}" not in workflow
    producer_step = test_job[
        test_job.index(
            "      - name: Produce conditional private HDE-EPIC038 execution receipt"
        ) : test_job.index(
            "      - run: python tools/evidence/orientation_demo.py --check"
        )
    ]
    receipt_start = test_job.index(
        "      - name: Produce conditional private HDE-EPIC038 execution receipt"
    )
    assert (
        "      - run: python tools/evidence/update_evidence_index.py --check\n"
        not in test_job[:receipt_start]
    )
    assert (
        "            python tools/evidence/update_evidence_index.py --check\n"
        in producer_step
    )
    positions = [
        producer_step.index(f"              {command}")
        for command in closeout.PRIVATE_CI_COMMANDS
    ]
    assert positions == sorted(positions)
    writer = producer_step.index("closeout._write_private_ci_receipt()")
    assert positions[-1] < writer
    assert producer_step.count("git worktree add --detach") == 1

    receipt_free_clean = test_job.index(
        "      - name: Confirm receipt-free exact-head tree is clean"
    )
    legacy_evidence_tests = test_job.index(
        "      - name: Run legacy EPIC020/021 evidence tests in isolated exact-head worktree"
    )
    legacy_evidence_step = test_job[legacy_evidence_tests:receipt_free_clean]
    epic021_tests = legacy_evidence_step.index(
        "            EPIC021_QA_RUN_ID=ci-selftest-epic021 python -m pytest "
        "tests/qa/test_epic021_harness_entrypoint.py"
    )
    full_repo_tests = legacy_evidence_step.index(
        "            python -m pytest tests/evidence "
        "tests/ops/test_evidence_index.py tests/ops/test_hde_epic038_ops03.py"
    )
    assert legacy_evidence_step.count("git worktree add --detach") == 1
    assert legacy_evidence_step.count("git worktree remove --force") == 1
    assert legacy_evidence_step.count("trap cleanup EXIT") == 1
    assert legacy_evidence_step.count("trap - EXIT") == 1
    assert (
        'git worktree add --detach "$legacy_source" "$(git rev-parse HEAD)"'
        in legacy_evidence_step
    )
    assert '            cd "$legacy_source"\n' in legacy_evidence_step
    assert (
        "            unset GH_TOKEN _HDE_EPIC038_PRIVATE_CI_ROOT "
        "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID "
        "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST\n"
        in legacy_evidence_step
    )
    assert (
        "            export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 "
        "ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1\n"
        in legacy_evidence_step
    )
    assert '            export PYTHONPATH="$legacy_source"\n' in legacy_evidence_step
    assert "      - name: Run EPIC021 QA harness entrypoint self-test" not in test_job
    assert "      - run: python -m pytest tests/evidence " not in test_job
    upload = test_job.index(
        "      - name: Publish private exact-head HDE-EPIC038 execution receipt"
    )
    assert 0 <= epic021_tests < full_repo_tests
    assert legacy_evidence_tests < receipt_free_clean < upload
    upload_block = test_job[
        upload : test_job.index(
            "      - name: Authenticate and consume private HDE-EPIC038 execution artifact"
        )
    ]
    assert "        id: epic038_receipt_artifact\n" in upload_block
    assert "          overwrite: false\n" in upload_block
    assert "if: always()" not in upload_block

    consumer = test_job.index(
        "      - name: Authenticate and consume private HDE-EPIC038 execution artifact"
    )
    final_clean = test_job.index(
        "      - name: Confirm authenticated exact-head receipt fixed point is clean"
    )
    consumer_step = test_job[consumer:final_clean]
    assert upload < consumer < final_clean
    assert "          GH_TOKEN: ${{ github.token }}\n" in consumer_step
    assert (
        "${{ steps.epic038_receipt_artifact.outputs.artifact-id }}" in consumer_step
    )
    assert (
        "${{ steps.epic038_receipt_artifact.outputs.artifact-digest }}"
        in consumer_step
    )
    assert '          ALLOW_NETWORK: "1"\n' not in consumer_step
    assert consumer_step.count("git worktree add --detach") == 1
    assert consumer_step.count("ALLOW_NETWORK=1") == 2
    assert consumer_step.count("ALLOW_NETWORK=0") == 4
    assert consumer_step.count(
        "unset GH_TOKEN _HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID "
        "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST"
    ) == 2
    control_plane_write = consumer_step.index(
        f"            {closeout.PRIVATE_CI_CONTROL_PLANE_WRITE_COMMAND}\n"
    )
    control_plane_check = consumer_step.index(
        f"            {closeout.PRIVATE_CI_CONTROL_PLANE_CHECK_COMMAND}\n"
    )
    updater_check = consumer_step.index(
        "              SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C "
        "LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check\n"
    )
    assert control_plane_write < control_plane_check < updater_check
    assert test_job.index("git diff --exit-code", final_clean) > final_clean

    mutations = (
        workflow.replace(
            "      - compat-conj-pr01-closure\n", "", 1
        ),
        workflow.replace('      PYTHONDONTWRITEBYTECODE: "1"\n', "", 1),
        workflow.replace(
            "      - run: python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized\n",
            "      - run: python tools/evidence/update_evidence_index.py --check\n"
            "      - run: python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized\n",
            1,
        ),
        workflow.replace(
            "          ref: ${{ github.event.pull_request.head.sha || github.sha }}",
            "          ref: main",
            1,
        ),
        workflow.replace(
            "              unset _HDE_EPIC038_PRIVATE_CI_ROOT\n", "", 1
        ),
        workflow.replace(
            f"              {closeout.PLAN_CLOSEOUT_PREFLIGHT_COMMAND}",
            f"              {closeout.PLAN_CLOSEOUT_PREFLIGHT_COMMAND} || true",
            1,
        ),
        workflow.replace(
            "        if: steps.epic038_receipt.outputs.produced == 'true'",
            "        if: always()",
            1,
        ),
        workflow.replace("      actions: read\n", "      actions: write\n", 1),
        workflow.replace("          overwrite: false\n", "          overwrite: true\n", 1),
        workflow.replace(
            "${{ steps.epic038_receipt_artifact.outputs.artifact-id }}",
            "777777",
            1,
        ),
        workflow.replace(
            "${{ steps.epic038_receipt_artifact.outputs.artifact-digest }}",
            "dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",
            1,
        ),
        workflow.replace("          GH_TOKEN: ${{ github.token }}\n", "", 1),
        workflow.replace(
            "              unset GH_TOKEN _HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID "
            "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST\n",
            "",
            1,
        ),
        workflow.replace(
            "              SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C "
            "LANG=C TZ=UTC python tools/evidence/update_evidence_index.py\n",
            "              SAFE_MODE=1 ALLOW_NETWORK=1 APP_ENV=dev LC_ALL=C "
            "LANG=C TZ=UTC python tools/evidence/update_evidence_index.py\n",
            1,
        ),
        workflow.replace(
            "          path: ${{ runner.temp }}/hde-epic038-private-receipt",
            "          path: audit/hde-epic038-private-receipt",
            1,
        ),
        workflow.replace(
            '          git worktree add --detach "$legacy_source" "$(git rev-parse HEAD)"',
            '          git worktree add --detach "$legacy_source" main',
            1,
        ),
        workflow.replace(
            "      - name: Confirm authenticated exact-head receipt fixed point is clean\n"
            "        run: |\n"
            "          git diff --check\n"
            "          git diff --exit-code\n",
            "      - name: Confirm authenticated exact-head receipt fixed point is clean\n"
            "        run: |\n"
            "          git diff --check\n",
            1,
        ),
    )
    for changed in mutations:
        assert changed != workflow
        with pytest.raises(ValueError, match="CI command binding mismatch"):
            closeout.validate_doc_delta_ci(changed)


def test_doc_delta_ci_freezes_regular_dev_requirements_file(
    tmp_path, monkeypatch
) -> None:
    workflow = (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
    requirements_path = tmp_path / "requirements-dev.txt"
    requirements_path.write_bytes(EXPECTED_DEV_REQUIREMENTS_BYTES)
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    closeout.validate_doc_delta_ci(workflow)

    mutations = (
        EXPECTED_DEV_REQUIREMENTS_BYTES.replace(
            b"pytest>=7.4,<9.0", b"pytest", 1
        ),
        EXPECTED_DEV_REQUIREMENTS_BYTES.replace(
            b"jsonschema==4.23.0", b"jsonschema", 1
        ),
        EXPECTED_DEV_REQUIREMENTS_BYTES + b"-r other-requirements.txt\n",
        EXPECTED_DEV_REQUIREMENTS_BYTES.removesuffix(b"\n"),
    )
    for changed in mutations:
        requirements_path.write_bytes(changed)
        with pytest.raises(ValueError, match="CI command binding mismatch"):
            closeout.validate_doc_delta_ci(workflow)

    requirements_path.unlink()
    with pytest.raises(ValueError, match="CI command binding mismatch"):
        closeout.validate_doc_delta_ci(workflow)

    source = tmp_path / "requirements-source.txt"
    source.write_bytes(EXPECTED_DEV_REQUIREMENTS_BYTES)
    requirements_path.symlink_to(source)
    with pytest.raises(ValueError, match="CI command binding mismatch"):
        closeout.validate_doc_delta_ci(workflow)


def test_doc_delta_renderer_cannot_redefine_its_frozen_test_or_index_baseline(
    monkeypatch,
) -> None:
    changed_lines = tuple(
        "- changed" if line.startswith("- None identified") else line
        for line in closeout._doc_delta_required_nonempty_lines()
    )
    monkeypatch.setattr(
        closeout,
        "_doc_delta_required_nonempty_lines",
        lambda: changed_lines,
    )
    changed = (
        "\n".join(
            (
                changed_lines[0],
                "",
                *changed_lines[1:4],
                "",
                *changed_lines[4:6],
                "",
                *changed_lines[6:],
                "",
            )
        )
    ).encode("utf-8")
    monkeypatch.setattr(
        closeout,
        "DOC_DELTA_CURRENT_PAIR_SHA256",
        hashlib.sha256(changed).hexdigest(),
    )
    assert closeout.render_doc_delta_pair() == changed
    assert changed != EXPECTED_DOC_DELTA_BYTES
    with pytest.raises(ValueError, match="injected/disk byte mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=changed,
            capture_bytes=changed,
        )


def test_doc_delta_semantics_do_not_use_pair_identity_as_a_substitute() -> None:
    primary = EXPECTED_DOC_DELTA_BYTES
    # An extra blank line changes bytes without changing any governed semantic
    # line. The PF04/PF27 layer accepts both surfaces independently.
    capture = primary.replace(b"\n## BLOCKERS", b"\n\n## BLOCKERS", 1)
    assert capture != primary
    closeout.validate_doc_delta_semantics(primary, surface="staging")
    closeout.validate_doc_delta_semantics(capture, surface="capture")
    closeout.validate_doc_delta_surface(primary, surface="staging")
    with pytest.raises(ValueError, match="capture canonical layout mismatch"):
        closeout.validate_doc_delta_surface(capture, surface="capture")
    with pytest.raises(ValueError, match="QA-plan pair identity mismatch"):
        closeout.validate_doc_delta_pair_identity(primary, capture)
    with pytest.raises(ValueError, match="capture canonical layout mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
        )


@pytest.mark.parametrize(
    "primary,capture",
    ((EXPECTED_DOC_DELTA_BYTES, None), (None, EXPECTED_DOC_DELTA_BYTES)),
    ids=("primary-only", "capture-only"),
)
def test_doc_delta_evidence_rejects_partial_injected_pair(primary, capture) -> None:
    with pytest.raises(ValueError, match="partial byte injection"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
        )


@pytest.mark.parametrize(
    "mutation",
    [
        lambda data: data.replace(
            b"- Draft/staging surface (primary token-evidence binding): "
            b"`audit/docdeltas/hde-epic038_doc_deltas.md`\n",
            b"",
        ),
        lambda data: data.replace(
            b"audit/docdeltas/hde-epic038_doc_deltas.md",
            b"audit/docdeltas/wrong.md",
        ),
        lambda data: data.replace(
            b"audit/docdeltas/hde-epic038_doc_deltas.md",
            b"__STAGING_PATH__",
        )
        .replace(
            b"audit/qa/hde-epic038/00_meta/doc_deltas.md",
            b"audit/docdeltas/hde-epic038_doc_deltas.md",
        )
        .replace(
            b"__STAGING_PATH__",
            b"audit/qa/hde-epic038/00_meta/doc_deltas.md",
        ),
        lambda data: data.replace(b"## BLOCKERS\n", b""),
        lambda data: data.replace(b"## CAVEATS\n", b""),
        lambda data: data.replace(
            b"- DOC-CAVEAT-001: Implementation, repository, release, and "
            b"operational evidence do not independently establish Live QA "
            b"acceptance or epic closeout.\n",
            b"",
        ),
        lambda data: data.replace(
            b"## BLOCKERS\n",
            b"## BLOCKERS\n## SURFACE BINDING\n",
        ),
        lambda data: data.replace(
            b"- Draft/staging surface (primary token-evidence binding): "
            b"`audit/docdeltas/hde-epic038_doc_deltas.md`\n",
            b"- Draft/staging surface (primary token-evidence binding): "
            b"`audit/docdeltas/hde-epic038_doc_deltas.md`\n"
            b"- Draft/staging surface (primary token-evidence binding): "
            b"`audit/docdeltas/hde-epic038_doc_deltas.md`\n",
        ),
    ],
    ids=(
        "missing-staging-reference",
        "wrong-staging-reference",
        "reversed-roles",
        "missing-blockers-section",
        "missing-caveats-section",
        "missing-stable-caveat",
        "duplicate-binding",
        "duplicate-staging-reference",
    ),
)
def test_doc_delta_identical_semantic_defects_fail_closed(mutation) -> None:
    deficient = mutation(EXPECTED_DOC_DELTA_BYTES)
    assert deficient != EXPECTED_DOC_DELTA_BYTES
    # Equality alone is intentionally insufficient: both deficient inputs fail
    # before the separate r7/PF19 pair-identity predicate is considered.
    with pytest.raises(ValueError, match="staging semantic contract mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=deficient,
            capture_bytes=deficient,
        )
    with pytest.raises(ValueError, match="capture semantic contract mismatch"):
        closeout.validate_doc_delta_surface(deficient, surface="capture")


@pytest.mark.parametrize(
    "deficient",
    [
        EXPECTED_DOC_DELTA_BYTES.removesuffix(b"\n"),
        b"\xef\xbb\xbf" + EXPECTED_DOC_DELTA_BYTES,
        EXPECTED_DOC_DELTA_BYTES.replace(b"\n", b"\r\n"),
        EXPECTED_DOC_DELTA_BYTES + b"\xff",
    ],
    ids=("missing-final-lf", "utf8-bom", "crlf", "invalid-utf8"),
)
def test_doc_delta_encoding_and_lf_contract_fails_closed(deficient) -> None:
    with pytest.raises(ValueError, match="capture semantic contract mismatch"):
        closeout.validate_doc_delta_surface(deficient, surface="capture")


@pytest.mark.parametrize(
    "deficient,match",
    [
        (
            EXPECTED_DOC_DELTA_BYTES.replace(
                b"\n## BLOCKERS", b"\n\n## BLOCKERS", 1
            ),
            "staging canonical layout mismatch",
        ),
        (
            EXPECTED_DOC_DELTA_BYTES.replace(
                b"## BLOCKERS", "## BLOCKERS\u2028".encode("utf-8"), 1
            ),
            "staging semantic contract mismatch",
        ),
        (
            EXPECTED_DOC_DELTA_BYTES.replace(
                b"## BLOCKERS", b"## BLOCKERS\x0b", 1
            ),
            "staging semantic contract mismatch",
        ),
        (
            EXPECTED_DOC_DELTA_BYTES.replace(
                b"## BLOCKERS", b"## BLOCKERS\x0c", 1
            ),
            "staging semantic contract mismatch",
        ),
    ],
    ids=("extra-blank-line", "unicode-line-separator", "vertical-tab", "form-feed"),
)
def test_doc_delta_equal_noncanonical_pair_fails_closed(deficient, match) -> None:
    with pytest.raises(ValueError, match=match):
        closeout.validate_doc_delta_evidence(
            primary_bytes=deficient,
            capture_bytes=deficient,
        )


def test_doc_delta_pair_and_historical_origin_regressions_fail_closed() -> None:
    primary = (ROOT / "audit/docdeltas/hde-epic038_doc_deltas.md").read_bytes()
    capture = (
        ROOT / "audit/qa/hde-epic038/00_meta/doc_deltas.md"
    ).read_bytes()
    manifest = json.loads(
        (ROOT / "audit/qa/hde-epic038/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    historical_log_bytes = (
        ROOT
        / "audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log"
    ).read_bytes()
    assert hashlib.sha256(historical_log_bytes).hexdigest() == (
        "db9e7ac48e168f7fac380f294271110bbf5e88b0874a1e6d5591cb868d6eecbe"
    )
    assert len(historical_log_bytes) == 8248
    historical_log = historical_log_bytes.decode("utf-8")
    assert primary == capture == EXPECTED_DOC_DELTA_BYTES
    assert (
        hashlib.sha256(EXPECTED_HISTORICAL_DOC_DELTA_BYTES).hexdigest()
        == EXPECTED_DOC_DELTA_HISTORICAL_SHA256
    )
    assert closeout.render_historical_doc_delta_pair() == (
        EXPECTED_HISTORICAL_DOC_DELTA_BYTES
    )
    header = json.loads(historical_log.splitlines()[0])
    historical_command = header["command"]
    assert "## SURFACE BINDING" not in historical_command
    assert EXPECTED_DOC_DELTA_WRITE_COMMAND not in historical_command
    assert EXPECTED_DOC_DELTA_CHECK_COMMAND not in historical_command
    closeout.validate_doc_delta_historical_origin(manifest, historical_log)

    with pytest.raises(ValueError, match="capture semantic contract mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture + b"drift\n",
            qa_manifest=manifest,
            historical_log=historical_log,
        )

    with pytest.raises(ValueError, match="staging semantic contract mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=b"unbound replacement\n",
            capture_bytes=b"unbound replacement\n",
            qa_manifest=manifest,
            historical_log=historical_log,
        )

    changed_manifest = json.loads(json.dumps(manifest))
    changed_manifest["qa-00-step-0-discovery"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="historical manifest binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=changed_manifest,
            historical_log=historical_log,
        )

    changed_log = historical_log.replace(
        '"doc_delta_posture": "created"',
        '"doc_delta_posture": "preserved_existing"',
    )
    assert changed_log != historical_log
    changed_log_manifest = json.loads(json.dumps(manifest))
    changed_log_bytes = changed_log.encode("utf-8")
    changed_log_manifest["qa-00-step-0-discovery"]["sha256"] = hashlib.sha256(
        changed_log_bytes
    ).hexdigest()
    changed_log_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        changed_log_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest|origin) binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=changed_log_manifest,
            historical_log=changed_log,
        )

    open_rails_lines = historical_log.splitlines()
    open_rails_header = json.loads(open_rails_lines[0])
    open_rails_header["captured_env"]["SAFE_MODE"] = "0"
    open_rails_header["captured_env"]["ALLOW_NETWORK"] = "1"
    open_rails_lines[0] = json.dumps(open_rails_header, sort_keys=True)
    open_rails_log = "\n".join(open_rails_lines) + "\n"
    open_rails_bytes = open_rails_log.encode("utf-8")
    open_rails_manifest = json.loads(json.dumps(manifest))
    open_rails_manifest["qa-00-step-0-discovery"]["sha256"] = hashlib.sha256(
        open_rails_bytes
    ).hexdigest()
    open_rails_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        open_rails_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest|origin) binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=open_rails_manifest,
            historical_log=open_rails_log,
        )

    duplicate_artifact_lines = historical_log.splitlines()
    duplicate_artifact_header = json.loads(duplicate_artifact_lines[0])
    duplicate_artifact_header["evidence_artifacts"].append(
        "audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log"
    )
    duplicate_artifact_lines[0] = json.dumps(
        duplicate_artifact_header,
        sort_keys=True,
    )
    duplicate_artifact_log = "\n".join(duplicate_artifact_lines) + "\n"
    duplicate_artifact_bytes = duplicate_artifact_log.encode("utf-8")
    duplicate_artifact_manifest = json.loads(json.dumps(manifest))
    duplicate_artifact_manifest["qa-00-step-0-discovery"]["sha256"] = (
        hashlib.sha256(duplicate_artifact_bytes).hexdigest()
    )
    duplicate_artifact_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        duplicate_artifact_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest|origin) binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=duplicate_artifact_manifest,
            historical_log=duplicate_artifact_log,
        )

    failed_behavior_log = historical_log.replace(
        "BEHAVIOR_EXIT_CODE=0",
        "BEHAVIOR_EXIT_CODE=1",
        1,
    )
    assert failed_behavior_log != historical_log
    failed_behavior_bytes = failed_behavior_log.encode("utf-8")
    failed_behavior_manifest = json.loads(json.dumps(manifest))
    failed_behavior_manifest["qa-00-step-0-discovery"]["sha256"] = (
        hashlib.sha256(failed_behavior_bytes).hexdigest()
    )
    failed_behavior_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        failed_behavior_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest|origin) binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=failed_behavior_manifest,
            historical_log=failed_behavior_log,
        )

    contradictory_receipt_log = historical_log + "BEHAVIOR_EXIT_CODE=1\n"
    contradictory_receipt_bytes = contradictory_receipt_log.encode("utf-8")
    contradictory_receipt_manifest = json.loads(json.dumps(manifest))
    contradictory_receipt_manifest["qa-00-step-0-discovery"]["sha256"] = (
        hashlib.sha256(contradictory_receipt_bytes).hexdigest()
    )
    contradictory_receipt_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        contradictory_receipt_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest|origin) binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=contradictory_receipt_manifest,
            historical_log=contradictory_receipt_log,
        )

    duplicate_result_log = historical_log + json.dumps(
        {
            "doc_delta_posture": "created",
            "epic_id": "HDE-EPIC038",
            "future_check_artifacts": "NOT RUN",
            "production_factory_missing_routes": [],
            "production_factory_required_routes": [],
            "qa_root": "audit/qa/hde-epic038/",
            "repository": "glow-hdengine-v2",
        },
        sort_keys=True,
    ) + "\n"
    duplicate_result_bytes = duplicate_result_log.encode("utf-8")
    duplicate_result_manifest = json.loads(json.dumps(manifest))
    duplicate_result_manifest["qa-00-step-0-discovery"]["sha256"] = (
        hashlib.sha256(duplicate_result_bytes).hexdigest()
    )
    duplicate_result_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        duplicate_result_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest binding|log shape) mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=duplicate_result_manifest,
            historical_log=duplicate_result_log,
        )

    contradictory_result_log = historical_log.replace(
        '"production_factory_missing_routes": []',
        '"production_factory_missing_routes": [["/api/compat/v1", "POST"]]',
        1,
    )
    assert contradictory_result_log != historical_log
    contradictory_result_bytes = contradictory_result_log.encode("utf-8")
    contradictory_result_manifest = json.loads(json.dumps(manifest))
    contradictory_result_manifest["qa-00-step-0-discovery"]["sha256"] = (
        hashlib.sha256(contradictory_result_bytes).hexdigest()
    )
    contradictory_result_manifest["qa-00-step-0-discovery"]["size_bytes"] = len(
        contradictory_result_bytes
    )
    with pytest.raises(ValueError, match="historical (?:manifest|origin) binding mismatch"):
        closeout.validate_doc_delta_evidence(
            primary_bytes=primary,
            capture_bytes=capture,
            qa_manifest=contradictory_result_manifest,
            historical_log=contradictory_result_log,
        )


@pytest.mark.parametrize(
    "current_marker",
    (
        EXPECTED_DOC_DELTA_WRITE_COMMAND,
        "python ./tools/evidence/generate_hde_epic038_closeout.py --doc-deltas",
        "python -m tools.evidence.generate_hde_epic038_closeout --check-doc-deltas",
        (
            "python -c 'from tools.evidence.generate_hde_epic038_closeout "
            "import write_doc_delta_pair; write_doc_delta_pair()'"
        ),
        "python -c \"print('SURFACE BINDING')\"",
    ),
    ids=(
        "exact-writer",
        "alternate-writer",
        "module-check",
        "imported-writer",
        "single-quoted-marker",
    ),
)
def test_historical_receipt_cannot_be_correlated_into_current_producer(
    monkeypatch, current_marker
) -> None:
    manifest = json.loads(
        (ROOT / closeout.QA_MANIFEST_PATH).read_text(encoding="utf-8")
    )
    lines = (
        ROOT / closeout.DOC_DELTA_HISTORICAL_LOG_PATH
    ).read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    header["command"] += f"; {current_marker}"
    lines[0] = json.dumps(header, sort_keys=True)
    changed_log = "\n".join(lines) + "\n"
    changed_bytes = changed_log.encode("utf-8")
    changed_manifest = json.loads(json.dumps(manifest))
    changed_manifest[closeout.DOC_DELTA_HISTORICAL_CHECK_ID]["sha256"] = (
        hashlib.sha256(changed_bytes).hexdigest()
    )
    changed_manifest[closeout.DOC_DELTA_HISTORICAL_CHECK_ID]["size_bytes"] = len(
        changed_bytes
    )
    monkeypatch.setattr(
        closeout,
        "DOC_DELTA_HISTORICAL_LOG_SHA256",
        hashlib.sha256(changed_bytes).hexdigest(),
    )
    monkeypatch.setattr(
        closeout,
        "DOC_DELTA_HISTORICAL_LOG_SIZE_BYTES",
        len(changed_bytes),
    )
    with pytest.raises(ValueError, match="historical origin binding mismatch"):
        closeout.validate_doc_delta_historical_origin(
            changed_manifest,
            changed_log,
        )


@pytest.mark.parametrize(
    "path",
    [
        "audit/docdeltas/hde-epic038_doc_deltas.md",
        "audit/qa/hde-epic038/00_meta/doc_deltas.md",
    ],
    ids=("staging", "capture"),
)
def test_doc_delta_stale_path_proof_fails_closed(tmp_path, monkeypatch, path) -> None:
    target = tmp_path / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(EXPECTED_DOC_DELTA_BYTES)
    proof_path = tmp_path / f"{path}.path_proof.txt"
    proof_path.write_text(
        f"path: {path}\n"
        f"size_bytes: {len(EXPECTED_DOC_DELTA_BYTES)}\n"
        f"sha256: {'0' * 64}\n"
        "mtime_utc: 2026-07-31T00:00:00Z\n"
        "produced_at_utc: 2026-07-31T00:00:00Z\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    with pytest.raises(ValueError, match="proof sha mismatch"):
        closeout._validate_proof(path, f"{path}.path_proof.txt")


@pytest.mark.parametrize("field,value", [("sha256", "0" * 64), ("size_bytes", 0)])
def test_doc_delta_stale_mirror_record_fails_closed(field, value) -> None:
    human = closeout._human_items()
    items = list(closeout._mirror_items())
    index = next(
        index
        for index, item in enumerate(items)
        if item["artifact_key"] == "epic038.qa_meta_doc_deltas"
    )
    changed = dict(items[index])
    changed[field] = value
    items[index] = changed
    with pytest.raises(ValueError, match="Index/Mirror record binding mismatch"):
        closeout.validate_doc_delta_index_bindings(human, items)


def test_human_index_rejects_duplicate_governed_fields(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    target = tmp_path / closeout.HUMAN_INDEX_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        '[{"artifact_key":"first","artifact_key":"last",'
        '"discovered_physical_path":"audit/docdeltas/first.md",'
        '"discovered_physical_path":"audit/docdeltas/last.md"}]\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Human Index shape mismatch"):
        closeout._human_items()


def test_machine_mirror_rejects_duplicate_governed_fields(
    tmp_path, monkeypatch
) -> None:
    monkeypatch.setattr(closeout, "ROOT", tmp_path)
    target = tmp_path / closeout.MACHINE_MIRROR_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        '{"artifact_key":"epic038.doc_deltas",'
        '"sha256":"first","sha256":"last",'
        '"proof_anchor":"first","proof_anchor":"last"}\n',
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Machine Mirror record shape mismatch: 1"):
        closeout._mirror_items()


@pytest.mark.parametrize("surface", ("human", "mirror"))
@pytest.mark.parametrize(
    "key",
    ("epic038.doc_deltas", "epic038.qa_meta_doc_deltas"),
)
def test_doc_delta_index_records_reject_token_claim_fields(surface, key) -> None:
    human = [dict(item) for item in closeout._human_items()]
    mirror = [dict(item) for item in closeout._mirror_items()]
    items = human if surface == "human" else mirror
    record = next(item for item in items if item.get("artifact_key") == key)
    record["tokens"] = ["DOC_DELTA_PRESENT_OK"]
    with pytest.raises(ValueError, match="Index/Mirror family binding mismatch"):
        closeout.validate_doc_delta_index_bindings(human, mirror)


@pytest.mark.parametrize("surface", ("human", "mirror"))
@pytest.mark.parametrize(
    "alias_kind",
    ("same-path-new-key", "same-key-other-path"),
)
def test_doc_delta_index_family_rejects_claiming_aliases(
    surface, alias_kind
) -> None:
    human = [dict(item) for item in closeout._human_items()]
    mirror = [dict(item) for item in closeout._mirror_items()]
    items = human if surface == "human" else mirror
    primary = next(
        item for item in items if item.get("artifact_key") == "epic038.doc_deltas"
    )
    alias = dict(primary)
    if alias_kind == "same-path-new-key":
        alias["artifact_key"] = "epic038.doc_deltas.claiming_alias"
        alias["discovered_physical_path"] = (
            "./" + closeout.DOC_DELTA_PRIMARY_PATH
        )
    else:
        alias["discovered_physical_path"] = closeout.DOC_DELTA_CAPTURE_PATH
    alias["tokens"] = ["DOC_DELTA_PRESENT_OK"]
    items.append(alias)
    with pytest.raises(ValueError, match="Index/Mirror family binding mismatch"):
        closeout.validate_doc_delta_index_bindings(human, mirror)


@pytest.mark.parametrize("field", ["record_type", "notes"])
def test_doc_delta_swapped_index_role_metadata_fails_closed(field) -> None:
    human = [dict(item) for item in closeout._human_items()]
    mirror = [dict(item) for item in closeout._mirror_items()]
    keys = ("epic038.doc_deltas", "epic038.qa_meta_doc_deltas")
    for items in (human, mirror):
        records = [
            next(item for item in items if item.get("artifact_key") == key)
            for key in keys
        ]
        records[0][field], records[1][field] = records[1][field], records[0][field]
    with pytest.raises(ValueError, match="Index/Mirror record binding mismatch"):
        closeout.validate_doc_delta_index_bindings(human, mirror)


@pytest.mark.parametrize(
    "path,key",
    [
        (
            "audit/qa/hde-epic038/00_meta/doc_deltas.md",
            "epic038.qa_meta_doc_deltas",
        ),
        (
            "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
            "epic038.closeout_remediation_ledger",
        ),
    ],
)
def test_doc_delta_row_rejects_capture_or_ledger_as_primary(path, key) -> None:
    rows = closeout.build_rows()
    index = next(
        index
        for index, row in enumerate(rows)
        if row.token == "DOC_DELTA_PRESENT_OK"
    )
    row = rows[index]
    changed = replace(
        row,
        primary_evidence=(path,),
        artifact_keys=(key,),
        proof_anchors=(f"{path}.path_proof.txt",),
    )
    with pytest.raises(ValueError, match="doc-delta evidence binding mismatch"):
        closeout._validate_special_semantics(changed)
    with pytest.raises(ValueError):
        closeout.validate_rows(rows[:index] + (changed,) + rows[index + 1 :])


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


def test_cli_reader_parity_row_binds_actual_reader_dump_checks() -> None:
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "CLI_READER_PARITY_OK"
    )
    assert row.primary_evidence == (closeout.PREIMAGE_PATH,)
    assert row.artifact_keys == (closeout.PREIMAGE_KEY,)
    assert row.proof_anchors == (f"{closeout.PREIMAGE_PATH}.path_proof.txt",)
    assert set(row.test_binding.split("; ")) == {
        "tests/evidence/test_determinism_gate_proofs.py",
        "tests/cli/test_showcompat_parity_and_identity.py",
    }
    assert row.live_qa == "qa-04-po-004"
    assert "reader-dump/runtime comparison" in row.future_claim


@pytest.mark.parametrize(
    "mutation",
    [
        lambda payload: payload["predicates"].__setitem__(
            "reader_cli_byte_identity", False
        ),
        lambda payload: payload["hashes"].__setitem__("cli_sha256", "0" * 64),
        lambda payload: payload.__setitem__("acceptance_token_satisfied", True),
        lambda payload: payload["sources"].__setitem__(
            "cli", "python -m engine.cli showcompat"
        ),
    ],
)
def test_cli_reader_parity_regressions_fail_closed(mutation) -> None:
    payload = json.loads(
        (ROOT / closeout.PREIMAGE_PATH).read_text(encoding="utf-8")
    )
    mutation(payload)
    with pytest.raises(ValueError, match="CLI/Reader parity"):
        closeout.validate_cli_reader_parity_payload(payload)


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
        (lambda text: text + "vendor_calls=1 db_calls=1\n", None),
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
        "source_tree_sha256": "c" * 64,
        "manifest_sha256": manifest_sha256,
        "release_id": manifest_sha256,
        "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS",
        "pipeline_stop": None,
        "rails": dict(sorted(closeout.RELEASE_ATTESTATION_RAILS.items())),
    }


def _configure_private_ci_evidence(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    *,
    include_receipt: bool = True,
    authenticate_receipt: bool | None = None,
    run_id: str = "424242",
) -> tuple[Path, dict[str, object], dict[str, object]]:
    source_commit = "a" * 40
    manifest_sha256 = hashlib.sha256(
        (closeout.ROOT / closeout.RELEASE_MANIFEST_PATH).read_bytes()
    ).hexdigest()
    attestation = _release_attestation(source_commit, manifest_sha256)
    attestation_bytes = closeout._canonical_json(attestation)
    root = tmp_path / f"private-ci-{run_id}"
    attestation_root = root / closeout.PRIVATE_CI_ATTESTATION_DIR
    attestation_root.mkdir(parents=True)
    (attestation_root / "attestation.json").write_bytes(attestation_bytes)
    receipt = closeout._private_execution_receipt_payload(
        attestation,
        attestation_bytes,
        event_name="pull_request",
        run_id=run_id,
        run_attempt="1",
        source_commit=source_commit,
    )
    if include_receipt:
        (root / closeout.PRIVATE_CI_RECEIPT_NAME).write_bytes(
            closeout._canonical_json(receipt)
        )
    monkeypatch.setattr(
        closeout,
        "_verify_private_release_attestation_bundle",
        lambda _root: None,
    )
    monkeypatch.setattr(closeout, "_current_source_commit", lambda: source_commit)
    exact_source_tree_sha256 = str(attestation["source_tree_sha256"])
    monkeypatch.setattr(
        closeout,
        "_current_source_tree_sha256",
        lambda: exact_source_tree_sha256,
    )
    monkeypatch.setattr(
        closeout,
        "_validate_private_source_worktree",
        lambda *, allow_generated: None,
    )
    if authenticate_receipt is None:
        authenticate_receipt = include_receipt
    if authenticate_receipt:
        monkeypatch.delenv(closeout.PRIVATE_CI_ROOT_ENV, raising=False)
        monkeypatch.setenv(closeout.PRIVATE_CI_ARTIFACT_ID_ENV, "777777")
        monkeypatch.setenv(closeout.PRIVATE_CI_ARTIFACT_DIGEST_ENV, "d" * 64)

        def authenticated_files() -> dict[str, bytes]:
            return {
                path.relative_to(root).as_posix(): path.read_bytes()
                for path in sorted(root.rglob("*"))
                if path.is_file() and not path.is_symlink()
            }

        monkeypatch.setattr(
            closeout,
            "_authenticated_private_ci_files",
            authenticated_files,
        )
    else:
        monkeypatch.delenv(closeout.PRIVATE_CI_ARTIFACT_ID_ENV, raising=False)
        monkeypatch.delenv(closeout.PRIVATE_CI_ARTIFACT_DIGEST_ENV, raising=False)
        monkeypatch.setenv(closeout.PRIVATE_CI_ROOT_ENV, str(root))
    return root, receipt, attestation


def _private_ci_archive(root: Path) -> bytes:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(root.rglob("*")):
            if path.is_file():
                archive.writestr(path.relative_to(root).as_posix(), path.read_bytes())
    return stream.getvalue()


def _private_ci_api_payloads(
    *, source_commit: str, archive: bytes, run_id: str = "424242"
) -> tuple[dict[str, object], dict[str, object]]:
    digest = hashlib.sha256(archive).hexdigest()
    head_sha = source_commit
    metadata = {
        "id": 777777,
        "name": (
            f"{closeout.PRIVATE_CI_ARTIFACT_PREFIX}-{source_commit}-"
            f"{run_id}-1"
        ),
        "expired": False,
        "digest": f"sha256:{digest}",
        "size_in_bytes": len(archive),
        "workflow_run": {
            "id": int(run_id),
            "repository_id": closeout.PRIVATE_CI_REPOSITORY_ID,
            "head_repository_id": closeout.PRIVATE_CI_REPOSITORY_ID,
            "head_branch": "codex/implement-dev-02-closeout-tooling",
            "head_sha": head_sha,
        },
    }
    attempt = {
        "id": int(run_id),
        "run_attempt": 1,
        "event": "pull_request",
        "path": f"{closeout.PRIVATE_CI_WORKFLOW_PATH}@main",
        "head_branch": metadata["workflow_run"]["head_branch"],
        "head_sha": head_sha,
        "repository": {
            "id": closeout.PRIVATE_CI_REPOSITORY_ID,
            "full_name": closeout.PRIVATE_CI_REPOSITORY,
        },
        "head_repository": {
            "id": closeout.PRIVATE_CI_REPOSITORY_ID,
            "full_name": closeout.PRIVATE_CI_REPOSITORY,
        },
    }
    return metadata, attempt


def _configure_private_ci_artifact_environment(
    monkeypatch: pytest.MonkeyPatch, *, digest: str, run_id: str = "424242"
) -> None:
    environment = {
        **closeout.PRIVATE_CI_EXECUTION_RAILS,
        "ALLOW_NETWORK": "1",
        "GH_TOKEN": "github-actions-token-value",
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "pull_request",
        "GITHUB_JOB": closeout.PRIVATE_CI_JOB,
        "GITHUB_REPOSITORY": closeout.PRIVATE_CI_REPOSITORY,
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_RUN_ID": run_id,
        "GITHUB_WORKFLOW": "ci",
        closeout.PRIVATE_CI_ARTIFACT_ID_ENV: "777777",
        closeout.PRIVATE_CI_ARTIFACT_DIGEST_ENV: digest,
    }
    monkeypatch.delenv(closeout.PRIVATE_CI_ROOT_ENV, raising=False)
    for key, value in environment.items():
        monkeypatch.setenv(key, value)


def test_release_identity_binding_uses_complete_governed_family() -> None:
    row = next(
        row
        for row in closeout.validate_rows(closeout.build_rows())
        if row.token == "RELEASE_ID_RECOMPUTE_OK"
    )
    manifest_sha256, captured_release_id = (
        closeout.validate_release_identity_family()
    )
    assert row.primary_evidence == (
        "catalog/manifest.json",
        "artifacts/identity/release_id.json",
        "artifacts/identity/release_id_recompute.log",
    )
    assert row.artifact_keys == (
        "epic038.release.catalog_manifest",
        "epic038.pr01.identity_release_id",
        "epic038.pr01.identity_release_id_recompute",
    )
    assert row.proof_anchors == (
        "catalog/manifest.json.path_proof.txt",
        "artifacts/identity/release_id.json.path_proof.txt",
        "artifacts/identity/release_id_recompute.log.path_proof.txt",
    )
    assert set(row.test_binding.split("; ")) == {
        "scripts/release_id_recompute.py",
        "tools/evidence/generate_identity_provenance.py",
        "tests/evidence/test_identity_provenance.py",
        "tools/evidence/build_release_attestation.py",
        "tests/evidence/test_release_manifest_content_binding.py",
        "tests/evidence/test_release_attestation.py",
    }
    assert row.ci_binding == closeout.RELEASE_CI_JOB
    assert row.live_qa == "qa-21-po-021"
    assert f"`manifest_sha256={manifest_sha256}`" in row.future_claim
    assert f"digest `{manifest_sha256}`" in row.posture
    assert f"capture digest `{captured_release_id}`" in row.posture
    assert manifest_sha256 != captured_release_id
    assert row.posture.startswith("UNCLAIMED:")


def test_release_identity_family_rejects_incoherent_capture() -> None:
    release_bytes = (ROOT / "artifacts/identity/release_id.json").read_bytes()
    release_payload = json.loads(release_bytes)
    recompute_text = (
        ROOT / "artifacts/identity/release_id_recompute.log"
    ).read_text(encoding="utf-8")
    release_payload["release_id"] = "0" * 64
    with pytest.raises(ValueError, match="release identity JSON binding mismatch"):
        closeout.validate_release_identity_family(
            release_payload=release_payload,
            recompute_text=recompute_text,
        )

    duplicate_field_log = recompute_text.replace(
        "release_id=",
        f"release_id={'0' * 64}\nrelease_id=",
        1,
    )
    with pytest.raises(ValueError, match="recomputation log shape mismatch"):
        closeout.validate_release_identity_family(
            recompute_text=duplicate_field_log,
        )

    duplicate_key_bytes = release_bytes.replace(
        b'"release_id":',
        b'"release_id":"' + (b"0" * 64) + b'","release_id":',
        1,
    )
    assert duplicate_key_bytes != release_bytes
    with pytest.raises(ValueError, match="release identity JSON binding mismatch"):
        closeout.validate_release_identity_family(
            release_bytes=duplicate_key_bytes,
        )


def test_release_row_rejects_manifest_only_substitution() -> None:
    rows = closeout.build_rows()
    index = next(
        index
        for index, row in enumerate(rows)
        if row.token == "RELEASE_ID_RECOMPUTE_OK"
    )
    changed = replace(
        rows[index],
        primary_evidence=("catalog/manifest.json",),
        artifact_keys=("epic038.release.catalog_manifest",),
        proof_anchors=("catalog/manifest.json.path_proof.txt",),
    )
    with pytest.raises(ValueError, match="release identity source binding mismatch"):
        closeout.validate_rows(rows[:index] + (changed,) + rows[index + 1 :])


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
        (
            lambda payload: payload.__setitem__("source_tree_sha256", "bad"),
            "source_tree_sha256",
        ),
        (
            lambda payload: payload.__setitem__("validation_result", "FAIL"),
            "validation_result",
        ),
        (
            lambda payload: payload.__setitem__("release_admission", "DENIED"),
            "release_admission",
        ),
        (
            lambda payload: payload.__setitem__("pipeline_stop", "release"),
            "pipeline_stop",
        ),
        (
            lambda payload: payload["rails"].__setitem__("ALLOW_NETWORK", "1"),
            "rails",
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


def test_release_attestation_core_payload_accepts_current_closed_rails() -> None:
    source_commit = "a" * 40
    manifest_sha256 = "d" * 64
    closeout.validate_release_attestation_payload(
        _release_attestation(source_commit, manifest_sha256),
        expected_source_commit=source_commit,
        manifest_sha256=manifest_sha256,
    )


def test_private_ci_receipt_is_external_exact_and_token_agnostic(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch
    )
    outcome = closeout._private_ci_evidence()
    assert outcome.release_state == "PASS"
    assert outcome.planned_state == "PASS"
    assert receipt["command_results"] == [
        {"command": command, "exit_code": 0, "result": "PASS"}
        for command in closeout.PRIVATE_CI_COMMANDS
    ]
    assert tuple(
        item["command"] for item in receipt["command_results"]
    ) == closeout.PRIVATE_CI_COMMANDS
    serialized = (root / closeout.PRIVATE_CI_RECEIPT_NAME).read_text(
        encoding="utf-8"
    )
    assert "artifact_key" not in serialized
    assert all(token not in serialized for token in closeout.TOKENS)
    assert str(root) not in serialized


def test_synthetic_private_root_and_spoofed_actions_environment_promote_nothing(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _root, _receipt, _attestation = _configure_private_ci_evidence(
        tmp_path,
        monkeypatch,
        authenticate_receipt=False,
    )
    environment = {
        **closeout.PRIVATE_CI_EXECUTION_RAILS,
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "pull_request",
        "GITHUB_JOB": closeout.PRIVATE_CI_JOB,
        "GITHUB_REPOSITORY": closeout.PRIVATE_CI_REPOSITORY,
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_RUN_ID": "424242",
        "GITHUB_WORKFLOW": "ci",
    }
    for key, value in environment.items():
        monkeypatch.setenv(key, value)
    outcome = closeout._private_ci_evidence()
    assert outcome.release_state == "FAIL"
    assert outcome.planned_state == "FAIL"


def test_authenticated_private_artifact_binds_server_run_and_archive(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, _receipt, _attestation = _configure_private_ci_evidence(
        tmp_path,
        monkeypatch,
        authenticate_receipt=False,
    )
    source_commit = "a" * 40
    archive = _private_ci_archive(root)
    digest = hashlib.sha256(archive).hexdigest()
    metadata, attempt = _private_ci_api_payloads(
        source_commit=source_commit,
        archive=archive,
    )
    _configure_private_ci_artifact_environment(monkeypatch, digest=digest)
    monkeypatch.setattr(closeout, "_current_source_commit", lambda: source_commit)

    def api_bytes(
        endpoint: str, *, accept: str, limit: int, allow_redirect: bool
    ) -> bytes:
        assert accept == "application/vnd.github+json"
        assert limit > 0
        if endpoint.endswith("/zip"):
            assert allow_redirect is True
            return archive
        assert allow_redirect is False
        if "/attempts/" in endpoint:
            return json.dumps(attempt, separators=(",", ":")).encode()
        return json.dumps(metadata, separators=(",", ":")).encode()

    monkeypatch.setattr(closeout, "_github_api_bytes", api_bytes)
    files = closeout._authenticated_private_ci_files()
    assert files[closeout.PRIVATE_CI_RECEIPT_NAME] == (
        root / closeout.PRIVATE_CI_RECEIPT_NAME
    ).read_bytes()
    assert closeout._private_ci_evidence().planned_state == "PASS"


@pytest.mark.parametrize(
    "case",
    [
        "artifact-id",
        "artifact-name",
        "expired",
        "server-digest",
        "server-size",
        "artifact-run",
        "artifact-repository",
        "artifact-head-repository",
        "attempt-number",
        "attempt-event",
        "attempt-workflow",
        "attempt-repository",
        "attempt-head",
        "receipt-run",
        "receipt-attempt",
        "receipt-event",
        "archive-bytes",
    ],
)
def test_authenticated_private_artifact_rejects_provenance_or_archive_tamper(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    case: str,
) -> None:
    root, receipt, _attestation = _configure_private_ci_evidence(
        tmp_path,
        monkeypatch,
        authenticate_receipt=False,
    )
    source_commit = "a" * 40
    if case == "receipt-run":
        receipt["run_id"] = "424243"
    elif case == "receipt-attempt":
        receipt["run_attempt"] = "2"
    elif case == "receipt-event":
        receipt["event_name"] = "push"
    if case.startswith("receipt-"):
        (root / closeout.PRIVATE_CI_RECEIPT_NAME).write_bytes(
            closeout._canonical_json(receipt)
        )
    archive = _private_ci_archive(root)
    digest = hashlib.sha256(archive).hexdigest()
    metadata, attempt = _private_ci_api_payloads(
        source_commit=source_commit,
        archive=archive,
    )
    if case == "artifact-id":
        metadata["id"] = 888888
    elif case == "artifact-name":
        metadata["name"] = "synthetic-receipt"
    elif case == "expired":
        metadata["expired"] = True
    elif case == "server-digest":
        metadata["digest"] = f"sha256:{'e' * 64}"
    elif case == "server-size":
        metadata["size_in_bytes"] = len(archive) + 1
    elif case == "artifact-run":
        metadata["workflow_run"]["id"] = 424243
    elif case == "artifact-repository":
        metadata["workflow_run"]["repository_id"] = 1
    elif case == "artifact-head-repository":
        metadata["workflow_run"]["head_repository_id"] = 1
    elif case == "attempt-number":
        attempt["run_attempt"] = 2
    elif case == "attempt-event":
        attempt["event"] = "push"
    elif case == "attempt-workflow":
        attempt["path"] = ".github/workflows/other.yml"
    elif case == "attempt-repository":
        attempt["repository"]["id"] = 1
    elif case == "attempt-head":
        attempt["head_sha"] = "c" * 40
    elif case == "archive-bytes":
        archive += b"tamper"
    _configure_private_ci_artifact_environment(monkeypatch, digest=digest)
    monkeypatch.setattr(closeout, "_current_source_commit", lambda: source_commit)

    def api_bytes(
        endpoint: str, *, accept: str, limit: int, allow_redirect: bool
    ) -> bytes:
        if endpoint.endswith("/zip"):
            return archive
        if "/attempts/" in endpoint:
            return json.dumps(attempt, separators=(",", ":")).encode()
        return json.dumps(metadata, separators=(",", ":")).encode()

    monkeypatch.setattr(closeout, "_github_api_bytes", api_bytes)
    with pytest.raises(ValueError):
        closeout._authenticated_private_ci_files()


@pytest.mark.parametrize(
    ("name", "mode"),
    [
        ("../execution-receipt.json", None),
        ("/execution-receipt.json", None),
        ("release-attestation\\attestation.json", None),
        ("unexpected.json", None),
        ("linked-receipt.json", stat.S_IFLNK | 0o777),
    ],
)
def test_private_ci_artifact_archive_rejects_unsafe_or_extra_members(
    tmp_path: Path,
    name: str,
    mode: int | None,
) -> None:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(closeout.PRIVATE_CI_RECEIPT_NAME, b"{}\n")
        archive.writestr(
            f"{closeout.PRIVATE_CI_ATTESTATION_DIR}/attestation.json",
            b"{}\n",
        )
        info = zipfile.ZipInfo(name)
        if mode is not None:
            info.create_system = 3
            info.external_attr = mode << 16
        archive.writestr(info, b"unsafe\n")
    with pytest.raises(ValueError):
        closeout._private_ci_archive_files(stream.getvalue())


def test_private_ci_artifact_archive_accepts_bounded_production_shape() -> None:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(closeout.PRIVATE_CI_RECEIPT_NAME, b"{}\n")
        archive.writestr(
            f"{closeout.PRIVATE_CI_ATTESTATION_DIR}/attestation.json",
            b"{}\n",
        )
        for index in range(184):
            archive.writestr(
                f"{closeout.PRIVATE_CI_ATTESTATION_DIR}/evidence/{index:03d}.txt",
                b"bounded\n",
            )
    files = closeout._private_ci_archive_files(stream.getvalue())
    assert len(files) == 186


def test_private_ci_artifact_archive_rejects_entry_count_above_bound() -> None:
    stream = io.BytesIO()
    with zipfile.ZipFile(stream, mode="w", compression=zipfile.ZIP_DEFLATED) as archive:
        for index in range(closeout.PRIVATE_CI_ARCHIVE_ENTRY_LIMIT + 1):
            archive.writestr(
                f"{closeout.PRIVATE_CI_ATTESTATION_DIR}/evidence/{index:03d}.txt",
                b"bounded\n",
            )
    with pytest.raises(ValueError, match="inventory is invalid"):
        closeout._private_ci_archive_files(stream.getvalue())


def test_private_github_api_requires_nonforwarded_step_scoped_credential(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.delenv("GH_TOKEN", raising=False)
    with pytest.raises(ValueError, match="credential is unavailable"):
        closeout._github_api_bytes(
            f"/repos/{closeout.PRIVATE_CI_REPOSITORY}/actions/artifacts/777777",
            accept="application/vnd.github+json",
            limit=1024,
            allow_redirect=False,
        )


def test_private_ci_attestation_without_execution_receipt_promotes_no_token(
    dev02_fixed_repo: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _configure_private_ci_evidence(
        tmp_path, monkeypatch, include_receipt=False
    )
    outcome = closeout._private_ci_evidence()
    assert outcome.release_state == "ATTESTED"
    assert outcome.planned_state == "ABSENT"
    snapshot = closeout.evaluate_closeout()
    affected = {
        *closeout.PLANNED_BINDINGS,
        "RELEASE_ID_RECOMPUTE_OK",
    }
    assert {
        result.status
        for result in snapshot.token_results
        if result.token in affected
    } == {"UNCLAIMED"}
    package = closeout.build_package(evaluation_snapshot=snapshot)
    assert json.loads(package[closeout.CLOSE_MANIFEST_PATH])["decision"] == (
        "NOT SATISFIED"
    )


def test_private_ci_attestation_must_match_exact_head_tree_digest(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, receipt, attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch
    )
    attestation["source_tree_sha256"] = "b" * 64
    attestation_bytes = closeout._canonical_json(attestation)
    (
        root
        / closeout.PRIVATE_CI_ATTESTATION_DIR
        / "attestation.json"
    ).write_bytes(attestation_bytes)
    receipt["source_tree_sha256"] = "b" * 64
    receipt["release_attestation_sha256"] = hashlib.sha256(
        attestation_bytes
    ).hexdigest()
    (root / closeout.PRIVATE_CI_RECEIPT_NAME).write_bytes(
        closeout._canonical_json(receipt)
    )
    outcome = closeout._private_ci_evidence()
    assert outcome.release_state == "FAIL"
    assert outcome.planned_state == "FAIL"


def test_exact_head_tree_digest_ignores_dirty_worktree_bytes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository = tmp_path / "source"
    repository.mkdir()
    (repository / "alpha.txt").write_bytes(b"alpha\n")
    (repository / "nested").mkdir()
    (repository / "nested/beta.txt").write_bytes(b"beta\n")
    subprocess.run(["git", "init", "-q", str(repository)], check=True)
    subprocess.run(["git", "-C", str(repository), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "-c",
            "user.name=Receipt Test",
            "-c",
            "user.email=receipt@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    rows = [
        {
            "path": path,
            "sha256": hashlib.sha256(body).hexdigest(),
            "size": len(body),
        }
        for path, body in (
            ("alpha.txt", b"alpha\n"),
            ("nested/beta.txt", b"beta\n"),
        )
    ]
    expected = hashlib.sha256(closeout._canonical_json(rows)).hexdigest()
    monkeypatch.setattr(closeout, "ROOT", repository)
    assert closeout._current_source_tree_sha256() == expected
    (repository / "alpha.txt").write_bytes(b"dirty\n")
    assert closeout._current_source_tree_sha256() == expected


def test_private_source_worktree_rejects_unrelated_drift_and_only_allows_outputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository = tmp_path / "source"
    repository.mkdir()
    (repository / "alpha.txt").write_bytes(b"alpha\n")
    subprocess.run(["git", "init", "-q", str(repository)], check=True)
    subprocess.run(["git", "-C", str(repository), "add", "."], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(repository),
            "-c",
            "user.name=Receipt Test",
            "-c",
            "user.email=receipt@example.invalid",
            "commit",
            "-qm",
            "fixture",
        ],
        check=True,
    )
    monkeypatch.setattr(closeout, "ROOT", repository)
    closeout._validate_private_source_worktree(allow_generated=False)

    (repository / "alpha.txt").write_bytes(b"dirty\n")
    with pytest.raises(ValueError, match="unrelated tracked or untracked drift"):
        closeout._validate_private_source_worktree(allow_generated=True)

    (repository / "alpha.txt").write_bytes(b"alpha\n")
    generated = repository / closeout.CLOSE_REPORT_PATH
    generated.parent.mkdir(parents=True)
    generated.write_bytes(b"generated\n")
    closeout._validate_private_source_worktree(allow_generated=True)
    with pytest.raises(ValueError, match="unrelated tracked or untracked drift"):
        closeout._validate_private_source_worktree(allow_generated=False)


@pytest.mark.parametrize(
    "mutation",
    [
        pytest.param(
            lambda payload: payload["command_results"].pop(),
            id="missing-command",
        ),
        pytest.param(
            lambda payload: payload["command_results"].reverse(),
            id="reordered-commands",
        ),
        pytest.param(
            lambda payload: payload["command_results"].append(
                dict(payload["command_results"][-1])
            ),
            id="duplicated-command",
        ),
        pytest.param(
            lambda payload: payload["command_results"][0].__setitem__(
                "command", "python -m pytest"
            ),
            id="substituted-command",
        ),
        pytest.param(
            lambda payload: payload["command_results"][2].__setitem__(
                "exit_code", 1
            ),
            id="nonzero-exit",
        ),
        pytest.param(
            lambda payload: payload["closed_rails"].__setitem__(
                "ALLOW_NETWORK", "1"
            ),
            id="opened-rails",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("source_commit", "b" * 40),
            id="stale-head",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("manifest_sha256", "b" * 64),
            id="wrong-manifest",
        ),
        pytest.param(
            lambda payload: payload.__setitem__(
                "release_attestation_sha256", "b" * 64
            ),
            id="wrong-attestation-digest",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("source_tree_sha256", "b" * 64),
            id="wrong-source-tree",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("repository", "someone/else"),
            id="wrong-repository",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("workflow_path", "other.yml"),
            id="wrong-workflow",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("job", "other"),
            id="wrong-job",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("event_name", "workflow_dispatch"),
            id="wrong-event",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("run_id", "0"),
            id="invalid-run",
        ),
        pytest.param(
            lambda payload: payload.__setitem__("unexpected", True),
            id="extra-field",
        ),
    ],
)
def test_private_ci_receipt_tamper_blocks_every_affected_token(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation: Callable[[dict[str, object]], None],
) -> None:
    root, receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch
    )
    mutation(receipt)
    (root / closeout.PRIVATE_CI_RECEIPT_NAME).write_bytes(
        closeout._canonical_json(receipt)
    )
    outcome = closeout._private_ci_evidence()
    assert outcome.release_state == "FAIL"
    assert outcome.planned_state == "FAIL"


@pytest.mark.parametrize("encoding", ["pretty", "duplicate-key", "symlink"])
def test_private_ci_receipt_rejects_noncanonical_or_aliased_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    encoding: str,
) -> None:
    root, receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch
    )
    path = root / closeout.PRIVATE_CI_RECEIPT_NAME
    if encoding == "pretty":
        path.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    elif encoding == "duplicate-key":
        raw = closeout._canonical_json(receipt)
        path.write_bytes(raw.replace(b"{", b'{"contract":"duplicate",', 1))
    else:
        target = tmp_path / "aliased-receipt.json"
        target.write_bytes(closeout._canonical_json(receipt))
        path.unlink()
        path.symlink_to(target)
    outcome = closeout._private_ci_evidence()
    assert outcome.release_state == "FAIL"
    assert outcome.planned_state == "FAIL"


def test_private_ci_root_must_be_absolute_external_and_nonaliased(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repository = tmp_path / "repository"
    repository.mkdir()
    inside = repository / "receipt"
    (inside / closeout.PRIVATE_CI_ATTESTATION_DIR).mkdir(parents=True)
    monkeypatch.setattr(closeout, "ROOT", repository)
    with pytest.raises(ValueError, match="external"):
        closeout._private_ci_root(str(inside))
    with pytest.raises(ValueError, match="absolute"):
        closeout._private_ci_root("relative/receipt")

    external = tmp_path / "external"
    (external / closeout.PRIVATE_CI_ATTESTATION_DIR).mkdir(parents=True)
    alias = tmp_path / "alias"
    alias.symlink_to(external, target_is_directory=True)
    with pytest.raises(ValueError, match="non-symlink"):
        closeout._private_ci_root(str(alias))


def test_private_ci_writer_requires_github_test_job_and_writes_mode_0600(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    root, _receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch, include_receipt=False
    )
    environment = {
        **closeout.PRIVATE_CI_EXECUTION_RAILS,
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "pull_request",
        "GITHUB_JOB": closeout.PRIVATE_CI_JOB,
        "GITHUB_REPOSITORY": closeout.PRIVATE_CI_REPOSITORY,
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_RUN_ID": "424242",
        "GITHUB_WORKFLOW": "ci",
    }
    for key, value in environment.items():
        monkeypatch.setenv(key, value)
    written = closeout._write_private_ci_receipt()
    assert written == root / closeout.PRIVATE_CI_RECEIPT_NAME
    assert written.stat().st_mode & 0o077 == 0
    assert closeout._private_ci_evidence().planned_state == "FAIL"
    monkeypatch.delenv(closeout.PRIVATE_CI_ROOT_ENV)
    monkeypatch.setenv(closeout.PRIVATE_CI_ARTIFACT_ID_ENV, "777777")
    monkeypatch.setenv(closeout.PRIVATE_CI_ARTIFACT_DIGEST_ENV, "d" * 64)
    monkeypatch.setattr(
        closeout,
        "_authenticated_private_ci_files",
        lambda: {
            path.relative_to(root).as_posix(): path.read_bytes()
            for path in sorted(root.rglob("*"))
            if path.is_file()
        },
    )
    assert closeout._private_ci_evidence().planned_state == "PASS"
    monkeypatch.delenv(closeout.PRIVATE_CI_ARTIFACT_ID_ENV)
    monkeypatch.delenv(closeout.PRIVATE_CI_ARTIFACT_DIGEST_ENV)
    monkeypatch.setenv(closeout.PRIVATE_CI_ROOT_ENV, str(root))
    with pytest.raises(ValueError, match="empty receipt destination"):
        closeout._write_private_ci_receipt()


@pytest.mark.parametrize("rail", sorted(closeout.PRIVATE_CI_EXECUTION_RAILS))
def test_private_ci_writer_rejects_open_or_missing_execution_rail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    rail: str,
) -> None:
    root, _receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch, include_receipt=False
    )
    environment = {
        **closeout.PRIVATE_CI_EXECUTION_RAILS,
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "pull_request",
        "GITHUB_JOB": closeout.PRIVATE_CI_JOB,
        "GITHUB_REPOSITORY": closeout.PRIVATE_CI_REPOSITORY,
        "GITHUB_RUN_ATTEMPT": "1",
        "GITHUB_RUN_ID": "424242",
        "GITHUB_WORKFLOW": "ci",
    }
    for key, value in environment.items():
        monkeypatch.setenv(key, value)
    monkeypatch.delenv(rail)
    with pytest.raises(ValueError, match="producer rails mismatch"):
        closeout._write_private_ci_receipt()
    assert not (root / closeout.PRIVATE_CI_RECEIPT_NAME).exists()


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


def test_doc_delta_cli_check_mode_is_read_only_for_pair_history_and_ledgers() -> None:
    watched = [
        ROOT / closeout.DOC_DELTA_PRIMARY_PATH,
        ROOT / closeout.DOC_DELTA_CAPTURE_PATH,
        ROOT / closeout.DOC_DELTA_HISTORICAL_LOG_PATH,
        ROOT / closeout.QA_MANIFEST_PATH,
        ROOT / closeout.HUMAN_INDEX_PATH,
        ROOT / closeout.MACHINE_MIRROR_PATH,
    ]
    before = {
        path: (hashlib.sha256(path.read_bytes()).digest(), path.stat().st_mtime_ns)
        for path in watched
    }
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/evidence/generate_hde_epic038_closeout.py"),
            "--check-doc-deltas",
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "DOC_DELTA_PAIR_OK" in result.stdout
    assert before == {
        path: (hashlib.sha256(path.read_bytes()).digest(), path.stat().st_mtime_ns)
        for path in watched
    }


@pytest.mark.parametrize(
    "abbreviation",
    ("--doc", "--doc-d", "--check-doc", "--token", "--check-token"),
)
def test_doc_delta_cli_rejects_abbreviated_modes_without_writes(
    abbreviation: str,
) -> None:
    watched = [
        ROOT / closeout.OUTPUT,
        ROOT / closeout.DOC_DELTA_PRIMARY_PATH,
        ROOT / closeout.DOC_DELTA_CAPTURE_PATH,
        ROOT / closeout.DOC_DELTA_HISTORICAL_LOG_PATH,
    ]
    before = {
        path: (hashlib.sha256(path.read_bytes()).digest(), path.stat().st_mtime_ns)
        for path in watched
    }
    result = subprocess.run(
        [
            sys.executable,
            str(ROOT / "tools/evidence/generate_hde_epic038_closeout.py"),
            abbreviation,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2, result.stdout + result.stderr
    assert "WROTE" not in result.stdout
    assert before == {
        path: (hashlib.sha256(path.read_bytes()).digest(), path.stat().st_mtime_ns)
        for path in watched
    }


DEV02_ENV = {
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "PYTHONDONTWRITEBYTECODE": "1",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
DEV02_COPY_IGNORES = shutil.ignore_patterns(
    ".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__"
)


def _clone_repo(source: Path, target: Path) -> Path:
    shutil.copytree(
        source,
        target,
        # Canonical producers may update an existing file in place. Real copies
        # are required here: hard links would let an isolated DEV-03 simulation
        # mutate the source checkout through the shared inode.
        copy_function=shutil.copy2,
        ignore=DEV02_COPY_IGNORES,
    )
    return target


def _run_repo_tool(root: Path, relative_tool: str, *arguments: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(DEV02_ENV)
    return subprocess.run(
        [sys.executable, str(root / relative_tool), *arguments],
        cwd=root,
        env=env,
        capture_output=True,
        text=True,
    )


def _assert_success(result: subprocess.CompletedProcess[str]) -> None:
    assert result.returncode == 0, result.stdout + result.stderr


def _replace_bytes(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.unlink(missing_ok=True)
    path.write_bytes(data)


def _replace_json(path: Path, payload: object) -> None:
    _replace_bytes(path, closeout._canonical_json(payload))


def _package_at(root: Path) -> dict[str, bytes]:
    return {relative: (root / relative).read_bytes() for relative in closeout.PACKAGE_PATHS}


def _mutate_package_json(
    package: Mapping[str, bytes],
    relative: str,
    mutation: Callable[[dict[str, object]], None],
) -> dict[str, bytes]:
    changed = dict(package)
    payload = json.loads(changed[relative], object_pairs_hook=closeout._unique_json_object)
    assert isinstance(payload, dict)
    mutation(payload)
    changed[relative] = closeout._canonical_json(payload)
    return changed


def _tree_state(root: Path) -> dict[str, tuple[object, ...]]:
    state: dict[str, tuple[object, ...]] = {}
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root).as_posix()
        stat_result = path.lstat()
        if path.is_symlink():
            state[relative] = (
                "symlink",
                path.readlink().as_posix(),
                stat_result.st_mode,
                stat_result.st_mtime_ns,
            )
        elif path.is_file():
            body = path.read_bytes()
            state[relative] = (
                "file",
                hashlib.sha256(body).hexdigest(),
                len(body),
                stat_result.st_mode,
                stat_result.st_mtime_ns,
            )
        elif path.is_dir():
            state[relative] = (
                "directory",
                tuple(sorted(child.name for child in path.iterdir())),
                stat_result.st_mode,
                stat_result.st_mtime_ns,
            )
    return state


@pytest.fixture(scope="session")
def dev02_source_tree(tmp_path_factory: pytest.TempPathFactory) -> Path:
    root = _clone_repo(
        ROOT, tmp_path_factory.mktemp("hde-epic038-dev02-source") / "repo"
    )
    # Keep this fixture at the DEV-02 pre-generation boundary even when the
    # exact head already contains a complete DEV-03 package.  The deletion is
    # isolated to the temporary copy; the canonical updater below removes the
    # corresponding generated companions and reconstructs the approved baseline.
    for relative in (
        *closeout.PACKAGE_ACTIVATION_PATHS,
        *(
            proof
            for _primary, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
        ),
    ):
        (root / relative).unlink(missing_ok=True)
    # Establish a complete current reused-evidence baseline through canonical
    # producers only. This prevents a stale checkout companion from turning all
    # 33 predicates into the same synthetic matrix-level failure and creating a
    # false negative fixture.
    for _ in range(2):
        _assert_success(
            _run_repo_tool(root, "tools/evidence/update_evidence_index.py")
        )
        _assert_success(_run_repo_tool(root, "tools/evidence/orientation_demo.py"))
        _assert_success(
            _run_repo_tool(root, "tools/evidence/update_evidence_index.py")
        )
    _assert_success(
        _run_repo_tool(root, "tools/evidence/update_evidence_index.py", "--check")
    )
    _assert_success(
        _run_repo_tool(root, "tools/evidence/orientation_demo.py", "--check")
    )
    return root


@pytest.fixture(scope="session")
def dev02_fixed_point_tree(
    dev02_source_tree: Path, tmp_path_factory: pytest.TempPathFactory
) -> Path:
    root = _clone_repo(
        dev02_source_tree,
        tmp_path_factory.mktemp("hde-epic038-dev02-fixed") / "repo",
    )
    # Exercise the exact approved DEV-03 producer order in the isolated tree:
    # one atomic primary-package write, updater, orientation, then the second
    # updater. No extra generator pass may silently revise the decision after
    # companion evidence appears.
    planned_proofs = tuple(
        proof for _path, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
    )
    assert not any((root / proof).exists() for proof in planned_proofs)
    _assert_success(
        _run_repo_tool(root, "tools/evidence/generate_hde_epic038_closeout.py")
    )
    assert not any((root / proof).exists() for proof in planned_proofs)
    generated_primaries = _package_at(root)
    _assert_success(_run_repo_tool(root, "tools/evidence/update_evidence_index.py"))
    assert _package_at(root) == generated_primaries
    _assert_success(_run_repo_tool(root, "tools/evidence/orientation_demo.py"))
    _assert_success(_run_repo_tool(root, "tools/evidence/update_evidence_index.py"))
    assert _package_at(root) == generated_primaries
    _assert_success(
        _run_repo_tool(
            root, "tools/evidence/generate_hde_epic038_closeout.py", "--check"
        )
    )
    _assert_success(
        _run_repo_tool(root, "tools/evidence/update_evidence_index.py", "--check")
    )
    _assert_success(
        _run_repo_tool(root, "tools/evidence/orientation_demo.py", "--check")
    )
    return root


@pytest.fixture
def dev02_repo(
    dev02_source_tree: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Path:
    root = _clone_repo(dev02_source_tree, tmp_path / "repo")
    monkeypatch.setattr(closeout, "ROOT", root)
    monkeypatch.setattr(updater, "ROOT", root)
    return root


@pytest.fixture
def dev02_fixed_repo(
    dev02_fixed_point_tree: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> Path:
    root = _clone_repo(dev02_fixed_point_tree, tmp_path / "repo")
    monkeypatch.setattr(closeout, "ROOT", root)
    monkeypatch.setattr(updater, "ROOT", root)
    return root


@pytest.fixture
def dev02_valid_package(dev02_fixed_repo: Path) -> dict[str, bytes]:
    package = _package_at(dev02_fixed_repo)
    closeout.validate_package(package)
    return package


def test_dev02_release_token_stays_unclaimed_without_current_attestation(
    dev02_repo: Path,
) -> None:
    result = _token_result(
        closeout.evaluate_closeout(), "RELEASE_ID_RECOMPUTE_OK"
    )
    assert result.status == "UNCLAIMED"
    assert "external exact-source release attestation" in result.detail
    assert "retained identity captures remain historical" in result.detail


def test_dev02_release_semantic_rejects_canonical_manifest_content_drift(
    dev02_repo: Path,
) -> None:
    manifest_path = dev02_repo / closeout.RELEASE_MANIFEST_PATH
    payload = json.loads(manifest_path.read_bytes())
    payload["files"][0]["sha256"] = "0" * 64
    _replace_json(manifest_path, payload)
    problems = closeout.manifest_only_problems(manifest_path)
    assert any("manifest_file_audit:BAD" in problem for problem in problems)
    row = next(
        row
        for row in closeout.build_rows()
        if row.token == "RELEASE_ID_RECOMPUTE_OK"
    )
    with pytest.raises(ValueError, match="manifest content validation failed"):
        closeout._semantic_release(row)
    snapshot = closeout.evaluate_closeout()
    assert _token_result(snapshot, "RELEASE_ID_RECOMPUTE_OK").status == "FAIL"
    blocker = next(
        item
        for item in snapshot.blockers
        if item["subject"]["value"] == "RELEASE_ID_RECOMPUTE_OK"
    )
    assert blocker["failure_class"] == "EVIDENCE_PRODUCER_OR_VALIDATOR_DEFECT"
    assert blocker["permitted_files"] == []


def test_dev02_updater_repairs_orientation_producer_stale_proof_before_full_validation(
    dev02_repo: Path,
) -> None:
    _assert_success(
        _run_repo_tool(
            dev02_repo, "tools/evidence/generate_hde_epic038_closeout.py"
        )
    )
    _assert_success(
        _run_repo_tool(dev02_repo, "tools/evidence/update_evidence_index.py")
    )

    orientation = dev02_repo / "audit/gates/topology/orientation_demo.txt"
    proof = dev02_repo / "audit/gates/topology/orientation_demo.txt.path_proof.txt"
    before = orientation.read_bytes()
    _assert_success(
        _run_repo_tool(dev02_repo, "tools/evidence/orientation_demo.py")
    )
    after = orientation.read_bytes()
    assert after != before
    assert closeout._proof_fields(proof)["sha256"] != hashlib.sha256(after).hexdigest()

    _assert_success(
        _run_repo_tool(dev02_repo, "tools/evidence/update_evidence_index.py")
    )
    assert closeout._proof_fields(proof)["sha256"] == hashlib.sha256(after).hexdigest()
    _assert_success(
        _run_repo_tool(
            dev02_repo, "tools/evidence/update_evidence_index.py", "--check"
        )
    )


def test_dev02_updater_rejects_structurally_invalid_package_before_mutation(
    dev02_repo: Path,
) -> None:
    _assert_success(
        _run_repo_tool(
            dev02_repo, "tools/evidence/generate_hde_epic038_closeout.py"
        )
    )
    manifest_path = dev02_repo / closeout.CLOSE_MANIFEST_PATH
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["pf09_scope"].pop()
    _replace_json(manifest_path, manifest)
    before = _tree_state(dev02_repo)

    result = _run_repo_tool(
        dev02_repo, "tools/evidence/update_evidence_index.py"
    )
    assert result.returncode != 0
    assert (
        "INVALID_EPIC038_CLOSEOUT_PACKAGE_STRUCTURE"
        in result.stdout + result.stderr
    )
    assert _tree_state(dev02_repo) == before


def test_dev02_updater_rolls_back_after_reused_semantic_primary_drift(
    dev02_repo: Path,
) -> None:
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/generate_hde_epic038_closeout.py",
        )
    )
    assert all(
        (dev02_repo / path).is_file()
        for path in closeout.PACKAGE_ACTIVATION_PATHS
    )
    closeout_proofs = {
        proof for _primary, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
    }
    assert not any((dev02_repo / proof).exists() for proof in closeout_proofs)
    closeout_keys = set(closeout.CLOSEOUT_PRIMARY_BINDINGS)
    assert not closeout_keys & {
        str(item.get("artifact_key")) for item in closeout._human_items()
    }
    assert not closeout_keys & {
        str(item.get("artifact_key")) for item in closeout._mirror_items()
    }

    reused_path = "audit/qa/hde-epic038/qa_step_logs_manifest.json"
    assert reused_path not in closeout.PACKAGE_PATHS
    assert reused_path in {
        path
        for row in closeout.build_rows()
        for path in row.primary_evidence
    }
    target = dev02_repo / reused_path
    payload = json.loads(target.read_bytes())
    record = payload["qa-00-step-0-discovery"]
    assert record["status"] == "PASS"
    record["status"] = "FAIL"
    _replace_json(target, payload)
    before = _tree_state(dev02_repo)

    result = _run_repo_tool(
        dev02_repo,
        "tools/evidence/update_evidence_index.py",
    )
    assert result.returncode != 0
    assert "INVALID_EPIC038_CLOSEOUT_PACKAGE" in result.stdout + result.stderr
    assert _tree_state(dev02_repo) == before
    assert not any((dev02_repo / proof).exists() for proof in closeout_proofs)
    assert not closeout_keys & {
        str(item.get("artifact_key")) for item in closeout._human_items()
    }
    assert not closeout_keys & {
        str(item.get("artifact_key")) for item in closeout._mirror_items()
    }


def test_dev02_updater_rejects_parent_traversal_before_transaction(
    dev02_repo: Path,
) -> None:
    external = dev02_repo.parent / "transaction-scope-probe.json"
    external.write_bytes(b'{"sentinel":"unchanged"}\n')
    external_mode = external.stat().st_mode
    external_mtime_ns = external.stat().st_mtime_ns
    external_proof = external.with_name(f"{external.name}.path_proof.txt")
    assert not external_proof.exists()

    index_path = dev02_repo / "docs/evidence/INDEX.json"
    index = json.loads(index_path.read_bytes())
    index.append(
        {
            "artifact_key": "transaction.scope.probe",
            "discovered_physical_path": "../transaction-scope-probe.json",
            "record_type": "audit",
            "schema_version": "1.0",
        }
    )
    _replace_json(index_path, index)
    before = _tree_state(dev02_repo)

    result = _run_repo_tool(
        dev02_repo,
        "tools/evidence/update_evidence_index.py",
    )
    assert result.returncode != 0
    assert "Invalid discovered_physical_path" in result.stdout + result.stderr
    assert _tree_state(dev02_repo) == before
    assert external.read_bytes() == b'{"sentinel":"unchanged"}\n'
    assert external.stat().st_mode == external_mode
    assert external.stat().st_mtime_ns == external_mtime_ns
    assert not external_proof.exists()


def _token_result(snapshot: object, token: str) -> object:
    matches = [result for result in snapshot.token_results if result.token == token]
    assert len(matches) == 1
    return matches[0]


def _snapshot_text(snapshot: object) -> str:
    return json.dumps(
        {
            "blockers": list(snapshot.blockers),
            "obligations": list(snapshot.obligations),
            "proof_families": list(snapshot.proof_families),
            "token_results": [result.as_dict() for result in snapshot.token_results],
        },
        default=str,
        sort_keys=True,
    )


def test_dev02_complete_registered_fixture_remains_truthfully_nonclaiming(
    dev02_fixed_repo: Path,
) -> None:
    snapshot = closeout.evaluate_closeout()
    assert tuple(result.token for result in snapshot.token_results) == closeout.TOKENS
    pending = {
        result.token
        for result in snapshot.token_results
        if result.status == "UNCLAIMED"
    }
    assert pending == {
        *closeout.PLANNED_BINDINGS,
        "RELEASE_ID_RECOMPUTE_OK",
    }
    assert all(
        result.status == "PASS"
        for result in snapshot.token_results
        if result.token not in pending
    )
    assert not snapshot.blockers
    assert len(snapshot.proof_families) == sum(
        len(row.primary_evidence) for row in closeout.build_rows()
    )
    accounting = _snapshot_text(snapshot)
    for required in (
        *closeout.PF09_SCOPE,
        *closeout.PF09_EXCLUSIONS,
        *closeout.TRACKED_ISSUES,
        *(record["label"] for record in closeout.ADR_RECORDS),
        closeout.QA_RCA_PATH,
    ):
        assert str(required) in accounting
    assert len(snapshot.fingerprint) == 64
    int(snapshot.fingerprint, 16)

    first = closeout.build_package()
    second = closeout.build_package()
    assert first == second == _package_at(dev02_fixed_repo)
    manifest = json.loads(first[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "NOT SATISFIED"
    assert manifest["minimum_follow_up"]
    assert isinstance(manifest["key_outputs"], dict)
    assert tuple(manifest["token_roster"]) == closeout.TOKENS


def test_private_receipt_promotes_only_four_tokens_and_reaches_stable_satisfied(
    dev02_fixed_repo: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    baseline = closeout.evaluate_closeout()
    baseline_by_token = {item.token: item for item in baseline.token_results}
    assert {
        token
        for token, result in baseline_by_token.items()
        if result.status == "UNCLAIMED"
    } == {*closeout.PLANNED_BINDINGS, "RELEASE_ID_RECOMPUTE_OK"}

    root, receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch, run_id="424242"
    )
    admitted = closeout.evaluate_closeout()
    admitted_by_token = {item.token: item for item in admitted.token_results}
    changed = {
        token
        for token in closeout.TOKENS
        if admitted_by_token[token].status != baseline_by_token[token].status
    }
    assert changed == {
        *closeout.PLANNED_BINDINGS,
        "RELEASE_ID_RECOMPUTE_OK",
    }
    assert all(item.status == "PASS" for item in admitted.token_results)
    assert not admitted.blockers

    first = closeout.build_package(evaluation_snapshot=admitted)
    closeout.validate_package(first)
    manifest = json.loads(first[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "SATISFIED"
    assert not manifest["minimum_follow_up"]
    assert set(manifest["token_status"].values()) == {"PASS"}
    assert {
        json.loads(first[path])["result"]
        for path in (
            closeout.PRECOMMIT_CHECKLIST_PATH,
            closeout.POSTCOMMIT_CHECKLIST_PATH,
        )
    } == {"PASS"}

    receipt["run_id"] = "434343"
    (root / closeout.PRIVATE_CI_RECEIPT_NAME).write_bytes(
        closeout._canonical_json(receipt)
    )
    second = closeout.build_package()
    assert second == first
    combined = b"".join(first[path] for path in closeout.PACKAGE_PATHS)
    assert b"424242" not in combined
    assert b"434343" not in combined
    assert str(root).encode("utf-8") not in combined


def test_invalid_private_receipt_keeps_package_not_satisfied(
    dev02_fixed_repo: Path,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    root, receipt, _attestation = _configure_private_ci_evidence(
        tmp_path, monkeypatch
    )
    receipt["command_results"][0]["exit_code"] = 1
    (root / closeout.PRIVATE_CI_RECEIPT_NAME).write_bytes(
        closeout._canonical_json(receipt)
    )
    snapshot = closeout.evaluate_closeout()
    results = {item.token: item for item in snapshot.token_results}
    assert results["RELEASE_ID_RECOMPUTE_OK"].status == "FAIL"
    assert {
        results[token].status for token in closeout.PLANNED_BINDINGS
    } == {"FAIL"}
    assert all(
        results[token].status == "PASS"
        for token in closeout.TOKENS
        if token not in {*closeout.PLANNED_BINDINGS, "RELEASE_ID_RECOMPUTE_OK"}
    )
    package = closeout.build_package(evaluation_snapshot=snapshot)
    closeout.validate_package(package)
    manifest = json.loads(package[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "NOT SATISFIED"
    assert manifest["minimum_follow_up"]


def _private_projection(state: str) -> closeout._PrivateCiEvidence:
    if state == "ABSENT":
        return closeout._PrivateCiEvidence(
            "ABSENT",
            "no private external exact-source release attestation was supplied",
            "ABSENT",
            "no private external exact-command CI receipt was supplied",
        )
    if state == "FAIL":
        return closeout._PrivateCiEvidence(
            "FAIL",
            closeout.PRIVATE_CI_INVALID_DETAIL,
            "FAIL",
            closeout.PRIVATE_CI_INVALID_DETAIL,
        )
    if state == "PASS":
        return closeout._PrivateCiEvidence(
            "PASS",
            closeout.PRIVATE_CI_ATTESTATION_PASS_DETAIL,
            "PASS",
            closeout.PRIVATE_CI_RECEIPT_PASS_DETAIL,
        )
    raise AssertionError(state)


def _package_for_private_projection(
    private_evidence: closeout._PrivateCiEvidence,
) -> dict[str, bytes]:
    snapshot = closeout._evaluate_closeout(private_evidence)
    ledger = closeout.record_blockers(
        closeout._load_ledger(), [dict(item) for item in snapshot.blockers]
    )
    return closeout._construct_package(snapshot, ledger)


def test_canonical_updater_accepts_receipt_satisfied_projection_without_receipt(
    dev02_fixed_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    package = _package_for_private_projection(_private_projection("PASS"))
    assert json.loads(package[closeout.CLOSE_MANIFEST_PATH])["decision"] == "SATISFIED"
    closeout._validate_package_for_canonical_updater(package)
    for relative, body in package.items():
        _replace_bytes(dev02_fixed_repo / relative, body)
    primaries = _package_at(dev02_fixed_repo)

    _assert_success(
        _run_repo_tool(dev02_fixed_repo, "tools/evidence/update_evidence_index.py")
    )
    assert _package_at(dev02_fixed_repo) == primaries
    _assert_success(
        _run_repo_tool(dev02_fixed_repo, "tools/evidence/orientation_demo.py")
    )
    _assert_success(
        _run_repo_tool(dev02_fixed_repo, "tools/evidence/update_evidence_index.py")
    )
    assert _package_at(dev02_fixed_repo) == primaries
    _assert_success(
        _run_repo_tool(
            dev02_fixed_repo,
            "tools/evidence/update_evidence_index.py",
            "--check",
        )
    )
    monkeypatch.setattr(
        closeout,
        "_private_ci_evidence",
        lambda: _private_projection("PASS"),
    )
    closeout.validate_package(_package_at(dev02_fixed_repo))


def test_canonical_updater_rejects_mixed_external_gate_projection(
    dev02_fixed_repo: Path,
) -> None:
    absent = closeout._evaluate_closeout(_private_projection("ABSENT"))
    admitted = closeout._evaluate_closeout(_private_projection("PASS"))
    admitted_by_token = {item.token: item for item in admitted.token_results}
    mixed_results = tuple(
        admitted_by_token[item.token]
        if item.token == "RELEASE_ID_RECOMPUTE_OK"
        else item
        for item in absent.token_results
    )
    mixed = closeout._make_snapshot(
        mixed_results,
        absent.proof_families,
        (),
        absent.obligations,
    )
    package = closeout._construct_package(mixed, closeout._load_ledger())
    closeout.validate_package_structure(package)
    with pytest.raises(ValueError, match="complete canonical external-gate projection"):
        closeout._validate_package_for_canonical_updater(package)


def test_canonical_updater_recomputes_ungated_predicates_under_satisfied_projection(
    dev02_fixed_repo: Path,
) -> None:
    package = _package_for_private_projection(_private_projection("PASS"))
    source = dev02_fixed_repo / closeout.DOC_DELTA_PRIMARY_PATH
    source.write_bytes(source.read_bytes() + b"drift\n")
    before = _tree_state(dev02_fixed_repo)
    with pytest.raises(ValueError, match="complete canonical external-gate projection"):
        closeout._validate_package_for_canonical_updater(package)
    assert _tree_state(dev02_fixed_repo) == before


def test_canonical_updater_accepts_complete_invalid_external_gate_projection(
    dev02_fixed_repo: Path,
) -> None:
    package = _package_for_private_projection(_private_projection("FAIL"))
    manifest = json.loads(package[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "NOT SATISFIED"
    assert {
        manifest["token_status"][token]
        for token in {
            *closeout.PLANNED_BINDINGS,
            "RELEASE_ID_RECOMPUTE_OK",
        }
    } == {"FAIL"}
    closeout._validate_package_for_canonical_updater(package)


def test_dev02_legacy_empty_blocker_override_is_not_an_api() -> None:
    with pytest.raises(TypeError):
        closeout.build_package([], closeout._empty_ledger())


def test_dev02_empty_or_unevaluated_snapshot_cannot_force_satisfied(
    dev02_fixed_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    empty = closeout.EvaluationSnapshot((), (), (), (), "0" * 64)
    with pytest.raises(ValueError, match="snapshot|token|evaluation|roster"):
        closeout.build_package(evaluation_snapshot=empty)

    monkeypatch.setattr(closeout, "evaluate_closeout", lambda: empty)
    with pytest.raises(ValueError, match="snapshot|token|evaluation|roster"):
        closeout.build_package()


def test_dev02_pre_generation_source_stays_unclaimed_in_provisional_candidate(
    dev02_repo: Path,
) -> None:
    snapshot = closeout.evaluate_closeout()
    planned = {
        result.token: result
        for result in snapshot.token_results
        if result.token in closeout.PLANNED_BINDINGS
    }
    reused = {
        result.token: result
        for result in snapshot.token_results
        if result.token not in closeout.PLANNED_BINDINGS
    }
    assert planned
    assert reused
    assert not snapshot.blockers
    assert reused["RELEASE_ID_RECOMPUTE_OK"].status == "UNCLAIMED"
    assert all(
        result.status == "PASS"
        for token, result in reused.items()
        if token != "RELEASE_ID_RECOMPUTE_OK"
    )
    assert all(result.status == "UNCLAIMED" for result in planned.values())
    package = closeout.build_package(evaluation_snapshot=snapshot)
    manifest = json.loads(package[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "NOT SATISFIED"
    assert all(
        manifest["source_token_status"][token] == "UNCLAIMED" for token in planned
    )
    assert all(manifest["token_status"][token] == "UNCLAIMED" for token in planned)
    assert manifest["token_status"]["RELEASE_ID_RECOMPUTE_OK"] == "UNCLAIMED"
    assert manifest["minimum_follow_up"]
    assert {
        json.loads(package[path])["result"]
        for path in (
            closeout.PRECOMMIT_CHECKLIST_PATH,
            closeout.POSTCOMMIT_CHECKLIST_PATH,
        )
    } == {"FAIL"}
    report = package[closeout.CLOSE_REPORT_PATH].decode("utf-8")
    assert "Source-tree planned tokens remain UNCLAIMED" in report


@pytest.mark.parametrize("token", tuple(closeout.PLANNED_BINDINGS))
def test_dev02_pass_shaped_planned_primary_without_execution_receipt_is_unclaimed(
    token: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    row = next(row for row in closeout.build_rows() if row.token == token)
    monkeypatch.setattr(closeout, "_validate_row_bindings", lambda _row: None)
    monkeypatch.setattr(closeout, "_checklist_payload_result", lambda _row: "PASS")
    evaluators = dict(closeout.TOKEN_EVALUATOR_REGISTRY)
    evaluators[token] = lambda _row: "PASS-shaped primary semantics validate"
    monkeypatch.setattr(closeout, "TOKEN_EVALUATOR_REGISTRY", evaluators)

    result = closeout._planned_result(
        row,
        ("REGISTERED", "complete primary and companion family validates"),
    )

    assert result.status == "UNCLAIMED"
    assert "do not prove" in result.detail
    assert "execution evidence" in result.minimum_follow_up


def test_dev02_missing_token_evaluator_cannot_default_to_pass(
    dev02_fixed_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    registry = dict(closeout.TOKEN_EVALUATOR_REGISTRY)
    registry.pop(closeout.TOKENS[-1])
    monkeypatch.setattr(closeout, "TOKEN_EVALUATOR_REGISTRY", registry)
    with pytest.raises(ValueError, match="evaluator registry|roster|approved"):
        closeout.evaluate_closeout()


def test_dev02_positive_evaluation_executes_every_token_specific_evaluator(
    dev02_fixed_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[str] = []
    wrapped: dict[str, Callable[[object], str]] = {}
    for token, evaluator in closeout.TOKEN_EVALUATOR_REGISTRY.items():
        def observe(
            row: object,
            *,
            observed_token: str = token,
            observed_evaluator: Callable[[object], str] = evaluator,
        ) -> str:
            calls.append(observed_token)
            return observed_evaluator(row)

        wrapped[token] = observe
    monkeypatch.setattr(closeout, "TOKEN_EVALUATOR_REGISTRY", wrapped)
    release_evaluator = closeout._semantic_release

    def observe_release(
        row: object,
        private_evidence: closeout._PrivateCiEvidence | None = None,
    ) -> str:
        calls.append("RELEASE_ID_RECOMPUTE_OK")
        return release_evaluator(row, private_evidence)

    monkeypatch.setattr(closeout, "_semantic_release", observe_release)
    snapshot = closeout.evaluate_closeout()
    assert calls == [
        token
        for token in closeout.TOKENS
        if token
        not in {"QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"}
    ]
    assert all(
        result.status == "PASS"
        for result in snapshot.token_results
        if result.token
        not in {*closeout.PLANNED_BINDINGS, "RELEASE_ID_RECOMPUTE_OK"}
    )


@pytest.mark.parametrize(
    "mutation,match",
    [
        (lambda rows: rows + (rows[0],), "duplicate token"),
        (lambda rows: rows[:-1], "token set mismatch"),
        (
            lambda rows: (replace(rows[0], token="UNEXPECTED_TOKEN_OK"), *rows[1:]),
            "token set mismatch",
        ),
        (
            lambda rows: (
                replace(rows[0], token="DEV_DB_BRIDGE_FALLBACK_OK"),
                *rows[1:],
            ),
            "token set mismatch|prohibited",
        ),
        (
            lambda rows: (replace(rows[0], token="UNREGISTERED_TOKEN_OK"), *rows[1:]),
            "token set mismatch|unregistered",
        ),
    ],
    ids=(
        "duplicate-token-row",
        "missing-corrected-roster-token",
        "unexpected-token",
        "retired-bridge-token",
        "unregistered-token",
    ),
)
def test_dev02_required_matrix_identity_negatives(
    dev02_repo: Path,
    mutation: Callable[[tuple[object, ...]], tuple[object, ...]],
    match: str,
) -> None:
    rows = closeout.build_rows()
    with pytest.raises(ValueError, match=match):
        closeout.validate_rows(mutation(rows), planned_mode="allow-current")


def test_dev02_retired_token_in_current_acceptance_artifact_fails(
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    def mutation(payload: dict[str, object]) -> None:
        records = payload["records"]
        assert isinstance(records, list) and isinstance(records[0], dict)
        records[0]["token"] = "DEV_DB_BRIDGE_FALLBACK_OK"

    broken = _mutate_package_json(
        dev02_valid_package, closeout.ACCEPTANCE_MAP_PATH, mutation
    )
    with pytest.raises(ValueError, match="roster|token|retired|prohibited"):
        closeout.validate_package(broken)


def test_dev02_p1_reused_evidence_is_revalidated_after_planned_materializes(
    dev02_fixed_repo: Path,
) -> None:
    row = next(
        row for row in closeout.build_rows() if row.token == "DOC_DELTA_PRESENT_OK"
    )
    assert all((dev02_fixed_repo / path).is_file() for path in closeout.PACKAGE_PATHS)
    (dev02_fixed_repo / row.primary_evidence[0]).unlink()
    snapshot = closeout.evaluate_closeout()
    assert _token_result(snapshot, row.token).status != "PASS"
    assert snapshot.blockers
    assert row.primary_evidence[0] in _snapshot_text(snapshot)


@pytest.mark.parametrize("posture", ("missing", "mismatched"))
def test_dev02_missing_or_mismatched_path_proof_fails_current_evaluation(
    dev02_fixed_repo: Path,
    posture: str,
) -> None:
    row = next(
        row for row in closeout.build_rows() if row.token == "DOC_DELTA_PRESENT_OK"
    )
    proof = dev02_fixed_repo / row.proof_anchors[0]
    if posture == "missing":
        proof.unlink()
    else:
        text = proof.read_text(encoding="utf-8")
        _replace_bytes(proof, text.replace("sha256: ", "sha256: 0", 1).encode())
    snapshot = closeout.evaluate_closeout()
    assert _token_result(snapshot, row.token).status != "PASS"
    assert row.proof_anchors[0] in _snapshot_text(snapshot)


@pytest.mark.parametrize("surface", ("human", "mirror"))
def test_dev02_nonexistent_or_mismatched_index_mirror_key_fails_current_evaluation(
    dev02_fixed_repo: Path,
    surface: str,
) -> None:
    row = next(
        row for row in closeout.build_rows() if row.token == "DOC_DELTA_PRESENT_OK"
    )
    key, path = row.artifact_keys[0], row.primary_evidence[0]
    if surface == "human":
        target = dev02_fixed_repo / closeout.HUMAN_INDEX_PATH
        payload = json.loads(target.read_text(encoding="utf-8"))
        match = next(
            item
            for item in payload
            if item.get("artifact_key") == key
            and item.get("discovered_physical_path") == path
        )
        match["artifact_key"] = "nonexistent.current.key"
        _replace_json(target, payload)
    else:
        target = dev02_fixed_repo / closeout.MACHINE_MIRROR_PATH
        records = [json.loads(line) for line in target.read_text(encoding="utf-8").splitlines()]
        match = next(
            item
            for item in records
            if item.get("artifact_key") == key
            and item.get("discovered_physical_path") == path
        )
        match["artifact_key"] = "nonexistent.current.key"
        body = b"".join(closeout._canonical_json(item) for item in records)
        _replace_bytes(target, body)
    snapshot = closeout.evaluate_closeout()
    assert _token_result(snapshot, row.token).status != "PASS"
    assert key in _snapshot_text(snapshot)


def test_dev02_stale_qa_current_state_fails_closed(dev02_fixed_repo: Path) -> None:
    manifest_path = dev02_fixed_repo / closeout.QA_MANIFEST_PATH
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["qa-23-po-023"]["status"] = "FAIL"
    _replace_json(manifest_path, manifest)
    snapshot = closeout.evaluate_closeout()
    assert snapshot.blockers
    assert not all(result.status == "PASS" for result in snapshot.token_results)
    assert "qa-23-po-023" in _snapshot_text(snapshot)


@pytest.mark.parametrize(
    "missing_path",
    (
        closeout.QA_MANIFEST_PATH,
        f"{closeout.QA_MANIFEST_PATH}.path_proof.txt",
        closeout.HUMAN_INDEX_PATH,
        closeout.MACHINE_MIRROR_PATH,
    ),
)
def test_dev02_positive_evaluation_refuses_incomplete_source_fixture(
    dev02_fixed_repo: Path,
    missing_path: str,
) -> None:
    (dev02_fixed_repo / missing_path).unlink()
    snapshot = closeout.evaluate_closeout()
    assert snapshot.blockers
    assert not all(result.status == "PASS" for result in snapshot.token_results)


@pytest.mark.parametrize("label", closeout.NON_TOKEN_OBLIGATIONS)
def test_dev02_every_non_token_close_obligation_is_directly_revalidated(
    dev02_fixed_repo: Path,
    label: str,
) -> None:
    _key, path, _proof = closeout.NON_TOKEN_BINDINGS[label]
    (dev02_fixed_repo / path).unlink()
    snapshot = closeout.evaluate_closeout()
    matches = [
        obligation
        for obligation in snapshot.obligations
        if obligation.get("label") == label
    ]
    assert len(matches) == 1
    assert matches[0]["status"] == "FAIL"
    assert any(
        blocker["predicate_key"]
        == f"non_token.{label}.current_governed_result"
        for blocker in snapshot.blockers
    )


def test_dev02_reduced_proof_family_roster_is_rejected(
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    def mutation(payload: dict[str, object]) -> None:
        proof_families = payload["proof_family_roster"]
        assert isinstance(proof_families, list) and proof_families
        proof_families.pop()

    broken = _mutate_package_json(
        dev02_valid_package, closeout.ACCEPTANCE_MAP_PATH, mutation
    )
    with pytest.raises(ValueError, match="proof-family|proof family|roster|reduced"):
        closeout.validate_package(broken)


def test_dev02_pointer_only_qa_rca_close_report_is_rejected(
    dev02_fixed_repo: Path,
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    source = (dev02_fixed_repo / closeout.QA_RCA_PATH).read_text(encoding="utf-8").rstrip()
    report = dev02_valid_package[closeout.CLOSE_REPORT_PATH].decode("utf-8")
    assert source in report
    pointer_only = report.replace(
        source,
        f"See preserved execution-level source evidence `{closeout.QA_RCA_PATH}`.",
        1,
    )
    broken = dict(dev02_valid_package)
    broken[closeout.CLOSE_REPORT_PATH] = pointer_only.encode("utf-8")
    with pytest.raises(ValueError, match="QA RCA|Doc Delta|embedded|report"):
        closeout.validate_package(broken)


def test_dev02_missing_pf09_scope_item_is_rejected(
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    missing = closeout.PF09_SCOPE[-1]

    def mutation(payload: dict[str, object]) -> None:
        scope = payload["pf09_scope"]
        assert isinstance(scope, list)
        scope.remove(missing)

    broken = _mutate_package_json(
        dev02_valid_package, closeout.CLOSE_MANIFEST_PATH, mutation
    )
    with pytest.raises(ValueError, match="PF09|scope|package"):
        closeout.validate_package(broken)


@pytest.mark.parametrize("issue", tuple(closeout.TRACKED_ISSUES))
def test_dev02_missing_tracked_issue_disposition_is_rejected(
    dev02_valid_package: Mapping[str, bytes],
    issue: str,
) -> None:
    report = dev02_valid_package[closeout.CLOSE_REPORT_PATH].decode("utf-8")
    assert issue in report
    broken = dict(dev02_valid_package)
    broken[closeout.CLOSE_REPORT_PATH] = report.replace(
        issue, "OMITTED-TRACKED-ISSUE"
    ).encode("utf-8")
    with pytest.raises(ValueError, match="tracked|issue|report|incomplete"):
        closeout.validate_package(broken)


@pytest.mark.parametrize(
    "adr", tuple(str(record["label"]) for record in closeout.ADR_RECORDS)
)
def test_dev02_missing_or_incomplete_adr_block_is_rejected(
    dev02_valid_package: Mapping[str, bytes],
    adr: str,
) -> None:
    report = dev02_valid_package[closeout.CLOSE_REPORT_PATH].decode("utf-8")
    assert adr in report
    broken = dict(dev02_valid_package)
    broken[closeout.CLOSE_REPORT_PATH] = report.replace(
        adr, "OMITTED-ADR-RECORD"
    ).encode("utf-8")
    with pytest.raises(ValueError, match="ADR|report|incomplete"):
        closeout.validate_package(broken)


def test_dev02_manifest_key_outputs_list_is_rejected(
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    def mutation(payload: dict[str, object]) -> None:
        key_outputs = payload["key_outputs"]
        assert isinstance(key_outputs, dict)
        payload["key_outputs"] = list(key_outputs.values())

    broken = _mutate_package_json(
        dev02_valid_package, closeout.CLOSE_MANIFEST_PATH, mutation
    )
    with pytest.raises(ValueError, match="key_outputs|object"):
        closeout.validate_package(broken)


def test_dev02_close_report_manifest_decision_mismatch_is_rejected(
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    def mutation(payload: dict[str, object]) -> None:
        payload["decision"] = "SATISFIED"

    broken = _mutate_package_json(
        dev02_valid_package, closeout.CLOSE_MANIFEST_PATH, mutation
    )
    with pytest.raises(ValueError, match="decision|mismatch"):
        closeout.validate_package(broken)


@pytest.fixture
def dev02_blocked_package(dev02_fixed_repo: Path) -> dict[str, bytes]:
    row = next(
        row for row in closeout.build_rows() if row.token == "DOC_DELTA_PRESENT_OK"
    )
    (dev02_fixed_repo / row.primary_evidence[0]).unlink()
    package = closeout.build_package()
    manifest = json.loads(package[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "NOT SATISFIED"
    assert manifest["minimum_follow_up"]
    assert set(package) == set(closeout.PACKAGE_PATHS)
    return package


def test_dev02_real_false_predicate_emits_complete_not_satisfied_package(
    dev02_blocked_package: Mapping[str, bytes],
) -> None:
    manifest = json.loads(dev02_blocked_package[closeout.CLOSE_MANIFEST_PATH])
    assert set(dev02_blocked_package) == set(closeout.PACKAGE_PATHS)
    assert manifest["decision"] == "NOT SATISFIED"
    assert {
        json.loads(dev02_blocked_package[path])["result"]
        for path in (
            closeout.PRECOMMIT_CHECKLIST_PATH,
            closeout.POSTCOMMIT_CHECKLIST_PATH,
        )
    } == {"FAIL"}


def test_dev02_forced_satisfied_with_false_predicate_is_rejected(
    dev02_blocked_package: Mapping[str, bytes],
) -> None:
    broken = dict(dev02_blocked_package)
    for relative in (closeout.CLOSE_MANIFEST_PATH, closeout.ACCEPTANCE_MAP_PATH):
        payload = json.loads(broken[relative])
        payload["decision"] = "SATISFIED"
        if isinstance(payload.get("token_status"), dict):
            payload["token_status"] = {token: "PASS" for token in closeout.TOKENS}
        if isinstance(payload.get("records"), list):
            for record in payload["records"]:
                if isinstance(record, dict) and "status" in record:
                    record["status"] = "PASS"
        broken[relative] = closeout._canonical_json(payload)
    broken[closeout.CLOSE_REPORT_PATH] = broken[closeout.CLOSE_REPORT_PATH].replace(
        b"NOT SATISFIED", b"SATISFIED"
    )
    broken[closeout.VIABILITY_PATH] = broken[closeout.VIABILITY_PATH].replace(
        b"NOT SATISFIED", b"SATISFIED"
    )
    with pytest.raises(
        ValueError,
        match="forced|blocker|SATISFIED|predicate|evaluation|token-status",
    ):
        closeout.validate_package(broken)


def test_dev02_not_satisfied_without_exact_minimum_follow_up_is_rejected(
    dev02_blocked_package: Mapping[str, bytes],
) -> None:
    broken = dict(dev02_blocked_package)
    for relative in (closeout.CLOSE_MANIFEST_PATH, closeout.ACCEPTANCE_MAP_PATH):
        payload = json.loads(broken[relative])
        payload["minimum_follow_up"] = []
        broken[relative] = closeout._canonical_json(payload)
    report = broken[closeout.CLOSE_REPORT_PATH].decode("utf-8")
    marker = "## Minimum follow-up"
    assert marker in report
    broken[closeout.CLOSE_REPORT_PATH] = report.split(marker, 1)[0].rstrip().encode() + b"\n"
    with pytest.raises(ValueError, match="follow-up|follow up|NOT SATISFIED"):
        closeout.validate_package(broken)


@pytest.mark.parametrize(
    "suppressed", (closeout.CLOSE_REPORT_PATH, closeout.CLOSE_MANIFEST_PATH)
)
def test_dev02_blocker_cannot_suppress_or_partially_emit_binary_outputs(
    dev02_blocked_package: Mapping[str, bytes],
    suppressed: str,
) -> None:
    broken = dict(dev02_blocked_package)
    del broken[suppressed]
    with pytest.raises(ValueError, match="incomplete|package|path"):
        closeout.validate_package(broken)


def test_dev02_write_revalidates_package_before_staging(
    dev02_fixed_repo: Path,
    dev02_valid_package: Mapping[str, bytes],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    broken = dict(dev02_valid_package)
    del broken[closeout.CLOSE_MANIFEST_PATH]
    before = _tree_state(dev02_fixed_repo)

    def forbidden_stage(_target: Path, _data: bytes, _mode: int) -> Path:
        pytest.fail("invalid package reached staging")

    monkeypatch.setattr(closeout, "_stage_atomic_bytes", forbidden_stage)
    with pytest.raises(ValueError, match="incomplete|package|path"):
        closeout._write_package(broken)
    assert _tree_state(dev02_fixed_repo) == before


@pytest.mark.parametrize("failed_stage", range(1, len(closeout.PACKAGE_PATHS) + 1))
def test_dev02_atomic_write_leaves_no_partial_package_after_staging_failure(
    dev02_fixed_repo: Path,
    dev02_valid_package: Mapping[str, bytes],
    monkeypatch: pytest.MonkeyPatch,
    failed_stage: int,
) -> None:
    before = _package_at(dev02_fixed_repo)
    before_entries = {
        (dev02_fixed_repo / relative).parent: tuple(
            sorted(path.name for path in (dev02_fixed_repo / relative).parent.iterdir())
        )
        for relative in closeout.PACKAGE_PATHS
    }
    changed = {
        relative: body + b"INJECTED-TRANSACTION-CANDIDATE\n"
        for relative, body in dev02_valid_package.items()
    }
    real_stage = closeout._stage_atomic_bytes
    calls = 0

    def fail_once(target: Path, data: bytes, mode: int) -> Path:
        nonlocal calls
        calls += 1
        if calls == failed_stage:
            raise OSError("injected staging failure")
        return real_stage(target, data, mode)

    monkeypatch.setattr(closeout, "validate_package", lambda _package: None)
    monkeypatch.setattr(closeout, "_stage_atomic_bytes", fail_once)
    with pytest.raises(OSError, match="injected staging failure"):
        closeout._write_package(changed)
    assert _package_at(dev02_fixed_repo) == before
    assert {
        parent: tuple(sorted(path.name for path in parent.iterdir()))
        for parent in before_entries
    } == before_entries


def test_dev02_atomic_write_is_byte_idempotent(
    dev02_fixed_repo: Path,
    dev02_valid_package: Mapping[str, bytes],
) -> None:
    closeout._write_package(dev02_valid_package)
    first = _package_at(dev02_fixed_repo)
    closeout._write_package(dev02_valid_package)
    assert _package_at(dev02_fixed_repo) == first == dict(dev02_valid_package)


@pytest.mark.parametrize("failed_replace", range(1, len(closeout.PACKAGE_PATHS) + 1))
def test_dev02_atomic_write_restores_every_target_after_replacement_failure(
    dev02_fixed_repo: Path,
    dev02_valid_package: Mapping[str, bytes],
    monkeypatch: pytest.MonkeyPatch,
    failed_replace: int,
) -> None:
    before = _package_at(dev02_fixed_repo)
    changed = {
        relative: body + b"INJECTED-TRANSACTION-CANDIDATE\n"
        for relative, body in dev02_valid_package.items()
    }
    real_replace = closeout.os.replace
    calls = 0

    def fail_once(source: object, target: object) -> None:
        nonlocal calls
        calls += 1
        if calls == failed_replace:
            raise OSError("injected replacement failure")
        real_replace(source, target)

    monkeypatch.setattr(closeout, "validate_package", lambda _package: None)
    monkeypatch.setattr(closeout.os, "replace", fail_once)
    with pytest.raises(OSError, match="injected replacement failure"):
        closeout._write_package(changed)
    assert _package_at(dev02_fixed_repo) == before


def test_dev02_preflight_is_fully_read_only(dev02_repo: Path) -> None:
    before = _tree_state(dev02_repo)
    result = _run_repo_tool(
        dev02_repo, "tools/evidence/generate_hde_epic038_closeout.py", "--preflight"
    )
    _assert_success(result)
    assert "PREFLIGHT" in result.stdout
    assert _tree_state(dev02_repo) == before


def test_dev02_check_is_fully_read_only(dev02_fixed_repo: Path) -> None:
    before = _tree_state(dev02_fixed_repo)
    result = _run_repo_tool(
        dev02_fixed_repo,
        "tools/evidence/generate_hde_epic038_closeout.py",
        "--check",
    )
    _assert_success(result)
    assert "CLOSEOUT_PACKAGE_OK" in result.stdout
    assert _tree_state(dev02_fixed_repo) == before


def test_dev02_check_never_dispatches_the_package_writer(
    dev02_fixed_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def forbidden_write(_package: Mapping[str, bytes]) -> None:
        pytest.fail("--check attempted to dispatch the package writer")

    monkeypatch.setattr(closeout, "_write_package", forbidden_write)
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate_hde_epic038_closeout.py", "--check"],
    )
    assert closeout.main() == 0


@pytest.mark.parametrize("argument", ("--pre", "--rec", "--close-b"))
def test_dev02_cli_abbreviations_are_rejected_without_writes(
    dev02_repo: Path,
    argument: str,
) -> None:
    before = _tree_state(dev02_repo)
    result = _run_repo_tool(
        dev02_repo, "tools/evidence/generate_hde_epic038_closeout.py", argument
    )
    assert result.returncode == 2
    assert "WROTE" not in result.stdout
    assert _tree_state(dev02_repo) == before


def test_dev02_updater_family_is_inactive_when_no_primary_exists(
    dev02_repo: Path,
) -> None:
    family_paths = tuple(
        str(record["discovered_physical_path"])
        for record in updater.EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS
    )
    assert not any((dev02_repo / path).exists() for path in family_paths)
    before = _tree_state(dev02_repo)
    assert updater._load_epic038_closeout_entries() == []
    assert _tree_state(dev02_repo) == before


@pytest.mark.parametrize(
    "present_index",
    range(len(updater.EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS)),
)
def test_dev02_updater_rejects_every_partial_primary_family(
    dev02_repo: Path,
    present_index: int,
) -> None:
    record = updater.EPIC038_CLOSEOUT_PRIMARY_ARTIFACTS[present_index]
    path = dev02_repo / str(record["discovered_physical_path"])
    _replace_bytes(path, b"partial DEV-03 family\n")
    with pytest.raises(SystemExit, match="INCOMPLETE_EPIC038_CLOSEOUT_FAMILY"):
        updater._load_epic038_closeout_entries()


def _assert_dev02_planned_family_fails_closed(
    snapshot: closeout.EvaluationSnapshot,
) -> None:
    planned_tokens = set(closeout.PLANNED_BINDINGS)
    planned_results = [
        result
        for result in snapshot.token_results
        if result.token in planned_tokens
    ]
    assert {result.token for result in planned_results} == planned_tokens
    assert {result.status for result in planned_results} == {"FAIL"}
    assert all(
        result.predicate_key.endswith(".planned_binding")
        for result in planned_results
    )
    assert len({result.detail for result in planned_results}) == 1
    assert {
        blocker["subject"]["value"] for blocker in snapshot.blockers
    } == planned_tokens
    assert all(
        result.status == "PASS"
        for result in snapshot.token_results
        if result.token
        not in {*planned_tokens, "RELEASE_ID_RECOMPUTE_OK"}
    )
    assert _token_result(snapshot, "RELEASE_ID_RECOMPUTE_OK").status == "UNCLAIMED"
    assert all(
        obligation.get("status") == "PASS"
        for obligation in snapshot.obligations
    )


def _dev02_atomic_family_watch_paths() -> set[str]:
    paths = {
        *closeout.PACKAGE_PATHS,
        *(
            proof
            for _primary, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
        ),
        closeout.HUMAN_INDEX_PATH,
        f"{closeout.HUMAN_INDEX_PATH}.path_proof.txt",
        "docs/evidence/INDEX.sha256",
        "docs/evidence/INDEX.sha256.path_proof.txt",
        closeout.MACHINE_MIRROR_PATH,
        f"{closeout.MACHINE_MIRROR_PATH}.path_proof.txt",
        "artifacts/evidence_index.jsonl.sha256",
        "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
    }
    for relative in tuple(paths):
        parent = Path(relative).parent
        while parent != Path("."):
            paths.add(parent.as_posix())
            parent = parent.parent
    return paths


def _dev02_atomic_family_watch_state(root: Path) -> dict[str, tuple[object, ...]]:
    state: dict[str, tuple[object, ...]] = {}
    for relative in sorted(_dev02_atomic_family_watch_paths()):
        path = root / relative
        if not path.exists() and not path.is_symlink():
            state[relative] = ("missing",)
            continue
        stat_result = path.lstat()
        if path.is_symlink():
            state[relative] = (
                "symlink",
                path.readlink().as_posix(),
                stat_result.st_mode,
                stat_result.st_mtime_ns,
            )
        elif path.is_file():
            body = path.read_bytes()
            state[relative] = (
                "file",
                hashlib.sha256(body).hexdigest(),
                len(body),
                stat_result.st_mode,
                stat_result.st_mtime_ns,
            )
        elif path.is_dir():
            state[relative] = (
                "directory",
                tuple(sorted(child.name for child in path.iterdir())),
                stat_result.st_mode,
                stat_result.st_mtime_ns,
            )
    return state


def _dev02_nonfamily_tree_state(root: Path) -> dict[str, tuple[object, ...]]:
    excluded = _dev02_atomic_family_watch_paths()
    return {
        relative: value
        for relative, value in _tree_state(root).items()
        if relative not in excluded
    }


def _assert_dev02_blocked_preflight(
    root: Path,
    *,
    allow_structural_error: bool = False,
) -> None:
    result = _run_repo_tool(
        root,
        "tools/evidence/generate_hde_epic038_closeout.py",
        "--preflight",
    )
    assert result.returncode != 0, result.stdout + result.stderr
    if "PREFLIGHT BLOCKED" in result.stdout:
        assert f"blockers={len(closeout.PLANNED_BINDINGS)}" in result.stdout
    else:
        assert allow_structural_error
        assert "PREFLIGHT_BLOCKER:" in result.stdout
        assert "invalid ledger template" in result.stdout
    assert "WROTE" not in result.stdout


def _assert_dev02_blocked_preflight_in_process(
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        ["generate_hde_epic038_closeout.py", "--preflight"],
    )
    assert closeout.main() == 1
    captured = capsys.readouterr()
    assert not captured.err
    assert "PREFLIGHT BLOCKED" in captured.out
    assert f"blockers={len(closeout.PLANNED_BINDINGS)}" in captured.out
    assert "WROTE" not in captured.out


def test_dev02_evaluate_and_preflight_reject_every_partial_atomic_primary_family(
    dev02_repo: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    primary_paths = tuple(closeout.PACKAGE_ACTIVATION_PATHS)
    assert len(primary_paths) == 7
    assert closeout.CLOSE_REPORT_PATH in primary_paths
    assert not any((dev02_repo / path).exists() for path in primary_paths)
    assert all((dev02_repo / path).parent.is_dir() for path in primary_paths)
    baseline = closeout.evaluate_closeout()
    assert not baseline.blockers
    assert {
        result.status
        for result in baseline.token_results
        if result.token in closeout.PLANNED_BINDINGS
    } == {"UNCLAIMED"}
    canonical = closeout.build_package(evaluation_snapshot=baseline)
    proper_masks = range(1, (1 << len(primary_paths)) - 1)
    assert len(proper_masks) == 126
    before_all_subsets = _dev02_nonfamily_tree_state(dev02_repo)

    for mask in proper_masks:
        subset = tuple(
            path
            for index, path in enumerate(primary_paths)
            if mask & (1 << index)
        )
        try:
            for path in subset:
                _replace_bytes(dev02_repo / path, canonical[path])
            before_evaluate = _dev02_atomic_family_watch_state(dev02_repo)
            snapshot = closeout.evaluate_closeout()
            _assert_dev02_planned_family_fails_closed(snapshot)
            _assert_dev02_blocked_preflight_in_process(capsys, monkeypatch)
            assert (
                _dev02_atomic_family_watch_state(dev02_repo) == before_evaluate
            ), subset
        finally:
            for path in subset:
                (dev02_repo / path).unlink(missing_ok=True)

    assert not any((dev02_repo / path).exists() for path in primary_paths)
    assert _dev02_nonfamily_tree_state(dev02_repo) == before_all_subsets


def test_dev02_arbitrary_isolated_close_report_fails_closed_and_read_only(
    dev02_repo: Path,
) -> None:
    primary_paths = tuple(closeout.PACKAGE_ACTIVATION_PATHS)
    close_report = dev02_repo / closeout.CLOSE_REPORT_PATH
    _replace_bytes(
        close_report,
        b"# Arbitrary incomplete HDE-EPIC038 close report\n",
    )
    assert {
        path for path in primary_paths if (dev02_repo / path).is_file()
    } == {closeout.CLOSE_REPORT_PATH}

    before_evaluate = _tree_state(dev02_repo)
    snapshot = closeout.evaluate_closeout()
    _assert_dev02_planned_family_fails_closed(snapshot)
    assert _tree_state(dev02_repo) == before_evaluate
    before_preflight = _tree_state(dev02_repo)
    _assert_dev02_blocked_preflight(dev02_repo)
    assert _tree_state(dev02_repo) == before_preflight


def test_dev02_complete_canonical_primary_only_transition_converges(
    dev02_repo: Path,
) -> None:
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/generate_hde_epic038_closeout.py",
        )
    )
    primary_paths = tuple(closeout.PACKAGE_ACTIVATION_PATHS)
    primary_package = _package_at(dev02_repo)
    assert all((dev02_repo / path).is_file() for path in primary_paths)
    assert not any(
        (dev02_repo / proof).exists()
        for _primary, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
    )

    transition = closeout.evaluate_closeout()
    assert not transition.blockers
    assert {
        result.status
        for result in transition.token_results
        if result.token in closeout.PLANNED_BINDINGS
    } == {"UNCLAIMED"}
    assert closeout.build_package(evaluation_snapshot=transition) == primary_package
    before_preflight = _tree_state(dev02_repo)
    preflight = _run_repo_tool(
        dev02_repo,
        "tools/evidence/generate_hde_epic038_closeout.py",
        "--preflight",
    )
    _assert_success(preflight)
    assert "PREFLIGHT OK" in preflight.stdout
    assert f"planned_unclaimed={len(closeout.PLANNED_BINDINGS)}" in preflight.stdout
    assert _tree_state(dev02_repo) == before_preflight

    _converge_dev02_evidence_graph(dev02_repo)
    assert _package_at(dev02_repo) == primary_package
    converged = closeout.evaluate_closeout()
    assert not converged.blockers
    assert {
        result.status
        for result in converged.token_results
        if result.token in closeout.PLANNED_BINDINGS
    } == {"UNCLAIMED"}
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/generate_hde_epic038_closeout.py",
            "--check",
        )
    )
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/update_evidence_index.py",
            "--check",
        )
    )
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/orientation_demo.py",
            "--check",
        )
    )


def test_dev02_evaluate_and_preflight_reject_each_tampered_complete_primary_family(
    dev02_repo: Path,
) -> None:
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/generate_hde_epic038_closeout.py",
        )
    )
    primary_paths = tuple(closeout.PACKAGE_ACTIVATION_PATHS)
    canonical = _package_at(dev02_repo)
    before_all_tampering = _dev02_nonfamily_tree_state(dev02_repo)

    for tampered_path in primary_paths:
        target = dev02_repo / tampered_path
        _replace_bytes(target, canonical[tampered_path] + b"TAMPERED\n")
        try:
            before_evaluate = _dev02_atomic_family_watch_state(dev02_repo)
            snapshot = closeout.evaluate_closeout()
            _assert_dev02_planned_family_fails_closed(snapshot)
            _assert_dev02_blocked_preflight(
                dev02_repo,
                allow_structural_error=tampered_path == closeout.LEDGER_PATH,
            )
            assert (
                _dev02_atomic_family_watch_state(dev02_repo) == before_evaluate
            ), tampered_path
        finally:
            _replace_bytes(target, canonical[tampered_path])

    assert _dev02_nonfamily_tree_state(dev02_repo) == before_all_tampering


def test_dev02_coordinated_source_fingerprint_tamper_fails_closed_and_read_only(
    dev02_repo: Path,
) -> None:
    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/generate_hde_epic038_closeout.py",
        )
    )
    assert all(
        (dev02_repo / path).is_file()
        for path in closeout.PACKAGE_ACTIVATION_PATHS
    )
    assert not any(
        (dev02_repo / proof).exists()
        for _primary, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
    )
    closeout_keys = set(closeout.CLOSEOUT_PRIMARY_BINDINGS)
    assert not closeout_keys & {
        str(item.get("artifact_key")) for item in closeout._human_items()
    }
    assert not closeout_keys & {
        str(item.get("artifact_key")) for item in closeout._mirror_items()
    }
    transition = closeout.evaluate_closeout()
    assert not transition.blockers
    assert {
        result.status
        for result in transition.token_results
        if result.token in closeout.PLANNED_BINDINGS
    } == {"UNCLAIMED"}

    canonical = _package_at(dev02_repo)
    manifest = json.loads(canonical[closeout.CLOSE_MANIFEST_PATH])
    original_fingerprint = manifest["source_evaluation_fingerprint"]
    assert isinstance(original_fingerprint, str)
    assert len(original_fingerprint) == 64
    tampered_fingerprint = "0" * 64
    if tampered_fingerprint == original_fingerprint:
        tampered_fingerprint = "1" * 64

    tampered = _mutate_package_json(
        canonical,
        closeout.CLOSE_MANIFEST_PATH,
        lambda payload: payload.__setitem__(
            "source_evaluation_fingerprint", tampered_fingerprint
        ),
    )
    tampered = _mutate_package_json(
        tampered,
        closeout.ACCEPTANCE_MAP_PATH,
        lambda payload: payload.__setitem__(
            "source_evaluation_fingerprint", tampered_fingerprint
        ),
    )
    fingerprint_line = (
        f"SOURCE_EVALUATION_FINGERPRINT: {original_fingerprint}\n".encode()
    )
    tampered_line = (
        f"SOURCE_EVALUATION_FINGERPRINT: {tampered_fingerprint}\n".encode()
    )
    assert canonical[closeout.VIABILITY_PATH].count(fingerprint_line) == 1
    tampered[closeout.VIABILITY_PATH] = canonical[
        closeout.VIABILITY_PATH
    ].replace(fingerprint_line, tampered_line)
    assert original_fingerprint.encode() not in canonical[closeout.CLOSE_REPORT_PATH]

    before_validation = _tree_state(dev02_repo)
    with pytest.raises(ValueError, match="fingerprint|snapshot|structure"):
        closeout.validate_package_structure(tampered)
    assert _tree_state(dev02_repo) == before_validation
    with pytest.raises(ValueError, match="fingerprint|snapshot|cross-surface"):
        closeout.validate_package(tampered)
    assert _tree_state(dev02_repo) == before_validation

    for path in (
        closeout.CLOSE_MANIFEST_PATH,
        closeout.ACCEPTANCE_MAP_PATH,
        closeout.VIABILITY_PATH,
    ):
        _replace_bytes(dev02_repo / path, tampered[path])
    before_evaluate = _tree_state(dev02_repo)
    snapshot = closeout.evaluate_closeout()
    _assert_dev02_planned_family_fails_closed(snapshot)
    assert _tree_state(dev02_repo) == before_evaluate
    before_preflight = _tree_state(dev02_repo)
    _assert_dev02_blocked_preflight(dev02_repo)
    assert _tree_state(dev02_repo) == before_preflight


@pytest.mark.parametrize(
    "field,replacement",
    (
        ("epic_id", "HDE-EPIC999"),
        ("schema_version", "9.9"),
        ("key_outputs", {"reduced": "audit/EPIC-038_close_report.md"}),
    ),
    ids=("epic-identity", "schema", "key-output-bindings"),
)
def test_dev02_updater_rejects_mismatched_manifest_bindings(
    dev02_fixed_repo: Path,
    field: str,
    replacement: object,
) -> None:
    manifest_path = dev02_fixed_repo / closeout.CLOSE_MANIFEST_PATH
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest[field] = replacement
    _replace_json(manifest_path, manifest)
    with pytest.raises(SystemExit, match="INVALID_EPIC038_CLOSEOUT"):
        updater._load_epic038_closeout_entries()


def test_dev02_generation_preserves_dev01_bytes_and_nonclaiming_contract(
    dev02_repo: Path,
) -> None:
    matrix_path = dev02_repo / closeout.OUTPUT
    before = matrix_path.read_bytes()
    before_rows = tuple(
        (row.token, row.posture, row.future_claim) for row in closeout.build_rows()
    )
    assert hashlib.sha256(before).hexdigest() == closeout.TOKEN_MATRIX_SHA256
    assert before == closeout.render(planned_mode="require-absent")
    assert all("UNCLAIMED" in posture for _token, posture, _claim in before_rows)

    _assert_success(
        _run_repo_tool(
            dev02_repo,
            "tools/evidence/generate_hde_epic038_closeout.py",
        )
    )

    assert matrix_path.read_bytes() == before
    assert hashlib.sha256(matrix_path.read_bytes()).hexdigest() == (
        closeout.TOKEN_MATRIX_SHA256
    )
    after_rows = closeout.validate_rows(
        closeout.build_rows(), planned_mode="allow-current"
    )
    assert tuple(
        (row.token, row.posture, row.future_claim) for row in after_rows
    ) == before_rows


def _dev02_blocker_descriptor(
    token: str = "TESTS_PASS_OK",
    *,
    predicate_key: str | None = None,
    external_action_posture: str = "NONE_REQUIRED",
) -> dict[str, object]:
    row = next(row for row in closeout.build_rows() if row.token == token)
    return closeout._descriptor(
        predicate_key or f"token.{token}.current_governed_result",
        "TOKEN",
        token,
        f"fixture records a directly re-evaluable failing predicate for {token}",
        [
            {"kind": "ARTIFACT_PATH", "value": row.primary_evidence[0]},
            {"kind": "ARTIFACT_KEY", "value": row.artifact_keys[0]},
        ],
        closeout.PLAN_CLOSEOUT_CHECK_COMMAND,
        "GOVERNED_ARTIFACT_DRIFT",
        [row.primary_evidence[0]],
        f"Re-establish and directly validate the current predicate for {token}.",
        ["closeout_package_in_memory", "epic038_current_state"],
        external_action_posture,
    )


def _dev02_close_request(
    blocker_id: str,
    *,
    regenerated_artifacts: tuple[str, ...] = (),
    external_action_posture: str = "NONE_REQUIRED",
) -> str:
    return closeout._canonical_json(
        {
            "blocker_id": blocker_id,
            "correction_performed": "Restored the exact governed predicate bytes.",
            "external_action_posture": external_action_posture,
            "historical_evidence_rewritten": False,
            "regenerated_artifacts": list(regenerated_artifacts),
            "schema": closeout.CLOSE_REQUEST_SCHEMA,
        }
    ).decode("utf-8")


def _dev02_closed_ledger(
    open_ledger: Mapping[str, object],
) -> dict[str, object]:
    closed = json.loads(json.dumps(open_ledger))
    entry = closed["entries"][0]
    entry.update(
        {
            "after_outcome": {
                "detail": "original predicate and validators directly pass",
                "result": "PASS",
            },
            "correction_performed": "Restored exact governed bytes.",
            "regenerated_artifacts": [],
            "reviewer_disposition": "CLOSURE_VALIDATED",
            "status": "CLOSED",
            "tests_and_validators": [
                {
                    "command": "internal:validate_package",
                    "exit_code": 0,
                    "id": "closeout_package_in_memory",
                    "result": "PASS",
                },
                {
                    "command": (
                        "python tools/evidence/"
                        "check_hde_epic038_qa_current_state.py --require-finalized"
                    ),
                    "exit_code": 0,
                    "id": "epic038_current_state",
                    "result": "PASS",
                },
            ],
        }
    )
    closeout.validate_ledger(closed)
    return closed


def test_dev02_ledger_record_is_idempotent_for_identical_open_blocker(
    dev02_repo: Path,
) -> None:
    descriptor = _dev02_blocker_descriptor()
    first = closeout.record_blockers(closeout._empty_ledger(), [descriptor])
    second = closeout.record_blockers(first, [descriptor])
    assert second == first
    assert len(second["entries"]) == 1
    closeout.validate_ledger(second)


def test_dev02_ledger_recurrence_preserves_closed_history_and_increments_id(
    dev02_repo: Path,
) -> None:
    descriptor = _dev02_blocker_descriptor()
    first = closeout.record_blockers(closeout._empty_ledger(), [descriptor])
    closed = _dev02_closed_ledger(first)
    recurrent = closeout.record_blockers(closed, [descriptor])
    assert len(recurrent["entries"]) == 2
    assert recurrent["entries"][0] == closed["entries"][0]
    assert [entry["status"] for entry in recurrent["entries"]] == [
        "CLOSED",
        "OPEN",
    ]
    first_id, second_id = [entry["blocker_id"] for entry in recurrent["entries"]]
    assert first_id[:-4] == second_id[:-4]
    assert first_id.endswith("0001")
    assert second_id.endswith("0002")


def test_dev02_ledger_rejects_normalized_identity_digest_collisions(
    dev02_repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def colliding_id(
        _predicate_key: str,
        _subject: Mapping[str, str],
        occurrence: int = 1,
    ) -> str:
        return f"HDE-EPIC038-BLK-deadbeefdeadbeef-{occurrence:04d}"

    monkeypatch.setattr(closeout, "_blocker_id", colliding_id)
    blockers = [
        _dev02_blocker_descriptor("TESTS_PASS_OK"),
        _dev02_blocker_descriptor("DOC_DELTA_PRESENT_OK"),
    ]
    with pytest.raises(ValueError, match="collision"):
        closeout.record_blockers(closeout._empty_ledger(), blockers)


@pytest.mark.parametrize(
    "raw,match",
    (
        ("{}", "close request|schema|canonical"),
        ('{"blocker_id":"x","blocker_id":"y"}\n', "duplicate|invalid"),
        ("not-json\n", "JSON"),
        (
            '{"blocker_id":"x","correction_performed":"x",'
            '"external_action_posture":"NONE_REQUIRED",'
            '"historical_evidence_rewritten":false,'
            '"regenerated_artifacts":[],"schema":'
            f'"{closeout.CLOSE_REQUEST_SCHEMA}"}}',
            "canonical",
        ),
    ),
    ids=("empty-object", "duplicate-key", "invalid-json", "missing-final-lf"),
)
def test_dev02_close_rejects_malformed_or_noncanonical_requests(
    dev02_repo: Path,
    raw: str,
    match: str,
) -> None:
    with pytest.raises(ValueError, match=match):
        closeout.close_blocker(raw)


def test_dev02_close_rejects_historical_evidence_rewrite_request(
    dev02_repo: Path,
) -> None:
    raw = closeout._canonical_json(
        {
            "blocker_id": "HDE-EPIC038-BLK-0000000000000000-0001",
            "correction_performed": "Attempted an impermissible history rewrite.",
            "external_action_posture": "NONE_REQUIRED",
            "historical_evidence_rewritten": True,
            "regenerated_artifacts": [],
            "schema": closeout.CLOSE_REQUEST_SCHEMA,
        }
    ).decode("utf-8")
    with pytest.raises(ValueError, match="historical evidence rewrite"):
        closeout.close_blocker(raw)


def test_dev02_close_rejects_unknown_blocker_identity(
    dev02_repo: Path,
) -> None:
    request = _dev02_close_request(
        "HDE-EPIC038-BLK-0000000000000000-0001"
    )
    with pytest.raises(RuntimeError, match="exactly one OPEN|unknown"):
        closeout.close_blocker(request)


def test_dev02_ledger_parser_rejects_noncanonical_serialization(
    dev02_repo: Path,
) -> None:
    canonical = closeout.render_ledger(closeout._empty_ledger())
    for malformed in (
        canonical.removesuffix(b"\n"),
        canonical.replace(b"  \"entries\"", b" \"entries\"", 1),
        canonical.replace(b"\n", b"\r\n"),
    ):
        with pytest.raises(ValueError, match="ledger|template|canonical"):
            closeout.parse_ledger(malformed)


def _converge_dev02_evidence_graph(root: Path) -> None:
    _assert_success(_run_repo_tool(root, "tools/evidence/update_evidence_index.py"))
    _assert_success(_run_repo_tool(root, "tools/evidence/orientation_demo.py"))
    _assert_success(_run_repo_tool(root, "tools/evidence/update_evidence_index.py"))


@pytest.fixture(scope="session")
def dev02_open_ledger_tree(
    dev02_fixed_point_tree: Path,
    tmp_path_factory: pytest.TempPathFactory,
) -> tuple[Path, str]:
    root = _clone_repo(
        dev02_fixed_point_tree,
        tmp_path_factory.mktemp("hde-epic038-dev02-open-ledger") / "repo",
    )
    previous_root = closeout.ROOT
    closeout.ROOT = root
    try:
        descriptor = _dev02_blocker_descriptor("DOC_DELTA_PRESENT_OK")
        ledger = closeout.record_blockers(closeout._empty_ledger(), [descriptor])
        package = closeout.build_package(ledger=ledger)
        manifest = json.loads(package[closeout.CLOSE_MANIFEST_PATH])
        assert manifest["decision"] == "NOT SATISFIED"
        assert {
            json.loads(package[path])["result"]
            for path in (
                closeout.PRECOMMIT_CHECKLIST_PATH,
                closeout.POSTCOMMIT_CHECKLIST_PATH,
            )
        } == {"FAIL"}
        closeout._write_package(package)
    finally:
        closeout.ROOT = previous_root
    primaries = _package_at(root)
    _assert_success(_run_repo_tool(root, "tools/evidence/update_evidence_index.py"))
    assert _package_at(root) == primaries
    _assert_success(_run_repo_tool(root, "tools/evidence/orientation_demo.py"))
    _assert_success(_run_repo_tool(root, "tools/evidence/update_evidence_index.py"))
    assert _package_at(root) == primaries
    entry = closeout.parse_ledger(package[closeout.LEDGER_PATH])["entries"][0]
    assert entry["status"] == "OPEN"
    return root, str(entry["blocker_id"])


@pytest.fixture
def dev02_open_ledger_repo(
    dev02_open_ledger_tree: tuple[Path, str],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[Path, str]:
    source, blocker_id = dev02_open_ledger_tree
    root = _clone_repo(source, tmp_path / "repo")
    monkeypatch.setattr(closeout, "ROOT", root)
    monkeypatch.setattr(updater, "ROOT", root)
    return root, blocker_id


def test_dev02_close_executes_real_predicate_and_all_registered_validators(
    dev02_open_ledger_repo: tuple[Path, str],
) -> None:
    root, blocker_id = dev02_open_ledger_repo
    governed_paths = {
        *closeout.PACKAGE_PATHS,
        *(
            proof
            for _primary, proof in closeout.CLOSEOUT_PRIMARY_BINDINGS.values()
        ),
        closeout.HUMAN_INDEX_PATH,
        f"{closeout.HUMAN_INDEX_PATH}.path_proof.txt",
        "docs/evidence/INDEX.sha256",
        "docs/evidence/INDEX.sha256.path_proof.txt",
        closeout.MACHINE_MIRROR_PATH,
        f"{closeout.MACHINE_MIRROR_PATH}.path_proof.txt",
        "artifacts/evidence_index.jsonl.sha256",
        "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
    }

    def assert_governed_state_present() -> None:
        missing = sorted(path for path in governed_paths if not (root / path).is_file())
        assert not missing

    assert_governed_state_present()
    open_package = _package_at(root)
    open_manifest = json.loads(open_package[closeout.CLOSE_MANIFEST_PATH])
    open_ledger = closeout.parse_ledger(open_package[closeout.LEDGER_PATH])
    assert open_manifest["decision"] == "NOT SATISFIED"
    assert {
        json.loads(open_package[path])["result"]
        for path in (
            closeout.PRECOMMIT_CHECKLIST_PATH,
            closeout.POSTCOMMIT_CHECKLIST_PATH,
        )
    } == {"FAIL"}
    assert [
        entry["blocker_id"]
        for entry in open_ledger["entries"]
        if entry["status"] == "OPEN"
    ] == [blocker_id]
    assert not any(
        entry["status"] == "OPEN"
        and entry["subject"]["value"] in closeout.PLANNED_BINDINGS
        for entry in open_ledger["entries"]
    )

    materialized = closeout.evaluate_closeout()
    assert not materialized.blockers
    assert {
        result.status
        for result in materialized.token_results
        if result.token
        in {"QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"}
    } == {"UNCLAIMED"}
    assert all(
        result.status != "FAIL"
        for result in materialized.token_results
        if result.token in closeout.PLANNED_BINDINGS
    )
    assert closeout.build_package(evaluation_snapshot=materialized) == open_package

    before_preflight = _tree_state(root)
    preflight = _run_repo_tool(
        root,
        "tools/evidence/generate_hde_epic038_closeout.py",
        "--preflight",
    )
    assert preflight.returncode != 0, preflight.stdout + preflight.stderr
    assert "PREFLIGHT BLOCKED" in preflight.stdout
    assert "blockers=0" in preflight.stdout
    assert "open_ledger=1" in preflight.stdout
    assert _tree_state(root) == before_preflight

    package = closeout.close_blocker(_dev02_close_request(blocker_id))
    closeout.validate_package(package)
    ledger = closeout.parse_ledger(package[closeout.LEDGER_PATH])
    entry = ledger["entries"][0]
    assert entry["status"] == "CLOSED"
    assert entry["after_outcome"]["result"] == "PASS"
    assert [result["id"] for result in entry["tests_and_validators"]] == [
        "closeout_package_in_memory",
        "epic038_current_state",
    ]
    assert all(
        result["result"] == "PASS" and result["exit_code"] == 0
        for result in entry["tests_and_validators"]
    )
    manifest = json.loads(package[closeout.CLOSE_MANIFEST_PATH])
    assert manifest["decision"] == "NOT SATISFIED"
    assert {
        token
        for token, status in manifest["token_status"].items()
        if status == "UNCLAIMED"
    } == {*closeout.PLANNED_BINDINGS, "RELEASE_ID_RECOMPUTE_OK"}
    assert {
        json.loads(package[path])["result"]
        for path in (
            closeout.PRECOMMIT_CHECKLIST_PATH,
            closeout.POSTCOMMIT_CHECKLIST_PATH,
        )
    } == {"FAIL"}

    closeout._write_package(package)
    _converge_dev02_evidence_graph(root)
    assert_governed_state_present()
    assert _package_at(root) == package
    assert closeout.build_package() == package
    _assert_success(
        _run_repo_tool(
            root,
            "tools/evidence/generate_hde_epic038_closeout.py",
            "--check",
        )
    )
    _assert_success(
        _run_repo_tool(root, "tools/evidence/update_evidence_index.py", "--check")
    )
    _assert_success(
        _run_repo_tool(root, "tools/evidence/orientation_demo.py", "--check")
    )


def test_dev02_close_rejects_already_closed_identity(
    dev02_open_ledger_repo: tuple[Path, str],
) -> None:
    _root, blocker_id = dev02_open_ledger_repo
    request = _dev02_close_request(blocker_id)
    closed_package = closeout.close_blocker(request)
    closeout._write_package(closed_package)
    before = _tree_state(closeout.ROOT)
    with pytest.raises(RuntimeError, match="OPEN|closed|exactly one"):
        closeout.close_blocker(request)
    assert _tree_state(closeout.ROOT) == before


def test_dev02_close_rejects_out_of_scope_regenerated_artifact(
    dev02_open_ledger_repo: tuple[Path, str],
) -> None:
    _root, blocker_id = dev02_open_ledger_repo
    request = _dev02_close_request(
        blocker_id, regenerated_artifacts=("pyproject.toml",)
    )
    before = _tree_state(closeout.ROOT)
    with pytest.raises(RuntimeError, match="permitted|scope"):
        closeout.close_blocker(request)
    assert _tree_state(closeout.ROOT) == before


def test_dev02_close_rejects_validator_failure_without_persistence(
    dev02_open_ledger_repo: tuple[Path, str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _root, blocker_id = dev02_open_ledger_repo

    def fail_validator(
        validator_id: str,
        package: Mapping[str, bytes] | None = None,
    ) -> dict[str, object]:
        raise ValueError(f"validator failed: {validator_id}")

    monkeypatch.setattr(closeout, "run_registered_validator", fail_validator)
    before = _tree_state(closeout.ROOT)
    with pytest.raises(ValueError, match="validator failed"):
        closeout.close_blocker(_dev02_close_request(blocker_id))
    assert _tree_state(closeout.ROOT) == before


@pytest.mark.parametrize(
    "posture", ("PO_AUTHORIZATION_REQUIRED", "PO_AUTHORIZED_EVIDENCE_BOUND")
)
def test_dev02_close_rejects_unauthorized_external_posture(
    dev02_open_ledger_repo: tuple[Path, str],
    posture: str,
) -> None:
    _root, blocker_id = dev02_open_ledger_repo
    before = _tree_state(closeout.ROOT)
    with pytest.raises(RuntimeError, match="authorization|external|posture"):
        closeout.close_blocker(
            _dev02_close_request(
                blocker_id, external_action_posture=posture
            )
        )
    assert _tree_state(closeout.ROOT) == before


def test_dev02_in_memory_validator_really_calls_package_validation(
    dev02_valid_package: Mapping[str, bytes],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[Mapping[str, bytes]] = []

    def observe(package: Mapping[str, bytes]) -> None:
        calls.append(package)
        raise ValueError("injected real package validation failure")

    monkeypatch.setattr(closeout, "validate_package", observe)
    with pytest.raises(ValueError, match="real package validation failure"):
        closeout.run_registered_validator(
            "closeout_package_in_memory", package=dev02_valid_package
        )
    assert calls == [dev02_valid_package]
