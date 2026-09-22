import hashlib
import json
from pathlib import Path

import jsonschema
import pytest

from adapter.factory import create_app
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.resolver import ResolvedCompatChart
from engine.bodygraph.vendor_client import VendorError
from engine.compat import compute
from engine.compat.categories import CATEGORIES_ORDER_V1
from engine.compat.compute import conjunction_public, conjunction_public_resolved, evaluation_party
from engine.db.errors import PrimaryUnavailable
from engine.presenter import emit_public
from tests.support.pr04_fixtures import (
    GATES_A,
    GATES_B,
    UUID_A,
    UUID_B,
    FakeCurrentViewDB,
    build_bundle,
    build_pack,
    complete_chart,
    inject_seams,
)

SCHEMA = json.loads(Path("schemas/magic10_compat_result_v1.schema.json").read_text(encoding="utf-8"))


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-compat-route-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-compat-route-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: pytest.fail("vendor client constructed"))


def _client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _prefs():
    return {"top_category": CATEGORIES_ORDER_V1[0], "weights": {cat: 10 for cat in CATEGORIES_ORDER_V1}}


def _payload():
    return {"a": complete_chart(UUID_A, GATES_A), "b": complete_chart(UUID_B, GATES_B), "viewer_prefs": _prefs()}


def _post(client, body):
    return client.post("/api/compat/v1", data=json.dumps(body, sort_keys=True), headers={"Content-Type": "application/json; charset=utf-8"})


def _catalog_entries():
    catalog = json.loads(Path("docs/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8"))
    return catalog.get("endpoints", [])


def _party(uid, gates):
    return evaluation_party(ResolvedCompatChart(uid, complete_chart(uid, gates), "resolved", None, None, None, None))


def test_conjunction_contract_emits_stable_canonical_bytes():
    left = _party(UUID_A, GATES_A)
    right = _party(UUID_B, GATES_B)
    first = conjunction_public(left, right)
    second = conjunction_public(left, right)
    swapped = conjunction_public(right, left)
    first_bytes, second_bytes, swapped_bytes = emit_public(first), emit_public(second), emit_public(swapped)
    assert first_bytes == second_bytes == swapped_bytes
    assert first_bytes.endswith(b"\n")
    assert set(first["conjunction"]) == {"left", "right", "compat"}
    jsonschema.validate(instance=first["conjunction"]["compat"], schema=SCHEMA)


def test_conjunction_identity_hash_artifact_matches_canonical_bytes():
    canonical_bytes = Path("artifacts/compat/AB.json").read_bytes()
    observed_hash = hashlib.sha256(canonical_bytes).hexdigest()
    artifact_hash = Path("artifacts/compat/identity_hash.txt").read_text(encoding="utf-8").strip()
    assert observed_hash == artifact_hash


def test_compat_post_contract_and_catalog_entry(bundle):
    resp = _post(_client(), _payload())
    assert resp.status_code == 200
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    payload = json.loads(resp.data.decode("utf-8"))
    assert "keys" not in payload
    jsonschema.validate(instance=payload, schema=SCHEMA)
    assert set(payload) == {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}
    assert payload["release_id"] == bundle.release_id
    assert emit_public(payload) == resp.data
    for row in payload["categories"]:
        assert set(row) == {"category_id", "score", "band", "shared_key", "personal_lo_to_hi_key", "personal_hi_to_lo_key"}
        assert row["shared_key"] and not row["shared_key"].isdigit()

    entry = next((item for item in _catalog_entries() if item.get("path") == "/api/compat/v1"), None)
    assert entry is not None
    method = entry.get("method")
    if isinstance(method, list):
        assert "POST" in method
    else:
        assert method == "POST"
    assert entry.get("classification") == "internal_admin"
    assert entry.get("a7_eligible") is False
    assert isinstance(entry.get("env_gate"), str) and entry.get("env_gate")


def test_compat_post_ab_ba_and_two_run_bytes_identical():
    client = _client()
    payload = _payload()
    swapped = {"a": payload["b"], "b": payload["a"], "viewer_prefs": payload["viewer_prefs"]}
    first, second, third = _post(client, payload), _post(client, swapped), _post(client, payload)
    assert first.status_code == second.status_code == third.status_code == 200
    assert first.data == second.data == third.data


