#!/usr/bin/env python3
"""Generate the deterministic, nonclaiming HDE-EPIC038 DEV-01 token matrix."""
from __future__ import annotations

import argparse
import difflib
import json
from dataclasses import dataclass, replace
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path("audit/qa/hde-epic038/token_evidence_matrix.md")
EPIC_ID = "HDE-EPIC038"
CI_JOB = "test (.github/workflows/ci.yml)"
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
PLANNED_PATHS = frozenset({
    "audit/EPIC-038_close_report.md", "audit/EPIC-038_close_report.md.path_proof.txt",
    "audit/EPIC-038_MANIFEST.json", "audit/EPIC-038_MANIFEST.json.path_proof.txt",
    "docs/acceptance_map_epic038.json", "docs/acceptance_map_epic038.json.path_proof.txt",
    "audit/qa/hde-epic038/acceptance_map_viability.log",
    "audit/qa/hde-epic038/acceptance_map_viability.log.path_proof.txt",
    "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
    "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md.path_proof.txt",
})

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
    future_claim: str


def _row(token: str, test: str, qa: str, path: str, key: str) -> Row:
    return Row(token, token, token, test, CI_JOB, qa, (path,), (key,), EPIC_ID,
               (path + ".path_proof.txt",),
               "UNCLAIMED: retained evidence is a binding candidate only; presence or historical PASS text is not acceptance.",
               "existing/reused",
               "Future status may become CLAIMED only after exact-head closed-rails execution, finalized acceptance-map and manifest derivation, and independent Gate B PASS.")


