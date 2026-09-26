"""PF10 §2.23 (C040-07) Reader v2 on the production ``POST /api/reader`` route and the
PF05 §5.4 prefix mechanism (HDE-EPIC040-PR06a)."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import jsonschema
import pytest
from flask import Flask

from adapter import factory, http_reader, wsgi
from engine.bodygraph.resolver import resolve_compat_chart
from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.compat import compute
from engine.config.registry_loader import SchemaValidationError
from engine.db.errors import PrimaryUnavailable
from engine.runtime.identity import identity_meta
from engine.serializer.canon import sercanon
from tests.support.pr04_fixtures import (
    GATES_A,
    GATES_B,
    UUID_A,
    UUID_B,
    UUID_C,
    FakeCurrentViewDB,
    build_bundle,
    build_pack,
    complete_chart,
    inject_seams,
)

SIX_KEYS = ["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]
BANDS = {"Cool", "Open", "Warm", "Glow"}
FORBIDDEN = (
    "score", "signals", "pair_key", "gates", "shared_key", "personal", "config_id", "keys", "q\"",
    UUID_A, UUID_B, "bodygraph", "prompt",
)
V2_SCHEMA = json.loads(Path("schemas/reader.v2.schema.json").read_text(encoding="utf-8"))
GOLDENS = json.loads(Path("tests/fixtures/magic10/v1/goldens.json").read_text(encoding="utf-8"))["cases"]


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr06a-reader-v2-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr06a-reader-v2-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    for name in ("HD_API_BASE_URL", "HDAPI_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor client constructed"))
    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("ingest attempted"))
    monkeypatch.setattr("engine.bodygraph.resolver.persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))


def _install_db(monkeypatch, charts):
    fake = FakeCurrentViewDB(charts)
    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: fake))
    return fake


@pytest.fixture
def db(monkeypatch):
    return _install_db(monkeypatch, {UUID_A: complete_chart(UUID_A, GATES_A), UUID_B: complete_chart(UUID_B, GATES_B)})


def _client(create_app=http_reader.create_app):
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _post(client, body=None, *, raw: bytes | None = None, query="v=2", headers=None):
    data = raw if raw is not None else (json.dumps(body, sort_keys=True).encode("utf-8") if body is not None else None)
    return client.post(f"/api/reader?{query}" if query else "/api/reader", data=data, headers=headers or {"Content-Type": "application/json; charset=utf-8"})


def _assert_error(resp, token, status, db=None):
    assert resp.status_code == status, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert body == {"schema": "v1", "ok": False, "code": token, "error": body["error"]}
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    assert resp.data.endswith(b"\n")
    if db is not None:
        assert db.queries == []


def _oracle_bands(left_chart, right_chart) -> list[tuple[str, str]]:
    """In-process oracle: the validated compat result of the same parties, in its validated order."""
    left = resolve_compat_chart(left_chart, source_policy="local", env=None)
    right = resolve_compat_chart(right_chart, source_policy="local", env=None)
    result = compute.evaluate_pair(compute.evaluation_party(left), compute.evaluation_party(right))
    assert not compute.is_ineligible_carrier(result)
    return [(row["category_id"], row["band"]) for row in result["categories"]]


def _strict_validator(schema):
    strict = jsonschema.Draft202012Validator.TYPE_CHECKER.redefine(
        "integer", lambda checker, instance: type(instance) is int
    )
    return jsonschema.validators.extend(jsonschema.Draft202012Validator, type_checker=strict)(schema)


# --- 1. eligible pair ------------------------------------------------------------------------

def test_v2_eligible_pair_is_the_ordered_full_magic10(db, bundle):
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_B})
    assert resp.status_code == 200, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert list(body) == SIX_KEYS
    assert body["reader_version"] == "v2" and body["eligible"] is True
    assert len(body["categories"]) == 10
    assert [item["id"] for item in body["categories"]] == list(FROZEN_MAGIC10_ORDER)
    assert all(set(item) == {"band", "id"} and item["band"] in BANDS for item in body["categories"])
    oracle = _oracle_bands(complete_chart(UUID_A, GATES_A), complete_chart(UUID_B, GATES_B))
    assert [(item["id"], item["band"]) for item in body["categories"]] == oracle
    assert body["meta"] == {"engine_tag": identity_meta()["engine_tag"], "invocation_tag": identity_meta()["invocation_tag"]}
    assert body["release_id"] == bundle.release_id
    assert sercanon(body) == resp.data
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert resp.headers.get("Cache-Control") == "private, max-age=0, must-revalidate"
    assert resp.headers.get("Vary") == "Authorization, Accept-Encoding"
    assert resp.headers.get("Content-Length") == str(len(resp.data))
    assert "ETag" not in resp.headers
    text = resp.data.decode("utf-8")
    for forbidden in FORBIDDEN:
        assert forbidden not in text, forbidden


# --- 2. AB/BA, two-run and preimage coupling -----------------------------------------------------

def test_v2_ab_ba_two_run_identity_and_preimage_coupling(db):
    client = _client()
    ab = _post(client, {"a_id": UUID_A, "b_id": UUID_B})
    ba = _post(client, {"a_id": UUID_B, "b_id": UUID_A})
    again = _post(client, {"a_id": UUID_A, "b_id": UUID_B})
    assert ab.status_code == 200, ab.data
    assert ab.data == ba.data == again.data
    body = json.loads(ab.data.decode("utf-8"))
    preimage = {key: value for key, value in body.items() if key != "idempotence_hash"}
    assert body["idempotence_hash"] == hashlib.sha256(sercanon(preimage)).hexdigest()
    conditional = client.post(
        "/api/reader?v=2",
        data=json.dumps({"a_id": UUID_A, "b_id": UUID_B}),
        headers={"Content-Type": "application/json; charset=utf-8", "If-None-Match": '"' + hashlib.sha256(ab.data).hexdigest() + '"'},
    )
    assert conditional.status_code == 200 and conditional.data == ab.data and "ETag" not in conditional.headers


# --- 3. valid self-pair ------------------------------------------------------------------------

def test_v2_valid_self_pair_is_ineligible_with_empty_categories(db, monkeypatch):
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached for a self-pair"))
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_A})
    assert resp.status_code == 200, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert list(body) == SIX_KEYS
    assert body["reader_version"] == "v2" and body["eligible"] is False and body["categories"] == []
    assert body["release_id"] == identity_meta()["release_id"]
    assert [params for _sql, params in db.queries] == [(UUID_A,)]


# --- 4. schema ------------------------------------------------------------------------------------

def test_v2_bodies_validate_against_the_v2_schema(db):
    client = _client()
    validator = _strict_validator(V2_SCHEMA)
    eligible = json.loads(_post(client, {"a_id": UUID_A, "b_id": UUID_B}).data)
    ineligible = json.loads(_post(client, {"a_id": UUID_A, "b_id": UUID_A}).data)
    invalid_version = json.loads(_post(client, {"a_id": UUID_A, "b_id": UUID_B}, query="v=3").data)
    for instance in (eligible, ineligible, invalid_version):
        validator.validate(instance)
    wrong_order = dict(eligible, categories=list(reversed(eligible["categories"])))
    assert not validator.is_valid(wrong_order)
    assert not validator.is_valid(dict(eligible, reader_version="v1"))


# --- 5. golden-derived pairs ---------------------------------------------------------------------

def _case(case_id: str) -> dict:
    return next(case for case in GOLDENS if case["case_id"] == case_id)


def _golden_pairs():
    g004 = _case("M10-G004")
    yield "M10-G004", g004["inputs"]["member_a_gates"], g004["inputs"]["member_b_gates"], g004["expected"]["categories"]
    g005 = _case("M10-G005")
    for pair in g005["inputs"]["pairs"]:
        yield f"M10-G005:{pair['pair_id']}", pair["a"]["gates"], pair["b"]["gates"], g005["expected"]["intrinsic"]["categories"]
    g008 = _case("M10-G008")
    yield "M10-G008", g008["inputs"]["a"]["gates"], g008["inputs"]["b"]["gates"], g008["expected"]["categories"]


@pytest.mark.parametrize(("case_id", "a_gates", "b_gates", "expected"), list(_golden_pairs()), ids=lambda value: value if isinstance(value, str) else None)
def test_v2_golden_derived_pairs_reproduce_the_expected_band_vector(monkeypatch, case_id, a_gates, b_gates, expected):
    _install_db(monkeypatch, {UUID_A: complete_chart(UUID_A, [str(g) for g in a_gates]), UUID_B: complete_chart(UUID_B, [str(g) for g in b_gates])})
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_B})
    assert resp.status_code == 200, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert body["eligible"] is True
    assert [(item["id"], item["band"]) for item in body["categories"]] == [(row["category_id"], row["band"]) for row in expected]


def test_v2_golden_self_pair_is_ineligible(monkeypatch):
    g007 = _case("M10-G007")
    assert g007["inputs"]["a"]["person_uid"] == g007["inputs"]["b"]["person_uid"]
    _install_db(monkeypatch, {UUID_A: complete_chart(UUID_A, [str(g) for g in g007["inputs"]["a"]["gates"]])})
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached for a self-pair"))
    body = json.loads(_post(_client(), {"a_id": UUID_A, "b_id": UUID_A}).data)
    assert body["eligible"] is False and body["categories"] == []
    assert g007["expected"]["reader"]["eligible"] is False and g007["expected"]["reader"]["categories"] == []


# --- 6. version strictness -----------------------------------------------------------------------

@pytest.mark.parametrize("query", ["", "v=", "v=3", "v=01", "v=1&v=1", "v=1&v=2", "v=2&v=2", "v=%201", "v=1.0", "v=v2"])
def test_version_strictness_refuses_before_any_lookup(db, query):
    _assert_error(_post(_client(), {"a_id": UUID_A, "b_id": UUID_B}, query=query), "ERR_READER_INVALID_VERSION", 400, db)


# --- 7. method refusals --------------------------------------------------------------------------

@pytest.mark.parametrize("method", ["GET", "HEAD", "PUT", "PATCH", "DELETE", "OPTIONS"])
def test_non_post_methods_on_the_production_route_are_the_governed_405(db, method):
    resp = _client().open("/api/reader?v=2", method=method)
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "POST"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert "ETag" not in resp.headers and "Content-Encoding" not in resp.headers
    if method != "HEAD":
        assert json.loads(resp.data) == {"schema": "v1", "ok": False, "code": "ERR_NOT_FOUND", "error": "not found"}
        assert resp.data.endswith(b"\n")
    assert db.queries == []


@pytest.mark.parametrize("create_app", [factory.create_app, http_reader.create_app, wsgi.create_app], ids=["factory", "http_reader", "wsgi"])
@pytest.mark.parametrize("method", ["GET", "HEAD", "PUT", "PATCH", "DELETE", "OPTIONS", "TRACE", "CONNECT", "PROPFIND", "QUERY"])
def test_every_non_post_method_is_the_same_governed_405_on_every_app_factory(db, create_app, method):
    # TRACE, CONNECT and extension methods match no rule, so routing refuses them before
    # any view runs; they still get the route's governed 405, not the factory's own.
    resp = _client(create_app).open("/api/reader?v=2", method=method)
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "POST"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"
    assert "ETag" not in resp.headers and "Content-Encoding" not in resp.headers
    if method != "HEAD":
        body = json.loads(resp.data)
        assert body == {"schema": "v1", "ok": False, "code": "ERR_NOT_FOUND", "error": "not found"}
        assert sercanon(body) == resp.data
    assert db.queries == []


def test_the_unrouted_method_refusal_is_bound_to_the_mounted_route(db):
    app = Flask(__name__)
    app.register_blueprint(http_reader.get_reader_api_bp(), url_prefix="/elsewhere")
    client = app.test_client()
    moved = client.open("/elsewhere/reader", method="TRACE")
    assert moved.status_code == 405 and moved.headers.get("Allow") == "POST"
    assert json.loads(moved.data)["code"] == "ERR_NOT_FOUND"
    assert client.open("/api/reader", method="TRACE").status_code == 404
    # Other routes keep their own 405: the dev GET /reader is not the production Reader.
    dev = _client().open("/reader?v=1", method="TRACE")
    assert dev.status_code == 405 and dev.headers.get("Allow") != "POST"
    assert db.queries == []


def test_unprefixed_post_reader_is_the_governed_405(db):
    resp = _client().post("/reader?v=2", data=json.dumps({"a_id": UUID_A, "b_id": UUID_B}), headers={"Content-Type": "application/json; charset=utf-8"})
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "GET, HEAD"
    assert resp.headers.get("Cache-Control") == "no-store" and "ETag" not in resp.headers
    assert json.loads(resp.data) == {"schema": "v1", "ok": False, "code": "ERR_NOT_FOUND", "error": "not found"}
    assert db.queries == []


# --- 8. mounts -----------------------------------------------------------------------------------

@pytest.mark.parametrize("create_app", [factory.create_app, http_reader.create_app, wsgi.create_app], ids=["factory", "http_reader", "wsgi"])
def test_every_app_factory_mounts_the_production_reader_under_api(create_app):
    app = create_app()
    rules = {}
    for rule in app.url_map.iter_rules():
        # Automatic OPTIONS is Flask's, not the rule's; an explicitly declared OPTIONS stays.
        declared = rule.methods - ({"OPTIONS"} if rule.provide_automatic_options else set())
        rules.setdefault(rule.rule, []).append((frozenset(declared), rule.endpoint))
    api_reader = {methods: endpoint for methods, endpoint in rules["/api/reader"]}
    assert api_reader[frozenset({"POST"})] == "reader_api.reader_post"
    assert api_reader[frozenset({"GET", "HEAD", "PUT", "PATCH", "DELETE", "OPTIONS"})] == "reader_api.reader_method_not_allowed"
    reader = {methods: endpoint for methods, endpoint in rules["/reader"]}
    assert reader[frozenset({"GET", "HEAD"})] == "reader_v1.reader_v1"
    assert reader[frozenset({"POST"})] == "reader_v1.reader_post_not_allowed"
    assert "/api/aux/narrative" in rules and "/aux/narrative" in rules
    assert "/internal/version" in rules
    for path in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction", "/internal/dev/sampler"):
        assert path in rules, path
    assert not any(path.startswith("/api/") for path in rules if path not in ("/api/reader", "/api/aux/narrative") and not path.startswith("/api/compat/"))


# --- 9. real admission owner -----------------------------------------------------------------------

def test_real_admission_owner_serves_v2_with_the_admitted_release(db, monkeypatch):
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    resp = _post(_client(), {"a_id": UUID_A, "b_id": UUID_B})
    assert resp.status_code == 200, resp.data
    body = json.loads(resp.data.decode("utf-8"))
    assert list(body) == SIX_KEYS and body["reader_version"] == "v2"
    assert body["release_id"] == identity_meta()["release_id"]
    assert [item["id"] for item in body["categories"]] == list(FROZEN_MAGIC10_ORDER)


# --- 10. errors are the v1 route's, byte for byte -------------------------------------------------

def _unknown_person(monkeypatch):
    _install_db(monkeypatch, {UUID_A: complete_chart(UUID_A, GATES_A)})
    return {"a_id": UUID_A, "b_id": UUID_C}, "ERR_M10_PERSON_UNRESOLVED", 404


def _db_unavailable(monkeypatch):
    def _unavailable(cls, *a, **k):
        raise PrimaryUnavailable(code="missing_database_url")

    monkeypatch.setattr(http_reader.DBAccess, "for_current_env", classmethod(_unavailable))
    return {"a_id": UUID_A, "b_id": UUID_B}, "ERR_M10_RESOLVER_UNAVAILABLE", 503


def _stored_row_defect(monkeypatch):
    defective = complete_chart(UUID_A, GATES_A)
    defective["bodygraph"].pop("profile")
    _install_db(monkeypatch, {UUID_A: defective, UUID_B: complete_chart(UUID_B, GATES_B)})
    monkeypatch.setattr(compute, "compute_core", lambda *a, **k: pytest.fail("core reached"))
    return {"a_id": UUID_A, "b_id": UUID_B}, "ERR_M10_BODYGRAPH_INCOMPLETE", 503


def _admission_refusal(monkeypatch):
    _install_db(monkeypatch, {UUID_A: complete_chart(UUID_A, GATES_A), UUID_B: complete_chart(UUID_B, GATES_B)})

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", refuse)
    return {"a_id": UUID_A, "b_id": UUID_B}, "ERR_M10_MANIFEST_MISMATCH", 503


@pytest.mark.parametrize("scenario", [_unknown_person, _db_unavailable, _stored_row_defect, _admission_refusal], ids=lambda fn: fn.__name__)
def test_v2_errors_are_identical_to_v1_errors(monkeypatch, scenario):
    body, token, status = scenario(monkeypatch)
    client = _client()
    v1 = _post(client, body, query="v=1")
    v2 = _post(client, body, query="v=2")
    _assert_error(v1, token, status)
    _assert_error(v2, token, status)
    assert v1.data == v2.data
    assert v1.status_code == v2.status_code


# --- 11. production APP_ENV ----------------------------------------------------------------------

def test_production_app_env_serves_v2_and_forbids_the_dev_get(db, monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    client = _client()
    resp = _post(client, {"a_id": UUID_A, "b_id": UUID_B})
    assert resp.status_code == 200, resp.data
    assert json.loads(resp.data)["reader_version"] == "v2"
    assert client.get("/reader?v=1&a=x&b=y").status_code == 403
    assert client.get("/reader?v=2&a=x&b=y").status_code == 400
