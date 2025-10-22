import json, logging, re
from engine.config import provider_loader

def test_resolve_log_has_correlation_id(caplog, monkeypatch, tmp_path):
    # Ensure empty secrets to fall through to env/default cleanly
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))
    with caplog.at_level(logging.INFO):
        provider_loader.resolve_provider(correlation_id=None)
    # Find a success line
    msgs = [r.message for r in caplog.records if "provider.resolve" in r.message and ".error" not in r.message]
    assert msgs, "expected provider.resolve log line"
    obj = json.loads(msgs[-1])
    assert obj.get("route") == "provider.resolve"
    cid = obj.get("correlation_id", "")
    assert re.fullmatch(r"CID-[0-9a-f]{8}", cid), cid