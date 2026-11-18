"""Owner tests of scripts/ops/post_deploy_smoke.py (HDE-EPIC043 WU-PR-06; HDE-COAG003.5).

The harness runs against the repository's own app, ``adapter.factory.create_app()``
under production posture (``APP_ENV=prod``), served on a loopback socket by a
server the test starts. That is the change's own system, not an emulation of the
hosted service. A deviating response used for a FAIL case stands for a response
the hosted edge or a deployment can return. Every test runs under closed rails;
the only socket is loopback. No test needs, accepts or contacts a database, and
none constructs a database provider.
"""
from __future__ import annotations

import hashlib
import http.client
import json
import subprocess
import threading
from contextlib import contextmanager
from pathlib import Path

import pytest
from werkzeug.serving import make_server

from engine.db.adapter import RETIRED_DB_TRANSPORT_KEYS
from engine.db.errors import PrimaryUnavailable
from engine.serializer.canon import sercanon
from scripts.ops import post_deploy_smoke as smoke

ROOT = Path(__file__).resolve().parents[2]
OPS_TASK_REF = "HDE-EPIC043-WU-OPS-01-ops-task-v1.0"
ALL_CHECKS = ("H-01", "H-02", "H-03", "H-04", "H-05", "H-06", "H-07", "H-08")

# Pinned DB introspection results, shaped like the current
# engine/db/providers/psycopg_provider.py return values (the real input of the
# comparison). Values: search_path verbatim from artifacts/db/introspect.search_path.json;
# columns, nullability and the unique clause from migrations/011_body_graphs_durability.sql;
# grants entries from artifacts/db/introspect.grants.json. They are not a recording of a
# live database. The constraint name is PostgreSQL's generated name for the unnamed
# unique clause; the comparison reads the definition, not the name.
PINNED_SEARCH_PATH = {"search_path": "hde, public", "status": "ok"}
_NOT_NULL = ("user_id", "vendor", "vendor_version", "input_fingerprint", "payload", "created_at")
PINNED_FINGERPRINT = {
    "schema": "hde",
    "version": 1,
    "objects": {
        "hde.body_graphs": {
            "columns": [
                {"name": name, "data_type": data_type, "nullable": name not in _NOT_NULL, "default": default}
                for name, data_type, default in (
                    ("user_id", "uuid", ""),
                    ("vendor", "text", ""),
                    ("vendor_version", "integer", ""),
                    ("input_fingerprint", "character", ""),
                    ("payload", "jsonb", ""),
                    ("created_at", "timestamp with time zone", "now()"),
                    ("refreshed_at", "timestamp with time zone", ""),
                    ("ttl_at", "timestamp with time zone", ""),
                )
            ],
            "constraints": [
                {
                    "name": "body_graphs_user_id_vendor_vendor_version_input_fingerprint_key",
                    "definition": "UNIQUE (user_id, vendor, vendor_version, input_fingerprint)",
                }
            ],
        },
        "hde.body_graphs_current": {"definition": "SELECT DISTINCT ON (user_id, vendor) user_id FROM hde.body_graphs"},
        "public.hde_body_graphs_current": {"definition": "SELECT user_id FROM hde.body_graphs_current"},
    },
}
PINNED_GRANTS = {
    "flags": {"rolcreatedb": True, "rolcreaterole": True, "rolsuper": True},
    "grants": json.loads((ROOT / "artifacts/db/introspect.grants.json").read_bytes())["grants"],
    "default_privileges": ["(none)"],
}


def _pinned(**overrides):
    live = {"search_path": PINNED_SEARCH_PATH, "fingerprint": PINNED_FINGERPRINT, "grants": PINNED_GRANTS}
    live.update(overrides)
    return lambda: live


