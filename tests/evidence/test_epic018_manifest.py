from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "audit/EPIC-018_MANIFEST.json"
INDEX_PATH = ROOT / "docs/evidence/INDEX.json"


EXPECTED_TOKENS = {
    "CLI_SERIALIZER_GUARD_OK",
    "COMPOSITE_ABBA_IDENTITY_OK",
    "CONFIG_BUNDLES_DETERMINISTIC_OK",
    "CONFIG_MAGIC10_OK",
    "CONFIG_REGISTRY_OK",
    "DETERMINISM_ENV_PINS_OK",
    "DOC_DELTA_PRESENT_OK",
    "EMITTER_SYMBOL_PROOF_OK",
    "ENV_RAILS_POLICY_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "JSON_CANONICAL_CHECK_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "PR_OPENED_OK",
    "QA_POSTCOMMIT_CHECKLIST_OK",
    "QA_PRECOMMIT_CHECKLIST_OK",
    "READER_CLI_PARITY_OK",
    "SANITY_PIPELINE_OK",
    "SERIALIZER_GREP_GUARD_OK",
    "TESTS_PASS_OK",
    "TWO_RUN_IDENTITY_OK",
}

NEW_CANON_TOKENS = {
    "CONFIG_BUNDLES_DETERMINISTIC_OK",
    "EMITTER_SYMBOL_PROOF_OK",
    "SERIALIZER_GREP_GUARD_OK",
}


def _load_manifest() -> dict:
    raw = MANIFEST_PATH.read_text(encoding="utf-8")
    parsed = json.loads(raw)
    assert raw == json.dumps(parsed, sort_keys=True, separators=(",", ":")) + "\n"
    return parsed


def _artifact_keys() -> set[str]:
    entries = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    return {entry["artifact_key"] for entry in entries}


def _assert_test_node_exists(test_name: str) -> None:
    file_name, _, node = test_name.partition("::")
    path = ROOT / file_name
    assert path.exists(), f"missing test file: {file_name}"
    if node:
        content = path.read_text(encoding="utf-8")
        assert node in content, f"missing test node: {test_name}"


def test_manifest_schema_and_roster():
    manifest = _load_manifest()
    assert manifest.get("epic_id") == "HDE-EPIC018"
    assert manifest.get("schema") == "epic_manifest.v1"
    tokens = manifest.get("tokens")
    assert isinstance(tokens, list) and tokens
    seen = {entry["token_name"] for entry in tokens}
    assert seen == EXPECTED_TOKENS


def test_token_records_reference_known_artifacts_and_tests():
    manifest = _load_manifest()
    index_keys = _artifact_keys()
    for record in manifest["tokens"]:
        assert record["token_name"] in EXPECTED_TOKENS
        assert record.get("status") == "expected_green"
        for artifact_key in record.get("evidence_artifacts", []):
            assert artifact_key in index_keys, f"missing artifact_key {artifact_key}"
        for test_name in record.get("tests", []):
            _assert_test_node_exists(test_name)
        if record["token_name"] in NEW_CANON_TOKENS:
            assert "NEW CANON" in record.get("notes", "")

