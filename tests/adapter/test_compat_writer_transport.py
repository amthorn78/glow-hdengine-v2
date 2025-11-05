import json

import pytest

from adapter.app import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1


@pytest.fixture()
def compat_client():
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


def test_compat_writer_success_cache_control(compat_client):
    resp = compat_client.post(
        "/api/compat/v1",
        data=json.dumps(_payload()),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    assert resp.status_code == 200
    assert resp.headers.get("Cache-Control") == "no-store"
    assert "ETag" not in resp.headers
    assert "Content-Encoding" not in resp.headers


def test_compat_writer_head_405(compat_client):
    resp = compat_client.head("/api/compat/v1")
    assert resp.status_code == 405
    assert resp.headers.get("Allow") == "POST, OPTIONS"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Length") == "0"


def test_compat_writer_options_204(compat_client):
    resp = compat_client.open("/api/compat/v1", method="OPTIONS")
    assert resp.status_code == 204
    assert resp.headers.get("Allow") == "POST, OPTIONS"
    assert resp.headers.get("Cache-Control") == "no-store"
    assert resp.headers.get("Content-Length") == "0"
    assert resp.data == b""
