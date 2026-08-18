from __future__ import annotations

import contextlib
import json
import subprocess
from pathlib import Path
from typing import Mapping, Sequence

import pytest

from tools.qa import generate_epic029_close_pack as epic029
from tools.qa.qa_harness import Status


def _repository_fixture(root: Path) -> None:
    for rel in epic029._required_requalification_paths():
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("fixture\n", encoding="utf-8")


def _sanity_pass_bytes() -> bytes:
    lines = [
        "run:sanity-pipeline",
        "pipeline_identity:HDE-EPIC038-PR06-release-sanity",
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC",
        "env_pins:audit/gates/determinism/env_pins.log",
        "ops_evidence:retained_integrity_provenance_secret_safe_only;historical_nonclaim=true;not_rerun=true",
    ]
    for name in epic029.SANITY_STAGE_NAMES:
        lines.append(f"check {name}:OK")
        if name == "12 Historical bridge evidence integrity":
            lines.append("stage_result:12:HISTORICAL_INTEGRITY_OK")
    lines.extend(("first_failed_stage:NONE", "summary:PASS", ""))
    return "\n".join(lines).encode("utf-8")


def _legacy_family(root: Path) -> None:
    checks: dict[str, dict[str, str]] = {}
    for check_id in epic029.REQUALIFICATION_CHECK_IDS:
        rel = f"checks/{check_id}/primary.log"
        path = root / "audit/qa/hde-epic029" / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            f"[check_id] {check_id}\n[status] ungoverned\n[exit_code] 0\n",
            encoding="utf-8",
        )
        checks[check_id] = {
            "check_id": check_id,
            "log_path": rel,
            "status": "PASS",
        }
    manifest = root / "audit/qa/hde-epic029/qa_step_logs_manifest.json"
    manifest.write_text(
        json.dumps({"epic_id": epic029.EPIC_ID, "checks": checks}) + "\n",
        encoding="utf-8",
    )


class PassingRunner:
    def __init__(self, root: Path, *, post_stdout: str = "sanity receipt\n") -> None:
        self.root = root
        self.post_stdout = post_stdout
        self.calls: list[tuple[tuple[str, ...], Path, dict[str, str]]] = []

    def __call__(
        self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
    ) -> subprocess.CompletedProcess[str]:
        command = tuple(argv)
        self.calls.append((command, cwd, dict(env)))
        if command[-2:] == ("pytest", "--version"):
            stdout = "pytest 9.0.3\n"
        elif "--collect-only" in command:
            nodes = [f"{path}::test_fixture" for path in epic029.LIVE_QA_TESTS]
            stdout = "\n".join((*nodes, f"{len(nodes)} tests collected in 0.01s", ""))
        elif "pytest" in command and "-q" in command:
            stdout = "... [100%]\n3 passed in 1.39s\n"
        elif command == (epic029.PRECOMMIT_SCRIPTS[0],):
            stdout = "[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC\n"
        elif command[-1:] == (epic029.SANITY_PIPELINE_PATH,):
            path = self.root / epic029.SANITY_LOG_REL
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(_sanity_pass_bytes())
            stdout = self.post_stdout
        else:
            stdout = ""
        return subprocess.CompletedProcess(command, 0, stdout, "")


