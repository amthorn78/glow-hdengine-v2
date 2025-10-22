import sys, json, hashlib, pathlib, subprocess

from engine.stable.sercanon import serialize

def _sha256(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def _run_cli(a: pathlib.Path, b: pathlib.Path, admin_out: pathlib.Path | None = None) -> bytes:
    cmd = [sys.executable, "scripts/hd_cli.py", str(a), str(b)]
    if admin_out:
        cmd += ["--admin-out", str(admin_out)]
    out = subprocess.check_output(cmd)
    assert out.endswith(b"\n"), "stdout must end with exactly one LF"
    # preimage hash-coupling: sha256(sercanon(envelope_without_hash)) == idempotence_hash
    env = json.loads(out.decode("utf-8"))
    pre = dict(env); pre.pop("idempotence_hash", None)
    pre_b = serialize(pre)
    assert _sha256(pre_b) == env["idempotence_hash"], "hash coupling failed"
    return out

def test_cli_stdout_lf_hash_and_admin_sidecar_invariance(tmp_path: pathlib.Path):
    A = pathlib.Path("tests/fixtures/reader_v1/abba_A.json")
    B = pathlib.Path("tests/fixtures/reader_v1/abba_B.json")
    # Baseline stdout
    out1 = _run_cli(A, B)
    # With admin sidecar
    side = tmp_path / "admin.json"
    out2 = _run_cli(A, B, admin_out=side)
    assert out1 == out2, "stdout changed when using --admin-out"
    assert side.read_bytes().endswith(b"\n"), "admin sidecar must be LF-terminated"
