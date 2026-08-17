import json
from pathlib import Path

import pytest

from engine.mech.helpers import canonicalize_declared_set
from tools.evidence import generate_arrays_as_sets_report as report_generator
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
    normalized_channels = canonicalize_declared_set(channels, identity="id")
    assert channels == normalized_channels
    assert "path: catalog/channels_v1.json:channels\n" in report_text
    assert (
        "normalizer: engine.mech.helpers.canonicalize_declared_set(identity=id)"
        in report_text
    )
    assert "raw identities: " in report_text
    assert "normalized identities: " in report_text
    for field in ("centers", "domains", "flags", "gates"):
        case, fallback = _select_case(channels, field)
        assert case["raw"] == case["normalized"]
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


def test_report_render_helpers_intrinsically_reject_noncanonical_sets():
    channels = _load_channels()
    nested = json.loads(json.dumps(channels))
    nested[0]["centers"] = list(reversed(nested[0]["centers"]))
    with pytest.raises(
        SystemExit,
        match=r"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:\$\.channels\[0\]\.centers$",
    ):
        report_generator._select_case(nested, "centers")

    top_level = list(reversed(channels))
    with pytest.raises(
        SystemExit,
        match=r"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:\$\.channels$",
    ):
        report_generator._render_channel_roster_case(top_level)


def test_report_is_deterministic_and_check_mode_is_nonwriting():
    assert build_report().encode("utf-8") == REPORT_PATH.read_bytes()
    before = REPORT_PATH.stat().st_mtime_ns
    assert write_report(check=True) == REPORT_PATH
    assert REPORT_PATH.stat().st_mtime_ns == before


def _write_channels(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


def test_build_report_rejects_noncanonical_top_level_channel_set(
    tmp_path, monkeypatch
):
    payload = json.loads(CHANNELS_PATH.read_text(encoding="utf-8"))
    payload["channels"] = list(reversed(payload["channels"]))
    source = tmp_path / "channels_v1.json"
    _write_channels(source, payload)
    monkeypatch.setattr(report_generator, "CHANNELS_PATH", source)

    with pytest.raises(
        SystemExit,
        match=r"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:\$\.channels$",
    ):
        build_report()


@pytest.mark.parametrize("field", ("centers", "domains", "flags", "gates"))
def test_build_report_rejects_every_noncanonical_nested_channel_set(
    tmp_path, monkeypatch, field
):
    payload = json.loads(CHANNELS_PATH.read_text(encoding="utf-8"))
    channels = payload["channels"]
    if field == "flags":
        index = next(i for i, row in enumerate(channels) if row[field])
        channels[index][field] = channels[index][field] * 2
    else:
        index = next(i for i, row in enumerate(channels) if len(row[field]) > 1)
        channels[index][field] = list(reversed(channels[index][field]))
    source = tmp_path / "channels_v1.json"
    _write_channels(source, payload)
    monkeypatch.setattr(report_generator, "CHANNELS_PATH", source)

    with pytest.raises(
        SystemExit,
        match=rf"ARRAYS_AS_SETS_SOURCE_NONCANONICAL:\$\.channels\[{index}\]\.{field}$",
    ):
        build_report()


def test_write_report_rejects_noncanonical_source_without_overwriting(
    tmp_path, monkeypatch
):
    payload = json.loads(CHANNELS_PATH.read_text(encoding="utf-8"))
    payload["channels"][0]["gates"] = list(
        reversed(payload["channels"][0]["gates"])
    )
    source = tmp_path / "channels_v1.json"
    output = tmp_path / "arrays_as_sets_report.log"
    _write_channels(source, payload)
    output.write_bytes(b"preserve-me\n")
    monkeypatch.setattr(report_generator, "CHANNELS_PATH", source)
    monkeypatch.setattr(report_generator, "REPORT_PATH", output)

    with pytest.raises(SystemExit, match="ARRAYS_AS_SETS_SOURCE_NONCANONICAL"):
        write_report()
    assert output.read_bytes() == b"preserve-me\n"


def test_check_mode_rejects_noncanonical_source_before_staleness(
    tmp_path, monkeypatch
):
    payload = json.loads(CHANNELS_PATH.read_text(encoding="utf-8"))
    payload["channels"][0]["centers"] = list(
        reversed(payload["channels"][0]["centers"])
    )
    source = tmp_path / "channels_v1.json"
    output = tmp_path / "arrays_as_sets_report.log"
    _write_channels(source, payload)
    output.write_bytes(REPORT_PATH.read_bytes())
    before = output.stat().st_mtime_ns
    monkeypatch.setattr(report_generator, "CHANNELS_PATH", source)
    monkeypatch.setattr(report_generator, "REPORT_PATH", output)

    with pytest.raises(SystemExit, match="ARRAYS_AS_SETS_SOURCE_NONCANONICAL"):
        write_report(check=True)
    assert output.read_bytes() == REPORT_PATH.read_bytes()
    assert output.stat().st_mtime_ns == before
