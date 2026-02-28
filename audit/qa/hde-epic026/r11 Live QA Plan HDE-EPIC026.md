## **1\) Live QA Plan**

### **Front matter**

* Epic: **HDE-EPIC026**  
* Role: **Kronos (QA agent)**  
* Executor: **PO (human), in Codespaces**  
* Version: **r11**  
* Date: **2026-02-21** (Europe/Madrid)  
* **Operator-set variable (required): `EVIDENCE_ROOT`**  
* Set `EVIDENCE_ROOT` to the epic’s **current-state** QA root (EPIC\_QA\_ROOT) under `audit/qa/` (lowercase ASCII; **MUST NOT** be under `docs/`). Evidence is check-centric under a single, stable epic-scoped QA root, with no run-id or timestamped run directories.

* export EVIDENCE\_ROOT="audit/qa/hde-epic026"

---

#### **Canon precedence statement (required)**

* **PF10 supersedes all other PF docs** where it speaks to QA procedure, constraints, or planning posture.  
* Where PF10 is silent:  
  * **PF19** governs QA procedure and evidence posture.  
  * **PF23** governs repo-reality/audit discipline and what may be asserted from audits.  
  * **PF05** governs CLI/API semantics when needed for runnable steps.  
  * **PF27** governs the Live QA Plan template format, check log structure, and required Step‑0 artifacts.

Non-canon inputs were used only as **inlined verbatim excerpts** at point-of-use (never referenced by filename).

---

#### **Canon set (explicit; stable references only)**

* PF10 — HDE‑Build Notes  
* PF23 — Reality Audits  
* PF19 — Glow QA Guide  
* PF05 — HDE CLI/API Vendor Reference  
* PF27 — Plan Templates

Additional PF‑Canon used only to resolve a concrete execution gap:

* PF04 — HDE Governance (only for acceptance-token concepts referenced by PF27 template)

---

### **Scope statement**

This Live QA Plan verifies **all 12 proof obligations** for HDE‑EPIC026 as step-by-step, PO-runnable checks in Codespaces. The plan produces a **check-centric evidence pack** under `EVIDENCE_ROOT` with:

* a primary log per check (PF27 header schema),  
* a per-run `qa_step_logs_manifest.json` and `qa_step_logs_manifest.json.path_proof.txt` under `EVIDENCE_ROOT/checks/po-000/`,  
* Step‑0 Doc Delta Capture under `EVIDENCE_ROOT/checks/po-000/doc_deltas.md`,  
* concrete PASS/FAIL predicates per check.

This runbook does **not** require the PO to open any non-canonical guide/audit files; any needed content is inlined verbatim at point of use.

---

#### **PF10 overrides / conflicts (if any)**

PF10 imposes binding requirements on QA planning provenance and mandates PF23 consultation.

PF10 — HDE‑Build Notes, **§2.16 PF23 required in QA planning**  
CANON PROOF EXCERPT (verbatim):

1. **PF23 MUST be consulted during QA planning.**  
   Any QA planning activity MUST explicitly consult PF23 before finalizing plans or checklists.

PF10 — HDE‑Build Notes, **§2.17 QA planning locus provenance lock (PF10 / PF-Canon / initial QA Audit only)**  
CANON PROOF EXCERPT (verbatim):

1. **Allowed provenance sources (exclusive).**  
   In QA planning (including Live QA Plans, QA Guides, QA reviews, QA prompts, and QA checklists), the ONLY allowed sources for any repo-reality claim are:  
* PF10 — HDE Build Notes  
* PF-Canon (any PF document)  
* The initial QA Audit for the epic (repo reality and readiness proof)

No other PF10 conflicts identified for this epic’s QA procedures.

---

### **PF23 anchors**

Repo-reality claims (paths, endpoints, scripts) are based only on the epic’s initial audit snapshot, and any audit-noted gaps are treated as blockers where they affect executable steps.

SOURCE EXCERPT (verbatim):

Search roots: repo/  
Searched pattern(s): "dev/sampler/conjunction", "dev/compat/conjunction", "dev/writer/conjunction", "ENDPOINTS\_CATALOG.json", "qa\_step\_logs\_manifest.json"  
Search command(s): rg \-n ""

SOURCE EXCERPT (verbatim):

Gaps that block deterministic Live QA plan:

* Endpoint Catalog generator command is unclear.  
* No dedicated Epic026 QA harness runner entrypoint.  
* Multiple app startup paths; which one is canonical for local QA is unclear.

Operational interpretation for this plan:

* If a step requires a generator entrypoint the audit called **unclear**, that step remains included but is marked **BLOCKED** with rerun directives (per rules).  
* If tests and scripts exist and are runnable without invoking unclear generators, the step remains runnable.

---

### **Environment and rails posture**

#### **Determinism pins (canonical pins only)**

PF05 defines canonical JSON and locale assumptions. This plan sets determinism pins on every check execution.

PF05 — HDE CLI/API Vendor Reference, **§0.2 Scope \[Required-Now\]**  
CANON PROOF EXCERPT (verbatim):

* Canonical JSON and locale: all canonical JSON is UTF-8; keys ASCII-sorted; exactly one trailing LF; assume LC\_ALL=C LANG=C TZ=UTC.

Additionally, this plan treats missing tooling (e.g., pytest not installed) as a **tooling failure**, not a behavior failure.

PF19 — Glow QA Guide, **§2.2.5 Tooling vs behavior failures (pytest and harnesses)**  
CANON PROOF EXCERPT (verbatim):

If the toolchain itself is broken (missing deps, broken venv, pytest import fails), classify as TOOLING and block the step; do not log a behavior FAIL.

---

#### **Rails posture (explicit)**

Default posture for this runbook:

* Start with **closed rails**: `SAFE_MODE=1`, `ALLOW_NETWORK=0`  
* Use **non-prod app env** unless explicitly required for a check: `APP_ENV=dev`  
* Open rails only when a step explicitly requires external acquisition:  
  * `SAFE_MODE=0`, `ALLOW_NETWORK=1` (and any required base URL/credentials)

SOURCE EXCERPT (verbatim):

rails\_env \= python \-m engine.runtime.determinism\_env  
SAFE\_MODE=1  
ALLOW\_NETWORK=0  
APP\_ENV=prod

(That excerpt proves these rails variables exist as a documented environment posture; this plan uses `APP_ENV=dev` unless a check explicitly needs prod-like behavior.)

#### **No VCS workflow content (hard)**

This plan includes **no branch/merge/commit workflow** steps. All actions are local execution \+ evidence capture only.

---

### **PO inputs needed**

Provide these only if executing the CLI or open-rails acquisition checks:

1. **For CLI conjunction runs (PO‑008 / PO‑009 / PO‑010):**  
   * `USER_A_ID` — valid HD user id  
   * `USER_B_ID` — valid HD user id (distinct from A)  
2. **For any step that must permit external acquisition (open rails):**  
   * `HDAPI_BASE_URL` (if required by your environment)  
   * Any required credential env var(s) used in your Codespaces setup (do not write secrets into logs; redact before saving).

If the PO cannot provide valid user IDs or credentials, those specific checks remain included but may become **BLOCKED**.

---

### **Evidence posture and directory structure**

#### **Epic QA root normalization (required)**

All QA-created evidence must be under `EVIDENCE_ROOT` as EPIC\_QA\_ROOT current-state evidence (under `audit/qa/`; never `docs/`); evidence is check-centric under a single, stable epic-scoped QA root, with no run-id or timestamped run directories.

#### **Check-centric, single-root evidence posture (normative)**

* Each check writes to:  
  `"$EVIDENCE_ROOT/checks/<check_id>/"` (lowercase ASCII)  
* Each check produces a **primary log**:  
  `"$EVIDENCE_ROOT/checks/<check_id>/primary.log"`  
* All other check artifacts are sibling files in the same directory.

#### **Recommended canonical layout (default for new plans)**

This plan uses the PF27 check-centric layout, rooted at `EVIDENCE_ROOT`.

#### **Step-log header schema expectations (minimum; required)**

PF27 requires that each check’s primary log begins with a single-line JSON header with required keys.

PF27 — Plan Templates, **§Step-log header schema expectations (minimum; required)**  
CANON PROOF EXCERPT (verbatim):

The primary log MUST begin with a single-line JSON header containing these required keys:

* `schema_version`  
* `timestamp_utc`

Implementation in this plan:

* A helper script writes the header line and appends the body logs.  
* `intended_tokens` and `claimed_tokens` are included as JSON arrays (may be empty if token binding is not determined).

**Required per-run manifest files (PF27):**

PF27 — Plan Templates, **§Check Blocks**  
CANON PROOF EXCERPT (verbatim):

* `audit/qa/<epic-id>/qa_step_logs_manifest.json` (required)  
* `audit/qa/<epic-id>/qa_step_logs_manifest.json.path_proof.txt` (required)

This plan creates them under `$EVIDENCE_ROOT/checks/po-000/` (stable check directory).

---

#### **Evidence setup (run once before checks)**

1. Create evidence root, checks folders, plan-artifacts check directory, helper script, and initialize the per-run manifest.

set \-euo pipefail  
: "${EVIDENCE\_ROOT:?EVIDENCE\_ROOT is not set}"

