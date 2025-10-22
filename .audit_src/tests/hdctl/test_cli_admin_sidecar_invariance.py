
from __future__ import annotations
import json, os, stat, subprocess, sys
from pathlib import Path

SAFE_ENV = {
    "SAFE_MODE": "1",
    # scrub any network-enabling envs
    "ALLOW_NETWORK": "",
    "HD_API_KEY": "",
    "GEO_API_KEY": "",
    "ENGINE_PROVIDER": "",
}

ARGS = ["showcompat",
        "--a-birthdate","1990-05-04","--a-birthtime","14:22","--a-place","Austin, US","--a-tz","Europe/Amsterdam",
        "--b-birthdate","1992-07-19","--b-birthtime","08:05","--b-place","New York, US","--b-tz","Europe/Amsterdam"]

def _run(extra: list[str], env_extra: dict[str,str] | None = None):
    env = dict(os.environ)
    env.update(SAFE_ENV)
    if env_extra:
        env.update(env_extra)
    p = subprocess.run([sys.executable, "scripts/hdctl.py", *ARGS, *extra],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    return p.returncode, p.stdout, p.stderr

def test_sidecar_stdout_invariance_and_perms(tmp_path: Path):
    # Run #1: no sidecar
    rc1, out1, err1 = _run([])
    assert rc1 == 0 and err1 == b""

    # Run #2: with sidecar at a per-test path (explicit)
    side = tmp_path / "admin_inv" / "compat_math.json"
    side.parent.mkdir(parents=True, exist_ok=True)
    rc2, out2, err2 = _run(["--showmath", str(side)], env_extra={"HD_ADMIN":"1"})
    assert rc2 == 0 and err2 == b""

    # Stdout invariant & LF/BOM hygiene
    assert out1 == out2, "stdout must be invariant with and without --showmath"
    assert out1.endswith(b"\n") and b"\r" not in out1 and not out1.startswith(b"\xef\xbb\xbf")

    # Sidecar hygiene: exists, JSON, LF, 0600, BOM-free
    b = side.read_bytes()
    json.loads(b.decode("utf-8"))  # must parse as JSON
    assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
    mode = stat.S_IMODE(os.stat(side).st_mode)
    assert mode == 0o600
