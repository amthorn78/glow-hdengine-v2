## 1\) Live QA Plan

### Front matter

Epic ID: HDE-EPIC029   
Plan type: Live QA Plan / Runbook   
Execution venue: Codespaces   
Target environment: dev   
Plan revision: r5   
Date (UTC): 2026-04-15   
Operators (names-only): PO, QA agent

#### Canon precedence statement (required)

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

Canon set (titles-only, names-only, no version numbers in prose):

* PF10 — HDE-Build Notes, relevant addenda 2.2, 2.20, and 2.21  
* PF04 — HDE-Governance, §2.0 Acceptance Tokens  
* PF05 — HDE CLI/API Vendor Reference, §5.6 Endpoint Catalog (JSON success); §5.11 Dev sampler HTTP harness (dev/admin-only); §A.3 Writers and errors  
* PF06 — Epic Process Guide, §0.4.1 Live QA discovery and RCA  
* PF09.4 — HDE Build Checklist Conjunction, HDE-CONJ001.4; HDE-CONJ008.1; HDE-CONJ009.1  
* PF12 — HDE Schemas and Artifacts, Epic QA harness ledger artifacts; Canonical epic QA root; Invariant required outputs  
* PF19 — Glow QA Guide, §3.5.4 Artifact-first Live QA pattern (behavior vs artifacts)  
* PF27 — Canon Plan Templates, §1) Live QA Plan; Check-centric, single-root evidence posture (normative); Step-log header schema expectations (minimum; required); Template-safe placeholders and ellipsis prohibition (hard)

### Scope statement

SOURCE EXCERPT (verbatim):

"This epic is a bounded Conjunction closeout slice focused on three remaining integration areas: canonical JSON discipline, writer posture, and dev/internal harness closure." "The implemented work stays on existing surfaces and is not meant to create a new public surface." "The writer work is about preserving the existing development-only writer behavior with strict envelope posture, not widening it into a public or formal transport-proof surface." "The dev sampler work is about truthful non-production binding closure and environment coverage, not about inventing a new route or a new environment model."

This plan evaluates the following in-scope surfaces / checks:

* PO-001 — Bounded Conjunction closeout slice / no new public surface  
* PO-002 — Canonical JSON discipline across the bounded Conjunction slice  
* PO-003 — Existing dev writer posture remains typed, numeric-free, and outside formal transport proofs  
* PO-004 — Internal sampler harness remains dev/admin-only and refuses prod or misconfigured use  
* PO-005 — Published dev sampler binding closes both intended development environments truthfully  
* PO-006 — Formal transport proof surface remains only the cataloged Reader success surface  
* PO-007 — At least one real functional harness proof exists and passes  
* PO-008 — Final closeout records stay on one bounded acceptance surface and are backed by real passing QA evidence

This plan explicitly excludes:

* any new public route  
* any writer widening into a formal transport-proof surface  
* any new environment model  
* any new acceptance-token names  
* any PF document edits  
* any branch / PR / merge workflow actions

#### PF10 overrides / conflicts (if any)

* PF10 Addendum 2.2 — temporary token registry bridge — allows TESTS\_PASS\_OK, QA\_PRECOMMIT\_CHECKLIST\_OK, and QA\_POSTCOMMIT\_CHECKLIST\_OK to be used in epic-close acceptance artifacts when bound to truthful governed evidence — impacts epic-close token binding only. PF10 — HDE-Build Notes, §2.2) HDE-EPIC029 temporary token registry bridge Canon proof excerpt: "For HDE-EPIC029, TESTS\_PASS\_OK, QA\_PRECOMMIT\_CHECKLIST\_OK, and QA\_POSTCOMMIT\_CHECKLIST\_OK are temporarily canonical acceptance tokens in PF10" "These exact spellings may be used in epic-close acceptance artifacts when bound to truthful governed evidence."  
    
* PF10 Addendum 2.20 — local-dev sampler closure may use binding-equivalence for this epic — impacts PO-005 and the closure interpretation of the second development environment. PF10 — HDE-Build Notes, §2.20) HDE-EPIC029 W-004 — DEV\_SAMPLER\_URL local\_dev closure may use binding-equivalence Canon proof excerpt: "the local\_dev side of HDE-CONJ001.4 MAY be closed by binding-equivalence without a second independent local-dev runtime rerun" "http://127.0.0.1:8000/internal/dev/sampler"  
    
* PF10 Addendum 2.21 — final in-epic closure truth — impacts PO-008 closeout interpretation and later PF09.4 drain language. PF10 — HDE-Build Notes, §2.21) HDE-EPIC029 final in-epic closure truth Canon proof excerpt: "the live PF10 truth is now that the controlling Conjunction work is complete in substance and supportable for later drain at epic close." "PF09 remains unchanged until epic-end drain."

### PF23 anchors

PF23 — Canon Reality Audits, §Intent & scope \[Required-Now\] Canon proof excerpt: "Agents may read these audits as context when planning future work" "but they do not schedule, trigger, or satisfy them."

PF23 anchors note (informational only):

* Components consulted for repo-reality framing: adapter/http\_reader.py, scripts/dev\_start\_reader.sh, scripts/qa/dev\_sampler\_healthcheck.py, tools/evidence/run\_canonical\_json\_gate.py, tools/evidence/generate\_conjunction\_writer\_evidence.py, tools/qa/generate\_epic029\_close\_pack.py  
* Governed loci consulted for repo-reality framing: docs/ENDPOINTS\_CATALOG.json, docs/acceptance\_map\_epic029.json, audit/qa/hde-epic029/token\_evidence\_matrix.md, audit/qa/hde-epic029/acceptance\_map\_viability.log, audit/qa/hde-epic029/qa\_step\_logs\_manifest.json, audit/EPIC-029\_close\_report.md, audit/EPIC-029\_MANIFEST.json  
* This anchor is planning-time only and is not a required deliverable or acceptance token.

### Environment and rails posture

#### Determinism pins (canonical pins only)

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

  #### **Rails posture (explicit)**

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

No step in this plan opens rails. The plan uses existing governed OPS evidence for the second-environment closure claim and writes all plan-created QA artifacts only to stable current-state check paths under audit/qa/hde-epic029/checks/.

SOURCE EXCERPT (verbatim):

"DETERMINISM\_ENV\_PINS: {"LC\_ALL":"C","LANG":"C","TZ":"UTC","SAFE\_MODE":"1","ALLOW\_NETWORK":"0"}"  
 ": "${SAFE\_MODE:=1}" and : "${ALLOW\_NETWORK:=0}""  
 "raw\_sampler\_url \= os.environ.get("DEV\_SAMPLER\_URL")"  
 "DEV\_SAMPLER\_URL is required and must be non-empty"

### **PO inputs needed**

* No operator-set evidence-root variable is required.  
* The operator must be able to write plan-created QA artifacts under audit/qa/hde-epic029/checks/ and audit/qa/hde-epic029/00\_meta/delta/.

Shared setup commands for the whole run:

Command 0.1: export SAFE\_MODE=1  
 Command 0.2: export ALLOW\_NETWORK=0  
 Command 0.3: export APP\_ENV=dev  
 Command 0.4: export LC\_ALL=C  
 Command 0.5: export LANG=C  
 Command 0.6: export TZ=UTC

### **Evidence posture and directory structure**

#### **Epic QA root normalization (required)**

Canonical epic QA root already present in repo reality:

* audit/qa/hde-epic029/

This plan uses a single current-state evidence posture:

* Existing governed repo evidence remains at fixed, audit-proven paths.  
* Plan-created QA artifacts are written only under stable check-scoped current-state paths beneath audit/qa/hde-epic029/checks/.

SOURCE EXCERPT (verbatim):

"audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md"  
 "audit/qa/hde-epic029/qa\_step\_logs\_manifest.json"  
 "audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log"

#### **Recommended canonical layout (default for this run)**

Use this current-state layout:

* audit/qa/hde-epic029/00\_meta/  
* audit/qa/hde-epic029/checks/po-001/  
* audit/qa/hde-epic029/checks/po-002/  
* audit/qa/hde-epic029/checks/po-003/  
* audit/qa/hde-epic029/checks/po-004/  
* audit/qa/hde-epic029/checks/po-005/  
* audit/qa/hde-epic029/checks/po-006/  
* audit/qa/hde-epic029/checks/po-007/  
* audit/qa/hde-epic029/checks/po-008/

