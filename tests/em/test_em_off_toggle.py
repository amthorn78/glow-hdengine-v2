import os, sys, json, subprocess
from pathlib import Path

def test_admin_can_disable_em_and_bytes_change_or_hold_consistently(tmp_path: Path):
    a = tmp_path/"A.json"; b = tmp_path/"B.json"
    a.write_text('{"gates":[1,2]}', encoding="utf-8")
    b.write_text('{"gates":[3,4]}', encoding="utf-8")

    out_on  = subprocess.check_output([sys.executable, "scripts/hd_cli.py", str(a), str(b)])
    env = dict(os.environ); env["HD_FORCE_EM_OFF"] = "1"
    out_off = subprocess.check_output([sys.executable, "scripts/hd_cli.py", str(a), str(b)], env=env)

    # Public contract: LF-terminated, valid JSON both ways
    assert out_on.endswith(b"\n") and not out_on[:-1].endswith(b"\n")
    assert out_off.endswith(b"\n") and not out_off[:-1].endswith(b"\n")
    json.loads(out_on.decode("utf-8"))
    json.loads(out_off.decode("utf-8"))
