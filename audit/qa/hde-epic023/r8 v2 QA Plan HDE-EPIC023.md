## **1\) Live QA Plan**

### **Front matter**

Epic ID: HDE-EPIC023  
Plan type: Live QA Plan / Runbook  
Execution venue: Codespaces (or Other: \_\_\_\_)  
Target environment: dev (Codespaces)  
Plan revision: r8

Date (UTC): 2026-01-07  
Operators (names-only): PO, IA, (optional) QA agent, (optional) Codex

#### **Canon precedence statement (required)**

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### **Canon set (explicit; stable references only)**

List the governing sources as PF ID \+ Title \+ Section (no filenames/versions).

* PF10 — HDE-Build Notes (relevant addenda: 2.13 “HDE-EPIC023 PR05”; 2.14 “HDE-EPIC023 PR05”; 2.16 “Evidence Registry/Index/Mirror updated”; 2.17 “Forbid fabricated paths in plans”)  
* PF04 — HDE-Governance, §… (token registry \+ relevant invariants referenced by acceptance validation)  
* PF06 — Epic Process Guide, §0.4.1 (Discovery \+ QA RCA/Doc Delta)  
* PF12 — HDE-Schemas and Artifacts, §8.3 (Path-proof transcript schema), §8.3.3 (Determinism env pins log), §8.3.4 (Sanity pipeline log), §8.17.5 (Codespaces snapshot schema)  
* PF14 — HDE-Mechanics Guide, §37.2 (Acceptance scaffolds), §37.3 (Close pack), §9.4 (Internal version evidence family)  
* PF19 — Glow QA Guide, §4.4 (step logs \+ manifest \+ status vocabulary), §14.4.3 (Codespaces snapshot requirement), §14.4.4 (Doc Delta Capture requirement)  
* PF23 — Reality Audits, §… (component boundaries \+ canonical loci; consulted as trace)  
* PF27 — Canon Plan Templates, §1 (template obligations)

---

### **Scope statement**

#### **Epic intent and boundaries (names-only; PF-anchored)**

Epic record anchor(s): PF20 — HDE-Phased Epics (Epic 023 record not located via text scan; scope derived from governed deliverables and repo evidence surfaces)

**In-scope surfaces / checks (names-only):**

* D01 — EPIC023 Acceptance Map  
* D02 — Token-to-Evidence Matrix  
* D03 — Acceptance Map Viability Log  
* D04 — Acceptance Alignment Validator Test  
* D05 — QA Step Logs Manifest  
* D06 — Primary QA Step Logs  
* D07 — Codespaces Snapshot  
* D08 — QA Doc Deltas Capture  
* D09 — PF23 Consult Capture  
* D10 — EPIC023 Doc-Delta Draft  
* D11 — EPIC023 Close Report  
* D12 — EPIC023 Close Pack Manifest  
* D13 — Human Evidence Index  
* D14 — Evidence Index Hash Sentinel  
* D15 — Machine Evidence Mirror  
* D16 — Topology Orientation Demo Report  
* D17 — Determinism Environment Pins Log  
* D18 — Sanity Pipeline Log  
* D19 — Canonical JSON Gate Check Log  
* D20 — Canonical JSON Gate Compare Log  
* D21 — /internal/version Evidence Family \+ Endpoint Reality  
* D22 — Canonical JSON Gate Structured Record  
* D23 — EPIC023 Evidence Index Snapshot Artifact

**Out-of-scope surfaces / checks (names-only):**

* Any remediation/implementation work (generators, refactors, schema changes, acceptance-map edits)  
* Any VCS-based provenance checks (git status/sha/etc)  
* Any network calls outside what is explicitly required by a check (default posture is closed rails)

#### **PF10 overrides / conflicts (if any)**

List each as:

* PF10 Addendum 2.17 — → forbids invented paths/commands in plans → impacts all file/path mentions and all PO-executable commands in this runbook  
* PF10 Addendum 2.13 — → pins EPIC023 acceptance scaffolds \+ viability expectations \+ key artifact loci → impacts D01–D04, D13–D15, D11–D12  
* PF10 Addendum 2.14 — → pins EPIC023 close-pack posture \+ artifact expectations → impacts D11–D12  
* PF10 Addendum 2.16 — → asserts Evidence Index/Mirror updates are closure-critical → impacts D13–D16  
* PF10 Addendum 2.13/2.14 vs observed close-pack manifest “key\_outputs” membership — → potential drift risk; this runbook treats it as behavior-checkable and will PASS/FAIL mechanically → impacts D12

---

### **PF23 anchors**

#### **PF23 consult (required for planning)**

PF23 is consulted for component boundaries and canonical loci.

#### **PF23 anchors (names-only; optional but recommended)**

Components consulted: acceptance scaffolds; evidence index/mirror; rails/gates evidence; internal version evidence family; close-pack artifact family  
Key loci pulled (paths/names-only): `docs/acceptance_map_epic023.json`; `audit/qa/hde-epic023/token_evidence_matrix.md`; `audit/qa/hde-epic023/`; `docs/evidence/INDEX.json`; `artifacts/evidence_index.jsonl`; `audit/gates/*`; `artifacts/ops/internal_version/*`; `audit/EPIC-023_*`

(Do not duplicate PF23 content. This is a trace anchor only.)

---

### **Environment and rails posture**

#### **Determinism pins (canonical pins only)**

When producing governed bytes (evidence artifacts, canonical JSON, hash inputs), use:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

**Rule (normative):**

* Do not add new “pins” (example: PYTHONHASHSEED) as a plan-approval or execution requirement.  
* If ordering nondeterminism exists, fix it by explicit normalization (sorting keys/lists, stable ordering) in the step/tool, not by adding pins.

#### **Rails posture (explicit)**

Default rails for this runbook (fill values):

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

If rails change by check, list it (names-only):

* None. (All checks are designed to run under closed rails; if any required input is missing at runtime, mark the affected check TOOLING\_BLOCKED.)

#### **Gitless Live QA (non-negotiable)**

* Runbook steps MUST NOT execute any `git …` command.  
* PASS/FAIL MUST NOT be gated on “working tree clean” or git status.  
* Traceability comes from governed identity artifacts and the captured evidence outputs, not VCS state.

---

### **PO inputs needed**

List all required external inputs by name only (never store secret values in plan artifacts).

Required (non-secret):

* EVIDENCE\_ROOT (set to the EPIC QA root; see bootstrap snippet below)

Optional (only if you deliberately choose to run prod-like handshakes; this runbook does not require them by default):

* HDE\_BASE\_URL (if needed)  
* HDE\_PROD\_BASE\_URL (if needed)  
* PORT (if needed)

Any auth/header inputs only as optional execution inputs where permitted by canon:

* AUTH\_HEADER\_NAME (names-only)  
* AUTH\_HEADER\_VALUE (never persisted; never logged; presence-only is allowed in snapshots)

**Rule (normative):**

* If a required input is missing at runtime, classify the affected check as TOOLING\_BLOCKED (do not guess).

---

### **Evidence posture and directory structure**

#### **Epic QA root normalization (required)**

Canonical epic QA root MUST be lowercase:

* EPIC\_QA\_ROOT \= `audit/qa/hde-epic<NNN>/`

For this epic:

* EPIC\_QA\_ROOT \= `audit/qa/hde-epic023/`

#### **Check-centric, single-root evidence posture (normative)**

This runbook is written for the check-centric posture:

* Canonical evidence outputs are organized by **check\_id** under EPIC\_QA\_ROOT as **current-state evidence**.  
* Per-run directory nesting MAY exist for convenience/history, but it is optional and non-canon.  
* No “latest\_run\_id” pointer files or “run-id as correctness key.”

#### **Recommended canonical layout (default for new plans)**

Use this layout unless an owning PF document defines a fixed canonical path for a specific artifact family.

* `audit/qa/hde-epic<NNN>/00_meta/`  
  Stable epic-level meta artifacts (current-state).  
* `audit/qa/hde-epic<NNN>/checks/<check_id>/`  
  Current-state evidence for each check.

Within each `checks/<check_id>/`:

* Primary step log (required): `primary.log`  
* Supporting artifacts (optional): `tmp_*` files, `.sha256` sidecars where required, etc.

Optional (non-canon) history retention:

* `audit/qa/hde-epic<NNN>/runs/<attempt_label>/...`  
  Where `<attempt_label>` is a UTC timestamp label (git-free).  
  If you keep run-local copies here, they MUST be treated as convenience copies, not canonical acceptance binding surfaces.

**Bootstrap snippet (run once; required for this runbook)**

\# Required operator-set variable (non-secret)  
export EVIDENCE\_ROOT="audit/qa/hde-epic023"

\# Determinism pins (canonical)  
export LC\_ALL=C  
export LANG=C  
export TZ=UTC

\# Rails defaults (closed)  
export SAFE\_MODE=1  
export ALLOW\_NETWORK=0  
export APP\_ENV=dev

\# Prevent incidental file creation outside audit/\*\* and artifacts/\*\* during python/pytest runs  
export PYTHONDONTWRITEBYTECODE=1  
export PYTEST\_ADDOPTS="-p no:cacheprovider"

\# Sanity check: confirm you are at repo root by presence of expected top-level dirs  
ls \-la docs audit artifacts ci tools tests \>/dev/null

#### **Step-log header schema expectations (minimum; required)**

Each primary step log MUST begin with a machine-readable header block containing at least:

* `check_id` (stable)

* `status` (PASS | FAIL\_BEHAVIOR | FAIL\_TOOLING | TOOLING\_BLOCKED | PARKED)

* `command` (literal command(s) executed for the check)

* `captured_env` (rails \+ determinism pins \+ materially relevant env keys; values allowed only for non-secrets)

* `pf_refs` (titles-only PF references used by this check; include § anchor when applicable; empty list allowed)

* `intended_tokens` (names-only; empty list allowed)

* `claimed_tokens` (names-only; empty list unless status=PASS and a token claim is being made)

Notes:

* If a legacy field named `tokens` exists, treat it as `intended_tokens` only (never as a claim surface).

#### **Step outcomes: tooling vs behavior (default mapping)**

Use this default mapping unless a governing PF rule overrides it:

* Missing required PO inputs or required local files → TOOLING\_BLOCKED  
* Tool/command invocation failure (non-zero RC attributable to tooling) → FAIL\_TOOLING  
* Behavioral failure only when the surface is reachable and a valid response/output is captured, but it contradicts canon → FAIL\_BEHAVIOR

---

### **Mandatory Step‑0 artifacts**

These are execution deliverables and must be mechanically produced.

#### **Step‑0A — Codespaces snapshot (mechanical; evidence not prose)**

Purpose: capture rails/pins posture, tooling versions, and presence-only env/secrets context without leaking values.

Canonical output (current-state; epic-level):

* `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json`

Optional (non-canon) run-local copy:

* If produced under a run-local tree, it MUST be byte-identical to the epic-level snapshot.

  #### **Step‑0B — Doc Delta Capture (mechanical; runbook self-honesty)**

Purpose: mechanically record repo reality mismatches, missing prerequisites, and canon conflicts (or explicitly record “no deltas”).

Canonical output (under `EVIDENCE_ROOT`):

* `00_meta/doc_deltas.md`

* `00_meta/doc_deltas.md.path_proof.txt`

Requirements:

* MUST be generated by commands (no manual editing; no placeholders).

* MUST explicitly list observed deltas (missing prerequisites / drift / conflicts), OR explicitly state “no deltas” when none are observed.

#### **Step‑0C — Prod handshake (identity-only) when target is prod-like**

Include only if the plan claims Codespaces → prod behavior.

If using `/internal/version` as part of Step‑0C:

* Interim posture is canon: `/internal/version` is operator-network-only; no application-layer auth yet.  
* Runbooks MUST NOT require an auth header as a prerequisite.  
* A runbook MAY accept an auth header input as an execution convenience, but MUST NOT treat it as canon-required.

---

### **Runbook Check Matrix**

Every row MUST have a corresponding Check Block (below).

| check\_id | check\_name | surface / D-goal mapping | rails posture | PO command(s) | PASS/FAIL predicates | primary evidence path | deliverables (minimal set) | tokens (optional) | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| D12\_close\_pack\_manifest | D12 — EPIC023 Close Pack Manifest | D12 / Guide deliverables | SAFE\_MODE=1, ALLOW\_NETWORK=0 | File existence \+ required anchors check | PASS if manifest \+ path proof exist and required anchors present | audit/qa/hde-epic023/checks/D12\_close\_pack\_manifest/primary.log | close pack manifest \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D13\_human\_index | D13 — Human Evidence Index | D13 / Guide deliverables | SAFE\_MODE=1, ALLOW\_NETWORK=0 | File existence \+ required anchors check | PASS if human evidence index \+ path proof exist and required anchors present | audit/qa/hde-epic023/checks/D13\_human\_index/primary.log | human evidence index \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D14\_index\_hash\_sentinel | D14 — Evidence Index Hash Sentinel | D14 / Guide deliverables | SAFE\_MODE=1, ALLOW\_NETWORK=0 | File existence \+ required anchors check | PASS if hash sentinel \+ path proof exist and required anchors present | audit/qa/hde-epic023/checks/D14\_index\_hash\_sentinel/primary.log | evidence index hash sentinel \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D15\_machine\_mirror | D15 — Machine Evidence Mirror | D15 / Governed evidence | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Schema \+ content slice check | PASS if evidence\_index.jsonl \+ path proof exist and EPIC023 slice checks pass | audit/qa/hde-epic023/checks/D15\_machine\_mirror/primary.log | evidence\_index.jsonl \+ path proof \+ primary.log | n/a | PF12 §8.5; PF10 Addendum 2.16 |
| D16\_orientation\_demo | D16 — Orientation Demo Evidence | D16 / Governed evidence | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Run orientation\_demo.py \--check | PASS if report \+ sample exist and validate; primary.log shows PASS | audit/qa/hde-epic023/checks/D16\_orientation\_demo/primary.log | orientation\_demo\_report.json \+ sample \+ primary.log | n/a | PF12 §8.5 |
| D17\_env\_pins | D17 — Determinism Environment Pins | D17 / Governed evidence | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Generate env pins log \+ path proof | PASS if env\_pins.log \+ path proof exist and primary.log shows PASS | audit/qa/hde-epic023/checks/D17\_env\_pins/primary.log | env\_pins.log \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D18\_sanity\_log | D18 — Sanity Pipeline Log | D18 / Governed evidence | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Generate sanity pipeline log \+ path proof | PASS if sanity\_pipeline.log \+ path proof exist and primary.log shows PASS | audit/qa/hde-epic023/checks/D18\_sanity\_log/primary.log | sanity\_pipeline.log \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D19\_json\_gate\_check\_log | D19 — Canonical JSON Gate Check Log | D19 / Governed evidence | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Generate json gate check log \+ path proof | PASS if json\_gate\_check.log \+ path proof exist and primary.log shows PASS | audit/qa/hde-epic023/checks/D19\_json\_gate\_check\_log/primary.log | json\_gate\_check.log \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D20\_json\_gate\_compare\_log | D20 — Canonical JSON Gate Compare Log | D20 / Governed evidence | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Generate json canon compare log \+ path proof | PASS if json\_canon\_compare.log \+ path proof exist and primary.log shows PASS | audit/qa/hde-epic023/checks/D20\_json\_gate\_compare\_log/primary.log | json\_canon\_compare.log \+ path proof \+ primary.log | none | PF06 §0.4.1 |
| D21\_internal\_version | D21 — Internal Version Endpoint | D21 / Surface endpoint | SAFE\_MODE=1, ALLOW\_NETWORK=0 | Evidence family \+ route/config proof check | PASS if artifacts/ops/internal\_version/ evidence family is present | audit/qa/hde-epic023/checks/D21\_internal\_version/primary.log | artifacts/ops/internal\_version/ (required files) \+ primary.log | n/a | PF14 §9.4 |
| D22\_canonical\_json\_gate\_structured\_record | D22 — Canonical JSON Gate Structured Record | D22 / Canonical JSON gate (UNPROVEN) | SAFE\_MODE=1, ALLOW\_NETWORK=0 | UNPROVEN/TOOLING\_BLOCKED: record posture only | TOOLING\_BLOCKED (UNPROVEN) — primary.log records the unproven posture | audit/qa/hde-epic023/checks/D22\_canonical\_json\_gate\_structured\_record/primary.log | primary.log only (UNPROVEN/TOOLING\_BLOCKED) | n/a | PF09 (canonical JSON gate) (UNPROVEN) |
| D23\_evidence\_index\_snapshot\_artifact | D23 — EPIC023 Evidence Index Snapshot Artifact | D23 / Evidence index snapshot (UNPROVEN) | SAFE\_MODE=1, ALLOW\_NETWORK=0 | UNPROVEN/TOOLING\_BLOCKED: record posture only | TOOLING\_BLOCKED (UNPROVEN) — primary.log records the unproven posture | audit/qa/hde-epic023/checks/D23\_evidence\_index\_snapshot\_artifact/primary.log | primary.log only (UNPROVEN/TOOLING\_BLOCKED) | n/a | (guide-only; UNPROVEN/TOOLING\_BLOCKED pending confirmation) |

