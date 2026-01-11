# HDE-EPIC023 — D07_codespaces_snapshot + D08_qa_doc_deltas_capture — Step Report

## Step Results

- D07_codespaces_snapshot: PASS
  - Primary log: audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log
  - Deliverables:
    - audit/qa/hde-epic023/00_meta/codespaces_snapshot.json
    - audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt
    - audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log
- D08_qa_doc_deltas_capture: PASS
  - Primary log: audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log
  - Deliverables:
    - audit/qa/hde-epic023/00_meta/doc_deltas.md
    - audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt
    - audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log
- Step logs manifest updated by both steps:
  - audit/qa/hde-epic023/qa_step_logs_manifest.json
  - audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt

## Commands/actions executed (in order)

1) CHECK D07_codespaces_snapshot — PO command block executed

```bash
CHECK_ID="D07_codespaces_snapshot"
LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"
LOG_PATH="${LOG_DIR}/primary.log"
TMP_OUT="${LOG_DIR}/tmp.out"
SNAP="${EVIDENCE_ROOT:?}/00_meta/codespaces_snapshot.json"
PROOF="${SNAP}.path_proof.txt"
mkdir -p "${LOG_DIR}" "$(dirname "${SNAP}")"

python - <<'PY' >"${TMP_OUT}" 2>&1
import json, os, sys, pathlib, hashlib, datetime

def utc_now_z():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root = pathlib.Path(os.environ["EVIDENCE_ROOT"])
snap = root / "00_meta" / "codespaces_snapshot.json"
proof = pathlib.Path(str(snap) + ".path_proof.txt")

payload = {
  "schema": "hde.qa.codespaces_snapshot.v1",
  "captured_at_utc": utc_now_z(),
  "repo_root": str(pathlib.Path(".").resolve()),
  "git": {
    "head_sha": os.popen("git rev-parse HEAD").read().strip(),
    "status_porcelain": os.popen("git status --porcelain").read(),
  },
  "env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE"),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),
    "APP_ENV": os.environ.get("APP_ENV"),
    "LC_ALL": os.environ.get("LC_ALL"),
    "LANG": os.environ.get("LANG"),
    "TZ": os.environ.get("TZ"),
    "PYTHONDONTWRITEBYTECODE": os.environ.get("PYTHONDONTWRITEBYTECODE"),
    "PYTHONHASHSEED": os.environ.get("PYTHONHASHSEED"),
  }
}

b = (json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
snap.write_bytes(b)

sha = hashlib.sha256(b).hexdigest()
st = snap.stat()
mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

proof_lines = [
  f"path: {snap.as_posix()}",
  f"sha256: {sha}",
  f"size_bytes: {st.st_size}",
  f"mtime_utc: {mtime_utc}",
  f"produced_at_utc: {utc_now_z()}",
]
proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")

print("PASS: codespaces_snapshot.json + path proof written.")
PY
RC=$?

STATUS="PASS"
case "${RC}" in
  0) STATUS="PASS" ;;
  *) STATUS="FAIL_TOOLING" ;;
esac

python - <<PY >"${LOG_PATH}"
import json, os
hdr = {
  "check_id": "${CHECK_ID}",
  "status": "${STATUS}",
  "command": "python (embedded) generate codespaces_snapshot.json + path proof",
  "captured_env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE"),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),
    "APP_ENV": os.environ.get("APP_ENV"),
    "LC_ALL": os.environ.get("LC_ALL"),
    "LANG": os.environ.get("LANG"),
    "TZ": os.environ.get("TZ"),
    "PYTHONDONTWRITEBYTECODE": os.environ.get("PYTHONDONTWRITEBYTECODE"),
    "PYTHONHASHSEED": os.environ.get("PYTHONHASHSEED"),
  },
  "pf_refs": [
    "PF12 — HDE-Schemas and Artifacts, §8.17.5",
    "PF12 — HDE-Schemas and Artifacts, §8.3",
    "PF19 — Glow QA Guide, §14.4.3"
  ],
  "intended_tokens": [],
  "claimed_tokens": [],
}
print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))
PY
cat "${TMP_OUT}" >>"${LOG_PATH}"
rm -f "${TMP_OUT}"

# Upsert this check into the step-logs manifest (PF19 §4.4.3)
python - <<PY >>"${LOG_PATH}" 2>&1
import json, os, hashlib, datetime
from pathlib import Path

def utc_now_z():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root = Path(os.environ["EVIDENCE_ROOT"])
manifest = root / "qa_step_logs_manifest.json"
proof = Path(str(manifest) + ".path_proof.txt")

epic_id = "HDE-EPIC023"
check_id = "${CHECK_ID}"
status = "${STATUS}"
log_path = "${LOG_PATH}"

now = utc_now_z()

if manifest.exists():
    try:
        obj = json.loads(manifest.read_text(encoding="utf-8"))
    except Exception:
        obj = {"epic_id": epic_id, "steps": []}
else:
    obj = {"epic_id": epic_id, "steps": []}

if not isinstance(obj, dict):
    obj = {"epic_id": epic_id, "steps": []}
obj["epic_id"] = epic_id

steps = obj.get("steps")
if not isinstance(steps, list):
    steps = []
steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]
steps.append({"check_id": check_id, "status": status, "log_path": log_path})
steps.sort(key=lambda s: s.get("check_id",""))
obj["steps"] = steps

data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
manifest.parent.mkdir(parents=True, exist_ok=True)
manifest.write_bytes(data)

sha = hashlib.sha256(data).hexdigest()
st = manifest.stat()
mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
proof_lines = [
    f"path: {manifest.as_posix()}",
    f"sha256: {sha}",
    f"size_bytes: {st.st_size}",
    f"mtime_utc: {mtime_utc}",
    f"produced_at_utc: {now}",
]
proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")

print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")
PY

echo "${CHECK_ID} => ${STATUS}"
```

