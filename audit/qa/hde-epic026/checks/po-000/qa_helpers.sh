#!/usr/bin/env bash
set -euo pipefail

: "${EVIDENCE_ROOT:?EVIDENCE_ROOT is not set}"

qa_sha256_file() {
  local path="$1"
  sha256sum "$path" | awk '{print $1}'
}

qa_emit_step_log_header() {
  local ts
  ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  python - <<'PY'
import json, os, datetime
hdr = {
  "schema": "pf27-step-log-header-v1",
  "schema_version": "pf27.step_log_header.v1",
  "timestamp_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
  "captured_env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE", ""),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK", ""),
    "APP_ENV": os.environ.get("APP_ENV", ""),
    "LC_ALL": os.environ.get("LC_ALL", ""),
    "LANG": os.environ.get("LANG", ""),
    "TZ": os.environ.get("TZ", ""),
  },
  "check_id": os.environ.get("CHECK_ID", ""),
  "check_name": os.environ.get("CHECK_NAME", ""),
  "pass_fail": os.environ.get("PASS_FAIL", ""),
  "fail_status": os.environ.get("FAIL_STATUS", ""),
  "intended_tokens": __import__("json").loads(os.environ.get("INTENDED_TOKENS_JSON", "[]")),
  "claimed_tokens": __import__("json").loads(os.environ.get("CLAIMED_TOKENS_JSON", "[]")),
  "commands": __import__("json").loads(os.environ.get("COMMANDS_JSON", "[]")),
  "artifacts": __import__("json").loads(os.environ.get("ARTIFACTS_JSON", "[]")),
  "pf_refs": __import__("json").loads(os.environ.get("PF_REFS_JSON", "[]")),
}
print(json.dumps(hdr, ensure_ascii=False))
print()
print("###")
PY
}

qa_manifest_path() {
  echo "$EVIDENCE_ROOT/checks/po-000/qa_step_logs_manifest.json"
}

qa_manifest_proof_path() {
  echo "$EVIDENCE_ROOT/checks/po-000/qa_step_logs_manifest.json.path_proof.txt"
}

qa_write_manifest_path_proof() {
  local manifest_path proof_path sha
  manifest_path="$(qa_manifest_path)"
  proof_path="$(qa_manifest_proof_path)"
  sha="$(qa_sha256_file "$manifest_path")"
  local manifest_abs
  manifest_abs="$(python -c 'import pathlib,sys; print(pathlib.Path(sys.argv[1]).resolve())' "$manifest_path")"
  {
    printf 'manifest_path=%s\n' "$manifest_abs"
    printf 'manifest_sha256=%s\n' "$sha"
  } > "$proof_path"
}

qa_init_manifest() {
  local manifest_path
  manifest_path="$(qa_manifest_path)"
  if [ ! -f "$manifest_path" ]; then
    python - <<'PY' > "$manifest_path"
import datetime, json
print(json.dumps({
  "schema_version": "pf27.qa_step_logs_manifest.v1",
  "generated_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
  "checks": [],
}, ensure_ascii=False, indent=2) + "\n")
PY
  fi
  qa_write_manifest_path_proof
}

qa_append_manifest() {
  local check_id status log_path sha256 manifest_path
  check_id="$1"
  status="$2"
  log_path="$3"
  sha256="$4"
  manifest_path="$(qa_manifest_path)"
  python - "$manifest_path" "$check_id" "$status" "$log_path" "$sha256" <<'PY'
import datetime, json, pathlib, sys
manifest_path = pathlib.Path(sys.argv[1])
check_id = sys.argv[2]
status = sys.argv[3]
log_path = sys.argv[4]
sha256 = sys.argv[5]
data = json.loads(manifest_path.read_text(encoding="utf-8"))
data.setdefault("checks", []).append({
  "timestamp_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
  "check_id": check_id,
  "status": status,
  "log_path": log_path,
  "sha256": sha256,
})
manifest_path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
PY
  qa_write_manifest_path_proof
}