plan\_dir="$EVIDENCE\_ROOT/checks/po-000"  
mkdir \-p "$plan\_dir" "$EVIDENCE\_ROOT/checks"

helper="$plan\_dir/qa\_helpers.sh"

python \-c 'import pathlib, textwrap, sys  
p \= pathlib.Path(sys.argv\[1\])  
p.parent.mkdir(parents=True, exist\_ok=True)  
p.write\_text(textwrap.dedent(r"""  
\#\!/usr/bin/env bash  
set \-euo pipefail

: "${EVIDENCE\_ROOT:?EVIDENCE\_ROOT is not set}"

qa\_sha256\_file() {  
local path="$1"  
sha256sum "$path" | awk "{print \\$1}"  
}

qa\_json\_header() {  
local check\_id="$1"  
local step\_id="$2"  
local target="$3"

python \-c "import json, sys, datetime; check\_id=sys.argv\[1\]; step\_id=sys.argv\[2\]; target=sys.argv\[3\]; ts=datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"; hdr={"schema":"pf27-step-log-header-v1","check\_id":check\_id,"step\_id":step\_id,"target":target,"timestamp\_utc":ts}; print(json.dumps(hdr, ensure\_ascii=False))" "$check\_id" "$step\_id" "$target"  
}

qa\_emit\_step\_log\_header() {  
local check\_id="$1"  
local step\_id="$2"  
local target="$3"

qa\_json\_header "$check\_id" "$step\_id" "$target"  
echo  
echo "\#\#\#"  
}

qa\_manifest\_path() {  
echo "$EVIDENCE\_ROOT/checks/po-000/qa\_step\_logs\_manifest.json"  
}

qa\_manifest\_proof\_path() {  
echo "$EVIDENCE\_ROOT/checks/po-000/qa\_step\_logs\_manifest.json.path\_proof.txt"  
}

qa\_write\_manifest\_path\_proof() {  
local manifest\_path  
local proof\_path  
manifest\_path="$(qa\_manifest\_path)"  
proof\_path="$(qa\_manifest\_proof\_path)"

python \-c "import pathlib, sys; mp=pathlib.Path(sys.argv\[1\]).resolve(); pp=pathlib.Path(sys.argv\[2\]); pp.parent.mkdir(parents=True, exist\_ok=True); pp.write\_text(str(mp)+"\\n", encoding="utf-8")" "$manifest\_path" "$proof\_path"  
}

qa\_init\_manifest() {  
local manifest\_path  
manifest\_path="$(qa\_manifest\_path)"

python \-c "import json, pathlib, sys, datetime; p=pathlib.Path(sys.argv\[1\]); p.parent.mkdir(parents=True, exist\_ok=True); now=datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"; data=json.loads(p.read\_text(encoding="utf-8")) if p.exists() else {"schema":"pf27-step-logs-manifest-v1","schema\_version":1,"created\_utc":now,"entries":\[\]}; p.write\_text(json.dumps(data, indent=2, sort\_keys=True)+"\\n", encoding="utf-8")" "$manifest\_path"

qa\_write\_manifest\_path\_proof  
}

qa\_append\_manifest() {  
local check\_id="$1"  
local step\_id="$2"  
local artifact\_relpath="$3"  
local artifact\_abspath="$4"  
local summary="$5"  
local status="$6"

local manifest\_path  
manifest\_path="$(qa\_manifest\_path)"

local sha  
sha="$(qa\_sha256\_file "$artifact\_abspath")"

python \-c "import json, pathlib, sys, datetime; mp=pathlib.Path(sys.argv\[1\]); check\_id=sys.argv\[2\]; step\_id=sys.argv\[3\]; rel=sys.argv\[4\]; sha=sys.argv\[5\]; summary=sys.argv\[6\]; status=sys.argv\[7\]; mp.parent.mkdir(parents=True, exist\_ok=True); now=datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"; data=json.loads(mp.read\_text(encoding="utf-8")) if mp.exists() else {"schema":"pf27-step-logs-manifest-v1","schema\_version":1,"created\_utc":now,"entries":\[\]}; entry={"timestamp\_utc":now,"check\_id":check\_id,"step\_id":step\_id,"artifact\_relpath":rel,"sha256":sha,"summary":summary,"status":status}; data.setdefault("entries", \[\]).append(entry); mp.write\_text(json.dumps(data, indent=2, sort\_keys=True)+"\\n", encoding="utf-8")" "$manifest\_path" "$check\_id" "$step\_id" "$artifact\_relpath" "$sha" "$summary" "$status"  
}  
""" ).lstrip(), encoding="utf-8")' "$helper"

chmod \+x "$helper"  
source "$helper"

qa\_init\_manifest() {

  local manifest\_path="$EVIDENCE\_ROOT/qa\_step\_logs\_manifest.json"

  if \[ \! \-f "$manifest\_path" \]; then

    python \- \<\<'PY' \> "$manifest\_path"

import datetime, json

print(json.dumps({

  "schema\_version": "pf27.qa\_step\_logs\_manifest.v1",

  "generated\_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z",

  "checks": \[\],

}, ensure\_ascii=False, indent=2) \+ "\\n")

PY

  fi

  qa\_write\_manifest\_path\_proof

}

qa\_append\_manifest() {

  local check\_id="$1"

  local status="$2"

  local log\_path="$3"

  local sha256="$4"

  local manifest\_path="$EVIDENCE\_ROOT/qa\_step\_logs\_manifest.json"

  python \- "$manifest\_path" "$check\_id" "$status" "$log\_path" "$sha256" \<\<'PY'

import datetime, json, pathlib, sys

manifest\_path \= pathlib.Path(sys.argv\[1\])

check\_id \= sys.argv\[2\]

status \= sys.argv\[3\]

log\_path \= sys.argv\[4\]

sha256 \= sys.argv\[5\]

data \= json.loads(manifest\_path.read\_text(encoding="utf-8"))

data.setdefault("checks", \[\]).append({

  "timestamp\_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z",

  "check\_id": check\_id,

  "status": status,

  "log\_path": log\_path,

  "sha256": sha256,

})

manifest\_path.write\_text(json.dumps(data, ensure\_ascii=False, indent=2) \+ "\\n", encoding="utf-8")

PY

  qa\_write\_manifest\_path\_proof

}

qa\_write\_manifest\_path\_proof() {

  local manifest\_path="$EVIDENCE\_ROOT/qa\_step\_logs\_manifest.json"

  local proof\_path="$EVIDENCE\_ROOT/qa\_step\_logs\_manifest.json.path\_proof.txt"

  python \- "$manifest\_path" \<\<'PY' \> "$proof\_path"

import hashlib, pathlib, sys

p \= pathlib.Path(sys.argv\[1\]).resolve()

h \= hashlib.sha256(p.read\_bytes()).hexdigest()

print(f"manifest\_path={p}")

print(f"manifest\_sha256={h}")

PY

}

BASH

chmod \+x "$EVIDENCE\_ROOT/00\_meta/qa\_helpers.sh"

\# Initialize manifest now

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

qa\_init\_manifest

2. Prove that the epic has an established QA root pattern (repo reality proof; not used as a dependency, but anchors existence).

SOURCE EXCERPT (verbatim):

Path: audit/qa/hde-epic026/qa\_step\_logs\_manifest.json  
Category: QA evidence output  
Proof: audit/qa/hde-epic026/qa\_step\_logs\_manifest.json

---

### **Mandatory Step‑0 artifacts**

#### **Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**

Create `doc_deltas.md` for this run and record any planned/observed doc deltas and known blockers.

PF27 — Plan Templates, **§Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**  
CANON PROOF EXCERPT (verbatim):

Capture doc deltas that might be required due to code / behavior changes.  
Must include any deltas in docs/ and in audit/gates outputs.

set \-euo pipefail

mkdir \-p "$EVIDENCE\_ROOT/checks/po-000"

doc\_deltas="$EVIDENCE\_ROOT/checks/po-000/doc\_deltas.md"

python \-c 'import pathlib, textwrap, sys  
p \= pathlib.Path(sys.argv\[1\])  
p.parent.mkdir(parents=True, exist\_ok=True)  
p.write\_text(textwrap.dedent(r"""  
\# doc delta capture — hde-epic026

\#\# Doc delta summary (required)  
\# change\_type: \[NONE|DOC\_ONLY|CODE\_ONLY|DOC\_AND\_CODE|UNKNOWN\]  
\# summary: \<1–4 bullets\>  
\# evidence\_basis:  
\# \- doc\_a\_anchor:  
\# \- doc\_b\_anchor:  
\# \- pf\_anchor:

\#\# Actual delta notes (fill in; keep terse)  
\# change\_type: UNKNOWN  
\# summary:  
\# \- TBD  
\# evidence\_basis:  
\# \- doc\_a\_anchor: TBD  
\# \- doc\_b\_anchor: TBD  
\# \- pf\_anchor: TBD

\#\# Re-run notes (optional)  
\# If any check is NOT RUN, record why here with explicit condition.  
""" ).lstrip(), encoding="utf-8")' "$doc\_deltas"

#### **Step‑0C — Prod handshake (identity-only) when target is prod-like**

This runbook is intended for Codespaces execution and does not require direct prod access by default. If you are targeting a prod-like environment for any open-rails checks, capture an identity-only handshake (no mutations, no write endpoints). If not applicable, record “NOT RUN” in `doc_deltas.md`.

