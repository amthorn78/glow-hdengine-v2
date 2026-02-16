import json

import pytest
from pathlib import Path

from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1

from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.vendor_client import VendorError
from engine.compat.compute import conjunction_public, conjunction_public_resolved
from engine.presenter import emit_public


def _client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _payload():
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    return {
        "a": {"person_uid": "alice"},
        "b": {"person_uid": "bob"},
        "viewer_prefs": {"top_category": CATEGORIES_ORDER_V1[0], "weights": weights},
    }


def _catalog_entries():
    catalog = json.loads(Path("docs/ENDPOINTS_CATALOG.json").read_text(encoding="utf-8"))
    return catalog.get("endpoints", [])




def test_conjunction_contract_emits_stable_canonical_bytes():
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    left = {"person_uid": "alice", "chart": {"type": "resolved"}}
    right = {"person": {"person_uid": "bob"}, "chart": {"type": "resolved"}}

    first = conjunction_public(
        left,
        right,
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
    )
    second = conjunction_public(
        left,
        right,
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
    )
    swapped = conjunction_public(
        right,
        left,
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
    )

    first_bytes = emit_public(first)
    second_bytes = emit_public(second)
    swapped_bytes = emit_public(swapped)

    assert first_bytes == second_bytes
    assert first_bytes == swapped_bytes
    assert first_bytes.endswith(b"\n")

