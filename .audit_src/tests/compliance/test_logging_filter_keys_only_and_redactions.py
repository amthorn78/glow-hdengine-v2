import json
from adapter.wsgi import create_app

ALLOW_KEYS = {"ts","correlation_id","route","method","status","duration_ms","engine_tag","invocation_tag","release_id"}

def test_keys_only_log_and_redactions_and_echo_cid():
    app = create_app()
    sink = []
    app.config["LOG_SINK"] = sink
    app.config["ENGINE_TAG"] = "Isis6"
    app.config["RELEASE_ID"] = "rel_abc123"

    with app.test_client() as c:
        # Send sensitive headers (must never appear in log line)
        r = c.get(
            "/reader",
            headers={
                "X-Correlation-Id": "abc123",
                "X-Invocation-Id": "INV-aaaaaaaaaaaaaaaa",
                "Authorization": "Bearer secret",
                "Cookie": "id=1",
                "Proxy-Authorization": "Basic sss",
                "X-Api-Token": "tok",
            },
        )
        assert r.status_code in (200, 304, 401, 200)
        # Echo header present:
        assert r.headers.get("X-Correlation-Id") == "abc123"

    # One keys-only line captured
    assert len(sink) >= 1
    rec = json.loads(sink[-1])
    assert set(rec.keys()) == ALLOW_KEYS
    assert rec["correlation_id"] == "abc123"
    assert rec["route"] in ("adapter.http_reader.reader", "reader", "unknown")
    assert rec["engine_tag"] == "Isis6"
    assert rec["release_id"] == "rel_abc123"
    # Sensitive names should not be present as keys
    bad_keys = {"authorization","cookie","proxy-authorization","x-api-token","set-cookie"}
    assert not (set(k.lower() for k in rec.keys()) & bad_keys)
