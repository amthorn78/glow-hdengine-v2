#!/usr/bin/env python3
"""Regenerate and verify the complete identity and release evidence closure."""
from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping

ROOT = Path(__file__).resolve().parents[2]

CLOSED_RAILS = {
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "PIP_NO_INDEX": "1",
}

RELEASE_RECOMPUTE_OUTPUTS = (
    "artifacts/math/freeze_pack_manifest.json",
    "artifacts/math/freeze_pack_manifest.json.sha256",
    "artifacts/math/release_id.txt",
    "artifacts/math/release_id.txt.sha256",
    "artifacts/math/release_id_recompute.log",
    "artifacts/math/release_id_recompute.log.sha256",
    "artifacts/math/checksums_audit.log",
    "artifacts/math/manifest_snapshot.json",
    "artifacts/proofs/env_pins.txt",
)
CONFIG_ARTIFACT_OUTPUTS = (
    "artifacts/registry/registry_report.json",
    "artifacts/thresholds/magic10_config.json",
    "artifacts/thresholds/band_edges.json",
)
CONFIG_BUNDLE_OUTPUTS = (
    "artifacts/config_bundles/be_bundle.json",
    "artifacts/config_bundles/fe_bundle.json",
)
ENV_MATRIX_OUTPUTS = ("artifacts/runtime/env_matrix.snapshot.json",)
IDENTITY_PROVENANCE_OUTPUTS = (
    "artifacts/identity/service_identity.json",
    "artifacts/identity/release_id.json",
    "artifacts/identity/release_id_recompute.log",
    "artifacts/identity/emitter_sha256.json",
    "artifacts/identity/invocation_sha256.json",
    "artifacts/parity/two_run_identity.log",
)
RELEASE_BINDING_OUTPUTS = ("artifacts/bodygraph/release_bindings.json",)
SHOWCOMPAT_OUTPUTS = (
    "artifacts/cli/showcompat/stdout.json",
    "artifacts/cli/showcompat/stdout.json.sha256",
    "artifacts/cli/showcompat/args.json",
)
CLI_CONFORMANCE_OUTPUTS = (
    "artifacts/cli/ab.json",
    "artifacts/cli/ba.json",
    "artifacts/cli/summary.json",
    "artifacts/cli/help/hdctl_help.txt",
    "artifacts/cli/help/showcompat_help.txt",
    "artifacts/cli/help/reject_nonjson.txt",
    "artifacts/cli/install/entrypoints.txt",
    "artifacts/cli/install/installability_summary.json",
)
CANONICAL_JSON_OUTPUTS = (
    "audit/gates/canonical_json/json_canonical_check.log",
    "audit/gates/canonical_json/json_canon_compare.log",
    "audit/gates/canonical_json/canonical_json.gate.json",
    "audit/gates/json_gate/canonical/json_gate_check_log.ndjson",
    "audit/gates/json_gate/canonical/json_gate_compare_log.ndjson",
    "audit/gates/json_gate/canonical/json_gate_structured_record.json",
)
READER_CLI_DETERMINISM_OUTPUTS = (
    "audit/gates/parity/reader_cli/ab.json",
    "audit/gates/parity/reader_cli/ba.json",
    "audit/gates/parity/reader_cli/summary.json",
    "audit/gates/determinism/abba.bytes",
    "audit/gates/determinism/tworun_identity.sha256",
    "artifacts/cards/a3/IDENTITY_OK.txt",
)
OPEN_RAILS_ABBA_OUTPUTS = ("audit/gates/determinism/open_rails_abba.json",)
A7_TRANSPORT_OUTPUTS = (
    "docs/ENDPOINTS_CATALOG.json",
    "docs/ENDPOINTS_CATALOG.json.sha256",
    "artifacts/audit/ENDPOINTS_CATALOG.json",
    "artifacts/audit/ENDPOINTS_CATALOG.json.sha256",
    "artifacts/reader/endpoints_snapshot.json",
    "artifacts/proofs/endpoints_env_gate_proof.log",
    "artifacts/proofs/success_get.txt",
    "artifacts/proofs/success_head.txt",
    "artifacts/proofs/success_304.txt",
    "artifacts/proofs/success_writers_errors.txt",
    "artifacts/proofs/success_encoding_invariance.txt",
    "artifacts/proofs/reader_success_get_head_304.json",
)
RAILS_GATE_OUTPUTS = (
    "artifacts/proofs/ops_refusal_proof.txt",
    "artifacts/vendor/retry_after_parse.log",
    "artifacts/vendor/rails_gate_keys_only.logs.sample",
)
DB_RUNTIME_OUTPUTS = (
    "artifacts/db/ddl_fingerprint.json",
    "artifacts/db/grants.txt",
    "artifacts/db/check_schema.txt",
    "artifacts/db/check_constraints.txt",
    "artifacts/db/boundary_view.readonly.proof.txt",
    "artifacts/db/partition_plan.txt",
    "artifacts/db/partition_verify.log",
)
BODYGRAPH_POLICY_OUTPUTS = (
    "artifacts/bodygraph/source_selection.snapshot.json",
    "artifacts/bodygraph/refresh_policy.snapshot.json",
    "artifacts/bodygraph/metrics.snapshot.json",
    "artifacts/bodygraph/keys_only.logs.sample",
    "artifacts/bodygraph/source_invariance/ab.json",
    "artifacts/bodygraph/source_invariance/ba.json",
    "artifacts/bodygraph/source_invariance/summary.json",
)
ARCHITECTURE_OUTPUTS = (
    "artifacts/architecture/architecture_snapshot.keys_only.json",
)
MAPPED_CACHE_OUTPUTS = (
    "artifacts/bodygraph/v2_mapped_cache/write_transcript.json",
    "artifacts/bodygraph/v2_mapped_cache/read_back_transcript.json",
    "artifacts/bodygraph/v2_mapped_cache/canonical_parity.log",
    "artifacts/bodygraph/v2_mapped_cache/no_raw_vendor_payload_persistence.log",
    "artifacts/bodygraph/v2_mapped_cache/idempotence.log",
    "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log",
    "artifacts/bodygraph/v2_mapped_cache/legacy_fallback_preservation.log",
    "artifacts/bodygraph/v2_mapped_cache/manifest.json",
)
INTERNAL_VERSION_OUTPUTS = (
    "artifacts/ops/internal_version/body_get.json",
    "artifacts/ops/internal_version/body_get.sha256",
    "artifacts/ops/internal_version/headers_get.txt",
    "artifacts/ops/internal_version/headers_head.txt",
    "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
    "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
    "artifacts/ops/internal_version/two_run_identity.log",
    "artifacts/ops/internal_version/request_chain_manifest.json",
)
EVIDENCE_INDEX_OUTPUTS = (
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.sha256",
    "artifacts/evidence_index.jsonl",
    "artifacts/evidence_index.jsonl.sha256",
)
ORIENTATION_OUTPUTS = ("audit/gates/topology/orientation_demo.txt",)
SANITY_OUTPUTS = ("audit/gates/sanity_pipeline/sanity_pipeline.log",)