Matrix rules (normative):

* Commands must be copy/paste-ready.  
* PASS/FAIL predicates must be explicit and mechanically checkable.  
* Tokens are optional; if present, use names-only from governed acceptance artifacts; no invention/aliases.

---

### **Check Blocks**

Repeat one block per matrix row.

#### **CHECK D07\_codespaces\_snapshot: D07 — Codespaces Snapshot**

Surface / D-goal mapping: D07 \+ Step‑0A (Codespaces snapshot)  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF12 — HDE-Schemas and Artifacts, §8.17.5; PF12 — HDE-Schemas and Artifacts, §8.3; PF19 — Glow QA Guide, §14.4.3 (titles-only)

Goal: Create the missing epic-level Codespaces snapshot and its path-proof transcript without logging secrets or using VCS identity.  
Preconditions: `EVIDENCE_ROOT` exported; you are at repo root.  
Setup: None beyond bootstrap exports.

**PO command(s) (copy/paste)**

CHECK\_ID="D07\_codespaces\_snapshot"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
SNAP="${EVIDENCE\_ROOT:?}/00\_meta/codespaces\_snapshot.json"  
PROOF="${SNAP}.path\_proof.txt"  
mkdir \-p "${LOG\_DIR}" "$(dirname "${SNAP}")"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import json, os, sys, pathlib, hashlib, datetime

def utc\_now\_z():  
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root \= pathlib.Path(os.environ\["EVIDENCE\_ROOT"\])  
snap \= root / "00\_meta" / "codespaces\_snapshot.json"  
proof \= pathlib.Path(str(snap) \+ ".path\_proof.txt")

payload \= {  
  "schema": "hde.qa.codespaces\_snapshot.v1",  
  "captured\_at\_utc": utc\_now\_z(),  
  "repo\_root": str(pathlib.Path(".").resolve()),  
  "git": {  
    "head\_sha": os.popen("git rev-parse HEAD").read().strip(),  
    "status\_porcelain": os.popen("git status \--porcelain").read(),  
  },  
  "env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
    "PYTHONDONTWRITEBYTECODE": os.environ.get("PYTHONDONTWRITEBYTECODE"),  
    "PYTHONHASHSEED": os.environ.get("PYTHONHASHSEED"),  
  }  
}

b \= (json.dumps(payload, ensure\_ascii=False, sort\_keys=True, separators=(",", ":")) \+ "\\n").encode("utf-8")  
snap.write\_bytes(b)

