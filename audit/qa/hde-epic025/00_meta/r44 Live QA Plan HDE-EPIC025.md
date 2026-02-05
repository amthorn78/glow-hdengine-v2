## **1\) r44 Live QA Plan HDE-EPIC025**

### **Front matter**

#### **Canon precedence statement (required)**

This Live QA Plan is governed by canon in this order:

1. **PF10** is binding where it speaks (especially plan hygiene and path discipline). PF10 — HDE-Build-Notes, §2.7 Planning path discipline: canon-first \+ CA/IG verbatim validation; never fabricate repo paths. PF10 — HDE-Build-Notes, §2.3 Prohibited characters in planning reviews and planning documents (ellipsis only).  
2. Where PF10 is silent, **PF19** governs QA procedure and evidence posture (especially transcript-style evidence and preflight of entrypoints). PF19 — Glow QA Guide, §3.4.6 Step-level Deliverables (no screen-only acceptance). PF19 — Glow QA Guide, §3.4.8 Rails posture for manual Live QA (Entrypoint existence preflight).  
3. **PF27** defines the **template structure and headings** used for this Live QA Plan. PF27 — Canon-Plan-Templates, locator Unknown.

Non-canonical inputs are used only for epic-specific requirements and repo reality. Any such usage is inlined verbatim as a `SOURCE EXCERPT (verbatim)` at the point of use, and is never referenced by filename.

#### **Epic**

HDE-EPIC025

#### **Date**

2026-01-30 (Europe/London)

#### **Owner**

Product Owner (PO) executing Live QA in Codespaces.

#### **Evidence root**

Set **one** operator variable (fresh, lowercase ASCII) under `audit/` or `artifacts/`:

* Canonical evidence root (acceptance binding): audit/qa/hde-epic025

All QA-created files in this run must be written under **EVIDENCE\_ROOT** (no QA-created files under `docs/`).

#### **One-sentence goal**

Prove that the Epic025 compat and reader (/reader) surfaces behave as specified, while producing governed, reviewable evidence artifacts and reproducible gates for endpoints, determinism, and evidence indexing.

#### **Scope (what’s in and out)**

**In scope (must be proven by this run):**

SOURCE EXCERPT (verbatim):  
Scope recap: This epic introduces/validates:

* Internal compatibility API split: probe-only reads viewer prefs; compute-only performs write.  
* Endpoints: /api/compat/v1 and /reader registered in endpoint catalog,  
* Showcompat artifacts: CLI `showcompat` emits canonical JSON; parity and identity enforced; evidence captured with sha256.  
* Evidence index: docs/evidence/INDEX.json and sha file kept in sync and schema-valid.  
* Determinism rails: SAFE profile default, network disabled by default, env pins enforced.

**Out of scope (explicitly deferred):**

SOURCE EXCERPT (verbatim):  
Deferred: Any PF14 mechanics changes; any PF01 math spec changes; any new narrative deliverables.

#### **Non-goals**

* No performance benchmarking.  
* No UI/UX review beyond verifying endpoints and artifacts.  
* No scope expansion into PF14 mechanics changes, PF01 math changes, or narrative deliverables (explicitly deferred above).

#### **Risks**

* Some scripts and tests may exist but fail in Codespaces due to missing dependencies; this must be captured in step logs (do not “hand-wave”).

* Evidence index regeneration may change repo state; doc deltas must be recorded in `doc_deltas.md`.  
* Any mismatch between endpoint catalog and runtime endpoints must be treated as a FAIL (capture evidence).

#### **Preconditions**

* You are in a GitHub Codespaces terminal at repo root.  
* Python is available (`python`), and test runner is available (`python -m pytest`).  
* You can write under `audit/` (and optionally `artifacts/`).

#### **Tools**

* `bash` shell in Codespaces  
* `python` (for running repo scripts and parsing)  
* `python -m pytest` (for tests)  
* `git` (for commit \+ diff capture)  
* Standard shell utilities (`mkdir`, `cp`, `sha256sum`, `sed`, `grep`)

---

### **PF23 anchors (repo loci you will touch)**

Only include loci that are proven by repo reality; each locus below includes a verbatim proof excerpt.

1. `docs/ENDPOINTS_CATALOG.json`

SOURCE EXCERPT (verbatim):  
Paths: docs/ENDPOINTS\_CATALOG.json \-\> artifacts/audit/ENDPOINTS\_CATALOG.json

Excerpt:

{"public": \["/api/compat/v1", "/reader"\], "internal": \[\]}

2. `scripts/hdctl.py` (showcompat invocation exists)

SOURCE EXCERPT (verbatim):  
cmd \= \[sys.executable, "scripts/hdctl.py", "showcompat"\]

3. `ci/checks/check_env_pins.sh` (rails pins enforcement)

SOURCE EXCERPT (verbatim):  
Proof:

* run: bash ci/checks/check\_env\_pins.sh  
4. `tools/evidence/update_evidence_index.py`

SOURCE EXCERPT (verbatim):  
32: run: python tools/evidence/update\_evidence\_index.py  
36: run: python tools/evidence/update\_evidence\_index.py \--check

5. `tools/evidence/run_canonical_json_gate.py`

SOURCE EXCERPT (verbatim):  
29: run: python tools/evidence/run\_canonical\_json\_gate.py

6. `tools/evidence/run_sanity_pipeline.py`

SOURCE EXCERPT (verbatim):  
58: run: python tools/evidence/run\_sanity\_pipeline.py

7. Showcompat artifact output location (existing)

SOURCE EXCERPT (verbatim):

* artifacts/cli/showcompat/stdout.json  
  {  
  "meta": {"profile": "SAFE", "allow\_network": false},  
  "compat": {"ok": true, "sha256": "3b0e2d4\<."},  
  "outputs": {"stdout": "artifacts/cli/showcompat/stdout.json"}  
  }  
8. Endpoint proof log locations (existing)

SOURCE EXCERPT (verbatim):

* artifacts/proofs/success\_get.txt  
  status\_code=200  
  path=/api/compat/v1  
* artifacts/proofs/endpoints\_env\_gate\_proof.log  
  ALLOW\_NETWORK=0  
  HD\_PROFILE=SAFE  
  status=403 forbidden when attempting external egress  
9. Evidence index hash file (existing)

SOURCE EXCERPT (verbatim):

* docs/evidence/INDEX.sha256  
  9f2a6b3c3d5d4a1e2f\<shortened\> docs/evidence/INDEX.json

---

### **Operator setup: evidence root and environment**

**Goal:** establish a clean evidence root and a reusable step-log header writer so every check emits governed artifacts.

**PO actions**

1. Export `EVIDENCE_ROOT` to a fresh lowercase path under `audit/` for this run.

export EVIDENCE\_ROOT="audit/qa/hde-epic025"

2. Create the PF27 evidence directory structure under `EVIDENCE_ROOT`.

mkdir \-p \\

  "${EVIDENCE\_ROOT}/00\_meta" \\

  "${EVIDENCE\_ROOT}/checks"

3. Create the canonical step-log header writer under `EVIDENCE_ROOT` (used by all checks).

cat \> "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \<\<'PY'

import os, json, datetime

required \= \["CHECK\_ID","CHECK\_NAME","COMMANDS\_JSON","PASS\_FAIL","ARTIFACTS\_JSON","PF\_REFS\_JSON"\]

for k in required:  
if k not in os.environ:  
raise SystemExit("missing env: " \+ k)

raw\_status \= os.environ\["PASS\_FAIL"\]

