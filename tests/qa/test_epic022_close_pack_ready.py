from __future__ import annotations

import json
from pathlib import Path

QA_ROOT = Path("audit/qa/hde-epic022")
TOKEN_MATRIX = QA_ROOT / "token_evidence_matrix.md"
ACCEPTANCE_MAP = Path("docs/acceptance_map_epic022.json")
CLOSE_REPORT = Path("audit/EPIC-022_close_report.md")
MANIFEST = Path("audit/EPIC-022_MANIFEST.json")

REQUIRED_TOKENS = {
    # PF20 §2.7.5.A baseline tokens
    "PR_OPENED_OK",
    "TESTS_PASS_OK",
    "DOC_DELTA_PRESENT_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_INDEX_MIRROR_OK",
    "EVIDENCE_PATHS_VALIDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "QA_PRECOMMIT_CHECKLIST_OK",
    "QA_POSTCOMMIT_CHECKLIST_OK",
    "ENV_RAILS_POLICY_OK",
    "DETERMINISM_ENV_PINS_OK",
    "SANITY_PIPELINE_OK",
    "CLOSE_PACK_FILES_PRESENT_OK",
    # PF20 §2.7.5.B1 (D1)
    "ERROR_JSON_CANON_OK",
    "ERROR_TOKEN_MAP_OK",
    "CLI_READER_PARITY_OK",
    "TWO_RUN_IDENTITY_OK",
    # PF20 §2.7.5.B3 (D2)
    "CLI_STDOUT_LF_OK",
    # PF20 §2.7.5.B5 (D3)
    "INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK",
    "INTERNAL_VERSION_HEAD_PARITY_OK",
    "INTERNAL_VERSION_CONDITIONALS_IGNORED_OK",
    "INTERNAL_VERSION_NO_ETAG_OK",
    "INTERNAL_VERSION_NO_STORE_OK",
    "RELEASE_ID_RECOMPUTE_OK",
    "RELEASE_ID_FROM_MANIFEST_OK",
}

FORBIDDEN_TOKENS = {"CLI_STDERR_ONLY_ON_ERROR_OK"}

REQUIRED_BUNDLE_ARTIFACTS = {
    Path("artifacts/sanity/sanity.log"),
    Path("artifacts/ops/internal_version/two_run_identity.log"),
    Path("artifacts/cli/showcompat/stdout.json"),
}


def _parse_matrix_rows():
    lines = [
        line for line in TOKEN_MATRIX.read_text(encoding="utf-8").splitlines() if line.startswith("|")
    ]
    header = [col.strip() for col in lines[0].strip("|").split("|")]
    rows = []
    for raw in lines[2:]:
        cells = [cell.strip() for cell in raw.strip("|").split("|")]
        if len(cells) == len(header):
            rows.append(dict(zip(header, cells)))
    return rows


def _load_acceptance_tokens():
    payload = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    return payload.get("tokens", [])


def test_close_pack_files_exist():
    for path in (TOKEN_MATRIX, ACCEPTANCE_MAP, CLOSE_REPORT, MANIFEST):
        assert path.is_file(), f"Close-pack file missing: {path}"


def test_required_artifacts_exist():
    for artifact in REQUIRED_BUNDLE_ARTIFACTS:
        assert artifact.is_file(), f"Required artifact missing: {artifact}"


def test_token_roster_matches_required_set():
    rows = _parse_matrix_rows()
    matrix_tokens = [row["Token name"] for row in rows]
    assert len(matrix_tokens) == len(set(matrix_tokens)), "Matrix tokens must be unique"
    assert set(matrix_tokens) == REQUIRED_TOKENS, "Matrix tokens must match PF20 roster"

    acceptance_entries = _load_acceptance_tokens()
    acceptance_names = [entry.get("name") for entry in acceptance_entries]
    assert len(acceptance_names) == len(set(acceptance_names)), "Acceptance map tokens must be unique"
    assert set(acceptance_names) == REQUIRED_TOKENS, "Acceptance map tokens must match PF20 roster"


def test_forbidden_token_absent():
    matrix_text = TOKEN_MATRIX.read_text(encoding="utf-8")
    acceptance_text = ACCEPTANCE_MAP.read_text(encoding="utf-8")
    for forbidden in FORBIDDEN_TOKENS:
        assert forbidden not in matrix_text, f"Forbidden token present in matrix: {forbidden}"
        assert forbidden not in acceptance_text, f"Forbidden token present in acceptance map: {forbidden}"


def test_determinism_env_pins_binding():
    rows = _parse_matrix_rows()
    det_rows = [row for row in rows if row["Token name"] == "DETERMINISM_ENV_PINS_OK"]
    assert len(det_rows) == 1, "DETERMINISM_ENV_PINS_OK should appear exactly once in matrix"
    evidence_cells = {
        part.strip()
        for part in det_rows[0]["Evidence artifacts (titles / paths / artifact_keys)"].split(";")
        if part.strip()
    }
    expected = {
        "audit/gates/determinism/env_pins.log",
        "audit/gates/determinism/env_pins.log.path_proof.txt",
    }
    assert evidence_cells == expected, "Determinism pins evidence must use canonical log + path proof"

    acceptance_entries = _load_acceptance_tokens()
    matching = [entry for entry in acceptance_entries if entry.get("name") == "DETERMINISM_ENV_PINS_OK"]
    assert len(matching) == 1, "DETERMINISM_ENV_PINS_OK should appear once in acceptance map"
    acceptance_evidence = set(matching[0].get("evidence_titles", []))
    assert acceptance_evidence == expected, "Acceptance binding must use canonical determinism pins artifacts"
