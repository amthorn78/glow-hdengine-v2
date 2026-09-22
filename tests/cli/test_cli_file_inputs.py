import hashlib
import json
import os
import pathlib
import subprocess
import sysconfig

import pytest

from engine.cli.main import cli
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams

pytestmark = pytest.mark.epic006


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-files-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-files-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: pytest.fail("file mode must not touch the DB"))
    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **k: pytest.fail("file mode must not touch the vendor"))


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    env.update({"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    return env


def _write_json(path: pathlib.Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, separators=(",", ":")) + "\n", encoding="utf-8")


def _sha(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def test_pair_file_and_ab_file_modes(tmp_path: pathlib.Path, capsys):
    a = complete_chart(UUID_A, GATES_A)
    b = complete_chart(UUID_B, GATES_B)
    pa, pb, pp = tmp_path / "A.json", tmp_path / "B.json", tmp_path / "pair.json"
    _write_json(pa, a)
    _write_json(pb, b)
    _write_json(pp, {"left": a, "right": b})

    outputs = []
    for args in (
        ["showcompat", "--pair-file", str(pp)],
        ["showcompat", "--a-file", str(pa), "--b-file", str(pb)],
        ["showcompat", "--a-file", str(pb), "--b-file", str(pa)],
        ["showcompat", "--a", str(pa), "--b", str(pb)],
    ):
        exit_code = cli(args)
        captured = capsys.readouterr()
        assert exit_code == 0, captured.err
        assert captured.err == ""
        out = captured.out
        assert out.endswith("\n") and "\n\n" not in out
        obj = json.loads(out)
        assert obj["schema"] == "magic10_compat_result.v1"
        assert isinstance(obj["categories"], list) and len(obj["categories"]) == 10
        assert not any(key in obj for key in ("a", "b", "viewer_prefs", "compat", "meta"))
        outputs.append(out)
    assert len({_sha(out) for out in outputs}) == 1


def test_birth_only_file_input_is_legacy_unsupported(tmp_path: pathlib.Path, capsys):
    a = {"birthdate": "1990-01-10", "birthtime": "14:05", "location": "Chicago, US"}
    b = {"birthdate": "1992-03-04", "birthtime": "08:15", "location": "Berlin, DE"}
    pp = tmp_path / "pair.json"
    _write_json(pp, {"left": a, "right": b})
    exit_code = cli(["showcompat", "--pair-file", str(pp)])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "ERR_M10_LEGACY_INPUT_UNSUPPORTED\n"
    # The installed console script refuses the same way with no repository state.
    result = subprocess.run(["hdctl", "showcompat", "--pair-file", str(pp)], capture_output=True, text=True, env=_cli_env())
    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr == "ERR_M10_LEGACY_INPUT_UNSUPPORTED\n"


def test_type_only_and_empty_gate_fixtures_are_negative_cases(tmp_path: pathlib.Path, capsys):
    pp = tmp_path / "pair.json"
    _write_json(pp, {"left": {"person_uid": UUID_A, "mechanics": {"type": "Generator"}}, "right": complete_chart(UUID_B, GATES_B)})
    assert cli(["showcompat", "--pair-file", str(pp)]) == 1
    assert capsys.readouterr().err == "ERR_M10_LEGACY_INPUT_UNSUPPORTED\n"
    _write_json(pp, {"left": complete_chart(UUID_A, []), "right": complete_chart(UUID_B, GATES_B)})
    assert cli(["showcompat", "--pair-file", str(pp)]) == 1
    assert capsys.readouterr().err == "ERR_READER_MISSING_PARAM\n"
    _write_json(pp, {"left": complete_chart(UUID_A, ["10", "010"]), "right": complete_chart(UUID_B, GATES_B)})
    assert cli(["showcompat", "--pair-file", str(pp)]) == 1
    assert capsys.readouterr().err == "ERR_READER_INVALID_CHART\n"