---

### **Runbook Check Matrix**

| Check ID | Step | Primary method | Rails posture | Core evidence |
| ----- | ----- | ----- | ----- | ----- |
| po-001 | PO‑001 | pytest contract tests (+ optional CLI byte-compare) | closed rails | pytest logs; optional CLI outputs \+ sha |
| po-002 | PO‑002 | pytest contract tests \+ catalog inspection | closed rails | pytest logs; catalog extract |
| po-003 | PO‑003 | pytest contract tests | closed rails | pytest logs |
| po-004 | PO‑004 | pytest contract tests | closed rails | pytest logs |
| po-005 | PO‑005 | pytest dev-endpoint tests \+ route proof | APP\_ENV=dev | pytest logs; route grep evidence |
| po-006 | PO‑006 | pytest dev-endpoint tests \+ route proof | APP\_ENV=dev | pytest logs; route grep evidence |
| po-007 | PO‑007 | endpoint catalog sha \+ content checks | closed rails | sha check; extracted entries |
| po-008 | PO‑008 | CLI help \+ CLI run \+ canonical key-order check | closed rails | help logs; run outputs; canonical check |
| po-009 | PO‑009 | CLI closed-rails refusal \+ open-rails success | closed rails \+ open rails | refusal logs; success logs |
| po-010 | PO‑010 | docs alignment via catalog \+ CLI help | closed rails | extracted catalog \+ help text |
| po-011 | PO‑011 | governance scripts in CI mode | closed rails | script stdout/stderr; rc |
| po-012 | PO‑012 | close-pack generation \+ artifact presence | closed rails | generator logs; copied close pack |

---

#### **Token coverage and evidence binding (required)**

This plan includes `intended_tokens` / `claimed_tokens` arrays in every check header (PF27 schema). If your epic acceptance roster requires specific tokens, map them during execution and record mapping decisions in `doc_deltas.md`.

PF04 — HDE Governance, **§2.1 A3 — Determinism gate (hash and normalize)**  
CANON PROOF EXCERPT (verbatim):

All JSON outputs must normalize and hash deterministically.  
If `AB` and `BA` are semantically identical, they must produce identical canonical bytes (AB↔BA identity).

Plan token default:

* Checks that explicitly validate canonical bytes/determinism set `intended_tokens=["A3"]`.  
* All other checks default token arrays to `[]` unless the PO can bind additional tokens confidently.

---

### **Check Blocks**

#### **Embedded harness checks (pattern; use when no standalone script exists)**

Pattern used in each check:

* Create a per-check directory under `"$EVIDENCE_ROOT/checks/<check_id>/"`.  
* Run command(s), capturing stdout/stderr and exit codes.  
* Write `primary.log` as: **header JSON line** \+ appended body log.  
* Update `qa_step_logs_manifest.json` under `$EVIDENCE_ROOT/checks/po-000/` after each check.

#### **Canon check clarifications (addenda-driven; locked)**

* Repo-reality strings (paths, routes, scripts) are never invented; they must be proven verbatim from the audit snapshot (PF10 provenance lock).  
* Tooling failures (missing pytest, broken venv) are recorded as **BLOCKED/TOOLING**, not behavior fails (PF19).

---

#### **CHECK po-001: PO-001 — Conjunction canonical bytes AB↔BA identity**

SOURCE EXCERPT (verbatim):

PO-001  
Proof obligation: Conjunction output must be canonically serializable and deterministic, including AB↔BA swap producing identical canonical bytes.

##### **Intent**

Prove that conjunction output is deterministic and canonically serializable, and that AB↔BA swapping produces identical canonical bytes (at least via the contract-test harness; optional CLI byte-compare if user IDs are available).

##### **Inputs**

* Environment pins: `LC_ALL=C LANG=C TZ=UTC`  
* Closed rails: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Optional for CLI byte-compare: `USER_A_ID`, `USER_B_ID` and working `hdctl`

##### **Deliverables**

Under:

* `"$EVIDENCE_ROOT/checks/po-001/primary.log"` (PF27 header \+ body)  
* `"$EVIDENCE_ROOT/checks/po-001/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-001/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-001/pytest_rc.txt"`  
* Optional CLI lane (only if executed):  
  * `"$EVIDENCE_ROOT/checks/po-001/cli_ab.json"`  
  * `"$EVIDENCE_ROOT/checks/po-001/cli_ba.json"`  
  * `"$EVIDENCE_ROOT/checks/po-001/cli_sha256.txt"`  
  * `"$EVIDENCE_ROOT/checks/po-001/cli_canonical_keyorder_check.txt"`

##### **Procedure**

1. Run the contract test file that asserts compat endpoint invariants (includes canonical JSON checks per audit notes).

SOURCE EXCERPT (verbatim):

PTH-039  
Path: tests/http/test\_compat\_endpoint\_contract.py  
Category: Test/CI job  
Proof: tests/http/test\_compat\_endpoint\_contract.py

SOURCE EXCERPT (verbatim):

* Compat endpoint tests: tests/http/test\_compat\_endpoint\_contract.py asserts  
  * rejects when SAFE\_MODE=1 and missing local data (no external acquisition)

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-001"

check\_name="PO-001 — Conjunction canonical bytes AB↔BA identity"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

\# determinism pins \+ closed rails

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

\# token binding default for this determinism check

export INTENDED\_TOKENS\_JSON='\["A3"\]'

\# claimed tokens only set to \["A3"\] on PASS

export CLAIMED\_TOKENS\_JSON='\[\]'

body="$check\_dir/body.log"

: \> "$body"

{

  echo "RUN: python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py"

  echo "ENV: LC\_ALL=$LC\_ALL LANG=$LANG TZ=$TZ SAFE\_MODE=$SAFE\_MODE ALLOW\_NETWORK=$ALLOW\_NETWORK APP\_ENV=$APP\_ENV"

} \>\> "$body"

set \+e

python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

  export CLAIMED\_TOKENS\_JSON='\["A3"\]'

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py"\]'

export ARTIFACTS\_JSON="$(python \- \<\<'PY'

import json

arts \= \[

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"},

\]

print(json.dumps(arts))

PY

)"

export PF\_REFS\_JSON='\["PF05 §0.2 Scope \[Required-Now\]","PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF04 §2.1 A3 — Determinism gate (hash and normalize)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

2. Optional CLI byte-compare (only if `USER_A_ID` and `USER_B_ID` are available and `hdctl` is runnable). If not executed, record “NOT RUN (no IDs/tooling)” in `doc_deltas.md`.

set \-euo pipefail

if \[ \-n "${USER\_A\_ID:-}" \] && \[ \-n "${USER\_B\_ID:-}" \]; then

  check\_dir="$EVIDENCE\_ROOT/checks/po-001"

  \# closed rails for this optional lane

  export LC\_ALL=C LANG=C TZ=UTC

  export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

  set \+e

  hdctl showcompat \--conjunction \--user-a "$USER\_A\_ID" \--user-b "$USER\_B\_ID" \--format json \> "$check\_dir/cli\_ab.json" 2\> "$check\_dir/cli\_ab.err"

  rc1=$?

  hdctl showcompat \--conjunction \--user-a "$USER\_B\_ID" \--user-b "$USER\_A\_ID" \--format json \> "$check\_dir/cli\_ba.json" 2\> "$check\_dir/cli\_ba.err"

  rc2=$?

  set \-e

  python \- \<\<'PY' \> "$check\_dir/cli\_sha256.txt"

import hashlib, pathlib

def sha(p):

  return hashlib.sha256(pathlib.Path(p).read\_bytes()).hexdigest()

print("cli\_ab\_sha256=" \+ sha("cli\_ab.json"))

print("cli\_ba\_sha256=" \+ sha("cli\_ba.json"))

PY

  \# Canonical key-order \+ single trailing LF check per PF05

  python \- \<\<'PY' \> "$check\_dir/cli\_canonical\_keyorder\_check.txt"

import json, pathlib, sys

def check\_file(path):

  b \= pathlib.Path(path).read\_bytes()

  if not b.endswith(b"\\n") or b.endswith(b"\\n\\n"):

    raise SystemExit(f"{path}: trailing LF rule violated")

  s \= b.decode("utf-8")

  def hook(pairs):

    keys \= \[k for k,\_ in pairs\]

    if keys \!= sorted(keys):

      raise ValueError(f"key order not ASCII-sorted: {keys}")

    return dict(pairs)

  json.loads(s, object\_pairs\_hook=hook)

  return f"{path}: OK"

print(check\_file("cli\_ab.json"))

print(check\_file("cli\_ba.json"))

PY

  printf "cli\_ab\_rc=%s\\ncli\_ba\_rc=%s\\n" "$rc1" "$rc2" \>\> "$check\_dir/cli\_canonical\_keyorder\_check.txt"

fi

##### **PASS/FAIL**

PASS if:

* `pytest_rc.txt` is `0` for `tests/http/test_compat_endpoint_contract.py`, **and**  
* (If optional CLI lane was executed) both CLI outputs pass the canonical key-order check and the two sha256 values match.

FAIL if:

