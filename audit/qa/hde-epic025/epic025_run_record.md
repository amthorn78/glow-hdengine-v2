# HDE-EPIC025 QA Run Record

## Summary of steps taken

1. **Operator setup (Step-0)**
   - Set `EVIDENCE_ROOT` to `audit/qa/hde-epic025`.
   - Created evidence directory structure: `00_meta/` and `checks/`.
   - Wrote canonical step-log header writer.
   - Captured baseline repo snapshot to `00_meta/repo_baseline.txt`.

2. **Step-0A: Evidence root governance**
   - Verified `EVIDENCE_ROOT` is under `audit/`.
   - Created `00_meta/evidence_root_manifest.txt`.

3. **Step-0B: QA step logs manifest**
   - Created `00_meta/doc_deltas.md`.
   - Created `qa_step_logs_manifest.json` stub and path proof.

4. **d0_discovery**
   - Verified Step-0 artifacts and captured transcript in `checks/d0_discovery/primary.log`.
   - Result: PASS.

---

## Evidence outputs

### 00_meta/repo_baseline.txt
```
]633;E;{   echo "timestamp_utc: $(/workspaces/glow-hdengine-v2/.venv/bin/python -c 'import datetime\x3b print(datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z")')"\x3b   echo "git_rev_parse_head:"\x3b   git rev-parse HEAD\x3b   echo "git_status_porcelain:"\x3b   git status --porcelain\x3b } > "${EVIDENCE_ROOT}/00_meta/repo_baseline.txt";b8f1d155-bfa1-4a57-a6f9-98edc0f57ec0]633;Ctimestamp_utc: 2026-02-02T15:20:48Z
git_rev_parse_head:
6fdf0d809d34b19c15eae5d56a89c05c1f24fc37
git_status_porcelain:
 M audit/qa/hde-epic025/qa_step_logs_manifest.json
 M audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt
?? audit/qa/hde-epic025/00_meta/
?? audit/qa/hde-epic025/checks/d0_discovery/
?? "audit/qa/hde-epic025/r43 Live QA Plan HDE-EPIC025.md"
```

### 00_meta/evidence_root_manifest.txt
```
evidence_root_manifest
- all qa-created artifacts for this run live under EVIDENCE_ROOT
- repo files under docs/ and artifacts/ may be read and copied into EVIDENCE_ROOT
- no qa-created files under docs/
```

### 00_meta/doc_deltas.md
```
# doc_deltas

## blockers
- none recorded yet

## caveats
- none recorded yet
```

### 00_meta/write_step_log_header.py
```python
import os, json, datetime
required = ["CHECK_ID","CHECK_NAME","COMMANDS_JSON","PASS_FAIL","ARTIFACTS_JSON","PF_REFS_JSON"]
for k in required:
    if k not in os.environ:
        raise SystemExit("missing env: " + k)
raw_status = os.environ["PASS_FAIL"]
raw_fail_status = os.environ.get("FAIL_STATUS", "")
if raw_status == "pass":
    status = "PASS"
    fail_status = ""
else:
    status = raw_status
if status == "fail":
    status = raw_fail_status if raw_fail_status else "FAIL_BEHAVIOR"
if status == "FAIL_ENVIRONMENT":
    status = "FAIL_TOOLING"
allowed_status = ["PASS","FAIL_BEHAVIOR","FAIL_TOOLING","TOOLING_BLOCKED","SKIPPED","WARN"]
if status not in allowed_status:
    status = "FAIL_BEHAVIOR"
if status == "PASS":
    fail_status = ""
elif status in ["FAIL_BEHAVIOR","FAIL_TOOLING"]:
    fail_status = status
else:
    fail_status = raw_fail_status if raw_fail_status in ["FAIL_BEHAVIOR","FAIL_TOOLING","FAIL_ENVIRONMENT"] else "FAIL_TOOLING"
commands_list = json.loads(os.environ["COMMANDS_JSON"])
command = "\n".join(commands_list) if commands_list else "N/A"
command_provenance = "Copy/paste from plan"
captured_env = {
    "MODO_AI_BUNDLE": os.environ.get("MODO_AI_BUNDLE", ""),
    "MODO_AI_VERBOSE": os.environ.get("MODO_AI_VERBOSE", ""),
    "MODO_RAILS": os.environ.get("MODO_RAILS", ""),
    "LC_ALL": os.environ.get("LC_ALL", ""),
    "LANG": os.environ.get("LANG", ""),
    "TZ": os.environ.get("TZ", ""),
}
hdr = {
    "check_id": os.environ["CHECK_ID"],
    "check_name": os.environ["CHECK_NAME"],
    "captured_env": captured_env,
    "timestamp_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",
    "command": command,
    "command_provenance": command_provenance,
    "status": status,
    "fail_status": fail_status,
    "intended_tokens": [],
    "claimed_tokens": [],
    "artifacts": json.loads(os.environ["ARTIFACTS_JSON"]),
    "pf_refs": json.loads(os.environ["PF_REFS_JSON"]),
}
print(json.dumps(hdr, sort_keys=True))
```

