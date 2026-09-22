import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import sysconfig

import pytest

from engine.serializer.canon import sercanon
from engine.presenter import emitter
from engine.cli.main import cli
from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, FakeCurrentViewDB, build_bundle, build_pack, complete_chart, inject_seams

pytestmark = pytest.mark.epic006

REPO_ROOT = Path(__file__).resolve().parents[2]
PAIR = json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}, separators=(",", ":"))
CONJUNCTION_PAIR = json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}, separators=(",", ":"))


@pytest.fixture(scope="module")
def bundle(tmp_path_factory):
    return build_bundle(tmp_path_factory.mktemp("pr04-canon-bundle"))


@pytest.fixture(scope="module")
def pack(tmp_path_factory):
    return build_pack(tmp_path_factory.mktemp("pr04-canon-pack"))


@pytest.fixture(autouse=True)
def _seams(monkeypatch, bundle, pack):
    inject_seams(monkeypatch, bundle, pack)


def _cli_env() -> dict[str, str]:
    env = os.environ.copy()
    scripts_dir = sysconfig.get_paths()["scripts"]
    env["PATH"] = f"{scripts_dir}:{env.get('PATH', '')}"
    env.update({"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"})
    return env


def _assert_canonical_bytes(data: bytes) -> dict:
    assert data.endswith(b"\n") and b"\n\n" not in data
    assert b"\r\n" not in data
    payload = json.loads(data)
    assert sercanon(payload) == data
    return payload


def _run_in_process(monkeypatch, capsys, args: list[str], *, stdin: str | None = None) -> tuple[int, bytes, str]:
    if stdin is not None:
        monkeypatch.setattr(sys, "stdin", io.StringIO(stdin))
    exit_code = cli(args)
    captured = capsys.readouterr()
    return exit_code, captured.out.encode("utf-8"), captured.err


def _run_hdctl(args: list[str], *, stdin: bytes | None = None, cwd: os.PathLike[str] | None = None) -> subprocess.CompletedProcess:
    base = [sys.executable, str(REPO_ROOT / "scripts/hdctl.py")]
    return subprocess.run(base + args, input=stdin, capture_output=True, env=_cli_env(), cwd=cwd)


def test_showcompat_stdout_is_canonical(monkeypatch, capsys):
    exit_code, stdout, stderr = _run_in_process(monkeypatch, capsys, ["showcompat"], stdin=PAIR + "\n")
    assert exit_code == 0, stderr
    assert stderr == ""
    payload = _assert_canonical_bytes(stdout)
    assert stdout == emitter.emit_public(payload)
    assert set(payload) == {"schema", "config_id", "release_id", "pair_key", "signals", "categories"}
    assert payload["schema"] == "magic10_compat_result.v1"
    assert len(payload["release_id"]) == 64


def test_reader_dump_and_admin_sidecars_are_canonical(monkeypatch, capsys, tmp_path: Path):
    pair_path = tmp_path / "pair.json"
    pair_path.write_text(PAIR + "\n", encoding="utf-8")
    reader_path = tmp_path / "reader.json"
    admin_dir = tmp_path / "admin"

    exit_code, stdout, stderr = _run_in_process(
        monkeypatch,
        capsys,
        ["showcompat", "--pair-file", str(pair_path), "--dump-reader", str(reader_path), "--dump-admin-dir", str(admin_dir)],
    )
    assert exit_code == 0, stderr
    assert stderr == ""
    _assert_canonical_bytes(stdout)
    envelope = _assert_canonical_bytes(reader_path.read_bytes())
    assert list(envelope) == ["categories", "eligible", "idempotence_hash", "meta", "reader_version", "release_id"]
    assert envelope["eligible"] is True and envelope["categories"] == [{"band": envelope["categories"][0]["band"], "id": "harmony"}]

    produced = sorted(admin_dir.glob("*"))
    assert produced, "expected admin dumps to be written"
    for path in produced:
        if path.suffix == ".sha256":
            assert path.read_text(encoding="utf-8").endswith("\n")
            continue
        _assert_canonical_bytes(path.read_bytes())


def test_aux_preview_admin_out_is_canonical(tmp_path: Path):
    runtime_root = tmp_path / "runtime"
    shutil.copytree(REPO_ROOT / "catalog" / "narratives", runtime_root / "catalog" / "narratives")
    admin_out = tmp_path / "aux_admin.json"
    result = _run_hdctl(
        ["aux-preview", "--category", "harmony", "--band", "Cool", "--perspective", "shared", "--admin-out", str(admin_out)],
        cwd=runtime_root,
    )
    assert result.returncode == 0
    assert result.stderr == b""
    assert (runtime_root / "narratives").is_dir()
    _assert_canonical_bytes(admin_out.read_bytes())


def test_showcompat_conjunction_stdout_is_canonical(monkeypatch, capsys):
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: pytest.fail("complete charts need no DB"))
    exit_code, stdout, stderr = _run_in_process(monkeypatch, capsys, ["showcompat", "--conjunction"], stdin=CONJUNCTION_PAIR + "\n")
    assert exit_code == 0, stderr
    assert stderr == ""
    payload = _assert_canonical_bytes(stdout)
    assert stdout == emitter.emit_public(payload)
    assert set(payload) == {"conjunction"}
    assert set(payload["conjunction"]) == {"left", "right", "compat"}
    assert payload["conjunction"]["left"] == {"person_uid": UUID_A}
    assert payload["conjunction"]["right"] == {"person_uid": UUID_B}


def test_showcompat_conjunction_closed_rails_refuses_when_local_missing(monkeypatch, capsys):
    monkeypatch.setattr("engine.cli.main.DBAccess.for_current_env", lambda *a, **k: FakeCurrentViewDB({}))
    exit_code = cli(["showcompat", "--conjunction", "--user-a", "missing-left", "--user-b", "missing-right"])
    captured = capsys.readouterr()
    assert exit_code == 1
    assert captured.out == ""
    assert captured.err == "PROVIDER_REFUSED\n"


def test_showcompat_subprocess_usage_error_is_stderr_only():
    result = _run_hdctl(["showcompat", "--pair-file", "no_such.json"])
    assert result.returncode == 64
    assert result.stdout == b""
    assert result.stderr.endswith(b"\n")
