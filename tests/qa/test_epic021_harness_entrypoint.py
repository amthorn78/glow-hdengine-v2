import json
from pathlib import Path

import pytest

from tools.qa import epic021_qa
from tools.evidence import run_sanity_pipeline
from tools.qa.epic021_qa import run_epic021_qa
from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check


def _repo(root: Path) -> None:
    (root / "docs/pfcanon").mkdir(parents=True)
    (root / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md").write_text(
        "## **2.0 Acceptance Tokens (single-home roster)**\n"
        "* **QA_HARNESS_DISCIPLINE_OK** — registered.\n"
        "## **2.1 Next**\n",
        encoding="utf-8",
    )
    (root / "docs").mkdir(exist_ok=True)
    (root / "docs/acceptance_map_epic021.json").write_text(
        json.dumps(
            {
                "epic_id": "HDE-EPIC021",
                "tokens": [
                    {
                        "evidence_titles": ["proof.txt"],
                        "name": "QA_HARNESS_DISCIPLINE_OK",
                        "owner_pf": "PF04",
                        "status": "implemented",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    qa = root / "audit/qa/hde-epic021"
    qa.mkdir(parents=True)
    (root / "proof.txt").write_text("proof\n", encoding="utf-8")
    (qa / "token_evidence_matrix.md").write_text(
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        "| QA_HARNESS_DISCIPLINE_OK | PF04 | proof.txt | "
        "python -m pytest -q tests/qa/test_epic021_scaffolding.py | "
        "checks/d00-bootstrap/primary.log | Implemented | fixture |\n",
        encoding="utf-8",
    )
    tests = root / "tests/qa"
    tests.mkdir(parents=True)
    (tests / "test_epic021_scaffolding.py").write_text(
        "def test_scaffold():\n    assert True\n", encoding="utf-8"
    )


def test_wrapper_delegates_to_current_state_harness(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _repo(tmp_path)

    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    result = run_epic021_qa(repo_root=tmp_path)
    assert result["bootstrap"].status is Status.PASS
    assert result["viability"].status is Status.PASS
    manifest = json.loads(
        (
            tmp_path / "audit/qa/hde-epic021/qa_step_logs_manifest.json"
        ).read_text()
    )
    assert set(manifest) == {"d00-bootstrap", "acceptance-map-viability"}
    assert "run_id" not in json.dumps(manifest)
    ledger = tmp_path / "audit/qa/hde-epic021/acceptance_map_viability.log"
    assert result["governed_ledger"] == ledger
    assert result["viability"].governed_ledger == ledger
    assert json.loads(ledger.read_text(encoding="utf-8"))["status"] == "PASS"


def test_wrapper_never_creates_checkout_qa_files(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _repo(tmp_path)
    before = {
        path.as_posix() for path in Path("audit/qa").rglob("*") if path.is_file()
    }

    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    run_epic021_qa(repo_root=tmp_path)
    after = {
        path.as_posix() for path in Path("audit/qa").rglob("*") if path.is_file()
    }
    assert after == before


def test_outer_transaction_restores_bytes_modes_and_new_targets(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    existing = tmp_path / "existing.log"
    created = tmp_path / "nested/new.log"
    existing.write_bytes(b"before\n")
    existing.chmod(0o640)
    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)
    monkeypatch.setattr(
        epic021_qa, "_wrapper_write_paths", lambda: (existing, created)
    )

    with pytest.raises(RuntimeError, match="injected"):
        with epic021_qa._WrapperWriteTransaction():
            existing.write_bytes(b"after\n")
            existing.chmod(0o600)
            created.parent.mkdir(parents=True)
            created.write_bytes(b"new\n")
            raise RuntimeError("injected")

    assert existing.read_bytes() == b"before\n"
    assert existing.stat().st_mode & 0o777 == 0o640
    assert not created.exists()
    assert not created.parent.exists()


def _legacy_bootstrap_binding(root: Path) -> tuple[HarnessConfig, Path, Path]:
    config = HarnessConfig("HDE-EPIC021", repo_root=root)
    relative = "audit/qa/hde-epic021/checks/D00_bootstrap/primary.log"
    primary, _ = record_check(
        config,
        CheckResult(
            "D00_bootstrap",
            Status.PASS,
            command=("python", "-V"),
            command_provenance="test fixture",
            exit_code=0,
            evidence_artifacts=(relative,),
        ),
    )
    proof = primary.with_name("primary.log.path_proof.txt")
    proof.write_bytes(b"historical proof\n")
    return config, primary, proof


def test_legacy_bootstrap_binding_is_superseded_idempotently_without_rewrite(
    tmp_path: Path,
):
    config, primary, proof = _legacy_bootstrap_binding(tmp_path)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    primary_before = primary.read_bytes()
    proof_before = proof.read_bytes()

    epic021_qa._supersede_legacy_bootstrap_manifest(config)
    first_manifest = manifest.read_bytes()
    epic021_qa._supersede_legacy_bootstrap_manifest(config)

    assert json.loads(first_manifest) == {}
    assert manifest.read_bytes() == first_manifest
    assert primary.read_bytes() == primary_before
    assert proof.read_bytes() == proof_before


def test_wrapper_replaces_legacy_binding_but_preserves_historical_bytes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    _repo(tmp_path)
    _, primary, proof = _legacy_bootstrap_binding(tmp_path)
    primary_before = primary.read_bytes()
    proof_before = proof.read_bytes()

    class Done:
        returncode = 0
        stdout = "passed"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    run_epic021_qa(repo_root=tmp_path)

    manifest = json.loads(
        (
            tmp_path / "audit/qa/hde-epic021/qa_step_logs_manifest.json"
        ).read_text(encoding="utf-8")
    )
    assert set(manifest) == {"d00-bootstrap", "acceptance-map-viability"}
    assert primary.read_bytes() == primary_before
    assert proof.read_bytes() == proof_before


def test_legacy_bootstrap_supersession_rolls_back_with_outer_transaction(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    config, primary, proof = _legacy_bootstrap_binding(tmp_path)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    before = {
        path: path.read_bytes()
        for path in (manifest, primary, proof)
    }
    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)
    monkeypatch.setattr(
        epic021_qa,
        "_wrapper_write_paths",
        lambda: (manifest, primary, proof),
    )

    with pytest.raises(RuntimeError, match="injected"):
        with epic021_qa._WrapperWriteTransaction():
            epic021_qa._supersede_legacy_bootstrap_manifest(config)
            raise RuntimeError("injected")

    assert {path: path.read_bytes() for path in before} == before


def test_legacy_bootstrap_supersession_rejects_dual_current_authority(
    tmp_path: Path,
):
    config, _, _ = _legacy_bootstrap_binding(tmp_path)
    record_check(
        config,
        CheckResult(
            "d00-bootstrap",
            Status.PASS,
            command=("python", "-V"),
            command_provenance="test fixture",
            exit_code=0,
            evidence_artifacts=(
                "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log",
            ),
        ),
    )

    with pytest.raises(RuntimeError, match="EPIC021_BOOTSTRAP_DUAL_CURRENT_BINDING"):
        epic021_qa._supersede_legacy_bootstrap_manifest(config)


def test_main_rolls_back_input_writes_when_finalization_fails(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
):
    first = tmp_path / "acceptance.json"
    second = tmp_path / "matrix.md"
    first.write_bytes(b"old acceptance\n")
    second.write_bytes(b"old matrix\n")
    monkeypatch.setattr(epic021_qa, "ROOT", tmp_path)
    monkeypatch.setattr(
        epic021_qa, "_wrapper_write_paths", lambda: (first, second)
    )
    monkeypatch.setattr(epic021_qa, "ensure_determinism_env", lambda **_kwargs: None)

    def write_inputs() -> None:
        first.write_bytes(b"new acceptance\n")
        second.write_bytes(b"new matrix\n")

    monkeypatch.setattr(epic021_qa, "_write_acceptance_inputs", write_inputs)
    monkeypatch.setattr(epic021_qa, "_write_close_pack", lambda _timestamp: None)
    monkeypatch.setattr(
        epic021_qa,
        "_execute_current_family",
        lambda: (_ for _ in ()).throw(RuntimeError("updater failed")),
    )

    assert epic021_qa.main() == 1
    assert first.read_bytes() == b"old acceptance\n"
    assert second.read_bytes() == b"old matrix\n"


def test_controlled_tooling_probe_uses_actual_pytest_cause():
    result = epic021_qa._tooling_classification_result()
    assert result.status is Status.PASS
    assert result.exit_code == 0
    assert len(result.command) == 2
    assert result.command[0][-1] == epic021_qa.TOOLING_CLASSIFICATION_FIXTURE
    assert "ModuleNotFoundError" in result.output
    assert "_epic021_deliberately_missing_dependency" in result.output
    assert "summary:FAIL_TOOLING" in epic021_qa.CONTROLLED_TOOLING_FAILURE_CONTENT
    assert (
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC"
        in epic021_qa.CONTROLLED_TOOLING_FAILURE_CONTENT
    )


def test_precommit_env_pin_failure_is_tooling_causal(
    monkeypatch: pytest.MonkeyPatch,
):
    receipt = epic021_qa._CommandReceipt(
        epic021_qa.PRECOMMIT_COMMANDS[0],
        1,
        "",
        "mismatched rail",
    )
    monkeypatch.setattr(epic021_qa, "_run_commands", lambda *_args, **_kwargs: (receipt,))
    result = epic021_qa._precommit_result()
    assert result.status is Status.FAIL_TOOLING
    assert result.status_reason == "environment-pins gate failed"


def test_main_rejects_open_rails_before_any_write(monkeypatch: pytest.MonkeyPatch):
    writes: list[str] = []
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setattr(
        epic021_qa,
        "_write_acceptance_inputs",
        lambda: writes.append("inputs"),
    )
    assert epic021_qa.main() == 1
    assert writes == []


def test_transient_narrative_mounts_are_removed(tmp_path: Path):
    catalog = tmp_path / "catalog/narratives"
    catalog.mkdir(parents=True)
    (catalog / "manifest.json").write_text("{}\n", encoding="utf-8")
    (catalog / "manifest.json.sha256").write_text("digest\n", encoding="utf-8")
    mount_root = tmp_path / "narratives"
    mount_root.mkdir()
    retained = mount_root / ("a" * 64)
    retained.mkdir()

    with epic021_qa._TransientNarrativeMounts(tmp_path):
        created = mount_root / ("b" * 64)
        created.mkdir()
        (created / "manifest.json").write_text("{}\n", encoding="utf-8")
        (created / "manifest.json.sha256").write_text(
            "digest\n", encoding="utf-8"
        )

    assert retained.is_dir()
    assert not created.exists()


def test_sanity_failure_is_behavior_causal_but_malformed_is_tooling():
    failure = run_sanity_pipeline.STAGE_NAMES[2]
    results = []
    for index, name in enumerate(run_sanity_pipeline.STAGE_NAMES):
        if index < 2:
            status = "OK"
        elif index == 2:
            status = "FAIL"
        else:
            status = f"NOT_EXECUTED_EARLIER_FAILURE:{failure}"
        results.append((name, status))
    payload = run_sanity_pipeline._render_log(results, failure, "FAIL")

    status, reason = epic021_qa._sanity_status(payload)
    assert status is Status.FAIL_BEHAVIOR
    assert failure in reason
    assert epic021_qa._sanity_status(None)[0] is Status.FAIL_TOOLING
    assert epic021_qa._sanity_status(b"malformed\n")[0] is Status.FAIL_TOOLING


def test_close_pack_names_required_rails_and_same_run_receipts():
    captured_at = "2026-08-18T00:00:00Z"
    manifest = json.loads(epic021_qa._close_manifest_content(captured_at))
    report = epic021_qa._close_report_content(captured_at)

    assert "## Acceptance and evidence pointers" in report
    assert "## QA Rails — Open/Close (Final PR)" in report
    expected_logs = {
        "qa_log_acceptance_map_viability": (
            "audit/qa/hde-epic021/checks/acceptance-map-viability/primary.log"
        ),
        "qa_log_bootstrap": (
            "audit/qa/hde-epic021/checks/d00-bootstrap/primary.log"
        ),
        "qa_log_bootstrap_tooling_classification": (
            "audit/qa/hde-epic021/checks/"
            "bootstrap-tooling-classification/primary.log"
        ),
        "qa_log_live_qa": (
            "audit/qa/hde-epic021/checks/po-epic021-live-qa/primary.log"
        ),
        "qa_log_postcommit": (
            "audit/qa/hde-epic021/checks/po-postcommit/primary.log"
        ),
        "qa_log_precommit": (
            "audit/qa/hde-epic021/checks/po-precommit/primary.log"
        ),
    }
    assert {
        key: manifest["key_outputs"][key] for key in expected_logs
    } == expected_logs
