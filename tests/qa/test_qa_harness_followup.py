import json
from pathlib import Path

import pytest

from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    Status,
    evaluate_acceptance_map_viability,
    read_primary_header,
    record_check,
    record_check_family,
)

MATRIX_HEADER = (
    "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |\n"
    "| --- | --- | --- | --- | --- | --- | --- |\n"
)
TOKEN = "QA_HARNESS_DISCIPLINE_OK"


def _matrix_row(
    evidence: str = "evidence/proof.json",
    *,
    ci: str = "python tools/check.py",
    qa: str = "checks/acceptance-map-viability/primary.log",
    token: str = TOKEN,
) -> str:
    return f"| {token} | PF04 | {evidence} | {ci} | {qa} | Implemented | fixture |\n"


@pytest.fixture
def repository(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    for key, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "APP_ENV": "test",
    }.items():
        monkeypatch.setenv(key, value)
    (tmp_path / "docs/pfcanon").mkdir(parents=True)
    (tmp_path / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md").write_text(
        "## **2.0 Acceptance Tokens (single-home roster)**\n"
        "* **QA\\_HARNESS\\_DISCIPLINE\\_OK** — declared.\n"
        "* **QA\\_HARNESS\\_DISCIPLINE\\_OK** — duplicate declaration is harmless.\n"
        "`RETIRED_PROSE_OK` is not a token.\n"
        "## **2.1 Next**\n",
        encoding="utf-8",
    )
    (tmp_path / "evidence").mkdir()
    (tmp_path / "evidence/proof.json").write_text('{"ok":true}\n', encoding="utf-8")
    (tmp_path / "tools").mkdir()
    (tmp_path / "tools/check.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
    return tmp_path


def _configure(
    root: Path,
    epic_id: str,
    *,
    evidence_titles: tuple[str, ...] = ("evidence/proof.json",),
    evidence: str = "evidence/proof.json",
    ci: str = "python tools/check.py",
    qa: str = "checks/acceptance-map-viability/primary.log",
    step_names: tuple[str, ...] = (),
) -> HarnessConfig:
    config = HarnessConfig(epic_id, repo_root=root, step_names=step_names)
    config.acceptance_map_path.parent.mkdir(parents=True, exist_ok=True)
    config.acceptance_map_path.write_text(
        json.dumps(
            {
                "epic_id": epic_id,
                "tokens": [
                    {
                        "name": TOKEN,
                        "owner_pf": "PF04",
                        "status": "implemented",
                        "evidence_titles": list(evidence_titles),
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    config.token_matrix_path.parent.mkdir(parents=True, exist_ok=True)
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(evidence, ci=ci, qa=qa), encoding="utf-8"
    )
    return config


def _write_v1(config: HarnessConfig, check_id: str, *, status: str = "PASS") -> Path:
    path = config.qa_root / "checks" / check_id / "primary.log"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "schema_version": "pf27.step_log_header.v1",
                "check_id": check_id,
                "status": status,
            },
            sort_keys=True,
        )
        + "\nhistorical body\n",
        encoding="utf-8",
    )
    return path


def _entry(
    config: HarnessConfig, check_id: str, *, full: bool = False
) -> dict[str, str]:
    path = f"checks/{check_id}/primary.log"
    if full:
        path = f"audit/qa/hde-epic{config.epic_number}/{path}"
    return {"check_id": check_id, "log_path": path, "status": "STALE_MANIFEST_VALUE"}


def _pass(check_id: str, *, command=("true",)) -> CheckResult:
    return CheckResult(
        check_id,
        Status.PASS,
        exit_code=0,
        command=command,
        command_provenance="test fixture",
    )


def test_epic027_flat_v1_transition_retains_all_historical_identities(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    check_ids = ("d0_discovery", *(f"po-{index:03d}" for index in range(1, 11)))
    before = {}
    manifest = {}
    for index, check_id in enumerate(check_ids):
        path = _write_v1(config, check_id)
        before[check_id] = path.read_bytes()
        manifest[check_id] = _entry(config, check_id, full=index % 2 == 0)
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )

    record_check(config, _pass("acceptance-map-viability"))

    transitioned = json.loads(
        (config.qa_root / "qa_step_logs_manifest.json").read_text()
    )
    assert set(transitioned) == {*check_ids, "acceptance-map-viability"}
    for check_id in check_ids:
        assert transitioned[check_id] == {
            "check_id": check_id,
            "log_path": f"audit/qa/hde-epic027/checks/{check_id}/primary.log",
            "status": "PASS",
        }
        assert (
            config.qa_root / "checks" / check_id / "primary.log"
        ).read_bytes() == before[check_id]


@pytest.mark.parametrize("schema_version", ["v1", "v2"])
def test_uppercase_legacy_entry_cannot_be_carried_into_current_manifest(
    repository: Path, schema_version: str
):
    config = _configure(repository, "HDE-EPIC027")
    check_id = "D00_legacy"
    if schema_version == "v1":
        primary = _write_v1(config, check_id)
    else:
        relative = f"audit/qa/hde-epic027/checks/{check_id}/primary.log"
        primary = config.repo_root / relative
        primary.parent.mkdir(parents=True)
        primary.write_text(
            json.dumps(
                {
                    "captured_env": {},
                    "check_id": check_id,
                    "check_name": "historical uppercase check",
                    "claimed_tokens": [],
                    "command": ["true"],
                    "command_provenance": "historical test fixture",
                    "evidence_artifacts": [relative],
                    "exit_code": 0,
                    "intended_tokens": [],
                    "pf_refs": [],
                    "schema_version": "pf27.step_log_header.v2",
                    "status": "PASS",
                    "status_reason": "",
                    "timestamp_utc": "2026-08-18T00:00:00Z",
                },
                sort_keys=True,
                separators=(",", ":"),
            )
            + "\n",
            encoding="utf-8",
        )
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    entry = _entry(config, check_id)
    if schema_version == "v2":
        entry["status"] = "PASS"
    manifest.write_text(
        json.dumps({check_id: entry}), encoding="utf-8"
    )
    manifest_before = manifest.read_bytes()
    primary_before = primary.read_bytes()

    with pytest.raises(ValueError, match="lowercase ASCII"):
        record_check(config, _pass("current"))

    assert manifest.read_bytes() == manifest_before
    assert primary.read_bytes() == primary_before
    assert not (config.qa_root / "checks/current/primary.log").exists()


def test_epic028_wrapped_v1_transition_becomes_flat(repository: Path):
    config = _configure(repository, "HDE-EPIC028")
    for check_id in ("d0", "po-001"):
        _write_v1(config, check_id)
    manifest = {
        "epic_id": config.epic_id,
        "checks": {check_id: _entry(config, check_id) for check_id in ("d0", "po-001")},
    }
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps(manifest), encoding="utf-8"
    )
    record_check(config, _pass("current"))
    transitioned = json.loads(
        (config.qa_root / "qa_step_logs_manifest.json").read_text()
    )
    assert set(transitioned) == {"d0", "po-001", "current"}
    assert "epic_id" not in transitioned and "checks" not in transitioned


def test_epic021_runs_envelope_is_recognized_without_import(repository: Path):
    config = _configure(repository, "HDE-EPIC021")
    historical = config.qa_root / "old-run/step.log"
    historical.parent.mkdir(parents=True)
    historical.write_text("historical bytes\n", encoding="utf-8")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "epic_id": config.epic_id,
                "runs": [{"run_id": "old", "steps": [{"log_path": str(historical)}]}],
            }
        ),
        encoding="utf-8",
    )
    original = historical.read_bytes()
    record_check(config, _pass("current"))
    assert set(json.loads(manifest.read_text())) == {"current"}
    assert historical.read_bytes() == original


