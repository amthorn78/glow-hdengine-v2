import json, subprocess, os

def test_hash_coupling_guard_fails_closed():
    env = {**os.environ, "DET_FORCE_HASH_MISMATCH": "1"}
    p = subprocess.run(["bash", "scripts/validate_det.sh"], capture_output=True, text=True, env=env)
    assert p.returncode != 0
    # Last stderr line must be a JSON envelope with the expected code
    err = p.stderr.strip().splitlines()[-1]
    doc = json.loads(err)
    assert doc.get("ok") is False
    assert doc.get("schema") == "v1"
    assert doc.get("code") == "HashCouplingFailed"
    assert isinstance(doc.get("error"), str)
