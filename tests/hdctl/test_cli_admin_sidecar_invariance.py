
from __future__ import annotations
import json, os, stat, subprocess, sys
from pathlib import Path

from tests.support.pr04_fixtures import GATES_A, GATES_B, UUID_A, UUID_B, complete_chart

SAFE_ENV = {
    "SAFE_MODE": "1",
    # scrub any network-enabling envs
    "ALLOW_NETWORK": "0",
    "HD_API_KEY": "",
    "GEO_API_KEY": "",
    "ENGINE_PROVIDER": "",
}

def _run(pair: Path, extra: list[str]):
    env = dict(os.environ)
    env.update(SAFE_ENV)
    p = subprocess.run([sys.executable, "scripts/hdctl.py", "showcompat", "--pair-file", str(pair), *extra],
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)
    return p.returncode, p.stdout, p.stderr

def test_sidecar_stdout_invariance_and_perms(tmp_path: Path):
    pair = tmp_path / "pair.json"
    pair.write_text(json.dumps({"left": complete_chart(UUID_A, GATES_A), "right": complete_chart(UUID_B, GATES_B)}), encoding="utf-8")

    # Run #1: no admin dumps
    rc1, out1, err1 = _run(pair, [])
    assert rc1 == 0 and err1 == b""

    # Run #2: with admin dumps at a per-test path (explicit)
    admin_dir = tmp_path / "admin_inv"
    rc2, out2, err2 = _run(pair, ["--dump-admin-dir", str(admin_dir)])
    assert rc2 == 0 and err2 == b""

    # Stdout invariant & LF/BOM hygiene
    assert out1 == out2, "stdout must be invariant with and without --dump-admin-dir"
    assert out1.endswith(b"\n") and b"\r" not in out1 and not out1.startswith(b"\xef\xbb\xbf")

    # Sidecar hygiene: exists, JSON, LF, 0600, BOM-free
    dumps = sorted(admin_dir.glob("*.json"))
    assert dumps
    for side in dumps:
        b = side.read_bytes()
        json.loads(b.decode("utf-8"))  # must parse as JSON
        assert b.endswith(b"\n") and not b.startswith(b"\xef\xbb\xbf")
        assert stat.S_IMODE(os.stat(side).st_mode) == 0o600