def test_epic029_bracket_headers_fail_closed_without_writes(repository: Path):
    config = _configure(repository, "HDE-EPIC029")
    check_ids = ("po-epic-close-live-qa", "po-precommit", "po-postcommit")
    checks = {}
    for check_id in check_ids:
        path = config.qa_root / "checks" / check_id / "primary.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"[check_id] {check_id}\n[exit_code] 0\n", encoding="utf-8")
        checks[check_id] = _entry(config, check_id)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps({"epic_id": config.epic_id, "checks": checks}), encoding="utf-8"
    )
    before = manifest.read_bytes()
    with pytest.raises(
        ValueError,
        match="unsupported primary-log schema without governed status: po-epic-close-live-qa",
    ):
        record_check(config, _pass("acceptance-map-viability"))
    assert manifest.read_bytes() == before
    assert not (config.qa_root / "checks/acceptance-map-viability/primary.log").exists()


def test_manifest_key_entry_and_header_identity_must_agree(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    _write_v1(config, "po-001")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps({"po-001": {**_entry(config, "po-001"), "check_id": "po-002"}})
    )
    with pytest.raises(ValueError, match="identity disagree"):
        record_check(config, _pass("current"))


def test_transition_rejects_invalid_header_status(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    _write_v1(config, "po-001", status="SUCCESS")
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"po-001": _entry(config, "po-001")}), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="invalid status"):
        record_check(config, _pass("current"))