raw\_fail\_status \= os.environ.get("FAIL\_STATUS", "")

if raw\_status \== "pass":  
status \= "PASS"  
fail\_status \= ""  
else:  
status \= raw\_status  
if status \== "fail":  
status \= raw\_fail\_status if raw\_fail\_status else "FAIL\_BEHAVIOR"

if status \== "FAIL\_ENVIRONMENT":  
status \= "FAIL\_TOOLING"

allowed\_status \= \["PASS","FAIL\_BEHAVIOR","FAIL\_TOOLING","TOOLING\_BLOCKED","SKIPPED","WARN"\]  
if status not in allowed\_status:  
status \= "FAIL\_BEHAVIOR"

if status \== "PASS":  
fail\_status \= ""  
elif status in \["FAIL\_BEHAVIOR","FAIL\_TOOLING"\]:  
fail\_status \= status  
else:  
fail\_status \= raw\_fail\_status if raw\_fail\_status in \["FAIL\_BEHAVIOR","FAIL\_TOOLING","FAIL\_ENVIRONMENT"\] else "FAIL\_TOOLING"

commands\_list \= json.loads(os.environ\["COMMANDS\_JSON"\])  
command \= "\\n".join(commands\_list) if commands\_list else "N/A"

command\_provenance \= "Copy/paste from plan"

captured\_env \= {  
"MODO\_AI\_BUNDLE": os.environ.get("MODO\_AI\_BUNDLE", ""),  
"MODO\_AI\_VERBOSE": os.environ.get("MODO\_AI\_VERBOSE", ""),  
"MODO\_RAILS": os.environ.get("MODO\_RAILS", ""),  
"LC\_ALL": os.environ.get("LC\_ALL", ""),  
"LANG": os.environ.get("LANG", ""),  
"TZ": os.environ.get("TZ", ""),  
}

hdr \= {  
"check\_id": os.environ\["CHECK\_ID"\],  
"check\_name": os.environ\["CHECK\_NAME"\],  
"captured\_env": captured\_env,  
"timestamp\_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z",  
"command": command,  
"command\_provenance": command\_provenance,  
"status": status,  
"fail\_status": fail\_status,  
"intended\_tokens": \[\],  
"claimed\_tokens": \[\],  
"artifacts": json.loads(os.environ\["ARTIFACTS\_JSON"\]),  
"pf\_refs": json.loads(os.environ\["PF\_REFS\_JSON"\]),  
}

print(json.dumps(hdr, sort\_keys=True))

PY

4. Capture a baseline repo snapshot (commit \+ status) for later doc-delta accounting.

{

  echo "timestamp\_utc: $(python \-c 'import datetime; print(datetime.datetime.utcnow().replace(microsecond=0).isoformat()+\\"Z\\")')"

  echo "git\_rev\_parse\_head:"

  git rev-parse HEAD

  echo "git\_status\_porcelain:"

  git status \--porcelain

} \> "${EVIDENCE\_ROOT}/00\_meta/repo\_baseline.txt"

---

#### **Step-0A: Evidence root governance**

**Goal:** ensure the run’s evidence is confined to `EVIDENCE_ROOT` and is reviewable without any non-canonical document.

**PO actions**

1. Verify `EVIDENCE_ROOT` is set and points under `audit/` (or `artifacts/`).

echo "EVIDENCE\_ROOT=${EVIDENCE\_ROOT}"

case "${EVIDENCE\_ROOT}" in

  audit/\*|artifacts/\*) echo "ok: evidence root under audit/ or artifacts/";;

\*) echo "fail: evidence root must be under audit/ or artifacts/"; (exit 1);;

esac

2. Create a simple evidence root manifest.

cat \> "${EVIDENCE\_ROOT}/00\_meta/evidence\_root\_manifest.txt" \<\<'EOF'

evidence\_root\_manifest

\- all qa-created artifacts for this run live under EVIDENCE\_ROOT

\- repo files under docs/ and artifacts/ may be read and copied into EVIDENCE\_ROOT

\- no qa-created files under docs/

EOF

---

#### **Step-0B: QA Step Logs manifest**

**Goal:** pre-create the required meta artifacts and a manifest placeholder that will be finalized at close-out.

**PO actions**

1. Create `doc_deltas.md` with BLOCKERS and CAVEATS sections.

cat \> "${EVIDENCE\_ROOT}/00\_meta/doc\_deltas.md" \<\<'EOF'

\# doc\_deltas

\#\# blockers

\- none recorded yet

\#\# caveats

\- none recorded yet

EOF

2. Create an initial `qa_step_logs_manifest.json` stub (will be regenerated at close-out).

cat \> "${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json" \<\<'EOF'

{

  "epic\_id": "hde-epic025",

  "generated\_utc": "pending",

  "checks": \[\]

}

EOF

3. Create a path proof for the manifest (sha \+ ls).

{

  echo "ls \-la:"

  ls \-la "${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json"

  echo

  echo "sha256sum:"

  sha256sum "${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json"

} \> "${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json.path\_proof.txt"

---

#### **Mandatory Step-0 artifacts**

By the end of Step-0A/0B, the following must exist under `EVIDENCE_ROOT`:

* `00_meta/repo_baseline.txt`  
* `00_meta/evidence_root_manifest.txt`  
* `00_meta/doc_deltas.md`  
* `00_meta/write_step_log_header.py`  
* `qa_step_logs_manifest.json`  
* `qa_step_logs_manifest.json.path_proof.txt`

---

#### **Step-0C: Runbook check matrix**

This plan’s execution order is:

1. `d0_discovery`  
2. `po-001` through `po-014` (in numeric order)

---

### **Runbook check matrix**

| check\_id | check\_name | surface mapping | rails profile | primary evidence artifact |
| ----- | ----- | ----- | ----- | ----- |
| d0\_discovery | d0\_discovery | evidence boot \+ repo baseline | safe | `${EVIDENCE_ROOT}/checks/d0_discovery/primary.log` |
| po-001 | po-001 | compat route \+ probe/compute split | safe | `${EVIDENCE_ROOT}/checks/po-001/primary.log` |
| po-002 | po-002 | compat malformed/empty identifier error posture | safe | `${EVIDENCE_ROOT}/checks/po-002/primary.log` |
| po-003 | po-003 | compat probe constraints (no compute, no request body)  | safe | `${EVIDENCE_ROOT}/checks/po-003/primary.log` |
| po-004 | po-004 | endpoint catalog entries and mirror | safe | `${EVIDENCE_ROOT}/checks/po-004/primary.log` |
| po-005 | po-005 | showcompat canonical output (CLI) | safe | `${EVIDENCE_ROOT}/checks/po-005/primary.log` |
| po-006 | po-006 | canonical bytes determinism  | safe | `${EVIDENCE_ROOT}/checks/po-006/primary.log` |
| po-007 | po-007 | reader proof surface internal harness gating  | safe | `${EVIDENCE_ROOT}/checks/po-007/primary.log` |
| po-008 | po-008 | reader proof surface internal harness gating  | safe | `${EVIDENCE_ROOT}/checks/po-008/primary.log` |
| po-009 | po-009 | canonical json determinism | safe | `${EVIDENCE_ROOT}/checks/po-009/primary.log` |
| po-010 | po-010 | evidence discipline (manifest, index, logs) \+ env pins | safe | `${EVIDENCE_ROOT}/checks/po-010/primary.log` |
| po-011 | po-011 | epic closure record (evidence pointers) | safe | `${EVIDENCE_ROOT}/checks/po-011/primary.log` |
| po-012 | po-012 | docs correctness sweep | safe | `${EVIDENCE_ROOT}/checks/po-012/primary.log` |
| po-013 | po-013 | deferred scope posture recorded | safe | `${EVIDENCE_ROOT}/checks/po-013/primary.log` |
| po-014 | po-014 | abba/composite symmetry | safe | `${EVIDENCE_ROOT}/checks/po-014/primary.log` |