Each step writes:

* primary.log  
* only the minimal snapshots / logs / rc files needed to judge that step  
* any plan-created deliverable at the exact stable path named in the relevant Check Block

  #### **Step-log header schema expectations (minimum; required)**

Header MUST include, at minimum:

* schema\_version: pf27.step\_log\_header.v1  
* timestamp\_utc: ISO-8601 UTC timestamp with a Z suffix  
* check\_id  
* check\_name  
* status  
* fail\_status  
* command  
* command\_provenance  
* evidence\_artifacts  
* captured\_env  
* pf\_refs  
* intended\_tokens  
* claimed\_tokens

Primary-log rules:

* status must be one of PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, SKIPPED, WARN.  
* fail\_status must be empty when status is PASS, else it must equal status.  
* command must record the exact command line executed for the check, or the exact ;\-joined command sequence executed in order.  
* command\_provenance is Copy/paste from plan for the runbook commands below.  
* evidence\_artifacts must include the check’s primary.log path.  
* captured\_env must record only SAFE\_MODE, ALLOW\_NETWORK, APP\_ENV, LC\_ALL, LANG, and TZ.  
* pf\_refs must use titles only.  
* intended\_tokens and claimed\_tokens may be empty.  
* When a step does not pass, write the actual non-PASS value in both status and fail\_status.

Canonical header-writer contract for this plan:

* Step templates MUST generate the header via the PF27 canonical step-log header writer contract.  
* This plan uses one header-writer contract consistently across po-001 through po-008.  
* Immediately before header generation for each check, export:  
  * CHECK\_ID  
  * CHECK\_NAME  
  * PASS\_FAIL  
  * COMMANDS\_JSON  
  * ARTIFACTS\_JSON  
  * PF\_REFS\_JSON  
* Optional per-check exports:  
  * COMMAND\_PROVENANCE  
  * INTENDED\_TOKENS\_JSON  
  * CLAIMED\_TOKENS\_JSON  
* PASS\_FAIL must be set from the actual per-check outcome after the step commands and review are complete.  
* When PASS\_FAIL is PASS, fail\_status is empty. Otherwise fail\_status must equal PASS\_FAIL.  
* The emitted single-line JSON header must be written as the first line of that check’s primary.log.

**Canonical step-log header writer (paste-ready; emits header JSON with all required keys):**

This writes a single-line JSON header to stdout. Paste it into primary.logas the first line.

The python \- \<\<form is part of canon. Do not replace it with python file.py.

python \- \<\< 'PY'

import datetime

import json

import os

def env(name: str, default: str \= "") \-\> str:

   value \= os.environ.get(name)

   return value if value is not None else default

def env\_json(name: str, default):

   raw \= os.environ.get(name)

   if raw is None or raw \== "":

       return default

   return json.loads(raw)

schema\_version \= "pf27.step\_log\_header.v1"

timestamp\_utc \= datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"

status \= env("PASS\_FAIL")

fail\_status \= "" if status \== "PASS" else status

commands \= env\_json("COMMANDS\_JSON", \[\])

if isinstance(commands, str):

   commands \= \[commands\]

command \= "; ".join(commands) if commands else "N/A"

header \= {

   "schema\_version": schema\_version,

   "timestamp\_utc": timestamp\_utc,

   "check\_id": env("CHECK\_ID"),

   "check\_name": env("CHECK\_NAME"),

   "status": status,

   "fail\_status": fail\_status,

   "command": command,

   "command\_provenance": env("COMMAND\_PROVENANCE", "Explicitly created"),

   "evidence\_artifacts": env\_json("ARTIFACTS\_JSON", \[\]),

   "captured\_env": {

       "SAFE\_MODE": env("SAFE\_MODE"),

       "ALLOW\_NETWORK": env("ALLOW\_NETWORK"),

       "APP\_ENV": env("APP\_ENV"),

       "LC\_ALL": env("LC\_ALL"),

       "LANG": env("LANG"),

       "TZ": env("TZ"),

   },

   "pf\_refs": env\_json("PF\_REFS\_JSON", \[\]),

   "intended\_tokens": env\_json("INTENDED\_TOKENS\_JSON", \[\]),

   "claimed\_tokens": env\_json("CLAIMED\_TOKENS\_JSON", \[\]),

}

print(json.dumps(header, ensure\_ascii=False))

PY

### **Mandatory Step-0 artifacts**

#### **Step-0A — Discovery artifact (required)**

Use the existing bounded-scope inventory artifact as the discovery artifact for this run.

Discovery artifact path:

* audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md

This artifact satisfies the close-out discovery-artifact requirement for the bounded Conjunction slice.

#### **Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**

Use this only if bounded Moon Loop remediation becomes necessary during execution.

Create under:

* audit/qa/hde-epic029/00\_meta/delta/patch.diff  
* audit/qa/hde-epic029/00\_meta/delta/changed\_files.txt  
* audit/docdeltas/hde-epic029\_doc\_deltas.md — NOT RUN unless Step-0B executes  
* audit/qa/hde-epic029/00\_meta/doc\_deltas.md — NOT RUN unless Step-0B executes

Treat patch.diff and changed\_files.txt as supplementary Moon Loop evidence under audit/qa/hde-epic029/00\_meta/delta/.

This plan does not require Moon Loop by default. If a bounded Moon Loop happens, capture the smallest truthful delta pair at those stable current-state paths and keep the run within the already-approved epic scope.

### **Runbook Check Matrix**

| check\_id | check\_name | commands (PO-only) | expected result | primary evidence | deliverables | intended\_tokens | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| po-001 | Bounded Conjunction closeout slice / no new public surface | snapshot scope inventory \+ endpoint catalog \+ route slice | PASS if only the bounded Conjunction surfaces are needed for later steps | audit/qa/hde-epic029/checks/po-001/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-001/ | \[INTENTIONALLY LEFT BLANK\] | PF10 2.13; PF27 Live QA Plan |
| po-002 | Canonical JSON discipline across the bounded Conjunction slice | run canonical JSON gate \+ snapshot both governed canonical families | PASS if canonical gate exits 0 and both governed families remain inspectable | audit/qa/hde-epic029/checks/po-002/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-002/ | \[INTENTIONALLY LEFT BLANK\] | PF05 §5.6; PF27 Live QA Plan |
| po-003 | Existing dev writer posture remains typed, numeric-free, and outside formal transport proofs | run writer evidence generator \+ writer HTTP test \+ snapshot writer artifacts | PASS if writer proof runs clean and the dev writer surface remains outside A7 | audit/qa/hde-epic029/checks/po-003/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-003/ | \[INTENTIONALLY LEFT BLANK\] | PF05 §5.6; PF05 §A.3 |
| po-004 | Internal sampler harness remains dev/admin-only and refuses prod or misconfigured use | run sampler HTTP test \+ snapshot sampler harness loci | PASS if sampler test passes and the route remains dev/admin-only with prod refusal posture | audit/qa/hde-epic029/checks/po-004/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-004/ | \[INTENTIONALLY LEFT BLANK\] | PF05 §5.11 |
| po-005 | Published dev sampler binding closes both intended development environments truthfully | snapshot OPS-01 binding artifacts and review closure mode | PASS if codespaces is direct runtime closure and local\_dev is binding-equivalence closure with one truthful binding posture | audit/qa/hde-epic029/checks/po-005/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-005/ | \[INTENTIONALLY LEFT BLANK\] | PF10 2.20 |
| po-006 | Formal transport proof surface remains only the cataloged Reader success surface | run endpoint catalog test \+ snapshot catalog | PASS if /reader is the cataloged proof surface and dev/internal surfaces stay outside that family | audit/qa/hde-epic029/checks/po-006/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-006/ | \[INTENTIONALLY LEFT BLANK\] | PF05 §5.6; PF05 §5.11.6 |
| po-007 | At least one real functional harness proof exists and passes | run the combined functional pytest bundle | PASS if the combined real functional bundle exits 0 | audit/qa/hde-epic029/checks/po-007/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-007/ | \[INTENTIONALLY LEFT BLANK\] | PF06 §3.5.2.8; PF19 §3.5.4 |
| po-008 | Final closeout records stay on one bounded acceptance surface and are backed by real passing QA evidence | snapshot acceptance / token / viability / close-pack / QA-log families and review them together | PASS if the closeout family agrees on the same bounded surface and is backed by real passing QA logs | audit/qa/hde-epic029/checks/po-008/primary.log | check-scoped current-state artifacts under audit/qa/hde-epic029/checks/po-008/ | TESTS\_PASS\_OK, QA\_PRECOMMIT\_CHECKLIST\_OK, QA\_POSTCOMMIT\_CHECKLIST\_OK | PF10 2.2; PF10 2.21 |