@dataclass(frozen=True)
class ClosureStep:
    """One deterministic producer and its residue-free validation command."""

    name: str
    write: tuple[str, ...]
    check: tuple[str, ...]
    outputs: tuple[str, ...]
    write_env: tuple[tuple[str, str], ...] = ()


# This is the single declared write/check graph for deterministic local release
# artifacts that must exist before OPS-03.  The release pipeline consumes these
# bytes in check mode; it must never discover and repair stale primaries itself.
CLOSURE_STEPS = (
    ClosureStep(
        "config_artifacts",
        ("tools/config/generate_config_artifacts.py",),
        ("tools/config/generate_config_artifacts.py", "--check"),
        CONFIG_ARTIFACT_OUTPUTS,
    ),
    ClosureStep(
        "config_bundles",
        ("tools/config/generate_bundles.py",),
        ("tools/config/generate_bundles.py", "--check"),
        CONFIG_BUNDLE_OUTPUTS,
    ),
    ClosureStep(
        "env_matrix",
        ("tools/evidence/generate_env_matrix_snapshot.py",),
        ("tools/evidence/generate_env_matrix_snapshot.py", "--check"),
        ENV_MATRIX_OUTPUTS,
    ),
    ClosureStep(
        "identity_provenance",
        ("tools/evidence/generate_identity_provenance.py",),
        ("tools/evidence/generate_identity_provenance.py", "--check"),
        IDENTITY_PROVENANCE_OUTPUTS,
    ),
    ClosureStep(
        "release_bindings",
        ("tools/evidence/generate_release_bindings.py",),
        ("tools/evidence/generate_release_bindings.py", "--check"),
        RELEASE_BINDING_OUTPUTS,
    ),
    ClosureStep(
        "showcompat",
        ("tools/cli/generate_showcompat_artifacts.py",),
        ("tools/cli/generate_showcompat_artifacts.py", "--check"),
        SHOWCOMPAT_OUTPUTS,
    ),
    ClosureStep(
        "cli_conformance",
        ("tools/cli/generate_cli_conformance_artifacts.py",),
        ("tools/cli/generate_cli_conformance_artifacts.py", "--check"),
        CLI_CONFORMANCE_OUTPUTS,
    ),
    ClosureStep(
        "canonical_json",
        ("tools/evidence/run_canonical_json_gate.py",),
        ("tools/evidence/run_canonical_json_gate.py", "--check-only"),
        CANONICAL_JSON_OUTPUTS,
    ),
    ClosureStep(
        "reader_cli_determinism",
        ("tools/evidence/generate_determinism_gate_proofs.py",),
        ("tools/evidence/generate_determinism_gate_proofs.py", "--check"),
        READER_CLI_DETERMINISM_OUTPUTS,
    ),
    ClosureStep(
        "fixture_open_rails_abba",
        ("tools/evidence/generate_open_rails_abba_proof.py",),
        ("tools/evidence/generate_open_rails_abba_proof.py", "--check"),
        OPEN_RAILS_ABBA_OUTPUTS,
    ),
    ClosureStep(
        "a7_transport",
        ("tools/evidence/generate_a7_transport_proofs.py",),
        ("tools/evidence/generate_a7_transport_proofs.py", "--check"),
        A7_TRANSPORT_OUTPUTS,
        (("HDE_WRITE_A7_PROOFS", "1"),),
    ),
    ClosureStep(
        "rails_gate",
        ("tools/evidence/generate_rails_gate_evidence.py",),
        ("tools/evidence/generate_rails_gate_evidence.py", "--check"),
        RAILS_GATE_OUTPUTS,
    ),
    ClosureStep(
        "db_runtime_posture",
        ("tools/evidence/generate_db_runtime_posture.py",),
        ("tools/evidence/generate_db_runtime_posture.py", "--check"),
        DB_RUNTIME_OUTPUTS,
    ),
    ClosureStep(
        "bodygraph_policy",
        ("tools/evidence/generate_bodygraph_policy_proofs.py",),
        ("tools/evidence/generate_bodygraph_policy_proofs.py", "--check"),
        BODYGRAPH_POLICY_OUTPUTS,
    ),
    ClosureStep(
        "architecture_snapshot",
        ("tools/evidence/generate_architecture_snapshot.py",),
        ("tools/evidence/generate_architecture_snapshot.py", "--check"),
        ARCHITECTURE_OUTPUTS,
    ),
    ClosureStep(
        "mapped_cache",
        ("tools/evidence/generate_v2_mapped_cache_evidence.py",),
        ("tools/evidence/generate_v2_mapped_cache_evidence.py", "--check"),
        MAPPED_CACHE_OUTPUTS,
    ),
    ClosureStep(
        "internal_version",
        (
            "-m",
            "pytest",
            "tests/transport/test_internal_version_contract.py",
            "-q",
        ),
        (
            "-m",
            "pytest",
            "tests/evidence/test_internal_version_manifest_captures.py",
            "-q",
        ),
        INTERNAL_VERSION_OUTPUTS,
    ),
    ClosureStep(
        "evidence_index",
        ("tools/evidence/update_evidence_index.py",),
        ("tools/evidence/update_evidence_index.py", "--check"),
        EVIDENCE_INDEX_OUTPUTS,
    ),
    ClosureStep(
        "orientation",
        ("tools/evidence/orientation_demo.py",),
        ("tools/evidence/orientation_demo.py", "--check"),
        ORIENTATION_OUTPUTS,
    ),
)

