#!/usr/bin/env python3
"""Generate/check HDE-EPIC038 DEV-01 matrix and doc-delta evidence."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import io
import json
import os
import re
import stat
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.presenter import emitter
from scripts.release_id_recompute import manifest_only_problems

OUTPUT = Path("audit/qa/hde-epic038/token_evidence_matrix.md")
EPIC_ID = "HDE-EPIC038"
CURRENT_POSTURE_PREFIX = "UNCLAIMED: "
FUTURE_CLAIM_PREFIXES = (
    "Future status may become CLAIMED only after ",
    "Future status may become CLAIMED only when ",
)
ROW_CONTRACT_SHA256 = (
    "7749ddc57c5a7e1e8624e193d9219d91b0601af169daac8f4ee34f5d501b1a32"
)
CI_JOB = "test (.github/workflows/ci.yml)"
HUMAN_INDEX_PATH = "docs/evidence/INDEX.json"
HUMAN_INDEX_KEY = "index.human_index"
MACHINE_MIRROR_PATH = "artifacts/evidence_index.jsonl"
MACHINE_MIRROR_KEY = "index.machine_mirror"
EVIDENCE_PATH_VALIDATOR_PATH = "tools/evidence/validate_evidence_paths.py"
MIRROR_SCHEMA_VALIDATOR_PATH = "ci/checks/check_mirror_schema.sh"
EVIDENCE_INDEX_MIRROR_CI_JOB = (
    "test (.github/workflows/ci.yml): "
    "Run python tools/evidence/update_evidence_index.py --check; "
    "Run ci/checks/check_mirror_schema.sh"
)
EVIDENCE_PATHS_CI_JOB = (
    "test (.github/workflows/ci.yml): Validate governed evidence paths"
)
EVIDENCE_PATH_PROOFS_CI_JOB = (
    "test (.github/workflows/ci.yml): Run ci/checks/check_mirror_schema.sh"
)
RELEASE_CI_JOB = (
    "test (.github/workflows/ci.yml): Verify immutable release input without "
    "derived-tree writes; Run HDE-EPIC038 DEV-01 focused tests; "
    "python -m pytest tests/evidence tests/ops/test_evidence_index.py "
    "tests/ops/test_hde_epic038_ops03.py; "
    "sanity-pipeline (.github/workflows/ci.yml): "
    "Build PR-06R-B release attestation outside the source tree; "
    "Run canonical JSON gate (closed rails); "
    "Publish exact-head release attestation"
)
FINAL_LF_CI_JOB = (
    "test (.github/workflows/ci.yml): Run ci/checks/check_final_lf.sh"
)
PLANNED_COMMANDS = (
    "python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized; "
    "python tools/evidence/generate_hde_epic038_closeout.py --check; "
    "python -m pytest -q tests/evidence/test_hde_epic038_closeout.py"
)
PLANNED_CI_BINDING = f"{CI_JOB}; planned commands: {PLANNED_COMMANDS}"
PLAN_CLOSEOUT_WRITE_COMMAND = (
    "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC "
    "python tools/evidence/generate_hde_epic038_closeout.py"
)
PLAN_CLOSEOUT_CHECK_COMMAND = f"{PLAN_CLOSEOUT_WRITE_COMMAND} --check"
PLAN_CLOSEOUT_PREFLIGHT_COMMAND = f"{PLAN_CLOSEOUT_WRITE_COMMAND} --preflight"
PLAN_CURRENT_STATE_COMMAND = (
    "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC "
    "python tools/evidence/check_hde_epic038_qa_current_state.py "
    "--require-finalized"
)
PLAN_FOCUSED_TEST_COMMAND = (
    "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC "
    "python -m pytest -q tests/evidence/test_hde_epic038_closeout.py"
)
PRIVATE_CI_ROOT_ENV = "_HDE_EPIC038_PRIVATE_CI_ROOT"
PRIVATE_CI_ARTIFACT_ID_ENV = "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID"
PRIVATE_CI_ARTIFACT_DIGEST_ENV = "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST"
PRIVATE_CI_CONTRACT = "hde-epic038-private-ci-execution-receipt"
PRIVATE_CI_REPOSITORY = "amthorn78/glow-hdengine-v2"
PRIVATE_CI_REPOSITORY_ID = 1063073682
PRIVATE_CI_WORKFLOW_PATH = ".github/workflows/ci.yml"
PRIVATE_CI_JOB = "test"
PRIVATE_CI_RECEIPT_NAME = "execution-receipt.json"
PRIVATE_CI_ATTESTATION_DIR = "release-attestation"
PRIVATE_CI_ARTIFACT_PREFIX = "hde-epic038-execution-receipt"
PRIVATE_CI_API_ORIGIN = "https://api.github.com"
PRIVATE_CI_API_VERSION = "2022-11-28"
PRIVATE_CI_ARCHIVE_LIMIT = 16 * 1024 * 1024
PRIVATE_CI_ARCHIVE_ENTRY_LIMIT = 256
PRIVATE_CI_ARCHIVE_FILE_LIMIT = 4 * 1024 * 1024
PRIVATE_CI_ARCHIVE_TOTAL_LIMIT = 12 * 1024 * 1024
PRIVATE_CI_ATTESTATION_PASS_DETAIL = (
    "private external exact-source release attestation validates"
)
PRIVATE_CI_RECEIPT_PASS_DETAIL = (
    "private external exact-command CI receipt validates"
)
PRIVATE_CI_INVALID_DETAIL = (
    "private exact-source attestation and exact-command CI receipt do not "
    "jointly validate"
)
PRIVATE_CI_EXECUTION_RAILS: Mapping[str, str] = {
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
PRIVATE_CI_COMMANDS = (
    PLAN_CURRENT_STATE_COMMAND,
    PLAN_CLOSEOUT_PREFLIGHT_COMMAND,
    PLAN_CLOSEOUT_WRITE_COMMAND,
    PLAN_CLOSEOUT_CHECK_COMMAND,
    PLAN_FOCUSED_TEST_COMMAND,
)
PRIVATE_CI_CONTROL_PLANE_WRITE_COMMAND = PLAN_CLOSEOUT_WRITE_COMMAND.replace(
    "ALLOW_NETWORK=0", "ALLOW_NETWORK=1"
)
PRIVATE_CI_CONTROL_PLANE_CHECK_COMMAND = PLAN_CLOSEOUT_CHECK_COMMAND.replace(
    "ALLOW_NETWORK=0", "ALLOW_NETWORK=1"
)
TOKENS = (
    "TESTS_PASS_OK", "DOC_DELTA_PRESENT_OK", "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK", "EVIDENCE_INDEX_HASH_OK",
    "QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK",
    "ENV_RAILS_POLICY_OK", "PREIMAGE_RECOMPUTE_OK", "CLI_READER_PARITY_OK",
    "COMPOSITE_ABBA_IDENTITY_OK", "TWO_RUN_IDENTITY_OK", "JSON_CANONICAL_CHECK_OK",
    "A7_GET_QUOTED_ETAG_OK", "A7_HEAD_PARITY_OK", "A7_304_OMITS_CT_CL_OK",
    "A7_VARY_AUTH_AE_OK", "A7_ENCODING_INVARIANCE_OK", "A7_TRANSPORT_PROOF_OK",
    "ENDPOINTS_CATALOG_OK", "ENDPOINTS_CATALOG_ENV_GATE_OK", "ENV_LC_ALL_C_OK",
    "EVIDENCE_INDEX_MIRROR_OK", "EVIDENCE_PATHS_VALIDATED_OK",
    "DB_RUNTIME_SEARCH_PATH_OK", "DB_ROLE_OK", "DB_SCHEMA_FINGERPRINT_OK",
    "DB_CONN_ENV_OK", "EVIDENCE_PATH_PROOFS_OK", "CI_CHECK_MIRROR_SCHEMA_OK",
    "CI_CHECK_FINAL_LF_OK", "NO_EXTERNAL_IO_ON_REFUSAL_OK",
    "RELEASE_ID_RECOMPUTE_OK",
)
PROHIBITED = frozenset({
    "DEV_DB_BRIDGE_FALLBACK_OK", "BG_SOURCE_SELECTION_OK",
    "BG_VENDOR_CALLS_DISABLED_IN_PROD_OK", "BG_SOURCE_INVARIANCE_OK",
    "BG_TTL_SWR_POLICY_OK", "BG_RATE_LIMIT_POLICY_OK",
    "BG_CIRCUIT_BREAKER_POLICY_OK", "ENV_SNAPSHOT_SINGLETON_OK",
    "ENV_SNAPSHOT_SCHEMA_V3_OK", "ENV_PINS_PRESENT_OK",
})
# Independent review allowlist for the exact nonclaiming prose pair on each row.
# This mapping is intentionally not derived from build_rows(): generator prose
# cannot redefine its own accepted baseline.
NONCLAIMING_TEXT_SHA256: Mapping[str, str] = {
    "TESTS_PASS_OK": "f895c4d36bffea6a1e5740efeeef85389f581041a63c89fa92686884388ccb63",
    "DOC_DELTA_PRESENT_OK": "71ae70bd1df89a4c8a38413cc436ac4e39fb087eade6f846abee044cc12e2e50",
    "EVIDENCE_INDEX_UPDATED_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "MACHINE_MIRROR_UPDATED_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "EVIDENCE_INDEX_HASH_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "QA_PRECOMMIT_CHECKLIST_OK": "2d4d18c138e01d3616df8ab01d5009d9a30b76aff5d6335eed1c193338678426",
    "QA_POSTCOMMIT_CHECKLIST_OK": "e36486d4c1b7d35f3d2904d4c082955e11c44ab5972cd58fb552056638d16ebd",
    "ENV_RAILS_POLICY_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "PREIMAGE_RECOMPUTE_OK": "a82f1ccfa039a408ac8d3b84f46eb7d850f554dbf49b938056cafaa22fa3472d",
    "CLI_READER_PARITY_OK": "c19b41956747816771a6ec95fc95c070a2e4e2c9d8afd4e8241ba6855c921682",
    "COMPOSITE_ABBA_IDENTITY_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "TWO_RUN_IDENTITY_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "JSON_CANONICAL_CHECK_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "A7_GET_QUOTED_ETAG_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "A7_HEAD_PARITY_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "A7_304_OMITS_CT_CL_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "A7_VARY_AUTH_AE_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "A7_ENCODING_INVARIANCE_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "A7_TRANSPORT_PROOF_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "ENDPOINTS_CATALOG_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "ENDPOINTS_CATALOG_ENV_GATE_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "ENV_LC_ALL_C_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "EVIDENCE_INDEX_MIRROR_OK": "70d309c2037a02bf786fed90bb380d629444fc8ee42ffbb2ad5a5c2c98d988e3",
    "EVIDENCE_PATHS_VALIDATED_OK": "e584407305119230e7f869263ea9453540d3f892ed45d81407e04c4133f82402",
    "DB_RUNTIME_SEARCH_PATH_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "DB_ROLE_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "DB_SCHEMA_FINGERPRINT_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "DB_CONN_ENV_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "EVIDENCE_PATH_PROOFS_OK": "1fa9682d8c7391fce99ab778733bb707e0a1564d97a7eaa240cd20a559359ee2",
    "CI_CHECK_MIRROR_SCHEMA_OK": "7029081103413c34b0df96d0fcad69542faa4fb76a02eef8af430dcc6775cff3",
    "CI_CHECK_FINAL_LF_OK": "9ec6f302f7624cad060ea1699e5a699f99638324423508379939581a55bd4b52",
    "NO_EXTERNAL_IO_ON_REFUSAL_OK": "973ea977d8666b0acdfe96f78b443dcd6426f62d021441a92c78a479ab0d3a9f",
    "RELEASE_ID_RECOMPUTE_OK": "f44e5bc7fffa26a946bf62d9fc1e004ff6594295a921258ebf353efd5b0f8e0a",
}
PLANNED_BINDINGS: Mapping[str, tuple[str, str, str]] = {
    "TESTS_PASS_OK": (
        "audit/EPIC-038_close_report.md",
        "epic038.close_report",
        "DEV-03",
    ),
    "QA_PRECOMMIT_CHECKLIST_OK": (
        "audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log",
        "epic038.qa_precommit_checklist",
        "DEV-03",
    ),
    "QA_POSTCOMMIT_CHECKLIST_OK": (
        "audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log",
        "epic038.qa_postcommit_checklist",
        "DEV-03",
    ),
}
PLANNED_PATHS = frozenset(
    path
    for primary, _key, _owner in PLANNED_BINDINGS.values()
    for path in (primary, f"{primary}.path_proof.txt")
)
PLANNED_KEYS = frozenset(key for _path, key, _owner in PLANNED_BINDINGS.values())
DB_POSTURE_PATH = "audit/ops/hde-epic038/ops-03/db_posture_summary.json"
DB_POSTURE_KEY = "epic038.ops03.db_posture_summary"
REFUSAL_PATH = "artifacts/bodygraph/v2_mapped_cache/closed_rails_refusal.log"
REFUSAL_KEY = "epic038.pr05.v2_mapped_cache.closed_rails_refusal"
REFUSAL_MANIFEST_PATH = "artifacts/bodygraph/v2_mapped_cache/manifest.json"
REFUSAL_MANIFEST_KEY = "epic038.pr05.v2_mapped_cache.manifest"
RELEASE_MANIFEST_PATH = "catalog/manifest.json"
RELEASE_MANIFEST_KEY = "epic038.release.catalog_manifest"
RELEASE_ID_PATH = "artifacts/identity/release_id.json"
RELEASE_ID_KEY = "epic038.pr01.identity_release_id"
RELEASE_RECOMPUTE_PATH = "artifacts/identity/release_id_recompute.log"
RELEASE_RECOMPUTE_KEY = "epic038.pr01.identity_release_id_recompute"
RELEASE_ATTESTATION_RAILS: Mapping[str, str] = {
    "ALLOW_NETWORK": "0",
    "LANG": "C",
    "LC_ALL": "C",
    "PIP_NO_INDEX": "1",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
DOC_DELTA_PRIMARY_PATH = "audit/docdeltas/hde-epic038_doc_deltas.md"
DOC_DELTA_PRIMARY_KEY = "epic038.doc_deltas"
DOC_DELTA_CAPTURE_PATH = "audit/qa/hde-epic038/00_meta/doc_deltas.md"
DOC_DELTA_CAPTURE_KEY = "epic038.qa_meta_doc_deltas"
DOC_DELTA_HISTORICAL_CHECK_ID = "qa-00-step-0-discovery"
DOC_DELTA_HISTORICAL_LOG_PATH = (
    "audit/qa/hde-epic038/checks/qa-00-step-0-discovery/primary.log"
)
DOC_DELTA_HISTORICAL_LOG_SHA256 = (
    "db9e7ac48e168f7fac380f294271110bbf5e88b0874a1e6d5591cb868d6eecbe"
)
DOC_DELTA_HISTORICAL_LOG_SIZE_BYTES = 8248
DOC_DELTA_HISTORICAL_PAIR_SHA256 = (
    "7372dcd1d04e7762a0b826d505c43530578e654bd9fc7a51db5a217685d4bdde"
)
DOC_DELTA_CURRENT_PAIR_SHA256 = (
    "322db8191bcadf82df5231697d32b66d615e7a9ed88813c596c887d31ae55c4a"
)
DOC_DELTA_WRITE_COMMAND = (
    "python tools/evidence/generate_hde_epic038_closeout.py --doc-deltas"
)
DOC_DELTA_CHECK_COMMAND = (
    "python tools/evidence/generate_hde_epic038_closeout.py --check-doc-deltas"
)
DOC_DELTA_CI_JOB = (
    "test (.github/workflows/ci.yml): Check HDE-EPIC038 DEV-01 doc-delta pair"
)
DEV_REQUIREMENTS_SHA256 = (
    "2e286c3451a45472dd54ef356895110f6ec320ebe19d488b6348572c3863e04e"
)
QA_MANIFEST_PATH = "audit/qa/hde-epic038/qa_step_logs_manifest.json"
QA_MANIFEST_KEY = "epic038.qa_step_logs_manifest"
PREIMAGE_PATH = "audit/gates/parity/reader_cli/summary.json"
PREIMAGE_KEY = "epic038.pr02.reader_cli_summary"
PREIMAGE_SOURCE_PATH = "audit/gates/parity/reader_cli/ab.json"
PREIMAGE_SOURCE_KEY = "epic038.pr02.reader_cli_ab"
FINAL_LF_CHECK_ID = "qa-19-po-019"
FINAL_LF_LOG_PATH = (
    "audit/qa/hde-epic038/checks/qa-19-po-019/primary.log"
)
EVIDENCE_INTEGRITY_CHECK_ID = "qa-19-po-019"
EVIDENCE_INTEGRITY_LOG_PATH = FINAL_LF_LOG_PATH
QA19_HEADER_COMMAND_SHA256 = (
    "242f24210d3058ca48775c8492a95103968987e60ddede5ba11936156cb9eda8"
)
QA19_BEHAVIOR_COMMAND = (
    "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC "
    "python tools/evidence/update_evidence_index.py --check && "
    "python tools/evidence/validate_evidence_paths.py && "
    "python ci/checks/check_mirror_schema.sh && "
    "bash ci/checks/check_evidence_index_hash.sh && "
    "python tools/evidence/orientation_demo.py --check && "
    "bash ci/checks/check_final_lf.sh"
)
QA19_HEADER_FIELDS = frozenset(
    {
        "captured_env",
        "check_id",
        "check_name",
        "claimed_tokens",
        "command",
        "command_provenance",
        "evidence_artifacts",
        "exit_code",
        "fail_status",
        "intended_tokens",
        "pf_refs",
        "schema_version",
        "status",
        "timestamp_utc",
    }
)
FINAL_LF_SCRIPT_PATH = "ci/checks/check_final_lf.sh"
FINAL_LF_REQUIRED_PATHS = (
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.sha256",
    "artifacts/evidence_index.jsonl",
    "docs/evidence/INDEX.json.path_proof.txt",
    "docs/evidence/INDEX.sha256.path_proof.txt",
    "artifacts/evidence_index.jsonl.path_proof.txt",
    "artifacts/evidence_index.jsonl.sha256",
    "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
    "audit/gates/topology/orientation_demo.txt",
    "audit/gates/topology/orientation_demo.txt.path_proof.txt",
    "artifacts/runtime/env_matrix.snapshot.json",
    "artifacts/runtime/env_matrix.snapshot.json.path_proof.txt",
    "audit/qa/hde-epic038/token_evidence_matrix.md",
    "audit/qa/hde-epic038/token_evidence_matrix.md.path_proof.txt",
)
FINAL_LF_PLANNED_PATHS = (
    "audit/EPIC-038_close_report.md",
    "audit/EPIC-038_close_report.md.path_proof.txt",
    "audit/EPIC-038_MANIFEST.json",
    "audit/EPIC-038_MANIFEST.json.path_proof.txt",
    "docs/acceptance_map_epic038.json",
    "docs/acceptance_map_epic038.json.path_proof.txt",
    "audit/qa/hde-epic038/acceptance_map_viability.log",
    "audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt",
    "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
    "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt",
)


@dataclass(frozen=True)
class Row:
    token: str
    acceptance_token: str
    manifest_token: str
    test_binding: str
    ci_binding: str
    live_qa: str
    primary_evidence: tuple[str, ...]
    artifact_keys: tuple[str, ...]
    epic_id: str
    proof_anchors: tuple[str, ...]
    posture: str
    classification: str
    owner_task: str
    future_claim: str


def _row(token: str, test: str, qa: str, path: str, key: str) -> Row:
    return Row(
        token,
        token,
        token,
        test,
        CI_JOB,
        qa,
        (path,),
        (key,),
        EPIC_ID,
        (path + ".path_proof.txt",),
        (
            "UNCLAIMED: retained evidence is a binding candidate only; "
            "presence or historical PASS text is not acceptance."
        ),
        "existing/reused",
        "N/A: existing/reused evidence",
        (
            "Future status may become CLAIMED only after exact-head closed-rails "
            "execution, finalized acceptance-map and manifest derivation, and "
            "independent Gate B PASS."
        ),
    )


def _hex64(value: object) -> bool:
    return (
        isinstance(value, str)
        and len(value) == 64
        and all(character in "0123456789abcdef" for character in value)
    )


def _unique_json_object(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def validate_release_identity_family(
    manifest_bytes: bytes | None = None,
    release_payload: Mapping[str, object] | None = None,
    release_bytes: bytes | None = None,
    recompute_text: str | None = None,
) -> tuple[str, str]:
    raw = (
        (ROOT / RELEASE_MANIFEST_PATH).read_bytes()
        if manifest_bytes is None
        else manifest_bytes
    )
    try:
        manifest = json.loads(raw)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("release manifest JSON mismatch") from exc
    canonical = (
        json.dumps(manifest, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode("utf-8")
    if raw != canonical:
        raise ValueError("release manifest is not canonical")
    manifest_sha256 = hashlib.sha256(raw).hexdigest()

    if release_payload is not None and release_bytes is not None:
        raise ValueError("release identity JSON binding mismatch")
    if release_payload is None:
        raw_release = (
            (ROOT / RELEASE_ID_PATH).read_bytes()
            if release_bytes is None
            else release_bytes
        )
        try:
            loaded = json.loads(
                raw_release,
                object_pairs_hook=_unique_json_object,
            )
        except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
            raise ValueError("release identity JSON binding mismatch") from exc
        if not isinstance(loaded, dict):
            raise ValueError("release identity JSON shape mismatch")
        canonical_release = (
            json.dumps(
                loaded,
                ensure_ascii=False,
                separators=(",", ":"),
                sort_keys=True,
            )
            + "\n"
        ).encode("utf-8")
        if raw_release != canonical_release:
            raise ValueError("release identity JSON binding mismatch")
        release_payload = loaded
    required_release = {
        "manifest_path",
        "manifest_sha256",
        "release_id",
        "release_id_algorithm",
    }
    captured_release_id = release_payload.get("release_id")
    if (
        set(release_payload) != required_release
        or release_payload.get("manifest_path") != RELEASE_MANIFEST_PATH
        or release_payload.get("manifest_sha256") != captured_release_id
        or not _hex64(captured_release_id)
        or release_payload.get("release_id_algorithm")
        != "sha256(canonical_bytes(catalog/manifest.json))"
    ):
        raise ValueError("release identity JSON binding mismatch")

    text = (
        (ROOT / RELEASE_RECOMPUTE_PATH).read_text(encoding="utf-8")
        if recompute_text is None
        else recompute_text
    )
    lines = text.splitlines()
    if not lines or lines[0] != "identity_release_id_recompute":
        raise ValueError("release recomputation log shape mismatch")
    field_lines = [line for line in lines[1:] if line]
    if len(field_lines) != 3 or any("=" not in line for line in field_lines):
        raise ValueError("release recomputation log shape mismatch")
    pairs = [line.split("=", 1) for line in field_lines]
    if len({key for key, _value in pairs}) != len(pairs):
        raise ValueError("release recomputation log shape mismatch")
    fields = dict(pairs)
    if (
        set(fields) != {"manifest_sha256", "release_id", "status"}
        or fields.get("manifest_sha256") != captured_release_id
        or fields.get("release_id") != captured_release_id
        or fields.get("status") != "PASS"
    ):
        raise ValueError("release recomputation log binding mismatch")
    return manifest_sha256, str(captured_release_id)


def _doc_delta_required_nonempty_lines() -> tuple[str, ...]:
    return (
        "# HDE-EPIC038 QA Doc Deltas",
        "## SURFACE BINDING",
        (
            "- Draft/staging surface (primary token-evidence binding): "
            f"`{DOC_DELTA_PRIMARY_PATH}`"
        ),
        (
            "- Epic-scoped capture surface (stable QA record): "
            f"`{DOC_DELTA_CAPTURE_PATH}`"
        ),
        "## BLOCKERS",
        "- None identified by Step-0 route discovery.",
        "## CAVEATS",
        (
            "- DOC-CAVEAT-001: Implementation, repository, release, and "
            "operational evidence do not independently establish Live QA "
            "acceptance or epic closeout."
        ),
    )


def render_doc_delta_pair() -> bytes:
    """Render the exact current PF04/r7-compatible two-surface bytes."""
    required = _doc_delta_required_nonempty_lines()
    data = (
        "\n".join(
            (
                required[0],
                "",
                *required[1:4],
                "",
                *required[4:6],
                "",
                *required[6:],
                "",
            )
        )
    ).encode("utf-8")
    if hashlib.sha256(data).hexdigest() != DOC_DELTA_CURRENT_PAIR_SHA256:
        raise ValueError("doc-delta current renderer contract drift")
    return data


def render_historical_doc_delta_pair() -> bytes:
    """Render only the immutable body created by the retained Step-0 log."""
    data = (
        "# HDE-EPIC038 QA Doc Deltas\n"
        "\n"
        "## BLOCKERS\n"
        "- None identified by Step-0 route discovery.\n"
        "\n"
        "## CAVEATS\n"
        "- DOC-CAVEAT-001: Implementation, repository, release, and "
        "operational evidence do not independently establish Live QA "
        "acceptance or epic closeout.\n"
    ).encode("utf-8")
    if hashlib.sha256(data).hexdigest() != DOC_DELTA_HISTORICAL_PAIR_SHA256:
        raise ValueError("doc-delta historical renderer contract drift")
    return data


def validate_doc_delta_semantics(data: bytes, *, surface: str) -> str:
    """Validate PF04/PF27 roles and content without consulting the peer."""
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"doc-delta {surface} semantic contract mismatch") from exc
    # Split only on the canonical ASCII LF. str.splitlines() would silently
    # normalize VT, FF, and Unicode line separators into accepted structure.
    nonempty_lines = tuple(line for line in text.split("\n") if line)
    if (
        not data
        or data.startswith(b"\xef\xbb\xbf")
        or b"\r" in data
        or not data.endswith(b"\n")
        or nonempty_lines != _doc_delta_required_nonempty_lines()
    ):
        raise ValueError(f"doc-delta {surface} semantic contract mismatch")
    return text


def validate_doc_delta_surface(data: bytes, *, surface: str) -> None:
    """Validate one surface's semantics and exact canonical layout."""
    validate_doc_delta_semantics(data, surface=surface)
    if data != render_doc_delta_pair():
        raise ValueError(f"doc-delta {surface} canonical layout mismatch")


def validate_doc_delta_pair_identity(primary: bytes, capture: bytes) -> None:
    """Apply r7/PF19 equality only after independent PF04 role checks."""
    if primary != capture:
        raise ValueError("doc-delta QA-plan pair identity mismatch")


def _stage_atomic_bytes(target: Path, data: bytes, mode: int) -> Path:
    """Stage bytes beside ``target`` so the final replace stays on one FS."""
    target.parent.mkdir(parents=True, exist_ok=True)
    staged = target.with_name(f".{target.name}.hde-epic038.tmp")
    stream = staged.open("xb")
    try:
        with stream:
            stream.write(data)
            stream.flush()
        staged.chmod(mode)
        return staged
    except BaseException:
        staged.unlink(missing_ok=True)
        raise


def write_doc_delta_pair() -> None:
    """Write the pair transactionally; restore both originals on failure."""
    validate_doc_delta_historical_origin()
    data = render_doc_delta_pair()
    targets = tuple(
        ROOT / path
        for path in (DOC_DELTA_PRIMARY_PATH, DOC_DELTA_CAPTURE_PATH)
    )
    originals: dict[Path, tuple[bytes | None, int]] = {}
    staged: dict[Path, Path] = {}
    committed: list[Path] = []
    for target in targets:
        exists = target.is_file()
        originals[target] = (
            target.read_bytes() if exists else None,
            target.stat().st_mode & 0o777 if exists else 0o644,
        )
    try:
        for target in targets:
            staged[target] = _stage_atomic_bytes(
                target,
                data,
                originals[target][1],
            )
        for target in targets:
            staged[target].replace(target)
            committed.append(target)
        if any(target.read_bytes() != data for target in targets):
            raise ValueError("doc-delta deterministic write verification failed")
    except BaseException as exc:
        rollback_errors: list[OSError] = []
        for target in reversed(committed):
            original, mode = originals[target]
            try:
                if original is None:
                    target.unlink(missing_ok=True)
                else:
                    rollback = _stage_atomic_bytes(target, original, mode)
                    try:
                        rollback.replace(target)
                    finally:
                        rollback.unlink(missing_ok=True)
            except OSError as rollback_exc:
                rollback_errors.append(rollback_exc)
        if rollback_errors:
            raise RuntimeError(
                "doc-delta write failed and original-pair rollback failed"
            ) from exc
        raise
    finally:
        for path in staged.values():
            path.unlink(missing_ok=True)


def check_doc_delta_pair() -> None:
    """Read-only exact-byte check for the current deterministic pair."""
    expected = render_doc_delta_pair()
    for path in (DOC_DELTA_PRIMARY_PATH, DOC_DELTA_CAPTURE_PATH):
        target = ROOT / path
        actual = target.read_bytes() if target.is_file() else b""
        if actual != expected:
            raise ValueError(f"doc-delta current producer drift: {path}")