def test_compat_post_matches_cli_stdout_for_the_same_pair(tmp_path, capsys):
    from engine.cli.main import cli

    resp = _post(_client(), _payload())
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}), encoding="utf-8")
    assert cli(["showcompat", "--pair-file", str(pair)]) == 0
    assert capsys.readouterr().out.encode("utf-8") == resp.data


def test_compat_post_stored_ids_resolve_read_only_through_current_rows(monkeypatch):
    key_a = resolve_db_user_id("alice")
    key_b = resolve_db_user_id("bob")
    db = FakeCurrentViewDB({key_a: complete_chart(f"person-{key_a}", GATES_A), key_b: complete_chart(f"person-{key_b}", GATES_B)})
    monkeypatch.setattr("engine.http.compat_handler.DBAccess.for_current_env", lambda *a, **k: db)
    resp = _post(_client(), {"a_id": "alice", "b_id": "bob", "viewer_prefs": _prefs()})
    assert resp.status_code == 200, resp.data
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload["schema"] == "magic10_compat_result.v1"
    assert {params[0] for _sql, params in db.queries} == {key_a, key_b}
    for sql, _params in db.queries:
        assert "public.hde_body_graphs_current" in sql and "vendor = 'hdapi'" in sql and "%s" in sql
    assert db.writes == []


def test_compat_post_stored_id_miss_and_db_unavailable(monkeypatch):
    db = FakeCurrentViewDB({})
    monkeypatch.setattr("engine.http.compat_handler.DBAccess.for_current_env", lambda *a, **k: db)
    resp = _post(_client(), {"a_id": "alice", "b_id": "bob", "viewer_prefs": _prefs()})
    assert resp.status_code == 404
    assert json.loads(resp.data)["code"] == "ERR_NOT_FOUND"
    assert resp.headers.get("Cache-Control") == "no-store"

    def _unavailable(*a, **k):
        raise PrimaryUnavailable(code="missing_database_url")

    monkeypatch.setattr("engine.http.compat_handler.DBAccess.for_current_env", _unavailable)
    resp = _post(_client(), {"a_id": "alice", "b_id": "bob", "viewer_prefs": _prefs()})
    assert resp.status_code == 503
    assert json.loads(resp.data)["code"] == "ERR_M10_RESOLVER_UNAVAILABLE"


def test_compat_post_inline_legacy_and_invalid_charts_refuse():
    client = _client()
    resp = _post(client, {"a": {"person_uid": "alice"}, "b": {"person_uid": "bob"}, "viewer_prefs": _prefs()})
    assert resp.status_code == 422
    assert json.loads(resp.data)["code"] == "ERR_M10_LEGACY_INPUT_UNSUPPORTED"
    broken = _payload()
    broken["a"]["bodygraph"]["gates"] = ["10", "10"]
    resp = _post(client, broken)
    assert resp.status_code == 422
    assert json.loads(resp.data)["code"] == "ERR_READER_INVALID_CHART"
    empty = _payload()
    empty["a"]["bodygraph"]["gates"] = []
    resp = _post(client, empty)
    assert resp.status_code == 422
    assert json.loads(resp.data)["code"] == "ERR_READER_MISSING_PARAM"


def test_compat_post_self_pair_returns_carrier_and_admission_refusal_is_503(monkeypatch):
    client = _client()
    resp = _post(client, {"a": complete_chart(UUID_A, GATES_A), "b": complete_chart(UUID_A, GATES_A), "viewer_prefs": _prefs()})
    assert resp.status_code == 200
    assert json.loads(resp.data) == {"categories": [], "eligible": False}
    monkeypatch.setattr(compute, "_BUNDLE_PROVIDER", compute.load_active_mechanics_bundle)
    resp = _post(client, _payload())
    assert resp.status_code == 503
    assert json.loads(resp.data)["code"] == "ERR_M10_MANIFEST_MISMATCH"
    assert resp.headers.get("Cache-Control") == "no-store"


def test_compat_post_viewer_prefs_validated_before_resolution():
    resp = _post(_client(), {"a": {"person_uid": "A"}, "b": {"person_uid": "B"}, "viewer_prefs": {"top_category": "not_a_category"}})
    assert resp.status_code == 400
    assert json.loads(resp.data)["code"] == "ERR_INVALID_VIEWER_PREFS"


@pytest.mark.parametrize("app_env", ["prod", "production", "live", " Production ", "LIVE"])
def test_compat_post_is_hidden_for_normalized_production_aliases(monkeypatch, app_env):
    monkeypatch.setenv("APP_ENV", app_env)
    resp = _client().post("/api/compat/v1", json=_payload())
    assert resp.status_code == 404
    assert resp.get_json()["code"] == "ERR_NOT_FOUND"
    assert resp.headers["Cache-Control"] == "no-store"


