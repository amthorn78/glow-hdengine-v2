#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  qa_check.sh \
    --check-id <ID> \
    --check-name <NAME> \
    --surface <SURFACE> \
    --pf-refs <PF_REFS> \
    --intended-tokens <TOKENS> \
    --out-dir <OUT_DIR> \
    --cmd-bundle "<COMMANDS...>"

Notes:
  - Reads a command bundle from stdin if --cmd-bundle is not provided.
  - Writes PF19-style logs under OUT_DIR/primary.log
  - First line of primary.log is JSON header (includes: check_id, status, command, captured_env).
  - Status uses PF19 stable statuses:
      PASS | FAIL_BEHAVIOR | FAIL_TOOLING | TOOLING_BLOCKED
USAGE
}

check_id=""
check_name=""
surface=""
pf_refs=""
intended_tokens=""
out_dir=""
cmd_bundle=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --check-id) check_id="$2"; shift 2 ;;
    --check-name) check_name="$2"; shift 2 ;;
    --surface) surface="$2"; shift 2 ;;
    --pf-refs) pf_refs="$2"; shift 2 ;;
    --intended-tokens) intended_tokens="$2"; shift 2 ;;
    --out-dir) out_dir="$2"; shift 2 ;;
    --cmd-bundle) cmd_bundle="$2"; shift 2 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; usage; exit 2 ;;
  esac
done

if [[ -z "${check_id}" || -z "${check_name}" || -z "${surface}" || -z "${out_dir}" ]]; then
  echo "Missing required args" >&2
  usage
  exit 2
fi

mkdir -p "${out_dir}"
log_path="${out_dir}/primary.log"

if [[ -z "${cmd_bundle}" ]]; then
  cmd_bundle="$(cat)"
fi

tmp_out="${out_dir}/cmd.stdout"
tmp_err="${out_dir}/cmd.stderr"
tmp_rc="${out_dir}/cmd.rc"

start_utc="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

set +e
bash -lc "${cmd_bundle}" >"${tmp_out}" 2>"${tmp_err}"
rc=$?
set -e

end_utc="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"

# PF19 stable status mapping:
# - PASS: rc==0
# - TOOLING_BLOCKED: rc==2 (commonly used by plan scripts for "missing required artifact/tooling precondition")
# - FAIL_BEHAVIOR: rc==3 (commonly used by plan scripts for "proof fact mismatch / content invalid")
# - FAIL_TOOLING: anything else (unexpected crash / command error)
status="FAIL_TOOLING"
if [[ $rc -eq 0 ]]; then
  status="PASS"
elif [[ $rc -eq 2 ]]; then
  status="TOOLING_BLOCKED"
elif [[ $rc -eq 3 ]]; then
  status="FAIL_BEHAVIOR"
fi

# Normalize command bundle to avoid raw newlines in JSON
cmd_bundle="${cmd_bundle//$'\n'/\\n}"

# Convert pf_refs and tokens into JSON arrays safely via python.
export CHECK_ID="${check_id}"
export CHECK_NAME="${check_name}"
export SURFACE="${surface}"
export CMD="${cmd_bundle}"
export PF_REFS="${pf_refs}"
export TOKENS="${intended_tokens}"
export STATUS="${status}"
export START_UTC="${start_utc}"
export END_UTC="${end_utc}"
export EXIT_CODE="${rc}"

python - <<PY > "${log_path}"
import json, os

def split_csv(s: str):
    s = (s or "").strip()
    if not s:
        return []
    return [x.strip() for x in s.split(",") if x.strip()]

pf_list = split_csv(os.environ.get("PF_REFS", ""))
tok_list = split_csv(os.environ.get("TOKENS", ""))

status = os.environ["STATUS"]

header = {
  "check_id": os.environ["CHECK_ID"],
  "check_name": os.environ["CHECK_NAME"],
  "surface": os.environ["SURFACE"],
  "command": os.environ["CMD"],
  "captured_env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE",""),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK",""),
    "LC_ALL": os.environ.get("LC_ALL",""),
    "LANG": os.environ.get("LANG",""),
    "TZ": os.environ.get("TZ",""),
  },
  "pf_refs": pf_list,
  "intended_tokens": tok_list,
  "claimed_tokens": (tok_list if status == "PASS" else []),
  "status": status,
  "start_time_utc": os.environ["START_UTC"],
  "end_time_utc": os.environ["END_UTC"],
  "exit_code": int(os.environ["EXIT_CODE"]),
}
print(json.dumps(header, sort_keys=True))
PY

{
  echo ""
  echo "== STDOUT =="
  cat "${tmp_out}"
  echo ""
  echo "== STDERR =="
  cat "${tmp_err}"
  echo ""
  echo "== RC =="
  cat <<RC
${rc}
RC
} >> "${log_path}"

# One-line summary (human)
printf "CHECK=%s STATUS=%s RC=%s OUT=%s\n" "${check_id}" "${status}" "${rc}" "${out_dir}"
