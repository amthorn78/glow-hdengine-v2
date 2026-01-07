# Step Report: HDE-EPIC023__d04-acceptance-alignment-validator-d05-step-logs-manifest

## Step Results

### D04_acceptance_alignment_validator

**Command executed:**
```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC EVIDENCE_ROOT=audit/qa/hde-epic023

CHECK_ID="D04_acceptance_alignment_validator"
LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"
LOG_PATH="${LOG_DIR}/primary.log"
TMP_OUT="${LOG_DIR}/tmp.out"
mkdir -p "${LOG_DIR}"

# Run pytest (no cache provider; no bytecode)
python -m pytest tests/qa/test_epic023_acceptance_alignment.py >"${TMP_OUT}" 2>&1
RC=$?

STATUS="PASS"
INTENDED_TOKENS="[]"
CLAIMED_TOKENS="[]"

# Extract intended tokens from the acceptance map (names-only) without writing outside governed roots
TOK_TMP="${LOG_DIR}/tmp_tokens.json"
python - <<'PY' >"${TOK_TMP}" 2>/dev/null || true
import json, pathlib
p = pathlib.Path("docs/acceptance_map_epic023.json")
obj = json.loads(p.read_text(encoding="utf-8"))
tokens = obj.get("tokens", [])
names = []
for t in tokens:
    if isinstance(t, dict) and "token" in t:
        names.append(t["token"])
print(json.dumps(sorted(set(names))))
PY
INTENDED_TOKENS="$(cat "${TOK_TMP}" 2>/dev/null || echo '[]')"
rm -f "${TOK_TMP}"

if [ "${RC}" -ne 0 ]; then
  STATUS="FAIL_BEHAVIOR"
else
  STATUS="PASS"
  CLAIMED_TOKENS="${INTENDED_TOKENS}"
fi

python - <<PY >"${LOG_PATH}"
import json, os
hdr = {
  "check_id": "${CHECK_ID}",
  "status": "${STATUS}",
  "command": "python -m pytest tests/qa/test_epic023_acceptance_alignment.py (no bytecode) + extract intended tokens",
  "captured_env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE"),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),
    "APP_ENV": os.environ.get("APP_ENV"),
    "LC_ALL": os.environ.get("LC_ALL"),
    "LANG": os.environ.get("LANG"),
    "TZ": os.environ.get("TZ"),
  },
  "pf_refs": [
    "PF14 — HDE-Mechanics Guide, §37.2",
    "PF04 — HDE-Governance (token registry invariants) (titles-only)"
  ],
  "intended_tokens": json.loads("""${INTENDED_TOKENS}"""),
  "claimed_tokens": json.loads("""${CLAIMED_TOKENS}"""),
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

**Status:** FAIL_BEHAVIOR

**Key outputs:**
```
============================= test session starts ==============================
FAILED tests/qa/test_epic023_acceptance_alignment.py::test_epic023_acceptance_alignment_and_bindings
============================== 1 failed in 0.12s ===============================
manifest_upsert: check_id=D04_acceptance_alignment_validator status=FAIL_BEHAVIOR log_path=audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log steps_count=5
D04_acceptance_alignment_validator => FAIL_BEHAVIOR
```

**Note:** Test failed with assertion error: `matrix and acceptance map token sets must match`. The test parser incorrectly treated the header row `token_name` as a data token because the parser skips `Token name` (title case) but the matrix header uses `token_name` (lowercase) after D02 remediation. This is a test parser issue, not a matrix content issue.

---

### D05_step_logs_manifest

**Command executed:**
```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC EVIDENCE_ROOT=audit/qa/hde-epic023

CHECK_ID="D05_step_logs_manifest"
LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"
LOG_PATH="${LOG_DIR}/primary.log"
TMP_OUT="${LOG_DIR}/tmp.out"
MANIFEST="${EVIDENCE_ROOT:?}/qa_step_logs_manifest.json"
PROOF="${MANIFEST}.path_proof.txt"
mkdir -p "${LOG_DIR}"

python - <<'PY' >"${TMP_OUT}" 2>&1
import os, sys, json, hashlib
from pathlib import Path

root = Path(os.environ["EVIDENCE_ROOT"])
manifest = root / "qa_step_logs_manifest.json"
proof = Path(str(manifest) + ".path_proof.txt")

if not manifest.exists():
    print(f"TOOLING_BLOCKED: missing {manifest}")
    sys.exit(3)
if not proof.exists():
    print(f"FAIL_BEHAVIOR: missing path proof {proof}")
    sys.exit(2)

