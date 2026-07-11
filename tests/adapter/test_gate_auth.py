import os
from wsgiref.util import setup_testing_defaults
from adapter.app import app

def _call(path="/internal/version", headers=None, env_overrides=None):
    # Allow per-call env adjustments (ENGINE_ENV, ENGINE_SERVICE_TOKEN)
    if env_overrides:
        os.environ.update(env_overrides)
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"
    environ["PATH_INFO"] = path
    headers = headers or {}
    for k, v in headers.items():
        environ["HTTP_" + k.upper().replace("-", "_")] = v

    status_meta = {}
    def start_response(status, hdrs):
        status_meta["status"] = status
        status_meta["headers"] = dict(hdrs)
    body = b"".join(app(environ, start_response))
    return status_meta["status"], status_meta["headers"], body

def test_version_dev_allows_without_bearer_and_is_stable():
    st1, h1, b1 = _call(env_overrides={"ENGINE_ENV": "dev"})
    assert st1.startswith("200")
    assert b1.endswith(b"\n")
    # Call again (dev) -> byte-identical
    st2, h2, b2 = _call(env_overrides={"ENGINE_ENV": "dev"})
    assert st2.startswith("200")
    assert b2 == b1

def test_version_prod_requires_bearer_and_errors_shape_is_canonical(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)
    # Missing header -> 401 Unauthorized with normalized envelope
    st, h, b = _call(env_overrides={"ENGINE_ENV": "prod", "ENGINE_SERVICE_TOKEN": "s3cr3t"})
    assert st.startswith("401")
    assert b.endswith(b"\n")
    assert b == b'{"code":"Unauthorized","error":"InvalidOrMissingToken","ok":false,"schema":"v1"}\n'

    # Wrong token -> 401 Unauthorized
    st2, h2, b2 = _call(headers={"Authorization": "Bearer nope"}, env_overrides={"ENGINE_ENV": "prod", "ENGINE_SERVICE_TOKEN": "s3cr3t"})
    assert st2.startswith("401")
    assert b2 == b

    # Correct token -> 200
    st3, h3, b3 = _call(headers={"Authorization": "Bearer s3cr3t"}, env_overrides={"ENGINE_ENV": "prod", "ENGINE_SERVICE_TOKEN": "s3cr3t"})
    assert st3.startswith("200")
    assert b3.endswith(b"\n")

def test_version_app_env_prod_alias_requires_bearer(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    monkeypatch.delenv("ENGINE_ENV", raising=False)
    monkeypatch.setenv("ENGINE_SERVICE_TOKEN", "s3cr3t")
    st, _h, b = _call()
    assert st.startswith("401")
    assert b == b'{"code":"Unauthorized","error":"InvalidOrMissingToken","ok":false,"schema":"v1"}\n'
    st2, _h2, _b2 = _call(headers={"Authorization": "Bearer s3cr3t"})
    assert st2.startswith("200")