@pytest.mark.parametrize(
    "log_path",
    [
        "checks/po-001/missing.log",
        "../checks/po-001/primary.log",
        "/tmp/primary.log",
        "audit/qa/hde-epic028/checks/po-001/primary.log",
        "checks/po-002/primary.log",
    ],
)
def test_transition_rejects_missing_traversing_foreign_or_mismatched_paths(
    repository: Path, log_path: str
):
    config = _configure(repository, "HDE-EPIC027")
    _write_v1(config, "po-001")
    entry = _entry(config, "po-001")
    entry["log_path"] = log_path
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"po-001": entry}), encoding="utf-8"
    )
    with pytest.raises(ValueError):
        record_check(config, _pass("current"))


def test_transition_rejects_unsupported_json_header_schema(repository: Path):
    config = _configure(repository, "HDE-EPIC027")
    path = config.qa_root / "checks/po-001/primary.log"
    path.parent.mkdir(parents=True)
    path.write_text(
        json.dumps(
            {"schema_version": "unknown", "check_id": "po-001", "status": "PASS"}
        )
        + "\n",
        encoding="utf-8",
    )
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"po-001": _entry(config, "po-001")}), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="unsupported primary-log JSON schema"):
        record_check(config, _pass("current"))


def test_canonical_v2_entry_is_idempotently_replaced(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    _, manifest = record_check(config, _pass("current"))
    record_check(
        config,
        CheckResult(
            "current",
            Status.FAIL_BEHAVIOR,
            "new contradiction",
            exit_code=1,
            command=("false",),
            command_provenance="fixture",
        ),
    )
    payload = json.loads(manifest.read_text())
    assert list(payload) == ["current"]
    assert payload["current"]["status"] == "FAIL_BEHAVIOR"


def test_complete_legacy_family_replacement_admits_only_viability(repository: Path):
    config = _configure(repository, "HDE-EPIC029")
    legacy_ids = ("po-epic-close-live-qa", "po-precommit", "po-postcommit")
    checks = {}
    for check_id in legacy_ids:
        path = config.qa_root / "checks" / check_id / "primary.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"[check_id] {check_id}\n[exit_code] 0\n", encoding="utf-8")
        checks[check_id] = _entry(config, check_id)
    (config.qa_root / "qa_step_logs_manifest.json").write_text(
        json.dumps({"epic_id": config.epic_id, "checks": checks}), encoding="utf-8"
    )
    captured_env = (
        ("ALLOW_NETWORK", "0"),
        ("APP_ENV", "dev"),
        ("LANG", "C"),
        ("LC_ALL", "C"),
        ("SAFE_MODE", "1"),
        ("TZ", "UTC"),
    )
    results = [
        CheckResult(
            check_id,
            Status.PASS,
            exit_code=0,
            command=(("python", "-m", "pytest", "--version"), ("python", "check.py")),
            command_provenance="fresh requalification",
            captured_env=captured_env,
        )
        for check_id in legacy_ids
    ]
    results.append(_pass("acceptance-map-viability"))
    ledger = config.viability_ledger_path
    ledger_content = '{"status":"PASS"}\n'

    logs, manifest = record_check_family(
        config,
        results,
        additional_files=((ledger, ledger_content),),
        coherence_verifier=lambda: json.loads(ledger.read_text()),
        replace_legacy_family_ids=legacy_ids,
        admit_new_check_ids=("acceptance-map-viability",),
        captured_at_utc="2026-08-18T12:00:00Z",
    )

    assert set(json.loads(manifest.read_text())) == {
        *legacy_ids,
        "acceptance-map-viability",
    }
    assert ledger.read_text() == ledger_content
    for log in logs:
        header = read_primary_header(log)
        assert header["timestamp_utc"] == "2026-08-18T12:00:00Z"
    assert isinstance(read_primary_header(logs[0])["command"][0], list)
    assert read_primary_header(logs[0])["captured_env"] == dict(captured_env)


def test_complete_legacy_family_replacement_rejects_partial_fresh_family(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC029")
    legacy_ids = ("po-epic-close-live-qa", "po-precommit", "po-postcommit")
    checks = {}
    for check_id in legacy_ids:
        path = config.qa_root / "checks" / check_id / "primary.log"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("[exit_code] 0\n", encoding="utf-8")
        checks[check_id] = _entry(config, check_id)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "checks": checks}))
    before = manifest.read_bytes()
    with pytest.raises(ValueError, match="partial, extra"):
        record_check_family(
            config,
            [_pass(legacy_ids[0])],
            replace_legacy_family_ids=legacy_ids,
        )
    assert manifest.read_bytes() == before