DECLARED_PRODUCER_OUTPUTS = (
    *RELEASE_RECOMPUTE_OUTPUTS,
    *(path for step in CLOSURE_STEPS for path in step.outputs),
    *SANITY_OUTPUTS,
)
ATTESTATION_PRIMARY_OUTPUTS = tuple(sorted(set(DECLARED_PRODUCER_OUTPUTS)))
ATTESTATION_PATH_PROOF_TARGETS = tuple(
    path
    for path in ATTESTATION_PRIMARY_OUTPUTS
    if path not in set(RELEASE_RECOMPUTE_OUTPUTS)
)
ATTESTATION_GENERATED_OUTPUTS = tuple(
    sorted(
        (
            *ATTESTATION_PRIMARY_OUTPUTS,
            *(f"{path}.path_proof.txt" for path in ATTESTATION_PATH_PROOF_TARGETS),
        )
    )
)


def _env(overrides: Mapping[str, str] | None = None) -> dict[str, str]:
    env = os.environ.copy()
    env.update(CLOSED_RAILS)
    env.update(overrides or {})
    return env


def _run(*args: str, env_overrides: Mapping[str, str] | None = None) -> None:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=_env(env_overrides),
        check=False,
    )
    if proc.returncode != 0:
        raise SystemExit(f"CLOSURE_STEP_FAILED:{' '.join(args)}:{proc.returncode}")


