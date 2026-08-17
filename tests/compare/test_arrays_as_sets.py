import json
from pathlib import Path

from engine.mech.helpers import canonicalize_declared_set
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
    fallback_raw: list[object] | None = None
    fallback_normalized: list[object] | None = None

    for entry in channels:
        values = entry.get(field)
        if not isinstance(values, list) or not values:
            continue
        channel_id = entry.get("id")
        if not isinstance(channel_id, str):
            continue
        raw = list(values)
        normalized = canonicalize_declared_set(raw, identity=None)
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
    assert REPORT_PATH.exists()
    report_text = REPORT_PATH.read_text(encoding="utf-8")
    fallbacks: list[bool] = []
    for field in ("centers", "domains", "flags", "gates"):
        case, fallback = _select_case(channels, field)
        assert case["normalized"] == canonicalize_declared_set(
            case["raw"], identity=None
        )
        assert (
            f"catalog/channels_v1.json:channels[id={case['channel_id']}].{field}"
            in report_text
        )
        fallbacks.append(fallback)

    gates_case, _ = _select_case(channels, "gates")
    assert all(type(value) is int for value in gates_case["raw"])
    assert "arrays-as-sets report v1" in report_text
    if any(fallbacks):
        assert "note: raw == normalized (already canonical)" in report_text


def test_report_is_deterministic_and_check_mode_is_nonwriting():
    assert build_report().encode("utf-8") == REPORT_PATH.read_bytes()
    before = REPORT_PATH.stat().st_mtime_ns
    assert write_report(check=True) == REPORT_PATH
    assert REPORT_PATH.stat().st_mtime_ns == before