2) VERIFY D07 deliverables existed (file listing)

```text
== ls D07 outputs ==
-rw-rw-rw- 1 vscode vscode 724 Jan  7 15:39 audit/qa/hde-epic023/00_meta/codespaces_snapshot.json
-rw-rw-rw- 1 vscode vscode 219 Jan  7 15:39 audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt
-rw-rw-rw- 1 vscode vscode 689 Jan  7 15:39 audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log
```

3) CHECK D08_qa_doc_deltas_capture — PO command block executed

```bash
CHECK_ID="D08_qa_doc_deltas_capture"
LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"
LOG_PATH="${LOG_DIR}/primary.log"
TMP_OUT="${LOG_DIR}/tmp.out"
DOC="${EVIDENCE_ROOT:?}/00_meta/doc_deltas.md"
PROOF="${DOC}.path_proof.txt"
mkdir -p "${LOG_DIR}" "$(dirname "${DOC}")"

python - <<'PY' >"${TMP_OUT}" 2>&1
import os, sys, json, hashlib, datetime
from pathlib import Path

def utc_now_z():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root = Path(os.environ["EVIDENCE_ROOT"])
doc = root / "00_meta" / "doc_deltas.md"
proof = Path(str(doc) + ".path_proof.txt")
checks_dir = root / "checks"

deltas = []
if checks_dir.exists():
    for d in sorted([p for p in checks_dir.iterdir() if p.is_dir()]):
        lp = d / "primary.log"
        if not lp.exists():
            continue
        try:
            first = lp.read_text(encoding="utf-8", errors="replace").splitlines()[0]
            hdr = json.loads(first)
            cid = str(hdr.get("check_id", d.name))
            status = str(hdr.get("status", "UNKNOWN"))
        except Exception:
            cid = d.name
            status = "UNPARSEABLE_HEADER"
        if status != "PASS":
            deltas.append(f"- {cid} status={status} (see {lp.as_posix()})")

now = utc_now_z()
lines = []
lines.append("# QA Doc Deltas Capture — HDE-EPIC023")
lines.append("")
lines.append(f"captured_at_utc: {now}")
lines.append(f"scope: current-state deltas observed in check logs under {checks_dir.as_posix()}/")
lines.append("deltas:")
if deltas:
    lines.extend(deltas)
else:
    lines.append("- no deltas")
lines.append("")

doc.write_text("\n".join(lines), encoding="utf-8")

b = doc.read_bytes()
if len(b) == 0:
    print("FAIL_BEHAVIOR: doc_deltas.md is empty after write")
    sys.exit(2)
if not b.endswith(b"\n"):
    print("FAIL_BEHAVIOR: doc_deltas.md missing trailing LF")
    sys.exit(2)

txt = doc.read_text(encoding="utf-8", errors="replace")
for bad in ["TBD", "PLACEHOLDER", "placeholder"]:
    if bad in txt:
        print(f"FAIL_BEHAVIOR: placeholder marker detected: {bad}")
        sys.exit(2)

sha = hashlib.sha256(b).hexdigest()
st = doc.stat()
mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
proof_lines = [
    f"path: {doc.as_posix()}",
    f"sha256: {sha}",
    f"size_bytes: {st.st_size}",
    f"mtime_utc: {mtime_utc}",
    f"produced_at_utc: {now}",
]
proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")

print("PASS: doc_deltas.md + path proof generated and validated.")
PY
RC=$?

STATUS="PASS"
case "${RC}" in
  0) STATUS="PASS" ;;
  2) STATUS="FAIL_BEHAVIOR" ;;
  3) STATUS="TOOLING_BLOCKED" ;;
  *) STATUS="FAIL_TOOLING" ;;
esac

python - <<PY >"${LOG_PATH}"
import json, os
hdr = {
  "check_id": "${CHECK_ID}",
  "status": "${STATUS}",
  "command": "python (embedded) generate+prove+validate ${EVIDENCE_ROOT}/00_meta/doc_deltas.md",
  "captured_env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE"),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),
    "APP_ENV": os.environ.get("APP_ENV"),
    "LC_ALL": os.environ.get("LC_ALL"),
    "LANG": os.environ.get("LANG"),
    "TZ": os.environ.get("TZ"),
  },
  "pf_refs": [
    "PF19 — Glow QA Guide, §14.4.4",
    "PF27 — Plan Templates (Step‑0B posture) (titles-only)"
  ],
  "intended_tokens": [],
  "claimed_tokens": [],
}
print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))
PY
cat "${TMP_OUT}" >>"${LOG_PATH}"
rm -f "${TMP_OUT}"

# Upsert this check into the step-logs manifest (PF19 §4.4.3)
python - <<PY >>"${LOG_PATH}" 2>&1
import json, os, hashlib, datetime
from pathlib import Path

def utc_now_z():
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root = Path(os.environ["EVIDENCE_ROOT"])
manifest = root / "qa_step_logs_manifest.json"
proof = Path(str(manifest) + ".path_proof.txt")

epic_id = "HDE-EPIC023"
check_id = "${CHECK_ID}"
status = "${STATUS}"
log_path = "${LOG_PATH}"

now = utc_now_z()

if manifest.exists():
    try:
        obj = json.loads(manifest.read_text(encoding="utf-8"))
    except Exception:
        obj = {"epic_id": epic_id, "steps": []}
else:
    obj = {"epic_id": epic_id, "steps": []}

if not isinstance(obj, dict):
    obj = {"epic_id": epic_id, "steps": []}
obj["epic_id"] = epic_id

steps = obj.get("steps")
if not isinstance(steps, list):
    steps = []
steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]
steps.append({"check_id": check_id, "status": status, "log_path": log_path})
steps.sort(key=lambda s: s.get("check_id",""))
obj["steps"] = steps

data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")
manifest.parent.mkdir(parents=True, exist_ok=True)
manifest.write_bytes(data)

sha = hashlib.sha256(data).hexdigest()
st = manifest.stat()
mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")
proof_lines = [
    f"path: {manifest.as_posix()}",
    f"sha256: {sha}",
    f"size_bytes: {st.st_size}",
    f"mtime_utc: {mtime_utc}",
    f"produced_at_utc: {now}",
]
proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")

print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")
PY

echo "${CHECK_ID} => ${STATUS}"
```

