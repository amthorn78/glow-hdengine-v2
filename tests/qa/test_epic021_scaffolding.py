import json
from pathlib import Path

QA_ROOT = Path("audit/qa/hde-epic021")
TOKEN_MATRIX = QA_ROOT / "token_evidence_matrix.md"
ACCEPTANCE_MAP = Path("docs/acceptance_map_epic021.json")


def test_epic021_qa_root_exists():
    assert QA_ROOT.is_dir(), "EPIC021 QA_ROOT should exist for calcination scaffolding"


def test_token_matrix_present_and_non_empty():
    assert TOKEN_MATRIX.is_file(), "token_evidence_matrix.md should be seeded for EPIC021"
    content = TOKEN_MATRIX.read_text(encoding="utf-8").strip()
    assert content, "token_evidence_matrix.md should not be empty"


def test_acceptance_map_structure():
    assert ACCEPTANCE_MAP.is_file(), "EPIC021 acceptance map should be present in docs"
    data = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    assert data.get("epic_id") == "HDE-EPIC021", "Acceptance map epic_id should target EPIC021"
    tokens = data.get("tokens")
    assert isinstance(tokens, list) and tokens, "Acceptance map should declare at least one token entry"
