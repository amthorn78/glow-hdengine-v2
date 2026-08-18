#!/usr/bin/env python3
"""Generate and requalify the EPIC029 offline close pack.

The three close-pack QA checks are a current-state evidence family.  Their
historical bracket logs are retained only as preimages for a complete-family
replacement; neither those logs nor the legacy manifest is an authority for a
new result.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as _dt
import hashlib
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
from collections.abc import Callable, Iterator, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from tools.qa import qa_harness

EPIC_ID = "HDE-EPIC029"
EPIC_SLUG = "hde-epic029"
RUN_ID = "epic029-close"
PF09_TASK_ID = "HDE-CONJ009"
PF09_SUBTASK_ID = "HDE-CONJ009.1"
PF09_SCOPE = [
    {"task_id": "HDE-CONJ009", "subtask_id": "HDE-CONJ009.1"},
    {"task_id": "HDE-CONJ008", "subtask_id": "HDE-CONJ008.1"},
    {"task_id": "HDE-CONJ001", "subtask_id": "HDE-CONJ001.4"},
]

QA_ROOT = ROOT / "audit" / "qa" / EPIC_SLUG
OPS_ROOT = ROOT / "audit" / "ops" / EPIC_SLUG / "ops-01"
CLOSURE_MODE = "binding-equivalence"

ACCEPTANCE_MAP_PATH = ROOT / "docs" / "acceptance_map_epic029.json"
TOKEN_MATRIX_PATH = QA_ROOT / "token_evidence_matrix.md"
VIABILITY_LOG_PATH = QA_ROOT / "acceptance_map_viability.log"
QA_STEP_MANIFEST_PATH = QA_ROOT / "qa_step_logs_manifest.json"

SURFACE_INVENTORY_PATH = QA_ROOT / "00_meta" / "conjunction_json_surface_inventory.md"
DEV_HARNESS_BINDING_COVERAGE_PATH = QA_ROOT / "00_meta" / "dev_harness_binding_coverage.md"

DOC_DELTAS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic029_doc_deltas.md"
DRAIN_TARGETS_PATH = ROOT / "audit" / "docdeltas" / "hde-epic029_drain_targets.md"

CLOSE_REPORT_PATH = ROOT / "audit" / "EPIC-029_close_report.md"
CLOSE_MANIFEST_PATH = ROOT / "audit" / "EPIC-029_MANIFEST.json"

OPS_REQUIRED = [
    "commands.txt",
    "stdout.log",
    "stderr.log",
    "exit_codes.txt",
    "codespaces_dev_sampler_url.md",
    "local_dev_sampler_url.md",
    "binding_disposition.md",
    "created_files_sha256.txt",
]

LIVE_QA_CHECKS = {
    "po-epic-close-live-qa": QA_ROOT / "checks" / "po-epic-close-live-qa" / "primary.log",
    "po-precommit": QA_ROOT / "checks" / "po-precommit" / "primary.log",
    "po-postcommit": QA_ROOT / "checks" / "po-postcommit" / "primary.log",
}

REQUALIFICATION_CHECK_IDS = (
    "po-epic-close-live-qa",
    "po-precommit",
    "po-postcommit",
)
LIVE_QA_TESTS = (
    "tests/adapter/test_dev_sampler_http.py",
    "tests/http/test_dev_conjunction_http.py",
    "tests/http/test_endpoint_catalog.py",
)
PRECOMMIT_SCRIPTS = (
    "ci/checks/check_env_pins.sh",
    "ci/checks/check_cli_help.sh",
    "ci/checks/check_final_lf.sh",
)
SANITY_PIPELINE_PATH = "tools/evidence/run_sanity_pipeline.py"
SANITY_LOG_REL = "audit/gates/sanity_pipeline/sanity_pipeline.log"
EVIDENCE_INDEX_CHECK = ("tools/evidence/update_evidence_index.py", "--check")
STAGED_INPUT_GENERATORS = (
    "tools/config/generate_config_artifacts.py",
    "tools/config/generate_bundles.py",
)
STAGED_INPUT_OUTPUTS = (
    "artifacts/registry/registry_report.json",
    "artifacts/config_bundles/be_bundle.json",
    "artifacts/config_bundles/fe_bundle.json",
)
CAPTURED_EXECUTION_ENV = (
    ("ALLOW_NETWORK", "0"),
    ("APP_ENV", "dev"),
    ("LANG", "C"),
    ("LC_ALL", "C"),
    ("SAFE_MODE", "1"),
    ("TZ", "UTC"),
)
SANITY_STAGE_NAMES = (
    "01 Environment pins",
    "02 Identity and release provenance",
    "03 Canonical JSON",
    "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks",
    "05 A7 Catalog transport",
    "06 CI rails",
    "07 Direct DB selection contract",
    "08 Direct DB posture artifacts",
    "09 BodyGraph policy",
    "10 Architecture snapshot",
    "11 Configured-v2 mapped-cache local evidence",
    "12 Historical bridge evidence integrity",
    "13 OPS-02 mapped-cache packet validation",
    "14 OPS-03 direct DB posture packet validation",
    "15 Human Index and Machine Mirror refresh",
    "16 Evidence-path validation",
    "17 Mirror schema and index/mirror hash validation",
    "18 Topology orientation validation",
    "19 Final-LF validation",
)
PYTEST_PASS_RE = re.compile(r"(?m)^\s*(?P<count>[0-9]+) passed(?:[, ]|$)")


@dataclass(frozen=True)
class RequalificationCheck:
    """One governed check and its fixed, ordered, non-shell commands."""

    check_id: str
    check_name: str
    commands: tuple[tuple[str, ...], ...]
    intended_tokens: tuple[str, ...]


@dataclass(frozen=True)
class CommandReceipt:
    """Unmodified result of one current execution."""

    argv: tuple[str, ...]
    returncode: int | None
    stdout: str
    stderr: str
    process_error: str = ""
    semantic_artifact: bytes | None = None


@dataclass(frozen=True)
class RequalificationRun:
    """Complete result family plus the receipts used to classify it."""

    results: tuple[qa_harness.CheckResult, ...]
    executions: tuple[tuple[str, tuple[CommandReceipt, ...]], ...]

    def result_for(self, check_id: str) -> qa_harness.CheckResult:
        return next(result for result in self.results if result.check_id == check_id)

    def receipts_for(self, check_id: str) -> tuple[CommandReceipt, ...]:
        return next(receipts for current_id, receipts in self.executions if current_id == check_id)


@dataclass(frozen=True)
class StagedCandidateFile:
    rel: str
    content: bytes
    mode: int


@dataclass(frozen=True)
class PublicationTargetPreimage:
    """Ordinary-filesystem state used to detect target-local publication races."""

    kind: str
    content: bytes | None
    mode: int | None


CommandRunner = Callable[[Sequence[str], Path, Mapping[str, str]], subprocess.CompletedProcess[str]]


def requalification_checks(python_executable: str | None = None) -> tuple[RequalificationCheck, ...]:
    """Return the only admitted EPIC029 current-state requalification family."""

    python = python_executable or sys.executable
    return (
        RequalificationCheck(
            check_id="po-epic-close-live-qa",
            check_name="EPIC029 current functional close bundle",
            commands=(
                (python, "-m", "pytest", "--version"),
                (
                    python,
                    "-m",
                    "pytest",
                    "--collect-only",
                    "-q",
                    "-p",
                    "no:cacheprovider",
                    *LIVE_QA_TESTS,
                ),
                (
                    python,
                    "-m",
                    "pytest",
                    "-q",
                    "-p",
                    "no:cacheprovider",
                    *LIVE_QA_TESTS,
                ),
            ),
            intended_tokens=("TESTS_PASS_OK",),
        ),
        RequalificationCheck(
            check_id="po-precommit",
            check_name="EPIC029 current precommit checklist",
            commands=tuple((script,) for script in PRECOMMIT_SCRIPTS),
            intended_tokens=("QA_PRECOMMIT_CHECKLIST_OK",),
        ),
        RequalificationCheck(
            check_id="po-postcommit",
            check_name="EPIC029 current postcommit release-sanity checklist",
            commands=((python, SANITY_PIPELINE_PATH),),
            intended_tokens=("QA_POSTCOMMIT_CHECKLIST_OK",),
        ),
    )


def _closed_execution_env(environ: Mapping[str, str] | None = None) -> dict[str, str]:
    source = os.environ if environ is None else environ
    runtime_bin = str(Path(sys.executable).parent)
    inherited_path = source.get("PATH", "")
    return {
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LANG": "C",
        "LC_ALL": "C",
        "PATH": runtime_bin + (os.pathsep + inherited_path if inherited_path else ""),
        "PYTHONDONTWRITEBYTECODE": "1",
        "SAFE_MODE": "1",
        "TZ": "UTC",
    }


def _default_command_runner(
    argv: Sequence[str], cwd: Path, env: Mapping[str, str]
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        tuple(argv),
        cwd=cwd,
        env=dict(env),
        capture_output=True,
        text=True,
        check=False,
        shell=False,
        timeout=1800,
    )


def _required_requalification_paths() -> tuple[str, ...]:
    return (*LIVE_QA_TESTS, *PRECOMMIT_SCRIPTS, SANITY_PIPELINE_PATH)


def _validate_requalification_root(root: Path) -> None:
    root = root.resolve()
    if not root.is_dir():
        raise ValueError("requalification root is unavailable")
    missing = [rel for rel in _required_requalification_paths() if not (root / rel).is_file()]
    if missing:
        raise ValueError(f"requalification entrypoints unavailable: {','.join(missing)}")


def _execute_command(
    argv: Sequence[str],
    *,
    root: Path,
    env: Mapping[str, str],
    runner: CommandRunner,
) -> CommandReceipt:
    command = tuple(argv)
    try:
        completed = runner(command, root, env)
    except (OSError, subprocess.SubprocessError) as exc:
        return CommandReceipt(command, None, "", "", f"{type(exc).__name__}: {exc}")
    artifact = None
    if command[-1:] == (SANITY_PIPELINE_PATH,):
        try:
            artifact = (root / SANITY_LOG_REL).read_bytes()
        except OSError:
            artifact = None
    return CommandReceipt(
        argv=command,
        returncode=completed.returncode,
        stdout=completed.stdout or "",
        stderr=completed.stderr or "",
        semantic_artifact=artifact,
    )


def _render_receipts(receipts: Sequence[CommandReceipt]) -> str:
    sections = [qa_harness.NONCLAIM_EXPLANATION]
    for index, receipt in enumerate(receipts, start=1):
        sections.append(
            json.dumps(
                {
                    "argv": list(receipt.argv),
                    "command_index": index,
                    "process_error": receipt.process_error,
                    "returncode": receipt.returncode,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        sections.extend(("[stdout]", receipt.stdout.rstrip("\n"), "[stderr]", receipt.stderr.rstrip("\n")))
        if receipt.semantic_artifact is not None:
            sections.extend(
                (
                    "[semantic_artifact]",
                    receipt.semantic_artifact.decode("utf-8", errors="replace").rstrip("\n"),
                    "[semantic_artifact_sha256] "
                    + hashlib.sha256(receipt.semantic_artifact).hexdigest(),
                )
            )
    return "\n".join(sections).rstrip("\n") + "\n"


def _first_process_failure(receipts: Sequence[CommandReceipt]) -> CommandReceipt | None:
    return next(
        (
            receipt
            for receipt in receipts
            if receipt.process_error or receipt.returncode is None or receipt.returncode != 0
        ),
        None,
    )


def _classify_live_qa(receipts: Sequence[CommandReceipt]) -> tuple[qa_harness.Status, str]:
    if not receipts:
        return qa_harness.Status.FAIL_TOOLING, "pytest readiness command was not executed"
    if receipts[0].process_error or receipts[0].returncode is None:
        return qa_harness.Status.FAIL_TOOLING, "pytest readiness process malfunction"
    if receipts[0].returncode != 0:
        return qa_harness.Status.TOOLING_BLOCKED, "pytest readiness check failed"
    readiness_output = receipts[0].stdout + receipts[0].stderr
    if "pytest" not in readiness_output.lower():
        return qa_harness.Status.FAIL_TOOLING, "pytest readiness receipt lacks version identity"
    if len(receipts) != 3:
        return qa_harness.Status.FAIL_TOOLING, "functional pytest command was not executed"
    collection_receipt = receipts[1]
    if collection_receipt.process_error or collection_receipt.returncode is None:
        return qa_harness.Status.FAIL_TOOLING, "functional pytest collection process malfunction"
    if collection_receipt.returncode != 0:
        return qa_harness.Status.FAIL_TOOLING, "functional pytest collection failed"
    collected_nodes = {
        line.strip()
        for line in collection_receipt.stdout.splitlines()
        if "::" in line
    }
    if not collected_nodes or any(
        not any(node.startswith(f"{test_path}::") for node in collected_nodes)
        for test_path in LIVE_QA_TESTS
    ):
        return (
            qa_harness.Status.FAIL_TOOLING,
            "functional pytest collection omits a required test module",
        )

    test_receipt = receipts[2]
    if test_receipt.process_error or test_receipt.returncode is None:
        return qa_harness.Status.FAIL_TOOLING, "functional pytest process malfunction"
    if test_receipt.returncode in {2, 3, 4, 5} or test_receipt.returncode < 0:
        return qa_harness.Status.FAIL_TOOLING, "functional pytest collection or tooling failed"
    if test_receipt.returncode != 0:
        return qa_harness.Status.FAIL_BEHAVIOR, "functional pytest assertions failed"
    output = test_receipt.stdout + test_receipt.stderr
    summary = PYTEST_PASS_RE.search(output)
    if summary is None:
        return qa_harness.Status.FAIL_TOOLING, "functional pytest PASS summary is missing"
    if int(summary.group("count")) != len(collected_nodes):
        return (
            qa_harness.Status.FAIL_TOOLING,
            "functional pytest PASS count disagrees with exact collection",
        )
    return qa_harness.Status.PASS, ""


def _classify_precommit(receipts: Sequence[CommandReceipt]) -> tuple[qa_harness.Status, str]:
    failure = _first_process_failure(receipts)
    if failure is not None:
        if failure.process_error or failure.returncode is None or (failure.returncode or 0) < 0:
            return qa_harness.Status.FAIL_TOOLING, "precommit checklist process malfunction"
        failure_index = receipts.index(failure)
        if failure_index == 0:
            return qa_harness.Status.TOOLING_BLOCKED, "environment-pins prerequisite failed"
        if failure_index == 1:
            return qa_harness.Status.FAIL_BEHAVIOR, "CLI help contract failed"
        return qa_harness.Status.FAIL_TOOLING, "final-LF evidence gate failed"
    if len(receipts) != len(PRECOMMIT_SCRIPTS):
        return qa_harness.Status.FAIL_TOOLING, "precommit checklist family is incomplete"
    if "[env-pins] OK:" not in receipts[0].stdout:
        return qa_harness.Status.FAIL_TOOLING, "environment-pins receipt lacks its success predicate"
    return qa_harness.Status.PASS, ""


def _sanity_log_semantics(payload: bytes | None) -> tuple[qa_harness.Status, str]:
    if payload is None:
        return qa_harness.Status.FAIL_TOOLING, "sanity pipeline did not produce its governed result"
    try:
        lines = payload.decode("utf-8").splitlines()
    except UnicodeDecodeError:
        return qa_harness.Status.FAIL_TOOLING, "sanity pipeline result is not UTF-8"
    required_prefix = (
        "run:sanity-pipeline",
        "pipeline_identity:HDE-EPIC038-PR06-release-sanity",
        "env:ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC",
        "env_pins:audit/gates/determinism/env_pins.log",
        "ops_evidence:retained_integrity_provenance_secret_safe_only;historical_nonclaim=true;not_rerun=true",
    )
    if tuple(lines[: len(required_prefix)]) != required_prefix:
        return qa_harness.Status.FAIL_TOOLING, "sanity pipeline result header is malformed"
    expected_pass_lines = list(required_prefix)
    for name in SANITY_STAGE_NAMES:
        expected_pass_lines.append(f"check {name}:OK")
        if name == "12 Historical bridge evidence integrity":
            expected_pass_lines.append("stage_result:12:HISTORICAL_INTEGRITY_OK")
    expected_pass_lines.extend(("first_failed_stage:NONE", "summary:PASS"))
    if lines == expected_pass_lines:
        return qa_harness.Status.PASS, ""
    if "summary:FAIL" in lines:
        return qa_harness.Status.FAIL_TOOLING, "release-sanity evidence pipeline failed"
    return qa_harness.Status.FAIL_TOOLING, "sanity pipeline result is internally inconsistent"


def _classify_postcommit(receipts: Sequence[CommandReceipt]) -> tuple[qa_harness.Status, str]:
    if len(receipts) != 1:
        return qa_harness.Status.FAIL_TOOLING, "release-sanity command was not executed exactly once"
    receipt = receipts[0]
    if receipt.process_error or receipt.returncode is None or receipt.returncode < 0:
        return qa_harness.Status.FAIL_TOOLING, "release-sanity process malfunction"
    semantic_status, reason = _sanity_log_semantics(receipt.semantic_artifact)
    if receipt.returncode == 0 and semantic_status is qa_harness.Status.PASS:
        return qa_harness.Status.PASS, ""
    return qa_harness.Status.FAIL_TOOLING, reason or "release-sanity exit/result disagreement"


def _classify_check(
    definition: RequalificationCheck, receipts: Sequence[CommandReceipt]
) -> qa_harness.CheckResult:
    classifiers = {
        "po-epic-close-live-qa": _classify_live_qa,
        "po-precommit": _classify_precommit,
        "po-postcommit": _classify_postcommit,
    }
    status, reason = classifiers[definition.check_id](receipts)
    executed = tuple(
        receipt
        for receipt in receipts
        if not receipt.process_error and receipt.returncode is not None
    )
    command: tuple[str, ...] | tuple[tuple[str, ...], ...]
    if len(executed) == 1:
        command = executed[0].argv
    elif executed:
        command = tuple(receipt.argv for receipt in executed)
    else:
        command = ()
    exit_code = executed[-1].returncode if executed else None
    evidence_path = f"audit/qa/{EPIC_SLUG}/checks/{definition.check_id}/primary.log"
    return qa_harness.CheckResult(
        check_id=definition.check_id,
        status=status,
        status_reason=reason,
        check_name=definition.check_name,
        command=command,
        command_provenance=(
            "EPIC029 exact executed non-shell argv receipts"
            if executed
            else "Not executed"
        ),
        exit_code=exit_code,
        output=_render_receipts(receipts),
        evidence_artifacts=(evidence_path,),
        intended_tokens=(
            () if status is qa_harness.Status.TOOLING_BLOCKED else definition.intended_tokens
        ),
        pf_refs=(
            "PF14-Canon-HDE-Mechanics-Guide",
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
        captured_env=CAPTURED_EXECUTION_ENV,
    )


def _run_requalification_checks(
    root: Path,
    definitions: Sequence[RequalificationCheck],
    *,
    runner: CommandRunner = _default_command_runner,
    environ: Mapping[str, str] | None = None,
) -> RequalificationRun:
    root = root.resolve()
    _validate_requalification_root(root)
    env = _closed_execution_env(environ)
    results: list[qa_harness.CheckResult] = []
    executions: list[tuple[str, tuple[CommandReceipt, ...]]] = []
    for definition in definitions:
        receipts: list[CommandReceipt] = []
        for command in definition.commands:
            receipt = _execute_command(command, root=root, env=env, runner=runner)
            receipts.append(receipt)
            if receipt.process_error or receipt.returncode != 0:
                break
        frozen_receipts = tuple(receipts)
        results.append(_classify_check(definition, frozen_receipts))
        executions.append((definition.check_id, frozen_receipts))
    return RequalificationRun(tuple(results), tuple(executions))


def run_requalification_family(
    root: Path,
    *,
    runner: CommandRunner = _default_command_runner,
    environ: Mapping[str, str] | None = None,
    python_executable: str | None = None,
) -> RequalificationRun:
    """Execute and classify every EPIC029 check without publishing evidence."""

    return _run_requalification_checks(
        root,
        requalification_checks(python_executable),
        runner=runner,
        environ=environ,
    )


def run_preseal_requalification(
    root: Path,
    *,
    runner: CommandRunner = _default_command_runner,
    environ: Mapping[str, str] | None = None,
    python_executable: str | None = None,
) -> RequalificationRun:
    """Run the two checks that do not depend on the evidence-graph preseal."""

    return _run_requalification_checks(
        root,
        requalification_checks(python_executable)[:2],
        runner=runner,
        environ=environ,
    )


def require_preseal_requalification(run: RequalificationRun) -> None:
    expected = REQUALIFICATION_CHECK_IDS[:2]
    ids = tuple(result.check_id for result in run.results)
    if ids != expected:
        raise RuntimeError("EPIC029 preseal requalification is incomplete or out of order")
    failures = [
        f"{result.check_id}={result.status.value}:{result.status_reason}"
        for result in run.results
        if result.status is not qa_harness.Status.PASS
    ]
    if failures:
        raise RuntimeError("EPIC029_PRESEAL_REQUALIFICATION_FAILED:" + ";".join(failures))


def run_postcommit_requalification(
    root: Path,
    preseal: RequalificationRun,
    *,
    runner: CommandRunner = _default_command_runner,
    environ: Mapping[str, str] | None = None,
    python_executable: str | None = None,
) -> RequalificationRun:
    """Run postcommit only after a truthful complete-path graph preseal."""

    require_preseal_requalification(preseal)
    post = _run_requalification_checks(
        root,
        requalification_checks(python_executable)[2:],
        runner=runner,
        environ=environ,
    )
    return RequalificationRun(
        (*preseal.results, *post.results),
        (*preseal.executions, *post.executions),
    )


def require_complete_requalification(run: RequalificationRun) -> None:
    ids = tuple(result.check_id for result in run.results)
    if ids != REQUALIFICATION_CHECK_IDS:
        raise RuntimeError("EPIC029 requalification family is incomplete or out of order")
    failures = [
        f"{result.check_id}={result.status.value}:{result.status_reason}"
        for result in run.results
        if result.status is not qa_harness.Status.PASS
    ]
    if failures:
        raise RuntimeError("EPIC029_REQUALIFICATION_FAILED:" + ";".join(failures))


def verify_postcommit_fixed_point(
    root: Path,
    first_run: RequalificationRun,
    *,
    runner: CommandRunner = _default_command_runner,
    environ: Mapping[str, str] | None = None,
    python_executable: str | None = None,
) -> None:
    """Require a second exact sanity run to reproduce the first receipt bytes."""

    definition = next(
        item
        for item in requalification_checks(python_executable)
        if item.check_id == "po-postcommit"
    )
    env = _closed_execution_env(environ)
    receipt = _execute_command(definition.commands[0], root=root.resolve(), env=env, runner=runner)
    second_result = _classify_check(definition, (receipt,))
    if second_result.status is not qa_harness.Status.PASS:
        raise RuntimeError(
            "EPIC029_POSTCOMMIT_SEAL_FAILED:"
            f"{second_result.status.value}:{second_result.status_reason}"
        )
    first_receipts = first_run.receipts_for("po-postcommit")
    if first_receipts != (receipt,):
        raise RuntimeError("EPIC029_POSTCOMMIT_NOT_FIXED_POINT")


def live_qa_status_from_requalification(run: RequalificationRun) -> dict[str, bool]:
    """Derive close-pack readiness only from freshly classified results."""

    return {
        check_id: run.result_for(check_id).status is qa_harness.Status.PASS
        for check_id in REQUALIFICATION_CHECK_IDS
    }


def _has_path_proof(path: Path) -> bool:
    return path.with_name(path.name + ".path_proof.txt").exists()


def _evidence_index_status() -> dict[str, bool]:
    index = ROOT / "docs" / "evidence" / "INDEX.json"
    mirror = ROOT / "artifacts" / "evidence_index.jsonl"
    index_sha = ROOT / "docs" / "evidence" / "INDEX.sha256"
    mirror_sha = ROOT / "artifacts" / "evidence_index.jsonl.sha256"

    index_present = index.exists() and _has_path_proof(index)
    mirror_present = mirror.exists() and _has_path_proof(mirror)
    hashes_present = (
        index_sha.exists()
        and mirror_sha.exists()
        and _has_path_proof(index_sha)
        and _has_path_proof(mirror_sha)
    )
    hashes_match = False
    if index_present and mirror_present and hashes_present:
        index_parts = index_sha.read_text(encoding="utf-8").strip().split()
        mirror_parts = mirror_sha.read_text(encoding="utf-8").strip().split()
        if index_parts and mirror_parts:
            index_expected = index_parts[0]
            mirror_expected = mirror_parts[0]
            hashes_match = (
                index_expected == _sha256(index) and mirror_expected == _sha256(mirror)
            )
    return {
        "evidence_index_updated": index_present,
        "machine_mirror_updated": mirror_present,
        "evidence_index_hash": hashes_present and hashes_match,
    }


def _utc_now() -> str:
    return _dt.datetime.now(tz=_dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path.relative_to(ROOT).as_posix()}")


def _write_json(path: Path, payload: object) -> None:
    _write_text(path, json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


def _missing_required_paths() -> list[str]:
    required = [SURFACE_INVENTORY_PATH, ROOT / "artifacts" / "writer" / "conjunction_write_readback.log", ROOT / "artifacts" / "writer" / "conjunction_writer_summary.json"]
    required += [OPS_ROOT / name for name in OPS_REQUIRED]
    return [path.relative_to(ROOT).as_posix() for path in required if not path.exists()]


def _ops_binding_disposition_status() -> dict[str, str]:
    disposition = OPS_ROOT / "binding_disposition.md"
    status = {"codespaces": "not yet closed", "local_dev": "not yet closed"}
    if not disposition.exists():
        return status

    for raw in disposition.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("codespaces:"):
            status["codespaces"] = line.split(":", 1)[1].strip().split(" - ", 1)[0]
        elif line.startswith("local_dev:"):
            status["local_dev"] = line.split(":", 1)[1].strip().split(" - ", 1)[0]
    return status


def _has_surface_inventory_closure_semantics(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8")
    required_fragments = (
        "## Conclusion (PR-01 bounded outcome)",
        "single shared canonical emitter (`emit_public` -> `sercanon`)",
        "No in-place emitter fix was needed for the inventoried loci.",
    )
    return all(fragment in text for fragment in required_fragments)


def _has_writer_closure_semantics(log_path: Path, summary_path: Path) -> bool:
    if not (log_path.exists() and summary_path.exists()):
        return False

    log_lines = {
        line.strip()
        for line in log_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }
    required_log_lines = {
        "schema=conjunction_write_readback.log.v1",
        "route=/dev/writer/conjunction",
        "reader_route=/dev/reader/conjunction",
        "writer_first_status=200",
        "writer_second_status=200",
        "reader_status=200",
        "writer_invalid_status=422",
        "writer_bytes_two_run_equal=true",
        "writer_payload_two_run_equal=true",
        "writer_result_reader_readback_equal=true",
        "writer_success_type=dev.writer.conjunction.success.v1",
        "writer_error_type=dev.writer.conjunction.error.v1",
    }
    if not required_log_lines.issubset(log_lines):
        return False

    try:
        summary = json.loads(summary_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False

    checks = summary.get("checks")
    if not isinstance(checks, dict):
        return False

    required_true_checks = (
        "writer_status_200",
        "reader_status_200",
        "writer_error_typed_envelope",
        "writer_success_typed_envelope",
        "writer_bytes_two_run_equal",
        "writer_payload_two_run_equal",
        "writer_result_reader_readback_equal",
    )
    return all(checks.get(check_name) is True for check_name in required_true_checks)


def _pf09_row_closure_gate(live_qa: dict[str, bool], index_status: dict[str, bool]) -> dict[str, object]:
    disposition_status = _ops_binding_disposition_status()
    codespaces_closed = disposition_status["codespaces"] == "closed"
    local_dev_closed = disposition_status["local_dev"] == "closed"
    required_inputs_ready = not _missing_required_paths()
    qa_complete = all(live_qa.values())
    evidence_index_complete = all(index_status.values())
    writer_log = ROOT / "artifacts" / "writer" / "conjunction_write_readback.log"
    writer_summary = ROOT / "artifacts" / "writer" / "conjunction_writer_summary.json"
    hde_conj009_1_closed = _has_surface_inventory_closure_semantics(SURFACE_INVENTORY_PATH)
    hde_conj008_1_closed = _has_writer_closure_semantics(writer_log, writer_summary)
    hde_conj001_4_closed = codespaces_closed and local_dev_closed
    ready_for_close_binding = all(
        [
            hde_conj009_1_closed,
            hde_conj008_1_closed,
            hde_conj001_4_closed,
            required_inputs_ready,
            qa_complete,
            evidence_index_complete,
        ]
    )
    return {
        "sequencing_classification": "supportable from repo evidence",
        "closure_mode": CLOSURE_MODE,
        "codespaces": disposition_status["codespaces"],
        "local_dev": disposition_status["local_dev"],
        "row_closure_status": {
            "HDE-CONJ009.1": "closed" if hde_conj009_1_closed else "not closed",
            "HDE-CONJ008.1": "closed" if hde_conj008_1_closed else "not closed",
            "HDE-CONJ001.4": "closed" if hde_conj001_4_closed else "not closed",
        },
        "mapped_rows": {
            "HDE-CONJ009.1": "Supportable from repo evidence: HDE-CONJ009.1 -> Done",
            "HDE-CONJ008.1": "Supportable from repo evidence: HDE-CONJ008.1 -> Done",
            "HDE-CONJ001.4": (
                "Supportable from repo evidence: HDE-CONJ001.4 -> Done after OPS-01 normalization"
                if hde_conj001_4_closed
                else "remains open while codespaces or local_dev is not yet closed"
            ),
        },
        "ready_for_close_binding": ready_for_close_binding,
    }


def _tokens(live_qa: dict[str, bool], index_status: dict[str, bool], gate: dict[str, object]) -> list[dict[str, object]]:
    gate_open = bool(gate["ready_for_close_binding"])
    return [
        {
            "name": "DOC_DELTA_PRESENT_OK",
            "owner_pf": "PF04 — HDE Governance §2.0.0",
            "status": "implemented" if gate_open else "token_incomplete",
            "evidence_titles": [
                "audit/docdeltas/hde-epic029_doc_deltas.md",
                "audit/docdeltas/hde-epic029_drain_targets.md",
            ],
        },
        {
            "name": "EVIDENCE_INDEX_UPDATED_OK",
            "owner_pf": "PF12 — Schemas & Artifacts §Evidence Index",
            "status": "implemented" if (gate_open and index_status["evidence_index_updated"]) else "token_incomplete",
            "evidence_titles": ["docs/evidence/INDEX.json"],
        },
        {
            "name": "MACHINE_MIRROR_UPDATED_OK",
            "owner_pf": "PF12 — Schemas & Artifacts §Evidence Mirror",
            "status": "implemented" if (gate_open and index_status["machine_mirror_updated"]) else "token_incomplete",
            "evidence_titles": ["artifacts/evidence_index.jsonl"],
        },
        {
            "name": "EVIDENCE_INDEX_HASH_OK",
            "owner_pf": "PF12 — Schemas & Artifacts §Evidence Hash Discipline",
            "status": "implemented" if (gate_open and index_status["evidence_index_hash"]) else "token_incomplete",
            "evidence_titles": [
                "docs/evidence/INDEX.sha256",
                "artifacts/evidence_index.jsonl.sha256",
            ],
        },
        {
            "name": "ENV_RAILS_POLICY_OK",
            "owner_pf": "PF10 — HDE Build Notes §Closed Rails",
            "status": "implemented" if gate_open else "token_incomplete",
            "evidence_titles": ["artifacts/proofs/env_pins.txt"],
        },
        {
            "name": "JSON_CANONICAL_CHECK_OK",
            "owner_pf": "PF10 — HDE Build Notes §Canonical JSON Gate",
            "status": "implemented" if gate_open else "token_incomplete",
            "evidence_titles": [
                "audit/gates/json_gate/canonical/json_gate_structured_record.json",
                "audit/gates/canonical_json/json_canonical_check.log",
            ],
        },
        {
            "name": "TESTS_PASS_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if (gate_open and live_qa["po-epic-close-live-qa"]) else "token_incomplete",
            "evidence_titles": [
                "audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log",
            ],
        },
        {
            "name": "QA_PRECOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if (gate_open and live_qa["po-precommit"]) else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-precommit/primary.log"],
        },
        {
            "name": "QA_POSTCOMMIT_CHECKLIST_OK",
            "owner_pf": "PF19 — Glow QA Guide §QA Rails",
            "status": "implemented" if (gate_open and live_qa["po-postcommit"]) else "token_incomplete",
            "evidence_titles": ["audit/qa/hde-epic029/checks/po-postcommit/primary.log"],
        },
    ]


def _write_acceptance_map(live_qa: dict[str, bool], index_status: dict[str, bool], gate: dict[str, object]) -> None:
    _write_json(ACCEPTANCE_MAP_PATH, {"epic_id": EPIC_ID, "sequencing_gate": gate, "tokens": _tokens(live_qa, index_status, gate)})


def _require_protected_acceptance_map(
    live_qa: dict[str, bool],
    index_status: dict[str, bool],
    gate: dict[str, object],
) -> None:
    """Verify the preserved map already binds the current closure facts exactly."""

    expected = {
        "epic_id": EPIC_ID,
        "sequencing_gate": gate,
        "tokens": _tokens(live_qa, index_status, gate),
    }
    try:
        actual = qa_harness._loads_json_strict(
            ACCEPTANCE_MAP_PATH.read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(f"EPIC029_PROTECTED_ACCEPTANCE_MAP_INVALID:{exc}") from exc
    if actual != expected:
        raise RuntimeError("EPIC029_PROTECTED_ACCEPTANCE_MAP_STALE_OR_MISMATCHED")


def _write_token_matrix(live_qa: dict[str, bool], index_status: dict[str, bool], gate: dict[str, object]) -> None:
    gate_open = bool(gate["ready_for_close_binding"])
    lines = [
        "# HDE-EPIC029 Token ↔ Evidence Matrix",
        "",
        "Sequencing posture: **supportable from repo evidence**.",
        "Close-pack acceptance binding is supportable for the controlled PF09 rows in this bounded EPIC029 closeout.",
        "",
        "| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |",
        "| --- | --- | --- | --- | --- | --- | --- |",
        f"| DOC_DELTA_PRESENT_OK | PF04 — HDE Governance §2.0.0 | audit/docdeltas/hde-epic029_doc_deltas.md; audit/docdeltas/hde-epic029_drain_targets.md | python tools/qa/generate_epic029_close_pack.py | acceptance_map_viability.log | {'Implemented' if gate_open else 'Planned'} | {'Doc-delta and drain-target ledgers are generated and bound for close-pack readiness.' if gate_open else 'Deferred pending required readiness inputs.'} |",
        f"| EVIDENCE_INDEX_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Index | docs/evidence/INDEX.json | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | {'Implemented' if (gate_open and index_status['evidence_index_updated']) else 'Planned'} | {'Bound only when INDEX.json and INDEX.json.path_proof.txt are present.' if (gate_open and index_status['evidence_index_updated']) else 'Deferred pending required readiness inputs.'} |",
        f"| MACHINE_MIRROR_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Mirror | artifacts/evidence_index.jsonl | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | {'Implemented' if (gate_open and index_status['machine_mirror_updated']) else 'Planned'} | {'Bound only when evidence_index.jsonl and evidence_index.jsonl.path_proof.txt are present.' if (gate_open and index_status['machine_mirror_updated']) else 'Deferred pending required readiness inputs.'} |",
        f"| EVIDENCE_INDEX_HASH_OK | PF12 — Schemas & Artifacts §Evidence Hash Discipline | docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256 | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | {'Implemented' if (gate_open and index_status['evidence_index_hash']) else 'Planned'} | {'Bound only when sha256 sidecars and path proofs exist and hashes match current bytes.' if (gate_open and index_status['evidence_index_hash']) else 'Deferred pending required readiness inputs.'} |",
        f"| ENV_RAILS_POLICY_OK | PF10 — HDE Build Notes §Closed Rails | artifacts/proofs/env_pins.txt | ci/checks/check_env_pins.sh | acceptance_map_viability.log | {'Implemented' if gate_open else 'Planned'} | {'Determinism env pins evidence remains present for closed-rails posture.' if gate_open else 'Deferred pending required readiness inputs.'} |",
        f"| JSON_CANONICAL_CHECK_OK | PF10 — HDE Build Notes §Canonical JSON Gate | audit/gates/json_gate/canonical/json_gate_structured_record.json; audit/gates/canonical_json/json_canonical_check.log | python tools/evidence/run_canonical_json_gate.py --check-only | acceptance_map_viability.log | {'Implemented' if gate_open else 'Planned'} | {'Canonical JSON gate evidence is bound without introducing new token names.' if gate_open else 'Deferred pending required readiness inputs.'} |",
        f"| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log | python -m pytest -q -p no:cacheprovider {' '.join(LIVE_QA_TESTS)} | acceptance_map_viability.log | {'Implemented' if (gate_open and live_qa['po-epic-close-live-qa']) else 'Planned'} | {'Bound to a fresh complete-family requalification result.' if (gate_open and live_qa['po-epic-close-live-qa']) else 'Deferred pending current requalification.'} |",
        f"| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-precommit/primary.log | {'; '.join(PRECOMMIT_SCRIPTS)} | acceptance_map_viability.log | {'Implemented' if (gate_open and live_qa['po-precommit']) else 'Planned'} | {'Bound to a fresh ordered non-shell requalification result.' if (gate_open and live_qa['po-precommit']) else 'Deferred pending current requalification.'} |",
        f"| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-postcommit/primary.log | python {SANITY_PIPELINE_PATH} | acceptance_map_viability.log | {'Implemented' if (gate_open and live_qa['po-postcommit']) else 'Planned'} | {'Bound to a fresh release-sanity result and verified fixed point.' if (gate_open and live_qa['po-postcommit']) else 'Deferred pending current requalification.'} |",
        "",
        "## PF09 scope bindings (status-only; not acceptance tokens)",
        "",
        f"- Supportable from repo evidence: `{PF09_SCOPE[0]['subtask_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[0]['task_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[1]['subtask_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[1]['task_id']}` -> Done.",
        f"- Supportable from repo evidence: `{PF09_SCOPE[2]['subtask_id']}` -> Done after OPS-01 normalization.",
        "- `HDE-CONJ001` remains task-level done in PF09; this report only states subtask supportability from repo evidence.",
    ]
    _write_text(TOKEN_MATRIX_PATH, "\n".join(lines) + "\n")


def _write_dev_harness_binding_coverage(live_qa: dict[str, bool], gate: dict[str, object]) -> None:
    live_block = []
    for check_id, path in LIVE_QA_CHECKS.items():
        rel = path.relative_to(ROOT).as_posix()
        if live_qa[check_id]:
            live_block.append(f"- `{rel}`: present and bound.")
        else:
            live_block.append(f"- `{rel}`: missing (deferred; no synthetic PASS claim).")

    hde_conj001_4_closed = gate["row_closure_status"]["HDE-CONJ001.4"] == "closed"
    local_line = (
        "- Local dev is **closed** by explicit binding-equivalence to the canonical Codespaces loopback DEV_SAMPLER_URL for EPIC029 (not an independent second runtime proof)."
        if hde_conj001_4_closed
        else "- Local dev remains **not yet closed**; PF07 publishes `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`, but OPS disposition has not closed this environment."
    )
    hde_conj001_4_line = (
        "- Therefore `HDE-CONJ001.4` is closed under the approved equivalence rule for this epic slice."
        if hde_conj001_4_closed
        else "- Therefore `HDE-CONJ001.4` remains not done in this close-pack."
    )

    content = f"""# HDE-EPIC029 Dev Harness Binding Coverage