4) VERIFY D08 deliverables existed (file listing)

```text
== ls D08 outputs ==
-rw-rw-rw- 1 vscode root   185 Jan  7 15:41 audit/qa/hde-epic023/00_meta/doc_deltas.md
-rw-rw-rw- 1 vscode root   208 Jan  7 15:41 audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt
-rw-rw-rw- 1 vscode vscode 630 Jan  7 15:41 audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log
```

5) VERIFY qa_step_logs_manifest exists/updated (file listing)

```text
== ls manifest outputs ==
-rw-rw-rw- 1 vscode vscode 520 Jan  7 15:41 audit/qa/hde-epic023/qa_step_logs_manifest.json
-rw-rw-rw- 1 vscode vscode 213 Jan  7 15:41 audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt
```

6) Capture repository state for report

```bash
git --no-pager status --porcelain
```

Output:

```text
 M .vscode/settings.json
 M audit/qa/hde-epic023/00_meta/doc_deltas.md
 M audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt
 M audit/qa/hde-epic023/qa_step_logs_manifest.json
 M audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt
?? audit/qa/hde-epic023/00_meta/codespaces_snapshot.json
?? audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt
?? audit/qa/hde-epic023/checks/
?? "audit/qa/hde-epic023/r6 v2 QA Plan HDE-EPIC023.md"
?? HDE-EPIC023__d07-codespaces-snapshot-d08-qa-doc-deltas-capture__step_report.md
```