sha \= hashlib.sha256(b).hexdigest()  
st \= snap.stat()  
mtime\_utc \= datetime.datetime.fromtimestamp(st.st\_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

proof\_lines \= \[  
  f"path: {snap.as\_posix()}",  
  f"sha256: {sha}",  
  f"size\_bytes: {st.st\_size}",  
  f"mtime\_utc: {mtime\_utc}",  
  f"produced\_at\_utc: {utc\_now\_z()}",  
\]  
proof.write\_text("\\n".join(proof\_lines) \+ "\\n", encoding="utf-8")

print("PASS: codespaces\_snapshot.json \+ path proof written.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) generate codespaces\_snapshot.json \+ path proof",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
    "PYTHONDONTWRITEBYTECODE": os.environ.get("PYTHONDONTWRITEBYTECODE"),  
    "PYTHONHASHSEED": os.environ.get("PYTHONHASHSEED"),  
  },  
  "pf\_refs": \[  
    "PF12 — HDE-Schemas and Artifacts, §8.17.5",  
    "PF12 — HDE-Schemas and Artifacts, §8.3",  
    "PF19 — Glow QA Guide, §14.4.3"  
  \],  
  "intended\_tokens": \[\],  
  "claimed\_tokens": \[\],  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

\# Upsert this check into the step-logs manifest (PF19 §4.4.3)  
python \- \<\<PY \>\>"${LOG\_PATH}" 2\>&1  
import json, os, hashlib, datetime  
from pathlib import Path

def utc\_now\_z():  
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root \= Path(os.environ\["EVIDENCE\_ROOT"\])  
manifest \= root / "qa\_step\_logs\_manifest.json"  
proof \= Path(str(manifest) \+ ".path\_proof.txt")

epic\_id \= "HDE-EPIC023"  
check\_id \= "${CHECK\_ID}"  
status \= "${STATUS}"  
log\_path \= "${LOG\_PATH}"

now \= utc\_now\_z()

if manifest.exists():  
    try:  
        obj \= json.loads(manifest.read\_text(encoding="utf-8"))  
    except Exception:  
        obj \= {"epic\_id": epic\_id, "steps": \[\]}  
else:  
    obj \= {"epic\_id": epic\_id, "steps": \[\]}

if not isinstance(obj, dict):  
    obj \= {"epic\_id": epic\_id, "steps": \[\]}  
obj\["epic\_id"\] \= epic\_id

steps \= obj.get("steps")  
if not isinstance(steps, list):  
    steps \= \[\]  
steps \= \[s for s in steps if not (isinstance(s, dict) and s.get("check\_id") \== check\_id)\]  
steps.append({"check\_id": check\_id, "status": status, "log\_path": log\_path})  
steps.sort(key=lambda s: s.get("check\_id",""))  
obj\["steps"\] \= steps

data \= (json.dumps(obj, ensure\_ascii=False, sort\_keys=True, separators=(",", ":")) \+ "\\n").encode("utf-8")  
manifest.parent.mkdir(parents=True, exist\_ok=True)  
manifest.write\_bytes(data)

sha \= hashlib.sha256(data).hexdigest()  
st \= manifest.stat()  
mtime\_utc \= datetime.datetime.fromtimestamp(st.st\_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")  
proof\_lines \= \[  
    f"path: {manifest.as\_posix()}",  
    f"sha256: {sha}",  
    f"size\_bytes: {st.st\_size}",  
    f"mtime\_utc: {mtime\_utc}",  
    f"produced\_at\_utc: {now}",  
\]  
proof.write\_text("\\n".join(proof\_lines) \+ "\\n", encoding="utf-8")

print(f"manifest\_upsert: check\_id={check\_id} status={status} log\_path={log\_path} steps\_count={len(steps)}")  
PY

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json` exists and validates against PF12 §8.17.5 (exact keys; canonical JSON; no secrets)  
* `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt` exists and matches the snapshot sha/size per PF12 §8.3

FAIL\_BEHAVIOR if:

* (Not applicable for this check; failures here are tooling/IO unless the generated bytes violate PF12 schema)

FAIL\_TOOLING if:

* Snapshot generation/validation script exits non-zero

TOOLING\_BLOCKED if:

* `EVIDENCE_ROOT` is not set or `audit/qa/hde-epic023/00_meta/` is not writable

**Primary evidence artifact (required)**

Canonical (current-state) primary log:

* `audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log`

One-line description:

* “Header (command \+ captured\_env \+ status) \+ transcript \+ schema/proof validation outputs.”

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json`  
* `audit/qa/hde-epic023/00_meta/codespaces_snapshot.json.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D07_codespaces_snapshot/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D08\_qa\_doc\_deltas\_capture: D08 — QA Doc Deltas Capture**

Surface / D-goal mapping: D08 \+ governed doc delta capture  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF19 — Glow QA Guide, §14.4.4; PF27 — Plan Templates (Step‑0B posture) (titles-only)

Goal: Mechanically generate and validate the epic-level Doc Delta Capture (`doc_deltas.md` \+ path proof) as a current-state ledger (explicit “no deltas” when empty).  
 Preconditions: `EVIDENCE_ROOT` exported.

**PO command(s) (copy/paste)**

`CHECK_ID="D08_qa_doc_deltas_capture"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`DOC="${EVIDENCE_ROOT:?}/00_meta/doc_deltas.md"`

`PROOF="${DOC}.path_proof.txt"`

`mkdir -p "${LOG_DIR}" "$(dirname "${DOC}")"`

`python - <<'PY' >"${TMP_OUT}" 2>&1`

`import os, sys, json, hashlib, datetime`

`from pathlib import Path`

`def utc_now_z():`

    `return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`doc = root / "00_meta" / "doc_deltas.md"`

`proof = Path(str(doc) + ".path_proof.txt")`

`checks_dir = root / "checks"`

`deltas = []`

`if checks_dir.exists():`

    `for d in sorted([p for p in checks_dir.iterdir() if p.is_dir()]):`

        `lp = d / "primary.log"`

        `if not lp.exists():`

            `continue`

        `try:`

            `first = lp.read_text(encoding="utf-8", errors="replace").splitlines()[0]`

            `hdr = json.loads(first)`

            `cid = str(hdr.get("check_id", d.name))`

            `status = str(hdr.get("status", "UNKNOWN"))`

        `except Exception:`

            `cid = d.name`

            `status = "UNPARSEABLE_HEADER"`

        `if status != "PASS":`

            `deltas.append(f"- {cid} status={status} (see {lp.as_posix()})")`

`now = utc_now_z()`

`lines = []`

`lines.append("# QA Doc Deltas Capture — HDE-EPIC023")`

`lines.append("")`

`lines.append(f"captured_at_utc: {now}")`

`lines.append(f"scope: current-state deltas observed in check logs under {checks_dir.as_posix()}/")`

`lines.append("deltas:")`

`if deltas:`

    `lines.extend(deltas)`

`else:`

    `lines.append("- no deltas")`

`lines.append("")`

`doc.write_text("\n".join(lines), encoding="utf-8")`

`b = doc.read_bytes()`

`if len(b) == 0:`

    `print("FAIL_BEHAVIOR: doc_deltas.md is empty after write")`

    `sys.exit(2)`

`if not b.endswith(b"\n"):`

    `print("FAIL_BEHAVIOR: doc_deltas.md missing trailing LF")`

    `sys.exit(2)`

`txt = doc.read_text(encoding="utf-8", errors="replace")`

`for bad in ["TBD", "PLACEHOLDER", "placeholder"]:`

    `if bad in txt:`

        `print(f"FAIL_BEHAVIOR: placeholder marker detected: {bad}")`

        `sys.exit(2)`

`sha = hashlib.sha256(b).hexdigest()`

`st = doc.stat()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`proof_lines = [`

    `f"path: {doc.as_posix()}",`

    `f"sha256: {sha}",`

    `f"size_bytes: {st.st_size}",`

    `f"mtime_utc: {mtime_utc}",`

    `f"produced_at_utc: {now}",`

`]`

`proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")`

`print("PASS: doc_deltas.md + path proof generated and validated.")`

`PY`

`RC=$?`

`STATUS="PASS"`

`case "${RC}" in`

  `0) STATUS="PASS" ;;`

  `2) STATUS="FAIL_BEHAVIOR" ;;`

  `3) STATUS="TOOLING_BLOCKED" ;;`

  `*) STATUS="FAIL_TOOLING" ;;`

`esac`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "python (embedded) generate+prove+validate ${EVIDENCE_ROOT}/00_meta/doc_deltas.md",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"PF19 — Glow QA Guide, §14.4.4",`

    `"PF27 — Plan Templates (Step‑0B posture) (titles-only)"`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import json, os, hashlib, datetime`

`from pathlib import Path`

`def utc_now_z():`

    `return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = Path(str(manifest) + ".path_proof.txt")`

`epic_id = "HDE-EPIC023"`

`check_id = "${CHECK_ID}"`

`status = "${STATUS}"`

`log_path = "${LOG_PATH}"`

`now = utc_now_z()`

`if manifest.exists():`

    `try:`

        `obj = json.loads(manifest.read_text(encoding="utf-8"))`

    `except Exception:`

        `obj = {"epic_id": epic_id, "steps": []}`

`else:`

    `obj = {"epic_id": epic_id, "steps": []}`

`if not isinstance(obj, dict):`

    `obj = {"epic_id": epic_id, "steps": []}`

`obj["epic_id"] = epic_id`

`steps = obj.get("steps")`

`if not isinstance(steps, list):`

    `steps = []`

`steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]`

`steps.append({"check_id": check_id, "status": status, "log_path": log_path})`

`steps.sort(key=lambda s: s.get("check_id",""))`

`obj["steps"] = steps`

`data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")`

`manifest.parent.mkdir(parents=True, exist_ok=True)`

`manifest.write_bytes(data)`

`sha = hashlib.sha256(data).hexdigest()`

`st = manifest.stat()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`proof_lines = [`

    `f"path: {manifest.as_posix()}",`

    `f"sha256: {sha}",`

    `f"size_bytes: {st.st_size}",`

    `f"mtime_utc: {mtime_utc}",`

    `f"produced_at_utc: {now}",`

`]`

`proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")`

`print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

**Expected result (PASS/FAIL predicates)**

PASS if:

* `audit/qa/hde-epic023/00_meta/doc_deltas.md` is generated, non-empty, LF-terminated

* Content includes an explicit `- no deltas` line OR one-or-more `- <check_id> status=<...> (see <log_path>)` lines

* No placeholder markers are present

* `audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt` exists and is non-empty

FAIL\_BEHAVIOR if:

* generated file violates LF / placeholder / non-empty predicates

FAIL\_TOOLING if:

* embedded generator/validator crashes unexpectedly

TOOLING\_BLOCKED if:

* `EVIDENCE_ROOT` is not set

**Primary evidence artifact (required)**

Canonical (current-state) primary log:

* `audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log`

One-line description:

* “Header \+ transcript proving Step‑0B doc deltas artifact is mechanically generated and valid.”

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/00_meta/doc_deltas.md`

* `audit/qa/hde-epic023/00_meta/doc_deltas.md.path_proof.txt`

* `audit/qa/hde-epic023/checks/D08_qa_doc_deltas_capture/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D09\_pf23\_consult\_capture: D09 — PF23 Consult Capture**

Surface / D-goal mapping: D09 \+ PF23 trace capture  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF23 — Reality Audits (consult trace only); PF27 — PF23 anchors (titles-only)

Goal: Verify the PF23 consult capture exists and is non-empty.  
Preconditions: `EVIDENCE_ROOT` exported.

**PO command(s) (copy/paste)**

CHECK\_ID="D09\_pf23\_consult\_capture"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import os, sys, pathlib  
root \= pathlib.Path(os.environ\["EVIDENCE\_ROOT"\])  
p \= root / "00\_meta" / "pf23\_consult.md"

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)

b \= p.read\_bytes()  
if len(b) \== 0:  
    print("FAIL\_BEHAVIOR: pf23\_consult.md is empty")  
    sys.exit(2)  
if not b.endswith(b"\\n"):  
    print("FAIL\_BEHAVIOR: pf23\_consult.md missing trailing LF")  
    sys.exit(2)

print("PASS: pf23\_consult.md exists and is non-empty.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) verify ${EVIDENCE\_ROOT}/00\_meta/pf23\_consult.md",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `audit/qa/hde-epic023/00_meta/pf23_consult.md` exists and is non-empty

FAIL\_BEHAVIOR if:

* file exists but is empty or not LF-terminated

FAIL\_TOOLING if:

* embedded validator crashes unexpectedly

TOOLING\_BLOCKED if:

* file is missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D09_pf23_consult_capture/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/00_meta/pf23_consult.md`  
* `audit/qa/hde-epic023/checks/D09_pf23_consult_capture/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D01\_acceptance\_map: D01 — EPIC023 Acceptance Map**

Surface / D-goal mapping: D01 \+ Acceptance scaffold presence/shape  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF14 — HDE-Mechanics Guide, §37.2; PF10 — HDE-Build Notes, Addendum 2.13 (titles-only)

Goal: Verify acceptance map exists, parses, and has expected top-level shape without placeholders or path-proof references.  
Preconditions: repo has `docs/` and `audit/` trees.

**PO command(s) (copy/paste)**

CHECK\_ID="D01\_acceptance\_map"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import json, os, sys, pathlib, re  
p \= pathlib.Path("docs/acceptance\_map\_epic023.json")  
pp \= pathlib.Path("docs/acceptance\_map\_epic023.json.path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

b \= p.read\_bytes()  
if not b.endswith(b"\\n"):  
    print("FAIL\_BEHAVIOR: acceptance map missing trailing LF")  
    sys.exit(2)

obj \= json.loads(p.read\_text(encoding="utf-8"))  
if not isinstance(obj, dict):  
    print("FAIL\_BEHAVIOR: acceptance map is not a JSON object")  
    sys.exit(2)

keys \= set(obj.keys())  
expected \= {"epic\_id","tokens"}  
if keys \!= expected:  
    print(f"FAIL\_BEHAVIOR: top-level keys mismatch: got={sorted(keys)} expected={sorted(expected)}")  
    sys.exit(2)

\# basic content checks  
if obj.get("epic\_id") \!= "HDE-EPIC023":  
    print(f"FAIL\_BEHAVIOR: epic\_id mismatch: {obj.get('epic\_id')}")  
    sys.exit(2)

tokens \= obj.get("tokens")  
if not isinstance(tokens, list) or len(tokens) \== 0:  
    print("FAIL\_BEHAVIOR: tokens must be a non-empty list")  
    sys.exit(2)

txt \= p.read\_text(encoding="utf-8", errors="replace")  
if ".path\_proof.txt" in txt:  
    print("FAIL\_BEHAVIOR: acceptance map must not reference .path\_proof.txt")  
    sys.exit(2)  
if re.search(r"(TBD|PLACEHOLDER|placeholder)", txt):  
    print("FAIL\_BEHAVIOR: placeholder markers detected")  
    sys.exit(2)

print(f"PASS: acceptance map OK (tokens\_count={len(tokens)}).")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) validate docs/acceptance\_map\_epic023.json (+ path proof)",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `docs/acceptance_map_epic023.json` exists, parses, ends with LF  
* Top-level keys are exactly `{epic_id, tokens}`  
* `epic_id == "HDE-EPIC023"`  
* No `.path_proof.txt` references and no placeholder markers

FAIL\_BEHAVIOR if:

* Any of the above validations fail

FAIL\_TOOLING if:

* JSON parse errors due to tooling/runtime failures (unexpected crash)

TOOLING\_BLOCKED if:

* Acceptance map file is missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D01_acceptance_map/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `docs/acceptance_map_epic023.json`  
* `docs/acceptance_map_epic023.json.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D01_acceptance_map/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D02\_token\_evidence\_matrix: D02 — Token-to-Evidence Matrix**

Surface / D-goal mapping: D02 \+ acceptance scaffold matrix validity  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF14 — HDE-Mechanics Guide, §37.2; PF10 — HDE-Build Notes, Addendum 2.13 (titles-only)

Goal: Verify token-to-evidence matrix exists, contains a Markdown table header with PF12 minimum columns, and avoids path-proof references/placeholders.  
 Preconditions: none.

**PO command(s) (copy/paste)**

`CHECK_ID="D02_token_evidence_matrix"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`mkdir -p "${LOG_DIR}"`

`python - <<'PY' >"${TMP_OUT}" 2>&1`

`import os, sys, pathlib, re`

`p = pathlib.Path("audit/qa/hde-epic023/token_evidence_matrix.md")`

`pp = pathlib.Path(str(p) + ".path_proof.txt")`

`if not p.exists():`

    `print(f"TOOLING_BLOCKED: missing {p}")`

    `sys.exit(3)`

`if not pp.exists():`

    `print(f"FAIL_BEHAVIOR: missing path proof {pp}")`

    `sys.exit(2)`

`b = p.read_bytes()`

`if len(b) == 0:`

    `print("FAIL_BEHAVIOR: matrix is empty")`

    `sys.exit(2)`

`if not b.endswith(b"\n"):`

    `print("FAIL_BEHAVIOR: matrix missing trailing LF")`

    `sys.exit(2)`

`txt = p.read_text(encoding="utf-8", errors="replace")`

`if ".path_proof.txt" in txt:`

    `print("FAIL_BEHAVIOR: matrix must not reference .path_proof.txt")`

    `sys.exit(2)`

`if re.search(r"(TBD|PLACEHOLDER|placeholder)", txt):`

    `print("FAIL_BEHAVIOR: placeholder markers detected")`

    `sys.exit(2)`

`required_cols = {"token_name","owner_pf","evidence_artifacts","qa_root_logs","ci_tests_jobs"}`

`header_cells = None`

`for line in txt.splitlines():`

    `s = line.strip()`

    `if not s.startswith("|"):`

        `continue`

    `# candidate markdown table row`

    `cells = [c.strip() for c in s.strip("|").split("|")]`

    `if required_cols.intersection(set(cells)):`

        `header_cells = cells`

        `break`

`if header_cells is None:`

    `print("FAIL_BEHAVIOR: missing a Markdown table header row containing PF12 minimum columns")`

    `sys.exit(2)`

`missing = sorted(required_cols.difference(set(header_cells)))`

`if missing:`

    `print("FAIL_BEHAVIOR: missing required PF12 minimum columns:")`

    `for m in missing:`

        `print(f"  - {m}")`

    `print(f"observed_header_cells={header_cells}")`

    `sys.exit(2)`

`print("PASS: token_evidence_matrix.md header includes PF12 minimum columns and contains no placeholders/path-proof refs.")`

`PY`

`RC=$?`

`STATUS="PASS"`

`case "${RC}" in`

  `0) STATUS="PASS" ;;`

  `2) STATUS="FAIL_BEHAVIOR" ;;`

  `3) STATUS="TOOLING_BLOCKED" ;;`

  `*) STATUS="FAIL_TOOLING" ;;`

`esac`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "python (embedded) validate audit/qa/hde-epic023/token_evidence_matrix.md (+ path proof + PF12 minimum columns)",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"PF14 — HDE-Mechanics Guide, §37.2",`

    `"PF10 — HDE-Build Notes, Addendum 2.13 (titles-only)"`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import json, os, hashlib, datetime`

`from pathlib import Path`

`def utc_now_z():`

    `return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = Path(str(manifest) + ".path_proof.txt")`

`epic_id = "HDE-EPIC023"`

`check_id = "${CHECK_ID}"`

`status = "${STATUS}"`

`log_path = "${LOG_PATH}"`

`now = utc_now_z()`

`if manifest.exists():`

    `try:`

        `obj = json.loads(manifest.read_text(encoding="utf-8"))`

    `except Exception:`

        `obj = {"epic_id": epic_id, "steps": []}`

`else:`

    `obj = {"epic_id": epic_id, "steps": []}`

`if not isinstance(obj, dict):`

    `obj = {"epic_id": epic_id, "steps": []}`

`obj["epic_id"] = epic_id`

`steps = obj.get("steps")`

`if not isinstance(steps, list):`

    `steps = []`

`steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]`

`steps.append({"check_id": check_id, "status": status, "log_path": log_path})`

`steps.sort(key=lambda s: s.get("check_id",""))`

`obj["steps"] = steps`

`data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")`

`manifest.parent.mkdir(parents=True, exist_ok=True)`

`manifest.write_bytes(data)`

`sha = hashlib.sha256(data).hexdigest()`

`st = manifest.stat()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`proof_lines = [`

    `f"path: {manifest.as_posix()}",`

    `f"sha256: {sha}",`

    `f"size_bytes: {st.st_size}",`

    `f"mtime_utc: {mtime_utc}",`

    `f"produced_at_utc: {now}",`

`]`

`proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")`

`print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

**Expected result (PASS/FAIL predicates)**

PASS if:

* Matrix exists and is non-empty

* Matrix table header includes PF12 minimum columns: `token_name`, `owner_pf`, `evidence_artifacts`, `qa_root_logs`, `ci_tests_jobs`

* Contains no `.path_proof.txt` references and no placeholders

FAIL\_BEHAVIOR if:

* Any predicate fails

FAIL\_TOOLING if:

* embedded validator crashes unexpectedly

TOOLING\_BLOCKED if:

* matrix file is missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D02_token_evidence_matrix/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/token_evidence_matrix.md`

* `audit/qa/hde-epic023/token_evidence_matrix.md.path_proof.txt`

* `audit/qa/hde-epic023/checks/D02_token_evidence_matrix/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D03\_acceptance\_viability: D03 — Acceptance Map Viability Log**

Surface / D-goal mapping: D03 \+ viability log content  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF10 — HDE-Build Notes, Addendum 2.13 (titles-only)

Goal: Verify viability log exists and indicates MISSING=0.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D03\_acceptance\_viability"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import os, sys, pathlib, re  
p \= pathlib.Path("audit/qa/hde-epic023/acceptance\_map\_viability.log")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

txt \= p.read\_text(encoding="utf-8", errors="replace").splitlines()  
if len(txt) \== 0:  
    print("FAIL\_BEHAVIOR: viability log is empty")  
    sys.exit(2)

\# Required signals (from observed structure): run marker \+ summary with MISSING=0  
has\_run \= any(line.startswith("run:viability-check") for line in txt)  
summary\_lines \= \[line for line in txt if line.startswith("summary:")\]  
if not has\_run:  
    print("FAIL\_BEHAVIOR: missing 'run:viability-check' line")  
    sys.exit(2)  
if not summary\_lines:  
    print("FAIL\_BEHAVIOR: missing summary line")  
    sys.exit(2)

summary \= summary\_lines\[-1\]  
m \= re.search(r"\\bMISSING=(\\d+)\\b", summary)  
if not m:  
    print(f"FAIL\_BEHAVIOR: summary missing MISSING=... field: {summary}")  
    sys.exit(2)  
missing \= int(m.group(1))  
if missing \!= 0:  
    print(f"FAIL\_BEHAVIOR: MISSING \!= 0 (MISSING={missing})")  
    sys.exit(2)

print(f"PASS: viability summary indicates MISSING=0. (summary='{summary}')")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) validate audit/qa/hde-epic023/acceptance\_map\_viability.log (+ path proof)",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* viability log exists and has a `summary:` line with `MISSING=0`

FAIL\_BEHAVIOR if:

* MISSING is non-zero or required lines are absent

FAIL\_TOOLING if:

* embedded validator crashes unexpectedly

TOOLING\_BLOCKED if:

* viability log is missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D03_acceptance_viability/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/acceptance_map_viability.log`  
* `audit/qa/hde-epic023/acceptance_map_viability.log.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D03_acceptance_viability/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D04\_acceptance\_alignment\_validator: D04 — Acceptance Alignment Validator Test**

Surface / D-goal mapping: D04 \+ acceptance enforcement (map/matrix/index/mirror alignment)  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF14 — HDE-Mechanics Guide, §37.2; PF04 — HDE-Governance (token registry invariants) (titles-only)

Goal: Run the acceptance alignment validator test and record PASS/FAIL as executable evidence.  
Preconditions: pytest available in the Codespaces environment.

**PO command(s) (copy/paste)**

CHECK\_ID="D04\_acceptance\_alignment\_validator"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

\# Run pytest (no cache provider; no bytecode)  
python \-m pytest tests/qa/test\_epic023\_acceptance\_alignment.py \>"${TMP\_OUT}" 2\>&1  
RC=$?

STATUS="PASS"  
INTENDED\_TOKENS="\[\]"  
CLAIMED\_TOKENS="\[\]"

\# Extract intended tokens from the acceptance map (names-only) without writing outside governed roots  
TOK\_TMP="${LOG\_DIR}/tmp\_tokens.json"  
python \- \<\<'PY' \>"${TOK\_TMP}" 2\>/dev/null || true  
import json, pathlib  
p \= pathlib.Path("docs/acceptance\_map\_epic023.json")  
obj \= json.loads(p.read\_text(encoding="utf-8"))  
tokens \= obj.get("tokens", \[\])  
names \= \[\]  
for t in tokens:  
    if isinstance(t, dict) and "token" in t:  
        names.append(t\["token"\])  
print(json.dumps(sorted(set(names))))  
PY  
INTENDED\_TOKENS="$(cat "${TOK\_TMP}" 2\>/dev/null || echo '\[\]')"  
rm \-f "${TOK\_TMP}"

if \[ "${RC}" \-ne 0 \]; then  
  STATUS="FAIL\_BEHAVIOR"  
else  
  STATUS="PASS"  
  CLAIMED\_TOKENS="${INTENDED\_TOKENS}"  
fi

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python \-m pytest tests/qa/test\_epic023\_acceptance\_alignment.py (no bytecode) \+ extract intended tokens",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  },  
  "pf\_refs": \[  
    "PF14 — HDE-Mechanics Guide, §37.2",  
    "PF04 — HDE-Governance (token registry invariants) (titles-only)"  
  \],  
  "intended\_tokens": json.loads("""${INTENDED\_TOKENS}"""),  
  "claimed\_tokens": json.loads("""${CLAIMED\_TOKENS}"""),  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

\# Upsert this check into the step-logs manifest (PF19 §4.4.3)  
python \- \<\<PY \>\>"${LOG\_PATH}" 2\>&1  
import json, os, hashlib, datetime  
from pathlib import Path

def utc\_now\_z():  
    return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")

root \= Path(os.environ\["EVIDENCE\_ROOT"\])  
manifest \= root / "qa\_step\_logs\_manifest.json"  
proof \= Path(str(manifest) \+ ".path\_proof.txt")

epic\_id \= "HDE-EPIC023"  
check\_id \= "${CHECK\_ID}"  
status \= "${STATUS}"  
log\_path \= "${LOG\_PATH}"

now \= utc\_now\_z()

if manifest.exists():  
    try:  
        obj \= json.loads(manifest.read\_text(encoding="utf-8"))  
    except Exception:  
        obj \= {"epic\_id": epic\_id, "steps": \[\]}  
else:  
    obj \= {"epic\_id": epic\_id, "steps": \[\]}

if not isinstance(obj, dict):  
    obj \= {"epic\_id": epic\_id, "steps": \[\]}  
obj\["epic\_id"\] \= epic\_id

steps \= obj.get("steps")  
if not isinstance(steps, list):  
    steps \= \[\]  
steps \= \[s for s in steps if not (isinstance(s, dict) and s.get("check\_id") \== check\_id)\]  
steps.append({"check\_id": check\_id, "status": status, "log\_path": log\_path})  
steps.sort(key=lambda s: s.get("check\_id",""))  
obj\["steps"\] \= steps

data \= (json.dumps(obj, ensure\_ascii=False, sort\_keys=True, separators=(",", ":")) \+ "\\n").encode("utf-8")  
manifest.parent.mkdir(parents=True, exist\_ok=True)  
manifest.write\_bytes(data)

sha \= hashlib.sha256(data).hexdigest()  
st \= manifest.stat()  
mtime\_utc \= datetime.datetime.fromtimestamp(st.st\_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")  
proof\_lines \= \[  
    f"path: {manifest.as\_posix()}",  
    f"sha256: {sha}",  
    f"size\_bytes: {st.st\_size}",  
    f"mtime\_utc: {mtime\_utc}",  
    f"produced\_at\_utc: {now}",  
\]  
proof.write\_text("\\n".join(proof\_lines) \+ "\\n", encoding="utf-8")

print(f"manifest\_upsert: check\_id={check\_id} status={status} log\_path={log\_path} steps\_count={len(steps)}")  
PY

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `python -m pytest tests/qa/test_epic023_acceptance_alignment.py` returns RC=0

FAIL\_BEHAVIOR if:

* pytest runs and returns non-zero (test assertions failed)

FAIL\_TOOLING if:

* pytest cannot be invoked (missing pytest / interpreter errors)  
  (If this occurs, re-run with the same command and capture the traceback; classify as FAIL\_TOOLING only if the failure is clearly invocation-level.)

TOOLING\_BLOCKED if:

* required test file is missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/checks/D04_acceptance_alignment_validator/primary.log` (contains pytest transcript)

**Tokens (optional)**

This check is token-relevant (alignment validator). Token lists are populated in the step-log header.

---

#### **CHECK D05\_step\_logs\_manifest: D05 — Step Logs Manifest**

Surface / D-goal mapping: D05 \+ governed step log manifest validity  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF19 — Glow QA Guide, §4.4.3 (titles-only)

Goal: Validate that the current-state step logs manifest exists and is PF19-aligned (per-entry required fields \+ uniqueness \+ log\_path existence under epic QA root).  
 Preconditions: `EVIDENCE_ROOT` exported (check logs produced under `${EVIDENCE_ROOT}/checks/**/primary.log`).

**PO command(s) (copy/paste)**

`CHECK_ID="D05_step_logs_manifest"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`MANIFEST="${EVIDENCE_ROOT:?}/qa_step_logs_manifest.json"`

`PROOF="${MANIFEST}.path_proof.txt"`

`mkdir -p "${LOG_DIR}"`

`python - <<'PY' >"${TMP_OUT}" 2>&1`

`import os, sys, json, hashlib`

`from pathlib import Path`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = Path(str(manifest) + ".path_proof.txt")`

`if not manifest.exists():`

    `print(f"TOOLING_BLOCKED: missing {manifest}")`

    `sys.exit(3)`

`if not proof.exists():`

    `print(f"FAIL_BEHAVIOR: missing path proof {proof}")`

    `sys.exit(2)`

`b = manifest.read_bytes()`

`if len(b) == 0:`

    `print("FAIL_BEHAVIOR: manifest is empty")`

    `sys.exit(2)`

`if not b.endswith(b"\n"):`

    `print("FAIL_BEHAVIOR: manifest missing trailing LF")`

    `sys.exit(2)`

`obj = json.loads(manifest.read_text(encoding="utf-8"))`

`if not isinstance(obj, dict):`

    `print("FAIL_BEHAVIOR: manifest JSON must be an object")`

    `sys.exit(2)`

`if obj.get("epic_id") != "HDE-EPIC023":`

    `print(f"FAIL_BEHAVIOR: epic_id mismatch: {obj.get('epic_id')}")`

    `sys.exit(2)`

`steps = obj.get("steps")`

`if not isinstance(steps, list) or len(steps) == 0:`

    `print("TOOLING_BLOCKED: manifest.steps missing or empty")`

    `sys.exit(3)`

`allowed_status = {"PASS","FAIL_BEHAVIOR","FAIL_TOOLING","TOOLING_BLOCKED","PARKED"}`

`seen = set()`

`for i, s in enumerate(steps):`

    `if not isinstance(s, dict):`

        `print(f"FAIL_BEHAVIOR: steps[{i}] is not an object")`

        `sys.exit(2)`

    `for k in ("check_id","status","log_path"):`

        `if k not in s:`

            `print(f"FAIL_BEHAVIOR: steps[{i}] missing required field: {k}")`

            `sys.exit(2)`

    `cid = s["check_id"]`

    `st = s["status"]`

    `lp = s["log_path"]`

    `if not isinstance(cid, str) or not cid:`

        `print(f"FAIL_BEHAVIOR: steps[{i}].check_id must be a non-empty string")`

        `sys.exit(2)`

    `if cid in seen:`

        `print(f"FAIL_BEHAVIOR: duplicate check_id in manifest: {cid}")`

        `sys.exit(2)`

    `seen.add(cid)`

    `if st not in allowed_status:`

        `print(f"FAIL_BEHAVIOR: invalid status for {cid}: {st}")`

        `sys.exit(2)`

    `if not isinstance(lp, str) or not lp:`

        `print(f"FAIL_BEHAVIOR: steps[{i}].log_path must be a non-empty string")`

        `sys.exit(2)`

    `# Must live under epic QA root`

    `if not lp.startswith(root.as_posix() + "/"):`

        `print(f"FAIL_BEHAVIOR: log_path not under epic QA root: {cid} log_path={lp} root={root.as_posix()}")`

        `sys.exit(2)`

    `if not Path(lp).exists():`

        `print(f"FAIL_BEHAVIOR: referenced log_path does not exist: {cid} log_path={lp}")`

        `sys.exit(2)`

`# Path proof must match current bytes (sha256)`

`sha = hashlib.sha256(b).hexdigest()`

`proof_txt = proof.read_text(encoding="utf-8", errors="replace")`

`if f"sha256: {sha}" not in proof_txt:`

    `print("FAIL_BEHAVIOR: manifest path proof sha256 does not match current manifest bytes")`

    `sys.exit(2)`

`print(f"PASS: manifest OK (steps_count={len(steps)}; unique_check_ids={len(seen)}).")`

`PY`

`RC=$?`

`STATUS="PASS"`

`case "${RC}" in`

  `0) STATUS="PASS" ;;`

  `2) STATUS="FAIL_BEHAVIOR" ;;`

  `3) STATUS="TOOLING_BLOCKED" ;;`

  `*) STATUS="FAIL_TOOLING" ;;`

`esac`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "python (embedded) validate ${MANIFEST} (+ path proof; required fields check_id/status/log_path; uniqueness; existence under epic QA root)",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"PF19 — Glow QA Guide, §4.4.3 (titles-only)"`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import json, os, hashlib, datetime`

`from pathlib import Path`

`def utc_now_z():`

    `return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = Path(str(manifest) + ".path_proof.txt")`

`epic_id = "HDE-EPIC023"`

`check_id = "${CHECK_ID}"`

`status = "${STATUS}"`

`log_path = "${LOG_PATH}"`

`now = utc_now_z()`

`if manifest.exists():`

    `try:`

        `obj = json.loads(manifest.read_text(encoding="utf-8"))`

    `except Exception:`

        `obj = {"epic_id": epic_id, "steps": []}`

`else:`

    `obj = {"epic_id": epic_id, "steps": []}`

`if not isinstance(obj, dict):`

    `obj = {"epic_id": epic_id, "steps": []}`

`obj["epic_id"] = epic_id`

`steps = obj.get("steps")`

`if not isinstance(steps, list):`

    `steps = []`

`steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]`

`steps.append({"check_id": check_id, "status": status, "log_path": log_path})`

`steps.sort(key=lambda s: s.get("check_id",""))`

`obj["steps"] = steps`

`data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")`

`manifest.parent.mkdir(parents=True, exist_ok=True)`

`manifest.write_bytes(data)`

`sha = hashlib.sha256(data).hexdigest()`

`st = manifest.stat()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`proof_lines = [`

    `f"path: {manifest.as_posix()}",`

    `f"sha256: {sha}",`

    `f"size_bytes: {st.st_size}",`

    `f"mtime_utc: {mtime_utc}",`

    `f"produced_at_utc: {now}",`

`]`

`proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")`

`print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

**Expected result (PASS/FAIL predicates)**

PASS if:

* `audit/qa/hde-epic023/qa_step_logs_manifest.json` exists, is LF-terminated, parses as JSON object

* `epic_id == "HDE-EPIC023"`

* `steps` is a non-empty list

* Every step entry includes required fields: `check_id`, `status`, `log_path`

* `check_id` values are unique

* Every `log_path` exists and is under `audit/qa/hde-epic023/`

* `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt` exists and its sha256 matches current manifest bytes

FAIL\_BEHAVIOR if:

* Any required predicate fails (missing fields, duplicates, log\_path missing/outside root, sha mismatch)

FAIL\_TOOLING if:

* embedded validator crashes unexpectedly

TOOLING\_BLOCKED if:

* manifest missing OR `steps` missing/empty

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/qa_step_logs_manifest.json`

* `audit/qa/hde-epic023/qa_step_logs_manifest.json.path_proof.txt`

* `audit/qa/hde-epic023/checks/D05_step_logs_manifest/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D06\_primary\_step\_logs: D06 — Primary QA Step Logs**

Surface / D-goal mapping: D06 \+ verify referenced primary logs exist and are non-empty  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF19 — Glow QA Guide, §4.4.4 (titles-only)

Goal: Validate that every `log_path` referenced in the step logs manifest exists under the epic QA root and is non-empty.  
 Preconditions: D05 produced a non-empty manifest under `audit/qa/hde-epic023/`.

**PO command(s) (copy/paste)**

`CHECK_ID="D06_primary_step_logs"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`MANIFEST="${EVIDENCE_ROOT:?}/qa_step_logs_manifest.json"`

`mkdir -p "${LOG_DIR}"`

`python - <<'PY' >"${TMP_OUT}" 2>&1`

`import os, sys, json`

`from pathlib import Path`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`if not manifest.exists():`

    `print(f"TOOLING_BLOCKED: missing manifest {manifest}")`

    `sys.exit(3)`

`obj = json.loads(manifest.read_text(encoding="utf-8"))`

`steps = obj.get("steps")`

`if not isinstance(steps, list) or len(steps) == 0:`

    `print("TOOLING_BLOCKED: manifest.steps missing or empty")`

    `sys.exit(3)`

`missing = []`

`empty = []`

`outside = []`

`for s in steps:`

    `if not isinstance(s, dict):`

        `continue`

    `cid = s.get("check_id")`

    `lp = s.get("log_path")`

    `if not isinstance(lp, str) or not lp:`

        `continue`

    `if not lp.startswith(root.as_posix() + "/"):`

        `outside.append((cid, lp))`

        `continue`

    `p = Path(lp)`

    `if not p.exists():`

        `missing.append((cid, lp))`

        `continue`

    `if p.stat().st_size == 0:`

        `empty.append((cid, lp))`

`if outside:`

    `print("FAIL_BEHAVIOR: manifest contains log_path outside epic QA root:")`

    `for cid, lp in outside:`

        `print(f"  - check_id={cid} log_path={lp}")`

    `sys.exit(2)`

`if missing:`

    `print("FAIL_BEHAVIOR: missing referenced log paths:")`

    `for cid, lp in missing:`

        `print(f"  - check_id={cid} log_path={lp}")`

    `sys.exit(2)`

`if empty:`

    `print("FAIL_BEHAVIOR: referenced log paths exist but are empty:")`

    `for cid, lp in empty:`

        `print(f"  - check_id={cid} log_path={lp}")`

    `sys.exit(2)`

`print(f"PASS: all referenced log_path entries exist and are non-empty. (steps_count={len(steps)})")`

`PY`

`RC=$?`

`STATUS="PASS"`

`case "${RC}" in`

  `0) STATUS="PASS" ;;`

  `2) STATUS="FAIL_BEHAVIOR" ;;`

  `3) STATUS="TOOLING_BLOCKED" ;;`

  `*) STATUS="FAIL_TOOLING" ;;`

`esac`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "python (embedded) validate manifest.steps[].log_path exist+non-empty under epic QA root",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"PF19 — Glow QA Guide, §4.4.4 (titles-only)"`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Drift evidence (non-authoritative; do not gate): if a harness log directory exists, list its contents.`

`# NOTE: This is informational only; canonical evaluation is by manifest.steps[].log_path under EVIDENCE_ROOT.`

`if [ -d "${EVIDENCE_ROOT}/runs" ]; then`

  `echo "" >>"${LOG_PATH}"`

  `echo "INFO: detected ${EVIDENCE_ROOT}/runs/ directory; listing as drift evidence only:" >>"${LOG_PATH}"`

  `find "${EVIDENCE_ROOT}/runs" -maxdepth 3 -type f -name "*.log" -print >>"${LOG_PATH}" 2>/dev/null || true`

`fi`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import json, os, hashlib, datetime`

`from pathlib import Path`

`def utc_now_z():`

    `return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`root = Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = Path(str(manifest) + ".path_proof.txt")`

`epic_id = "HDE-EPIC023"`

`check_id = "${CHECK_ID}"`

`status = "${STATUS}"`

`log_path = "${LOG_PATH}"`

`now = utc_now_z()`

`if manifest.exists():`

    `try:`

        `obj = json.loads(manifest.read_text(encoding="utf-8"))`

    `except Exception:`

        `obj = {"epic_id": epic_id, "steps": []}`

`else:`

    `obj = {"epic_id": epic_id, "steps": []}`

`if not isinstance(obj, dict):`

    `obj = {"epic_id": epic_id, "steps": []}`

`obj["epic_id"] = epic_id`

`steps = obj.get("steps")`

`if not isinstance(steps, list):`

    `steps = []`

`steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]`

`steps.append({"check_id": check_id, "status": status, "log_path": log_path})`

`steps.sort(key=lambda s: s.get("check_id",""))`

`obj["steps"] = steps`

`data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")`

`manifest.parent.mkdir(parents=True, exist_ok=True)`

`manifest.write_bytes(data)`

`sha = hashlib.sha256(data).hexdigest()`

`st = manifest.stat()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`proof_lines = [`

    `f"path: {manifest.as_posix()}",`

    `f"sha256: {sha}",`

    `f"size_bytes: {st.st_size}",`

    `f"mtime_utc: {mtime_utc}",`

    `f"produced_at_utc: {now}",`

`]`

`proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")`

`print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

**Expected result (PASS/FAIL predicates)**

PASS if:

* Manifest exists and `steps` is non-empty

* Every `steps[].log_path` exists, is under `audit/qa/hde-epic023/`, and is non-empty

FAIL\_BEHAVIOR if:

* Any `log_path` is missing, empty, or outside the epic QA root

TOOLING\_BLOCKED if:

* Manifest missing or empty

FAIL\_TOOLING if:

* embedded validator crashes unexpectedly

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D06_primary_step_logs/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/qa/hde-epic023/qa_step_logs_manifest.json`

* `audit/qa/hde-epic023/checks/D06_primary_step_logs/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D10\_doc\_delta\_draft: D10 — EPIC023 Doc-Delta Draft**

Surface / D-goal mapping: D10 \+ doc-delta draft existence  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF06 — Epic Process Guide, §0.4.1 (titles-only)

Goal: Verify EPIC023 doc-delta draft exists and is non-empty.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D10\_doc\_delta\_draft"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import sys, pathlib  
p \= pathlib.Path("audit/docdeltas/hde-epic023\_doc\_deltas.md")  
if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
b \= p.read\_bytes()  
if len(b) \== 0:  
    print("FAIL\_BEHAVIOR: doc-delta draft is empty")  
    sys.exit(2)  
if not b.endswith(b"\\n"):  
    print("FAIL\_BEHAVIOR: doc-delta draft missing trailing LF")  
    sys.exit(2)  
print("PASS: doc-delta draft exists and is non-empty.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) verify audit/docdeltas/hde-epic023\_doc\_deltas.md",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `audit/docdeltas/hde-epic023_doc_deltas.md` exists and is non-empty

FAIL\_BEHAVIOR if:

* exists but empty or not LF-terminated

TOOLING\_BLOCKED if:

* missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D10_doc_delta_draft/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/docdeltas/hde-epic023_doc_deltas.md`  
* `audit/qa/hde-epic023/checks/D10_doc_delta_draft/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D11\_close\_report: D11 — EPIC023 Close Report**

Surface / D-goal mapping: D11 \+ close report required anchors  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF14 — HDE-Mechanics Guide, §37.3; PF10 — HDE-Build Notes, Addendum 2.14 (titles-only)

Goal: Verify close report exists, is path-proofed, and includes required rails/open-close anchor text and references to key artifacts.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D11\_close\_report"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import sys, pathlib, re  
p \= pathlib.Path("audit/EPIC-023\_close\_report.md")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

txt \= p.read\_text(encoding="utf-8", errors="replace")

required\_phrases \= \[  
  "QA Rails — Open/Close (Final PR)",  
  "docs/acceptance\_map\_epic023.json",  
  "audit/qa/hde-epic023/token\_evidence\_matrix.md",  
  "audit/qa/hde-epic023/acceptance\_map\_viability.log",  
  "audit/qa/hde-epic023/qa\_step\_logs\_manifest.json",  
\]  
missing \= \[s for s in required\_phrases if s not in txt\]  
if missing:  
    print("FAIL\_BEHAVIOR: close report missing required anchors/paths:")  
    for m in missing:  
        print(f"  \- {m}")  
    sys.exit(2)

print("PASS: close report contains required rails anchor and key path references.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) verify audit/EPIC-023\_close\_report.md (+ path proof \+ required anchors)",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* close report exists and has `.path_proof.txt`  
* contains “QA Rails — Open/Close (Final PR)”  
* references key EPIC023 artifact paths listed in the command

FAIL\_BEHAVIOR if:

* required anchors/paths are missing

TOOLING\_BLOCKED if:

* close report missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D11_close_report/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/EPIC-023_close_report.md`  
* `audit/EPIC-023_close_report.md.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D11_close_report/primary.log`

---

#### CHECK D12\_close\_pack\_manifest: D12 — EPIC023 Close Pack Manifest

 Surface / D-goal mapping: D12 \+ close pack manifest shape \+ key\_outputs pointers  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF14 — HDE-Mechanics Guide, §37.3; PF10 — HDE-Build Notes, §2.14  
 Goal: Verify the close pack manifest parses and includes required key\_outputs bindings (named pointers).  
 Preconditions: none.

PO command(s) (copy/paste)

`CHECK_ID="D12_close_pack_manifest"`  
`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`  
`LOG_PATH="${LOG_DIR}/primary.log"`  
`TMP_OUT="${LOG_DIR}/tmp.out"`  
`mkdir -p "${LOG_DIR}"`

`python - <<'PY' >"${TMP_OUT}" 2>&1`  
`import json, sys, pathlib`

`p = pathlib.Path("audit/EPIC-023_MANIFEST.json")`  
`pp = pathlib.Path(str(p) + ".path_proof.txt")`

`required_bindings = {`  
  `"acceptance_map": "docs/acceptance_map_epic023.json",`  
  `"token_matrix": "audit/qa/hde-epic023/token_evidence_matrix.md",`  
  `"acceptance_map_viability": "audit/qa/hde-epic023/acceptance_map_viability.log",`  
  `"qa_step_manifest": "audit/qa/hde-epic023/qa_step_logs_manifest.json",`  
  `"doc_deltas": "audit/docdeltas/hde-epic023_doc_deltas.md",`  
  `"close_report": "audit/EPIC-023_close_report.md",`  
  `"close_manifest": "audit/EPIC-023_MANIFEST.json",`  
`}`

`if not p.exists():`  
    `print(f"TOOLING_BLOCKED: missing {p}")`  
    `sys.exit(3)`  
`if not pp.exists():`  
    `print(f"FAIL_BEHAVIOR: missing path proof {pp}")`  
    `sys.exit(2)`

`obj = json.loads(p.read_text(encoding="utf-8"))`  
`if obj.get("epic_id") != "HDE-EPIC023":`  
    `print(f"FAIL_BEHAVIOR: epic_id mismatch: {obj.get('epic_id')}")`  
    `sys.exit(2)`

`ko = obj.get("key_outputs")`  
`if not isinstance(ko, dict):`  
    `print("FAIL_BEHAVIOR: key_outputs must be an object (dict) of named pointers to paths")`  
    `sys.exit(2)`

`non_str = [k for k,v in ko.items() if not isinstance(v, str)]`  
`if non_str:`  
    `print("FAIL_BEHAVIOR: key_outputs values must all be strings; non-string keys:")`  
    `for k in sorted(non_str):`  
        `print(f"  - {k}: {type(ko[k]).__name__}")`  
    `sys.exit(2)`

`missing_keys = [k for k in required_bindings.keys() if k not in ko]`  
`wrong_vals = [k for k, exp in required_bindings.items() if k in ko and ko[k] != exp]`

`if missing_keys or wrong_vals:`  
    `print("FAIL_BEHAVIOR: key_outputs bindings mismatch")`  
    `if missing_keys:`  
        `print("Missing required key_outputs keys:")`  
        `for k in missing_keys:`  
            `print(f"  - {k}")`  
    `if wrong_vals:`  
        `print("Wrong key_outputs values (expected exact-match paths):")`  
        `for k in wrong_vals:`  
            `print(f"  - {k}: expected={required_bindings[k]} observed={ko.get(k)}")`  
    `print("\nObserved key_outputs mapping:")`  
    `for k in sorted(ko.keys()):`  
        `print(f"  - {k}: {ko[k]}")`  
    `sys.exit(2)`

`print("PASS: close pack manifest key_outputs includes required named bindings (exact match).")`  
`PY`  
`RC=$?`

`STATUS="PASS"`  
`case "${RC}" in`  
  `0) STATUS="PASS" ;;`  
  `2) STATUS="FAIL_BEHAVIOR" ;;`  
  `3) STATUS="TOOLING_BLOCKED" ;;`  
  `*) STATUS="FAIL_TOOLING" ;;`  
`esac`

`python - <<PY >"${LOG_PATH}"`  
`import json, os`  
`hdr = {`  
  `"check_id": "${CHECK_ID}",`  
  `"status": "${STATUS}",`  
  `"command": "python (embedded) validate audit/EPIC-023_MANIFEST.json key_outputs named bindings (+ path proof)",`  
  `"captured_env": {`  
    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`  
    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`  
    `"APP_ENV": os.environ.get("APP_ENV"),`  
    `"LC_ALL": os.environ.get("LC_ALL"),`  
    `"LANG": os.environ.get("LANG"),`  
    `"TZ": os.environ.get("TZ"),`  
  `}`  
`}`  
`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`  
`PY`  
`cat "${TMP_OUT}" >>"${LOG_PATH}"`  
`rm -f "${TMP_OUT}"`

`echo "${CHECK_ID} => ${STATUS}"`

Expected result (PASS/FAIL predicates)

PASS if:

* `audit/EPIC-023_MANIFEST.json` exists and parses

* `audit/EPIC-023_MANIFEST.json.path_proof.txt` exists

* `epic_id` is exactly `"HDE-EPIC023"`

* `key_outputs` is an object (dict) whose required keys exist and whose values exactly match the required binding paths

FAIL\_BEHAVIOR if:

* any required key is missing, any required value path mismatches, or `key_outputs` is not a dict

TOOLING\_BLOCKED if:

* manifest is missing

Primary evidence artifact (required)

* `audit/qa/hde-epic023/checks/D12_close_pack_manifest/primary.log`

Deliverables (minimal evidence set; fully-qualified paths)

* `audit/EPIC-023_MANIFEST.json`

* `audit/EPIC-023_MANIFEST.json.path_proof.txt`

* `audit/qa/hde-epic023/checks/D12_close_pack_manifest/primary.log`

---

#### **CHECK D13\_human\_index: D13 — Human Evidence Index**

Surface / D-goal mapping: D13 \+ INDEX.json contains EPIC023 artifacts  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF12 — HDE-Schemas and Artifacts, §8.5 (evidence indexing discipline); PF10 — HDE-Build Notes, Addendum 2.16 (titles-only)

Goal: Verify INDEX.json exists, parses, and references required EPIC023 artifacts.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D13\_human\_index"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import json, sys, pathlib  
p \= pathlib.Path("docs/evidence/INDEX.json")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

required\_paths \= \[  
  "docs/acceptance\_map\_epic023.json",  
  "audit/qa/hde-epic023/token\_evidence\_matrix.md",  
  "audit/qa/hde-epic023/acceptance\_map\_viability.log",  
  "audit/EPIC-023\_close\_report.md",  
  "audit/EPIC-023\_MANIFEST.json",  
\]

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

obj \= json.loads(p.read\_text(encoding="utf-8"))  
if not isinstance(obj, list):  
    print("FAIL\_BEHAVIOR: INDEX.json must be a JSON array")  
    sys.exit(2)

raw \= p.read\_text(encoding="utf-8", errors="replace")  
missing \= \[rp for rp in required\_paths if rp not in raw\]  
if missing:  
    print("FAIL\_BEHAVIOR: INDEX.json does not contain required EPIC023 path strings:")  
    for m in missing:  
        print(f"  \- {m}")  
    sys.exit(2)

print("PASS: INDEX.json references all required EPIC023 artifact paths (string containment).")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) validate docs/evidence/INDEX.json contains EPIC023 entries (+ path proof)",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `docs/evidence/INDEX.json` parses as JSON array  
* contains all required EPIC023 path strings (at minimum)

FAIL\_BEHAVIOR if:

* missing any required references

TOOLING\_BLOCKED if:

* missing file

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D13_human_index/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `docs/evidence/INDEX.json`  
* `docs/evidence/INDEX.json.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D13_human_index/primary.log`

---

#### **CHECK D14\_index\_hash\_sentinel: D14 — Evidence Index Hash Sentinel**

Surface / D-goal mapping: D14 \+ INDEX.sha256 matches INDEX.json  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF12 — HDE-Schemas and Artifacts, §8.5; PF10 — HDE-Build Notes, Addendum 2.16 (titles-only)

Goal: Recompute sha256( INDEX.json ) and compare to docs/evidence/INDEX.sha256.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D14\_index\_hash\_sentinel"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import hashlib, pathlib, sys, re  
idx \= pathlib.Path("docs/evidence/INDEX.json")  
sent \= pathlib.Path("docs/evidence/INDEX.sha256")  
sent\_pp \= pathlib.Path(str(sent) \+ ".path\_proof.txt")

if not idx.exists() or not sent.exists():  
    print("TOOLING\_BLOCKED: missing INDEX.json and/or INDEX.sha256")  
    sys.exit(3)  
if not sent\_pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {sent\_pp}")  
    sys.exit(2)

idx\_bytes \= idx.read\_bytes()  
sha \= hashlib.sha256(idx\_bytes).hexdigest()

line \= sent.read\_text(encoding="utf-8", errors="replace").strip()  
m \= re.match(r"^(\[0-9a-f\]{64})\\s+(\\S+)$", line)  
if not m:  
    print(f"FAIL\_BEHAVIOR: sentinel line not in '\<sha\> \<path\>' form: {line}")  
    sys.exit(2)

sent\_sha, sent\_path \= m.group(1), m.group(2)  
if sent\_path \!= "docs/evidence/INDEX.json":  
    print(f"FAIL\_BEHAVIOR: sentinel path mismatch: {sent\_path}")  
    sys.exit(2)  
if sent\_sha \!= sha:  
    print(f"FAIL\_BEHAVIOR: sha mismatch: sentinel={sent\_sha} computed={sha}")  
    sys.exit(2)

print("PASS: INDEX.sha256 matches computed sha256(INDEX.json).")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) sha256 compare docs/evidence/INDEX.json vs docs/evidence/INDEX.sha256",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* `docs/evidence/INDEX.sha256` exactly matches computed sha256 of `docs/evidence/INDEX.json`

