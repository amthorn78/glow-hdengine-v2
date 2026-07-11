from wsgiref.util import setup_testing_defaults

import pytest

from adapter.app import app


def _call(path="/internal/version", headers=None):
    environ = {}
    setup_testing_defaults(environ)
    environ["REQUEST_METHOD"] = "GET"
    environ["PATH_INFO"] = path
    for key, value in (headers or {}).items():
        environ["HTTP_" + key.upper().replace("-", "_")] = value

    status_meta = {}

    def start_response(status, response_headers):
        status_meta["status"] = status
        status_meta["headers"] = dict(response_headers)

    body = b"".join(app(environ, start_response))
    return status_meta["status"], status_meta["headers"], body


def test_version_dev_allows_without_bearer_and_is_stable(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.setenv("ENGINE_ENV", "dev")
    monkeypatch.delenv("ENGINE_SERVICE_TOKEN", raising=False)

    status1, _headers1, body1 = _call()
    status2, _headers2, body2 = _call()

    assert status1.startswith("200")
    assert status2.startswith("200")
    assert body1.endswith(b"\n")
    assert body2 == body1


@pytest.mark.parametrize(
    ("env_key", "env_value"),
    (
        ("ENGINE_ENV", "prod"),
        ("APP_ENV", "prod"),
        ("APP_ENV", "production"),
        ("APP_ENV", "live"),
    ),
)
def test_version_prod_is_network_only_without_bearer(
    monkeypatch,
    env_key,
    env_value,
):
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.delenv("ENGINE_ENV", raising=False)
    monkeypatch.setenv(env_key, env_value)
    monkeypatch.setenv("ENGINE_SERVICE_TOKEN", "must-not-be-required")

    status, _headers, body = _call()
    status_with_header, _headers_with_header, body_with_header = _call(
        headers={"Authorization": "Bearer unrelated"}
    )

    assert status.startswith("200")
    assert status_with_header.startswith("200")
    assert body.endswith(b"\n")
    assert body_with_header == body
