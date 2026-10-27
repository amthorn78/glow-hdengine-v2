
from __future__ import annotations
import subprocess, sys, json
from pathlib import Path

from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, complete_chart

def run_showcompat(*argv):
    p = subprocess.run([sys.executable, "scripts/hdctl.py", "showcompat", *argv],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def _pair(path: Path, left: dict, right: dict) -> str:
    path.write_text(json.dumps({"left": left, "right": right}), encoding="utf-8")
    return str(path)

def test_ab_ba_parity_bytes_identical(tmp_path: Path):
    a, b = complete_chart(UUID_A, GATES_A), complete_chart(UUID_B, GATES_B)
    rc1, out1, err1 = run_showcompat("--pair-file", _pair(tmp_path / "ab.json", a, b))
    rc2, out2, err2 = run_showcompat("--pair-file", _pair(tmp_path / "ba.json", b, a))
    assert rc1 == rc2 == 0
    assert err1 == err2 == b""
    assert out1.endswith(b"\n") and out2.endswith(b"\n")
    assert out1 == out2
    # PF05 §4.1.3: stdout is the canonical magic10_compat_result.v1 document
    obj = json.loads(out1)
    assert obj["schema"] == "magic10_compat_result.v1" and "categories" in obj