```bash
git --no-pager diff --stat
```

Output:

```text
 .vscode/settings.json                                         |  3 ++-
 audit/qa/hde-epic023/00_meta/doc_deltas.md                    | 19 +++++--------------
 audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt     |  8 ++++----
 audit/qa/hde-epic023/qa_step_logs_manifest.json               | 18 +-----------------
 .../qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt  |  8 ++++----
 5 files changed, 16 insertions(+), 40 deletions(-)
```

```bash
find audit/qa/hde-epic023/checks -type f -maxdepth 3 -print | sort
```

Output:

```text
find: warning: you have specified the global option -maxdepth after the argument -type,
but global options are not positional, i.e., -maxdepth affects tests specified before it as well as those specified after it.  Please specify global options before other arguments.
audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log
audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log
```

## Key outputs (status lines, pass/fail signals, decisive log lines)

From audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log:

- status=PASS (header JSON)
- PASS: codespaces_snapshot.json + path proof written.
- manifest_upsert: check_id=D07_codespaces_snapshot status=PASS log_path=audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log steps_count=1

From audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log:

- status=PASS (header JSON)
- PASS: doc_deltas.md + path proof generated and validated.
- manifest_upsert: check_id=D08_qa_doc_deltas_capture status=PASS log_path=audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log steps_count=2

From audit/qa/hde-epic023/qa_step_logs_manifest.json:

- steps include:
  - D07_codespaces_snapshot: PASS
  - D08_qa_doc_deltas_capture: PASS

## Repository Changes

### Summary of what changed

- Added the epic-level Codespaces snapshot JSON + path-proof transcript.
- Generated/updated the epic-level doc deltas ledger + path proof.
- Created primary step logs for D07 and D08 under audit/qa/hde-epic023/checks/.
- Updated audit/qa/hde-epic023/qa_step_logs_manifest.json and its path proof to include D07 and D08.

### Full changed-files list (repo-relative paths)

- .vscode/settings.json
- audit/qa/hde-epic023/00_meta/codespaces_snapshot.json
- audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt
- audit/qa/hde-epic023/00_meta/doc_deltas.md
- audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt
- audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log
- audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log
- audit/qa/hde-epic023/qa_step_logs_manifest.json
- audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt
- audit/qa/hde-epic023/r6 v2 QA Plan HDE-EPIC023.md
- HDE-EPIC023__d07-codespaces-snapshot-d08-qa-doc-deltas-capture__step_report.md

### Diff summary

- `git diff --stat` is included above.
- Note: new/untracked files (e.g., codespaces_snapshot.json, primary logs, and this report file) do not appear in `git diff --stat`.

## Evidence Filedump (complete)

Path: audit/qa/hde-epic023/00_meta/codespaces_snapshot.json