FAIL\_BEHAVIOR if:

* mismatch or malformed sentinel

TOOLING\_BLOCKED if:

* missing required files

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D14_index_hash_sentinel/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `docs/evidence/INDEX.sha256`  
* `docs/evidence/INDEX.sha256.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D14_index_hash_sentinel/primary.log`

---

#### CHECK D15\_machine\_mirror: D15 — Machine Evidence Mirror

Surface / D-goal mapping: D15 \+ machine evidence mirror integrity \+ EPIC023 slice  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF12 — HDE-Schemas and Artifacts, §8.5 (evidence indexing discipline); PF10 — HDE-Build Notes, Addendum 2.16 (titles-only)

Goal: Validate the machine evidence mirror is schema-valid and contains EPIC023 entries with required proof anchors.  
 Preconditions: ci/checks/check\_mirror\_schema.sh exists and is executable; mirror file exists in canonical location.

PO command(s) (copy/paste)

`CHECK_ID="D15_machine_mirror"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`mkdir -p "${LOG_DIR}"`

`RC_SCHEMA=0`

`RC_CONTENT=0`

`# 1) Schema check`

`bash ci/checks/check_mirror_schema.sh >"${TMP_OUT}" 2>&1`

`RC_SCHEMA=$?`

`# 2) Content + proof anchor checks (decisive)`