def validate_doc_delta_ci(workflow_text: str | None = None) -> None:
    """Require one unsuppressed read-only check in the exact ``test`` job."""
    requirements_path = ROOT / "requirements-dev.txt"
    if (
        requirements_path.is_symlink()
        or not requirements_path.is_file()
        or hashlib.sha256(requirements_path.read_bytes()).hexdigest()
        != DEV_REQUIREMENTS_SHA256
    ):
        raise ValueError("doc-delta CI command binding mismatch")
    text = (
        (ROOT / ".github/workflows/ci.yml").read_text(encoding="utf-8")
        if workflow_text is None
        else workflow_text
    )
    raw_lines = tuple(text.splitlines())
    lines = tuple(line.strip() for line in raw_lines)
    direct_workflow_lines = tuple(
        line
        for line in raw_lines
        if line and not line[0].isspace() and not line.lstrip().startswith("#")
    )
    expected_direct_workflow_lines = (
        "name: ci",
        "on: [push, pull_request]",
        "jobs:",
    )
    direct_job_headers = tuple(
        line
        for line in raw_lines
        if line.startswith("  ")
        and not line.startswith("   ")
        and line[2:].strip()
        and not line[2:].lstrip().startswith("#")
    )
    expected_direct_job_headers = (
        "  test:",
        "  compat-conj-pr01-closure:",
        "  epic020:",
        "  compat-http-epic020:",
        "  epic020-evidence-bundles:",
        "  rails-policy-gates:",
        "  sanity-pipeline:",
    )
    generator_invocations = tuple(
        line for line in lines if "generate_hde_epic038_closeout" in line
    )
    expected_invocations = (
        f"run: {DOC_DELTA_CHECK_COMMAND}",
        "run: python tools/evidence/generate_hde_epic038_closeout.py "
        "--check-token-matrix",
        PLAN_CLOSEOUT_PREFLIGHT_COMMAND,
        PLAN_CLOSEOUT_WRITE_COMMAND,
        PLAN_CLOSEOUT_CHECK_COMMAND,
        (
            '_HDE_EPIC038_PRIVATE_CI_ROOT="$receipt_root" python -c '
            "'from tools.evidence import generate_hde_epic038_closeout as "
            "closeout; closeout._write_private_ci_receipt()'"
        ),
        PRIVATE_CI_CONTROL_PLANE_WRITE_COMMAND,
        PRIVATE_CI_CONTROL_PLANE_CHECK_COMMAND,
    )
    job_starts = tuple(
        index for index, line in enumerate(raw_lines) if line == "  test:"
    )
    job_start = job_starts[0] if len(job_starts) == 1 else -1
    job_end = (
        next(
            (
                index
                for index in range(job_start + 1, len(raw_lines))
                if raw_lines[index].startswith("  ")
                and not raw_lines[index].startswith("    ")
                and raw_lines[index].rstrip().endswith(":")
            ),
            len(raw_lines),
        )
        if job_start >= 0
        else -1
    )
    job_block = raw_lines[job_start:job_end] if job_start >= 0 else ()
    direct_job_lines = tuple(
        line
        for line in job_block[1:]
        if line.startswith("    ")
        and not line.startswith("     ")
        and line[4:].strip()
        and not line[4:].lstrip().startswith("#")
    )
    direct_job_keys = tuple(
        "".join(
            char
            for char in line[4:].split(":", 1)[0]
            if char not in " \t'\""
        ).lower()
        for line in direct_job_lines
    )
    expected_direct_job_keys = ("needs", "runs-on", "permissions", "env", "steps")
    expected_test_job_prefix = (
        "  test:",
        "    needs:",
        "      - compat-conj-pr01-closure",
        "      - epic020",
        "      - compat-http-epic020",
        "      - epic020-evidence-bundles",
        "      - rails-policy-gates",
        "      - sanity-pipeline",
        "    runs-on: ubuntu-latest",
        "    permissions:",
        "      actions: read",
        "      contents: read",
    )
    expected_env_block = (
        "      LC_ALL: C",
        "      LANG: C",
        "      TZ: UTC",
        '      SAFE_MODE: "1"',
        '      ALLOW_NETWORK: "0"',
        "      APP_ENV: dev",
        '      PYTHONDONTWRITEBYTECODE: "1"',
    )
    steps_starts = tuple(
        index for index, line in enumerate(raw_lines) if line == "    steps:"
    )
    test_steps_starts = tuple(
        index for index in steps_starts if job_start < index < job_end
    )
    env_starts = tuple(
        index for index, line in enumerate(raw_lines) if line == "    env:"
    )
    test_env_starts = tuple(
        index for index in env_starts if job_start < index < job_end
    )
    env_block: tuple[str, ...] = ()
    if len(test_env_starts) == 1 and len(test_steps_starts) == 1:
        env_block = tuple(
            line
            for line in raw_lines[test_env_starts[0] + 1 : test_steps_starts[0]]
            if line.strip() and not line.lstrip().startswith("#")
        )
    step_name = "      - name: Check HDE-EPIC038 DEV-01 doc-delta pair"
    step_starts = tuple(
        index for index, line in enumerate(raw_lines) if line == step_name
    )
    step_block: tuple[str, ...] = ()
    if len(step_starts) == 1:
        start = step_starts[0]
        end = next(
            (
                index
                for index in range(start + 1, len(raw_lines))
                if raw_lines[index].startswith("      - ")
            ),
            len(raw_lines),
        )
        step_block = raw_lines[start:end]
    expected_step_block = (
        step_name,
        "        shell: bash",
        f"        run: {DOC_DELTA_CHECK_COMMAND}",
    )
    expected_check_prefix = (
        "      - uses: actions/checkout@v4",
        "        with:",
        "          fetch-depth: 0",
        "          ref: ${{ github.event.pull_request.head.sha || github.sha }}",
        "      - uses: actions/setup-python@v5",
        "        with:",
        "          python-version: '3.12'",
        "      - name: Download exact-head release attestation",
        "        uses: actions/download-artifact@v4",
        "        with:",
        "          name: hde-release-attestation-${{ github.event.pull_request.head.sha || github.sha }}",
        "          path: ${{ runner.temp }}/hde-epic038-private-receipt/release-attestation",
        *expected_step_block,
        "      - name: Run HDE-EPIC038 DEV-01 focused tests",
        "        shell: bash",
        "        run: |",
        "          set -euo pipefail",
        "          python -m pip install -r requirements-dev.txt",
        "          python -m pip install -r requirements.txt",
        "          python -m pytest --version",
        "          python -m pytest -q tests/evidence/test_hde_epic038_closeout.py",
        "      - name: Verify downloaded exact-source release attestation",
        "        shell: bash",
        "        run: |",
        "          set -euo pipefail",
        '          chmod 700 "$RUNNER_TEMP/hde-epic038-private-receipt"',
        (
            "          python tools/evidence/build_release_attestation.py --verify "
            '"$RUNNER_TEMP/hde-epic038-private-receipt/release-attestation" '
            "--require-clean"
        ),
        "      - run: python -m pip install -U pip",
    )
    check_prefix: tuple[str, ...] = ()
    if len(test_steps_starts) == 1 and len(step_starts) == 1:
        prefix_start = test_steps_starts[0] + 1
        check_prefix = raw_lines[
            prefix_start : prefix_start + len(expected_check_prefix)
        ]
    closeout_step_name = (
        "      - name: Produce conditional private HDE-EPIC038 execution receipt"
    )
    closeout_step_starts = tuple(
        index for index, line in enumerate(raw_lines) if line == closeout_step_name
    )
    closeout_step_block: tuple[str, ...] = ()
    if len(closeout_step_starts) == 1:
        closeout_start = closeout_step_starts[0]
        closeout_end = next(
            (
                index
                for index in range(closeout_start + 1, len(raw_lines))
                if raw_lines[index].startswith("      - ")
            ),
            len(raw_lines),
        )
        closeout_step_block = raw_lines[closeout_start:closeout_end]
    expected_closeout_step_block = (
        closeout_step_name,
        "        id: epic038_receipt",
        "        shell: bash",
        "        run: |",
        "          set -euo pipefail",
        "          primaries=(",
        "            audit/EPIC-038_close_report.md",
        "            audit/EPIC-038_MANIFEST.json",
        "            docs/acceptance_map_epic038.json",
        "            audit/qa/hde-epic038/acceptance_map_viability.log",
        "            audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
        "            audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log",
        "            audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log",
        "          )",
        "          present=0",
        "          missing=()",
        '          for path in "${primaries[@]}"; do',
        '            if [[ -f "$path" ]]; then',
        "              present=$((present + 1))",
        "            else",
        '              missing+=("$path")',
        "            fi",
        "          done",
        "          if (( present == 0 )); then",
        '            echo "HDE-EPIC038 DEV-03 closeout family absent; private execution receipt not applicable."',
        "            python tools/evidence/update_evidence_index.py --check",
        "          elif (( present != ${#primaries[@]} )); then",
        "            printf 'INCOMPLETE_EPIC038_CLOSEOUT_FAMILY:%s\\n' \"$(IFS=,; echo \"${missing[*]}\")\"",
        "            exit 1",
        "          else",
        '            receipt_root="$RUNNER_TEMP/hde-epic038-private-receipt"',
        '            receipt_source="$RUNNER_TEMP/hde-epic038-receipt-source"',
        "            cleanup() {",
        '              git worktree remove --force "$receipt_source" >/dev/null 2>&1 || true',
        "            }",
        "            trap cleanup EXIT",
        '            git worktree add --detach "$receipt_source" "$(git rev-parse HEAD)"',
        "            (",
        '              cd "$receipt_source"',
        "              unset _HDE_EPIC038_PRIVATE_CI_ROOT",
        f"              {PLAN_CURRENT_STATE_COMMAND}",
        f"              {PLAN_CLOSEOUT_PREFLIGHT_COMMAND}",
        f"              {PLAN_CLOSEOUT_WRITE_COMMAND}",
        (
            "              SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C "
            "LANG=C TZ=UTC python tools/evidence/update_evidence_index.py"
        ),
        f"              {PLAN_CLOSEOUT_CHECK_COMMAND}",
        f"              {PLAN_FOCUSED_TEST_COMMAND}",
        "            )",
        (
            '            _HDE_EPIC038_PRIVATE_CI_ROOT="$receipt_root" python -c '
            "'from tools.evidence import generate_hde_epic038_closeout as "
            "closeout; closeout._write_private_ci_receipt()'"
        ),
        "            cleanup",
        "            trap - EXIT",
        '            echo "produced=true" >> "$GITHUB_OUTPUT"',
        "          fi",
    )
    def exact_step_block(step_name: str) -> tuple[tuple[int, ...], tuple[str, ...]]:
        starts = tuple(
            index for index, line in enumerate(raw_lines) if line == step_name
        )
        block: tuple[str, ...] = ()
        if len(starts) == 1:
            start = starts[0]
            end = next(
                (
                    index
                    for index in range(start + 1, len(raw_lines))
                    if raw_lines[index].startswith("      - ")
                    or (
                        raw_lines[index].startswith("  ")
                        and not raw_lines[index].startswith("    ")
                    )
                ),
                len(raw_lines),
            )
            block = raw_lines[start:end]
        return starts, block

    legacy_evidence_step_name = (
        "      - name: Run legacy EPIC020/021 evidence tests in isolated exact-head worktree"
    )
    legacy_evidence_step_starts, legacy_evidence_step_block = exact_step_block(
        legacy_evidence_step_name
    )
    expected_legacy_evidence_step_block = (
        legacy_evidence_step_name,
        "        shell: bash",
        "        run: |",
        "          set -euo pipefail",
        '          legacy_source="$RUNNER_TEMP/hde-legacy-evidence-tests"',
        "          cleanup() {",
        '            git worktree remove --force "$legacy_source" >/dev/null 2>&1 || true',
        "          }",
        "          trap cleanup EXIT",
        '          git worktree add --detach "$legacy_source" "$(git rev-parse HEAD)"',
        "          (",
        '            cd "$legacy_source"',
        (
            "            unset GH_TOKEN _HDE_EPIC038_PRIVATE_CI_ROOT "
            "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID "
            "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST"
        ),
        (
            "            export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 "
            "ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1"
        ),
        '            export PYTHONPATH="$legacy_source"',
        (
            "            EPIC021_QA_RUN_ID=ci-selftest-epic021 python -m pytest "
            "tests/qa/test_epic021_harness_entrypoint.py"
        ),
        (
            "            python -m pytest tests/evidence "
            "tests/ops/test_evidence_index.py tests/ops/test_hde_epic038_ops03.py"
        ),
        "          )",
        "          cleanup",
        "          trap - EXIT",
    )
    receipt_free_step_name = (
        "      - name: Confirm receipt-free exact-head tree is clean"
    )
    receipt_free_step_starts, receipt_free_step_block = exact_step_block(
        receipt_free_step_name
    )
    expected_receipt_free_step_block = (
        receipt_free_step_name,
        "        run: |",
        "          git diff --check",
        "          git diff --exit-code",
    )
    upload_step_name = (
        "      - name: Publish private exact-head HDE-EPIC038 execution receipt"
    )
    upload_step_starts, upload_step_block = exact_step_block(upload_step_name)
    expected_upload_step_block = (
        upload_step_name,
        "        id: epic038_receipt_artifact",
        "        if: steps.epic038_receipt.outputs.produced == 'true'",
        "        uses: actions/upload-artifact@v4",
        "        with:",
        (
            "          name: hde-epic038-execution-receipt-"
            "${{ github.event.pull_request.head.sha || github.sha }}-"
            "${{ github.run_id }}-${{ github.run_attempt }}"
        ),
        "          path: ${{ runner.temp }}/hde-epic038-private-receipt",
        "          if-no-files-found: error",
        "          retention-days: 30",
        "          overwrite: false",
    )
    authenticated_step_name = (
        "      - name: Authenticate and consume private HDE-EPIC038 execution artifact"
    )
    authenticated_step_starts, authenticated_step_block = exact_step_block(
        authenticated_step_name
    )
    expected_authenticated_step_block = (
        authenticated_step_name,
        "        if: steps.epic038_receipt.outputs.produced == 'true'",
        "        shell: bash",
        "        env:",
        "          GH_TOKEN: ${{ github.token }}",
        (
            "          _HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID: "
            "${{ steps.epic038_receipt_artifact.outputs.artifact-id }}"
        ),
        (
            "          _HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST: "
            "${{ steps.epic038_receipt_artifact.outputs.artifact-digest }}"
        ),
        "        run: |",
        "          set -euo pipefail",
        '          authenticated_source="$RUNNER_TEMP/hde-epic038-authenticated-source"',
        "          cleanup() {",
        '            git worktree remove --force "$authenticated_source" >/dev/null 2>&1 || true',
        "          }",
        "          trap cleanup EXIT",
        '          git worktree add --detach "$authenticated_source" "$(git rev-parse HEAD)"',
        "          (",
        '            cd "$authenticated_source"',
        "            unset _HDE_EPIC038_PRIVATE_CI_ROOT",
        f"            {PRIVATE_CI_CONTROL_PLANE_WRITE_COMMAND}",
        "            (",
        (
            "              unset GH_TOKEN _HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID "
            "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST"
        ),
        (
            "              SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C "
            "LANG=C TZ=UTC python tools/evidence/update_evidence_index.py"
        ),
        "            )",
        f"            {PRIVATE_CI_CONTROL_PLANE_CHECK_COMMAND}",
        "            (",
        (
            "              unset GH_TOKEN _HDE_EPIC038_PRIVATE_CI_ARTIFACT_ID "
            "_HDE_EPIC038_PRIVATE_CI_ARTIFACT_DIGEST"
        ),
        (
            "              SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C "
            "LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check"
        ),
        "            )",
        "          )",
        "          cleanup",
        "          trap - EXIT",
    )
    final_step_name = (
        "      - name: Confirm authenticated exact-head receipt fixed point is clean"
    )
    final_step_starts, final_step_block = exact_step_block(final_step_name)
    expected_final_step_block = (
        final_step_name,
        "        run: |",
        "          git diff --check",
        "          git diff --exit-code",
    )
    updater_check_lines = tuple(
        line
        for line in job_block
        if "python tools/evidence/update_evidence_index.py --check" in line
    )
    pre_receipt_updater_checks = tuple(
        line
        for line in raw_lines[job_start : closeout_step_starts[0]]
        if "python tools/evidence/update_evidence_index.py --check" in line
    )
    if (
        step_block != expected_step_block
        or check_prefix != expected_check_prefix
        or direct_workflow_lines != expected_direct_workflow_lines
        or direct_job_headers != expected_direct_job_headers
        or len(job_starts) != 1
        or tuple(job_block[: len(expected_test_job_prefix)])
        != expected_test_job_prefix
        or direct_job_keys != expected_direct_job_keys
        or job_block.count("    needs:") != 1
        or job_block.count("    runs-on: ubuntu-latest") != 1
        or len(test_steps_starts) != 1
        or len(test_env_starts) != 1
        or env_block != expected_env_block
        or not (job_start < step_starts[0] < job_end)
        or step_starts[0] <= test_steps_starts[0]
        or generator_invocations != expected_invocations
        or closeout_step_block != expected_closeout_step_block
        or legacy_evidence_step_block != expected_legacy_evidence_step_block
        or receipt_free_step_block != expected_receipt_free_step_block
        or upload_step_block != expected_upload_step_block
        or authenticated_step_block != expected_authenticated_step_block
        or final_step_block != expected_final_step_block
        or len(updater_check_lines) != 2
        or pre_receipt_updater_checks
        or not (job_start < closeout_step_starts[0] < job_end)
        or not (
            closeout_step_starts[0]
            < legacy_evidence_step_starts[0]
            < receipt_free_step_starts[0]
            < upload_step_starts[0]
            < authenticated_step_starts[0]
            < final_step_starts[0]
            < job_end
        )
        or "--doc-deltas" in text
    ):
        raise ValueError("doc-delta CI command binding mismatch")


def validate_doc_delta_index_bindings(
    human_items: Iterable[Mapping[str, object]] | None = None,
    mirror_items: Iterable[Mapping[str, object]] | None = None,
    bodies: Mapping[str, bytes] | None = None,
) -> None:
    """Bind both doc-delta roles to unique current Index/Mirror records."""
    human = tuple(_human_items() if human_items is None else human_items)
    mirror = tuple(_mirror_items() if mirror_items is None else mirror_items)
    expected = (
        (
            DOC_DELTA_PRIMARY_KEY,
            DOC_DELTA_PRIMARY_PATH,
            f"{DOC_DELTA_PRIMARY_PATH}.path_proof.txt",
            "epic038_doc_delta",
            (
                "Primary draft/staging binding for DOC_DELTA_PRESENT_OK; "
                "governed presence is nonclaiming"
            ),
        ),
        (
            DOC_DELTA_CAPTURE_KEY,
            DOC_DELTA_CAPTURE_PATH,
            f"{DOC_DELTA_CAPTURE_PATH}.path_proof.txt",
            "epic038_doc_delta_capture",
            (
                "Supporting QA capture for the HDE-EPIC038 doc-delta pair; not "
                "the primary token surface and not a token claim"
            ),
        ),
    )
    governed_keys = frozenset(item[0] for item in expected)
    governed_paths = frozenset(item[1] for item in expected)
    governed_targets = {
        path: _resolved_repo_file(path, "doc-delta governed artifact")
        for path in governed_paths
    }
    for surface, items in (("Human Index", human), ("Machine Mirror", mirror)):
        resolved_items = tuple(
            (
                item,
                _resolved_repo_file(
                    _record_text(item, "discovered_physical_path", surface),
                    f"{surface} artifact",
                ),
            )
            for item in items
        )
        family_records = tuple(
            (item, resolved)
            for item, resolved in resolved_items
            if item.get("artifact_key") in governed_keys
            or resolved in governed_targets.values()
        )
        family = tuple(item for item, _resolved in family_records)
        if (
            any("tokens" in item for item in family)
            or any(
                sum(item.get("artifact_key") == key for item in family) != 1
                for key in governed_keys
            )
            or any(
                sum(
                    resolved == target
                    for _item, resolved in family_records
                )
                != 1
                for target in governed_targets.values()
            )
        ):
            raise ValueError("doc-delta Index/Mirror family binding mismatch")
    for key, path, proof, record_type, notes in expected:
        human_matches = [
            item
            for item in human
            if item.get("artifact_key") == key
            and item.get("discovered_physical_path") == path
        ]
        mirror_matches = [
            item
            for item in mirror
            if item.get("artifact_key") == key
            and item.get("discovered_physical_path") == path
        ]
        body = (
            (ROOT / path).read_bytes()
            if bodies is None
            else bodies.get(path, b"")
        )
        if (
            len(human_matches) != 1
            or len(mirror_matches) != 1
            or any(
                item.get("epic_id") != EPIC_ID
                or item.get("record_type") != record_type
                or item.get("schema_version") != "1.0"
                or item.get("notes") != notes
                for item in (*human_matches, *mirror_matches)
            )
            or mirror_matches[0].get("role") != "snapshot"
            or mirror_matches[0].get("proof_anchor") != proof
            or mirror_matches[0].get("sha256")
            != hashlib.sha256(body).hexdigest()
            or mirror_matches[0].get("size_bytes") != len(body)
        ):
            raise ValueError("doc-delta Index/Mirror record binding mismatch")
        _validate_proof(path, proof, body)


def validate_doc_delta_historical_origin(
    qa_manifest: Mapping[str, object] | None = None,
    historical_log: str | None = None,
) -> None:
    """Validate immutable Step-0 discovery, never current-byte production."""
    historical_pair = render_historical_doc_delta_pair()
    if historical_pair == render_doc_delta_pair():
        raise ValueError("doc-delta historical/current provenance collapse")
    manifest = (
        json.loads(
            (ROOT / QA_MANIFEST_PATH).read_bytes(),
            object_pairs_hook=_unique_json_object,
        )
        if qa_manifest is None
        else qa_manifest
    )
    if not isinstance(manifest, Mapping):
        raise ValueError("doc-delta historical manifest binding mismatch")
    record = manifest.get(DOC_DELTA_HISTORICAL_CHECK_ID)
    text = (
        (ROOT / DOC_DELTA_HISTORICAL_LOG_PATH).read_text(encoding="utf-8")
        if historical_log is None
        else historical_log
    )
    log_bytes = text.encode("utf-8")
    if (
        not isinstance(record, dict)
        or record.get("check_id") != DOC_DELTA_HISTORICAL_CHECK_ID
        or record.get("log_path")
        != "checks/qa-00-step-0-discovery/primary.log"
        or record.get("status") != "PASS"
        or record.get("sha256") != DOC_DELTA_HISTORICAL_LOG_SHA256
        or record.get("size_bytes") != DOC_DELTA_HISTORICAL_LOG_SIZE_BYTES
        or record.get("sha256") != hashlib.sha256(log_bytes).hexdigest()
        or record.get("size_bytes") != len(log_bytes)
    ):
        raise ValueError("doc-delta historical manifest binding mismatch")

    lines = text.splitlines()
    try:
        header = json.loads(lines[0], object_pairs_hook=_unique_json_object)
    except (IndexError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("doc-delta historical log shape mismatch") from exc
    results: list[Mapping[str, object]] = []
    for line in lines[1:]:
        try:
            candidate = json.loads(line, object_pairs_hook=_unique_json_object)
        except json.JSONDecodeError:
            continue
        if isinstance(candidate, dict) and "doc_delta_posture" in candidate:
            results.append(candidate)
    if not isinstance(header, dict) or len(results) != 1:
        raise ValueError("doc-delta historical log shape mismatch")
    result = results[0]
    expected_artifacts = [
        DOC_DELTA_HISTORICAL_LOG_PATH,
        DOC_DELTA_PRIMARY_PATH,
        DOC_DELTA_CAPTURE_PATH,
    ]
    command = header.get("command")
    evidence_artifacts = header.get("evidence_artifacts")
    required_receipts = {
        "DEPENDENCY_INITIAL_EXIT_CODE=": "DEPENDENCY_INITIAL_EXIT_CODE=0",
        "DEPENDENCY_FINAL_EXIT_CODE=": "DEPENDENCY_FINAL_EXIT_CODE=0",
        "PATH_PREFLIGHT_EXIT_CODE=": "PATH_PREFLIGHT_EXIT_CODE=0",
        "FINAL_READINESS=": "FINAL_READINESS=READY",
        "BEHAVIOR_EXIT_CODE=": "BEHAVIOR_EXIT_CODE=0",
    }
    historical_literals = tuple(
        line
        for line in historical_pair.decode("utf-8").split("\n")
        if line
    )
    if (
        header.get("check_id") != DOC_DELTA_HISTORICAL_CHECK_ID
        or header.get("status") != "PASS"
        or header.get("exit_code") != 0
        or not isinstance(evidence_artifacts, list)
        or evidence_artifacts != expected_artifacts
        or header.get("intended_tokens") != []
        or header.get("claimed_tokens") != []
        or header.get("captured_env")
        != {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
        }
        or any(
            [line for line in lines if line.startswith(prefix)] != [expected]
            for prefix, expected in required_receipts.items()
        )
        or not isinstance(command, str)
        or DOC_DELTA_PRIMARY_PATH not in command
        or DOC_DELTA_CAPTURE_PATH not in command
        or "DOC_DELTA_PAIR_MISMATCH" not in command
        or any(json.dumps(line) not in command for line in historical_literals)
        or "SURFACE BINDING" in command
        or "--doc-deltas" in command
        or "--check-doc-deltas" in command
        or "generate_hde_epic038_closeout" in command
        or "write_doc_delta_pair" in command
        or set(result)
        != {
            "doc_delta_posture",
            "epic_id",
            "future_check_artifacts",
            "production_factory_missing_routes",
            "production_factory_required_routes",
            "qa_root",
            "repository",
        }
        or result.get("epic_id") != EPIC_ID
        or result.get("doc_delta_posture") != "created"
        or result.get("future_check_artifacts") != "NOT RUN"
        or result.get("production_factory_missing_routes") != []
        or result.get("production_factory_required_routes")
        != [
            ["/api/compat/v1", "POST"],
            ["/internal/version", "GET"],
            ["/reader", "GET"],
        ]
        or result.get("qa_root") != "audit/qa/hde-epic038/"
        or result.get("repository") != "glow-hdengine-v2"
    ):
        raise ValueError("doc-delta historical origin binding mismatch")


def validate_doc_delta_evidence(
    primary_bytes: bytes | None = None,
    capture_bytes: bytes | None = None,
    qa_manifest: Mapping[str, object] | None = None,
    historical_log: str | None = None,
) -> None:
    if (primary_bytes is None) != (capture_bytes is None):
        raise ValueError("doc-delta partial byte injection")
    injected = primary_bytes is not None
    primary = (
        (ROOT / DOC_DELTA_PRIMARY_PATH).read_bytes()
        if primary_bytes is None
        else primary_bytes
    )
    capture = (
        (ROOT / DOC_DELTA_CAPTURE_PATH).read_bytes()
        if capture_bytes is None
        else capture_bytes
    )
    # PF04 role/reference semantics govern first. r7/PF19 byte identity is a
    # separate current-pair predicate, not evidence that historical Step-0
    # produced the normalized bytes.
    validate_doc_delta_surface(primary, surface="staging")
    validate_doc_delta_surface(capture, surface="capture")
    validate_doc_delta_pair_identity(primary, capture)
    validate_doc_delta_historical_origin(qa_manifest, historical_log)
    validate_doc_delta_ci()
    if injected and (
        (ROOT / DOC_DELTA_PRIMARY_PATH).read_bytes() != primary
        or (ROOT / DOC_DELTA_CAPTURE_PATH).read_bytes() != capture
    ):
        raise ValueError("doc-delta injected/disk byte mismatch")

    validate_doc_delta_index_bindings(
        bodies={
            DOC_DELTA_PRIMARY_PATH: primary,
            DOC_DELTA_CAPTURE_PATH: capture,
        }
    )


def _release_row() -> Row:
    manifest_sha256, captured_release_id = validate_release_identity_family()
    row = _row(
        "RELEASE_ID_RECOMPUTE_OK",
        (
            "scripts/release_id_recompute.py; "
            "tools/evidence/generate_identity_provenance.py; "
            "tools/evidence/build_release_attestation.py; "
            "tests/evidence/test_identity_provenance.py; "
            "tests/evidence/test_release_manifest_content_binding.py; "
            "tests/evidence/test_release_attestation.py"
        ),
        "qa-21-po-021",
        RELEASE_MANIFEST_PATH,
        RELEASE_MANIFEST_KEY,
    )
    return replace(
        row,
        ci_binding=RELEASE_CI_JOB,
        primary_evidence=(
            RELEASE_MANIFEST_PATH,
            RELEASE_ID_PATH,
            RELEASE_RECOMPUTE_PATH,
        ),
        artifact_keys=(
            RELEASE_MANIFEST_KEY,
            RELEASE_ID_KEY,
            RELEASE_RECOMPUTE_KEY,
        ),
        proof_anchors=(
            f"{RELEASE_MANIFEST_PATH}.path_proof.txt",
            f"{RELEASE_ID_PATH}.path_proof.txt",
            f"{RELEASE_RECOMPUTE_PATH}.path_proof.txt",
        ),
        posture=(
            "UNCLAIMED: the complete governed release family is bound, but the "
            f"current manifest digest `{manifest_sha256}` differs from retained "
            f"capture digest `{captured_release_id}`; frozen PASS text and artifact "
            "presence do not establish current recomputation."
        ),
        future_claim=(
            "Future status may become CLAIMED only when the canonical manifest, "
            "release-identity JSON, and recomputation log agree on the exact current "
            f"digest `{manifest_sha256}`, the workflow artifact "
            "`hde-release-attestation-${{ github.event.pull_request.head.sha || "
            "github.sha }}/attestation.json` verifies `source_commit_exact=true`, "
            f"`manifest_sha256={manifest_sha256}`, `release_id=manifest_sha256`, "
            "`validation_result=PASS`, `release_admission=PR06R_B_FINAL_PASS`, "
            "`pipeline_stop=null`, closed rails, and independent Gate B PASS "
            "against that same exact head."
        ),
    )


def _doc_delta_row() -> Row:
    row = _row(
        "DOC_DELTA_PRESENT_OK",
        (
            "tools/evidence/generate_hde_epic038_closeout.py; "
            "tests/evidence/test_hde_epic038_closeout.py"
        ),
        DOC_DELTA_HISTORICAL_CHECK_ID,
        DOC_DELTA_PRIMARY_PATH,
        DOC_DELTA_PRIMARY_KEY,
    )
    return replace(
        row,
        ci_binding=DOC_DELTA_CI_JOB,
        posture=(
            "UNCLAIMED: the draft/staging surface is the primary token binding; "
            f"the stable capture `{DOC_DELTA_CAPTURE_PATH}` with key "
            f"`{DOC_DELTA_CAPTURE_KEY}` explicitly names the staging path and "
            "carries its discovered blockers and caveats. The current identical "
            f"pair is deterministic output of `{DOC_DELTA_WRITE_COMMAND}` at "
            f"SHA-256 `{DOC_DELTA_CURRENT_PAIR_SHA256}` and is checked read-only "
            f"by `{DOC_DELTA_CHECK_COMMAND}`. Retained log "
            f"`{DOC_DELTA_HISTORICAL_LOG_PATH}` proves only the original "
            f"{len(render_historical_doc_delta_pair())}-byte Step-0 discovery pair "
            f"at SHA-256 `{DOC_DELTA_HISTORICAL_PAIR_SHA256}`; it did not produce "
            "the current normalized bytes. Refreshed proofs and Index/Mirror rows "
            "bind the current surfaces; none establish acceptance."
        ),
        future_claim=(
            "Future status may become CLAIMED only after the exact-head focused "
            f"`{DOC_DELTA_CHECK_COMMAND}` and focused test independently verify "
            "each governed surface's role, exact staging reference, blockers and "
            "caveats, deterministic current producer bytes, Index/Mirror record, "
            "and proof. The separate r7/PF19 pair-identity predicate must pass "
            "without substituting for PF04 semantics. The hash-bound tokenless "
            f"`{DOC_DELTA_HISTORICAL_CHECK_ID}` record may support only the "
            "unchanged discovery facts, never current-byte production; finalized "
            "acceptance outputs must derive the result and independent Gate B must "
            "record PASS."
        ),
    )


def _checklist_future_claim(path: str, key: str, owner: str) -> str:
    return (
        "Future status may become CLAIMED only after DEV-02 implements "
        "the plan-authorized deterministic default write invocation "
        f"`{PLAN_CLOSEOUT_WRITE_COMMAND}` and read-only check invocation "
        f"`{PLAN_CLOSEOUT_CHECK_COMMAND}`, then "
        f"{owner} produces `{path}`, registers exact key `{key}` and its "
        "updater-owned proof, the planned exact-head `test` job commands "
        "succeed, and independent Gate B records PASS."
    )


def build_rows() -> tuple[Row, ...]:
    default = (
        "tests/evidence/test_hde_epic038_release_sanity.py",
        "qa-20-po-020",
        "audit/qa/hde-epic038/qa_step_logs_manifest.json",
        "epic038.qa_step_logs_manifest",
    )
    rows = {token: _row(token, *default) for token in TOKENS}

    def bind(
        tokens: Iterable[str], test: str, qa: str, path: str, key: str
    ) -> None:
        for token in tokens:
            rows[token] = _row(token, test, qa, path, key)

    bind(
        ("ENV_RAILS_POLICY_OK", "ENV_LC_ALL_C_OK"),
        "tests/invariance/test_determinism_env_helper.py",
        "qa-03-po-003",
        "artifacts/runtime/env_matrix.snapshot.json",
        "epic038.pr01.env_matrix_snapshot_v3",
    )
    rows["PREIMAGE_RECOMPUTE_OK"] = replace(
        _row(
            "PREIMAGE_RECOMPUTE_OK",
            (
                "tests/evidence/test_determinism_gate_proofs.py; "
                "tests/evidence/test_hde_epic038_closeout.py"
            ),
            "qa-04-po-004",
            PREIMAGE_PATH,
            PREIMAGE_KEY,
        ),
        primary_evidence=(PREIMAGE_PATH, PREIMAGE_SOURCE_PATH),
        artifact_keys=(PREIMAGE_KEY, PREIMAGE_SOURCE_KEY),
        proof_anchors=(
            f"{PREIMAGE_PATH}.path_proof.txt",
            f"{PREIMAGE_SOURCE_PATH}.path_proof.txt",
        ),
    )
    rows["PREIMAGE_RECOMPUTE_OK"] = replace(
        rows["PREIMAGE_RECOMPUTE_OK"],
        future_claim=(
            "Future status may become CLAIMED only after "
            "`tools.evidence.run_sanity_pipeline.validate_current_reader_cli_determinism` "
            "recomputes the canonical preimage with `idempotence_hash` removed, "
            "the governed summary records equal 64-hex stored/recomputed hashes "
            "and `preimage_hash_match=true`, the exact-head `test` job succeeds, "
            "and post-generation Gate D derives the result from finalized outputs."
        ),
    )
    bind(
        ("CLI_READER_PARITY_OK",),
        (
            "tests/evidence/test_determinism_gate_proofs.py; "
            "tests/cli/test_showcompat_parity_and_identity.py"
        ),
        "qa-04-po-004",
        "audit/gates/parity/reader_cli/summary.json",
        "epic038.pr02.reader_cli_summary",
    )
    rows["CLI_READER_PARITY_OK"] = replace(
        rows["CLI_READER_PARITY_OK"],
        future_claim=(
            "Future status may become CLAIMED only after the exact-head closed-rails "
            "determinism producer and canonical-output QA check `qa-04-po-004` "
            "re-run the CLI reader-dump/runtime comparison, the governed summary "
            "records equal reader/CLI hashes and `reader_cli_byte_identity=true`, "
            "post-generation Gate D derives the result from finalized outputs, "
            "and independent Gate B passes."
        ),
    )
    bind(
        ("COMPOSITE_ABBA_IDENTITY_OK",),
        "tests/cli/test_showcompat_parity_and_identity.py",
        "qa-04-po-004",
        "audit/gates/determinism/abba.bytes",
        "epic038.pr02.abba_bytes",
    )
    bind(
        ("TWO_RUN_IDENTITY_OK",),
        "tests/cli/test_showcompat_parity_and_identity.py",
        "qa-04-po-004",
        "audit/gates/determinism/tworun_identity.sha256",
        "epic038.pr02.tworun_identity",
    )
    bind(
        ("JSON_CANONICAL_CHECK_OK",),
        "tests/cli/test_cli_canonical_bytes.py",
        "qa-04-po-004",
        "audit/gates/json_gate/canonical/json_gate_structured_record.json",
        "audit.gates.json_gate.canonical.json_gate_structured_record.json",
    )
    a7 = (
        "A7_GET_QUOTED_ETAG_OK",
        "A7_HEAD_PARITY_OK",
        "A7_304_OMITS_CT_CL_OK",
        "A7_VARY_AUTH_AE_OK",
        "A7_ENCODING_INVARIANCE_OK",
        "A7_TRANSPORT_PROOF_OK",
    )
    bind(
        a7,
        "tests/http/test_reader_a7_transport.py",
        "qa-05-po-005",
        "artifacts/proofs/reader_success_get_head_304.json",
        "epic038.pr02.a7_reader_success_composite",
    )
    bind(
        ("ENDPOINTS_CATALOG_OK",),
        "tests/http/test_endpoint_catalog.py",
        "qa-05-po-005",
        "docs/ENDPOINTS_CATALOG.json",
        "epic038.pr02.endpoint_catalog",
    )
    bind(
        ("ENDPOINTS_CATALOG_ENV_GATE_OK",),
        "tests/http/test_endpoint_catalog.py",
        "qa-05-po-005",
        "artifacts/proofs/endpoints_env_gate_proof.log",
        "epic038.pr02.a7_env_gate",
    )
    bind(
        ("EVIDENCE_INDEX_UPDATED_OK",),
        "tests/ops/test_evidence_index.py",
        "qa-19-po-019",
        HUMAN_INDEX_PATH,
        HUMAN_INDEX_KEY,
    )
    bind(
        ("MACHINE_MIRROR_UPDATED_OK", "CI_CHECK_MIRROR_SCHEMA_OK"),
        "tests/ops/test_evidence_index.py",
        "qa-19-po-019",
        MACHINE_MIRROR_PATH,
        MACHINE_MIRROR_KEY,
    )
    index_mirror = _row(
        "EVIDENCE_INDEX_MIRROR_OK",
        (
            "tools/evidence/update_evidence_index.py; "
            "ci/checks/check_mirror_schema.sh; "
            "tests/evidence/test_hde_epic038_closeout.py"
        ),
        EVIDENCE_INTEGRITY_CHECK_ID,
        HUMAN_INDEX_PATH,
        HUMAN_INDEX_KEY,
    )
    rows[index_mirror.token] = replace(
        index_mirror,
        ci_binding=EVIDENCE_INDEX_MIRROR_CI_JOB,
        primary_evidence=(
            HUMAN_INDEX_PATH,
            MACHINE_MIRROR_PATH,
            QA_MANIFEST_PATH,
        ),
        artifact_keys=(
            HUMAN_INDEX_KEY,
            MACHINE_MIRROR_KEY,
            QA_MANIFEST_KEY,
        ),
        proof_anchors=(
            f"{HUMAN_INDEX_PATH}.path_proof.txt",
            f"{MACHINE_MIRROR_PATH}.path_proof.txt",
            f"{QA_MANIFEST_PATH}.path_proof.txt",
        ),
        posture=(
            "UNCLAIMED: the governed Human Index and Machine Mirror currently "
            "have equal ordered artifact-key/path topology, and the QA-19 "
            "manifest hash-binds their closed-rails integrity check; this is "
            "not acceptance."
        ),
        future_claim=(
            "Future status may become CLAIMED only after the exact-head updater "
            "check and Mirror schema workflow steps succeed, whole-surface "
            "Human/Mirror topology remains equal, finalized acceptance outputs "
            "derive the result, and independent Gate B records PASS."
        ),
    )
    paths_validated = _row(
        "EVIDENCE_PATHS_VALIDATED_OK",
        (
            f"{EVIDENCE_PATH_VALIDATOR_PATH}; "
            "tests/evidence/test_hde_epic038_closeout.py"
        ),
        EVIDENCE_INTEGRITY_CHECK_ID,
        MACHINE_MIRROR_PATH,
        MACHINE_MIRROR_KEY,
    )
    rows[paths_validated.token] = replace(
        paths_validated,
        ci_binding=EVIDENCE_PATHS_CI_JOB,
        primary_evidence=(MACHINE_MIRROR_PATH, QA_MANIFEST_PATH),
        artifact_keys=(MACHINE_MIRROR_KEY, QA_MANIFEST_KEY),
        proof_anchors=(
            f"{MACHINE_MIRROR_PATH}.path_proof.txt",
            f"{QA_MANIFEST_PATH}.path_proof.txt",
        ),
        posture=(
            "UNCLAIMED: every current Machine Mirror artifact path resolves "
            "inside the repository, and the QA-19 manifest hash-binds the "
            "closed-rails path-validator run; this is not acceptance."
        ),
        future_claim=(
            "Future status may become CLAIMED only after the exact-head "
            "`Validate governed evidence paths` workflow step validates every "
            "Machine Mirror path, finalized acceptance outputs derive the "
            "result, and independent Gate B records PASS."
        ),
    )
    path_proofs = _row(
        "EVIDENCE_PATH_PROOFS_OK",
        (
            f"{MIRROR_SCHEMA_VALIDATOR_PATH}; "
            "tests/evidence/test_hde_epic038_closeout.py"
        ),
        EVIDENCE_INTEGRITY_CHECK_ID,
        MACHINE_MIRROR_PATH,
        MACHINE_MIRROR_KEY,
    )
    rows[path_proofs.token] = replace(
        path_proofs,
        ci_binding=EVIDENCE_PATH_PROOFS_CI_JOB,
        primary_evidence=(MACHINE_MIRROR_PATH, QA_MANIFEST_PATH),
        artifact_keys=(MACHINE_MIRROR_KEY, QA_MANIFEST_KEY),
        proof_anchors=(
            f"{MACHINE_MIRROR_PATH}.path_proof.txt",
            f"{QA_MANIFEST_PATH}.path_proof.txt",
        ),
        posture=(
            "UNCLAIMED: every current Machine Mirror record and declared proof "
            "anchor has coherent path/hash/size binding, and the QA-19 manifest "
            "hash-binds the closed-rails Mirror schema run; this is not acceptance."
        ),
        future_claim=(
            "Future status may become CLAIMED only after the exact-head Mirror "
            "schema workflow step validates every record and proof anchor, "
            "finalized acceptance outputs derive the result, and independent "
            "Gate B records PASS."
        ),
    )
    bind(
        ("EVIDENCE_INDEX_HASH_OK",),
        "tests/ops/test_evidence_index.py",
        "qa-19-po-019",
        "docs/evidence/INDEX.sha256",
        "docs.evidence.INDEX.sha256",
    )
    bind(
        ("CI_CHECK_FINAL_LF_OK",),
        (
            "ci/checks/check_final_lf.sh; "
            "tests/evidence/test_hde_epic038_closeout.py"
        ),
        FINAL_LF_CHECK_ID,
        QA_MANIFEST_PATH,
        QA_MANIFEST_KEY,
    )
    rows["CI_CHECK_FINAL_LF_OK"] = replace(
        rows["CI_CHECK_FINAL_LF_OK"],
        ci_binding=FINAL_LF_CI_JOB,
        posture=(
            "UNCLAIMED: the governed QA-19 manifest hash-binds a closed-rails "
            "execution log for the repository-wide final-LF gate; historical "
            "PASS text and current file presence are not acceptance."
        ),
        future_claim=(
            "Future status may become CLAIMED only after the exact-head "
            "`Run ci/checks/check_final_lf.sh` workflow step succeeds with the "
            "current matrix and proof plus every present approved planned closeout "
            "output covered, the QA-19 manifest and hash-bound execution log "
            "remain coherent, and independent Gate B records PASS against that "
            "same exact head."
        ),
    )
    bind(
        (
            "DB_RUNTIME_SEARCH_PATH_OK",
            "DB_ROLE_OK",
            "DB_SCHEMA_FINGERPRINT_OK",
        ),
        "tests/ops/test_hde_epic038_ops03.py",
        "qa-22-po-022",
        DB_POSTURE_PATH,
        DB_POSTURE_KEY,
    )
    bind(
        ("DB_CONN_ENV_OK",),
        "tests/db/test_direct_db_pr06r.py",
        "qa-12-po-012",
        "artifacts/runtime/direct_db_selection.snapshot.json",
        "epic038.pr06r.direct_db_selection",
    )

    refusal = _row(
        "NO_EXTERNAL_IO_ON_REFUSAL_OK",
        "tests/evidence/test_v2_mapped_cache_evidence.py",
        "qa-16-po-016",
        REFUSAL_PATH,
        REFUSAL_KEY,
    )
    rows[refusal.token] = replace(
        refusal,
        primary_evidence=(REFUSAL_PATH, REFUSAL_MANIFEST_PATH),
        artifact_keys=(REFUSAL_KEY, REFUSAL_MANIFEST_KEY),
        proof_anchors=(
            f"{REFUSAL_PATH}.path_proof.txt",
            f"{REFUSAL_MANIFEST_PATH}.path_proof.txt",
        ),
        posture=(
            "UNCLAIMED: indexed closed-rails evidence records zero vendor and "
            "database calls and a bound zero-external-I/O predicate; evidence "
            "presence and historical PASS text are not acceptance."
        ),
    )
    rows["RELEASE_ID_RECOMPUTE_OK"] = _release_row()
    rows["DOC_DELTA_PRESENT_OK"] = _doc_delta_row()

    for token, (path, key, owner) in PLANNED_BINDINGS.items():
        row = rows[token]
        rows[token] = replace(
            row,
            test_binding="tests/evidence/test_hde_epic038_closeout.py",
            ci_binding=PLANNED_CI_BINDING,
            live_qa=(
                "N/A: the planned closeout artifact is repository-local DEV "
                "evidence and no Live QA execution is authorized."
            ),
            primary_evidence=(path,),
            artifact_keys=(key,),
            proof_anchors=(f"{path}.path_proof.txt",),
            posture=(
                f"UNCLAIMED: planned-new evidence owned by {owner} does not "
                "exist and has not been executed; DEV-01 makes no token claim."
            ),
            classification="planned-new",
            owner_task=owner,
            future_claim=(
                f"Future status may become CLAIMED only after {owner} canonically "
                f"produces `{path}` and `{path}.path_proof.txt`, registers exact "
                f"artifact key `{key}`, the planned commands execute successfully "
                "on the exact head, and independent Gate B records PASS."
            ),
        )
    for token in ("QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"):
        path, key, owner = PLANNED_BINDINGS[token]
        rows[token] = replace(
            rows[token],
            test_binding=(
                "tools/evidence/generate_hde_epic038_closeout.py; "
                "tests/evidence/test_hde_epic038_closeout.py"
            ),
            future_claim=_checklist_future_claim(path, key, owner),
        )
    return tuple(rows[token] for token in TOKENS)


def _human_items() -> tuple[Mapping[str, object], ...]:
    try:
        payload = json.loads(
            (ROOT / HUMAN_INDEX_PATH).read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
    except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("Human Index shape mismatch") from exc
    if not isinstance(payload, list) or not payload:
        raise ValueError("Human Index shape mismatch")
    if any(not isinstance(item, dict) for item in payload):
        raise ValueError("Human Index record shape mismatch")
    return tuple(payload)


def _mirror_items() -> tuple[Mapping[str, object], ...]:
    items: list[Mapping[str, object]] = []
    for line_number, line in enumerate(
        (ROOT / MACHINE_MIRROR_PATH).read_text(encoding="utf-8").splitlines(),
        1,
    ):
        if not line:
            raise ValueError(f"Machine Mirror empty line: {line_number}")
        try:
            item = json.loads(line, object_pairs_hook=_unique_json_object)
        except (json.JSONDecodeError, ValueError) as exc:
            raise ValueError(
                f"Machine Mirror record shape mismatch: {line_number}"
            ) from exc
        if not isinstance(item, dict):
            raise ValueError(f"Machine Mirror record shape mismatch: {line_number}")
        items.append(item)
    if not items:
        raise ValueError("Machine Mirror shape mismatch")
    return tuple(items)


def _record_text(
    item: Mapping[str, object],
    field: str,
    surface: str,
) -> str:
    value = item.get(field)
    if not isinstance(value, str) or not value:
        raise ValueError(f"{surface} field mismatch: {field}")
    return value


def _mirror_records() -> set[tuple[str, str, str]]:
    return {
        (
            _record_text(item, "artifact_key", "Machine Mirror"),
            _record_text(item, "discovered_physical_path", "Machine Mirror"),
            _record_text(item, "proof_anchor", "Machine Mirror"),
        )
        for item in _mirror_items()
    }


def validate_index_mirror_topology(
    human_items: Iterable[Mapping[str, object]] | None = None,
    mirror_items: Iterable[Mapping[str, object]] | None = None,
) -> None:
    human = tuple(_human_items() if human_items is None else human_items)
    mirror = tuple(_mirror_items() if mirror_items is None else mirror_items)
    if not human or not mirror:
        raise ValueError("evidence index/mirror topology empty")

    def pairs(
        items: tuple[Mapping[str, object], ...],
        surface: str,
    ) -> tuple[tuple[str, str], ...]:
        result = tuple(
            (
                _record_text(item, "artifact_key", surface),
                _record_text(item, "discovered_physical_path", surface),
            )
            for item in items
        )
        if len(result) != len(set(result)):
            raise ValueError(f"evidence index/mirror duplicate pair: {surface}")
        return result

    human_pairs = pairs(human, "Human Index")
    mirror_pairs = pairs(mirror, "Machine Mirror")
    if human_pairs != mirror_pairs:
        raise ValueError("evidence index/mirror topology mismatch")


def _resolved_repo_file(raw_path: str, surface: str) -> Path:
    candidate = Path(raw_path)
    if candidate.is_absolute():
        raise ValueError(f"{surface} absolute path: {raw_path}")
    if ".." in candidate.parts:
        raise ValueError(f"{surface} path traversal: {raw_path}")
    root = ROOT.resolve()
    resolved = (ROOT / candidate).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"{surface} path outside repository: {raw_path}") from exc
    if not resolved.is_file():
        raise ValueError(f"{surface} missing file: {raw_path}")
    return resolved


def validate_mirror_paths(
    records: Iterable[Mapping[str, object]] | None = None,
) -> None:
    items = tuple(_mirror_items() if records is None else records)
    if not items:
        raise ValueError("Machine Mirror path roster empty")
    for item in items:
        path = _record_text(
            item,
            "discovered_physical_path",
            "Machine Mirror",
        )
        _resolved_repo_file(path, "Machine Mirror artifact")


def _mirror_body_sha256() -> str:
    lines = (
        ROOT / MACHINE_MIRROR_PATH
    ).read_text(encoding="utf-8").splitlines(keepends=True)
    body: list[str] = []
    self_count = 0
    for line in lines:
        item = json.loads(line, object_pairs_hook=_unique_json_object)
        if (
            item.get("artifact_key") == MACHINE_MIRROR_KEY
            and item.get("discovered_physical_path") == MACHINE_MIRROR_PATH
        ):
            self_count += 1
        else:
            body.append(line)
    if self_count != 1:
        raise ValueError(f"Machine Mirror self-record count mismatch: {self_count}")
    return hashlib.sha256("".join(body).encode("utf-8")).hexdigest()


def validate_all_mirror_proofs(
    records: Iterable[Mapping[str, object]] | None = None,
) -> None:
    items = tuple(_mirror_items() if records is None else records)
    validate_mirror_paths(items)
    pairs: set[tuple[str, str]] = set()
    self_records = 0
    mirror_body_sha256 = _mirror_body_sha256()
    for item in items:
        key = _record_text(item, "artifact_key", "Machine Mirror")
        primary = _record_text(
            item,
            "discovered_physical_path",
            "Machine Mirror",
        )
        proof = _record_text(item, "proof_anchor", "Machine Mirror")
        pair = (key, primary)
        if pair in pairs:
            raise ValueError(f"Machine Mirror duplicate pair: {key} -> {primary}")
        pairs.add(pair)
        if not proof.endswith(".path_proof.txt"):
            raise ValueError(f"Machine Mirror proof suffix mismatch: {proof}")
        primary_path = _resolved_repo_file(
            primary,
            "Machine Mirror artifact",
        )
        _resolved_repo_file(proof, "Machine Mirror proof")
        _validate_proof(primary, proof)
        body = primary_path.read_bytes()
        expected_sha256 = hashlib.sha256(body).hexdigest()
        if primary == MACHINE_MIRROR_PATH:
            self_records += 1
            expected_sha256 = mirror_body_sha256
            if item.get("role") != "self_record":
                raise ValueError("Machine Mirror self-record role mismatch")
        if (
            item.get("sha256") != expected_sha256
            or item.get("size_bytes") != len(body)
        ):
            raise ValueError(f"Machine Mirror record binding mismatch: {primary}")
    if self_records != 1:
        raise ValueError(
            f"Machine Mirror self-record count mismatch: {self_records}"
        )


def _proof_fields(
    path: Path,
    expected_fields: frozenset[str] | None = None,
) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        if ": " not in line:
            raise ValueError(f"proof field format mismatch: {path}")
        key, value = line.split(": ", 1)
        if not key or not value or key in fields:
            raise ValueError(f"proof field duplicate or empty: {path}: {key}")
        fields[key] = value
    if expected_fields is not None and set(fields) != expected_fields:
        raise ValueError(f"proof field roster mismatch: {path}")
    return fields


def _validate_proof(
    primary: str,
    proof: str,
    primary_bytes: bytes | None = None,
) -> None:
    primary_path = ROOT / primary
    expected_fields = {
        "path",
        "size_bytes",
        "sha256",
        "mtime_utc",
        "produced_at_utc",
    }
    if primary == MACHINE_MIRROR_PATH:
        expected_fields.add("mirror_body_sha256")
    fields = _proof_fields(ROOT / proof, frozenset(expected_fields))
    body = primary_path.read_bytes() if primary_bytes is None else primary_bytes
    if fields.get("path") != primary:
        raise ValueError(f"proof path mismatch: {primary}")
    if fields.get("sha256") != hashlib.sha256(body).hexdigest():
        raise ValueError(f"proof sha mismatch: {primary}")
    if fields.get("size_bytes") != str(len(body)):
        raise ValueError(f"proof size mismatch: {primary}")


def validate_db_posture_payload(token: str, payload: Mapping[str, object]) -> None:
    observations = payload.get("observations")
    predicates = payload.get("predicates")
    if not isinstance(observations, dict) or not isinstance(predicates, dict):
        raise ValueError(f"database posture shape: {token}")
    if token == "DB_RUNTIME_SEARCH_PATH_OK":
        valid = (
            predicates.get("search_path_exact") is True
            and observations.get("search_path") == ["hde", "public"]
        )
    elif token == "DB_ROLE_OK":
        flags = observations.get("runtime_role_flags")
        valid = (
            predicates.get("least_privilege_role") is True
            and isinstance(flags, dict)
            and flags
            and all(value is False for value in flags.values())
        )
    elif token == "DB_SCHEMA_FINGERPRINT_OK":
        identity = observations.get("ddl_identity")
        valid = (
            predicates.get("ddl_identity_valid") is True
            and isinstance(identity, dict)
            and identity.get("schema") == "hde.ddl_identity_projection.v1"
            and isinstance(identity.get("canonical_sha256"), str)
            and len(identity["canonical_sha256"]) == 64
        )
    else:
        raise ValueError(f"unexpected database posture token: {token}")
    if not valid:
        raise ValueError(f"database posture predicate mismatch: {token}")


def validate_no_io_payloads(log_text: str, manifest: Mapping[str, object]) -> None:
    expected_log = (
        "PASS code=PROVIDER_REFUSED safe_mode=1 allow_network=0 "
        "vendor_calls=0 db_calls=0\n"
    )
    if log_text != expected_log:
        raise ValueError("closed-rails refusal counters mismatch")
    predicates = manifest.get("predicates")
    if (
        not isinstance(predicates, dict)
        or predicates.get("closed_rails_zero_io") is not True
    ):
        raise ValueError("closed-rails external I/O predicate mismatch")
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list):
        raise ValueError("closed-rails manifest artifacts missing")
    matches = [
        item
        for item in artifacts
        if isinstance(item, dict) and item.get("path") == REFUSAL_PATH
    ]
    if len(matches) != 1:
        raise ValueError("closed-rails refusal binding missing")
    match = matches[0]
    log_bytes = log_text.encode("utf-8")
    if (
        match.get("sha256") != hashlib.sha256(log_bytes).hexdigest()
        or match.get("size") != len(log_bytes)
    ):
        raise ValueError("closed-rails refusal binding mismatch")


