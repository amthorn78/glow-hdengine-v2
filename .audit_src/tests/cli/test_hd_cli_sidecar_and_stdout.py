import sys, subprocess, json, hashlib
from pathlib import Path

def _run(*args, **kwargs):
    return subprocess.check_output([sys.executable, "scripts/hd_cli.py", *args], **kwargs)

def test_stdout_invariant_with_admin_out_and_debug(tmp_path: Path):
    a = tmp_path / "A.json"; b = tmp_path / "B.json"
    a.write_text('{"gates":[1]}', encoding="utf-8")
    b.write_text('{"gates":[2]}', encoding="utf-8")

    # Baseline stdout
    out1 = _run(str(a), str(b))
    assert out1.endswith(b"\n") and not out1[:-1].endswith(b"\n")

    # With admin-out only — stdout must be identical
    side1 = tmp_path / "admin1.json"
    out2 = _run(str(a), str(b), "--admin-out", str(side1))
    assert out2 == out1
    assert side1.read_bytes().endswith(b"\n") and not side1.read_bytes()[:-1].endswith(b"\n")

    # With --debug + --admin-out — stdout still identical
    side2 = tmp_path / "admin2.json"
    out3 = _run(str(a), str(b), "--debug", "--admin-out", str(side2))
    assert out3 == out1
    assert side2.read_bytes().endswith(b"\n") and not side2.read_bytes()[:-1].endswith(b"\n")

    # Sanity: public stdout parses and carries a 64-hex idempotence_hash
    doc = json.loads(out1.decode("utf-8"))
    h = doc.get("idempotence_hash","")
    assert isinstance(h, str) and len(h) == 64 and all(c in "0123456789abcdef" for c in h)
