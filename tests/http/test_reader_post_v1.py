"""PF05 §5.1.0 / §5.3 production Reader POST (mounted under ``/api``, PF05 §5.4; HDE-EPIC040-PR06a)
and the dev GET fixture route (HDE-EPIC040-PR04)."""
from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path

import pytest

from adapter import http_reader
from engine.compat import compute
from engine.config.registry_loader import SchemaValidationError
from engine.db.errors import PrimaryUnavailable, SqlExecError
from engine.runtime.identity import identity_meta
from engine.serializer.canon import sercanon
from tests.support.pr04_fixtures import (
    GATES_A,
    GATES_B,
    UUID_A,
    UUID_B,
    UUID_C,
    UUID_MIXED,
    FakeCurrentViewDB,
    build_bundle,
    build_pack,
    complete_chart,
    inject_seams,
)

SIX_KEYS = ["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]
FORBIDDEN = ("score", "signals", "pair_key", "gates", "shared_key", "personal", "config_id", "keys", "q\"", UUID_A, UUID_B, "bodygraph")


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-reader-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-reader-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor client constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("ingest attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))


@pytest.fixture
def db(monkeypatch):
    fake = FakeCurrentViewDB({UUID_A: complete_chart(UUID_A, GATES_A), UUID_B: complete_chart(UUID_B, GATES_B)})
    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: fake))
    return fake


def _client():
    app = http_reader.create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _post(client, body=None, *, raw: bytes | None = None, query="v=1", headers=None):
    data = raw if raw is not None else (json.dumps(body, sort_keys=True).encode("utf-8") if body is not None else None)
    return client.post(f"/api/reader?{query}" if query else "/api/reader", data=data, headers=headers or {"Content-Type": "application/json; charset=utf-8"})


def _assert_error(resp, token, status, db=None):
    assert resp.status_code == status, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert body == {"schema": "v1", "ok": False, "code": token, "error": body["error"]}
    assert set(body) == {"schema", "ok", "code", "error"}
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    assert resp.data.endswith(b"\n")
    if db is not None:
        assert db.queries == []


# --- request grammar ---------------------------------------------------------------------

def test_missing_version_is_the_existing_version_error(db):
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}, query=""), "ERR_READER_INVALID_VERSION", 400, db)


@pytest.mark.parametrize("query", ["v=1&v=1", "v=1&v=2", "v=", "v=01"])
def test_duplicated_or_malformed_version_is_refused_before_any_lookup(db, query):
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}, query=query), "ERR_READER_INVALID_VERSION", 400, db)


def test_unprefixed_post_reader_is_the_governed_405(db):
    """PF05 §5.4 / PF10 §2.16 §4: no production handler is served outside the ``/api`` prefix."""
    resp = _client().post("/reader?v=1", data=json.dumps({"a_id": UUID_A, "b_id": UUID_B}), headers={"Content-Type": "application/json; charset=utf-8"})
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "GET, HEAD"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    assert json.loads(resp.data) == {"schema": "v1", "ok": False, "code": "ERR_NOT_FOUND", "error": "not found"}
    assert db.queries == []


@pytest.mark.parametrize(
    "raw",
    [
        b"",
        b"{bad",
        b"[]",
        b'"' + UUID_A.encode() + b'"',
        json.dumps({"a_id": UUID_A}).encode(),
        json.dumps({"a_id": UUID_A, "b_id": UUID_B, "viewer_prefs": {}}).encode(),
        json.dumps({"a_id": UUID_A, "b_id": UUID_B, "gates": ["1"]}).encode(),
        json.dumps({"a_id": UUID_MIXED.upper(), "b_id": UUID_B}).encode(),
        json.dumps({"a_id": "{" + UUID_A + "}", "b_id": UUID_B}).encode(),
        json.dumps({"a_id": UUID_A.replace("-", ""), "b_id": UUID_B}).encode(),
        json.dumps({"a_id": "alice", "b_id": UUID_B}).encode(),
        json.dumps({"a_id": "", "b_id": UUID_B}).encode(),
        json.dumps({"a_id": None, "b_id": UUID_B}).encode(),
        json.dumps({"a": {"person_uid": UUID_A}, "b": {"person_uid": UUID_B}}).encode(),
        b"\xef\xbb\xbf" + json.dumps({"a_id": UUID_A, "b_id": UUID_B}).encode(),
        b"\xff\xfe",
        b"{\"a_id\": \"" + UUID_A.encode() + b"\", \"b_id\": \"" + UUID_B.encode() + b"\", \"pad\": \"" + b"x" * 40_000 + b"\"}",
    ],
)
def test_invalid_input_is_422_no_store_and_performs_no_lookup(db, raw):
    _assert_error(_post(_client(), raw=raw), "ERR_READER_INVALID_INPUT", 422, db)