def _references() -> dict[str, bytes]:
    references = {f"artifacts/db/{name}": (ROOT / "artifacts/db" / name).read_bytes() for name in smoke.DB_REFERENCE_FILES}
    references[smoke.DDL_SOURCE_REL] = (ROOT / smoke.DDL_SOURCE_REL).read_bytes()
    return references


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch):
    for name, value in {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "prod"}.items():
        monkeypatch.setenv(name, value)
    for name in ("DATABASE_URL", "HTTPS_PROXY", "https_proxy", "NO_PROXY", "no_proxy", *RETIRED_DB_TRANSPORT_KEYS):
        monkeypatch.delenv(name, raising=False)


@pytest.fixture(scope="module")
def real_app():
    with pytest.MonkeyPatch.context() as patch:
        patch.setenv("APP_ENV", "prod")
        patch.setenv("SAFE_MODE", "1")
        patch.setenv("ALLOW_NETWORK", "0")
        patch.delenv("DATABASE_URL", raising=False)
        from adapter.factory import create_app

        # Production posture is decided when the blueprint registers.
        yield create_app()


@contextmanager
def _serve(app):
    server = make_server("127.0.0.1", 0, app, threaded=False)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}"
    finally:
        server.shutdown()
        thread.join(timeout=10)


class _Deviate:
    """WSGI middleware that rewrites one response the way an edge or deployment can."""

    def __init__(self, app, mutate):
        self.app = app
        self.mutate = mutate
        self.calls = 0

    def __call__(self, environ, start_response):
        self.calls += 1
        captured = {}

        def capture(status, headers, exc_info=None):
            captured["status"] = status
            captured["headers"] = list(headers)
            return lambda data: None

        chunks = self.app(environ, capture)
        try:
            body = b"".join(chunks)
        finally:
            if hasattr(chunks, "close"):
                chunks.close()
        status, headers, body = self.mutate(environ, captured["status"], captured["headers"], body)
        start_response(status, headers)
        return [body]


def _unchanged(environ, status, headers, body):
    return status, headers, body


def _replace_header(headers, name, value):
    kept = [(key, val) for key, val in headers if key.lower() != name.lower()]
    return kept + ([(name, value)] if value is not None else [])


def _is(environ, method, path, *, query="", header=None):
    return (
        environ["REQUEST_METHOD"] == method
        and environ["PATH_INFO"] == path
        and environ.get("QUERY_STRING", "") == query
        and (header is None or header in environ)
        and (header is not None or not any(key in environ for key in ("HTTP_IF_NONE_MATCH", "HTTP_IF_MODIFIED_SINCE")))
    )


def _argv(base, evidence_dir, **overrides):
    values = {
        "--base-url": base,
        "--evidence-dir": str(evidence_dir),
        "--ops-task-ref": OPS_TASK_REF,
        "--target-app-env": "prod",
    }
    values.update(overrides)
    return [part for pair in values.items() for part in pair]


def _manifest(evidence_dir):
    return json.loads((evidence_dir / "retained_path_manifest.json").read_bytes())


def _check_results(evidence_dir):
    results = {}
    for entry in _manifest(evidence_dir)["entries"]:
        if entry["check"] is not None:
            results[entry["check"]] = entry["check_result"]
    return results


def _get(base, path, headers=None, method="GET", body=None):
    host, port = base.removeprefix("http://").split(":")
    conn = http.client.HTTPConnection(host, int(port), timeout=10)
    try:
        conn.request(method, path, body=body, headers=headers or {})
        response = conn.getresponse()
        return response.status, response.read()
    finally:
        conn.close()


# --- 1. each check, PASS and FAIL --------------------------------------------------


def test_full_run_passes_against_the_real_app_under_production_posture(real_app, tmp_path, capsys):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        rc = smoke.main(_argv(base, evidence), db_reader=_pinned())
    out = capsys.readouterr().out.splitlines()
    assert rc == smoke.EXIT_PASS
    assert sorted(path.name for path in evidence.iterdir()) == sorted(smoke.CAPTURE_FILES)
    assert out[:9] == [f"SMOKE_CHECK:{check}:PASS" for check in (*ALL_CHECKS, "H-09")]
    assert out[9:11] == ["SMOKE_RESULT:PASS", "SMOKE_FILES:12"]
    assert set(_check_results(evidence).values()) == {"PASS"}
    assert _manifest(evidence)["run_result"] == "PASS"