def validate_preimage_payload(
    payload: Mapping[str, object],
    source_bytes: bytes,
) -> None:
    hashes = payload.get("idempotence_hash")
    artifact_hashes = payload.get("hashes")
    predicates = payload.get("predicates")
    if (
        payload.get("artifact_kind") != "hde_epic038_pr02_determinism_proof"
        or payload.get("acceptance_token_satisfied") is not False
        or not isinstance(hashes, dict)
        or not isinstance(artifact_hashes, dict)
        or not isinstance(predicates, dict)
    ):
        raise ValueError("preimage recompute evidence shape mismatch")
    try:
        source = json.loads(source_bytes)
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError("preimage recompute source mismatch") from exc
    if not isinstance(source, dict):
        raise ValueError("preimage recompute source mismatch")
    preimage = dict(source)
    source_stored = preimage.pop("idempotence_hash", None)
    source_recomputed = hashlib.sha256(emitter.emit_public(preimage)).hexdigest()
    source_sha256 = hashlib.sha256(source_bytes).hexdigest()
    stored = hashes.get("stored")
    recomputed = hashes.get("recomputed")
    if (
        not isinstance(stored, str)
        or not isinstance(recomputed, str)
        or len(stored) != 64
        or len(recomputed) != 64
        or any(character not in "0123456789abcdef" for character in stored)
        or any(character not in "0123456789abcdef" for character in recomputed)
        or stored != recomputed
        or stored != source_stored
        or recomputed != source_recomputed
        or artifact_hashes.get("ab_sha256") != source_sha256
        or predicates.get("preimage_hash_match") is not True
    ):
        raise ValueError("preimage recompute predicate mismatch")


def validate_cli_reader_parity_payload(payload: Mapping[str, object]) -> None:
    hashes = payload.get("hashes")
    predicates = payload.get("predicates")
    sources = payload.get("sources")
    if (
        payload.get("artifact_kind") != "hde_epic038_pr02_determinism_proof"
        or payload.get("acceptance_token_satisfied") is not False
        or not isinstance(hashes, dict)
        or not isinstance(predicates, dict)
        or sources
        != {
            "runtime": "engine.runtime.public.emit_reader_public_envelope",
            "cli": "python -m engine.cli showcompat --dump-reader",
        }
    ):
        raise ValueError("CLI/Reader parity evidence shape mismatch")
    reader_hash = hashes.get("reader_sha256")
    cli_hash = hashes.get("cli_sha256")
    if (
        not isinstance(reader_hash, str)
        or not isinstance(cli_hash, str)
        or len(reader_hash) != 64
        or len(cli_hash) != 64
        or any(character not in "0123456789abcdef" for character in reader_hash)
        or any(character not in "0123456789abcdef" for character in cli_hash)
        or reader_hash != cli_hash
        or predicates.get("reader_cli_byte_identity") is not True
    ):
        raise ValueError("CLI/Reader parity predicate mismatch")


def validate_release_attestation_payload(
    payload: Mapping[str, object],
    *,
    expected_source_commit: str,
    manifest_sha256: str,
) -> None:
    required = {
        "schema": "hde.release_attestation.v1",
        "source_commit": expected_source_commit,
        "source_commit_exact": True,
        "manifest_sha256": manifest_sha256,
        "release_id": manifest_sha256,
        "validation_result": "PASS",
        "release_admission": "PR06R_B_FINAL_PASS",
        "pipeline_stop": None,
        "rails": dict(sorted(RELEASE_ATTESTATION_RAILS.items())),
    }
    for key, expected in required.items():
        if payload.get(key) != expected:
            raise ValueError(f"release attestation mismatch: {key}")
    if not _hex64(payload.get("source_tree_sha256")):
        raise ValueError("release attestation mismatch: source_tree_sha256")


class EvidencePending(Exception):
    """A decisive current proof is not available and must remain unclaimed."""


def _validate_qa19_execution(
    manifest: Mapping[str, object],
    log_text: str,
    *,
    error_prefix: str,
) -> None:
    record = manifest.get(EVIDENCE_INTEGRITY_CHECK_ID)
    if not isinstance(record, dict):
        raise ValueError(f"{error_prefix} QA manifest record missing")
    expected_relative_log = "checks/qa-19-po-019/primary.log"
    log_bytes = log_text.encode("utf-8")
    if (
        record.get("log_path") != expected_relative_log
        or record.get("status") != "PASS"
        or record.get("sha256") != hashlib.sha256(log_bytes).hexdigest()
        or record.get("size_bytes") != len(log_bytes)
    ):
        raise ValueError(f"{error_prefix} QA manifest binding mismatch")
    lines = log_text.splitlines()
    if not lines:
        raise ValueError(f"{error_prefix} execution log missing")
    try:
        header = json.loads(lines[0], object_pairs_hook=_unique_json_object)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"{error_prefix} execution header invalid") from exc
    required_rails = {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }
    command = header.get("command") if isinstance(header, dict) else None
    behavior_receipts = [
        line for line in lines if line.startswith("[behavior command] ")
    ]
    exit_receipts = [line for line in lines if line.startswith("BEHAVIOR_EXIT_CODE=")]
    if (
        not isinstance(header, dict)
        or set(header) != QA19_HEADER_FIELDS
        or header.get("check_id") != FINAL_LF_CHECK_ID
        or header.get("status") != "PASS"
        or header.get("exit_code") != 0
        or not isinstance(command, str)
        or hashlib.sha256(command.encode("utf-8")).hexdigest()
        != QA19_HEADER_COMMAND_SHA256
        or not command.endswith(f"; {QA19_BEHAVIOR_COMMAND}")
        or behavior_receipts != [f"[behavior command] {QA19_BEHAVIOR_COMMAND}"]
        or exit_receipts != ["BEHAVIOR_EXIT_CODE=0"]
        or header.get("captured_env") != required_rails
        or header.get("intended_tokens") != []
        or header.get("claimed_tokens") != []
    ):
        raise ValueError(f"{error_prefix} execution predicate mismatch")


def validate_final_lf_evidence(
    manifest: Mapping[str, object], log_text: str
) -> None:
    _validate_qa19_execution(
        manifest,
        log_text,
        error_prefix="final-LF",
    )


def validate_integrity_qa19_evidence(
    manifest: Mapping[str, object],
    log_text: str,
) -> None:
    _validate_qa19_execution(
        manifest,
        log_text,
        error_prefix="evidence-integrity",
    )


def _shell_array(script_text: str, name: str) -> tuple[str, ...]:
    lines = script_text.splitlines()
    try:
        start = lines.index(f"{name}=(")
        end = lines.index(")", start + 1)
    except ValueError as exc:
        raise ValueError(f"final-LF array missing: {name}") from exc
    values = tuple(line.strip() for line in lines[start + 1 : end] if line.strip())
    if not values:
        raise ValueError(f"final-LF array empty: {name}")
    return values


def validate_final_lf_script(script_text: str) -> None:
    required = _shell_array(script_text, "required_files")
    planned = _shell_array(script_text, "planned_files")
    if required != FINAL_LF_REQUIRED_PATHS or planned != FINAL_LF_PLANNED_PATHS:
        raise ValueError("final-LF target coverage mismatch")
    required_loop = (
        'for f in "${required_files[@]}"; do\n'
        '  check_file "$f"\n'
        "done"
    )
    planned_loop = (
        'for f in "${planned_files[@]}"; do\n'
        '  if [[ -f "$f" ]]; then\n'
        '    check_file "$f"\n'
        "  fi\n"
        "done"
    )
    if required_loop not in script_text or planned_loop not in script_text:
        raise ValueError("final-LF loop coverage mismatch")


def _validate_special_semantics(row: Row) -> None:
    if row.token == "EVIDENCE_INDEX_MIRROR_OK":
        if (
            row.primary_evidence
            != (
                HUMAN_INDEX_PATH,
                MACHINE_MIRROR_PATH,
                QA_MANIFEST_PATH,
            )
            or row.artifact_keys
            != (
                HUMAN_INDEX_KEY,
                MACHINE_MIRROR_KEY,
                QA_MANIFEST_KEY,
            )
            or row.proof_anchors
            != (
                f"{HUMAN_INDEX_PATH}.path_proof.txt",
                f"{MACHINE_MIRROR_PATH}.path_proof.txt",
                f"{QA_MANIFEST_PATH}.path_proof.txt",
            )
            or set(row.test_binding.split("; "))
            != {
                "tools/evidence/update_evidence_index.py",
                MIRROR_SCHEMA_VALIDATOR_PATH,
                "tests/evidence/test_hde_epic038_closeout.py",
            }
            or row.ci_binding != EVIDENCE_INDEX_MIRROR_CI_JOB
            or row.live_qa != EVIDENCE_INTEGRITY_CHECK_ID
        ):
            raise ValueError("evidence index/mirror binding mismatch")
        validate_index_mirror_topology()
        validate_integrity_qa19_evidence(
            json.loads((ROOT / QA_MANIFEST_PATH).read_text(encoding="utf-8")),
            (ROOT / EVIDENCE_INTEGRITY_LOG_PATH).read_text(encoding="utf-8"),
        )
    elif row.token == "EVIDENCE_PATHS_VALIDATED_OK":
        if (
            row.primary_evidence != (MACHINE_MIRROR_PATH, QA_MANIFEST_PATH)
            or row.artifact_keys != (MACHINE_MIRROR_KEY, QA_MANIFEST_KEY)
            or row.proof_anchors
            != (
                f"{MACHINE_MIRROR_PATH}.path_proof.txt",
                f"{QA_MANIFEST_PATH}.path_proof.txt",
            )
            or set(row.test_binding.split("; "))
            != {
                EVIDENCE_PATH_VALIDATOR_PATH,
                "tests/evidence/test_hde_epic038_closeout.py",
            }
            or row.ci_binding != EVIDENCE_PATHS_CI_JOB
            or row.live_qa != EVIDENCE_INTEGRITY_CHECK_ID
        ):
            raise ValueError("evidence path-validation binding mismatch")
        validate_mirror_paths()
        validate_integrity_qa19_evidence(
            json.loads((ROOT / QA_MANIFEST_PATH).read_text(encoding="utf-8")),
            (ROOT / EVIDENCE_INTEGRITY_LOG_PATH).read_text(encoding="utf-8"),
        )
    elif row.token == "EVIDENCE_PATH_PROOFS_OK":
        if (
            row.primary_evidence != (MACHINE_MIRROR_PATH, QA_MANIFEST_PATH)
            or row.artifact_keys != (MACHINE_MIRROR_KEY, QA_MANIFEST_KEY)
            or row.proof_anchors
            != (
                f"{MACHINE_MIRROR_PATH}.path_proof.txt",
                f"{QA_MANIFEST_PATH}.path_proof.txt",
            )
            or set(row.test_binding.split("; "))
            != {
                MIRROR_SCHEMA_VALIDATOR_PATH,
                "tests/evidence/test_hde_epic038_closeout.py",
            }
            or row.ci_binding != EVIDENCE_PATH_PROOFS_CI_JOB
            or row.live_qa != EVIDENCE_INTEGRITY_CHECK_ID
        ):
            raise ValueError("evidence path-proof binding mismatch")
        validate_all_mirror_proofs()
        validate_integrity_qa19_evidence(
            json.loads((ROOT / QA_MANIFEST_PATH).read_text(encoding="utf-8")),
            (ROOT / EVIDENCE_INTEGRITY_LOG_PATH).read_text(encoding="utf-8"),
        )
    elif row.token in {
        "DB_RUNTIME_SEARCH_PATH_OK",
        "DB_ROLE_OK",
        "DB_SCHEMA_FINGERPRINT_OK",
    }:
        if (
            row.primary_evidence != (DB_POSTURE_PATH,)
            or row.artifact_keys != (DB_POSTURE_KEY,)
        ):
            raise ValueError(f"database posture binding mismatch: {row.token}")
        payload = json.loads((ROOT / DB_POSTURE_PATH).read_text(encoding="utf-8"))
        validate_db_posture_payload(row.token, payload)
    elif row.token == "NO_EXTERNAL_IO_ON_REFUSAL_OK":
        if row.primary_evidence != (REFUSAL_PATH, REFUSAL_MANIFEST_PATH):
            raise ValueError("closed-rails refusal binding mismatch")
        validate_no_io_payloads(
            (ROOT / REFUSAL_PATH).read_text(encoding="utf-8"),
            json.loads((ROOT / REFUSAL_MANIFEST_PATH).read_text(encoding="utf-8")),
        )
    elif row.token == "PREIMAGE_RECOMPUTE_OK":
        if (
            row.primary_evidence != (PREIMAGE_PATH, PREIMAGE_SOURCE_PATH)
            or row.artifact_keys != (PREIMAGE_KEY, PREIMAGE_SOURCE_KEY)
            or row.proof_anchors
            != (
                f"{PREIMAGE_PATH}.path_proof.txt",
                f"{PREIMAGE_SOURCE_PATH}.path_proof.txt",
            )
            or set(row.test_binding.split("; "))
            != {
                "tests/evidence/test_determinism_gate_proofs.py",
                "tests/evidence/test_hde_epic038_closeout.py",
            }
            or row.live_qa != "qa-04-po-004"
        ):
            raise ValueError("preimage recompute evidence binding mismatch")
        validate_preimage_payload(
            json.loads((ROOT / PREIMAGE_PATH).read_text(encoding="utf-8")),
            (ROOT / PREIMAGE_SOURCE_PATH).read_bytes(),
        )
    elif row.token == "CLI_READER_PARITY_OK":
        if (
            row.primary_evidence != (PREIMAGE_PATH,)
            or row.artifact_keys != (PREIMAGE_KEY,)
            or row.proof_anchors != (f"{PREIMAGE_PATH}.path_proof.txt",)
            or set(row.test_binding.split("; "))
            != {
                "tests/evidence/test_determinism_gate_proofs.py",
                "tests/cli/test_showcompat_parity_and_identity.py",
            }
            or row.live_qa != "qa-04-po-004"
        ):
            raise ValueError("CLI/Reader parity evidence binding mismatch")
        validate_cli_reader_parity_payload(
            json.loads((ROOT / PREIMAGE_PATH).read_text(encoding="utf-8"))
        )
    elif row.token == "DOC_DELTA_PRESENT_OK":
        if (
            row.primary_evidence != (DOC_DELTA_PRIMARY_PATH,)
            or row.artifact_keys != (DOC_DELTA_PRIMARY_KEY,)
            or row.proof_anchors
            != (f"{DOC_DELTA_PRIMARY_PATH}.path_proof.txt",)
            or set(row.test_binding.split("; "))
            != {
                "tools/evidence/generate_hde_epic038_closeout.py",
                "tests/evidence/test_hde_epic038_closeout.py",
            }
            or row.ci_binding != DOC_DELTA_CI_JOB
            or row.live_qa != DOC_DELTA_HISTORICAL_CHECK_ID
            or DOC_DELTA_CAPTURE_PATH not in row.posture
            or DOC_DELTA_CAPTURE_KEY not in row.posture
            or DOC_DELTA_HISTORICAL_LOG_PATH not in row.posture
            or DOC_DELTA_WRITE_COMMAND not in row.posture
            or DOC_DELTA_CHECK_COMMAND not in row.posture
            or DOC_DELTA_CURRENT_PAIR_SHA256 not in row.posture
            or DOC_DELTA_HISTORICAL_PAIR_SHA256 not in row.posture
            or "it did not produce the current normalized bytes" not in row.posture
            or DOC_DELTA_CHECK_COMMAND not in row.future_claim
            or "never current-byte production" not in row.future_claim
        ):
            raise ValueError("doc-delta evidence binding mismatch")
        validate_doc_delta_evidence()
    elif row.token in {
        "QA_PRECOMMIT_CHECKLIST_OK",
        "QA_POSTCOMMIT_CHECKLIST_OK",
    }:
        path, key, owner = PLANNED_BINDINGS[row.token]
        if (
            row.test_binding
            != (
                "tools/evidence/generate_hde_epic038_closeout.py; "
                "tests/evidence/test_hde_epic038_closeout.py"
            )
            or row.owner_task != "DEV-03"
            or row.classification != "planned-new"
            or row.future_claim != _checklist_future_claim(path, key, owner)
            or "--closeout" in row.future_claim
        ):
            raise ValueError(f"checklist planned binding mismatch: {row.token}")
    elif row.token == "RELEASE_ID_RECOMPUTE_OK":
        if (
            row.primary_evidence
            != (
                RELEASE_MANIFEST_PATH,
                RELEASE_ID_PATH,
                RELEASE_RECOMPUTE_PATH,
            )
            or row.artifact_keys
            != (
                RELEASE_MANIFEST_KEY,
                RELEASE_ID_KEY,
                RELEASE_RECOMPUTE_KEY,
            )
            or row.proof_anchors
            != (
                f"{RELEASE_MANIFEST_PATH}.path_proof.txt",
                f"{RELEASE_ID_PATH}.path_proof.txt",
                f"{RELEASE_RECOMPUTE_PATH}.path_proof.txt",
            )
        ):
            raise ValueError("release identity source binding mismatch")
        digest, captured_release_id = validate_release_identity_family()
        if (
            f"`manifest_sha256={digest}`" not in row.future_claim
            or f"digest `{digest}`" not in row.posture
            or f"capture digest `{captured_release_id}`" not in row.posture
        ):
            raise ValueError("release identity digest disclosure mismatch")
        required_bindings = {
            "scripts/release_id_recompute.py",
            "tools/evidence/generate_identity_provenance.py",
            "tools/evidence/build_release_attestation.py",
            "tests/evidence/test_identity_provenance.py",
            "tests/evidence/test_release_manifest_content_binding.py",
            "tests/evidence/test_release_attestation.py",
        }
        if set(row.test_binding.split("; ")) != required_bindings:
            raise ValueError("release validator binding mismatch")
        if row.ci_binding != RELEASE_CI_JOB or row.live_qa != "qa-21-po-021":
            raise ValueError("release execution binding mismatch")
    elif row.token == "CI_CHECK_FINAL_LF_OK":
        if (
            row.primary_evidence != (QA_MANIFEST_PATH,)
            or row.artifact_keys != (QA_MANIFEST_KEY,)
            or row.proof_anchors != (f"{QA_MANIFEST_PATH}.path_proof.txt",)
            or set(row.test_binding.split("; "))
            != {
                "ci/checks/check_final_lf.sh",
                "tests/evidence/test_hde_epic038_closeout.py",
            }
            or row.ci_binding != FINAL_LF_CI_JOB
            or row.live_qa != FINAL_LF_CHECK_ID
        ):
            raise ValueError("final-LF evidence binding mismatch")
        validate_final_lf_evidence(
            json.loads((ROOT / QA_MANIFEST_PATH).read_text(encoding="utf-8")),
            (ROOT / FINAL_LF_LOG_PATH).read_text(encoding="utf-8"),
        )
        validate_final_lf_script(
            (ROOT / FINAL_LF_SCRIPT_PATH).read_text(encoding="utf-8")
        )


