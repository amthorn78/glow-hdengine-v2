from __future__ import annotations
import json, os, re, shutil, subprocess, sys
from pathlib import Path
from typing import Tuple

A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"

HEX64 = re.compile(r"^[0-9a-f]{64}$")

def _run(*argv: str) -> Tuple[int, bytes, bytes]:
    p = subprocess.run([sys.executable, "scripts/hd_cli.py", *argv],
                       capture_output=True)
    return p.returncode, p.stdout, p.stderr

def _parse_release_id(stdout: bytes) -> str:
    obj = json.loads(stdout.decode("utf-8"))
    return obj["release_id"]

def test_release_id_env_precedence_over_file(tmp_path: Path, monkeypatch):
    art_dir = Path("artifacts"); art_dir.mkdir(parents=True, exist_ok=True)
    rid_file = art_dir / "release_id.txt"

    backup = None
    if rid_file.exists():
        backup = tmp_path / "release_id.bak"
        shutil.copy2(rid_file, backup)

    try:
        rid_file.write_text("0"*64 + "\n", encoding="utf-8")  # file value (should be ignored)
        env_rid = "1"*64
        monkeypatch.setenv("RELEASE_ID", env_rid)

        rc, out, err = _run(A, B)
        assert rc == 0 and err == b""
        rid = _parse_release_id(out)
        assert rid == env_rid and HEX64.match(rid)
    finally:
        if backup and backup.exists():
            shutil.copy2(backup, rid_file)
        elif rid_file.exists():
            rid_file.unlink()

def test_release_id_file_used_when_env_missing(tmp_path: Path, monkeypatch):
    art_dir = Path("artifacts"); art_dir.mkdir(parents=True, exist_ok=True)
    rid_file = art_dir / "release_id.txt"

    backup = None
    if rid_file.exists():
        backup = tmp_path / "release_id.bak"
        shutil.copy2(rid_file, backup)

    try:
        monkeypatch.delenv("RELEASE_ID", raising=False)
        file_rid = "2"*64
        rid_file.write_text(file_rid + "\n", encoding="utf-8")

        rc, out, err = _run(A, B)
        assert rc == 0 and err == b""
        rid = _parse_release_id(out)
        assert rid == file_rid and HEX64.match(rid)
    finally:
        if backup and backup.exists():
            shutil.copy2(backup, rid_file)
        elif rid_file.exists():
            rid_file.unlink()

def test_no_rel_dev_literal_in_cli_emit_path():
    # Grep-guard scoped to the public CLI emit path only.
    cli_text = Path("scripts/hd_cli.py").read_text(encoding="utf-8", errors="replace")
    assert "rel_dev" not in cli_text, "public CLI emit path must not include 'rel_dev'"