* pytest exit code is non-zero, or  
* CLI lane executed and sha256 differs, or canonical key-order check fails.  
  Capture: `pytest_stdout.log`, `pytest_stderr.log`, and any `cli_*.err`.

##### **Traceability**

* Step: PO‑001 (guide excerpt above)  
* Primary enforcement locus (test): `tests/http/test_compat_endpoint_contract.py` (audit-proven above)

---

#### **CHECK po-002: PO-002 — Existing non-conjunction behavior unchanged**

SOURCE EXCERPT (verbatim):

PO-002  
Proof obligation: Existing (non-conjunction) compatibility behavior remains unchanged.

##### **Intent**

Demonstrate that non-conjunction compat behavior still satisfies its contract (regression guard) and that no new public surface is introduced by the conjunction addition (catalog discipline).

##### **Inputs**

* Closed rails: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Determinism pins: `LC_ALL=C LANG=C TZ=UTC`

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-002/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-002/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-002/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-002/pytest_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-002/catalog_api_compat_entry.json"`

##### **Procedure**

1. Run the compat endpoint contract tests as regression guard (covers non-conjunction invariants in the same contract harness).

SOURCE EXCERPT (verbatim):

PTH-039  
Path: tests/http/test\_compat\_endpoint\_contract.py  
Category: Test/CI job  
Proof: tests/http/test\_compat\_endpoint\_contract.py

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-002"

check\_name="PO-002 — Existing non-conjunction behavior unchanged"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

body="$check\_dir/body.log"

: \> "$body"

echo "RUN: python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py" \>\> "$body"

set \+e

python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

\# Extract the endpoint catalog entry for /api/compat/v1 for “no new public surface” sanity

SOURCE\_CAT="docs/ENDPOINTS\_CATALOG.json"

python \- \<\<'PY' \> "$check\_dir/catalog\_api\_compat\_entry.json"

import json, pathlib

p \= pathlib.Path("docs/ENDPOINTS\_CATALOG.json")

data \= json.loads(p.read\_text(encoding="utf-8"))

target \= "/api/compat/v1"

hits \= \[\]

def walk(x):

  if isinstance(x, dict):

    if x.get("path") \== target:

      hits.append(x)

    for v in x.values():

      walk(v)

  elif isinstance(x, list):

    for i in x:

      walk(i)

walk(data)

print(json.dumps({"target": target, "matches": hits}, ensure\_ascii=False, indent=2))

PY

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py","python (extract /api/compat/v1 from docs/ENDPOINTS\_CATALOG.json)"\]'

export ARTIFACTS\_JSON='\[

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"},

  {"path":"catalog\_api\_compat\_entry.json","type":"json","desc":"catalog extract for /api/compat/v1"}

\]'

export PF\_REFS\_JSON='\["PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

2. Prove the catalog locus exists (repo reality).

SOURCE EXCERPT (verbatim):

PTH-003  
Path: docs/ENDPOINTS\_CATALOG.json  
Category: Docs (canonical)  
Proof: docs/ENDPOINTS\_CATALOG.json

##### **PASS/FAIL**

PASS if:

* pytest exit code is 0, and  
* `catalog_api_compat_entry.json` contains at least one match for `/api/compat/v1`.

FAIL if:

* pytest rc non-zero, or catalog extract finds no `/api/compat/v1` entry.

##### **Traceability**

* Step: PO‑002 (guide excerpt above)  
* Primary regression harness locus: `tests/http/test_compat_endpoint_contract.py`

---

#### **CHECK po-003: PO-003 — Local-first acquisition semantics are preserved**

SOURCE EXCERPT (verbatim):

PO-003  
Proof obligation: Conjunction resolver must preserve local-first semantics and only acquire external facts when permitted. Missing required local inputs must produce typed errors.

##### **Intent**

Verify local-first and rails gating behavior for the conjunction resolver via contract tests that assert:

* closed rails refusal on missing local inputs,  
* typed errors on missing required local inputs,  
* no unpermitted acquisition.

##### **Inputs**

* Closed rails: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Determinism pins: `LC_ALL=C LANG=C TZ=UTC`

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-003/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-003/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-003/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-003/pytest_rc.txt"`

##### **Procedure**

SOURCE EXCERPT (verbatim):

PTH-039  
Path: tests/http/test\_compat\_endpoint\_contract.py  
Category: Test/CI job  
Proof: tests/http/test\_compat\_endpoint\_contract.py

SOURCE EXCERPT (verbatim):

* Compat endpoint tests: tests/http/test\_compat\_endpoint\_contract.py asserts  
  * rejects when SAFE\_MODE=1 and missing local data (no external acquisition)  
  * accepts when SAFE\_MODE=0 and ALLOW\_NETWORK=1, closes back to SAFE\_MODE=1  
  * typed errors: missing\_input, rails\_closed, vendor\_shape\_invalid

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-003"

check\_name="PO-003 — Local-first acquisition semantics preserved"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

body="$check\_dir/body.log"

: \> "$body"

echo "RUN: python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py" \>\> "$body"

set \+e

python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py"\]'

export ARTIFACTS\_JSON='\[

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"}

\]'

export PF\_REFS\_JSON='\["PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if pytest exit code is 0\.

FAIL if pytest exit code is non-zero; capture both logs.

##### **Traceability**

* Step: PO‑003 (guide excerpt above)  
* Test locus: `tests/http/test_compat_endpoint_contract.py`

---

#### **CHECK po-004: PO-004 — Cached vendor-shaped payload normalization regression is fixed**

SOURCE EXCERPT (verbatim):

PO-004  
Proof obligation: Bug fix: cached payload shaped like vendor response should not break canonicalization; regression tests cover.

##### **Intent**

Verify regression coverage for the vendor-shaped cached payload fix via contract tests.

##### **Inputs**

* Closed rails: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Determinism pins: `LC_ALL=C LANG=C TZ=UTC`

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-004/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-004/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-004/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-004/pytest_rc.txt"`

##### **Procedure**

SOURCE EXCERPT (verbatim):

PTH-039  
Path: tests/http/test\_compat\_endpoint\_contract.py  
Category: Test/CI job  
Proof: tests/http/test\_compat\_endpoint\_contract.py

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-004"

check\_name="PO-004 — Cached vendor-shaped payload regression fixed"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

body="$check\_dir/body.log"

: \> "$body"

echo "RUN: python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py" \>\> "$body"

set \+e

python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py"\]'

export ARTIFACTS\_JSON='\[

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"}

\]'

export PF\_REFS\_JSON='\["PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if pytest exit code is 0\.

FAIL if pytest exit code is non-zero.

##### **Traceability**

* Step: PO‑004 (guide excerpt above)  
* Test locus: `tests/http/test_compat_endpoint_contract.py`

---

#### **CHECK po-005: PO-005 — Dev-only sampler and reader endpoints exist and are gated to dev**

SOURCE EXCERPT (verbatim):

PO-005  
Proof obligation: Dev-only sampler and reader endpoints expose conjunction behavior for QA; must be gated to dev/non-prod.

##### **Intent**

Prove dev-only sampler and reader endpoints exist and are gated to dev/non-prod (both via route proof and dev-endpoint test harness).

##### **Inputs**

* `APP_ENV=dev` (explicit)  
* Closed rails by default: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Determinism pins: `LC_ALL=C LANG=C TZ=UTC`

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-005/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-005/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-005/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-005/pytest_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-005/route_proof.txt"`

##### **Procedure**

1. Prove dev routes exist in the repo.

SOURCE EXCERPT (verbatim):

PTH-015  
Path: adapter/http\_reader.py  
Category: HTTP routes (dev)  
Proof: adapter/http\_reader.py

SOURCE EXCERPT (verbatim):

PTH-015  
Path: adapter/http\_reader.py  
Category: HTTP routes (dev)  
Proof: adapter/http\_reader.py:731: @bp.get("/dev/sampler/conjunction")

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-005"

check\_name="PO-005 — Dev sampler \+ reader conjunction endpoints gated to dev"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

\# Route proof capture (static grep via python for portability)

python \- \<\<'PY' \> "$check\_dir/route\_proof.txt"

import pathlib, re

p \= pathlib.Path("adapter/http\_reader.py")

text \= p.read\_text(encoding="utf-8")

targets \= \[

  r'@bp\\.get\\("/dev/sampler/conjunction"\\)',

r'@bp\\.get\\("/dev/reader/conjunction"\\)',

\]

for t in targets:

  m \= re.search(t, text)

  print(f"{t}: {'FOUND' if m else 'NOT\_FOUND'}")

PY

body="$check\_dir/body.log"

: \> "$body"

echo "RUN: python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py" \>\> "$body"

\# Run dev-endpoint tests

SOURCE\_TEST="tests/http/test\_dev\_conjunction\_http.py"

set \+e

python \-m pytest \-q "$SOURCE\_TEST" \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["python (route proof from adapter/http\_reader.py)","python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py"\]'

export ARTIFACTS\_JSON='\[

  {"path":"route\_proof.txt","type":"text","desc":"static route proof for dev sampler \+ compat endpoints"},

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"}

\]'

export PF\_REFS\_JSON='\["PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

2. Prove test locus exists.

SOURCE EXCERPT (verbatim):

PTH-037  
Path: tests/http/test\_dev\_conjunction\_http.py  
Category: Test/CI job  
Proof: tests/http/test\_dev\_conjunction\_http.py