def _h02_etag(environ, status, headers, body):
    if _is(environ, "GET", "/internal/version"):
        headers = headers + [("ETag", '"abc"')]
    return status, headers, body


def _h02_cache_control(environ, status, headers, body):
    if _is(environ, "GET", "/internal/version"):
        headers = _replace_header(headers, "Cache-Control", "max-age=60")
    return status, headers, body


def _h02_sorted_body(environ, status, headers, body):
    if _is(environ, "GET", "/internal/version"):
        body = sercanon(json.loads(body))
        headers = _replace_header(headers, "Content-Length", str(len(body)))
    return status, headers, body


def _h02_duplicate_cache_control(environ, status, headers, body):
    if _is(environ, "GET", "/internal/version"):
        headers = headers + [("Cache-Control", "no-store")]
    return status, headers, body


def _h03_content_length(environ, status, headers, body):
    if _is(environ, "HEAD", "/internal/version"):
        length = dict((key.lower(), value) for key, value in headers)["content-length"]
        headers = _replace_header(headers, "Content-Length", str(int(length) - 1))
    return status, headers, body


def _h04_not_modified(environ, status, headers, body):
    if _is(environ, "GET", "/internal/version", header="HTTP_IF_NONE_MATCH"):
        return "304 NOT MODIFIED", [("Cache-Control", "no-store")], b""
    return status, headers, body


def _h06_no_store_removed(environ, status, headers, body):
    if _is(environ, "POST", "/api/reader", query="v=1"):
        headers = _replace_header(headers, "Cache-Control", None)
    return status, headers, body


def _h06_accepted(environ, status, headers, body):
    if _is(environ, "POST", "/api/reader", query="v=9"):
        return "200 OK", headers, body
    return status, headers, body


def _h07_served(environ, status, headers, body):
    if _is(environ, "GET", "/reader", query="v=1"):
        body = sercanon({"ok": True, "schema": "v1"})
        return "200 OK", _replace_header(headers, "Content-Length", str(len(body))), body
    return status, headers, body


def _h07_wrong_code(environ, status, headers, body):
    if _is(environ, "GET", "/reader", query="v=1"):
        body = sercanon({"code": "ERR_NOT_FOUND", "error": "not found", "ok": False, "schema": "v1"})
        return status, _replace_header(headers, "Content-Length", str(len(body))), body
    return status, headers, body


def _h02_no_response(environ, status, headers, body):
    if _is(environ, "GET", "/internal/version"):
        headers = _replace_header(headers, "Content-Length", str(len(body) + 50))
    return status, headers, body


@pytest.mark.parametrize(
    ("mutate", "failing"),
    [
        (_h02_etag, {"H-02", "H-05"}),
        (_h02_cache_control, {"H-02", "H-05"}),
        (_h02_sorted_body, {"H-02", "H-04", "H-05"}),
        (_h02_duplicate_cache_control, {"H-02", "H-05"}),
        (_h03_content_length, {"H-03"}),
        (_h04_not_modified, {"H-04"}),
        (_h06_no_store_removed, {"H-06"}),
        (_h06_accepted, {"H-06"}),
        (_h07_served, {"H-07"}),
        (_h07_wrong_code, {"H-07"}),
        (_h02_no_response, {"H-02", "H-03", "H-04", "H-05"}),
    ],
    ids=lambda value: getattr(value, "__name__", ""),
)
def test_each_deviation_fails_its_named_check(real_app, tmp_path, capsys, mutate, failing):
    evidence = tmp_path / "smoke"
    with _serve(_Deviate(real_app, mutate)) as base:
        rc = smoke.main(_argv(base, evidence), db_reader=_pinned())
    out = capsys.readouterr().out.splitlines()
    assert rc == smoke.EXIT_FAIL
    results = _check_results(evidence)
    assert {check for check, result in results.items() if result == "FAIL"} == failing
    assert {check for check, result in results.items() if result == "PASS"} == set(ALL_CHECKS) - failing
    assert "SMOKE_RESULT:FAIL" in out
    assert _manifest(evidence)["run_result"] == "FAIL"
    if mutate is _h02_no_response:
        text = (evidence / "headers_get.txt").read_text()
        assert "Status: NO_RESPONSE" in text and "Error: IncompleteRead" in text


