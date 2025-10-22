from __future__ import annotations
import subprocess, sys

A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"

def _run(*argv):
    p = subprocess.run([sys.executable, "scripts/hd_cli.py", *argv], capture_output=True)
    return p.returncode, p.stdout, p.stderr

def _assert_text_bytes_ok(b: bytes):
    # no UTF-8 BOM
    assert not b.startswith(b"\xEF\xBB\xBF"), "BOM must not be present"
    # exactly one trailing LF
    assert b.endswith(b"\n"), "must end with single LF"
    assert len(b) >= 1 and b[-2:-1] != b"\n", "must not end with double LF"

def test_cli_text_artifacts_are_bom_free_and_single_lf():
    rc1, out_ab, err1 = _run(A, B)
    assert rc1 == 0 and err1 == b""
    _assert_text_bytes_ok(out_ab)

    rc2, out_ba, err2 = _run(B, A)
    assert rc2 == 0 and err2 == b""
    _assert_text_bytes_ok(out_ba)