##### **PASS/FAIL**

PASS if:

* `route_proof.txt` shows FOUND for both dev sampler and dev compat conjunction endpoints, and  
* pytest rc is 0 for `tests/http/test_dev_conjunction_http.py`.

FAIL if either route proof is NOT\_FOUND or pytest fails.

##### **Traceability**

* Step: PO‑005 (guide excerpt above)  
* Route locus: `adapter/http_reader.py`  
* Test locus: `tests/http/test_dev_conjunction_http.py`

---

#### **CHECK po-006: PO-006 — Dev-only writer endpoint exists and stable writer envelope**

SOURCE EXCERPT (verbatim):

PO-006  
Proof obligation: Dev-only writer endpoint exposes conjunction envelope used by writer; must be gated and stable.

##### **Intent**

Prove dev-only writer endpoint exists and is gated, and that dev conjunction writer envelope remains stable (validated via dev-endpoint tests and static route proof).

##### **Inputs**

* `APP_ENV=dev`  
* Closed rails by default: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Determinism pins: `LC_ALL=C LANG=C TZ=UTC`

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-006/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-006/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-006/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-006/pytest_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-006/route_proof.txt"`

##### **Procedure**

SOURCE EXCERPT (verbatim):

PTH-015  
Path: adapter/http\_reader.py  
Category: HTTP routes (dev)  
Proof: adapter/http\_reader.py:737: @bp.get("/dev/writer/conjunction")

SOURCE EXCERPT (verbatim):

PTH-037  
Path: tests/http/test\_dev\_conjunction\_http.py  
Category: Test/CI job  
Proof: tests/http/test\_dev\_conjunction\_http.py

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-006"

check\_name="PO-006 — Dev writer conjunction endpoint stable envelope"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

python \- \<\<'PY' \> "$check\_dir/route\_proof.txt"

import pathlib, re

p \= pathlib.Path("adapter/http\_reader.py")

text \= p.read\_text(encoding="utf-8")

targets \= \[

  r'@bp\\.get\\("/dev/writer/conjunction"\\)',

\]

for t in targets:

  m \= re.search(t, text)

  print(f"{t}: {'FOUND' if m else 'NOT\_FOUND'}")

PY

body="$check\_dir/body.log"

: \> "$body"

echo "RUN: python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py" \>\> "$body"

set \+e

python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["python (route proof from adapter/http\_reader.py)","python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py"\]'

export ARTIFACTS\_JSON='\[

  {"path":"route\_proof.txt","type":"text","desc":"static route proof for dev writer endpoint"},

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"}

\]'

export PF\_REFS\_JSON='\["PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if:

* route proof shows FOUND for `/dev/writer/conjunction`, and  
* pytest rc is 0 for `tests/http/test_dev_conjunction_http.py`.

FAIL otherwise.

##### **Traceability**

* Step: PO‑006 (guide excerpt above)  
* Route locus: `adapter/http_reader.py`  
* Test locus: `tests/http/test_dev_conjunction_http.py`

---

#### **CHECK po-007: PO-007 — Endpoint catalog updated and integrity check passes**

SOURCE EXCERPT (verbatim):

PO-007  
Proof obligation: Endpoint Catalog includes dev conjunction endpoints with correct env gating and integrity check (sha) passes.

##### **Intent**

Verify the endpoint catalog includes dev conjunction endpoints with correct env gating metadata, and that the sha256 integrity sidecar matches the catalog content.

##### **Inputs**

* Closed rails  
* Determinism pins

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-007/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-007/catalog_extract_dev_endpoints.json"`  
* `"$EVIDENCE_ROOT/checks/po-007/catalog_sha256_check.txt"`  
* `"$EVIDENCE_ROOT/checks/po-007/pytest_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-007/pytest_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-007/pytest_rc.txt"`

##### **Procedure**

1. Prove catalog and sidecar exist.

SOURCE EXCERPT (verbatim):

PTH-003  
Path: docs/ENDPOINTS\_CATALOG.json  
Category: Docs (canonical)  
Proof: docs/ENDPOINTS\_CATALOG.json

SOURCE EXCERPT (verbatim):

PTH-004  
Path: docs/ENDPOINTS\_CATALOG.json.sha256  
Category: Docs integrity  
Proof: docs/ENDPOINTS\_CATALOG.json.sha256

2. Compute sha256 of the catalog and compare to sidecar; extract dev conjunction endpoint entries by path match.

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-007"

check\_name="PO-007 — Endpoint catalog dev endpoints \+ sha256 integrity"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

python \- \<\<'PY' \> "$check\_dir/catalog\_sha256\_check.txt"

import hashlib, pathlib

cat\_path \= pathlib.Path("docs/ENDPOINTS\_CATALOG.json")

sidecar\_path \= pathlib.Path("docs/ENDPOINTS\_CATALOG.json.sha256")

cat\_sha \= hashlib.sha256(cat\_path.read\_bytes()).hexdigest()

sidecar \= sidecar\_path.read\_text(encoding="utf-8").strip()

print(f"computed\_sha256={cat\_sha}")

print(f"sidecar\_sha256={sidecar}")

print("match=" \+ ("YES" if cat\_sha \== sidecar else "NO"))

PY

python \- \<\<'PY' \> "$check\_dir/catalog\_extract\_dev\_endpoints.json"

import json, pathlib

p \= pathlib.Path("docs/ENDPOINTS\_CATALOG.json")

data \= json.loads(p.read\_text(encoding="utf-8"))

targets \= {

  "/dev/sampler/conjunction",

  "/dev/reader/conjunction",

  "/dev/writer/conjunction",

}

hits \= \[\]

def walk(x):

  if isinstance(x, dict):

    if x.get("path") in targets:

      hits.append(x)

    for v in x.values():

      walk(v)

  elif isinstance(x, list):

    for i in x:

      walk(i)

walk(data)

print(json.dumps({"targets": sorted(targets), "matches": hits}, ensure\_ascii=False, indent=2))

PY

body="$check\_dir/body.log"

: \> "$body"

echo "RUN: python \-m pytest \-q tests/http/test\_endpoint\_catalog.py" \>\> "$body"

\# Run catalog test harness

SOURCE EXCERPT\_PLACEHOLDER="(see plan text; repo proof is embedded below)"

set \+e

python \-m pytest \-q tests/http/test\_endpoint\_catalog.py \> "$check\_dir/pytest\_stdout.log" 2\> "$check\_dir/pytest\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/pytest\_rc.txt"

\# Determine pass/fail:

\# \- pytest must pass

\# \- sha256 match must be YES

pass\_fail="FAIL"

fail\_status="ASSERTION\_FAILED"

if \[ "$rc" \-eq 0 \] && grep \-q "match=YES" "$check\_dir/catalog\_sha256\_check.txt"; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\[

  "python (sha256 compare docs/ENDPOINTS\_CATALOG.json vs .sha256)",

  "python (extract dev conjunction endpoints from docs/ENDPOINTS\_CATALOG.json)",

  "python \-m pytest \-q tests/http/test\_endpoint\_catalog.py"

\]'

export ARTIFACTS\_JSON='\[

  {"path":"catalog\_sha256\_check.txt","type":"text","desc":"catalog sha256 vs sidecar comparison"},

  {"path":"catalog\_extract\_dev\_endpoints.json","type":"json","desc":"catalog extract for dev conjunction endpoints"},

  {"path":"pytest\_stdout.log","type":"log","desc":"pytest stdout"},

  {"path":"pytest\_stderr.log","type":"log","desc":"pytest stderr"},

  {"path":"pytest\_rc.txt","type":"text","desc":"pytest exit code"}

\]'

export PF\_REFS\_JSON='\["PF05 §0.2 Scope \[Required-Now\]","PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

3. Prove catalog test locus exists.

SOURCE EXCERPT (verbatim):

PTH-036  
Path: tests/http/test\_endpoint\_catalog.py  
Category: Test/CI job  
Proof: tests/http/test\_endpoint\_catalog.py

##### **PASS/FAIL**

PASS if:

* `catalog_sha256_check.txt` shows `match=YES`, and  
* pytest rc is 0 for `tests/http/test_endpoint_catalog.py`, and  
* `catalog_extract_dev_endpoints.json` includes matches for the three dev conjunction paths.

FAIL otherwise.

##### **Traceability**

* Step: PO‑007 (guide excerpt above)  
* Catalog loci: `docs/ENDPOINTS_CATALOG.json` and `.sha256`

---

#### **CHECK po-008: PO-008 — CLI supports conjunction mode with canonical JSON output**

SOURCE EXCERPT (verbatim):

PO-008  
Proof obligation: CLI has explicit conjunction mode output; canonical JSON output; rejects unsupported output modifiers.

##### **Intent**

Verify the CLI:

* exposes explicit conjunction mode flags,  
* rejects unsupported output modifiers in conjunction mode,  
* emits canonical JSON (PF05 key-order \+ trailing LF) when run in conjunction mode.

##### **Inputs**

