# HDE-EPIC023 / Calcination Pass 5 — Step-0 bootstrap: create the runbook helper — Step Report

## Step Results

### Commands/actions executed (in order)

#### Action 1 — Export the step-local root

Command:
```bash
export EVIDENCE_ROOT="audit/qa/hde-epic023/hde_epic023_qa_step_0"
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Action 2 — Create required directories

Command:
```bash
mkdir -p "${EVIDENCE_ROOT}/tools" "${EVIDENCE_ROOT}/00_meta"
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Action 3 — Create the runbook helper script (initial run)

Command (as provided in the step; executed literally):
```bash
cat > "${EVIDENCE_ROOT}/tools/qa_check.sh" <<'EOF'
...
EOF
EOF
```

Terminal output:
```
bash: EOF: command not found
```

Exit code:
```
127
```

#### Action 3 (chmod) — Mark the helper script executable

Command:
```bash
chmod +x "${EVIDENCE_ROOT}/tools/qa_check.sh"
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Action 4 — Create the CAV-001 PF27 structure mapping evidence artifact

Command:
```bash
cat > "${EVIDENCE_ROOT}/00_meta/pf27_structure_mapping.md" <<'EOF'
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
EOF
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

#### Remediation — Repeat Action 3 to achieve the step’s “exit code 0” expectation

Rationale:
- The provided Action 3 command text includes a duplicate trailing `EOF` line after the heredoc terminator.
- When executed literally, that trailing `EOF` is interpreted as a shell command, producing the non-zero exit shown above.

Remediation applied:
- Re-ran the Action 3 write so the heredoc terminator is present once (single `EOF`) and the command returns exit code `0`, while producing the intended `qa_check.sh` file at the same required output path.

Command (remediated execution used):
```bash
cat > "${EVIDENCE_ROOT}/tools/qa_check.sh" <<'EOF'
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
    "APP_ENV": os.environ.get("APP_ENV",""),
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
```

Terminal output:
```
(no output)
```

Exit code:
```
0
```

### Key outputs (status lines, pass/fail signals, decisive log lines)

Post-remediation verification transcript:
```
-- ls -la --
-rw-rw-rw- 1 vscode vscod
e  689 Jan  6 01:02 audit/qa/hde-epic023/hde_epic023_qa_step_0/00_meta/pf27_structure_mapping.md    -rwxrwxrwx 1 vscode vscod
e 4007 Jan  6 01:02 audit/qa/hde-epic023/hde_epic023_qa_step_0/tools/qa_check.sh                    
-- exec bit --
OK: qa_check.sh is execut
able                     
-- CAV-007 APP_ENV grep -
-                        OK: APP_ENV key present i
n qa_check.sh            
-- mapping non-empty --
OK: pf27_structure_mappin
g.md is non-empty        
-- find evidence files --
audit/qa/hde-epic023/hde_
epic023_qa_step_0/00_meta/pf27_structure_mapping.md                        audit/qa/hde-epic023/hde_
epic023_qa_step_0/HDE-EPIC023__step-0-bootstrap-create-the-runbook-helper__step_report.md           audit/qa/hde-epic023/hde_
epic023_qa_step_0/tools/qa_check.sh               
-- git status porcelain -
-                        ?? audit/qa/hde-epic023/h
de_epic023_qa_step_0/    
-- wc -l --
 155 audit/qa/hde-epic023
/hde_epic023_qa_step_0/tools/qa_check.sh            15 audit/qa/hde-epic023
/hde_epic023_qa_step_0/00_meta/pf27_structure_mapping.md                    170 total
```

### Final step outcome: PASS / FAIL / NEEDS REMEDIATION

PASS

## Repository Changes

### Summary of what changed

- Created/updated Step-0 artifacts under `audit/qa/hde-epic023/hde_epic023_qa_step_0/`.
- Created/updated `tools/qa_check.sh` and set executable bit.
- Created/updated `00_meta/pf27_structure_mapping.md`.
- Updated this step report file to reflect remediation and PASS outcome.

### Full changed-files list (repo-relative paths)

- audit/qa/hde-epic023/hde_epic023_qa_step_0/tools/qa_check.sh
- audit/qa/hde-epic023/hde_epic023_qa_step_0/00_meta/pf27_structure_mapping.md
- audit/qa/hde-epic023/hde_epic023_qa_step_0/HDE-EPIC023__step-0-bootstrap-create-the-runbook-helper__step_report.md

### Diff summary (or include diffs if they are already captured as files)

- `git diff` is empty because the artifacts for this step are untracked (per `git status --porcelain=v1`).

## Evidence Filedump (complete)

### Path: audit/qa/hde-epic023/hde_epic023_qa_step_0/tools/qa_check.sh

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
    "APP_ENV": os.environ.get("APP_ENV",""),
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

### Path: audit/qa/hde-epic023/hde_epic023_qa_step_0/00_meta/pf27_structure_mapping.md

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
