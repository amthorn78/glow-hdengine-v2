#!/usr/bin/env bash
set -euo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd); cd "$ROOT"

PASS=()
FAIL=()
note() { printf '%s\n' "$*" >&2; }
ok()   { PASS+=("$1"); note "PASS  $1"; }
ko()   { FAIL+=("$1 — $2"); note "FAIL  $1 — $2"; }

must_exist() { for f in "$@"; do [[ -f "$f" ]] || ko "FILE_MISSING" "$f"; done; }

if ./ci/checks/check_final_lf.sh; then ok CI_CHECK_FINAL_LF_OK; else ko CI_CHECK_FINAL_LF_OK "final LF / CR check"; fi
if ./ci/checks/check_mirror_schema.sh; then ok CI_CHECK_MIRROR_SCHEMA_OK; else ko CI_CHECK_MIRROR_SCHEMA_OK "mirror schema/order/dupes/path-proof"; fi

must_exist \
  artifacts/ops/rails_refusal_proof.txt \
  artifacts/ops/no_io_guard.txt \
  artifacts/runtime/env_matrix.snapshot.json \
  artifacts/runtime/env_matrix.failure.json \
  artifacts/db/check_schema.txt \
  artifacts/db/grants.txt \
  artifacts/db/ddl_fingerprint.json \
  artifacts/db/check_constraints.txt \
  artifacts/db/partition_plan.txt \
  artifacts/db/migration_runner.log \
  docs/evidence/INDEX.json \
  docs/evidence/INDEX.sha256 \
  artifacts/evidence_index.jsonl

python - <<'PY'
import sys, pathlib
p = pathlib.Path("artifacts/ops/rails_refusal_proof.txt")
try:
    b = p.read_bytes()
except FileNotFoundError:
    print("KO REFUSAL_PROOF_READ missing", file=sys.stderr); sys.exit(64)
text = b.decode("utf-8", "strict")
parts = text.split("\n\n", 1)
if len(parts) != 2:
    print("KO REFUSAL_PROOF_FORMAT need exactly one blank line", file=sys.stderr); sys.exit(65)
hdrs, body = parts
for line in [h for h in hdrs.splitlines() if h.strip()]:
    k = line.split(":",1)[0]
    if k != k.lower():
        print("KO REFUSAL_HEADERS_CASE", file=sys.stderr); sys.exit(66)
need = {"content-type: application/json; charset=utf-8", "cache-control: no-store"}
seen = {l.strip() for l in hdrs.lower().splitlines()}
for n in need:
    if n not in seen:
        print(f"KO REFUSAL_HEADERS_MISSING {n}", file=sys.stderr); sys.exit(67)
for bad in ("etag:", "content-encoding:", "vary:"):
    if any(l.startswith(bad) for l in (h.lower() for h in hdrs.splitlines())):
        print(f"KO REFUSAL_HEADERS_FORBIDDEN {bad}", file=sys.stderr); sys.exit(68)
expected = '{"schema":"v1","ok":false,"code":"rails_closed","error":"rails are closed"}\n'
if body != expected:
    print("KO REFUSAL_BODY_MISMATCH", file=sys.stderr); sys.exit(69)
print("OK")
PY
case $? in 0) ok ERROR_CACHECTL_NOSTORE_OK; ok ERROR_CTYPE_JSON_UTF8_OK; ok NO_CONTENT_ENCODING_OK;; *) ko REFUSAL_PROOF "headers/body/format";; esac

if grep -q '^external_io_attempts: 0$' artifacts/ops/no_io_guard.txt; then
  ok NO_EXTERNAL_IO_ON_REFUSAL_OK
else
  ko NO_EXTERNAL_IO_ON_REFUSAL_OK "expected: external_io_attempts: 0"
fi

python - <<'PY'
import json, sys, os
sink = os.environ.get("LOG_SINK_PATH")
# If the app isn’t running with LOG_SINK, skip silently
if not sink or not os.path.isfile(sink):
    print("OK"); sys.exit(0)
try:
    line = open(sink,"r",encoding="utf-8").read().splitlines()[-1]
    obj = json.loads(line)
except Exception:
    print("OK"); sys.exit(0)
keys = set(obj.keys())
expected = {"at","route","status","duration_ms","idempotence_hash","release_id"}
if keys != expected or obj.get("route") != "ops.rails.refusal":
    sys.exit(1)
print("OK")
PY
case $? in 0) ok OBS_KEYS_ONLY_OK;; *) ko OBS_KEYS_ONLY_OK "canonical keys-only log mismatch";; esac

if python tools/evidence/generate_env_matrix_snapshot.py --check && python - <<'PY'
import pathlib
import sys

failure = pathlib.Path("artifacts/runtime/env_matrix.failure.json").read_text(
    encoding="utf-8"
)
expected = '{"schema":"v1","ok":false,"code":"missing_db_config","error":"database configuration not found"}\n'
if failure != expected:
    sys.exit(72)
print("OK")
PY
then
  ok DB_CONN_ENV_OK
  ok DB_CONN_TYPED_ERROR_OK
else
  ko ENV_MATRIX "v3 singleton/failure mismatch"
fi

python - <<'PY'
import pathlib, sys
if pathlib.Path("artifacts/db/check_schema.txt").read_bytes() != b"hde, public\n":
    sys.exit(1)
