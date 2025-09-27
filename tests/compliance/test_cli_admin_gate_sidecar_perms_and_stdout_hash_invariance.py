import os, stat, subprocess, sys, hashlib, json, pathlib, time

CLI = [sys.executable, "scripts/hd_cli.py"]
A = "tests/fixtures/cli/A.json"
B = "tests/fixtures/cli/B.json"

def sha256(b: bytes) -> str: return hashlib.sha256(b).hexdigest()

def test_rejects_numeric_without_admin(tmp_path):
    # --print-percent without admin must fail
    p = subprocess.run(CLI + [A,B,"--print-percent"], capture_output=True)
    assert p.returncode != 0
    err = p.stderr.decode("utf-8")
    assert '"ADMIN_FLAG_REQUIRED"' in err
    # stdout stays numeric-free JSON and LF-terminated
    out = p.stdout
    assert out.endswith(b"\n")
    json.loads(out.decode("utf-8"))

def test_accepts_with_admin_and_writes_sidecar_atomic_0600_and_stdout_invariant(tmp_path, monkeypatch):
    # Baseline stdout
    out0 = subprocess.check_output(CLI + [A,B])
    # Admin path with sidecar
    side = tmp_path/"admin.json"
    env = dict(os.environ); env["HD_ADMIN"] = "1"
    p = subprocess.run(CLI + [A,B,"--print-percent","--admin-out", str(side)], capture_output=True, env=env)
    assert p.returncode == 0
    # stderr contains a percent; stdout identical to baseline
    stderr = p.stderr.decode("utf-8")
    assert "%" in stderr and any(ch.isdigit() for ch in stderr)
    out1 = p.stdout
    assert out1 == out0
    # Sidecar exists, 0600 perms, LF-terminated JSON
    st = side.stat()
    mode = stat.S_IMODE(st.st_mode)
    assert mode == 0o600
    bs = side.read_bytes()
    assert bs.endswith(b"\n")
    json.loads(bs.decode("utf-8"))
    # No stray temp files remaining
    temps = [p for p in tmp_path.iterdir() if p.name.startswith(".tmp_")]
    assert not temps

def test_float_policy_non_finite_fails_typed(tmp_path, monkeypatch):
    env = dict(os.environ); env["HD_ADMIN"] = "1"
    p = subprocess.run(CLI + [A,B,"--print-percent","--percent-value","inf"], capture_output=True, env=env)
    assert p.returncode != 0
    assert '"ADMIN_FLOAT_INVALID"' in p.stderr.decode("utf-8")
