import json
import runpy
import warnings
from pathlib import Path

import flask
import pytest

from adapter import http_reader
from engine.cli.main import cli
from engine.serializer.canon import sercanon
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-a7-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-a7-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def _client():
    app = http_reader.create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _reader_query_params() -> dict[str, str]:
    alice = Path("fixtures/charts/alice.json").resolve()
    bob = Path("fixtures/charts/bob.json").resolve()
    return {"v": "1", "a": str(alice), "b": str(bob), "a_tz": "UTC", "b_tz": "UTC"}


def _assert_canonical_lf_bytes(raw: bytes) -> None:
    assert raw.endswith(b"\n")
    assert not raw.endswith(b"\n\n")
    assert b"\r" not in raw
    assert sercanon(json.loads(raw)) == raw


def test_showcompat_dump_reader_matches_http_reader_for_same_normalized_pair(tmp_path: Path, monkeypatch, capsys):
    pair_path = tmp_path / "pair.json"
    pair_path.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}, sort_keys=True) + "\n", encoding="utf-8")
    cli_reader_path = tmp_path / "reader.json"
    admin_dir = tmp_path / "admin"

    exit_code = cli(["showcompat", "--pair-file", str(pair_path), "--dump-reader", str(cli_reader_path), "--dump-admin-dir", str(admin_dir)])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    assert captured.err == ""
    cli_reader = cli_reader_path.read_bytes()
    _assert_canonical_lf_bytes(cli_reader)

    # The CLI's governed admin sidecars are its normalized chart pair. Point the
    # HTTP path guard at only that private directory, then ask /reader to emit
    # the same pair through the current HTTP adapter.
    left_chart = admin_dir / "pair.left.bodygraph.json"
    right_chart = admin_dir / "pair.right.bodygraph.json"
    assert left_chart.is_file() and right_chart.is_file()
    monkeypatch.setattr(http_reader, "ALLOWED_ROOT", admin_dir.resolve())

    response = _client().get(
        "/reader",
        query_string={"v": "1", "a": str(left_chart), "b": str(right_chart), "a_tz": "UTC", "b_tz": "UTC"},
        headers={"Accept-Encoding": "identity"},
    )
    assert response.status_code == 200, response.data
    _assert_canonical_lf_bytes(response.data)
    assert response.data == cli_reader