@pytest.mark.parametrize("engine_env", ["prod", "production", "live", " Production ", "LIVE"])
def test_compat_post_is_hidden_for_normalized_engine_env_aliases(monkeypatch, engine_env):
    monkeypatch.delenv("APP_ENV", raising=False)
    monkeypatch.setenv("ENGINE_ENV", engine_env)
    resp = _client().post("/api/compat/v1", json=_payload())
    assert resp.status_code == 404
    assert resp.get_json()["code"] == "ERR_NOT_FOUND"
    assert resp.headers["Cache-Control"] == "no-store"


@pytest.mark.parametrize("method", ["GET", "POST", "HEAD", "OPTIONS", "PUT"])
def test_compat_path_is_hidden_for_every_method_in_production(monkeypatch, method):
    monkeypatch.setenv("APP_ENV", "production")
    kwargs = {"json": _payload()} if method == "POST" else {}
    resp = _client().open("/api/compat/v1", method=method, **kwargs)
    assert resp.status_code == 404
    assert resp.headers["Cache-Control"] == "no-store"
    if method == "HEAD":
        assert resp.data == b""
    else:
        assert resp.get_json()["code"] == "ERR_NOT_FOUND"


def test_compat_subpath_is_hidden_in_production(monkeypatch):
    monkeypatch.setenv("APP_ENV", "live")
    resp = _client().get("/api/compat/v1/missing")
    assert resp.status_code == 404
    assert resp.get_json()["code"] == "ERR_NOT_FOUND"
    assert resp.headers["Cache-Control"] == "no-store"


def test_compat_get_probe_only_ignores_ids():
    resp = _client().get("/api/compat/v1?a_id=alice&b_id=bob")
    assert resp.status_code == 200
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {"ok": True, "schema": "v1"}
    assert "categories" not in payload and "keys" not in payload


def test_compat_get_probe_only_without_ids():
    resp = _client().get("/api/compat/v1")
    assert resp.status_code == 200
    assert json.loads(resp.data.decode("utf-8")) == {"ok": True, "schema": "v1"}


def test_compat_get_rejects_body():
    resp = _client().get("/api/compat/v1", data=json.dumps(_payload(), sort_keys=True), headers={"Content-Type": "application/json; charset=utf-8"})
    assert resp.status_code == 400
    assert json.loads(resp.data.decode("utf-8")).get("ok") is False


def test_compat_post_rejects_empty_ids():
    resp = _post(_client(), {"a_id": "", "b_id": ""})
    assert resp.status_code == 400
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload.get("ok") is False and payload.get("code") == "ERR_COMPAT_INVALID_JSON"


def test_compat_post_rejects_malformed_ids():
    resp = _post(_client(), {"a_id": "bad id!", "b_id": "bob"})
    assert resp.status_code == 400
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload.get("ok") is False and payload.get("code") == "ERR_COMPAT_INVALID_JSON"


def test_conjunction_resolved_closed_rails_missing_refuses_without_provider():
    with pytest.raises(VendorError) as exc:
        conjunction_public_resolved({"user_id": "missing-left"}, {"person_uid": UUID_B}, env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}, local_lookup=lambda *_: None)
    assert exc.value.code == "PROVIDER_REFUSED"


def test_conjunction_resolved_defaults_to_closed_rails_when_env_none():
    with pytest.raises(VendorError) as exc:
        conjunction_public_resolved({"user_id": "missing-left"}, {"person_uid": UUID_B}, env=None, local_lookup=lambda *_: None)
    assert exc.value.code == "PROVIDER_REFUSED"


def test_conjunction_resolved_local_hits_evaluate_without_provider():
    key_left = resolve_db_user_id("left-user")
    key_right = resolve_db_user_id("right-user")
    store = {key_left: complete_chart(f"person-{key_left}", GATES_A), key_right: complete_chart(f"person-{key_right}", GATES_B)}
    payload = conjunction_public_resolved({"user_id": "left-user"}, {"user_id": "right-user"}, env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}, local_lookup=store.get)
    observed = {payload["conjunction"]["left"]["person_uid"], payload["conjunction"]["right"]["person_uid"]}
    assert observed == {key_left, key_right}
    assert payload["conjunction"]["compat"]["schema"] == "magic10_compat_result.v1"