def test_compat_post_contract_and_catalog_entry():
    client = _client()
    resp = client.post(
        "/api/compat/v1",
        data=json.dumps(_payload(), sort_keys=True),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert resp.status_code == 200
    payload = json.loads(resp.data.decode("utf-8"))
    assert "keys" in payload
    assert isinstance(payload["keys"], list)

    categories = payload.get("categories")
    assert isinstance(categories, list) and categories
    expected_keys = []
    for cat in categories:
        assert isinstance(cat, dict)
        expected_keys.extend([cat.get("personal_key"), cat.get("shared_key")])
    assert payload["keys"] == expected_keys
    for key in payload["keys"]:
        assert isinstance(key, str)
        assert key
        assert not key.isdigit()

    entry = next(
        (item for item in _catalog_entries() if item.get("path") == "/api/compat/v1"),
        None,
    )
    assert entry is not None
    method = entry.get("method")
    if isinstance(method, list):
        assert "POST" in method
    else:
        assert method == "POST"
    assert entry.get("classification") == "internal_admin"
    assert entry.get("a7_eligible") is False
    assert isinstance(entry.get("env_gate"), str)
    assert entry.get("env_gate")


def test_compat_get_probe_only_ignores_ids():
    client = _client()
    resp = client.get("/api/compat/v1?a_id=alice&b_id=bob")

    assert resp.status_code == 200
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {"ok": True, "schema": "v1"}
    assert "categories" not in payload
    assert "keys" not in payload


def test_compat_get_probe_only_without_ids():
    client = _client()
    resp = client.get("/api/compat/v1")

    assert resp.status_code == 200
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload == {"ok": True, "schema": "v1"}


def test_compat_get_rejects_body():
    client = _client()
    resp = client.get(
        "/api/compat/v1",
        data=json.dumps(_payload(), sort_keys=True),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert resp.status_code == 400
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload.get("ok") is False


def test_compat_post_rejects_empty_ids():
    client = _client()
    resp = client.post(
        "/api/compat/v1",
        data=json.dumps({"a_id": "", "b_id": ""}, sort_keys=True),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert resp.status_code == 400
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload.get("ok") is False
    assert payload.get("code") == "ERR_COMPAT_INVALID_JSON"


def test_compat_post_rejects_malformed_ids():
    client = _client()
    resp = client.post(
        "/api/compat/v1",
        data=json.dumps({"a_id": "bad id!", "b_id": "bob"}, sort_keys=True),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert resp.status_code == 400
    payload = json.loads(resp.data.decode("utf-8"))
    assert payload.get("ok") is False
    assert payload.get("code") == "ERR_COMPAT_INVALID_JSON"


def test_conjunction_resolved_closed_rails_missing_refuses_without_provider(monkeypatch):
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    calls = []

    class _Outcome:
        status = "error"
        payload = {
            "error": {
                "code": "PROVIDER_REFUSED",
                "message": "Vendor source is refused under SAFE rails (SAFE_MODE=1).",
            }
        }

    def _resolver(*args, **kwargs):
        calls.append((args, kwargs))
        return _Outcome()

    monkeypatch.setattr("engine.compat.compute.resolve_bodygraph", _resolver)

    with pytest.raises(VendorError) as exc:
        conjunction_public_resolved(
            {"user_id": "missing-left"},
            {"person_uid": "bob"},
            viewer_top=CATEGORIES_ORDER_V1[0],
            viewer_weights=weights,
            engine_tag="dev",
            release_id="dev",
            invocation_tag="INV-DEV",
            env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
            local_lookup=lambda *_: None,
        )

    assert exc.value.code == "PROVIDER_REFUSED"
    assert len(calls) == 1


def test_conjunction_resolved_defaults_to_closed_rails_when_env_none(monkeypatch):
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    calls = []

    class _Outcome:
        status = "error"
        payload = {
            "error": {
                "code": "PROVIDER_REFUSED",
                "message": "Vendor source is refused under SAFE rails (SAFE_MODE=1).",
            }
        }

    def _resolver(*args, **kwargs):
        calls.append((args, kwargs))
        return _Outcome()

    monkeypatch.setattr("engine.compat.compute.resolve_bodygraph", _resolver)

    with pytest.raises(VendorError) as exc:
        conjunction_public_resolved(
            {"user_id": "missing-left"},
            {"person_uid": "bob"},
            viewer_top=CATEGORIES_ORDER_V1[0],
            viewer_weights=weights,
            engine_tag="dev",
            release_id="dev",
            invocation_tag="INV-DEV",
            env=None,
            local_lookup=lambda *_: None,
        )

    assert exc.value.code == "PROVIDER_REFUSED"
    assert len(calls) == 1
    _, kwargs = calls[0]
    assert kwargs["env"] == {"SAFE_MODE": "1", "ALLOW_NETWORK": "0"}


def test_conjunction_resolved_open_rails_acquires_and_persists(monkeypatch):
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    store = {}
    calls = []

    def _lookup(user_id):
        return store.get(user_id)

    def _resolver(user_id, **kwargs):
        calls.append({"user_id": user_id, **kwargs})
        store[user_id] = {"person_uid": user_id}

        class _Outcome:
            status = "ok"
            payload = {"status": "ok"}

        return _Outcome()

    monkeypatch.setattr("engine.compat.compute.resolve_bodygraph", _resolver)

    payload = conjunction_public_resolved(
        {"user_id": "left-user", "birthdate": "1990-01-01", "birthtime": "08:30", "location": "Amsterdam"},
        {"user_id": "right-user", "birthdate": "1991-02-02", "birthtime": "09:45", "location": "Berlin"},
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1"},
        local_lookup=_lookup,
    )

    assert len(calls) == 2
    assert payload["conjunction"]["left"]["person_uid"] in store
    assert payload["conjunction"]["right"]["person_uid"] in store


def test_conjunction_resolved_close_back_uses_local_without_provider(monkeypatch):
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    store = {}

    def _lookup(user_id):
        return store.get(user_id)

    def _resolver_open(user_id, **kwargs):
        store[user_id] = {"person_uid": user_id}

        class _Outcome:
            status = "ok"
            payload = {"status": "ok"}

        return _Outcome()

    monkeypatch.setattr("engine.compat.compute.resolve_bodygraph", _resolver_open)

    conjunction_public_resolved(
        {"user_id": "left-user"},
        {"user_id": "right-user"},
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1"},
        local_lookup=_lookup,
    )

    def _resolver_closed(*args, **kwargs):
        raise AssertionError("provider path must not run once local cache is populated")

    monkeypatch.setattr("engine.compat.compute.resolve_bodygraph", _resolver_closed)

    payload = conjunction_public_resolved(
        {"user_id": "left-user"},
        {"user_id": "right-user"},
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
        local_lookup=_lookup,
    )

    assert payload["conjunction"]["left"]["person_uid"]
    assert payload["conjunction"]["right"]["person_uid"]


def test_conjunction_resolved_local_vendor_payload_uses_user_id_hint():
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}

    def _lookup(user_id):
        return {
            "id": user_id,
            "mechanics": {"type": "generator"},
            "birth": {"date": "1990-01-01", "time": "08:30", "location": "Amsterdam"},
        }

    payload = conjunction_public_resolved(
        {"user_id": "left-user"},
        {"user_id": "right-user"},
        viewer_top=CATEGORIES_ORDER_V1[0],
        viewer_weights=weights,
        engine_tag="dev",
        release_id="dev",
        invocation_tag="INV-DEV",
        env={"SAFE_MODE": "1", "ALLOW_NETWORK": "0"},
        local_lookup=_lookup,
    )

    observed = {
        payload["conjunction"]["left"]["person_uid"],
        payload["conjunction"]["right"]["person_uid"],
    }
    expected = {resolve_db_user_id("left-user"), resolve_db_user_id("right-user")}
    assert observed == expected
