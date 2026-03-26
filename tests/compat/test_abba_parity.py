from __future__ import annotations

import json

from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1

PAIR = {
    "left": {"person_uid": "alice"},
    "right": {"person_uid": "bob"},
}


def _client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _payload(left: dict[str, str], right: dict[str, str]) -> bytes:
    weights = {category: 10 for category in CATEGORIES_ORDER_V1}
    body = {
        "a": left,
        "b": right,
        "viewer_prefs": {
            "top_category": CATEGORIES_ORDER_V1[0],
            "weights": weights,
        },
    }
    return json.dumps(body, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _post_compat(client, *, left: dict[str, str], right: dict[str, str]):
    return client.post(
        "/api/compat/v1",
        data=_payload(left, right),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )


def test_internal_compat_ab_ba_parity_is_canonical_bytes_identical(monkeypatch) -> None:
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.setenv("APP_ENV", "test")

    client = _client()
    ab = _post_compat(client, left=PAIR["left"], right=PAIR["right"])
    ba = _post_compat(client, left=PAIR["right"], right=PAIR["left"])

    assert ab.status_code == ba.status_code == 200
    assert ab.data.endswith(b"\n")
    assert ba.data.endswith(b"\n")
    assert b"\r\n" not in ab.data
    assert b"\r\n" not in ba.data
    assert ab.data == ba.data

    ab_payload = json.loads(ab.data)
    ba_payload = json.loads(ba.data)
    assert ab_payload == ba_payload
    assert set(ab_payload) == {"categories", "keys", "meta"}