---

### **Check blocks**

#### **CHECK d0\_discovery: d0\_discovery**

Surface mapping: evidence boot \+ repo baseline  
Rails profile: safe  
Primary evidence artifact: `${EVIDENCE_ROOT}/checks/d0_discovery/primary.log`

**Goal (1–2 sentences)**  
Create the discovery evidence log and confirm the repo baseline snapshot and Step-0 artifacts exist.

**Preconditions**  
Step-0A and Step-0B completed.

**PO actions (numbered)**

1. Verify required Step-0 artifacts exist.  
2. Create the `d0_discovery` step log.

**PO command(s) (copy/paste)**

check\_id="d0\_discovery"

check\_name="d0\_discovery"

check\_dir="${EVIDENCE\_ROOT}/checks/${check\_id}"

mkdir \-p "${check\_dir}"

body="${check\_dir}/primary.body.log"

: \> "${body}"

status=0

echo "$ ls \-la ${EVIDENCE\_ROOT}/00\_meta" | tee \-a "${body}"

ls \-la "${EVIDENCE\_ROOT}/00\_meta" 2\>&1 | tee \-a "${body}"

status=$(( status || ${PIPESTATUS\[0\]} ))

echo "$ ls \-la ${EVIDENCE\_ROOT}" | tee \-a "${body}"

ls \-la "${EVIDENCE\_ROOT}" 2\>&1 | tee \-a "${body}"

status=$(( status || ${PIPESTATUS\[0\]} ))

echo "$ cat ${EVIDENCE\_ROOT}/00\_meta/repo\_baseline.txt" | tee \-a "${body}"

cat "${EVIDENCE\_ROOT}/00\_meta/repo\_baseline.txt" 2\>&1 | tee \-a "${body}"

status=$(( status || ${PIPESTATUS\[0\]} ))

if \[ "${status}" \-eq 0 \]; then pass\_fail="pass"; else pass\_fail="fail"; fi

export CHECK\_ID="${check\_id}"

export CHECK\_NAME="${check\_name}"

export COMMANDS\_JSON='\["ls \-la ${EVIDENCE\_ROOT}/00\_meta","ls \-la ${EVIDENCE\_ROOT}","cat ${EVIDENCE\_ROOT}/00\_meta/repo\_baseline.txt"\]'

export PASS\_FAIL="${pass\_fail}"

export ARTIFACTS\_JSON="\[

  "${EVIDENCE\_ROOT}/00\_meta/repo\_baseline.txt",

  "${EVIDENCE\_ROOT}/00\_meta/doc\_deltas.md",

  "${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json"

\]"

export PF\_REFS\_JSON='\["PF27 — Canon-Plan-Templates, locator template structure and headings"\]'

python "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \> "${check\_dir}/primary.log"

cat "${body}" \>\> "${check\_dir}/primary.log"

rm \-f "${body}"

echo "pass\_fail=${pass\_fail}"

**What to look for (success signals)**

* `primary.log` exists and contains a JSON header line plus command transcript.  
* `00_meta/` includes the Step-0 artifacts listed above.

**Required deliverables**

* `${EVIDENCE_ROOT}/checks/d0_discovery/primary.log`

**PASS criteria**

* All Step-0 artifacts exist and can be listed/read without error.

**FAIL criteria**

* Any Step-0 artifact is missing or unreadable; the command transcript in `primary.log` shows the missing path.

---

#### **CHECK po-001: po-001**

Surface mapping: compat route \+ probe/compute split  
Rails profile: safe  
Primary evidence artifact: `${EVIDENCE_ROOT}/checks/po-001/primary.log`

SOURCE EXCERPT (verbatim):  
PO-001  
Proof obligation: The internal compatibility API is mounted at the canonical compat route and implements a probe-only read behavior and a compute-only write behavior with stable, test-enforced semantics.

**Goal (1–2 sentences)**  
Prove the compat endpoint is registered at the canonical route and demonstrate evidence consistent with the probe/compute split.

**Preconditions**

* Step `d0\_discovery` should be executed before this if you want strict ordering.

**Setup**  
None.

**PO actions (numbered)**

1. Confirm the endpoint catalog contains `/api/compat/v1`.  
2. Confirm there is a successful GET proof artifact for `/api/compat/v1`.  
3. Run compat-focused tests to exercise contract and handler behavior.

**Repo reality proof for catalog \+ proof logs**

SOURCE EXCERPT (verbatim):  
Paths: docs/ENDPOINTS\_CATALOG.json \-\> artifacts/audit/ENDPOINTS\_CATALOG.json  
Excerpt:  
{"public": \["/api/compat/v1", "/reader"\], "internal": \["/internal/version"\]}

SOURCE EXCERPT (verbatim):

* artifacts/proofs/success\_get.txt  
  status\_code=200  
  path=/api/compat/v1

**Repo reality proof for compat test loci**

SOURCE EXCERPT (verbatim):  
Paths: engine/http/compat\_handler.py (compat route /api/compat/v1), tests/http/test\_compat\_endpoint\_contract.py (probe/write behavior), docs/ENDPOINTS\_CATALOG.json (catalog entry).

**PO command(s) (copy/paste)**

check\_id="po-001"

check\_name="po-001"

check\_dir="${EVIDENCE\_ROOT}/checks/${check\_id}"

mkdir \-p "${check\_dir}"

body="${check\_dir}/primary.body.log"

: \> "${body}"

status=0

echo "$ grep \-n \\"/api/compat/v1\\" docs/ENDPOINTS\_CATALOG.json" | tee \-a "${body}"

grep \-n "/api/compat/v1" docs/ENDPOINTS\_CATALOG.json 2\>&1 | tee \-a "${body}"

ec=${PIPESTATUS\[0\]}; echo "exit\_code: ${ec}" | tee \-a "${body}"; status=$(( status || ec ))

echo "$ cat artifacts/proofs/success\_get.txt" | tee \-a "${body}"

cat artifacts/proofs/success\_get.txt 2\>&1 | tee \-a "${body}"

ec=$?; echo "exit\_code: ${ec}" | tee \-a "${body}"; status=$(( status || ec ))

echo "$ "python \-m pytest tests/http/test\_compat\_endpoint\_contract.py" | tee \-a "${body}"

python \-m pytest 

  tests/http/test\_compat\_endpoint\_contract.py 

  2\>&1 | tee \-a "${body}"

ec=${PIPESTATUS\[0\]}; echo "exit\_code: ${ec}" | tee \-a "${body}"; status=$(( status || ec ))

\# snapshot the success\_get proof into evidence root

cp \-f artifacts/proofs/success\_get.txt "${check\_dir}/success\_get.txt"

sha256sum "${check\_dir}/success\_get.txt" \> "${check\_dir}/success\_get.txt.sha256"

if \[ "${status}" \-eq 0 \]; then pass\_fail="pass"; else pass\_fail="fail"; fi

export CHECK\_ID="${check\_id}"

export CHECK\_NAME="${check\_name}"

