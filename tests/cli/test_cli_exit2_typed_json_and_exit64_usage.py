from __future__ import annotations
import subprocess, sys, json
from pathlib import Path

A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"

def _run(*argv: str) -> tuple[int, bytes, bytes]:
    p = subprocess.run([sys.executable, "scripts/hd_cli.py", *argv], capture_output=True)
    return p.returncode, p.stdout, p.stderr

def test_help_is_exit64_one_line_lf_and_mentions_two_positionals():
    rc, out, err = _run("--help")
    # exit code and streams
    assert rc == 64
    assert out == b""
    assert err.endswith(b"\n")
    # one-line usage with two positionals
    s = err.decode("utf-8", "replace")
    assert "usage: hd_cli.py" in s
    assert "A.json B.json" in s

def test_admin_gate_is_exit2_and_stderr_is_typed_json_stdout_empty(tmp_path, monkeypatch):
    # ensure admin is OFF
    monkeypatch.delenv("HD_ADMIN", raising=False)
    rc, out, err = _run(A, B, "--admin-out", str(tmp_path / "side.json"))

    # exit code and streams
    assert rc == 2
    assert out == b""
    assert err.endswith(b"\n")

    # typed JSON envelope on stderr
    payload = json.loads(err.decode("utf-8"))
    assert payload["error"]["code"] == "ADMIN_FLAG_REQUIRED"
    assert "admin required" in payload["error"]["message"]