def build_rows() -> tuple[Row, ...]:
    default = ("tests/evidence/test_hde_epic038_release_sanity.py", "qa-20-po-020",
               "audit/qa/hde-epic038/qa_step_logs_manifest.json", "epic038.qa_step_logs_manifest")
    rows = {t: _row(t, *default) for t in TOKENS}
    def bind(tokens: Iterable[str], test: str, qa: str, path: str, key: str) -> None:
        for token in tokens: rows[token] = _row(token, test, qa, path, key)
    bind(("ENV_RAILS_POLICY_OK", "ENV_LC_ALL_C_OK"), "tests/invariance/test_determinism_env_helper.py", "qa-03-po-003", "artifacts/runtime/env_matrix.snapshot.json", "epic038.pr01.env_matrix_snapshot_v3")
    bind(("PREIMAGE_RECOMPUTE_OK",), "tests/evidence/test_identity_provenance.py", "qa-02-po-002", "artifacts/identity/release_id_recompute.log", "epic038.pr01.identity_release_id_recompute")
    bind(("CLI_READER_PARITY_OK",), "tests/adapter/test_compat_http_parity.py", "qa-06-po-006", "audit/gates/parity/reader_cli/summary.json", "epic038.pr02.reader_cli_summary")
    bind(("COMPOSITE_ABBA_IDENTITY_OK",), "tests/cli/test_showcompat_parity_and_identity.py", "qa-04-po-004", "audit/gates/determinism/abba.bytes", "epic038.pr02.abba_bytes")
    bind(("TWO_RUN_IDENTITY_OK",), "tests/cli/test_showcompat_parity_and_identity.py", "qa-04-po-004", "audit/gates/determinism/tworun_identity.sha256", "epic038.pr02.tworun_identity")
    bind(("JSON_CANONICAL_CHECK_OK",), "tests/cli/test_cli_canonical_bytes.py", "qa-04-po-004", "audit/gates/json_gate/canonical/json_gate_structured_record.json", "audit.gates.json_gate.canonical.json_gate_structured_record.json")
    a7 = ("A7_GET_QUOTED_ETAG_OK", "A7_HEAD_PARITY_OK", "A7_304_OMITS_CT_CL_OK", "A7_VARY_AUTH_AE_OK", "A7_ENCODING_INVARIANCE_OK", "A7_TRANSPORT_PROOF_OK")
    bind(a7, "tests/http/test_reader_a7_transport.py", "qa-05-po-005", "artifacts/proofs/reader_success_get_head_304.json", "epic038.pr02.a7_reader_success_composite")
    bind(("ENDPOINTS_CATALOG_OK",), "tests/http/test_endpoint_catalog.py", "qa-05-po-005", "docs/ENDPOINTS_CATALOG.json", "epic038.pr02.endpoint_catalog")
    bind(("ENDPOINTS_CATALOG_ENV_GATE_OK",), "tests/http/test_endpoint_catalog.py", "qa-05-po-005", "artifacts/proofs/endpoints_env_gate_proof.log", "epic038.pr02.a7_env_gate")
    bind(("EVIDENCE_INDEX_UPDATED_OK", "EVIDENCE_INDEX_MIRROR_OK", "EVIDENCE_PATHS_VALIDATED_OK", "EVIDENCE_PATH_PROOFS_OK"), "tests/ops/test_evidence_index.py", "qa-19-po-019", "docs/evidence/INDEX.json", "index.human_index")
    bind(("MACHINE_MIRROR_UPDATED_OK", "CI_CHECK_MIRROR_SCHEMA_OK"), "tests/ops/test_evidence_index.py", "qa-19-po-019", "artifacts/evidence_index.jsonl", "index.machine_mirror")
    bind(("EVIDENCE_INDEX_HASH_OK",), "tests/ops/test_evidence_index.py", "qa-19-po-019", "docs/evidence/INDEX.sha256", "docs.evidence.INDEX.sha256")
    bind(("CI_CHECK_FINAL_LF_OK",), "tests/ops/test_evidence_index.py", "qa-19-po-019", "audit/gates/topology/orientation_demo.txt", "topology.orientation_demo")
    bind(("DB_RUNTIME_SEARCH_PATH_OK", "DB_ROLE_OK", "DB_SCHEMA_FINGERPRINT_OK", "DB_CONN_ENV_OK"), "tests/db/test_direct_db_pr06r.py", "qa-12-po-012", "artifacts/runtime/direct_db_selection.snapshot.json", "epic038.pr06r.direct_db_selection")
    bind(("NO_EXTERNAL_IO_ON_REFUSAL_OK",), "tests/bodygraph/test_vendor_client.py", "qa-10-po-010", "artifacts/vendor/rails_gate_keys_only.logs.sample", "rails_gate.keys_only_logs")
    release = _row("RELEASE_ID_RECOMPUTE_OK", "tests/evidence/test_identity_provenance.py", "qa-02-po-002; qa-21-po-021", "artifacts/identity/release_id.json", "epic038.pr01.identity_release_id")
    release = replace(release,
        test_binding="scripts/release_id_recompute.py; tools/evidence/generate_identity_provenance.py; tests/evidence/test_identity_provenance.py",
        primary_evidence=("catalog/manifest.json", "artifacts/identity/release_id.json", "artifacts/identity/release_id_recompute.log"),
        artifact_keys=("epic038.pr01.identity_release_id", "epic038.pr01.identity_release_id_recompute"),
        proof_anchors=("artifacts/identity/release_id.json.path_proof.txt", "artifacts/identity/release_id_recompute.log.path_proof.txt"),
        posture="UNCLAIMED: PF10-HDE-Build-Notes, §2.37 makes this canonical; current identity artifacts and historical PASS text do not satisfy the token.")
    rows[release.token] = release
    future_paths = {
        "TESTS_PASS_OK": "audit/EPIC-038_close_report.md",
        "DOC_DELTA_PRESENT_OK": "audit/qa/hde-epic038/00_meta/closeout_remediation_ledger.md",
        "QA_PRECOMMIT_CHECKLIST_OK": "audit/qa/hde-epic038/acceptance_map_viability.log",
        "QA_POSTCOMMIT_CHECKLIST_OK": "audit/EPIC-038_MANIFEST.json",
    }
    for token, path in future_paths.items():
        r = rows[token]
        rows[token] = replace(
            r,
            ci_binding=f"{CI_JOB}; planned commands: {PLANNED_COMMANDS}",
            future_claim=(
                f"Future status may become CLAIMED only after planned-new `{path}` and "
                f"`{path}.path_proof.txt` are canonically produced and updater-registered, "
                "the exact authorized commands execute on the exact head, and independent Gate B records PASS."
            ),
        )
    return tuple(rows[t] for t in TOKENS)


