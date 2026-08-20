#!/usr/bin/env python3
"""Run the generic closed-rails release-sanity chain."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env

SANITY_LOG = ROOT / "audit/gates/sanity_pipeline/sanity_pipeline.log"
PIPELINE_ID = "hde-release-sanity-v1"

@dataclass(frozen=True)
class SanityStep:
    name: str
    commands: tuple[tuple[str, ...], ...]

    def __init__(self, name: str, command: Sequence[str] | Sequence[Sequence[str]]):
        object.__setattr__(self, "name", name)
        if command and isinstance(command[0], str):
            object.__setattr__(self, "commands", (tuple(command),))
        else:
            object.__setattr__(self, "commands", tuple(tuple(item) for item in command))


# PF10 — HDE Build Notes, §2.3 places only continuing current-source risks in
# this generic release lane. The former nineteen-stage HDE-EPIC038 family is
# not a current admission surface: architecture is protected independently in
# product CI, and its historical-bridge/OPS packet stages remain audit history.
# This result therefore makes no HDE-EPIC038, QA, acceptance, PF09, OPS,
# deployment, or closeout claim.
STAGE_NAMES = (
    "01 Environment pins", "02 Identity and release provenance", "03 Canonical JSON",
    "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks", "05 A7 Catalog transport",
    "06 CI rails", "07 Direct DB selection contract", "08 Direct DB posture artifacts",
    "09 BodyGraph policy", "10 Configured-v2 mapped-cache behavior",
    "11 Human Index and Machine Mirror refresh", "12 Evidence-path validation",
    "13 Mirror schema and index/mirror hash validation",
    "14 Topology orientation validation", "15 Final-LF validation",
)


def _py(path: str, *args: str) -> tuple[str, ...]:
    return (sys.executable, path, *args)


def default_steps() -> list[SanityStep]:
    return [
        SanityStep(STAGE_NAMES[0], (("ci/checks/check_env_pins.sh",),)),
        SanityStep(STAGE_NAMES[1], (
            _py("tools/config/generate_config_artifacts.py", "--check"),
            _py("tools/config/generate_bundles.py", "--check"),
            _py("tools/evidence/generate_env_matrix_snapshot.py", "--check"),
            _py("scripts/release_id_recompute.py", "--check-manifest-only"),
        )),
        SanityStep(STAGE_NAMES[2], (_py("tools/evidence/run_canonical_json_gate.py", "--check-only"),)),
        SanityStep(STAGE_NAMES[3], (("__validate_reader_cli_determinism__",), _py("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check"))),
        SanityStep(STAGE_NAMES[4], (("__validate_a7_transport__",),)),
        SanityStep(STAGE_NAMES[5], (_py("tools/evidence/generate_rails_gate_evidence.py", "--check"), _py("ci/checks/run_rails_job_definitions.py", "ci/jobs/rails_closed_refusal.yml", "ci/jobs/rails_open_conformance.yml", "ci/jobs/logs_keys_only_redaction.yml"))),
        SanityStep(STAGE_NAMES[6], (("__validate_direct_selection__",), _py("ci/checks/check_direct_db_contract.py"))),
        SanityStep(STAGE_NAMES[7], (_py("tools/evidence/generate_db_runtime_posture.py", "--check"),)),
        SanityStep(STAGE_NAMES[8], (_py("tools/evidence/generate_bodygraph_policy_proofs.py", "--check"),)),
        SanityStep(STAGE_NAMES[9], (("__validate_mapped_cache__",),)),
        SanityStep(
            STAGE_NAMES[10],
            (_py("tools/evidence/update_evidence_index.py", "--check"),),
        ),
        SanityStep(STAGE_NAMES[11], (_py("tools/evidence/validate_evidence_paths.py"),)),
        SanityStep(STAGE_NAMES[12], (("ci/checks/check_mirror_schema.sh",), ("bash", "ci/checks/check_evidence_index_hash.sh"))),
        SanityStep(
            STAGE_NAMES[13],
            (_py("tools/evidence/orientation_demo.py", "--check"),),
        ),
        SanityStep(STAGE_NAMES[14], (("ci/checks/check_final_lf.sh",),)),
    ]


def validate_direct_selection_contract() -> None:
    """Validate the tracked direct-selection primary against producer and schema."""

    from tools.evidence import generate_hde_epic038_direct_db_selection as direct

    primary = direct.OUT
    if not primary.is_file() or primary.is_symlink():
        raise ValueError("direct selection tracked primary missing")
    raw = primary.read_bytes()
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        raise ValueError("direct selection primary final LF invalid")
    payload = json.loads(raw.decode("utf-8"))
    first = direct.build()
    second = direct.build()
    expected = direct.canonical_bytes(first)
    if (
        direct.validate_contract(payload)
        or direct.validate_contract(first)
        or payload.get("result") != "PASS"
        or payload.get("failure") is not None
        or raw != expected
        or expected != direct.canonical_bytes(second)
    ):
        raise ValueError("direct selection contract validation failed")


def _run_command(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(DETERMINISM_ENV_PINS)
    if any(item.endswith("generate_a7_transport_proofs.py") for item in command):
        env["HDE_WRITE_A7_PROOFS"] = "1"
    return subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)


def validate_current_reader_cli_determinism() -> None:
    """Validate current behavior without rewriting frozen capture-time outputs."""

    from tools.evidence import generate_determinism_gate_proofs as determinism
    from tools.evidence import generate_open_rails_abba_proof as open_rails

    top_level, outputs = determinism.build()
    summary = json.loads(outputs[determinism.SUM])
    if (
        top_level is not True
        or summary.get("top_level_pass") is not True
        or not all(summary.get("predicates", {}).values())
    ):
        raise ValueError("current determinism predicates failed")
    fixture = open_rails.build_fixture_proof()
    if (
        fixture.get("top_level_pass") is not True
        or fixture.get("transport_call_count") != 0
        or not all(fixture.get("predicates", {}).values())
    ):
        raise ValueError("current open-rails fixture predicates failed")


def validate_current_a7_transport() -> None:
    """Exercise the current A7 transport contract without refreshing captures."""

    from tools.evidence import generate_a7_transport_proofs as transport

    outputs = transport.build()
    composite = json.loads(outputs[transport.PROOFS[6]])
    transport.validate_composite(composite)
    if not all(
        composite[name].get("pass") is True
        for name in ("get_200", "head_200", "after_304", "env_gate")
    ):
        raise ValueError("current A7 transport predicates failed")


def validate_current_mapped_cache() -> None:
    """Exercise current mapped-cache behavior without binding tracked evidence."""

    from tools.evidence import generate_v2_mapped_cache_evidence as mapped_cache

    outputs = mapped_cache.build()
    manifest_path = mapped_cache.OUT / "manifest.json"
    try:
        manifest = json.loads(outputs[manifest_path].decode("utf-8"))
    except (KeyError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("current mapped-cache manifest is invalid") from exc
    predicates = manifest.get("predicates")
    if (
        manifest.get("status") != "PASS"
        or not isinstance(predicates, dict)
        or set(predicates) != set(mapped_cache.PREDICATE_KEYS)
        or not all(value is True for value in predicates.values())
    ):
        raise ValueError("current mapped-cache behavior failed")


def _run_stage(step: SanityStep) -> int:
    for command in step.commands:
        if command == ("__validate_direct_selection__",):
            try:
                validate_direct_selection_contract()
            except Exception:
                print("direct_selection_contract_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_reader_cli_determinism__",):
            try:
                validate_current_reader_cli_determinism()
            except Exception:
                print("reader_cli_determinism_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_a7_transport__",):
            try:
                validate_current_a7_transport()
            except Exception:
                print("a7_transport_validation_failed", file=sys.stderr)
                return 1
        elif command == ("__validate_mapped_cache__",):
            try:
                validate_current_mapped_cache()
            except Exception:
                print("mapped_cache_validation_failed", file=sys.stderr)
                return 1
        else:
            result = _run_command(command)
            if result.returncode:
                print(
                    f"{step.name}: command exited {result.returncode}: {' '.join(command)}",
                    file=sys.stderr,
                )
                return result.returncode or 1
    return 0


def _render_log(results: Sequence[tuple[str, str]], first_failure: str, summary: str) -> bytes:
    lines = ["run:sanity-pipeline", f"pipeline_identity:{PIPELINE_ID}", "env:" + ",".join(f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)), "env_pins:audit/gates/determinism/env_pins.log"]
    for name, status in results:
        canonical_status = "OK" if status == "OK" else "FAIL"
        lines.append(f"check {name}:{canonical_status}")
        if status.startswith("NOT_EXECUTED_EARLIER_FAILURE:"):
            lines.append(f"not_executed {name}:earlier_mandatory_failure={status.split(':', 1)[1]}")
    lines.extend((f"first_failed_stage:{first_failure}", f"summary:{summary}"))
    return ("\n".join(lines) + "\n").encode("utf-8")


def _write_log(path: Path, results: Sequence[tuple[str, str]], first_failure: str, summary: str) -> bytes:
    data = _render_log(results, first_failure, summary)
    path.parent.mkdir(parents=True, exist_ok=True)
    try:
        current = path.read_bytes()
    except OSError:
        current = None
    if current != data:
        path.write_bytes(data)
    return data


def _rebind_failure_log() -> int:
    """Bind only the final FAIL log while preserving the evidence topology."""
    result = _run_command(
        _py("tools/evidence/update_evidence_index.py", "--rebind-sanity-log")
    )
    return result.returncode or 0


def run_pipeline(*, log_path: Path = SANITY_LOG, steps: Sequence[SanityStep] | None = None, refresh_index: bool = True) -> int:
    ensure_determinism_env()
    log_path = (log_path if log_path.is_absolute() else ROOT / log_path).resolve()
    roster = list(default_steps() if steps is None else steps)
    canonical_run = log_path == SANITY_LOG.resolve() and steps is None
    results: list[tuple[str, str]] = []
    failure = "NONE"
    code = 0
    prospective_pass: bytes | None = None
    sealing_index = next(
        (index for index, step in enumerate(roster) if step.name == STAGE_NAMES[10]),
        len(roster) - 1,
    )
    for index, step in enumerate(roster):
        # The final updater must bind the final sanity bytes, not an interim
        # version.  Render the prospective PASS log before that updater runs;
        # the normal final render below is byte-identical on success.
        if canonical_run and index == sealing_index and failure == "NONE":
            prospective_pass = _write_log(
                log_path,
                [*results, *((later.name, "OK") for later in roster[index:])],
                "NONE",
                "PASS",
            )
        code = _run_stage(step)
        status = "OK" if code == 0 else "FAIL"
        results.append((step.name, status))
        if code:
            failure = step.name
            results.extend((later.name, f"NOT_EXECUTED_EARLIER_FAILURE:{step.name}") for later in roster[index + 1:])
            break
    passed = code == 0 and len(results) == len(roster) and all(status == "OK" for _, status in results)
    final_bytes = _render_log(results, failure, "PASS" if passed else "FAIL")
    if passed and canonical_run:
        try:
            current_bytes = log_path.read_bytes()
        except OSError:
            current_bytes = b""
        if prospective_pass != final_bytes or current_bytes != final_bytes:
            print(
                "canonical PASS bytes changed during final evidence sealing: "
                f"prospective={hashlib.sha256(prospective_pass or b'').hexdigest()}:{len(prospective_pass or b'')} "
                f"current={hashlib.sha256(current_bytes).hexdigest()}:{len(current_bytes)} "
                f"final={hashlib.sha256(final_bytes).hexdigest()}:{len(final_bytes)}",
                file=sys.stderr,
            )
            results[-1] = (results[-1][0], "FAIL")
            failure = results[-1][0]
            _write_log(log_path, results, failure, "FAIL")
            seal_code = _rebind_failure_log()
            if seal_code:
                print(f"canonical FAIL evidence finalization failed with exit code {seal_code}", file=sys.stderr)
                return seal_code
            return 1
        return 0

    try:
        prior_final_bytes = log_path.read_bytes()
    except OSError:
        prior_final_bytes = None
    _write_log(log_path, results, failure, "PASS" if passed else "FAIL")
    if not passed and canonical_run and prior_final_bytes != final_bytes:
        seal_code = _rebind_failure_log()
        if seal_code:
            print(f"canonical FAIL evidence finalization failed with exit code {seal_code}", file=sys.stderr)
            return seal_code
    return 0 if passed else (code or 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-path", type=Path, default=SANITY_LOG)
    args = parser.parse_args(argv)
    return run_pipeline(log_path=args.log_path)


if __name__ == "__main__":
    raise SystemExit(main())
