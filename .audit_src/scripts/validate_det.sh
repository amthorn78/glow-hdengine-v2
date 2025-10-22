#!/usr/bin/env bash
set -euo pipefail

# Usage/help
if [[ "${1-}" == "--help" ]]; then
  cat <<'USAGE'
usage: scripts/validate_det.sh [--help]
Proofs:
  - Two-run byte identity on hd_cli stdout
  - Preimage-hash coupling: idempotence_hash == sha256( sercanon(envelope_without_hash) )
Emits:
  - artifacts/det_report.json (canonical, LF-terminated)
  - artifacts/det_report.json.sha256
Test hook:
  DET_FORCE_HASH_MISMATCH=1  -> force a typed failure envelope
USAGE
  exit 0
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"
DET_FORCE_HASH_MISMATCH="${DET_FORCE_HASH_MISMATCH:-0}"

# Drive everything in a single Python block (keeps bytes exact)
"$PYTHON_BIN" - <<'PY'
import sys, os, json, pathlib, subprocess, hashlib

# repo-root on sys.path
sys.path.insert(0, str(pathlib.Path('.').resolve()))

from engine.stable.sercanon import serialize
from engine.stable.hashcouple import preimage_bytes, compute_hash

ROOT = pathlib.Path('.')
ART  = ROOT / 'artifacts'
ART.mkdir(parents=True, exist_ok=True)
report_path = ART / 'det_report.json'
sha_path    = ART / 'det_report.json.sha256'

def _typed_error(code, msg, details=None, status=1):
    env = {"ok": False, "schema": "v1", "code": code, "error": msg}
    if details is not None:
        env["details"] = details
    s = serialize(env)
    sys.stderr.buffer.write(s)
    sys.exit(status)

def _one_run(a, b):
    # Run hd_cli.py and capture stdout bytes
    out = subprocess.check_output([sys.executable, "scripts/hd_cli.py", str(a), str(b)])
    return out

# Prepare tiny inputs
import tempfile
td = pathlib.Path(tempfile.gettempdir())
A = td / "HDS_A.json"; B = td / "HDS_B.json"
A.write_text('{"gates":[1]}', encoding="utf-8")
B.write_text('{"gates":[2]}', encoding="utf-8")

# Two runs
out1 = _one_run(A, B)
out2 = _one_run(A, B)

# Newline discipline
if not (out1.endswith(b"\n") and not out1[:-1].endswith(b"\n")):
    _typed_error("NewlineDisciplineFailed", "stdout must have exactly one trailing LF")

# Identity
if out1 != out2:
    _typed_error("StdoutIdentityFailed", "Two consecutive stdout bytes differ")

# Parse and recompute preimage hash
doc = json.loads(out1.decode("utf-8"))
h   = doc.get("idempotence_hash")
if not (isinstance(h, str) and len(h) == 64 and all(c in "0123456789abcdef" for c in h)):
    _typed_error("HashMissingOrInvalid", "idempotence_hash not present or invalid")

pre = {k:v for k,v in doc.items() if k != "idempotence_hash"}
pre_b = preimage_bytes(pre)
# Optional test hook to force mismatch
if os.getenv("DET_FORCE_HASH_MISMATCH","0") == "1":
    h2 = "0"*64
else:
    h2 = compute_hash(pre_b)

if h2 != h:
    _typed_error("HashCouplingFailed", "sha256(preimage_bytes) does not equal idempotence_hash",
                 {"recomputed_sha256": h2, "embedded_hash": h})

# Build and emit report (canonical JSON, LF-terminated)
rep = {
    "ok": True,
    "schema": "v1",
    "identity_ok": True,
    "lf_ok": True,
    "hash_coupling_ok": True,
    "hash": {"stdout_sha256": hashlib.sha256(out1).hexdigest(),
             "preimage_sha256": h2}
}
rb = serialize(rep)
report_path.write_bytes(rb)
sha_path.write_text(hashlib.sha256(rb).hexdigest() + "\n", encoding="utf-8")

# Human-readable success lines for callers
sys.stdout.write("IDENTITY_OK\n")
sys.stdout.write("HASH_COUPLING_OK\n")
PY

# shell exit 0 on success; non-zero handled inside Python via typed error