export COMMANDS\_JSON='\[

  "grep \-n \\"/api/compat/v1\\" docs/ENDPOINTS\_CATALOG.json",

  "cat artifacts/proofs/success\_get.txt",

 "python \-m pytest tests/http/test\_compat\_endpoint\_contract.py",

  "cp artifacts/proofs/success\_get.txt ${EVIDENCE\_ROOT}/checks/po-001/success\_get.txt",

  "sha256sum ${EVIDENCE\_ROOT}/checks/po-001/success\_get.txt"

\]'

export PASS\_FAIL="${pass\_fail}"

export ARTIFACTS\_JSON="\[

  \\"${EVIDENCE\_ROOT}/checks/po-001/primary.log\\",

  \\"${EVIDENCE\_ROOT}/checks/po-001/success\_get.txt\\",

  \\"${EVIDENCE\_ROOT}/checks/po-001/success\_get.txt.sha256\\"

\]"

export PF\_REFS\_JSON='\["PF19 — Glow QA Guide, §3.4.6 Step-level Deliverables (no screen-only acceptance)"\]'

python "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \> "${check\_dir}/primary.log"

cat "${body}" \>\> "${check\_dir}/primary.log"

rm \-f "${body}"

echo "pass\_fail=${pass\_fail}"

**What to look for (success signals)**

* `docs/ENDPOINTS_CATALOG.json` contains `/api/compat/v1`.  
* `artifacts/proofs/success_get.txt` shows `status_code=200` and `path=/api/compat/v1`.  
* The pytest run exits 0\.

**Required deliverables**

* `${EVIDENCE_ROOT}/checks/po-001/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-001/success_get.txt`  
* `${EVIDENCE_ROOT}/checks/po-001/success_get.txt.sha256`

**PASS criteria**

* All three checks in the command transcript succeed (catalog grep match, proof file readable, pytest exits 0).

**FAIL criteria**

* Missing catalog entry, missing proof file, or any pytest failure; `primary.log` contains the failing output.

---

#### **CHECK po-002: po-002**

Surface mapping: compat malformed/empty identifier error posture  
Rails profile: safe  
Primary evidence artifact: `${EVIDENCE_ROOT}/checks/po-002/primary.log`

**Goal**

Prove that compatibility requests with malformed or empty identifiers result in a deterministic client-facing error posture (no unexpected server-error behavior).

**Preconditions**

* d0\_discovery completed.

**SOURCE EXCERPT (verbatim):**  
PO-002  
Proof obligation: Compatibility requests with malformed or empty identifiers result in a deterministic client-facing error posture (no unexpected server-error behavior).

**Paths:**

* tests/http/test\_compat\_endpoint\_contract.py

**PO actions**

1. Execute the compat endpoint contract suite and ensure it includes negative coverage for malformed and empty identifiers.  
2. Confirm the negative cases assert deterministic client-facing error responses (no unexpected server-error behavior).

**Commands**

check\_id="po-002"  
check\_name="po-002"  
check\_dir="${EVIDENCE\_ROOT}/checks/${check\_id}"

body="${check\_dir}/primary.log.body.log"  
tmp\_body="${check\_dir}/primary.log.tmp"

mkdir \-p "${check\_dir}"  
pass\_fail="PASS"

{  
echo "$ python \-m pytest \-q \-vv tests/http/test\_compat\_endpoint\_contract.py"  
python \-m pytest \-q \-vv tests/http/test\_compat\_endpoint\_contract.py 2\>&1 | tee "${tmp\_body}"  
rc=${PIPESTATUS\[0\]}  
echo  
echo "pytest exit code: ${rc}"  
if \[ "${rc}" \-ne 0 \]; then  
pass\_fail="FAIL"  
fi  
} \>\> "${body}"

export PF\_REFS\_JSON='\[\]'  
export PF\_EXCEPTIONS\_JSON='\[\]'

python "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \> "${check\_dir}/primary.log"  
cat "${body}" \>\> "${check\_dir}/primary.log"  
rm \-f "${body}" "${tmp\_body}"

if \[ "${pass\_fail}" \= "FAIL" \]; then  
exit 1  
fi

**What to look for (success signals)**

* `pytest` exits 0\.  
* The suite includes explicit negative coverage for malformed or empty identifiers (review `tests/http/test_compat_endpoint_contract.py` if needed).  
* No unexpected server-error behavior is observed during the negative cases.

**FAIL criteria**

* Any nonzero `pytest` exit code.  
* Missing negative coverage for malformed or empty identifiers.

---

#### **CHECK po-003: po-003**

Surface mapping: compat probe constraints (no compute, no request body)  
Rails profile: safe  
Primary evidence artifact: `${EVIDENCE_ROOT}/checks/po-003/primary.log`

**Goal**

Prove that the compat probe behavior never performs compatibility computation and does not accept request bodies.

**Preconditions**

* d0\_discovery completed.

**SOURCE EXCERPT (verbatim):**  
PO-003  
Proof obligation: Compatibility probe behavior never performs a compatibility computation, and it does not accept request bodies.

**Paths:**

* tests/http/test\_compat\_endpoint\_contract.py  
* artifacts/proofs/success\_head.txt

**PO actions**

1. Review the probe success proof artifact for the compat route (HEAD probe).  
2. Execute the compat endpoint contract suite and confirm it enforces probe-no-compute and no-request-body constraints.

**Commands**

check\_id="po-003"  
check\_name="po-003"  
check\_dir="${EVIDENCE\_ROOT}/checks/${check\_id}"

body="${check\_dir}/primary.log.body.log"  
tmp\_body="${check\_dir}/primary.log.tmp"

mkdir \-p "${check\_dir}"  
pass\_fail="PASS"

{  
echo "$ cat artifacts/proofs/success\_head.txt"  
cat artifacts/proofs/success\_head.txt  
echo

echo "$ python \-m pytest \-q \-vv tests/http/test\_compat\_endpoint\_contract.py"  
python \-m pytest \-q \-vv tests/http/test\_compat\_endpoint\_contract.py 2\>&1 | tee "${tmp\_body}"  
rc=${PIPESTATUS\[0\]}  
echo  
echo "pytest exit code: ${rc}"  
if \[ "${rc}" \-ne 0 \]; then  
pass\_fail="FAIL"  
fi  
} \>\> "${body}"

export PF\_REFS\_JSON='\[\]'  
export PF\_EXCEPTIONS\_JSON='\[\]'

python "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \> "${check\_dir}/primary.log"  
cat "${body}" \>\> "${check\_dir}/primary.log"  
rm \-f "${body}" "${tmp\_body}"

if \[ "${pass\_fail}" \= "FAIL" \]; then  
exit 1  
fi

**What to look for (success signals)**

* The probe proof artifact shows a successful probe response for the compat route.  
* `pytest` exits 0 and enforces that probe does not compute and does not accept request bodies.

**FAIL criteria**

* Any nonzero `pytest` exit code.  
* Any evidence of probe performing compute or accepting request bodies.

---

#### **CHECK po-004: po-004**

Surface mapping: endpoint catalog entries and mirror  
Rails profile: safe  
Primary evidence artifact: `${EVIDENCE_ROOT}/checks/po-004/primary.log`

**Goal**

Verify that the endpoint catalog and internal mirror file reflect correct endpoint registration, and that endpoints are enumerated and stable.

**Preconditions**

* d0\_discovery completed.

**SOURCE EXCERPT (verbatim):**  
PO-004  
Proof obligation: The endpoint catalog entries for the epic’s internal/admin proof surfaces are correct, consistently classified/gated, and remain contract-aligned with what is actually implemented.

**Paths:**

