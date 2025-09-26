import subprocess, sys, hashlib
from pathlib import Path

def _sha(b: bytes) -> str:
    import hashlib; return hashlib.sha256(b).hexdigest()

def test_resolve_emit_has_single_lf_and_identity(tmp_path: Path):
    out = tmp_path/"res.json"
    # first write
    subprocess.check_call([sys.executable, "scripts/hd_resolve.py", "--out", str(out)])
    b1 = out.read_bytes()
    # second write (overwrite)
    subprocess.check_call([sys.executable, "scripts/hd_resolve.py", "--out", str(out)])
    b2 = out.read_bytes()

    assert b1.endswith(b"\n") and not b1[:-1].endswith(b"\n")
    assert b1 == b2 and _sha(b1) == _sha(b2)