def test_pass_with_intended_tokens_records_explicit_nonclaim(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    log, _ = record_check(
        config,
        CheckResult(
            "current",
            Status.PASS,
            exit_code=0,
            command=("true",),
            command_provenance="fixture",
            intended_tokens=(TOKEN,),
        ),
    )
    assert (
        "token_claim_posture: intended tokens are recorded but not claimed"
        in log.read_text()
    )


def test_pytest_collection_deduplicates_by_file_and_checks_exact_nodes(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text(
        "def test_one():\n    pass\n\ndef test_two():\n    pass\n", encoding="utf-8"
    )
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci="pytest tests/test_sample.py::test_one; python -m pytest tests/test_sample.py::test_two",
    )
    calls = []

    class Done:
        returncode = 0
        stdout = "tests/test_sample.py::test_one\ntests/test_sample.py::test_two\n"
        stderr = ""

    def fake_run(command, **kwargs):
        calls.append((tuple(command), kwargs))
        return Done()

    for key, value in {
        "PYTEST_ADDOPTS": "--ignore=tests/test_sample.py",
        "PYTHONPATH": "/hostile/pythonpath",
        "PYTHONHOME": "/hostile/pythonhome",
        "PYTEST_PLUGINS": "hostile_plugin",
    }.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, ledger = evaluate_acceptance_map_viability(config)
    assert result.status is Status.PASS
    assert len(calls) == 1
    assert calls[0][0][:8] == (
        calls[0][0][0],
        "-m",
        "pytest",
        "--collect-only",
        "-q",
        "-p",
        "no:cacheprovider",
        calls[0][0][7],
    )
    collection_env = calls[0][1]["env"]
    assert collection_env["PYTHONDONTWRITEBYTECODE"] == "1"
    assert {
        key: collection_env[key]
        for key in ("ALLOW_NETWORK", "LANG", "LC_ALL", "SAFE_MODE", "TZ")
    } == {
        "ALLOW_NETWORK": "0",
        "LANG": "C",
        "LC_ALL": "C",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }
    assert not {
        "PYTEST_ADDOPTS",
        "PYTHONPATH",
        "PYTHONHOME",
        "PYTEST_PLUGINS",
    } & collection_env.keys()
    assert result.command == calls[0][0]
    assert result.exit_code == 0
    assert json.loads(ledger)["resolved_reference_counts"]["matrix.ci_tests_jobs"] == 2


def test_collection_receipts_are_ordered_and_exclude_unlaunched_commands(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    for name in ("test_one.py", "test_two.py"):
        path = repository / "tests" / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci="pytest tests/test_one.py; pytest tests/test_two.py",
    )
    calls: list[tuple[str, ...]] = []

    class Done:
        returncode = 0
        stderr = ""

        def __init__(self, test_file: str):
            self.stdout = f"{test_file}::test_ok\n"

    def fake_run(command, **kwargs):
        del kwargs
        frozen = tuple(command)
        calls.append(frozen)
        if len(calls) == 2:
            raise OSError("collection launch failed")
        return Done("tests/test_one.py")

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING
    assert result.command == calls[0]
    assert result.exit_code == 0


def test_collection_stops_on_controlling_failure_and_blocks_pending_requests(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    for name in ("test_one.py", "test_two.py", "test_three.py"):
        path = repository / "tests" / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci="pytest tests/test_one.py; pytest tests/test_two.py",
    )
    governance = repository / "docs/pfcanon/PF04-Canon-HDE-Governance-v1.md"
    governance.write_text(
        governance.read_text(encoding="utf-8").replace(
            "## **2.1 Next**",
            "* **QA\\_HARNESS\\_ENTRYPOINT\\_SELFTEST\\_OK** — declared.\n"
            "## **2.1 Next**",
        ),
        encoding="utf-8",
    )
    acceptance = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    acceptance["tokens"].append(
        {
            "name": "QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
            "owner_pf": "PF04",
            "status": "implemented",
            "evidence_titles": ["evidence/proof.json"],
        }
    )
    config.acceptance_map_path.write_text(json.dumps(acceptance), encoding="utf-8")
    config.token_matrix_path.write_text(
        config.token_matrix_path.read_text(encoding="utf-8")
        + _matrix_row(
            token="QA_HARNESS_ENTRYPOINT_SELFTEST_OK",
            ci="pytest tests/test_three.py",
        ),
        encoding="utf-8",
    )
    calls: list[tuple[str, ...]] = []

    class Done:
        def __init__(self, returncode: int, test_file: str):
            self.returncode = returncode
            self.stdout = (
                f"{test_file}::test_ok\n" if returncode == 0 else "collection error\n"
            )
            self.stderr = (
                "ImportError while importing test module" if returncode else ""
            )

    def fake_run(command, **kwargs):
        del kwargs
        frozen = tuple(command)
        calls.append(frozen)
        test_file = next(value for value in frozen if value.startswith("tests/"))
        return Done(2 if len(calls) == 2 else 0, test_file)

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, ledger = evaluate_acceptance_map_viability(config)
    payload = json.loads(ledger)

    assert result.status is Status.FAIL_TOOLING
    assert result.command == tuple(calls)
    assert result.exit_code == 2
    assert len(calls) == 2
    assert (
        payload["token_status"]["QA_HARNESS_ENTRYPOINT_SELFTEST_OK"]
        == "TOOLING_BLOCKED"
    )
    pending = [
        item
        for item in payload["broken_references"]
        if item["token"] == "QA_HARNESS_ENTRYPOINT_SELFTEST_OK"
    ]
    assert len(pending) == 1
    assert pending[0]["status"] == "TOOLING_BLOCKED"
    assert "not executed after controlling FAIL_TOOLING" in pending[0]["reason"]


def test_exact_node_miss_stops_later_collection_requests(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    for name in ("test_one.py", "test_two.py"):
        path = repository / "tests" / name
        path.parent.mkdir(exist_ok=True)
        path.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository,
        "HDE-EPIC039",
        ci=(
            "pytest tests/test_one.py::test_missing; "
            "pytest tests/test_two.py"
        ),
    )
    calls: list[tuple[str, ...]] = []

    class Done:
        returncode = 0
        stdout = "tests/test_one.py::test_ok\n"
        stderr = ""

    def fake_run(command, **kwargs):
        del kwargs
        calls.append(tuple(command))
        return Done()

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result, ledger = evaluate_acceptance_map_viability(config)
    payload = json.loads(ledger)

    assert result.status is Status.TOOLING_BLOCKED
    assert result.command == calls[0]
    assert result.exit_code == 0
    assert len(calls) == 1
    reasons = [item["reason"] for item in payload["broken_references"]]
    assert any("pytest node was not collected exactly" in reason for reason in reasons)
    assert any(
        "not executed after controlling TOOLING_BLOCKED" in reason
        for reason in reasons
    )


def test_collection_launch_failure_before_completion_records_no_command(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    config = _configure(repository, "HDE-EPIC039", ci="pytest tests/test_sample.py")
    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run",
        lambda *args, **kwargs: (_ for _ in ()).throw(OSError("launch failed")),
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING
    assert result.command == ()
    assert result.exit_code is None


def test_bare_script_requires_executable_bit_but_python_form_does_not(
    repository: Path,
):
    script = repository / "tools/check.py"
    script.chmod(0o644)
    bare, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci="tools/check.py")
    )
    interpreted, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci="python tools/check.py")
    )
    script.chmod(0o755)
    executable, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci="tools/check.py")
    )
    assert bare.status is Status.TOOLING_BLOCKED
    assert "not executable" in bare.status_reason
    assert interpreted.status is Status.PASS
    assert executable.status is Status.PASS


