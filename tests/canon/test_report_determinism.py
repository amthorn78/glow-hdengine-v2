import json, re, subprocess, pathlib, hashlib
from core.canon.validate import load_repo_canon
from core.canon.checksums import build_checksums
from engine.stable import sercanon  # unified import path

HEX64 = re.compile(r"^[0-9a-f]{64}$")

def _canon_bytes(obj) -> bytes:
    s = sercanon.stable_dumps(obj)
    if isinstance(s, (bytes, bytearray)):
        bs = bytes(s)
    else:
        txt = s if isinstance(s, str) else str(s)
        bs = txt.encode("utf-8")
    # normalize to exactly one trailing LF
    if bs.endswith(b"\n"):
        bs = bs.rstrip(b"\n")
    return bs + b"\n"

def test_report_and_checksums_determinism(tmp_path):
    canon = load_repo_canon(pathlib.Path("."))
    ch1 = build_checksums(canon)
    ch2 = build_checksums(canon)
    b1 = _canon_bytes(ch1)
    b2 = _canon_bytes(ch2)
    h1 = hashlib.sha256(b1).hexdigest()
    h2 = hashlib.sha256(b2).hexdigest()
    assert b1 == b2 and h1 == h2

def test_validate_script_json_output():
    # --json must print exactly one JSON object (newline-terminated) with expected keys/patterns
    out = subprocess.check_output(["bash", "scripts/validate_canon.sh", "--json"], text=True)
    assert out.endswith("\n")
    doc = json.loads(out)
    assert doc.get("ok") is True and doc.get("schema") == "v1"
    hashes = doc.get("hashes", {})
    assert HEX64.match(hashes.get("checksums_sha256", "")) and HEX64.match(hashes.get("report_sha256", ""))