def test_body_without_content_length_is_bounded_before_buffering(db):
    """A chunked / Content-Length-less body must not be buffered past the limit.

    Without Content-Length the preliminary size check cannot fire, so the read
    itself is what bounds memory: this production route must never buffer an
    unbounded unauthenticated stream.
    """

    oversized = (
        b'{"a_id":"' + UUID_A.encode() + b'","b_id":"' + UUID_B.encode()
        + b'","pad":"' + b"x" * 5_000_000 + b'"}'
    )
    stream = io.BytesIO(oversized)
    resp = _client().post(
        "/api/reader?v=1",
        headers={"Content-Type": "application/json; charset=utf-8"},
        environ_overrides={"wsgi.input": stream, "wsgi.input_terminated": True, "CONTENT_LENGTH": ""},
    )
    _assert_error(resp, "ERR_READER_INVALID_INPUT", 422, db)
    assert stream.tell() <= http_reader._READER_MAX_BODY_BYTES + 1
    assert stream.tell() < len(oversized)


def test_alias_bridge_is_unreachable_from_the_public_reader(db, monkeypatch):
    monkeypatch.setattr("engine.bodygraph.resolver.resolve_db_user_id", lambda *_: pytest.fail("alias bridge reached"))
    _assert_error(_post(_client(), {"a_id": "epic011-s10-invariance-1", "b_id": UUID_B}), "ERR_READER_INVALID_INPUT", 422, db)


# --- resolution failures ------------------------------------------------------------------

def test_unknown_person_is_404_without_revealing_which_identifier(db):
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_C})
    _assert_error(resp, "ERR_M10_PERSON_UNRESOLVED", 404)
    assert UUID_C not in resp.data.decode("utf-8") and UUID_A not in resp.data.decode("utf-8")
    assert json.loads(resp.data)["error"] == "BodyGraph not found"


def test_db_unavailable_and_query_failures_are_503(monkeypatch):
    def _unavailable(cls, *a, **k):
        raise PrimaryUnavailable(code="missing_database_url")

    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(_unavailable))
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}), "ERR_M10_RESOLVER_UNAVAILABLE", 503)
    failing = FakeCurrentViewDB({}, fail=SqlExecError(code="fixture_query"))
    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: failing))
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}), "ERR_M10_RESOLVER_UNAVAILABLE", 503)


def test_row_contract_violations_are_503(monkeypatch):
    class _Ambiguous(FakeCurrentViewDB):
        def query(self, sql, params=None):
            rows = super().query(sql, params)
            return rows * 2

    ambiguous = _Ambiguous({UUID_A: complete_chart(UUID_A, GATES_A), UUID_B: complete_chart(UUID_B, GATES_B)})
    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: ambiguous))
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}), "ERR_M10_RESOLVER_UNAVAILABLE", 503)


@pytest.mark.parametrize(
    ("mutate", "token", "status"),
    [
        (lambda c: c["bodygraph"].pop("profile"), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].update(gates=[]), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].pop("gates"), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        # PF05 §5.2.3: every stored-row Gate defect -- duplicate, malformed,
        # noncanonical or outside 1..64 -- is ERR_M10_BODYGRAPH_INCOMPLETE/503, the
        # same as the other stored-row defects here. 422 would blame the client for
        # a chart the server stored.
        (lambda c: c["bodygraph"].update(gates=["10", "10"]), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].update(gates=[10, "10"]), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].update(gates=[True]), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].update(gates=["010"]), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].update(gates=[65]), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c.update(person_uid=UUID_C, person={"person_uid": UUID_C}), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
        (lambda c: c["bodygraph"].update(headers={"x": 1}), "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    ],
)
def test_stored_row_defects_refuse_without_partial_score(db, monkeypatch, mutate, token, status):
    mutate(db.charts[UUID_A])
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached"))
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}), token, status)


def test_admission_refusal_is_503_schema_mismatch(db, monkeypatch):
    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    # The repository root is admitted (PF10 §2.15 interval ended); the refusal branch is reached through the seam.
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}), "ERR_M10_MANIFEST_MISMATCH", 503)


