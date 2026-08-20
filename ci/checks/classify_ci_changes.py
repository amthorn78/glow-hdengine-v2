#!/usr/bin/env python3
"""Classify an exact Git change into the smallest safe CI lane set.

The classifier is deliberately repository-owned and fail-safe. Known paths select
only the lanes whose protected inputs they can affect. Unclassified paths and Git
events without a usable comparison base fail explicitly rather than silently
skipping protection.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[2]
LANES = ("product", "compat", "db", "rails", "evidence", "qa", "release")
SHA_RE = re.compile(r"[0-9a-fA-F]{40,64}\Z")

_FULL_VALIDATION_PREFIXES = (
    ".github/",
)
_FULL_VALIDATION_PATHS = {
    "ci/checks/classify_ci_changes.py",
    "pyproject.toml",
    "pytest.ini",
    "requirements-dev.txt",
    "requirements.txt",
    "tests/evidence/test_rails_ci_workflow_integration.py",
}
_FULL_VALIDATION_SUPPLEMENTAL_TESTS = (
    "tests/categories/test_registry_and_purity.py",
    "tests/cli/test_aux_preview.py",
    "tests/cli/test_bg_resolve.py",
    "tests/cli/test_cli_file_inputs.py",
    "tests/cli/test_cli_install_help.py",
    "tests/cli/test_dev_sampler_cli.py",
    "tests/cli/test_showcompat_sources.py",
    "tests/config/test_alias_policy_enforcement.py",
    "tests/config/test_config_artifacts.py",
    "tests/config/test_config_loader_unknown_ids_fail_closed.py",
    "tests/config/test_manifest_schema.py",
    "tests/config/test_registry_report.py",
    "tests/config/test_registry_report_determinism.py",
    "tests/config/test_registry_report_indexing.py",
    "tests/config/test_typed_bundles.py",
    "tests/evidence/test_evidence_tool_ownership.py",
    "tests/invariance/test_bytes_identity.py",
    "tests/invariance/test_determinism_env_helper.py",
    "tests/invariance/test_locale_tz.py",
    "tests/m10/test_defs_order.py",
    "tests/m10/test_m10_symmetry_identity.py",
    "tests/m10/test_thresholds_rounding.py",
    "tests/mech/test_arrays_as_sets.py",
    "tests/mech/test_constants.py",
    "tests/qa/test_cli_admin_dumps.py",
    "tests/qa/test_cli_admin_parity.py",
    "tests/qa/test_epic023_acceptance_alignment.py",
    "tests/qa/test_epic024_bootstrap_status.py",
    "tests/qa/test_qa_tool_ownership.py",
    "tests/support/test_change_gates.py",
    "tests/transport/test_a7_transport_proofs.py",
    "tests/transport/test_aux_narrative.py",
    "tests/transport/test_ops_rails_refusal.py",
    "tests/transport/test_writers_errors_headers.py",
)
_FULL_VALIDATION_INACTIVE_TESTS = {
    # Administrative or source-writing checks that are intentionally outside
    # the current behavioral suite. Direct edits fail closed until a current
    # consumer and safe execution owner are established.
    "tests/cli/test_cli_env_pins_epic021.py",
    "tests/config/test_config_acceptance_map.py",
    "tests/qa/test_epic021_scaffolding.py",
    "tests/qa/test_epic022_acceptance_scaffold.py",
    "tests/qa/test_epic022_close_pack_ready.py",
}
_HISTORICAL_PREFIXES = (
    ".audit_src/",
    "_archive/",
    "_backup_",
    "artifacts/architecture/",
    "artifacts/epic020/",
    "audit/history/",
    "audit/historical/",
    "audit/ops/",
)
_DOCUMENTATION_PREFIXES = (
    "docs/crd/",
    "docs/pfcanon/",
    "docs/plans/",
    "docs/qa/",
    "docs/run/",
)
_DOCUMENT_SUFFIXES = {".adoc", ".md", ".rst"}
_DOCUMENT_PATHS = {
    "LICENSE",
    "AcceptanceMap.md",
    "AGENTS.md",
    "ARCHITECTURE.md",
    "CHANGELOG.md",
    "README.md",
}
_RELEASE_EVIDENCE_PREFIXES = (
    "artifacts/audit/",
    "artifacts/bodygraph/",
    "artifacts/cards/",
    "artifacts/cli/",
    "artifacts/config_bundles/",
    "artifacts/db/",
    "artifacts/identity/",
    "artifacts/math/",
    "artifacts/ops/",
    "artifacts/parity/",
    "artifacts/presenter/",
    "artifacts/proofs/",
    "artifacts/reader/",
    "artifacts/registry/",
    "artifacts/runtime/",
    "artifacts/thresholds/",
    "artifacts/vendor/",
    "audit/gates/",
    "docs/evidence/",
)
_RELEASE_IMPLEMENTATION_PATHS = {
    "ci/checks/check_evidence_index_hash.sh",
    "ci/checks/check_env_pins.sh",
    "ci/checks/check_final_lf.sh",
    "ci/checks/check_mirror_schema.sh",
    "ci/checks/run_rails_job_definitions.py",
    "scripts/release_id_recompute.py",
    "tests/evidence/test_internal_version_manifest_captures.py",
    "tools/cli/generate_cli_conformance_artifacts.py",
    "tools/cli/generate_showcompat_artifacts.py",
    "tools/config/generate_bundles.py",
    "tools/config/generate_config_artifacts.py",
    "tools/evidence/build_release_attestation.py",
    "tools/evidence/generate_a7_transport_proofs.py",
    "tools/evidence/generate_bodygraph_policy_proofs.py",
    "tools/evidence/generate_db_runtime_posture.py",
    "tools/evidence/generate_determinism_gate_proofs.py",
    "tools/evidence/generate_env_matrix_snapshot.py",
    "tools/evidence/generate_hde_epic038_direct_db_selection.py",
    "tools/evidence/generate_identity_provenance.py",
    "tools/evidence/generate_open_rails_abba_proof.py",
    "tools/evidence/generate_rails_gate_evidence.py",
    "tools/evidence/generate_release_bindings.py",
    "tools/evidence/generate_v2_mapped_cache_evidence.py",
    "tools/evidence/orientation_demo.py",
    "tools/evidence/regenerate_identity_closure.py",
    "tools/evidence/retained_evidence_safety.py",
    "tools/evidence/run_canonical_json_gate.py",
    "tools/evidence/run_sanity_pipeline.py",
    "tools/evidence/run_sanity_pipeline_gate.py",
    "tools/evidence/update_evidence_index.py",
    "tools/evidence/validate_evidence_paths.py",
}
_RELEASE_IDENTITY_INPUT_PATHS = {"catalog/manifest.json"}
_ARCHITECTURE_ANALYSIS_PATHS = {
    "tests/evidence/test_architecture_snapshot.py",
    "tools/evidence/generate_architecture_snapshot.py",
}
_WORKFLOW_CONTROL_PATH_LANES = {
    "ci/checks/check_env_pins.sh": set(LANES),
    "ci/checks/check_cli_help.sh": {"compat"},
    "ci/checks/run_rails_job_definitions.py": {"rails", "release"},
    "tools/cli/emitter_symbol_proof.py": {"compat"},
    "tools/cli/serializer_grep_guard.py": {"compat"},
    "tools/order/generate_ordering_artifacts.py": {"product"},
}
_RAILS_MARKERS = (
    "open_rails",
    "rails_",
    "resolver_vendor",
    "vendor_client",
)
_COMPAT_MARKERS = (
    "/adapter/",
    "/catalog/",
    "/cli/",
    "/compat",
    "/http/",
    "/serializer",
    "/schemas/",
    "/transport/",
    "emitter",
    "http_reader",
    "showcompat",
)
_DB_MARKERS = (
    "/db/",
    "/migrations/",
    "/sql/",
    "cache_keys",
    "db_access",
    "direct_db",
    "ingest",
    "mapped_cache",
    "ops03",
)
_PRODUCT_PREFIXES = (
    "adapter/",
    "catalog/",
    "config/",
    "engine/",
    "math/",
    "migrations/",
    "presenter/",
    "schemas/",
    "scripts/",
    "sql/",
)
_SCHEMA_LANE_PREFIXES = (
    ("schemas/hde_release_attestation", {"release"}),
    ("schemas/architecture_snapshot", {"evidence"}),
    (
        "schemas/hde_epic038_direct_db_selection",
        {"db", "evidence", "release"},
    ),
    ("schemas/hde_epic038_ops03_", {"evidence"}),
)
_HISTORICAL_BACKUP_PATHS = {
    "engine/config/provider_loader.bak2",
    "engine/config/provider_loader.py.bak.1758996879",
    "engine/serializer/canon.py.bak.20251022212047",
    "scripts/card_close.sh.bak",
    "scripts/hdctl.backup.py",
    "scripts/hdctl.py.bak",
}
_NARRATIVE_TEST_OWNERS = (
    "tests/unit/test_narratives_router.py",
    "tests/unit/test_narratives_loader.py",
    "tests/cli/test_aux_preview.py",
)
_HTTP_READER_TEST_OWNERS = (
    "tests/adapter/test_compat_http_dev.py",
    "tests/adapter/test_compat_http_parity.py",
    "tests/adapter/test_dev_sampler_http.py",
    "tests/adapter/test_diagnostic_writer.py",
    "tests/cli/test_aux_preview.py",
    "tests/compat/test_abba_parity.py",
    "tests/db/test_conn_env_only.py",
    "tests/db/test_no_import_time_connect.py",
    "tests/http/test_compat_endpoint_contract.py",
    "tests/http/test_dev_conjunction_http.py",
    "tests/http/test_endpoint_catalog.py",
    "tests/http/test_reader_a7_transport.py",
    "tests/runtime/test_identity.py",
    "tests/transport/test_aux_narrative.py",
    "tests/transport/test_internal_version_contract.py",
    "tests/transport/test_ops_rails_refusal.py",
    "tests/transport/test_writers_errors_headers.py",
)
_PRODUCT_TEST_OWNER_PATHS = {
    "catalog/manifest.json": (
        "tests/runtime/test_identity.py",
        "tests/evidence/test_release_manifest_content_binding.py",
    ),
    "adapter/http_reader.py": _HTTP_READER_TEST_OWNERS,
    "engine/__init__.py": ("tests/runtime/test_identity.py",),
    "engine/constants.py": ("tests/mech/test_constants.py",),
    "engine/bodygraph/vendor_client.py": (
        "tests/bodygraph/test_vendor_client.py",
    ),
    "scripts/cut_release_manifest.py": ("tests/scripts/test_cut_release_manifest.py",),
    "scripts/emit_env_guard_artifact.py": (
        "tests/artifacts/test_env_guard_artifact_bytes.py",
    ),
    "scripts/ensure_env.py": ("tests/invariance/test_determinism_env_helper.py",),
    "scripts/probe_internal_version.py": (
        "tests/transport/test_internal_version_contract.py",
    ),
    "scripts/release_id_tools.py": (
        "tests/scripts/test_release_id_recompute.py",
    ),
}
_PRODUCT_TEST_OWNER_PREFIXES = (
    ("catalog/narratives/", _NARRATIVE_TEST_OWNERS),
    ("engine/narratives/", _NARRATIVE_TEST_OWNERS),
    ("engine/db/", ("tests/db",)),
    ("engine/order/", ("tests/order", "tests/mech/test_order_properties.py")),
    ("engine/serializer/", ("tests/cli/test_serializer_guards.py",)),
    ("migrations/", ("tests/db",)),
    ("sql/", ("tests/db",)),
    (
        "schemas/hde_release_attestation",
        (
            "tests/evidence/test_release_attestation.py",
            "tests/evidence/test_release_manifest_content_binding.py",
        ),
    ),
    ("schemas/architecture", ("tests/evidence/test_architecture_snapshot.py",)),
    (
        "schemas/hde_epic038_direct_db_selection",
        ("tests/evidence/test_hde_epic038_direct_db_selection.py",),
    ),
)
_EVIDENCE_GENERATOR_TEST_OWNERS = {
    "tools/evidence/generate_architecture_snapshot.py": (
        "tests/evidence/test_architecture_snapshot.py",
    ),
    "tools/evidence/generate_hde_epic037_v2_adapter.py": (
        "tests/evidence/test_hde_epic037_v2_adapter.py",
    ),
    "tools/evidence/generate_narrative_registry_diff.py": _NARRATIVE_TEST_OWNERS,
}
_EVIDENCE_HELPER_OWNERSHIP_TEST = (
    "tests/evidence/test_evidence_tool_ownership.py"
)
_EVIDENCE_HELPER_TEST_OWNERS = {
    "tools/evidence/build_release_attestation.py": (
        "tests/evidence/test_release_attestation.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/check_d23_evidence_index_snapshot_contract.py": (
        "tests/evidence/test_d23_evidence_index_snapshot_contract.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/check_epic024_acceptance_map_viability.py": (
        "tests/evidence/test_epic024_acceptance_map_viability.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/check_epic024_evidence_path_binding_validation.py": (
        "tests/evidence/test_epic024_evidence_path_binding_validation.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/check_lf_endings.py": (
        "tests/evidence/test_evidence_index_missing_state.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/check_po_006_token_registry_validity.py": (
        "tests/evidence/test_po_006_token_registry_validity.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/epic020_bundle.py": (
        "tests/tools/test_epic020_bundle_tool.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/hde_epic038_ops03.py": (
        "tests/ops/test_hde_epic038_ops03.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/orientation_demo.py": (
        "tests/evidence/test_orientation_demo.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/refresh_epic024_step_logs_manifest.py": (
        "tests/evidence/test_refresh_epic024_step_logs_manifest.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/refresh_step_logs_manifest.py": (
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/regenerate_identity_closure.py": (
        "tests/evidence/test_release_manifest_content_binding.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/retained_evidence_safety.py": (
        "tests/evidence/test_retained_evidence_safety.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/run_canonical_json_gate.py": (
        "tests/evidence/test_canonical_json_gate_check_outputs.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/run_sanity_pipeline.py": (
        "tests/evidence/test_sanity_pipeline.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/run_sanity_pipeline_gate.py": (
        "tests/evidence/test_sanity_pipeline.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/strict_json_schema.py": (
        "tests/ops/test_hde_epic038_ops03.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/update_evidence_index.py": (
        "tests/evidence/test_evidence_index_missing_state.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
    "tools/evidence/validate_evidence_paths.py": (
        "tests/evidence/test_evidence_index_missing_state.py",
        _EVIDENCE_HELPER_OWNERSHIP_TEST,
    ),
}
_EVIDENCE_HELPERS_REQUIRING_OWNER = {
    # These helpers have no safe focused behavioral owner in the ordinary PR
    # environment. Changes fail closed until that ownership is established.
    "tools/evidence/hdapi_v2_boundary_analyzer.py",
    "tools/evidence/run_cli_guardrail.py",
    "tools/evidence/run_env_pins_gate.py",
    "tools/evidence/run_sampler_evidence.py",
    "tools/evidence/run_showcompat_artifacts.py",
}
_QA_TEST_OWNERS = (
    "tests/qa/test_generic_qa_harness.py",
    "tests/qa/test_qa_harness_followup.py",
    "tests/qa/test_epic021_harness_entrypoint.py",
    "tests/qa/test_epic021_acceptance_alignment.py",
    "tests/qa/test_tooling_bootstrap.py",
    "tests/qa/test_viability_generator_wrappers.py",
    "tests/qa/test_epic029_requalification.py",
)
_QA_TOOL_OWNERSHIP_TEST = "tests/qa/test_qa_tool_ownership.py"
_QA_TOOL_TEST_OWNERS = {
    "tools/qa/__init__.py": (_QA_TOOL_OWNERSHIP_TEST,),
    "tools/qa/epic021_qa.py": (
        "tests/qa/test_epic021_harness_entrypoint.py",
        "tests/qa/test_epic021_acceptance_alignment.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/examples/__init__.py": (_QA_TOOL_OWNERSHIP_TEST,),
    "tools/qa/examples/d13_refactored_example.py": (_QA_TOOL_OWNERSHIP_TEST,),
    "tools/qa/generate_epic027_close_pack.py": (
        "tests/qa/test_qa_harness_followup.py",
        "tests/qa/test_viability_generator_wrappers.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/generate_epic028_acceptance_ledger.py": (
        "tests/qa/test_viability_generator_wrappers.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/generate_epic028_close_pack.py": (
        "tests/qa/test_viability_generator_wrappers.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/generate_epic029_close_pack.py": (
        "tests/qa/test_viability_generator_wrappers.py",
        "tests/qa/test_epic029_requalification.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/qa_harness.py": _QA_TEST_OWNERS + (_QA_TOOL_OWNERSHIP_TEST,),
    "tools/qa/refresh_epic024_step_logs_manifest.py": (
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/run_hde_epic024_harness.py": (
        "tests/qa/test_epic024_bootstrap_status.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
    "tools/qa/step_log_header.py": (_QA_TOOL_OWNERSHIP_TEST,),
    "tools/qa/token_roster_validate.py": (
        "tests/qa/test_epic023_acceptance_alignment.py",
        _QA_TOOL_OWNERSHIP_TEST,
    ),
}
_QA_TOOLS_REQUIRING_OWNER = {
    # These source-writing administrative close-pack generators have no
    # continuing executable consumer or focused regression owner.  Changes
    # remain deliberately fail-closed until that ownership is established.
    "tools/qa/generate_epic025_close_pack.py",
    "tools/qa/generate_epic026_close_pack.py",
}
_SAFE_TEST_SUPPORT_PREFIXES = {
    "tests/db/": ("tests/db",),
    "tests/order/": ("tests/order",),
    "tests/qa/": _QA_TEST_OWNERS,
}
_FIXED_LANE_TEST_DIRECTORIES = {
    "tests/db": "db",
    "tests/order": "product",
}
_FIXED_LANE_TEST_PROVIDERS = {
    **{path: "compat" for path in (
        "tests/adapter/test_compat_http_dev.py",
        "tests/adapter/test_compat_http_parity.py",
        "tests/adapter/test_jsonschema.py",
        "tests/cli/test_cli_canonical_bytes.py",
        "tests/cli/test_cli_usage_and_errors.py",
        "tests/cli/test_errors_parity.py",
        "tests/cli/test_serializer_guards.py",
        "tests/cli/test_showcompat_parity_and_identity.py",
        "tests/http/test_compat_endpoint_contract.py",
        "tests/transport/test_internal_version_contract.py",
    )},
    **{path: "db" for path in (
        "tests/bodygraph/test_bg_resolve_v2_mapped_cache.py",
        "tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py",
        "tests/bodygraph/test_ingest.py",
        "tests/ops/test_capture_rails_open_scope.py",
        "tests/ops/test_http_logging.py",
        "tests/unit/test_check_direct_db_contract.py",
    )},
    "tests/evidence/test_architecture_snapshot.py": "product",
    "tests/mech/test_order_properties.py": "product",
    "tests/evidence/test_rails_ci_workflow_integration.py": "rails",
    **{path: "evidence" for path in (
        "tests/evidence/test_evidence_index_missing_state.py",
        "tests/evidence/test_evidence_skeleton.py",
        "tests/evidence/test_machine_mirror_self_proof.py",
        "tests/evidence/test_orientation_demo.py",
        "tests/ops/test_evidence_index.py",
        "tests/qa/test_epic020_qa_docs.py",
    )},
    **{path: "qa" for path in _QA_TEST_OWNERS},
    **{path: "release" for path in (
        "tests/evidence/test_release_attestation.py",
        "tests/evidence/test_release_manifest_content_binding.py",
        "tests/evidence/test_sanity_pipeline.py",
        "tests/runtime/test_identity.py",
    )},
}
_UNKNOWN_SOURCE_SUFFIXES = {".py", ".sh", ".sql"}


@dataclass(frozen=True)
class Classification:
    flags: dict[str, bool]
    reason: str
    path_count: int
    test_targets: tuple[str, ...] = ()


def _full(reason: str, path_count: int) -> Classification:
    flags = {lane: True for lane in LANES}
    flags["needs_python"] = True
    return Classification(
        flags=flags,
        reason=reason,
        path_count=path_count,
        test_targets=tuple(sorted(_FULL_VALIDATION_SUPPLEMENTAL_TESTS)),
    )


def _empty_flags() -> dict[str, bool]:
    flags = {lane: False for lane in LANES}
    flags["needs_python"] = False
    return flags


def _normalized_path(raw: str) -> str:
    if not raw or "\x00" in raw or "\n" in raw or "\r" in raw:
        raise ValueError("changed path is empty or contains a control character")
    path = PurePosixPath(raw)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("changed path is not repository-relative")
    normalized = path.as_posix()
    if normalized in {"", "."}:
        raise ValueError("changed path is empty")
    return normalized


def _load_governed_primary_paths(repo_root: Path) -> frozenset[str]:
    """Load current Human Index paths for change-aware evidence selection.

    A governed primary can live under an otherwise documentation-only prefix.
    Reading the candidate's committed Human Index keeps that boundary durable
    without turning every ordinary document into evidence work.
    """
    index_path = repo_root / "docs/evidence/INDEX.json"
    if not index_path.exists():
        return frozenset()
    if index_path.is_symlink() or not index_path.is_file():
        raise ValueError("CI_GOVERNED_INDEX_INVALID")
    try:
        payload = json.loads(index_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise ValueError("CI_GOVERNED_INDEX_INVALID") from exc
    if not isinstance(payload, list):
        raise ValueError("CI_GOVERNED_INDEX_INVALID")

    paths: set[str] = set()
    for entry in payload:
        if not isinstance(entry, dict):
            raise ValueError("CI_GOVERNED_INDEX_INVALID")
        raw = entry.get("discovered_physical_path")
        if not isinstance(raw, str):
            raise ValueError("CI_GOVERNED_INDEX_INVALID")
        try:
            paths.add(_normalized_path(raw))
        except ValueError as exc:
            raise ValueError("CI_GOVERNED_INDEX_INVALID") from exc
    return frozenset(paths)


def _is_backup_record(path: str) -> bool:
    return path in _HISTORICAL_BACKUP_PATHS


def _fixed_lane_covers_test_target(source_path: str, target: str) -> bool:
    selected_lanes = _lanes_for_path(source_path)
    if selected_lanes is None:
        return False
    provider = _FIXED_LANE_TEST_PROVIDERS.get(target)
    if provider is None:
        provider = next(
            (
                lane
                for directory, lane in _FIXED_LANE_TEST_DIRECTORIES.items()
                if target == directory or target.startswith(f"{directory}/")
            ),
            None,
        )
    return provider in selected_lanes if provider is not None else False


def _registered_owner_test_paths() -> set[str]:
    paths = set(_FIXED_LANE_TEST_PROVIDERS) | set(
        _FULL_VALIDATION_SUPPLEMENTAL_TESTS
    )
    for targets in _PRODUCT_TEST_OWNER_PATHS.values():
        paths.update(targets)
    for _prefix, targets in _PRODUCT_TEST_OWNER_PREFIXES:
        paths.update(targets)
    for targets in _EVIDENCE_GENERATOR_TEST_OWNERS.values():
        paths.update(targets)
    for targets in _EVIDENCE_HELPER_TEST_OWNERS.values():
        paths.update(targets)
    for targets in _QA_TOOL_TEST_OWNERS.values():
        paths.update(targets)
    return paths


def _validated_owner_targets(
    repo_root: Path,
    source_path: str,
    targets: Iterable[str],
    *,
    error_code: str,
) -> tuple[str, ...]:
    validated: list[str] = []
    for target in targets:
        candidate = repo_root / target
        if not candidate.exists() or candidate.is_symlink():
            raise ValueError(f"{error_code}:{source_path}:{target}")
        if not _fixed_lane_covers_test_target(source_path, target):
            validated.append(target)
    return tuple(validated)


def _is_full_validation_path(path: str) -> bool:
    return path in _FULL_VALIDATION_PATHS or path.startswith(
        _FULL_VALIDATION_PREFIXES
    )


def _full_validation_owner_targets(repo_root: Path, path: str) -> tuple[str, ...]:
    if not _is_full_validation_path(path):
        return ()
    return _validated_owner_targets(
        repo_root,
        path,
        _FULL_VALIDATION_SUPPLEMENTAL_TESTS,
        error_code="CI_FULL_VALIDATION_TEST_INVALID",
    )


def _product_owner_targets(repo_root: Path, path: str) -> tuple[str, ...]:
    """Resolve a bounded behavioral owner or fail until one is registered.

    The repository contains legacy source surfaces whose broad test trees are
    not safe ordinary-PR fallbacks. Their changes intentionally fail with the
    exact unmapped path rather than claiming coverage from an unrelated lane.
    """
    if not path.startswith(_PRODUCT_PREFIXES):
        return ()
    if (
        path.endswith(".path_proof.txt")
        or path.endswith(".REMOVED.md")
        or _is_backup_record(path)
        or path in _RELEASE_IMPLEMENTATION_PATHS
        or path.startswith("schemas/hde_epic038_ops03_")
    ):
        return ()
    targets = _PRODUCT_TEST_OWNER_PATHS.get(path)
    if targets is None:
        targets = next(
            (
                owner_targets
                for prefix, owner_targets in _PRODUCT_TEST_OWNER_PREFIXES
                if path.startswith(prefix)
            ),
            None,
        )
    if targets is None:
        raise ValueError(f"CI_PRODUCT_OWNER_TEST_MISSING:{path}")
    return _validated_owner_targets(
        repo_root,
        path,
        targets,
        error_code="CI_PRODUCT_OWNER_TEST_INVALID",
    )


def _evidence_generator_owner_targets(
    repo_root: Path,
    path: str,
    *,
    changed_paths: set[str] | None = None,
) -> tuple[str, ...]:
    rel = PurePosixPath(path)
    if (
        len(rel.parts) < 3
        or rel.parts[:2] != ("tools", "evidence")
        or rel.suffix.lower() != ".py"
        or not rel.name.lower().startswith("generate_")
    ):
        return ()
    targets = _EVIDENCE_GENERATOR_TEST_OWNERS.get(path)
    if targets is not None:
        return _validated_owner_targets(
            repo_root,
            path,
            targets,
            error_code="CI_EVIDENCE_OWNER_TEST_INVALID",
        )
    if not (repo_root / path).exists() and changed_paths is not None:
        conventional_owner = (
            f"tests/evidence/test_{rel.stem.removeprefix('generate_')}.py"
        )
        if (
            conventional_owner in changed_paths
            and not (repo_root / conventional_owner).exists()
        ):
            # A paired generator/owner removal is an explicit subsystem
            # disposition. Generator-only deletion remains fail-closed.
            return ()
    raise ValueError(f"CI_EVIDENCE_OWNER_TEST_MISSING:{path}")


def _evidence_helper_owner_targets(
    repo_root: Path,
    path: str,
    *,
    changed_paths: set[str] | None = None,
) -> tuple[str, ...]:
    """Resolve non-generator evidence helpers to focused behavioral owners."""
    rel = PurePosixPath(path)
    if (
        len(rel.parts) < 3
        or rel.parts[:2] != ("tools", "evidence")
        or rel.suffix.lower() != ".py"
        or rel.name.lower().startswith("generate_")
    ):
        return ()
    targets = _EVIDENCE_HELPER_TEST_OWNERS.get(path)
    if targets is not None:
        return _validated_owner_targets(
            repo_root,
            path,
            targets,
            error_code="CI_EVIDENCE_HELPER_OWNER_INVALID",
        )
    if not (repo_root / path).exists() and changed_paths is not None:
        owner_stems = {rel.stem}
        if rel.stem.startswith("check_"):
            owner_stems.add(rel.stem.removeprefix("check_"))
        conventional_owners = {
            f"tests/evidence/test_{stem}.py" for stem in owner_stems
        }
        if any(
            owner in changed_paths and not (repo_root / owner).exists()
            for owner in conventional_owners
        ):
            # A paired helper/owner removal is an explicit subsystem
            # disposition. Helper-only deletion remains fail-closed.
            return ()
    raise ValueError(f"CI_EVIDENCE_HELPER_OWNER_MISSING:{path}")


def _qa_tool_owner_targets(repo_root: Path, path: str) -> tuple[str, ...]:
    """Resolve exact behavioral owners for repository QA tooling.

    The fixed QA lane protects the approved generic harness subsystem, while
    older bounded adapters and helpers have their own focused tests.  An
    unregistered Python tool fails classification instead of receiving a green
    conclusion from unrelated QA tests.
    """
    rel = PurePosixPath(path)
    if (
        len(rel.parts) < 3
        or rel.parts[:2] != ("tools", "qa")
        or rel.suffix.lower() != ".py"
    ):
        return ()
    targets = _QA_TOOL_TEST_OWNERS.get(path)
    if targets is None:
        raise ValueError(f"CI_QA_OWNER_TEST_MISSING:{path}")
    return _validated_owner_targets(
        repo_root,
        path,
        targets,
        error_code="CI_QA_OWNER_TEST_INVALID",
    )


def _test_support_owner_targets(repo_root: Path, path: str) -> tuple[str, ...]:
    targets = next(
        (
            owner_targets
            for prefix, owner_targets in _SAFE_TEST_SUPPORT_PREFIXES.items()
            if path.startswith(prefix)
        ),
        None,
    )
    if targets is None:
        raise ValueError(f"CI_TEST_SUPPORT_OWNER_MISSING:{path}")
    return _validated_owner_targets(
        repo_root,
        path,
        targets,
        error_code="CI_TEST_SUPPORT_OWNER_INVALID",
    )


def changed_test_targets(repo_root: Path, paths: Iterable[str]) -> tuple[str, ...]:
    """Return exact changed tests plus repository-owned behavioral owners.

    Product source and evidence-generator changes must execute tests that own
    their behavior, not merely turn on a lane with an unrelated fixed roster.
    Ambiguous test support files use bounded, known-collectable owner suites;
    an unmapped source fails classification rather than reporting false green.
    Removed standalone test modules are not executable at the candidate head.
    """
    targets: set[str] = set()
    normalized_paths = sorted({_normalized_path(raw) for raw in paths})
    changed_paths = set(normalized_paths)
    for path in normalized_paths:
        rel = PurePosixPath(path)
        if path in _FULL_VALIDATION_INACTIVE_TESTS:
            raise ValueError(f"CI_INACTIVE_TEST_REQUIRES_DISPOSITION:{path}")
        if (
            path.endswith(".path_proof.txt")
            or path.endswith(".REMOVED.md")
            or _is_backup_record(path)
        ):
            continue
        if _lanes_for_path(path) == set():
            continue
        targets.update(_full_validation_owner_targets(repo_root, path))
        if rel.parts and rel.parts[0] == "tests":
            candidate = repo_root / path
            is_test_module = rel.suffix == ".py" and rel.name.startswith("test_")
            if (
                is_test_module
                and candidate.exists()
                and candidate.is_file()
                and not candidate.is_symlink()
            ):
                if not _fixed_lane_covers_test_target(path, path):
                    targets.add(path)
                continue
            if is_test_module and not candidate.exists():
                if path in _registered_owner_test_paths():
                    raise ValueError(f"CI_REGISTERED_OWNER_TEST_DELETED:{path}")
                continue
            targets.update(_test_support_owner_targets(repo_root, path))
            continue
        targets.update(_product_owner_targets(repo_root, path))
        targets.update(
            _evidence_generator_owner_targets(
                repo_root,
                path,
                changed_paths=changed_paths,
            )
        )
        targets.update(
            _evidence_helper_owner_targets(
                repo_root,
                path,
                changed_paths=changed_paths,
            )
        )
        targets.update(_qa_tool_owner_targets(repo_root, path))
        if (
            PurePosixPath(path).suffix.lower() in _UNKNOWN_SOURCE_SUFFIXES
            and _lanes_for_path(path) is None
        ):
            raise ValueError(f"CI_SOURCE_OWNER_TEST_MISSING:{path}")
    return tuple(sorted(targets))


def _contains_component(path: str, component: str) -> bool:
    return component in PurePosixPath(path).parts


def _lanes_for_path(path: str) -> set[str] | None:
    """Return known lanes for one path, or ``None`` to fail classification."""
    if _is_full_validation_path(path):
        return set(LANES)

    if path.endswith(".REMOVED.md"):
        return set()

    if _is_backup_record(path):
        return {"evidence"}

    if path.endswith(".path_proof.txt"):
        lanes = {"evidence"}
        if (
            path.startswith(_RELEASE_EVIDENCE_PREFIXES)
            or path.startswith("artifacts/evidence_index")
            or path.startswith("docs/ENDPOINTS_CATALOG.json")
        ):
            lanes.add("release")
        return lanes

    if path.startswith("docs/ENDPOINTS_CATALOG.json"):
        return {"evidence", "release"}

    if path in _RELEASE_IDENTITY_INPUT_PATHS:
        return {"release"}

    schema_lanes = next(
        (lanes for prefix, lanes in _SCHEMA_LANE_PREFIXES if path.startswith(prefix)),
        None,
    )
    if schema_lanes is not None:
        return set(schema_lanes)

    if path.startswith(_DOCUMENTATION_PREFIXES):
        return set()

    historical_namespace = path.startswith(("audit/", "artifacts/", "docs/", "reports/"))
    if path.startswith(_HISTORICAL_PREFIXES) or (
        historical_namespace
        and any(
            _contains_component(path, component)
            for component in ("history", "historical", "runs")
        )
    ):
        return {"evidence"}

    workflow_control_lanes = _WORKFLOW_CONTROL_PATH_LANES.get(path)
    if workflow_control_lanes is not None:
        return set(workflow_control_lanes)

    if path in _RELEASE_IMPLEMENTATION_PATHS:
        return {"evidence", "release"}

    if path in _ARCHITECTURE_ANALYSIS_PATHS:
        return {"evidence", "product"}

    if path.startswith("tools/qa/") or path.startswith("tests/qa/"):
        return {"evidence", "qa"}

    if path.startswith("tests/evidence/"):
        lanes = {"evidence"}
        if "release" in path or "sanity_pipeline" in path:
            lanes.add("release")
        if "rails" in path:
            lanes.add("rails")
        return lanes

    if path.startswith("tools/evidence/"):
        lanes = {"evidence"}
        if any(marker in path for marker in _RAILS_MARKERS):
            lanes.add("rails")
        if path in _RELEASE_IMPLEMENTATION_PATHS or "release" in path:
            lanes.add("release")
        return lanes

    if path.startswith("ci/jobs/"):
        return {"rails", "release"}
    if path.startswith("ci/checks/"):
        if "direct_db" in path:
            return {"db", "product", "release"}
        if any(name in path for name in ("evidence", "mirror", "final_lf")):
            return {"evidence"}
        if "cli" in path:
            return {"compat", "product"}
        if "rails" in path:
            return {"rails"}
        return None

    if path.startswith(("audit/", "artifacts/")):
        lanes = {"evidence"}
        if path.startswith(_RELEASE_EVIDENCE_PREFIXES) or path.startswith(
            ("artifacts/evidence_index",)
        ):
            lanes.add("release")
        return lanes

    if path.startswith("docs/acceptance_map_") and path.endswith(".json"):
        return {"evidence", "release"}
    if path.startswith("docs/evidence/"):
        return {"evidence", "release"}
    if path.startswith("reports/"):
        return {"evidence"}

    if path in _DOCUMENT_PATHS or (
        PurePosixPath(path).suffix.lower() in _DOCUMENT_SUFFIXES
    ):
        return set()

    if path.startswith("tests/"):
        lanes = {"product"}
        if any(marker in f"/{path}" for marker in _COMPAT_MARKERS):
            lanes.add("compat")
        if any(marker in f"/{path}" for marker in _DB_MARKERS):
            lanes.add("db")
        if any(marker in path for marker in _RAILS_MARKERS):
            lanes.add("rails")
        lanes.add("release")
        return lanes

    if path.startswith(_PRODUCT_PREFIXES):
        lanes = {"product", "release"}
        marked_path = f"/{path}"
        if any(marker in marked_path for marker in _COMPAT_MARKERS):
            lanes.add("compat")
        if any(marker in marked_path for marker in _DB_MARKERS):
            lanes.add("db")
        if any(marker in path for marker in _RAILS_MARKERS):
            lanes.add("rails")
        return lanes

    return None


def classify_paths(
    paths: Iterable[str],
    *,
    governed_paths: Iterable[str] | None = None,
) -> Classification:
    normalized = sorted({_normalized_path(path) for path in paths})
    if not normalized:
        return _full("empty_change_set_full_validation", 0)

    governed = (
        _load_governed_primary_paths(ROOT)
        if governed_paths is None
        else frozenset(_normalized_path(path) for path in governed_paths)
    )

    selected: set[str] = set()
    for path in normalized:
        lanes = _lanes_for_path(path)
        if path in governed:
            lanes = set(lanes or ())
            lanes.add("evidence")
        if lanes is None:
            raise ValueError(f"CI_CHANGE_SURFACE_UNCLASSIFIED:{path}")
        selected.update(lanes)

    flags = _empty_flags()
    for lane in selected:
        flags[lane] = True
    flags["needs_python"] = bool(selected)
    reason = "selected_lanes" if selected else "documentation_only"
    return Classification(flags=flags, reason=reason, path_count=len(normalized))


def _validate_sha(raw: str, *, allow_zero: bool = False) -> str:
    value = raw.strip()
    if not SHA_RE.fullmatch(value):
        raise ValueError("Git comparison identity is not a full hexadecimal SHA")
    if not allow_zero and set(value) == {"0"}:
        raise ValueError("Git head identity cannot be all zeroes")
    return value.lower()


def _comparison_base(
    repo_root: Path,
    base: str,
    head: str,
    *,
    event_name: str,
) -> str:
    if event_name == "push":
        return base
    if event_name != "pull_request":
        raise ValueError(f"CI_CHANGE_EVENT_UNSUPPORTED:{event_name}")
    result = subprocess.run(
        ["git", "merge-base", base, head],
        cwd=repo_root,
        check=False,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        raise RuntimeError("CI_CHANGE_MERGE_BASE_UNAVAILABLE")
    try:
        return _validate_sha(result.stdout.strip())
    except ValueError as exc:
        raise RuntimeError("CI_CHANGE_MERGE_BASE_UNAVAILABLE") from exc


def git_changed_paths(repo_root: Path, base: str, head: str) -> tuple[str, ...]:
    result = subprocess.run(
        [
            "git",
            "diff",
            "--name-status",
            "-z",
            "--diff-filter=ACDMRTUXB",
            base,
            head,
            "--",
        ],
        cwd=repo_root,
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git changed-path discovery failed: {message}")
    tokens = [item for item in result.stdout.split(b"\0") if item]
    paths: list[str] = []
    index = 0
    while index < len(tokens):
        try:
            status = tokens[index].decode("ascii")
        except UnicodeDecodeError as exc:
            raise RuntimeError("git changed-path status is not ASCII") from exc
        index += 1
        path_count = 2 if status.startswith(("R", "C")) else 1
        if not status or status[0] not in "ACDMRTUXB" or index + path_count > len(tokens):
            raise RuntimeError("git changed-path output is malformed")
        for raw in tokens[index : index + path_count]:
            paths.append(raw.decode("utf-8"))
        index += path_count
    return tuple(paths)


def classify_git_change(
    repo_root: Path,
    base: str,
    head: str,
    *,
    event_name: str,
) -> Classification:
    base_sha = _validate_sha(base, allow_zero=True)
    head_sha = _validate_sha(head)
    if set(base_sha) == {"0"}:
        raise RuntimeError("CI_CHANGE_BASE_UNAVAILABLE")
    if base_sha == head_sha:
        return _full("identical_refs_full_validation", 0)
    comparison_base = _comparison_base(
        repo_root,
        base_sha,
        head_sha,
        event_name=event_name,
    )
    paths = git_changed_paths(repo_root, comparison_base, head_sha)
    result = classify_paths(
        paths,
        governed_paths=_load_governed_primary_paths(repo_root),
    )
    return Classification(
        flags=result.flags,
        reason=result.reason,
        path_count=result.path_count,
        test_targets=result.test_targets or changed_test_targets(repo_root, paths),
    )


def write_github_output(path: Path, classification: Classification) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8", newline="\n") as stream:
        for name in (*LANES, "needs_python"):
            stream.write(f"{name}={'true' if classification.flags[name] else 'false'}\n")
        stream.write(
            f"changed_tests={'true' if classification.test_targets else 'false'}\n"
        )
        stream.write(f"reason={classification.reason}\n")
        stream.write(f"path_count={classification.path_count}\n")


def write_changed_test_targets(path: Path, targets: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "".join(f"{target}\n" for target in targets)
    path.write_text(body, encoding="utf-8", newline="\n")


def _parse_args(argv: Sequence[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True)
    parser.add_argument("--head", required=True)
    parser.add_argument("--event-name", choices=("pull_request", "push"), required=True)
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument(
        "--github-output",
        type=Path,
        default=Path(os.environ["GITHUB_OUTPUT"]) if os.environ.get("GITHUB_OUTPUT") else None,
    )
    parser.add_argument(
        "--changed-tests-output",
        type=Path,
        default=(
            Path(os.environ["RUNNER_TEMP"]) / "ci-changed-test-targets.txt"
            if os.environ.get("RUNNER_TEMP")
            else None
        ),
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parse_args(argv)
    if args.github_output is None:
        print("CI_CHANGE_CLASSIFIER_GITHUB_OUTPUT_MISSING", file=sys.stderr)
        return 2
    if args.changed_tests_output is None:
        print("CI_CHANGE_CLASSIFIER_CHANGED_TESTS_OUTPUT_MISSING", file=sys.stderr)
        return 2
    try:
        classification = classify_git_change(
            args.repo_root.resolve(),
            args.base,
            args.head,
            event_name=args.event_name,
        )
        write_github_output(args.github_output, classification)
        write_changed_test_targets(
            args.changed_tests_output,
            classification.test_targets,
        )
    except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
        print(f"CI_CHANGE_CLASSIFIER_ERROR:{exc}", file=sys.stderr)
        return 2
    enabled = ",".join(
        lane for lane in LANES if classification.flags[lane]
    ) or "none"
    print(
        "CI_CHANGE_CLASSIFICATION:"
        f"event={args.event_name};reason={classification.reason};"
        f"paths={classification.path_count};lanes={enabled}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
