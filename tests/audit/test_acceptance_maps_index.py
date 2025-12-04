import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = ROOT / "docs/acceptance_maps.json"

EXPECTED = {
    "HDE-EPIC017": "docs/acceptance_map_epic017.json",
    "HDE-EPIC019": "docs/acceptance_map_epic019.json",
    "HDE-EPIC020": "docs/acceptance_map_epic020.json",
}


def test_acceptance_maps_index():
    records = json.loads(INDEX_PATH.read_text())
    index = {item["epic_id"]: item["path"] for item in records}
    assert index == EXPECTED

    for epic_id, rel_path in index.items():
        path = ROOT / rel_path
        assert path.exists()
        data = json.loads(path.read_text())
        assert data["epic_id"] == epic_id
