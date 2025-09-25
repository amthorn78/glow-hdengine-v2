import os, json, pathlib, time
from wsgiref.util import setup_testing_defaults
import adapter.app as A

OVR = pathlib.Path("config/runtime_overrides.json")

def _call(path="/internal/readyz", headers=None, env_overrides=None):
    if env_overrides:
        os.environ.update(env_overrides)
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"
    environ["PATH_INFO"] = path
    headers = headers or {}
    for k, v in headers.items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v
    meta = {}
    def start_response(status, hdrs):
        meta["status"] = status
        meta["headers"] = dict(hdrs)
    body = b"".join(A.app(environ, start_response))
    return meta["status"], meta["headers"], body

def test_ready_ok_and_headers_and_latency():
    if OVR.exists(): OVR.unlink()
    t0 = time.perf_counter()
    st, h, b = _call(env_overrides={"ENGINE_ENV": "dev"})
    elapsed_ms = (time.perf_counter() - t0) * 1000.0
    assert st.startswith("200")
    assert b == b'{"ok":true,"schema":"v1"}\n'
    assert "X-Toggles-SHA" in h and len(h["X-Toggles-SHA"]) == 64
    assert elapsed_ms <= 800.0

def test_prod_override_503_enforced():
    # Create prod override file -> expect 503 OverridesNotAllowedInProd
    OVR.parent.mkdir(parents=True, exist_ok=True)
    OVR.write_text('{"experiment":{"patch":{"intimacy.mode":"aggressive"}}}', encoding="utf-8")
    try:
        st, h, b = _call(env_overrides={"ENGINE_ENV": "prod"})
        assert st.startswith("503")
        assert b == b'{"code":"OverridesNotAllowedInProd","error":"Overrides present in prod","ok":false,"schema":"v1"}\n'
    finally:
        if OVR.exists(): OVR.unlink()

def test_generic_resolver_failure_503():
    # Monkeypatch the resolver wrapper to raise a generic error
    orig = A._resolve
    try:
        def boom(): raise RuntimeError("boom")
        A._resolve = boom
        st, h, b = _call(env_overrides={"ENGINE_ENV": "dev"})
        assert st.startswith("503")
        assert b == b'{"code":"DependencyFailure","error":"resolver","ok":false,"schema":"v1"}\n'
    finally:
        A._resolve = orig