def test_fixed_family_uses_exact_ordered_argv(tmp_path: Path) -> None:
    _repository_fixture(tmp_path)
    runner = PassingRunner(tmp_path)

    run = epic029.run_requalification_family(
        tmp_path,
        runner=runner,
        environ={},
        python_executable="/venv/bin/python",
    )

    expected = [
        ("/venv/bin/python", "-m", "pytest", "--version"),
        (
            "/venv/bin/python",
            "-m",
            "pytest",
            "--collect-only",
            "-q",
            "-p",
            "no:cacheprovider",
            *epic029.LIVE_QA_TESTS,
        ),
        (
            "/venv/bin/python",
            "-m",
            "pytest",
            "-q",
            "-p",
            "no:cacheprovider",
            *epic029.LIVE_QA_TESTS,
        ),
        *((script,) for script in epic029.PRECOMMIT_SCRIPTS),
        ("/venv/bin/python", epic029.SANITY_PIPELINE_PATH),
    ]
    assert [call[0] for call in runner.calls] == expected
    assert [result.check_id for result in run.results] == list(
        epic029.REQUALIFICATION_CHECK_IDS
    )
    assert all(result.status is Status.PASS for result in run.results)
    definitions = epic029.requalification_checks("/venv/bin/python")
    assert [result.command for result in run.results] == [
        (
            definition.commands[0]
            if len(definition.commands) == 1
            else definition.commands
        )
        for definition in definitions
    ]
    assert all(
        result.captured_env == epic029.CAPTURED_EXECUTION_ENV
        for result in run.results
    )
    assert all(call[1] == tmp_path for call in runner.calls)
    expected_env = {
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LANG": "C",
        "LC_ALL": "C",
        "PYTHONDONTWRITEBYTECODE": "1",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }
    assert all(
        all(call[2].get(key) == value for key, value in expected_env.items())
        for call in runner.calls
    )
    assert all("PYTHONHASHSEED" not in call[2] for call in runner.calls)
    assert all("PYTEST_ADDOPTS" not in call[2] for call in runner.calls)
    assert epic029.qa_harness.NONCLAIM_EXPLANATION in run.results[0].output