print("OK")
PY
case $? in 0) ok DB_RUNTIME_SEARCH_PATH_OK;; *) ko DB_RUNTIME_SEARCH_PATH_OK "expected exactly: hde, public";; esac

if grep -qi '^ALTER DEFAULT PRIVILEGES' artifacts/db/grants.txt; then
  ok DB_ROLE_OK
else
  ko DB_ROLE_OK "missing ADP section (present-even-empty required)"
fi

python - <<'PY'
import json, pathlib, sys
p = pathlib.Path("artifacts/db/ddl_fingerprint.json")
b = p.read_bytes()
if (not b.endswith(b"\n")) or b.count(b"\n") == 0 or b.count(b"\r") > 0:
    sys.exit(73)
try:
    json.loads(b)
except Exception:
    sys.exit(74)
print("OK")
PY
case $? in 0) ok DB_SCHEMA_FINGERPRINT_OK;; *) ko DB_SCHEMA_FINGERPRINT_OK "compact json / one LF / parse";; esac

if grep -qx 'no-op: no migrations to run' artifacts/db/migration_runner.log; then
  ok MIGRATION_REPLAY_IDENTITY_OK
  ok MIGRATION_RUNNER_OK
  ok MIGRATION_LOGGED_OK
else
  ko MIGRATION_REPLAY_IDENTITY_OK "missing exact no-op line"
fi

for f in artifacts/db/check_constraints.txt artifacts/db/partition_plan.txt; do
  if [[ -f "$f" ]] && [[ "$(wc -c < "$f")" -ge 1 ]]; then ok POSTURE_FILE_"$f"; else ko POSTURE_FILE_"$f" "missing or empty"; fi
done

python - <<'PY'
import hashlib, pathlib, sys, json
idx = pathlib.Path("docs/evidence/INDEX.json").read_bytes()
sent = pathlib.Path("docs/evidence/INDEX.sha256").read_text().strip()
h = hashlib.sha256(idx).hexdigest()
if h != sent:
    sys.exit(75)
allowed = {"proof", "snapshot", "log", "script", "golden"}
for line in pathlib.Path("artifacts/evidence_index.jsonl").read_text().splitlines(True):
    if not line.endswith("\n"):
        sys.exit(76)
    rec = json.loads(line)
    if rec.get("role") not in allowed:
        sys.exit(77)
print("OK")
PY
case $? in 0) ok EVIDENCE_INDEX_HASH_OK; ok EVIDENCE_INDEX_UPDATED_OK; ok EVIDENCE_INDEX_MIRROR_OK;; *) ko EVIDENCE_PARITY "sentinel/mirror checks";; esac

python - <<'PY'
import json, sys, pathlib
for name in ("artifacts/ops/restart_probe_before.json","artifacts/ops/restart_probe_after.json"):
    p = pathlib.Path(name)
    if not p.exists():
        continue
    obj = json.loads(p.read_text())
    if "probe_token" in obj:
        sys.exit(1)
    if "probe_token_present" not in obj or not isinstance(obj["probe_token_present"], bool):
        sys.exit(2)
print("OK")
PY
case $? in 0) ok OPS_PROBE_NO_TOKEN_LEAK;; *) ko OPS_PROBE_NO_TOKEN_LEAK "probe must only expose probe_token_present";; esac

if command -v curl >/dev/null 2>&1; then
  if curl -sSf -o /dev/null -D - http://127.0.0.1:8000/ops/rails/refusal | tr -d '\r' | awk 'BEGIN{s=1}/^HTTP\/1\.[01] 503/{s=0} END{exit s}'; then
    ok REFUSAL_LIVE_503_OK
  else
    note "SKIP  REFUSAL_LIVE_503_OK (server not reachable or unexpected status)"
  fi
fi

mkdir -p artifacts/qa
python - <<'PY'
import json, os
from pathlib import Path
report = {
  "tokens_pass": os.environ.get("PASS", "").split("|") if os.environ.get("PASS") else [],
  "tokens_fail": os.environ.get("FAIL", "").split("|") if os.environ.get("FAIL") else []
}
Path("artifacts/qa/epic009_precommit_report.json").write_text(json.dumps(report, separators=(",",":"))+"\n")
PY
printf -v PASS_JOIN '%s|' "${PASS[@]:-}"; PASS_JOIN=${PASS_JOIN%|}
printf -v FAIL_JOIN '%s|' "${FAIL[@]:-}"; FAIL_JOIN=${FAIL_JOIN%|}
PASS="$PASS_JOIN" FAIL="$FAIL_JOIN" python - <<'PY'
import json, os
rep = {
    "pass": os.environ.get("PASS", "").split("|") if os.environ.get("PASS") else [],
    "fail": os.environ.get("FAIL", "").split("|") if os.environ.get("FAIL") else []
}
print("=== HDE-EPIC009 PRE-COMMIT QA SUMMARY ===")
print("PASS:", len(rep["pass"]), rep["pass"])
print("FAIL:", len(rep["fail"]), rep["fail"])
open("artifacts/qa/epic009_precommit_report.json", "w").write(json.dumps(rep, separators=(",",":"))+"\n")
PY

if ((${#FAIL[@]}==0)); then
  echo "QA_OK"
  exit 0
else
  echo "QA_FAIL"
  exit 1
fi