### Token coverage and evidence binding (required)

PF10 — HDE-Build Notes, §2.2) HDE-EPIC029 temporary token registry bridge  
 Canon proof excerpt:  
 "TESTS\_PASS\_OK, QA\_PRECOMMIT\_CHECKLIST\_OK, and QA\_POSTCOMMIT\_CHECKLIST\_OK are temporarily canonical acceptance tokens in PF10"  
 "These exact spellings may be used in epic-close acceptance artifacts when bound to truthful governed evidence."

This plan uses the temporary token bridge only in po-008, where the final acceptance-binding surfaces are reviewed against the three existing passing QA logs. No new token names are introduced anywhere in this plan.

### **Check Blocks**

#### **CHECK po-001: Bounded Conjunction closeout slice / no new public surface**

Surface / D-goal mapping: D1 \+ bounded Conjunction scope and route inventory  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF10 — HDE-Build Notes, §2.13) Implementation report HDE-EPIC029; PF27 — Canon Plan Templates, §1) Live QA Plan

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-001"  
 "Proof obligation:"  
 "The epic must remain confined to its bounded Conjunction closeout slice and must not introduce or repurpose a new public surface."  
 "Implementation linkage:"  
 "PF10 frames the epic as closing three remaining Conjunction gaps without creating a new public surface."

Goal

Capture the current bounded-scope inventory, the endpoint catalog, and the route slice used by this epic. This step does not prove runtime behavior; it proves that the later steps stay on the intended surfaces and do not need or imply a new public route.

Preconditions

* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-001

Numbered PO actions

1. Snapshot the bounded conjunction inventory artifact.  
2. Snapshot the endpoint catalog.  
3. Capture the route slice for the five in-scope surfaces from the current route-definition file.  
4. Review the captured artifacts against the bounded-scope statement.  
5. Write the step receipt.

PO command(s)

Command 2: cp audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md audit/qa/hde-epic029/checks/po-001/conjunction\_json\_surface\_inventory.snapshot.md  
 SOURCE EXCERPT (verbatim):  
 "audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md"  
 "Path: audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md"  
 "Where found: head \-n 40 audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md"

Command 3: cp docs/ENDPOINTS\_CATALOG.json audit/qa/hde-epic029/checks/po-001/endpoints\_catalog.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: docs/ENDPOINTS\_CATALOG.json"  
 "Where found: nl \-ba docs/ENDPOINTS\_CATALOG.json | sed \-n '1,260p'"  
 "Endpoint catalog includes /reader and /dev/\*/conjunction; /internal/dev/sampler is code-defined but not catalog-listed in this snapshot."

Command 4: rg \-n '(/reader|/dev/writer/conjunction|/internal/dev/sampler|/dev/sampler/conjunction|/dev/reader/conjunction)' adapter/http\_reader.py | tee audit/qa/hde-epic029/checks/po-001/route\_snapshot.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: adapter/http\_reader.py"  
 "Proof: @bp.get("/reader")"  
 "Proof: @bp.route("/internal/dev/sampler", methods=\["POST"\], provide\_automatic\_options=False)"  
 "Proof: @bp.get("/dev/sampler/conjunction")"

Command 5.1: export CHECK\_ID='po-001'; export CHECK\_NAME='Bounded Conjunction closeout slice / no new public surface'; export COMMANDS\_JSON='\["cp audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md audit/qa/hde-epic029/checks/po-001/conjunction\_json\_surface\_inventory.snapshot.md","cp docs/ENDPOINTS\_CATALOG.json audit/qa/hde-epic029/checks/po-001/endpoints\_catalog.snapshot.json","rg \-n "(/reader|/dev/writer/conjunction|/internal/dev/sampler|/dev/sampler/conjunction|/dev/reader/conjunction)" adapter/http\_reader.py | tee audit/qa/hde-epic029/checks/po-001/route\_snapshot.txt"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-001/primary.log","audit/qa/hde-epic029/checks/po-001/conjunction\_json\_surface\_inventory.snapshot.md","audit/qa/hde-epic029/checks/po-001/endpoints\_catalog.snapshot.json","audit/qa/hde-epic029/checks/po-001/route\_snapshot.txt"\]'; export PF\_REFS\_JSON='\["PF10 — HDE-Build Notes","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 5.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 5.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-001/primary.log

What to look for

* The inventory snapshot stays on the bounded Conjunction slice.  
* The catalog snapshot includes /reader and /dev/writer/conjunction.  
* The route snapshot shows only the five in-scope surfaces named in this step.  
* Nothing in the captured inputs suggests a new public surface is needed for the later steps.

Expected result (PASS/FAIL predicates)

PASS if:

* all three snapshots exist and are non-empty  
* the captured route slice and catalog remain compatible with the bounded-scope statement

FAIL\_BEHAVIOR if:

* the captured scope inventory or route slice requires a new public surface to complete the epic

FAIL\_TOOLING if:

* cp or rg fails for any of the proven loci

TOOLING\_BLOCKED if:

* a named in-scope route or catalog file cannot be read at the proven repo path

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-001/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-001/primary.log  
* audit/qa/hde-epic029/checks/po-001/conjunction\_json\_surface\_inventory.snapshot.md  
* audit/qa/hde-epic029/checks/po-001/endpoints\_catalog.snapshot.json  
* audit/qa/hde-epic029/checks/po-001/route\_snapshot.txt

#### **CHECK po-002: Canonical JSON discipline across the bounded Conjunction slice**

Surface / D-goal mapping: D2 \+ canonical JSON discipline  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF05 — HDE-CLI-API-Vendor-Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\]; PF27 — Canon Plan Templates, §1) Live QA Plan

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-002"  
 "Proof obligation:"  
 "All in-scope JSON outputs for this epic must still honor canonical JSON discipline through the single shared emission path."  
 "Implementation linkage:"  
 "PF10 frames the implemented result as the bounded conjunction JSON inventory plus the canonical-JSON evidence refresh"

Goal

Run the canonical JSON gate and capture both governed canonical JSON evidence families into the stable check path. This proves that the bounded Conjunction slice still respects the shared canonical JSON discipline.

Preconditions

* po-001 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-002

Numbered PO actions

1. Run the canonical JSON gate.  
2. Record the gate return code.  
3. Snapshot the authoritative canonical JSON structured record.  
4. Snapshot the legacy canonical JSON check log.  
5. Review the outputs against the expected PASS posture.  
6. Write the step receipt.

PO command(s)

Command 2: python tools/evidence/run\_canonical\_json\_gate.py |& tee audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.output.log; printf '%s\\n' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.rc.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: tools/evidence/run\_canonical\_json\_gate.py"  
 "Proof: JSON\_GATE\_DIR \= ROOT / "audit" / "gates" / "json\_gate" / "canonical""  
 "Where found: nl \-ba tools/evidence/run\_canonical\_json\_gate.py | sed \-n '1,240p'"

Command 3: cp audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json audit/qa/hde-epic029/checks/po-002/json\_gate\_structured\_record.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json"  
 "Where found: head \-n 8 audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json"  
 "audit/gates/json\_gate/canonical/"

Command 4: cp audit/gates/canonical\_json/json\_canonical\_check.log audit/qa/hde-epic029/checks/po-002/json\_canonical\_check.snapshot.log  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/gates/canonical\_json/json\_canonical\_check.log"  
 "Where found: head \-n 10 audit/gates/canonical\_json/json\_canonical\_check.log"

