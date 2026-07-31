#!/usr/bin/env python3
"""Generate/check HDE-EPIC038 DEV-01 matrix and doc-delta evidence."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import sys
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.presenter import emitter

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
    expected_direct_job_keys = ("runs-on", "env", "steps")
    expected_env_block = (
        "      LC_ALL: C",
        "      LANG: C",
        "      TZ: UTC",
        '      SAFE_MODE: "1"',
        '      ALLOW_NETWORK: "0"',
        "      APP_ENV: dev",
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
        "      - uses: actions/setup-python@v5",
        "        with:",
        "          python-version: '3.12'",
        *expected_step_block,
        "      - name: Run HDE-EPIC038 DEV-01 focused tests",
        "        shell: bash",
        "        run: |",
        "          set -euo pipefail",
        "          python -m pip install -r requirements-dev.txt",
        "          python -m pytest --version",
        "          python -m pytest -q tests/evidence/test_hde_epic038_closeout.py",
        "      - run: python -m pip install -U pip",
    )
    check_prefix: tuple[str, ...] = ()
    if len(test_steps_starts) == 1 and len(step_starts) == 1:
        prefix_start = test_steps_starts[0] + 1
        check_prefix = raw_lines[
            prefix_start : prefix_start + len(expected_check_prefix)
        ]
    if (
        step_block != expected_step_block
        or check_prefix != expected_check_prefix
        or direct_workflow_lines != expected_direct_workflow_lines
        or direct_job_headers != expected_direct_job_headers
        or len(job_starts) != 1
        or direct_job_keys != expected_direct_job_keys
        or job_block.count("    runs-on: ubuntu-latest") != 1
        or len(test_steps_starts) != 1
        or len(test_env_starts) != 1
        or env_block != expected_env_block
        or not (job_start < step_starts[0] < job_end)
        or step_starts[0] <= test_steps_starts[0]
        or generator_invocations != expected_invocations
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
    }
    for key, expected in required.items():
        if payload.get(key) != expected:
            raise ValueError(f"release attestation mismatch: {key}")


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


def validate_rows(rows: Iterable[Row]) -> tuple[Row, ...]:
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
                if (ROOT / planned_path).exists():
                    raise ValueError(
                        f"planned path unexpectedly exists: {row.token}: {planned_path}"
                    )
            if key not in PLANNED_KEYS or key in current_keys:
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


def render(rows: Iterable[Row] | None = None) -> bytes:
    rows = validate_rows(build_rows() if rows is None else rows)
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


def main() -> int:
    parser = argparse.ArgumentParser(allow_abbrev=False)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--token-matrix", action="store_true")
    mode.add_argument("--check-token-matrix", action="store_true")
    mode.add_argument("--doc-deltas", action="store_true")
    mode.add_argument("--check-doc-deltas", action="store_true")
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
    expected = render()
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
