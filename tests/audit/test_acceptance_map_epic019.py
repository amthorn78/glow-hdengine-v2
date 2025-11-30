import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP_PATH = ROOT / "docs/acceptance_map_epic019.json"

EXPECTED_FOUNDATIONS = {
    "D1": {
        "status": "done",
        "tokens": {
            "PR_OPENED_OK",
            "TESTS_PASS_OK",
            "DETERMINISM_ENV_PINS_OK",
            "TWO_RUN_IDENTITY_OK",
            "COMPOSITE_ABBA_IDENTITY_OK",
            "AB_BA_PARITY_OK",
            "NO_IO_NO_CLOCKS_OK",
            "JSON_CANONICAL_CHECK_OK",
        },
    },
    "D2": {
        "status": "done",
        "tokens": {
            "DOC_DELTA_PRESENT_OK",
            "ENV_RAILS_POLICY_OK",
            "QA_PRECOMMIT_CHECKLIST_OK",
            "DETERMINISM_ENV_PINS_OK",
        },
    },
    "D3": {
        "status": "done",
        "tokens": {
            "QA_POSTCOMMIT_CHECKLIST_OK",
            "SANITY_PIPELINE_OK",
            "DETERMINISM_ENV_PINS_OK",
        },
    },
    "D4": {
        "status": "done",
        "tokens": {
            "EVIDENCE_INDEX_UPDATED_OK",
            "EVIDENCE_INDEX_HASH_OK",
            "EVIDENCE_INDEX_MIRROR_OK",
            "EVIDENCE_PATHS_VALIDATED_OK",
            "MACHINE_MIRROR_UPDATED_OK",
        },
    },
    "D5": {
        "status": "done",
        "tokens": {
            "SANITY_PIPELINE_OK",
            "DETERMINISM_ENV_PINS_OK",
            "AB_BA_PARITY_OK",
            "JSON_CANONICAL_CHECK_OK",
            "NO_IO_NO_CLOCKS_OK",
        },
    },
}

EXPECTED_TOKENS = {
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
    "TWO_RUN_IDENTITY_OK",
    "COMPOSITE_ABBA_IDENTITY_OK",
    "AB_BA_PARITY_OK",
    "NO_IO_NO_CLOCKS_OK",
    "JSON_CANONICAL_CHECK_OK",
}


def test_acceptance_map_shape():
    data = json.loads(MAP_PATH.read_text())
    assert data["epic_id"] == "HDE-EPIC019"
    assert data["manifest"] == "audit/EPIC019_MANIFEST.json"
    assert data.get("epic_name")
    assert data.get("pf20_ref")

    foundations = {item["deliverable"]: item for item in data["foundations"]}
    assert set(foundations) == set(EXPECTED_FOUNDATIONS)
    for key, meta in EXPECTED_FOUNDATIONS.items():
        foundation = foundations[key]
        assert foundation["status"] == meta["status"]
        assert set(foundation["tokens"]) == meta["tokens"]
        assert set(foundation["manifest_tokens"])

    token_status = data["token_status"]
    assert set(token_status) == EXPECTED_TOKENS
    for name, payload in token_status.items():
        assert payload["status"] == "GREEN"
        assert payload["tests"], name
        assert payload["artifacts"], name

    referenced_tokens = {token for foundation in data["foundations"] for token in foundation["tokens"]}
    assert referenced_tokens <= set(token_status)
