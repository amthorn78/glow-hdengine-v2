import json
from pathlib import Path

from engine.mech.helpers import canonicalize_array

ROOT = Path(__file__).resolve().parents[2]
CHANNELS_PATH = ROOT / "catalog" / "channels_v1.json"
REPORT_PATH = ROOT / "artifacts" / "canonical" / "arrays_as_sets_report.log"


def _load_channels() -> list[dict[str, object]]:
    raw = json.loads(CHANNELS_PATH.read_text(encoding="utf-8"))
    channels = raw.get("channels")
    if not isinstance(channels, list):
        raise AssertionError("channels_v1.json missing channels list")
    return channels


def _select_case(channels: list[dict[str, object]], field: str) -> dict[str, object]:
    for entry in channels:
        values = entry.get(field)
        if not isinstance(values, list) or not values:
            continue
        raw = [str(value) for value in values]
        normalized = canonicalize_array(raw)
        if normalized != raw:
            channel_id = entry.get("id")
            if isinstance(channel_id, str):
                return {
                    "channel_id": channel_id,
                    "field": field,
                    "raw": raw,
                    "normalized": normalized,
                }
    raise AssertionError(f"no unsorted {field} array found in channels_v1.json")


def test_arrays_as_sets_registry_report():
    channels = _load_channels()
    centers_case = _select_case(channels, "centers")
    domains_case = _select_case(channels, "domains")

    assert centers_case["normalized"] == sorted(set(centers_case["raw"]))
    assert domains_case["normalized"] == sorted(set(domains_case["raw"]))

    assert REPORT_PATH.exists()
    report_text = REPORT_PATH.read_text(encoding="utf-8")

    centers_path = (
        f"catalog/channels_v1.json:channels[id={centers_case['channel_id']}].centers"
    )
    domains_path = (
        f"catalog/channels_v1.json:channels[id={domains_case['channel_id']}].domains"
    )

    assert centers_path in report_text
    assert domains_path in report_text
    assert "arrays-as-sets report v1" in report_text
