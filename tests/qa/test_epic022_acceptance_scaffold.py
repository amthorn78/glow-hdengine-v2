import json
from pathlib import Path

QA_ROOT = Path("audit/qa/hde-epic022")
TOKEN_MATRIX = QA_ROOT / "token_evidence_matrix.md"
ACCEPTANCE_MAP = Path("docs/acceptance_map_epic022.json")
CLOSE_REPORT = Path("audit/EPIC-022_close_report.md")
MANIFEST = Path("audit/EPIC-022_MANIFEST.json")


def test_epic022_scaffold_files_exist():
    assert TOKEN_MATRIX.is_file(), "token_evidence_matrix.md should exist for EPIC022"
    assert ACCEPTANCE_MAP.is_file(), "EPIC022 acceptance map should exist in docs"
    assert CLOSE_REPORT.is_file(), "EPIC022 close report stub should exist"
    assert MANIFEST.is_file(), "EPIC022 manifest should exist"


def test_token_matrix_contains_epic_and_token():
    content = TOKEN_MATRIX.read_text(encoding="utf-8")
    assert "hde-epic022" in content.lower(), "Matrix should include the epic identifier"
    assert "PR_OPENED_OK" in content, "Matrix should seed baseline tokens"


def test_acceptance_map_structure_matches_template():
    template = json.loads(Path("docs/acceptance_map_epic021.json").read_text(encoding="utf-8"))
    data = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    assert set(data.keys()) == set(template.keys()), "Acceptance map keys should mirror the template"
    assert data.get("epic_id") == "HDE-EPIC022", "Acceptance map epic_id should target EPIC022"
    assert isinstance(data.get("tokens"), list), "Acceptance map tokens should be a list"


def test_close_report_mentions_matrix():
    content = CLOSE_REPORT.read_text(encoding="utf-8")
    assert "EPIC-022" in content, "Close report should identify EPIC-022"
    assert "audit/qa/hde-epic022/token_evidence_matrix.md" in content, "Close report should point to the token matrix"


def test_manifest_structure_matches_template():
    template = json.loads(Path("audit/EPIC-018_MANIFEST.json").read_text(encoding="utf-8"))
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert set(data.keys()) == set(template.keys()), "Manifest keys should mirror the template"
    assert data.get("epic_id") == "HDE-EPIC022", "Manifest epic_id should target EPIC022"
    assert isinstance(data.get("tokens"), list), "Manifest tokens should be a list"