def _is_current(*args: str, env_overrides: Mapping[str, str] | None = None) -> bool:
    proc = subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=_env(env_overrides),
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return proc.returncode == 0


def _ensure_step(step: ClosureStep) -> None:
    if _is_current(*step.check):
        return
    _run(*step.write, env_overrides=dict(step.write_env))
    _run(*step.check)


def _write_closure() -> None:
    # A closure build may repair derived outputs in an isolated copy, but it
    # never edits the source manifest. A stale manifest is a release-cut input
    # error and fails before any downstream producer can legitimize it.
    _run("scripts/release_id_recompute.py")
    _run("scripts/release_id_recompute.py", "--check")
    for step in CLOSURE_STEPS:
        _ensure_step(step)


def _check_closure() -> None:
    _run("scripts/release_id_recompute.py", "--check")
    for step in CLOSURE_STEPS:
        _run(*step.check)
    _run("tools/evidence/generate_open_rails_abba_proof.py", "--live", "--check")
    _run(
        "-m",
        "pytest",
        "tests/evidence/test_aux_preview_identity_parity.py",
        "tests/evidence/test_release_manifest_content_binding.py",
        "tests/qa/test_epic022_acceptance_scaffold.py",
        "tests/qa/test_epic022_close_pack_ready.py",
        "-q",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--in-place-isolated", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args(argv)
    if os.environ.get("HDE_ISOLATED_RELEASE_BUILD") != "1":
        raise SystemExit(
            "SOURCE_TREE_RELEASE_CLOSURE_REFUSED:"
            "use tools/evidence/build_release_attestation.py"
        )
    if not args.in_place_isolated:
        raise SystemExit("ISOLATED_RELEASE_BUILD_MODE_REQUIRED")
    if args.check:
        _check_closure()
    else:
        _write_closure()
        _check_closure()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