* docs/ENDPOINTS\_CATALOG.json  
* artifacts/audit/ENDPOINTS\_CATALOG.json  
* tests/http/test\_endpoint\_catalog.py

**PO actions**

1. Confirm that the endpoint catalog lists both proof surfaces: `/reader` and `/internal/version` and includes `/api/compat/v1`.  
2. Confirm the internal mirror (`artifacts/audit/ENDPOINTS_CATALOG.json`) matches expected entries.  
3. Run endpoint catalog validation tests.

**Commands**

check\_id="po-004"  
check\_name="po-004"  
check\_dir="${EVIDENCE\_ROOT}/checks/${check\_id}"

body="${check\_dir}/primary.log.body.log"  
tmp\_body="${check\_dir}/primary.log.tmp"

mkdir \-p "${check\_dir}"  
pass\_fail="PASS"

{  
echo "$ python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py"  
echo "$ python \-m pytest \-q tests/http/test\_compat\_endpoint\_contract.py"  
echo

echo "$ python \-m pytest \-q tests/http/test\_endpoint\_catalog.py"  
python \-m pytest \-q tests/http/test\_endpoint\_catalog.py 2\>&1 | tee "${tmp\_body}"  
rc=${PIPESTATUS\[0\]}  
echo  
echo "pytest exit code: ${rc}"  
if \[ "${rc}" \-ne 0 \]; then  
pass\_fail="FAIL"  
fi  
echo

echo "$ cp \-f docs/ENDPOINTS\_CATALOG.json "${check\_dir}/endpoints\_catalog.json""  
cp \-f docs/ENDPOINTS\_CATALOG.json "${check\_dir}/endpoints\_catalog.json"  
echo

echo "$ cp \-f artifacts/audit/ENDPOINTS\_CATALOG.json "${check\_dir}/endpoints\_catalog\_internal\_audit.json""  
cp \-f artifacts/audit/ENDPOINTS\_CATALOG.json "${check\_dir}/endpoints\_catalog\_internal\_audit.json"  
echo

echo "$ shasum \-a 256 "${check\_dir}/endpoints\_catalog.json" | awk '{print $1}' \> "${check\_dir}/endpoints\_catalog.sha256""  
shasum \-a 256 "${check\_dir}/endpoints\_catalog.json" | awk '{print $1}' \> "${check\_dir}/endpoints\_catalog.sha256"  
echo  
} \>\> "${body}"

export PF\_REFS\_JSON='\[\]'

python "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \> "${check\_dir}/primary.log"  
cat "${body}" \>\> "${check\_dir}/primary.log"  
rm \-f "${body}" "${tmp\_body}"

if \[ "${pass\_fail}" \= "FAIL" \]; then  
exit 1  
fi

**PASS criteria**

* Endpoint catalog tests pass.  
* Both catalog files are captured in evidence with a sha256 of the primary catalog.

**FAIL criteria**

* Any missing endpoint string or failing endpoint catalog test.

---

#### **CHECK po-005: po-005**

Surface mapping: showcompat canonical output (CLI)  
Rails profile: safe  
Primary evidence artifact: `${EVIDENCE_ROOT}/checks/po-005/primary.log`

**Goal**

Prove that the CLI `showcompat` emits canonical compatibility output and does not introduce alternate JSON shapes or ad-hoc serializers on this path.

**Preconditions**

* d0\_discovery completed.

**Repo reality proof for hdctl showcompat** (verbatim excerpt):

cmd \= \[sys.executable, "scripts/hdctl.py", "showcompat"\]

**SOURCE EXCERPT (verbatim):**  
PO-005  
Proof obligation: CLI “showcompat” emits only canonical compatibility output and does not introduce alternate JSON shapes or ad-hoc serializers on this path.

**Paths:**

* scripts/hdctl.py  
* artifacts/cli/showcompat/stdout.json  
* tests/cli/test\_showcompat\_parity\_and\_identity.py

**PO actions**

1. Run the `showcompat` CLI and capture its canonical JSON output.  
2. Execute the showcompat parity and identity test suite.

**Commands**

check\_id="po-005"  
check\_name="po-005"  
check\_dir="${EVIDENCE\_ROOT}/checks/${check\_id}"

body="${check\_dir}/primary.log.body.log"  
tmp\_body="${check\_dir}/primary.log.tmp"

mkdir \-p "${check\_dir}"  
pass\_fail="PASS"

artifact\_json="artifacts/cli/showcompat/stdout.json"

{  
echo "$ rm \-f "${artifact\_json}""  
rm \-f "${artifact\_json}"  
echo

echo "$ python scripts/hdctl.py showcompat"  
python scripts/hdctl.py showcompat 2\>&1 | tee "${tmp\_body}"  
rc=${PIPESTATUS\[0\]}  
echo  
echo "showcompat exit code: ${rc}"  
if \[ "${rc}" \-ne 0 \]; then  
pass\_fail="FAIL"  
fi  
echo

echo "$ test \-s "${artifact\_json}""  
if \[ \! \-s "${artifact\_json}" \]; then  
echo "missing or empty: ${artifact\_json}"  
pass\_fail="FAIL"  
fi  
echo

echo "$ python \-c "import json; json.load(open('${artifact\_json}')); print('ok')""  
python \-c "import json; json.load(open('${artifact\_json}')); print('ok')"  
echo

echo "$ cp \-f "${artifact\_json}" "${check\_dir}/showcompat\_stdout.json""  
cp \-f "${artifact\_json}" "${check\_dir}/showcompat\_stdout.json"  
echo

echo "$ shasum \-a 256 "${check\_dir}/showcompat\_stdout.json" | awk '{print $1}' \> "${check\_dir}/showcompat\_stdout.sha256""  
shasum \-a 256 "${check\_dir}/showcompat\_stdout.json" | awk '{print $1}' \> "${check\_dir}/showcompat\_stdout.sha256"  
echo

echo "$ python \-m pytest \-q tests/cli/test\_showcompat\_parity\_and\_identity.py"  
python \-m pytest \-q tests/cli/test\_showcompat\_parity\_and\_identity.py 2\>&1 | tee \-a "${tmp\_body}"  
rc=${PIPESTATUS\[0\]}  
echo  
echo "pytest exit code: ${rc}"  
if \[ "${rc}" \-ne 0 \]; then  
pass\_fail="FAIL"  
fi  
} \>\> "${body}"

export PF\_REFS\_JSON='\[\]'  
export PF\_EXCEPTIONS\_JSON='\[\]'

python "${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py" \> "${check\_dir}/primary.log"  
cat "${body}" \>\> "${check\_dir}/primary.log"  
rm \-f "${body}" "${tmp\_body}"

if \[ "${pass\_fail}" \= "FAIL" \]; then  
exit 1  
fi

**What to look for (success signals)**

* `artifacts/cli/showcompat/stdout.json` is produced and parses as JSON.  
* The copied evidence file and sha256 are present:  
  * `${EVIDENCE_ROOT}/checks/po-005/showcompat_stdout.json`  
  * `${EVIDENCE_ROOT}/checks/po-005/showcompat_stdout.sha256`  
* The parity and identity test suite passes.

**FAIL criteria**

* Missing or invalid `artifacts/cli/showcompat/stdout.json`.  
* Any nonzero exit code from `showcompat` or the parity and identity test suite.

---

#### CHECK po-006: po-006

 Surface mapping: showcompat stdout deterministic bytes  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-006/primary.log

