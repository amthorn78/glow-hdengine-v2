import json
from pathlib import Path

import pytest

from adapter.http_reader import app
from engine.cli import main as cli_main
from engine.narratives import emit_public_aux, get_pack
from engine.narratives import state as narrative_state
from engine.narratives.loader import load_pack


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


def test_aux_preview_missing_mapping_is_silent(monkeypatch, capsys):
    monkeypatch.setenv("RELEASE_ID", "0" * 64)
    pack = get_pack()
    missing_tuple = {
        "category": "unknown",
        "band": "Cool",
        "perspective": "shared",
    }

    exit_code = cli_main.cli(
        [
            "aux-preview",
            "--category",
            missing_tuple["category"],
            "--band",
            missing_tuple["band"],
            "--perspective",
            missing_tuple["perspective"],
        ]
    )
    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out == ""
    assert captured.err == ""

    emission = emit_public_aux(
        category=missing_tuple["category"],
        band=missing_tuple["band"],
        perspective=missing_tuple["perspective"],
        viewer_top=None,
        flags=None,
        families_fired=(),
        release_id="0" * 64,
        pack_sha=pack.pack_sha,
    )
    assert emission.suppressed
    assert emission.body == b""


# HDE-CRD-0002 WU-PR-04 (S08): --band applies to --pair-file input.


def _pair_file(tmp_path: Path, band: str = "Cool") -> Path:
    path = tmp_path / "pair.json"
    path.write_text(json.dumps({"categories": [{"category_id": "harmony", "band": band}], "release_id": "1" * 64}), encoding="utf-8")
    return path


def _expected(category: str, band: str, perspective: str = "shared"):
    return emit_public_aux(
        category=category, band=band, perspective=perspective, viewer_top=None, flags=None,
        families_fired=(), release_id="1" * 64, pack_sha=get_pack().pack_sha,
    )


@pytest.mark.parametrize("band", ["Cool", "Open", "Warm", "Glow"])
def test_aux_preview_pair_file_band_flag_selects_the_flagged_band(capsys, tmp_path, band):
    pair = _pair_file(tmp_path, band="Cool")
    admin = tmp_path / "admin.json"
    exit_code = cli_main.cli(["aux-preview", "--pair-file", str(pair), "--category", "harmony", "--band", band, "--show-narrative", "--admin-out", str(admin)])
    captured = capsys.readouterr()
    assert exit_code == 0 and captured.err == ""
    expected = _expected("harmony", band)
    assert captured.out == expected.body.decode("utf-8")
    sidecar = json.loads(admin.read_text(encoding="utf-8"))
    assert sidecar["key"] == expected.key and sidecar["release_id"] == "1" * 64


def test_aux_preview_pair_file_without_band_flag_uses_the_file_band(capsys, tmp_path):
    pair = _pair_file(tmp_path, band="Warm")
    assert cli_main.cli(["aux-preview", "--pair-file", str(pair), "--show-narrative"]) == 0
    assert capsys.readouterr().out == _expected("harmony", "Warm").body.decode("utf-8")


def test_aux_preview_pair_file_band_flag_keeps_category_refusals(capsys, tmp_path):
    pair = _pair_file(tmp_path)
    assert cli_main.cli(["aux-preview", "--pair-file", str(pair), "--category", "balance", "--band", "Glow", "--show-narrative"]) == 64
    assert capsys.readouterr() == ("", "MISSING_COMPAT_CATEGORY\n")
    empty = tmp_path / "empty.json"
    empty.write_text('{"categories": []}', encoding="utf-8")
    assert cli_main.cli(["aux-preview", "--pair-file", str(empty), "--band", "Glow"]) == 64
    assert capsys.readouterr() == ("", "MISSING_COMPAT_CATEGORY\n")
    bad = tmp_path / "bad.json"
    bad.write_text('{"conjunction": {"compat": 1}}', encoding="utf-8")
    assert cli_main.cli(["aux-preview", "--pair-file", str(bad), "--band", "Glow"]) == 64
    assert capsys.readouterr() == ("", "INVALID_COMPAT_INPUT\n")


def test_aux_preview_pair_file_band_flag_without_show_narrative_emits_nothing(capsys, tmp_path):
    pair = _pair_file(tmp_path)
    assert cli_main.cli(["aux-preview", "--pair-file", str(pair), "--band", "Glow"]) == 0
    assert capsys.readouterr() == ("", "")
