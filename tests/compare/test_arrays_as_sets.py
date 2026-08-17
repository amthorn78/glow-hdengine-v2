import json
from pathlib import Path

from engine.mech.helpers import canonicalize_array
from tools.evidence.generate_arrays_as_sets_report import build_report, write_report

ROOT = Path(__file__).resolve().parents[2]
CHANNELS_PATH = ROOT / "catalog" / "channels_v1.json"
REPORT_PATH = ROOT / "artifacts" / "canonical" / "arrays_as_sets_report.log"


def _load_channels() -> list[dict[str, object]]:
    raw = json.loads(CHANNELS_PATH.read_text(encoding="utf-8"))
    channels = raw.get("channels")
    if not isinstance(channels, list):
        raise AssertionError("channels_v1.json missing channels list")
    return channels


def _select_case(
    channels: list[dict[str, object]], field: str
) -> tuple[dict[str, object], bool]:
    fallback_entry: dict[str, object] | None = None
    fallback_raw: list[str] | None = None
    fallback_normalized: list[str] | None = None

    for entry in channels:
        values = entry.get(field)
        if not isinstance(values, list) or not values:
            continue
        channel_id = entry.get("id")
        if not isinstance(channel_id, str):
            continue
        raw = [str(value) for value in values]
        normalized = canonicalize_array(raw)
        if normalized != raw:
            return (
                {
                    "channel_id": channel_id,
                    "field": field,
                    "raw": raw,
                    "normalized": normalized,
                },
                False,
            )
        if fallback_entry is None:
            fallback_entry = entry
            fallback_raw = raw
            fallback_normalized = normalized

    if fallback_entry is None or fallback_raw is None or fallback_normalized is None:
        raise AssertionError(f"no {field} array found in channels_v1.json")

    return (
        {
            "channel_id": str(fallback_entry["id"]),
            "field": field,
            "raw": fallback_raw,
            "normalized": fallback_normalized,
        },
        True,
    )


def test_arrays_as_sets_registry_report():
    channels = _load_channels()
    centers_case, centers_fallback = _select_case(channels, "centers")
    domains_case, domains_fallback = _select_case(channels, "domains")

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
    if centers_fallback or domains_fallback:
        assert "note: raw == normalized (already canonical)" in report_text


def test_report_is_deterministic_and_check_mode_is_nonwriting():
    assert build_report().encode("utf-8") == REPORT_PATH.read_bytes()
    before = REPORT_PATH.stat().st_mtime_ns
    assert write_report(check=True) == REPORT_PATH
    assert REPORT_PATH.stat().st_mtime_ns == before
