from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import jsonschema

from adapter.http_reader import create_app
from engine.compat.categories import CATEGORIES_ORDER_V1
from tests.support.pr04_fixtures import (
    GATES_A,
    GATES_B,
    UUID_A,
    UUID_B,
    build_bundle,
    build_pack,
    complete_chart,
    inject_seams,
)

SCHEMA = json.loads(Path("schemas/magic10_compat_result_v1.schema.json").read_text(encoding="utf-8"))


def _client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def _payload(left: dict[str, Any], right: dict[str, Any]) -> bytes:
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


def _post_compat(client, *, left: dict[str, Any], right: dict[str, Any]):
    return client.post(
        "/api/compat/v1",
        data=_payload(left, right),
        headers={"Content-Type": "application/json; charset=utf-8"},
    )


def test_internal_compat_ab_ba_parity_is_canonical_bytes_identical(monkeypatch, tmp_path) -> None:
    # Seam inputs: complete mapped charts under canonical UUID identities. Legacy
    # ``person_uid`` aliases are refused at the boundary (PF05 §5.2.3
    # ``ERR_M10_LEGACY_INPUT_UNSUPPORTED``); the subject here is AB/BA canonical
    # byte identity, not the legacy input path.
    inject_seams(monkeypatch, build_bundle(tmp_path), build_pack(tmp_path))
    left = complete_chart(UUID_A, GATES_A)
    right = complete_chart(UUID_B, GATES_B)

    client = _client()
    ab = _post_compat(client, left=left, right=right)
    ba = _post_compat(client, left=right, right=left)

    assert ab.status_code == ba.status_code == 200
    assert ab.data.endswith(b"\n")
    assert ba.data.endswith(b"\n")
    assert b"\r\n" not in ab.data
    assert b"\r\n" not in ba.data
    assert ab.data == ba.data

    ab_payload = json.loads(ab.data)
    ba_payload = json.loads(ba.data)
    assert ab_payload == ba_payload
    # The switched handler emits the canonical magic10 compat result, not the
    # legacy ``{categories, keys, meta}`` envelope; bind the shape to its schema.
    assert set(ab_payload) == {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}
    assert ab_payload["schema"] == "magic10_compat_result.v1"
    jsonschema.validate(instance=ab_payload, schema=SCHEMA)
    jsonschema.validate(instance=ba_payload, schema=SCHEMA)
