from __future__ import annotations
import subprocess, sys, pathlib, re

def _run(*args: str):
    p = subprocess.run([sys.executable, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def test_help_is_exit64_one_line_lf_and_mentions_two_positionals():
    code, out, err = _run("scripts/hd_cli.py", "--help")
    # Usage is human one-liner to stderr; stdout empty
    assert out == b""
    assert code == 64
    assert err.endswith(b"\n") and b"\n" not in err[:-1]
    # Must mention two positional args (A.json B.json)
    msg = err.decode("utf-8", "replace").lower()
    assert "a.json" in msg and "b.json" in msg

def test_future_import_position_and_no_subparsers():
    p = pathlib.Path("scripts/hd_cli.py")
    src = p.read_text(encoding="utf-8")
    lines = src.splitlines()
    # If a future import exists, it must be at line 1
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("from __future__ import"):
            assert i == 1, f"'from __future__' must be line 1, found at {i}"
            break
    # Never introduce subcommands on frozen CLI
    assert "add_subparsers(" not in src
