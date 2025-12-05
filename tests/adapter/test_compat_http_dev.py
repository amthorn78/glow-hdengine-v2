import json

from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1


def _dev_client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _minimal_payload():
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    return {
        "a": {"person_uid": "alice"},
        "b": {"person_uid": "bob"},
        "viewer_prefs": {"top_category": CATEGORIES_ORDER_V1[0], "weights": weights},
    }


def test_dev_compat_malformed_json_returns_governed_error_json():
    client = _dev_client()
    resp = client.post(
        "/api/compat/v1",
        data=b"{bad: json",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert resp.status_code == 400
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"

    body_bytes = resp.data
    assert body_bytes.endswith(b"\n")

    payload = json.loads(body_bytes.decode("utf-8"))
    assert payload.get("ok") is False
    assert isinstance(payload.get("code"), str)
    assert isinstance(payload.get("error"), str)
    assert "<html" not in body_bytes.decode("utf-8").lower()


def test_dev_compat_minimal_valid_payload_success_behavior():
    client = _dev_client()
    payload = _minimal_payload()

    resp = client.post(
        "/api/compat/v1",
        data=json.dumps(payload, sort_keys=True),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )

    assert resp.status_code == 200
    assert resp.headers.get("Content-Type") == "application/json; charset=utf-8"

    body_bytes = resp.data
    assert body_bytes.endswith(b"\n")

    data = json.loads(body_bytes.decode("utf-8"))
    assert "categories" in data
    assert isinstance(data.get("meta"), dict)
    assert data.get("meta", {}).get("engine_tag") == "dev"
