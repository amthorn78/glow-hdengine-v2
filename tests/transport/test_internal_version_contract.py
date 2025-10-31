import json
import os

import pytest

os.environ.setdefault("DATABASE_URL", "postgresql://example")

from adapter.http_reader import app

pytestmark = pytest.mark.epic006


def test_internal_version_invariants():
    client = app.test_client()
    get_resp = client.get("/internal/version")
    head_resp = client.head("/internal/version")
    cond_resp = client.get("/internal/version", headers={"If-None-Match": "xyz"})

    assert get_resp.status_code == head_resp.status_code == cond_resp.status_code == 200
    assert "no-store" in get_resp.headers.get("Cache-Control", "")
    assert "ETag" not in get_resp.headers
    assert head_resp.headers.get("Content-Type") == get_resp.headers.get("Content-Type")

    payload = json.loads(get_resp.data.decode("utf-8"))
    assert list(payload.keys()) == [
        "engine_tag",
        "release_id",
        "invocation_tag",
        "build_commit",
        "emitter_sha256",
    ]
