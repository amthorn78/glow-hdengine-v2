import subprocess, sys, json, pathlib, hashlib
from engine.stable.sercanon import serialize

CLI = [sys.executable, "scripts/hd_cli.py"]
A = pathlib.Path("tests/fixtures/reader_v1/abba_A.json")
B = pathlib.Path("tests/fixtures/reader_v1/abba_B.json")

def _run(a: pathlib.Path, b: pathlib.Path):
    out = subprocess.check_output(CLI + [str(a), str(b)])
    assert out.endswith(b"\n")
    env = json.loads(out.decode("utf-8"))
    # preimage hash coupling sanity (doesn't hurt to reassert)
    pre = dict(env); pre.pop("idempotence_hash", None)
    assert hashlib.sha256(serialize(pre)).hexdigest() == env["idempotence_hash"]
    return env

def test_meta_abba_parity_same_release_and_meta():
    assert A.exists() and B.exists(), "expected reader_v1 ABBA fixtures"
    ab = _run(A,B)
    ba = _run(B,A)
    # Parity expectations: meta and release_id identical under same release
    assert ab["meta"] == ba["meta"]
    assert ab["release_id"] == ba["release_id"]
    # basic public guards
    assert ab["reader_version"] == "v1" and ba["reader_version"] == "v1"