def test_default_runner_explicitly_disables_shell(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    observed: dict[str, object] = {}

    def fake_run(*args: object, **kwargs: object) -> subprocess.CompletedProcess[str]:
        observed["args"] = args
        observed["kwargs"] = kwargs
        return subprocess.CompletedProcess(args[0], 0, "ok", "")

    monkeypatch.setattr(epic029.subprocess, "run", fake_run)
    epic029._default_command_runner(("tool", "arg"), tmp_path, {"X": "1"})

    kwargs = observed["kwargs"]
    assert isinstance(kwargs, dict)
    assert kwargs["shell"] is False
    assert kwargs["check"] is False
    assert kwargs["cwd"] == tmp_path
    assert observed["args"] == (("tool", "arg"),)


def test_execution_environment_does_not_inherit_sensitive_or_pytest_controls() -> None:
    env = epic029._closed_execution_env(
        {
            "PATH": "/usr/bin",
            "PYTEST_ADDOPTS": "--ignore=tests/http/test_endpoint_catalog.py",
            "HD_API_KEY": "secret",
            "DATABASE_URL": "postgres://secret",
        }
    )

    assert env["PATH"].split(":", 1)[0] == str(Path(epic029.sys.executable).parent)
    assert env["PATH"].endswith(":/usr/bin")
    assert env["SAFE_MODE"] == "1"
    assert env["ALLOW_NETWORK"] == "0"
    assert "PYTEST_ADDOPTS" not in env
    assert "HD_API_KEY" not in env
    assert "DATABASE_URL" not in env


def test_staged_generated_inputs_use_exact_canonical_writers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    calls: list[tuple[tuple[str, ...], Path]] = []
    monkeypatch.setattr(
        epic029,
        "_run_required_command",
        lambda argv, root: calls.append((tuple(argv), root)),
    )

    epic029._refresh_staged_generated_inputs(tmp_path)

    assert calls == [
        ((epic029.sys.executable, script), tmp_path)
        for script in epic029.STAGED_INPUT_GENERATORS
    ]


def test_staged_inputs_are_refreshed_before_graph_preseal(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    (tmp_path / ".git").mkdir()
    events: list[str] = []
    preseal = object()
    run = object()
    config = object()

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "_missing_required_paths", lambda: [])
    monkeypatch.setattr(epic029, "_utc_now", lambda: "2026-08-18T12:00:00Z")
    monkeypatch.setattr(
        epic029,
        "_refresh_staged_generated_inputs",
        lambda _root: events.append("refresh-generated-inputs"),
    )
    monkeypatch.setattr(
        epic029,
        "run_preseal_requalification",
        lambda _root: events.append("run-preseal") or preseal,
    )
    monkeypatch.setattr(
        epic029,
        "_publish_truthful_preseal",
        lambda *_args: events.append("publish-preseal") or config,
    )
    monkeypatch.setattr(
        epic029,
        "_run_required_command",
        lambda *_args: events.append("updater"),
    )
    monkeypatch.setattr(
        epic029,
        "run_postcommit_requalification",
        lambda *_args: events.append("run-postcommit") or run,
    )
    monkeypatch.setattr(epic029, "require_complete_requalification", lambda *_args: None)
    monkeypatch.setattr(
        epic029,
        "live_qa_status_from_requalification",
        lambda *_args: {check_id: True for check_id in epic029.REQUALIFICATION_CHECK_IDS},
    )
    monkeypatch.setattr(
        epic029,
        "_evidence_index_status",
        lambda: {"human": True, "mirror": True, "hash": True},
    )
    monkeypatch.setattr(
        epic029, "_publish_complete_requalification_after_preseal", lambda *_args: None
    )
    monkeypatch.setattr(
        epic029,
        "_pf09_row_closure_gate",
        lambda *_args: {"ready_for_close_binding": True},
    )
    monkeypatch.setattr(epic029, "_require_protected_acceptance_map", lambda *_args: None)
    monkeypatch.setattr(epic029, "_write_token_matrix", lambda *_args: None)
    monkeypatch.setattr(epic029, "_publish_viability_with_requalification", lambda *_args: None)
    monkeypatch.setattr(epic029, "verify_postcommit_fixed_point", lambda *_args: None)
    monkeypatch.setattr(epic029, "_verify_manifest_paths", lambda: None)

    assert epic029._materialize_staged_close_pack() == 0
    assert events[:5] == [
        "refresh-generated-inputs",
        "run-preseal",
        "publish-preseal",
        "updater",
        "run-postcommit",
    ]


def test_live_qa_requires_every_module_and_exact_execution_count(tmp_path: Path) -> None:
    _repository_fixture(tmp_path)

    class IncompleteCollectionRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if "--collect-only" in command:
                node = f"{epic029.LIVE_QA_TESTS[0]}::test_fixture"
                return subprocess.CompletedProcess(
                    command, 0, f"{node}\n1 test collected in 0.01s\n", ""
                )
            return result

    incomplete = epic029.run_requalification_family(
        tmp_path,
        runner=IncompleteCollectionRunner(tmp_path),
        environ={},
        python_executable="python",
    )
    assert incomplete.result_for("po-epic-close-live-qa").status is Status.FAIL_TOOLING

    class CountMismatchRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if "pytest" in command and "-q" in command and "--collect-only" not in command:
                return subprocess.CompletedProcess(command, 0, "2 passed in 0.01s\n", "")
            return result

    mismatched = epic029.run_requalification_family(
        tmp_path,
        runner=CountMismatchRunner(tmp_path),
        environ={},
        python_executable="python",
    )
    assert mismatched.result_for("po-epic-close-live-qa").status is Status.FAIL_TOOLING


def test_legacy_exit_code_text_has_no_authority(tmp_path: Path) -> None:
    _repository_fixture(tmp_path)
    legacy = (
        tmp_path
        / "audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log"
    )
    legacy.parent.mkdir(parents=True, exist_ok=True)
    legacy.write_text("[check_id] po-epic-close-live-qa\n[exit_code] 0\n", encoding="utf-8")

    class FailingLiveRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if (
                "pytest" in command
                and "-q" in command
                and "--collect-only" not in command
            ):
                return subprocess.CompletedProcess(command, 1, "1 failed\n", "")
            return result

    run = epic029.run_requalification_family(
        tmp_path,
        runner=FailingLiveRunner(tmp_path),
        environ={},
        python_executable="python",
    )

    assert run.result_for("po-epic-close-live-qa").status is Status.FAIL_BEHAVIOR
    with pytest.raises(RuntimeError, match="EPIC029_REQUALIFICATION_FAILED"):
        epic029.require_complete_requalification(run)
    assert legacy.read_text(encoding="utf-8").endswith("[exit_code] 0\n")


def test_complete_family_publication_replaces_legacy_without_status_import(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _repository_fixture(tmp_path)
    _legacy_family(tmp_path)
    run = epic029.run_requalification_family(
        tmp_path,
        runner=PassingRunner(tmp_path),
        environ={},
        python_executable="python",
    )
    epic029.require_complete_requalification(run)
    monkeypatch.setattr(epic029, "ROOT", tmp_path)

    epic029._publish_initial_requalification(run, "2026-08-18T12:00:00Z")

    manifest = json.loads(
        (tmp_path / "audit/qa/hde-epic029/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert set(manifest) == set(epic029.REQUALIFICATION_CHECK_IDS)
    for check_id in epic029.REQUALIFICATION_CHECK_IDS:
        primary = (
            tmp_path
            / f"audit/qa/hde-epic029/checks/{check_id}/primary.log"
        )
        header = json.loads(primary.read_text(encoding="utf-8").splitlines()[0])
        result = run.result_for(check_id)
        assert header["schema_version"] == "pf27.step_log_header.v2"
        assert header["status"] == "PASS"
        assert header["timestamp_utc"] == "2026-08-18T12:00:00Z"
        expected_command = (
            list(result.command)
            if result.command and isinstance(result.command[0], str)
            else [list(argv) for argv in result.command]
        )
        assert header["command"] == expected_command
        assert header["captured_env"] == dict(epic029.CAPTURED_EXECUTION_ENV)
        assert "[exit_code] 0" not in primary.read_text(encoding="utf-8")


def test_truthful_preseal_creates_every_registered_path_before_first_sanity(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _repository_fixture(tmp_path)
    _legacy_family(tmp_path)
    inherited = (
        "docs/acceptance_map_epic029.json",
        "audit/qa/hde-epic029/token_evidence_matrix.md",
        "audit/EPIC-029_close_report.md",
        "audit/EPIC-029_MANIFEST.json",
    )
    for rel in inherited:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("inherited\n", encoding="utf-8")
    runner = PassingRunner(tmp_path)
    preseal = epic029.run_preseal_requalification(
        tmp_path,
        runner=runner,
        environ={},
        python_executable="python",
    )
    epic029.require_preseal_requalification(preseal)
    viability_path = tmp_path / "audit/qa/hde-epic029/acceptance_map_viability.log"
    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "VIABILITY_LOG_PATH", viability_path)

    config = epic029._publish_truthful_preseal(
        preseal,
        "2026-08-18T12:00:00Z",
    )

    assert all(
        command[-1:] != (epic029.SANITY_PIPELINE_PATH,)
        for command, _, _ in runner.calls
    )
    registered = {
        *inherited,
        "audit/qa/hde-epic029/acceptance_map_viability.log",
        "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        *{
            f"audit/qa/hde-epic029/checks/{check_id}/primary.log"
            for check_id in (
                *epic029.REQUALIFICATION_CHECK_IDS,
                "acceptance-map-viability",
            )
        },
    }
    assert len(registered) == 10
    assert all((tmp_path / rel).is_file() for rel in registered)
    manifest = json.loads(
        (tmp_path / "audit/qa/hde-epic029/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert manifest["po-epic-close-live-qa"]["status"] == "PASS"
    assert manifest["po-precommit"]["status"] == "PASS"
    assert manifest["po-postcommit"]["status"] == "TOOLING_BLOCKED"
    assert manifest["acceptance-map-viability"]["status"] == "TOOLING_BLOCKED"
    assert json.loads(viability_path.read_text(encoding="utf-8"))["status"] == "TOOLING_BLOCKED"

    completed = epic029.run_postcommit_requalification(
        tmp_path,
        preseal,
        runner=runner,
        environ={},
        python_executable="python",
    )
    epic029.require_complete_requalification(completed)
    epic029._publish_complete_requalification_after_preseal(
        config,
        completed,
        "2026-08-18T12:00:00Z",
    )
    manifest = json.loads(
        (tmp_path / "audit/qa/hde-epic029/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert manifest["po-postcommit"]["status"] == "PASS"
    assert manifest["acceptance-map-viability"]["status"] == "TOOLING_BLOCKED"


def test_truthful_preseal_is_idempotent_after_flat_v2_transition(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _repository_fixture(tmp_path)
    _legacy_family(tmp_path)
    preseal = epic029.run_preseal_requalification(
        tmp_path,
        runner=PassingRunner(tmp_path),
        environ={},
        python_executable="python",
    )
    viability_path = tmp_path / "audit/qa/hde-epic029/acceptance_map_viability.log"
    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "VIABILITY_LOG_PATH", viability_path)

    epic029._publish_truthful_preseal(preseal, "2026-08-18T12:00:00Z")
    epic029._publish_truthful_preseal(preseal, "2026-08-18T12:00:01Z")

    manifest = json.loads(
        (tmp_path / "audit/qa/hde-epic029/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert set(manifest) == {
        *epic029.REQUALIFICATION_CHECK_IDS,
        "acceptance-map-viability",
    }
    assert manifest["po-postcommit"]["status"] == "TOOLING_BLOCKED"


def test_protected_acceptance_map_must_match_current_closure_exactly(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    live = {check_id: True for check_id in epic029.REQUALIFICATION_CHECK_IDS}
    index = {
        "evidence_index_updated": True,
        "machine_mirror_updated": True,
        "evidence_index_hash": True,
    }
    gate = {
        "ready_for_close_binding": True,
        "row_closure_status": {},
    }
    acceptance_map = tmp_path / "docs/acceptance_map_epic029.json"
    acceptance_map.parent.mkdir(parents=True)
    monkeypatch.setattr(epic029, "ACCEPTANCE_MAP_PATH", acceptance_map)
    monkeypatch.setattr(
        epic029,
        "_tokens",
        lambda *_args: [{"name": "TESTS_PASS_OK", "status": "implemented"}],
    )
    expected = {
        "epic_id": epic029.EPIC_ID,
        "sequencing_gate": gate,
        "tokens": [{"name": "TESTS_PASS_OK", "status": "implemented"}],
    }
    acceptance_map.write_text(json.dumps(expected), encoding="utf-8")
    epic029._require_protected_acceptance_map(live, index, gate)

    expected["sequencing_gate"] = {"ready_for_close_binding": False}
    acceptance_map.write_text(json.dumps(expected), encoding="utf-8")
    with pytest.raises(RuntimeError, match="STALE_OR_MISMATCHED"):
        epic029._require_protected_acceptance_map(live, index, gate)


def test_viability_joins_requalified_family_with_same_timestamp(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _repository_fixture(tmp_path)
    _legacy_family(tmp_path)
    run = epic029.run_requalification_family(
        tmp_path,
        runner=PassingRunner(tmp_path),
        environ={},
        python_executable="python",
    )
    timestamp = "2026-08-18T12:00:00Z"
    ledger = (
        '{"epic_id":"HDE-EPIC029","status":"PASS",'
        '"status_reason":"","token_status":{}}\n'
    )
    viability = epic029.qa_harness.CheckResult(
        "acceptance-map-viability",
        Status.PASS,
        check_name="Acceptance-map viability",
        command=("python", "tools/qa/generate_epic029_close_pack.py"),
        command_provenance="test fixture",
        exit_code=0,
        output=ledger,
        evidence_artifacts=(
            "audit/qa/hde-epic029/checks/acceptance-map-viability/primary.log",
        ),
    )
    viability_path = tmp_path / "audit/qa/hde-epic029/acceptance_map_viability.log"
    evaluation_calls: list[dict[str, object]] = []
    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "VIABILITY_LOG_PATH", viability_path)
    monkeypatch.setattr(
        epic029.qa_harness,
        "evaluate_acceptance_map_viability",
        lambda config, **kwargs: evaluation_calls.append(kwargs) or (viability, ledger),
    )
    config = epic029._publish_initial_requalification(run, timestamp)

    epic029._publish_viability_with_requalification(config, run, timestamp)

    manifest = json.loads(
        (tmp_path / "audit/qa/hde-epic029/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    assert set(manifest) == {
        *epic029.REQUALIFICATION_CHECK_IDS,
        "acceptance-map-viability",
    }
    assert viability_path.read_text(encoding="utf-8") == ledger
    assert evaluation_calls == [{"planned_governed_ledger": True}]
    for check_id in manifest:
        header = json.loads(
            (
                tmp_path
                / f"audit/qa/hde-epic029/checks/{check_id}/primary.log"
            )
            .read_text(encoding="utf-8")
            .splitlines()[0]
        )
        assert header["timestamp_utc"] == timestamp


@pytest.mark.parametrize(
    ("failed_script", "expected_status"),
    [
        (epic029.PRECOMMIT_SCRIPTS[0], Status.TOOLING_BLOCKED),
        (epic029.PRECOMMIT_SCRIPTS[1], Status.FAIL_BEHAVIOR),
        (epic029.PRECOMMIT_SCRIPTS[2], Status.FAIL_TOOLING),
    ],
)
def test_precommit_failures_have_causal_status(
    tmp_path: Path, failed_script: str, expected_status: Status
) -> None:
    _repository_fixture(tmp_path)

    class GateFailureRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if command == (failed_script,):
                return subprocess.CompletedProcess(command, 1, "", "gate failed\n")
            return result

    run = epic029.run_requalification_family(
        tmp_path,
        runner=GateFailureRunner(tmp_path),
        environ={},
        python_executable="python",
    )

    assert run.result_for("po-precommit").status is expected_status


def test_zero_exit_without_pytest_summary_is_tooling_failure(tmp_path: Path) -> None:
    _repository_fixture(tmp_path)

    class MissingSummaryRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if (
                "pytest" in command
                and "-q" in command
                and "--collect-only" not in command
            ):
                return subprocess.CompletedProcess(command, 0, "completed\n", "")
            return result

    run = epic029.run_requalification_family(
        tmp_path,
        runner=MissingSummaryRunner(tmp_path),
        environ={},
        python_executable="python",
    )

    assert run.result_for("po-epic-close-live-qa").status is Status.FAIL_TOOLING


def test_zero_exit_with_malformed_sanity_result_is_tooling_failure(tmp_path: Path) -> None:
    _repository_fixture(tmp_path)

    class MalformedSanityRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if command[-1:] == (epic029.SANITY_PIPELINE_PATH,):
                (self.root / epic029.SANITY_LOG_REL).write_text(
                    "summary:PASS\n", encoding="utf-8"
                )
            return result

    run = epic029.run_requalification_family(
        tmp_path,
        runner=MalformedSanityRunner(tmp_path),
        environ={},
        python_executable="python",
    )

    assert run.result_for("po-postcommit").status is Status.FAIL_TOOLING


@pytest.mark.parametrize(
    "mutator",
    [
        lambda body: body + b"summary:FAIL\n",
        lambda body: body.replace(
            b"check 10 Architecture snapshot:OK\n",
            b"check 10 Architecture snapshot:OK\ncheck 10 Architecture snapshot:OK\n",
        ),
    ],
)
def test_contradictory_or_duplicate_sanity_lines_are_tooling_failure(
    tmp_path: Path,
    mutator: object,
) -> None:
    _repository_fixture(tmp_path)

    class ContradictorySanityRunner(PassingRunner):
        def __call__(
            self, argv: Sequence[str], cwd: Path, env: Mapping[str, str]
        ) -> subprocess.CompletedProcess[str]:
            result = super().__call__(argv, cwd, env)
            command = tuple(argv)
            if command[-1:] == (epic029.SANITY_PIPELINE_PATH,):
                path = self.root / epic029.SANITY_LOG_REL
                path.write_bytes(mutator(path.read_bytes()))
            return result

    run = epic029.run_requalification_family(
        tmp_path,
        runner=ContradictorySanityRunner(tmp_path),
        environ={},
        python_executable="python",
    )
    assert run.result_for("po-postcommit").status is Status.FAIL_TOOLING


def test_postcommit_fixed_point_requires_identical_receipt_bytes(tmp_path: Path) -> None:
    _repository_fixture(tmp_path)
    first_runner = PassingRunner(tmp_path, post_stdout="stable\n")
    run = epic029.run_requalification_family(
        tmp_path,
        runner=first_runner,
        environ={},
        python_executable="python",
    )
    epic029.require_complete_requalification(run)

    epic029.verify_postcommit_fixed_point(
        tmp_path,
        run,
        runner=PassingRunner(tmp_path, post_stdout="stable\n"),
        environ={},
        python_executable="python",
    )
    with pytest.raises(RuntimeError, match="EPIC029_POSTCOMMIT_NOT_FIXED_POINT"):
        epic029.verify_postcommit_fixed_point(
            tmp_path,
            run,
            runner=PassingRunner(tmp_path, post_stdout="changed\n"),
            environ={},
            python_executable="python",
        )


def test_token_matrix_contains_only_concrete_supported_locators(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    matrix = tmp_path / "audit/qa/hde-epic029/token_evidence_matrix.md"
    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "TOKEN_MATRIX_PATH", matrix)
    live = {check_id: True for check_id in epic029.REQUALIFICATION_CHECK_IDS}
    index = {
        "evidence_index_updated": True,
        "machine_mirror_updated": True,
        "evidence_index_hash": True,
    }
    gate = {"ready_for_close_binding": True}

    epic029._write_token_matrix(live, index, gate)
    text = matrix.read_text(encoding="utf-8")

    assert "Existing epic-close live QA output only" not in text
    assert "Bound by close-pack generator outputs" not in text
    assert (
        "python -m pytest -q -p no:cacheprovider " + " ".join(epic029.LIVE_QA_TESTS)
    ) in text
    assert "; ".join(epic029.PRECOMMIT_SCRIPTS) in text
    assert f"python {epic029.SANITY_PIPELINE_PATH}" in text


def test_staged_publication_restores_preimage_when_verification_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stage = tmp_path / "stage"
    target = tmp_path / "target"
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    protected_rel = "docs/acceptance_map_epic029.json"
    (stage / rel).parent.mkdir(parents=True)
    (target / rel).parent.mkdir(parents=True)
    (target / protected_rel).parent.mkdir(parents=True)
    (stage / rel).write_text("candidate\n", encoding="utf-8")
    (target / rel).write_text("preimage\n", encoding="utf-8")
    (target / protected_rel).write_text("protected\n", encoding="utf-8")

    def fail_verification(*args: object, **kwargs: object) -> None:
        raise RuntimeError("mocked final verification failure")

    monkeypatch.setattr(
        epic029.qa_harness,
        "verify_manifest_entry",
        fail_verification,
    )

    with pytest.raises(RuntimeError, match="mocked final verification failure"):
        epic029._publish_staged_candidate(stage, target, (rel,))

    assert (target / rel).read_bytes() == b"preimage\n"
    assert (target / protected_rel).read_bytes() == b"protected\n"


def test_orchestration_never_publishes_before_worktree_cleanup_succeeds(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    sanity = tmp_path / epic029.SANITY_LOG_REL
    sanity.parent.mkdir(parents=True)
    sanity.write_bytes(_sanity_pass_bytes())
    stage = tmp_path / "stage"
    staged_sanity = stage / epic029.SANITY_LOG_REL
    staged_sanity.parent.mkdir(parents=True)
    staged_sanity.write_bytes(sanity.read_bytes())
    published: list[object] = []

    @contextlib.contextmanager
    def failing_cleanup(_root: Path):
        yield stage
        raise RuntimeError("worktree cleanup failed")

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "_require_clean_git_head", lambda _root: None)
    monkeypatch.setattr(epic029, "_staging_worktree", failing_cleanup)
    monkeypatch.setattr(epic029, "_candidate_paths", lambda _stage: ())
    monkeypatch.setattr(epic029, "_capture_staged_candidate", lambda *_args: ())
    monkeypatch.setattr(
        epic029,
        "_publish_captured_candidate",
        lambda *args: published.append(args),
    )
    monkeypatch.setattr(
        epic029.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, "", ""),
    )

    with pytest.raises(RuntimeError, match="worktree cleanup failed"):
        epic029._orchestrate_from_clean_head()

    assert published == []


def test_publication_allowlist_excludes_protected_surfaces() -> None:
    allowed = epic029._publication_allowlist()
    assert "audit/qa/hde-epic029/token_evidence_matrix.md" in allowed
    assert "audit/qa/hde-epic029/acceptance_map_viability.log" in allowed
    assert "docs/acceptance_map_epic029.json" not in allowed
    assert "audit/EPIC-029_close_report.md" not in allowed
    assert "audit/EPIC-029_MANIFEST.json" not in allowed
    assert "audit/docdeltas/hde-epic029_doc_deltas.md" not in allowed
    assert "audit/ops/hde-epic029/ops-01/stdout.log" not in allowed
    assert epic029.SANITY_LOG_REL not in allowed
    for path in epic029.STAGED_INPUT_OUTPUTS:
        assert path in allowed
        assert f"{path}.path_proof.txt" in allowed


def test_candidate_discovery_accepts_only_allowlisted_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    completed = subprocess.CompletedProcess(("git", "status"), 0, f" M {rel}\0", "")
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    assert epic029._candidate_paths(tmp_path) == (rel,)


@pytest.mark.parametrize(
    "protected_path",
    [
        "docs/acceptance_map_epic029.json",
        "audit/EPIC-029_close_report.md",
        "audit/EPIC-029_MANIFEST.json",
        "audit/docdeltas/hde-epic029_doc_deltas.md",
        "audit/ops/hde-epic029/ops-01/stdout.log",
        "audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md",
        "audit/qa/hde-epic029/checks/po-001/primary.log",
        "audit/gates/sanity_pipeline/sanity_pipeline.log",
        "docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.1.md",
    ],
)
def test_candidate_discovery_rejects_protected_stage_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    protected_path: str,
) -> None:
    source_preimage = tmp_path / "source-preimage"
    source_preimage.write_bytes(b"unchanged\n")
    completed = subprocess.CompletedProcess(
        ("git", "status"), 0, f" M {protected_path}\0", ""
    )
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    with pytest.raises(RuntimeError, match="PROTECTED_STAGE_MUTATION"):
        epic029._candidate_paths(tmp_path)
    assert source_preimage.read_bytes() == b"unchanged\n"


@pytest.mark.parametrize(
    "proof_path",
    [
        "docs/acceptance_map_epic029.json.path_proof.txt",
        "audit/EPIC-029_close_report.md.path_proof.txt",
        "audit/EPIC-029_MANIFEST.json.path_proof.txt",
    ],
)
def test_candidate_discovery_admits_only_proofs_for_preserved_close_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    proof_path: str,
) -> None:
    completed = subprocess.CompletedProcess(
        ("git", "status"), 0, f" M {proof_path}\0", ""
    )
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    assert epic029._candidate_paths(tmp_path) == (proof_path,)
    assert proof_path in epic029._publication_allowlist()
    assert not epic029._is_protected_stage_path(proof_path)


def test_candidate_discovery_rejects_other_unexpected_stage_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    completed = subprocess.CompletedProcess(
        ("git", "status"), 0, "?? outside-contract.txt\0", ""
    )
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    with pytest.raises(RuntimeError, match="UNEXPECTED_STAGED_OUTPUTS"):
        epic029._candidate_paths(tmp_path)