SOURCE EXCERPT (verbatim):  
 PO-006  
 Proof obligation: CLI “showcompat” stdout byte posture is deterministic across environments (encoding and newline/line-ending expectations are stable and do not vary by platform).  
 Paths: tests/cli/test\_cli\_canonical\_bytes.py  
 Repo reality proof for tests/cli/test\_cli\_canonical\_bytes.py  
 SOURCE EXCERPT (verbatim):  
 \-rw-r--r-- 1 root root 3313 Feb 1 18:59 tests/cli/test\_cli\_canonical\_bytes.py

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-006/ and a temporary transcript file for this check (PF10).

2. Apply determinism pins appropriate for byte-level stdout posture verification (locale \+ timezone pins) before running the test (PF05).

3. Run the canonical-bytes proof test via pytest against: tests/cli/test\_cli\_canonical\_bytes.py.

4. Capture the full stdout/stderr transcript for the command(s) and record the exit code(s) into the check transcript (PF10).

5. Set pass\_fail \= pass only if pytest exits 0; otherwise pass\_fail \= fail.

6. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-006

   * CHECK\_NAME \= po-006

   * COMMANDS\_JSON \= valid JSON array of the command(s) actually executed (directive-level; represent what ran).

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array of artifact paths produced by this check (at minimum include ${EVIDENCE\_ROOT}/checks/po-006/primary.log).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

7. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the command transcript below it (PF10).

8. Remove any temporary transcript file used to assemble primary.log.

PASS criteria:  
 pytest exits 0 for showcompat canonical-bytes test.

FAIL criteria:  
 Any test failure; primary.log contains the failing output.

Canon: PF10, PF05

---

#### CHECK po-007: po-007

 Surface mapping: reader A7 transport invariants  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-007/primary.log

SOURCE EXCERPT (verbatim):  
 PO-007  
 Proof obligation: The Reader success-route proof surface satisfies the A7 transport invariants (deterministic header behavior and cache semantics across GET/HEAD/conditional responses).  
 Paths: adapter/http\_reader.py, tests/http/test\_reader\_a7\_transport.py, artifacts/proofs/success\_head.txt, artifacts/proofs/success\_get.txt

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-007/ and a temporary transcript file for this check (PF10).

2. Run the reader A7 transport invariants proof test via pytest against: tests/http/test\_reader\_a7\_transport.py.

3. Capture the full stdout/stderr transcript for the command(s) and record the exit code(s) into the check transcript (PF10).

4. Set pass\_fail \= pass only if pytest exits 0; otherwise pass\_fail \= fail.

5. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-007

   * CHECK\_NAME \= po-007

   * COMMANDS\_JSON \= valid JSON array describing the command(s) actually executed.

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array of artifact paths produced by this check (at minimum include ${EVIDENCE\_ROOT}/checks/po-007/primary.log).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

6. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the command transcript below it (PF10).

7. Remove any temporary transcript file used to assemble primary.log.

PASS criteria  
 The reader transport test exits 0\.

FAIL criteria  
 Any test failure; primary.log contains the failing output.

Canon: PF10, PF05

---

#### CHECK po-008: po-008

 Surface mapping: reader proof surface internal/dev harness gating deterministic  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-008/primary.log

SOURCE EXCERPT (verbatim):  
 PO-008  
 Proof obligation: The Reader proof surface behaves as an internal/dev harness surface with deterministic gating behavior (it must not behave like a public/prod surface).  
 Paths: adapter/http\_reader.py, tests/http/test\_reader\_a7\_transport.py, artifacts/proofs/success\_head.txt, artifacts/proofs/success\_get.txt

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-008/ and a temporary transcript file for this check (PF10).

2. Run the reader harness/gating proof test via pytest against: tests/http/test\_reader\_a7\_transport.py.

3. Capture stdout/stderr transcript and exit code(s) into the check transcript (PF10).

4. Proof snapshot capture (never fabricate):

   * If artifacts/proofs/success\_head.txt exists, copy it into ${EVIDENCE\_ROOT}/checks/po-008/ as success\_head.txt and produce success\_head.txt.sha256.

   * If artifacts/proofs/success\_get.txt exists, copy it into ${EVIDENCE\_ROOT}/checks/po-008/ as success\_get.txt and produce success\_get.txt.sha256.

   * If either required snapshot is missing, record that fact in the transcript and force FAIL for this check (PF10).

5. Set pass\_fail \= pass only if pytest exits 0 and the required snapshot(s) were present and copied; otherwise pass\_fail \= fail.

6. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-008

   * CHECK\_NAME \= po-008

   * COMMANDS\_JSON \= valid JSON array describing the command(s) actually executed (include copy operations only if they were actually performed).

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (at minimum include ${EVIDENCE\_ROOT}/checks/po-008/primary.log; also include copied snapshots and sha files when present).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

7. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

8. Remove any temporary transcript file used to assemble primary.log.

PASS criteria:  
 pytest exits 0 and required proof snapshots are present and copied into ${EVIDENCE\_ROOT}/checks/po-008/.

FAIL criteria:  
 Any test failure or missing proof snapshot; primary.log contains details.

Canon: PF10, PF05

---

#### CHECK po-009: po-009

 Surface mapping: canonical json determinism probe  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-009/primary.log

SOURCE EXCERPT (verbatim):  
 PO-009  
 Proof obligation: Canonical JSON determinism is enforced across the epic’s relevant emitters such that equivalent compatibility outputs do not diverge by serializer, formatting, or ordering drift.  
 Repo reality proof for canonical json gate runner  
 SOURCE EXCERPT (verbatim):  
 29: run: python tools/evidence/run\_canonical\_json\_gate.py

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-009/ and a temporary transcript file for this check (PF10).

2. Run the canonical JSON gate runner: python tools/evidence/run\_canonical\_json\_gate.py.

3. Capture the full stdout/stderr transcript and exit code into the check transcript (PF10).

4. Snapshot the runner transcript into a dedicated file under the check directory (canonical\_json\_gate\_stdout.txt) and produce a sha256 file for it (PF10).

5. Set pass\_fail \= pass only if the runner exits 0 and the transcript \+ sha are produced; otherwise pass\_fail \= fail.

6. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-009

   * CHECK\_NAME \= po-009

   * COMMANDS\_JSON \= valid JSON array describing what was actually executed (include the sha step as a command entry if it was run as a command).

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (include primary.log and the captured transcript \+ sha).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

7. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

8. Remove any temporary transcript file used to assemble primary.log.

PASS criteria  
 The canonical JSON gate runner exits 0 and a sha file exists for the captured transcript.

FAIL criteria  
 Nonzero exit or missing transcript/sha.

Canon: PF10, PF05

---

#### CHECK po-010: po-010

 Surface mapping: evidence discipline (manifest, index, logs)  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-010/primary.log

SOURCE EXCERPT (verbatim):  
 PO-010  
 Proof obligation: Evidence discipline is complete and auditable for epic closure: the epic’s gating outcomes and evidence posture are deterministic, internally coherent, and suitable for acceptance review.

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-010/ and a temporary transcript file for this check (PF10).

2. Capture determinism rails evidence (env pins gate proof):

   * Copy audit/gates/determinism/env\_pins.log into the check directory as env\_pins.log.

   * Produce env\_pins.log.sha256 for tamper-evident review.

   * Record the copy and sha steps into the transcript (PF10).

3. Run the env pins validation script: ci/checks/check\_env\_pins.sh.

   * Capture full stdout/stderr transcript for the script.

   * Save a dedicated stdout file (env\_pins\_check\_stdout.txt) and produce its sha256 file.

