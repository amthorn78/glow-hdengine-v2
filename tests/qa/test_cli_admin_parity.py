import json
import pathlib

import pytest

from engine.cli.main import cli
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams

pytestmark = pytest.mark.epic006


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-parity-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-parity-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def _write_json(path: pathlib.Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, separators=(",", ":")) + "\n", encoding="utf-8")


def _run(pair: dict, outdir: pathlib.Path, capsys) -> dict[str, bytes]:
    pair_path = outdir / "pair.json"
    admin_dir = outdir / "admin"
    outdir.mkdir(parents=True, exist_ok=True)
    _write_json(pair_path, pair)
    exit_code = cli(["showcompat", "--pair-file", str(pair_path), "--dump-admin-dir", str(admin_dir)])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    files = {path.name: path.read_bytes() for path in sorted(admin_dir.glob("*.json"))}
    files["stdout"] = captured.out.encode("utf-8")
    return files


def test_admin_parity(tmp_path: pathlib.Path, capsys):
    left = complete_chart(UUID_A, GATES_A)
    right = complete_chart(UUID_B, GATES_B)

    files_ab = _run({"left": left, "right": right}, tmp_path / "ab", capsys)
    files_ba = _run({"left": right, "right": left}, tmp_path / "ba", capsys)

    assert files_ab.keys() == files_ba.keys()
    for name in files_ab:
        assert files_ab[name] == files_ba[name], name

    proof = json.loads(files_ab["pair.compat.proof.json"])
    assert [row["category_id"] for row in proof["categories"]] == [
        "harmony", "heat", "communication", "alignment", "comfort", "consistency", "expansion", "creativity", "drive", "balance",
    ]
    assert json.loads(files_ab["stdout"])["categories"] == proof["categories"]
