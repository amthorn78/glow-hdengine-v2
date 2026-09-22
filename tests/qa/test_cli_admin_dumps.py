import hashlib
import json
import pathlib
import stat

import pytest

from engine.cli.main import cli
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, build_bundle, build_pack, complete_chart, inject_seams

pytestmark = pytest.mark.epic006


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-admin-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-admin-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def _write_json(path: pathlib.Path, obj: dict) -> None:
    path.write_text(json.dumps(obj, separators=(",", ":")) + "\n", encoding="utf-8")


def _sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _assert_mode_0600(path: pathlib.Path) -> None:
    mode = stat.S_IMODE(path.stat().st_mode)
    assert mode == 0o600


def test_file_inputs_and_admin_dumps(tmp_path: pathlib.Path, capsys):
    left = complete_chart(UUID_A, GATES_A)
    right = complete_chart(UUID_B, GATES_B)
    pair_path = tmp_path / "pair.json"
    reader_path = tmp_path / "reader.json"
    admin_dir = tmp_path / "admin"
    _write_json(pair_path, {"left": left, "right": right})

    exit_code = cli(["showcompat", "--pair-file", str(pair_path), "--dump-reader", str(reader_path), "--dump-admin-dir", str(admin_dir)])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    out = captured.out
    assert out.endswith("\n") and "\n\n" not in out
    result = json.loads(out)

    reader_raw = reader_path.read_text(encoding="utf-8")
    assert reader_raw.endswith("\n") and "\n\n" not in reader_raw
    envelope = json.loads(reader_raw)
    assert set(envelope) == {"reader_version", "eligible", "categories", "meta", "release_id", "idempotence_hash"}
    assert envelope["eligible"] is True
    harmony = next(row for row in result["categories"] if row["category_id"] == "harmony")
    assert envelope["categories"] == [{"band": harmony["band"], "id": "harmony"}]
    assert envelope["release_id"] == result["release_id"]
    for forbidden in ("score", "pair_key", "signals", "gates", "shared_key", UUID_A):
        assert forbidden not in reader_raw

    expected_names = {
        "pair.left.bodygraph.json",
        "pair.right.bodygraph.json",
        "pair.composite.bodygraph.json",
        "pair.compat.proof.json",
    }
    dumped = {p.name for p in admin_dir.glob("*.json")}
    assert expected_names == dumped

    for name in expected_names:
        json_path = admin_dir / name
        sha_path = admin_dir / f"{name}.sha256"
        assert sha_path.exists()
        _assert_mode_0600(json_path)
        _assert_mode_0600(sha_path)
        assert _sha256(json_path) == sha_path.read_text(encoding="utf-8").strip()

    proof = json.loads((admin_dir / "pair.compat.proof.json").read_text(encoding="utf-8"))
    assert proof["schema"] == "magic10_compat_result.v1"
    assert proof["categories"] == result["categories"]
    assert proof["signals"] == result["signals"]
    assert proof["pair_key"] == result["pair_key"] and proof["release_id"] == result["release_id"]
    assert proof["thresholds"]["edges"] == [24, 49, 74, 100]
    assert "constants" not in proof and "overall" not in proof

    composite = json.loads((admin_dir / "pair.composite.bodygraph.json").read_text(encoding="utf-8"))
    assert composite["eligible"] is True
    assert {composite["left_person_uid"], composite["right_person_uid"]} == {UUID_A, UUID_B}
    assert composite["pair_key"] == result["pair_key"]
    left_dump = json.loads((admin_dir / "pair.left.bodygraph.json").read_text(encoding="utf-8"))
    assert set(left_dump) == {"bodygraph", "person", "person_uid"}
    assert left_dump["person_uid"] == composite["left_person_uid"]
    assert left_dump["bodygraph"]["gates"] == sorted(left_dump["bodygraph"]["gates"])
    assert all(isinstance(gate, int) for gate in left_dump["bodygraph"]["gates"])


def test_self_pair_admin_dumps_carry_no_result(tmp_path: pathlib.Path, capsys):
    pair_path = tmp_path / "pair.json"
    admin_dir = tmp_path / "admin"
    reader_path = tmp_path / "reader.json"
    _write_json(pair_path, {"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_A, GATES_A)})
    exit_code = cli(["showcompat", "--pair-file", str(pair_path), "--dump-reader", str(reader_path), "--dump-admin-dir", str(admin_dir)])
    captured = capsys.readouterr()
    assert exit_code == 0, captured.err
    assert json.loads(captured.out) == {"categories": [], "eligible": False}
    envelope = json.loads(reader_path.read_text(encoding="utf-8"))
    assert envelope["eligible"] is False and envelope["categories"] == []
    proof = json.loads((admin_dir / "pair.compat.proof.json").read_text(encoding="utf-8"))
    assert proof == {"eligible": False, "categories": [], "signals": []}
    composite = json.loads((admin_dir / "pair.composite.bodygraph.json").read_text(encoding="utf-8"))
    assert composite == {"eligible": False, "left_person_uid": UUID_A, "right_person_uid": UUID_A}
