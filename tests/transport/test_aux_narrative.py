import hashlib
import json
import shutil
from pathlib import Path

import pytest

from adapter.http_reader import app
from engine.narratives import MISSING_NARRATIVE_KEY, get_pack
from engine.narratives import state as narrative_state
from engine.narratives.loader import load_pack
from engine.narratives.router import route_keys
from engine.serializer.canon import sercanon

pytestmark = pytest.mark.epic010
ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture(autouse=True)
def _isolated_current_pack(tmp_path: Path, monkeypatch: pytest.MonkeyPatch):
    pack = load_pack(ROOT / "catalog/narratives", tmp_path / "mounted")
    monkeypatch.setattr(narrative_state, "_PACK", pack)
    return pack


def _load_pack_with_suppressed_shared_slots(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    slots: set[int],
):
    catalog = tmp_path / "sealed" / "catalog" / "narratives"
    shutil.copytree(ROOT / "catalog/narratives", catalog)

    current = get_pack()
    query = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
    }
    suppressed = {
        record.key
        for record in current.keys.values()
        if record.category_slug == query["category"]
        and record.band == query["band"]
        and record.perspective == query["perspective"]
        and record.slot in slots
    }
    assert len(suppressed) == len(slots)

    suppression_path = catalog / "suppression_map.json"
    suppression = json.loads(suppression_path.read_bytes())
    suppression.update(
        {
            key: {
                "notes": "test-only sealed suppression",
                "policy_reason": "conflict",
            }
            for key in suppressed
        }
    )
    suppression_bytes = sercanon(suppression, sort_keys=True)
    suppression_path.write_bytes(suppression_bytes)
    suppression_sha = hashlib.sha256(suppression_bytes).hexdigest()
    suppression_path.with_suffix(".json.sha256").write_text(
        f"{suppression_sha}\n", encoding="utf-8"
    )

    manifest_path = catalog / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    entry = next(
        item
        for item in manifest["files"]
        if item["path"] == "catalog/narratives/suppression_map.json"
    )
    entry.update(sha256=suppression_sha, size_bytes=len(suppression_bytes))
    manifest_bytes = sercanon(manifest, sort_keys=True)
    manifest_path.write_bytes(manifest_bytes)
    manifest_path.with_suffix(".json.sha256").write_text(
        f"{hashlib.sha256(manifest_bytes).hexdigest()}\n", encoding="utf-8"
    )

    pack = load_pack(catalog, tmp_path / "suppressed-mounted")
    assert pack.mount_path.is_relative_to(tmp_path)
    monkeypatch.setattr(narrative_state, "_PACK", pack)
    return pack, query


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
    assert resp.headers.get("X-Narrative-Composition", "").startswith(
        "nar.harmony.cool"
    )
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


def test_aux_narrative_catalog_suppression_falls_forward(
    tmp_path, monkeypatch
):
    pack, query = _load_pack_with_suppressed_shared_slots(
        tmp_path, monkeypatch, {1, 2}
    )
    expected = route_keys(**query)["shared_key"]
    assert expected.endswith(".3.sage-01")

    response = app.test_client().get(
        "/api/aux/narrative", query_string={**query, "v": "1"}
    )
    assert response.status_code == 200
    assert response.data
    assert response.headers.get("X-Narrative-Pack-Sha") == pack.pack_sha
    assert response.headers.get("X-Narrative-Composition") == expected


def test_aux_narrative_suppressed_posture_public_surface(tmp_path, monkeypatch):
    pack, suppressed_tuple = _load_pack_with_suppressed_shared_slots(
        tmp_path, monkeypatch, {1, 2, 3}
    )
    assert route_keys(**suppressed_tuple)["shared_key"] == MISSING_NARRATIVE_KEY
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
        assert resp.headers.get("X-Narrative-Composition") == MISSING_NARRATIVE_KEY
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
def test_aux_narrative_two_run_identity(path, scenario, tmp_path, monkeypatch):
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
        _, suppressed_tuple = _load_pack_with_suppressed_shared_slots(
            tmp_path, monkeypatch, {1, 2, 3}
        )
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
