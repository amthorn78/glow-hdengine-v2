#!/usr/bin/env python3
"""Run the HDE-EPIC038 closed-rails release-sanity chain."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
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
PIPELINE_ID = "HDE-EPIC038-PR06-release-sanity"

OPS_FILES = {
    "ops-01": ("commands.txt", "stdout.log", "stderr.log", "exit_code.txt", "env_presence.json", "db_posture_summary.json", "provider_parity.proof.json", "bridge_consistency.result.json", "nonclaims.json", "result_summary.json", "checksums.sha256"),
    "ops-02": ("commands.txt", "stdout.log", "stderr.log", "exit_code.txt", "env_presence.json", "request_summary.json", "mapped_output_summary.json", "read_back_summary.json", "canonical_parity.log", "idempotence.log", "no_raw_vendor_payload_persistence.log", "legacy_fallback_preservation.log", "nonclaims.json", "result_summary.json", "checksums.sha256"),
}


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


STAGE_NAMES = (
    "01 Environment pins", "02 Identity and release provenance", "03 Canonical JSON",
    "04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks", "05 A7 Catalog transport",
    "06 CI rails", "07 DB posture", "08 BodyGraph policy", "09 DB-bridge parity",
    "10 Architecture snapshot", "11 Configured-v2 mapped-cache local evidence",
    "12 OPS evidence checksum and summary validation", "13 Human Index and Machine Mirror refresh",
    "14 Path validation", "15 Mirror schema and hash validation",
    "16 Topology orientation validation", "17 Final LF validation",
)


def _py(path: str, *args: str) -> tuple[str, ...]:
    return (sys.executable, path, *args)


def default_steps() -> list[SanityStep]:
    return [
        SanityStep(STAGE_NAMES[0], (("ci/checks/check_env_pins.sh",),)),
        SanityStep(STAGE_NAMES[1], (_py("tools/evidence/generate_identity_provenance.py"), _py("tools/evidence/generate_release_bindings.py"), _py("tools/evidence/generate_env_matrix_snapshot.py"))),
        SanityStep(STAGE_NAMES[2], (_py("tools/evidence/run_canonical_json_gate.py", "--check-only"),)),
        SanityStep(STAGE_NAMES[3], (_py("tools/evidence/generate_determinism_gate_proofs.py"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--check"), _py("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check"))),
        SanityStep(STAGE_NAMES[4], (_py("tools/evidence/generate_a7_transport_proofs.py"),)),
        SanityStep(STAGE_NAMES[5], (_py("tools/evidence/generate_rails_gate_evidence.py"), _py("ci/checks/run_rails_job_definitions.py", "ci/jobs/rails_closed_refusal.yml", "ci/jobs/rails_open_conformance.yml", "ci/jobs/logs_keys_only_redaction.yml"))),
        SanityStep(STAGE_NAMES[6], (_py("tools/evidence/generate_db_runtime_posture.py"),)),
        SanityStep(STAGE_NAMES[7], (_py("tools/evidence/generate_bodygraph_policy_proofs.py"),)),
        SanityStep(STAGE_NAMES[8], (_py("tools/evidence/generate_db_bridge_parity.py"),)),
        SanityStep(STAGE_NAMES[9], (_py("tools/evidence/generate_architecture_snapshot.py"),)),
        SanityStep(STAGE_NAMES[10], (_py("tools/evidence/generate_v2_mapped_cache_evidence.py"),)),
        SanityStep(STAGE_NAMES[11], (("__validate_ops__",),)),
        SanityStep(STAGE_NAMES[12], (_py("tools/evidence/update_evidence_index.py"),)),
        SanityStep(STAGE_NAMES[13], (_py("tools/evidence/validate_evidence_paths.py"),)),
        SanityStep(STAGE_NAMES[14], (("ci/checks/check_mirror_schema.sh",), ("bash", "ci/checks/check_evidence_index_hash.sh"))),
        SanityStep(STAGE_NAMES[15], (_py("tools/evidence/orientation_demo.py"), _py("tools/evidence/update_evidence_index.py"), _py("tools/evidence/orientation_demo.py", "--check"))),
        SanityStep(STAGE_NAMES[16], (_py("tools/evidence/update_evidence_index.py"), _py("tools/evidence/update_evidence_index.py"), _py("tools/evidence/update_evidence_index.py", "--check"), _py("tools/evidence/orientation_demo.py", "--check"), ("ci/checks/check_mirror_schema.sh",), ("bash", "ci/checks/check_evidence_index_hash.sh"), ("ci/checks/check_final_lf.sh",))),
    ]


def _read_json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path.relative_to(ROOT)}: invalid JSON") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{path.relative_to(ROOT)}: expected JSON object")
    return value


def _validate_packet(root: Path, package: str, required: Sequence[str]) -> None:
    packet = root / "audit/ops/hde-epic038" / package
    for name in required:
        path = packet / name
        if not path.is_file() or path.stat().st_size == 0:
            raise ValueError(f"{package}: required file {name} is missing or empty")
    expected = set(required) - {"checksums.sha256"}
    rows: dict[str, str] = {}
    pattern = re.compile(r"^([0-9a-f]{64})  ([A-Za-z0-9_.-]+)$")
    for line_number, line in enumerate((packet / "checksums.sha256").read_text(encoding="ascii").splitlines(), 1):
        match = pattern.fullmatch(line)
        if not match:
            raise ValueError(f"{package}: checksums.sha256 malformed row {line_number}")
        digest, name = match.groups()
        if name in rows:
            raise ValueError(f"{package}: checksums.sha256 duplicate row for {name}")
        if name not in expected:
            raise ValueError(f"{package}: checksums.sha256 unknown or escaping path {name}")
        rows[name] = digest
    missing = expected - rows.keys()
    if missing:
        raise ValueError(f"{package}: checksums.sha256 missing {sorted(missing)[0]}")
    for name in sorted(expected):
        actual = hashlib.sha256((packet / name).read_bytes()).hexdigest()
        if actual != rows[name]:
            raise ValueError(f"{package}: checksums.sha256 mismatch for {name}")
    if (packet / "exit_code.txt").read_text(encoding="utf-8").strip() != "0":
        raise ValueError(f"{package}: exit_code.txt is not successful")

    summary = _read_json(packet / "result_summary.json")
    nonclaims = _read_json(packet / "nonclaims.json").get("nonclaims", [])
    required_nonclaims = {"no_qa_pass_claim", "no_acceptance_token_claim", "no_pf09_status_movement", "no_epic_closeout_claim"}
    if not required_nonclaims.issubset(nonclaims):
        raise ValueError(f"{package}: nonclaims.json is incomplete")
    if package == "ops-01":
        observations = summary.get("observations", {})
        if summary.get("ops_observation_status") != "PASS" or observations.get("db_posture") != "PASS" or observations.get("bridge_consistency") != "PASS":
            raise ValueError("ops-01: result_summary.json PASS predicates failed")
        parity = _read_json(packet / "provider_parity.proof.json")
        rows = parity.get("capabilities", [])
        rows_well_formed = (
            isinstance(rows, list)
            and bool(rows)
            and all(
                isinstance(row, dict)
                and isinstance(row.get("direct"), dict)
                and isinstance(row.get("bridge"), dict)
                for row in rows
            )
        )
        if not rows_well_formed or any(row.get("parity") != "match" or row["direct"].get("status") != "ok" or row["bridge"].get("status") != "ok" for row in rows):
            raise ValueError("ops-01: provider_parity.proof.json contains unavailable, errored, or unmatched claimed row")
        if observations.get("claimed_rows") != len(rows) or observations.get("matched_rows") != len(rows):
            raise ValueError("ops-01: result_summary.json claimed parity row counts failed")
    else:
        predicates = summary.get("predicates", {})
        required_predicates = {"adapter_mapped", "exactly_one_vendor_request", "canonical_write_read_back_equivalence", "idempotent_repeated_write", "mapped_payload_only", "normalized_identity_single_row", "production_like_refused", "explicit_legacy_fallback_preserved", "retained_by_po_decision"}
        if summary.get("status") != "PASS" or summary.get("retention_decision") != "retain" or any(predicates.get(key) is not True for key in required_predicates):
            raise ValueError("ops-02: result_summary.json PASS predicate failed")


def validate_ops_packages(root: Path = ROOT) -> None:
    for package, required in OPS_FILES.items():
        _validate_packet(root, package, required)


def _run_command(command: Sequence[str]) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env.update(DETERMINISM_ENV_PINS)
    if any(item.endswith("generate_a7_transport_proofs.py") for item in command):
        env["HDE_WRITE_A7_PROOFS"] = "1"
    return subprocess.run(command, cwd=ROOT, env=env, capture_output=True, text=True)


def _run_stage(step: SanityStep) -> int:
    for command in step.commands:
        if command == ("__validate_ops__",):
            try:
                validate_ops_packages()
            except ValueError as exc:
                print(str(exc), file=sys.stderr)
                return 1
        else:
            result = _run_command(command)
            if result.returncode:
                return result.returncode or 1
    return 0


def _write_log(path: Path, results: Sequence[tuple[str, str]], first_failure: str, summary: str) -> None:
    lines = [f"pipeline:{PIPELINE_ID}", "environment:" + ",".join(f"{key}={DETERMINISM_ENV_PINS[key]}" for key in sorted(DETERMINISM_ENV_PINS)), "ops_evidence:validated_existing_bytes_only;not_rerun=true"]
    lines.extend(f"stage:{name};status={status}" for name, status in results)
    lines.extend((f"first_failed_stage:{first_failure}", f"summary:{summary}"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(("\n".join(lines) + "\n").encode("utf-8"))


def run_pipeline(*, log_path: Path = SANITY_LOG, steps: Sequence[SanityStep] | None = None, refresh_index: bool = True) -> int:
    ensure_determinism_env()
    roster = list(default_steps() if steps is None else steps)
    results: list[tuple[str, str]] = []
    failure = "NONE"
    code = 0
    for index, step in enumerate(roster):
        # The final updater must bind the final sanity bytes, not an interim
        # version.  Render the prospective PASS log before that updater runs;
        # the normal final render below is byte-identical on success.
        if log_path == SANITY_LOG and index == len(roster) - 1 and not failure:
            _write_log(log_path, [*results, (step.name, "OK")], "NONE", "PASS")
        code = _run_stage(step)
        results.append((step.name, "OK" if code == 0 else "FAIL"))
        if code:
            failure = step.name
            results.extend((later.name, f"NOT_EXECUTED_EARLIER_FAILURE:{step.name}") for later in roster[index + 1:])
            break
    passed = code == 0 and len(results) == len(roster) and all(status == "OK" for _, status in results)
    _write_log(log_path, results, failure, "PASS" if passed else "FAIL")
    return 0 if passed else (code or 1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-path", type=Path, default=SANITY_LOG)
    args = parser.parse_args(argv)
    return run_pipeline(log_path=args.log_path)


if __name__ == "__main__":
    raise SystemExit(main())
