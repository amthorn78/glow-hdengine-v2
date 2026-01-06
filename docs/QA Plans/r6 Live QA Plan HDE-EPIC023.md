## Revised Live QA Plan (complete resubmission text)

# Live QA Plan HDE-EPIC023

> **Scope:** This plan is a *strict* execution runbook for EPIC023 Live QA.
> **Mode:** Editorial resubmission per Lead Review (r1).
> **Inputs:** This plan is self-contained; all execution-critical commands + deliverable paths are embedded here.

---

## 1) Provenance, precedence, and constraints

### Precedence (highest → lowest)

1. **PF docs** (PF10, PF19, PF27) — authoritative for format and rules.
2. **This runbook** — authoritative for *execution* of this QA run.
3. **Other documents** (if referenced) — **provenance only; not required to execute**.

### Non-PF references (provenance only)

* “QA Audit HDE-EPIC023.md” is provenance only; not required to execute (what paths/tools/scripts currently exist).

### Hard constraints

* Use **only** the commands and file paths explicitly listed here.
* Do **not** consult PF documents during execution; PF references are included only for traceability.
* Do **not** invent acceptance tokens; only use tokens explicitly defined as in-scope for EPIC023.

---

## 2) Execution rails

### Environment rails (must be enforced for every check)

* `SAFE_MODE=1`
* `ALLOW_NETWORK=0`
* `APP_ENV=dev`
* `LC_ALL=C`
* `LANG=C`
* `TZ=UTC`

### Evidence root (required; defined for this plan)

All run-produced QA evidence artifacts (step logs, stdout/stderr/rc captures, helper tooling) are written under this concrete root:

```bash
export EVIDENCE_ROOT="audit/qa/hde-epic023"
```

### Evidence rails

* All check evidence must be written under `${EVIDENCE_ROOT}` (see Step‑0).
* Every check must produce a `primary.log` whose **first line** is a JSON header containing (at minimum):
  `check_id`, `status`, `command`, `captured_env`.
* `status` **must** be one of the PF19 stable statuses:
  `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`.
* Token claiming behavior: **claim tokens only on `PASS`**.

---

## 3) What this runbook reads/validates (non-exhaustive)

This runbook is structured to validate the EPIC023 guide deliverable set **D01–D16** as the primary contract. See the deliverable steps in **Section 4** for the definitive per-deliverable artifact paths and PASS/FAIL criteria.

---

### Mandatory Step‑0 artifacts

#### Step‑0 bootstrap: create the runbook helper

> This helper writes PF19-style evidence logs and ensures every check writes a `primary.log` with a JSON first-line header using PF19 stable statuses.

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

---

## 4) Checks

> Each check is executed via `${EVIDENCE_ROOT}/_tools/qa_check.sh` and produces a PF19-style `primary.log` with a PF19-stable status value.

---

### Preflight checks (Pxx) — rails/tooling only (non-deliverable)

#### CHECK p01_tooling_available: Required Tooling Available

**Goal:** Ensure python and core tooling are available.

**PO actions:**

1. Confirm python is available.
2. Confirm basic repo tooling directories are visible.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "p01_tooling_available" \
  --check-name "P01 — Required Tooling Available" \
  --surface "runtime" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/p01_tooling_available" <<'CMD'
python --version
ls -la tools || true
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout shows a python version line.
**FAIL criteria:** `primary.log` status is not `PASS` (capture stdout/stderr in the produced evidence files).

---

#### CHECK p02_env_rails: Environment Rails Are Enforced

**Goal:** Confirm required environment rails are set.

**PO actions:**

1. Confirm required environment variables are set exactly.

```bash
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC \
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "p02_env_rails" \
  --check-name "P02 — Environment Rails Are Enforced" \
  --surface "env" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/p02_env_rails" <<'CMD'
python - <<'PY'
import os, sys
req = {
  "SAFE_MODE":"1",
  "ALLOW_NETWORK":"0",
  "APP_ENV":"dev",
  "LC_ALL":"C",
  "LANG":"C",
  "TZ":"UTC",
}
bad=[]
for k,v in req.items():
    if os.environ.get(k) != v:
        bad.append((k, os.environ.get(k), v))
if bad:
    print("ERR: env rails mismatch:", bad)
    sys.exit(3)
print("OK: env rails enforced")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: env rails enforced`.
**FAIL criteria:** `primary.log` status is not `PASS` (capture stdout/stderr).

---

#### CHECK p03_no_network: Network Must Be Disabled

**Goal:** Confirm network is not used during checks (ALLOW_NETWORK=0).

**PO actions:**

1. Ensure ALLOW_NETWORK=0 is set and enforced.

```bash
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC \
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "p03_no_network" \
  --check-name "P03 — Network Must Be Disabled" \
  --surface "env" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/p03_no_network" <<'CMD'
python - <<'PY'
import os, sys
if os.environ.get("ALLOW_NETWORK") != "0":
    print("ERR: ALLOW_NETWORK must be 0")
    sys.exit(3)
print("OK: ALLOW_NETWORK=0")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: ALLOW_NETWORK=0`.
**FAIL criteria:** `primary.log` status is not `PASS` (capture stdout/stderr).