# --- 2. canonical body and hash ------------------------------------------------------


def test_body_is_the_served_bytes_and_its_hash(real_app, tmp_path):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_PASS
        status, served = _get(base, "/internal/version", {"Accept-Encoding": "identity"})
    body = (evidence / "body_get.json").read_bytes()
    assert status == 200 and body == served
    assert (evidence / "body_get.sha256").read_bytes() == (hashlib.sha256(body).hexdigest() + "\n").encode()
    assert tuple(json.loads(body)) == smoke.INTERNAL_VERSION_KEYS


# --- 3. the refusal capture ---------------------------------------------------------


def test_refusal_capture_and_the_version_control(real_app, tmp_path):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_PASS
        status, body = _get(base, "/reader")
    lines = (evidence / "reader_refusal_get.txt").read_text().splitlines()
    assert lines[0] == "GET /reader?v=1"
    for line in ("status=403", "code=ERR_READER_FORBIDDEN", "cache_control=no-store", "etag_absent=true", "result=PASS"):
        assert line in lines
    # Without v=1 the product answers 400 before its refusal (S-4): a harness that
    # dropped the version would fail H-07.
    assert status == 400 and json.loads(body)["code"] == "ERR_READER_INVALID_VERSION"


# --- 4. the manifest ----------------------------------------------------------------


def test_manifest_maps_every_deliverable(real_app, tmp_path):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_PASS
    raw = (evidence / "retained_path_manifest.json").read_bytes()
    manifest = json.loads(raw)
    assert sercanon(manifest) == raw
    smoke.validate_manifest(manifest)
    entries = {entry["deliverable"]: entry for entry in manifest["entries"]}
    assert len(entries) == 14
    for name in smoke.WAIVED_PROOFS:
        entry = entries[name]
        assert entry["status"] == "NOT_CAPTURED_UNDER_C16" and entry["basis"] == "C-16"
        assert entry["retained_path"] is entry["sha256"] is entry["size_bytes"] is entry["check"] is None
        assert entry["check_result"] == "NOT_RUN"
        assert not (evidence / name).exists()
    refusal = entries[smoke.REFUSAL_DELIVERABLE]
    assert refusal["status"] == "EQUIVALENT_BY_MAPPING" and refusal["basis"] == "C-16"
    assert refusal["substitute_for"] == list(smoke.WAIVED_PROOFS)
    assert entries[smoke.DB_DELIVERABLE]["retained_path"] == "db_posture_spot_check.json"
    for entry in manifest["entries"]:
        if entry["retained_path"] is not None:
            data = (evidence / entry["retained_path"]).read_bytes()
            assert entry["sha256"] == hashlib.sha256(data).hexdigest() and entry["size_bytes"] == len(data)
    assert manifest["evidence_dir"] == "<outside-repository>"
    assert manifest["ops_task_ref"] == OPS_TASK_REF


@pytest.mark.parametrize("deviation", ["added_key", "removed_key", "unknown_status"])
def test_validate_manifest_refuses_a_deviating_shape(real_app, tmp_path, deviation):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_PASS
    manifest = _manifest(evidence)
    if deviation == "added_key":
        manifest["extra"] = True
    elif deviation == "removed_key":
        del manifest["nonclaims"]
    else:
        manifest["entries"][0]["status"] = "PARTIAL"
    with pytest.raises(ValueError):
        smoke.validate_manifest(manifest)


