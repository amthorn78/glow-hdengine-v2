import json, re
from adapter.wsgi import create_app

def _app():
    return create_app()

def test_retry_after_seconds_maps_to_ms_and_no_etag_no_store():
    app = _app()
    with app.test_client() as c:
        r = c.get("/_test/429_seconds?sec=7")
        assert r.status_code == 429
        assert r.headers.get("ETag") is None
        assert r.headers.get("Cache-Control") == "no-store"
        body = json.loads(r.data.decode("utf-8"))
        assert body["reader_version"] == "v1"
        err = body["error"]
        assert isinstance(err.get("retry_after_ms"), int)
        assert err["retry_after_ms"] == 7000  # exact for seconds form
        # LF termination is enforced by serializer: body bytes end with \n
        assert r.data.endswith(b"\n")

def test_retry_after_http_date_maps_to_ms_non_negative_and_reasonable_window():
    app = _app()
    with app.test_client() as c:
        r = c.get("/_test/429_date?delta=5")
        assert r.status_code == 429
        assert r.headers.get("ETag") is None
        body = json.loads(r.data.decode("utf-8"))
        ms = body["error"]["retry_after_ms"]
        assert isinstance(ms, int)
        # allow a small window due to test execution time
        assert 3000 <= ms <= 6000