---

#### CHECK p04_artifact_presence: Artifact-Based Gating (Gitless)

**Goal:** Replace git-based “repo cleanliness” with artifact-based gating: confirm the key governed artifacts referenced by deliverable checks exist as filesystem objects.

**PO actions:**

1. Confirm key governed artifacts exist (gitless).

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "p04_artifact_presence" \
  --check-name "P04 — Artifact-Based Gating (Gitless)" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/p04_artifact_presence" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

required = [
  # D01–D08
  Path("docs/acceptance_map_epic023.json"),
  Path("audit/qa/hde-epic023/token_evidence_matrix.md"),
  Path("audit/qa/hde-epic023/acceptance_map_viability.log"),
  Path("audit/qa/hde-epic023/qa_step_logs_manifest.json"),
  Path("audit/qa/hde-epic023/evidence_index_snapshot.json"),
  Path("audit/qa/hde-epic023/00_meta/doc_deltas_meta.md"),
  Path("audit/qa/hde-epic023/00_meta/pf20_update.md"),
  Path("audit/qa/hde-epic023/00_meta/pf23_consult.md"),

  # D09
  Path("audit/gates/canonical_json"),

  # D10
  Path("docs/evidence/INDEX.json"),
  Path("audit/index/evidence_index.jsonl"),
  Path("audit/index/evidence_index.hashes.json"),
  Path("audit/hashes/evidence_hash_sentinel.json"),
  Path("audit/evidence_index_mirror.md"),

  # D11–D12
  Path("audit/gates/topology/orientation_demo.txt"),
  Path("audit/gates/determinism/env_pins.log"),

  # D13
  Path("artifacts/sanity/sanity.log"),
  Path("artifacts/sanity/sanity_pipeline_evidence.md"),

  # D14
  Path("artifacts/ops/internal_version"),

  # D15
  Path("tests/qa/test_epic023_acceptance_alignment.py"),

  # D16
  Path("audit/EPIC-023_close_report.md"),
  Path("audit/EPIC-023_MANIFEST.json"),
]

missing = []
for p in required:
    if p.is_dir():
        if not p.exists():
            missing.append(str(p))
    else:
        if not p.is_file():
            missing.append(str(p))

if missing:
    print("ERR: missing required artifact(s):")
    for m in missing:
        print(" -", m)
    sys.exit(2)