## OPS-01 single-source disposition
- Source of truth: `audit/ops/hde-epic029/ops-01/binding_disposition.md`.
- Codespaces is **{gate['codespaces']}** based on OPS-01 evidence under closed rails.
- Closure mode: {gate['closure_mode']}
{local_line}
{hde_conj001_4_line}

## OPS-01 files bound by this PR
- `audit/ops/hde-epic029/ops-01/commands.txt`
- `audit/ops/hde-epic029/ops-01/stdout.log`
- `audit/ops/hde-epic029/ops-01/stderr.log`
- `audit/ops/hde-epic029/ops-01/exit_codes.txt`
- `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/binding_disposition.md`
- `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

## Epic-close Live QA outputs disposition
{chr(10).join(live_block)}
"""
    _write_text(DEV_HARNESS_BINDING_COVERAGE_PATH, content)


def _write_docdeltas() -> None:
    _write_text(
        DOC_DELTAS_PATH,
        "# HDE-EPIC029 doc deltas\n\n- Empty ledger: this PR binds governed acceptance/closeout artifacts only; no canon/doc prose deltas were introduced.\n",
    )
    _write_text(
        DRAIN_TARGETS_PATH,
        "# HDE-EPIC029 drain targets\n\n- Empty ledger: no additional drain-target document actions are required in this offline acceptance binding slice.\n",
    )


def _write_viability_log() -> None:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=("acceptance_map_viability",),
    )
    result = qa_harness.generate_acceptance_map_viability(config, publish_governed_ledger=True)
    ledger = qa_harness.require_governed_viability(result, VIABILITY_LOG_PATH)
    print(f"WROTE {ledger.relative_to(ROOT).as_posix()}")


def _write_close_report(produced_at: str, live_qa: dict[str, bool], gate: dict[str, object]) -> None:
    qa_lines = []
    for check_id, exists in live_qa.items():
        rel = LIVE_QA_CHECKS[check_id].relative_to(ROOT).as_posix()
        qa_lines.append(
            f"- `{rel}`: "
            f"{'freshly requalified PASS' if exists else 'current requalification did not PASS'}"
        )

    hde_conj001_4_closed = gate["row_closure_status"]["HDE-CONJ001.4"] == "closed"
    hde_conj001_4_line = (
        "- `HDE-CONJ001` / `HDE-CONJ001.4`: closed by explicit binding-equivalence normalization across OPS-01 governed evidence."
        if hde_conj001_4_closed
        else "- `HDE-CONJ001` / `HDE-CONJ001.4`: represented via OPS disposition; remains not done while codespaces/local_dev are not yet closed."
    )
    ops_truth_line = (
        "- `HDE-CONJ001.4` is marked complete using approved equivalence closure with no claim of a second independently exercised runtime."
        if hde_conj001_4_closed
        else "- `HDE-CONJ001.4` is therefore not marked complete in this PR."
    )

    content = f"""# HDE-EPIC029 — Close Report

## Overview
This EPIC029 closeout refresh is bounded to repo-side governed evidence and report-only status recommendations for the controlling conjunction rows.

## Capture timestamp
- `{produced_at}`

## PF09 mapping used
- Task: `{PF09_TASK_ID}`
- Subtask: `{PF09_SUBTASK_ID}`
- Additional bound subtasks: `HDE-CONJ008.1`, `HDE-CONJ001.4`.

## PF09 scope truth (bound in metadata, not minted as acceptance tokens)
- `HDE-CONJ001` / `HDE-CONJ001.4`: status supportability is bound via normalized OPS-01 disposition evidence.
- `HDE-CONJ008` / `HDE-CONJ008.1`: status supportability is bound via existing writer conjunction evidence.
- `HDE-CONJ009` / `HDE-CONJ009.1`: status supportability is bound via existing conjunction surface inventory evidence.

## OPS-01 truth preserved
- Codespaces is **{gate['codespaces']}** under OPS-01 governed evidence.
- Local dev is **{gate['local_dev']}** under OPS-01 governed evidence.
- Closure mode: {gate['closure_mode']}
{ops_truth_line}

## PF09 status recommendations (report only; no PF edits)
- Current PF09 text is not edited here.
- Statuses below are supportable from repo evidence only.
- Any PF09 status change happens later, outside this Codex work.
- Supportable from repo evidence: HDE-CONJ009.1 -> Done
- Supportable from repo evidence: HDE-CONJ009 -> Done
- Supportable from repo evidence: HDE-CONJ008.1 -> Done
- Supportable from repo evidence: HDE-CONJ008 -> Done
- Supportable from repo evidence: HDE-CONJ001.4 -> Done, contingent on the normalized OPS-01 binding-equivalence family now present in repo

## Epic-close Live QA outputs
{chr(10).join(qa_lines)}

## Canonical EPIC029 close-pack artifacts
- `docs/acceptance_map_epic029.json`
- `audit/qa/hde-epic029/token_evidence_matrix.md`
- `audit/qa/hde-epic029/acceptance_map_viability.log`
- `audit/qa/hde-epic029/qa_step_logs_manifest.json`
- `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`
- `audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md`
- `audit/docdeltas/hde-epic029_doc_deltas.md`
- `audit/docdeltas/hde-epic029_drain_targets.md`
- `audit/EPIC-029_close_report.md`
- `audit/EPIC-029_MANIFEST.json`
"""
    _write_text(CLOSE_REPORT_PATH, content)


def _write_close_manifest(produced_at: str, live_qa: dict[str, bool], gate: dict[str, object]) -> None:
    key_outputs = {
        "acceptance_map": "docs/acceptance_map_epic029.json",
        "token_matrix": "audit/qa/hde-epic029/token_evidence_matrix.md",
        "acceptance_map_viability": "audit/qa/hde-epic029/acceptance_map_viability.log",
        "qa_step_manifest": "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        "conjunction_json_surface_inventory": "audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md",
        "dev_harness_binding_coverage": "audit/qa/hde-epic029/00_meta/dev_harness_binding_coverage.md",
        "doc_deltas": "audit/docdeltas/hde-epic029_doc_deltas.md",
        "drain_targets": "audit/docdeltas/hde-epic029_drain_targets.md",
        "close_report": "audit/EPIC-029_close_report.md",
        "close_manifest": "audit/EPIC-029_MANIFEST.json",
        "ops_commands": "audit/ops/hde-epic029/ops-01/commands.txt",
        "ops_stdout": "audit/ops/hde-epic029/ops-01/stdout.log",
        "ops_stderr": "audit/ops/hde-epic029/ops-01/stderr.log",
        "ops_exit_codes": "audit/ops/hde-epic029/ops-01/exit_codes.txt",
        "ops_codespaces_dev_sampler_url": "audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md",
        "ops_local_dev_sampler_url": "audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md",
        "ops_binding_disposition": "audit/ops/hde-epic029/ops-01/binding_disposition.md",
        "ops_created_files_sha256": "audit/ops/hde-epic029/ops-01/created_files_sha256.txt",
    }
    payload = {
        "captured_at_utc": produced_at,
        "closeout_dir": "audit/qa/hde-epic029",
        "epic_id": EPIC_ID,
        "key_outputs": key_outputs,
        "ops_task_id": "OPS-01",
        "pf09_task_id": PF09_TASK_ID,
        "pf09_subtask_id": PF09_SUBTASK_ID,
        "pf09_scope": PF09_SCOPE,
        "qa_epic_root": "audit/qa/hde-epic029",
        "qa_step_count": len(live_qa),
        "qa_step_manifest_path": "audit/qa/hde-epic029/qa_step_logs_manifest.json",
        "qa_summary_lines": [
            f"po-epic-close-live-qa={'requalified' if live_qa['po-epic-close-live-qa'] else 'not_pass'}",
            f"po-precommit={'requalified' if live_qa['po-precommit'] else 'not_pass'}",
            f"po-postcommit={'requalified' if live_qa['po-postcommit'] else 'not_pass'}",
            f"codespaces={gate['codespaces']}",
            f"local_dev={gate['local_dev']}",
            f"closure_mode={gate['closure_mode']}",
            "hde_conj009_1=supportable_from_repo_evidence_done_report_only",
            "hde_conj009=supportable_from_repo_evidence_done_report_only",
            "hde_conj008_1=supportable_from_repo_evidence_done_report_only",
            "hde_conj008=supportable_from_repo_evidence_done_report_only",
            f"hde_conj001_4={gate['row_closure_status']['HDE-CONJ001.4']}",
            "hde_conj001_4_recommendation=supportable_from_repo_evidence_done_after_ops01_normalization",
            "pf09_report_only_recommendations=yes_no_pf_edits",
        ],
        "run_id": RUN_ID,
        "scope": "repo_side_governed_evidence_closeout_report_only_pf09_recommendations",
    }
    _write_json(CLOSE_MANIFEST_PATH, payload)


def _verify_manifest_paths(root: Path = ROOT) -> None:
    payload = json.loads(
        (root / "audit/EPIC-029_MANIFEST.json").read_text(encoding="utf-8")
    )
    missing: list[str] = []
    for rel in sorted(set(payload["key_outputs"].values())):
        if not (root / rel).exists():
            missing.append(rel)
    if missing:
        raise SystemExit(f"DANGLING_MANIFEST_PATHS:{','.join(missing)}")


def _run_required_command(argv: Sequence[str], root: Path) -> CommandReceipt:
    receipt = _execute_command(
        argv,
        root=root.resolve(),
        env=_closed_execution_env(),
        runner=_default_command_runner,
    )
    if receipt.process_error or receipt.returncode != 0:
        detail = receipt.process_error or receipt.stderr.strip() or receipt.stdout.strip()
        raise RuntimeError(f"REQUIRED_COMMAND_FAILED:{list(argv)!r}:{detail}")
    return receipt


def _refresh_staged_generated_inputs(root: Path) -> None:
    """Refresh current generated inputs before sealing the evidence graph."""

    for script in STAGED_INPUT_GENERATORS:
        _run_required_command((sys.executable, script), root)


def _publish_initial_requalification(
    run: RequalificationRun, produced_at: str
) -> qa_harness.HarnessConfig:
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=("acceptance_map_viability",),
    )
    qa_harness.record_check_family(
        config,
        run.results,
        replace_legacy_family_ids=REQUALIFICATION_CHECK_IDS,
        captured_at_utc=produced_at,
    )
    return config


def _provisional_result(check_id: str, reason: str) -> qa_harness.CheckResult:
    if check_id not in {"po-postcommit", "acceptance-map-viability"}:
        raise ValueError("unsupported provisional EPIC029 check")
    return qa_harness.CheckResult(
        check_id=check_id,
        status=qa_harness.Status.TOOLING_BLOCKED,
        status_reason=reason,
        check_name=(
            "EPIC029 postcommit graph preseal"
            if check_id == "po-postcommit"
            else "Acceptance-map viability graph preseal"
        ),
        command=(),
        command_provenance="Not executed",
        exit_code=None,
        output=qa_harness.NONCLAIM_EXPLANATION + "\n",
        evidence_artifacts=(
            f"audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log",
        ),
        intended_tokens=(),
        pf_refs=(
            "PF19-Canon-Glow-QA-Guide",
            "PF27-Canon-Plan-Templates",
        ),
    )


def _publish_truthful_preseal(
    preseal: RequalificationRun,
    produced_at: str,
) -> qa_harness.HarnessConfig:
    """Create every registered path without synthesizing a PASS result."""

    require_preseal_requalification(preseal)
    post_reason = "postcommit awaits an updater-bound evidence-graph preseal"
    viability_reason = "acceptance-map viability awaits current postcommit requalification"
    post = _provisional_result("po-postcommit", post_reason)
    viability = _provisional_result("acceptance-map-viability", viability_reason)
    ledger_content = json.dumps(
        {
            "epic_id": EPIC_ID,
            "status": qa_harness.Status.TOOLING_BLOCKED.value,
            "status_reason": viability_reason,
            "token_status": {},
        },
        sort_keys=True,
        separators=(",", ":"),
    ) + "\n"
    config = qa_harness.HarnessConfig(
        epic_id=EPIC_ID,
        repo_root=ROOT,
        step_names=("acceptance_map_viability",),
    )
    family = (*preseal.results, post, viability)
    shape, checks = qa_harness._manifest_shape(
        config, qa_harness._manifest_payload(config)
    )
    if shape == "wrapped-checks" and set(checks) == set(REQUALIFICATION_CHECK_IDS):
        qa_harness.record_check_family(
            config,
            family,
            additional_files=((VIABILITY_LOG_PATH, ledger_content),),
            replace_legacy_family_ids=REQUALIFICATION_CHECK_IDS,
            admit_new_check_ids=("acceptance-map-viability",),
            captured_at_utc=produced_at,
        )
    elif shape == "flat-checks" and set(checks) == {
        *REQUALIFICATION_CHECK_IDS,
        "acceptance-map-viability",
    }:
        qa_harness.record_check_family(
            config,
            family,
            additional_files=((VIABILITY_LOG_PATH, ledger_content),),
            captured_at_utc=produced_at,
        )
    else:
        raise ValueError("EPIC029 manifest is not an admitted requalification shape")
    return config


def _publish_complete_requalification_after_preseal(
    config: qa_harness.HarnessConfig,
    run: RequalificationRun,
    produced_at: str,
) -> None:
    require_complete_requalification(run)
    # The existing provisional viability entry remains explicitly non-PASS
    # until pure current-state evaluation succeeds below.
    qa_harness.record_check_family(
        config,
        run.results,
        captured_at_utc=produced_at,
    )


def _publish_viability_with_requalification(
    config: qa_harness.HarnessConfig,
    run: RequalificationRun,
    produced_at: str,
) -> None:
    viability, ledger_content = qa_harness.evaluate_acceptance_map_viability(
        config,
        planned_governed_ledger=True,
    )
    if viability.status is not qa_harness.Status.PASS:
        raise RuntimeError(
            "ACCEPTANCE_MAP_VIABILITY_"
            f"{viability.status.value}:{viability.status_reason}"
        )
    qa_harness.record_check_family(
        config,
        (*run.results, viability),
        additional_files=((VIABILITY_LOG_PATH, ledger_content),),
        captured_at_utc=produced_at,
    )
    for check_id in (*REQUALIFICATION_CHECK_IDS, viability.check_id):
        qa_harness.verify_manifest_entry(config, check_id)
    payload = json.loads(VIABILITY_LOG_PATH.read_text(encoding="utf-8"))
    if payload.get("epic_id") != EPIC_ID or payload.get("status") != "PASS":
        raise RuntimeError("acceptance-map viability ledger verification failed")
    _verify_viability_pair(ROOT)


def _verify_viability_pair(root: Path) -> None:
    ledger = root / f"audit/qa/{EPIC_SLUG}/acceptance_map_viability.log"
    primary = (
        root
        / f"audit/qa/{EPIC_SLUG}/checks/acceptance-map-viability/primary.log"
    )
    try:
        ledger_bytes = ledger.read_bytes()
        primary_bytes = primary.read_bytes()
    except OSError as exc:
        raise RuntimeError("acceptance-map viability pair is unavailable") from exc
    if not ledger_bytes or b"\n" not in primary_bytes:
        raise RuntimeError("acceptance-map viability pair is malformed")
    _, primary_body = primary_bytes.split(b"\n", 1)
    if primary_body != ledger_bytes:
        raise RuntimeError("acceptance-map viability primary and ledger disagree")


def _materialize_staged_close_pack() -> int:
    """Build and seal a candidate only inside a disposable Git worktree."""

    if not (ROOT / ".git").exists():
        raise RuntimeError("EPIC029 requalification requires a real Git worktree")
    missing = _missing_required_paths()
    if missing:
        raise RuntimeError(f"MISSING_REQUIRED_INPUTS:{','.join(missing)}")

    produced_at = _utc_now()
    # Release sanity checks these canonical generated inputs before its
    # evidence-index stage. Refresh them first so the preseal indexes the
    # exact bytes that the postcommit predicate later validates.
    _refresh_staged_generated_inputs(ROOT)
    preseal = run_preseal_requalification(ROOT)
    config = _publish_truthful_preseal(preseal, produced_at)
    # The updater registry requires all four current receipt paths.  The
    # truthful preseal above supplies them without claiming postcommit or
    # viability PASS, allowing the first sanity run to inspect a coherent
    # disposable graph.
    _run_required_command((sys.executable, "tools/evidence/update_evidence_index.py"), ROOT)
    run = run_postcommit_requalification(ROOT, preseal)
    require_complete_requalification(run)
    live_qa = live_qa_status_from_requalification(run)
    index_status = _evidence_index_status()
    if not all(index_status.values()):
        raise RuntimeError("EPIC029_EVIDENCE_GRAPH_PRECONDITION_FAILED")

    _publish_complete_requalification_after_preseal(config, run, produced_at)
    gate = _pf09_row_closure_gate(live_qa, index_status)
    if not gate["ready_for_close_binding"]:
        raise RuntimeError("EPIC029_CLOSE_BINDING_GATE_CLOSED")
    _require_protected_acceptance_map(live_qa, index_status, gate)
    _write_token_matrix(live_qa, index_status, gate)
    _run_required_command((sys.executable, "tools/evidence/update_evidence_index.py"), ROOT)
    _publish_viability_with_requalification(config, run, produced_at)

    # Bind the newly generated family before the second release-sanity seal.
    _run_required_command((sys.executable, "tools/evidence/update_evidence_index.py"), ROOT)
    verify_postcommit_fixed_point(ROOT, run)
    _run_required_command((sys.executable, *EVIDENCE_INDEX_CHECK), ROOT)
    _verify_manifest_paths()
    return 0


def _git_command(root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    try:
        return subprocess.run(
            ("git", "-C", str(root), *args),
            capture_output=True,
            text=True,
            check=False,
            shell=False,
            timeout=120,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise RuntimeError(f"Git worktree operation failed: {exc}") from exc


def _require_git_head(root: Path) -> str:
    probe = _git_command(root, "rev-parse", "--is-inside-work-tree")
    if probe.returncode != 0 or probe.stdout.strip() != "true":
        raise RuntimeError("EPIC029 orchestration requires a real Git worktree")
    head = _git_command(root, "rev-parse", "--verify", "HEAD^{commit}")
    revision = head.stdout.strip()
    if head.returncode != 0 or re.fullmatch(r"[0-9a-fA-F]{40,64}", revision) is None:
        raise RuntimeError("EPIC029 orchestration requires an available Git HEAD")
    return revision


@contextlib.contextmanager
def _staging_worktree(root: Path, revision: str) -> Iterator[Path]:
    with tempfile.TemporaryDirectory(prefix="epic029-requalification-") as temp_dir:
        stage = Path(temp_dir) / "worktree"
        added = _git_command(
            root,
            "worktree",
            "add",
            "--detach",
            str(stage),
            revision,
        )
        if added.returncode != 0:
            raise RuntimeError(f"Unable to create staging worktree: {added.stderr.strip()}")
        body_error: BaseException | None = None
        try:
            yield stage
        except BaseException as exc:
            body_error = exc
            raise
        finally:
            removed = _git_command(root, "worktree", "remove", "--force", str(stage))
            if removed.returncode != 0 and body_error is None:
                raise RuntimeError(
                    f"Unable to remove staging worktree: {removed.stderr.strip()}"
                )


def _publication_allowlist() -> set[str]:
    qa_paths = {
        f"audit/qa/{EPIC_SLUG}/token_evidence_matrix.md",
        f"audit/qa/{EPIC_SLUG}/acceptance_map_viability.log",
        f"audit/qa/{EPIC_SLUG}/qa_step_logs_manifest.json",
        *{
            f"audit/qa/{EPIC_SLUG}/checks/{check_id}/primary.log"
            for check_id in (*REQUALIFICATION_CHECK_IDS, "acceptance-map-viability")
        },
    }
    graph_paths = {
        "docs/evidence/INDEX.json",
        "docs/evidence/INDEX.sha256",
        "artifacts/evidence_index.jsonl",
        "artifacts/evidence_index.jsonl.sha256",
        "audit/gates/topology/orientation_demo.txt",
    }
    staged_input_paths = set(STAGED_INPUT_OUTPUTS)
    preserved_primary_proofs = {
        "docs/acceptance_map_epic029.json.path_proof.txt",
        "audit/EPIC-029_close_report.md.path_proof.txt",
        "audit/EPIC-029_MANIFEST.json.path_proof.txt",
    }
    primary_paths = qa_paths | graph_paths | staged_input_paths
    return (
        primary_paths
        | {f"{path}.path_proof.txt" for path in primary_paths}
        | preserved_primary_proofs
    )


def _is_protected_stage_path(rel: str) -> bool:
    admitted_proof_refreshes = {
        "docs/acceptance_map_epic029.json.path_proof.txt",
        "audit/EPIC-029_close_report.md.path_proof.txt",
        "audit/EPIC-029_MANIFEST.json.path_proof.txt",
    }
    if rel in admitted_proof_refreshes:
        return False
    primary_rel = rel.removesuffix(".path_proof.txt")
    exact = {
        "docs/acceptance_map_epic029.json",
        "audit/EPIC-029_close_report.md",
        "audit/EPIC-029_MANIFEST.json",
        f"audit/qa/{EPIC_SLUG}/00_meta/dev_harness_binding_coverage.md",
        SANITY_LOG_REL,
    }
    return (
        primary_rel in exact
        or primary_rel.startswith("docs/pfcanon/")
        or primary_rel.startswith("audit/docdeltas/")
        or primary_rel.startswith(f"audit/ops/{EPIC_SLUG}/")
        or re.match(rf"audit/qa/{EPIC_SLUG}/checks/po-00[1-8]/", primary_rel)
        is not None
    )


def _candidate_paths(stage: Path) -> tuple[str, ...]:
    status = _git_command(stage, "status", "--porcelain=v1", "-z", "--untracked-files=all")
    if status.returncode != 0:
        raise RuntimeError(f"Unable to inspect staged outputs: {status.stderr.strip()}")
    candidates: list[str] = []
    for record in status.stdout.split("\0"):
        if not record:
            continue
        if len(record) < 4 or record[2] != " ":
            raise RuntimeError("Malformed staged Git status record")
        state = record[:2]
        rel = record[3:]
        if any(marker in state for marker in "DRCT"):
            raise RuntimeError(f"Staged generation attempted a non-file replacement: {rel}")
        candidate = Path(rel)
        if candidate.is_absolute() or ".." in candidate.parts:
            raise RuntimeError(f"Unsafe staged output path: {rel}")
        candidates.append(candidate.as_posix())
    protected = sorted(rel for rel in set(candidates) if _is_protected_stage_path(rel))
    if protected:
        raise RuntimeError(f"PROTECTED_STAGE_MUTATION:{','.join(protected)}")
    unexpected = sorted(set(candidates) - _publication_allowlist())
    if unexpected:
        raise RuntimeError(f"UNEXPECTED_STAGED_OUTPUTS:{','.join(unexpected)}")
    return tuple(sorted(set(candidates)))


def _write_bytes_atomically(path: Path, data: bytes, mode: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temp_path = Path(temp_name)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.chmod(temp_path, mode)
        os.replace(temp_path, path)
    finally:
        temp_path.unlink(missing_ok=True)


def _publication_target_preimage(root: Path, rel: str) -> PublicationTargetPreimage:
    target = root / rel
    try:
        metadata = target.lstat()
    except FileNotFoundError:
        return PublicationTargetPreimage("missing", None, None)
    mode = metadata.st_mode & 0o777
    if stat.S_ISREG(metadata.st_mode):
        return PublicationTargetPreimage("file", target.read_bytes(), mode)
    if stat.S_ISLNK(metadata.st_mode):
        return PublicationTargetPreimage(
            "symlink",
            os.fsencode(os.readlink(target)),
            mode,
        )
    return PublicationTargetPreimage("other", None, mode)


def _capture_publication_preimages(
    root: Path,
) -> dict[str, PublicationTargetPreimage]:
    return {
        rel: _publication_target_preimage(root, rel)
        for rel in sorted(_publication_allowlist())
    }


def _capture_staged_candidate(
    stage: Path, paths: Sequence[str]
) -> tuple[StagedCandidateFile, ...]:
    captured: list[StagedCandidateFile] = []
    for rel in paths:
        source = stage / rel
        if not source.is_file() or source.is_symlink():
            raise RuntimeError(f"Staged output is not a regular file: {rel}")
        content = source.read_bytes()
        if not content:
            raise RuntimeError(f"Staged output is empty: {rel}")
        captured.append(
            StagedCandidateFile(
                rel=rel,
                content=content,
                mode=source.stat().st_mode & 0o777,
            )
        )
    return tuple(captured)


def _publish_captured_candidate(
    candidate: Sequence[StagedCandidateFile],
    root: Path,
    *,
    expected_preimages: Mapping[str, PublicationTargetPreimage] | None = None,
) -> None:
    originals: dict[str, tuple[bytes, int] | None] = {}
    preflight: dict[str, PublicationTargetPreimage] = {}
    published: list[str] = []
    for staged_file in candidate:
        rel = staged_file.rel
        target = root / rel
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise RuntimeError(f"Publication target is not a regular file: {rel}")
        ancestor = target.parent
        while ancestor != root:
            if ancestor.is_symlink():
                raise RuntimeError(f"Publication target has an aliased parent: {rel}")
            if ancestor == ancestor.parent:
                raise RuntimeError(f"Publication target escapes source root: {rel}")
            ancestor = ancestor.parent
        current = _publication_target_preimage(root, rel)
        if expected_preimages is not None:
            expected = expected_preimages.get(rel)
            if expected is None or current != expected:
                raise RuntimeError(f"PUBLICATION_TARGET_CHANGED:{rel}")
        if current.kind not in {"file", "missing"}:
            raise RuntimeError(f"Publication target is not a regular file: {rel}")
        preflight[rel] = current
        originals[rel] = (
            (current.content or b"", current.mode or 0)
            if current.kind == "file"
            else None
        )
    try:
        for staged_file in candidate:
            rel = staged_file.rel
            if _publication_target_preimage(root, rel) != preflight[rel]:
                raise RuntimeError(f"PUBLICATION_TARGET_CHANGED:{rel}")
            _write_bytes_atomically(
                root / rel,
                staged_file.content,
                staged_file.mode,
            )
            published.append(rel)
        for staged_file in candidate:
            if (root / staged_file.rel).read_bytes() != staged_file.content:
                rel = staged_file.rel
                raise RuntimeError(f"Post-publication byte verification failed: {rel}")
        config = qa_harness.HarnessConfig(EPIC_ID, repo_root=root)
        for check_id in (*REQUALIFICATION_CHECK_IDS, "acceptance-map-viability"):
            qa_harness.verify_manifest_entry(config, check_id)
        _verify_viability_pair(root)
        _verify_manifest_paths(root)
        _run_required_command((sys.executable, *EVIDENCE_INDEX_CHECK), root)
    except BaseException:
        for rel in reversed(published):
            target = root / rel
            original = originals[rel]
            if original is None:
                target.unlink(missing_ok=True)
            else:
                _write_bytes_atomically(target, original[0], original[1])
        raise


def _publish_staged_candidate(stage: Path, root: Path, paths: Sequence[str]) -> None:
    """Compatibility wrapper for already isolated unit-test candidates."""

    _publish_captured_candidate(_capture_staged_candidate(stage, paths), root)


def _orchestrate_from_head() -> int:
    revision = _require_git_head(ROOT)
    publication_preimages = _capture_publication_preimages(ROOT)
    try:
        sanity_preimage = (ROOT / SANITY_LOG_REL).read_bytes()
    except OSError as exc:
        raise RuntimeError("Canonical sanity-log preimage is unavailable") from exc
    if not sanity_preimage:
        raise RuntimeError("Canonical sanity-log preimage is empty")
    candidate: tuple[StagedCandidateFile, ...]
    staged_stdout = ""
    with _staging_worktree(ROOT, revision) as stage:
        command = (
            sys.executable,
            "tools/qa/generate_epic029_close_pack.py",
            "--staged-materialization",
        )
        completed = subprocess.run(
            command,
            cwd=stage,
            env=_closed_execution_env(),
            capture_output=True,
            text=True,
            check=False,
            shell=False,
        )
        if completed.returncode != 0:
            if completed.stdout:
                print(completed.stdout, end="")
            if completed.stderr:
                print(completed.stderr, end="", file=sys.stderr)
            raise RuntimeError(
                f"EPIC029 staged requalification failed with exit code {completed.returncode}"
            )
        try:
            staged_sanity = (stage / SANITY_LOG_REL).read_bytes()
        except OSError as exc:
            raise RuntimeError("Staged sanity-log result is unavailable") from exc
        if staged_sanity != sanity_preimage:
            raise RuntimeError("EPIC029_SANITY_LOG_PREIMAGE_CHANGED")
        paths = _candidate_paths(stage)
        candidate = _capture_staged_candidate(stage, paths)
        staged_stdout = completed.stdout
    if staged_stdout:
        print(staged_stdout, end="")
    try:
        current_sanity = (ROOT / SANITY_LOG_REL).read_bytes()
    except OSError as exc:
        raise RuntimeError("EPIC029_SANITY_LOG_PREIMAGE_CHANGED") from exc
    if current_sanity != sanity_preimage:
        raise RuntimeError("EPIC029_SANITY_LOG_PREIMAGE_CHANGED")
    if _require_git_head(ROOT) != revision:
        raise RuntimeError("EPIC029_SOURCE_HEAD_CHANGED")
    _publish_captured_candidate(
        candidate,
        ROOT,
        expected_preimages=publication_preimages,
    )
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--staged-materialization", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(list(argv or ()))
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    try:
        return (
            _materialize_staged_close_pack()
            if args.staged_materialization
            else _orchestrate_from_head()
        )
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