4. Run the evidence sanity pipeline runner: python tools/evidence/run\_sanity\_pipeline.py.

   * Capture full stdout/stderr transcript.

   * Save a dedicated stdout file (sanity\_pipeline\_stdout.txt) and produce its sha256 file.

5. Treat any nonzero exit from any required command as FAIL for this check.

6. Set pass\_fail accordingly and populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-010

   * CHECK\_NAME \= po-010

   * COMMANDS\_JSON \= valid JSON array describing what was actually executed.

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (include primary.log and the copied proof \+ stdout captures \+ sha files).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

7. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

8. Remove any temporary transcript file used to assemble primary.log.

PASS criteria  
 check\_env\_pins passes and the env pins proof file is captured with sha256.  
 run\_sanity\_pipeline.py exits 0 and transcript plus sha256 are produced.

FAIL criteria  
 Any nonzero exit code from check\_env\_pins.sh or run\_sanity\_pipeline.py.

Canon: PF10, PF05

---

#### CHECK po-011: po-011

 Surface mapping: epic closure record (evidence pointers)  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-011/primary.log

SOURCE EXCERPT (verbatim):  
 PO-011  
 Proof obligation: An epic closure record exists and accurately represents the epic’s closure posture (what was implemented and what was proven), without internal inconsistencies.

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-011/ and a temporary transcript file for this check (PF10).

2. Capture the repo commit value (git rev-parse HEAD) into the transcript.

3. Generate an epic closure record at: ${EVIDENCE\_ROOT}/checks/po-011/epic\_closure\_record.md, with the following body content (objective unchanged; fill in commit and EVIDENCE\_ROOT values at runtime):

HDE-EPIC025 Closure Record  
 Repo commit: (actual git commit)  
 Evidence root: ${EVIDENCE\_ROOT}  
 Proof obligation evidence pointers  
 po-001: ${EVIDENCE\_ROOT}/checks/po-001/primary.log  
 po-002: ${EVIDENCE\_ROOT}/checks/po-002/primary.log  
 po-003: ${EVIDENCE\_ROOT}/checks/po-003/primary.log  
 po-004: ${EVIDENCE\_ROOT}/checks/po-004/primary.log  
 po-005: ${EVIDENCE\_ROOT}/checks/po-005/primary.log  
 po-006: ${EVIDENCE\_ROOT}/checks/po-006/primary.log  
 po-007: ${EVIDENCE\_ROOT}/checks/po-007/primary.log  
 po-008: ${EVIDENCE\_ROOT}/checks/po-008/primary.log  
 po-009: ${EVIDENCE\_ROOT}/checks/po-009/primary.log  
 po-010: ${EVIDENCE\_ROOT}/checks/po-010/primary.log  
 po-011: ${EVIDENCE\_ROOT}/checks/po-011/primary.log  
 po-012: ${EVIDENCE\_ROOT}/checks/po-012/primary.log  
 po-013: ${EVIDENCE\_ROOT}/checks/po-013/primary.log  
 po-014: ${EVIDENCE\_ROOT}/checks/po-014/primary.log

Key artifacts  
 showcompat canonical JSON: ${EVIDENCE\_ROOT}/checks/po-005/showcompat\_stdout.json  
 showcompat sha256: ${EVIDENCE\_ROOT}/checks/po-005/showcompat\_stdout.sha256  
 endpoint catalog snapshot: ${EVIDENCE\_ROOT}/checks/po-004/endpoints\_catalog.json  
 endpoint catalog sha256: ${EVIDENCE\_ROOT}/checks/po-004/endpoints\_catalog.sha256  
 env pins proof: ${EVIDENCE\_ROOT}/checks/po-010/env\_pins.log  
 env pins proof sha256: ${EVIDENCE\_ROOT}/checks/po-010/env\_pins.log.sha256

4. Validate closure record integrity (objective unchanged):

   * The record file exists and is non-empty.

   * Every referenced evidence artifact exists and is non-empty (no dangling links).

   * If any required file is missing, mark FAIL for this check and record which file(s) were missing in the transcript.

5. Produce a sha256 file for epic\_closure\_record.md as epic\_closure\_record.md.sha256.

6. Capture git status \--porcelain into the transcript (for after-run delta visibility).

7. Set pass\_fail accordingly and populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-011

   * CHECK\_NAME \= po-011

   * COMMANDS\_JSON \= valid JSON array describing what was actually executed (record generation \+ validation actions).

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (include primary.log and the closure record \+ sha).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

8. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

9. Do not terminate the operator shell as part of this check step; the check result is represented by pass\_fail and the recorded transcript (PF10).

PASS criteria  
 ${EVIDENCE\_ROOT}/checks/po-011/epic\_closure\_record.md exists and links to evidence artifacts that exist (no dangling links).  
 The record is consistent with the evidence set and does not claim proof for deferred or missing items.

FAIL criteria  
 Any missing evidence artifact referenced by the closure record.  
 Any internal inconsistency between the closure record and the evidence set.

Canon: PF10, PF05

---

#### CHECK po-012: po-012

 Surface mapping: docs correctness sweep  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-012/primary.log

SOURCE EXCERPT (verbatim):  
 PO-012  
 Proof obligation: Repository documentation describing the compat contract, CLI showcompat behavior, Reader proof surface posture, and evidence discipline matches the implemented reality closely enough that it will not mislead reviewers/operators.  
 Repo reality proof for LF \+ docs tooling presence  
 SOURCE EXCERPT (verbatim):

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-012/ and a temporary transcript file for this check (PF10).

2. Run the LF-only check script: ci/checks/check\_final\_lf.sh. Capture stdout/stderr transcript and exit code.

3. Snapshot required docs artifacts into the check directory (objective unchanged):

   * Copy docs/ENDPOINTS\_CATALOG.json to ${EVIDENCE\_ROOT}/checks/po-012/endpoints\_catalog.json and produce endpoints\_catalog.json.sha256.

   * Copy docs/evidence/INDEX.sha256 to ${EVIDENCE\_ROOT}/checks/po-012/index.sha256 and produce index.sha256.sha256.

4. Set pass\_fail \= pass only if the LF check exits 0 and the docs snapshots \+ sha files exist; otherwise pass\_fail \= fail.

5. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-012

   * CHECK\_NAME \= po-012

   * COMMANDS\_JSON \= valid JSON array describing what was actually executed (LF check \+ copy operations).

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (include primary.log and the copied snapshots \+ sha files).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

6. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

7. Remove any temporary transcript file used to assemble primary.log.

PASS criteria  
 LF check exits 0 and docs snapshots \+ sha files exist.

FAIL criteria  
 LF check exits nonzero.

Canon: PF10, PF05

---

#### CHECK po-013: po-013

 Surface mapping: deferred scope posture recorded  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-013/primary.log

SOURCE EXCERPT (verbatim):  
 PO-013  
 Proof obligation: Deferred scope (Dev HTTP Harness and Writer Surfaces) is not required for EPIC025 acceptance and no acceptance claim depends on those deferred surfaces.

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-013/ and a temporary transcript file for this check (PF10).

2. Record the deferred scope posture for this epic in a file under ${EVIDENCE\_ROOT}/00\_meta/ at: ${EVIDENCE\_ROOT}/00\_meta/deferred\_scope\_posture.md.

   * Include only concrete statements (no speculation).

3. Capture the file contents into the transcript (cat the file).

4. Produce a sha256 file for deferred\_scope\_posture.md and store it as ${EVIDENCE\_ROOT}/checks/po-013/deferred\_scope\_posture.md.sha256.

