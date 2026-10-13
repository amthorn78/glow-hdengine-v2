import json, io
from wsgiref.util import setup_testing_defaults
from adapter.app import app

def _call(path="/internal/healthz", headers=None):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"
    environ["PATH_INFO"] = path
    headers = headers or {}
    for k, v in headers.items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v

    status_holder = {}
    def start_response(status, hdrs):
        status_holder["status"] = status
        status_holder["headers"] = dict(hdrs)
    body_chunks = list(app(environ, start_response))
    body = b"".join(body_chunks)
    return status_holder["status"], status_holder["headers"], body

def test_healthz_headers_and_identity():
    # First call without correlation id (adapter should generate it)
    st1, h1, b1 = _call()
    assert st1.startswith("200")
    # Required headers present (dev: no HSTS)
    for hk in ("Cache-Control","Content-Type","X-Adapter-Version","X-Engine-Tag","X-Release-Id","X-Correlation-Id","X-Content-Type-Options","Referrer-Policy","X-Frame-Options"):
        assert hk in h1
    assert h1["Cache-Control"] == "no-store"
    assert h1["Content-Type"].startswith("application/json")

    # Body is exact, newline-terminated, minified & stable
    assert b1.endswith(b"\n")
    assert b1 == b'{"ok":true,"schema":"v1"}\n'

    # Second call with explicit correlation id; must echo exactly; body must be byte-identical
    corr = "abc123" * 6  # 36 chars OK; not strictly UUID but acceptable for echo
    st2, h2, b2 = _call(headers={"X-Correlation-Id": corr})
    assert st2.startswith("200")
    assert h2["X-Correlation-Id"] == corr
    assert b2 == b1  # byte identity across calls (dev)

def _call_with_env(monkeypatch, path="/internal/healthz", headers=None, env_overrides=None):
    from wsgiref.util import setup_testing_defaults
    # APP_ENV takes precedence over ENGINE_ENV in adapter/wsgi.py; clear it so the
    # ENGINE_ENV override is the effective environment, and restore after the test.
    monkeypatch.delenv("APP_ENV", raising=False)
    for k, v in (env_overrides or {}).items():
        monkeypatch.setenv(k, v)
    environ = {}; setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"; environ["PATH_INFO"] = path
    headers = headers or {}
    for k, v in headers.items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v
    status_meta = {}
    def start_response(status, hdrs):
        status_meta["status"] = status
        status_meta["headers"] = dict(hdrs)
    body = b"".join(app(environ, start_response))
    return status_meta["status"], status_meta["headers"], body

def test_hsts_header_prod_only(monkeypatch):
    # dev -> no HSTS
    st, h, b = _call_with_env(monkeypatch, env_overrides={"ENGINE_ENV": "dev"})
    assert "Strict-Transport-Security" not in h
    # prod -> HSTS present
    st2, h2, b2 = _call_with_env(monkeypatch, env_overrides={"ENGINE_ENV": "prod"})
    assert h2.get("Strict-Transport-Security") == "max-age=31536000; includeSubDomains"

def test_access_log_one_line_per_request(monkeypatch):
    # adapter/logging_filter.py emits exactly one keys-only line per request to the
    # app's LOG_SINK (and the "engine.app" logger); no correlation id or path is logged.
    sink = []
    monkeypatch.setitem(app.config, "LOG_SINK", sink)
    st, h, b = _call_with_env(monkeypatch, env_overrides={"ENGINE_ENV": "dev"})
    assert st.startswith("200")
    assert len(sink) == 1
    rec = json.loads(sink[0])
    assert set(rec) == {"at", "route", "status", "duration_ms", "idempotence_hash", "release_id"}
    assert rec["status"] == 200
    assert rec["route"] == "internal_healthz"
