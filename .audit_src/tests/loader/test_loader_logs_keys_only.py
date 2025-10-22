
from __future__ import annotations
import json, os, re
from pathlib import Path
from engine.charts.loader import load_chart

CID_RE = re.compile(r"^CID-[a-f0-9]{16}$")

def test_loader_emits_keys_only_log(monkeypatch, tmp_path):
    # Ensure SAFE_MODE=1 so log shows safe_mode True
    monkeypatch.setenv("SAFE_MODE", "1")
    logf = Path("artifacts/logs/loader_call.jsonl")
    if logf.exists():
        logf.unlink()

    load_chart("1990-01-01","12:34","Amsterdam, NL", tz="Europe/Amsterdam", correlation_id="CID-0123456789abcdef")

    data = logf.read_text(encoding="utf-8").strip().splitlines()
    assert data, "no log lines found"
    last = json.loads(data[-1])
    # Required keys present
    for k in ("ts","route","provider","source","status","duration_ms","safe_mode","correlation_id"):
        assert k in last
    # Shape and values
    assert last["route"] == "loader.load_chart"
    assert isinstance(last["duration_ms"], int)
    assert isinstance(last["safe_mode"], bool) and last["safe_mode"] is True
    assert CID_RE.match(last["correlation_id"])

    # Keys-only: ensure no inputs leaked
    raw = data[-1]
    for forbidden in ("birthdate","birthtime","location","place","Amsterdam","1990-01-01","12:34"):
        assert forbidden not in raw
