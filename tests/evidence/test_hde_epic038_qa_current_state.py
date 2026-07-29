from __future__ import annotations

import datetime as dt
import hashlib
import json
from pathlib import Path

import pytest

from tools.evidence import check_hde_epic038_qa_current_state as current


def _write_proof(root: Path, manifest: Path, proof: Path) -> None:
    raw = manifest.read_bytes()
    timestamp = dt.datetime(2026, 7, 28, tzinfo=dt.timezone.utc).isoformat().replace(
        "+00:00", "Z"
    )
    proof.write_text(
        "\n".join(
            (
                f"path: {manifest.relative_to(root).as_posix()}",
                f"sha256: {hashlib.sha256(raw).hexdigest()}",
                f"size_bytes: {len(raw)}",
                f"mtime_utc: {timestamp}",
                f"produced_at_utc: {timestamp}",
                "",
            )
        ),
        encoding="utf-8",
    )


def _summary_for_state(*, finalized: bool) -> str:
    lines = current.SUMMARY_PATH.read_text(encoding="utf-8").splitlines()
    lines = [
        line
        for line in lines
        if not line.startswith("- epic-wide qa_step_logs_manifest lookup: ")
    ]

    def replace_line(prefix: str, replacement: str) -> None:
        matches = [index for index, line in enumerate(lines) if line.startswith(prefix)]
        assert len(matches) == 1
        lines[matches[0]] = replacement

    if finalized:
        replace_line(
            "- Epic-wide finalization command: ",
            "- Epic-wide finalization command: qa_closeout finalize.",
        )
        replace_line(
            "- Epic-wide lookup status: ", "- Epic-wide lookup status: PASS."
        )
        lookup_hits = json.dumps(
            {
                "Human Evidence Index": True,
                "Machine Mirror": True,
                "canonical evidence updater/source": True,
            },
            sort_keys=True,
        )
        replace_line(
            "- Epic-wide lookup detail: ",
            f"- Epic-wide lookup detail: updater_exit=0; lookup_hits={lookup_hits}.",
        )
        replace_line(
            "- Epic-wide routing receipt: ",
            "- Epic-wide routing receipt: PR#999@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.",
        )
    else:
        live_findings_index = lines.index("## PF-Canon mapping") - 1
        lines.insert(
            live_findings_index,
            "- epic-wide qa_step_logs_manifest lookup: TOOLING_BLOCKED",
        )
        replace_line(
            "- Epic-wide finalization command: ",
            "- Epic-wide finalization command: NOT RUN.",
        )
        replace_line(
            "- Epic-wide lookup status: ",
            "- Epic-wide lookup status: TOOLING_BLOCKED.",
        )
        replace_line(
            "- Epic-wide lookup detail: ",
            "- Epic-wide lookup detail: approved PR routing and required companion refresh pending.",
        )
        replace_line(
            "- Epic-wide routing receipt: ",
            "- Epic-wide routing receipt: NONE.",
        )
    replace_line(
        "- Repo-supported completion: ",
        "- Repo-supported completion: NOT READY.",
    )
    return "\n".join(lines) + "\n"


def _validate_summary_text(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    text: str,
    coverage: list[tuple[str, str, str | None]] | None = None,
) -> str:
    summary = tmp_path / "qa_rca_doc_delta_summary.md"
    summary.write_text(text, encoding="utf-8")
    monkeypatch.setattr(current, "SUMMARY_PATH", summary)
    if coverage is None:
        _, coverage = current.build_expected_manifest()
    return current.validate_summary(coverage)


def test_current_epic038_qa_state_is_complete_and_coherent():
    current.validate_current_state()


def test_current_manifest_has_the_accepted_qa08_binding():
    manifest, coverage, proof = current.validate_manifest_and_proof()
    current_primary_logs = tuple(
        (current.QA_ROOT / "checks").glob("*/primary.log")
    )

    assert len(manifest) == len(current_primary_logs)
    assert proof["sha256"] == hashlib.sha256(current.MANIFEST_PATH.read_bytes()).hexdigest()
    assert manifest[current.QA08_ID] == {
        "check_id": current.QA08_ID,
        "log_path": "checks/qa-08-po-008/primary.log",
        "sha256": current.QA08_PRIMARY_SHA256,
        "size_bytes": current.QA08_PRIMARY_SIZE,
        "status": "PASS",
    }
    assert coverage[8] == (
        current.QA08_ID,
        "PASS",
        "checks/qa-08-po-008/primary.log",
    )