b = manifest.read_bytes()
if len(b) == 0:
    print("FAIL_BEHAVIOR: manifest is empty")
    sys.exit(2)
if not b.endswith(b"\n"):
    print("FAIL_BEHAVIOR: manifest missing trailing LF")
    sys.exit(2)

obj = json.loads(manifest.read_text(encoding="utf-8"))
if not isinstance(obj, dict):
    print("FAIL_BEHAVIOR: manifest JSON must be an object")
    sys.exit(2)

if obj.get("epic_id") != "HDE-EPIC023":
    print(f"FAIL_BEHAVIOR: epic_id mismatch: {obj.get('epic_id')}")
    sys.exit(2)

steps = obj.get("steps")
if not isinstance(steps, list) or len(steps) == 0:
    print("TOOLING_BLOCKED: manifest.steps missing or empty")
    sys.exit(3)

allowed_status = {"PASS","FAIL_BEHAVIOR","FAIL_TOOLING","TOOLING_BLOCKED","PARKED"}

seen = set()
for i, s in enumerate(steps):
    if not isinstance(s, dict):
        print(f"FAIL_BEHAVIOR: steps[{i}] is not an object")
        sys.exit(2)
    for k in ("check_id","status","log_path"):
        if k not in s:
            print(f"FAIL_BEHAVIOR: steps[{i}] missing required field: {k}")
            sys.exit(2)

    cid = s["check_id"]
    st = s["status"]
    lp = s["log_path"]

    if not isinstance(cid, str) or not cid:
        print(f"FAIL_BEHAVIOR: steps[{i}].check_id must be a non-empty string")
        sys.exit(2)
    if cid in seen:
        print(f"FAIL_BEHAVIOR: duplicate check_id in manifest: {cid}")
        sys.exit(2)
    seen.add(cid)

    if st not in allowed_status:
        print(f"FAIL_BEHAVIOR: invalid status for {cid}: {st}")
        sys.exit(2)

    if not isinstance(lp, str) or not lp:
        print(f"FAIL_BEHAVIOR: steps[{i}].log_path must be a non-empty string")
        sys.exit(2)

    # Must live under epic QA root
    if not lp.startswith(root.as_posix() + "/"):
        print(f"FAIL_BEHAVIOR: log_path not under epic QA root: {cid} log_path={lp} root={root.as_posix()}")
        sys.exit(2)

    if not Path(lp).exists():
        print(f"FAIL_BEHAVIOR: referenced log_path does not exist: {cid} log_path={lp}")
        sys.exit(2)

# Path proof must match current bytes (sha256)
sha = hashlib.sha256(b).hexdigest()
proof_txt = proof.read_text(encoding="utf-8", errors="replace")
if f"sha256: {sha}" not in proof_txt:
    print("FAIL_BEHAVIOR: manifest path proof sha256 does not match current manifest bytes")
    sys.exit(2)