def _index_records() -> set[tuple[str, str]]:
    records = set()
    for line in (ROOT / "artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines():
        item = json.loads(line); records.add((item["artifact_key"], item["discovered_physical_path"]))
    return records


def validate_rows(rows: Iterable[Row]) -> tuple[Row, ...]:
    rows = tuple(rows); names = [r.token for r in rows]
    if len(names) != len(set(names)): raise ValueError("duplicate token")
    if set(names) != set(TOKENS): raise ValueError(f"token set mismatch: missing={sorted(set(TOKENS)-set(names))}; unexpected={sorted(set(names)-set(TOKENS))}")
    if any(name in PROHIBITED for name in names): raise ValueError("prohibited token or non-token label")
    records = _index_records()
    qa_manifest = json.loads(
        (ROOT / "audit/qa/hde-epic038/qa_step_logs_manifest.json").read_text(
            encoding="utf-8"
        )
    )
    for row in rows:
        values = tuple(str(v) for v in row.__dict__.values())
        if any(not v for v in values): raise ValueError(f"empty field: {row.token}")
        joined = " ".join(values)
        if "*" in joined: raise ValueError(f"missing existing path or wildcard-only binding: {row.token}")
        if any(marker in joined for marker in ("TBD", "e.g.", "??")): raise ValueError(f"placeholder: {row.token}")
        if row.acceptance_token != row.token or row.manifest_token != row.token: raise ValueError(f"token alias: {row.token}")
        if row.epic_id != EPIC_ID or row.classification not in {"existing/reused", "planned-new"}: raise ValueError(f"invalid binding: {row.token}")
        if "PASS conclusion" in joined or "status=PASS" in joined: raise ValueError(f"acceptance inference: {row.token}")
        for test_path in row.test_binding.split("; "):
            if not (ROOT / test_path).is_file():
                raise ValueError(f"missing existing test path: {row.token}: {test_path}")
        for check_id in row.live_qa.split("; "):
            if check_id not in qa_manifest:
                raise ValueError(f"unregistered Live QA check ID: {row.token}: {check_id}")
        if row.classification == "existing/reused":
            for path in (*row.primary_evidence, *row.proof_anchors):
                if "*" in path or not (ROOT / path).is_file(): raise ValueError(f"missing existing path: {row.token}: {path}")
            for key, path in zip(row.artifact_keys, row.primary_evidence[-len(row.artifact_keys):]):
                if (key, path) not in records: raise ValueError(f"unregistered artifact key: {row.token}: {key} -> {path}")
        else:
            for path in (*row.primary_evidence, *row.proof_anchors):
                if path not in PLANNED_PATHS: raise ValueError(f"unauthorized planned path: {row.token}: {path}")
                if (ROOT / path).exists(): raise ValueError(f"planned path unexpectedly exists: {row.token}: {path}")
            if PLANNED_COMMANDS not in row.ci_binding: raise ValueError(f"inexact planned command: {row.token}")
    return rows


def render(rows: Iterable[Row] | None = None) -> bytes:
    rows = validate_rows(build_rows() if rows is None else rows)
    lines = ["# HDE-EPIC038 DEV-01 Token Evidence Matrix", "",
      "> Nonclaim: all 33 tokens are UNCLAIMED. Matrix construction, artifact presence, historical PASS text, validation, PR creation, and Gate B review do not satisfy an acceptance token.", "",
      "Each numbered row is canonical; semicolon-separated values are exact bindings.", ""]
    for i, r in enumerate(rows, 1):
        lines += [f"## {i}. `{r.token}`", f"- Canonical governance token: `{r.token}`", f"- Acceptance-map token: `{r.acceptance_token}`", f"- Manifest token: `{r.manifest_token}`", f"- Test/stable identifier: `{r.test_binding}`", f"- Closed-rails CI binding: `{r.ci_binding}`", f"- Live QA: `{r.live_qa}`", f"- Primary governed evidence: `{'; '.join(r.primary_evidence)}`", f"- Human Index / Machine Mirror artifact keys: `{'; '.join(r.artifact_keys)}`", f"- Epic: `epic_id={r.epic_id}`", f"- Proof anchors: `{'; '.join(r.proof_anchors)}`", f"- Current posture: {r.posture}", f"- Classification: `{r.classification}`", f"- Intended future claim and prerequisite: {r.future_claim}", ""]
    return ("\n".join(lines).rstrip("\n") + "\n").encode("utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(); mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--token-matrix", action="store_true"); mode.add_argument("--check-token-matrix", action="store_true")
    args = parser.parse_args(); expected = render(); target = ROOT / OUTPUT
    if args.token_matrix:
        target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(expected); print(f"WROTE {OUTPUT}"); return 0
    actual = target.read_bytes() if target.is_file() else b""
    if actual != expected:
        diff = difflib.unified_diff(actual.decode("utf-8", "replace").splitlines(), expected.decode().splitlines(), fromfile=str(OUTPUT), tofile="expected", lineterm="")
        print("TOKEN_MATRIX_DRIFT\n" + "\n".join(diff)); return 1
    print("TOKEN_MATRIX_OK rows=33 unique=33 claimed=0"); return 0

if __name__ == "__main__": raise SystemExit(main())
