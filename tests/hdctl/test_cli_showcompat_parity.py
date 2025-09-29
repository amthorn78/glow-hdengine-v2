
from __future__ import annotations
import subprocess, sys, re, json

def run_showcompat(*argv):
    p = subprocess.run([sys.executable, "scripts/hdctl.py", "showcompat", *argv],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def _argsA():
    return ["--a-birthdate","1990-05-04","--a-birthtime","14:22","--a-place","Austin, US","--a-tz","Europe/Amsterdam",
            "--b-birthdate","1992-07-19","--b-birthtime","08:05","--b-place","New York, US","--b-tz","Europe/Amsterdam"]

def _argsB():
    return ["--a-birthdate","1992-07-19","--a-birthtime","08:05","--a-place","New York, US","--a-tz","Europe/Amsterdam",
            "--b-birthdate","1990-05-04","--b-birthtime","14:22","--b-place","Austin, US","--b-tz","Europe/Amsterdam"]

def test_ab_ba_parity_bytes_identical():
    rc1, out1, err1 = run_showcompat(*_argsA())
    rc2, out2, err2 = run_showcompat(*_argsB())
    assert rc1 == rc2 == 0
    assert err1 == err2 == b""
    assert out1.endswith(b"\n") and out2.endswith(b"\n")
    assert out1 == out2
    # public is numeric-free
    obj = json.loads(out1)
    assert "band" in obj and "categories" in obj
    s = out1.decode("utf-8")
    # no raw numeric JSON values (digits only inside strings)
    assert not re.search(r':\s*\d', s)