@pytest.mark.parametrize(
    ("ci", "expected", "reason_fragment"),
    [
        (
            "pytest --definitely-invalid tests/test_sample.py",
            Status.TOOLING_BLOCKED,
            "unsupported option",
        ),
        (
            "pytest -k no_such_test tests/test_sample.py",
            Status.TOOLING_BLOCKED,
            "pytest file is unavailable",
        ),
    ],
)
def test_pytest_locator_options_are_preserved_during_collection(
    repository: Path,
    ci: str,
    expected: Status,
    reason_fragment: str,
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    result, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci=ci)
    )
    assert result.status is expected
    assert reason_fragment in result.status_reason
    if "-k" in ci:
        serialized = result.command
        if serialized and isinstance(serialized[0], tuple):
            flattened = " ".join(serialized[0])
        else:
            flattened = " ".join(serialized)
        assert "no_such_test" in flattened
    else:
        assert result.command == ()


@pytest.mark.parametrize(
    "ci",
    [
        "pytest --ignore tests/test_sample.py tests/test_sample.py",
        "pytest --basetemp=/tmp/foreign tests/test_sample.py",
        "pytest -c /tmp/foreign.ini tests/test_sample.py",
        "pytest -p arbitrary_plugin tests/test_sample.py",
    ],
)
def test_pytest_locator_rejects_path_and_plugin_control_options(
    repository: Path, ci: str
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_ok():\n    pass\n", encoding="utf-8")
    result, _ = evaluate_acceptance_map_viability(
        _configure(repository, "HDE-EPIC039", ci=ci)
    )
    assert result.status is Status.TOOLING_BLOCKED
    assert "pytest locator" in result.status_reason


def test_missing_pytest_node_is_tooling_blocked(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("def test_one():\n    pass\n", encoding="utf-8")
    config = _configure(
        repository, "HDE-EPIC039", ci="pytest tests/test_sample.py::test_missing"
    )

    class Done:
        returncode = 0
        stdout = "tests/test_sample.py::test_one\n"
        stderr = ""

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.TOOLING_BLOCKED


def test_collection_import_failure_is_fail_tooling(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "tests/test_sample.py"
    test_file.parent.mkdir()
    test_file.write_text("raise RuntimeError('import')\n", encoding="utf-8")
    config = _configure(repository, "HDE-EPIC039", ci="pytest tests/test_sample.py")

    class Done:
        returncode = 2
        stdout = ""
        stderr = "ERROR collecting tests/test_sample.py"

    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run", lambda *args, **kwargs: Done()
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING


@pytest.mark.parametrize(
    ("locator", "expected"),
    [
        ("python tools/missing.py", Status.TOOLING_BLOCKED),
        ("pytest tests/missing.py::test_x", Status.TOOLING_BLOCKED),
        ("Existing epic-close output only", Status.TOOLING_BLOCKED),
        ("python <repository-script>", Status.TOOLING_BLOCKED),
    ],
)
def test_missing_or_prose_ci_locators_are_tooling_blocked(
    repository: Path, locator: str, expected: Status
):
    config = _configure(repository, "HDE-EPIC039", ci=locator)
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is expected


@pytest.mark.parametrize(
    ("locator", "expected"),
    [
        ("audit/qa/hde-epic028/checks/other/primary.log", Status.FAIL_BEHAVIOR),
        ("../escape.log", Status.FAIL_BEHAVIOR),
        ("checks/<run-id>/primary.log", Status.TOOLING_BLOCKED),
        ("checks/missing/primary.log", Status.TOOLING_BLOCKED),
    ],
)
def test_invalid_qa_locators_fail_causally(
    repository: Path, locator: str, expected: Status
):
    config = _configure(repository, "HDE-EPIC039", qa=locator)
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is expected


def test_declared_planned_qa_output_is_valid(repository: Path):
    config = _configure(
        repository,
        "HDE-EPIC039",
        qa="checks/future-step/primary.log",
        step_names=("future-step",),
    )
    result, _ = evaluate_acceptance_map_viability(config)
    assert result.status is Status.PASS


def test_governed_ledger_self_output_requires_explicit_publication_plan(
    repository: Path,
):
    config = _configure(repository, "HDE-EPIC039", qa="acceptance_map_viability.log")
    blocked, _ = evaluate_acceptance_map_viability(config)
    planned, _ = evaluate_acceptance_map_viability(config, planned_governed_ledger=True)
    assert blocked.status is Status.TOOLING_BLOCKED
    assert blocked.evidence_artifacts == ()
    assert planned.status is Status.PASS
    assert planned.evidence_artifacts == (
        "audit/qa/hde-epic039/acceptance_map_viability.log",
    )


def test_referenced_manifest_with_broken_nested_log_is_fail_tooling(repository: Path):
    config = _configure(
        repository,
        "HDE-EPIC039",
        evidence_titles=("audit/qa/hde-epic039/qa_step_logs_manifest.json",),
        evidence="audit/qa/hde-epic039/qa_step_logs_manifest.json",
    )
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "broken": {
                    "check_id": "broken",
                    "log_path": "checks/broken/primary.log",
                    "status": "PASS",
                }
            }
        ),
        encoding="utf-8",
    )
    result, ledger = evaluate_acceptance_map_viability(config)
    payload = json.loads(ledger)
    assert result.status is Status.FAIL_TOOLING
    assert payload["referenced_manifests"] == [
        "audit/qa/hde-epic039/qa_step_logs_manifest.json"
    ]
    assert payload["broken_references"]