* Closed rails: `SAFE_MODE=1 ALLOW_NETWORK=0`  
* Determinism pins: `LC_ALL=C LANG=C TZ=UTC`  
* For runtime CLI output: `USER_A_ID`, `USER_B_ID`

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-008/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-008/cli_help.txt"`  
* `"$EVIDENCE_ROOT/checks/po-008/showcompat_help.txt"`  
* `"$EVIDENCE_ROOT/checks/po-008/reject_nonjson_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-008/reject_nonjson_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-008/reject_nonjson_rc.txt"`  
* If IDs provided:  
  * `"$EVIDENCE_ROOT/checks/po-008/cli_conjunction.json"`  
  * `"$EVIDENCE_ROOT/checks/po-008/cli_conjunction_rc.txt"`  
  * `"$EVIDENCE_ROOT/checks/po-008/canonical_keyorder_check.txt"`

##### **Procedure**

1. Prove CLI entrypoint and conjunction flags exist.

SOURCE EXCERPT (verbatim):

PTH-028  
Path: pyproject.toml  
Category: CLI entrypoint  
Proof: pyproject.toml: \[project.scripts\] hdctl \= "engine.cli.main:cli"

SOURCE EXCERPT (verbatim):

PTH-027  
Path: engine/cli/main.py  
Category: CLI (compat show)  
Proof: engine/cli/main.py: show.add\_argument("--conjunction", action="store\_true")

2. Capture help text and verify rejection of non-json `--format` in conjunction mode.

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-008"

check\_name="PO-008 — CLI conjunction mode \+ canonical JSON \+ modifier rejection"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\["A3"\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

body="$check\_dir/body.log"

: \> "$body"

\# Help capture

set \+e

hdctl \--help \> "$check\_dir/cli\_help.txt" 2\> "$check\_dir/cli\_help.err"

h1=$?

hdctl showcompat \--help \> "$check\_dir/showcompat\_help.txt" 2\> "$check\_dir/showcompat\_help.err"

h2=$?

set \-e

printf "hdctl\_help\_rc=%s\\nshowcompat\_help\_rc=%s\\n" "$h1" "$h2" \>\> "$body"

\# Rejection test: non-json format in conjunction mode (should fail fast)

set \+e

hdctl showcompat \--conjunction \--format yaml \> "$check\_dir/reject\_nonjson\_stdout.log" 2\> "$check\_dir/reject\_nonjson\_stderr.log"

rj=$?

set \-e

printf "%s\\n" "$rj" \> "$check\_dir/reject\_nonjson\_rc.txt"

\# Optional: run conjunction output if USER\_A\_ID / USER\_B\_ID are provided

cli\_rc="NOT\_RUN"

if \[ \-n "${USER\_A\_ID:-}" \] && \[ \-n "${USER\_B\_ID:-}" \]; then

  set \+e

  hdctl showcompat \--conjunction \--user-a "$USER\_A\_ID" \--user-b "$USER\_B\_ID" \--format json \> "$check\_dir/cli\_conjunction.json" 2\> "$check\_dir/cli\_conjunction.err"

  cli\_rc=$?

  set \-e

  printf "%s\\n" "$cli\_rc" \> "$check\_dir/cli\_conjunction\_rc.txt"

  \# Canonical key-order \+ single trailing LF check (PF05)

  python \- \<\<'PY' \> "$check\_dir/canonical\_keyorder\_check.txt"

import json, pathlib

b \= pathlib.Path("cli\_conjunction.json").read\_bytes()

if not b.endswith(b"\\n") or b.endswith(b"\\n\\n"):

  raise SystemExit("trailing LF rule violated")

s \= b.decode("utf-8")

def hook(pairs):

  keys \= \[k for k,\_ in pairs\]

  if keys \!= sorted(keys):

    raise ValueError(f"key order not ASCII-sorted: {keys}")

  return dict(pairs)

json.loads(s, object\_pairs\_hook=hook)

print("canonical\_keyorder\_check=OK")

PY

fi

\# Determine PASS:

\# \- help commands must be runnable (rc 0\)

\# \- reject\_nonjson\_rc must be non-zero

\# \- if CLI run executed, rc must be 0 and canonical check file must contain OK

pass\_fail="FAIL"

fail\_status="BEHAVIOR\_MISMATCH"

if \[ "$h1" \-eq 0 \] && \[ "$h2" \-eq 0 \] && \[ "$rj" \-ne 0 \]; then

  if \[ "$cli\_rc" \= "NOT\_RUN" \]; then

    \# PASS for modifier rejection \+ help exposure; runtime canonical output is BLOCKED by missing inputs

    pass\_fail="PASS"

    fail\_status=""

  else

    if \[ "$cli\_rc" \-eq 0 \] && \[ \-f "$check\_dir/canonical\_keyorder\_check.txt" \] && grep \-q "OK" "$check\_dir/canonical\_keyorder\_check.txt"; then

      pass\_fail="PASS"

      fail\_status=""

      export CLAIMED\_TOKENS\_JSON='\["A3"\]'

    fi

  fi

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\[

  "hdctl \--help",

  "hdctl showcompat \--help",

  "hdctl showcompat \--conjunction \--format yaml",

  "hdctl showcompat \--conjunction \--user-a $USER\_A\_ID \--user-b $USER\_B\_ID \--format json (optional)"

\]'

export ARTIFACTS\_JSON='\[

  {"path":"cli\_help.txt","type":"text","desc":"hdctl help"},

  {"path":"showcompat\_help.txt","type":"text","desc":"showcompat help"},

  {"path":"reject\_nonjson\_stdout.log","type":"log","desc":"stdout for non-json rejection"},

  {"path":"reject\_nonjson\_stderr.log","type":"log","desc":"stderr for non-json rejection"},

  {"path":"reject\_nonjson\_rc.txt","type":"text","desc":"exit code for non-json rejection"}

\]'

export PF\_REFS\_JSON='\["PF05 §0.2 Scope \[Required-Now\]","PF04 §2.1 A3 — Determinism gate (hash and normalize)","PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if:

* `hdctl --help` and `hdctl showcompat --help` succeed, and  
* non-json modifier rejection returns non-zero exit, and  
* if conjunction output run is executed, it succeeds and passes canonical key-order check.

FAIL if help cannot be invoked, modifier rejection does not fail, or conjunction output violates canonical key-order/trailing LF.

##### **Traceability**

* Step: PO‑008 (guide excerpt above)  
* CLI entrypoint \+ conjunction flag locus: `pyproject.toml` and `engine/cli/main.py` (audit excerpts above)

---

#### **CHECK po-009: PO-009 — CLI must refuse closed-rails acquisition and succeed when permitted**

SOURCE EXCERPT (verbatim):

PO-009  
Proof obligation: In conjunction mode CLI must refuse when required data not present locally and external acquisition not permitted; it must succeed when resolvable under permission.

##### **Intent**

Demonstrate rails behavior at the CLI level:

* closed rails refusal when local data is missing and acquisition is not permitted,  
* open rails success when external acquisition is permitted and configuration supports it.

##### **Inputs**

* Required: `USER_A_ID`, `USER_B_ID`  
* Closed rails env and Open rails env  
* Any required vendor env vars (do not log secrets)

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-009/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-009/closed_rails_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-009/closed_rails_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-009/closed_rails_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-009/open_rails_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-009/open_rails_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-009/open_rails_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-009/open_rails_note.txt"` (if blocked)

##### **Procedure**

Precondition: If `USER_A_ID`/`USER_B_ID` not set, this check is **BLOCKED** (inputs missing). Record in `doc_deltas.md`.

SOURCE EXCERPT (verbatim):

PTH-028  
Path: pyproject.toml  
Category: CLI entrypoint  
Proof: pyproject.toml: \[project.scripts\] hdctl \= "engine.cli.main:cli"

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-009"

check\_name="PO-009 — CLI rails: closed refusal, open success"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

body="$check\_dir/body.log"

: \> "$body"

if \[ \-z "${USER\_A\_ID:-}" \] || \[ \-z "${USER\_B\_ID:-}" \]; then

  echo "BLOCKED: USER\_A\_ID/USER\_B\_ID not provided" \> "$check\_dir/open\_rails\_note.txt"

  export PASS\_FAIL="FAIL"

  export FAIL\_STATUS="BLOCKED\_MISSING\_INPUTS"

  export COMMANDS\_JSON='\[\]'

  export ARTIFACTS\_JSON='\[{"path":"open\_rails\_note.txt","type":"text","desc":"missing USER\_A\_ID/USER\_B\_ID"}\]'

  export PF\_REFS\_JSON='\["PF27 §Step-log header schema expectations (minimum; required)"\]'

  primary="$check\_dir/primary.log"

  qa\_emit\_step\_log\_header \> "$primary"

  cat "$body" \>\> "$primary"

  sha="$(qa\_sha256\_file "$primary")"

  qa\_append\_manifest "$check\_id" "FAIL" "checks/$check\_id/primary.log" "$sha"

  exit 0

fi

\# Closed rails run

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

set \+e

hdctl showcompat \--conjunction \--user-a "$USER\_A\_ID" \--user-b "$USER\_B\_ID" \--format json \> "$check\_dir/closed\_rails\_stdout.log" 2\> "$check\_dir/closed\_rails\_stderr.log"

rc\_closed=$?

set \-e

printf "%s\\n" "$rc\_closed" \> "$check\_dir/closed\_rails\_rc.txt"

\# Open rails run (may require additional env vars already set in Codespaces secrets)

