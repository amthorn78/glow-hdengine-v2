from __future__ import annotations
import subprocess, sys, json, hashlib, re
from engine.stable.sercanon import serialize

A = "tests/fixtures/reader_v1/abba_A.json"
B = "tests/fixtures/reader_v1/abba_B.json"

_HEX64 = re.compile(r"^[0-9a-f]{64}$")

def _run(a: str, b: str):
    p = subprocess.run([sys.executable, "scripts/hd_cli.py", a, b], capture_output=True)
    return p.returncode, p.stdout, p.stderr

def test_ab_ba_byte_identity_and_lf():
    rc1, out1, err1 = _run(A, B)
    rc2, out2, err2 = _run(B, A)
    assert rc1 == 0 and rc2 == 0
    assert out1 and out2
    # exactly one trailing LF and no BOM
    assert out1.endswith(b"\n") and out2.endswith(b"\n")
    assert not out1.startswith(b"\xef\xbb\xbf")
    # AB ↔ BA must be byte-identical
    assert out1 == out2

def test_hash_coupling_preimage_equals_idempotence_hash():
    rc, out, err = _run(A, B)
    assert rc == 0 and out
    obj = json.loads(out)
    h = obj.get("idempotence_hash")
    assert isinstance(h, str) and _HEX64.match(h)
    # Preimage = envelope without the hash, serialized canonically
    pre = dict(obj)
    pre.pop("idempotence_hash", None)
    pre_b = serialize(pre)
    assert hashlib.sha256(pre_b).hexdigest() == h
