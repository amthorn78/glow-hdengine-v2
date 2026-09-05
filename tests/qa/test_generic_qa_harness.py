import hashlib
import json
import sys
from dataclasses import replace
from pathlib import Path

import pytest

from tools.qa import qa_harness
from tools.qa.qa_harness import (
    CheckResult,
    HarnessConfig,
    Status,
    classify_pytest_returncode,
    evaluate_acceptance_map_viability,
    generate_acceptance_map_viability,
    read_primary_header,
    record_check,
    record_check_family,
    require_governed_viability,
    run_pytest_check,
    summarize_checks,
    update_manifest,
    validate_crd_check_family,
    write_primary_log,
)

MATRIX_HEADER = (
    "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |\n"
    "| --- | --- | --- | --- | --- | --- | --- |\n"
)
FIXED_TIMESTAMP = "2026-01-01T00:00:00Z"


def _write_evidence_graph(
    root: Path, bindings: dict[str, tuple[str, ...]]
) -> None:
    human_rows: list[dict[str, object]] = []
    mirror_rows: list[dict[str, object]] = []
    for path, artifact_keys in bindings.items():
        payload = (root / path).read_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        size = len(payload)
        proof = root / f"{path}.path_proof.txt"
        proof.parent.mkdir(parents=True, exist_ok=True)
        proof.write_text(
            "\n".join(
                (
                    f"path: {path}",
                    f"size_bytes: {size}",
                    f"sha256: {digest}",
                    f"mtime_utc: {FIXED_TIMESTAMP}",
                    f"produced_at_utc: {FIXED_TIMESTAMP}",
                    "",
                )
            ),
            encoding="utf-8",
        )
        for artifact_key in artifact_keys:
            human_rows.append(
                {
                    "artifact_key": artifact_key,
                    "discovered_physical_path": path,
                }
            )
            mirror_rows.append(
                {
                    "artifact_key": artifact_key,
                    "discovered_physical_path": path,
                    "produced_at_utc": FIXED_TIMESTAMP,
                    "proof_anchor": f"{path}.path_proof.txt",
                    "role": "snapshot",
                    "sha256": digest,
                    "size_bytes": size,
                }
            )
    human_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    mirror_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    body_bytes = b"".join(
        (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode(
            "utf-8"
        )
        for row in mirror_rows
    )
    body_sha = hashlib.sha256(body_bytes).hexdigest()
    self_record: dict[str, object] = {
        "artifact_key": "index.machine_mirror",
        "discovered_physical_path": "artifacts/evidence_index.jsonl",
        "produced_at_utc": FIXED_TIMESTAMP,
        "proof_anchor": "artifacts/evidence_index.jsonl.path_proof.txt",
        "role": "self_record",
        "sha256": body_sha,
        "size_bytes": 0,
    }
    mirror_rows.append(self_record)
    mirror_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    while True:
        mirror_bytes = b"".join(
            (json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n").encode(
                "utf-8"
            )
            for row in mirror_rows
        )
        if self_record["size_bytes"] == len(mirror_bytes):
            break
        self_record["size_bytes"] = len(mirror_bytes)
    human_rows.append(
        {
            "artifact_key": "index.machine_mirror",
            "discovered_physical_path": "artifacts/evidence_index.jsonl",
        }
    )
    human_rows.sort(
        key=lambda row: (row["artifact_key"], row["discovered_physical_path"])
    )
    human_index = root / "docs/evidence/INDEX.json"
    human_index.parent.mkdir(parents=True, exist_ok=True)
    human_index.write_text(
        json.dumps(human_rows, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    mirror = root / "artifacts/evidence_index.jsonl"
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_bytes(mirror_bytes)
    (root / "artifacts/evidence_index.jsonl.path_proof.txt").write_text(
        "\n".join(
            (
                "path: artifacts/evidence_index.jsonl",
                f"size_bytes: {len(mirror_bytes)}",
                f"sha256: {hashlib.sha256(mirror_bytes).hexdigest()}",
                f"mirror_body_sha256: {body_sha}",
                f"mtime_utc: {FIXED_TIMESTAMP}",
                f"produced_at_utc: {FIXED_TIMESTAMP}",
                "",
            )
        ),
        encoding="utf-8",
    )


def _matrix_row(
    evidence: str,
    *,
    token: str = "QA_HARNESS_DISCIPLINE_OK",
    ci: str = "python tools/check.py",
    qa: str = "checks/acceptance-map-viability/primary.log",
    status: str = "Implemented",
) -> str:
    return f"| {token} | PF04 | {evidence} | {ci} | {qa} | {status} | fixture |\n"


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
    _write_evidence_graph(
        tmp_path, {"evidence/proof.json": ("fixture.primary_evidence",)}
    )
    (tmp_path / "tools").mkdir()
    (tmp_path / "tools/check.py").write_text("raise SystemExit(0)\n", encoding="utf-8")
    config = HarnessConfig("HDE-EPIC039", repo_root=tmp_path)
    config.acceptance_map_path.parent.mkdir(exist_ok=True)
    config.acceptance_map_path.write_text(
        json.dumps(
            {
                "epic_id": "HDE-EPIC039",
                "tokens": [
                    {
                        "name": "QA_HARNESS_DISCIPLINE_OK",
                        "owner_pf": "PF04",
                        "status": "implemented",
                        "evidence_titles": ["evidence/proof.json"],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    config.token_matrix_path.parent.mkdir(parents=True)
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row("evidence/proof.json"), encoding="utf-8"
    )
    return tmp_path


def test_config_derives_canonical_paths(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    assert config.qa_root == repository / "audit/qa/hde-epic039"
    assert config.acceptance_map_path == repository / "docs/acceptance_map_epic039.json"
    assert config.token_matrix_path == config.qa_root / "token_evidence_matrix.md"
    with pytest.raises(ValueError):
        HarnessConfig("hde-epic039", repo_root=repository)


def test_exact_status_set_and_causal_rollup():
    assert {status.value for status in Status} == {
        "PASS",
        "FAIL_BEHAVIOR",
        "FAIL_TOOLING",
        "TOOLING_BLOCKED",
        "PARKED",
    }
    assert summarize_checks([CheckResult("ok", Status.PASS)]) is Status.PASS
    assert (
        summarize_checks([CheckResult("parked", Status.PARKED, "authorized deferral")])
        is Status.PARKED
    )
    assert (
        summarize_checks([CheckResult("blocked", Status.TOOLING_BLOCKED, "missing")])
        is Status.TOOLING_BLOCKED
    )
    with pytest.raises(ValueError):
        CheckResult("bad", "SUCCESS")


@pytest.mark.parametrize("check_id", ["", "..", "a/b", "a\\b", "/absolute"])
def test_unsafe_check_ids_are_rejected(repository: Path, check_id: str):
    with pytest.raises(ValueError):
        CheckResult(check_id, Status.PASS, exit_code=0)


@pytest.mark.parametrize("publish_family", [False, True])
def test_current_publishers_reject_uppercase_ids_before_writes_and_admit_lowercase(
    repository: Path, publish_family: bool
):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    sidecar = config.qa_root / "publication-sidecar.log"

    with pytest.raises(ValueError, match="lowercase ASCII"):
        CheckResult("D00_new", Status.PASS)

    corrupted = CheckResult(
        "d00-new",
        Status.PASS,
        command=("true",),
        command_provenance="test fixture",
        exit_code=0,
    )
    object.__setattr__(corrupted, "check_id", "D00_new")
    with pytest.raises(ValueError, match="lowercase ASCII"):
        if publish_family:
            record_check_family(
                config,
                (corrupted,),
                additional_files=((sidecar, "must not publish\n"),),
            )
        else:
            record_check(
                config,
                corrupted,
                additional_files=((sidecar, "must not publish\n"),),
            )

    assert not (config.qa_root / "checks/D00_new/primary.log").exists()
    assert not (config.qa_root / "qa_step_logs_manifest.json").exists()
    assert not sidecar.exists()

    lowercase = CheckResult(
        "d00-new",
        Status.PASS,
        command=("true",),
        command_provenance="test fixture",
        exit_code=0,
    )
    uppercase_sidecar = config.qa_root / "checks/D00_new/sidecar.txt"
    with pytest.raises(ValueError, match="lowercase ASCII"):
        if publish_family:
            record_check_family(
                config,
                (lowercase,),
                additional_files=((uppercase_sidecar, "must not publish\n"),),
            )
        else:
            record_check(
                config,
                lowercase,
                additional_files=((uppercase_sidecar, "must not publish\n"),),
            )
    assert not (config.qa_root / "checks/d00-new/primary.log").exists()
    assert not (config.qa_root / "qa_step_logs_manifest.json").exists()
    assert not uppercase_sidecar.exists()
    assert not uppercase_sidecar.parent.exists()

    uppercase_report = config.qa_root / "UPPERCASE-REPORT.txt"
    if publish_family:
        logs, manifest = record_check_family(
            config,
            (lowercase,),
            additional_files=((uppercase_report, "allowed outside checks\n"),),
        )
        log = logs[0]
    else:
        log, manifest = record_check(
            config,
            lowercase,
            additional_files=((uppercase_report, "allowed outside checks\n"),),
        )
    assert log == config.qa_root / "checks/d00-new/primary.log"
    assert uppercase_report.read_text(encoding="utf-8") == "allowed outside checks\n"
    assert json.loads(manifest.read_text(encoding="utf-8")) == {
        "d00-new": {
            "check_id": "d00-new",
            "log_path": "audit/qa/hde-epic039/checks/d00-new/primary.log",
            "status": "PASS",
        }
    }


def test_pf27_header_and_manifest_replace_by_check_id(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    first = CheckResult(
        "selftest",
        Status.PASS,
        exit_code=0,
        command=("true",),
        command_provenance="test fixture",
    )
    log, manifest = record_check(config, first)
    header = read_primary_header(log)
    assert header["schema_version"] == "pf27.step_log_header.v2"
    assert header["claimed_tokens"] == []
    assert header["evidence_artifacts"] == [
        "audit/qa/hde-epic039/checks/selftest/primary.log"
    ]
    second = CheckResult(
        "selftest",
        Status.FAIL_BEHAVIOR,
        "contradiction",
        exit_code=1,
        command=("false",),
        command_provenance="test fixture",
    )
    update_manifest(config, record_check(config, second)[0])
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    assert list(payload) == ["selftest"]
    assert payload["selftest"]["status"] == "FAIL_BEHAVIOR"
    assert "run_id" not in manifest.read_text(encoding="utf-8")


def test_same_interpreter_and_classification(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "test_sample.py"
    test_file.write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    calls = []

    class Done:
        returncode = 0
        stdout = "ok"
        stderr = ""

    def fake_run(command, **kwargs):
        calls.append(tuple(command))
        return Done()

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result = run_pytest_check(
        HarnessConfig("HDE-EPIC039", repo_root=repository),
        "pytest",
        ("-q", "test_sample.py"),
    )
    assert calls[0] == (sys.executable, "-m", "pytest", "--version")
    assert result.command == (
        (sys.executable, "-m", "pytest", "--version"),
        (sys.executable, "-m", "pytest", "-q", "test_sample.py"),
    )
    assert result.exit_code == 0
    assert result.status is Status.PASS
    missing = run_pytest_check(
        HarnessConfig("HDE-EPIC039", repo_root=repository), "missing", ("missing.py",)
    )
    assert missing.status is Status.TOOLING_BLOCKED


def test_pytest_rejects_uppercase_check_id_without_spawning(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "test_sample.py"
    test_file.write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    calls = []
    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run",
        lambda *args, **kwargs: calls.append((args, kwargs)),
    )

    with pytest.raises(ValueError, match="lowercase ASCII"):
        run_pytest_check(
            HarnessConfig("HDE-EPIC039", repo_root=repository),
            "D00_new",
            ("-q", "test_sample.py"),
        )

    assert calls == []


@pytest.mark.parametrize(
    "pytest_args",
    [
        ("-q", "-k", "expression", "test_sample.py"),
        ("-q", "-m", "not slow", "test_sample.py"),
        ("-q", "-p", "no:cacheprovider", "test_sample.py"),
    ],
)
def test_pytest_preflight_skips_admitted_option_values(
    repository: Path,
    monkeypatch: pytest.MonkeyPatch,
    pytest_args: tuple[str, ...],
):
    test_file = repository / "test_sample.py"
    test_file.write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    calls = []

    class Done:
        returncode = 0
        stdout = "ok"
        stderr = ""

    def fake_run(command, **kwargs):
        calls.append((tuple(command), kwargs))
        return Done()

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)

    result = run_pytest_check(
        HarnessConfig("HDE-EPIC039", repo_root=repository),
        "pytest-options",
        pytest_args,
    )

    assert result.status is Status.PASS
    assert [command for command, _ in calls] == [
        (sys.executable, "-m", "pytest", "--version"),
        (sys.executable, "-m", "pytest", *pytest_args),
    ]
    assert result.command == tuple(command for command, _ in calls)


@pytest.mark.parametrize(
    ("pytest_args", "reason"),
    [
        (("-q", "-k"), "lacks its expression"),
        (
            ("-q", "-p", "arbitrary_plugin", "test_sample.py"),
            "admits only -p no:cacheprovider",
        ),
        (
            ("-q", "--basetemp", "/tmp/foreign", "test_sample.py"),
            "uses unsupported option: --basetemp",
        ),
    ],
)
def test_pytest_preflight_rejects_unbounded_option_controls_without_execution(
    repository: Path,
    monkeypatch: pytest.MonkeyPatch,
    pytest_args: tuple[str, ...],
    reason: str,
):
    (repository / "test_sample.py").write_text(
        "def test_ok():\n    assert True\n", encoding="utf-8"
    )
    calls = []
    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run",
        lambda *args, **kwargs: calls.append((args, kwargs)),
    )

    result = run_pytest_check(
        HarnessConfig("HDE-EPIC039", repo_root=repository),
        "pytest-options",
        pytest_args,
    )

    assert result.status is Status.TOOLING_BLOCKED
    assert reason in result.status_reason
    assert result.command == ()
    assert result.exit_code is None
    assert calls == []


def test_pytest_readiness_launch_failure_records_no_executed_command(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "test_sample.py"
    test_file.write_text("def test_ok():\n    assert True\n", encoding="utf-8")
    monkeypatch.setattr(
        "tools.qa.qa_harness.subprocess.run",
        lambda *args, **kwargs: (_ for _ in ()).throw(OSError("launch failed")),
    )
    result = run_pytest_check(
        HarnessConfig("HDE-EPIC039", repo_root=repository),
        "pytest",
        ("-q", "test_sample.py"),
    )
    assert result.status is Status.FAIL_TOOLING
    assert result.command == ()
    assert result.exit_code is None


def test_pytest_no_collection_is_tooling_blocked(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    test_file = repository / "test_sample.py"
    test_file.write_text("def test_ok():\n    assert True\n", encoding="utf-8")

    class Done:
        stdout = ""
        stderr = ""

        def __init__(self, returncode: int):
            self.returncode = returncode

    calls = 0

    def fake_run(*args, **kwargs):
        nonlocal calls
        del args, kwargs
        calls += 1
        return Done(0 if calls == 1 else 5)

    monkeypatch.setattr("tools.qa.qa_harness.subprocess.run", fake_run)
    result = run_pytest_check(
        HarnessConfig("HDE-EPIC039", repo_root=repository),
        "pytest",
        ("-q", "test_sample.py"),
    )
    assert result.status is Status.TOOLING_BLOCKED
    assert result.exit_code == 5


def test_viability_passes_exact_and_legacy_single_path(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    assert generate_acceptance_map_viability(config).status is Status.PASS
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row("Proof title (`evidence/proof.json`)"),
        encoding="utf-8",
    )
    result = generate_acceptance_map_viability(config)
    assert result.status is Status.PASS
    assert result.primary_log and result.primary_log.stat().st_size > 0
    manifest = json.loads(result.manifest.read_text(encoding="utf-8"))
    assert list(manifest).count("acceptance-map-viability") == 1


def test_governance_binding_does_not_promote_ci_or_qa_locators(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    indexed_paths = {
        row["discovered_physical_path"]
        for row in json.loads(
            (repository / "docs/evidence/INDEX.json").read_text(encoding="utf-8")
        )
    }

    result, _ = evaluate_acceptance_map_viability(config)

    assert "tools/check.py" not in indexed_paths
    assert (
        "audit/qa/hde-epic039/checks/acceptance-map-viability/primary.log"
        not in indexed_paths
    )
    assert result.status is Status.PASS


def test_existing_unindexed_acceptance_evidence_cannot_pass(repository: Path):
    unindexed = repository / "evidence/unindexed.txt"
    unindexed.write_text("present but not governed\n", encoding="utf-8")
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = ["evidence/unindexed.txt"]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row("evidence/unindexed.txt"), encoding="utf-8"
    )

    result, ledger = evaluate_acceptance_map_viability(config)
    broken = json.loads(ledger)["broken_references"]

    assert result.status is Status.TOOLING_BLOCKED
    assert {
        item["source_field"]
        for item in broken
        if item["resolved_path"] == "evidence/unindexed.txt"
    } == {"acceptance_map.evidence_titles", "matrix.evidence_artifacts"}
    assert all("Human Index and Machine Mirror" in item["reason"] for item in broken)


def test_governance_graph_requires_exact_key_set_parity(repository: Path):
    mirror = repository / "artifacts/evidence_index.jsonl"
    rows = [
        json.loads(line) for line in mirror.read_text(encoding="utf-8").splitlines()
    ]
    row = next(item for item in rows if item["role"] != "self_record")
    row["artifact_key"] = "fixture.contradictory_alias"
    mirror.write_text(
        "".join(
            json.dumps(item, sort_keys=True, separators=(",", ":")) + "\n"
            for item in rows
        ),
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )

    assert result.status is Status.FAIL_TOOLING
    assert "key/path bindings disagree" in result.status_reason


def test_governance_graph_requires_self_record_for_ordinary_evidence(
    repository: Path,
):
    human_path = repository / "docs/evidence/INDEX.json"
    human = [
        row
        for row in json.loads(human_path.read_text(encoding="utf-8"))
        if row["artifact_key"] != "index.machine_mirror"
    ]
    human_path.write_text(
        json.dumps(human, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    mirror_path = repository / "artifacts/evidence_index.jsonl"
    mirror = [
        json.loads(line)
        for line in mirror_path.read_text(encoding="utf-8").splitlines()
        if json.loads(line)["artifact_key"] != "index.machine_mirror"
    ]
    mirror_path.write_text(
        "".join(
            json.dumps(row, sort_keys=True, separators=(",", ":")) + "\n"
            for row in mirror
        ),
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )

    assert result.status is Status.FAIL_TOOLING
    assert "exactly one canonical self-record" in result.status_reason


def test_governance_graph_rejects_unrelated_global_parity_gap(repository: Path):
    other = repository / "evidence/other.txt"
    other.write_text("other\n", encoding="utf-8")
    human_path = repository / "docs/evidence/INDEX.json"
    human = json.loads(human_path.read_text(encoding="utf-8"))
    human.append(
        {
            "artifact_key": "fixture.unpaired",
            "discovered_physical_path": "evidence/other.txt",
        }
    )
    human.sort(key=lambda row: (row["artifact_key"], row["discovered_physical_path"]))
    human_path.write_text(
        json.dumps(human, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )

    assert result.status is Status.FAIL_TOOLING
    assert "key/path bindings disagree" in result.status_reason
    assert "fixture.unpaired" in result.status_reason


def test_governance_graph_allows_matching_multi_key_path(repository: Path):
    _write_evidence_graph(
        repository,
        {
            "evidence/proof.json": (
                "fixture.alias_a",
                "fixture.alias_b",
            )
        },
    )

    result, _ = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )

    assert result.status is Status.PASS


def test_acceptance_evidence_rejects_noncanonical_dot_alias(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = ["evidence/./proof.json"]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row("evidence/./proof.json"), encoding="utf-8"
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_BEHAVIOR
    assert "traverses or is absolute" in result.status_reason


def test_planned_acceptance_output_rejects_symlink_alias(repository: Path):
    planned = repository / (
        "audit/qa/hde-epic039/checks/acceptance-map-viability/primary.log"
    )
    planned.parent.mkdir(parents=True, exist_ok=True)
    planned.symlink_to((repository / "evidence/proof.json").resolve())
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = [
        planned.relative_to(repository).as_posix()
    ]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(planned.relative_to(repository).as_posix()),
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_BEHAVIOR
    assert "planned output is aliased" in result.status_reason


def test_planned_acceptance_output_rejects_existing_directory(repository: Path):
    planned = repository / (
        "audit/qa/hde-epic039/checks/acceptance-map-viability/primary.log"
    )
    planned.mkdir(parents=True)
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = [
        planned.relative_to(repository).as_posix()
    ]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(planned.relative_to(repository).as_posix()),
        encoding="utf-8",
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_BEHAVIOR
    assert "non-regular file" in result.status_reason


def test_missing_sibling_path_proof_is_tooling_blocked(repository: Path):
    (repository / "evidence/proof.json.path_proof.txt").unlink()

    result, _ = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )

    assert result.status is Status.TOOLING_BLOCKED
    assert "sibling path proof is missing" in result.status_reason


@pytest.mark.parametrize(
    ("mutation", "expected"),
    [("missing", Status.TOOLING_BLOCKED), ("malformed", Status.FAIL_TOOLING)],
)
def test_evidence_graph_failure_classification_is_causal(
    repository: Path, mutation: str, expected: Status
):
    human_index = repository / "docs/evidence/INDEX.json"
    if mutation == "missing":
        human_index.unlink()
    else:
        human_index.write_text("{", encoding="utf-8")

    result, _ = evaluate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )

    assert result.status is expected


def test_path_proof_cannot_be_primary_acceptance_evidence(repository: Path):
    proof_path = "evidence/proof.json.path_proof.txt"
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = [proof_path]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(proof_path), encoding="utf-8"
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "cannot be primary acceptance evidence" in result.status_reason


def test_graph_snapshot_is_refreshed_for_each_evaluation(repository: Path):
    path = "evidence/newly-governed.txt"
    (repository / path).write_text("new\n", encoding="utf-8")
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = [path]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(path), encoding="utf-8"
    )

    first, _ = evaluate_acceptance_map_viability(config)
    _write_evidence_graph(repository, {path: ("fixture.newly_governed",)})
    second, _ = evaluate_acceptance_map_viability(config)

    assert first.status is Status.TOOLING_BLOCKED
    assert second.status is Status.PASS


@pytest.mark.parametrize(
    "source_field",
    ["acceptance_map.evidence_titles", "matrix.evidence_artifacts"],
)
def test_planned_output_cannot_substitute_for_governed_acceptance_evidence(
    repository: Path, source_field: str
):
    planned = "audit/qa/hde-epic039/checks/acceptance-map-viability/primary.log"
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    if source_field == "acceptance_map.evidence_titles":
        payload["tokens"][0]["evidence_titles"] = [planned]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    if source_field == "matrix.evidence_artifacts":
        config.token_matrix_path.write_text(
            MATRIX_HEADER + _matrix_row(planned), encoding="utf-8"
        )

    result, ledger = evaluate_acceptance_map_viability(config)
    broken = json.loads(ledger)["broken_references"]

    assert result.status is Status.TOOLING_BLOCKED
    assert any(
        item["source_field"] == source_field
        and item["resolved_path"] == planned
        and "missing or empty" in item["reason"]
        for item in broken
    )


def test_planned_acceptance_output_exception_is_exact(repository: Path):
    adjacent = "audit/qa/hde-epic039/checks/acceptance-map-viability/adjacent.log"
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = [adjacent]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(adjacent), encoding="utf-8"
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.TOOLING_BLOCKED
    assert "missing or empty" in result.status_reason


def test_machine_mirror_checksum_has_no_acceptance_evidence_exception(
    repository: Path,
):
    checksum = "artifacts/evidence_index.jsonl.sha256"
    (repository / checksum).write_text(
        "0" * 64 + "  artifacts/evidence_index.jsonl\n", encoding="utf-8"
    )
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = [checksum]
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(checksum), encoding="utf-8"
    )

    result, _ = evaluate_acceptance_map_viability(config)

    assert result.status is Status.TOOLING_BLOCKED
    assert "absent from the Human Index and Machine Mirror" in result.status_reason


def test_pf04_declaration_forms_ignore_explanatory_prose(repository: Path):
    from tools.qa.qa_harness import _governance_tokens

    tokens, error = _governance_tokens(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )
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
    _write_evidence_graph(
        repository,
        {
            "evidence/proof.json": ("fixture.primary_evidence",),
            "evidence/second.txt": ("fixture.second_evidence",),
        },
    )
    config.token_matrix_path.write_text(
        MATRIX_HEADER
        + _matrix_row("evidence/proof.json; Proof (`evidence/second.txt`)"),
        encoding="utf-8",
    )
    assert generate_acceptance_map_viability(config).status is Status.PASS
    config.token_matrix_path.write_text(
        config.token_matrix_path.read_text(encoding="utf-8").replace(
            "; Proof", "; ; Proof"
        ),
        encoding="utf-8",
    )
    assert generate_acceptance_map_viability(config).status is Status.FAIL_TOOLING


def test_generator_only_viability_ledger_matches_primary_evaluation(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    result = generate_acceptance_map_viability(config, publish_governed_ledger=True)
    assert result.status is Status.PASS
    assert result.governed_ledger == config.viability_ledger_path
    ledger = json.loads(result.governed_ledger.read_text(encoding="utf-8"))
    primary_evaluation = json.loads(
        result.primary_log.read_text(encoding="utf-8").splitlines()[1]
    )
    assert ledger == primary_evaluation
    assert read_primary_header(result.primary_log)["evidence_artifacts"] == [
        "audit/qa/hde-epic039/checks/acceptance-map-viability/primary.log",
        "audit/qa/hde-epic039/acceptance_map_viability.log",
    ]
    assert require_governed_viability(result, config.viability_ledger_path) == (
        config.viability_ledger_path
    )


def test_governed_viability_admission_rejects_unbound_ledger(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    result = generate_acceptance_map_viability(config, publish_governed_ledger=True)
    primary_lines = result.primary_log.read_text(encoding="utf-8").splitlines()
    header = json.loads(primary_lines[0])
    header["evidence_artifacts"].remove(
        "audit/qa/hde-epic039/acceptance_map_viability.log"
    )
    result.primary_log.write_text(
        "\n".join(
            (
                json.dumps(header, sort_keys=True, separators=(",", ":")),
                *primary_lines[1:],
                "",
            )
        ),
        encoding="utf-8",
    )

    with pytest.raises(SystemExit, match="ACCEPTANCE_MAP_VIABILITY_LEDGER_UNBOUND"):
        require_governed_viability(result, config.viability_ledger_path)


@pytest.mark.parametrize(
    ("reference", "expected"),
    [
        ("../escape.txt", Status.FAIL_BEHAVIOR),
        ("/tmp/absolute", Status.FAIL_BEHAVIOR),
        ("no path prose", Status.TOOLING_BLOCKED),
        ("evidence/proof.json and evidence/other.json", Status.FAIL_BEHAVIOR),
        ("evidence/empty.txt", Status.TOOLING_BLOCKED),
        ("evidence/bad.json", Status.FAIL_TOOLING),
    ],
)
def test_viability_rejects_bad_references(
    repository: Path, reference: str, expected: Status
):
    (repository / "evidence/other.json").write_text('{"ok":true}', encoding="utf-8")
    (repository / "evidence/empty.txt").write_text("", encoding="utf-8")
    (repository / "evidence/bad.json").write_text("{", encoding="utf-8")
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    config.token_matrix_path.write_text(
        MATRIX_HEADER + _matrix_row(reference), encoding="utf-8"
    )
    assert generate_acceptance_map_viability(config).status is expected


def test_viability_duplicate_or_orphan_tokens_fail_tooling(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    data = {
        "epic_id": "HDE-EPIC039",
        "tokens": [
            {
                "name": "QA_HARNESS_DISCIPLINE_OK",
                "owner_pf": "PF04",
                "status": "implemented",
                "evidence_titles": ["evidence/proof.json"],
            },
            {
                "name": "QA_HARNESS_DISCIPLINE_OK",
                "owner_pf": "PF04",
                "status": "implemented",
                "evidence_titles": ["evidence/proof.json"],
            },
        ],
    }
    config.acceptance_map_path.write_text(json.dumps(data), encoding="utf-8")
    duplicate = generate_acceptance_map_viability(config)
    assert duplicate.status is Status.FAIL_TOOLING
    assert (
        duplicate.token_status["QA_HARNESS_DISCIPLINE_OK"]
        == "DUPLICATE_ACCEPTANCE_TOKEN"
    )
    data["tokens"] = [
        {
            "name": "QA_HARNESS_DISCIPLINE_OK",
            "owner_pf": "PF04",
            "status": "implemented",
            "evidence_titles": ["evidence/proof.json"],
        }
    ]
    config.acceptance_map_path.write_text(json.dumps(data), encoding="utf-8")
    config.token_matrix_path.write_text(
        config.token_matrix_path.read_text()
        + _matrix_row("evidence/proof.json", token="QA_HARNESS_ENTRYPOINT_SELFTEST_OK"),
        encoding="utf-8",
    )
    orphan = generate_acceptance_map_viability(config)
    assert orphan.status is Status.FAIL_TOOLING
    assert orphan.token_status["QA_HARNESS_ENTRYPOINT_SELFTEST_OK"] == "ORPHAN_MATRIX"


def test_wrong_epic_identity_is_tooling_failure_and_invalidates_tokens(
    repository: Path,
):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["epic_id"] = "HDE-EPIC040"
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")

    result = generate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "epic identity" in result.status_reason
    assert (
        result.token_status["QA_HARNESS_DISCIPLINE_OK"]
        == "ACCEPTANCE_MAP_IDENTITY_MISMATCH"
    )


@pytest.mark.parametrize(
    ("payload", "reason"),
    [
        ([], "epic identity"),
        ({"epic_id": "HDE-EPIC039", "tokens": {}}, "non-empty list"),
        ({"epic_id": "HDE-EPIC039", "tokens": []}, "non-empty list"),
        (
            {"epic_id": "HDE-EPIC039", "tokens": ["not-an-object"]},
            "not an object",
        ),
        (
            {
                "epic_id": "HDE-EPIC039",
                "tokens": [
                    {
                        "name": "not-a-canonical-token",
                        "owner_pf": "PF04",
                        "status": "implemented",
                        "evidence_titles": ["evidence/proof.json"],
                    }
                ],
            },
            "invalid name",
        ),
    ],
)
def test_malformed_acceptance_map_structure_is_tooling_failure(
    repository: Path, payload: object, reason: str
):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")

    result = generate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert reason in result.status_reason
    assert "VALID" not in result.token_status.values()


@pytest.mark.parametrize("owner_pf", [None, "", "PF19"])
def test_viability_requires_matching_acceptance_owner_pf(
    repository: Path, owner_pf: str | None
):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    token = {
        "name": "QA_HARNESS_DISCIPLINE_OK",
        "status": "implemented",
        "evidence_titles": ["evidence/proof.json"],
    }
    if owner_pf is not None:
        token["owner_pf"] = owner_pf
    config.acceptance_map_path.write_text(
        json.dumps({"epic_id": "HDE-EPIC039", "tokens": [token]}),
        encoding="utf-8",
    )
    result = generate_acceptance_map_viability(config)
    assert result.status is Status.FAIL_TOOLING
    assert "owner_pf" in result.status_reason
    assert result.token_status["QA_HARNESS_DISCIPLINE_OK"] == (
        "OWNER_MISMATCH" if owner_pf == "PF19" else "INVALID_ACCEPTANCE_OWNER"
    )


@pytest.mark.parametrize("evidence_titles", [None, [], [""], [1]])
def test_malformed_acceptance_evidence_titles_are_tooling_failure(
    repository: Path, evidence_titles: object
):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    payload["tokens"][0]["evidence_titles"] = evidence_titles
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")

    result = generate_acceptance_map_viability(config)

    assert result.status is Status.FAIL_TOOLING
    assert "evidence_titles" in result.status_reason
    assert (
        result.token_status["QA_HARNESS_DISCIPLINE_OK"]
        == "INVALID_ACCEPTANCE_EVIDENCE_TITLES"
    )


@pytest.mark.parametrize(
    ("map_status", "matrix_status", "expected", "disposition"),
    [
        ("implemented", "Implemented", Status.PASS, "VALID"),
        ("covered", "Covered", Status.PASS, "VALID"),
        ("satisfied", "Satisfied", Status.PASS, "VALID"),
        ("planned", "Implemented", Status.FAIL_TOOLING, "STATUS_MISMATCH"),
        (None, "Implemented", Status.FAIL_TOOLING, "INVALID_ACCEPTANCE_STATUS"),
        ("done", "Implemented", Status.FAIL_TOOLING, "INVALID_ACCEPTANCE_STATUS"),
        ("implemented", "done", Status.FAIL_TOOLING, "INVALID_MATRIX_STATUS"),
        ("implemented", "", Status.FAIL_TOOLING, "INVALID_MATRIX_STATUS"),
        ("planned", "Planned", Status.TOOLING_BLOCKED, "PLANNED"),
        (
            "token_incomplete",
            "Token-incomplete",
            Status.TOOLING_BLOCKED,
            "TOKEN_INCOMPLETE",
        ),
    ],
)
def test_viability_normalizes_and_compares_acceptance_posture(
    repository: Path,
    map_status: str | None,
    matrix_status: str,
    expected: Status,
    disposition: str,
):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    payload = json.loads(config.acceptance_map_path.read_text(encoding="utf-8"))
    if map_status is None:
        payload["tokens"][0].pop("status")
    else:
        payload["tokens"][0]["status"] = map_status
    config.acceptance_map_path.write_text(json.dumps(payload), encoding="utf-8")
    config.token_matrix_path.write_text(
        MATRIX_HEADER
        + _matrix_row("evidence/proof.json", status=matrix_status),
        encoding="utf-8",
    )

    result = generate_acceptance_map_viability(config)

    assert result.status is expected
    assert result.token_status["QA_HARNESS_DISCIPLINE_OK"] == disposition


def test_missing_and_malformed_inputs_are_structured(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    config.acceptance_map_path.unlink()
    assert generate_acceptance_map_viability(config).status is Status.TOOLING_BLOCKED
    config.acceptance_map_path.write_text("{", encoding="utf-8")
    assert generate_acceptance_map_viability(config).status is Status.FAIL_TOOLING


def test_writer_failure_is_fail_tooling(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
    monkeypatch.setattr(
        "tools.qa.qa_harness._atomic_write",
        lambda *_: (_ for _ in ()).throw(OSError("disk")),
    )
    result = generate_acceptance_map_viability(
        HarnessConfig("HDE-EPIC039", repo_root=repository)
    )
    assert result.status is Status.FAIL_TOOLING
    assert result.primary_log is None


def test_legacy_manifest_is_replaced_without_importing_run_state(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    historical = config.qa_root / "legacy-run/historical.log"
    historical.parent.mkdir(parents=True)
    historical.write_text("historical bytes\n", encoding="utf-8")
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps(
            {
                "epic_id": config.epic_id,
                "runs": [
                    {
                        "run_id": "old",
                        "produced_at_utc": "old",
                        "steps": [{"log_path": str(historical), "status": "PASS"}],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    before = historical.read_bytes()
    record_check(
        config,
        CheckResult(
            "current",
            Status.PASS,
            exit_code=0,
            command=("true",),
            command_provenance="fixture",
        ),
    )
    payload = json.loads(manifest.read_text(encoding="utf-8"))
    assert payload == {
        "current": {
            "check_id": "current",
            "log_path": "audit/qa/hde-epic039/checks/current/primary.log",
            "status": "PASS",
        }
    }
    assert historical.read_bytes() == before


def test_unknown_manifest_shape_fails_before_primary_log(repository: Path):
    config = HarnessConfig("HDE-EPIC039", repo_root=repository)
    manifest = config.qa_root / "qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps({"epic_id": config.epic_id, "steps": []}), encoding="utf-8"
    )
    with pytest.raises(ValueError, match="unknown QA manifest shape"):
        record_check(
            config,
            CheckResult(
                "current",
                Status.PASS,
                exit_code=0,
                command=("true",),
                command_provenance="fixture",
            ),
        )
    assert not (config.qa_root / "checks/current/primary.log").exists()


def test_publication_rolls_back_when_manifest_write_fails(
    repository: Path, monkeypatch: pytest.MonkeyPatch
):
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
        record_check(
            config,
            CheckResult(
                "current",
                Status.PASS,
                exit_code=0,
                command=("true",),
                command_provenance="fixture",
            ),
        )
    assert manifest.read_text(encoding="utf-8") == original
    assert not (config.qa_root / "checks/current/primary.log").exists()


@pytest.mark.parametrize(
    ("returncode", "expected"),
    [
        (0, Status.PASS),
        (1, Status.FAIL_BEHAVIOR),
        (2, Status.FAIL_TOOLING),
        (3, Status.FAIL_TOOLING),
        (4, Status.FAIL_TOOLING),
        (5, Status.TOOLING_BLOCKED),
        (-9, Status.FAIL_TOOLING),
    ],
)
def test_pytest_returncode_classification_is_causal(returncode, expected):
    assert classify_pytest_returncode(returncode) is expected


def test_pytest_returncode_classification_rejects_non_integer():
    with pytest.raises(ValueError, match="integer"):
        classify_pytest_returncode(True)


@pytest.fixture
def crd_config(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> HarnessConfig:
    # Deliberately no Epic map, matrix, PF registry or viability ledger.
    for key, value in {
        "ALLOW_NETWORK": "0", "SAFE_MODE": "1", "LANG": "C",
        "LC_ALL": "C", "TZ": "UTC", "APP_ENV": "test",
    }.items():
        monkeypatch.setenv(key, value)
    return HarnessConfig(crd_id="HDE-CRD-0001", repo_root=tmp_path)


def _crd_result(check_id: str = "current") -> CheckResult:
    return CheckResult(
        check_id, Status.PASS, command=("fixture-command",), exit_code=0,
        command_provenance="unit fixture; no live QA outcome asserted",
    )


def test_crd_config_preserves_epic_positional_interface(crd_config):
    root = crd_config.repo_root
    for config in (
        HarnessConfig("HDE-EPIC039", root, ("one",)),
        HarnessConfig(epic_id="HDE-EPIC039", repo_root=root, step_names=("one",)),
    ):
        assert config.epic_number == "039"
        assert config.qa_root == root / "audit/qa/hde-epic039"
        assert config.acceptance_map_path == root / "docs/acceptance_map_epic039.json"
        assert config.token_matrix_path == config.qa_root / "token_evidence_matrix.md"
        assert config.viability_ledger_path == config.qa_root / "acceptance_map_viability.log"
        assert config.step_names == ("one",)
    assert crd_config.epic_id is None
    assert crd_config.qa_root == root / "audit/qa/hde-crd-0001"
    assert all(getattr(crd_config, field) is None for field in (
        "epic_number", "acceptance_map_path", "token_matrix_path", "viability_ledger_path"
    ))
    assert list(root.iterdir()) == []


@pytest.mark.parametrize("identifiers", [
    {}, {"epic_id": "HDE-EPIC039", "crd_id": "HDE-CRD-0001"},
    {"crd_id": ""}, {"crd_id": 1}, {"epic_id": 1},
    *({"crd_id": value} for value in (
        "hde-crd-0001", "HDE-CRD-1", "HDE-CRD-00001", "HDE-CRD-0001/../x",
        "HDE-CRD-0001\n", "HDE-CRD-０００１",
    )),
])
def test_crd_config_rejects_ambiguous_or_unsafe_identity(tmp_path, identifiers):
    with pytest.raises(ValueError):
        HarnessConfig(repo_root=tmp_path, **identifiers)
    assert list(tmp_path.iterdir()) == []


@pytest.mark.parametrize("target", ["root", "audit", "audit/qa", "audit/qa/hde-crd-0001"])
def test_crd_config_rejects_symlinked_root_and_ancestors(tmp_path, target):
    repo, external = tmp_path / "repo", tmp_path / "external"
    external.mkdir()
    if target == "root":
        repo.symlink_to(external, target_is_directory=True)
    else:
        path = repo / target
        path.parent.mkdir(parents=True)
        path.symlink_to(external, target_is_directory=True)
    with pytest.raises(ValueError, match="aliased|symlink"):
        HarnessConfig(crd_id="HDE-CRD-0001", repo_root=repo)
    assert list(external.iterdir()) == []


def test_crd_ordinary_recording_and_supersession_need_no_epic_inputs(crd_config):
    first, manifest = record_check(crd_config, _crd_result("first"))
    second = write_primary_log(crd_config, _crd_result("second"))
    assert update_manifest(crd_config, second) == manifest
    assert set(validate_crd_check_family(crd_config)) == {"first", "second"}
    old_bytes = first.read_bytes()
    record_check(crd_config, _crd_result("replacement"), supersede_check_ids=("first",))
    assert set(validate_crd_check_family(crd_config)) == {"replacement", "second"}
    assert first.read_bytes() == old_bytes
    assert not (crd_config.repo_root / "docs").exists()
    assert not (crd_config.qa_root / "token_evidence_matrix.md").exists()


@pytest.mark.parametrize("status", list(Status))
def test_crd_statuses_retain_full_v2_and_empty_claims(crd_config, status):
    if status is Status.PASS:
        result = _crd_result()
    elif status is Status.FAIL_BEHAVIOR:
        result = replace(_crd_result(), status=status, exit_code=1, status_reason="fixture assertion failed")
    else:
        result = CheckResult(
            "current", status,
            "Fixture prerequisite unavailable" if status is not Status.PARKED else
            "Fixture owner parked this check outside present scope; reactivate when the prerequisite is approved",
        )
    logs, manifest = record_check_family(crd_config, (result,), captured_at_utc=FIXED_TIMESTAMP)
    raw = logs[0].read_bytes()
    header = read_primary_header(logs[0])
    assert len(header) == 14
    assert header["schema_version"] == "pf27.step_log_header.v2"
    assert header["claimed_tokens"] == header["intended_tokens"] == []
    assert header["status"] == status.value
    assert raw.endswith(b"\n") and b"\r" not in raw
    assert raw.split(b"\n")[0] == json.dumps(header, sort_keys=True, separators=(",", ":")).encode()
    assert validate_crd_check_family(crd_config)["current"]["status"] == status.value
    before = (raw, manifest.read_bytes())
    record_check_family(crd_config, (result,), captured_at_utc=FIXED_TIMESTAMP)
    assert (logs[0].read_bytes(), manifest.read_bytes()) == before


def test_crd_intentions_are_explicitly_unclaimed(crd_config):
    log, _ = record_check(crd_config, replace(_crd_result(), intended_tokens=("FIXTURE_INTENTION",)))
    assert read_primary_header(log)["claimed_tokens"] == []
    assert qa_harness.NONCLAIM_EXPLANATION in log.read_text().splitlines()[1:]


@pytest.mark.parametrize("mutation", [
    {"status": Status.PARKED, "status_reason": "not currently authorized"},
    {"status": Status.FAIL_BEHAVIOR, "status_reason": "unexecuted", "command": (), "exit_code": None, "command_provenance": "Not executed"},
    {"intended_tokens": "TOKEN"}, {"intended_tokens": {"TOKEN": True}},
    {"evidence_artifacts": "audit/fixture.log"}, {"output": "hidden\r\nnormalization"},
])
def test_crd_rejects_invalid_outcomes_before_writing(crd_config, mutation):
    result = replace(_crd_result(), **mutation)
    with pytest.raises(ValueError):
        record_check(crd_config, result)
    assert not crd_config.qa_root.exists()


@pytest.mark.parametrize("corruption", [
    "wrapper", "v1", "extra-entry-field", "status", "identity", "duplicate",
    "absolute", "traversal", "dot", "double-slash", "backslash", "foreign", "wrong-check",
    "manifest-crlf", "manifest-bom", "manifest-whitespace", "empty",
])
def test_crd_manifest_admission_refuses_malformed_current_bytes(crd_config, corruption):
    log, manifest = record_check(crd_config, _crd_result())
    checks = json.loads(manifest.read_bytes())
    entry = checks["current"]
    raw_path = entry["log_path"]
    if corruption == "wrapper":
        checks = {"epic_id": None, "checks": checks}
    elif corruption == "v1":
        log.write_text('{"schema_version":"pf27.step_log_header.v1","check_id":"current","status":"PASS"}\n')
    elif corruption == "extra-entry-field":
        entry["tokens"] = []
    elif corruption in {"status", "identity"}:
        entry["status" if corruption == "status" else "check_id"] = "PARKED" if corruption == "status" else "other"
    elif corruption in {"absolute", "traversal", "dot", "double-slash", "backslash", "foreign", "wrong-check"}:
        entry["log_path"] = {
            "absolute": str(log), "traversal": "../" + raw_path,
            "dot": raw_path.replace("/checks/", "/./checks/"),
            "double-slash": raw_path.replace("/checks/", "//checks/"),
            "backslash": raw_path.replace("/", "\\"),
            "foreign": raw_path.replace("0001", "0002"),
            "wrong-check": raw_path.replace("current", "other"),
        }[corruption]
    raw = (json.dumps(checks, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if corruption == "duplicate":
        raw = raw.replace(b'"check_id":"current"', b'"check_id":"current","check_id":"current"')
    elif corruption == "manifest-crlf":
        raw = raw.replace(b"\n", b"\r\n")
    elif corruption == "manifest-bom":
        raw = b"\xef\xbb\xbf" + raw
    elif corruption == "manifest-whitespace":
        raw = b" " + raw
    elif corruption == "empty":
        raw = b"{}\n"
    manifest.write_bytes(raw)
    before = (manifest.read_bytes(), log.read_bytes())
    with pytest.raises(ValueError):
        validate_crd_check_family(crd_config)
    with pytest.raises(ValueError):
        record_check(crd_config, _crd_result("new"))
    assert (manifest.read_bytes(), log.read_bytes()) == before
    assert not (crd_config.qa_root / "checks/new").exists()


@pytest.mark.parametrize("corruption", [
    "missing-field", "extra-field", "claims", "own-log", "header-id", "bad-command",
    "no-exit", "false-provenance", "no-reason", "parked-execution", "behavior-unexecuted",
    "crlf", "bom", "no-lf", "whitespace", "duplicate", "nonclaim", "invalid-utf8",
])
def test_crd_primary_admission_reuses_v2_and_checks_raw_bytes(crd_config, corruption):
    result = replace(_crd_result(), intended_tokens=("FIXTURE_INTENTION",))
    log, _ = record_check(crd_config, result)
    header = read_primary_header(log)
    if corruption == "missing-field":
        del header["captured_env"]
    elif corruption == "extra-field":
        header["crd_id"] = crd_config.crd_id
    else:
        changes = {
            "claims": {"claimed_tokens": ["FIXTURE_INTENTION"]},
            "own-log": {"evidence_artifacts": ["other.log"]},
            "header-id": {"check_id": "other"}, "bad-command": {"command": "true"},
            "no-exit": {"exit_code": None}, "false-provenance": {"command_provenance": "Not executed"},
            "no-reason": {"status": "FAIL_TOOLING"},
            "parked-execution": {"status": "PARKED", "status_reason": "parked"},
            "behavior-unexecuted": {"status": "FAIL_BEHAVIOR", "status_reason": "not run", "command": [], "command_provenance": "Not executed", "exit_code": None},
        }
        header.update(changes.get(corruption, {}))
    raw = (json.dumps(header, sort_keys=True, separators=(",", ":")) + "\n" + qa_harness.NONCLAIM_EXPLANATION + "\n").encode()
    if corruption == "crlf":
        raw = raw.replace(b"\n", b"\r\n")
    elif corruption == "bom":
        raw = b"\xef\xbb\xbf" + raw
    elif corruption == "no-lf":
        raw = raw.rstrip(b"\n")
    elif corruption == "whitespace":
        raw = b" " + raw
    elif corruption == "duplicate":
        raw = raw.replace(b'"status":"PASS"', b'"status":"PASS","status":"PASS"')
    elif corruption == "nonclaim":
        raw = raw.split(b"\n")[0] + b"\n"
    elif corruption == "invalid-utf8":
        raw += b"\xff\n"
    log.write_bytes(raw)
    with pytest.raises(ValueError):
        validate_crd_check_family(crd_config)
    assert log.read_bytes() == raw


@pytest.mark.parametrize("member", ["qa_step_logs_manifest.json", "checks/current/primary.log", "checks/current"])
def test_crd_validation_and_direct_update_refuse_aliases(crd_config, member):
    log, _ = record_check(crd_config, _crd_result())
    path = crd_config.qa_root / member
    moved = path.with_name(path.name + ".original")
    path.rename(moved)
    path.symlink_to(moved, target_is_directory=moved.is_dir())
    with pytest.raises(ValueError, match="symlink"):
        validate_crd_check_family(crd_config)
    with pytest.raises(ValueError, match="symlink"):
        update_manifest(crd_config, log)


def test_crd_rechecks_captured_bytes_during_validation(crd_config, monkeypatch):
    log, _ = record_check(crd_config, _crd_result())
    original = qa_harness._read_stable_acceptance_file
    calls = 0

    def mutate_after_capture(*args, **kwargs):
        nonlocal calls
        captured = original(*args, **kwargs)
        if args[1] == log:
            calls += 1
            if calls == 1:
                log.write_bytes(log.read_bytes() + b"changed during validation\n")
        return captured

    monkeypatch.setattr(qa_harness, "_read_stable_acceptance_file", mutate_after_capture)
    with pytest.raises(ValueError, match="changed"):
        validate_crd_check_family(crd_config)


def test_crd_legacy_operations_refuse_before_output(crd_config):
    for operation in (evaluate_acceptance_map_viability, generate_acceptance_map_viability):
        with pytest.raises(ValueError, match="unsupported for CRD"):
            operation(crd_config)
    for kwargs in ({"replace_legacy_family_ids": ("current",)}, {"admit_new_check_ids": ("current",)}):
        with pytest.raises(ValueError, match="legacy-family"):
            record_check_family(crd_config, (_crd_result(),), **kwargs)
    assert not crd_config.qa_root.exists()


@pytest.mark.parametrize("expression, expected", [("True", Status.PASS), ("False", Status.FAIL_BEHAVIOR)])
def test_crd_pytest_runner_records_actual_same_interpreter_outcome(crd_config, expression, expected):
    test_file = crd_config.repo_root / "test_fixture.py"
    test_file.write_text(f"def test_observation():\n    assert {expression}\n")
    result = run_pytest_check(crd_config, "executed", ("-q", "-p", "no:cacheprovider", "test_fixture.py"))
    assert result.status is expected
    assert result.command[0][0] == sys.executable
    assert "CRD wrapper" in result.command_provenance
    log, _ = record_check(crd_config, result)
    header = read_primary_header(log)
    assert header["exit_code"] == (0 if expected is Status.PASS else 1)
    assert validate_crd_check_family(crd_config)["executed"]["status"] == expected.value
