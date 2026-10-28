
from __future__ import annotations
import json, re
from adapter.chart_orchestration import load_chart

CID_RE = re.compile(r"^CID-[a-f0-9]{16}$")
TS_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")

def test_loader_emits_keys_only_log(monkeypatch):
    # Ensure SAFE_MODE=1 so log shows safe_mode True
    monkeypatch.setenv("SAFE_MODE", "1")
    data: list[str] = []

    load_chart("1990-01-01","12:34","Amsterdam, NL", tz="Europe/Amsterdam", correlation_id="CID-0123456789abcdef", log_sink=data.append)

    assert len(data) == 1, data
    last = json.loads(data[-1])
    # Required keys present
    for k in ("ts","route","provider","source","status","duration_ms","safe_mode","correlation_id"):
        assert k in last
    # Shape and values
    assert last["route"] == "loader.load_chart"
    assert isinstance(last["duration_ms"], int)
    assert isinstance(last["safe_mode"], bool) and last["safe_mode"] is True
    assert CID_RE.match(last["correlation_id"])

    # Keys-only: ensure no inputs leaked. ts is the clock: pinned to its shape and
    # left out of the substring check (at 12:34 UTC it holds "12:34").
    assert TS_RE.match(last["ts"])
    raw = data[-1].replace(last["ts"], "", 1)
    for forbidden in ("birthdate","birthtime","location","place","Amsterdam","1990-01-01","12:34"):
        assert forbidden not in raw
