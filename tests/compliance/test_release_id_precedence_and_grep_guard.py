from __future__ import annotations
import json, os, re, subprocess, sys
from pathlib import Path
from typing import Tuple

ROOT = Path(__file__).resolve().parents[2]
CLI = ROOT / "scripts" / "hd_cli.py"
A = ROOT / "tests/fixtures/reader_v1/abba_A.json"
B = ROOT / "tests/fixtures/reader_v1/abba_B.json"

HEX64 = re.compile(r"^[0-9a-f]{64}$")

def _run(cwd: Path, *argv: str) -> Tuple[int, bytes, bytes]:
    # hd_cli.py resolves the relative path artifacts/release_id.txt against its
    # working directory, so each run uses a private one and the tracked
    # artifacts/release_id.txt is never written.
    env = dict(os.environ)
    env["PYTHONPATH"] = os.pathsep.join(p for p in (str(ROOT), env.get("PYTHONPATH", "")) if p)
    p = subprocess.run([sys.executable, str(CLI), *argv],
                       capture_output=True, cwd=cwd, env=env)
    return p.returncode, p.stdout, p.stderr

def _parse_release_id(stdout: bytes) -> str:
    obj = json.loads(stdout.decode("utf-8"))
    return obj["release_id"]

def _rid_file(cwd: Path) -> Path:
    art_dir = cwd / "artifacts"; art_dir.mkdir(parents=True, exist_ok=True)
    return art_dir / "release_id.txt"

def test_release_id_env_precedence_over_file(tmp_path: Path, monkeypatch):
    _rid_file(tmp_path).write_text("0"*64 + "\n", encoding="utf-8")  # file value (should be ignored)
    env_rid = "1"*64
    monkeypatch.setenv("RELEASE_ID", env_rid)

    rc, out, err = _run(tmp_path, str(A), str(B))
    assert rc == 0 and err == b""
    rid = _parse_release_id(out)
    assert rid == env_rid and HEX64.match(rid)

def test_release_id_file_used_when_env_missing(tmp_path: Path, monkeypatch):
    monkeypatch.delenv("RELEASE_ID", raising=False)
    file_rid = "2"*64
    _rid_file(tmp_path).write_text(file_rid + "\n", encoding="utf-8")

    rc, out, err = _run(tmp_path, str(A), str(B))
    assert rc == 0 and err == b""
    rid = _parse_release_id(out)
    assert rid == file_rid and HEX64.match(rid)

def test_no_rel_dev_literal_in_cli_emit_path():
    # Grep-guard scoped to the public CLI emit path only.
    cli_text = CLI.read_text(encoding="utf-8", errors="replace")
    assert "rel_dev" not in cli_text, "public CLI emit path must not include 'rel_dev'"
