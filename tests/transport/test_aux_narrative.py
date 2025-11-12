import hashlib

import pytest

from adapter.http_reader import app
from engine.narratives import get_pack
from engine.narratives.router import route_keys

pytestmark = pytest.mark.epic010


def _find_suppressed_tuple() -> tuple[dict[str, str], str]:
    pack = get_pack()
    for key in pack.suppression_map:
        record = pack.keys.get(key)
        if record is None:
            continue
        if record.perspective == "shared":
            perspectives = ["shared"]
        else:
            perspectives = list(record.directions)
        for perspective in perspectives:
            routed = route_keys(record.category, record.band, perspective)
            lookup = "shared_key" if perspective == "shared" else "personal_key"
            target = routed.get(lookup)
            if target == key:
                return (
                    {
                        "category": record.category,
                        "band": record.band,
                        "perspective": perspective,
                    },
                    key,
                )
            if target == "missing_narrative_key":
                return (
                    {
                        "category": record.category,
                        "band": record.band,
                        "perspective": perspective,
                    },
                    "missing_narrative_key",
                )
    raise AssertionError("unable to locate suppressed tuple in narrative pack")


@pytest.mark.parametrize("path", ["/aux/narrative", "/api/aux/narrative"])
def test_aux_narrative_success_minimal_tuple(path):
    pack = get_pack()
    client = app.test_client()
    params = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "v": "1",
    }
    resp = client.get(path, query_string=params)
    assert resp.status_code == 200
    body = resp.data.decode("utf-8")
    assert body.endswith("\n")
    assert resp.headers.get("Content-Type") == "text/plain; charset=utf-8"
    vary = resp.headers.get("Vary", "")
    assert "authorization" in vary.lower()
    assert "accept-encoding" in vary.lower()
    assert resp.headers.get("X-Narrative-Pack-Sha") == pack.pack_sha
    assert resp.headers.get("X-Narrative-Composition", "").startswith("harmony.cool")
    expected_etag = "\"" + hashlib.sha256(resp.data).hexdigest() + "\""
    assert resp.headers.get("ETag") == expected_etag


def test_aux_narrative_tolerates_internal_parameters():
    pack = get_pack()
    client = app.test_client()
    base = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "v": "1",
    }
    minimal = client.get("/api/aux/narrative", query_string=base)
    assert minimal.status_code == 200

    extras = base | {
        "families_fired": ["compat_harmony"],
        "release_id": "0" * 64,
        "pack_sha": pack.pack_sha,
        "flags": ["demo"],
    }
    enriched = client.get("/api/aux/narrative", query_string=extras)
    assert enriched.status_code == 200
    assert enriched.data == minimal.data


def test_aux_narrative_suppressed_posture_public_surface():
    pack = get_pack()
    suppressed_tuple, expected_composition = _find_suppressed_tuple()
    client = app.test_client()
    query = {**suppressed_tuple, "v": "1"}

    canonical = client.get("/api/aux/narrative", query_string=query)
    alias = client.get("/aux/narrative", query_string=query)

    for resp in (canonical, alias):
        assert resp.status_code == 200
        assert resp.data == b""
        assert resp.headers.get("ETag") is None
        vary = resp.headers.get("Vary", "")
        assert "authorization" in vary.lower()
        assert "accept-encoding" in vary.lower()
        assert resp.headers.get("X-Narrative-Pack-Sha") == pack.pack_sha
        assert resp.headers.get("X-Narrative-Composition") == expected_composition
        assert "X-Narrative-Key" not in resp.headers
        policy_header = resp.headers.get("X-Narrative-Policy")
        assert policy_header in (None, "suppressed")

    assert canonical.data == alias.data
    assert list(canonical.headers.items()) == list(alias.headers.items())


def test_aux_narrative_alias_byte_identity_text_case():
    client = app.test_client()
    query = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
        "v": "1",
    }

    canonical = client.get("/api/aux/narrative", query_string=query)
    alias = client.get("/aux/narrative", query_string=query)

    assert canonical.status_code == alias.status_code == 200
    assert canonical.data == alias.data
    assert canonical.headers == alias.headers


@pytest.mark.parametrize("path", ["/aux/narrative", "/api/aux/narrative"])
@pytest.mark.parametrize("scenario", ["text", "suppressed"])
def test_aux_narrative_two_run_identity(path, scenario, monkeypatch):
    monkeypatch.setenv("LC_ALL", "C")
    monkeypatch.setenv("LANG", "C")
    monkeypatch.setenv("TZ", "UTC")

    client = app.test_client()

    if scenario == "text":
        query = {
            "category": "harmony",
            "band": "Cool",
            "perspective": "shared",
            "v": "1",
        }
    else:
        suppressed_tuple, _ = _find_suppressed_tuple()
        query = {**suppressed_tuple, "v": "1"}

    first = client.get(path, query_string=query)
    second = client.get(path, query_string=query)

    assert first.status_code == second.status_code == 200
    assert first.data == second.data

    vary = first.headers.get("Vary", "")
    assert "authorization" in vary.lower()
    assert "accept-encoding" in vary.lower()
    assert first.headers.get("Vary") == second.headers.get("Vary")
    assert first.headers.get("X-Narrative-Pack-Sha") == second.headers.get(
        "X-Narrative-Pack-Sha"
    )
    assert first.headers.get("X-Narrative-Composition") == second.headers.get(
        "X-Narrative-Composition"
    )

    if scenario == "text":
        assert first.headers.get("ETag")
        assert second.headers.get("ETag")
        assert first.headers.get("ETag") == second.headers.get("ETag")
    else:
        assert first.headers.get("ETag") is None
        assert second.headers.get("ETag") is None