### qa_step_logs_manifest.json
```json
{
  "epic_id": "hde-epic025",
  "generated_utc": "pending",
  "checks": []
}
```

### qa_step_logs_manifest.json.path_proof.txt
```
]633;E;{   echo "ls -la:"\x3b   ls -la "${EVIDENCE_ROOT}/qa_step_logs_manifest.json"\x3b   echo\x3b   echo "sha256sum:"\x3b   sha256sum "${EVIDENCE_ROOT}/qa_step_logs_manifest.json"\x3b } > "${EVIDENCE_ROOT}/qa_step_logs_manifest.json.path_proof.txt";b8f1d155-bfa1-4a57-a6f9-98edc0f57ec0]633;Cls -la:
-rw-rw-rw- 1 vscode vscode 77 Feb  2 15:20 audit/qa/hde-epic025/qa_step_logs_manifest.json

sha256sum:
101ea27678315b19efdde31508c033c1ca8a33aa679de907b0ace83e754e02ce  audit/qa/hde-epic025/qa_step_logs_manifest.json
```

### checks/d0_discovery/primary.log
```log
{"artifacts": ["audit/qa/hde-epic025/00_meta/repo_baseline.txt", "audit/qa/hde-epic025/00_meta/doc_deltas.md", "audit/qa/hde-epic025/qa_step_logs_manifest.json"], "captured_env": {"LANG": "en_US.UTF-8", "LC_ALL": "C", "MODO_AI_BUNDLE": "", "MODO_AI_VERBOSE": "", "MODO_RAILS": "", "TZ": "UTC"}, "check_id": "d0_discovery", "check_name": "d0_discovery", "claimed_tokens": [], "command": "ls -la ${EVIDENCE_ROOT}/00_meta\nls -la ${EVIDENCE_ROOT}\ncat ${EVIDENCE_ROOT}/00_meta/repo_baseline.txt", "command_provenance": "Copy/paste from plan", "fail_status": "", "intended_tokens": [], "pf_refs": ["PF27 \u2014 Canon-Plan-Templates, locator template structure and headings"], "status": "PASS", "timestamp_utc": "2026-02-02T15:21:36Z"}
$ ls -la audit/qa/hde-epic025/00_meta
total 24
drwxrwxrwx+ 2 vscode vscode 4096 Feb  2 15:20 .
drwxrwxrwx+ 4 vscode root   4096 Feb  2 15:20 ..
-rw-rw-rw-  1 vscode vscode   78 Feb  2 15:20 doc_deltas.md
-rw-rw-rw-  1 vscode vscode  204 Feb  2 15:20 evidence_root_manifest.txt
-rw-rw-rw-  1 vscode vscode  773 Feb  2 15:20 repo_baseline.txt
-rw-rw-rw-  1 vscode vscode 1978 Feb  2 15:20 write_step_log_header.py
$ ls -la audit/qa/hde-epic025
total 88
drwxrwxrwx+  4 vscode root    4096 Feb  2 15:20 .
drwxrwxrwx+ 14 vscode root    4096 Jan 28 21:21 ..
drwxrwxrwx+  2 vscode vscode  4096 Feb  2 15:20 00_meta
drwxrwxrwx+ 18 vscode root    4096 Feb  2 15:15 checks
-rw-rw-rw-   1 vscode vscode    77 Feb  2 15:20 qa_step_logs_manifest.json
-rw-rw-rw-   1 vscode vscode   522 Feb  2 15:20 qa_step_logs_manifest.json.path_proof.txt
-rw-rw-rw-   1 vscode vscode 62653 Feb  2 15:20 r43 Live QA Plan HDE-EPIC025.md
$ cat audit/qa/hde-epic025/00_meta/repo_baseline.txt
]633;E;{   echo "timestamp_utc: $(/workspaces/glow-hdengine-v2/.venv/bin/python -c 'import datetime\x3b print(datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z")')"\x3b   echo "git_rev_parse_head:"\x3b   git rev-parse HEAD\x3b   echo "git_status_porcelain:"\x3b   git status --porcelain\x3b } > "${EVIDENCE_ROOT}/00_meta/repo_baseline.txt";b8f1d155-bfa1-4a57-a6f9-98edc0f57ec0]633;Ctimestamp_utc: 2026-02-02T15:20:48Z
git_rev_parse_head:
6fdf0d809d34b19c15eae5d56a89c05c1f24fc37
git_status_porcelain:
 M audit/qa/hde-epic025/qa_step_logs_manifest.json
 M audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt
?? audit/qa/hde-epic025/00_meta/
?? audit/qa/hde-epic025/checks/d0_discovery/
?? "audit/qa/hde-epic025/r43 Live QA Plan HDE-EPIC025.md"
```
