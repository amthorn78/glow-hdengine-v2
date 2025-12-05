import json

from adapter.http_reader import create_app as create_dev_app
from adapter import wsgi as wsgi_adapter
from engine.compat.categories import CATEGORIES_ORDER_V1


def _minimal_payload():
    weights = {cat: 10 for cat in CATEGORIES_ORDER_V1}
    return {
        "a": {"person_uid": "alice"},
        "b": {"person_uid": "bob"},
        "viewer_prefs": {"top_category": CATEGORIES_ORDER_V1[0], "weights": weights},
    }


def _clients():
    dev_app = create_dev_app()
    dev_app.config.update(TESTING=True)

    wsgi_app = wsgi_adapter.create_app()
    wsgi_app.config.update(TESTING=True)

    return dev_app.test_client(), wsgi_app.test_client()


def test_dev_vs_wsgi_compat_parity_malformed_json():
    dev_client, wsgi_client = _clients()

    body = b"{bad: json"
    headers = {"Content-Type": "application/json; charset=utf-8"}

    dev_resp = dev_client.post("/api/compat/v1", data=body, headers=headers)
    wsgi_resp = wsgi_client.post("/api/compat/v1", data=body, headers=headers)

    assert dev_resp.status_code == wsgi_resp.status_code == 400
    assert dev_resp.headers.get("Content-Type") == wsgi_resp.headers.get("Content-Type")
    assert dev_resp.headers.get("Cache-Control") == wsgi_resp.headers.get("Cache-Control")
    assert dev_resp.data == wsgi_resp.data


def test_dev_vs_wsgi_compat_parity_minimal_valid_payload():
    dev_client, wsgi_client = _clients()

    payload = json.dumps(_minimal_payload(), sort_keys=True)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    dev_resp = dev_client.post("/api/compat/v1", data=payload, headers=headers)
    wsgi_resp = wsgi_client.post("/api/compat/v1", data=payload, headers=headers)

    assert dev_resp.status_code == wsgi_resp.status_code == 200
    assert dev_resp.headers.get("Content-Type") == wsgi_resp.headers.get("Content-Type")
    assert dev_resp.headers.get("Cache-Control") == wsgi_resp.headers.get("Cache-Control")
    assert dev_resp.data == wsgi_resp.data