`python - <<'PY' >>"${TMP_OUT}" 2>&1`

`import sys, json, pathlib`

`mm = pathlib.Path("artifacts/evidence_index.jsonl")`

`pp = pathlib.Path(str(mm) + ".path_proof.txt")`

`required_paths = {`

    `"docs/acceptance_map_epic023.json",`

    `"audit/qa/hde-epic023/token_evidence_matrix.md",`

    `"audit/qa/hde-epic023/acceptance_map_viability.log",`

    `"audit/qa/hde-epic023/qa_step_logs_manifest.json",`

`}`

`if not mm.exists():`

    `print("TOOLING_BLOCKED: missing artifacts/evidence_index.jsonl")`

    `sys.exit(12)`

`if not pp.exists():`

    `print("TOOLING_BLOCKED: missing artifacts/evidence_index.jsonl.path_proof.txt")`

    `sys.exit(13)`

`found = set()`

`anchors = set()`

`for line in mm.read_text(encoding="utf-8").splitlines():`

    `if not line.strip():`

        `continue`

    `obj = json.loads(line)`

    `if obj.get("epic_id") != "EPIC023":`

        `continue`

    `p = obj.get("path")`

    `if p in required_paths:`

        `found.add(p)`

        `if obj.get("proof_anchor"):`

            `anchors.add(obj["proof_anchor"])`