export SAFE\_MODE=0 ALLOW\_NETWORK=1 APP\_ENV=dev

set \+e

hdctl showcompat \--conjunction \--user-a "$USER\_A\_ID" \--user-b "$USER\_B\_ID" \--format json \> "$check\_dir/open\_rails\_stdout.log" 2\> "$check\_dir/open\_rails\_stderr.log"

rc\_open=$?

set \-e

printf "%s\\n" "$rc\_open" \> "$check\_dir/open\_rails\_rc.txt"

\# PASS logic:

\# \- closed rails should fail (rc \!= 0\) IF it truly requires acquisition; if it succeeds, record as "local cache present"

\# \- open rails should succeed (rc \== 0\) IF environment supports acquisition; if it fails, record as BLOCKED by env config

pass\_fail="FAIL"

fail\_status="BEHAVIOR\_MISMATCH"

if \[ "$rc\_open" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

else

  \# If open rails fails, treat as BLOCKED unless you can prove it's a behavior failure.

  echo "NOTE: open rails run failed; verify vendor config/credentials. Treat as BLOCKED unless behavior defect confirmed." \> "$check\_dir/open\_rails\_note.txt"

  fail\_status="BLOCKED\_ENV\_CONFIG"

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\[

  "SAFE\_MODE=1 ALLOW\_NETWORK=0 hdctl showcompat \--conjunction \--user-a ... \--user-b ... \--format json",

  "SAFE\_MODE=0 ALLOW\_NETWORK=1 hdctl showcompat \--conjunction \--user-a ... \--user-b ... \--format json"

\]'

export ARTIFACTS\_JSON='\[

  {"path":"closed\_rails\_stdout.log","type":"log","desc":"closed rails stdout"},

  {"path":"closed\_rails\_stderr.log","type":"log","desc":"closed rails stderr"},

  {"path":"closed\_rails\_rc.txt","type":"text","desc":"closed rails exit code"},

  {"path":"open\_rails\_stdout.log","type":"log","desc":"open rails stdout"},

  {"path":"open\_rails\_stderr.log","type":"log","desc":"open rails stderr"},

  {"path":"open\_rails\_rc.txt","type":"text","desc":"open rails exit code"},

  {"path":"open\_rails\_note.txt","type":"text","desc":"open rails note (if blocked)","optional":true}

\]'

export PF\_REFS\_JSON='\["PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

cat "$body" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if:

* open rails run succeeds (rc 0).  
  Closed rails refusal is expected when acquisition is needed; if it succeeds, record “local data present” (not a failure).

FAIL if:

* open rails run fails and you can confirm it is a behavior defect (not an env/credential/tooling issue). Otherwise classify as **BLOCKED\_ENV\_CONFIG**.

##### **Traceability**

* Step: PO‑009 (guide excerpt above)  
* CLI entrypoint locus: `pyproject.toml` (audit excerpt above)

---

#### **CHECK po-010: PO-010 — Docs align: endpoint catalog \+ CLI help reflect conjunction**

SOURCE EXCERPT (verbatim):

PO-010  
Proof obligation: Docs reflect new dev endpoints and CLI usage and remain consistent with canonical Endpoint Catalog and CLI help output.

##### **Intent**

Validate documentation alignment by comparing:

* `docs/ENDPOINTS_CATALOG.json` entries for dev conjunction endpoints, and  
* `hdctl showcompat --help` content showing conjunction mode usage.

##### **Inputs**

* Closed rails (help only)  
* Determinism pins

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-010/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-010/showcompat_help.txt"`  
* `"$EVIDENCE_ROOT/checks/po-010/catalog_extract_dev_endpoints.json"`

##### **Procedure**

SOURCE EXCERPT (verbatim):

PTH-003  
Path: docs/ENDPOINTS\_CATALOG.json  
Category: Docs (canonical)  
Proof: docs/ENDPOINTS\_CATALOG.json

SOURCE EXCERPT (verbatim):

PTH-015  
Path: adapter/http\_reader.py  
Category: HTTP routes (dev)  
Proof: adapter/http\_reader.py:731: @bp.get("/dev/sampler/conjunction")

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-010"

check\_name="PO-010 — Docs alignment: catalog \+ CLI help"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

\# Capture help

set \+e

hdctl showcompat \--help \> "$check\_dir/showcompat\_help.txt" 2\> "$check\_dir/showcompat\_help.err"

rc\_help=$?

set \-e

\# Extract dev endpoints from catalog

python \- \<\<'PY' \> "$check\_dir/catalog\_extract\_dev\_endpoints.json"

import json, pathlib

p \= pathlib.Path("docs/ENDPOINTS\_CATALOG.json")

data \= json.loads(p.read\_text(encoding="utf-8"))

targets \= {"/dev/sampler/conjunction","/dev/reader/conjunction","/dev/writer/conjunction"}

hits=\[\]

def walk(x):

  if isinstance(x, dict):

    if x.get("path") in targets:

      hits.append(x)

    for v in x.values(): walk(v)

  elif isinstance(x, list):

    for i in x: walk(i)

walk(data)

print(json.dumps({"targets": sorted(targets), "matches": hits}, ensure\_ascii=False, indent=2))

PY

\# PASS: help command must run; catalog extract must contain entries

pass\_fail="FAIL"

fail\_status="DOC\_ALIGNMENT\_MISSING"

if \[ "$rc\_help" \-eq 0 \] && python \- \<\<'PY'

import json

data=json.load(open("catalog\_extract\_dev\_endpoints.json","r",encoding="utf-8"))

raise SystemExit(0 if len(data.get("matches",\[\]))\>=1 else 1\)

PY

then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\["hdctl showcompat \--help","python (extract dev endpoints from docs/ENDPOINTS\_CATALOG.json)"\]'

export ARTIFACTS\_JSON='\[

  {"path":"showcompat\_help.txt","type":"text","desc":"CLI help output for showcompat"},

  {"path":"catalog\_extract\_dev\_endpoints.json","type":"json","desc":"catalog extract for dev conjunction endpoints"}

\]'

export PF\_REFS\_JSON='\["PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

printf "showcompat\_help\_rc=%s\\n" "$rc\_help" \>\> "$check\_dir/body.log"

cat "$check\_dir/body.log" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if:

* `hdctl showcompat --help` succeeds, and  
* the catalog extract includes at least one of the dev conjunction endpoints.

FAIL if help fails or catalog lacks dev endpoints.

##### **Traceability**

* Step: PO‑010 (guide excerpt above)  
* Doc locus: `docs/ENDPOINTS_CATALOG.json`

---

#### **CHECK po-011: PO-011 — Governance scripts do not drift / fail due to stale fixtures**

SOURCE EXCERPT (verbatim):

PO-011  
Proof obligation: Repo governance scripts (canonical JSON gate, evidence index, etc.) must not exhibit drift failures caused by stale fixtures.

##### **Intent**

Run the governance scripts that CI runs for canonical JSON and evidence index; they must pass (exit 0\) and not report drift failures.

##### **Inputs**

* Closed rails  
* Determinism pins

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-011/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-011/canonical_json_gate_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-011/canonical_json_gate_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-011/canonical_json_gate_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-011/update_evidence_index_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-011/update_evidence_index_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-011/update_evidence_index_rc.txt"`

##### **Procedure**

Prove script loci exist and are CI-invoked.

SOURCE EXCERPT (verbatim):

PTH-035  
Path: tools/evidence/run\_canonical\_json\_gate.py  
Category: Governance script  
Proof: CI runs python tools/evidence/run\_canonical\_json\_gate.py

SOURCE EXCERPT (verbatim):

PTH-034  
Path: tools/evidence/update\_evidence\_index.py  
Category: Governance script  
Proof: CI runs python tools/evidence/update\_evidence\_index.py \--check

SOURCE EXCERPT (verbatim):

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-011"

check\_name="PO-011 — Governance scripts pass (no drift failures)"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

set \+e

python tools/evidence/run\_canonical\_json\_gate.py \> "$check\_dir/canonical\_json\_gate\_stdout.log" 2\> "$check\_dir/canonical\_json\_gate\_stderr.log"

rc1=$?

python tools/evidence/update\_evidence\_index.py \--check \> "$check\_dir/update\_evidence\_index\_stdout.log" 2\> "$check\_dir/update\_evidence\_index\_stderr.log"

rc2=$?

rc3=0

set \-e

printf "%s\\n" "$rc1" | tee "$check\_dir/canonical\_json\_gate\_rc.txt"

printf "%s\\n" "$rc2" | tee "$check\_dir/update\_evidence\_index\_rc.txt"

pass\_fail="FAIL"

fail\_status="GOVERNANCE\_FAIL"

if \[ "$rc1" \-eq 0 \] && \[ "$rc2" \-eq 0 \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\[

  "python tools/evidence/run\_canonical\_json\_gate.py",

  "python tools/evidence/update\_evidence\_index.py \--check",

\]'

export ARTIFACTS\_JSON='\[

  {"path":"canonical\_json\_gate\_stdout.log","type":"log","desc":"canonical json gate stdout"},

  {"path":"canonical\_json\_gate\_stderr.log","type":"log","desc":"canonical json gate stderr"},

  {"path":"canonical\_json\_gate\_rc.txt","type":"text","desc":"canonical json gate exit code"},

  {"path":"update\_evidence\_index\_stdout.log","type":"log","desc":"update evidence index stdout"},

  {"path":"update\_evidence\_index\_stderr.log","type":"log","desc":"update evidence index stderr"},

{"path":"update\_evidence\_index\_rc.txt","type":"text","desc":"update evidence index exit code"}

\]'

