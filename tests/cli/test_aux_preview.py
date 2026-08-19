from pathlib import Path

import pytest

from adapter.http_reader import app
from engine.cli import main as cli_main
from engine.narratives import emit_public_aux, get_pack
from engine.narratives import state as narrative_state
from engine.narratives.loader import load_pack
from engine.narratives.router import route_keys


DETERMINISM_PINS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
}


@pytest.fixture(autouse=True)
def _rails(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    for key, value in DETERMINISM_PINS.items():
        monkeypatch.setenv(key, value)
    monkeypatch.setattr(
        narrative_state,
        "_PACK",
        load_pack(Path("catalog/narratives"), tmp_path / "narratives"),
    )


def _find_suppressed_tuple():
    pack = get_pack()
    for key in pack.suppression_map:
        record = pack.keys.get(key)
        if record is None:
            continue
        perspective = record.perspective
        pack.primary_by_perspective[
            (record.category, record.band, perspective)
        ] = record
        routed = route_keys(record.category, record.band, perspective)
        lookup = "shared_key" if perspective == "shared" else "personal_key"
        if routed.get(lookup) != key:
            continue
        return {
            "category": record.category,
            "band": record.band,
            "perspective": perspective,
        }
    raise AssertionError("suppressed tuple not found")


def test_aux_preview_text_tuple_matches_aux(monkeypatch, capsys):
    monkeypatch.setenv("RELEASE_ID", "0" * 64)
    pack = get_pack()
    query = {
        "category": "harmony",
        "band": "Cool",
        "perspective": "shared",
    }

    exit_code = cli_main.cli(
        [
            "aux-preview",
            "--category",
            query["category"],
            "--band",
            query["band"],
            "--perspective",
            query["perspective"],
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 0

    emission = emit_public_aux(
        category=query["category"],
        band=query["band"],
        perspective=query["perspective"],
        viewer_top=None,
        flags=None,
        families_fired=(),
        release_id="0" * 64,
        pack_sha=pack.pack_sha,
    )
    assert not emission.suppressed
    expected_text = emission.body.decode("utf-8")
    assert captured.out == expected_text
    assert captured.err == ""
    assert expected_text.endswith("\n")
    assert "\x1b" not in expected_text

    client = app.test_client()
    resp = client.get(
        "/api/aux/narrative",
        query_string=query | {"v": "1"},
    )
    assert resp.status_code == 200
    assert resp.data.decode("utf-8") == expected_text


def test_aux_preview_suppressed_is_silent(monkeypatch, capsys):
    monkeypatch.setenv("RELEASE_ID", "0" * 64)
    pack = get_pack()
    suppressed_tuple = _find_suppressed_tuple()

    exit_code = cli_main.cli(
        [
            "aux-preview",
            "--category",
            suppressed_tuple["category"],
            "--band",
            suppressed_tuple["band"],
            "--perspective",
            suppressed_tuple["perspective"],
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == ""
    assert captured.err == ""

    emission = emit_public_aux(
        category=suppressed_tuple["category"],
        band=suppressed_tuple["band"],
        perspective=suppressed_tuple["perspective"],
        viewer_top=None,
        flags=None,
        families_fired=(),
        release_id="0" * 64,
        pack_sha=pack.pack_sha,
    )
    assert emission.suppressed
    assert emission.body == b""
