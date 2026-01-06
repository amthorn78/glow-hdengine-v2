# HDE-EPIC023 — Step-0 bootstrap: create the runbook helper — Step Report

## Step Results

### Commands/actions executed (in order)

#### Action 1 — Use the Approved Plan’s `EVIDENCE_ROOT` and helper location

Command:
```bash
export EVIDENCE_ROOT="audit/qa/hde-epic023"
mkdir -p "${EVIDENCE_ROOT}/_tools" "${EVIDENCE_ROOT}/00_meta"
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Action 2 — Re-run the Approved Plan’s Step-0 bash block verbatim

Source (Approved Plan): `docs/QA Plans/r6 Live QA Plan HDE-EPIC023.md` → “Step‑0 bootstrap: create the runbook helper”

Command (verbatim fenced `bash` block):
```bash
mkdir -p "${EVIDENCE_ROOT}/_tools"

cat > "${EVIDENCE_ROOT}/_tools/qa_check.sh" <<'EOF'
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
EOF

chmod +x "${EVIDENCE_ROOT}/_tools/qa_check.sh"
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Action 3 — Ensure CAV-001 PF27 structure mapping artifact is under the canonical QA meta location

Command (exactly as provided in the remediation text):
```bash
cp -f "audit/qa/hde-epic023/hde_epic023_qa_step_0/00_meta/pf27_structure_mapping.md" \
  "audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md"
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Action 4 — Presence/permission verification + repo status capture

Command:
```bash
ls -la audit/qa/hde-epic023/_tools/qa_check.sh audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md

git status --porcelain=v1
```

Terminal output:
```
-rw-rw-rw- 1 vscode vscode  689 Jan  6 01:42 audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md
-rwxrwxrwx 1 vscode vscode 3962 Jan  6 01:41 audit/qa/hde-epic023/_tools/qa_check.sh

?? audit/qa/hde-epic023/00_
meta/pf27_structure_mapping.md                        ?? audit/qa/hde-epic023/_to
ols/                       ?? audit/qa/hde-epic023/hde
_epic023_qa_step_0/        ?? "docs/QA Plans/"
```

Exit code:
```
0
```

### Key outputs (status lines, pass/fail signals, decisive log lines)

- Helper created at the plan-required path: `audit/qa/hde-epic023/_tools/qa_check.sh` (executable bit set).
- CAV-001 PF27 structure mapping present at the plan-required meta path: `audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md`.

### Final step outcome: PASS / FAIL / NEEDS REMEDIATION

PASS

## Repository Changes

### Summary of what changed

- Created/updated the plan-required runbook helper at `audit/qa/hde-epic023/_tools/qa_check.sh`.
- Created/updated the plan-required PF27 mapping artifact at `audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md`.

### Full changed-files list (repo-relative paths)

- audit/qa/hde-epic023/_tools/qa_check.sh
- audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md
- audit/qa/hde-epic023/HDE-EPIC023__step-0-bootstrap-create-the-runbook-helper__step_report.md

### Diff summary (or include diffs if they are already captured as files)

- `git diff --stat` (no output)
- `git diff` (no output)

## Evidence Filedump (complete)

### Path: audit/qa/hde-epic023/_tools/qa_check.sh

Contents:
```bash
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
```

### Path: audit/qa/hde-epic023/00_meta/pf27_structure_mapping.md

Contents:
```markdown
# pf27 structure mapping evidence (cav-001)

Purpose: Evidence artifact required by Approval Doc CAV-001. It maps PF27 required sections to the approved plan’s actual sections, or marks them missing. This artifact blocks any claim that the plan is PF27-format compliant when any required section is marked MISSING.

## mapping

- front matter: MISSING
- scope statement: MISSING
- pf23 anchors trace section: MISSING
- po inputs needed: MISSING
- evidence posture + directory structure: PARTIAL
  - mapped to: "2) Execution rails" → "Evidence root (required; defined for this plan)" and "Evidence rails"
- runbook check matrix: MISSING
- check blocks: FOUND
  - mapped to: "4) Checks"
```
