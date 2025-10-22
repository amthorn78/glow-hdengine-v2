import json, subprocess

def test_serializer_mismatch_envelope():
    # Force a mismatch via env hook; expect non-zero and typed error JSON on stderr
    p = subprocess.run(["bash", "scripts/validate_canon.sh", "--json"],
                       capture_output=True, text=True, env={**dict(), "TEST_FORCE_SERIALIZER_MISMATCH":"1"})
    assert p.returncode != 0
    # stderr must be a single JSON object with our envelope
    err = p.stderr.strip().splitlines()[-1]
    doc = json.loads(err)
    assert doc.get("ok") is False
    assert doc.get("schema") == "v1"
    assert doc.get("code") == "CANON_SERIALIZER_MISMATCH"
    assert isinstance(doc.get("error"), str)