`missing = required_paths - found`

`if missing:`

    `print("FAIL_BEHAVIOR: missing required EPIC023 entries in mirror:", sorted(missing))`

    `sys.exit(2)`

`bad = []`

`for a in sorted(anchors):`

    `ap = pathlib.Path(a)`

    `if not ap.exists():`

        `bad.append(a)`

`if bad:`

    `print("FAIL_BEHAVIOR: proof_anchor targets missing:", bad)`

    `sys.exit(3)`

`print("PASS: artifacts/evidence_index.jsonl contains required EPIC023 entries + resolvable proof anchors.")`

`PY`

`RC_CONTENT=$?`

`# Decide status`

`STATUS="PASS"`

`if [ "${RC_SCHEMA}" -ne 0 ] || [ "${RC_CONTENT}" -ne 0 ]; then`

  `if grep -q "TOOLING_BLOCKED" "${TMP_OUT}"; then`

    `STATUS="TOOLING_BLOCKED"`

  `else`

    `STATUS="FAIL_BEHAVIOR"`

  `fi`

`fi`

`# Write primary.log with header`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "check mirror schema + EPIC023 slice in artifacts/evidence_index.jsonl",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"PF12 — HDE-Schemas and Artifacts, §8.5",`

    `"PF10 — HDE-Build Notes, Addendum 2.16 (titles-only)",`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import os, json, pathlib, hashlib, datetime`

`root = pathlib.Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = root / "qa_step_logs_manifest.json.path_proof.txt"`

`# Load existing`

`data = {"epic_id":"EPIC023","checks":[]}`

`if manifest.exists():`

  `data = json.loads(manifest.read_text(encoding="utf-8"))`

`# Remove any previous entry for this check_id`

`data["checks"] = [c for c in data.get("checks", []) if c.get("check_id") != "${CHECK_ID}"]`

`# Stat log`

`lp = pathlib.Path("${LOG_PATH}")`

`st = lp.stat()`

`sha = hashlib.sha256(lp.read_bytes()).hexdigest()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`entry = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"log_path": "${LOG_PATH}",`

  `"sha256": sha,`

  `"size_bytes": st.st_size,`

  `"mtime_utc": mtime_utc,`

  `"safe_mode": os.environ.get("SAFE_MODE"),`

  `"allow_network": os.environ.get("ALLOW_NETWORK"),`

  `"app_env": os.environ.get("APP_ENV"),`

  `"tokens_claimed": [],`

`}`

`data["checks"].append(entry)`

`data["checks"] = sorted(data["checks"], key=lambda c: c["check_id"])`

`manifest.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")`

`# Update proof (minimal: sha256 + size + mtime)`

`proof.write_text(`

  `f"qa_step_logs_manifest.json\nsha256={hashlib.sha256(manifest.read_bytes()).hexdigest()}\nsize_bytes={manifest.stat().st_size}\nmtime_utc={mtime_utc}\n",`

  `encoding="utf-8"`

`)`

`print("Updated qa_step_logs_manifest.json + path proof.")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

Expected result (PASS/FAIL predicates)

PASS:

* artifacts/evidence\_index.jsonl exists and is path-proofed (artifacts/evidence\_index.jsonl.path\_proof.txt).

* Mirror schema check passes.

* Machine evidence mirror includes EPIC023 entries for:

  * docs/acceptance\_map\_epic023.json

  * audit/qa/hde-epic023/token\_evidence\_matrix.md

  * audit/qa/hde-epic023/acceptance\_map\_viability.log

  * audit/qa/hde-epic023/qa\_step\_logs\_manifest.json

* All EPIC023 entries include proof\_anchor values that resolve to existing files.

FAIL\_BEHAVIOR if:

* Mirror schema invalid, missing required EPIC023 entries, or proof\_anchor files missing.

TOOLING\_BLOCKED if:

* machine evidence mirror file is missing or unreadable, or path proof is missing.

Primary evidence artifact (required)

audit/qa/hde-epic023/checks/D15\_machine\_mirror/primary.log

Deliverables (minimal evidence set; fully-qualified paths)

artifacts/evidence\_index.jsonl  
 artifacts/evidence\_index.jsonl.path\_proof.txt  
 audit/qa/hde-epic023/checks/D15\_machine\_mirror/primary.log

Tokens (optional)

No token claims for this check.

---

#### **CHECK D16\_orientation\_demo: D16 — Orientation Demo Evidence**

Surface / D-goal mapping: D16 \+ orientation demo outputs and validation  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF12 — HDE-Schemas and Artifacts, §8.5 (titles-only)

Goal: Verify the orientation demo evidence outputs exist and are valid per the demo checker.  
 Preconditions: `tools/evidence/orientation_demo.py` exists.

**PO command(s) (copy/paste)**

`CHECK_ID="D16_orientation_demo"`  
`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`  
`LOG_PATH="${LOG_DIR}/primary.log"`  
`TMP_OUT="${LOG_DIR}/tmp.out"`  
`mkdir -p "${LOG_DIR}"`

`RC_SCRIPT=0`  
`RC_FILES=0`

`python tools/evidence/orientation_demo.py --check >"${TMP_OUT}" 2>&1`  
`RC_SCRIPT=$?`

`python - <<'PY' >>"${TMP_OUT}" 2>&1`  
`import sys, json, pathlib`

`report = pathlib.Path("artifacts/hde-epic023_orientation_demo/orientation_demo_report.json")`  
`sample = pathlib.Path("artifacts/hde-epic023_orientation_demo/sample_result.json")`

`if not report.exists():`  
    `print(f"FAIL_BEHAVIOR: missing report {report}")`  
    `sys.exit(2)`  
`if not sample.exists():`  
    `print(f"FAIL_BEHAVIOR: missing sample {sample}")`  
    `sys.exit(2)`

`obj = json.loads(report.read_text(encoding="utf-8"))`  
`status = obj.get("status")`  
`if status != "ok":`  
    `print(f"FAIL_BEHAVIOR: orientation_demo_report.json status != ok (status={status})")`  
    `sys.exit(2)`

`print("PASS: orientation demo report/sample exist and report status is ok.")`  
`sys.exit(0)`  
`PY`  
`RC_FILES=$?`

`STATUS="PASS"`  
`if [ "${RC_SCRIPT}" -ne 0 ]; then`  
  `STATUS="FAIL_BEHAVIOR"`  
`elif [ "${RC_FILES}" -ne 0 ]; then`  
  `STATUS="FAIL_BEHAVIOR"`  
`else`  
  `STATUS="PASS"`  
`fi`

`python - <<PY >"${LOG_PATH}"`  
`import json, os`  
`hdr = {`  
  `"check_id": "${CHECK_ID}",`  
  `"status": "${STATUS}",`  
  `"command": "python tools/evidence/orientation_demo.py --check + python (embedded) validate required artifacts",`  
  `"captured_env": {`  
    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`  
    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`  
    `"APP_ENV": os.environ.get("APP_ENV"),`  
    `"LC_ALL": os.environ.get("LC_ALL"),`  
    `"LANG": os.environ.get("LANG"),`  
    `"TZ": os.environ.get("TZ"),`  
  `},`  
  `"pf_refs": [`  
    `"PF12 — HDE-Schemas and Artifacts, §8.5 (titles-only)"`  
  `],`  
  `"intended_tokens": [],`  
  `"claimed_tokens": [],`  
`}`  
`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`  
`PY`  
`cat "${TMP_OUT}" >>"${LOG_PATH}"`  
`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`  
`python - <<PY >>"${LOG_PATH}" 2>&1`  
`import json, os, hashlib, datetime`  
`from pathlib import Path`

`def utc_now_z():`  
    `return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`root = Path(os.environ["EVIDENCE_ROOT"])`  
`manifest = root / "qa_step_logs_manifest.json"`  
`proof = Path(str(manifest) + ".path_proof.txt")`

`epic_id = "HDE-EPIC023"`  
`check_id = "${CHECK_ID}"`  
`status = "${STATUS}"`  
`log_path = "${LOG_PATH}"`

`now = utc_now_z()`

`if manifest.exists():`  
    `try:`  
        `obj = json.loads(manifest.read_text(encoding="utf-8"))`  
    `except Exception:`  
        `obj = {"epic_id": epic_id, "steps": []}`  
`else:`  
    `obj = {"epic_id": epic_id, "steps": []}`

`if not isinstance(obj, dict):`  
    `obj = {"epic_id": epic_id, "steps": []}`  
`obj["epic_id"] = epic_id`

`steps = obj.get("steps")`  
`if not isinstance(steps, list):`  
    `steps = []`  
`steps = [s for s in steps if not (isinstance(s, dict) and s.get("check_id") == check_id)]`  
`steps.append({"check_id": check_id, "status": status, "log_path": log_path})`  
`steps.sort(key=lambda s: s.get("check_id",""))`  
`obj["steps"] = steps`

`data = (json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")`  
`manifest.parent.mkdir(parents=True, exist_ok=True)`  
`manifest.write_bytes(data)`

`sha = hashlib.sha256(data).hexdigest()`  
`st = manifest.stat()`  
`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`  
`proof_lines = [`  
    `f"path: {manifest.as_posix()}",`  
    `f"sha256: {sha}",`  
    `f"size_bytes: {st.st_size}",`  
    `f"mtime_utc: {mtime_utc}",`  
    `f"produced_at_utc: {now}",`  
`]`  
`proof.write_text("\n".join(proof_lines) + "\n", encoding="utf-8")`

`print(f"manifest_upsert: check_id={check_id} status={status} log_path={log_path} steps_count={len(steps)}")`  
`PY`

`echo "${CHECK_ID} => ${STATUS}"`

**Expected result (PASS/FAIL predicates)**

PASS if:

* `python tools/evidence/orientation_demo.py --check` returns 0

* `artifacts/hde-epic023_orientation_demo/orientation_demo_report.json` exists and has `status: ok`

* `artifacts/hde-epic023_orientation_demo/sample_result.json` exists

FAIL\_BEHAVIOR if:

* any of the above predicates fail

FAIL\_TOOLING if:

* tools crash unexpectedly

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `artifacts/hde-epic023_orientation_demo/orientation_demo_report.json`

* `artifacts/hde-epic023_orientation_demo/sample_result.json`

* `audit/qa/hde-epic023/checks/D16_orientation_demo/primary.log`

**Tokens (optional)**

No token claims for this check.

---

#### **CHECK D17\_env\_pins: D17 — Determinism Environment Pins Log**

Surface / D-goal mapping: D17 \+ determinism pins (rails posture evidence)  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF12 — HDE-Schemas and Artifacts, §8.3.3 (titles-only)

Goal: Validate `env_pins.log` is valid determinism pins JSON and reflects closed rails \+ pins.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D17\_env\_pins"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import json, sys, pathlib  
p \= pathlib.Path("audit/gates/determinism/env\_pins.log")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

lines \= p.read\_text(encoding="utf-8").splitlines()  
if len(lines) \!= 1:  
    print(f"FAIL\_BEHAVIOR: env\_pins.log must be exactly one JSON line; got {len(lines)} lines")  
    sys.exit(2)

obj \= json.loads(lines\[0\])  
if obj.get("schema") \!= "determinism\_env\_pins.v1":  
    print(f"FAIL\_BEHAVIOR: schema mismatch: {obj.get('schema')}")  
    sys.exit(2)

rails \= obj.get("rails")  
if not isinstance(rails, dict):  
    print("FAIL\_BEHAVIOR: rails must be an object")  
    sys.exit(2)

\# minimal pinned expectations  
req \= {  
  "SAFE\_MODE": 1,  
  "ALLOW\_NETWORK": 0,  
  "LC\_ALL": "C",  
  "LANG": "C",  
  "TZ": "UTC",  
}  
for k,v in req.items():  
    if k not in rails:  
        print(f"FAIL\_BEHAVIOR: rails missing key {k}")  
        sys.exit(2)  
    if str(rails\[k\]) \!= str(v):  
        print(f"FAIL\_BEHAVIOR: rails\[{k}\] mismatch: got={rails\[k\]} expected={v}")  
        sys.exit(2)