def test_post_write_coherence_failure_restores_every_preimage(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    original_manifest = json.dumps({"epic_id": config.epic_id, "runs": []})
    manifest.write_text(original_manifest, encoding="utf-8")
    additional = config.qa_root / "acceptance_map_viability.log"
    additional.write_text("old ledger\n", encoding="utf-8")

    def reject() -> None:
        raise RuntimeError("post-write coherence failed")

    with pytest.raises(RuntimeError, match="post-write coherence failed"):
        record_check_family(
            config,
            (_pass("one"), _pass("two")),
            additional_files=((additional, "new ledger\n"),),
            coherence_verifier=reject,
        )
    assert manifest.read_text() == original_manifest
    assert additional.read_text() == "old ledger\n"
    assert not (config.qa_root / "checks/one/primary.log").exists()
    assert not (config.qa_root / "checks/two/primary.log").exists()


def test_empty_preimage_is_restored_after_publication_failure(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "runs": []}))
    additional = config.qa_root / "acceptance_map_viability.log"
    additional.write_bytes(b"")

    with pytest.raises(RuntimeError, match="reject staged family"):
        record_check_family(
            config,
            (_pass("current"),),
            additional_files=((additional, "replacement\n"),),
            coherence_verifier=lambda: (_ for _ in ()).throw(
                RuntimeError("reject staged family")
            ),
        )

    assert additional.exists() and additional.read_bytes() == b""
    assert not (config.qa_root / "checks/current/primary.log").exists()


