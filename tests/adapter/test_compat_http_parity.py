import json

from adapter.factory import create_app as create_selected_app
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
    selected_app = create_selected_app()
    selected_app.config.update(TESTING=True)

    dev_app = create_dev_app()
    dev_app.config.update(TESTING=True)

    wsgi_app = wsgi_adapter.create_app()
    wsgi_app.config.update(TESTING=True)

    return selected_app.test_client(), dev_app.test_client(), wsgi_app.test_client()


def test_selected_factory_required_route_inventory():
    app = create_selected_app()
    inventory = {
        (method, rule.rule)
        for rule in app.url_map.iter_rules()
        for method in rule.methods
    }
    assert inventory >= {
        ("GET", "/reader"),
        ("GET", "/internal/version"),
        ("POST", "/api/compat/v1"),
    }


def test_dev_vs_wsgi_compat_parity_malformed_json():
    selected_client, dev_client, wsgi_client = _clients()

    body = b"{bad: json"
    headers = {"Content-Type": "application/json; charset=utf-8"}

    dev_resp = dev_client.post("/api/compat/v1", data=body, headers=headers)
    wsgi_resp = wsgi_client.post("/api/compat/v1", data=body, headers=headers)
    selected_resp = selected_client.post("/api/compat/v1", data=body, headers=headers)

    for response in (selected_resp, wsgi_resp):
        assert dev_resp.status_code == response.status_code == 400
        assert dev_resp.headers.get("Content-Type") == response.headers.get("Content-Type")
        assert dev_resp.headers.get("Cache-Control") == response.headers.get("Cache-Control")
        assert dev_resp.data == response.data


def test_dev_vs_wsgi_compat_parity_minimal_valid_payload():
    selected_client, dev_client, wsgi_client = _clients()

    payload = json.dumps(_minimal_payload(), sort_keys=True)
    headers = {"Content-Type": "application/json; charset=utf-8"}

    dev_resp = dev_client.post("/api/compat/v1", data=payload, headers=headers)
    wsgi_resp = wsgi_client.post("/api/compat/v1", data=payload, headers=headers)
    selected_resp = selected_client.post("/api/compat/v1", data=payload, headers=headers)

    for response in (selected_resp, wsgi_resp):
        assert dev_resp.status_code == response.status_code == 200
        assert dev_resp.headers.get("Content-Type") == response.headers.get("Content-Type")
        assert dev_resp.headers.get("Cache-Control") == response.headers.get("Cache-Control")
        assert dev_resp.data == response.data
