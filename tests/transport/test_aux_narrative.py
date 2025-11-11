import hashlib

import pytest

from adapter.http_reader import app
from engine.narratives import get_pack

pytestmark = pytest.mark.epic010


@pytest.mark.parametrize("path", ["/aux/narrative", "/api/aux/narrative"])
def test_aux_narrative_success(path):
    pack = get_pack()
    client = app.test_client()
    params = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "families_fired": "compat_harmony",
        "release_id": "0" * 64,
        "pack_sha": pack.pack_sha,
        "v": "1",
    }
    resp = client.get(path, query_string=params)
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


def test_aux_narrative_suppressed_posture_and_alias():
    pack = get_pack()
    client = app.test_client()
    params = [
        ("category", "harmony"),
        ("band", "Cool"),
        ("perspective", "shared"),
        ("families_fired", "z"),
        ("families_fired", "a"),
        ("release_id", "0" * 64),
        ("pack_sha", pack.pack_sha),
        ("v", "1"),
    ]

    canonical = client.get("/api/aux/narrative", query_string=params)
    alias = client.get("/aux/narrative", query_string=params)

    for resp in (canonical, alias):
        assert resp.status_code == 200
        assert resp.data == b""
        assert "ETag" not in resp.headers
        policy_header = resp.headers.get("X-Narrative-Policy")
        assert policy_header in (None, "suppressed")
        assert resp.headers.get("X-Narrative-Pack-Sha") == pack.pack_sha
        composition_header = resp.headers.get("X-Narrative-Composition")
        assert composition_header

    assert canonical.data == alias.data
    assert list(canonical.headers.items()) == list(alias.headers.items())
    assert canonical.headers.get("X-Narrative-Composition") == alias.headers.get(
        "X-Narrative-Composition"
    )


def test_aux_narrative_alias_byte_identity():
    pack = get_pack()
    client = app.test_client()
    params = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "families_fired": "compat_harmony",
        "release_id": "0" * 64,
        "pack_sha": pack.pack_sha,
        "v": "1",
    }

    canonical = client.get("/api/aux/narrative", query_string=params)
    alias = client.get("/aux/narrative", query_string=params)

    assert canonical.status_code == alias.status_code == 200
    assert canonical.data == alias.data
    for header in [
        "Content-Type",
        "ETag",
        "Vary",
        "X-Narrative-Pack-Sha",
        "X-Narrative-Composition",
    ]:
        assert canonical.headers.get(header) == alias.headers.get(header)


@pytest.mark.parametrize("path", ["/aux/narrative", "/api/aux/narrative"])
@pytest.mark.parametrize("scenario", ["text", "suppressed"])
def test_aux_narrative_two_run_identity(path, scenario, monkeypatch):
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")

    pack = get_pack()
    client = app.test_client()

    if scenario == "text":
        query = {
            "category": "harmony",
            "band": "Cool",
            "perspective": "shared",
            "families_fired": "compat_harmony",
            "release_id": "0" * 64,
            "pack_sha": pack.pack_sha,
            "v": "1",
        }
    else:
        query = [
            ("category", "harmony"),
            ("band", "Cool"),
            ("perspective", "shared"),
            ("families_fired", "z"),
            ("families_fired", "a"),
            ("release_id", "0" * 64),
            ("pack_sha", pack.pack_sha),
            ("v", "1"),
        ]

    first = client.get(path, query_string=query)
    second = client.get(path, query_string=query)

    assert first.status_code == second.status_code == 200
    assert first.data == second.data

    headers = [
        "Content-Type",
        "Vary",
        "X-Narrative-Pack-Sha",
        "X-Narrative-Composition",
    ]

    if scenario == "text":
        headers.append("ETag")
        assert first.headers.get("ETag")
        assert second.headers.get("ETag")
    else:
        assert "ETag" not in first.headers
        assert "ETag" not in second.headers

    for header in headers:
        assert first.headers.get(header) == second.headers.get(header)
