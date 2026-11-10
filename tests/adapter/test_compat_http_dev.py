import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

from adapter import factory as _factory
from adapter import http_reader as _http_reader
from adapter import wsgi as _wsgi
from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.http import compat_handler as _compat_handler
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-compat-dev-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-compat-dev-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def _dev_client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _minimal_payload():
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    return {
        "a": complete_chart(UUID_A, GATES_A),
        "b": complete_chart(UUID_B, GATES_B),
        "viewer_prefs": {"top_category": CATEGORIES_ORDER_V1[0], "weights": weights},
    }


def test_dev_compat_malformed_json_returns_governed_error_json():
    client = _dev_client()
    resp = client.post("/api/compat/v1", data=b"{bad: json", headers={"Content-Type": "application/json; charset=utf-8"})
    assert resp.status_code == 400
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    body_bytes = resp.data
    assert body_bytes.endswith(b"\n")
    payload = json.loads(body_bytes.decode("utf-8"))
    assert payload.get("ok") is False
    assert isinstance(payload.get("code"), str)
    assert isinstance(payload.get("error"), str)
    assert "<html" not in body_bytes.decode("utf-8").lower()


def test_dev_compat_minimal_valid_payload_success_behavior(bundle):
    client = _dev_client()
    resp = client.post("/api/compat/v1", data=json.dumps(_minimal_payload(), sort_keys=True), headers={"Content-Type": "application/json; charset=utf-8"})
    assert resp.status_code == 200
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert resp.headers.get("Cache-Control") == "no-store"
    body_bytes = resp.data
    assert body_bytes.endswith(b"\n")
    data = json.loads(body_bytes.decode("utf-8"))
    assert data["schema"] == "magic10_compat_result.v1"
    assert data["release_id"] == bundle.release_id
    assert "meta" not in data and "keys" not in data


# --- HDE-CRD-0003 S03: the compat namespace's dev/admin gate (step 2)
# HDE CLI/API/Vendor Ref §5.5 "Dev/admin gate (step 2)"; HDE Governance §4.1.4
# "Compat namespace (dev/admin surface)". Step 1, the production-like 404, is pinned
# in tests/http/test_compat_endpoint_contract.py and unchanged.