Command 5.1: export CHECK\_ID='po-002'; export CHECK\_NAME='Canonical JSON discipline across the bounded Conjunction slice'; export COMMANDS\_JSON='\["python tools/evidence/run\_canonical\_json\_gate.py |& tee audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.output.log; printf '''%s\\n''' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.rc.txt","cp audit/gates/json\_gate/canonical/json\_gate\_structured\_record.json audit/qa/hde-epic029/checks/po-002/json\_gate\_structured\_record.snapshot.json","cp audit/gates/canonical\_json/json\_canonical\_check.log audit/qa/hde-epic029/checks/po-002/json\_canonical\_check.snapshot.log"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-002/primary.log","audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.output.log","audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.rc.txt","audit/qa/hde-epic029/checks/po-002/json\_gate\_structured\_record.snapshot.json","audit/qa/hde-epic029/checks/po-002/json\_canonical\_check.snapshot.log"\]'; export PF\_REFS\_JSON='\["PF05 — HDE CLI/API Vendor Reference","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 5.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 5.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-002/primary.log

What to look for

* run\_canonical\_json\_gate.rc.txt contains 0.  
* The authoritative canonical family snapshot exists.  
* The legacy canonical family snapshot exists.  
* Nothing in the step requires a second emitter path or a new JSON surface.

Expected result (PASS/FAIL predicates)

PASS if:

* the gate runner exits 0  
* both governed canonical JSON family snapshots exist and are non-empty

FAIL\_BEHAVIOR if:

* the canonical gate exits successfully but the snapshots show contradictory postures across the two governed families

FAIL\_TOOLING if:

* the gate runner exits non-zero

TOOLING\_BLOCKED if:

* either governed canonical JSON family cannot be read at the proven repo path

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-002/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-002/primary.log  
* audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.output.log  
* audit/qa/hde-epic029/checks/po-002/run\_canonical\_json\_gate.rc.txt  
* audit/qa/hde-epic029/checks/po-002/json\_gate\_structured\_record.snapshot.json  
* audit/qa/hde-epic029/checks/po-002/json\_canonical\_check.snapshot.log

#### **CHECK po-003: Existing dev writer posture remains typed, numeric-free, and outside formal transport proofs**

Surface / D-goal mapping: D3 \+ dev writer posture  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF05 — HDE-CLI-API-Vendor-Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\]; PF05 — HDE-CLI-API-Vendor-Ref, §A.3 Writers and errors

PF05 — HDE-CLI-API-Vendor-Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\]  
 Canon proof excerpt:  
 "\* **Dev writer conjunction (dev-only):** /dev/writer/conjunction"  
 "\* Such writer-evidence runs do not widen the route contract and do not move this endpoint into the A7 proof family."

PF05 — HDE-CLI-API-Vendor-Ref, §A.3 Writers and errors  
 Canon proof excerpt:  
 "\* No-store and no-ETag posture (writers/errors)"  
 "\* artifacts/writer/conjunction\_write\_readback.log"  
 "\* artifacts/writer/conjunction\_writer\_summary.json"

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-003"  
 "Proof obligation:"  
 "The existing development-only writer surface must still return typed, numeric-free success and error behavior, remain non-conditional, and remain outside the formal transport-proof surface."  
 "Implementation linkage:"  
 "PF10 frames PR-02 as finishing the existing dev writer surface’s typed numeric-free success/error posture"

Goal

Refresh the governed writer evidence family and run the existing dev conjunction HTTP test. This step proves the dev writer posture still behaves correctly and still sits outside the formal transport-proof family.

Preconditions

* po-002 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-003

Numbered PO actions

1. Run the writer evidence generator.  
2. Record its return code.  
3. Run the dev conjunction HTTP test file.  
4. Record its return code.  
5. Snapshot the governed writer evidence artifacts.  
6. Review the outputs against the expected PASS posture.  
7. Write the step receipt.

PO command(s)

Command 2: python tools/evidence/generate\_conjunction\_writer\_evidence.py |& tee audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.output.log; printf '%s\\n' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.rc.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: tools/evidence/generate\_conjunction\_writer\_evidence.py"  
 "Proof: WRITE\_READBACK\_LOG \= ROOT / "artifacts/writer/conjunction\_write\_readback.log""  
 "Where found: nl \-ba tools/evidence/generate\_conjunction\_writer\_evidence.py | sed \-n '1,260p'"

Command 3: python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py |& tee audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.output.log; printf '%s\\n' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.rc.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: tests/http/test\_dev\_conjunction\_http.py"  
 "Proof: for route in ("/dev/sampler/conjunction", "/dev/reader/conjunction", "/dev/writer/conjunction"):"  
 "Where found: nl \-ba tests/http/test\_dev\_conjunction\_http.py | sed \-n '1,220p'"

Command 4: cp artifacts/writer/conjunction\_write\_readback.log audit/qa/hde-epic029/checks/po-003/conjunction\_write\_readback.snapshot.log  
 SOURCE EXCERPT (verbatim):  
 "Path: artifacts/writer/conjunction\_write\_readback.log"  
 "Proof: schema=conjunction\_write\_readback.log.v1"  
 "Where found: head \-n 40 artifacts/writer/conjunction\_write\_readback.log"

Command 5: cp artifacts/writer/conjunction\_writer\_summary.json audit/qa/hde-epic029/checks/po-003/conjunction\_writer\_summary.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: artifacts/writer/conjunction\_writer\_summary.json"  
 "Where found: head \-n 40 artifacts/writer/conjunction\_writer\_summary.json"

Command 6.1: export CHECK\_ID='po-003'; export CHECK\_NAME='Existing dev writer posture remains typed, numeric-free, and outside formal transport proofs'; export COMMANDS\_JSON='\["python tools/evidence/generate\_conjunction\_writer\_evidence.py |& tee audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.output.log; printf '''%s\\n''' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.rc.txt","python \-m pytest \-q tests/http/test\_dev\_conjunction\_http.py |& tee audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.output.log; printf '''%s\\n''' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.rc.txt","cp artifacts/writer/conjunction\_write\_readback.log audit/qa/hde-epic029/checks/po-003/conjunction\_write\_readback.snapshot.log","cp artifacts/writer/conjunction\_writer\_summary.json audit/qa/hde-epic029/checks/po-003/conjunction\_writer\_summary.snapshot.json"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-003/primary.log","audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.output.log","audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.rc.txt","audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.output.log","audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.rc.txt","audit/qa/hde-epic029/checks/po-003/conjunction\_write\_readback.snapshot.log","audit/qa/hde-epic029/checks/po-003/conjunction\_writer\_summary.snapshot.json"\]'; export PF\_REFS\_JSON='\["PF05 — HDE CLI/API Vendor Reference","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 6.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 6.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-003/primary.log

What to look for

* Both rc files contain 0.  
* The writer summary snapshot still points at /dev/writer/conjunction.  
* The writer artifacts exist and are non-empty.  
* Nothing in the writer artifacts or the test output suggests widening into A7 or a formal transport-proof surface.

Expected result (PASS/FAIL predicates)

PASS if:

* the writer evidence generator exits 0  
* tests/http/test\_dev\_conjunction\_http.py exits 0  
* the two writer artifact snapshots exist and are non-empty

FAIL\_BEHAVIOR if:

* the writer test fails on typed numeric-free or writer-route behavior

FAIL\_TOOLING if:

* the writer evidence generator fails  
* the pytest command fails for a tooling reason

TOOLING\_BLOCKED if:

* either governed writer artifact cannot be read at the proven repo path

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-003/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-003/primary.log  
* audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.output.log  
* audit/qa/hde-epic029/checks/po-003/generate\_conjunction\_writer\_evidence.rc.txt  
* audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.output.log  
* audit/qa/hde-epic029/checks/po-003/test\_dev\_conjunction\_http.rc.txt  
* audit/qa/hde-epic029/checks/po-003/conjunction\_write\_readback.snapshot.log  
* audit/qa/hde-epic029/checks/po-003/conjunction\_writer\_summary.snapshot.json

#### **CHECK po-004: Internal sampler harness remains dev/admin-only and refuses prod or misconfigured use**

Surface / D-goal mapping: D4 \+ dev/internal sampler harness  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF05 — HDE-CLI-API-Vendor-Ref, §5.11 Dev sampler HTTP harness (dev/admin-only) \[Implemented\]

PF05 — HDE-CLI-API-Vendor-Ref, §5.11 Dev sampler HTTP harness (dev/admin-only) \[Implemented\]  
 Canon proof excerpt:  
 "The dev sampler HTTP harness is a **dev/admin-only** route"  
 "When APP\_ENV is unset, empty, or set to any other value (including prod), the handler **MUST** return a **403 Forbidden** response"  
 "POST /internal/dev/sampler is a **dev/admin-only internal harness** and is explicitly excluded from the Endpoint Catalog (§5.6)."

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-004"  
 "Proof obligation:"  
 "The internal sampler harness must behave as a non-production development/admin surface: it must work in allowed development modes and refuse production-mode or misconfigured use."  
 "Implementation linkage:"  
 "PF10 frames the implemented result as a valid non-production sampler rerun with expected development success and expected production-mode refusal behavior."

Goal

Run the existing sampler HTTP test and snapshot the existing harness-start and healthcheck loci. This step proves the harness behavior exists and that the current repo still enforces dev/admin-only posture.

Preconditions

* po-003 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-004

Numbered PO actions

1. Run the existing sampler HTTP test.  
2. Record the return code.  
3. Snapshot the existing harness-start script.  
4. Snapshot the existing sampler healthcheck script.  
5. Review the outputs against the expected PASS posture.  
6. Write the step receipt.

PO command(s)

Command 2: python \-m pytest \-q tests/adapter/test\_dev\_sampler\_http.py |& tee audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.output.log; printf '%s\\n' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.rc.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: tests/adapter/test\_dev\_sampler\_http.py"  
 "Proof: assert resp.status\_code \== 403 (prod gate)"  
 "Where found: nl \-ba tests/adapter/test\_dev\_sampler\_http.py | sed \-n '1,220p'"

Command 3: cp scripts/dev\_start\_reader.sh audit/qa/hde-epic029/checks/po-004/dev\_start\_reader.snapshot.sh  
 SOURCE EXCERPT (verbatim):  
 "Path: scripts/dev\_start\_reader.sh"  
 "Proof: : "${SAFE\_MODE:=1}" and exec python \-m adapter.http\_reader"  
 "Where found: nl \-ba scripts/dev\_start\_reader.sh | sed \-n '1,180p'"

Command 4: cp scripts/qa/dev\_sampler\_healthcheck.py audit/qa/hde-epic029/checks/po-004/dev\_sampler\_healthcheck.snapshot.py  
 SOURCE EXCERPT (verbatim):  
 "Path: scripts/qa/dev\_sampler\_healthcheck.py"  
 "Proof: raw\_sampler\_url \= os.environ.get("DEV\_SAMPLER\_URL") and DEV\_SAMPLER\_URL is required and must be non-empty"  
 "Where found: nl \-ba scripts/qa/dev\_sampler\_healthcheck.py | sed \-n '1,260p'"

Command 5.1: export CHECK\_ID='po-004'; export CHECK\_NAME='Internal sampler harness remains dev/admin-only and refuses prod or misconfigured use'; export COMMANDS\_JSON='\["python \-m pytest \-q tests/adapter/test\_dev\_sampler\_http.py |& tee audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.output.log; printf '''%s\\n''' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.rc.txt","cp scripts/dev\_start\_reader.sh audit/qa/hde-epic029/checks/po-004/dev\_start\_reader.snapshot.sh","cp scripts/qa/dev\_sampler\_healthcheck.py audit/qa/hde-epic029/checks/po-004/dev\_sampler\_healthcheck.snapshot.py"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-004/primary.log","audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.output.log","audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.rc.txt","audit/qa/hde-epic029/checks/po-004/dev\_start\_reader.snapshot.sh","audit/qa/hde-epic029/checks/po-004/dev\_sampler\_healthcheck.snapshot.py"\]'; export PF\_REFS\_JSON='\["PF05 — HDE CLI/API Vendor Reference","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 5.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 5.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-004/primary.log

What to look for

* test\_dev\_sampler\_http.rc.txt contains 0.  
* The harness-start and healthcheck snapshots are present.  
* The sampler step remains tied to /internal/dev/sampler.  
* The evidence you review stays dev/admin-only and does not treat the route as cataloged or public.

Expected result (PASS/FAIL predicates)

PASS if:

* the sampler HTTP test exits 0  
* both harness snapshots exist and are non-empty

FAIL\_BEHAVIOR if:

* the sampler HTTP test no longer enforces dev/admin-only refusal behavior

FAIL\_TOOLING if:

* the pytest command fails for a tooling reason

TOOLING\_BLOCKED if:

* the test file or harness loci cannot be read at the proven repo paths

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-004/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-004/primary.log  
* audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.output.log  
* audit/qa/hde-epic029/checks/po-004/test\_dev\_sampler\_http.rc.txt  
* audit/qa/hde-epic029/checks/po-004/dev\_start\_reader.snapshot.sh  
* audit/qa/hde-epic029/checks/po-004/dev\_sampler\_healthcheck.snapshot.py

#### **CHECK po-005: Published dev sampler binding closes both intended development environments truthfully**

Surface / D-goal mapping: D5 \+ binding truth for the dev sampler harness  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF10 — HDE-Build Notes, §2.20) HDE-EPIC029 W-004 — DEV\_SAMPLER\_URL local\_dev closure may use binding-equivalence

PF10 — HDE-Build Notes, §2.20) HDE-EPIC029 W-004 — DEV\_SAMPLER\_URL local\_dev closure may use binding-equivalence  
 Canon proof excerpt:  
 "the local\_dev side of HDE-CONJ001.4 MAY be closed by binding-equivalence without a second independent local-dev runtime rerun"  
 "http://127.0.0.1:8000/internal/dev/sampler"  
 "Closure mode: binding-equivalence"

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-005"  
 "Proof obligation:"  
 "The non-production sampler access value used for QA must be the authoritative published binding for the intended environment, and the two intended development environments must resolve to one truthful, closed access posture."  
 "Notes:"  
 "For this epic, PF10 treats the second environment’s closure as equivalence-based rather than as a separate second runtime proof pass."

Goal

Inspect the existing OPS-01 binding family and prove one truthful closure posture across the two intended development environments. This step is evidence inspection only; it does not attempt a second environment session.

Preconditions

* po-004 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-005

Numbered PO actions

1. Snapshot the OPS-01 command, exit-code, URL, and binding-disposition artifacts.  
2. Review the snapshots together as one binding family.  
3. Write the step receipt.

PO command(s)

Command 2: cp audit/ops/hde-epic029/ops-01/commands.txt audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/ops/hde-epic029/ops-01/commands.txt"  
 "Proof: APP\_ENV=dev SAFE\_MODE=1 ALLOW\_NETWORK=0 LC\_ALL=C LANG=C TZ=UTC PORT=8000 scripts/dev\_start\_reader.sh"  
 "Where found: head \-n 20 audit/ops/hde-epic029/ops-01/commands.txt"

Command 3: cp audit/ops/hde-epic029/ops-01/exit\_codes.txt audit/qa/hde-epic029/checks/po-005/exit\_codes.snapshot.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/ops/hde-epic029/ops-01/exit\_codes.txt"  
 "Proof: codespaces\_healthcheck=0"  
 "Where found: head \-n 20 audit/ops/hde-epic029/ops-01/exit\_codes.txt"

Command 4: cp audit/ops/hde-epic029/ops-01/codespaces\_dev\_sampler\_url.md audit/qa/hde-epic029/checks/po-005/codespaces\_dev\_sampler\_url.snapshot.md  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/ops/hde-epic029/ops-01/codespaces\_dev\_sampler\_url.md"  
 "Proof: file listed under ops-01 evidence family"  
 "Where found: find audit/ops/hde-epic029 \-maxdepth 4 \-type f | sort"

Command 5: cp audit/ops/hde-epic029/ops-01/local\_dev\_sampler\_url.md audit/qa/hde-epic029/checks/po-005/local\_dev\_sampler\_url.snapshot.md  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/ops/hde-epic029/ops-01/local\_dev\_sampler\_url.md"  
 "Proof: file listed under ops-01 evidence family"  
 "Where found: find audit/ops/hde-epic029 \-maxdepth 4 \-type f | sort"

Command 6: cp audit/ops/hde-epic029/ops-01/binding\_disposition.md audit/qa/hde-epic029/checks/po-005/binding\_disposition.snapshot.md  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/ops/hde-epic029/ops-01/binding\_disposition.md"  
 "Proof: codespaces: closed \- closed by direct runtime validation."  
 "Where found: head \-n 40 audit/ops/hde-epic029/ops-01/binding\_disposition.md"

Command 7.1: export CHECK\_ID='po-005'; export CHECK\_NAME='Published dev sampler binding closes both intended development environments truthfully'; export COMMANDS\_JSON='\["cp audit/ops/hde-epic029/ops-01/commands.txt audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt","cp audit/ops/hde-epic029/ops-01/exit\_codes.txt audit/qa/hde-epic029/checks/po-005/exit\_codes.snapshot.txt","cp audit/ops/hde-epic029/ops-01/codespaces\_dev\_sampler\_url.md audit/qa/hde-epic029/checks/po-005/codespaces\_dev\_sampler\_url.snapshot.md","cp audit/ops/hde-epic029/ops-01/local\_dev\_sampler\_url.md audit/qa/hde-epic029/checks/po-005/local\_dev\_sampler\_url.snapshot.md","cp audit/ops/hde-epic029/ops-01/binding\_disposition.md audit/qa/hde-epic029/checks/po-005/binding\_disposition.snapshot.md"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-005/primary.log","audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt","audit/qa/hde-epic029/checks/po-005/exit\_codes.snapshot.txt","audit/qa/hde-epic029/checks/po-005/codespaces\_dev\_sampler\_url.snapshot.md","audit/qa/hde-epic029/checks/po-005/local\_dev\_sampler\_url.snapshot.md","audit/qa/hde-epic029/checks/po-005/binding\_disposition.snapshot.md"\]'; export PF\_REFS\_JSON='\["PF10 — HDE-Build Notes","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 7.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 7.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-005/primary.log

What to look for

* The commands snapshot shows the approved dev harness binding flow.  
* The exit-codes snapshot still records a successful Codespaces healthcheck.  
* The codespaces and local-dev URL snapshots use the same published binding value.  
* The binding-disposition snapshot states Codespaces closure by direct runtime validation and local\_dev closure by binding-equivalence.  
* No contradictory open or deferred posture remains in the captured OPS-01 family.

Expected result (PASS/FAIL predicates)

PASS if:

* the OPS-01 snapshots are all present  
* the two URL snapshots agree on one published binding value  
* the binding-disposition snapshot records direct closure for Codespaces and binding-equivalence closure for local\_dev

FAIL\_BEHAVIOR if:

* the captured OPS family shows contradictory closure states for the two intended development environments

FAIL\_TOOLING if:

* any required OPS artifact cannot be copied

TOOLING\_BLOCKED if:

* the required OPS family is missing from the proven repo paths

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-005/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-005/primary.log  
* audit/qa/hde-epic029/checks/po-005/commands.snapshot.txt  
* audit/qa/hde-epic029/checks/po-005/exit\_codes.snapshot.txt  
* audit/qa/hde-epic029/checks/po-005/codespaces\_dev\_sampler\_url.snapshot.md  
* audit/qa/hde-epic029/checks/po-005/local\_dev\_sampler\_url.snapshot.md  
* audit/qa/hde-epic029/checks/po-005/binding\_disposition.snapshot.md

#### **CHECK po-006: Formal transport proof surface remains only the cataloged Reader success surface**

Surface / D-goal mapping: D6 \+ proof-surface boundary  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF05 — HDE-CLI-API-Vendor-Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\]; PF05 — HDE-CLI-API-Vendor-Ref, §5.11.6 A7, Catalog, and evidence (informative)

PF05 — HDE-CLI-API-Vendor-Ref, §5.6 Endpoint Catalog (JSON success) \[Required−Now\]  
 Canon proof excerpt:  
 "Endpoint Catalog (JSON success) — Required-Now."  
 "Internal-only, env-gated per entry, and the **single A7 proof surface** for Reader success routes"  
 "not /internal/version."

PF05 — HDE-CLI-API-Vendor-Ref, §5.11.6 A7, Catalog, and evidence (informative)  
 Canon proof excerpt:  
 "POST /internal/dev/sampler is a **dev/admin-only internal harness** and is explicitly excluded from the Endpoint Catalog (§5.6)."  
 "No A7 proofs run on this route."

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-006"  
 "Proof obligation:"  
 "Only the cataloged reader success surface may be used for formal transport proofs in this epic, while the development writer and internal sampler surfaces must remain outside that proof family."  
 "Implementation linkage:"  
 "PF10 frames the writer posture as explicitly outside formal transport proofs"

Goal

Verify the endpoint catalog and its test proof, then capture the current catalog state for manual review. This step proves the formal proof surface stays on the cataloged Reader success route and not on the dev writer or internal sampler surfaces.

Preconditions

* po-005 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-006

Numbered PO actions

1. Run the endpoint catalog test.  
2. Record the return code.  
3. Snapshot the endpoint catalog.  
4. Review the captured catalog against the proof-surface boundary.  
5. Write the step receipt.

PO command(s)

Command 2: python \-m pytest \-q tests/http/test\_endpoint\_catalog.py |& tee audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.output.log; printf '%s\\n' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.rc.txt  
 SOURCE EXCERPT (verbatim):  
 "Path: tests/http/test\_endpoint\_catalog.py"  
 "Proof: entry \= next((item for item in \_catalog\_entries() if item.get("path") \== "/reader"), None)"  
 "Where found: nl \-ba tests/http/test\_endpoint\_catalog.py | sed \-n '1,220p'"

Command 3: cp docs/ENDPOINTS\_CATALOG.json audit/qa/hde-epic029/checks/po-006/endpoints\_catalog.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: docs/ENDPOINTS\_CATALOG.json"  
 "Where found: nl \-ba docs/ENDPOINTS\_CATALOG.json | sed \-n '1,260p'"  
 "Endpoint catalog includes /reader and /dev/\*/conjunction; /internal/dev/sampler is code-defined but not catalog-listed in this snapshot."

Command 4.1: export CHECK\_ID='po-006'; export CHECK\_NAME='Formal transport proof surface remains only the cataloged Reader success surface'; export COMMANDS\_JSON='\["python \-m pytest \-q tests/http/test\_endpoint\_catalog.py |& tee audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.output.log; printf '''%s\\n''' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.rc.txt","cp docs/ENDPOINTS\_CATALOG.json audit/qa/hde-epic029/checks/po-006/endpoints\_catalog.snapshot.json"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-006/primary.log","audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.output.log","audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.rc.txt","audit/qa/hde-epic029/checks/po-006/endpoints\_catalog.snapshot.json"\]'; export PF\_REFS\_JSON='\["PF05 — HDE CLI/API Vendor Reference","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 4.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 4.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-006/primary.log

What to look for

* test\_endpoint\_catalog.rc.txt contains 0.  
* The catalog snapshot is present.  
* The catalog includes /reader.  
* The cataloged proof surface remains /reader, while /dev/writer/conjunction stays outside the A7 family and /internal/dev/sampler remains uncataloged.

Expected result (PASS/FAIL predicates)

PASS if:

* the endpoint catalog test exits 0  
* the catalog snapshot exists and supports /reader as the formal proof surface  
* nothing in the captured catalog widens /dev/writer/conjunction or /internal/dev/sampler into the formal proof family

FAIL\_BEHAVIOR if:

* the catalog or its test now treats a dev/internal surface as the formal proof surface for this epic

FAIL\_TOOLING if:

* the endpoint catalog test fails for a tooling reason

TOOLING\_BLOCKED if:

* the catalog file or test file is missing at the proven repo path

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-006/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-006/primary.log  
* audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.output.log  
* audit/qa/hde-epic029/checks/po-006/test\_endpoint\_catalog.rc.txt  
* audit/qa/hde-epic029/checks/po-006/endpoints\_catalog.snapshot.json

#### **CHECK po-007: At least one real functional harness proof exists and passes**

Surface / D-goal mapping: D7 \+ real functional proof  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF06 — Epic-Process-Guide, §3.5.2.8 Live QA via harness (required for epic closeout); PF19 — Glow QA Guide, §3.5.4 Artifact-first Live QA pattern (behavior vs artifacts)

PF06 — Epic-Process-Guide, §3.5.2.8 Live QA via harness (required for epic closeout)  
 Canon proof excerpt:  
 "If an epic changes a functional feature (runtime behavior, user-visible outputs, integration seams, or data flow), the Live QA plan MUST include at least one functional proof step that exercises the changed behavior in the harness and produces governed evidence. Static artifacts alone (schemas, diffs, logs without a proof step) are not sufficient."

PF19 — Glow QA Guide, §3.5.4 Artifact-first Live QA pattern (behavior vs artifacts)  
 Canon proof excerpt:  
 "For any Live QA step that refers to behavior, QA plans MUST follow a two-part, artifact-first pattern."  
 "Key principle: Codespaces is where we persist and analyze what happened"  
 "it is not itself the authoritative behavior runtime."

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-007"  
 "Proof obligation:"  
 "The Live QA plan must prove changed behavior through at least one real functional check and must not rely only on artifact refresh or local smoke evidence."  
 "Canon reference:"  
 "PF06 — Canon-Epic-Process-Guide, §3.5.2.8 Live QA via harness (required for epic closeout); PF19 — Canon-Glow-QA-Guide, §3.5.4 Artifact-first Live QA pattern (behavior vs artifacts)."

Goal

Run one combined real functional pytest bundle across the dev sampler, dev conjunction, and endpoint catalog surfaces, then capture its outputs under the stable check path. This is the plan’s explicit real functional proof step.

Preconditions

* po-006 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-007

Numbered PO actions

1. Run the combined functional pytest bundle.  
2. Record the return code.  
3. Review the captured output as a real functional proof step.  
4. Write the step receipt.

PO command(s)

Command 2: python \-m pytest \-q tests/adapter/test\_dev\_sampler\_http.py tests/http/test\_dev\_conjunction\_http.py tests/http/test\_endpoint\_catalog.py |& tee audit/qa/hde-epic029/checks/po-007/functional\_bundle.output.log; printf '%s\\n' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-007/functional\_bundle.rc.txt  
 SOURCE EXCERPT (verbatim):  
 "\[command\] /workspaces/glow-hdengine-v2/.venv/bin/python \-m pytest \-q tests/adapter/test\_dev\_sampler\_http.py tests/http/test\_dev\_conjunction\_http.py tests/http/test\_endpoint\_catalog.py"  
 "\[exit\_code\] 0"  
 "Path: audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log"

Command 3.1: export CHECK\_ID='po-007'; export CHECK\_NAME='At least one real functional harness proof exists and passes'; export COMMANDS\_JSON='\["python \-m pytest \-q tests/adapter/test\_dev\_sampler\_http.py tests/http/test\_dev\_conjunction\_http.py tests/http/test\_endpoint\_catalog.py |& tee audit/qa/hde-epic029/checks/po-007/functional\_bundle.output.log; printf '''%s\\n''' "${PIPESTATUS\[0\]}" | tee audit/qa/hde-epic029/checks/po-007/functional\_bundle.rc.txt"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-007/primary.log","audit/qa/hde-epic029/checks/po-007/functional\_bundle.output.log","audit/qa/hde-epic029/checks/po-007/functional\_bundle.rc.txt"\]'; export PF\_REFS\_JSON='\["PF06 — Epic Process Guide","PF19 — Glow QA Guide","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\[\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 3.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR', 'FAIL\_TOOLING', or 'TOOLING\_BLOCKED' as actually observed for this step

Command 3.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-007/primary.log

What to look for

* functional\_bundle.rc.txt contains 0.  
* The combined output log exists.  
* The step proves a real functional bundle, not just artifact refresh or static inspection.

Expected result (PASS/FAIL predicates)

PASS if:

* the combined functional pytest bundle exits 0  
* the combined output log and rc capture are present under audit/qa/hde-epic029/checks/po-007/

FAIL\_BEHAVIOR if:

* the bundle exits non-zero because one or more functional checks fail

FAIL\_TOOLING if:

* the bundle cannot run because pytest or another required tool is missing

TOOLING\_BLOCKED if:

* any of the three proven test files cannot be read at the audited repo paths

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-007/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-007/primary.log  
* audit/qa/hde-epic029/checks/po-007/functional\_bundle.output.log  
* audit/qa/hde-epic029/checks/po-007/functional\_bundle.rc.txt

#### **CHECK po-008: Final closeout records stay on one bounded acceptance surface and are backed by real passing QA evidence**

Surface / D-goal mapping: D8 \+ acceptance / closeout coherence  
 Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev  
 Pins: LC\_ALL=C LANG=C TZ=UTC  
 PF anchors: PF10 — HDE-Build Notes, §2.2) HDE-EPIC029 temporary token registry bridge; PF10 — HDE-Build Notes, §2.21) HDE-EPIC029 final in-epic closure truth

PF10 — HDE-Build Notes, §2.21) HDE-EPIC029 final in-epic closure truth  
 Canon proof excerpt:  
 "the live PF10 truth is now that the controlling Conjunction work is complete in substance and supportable for later drain at epic close."  
 "Epic close review must use this addendum plus the governed repo evidence as the authoritative in-flight closure basis."

**Intent (required)**

SOURCE EXCERPT (verbatim):

"PO-008"  
 "Proof obligation:"  
 "The final closeout records for this epic must all describe the same in-scope acceptance surface and be backed by real passing QA evidence, so the bounded Conjunction work can be treated as complete in substance at epic close."  
 "Implementation linkage:"  
 "PF10 frames PR-04 as binding real pass QA evidence into the close-pack"

Goal

Capture the current acceptance map, token matrix, viability log, step manifest, close-pack pair, and three canonical QA logs into one stable check-scoped evidence folder, then review them together as the final bounded acceptance surface for this epic.

Preconditions

* po-007 is complete.  
* Shared setup commands have already been run.

Setup

Command 1: mkdir \-p audit/qa/hde-epic029/checks/po-008

Numbered PO actions

1. Snapshot the acceptance map, token matrix, viability log, step manifest, close report, and close manifest.  
2. Snapshot the three canonical QA logs that the close-pack family relies on.  
3. Review the snapshot set as one bounded acceptance surface.  
4. Write the step receipt.

PO command(s)

Command 2: cp docs/acceptance\_map\_epic029.json audit/qa/hde-epic029/checks/po-008/acceptance\_map.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: docs/acceptance\_map\_epic029.json"  
 "Where found: head \-n 40 docs/acceptance\_map\_epic029.json"

Command 3: cp audit/qa/hde-epic029/token\_evidence\_matrix.md audit/qa/hde-epic029/checks/po-008/token\_evidence\_matrix.snapshot.md  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/qa/hde-epic029/token\_evidence\_matrix.md"  
 "Proof: \# HDE-EPIC029 Token ↔ Evidence Matrix"  
 "Where found: head \-n 60 audit/qa/hde-epic029/token\_evidence\_matrix.md"

Command 4: cp audit/qa/hde-epic029/acceptance\_map\_viability.log audit/qa/hde-epic029/checks/po-008/acceptance\_map\_viability.snapshot.log  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/qa/hde-epic029/acceptance\_map\_viability.log"  
 "Proof: summary: COVERED=9 PLANNED=0 MISSING=0"  
 "Where found: head \-n 40 audit/qa/hde-epic029/acceptance\_map\_viability.log"

Command 5: cp audit/qa/hde-epic029/qa\_step\_logs\_manifest.json audit/qa/hde-epic029/checks/po-008/qa\_step\_logs\_manifest.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/qa/hde-epic029/qa\_step\_logs\_manifest.json"  
 "Where found: head \-n 40 audit/qa/hde-epic029/qa\_step\_logs\_manifest.json"

Command 6: cp audit/EPIC-029\_close\_report.md audit/qa/hde-epic029/checks/po-008/close\_report.snapshot.md  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/EPIC-029\_close\_report.md"  
 "Proof: \# HDE-EPIC029 — Close Report"  
 "Where found: head \-n 40 audit/EPIC-029\_close\_report.md"

Command 7: cp audit/EPIC-029\_MANIFEST.json audit/qa/hde-epic029/checks/po-008/close\_manifest.snapshot.json  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/EPIC-029\_MANIFEST.json"  
 "Where found: head \-n 40 audit/EPIC-029\_MANIFEST.json"

Command 8: cp audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log audit/qa/hde-epic029/checks/po-008/po\_epic\_close\_live\_qa.snapshot.log  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log"  
 "Proof: \[exit\_code\] 0"  
 "Where found: head \-n 20 audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log"

Command 9: cp audit/qa/hde-epic029/checks/po-precommit/primary.log audit/qa/hde-epic029/checks/po-008/po\_precommit.snapshot.log  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/qa/hde-epic029/checks/po-precommit/primary.log"  
 "Proof: \[command\] ci/checks/check\_env\_pins.sh && ci/checks/check\_cli\_help.sh && ci/checks/check\_final\_lf.sh"  
 "Where found: head \-n 20 audit/qa/hde-epic029/checks/po-precommit/primary.log"

Command 10: cp audit/qa/hde-epic029/checks/po-postcommit/primary.log audit/qa/hde-epic029/checks/po-008/po\_postcommit.snapshot.log  
 SOURCE EXCERPT (verbatim):  
 "Path: audit/qa/hde-epic029/checks/po-postcommit/primary.log"  
 "Proof: \[command\] /workspaces/glow-hdengine-v2/.venv/bin/python tools/evidence/run\_sanity\_pipeline.py"  
 "Where found: head \-n 20 audit/qa/hde-epic029/checks/po-postcommit/primary.log"

Command 11.1: export CHECK\_ID='po-008'; export CHECK\_NAME='Final closeout records stay on one bounded acceptance surface and are backed by real passing QA evidence'; export COMMANDS\_JSON='\["cp docs/acceptance\_map\_epic029.json audit/qa/hde-epic029/checks/po-008/acceptance\_map.snapshot.json","cp audit/qa/hde-epic029/token\_evidence\_matrix.md audit/qa/hde-epic029/checks/po-008/token\_evidence\_matrix.snapshot.md","cp audit/qa/hde-epic029/acceptance\_map\_viability.log audit/qa/hde-epic029/checks/po-008/acceptance\_map\_viability.snapshot.log","cp audit/qa/hde-epic029/qa\_step\_logs\_manifest.json audit/qa/hde-epic029/checks/po-008/qa\_step\_logs\_manifest.snapshot.json","cp audit/EPIC-029\_close\_report.md audit/qa/hde-epic029/checks/po-008/close\_report.snapshot.md","cp audit/EPIC-029\_MANIFEST.json audit/qa/hde-epic029/checks/po-008/close\_manifest.snapshot.json","cp audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log audit/qa/hde-epic029/checks/po-008/po\_epic\_close\_live\_qa.snapshot.log","cp audit/qa/hde-epic029/checks/po-precommit/primary.log audit/qa/hde-epic029/checks/po-008/po\_precommit.snapshot.log","cp audit/qa/hde-epic029/checks/po-postcommit/primary.log audit/qa/hde-epic029/checks/po-008/po\_postcommit.snapshot.log"\]'; export ARTIFACTS\_JSON='\["audit/qa/hde-epic029/checks/po-008/primary.log","audit/qa/hde-epic029/checks/po-008/acceptance\_map.snapshot.json","audit/qa/hde-epic029/checks/po-008/token\_evidence\_matrix.snapshot.md","audit/qa/hde-epic029/checks/po-008/acceptance\_map\_viability.snapshot.log","audit/qa/hde-epic029/checks/po-008/qa\_step\_logs\_manifest.snapshot.json","audit/qa/hde-epic029/checks/po-008/close\_report.snapshot.md","audit/qa/hde-epic029/checks/po-008/close\_manifest.snapshot.json","audit/qa/hde-epic029/checks/po-008/po\_epic\_close\_live\_qa.snapshot.log","audit/qa/hde-epic029/checks/po-008/po\_precommit.snapshot.log","audit/qa/hde-epic029/checks/po-008/po\_postcommit.snapshot.log"\]'; export PF\_REFS\_JSON='\["PF10 — HDE-Build Notes","PF27 — Canon Plan Templates"\]'; export COMMAND\_PROVENANCE='Copy/paste from plan'; export INTENDED\_TOKENS\_JSON='\["TESTS\_PASS\_OK","QA\_PRECOMMIT\_CHECKLIST\_OK","QA\_POSTCOMMIT\_CHECKLIST\_OK"\]'; export CLAIMED\_TOKENS\_JSON='\[\]'

Command 11.2: after reviewing the actual step outcome, export PASS\_FAIL='PASS' if this step passes; otherwise export PASS\_FAIL='FAIL\_BEHAVIOR' or PASS\_FAIL='FAIL\_TOOLING' or PASS\_FAIL='TOOLING\_BLOCKED' as actually observed for this step; if \[ "${PASS\_FAIL}" \= 'PASS' \]; then export CLAIMED\_TOKENS\_JSON='\["TESTS\_PASS\_OK","QA\_PRECOMMIT\_CHECKLIST\_OK","QA\_POSTCOMMIT\_CHECKLIST\_OK"\]'; else export CLAIMED\_TOKENS\_JSON='\[\]'; fi

Command 11.3: run the embedded canonical PF27 header-writer snippet in the Step-log header schema expectations section and tee its single-line JSON output to audit/qa/hde-epic029/checks/po-008/primary.log

What to look for

* acceptance\_map.snapshot.json shows ready\_for\_close\_binding.  
* acceptance\_map\_viability.snapshot.log shows summary: COVERED=9 PLANNED=0 MISSING=0.  
* The three QA log snapshots are present and show passing evidence.  
* The close report and close manifest remain on the same bounded acceptance surface and do not widen the epic into a new public surface or a writer-runtime redesign.  
* The token matrix snapshot is present and aligns with the same bounded acceptance surface.

Expected result (PASS/FAIL predicates)

PASS if:

* all snapshot deliverables exist  
* the acceptance map shows ready\_for\_close\_binding  
* the viability snapshot shows COVERED=9 PLANNED=0 MISSING=0  
* the three QA log snapshots support the three temporary QA bridge tokens  
* the close-pack family stays on the same bounded Conjunction acceptance surface

FAIL\_BEHAVIOR if:

* the acceptance family contradicts itself about the in-scope closure surface  
* the close-pack family overclaims a new public surface or a widened writer/runtime scope

FAIL\_TOOLING if:

* any required snapshot command fails

TOOLING\_BLOCKED if:

* any required closeout artifact or QA log is missing at its proven repo path

Primary evidence artifact

* audit/qa/hde-epic029/checks/po-008/primary.log

Deliverables

* audit/qa/hde-epic029/checks/po-008/primary.log  
* audit/qa/hde-epic029/checks/po-008/acceptance\_map.snapshot.json  
* audit/qa/hde-epic029/checks/po-008/token\_evidence\_matrix.snapshot.md  
* audit/qa/hde-epic029/checks/po-008/acceptance\_map\_viability.snapshot.log  
* audit/qa/hde-epic029/checks/po-008/qa\_step\_logs\_manifest.snapshot.json  
* audit/qa/hde-epic029/checks/po-008/close\_report.snapshot.md  
* audit/qa/hde-epic029/checks/po-008/close\_manifest.snapshot.json  
* audit/qa/hde-epic029/checks/po-008/po\_epic\_close\_live\_qa.snapshot.log  
* audit/qa/hde-epic029/checks/po-008/po\_precommit.snapshot.log  
* audit/qa/hde-epic029/checks/po-008/po\_postcommit.snapshot.log

## **Review guardrails**

### **Hard blockers for plan approval/execution**

* Any check block that writes primary.log headers as ad hoc key-value text instead of canonical JSON header-writer output.  
* Any reintroduction of EVIDENCE\_ROOT or any other per-run root selector.  
* Any close-out deliverables section that omits the discovery artifact or the QA RCA and Doc Delta summary surfaces.  
* Any plan ending that omits this Review guardrails section.

### **Close-out deliverables**

At minimum, this run should leave:

* audit/qa/hde-epic029/checks/po-001/primary.log  
* audit/qa/hde-epic029/checks/po-002/primary.log  
* audit/qa/hde-epic029/checks/po-003/primary.log  
* audit/qa/hde-epic029/checks/po-004/primary.log  
* audit/qa/hde-epic029/checks/po-005/primary.log  
* audit/qa/hde-epic029/checks/po-006/primary.log  
* audit/qa/hde-epic029/checks/po-007/primary.log  
* audit/qa/hde-epic029/checks/po-008/primary.log

Required discovery and summary surfaces:

* audit/qa/hde-epic029/00\_meta/conjunction\_json\_surface\_inventory.md  
* audit/EPIC-029\_close\_report.md  
* audit/qa/hde-epic029/00\_meta/delta/patch.diff — DEFERRED unless Step-0B executes  
* audit/qa/hde-epic029/00\_meta/delta/changed\_files.txt — DEFERRED unless Step-0B executes

And the key final bounded-closeout snapshot family under audit/qa/hde-epic029/checks/po-008/:

* acceptance\_map.snapshot.json  
* token\_evidence\_matrix.snapshot.md  
* acceptance\_map\_viability.snapshot.log  
* qa\_step\_logs\_manifest.snapshot.json  
* close\_report.snapshot.md  
* close\_manifest.snapshot.json  
* po\_epic\_close\_live\_qa.snapshot.log  
* po\_precommit.snapshot.log  
* po\_postcommit.snapshot.log

ASK OK?  
