import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MAP_PATH = ROOT / "docs/acceptance_map_epic017.json"

EXPECTED_FOUNDATIONS = {
    "D1": {"status": "done"},
    "D2": {"status": "done"},
    "D3": {"status": "done"},
    "D4": {"status": "done"},
}


def test_acceptance_map_shape():
    data = json.loads(MAP_PATH.read_text())
    assert data["epic_id"] == "HDE-EPIC017"
    assert data["manifest"] == "audit/EPIC017_MANIFEST.json"
    foundations = {item["deliverable"]: item for item in data["foundations"]}
    assert set(foundations) == set(EXPECTED_FOUNDATIONS)
    for key, meta in EXPECTED_FOUNDATIONS.items():
        foundation = foundations[key]
        assert foundation["status"] == meta["status"]
        assert foundation.get("tokens")
        assert foundation.get("manifest_tokens")