def validate_rows(
    rows: Iterable[Row], *, planned_mode: str = "require-absent"
) -> tuple[Row, ...]:
    if planned_mode not in {"require-absent", "allow-current"}:
        raise ValueError(f"invalid planned validation mode: {planned_mode}")
    rows = tuple(rows)
    names = [row.token for row in rows]
    if len(names) != len(set(names)):
        raise ValueError("duplicate token")
    if set(names) != set(TOKENS):
        raise ValueError(
            "token set mismatch: "
            f"missing={sorted(set(TOKENS) - set(names))}; "
            f"unexpected={sorted(set(names) - set(TOKENS))}"
        )
    if tuple(names) != TOKENS:
        raise ValueError("token order mismatch")
    if any(name in PROHIBITED for name in names):
        raise ValueError("prohibited token or non-token label")

    records = _mirror_records()
    current_keys = {key for key, _path, _proof in records}
    qa_manifest = json.loads(
        (ROOT / "audit/qa/hde-epic038/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    scalar_fields = (
        "token",
        "acceptance_token",
        "manifest_token",
        "test_binding",
        "ci_binding",
        "live_qa",
        "epic_id",
        "posture",
        "classification",
        "owner_task",
        "future_claim",
    )
    structured_fields = ("primary_evidence", "artifact_keys", "proof_anchors")
    if set(NONCLAIMING_TEXT_SHA256) != set(TOKENS):
        raise ValueError("nonclaiming allowlist token mismatch")

    for row in rows:
        if any(
            not isinstance(getattr(row, field), str)
            or not getattr(row, field).strip()
            for field in scalar_fields
        ):
            raise ValueError(f"empty field: {row.token}")
        for field in structured_fields:
            values = getattr(row, field)
            if (
                not isinstance(values, (tuple, list))
                or not values
                or any(not isinstance(value, str) or not value.strip() for value in values)
            ):
                raise ValueError(f"empty structured field: {row.token}: {field}")
        if not (
            len(row.primary_evidence)
            == len(row.artifact_keys)
            == len(row.proof_anchors)
        ):
            raise ValueError(f"evidence binding count mismatch: {row.token}")

        values = [
            *(getattr(row, field) for field in scalar_fields),
            *row.primary_evidence,
            *row.artifact_keys,
            *row.proof_anchors,
        ]
        joined = " ".join(values)
        if "*" in joined:
            raise ValueError(
                f"missing existing path or wildcard-only binding: {row.token}"
            )
        if any(marker in joined for marker in ("TBD", "e.g.", "??")):
            raise ValueError(f"placeholder: {row.token}")
        if (
            row.acceptance_token != row.token
            or row.manifest_token != row.token
        ):
            raise ValueError(f"token alias: {row.token}")
        if (
            row.epic_id != EPIC_ID
            or row.classification not in {"existing/reused", "planned-new"}
        ):
            raise ValueError(f"invalid binding: {row.token}")
        nonclaiming_digest = hashlib.sha256(
            f"{row.posture}\0{row.future_claim}".encode("utf-8")
        ).hexdigest()
        if (
            not row.posture.startswith(CURRENT_POSTURE_PREFIX)
            or not row.future_claim.startswith(FUTURE_CLAIM_PREFIXES)
            or nonclaiming_digest != NONCLAIMING_TEXT_SHA256[row.token]
        ):
            raise ValueError(f"nonclaiming posture contract: {row.token}")
        if any(
            marker in joined
            for marker in ("PASS conclusion", "status=PASS", "CLAIMED: PASS")
        ):
            raise ValueError(f"acceptance inference: {row.token}")
        if ".github/workflows/ci.yml" not in row.ci_binding:
            raise ValueError(f"inexact CI binding: {row.token}")

        for test_path in row.test_binding.split("; "):
            if not (ROOT / test_path).is_file():
                raise ValueError(
                    f"missing existing test path: {row.token}: {test_path}"
                )
        if row.live_qa.startswith("N/A:"):
            if len(row.live_qa.removeprefix("N/A:").strip()) < 20:
                raise ValueError(f"insubstantive Live QA N/A: {row.token}")
        else:
            for check_id in row.live_qa.split("; "):
                if check_id not in qa_manifest:
                    raise ValueError(
                        f"unregistered Live QA check ID: {row.token}: {check_id}"
                    )

        if row.classification == "existing/reused":
            if row.owner_task != "N/A: existing/reused evidence":
                raise ValueError(f"invalid existing owner: {row.token}")
            for path in (*row.primary_evidence, *row.proof_anchors):
                if "*" in path or not (ROOT / path).is_file():
                    raise ValueError(f"missing existing path: {row.token}: {path}")
            for key, path, proof in zip(
                row.artifact_keys, row.primary_evidence, row.proof_anchors
            ):
                if (key, path, proof) not in records:
                    raise ValueError(
                        f"unregistered artifact key: {row.token}: {key} -> {path}"
                    )
                _validate_proof(path, proof)
        else:
            expected = PLANNED_BINDINGS.get(row.token)
            if expected is None:
                raise ValueError(f"unauthorized planned token: {row.token}")
            path, key, owner = expected
            if (
                row.primary_evidence != (path,)
                or row.artifact_keys != (key,)
                or row.proof_anchors != (f"{path}.path_proof.txt",)
                or row.owner_task != owner
            ):
                raise ValueError(f"inexact planned binding: {row.token}")
            for planned_path in (*row.primary_evidence, *row.proof_anchors):
                if planned_path not in PLANNED_PATHS:
                    raise ValueError(
                        f"unauthorized planned path: {row.token}: {planned_path}"
                    )
                if (
                    planned_mode == "require-absent"
                    and (ROOT / planned_path).exists()
                ):
                    raise ValueError(
                        f"planned path unexpectedly exists: {row.token}: {planned_path}"
                    )
            if key not in PLANNED_KEYS or (
                planned_mode == "require-absent" and key in current_keys
            ):
                raise ValueError(f"invalid planned artifact key: {row.token}: {key}")
            if row.ci_binding != PLANNED_CI_BINDING:
                raise ValueError(f"inexact planned command: {row.token}")
            if "UNCLAIMED" not in row.posture or "has not been executed" not in row.posture:
                raise ValueError(f"planned evidence claim: {row.token}")

        _validate_special_semantics(row)
    row_contract = json.dumps(
        [vars(row) for row in rows],
        ensure_ascii=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    if hashlib.sha256(row_contract).hexdigest() != ROW_CONTRACT_SHA256:
        raise ValueError("independent row contract drift")
    return rows


def render(
    rows: Iterable[Row] | None = None, *, planned_mode: str = "require-absent"
) -> bytes:
    rows = validate_rows(
        build_rows() if rows is None else rows, planned_mode=planned_mode
    )
    lines = [
        "# HDE-EPIC038 DEV-01 Token Evidence Matrix",
        "",
        (
            "> Nonclaim: all 33 tokens are UNCLAIMED. Matrix construction, "
            "artifact presence, historical PASS text, validation, PR creation, "
            "and Gate B review do not satisfy an acceptance token."
        ),
        "",
        "Each numbered row is canonical; semicolon-separated values are exact bindings.",
        "",
    ]
    for index, row in enumerate(rows, 1):
        lines += [
            f"## {index}. `{row.token}`",
            f"- Canonical governance token: `{row.token}`",
            f"- Acceptance-map token: `{row.acceptance_token}`",
            f"- Manifest token: `{row.manifest_token}`",
            f"- Test/stable identifier: `{row.test_binding}`",
            f"- Closed-rails CI binding: `{row.ci_binding}`",
            f"- Live QA: `{row.live_qa}`",
            f"- Primary governed evidence: `{'; '.join(row.primary_evidence)}`",
            (
                "- Human Index / Machine Mirror artifact keys: "
                f"`{'; '.join(row.artifact_keys)}`"
            ),
            f"- Epic: `epic_id={row.epic_id}`",
            f"- Proof anchors: `{'; '.join(row.proof_anchors)}`",
            f"- Current posture: {row.posture}",
            f"- Classification: `{row.classification}`",
            f"- Owning task: `{row.owner_task}`",
            (
                "- Intended future claim and prerequisite: "
                f"{row.future_claim}"
            ),
            "",
        ]
    return ("\n".join(lines).rstrip("\n") + "\n").encode("utf-8")


# DEV-02 close-package contract.  The matrix renderer above intentionally remains
# byte-for-byte the independently reviewed DEV-01 implementation.
CLOSE_REPORT_PATH = "audit/EPIC-038_close_report.md"
CLOSE_MANIFEST_PATH = "audit/EPIC-038_MANIFEST.json"
ACCEPTANCE_MAP_PATH = "docs/acceptance_map_epic038.json"
VIABILITY_PATH = "audit/qa/hde-epic038/acceptance_map_viability.log"
LEDGER_PATH = "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md"
QA_RCA_PATH = "audit/qa/hde-epic038/00_meta/qa_rca_doc_delta_summary.md"
PACKAGE_PATHS = (CLOSE_REPORT_PATH, CLOSE_MANIFEST_PATH, ACCEPTANCE_MAP_PATH,
                 OUTPUT.as_posix(), VIABILITY_PATH, LEDGER_PATH)
PF09_SCOPE = ("HDE-DIST005.1", "HDE-DIST005.2", "HDE-DIST006.1",
              "HDE-DIST006.2", "HDE-DIST006.3", "HDE-DIST002.4",
              "HDE-DIST002.5", "HDE-DIST003.1", "HDE-DIST003.4",
              "HDE-DIST001.1", "HDE-DIST001.2", "HDE-DIST001.3",
              "HDE-DIST001.4", "HDE-DIST001.5", "HDE-DIST001.9",
              "HDE-DIST001.10", "HDE-DIST001.11", "HDE-DIST001.6",
              "HDE-DIST007 (subtask N/A)")
PF09_EXCLUSIONS = tuple(f"HDE-DIST004.{n}" for n in range(1, 5))
NONCLAIMS = ("OPS execution", "Live QA rerun", "deployment", "PF09 movement",
             "board movement", "Product Owner acceptance", "merge", "epic closure")
LEDGER_SCHEMA = "hde.epic038.closeout_remediation_ledger.v1"
CLOSE_REQUEST_SCHEMA = "hde.epic038.closeout_remediation_ledger.close_request.v1"
LEDGER_KEY = "epic038.closeout_remediation_ledger"
TOKEN_MATRIX_SHA256 = "40918fdf7c2c2e7cb475faa0d0d335ae4641ab25165ec8471491d7029ae73a4c"
SUBJECT_KINDS = frozenset({"TOKEN", "ARTIFACT_PATH", "ARTIFACT_KEY", "CHECK", "PACKAGE", "AUTHORITY"})
FAILURE_OWNERS = {"REGISTRY_OR_WIRING_DEFECT": "CodEx", "EVIDENCE_PRODUCER_OR_VALIDATOR_DEFECT": "CodEx",
                  "GOVERNED_ARTIFACT_DRIFT": "CodEx", "EXISTING_BEHAVIOR_REGRESSION": "Product Owner",
                  "SOURCE_AUTHORITY_CONFLICT": "Product Owner", "EXTERNAL_ONLY_PROOF_GAP": "Product Owner"}
KEY_OUTPUTS = {"acceptance_map": ACCEPTANCE_MAP_PATH, "acceptance_map_viability": VIABILITY_PATH,
               "close_manifest": CLOSE_MANIFEST_PATH, "close_report": CLOSE_REPORT_PATH,
               "closeout_remediation_ledger": LEDGER_PATH, "token_matrix": OUTPUT.as_posix()}


def _canonical_json(value: object, *, pretty: bool = False) -> bytes:
    options = {"ensure_ascii": False, "sort_keys": True}
    if pretty:
        options["indent"] = 2
    else:
        options["separators"] = (",", ":")
    return (json.dumps(value, **options) + "\n").encode("utf-8")


def _blocker_id(predicate_key: str, subject: Mapping[str, str], occurrence: int = 1) -> str:
    identity = {"epic_id": EPIC_ID, "predicate_key": predicate_key, "subject": dict(subject)}
    digest = hashlib.sha256(_canonical_json(identity)).hexdigest()[:16]
    return f"HDE-EPIC038-BLK-{digest}-{occurrence:04d}"


def _normalized_paths(values: object, *, must_exist: bool = False) -> list[str]:
    if not isinstance(values, list) or any(not isinstance(v, str) for v in values):
        raise ValueError("paths must be an array of strings")
    if values != sorted(set(values)):
        raise ValueError("paths must be ASCII-sorted and duplicate-free")
    for value in values:
        path = Path(value)
        if (not value or path.is_absolute() or ".." in path.parts or "*" in value or "?" in value
                or value.endswith("/") or (ROOT / value).is_dir()):
            raise ValueError(f"invalid repository-relative file path: {value}")
        if value.startswith(("audit/ops/", "audit/qa/hde-epic038/checks/")):
            raise ValueError(f"historical evidence path is not writable: {value}")
        if must_exist and not (ROOT / value).is_file():
            raise ValueError(f"missing regenerated artifact: {value}")
    return values


def _descriptor(predicate_key: str, kind: str, value: str, predicate: str,
                evidence: list[dict[str, str]], command: str, failure_class: str,
                permitted: list[str], follow_up: str, validators: list[str],
                external: str = "NONE_REQUIRED") -> dict[str, object]:
    if kind not in SUBJECT_KINDS or FAILURE_OWNERS.get(failure_class) is None:
        raise ValueError("invalid registered blocker descriptor")
    permitted = _normalized_paths(sorted(permitted))
    return {"predicate_key": predicate_key, "subject": {"kind": kind, "value": value},
            "failing_predicate": predicate, "decisive_evidence": evidence,
            "decisive_command": command, "failure_class": failure_class,
            "owner": FAILURE_OWNERS[failure_class], "permitted_files": permitted,
            "minimum_follow_up": follow_up, "required_validator_ids": validators,
            "external_action_posture": external}


def derive_blockers() -> list[dict[str, object]]:
    """Evaluate registered predicates; artifact presence alone is never PASS."""
    if not any((ROOT / path).exists() for path in PLANNED_PATHS):
        validate_rows(build_rows())
    elif hashlib.sha256(_matrix_bytes()).hexdigest() != TOKEN_MATRIX_SHA256:
        raise ValueError("DEV-01 token matrix drift")
    blockers: list[dict[str, object]] = []
    for token in ("TESTS_PASS_OK", "QA_PRECOMMIT_CHECKLIST_OK", "QA_POSTCOMMIT_CHECKLIST_OK"):
        path, key, _owner = PLANNED_BINDINGS[token]
        descriptor = _descriptor(
            f"token.{token}.current_governed_result", "TOKEN", token,
            f"{token} lacks an exact current governed PASS receipt",
            [{"kind": "ARTIFACT_PATH", "value": path}, {"kind": "ARTIFACT_KEY", "value": key}],
            PLAN_CLOSEOUT_CHECK_COMMAND if token == "TESTS_PASS_OK" else PLANNED_COMMANDS,
            "GOVERNED_ARTIFACT_DRIFT", [path],
            f"DEV-03 must produce, register, prove, and validate the exact current evidence for {token}.",
            ["closeout_package_in_memory", "epic038_current_state"]
        )
        passed, _detail = evaluate_registered_predicate(descriptor)
        if not passed:
            blockers.append(descriptor)
    return sorted(blockers, key=lambda d: (str(d["predicate_key"]), json.dumps(d["subject"], sort_keys=True)))


def _empty_ledger() -> dict[str, object]:
    return {"artifact_key": LEDGER_KEY, "entries": [], "epic_id": EPIC_ID, "schema": LEDGER_SCHEMA}


def render_ledger(payload: Mapping[str, object]) -> bytes:
    validate_ledger(payload)
    body = json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2)
    return f"# HDE-EPIC038 Closeout Remediation Ledger\n\n```json\n{body}\n```\n".encode()


def parse_ledger(data: bytes) -> dict[str, object]:
    prefix, suffix = b"# HDE-EPIC038 Closeout Remediation Ledger\n\n```json\n", b"\n```\n"
    if not data.startswith(prefix) or not data.endswith(suffix):
        raise ValueError("invalid ledger template")
    payload = json.loads(data[len(prefix):-len(suffix)], object_pairs_hook=_unique_json_object)
    if render_ledger(payload) != data:
        raise ValueError("noncanonical remediation ledger")
    return payload


def validate_ledger(payload: Mapping[str, object]) -> None:
    if set(payload) != {"artifact_key", "entries", "epic_id", "schema"} or payload.get("artifact_key") != LEDGER_KEY or payload.get("epic_id") != EPIC_ID or payload.get("schema") != LEDGER_SCHEMA:
        raise ValueError("invalid remediation ledger identity")
    entries = payload.get("entries")
    if not isinstance(entries, list): raise ValueError("invalid remediation ledger entries")
    ids: list[str] = []
    exact = {"after_outcome", "before_outcome", "blocker_id", "correction_performed", "decisive_command", "decisive_evidence", "external_action_posture", "failing_predicate", "failure_class", "historical_evidence_rewritten", "minimum_follow_up", "owner", "permitted_files", "predicate_key", "regenerated_artifacts", "required_validator_ids", "reviewer_disposition", "status", "subject", "tests_and_validators"}
    identities: dict[str, tuple[str, str, str]] = {}
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != exact: raise ValueError("invalid ledger entry fields")
        subject = entry["subject"]
        if not isinstance(subject, dict) or set(subject) != {"kind", "value"} or subject["kind"] not in SUBJECT_KINDS: raise ValueError("invalid ledger subject")
        match = re.fullmatch(r"HDE-EPIC038-BLK-([0-9a-f]{16})-([0-9]{4})", str(entry["blocker_id"]))
        if not match or match.group(1) != _blocker_id(str(entry["predicate_key"]), subject).split("-")[-2]: raise ValueError("invalid blocker id")
        identity = (str(entry["predicate_key"]), str(subject["kind"]), str(subject["value"]))
        if match.group(1) in identities and identities[match.group(1)] != identity: raise ValueError("blocker digest collision")
        identities[match.group(1)] = identity; ids.append(str(entry["blocker_id"]))
        if entry["owner"] != FAILURE_OWNERS.get(str(entry["failure_class"])): raise ValueError("invalid failure owner")
        if not isinstance(entry["predicate_key"], str) or not entry["predicate_key"] or not isinstance(entry["failing_predicate"], str) or not entry["failing_predicate"]:
            raise ValueError("invalid ledger predicate")
        if not isinstance(entry["decisive_command"], str) or not entry["decisive_command"]:
            raise ValueError("invalid decisive command")
        evidence = entry["decisive_evidence"]
        if not isinstance(evidence, list) or not evidence or any(not isinstance(item, dict) or set(item) != {"kind", "value"} or item["kind"] not in {"ARTIFACT_PATH", "ARTIFACT_KEY", "CHECK", "DIGEST", "DETAIL"} or not isinstance(item["value"], str) or not item["value"] for item in evidence):
            raise ValueError("invalid decisive evidence")
        if entry["external_action_posture"] not in {"NONE_REQUIRED", "PO_AUTHORIZATION_REQUIRED", "PO_AUTHORIZED_EVIDENCE_BOUND"}:
            raise ValueError("invalid external action posture")
        if not isinstance(entry["minimum_follow_up"], str) or not entry["minimum_follow_up"]:
            raise ValueError("invalid minimum follow-up")
        if not isinstance(entry["required_validator_ids"], list) or any(not isinstance(v, str) or not v for v in entry["required_validator_ids"]):
            raise ValueError("invalid validator roster")
        before = entry["before_outcome"]
        if not isinstance(before, dict) or set(before) != {"detail", "result"} or before["result"] != "FAIL" or not isinstance(before["detail"], str) or not before["detail"]:
            raise ValueError("invalid before outcome")
        _normalized_paths(entry["permitted_files"]); _normalized_paths(entry["regenerated_artifacts"])
        if entry["historical_evidence_rewritten"] is not False: raise ValueError("historical evidence rewrite")
        if entry["status"] == "OPEN":
            if entry["reviewer_disposition"] != "PENDING_REVIEW" or entry["after_outcome"] is not None or entry["correction_performed"] is not None or entry["tests_and_validators"] or entry["regenerated_artifacts"]: raise ValueError("invalid OPEN entry")
        elif entry["status"] == "CLOSED":
            if entry["reviewer_disposition"] != "CLOSURE_VALIDATED" or not entry["correction_performed"] or not entry["tests_and_validators"] or entry["after_outcome"] is None: raise ValueError("invalid CLOSED entry")
            after = entry["after_outcome"]
            if not isinstance(after, dict) or set(after) != {"detail", "result"} or after["result"] != "PASS" or not isinstance(after["detail"], str) or not after["detail"]:
                raise ValueError("invalid after outcome")
            if any(not isinstance(item, dict) or set(item) != {"command", "exit_code", "id", "result"} or item["exit_code"] != 0 or item["result"] != "PASS" or not item["command"] or not item["id"] for item in entry["tests_and_validators"]):
                raise ValueError("invalid closure validator result")
        else: raise ValueError("invalid ledger status")
    if ids != sorted(set(ids)): raise ValueError("ledger entries not sorted or unique")


def _load_ledger() -> dict[str, object]:
    path = ROOT / LEDGER_PATH
    return parse_ledger(path.read_bytes()) if path.is_file() else _empty_ledger()


def record_blockers(ledger: Mapping[str, object], blockers: list[dict[str, object]]) -> dict[str, object]:
    entries = [dict(e) for e in ledger["entries"]]  # type: ignore[index]
    for descriptor in blockers:
        subject = descriptor["subject"]
        matching = [e for e in entries if e["predicate_key"] == descriptor["predicate_key"] and e["subject"] == subject]
        if any(e["status"] == "OPEN" for e in matching): continue
        occurrence = max([int(str(e["blocker_id"])[-4:]) for e in matching] or [0]) + 1
        entry = dict(descriptor)
        entry.update({"blocker_id": _blocker_id(str(descriptor["predicate_key"]), subject, occurrence),
                      "before_outcome": {"detail": descriptor["failing_predicate"], "result": "FAIL"},
                      "after_outcome": None, "correction_performed": None,
                      "regenerated_artifacts": [], "historical_evidence_rewritten": False,
                      "reviewer_disposition": "PENDING_REVIEW", "status": "OPEN", "tests_and_validators": []})
        entries.append(entry)
    result = _empty_ledger(); result["entries"] = sorted(entries, key=lambda e: e["blocker_id"])
    validate_ledger(result); return result


def _matrix_bytes() -> bytes:
    path = ROOT / OUTPUT
    if path.is_file(): return path.read_bytes()
    return render()


def build_package(blockers: list[dict[str, object]] | None = None, ledger: Mapping[str, object] | None = None) -> dict[str, bytes]:
    blockers = derive_blockers() if blockers is None else blockers
    ledger = record_blockers(_load_ledger() if ledger is None else ledger, blockers)
    open_ids = [e["blocker_id"] for e in ledger["entries"] if e["status"] == "OPEN"]  # type: ignore[index]
    decision = "NOT SATISFIED" if blockers or open_ids else "SATISFIED"
    blocker_tokens = {d["subject"]["value"] for d in blockers if d["subject"]["kind"] == "TOKEN"}
    statuses = {token: ("NOT PASS" if token in blocker_tokens else "PASS") for token in TOKENS}
    minimum = [str(d["minimum_follow_up"]) for d in blockers]
    acceptance = {"artifact_key": "epic038.acceptance_map", "decision": decision, "epic_id": EPIC_ID,
                  "pf09_scope": list(PF09_SCOPE), "pf09_exclusions": list(PF09_EXCLUSIONS),
                  "records": [{"token": row.token, "status": statuses[row.token], "test_binding": row.test_binding,
                               "ci_binding": row.ci_binding, "live_qa": row.live_qa, "primary_evidence": list(row.primary_evidence),
                               "artifact_keys": list(row.artifact_keys), "proof_anchors": list(row.proof_anchors),
                               "classification": row.classification, "claim_prerequisite": row.future_claim} for row in build_rows()],
                  "minimum_follow_up": minimum, "schema_version": "1.0"}
    viability_lines = ["HDE-EPIC038 ACCEPTANCE MAP VIABILITY", f"DECISION: {decision}"]
    for token in TOKENS: viability_lines.append(f"TOKEN {token}: {statuses[token]}")
    for d in blockers: viability_lines.append(f"BLOCKER {_blocker_id(str(d['predicate_key']), d['subject'])}: {d['failing_predicate']} | MINIMUM FOLLOW-UP: {d['minimum_follow_up']}")
    viability = ("\n".join(viability_lines) + "\n").encode()
    qapath = ROOT / QA_RCA_PATH
    qa = qapath.read_text(encoding="utf-8") if qapath.is_file() else "SOURCE UNAVAILABLE"
    report = ["# HDE-EPIC038 Close Report", "", f"## Final decision: {decision}", "",
              "## Exact package pointers"] + [f"- `{k}`: `{v}`" for k, v in KEY_OUTPUTS.items()]
    report += ["", "## Token outcomes"] + [f"- `{t}`: `{statuses[t]}`" for t in TOKENS]
    report += ["", "## PF09 scope"] + [f"- `{x}`" for x in PF09_SCOPE] + ["", "## Explicit exclusions"] + [f"- `{x}`" for x in PF09_EXCLUSIONS]
    report += ["", "## Embedded complete QA RCA and Doc Delta accounting", f"Preserved execution-level source evidence: `{QA_RCA_PATH}`. It is not the canonical standalone closeout-summary path.", "", qa.rstrip(), "",
               "Closeout-level accounting: qa-00 through qa-23 are retained in plan order; Step-0C was non-applicable. qa-05 used bounded remediation; ADR-DEV-01 used partial-cluster generation; qa-08 used the Extended Moon Loop; qa-11 records the preflight deviation; legacy `.sh` Python entrypoints are historical naming, not shell execution. Source-of-truth, accepted-deviation, evidence-light-source, root-cause, remediation-loop, evidence-hygiene, and Doc Delta dimensions follow PF10 — HDE Build Notes §2.36. Historical execution venue: UNKNOWN - NON-MATERIAL. PF10 §2.34 is evidence-light; its historical PF19-availability statement is stale against current Repo and permanent-canon drainage remains non-blocking follow-up. Execution-level READY FOR CLOSEOUT REVIEW and closeout-review READY WITH CAVEATS do not mean SATISFIED.", "",
               "## Tracked issues", "- TI-001: RELEASE_ID_RECOMPUTE_OK admitted; retired DEV_DB_BRIDGE_FALLBACK_OK removed; nine prohibited PF09 labels remain non-token obligations; registry drainage is separate.", "- TI-R1-001: landed matrix and Gate B resolve only the matrix checkpoint and claim no token.", "- TI-R1-002: acceptance outputs require DEV-02 capability plus DEV-03 governed generation.", "- TI-R1-003: formal completion continues through exact-head validation and Gate D.", "- TI-R1-004: blockers remain ledgered in NOT SATISFIED until exact evidence closes them.", "- TI-R1-005: approval preceded DEV-01; DEV-02 remains conditioned on landed Gate B.", "",
               "## ADR records"]
    adr_decisions = ["one bounded closed-rails DEV lineage; no OPS or Live QA", "evidence-derived SATISFIED; blockers require complete NOT SATISFIED and minimum follow-up", "retired bridge token removed only from current claims; history immutable", "no new PF09 task; PF06 owns close mechanics and HDE-DIST005.2 owns updater discipline", "DEV-01 follows approval and DEV-02 follows Gate B; authority changes require stop"]
    for i, decision_text in enumerate(adr_decisions, 1):
        report += [f"### ADR-R1-00{i}", f"- Decision label: ADR-R1-00{i}", "- Decision point: bounded HDE-EPIC038 remediation closeout", "- Options: use the established bounded decision or stop for renewed authority; no additional option is established.", "- Governing canon: PF06 close-gate rules and PF10 HDE Build Notes", f"- Final decision: {decision_text}.", "- Disposition: epic-specific unless permanent canon drainage is explicitly authorized.", "- Drain targets: established PF06/PF09 homes only; no invented target.", ""]
    report += ["## Reused proof disclosure", "Existing proof families are reused, not regenerated. No Index, Mirror, orientation, checksum, or proof refresh is claimed without same-run updater evidence.", "", "## Nonclaims"] + [f"- No {x}." for x in NONCLAIMS]
    if decision == "NOT SATISFIED": report += ["", "## Minimum follow-up"] + [f"- {x}" for x in minimum or ["Close every OPEN remediation entry with registered evidence and validators."]]
    report_bytes = ("\n".join(report).rstrip() + "\n").encode()
    manifest = {"decision": decision, "epic_id": EPIC_ID, "key_outputs": KEY_OUTPUTS, "nonclaims": list(NONCLAIMS),
                "pf09_scope": list(PF09_SCOPE), "pf09_exclusions": list(PF09_EXCLUSIONS), "token_roster": list(TOKENS),
                "token_status": statuses, "minimum_follow_up": minimum, "schema_version": "1.0"}
    package = {CLOSE_REPORT_PATH: report_bytes, CLOSE_MANIFEST_PATH: _canonical_json(manifest),
               ACCEPTANCE_MAP_PATH: _canonical_json(acceptance), OUTPUT.as_posix(): _matrix_bytes(),
               VIABILITY_PATH: viability, LEDGER_PATH: render_ledger(ledger)}
    validate_package(package); return package


def validate_package_structure(package: Mapping[str, bytes]) -> None:
    """Validate package bytes and cross-surfaces without current proof/index state."""
    if set(package) != set(PACKAGE_PATHS) or any(not b or not b.endswith(b"\n") or b"\r" in b for b in package.values()): raise ValueError("incomplete or noncanonical package")
    manifest = json.loads(package[CLOSE_MANIFEST_PATH], object_pairs_hook=_unique_json_object)
    amap = json.loads(package[ACCEPTANCE_MAP_PATH], object_pairs_hook=_unique_json_object)
    ledger = parse_ledger(package[LEDGER_PATH])
    if not isinstance(manifest.get("key_outputs"), dict) or manifest["key_outputs"] != KEY_OUTPUTS: raise ValueError("manifest key_outputs must be exact object")
    roster = [r.get("token") for r in amap.get("records", [])]
    if tuple(roster) != TOKENS or manifest.get("token_roster") != list(TOKENS): raise ValueError("reduced or invalid package roster")
    decision = manifest.get("decision")
    if decision not in {"SATISFIED", "NOT SATISFIED"} or amap.get("decision") != decision or f"DECISION: {decision}".encode() not in package[VIABILITY_PATH] or f"Final decision: {decision}".encode() not in package[CLOSE_REPORT_PATH]: raise ValueError("package decision mismatch")
    open_entries = any(e["status"] == "OPEN" for e in ledger["entries"])
    false_tokens = any(v != "PASS" for v in manifest.get("token_status", {}).values())
    if decision == "SATISFIED" and (open_entries or false_tokens): raise ValueError("forced SATISFIED")
    if decision == "NOT SATISFIED" and not manifest.get("minimum_follow_up") and not open_entries: raise ValueError("NOT SATISFIED without minimum follow-up")
    report = package[CLOSE_REPORT_PATH].decode()
    for required in (*PF09_SCOPE, *PF09_EXCLUSIONS, "TI-001", "TI-R1-005", "ADR-R1-001", "ADR-R1-005", QA_RCA_PATH, "qa-00", "qa-23", "UNKNOWN - NON-MATERIAL"):
        if required not in report: raise ValueError(f"incomplete close report: {required}")


def _write_package(package: Mapping[str, bytes]) -> None:
    staged: dict[Path, Path] = {}; originals: dict[Path, bytes | None] = {}; modes: dict[Path, int] = {}
    try:
        for rel in PACKAGE_PATHS:
            target = ROOT / rel; originals[target] = target.read_bytes() if target.is_file() else None
            modes[target] = target.stat().st_mode & 0o777 if target.exists() else 0o644
            staged[target] = _stage_atomic_bytes(target, package[rel], modes[target])
        replaced: list[Path] = []
        try:
            for rel in PACKAGE_PATHS:
                target = ROOT / rel; os.replace(staged[target], target); replaced.append(target)
        except Exception:
            for target in reversed(replaced):
                prior = originals[target]
                if prior is None: target.unlink(missing_ok=True)
                else:
                    rollback = _stage_atomic_bytes(target, prior, modes[target]); os.replace(rollback, target)
            raise
    finally:
        for path in staged.values(): path.unlink(missing_ok=True)


def _parse_close_request(raw: str) -> dict[str, object]:
    try:
        request = json.loads(raw, object_pairs_hook=_unique_json_object)
    except (json.JSONDecodeError, ValueError) as exc:
        raise ValueError("invalid close request JSON") from exc
    keys = {"blocker_id", "correction_performed", "external_action_posture",
            "historical_evidence_rewritten", "regenerated_artifacts", "schema"}
    if not isinstance(request, dict) or set(request) != keys or request.get("schema") != CLOSE_REQUEST_SCHEMA:
        raise ValueError("invalid close request schema")
    if _canonical_json(request).decode() != raw:
        raise ValueError("close request is not canonical compact JSON with final LF")
    if not isinstance(request.get("correction_performed"), str) or not request["correction_performed"].strip() or request["correction_performed"] != request["correction_performed"].strip():
        raise ValueError("invalid correction_performed")
    if request.get("historical_evidence_rewritten") is not False:
        raise ValueError("historical evidence rewrite is prohibited")
    if request.get("external_action_posture") not in {"NONE_REQUIRED", "PO_AUTHORIZATION_REQUIRED", "PO_AUTHORIZED_EVIDENCE_BOUND"}:
        raise ValueError("invalid external action posture")
    _normalized_paths(request.get("regenerated_artifacts"), must_exist=True)
    return request


def evaluate_registered_predicate(entry: Mapping[str, object]) -> tuple[bool, str]:
    """Direct predicate registry. No result is inferred from blocker absence."""
    token = entry["subject"].get("value") if isinstance(entry.get("subject"), dict) else None
    if token not in PLANNED_BINDINGS:
        return False, "predicate has no source-controlled closure evaluator"
    path, key, _owner = PLANNED_BINDINGS[str(token)]
    try:
        if not (ROOT / path).is_file(): return False, f"missing governed primary {path}"
        _validate_proof(path, path + ".path_proof.txt")
        if not any(record[:2] == (key, path) for record in _mirror_records()):
            return False, f"missing current Index/Mirror binding {key}"
    except ValueError as exc:
        return False, str(exc)
    return True, f"registered current evidence validates for {token}"


def run_registered_validator(validator_id: str) -> dict[str, object]:
    if validator_id == "closeout_package_in_memory":
        return {"command": "internal:validate_package", "exit_code": 0, "id": validator_id, "result": "PASS"}
    if validator_id == "epic038_current_state":
        command = [sys.executable, str(ROOT / "tools/evidence/check_hde_epic038_qa_current_state.py"), "--require-finalized"]
        result = subprocess.run(command, cwd=ROOT, env={**os.environ, "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, capture_output=True, text=True)
        if result.returncode: raise ValueError(f"validator failed: {validator_id}")
        return {"command": "python tools/evidence/check_hde_epic038_qa_current_state.py --require-finalized", "exit_code": 0, "id": validator_id, "result": "PASS"}
    raise ValueError(f"unknown registered validator: {validator_id}")


def close_blocker(raw_request: str) -> dict[str, bytes]:
    request = _parse_close_request(raw_request)
    ledger = _load_ledger(); entries = [dict(e) for e in ledger["entries"]]  # type: ignore[index]
    matches = [e for e in entries if e["blocker_id"] == request["blocker_id"] and e["status"] == "OPEN"]
    if len(matches) != 1: raise RuntimeError("close request does not identify exactly one OPEN entry")
    entry = matches[0]
    if entry["external_action_posture"] == "PO_AUTHORIZATION_REQUIRED" or request["external_action_posture"] == "PO_AUTHORIZATION_REQUIRED":
        raise RuntimeError("Product Owner authorization and bound evidence are required")
    permitted = set(entry["permitted_files"])
    if not set(request["regenerated_artifacts"]).issubset(permitted): raise RuntimeError("regenerated artifacts exceed permitted scope")
    passed, detail = evaluate_registered_predicate(entry)
    if not passed: raise RuntimeError(detail)
    results = [run_registered_validator(str(v)) for v in entry["required_validator_ids"]]
    entry.update({"after_outcome": {"detail": detail, "result": "PASS"},
                  "correction_performed": request["correction_performed"],
                  "external_action_posture": request["external_action_posture"],
                  "regenerated_artifacts": request["regenerated_artifacts"],
                  "reviewer_disposition": "CLOSURE_VALIDATED", "status": "CLOSED",
                  "tests_and_validators": results})
    updated = _empty_ledger(); updated["entries"] = sorted(entries, key=lambda e: e["blocker_id"])
    validate_ledger(updated)
    # Re-evaluate directly. A still-false predicate remains a blocker; absence is
    # never interpreted as success.
    blockers = derive_blockers()
    blockers = [b for b in blockers if not (b["predicate_key"] == entry["predicate_key"] and b["subject"] == entry["subject"])]
    return build_package(blockers, updated)


# DEV-02 authoritative evaluator and package implementation.  These definitions
# deliberately replace the provisional implementation above while leaving the
# independently approved DEV-01 matrix implementation and bytes intact.
PRECOMMIT_CHECKLIST_PATH = (
    "audit/qa/hde-epic038/00_meta/qa_precommit_checklist.log"
)
POSTCOMMIT_CHECKLIST_PATH = (
    "audit/qa/hde-epic038/00_meta/qa_postcommit_checklist.log"
)
PRECOMMIT_CHECKLIST_KEY = "epic038.qa_precommit_checklist"
POSTCOMMIT_CHECKLIST_KEY = "epic038.qa_postcommit_checklist"
PACKAGE_PATHS = (
    CLOSE_REPORT_PATH,
    CLOSE_MANIFEST_PATH,
    ACCEPTANCE_MAP_PATH,
    OUTPUT.as_posix(),
    VIABILITY_PATH,
    LEDGER_PATH,
    PRECOMMIT_CHECKLIST_PATH,
    POSTCOMMIT_CHECKLIST_PATH,
)
PACKAGE_ACTIVATION_PATHS = (
    CLOSE_REPORT_PATH,
    CLOSE_MANIFEST_PATH,
    ACCEPTANCE_MAP_PATH,
    VIABILITY_PATH,
    LEDGER_PATH,
    PRECOMMIT_CHECKLIST_PATH,
    POSTCOMMIT_CHECKLIST_PATH,
)
KEY_OUTPUTS = {
    "acceptance_map": ACCEPTANCE_MAP_PATH,
    "acceptance_map_viability": VIABILITY_PATH,
    "close_manifest": CLOSE_MANIFEST_PATH,
    "close_report": CLOSE_REPORT_PATH,
    "closeout_remediation_ledger": LEDGER_PATH,
    "qa_postcommit_checklist": POSTCOMMIT_CHECKLIST_PATH,
    "qa_precommit_checklist": PRECOMMIT_CHECKLIST_PATH,
    "token_matrix": OUTPUT.as_posix(),
}
CLOSEOUT_PRIMARY_BINDINGS: Mapping[str, tuple[str, str]] = {
    "epic038.close_report": (CLOSE_REPORT_PATH, f"{CLOSE_REPORT_PATH}.path_proof.txt"),
    "epic038.manifest": (CLOSE_MANIFEST_PATH, f"{CLOSE_MANIFEST_PATH}.path_proof.txt"),
    "epic038.acceptance_map": (ACCEPTANCE_MAP_PATH, f"{ACCEPTANCE_MAP_PATH}.path_proof.txt"),
    "epic038.acceptance_map_viability": (VIABILITY_PATH, f"{VIABILITY_PATH}.path_proof.txt"),
    LEDGER_KEY: (LEDGER_PATH, f"{LEDGER_PATH}.path_proof.txt"),
    PRECOMMIT_CHECKLIST_KEY: (
        PRECOMMIT_CHECKLIST_PATH,
        f"{PRECOMMIT_CHECKLIST_PATH}.path_proof.txt",
    ),
    POSTCOMMIT_CHECKLIST_KEY: (
        POSTCOMMIT_CHECKLIST_PATH,
        f"{POSTCOMMIT_CHECKLIST_PATH}.path_proof.txt",
    ),
}
FINAL_LF_PLANNED_PATHS = (
    "audit/EPIC-038_close_report.md",
    "audit/EPIC-038_close_report.md.path_proof.txt",
    "audit/EPIC-038_MANIFEST.json",
    "audit/EPIC-038_MANIFEST.json.path_proof.txt",
    "docs/acceptance_map_epic038.json",
    "docs/acceptance_map_epic038.json.path_proof.txt",
    "audit/qa/hde-epic038/acceptance_map_viability.log",
    "audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt",
    "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
    "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt",
    PRECOMMIT_CHECKLIST_PATH,
    f"{PRECOMMIT_CHECKLIST_PATH}.path_proof.txt",
    POSTCOMMIT_CHECKLIST_PATH,
    f"{POSTCOMMIT_CHECKLIST_PATH}.path_proof.txt",
)

_PRIVATE_CI_ALLOWED_GENERATED_PATHS = frozenset(
    {
        *FINAL_LF_PLANNED_PATHS,
        HUMAN_INDEX_PATH,
        f"{HUMAN_INDEX_PATH}.path_proof.txt",
        "docs/evidence/INDEX.sha256",
        "docs/evidence/INDEX.sha256.path_proof.txt",
        MACHINE_MIRROR_PATH,
        f"{MACHINE_MIRROR_PATH}.path_proof.txt",
        "artifacts/evidence_index.jsonl.sha256",
        "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
        "audit/gates/topology/orientation_demo.txt",
        "audit/gates/topology/orientation_demo.txt.path_proof.txt",
    }
)

QA_CHECK_IDS = (
    "qa-00-step-0-discovery",
    "qa-01-po-001",
    "qa-02-po-002",
    "qa-03-po-003",
    "qa-04-po-004",
    "qa-05-po-005",
    "qa-06-po-006",
    "qa-07-po-007",
    "qa-08-po-008",
    "qa-09-po-009",
    "qa-10-po-010",
    "qa-11-po-011",
    "qa-12-po-012",
    "qa-13-po-013",
    "qa-14-po-014",
    "qa-15-po-015",
    "qa-16-po-016",
    "qa-17-po-017",
    "qa-18-po-018",
    "qa-19-po-019",
    "qa-20-po-020",
    "qa-21-po-021",
    "qa-22-po-022",
    "qa-23-po-023",
)
PLAN_PATH = "docs/plans/r5-Epic-Remediation-Plan-HDE-EPIC038-Closeout-Completion.md"
APPROVED_PLAN_SHA256 = "3846232f0a8fd1e7a1bc8ab1723107cce40c26c9622a8379e4ac212c215bffbf"
NON_TOKEN_OBLIGATIONS = (
    "BG_SOURCE_SELECTION_OK",
    "BG_VENDOR_CALLS_DISABLED_IN_PROD_OK",
    "BG_SOURCE_INVARIANCE_OK",
    "BG_TTL_SWR_POLICY_OK",
    "BG_RATE_LIMIT_POLICY_OK",
    "BG_CIRCUIT_BREAKER_POLICY_OK",
    "ENV_SNAPSHOT_SINGLETON_OK",
    "ENV_SNAPSHOT_SCHEMA_V3_OK",
    "ENV_PINS_PRESENT_OK",
)
NON_TOKEN_BINDINGS: Mapping[str, tuple[str, str, str]] = {
    "BG_SOURCE_SELECTION_OK": (
        "bodygraph.source_selection",
        "artifacts/bodygraph/source_selection.snapshot.json",
        "artifacts/bodygraph/source_selection.snapshot.json.path_proof.txt",
    ),
    "BG_VENDOR_CALLS_DISABLED_IN_PROD_OK": (
        "bodygraph.source_selection",
        "artifacts/bodygraph/source_selection.snapshot.json",
        "artifacts/bodygraph/source_selection.snapshot.json.path_proof.txt",
    ),
    "BG_SOURCE_INVARIANCE_OK": (
        "bodygraph.source_invariance.summary",
        "artifacts/bodygraph/source_invariance/summary.json",
        "artifacts/bodygraph/source_invariance/summary.json.path_proof.txt",
    ),
    "BG_TTL_SWR_POLICY_OK": (
        "bodygraph.refresh_policy.snapshot",
        "artifacts/bodygraph/refresh_policy.snapshot.json",
        "artifacts/bodygraph/refresh_policy.snapshot.json.path_proof.txt",
    ),
    "BG_RATE_LIMIT_POLICY_OK": (
        "bodygraph.refresh_policy.snapshot",
        "artifacts/bodygraph/refresh_policy.snapshot.json",
        "artifacts/bodygraph/refresh_policy.snapshot.json.path_proof.txt",
    ),
    "BG_CIRCUIT_BREAKER_POLICY_OK": (
        "bodygraph.refresh_policy.snapshot",
        "artifacts/bodygraph/refresh_policy.snapshot.json",
        "artifacts/bodygraph/refresh_policy.snapshot.json.path_proof.txt",
    ),
    "ENV_SNAPSHOT_SINGLETON_OK": (
        "epic038.pr01.env_matrix_snapshot_v3",
        "artifacts/runtime/env_matrix.snapshot.json",
        "artifacts/runtime/env_matrix.snapshot.json.path_proof.txt",
    ),
    "ENV_SNAPSHOT_SCHEMA_V3_OK": (
        "epic038.pr01.env_matrix_snapshot_v3",
        "artifacts/runtime/env_matrix.snapshot.json",
        "artifacts/runtime/env_matrix.snapshot.json.path_proof.txt",
    ),
    "ENV_PINS_PRESENT_OK": (
        "epic038.pr01.env_matrix_snapshot_v3",
        "artifacts/runtime/env_matrix.snapshot.json",
        "artifacts/runtime/env_matrix.snapshot.json.path_proof.txt",
    ),
}

TRACKED_ISSUES: Mapping[str, Mapping[str, str]] = {
    "TI-001": {
        "disposition": "RETAINED_AND_ACCOUNTED",
        "detail": (
            "RELEASE_ID_RECOMPUTE_OK is admitted; retired "
            "DEV_DB_BRIDGE_FALLBACK_OK is excluded from every current acceptance "
            "surface; nine prohibited PF09 labels remain non-token obligations."
        ),
    },
    "TI-R1-001": {
        "disposition": "MATRIX_CHECKPOINT_ONLY",
        "detail": "The landed DEV-01 matrix and Gate B make no token claim.",
    },
    "TI-R1-002": {
        "disposition": "DEV03_FIXED_POINT_REQUIRED",
        "detail": "Final acceptance outputs require DEV-03 governed generation.",
    },
    "TI-R1-003": {
        "disposition": "EXACT_HEAD_VALIDATION_REQUIRED",
        "detail": "Formal completion continues through exact-head validation and Gate D.",
    },
    "TI-R1-004": {
        "disposition": "LEDGER_UNTIL_CLOSED",
        "detail": "Every blocker remains OPEN and NOT SATISFIED until directly revalidated.",
    },
    "TI-R1-005": {
        "disposition": "SEQUENCING_PRESERVED",
        "detail": "DEV-02 follows landed Gate B and does not perform DEV-03 or acceptance.",
    },
}

ADR_RECORDS: tuple[Mapping[str, object], ...] = (
    {
        "label": "ADR-R1-001",
        "decision_point": "Execution lineage and rails",
        "options": [
            "One bounded closed-rails DEV lineage with no OPS or Live QA",
            "Broaden execution into OPS or Live QA",
        ],
        "governing_canon": ["PF06 §3.5", "PF10 Addendum 2.36"],
        "final_decision": "Use one bounded closed-rails DEV lineage; no OPS or Live QA.",
        "disposition": "EPIC_SPECIFIC",
        "drain_targets": ["PF06 close-gate rules"],
    },
    {
        "label": "ADR-R1-002",
        "decision_point": "Binary closeout decision",
        "options": [
            "Derive SATISFIED from affirmative evidence",
            "Infer SATISFIED from missing blockers or path presence",
        ],
        "governing_canon": ["PF06 §3.5.4", "PF10 Addendum 2.36"],
        "final_decision": (
            "Derive SATISFIED only from affirmative evidence; otherwise emit the "
            "complete NOT SATISFIED package with exact follow-up."
        ),
        "disposition": "EPIC_SPECIFIC",
        "drain_targets": ["PF06 close-gate rules"],
    },
    {
        "label": "ADR-R1-003",
        "decision_point": "Retired bridge-token history",
        "options": [
            "Exclude the retired token from current claims while preserving history",
            "Rewrite historical evidence or restore the retired token",
        ],
        "governing_canon": ["PF04 governance", "PF10 Addendum 2.37"],
        "final_decision": (
            "Exclude the retired bridge token from current claims and preserve "
            "historical evidence unchanged."
        ),
        "disposition": "EPIC_SPECIFIC",
        "drain_targets": ["PF04 governance"],
    },
    {
        "label": "ADR-R1-004",
        "decision_point": "Checklist ownership",
        "options": [
            "Keep close mechanics in PF06 and updater discipline in HDE-DIST005.2",
            "Invent a new PF09 task or token",
        ],
        "governing_canon": ["PF06 §3.5", "PF09.6 HDE-DIST005.2"],
        "final_decision": (
            "Create no new PF09 task; PF06 owns close mechanics and "
            "HDE-DIST005.2 owns updater discipline."
        ),
        "disposition": "EPIC_SPECIFIC",
        "drain_targets": ["PF06 §3.5", "PF09.6 HDE-DIST005.2"],
    },
    {
        "label": "ADR-R1-005",
        "decision_point": "Sequencing authority",
        "options": [
            "Run DEV-01 after approval and DEV-02 after Gate B",
            "Advance without the required gate or silently revise authority",
        ],
        "governing_canon": ["Approved r5 plan", "Product Owner authorization"],
        "final_decision": (
            "DEV-01 follows approval and DEV-02 follows Gate B; changed authority "
            "requires a stop and explicit reauthorization."
        ),
        "disposition": "EPIC_SPECIFIC",
        "drain_targets": ["PF06 close-gate rules"],
    },
)

QA_CLOSEOUT_ACCOUNTING: Mapping[str, object] = {
    "accepted_deviations": [
        "qa-05 bounded remediation",
        "ADR-DEV-01 partial-cluster generation",
        "qa-08 Product-Owner-approved Extended Moon Loop",
        "qa-11 preflight deviation",
        "legacy .sh Python entrypoint naming is historical, not shell execution",
    ],
    "coverage": list(QA_CHECK_IDS),
    "doc_delta": (
        "Source-of-truth, accepted-deviation, evidence-light-source, root-cause, "
        "remediation-loop, evidence-hygiene, and Doc Delta dimensions follow "
        "PF10 HDE Build Notes Addendum 2.36."
    ),
    "evidence_light_source": (
        "PF10 §2.34 is evidence-light; its historical PF19-availability statement "
        "is stale against the current repository and permanent-canon drainage is "
        "a non-blocking follow-up."
    ),
    "historical_execution_venue": "UNKNOWN - NON-MATERIAL",
    "remediation_loop": (
        "Every execution-phase blocker remains in the canonical remediation "
        "ledger until the original predicate and all registered validators pass."
    ),
    "source_of_truth": (
        "The current matrix, QA manifest and logs, governed artifacts and proofs, "
        "Human Index, Machine Mirror, r5 scope, PF09 mapping, issues, and ADRs."
    ),
    "superseded_readiness": (
        "Execution-level READY FOR CLOSEOUT REVIEW and closeout-review READY WITH "
        "CAVEATS are superseded interim postures and do not mean SATISFIED."
    ),
}


@dataclass(frozen=True)
class TokenResult:
    token: str
    status: str
    predicate_key: str
    detail: str
    decisive_evidence: tuple[tuple[str, str], ...]
    minimum_follow_up: str

    def as_dict(self) -> dict[str, object]:
        return {
            "decisive_evidence": [
                {"kind": kind, "value": value}
                for kind, value in self.decisive_evidence
            ],
            "detail": self.detail,
            "minimum_follow_up": self.minimum_follow_up,
            "predicate_key": self.predicate_key,
            "status": self.status,
            "token": self.token,
        }


@dataclass(frozen=True)
class EvaluationSnapshot:
    token_results: tuple[TokenResult, ...]
    proof_families: tuple[Mapping[str, object], ...]
    blockers: tuple[Mapping[str, object], ...]
    obligations: tuple[Mapping[str, object], ...]
    fingerprint: str


@dataclass(frozen=True)
class _PrivateCiEvidence:
    release_state: str
    release_detail: str
    planned_state: str
    planned_detail: str


def _current_source_commit() -> str:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), "rev-parse", "HEAD"],
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError as exc:
        raise ValueError("exact source commit is unavailable") from exc
    value = result.stdout.strip()
    if (
        result.returncode != 0
        or len(value) != 40
        or any(character not in "0123456789abcdef" for character in value)
    ):
        raise ValueError("exact source commit is unavailable")
    return value


def _current_source_tree_sha256() -> str:
    try:
        inventory = subprocess.run(
            ["git", "-C", str(ROOT), "ls-tree", "-rz", "--full-tree", "HEAD"],
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        raise ValueError("exact source tree is unavailable") from exc
    if inventory.returncode != 0:
        raise ValueError("exact source tree is unavailable")
    entries: list[tuple[str, bytes]] = []
    try:
        for raw in inventory.stdout.split(b"\0"):
            if not raw:
                continue
            metadata, encoded_path = raw.split(b"\t", 1)
            _mode, object_type, object_id = metadata.split(b" ", 2)
            if object_type != b"blob":
                continue
            path = encoded_path.decode("utf-8")
            relative = Path(path)
            if (
                not path
                or relative.is_absolute()
                or ".." in relative.parts
                or relative.as_posix() != path
                or len(object_id) != 40
                or any(character not in b"0123456789abcdef" for character in object_id)
            ):
                raise ValueError
            entries.append((path, object_id))
    except (UnicodeError, ValueError) as exc:
        raise ValueError("exact source tree inventory is malformed") from exc
    entries.sort(key=lambda item: item[0])
    try:
        objects = subprocess.run(
            ["git", "-C", str(ROOT), "cat-file", "--batch"],
            input=b"".join(object_id + b"\n" for _path, object_id in entries),
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        raise ValueError("exact source tree objects are unavailable") from exc
    if objects.returncode != 0:
        raise ValueError("exact source tree objects are unavailable")
    cursor = 0
    rows: list[dict[str, object]] = []
    try:
        for path, expected_object_id in entries:
            header_end = objects.stdout.index(b"\n", cursor)
            header = objects.stdout[cursor:header_end].split(b" ")
            if (
                len(header) != 3
                or header[0] != expected_object_id
                or header[1] != b"blob"
            ):
                raise ValueError
            size = int(header[2])
            if size < 0:
                raise ValueError
            body_start = header_end + 1
            body_end = body_start + size
            if body_end >= len(objects.stdout) or objects.stdout[body_end] != 10:
                raise ValueError
            body = objects.stdout[body_start:body_end]
            rows.append(
                {
                    "path": path,
                    "sha256": hashlib.sha256(body).hexdigest(),
                    "size": len(body),
                }
            )
            cursor = body_end + 1
    except (IndexError, ValueError) as exc:
        raise ValueError("exact source tree object stream is malformed") from exc
    if cursor != len(objects.stdout):
        raise ValueError("exact source tree object stream has trailing data")
    return hashlib.sha256(_canonical_json(rows)).hexdigest()


def _private_source_worktree_paths(*arguments: str) -> frozenset[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(ROOT), *arguments],
            check=False,
            capture_output=True,
        )
    except OSError as exc:
        raise ValueError("exact source worktree inventory is unavailable") from exc
    if result.returncode != 0:
        raise ValueError("exact source worktree inventory is unavailable")
    paths: set[str] = set()
    try:
        for encoded in result.stdout.split(b"\0"):
            if not encoded:
                continue
            value = encoded.decode("utf-8")
            relative = Path(value)
            if (
                relative.is_absolute()
                or ".." in relative.parts
                or relative.as_posix() != value
            ):
                raise ValueError
            paths.add(value)
    except (UnicodeError, ValueError) as exc:
        raise ValueError("exact source worktree inventory is malformed") from exc
    return frozenset(paths)


def _validate_private_source_worktree(*, allow_generated: bool) -> None:
    changed = _private_source_worktree_paths(
        "diff",
        "--name-only",
        "-z",
        "--no-ext-diff",
        "--diff-filter=ACDMRTUXB",
        "HEAD",
        "--",
    ) | _private_source_worktree_paths(
        "ls-files", "--others", "--exclude-standard", "-z"
    )
    permitted = _PRIVATE_CI_ALLOWED_GENERATED_PATHS if allow_generated else frozenset()
    if not changed.issubset(permitted):
        raise ValueError("exact source worktree has unrelated tracked or untracked drift")


def _private_ci_root(configured: str) -> Path:
    if not configured or "\x00" in configured:
        raise ValueError("private CI root is empty or malformed")
    raw = Path(configured)
    if not raw.is_absolute() or raw.is_symlink():
        raise ValueError("private CI root must be an absolute non-symlink directory")
    try:
        resolved = raw.resolve(strict=True)
        repository_root = ROOT.resolve(strict=True)
    except OSError as exc:
        raise ValueError("private CI root is unavailable") from exc
    if resolved != raw or not resolved.is_dir():
        raise ValueError("private CI root must be a canonical directory path")
    if resolved == repository_root or repository_root in resolved.parents:
        raise ValueError("private CI root must be external to the repository")
    expected = {PRIVATE_CI_ATTESTATION_DIR, PRIVATE_CI_RECEIPT_NAME}
    try:
        children = tuple(resolved.iterdir())
    except OSError as exc:
        raise ValueError("private CI root inventory is unavailable") from exc
    names = {child.name for child in children}
    if (
        PRIVATE_CI_ATTESTATION_DIR not in names
        or not names.issubset(expected)
        or len(names) != len(children)
    ):
        raise ValueError("private CI root inventory is invalid")
    attestation_root = resolved / PRIVATE_CI_ATTESTATION_DIR
    if attestation_root.is_symlink() or not attestation_root.is_dir():
        raise ValueError("private release attestation root is invalid")
    return resolved


def _read_private_json(path: Path, label: str, *, limit: int) -> tuple[dict[str, object], bytes]:
    try:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"{label} is not a regular file")
        size = path.stat().st_size
        if size <= 0 or size > limit:
            raise ValueError(f"{label} size is invalid")
        raw = path.read_bytes()
        payload = json.loads(raw, object_pairs_hook=_unique_json_object)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        if isinstance(exc, ValueError) and str(exc).startswith(label):
            raise
        raise ValueError(f"{label} is unreadable or noncanonical") from exc
    if not isinstance(payload, dict) or raw != _canonical_json(payload):
        raise ValueError(f"{label} is unreadable or noncanonical")
    return payload, raw


def _verify_private_release_attestation_bundle(attestation_root: Path) -> None:
    try:
        from tools.evidence.build_release_attestation import (
            AttestationBuildError,
            verify_attestation,
        )
    except ImportError as exc:
        raise ValueError("private release attestation bundle is unverifiable") from exc
    try:
        verify_attestation(attestation_root, require_exact=False, source=ROOT)
    except AttestationBuildError as exc:
        raise ValueError(
            f"private release attestation bundle invalid: {exc.code}"
        ) from exc
    except (OSError, RuntimeError, ValueError) as exc:
        raise ValueError("private release attestation bundle is unverifiable") from exc


def _private_execution_receipt_payload(
    attestation: Mapping[str, object],
    attestation_bytes: bytes,
    *,
    event_name: str,
    run_id: str,
    run_attempt: str,
    source_commit: str,
) -> dict[str, object]:
    return {
        "closed_rails": dict(sorted(PRIVATE_CI_EXECUTION_RAILS.items())),
        "command_results": [
            {"command": command, "exit_code": 0, "result": "PASS"}
            for command in PRIVATE_CI_COMMANDS
        ],
        "contract": PRIVATE_CI_CONTRACT,
        "epic_id": EPIC_ID,
        "event_name": event_name,
        "job": PRIVATE_CI_JOB,
        "manifest_sha256": attestation.get("manifest_sha256"),
        "provider": "github-actions",
        "release_attestation_sha256": hashlib.sha256(attestation_bytes).hexdigest(),
        "repository": PRIVATE_CI_REPOSITORY,
        "result": "PASS",
        "run_attempt": run_attempt,
        "run_id": run_id,
        "source_commit": source_commit,
        "source_commit_exact": True,
        "source_tree_sha256": attestation.get("source_tree_sha256"),
        "version": 1,
        "workflow_path": PRIVATE_CI_WORKFLOW_PATH,
    }


def _positive_decimal(value: object) -> bool:
    return (
        isinstance(value, str)
        and value.isascii()
        and value.isdecimal()
        and str(int(value)) == value
        and int(value) > 0
    )


def _validate_private_execution_receipt(
    payload: Mapping[str, object],
    *,
    attestation: Mapping[str, object],
    attestation_bytes: bytes,
    source_commit: str,
    manifest_sha256: str,
) -> None:
    expected_fields = {
        "closed_rails",
        "command_results",
        "contract",
        "epic_id",
        "event_name",
        "job",
        "manifest_sha256",
        "provider",
        "release_attestation_sha256",
        "repository",
        "result",
        "run_attempt",
        "run_id",
        "source_commit",
        "source_commit_exact",
        "source_tree_sha256",
        "version",
        "workflow_path",
    }
    expected_commands = [
        {"command": command, "exit_code": 0, "result": "PASS"}
        for command in PRIVATE_CI_COMMANDS
    ]
    if set(payload) != expected_fields:
        raise ValueError("private execution receipt field roster mismatch")
    required = {
        "closed_rails": dict(sorted(PRIVATE_CI_EXECUTION_RAILS.items())),
        "command_results": expected_commands,
        "contract": PRIVATE_CI_CONTRACT,
        "epic_id": EPIC_ID,
        "job": PRIVATE_CI_JOB,
        "manifest_sha256": manifest_sha256,
        "provider": "github-actions",
        "release_attestation_sha256": hashlib.sha256(attestation_bytes).hexdigest(),
        "repository": PRIVATE_CI_REPOSITORY,
        "result": "PASS",
        "source_commit": source_commit,
        "source_commit_exact": True,
        "source_tree_sha256": attestation.get("source_tree_sha256"),
        "version": 1,
        "workflow_path": PRIVATE_CI_WORKFLOW_PATH,
    }
    for key, expected in required.items():
        if payload.get(key) != expected:
            raise ValueError(f"private execution receipt mismatch: {key}")
    if payload.get("event_name") not in {"pull_request", "push"}:
        raise ValueError("private execution receipt mismatch: event_name")
    if not _positive_decimal(payload.get("run_id")) or not _positive_decimal(
        payload.get("run_attempt")
    ):
        raise ValueError("private execution receipt run identity mismatch")
    if not _hex64(payload.get("source_tree_sha256")):
        raise ValueError("private execution receipt mismatch: source_tree_sha256")


def _github_api_bytes(
    endpoint: str,
    *,
    accept: str,
    limit: int,
    allow_redirect: bool,
) -> bytes:
    prefix = f"/repos/{PRIVATE_CI_REPOSITORY}/actions/"
    if (
        not endpoint.startswith(prefix)
        or "\x00" in endpoint
        or "?" in endpoint
        or "#" in endpoint
        or limit <= 0
    ):
        raise ValueError("private GitHub API endpoint is invalid")
    token = os.environ.get("GH_TOKEN", "")
    if (
        len(token) < 20
        or len(token) > 4096
        or any(character.isspace() for character in token)
        or "\x00" in token
    ):
        raise ValueError("private GitHub API credential is unavailable")
    url = f"{PRIVATE_CI_API_ORIGIN}{endpoint}"
    request = urllib.request.Request(url, method="GET")
    # This header is deliberately not forwarded to the artifact-storage
    # redirect target. The signed redirect authenticates the archive download.
    request.add_unredirected_header("Authorization", f"Bearer {token}")
    request.add_header("Accept", accept)
    request.add_header("X-GitHub-Api-Version", PRIVATE_CI_API_VERSION)
    request.add_header("User-Agent", "glow-hde-epic038-private-ci-verifier")
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = response.getcode()
            final_url = response.geturl()
            raw = response.read(limit + 1)
    except (OSError, TimeoutError, urllib.error.URLError) as exc:
        raise ValueError("private GitHub API request failed") from exc
    parsed = urllib.parse.urlsplit(final_url)
    if (
        status != 200
        or parsed.scheme != "https"
        or not parsed.hostname
        or (not allow_redirect and final_url != url)
        or len(raw) == 0
        or len(raw) > limit
    ):
        raise ValueError("private GitHub API response is invalid")
    return raw


def _github_api_json(endpoint: str, *, limit: int) -> dict[str, object]:
    raw = _github_api_bytes(
        endpoint,
        accept="application/vnd.github+json",
        limit=limit,
        allow_redirect=False,
    )
    try:
        payload = json.loads(raw, object_pairs_hook=_unique_json_object)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("private GitHub API JSON is malformed") from exc
    if not isinstance(payload, dict):
        raise ValueError("private GitHub API JSON is malformed")
    return payload


def _private_ci_archive_files(raw: bytes) -> dict[str, bytes]:
    if not raw or len(raw) > PRIVATE_CI_ARCHIVE_LIMIT:
        raise ValueError("private execution artifact archive size is invalid")
    files: dict[str, bytes] = {}
    names: set[str] = set()
    total_size = 0
    try:
        with zipfile.ZipFile(io.BytesIO(raw), mode="r") as archive:
            infos = archive.infolist()
            if not infos or len(infos) > PRIVATE_CI_ARCHIVE_ENTRY_LIMIT:
                raise ValueError("private execution artifact inventory is invalid")
            for info in infos:
                name = info.filename
                if name in names:
                    raise ValueError("private execution artifact has duplicate paths")
                names.add(name)
                if info.is_dir():
                    if name != f"{PRIVATE_CI_ATTESTATION_DIR}/":
                        raise ValueError("private execution artifact directory is invalid")
                    continue
                relative = Path(name)
                if (
                    not name
                    or "\x00" in name
                    or "\\" in name
                    or relative.is_absolute()
                    or ".." in relative.parts
                    or relative.as_posix() != name
                    or not (
                        name == PRIVATE_CI_RECEIPT_NAME
                        or (
                            len(relative.parts) > 1
                            and relative.parts[0] == PRIVATE_CI_ATTESTATION_DIR
                        )
                    )
                ):
                    raise ValueError("private execution artifact path is invalid")
                mode = (info.external_attr >> 16) & 0xFFFF
                if (
                    info.flag_bits & 0x1
                    or stat.S_ISLNK(mode)
                    or stat.S_IFMT(mode) not in {0, stat.S_IFREG}
                    or info.file_size < 0
                    or info.file_size > PRIVATE_CI_ARCHIVE_FILE_LIMIT
                    or info.compress_size < 0
                    or (
                        info.file_size > 0
                        and (
                            info.compress_size == 0
                            or info.file_size > info.compress_size * 1000
                        )
                    )
                ):
                    raise ValueError("private execution artifact member is invalid")
                total_size += info.file_size
                if total_size > PRIVATE_CI_ARCHIVE_TOTAL_LIMIT:
                    raise ValueError("private execution artifact expansion is invalid")
                body = archive.read(info)
                if len(body) != info.file_size:
                    raise ValueError("private execution artifact member is truncated")
                files[name] = body
    except (OSError, RuntimeError, zipfile.BadZipFile) as exc:
        raise ValueError("private execution artifact archive is invalid") from exc
    if (
        PRIVATE_CI_RECEIPT_NAME not in files
        or f"{PRIVATE_CI_ATTESTATION_DIR}/attestation.json" not in files
    ):
        raise ValueError("private execution artifact required files are missing")
    return files


def _authenticated_private_ci_files() -> dict[str, bytes]:
    artifact_id = os.environ.get(PRIVATE_CI_ARTIFACT_ID_ENV, "")
    artifact_digest = os.environ.get(PRIVATE_CI_ARTIFACT_DIGEST_ENV, "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    if (
        os.environ.get("GITHUB_ACTIONS") != "true"
        or os.environ.get("GITHUB_REPOSITORY") != PRIVATE_CI_REPOSITORY
        or os.environ.get("GITHUB_WORKFLOW") != "ci"
        or os.environ.get("GITHUB_JOB") != PRIVATE_CI_JOB
        or event_name not in {"pull_request", "push"}
        or not _positive_decimal(artifact_id)
        or not _hex64(artifact_digest)
        or not _positive_decimal(run_id)
        or not _positive_decimal(run_attempt)
        or os.environ.get("SAFE_MODE") != "1"
        or os.environ.get("ALLOW_NETWORK") != "1"
        or any(
            os.environ.get(key) != value
            for key, value in PRIVATE_CI_EXECUTION_RAILS.items()
            if key not in {"ALLOW_NETWORK"}
        )
    ):
        raise ValueError("private execution artifact consumer identity mismatch")
    source_commit = _current_source_commit()
    artifact_name = (
        f"{PRIVATE_CI_ARTIFACT_PREFIX}-{source_commit}-{run_id}-{run_attempt}"
    )
    artifact_endpoint = (
        f"/repos/{PRIVATE_CI_REPOSITORY}/actions/artifacts/{artifact_id}"
    )
    metadata = _github_api_json(artifact_endpoint, limit=1024 * 1024)
    workflow_run = metadata.get("workflow_run")
    expected_server_digest = f"sha256:{artifact_digest}"
    if (
        metadata.get("id") != int(artifact_id)
        or metadata.get("name") != artifact_name
        or metadata.get("expired") is not False
        or metadata.get("digest") != expected_server_digest
        or not isinstance(metadata.get("size_in_bytes"), int)
        or isinstance(metadata.get("size_in_bytes"), bool)
        or not 0 < int(metadata["size_in_bytes"]) <= PRIVATE_CI_ARCHIVE_LIMIT
        or not isinstance(workflow_run, dict)
        or workflow_run.get("id") != int(run_id)
        or workflow_run.get("repository_id") != PRIVATE_CI_REPOSITORY_ID
        or workflow_run.get("head_repository_id") != PRIVATE_CI_REPOSITORY_ID
        or not isinstance(workflow_run.get("head_branch"), str)
        or not workflow_run.get("head_branch")
        or workflow_run.get("head_sha") != source_commit
        or not (
            isinstance(workflow_run.get("head_sha"), str)
            and len(str(workflow_run["head_sha"])) == 40
            and all(
                character in "0123456789abcdef"
                for character in str(workflow_run["head_sha"])
            )
        )
    ):
        raise ValueError("private execution artifact metadata mismatch")
    attempt_endpoint = (
        f"/repos/{PRIVATE_CI_REPOSITORY}/actions/runs/{run_id}/attempts/"
        f"{run_attempt}"
    )
    attempt = _github_api_json(attempt_endpoint, limit=2 * 1024 * 1024)
    repository = attempt.get("repository")
    head_repository = attempt.get("head_repository")
    workflow_path = attempt.get("path")
    workflow_path_matches = workflow_path == PRIVATE_CI_WORKFLOW_PATH
    if isinstance(workflow_path, str) and workflow_path.startswith(
        f"{PRIVATE_CI_WORKFLOW_PATH}@"
    ):
        workflow_ref = workflow_path.removeprefix(
            f"{PRIVATE_CI_WORKFLOW_PATH}@"
        )
        workflow_path_matches = bool(
            workflow_ref
            and len(workflow_ref) <= 255
            and re.fullmatch(r"[A-Za-z0-9._/-]+", workflow_ref)
            and ".." not in workflow_ref
            and "//" not in workflow_ref
            and not workflow_ref.startswith(('/', '.'))
            and not workflow_ref.endswith(('/', '.', '.lock'))
        )
    if (
        attempt.get("id") != int(run_id)
        or attempt.get("run_attempt") != int(run_attempt)
        or attempt.get("event") != event_name
        or not workflow_path_matches
        or attempt.get("head_sha") != workflow_run.get("head_sha")
        or attempt.get("head_branch") != workflow_run.get("head_branch")
        or not isinstance(repository, dict)
        or repository.get("id") != PRIVATE_CI_REPOSITORY_ID
        or repository.get("full_name") != PRIVATE_CI_REPOSITORY
        or not isinstance(head_repository, dict)
        or head_repository.get("id") != PRIVATE_CI_REPOSITORY_ID
        or head_repository.get("full_name") != PRIVATE_CI_REPOSITORY
    ):
        raise ValueError("private execution workflow-run attempt mismatch")
    archive = _github_api_bytes(
        f"{artifact_endpoint}/zip",
        accept="application/vnd.github+json",
        limit=PRIVATE_CI_ARCHIVE_LIMIT,
        allow_redirect=True,
    )
    if (
        len(archive) != metadata["size_in_bytes"]
        or hashlib.sha256(archive).hexdigest() != artifact_digest
    ):
        raise ValueError("private execution artifact archive digest mismatch")
    files = _private_ci_archive_files(archive)
    receipt_bytes = files[PRIVATE_CI_RECEIPT_NAME]
    try:
        receipt = json.loads(
            receipt_bytes, object_pairs_hook=_unique_json_object
        )
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError("private execution artifact receipt is malformed") from exc
    if (
        not isinstance(receipt, dict)
        or receipt_bytes != _canonical_json(receipt)
        or receipt.get("run_id") != run_id
        or receipt.get("run_attempt") != run_attempt
        or receipt.get("event_name") != event_name
    ):
        raise ValueError("private execution artifact receipt run mismatch")
    return files


def _materialize_private_ci_files(files: Mapping[str, bytes], root: Path) -> None:
    for name, body in sorted(files.items()):
        target = root / name
        target.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        descriptor: int | None = None
        try:
            descriptor = os.open(
                target,
                os.O_WRONLY | os.O_CREAT | os.O_EXCL,
                0o600,
            )
            with os.fdopen(descriptor, "wb") as stream:
                descriptor = None
                stream.write(body)
        finally:
            if descriptor is not None:
                os.close(descriptor)


def _private_ci_evidence_from_root(
    root: Path, *, authenticated_receipt: bool
) -> _PrivateCiEvidence:
    try:
        root = _private_ci_root(str(root))
        attestation_root = root / PRIVATE_CI_ATTESTATION_DIR
        _validate_private_source_worktree(allow_generated=True)
        _verify_private_release_attestation_bundle(attestation_root)
        attestation, attestation_bytes = _read_private_json(
            attestation_root / "attestation.json",
            "private release attestation",
            limit=1024 * 1024,
        )
        source_commit = _current_source_commit()
        source_tree_sha256 = _current_source_tree_sha256()
        manifest_bytes = (ROOT / RELEASE_MANIFEST_PATH).read_bytes()
        manifest_sha256 = hashlib.sha256(manifest_bytes).hexdigest()
        validate_release_attestation_payload(
            attestation,
            expected_source_commit=source_commit,
            manifest_sha256=manifest_sha256,
        )
        if attestation.get("source_tree_sha256") != source_tree_sha256:
            raise ValueError("release attestation mismatch: source_tree_sha256")
    except (OSError, UnicodeError, ValueError):
        return _PrivateCiEvidence(
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
        )
    receipt_path = root / PRIVATE_CI_RECEIPT_NAME
    if not receipt_path.exists() and not receipt_path.is_symlink():
        return _PrivateCiEvidence(
            "ATTESTED",
            PRIVATE_CI_ATTESTATION_PASS_DETAIL,
            "ABSENT",
            "no private external exact-command CI receipt was supplied",
        )
    if not authenticated_receipt:
        return _PrivateCiEvidence(
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
        )
    try:
        receipt, _receipt_bytes = _read_private_json(
            receipt_path,
            "private execution receipt",
            limit=128 * 1024,
        )
        _validate_private_execution_receipt(
            receipt,
            attestation=attestation,
            attestation_bytes=attestation_bytes,
            source_commit=source_commit,
            manifest_sha256=manifest_sha256,
        )
    except (OSError, UnicodeError, ValueError):
        return _PrivateCiEvidence(
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
        )
    return _PrivateCiEvidence(
        "PASS",
        PRIVATE_CI_ATTESTATION_PASS_DETAIL,
        "PASS",
        PRIVATE_CI_RECEIPT_PASS_DETAIL,
    )


def _private_ci_evidence() -> _PrivateCiEvidence:
    configured = os.environ.get(PRIVATE_CI_ROOT_ENV)
    artifact_configuration = (
        os.environ.get(PRIVATE_CI_ARTIFACT_ID_ENV),
        os.environ.get(PRIVATE_CI_ARTIFACT_DIGEST_ENV),
    )
    if any(value is not None for value in artifact_configuration):
        if configured is not None or not all(artifact_configuration):
            return _PrivateCiEvidence(
                "FAIL",
                PRIVATE_CI_INVALID_DETAIL,
                "FAIL",
                PRIVATE_CI_INVALID_DETAIL,
            )
        try:
            files = _authenticated_private_ci_files()
            if (
                PRIVATE_CI_RECEIPT_NAME not in files
                or f"{PRIVATE_CI_ATTESTATION_DIR}/attestation.json" not in files
            ):
                raise ValueError("authenticated private artifact is incomplete")
            with tempfile.TemporaryDirectory(
                prefix="hde-epic038-authenticated-receipt-"
            ) as temporary:
                root = Path(temporary)
                os.chmod(root, 0o700)
                _materialize_private_ci_files(files, root)
                return _private_ci_evidence_from_root(
                    root, authenticated_receipt=True
                )
        except (OSError, UnicodeError, ValueError):
            return _PrivateCiEvidence(
                "FAIL",
                PRIVATE_CI_INVALID_DETAIL,
                "FAIL",
                PRIVATE_CI_INVALID_DETAIL,
            )
    if configured is None:
        return _PrivateCiEvidence(
            "ABSENT",
            "no private external exact-source release attestation was supplied",
            "ABSENT",
            "no private external exact-command CI receipt was supplied",
        )
    return _private_ci_evidence_from_root(
        Path(configured), authenticated_receipt=False
    )


def _write_private_ci_receipt() -> Path:
    configured = os.environ.get(PRIVATE_CI_ROOT_ENV)
    if configured is None:
        raise ValueError("private CI root was not supplied")
    root = _private_ci_root(configured)
    receipt_path = root / PRIVATE_CI_RECEIPT_NAME
    if receipt_path.exists() or {path.name for path in root.iterdir()} != {
        PRIVATE_CI_ATTESTATION_DIR
    }:
        raise ValueError("private CI root is not an empty receipt destination")
    if (
        os.environ.get("GITHUB_ACTIONS") != "true"
        or os.environ.get("GITHUB_REPOSITORY") != PRIVATE_CI_REPOSITORY
        or os.environ.get("GITHUB_WORKFLOW") != "ci"
        or os.environ.get("GITHUB_JOB") != PRIVATE_CI_JOB
    ):
        raise ValueError("private execution receipt producer identity mismatch")
    event_name = os.environ.get("GITHUB_EVENT_NAME", "")
    run_id = os.environ.get("GITHUB_RUN_ID", "")
    run_attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    if event_name not in {"pull_request", "push"} or not _positive_decimal(
        run_id
    ) or not _positive_decimal(run_attempt):
        raise ValueError("private execution receipt run identity mismatch")
    if any(
        os.environ.get(key) != value
        for key, value in PRIVATE_CI_EXECUTION_RAILS.items()
    ):
        raise ValueError("private execution receipt producer rails mismatch")
    _validate_private_source_worktree(allow_generated=False)
    evidence = _private_ci_evidence()
    if evidence.release_state != "ATTESTED" or evidence.planned_state != "ABSENT":
        raise ValueError("private exact-source attestation is not ready for receipt production")
    attestation, attestation_bytes = _read_private_json(
        root / PRIVATE_CI_ATTESTATION_DIR / "attestation.json",
        "private release attestation",
        limit=1024 * 1024,
    )
    source_commit = _current_source_commit()
    payload = _private_execution_receipt_payload(
        attestation,
        attestation_bytes,
        event_name=event_name,
        run_id=run_id,
        run_attempt=run_attempt,
        source_commit=source_commit,
    )
    manifest_sha256 = hashlib.sha256(
        (ROOT / RELEASE_MANIFEST_PATH).read_bytes()
    ).hexdigest()
    _validate_private_execution_receipt(
        payload,
        attestation=attestation,
        attestation_bytes=attestation_bytes,
        source_commit=source_commit,
        manifest_sha256=manifest_sha256,
    )
    raw = _canonical_json(payload)
    descriptor: int | None = None
    try:
        descriptor = os.open(
            receipt_path,
            os.O_WRONLY | os.O_CREAT | os.O_EXCL,
            0o600,
        )
        with os.fdopen(descriptor, "wb") as stream:
            descriptor = None
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        if receipt_path.read_bytes() != raw or receipt_path.stat().st_mode & 0o077:
            raise OSError("private receipt write verification failed")
    except BaseException:
        if descriptor is not None:
            os.close(descriptor)
        receipt_path.unlink(missing_ok=True)
        raise
    return receipt_path


def _json_object(path: str) -> dict[str, object]:
    try:
        value = json.loads(
            (ROOT / path).read_text(encoding="utf-8"),
            object_pairs_hook=_unique_json_object,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"invalid JSON artifact: {path}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"JSON artifact must be an object: {path}")
    return value


def _qa_manifest() -> dict[str, object]:
    payload = _json_object(QA_MANIFEST_PATH)
    if tuple(payload) != QA_CHECK_IDS:
        raise ValueError("QA manifest roster/order mismatch")
    raw = (ROOT / QA_MANIFEST_PATH).read_bytes()
    if raw != _canonical_json(payload):
        raise ValueError("QA manifest is not canonical JSON")
    return payload


def _validate_qa_receipt(check_id: str) -> None:
    manifest = _qa_manifest()
    record = manifest.get(check_id)
    expected_path = f"checks/{check_id}/primary.log"
    if (
        not isinstance(record, dict)
        or set(record) != {"check_id", "log_path", "sha256", "size_bytes", "status"}
        or record.get("check_id") != check_id
        or record.get("log_path") != expected_path
        or record.get("status") != "PASS"
    ):
        raise ValueError(f"QA receipt metadata mismatch: {check_id}")
    path = ROOT / "audit/qa/hde-epic038" / expected_path
    try:
        raw = path.read_bytes()
        header = json.loads(raw.splitlines()[0], object_pairs_hook=_unique_json_object)
    except (OSError, IndexError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"QA receipt unavailable: {check_id}") from exc
    if (
        record.get("sha256") != hashlib.sha256(raw).hexdigest()
        or record.get("size_bytes") != len(raw)
        or not isinstance(header, dict)
        or header.get("check_id") != check_id
        or header.get("status") != "PASS"
        or header.get("exit_code") != 0
        or header.get("claimed_tokens") != []
    ):
        raise ValueError(f"QA receipt current-state mismatch: {check_id}")


def _validate_finalized_qa_state() -> None:
    manifest = _qa_manifest()
    for check_id in QA_CHECK_IDS:
        _validate_qa_receipt(check_id)
    _validate_proof(QA_MANIFEST_PATH, f"{QA_MANIFEST_PATH}.path_proof.txt")
    records = _mirror_records()
    if (
        QA_MANIFEST_KEY,
        QA_MANIFEST_PATH,
        f"{QA_MANIFEST_PATH}.path_proof.txt",
    ) not in records:
        raise ValueError("QA manifest missing exact Machine Mirror binding")
    human = _human_items()
    matches = [
        item
        for item in human
        if item.get("artifact_key") == QA_MANIFEST_KEY
        and item.get("discovered_physical_path") == QA_MANIFEST_PATH
    ]
    if len(matches) != 1:
        raise ValueError("QA manifest missing exact Human Index binding")
    summary = (ROOT / QA_RCA_PATH).read_text(encoding="utf-8")
    required = (
        "# HDE-EPIC038 QA RCA and Doc Delta Summary",
        "## Coverage versus QA Plan",
        "qa-00-step-0-discovery",
        "qa-23-po-023",
        "READY FOR CLOSEOUT REVIEW",
        "Formal close-pack completion: NOT CLAIMED",
    )
    if any(item not in summary for item in required):
        raise ValueError("QA RCA/current-state summary is stale or incomplete")


def _validate_row_bindings(row: Row) -> None:
    mirror = tuple(_mirror_items())
    human = tuple(_human_items())
    for key, path, proof in zip(
        row.artifact_keys, row.primary_evidence, row.proof_anchors
    ):
        if not (ROOT / path).is_file() or not (ROOT / proof).is_file():
            raise ValueError(f"missing governed evidence family: {row.token}: {path}")
        _validate_proof(path, proof)
        mirror_matches = [
            item
            for item in mirror
            if item.get("artifact_key") == key
            and item.get("discovered_physical_path") == path
            and item.get("proof_anchor") == proof
        ]
        human_matches = [
            item
            for item in human
            if item.get("artifact_key") == key
            and item.get("discovered_physical_path") == path
        ]
        if len(mirror_matches) != 1 or len(human_matches) != 1:
            raise ValueError(
                f"missing or duplicate Human Index/Machine Mirror binding: "
                f"{row.token}: {key}"
            )
        body = (ROOT / path).read_bytes()
        expected_sha = (
            _mirror_body_sha256()
            if path == MACHINE_MIRROR_PATH
            else hashlib.sha256(body).hexdigest()
        )
        expected = (expected_sha, len(body))
        match = mirror_matches[0]
        if match.get("sha256") != expected[0] or match.get("size_bytes") != expected[1]:
            raise ValueError(f"stale Machine Mirror binding: {row.token}: {key}")


def _proof_family_records(rows: Sequence[Row]) -> tuple[Mapping[str, object], ...]:
    result: list[Mapping[str, object]] = []
    for row in rows:
        for key, path, proof in zip(
            row.artifact_keys, row.primary_evidence, row.proof_anchors
        ):
            result.append(
                {
                    "artifact_key": key,
                    "classification": row.classification,
                    "epic_id": row.epic_id,
                    "primary_evidence": path,
                    "proof_anchor": proof,
                    "token": row.token,
                }
            )
    expected_count = sum(len(row.primary_evidence) for row in rows)
    identities = [
        (item["token"], item["artifact_key"], item["primary_evidence"], item["proof_anchor"])
        for item in result
    ]
    if len(result) != expected_count or len(identities) != len(set(identities)):
        raise ValueError("reduced or duplicate proof-family roster")
    return tuple(result)


def _validate_live_qa(row: Row) -> None:
    if row.live_qa.startswith("N/A:"):
        if len(row.live_qa.removeprefix("N/A:").strip()) < 20:
            raise ValueError(f"insubstantive Live QA N/A: {row.token}")
        return
    for check_id in row.live_qa.split("; "):
        _validate_qa_receipt(check_id)


def _semantic_doc_delta(_row: Row) -> str:
    validate_doc_delta_evidence()
    return "current canonical Doc Delta pair and historical provenance validate"


def _semantic_human_index(_row: Row) -> str:
    validate_index_mirror_topology()
    return "current Human Index topology validates against the Machine Mirror"


def _semantic_machine_mirror(_row: Row) -> str:
    validate_index_mirror_topology()
    validate_all_mirror_proofs()
    return "current Machine Mirror topology, paths, digests, and proofs validate"


def _semantic_index_hash(_row: Row) -> str:
    index_bytes = (ROOT / HUMAN_INDEX_PATH).read_bytes()
    expected = (
        f"{hashlib.sha256(index_bytes).hexdigest()}  {HUMAN_INDEX_PATH}\n".encode()
    )
    if (ROOT / "docs/evidence/INDEX.sha256").read_bytes() != expected:
        raise ValueError("Human Index hash sentinel mismatch")
    return "current Human Index hash sentinel validates"


def _semantic_env(row: Row) -> str:
    payload = _json_object("artifacts/runtime/env_matrix.snapshot.json")
    rails = payload.get("default_rails")
    pins = payload.get("determinism_pins")
    if (
        payload.get("schema_version") != 3
        or not isinstance(rails, dict)
        or rails.get("dev") != {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"}
        or rails.get("stage") != {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"}
        or rails.get("CI") != {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"}
        or rails.get("prod") != {"ALLOW_NETWORK": "1", "SAFE_MODE": "0"}
        or pins != {"LANG": "C", "LC_ALL": "C", "TZ": "UTC"}
    ):
        raise ValueError(f"environment predicate mismatch: {row.token}")
    predicate = (
        "closed-rails environment policy validates"
        if row.token == "ENV_RAILS_POLICY_OK"
        else "LC_ALL=C determinism pin validates"
    )
    return predicate


def _semantic_preimage(_row: Row) -> str:
    validate_preimage_payload(
        _json_object(PREIMAGE_PATH), (ROOT / PREIMAGE_SOURCE_PATH).read_bytes()
    )
    return "stored and recomputed canonical preimage hashes are identical"


def _semantic_cli_reader(_row: Row) -> str:
    validate_cli_reader_parity_payload(_json_object(PREIMAGE_PATH))
    return "current CLI and Reader canonical bytes are identical"


def _key_value_lines(path: str, keys: tuple[str, ...]) -> dict[str, str]:
    lines = (ROOT / path).read_text(encoding="utf-8").splitlines()
    if len(lines) != len(keys) or any("=" not in line for line in lines):
        raise ValueError(f"structured log shape mismatch: {path}")
    result = dict(line.split("=", 1) for line in lines)
    if tuple(result) != keys:
        raise ValueError(f"structured log field order mismatch: {path}")
    return result


def _semantic_abba(_row: Row) -> str:
    payload = _key_value_lines(
        "audit/gates/determinism/abba.bytes",
        ("ab_sha256", "ba_sha256", "byte_identity"),
    )
    if (
        not _hex64(payload["ab_sha256"])
        or payload["ab_sha256"] != payload["ba_sha256"]
        or payload["byte_identity"] != "true"
    ):
        raise ValueError("ABBA identity predicate mismatch")
    return "current AB and BA canonical byte hashes are identical"


def _semantic_two_run(_row: Row) -> str:
    payload = _key_value_lines(
        "audit/gates/determinism/tworun_identity.sha256",
        ("run1_sha256", "run2_sha256", "byte_identity"),
    )
    if (
        not _hex64(payload["run1_sha256"])
        or payload["run1_sha256"] != payload["run2_sha256"]
        or payload["byte_identity"] != "true"
    ):
        raise ValueError("two-run identity predicate mismatch")
    return "current repeated-run canonical byte hashes are identical"


def _semantic_json_gate(_row: Row) -> str:
    payload = _json_object(
        "audit/gates/json_gate/canonical/json_gate_structured_record.json"
    )
    if (
        payload.get("schema") != "canonical_json.gate.v1"
        or payload.get("status") != "pass"
        or payload.get("failures") != []
        or payload.get("env")
        != {
            "ALLOW_NETWORK": "0",
            "LANG": "C",
            "LC_ALL": "C",
            "SAFE_MODE": "1",
            "TZ": "UTC",
        }
    ):
        raise ValueError("canonical JSON gate predicate mismatch")
    return "current canonical JSON gate structured record validates"


def _a7_payload() -> dict[str, object]:
    return _json_object("artifacts/proofs/reader_success_get_head_304.json")


def _semantic_a7(row: Row) -> str:
    payload = _a7_payload()
    get = payload.get("get_200")
    head = payload.get("head_200")
    after = payload.get("after_304")
    encodings = payload.get("tested_encodings")
    flags = payload.get("vary_flags")
    if not all(isinstance(item, dict) for item in (get, head, after, flags)):
        raise ValueError("A7 composite proof shape mismatch")
    etag = payload.get("etag")
    quoted = (
        isinstance(etag, str)
        and len(etag) == 66
        and etag.startswith('"')
        and etag.endswith('"')
        and _hex64(etag[1:-1])
    )
    predicates: Mapping[str, bool] = {
        "A7_GET_QUOTED_ETAG_OK": bool(
            quoted
            and get.get("pass") is True
            and get.get("status") == 200
            and get.get("etag") == etag
            and get.get("body_sha256") == etag[1:-1]
        ),
        "A7_HEAD_PARITY_OK": bool(
            head.get("pass") is True
            and head.get("status") == 200
            and head.get("body_empty") is True
            and head.get("etag") == get.get("etag")
            and head.get("content_length") == get.get("content_length")
            and head.get("content_type") == get.get("content_type")
        ),
        "A7_304_OMITS_CT_CL_OK": bool(
            after.get("pass") is True
            and after.get("status") == 304
            and after.get("body_empty") is True
            and after.get("content_type_absent") is True
            and after.get("content_length_absent") is True
            and after.get("entity_headers_absent") is True
        ),
        "A7_VARY_AUTH_AE_OK": bool(
            flags == {"accept_encoding": True, "authorization": True}
            and get.get("vary") == "Authorization, Accept-Encoding"
            and head.get("vary") == get.get("vary")
            and after.get("vary") == get.get("vary")
        ),
        "A7_ENCODING_INVARIANCE_OK": bool(
            isinstance(encodings, list)
            and [item.get("accept_encoding") for item in encodings]
            == ["identity", "gzip", "br"]
            and all(
                isinstance(item, dict)
                and item.get("content_encoding") == "identity"
                and item.get("etag") == etag
                and item.get("head_identity_length") == get.get("content_length")
                for item in encodings
            )
        ),
        "A7_TRANSPORT_PROOF_OK": bool(
            payload.get("route_path") == "/reader"
            and get.get("pass") is True
            and head.get("pass") is True
            and after.get("pass") is True
            and quoted
        ),
    }
    if predicates.get(row.token) is not True:
        raise ValueError(f"A7 token-specific predicate mismatch: {row.token}")
    return f"current A7 composite predicate validates for {row.token}"


def _semantic_endpoint_catalog(_row: Row) -> str:
    payload = _json_object("docs/ENDPOINTS_CATALOG.json")
    endpoints = payload.get("endpoints")
    if not isinstance(endpoints, list) or not endpoints:
        raise ValueError("endpoint catalog is empty")
    identities = [
        (item.get("method"), item.get("path"))
        for item in endpoints
        if isinstance(item, dict)
    ]
    reader = [
        item
        for item in endpoints
        if isinstance(item, dict) and item.get("path") == "/reader"
    ]
    if (
        len(identities) != len(endpoints)
        or len(identities) != len(set(identities))
        or {(item.get("method"), item.get("env_gate"), item.get("a7_eligible")) for item in reader}
        != {("GET", "APP_ENV=dev", True), ("HEAD", "APP_ENV=dev", True)}
        or payload.get("success_endpoints") != [{"method": "GET", "path": "/reader"}]
    ):
        raise ValueError("endpoint catalog predicate mismatch")
    return "current endpoint catalog has exact unique reader bindings"


def _semantic_endpoint_env_gate(_row: Row) -> str:
    expected = (
        "APP_ENV=prod\n"
        "/reader_success_unreachable=true\n"
        "cache_control=no-store\n"
        "etag_absent=true\n"
    )
    if (ROOT / "artifacts/proofs/endpoints_env_gate_proof.log").read_text(
        encoding="utf-8"
    ) != expected:
        raise ValueError("endpoint environment-gate proof mismatch")
    return "current production environment-gate refusal proof validates"


def _semantic_index_mirror(_row: Row) -> str:
    validate_index_mirror_topology()
    _validate_finalized_qa_state()
    return "current Human Index/Machine Mirror topology and QA binding validate"


def _semantic_paths(_row: Row) -> str:
    validate_mirror_paths()
    _validate_finalized_qa_state()
    return "every current Machine Mirror physical path resolves inside the repository"


def _semantic_db(row: Row) -> str:
    validate_db_posture_payload(row.token, _json_object(DB_POSTURE_PATH))
    return f"current database posture predicate validates for {row.token}"


def _semantic_db_connection(_row: Row) -> str:
    payload = _json_object("artifacts/runtime/direct_db_selection.snapshot.json")
    predicates = payload.get("predicates")
    cases = payload.get("cases")
    required = {
        "alternate_transport_attempts_zero",
        "direct_only_provider",
        "missing_direct_fails_closed",
        "retired_keys_fail_before_provider_attempt",
        "secret_values_absent",
        "unavailable_direct_fails_closed",
    }
    if (
        payload.get("schema") != "hde_epic038.direct_db_selection.v1"
        or payload.get("result") != "PASS"
        or payload.get("failure") is not None
        or not isinstance(predicates, dict)
        or set(predicates) != required
        or any(value is not True for value in predicates.values())
        or not isinstance(cases, list)
        or len(cases) != 4
        or any(not isinstance(item, dict) or item.get("result") != "PASS" for item in cases)
    ):
        raise ValueError("direct database selection predicate mismatch")
    return "current direct-only database selection and fail-closed cases validate"


def _semantic_all_proofs(_row: Row) -> str:
    validate_all_mirror_proofs()
    _validate_finalized_qa_state()
    return "every current Machine Mirror proof family validates"


def _semantic_mirror_schema(_row: Row) -> str:
    validate_index_mirror_topology()
    validate_all_mirror_proofs()
    return "current mirror schema topology and record bindings validate"


def _semantic_final_lf(_row: Row) -> str:
    manifest = _qa_manifest()
    validate_final_lf_evidence(
        manifest, (ROOT / FINAL_LF_LOG_PATH).read_text(encoding="utf-8")
    )
    validate_final_lf_script((ROOT / FINAL_LF_SCRIPT_PATH).read_text(encoding="utf-8"))
    return "current final-LF execution receipt and target coverage validate"


def _semantic_no_io(_row: Row) -> str:
    validate_no_io_payloads(
        (ROOT / REFUSAL_PATH).read_text(encoding="utf-8"),
        _json_object(REFUSAL_MANIFEST_PATH),
    )
    return "current closed-rails refusal proves zero vendor and database calls"


def _semantic_release(
    _row: Row, private_evidence: _PrivateCiEvidence | None = None
) -> str:
    problems = manifest_only_problems(ROOT / RELEASE_MANIFEST_PATH)
    if problems:
        raise ValueError(
            "current release manifest content validation failed: "
            + "; ".join(problems)
        )
    manifest_digest, captured_digest = validate_release_identity_family()
    if not (_hex64(manifest_digest) and _hex64(captured_digest)):
        raise ValueError("release identity digest shape mismatch")
    evidence = _private_ci_evidence() if private_evidence is None else private_evidence
    if evidence.release_state == "ABSENT":
        raise EvidencePending
    if evidence.release_state == "ATTESTED":
        raise EvidencePending
    if evidence.release_state == "FAIL":
        raise ValueError(evidence.release_detail)
    if evidence.release_state != "PASS":
        raise ValueError("unknown private release-attestation state")
    return (
        "current manifest contents and retained release family validate; "
        + evidence.release_detail
        + "; "
        + evidence.planned_detail
    )


def _checklist_payload_result(row: Row) -> str:
    path, _key, _owner = PLANNED_BINDINGS[row.token]
    raw = (ROOT / path).read_bytes()
    try:
        payload = json.loads(raw, object_pairs_hook=_unique_json_object)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"invalid planned checklist JSON: {row.token}") from exc
    phase = "PRECOMMIT" if row.token == "QA_PRECOMMIT_CHECKLIST_OK" else "POSTCOMMIT"
    result = payload.get("result") if isinstance(payload, dict) else None
    if result not in {"PASS", "FAIL"} or raw != _render_checklist(
        phase, result=result
    ):
        raise ValueError(f"planned checklist semantic mismatch: {row.token}")
    return result


def _validate_checklist_payload(row: Row) -> str:
    result = _checklist_payload_result(row)
    phase = "PRECOMMIT" if row.token == "QA_PRECOMMIT_CHECKLIST_OK" else "POSTCOMMIT"
    if result != "PASS":
        raise ValueError(f"planned checklist does not record PASS: {row.token}")
    return f"current {phase.lower()} checklist is canonical and records PASS"


def _validate_close_report_primary(_row: Row) -> str:
    raw = (ROOT / CLOSE_REPORT_PATH).read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeError as exc:
        raise ValueError("close report is not UTF-8") from exc
    required = (
        "# HDE-EPIC038 Close Report",
        "## Final decision:",
        "## Exact package pointers",
        "## Token outcomes",
        "## Embedded complete QA RCA and Doc Delta accounting",
        "## Tracked issues",
        "## PF06 §3.5.4 ADR records",
        "## Reused proof disclosure",
        "## Nonclaims",
        "DEV-02 in-memory package validation: PASS",
    )
    if not raw.endswith(b"\n") or b"\r" in raw or any(item not in text for item in required):
        raise ValueError("close report semantic contract mismatch")
    if any(token not in text for token in TOKENS):
        raise ValueError("close report token roster is incomplete")
    return "current governed close report is complete and in-memory validated"


TOKEN_EVALUATOR_REGISTRY: Mapping[str, Callable[[Row], str]] = {
    "TESTS_PASS_OK": _validate_close_report_primary,
    "DOC_DELTA_PRESENT_OK": _semantic_doc_delta,
    "EVIDENCE_INDEX_UPDATED_OK": _semantic_human_index,
    "MACHINE_MIRROR_UPDATED_OK": _semantic_machine_mirror,
    "EVIDENCE_INDEX_HASH_OK": _semantic_index_hash,
    "QA_PRECOMMIT_CHECKLIST_OK": _validate_checklist_payload,
    "QA_POSTCOMMIT_CHECKLIST_OK": _validate_checklist_payload,
    "ENV_RAILS_POLICY_OK": _semantic_env,
    "PREIMAGE_RECOMPUTE_OK": _semantic_preimage,
    "CLI_READER_PARITY_OK": _semantic_cli_reader,
    "COMPOSITE_ABBA_IDENTITY_OK": _semantic_abba,
    "TWO_RUN_IDENTITY_OK": _semantic_two_run,
    "JSON_CANONICAL_CHECK_OK": _semantic_json_gate,
    "A7_GET_QUOTED_ETAG_OK": _semantic_a7,
    "A7_HEAD_PARITY_OK": _semantic_a7,
    "A7_304_OMITS_CT_CL_OK": _semantic_a7,
    "A7_VARY_AUTH_AE_OK": _semantic_a7,
    "A7_ENCODING_INVARIANCE_OK": _semantic_a7,
    "A7_TRANSPORT_PROOF_OK": _semantic_a7,
    "ENDPOINTS_CATALOG_OK": _semantic_endpoint_catalog,
    "ENDPOINTS_CATALOG_ENV_GATE_OK": _semantic_endpoint_env_gate,
    "ENV_LC_ALL_C_OK": _semantic_env,
    "EVIDENCE_INDEX_MIRROR_OK": _semantic_index_mirror,
    "EVIDENCE_PATHS_VALIDATED_OK": _semantic_paths,
    "DB_RUNTIME_SEARCH_PATH_OK": _semantic_db,
    "DB_ROLE_OK": _semantic_db,
    "DB_SCHEMA_FINGERPRINT_OK": _semantic_db,
    "DB_CONN_ENV_OK": _semantic_db_connection,
    "EVIDENCE_PATH_PROOFS_OK": _semantic_all_proofs,
    "CI_CHECK_MIRROR_SCHEMA_OK": _semantic_mirror_schema,
    "CI_CHECK_FINAL_LF_OK": _semantic_final_lf,
    "NO_EXTERNAL_IO_ON_REFUSAL_OK": _semantic_no_io,
    "RELEASE_ID_RECOMPUTE_OK": _semantic_release,
}


def _planned_family_state() -> tuple[str, str]:
    """Classify the seven-primary closeout family as one atomic lifecycle state."""
    primary_paths = tuple(PACKAGE_ACTIVATION_PATHS)
    primary_nodes = tuple(ROOT / path for path in primary_paths)
    observed_primaries = tuple(
        path
        for path, node in zip(primary_paths, primary_nodes)
        if node.exists() or node.is_symlink()
    )
    aliased_primaries = tuple(
        path
        for path, node in zip(primary_paths, primary_nodes)
        if node.is_symlink()
    )
    nonfile_primaries = tuple(
        path
        for path, node in zip(primary_paths, primary_nodes)
        if (node.exists() or node.is_symlink()) and not node.is_file()
    )
    if aliased_primaries or nonfile_primaries:
        invalid = sorted(set((*aliased_primaries, *nonfile_primaries)))
        return "FAIL", "closeout primary is aliased or not a regular file: " + ",".join(invalid)
    if observed_primaries and len(observed_primaries) != len(primary_paths):
        missing = sorted(set(primary_paths) - set(observed_primaries))
        return "FAIL", "partial closeout primary family; missing: " + ",".join(missing)

    expected_human = {
        (key, path)
        for key, (path, _proof) in CLOSEOUT_PRIMARY_BINDINGS.items()
    }
    expected_mirror = {
        (key, path, proof)
        for key, (path, proof) in CLOSEOUT_PRIMARY_BINDINGS.items()
    }
    proof_paths = {proof for _path, proof in CLOSEOUT_PRIMARY_BINDINGS.values()}
    closeout_keys = set(CLOSEOUT_PRIMARY_BINDINGS)
    closeout_paths = set(primary_paths)
    if (
        len(primary_paths) != 7
        or len(CLOSEOUT_PRIMARY_BINDINGS) != 7
        or len(expected_human) != 7
        or len(expected_mirror) != 7
        or len(proof_paths) != 7
        or {path for path, _proof in CLOSEOUT_PRIMARY_BINDINGS.values()}
        != closeout_paths
    ):
        return "FAIL", "closeout primary/companion registry is not the exact seven-family roster"
    try:
        human_related = tuple(
            (
                item.get("artifact_key"),
                item.get("discovered_physical_path"),
            )
            for item in _human_items()
            if item.get("artifact_key") in closeout_keys
            or item.get("discovered_physical_path") in closeout_paths
        )
        mirror_related = tuple(
            (
                item.get("artifact_key"),
                item.get("discovered_physical_path"),
                item.get("proof_anchor"),
            )
            for item in _mirror_items()
            if item.get("artifact_key") in closeout_keys
            or item.get("discovered_physical_path") in closeout_paths
            or item.get("proof_anchor") in proof_paths
        )
    except (OSError, UnicodeError, ValueError) as exc:
        return "FAIL", f"closeout Index/Mirror companion state is invalid: {exc}"
    proof_nodes = tuple((proof, ROOT / proof) for proof in sorted(proof_paths))
    observed_proofs = tuple(
        proof
        for proof, node in proof_nodes
        if node.exists() or node.is_symlink()
    )
    companion_seen = bool(observed_proofs or human_related or mirror_related)

    if not observed_primaries:
        if companion_seen:
            return "FAIL", "closeout companions exist without the atomic primary family"
        return "ABSENT", "no closeout primary or companion family exists"

    try:
        actual_package = {
            path: (ROOT / path).read_bytes() for path in PACKAGE_PATHS
        }
        validate_package_structure(actual_package)
    except (KeyError, OSError, TypeError, UnicodeError, ValueError) as exc:
        return "FAIL", f"closeout primary package structure is invalid: {exc}"

    if not companion_seen:
        return (
            "PRIMARY_ONLY",
            "complete atomic closeout primary package is structurally valid and awaits canonical companions",
        )

    if any(node.is_symlink() or not node.is_file() for _proof, node in proof_nodes):
        return "FAIL", "closeout proof companion roster is partial, aliased, or non-file"
    if (
        len(human_related) != len(expected_human)
        or set(human_related) != expected_human
        or len(mirror_related) != len(expected_mirror)
        or set(mirror_related) != expected_mirror
    ):
        return "FAIL", "closeout Human Index/Machine Mirror companion roster is not exact"
    try:
        mirror_items = tuple(_mirror_items())
        for key, (path, proof) in CLOSEOUT_PRIMARY_BINDINGS.items():
            _validate_proof(path, proof)
            body = (ROOT / path).read_bytes()
            matches = [
                item
                for item in mirror_items
                if item.get("artifact_key") == key
                and item.get("discovered_physical_path") == path
                and item.get("proof_anchor") == proof
            ]
            if (
                len(matches) != 1
                or matches[0].get("sha256") != hashlib.sha256(body).hexdigest()
                or matches[0].get("size_bytes") != len(body)
            ):
                raise ValueError(f"stale closeout companion binding: {key}")
    except (OSError, UnicodeError, ValueError) as exc:
        return "FAIL", f"closeout registered companion validation failed: {exc}"
    return "REGISTERED", "complete closeout primary and companion families validate"


def _planned_result(
    row: Row,
    family_state: tuple[str, str],
    private_evidence: _PrivateCiEvidence | None = None,
) -> TokenResult:
    path, key, _owner = PLANNED_BINDINGS[row.token]
    evidence = (("ARTIFACT_PATH", path), ("ARTIFACT_KEY", key))
    follow_up = (
        f"DEV-03 must canonically produce {path}, run the canonical evidence "
        "updater, establish the exact proof and Human Index/Machine Mirror binding, "
        "and retain successful execution evidence for every exact planned command "
        "before this token may pass."
    )
    state, state_detail = family_state
    if state == "FAIL":
        return TokenResult(
            row.token,
            "FAIL",
            f"token.{row.token}.planned_binding",
            state_detail,
            evidence,
            follow_up,
        )
    if state == "ABSENT":
        return _unclaimed_planned_result(row)
    if state == "PRIMARY_ONLY":
        return TokenResult(
            row.token,
            "UNCLAIMED",
            f"token.{row.token}.current_governed_result",
            state_detail,
            evidence,
            follow_up,
        )
    if state != "REGISTERED":
        raise ValueError(f"unknown planned family state: {state}")
    private = _private_ci_evidence() if private_evidence is None else private_evidence
    try:
        _validate_row_bindings(row)
        if row.token in {
            "QA_PRECOMMIT_CHECKLIST_OK",
            "QA_POSTCOMMIT_CHECKLIST_OK",
        }:
            checklist_result = _checklist_payload_result(row)
            phase = (
                "precommit"
                if row.token == "QA_PRECOMMIT_CHECKLIST_OK"
                else "postcommit"
            )
            projected_result = (
                "PASS" if private.planned_state == "PASS" else checklist_result
            )
            detail = (
                f"current {phase} checklist is canonical and records "
                f"{projected_result}"
            )
        else:
            detail = TOKEN_EVALUATOR_REGISTRY[row.token](row)
        if private.planned_state == "FAIL":
            raise ValueError(private.planned_detail)
        if private.planned_state == "ABSENT":
            return TokenResult(
                row.token,
                "UNCLAIMED",
                f"token.{row.token}.current_governed_result",
                (
                    f"{detail}; current primary and companion bytes are necessary "
                    "but do not prove that the exact planned commands executed "
                    "successfully"
                ),
                evidence,
                follow_up,
            )
        if private.planned_state != "PASS":
            raise ValueError("unknown private execution-receipt state")
    except (OSError, UnicodeError, ValueError) as exc:
        return TokenResult(
            row.token,
            "FAIL",
            f"token.{row.token}.planned_binding",
            str(exc),
            evidence,
            follow_up,
        )
    return TokenResult(
        row.token,
        "PASS",
        f"token.{row.token}.current_governed_result",
        f"{detail}; {private.planned_detail}",
        evidence,
        "NONE",
    )


def _current_result(
    row: Row, private_evidence: _PrivateCiEvidence | None = None
) -> TokenResult:
    evidence = tuple(
        ("ARTIFACT_PATH", path) for path in row.primary_evidence
    ) + tuple(("ARTIFACT_KEY", key) for key in row.artifact_keys)
    follow_up = (
        f"Correct or canonically regenerate the exact governed evidence family for "
        f"{row.token}, then rerun its registered validators."
    )
    try:
        _validate_row_bindings(row)
        _validate_live_qa(row)
        detail = (
            _semantic_release(row, private_evidence)
            if row.token == "RELEASE_ID_RECOMPUTE_OK"
            else TOKEN_EVALUATOR_REGISTRY[row.token](row)
        )
    except EvidencePending as exc:
        if row.token != "RELEASE_ID_RECOMPUTE_OK":
            raise ValueError(
                f"unsupported pending-evidence token: {row.token}"
            ) from exc
        return _unclaimed_release_result(row)
    except (OSError, UnicodeError, ValueError) as exc:
        return TokenResult(
            row.token,
            "FAIL",
            f"token.{row.token}.current_governed_result",
            str(exc),
            evidence,
            follow_up,
        )
    return TokenResult(
        row.token,
        "PASS",
        f"token.{row.token}.current_governed_result",
        detail,
        evidence,
        "NONE",
    )


def _unclaimed_release_result(
    row: Row, *, detail: str | None = None
) -> TokenResult:
    if row.token != "RELEASE_ID_RECOMPUTE_OK":
        raise ValueError("release pending result used for another token")
    if detail is None:
        manifest_digest, captured_digest = validate_release_identity_family()
        detail = (
            "current manifest content validates, but no verified external "
            "exact-source release attestation was supplied; retained identity "
            "captures remain historical "
            f"(manifest={manifest_digest}; retained_capture={captured_digest})"
        )
    evidence = tuple(
        ("ARTIFACT_PATH", path) for path in row.primary_evidence
    ) + tuple(("ARTIFACT_KEY", key) for key in row.artifact_keys)
    return TokenResult(
        row.token,
        "UNCLAIMED",
        f"token.{row.token}.current_governed_result",
        detail,
        evidence,
        (
            "Validate the current canonical manifest contents and supply the "
            "canonical external exact-source release attestation and exact-command "
            "CI receipt for this source head before RELEASE_ID_RECOMPUTE_OK may pass."
        ),
    )


def _token_blocker(result: TokenResult) -> Mapping[str, object]:
    row = {item.token: item for item in build_rows()}[result.token]
    if result.token == "RELEASE_ID_RECOMPUTE_OK":
        return _descriptor(
            result.predicate_key,
            "TOKEN",
            result.token,
            result.detail,
            [
                {"kind": kind, "value": value}
                for kind, value in result.decisive_evidence
            ],
            (
                "python scripts/release_id_recompute.py --check-manifest-only; "
                "python tools/evidence/build_release_attestation.py --verify "
                '"$RUNNER_TEMP/hde-release-attestation" --require-clean'
            ),
            "EVIDENCE_PRODUCER_OR_VALIDATOR_DEFECT",
            [],
            result.minimum_follow_up,
            ["closeout_package_in_memory", "epic038_current_state"],
        )
    permitted = [
        path
        for path in row.primary_evidence
        if not path.startswith(("audit/ops/", "audit/qa/hde-epic038/checks/"))
    ]
    return _descriptor(
        result.predicate_key,
        "TOKEN",
        result.token,
        result.detail,
        [
            {"kind": kind, "value": value}
            for kind, value in result.decisive_evidence
        ],
        PLAN_CLOSEOUT_CHECK_COMMAND,
        "GOVERNED_ARTIFACT_DRIFT",
        permitted,
        result.minimum_follow_up,
        ["closeout_package_in_memory", "epic038_current_state"],
    )


def _plan_authority() -> dict[str, object]:
    try:
        raw = (ROOT / PLAN_PATH).read_bytes()
        text = raw.decode("utf-8")
    except (OSError, UnicodeError) as exc:
        raise ValueError(f"approved r5 source unavailable: {PLAN_PATH}") from exc
    if not raw.endswith(b"\n") or b"\r" in raw:
        raise ValueError("approved r5 source byte format mismatch")
    if hashlib.sha256(raw).hexdigest() != APPROVED_PLAN_SHA256:
        raise ValueError("approved r5 complete-source digest mismatch")
    try:
        pf09_section = text.split("## 6. PF09 accountability\n", 1)[1].split(
            "\n## 7. Corrected token scope", 1
        )[0]
        decisions_section = text.split(
            "## 12. Tracked issues and decision records\n", 1
        )[1].split("\n## 13. Canon and drainage dispositions", 1)[0]
    except IndexError as exc:
        raise ValueError("approved r5 required section topology mismatch") from exc
    bullet_ids = tuple(re.findall(r"^\* `([^`]+)`", pf09_section, re.MULTILINE))
    expected_ids = tuple(
        value.removesuffix(" (subtask N/A)") for value in PF09_SCOPE
    ) + PF09_EXCLUSIONS
    if bullet_ids != expected_ids:
        raise ValueError("approved r5 PF09 scope/exclusion mismatch")
    issue_labels = tuple(re.findall(r"^### (TI(?:-R1)?-[0-9]{3}) —", decisions_section, re.MULTILINE))
    adr_labels = tuple(re.findall(r"^### (ADR-R1-[0-9]{3}) —", decisions_section, re.MULTILINE))
    if issue_labels != tuple(TRACKED_ISSUES) or adr_labels != tuple(
        item["label"] for item in ADR_RECORDS
    ):
        raise ValueError("approved r5 issue/ADR roster mismatch")
    required_decisions = (
        "RELEASE_ID_RECOMPUTE_OK` is admitted",
        "Assigned to DEV-01",
        "Assigned to DEV-02 and DEV-03",
        "Assigned to DEV-02 through DEV-04",
        "Assigned to DEV-R1",
        "Resolved by published PF10 Addendum 2.38",
        "Use one bounded DEV remediation lineage",
        "only at evidence-derived `SATISFIED`",
        "Remove the bridge token only from current claim surfaces",
        "Create no new task in that phased document",
        "DEV-02 begins only after the matrix is complete",
    )
    if any(value not in decisions_section for value in required_decisions):
        raise ValueError("approved r5 issue/ADR disposition mismatch")
    return {
        "adr_records": [dict(item) for item in ADR_RECORDS],
        "pf09_exclusions": list(PF09_EXCLUSIONS),
        "pf09_scope": list(PF09_SCOPE),
        "plan_path": PLAN_PATH,
        "plan_sha256": APPROVED_PLAN_SHA256,
        "tracked_issues": {
            key: dict(value) for key, value in TRACKED_ISSUES.items()
        },
    }


def _validate_non_token_family(label: str) -> str:
    if tuple(NON_TOKEN_BINDINGS) != NON_TOKEN_OBLIGATIONS:
        raise ValueError("non-token evaluator registry mismatch")
    key, path, proof = NON_TOKEN_BINDINGS[label]
    if not (ROOT / path).is_file() or not (ROOT / proof).is_file():
        raise ValueError(f"missing non-token proof family: {label}")
    _validate_proof(path, proof)
    mirror = [
        item
        for item in _mirror_items()
        if item.get("artifact_key") == key
        and item.get("discovered_physical_path") == path
        and item.get("proof_anchor") == proof
    ]
    human = [
        item
        for item in _human_items()
        if item.get("artifact_key") == key
        and item.get("discovered_physical_path") == path
    ]
    if len(mirror) != 1 or len(human) != 1:
        raise ValueError(f"non-token Index/Mirror binding mismatch: {label}")
    body = (ROOT / path).read_bytes()
    if (
        mirror[0].get("sha256") != hashlib.sha256(body).hexdigest()
        or mirror[0].get("size_bytes") != len(body)
    ):
        raise ValueError(f"stale non-token Machine Mirror binding: {label}")
    payload = _json_object(path)
    proof_labels = payload.get("proof_labels")
    actual_labels = (
        tuple(
            item.get("name")
            for item in proof_labels
            if isinstance(item, dict) and item.get("type") == "non_token"
        )
        if isinstance(proof_labels, list)
        else ()
    )
    if label.startswith("BG_") and label not in actual_labels:
        raise ValueError(f"non-token proof label mismatch: {label}")
    if label in {
        "BG_SOURCE_SELECTION_OK",
        "BG_VENDOR_CALLS_DISABLED_IN_PROD_OK",
    }:
        scenarios = payload.get("scenarios")
        if (
            payload.get("schema") != "v1"
            or actual_labels
            != ("BG_SOURCE_SELECTION_OK", "BG_VENDOR_CALLS_DISABLED_IN_PROD_OK")
            or not isinstance(scenarios, list)
            or len(scenarios) != 3
            or any(
                not isinstance(item, dict) or item.get("transport_calls") != 0
                for item in scenarios
            )
            or not any(
                isinstance(item, dict)
                and item.get("requested_source") == "vendor"
                and item.get("reason") == "PROVIDER_REFUSED"
                and item.get("status") == "error"
                for item in scenarios
            )
        ):
            raise ValueError(f"source-selection non-token predicate mismatch: {label}")
    elif label == "BG_SOURCE_INVARIANCE_OK":
        predicates = payload.get("predicates")
        if (
            payload.get("schema") != "bodygraph.source_invariance.summary.v2"
            or actual_labels != (label,)
            or payload.get("top_level_pass") is not True
            or not isinstance(predicates, dict)
            or not predicates
            or any(value is not True for value in predicates.values())
        ):
            raise ValueError("source-invariance non-token predicate mismatch")
    elif label.startswith("BG_"):
        circuit = payload.get("circuit_breaker")
        rate = payload.get("rate_limit")
        if (
            payload.get("schema") != "v1"
            or actual_labels
            != (
                "BG_TTL_SWR_POLICY_OK",
                "BG_RATE_LIMIT_POLICY_OK",
                "BG_CIRCUIT_BREAKER_POLICY_OK",
            )
            or not isinstance(payload.get("ttl_s"), int)
            or not isinstance(payload.get("swr_s"), int)
            or payload["ttl_s"] <= payload["swr_s"]
            or payload["swr_s"] <= 0
            or not isinstance(rate, dict)
            or any(not isinstance(rate.get(name), int) or rate[name] <= 0 for name in ("requests_per_window", "window_s"))
            or not isinstance(circuit, dict)
            or any(not isinstance(circuit.get(name), int) or circuit[name] <= 0 for name in ("cooldown_s", "fail_threshold", "window_s"))
        ):
            raise ValueError(f"refresh-policy non-token predicate mismatch: {label}")
    else:
        rails = payload.get("default_rails")
        pins = payload.get("determinism_pins")
        predicates = {
            "ENV_SNAPSHOT_SINGLETON_OK": bool(
                {
                    item.get("artifact_key")
                    for item in _mirror_items()
                    if item.get("discovered_physical_path") == path
                }
                == {
                    "epic038.pr01.env_matrix_snapshot_v3",
                    "runtime.env_matrix.snapshot",
                }
            ),
            "ENV_SNAPSHOT_SCHEMA_V3_OK": payload.get("schema_version") == 3,
            "ENV_PINS_PRESENT_OK": pins == {"LANG": "C", "LC_ALL": "C", "TZ": "UTC"},
        }
        closed = {"ALLOW_NETWORK": "0", "SAFE_MODE": "1"}
        if (
            predicates[label] is not True
            or not isinstance(rails, dict)
            or any(rails.get(name) != closed for name in ("dev", "stage", "CI"))
        ):
            raise ValueError(f"environment non-token predicate mismatch: {label}")
    return "affirmative current non-token predicate validates"


def _obligation_results() -> tuple[Mapping[str, object], ...]:
    obligations: list[Mapping[str, object]] = []
    checks: tuple[tuple[str, Callable[[], None], list[dict[str, str]], str], ...] = (
        (
            "qa.finalized_current_state",
            _validate_finalized_qa_state,
            [
                {"kind": "ARTIFACT_PATH", "value": QA_MANIFEST_PATH},
                {"kind": "ARTIFACT_PATH", "value": QA_RCA_PATH},
            ],
            "Restore the finalized 24-check QA current-state fixed point through its owning process.",
        ),
        (
            "evidence.full_index_mirror_topology",
            lambda: (validate_index_mirror_topology(), validate_all_mirror_proofs()),
            [
                {"kind": "ARTIFACT_PATH", "value": HUMAN_INDEX_PATH},
                {"kind": "ARTIFACT_PATH", "value": MACHINE_MIRROR_PATH},
            ],
            "Run the canonical evidence updater and all companion validators.",
        ),
    )
    for key, validator, evidence, follow_up in checks:
        try:
            validator()
            obligations.append(
                {
                    "detail": "affirmative current predicate validates",
                    "predicate_key": key,
                    "status": "PASS",
                }
            )
        except (OSError, UnicodeError, ValueError) as exc:
            obligations.append(
                {
                    "blocker": _descriptor(
                        key,
                        "CHECK",
                        key,
                        str(exc),
                        evidence,
                        PLAN_CLOSEOUT_CHECK_COMMAND,
                        "GOVERNED_ARTIFACT_DRIFT",
                        [],
                        follow_up,
                        ["closeout_package_in_memory", "epic038_current_state"],
                    ),
                    "detail": str(exc),
                    "predicate_key": key,
                    "status": "FAIL",
                }
            )
    try:
        authority = _plan_authority()
        obligations.append(
            {
                "detail": f"approved r5 source validates at {authority['plan_sha256']}",
                "predicate_key": "authority.approved_r5_source",
                "status": "PASS",
            }
        )
        obligations.extend(
            {
                "detail": "approved r5 PF09 scope item validates",
                "item": item,
                "predicate_key": f"authority.pf09_scope.{item}",
                "status": "PASS",
            }
            for item in PF09_SCOPE
        )
        obligations.extend(
            {
                "detail": "approved r5 PF09 exclusion validates",
                "item": item,
                "predicate_key": f"authority.pf09_exclusion.{item}",
                "status": "PASS",
            }
            for item in PF09_EXCLUSIONS
        )
        obligations.extend(
            {
                "detail": "approved r5 tracked-issue disposition validates",
                "item": issue,
                "predicate_key": f"authority.tracked_issue.{issue}",
                "status": "PASS",
            }
            for issue in TRACKED_ISSUES
        )
        obligations.extend(
            {
                "detail": "approved r5 ADR disposition validates",
                "item": str(record["label"]),
                "predicate_key": f"authority.adr.{record['label']}",
                "status": "PASS",
            }
            for record in ADR_RECORDS
        )
        obligations.append(
            {
                "detail": "preserved execution-level QA RCA source is consumed",
                "item": QA_RCA_PATH,
                "predicate_key": "authority.qa_rca_source",
                "status": "PASS",
            }
        )
    except (OSError, UnicodeError, ValueError) as exc:
        obligations.append(
            {
                "blocker": _descriptor(
                    "authority.approved_r5_source",
                    "AUTHORITY",
                    PLAN_PATH,
                    str(exc),
                    [{"kind": "ARTIFACT_PATH", "value": PLAN_PATH}],
                    "internal:validate-approved-r5-source",
                    "SOURCE_AUTHORITY_CONFLICT",
                    [],
                    "Restore or reconcile the complete approved r5 authority before continuing.",
                    ["closeout_package_in_memory"],
                    "PO_AUTHORIZATION_REQUIRED",
                ),
                "detail": str(exc),
                "predicate_key": "authority.approved_r5_source",
                "status": "FAIL",
            }
        )
    for label in NON_TOKEN_OBLIGATIONS:
        key, path, _proof = NON_TOKEN_BINDINGS[label]
        predicate_key = f"non_token.{label}.current_governed_result"
        try:
            detail = _validate_non_token_family(label)
            obligations.append(
                {
                    "artifact_key": key,
                    "detail": detail,
                    "label": label,
                    "path": path,
                    "predicate_key": predicate_key,
                    "status": "PASS",
                }
            )
        except (OSError, UnicodeError, ValueError) as exc:
            follow_up = (
                f"Correct or canonically regenerate the exact governed non-token "
                f"proof family for {label}, then rerun all companion validators."
            )
            obligations.append(
                {
                    "artifact_key": key,
                    "blocker": _descriptor(
                        predicate_key,
                        "CHECK",
                        label,
                        str(exc),
                        [
                            {"kind": "ARTIFACT_PATH", "value": path},
                            {"kind": "ARTIFACT_KEY", "value": key},
                        ],
                        PLAN_CLOSEOUT_CHECK_COMMAND,
                        "GOVERNED_ARTIFACT_DRIFT",
                        [path],
                        follow_up,
                        ["closeout_package_in_memory", "epic038_current_state"],
                    ),
                    "detail": str(exc),
                    "label": label,
                    "path": path,
                    "predicate_key": predicate_key,
                    "status": "FAIL",
                }
            )
    observed_non_tokens = tuple(
        item.get("label") for item in obligations if "label" in item
    )
    if observed_non_tokens != NON_TOKEN_OBLIGATIONS:
        raise ValueError("non-token obligation roster/order mismatch")
    return tuple(obligations)


def _make_snapshot(
    results: Sequence[TokenResult],
    families: Sequence[Mapping[str, object]],
    blockers: Sequence[Mapping[str, object]],
    obligations: Sequence[Mapping[str, object]],
) -> EvaluationSnapshot:
    snapshot_payload = {
        "blockers": list(blockers),
        "obligations": [
            {key: value for key, value in item.items() if key != "blocker"}
            for item in obligations
        ],
        "proof_families": list(families),
        "token_results": [item.as_dict() for item in results],
    }
    fingerprint = hashlib.sha256(_canonical_json(snapshot_payload)).hexdigest()
    return EvaluationSnapshot(
        tuple(results),
        tuple(families),
        tuple(blockers),
        tuple(obligations),
        fingerprint,
    )


def _source_results_for_fingerprint(
    results: Sequence[TokenResult], source_status: Mapping[str, object]
) -> tuple[TokenResult, ...]:
    """Rebuild the canonical pre-generation token results from package bytes."""
    rows = {row.token: row for row in build_rows()}
    rebuilt: list[TokenResult] = []
    for result in results:
        status = source_status.get(result.token)
        if result.token in PLANNED_BINDINGS:
            if status == "UNCLAIMED" and result.status == "UNCLAIMED":
                rebuilt.append(_unclaimed_planned_result(rows[result.token]))
                continue
            if status == result.status and result.status in {"PASS", "FAIL"}:
                rebuilt.append(result)
                continue
            raise ValueError("manifest canonical planned source-token status mismatch")
        if result.token == "RELEASE_ID_RECOMPUTE_OK":
            if status == "UNCLAIMED" and result.status == "UNCLAIMED":
                rebuilt.append(_unclaimed_release_result(rows[result.token]))
                continue
            if status == result.status and result.status in {"PASS", "FAIL"}:
                rebuilt.append(result)
                continue
            raise ValueError("manifest canonical release source-token status mismatch")
        if result.status not in {"PASS", "FAIL"} or status != result.status:
            raise ValueError("manifest canonical reused source-token status mismatch")
        rebuilt.append(result)
    return tuple(rebuilt)


def _fingerprint_obligations(
    obligations: Sequence[Mapping[str, object]],
) -> tuple[Mapping[str, object], ...]:
    """Restore fields omitted by the viability rendering but bound by the hash."""
    canonical_pass_details = {
        "qa.finalized_current_state": "affirmative current predicate validates",
        "evidence.full_index_mirror_topology": "affirmative current predicate validates",
        "authority.approved_r5_source": (
            f"approved r5 source validates at {APPROVED_PLAN_SHA256}"
        ),
        **{
            f"authority.pf09_scope.{value}": "approved r5 PF09 scope item validates"
            for value in PF09_SCOPE
        },
        **{
            f"authority.pf09_exclusion.{value}": "approved r5 PF09 exclusion validates"
            for value in PF09_EXCLUSIONS
        },
        **{
            f"authority.tracked_issue.{value}": "approved r5 tracked-issue disposition validates"
            for value in TRACKED_ISSUES
        },
        **{
            f"authority.adr.{record['label']}": "approved r5 ADR disposition validates"
            for record in ADR_RECORDS
        },
        "authority.qa_rca_source": (
            "preserved execution-level QA RCA source is consumed"
        ),
    }
    dynamically_failing = {
        "qa.finalized_current_state",
        "evidence.full_index_mirror_topology",
    }
    rebuilt: list[Mapping[str, object]] = []
    for obligation in obligations:
        item = dict(obligation)
        predicate_key = str(item.get("predicate_key", ""))
        status = item.get("status")
        detail = item.get("detail")
        label = item.get("label")
        if label is not None:
            if label not in NON_TOKEN_OBLIGATIONS:
                raise ValueError("fingerprint non-token obligation label mismatch")
            key, path, _proof = NON_TOKEN_BINDINGS[str(label)]
            if item != {
                "artifact_key": key,
                "detail": detail,
                "label": label,
                "path": path,
                "predicate_key": (
                    f"non_token.{label}.current_governed_result"
                ),
                "status": status,
            }:
                raise ValueError("fingerprint non-token obligation payload mismatch")
            if status == "PASS" and detail != (
                "affirmative current non-token predicate validates"
            ):
                raise ValueError("fingerprint non-token PASS detail mismatch")
            if status not in {"PASS", "FAIL"}:
                raise ValueError("fingerprint non-token status mismatch")
            rebuilt.append(item)
            continue
        if predicate_key not in canonical_pass_details:
            raise ValueError("fingerprint structural obligation mismatch")
        if status == "PASS":
            if detail != canonical_pass_details[predicate_key]:
                raise ValueError("fingerprint structural PASS detail mismatch")
        elif status != "FAIL" or predicate_key not in dynamically_failing:
            raise ValueError("fingerprint structural obligation status mismatch")
        if predicate_key.startswith("authority.pf09_scope."):
            value = predicate_key.removeprefix("authority.pf09_scope.")
            if value not in PF09_SCOPE:
                raise ValueError("fingerprint PF09 scope obligation mismatch")
            item["item"] = value
        elif predicate_key.startswith("authority.pf09_exclusion."):
            value = predicate_key.removeprefix("authority.pf09_exclusion.")
            if value not in PF09_EXCLUSIONS:
                raise ValueError("fingerprint PF09 exclusion obligation mismatch")
            item["item"] = value
        elif predicate_key.startswith("authority.tracked_issue."):
            value = predicate_key.removeprefix("authority.tracked_issue.")
            if value not in TRACKED_ISSUES:
                raise ValueError("fingerprint tracked-issue obligation mismatch")
            item["item"] = value
        elif predicate_key.startswith("authority.adr."):
            value = predicate_key.removeprefix("authority.adr.")
            if value not in {str(record["label"]) for record in ADR_RECORDS}:
                raise ValueError("fingerprint ADR obligation mismatch")
            item["item"] = value
        elif predicate_key == "authority.qa_rca_source":
            item["item"] = QA_RCA_PATH
        rebuilt.append(item)
    return tuple(rebuilt)


def _fingerprint_blockers(
    results: Sequence[TokenResult],
    obligations: Sequence[Mapping[str, object]],
) -> tuple[Mapping[str, object], ...]:
    """Rebuild source blockers without evaluating repository companion state."""
    blockers: list[Mapping[str, object]] = [
        _token_blocker(result) for result in results if result.status == "FAIL"
    ]
    structural = {
        "qa.finalized_current_state": (
            [
                {"kind": "ARTIFACT_PATH", "value": QA_MANIFEST_PATH},
                {"kind": "ARTIFACT_PATH", "value": QA_RCA_PATH},
            ],
            "Restore the finalized 24-check QA current-state fixed point through its owning process.",
        ),
        "evidence.full_index_mirror_topology": (
            [
                {"kind": "ARTIFACT_PATH", "value": HUMAN_INDEX_PATH},
                {"kind": "ARTIFACT_PATH", "value": MACHINE_MIRROR_PATH},
            ],
            "Run the canonical evidence updater and all companion validators.",
        ),
    }
    for obligation in obligations:
        if obligation.get("status") != "FAIL":
            continue
        predicate_key = str(obligation.get("predicate_key", ""))
        detail = str(obligation.get("detail", ""))
        if predicate_key in structural:
            evidence, follow_up = structural[predicate_key]
            blockers.append(
                _descriptor(
                    predicate_key,
                    "CHECK",
                    predicate_key,
                    detail,
                    evidence,
                    PLAN_CLOSEOUT_CHECK_COMMAND,
                    "GOVERNED_ARTIFACT_DRIFT",
                    [],
                    follow_up,
                    ["closeout_package_in_memory", "epic038_current_state"],
                )
            )
            continue
        if predicate_key == "authority.approved_r5_source":
            blockers.append(
                _descriptor(
                    predicate_key,
                    "AUTHORITY",
                    PLAN_PATH,
                    detail,
                    [{"kind": "ARTIFACT_PATH", "value": PLAN_PATH}],
                    "internal:validate-approved-r5-source",
                    "SOURCE_AUTHORITY_CONFLICT",
                    [],
                    "Restore or reconcile the complete approved r5 authority before continuing.",
                    ["closeout_package_in_memory"],
                    "PO_AUTHORIZATION_REQUIRED",
                )
            )
            continue
        label = obligation.get("label")
        if label in NON_TOKEN_OBLIGATIONS:
            key, path, _proof = NON_TOKEN_BINDINGS[str(label)]
            blockers.append(
                _descriptor(
                    predicate_key,
                    "CHECK",
                    str(label),
                    detail,
                    [
                        {"kind": "ARTIFACT_PATH", "value": path},
                        {"kind": "ARTIFACT_KEY", "value": key},
                    ],
                    PLAN_CLOSEOUT_CHECK_COMMAND,
                    "GOVERNED_ARTIFACT_DRIFT",
                    [path],
                    (
                        "Correct or canonically regenerate the exact governed "
                        f"non-token proof family for {label}, then rerun all "
                        "companion validators."
                    ),
                    ["closeout_package_in_memory", "epic038_current_state"],
                )
            )
            continue
        raise ValueError(f"unsupported failing fingerprint obligation: {predicate_key}")
    blockers.sort(
        key=lambda item: (
            str(item["predicate_key"]),
            json.dumps(item["subject"], sort_keys=True),
        )
    )
    return tuple(blockers)


def _unclaimed_planned_result(row: Row) -> TokenResult:
    path, key, _owner = PLANNED_BINDINGS[row.token]
    return TokenResult(
        row.token,
        "UNCLAIMED",
        f"token.{row.token}.current_governed_result",
        "exact planned-new binding is computable and not yet produced",
        (("ARTIFACT_PATH", path), ("ARTIFACT_KEY", key)),
        (
            f"DEV-03 must canonically produce {path}, run the canonical evidence "
            "updater, establish the exact proof and Human Index/Machine Mirror "
            "binding, and retain successful execution evidence for every exact "
            "planned command before this token may pass."
        ),
    )


def _evaluate_closeout(private_evidence: _PrivateCiEvidence) -> EvaluationSnapshot:
    if tuple(TOKEN_EVALUATOR_REGISTRY) != TOKENS:
        raise ValueError("token evaluator registry must equal the approved roster/order")
    raw_rows = tuple(build_rows())
    try:
        rows = validate_rows(raw_rows, planned_mode="allow-current")
        expected_matrix = render(rows, planned_mode="allow-current")
        actual_matrix = _matrix_bytes()
        if (
            actual_matrix != expected_matrix
            or hashlib.sha256(actual_matrix).hexdigest() != TOKEN_MATRIX_SHA256
        ):
            raise ValueError("DEV-01 token matrix byte contract drift")
    except (OSError, UnicodeError, ValueError) as exc:
        if tuple(row.token for row in raw_rows) != TOKENS:
            raise ValueError(f"invalid DEV-01 row contract: {exc}") from exc
        rows = raw_rows
        detail = f"complete DEV-01 row validation failed: {exc}"
        results = tuple(
            TokenResult(
                row.token,
                "FAIL",
                f"token.{row.token}.current_governed_result",
                detail,
                tuple(("ARTIFACT_PATH", path) for path in row.primary_evidence),
                "Restore the approved DEV-01 matrix and every declared evidence family.",
            )
            for row in rows
        )
    else:
        planned_family_state = _planned_family_state()
        results = tuple(
            _planned_result(row, planned_family_state, private_evidence)
            if row.classification == "planned-new"
            else _current_result(row, private_evidence)
            for row in rows
        )
    if tuple(item.token for item in results) != TOKENS:
        raise ValueError("token result roster/order mismatch")
    if any(item.status not in {"PASS", "UNCLAIMED", "FAIL"} for item in results):
        raise ValueError("invalid token result status")
    families = _proof_family_records(rows)
    obligations = _obligation_results()
    blockers: list[Mapping[str, object]] = [
        _token_blocker(item) for item in results if item.status == "FAIL"
    ]
    blockers.extend(
        item["blocker"]
        for item in obligations
        if item.get("status") == "FAIL" and isinstance(item.get("blocker"), dict)
    )
    blockers.sort(
        key=lambda item: (
            str(item["predicate_key"]),
            json.dumps(item["subject"], sort_keys=True),
        )
    )
    return _make_snapshot(results, families, blockers, obligations)


def evaluate_closeout() -> EvaluationSnapshot:
    return _evaluate_closeout(_private_ci_evidence())


def derive_blockers(
    snapshot: EvaluationSnapshot | None = None,
) -> list[dict[str, object]]:
    current = evaluate_closeout()
    if snapshot is not None and snapshot != current:
        raise ValueError("stale or caller-forged evaluation snapshot")
    return [dict(item) for item in current.blockers]


def _validate_snapshot_contract(snapshot: EvaluationSnapshot) -> None:
    if tuple(item.token for item in snapshot.token_results) != TOKENS:
        raise ValueError("evaluation snapshot token roster/order mismatch")
    if any(
        item.status not in {"PASS", "UNCLAIMED", "FAIL"}
        or not item.predicate_key
        or not item.detail
        or not item.decisive_evidence
        or (item.status == "PASS" and item.minimum_follow_up != "NONE")
        for item in snapshot.token_results
    ):
        raise ValueError("evaluation snapshot token result mismatch")
    expected_families = _proof_family_records(tuple(build_rows()))
    if snapshot.proof_families != expected_families:
        raise ValueError("evaluation snapshot proof-family roster mismatch")
    labels = tuple(
        item.get("label") for item in snapshot.obligations if "label" in item
    )
    if labels != NON_TOKEN_OBLIGATIONS:
        raise ValueError("evaluation snapshot non-token obligation roster mismatch")
    rebuilt = _make_snapshot(
        snapshot.token_results,
        snapshot.proof_families,
        snapshot.blockers,
        snapshot.obligations,
    )
    if rebuilt != snapshot:
        raise ValueError("evaluation snapshot fingerprint or structure mismatch")


def _canonical_source_snapshot(snapshot: EvaluationSnapshot) -> EvaluationSnapshot:
    """Normalize only the receipt-absent planned lifecycle details."""

    rows = {row.token: row for row in build_rows()}
    normalized = tuple(
        _unclaimed_planned_result(rows[item.token])
        if item.token in PLANNED_BINDINGS and item.status == "UNCLAIMED"
        else item
        for item in snapshot.token_results
    )
    if normalized == snapshot.token_results:
        return snapshot
    return _make_snapshot(
        normalized,
        snapshot.proof_families,
        snapshot.blockers,
        snapshot.obligations,
    )


def _validate_candidate_primary_bytes(
    row: Row, result: TokenResult, package: Mapping[str, bytes]
) -> None:
    path, _key, _owner = PLANNED_BINDINGS[row.token]
    try:
        raw = package[path]
    except KeyError as exc:
        raise ValueError(f"candidate lacks planned primary: {path}") from exc
    if not isinstance(raw, bytes) or not raw or not raw.endswith(b"\n") or b"\r" in raw:
        raise ValueError(f"candidate planned primary is not canonical LF: {path}")
    if row.token == "TESTS_PASS_OK":
        try:
            text = raw.decode("utf-8")
        except UnicodeError as exc:
            raise ValueError("candidate close report is not UTF-8") from exc
        try:
            manifest = json.loads(
                package[CLOSE_MANIFEST_PATH],
                object_pairs_hook=_unique_json_object,
            )
        except (KeyError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            raise ValueError("candidate close manifest is invalid") from exc
        decision = manifest.get("decision") if isinstance(manifest, dict) else None
        if decision not in {"SATISFIED", "NOT SATISFIED"}:
            raise ValueError("candidate close manifest decision is invalid")
        required = (
            "# HDE-EPIC038 Close Report",
            f"## Final decision: {decision}",
            "DEV-02 in-memory package validation: PASS",
            "## Exact package pointers",
            "## Token outcomes",
            "## Embedded complete QA RCA and Doc Delta accounting",
            "## Tracked issues",
            "## PF06 §3.5.4 ADR records",
            "## Reused proof disclosure",
            "## Nonclaims",
        )
        if any(value not in text for value in required) or (
            f"- {row.token}: {result.status};" not in text
        ):
            raise ValueError("candidate close report semantic contract mismatch")
        return
    phase = "PRECOMMIT" if row.token == "QA_PRECOMMIT_CHECKLIST_OK" else "POSTCOMMIT"
    try:
        payload = json.loads(raw, object_pairs_hook=_unique_json_object)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"candidate checklist is invalid: {row.token}") from exc
    checklist_result = payload.get("result") if isinstance(payload, dict) else None
    if checklist_result not in {"PASS", "FAIL"} or raw != _render_checklist(
        phase, result=str(checklist_result)
    ):
        raise ValueError(f"candidate checklist semantic mismatch: {row.token}")


def _candidate_token_results(
    snapshot: EvaluationSnapshot, package: Mapping[str, bytes]
) -> tuple[TokenResult, ...]:
    """Validate planned primaries without converting their evidence posture."""
    rows = {row.token: row for row in build_rows()}
    for item in snapshot.token_results:
        if item.token in PLANNED_BINDINGS:
            _validate_candidate_primary_bytes(rows[item.token], item, package)
    return snapshot.token_results


def _minimum_follow_up(
    results: Sequence[TokenResult], ledger: Mapping[str, object]
) -> list[str]:
    values = {
        item.minimum_follow_up
        for item in results
        if item.status != "PASS" and item.minimum_follow_up != "NONE"
    }
    for entry in ledger["entries"]:  # type: ignore[index]
        if entry["status"] == "OPEN":
            values.add(str(entry["minimum_follow_up"]))
    return sorted(values)


def _render_checklist(
    phase: str, *, result: str
) -> bytes:
    if phase not in {"PRECOMMIT", "POSTCOMMIT"} or result not in {"PASS", "FAIL"}:
        raise ValueError("invalid checklist render state")
    key = (
        PRECOMMIT_CHECKLIST_KEY if phase == "PRECOMMIT" else POSTCOMMIT_CHECKLIST_KEY
    )
    payload = {
        "artifact_key": key,
        "closed_rails": {
            "ALLOW_NETWORK": "0",
            "APP_ENV": "dev",
            "LANG": "C",
            "LC_ALL": "C",
            "SAFE_MODE": "1",
            "TZ": "UTC",
        },
        "epic_id": EPIC_ID,
        "phase": phase,
        "result": result,
        "schema": "hde.epic038.closeout_checklist.v1",
        "token_roster": list(TOKENS),
        "validation_commands": [PLAN_CLOSEOUT_CHECK_COMMAND, PLANNED_COMMANDS],
    }
    return _canonical_json(payload)


def _acceptance_payload(
    snapshot: EvaluationSnapshot,
    results: Sequence[TokenResult],
    decision: str,
    minimum: Sequence[str],
) -> dict[str, object]:
    result_by_token = {item.token: item for item in results}
    rows = tuple(build_rows())
    if tuple(row.token for row in rows) != TOKENS:
        raise ValueError("acceptance-map row roster/order mismatch")
    families_by_token: dict[str, list[Mapping[str, object]]] = {
        token: [] for token in TOKENS
    }
    for family in snapshot.proof_families:
        families_by_token[str(family["token"])].append(dict(family))
    records = []
    for row in rows:
        token_result = result_by_token[row.token]
        records.append(
            {
                "acceptance_token": row.acceptance_token,
                "artifact_keys": list(row.artifact_keys),
                "ci_binding": row.ci_binding,
                "classification": row.classification,
                "current_posture": row.posture,
                "epic_id": row.epic_id,
                "future_claim_prerequisite": row.future_claim,
                "live_qa": row.live_qa,
                "manifest_token": row.manifest_token,
                "owner_task": row.owner_task,
                "primary_evidence": list(row.primary_evidence),
                "proof_anchors": list(row.proof_anchors),
                "proof_families": families_by_token[row.token],
                "result": token_result.as_dict(),
                "status": token_result.status,
                "test_binding": row.test_binding,
                "token": row.token,
            }
        )
    non_tokens = [
        {key: value for key, value in item.items() if key != "blocker"}
        for item in snapshot.obligations
        if item.get("label") in NON_TOKEN_OBLIGATIONS
    ]
    if tuple(item.get("label") for item in non_tokens) != NON_TOKEN_OBLIGATIONS:
        raise ValueError("acceptance non-token roster mismatch")
    return {
        "artifact_key": "epic038.acceptance_map",
        "close_obligation_families": [
            {
                "artifact_key": key,
                "epic_id": EPIC_ID,
                "primary_evidence": path,
                "proof_anchor": proof,
            }
            for key, (path, proof) in CLOSEOUT_PRIMARY_BINDINGS.items()
        ],
        "decision": decision,
        "epic_id": EPIC_ID,
        "minimum_follow_up": list(minimum),
        "non_token_obligations": non_tokens,
        "pf09_exclusions": list(PF09_EXCLUSIONS),
        "pf09_scope": list(PF09_SCOPE),
        "proof_family_roster": [dict(item) for item in snapshot.proof_families],
        "records": records,
        "schema": "hde.epic038.acceptance_map.v1",
        "schema_version": "1.0",
        "source_evaluation_fingerprint": snapshot.fingerprint,
    }


def _viability_bytes(
    snapshot: EvaluationSnapshot,
    results: Sequence[TokenResult],
    decision: str,
    minimum: Sequence[str],
) -> bytes:
    lines = [
        "HDE-EPIC038 ACCEPTANCE MAP VIABILITY",
        f"DECISION: {decision}",
        f"SOURCE_EVALUATION_FINGERPRINT: {snapshot.fingerprint}",
    ]
    for item in results:
        lines.append(
            f"TOKEN {item.token}: {item.status} | PREDICATE: {item.predicate_key} | DETAIL: {item.detail}"
        )
    lines.append(f"PROOF_FAMILY_COUNT: {len(snapshot.proof_families)}")
    for family in snapshot.proof_families:
        lines.append(
            "PROOF_FAMILY "
            f"{family['token']} | {family['artifact_key']} | "
            f"{family['primary_evidence']} | {family['proof_anchor']} | "
            f"{family['classification']}"
        )
    for item in snapshot.obligations:
        if item.get("label") in NON_TOKEN_OBLIGATIONS:
            lines.append(
                f"NON_TOKEN {item['label']}: {item['status']} | "
                f"PREDICATE: {item['predicate_key']} | DETAIL: {item['detail']}"
            )
    for item in snapshot.obligations:
        if item.get("label") not in NON_TOKEN_OBLIGATIONS:
            lines.append(
                f"OBLIGATION {item['predicate_key']}: {item['status']} | DETAIL: {item['detail']}"
            )
    for value in minimum:
        lines.append(f"MINIMUM_FOLLOW_UP: {value}")
    return ("\n".join(lines) + "\n").encode("utf-8")


def _report_bytes(
    snapshot: EvaluationSnapshot,
    results: Sequence[TokenResult],
    decision: str,
    minimum: Sequence[str],
) -> bytes:
    authority = _plan_authority()
    qa_source = (ROOT / QA_RCA_PATH).read_text(encoding="utf-8")
    lines = [
        "# HDE-EPIC038 Close Report",
        "",
        f"## Final decision: {decision}",
        "",
        "DEV-02 in-memory package validation: PASS",
        (
            "Source-tree planned tokens remain UNCLAIMED at the Gate D "
            "pre-generation boundary. This provisional candidate promotes them only "
            "after every reused and non-token predicate passes and the actual generated "
            "primary bytes validate; DEV-03 must still establish their governed proofs "
            "and Human Index/Machine Mirror bindings."
        ),
        "",
        "## Exact package pointers",
    ]
    lines.extend(f"- {key}: {path}" for key, path in KEY_OUTPUTS.items())
    lines.extend(["", "## Token outcomes"])
    lines.extend(
        f"- {item.token}: {item.status}; predicate={item.predicate_key}; detail={item.detail}"
        for item in results
    )
    lines.extend(["", "## Full intended proof-family roster"])
    lines.extend(
        f"- {item['token']} | {item['artifact_key']} | {item['primary_evidence']} | {item['proof_anchor']} | {item['classification']}"
        for item in snapshot.proof_families
    )
    lines.extend(["", "## Required non-token proof obligations"])
    for item in snapshot.obligations:
        if item.get("label") in NON_TOKEN_OBLIGATIONS:
            lines.append(
                f"- {item['label']}: {item['status']}; {item['artifact_key']} -> {item['path']}; {item['detail']}"
            )
    lines.extend(["", "## PF09 scope"])
    lines.extend(f"- {item}" for item in authority["pf09_scope"])
    lines.extend(["", "## Explicit PF09 exclusions"])
    lines.extend(f"- {item}" for item in authority["pf09_exclusions"])
    lines.extend(
        [
            "",
            "## Embedded complete QA RCA and Doc Delta accounting",
            (
                f"Preserved execution-level source evidence: {QA_RCA_PATH}. This is "
                "not the canonical standalone closeout-summary path."
            ),
            "",
            qa_source.rstrip("\n"),
            "",
            "### Closeout-level accounting derived from approved r5",
            json.dumps(QA_CLOSEOUT_ACCOUNTING, ensure_ascii=False, sort_keys=True),
            "",
            "## Tracked issues",
        ]
    )
    for label, record in authority["tracked_issues"].items():
        lines.extend(
            [
                f"### {label}",
                f"- Disposition: {record['disposition']}",
                f"- Detail: {record['detail']}",
            ]
        )
    lines.extend(["", "## PF06 §3.5.4 ADR records"])
    for record in authority["adr_records"]:
        lines.extend(
            [
                f"### {record['label']}",
                f"- Decision point: {record['decision_point']}",
                "- Options:",
                *(f"  - {option}" for option in record["options"]),
                f"- Governing canon: {'; '.join(record['governing_canon'])}",
                f"- Final decision: {record['final_decision']}",
                f"- Disposition: {record['disposition']}",
                f"- Drain targets: {'; '.join(record['drain_targets'])}",
            ]
        )
    lines.extend(
        [
            "",
            "## Superseded interim-readiness posture",
            str(QA_CLOSEOUT_ACCOUNTING["superseded_readiness"]),
            "",
            "## Reused proof disclosure",
            (
                "Every existing proof family is reused and revalidated against current "
                "bytes. No historical primary, proof, Index, Mirror, orientation, or "
                "checksum artifact is described as newly implemented or refreshed."
            ),
            "",
            "## Nonclaims",
            *(f"- No {item}." for item in NONCLAIMS),
        ]
    )
    if decision == "NOT SATISFIED":
        lines.extend(["", "## Minimum follow-up"])
        lines.extend(f"- {item}" for item in minimum)
    return ("\n".join(lines).rstrip("\n") + "\n").encode("utf-8")


def _construct_package(
    snapshot: EvaluationSnapshot, ledger: Mapping[str, object]
) -> dict[str, bytes]:
    validate_ledger(ledger)
    snapshot = _canonical_source_snapshot(snapshot)
    open_entries = [
        entry for entry in ledger["entries"] if entry["status"] == "OPEN"  # type: ignore[index]
    ]
    results = snapshot.token_results
    decision = (
        "SATISFIED"
        if all(item.status == "PASS" for item in results)
        and not snapshot.blockers
        and not open_entries
        else "NOT SATISFIED"
    )
    minimum = _minimum_follow_up(results, ledger)
    if decision == "NOT SATISFIED" and not minimum:
        minimum = [
            "Resolve every non-PASS predicate and OPEN remediation entry, then rerun the complete fixed-point suite."
        ]
    authority = _plan_authority()
    acceptance = _acceptance_payload(snapshot, results, decision, minimum)
    statuses = {item.token: item.status for item in results}
    source_statuses = {item.token: item.status for item in snapshot.token_results}
    manifest = {
        "adr_records": authority["adr_records"],
        "decision": decision,
        "epic_id": EPIC_ID,
        "evaluations": [item.as_dict() for item in results],
        "key_outputs": dict(KEY_OUTPUTS),
        "minimum_follow_up": minimum,
        "non_token_obligations": acceptance["non_token_obligations"],
        "nonclaims": list(NONCLAIMS),
        "pf09_exclusions": authority["pf09_exclusions"],
        "pf09_scope": authority["pf09_scope"],
        "plan_path": authority["plan_path"],
        "plan_sha256": authority["plan_sha256"],
        "proof_family_roster": [dict(item) for item in snapshot.proof_families],
        "qa_rca_source_path": QA_RCA_PATH,
        "qa_rca_source_sha256": hashlib.sha256(
            (ROOT / QA_RCA_PATH).read_bytes()
        ).hexdigest(),
        "schema": "hde.epic038.close_manifest.v1",
        "schema_version": "1.0",
        "source_evaluation_fingerprint": snapshot.fingerprint,
        "source_token_status": source_statuses,
        "token_roster": list(TOKENS),
        "token_status": statuses,
        "tracked_issues": authority["tracked_issues"],
    }
    checklist_result = (
        "PASS"
        if not open_entries
        and all(
            statuses[token] == "PASS" for token in PLANNED_BINDINGS
        )
        else "FAIL"
    )
    package = {
        CLOSE_REPORT_PATH: _report_bytes(snapshot, results, decision, minimum),
        CLOSE_MANIFEST_PATH: _canonical_json(manifest),
        ACCEPTANCE_MAP_PATH: _canonical_json(acceptance),
        OUTPUT.as_posix(): _matrix_bytes(),
        VIABILITY_PATH: _viability_bytes(snapshot, results, decision, minimum),
        LEDGER_PATH: render_ledger(ledger),
        PRECOMMIT_CHECKLIST_PATH: _render_checklist(
            "PRECOMMIT", result=checklist_result
        ),
        POSTCOMMIT_CHECKLIST_PATH: _render_checklist(
            "POSTCOMMIT", result=checklist_result
        ),
    }
    validated_results = _candidate_token_results(snapshot, package)
    if validated_results != results:
        raise ValueError("candidate result projection changed after primary-byte validation")
    return package


def build_package(
    *,
    ledger: Mapping[str, object] | None = None,
    evaluation_snapshot: EvaluationSnapshot | None = None,
) -> dict[str, bytes]:
    current = evaluate_closeout()
    if evaluation_snapshot is not None and evaluation_snapshot != current:
        raise ValueError("stale or caller-forged evaluation snapshot")
    selected = current
    _validate_snapshot_contract(selected)
    source_ledger = _load_ledger() if ledger is None else ledger
    validate_ledger(source_ledger)
    recorded = record_blockers(source_ledger, [dict(item) for item in selected.blockers])
    package = _construct_package(selected, recorded)
    validate_package(package)
    return package


def _load_canonical_object(data: bytes, label: str) -> dict[str, object]:
    try:
        payload = json.loads(data, object_pairs_hook=_unique_json_object)
    except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
        raise ValueError(f"invalid canonical JSON: {label}") from exc
    if not isinstance(payload, dict) or data != _canonical_json(payload):
        raise ValueError(f"invalid canonical JSON: {label}")
    return payload


def _bootstrap_snapshot(
    current: EvaluationSnapshot, package: Mapping[str, bytes]
) -> EvaluationSnapshot | None:
    if (
        any(
            not (ROOT / path).is_file()
            or (ROOT / path).read_bytes() != package[path]
            for path in PACKAGE_ACTIVATION_PATHS
        )
        or any(item.get("status") != "PASS" for item in current.obligations)
    ):
        return None
    planned_tokens = set(PLANNED_BINDINGS)
    if any(
        item.status != "PASS"
        for item in current.token_results
        if item.token not in planned_tokens
    ):
        return None
    if any(
        not (
            isinstance(blocker.get("subject"), dict)
            and blocker["subject"].get("kind") == "TOKEN"
            and blocker["subject"].get("value") in planned_tokens
            and str(blocker.get("predicate_key", "")).endswith(".planned_binding")
        )
        for blocker in current.blockers
    ):
        return None
    try:
        manifest = _load_canonical_object(
            package[CLOSE_MANIFEST_PATH], "bootstrap close manifest"
        )
    except (KeyError, ValueError):
        return None
    source_status = manifest.get("source_token_status")
    raw_evaluations = manifest.get("evaluations")
    if not isinstance(source_status, dict) or not isinstance(raw_evaluations, list):
        return None
    embedded: dict[str, TokenResult] = {}
    for raw in raw_evaluations:
        if not isinstance(raw, dict) or raw.get("token") not in planned_tokens:
            continue
        evidence = raw.get("decisive_evidence")
        if (
            raw.get("status") != "UNCLAIMED"
            or not isinstance(evidence, list)
            or any(
                not isinstance(item, dict)
                or set(item) != {"kind", "value"}
                or not isinstance(item["kind"], str)
                or not isinstance(item["value"], str)
                for item in evidence
            )
        ):
            return None
        token = str(raw["token"])
        if source_status.get(token) != raw.get("status"):
            return None
        embedded[token] = TokenResult(
            token,
            str(raw["status"]),
            str(raw.get("predicate_key", "")),
            str(raw.get("detail", "")),
            tuple((str(item["kind"]), str(item["value"])) for item in evidence),
            str(raw.get("minimum_follow_up", "")),
        )
    if set(embedded) != planned_tokens:
        return None
    normalized = tuple(
        embedded[item.token] if item.token in planned_tokens else item
        for item in current.token_results
    )
    result = _make_snapshot(
        normalized, current.proof_families, (), current.obligations
    )
    if result.fingerprint != manifest.get("source_evaluation_fingerprint"):
        return None
    return result


def validate_package_structure(package: Mapping[str, bytes]) -> None:
    if set(package) != set(PACKAGE_PATHS):
        raise ValueError("incomplete, partial, or unexpected package family")
    if any(
        not isinstance(value, bytes)
        or not value
        or not value.endswith(b"\n")
        or b"\r" in value
        for value in package.values()
    ):
        raise ValueError("package bytes are not canonical UTF-8/LF outputs")
    if hashlib.sha256(package[OUTPUT.as_posix()]).hexdigest() != TOKEN_MATRIX_SHA256:
        raise ValueError("package DEV-01 token matrix bytes mismatch")
    manifest = _load_canonical_object(package[CLOSE_MANIFEST_PATH], "close manifest")
    acceptance = _load_canonical_object(package[ACCEPTANCE_MAP_PATH], "acceptance map")
    pre = _load_canonical_object(package[PRECOMMIT_CHECKLIST_PATH], "precommit checklist")
    post = _load_canonical_object(package[POSTCOMMIT_CHECKLIST_PATH], "postcommit checklist")
    ledger = parse_ledger(package[LEDGER_PATH])
    authority = _plan_authority()
    try:
        qa_rca_source_bytes = (ROOT / QA_RCA_PATH).read_bytes()
    except OSError as exc:
        raise ValueError(f"QA RCA source unavailable: {QA_RCA_PATH}") from exc
    if (
        manifest.get("epic_id") != EPIC_ID
        or manifest.get("schema") != "hde.epic038.close_manifest.v1"
    ):
        raise ValueError("manifest epic/schema identity mismatch")
    if (
        manifest.get("plan_path") != authority["plan_path"]
        or manifest.get("plan_sha256") != authority["plan_sha256"]
    ):
        raise ValueError("manifest approved-plan authority mismatch")
    if (
        manifest.get("qa_rca_source_path") != QA_RCA_PATH
        or manifest.get("qa_rca_source_sha256")
        != hashlib.sha256(qa_rca_source_bytes).hexdigest()
    ):
        raise ValueError("manifest QA RCA source authority mismatch")
    if manifest.get("tracked_issues") != authority["tracked_issues"]:
        raise ValueError("manifest tracked-issue disposition mismatch")
    if manifest.get("adr_records") != authority["adr_records"]:
        raise ValueError("manifest PF06 §3.5.4 ADR block mismatch")
    if manifest.get("nonclaims") != list(NONCLAIMS):
        raise ValueError("manifest nonclaim roster mismatch")
    if not isinstance(manifest.get("key_outputs"), dict):
        raise ValueError("manifest key_outputs must be a named object")
    if manifest.get("key_outputs") != KEY_OUTPUTS:
        raise ValueError("manifest key_outputs mismatch")
    if manifest.get("token_roster") != list(TOKENS):
        raise ValueError("manifest corrected-roster mismatch")
    if manifest.get("schema_version") != "1.0":
        raise ValueError("manifest schema-version mismatch")
    if set(manifest.get("token_status", {})) != set(TOKENS):
        raise ValueError("manifest token-status roster/order mismatch")
    if manifest.get("pf09_scope") != list(PF09_SCOPE) or manifest.get(
        "pf09_exclusions"
    ) != list(PF09_EXCLUSIONS):
        raise ValueError("manifest PF09 scope/exclusion mismatch")
    if set(manifest.get("tracked_issues", {})) != set(TRACKED_ISSUES):
        raise ValueError("manifest tracked-issue disposition mismatch")
    adrs = manifest.get("adr_records")
    if (
        not isinstance(adrs, list)
        or tuple(item.get("label") for item in adrs if isinstance(item, dict))
        != tuple(item["label"] for item in ADR_RECORDS)
        or any(
            not isinstance(item, dict)
            or not isinstance(item.get("options"), list)
            or len(item["options"]) < 2
            for item in adrs
        )
    ):
        raise ValueError("manifest PF06 §3.5.4 ADR block mismatch")
    evaluations = manifest.get("evaluations")
    if (
        not isinstance(evaluations, list)
        or tuple(item.get("token") for item in evaluations if isinstance(item, dict))
        != TOKENS
        or any(
            not isinstance(item, dict)
            or set(item)
            != {
                "decisive_evidence",
                "detail",
                "minimum_follow_up",
                "predicate_key",
                "status",
                "token",
            }
            or item.get("status") not in {"PASS", "UNCLAIMED", "FAIL"}
            or not item.get("detail")
            or not isinstance(item.get("decisive_evidence"), list)
            or not item.get("decisive_evidence")
            or any(
                not isinstance(evidence, dict)
                or set(evidence) != {"kind", "value"}
                or not isinstance(evidence.get("kind"), str)
                or not evidence.get("kind")
                or not isinstance(evidence.get("value"), str)
                or not evidence.get("value")
                for evidence in item.get("decisive_evidence", [])
            )
            or (
                item.get("status") == "PASS"
                and item.get("minimum_follow_up") != "NONE"
            )
            for item in evaluations
        )
    ):
        raise ValueError("manifest affirmative evaluation roster mismatch")
    evaluation_by_token = {
        str(item["token"]): item for item in evaluations if isinstance(item, dict)
    }
    if manifest.get("token_status") != {
        token: evaluation_by_token[token]["status"] for token in TOKENS
    }:
        raise ValueError("forced SATISFIED or manifest token-status/evaluation mismatch")
    source_status = manifest.get("source_token_status")
    if (
        not isinstance(source_status, dict)
        or set(source_status) != set(TOKENS)
        or any(value not in {"PASS", "UNCLAIMED", "FAIL"} for value in source_status.values())
        or any(
            source_status[token] != evaluation_by_token[token]["status"]
            for token in TOKENS
        )
    ):
        raise ValueError("manifest canonical source-token status mismatch")
    decision = manifest.get("decision")
    if decision not in {"SATISFIED", "NOT SATISFIED"}:
        raise ValueError("invalid binary closeout decision")
    token_status = manifest["token_status"]
    open_entries = any(entry["status"] == "OPEN" for entry in ledger["entries"])
    expected_decision = (
        "SATISFIED"
        if all(token_status[token] == "PASS" for token in TOKENS)
        and not open_entries
        else "NOT SATISFIED"
    )
    if decision != expected_decision:
        raise ValueError("forced SATISFIED or close-report/manifest decision mismatch")
    minimum = manifest.get("minimum_follow_up")
    if (
        not isinstance(minimum, list)
        or minimum != sorted(set(minimum))
        or (decision == "NOT SATISFIED" and not minimum)
        or (decision == "SATISFIED" and minimum)
    ):
        raise ValueError("NOT SATISFIED minimum follow-up mismatch")
    if acceptance.get("decision") != decision:
        raise ValueError("close-report and manifest decision mismatch")
    if acceptance.get("schema_version") != "1.0":
        raise ValueError("acceptance-map schema-version mismatch")
    if acceptance.get("pf09_scope") != list(PF09_SCOPE):
        raise ValueError("acceptance map PF09 scope mismatch")
    if tuple(
        item.get("token")
        for item in acceptance.get("records", [])
        if isinstance(item, dict)
    ) != TOKENS:
        raise ValueError("acceptance map reduced proof-family roster")
    acceptance_records = acceptance.get("records", [])
    if any(
        not isinstance(item, dict)
        or item.get("status") != manifest["token_status"].get(item.get("token"))
        or item.get("result") != evaluation_by_token.get(str(item.get("token")))
        for item in acceptance_records
    ):
        raise ValueError("acceptance map token-result mismatch")
    if acceptance.get("proof_family_roster") != manifest.get("proof_family_roster"):
        raise ValueError("acceptance map reduced proof-family roster")
    if tuple(
        item.get("label")
        for item in acceptance.get("non_token_obligations", [])
        if isinstance(item, dict)
    ) != NON_TOKEN_OBLIGATIONS:
        raise ValueError("acceptance map non-token obligation roster mismatch")
    proof_roster = manifest.get("proof_family_roster")
    expected_proof_roster = [
        dict(item) for item in _proof_family_records(tuple(build_rows()))
    ]
    if proof_roster != expected_proof_roster:
        raise ValueError("manifest proof-family roster mismatch")
    non_token_obligations = acceptance.get("non_token_obligations")
    if (
        not isinstance(non_token_obligations, list)
        or manifest.get("non_token_obligations") != non_token_obligations
        or any(
            not isinstance(item, dict)
            or set(item)
            != {
                "artifact_key",
                "detail",
                "label",
                "path",
                "predicate_key",
                "status",
            }
            or item.get("status") not in {"PASS", "FAIL"}
            or not isinstance(item.get("detail"), str)
            or not item.get("detail")
            for item in non_token_obligations
        )
    ):
        raise ValueError("manifest non-token obligation payload mismatch")
    source_fingerprint = manifest.get("source_evaluation_fingerprint")
    if not isinstance(source_fingerprint, str) or not _hex64(source_fingerprint):
        raise ValueError("manifest source-evaluation fingerprint mismatch")
    token_results = tuple(
        TokenResult(
            str(item["token"]),
            str(item["status"]),
            str(item["predicate_key"]),
            str(item["detail"]),
            tuple(
                (str(evidence["kind"]), str(evidence["value"]))
                for evidence in item["decisive_evidence"]
            ),
            str(item["minimum_follow_up"]),
        )
        for item in evaluations
    )
    obligation_keys = (
        "qa.finalized_current_state",
        "evidence.full_index_mirror_topology",
        "authority.approved_r5_source",
        *(f"authority.pf09_scope.{item}" for item in PF09_SCOPE),
        *(f"authority.pf09_exclusion.{item}" for item in PF09_EXCLUSIONS),
        *(f"authority.tracked_issue.{item}" for item in TRACKED_ISSUES),
        *(f"authority.adr.{item['label']}" for item in ADR_RECORDS),
        "authority.qa_rca_source",
    )
    try:
        viability_lines = package[VIABILITY_PATH].decode("utf-8").splitlines()
    except UnicodeError as exc:
        raise ValueError("viability log is not UTF-8") from exc
    cursor = 0

    def require_viability_line(expected: str) -> None:
        nonlocal cursor
        if cursor >= len(viability_lines) or viability_lines[cursor] != expected:
            raise ValueError(f"viability log canonical line mismatch: {expected}")
        cursor += 1

    require_viability_line("HDE-EPIC038 ACCEPTANCE MAP VIABILITY")
    require_viability_line(f"DECISION: {decision}")
    require_viability_line(f"SOURCE_EVALUATION_FINGERPRINT: {source_fingerprint}")
    for item in token_results:
        require_viability_line(
            f"TOKEN {item.token}: {item.status} | PREDICATE: "
            f"{item.predicate_key} | DETAIL: {item.detail}"
        )
    require_viability_line(f"PROOF_FAMILY_COUNT: {len(proof_roster)}")
    for family in proof_roster:
        require_viability_line(
            "PROOF_FAMILY "
            f"{family['token']} | {family['artifact_key']} | "
            f"{family['primary_evidence']} | {family['proof_anchor']} | "
            f"{family['classification']}"
        )
    for item in non_token_obligations:
        require_viability_line(
            f"NON_TOKEN {item['label']}: {item['status']} | "
            f"PREDICATE: {item['predicate_key']} | DETAIL: {item['detail']}"
        )
    structural_obligations: list[Mapping[str, object]] = []
    for predicate_key in obligation_keys:
        prefix = f"OBLIGATION {predicate_key}: "
        if cursor >= len(viability_lines) or not viability_lines[cursor].startswith(prefix):
            raise ValueError(f"viability obligation roster mismatch: {predicate_key}")
        rendered = viability_lines[cursor][len(prefix) :]
        status, separator, detail = rendered.partition(" | DETAIL: ")
        if separator != " | DETAIL: " or status not in {"PASS", "FAIL"} or not detail:
            raise ValueError(f"viability obligation payload mismatch: {predicate_key}")
        structural_obligations.append(
            {
                "detail": detail,
                "predicate_key": predicate_key,
                "status": status,
            }
        )
        cursor += 1
    for follow_up in minimum:
        require_viability_line(f"MINIMUM_FOLLOW_UP: {follow_up}")
    if cursor != len(viability_lines):
        raise ValueError("viability log has unexpected trailing or duplicate lines")
    fingerprint_obligations = _fingerprint_obligations(
        (*structural_obligations, *non_token_obligations)
    )
    source_results = _source_results_for_fingerprint(token_results, source_status)
    source_blockers = _fingerprint_blockers(
        source_results, fingerprint_obligations
    )
    recomputed_source = _make_snapshot(
        source_results,
        tuple(proof_roster),
        source_blockers,
        fingerprint_obligations,
    )
    if recomputed_source.fingerprint != source_fingerprint:
        raise ValueError("source-evaluation fingerprint payload mismatch")
    structural_snapshot = EvaluationSnapshot(
        token_results,
        tuple(proof_roster),
        (),
        fingerprint_obligations,
        source_fingerprint,
    )
    expected_manifest = {
        "adr_records": authority["adr_records"],
        "decision": decision,
        "epic_id": EPIC_ID,
        "evaluations": [item.as_dict() for item in token_results],
        "key_outputs": dict(KEY_OUTPUTS),
        "minimum_follow_up": minimum,
        "non_token_obligations": non_token_obligations,
        "nonclaims": list(NONCLAIMS),
        "pf09_exclusions": authority["pf09_exclusions"],
        "pf09_scope": authority["pf09_scope"],
        "plan_path": authority["plan_path"],
        "plan_sha256": authority["plan_sha256"],
        "proof_family_roster": [dict(item) for item in proof_roster],
        "qa_rca_source_path": QA_RCA_PATH,
        "qa_rca_source_sha256": hashlib.sha256(qa_rca_source_bytes).hexdigest(),
        "schema": "hde.epic038.close_manifest.v1",
        "schema_version": "1.0",
        "source_evaluation_fingerprint": source_fingerprint,
        "source_token_status": dict(source_status),
        "token_roster": list(TOKENS),
        "token_status": {
            item.token: item.status for item in token_results
        },
        "tracked_issues": authority["tracked_issues"],
    }
    if manifest != expected_manifest:
        raise ValueError("close manifest canonical payload mismatch")
    if package[VIABILITY_PATH] != _viability_bytes(
        structural_snapshot, token_results, decision, minimum
    ):
        raise ValueError("viability log canonical bytes mismatch")
    expected_acceptance = _acceptance_payload(
        structural_snapshot, token_results, decision, minimum
    )
    if acceptance != expected_acceptance:
        raise ValueError("acceptance map canonical bytes mismatch")
    if package[CLOSE_REPORT_PATH] != _report_bytes(
        structural_snapshot, token_results, decision, minimum
    ):
        raise ValueError("close report canonical bytes mismatch")
    report = package[CLOSE_REPORT_PATH].decode("utf-8")
    qa_source = (ROOT / QA_RCA_PATH).read_text(encoding="utf-8").rstrip("\n")
    if qa_source not in report:
        raise ValueError("close report does not embed the complete QA RCA/Doc Delta source")
    if any(item not in report for item in PF09_SCOPE):
        raise ValueError("close report PF09 scope mismatch")
    if any(item not in report for item in TRACKED_ISSUES):
        raise ValueError("close report tracked-issue disposition mismatch")
    if any(str(item["label"]) not in report for item in ADR_RECORDS):
        raise ValueError("close report PF06 §3.5.4 ADR block mismatch")
    if f"## Final decision: {decision}" not in report:
        raise ValueError("close-report and manifest decision mismatch")
    if decision == "NOT SATISFIED" and "## Minimum follow-up" not in report:
        raise ValueError("NOT SATISFIED without minimum follow-up")
    checklist_result = pre.get("result")
    if checklist_result not in {"PASS", "FAIL"} or post.get("result") != checklist_result:
        raise ValueError("checklist result mismatch")
    expected_checklist_result = (
        "PASS"
        if all(token_status[token] == "PASS" for token in PLANNED_BINDINGS)
        and not open_entries
        else "FAIL"
    )
    if checklist_result != expected_checklist_result:
        raise ValueError("checklist result lacks execution-derived token support")
    if pre != json.loads(_render_checklist("PRECOMMIT", result=checklist_result)):
        raise ValueError("precommit checklist mismatch")
    if post != json.loads(_render_checklist("POSTCOMMIT", result=checklist_result)):
        raise ValueError("postcommit checklist mismatch")
    recorded = record_blockers(
        ledger, [dict(blocker) for blocker in source_blockers]
    )
    if recorded != ledger:
        raise ValueError("remediation ledger omits a canonical source blocker")
    reconstructed_package = _construct_package(recomputed_source, ledger)
    if any(
        reconstructed_package[path] != package[path]
        for path in PACKAGE_PATHS
    ):
        raise ValueError("closeout package canonical reconstruction mismatch")


def validate_package(package: Mapping[str, bytes]) -> None:
    validate_package_structure(package)
    ledger = parse_ledger(package[LEDGER_PATH])
    snapshot = evaluate_closeout()
    recorded = record_blockers(ledger, [dict(item) for item in snapshot.blockers])
    if recorded != ledger:
        raise ValueError("package ledger suppresses a current blocker")
    expected = _construct_package(snapshot, ledger)
    drift = [path for path in PACKAGE_PATHS if package[path] != expected[path]]
    if drift:
        raise ValueError("package cross-surface mismatch: " + ",".join(drift))


def _validate_package_for_canonical_updater(
    package: Mapping[str, bytes],
) -> None:
    """Validate one whole canonical projection without consuming private CI files."""

    validate_package_structure(package)
    ledger = parse_ledger(package[LEDGER_PATH])
    projections = (
        _PrivateCiEvidence(
            "ABSENT",
            "no private external exact-source release attestation was supplied",
            "ABSENT",
            "no private external exact-command CI receipt was supplied",
        ),
        _PrivateCiEvidence(
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
            "FAIL",
            PRIVATE_CI_INVALID_DETAIL,
        ),
        _PrivateCiEvidence(
            "PASS",
            PRIVATE_CI_ATTESTATION_PASS_DETAIL,
            "PASS",
            PRIVATE_CI_RECEIPT_PASS_DETAIL,
        ),
    )
    for private_evidence in projections:
        snapshot = _evaluate_closeout(private_evidence)
        recorded = record_blockers(
            ledger, [dict(item) for item in snapshot.blockers]
        )
        if recorded != ledger:
            continue
        expected = _construct_package(snapshot, ledger)
        if all(package[path] == expected[path] for path in PACKAGE_PATHS):
            return
    raise ValueError("package is not one complete canonical external-gate projection")


_provisional_validate_ledger = validate_ledger


def validate_ledger(payload: Mapping[str, object]) -> None:
    _provisional_validate_ledger(payload)
    entries = payload["entries"]
    by_identity: dict[tuple[str, str, str], list[Mapping[str, object]]] = {}
    for raw_entry in entries:  # type: ignore[assignment]
        entry = raw_entry
        subject = entry["subject"]
        identity = (
            str(entry["predicate_key"]),
            str(subject["kind"]),
            str(subject["value"]),
        )
        by_identity.setdefault(identity, []).append(entry)
        if entry["failure_class"] not in FAILURE_OWNERS:
            raise ValueError("invalid ledger failure class")
        if entry["permitted_files"] != sorted(set(entry["permitted_files"])):
            raise ValueError("ledger permitted-files ordering mismatch")
        if entry["regenerated_artifacts"] != sorted(
            set(entry["regenerated_artifacts"])
        ):
            raise ValueError("ledger regenerated-artifact ordering mismatch")
        validators = entry["required_validator_ids"]
        if validators != sorted(set(validators)):
            raise ValueError("ledger validator roster ordering mismatch")
        evidence_identities = [
            (item["kind"], item["value"]) for item in entry["decisive_evidence"]
        ]
        if len(evidence_identities) != len(set(evidence_identities)):
            raise ValueError("ledger decisive evidence is duplicated")
        if entry["status"] == "CLOSED":
            results = entry["tests_and_validators"]
            if [item["id"] for item in results] != validators:
                raise ValueError("ledger closure validator roster mismatch")
    for identity, occurrences in by_identity.items():
        suffixes = [int(str(entry["blocker_id"])[-4:]) for entry in occurrences]
        if suffixes != list(range(1, len(occurrences) + 1)):
            raise ValueError(f"ledger recurrence sequence mismatch: {identity}")
        if sum(entry["status"] == "OPEN" for entry in occurrences) > 1:
            raise ValueError(f"ledger identity has multiple OPEN entries: {identity}")


def _validate_descriptor_payload(descriptor: Mapping[str, object]) -> None:
    fields = {
        "decisive_command",
        "decisive_evidence",
        "external_action_posture",
        "failing_predicate",
        "failure_class",
        "minimum_follow_up",
        "owner",
        "permitted_files",
        "predicate_key",
        "required_validator_ids",
        "subject",
    }
    if set(descriptor) != fields:
        raise ValueError("invalid blocker descriptor fields")
    rebuilt = _descriptor(
        str(descriptor["predicate_key"]),
        str(descriptor["subject"]["kind"]),  # type: ignore[index]
        str(descriptor["subject"]["value"]),  # type: ignore[index]
        str(descriptor["failing_predicate"]),
        list(descriptor["decisive_evidence"]),  # type: ignore[arg-type]
        str(descriptor["decisive_command"]),
        str(descriptor["failure_class"]),
        list(descriptor["permitted_files"]),  # type: ignore[arg-type]
        str(descriptor["minimum_follow_up"]),
        list(descriptor["required_validator_ids"]),  # type: ignore[arg-type]
        str(descriptor["external_action_posture"]),
    )
    if rebuilt != descriptor:
        raise ValueError("noncanonical blocker descriptor")


def record_blockers(
    ledger: Mapping[str, object], blockers: list[dict[str, object]]
) -> dict[str, object]:
    validate_ledger(ledger)
    entries = [dict(entry) for entry in ledger["entries"]]  # type: ignore[index]
    ordered = sorted(
        blockers,
        key=lambda item: (
            str(item["predicate_key"]),
            json.dumps(item["subject"], sort_keys=True),
        ),
    )
    descriptor_fields = {
        "decisive_command",
        "decisive_evidence",
        "external_action_posture",
        "failing_predicate",
        "failure_class",
        "minimum_follow_up",
        "owner",
        "permitted_files",
        "predicate_key",
        "required_validator_ids",
        "subject",
    }
    for descriptor in ordered:
        _validate_descriptor_payload(descriptor)
        matching = [
            entry
            for entry in entries
            if entry["predicate_key"] == descriptor["predicate_key"]
            and entry["subject"] == descriptor["subject"]
        ]
        open_matches = [entry for entry in matching if entry["status"] == "OPEN"]
        if open_matches:
            immutable = {
                key: open_matches[0][key] for key in descriptor_fields
            }
            if immutable != descriptor:
                raise ValueError("OPEN blocker descriptor changed without closure")
            continue
        occurrence = len(matching) + 1
        entry = dict(descriptor)
        entry.update(
            {
                "after_outcome": None,
                "before_outcome": {
                    "detail": descriptor["failing_predicate"],
                    "result": "FAIL",
                },
                "blocker_id": _blocker_id(
                    str(descriptor["predicate_key"]),
                    descriptor["subject"],  # type: ignore[arg-type]
                    occurrence,
                ),
                "correction_performed": None,
                "historical_evidence_rewritten": False,
                "regenerated_artifacts": [],
                "reviewer_disposition": "PENDING_REVIEW",
                "status": "OPEN",
                "tests_and_validators": [],
            }
        )
        entries.append(entry)
    result = _empty_ledger()
    result["entries"] = sorted(entries, key=lambda item: item["blocker_id"])
    validate_ledger(result)
    return result


def _matrix_bytes() -> bytes:
    path = ROOT / OUTPUT
    if not path.is_file():
        raise ValueError(f"missing approved DEV-01 token matrix: {OUTPUT}")
    return path.read_bytes()


def evaluate_registered_predicate(entry: Mapping[str, object]) -> tuple[bool, str]:
    subject = entry.get("subject")
    if not isinstance(subject, dict):
        return False, "registered predicate subject is malformed"
    predicate_key = str(entry.get("predicate_key", ""))
    value = str(subject.get("value", ""))
    if subject.get("kind") == "TOKEN" and value in TOKENS:
        result = {item.token: item for item in evaluate_closeout().token_results}[value]
        if predicate_key.endswith(".planned_binding"):
            passed = result.status in {"UNCLAIMED", "PASS"}
        else:
            passed = result.status == "PASS"
        return passed, result.detail
    if value in NON_TOKEN_OBLIGATIONS:
        try:
            detail = _validate_non_token_family(value)
        except (OSError, UnicodeError, ValueError) as exc:
            return False, str(exc)
        return True, detail
    validators: Mapping[str, Callable[[], None]] = {
        "qa.finalized_current_state": _validate_finalized_qa_state,
        "evidence.full_index_mirror_topology": lambda: (
            validate_index_mirror_topology(),
            validate_all_mirror_proofs(),
        ),
        "authority.approved_r5_source": lambda: _plan_authority() and None,
    }
    validator = validators.get(predicate_key)
    if validator is None:
        return False, "predicate has no source-controlled closure evaluator"
    try:
        validator()
    except (OSError, UnicodeError, ValueError) as exc:
        return False, str(exc)
    return True, "registered current predicate validates"


def run_registered_validator(
    validator_id: str, *, package: Mapping[str, bytes] | None = None
) -> dict[str, object]:
    if validator_id == "closeout_package_in_memory":
        if package is None:
            raise ValueError("in-memory package bytes are required")
        validate_package(package)
        return {
            "command": "internal:validate_package(actual package bytes)",
            "exit_code": 0,
            "id": validator_id,
            "result": "PASS",
        }
    if validator_id == "epic038_current_state":
        command = [
            sys.executable,
            str(ROOT / "tools/evidence/check_hde_epic038_qa_current_state.py"),
            "--require-finalized",
        ]
        result = subprocess.run(
            command,
            cwd=ROOT,
            env={
                **os.environ,
                "SAFE_MODE": "1",
                "ALLOW_NETWORK": "0",
                "APP_ENV": "dev",
                "LC_ALL": "C",
                "LANG": "C",
                "TZ": "UTC",
            },
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            detail = (result.stdout + result.stderr).strip()
            raise ValueError(
                f"validator failed: {validator_id}: {detail or result.returncode}"
            )
        return {
            "command": (
                "python tools/evidence/check_hde_epic038_qa_current_state.py "
                "--require-finalized"
            ),
            "exit_code": 0,
            "id": validator_id,
            "result": "PASS",
        }
    raise ValueError(f"unknown registered validator: {validator_id}")


def close_blocker(raw_request: str) -> dict[str, bytes]:
    request = _parse_close_request(raw_request)
    ledger = _load_ledger()
    validate_ledger(ledger)
    entries = [dict(entry) for entry in ledger["entries"]]  # type: ignore[index]
    matches = [
        entry
        for entry in entries
        if entry["blocker_id"] == request["blocker_id"]
        and entry["status"] == "OPEN"
    ]
    if len(matches) != 1:
        raise RuntimeError("close request does not identify exactly one OPEN entry")
    entry = matches[0]
    if entry["external_action_posture"] != "NONE_REQUIRED" or request[
        "external_action_posture"
    ] != "NONE_REQUIRED":
        raise RuntimeError(
            "Product Owner authorization and separately bound evidence are required"
        )
    regenerated = set(request["regenerated_artifacts"])
    if not regenerated.issubset(set(entry["permitted_files"])):
        raise RuntimeError("regenerated artifacts exceed the recorded permitted scope")
    passed, detail = evaluate_registered_predicate(entry)
    if not passed:
        raise RuntimeError(detail)
    validator_ids = list(entry["required_validator_ids"])
    results: list[dict[str, object]] = []
    package_receipt = {
        "command": "internal:validate_package(actual package bytes)",
        "exit_code": 0,
        "id": "closeout_package_in_memory",
        "result": "PASS",
    }
    for validator_id in validator_ids:
        if validator_id == "closeout_package_in_memory":
            results.append(dict(package_receipt))
        else:
            results.append(run_registered_validator(str(validator_id)))
    entry.update(
        {
            "after_outcome": {"detail": detail, "result": "PASS"},
            "correction_performed": request["correction_performed"],
            "external_action_posture": request["external_action_posture"],
            "regenerated_artifacts": request["regenerated_artifacts"],
            "reviewer_disposition": "CLOSURE_VALIDATED",
            "status": "CLOSED",
            "tests_and_validators": results,
        }
    )
    updated = _empty_ledger()
    updated["entries"] = sorted(entries, key=lambda item: item["blocker_id"])
    validate_ledger(updated)
    snapshot = evaluate_closeout()
    remaining = [dict(item) for item in snapshot.blockers]
    recorded = record_blockers(updated, remaining)
    package = _construct_package(snapshot, recorded)
    if "closeout_package_in_memory" in validator_ids:
        actual = run_registered_validator(
            "closeout_package_in_memory", package=package
        )
        if actual != package_receipt:
            raise RuntimeError("in-memory validator receipt mismatch")
    else:
        validate_package(package)
    return package


def _write_package(package: Mapping[str, bytes]) -> None:
    validate_package(package)
    changed = [
        rel
        for rel in PACKAGE_PATHS
        if not (ROOT / rel).is_file() or (ROOT / rel).read_bytes() != package[rel]
    ]
    if not changed:
        return
    staged: dict[Path, Path] = {}
    originals: dict[Path, bytes | None] = {}
    modes: dict[Path, int] = {}
    created_dirs: list[Path] = []
    replaced: list[Path] = []
    try:
        for rel in changed:
            target = ROOT / rel
            missing_parents: list[Path] = []
            parent = target.parent
            while parent != ROOT and not parent.exists():
                missing_parents.append(parent)
                parent = parent.parent
            for directory in reversed(missing_parents):
                directory.mkdir()
                created_dirs.append(directory)
            originals[target] = target.read_bytes() if target.is_file() else None
            modes[target] = target.stat().st_mode & 0o777 if target.exists() else 0o644
            staged[target] = _stage_atomic_bytes(target, package[rel], modes[target])
            if staged[target].read_bytes() != package[rel]:
                raise OSError(f"staged package byte mismatch: {rel}")
        for rel in changed:
            target = ROOT / rel
            os.replace(staged[target], target)
            replaced.append(target)
    except BaseException:
        rollback_error: BaseException | None = None
        for target in reversed(replaced):
            try:
                prior = originals[target]
                if prior is None:
                    target.unlink(missing_ok=True)
                else:
                    rollback = _stage_atomic_bytes(target, prior, modes[target])
                    os.replace(rollback, target)
            except BaseException as exc:
                rollback_error = exc
        if rollback_error is not None:
            raise RuntimeError("package replacement and rollback both failed") from rollback_error
        raise
    finally:
        for path in staged.values():
            path.unlink(missing_ok=True)
        for directory in reversed(created_dirs):
            try:
                directory.rmdir()
            except OSError:
                pass


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    mode = parser.add_mutually_exclusive_group(required=False)
    mode.add_argument("--token-matrix", action="store_true")
    mode.add_argument("--check-token-matrix", action="store_true")
    mode.add_argument("--doc-deltas", action="store_true")
    mode.add_argument("--check-doc-deltas", action="store_true")
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument("--check", action="store_true")
    mode.add_argument("--record-blockers", action="store_true")
    mode.add_argument("--close-blocker", metavar="CLOSE_REQUEST_JSON")
    args = parser.parse_args()
    if args.doc_deltas:
        write_doc_delta_pair()
        print(
            "WROTE DOC_DELTA_PAIR "
            f"sha256={DOC_DELTA_CURRENT_PAIR_SHA256} size_bytes="
            f"{len(render_doc_delta_pair())}"
        )
        return 0
    if args.check_doc_deltas:
        try:
            check_doc_delta_pair()
            validate_doc_delta_evidence()
        except ValueError as exc:
            print(f"DOC_DELTA_PAIR_DRIFT: {exc}")
            return 1
        print(
            "DOC_DELTA_PAIR_OK "
            f"sha256={DOC_DELTA_CURRENT_PAIR_SHA256} size_bytes="
            f"{len(render_doc_delta_pair())} historical_origin_only="
            f"{DOC_DELTA_HISTORICAL_PAIR_SHA256}"
        )
        return 0
    if args.preflight:
        try:
            snapshot = evaluate_closeout()
            blockers = [dict(item) for item in snapshot.blockers]
            ledger = _load_ledger()
            projected = record_blockers(ledger, blockers)
        except ValueError as exc:
            print(f"PREFLIGHT_BLOCKER: {exc}")
            return 1
        by_identity = {
            (entry["predicate_key"], json.dumps(entry["subject"], sort_keys=True)): entry["blocker_id"]
            for entry in projected["entries"]
        }
        for blocker in blockers:
            item = dict(blocker)
            item["blocker_id"] = by_identity[
                (
                    blocker["predicate_key"],
                    json.dumps(blocker["subject"], sort_keys=True),
                )
            ]
            print(_canonical_json(item).decode(), end="")
        pending = sum(
            item.token in PLANNED_BINDINGS and item.status == "UNCLAIMED"
            for item in snapshot.token_results
        )
        open_ledger = sum(
            entry["status"] == "OPEN" for entry in projected["entries"]
        )
        print(
            f"PREFLIGHT {'OK' if not blockers and not open_ledger else 'BLOCKED'} "
            f"blockers={len(blockers)} open_ledger={open_ledger} "
            f"planned_unclaimed={pending} "
            f"fingerprint={snapshot.fingerprint}"
        )
        return 0 if not blockers and not open_ledger else 1
    if args.close_blocker is not None:
        try: package = close_blocker(args.close_blocker)
        except ValueError as exc:
            parser.error(str(exc))
        except RuntimeError as exc:
            print(f"CLOSE_BLOCKER_FAILED: {exc}"); return 1
        _write_package(package); print("CLOSED BLOCKER AND WROTE COMPLETE PACKAGE"); return 0
    if args.check or args.record_blockers or not any((args.token_matrix, args.check_token_matrix, args.doc_deltas, args.check_doc_deltas)):
        try: package = build_package()
        except ValueError as exc:
            print(f"CLOSEOUT_GENERATION_FAILED: {exc}"); return 1
        if args.check:
            drift = [rel for rel, expected_bytes in package.items() if not (ROOT / rel).is_file() or (ROOT / rel).read_bytes() != expected_bytes]
            if drift: print("CLOSEOUT_PACKAGE_DRIFT: " + ",".join(drift)); return 1
            print("CLOSEOUT_PACKAGE_OK"); return 0
        _write_package(package); print("WROTE COMPLETE HDE-EPIC038 PACKAGE"); return 0
    expected = render(planned_mode="allow-current")
    target = ROOT / OUTPUT
    if args.token_matrix:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(expected)
        print(f"WROTE {OUTPUT}")
        return 0
    actual = target.read_bytes() if target.is_file() else b""
    if actual != expected:
        diff = difflib.unified_diff(
            actual.decode("utf-8", "replace").splitlines(),
            expected.decode().splitlines(),
            fromfile=str(OUTPUT),
            tofile="expected",
            lineterm="",
        )
        print("TOKEN_MATRIX_DRIFT\n" + "\n".join(diff))
        return 1
    print("TOKEN_MATRIX_OK rows=33 unique=33 claimed=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
