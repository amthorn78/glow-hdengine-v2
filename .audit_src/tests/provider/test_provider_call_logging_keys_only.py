import os, json, re, pytest
from engine.charts.loader import load_chart
from engine.providers.vendor_http import VendorHttpProvider
from engine.config.provider_errors import ProviderUnavailable

CIDRE = re.compile(r"^CID-[0-9a-f]{8}$")

def _parse_jsonl(messages):
    # Each log record .message is a JSON line
    recs = []
    for m in messages:
        try:
            recs.append(json.loads(m))
        except Exception:
            pass
    return recs

def test_logging_keys_only_on_ok(caplog, monkeypatch):
    caplog.clear()
    # Default fixtures via resolver under SAFE_MODE
    monkeypatch.setenv("SAFE_MODE", "1")
    with caplog.at_level("INFO", logger="provider"):
        load_chart("user-abc", correlation_id="CID-deadbeef")
    # Find at least one provider.call line
    msgs = [r.message for r in caplog.records if r.name == "provider"]
    recs = [r for r in _parse_jsonl(msgs) if r.get("route") == "provider.call"]
    assert recs, "expected provider.call log"
    rec = recs[-1]
    # Required keys
    assert set(rec.keys()) == {"ts","route","provider","op","status","duration_ms","safe_mode","correlation_id"}
    assert rec["op"] == "get_chart"
    assert rec["provider"] in {"fixtures","internal_engine","vendor_http"}
    assert rec["status"] == "ok"
    assert isinstance(rec["duration_ms"], int)
    assert rec["safe_mode"] in (True, False)  # placeholder flag present
    assert CIDRE.match(rec["correlation_id"])
    # No payloads / user ids
    assert "user" not in json.dumps(rec)
    assert "gates" not in json.dumps(rec)

def test_logging_unavailable_on_gated_vendor(caplog, monkeypatch):
    caplog.clear()
    # Force vendor under SAFE_MODE=1 to trigger unavailability
    monkeypatch.setenv("SAFE_MODE", "1")
    import engine.charts.loader as L
    L.resolve_provider = lambda: VendorHttpProvider()  # type: ignore
    with pytest.raises(ProviderUnavailable):
        with caplog.at_level("INFO", logger="provider"):
            load_chart("user-xyz")
    msgs = [r.message for r in caplog.records if r.name == "provider"]
    recs = [r for r in _parse_jsonl(msgs) if r.get("route") == "provider.call"]
    assert recs, "expected provider.call log"
    rec = recs[-1]
    assert rec["status"] == "unavailable"
    assert rec["provider"] == "vendor_http"
    assert CIDRE.match(rec["correlation_id"])
    # No payload leakage
    s = json.dumps(rec)
    assert "user" not in s and "gates" not in s and "token" not in s
