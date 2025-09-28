#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="audit/T-API-CLI-SMOKE-001_${STAMP}"
mkdir -p "$OUTDIR"/{env,git,files,cmd,tests,artifacts,schemas}

note() { printf '%s\n' "$*" | tee -a "$OUTDIR/00_audit_log.txt" >&2; }

# ---------- 0) Repo & env ----------
note "[env] snapshot"
(
  set -x
  uname -a
  python -V
  python - <<'PY'
import json, sys, pkgutil
mods = {}
for n in ("pytest","jsonschema"):
    try:
        __import__(n); v = sys.modules[n].__version__
    except Exception:
        v = "(not importable)"
    mods[n] = v
print(json.dumps(mods, indent=2))
PY
  echo "PWD=$PWD"
  echo "SAFE_MODE=${SAFE_MODE-}"
  echo "ENGINE_ENV=${ENGINE_ENV-}"
  echo "RELEASE_ID=${RELEASE_ID-}"
  locale || true
) > "$OUTDIR/env/00_env.txt" 2>&1 || true

git rev-parse HEAD > "$OUTDIR/git/00_head_sha.txt" || true
git status --porcelain=v1 > "$OUTDIR/git/01_status.txt" || true
git log -n 20 --oneline > "$OUTDIR/git/02_log.txt" || true

# ---------- 1) Key files (with line numbers) ----------
nl -ba scripts/hd_cli.py > "$OUTDIR/files/hd_cli.py.txt" || echo "MISSING scripts/hd_cli.py" > "$OUTDIR/files/hd_cli.py.txt"
nl -ba tests/cli/test_cli_exit2_typed_json_and_exit64_usage.py > "$OUTDIR/files/test_cli_exit2_typed_json_and_exit64_usage.py.txt" || true
nl -ba tests/cli/test_cli_stdout_schema_and_lf.py > "$OUTDIR/files/test_cli_stdout_schema_and_lf.py.txt" || true

# Schema & pin (if present)
if [ -f schemas/reader.v1.schema.json ]; then
  cp -a schemas/reader.v1.schema.json "$OUTDIR/schemas/"
  [ -f schemas/reader.v1.schema.json.sha256 ] && cp -a schemas/reader.v1.schema.json.sha256 "$OUTDIR/schemas/" || true
  python - <<'PY' > "$OUTDIR/schemas/01_schema_hash_check.txt"
import hashlib, pathlib
s = pathlib.Path("schemas/reader.v1.schema.json")
p = s.read_bytes()
h = hashlib.sha256(p).hexdigest()
out = [f"schema_sha256={h}"]
p2 = pathlib.Path("schemas/reader.v1.schema.json.sha256")
if p2.exists():
    exp = p2.read_text(encoding="utf-8").strip().split()[0]
    out.append(f"schema_pin={exp}")
    out.append("SCHEMA_PIN_OK" if exp==h else "SCHEMA_PIN_MISMATCH")
else:
    out.append("SCHEMA_PIN_FILE_MISSING")
print("\n".join(out))
PY
fi

# ---------- 2) Static grep sanity ----------
{
  echo "== grep hd_cli.py =="
  grep -nE "sys\.exit\(|argparse|add_help=False|usage:" -n scripts/hd_cli.py || true
} > "$OUTDIR/files/grep_hd_cli.txt" || true

# ---------- 3) Commands (help, normal, admin-gate) ----------
A="tests/fixtures/reader_v1/abba_A.json"
B="tests/fixtures/reader_v1/abba_B.json"

run_cmd() { # usage: run_cmd <label> <cmd> [args...]
  local label="$1"; shift
  local outb="$OUTDIR/cmd/${label}"
  mkdir -p "$(dirname "$outb")"

  # record argv as JSON using python stdin script; pass "$@" as its argv
  python - "$@" <<'PY' > "${outb}_meta.txt"
import json, sys
print(json.dumps({"cmd": sys.argv[1:]}, indent=2))
PY

  # run and capture
  (
    set +e
    "$@" > "${outb}_stdout.bin" 2> "${outb}_stderr.txt"
    echo $? > "${outb}_rc.txt"
  )

  # summarize bytes
  python - <<'PY' "${outb}_stdout.bin" "${outb}_stderr.txt" "${outb}_rc.txt" > "${outb}_summary.txt"
import sys, json, pathlib
pout, perr, prc = map(pathlib.Path, sys.argv[1:4])
b = pout.read_bytes() if pout.exists() else b""
e = perr.read_text(encoding="utf-8", errors="replace") if perr.exists() else ""
rc = int(prc.read_text().strip()) if prc.exists() else None
def tail_hex(x: bytes, n=8): 
    t = x[-n:]
    return " ".join(f"{c:02x}" for c in t)
print(json.dumps({
  "stdout_len": len(b),
  "stdout_tail_hex": tail_hex(b, 8),
  "stdout_ends_lf": b.endswith(b"\n"),
  "stderr_len": len(e.encode()),
  "stderr_tail": e[-160:],
  "rc": rc
}, indent=2))
PY
}

run_cmd help              python scripts/hd_cli.py --help
run_cmd ab                python scripts/hd_cli.py "$A" "$B"
run_cmd ab_admin_violate  python scripts/hd_cli.py "$A" "$B" --admin-out "$OUTDIR/artifacts/side.json"

# ---------- 4) JSON/schema and hash coupling on normal stdout ----------
python - <<'PY' "$OUTDIR/cmd/ab_stdout.bin" > "$OUTDIR/artifacts/abba_json_validation.txt"
import json, sys, hashlib, pathlib
p = pathlib.Path(sys.argv[1])
b = p.read_bytes()
o = json.loads(b)
# hash coupling: preimage is envelope minus idempotence_hash
pre = dict(o); pre.pop("idempotence_hash", None)
pre_b = json.dumps(pre, ensure_ascii=False, separators=(",",":"), sort_keys=True).encode("utf-8")+b"\n"
h = hashlib.sha256(pre_b).hexdigest()
print("HASH_COUPLED", "OK" if o.get("idempotence_hash")==h else "MISMATCH")
print("LF_OK", b.endswith(b"\n"))
print("LEN", len(b))
# schema if present
sp = pathlib.Path("schemas/reader.v1.schema.json")
if sp.exists():
    try:
        import jsonschema
        sch = json.loads(sp.read_text(encoding="utf-8"))
        jsonschema.Draft7Validator(sch).validate(o)
        print("SCHEMA_OK")
    except Exception as e:
        print("SCHEMA_FAIL", type(e).__name__, str(e)[:300])
else:
    print("SCHEMA_SKIPPED")
PY

# ---------- 5) Re-run targeted pytest and capture ----------
(
  set +e
  pytest -q tests/cli/test_cli_exit2_typed_json_and_exit64_usage.py
  echo "---"
  pytest -q tests/cli/test_cli_stdout_schema_and_lf.py
  echo $?
) &> "$OUTDIR/tests/pytest_targeted.txt"

# ---------- 6) Bundle ----------
ZIP="$OUTDIR.zip"
( cd "$(dirname "$OUTDIR")" && zip -qr "$(basename "$ZIP")" "$(basename "$OUTDIR")" )
printf '[cli-audit] %s\n[bundle] %s\n' "$OUTDIR" "$ZIP"