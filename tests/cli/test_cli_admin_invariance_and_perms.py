from __future__ import annotations
import os, stat, subprocess, sys, hashlib
from pathlib import Path
A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"

def _run(*argv):
    p = subprocess.run([sys.executable, "scripts/hd_cli.py", *argv], capture_output=True)
    return p.returncode, p.stdout, p.stderr

def test_admin_sidecar_invariance_and_perms(tmp_path: Path, monkeypatch):
    # admin-on so gate doesn't trip
    monkeypatch.setenv("HD_ADMIN", "1")

    # 1) baseline stdout
    rc1, out1, err1 = _run(A, B)
    assert rc1 == 0 and err1 == b""
    assert out1.endswith(b"\n")

    # 2) stdout with admin sidecar
    side = tmp_path / "abba_sidecar.json"
    rc2, out2, err2 = _run(A, B, "--admin-out", str(side))
    assert rc2 == 0 and err2 == b""
    assert out2.endswith(b"\n")

    # Invariance: stdout bytes identical
    assert out1 == out2, "stdout must be invariant when writing admin sidecar"

    # Sidecar exists, is JSON-looking, and has 0600 perms
    data = side.read_bytes()
    assert data.endswith(b"\n")
    mode = stat.S_IMODE(os.stat(side).st_mode)
    assert mode == 0o600, f"expected 0600, got {oct(mode)}"

    # Optional: quick hash to aid debugging
    _ = hashlib.sha256(out1).hexdigest()