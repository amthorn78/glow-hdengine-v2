from flask import Flask, Response
from adapter.etag_core import writer_headers, NO_STORE

def _app():
    app = Flask(__name__)
    @app.post("/writer")
    def writer():
        # 204 writer response: must have Cache-Control: no-store; no ETag.
        return Response(status=204, headers=writer_headers())
    @app.get("/boom")
    def boom():
        # Error branch: must also be no-store; no ETag.
        return Response('{"ok":false,"code":"Bad","error":"bad"}',
                        status=400,
                        headers=writer_headers(),
                        mimetype="application/json")
    return app

def test_writer_has_no_etag_and_no_store():
    app = _app()
    with app.test_client() as c:
        r = c.post("/writer")
        assert r.status_code == 204
        assert r.headers.get("ETag") is None
        assert r.headers.get("Cache-Control") == NO_STORE

def test_error_has_no_etag_and_no_store():
    app = _app()
    with app.test_client() as c:
        r = c.get("/boom")
        assert r.status_code == 400
        assert r.headers.get("ETag") is None
        assert r.headers.get("Cache-Control") == NO_STORE
