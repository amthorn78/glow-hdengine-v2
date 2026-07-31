from __future__ import annotations

import hashlib
import json
import runpy
import subprocess
import sys
from dataclasses import replace
from pathlib import Path

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


def test_planned_rows_are_exact_owned_absent_and_unclaimed() -> None:
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
        assert not (ROOT / path).exists()
        assert not (ROOT / f"{path}.path_proof.txt").exists()

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
    assert workflow.count(f"run: {EXPECTED_DOC_DELTA_CHECK_COMMAND}") == 1
    assert EXPECTED_DOC_DELTA_WRITE_COMMAND not in workflow
    check_line = f"run: {EXPECTED_DOC_DELTA_CHECK_COMMAND}"
    step_name = "      - name: Check HDE-EPIC038 DEV-01 doc-delta pair"
    indented_check = f"        {check_line}"
    explicit_shell = "        shell: bash"
    focused_run = (
        "        run: python -m pytest -q "
        "tests/evidence/test_hde_epic038_closeout.py"
    )
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
        with pytest.raises(ValueError, match="CI command binding mismatch"):
            closeout.validate_doc_delta_ci(changed)


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
        "manifest_sha256": manifest_sha256,
        "release_id": manifest_sha256,
        "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS",
        "pipeline_stop": None,
    }


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