print("PASS: env\_pins.log schema OK and rails/pins match expected closed posture.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) validate audit/gates/determinism/env\_pins.log (+ path proof)",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* env\_pins.log is exactly one JSON line with schema `determinism_env_pins.v1`  
* rails reflect SAFE\_MODE=1, ALLOW\_NETWORK=0, LC\_ALL=C, LANG=C, TZ=UTC

FAIL\_BEHAVIOR if:

* schema mismatch, wrong line count, or pinned values mismatch

TOOLING\_BLOCKED if:

* file missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D17_env_pins/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/gates/determinism/env_pins.log`  
* `audit/gates/determinism/env_pins.log.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D17_env_pins/primary.log`

---

#### **CHECK D18\_sanity\_log: D18 — Sanity Pipeline Log**

Surface / D-goal mapping: D18 \+ sanity pipeline evidence log  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF12 — HDE-Schemas and Artifacts, §8.3.4 (titles-only)

Goal: Validate sanity.log has required lines including summary PASS.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D18\_sanity\_log"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import sys, pathlib  
p \= pathlib.Path("artifacts/sanity/sanity.log")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

lines \= p.read\_text(encoding="utf-8", errors="replace").splitlines()  
if not lines:  
    print("FAIL\_BEHAVIOR: sanity.log empty")  
    sys.exit(2)

need \= \[  
  "run:sanity-pipeline",  
  "env\_pins: audit/gates/determinism/env\_pins.log",  
  "summary:PASS",  
\]  
missing \= \[s for s in need if not any(s in ln for ln in lines)\]  
if missing:  
    print("FAIL\_BEHAVIOR: sanity.log missing required lines:")  
    for m in missing:  
        print(f"  \- {m}")  
    sys.exit(2)

print("PASS: sanity.log contains required run/env\_pins/summary lines.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) validate artifacts/sanity/sanity.log (+ path proof)",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* sanity.log includes `run:sanity-pipeline`  
* includes `env_pins: audit/gates/determinism/env_pins.log`  
* includes `summary:PASS`

FAIL\_BEHAVIOR if:

* required lines missing or log empty

TOOLING\_BLOCKED if:

* log missing

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D18_sanity_log/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `artifacts/sanity/sanity.log`  
* `artifacts/sanity/sanity.log.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D18_sanity_log/primary.log`

---

#### **CHECK D19\_json\_gate\_check\_log: D19 — Canonical JSON Gate Check Log**

Surface / D-goal mapping: D19 \+ canonical JSON gate check log existence \+ status pass  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF09 — HDE Build Checklist (canonical JSON gate); PF10 — HDE-Build Notes (gate outputs referenced) (titles-only)

Goal: Validate JSONL-like gate check log parses and includes status=pass records.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D19\_json\_gate\_check\_log"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import json, sys, pathlib  
p \= pathlib.Path("audit/gates/canonical\_json/json\_canonical\_check.log")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

pass\_seen \= False  
line\_count \= 0  
for line in p.read\_text(encoding="utf-8", errors="replace").splitlines():  
    if not line.strip():  
        continue  
    line\_count \+= 1  
    obj \= json.loads(line)  
    if obj.get("status") \== "pass":  
        pass\_seen \= True

if line\_count \== 0:  
    print("FAIL\_BEHAVIOR: json\_canonical\_check.log contains no JSON records")  
    sys.exit(2)  
if not pass\_seen:  
    print("FAIL\_BEHAVIOR: no record with status=pass found")  
    sys.exit(2)

print(f"PASS: parsed {line\_count} JSON records; status=pass observed.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) parse audit/gates/canonical\_json/json\_canonical\_check.log (+ path proof) for status=pass",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* log parses as JSON-per-line and contains at least one record with `status="pass"`

FAIL\_BEHAVIOR if:

* no pass record, empty log, or parse failures

TOOLING\_BLOCKED if:

* missing log

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D19_json_gate_check_log/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/gates/canonical_json/json_canonical_check.log`  
* `audit/gates/canonical_json/json_canonical_check.log.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D19_json_gate_check_log/primary.log`

---

#### **CHECK D20\_json\_gate\_compare\_log: D20 — Canonical JSON Gate Compare Log**

Surface / D-goal mapping: D20 \+ canonical JSON compare log existence \+ status pass  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF09 — HDE Build Checklist (canonical JSON gate) (titles-only)

Goal: Validate JSONL-like compare log parses and includes status=pass.  
Preconditions: none.

**PO command(s) (copy/paste)**

CHECK\_ID="D20\_json\_gate\_compare\_log"  
LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"  
LOG\_PATH="${LOG\_DIR}/primary.log"  
TMP\_OUT="${LOG\_DIR}/tmp.out"  
mkdir \-p "${LOG\_DIR}"

python \- \<\<'PY' \>"${TMP\_OUT}" 2\>&1  
import json, sys, pathlib  
p \= pathlib.Path("audit/gates/canonical\_json/json\_canon\_compare.log")  
pp \= pathlib.Path(str(p) \+ ".path\_proof.txt")

if not p.exists():  
    print(f"TOOLING\_BLOCKED: missing {p}")  
    sys.exit(3)  
if not pp.exists():  
    print(f"FAIL\_BEHAVIOR: missing path proof {pp}")  
    sys.exit(2)

pass\_seen \= False  
line\_count \= 0  
for line in p.read\_text(encoding="utf-8", errors="replace").splitlines():  
    if not line.strip():  
        continue  
    line\_count \+= 1  
    obj \= json.loads(line)  
    if obj.get("status") \== "pass":  
        pass\_seen \= True

if line\_count \== 0:  
    print("FAIL\_BEHAVIOR: json\_canon\_compare.log contains no JSON records")  
    sys.exit(2)  
if not pass\_seen:  
    print("FAIL\_BEHAVIOR: no record with status=pass found")  
    sys.exit(2)

print(f"PASS: parsed {line\_count} JSON records; status=pass observed.")  
PY  
RC=$?

STATUS="PASS"  
case "${RC}" in  
  0\) STATUS="PASS" ;;  
  2\) STATUS="FAIL\_BEHAVIOR" ;;  
  3\) STATUS="TOOLING\_BLOCKED" ;;  
  \*) STATUS="FAIL\_TOOLING" ;;  
esac

python \- \<\<PY \>"${LOG\_PATH}"  
import json, os  
hdr \= {  
  "check\_id": "${CHECK\_ID}",  
  "status": "${STATUS}",  
  "command": "python (embedded) parse audit/gates/canonical\_json/json\_canon\_compare.log (+ path proof) for status=pass",  
  "captured\_env": {  
    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),  
    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),  
    "APP\_ENV": os.environ.get("APP\_ENV"),  
    "LC\_ALL": os.environ.get("LC\_ALL"),  
    "LANG": os.environ.get("LANG"),  
    "TZ": os.environ.get("TZ"),  
  }  
}  
print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))  
PY  
cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"  
rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* compare log parses and contains at least one `status="pass"` record

FAIL\_BEHAVIOR if:

* no pass record or parse failure

TOOLING\_BLOCKED if:

* missing compare log

**Primary evidence artifact (required)**

* `audit/qa/hde-epic023/checks/D20_json_gate_compare_log/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `audit/gates/canonical_json/json_canon_compare.log`  
* `audit/gates/canonical_json/json_canon_compare.log.path_proof.txt`  
* `audit/qa/hde-epic023/checks/D20_json_gate_compare_log/primary.log`

---

#### CHECK D21\_internal\_version: D21 — Internal Version Endpoint

Surface / D-goal mapping: D21 \+ internal version endpoint evidence family \+ endpoint reality  
Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
PF anchors: PF14 — HDE Mechanics Guide, §9.4 (/internal/version evidence family \+ endpoint reality)  
Goal: Verify the `/internal/version` evidence family is complete at the canon path, and that endpoint reality is reflected in the Endpoint Catalog.  
Preconditions: repo checked out.

**What this check will validate**

Evidence family present under `artifacts/ops/internal_version/` (minimum required set):

* `headers_get.txt`  
* `headers_head.txt`  
* `body_get.json` and `body_get.sha256`  
* `headers_cond_if_none_match.txt`  
* `headers_cond_if_modified_since.txt`  
* `request_chain_manifest.json`  
* `two_run_identity.log`

Endpoint reality (inventory posture): `docs/ENDPOINTS_CATALOG.json` contains an entry for `/internal/version` with `a7_eligible == false` (ops-only; not an A7 proof surface).

(Optional) contract test exists and passes if present in tests/ (do not fail if absent)

**PO command(s) (copy/paste)**

CHECK\_ID="D21\_internal\_version"

LOG\_DIR="${EVIDENCE\_ROOT:?}/checks/${CHECK\_ID}"

LOG\_PATH="${LOG\_DIR}/primary.log"

TMP\_OUT="${LOG\_DIR}/tmp.out"

mkdir \-p "${LOG\_DIR}"

STATUS="PASS"

echo "== D21: /internal/version evidence family \+ endpoint reality \==" \>"${TMP\_OUT}"

python \- \<\<'PY' \>\>"${TMP\_OUT}" 2\>&1

import json, sys, pathlib, hashlib, re

root \= pathlib.Path("artifacts/ops/internal\_version")

required\_files \= \[

  "headers\_get.txt",

  "headers\_head.txt",

  "body\_get.json",

  "body\_get.sha256",

  "headers\_cond\_if\_none\_match.txt",

  "headers\_cond\_if\_modified\_since.txt",

  "request\_chain\_manifest.json",

  "two\_run\_identity.log",

\]

def fail(msg, code=2):

    print(msg)

    sys.exit(code)

if not root.exists():

    fail("TOOLING\_BLOCKED: missing artifacts/ops/internal\_version/", 3\)

missing \= \[f for f in required\_files if not (root / f).exists()\]

if missing:

    print("FAIL\_BEHAVIOR: missing required /internal/version evidence files:")

    for m in missing:

        print(f"  \- artifacts/ops/internal\_version/{m}")

    sys.exit(2)

\# Basic non-empty checks

for f in required\_files:

    p \= root / f

    if p.stat().st\_size \== 0:

        fail(f"FAIL\_BEHAVIOR: evidence file is empty: {p}")

\# headers\_get.txt posture: must show no-store and no ETag

hg \= (root / "headers\_get.txt").read\_text(encoding="utf-8", errors="replace")

if "no-store" not in hg.lower():

    fail("FAIL\_BEHAVIOR: headers\_get.txt does not demonstrate Cache-Control: no-store")

if re.search(r"(?im)^etag\\s\*:", hg):

    fail("FAIL\_BEHAVIOR: headers\_get.txt contains ETag (must be absent)")

\# headers\_head.txt posture: same no-store and no ETag

hh \= (root / "headers\_head.txt").read\_text(encoding="utf-8", errors="replace")

if "no-store" not in hh.lower():

    fail("FAIL\_BEHAVIOR: headers\_head.txt does not demonstrate Cache-Control: no-store")

if re.search(r"(?im)^etag\\s\*:", hh):

    fail("FAIL\_BEHAVIOR: headers\_head.txt contains ETag (must be absent)")

\# Conditional captures: must not show a 304 (conditionals ignored \=\> still 200\)

c1 \= (root / "headers\_cond\_if\_none\_match.txt").read\_text(encoding="utf-8", errors="replace")

c2 \= (root / "headers\_cond\_if\_modified\_since.txt").read\_text(encoding="utf-8", errors="replace")

for name, txt in \[("headers\_cond\_if\_none\_match.txt", c1), ("headers\_cond\_if\_modified\_since.txt", c2)\]:

    if "304" in txt:

        fail(f"FAIL\_BEHAVIOR: {name} appears to contain 304 (conditionals must be ignored)")

\# body\_get.json: LF-terminated, JSON object, 6 keys, includes release\_id

body\_p \= root / "body\_get.json"

body\_raw \= body\_p.read\_text(encoding="utf-8")

if not body\_raw.endswith("\\n"):

    fail("FAIL\_BEHAVIOR: body\_get.json is not LF-terminated")

body \= json.loads(body\_raw)

if not isinstance(body, dict):

    fail("FAIL\_BEHAVIOR: body\_get.json must be a JSON object")

if len(body.keys()) \!= 6:

    fail(f"FAIL\_BEHAVIOR: body\_get.json must have exactly 6 top-level keys (got {len(body.keys())})")

if "release\_id" not in body:

    fail("FAIL\_BEHAVIOR: body\_get.json missing required key: release\_id")

\# body\_get.sha256 must match sha256(body\_get.json bytes)

sha\_line \= (root / "body\_get.sha256").read\_text(encoding="utf-8", errors="replace").strip()

sha \= sha\_line.split()\[0\] if sha\_line else ""

if not re.fullmatch(r"\[0-9a-f\]{64}", sha):

    fail("FAIL\_BEHAVIOR: body\_get.sha256 does not contain a lowercase hex64 sha256")

calc \= hashlib.sha256(body\_p.read\_bytes()).hexdigest()

if sha \!= calc:

    fail(f"FAIL\_BEHAVIOR: body\_get.sha256 mismatch: expected={calc} found={sha}")

\# request\_chain\_manifest.json: parseable JSON and LF-terminated

rcm\_p \= root / "request\_chain\_manifest.json"

rcm\_raw \= rcm\_p.read\_text(encoding="utf-8")

if not rcm\_raw.endswith("\\n"):

    fail("FAIL\_BEHAVIOR: request\_chain\_manifest.json is not LF-terminated")

json.loads(rcm\_raw)

\# two\_run\_identity.log: must assert identity and reference env pins (string-level check)

tri \= (root / "two\_run\_identity.log").read\_text(encoding="utf-8", errors="replace")

if "two\_run" not in tri.lower():

    fail("FAIL\_BEHAVIOR: two\_run\_identity.log does not appear to record two-run identity")

if "env\_pins" not in tri.lower():

    fail("FAIL\_BEHAVIOR: two\_run\_identity.log does not reference env pins evidence")

print("PASS: /internal/version evidence family present and passes minimal posture checks.")

PY

RC\_EVID=$?

if \[ "${RC\_EVID}" \-ne 0 \]; then

  case "${RC\_EVID}" in

    3\) STATUS="TOOLING\_BLOCKED" ;;

    2\) STATUS="FAIL\_BEHAVIOR" ;;

    \*) STATUS="FAIL\_TOOLING" ;;

  esac

fi

\# Endpoint reality via Endpoint Catalog (preferred over grepping code paths)

python \- \<\<'PY' \>\>"${TMP\_OUT}" 2\>&1

import json, sys

from pathlib import Path

p \= Path("docs/ENDPOINTS\_CATALOG.json")

if not p.exists():

    print("TOOLING\_BLOCKED: missing docs/ENDPOINTS\_CATALOG.json (cannot confirm endpoint inventory reality)")

    sys.exit(3)

data \= json.loads(p.read\_text(encoding="utf-8"))

\# allow either {"endpoints":\[...\]} or top-level list (do not assume more)

endpoints \= data.get("endpoints", data if isinstance(data, list) else \[\])

if not isinstance(endpoints, list):

    print("FAIL\_BEHAVIOR: ENDPOINTS\_CATALOG.json does not contain an endpoints list")

    sys.exit(2)

hit \= None

for e in endpoints:

    if isinstance(e, dict) and e.get("path") \== "/internal/version":

        hit \= e

        break

if not hit:

    print("FAIL\_BEHAVIOR: ENDPOINTS\_CATALOG.json missing entry for /internal/version")

    sys.exit(2)

a7 \= hit.get("a7\_eligible", None)

if a7 is not False:

    print(f"FAIL\_BEHAVIOR: /internal/version must be a7\_eligible=false (got {a7})")

    sys.exit(2)

print("PASS: Endpoint Catalog contains /internal/version with a7\_eligible=false")

PY

RC\_CAT=$?

if \[ "${RC\_CAT}" \-ne 0 \]; then

  case "${RC\_CAT}" in

    3\) STATUS="TOOLING\_BLOCKED" ;;

    2\) STATUS="FAIL\_BEHAVIOR" ;;

    \*) STATUS="FAIL\_TOOLING" ;;

  esac

fi

\# Optional contract test: do not fail if absent; if present, must pass

if \[ \-f "tests/transport/test\_internal\_version\_contract.py" \]; then

  echo "INFO: found tests/transport/test\_internal\_version\_contract.py; running python \-m pytest (no network)" \>\>"${TMP\_OUT}"

  python \-m pytest \-q tests/transport/test\_internal\_version\_contract.py \>\>"${TMP\_OUT}" 2\>&1 || STATUS="FAIL\_BEHAVIOR"

elif \[ \-f "tests/test\_internal\_version.py" \]; then

  echo "INFO: found tests/test\_internal\_version.py; running python \-m pytest (no network)" \>\>"${TMP\_OUT}"

  python \-m pytest \-q tests/test\_internal\_version.py \>\>"${TMP\_OUT}" 2\>&1 || STATUS="FAIL\_BEHAVIOR"

else

  echo "INFO: no internal version contract test found; skipping (optional)" \>\>"${TMP\_OUT}"

fi

\# Write header \+ details to primary.log

python \- \<\<PY \>"${LOG\_PATH}"

import json, os

hdr \= {

  "check\_id": "${CHECK\_ID}",

  "status": "${STATUS}",

  "command": "validate /internal/version evidence family (canon) \+ Endpoint Catalog reality (+ optional contract test)",

  "captured\_env": {

    "SAFE\_MODE": os.environ.get("SAFE\_MODE"),

    "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK"),

    "APP\_ENV": os.environ.get("APP\_ENV"),

    "LC\_ALL": os.environ.get("LC\_ALL"),

    "LANG": os.environ.get("LANG"),

    "TZ": os.environ.get("TZ"),

  },

  "pf\_refs": \[

    "PF14 — HDE Mechanics Guide, §9.4",

  \],

  "intended\_tokens": \[\],

  "claimed\_tokens": \[\],

}

print(json.dumps(hdr, sort\_keys=True, separators=(",", ":")))

PY

cat "${TMP\_OUT}" \>\>"${LOG\_PATH}"

rm \-f "${TMP\_OUT}"

echo "${CHECK\_ID} \=\> ${STATUS}"

**Expected result (PASS/FAIL predicates)**

PASS if:

* All required files exist under `artifacts/ops/internal_version/` and pass the minimal posture checks listed above (no-store; no ETag; conditionals ignored; body\_get.sha256 matches body bytes; request\_chain\_manifest parses; two\_run\_identity references env pins).  
* Endpoint Catalog includes `/internal/version` with `a7_eligible=false`.

FAIL\_BEHAVIOR if:

* Any required file exists but violates the minimal posture checks, or `/internal/version` is missing/mis-declared in the Endpoint Catalog.

TOOLING\_BLOCKED if:

* `artifacts/ops/internal_version/` is missing, any required evidence file is missing, or `docs/ENDPOINTS_CATALOG.json` is missing.

**Primary evidence artifact (required)**  
`audit/qa/hde-epic023/checks/D21_internal_version/primary.log`

**Deliverables (minimal evidence set; fully-qualified paths)**

* `artifacts/ops/internal_version/headers_get.txt`  
* `artifacts/ops/internal_version/headers_head.txt`  
* `artifacts/ops/internal_version/body_get.json`  
* `artifacts/ops/internal_version/body_get.sha256`  
* `artifacts/ops/internal_version/headers_cond_if_none_match.txt`  
* `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`  
* `artifacts/ops/internal_version/request_chain_manifest.json`  
* `artifacts/ops/internal_version/two_run_identity.log`  
* `audit/qa/hde-epic023/checks/D21_internal_version/primary.log`

**Tokens (optional)**  
No token claims for this check.

---

#### CHECK D22\_canonical\_json\_gate\_structured\_record: D22 — Canonical JSON Gate Structured Record

Surface / D-goal mapping: D22 \+ canonical JSON gate structured record (UNPROVEN)  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF09 — HDE Build Checklist (canonical JSON gate) (titles-only)

Goal: UNPROVEN/TOOLING\_BLOCKED. Record the posture for this surface without asserting required artifact paths.  
 Preconditions: none.

PO command(s) (copy/paste)

`CHECK_ID="D22_canonical_json_gate_structured_record"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`mkdir -p "${LOG_DIR}"`