# --- 5. the DB comparison ------------------------------------------------------------


def _results(record):
    return {item["id"]: item["result"] for item in record["items"]}


def test_db_comparison_passes_over_the_pinned_results():
    record = smoke.compare_db_posture(PINNED_SEARCH_PATH, PINNED_FINGERPRINT, PINNED_GRANTS, _references())
    assert record["check_result"] == "PASS"
    assert _results(record) == {
        "DB-1": "PASS",
        "DB-2": "PASS",
        "DB-3": "PASS",
        "DB-4": "PASS",
        "DB-5": "NOT_COMPARABLE",
        "DB-6": "NOT_COMPARABLE",
        "DB-7": "NOT_COMPARABLE",
        "DB-8": "CAPTURED_BY_HASH",
    }
    assert record["grants_sha256"] == hashlib.sha256(sercanon(PINNED_GRANTS)).hexdigest()
    assert "SELECT" not in json.dumps(record)


def _fingerprint(mutate):
    fingerprint = json.loads(json.dumps(PINNED_FINGERPRINT))
    mutate(fingerprint["objects"])
    return fingerprint


@pytest.mark.parametrize(
    ("search_path", "fingerprint", "failing"),
    [
        ({"search_path": "public", "status": "ok"}, PINNED_FINGERPRINT, "DB-1"),
        (PINNED_SEARCH_PATH, _fingerprint(lambda objects: objects.pop("public.hde_body_graphs_current")), "DB-2"),
        (PINNED_SEARCH_PATH, _fingerprint(lambda objects: objects["hde.body_graphs"].update(constraints=[])), "DB-3"),
        (
            PINNED_SEARCH_PATH,
            _fingerprint(lambda objects: objects["hde.body_graphs"]["columns"][1].update(nullable=True)),
            "DB-4",
        ),
    ],
    ids=["search_path", "missing_view", "missing_unique", "nullable_not_null"],
)
def test_db_comparison_fails_on_each_live_difference(search_path, fingerprint, failing):
    record = smoke.compare_db_posture(search_path, fingerprint, PINNED_GRANTS, _references())
    results = _results(record)
    assert record["check_result"] == "FAIL"
    assert results[failing] == "FAIL"
    assert {item for item in ("DB-1", "DB-2", "DB-3", "DB-4") if results[item] == "FAIL"} == {failing}
    assert [results[item] for item in ("DB-5", "DB-6", "DB-7", "DB-8")] == ["NOT_COMPARABLE"] * 3 + ["CAPTURED_BY_HASH"]


def test_db_comparison_fails_closed_on_an_unrecognized_reference_line():
    references = _references()
    references["artifacts/db/check_constraints.txt"] += b"PASS something unexpected\n"
    record = smoke.compare_db_posture(PINNED_SEARCH_PATH, PINNED_FINGERPRINT, PINNED_GRANTS, references)
    results = _results(record)
    assert record["check_result"] == "FAIL"
    assert results["DB-3"] == results["DB-4"] == "FAIL"


def test_db_check_refuses_without_a_database_url_and_constructs_nothing(real_app, tmp_path, monkeypatch, capsys):
    def forbidden(*args, **kwargs):
        raise AssertionError("a database provider was constructed")

    monkeypatch.setattr(smoke.DBAccess, "for_current_env", forbidden)
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        rc = smoke.main(_argv(base, evidence))
    record = json.loads((evidence / "db_posture_spot_check.json").read_bytes())
    assert rc == smoke.EXIT_FAIL
    assert record["check_result"] == "REFUSED" and record["refusal"] == "DATABASE_URL_UNSET"
    assert record["database_url"] == "UNSET" and record["items"] == []
    assert "SMOKE_CHECK:H-08:REFUSED" in capsys.readouterr().out
    assert "DATABASE_URL=UNSET" in (evidence / "env_pins.txt").read_text()