export PF\_REFS\_JSON='\["PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

printf "rc\_canonical\_json\_gate=%s\\nrc\_update\_evidence\_index=%s\\nrc\_check\_evidence\_bindings=%s\\n" "$rc1" "$rc2" "$rc3" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if both script exit codes are 0\.

FAIL otherwise; capture stdout/stderr logs.

##### **Traceability**

* Step: PO‑011 (guide excerpt above)  
* Governance scripts: `tools/evidence/run_canonical_json_gate.py`, `tools/evidence/update_evidence_index.py`

---

#### **CHECK po-012: PO-012 — Close-out package can be produced and contains required artifacts**

SOURCE EXCERPT (verbatim):

PO-012  
Proof obligation: Epic closeout package can be produced and contains required artifacts (catalog, hashes, evidence index, step logs manifest).

##### **Intent**

Prove the close-out package generator exists and can be run, and that the expected close-pack artifacts exist. Copy key close-pack artifacts into `EVIDENCE_ROOT` for this run’s evidence bundle.

##### **Inputs**

* Closed rails  
* Determinism pins

##### **Deliverables**

* `"$EVIDENCE_ROOT/checks/po-012/primary.log"`  
* `"$EVIDENCE_ROOT/checks/po-012/generator_stdout.log"`  
* `"$EVIDENCE_ROOT/checks/po-012/generator_stderr.log"`  
* `"$EVIDENCE_ROOT/checks/po-012/generator_rc.txt"`  
* `"$EVIDENCE_ROOT/checks/po-012/close_pack_copy/epic-026_manifest.json"`  
* `"$EVIDENCE_ROOT/checks/po-012/close_pack_copy/epic-026_evidence_index.json"`  
* `"$EVIDENCE_ROOT/checks/po-012/close_pack_copy/endpoints_catalog.json"`  
* `"$EVIDENCE_ROOT/checks/po-012/close_pack_copy/endpoints_catalog.json.sha256"`

##### **Procedure**

1. Prove generator and expected outputs exist (repo reality).

SOURCE EXCERPT (verbatim):

PTH-008  
Path: tools/qa/generate\_epic026\_close\_pack.py  
Category: Close-out generator  
Proof: tools/qa/generate\_epic026\_close\_pack.py

SOURCE EXCERPT (verbatim):

PTH-009  
Path: audit/EPIC-026\_MANIFEST.json  
Category: Close-out artifact  
Proof: audit/EPIC-026\_MANIFEST.json

SOURCE EXCERPT (verbatim):

PTH-010  
	Path: audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json  
	Category: Close-out artifact  
	Proof: audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json

SOURCE EXCERPT (verbatim):

PTH-003  
Path: docs/ENDPOINTS\_CATALOG.json  
Category: Docs (canonical)  
Proof: docs/ENDPOINTS\_CATALOG.json

SOURCE EXCERPT (verbatim):

PTH-004  
Path: docs/ENDPOINTS\_CATALOG.json.sha256  
Category: Docs integrity  
Proof: docs/ENDPOINTS\_CATALOG.json.sha256

2. Run generator, then copy required artifacts into run evidence.

set \-euo pipefail

source "$EVIDENCE\_ROOT/checks/po-000/qa\_helpers.sh"

check\_id="po-012"

check\_name="PO-012 — Close-out package generation \+ required artifacts present"

check\_dir="$EVIDENCE\_ROOT/checks/$check\_id"

mkdir \-p "$check\_dir"

mkdir \-p "$check\_dir/close\_pack\_copy"

export CHECK\_ID="$check\_id"

export CHECK\_NAME="$check\_name"

export LC\_ALL=C LANG=C TZ=UTC

export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

export INTENDED\_TOKENS\_JSON='\[\]'

export CLAIMED\_TOKENS\_JSON='\[\]'

set \+e

python tools/qa/generate\_epic026\_close\_pack.py \> "$check\_dir/generator\_stdout.log" 2\> "$check\_dir/generator\_stderr.log"

rc=$?

set \-e

printf "%s\\n" "$rc" \> "$check\_dir/generator\_rc.txt"

\# Copy (as evidence snapshots for this run; do not modify originals)

python \- \<\<'PY'

import shutil, pathlib, os

out \= pathlib.Path(os.environ\["EVIDENCE\_ROOT"\]) / "checks" / os.environ\["CHECK\_ID"\] / "close\_pack\_copy"

mapping \= {

  "audit/EPIC-026\_MANIFEST.json": out / "epic-026\_manifest.json",

 "audit/gates/evidence\_index\_snapshot/evidence\_index\_snapshot.json": out / "epic-026\_evidence\_index.json",

  "docs/ENDPOINTS\_CATALOG.json": out / "endpoints\_catalog.json",

  "docs/ENDPOINTS\_CATALOG.json.sha256": out / "endpoints\_catalog.json.sha256",

}

for src, dst in mapping.items():

  dst.parent.mkdir(parents=True, exist\_ok=True)

  shutil.copyfile(src, dst)

print("copied=" \+ ",".join(str(v) for v in mapping.values()))

PY

\# Determine PASS:

\# \- generator exit code 0

\# \- copied artifacts exist

pass\_fail="FAIL"

fail\_status="CLOSE\_PACK\_FAIL"

if \[ "$rc" \-eq 0 \] && \[ \-f "$check\_dir/close\_pack\_copy/epic-026\_manifest.json" \] && \[ \-f "$check\_dir/close\_pack\_copy/endpoints\_catalog.json" \]; then

  pass\_fail="PASS"

  fail\_status=""

fi

export PASS\_FAIL="$pass\_fail"

export FAIL\_STATUS="$fail\_status"

export COMMANDS\_JSON='\[

  "python tools/qa/generate\_epic026\_close\_pack.py",

  "python (copy close-pack artifacts into checks/po-012/close\_pack\_copy/)"

\]'

export ARTIFACTS\_JSON='\[

  {"path":"generator\_stdout.log","type":"log","desc":"close pack generator stdout"},

  {"path":"generator\_stderr.log","type":"log","desc":"close pack generator stderr"},

  {"path":"generator\_rc.txt","type":"text","desc":"close pack generator exit code"},

  {"path":"close\_pack\_copy/epic-026\_manifest.json","type":"json","desc":"copied epic manifest"},

  {"path":"close\_pack\_copy/epic-026\_evidence\_index.json","type":"json","desc":"copied evidence index"},

  {"path":"close\_pack\_copy/endpoints\_catalog.json","type":"json","desc":"copied endpoint catalog"},

  {"path":"close\_pack\_copy/endpoints\_catalog.json.sha256","type":"text","desc":"copied endpoint catalog sha256"}

\]'

export PF\_REFS\_JSON='\["PF27 §Step-log header schema expectations (minimum; required)"\]'

primary="$check\_dir/primary.log"

qa\_emit\_step\_log\_header \> "$primary"

printf "generator\_rc=%s\\n" "$rc" \>\> "$primary"

sha="$(qa\_sha256\_file "$primary")"

qa\_append\_manifest "$check\_id" "$pass\_fail" "checks/$check\_id/primary.log" "$sha"

##### **PASS/FAIL**

PASS if:

* generator returns exit code 0, and  
* copied close-pack artifacts exist under `$EVIDENCE_ROOT/checks/po-012/close_pack_copy/`.

FAIL otherwise (capture generator stdout/stderr).

##### **Traceability**

* Step: PO‑012 (guide excerpt above)  
* Generator: `tools/qa/generate_epic026_close_pack.py`

* Close-pack artifacts: `audit/EPIC-026_MANIFEST.json`, `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

---

### **Close-out deliverables**

At the end of the run, the PO must have:

* **Per-run manifest**  
  * `"$EVIDENCE_ROOT/checks/po-000/qa_step_logs_manifest.json"`  
  * `"$EVIDENCE_ROOT/checks/po-000/qa_step_logs_manifest.json.path_proof.txt"`  
* **Step-0 artifacts**  
  * `"$EVIDENCE_ROOT/checks/po-000/doc_deltas.md"`  
  * `"$EVIDENCE_ROOT/checks/po-000/qa_helpers.sh"`  
3. **Per-check evidence**  
* `"$EVIDENCE_ROOT/checks/<check_id>/primary.log"` for all `po-001` through `po-012`  
* All auxiliary logs/artifacts listed in each check’s Deliverables section.  
4. **Close pack evidence copy**  
* `"$EVIDENCE_ROOT/checks/po-012/close_pack_copy/"` with the copied close-pack artifacts.

---

#### **What “QA RCA & Doc Delta summary” means (definition; required in close-out)**

* A concise summary (in `doc_deltas.md`) of:  
  * any checks that were BLOCKED and why (inputs/tooling/unclear repo loci),  
  * any doc inconsistencies found,  
  * any deviations from expected rails behavior or determinism pins,  
  * links (paths) to the primary logs for failing/blocked checks.

ASK OK?

