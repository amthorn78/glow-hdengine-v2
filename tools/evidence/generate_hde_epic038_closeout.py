#!/usr/bin/env python3
"""Generate the deterministic, nonclaiming HDE-EPIC038 DEV-01 token matrix."""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path("audit/qa/hde-epic038/token_evidence_matrix.md")
EPIC_ID = "HDE-EPIC038"
CI_JOB = "test (.github/workflows/ci.yml)"
RELEASE_CI_JOB = (
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
PLANNED_BINDINGS: Mapping[str, tuple[str, str, str]] = {
    "TESTS_PASS_OK": (
        "audit/EPIC-038_close_report.md",
        "epic038.close_report",
        "DEV-03",
    ),
    "DOC_DELTA_PRESENT_OK": (
        "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
        "epic038.closeout_remediation_ledger",
        "DEV-02",
    ),
    "QA_PRECOMMIT_CHECKLIST_OK": (
        "audit/qa/hde-epic038/acceptance_map_viability.log",
        "epic038.acceptance_map_viability",
        "DEV-03",
    ),
    "QA_POSTCOMMIT_CHECKLIST_OK": (
        "audit/EPIC-038_MANIFEST.json",
        "epic038.manifest",
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
QA_MANIFEST_PATH = "audit/qa/hde-epic038/qa_step_logs_manifest.json"
QA_MANIFEST_KEY = "epic038.qa_step_logs_manifest"
FINAL_LF_CHECK_ID = "qa-19-po-019"
FINAL_LF_LOG_PATH = (
    "audit/qa/hde-epic038/checks/qa-19-po-019/primary.log"
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


def _release_row() -> Row:
    manifest_sha256 = hashlib.sha256(
        (ROOT / RELEASE_MANIFEST_PATH).read_bytes()
    ).hexdigest()
    row = _row(
        "RELEASE_ID_RECOMPUTE_OK",
        (
            "scripts/release_id_recompute.py; "
            "tools/evidence/build_release_attestation.py; "
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
        posture=(
            "UNCLAIMED: the canonical manifest is the exact current source input; "
            "frozen capture-time identity artifacts and historical PASS text are "
            "not current release evidence."
        ),
        future_claim=(
            "Future status may become CLAIMED only when the workflow artifact "
            "`hde-release-attestation-${{ github.event.pull_request.head.sha || "
            "github.sha }}/attestation.json` verifies `source_commit_exact=true`, "
            f"`manifest_sha256={manifest_sha256}`, `release_id=manifest_sha256`, "
            "`validation_result=PASS`, `release_admission=PR06R_B_FINAL_PASS`, "
            "`pipeline_stop=null`, closed rails, and independent Gate B PASS "
            "against that same exact head."
        ),
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
    bind(
        ("PREIMAGE_RECOMPUTE_OK",),
        "tests/evidence/test_identity_provenance.py",
        "qa-02-po-002",
        "artifacts/identity/release_id_recompute.log",
        "epic038.pr01.identity_release_id_recompute",
    )
    bind(
        ("CLI_READER_PARITY_OK",),
        "tests/adapter/test_compat_http_parity.py",
        "qa-06-po-006",
        "audit/gates/parity/reader_cli/summary.json",
        "epic038.pr02.reader_cli_summary",
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
        (
            "EVIDENCE_INDEX_UPDATED_OK",
            "EVIDENCE_INDEX_MIRROR_OK",
            "EVIDENCE_PATHS_VALIDATED_OK",
            "EVIDENCE_PATH_PROOFS_OK",
        ),
        "tests/ops/test_evidence_index.py",
        "qa-19-po-019",
        "docs/evidence/INDEX.json",
        "index.human_index",
    )
    bind(
        ("MACHINE_MIRROR_UPDATED_OK", "CI_CHECK_MIRROR_SCHEMA_OK"),
        "tests/ops/test_evidence_index.py",
        "qa-19-po-019",
        "artifacts/evidence_index.jsonl",
        "index.machine_mirror",
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
            "`Run ci/checks/check_final_lf.sh` workflow step succeeds, the "
            "QA-19 manifest and hash-bound execution log remain coherent, and "
            "independent Gate B records PASS against that same exact head."
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

    for token, (path, key, owner) in PLANNED_BINDINGS.items():
        row = rows[token]
        rows[token] = replace(
            row,
            test_binding="tests/evidence/test_hde_epic038_closeout.py",
            ci_binding=f"{CI_JOB}; planned commands: {PLANNED_COMMANDS}",
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
    return tuple(rows[token] for token in TOKENS)


def _mirror_records() -> set[tuple[str, str, str]]:
    records = set()
    for line in (
        ROOT / "artifacts/evidence_index.jsonl"
    ).read_text(encoding="utf-8").splitlines():
        item = json.loads(line)
        records.add(
            (
                item["artifact_key"],
                item["discovered_physical_path"],
                item["proof_anchor"],
            )
        )
    return records


def _proof_fields(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if ": " in line:
            key, value = line.split(": ", 1)
            fields[key] = value
    return fields


def _validate_proof(primary: str, proof: str) -> None:
    primary_path = ROOT / primary
    fields = _proof_fields(ROOT / proof)
    body = primary_path.read_bytes()
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
    required_log_fields = (
        "code=PROVIDER_REFUSED",
        "safe_mode=1",
        "allow_network=0",
        "vendor_calls=0",
        "db_calls=0",
    )
    if not all(field in log_text.split() for field in required_log_fields):
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
    log_path = ROOT / REFUSAL_PATH
    matches = [
        item
        for item in artifacts
        if isinstance(item, dict) and item.get("path") == REFUSAL_PATH
    ]
    if len(matches) != 1:
        raise ValueError("closed-rails refusal binding missing")
    match = matches[0]
    log_bytes = log_path.read_bytes()
    if (
        match.get("sha256") != hashlib.sha256(log_bytes).hexdigest()
        or match.get("size") != len(log_bytes)
    ):
        raise ValueError("closed-rails refusal binding mismatch")


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


def validate_final_lf_evidence(
    manifest: Mapping[str, object], log_text: str
) -> None:
    record = manifest.get(FINAL_LF_CHECK_ID)
    if not isinstance(record, dict):
        raise ValueError("final-LF QA manifest record missing")
    expected_relative_log = "checks/qa-19-po-019/primary.log"
    log_bytes = log_text.encode("utf-8")
    if (
        record.get("log_path") != expected_relative_log
        or record.get("status") != "PASS"
        or record.get("sha256") != hashlib.sha256(log_bytes).hexdigest()
        or record.get("size_bytes") != len(log_bytes)
    ):
        raise ValueError("final-LF QA manifest binding mismatch")
    lines = log_text.splitlines()
    if not lines:
        raise ValueError("final-LF execution log missing")
    try:
        header = json.loads(lines[0])
    except json.JSONDecodeError as exc:
        raise ValueError("final-LF execution header invalid") from exc
    required_rails = {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }
    if (
        not isinstance(header, dict)
        or header.get("check_id") != FINAL_LF_CHECK_ID
        or header.get("status") != "PASS"
        or header.get("exit_code") != 0
        or "bash ci/checks/check_final_lf.sh" not in header.get("command", "")
        or header.get("captured_env") != required_rails
        or header.get("intended_tokens") != []
        or header.get("claimed_tokens") != []
        or "BEHAVIOR_EXIT_CODE=0" not in lines
    ):
        raise ValueError("final-LF execution predicate mismatch")


def _validate_special_semantics(row: Row) -> None:
    if row.token in {
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
    elif row.token == "RELEASE_ID_RECOMPUTE_OK":
        if (
            row.primary_evidence != (RELEASE_MANIFEST_PATH,)
            or row.artifact_keys != (RELEASE_MANIFEST_KEY,)
            or any(path.startswith("artifacts/identity/") for path in row.primary_evidence)
        ):
            raise ValueError("release identity source binding mismatch")
        raw = (ROOT / RELEASE_MANIFEST_PATH).read_bytes()
        payload = json.loads(raw)
        canonical = (
            json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
            + "\n"
        ).encode("utf-8")
        if raw != canonical:
            raise ValueError("release manifest is not canonical")
        digest = hashlib.sha256(raw).hexdigest()
        if f"`manifest_sha256={digest}`" not in row.future_claim:
            raise ValueError("release manifest digest binding mismatch")
        required_bindings = {
            "scripts/release_id_recompute.py",
            "tools/evidence/build_release_attestation.py",
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
            if PLANNED_COMMANDS not in row.ci_binding:
                raise ValueError(f"inexact planned command: {row.token}")
            if "UNCLAIMED" not in row.posture or "has not been executed" not in row.posture:
                raise ValueError(f"planned evidence claim: {row.token}")

        _validate_special_semantics(row)
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
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--token-matrix", action="store_true")
    mode.add_argument("--check-token-matrix", action="store_true")
    args = parser.parse_args()
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