print("OK: required artifacts present (gitless)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: required artifacts present (gitless)`.
**FAIL criteria:** `primary.log` status is `TOOLING_BLOCKED` and stdout lists missing artifacts (capture evidence; do not substitute git commands).

---

### Deliverable checks (D01–D16) — guide deliverables as primary contract

> **Note:** Deliverable IDs D01–D16 are treated as the primary contract; preflight/rails checks are Pxx and do not reuse deliverable IDs.

---

#### DELIVERABLE D01 — Acceptance Map Presence + Parse

**Goal:** Validate EPIC023 acceptance map exists and parses.

**PO actions:**

1. Confirm `docs/acceptance_map_epic023.json` exists and is parseable JSON.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d01_acceptance_map" \
  --check-name "D01 — Acceptance Map Presence + Parse" \
  --surface "filesystem" \
  --pf-refs "PF10, PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d01_acceptance_map" <<'CMD'
python - <<'PY'
from pathlib import Path
import json
import sys

p = Path("docs/acceptance_map_epic023.json")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

try:
    json.loads(p.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERR: JSON parse failed: {e}")
    sys.exit(3)

print("OK: acceptance map present + parseable")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: acceptance map present + parseable`.
**FAIL criteria:** `primary.log` status is not `PASS` (capture stdout/stderr; missing file = `TOOLING_BLOCKED`, parse/content failure = `FAIL_BEHAVIOR`).

**Required deliverables (validated by this step):**

* `docs/acceptance_map_epic023.json`

---

#### DELIVERABLE D02 — Token↔Evidence Matrix (Guide D02)

**Goal:** Validate the token↔evidence matrix exists at the guide-required path and that its token roster matches D01 exactly (no duplicates; no extra/missing tokens).

**PO actions:**

1. Confirm the matrix file exists at `audit/qa/hde-epic023/token_evidence_matrix.md`.
2. Confirm its token roster matches the D01 acceptance map token roster **exactly**.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d02_token_evidence_matrix" \
  --check-name "D02 — Token↔Evidence Matrix (matches D01)" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d02_token_evidence_matrix" <<'CMD'
python - <<'PY'
from pathlib import Path
import json, re, sys
from typing import Any, List

token_re = re.compile(r"^[A-Z][A-Z0-9_]{2,}$")

def find_token_lists(obj: Any) -> List[List[str]]:
    hits = []
    if isinstance(obj, dict):
        for v in obj.values():
            hits.extend(find_token_lists(v))
    elif isinstance(obj, list):
        if obj and all(isinstance(x, str) for x in obj):
            if all(token_re.match(x.strip()) for x in obj):
                hits.append([x.strip() for x in obj])
        for v in obj:
            hits.extend(find_token_lists(v))
    return hits

# Load D01 acceptance map
am_path = Path("docs/acceptance_map_epic023.json")
if not am_path.is_file():
    print(f"ERR: missing {am_path}")
    sys.exit(2)

try:
    am = json.loads(am_path.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERR: acceptance map not parseable JSON: {e}")
    sys.exit(3)

token_lists = find_token_lists(am)
# EPIC023 roster expected to be 8 tokens; select a single unambiguous length-8 roster.
candidates = []
for lst in token_lists:
    uniq = []
    for t in lst:
        if t not in uniq:
            uniq.append(t)
    if len(uniq) == 8:
        candidates.append(uniq)

# De-dup identical candidate lists (by set)
uniq_sets = []
for c in candidates:
    s = tuple(sorted(set(c)))
    if s not in uniq_sets:
        uniq_sets.append(s)

if len(uniq_sets) != 1:
    print("ERR: unable to unambiguously derive the 8-token roster from D01 acceptance map JSON")
    print(f"Found {len(uniq_sets)} distinct length-8 token-roster candidates")
    sys.exit(2)

d01_tokens = set(uniq_sets[0])

# Load D02 token evidence matrix and extract tokens from table first column/backticks
m_path = Path("audit/qa/hde-epic023/token_evidence_matrix.md")
if not m_path.is_file():
    print(f"ERR: missing {m_path}")
    sys.exit(2)

txt = m_path.read_text(encoding="utf-8", errors="replace")

tokens_found = []

# 1) table-like rows: | TOKEN | ...
for line in txt.splitlines():
    if line.strip().startswith("|"):
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if parts:
            cell = parts[0].strip().strip("`").strip()
            if token_re.match(cell):
                tokens_found.append(cell)

# 2) backticks (fallback)
for m in re.findall(r"`([A-Z][A-Z0-9_]{2,})`", txt):
    if token_re.match(m):
        tokens_found.append(m)

d02_tokens = []
for t in tokens_found:
    if t not in d02_tokens:
        d02_tokens.append(t)

if not d02_tokens:
    print("ERR: no tokens detected in token_evidence_matrix.md")
    sys.exit(3)

d02_set = set(d02_tokens)

missing = sorted(d01_tokens - d02_set)
extra = sorted(d02_set - d01_tokens)

if missing or extra:
    print("ERR: token set mismatch vs D01")
    if missing:
        print(" - missing in D02:", missing)
    if extra:
        print(" - extra in D02:", extra)
    sys.exit(3)

# Duplicate-row check (tokens_found may contain repeats; enforce one-row-per-token expectation)
dups = sorted({t for t in tokens_found if tokens_found.count(t) > 1})
if dups:
    print("ERR: duplicate token rows detected in D02:", dups)
    sys.exit(3)

print("OK: D02 token set matches D01 exactly (8 tokens; no missing/extra/duplicate)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: D02 token set matches D01 exactly (8 tokens; no missing/extra/duplicate)`.
**FAIL criteria:**

* `TOOLING_BLOCKED`: matrix missing or D01 token roster cannot be derived unambiguously.
* `FAIL_BEHAVIOR`: mismatch/duplicate tokens (capture stdout/stderr).

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/token_evidence_matrix.md`

---

#### DELIVERABLE D03 — Acceptance Map Viability Log (Guide D03)

**Goal:** Validate the acceptance viability log exists and includes the guide-required viability summary proof line.

**PO actions:**

1. Confirm `audit/qa/hde-epic023/acceptance_map_viability.log` exists and contains the decisive summary line.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d03_acceptance_map_viability" \
  --check-name "D03 — Acceptance Map Viability Log" \
  --surface "filesystem" \
  --pf-refs "PF10, PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d03_acceptance_map_viability" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

p = Path("audit/qa/hde-epic023/acceptance_map_viability.log")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

txt = p.read_text(encoding="utf-8", errors="replace")
needle = "summary: COVERED=8 PLANNED=0 MISSING=0"
if needle not in txt:
    print("ERR: missing required viability summary line:")
    print(needle)
    sys.exit(3)

print("OK: viability log contains required summary line")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: viability log contains required summary line`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`) or missing summary line (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/acceptance_map_viability.log`

---

#### DELIVERABLE D04 — QA Step Logs Manifest (Guide D04)

**Goal:** Validate the QA step logs manifest exists, parses as JSON, and includes a pointer entry containing the exact viability log path string.

**PO actions:**

1. Confirm `audit/qa/hde-epic023/qa_step_logs_manifest.json` exists and parses as JSON.
2. Confirm it contains the exact string path: `audit/qa/hde-epic023/acceptance_map_viability.log`.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d04_step_logs_manifest" \
  --check-name "D04 — QA Step Logs Manifest" \
  --surface "filesystem" \
  --pf-refs "PF10, PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d04_step_logs_manifest" <<'CMD'
python - <<'PY'
from pathlib import Path
import json, sys

p = Path("audit/qa/hde-epic023/qa_step_logs_manifest.json")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

try:
    obj = json.loads(p.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERR: JSON parse failed: {e}")
    sys.exit(3)

s = json.dumps(obj, sort_keys=True)
needle = "audit/qa/hde-epic023/acceptance_map_viability.log"
if needle not in s:
    print("ERR: manifest does not include required viability log pointer string:")
    print(needle)
    sys.exit(3)

print("OK: step logs manifest includes required viability log pointer string")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: step logs manifest includes required viability log pointer string`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`), JSON parse failure or missing pointer (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/qa_step_logs_manifest.json`

---

#### DELIVERABLE D05 — Evidence Index Snapshot (Guide D05)

**Goal:** Validate the evidence index snapshot exists at the guide-required path and parses as non-empty JSON.

**PO actions:**

1. Confirm `audit/qa/hde-epic023/evidence_index_snapshot.json` exists and is parseable JSON.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d05_evidence_index_snapshot" \
  --check-name "D05 — Evidence Index Snapshot" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d05_evidence_index_snapshot" <<'CMD'
python - <<'PY'
from pathlib import Path
import json, sys

p = Path("audit/qa/hde-epic023/evidence_index_snapshot.json")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

try:
    obj = json.loads(p.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERR: JSON parse failed: {e}")
    sys.exit(3)

if not isinstance(obj, dict) or not obj:
    print("ERR: evidence index snapshot JSON must be a non-empty object")
    sys.exit(3)

print("OK: evidence index snapshot present + parseable (non-empty object)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: evidence index snapshot present + parseable (non-empty object)`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`) or JSON parse/emptiness failure (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/evidence_index_snapshot.json`

---

#### DELIVERABLE D06 — Doc‑Deltas Meta (Guide D06)

**Goal:** Validate the doc‑deltas meta artifact exists at the guide-required path and is non-empty.

**PO actions:**

1. Confirm `audit/qa/hde-epic023/00_meta/doc_deltas_meta.md` exists and is non-empty.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d06_doc_deltas_meta" \
  --check-name "D06 — Doc‑Deltas Meta" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d06_doc_deltas_meta" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

p = Path("audit/qa/hde-epic023/00_meta/doc_deltas_meta.md")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

if p.stat().st_size == 0:
    print(f"ERR: empty file: {p}")
    sys.exit(3)

print("OK: doc‑deltas meta present (non-empty)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: doc‑deltas meta present (non-empty)`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`) or empty file (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/00_meta/doc_deltas_meta.md`

---

#### DELIVERABLE D07 — PF20 Update Note (Guide D07)

**Goal:** Validate the PF20 update note exists at the guide-required path and is non-empty.

**PO actions:**

1. Confirm `audit/qa/hde-epic023/00_meta/pf20_update.md` exists and is non-empty.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d07_pf20_update" \
  --check-name "D07 — PF20 Update Note" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d07_pf20_update" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

p = Path("audit/qa/hde-epic023/00_meta/pf20_update.md")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

if p.stat().st_size == 0:
    print(f"ERR: empty file: {p}")
    sys.exit(3)

print("OK: PF20 update note present (non-empty)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: PF20 update note present (non-empty)`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`) or empty file (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/00_meta/pf20_update.md`

---

#### DELIVERABLE D08 — PF23 Consult Record (Guide D08)

**Goal:** Validate the PF23 consult record exists at the guide-required path and is non-empty.

**PO actions:**

1. Confirm `audit/qa/hde-epic023/00_meta/pf23_consult.md` exists and is non-empty.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d08_pf23_consult" \
  --check-name "D08 — PF23 Consult Record" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d08_pf23_consult" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

p = Path("audit/qa/hde-epic023/00_meta/pf23_consult.md")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)

if p.stat().st_size == 0:
    print(f"ERR: empty file: {p}")
    sys.exit(3)

print("OK: PF23 consult record present (non-empty)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: PF23 consult record present (non-empty)`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`) or empty file (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `audit/qa/hde-epic023/00_meta/pf23_consult.md`

---

#### DELIVERABLE D09 — Canonical JSON Gate Evidence Pack

**Goal:** Validate the canonical JSON gate evidence pack exists at the canonical home under `audit/gates/canonical_json/` and includes the required gate json, compare log, and gate log(s).

**PO actions:**

1. Validate the evidence pack exists under `audit/gates/canonical_json/` and includes the required gate json, compare log, and gate log(s).
2. Validate decisive proof facts: gate json parses; compare/log files are non-empty and parseable where applicable.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d09_canonical_json_gate" \
  --check-name "D09 — Canonical JSON Gate Evidence Pack" \
  --surface "D09" \
  --pf-refs "PF19" \
  --intended-tokens "JSON_CANONICAL_CHECK_OK" \
  --out-dir "${EVIDENCE_ROOT}/checks/d09_canonical_json_gate" <<'CMD'
python - <<'PY'
from pathlib import Path
import json
import sys

base = Path("audit/gates/canonical_json")
if not base.is_dir():
    print(f"ERR: missing directory: {base}")
    sys.exit(2)

def _is_proof(p: Path) -> bool:
    return p.name.endswith(".path_proof.txt") or p.name.endswith(".path_proof.md")

def first_glob(globs):
    for g in globs:
        hits = sorted([p for p in base.glob(g) if p.is_file() and not _is_proof(p)])
        if hits:
            return hits[0]
    return None

gate = first_glob(["*.gate.json", "*gate*.json"])
if gate is None:
    print("ERR: missing gate json (expected *.gate.json or *gate*.json)")
    sys.exit(2)

compare_candidates = sorted(
    [p for p in base.iterdir() if p.is_file() and ("compare" in p.name) and not _is_proof(p)]
)
if not compare_candidates:
    print("ERR: missing compare log (expected filename containing 'compare')")
    sys.exit(2)
compare = compare_candidates[0]

log_candidates = sorted(
    [p for p in base.iterdir() if p.is_file() and ("log" in p.name) and (p != compare) and not _is_proof(p)]
)
if not log_candidates:
    print("ERR: missing gate log(s) (expected one or more files with 'log' in the name)")
    sys.exit(2)

try:
    json.loads(gate.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERR: gate json not parseable: {gate} :: {e}")
    sys.exit(3)

def check_file(p: Path):
    if p.stat().st_size == 0:
        print(f"ERR: empty file: {p}")
        sys.exit(3)
    if p.suffix == ".json":
        try:
            json.loads(p.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"ERR: json not parseable: {p} :: {e}")
            sys.exit(3)

check_file(compare)
for lp in log_candidates:
    check_file(lp)

print(f"OK: gate json: {gate}")
print(f"OK: compare log: {compare}")
print("OK: log(s):")
for lp in log_candidates:
    print(f" - {lp}")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout lists `OK:` lines for gate json, compare log, and at least one gate log.
**FAIL criteria:** missing required artifacts (`TOOLING_BLOCKED`) or parse/emptiness failure (`FAIL_BEHAVIOR`)—capture stdout/stderr.

---

#### DELIVERABLE D10 — Evidence Registry Surfaces (Guide D10)

**Goal:** Verify the guide-required Evidence Registry surface artifacts exist and meet basic validity checks.

**PO actions:**

1. Confirm the required registry surface artifacts exist at the specified paths.
2. Confirm JSON artifacts parse; confirm JSONL artifact contains parseable JSON objects on lines; confirm markdown artifact is non-empty.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d10_evidence_registry_surfaces" \
  --check-name "D10 — Evidence Registry Surfaces" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d10_evidence_registry_surfaces" <<'CMD'
python - <<'PY'
from pathlib import Path
import json, sys

index = Path("docs/evidence/INDEX.json")
mirror = Path("audit/index/evidence_index.jsonl")
hashes = Path("audit/index/evidence_index.hashes.json")
sentinel = Path("audit/hashes/evidence_hash_sentinel.json")
mirror_md = Path("audit/evidence_index_mirror.md")

required = [index, mirror, hashes, sentinel, mirror_md]
for p in required:
    if not p.is_file():
        print(f"ERR: missing {p}")
        sys.exit(2)
    if p.stat().st_size == 0:
        print(f"ERR: empty file: {p}")
        sys.exit(3)

# JSON parse checks
for p in [index, hashes, sentinel]:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERR: JSON parse failed: {p} :: {e}")
        sys.exit(3)

# JSONL basic parse check (sample up to 50 lines)
lines = mirror.read_text(encoding="utf-8", errors="replace").splitlines()
if not lines:
    print(f"ERR: mirror jsonl has no lines: {mirror}")
    sys.exit(3)

for i, line in enumerate(lines[:50], start=1):
    if not line.strip():
        continue
    try:
        json.loads(line)
    except Exception as e:
        print(f"ERR: mirror jsonl line {i} not parseable JSON: {e}")
        sys.exit(3)

print("OK: evidence registry surfaces present + parseable (INDEX.json, mirror jsonl, hashes, sentinel, mirror.md)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: evidence registry surfaces present + parseable ...`.
**FAIL criteria:** missing artifact (`TOOLING_BLOCKED`) or parse/emptiness failure (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `docs/evidence/INDEX.json`
* `audit/index/evidence_index.jsonl`
* `audit/index/evidence_index.hashes.json`
* `audit/hashes/evidence_hash_sentinel.json`
* `audit/evidence_index_mirror.md`

---

#### DELIVERABLE D11 — Topology Orientation Evidence

**Goal:** Validate topology orientation evidence at `audit/gates/topology/orientation_demo.txt` and confirm required proof facts (status: ok).

**PO actions:**

1. Validate the orientation demo artifact exists and includes proof fact `status: ok`.
2. Run the orientation demo validator (if provided).

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d11_topology_orientation" \
  --check-name "D11 — Topology Orientation Evidence" \
  --surface "filesystem" \
  --pf-refs "PF10, PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d11_topology_orientation" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

demo = Path("audit/gates/topology/orientation_demo.txt")
if not demo.is_file():
    print(f"ERR: missing file: {demo}")
    sys.exit(2)

txt = demo.read_text(encoding="utf-8", errors="replace")
if "status: ok" not in txt.lower():
    print("ERR: expected proof fact 'status: ok' in orientation_demo.txt")
    sys.exit(3)

print("OK: orientation_demo.txt present and contains 'status: ok'")
PY

python tools/evidence/orientation_demo.py --check
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: orientation_demo.txt present and contains 'status: ok'`.
**FAIL criteria:** missing artifact (`TOOLING_BLOCKED`) or proof-fact mismatch (`FAIL_BEHAVIOR`)—capture stdout/stderr.

---

#### DELIVERABLE D12 — Env Pins Evidence

**Goal:** Validate the env pins log exists at `audit/gates/determinism/env_pins.log`, includes the required pinned keys, and includes proof transcript(s).

**PO actions:**

1. Validate env pins log + proof transcript exist and are content-valid.
2. Confirm required pinned keys are present: SAFE_MODE, ALLOW_NETWORK, LC_ALL, LANG, TZ.

```bash
SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC \
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d12_env_pins" \
  --check-name "D12 — Env Pins Evidence" \
  --surface "filesystem" \
  --pf-refs "PF10, PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d12_env_pins" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

p = Path("audit/gates/determinism/env_pins.log")
if not p.is_file():
    print(f"ERR: missing file: {p}")
    sys.exit(2)

base = p.parent
proofs = sorted(base.glob("env_pins*.path_proof.txt"))
if not proofs:
    print("ERR: missing proof transcript(s) (expected env_pins*.path_proof.txt)")
    sys.exit(2)

text = p.read_text(encoding="utf-8", errors="replace")
required = ["SAFE_MODE=", "ALLOW_NETWORK=", "LC_ALL=", "LANG=", "TZ="]
missing = [k for k in required if k not in text]
if missing:
    print(f"ERR: missing required pins in log: {missing}")
    sys.exit(3)

proof_ok = False
for pr in proofs:
    pr_txt = pr.read_text(encoding="utf-8", errors="replace")
    if "env_pins.log" in pr_txt or str(p) in pr_txt:
        proof_ok = True
        break
if not proof_ok:
    print("ERR: proof transcript(s) present but none reference env_pins.log")
    sys.exit(3)

print("OK: env pins present and include required keys; proof transcript(s) present")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: env pins present and include required keys; proof transcript(s) present`.
**FAIL criteria:** missing artifacts (`TOOLING_BLOCKED`) or missing pins/proof-facts (`FAIL_BEHAVIOR`)—capture stdout/stderr.

---

#### DELIVERABLE D13 — Sanity Pipeline Evidence (Guide D13)

**Goal:** Validate the guide-required sanity pipeline evidence artifacts exist and are non-empty.

**PO actions:**

1. Confirm `artifacts/sanity/sanity.log` exists and is non-empty.
2. Confirm `artifacts/sanity/sanity_pipeline_evidence.md` exists and is non-empty.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d13_sanity_pipeline" \
  --check-name "D13 — Sanity Pipeline Evidence" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d13_sanity_pipeline" <<'CMD'
python - <<'PY'
from pathlib import Path
import sys

logp = Path("artifacts/sanity/sanity.log")
evp = Path("artifacts/sanity/sanity_pipeline_evidence.md")

for p in [logp, evp]:
    if not p.is_file():
        print(f"ERR: missing {p}")
        sys.exit(2)
    if p.stat().st_size == 0:
        print(f"ERR: empty file: {p}")
        sys.exit(3)

print("OK: sanity pipeline evidence artifacts present (non-empty)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: sanity pipeline evidence artifacts present (non-empty)`.
**FAIL criteria:** missing artifact (`TOOLING_BLOCKED`) or empty artifact (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `artifacts/sanity/sanity.log`
* `artifacts/sanity/sanity_pipeline_evidence.md`

---

#### DELIVERABLE D14 — Internal Version Evidence Bundle (Guide D14)

**Goal:** Validate the internal_version evidence family exists under `artifacts/ops/internal_version/` and includes required primary evidence files (txt/json) with corresponding `.path_proof.txt` transcripts.

**PO actions:**

1. Confirm `artifacts/ops/internal_version/` exists.
2. Confirm at least one primary `.txt` and at least one primary `.json` evidence file exist (excluding `*.path_proof.txt`).
3. For each primary evidence file, confirm the sibling `<filename>.path_proof.txt` exists, is non-empty, and references the primary filename.
4. Confirm `.json` files parse as JSON.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d14_internal_version" \
  --check-name "D14 — Internal Version Evidence Bundle" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d14_internal_version" <<'CMD'
python - <<'PY'
from pathlib import Path
import json, sys

base = Path("artifacts/ops/internal_version")
if not base.is_dir():
    print(f"ERR: missing directory: {base}")
    sys.exit(2)

def is_path_proof(p: Path) -> bool:
    return p.name.endswith(".path_proof.txt")

primary = sorted([p for p in base.iterdir() if p.is_file() and not is_path_proof(p)])
primary_txt = [p for p in primary if p.suffix == ".txt"]
primary_json = [p for p in primary if p.suffix == ".json"]

if not primary_txt:
    print("ERR: missing primary .txt evidence file(s) under artifacts/ops/internal_version/")
    sys.exit(2)
if not primary_json:
    print("ERR: missing primary .json evidence file(s) under artifacts/ops/internal_version/")
    sys.exit(2)

for p in primary_txt + primary_json:
    if p.stat().st_size == 0:
        print(f"ERR: empty primary evidence file: {p}")
        sys.exit(3)

    proof = Path(str(p) + ".path_proof.txt")
    if not proof.is_file():
        print(f"ERR: missing path proof transcript: {proof}")
        sys.exit(2)
    if proof.stat().st_size == 0:
        print(f"ERR: empty path proof transcript: {proof}")
        sys.exit(3)

    pt = proof.read_text(encoding="utf-8", errors="replace")
    if p.name not in pt:
        print(f"ERR: path proof does not reference primary filename ({p.name}): {proof}")
        sys.exit(3)

# JSON parse check
for p in primary_json:
    try:
        json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"ERR: JSON parse failed: {p} :: {e}")
        sys.exit(3)

print("OK: internal_version evidence present (txt/json + path proofs; json parses)")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: internal_version evidence present (txt/json + path proofs; json parses)`.
**FAIL criteria:** missing artifacts (`TOOLING_BLOCKED`) or content/proof/parse mismatch (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `artifacts/ops/internal_version/*.txt` (primary evidence files; excluding `*.path_proof.txt`)
* `artifacts/ops/internal_version/*.json` (primary evidence files; excluding `*.path_proof.txt`)
* `artifacts/ops/internal_version/*.txt.path_proof.txt` and `artifacts/ops/internal_version/*.json.path_proof.txt`

---

#### DELIVERABLE D15 — Acceptance Alignment Test Module (Guide D15)

**Goal:** Validate the guide-required acceptance alignment test module exists and is syntactically valid Python.

**PO actions:**

1. Confirm `tests/qa/test_epic023_acceptance_alignment.py` exists and is non-empty.
2. Confirm it parses as Python (syntax-valid).

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d15_acceptance_alignment_test_module" \
  --check-name "D15 — Acceptance Alignment Test Module" \
  --surface "filesystem" \
  --pf-refs "PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d15_acceptance_alignment_test_module" <<'CMD'
python - <<'PY'
from pathlib import Path
import ast, sys

p = Path("tests/qa/test_epic023_acceptance_alignment.py")
if not p.is_file():
    print(f"ERR: missing {p}")
    sys.exit(2)
if p.stat().st_size == 0:
    print(f"ERR: empty file: {p}")
    sys.exit(3)

src = p.read_text(encoding="utf-8", errors="replace")
try:
    ast.parse(src)
except Exception as e:
    print(f"ERR: python syntax parse failed: {e}")
    sys.exit(3)

print("OK: acceptance alignment test module present + parses as python")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: acceptance alignment test module present + parses as python`.
**FAIL criteria:** missing file (`TOOLING_BLOCKED`) or empty/syntax failure (`FAIL_BEHAVIOR`)—capture stdout/stderr.

**Required deliverables (validated by this step):**

* `tests/qa/test_epic023_acceptance_alignment.py`

---

#### DELIVERABLE D16 — Close Pack Evidence (Token-safe)

**Goal:** Validate the guide-required Close Pack exists at the canonical audit paths (close report + manifest) and includes sibling path proof transcripts, with required content proof facts.

**PO actions:**

1. Validate `audit/EPIC-023_close_report.md` exists, is non-empty, and has its sibling `*.path_proof.txt`.
2. Validate `audit/EPIC-023_MANIFEST.json` exists, is non-empty, parses as JSON, and has its sibling `*.path_proof.txt`.
3. Validate close report contains `QA Rails — Open/Close (Final PR)` and manifest binds to `EPIC-023_close_report.md`.

```bash
"${EVIDENCE_ROOT}/_tools/qa_check.sh" \
  --check-id "d16_close_pack" \
  --check-name "D16 — Close Pack Evidence (token-safe)" \
  --surface "filesystem" \
  --pf-refs "PF10, PF19" \
  --intended-tokens "" \
  --out-dir "${EVIDENCE_ROOT}/checks/d16_close_pack" <<'CMD'
python - <<'PY'
from pathlib import Path
import json
import sys

base = Path("audit")
report = base / "EPIC-023_close_report.md"
manifest = base / "EPIC-023_MANIFEST.json"

report_proof = base / "EPIC-023_close_report.md.path_proof.txt"
manifest_proof = base / "EPIC-023_MANIFEST.json.path_proof.txt"

for p in [report, manifest, report_proof, manifest_proof]:
    if not p.is_file():
        print(f"ERR: missing file: {p}")
        sys.exit(2)
    if p.stat().st_size == 0:
        print(f"ERR: empty file: {p}")
        sys.exit(3)

rp_txt = report_proof.read_text(encoding="utf-8", errors="replace")
mp_txt = manifest_proof.read_text(encoding="utf-8", errors="replace")
if "EPIC-023_close_report.md" not in rp_txt:
    print("ERR: close report path_proof does not reference EPIC-023_close_report.md")
    sys.exit(3)
if "EPIC-023_MANIFEST.json" not in mp_txt:
    print("ERR: manifest path_proof does not reference EPIC-023_MANIFEST.json")
    sys.exit(3)

rt = report.read_text(encoding="utf-8", errors="replace")
required_heading = "QA Rails — Open/Close (Final PR)"
if required_heading not in rt:
    print(f"ERR: close report missing required heading: {required_heading}")
    sys.exit(3)

try:
    mj = json.loads(manifest.read_text(encoding="utf-8"))
except Exception as e:
    print(f"ERR: manifest JSON not parseable: {e}")
    sys.exit(3)

mj_dump = json.dumps(mj, sort_keys=True)
if "EPIC-023_close_report.md" not in mj_dump:
    print("ERR: manifest does not appear to bind EPIC-023_close_report.md")
    sys.exit(3)

print("OK: close report + manifest + path proofs present; content + manifest binding checks passed")
PY
CMD
```

**PASS criteria:** `primary.log` status is `PASS` and stdout includes `OK: close report + manifest + path proofs present; content + manifest binding checks passed`.
**FAIL criteria:** missing artifacts (`TOOLING_BLOCKED`) or proof-fact mismatch (`FAIL_BEHAVIOR`)—capture stdout/stderr.

---

### Close-out deliverables

**Required QA evidence outputs (produced by this run):**

1. `${EVIDENCE_ROOT}/checks/**/primary.log` for each check
2. `${EVIDENCE_ROOT}/checks/**/cmd.stdout`
3. `${EVIDENCE_ROOT}/checks/**/cmd.stderr`
4. `${EVIDENCE_ROOT}/checks/**/cmd.rc`

**Reviewer rejection guardrails:**

* Any `primary.log` whose first line is not JSON is a rejection.
* Any `primary.log` JSON header missing `check_id`, `status`, `command`, or `captured_env` is a rejection.
* Any `primary.log` JSON header whose `status` is not one of `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED` is a rejection.

---

## Change Log vs Doc A (this revision only)

1. **What changed:** Implemented runnable checks for D05–D08 (removed “BLOCKED IN THIS REVISION” placeholders) using the required deliverable paths and explicit PASS/FAIL criteria.
   **Where:** Section 4 → Deliverables D05, D06, D07, D08.
   **Doc B item label:** REV-001

2. **What changed:** Replaced D10 with the guide-aligned “Evidence Registry Surfaces” validation, checking the required INDEX/mirror/hashes/sentinel/mirror.md artifacts and basic parseability.
   **Where:** Section 4 → Deliverable D10.
   **Doc B item label:** REV-002

3. **What changed:** Replaced D13 with the guide-aligned “Sanity Pipeline Evidence” validation and removed the prior `|| true` informational-only behavior so the step can FAIL when required artifacts are missing/empty.
   **Where:** Section 4 → Deliverable D13.
   **Doc B item label:** REV-003

4. **What changed:** Rewrote D14 to validate the internal_version evidence contract under `artifacts/ops/internal_version/` using primary `*.txt`/`*.json` evidence files and corresponding `.path_proof.txt` transcripts (removed the prior `INTERNAL_VERSION_PROOF.md` dependency).
   **Where:** Section 4 → Deliverable D14.
   **Doc B item label:** REV-004

5. **What changed:** Replaced D15 with a check verifying the guide-required acceptance alignment test module exists and is syntactically valid Python.
   **Where:** Section 4 → Deliverable D15.
   **Doc B item label:** REV-005

6. **What changed:** Removed execution-blocking revision dependencies by eliminating blocked/placeholder language and ensuring the deliverable set is runnable end-to-end with explicit per-deliverable evidence and PASS/FAIL semantics.
   **Where:** Section 4 → Deliverables D05–D08; Deliverables section note text.
   **Doc B item label:** REV-006

ASK OK?
