
from __future__ import annotations
import json, subprocess, sys

def run(*argv: str):
    p = subprocess.run([sys.executable, "scripts/hdctl.py", *argv],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def test_singlebg_success_lf_only():
    rc, out, err = run("read","singlebg",
                       "--birthdate","1990-01-01",
                       "--birthtime","12:34",
                       "--place","Amsterdam, NL",
                       "--tz","Europe/Amsterdam")
    assert rc == 0 and err == b""
    assert out.endswith(b"\n")
    obj = json.loads(out)
    assert isinstance(obj, dict) and "gates" in obj and isinstance(obj["gates"], list)

def test_singlebg_bad_inputs_exit2_typed_json():
    rc, out, err = run("read","singlebg",
                       "--birthdate","1990-13-99",
                       "--birthtime","25:61",
                       "--place","NoComma",
                       "--tz","Bad/TZ")
    assert rc == 2 and out == b""
    j = json.loads(err.decode("utf-8"))
    assert "error" in j and j["error"]["code"] == "READER_INVALID_INPUT"