def test_manifest_omission_fails_even_with_a_matching_path_proof(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    manifest, _ = current.build_expected_manifest()
    manifest.pop(current.QA08_ID)
    manifest_path = tmp_path / "qa_step_logs_manifest.json"
    proof_path = tmp_path / "qa_step_logs_manifest.json.path_proof.txt"
    manifest_path.write_bytes(current._canonical_json_bytes(manifest))
    _write_proof(tmp_path, manifest_path, proof_path)
    monkeypatch.setattr(current, "ROOT", tmp_path)

    with pytest.raises(
        current.CurrentStateError,
        match="manifest does not match every current primary log",
    ):
        current.validate_manifest_and_proof(
            current.QA_ROOT, manifest_path, proof_path
        )


def test_duplicate_manifest_key_is_rejected(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    manifest_path = tmp_path / "qa_step_logs_manifest.json"
    proof_path = tmp_path / "qa_step_logs_manifest.json.path_proof.txt"
    manifest_path.write_text(
        '{"qa-08-po-008":{},"qa-08-po-008":{}}\n', encoding="utf-8"
    )
    _write_proof(tmp_path, manifest_path, proof_path)
    monkeypatch.setattr(current, "ROOT", tmp_path)

    with pytest.raises(current.CurrentStateError, match="duplicate JSON key"):
        current.validate_manifest_and_proof(
            current.QA_ROOT, manifest_path, proof_path
        )


def test_checker_is_read_only():
    paths = (
        current.MANIFEST_PATH,
        current.PROOF_PATH,
        current.SUMMARY_PATH,
        current.LIVE_PROOF_PATH,
        current.LIVE_PROOF_PATH_PROOF,
        current.HUMAN_INDEX_PATH,
        current.MIRROR_PATH,
    )
    before = {path: path.read_bytes() for path in paths}

    current.validate_current_state()

    assert {path: path.read_bytes() for path in paths} == before


def test_index_owner_and_companions_have_one_manifest_row():
    _, _, proof = current.validate_manifest_and_proof()
    current.validate_index_binding(proof)

    human = json.loads(current.HUMAN_INDEX_PATH.read_text(encoding="utf-8"))
    mirror = [
        json.loads(line)
        for line in current.MIRROR_PATH.read_text(encoding="utf-8").splitlines()
        if line
    ]
    assert len(current._matching_rows(human)) == 1
    assert len(current._matching_rows(mirror)) == 1
    live_human = current._matching_rows(
        human,
        artifact_key=current.LIVE_PROOF_KEY,
        path=current.LIVE_PROOF_REL,
    )
    live_mirror = current._matching_rows(
        mirror,
        artifact_key=current.LIVE_PROOF_KEY,
        path=current.LIVE_PROOF_REL,
    )
    assert live_human[0]["produced_at_utc"] == current.LIVE_PROOF_PRODUCED_AT_UTC
    assert live_mirror[0]["produced_at_utc"] == current.LIVE_PROOF_PRODUCED_AT_UTC


def test_accepted_live_proof_is_immutable_and_semantically_validated(tmp_path: Path):
    proof = current.validate_live_proof()
    assert proof["requests_attempted"] == 2
    assert proof["requests_completed"] == 2
    assert proof["top_level_pass"] is True

    drifted = json.loads(current.LIVE_PROOF_PATH.read_text(encoding="utf-8"))
    drifted["generated_at_utc"] = "2026-07-27T23:38:10Z"
    drift_path = tmp_path / "open_rails_vendor_abba.json"
    drift_path.write_bytes(current._canonical_json_bytes(drifted))
    with pytest.raises(
        current.CurrentStateError,
        match="accepted qa-08-po-008 live proof changed",
    ):
        current.validate_live_proof(
            drift_path, semantic_check=False
        )


def test_live_proof_path_proof_is_required_and_exact(tmp_path: Path):
    invalid_proof = tmp_path / "open_rails_vendor_abba.json.path_proof.txt"
    invalid_proof.write_text(
        current.LIVE_PROOF_PATH_PROOF.read_text(encoding="utf-8").replace(
            current.LIVE_PROOF_SHA256,
            "0" * 64,
        ),
        encoding="utf-8",
    )
    with pytest.raises(
        current.CurrentStateError,
        match="live path-proof binding is stale",
    ):
        current.validate_live_proof(
            proof_path=invalid_proof,
            semantic_check=False,
        )


def test_finalized_current_state_can_remain_epic_not_ready(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _, coverage = current.build_expected_manifest()
    incomplete_check = current.CHECK_IDS[-1]
    assert coverage[-1] == (
        incomplete_check,
        "PASS",
        f"checks/{incomplete_check}/primary.log",
    )
    incomplete_coverage = list(coverage)
    incomplete_coverage[-1] = (incomplete_check, "NOT RUN", None)

    summary = _summary_for_state(finalized=True)
    summary = summary.replace(
        f"| {incomplete_check} | PASS | checks/{incomplete_check}/primary.log |",
        f"| {incomplete_check} | NOT RUN | Unknown |",
    )
    assert "- Repo-supported completion: NOT READY." in summary
    assert (
        _validate_summary_text(
            tmp_path,
            monkeypatch,
            summary,
            coverage=incomplete_coverage,
        )
        == "PASS"
    )
    monkeypatch.setattr(
        current,
        "validate_manifest_and_proof",
        lambda: ({}, incomplete_coverage, {}),
    )
    monkeypatch.setattr(current, "validate_live_proof", lambda: {})
    monkeypatch.setattr(current, "validate_index_binding", lambda _proof: None)
    current.validate_current_state(require_finalized=True)


def test_require_finalized_rejects_generation_state(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    summary = _summary_for_state(finalized=False)
    _validate_summary_text(tmp_path, monkeypatch, summary)
    with pytest.raises(
        current.CurrentStateError,
        match="current-state ledger is not finalized",
    ):
        current.validate_current_state(require_finalized=True)


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        (
            lambda text: text + "- Step status: NOT RUN.\n",
            "expected one summary line",
        ),
        (
            lambda text: text + "- Finalization command: NOT RUN.\n",
            "legacy unscoped state line",
        ),
        (
            lambda text: text.replace(
                "- Epic-wide routing receipt: PR#999@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.",
                "- Epic-wide routing receipt: NONE.",
            ),
            "finalized summary routing is incoherent",
        ),
        (
            lambda text: text.replace(
                "- Epic-wide routing receipt: PR#999@aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa.",
                "- Epic-wide routing receipt: PR#999@not-a-merge-sha.",
            ),
            "finalized summary routing is incoherent",
        ),
        (
            lambda text: text.replace(
                "lookup_hits={\"Human Evidence Index\": true, \"Machine Mirror\": true, \"canonical evidence updater/source\": true}",
                "lookup_hits={\"Human Evidence Index\": true}",
            ),
            "lookup detail is incomplete",
        ),
        (
            lambda text: text + "- Repo-supported completion: READY FOR CLOSEOUT REVIEW.\n",
            "completion state is stale",
        ),
        (
            lambda text: text.replace(
                "- Epic-wide generation command: qa_closeout generation.",
                "- Epic-wide generation command: NOT RUN.",
            ),
            "generation command is stale",
        ),
        (
            lambda text: text.replace(
                "- Required routing type: PR.",
                "- Required routing type: OPS.",
            ),
            "required routing type is stale",
        ),
        (
            lambda text: text
            + "- No completed qa-08-po-008 Extended Moon Loop is claimed by this summary.\n",
            "Extended Moon Loop posture is contradictory",
        ),
        (
            lambda text: text.replace(
                "- Canon-drain completion: NOT CLAIMED.",
                "- Canon-drain completion: CLAIMED.",
            ),
            "canon-drain nonclaim is stale",
        ),
        (
            lambda text: text.replace(
                "- Formal close-pack completion: NOT CLAIMED.",
                "- Formal close-pack completion: CLAIMED.",
            ),
            "close-pack nonclaim is stale",
        ),
        (
            lambda text: text + "- qa-08-po-008: NOT RUN.\n",
            "summary contradicts qa-08 PASS",
        ),
    ),
)
def test_summary_rejects_contradictory_or_fabricated_finalized_state(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mutation,
    message: str,
):
    summary = mutation(_summary_for_state(finalized=True))
    with pytest.raises(current.CurrentStateError, match=message):
        _validate_summary_text(tmp_path, monkeypatch, summary)


def test_duplicate_artifact_key_at_another_path_is_rejected():
    rows = [
        {
            "artifact_key": current.MANIFEST_KEY,
            "discovered_physical_path": current.MANIFEST_REL,
        },
        {
            "artifact_key": current.MANIFEST_KEY,
            "discovered_physical_path": "audit/qa/hde-epic038/wrong.json",
        },
    ]
    assert current._matching_rows(rows) == []


def test_plan_permitted_none_pre_routing_receipt_is_accepted(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    summary = _summary_for_state(finalized=False).replace(
        "- Epic-wide pre-routing blocked or failed receipt: REMEDIATION_NEEDED_F-001.",
        "- Epic-wide pre-routing blocked or failed receipt: NONE.",
    )
    assert _validate_summary_text(tmp_path, monkeypatch, summary) == "TOOLING_BLOCKED"


def test_plan_closeout_wrapper_forces_closed_rails_and_pr_receipt_shape():
    plan = (current.ROOT / "docs/qa/r7-qa-plan-hde-epic038.md").read_text(
        encoding="utf-8"
    )
    for required in (
        "-u QA08_AUTHORIZATION_CONFIRMATION",
        "-u QA08_PO_EVENT_RECEIPT",
        "SAFE_MODE=1",
        "ALLOW_NETWORK=0",
        're.fullmatch(r"PR#[1-9][0-9]*@[0-9a-f]{40}", routing_receipt)',
    ):
        assert required in plan
