import hashlib

import pytest

from adapter.http_reader import app
from engine.narratives import get_pack

pytestmark = pytest.mark.epic010


def test_aux_narrative_success():
    pack = get_pack()
    client = app.test_client()
    params = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "families_fired": "compat_harmony",
        "release_id": "0" * 64,
        "pack_sha": pack.pack_sha,
    }
    resp = client.get("/aux/narrative", query_string=params)
    assert resp.status_code == 200
    body = resp.data.decode("utf-8")
    assert body.endswith("\n")
    assert resp.headers.get("Content-Type") == "text/plain; charset=utf-8"
    assert resp.headers.get("ETag")
    assert "Authorization" in resp.headers.get("Vary", "")
    assert resp.headers.get("X-Narrative-Pack-Sha") == pack.pack_sha
    assert resp.headers.get("X-Narrative-Composition", "").startswith("harmony.cool")
    expected_etag = "\"" + hashlib.sha256(resp.data).hexdigest() + "\""
    assert resp.headers.get("ETag") == expected_etag


def test_aux_narrative_suppressed_unsorted_families():
    pack = get_pack()
    client = app.test_client()
    params = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "families_fired": ["z", "a"],
        "release_id": "0" * 64,
        "pack_sha": pack.pack_sha,
    }
    resp = client.get("/aux/narrative", query_string=params)
    assert resp.status_code == 200
    assert resp.data == b""
    assert "ETag" not in resp.headers
    assert resp.headers.get("X-Narrative-Policy") == "invalid_families"
    assert resp.headers.get("X-Narrative-Pack-Sha") == pack.pack_sha