```json
{"captured_at_utc":"2026-01-07T15:39:45Z","env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","SAFE_MODE":"1","TZ":"UTC"},"git":{"head_sha":"8e4cba987a7aecd60ade00fa3bcb15fc825845c2","status_porcelain":" M .vscode/settings.json\n M audit/qa/hde-epic023/qa_step_logs_manifest.json\n M audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt\n?? audit/qa/hde-epic023/00_meta/codespaces_snapshot.json\n?? audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt\n?? audit/qa/hde-epic023/checks/\n?? \"audit/qa/hde-epic023/r6 v2 QA Plan HDE-EPIC023.md\"\n"},"repo_root":"/workspaces/glow-hdengine-v2","schema":"hde.qa.codespaces_snapshot.v1"}
```

Path: audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt

```text
path: audit/qa/hde-epic023/00_meta/codespaces_snapshot.json
sha256: 0afca92724a91a312cd736ad2c076330e94cf0eec3f700495047f57f87aca902
size_bytes: 724
mtime_utc: 2026-01-07T15:39:45Z
produced_at_utc: 2026-01-07T15:39:45Z

```

Path: audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log

```log
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","PYTHONDONTWRITEBYTECODE":"1","PYTHONHASHSEED":"0","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D07_codespaces_snapshot","claimed_tokens":[],"command":"python (embedded) generate codespaces_snapshot.json + path proof","intended_tokens":[],"pf_refs":["PF12 — HDE-Schemas and Artifacts, §8.17.5","PF12 — HDE-Schemas and Artifacts, §8.3","PF19 — Glow QA Guide, §14.4.3"],"status":"PASS"}
PASS: codespaces_snapshot.json + path proof written.
manifest_upsert: check_id=D07_codespaces_snapshot status=PASS log_path=audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log steps_count=1

```

Path: audit/qa/hde-epic023/00_meta/doc_deltas.md

```markdown
# QA Doc Deltas Capture — HDE-EPIC023

captured_at_utc: 2026-01-07T15:41:00Z
scope: current-state deltas observed in check logs under audit/qa/hde-epic023/checks/
deltas:
- no deltas

```

Path: audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt

```text
path: audit/qa/hde-epic023/00_meta/doc_deltas.md
sha256: 604ff7813ec8960b40e9ebd9a2d66483dbcc80e8e8e07f98c9c44689e97f19c9
size_bytes: 185
mtime_utc: 2026-01-07T15:41:00Z
produced_at_utc: 2026-01-07T15:41:00Z

```

Path: audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log

```log
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D08_qa_doc_deltas_capture","claimed_tokens":[],"command":"python (embedded) generate+prove+validate audit/qa/hde-epic023/00_meta/doc_deltas.md","intended_tokens":[],"pf_refs":["PF19 — Glow QA Guide, §14.4.4","PF27 — Plan Templates (Step‑0B posture) (titles-only)"],"status":"PASS"}
PASS: doc_deltas.md + path proof generated and validated.
manifest_upsert: check_id=D08_qa_doc_deltas_capture status=PASS log_path=audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log steps_count=2

```

Path: audit/qa/hde-epic023/qa_step_logs_manifest.json

```json
{"epic_id":"HDE-EPIC023","runs":[{"produced_at_utc":"2026-01-05T03:49:38.236980+00:00","run_id":"viability-check","steps":[{"log_path":"audit/qa/hde-epic023/acceptance_map_viability.log","name":"acceptance_map_viability","status":"PASS"}]}],"steps":[{"check_id":"D07_codespaces_snapshot","log_path":"audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log","status":"PASS"},{"check_id":"D08_qa_doc_deltas_capture","log_path":"audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log","status":"PASS"}]}

```

Path: audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt

```text
path: audit/qa/hde-epic023/qa_step_logs_manifest.json
sha256: a7a7d703e7bfddfda589546627685ae431df340bc6fc2dec5715e862ae3e4e54
size_bytes: 520
mtime_utc: 2026-01-07T15:41:01Z
produced_at_utc: 2026-01-07T15:41:01Z

```
