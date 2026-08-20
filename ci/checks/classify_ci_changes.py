#!/usr/bin/env python3
"""Classify an exact Git change into the smallest safe CI lane set.

The classifier is deliberately repository-owned and fail-safe. Known paths select
only the lanes whose protected inputs they can affect. Unclassified paths and Git
events without a usable comparison base fail explicitly rather than silently
skipping protection.
"""
from __future__ import annotations

import argparse
import ast
import importlib.util
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
_STATIC_STRING_VALUE_LIMIT = 128
_STATIC_STRING_LENGTH_LIMIT = 4096
_STATIC_STRING_EXPRESSION_LIMIT = 2048
_STATIC_ALIAS_ASSIGNMENT_LIMIT = 4096
_STATIC_ALIAS_NODE_LIMIT = 8192

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
_SOURCE_WRITING_INACTIVE_TESTS = frozenset(
    {
        "tests/compliance/test_log_shape_snapshot.py",
        "tests/compliance/test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py",
    }
)
_STALE_BRIDGE_INACTIVE_TESTS = frozenset(
    {
        "tests/adapter/test_headers_and_determinism.py",
        "tests/adapter/test_reader_parity.py",
        "tests/compliance/test_429_retry_after_mapping_seconds_and_date.py",
        "tests/compliance/test_override_guard_engine_env_and_app_env_alias.py",
        "tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py",
        "tests/compliance/test_reader_etag_and_conditional.py",
        "tests/compliance/test_reader_etag_compression_invariance.py",
    }
)
_UNCONFIGURED_INACTIVE_TESTS = (
    _SOURCE_WRITING_INACTIVE_TESTS | _STALE_BRIDGE_INACTIVE_TESTS
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
} | set(_UNCONFIGURED_INACTIVE_TESTS)
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
_DB_AWARE_PRODUCT_PATHS = {"adapter/http_reader.py"}
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
_HTTP_READER_OWNERSHIP_GUARD = "tests/evidence/test_http_reader_ci_ownership.py"
_HTTP_READER_TEST_OWNERS = (
    "tests/adapter/test_compat_http_dev.py",
    "tests/adapter/test_compat_http_parity.py",
    "tests/adapter/test_compat_writer_transport.py",
    "tests/adapter/test_diagnostic_writer.py",
    "tests/adapter/test_dev_sampler_http.py",
    "tests/adapter/test_gate_auth.py",
    "tests/cli/test_aux_preview.py",
    "tests/compat/test_abba_parity.py",
    "tests/compliance/test_logging_filter_keys_only_and_redactions.py",
    "tests/db/test_conn_env_only.py",
    "tests/db/test_no_import_time_connect.py",
    _HTTP_READER_OWNERSHIP_GUARD,
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
_HTTP_READER_INDIRECT_OWNER_BRIDGES = {
    "tests/adapter/test_compat_writer_transport.py": (
        "adapter.app",
        "adapter.wsgi",
        "adapter.http_reader",
    ),
    "tests/adapter/test_dev_sampler_http.py": (
        "adapter.factory",
        "adapter.http_reader",
    ),
    "tests/adapter/test_gate_auth.py": (
        "adapter.app",
        "adapter.wsgi",
        "adapter.http_reader",
    ),
    "tests/compliance/test_logging_filter_keys_only_and_redactions.py": (
        "adapter.wsgi",
        "adapter.http_reader",
    ),
    "tests/http/test_compat_endpoint_contract.py": (
        "adapter.factory",
        "adapter.http_reader",
    ),
    "tests/transport/test_ops_rails_refusal.py": (
        "adapter.wsgi",
        "adapter.http_reader",
    ),
}
_HTTP_READER_INDIRECT_TEST_OWNERS = frozenset(
    _HTTP_READER_INDIRECT_OWNER_BRIDGES
)
_HTTP_READER_BRIDGE_TOPOLOGY = {
    "adapter.app": ("adapter.wsgi", "adapter.http_reader"),
    "adapter.factory": ("adapter.http_reader",),
    "adapter.wsgi": ("adapter.http_reader",),
    "tests._helpers.app_import": ("adapter.wsgi", "adapter.http_reader"),
}
_HTTP_READER_BRIDGE_MODULES = frozenset(_HTTP_READER_BRIDGE_TOPOLOGY)
_HTTP_READER_INDIRECT_NON_OWNERS = frozenset(
    {
        "tests/_helpers/app_import.py",
        "tests/adapter/test_env_guard_import_purity.py",
        "tests/adapter/test_headers_and_determinism.py",
        "tests/adapter/test_jsonschema.py",
        "tests/adapter/test_reader_parity.py",
        "tests/adapter/test_readyz.py",
        "tests/compliance/test_429_retry_after_mapping_seconds_and_date.py",
        "tests/compliance/test_log_shape_snapshot.py",
        "tests/compliance/test_override_guard_engine_env_and_app_env_alias.py",
        "tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py",
        "tests/compliance/test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py",
        "tests/compliance/test_reader_etag_and_conditional.py",
        "tests/compliance/test_reader_etag_compression_invariance.py",
    }
)
_HTTP_READER_DIRECT_NON_OWNER_SHA256 = {
    # This preserved OPS regression wraps the built-in importer to prove a
    # fail-closed source-identity boundary; its indeterminate wrapper is not a
    # Reader consumer.  Exact-byte binding prevents the exception from drifting.
    "tests/ops/test_hde_epic038_ops03.py": (
        "17ae39cd98dcefef701f4de0ea3e3572162d6dca97e9d8db871132c44a4a743f"
    ),
    # This fixed QA-lane module parametrically imports an explicit bounded
    # roster of QA generators.  Its variable dynamic import is deliberately
    # classified fail-closed.  Binding the exception to exact reviewed bytes
    # prevents the path disposition from concealing a later Reader consumer.
    "tests/qa/test_viability_generator_wrappers.py": (
        "c6a0dc4f1f61afd2bc79ca6ecd6b492490d1b14b2321fc3c416b2c62292052eb"
    ),
}
_HTTP_READER_DIRECT_NON_OWNERS = frozenset(
    _HTTP_READER_DIRECT_NON_OWNER_SHA256
)
_HTTP_READER_DISPOSITION_PATHS = frozenset(_HTTP_READER_TEST_OWNERS) | (
    _HTTP_READER_INDIRECT_NON_OWNERS | _HTTP_READER_DIRECT_NON_OWNERS
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
        test_targets=_full_validation_test_targets(),
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


def _fixed_lane_test_provider(target: str) -> str | None:
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
    return provider


def _fixed_lane_covers_test_target(source_path: str, target: str) -> bool:
    selected_lanes = _lanes_for_path(source_path)
    if selected_lanes is None:
        return False
    provider = _fixed_lane_test_provider(target)
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


def _full_validation_test_targets() -> tuple[str, ...]:
    """Return every active registered owner not supplied by a fixed lane.

    The repository's configured pytest roots are intentionally narrower than
    the complete owner registry.  Full-validation inputs therefore run the
    explicit supplement plus every registered owner outside the fixed lanes,
    without rediscovering unsafe legacy tests or duplicating fixed providers.
    """
    return tuple(
        sorted(
            target
            for target in _registered_owner_test_paths()
            if target not in _FULL_VALIDATION_INACTIVE_TESTS
            and _fixed_lane_test_provider(target) is None
        )
    )


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
        _full_validation_test_targets(),
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


def _is_pytest_test_module(path: str | PurePosixPath) -> bool:
    """Return whether a path matches pytest's active module-name policy."""
    name = PurePosixPath(path).name
    return name.endswith(".py") and (
        name.startswith("test_") or name.endswith("_test.py")
    )


def _bounded_static_strings(values: Iterable[str]) -> set[str]:
    bounded: set[str] = set()
    for value in values:
        if len(value) > _STATIC_STRING_LENGTH_LIMIT:
            raise ValueError("CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED")
        bounded.add(value)
        if len(bounded) > _STATIC_STRING_VALUE_LIMIT:
            raise ValueError("CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED")
    return bounded


def _bounded_string_product(left: set[str], right: set[str]) -> set[str]:
    if len(left) * len(right) > _STATIC_STRING_VALUE_LIMIT:
        raise ValueError("CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED")
    return _bounded_static_strings(
        prefix + suffix for prefix in left for suffix in right
    )


def _static_string_values(
    node: ast.expr,
    constants: dict[str, set[str]],
) -> set[str]:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return _bounded_static_strings((node.value,))
    if isinstance(node, ast.Name):
        return set(constants.get(node.id, set()))
    if isinstance(node, ast.NamedExpr):
        return _static_string_values(node.value, constants)
    if isinstance(node, ast.IfExp):
        return _bounded_static_strings(
            _static_string_values(node.body, constants)
            | _static_string_values(node.orelse, constants)
        )
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        left = _static_string_values(node.left, constants)
        right = _static_string_values(node.right, constants)
        return _bounded_string_product(left, right)
    if isinstance(node, ast.JoinedStr):
        parts = {""}
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                values = {value.value}
            elif (
                isinstance(value, ast.FormattedValue)
                and value.format_spec is None
                and value.conversion in {-1, ord("s")}
            ):
                values = _static_string_values(value.value, constants)
            else:
                return set()
            if not values:
                return set()
            parts = _bounded_string_product(parts, values)
        return parts
    return set()


def _static_call_argument_expressions(
    node: ast.Call,
    *,
    position: int,
    keyword: str,
) -> list[ast.expr]:
    values: list[ast.expr] = []
    if len(node.args) > position:
        values.append(node.args[position])
    values.extend(
        item.value for item in node.keywords if item.arg == keyword
    )
    return values


def _static_call_argument_values(
    node: ast.Call,
    *,
    position: int,
    keyword: str,
    constants: dict[str, set[str]],
) -> set[str]:
    return {
        resolved
        for value in _static_call_argument_expressions(
            node, position=position, keyword=keyword
        )
        for resolved in _static_string_values(value, constants)
    }


def _importlib_call_module_names(
    node: ast.Call,
    constants: dict[str, set[str]],
) -> set[str]:
    names = _static_call_argument_values(
        node, position=0, keyword="name", constants=constants
    )
    packages = _static_call_argument_values(
        node, position=1, keyword="package", constants=constants
    )
    resolved: set[str] = set()
    for name in names:
        if not name.startswith("."):
            resolved.add(name)
            continue
        for package in packages:
            try:
                resolved.add(importlib.util.resolve_name(name, package))
            except (ImportError, ValueError):
                continue
    return resolved


def _static_collection_string_values(
    node: ast.expr,
    constants: dict[str, set[str]],
) -> set[str]:
    if isinstance(node, (ast.List, ast.Set, ast.Tuple)):
        return _bounded_static_strings(
            item
            for element in node.elts
            for item in _static_string_values(element, constants)
        )
    return _static_string_values(node, constants)


def _builtin_call_module_names(
    node: ast.Call,
    constants: dict[str, set[str]],
) -> set[str]:
    names = _static_call_argument_values(
        node, position=0, keyword="name", constants=constants
    )
    fromlist = _bounded_static_strings(
        item
        for expression in _static_call_argument_expressions(
            node, position=3, keyword="fromlist"
        )
        for item in _static_collection_string_values(expression, constants)
    )
    resolved = set(names)
    if names and fromlist:
        resolved.update(
            _bounded_string_product(
                _bounded_static_strings(name + "." for name in names),
                {item for item in fromlist if item != "*"},
            )
        )
    return resolved


def _parse_python_source(candidate: Path) -> ast.Module:
    try:
        return ast.parse(candidate.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, SyntaxError) as exc:
        raise ValueError(
            f"CI_HTTP_READER_OWNER_SCAN_INVALID:{candidate.as_posix()}"
        ) from exc


def _import_statement_imports(node: ast.AST, module_name: str) -> bool:
    parent, separator, leaf = module_name.rpartition(".")
    if isinstance(node, ast.Import):
        return any(alias.name == module_name for alias in node.names)
    if not isinstance(node, ast.ImportFrom) or node.level != 0:
        return False
    return node.module == module_name or (
        bool(separator)
        and node.module == parent
        and any(alias.name == leaf for alias in node.names)
    )


def _assignment_names(target: ast.expr) -> set[str]:
    if isinstance(target, ast.Name):
        return {target.id}
    if isinstance(target, (ast.List, ast.Tuple)):
        return {
            name
            for item in target.elts
            for name in _assignment_names(item)
        }
    return set()


def _assignment_bindings(
    target: ast.expr,
    value: ast.expr,
) -> Iterable[tuple[str, ast.expr]]:
    """Yield statically positional name/value bindings for an assignment."""
    if isinstance(target, ast.Name):
        yield target.id, value
        return
    if (
        isinstance(target, (ast.List, ast.Tuple))
        and isinstance(value, (ast.List, ast.Tuple))
        and len(target.elts) == len(value.elts)
    ):
        for child_target, child_value in zip(target.elts, value.elts):
            yield from _assignment_bindings(child_target, child_value)
        return
    if isinstance(target, (ast.List, ast.Tuple)):
        # A non-literal iterable cannot be positionally resolved here.  Bind
        # every target to the RHS as a conservative alias may-flow so a trusted
        # import callable cannot disappear through one unpacking step.
        for name in _assignment_names(target):
            yield name, value


def _module_scope_statements(
    statements: Iterable[ast.stmt],
) -> Iterable[ast.stmt]:
    for statement in statements:
        yield statement
        nested: list[list[ast.stmt]] = []
        if isinstance(statement, (ast.If, ast.For, ast.AsyncFor, ast.While)):
            nested.extend((statement.body, statement.orelse))
        elif isinstance(statement, (ast.With, ast.AsyncWith)):
            nested.append(statement.body)
        elif isinstance(statement, _ast_try_node_types()):
            nested.extend(
                (
                    statement.body,
                    statement.orelse,
                    statement.finalbody,
                    *(handler.body for handler in statement.handlers),
                )
            )
        elif isinstance(statement, ast.Match):
            nested.extend(case.body for case in statement.cases)
        for body in nested:
            yield from _module_scope_statements(body)


def _ast_try_node_types() -> tuple[type[ast.AST], ...]:
    """Return try-node classes without requiring Python 3.11 TryStar."""
    try_star = getattr(ast, "TryStar", None)
    if isinstance(try_star, type):
        return (ast.Try, try_star)
    return (ast.Try,)


def _module_binding_counts(tree: ast.Module) -> dict[str, int]:
    counts: dict[str, int] = {}

    def bind(name: str) -> None:
        counts[name] = counts.get(name, 0) + 1

    for statement in _module_scope_statements(tree.body):
        if isinstance(statement, ast.Import):
            for alias in statement.names:
                bind(alias.asname or alias.name.partition(".")[0])
        elif isinstance(statement, ast.ImportFrom):
            for alias in statement.names:
                if alias.name != "*":
                    bind(alias.asname or alias.name)
        elif isinstance(statement, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            bind(statement.name)
        elif isinstance(statement, ast.Assign):
            for target in statement.targets:
                for name in _assignment_names(target):
                    bind(name)
        elif isinstance(statement, (ast.AnnAssign, ast.AugAssign)):
            for name in _assignment_names(statement.target):
                bind(name)
        elif isinstance(statement, (ast.For, ast.AsyncFor)):
            for name in _assignment_names(statement.target):
                bind(name)
        elif isinstance(statement, (ast.With, ast.AsyncWith)):
            for item in statement.items:
                if item.optional_vars is not None:
                    for name in _assignment_names(item.optional_vars):
                        bind(name)
    return counts


def _module_string_constants(
    tree: ast.Module,
    required_names: set[str],
) -> tuple[dict[str, set[str]], set[str]]:
    expressions: dict[str, list[ast.expr]] = {}
    for statement in ast.walk(tree):
        if isinstance(statement, ast.Assign):
            for target in statement.targets:
                for name, value in _assignment_bindings(
                    target, statement.value
                ):
                    expressions.setdefault(name, []).append(value)
        elif (
            isinstance(statement, ast.AnnAssign)
            and isinstance(statement.target, ast.Name)
            and statement.value is not None
        ):
            expressions.setdefault(statement.target.id, []).append(
                statement.value
            )
        elif (
            isinstance(statement, ast.NamedExpr)
            and isinstance(statement.target, ast.Name)
        ):
            expressions.setdefault(statement.target.id, []).append(
                statement.value
            )
        elif (
            isinstance(statement, ast.AugAssign)
            and isinstance(statement.target, ast.Name)
            and isinstance(statement.op, ast.Add)
        ):
            expressions.setdefault(statement.target.id, []).append(
                ast.BinOp(
                    left=ast.Name(id=statement.target.id, ctx=ast.Load()),
                    op=ast.Add(),
                    right=statement.value,
                )
            )

    selected_names = set(required_names)
    pending = list(required_names)
    while pending:
        name = pending.pop()
        for value in expressions.get(name, ()):
            for child in ast.walk(value):
                if isinstance(child, ast.Name) and child.id not in selected_names:
                    selected_names.add(child.id)
                    pending.append(child.id)
    selected = {
        name: expressions[name]
        for name in selected_names
        if name in expressions
    }

    if sum(len(values) for values in selected.values()) > (
        _STATIC_STRING_EXPRESSION_LIMIT
    ):
        raise ValueError("CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED")

    constants: dict[str, set[str]] = {}
    # A bounded fixed-point handles simple cross-name aliases and repeated
    # assignments while conservatively retaining every statically possible
    # value across scopes.  The expression count, rather than only the number
    # of names, bounds the longest resolvable assignment chain.
    iteration_limit = sum(len(values) for values in selected.values()) + 1
    for _ in range(iteration_limit):
        changed = False
        for name, values in selected.items():
            resolved = _bounded_static_strings(
                item
                for value in values
                for item in _static_string_values(value, constants)
            )
            current = constants.setdefault(name, set())
            additions = resolved - current
            if additions:
                current.update(_bounded_static_strings(additions | current))
                changed = True
        if not changed:
            break
    complete_names: set[str] = set()
    for _ in range(len(selected) + 1):
        additions = {
            name
            for name, values in selected.items()
            if values
            and all(
                _static_string_expression_is_complete(value, complete_names)
                for value in values
            )
        } - complete_names
        if not additions:
            break
        complete_names.update(additions)
    return constants, complete_names


def _static_string_expression_is_complete(
    node: ast.expr,
    complete_names: set[str],
) -> bool:
    if isinstance(node, ast.Constant):
        return isinstance(node.value, str)
    if isinstance(node, ast.Name):
        return node.id in complete_names
    if isinstance(node, ast.NamedExpr):
        return _static_string_expression_is_complete(
            node.value, complete_names
        )
    if isinstance(node, ast.IfExp):
        return _static_string_expression_is_complete(
            node.body, complete_names
        ) and _static_string_expression_is_complete(
            node.orelse, complete_names
        )
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        return _static_string_expression_is_complete(
            node.left, complete_names
        ) and _static_string_expression_is_complete(
            node.right, complete_names
        )
    if isinstance(node, ast.JoinedStr):
        return all(
            (
                isinstance(value, ast.Constant)
                and isinstance(value.value, str)
            )
            or (
                isinstance(value, ast.FormattedValue)
                and value.format_spec is None
                and value.conversion in {-1, ord("s")}
                and _static_string_expression_is_complete(
                    value.value, complete_names
                )
            )
            for value in node.values
        )
    return False


def _static_collection_expression_is_complete(
    node: ast.expr,
    complete_names: set[str],
) -> bool:
    if isinstance(node, (ast.List, ast.Set, ast.Tuple)):
        return all(
            _static_string_expression_is_complete(item, complete_names)
            for item in node.elts
        )
    return _static_string_expression_is_complete(node, complete_names)


def _extend_dynamic_import_aliases(
    tree: ast.Module,
    binding_counts: dict[str, int],
    *,
    importlib_names: set[str],
    import_module_names: set[str],
    builtins_names: set[str],
    builtin_import_names: set[str],
    pytest_names: set[str],
    importorskip_names: set[str],
) -> None:
    raw_assignments: list[tuple[str, ast.expr]] = []
    for statement in ast.walk(tree):
        if isinstance(statement, ast.Assign):
            for target in statement.targets:
                for name, value in _assignment_bindings(
                    target, statement.value
                ):
                    raw_assignments.append((name, value))
        elif (
            isinstance(statement, ast.AnnAssign)
            and isinstance(statement.target, ast.Name)
            and statement.value is not None
        ):
            raw_assignments.append((statement.target.id, statement.value))
        elif (
            isinstance(statement, ast.NamedExpr)
            and isinstance(statement.target, ast.Name)
        ):
            raw_assignments.append((statement.target.id, statement.value))

    if len(raw_assignments) > _STATIC_ALIAS_ASSIGNMENT_LIMIT:
        raise ValueError("CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED")
    assignments: list[tuple[str, tuple[ast.expr, ...]]] = []
    dependents: dict[str, set[int]] = {}
    node_count = 0
    for name, value in raw_assignments:
        candidates = tuple(_possible_alias_values(value))
        node_count += len(candidates)
        if node_count > _STATIC_ALIAS_NODE_LIMIT:
            raise ValueError("CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED")
        index = len(assignments)
        assignments.append((name, candidates))
        for candidate in candidates:
            if isinstance(candidate, ast.Name):
                dependents.setdefault(candidate.id, set()).add(index)

    queue = list(range(len(assignments)))
    queued = set(queue)
    cursor = 0
    while cursor < len(queue):
        index = queue[cursor]
        cursor += 1
        queued.discard(index)
        name, possible_values = assignments[index]
        before = (
            name in importlib_names,
            name in import_module_names,
            name in builtins_names,
            name in builtin_import_names,
            name in pytest_names,
            name in importorskip_names,
        )
        for value in possible_values:
            if isinstance(value, ast.Name):
                if value.id in importlib_names:
                    importlib_names.add(name)
                if value.id in import_module_names:
                    import_module_names.add(name)
                if value.id in builtins_names:
                    builtins_names.add(name)
                if value.id in builtin_import_names or (
                    value.id == "__import__"
                    and binding_counts.get("__import__", 0) == 0
                ):
                    builtin_import_names.add(name)
                if value.id in pytest_names:
                    pytest_names.add(name)
                if value.id in importorskip_names:
                    importorskip_names.add(name)
            elif isinstance(value, ast.Attribute):
                providers = _dynamic_import_provider_kinds(
                    value.value,
                    importlib_names=importlib_names,
                    builtins_names=builtins_names,
                    pytest_names=pytest_names,
                )
                if "importlib" in providers and value.attr == "import_module":
                    import_module_names.add(name)
                if "builtins" in providers and value.attr == "__import__":
                    builtin_import_names.add(name)
                if "pytest" in providers and value.attr == "importorskip":
                    importorskip_names.add(name)
            elif isinstance(value, ast.Call):
                kinds = _dynamic_import_getattr_kinds(
                    value,
                    importlib_names=importlib_names,
                    builtins_names=builtins_names,
                    pytest_names=pytest_names,
                )
                if "importlib" in kinds:
                    import_module_names.add(name)
                if "builtin" in kinds:
                    builtin_import_names.add(name)
                if "pytest" in kinds:
                    importorskip_names.add(name)
        after = (
            name in importlib_names,
            name in import_module_names,
            name in builtins_names,
            name in builtin_import_names,
            name in pytest_names,
            name in importorskip_names,
        )
        if before == after:
            continue
        for dependent in dependents.get(name, ()):
            if dependent not in queued:
                queue.append(dependent)
                queued.add(dependent)


def _possible_alias_values(value: ast.expr) -> Iterable[ast.expr]:
    """Yield expression nodes that may carry a trusted callable alias."""
    yield from (
        node for node in ast.walk(value) if isinstance(node, ast.expr)
    )


def _dynamic_import_provider_kinds(
    value: ast.expr,
    *,
    importlib_names: set[str],
    builtins_names: set[str],
    pytest_names: set[str],
) -> set[str]:
    providers: set[str] = set()
    pending: list[ast.expr] = [value]
    visited = 0
    while pending:
        node = pending.pop()
        visited += 1
        if visited > _STATIC_ALIAS_NODE_LIMIT:
            raise ValueError(
                "CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED"
            )
        if isinstance(node, ast.Name):
            if node.id in importlib_names:
                providers.add("importlib")
            if node.id in builtins_names:
                providers.add("builtins")
            if node.id in pytest_names:
                providers.add("pytest")
        elif isinstance(node, ast.NamedExpr):
            pending.append(node.value)
        elif isinstance(node, ast.IfExp):
            pending.extend((node.body, node.orelse))
        elif isinstance(node, ast.BoolOp):
            pending.extend(node.values)
        elif isinstance(node, ast.Subscript):
            pending.append(node.value)
        elif isinstance(node, (ast.List, ast.Set, ast.Tuple)):
            pending.extend(node.elts)
        elif isinstance(node, ast.Dict):
            pending.extend(node.values)
        elif isinstance(node, ast.Starred):
            pending.append(node.value)
        elif (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "getattr"
            and len(node.args) >= 3
        ):
            # A present default is a possible provider value even when the
            # inspected object and attribute are unrelated.
            pending.append(node.args[2])
    return providers


def _dynamic_import_getattr_kinds(
    function: ast.expr,
    *,
    importlib_names: set[str],
    builtins_names: set[str],
    pytest_names: set[str],
) -> set[str]:
    """Return import-call kinds exposed by a bounded ``getattr`` call.

    A nonliteral attribute on a trusted provider is intentionally treated as
    ambiguous and therefore import-capable.  The surrounding call still has
    to target the governed module (or itself be indeterminate) before the
    ownership guard is selected.
    """
    if not (
        isinstance(function, ast.Call)
        and isinstance(function.func, ast.Name)
        and function.func.id == "getattr"
        and len(function.args) >= 2
    ):
        return set()
    providers = _dynamic_import_provider_kinds(
        function.args[0],
        importlib_names=importlib_names,
        builtins_names=builtins_names,
        pytest_names=pytest_names,
    )
    attribute_node = function.args[1]
    attribute = (
        attribute_node.value
        if isinstance(attribute_node, ast.Constant)
        and isinstance(attribute_node.value, str)
        else None
    )
    kinds: set[str] = set()
    if "importlib" in providers and attribute in {None, "import_module"}:
        kinds.add("importlib")
    if "builtins" in providers and attribute in {None, "__import__"}:
        kinds.add("builtin")
    if "pytest" in providers and attribute in {None, "importorskip"}:
        kinds.add("pytest")
    return kinds


def _dynamic_import_call_kinds(
    function: ast.expr,
    binding_counts: dict[str, int],
    *,
    importlib_names: set[str],
    import_module_names: set[str],
    builtins_names: set[str],
    builtin_import_names: set[str],
    pytest_names: set[str],
    importorskip_names: set[str],
) -> set[str]:
    kinds: set[str] = set()
    pending: list[ast.expr] = [function]
    visited = 0
    while pending:
        node = pending.pop()
        visited += 1
        if visited > _STATIC_ALIAS_NODE_LIMIT:
            raise ValueError(
                "CI_HTTP_READER_STATIC_ANALYSIS_BUDGET_EXCEEDED"
            )
        if isinstance(node, ast.Call):
            kinds.update(
                _dynamic_import_getattr_kinds(
                    node,
                    importlib_names=importlib_names,
                    builtins_names=builtins_names,
                    pytest_names=pytest_names,
                )
            )
            if (
                isinstance(node.func, ast.Name)
                and node.func.id == "getattr"
                and len(node.args) >= 3
            ):
                pending.append(node.args[2])
        elif isinstance(node, ast.Subscript):
            pending.append(node.value)
        elif isinstance(node, (ast.List, ast.Set, ast.Tuple)):
            pending.extend(node.elts)
        elif isinstance(node, ast.Dict):
            pending.extend(node.values)
        elif isinstance(node, ast.NamedExpr):
            pending.append(node.value)
        elif isinstance(node, ast.IfExp):
            pending.extend((node.body, node.orelse))
        elif isinstance(node, ast.BoolOp):
            pending.extend(node.values)
        elif isinstance(node, ast.Starred):
            pending.append(node.value)
        elif isinstance(node, ast.Name):
            if node.id in import_module_names:
                kinds.add("importlib")
            if node.id in builtin_import_names or (
                node.id == "__import__"
                and binding_counts.get("__import__", 0) == 0
            ):
                kinds.add("builtin")
            if node.id in importorskip_names:
                kinds.add("pytest")
        elif isinstance(node, ast.Attribute):
            providers = _dynamic_import_provider_kinds(
                node.value,
                importlib_names=importlib_names,
                builtins_names=builtins_names,
                pytest_names=pytest_names,
            )
            if "importlib" in providers and node.attr == "import_module":
                kinds.add("importlib")
            if "builtins" in providers and node.attr == "__import__":
                kinds.add("builtin")
            if "pytest" in providers and node.attr == "importorskip":
                kinds.add("pytest")
    return kinds


def _dynamic_import_call_is_indeterminate(
    node: ast.Call,
    kind: str,
    constants: dict[str, set[str]],
    complete_names: set[str],
) -> bool:
    if any(keyword.arg is None for keyword in node.keywords):
        return True
    name_expressions = _static_call_argument_expressions(
        node,
        position=0,
        keyword="modname" if kind == "pytest" else "name",
    )
    if not name_expressions:
        return False
    if not all(
        _static_string_expression_is_complete(expression, complete_names)
        for expression in name_expressions
    ):
        return True
    if kind == "importlib":
        names = {
            item
            for expression in name_expressions
            for item in _static_string_values(expression, constants)
        }
        if any(name.startswith(".") for name in names):
            package_expressions = _static_call_argument_expressions(
                node, position=1, keyword="package"
            )
            if not package_expressions:
                # importlib rejects a relative name without a package before
                # importing anything; this is conclusively not a consumer.
                return False
            return not all(
                _static_string_expression_is_complete(
                    expression, complete_names
                )
                for expression in package_expressions
            )
    if kind == "builtin":
        fromlist_expressions = _static_call_argument_expressions(
            node, position=3, keyword="fromlist"
        )
        return bool(fromlist_expressions) and not all(
            _static_collection_expression_is_complete(
                expression, complete_names
            )
            for expression in fromlist_expressions
        )
    return False


def _python_module_statically_imports(
    candidate: Path, module_name: str
) -> bool:
    """Return whether a module has a direct top-level absolute import."""
    tree = _parse_python_source(candidate)
    return any(
        _import_statement_imports(node, module_name) for node in tree.body
    )


def _python_module_imports(candidate: Path, module_name: str) -> bool:
    """Return whether source may import an exact module through known APIs.

    This is deliberately a bounded may-analysis: a recognized import API or
    module-name binding that is also reassigned remains a consumer.  That
    conservative ambiguity policy can over-classify but cannot hide applicable
    Reader protection.
    """
    tree = _parse_python_source(candidate)
    binding_counts = _module_binding_counts(tree)
    importlib_names: set[str] = set()
    import_module_names: set[str] = set()
    builtins_names: set[str] = set()
    builtin_import_names: set[str] = set()
    pytest_names: set[str] = set()
    importorskip_names: set[str] = set()

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if _import_statement_imports(node, module_name):
                    return True
                bound_name = alias.asname or alias.name.partition(".")[0]
                if alias.name == "importlib" or (
                    alias.asname is None
                    and alias.name.startswith("importlib.")
                ):
                    importlib_names.add(
                        bound_name if alias.asname is not None else "importlib"
                    )
                elif alias.name == "builtins":
                    builtins_names.add(bound_name)
                elif alias.name == "pytest" or (
                    alias.asname is None and alias.name.startswith("pytest.")
                ):
                    pytest_names.add(
                        bound_name if alias.asname is not None else "pytest"
                    )
        elif isinstance(node, ast.ImportFrom) and node.level == 0:
            if _import_statement_imports(node, module_name):
                return True
            for alias in node.names:
                bound_name = alias.asname or alias.name
                if node.module == "importlib" and alias.name == "import_module":
                    import_module_names.add(bound_name)
                elif node.module == "builtins" and alias.name == "__import__":
                    builtin_import_names.add(bound_name)
                elif node.module == "pytest" and alias.name == "importorskip":
                    importorskip_names.add(bound_name)

    _extend_dynamic_import_aliases(
        tree,
        binding_counts,
        importlib_names=importlib_names,
        import_module_names=import_module_names,
        builtins_names=builtins_names,
        builtin_import_names=builtin_import_names,
        pytest_names=pytest_names,
        importorskip_names=importorskip_names,
    )

    relevant_calls: list[tuple[ast.Call, str]] = []
    required_names: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        kinds = _dynamic_import_call_kinds(
            node.func,
            binding_counts,
            importlib_names=importlib_names,
            import_module_names=import_module_names,
            builtins_names=builtins_names,
            builtin_import_names=builtin_import_names,
            pytest_names=pytest_names,
            importorskip_names=importorskip_names,
        )
        if not kinds:
            continue
        for kind in sorted(kinds):
            relevant_calls.append((node, kind))
            expressions = _static_call_argument_expressions(
                node,
                position=0,
                keyword="modname" if kind == "pytest" else "name",
            )
            if kind == "importlib":
                expressions.extend(
                    _static_call_argument_expressions(
                        node, position=1, keyword="package"
                    )
                )
            elif kind == "builtin":
                expressions.extend(
                    _static_call_argument_expressions(
                        node, position=3, keyword="fromlist"
                    )
                )
            required_names.update(
                child.id
                for expression in expressions
                for child in ast.walk(expression)
                if isinstance(child, ast.Name)
            )

    if not relevant_calls:
        return False
    constants, complete_names = _module_string_constants(tree, required_names)
    for node, kind in relevant_calls:
        if kind == "importlib":
            argument_names = _importlib_call_module_names(node, constants)
        elif kind == "builtin":
            argument_names = _builtin_call_module_names(node, constants)
        else:
            argument_names = _static_call_argument_values(
                node,
                position=0,
                keyword="modname" if kind == "pytest" else "name",
                constants=constants,
            )
        if module_name in argument_names:
            return True
        if _dynamic_import_call_is_indeterminate(
            node, kind, constants, complete_names
        ):
            return True
    return False


def _test_module_imports_http_reader(candidate: Path) -> bool:
    """Return whether test Python directly imports the HTTP reader."""
    return _python_module_imports(candidate, "adapter.http_reader")


def _test_module_imports_http_reader_bridge(candidate: Path) -> bool:
    """Return whether test Python imports a governed Reader bridge."""
    return any(
        _python_module_imports(candidate, module)
        for module in _HTTP_READER_BRIDGE_MODULES
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
            if candidate.is_symlink():
                raise ValueError(f"CI_TEST_SYMLINK_UNSUPPORTED:{path}")
            is_test_module = _is_pytest_test_module(rel)
            is_regular_python = (
                rel.suffix == ".py"
                and candidate.exists()
                and candidate.is_file()
            )
            imports_http_reader = (
                is_regular_python
                and path != _HTTP_READER_OWNERSHIP_GUARD
                and _test_module_imports_http_reader(candidate)
            )
            imports_http_reader_bridge = (
                is_regular_python
                and path != _HTTP_READER_OWNERSHIP_GUARD
                and _test_module_imports_http_reader_bridge(candidate)
            )
            if path != _HTTP_READER_OWNERSHIP_GUARD and (
                imports_http_reader
                or imports_http_reader_bridge
                or path in _HTTP_READER_DISPOSITION_PATHS
            ):
                targets.update(
                    _validated_owner_targets(
                        repo_root,
                        path,
                        (_HTTP_READER_OWNERSHIP_GUARD,),
                        error_code="CI_HTTP_READER_OWNER_GUARD_INVALID",
                    )
                )
            if (
                is_test_module
                and is_regular_python
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
        if path in _DB_AWARE_PRODUCT_PATHS or any(
            marker in marked_path for marker in _DB_MARKERS
        ):
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
