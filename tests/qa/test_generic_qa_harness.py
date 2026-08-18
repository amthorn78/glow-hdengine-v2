import json
import sys
from pathlib import Path

import pytest

from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    Status,
    generate_acceptance_map_viability,
    read_primary_header,
    record_check,
    run_pytest_check,
    summarize_checks,
    update_manifest,
)


@pytest.fixture
def repository(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    for key, value in {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC", "APP_ENV": "test"}.items():
        monkeypatch.setenv(key, value)
    (tmp_path / "docs/pfcanon").mkdir(parents=True)
    (tmp_path / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md").write_text(
        "## **2.0 Acceptance Tokens (single-home roster)**\n"
        "* **QA\\_HARNESS\\_DISCIPLINE\\_OK** — bullet declaration.\n"
        "**QA\\_HARNESS\\_ENTRYPOINT\\_SELFTEST\\_OK** — standalone declaration.\n"
        "* **`HYPHEN-TOKEN_OK`** — bold-code declaration.\n"
        "* **IN_BOLD_DASH_OK — in-bold declaration.**\n"
        "`RETIRED_PROSE_OK` is a retired non-token label only.\n"
        "QA_HARNESS_DISCIPLINE_OK appears again in explanatory prose.\n"
        "* **QA\\_HARNESS\\_DISCIPLINE\\_OK** — legitimate repeated declaration.\n"
        "## **2.1 Next**\n",
        encoding="utf-8",
    )
    (tmp_path / "evidence").mkdir()
    (tmp_path / "evidence/proof.json").write_text('{"ok":true}\n', encoding="utf-8")
    config = HarnessConfig("HDE-EPIC039", repo_root=tmp_path)
    config.acceptance_map_path.parent.mkdir(exist_ok=True)
    config.acceptance_map_path.write_text(json.dumps({"epic_id": "HDE-EPIC039", "tokens": [{"name": "QA_HARNESS_DISCIPLINE_OK"}]}), encoding="utf-8")
    config.token_matrix_path.parent.mkdir(parents=True)
    config.token_matrix_path.write_text("| token_name | owner | evidence_artifacts |\n| --- | --- | --- |\n| QA_HARNESS_DISCIPLINE_OK | PF04 | evidence/proof.json |\n", encoding="utf-8")
    return tmp_path


def test_config_derives_canonical_paths(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    assert config.qa_root == repository / "audit/qa/hde-epic039"
    assert config.acceptance_map_path == repository / "docs/acceptance_map_epic039.json"
    assert config.token_matrix_path == config.qa_root / "token_evidence_matrix.md"
    with pytest.raises(ValueError):
        HarnessConfig("hde-epic039", repo_root=repository)


def test_exact_status_set_and_causal_rollup():
    assert {status.value for status in Status} == {"PASS", "FAIL_BEHAVIOR", "FAIL_TOOLING", "TOOLING_BLOCKED", "PARKED"}
    assert summarize_checks([CheckResult("ok", Status.PASS)]) is Status.PASS
    assert summarize_checks([CheckResult("parked", Status.PARKED, "authorized deferral")]) is Status.PARKED
    assert summarize_checks([CheckResult("blocked", Status.TOOLING_BLOCKED, "missing")]) is Status.TOOLING_BLOCKED
    with pytest.raises(ValueError):
        CheckResult("bad", "SUCCESS")


@pytest.mark.parametrize("check_id", ["", "..", "a/b", "a\\b", "/absolute"])
def test_unsafe_check_ids_are_rejected(repository: Path, check_id: str):
    with pytest.raises(ValueError):
        CheckResult(check_id, Status.PASS, exit_code=0)


def test_pf27_header_and_manifest_replace_by_check_id(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    first = CheckResult("selftest", Status.PASS, exit_code=0, command=("true",), command_provenance="test fixture")
    log, manifest = record_check(config, first)
    header = read_primary_header(log)
    assert header["schema_version"] == "pf27.step_log_header.v2"
    assert header["claimed_tokens"] == []
    assert header["evidence_artifacts"] == ["audit/qa/hde-epic039/checks/selftest/primary.log"]
    second = CheckResult("selftest", Status.FAIL_BEHAVIOR, "contradiction", exit_code=1, command=("false",), command_provenance="test fixture")
    update_manifest(config, record_check(config, second)[0])
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    assert list(payload["checks"]) == ["selftest"]
    assert payload["checks"]["selftest"]["status"] == "FAIL_BEHAVIOR"
    assert "run_id" not in manifest.read_text(encoding="utf-8")


def test_same_interpreter_and_classification(repository: Path, monkeypatch: pytest.MonkeyPatch):
    test_file = repository / "test_sample.py"
    test_file.write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    calls = []
    class Done:
        returncode = 0
        stdout = "ok"
        stderr = ""
    def fake_run(command, **kwargs):
        calls.append(tuple(command)); return Done()
    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result = run_pytest_check(HarnessConfig("HDE-EPIC039", repo_root=repository), "pytest", ("-q", "test_sample.py"))
    assert calls[0] == (sys.executable, "-m", "pytest", "--version")
    assert result.command[:3] == (sys.executable, "-m", "pytest")
    assert result.status is Status.PASS
    missing = run_pytest_check(HarnessConfig("HDE-EPIC039", repo_root=repository), "missing", ("missing.py",))
    assert missing.status is Status.TOOLING_BLOCKED


def test_viability_passes_exact_and_legacy_single_path(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    assert generate_acceptance_map_viability(config).status is Status.PASS
    config.token_matrix_path.write_text("| token_name | owner | evidence_artifacts |\n| --- | --- | --- |\n| QA_HARNESS_DISCIPLINE_OK | PF04 | Proof title (`evidence/proof.json`) |\n", encoding="utf-8")
    result = generate_acceptance_map_viability(config)
    assert result.status is Status.PASS
    assert result.primary_log and result.primary_log.stat().st_size > 0
    manifest = json.loads(result.manifest.read_text(encoding="utf-8"))
    assert list(manifest["checks"]).count("acceptance-map-viability") == 1


def test_pf04_declaration_forms_ignore_explanatory_prose(repository: Path):
    from tools.qa.qa_harness import _governance_tokens

    tokens, error = _governance_tokens(HarnessConfig("HDE-EPIC039", repo_root=repository))
    assert error == ""
    assert tokens == {
        "QA_HARNESS_DISCIPLINE_OK",
        "QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
        "HYPHEN-TOKEN_OK",
        "IN_BOLD_DASH_OK",
    }


def test_viability_validates_each_semicolon_delimited_reference(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    (repository / "evidence/second.txt").write_text("second\n", encoding="utf-8")
    config.token_matrix_path.write_text(
        "| token_name | owner | evidence_artifacts |\n| --- | --- | --- |\n"
        "| QA_HARNESS_DISCIPLINE_OK | PF04 | evidence/proof.json; Proof (`evidence/second.txt`) |\n",
        encoding="utf-8",
    )
    assert generate_acceptance_map_viability(config).status is Status.PASS
    config.token_matrix_path.write_text(
        config.token_matrix_path.read_text(encoding="utf-8").replace("; Proof", "; ; Proof"),
        encoding="utf-8",
    )
    assert generate_acceptance_map_viability(config).status is Status.FAIL_TOOLING


def test_generator_only_viability_ledger_matches_primary_evaluation(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    result = generate_acceptance_map_viability(config, publish_governed_ledger=True)
    assert result.status is Status.PASS
    assert result.governed_ledger == config.viability_ledger_path
    ledger = json.loads(result.governed_ledger.read_text(encoding="utf-8"))
    primary_evaluation = json.loads(result.primary_log.read_text(encoding="utf-8").splitlines()[1])
    assert ledger == primary_evaluation


@pytest.mark.parametrize("reference", ["../escape.txt", "/tmp/absolute", "no path prose", "evidence/proof.json and evidence/other.json", "evidence/empty.txt", "evidence/bad.json"])
def test_viability_rejects_bad_references(repository: Path, reference: str):
    (repository / "evidence/other.json").write_text('{"ok":true}', encoding="utf-8")
    (repository / "evidence/empty.txt").write_text("", encoding="utf-8")
    (repository / "evidence/bad.json").write_text("{", encoding="utf-8")
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    config.token_matrix_path.write_text(f"| token_name | owner | evidence_artifacts |\n| --- | --- | --- |\n| QA_HARNESS_DISCIPLINE_OK | PF04 | {reference} |\n", encoding="utf-8")
    assert generate_acceptance_map_viability(config).status is Status.FAIL_BEHAVIOR


def test_viability_duplicate_or_orphan_tokens_fail_behavior(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    data = {"epic_id": "HDE-EPIC039", "tokens": [{"name": "QA_HARNESS_DISCIPLINE_OK"}, {"name": "QA_HARNESS_DISCIPLINE_OK"}]}
    config.acceptance_map_path.write_text(json.dumps(data), encoding="utf-8")
    assert generate_acceptance_map_viability(config).status is Status.FAIL_BEHAVIOR
    data["tokens"] = [{"name": "QA_HARNESS_DISCIPLINE_OK"}]
    config.acceptance_map_path.write_text(json.dumps(data), encoding="utf-8")
    config.token_matrix_path.write_text(config.token_matrix_path.read_text() + "| QA_HARNESS_ENTRYPOINT_SELFTEST_OK | PF04 | evidence/proof.json |\n", encoding="utf-8")
    assert generate_acceptance_map_viability(config).status is Status.FAIL_BEHAVIOR


def test_missing_and_malformed_inputs_are_structured(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    config.acceptance_map_path.unlink()
    assert generate_acceptance_map_viability(config).status is Status.TOOLING_BLOCKED
    config.acceptance_map_path.write_text("{", encoding="utf-8")
    assert generate_acceptance_map_viability(config).status is Status.FAIL_TOOLING


def test_writer_failure_is_fail_tooling(repository: Path, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setattr("tools.qa.qa_harness._atomic_write", lambda *_: (_ for _ in ()).throw(OSError("disk")))
    result = generate_acceptance_map_viability(HarnessConfig("HDE-EPIC039", repo_root=repository))
    assert result.status is Status.FAIL_TOOLING
    assert result.primary_log is None


def test_legacy_manifest_is_replaced_without_importing_run_state(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    historical = config.qa_root / "legacy-run/historical.log"
    historical.parent.mkdir(parents=True)
    historical.write_text("historical bytes\n", encoding="utf-8")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "runs": [{"run_id": "old", "produced_at_utc": "old", "steps": [{"log_path": str(historical), "status": "PASS"}]}]}), encoding="utf-8")
    before = historical.read_bytes()
    record_check(config, CheckResult("current", Status.PASS, exit_code=0, command=("true",), command_provenance="fixture"))
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    assert payload == {"checks": {"current": {"check_id": "current", "log_path": "audit/qa/hde-epic039/checks/current/primary.log", "status": "PASS"}}, "epic_id": config.epic_id}
    assert historical.read_bytes() == before


def test_unknown_manifest_shape_fails_before_primary_log(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "steps": []}), encoding="utf-8")
    with pytest.raises(ValueError, match="unknown QA manifest shape"):
        record_check(config, CheckResult("current", Status.PASS, exit_code=0, command=("true",), command_provenance="fixture"))
    assert not (config.qa_root / "checks/current/primary.log").exists()


def test_publication_rolls_back_when_manifest_write_fails(repository: Path, monkeypatch: pytest.MonkeyPatch):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    original = json.dumps({"epic_id": config.epic_id, "runs": []})
    manifest.write_text(original, encoding="utf-8")
    from tools.qa import qa_harness
    real_write = qa_harness._atomic_write
    calls = 0
    def fail_second(path, content):
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("manifest write failed")
        real_write(path, content)
    monkeypatch.setattr(qa_harness, "_atomic_write", fail_second)
    with pytest.raises(OSError, match="manifest write failed"):
        record_check(config, CheckResult("current", Status.PASS, exit_code=0, command=("true",), command_provenance="fixture"))
    assert manifest.read_text(encoding="utf-8") == original
    assert not (config.qa_root / "checks/current/primary.log").exists()