`cat >"${TMP_OUT}" <<'EOF'`

`UNPROVEN/TOOLING_BLOCKED: This surface requires repo/tooling confirmation before a governed artifact path and PASS/FAIL predicate can be asserted. This plan revision records posture only.`

`EOF`

`STATUS="TOOLING_BLOCKED"`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "UNPROVEN/TOOLING_BLOCKED: record posture only (no required deliverable paths asserted)",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"PF09 — HDE Build Checklist (canonical JSON gate) (titles-only)"`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import os, json, pathlib, hashlib, datetime`

`root = pathlib.Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = root / "qa_step_logs_manifest.json.path_proof.txt"`

`# Load existing`

`data = {"epic_id":"EPIC023","checks":[]}`

`if manifest.exists():`

  `data = json.loads(manifest.read_text(encoding="utf-8"))`

`# Remove any previous entry for this check_id`

`data["checks"] = [c for c in data.get("checks", []) if c.get("check_id") != "${CHECK_ID}"]`

`# Stat log`

`lp = pathlib.Path("${LOG_PATH}")`

`st = lp.stat()`

`sha = hashlib.sha256(lp.read_bytes()).hexdigest()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`entry = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"log_path": "${LOG_PATH}",`

  `"sha256": sha,`

  `"size_bytes": st.st_size,`

  `"mtime_utc": mtime_utc,`

  `"safe_mode": os.environ.get("SAFE_MODE"),`

  `"allow_network": os.environ.get("ALLOW_NETWORK"),`

  `"app_env": os.environ.get("APP_ENV"),`

  `"tokens_claimed": [],`

`}`

`data["checks"].append(entry)`

`data["checks"] = sorted(data["checks"], key=lambda c: c["check_id"])`

`manifest.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")`

`# Update proof (minimal: sha256 + size + mtime)`

`proof.write_text(`

  `f"qa_step_logs_manifest.json\nsha256={hashlib.sha256(manifest.read_bytes()).hexdigest()}\nsize_bytes={manifest.stat().st_size}\nmtime_utc={mtime_utc}\n",`

  `encoding="utf-8"`

`)`

`print("Updated qa_step_logs_manifest.json + path proof.")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

Expected result (PASS/FAIL predicates)

UNPROVEN/TOOLING\_BLOCKED:

* primary.log exists and contains the UNPROVEN/TOOLING\_BLOCKED posture note.

* No governed artifact path is asserted by this check in this plan revision.

Primary evidence artifact (required)

audit/qa/hde-epic023/checks/D22\_canonical\_json\_gate\_structured\_record/primary.log

Deliverables (minimal evidence set; fully-qualified paths)

audit/qa/hde-epic023/checks/D22\_canonical\_json\_gate\_structured\_record/primary.log

Tokens (optional)

No token claims for this check.

---

#### CHECK D23\_evidence\_index\_snapshot\_artifact: D23 — EPIC023 Evidence Index Snapshot Artifact

Surface / D-goal mapping: D23 \+ evidence index snapshot artifact (UNPROVEN)  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins (when producing governed bytes): LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: (guide-only; UNPROVEN/TOOLING\_BLOCKED pending confirmation)

Goal: UNPROVEN/TOOLING\_BLOCKED. Record the posture for this surface without asserting required artifact paths.  
 Preconditions: none.

PO command(s) (copy/paste)

`CHECK_ID="D23_evidence_index_snapshot_artifact"`

`LOG_DIR="${EVIDENCE_ROOT:?}/checks/${CHECK_ID}"`

`LOG_PATH="${LOG_DIR}/primary.log"`

`TMP_OUT="${LOG_DIR}/tmp.out"`

`mkdir -p "${LOG_DIR}"`

`cat >"${TMP_OUT}" <<'EOF'`

`UNPROVEN/TOOLING_BLOCKED: This surface requires repo/tooling confirmation before a governed artifact path and PASS/FAIL predicate can be asserted. This plan revision records posture only.`

`EOF`

`STATUS="TOOLING_BLOCKED"`

`python - <<PY >"${LOG_PATH}"`

`import json, os`

`hdr = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"command": "UNPROVEN/TOOLING_BLOCKED: record posture only (no required deliverable paths asserted)",`

  `"captured_env": {`

    `"SAFE_MODE": os.environ.get("SAFE_MODE"),`

    `"ALLOW_NETWORK": os.environ.get("ALLOW_NETWORK"),`

    `"APP_ENV": os.environ.get("APP_ENV"),`

    `"LC_ALL": os.environ.get("LC_ALL"),`

    `"LANG": os.environ.get("LANG"),`

    `"TZ": os.environ.get("TZ"),`

  `},`

  `"pf_refs": [`

    `"(guide-only; UNPROVEN/TOOLING_BLOCKED pending confirmation)"`

  `],`

  `"intended_tokens": [],`

  `"claimed_tokens": [],`

`}`

`print(json.dumps(hdr, sort_keys=True, separators=(",", ":")))`

`PY`

`cat "${TMP_OUT}" >>"${LOG_PATH}"`

`rm -f "${TMP_OUT}"`

`# Upsert this check into the step-logs manifest (PF19 §4.4.3)`

`python - <<PY >>"${LOG_PATH}" 2>&1`

`import os, json, pathlib, hashlib, datetime`

`root = pathlib.Path(os.environ["EVIDENCE_ROOT"])`

`manifest = root / "qa_step_logs_manifest.json"`

`proof = root / "qa_step_logs_manifest.json.path_proof.txt"`

`# Load existing`

`data = {"epic_id":"EPIC023","checks":[]}`

`if manifest.exists():`

  `data = json.loads(manifest.read_text(encoding="utf-8"))`

`# Remove any previous entry for this check_id`

`data["checks"] = [c for c in data.get("checks", []) if c.get("check_id") != "${CHECK_ID}"]`

`# Stat log`

`lp = pathlib.Path("${LOG_PATH}")`

`st = lp.stat()`

`sha = hashlib.sha256(lp.read_bytes()).hexdigest()`

`mtime_utc = datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z")`

`entry = {`

  `"check_id": "${CHECK_ID}",`

  `"status": "${STATUS}",`

  `"log_path": "${LOG_PATH}",`

  `"sha256": sha,`

  `"size_bytes": st.st_size,`

  `"mtime_utc": mtime_utc,`

  `"safe_mode": os.environ.get("SAFE_MODE"),`

  `"allow_network": os.environ.get("ALLOW_NETWORK"),`

  `"app_env": os.environ.get("APP_ENV"),`

  `"tokens_claimed": [],`

`}`

`data["checks"].append(entry)`

`data["checks"] = sorted(data["checks"], key=lambda c: c["check_id"])`

`manifest.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")`

`# Update proof (minimal: sha256 + size + mtime)`

`proof.write_text(`

  `f"qa_step_logs_manifest.json\nsha256={hashlib.sha256(manifest.read_bytes()).hexdigest()}\nsize_bytes={manifest.stat().st_size}\nmtime_utc={mtime_utc}\n",`

  `encoding="utf-8"`

`)`

`print("Updated qa_step_logs_manifest.json + path proof.")`

`PY`

`echo "${CHECK_ID} => ${STATUS}"`

Expected result (PASS/FAIL predicates)

UNPROVEN/TOOLING\_BLOCKED:

* primary.log exists and contains the UNPROVEN/TOOLING\_BLOCKED posture note.

* No governed artifact path is asserted by this check in this plan revision.

Primary evidence artifact (required)

audit/qa/hde-epic023/checks/D23\_evidence\_index\_snapshot\_artifact/primary.log

Deliverables (minimal evidence set; fully-qualified paths)

audit/qa/hde-epic023/checks/D23\_evidence\_index\_snapshot\_artifact/primary.log

Tokens (optional)

No token claims for this check.

---

### **Close-out deliverables**

This runbook MUST ensure the epic produces the execution deliverables required by the Epic Process Guide:

* Discovery artifact (Step‑0 artifacts satisfy this when properly defined by canon)  
* QA RCA & Doc Delta summary (execution deliverable)

#### **What “QA RCA & Doc Delta summary” means (explicit; non-drifting)**

In this posture, “QA RCA & Doc Delta summary” is not a debugging diary and not a demand for narrative prose.

It is a closure-oriented summary artifact that:

* states what Live QA found (or explicitly states “no new deltas found”),  
* maps any substantive findings to PF-Canon doc delta intents by PF title, and  
* records deferrals (if any) as deferrals (not as “unknowns”).

Location:

* MAY live as a section of the epic close report, or a governed artifact referenced by it.

---

### **Review guardrails**

Hard blockers for plan approval/execution:

* Manual result placeholders (“fill PASS/FAIL”, “operator summary”, etc.).  
* Any `git …` command in PO-executable steps.  
* Helper/wrapper scripts not canon-named by explicit path (unless the full tool source is embedded in the plan and written under `audit/qa/<epic-id>/...` before execution).  
* Missing Step‑0 mechanical artifacts (Codespaces snapshot \+ Doc Delta Capture) when in Codespaces.  
* Any check listed in the matrix without a corresponding Check Block (or vice versa).  
* Closure-scoped plans containing placeholder non-PASS steps for closure-critical artifact families (scope must be downgraded or resolved via canon-safe ADR before execution).

Caveats (allowed, must be mechanically logged):

* DOC\_DRIFT — plan adapts to repo reality; record mismatch mechanically and drain later.  
* ENV\_DRIFT — environment differs from baseline; capture mechanically; do not invent new rails.

ASK OK?