def test_real_admission_owner_serves_the_admitted_release(db, monkeypatch):
    """With the unchanged admission owner (no injected bundle) the real root admits and the
    Reader answers 200 with the admitted release identity."""
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_B})
    assert resp.status_code == 200, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert list(body) == SIX_KEYS
    assert body["release_id"] == identity_meta()["release_id"]
    assert body["release_id"] == hashlib.sha256(Path("catalog/manifest.json").read_bytes()).hexdigest()


# --- success ------------------------------------------------------------------------------

def test_success_envelope_headers_and_ab_ba_identity(db, bundle):
    client = _client()
    ab = _post(client, {"a_id": UUID_A, "b_id": UUID_B})
    ba = _post(client, {"a_id": UUID_B, "b_id": UUID_A})
    again = _post(client, {"a_id": UUID_A, "b_id": UUID_B})
    assert ab.status_code == 200, ab.data
    assert ab.data == ba.data == again.data
    body = json.loads(ab.data.decode("utf-8"))
    assert list(body) == SIX_KEYS
    assert body["reader_version"] == "v1" and body["eligible"] is True
    assert body["categories"] == [{"band": body["categories"][0]["band"], "id": "harmony"}]
    assert body["categories"][0]["band"] in {"Cool", "Open", "Warm", "Glow"}
    assert body["meta"] == {"engine_tag": identity_meta()["engine_tag"], "invocation_tag": identity_meta()["invocation_tag"]}
    assert body["release_id"] == bundle.release_id
    assert sercanon(body) == ab.data
    assert ab.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert ab.headers.get("Cache-Control") == "private, max-age=0, must-revalidate"
    assert ab.headers.get("Vary") == "Authorization, Accept-Encoding"
    assert ab.headers.get("Content-Length") == str(len(ab.data))
    assert "ETag" not in ab.headers
    text = ab.data.decode("utf-8")
    for forbidden in FORBIDDEN:
        assert forbidden not in text, forbidden


def test_post_is_non_conditional(db):
    client = _client()
    first = _post(client, {"a_id": UUID_A, "b_id": UUID_B})
    import hashlib

    etag = '"' + hashlib.sha256(first.data).hexdigest() + '"'
    conditional = client.post(
        "/api/reader?v=1",
        data=json.dumps({"a_id": UUID_A, "b_id": UUID_B}),
        headers={"Content-Type": "application/json; charset=utf-8", "If-None-Match": etag},
    )
    assert conditional.status_code == 200
    assert conditional.data == first.data
    assert "ETag" not in conditional.headers


def test_lookup_is_parameterized_read_only_current_rows(db):
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_B})
    assert resp.status_code == 200
    assert [params for _sql, params in db.queries] == [(UUID_A,), (UUID_B,)]
    for sql, _params in db.queries:
        assert sql == http_reader.read_current_mapped_bodygraph.__globals__["CURRENT_ROW_SQL"]
        assert "public.hde_body_graphs_current" in sql and "vendor = 'hdapi'" in sql and sql.count("%s") == 1
        assert not any(verb in sql.upper() for verb in ("INSERT", "UPDATE", "DELETE", "CALL"))
    assert db.writes == []


def test_same_uuid_twice_with_equal_rows_is_ineligible(db, monkeypatch, bundle):
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached for a self-pair"))
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_A})
    assert resp.status_code == 200
    body = json.loads(resp.data.decode("utf-8"))
    assert body["eligible"] is False and body["categories"] == []
    assert list(body) == SIX_KEYS
    assert body["release_id"] == identity_meta()["release_id"]
    assert [params for _sql, params in db.queries] == [(UUID_A,)]


