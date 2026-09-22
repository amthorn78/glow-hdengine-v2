import json, hashlib
from adapter.wsgi import create_app
from engine.stable.sercanon import serialize
from tests.support.pr04_fixtures import build_bundle, build_pack, inject_seams

def test_keys_only_log_snapshot_and_sha256(monkeypatch, tmp_path):
    monkeypatch.setenv("APP_ENV", "dev")
    # The canonical-bytes round trip below writes its own sample, and the record
    # carries a wall-clock "at", so the bytes differ on every run. Writing them
    # into the tracked tree would leave the candidate dirty; this test is the
    # only reader or writer of that path, and nothing indexes it.
    snap = tmp_path / "keys_only_sample.jsonl"
    total = tmp_path / "keys_only_sample.jsonl.sha256"
    # The subject is the keys-only log shape, so the request has to reach a
    # served response: without an admitted release the route refuses 503 and
    # never emits the line under test.
    inject_seams(monkeypatch, build_bundle(tmp_path), build_pack(tmp_path))

    app = create_app()
    sink = []
    app.config["LOG_SINK"] = sink
    app.config["ENGINE_TAG"] = "Isis6"
    app.config["RELEASE_ID"] = "rel_dev_abcd1234"  # any >=8 chars OK

    with app.test_client() as c:
        r = c.get(
            "/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo",
            headers={
                "X-Correlation-Id": "cid123",
                "X-Invocation-Id": "INV-aaaaaaaaaaaaaaaa",
                "Authorization": "Bearer secret-should-not-log",
                "Cookie": "id=1; secret=yes",
                "Proxy-Authorization": "Basic abc",
                "X-Api-Token": "tok",
            },
        )
        assert r.status_code in (200, 304)

    # Grab the last emitted keys-only line (sink may hold dict or JSON string)
    assert len(sink) >= 1
    rec = sink[-1]
    if isinstance(rec, str):
        rec = json.loads(rec)

    # Required keys present; no bodies or sensitive values
    want = {"at","route","status","duration_ms","idempotence_hash","release_id"}
    assert want.issubset(rec.keys())
    assert "Authorization" not in json.dumps(rec) and "Cookie" not in json.dumps(rec)

    # Canonical one-line JSONL + sha256 sidecar
    b = serialize(rec)
    snap.write_bytes(b)
    h = hashlib.sha256(b).hexdigest()
    total.write_text(h + "\n", encoding="utf-8")

    # Re-open and verify
    b2 = snap.read_bytes()
    assert b2.endswith(b"\n")
    assert hashlib.sha256(b2).hexdigest() == h