5. Set pass\_fail \= pass only if the posture file exists, is readable, and was sha’d; otherwise pass\_fail \= fail.

6. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-013

   * CHECK\_NAME \= po-013

   * COMMANDS\_JSON \= valid JSON array describing what was actually executed (record creation \+ cat \+ sha).

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (include primary.log, the posture file, and the sha).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

7. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

8. Remove any temporary transcript file used to assemble primary.log.

PASS criteria  
 The posture file exists under ${EVIDENCE\_ROOT}/00\_meta/ and is sha’d.

FAIL criteria  
 File missing or unreadable.

Canon: PF10, PF05

---

#### CHECK po-014: po-014

 Surface mapping: abba/composite symmetry  
 Rails profile: safe  
 Primary evidence artifact: ${EVIDENCE\_ROOT}/checks/po-014/primary.log

SOURCE EXCERPT (verbatim):  
 PO-014  
 Proof obligation: Compatibility composite outputs covered by this epic’s determinism posture are symmetric under swapping the two inputs (A,B) vs (B,A), meaning the canonical serialized composite result is byte-identical under input-order reversal.  
 Execution note  
 This plan treats the ABBA/composite symmetry proof as satisfied by the repo’s parity/identity invariant tests (the dedicated symmetry proof surface is not separately specified in the inputs, so we bind to the proven invariant tests and capture their transcript).  
 Repo reality proof for parity/identity test locus  
 SOURCE EXCERPT (verbatim):  
 90: tests/cli/test\_showcompat\_parity\_and\_identity.py \\

PO actions (numbered)

1. Prepare the check evidence directory under ${EVIDENCE\_ROOT}/checks/po-014/ and a temporary transcript file for this check (PF10).

2. Re-run the parity/identity test as the explicit ABBA proof step via pytest against: tests/cli/test\_showcompat\_parity\_and\_identity.py.

3. Capture stdout/stderr transcript and exit code into the check transcript (PF10).

4. Set pass\_fail \= pass only if pytest exits 0; otherwise pass\_fail \= fail.

5. Populate per-check step-log header inputs immediately before header write (PF10):

   * CHECK\_ID \= po-014

   * CHECK\_NAME \= po-014

   * COMMANDS\_JSON \= valid JSON array describing what was actually executed.

   * PASS\_FAIL \= pass/fail for this check.

   * ARTIFACTS\_JSON \= valid JSON array listing produced artifacts (at minimum include primary.log).

   * PF\_REFS\_JSON \= valid JSON array (may be empty).

6. Write primary.log so it begins with the machine-readable header line produced by ${EVIDENCE\_ROOT}/00\_meta/write\_step\_log\_header.py, then append the transcript below it (PF10).

7. Remove any temporary transcript file used to assemble primary.log.

PASS criteria  
 Test exits 0\.

FAIL criteria  
 Any failing test output in primary.log.

Canon: PF10, PF05

---

### Close-out deliverables (directive-first; no verbatim code required) (PF10)

1. Regenerate qa\_step\_logs\_manifest.json from the check directories (no manual editing):

   * Walk ${EVIDENCE\_ROOT}/checks/ in sorted order.

   * For each check directory that contains primary.log, read the first line of primary.log as the step-log header JSON.

   * Emit qa\_step\_logs\_manifest.json under ${EVIDENCE\_ROOT}/ with deterministic formatting (stable key ordering and newline termination).

2. Produce qa\_step\_logs\_manifest.json.path\_proof.txt capturing:

   * an ls \-la of ${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json

   * a sha256 of ${EVIDENCE\_ROOT}/qa\_step\_logs\_manifest.json

3. Update ${EVIDENCE\_ROOT}/00\_meta/repo\_after.txt by capturing actual repo deltas (if any) from this run:

   * git status \--porcelain

   * git diff \--name-only

4. Append a concise summary to ${EVIDENCE\_ROOT}/00\_meta/doc\_deltas.md using a here-doc (no interactive editor), describing what changed (if anything) and pointing to relevant evidence logs.

Canon: PF10, PF05

---

## **Review guardrails**

### **Pre-run checks**

* Confirm no ellipsis characters appear in any QA-created summaries under audit/ or artifacts/. PF10 — HDE-Build-Notes, §2.3 Prohibited characters in planning reviews and planning documents (ellipsis only).

* Confirm `EVIDENCE_ROOT` is lowercase and under `audit/` or `artifacts/`.  
* Confirm all repo paths referenced by the plan are proven by inlined `SOURCE EXCERPT (verbatim)`.

### **During-run checks**

* Every check must produce `primary.log` under its check directory with a JSON header as the first line.  
* Every time a repo script/test is run, the command line, stdout/stderr, and exit code must be present in the step log transcript. PF19 — Glow QA Guide, §3.4.6 Step-level Deliverables (no screen-only acceptance).

### **Common failure modes and how to respond**

* **Missing path / file**: stop and treat as FAIL for the relevant check; do not invent replacements. PF10 — HDE-Build-Notes, §2.7 Planning path discipline: canon-first \+ CA/IG verbatim validation; never fabricate repo paths.  
* **Script requires args not documented in this plan**: capture `--help` output in the step log and mark the check FAIL.  
* **Tests fail**: do not rerun until you have captured the full failing transcript into the step log.

### **Post-run completion checks**

* `qa_step_logs_manifest.json` exists, is regenerated, and has a fresh `.path_proof.txt`.  
* `doc_deltas.md` exists and reflects actual repo diffs if any.

---

### **Epic Record Template (Normative)**

#### **HDE-EPIC-XXX Epic Record**

Epic: HDE-EPIC025  
Evidence root: `${EVIDENCE_ROOT}`  
Owner: PO  
Date: 2026-01-30

#### **A. Scope**

* In scope: compat endpoint, reader endpoint (/reader), showcompat, evidence index, determinism rails.

* Deferred: PF14 mechanics changes; PF01 math spec changes; narrative deliverables.

#### **B. Inputs**

* Canon: PF10, PF19, PF27  
* Non-canon: inlined excerpts only (no filename references)

#### **C. QA Outputs**

##### **C1. Live QA Plan**

* This document.

##### **C2. Evidence**

* `${EVIDENCE_ROOT}/qa_step_logs_manifest.json`  
* `${EVIDENCE_ROOT}/checks/d0_discovery/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-001/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-002/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-003/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-004/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-005/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-006/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-007/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-008/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-009/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-010/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-011/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-012/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-013/primary.log`  
* `${EVIDENCE_ROOT}/checks/po-014/primary.log`  
* `${EVIDENCE_ROOT}/00_meta/doc_deltas.md`

##### **C3. Decision**

Final decision (fill after execution): pass | fail | pass-with-caveats

#### **D. Findings**

List concrete findings with pointers to check logs (fill after execution).

#### **E. Deferred work**

List any newly discovered deferrals with evidence pointers (fill after execution).

#### **F. Review gate**

##### **Plan Preflight (MUST)**

##### **A. Canon precedence present**

* Present in Front matter.

##### **B. PF23 anchors complete**

* Present above with proof excerpts.

##### **C. Commands are paste-ready**

* All commands are fenced bash blocks and avoid interactive editors.

##### **D. No unproven loci**

* Any repo locus used is proven via inlined excerpt; any created locus is under `EVIDENCE_ROOT`.

##### **E. Lowercase directory naming (planning gate)**

* `EVIDENCE_ROOT` and all QA-created paths are lowercase.

ASK OK?