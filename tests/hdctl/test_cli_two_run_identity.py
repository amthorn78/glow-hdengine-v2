
from __future__ import annotations
import subprocess, sys

ARGS = ["--a-birthdate","1990-05-04","--a-birthtime","14:22","--a-place","Austin, US","--a-tz","Europe/Amsterdam",
        "--b-birthdate","1992-07-19","--b-birthtime","08:05","--b-place","New York, US","--b-tz","Europe/Amsterdam"]

def run_once():
    p = subprocess.run([sys.executable, "scripts/hdctl.py", "showcompat", *ARGS],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def test_two_runs_identical_bytes():
    rc1, out1, err1 = run_once()
    rc2, out2, err2 = run_once()
    assert rc1 == rc2 == 0
    assert err1 == err2 == b""
    assert out1 == out2 and out1.endswith(b"\n")
