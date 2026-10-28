"""The new entry against today's engine/charts/loader.py (HDE-EPIC041 WU-PR-01).

Proves equal results, errors and log fields for every call shape today's
supported path accepts. WU-PR-02 deletes this file with the loader. Only the
supported-path shapes are compared: a legacy-signature call would run the
provider resolver, which writes artifacts/provider/decision.txt.
"""
from __future__ import annotations

import json
from pathlib import Path

import pytest

import adapter.chart_orchestration as entry
import engine.charts.loader as loader
from engine.charts.pure import normalize_chart

ROOT = Path(__file__).resolve().parents[2]
CID = "CID-0123456789abcdef"
TZ = "Europe/Amsterdam"
GENERATOR = [
    {"birthdate": "1990-05-04", "birthtime": "14:22", "place": "Austin, US", "tz": TZ},
    {"birthdate": "1992-07-19", "birthtime": "08:05", "place": "New York, US", "tz": TZ},
]
SHAPES = [
    (("1990-01-01", "12:34", "Amsterdam, NL"), {"tz": TZ}),
    (("1990-01-01", "12:34", "Amsterdam, NL", TZ), {}),
    (("1990-02-30", "12:34", "Amsterdam, NL"), {"tz": TZ}),
    (("1990-01-01", "24:00", "Amsterdam, NL"), {"tz": TZ}),
    (("1990-01-01", "12:34", "Nowhere"), {"tz": TZ}),
    (("1990-01-01", "12:34", "Amsterdam, NL"), {}),
    (("1990-01-01", "12:34", "Amsterdam, NL"), {"tz": "Europe/NotARealCity"}),
    ((), GENERATOR[0]),
    ((), GENERATOR[1]),
    ((), {"birthdate": "1990-02-30", "birthtime": "12:34", "place": "Amsterdam, NL", "tz": TZ}),
    ((), {"birthdate": "1990-01-01", "birthtime": "12:34", "place": "Amsterdam, NL"}),
    ((), {}),
    (("1990-01-01",), {}),
]


def _outcome(fn, args, kwargs):
    try:
        return ("ok", fn(*args, correlation_id=CID, **kwargs))
    except TypeError as e:
        return ("TypeError", str(e))
    except Exception as e:
        return ("typed", e.code, e.details.get("field"), e.message)


@pytest.mark.parametrize("args,kwargs", SHAPES)
def test_entry_matches_todays_loader(monkeypatch, tmp_path, args, kwargs):
    monkeypatch.chdir(ROOT)  # today's validators read the pinned lists relative to the CWD
    monkeypatch.setattr(loader, "_Path", lambda p: tmp_path / p)
    lines: list[str] = []
    assert _outcome(entry.load_chart, args, dict(kwargs, log_sink=lines.append)) == _outcome(loader.load_chart, args, kwargs)
    # Today's keyword form writes a second line from its recursive call; its last line is the call's own.
    today = json.loads((tmp_path / "artifacts/logs/loader_call.jsonl").read_text(encoding="utf-8").splitlines()[-1])
    assert len(lines) == 1
    new = json.loads(lines[0])
    for key in ("ts", "duration_ms"):
        today.pop(key)
        new.pop(key)
    assert new == today


def test_normalize_chart_matches_todays_normalizer():
    fixture = entry._fixture_chart()
    assert normalize_chart(fixture) == loader._normalize_chart(fixture)