@pytest.mark.epic025
def test_reader_a7_transport_invariants(monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    client = _client()
    params = _reader_query_params()

    get_resp_identity = client.get("/reader", query_string=params, headers={"Accept-Encoding": "identity"})
    get_resp_gzip = client.get("/reader", query_string=params, headers={"Accept-Encoding": "gzip"})

    assert get_resp_identity.status_code == 200, get_resp_identity.data
    assert get_resp_gzip.status_code == 200
    assert get_resp_identity.data.endswith(b"\n")
    assert get_resp_identity.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert get_resp_identity.headers.get("Cache-Control") == "private, max-age=0, must-revalidate"
    assert get_resp_identity.headers.get("Vary") == "Authorization, Accept-Encoding"
    assert get_resp_identity.headers.get("Content-Length") == str(len(get_resp_identity.data))
    payload = get_resp_identity.get_json()
    assert list(payload.keys()) == ["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]
    etag = get_resp_identity.headers.get("ETag")
    assert isinstance(etag, str)
    assert etag.startswith('"') and etag.endswith('"')
    assert not etag.startswith("W/")
    assert get_resp_gzip.headers.get("ETag") == etag
    assert get_resp_gzip.headers.get("Content-Length") == str(len(get_resp_gzip.data))

    head_resp = client.head("/reader", query_string=params)
    assert head_resp.status_code == 200
    assert head_resp.data == b""
    assert head_resp.headers.get("Content-Type") == get_resp_identity.headers.get("Content-Type")
    assert head_resp.headers.get("Cache-Control") == get_resp_identity.headers.get("Cache-Control")
    assert head_resp.headers.get("Vary") == get_resp_identity.headers.get("Vary")
    assert head_resp.headers.get("ETag") == etag
    assert head_resp.headers.get("Content-Length") == str(len(get_resp_identity.data))

    cond_resp = client.get("/reader", query_string=params, headers={"If-None-Match": etag})
    assert cond_resp.status_code == 304
    assert cond_resp.data == b""
    assert "Content-Type" not in cond_resp.headers
    assert "Content-Length" not in cond_resp.headers
    assert cond_resp.headers.get("ETag") == etag
    assert cond_resp.headers.get("Vary") == get_resp_identity.headers.get("Vary")

    # PF05 §5.4: the production Reader is served only under /api; the unprefixed
    # POST /reader is the governed 405 (no ETag, no-store).
    post_resp = client.post("/reader", query_string=params)
    assert post_resp.status_code == 405
    assert post_resp.get_json()["code"] == "ERR_NOT_FOUND"
    assert post_resp.headers.get("Allow") == "GET, HEAD"
    assert "ETag" not in post_resp.headers
    assert post_resp.headers.get("Cache-Control") == "no-store"

    # PF05 §5.3: POST is non-conditional; query-only input is not a Reader request.
    api_post = client.post("/api/reader", query_string=params)
    assert api_post.status_code == 422
    assert api_post.get_json()["code"] == "ERR_READER_INVALID_INPUT"
    assert "ETag" not in api_post.headers
    assert api_post.headers.get("Cache-Control") == "no-store"
    conditional_post = client.post("/api/reader", query_string=params, headers={"If-None-Match": etag})
    assert conditional_post.status_code == 422
    assert conditional_post.data == api_post.data


@pytest.mark.parametrize("app_env", ["dev"])
def test_dev_reader_is_served_only_for_explicit_dev(monkeypatch, app_env):
    # HDE-CRD-0002 S10 / IF-10 (PF05 §5.4, §5.6): only APP_ENV exactly "dev" serves (AD-2).
    monkeypatch.setenv("APP_ENV", app_env)
    client = _client()
    params = _reader_query_params()
    assert client.get("/reader", query_string=params).status_code == 200
    head = client.head("/reader", query_string=params)
    assert head.status_code == 200 and head.data == b""


@pytest.mark.parametrize(
    "app_env",
    [None, "", "  ", " dev", "dev ", " DEV ", "Dev", "DEV", "test", "local", "prod", "production", "live", "staging", "development", "dev1"],
)
def test_dev_reader_refuses_every_other_environment(monkeypatch, app_env):
    # Unset, empty and every value other than exactly "dev" -- including padded
    # and case variants (AD-2) -- refuse with ERR_READER_FORBIDDEN 403, the
    # governed error headers, and no ETag; HEAD carries no body.
    if app_env is None:
        monkeypatch.delenv("APP_ENV", raising=False)
    else:
        monkeypatch.setenv("APP_ENV", app_env)
    client = _client()
    params = _reader_query_params()
    resp = client.get("/reader", query_string=params)
    assert resp.status_code == 403
    assert json.loads(resp.data)["code"] == "ERR_READER_FORBIDDEN"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert "ETag" not in resp.headers
    head = client.head("/reader", query_string=params)
    assert head.status_code == 403 and head.data == b""
    # Version validation still precedes the environment gate.
    assert json.loads(client.get("/reader", query_string={"v": "2"}).data)["code"] == "ERR_READER_INVALID_VERSION"


# --- HDE-CRD-0002 AD-3: the canonical dev runner meets the required local capture profile ---
# (PF05 §5.4 "Gate"; PF14 §34 "Required local capture profile"; Conjunction checklist HDE-CONJ001.1)


@pytest.mark.parametrize(("port_env", "port"), [(None, 8000), ("8123", 8123)])
def test_dev_runner_binds_loopback_with_debugger_and_reloader_off(monkeypatch, port_env, port):
    calls = []
    monkeypatch.setattr(flask.Flask, "run", lambda app, **kwargs: calls.append((app, kwargs)))
    monkeypatch.setenv("APP_ENV", "dev")
    if port_env is None:
        monkeypatch.delenv("PORT", raising=False)
    else:
        monkeypatch.setenv("PORT", port_env)
    with warnings.catch_warnings():
        # runpy warns when the module is already imported; it re-executes it as __main__.
        warnings.filterwarnings("ignore", message=".*found in sys.modules.*", category=RuntimeWarning)
        runpy.run_module(http_reader.__name__, run_name="__main__")
    assert len(calls) == 1
    app, kwargs = calls[0]
    assert kwargs == {"host": "127.0.0.1", "port": port, "debug": False, "use_debugger": False, "use_reloader": False}
    assert "/reader" in {rule.rule for rule in app.url_map.iter_rules()}


_CORS_ORIGIN = {"Origin": "https://cross-origin.invalid"}


@pytest.mark.parametrize(
    ("app_env", "method", "path", "query", "headers", "status"),
    [
        ("dev", "GET", "/reader", "reader", _CORS_ORIGIN, 200),
        ("dev", "HEAD", "/reader", "reader", _CORS_ORIGIN, 200),
        ("dev", "OPTIONS", "/reader", None, {**_CORS_ORIGIN, "Access-Control-Request-Method": "GET"}, 200),
        ("prod", "GET", "/reader", "reader", _CORS_ORIGIN, 403),
        ("dev", "GET", "/reader", {"v": "2"}, _CORS_ORIGIN, 400),
        ("dev", "GET", "/no-such-route", None, _CORS_ORIGIN, 404),
    ],
)
def test_dev_runner_emits_no_cors_headers(monkeypatch, app_env, method, path, query, headers, status):
    # No cross-origin allow-list, wildcard, credentials or CORS response header (PF14 §34).
    monkeypatch.setenv("APP_ENV", app_env)
    query_string = _reader_query_params() if query == "reader" else query
    resp = _client().open(path, method=method, query_string=query_string, headers=headers)
    assert resp.status_code == status
    assert [name for name in resp.headers.keys() if name.lower().startswith("access-control-")] == []