def test_db_check_records_an_unreachable_database_by_code_only(real_app, tmp_path, monkeypatch):
    def unreachable(*args, **kwargs):
        raise PrimaryUnavailable("connection refused at db.internal", code="primary_connect_failed")

    monkeypatch.setattr(smoke.DBAccess, "for_current_env", unreachable)
    monkeypatch.setenv("DATABASE_URL", "set-for-the-presence-check-only")
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence)) == smoke.EXIT_FAIL
    raw = (evidence / "db_posture_spot_check.json").read_bytes()
    record = json.loads(raw)
    assert record["check_result"] == "FAIL" and record["error_code"] == "primary_connect_failed"
    assert record["database_url"] == "SET"
    assert b"db.internal" not in raw and b"set-for-the-presence" not in raw


# --- 6. preconditions ----------------------------------------------------------------


def _precondition(monkeypatch, tmp_path, token):
    """Apply one failing precondition; return argv overrides and the evidence directory."""
    evidence = tmp_path / "smoke"
    overrides = {}
    if token == "LOCALE_PINS":
        monkeypatch.setenv("LC_ALL", "en_US.UTF-8")
    elif token.startswith("BASE_URL_FORM:"):
        overrides["--base-url"] = token.split(":", 1)[1]
    elif token == "EVIDENCE_DIR_NOT_A_DIRECTORY":
        evidence.write_text("x")
    elif token == "EVIDENCE_DIR_NOT_EMPTY":
        evidence.mkdir()
        (evidence / "earlier.txt").write_text("x")
    elif token.startswith("EVIDENCE_DIR_PROTECTED:"):
        evidence = ROOT / token.split(":", 1)[1]
    elif token == "RETIRED_DB_TRANSPORT_KEYS":
        monkeypatch.setenv(RETIRED_DB_TRANSPORT_KEYS[0], "")
    elif token == "RAILS_POSTURE_UNSET":
        monkeypatch.delenv("SAFE_MODE")
    elif token == "OPS_TASK_REF_INVALID":
        overrides["--ops-task-ref"] = "no spaces allowed"
    elif token == "TARGET_APP_ENV_UNSUPPORTED":
        overrides["--target-app-env"] = "dev"
    elif token == "PROXY_FORM":
        overrides["--base-url"] = "https://glow-hdengine-v2-production.up.railway.app"
        monkeypatch.setenv("HTTPS_PROXY", "http://user:secret@127.0.0.1:9")
    elif token == "CATALOG_ROUTE":
        catalog = json.loads((ROOT / "docs/ENDPOINTS_CATALOG.json").read_bytes())
        catalog["success_endpoints"] = []
        path = tmp_path / "catalog.json"
        path.write_bytes(sercanon(catalog))
        monkeypatch.setattr(smoke, "CATALOG_PATH", path)
    elif token == "REFERENCE_INPUT_MISSING":
        monkeypatch.setattr(smoke, "DB_REFERENCE_DIR", tmp_path / "no-db-references")
    return overrides, evidence


PRECONDITIONS = [
    "LOCALE_PINS",
    "BASE_URL_FORM:https://user:pw@glow-hdengine-v2-production.up.railway.app",
    "BASE_URL_FORM:https://glow-hdengine-v2-production.up.railway.app/?q=1",
    "BASE_URL_FORM:https://glow-hdengine-v2-production.up.railway.app/internal",
    "BASE_URL_FORM:http://glow-hdengine-v2-production.up.railway.app",
    "BASE_URL_FORM:http://localhost:8000",
    "EVIDENCE_DIR_NOT_A_DIRECTORY",
    "EVIDENCE_DIR_NOT_EMPTY",
    "EVIDENCE_DIR_PROTECTED:artifacts/proofs",
    "EVIDENCE_DIR_PROTECTED:artifacts/ops/internal_version",
    "EVIDENCE_DIR_PROTECTED:artifacts/db",
    "EVIDENCE_DIR_PROTECTED:artifacts/db/smoke",
    "RETIRED_DB_TRANSPORT_KEYS",
    "RAILS_POSTURE_UNSET",
    "OPS_TASK_REF_INVALID",
    "TARGET_APP_ENV_UNSUPPORTED",
    "PROXY_FORM",
    "CATALOG_ROUTE",
    "REFERENCE_INPUT_MISSING",
]


