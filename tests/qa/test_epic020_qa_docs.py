from __future__ import annotations

import json
from pathlib import Path

CHECKLIST = Path("docs/QA_CHECKLIST_EPIC020.md")
ACCEPTANCE_MAP = Path("docs/acceptance_map_epic020.json")
MANIFEST = Path("audit/EPIC020_MANIFEST.json")
MIRROR = Path("artifacts/evidence_index.jsonl")

QA_TOKENS = [
    "QA_PRECOMMIT_CHECKLIST_OK",
    "QA_POSTCOMMIT_CHECKLIST_OK",
    "QA_EVIDENCE_ONLY_OK",
    "QA_CI_DIFF_SCOPED_OK",
    "ENV_RAILS_POLICY_OK",
    "DETERMINISM_ENV_PINS_OK",
]

REQUIRED_HEADINGS = [
    "Pre-commit checklist",
    "Post-commit checklist",
    "Evidence-only pull requests",
    "Diff-scoped CI expectations",
    "Rails posture",
]

REQUIRED_CALLS = [
    "ci/checks/check_env_pins.sh",
    "python tools/evidence/update_evidence_index.py --check",
    "python tools/evidence/orientation_demo.py --check",
]

REQUIRED_TEST_REFERENCES = [
    "tests/adapter/test_jsonschema.py",
    "tests/cli/test_cli_usage_and_errors.py",
    "tests/cli/test_errors_parity.py",
    "tests/cli/test_cli_canonical_bytes.py",
    "tests/cli/test_showcompat_parity_and_identity.py",
    "tests/cli/test_serializer_guards.py",
    "tests/transport/test_internal_version_contract.py",
]

ENV_ARTIFACT = "audit/gates/determinism/env_pins.log"


def test_checklist_covers_required_sections() -> None:
    text = CHECKLIST.read_text(encoding="utf-8")
    for heading in REQUIRED_HEADINGS:
        assert heading in text, heading
    for call in REQUIRED_CALLS:
        assert call in text, call
    for reference in REQUIRED_TEST_REFERENCES:
        assert reference in text, reference


def test_acceptance_metadata_captures_qa_tokens() -> None:
    acceptance = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

    token_status = acceptance["token_status"]
    manifest_tokens = manifest["tokens"]
    manifest_artifacts = manifest["token_artifacts"]

    for token in QA_TOKENS:
        assert token_status[token]["status"] == "DONE"
        assert token_status[token]["tests"], token
        assert manifest_tokens[token], token
        assert manifest_artifacts[token], token



def test_env_pin_artifact_is_indexed() -> None:
    lines = MIRROR.read_text(encoding="utf-8").splitlines()
    entries = [json.loads(line) for line in lines if line.strip()]
    assert any(entry.get("discovered_physical_path") == ENV_ARTIFACT for entry in entries)

    acceptance = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    for token in ("ENV_RAILS_POLICY_OK", "DETERMINISM_ENV_PINS_OK"):
        assert ENV_ARTIFACT in acceptance["token_status"][token]["artifacts"]