def test_production_app_env_serves_post_and_forbids_dev_get(db, monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    client = _client()
    assert _post(client, {"a_id": UUID_A, "b_id": UUID_B}).status_code == 200
    assert client.get("/reader?v=1&a=x&b=y").status_code == 403


# --- dev GET fixture route regression ---------------------------------------------------------

def _fixture_params(**overrides):
    params = {
        "v": "1",
        "a": str(Path("fixtures/charts/alice.json").resolve()),
        "b": str(Path("fixtures/charts/bob.json").resolve()),
        "a_tz": "UTC",
        "b_tz": "UTC",
    }
    params.update(overrides)
    return params


def test_dev_get_route_resolves_complete_fixtures_and_keeps_tz_and_conditional_contract():
    client = _client()
    ok = client.get("/reader", query_string=_fixture_params(), headers={"Accept-Encoding": "identity"})
    assert ok.status_code == 200, ok.data
    body = json.loads(ok.data)
    assert list(body) == SIX_KEYS and body["eligible"] is True
    etag = ok.headers.get("ETag")
    assert etag and etag.startswith('"') and not etag.startswith("W/")
    assert client.get("/reader", query_string=_fixture_params(), headers={"If-None-Match": etag}).status_code == 304
    head = client.head("/reader", query_string=_fixture_params())
    assert head.status_code == 200 and head.data == b"" and head.headers.get("ETag") == etag
    missing_tz = client.get("/reader", query_string={key: value for key, value in _fixture_params().items() if key != "a_tz"})
    assert missing_tz.status_code == 400
    assert json.loads(missing_tz.data)["code"] == "ERR_READER_MISSING_TZ_A"


def test_dev_get_route_refuses_legacy_or_incomplete_fixtures(tmp_path, monkeypatch):
    legacy = tmp_path / "legacy.json"
    legacy.write_text('{"person_uid":"a","mechanics":{"type":"Generator"}}\n', encoding="utf-8")
    incomplete = tmp_path / "incomplete.json"
    chart = complete_chart(UUID_B, [])
    incomplete.write_text(json.dumps(chart), encoding="utf-8")
    good = tmp_path / "good.json"
    good.write_text(json.dumps(complete_chart(UUID_A, GATES_A)), encoding="utf-8")
    monkeypatch.setattr(http_reader, "ALLOWED_ROOT", tmp_path.resolve())
    client = _client()
    resp = client.get("/reader", query_string={"v": "1", "a": str(legacy), "b": str(good), "a_tz": "UTC", "b_tz": "UTC"})
    assert resp.status_code == 422 and json.loads(resp.data)["code"] == "ERR_M10_LEGACY_INPUT_UNSUPPORTED"
    resp = client.get("/reader", query_string={"v": "1", "a": str(incomplete), "b": str(good), "a_tz": "UTC", "b_tz": "UTC"})
    assert resp.status_code == 503 and json.loads(resp.data)["code"] == "ERR_M10_BODYGRAPH_INCOMPLETE"
    assert "ETag" not in resp.headers and resp.headers.get("Cache-Control") == "no-store"


# --- dev GET bytes unchanged (PR06a: Reader v1 bytes are byte-for-byte pre-change) -------------------

# Recorded at the planning baseline (main 547dc5b, before any PR06a change): the dev GET /reader
# bytes for fixtures/charts/{alice,bob}.json through the pre-change emitter under the fixed
# synthetic identity (Isis5 / INV-000000 / release_id "a"*64).
PRE_CHANGE_DEV_GET_BYTES = (
    b'{"categories":[{"band":"Cool","id":"harmony"}],"eligible":true,'
    b'"idempotence_hash":"400041025cdb2c8e4b14bb428abc2a43eb182b6126b9d69b6f614f6257731145",'
    b'"meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v1",'
    b'"release_id":"' + b"a" * 64 + b'"}\n'
)


def test_dev_get_bytes_for_the_fixture_pair_are_unchanged():
    from flask import Flask
    from engine.runtime.public import emit_reader_public_bytes

    seen = {}

    def fixed_identity(a, b, *, engine_tag, invocation_tag, release_id, eligible, harmony_band):
        seen.update({"eligible": eligible, "harmony_band": harmony_band})
        return emit_reader_public_bytes(a, b, engine_tag="Isis5", invocation_tag="INV-000000", release_id="a" * 64, eligible=eligible, harmony_band=harmony_band)

    app = Flask(__name__)
    app.register_blueprint(http_reader.get_reader_bp(emit_fn=fixed_identity))
    client = app.test_client()
    params = _fixture_params()
    resp = client.get("/reader", query_string=params, headers={"Accept-Encoding": "identity"})
    assert resp.status_code == 200, resp.data
    assert resp.data == PRE_CHANGE_DEV_GET_BYTES
    assert seen == {"eligible": True, "harmony_band": "Cool"}
    swapped = client.get("/reader", query_string=_fixture_params(a=params["b"], b=params["a"]), headers={"Accept-Encoding": "identity"})
    assert swapped.data == PRE_CHANGE_DEV_GET_BYTES