@pytest.mark.parametrize("token", PRECONDITIONS)
def test_each_precondition_refuses_before_any_request_or_write(real_app, tmp_path, monkeypatch, capsys, token):
    counter = _Deviate(real_app, _unchanged)
    with _serve(counter) as base:
        overrides, evidence = _precondition(monkeypatch, tmp_path, token)
        before = sorted(evidence.iterdir()) if evidence.is_dir() else None
        rc = smoke.main(_argv(base, evidence, **overrides), db_reader=_pinned())
    captured = capsys.readouterr()
    assert rc == smoke.EXIT_REFUSED
    assert captured.err.splitlines() == ["OPS_REFUSED:" + token.split(":", 1)[0]]
    assert captured.out == ""
    assert counter.calls == 0
    if before is None:
        assert not evidence.is_dir()
    else:
        assert sorted(evidence.iterdir()) == before


# --- 7. secret safety ------------------------------------------------------------------


def _bearer_in_body(environ, status, headers, body):
    if environ["PATH_INFO"] == "/internal/version" and environ["REQUEST_METHOD"] == "GET":
        obj = json.loads(body)
        obj["engine_tag"] = "Bearer placeholder-not-a-real-credential-0123456789"
        body = sercanon(obj, sort_keys=False)
        headers = _replace_header(headers, "Content-Length", str(len(body)))
    return status, headers, body


def test_a_credential_in_a_served_body_refuses_and_writes_nothing(real_app, tmp_path, capsys):
    evidence = tmp_path / "smoke"
    with _serve(_Deviate(real_app, _bearer_in_body)) as base:
        rc = smoke.main(_argv(base, evidence), db_reader=_pinned())
    captured = capsys.readouterr()
    assert rc == smoke.EXIT_UNSAFE
    assert captured.err.splitlines() == ["OPS_REFUSED:RETAINED_TEXT_UNSAFE"]
    assert "placeholder" not in captured.out + captured.err
    assert not evidence.exists()


def test_a_clean_run_scans_clean_and_logs_keys_only(real_app, tmp_path, capsys):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        rc = smoke.main(_argv(base, evidence), db_reader=_pinned())
        port = base.rsplit(":", 1)[1]
    captured = capsys.readouterr()
    assert rc == smoke.EXIT_PASS
    for name in smoke.CAPTURE_FILES:
        assert smoke.validate_retained_text_safety(Path(name), (evidence / name).read_bytes()) == ()
    release_id = json.loads((evidence / "body_get.json").read_bytes())["release_id"]
    logs = captured.out + captured.err
    for value in ("no-store", "application/json", release_id, port, "engine_tag"):
        assert value not in logs
    assert all(line.startswith("SMOKE_") for line in captured.out.splitlines())


# --- 8. no write, no overwrite -----------------------------------------------------------


