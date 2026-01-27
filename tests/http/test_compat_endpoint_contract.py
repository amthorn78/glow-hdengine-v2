import json
from pathlib import Path

from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1


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
