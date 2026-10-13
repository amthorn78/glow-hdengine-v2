
from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, complete_chart


def run_once(pair: Path):
    p = subprocess.run([sys.executable, "scripts/hdctl.py", "showcompat", "--pair-file", str(pair)],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p.returncode, p.stdout, p.stderr

def test_two_runs_identical_bytes(tmp_path: Path):
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}), encoding="utf-8")
    rc1, out1, err1 = run_once(pair)
    rc2, out2, err2 = run_once(pair)
    assert rc1 == rc2 == 0
    assert err1 == err2 == b""
    assert out1 == out2 and out1.endswith(b"\n") and not out1.endswith(b"\n\n") and b"\r" not in out1