def _local_evidence_state():
    state = {}
    for rel in smoke.PROTECTED_DIRS:
        for path in sorted((ROOT / rel).rglob("*")):
            if path.is_file():
                state[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    status = subprocess.run(
        ("git", "status", "--porcelain", "--untracked-files=all"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    return state, status


def test_a_full_run_leaves_the_local_evidence_and_the_tree_unchanged(real_app, tmp_path):
    before = _local_evidence_state()
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_PASS
    assert _local_evidence_state() == before
    for name in smoke.WAIVED_PROOFS:
        assert not (evidence / name).exists()


def test_a_second_run_never_overwrites(real_app, tmp_path, capsys):
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_PASS
        first = {path.name: path.read_bytes() for path in evidence.iterdir()}
        capsys.readouterr()
        assert smoke.main(_argv(base, evidence), db_reader=_pinned()) == smoke.EXIT_REFUSED
    assert capsys.readouterr().err.splitlines() == ["OPS_REFUSED:EVIDENCE_DIR_NOT_EMPTY"]
    assert {path.name: path.read_bytes() for path in evidence.iterdir()} == first


def test_a_write_failure_removes_the_files_this_run_created(real_app, tmp_path, monkeypatch, capsys):
    real_create = smoke._create_file
    calls = []

    def failing_create(path, data):
        calls.append(path.name)
        if len(calls) == 5:
            raise OSError("disk full")
        real_create(path, data)

    monkeypatch.setattr(smoke, "_create_file", failing_create)
    evidence = tmp_path / "smoke"
    with _serve(real_app) as base:
        rc = smoke.main(_argv(base, evidence), db_reader=_pinned())
    assert rc == smoke.EXIT_WRITE_FAILED
    assert capsys.readouterr().err.splitlines() == ["OPS_REFUSED:EVIDENCE_WRITE_FAILED"]
    assert len(calls) == 5
    assert not evidence.exists()


# --- 9. no valid Reader request ------------------------------------------------------------


def test_the_probe_set_is_closed():
    assert [(probe.id, probe.check, probe.method, probe.target, probe.body) for probe in smoke.PROBES] == [
        ("P-1", "H-02", "GET", "/internal/version", None),
        ("P-2", "H-03", "HEAD", "/internal/version", None),
        ("P-3", "H-04", "GET", "/internal/version", None),
        ("P-4", "H-04", "GET", "/internal/version", None),
        ("P-5", "H-06", "POST", "/api/reader?v=1", b"{"),
        ("P-6", "H-06", "POST", "/api/reader?v=9", b"{}"),
        ("P-7", "H-07", "GET", "/reader?v=1", None),
    ]
    for probe in smoke.PROBES:
        assert {name.lower() for name, _ in probe.headers} <= {
            "accept-encoding",
            "content-type",
            "if-none-match",
            "if-modified-since",
        }


def test_no_probe_is_a_valid_reader_request(real_app, monkeypatch):
    def forbidden(*args, **kwargs):
        raise AssertionError("a probe reached the database")

    monkeypatch.setattr(smoke.DBAccess, "for_current_env", forbidden)
    expected = {"P-5": (422, "ERR_READER_INVALID_INPUT"), "P-6": (400, "ERR_READER_INVALID_VERSION"), "P-7": (403, "ERR_READER_FORBIDDEN")}
    with _serve(real_app) as base:
        target = smoke._connection_target(base, {})
        for probe in smoke.PROBES:
            if probe.id in expected:
                response = smoke._send(target, probe)
                assert (response.status, json.loads(response.body)["code"]) == expected[probe.id]


# --- 10. connection target and proxy --------------------------------------------------------


def test_connection_target_and_proxy_selection():
    host = "glow-hdengine-v2-production.up.railway.app"
    assert smoke._connection_target("http://127.0.0.1:8000", {"HTTPS_PROXY": "http://127.0.0.1:9"}) == smoke.Target(
        "http", "127.0.0.1", 8000, None
    )
    assert smoke._connection_target(f"https://{host}", {}) == smoke.Target("https", host, 443, None)
    assert smoke._connection_target(f"https://{host}/", {"HTTPS_PROXY": "http://127.0.0.1:46383"}) == smoke.Target(
        "https", host, 443, ("127.0.0.1", 46383)
    )
    assert smoke._connection_target(
        f"https://{host}", {"https_proxy": "http://127.0.0.1:46383", "NO_PROXY": ".railway.app"}
    ) == smoke.Target("https", host, 443, None)
    for proxy in ("http://user:pw@127.0.0.1:9", "https://127.0.0.1:9", "http://127.0.0.1:9/?x=1"):
        with pytest.raises(smoke.Refusal) as refusal:
            smoke._connection_target(f"https://{host}", {"HTTPS_PROXY": proxy})
        assert refusal.value.token == "PROXY_FORM"
