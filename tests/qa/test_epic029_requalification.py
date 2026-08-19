from __future__ import annotations

import contextlib
import json
import os
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


def _scope_orchestration_causality_to_sanity(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        epic029,
        "_causal_input_paths",
        lambda: (epic029.SANITY_LOG_REL,),
    )


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
    monkeypatch.setattr(
        epic029,
        "_write_acceptance_map",
        lambda *_args: events.append("write-acceptance-map"),
    )
    monkeypatch.setattr(
        epic029,
        "_verify_acceptance_map",
        lambda *_args: events.append("verify-acceptance-map"),
    )
    monkeypatch.setattr(
        epic029,
        "_write_token_matrix",
        lambda *_args: events.append("write-token-matrix"),
    )
    monkeypatch.setattr(epic029, "_publish_viability_with_requalification", lambda *_args: None)
    monkeypatch.setattr(epic029, "verify_postcommit_fixed_point", lambda *_args: None)
    monkeypatch.setattr(epic029, "_verify_close_pack_convergence", lambda *_args: None)
    monkeypatch.setattr(epic029, "_verify_manifest_paths", lambda: None)

    assert epic029._materialize_staged_close_pack() == 0
    assert events[:5] == [
        "refresh-generated-inputs",
        "run-preseal",
        "publish-preseal",
        "updater",
        "run-postcommit",
    ]
    assert events[5:9] == [
        "write-acceptance-map",
        "verify-acceptance-map",
        "write-token-matrix",
        "updater",
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


def test_acceptance_map_writer_and_verifier_bind_current_closure_canonically(
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
    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    monkeypatch.setattr(epic029, "ACCEPTANCE_MAP_PATH", acceptance_map)
    monkeypatch.setattr(
        epic029,
        "_tokens",
        lambda *_args: [{"name": "TESTS_PASS_OK", "status": "implemented"}],
    )
    expected = epic029._acceptance_map_payload(live, index, gate)
    epic029._write_acceptance_map(live, index, gate)

    assert acceptance_map.read_bytes() == (
        json.dumps(expected, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")
    epic029._verify_acceptance_map(acceptance_map, live, index, gate)

    acceptance_map.write_text(json.dumps(expected), encoding="utf-8")
    with pytest.raises(RuntimeError, match="NONCANONICAL"):
        epic029._verify_acceptance_map(acceptance_map, live, index, gate)

    stale = dict(expected)
    stale["sequencing_gate"] = {"ready_for_close_binding": False}
    acceptance_map.write_text(
        json.dumps(stale, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    with pytest.raises(RuntimeError, match="STALE_OR_MISMATCHED"):
        epic029._verify_acceptance_map(acceptance_map, live, index, gate)


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
            "audit/qa/hde-epic029/acceptance_map_viability.log",
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

    receipt = epic029._publish_viability_with_requalification(
        config, run, timestamp
    )

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
    assert receipt == epic029.ViabilityReceipt(viability, ledger)
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
        if check_id == "acceptance-map-viability":
            assert header["evidence_artifacts"] == [
                "audit/qa/hde-epic029/checks/acceptance-map-viability/primary.log",
                "audit/qa/hde-epic029/acceptance_map_viability.log",
            ]


def test_dormant_close_manifest_writer_uses_canonical_binding_keys(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    captured: list[dict[str, object]] = []
    monkeypatch.setattr(
        epic029,
        "_write_json",
        lambda _path, payload: captured.append(payload),
    )

    epic029._write_close_manifest(
        "2026-08-18T00:00:00Z",
        {check_id: True for check_id in epic029.REQUALIFICATION_CHECK_IDS},
        {
            "codespaces": "closed",
            "local_dev": "closed",
            "closure_mode": "binding-equivalence",
            "row_closure_status": {"HDE-CONJ001.4": "closed"},
        },
    )

    key_outputs = captured[0]["key_outputs"]
    assert key_outputs["acceptance_viability"] == (
        "audit/qa/hde-epic029/acceptance_map_viability.log"
    )
    assert key_outputs["step_logs_manifest"] == (
        "audit/qa/hde-epic029/qa_step_logs_manifest.json"
    )
    assert "acceptance_map_viability" not in key_outputs
    assert "qa_step_manifest" not in key_outputs


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
    assert "audit/gates/determinism/env_pins.log" in text
    assert "docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl" in text
    assert "artifacts/proofs/env_pins.txt" not in text
    assert "artifacts/evidence_index.jsonl.sha256" not in text


def test_acceptance_tokens_bind_only_governed_epic029_evidence() -> None:
    live = {check_id: True for check_id in epic029.REQUALIFICATION_CHECK_IDS}
    index = {
        "evidence_index_updated": True,
        "machine_mirror_updated": True,
        "evidence_index_hash": True,
    }
    tokens = {
        token["name"]: token
        for token in epic029._tokens(
            live,
            index,
            {"ready_for_close_binding": True},
        )
    }

    assert tokens["DOC_DELTA_PRESENT_OK"]["evidence_titles"] == [
        epic029.DOC_DELTAS_REL,
        epic029.DRAIN_TARGETS_REL,
    ]
    assert tokens["ENV_RAILS_POLICY_OK"]["evidence_titles"] == [
        "audit/gates/determinism/env_pins.log"
    ]
    assert tokens["EVIDENCE_INDEX_HASH_OK"]["evidence_titles"] == [
        "docs/evidence/INDEX.sha256",
        "artifacts/evidence_index.jsonl",
    ]


def test_staged_publication_restores_preimage_when_verification_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stage = tmp_path / "stage"
    target = tmp_path / "target"
    map_rel = epic029.ACCEPTANCE_MAP_REL
    proof_rel = epic029.ACCEPTANCE_MAP_PROOF_REL
    (stage / map_rel).parent.mkdir(parents=True)
    (target / map_rel).parent.mkdir(parents=True)
    (stage / map_rel).write_bytes(b'{"epic_id":"HDE-EPIC029"}\n')
    (stage / proof_rel).write_text("candidate proof\n", encoding="utf-8")
    (target / map_rel).write_bytes(b'{"epic_id":"source-preimage"}\n')
    (target / proof_rel).write_text("proof preimage\n", encoding="utf-8")

    def fail_verification(*args: object, **kwargs: object) -> None:
        raise RuntimeError("mocked final verification failure")

    monkeypatch.setattr(
        epic029.qa_harness,
        "verify_manifest_entry",
        fail_verification,
    )
    preimages = epic029._capture_publication_preimages(target)
    candidate = epic029._capture_staged_candidate(stage, (map_rel, proof_rel))

    with pytest.raises(RuntimeError, match="mocked final verification failure"):
        epic029._publish_captured_candidate(
            candidate,
            target,
            expected_preimages=preimages,
        )

    assert (target / map_rel).read_bytes() == b'{"epic_id":"source-preimage"}\n'
    assert (target / proof_rel).read_bytes() == b"proof preimage\n"


def test_git_head_preflight_never_queries_source_cleanliness(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    revision = "a" * 40
    unrelated = tmp_path / "local-untracked-notes.txt"
    unrelated.write_bytes(b"preserve me\n")
    calls: list[tuple[str, ...]] = []

    def fake_git(_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
        calls.append(args)
        if args == ("rev-parse", "--is-inside-work-tree"):
            return subprocess.CompletedProcess(args, 0, "true\n", "")
        if args == ("rev-parse", "--verify", "HEAD^{commit}"):
            return subprocess.CompletedProcess(args, 0, f"{revision}\n", "")
        raise AssertionError(f"unexpected Git query: {args}")

    monkeypatch.setattr(epic029, "_git_command", fake_git)

    assert epic029._require_git_head(tmp_path) == revision
    assert calls == [
        ("rev-parse", "--is-inside-work-tree"),
        ("rev-parse", "--verify", "HEAD^{commit}"),
    ]
    assert unrelated.read_bytes() == b"preserve me\n"


def test_orchestration_allows_stable_dirty_acceptance_targets(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    sanity = tmp_path / epic029.SANITY_LOG_REL
    sanity.parent.mkdir(parents=True)
    sanity.write_bytes(_sanity_pass_bytes())
    source_map = tmp_path / epic029.ACCEPTANCE_MAP_REL
    source_proof = tmp_path / epic029.ACCEPTANCE_MAP_PROOF_REL
    source_map.parent.mkdir(parents=True)
    source_map.write_bytes(b'{"epic_id":"local-edit"}\n')
    source_proof.write_text("source proof\n", encoding="utf-8")

    stage = tmp_path / "stage"
    staged_sanity = stage / epic029.SANITY_LOG_REL
    staged_map = stage / epic029.ACCEPTANCE_MAP_REL
    staged_proof = stage / epic029.ACCEPTANCE_MAP_PROOF_REL
    staged_sanity.parent.mkdir(parents=True)
    staged_map.parent.mkdir(parents=True)
    staged_sanity.write_bytes(sanity.read_bytes())
    staged_map.write_bytes(b'{"epic_id":"committed-preimage"}\n')
    staged_proof.write_text("source proof\n", encoding="utf-8")
    published: list[tuple[epic029.StagedCandidateFile, ...]] = []

    @contextlib.contextmanager
    def staged_worktree(_root: Path, _revision: str):
        yield stage

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    _scope_orchestration_causality_to_sanity(monkeypatch)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: "a" * 40)
    monkeypatch.setattr(epic029, "_staging_worktree", staged_worktree)
    monkeypatch.setattr(
        epic029,
        "_candidate_paths",
        lambda _stage: (),
    )
    monkeypatch.setattr(
        epic029.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, "", ""),
    )

    def publish(candidate, _root, **_kwargs):
        published.append(tuple(candidate))

    monkeypatch.setattr(
        epic029,
        "_publish_captured_candidate",
        publish,
    )

    assert epic029._orchestrate_from_head() == 0

    assert [item.rel for item in published[0]] == [
        epic029.ACCEPTANCE_MAP_REL,
        epic029.ACCEPTANCE_MAP_PROOF_REL,
    ]
    assert published[0][0].content == b'{"epic_id":"committed-preimage"}\n'
    assert source_map.read_bytes() == b'{"epic_id":"local-edit"}\n'
    assert source_proof.read_bytes() == b"source proof\n"


def test_orchestration_allows_unrelated_source_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    sanity = tmp_path / epic029.SANITY_LOG_REL
    sanity.parent.mkdir(parents=True)
    sanity.write_bytes(_sanity_pass_bytes())
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    target = tmp_path / rel
    target.parent.mkdir(parents=True)
    target.write_bytes(b"source preimage\n")
    unrelated = tmp_path / "local-untracked-notes.txt"
    unrelated.write_bytes(b"preserve me\n")

    stage = tmp_path / "stage"
    staged_sanity = stage / epic029.SANITY_LOG_REL
    staged_sanity.parent.mkdir(parents=True)
    staged_sanity.write_bytes(sanity.read_bytes())
    staged_target = stage / rel
    staged_target.parent.mkdir(parents=True)
    staged_target.write_bytes(b"candidate\n")
    staged_map = stage / epic029.ACCEPTANCE_MAP_REL
    staged_proof = stage / epic029.ACCEPTANCE_MAP_PROOF_REL
    staged_map.parent.mkdir(parents=True)
    staged_map.write_bytes(b'{"epic_id":"HDE-EPIC029"}\n')
    staged_proof.write_text("candidate proof\n", encoding="utf-8")
    published: list[tuple[epic029.StagedCandidateFile, ...]] = []

    @contextlib.contextmanager
    def successful_stage(_root: Path, revision: str):
        assert revision == "a" * 40
        yield stage

    def publish(
        candidate: Sequence[epic029.StagedCandidateFile],
        root: Path,
        *,
        expected_preimages: Mapping[str, epic029.PublicationTargetPreimage],
        expected_revision: str,
        source_stability_verifier,
    ) -> None:
        assert expected_preimages[rel].content == b"source preimage\n"
        assert expected_revision == "a" * 40
        captured = tuple(candidate)
        published.append(captured)
        (root / rel).write_bytes(captured[0].content)

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    _scope_orchestration_causality_to_sanity(monkeypatch)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: "a" * 40)
    monkeypatch.setattr(epic029, "_staging_worktree", successful_stage)
    monkeypatch.setattr(epic029, "_candidate_paths", lambda _stage: (rel,))
    monkeypatch.setattr(epic029, "_publish_captured_candidate", publish)
    monkeypatch.setattr(
        epic029.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, "", ""),
    )

    assert epic029._orchestrate_from_head() == 0
    assert published[0][0].content == b"candidate\n"
    assert target.read_bytes() == b"candidate\n"
    assert unrelated.read_bytes() == b"preserve me\n"


def test_publication_preserves_unrelated_source_drift(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    target = tmp_path / rel
    target.parent.mkdir(parents=True)
    target.write_bytes(b"stable local preimage\n")
    unrelated = tmp_path / "notes" / "untracked.txt"
    unrelated.parent.mkdir(parents=True)
    unrelated.write_bytes(b"unrelated local bytes\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    candidate = (epic029.StagedCandidateFile(rel, b"candidate\n", 0o640),)

    monkeypatch.setattr(
        epic029.qa_harness,
        "verify_manifest_entry",
        lambda *args, **kwargs: None,
    )
    monkeypatch.setattr(epic029, "_verify_viability_pair", lambda *args: None)
    monkeypatch.setattr(epic029, "_verify_manifest_paths", lambda *args: None)
    monkeypatch.setattr(epic029, "_run_required_command", lambda *args: None)

    epic029._publish_captured_candidate(
        candidate,
        tmp_path,
        expected_preimages=preimages,
    )

    assert target.read_bytes() == b"candidate\n"
    assert target.stat().st_mode & 0o777 == 0o640
    assert unrelated.read_bytes() == b"unrelated local bytes\n"


def test_publication_target_race_aborts_before_writes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rel = epic029.ACCEPTANCE_MAP_REL
    target = tmp_path / rel
    target.parent.mkdir(parents=True)
    target.write_bytes(b'{"epic_id":"initial"}\n')
    preimages = epic029._capture_publication_preimages(tmp_path)
    target.write_bytes(b'{"epic_id":"concurrent-change"}\n')
    writes: list[str] = []

    monkeypatch.setattr(
        epic029,
        "_publish_swap_at",
        lambda held, *_args: writes.append(held.rel),
    )

    with pytest.raises(RuntimeError, match=f"PUBLICATION_TARGET_CHANGED:{rel}"):
        epic029._publish_captured_candidate(
            (
                epic029.StagedCandidateFile(
                    rel,
                    b'{"epic_id":"HDE-EPIC029"}\n',
                    0o644,
                ),
            ),
            tmp_path,
            expected_preimages=preimages,
        )

    assert writes == []
    assert target.read_bytes() == b'{"epic_id":"concurrent-change"}\n'


def test_publication_rolls_back_when_source_head_changes_during_write(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    target = tmp_path / rel
    target.parent.mkdir(parents=True)
    target.write_bytes(b"stable source preimage\n")
    original_mode = target.stat().st_mode & 0o777
    unrelated = tmp_path / "local-untracked-notes.txt"
    unrelated.write_bytes(b"preserve me\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    expected_revision = "a" * 40
    current_revision = expected_revision
    publish_swap_at = epic029._publish_swap_at

    def advance_head_during_candidate_write(target, staged_file, expected):
        nonlocal current_revision
        swap = publish_swap_at(target, staged_file, expected)
        current_revision = "b" * 40
        return swap

    monkeypatch.setattr(
        epic029,
        "_require_git_head",
        lambda _root: current_revision,
    )
    monkeypatch.setattr(
        epic029,
        "_publish_swap_at",
        advance_head_during_candidate_write,
    )

    with pytest.raises(RuntimeError, match="EPIC029_SOURCE_HEAD_CHANGED"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o640),),
            tmp_path,
            expected_preimages=preimages,
            expected_revision=expected_revision,
        )

    assert target.read_bytes() == b"stable source preimage\n"
    assert target.stat().st_mode & 0o777 == original_mode
    assert unrelated.read_bytes() == b"preserve me\n"


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
    def failing_cleanup(_root: Path, _revision: str):
        yield stage
        raise RuntimeError("worktree cleanup failed")

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    _scope_orchestration_causality_to_sanity(monkeypatch)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: "a" * 40)
    monkeypatch.setattr(epic029, "_staging_worktree", failing_cleanup)
    monkeypatch.setattr(epic029, "_candidate_paths", lambda _stage: ())
    monkeypatch.setattr(epic029, "_capture_staged_candidate", lambda *_args: ())
    monkeypatch.setattr(
        epic029,
        "_publish_captured_candidate",
        lambda *args, **kwargs: published.append((args, kwargs)),
    )
    monkeypatch.setattr(
        epic029.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, "", ""),
    )

    with pytest.raises(RuntimeError, match="worktree cleanup failed"):
        epic029._orchestrate_from_head()

    assert published == []


def test_orchestration_never_publishes_after_source_head_changes(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    sanity = tmp_path / epic029.SANITY_LOG_REL
    sanity.parent.mkdir(parents=True)
    sanity.write_bytes(_sanity_pass_bytes())
    stage = tmp_path / "stage"
    staged_sanity = stage / epic029.SANITY_LOG_REL
    staged_sanity.parent.mkdir(parents=True)
    staged_sanity.write_bytes(sanity.read_bytes())
    revisions = iter(("a" * 40, "b" * 40))
    published: list[object] = []

    @contextlib.contextmanager
    def successful_cleanup(_root: Path, revision: str):
        assert revision == "a" * 40
        yield stage

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    _scope_orchestration_causality_to_sanity(monkeypatch)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: next(revisions))
    monkeypatch.setattr(epic029, "_staging_worktree", successful_cleanup)
    monkeypatch.setattr(epic029, "_candidate_paths", lambda _stage: ())
    monkeypatch.setattr(epic029, "_capture_staged_candidate", lambda *_args: ())
    monkeypatch.setattr(
        epic029,
        "_publish_captured_candidate",
        lambda *args, **kwargs: published.append((args, kwargs)),
    )
    monkeypatch.setattr(
        epic029.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, "", ""),
    )

    with pytest.raises(RuntimeError, match="EPIC029_SOURCE_HEAD_CHANGED"):
        epic029._orchestrate_from_head()

    assert published == []


def test_orchestration_never_publishes_after_source_sanity_changes(
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
    def source_sanity_changes_during_cleanup(_root: Path, _revision: str):
        yield stage
        sanity.write_bytes(b"concurrent source sanity change\n")

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    _scope_orchestration_causality_to_sanity(monkeypatch)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: "a" * 40)
    monkeypatch.setattr(
        epic029,
        "_staging_worktree",
        source_sanity_changes_during_cleanup,
    )
    monkeypatch.setattr(epic029, "_candidate_paths", lambda _stage: ())
    monkeypatch.setattr(epic029, "_capture_staged_candidate", lambda *_args: ())
    monkeypatch.setattr(
        epic029,
        "_publish_captured_candidate",
        lambda *args, **kwargs: published.append((args, kwargs)),
    )
    monkeypatch.setattr(
        epic029.subprocess,
        "run",
        lambda *args, **kwargs: subprocess.CompletedProcess(args[0], 0, "", ""),
    )

    with pytest.raises(RuntimeError, match="EPIC029_CAUSAL_INPUT_CHANGED"):
        epic029._orchestrate_from_head()

    assert published == []
    assert sanity.read_bytes() == b"concurrent source sanity change\n"


def test_publication_allowlist_admits_exact_generated_and_proof_surfaces() -> None:
    allowed = epic029._publication_allowlist()
    assert "audit/qa/hde-epic029/token_evidence_matrix.md" in allowed
    assert "audit/qa/hde-epic029/acceptance_map_viability.log" in allowed
    assert epic029.ACCEPTANCE_MAP_REL in allowed
    assert epic029.ACCEPTANCE_MAP_PROOF_REL in allowed
    assert "audit/EPIC-029_close_report.md" not in allowed
    assert "audit/EPIC-029_MANIFEST.json" not in allowed
    assert epic029.DOC_DELTAS_REL not in allowed
    assert epic029.DRAIN_TARGETS_REL not in allowed
    assert f"{epic029.DOC_DELTAS_REL}.path_proof.txt" in allowed
    assert f"{epic029.DRAIN_TARGETS_REL}.path_proof.txt" in allowed
    assert "audit/ops/hde-epic029/ops-01/stdout.log" not in allowed
    assert epic029.SANITY_LOG_REL not in allowed
    for path in epic029.STAGED_INPUT_OUTPUTS:
        assert path in allowed
        assert f"{path}.path_proof.txt" in allowed
    for proof_path in epic029.UPDATER_BOOTSTRAP_PROOF_PATHS:
        assert proof_path in allowed
        assert proof_path.removesuffix(".path_proof.txt") not in allowed


def test_candidate_discovery_accepts_only_allowlisted_output(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    completed = subprocess.CompletedProcess(("git", "status"), 0, f" M {rel}\0", "")
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    assert epic029._candidate_paths(tmp_path) == (rel,)


@pytest.mark.parametrize(
    "generated_path",
    [epic029.ACCEPTANCE_MAP_REL, epic029.ACCEPTANCE_MAP_PROOF_REL],
)
def test_candidate_discovery_accepts_canonical_acceptance_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    generated_path: str,
) -> None:
    completed = subprocess.CompletedProcess(
        ("git", "status"), 0, f" M {generated_path}\0", ""
    )
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    assert epic029._candidate_paths(tmp_path) == (generated_path,)
    assert not epic029._is_protected_stage_path(generated_path)


@pytest.mark.parametrize("proof_path", epic029.UPDATER_BOOTSTRAP_PROOF_PATHS)
def test_candidate_discovery_admits_exact_updater_bootstrap_proofs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    proof_path: str,
) -> None:
    completed = subprocess.CompletedProcess(
        ("git", "status"), 0, f"?? {proof_path}\0", ""
    )
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    assert epic029._candidate_paths(tmp_path) == (proof_path,)
    assert not epic029._is_protected_stage_path(proof_path)


def test_candidate_discovery_rejects_unregistered_cross_epic_proof(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    proof_path = (
        "audit/qa/hde-epic027/checks/gate_unregistered/"
        "primary.log.path_proof.txt"
    )
    completed = subprocess.CompletedProcess(
        ("git", "status"), 0, f"?? {proof_path}\0", ""
    )
    monkeypatch.setattr(epic029, "_git_command", lambda *args: completed)

    with pytest.raises(RuntimeError, match="UNEXPECTED_STAGED_OUTPUTS"):
        epic029._candidate_paths(tmp_path)


@pytest.mark.parametrize(
    "protected_path",
    [
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
        "audit/EPIC-029_close_report.md.path_proof.txt",
        "audit/EPIC-029_MANIFEST.json.path_proof.txt",
        f"{epic029.DOC_DELTAS_REL}.path_proof.txt",
        f"{epic029.DRAIN_TARGETS_REL}.path_proof.txt",
    ],
)
def test_candidate_discovery_admits_only_proofs_for_protected_primaries(
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


def _causal_file(root: Path, rel: str, content: bytes = b"governed\n") -> Path:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(content)
    return path


def test_causal_inputs_reject_source_vs_detached_byte_drift(tmp_path: Path) -> None:
    rel = "audit/ops/hde-epic029/ops-01/binding_disposition.md"
    source = tmp_path / "source"
    stage = tmp_path / "stage"
    _causal_file(source, rel, b"local_dev: not yet closed\n")
    _causal_file(stage, rel, b"local_dev: closed\n")

    source_snapshot = epic029._capture_causal_inputs(source, (rel,))
    stage_snapshot = epic029._capture_causal_inputs(stage, (rel,))

    with pytest.raises(RuntimeError, match="EPIC029_CAUSAL_INPUT_CHANGED"):
        epic029._require_causal_inputs_equal(
            source_snapshot,
            stage_snapshot,
            phase="test",
        )


def test_causal_input_contract_includes_config_sources_and_close_manifest() -> None:
    causal = set(epic029._causal_input_paths())

    assert set(epic029.STAGED_CONFIG_SOURCE_INPUTS) <= causal
    assert set(epic029.UPDATER_BOOTSTRAP_PRIMARY_PATHS) <= causal
    assert "audit/EPIC-029_MANIFEST.json" in causal
    assert set(epic029._close_binding_input_paths()) <= causal


@pytest.mark.parametrize("replacement", ["missing", "directory", "leaf-symlink"])
def test_causal_inputs_reject_missing_directory_and_leaf_aliases(
    tmp_path: Path,
    replacement: str,
) -> None:
    rel = "audit/ops/hde-epic029/ops-01/binding_disposition.md"
    root = tmp_path / replacement
    path = _causal_file(root, rel)
    path.unlink()
    if replacement == "directory":
        path.mkdir()
    elif replacement == "leaf-symlink":
        external = tmp_path / "external.txt"
        external.write_bytes(b"governed\n")
        path.symlink_to(external)

    with pytest.raises(RuntimeError, match="EPIC029_CAUSAL_INPUT_INVALID"):
        epic029._capture_causal_inputs(root, (rel,))


def test_causal_inputs_reject_symlinked_parent_even_when_bytes_match(
    tmp_path: Path,
) -> None:
    rel = "audit/ops/hde-epic029/ops-01/binding_disposition.md"
    root = tmp_path / "source"
    external_parent = tmp_path / "external" / "ops-01"
    external_parent.mkdir(parents=True)
    (external_parent / "binding_disposition.md").write_bytes(b"governed\n")
    aliased_parent = root / "audit/ops/hde-epic029/ops-01"
    aliased_parent.parent.mkdir(parents=True)
    aliased_parent.symlink_to(external_parent, target_is_directory=True)

    with pytest.raises(RuntimeError, match="EPIC029_CAUSAL_INPUT_INVALID"):
        epic029._capture_causal_inputs(root, (rel,))


def test_causal_mode_comparison_is_limited_to_direct_shell_entrypoints(
    tmp_path: Path,
) -> None:
    source = tmp_path / "source"
    stage = tmp_path / "stage"
    python_rel = "tools/qa/generate_epic029_close_pack.py"
    shell_rel = epic029.PRECOMMIT_SCRIPTS[0]
    source_python = _causal_file(source, python_rel)
    stage_python = _causal_file(stage, python_rel)
    source_shell = _causal_file(source, shell_rel)
    stage_shell = _causal_file(stage, shell_rel)
    source_python.chmod(0o644)
    stage_python.chmod(0o755)
    source_shell.chmod(0o644)
    stage_shell.chmod(0o755)

    python_source = epic029._capture_causal_inputs(source, (python_rel,))
    python_stage = epic029._capture_causal_inputs(stage, (python_rel,))
    epic029._require_causal_inputs_equal(
        python_source,
        python_stage,
        phase="interpreter-entrypoint",
    )

    shell_source = epic029._capture_causal_inputs(source, (shell_rel,))
    shell_stage = epic029._capture_causal_inputs(stage, (shell_rel,))
    with pytest.raises(RuntimeError, match="EPIC029_CAUSAL_INPUT_CHANGED"):
        epic029._require_causal_inputs_equal(
            shell_source,
            shell_stage,
            phase="direct-shell-entrypoint",
        )


def test_causal_snapshot_rejects_path_replacement_during_stable_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/ops/hde-epic029/ops-01/binding_disposition.md"
    _causal_file(tmp_path, rel, b"first inode\n")
    stable_read = epic029._stable_regular_bytes

    def replace_after_read(parent_fd: int, leaf: str, **kwargs):
        content, metadata = stable_read(parent_fd, leaf, **kwargs)
        os.unlink(leaf, dir_fd=parent_fd)
        descriptor = os.open(
            leaf,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o644,
            dir_fd=parent_fd,
        )
        try:
            os.write(descriptor, b"replacement inode\n")
        finally:
            os.close(descriptor)
        return content, metadata

    monkeypatch.setattr(epic029, "_stable_regular_bytes", replace_after_read)

    with pytest.raises(RuntimeError, match="UNSTABLE_REPOSITORY_READ"):
        epic029._capture_causal_inputs(tmp_path, (rel,))


def test_orchestration_rejects_causal_input_changed_inside_detached_stage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = epic029.SANITY_LOG_REL
    source_path = _causal_file(tmp_path, rel, _sanity_pass_bytes())
    stage = tmp_path / "stage"
    staged_path = _causal_file(stage, rel, source_path.read_bytes())
    published: list[object] = []

    @contextlib.contextmanager
    def staged_worktree(_root: Path, _revision: str):
        yield stage

    def mutate_stage(*args, **kwargs):
        staged_path.write_bytes(b"changed during materialization\n")
        return subprocess.CompletedProcess(args[0], 0, "", "")

    monkeypatch.setattr(epic029, "ROOT", tmp_path)
    _scope_orchestration_causality_to_sanity(monkeypatch)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: "a" * 40)
    monkeypatch.setattr(epic029, "_staging_worktree", staged_worktree)
    monkeypatch.setattr(epic029.subprocess, "run", mutate_stage)
    monkeypatch.setattr(
        epic029,
        "_publish_captured_candidate",
        lambda *args, **kwargs: published.append((args, kwargs)),
    )

    with pytest.raises(RuntimeError, match="EPIC029_CAUSAL_INPUT_CHANGED"):
        epic029._orchestrate_from_head()
    assert published == []


@pytest.mark.parametrize("concurrent_kind", ["file", "directory", "symlink"])
def test_rollback_preserves_concurrent_replacement_kind(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    concurrent_kind: str,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at

    def replace_after_candidate(target, staged_file, expected):
        swap = publish_swap_at(target, staged_file, expected)
        path.unlink()
        if concurrent_kind == "file":
            path.write_bytes(b"concurrent\n")
        elif concurrent_kind == "directory":
            path.mkdir()
        else:
            external = tmp_path / "external.txt"
            external.write_bytes(b"external\n")
            path.symlink_to(external)
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", replace_after_candidate)

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )

    if concurrent_kind == "file":
        assert path.read_bytes() == b"concurrent\n"
    elif concurrent_kind == "directory":
        assert path.is_dir()
    else:
        assert path.is_symlink()


def test_rollback_preserves_concurrent_create_when_target_was_missing(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = tmp_path / rel
    path.parent.mkdir(parents=True)
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at

    def create_after_candidate(target, staged_file, expected):
        swap = publish_swap_at(target, staged_file, expected)
        path.write_bytes(b"concurrent create\n")
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", create_after_candidate)

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"concurrent create\n"


def test_rollback_aggregates_conflicts_and_restores_uncontested_targets(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rels = (
        "audit/qa/hde-epic029/token_evidence_matrix.md",
        "audit/qa/hde-epic029/acceptance_map_viability.log",
    )
    paths = {rel: _causal_file(tmp_path, rel, f"old:{rel}\n".encode()) for rel in rels}
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at

    def conflict_every_write(target, staged_file, expected):
        swap = publish_swap_at(target, staged_file, expected)
        paths[target.rel].write_bytes(f"concurrent:{target.rel}\n".encode())
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", conflict_every_write)

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE") as exc_info:
        epic029._publish_captured_candidate(
            tuple(
                epic029.StagedCandidateFile(rel, f"candidate:{rel}\n".encode(), 0o644)
                for rel in rels
            ),
            tmp_path,
            expected_preimages=preimages,
        )
    message = str(exc_info.value)
    assert all(rel in message for rel in rels)
    assert all(paths[rel].read_bytes().startswith(b"concurrent:") for rel in rels)


def test_head_move_with_checkout_bytes_preserves_new_head_content(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"old head\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    current_revision = "a" * 40
    publish_swap_at = epic029._publish_swap_at

    def move_head_and_checkout(target, staged_file, expected):
        nonlocal current_revision
        swap = publish_swap_at(target, staged_file, expected)
        path.write_bytes(b"new head checkout\n")
        current_revision = "b" * 40
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", move_head_and_checkout)
    monkeypatch.setattr(epic029, "_require_git_head", lambda _root: current_revision)

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
            expected_revision="a" * 40,
        )
    assert path.read_bytes() == b"new head checkout\n"


def test_parent_symlink_swap_cannot_redirect_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    parent = path.parent
    moved_parent = tmp_path / "moved-parent"
    external_parent = tmp_path / "external-parent"
    external_parent.mkdir()
    external_target = external_parent / path.name
    external_target.write_bytes(b"external preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at

    def swap_parent_before_held_write(target, staged_file, expected):
        parent.rename(moved_parent)
        parent.symlink_to(external_parent, target_is_directory=True)
        return publish_swap_at(target, staged_file, expected)

    monkeypatch.setattr(epic029, "_publish_swap_at", swap_parent_before_held_write)

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert external_target.read_bytes() == b"external preimage\n"
    assert (moved_parent / path.name).read_bytes() == b"candidate\n"


def test_atomic_park_detects_same_bytes_new_inode_race_before_publish(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    renameat2 = epic029._renameat2
    raced = False
    replacement_inode = 0

    def race_before_park(parent_fd, source_leaf, target_leaf, flags):
        nonlocal raced, replacement_inode
        if (
            flags == 1
            and source_leaf == path.name
            and ".preimage." in target_leaf
            and not raced
        ):
            replacement = path.with_name("same-bytes-replacement.tmp")
            replacement.write_bytes(b"preimage\n")
            replacement.chmod(0o644)
            os.replace(replacement, path)
            replacement_inode = path.stat().st_ino
            raced = True
        return renameat2(parent_fd, source_leaf, target_leaf, flags)

    monkeypatch.setattr(epic029, "_renameat2", race_before_park)

    with pytest.raises(RuntimeError, match="PUBLICATION_TARGET_CHANGED"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"preimage\n"
    assert path.stat().st_ino == replacement_inode


def test_atomic_noreplace_preserves_concurrent_create_for_missing_target(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = tmp_path / rel
    path.parent.mkdir(parents=True)
    preimages = epic029._capture_publication_preimages(tmp_path)
    renameat2 = epic029._renameat2

    def create_before_noreplace(parent_fd, source_leaf, target_leaf, flags):
        if flags == 1 and target_leaf == path.name and not path.exists():
            path.write_bytes(b"concurrent create\n")
        return renameat2(parent_fd, source_leaf, target_leaf, flags)

    monkeypatch.setattr(epic029, "_renameat2", create_before_noreplace)

    with pytest.raises(OSError):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"concurrent create\n"


def test_atomic_noreplace_reports_retained_backup_on_create_after_park(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    renameat2 = epic029._renameat2
    backup_leaf = ""

    def create_after_park(parent_fd, source_leaf, target_leaf, flags):
        nonlocal backup_leaf
        result = renameat2(parent_fd, source_leaf, target_leaf, flags)
        if (
            flags == 1
            and source_leaf == path.name
            and ".preimage." in target_leaf
            and not backup_leaf
        ):
            backup_leaf = target_leaf
            path.write_bytes(b"concurrent create after park\n")
        return result

    monkeypatch.setattr(epic029, "_renameat2", create_after_park)

    with pytest.raises(
        RuntimeError,
        match="PUBLICATION_PARK_RECOVERY_INCOMPLETE",
    ) as exc_info:
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert backup_leaf in str(exc_info.value)
    assert path.read_bytes() == b"concurrent create after park\n"
    assert (path.parent / backup_leaf).read_bytes() == b"preimage\n"


def test_atomic_rollback_preserves_same_bytes_new_inode_replacement(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at
    replacement_inode = 0

    def replace_installed_candidate(target, staged_file, expected):
        nonlocal replacement_inode
        swap = publish_swap_at(target, staged_file, expected)
        replacement = path.with_name("same-candidate-replacement.tmp")
        replacement.write_bytes(b"candidate\n")
        replacement.chmod(0o644)
        os.replace(replacement, path)
        replacement_inode = path.stat().st_ino
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", replace_installed_candidate)

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"candidate\n"
    assert path.stat().st_ino == replacement_inode


def test_publish_exception_after_park_restores_exact_preimage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    original_inode = path.stat().st_ino
    preimages = epic029._capture_publication_preimages(tmp_path)
    renameat2 = epic029._renameat2

    def fail_candidate_install(parent_fd, source_leaf, target_leaf, flags):
        if (
            flags == 1
            and target_leaf == path.name
            and source_leaf != path.name
            and ".preimage." not in source_leaf
        ):
            raise OSError(5, "injected I/O failure")
        return renameat2(parent_fd, source_leaf, target_leaf, flags)

    monkeypatch.setattr(epic029, "_renameat2", fail_candidate_install)

    with pytest.raises(OSError, match="injected I/O failure"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"preimage\n"
    assert path.stat().st_ino == original_inode
    assert not tuple(path.parent.glob(f".{path.name}.*"))


def test_renameat2_unavailable_fails_before_target_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    original_inode = path.stat().st_ino
    preimages = epic029._capture_publication_preimages(tmp_path)
    monkeypatch.setattr(
        epic029,
        "_renameat2",
        lambda *_args: (_ for _ in ()).throw(RuntimeError("renameat2 unavailable")),
    )

    with pytest.raises(RuntimeError, match="renameat2 unavailable"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o640),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"preimage\n"
    assert path.stat().st_ino == original_inode
    assert not tuple(path.parent.glob(f".{path.name}.*"))


def test_successful_publication_cleans_private_leaves_and_closes_owned_fd(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at
    installed_fds: list[int] = []

    def capture_fd(target, staged_file, expected):
        swap = publish_swap_at(target, staged_file, expected)
        installed_fds.append(swap.installed_fd)
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", capture_fd)
    monkeypatch.setattr(epic029.qa_harness, "verify_manifest_entry", lambda *_args: None)
    monkeypatch.setattr(epic029, "_verify_viability_pair", lambda *_args: None)
    monkeypatch.setattr(epic029, "_verify_manifest_paths", lambda *_args: None)
    monkeypatch.setattr(epic029, "_run_required_command", lambda *_args: None)

    epic029._publish_captured_candidate(
        (epic029.StagedCandidateFile(rel, b"candidate\n", 0o640),),
        tmp_path,
        expected_preimages=preimages,
    )
    assert path.read_bytes() == b"candidate\n"
    assert path.stat().st_mode & 0o777 == 0o640
    assert not tuple(path.parent.glob(f".{path.name}.*"))
    assert installed_fds
    with pytest.raises(OSError):
        os.fstat(installed_fds[0])


def test_rollback_never_installs_same_bytes_replaced_backup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rel = "audit/qa/hde-epic029/token_evidence_matrix.md"
    path = _causal_file(tmp_path, rel, b"preimage\n")
    preimages = epic029._capture_publication_preimages(tmp_path)
    publish_swap_at = epic029._publish_swap_at
    tampered_backup: Path | None = None

    def replace_backup_after_publish(target, staged_file, expected):
        nonlocal tampered_backup
        swap = publish_swap_at(target, staged_file, expected)
        assert swap.backup_leaf is not None
        tampered_backup = path.parent / swap.backup_leaf
        replacement = path.with_name("backup-replacement.tmp")
        replacement.write_bytes(b"preimage\n")
        replacement.chmod(0o644)
        os.replace(replacement, tampered_backup)
        return swap

    monkeypatch.setattr(epic029, "_publish_swap_at", replace_backup_after_publish)
    monkeypatch.setattr(
        epic029.qa_harness,
        "verify_manifest_entry",
        lambda *_args: (_ for _ in ()).throw(RuntimeError("force rollback")),
    )

    with pytest.raises(RuntimeError, match="EPIC029_ROLLBACK_INCOMPLETE"):
        epic029._publish_captured_candidate(
            (epic029.StagedCandidateFile(rel, b"candidate\n", 0o644),),
            tmp_path,
            expected_preimages=preimages,
        )
    assert path.read_bytes() == b"candidate\n"
    assert tampered_backup is not None
    assert tampered_backup.read_bytes() == b"preimage\n"


def test_close_pack_convergence_replays_frozen_viability_without_reevaluation(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    snapshot = {
        "docs/acceptance_map_epic029.json": epic029.PublicationTargetPreimage(
            "file", b"stable\n", 0o644
        )
    }
    frozen_receipt = object()
    events: list[object] = []
    monkeypatch.setattr(epic029, "_capture_convergence_state", lambda _root: snapshot)
    monkeypatch.setattr(epic029, "_write_acceptance_map", lambda *_args: events.append("map"))
    monkeypatch.setattr(epic029, "_verify_acceptance_map", lambda *_args: events.append("verify"))
    monkeypatch.setattr(epic029, "_write_token_matrix", lambda *_args: events.append("matrix"))
    monkeypatch.setattr(
        epic029,
        "_replay_viability_receipt",
        lambda *_args: events.append(("viability", _args[-1])),
    )
    monkeypatch.setattr(
        epic029.qa_harness,
        "evaluate_acceptance_map_viability",
        lambda *_args, **_kwargs: pytest.fail(
            "convergence must not allocate a fresh pytest --basetemp receipt"
        ),
    )
    monkeypatch.setattr(epic029, "_run_required_command", lambda *_args: events.append("updater"))

    epic029._verify_close_pack_convergence(
        object(), object(), "timestamp", {}, {}, {}, frozen_receipt
    )

    assert events == [
        "map",
        "verify",
        "matrix",
        ("viability", frozen_receipt),
        "updater",
    ]


def test_close_pack_convergence_rejects_any_changed_publication_output(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    states = iter(
        (
            {"x": epic029.PublicationTargetPreimage("file", b"before\n", 0o644)},
            {"x": epic029.PublicationTargetPreimage("file", b"after\n", 0o644)},
        )
    )
    monkeypatch.setattr(epic029, "_capture_convergence_state", lambda _root: next(states))
    monkeypatch.setattr(epic029, "_write_acceptance_map", lambda *_args: None)
    monkeypatch.setattr(epic029, "_verify_acceptance_map", lambda *_args: None)
    monkeypatch.setattr(epic029, "_write_token_matrix", lambda *_args: None)
    monkeypatch.setattr(epic029, "_replay_viability_receipt", lambda *_args: None)
    monkeypatch.setattr(epic029, "_run_required_command", lambda *_args: None)

    with pytest.raises(RuntimeError, match="EPIC029_CLOSE_PACK_NOT_FIXED_POINT:x"):
        epic029._verify_close_pack_convergence(
            object(), object(), "timestamp", {}, {}, {}, object()
        )
