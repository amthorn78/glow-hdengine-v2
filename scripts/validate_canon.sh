#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
usage: scripts/validate_canon.sh [--json]|[--help]
  --json   Print only the canon_report.json body (newline-terminated) to stdout
  --help   Show this message
Notes:
  - Emits CANON_CHECKSUMS.json (repo root) and artifacts/canon_report.json
  - Serializer guard + two-run identity enforced
  - Prod overrides (env keys or config/overrides/*.json) fail with typed envelope
USAGE
}

JSON_ONLY=0
if [[ "${1-}" == "--help" ]]; then
  usage
  exit 0
elif [[ "${1-}" == "--json" ]]; then
  JSON_ONLY=1
elif [[ "${1-}" != "" ]]; then
  usage 1>&2
  exit 2
fi

PYTHON_BIN="${PYTHON_BIN:-python3}"
JSON_ONLY="${JSON_ONLY}" TEST_FORCE_SERIALIZER_MISMATCH="${TEST_FORCE_SERIALIZER_MISMATCH:-0}" "$PYTHON_BIN" - <<'PY'
import sys, json, pathlib, os, hashlib

# repo root on path
sys.path.insert(0, str(pathlib.Path('.').resolve()))

from core.canon.validate import load_repo_canon, detect_prod_overrides
from core.canon.checksums import build_checksums
from core.stable import sercanon  # single serializer

ROOT = pathlib.Path('.')
ART = ROOT / 'artifacts'
ART.mkdir(parents=True, exist_ok=True)

checksums_path = ROOT / 'CANON_CHECKSUMS.json'
report_path    = ART  / 'canon_report.json'

def _stdout_json(obj):
    s = sercanon.stable_dumps(obj)
    if isinstance(s, (bytes, bytearray)): s = s.decode('utf-8')
    if s.endswith("\n"): s = s.rstrip("\n")
    sys.stdout.write(s + "\n")

def _canon_bytes(obj) -> bytes:
    s = sercanon.stable_dumps(obj)
    if isinstance(s, (bytes, bytearray)):
        bs = bytes(s)
    else:
        bs = (s if isinstance(s, str) else str(s)).encode('utf-8')
    if bs.endswith(b"\n"): bs = bs.rstrip(b"\n")
    return bs + b"\n"

def _typed_error(code: str, message: str, details=None, status=1):
    env = {"ok": False, "schema": "v1", "code": code, "error": message}
    if details is not None:
        env["details"] = details
    s = sercanon.stable_dumps(env)
    if isinstance(s, (bytes, bytearray)): s = s.decode('utf-8')
    if not s.endswith("\n"): s += "\n"
    sys.stderr.write(s)
    sys.exit(status)

def _sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

# 0) prod overrides guard
hit = detect_prod_overrides(pathlib.Path("."))
if hit:
    _typed_error(hit, "Overrides present in prod")

# 1) load/build
canon = load_repo_canon(ROOT)
chs = build_checksums(canon)

# 2) write with serializer guard (optionally force mismatch for testing)
force = os.getenv("TEST_FORCE_SERIALIZER_MISMATCH", "0") == "1"

def _write_one(path: pathlib.Path, obj):
    b = _canon_bytes(obj)
    path.write_bytes(b)
    guard_b = _canon_bytes(obj)
    if force:
        # flip last byte deterministically to simulate mismatch
        guard_b = guard_b[:-1] + (b'\n' if guard_b[-1:] != b'\n' else b' ')
    if guard_b != b:
        _typed_error("CANON_SERIALIZER_MISMATCH", "Serializer produced non-identical bytes on re-run",
                     {"path": str(path)})
    return b

def _two_run_identity(path: pathlib.Path, obj):
    b1 = _write_one(path, obj)
    b2 = _write_one(path, obj)
    if _sha(b1) != _sha(b2):
        _typed_error("CANON_REPORT_NON_DETERMINISTIC", "Artifact bytes are not identical across two writes",
                     {"path": str(path)})
    return _sha(b1)

rep = {
    "ok": True,
    "schema": "v1",
    "summary": {
        "gates": len(canon.get("gates") or []),
        "channels": len(canon.get("channels") or []),
    },
    "hashes": {}
}

chs_sha = _two_run_identity(checksums_path, chs)
rep_sha = _two_run_identity(report_path, rep)
rep["hashes"] = {"checksums_sha256": chs_sha, "report_sha256": rep_sha}

if os.getenv("JSON_ONLY") == "1":
    _stdout_json(rep)
PY
