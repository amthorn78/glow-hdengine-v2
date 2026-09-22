import json

import pytest

from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1
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