print(f"PASS: manifest OK (steps_count={len(steps)}; unique_check_ids={len(seen)}).")
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
  "command": "python (embedded) validate ${MANIFEST} (+ path proof; required fields check_id/status/log_path; uniqueness; existence under epic QA root)",
  "captured_env": {
    "SAFE_MODE": os.environ.get("SAFE_MODE"),
    "ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),
    "APP_ENV": os.environ.get("APP_ENV"),
    "LC_ALL": os.environ.get("LC_ALL"),
    "LANG": os.environ.get("LANG"),
    "TZ": os.environ.get("TZ"),
  },
  "pf_refs": [
    "PF19 — Glow QA Guide, §4.4.3 (titles-only)"
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

**Status:** PASS

**Key outputs:**
```
PASS: manifest OK (steps_count=4; unique_check_ids=4).
manifest_upsert: check_id=D05_step_logs_manifest status=PASS log_path=audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log steps_count=5
D05_step_logs_manifest => PASS
```

---

## Repository Changes

### Summary
- Created primary log for D04_acceptance_alignment_validator (status: FAIL_BEHAVIOR due to test parser/matrix header mismatch)
- Created primary log for D05_step_logs_manifest (status: PASS)
- Updated `qa_step_logs_manifest.json` with D04 and D05 check entries
- Updated `qa_step_logs_manifest.json.path_proof.txt`

### Full changed-files list
- `audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log` (created)
- `audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log` (created)
- `audit/qa/hde-epic023/qa_step_logs_manifest.json` (updated)
- `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt` (updated)

### Diff summary
- D04 primary log: created with FAIL_BEHAVIOR status and pytest transcript showing assertion error (matrix header column name treated as token by test parser)
- D05 primary log: created with PASS status validating manifest structure/content
- Manifest: upserted D04 (FAIL_BEHAVIOR) and D05 (PASS) check entries

---

## Evidence Filedump (complete)

### Path: audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log

```
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D04_acceptance_alignment_validator","claimed_tokens":[],"command":"python -m pytest tests/qa/test_epic023_acceptance_alignment.py (no bytecode) + extract intended tokens","intended_tokens":[],"pf_refs":["PF14 — HDE-Mechanics Guide, §37.2","PF04 — HDE-Governance (token registry invariants) (titles-only)"],"status":"FAIL_BEHAVIOR"}
============================= test session starts ==============================
platform linux -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0
rootdir: /workspaces/glow-hdengine-v2
configfile: pytest.ini
collected 1 item

tests/qa/test_epic023_acceptance_alignment.py F                          [100%]

=================================== FAILURES ===================================
________________ test_epic023_acceptance_alignment_and_bindings ________________

    def test_epic023_acceptance_alignment_and_bindings() -> None:
        matrix_tokens, matrix_duplicates = _parse_matrix()
        acceptance_tokens, acceptance_duplicates = _parse_acceptance_map()
        registry_tokens = _load_registry_tokens()
    
        assert matrix_tokens, "expected token matrix entries"
        assert acceptance_tokens, "expected acceptance map entries"
        assert not matrix_duplicates, f"duplicate matrix tokens: {sorted(matrix_duplicates)}"
        assert not acceptance_duplicates, f"duplicate acceptance map tokens: {sorted(acceptance_duplicates)}"
>       assert set(matrix_tokens) == set(acceptance_tokens), "matrix and acceptance map token sets must match"
E       AssertionError: matrix and acceptance map token sets must match
E       assert {'DETERMINISM...LITY_OK', ...} == {'DETERMINISM...LITY_OK', ...}
E         
E         Extra items in the left set:
E         'token_name'
E         Use -v to get more diff

tests/qa/test_epic023_acceptance_alignment.py:127: AssertionError
=========================== short test summary info ============================
FAILED tests/qa/test_epic023_acceptance_alignment.py::test_epic023_acceptance_alignment_and_bindings
============================== 1 failed in 0.12s ===============================
manifest_upsert: check_id=D04_acceptance_alignment_validator status=FAIL_BEHAVIOR log_path=audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log steps_count=5
```

---

### Path: audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log

```
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"D05_step_logs_manifest","claimed_tokens":[],"command":"python (embedded) validate audit/qa/hde-epic023/qa_step_logs_manifest.json (+ path proof; required fields check_id/status/log_path; uniqueness; existence under epic QA root)","intended_tokens":[],"pf_refs":["PF19 — Glow QA Guide, §4.4.3 (titles-only)"],"status":"PASS"}
PASS: manifest OK (steps_count=4; unique_check_ids=4).
manifest_upsert: check_id=D05_step_logs_manifest status=PASS log_path=audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log steps_count=5
```

---

### Path: audit/qa/hde-epic023/qa_step_logs_manifest.json

```
{"epic_id":"HDE-EPIC023","runs":[{"produced_at_utc":"2026-01-05T03:49:38.236980+00:00","run_id":"viability-check","steps":[{"log_path":"audit/qa/hde-epic023/acceptance_map_viability.log","name":"acceptance_map_viability","status":"PASS"}]}],"steps":[{"check_id":"D02_token_evidence_matrix","log_path":"audit/qa/hde-epic023/checks/D02_token_evidence_matrix/primary.log","status":"PASS"},{"check_id":"D04_acceptance_alignment_validator","log_path":"audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log","status":"FAIL_BEHAVIOR"},{"check_id":"D05_step_logs_manifest","log_path":"audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log","status":"PASS"},{"check_id":"D07_codespaces_snapshot","log_path":"audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log","status":"PASS"},{"check_id":"D08_qa_doc_deltas_capture","log_path":"audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log","status":"PASS"}]}
```

---

### Path: audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt

```
path: audit/qa/hde-epic023/qa_step_logs_manifest.json
sha256: 54388be51f821bcd0c8d26331395bac60b772fbd19ad0e111e1c3c3621528946
size_bytes: 949
mtime_utc: 2026-01-07T19:22:44Z
produced_at_utc: 2026-01-07T19:22:44Z
```