def test_publication_rejects_symlink_output_without_mutation(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text(json.dumps({"epic_id": config.epic_id, "runs": []}))
    outside = repository / "outside.log"
    outside.write_text("protected\n", encoding="utf-8")
    primary = config.qa_root / "checks/current/primary.log"
    primary.parent.mkdir(parents=True)
    primary.symlink_to(outside)

    with pytest.raises(ValueError, match="cannot be a symlink"):
        record_check(config, _pass("current"))

    assert primary.is_symlink()
    assert outside.read_text(encoding="utf-8") == "protected\n"
    assert json.loads(manifest.read_text(encoding="utf-8")) == {
        "epic_id": config.epic_id,
        "runs": [],
    }


def test_flat_v2_status_mismatch_fails_before_any_write(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    current_log, manifest = record_check(config, _pass("current"))
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    payload["current"]["status"] = "FAIL_BEHAVIOR"
    manifest.write_text(json.dumps(payload), encoding="utf-8")
    before_manifest = manifest.read_bytes()
    before_log = current_log.read_bytes()

    with pytest.raises(ValueError, match="status disagrees"):
        record_check(config, _pass("new"))

    assert manifest.read_bytes() == before_manifest
    assert current_log.read_bytes() == before_log
    assert not (config.qa_root / "checks/new/primary.log").exists()


def test_flat_v2_legacy_pf_ref_fails_before_any_write(repository: Path):
    config = _configure(repository, "HDE-EPIC039")
    current_log, manifest = record_check(config, _pass("current"))
    lines = current_log.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    header["pf_refs"] = ["PF19 §4.4"]
    current_log.write_text(
        json.dumps(header, sort_keys=True, separators=(",", ":"))
        + "\n"
        + "\n".join(lines[1:])
        + ("\n" if len(lines) > 1 else ""),
        encoding="utf-8",
    )
    before_manifest = manifest.read_bytes()

    with pytest.raises(ValueError, match="exact in-document PF titles"):
        record_check(config, _pass("new"))

    assert manifest.read_bytes() == before_manifest
    assert not (config.qa_root / "checks/new/primary.log").exists()


@pytest.mark.parametrize(
    "kwargs",
    [
        {"command": ("true",), "exit_code": None},
        {"command": (), "exit_code": 0},
        {"command": ("true",), "exit_code": True},
    ],
)
def test_check_result_rejects_command_exit_contradictions(kwargs: dict[str, object]):
    with pytest.raises(ValueError, match="exit_code|command execution"):
        CheckResult("invalid", Status.FAIL_TOOLING, "invalid receipt", **kwargs)


def test_check_result_rejects_section_qualified_pf_aliases():
    with pytest.raises(ValueError, match="exact in-document PF titles"):
        CheckResult(
            "invalid-pf-ref",
            Status.FAIL_TOOLING,
            "invalid receipt",
            pf_refs=("PF19 — Glow QA Guide §4.4",),
        )


def test_unmocked_epic027_viability_wrapper_uses_shared_evaluator(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    from tools.qa import generate_epic027_close_pack as module

    config = _configure(
        repository,
        "HDE-EPIC027",
        qa="acceptance_map_viability.log",
        step_names=("acceptance_map_viability",),
    )
    monkeypatch.setattr(module, "ROOT", repository)
    monkeypatch.setattr(module, "VIABILITY_LOG_PATH", config.viability_ledger_path)
    module._write_viability_log()
    assert config.viability_ledger_path.is_file()
    payload = json.loads((config.qa_root / "qa_step_logs_manifest.json").read_text())
    assert payload["acceptance-map-viability"]["status"] == "PASS"