_ROOT = Path(__file__).resolve().parents[2]
_FACTORIES = {
    "factory": _factory.create_app,
    "http_reader": _http_reader.create_app,
    "wsgi": _wsgi.create_app,
}
_FORBIDDEN_BODY = b'{"code":"ERR_WRITER_FORBIDDEN","error":"insufficient scope","ok":false,"schema":"v1"}\n'
# (APP_ENV, ENGINE_ENV); ``None`` is unset. None of these resolves production-like.
_REFUSED_ENVS = [
    (None, None),
    ("", None),
    ("staging", None),
    ("Dev", None),
    (" dev ", None),
    ("DEV", None),
    ("development", None),
    (None, "dev"),
    (None, "test"),
    (None, "local"),
    ("", "dev"),
    (None, "staging"),
]
_ADMITTED_ENVS = [("dev", None), ("test", None), ("local", None), ("dev", "staging"), ("local", "dev")]
_EXACT_PATH_METHODS = ["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "PATCH"]
_DESCENDANTS = ["/api/compat/v1/", "/api/compat/v1/x", "/api/compat/v1/x/y"]


def _gate_env(monkeypatch, app_env, engine_env):
    for key, value in (("APP_ENV", app_env), ("ENGINE_ENV", engine_env)):
        if value is None:
            monkeypatch.delenv(key, raising=False)
        else:
            monkeypatch.setenv(key, value)


@pytest.fixture()
def compat_spies(monkeypatch):
    """Count the route's database, row, resolution and evaluation calls; each spy calls through."""

    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor client constructed"))
    calls = {"db": 0, "row_read": 0, "resolve": 0, "evaluate": 0}

    def _counting(name, fn):
        def _spy(*args, **kwargs):
            calls[name] += 1
            return fn(*args, **kwargs)

        return _spy

    monkeypatch.setattr(_compat_handler.DBAccess, "for_current_env", _counting("db", _compat_handler.DBAccess.for_current_env))
    monkeypatch.setattr(_compat_handler, "read_current_mapped_bodygraph", _counting("row_read", _compat_handler.read_current_mapped_bodygraph))
    monkeypatch.setattr(_compat_handler, "resolve_compat_chart", _counting("resolve", _compat_handler.resolve_compat_chart))
    monkeypatch.setattr(_compat_handler, "evaluate_pair", _counting("evaluate", _compat_handler.evaluate_pair))
    return calls


def _gate_client(factory):
    app = _FACTORIES[factory]()
    app.config.update(TESTING=True)
    return app.test_client()


def _stored_payload():
    return {"a_id": UUID_A, "b_id": UUID_B, "viewer_prefs": _minimal_payload()["viewer_prefs"]}


def _gate_requests(client):
    for method in _EXACT_PATH_METHODS:
        kwargs = {"json": _minimal_payload()} if method == "POST" else {}
        yield f"{method} /api/compat/v1", method, client.open("/api/compat/v1", method=method, **kwargs)
    yield "POST /api/compat/v1 (stored ids)", "POST", client.post("/api/compat/v1", json=_stored_payload())
    for path in _DESCENDANTS:
        for method in ("GET", "POST", "HEAD"):
            kwargs = {"json": _stored_payload()} if method == "POST" else {}
            yield f"{method} {path}", method, client.open(path, method=method, **kwargs)


def _assert_forbidden(label, method, resp):
    assert resp.status_code == 403, label
    assert resp.headers["Cache-Control"] == "no-store", label
    assert "ETag" not in resp.headers, label
    if method == "HEAD":
        assert resp.data == b"", label
    else:
        assert resp.data == _FORBIDDEN_BODY, label
        assert resp.headers["Content-Type"] == "application/json; charset=utf-8", label


@pytest.mark.parametrize("factory", sorted(_FACTORIES))
@pytest.mark.parametrize("app_env,engine_env", _REFUSED_ENVS)
def test_s03_compat_namespace_refuses_outside_exact_dev_test_local(monkeypatch, compat_spies, factory, app_env, engine_env):
    _gate_env(monkeypatch, app_env, engine_env)
    client = _gate_client(factory)
    for label, method, resp in _gate_requests(client):
        _assert_forbidden(label, method, resp)
    assert compat_spies == {"db": 0, "row_read": 0, "resolve": 0, "evaluate": 0}


@pytest.mark.parametrize("factory", sorted(_FACTORIES))
@pytest.mark.parametrize("app_env,engine_env", _ADMITTED_ENVS)
def test_s03_compat_namespace_admits_exact_dev_test_local(monkeypatch, compat_spies, factory, app_env, engine_env):
    _gate_env(monkeypatch, app_env, engine_env)
    client = _gate_client(factory)
    probe = client.get("/api/compat/v1")
    assert probe.status_code == 200 and probe.data == b'{"ok":true,"schema":"v1"}\n'
    head = client.head("/api/compat/v1")
    assert head.status_code == 405 and head.data == b"" and head.headers["Allow"] == "POST, OPTIONS"
    options = client.open("/api/compat/v1", method="OPTIONS")
    assert options.status_code == 204 and options.data == b"" and options.headers["Allow"] == "POST, OPTIONS"
    put = client.put("/api/compat/v1")
    assert put.status_code == 405 and put.get_json()["code"] == "ERR_NOT_FOUND"
    descendant = client.get("/api/compat/v1/x")
    assert descendant.status_code == 404 and descendant.get_json()["code"] == "ERR_NOT_FOUND"
    result = client.post("/api/compat/v1", json=_minimal_payload())
    assert result.status_code == 200
    assert result.get_json()["schema"] == "magic10_compat_result.v1"
    assert compat_spies["resolve"] == 2 and compat_spies["evaluate"] == 1
    # The stored-id path reaches the governed database seam (no database is configured here).
    client.post("/api/compat/v1", json=_stored_payload())
    assert compat_spies["db"] >= 1


@pytest.mark.parametrize("app_env", [None, "", "staging"])
def test_s03_refusal_is_the_dev_admin_writer_refusal(monkeypatch, app_env):
    _gate_env(monkeypatch, app_env, None)
    client = _gate_client("http_reader")
    compat = client.post("/api/compat/v1", json=_minimal_payload())
    sampler = client.post("/internal/dev/sampler", json={})
    assert compat.status_code == sampler.status_code == 403
    assert compat.data == sampler.data == _FORBIDDEN_BODY
    for header in ("Content-Type", "Cache-Control", "Content-Length"):
        assert compat.headers[header] == sampler.headers[header]
    assert "ETag" not in compat.headers and "ETag" not in sampler.headers


@pytest.mark.parametrize("app_env", [None, "staging"])
def test_s03_unrelated_prefix_is_not_the_compat_namespace(monkeypatch, app_env):
    _gate_env(monkeypatch, app_env, None)
    resp = _gate_client("factory").get("/api/compat/v10")
    assert resp.status_code == 404
    assert resp.get_json()["code"] == "ERR_NOT_FOUND"


@pytest.mark.parametrize("app_env", ["prod", "production", "live", " Production "])
@pytest.mark.parametrize("engine_env", [None, "dev"])
def test_s03_production_like_posture_keeps_the_step_one_not_found(monkeypatch, app_env, engine_env):
    _gate_env(monkeypatch, app_env, engine_env)
    client = _gate_client("factory")
    for method in _EXACT_PATH_METHODS:
        kwargs = {"json": _minimal_payload()} if method == "POST" else {}
        resp = client.open("/api/compat/v1", method=method, **kwargs)
        assert resp.status_code == 404, method
        assert resp.headers["Cache-Control"] == "no-store", method
        if method == "HEAD":
            assert resp.data == b"", method
        else:
            assert resp.get_json()["code"] == "ERR_NOT_FOUND", method


# --- HDE-CRD-0003 S03 ("Dev surfaces"; Audit EC-4): ``run_flask_dev.sh`` defaults
# ``APP_ENV=dev`` only when neither ``APP_ENV`` nor ``ENGINE_ENV`` is set, the one case
# ``adapter/env_guard.py`` already resolves as ``dev``; any value the caller set is kept.


def _run_dev_helper(tmp_path, app_env, engine_env):
    work = tmp_path / "checkout"
    (work / ".venv" / "bin").mkdir(parents=True)
    (work / ".venv" / "bin" / "activate").write_text("", encoding="utf-8")
    shutil.copyfile(_ROOT / "run_flask_dev.sh", work / "run_flask_dev.sh")
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    shim = bin_dir / "python"
    # Stands in for the interpreter: report the APP_ENV the helper hands to run_flask.py.
    shim.write_text(
        '#!/bin/sh\n'
        'if [ "${APP_ENV+set}" = set ]; then printf "APP_ENV=<%s>\\n" "$APP_ENV"; else echo "APP_ENV unset"; fi\n'
        'echo "argv=$*"\n',
        encoding="utf-8",
    )
    shim.chmod(0o755)
    env = {"PATH": os.pathsep.join([str(bin_dir), "/usr/bin", "/bin"]), "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}
    if app_env is not None:
        env["APP_ENV"] = app_env
    if engine_env is not None:
        env["ENGINE_ENV"] = engine_env
    proc = subprocess.run(
        [shutil.which("bash") or "/bin/bash", str(work / "run_flask_dev.sh")],
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    assert proc.returncode == 0, proc.stderr
    assert "argv=run_flask.py" in proc.stdout.splitlines()
    return proc.stdout.splitlines()


@pytest.mark.parametrize(
    "app_env,engine_env,expected",
    [
        (None, None, "APP_ENV=<dev>"),
        ("", None, "APP_ENV=<dev>"),
        (None, "", "APP_ENV=<dev>"),
        ("dev", None, "APP_ENV=<dev>"),
        ("test", None, "APP_ENV=<test>"),
        ("local", None, "APP_ENV=<local>"),
        ("staging", None, "APP_ENV=<staging>"),
        ("Dev", None, "APP_ENV=<Dev>"),
        ("prod", None, "APP_ENV=<prod>"),
        ("test", "prod", "APP_ENV=<test>"),
        (None, "prod", "APP_ENV unset"),
        (None, "dev", "APP_ENV unset"),
        ("", "production", "APP_ENV=<>"),
    ],
)
def test_s03_run_flask_dev_defaults_app_env_only_when_neither_variable_is_set(tmp_path, app_env, engine_env, expected):
    assert expected in _run_dev_helper(tmp_path, app_env, engine_env)
