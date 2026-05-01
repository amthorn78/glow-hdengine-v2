## 1\) Live QA Plan

### Front matter

Epic ID: HDE-EPIC030

Plan type: Live QA Plan / Runbook

Execution venue: Codespaces

Target environment: dev for local/internal harness checks; prod-facing public contract is verified by repo-local public-output checks only

Plan revision: r13

Date (UTC): 2026-05-01

Operators (names-only): PO, IA, Kronos

#### Canon precedence statement (required)

PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.

Canon set:

* \* PF10 — HDE-Build Notes, relevant addenda: 2.1 HDE-EPIC030 Dissolution carry-forward conflict, 2.2 PF09.2 history-lock narrowing, 2.3 Planning markup wrappers, 2.4 ASK OK approval sentinel, 2.5 Retrieval-first proof posture, 2.6 PR01 HDE-EPIC030, 2.7 PR02 HDE-EPIC030, 2.8 PR03 HDE-EPIC030, 2.9 PR04 HDE-EPIC030, 2.10 PR05 HDE-EPIC030, 2.20 po-006 remediation ADR set, 2.23 Remediation PR-02 birth-only no-user proof, 2.24 OPS-02 birth-only vendor-backed no-user smoke completion contract    
* PF04 — HDE-Governance, §2.0 token registry and acceptance invariants  
* PF05 — HDE-CLI-API-Vendor-Ref, public bands-only and CLI/API semantics  
* PF06 — Epic Process Guide, §0.4.1 Discovery and QA RCA/Doc Delta  
* PF09.2 — HDE Build Checklist Dissolution, phase scope and affected Dissolution subtasks  
* PF12 — HDE Schemas & Artifacts, evidence index, mirror, path-proof, close-pack paths  
* PF19 — Glow QA Guide, evidence posture, tooling vs behavior classification, dependency readiness  
* PF23 — Reality Audits, planning-time repo-reality context only  
* PF27 — Canon Plan Templates, Live QA Plan structure and step-log posture

Note: PF20 may be used only for historical record context, never as a source of current requirements.

### Scope statement

This plan evaluates the following in-scope surfaces and checks:

* PO-001 Dissolution closeout boundary and no public-surface widening  
* PO-002 zero-weight user intent handoff into sampler exclusion behavior  
* PO-003 viewer-preference normalization validity and determinism  
* PO-004 dev-only candidate-selection harness boundary, determinism, and safe output  
* PO-005 compatibility order-neutrality, identity stability, and category-order coherence  
* PO-006 public user-facing compatibility output remains band-only and numeric-free, and completed OPS-02 evidence proves the vendor-backed birth-only no-user implementation-validation smoke without claiming QA PASS, Live QA completion, PF09 status change, or epic closure    
* PO-007 band threshold and tuning single ownership  
* PO-008 band tuning comparison and identity proof  
* PO-009 category-framework mechanics, comparison, and evidence binding  
* PO-010 generated-proof fail-closed posture  
* PO-011 all active implementation slices trace through governed evidence  
* PO-012 already-complete foundations remain reused history  
* PO-013 QA interpretation separates repo-supported completion from permanent checklist drainage  
* PO-014 full post-implementation all-slice coherence  
* PO-015 baseline execution context, reachable surfaces, and tool-health posture  
* PO-016 final QA interpretation and evidence-backed meaning  
* PO-017 undrained documentation deltas are not QA blockers by themselves

This plan explicitly excludes:

* public route creation  
* public-surface redesign  
* production-hardening or later-phase Coagulation work  
* PF-canon editing as a QA execution task  
* new acceptance-token creation  
* VCS workflow, branch, commit, or PR instructions

#### PF10 overrides / conflicts (if any)

* PF10 Addendum 2.1 — Treats HDE-DISS005.2, HDE-DISS005.3, HDE-DISS005.4, HDE-DISS006.3, HDE-DISS006.4, and HDE-DISS006.5 as active HDE-EPIC030 Dissolution scope.  
* PF10 Addendum 2.2 — Narrows PF09.2 history-lock wording so only HDE-DISS005.1, HDE-DISS006.1, and HDE-DISS006.2 remain history-only and already complete for this epic.  
* PF10 Addenda 2.6 through 2.10 — Frame PR01 through PR05 as implementation slices with repo-supported proof that still require Live QA close-stage interpretation.  
* PF10 Addendum 2.4 — Requires ASK OK? as approval sentinel for plans submitted for approval.  
* PF10 Addendum 2.1 — Treats HDE-DISS005.2, HDE-DISS005.3, HDE-DISS005.4, HDE-DISS006.3, HDE-DISS006.4, and HDE-DISS006.5 as active HDE-EPIC030 Dissolution scope.    
* PF10 Addendum 2.2 — Narrows PF09.2 history-lock wording so only HDE-DISS005.1, HDE-DISS006.1, and HDE-DISS006.2 remain history-only and already complete for this epic.    
* PF10 Addenda 2.6 through 2.10 — Frame PR01 through PR05 as implementation slices with repo-supported proof that still require Live QA close-stage interpretation.    
* PF10 Addendum 2.20 — Establishes po-006 remediation proof classes: public numeric-free output proof, internal/admin compatibility compute proof, and vendor-backed no-user behavior proof. It also establishes that the controlled vendor smoke is implementation validation only, not QA PASS, Live QA completion, or epic closure.    
* PF10 Addendum 2.23 — Records that the accepted PR-02 remediation proof is birth-only at caller input: no caller \`person\_uid\` and no caller \`user\_id\`, while preserving \`/api/compat/v1\` as internal/admin and preserving public Reader bands-only/numeric-free posture.    
* PF10 Addendum 2.24 — Establishes the OPS-02 completion contract for the birth-only vendor-backed no-user smoke, including \`CLI\_LOCAL\_VENDOR\_SMOKE\`, birth-only command shape, required OPS-02 evidence outputs, classification rules, and the statement that OPS-02 can support later PF09.2 review language but does not itself authorize immediate PF09 status change.    
* PF10 Addendum 2.4 — Requires ASK OK? as approval sentinel for plans submitted for approval.    
* PF10 Addendum 2.5 — Requires retrieval-first, proof-first review posture for plan and repo analysis.


### PF23 anchors

PF23 was consulted read-only during QA planning for repo-reality context, component boundaries, and locus framing. It is informational only and is not an acceptance token, deliverable, execution step, or blocker source by itself.

Planning-time loci touched by this runbook:

* engine/validation/viewer\_prefs.py  
* engine/sampler/core.py  
* engine/compat/compute.py  
* engine/compat/thresholds.py  
* engine/magic10/thresholds.py  
* engine/http/compat\_handler.py  
* adapter/http\_reader.py  
* pyproject.toml  
* engine/cli/main.py  
* docs/ENDPOINTS\_CATALOG.json  
* docs/evidence/INDEX.json  
* docs/evidence/INDEX.sha256  
* artifacts/evidence\_index.jsonl  
* audit/qa/hde-epic030/pr-01/  
* audit/qa/hde-epic030/pr-02/  
* audit/qa/hde-epic030/pr-03/  
* audit/qa/hde-epic030/pr-04/  
* audit/qa/hde-epic030/pr-05/  
* tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py  
* tools/evidence/generate\_epic030\_pr02\_sampler\_harness\_evidence.py  
* tools/evidence/generate\_epic030\_pr03\_compat\_evidence.py  
* tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py  
* tools/evidence/generate\_epic030\_pr05\_category\_framework\_evidence.py  
* scripts/qa/dev\_sampler\_healthcheck.py  
* scripts/qa/dev\_sampler\_live\_qa.py  
* tests/unit/test\_viewer\_prefs\_normalization.py  
* tests/unit/test\_sampler\_core.py  
* tests/adapter/test\_dev\_sampler\_http.py  
* tests/cli/test\_dev\_sampler\_cli.py  
* tests/compat/test\_compat\_public\_ab\_ba\_identity.py  
* tests/compat/test\_compat\_public\_lf\_bom.py  
* tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py  
* tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py

### Environment and rails posture

#### Determinism pins (canonical pins only)

When producing governed bytes, evidence artifacts, canonical JSON, hash inputs, or compare logs, use:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

Do not add non-canonical determinism pins as runbook requirements. PYTHONHASHSEED is not a required pin for this plan.

#### Rails posture (explicit)

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

Rails change by check:

* po-004 optional live HTTP subcheck may use DEV\_SAMPLER\_URL only when the PO has a confirmed non-prod dev sampler URL. That subcheck stays APP\_ENV=dev. It must not target prod. If DEV\_SAMPLER\_URL is missing, the live HTTP subcheck is TOOLING\_BLOCKED, not FAIL\_BEHAVIOR.   
*  po-006 does not run a vendor command during Live QA. po-006 consumes completed OPS-02 evidence and verifies that the prior PO-run controlled smoke used the birth-only \`CLI\_LOCAL\_VENDOR\_SMOKE\` posture with vendor source, no caller \`user\_id\`, no caller \`person\_uid\`, and no app user IDs.   
* OPS-02 may show a prior controlled vendor step using \`SAFE\_MODE=0\` and \`ALLOW\_NETWORK=1\`; that open-rails posture belongs to the completed OPS evidence, not to a new QA-run vendor command.    
* All other checks remain closed rails.

No VCS workflow content:

* Do not use branch, commit SHA, PR ID, working-tree cleanliness, checkout, merge, rebase, commit, push, or pull as PASS or FAIL criteria.  
* Optional repo-root sanity may be done outside this plan, but it is non-gating.

### PO inputs needed

**Required for baseline closed-rails execution:**

* None beyond access to the repository in Codespaces and permission to create governed QA artifacts under audit/qa/hde-epic030/.

**Required for po-006 OPS-02 evidence interpretation:**

* Completed OPS-02 evidence under audit/ops/hde-epic030/ops-02/.  
* Required OPS-02 evidence files include:  
  * vendor\_command.txt  
  * sample\_birth\_inputs.json  
  * redacted\_env\_presence.json  
  * target\_disposition.md  
  * pr02\_runtime\_binding.md  
  * request\_summary.txt  
  * result\_summary.md  
  * pfcanon\_ops02\_completion\_matrix.md  
  * execution\_classification.md  
  * stdout.json  
  * stderr.log  
  * exit\_code.txt  
  * stdout\_parse\_validation.md  
  * stdout.json.sha256  
  * files\_sha256.txt  
  * ops02\_complete\_action\_log\_and\_evidence\_final.md  
* If the completed OPS-02 consolidated evidence bundle has a reviewed copy name such as ops02\_complete\_action\_log\_and\_evidence\_final\_v2.md outside the repo, do not treat that external name as a canonical repo path. The QA check should consume the repo-resident OPS-02 evidence family under audit/ops/hde-epic030/ops-02/.

**Optional for po-004 live HTTP harness execution:**

* DEV\_SAMPLER\_URL, only if PF07 or the current Codespaces environment already provides a confirmed non-prod dev sampler URL.  
* If DEV\_SAMPLER\_URL is absent or unclear, do not guess host, port, or endpoint. Mark the live HTTP subcheck as TOOLING\_BLOCKED and continue with source, CLI, and pytest-backed harness checks.

No secret values are required for this plan. Do not record secrets in logs.

### Evidence posture and directory structure

#### Epic QA root normalization (required)

Stable epic QA root:

* audit/qa/hde-epic030/

Check-centric roots:

* audit/qa/hde-epic030/checks/po-001/  
* audit/qa/hde-epic030/checks/po-002/  
* audit/qa/hde-epic030/checks/po-003/  
* audit/qa/hde-epic030/checks/po-004/  
* audit/qa/hde-epic030/checks/po-005/  
* audit/qa/hde-epic030/checks/po-006/  
* audit/qa/hde-epic030/checks/po-007/  
* audit/qa/hde-epic030/checks/po-008/  
* audit/qa/hde-epic030/checks/po-009/  
* audit/qa/hde-epic030/checks/po-010/  
* audit/qa/hde-epic030/checks/po-011/  
* audit/qa/hde-epic030/checks/po-012/  
* audit/qa/hde-epic030/checks/po-013/  
* audit/qa/hde-epic030/checks/po-014/  
* audit/qa/hde-epic030/checks/po-015/  
* audit/qa/hde-epic030/checks/po-016/  
* audit/qa/hde-epic030/checks/po-017/

Meta root:

* audit/qa/hde-epic030/00\_meta/

Doc-delta root:

* audit/docdeltas/

Per-run directories are prohibited. Do not create run-id, timestamped, or fresh-run roots.

#### **Recommended canonical layout (default for this run)**

* audit/qa/hde-epic030/00\_meta/doc\_deltas.md  
* audit/qa/hde-epic030/00\_meta/qa\_helpers.sh  
* audit/docdeltas/hde-epic030\_doc\_deltas.md  
* audit/qa/hde-epic030/checks/po-015/discovery.json  
* audit/qa/hde-epic030/checks/\<check-id\>/primary.log  
* audit/qa/hde-epic030/checks/\<check-id\>/stdout.log  
* audit/qa/hde-epic030/checks/\<check-id\>/stderr.log  
* audit/qa/hde-epic030/checks/\<check-id\>/exit\_code.txt  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic030/acceptance\_map\_viability.log  
* audit/qa/hde-epic030/token\_evidence\_matrix.md  
* docs/acceptance\_map\_epic030.json  
* audit/EPIC-030\_QA\_RCA.md  
* audit/EPIC-030\_close\_report.md  
* audit/EPIC-030\_MANIFEST.json

Existing implementation-slice evidence roots:

* audit/qa/hde-epic030/pr-01/  
* audit/qa/hde-epic030/pr-02/  
* audit/qa/hde-epic030/pr-03/  
* audit/qa/hde-epic030/pr-04/  
* audit/qa/hde-epic030/pr-05/

Those PR roots are existing governed implementation evidence families. Live QA check outputs must still land under audit/qa/hde-epic030/checks/\<check-id\>/.

#### **Step-log header schema expectations (minimum; required)**

Every primary.log must begin with a single-line JSON header using schema\_version pf27.step\_log\_header.v1.

Required header keys:

* schema\_version  
* timestamp\_utc  
* check\_id  
* check\_name  
* status  
* fail\_status  
* command  
* command\_provenance  
* exit\_code  
* evidence\_artifacts  
* captured\_env  
* pf\_refs  
* intended\_tokens  
* claimed\_tokens

Canonical step-log header writer for every check:

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
 exit\_code\_raw \= env("EXIT\_CODE", "")  
 exit\_code \= int(exit\_code\_raw) if exit\_code\_raw \!= "" else None  
 if status \== "PASS" and exit\_code \!= 0:  
 raise SystemExit("PASS requires EXIT\_CODE=0")  
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
 "exit\_code": exit\_code,  
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

For this plan, each step uses the PF27 canonical inline header writer directly. Do not create or invoke a QA-local header helper.

### Mandatory Step-0 artifacts

These are execution deliverables and must be mechanically produced before behavior-level checks.

#### **Step-0A — Discovery posture**

Goal: create the stable QA roots, capture runtime context and reachable-surface inventory, and verify tool health without creating a QA-local header helper.

Required dependencies:

* Python 3  
* Bash  
* grep  
* test  
* repository files listed in the PF23 anchors section

Preflight check:

* python \--version  
* python \-m pytest \--version  
* test \-f pyproject.toml  
* test \-f engine/cli/main.py  
* test \-f docs/evidence/INDEX.json  
* test \-f artifacts/evidence\_index.jsonl

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt

If still unavailable:

* TOOLING\_BLOCKED for all executable checks that depend on the missing tool or file.

Command 1: mkdir \-p audit/qa/hde-epic030/00\_meta audit/docdeltas audit/qa/hde-epic030/checks/po-001 audit/qa/hde-epic030/checks/po-002 audit/qa/hde-epic030/checks/po-003 audit/qa/hde-epic030/checks/po-004 audit/qa/hde-epic030/checks/po-005 audit/qa/hde-epic030/checks/po-006 audit/qa/hde-epic030/checks/po-007 audit/qa/hde-epic030/checks/po-008 audit/qa/hde-epic030/checks/po-009 audit/qa/hde-epic030/checks/po-010 audit/qa/hde-epic030/checks/po-011 audit/qa/hde-epic030/checks/po-012 audit/qa/hde-epic030/checks/po-013 audit/qa/hde-epic030/checks/po-014 audit/qa/hde-epic030/checks/po-015 audit/qa/hde-epic030/checks/po-016 audit/qa/hde-epic030/checks/po-017

Command 2: bash \-lc 'set \-o pipefail; LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev python \--version \> audit/qa/hde-epic030/checks/po-015/python\_version.txt 2\> audit/qa/hde-epic030/checks/po-015/python\_version.stderr; python \-m pytest \--version \> audit/qa/hde-epic030/checks/po-015/pytest\_version.txt 2\> audit/qa/hde-epic030/checks/po-015/pytest\_version.stderr; rc=$?; printf "%s\\n" "$rc" \> audit/qa/hde-epic030/checks/po-015/preflight\_rc.txt; test "$rc" \= "0"'

Command 3: python \-c 'import json, os, pathlib, sys; paths=\["pyproject.toml","engine/cli/main.py","engine/validation/viewer\_prefs.py","engine/sampler/core.py","engine/compat/compute.py","engine/compat/thresholds.py","engine/magic10/thresholds.py","engine/http/compat\_handler.py","adapter/http\_reader.py","docs/ENDPOINTS\_CATALOG.json","docs/evidence/INDEX.json","docs/evidence/INDEX.sha256","artifacts/evidence\_index.jsonl","audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json","audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json","audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log","audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json","audit/qa/hde-epic030/pr-05/category\_framework\_binding.log"\]; data={"schema":"hde\_epic030.live\_qa\_discovery.v1","python":sys.version.split()\[0\],"rails":{"SAFE\_MODE":os.environ.get("SAFE\_MODE","1"),"ALLOW\_NETWORK":os.environ.get("ALLOW\_NETWORK","0"),"APP\_ENV":os.environ.get("APP\_ENV","dev"),"LC\_ALL":os.environ.get("LC\_ALL","C"),"LANG":os.environ.get("LANG","C"),"TZ":os.environ.get("TZ","UTC")},"paths":{p:pathlib.Path(p).exists() for p in paths},"surfaces":\["/api/compat/v1","/internal/dev/sampler","/reader","/dev/sampler/conjunction"\],"constraints":\["no public widening","no per-run root","documentation drainage is not a blocker by itself"\]}; pathlib.Path("audit/qa/hde-epic030/checks/po-015/discovery.json").write\_text(json.dumps(data,sort\_keys=True,separators=(",",":"))+"\\n",encoding="utf-8")'

Command 4: PASS\_FAIL="$(test "$(cat audit/qa/hde-epic030/checks/po-015/preflight\_rc.txt)" \= "0" && printf PASS || printf TOOLING\_BLOCKED)" EXIT\_CODE="$(cat audit/qa/hde-epic030/checks/po-015/preflight\_rc.txt)" CHECK\_ID="po-015" CHECK\_NAME="Before behavior-level Live QA begins, the QA plan must establish the baseline execution context, reachable surfaces, and tool-health posture." COMMAND\_PROVENANCE="Copy/paste from plan" COMMANDS\_JSON='\["python \--version","python \-m pytest \--version","discovery path inventory"\]' ARTIFACTS\_JSON='\["audit/qa/hde-epic030/checks/po-015/primary.log","audit/qa/hde-epic030/checks/po-015/discovery.json","audit/qa/hde-epic030/checks/po-015/python\_version.txt","audit/qa/hde-epic030/checks/po-015/pytest\_version.txt","audit/qa/hde-epic030/checks/po-015/preflight\_rc.txt"\]' PF\_REFS\_JSON='\["PF06 — Epic Process Guide","PF19 — Glow QA Guide","PF27 — Canon Plan Templates"\]' INTENDED\_TOKENS\_JSON='\[\]' CLAIMED\_TOKENS\_JSON='\[\]' SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python \- \<\< 'PY' \> audit/qa/hde-epic030/checks/po-015/primary.log  
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
 exit\_code\_raw \= env("EXIT\_CODE", "")  
 exit\_code \= int(exit\_code\_raw) if exit\_code\_raw \!= "" else None  
 if status \== "PASS" and exit\_code \!= 0:  
 raise SystemExit("PASS requires EXIT\_CODE=0")  
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
 "exit\_code": exit\_code,  
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
 cat audit/qa/hde-epic030/checks/po-015/discovery.json \>\> audit/qa/hde-epic030/checks/po-015/primary.log

What to look for:

* discovery.json exists and records rails, tool health, and expected surfaces.  
* Any missing repo-locus path is recorded as false in discovery.json, not assumed present.  
* If Python or pytest is unavailable after install action, all dependent behavior checks are TOOLING\_BLOCKED.

Required deliverables:

* audit/qa/hde-epic030/checks/po-015/primary.log  
* audit/qa/hde-epic030/checks/po-015/discovery.json

PASS criteria:

* primary.log begins with a pf27.step\_log\_header.v1 JSON header.  
* discovery.json exists and records rails, tool health, and all checked loci.  
* Required tools are available.

FAIL criteria:

* FAIL\_TOOLING or TOOLING\_BLOCKED if Python, pytest, or the stable repo loci cannot be verified.  
* FAIL\_BEHAVIOR is not used for dependency or setup failure.

  #### **Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**

Goal: mechanically record documentation-drainage candidates and current source-of-truth boundaries without treating drainage as a QA blocker.

Required dependencies:

* Python 3  
* audit/qa/hde-epic030/00\_meta/ exists from Step-0A

Preflight check:

* test \-d audit/qa/hde-epic030/00\_meta

If missing, activation/install action:

* Re-run Step-0A.

If still unavailable:

* TOOLING\_BLOCKED for Step-0B.

Command 1: mkdir \-p audit/docdeltas audit/qa/hde-epic030/00\_meta

Command 2: python \- \<\< 'PY'  
 from pathlib import Path

body \= "\\n".join(\[  
 "\# HDE-EPIC030 Doc Deltas",  
 "",  
 "Status: GENERATED BY STEP-0B",  
 "",  
 "\#\# BLOCKERS",  
 "",  
 "no deltas",  
 "",  
 "\#\# CAVEATS",  
 "",  
 "CAV-001 — PF09.2 history-lock narrowing for HDE-DISS005 and HDE-DISS006 remains a later drainage candidate.",  
 "CAV-002 — HDE-EPIC030 implementation support may be repo-supported before permanent PF09.2 drainage.",  
 "CAV-003 — Documentation drainage is not a QA blocker by itself when implementation truth and governed proof are otherwise complete.",  
 "",  
 \]) \+ "\\n"

Path("audit/docdeltas/hde-epic030\_doc\_deltas.md").write\_text(body, encoding="utf-8")  
 Path("audit/qa/hde-epic030/00\_meta/doc\_deltas.md").write\_text(body, encoding="utf-8")  
 PY

Command 3: PASS\_FAIL=PASS EXIT\_CODE=0 CHECK\_ID="step-0b-doc-delta-capture" CHECK\_NAME="Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)" COMMAND\_PROVENANCE="Copy/paste from plan" COMMANDS\_JSON='\["create HDE-EPIC030 doc delta files"\]' ARTIFACTS\_JSON='\["audit/docdeltas/hde-epic030\_doc\_deltas.md","audit/qa/hde-epic030/00\_meta/doc\_deltas.md"\]' PF\_REFS\_JSON='\["PF06 — Epic Process Guide","PF10 — HDE-Build Notes","PF19 — Glow QA Guide","PF27 — Canon Plan Templates"\]' INTENDED\_TOKENS\_JSON='\[\]' CLAIMED\_TOKENS\_JSON='\[\]' SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python \- \<\< 'PY' \> audit/qa/hde-epic030/00\_meta/step\_0b\_primary.log  
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
 exit\_code\_raw \= env("EXIT\_CODE", "")  
 exit\_code \= int(exit\_code\_raw) if exit\_code\_raw \!= "" else None  
 if status \== "PASS" and exit\_code \!= 0:  
 raise SystemExit("PASS requires EXIT\_CODE=0")  
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
 "exit\_code": exit\_code,  
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
 cat audit/qa/hde-epic030/00\_meta/doc\_deltas.md \>\> audit/qa/hde-epic030/00\_meta/step\_0b\_primary.log

Required deliverables:

* audit/docdeltas/hde-epic030\_doc\_deltas.md  
* audit/qa/hde-epic030/00\_meta/doc\_deltas.md  
* audit/qa/hde-epic030/00\_meta/step\_0b\_primary.log

PASS criteria:

* Both doc-delta files exist.  
* Both doc-delta files contain a BLOCKERS section and a CAVEATS section, or explicitly output "no deltas" when empty.  
* Every listed BLOCKERS or CAVEATS finding uses a stable ID beginning with BLK- or CAV-.  
* The files identify doc-delta candidates without making drainage an execution gate.

FAIL criteria:

* FAIL\_TOOLING if the files cannot be created.  
* FAIL\_BEHAVIOR if either file lacks BLOCKERS/CAVEATS classification or an explicit no-deltas posture.  
* FAIL\_BEHAVIOR if the text claims drainage is required before QA can pass.

### Runbook Check Matrix

| Order | Check ID | Step name copied from guide | Status before execution | Primary deliverable |
| :---- | :---- | :---- | :---- | :---- |
| 1 | po-001 | The epic must remain a Dissolution closeout of internal and admin-only behavior, without widening the public user-facing contract. | NOT RUN | audit/qa/hde-epic030/checks/po-001/primary.log |
| 2 | po-002 | Zero-weight user intent must be preserved through normalization and lead to the intended candidate exclusion behavior. | NOT RUN | audit/qa/hde-epic030/checks/po-002/primary.log |
| 3 | po-003 | Viewer-preference normalization must reject invalid input while preserving deterministic, stable output for valid input. | NOT RUN | audit/qa/hde-epic030/checks/po-003/primary.log |
| 4 | po-004 | The dev-only candidate-selection harness must remain non-public, environment-bounded, deterministic, and limited to safe diagnostic output. | NOT RUN | audit/qa/hde-epic030/checks/po-004/primary.log |
| 5 | po-005 | Compatibility behavior must be proven order-neutral, identity-stable, and category-order coherent for the implemented slice. | NOT RUN | audit/qa/hde-epic030/checks/po-005/primary.log |
| 6 | po-006 | Public user-facing compatibility output must remain band-only and free of numeric compatibility details, and OPS-02 must show birth-only vendor-backed no-user implementation-validation evidence without claiming QA PASS, Live QA completion, PF09 status change, or epic closure. | NOT RUN | audit/qa/hde-epic030/checks/po-006/primary.log |
| 7 | po-007 | Band threshold and tuning behavior must use the existing single ownership model and must not introduce a duplicate home. | NOT RUN | audit/qa/hde-epic030/checks/po-007/primary.log |
| 8 | po-008 | Band tuning proof must show that comparisons and identity behavior are current, complete, and based on the final implemented logic. | NOT RUN | audit/qa/hde-epic030/checks/po-008/primary.log |
| 9 | po-009 | Category-framework behavior must prove per-channel mechanics, category comparison, and evidence binding agree before the result is accepted. | NOT RUN | audit/qa/hde-epic030/checks/po-009/primary.log |
| 10 | po-010 | Any generated proof used for this epic must fail closed when the claimed predicate is missing, stale, or contradicted. | NOT RUN | audit/qa/hde-epic030/checks/po-010/primary.log |
| 11 | po-011 | The implementation proof for each active slice must be current, mutually coherent, and traceable through the governed evidence system. | NOT RUN | audit/qa/hde-epic030/checks/po-011/primary.log |
| 12 | po-012 | Previously complete foundation work must be treated as reused history, not as newly implemented HDE-EPIC030 work. | NOT RUN | audit/qa/hde-epic030/checks/po-012/primary.log |
| 13 | po-013 | QA interpretation must distinguish implemented completion support from permanent checklist drainage. | NOT RUN | audit/qa/hde-epic030/checks/po-013/primary.log |
| 14 | po-014 | The full post-implementation state must be proven coherent after all implementation slices and documentation-facing updates are considered together. | NOT RUN | audit/qa/hde-epic030/checks/po-014/primary.log |
| 15 | po-015 | Before behavior-level Live QA begins, the QA plan must establish the baseline execution context, reachable surfaces, and tool-health posture. | NOT RUN | audit/qa/hde-epic030/checks/po-015/primary.log |
| 16 | po-016 | The final QA interpretation must explain what was run, what the outcomes mean, what evidence supports them, and whether canon follow-up is required. | NOT RUN | audit/qa/hde-epic030/checks/po-016/primary.log |
| 17 | po-017 | Undrained documentation deltas must not be treated as QA blockers when implementation truth and governed proof are otherwise complete. | NOT RUN | audit/qa/hde-epic030/checks/po-017/primary.log |

Execution dependency note: Run Step-0A and Step-0B first. Then run po-001 through po-017 in matrix order. po-015 is listed in guide order but its discovery artifact is created in Step-0A before behavior-level checks.

### Token coverage and evidence binding (required)

This plan does not mint new tokens.

Default token posture for step logs:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

Existing tokens may be claimed only when the step directly verifies them and the produced evidence supports the claim. Do not claim any token on non-PASS status.

Existing token names that may be relevant only if directly verified:

* TESTS\_PASS\_OK  
* JSON\_CANONICAL\_CHECK\_OK  
* COMPOSITE\_ABBA\_IDENTITY\_OK  
* TWO\_RUN\_IDENTITY\_OK  
* EVIDENCE\_INDEX\_UPDATED\_OK  
* EVIDENCE\_INDEX\_HASH\_OK  
* EVIDENCE\_INDEX\_MIRROR\_OK  
* MACHINE\_MIRROR\_UPDATED\_OK  
* EVIDENCE\_PATHS\_VALIDATED\_OK

Acceptance-map, token-matrix, and close-pack artifacts are NOT RUN until closeout steps execute.

### **Check Blocks**

Header-generation correction for all Check Blocks:

* Step-0A, Step-0B, and every Check Block must use the PF27 canonical inline header writer shown in the Step-log header schema expectations section.  
* No Check Block may require, preflight, invoke, or depend on a QA-local header helper.  
* For each Check Block, export that Check Block’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer to write that Check Block’s primary.log before appending the named proof artifacts.  
* If the PF27 inline writer cannot be run with that Check Block’s exported inputs, classify the affected step as FAIL\_TOOLING or TOOLING\_BLOCKED according to that step’s dependency posture; do not keep or substitute a QA-local header helper.

#### **CHECK po-001: The epic must remain a Dissolution closeout of internal and admin-only behavior, without widening the public user-facing contract.**

Goal:

Prove that the current HDE-EPIC030 close-stage scope stays internal, admin-only, and dev-only. This check must not create or validate a new public route.

Required dependencies:

* Python 3  
* docs/ENDPOINTS\_CATALOG.json  
* engine/http/compat\_handler.py  
* adapter/http\_reader.py

Preflight check:

* test \-f docs/ENDPOINTS\_CATALOG.json  
* test \-f engine/http/compat\_handler.py  
* test \-f adapter/http\_reader.py

If missing, activation/install action:

* No package install can create missing repo loci. Rerun repo audit or restore missing files.

If still unavailable:

* TOOLING\_BLOCKED with RERUN AUDIT REQUIRED for the missing locus.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Inspect endpoint catalog and route source for only the seeded existing routes.  
2. Capture route and classification evidence under po-001.  
3. Classify any new public route or ungated public compat exposure as FAIL\_BEHAVIOR.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-001

Command 2: python \- \<\< 'PY'  
 import json  
 import pathlib  
 import re  
 import sys

out \= pathlib.Path("audit/qa/hde-epic030/checks/po-001")  
 catalog \= pathlib.Path("docs/ENDPOINTS\_CATALOG.json")  
 compat \= pathlib.Path("engine/http/compat\_handler.py")  
 reader \= pathlib.Path("adapter/http\_reader.py")  
 required \= \[catalog, compat, reader\]  
 missing \= \[str(p) for p in required if not p.exists()\]  
 lines \= \["schema: hde\_epic030.po001.surface\_inventory.v1"\]  
 status \= "PASS"

if missing:  
 status \= "TOOLING\_BLOCKED"  
 lines.append("missing\_loci: " \+ ", ".join(missing))  
 else:  
 catalog\_text \= catalog.read\_text(encoding="utf-8")  
 compat\_text \= compat.read\_text(encoding="utf-8")  
 reader\_text \= reader.read\_text(encoding="utf-8")  
 public\_findings \= \[\]  
 for route in \["/api/compat/v1", "/internal/dev/sampler", "/reader", "/dev/sampler/conjunction"\]:  
 present \= route in catalog\_text or route in compat\_text or route in reader\_text  
 lines.append(f"route:{route}:present={present}")  
 if "/api/compat/v1" in catalog\_text and "internal\_admin" not in catalog\_text:  
 public\_findings.append("/api/compat/v1 missing internal\_admin classification in catalog text")  
 if "/internal/dev/sampler" in catalog\_text and "dev" not in catalog\_text:  
 public\_findings.append("/internal/dev/sampler missing dev/internal classification in catalog text")  
 new\_public \= \[  
 m.group(0)  
 for m in re.finditer(r'"/\[^"\]+"', catalog\_text)  
 if "public" in catalog\_text\[max(0, m.start() \- 200):m.end() \+ 200\].lower()  
 and m.group(0).strip('"') not in {"/reader"}  
 \]  
 if public\_findings or new\_public:  
 status \= "FAIL\_BEHAVIOR"  
 for item in public\_findings:  
 lines.append("public\_surface\_finding: " \+ item)  
 for item in sorted(set(new\_public)):  
 lines.append("unexpected\_public\_route\_literal: " \+ item)  
 else:  
 lines.append("no\_public\_widening\_found: True")

(out / "surface\_inventory.txt").write\_text("\\n".join(lines) \+ "\\n", encoding="utf-8")  
 (out / "stderr.log").write\_text("", encoding="utf-8")  
 (out / "exit\_code.txt").write\_text({"PASS": "0", "FAIL\_BEHAVIOR": "1", "TOOLING\_BLOCKED": "2"}\[status\] \+ "\\n", encoding="utf-8")  
 raise SystemExit(0)  
 PY

Command 3: Export PASS\_FAIL, EXIT\_CODE, CHECK\_ID="po-001", CHECK\_NAME="The epic must remain a Dissolution closeout of internal and admin-only behavior, without widening the public user-facing contract.", COMMAND\_PROVENANCE="QA-created inline command", COMMANDS\_JSON, ARTIFACTS\_JSON, PF\_REFS\_JSON, INTENDED\_TOKENS\_JSON, CLAIMED\_TOKENS\_JSON, SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev, LC\_ALL=C, LANG=C, and TZ=UTC. Run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-001/primary.log. Then append audit/qa/hde-epic030/checks/po-001/surface\_inventory.txt to audit/qa/hde-epic030/checks/po-001/primary.log.

What to look for:

* /api/compat/v1 remains internal\_admin or equivalent non-public classification.  
* /internal/dev/sampler remains internal/dev.  
* /reader remains the existing cataloged reader surface and is not widened by this epic.  
* No new public route appears in this check output.

Required deliverables:

* audit/qa/hde-epic030/checks/po-001/primary.log  
* audit/qa/hde-epic030/checks/po-001/surface\_inventory.txt  
* audit/qa/hde-epic030/checks/po-001/exit\_code.txt

PASS criteria tied to deliverables:

* surface\_inventory.txt contains only existing seeded route families and no new HDE-EPIC030 public route.  
* primary.log begins with the PF27 header and records PASS.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if a new public route or public compat widening is found.  
* TOOLING\_BLOCKED if seeded source or catalog files are missing.

Blocked posture:

* RERUN AUDIT REQUIRED for any unproven route or catalog locus.

#### **CHECK po-002: Zero-weight user intent must be preserved through normalization and lead to the intended candidate exclusion behavior.**

Goal:

Prove zero-weight intent flows from normalized viewer preferences into sampler exclusion behavior.

Required dependencies:

* Python 3  
* pytest  
* tests/unit/test\_viewer\_prefs\_normalization.py  
* tests/unit/test\_sampler\_core.py  
* tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tests/unit/test\_viewer\_prefs\_normalization.py  
* test \-f tests/unit/test\_sampler\_core.py  
* test \-f tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo or evidence generator loci.

If still unavailable:

* TOOLING\_BLOCKED with RERUN AUDIT REQUIRED for the missing test or generator locus.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the normalization and sampler unit tests with explicit test-file identities.  
2. Execute the PR-01 normalization evidence generator with its audit-proven script path.  
3. Confirm zero\_weight\_handoff.json remains present and expresses sampler exclusion.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-002

Command 2: bash \-lc 'set \+e; python \-m pytest tests/unit/test\_viewer\_prefs\_normalization.py tests/unit/test\_sampler\_core.py \> audit/qa/hde-epic030/checks/po-002/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-002/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-002/pytest\_rc.txt; python tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py \> audit/qa/hde-epic030/checks/po-002/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-002/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-002/generator\_rc.txt; if \[ "$pytest\_rc" \-eq 0 \] && \[ "$generator\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-002/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-002/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-002/primary.log. Then append audit/qa/hde-epic030/checks/po-002/pytest\_stdout.log and audit/qa/hde-epic030/checks/po-002/generator\_stdout.log to audit/qa/hde-epic030/checks/po-002/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-002/primary.log  
* audit/qa/hde-epic030/checks/po-002/pytest\_stdout.log  
* audit/qa/hde-epic030/checks/po-002/generator\_stdout.log  
* audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json

PASS criteria tied to deliverables:

* pytest exit code is 0\.  
* generator exit code is 0\.  
* zero\_weight\_handoff.json exists and expresses zero-weight candidate exclusion.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if tests fail or zero-weight evidence contradicts exclusion behavior.  
* FAIL\_TOOLING if pytest or the generator cannot run.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test or generator loci.

#### **CHECK po-003: Viewer-preference normalization must reject invalid input while preserving deterministic, stable output for valid input.**

Goal:

Prove viewer-preference normalization rejects invalid input and produces stable output for valid input.

Required dependencies:

* Python 3  
* pytest  
* tests/unit/test\_viewer\_prefs\_normalization.py  
* tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tests/unit/test\_viewer\_prefs\_normalization.py  
* test \-f tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo or evidence generator loci.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the viewer-preference normalization tests with the exact discovered test path.  
2. Execute the PR-01 normalization evidence generator with its audit-proven script path.  
3. Confirm invalid\_viewer\_prefs.log and normalization\_canonical\_compare.log remain present.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-003

Command 2: bash \-lc 'set \+e; python \-m pytest tests/unit/test\_viewer\_prefs\_normalization.py \> audit/qa/hde-epic030/checks/po-003/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-003/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-003/pytest\_rc.txt; python tools/evidence/generate\_epic030\_pr01\_normalization\_evidence.py \> audit/qa/hde-epic030/checks/po-003/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-003/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-003/generator\_rc.txt; if \[ "$pytest\_rc" \-eq 0 \] && \[ "$generator\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-01/invalid\_viewer\_prefs.log \] && \[ \-s audit/qa/hde-epic030/pr-01/normalization\_canonical\_compare.log \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-003/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-003/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-003/primary.log. Then append audit/qa/hde-epic030/checks/po-003/pytest\_stdout.log and audit/qa/hde-epic030/checks/po-003/generator\_stdout.log to audit/qa/hde-epic030/checks/po-003/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-003/primary.log  
* audit/qa/hde-epic030/pr-01/invalid\_viewer\_prefs.log  
* audit/qa/hde-epic030/pr-01/normalization\_canonical\_compare.log

PASS criteria tied to deliverables:

* pytest exit code is 0\.  
* generator exit code is 0\.  
* invalid\_viewer\_prefs.log and normalization\_canonical\_compare.log exist and are non-empty.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if invalid input is not rejected or valid normalization is unstable.  
* FAIL\_TOOLING if pytest or the generator cannot run.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test or generator loci.

#### **CHECK po-004: The dev-only candidate-selection harness must remain non-public, environment-bounded, deterministic, and limited to safe diagnostic output.**

Goal:

Prove the dev-only candidate-selection harness remains non-public, environment-bounded, deterministic, and limited to safe diagnostic output.

Required dependencies:

* Python 3  
* pytest  
* tests/adapter/test\_dev\_sampler\_http.py  
* tests/cli/test\_dev\_sampler\_cli.py  
* tools/evidence/generate\_epic030\_pr02\_sampler\_harness\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tests/adapter/test\_dev\_sampler\_http.py  
* test \-f tests/cli/test\_dev\_sampler\_cli.py  
* test \-f tools/evidence/generate\_epic030\_pr02\_sampler\_harness\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo or evidence generator loci.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the dev sampler adapter and CLI tests with exact discovered test paths.  
2. Execute the PR-02 sampler harness evidence generator with its audit-proven script path.  
3. Confirm dev\_sampler\_two\_run\_identity.json and dev\_sampler\_http\_headers.txt remain present.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-004

Command 2: bash \-lc 'set \+e; python \-m pytest tests/adapter/test\_dev\_sampler\_http.py tests/cli/test\_dev\_sampler\_cli.py \> audit/qa/hde-epic030/checks/po-004/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-004/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-004/pytest\_rc.txt; python tools/evidence/generate\_epic030\_pr02\_sampler\_harness\_evidence.py \> audit/qa/hde-epic030/checks/po-004/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-004/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-004/generator\_rc.txt; if \[ "$pytest\_rc" \-eq 0 \] && \[ "$generator\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json \] && \[ \-s audit/qa/hde-epic030/pr-02/dev\_sampler\_http\_headers.txt \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-004/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-004/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-004/primary.log. Then append audit/qa/hde-epic030/checks/po-004/pytest\_stdout.log and audit/qa/hde-epic030/checks/po-004/generator\_stdout.log to audit/qa/hde-epic030/checks/po-004/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-004/primary.log  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_http\_headers.txt

PASS criteria tied to deliverables:

* pytest exit code is 0\.  
* generator exit code is 0\.  
* dev-only sampler evidence exists and remains bounded to the internal/dev harness.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if the harness is public, non-deterministic, or unsafe in output posture.  
* FAIL\_TOOLING if pytest or the generator cannot run.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test or generator loci.

#### **CHECK po-005: Compatibility behavior must be proven order-neutral, identity-stable, and category-order coherent for the implemented slice.**

Goal:

Prove compatibility behavior is order-neutral, identity-stable, and category-order coherent for the implemented slice.

Required dependencies:

* Python 3  
* pytest  
* tests/compat/test\_compat\_public\_ab\_ba\_identity.py  
* tools/evidence/generate\_epic030\_pr03\_compat\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tests/compat/test\_compat\_public\_ab\_ba\_identity.py  
* test \-f tools/evidence/generate\_epic030\_pr03\_compat\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo or evidence generator loci.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the compatibility AB/BA identity test with its exact discovered test path.  
2. Execute the PR-03 compatibility evidence generator with its audit-proven script path.  
3. Confirm compat\_identity\_binding.log and compat\_parity\_binding.log remain present.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-005

Command 2: bash \-lc 'set \+e; python \-m pytest tests/compat/test\_compat\_public\_ab\_ba\_identity.py \> audit/qa/hde-epic030/checks/po-005/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-005/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-005/pytest\_rc.txt; python tools/evidence/generate\_epic030\_pr03\_compat\_evidence.py \> audit/qa/hde-epic030/checks/po-005/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-005/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-005/generator\_rc.txt; if \[ "$pytest\_rc" \-eq 0 \] && \[ "$generator\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log \] && \[ \-s audit/qa/hde-epic030/pr-03/compat\_parity\_binding.log \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-005/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-005/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-005/primary.log. Then append audit/qa/hde-epic030/checks/po-005/pytest\_stdout.log and audit/qa/hde-epic030/checks/po-005/generator\_stdout.log to audit/qa/hde-epic030/checks/po-005/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-005/primary.log  
* audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log  
* audit/qa/hde-epic030/pr-03/compat\_parity\_binding.log

PASS criteria tied to deliverables:

* pytest exit code is 0\.  
* generator exit code is 0\.  
* compatibility identity and parity evidence exists.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if tests fail or required evidence is absent.  
* FAIL\_TOOLING if pytest or the generator cannot run.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test or generator loci.

#### **CHECK po-006: Public user-facing compatibility output must remain band-only and OPS-02 must prove birth-only vendor-backed no-user implementation-validation evidence.**

Goal:

Prove both po-006 proof classes now required by PF10:

* Public user-facing compatibility output remains band-only and numeric-free.  
* Completed OPS-02 evidence shows a PO-run controlled vendor-backed no-user smoke using birth data only, with no caller `user_id`, no app user ID, and no caller `person_uid`.

This check interprets completed OPS-02 implementation-validation evidence. It does not run a vendor command and does not claim QA PASS, Live QA completion, PF09 status change, or epic closure from OPS-02 alone.

Required dependencies:

* Python 3  
* pytest  
* grep  
* `tests/compat/test_compat_public_ab_ba_identity.py`  
* `tests/compat/test_compat_public_lf_bom.py`  
* `audit/qa/hde-epic030/pr-05/category_framework_binding.log`  
* `audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`  
* `audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `audit/ops/hde-epic030/ops-02/target_disposition.md`  
* `audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md`  
* `audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `audit/ops/hde-epic030/ops-02/result_summary.md`  
* `audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md`  
* `audit/ops/hde-epic030/ops-02/execution_classification.md`  
* `audit/ops/hde-epic030/ops-02/stdout.json`  
* `audit/ops/hde-epic030/ops-02/stderr.log`  
* `audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `audit/ops/hde-epic030/ops-02/stdout_parse_validation.md`  
* `audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* `audit/ops/hde-epic030/ops-02/files_sha256.txt`  
* `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`

Preflight check:

* `python -m pytest --version`  
* `test -f tests/compat/test_compat_public_ab_ba_identity.py`  
* `test -f tests/compat/test_compat_public_lf_bom.py`  
* `test -f audit/qa/hde-epic030/pr-05/category_framework_binding.log`  
* `test -f audit/ops/hde-epic030/ops-02/vendor_command.txt`  
* `test -f audit/ops/hde-epic030/ops-02/sample_birth_inputs.json`  
* `test -f audit/ops/hde-epic030/ops-02/redacted_env_presence.json`  
* `test -f audit/ops/hde-epic030/ops-02/target_disposition.md`  
* `test -f audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md`  
* `test -f audit/ops/hde-epic030/ops-02/request_summary.txt`  
* `test -f audit/ops/hde-epic030/ops-02/result_summary.md`  
* `test -f audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md`  
* `test -f audit/ops/hde-epic030/ops-02/execution_classification.md`  
* `test -f audit/ops/hde-epic030/ops-02/stdout.json`  
* `test -f audit/ops/hde-epic030/ops-02/stderr.log`  
* `test -f audit/ops/hde-epic030/ops-02/exit_code.txt`  
* `test -f audit/ops/hde-epic030/ops-02/stdout_parse_validation.md`  
* `test -f audit/ops/hde-epic030/ops-02/stdout.json.sha256`  
* `test -f audit/ops/hde-epic030/ops-02/files_sha256.txt`  
* `test -f audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`

If missing, activation/install action:

* `python -m pip install -r requirements-dev.txt` for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo evidence loci.  
* Do not re-run OPS-02 from this QA plan.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.  
* Completed OPS-02 evidence exists under `audit/ops/hde-epic030/ops-02/`.  
* The QA operator is not executing a vendor command in this check.

Setup:

* Use closed rails for this QA check.  
* Do not run `hdctl showcompat`.  
* Do not open network rails.  
* Interpret the completed OPS-02 evidence as implementation-validation evidence only.

PO actions:

1. Execute public compatibility tests with exact discovered test paths.  
2. Grep PR-05 binding log for `public_reader_bands_only_numeric_free: True`.  
3. Validate the completed OPS-02 evidence family for birth-only vendor-backed no-user posture, PASS classification, zero exit code, parseable stdout, no secret persistence, non-claim posture, and PF canon completion-matrix presence.  
4. Capture the numeric-free snapshot and OPS-02 evidence interpretation under po-006.

Command 1:

`mkdir -p audit/qa/hde-epic030/checks/po-006`

Command 2:

bash \-lc 'set \+e; python \-m pytest tests/compat/test\_compat\_public\_ab\_ba\_identity.py tests/compat/test\_compat\_public\_lf\_bom.py \> audit/qa/hde-epic030/checks/po-006/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-006/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-006/pytest\_rc.txt; grep \-n "public\_reader\_bands\_only\_numeric\_free: True" audit/qa/hde-epic030/pr-05/category\_framework\_binding.log \> audit/qa/hde-epic030/checks/po-006/numeric\_free\_grep.txt 2\> audit/qa/hde-epic030/checks/po-006/grep\_stderr.log; grep\_rc=$?; printf "%s\\n" "$grep\_rc" \> audit/qa/hde-epic030/checks/po-006/grep\_rc.txt; python \- \<\< "PY" \> audit/qa/hde-epic030/checks/po-006/ops02\_evidence\_validation.json 2\> audit/qa/hde-epic030/checks/po-006/ops02\_evidence\_validation.stderr  
 import json, pathlib, sys

root \= pathlib.Path("audit/ops/hde-epic030/ops-02")  
 required \= {  
 "vendor\_command": root / "vendor\_command.txt",  
 "sample\_birth\_inputs": root / "sample\_birth\_inputs.json",  
 "redacted\_env\_presence": root / "redacted\_env\_presence.json",  
 "target\_disposition": root / "target\_disposition.md",  
 "pr02\_runtime\_binding": root / "pr02\_runtime\_binding.md",  
 "request\_summary": root / "request\_summary.txt",  
 "result\_summary": root / "result\_summary.md",  
 "pfcanon\_ops02\_completion\_matrix": root / "pfcanon\_ops02\_completion\_matrix.md",  
 "execution\_classification": root / "execution\_classification.md",  
 "stdout": root / "stdout.json",  
 "stderr": root / "stderr.log",  
 "exit\_code": root / "exit\_code.txt",  
 "stdout\_parse\_validation": root / "stdout\_parse\_validation.md",  
 "stdout\_sha256": root / "stdout.json.sha256",  
 "files\_sha256": root / "files\_sha256.txt",  
 "final\_bundle": root / "ops02\_complete\_action\_log\_and\_evidence\_final.md",  
 }  
 missing \= \[str(p) for p in required.values() if not p.exists()\]  
 empty\_required \= \[  
 str(p)  
 for name, p in required.items()  
 if name \!= "stderr" and p.exists() and p.stat().st\_size \== 0  
 \]

def read(path):  
 return path.read\_text(encoding="utf-8") if path.exists() else ""

vendor\_command \= read(required\["vendor\_command"\]).strip()  
 sample\_text \= read(required\["sample\_birth\_inputs"\])  
 target\_text \= read(required\["target\_disposition"\])  
 pr02\_text \= read(required\["pr02\_runtime\_binding"\])  
 request\_text \= read(required\["request\_summary"\])  
 result\_text \= read(required\["result\_summary"\])  
 completion\_matrix\_text \= read(required\["pfcanon\_ops02\_completion\_matrix"\])  
 classification\_text \= read(required\["execution\_classification"\])  
 parse\_text \= read(required\["stdout\_parse\_validation"\])  
 exit\_code \= read(required\["exit\_code"\]).strip()  
 stdout\_text \= read(required\["stdout"\])  
 stderr\_text \= read(required\["stderr"\])  
 files\_sha\_text \= read(required\["files\_sha256"\])  
 final\_bundle\_text \= read(required\["final\_bundle"\])

try:  
 sample \= json.loads(sample\_text) if sample\_text else {}  
 except Exception:  
 sample \= {}

forbidden\_command\_fragments \= \["--user-a", "--user-b", "--a-user", "--b-user", "--source db", "user\_id", "person\_uid", "\<YYYY-MM-DD\>", "HH:MM", "\<LOCATION\_A\>", "\<LOCATION\_B\>"\]

checks \= {  
 "all\_required\_files\_exist": not missing,  
 "required\_files\_nonempty\_except\_stderr": not empty\_required,  
 "vendor\_command\_source\_vendor": "--source vendor" in vendor\_command,  
 "vendor\_command\_birthdate\_a": "--birthdate-a" in vendor\_command,  
 "vendor\_command\_birthtime\_a": "--birthtime-a" in vendor\_command,  
 "vendor\_command\_location\_a": "--location-a" in vendor\_command,  
 "vendor\_command\_birthdate\_b": "--birthdate-b" in vendor\_command,  
 "vendor\_command\_birthtime\_b": "--birthtime-b" in vendor\_command,  
 "vendor\_command\_location\_b": "--location-b" in vendor\_command,  
 "vendor\_command\_no\_forbidden\_identity\_or\_placeholder": not any(fragment in vendor\_command for fragment in forbidden\_command\_fragments),  
 "sample\_no\_app\_user\_ids": sample.get("constraints", {}).get("no\_app\_user\_ids") is True,  
 "sample\_no\_person\_uid": sample.get("constraints", {}).get("no\_person\_uid") is True,  
 "sample\_no\_user\_id": sample.get("constraints", {}).get("no\_user\_id") is True,  
 "sample\_vendor\_call\_executed": sample.get("constraints", {}).get("vendor\_call\_executed") is True,  
 "target\_cli\_local\_vendor\_smoke": "CLI\_LOCAL\_VENDOR\_SMOKE" in target\_text,  
 "target\_hosted\_pf07\_not\_required": "PF07 hosted-service binding required: no" in target\_text,  
 "pr02\_runtime\_binding\_present": "PR-02 remediation present in runtime: true" in pr02\_text,  
 "pr02\_birth\_only\_boundary": "birth-only boundary implemented: true" in pr02\_text,  
 "pr02\_no\_caller\_user\_id": "no caller user\_id required: true" in pr02\_text,  
 "pr02\_no\_caller\_person\_uid": "no caller person\_uid required: true" in pr02\_text,  
 "request\_command\_source\_ops01": "command\_source\_was\_ops01=true" in request\_text or "command source: OPS-01" in request\_text,  
 "request\_birth\_only": "input\_shape=birth-only" in request\_text or "input shape: birth-only" in request\_text,  
 "request\_po\_authorization": "po\_authorization\_to\_run\_controlled\_smoke=true" in request\_text or "PO authorization" in request\_text,  
 "result\_status\_pass": "status: PASS" in result\_text or "- status: PASS" in result\_text,  
 "completion\_matrix\_present": bool(completion\_matrix\_text.strip()),  
 "classification\_pass": "classification: PASS" in classification\_text or "- classification: PASS" in classification\_text,  
 "classification\_command\_ran": "command\_ran: true" in classification\_text or "- command\_ran: true" in classification\_text,  
 "classification\_vendor\_call\_executed": "vendor\_call\_executed: true" in classification\_text or "- vendor\_call\_executed: true" in classification\_text,  
 "exit\_code\_zero": exit\_code \== "0",  
 "stdout\_nonempty": bool(stdout\_text.strip()),  
 "stderr\_empty": stderr\_text \== "",  
 "parseable\_json\_true": "parseable\_json: true" in parse\_text,  
 "stdout\_nonempty\_true": "stdout\_nonempty: true" in parse\_text,  
 "secret\_values\_detected\_false": "secret\_values\_detected: false" in parse\_text,  
 "non\_claim\_not\_qa\_pass": "not QA PASS" in result\_text or "not QA PASS" in final\_bundle\_text,  
 "non\_claim\_not\_live\_qa": "not Live QA completion" in result\_text or "not Live QA completion" in final\_bundle\_text,  
 "non\_claim\_not\_pf09": "not PF09 status change" in result\_text or "not PF09 status change" in final\_bundle\_text,  
 "non\_claim\_not\_closure": "not epic closure" in result\_text or "not epic closure" in final\_bundle\_text,  
 }  
 for name, path in required.items():  
 checks\[f"files\_sha256\_contains\_{name}"\] \= str(path) in files\_sha\_text

if missing or empty\_required:  
 status \= "TOOLING\_BLOCKED"  
 else:  
 status \= "PASS" if all(checks.values()) else "FAIL\_BEHAVIOR"

out \= {  
 "schema": "hde\_epic030.po006.ops02\_evidence\_validation.v1",  
 "status": status,  
 "missing": missing,  
 "empty\_required": empty\_required,  
 "checks": checks,  
 }  
 print(json.dumps(out, sort\_keys=True, separators=(",", ":")))  
 sys.exit(0 if status \== "PASS" else (2 if status \== "TOOLING\_BLOCKED" else 1))  
 PY  
 ops02\_rc=$?; printf "%s\\n" "$ops02\_rc" \> audit/qa/hde-epic030/checks/po-006/ops02\_evidence\_validation\_rc.txt; if \[ "$pytest\_rc" \-eq 0 \] && \[ "$grep\_rc" \-eq 0 \] && \[ "$ops02\_rc" \-eq 0 \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-006/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-006/exit\_code.txt; fi'

Command 3:

Export this check’s header inputs and run the PF27 canonical inline `python - << 'PY'` header writer shown in the Step-log header schema expectations section to write `audit/qa/hde-epic030/checks/po-006/primary.log`. The primary log status must match the observed step status: PASS only when pytest rc is 0, grep rc is 0, and `ops02_evidence_validation.json` reports status PASS; TOOLING\_BLOCKED when `ops02_evidence_validation.json` reports status TOOLING\_BLOCKED; FAIL\_TOOLING when pytest, grep, or the validation script cannot run; FAIL\_BEHAVIOR otherwise. Then append `audit/qa/hde-epic030/checks/po-006/pytest_stdout.log`, `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt`, and `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json` to `audit/qa/hde-epic030/checks/po-006/primary.log`.

Required deliverables:

* `audit/qa/hde-epic030/checks/po-006/primary.log`  
* `audit/qa/hde-epic030/checks/po-006/numeric_free_grep.txt`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.json`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation.stderr`  
* `audit/qa/hde-epic030/checks/po-006/ops02_evidence_validation_rc.txt`  
* `audit/qa/hde-epic030/pr-05/category_framework_binding.log`  
* `audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md`

PASS criteria tied to deliverables:

* pytest exit code is 0\.  
* `numeric_free_grep.txt` contains `public_reader_bands_only_numeric_free: True`.  
* `ops02_evidence_validation.json` has status PASS.  
* OPS-02 command proof is birth-only and explicit vendor source.  
* OPS-02 evidence proves no caller `user_id`, no caller `person_uid`, and no app user IDs.  
* OPS-02 evidence proves target classification `CLI_LOCAL_VENDOR_SMOKE` or another allowed non-blocked target classification from the completed OPS-02 evidence.  
* OPS-02 evidence proves PR-02 runtime binding and birth-only boundary are present.  
* OPS-02 evidence proves `pfcanon_ops02_completion_matrix.md` exists and is included in `files_sha256.txt`.  
* OPS-02 evidence proves exit code 0, non-empty parseable stdout, empty or explained stderr, and no secret values detected.  
* OPS-02 evidence preserves non-claims: not QA PASS, not Live QA completion, not PF09 status change, and not epic closure.  
* No new public numeric compatibility detail is accepted.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if public user-facing compatibility output is not band-only and numeric-free.  
* FAIL\_BEHAVIOR if OPS-02 evidence exists and contradicts the birth-only no-user vendor smoke predicate after the evidence family claims PASS.  
* FAIL\_BEHAVIOR if OPS-02 evidence exists and lacks PR-02 runtime binding while claiming PASS.  
* FAIL\_BEHAVIOR if OPS-02 evidence claims QA PASS, Live QA completion, PF09 status change, or epic closure.  
* FAIL\_TOOLING if pytest, grep, or the OPS-02 evidence validation script cannot run.  
* FAIL\_TOOLING if OPS-02 evidence exposes secret values.

Blocked posture:

* TOOLING\_BLOCKED if required OPS-02 files are missing or incomplete, including `audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md`.  
* TOOLING\_BLOCKED if OPS-02 target classification is TARGET\_UNPROVEN\_TOOLING\_BLOCKED.  
* TOOLING\_BLOCKED if OPS-02 command proof remains unresolved or placeholder-bearing.  
* RERUN AUDIT REQUIRED for missing test or evidence loci that cannot be restored.

#### **CHECK po-007: Band threshold and tuning behavior must use the existing single ownership model and must not introduce a duplicate home.**

Goal:

Prove band threshold and tuning behavior uses the existing single ownership model and does not introduce a duplicate home.

Required dependencies:

* Python 3  
* engine/compat/thresholds.py  
* engine/magic10/thresholds.py  
* tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py

Preflight check:

* test \-f engine/compat/thresholds.py  
* test \-f engine/magic10/thresholds.py  
* test \-f tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py

If missing, activation/install action:

* No package install can create missing repo loci. Rerun repo audit or restore missing files.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the PR-04 band thresholds evidence generator with its audit-proven script path.  
2. Inspect the exact threshold source files named in the audit.  
3. Confirm no duplicate threshold home is introduced.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-007

Command 2: bash \-lc 'set \+e; python tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py \> audit/qa/hde-epic030/checks/po-007/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-007/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-007/generator\_rc.txt; python \- \<\< '"'"'PY'"'"'  
 from pathlib import Path  
 out \= Path("audit/qa/hde-epic030/checks/po-007/threshold\_ownership.txt")  
 sources \= \[  
 "engine/compat/thresholds.py",  
 "engine/magic10/thresholds.py",  
 \]  
 lines \= \["schema: hde\_epic030.po007.threshold\_ownership.v1"\]  
 for path in sources:  
 p \= Path(path)  
 lines.append(f"{path}:exists={p.exists()}")  
 if p.exists():  
 text \= p.read\_text(encoding="utf-8", errors="replace")  
 lines.append(f"{path}:has\_thresholds\_v1={'THRESHOLDS\_V1' in text}")  
 lines.append(f"{path}:has\_threshold\_edges={'THRESHOLD\_EDGES' in text}")  
 out.write\_text("\\n".join(lines) \+ "\\n", encoding="utf-8")  
 PY  
 if \[ "$generator\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-04/band\_edges\_binding.log \] && \[ \-s audit/qa/hde-epic030/checks/po-007/threshold\_ownership.txt \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-007/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-007/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-007/primary.log. Then append audit/qa/hde-epic030/checks/po-007/threshold\_ownership.txt and audit/qa/hde-epic030/checks/po-007/generator\_stdout.log to audit/qa/hde-epic030/checks/po-007/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-007/primary.log  
* audit/qa/hde-epic030/checks/po-007/threshold\_ownership.txt  
* audit/qa/hde-epic030/pr-04/band\_edges\_binding.log

PASS criteria tied to deliverables:

* Generator exit code is 0\.  
* threshold\_ownership.txt identifies the existing threshold source files.  
* No duplicate threshold home is introduced.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if duplicate threshold ownership is introduced or the expected binding is contradicted.  
* FAIL\_TOOLING if source files or generator cannot be inspected.

Blocked posture:

* RERUN AUDIT REQUIRED for missing repo or generator loci.

#### **CHECK po-008: Band tuning proof must show that comparisons and identity behavior are current, complete, and based on the final implemented logic.**

Goal:

Prove band tuning comparison and identity behavior are current, complete, and based on final implemented logic.

Required dependencies:

* Python 3  
* pytest  
* tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py  
* tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py  
* test \-f tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo or evidence generator loci.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the PR-04 band thresholds evidence generator with its audit-proven script path.  
2. Execute the PR-04 evidence test with its discovered test path.  
3. Confirm band\_thresholds\_diff.json and band\_thresholds\_identity.log are current.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-008

Command 2: bash \-lc 'set \+e; python tools/evidence/generate\_epic030\_pr04\_band\_thresholds\_evidence.py \> audit/qa/hde-epic030/checks/po-008/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-008/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-008/generator\_rc.txt; python \-m pytest tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py \> audit/qa/hde-epic030/checks/po-008/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-008/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-008/pytest\_rc.txt; if \[ "$generator\_rc" \-eq 0 \] && \[ "$pytest\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json \] && \[ \-s audit/qa/hde-epic030/pr-04/band\_thresholds\_identity.log \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-008/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-008/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-008/primary.log. Then append audit/qa/hde-epic030/checks/po-008/generator\_stdout.log and audit/qa/hde-epic030/checks/po-008/pytest\_stdout.log to audit/qa/hde-epic030/checks/po-008/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-008/primary.log  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_identity.log

PASS criteria tied to deliverables:

* Generator exit code is 0\.  
* pytest exit code is 0\.  
* band threshold comparison and identity artifacts exist and are non-empty.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if comparison or identity evidence is missing, stale, or contradictory.  
* FAIL\_TOOLING if pytest or generator cannot run.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test or generator loci.

#### **CHECK po-009: Category-framework behavior must prove per-channel mechanics, category comparison, and evidence binding agree before the result is accepted.**

Goal:

Prove category-framework behavior, per-channel mechanics, category comparison, and evidence binding agree before acceptance.

Required dependencies:

* Python 3  
* pytest  
* tools/evidence/generate\_epic030\_pr05\_category\_framework\_evidence.py  
* tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tools/evidence/generate\_epic030\_pr05\_category\_framework\_evidence.py  
* test \-f tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo or evidence generator loci.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute the PR-05 category-framework evidence generator with its audit-proven script path.  
2. Execute the PR-05 evidence test with its discovered test path.  
3. Confirm category\_framework\_binding.log records index and mirror binding.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-009

Command 2: bash \-lc 'set \+e; python tools/evidence/generate\_epic030\_pr05\_category\_framework\_evidence.py \> audit/qa/hde-epic030/checks/po-009/generator\_stdout.log 2\> audit/qa/hde-epic030/checks/po-009/generator\_stderr.log; generator\_rc=$?; printf "%s\\n" "$generator\_rc" \> audit/qa/hde-epic030/checks/po-009/generator\_rc.txt; python \-m pytest tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py \> audit/qa/hde-epic030/checks/po-009/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-009/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-009/pytest\_rc.txt; if \[ "$generator\_rc" \-eq 0 \] && \[ "$pytest\_rc" \-eq 0 \] && \[ \-s audit/qa/hde-epic030/pr-05/category\_framework\_binding.log \]; then printf "0\\n" \> audit/qa/hde-epic030/checks/po-009/exit\_code.txt; else printf "1\\n" \> audit/qa/hde-epic030/checks/po-009/exit\_code.txt; fi'

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-009/primary.log. Then append audit/qa/hde-epic030/checks/po-009/generator\_stdout.log and audit/qa/hde-epic030/checks/po-009/pytest\_stdout.log to audit/qa/hde-epic030/checks/po-009/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-009/primary.log  
* audit/qa/hde-epic030/pr-05/category\_framework\_binding.log

PASS criteria tied to deliverables:

* Generator exit code is 0\.  
* pytest exit code is 0\.  
* category\_framework\_binding.log records index and mirror binding.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if category mechanics, comparison, or evidence binding is missing or contradictory.  
* FAIL\_TOOLING if pytest or generator cannot run.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test or generator loci.

  #### **CHECK po-010: Any generated proof used for this epic must fail closed when the claimed predicate is missing, stale, or contradicted.**

Goal:

Prove generated proofs used for this epic fail closed when the claimed predicate is missing, stale, or contradicted.

Required dependencies:

* Python 3  
* pytest  
* tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py  
* tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py

Preflight check:

* python \-m pytest \--version  
* test \-f tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py  
* test \-f tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py

If missing, activation/install action:

* python \-m pip install \-r requirements-dev.txt for missing pytest only.  
* RERUN AUDIT REQUIRED for missing repo loci.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Execute discovered fail-closed evidence tests for PR-04 and PR-05.  
2. Record that PR-01 through PR-03 fail-closed visibility is not comprehensive proof for every generated proof family used by the epic.  
3. Classify po-010 as TOOLING\_BLOCKED when any generated-proof family used by the epic lacks fail-closed proof.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-010

Command 2: bash \-lc 'set \+e; python \-m pytest tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py \> audit/qa/hde-epic030/checks/po-010/pytest\_stdout.log 2\> audit/qa/hde-epic030/checks/po-010/pytest\_stderr.log; pytest\_rc=$?; printf "%s\\n" "$pytest\_rc" \> audit/qa/hde-epic030/checks/po-010/pytest\_rc.txt; python \- \<\< '"'"'PY'"'"'  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-010/fail\_closed\_visibility.txt")  
 lines \= \[  
 "schema: hde\_epic030.po010.fail\_closed\_visibility.v1",  
 "pr04\_fail\_closed\_test: tests/evidence/test\_epic030\_pr04\_band\_thresholds\_evidence.py",  
 "pr05\_fail\_closed\_test: tests/evidence/test\_epic030\_pr05\_category\_framework\_evidence.py",  
 "pr01\_pr03\_fail\_closed\_comprehensive\_proof: not proven in this plan",  
 "classification: TOOLING\_BLOCKED until fail-closed proof exists for every generated proof family used by the epic",  
 \]  
 out.write\_text("\\n".join(lines) \+ "\\n", encoding="utf-8")  
 PY  
 if \[ "$pytest\_rc" \-ne 0 \]; then printf "1\\n" \> audit/qa/hde-epic030/checks/po-010/exit\_code.txt; elif grep \-q "pr01\_pr03\_fail\_closed\_comprehensive\_proof: not proven" audit/qa/hde-epic030/checks/po-010/fail\_closed\_visibility.txt; then printf "2\\n" \> audit/qa/hde-epic030/checks/po-010/exit\_code.txt; else printf "0\\n" \> audit/qa/hde-epic030/checks/po-010/exit\_code.txt; fi'

Command 3: Use the PF27 canonical inline header writer from the Step-log header schema expectations section with PASS\_FAIL derived from audit/qa/hde-epic030/checks/po-010/exit\_code.txt as follows: 0 maps to PASS, 2 maps to TOOLING\_BLOCKED, and any other value maps to FAIL\_BEHAVIOR. Write the header to audit/qa/hde-epic030/checks/po-010/primary.log, then append audit/qa/hde-epic030/checks/po-010/pytest\_stdout.log and audit/qa/hde-epic030/checks/po-010/fail\_closed\_visibility.txt to audit/qa/hde-epic030/checks/po-010/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-010/primary.log  
* audit/qa/hde-epic030/checks/po-010/fail\_closed\_visibility.txt  
* audit/qa/hde-epic030/checks/po-010/pytest\_stdout.log  
* audit/qa/hde-epic030/checks/po-010/exit\_code.txt

PASS criteria tied to deliverables:

* PR-04 and PR-05 fail-closed evidence tests pass.  
* Every generated proof family used by the epic has fail-closed proof.  
* fail\_closed\_visibility.txt does not classify any generated proof family as not proven.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if a discovered fail-closed predicate test fails.  
* FAIL\_TOOLING if pytest cannot run.  
* TOOLING\_BLOCKED if any generated proof family used by the epic lacks fail-closed proof.

Blocked posture:

* RERUN AUDIT REQUIRED for missing test loci.  
* Do not mark po-010 PASS while any generated-proof family used by the epic remains not proven for fail-closed behavior.

#### **CHECK po-011: The implementation proof for each active slice must be current, mutually coherent, and traceable through the governed evidence system.**

Goal:

Prove the implementation proof for each active slice is current, coherent, and traceable through the governed evidence system.

Required dependencies:

* Python 3  
* docs/evidence/INDEX.json  
* artifacts/evidence\_index.jsonl  
* audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json  
* audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json  
* audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log  
* audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json  
* audit/qa/hde-epic030/pr-05/category\_framework\_binding.log

Preflight check:

* test \-f docs/evidence/INDEX.json  
* test \-f artifacts/evidence\_index.jsonl  
* test \-f audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json  
* test \-f audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json  
* test \-f audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log  
* test \-f audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json  
* test \-f audit/qa/hde-epic030/pr-05/category\_framework\_binding.log

If missing, activation/install action:

* No package install can create missing governed evidence loci. Rerun the relevant evidence generator or repo audit.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A discovery exists.

Setup:

* Use closed rails.

PO actions:

1. Read docs/evidence/INDEX.json and artifacts/evidence\_index.jsonl.  
2. Check all required PR-slice artifacts are present.  
3. Check all required PR-slice artifacts are indexed and mirrored.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-011

Command 2: python \- \<\< 'PY'  
 import json  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-011")  
 required \= \[  
 "audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json",  
 "audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json",  
 "audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log",  
 "audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json",  
 "audit/qa/hde-epic030/pr-05/category\_framework\_binding.log",  
 \]  
 summary \= {  
 "schema": "hde\_epic030.po011.traceability\_summary.v1",  
 "present": {path: Path(path).exists() for path in required},  
 "indexed": {},  
 "mirrored": {},  
 }  
 index\_text \= Path("docs/evidence/INDEX.json").read\_text(encoding="utf-8") if Path("docs/evidence/INDEX.json").exists() else ""  
 mirror\_text \= Path("artifacts/evidence\_index.jsonl").read\_text(encoding="utf-8") if Path("artifacts/evidence\_index.jsonl").exists() else ""  
 for path in required:  
 summary\["indexed"\]\[path\] \= path in index\_text  
 summary\["mirrored"\]\[path\] \= path in mirror\_text  
 summary\["all\_present"\] \= all(summary\["present"\].values())  
 summary\["all\_indexed"\] \= all(summary\["indexed"\].values())  
 summary\["all\_mirrored"\] \= all(summary\["mirrored"\].values())  
 (out / "traceability\_summary.json").write\_text(json.dumps(summary, sort\_keys=True, separators=(",", ":")) \+ "\\n", encoding="utf-8")  
 (out / "exit\_code.txt").write\_text(("0" if summary\["all\_present"\] and summary\["all\_indexed"\] and summary\["all\_mirrored"\] else "1") \+ "\\n", encoding="utf-8")  
 PY

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-011/primary.log. Then append audit/qa/hde-epic030/checks/po-011/traceability\_summary.json to audit/qa/hde-epic030/checks/po-011/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-011/primary.log  
* audit/qa/hde-epic030/checks/po-011/traceability\_summary.json

PASS criteria tied to deliverables:

* traceability\_summary.json records all required artifacts present, indexed, and mirrored.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if any required artifact, index binding, or mirror binding is missing.  
* FAIL\_TOOLING if ledgers cannot be read.

Blocked posture:

* RERUN AUDIT REQUIRED for missing governed evidence loci.

#### **CHECK po-012: Previously complete foundation work must be treated as reused history, not as newly implemented HDE-EPIC030 work.**

Goal:

Prove QA interpretation does not reopen already-complete foundation rows as new HDE-EPIC030 work.

Required dependencies:

* Python 3

Preflight check:

* python \--version

If missing, activation/install action:

* Restore Python 3 availability in the execution venue.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0B doc delta capture exists.

Setup:

* Use closed rails.

PO actions:

1. Create a mechanical interpretation note that lists reused-history rows.  
2. Confirm the note does not claim new HDE-EPIC030 implementation for HDE-DISS005.1, HDE-DISS006.1, or HDE-DISS006.2.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-012

Command 2: python \- \<\< 'PY'  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-012/reused\_history\_classification.txt")  
 lines \= \[  
 "schema: hde\_epic030.po012.reused\_history\_classification.v1",  
 "reused\_history: HDE-DISS005.1",  
 "reused\_history: HDE-DISS006.1",  
 "reused\_history: HDE-DISS006.2",  
 "active\_hde\_epic030\_scope: HDE-DISS005.2",  
 "active\_hde\_epic030\_scope: HDE-DISS005.3",  
 "active\_hde\_epic030\_scope: HDE-DISS005.4",  
 "active\_hde\_epic030\_scope: HDE-DISS006.3",  
 "active\_hde\_epic030\_scope: HDE-DISS006.4",  
 "active\_hde\_epic030\_scope: HDE-DISS006.5",  
 "new\_implementation\_claim\_for\_reused\_history: False",  
 \]  
 out.write\_text("\\n".join(lines) \+ "\\n", encoding="utf-8")  
 PY

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-012/primary.log. Then append audit/qa/hde-epic030/checks/po-012/reused\_history\_classification.txt to audit/qa/hde-epic030/checks/po-012/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-012/primary.log  
* audit/qa/hde-epic030/checks/po-012/reused\_history\_classification.txt

PASS criteria tied to deliverables:

* Reused history and active rows are clearly separated.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if reused-history rows are claimed as newly implemented HDE-EPIC030 work.

Blocked posture:

* None if Python 3 is available.

#### **CHECK po-013: QA interpretation must distinguish implemented completion support from permanent checklist drainage.**

Goal:

Prove the QA interpretation separates repo-supported completion from PF09.2 drainage.

Required dependencies:

* Python 3  
* audit/qa/hde-epic030/00\_meta/doc\_deltas.md

Preflight check:

* test \-f audit/qa/hde-epic030/00\_meta/doc\_deltas.md

If missing, activation/install action:

* Re-run Step-0B.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0B exists.

Setup:

* Use closed rails.

PO actions:

1. Create a source-of-truth posture file.  
2. Confirm it says repo-supported completion, canon-drain completion, and formal close-pack completion are separate states.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-013

Command 2: python \- \<\< 'PY'  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-013/source\_of\_truth\_posture.txt")  
 lines \= \[  
 "schema: hde\_epic030.po013.source\_of\_truth\_posture.v1",  
 "repo\_supported\_completion: evaluated by implementation proof and Live QA logs",  
 "canon\_drain\_completion: no-claim until drained",  
 "formal\_close\_pack\_completion: no-claim until close-pack artifacts exist",  
 "drainage\_required\_before\_QA\_PASS: False",  
 \]  
 out.write\_text("\\n".join(lines) \+ "\\n", encoding="utf-8")  
 PY

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-013/primary.log. Then append audit/qa/hde-epic030/checks/po-013/source\_of\_truth\_posture.txt to audit/qa/hde-epic030/checks/po-013/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-013/primary.log  
* audit/qa/hde-epic030/checks/po-013/source\_of\_truth\_posture.txt

PASS criteria tied to deliverables:

* Three states are separate and truthful.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if drainage is treated as a required execution gate.

Blocked posture:

* None if Step-0B exists.

#### **CHECK po-014: The full post-implementation state must be proven coherent after all implementation slices and documentation-facing updates are considered together.**

Goal:

Prove all implementation slices and documentation-facing updates are considered together before closeout interpretation.

Required dependencies:

* Python 3  
* po-001 through po-013 primary logs where available

Preflight check:

* test \-d audit/qa/hde-epic030/checks

If missing, activation/install action:

* Execute the planned checks that create audit/qa/hde-epic030/checks.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* po-001 through po-013 should be run first.

Setup:

* Use closed rails.

PO actions:

1. Generate all-slice coherence summary.  
2. Record which earlier checks are present.  
3. Classify missing prior check logs as TOOLING\_BLOCKED.  
4. Classify missing or contradictory required PR artifacts as FAIL\_BEHAVIOR.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-014

Command 2: python \- \<\< 'PY'  
 import json  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-014")  
 prior\_logs \= \[Path(f"audit/qa/hde-epic030/checks/po-{i:03d}/primary.log") for i in range(1, 14)\]  
 pr\_artifacts \= \[  
 Path("audit/qa/hde-epic030/pr-01/zero\_weight\_handoff.json"),  
 Path("audit/qa/hde-epic030/pr-01/invalid\_viewer\_prefs.log"),  
 Path("audit/qa/hde-epic030/pr-01/normalization\_canonical\_compare.log"),  
 Path("audit/qa/hde-epic030/pr-02/dev\_sampler\_two\_run\_identity.json"),  
 Path("audit/qa/hde-epic030/pr-03/compat\_identity\_binding.log"),  
 Path("audit/qa/hde-epic030/pr-04/band\_thresholds\_diff.json"),  
 Path("audit/qa/hde-epic030/pr-05/category\_framework\_binding.log"),  
 \]  
 summary \= {  
 "schema": "hde\_epic030.po014.all\_slice\_coherence.v1",  
 "prior\_logs": {str(p): p.exists() for p in prior\_logs},  
 "pr\_artifacts": {str(p): p.exists() for p in pr\_artifacts},  
 }  
 summary\["all\_prior\_logs\_present"\] \= all(summary\["prior\_logs"\].values())  
 summary\["all\_pr\_artifacts\_present"\] \= all(summary\["pr\_artifacts"\].values())  
 if not summary\["all\_prior\_logs\_present"\]:  
 exit\_code \= 2  
 summary\["status"\] \= "TOOLING\_BLOCKED"  
 elif not summary\["all\_pr\_artifacts\_present"\]:  
 exit\_code \= 1  
 summary\["status"\] \= "FAIL\_BEHAVIOR"  
 else:  
 exit\_code \= 0  
 summary\["status"\] \= "PASS"  
 (out / "all\_slice\_coherence.json").write\_text(json.dumps(summary, sort\_keys=True, separators=(",", ":")) \+ "\\n", encoding="utf-8")  
 (out / "exit\_code.txt").write\_text(str(exit\_code) \+ "\\n", encoding="utf-8")  
 PY

Command 3: Use the PF27 canonical inline header writer from the Step-log header schema expectations section with PASS\_FAIL derived from audit/qa/hde-epic030/checks/po-014/exit\_code.txt as follows: 0 maps to PASS, 2 maps to TOOLING\_BLOCKED, and any other value maps to FAIL\_BEHAVIOR. Write the header to audit/qa/hde-epic030/checks/po-014/primary.log, then append audit/qa/hde-epic030/checks/po-014/all\_slice\_coherence.json.

Required deliverables:

* audit/qa/hde-epic030/checks/po-014/primary.log  
* audit/qa/hde-epic030/checks/po-014/all\_slice\_coherence.json  
* audit/qa/hde-epic030/checks/po-014/exit\_code.txt

PASS criteria tied to deliverables:

* All PR01 through PR05 core artifacts exist.  
* All prior po-001 through po-013 primary logs exist.  
* primary.log records PASS.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if any required PR artifact is missing or contradictory.  
* TOOLING\_BLOCKED if prior check logs are absent because earlier steps were not run.

Blocked posture:

* Do not close the epic if po-014 records missing required prior logs.

#### **CHECK po-015: Before behavior-level Live QA begins, the QA plan must establish the baseline execution context, reachable surfaces, and tool-health posture.**

Goal:

This guide-defined check is satisfied by Step-0A discovery. Re-validate that the discovery deliverable exists and is usable.

Required dependencies:

* Python 3  
* audit/qa/hde-epic030/checks/po-015/discovery.json

Preflight check:

* test \-f audit/qa/hde-epic030/checks/po-015/discovery.json

If missing, activation/install action:

* Re-run Step-0A.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0A should already have produced the primary log and discovery file.

Setup:

* Use closed rails.

PO actions:

1. Validate discovery JSON parses.  
2. Confirm it includes rails and path inventory.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-015

Command 2: python \- \<\< 'PY'  
 import json  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-015")  
 discovery \= out / "discovery.json"  
 result \= {  
 "schema": "hde\_epic030.po015.discovery\_validation.v1",  
 "discovery\_path": str(discovery),  
 "discovery\_exists": discovery.exists(),  
 "discovery\_valid": False,  
 "has\_rails": False,  
 "has\_paths": False,  
 "has\_surfaces": False,  
 }  
 try:  
 data \= json.loads(discovery.read\_text(encoding="utf-8"))  
 result\["discovery\_valid"\] \= True  
 result\["has\_rails"\] \= isinstance(data.get("rails"), dict)  
 result\["has\_paths"\] \= isinstance(data.get("paths"), dict)  
 result\["has\_surfaces"\] \= isinstance(data.get("surfaces"), list)  
 except Exception as exc:  
 result\["parse\_error"\] \= f"{exc.**class**.**name**}: {exc}"  
 status \= "PASS" if result\["discovery\_exists"\] and result\["discovery\_valid"\] and result\["has\_rails"\] and result\["has\_paths"\] and result\["has\_surfaces"\] else "TOOLING\_BLOCKED"  
 (out / "discovery\_validation.txt").write\_text(json.dumps(result, sort\_keys=True, separators=(",", ":")) \+ "\\n", encoding="utf-8")  
 (out / "exit\_code.txt").write\_text(("0" if status \== "PASS" else "2") \+ "\\n", encoding="utf-8")  
 PY

Command 3: Use the PF27 canonical inline header writer from the Step-log header schema expectations section with PASS\_FAIL=PASS only if audit/qa/hde-epic030/checks/po-015/discovery\_validation.txt records discovery\_valid, has\_rails, has\_paths, and has\_surfaces as true. Otherwise use TOOLING\_BLOCKED. Write the header to audit/qa/hde-epic030/checks/po-015/primary.log, then append audit/qa/hde-epic030/checks/po-015/discovery\_validation.txt.

Required deliverables:

* audit/qa/hde-epic030/checks/po-015/primary.log  
* audit/qa/hde-epic030/checks/po-015/discovery.json  
* audit/qa/hde-epic030/checks/po-015/discovery\_validation.txt

PASS criteria tied to deliverables:

* discovery file is present, parseable, and includes rails, paths, and surfaces.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if discovery cannot be produced or parsed.

Blocked posture:

* Do not run behavior-level closeout interpretation until discovery exists.

#### **CHECK po-016: The final QA interpretation must explain what was run, what the outcomes mean, what evidence supports them, and whether canon follow-up is required.**

Goal:

Produce the QA RCA & Doc Delta summary required for close-stage interpretation.

Required dependencies:

* Python 3  
* primary logs for po-001 through po-017 as available

Preflight check:

* test \-d audit/qa/hde-epic030/checks

If missing, activation/install action:

* Execute the planned checks that create audit/qa/hde-epic030/checks.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* All behavior and evidence checks should be run before finalizing po-016.

Setup:

* Use closed rails.

PO actions:

1. Generate audit/EPIC-030\_QA\_RCA.md.  
2. Include coverage vs plan accounting in guide order.  
3. Include findings classification derived from primary.log headers.  
4. Include outcome meaning, evidence support, canon follow-up posture, and closeout-readiness recommendation.  
5. State closeout-readiness recommendation separate from final close-report SATISFIED or NOT SATISFIED decision.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-016 audit

Command 2: python \- \<\< 'PY'  
 import json  
 from pathlib import Path

ids \= \[f"po-{i:03d}" for i in range(1, 18)\]  
 statuses \= {}  
 artifacts \= {}  
 parse\_notes \= {}

for cid in ids:  
 p \= Path(f"audit/qa/hde-epic030/checks/{cid}/primary.log")  
 if not p.exists():  
 statuses\[cid\] \= "NOT\_EVIDENCED"  
 artifacts\[cid\] \= \[\]  
 parse\_notes\[cid\] \= "primary log missing"  
 continue  
 try:  
 first \= p.read\_text(encoding="utf-8").splitlines()\[0\]  
 header \= json.loads(first)  
 statuses\[cid\] \= str(header.get("status", "UNKNOWN"))  
 artifacts\[cid\] \= header.get("evidence\_artifacts", \[\])  
 parse\_notes\[cid\] \= ""  
 except Exception as exc:  
 statuses\[cid\] \= "FAIL\_TOOLING"  
 artifacts\[cid\] \= \[str(p)\]  
 parse\_notes\[cid\] \= f"header parse failed: {exc.**class**.**name**}"

fully \= \[cid for cid, status in statuses.items() if status \== "PASS"\]  
 blocked \= \[cid for cid, status in statuses.items() if status in {"FAIL\_TOOLING", "TOOLING\_BLOCKED", "NOT\_EVIDENCED"}\]  
 behavior \= \[cid for cid, status in statuses.items() if status \== "FAIL\_BEHAVIOR"\]

lines \= \[  
 "\# HDE-EPIC030 QA RCA & Doc Delta Summary",  
 "",  
 "Source-of-truth posture: repo-supported completion is evaluated by Live QA logs; canon-drain completion is no-claim until drained; formal close-pack completion is no-claim until close-pack artifacts exist.",  
 "",  
 "\#\# Coverage vs QA Plan",  
 \]  
 for cid in ids:  
 status \= statuses\[cid\]  
 coverage \= "Fully evidenced" if status \== "PASS" else ("Partially evidenced" if status in {"FAIL\_BEHAVIOR", "FAIL\_TOOLING", "TOOLING\_BLOCKED"} else "Not evidenced")  
 lines.append(f"- {cid}: {coverage}; status={status}; artifacts={artifacts\[cid\]}; note={parse\_notes\[cid\]}")  
 lines \+= \[  
 "",  
 "\#\# Findings classification",  
 f"PASS checks: {', '.join(fully) if fully else 'none'}",  
 f"FAIL\_BEHAVIOR checks: {', '.join(behavior) if behavior else 'none'}",  
 f"FAIL\_TOOLING, TOOLING\_BLOCKED, or not-evidenced checks: {', '.join(blocked) if blocked else 'none'}",  
 "",  
 "\#\# Outcome meaning",  
 "PASS means the check's governed evidence satisfied the plan predicate. FAIL\\\_BEHAVIOR means observed evidence contradicts the approved predicate. FAIL\\\_TOOLING or TOOLING\\\_BLOCKED means the run did not establish behavior truth for that check.",  

 "For po-006, OPS-02 PASS is implementation-validation evidence for the vendor-backed birth-only no-user smoke. It is not QA PASS by itself, not Live QA completion, not PF09 status change, and not epic closure.", 

 "\#\# Evidence support",  
 "Evidence support is the per-check primary.log header and the artifacts listed in each parsed header. Missing or unparseable headers are classified above and are not hidden.",  
 "",  
 "\#\# Canon follow-up",  
 "PF09.2 history-lock narrowing remains a doc-delta candidate unless already drained. Documentation drainage is not an execution blocker by itself.",  
 "",  
 "\#\# Closeout-readiness recommendation",  
 "NOT FINAL until all required primary logs, discovery artifact, QA RCA, step-log manifest, acceptance map, token matrix, viability log, close report, close manifest, and required path proofs exist and are reviewed.",  
 "",  
 \]  
 Path("audit/EPIC-030\_QA\_RCA.md").write\_text("\\n".join(lines), encoding="utf-8")  
 PY

Command 3: Use the PF27 canonical inline header writer from the Step-log header schema expectations section with PASS\_FAIL=PASS only if audit/EPIC-030\_QA\_RCA.md exists, contains Findings classification, Outcome meaning, Evidence support, Canon follow-up, and Closeout-readiness recommendation, and does not contain fill from primary logs after execution. Otherwise use FAIL\_BEHAVIOR or FAIL\_TOOLING according to the failed predicate. Write the header to audit/qa/hde-epic030/checks/po-016/primary.log, then append audit/EPIC-030\_QA\_RCA.md.

Required deliverables:

* audit/qa/hde-epic030/checks/po-016/primary.log  
* audit/EPIC-030\_QA\_RCA.md

PASS criteria tied to deliverables:

* QA RCA exists and includes coverage vs QA Plan accounting.  
* QA RCA includes completed Findings classification.  
* QA RCA includes outcome meaning and evidence support.  
* QA RCA includes canon follow-up posture.  
* QA RCA includes closeout-readiness recommendation.  
* The summary distinguishes repo-supported completion, canon-drain completion, and formal close-pack completion.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if QA RCA overclaims closeout, hides blocked steps, or contains an unresolved placeholder.  
* FAIL\_TOOLING if QA RCA cannot be written.

Blocked posture:

* Do not treat the epic as fully accepted if audit/EPIC-030\_QA\_RCA.md is missing.

#### **CHECK po-017: Undrained documentation deltas must not be treated as QA blockers when implementation truth and governed proof are otherwise complete.**

Goal:

Prove final QA interpretation treats undrained documentation deltas as follow-up items, not blockers by themselves.

Required dependencies:

* Python 3  
* audit/docdeltas/hde-epic030\_doc\_deltas.md  
* audit/qa/hde-epic030/00\_meta/doc\_deltas.md

Preflight check:

* test \-f audit/docdeltas/hde-epic030\_doc\_deltas.md  
* test \-f audit/qa/hde-epic030/00\_meta/doc\_deltas.md

If missing, activation/install action:

* Re-run Step-0B.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* po-013 and po-016 should be run first.

Setup:

* Use closed rails.

PO actions:

1. Generate final drainage posture note.  
2. Confirm no step is marked failed solely because PF09.2 is not yet drained.

Command 1: mkdir \-p audit/qa/hde-epic030/checks/po-017

Command 2: python \- \<\< 'PY'  
 from pathlib import Path

out \= Path("audit/qa/hde-epic030/checks/po-017/documentation\_drainage\_posture.txt")  
 lines \= \[  
 "schema: hde\_epic030.po017.documentation\_drainage\_posture.v1",  
 "drainage\_blocker: False",  
 "real\_truth\_and\_proof\_blockers: incomplete\_required\_QA\_steps",  
 "real\_truth\_and\_proof\_blockers: missing\_required\_deliverables",  
 "real\_truth\_and\_proof\_blockers: untrusted\_or\_non\_governed\_evidence",  
 "real\_truth\_and\_proof\_blockers: unresolved\_FAIL\_BEHAVIOR\_FAIL\_TOOLING\_or\_TOOLING\_BLOCKED\_conditions\_that\_affect\_acceptance",  
 "real\_truth\_and\_proof\_blockers: missing\_required\_close\_gate\_QA\_artifacts",  
 "pf09\_2\_drainage\_required\_before\_otherwise\_proven\_QA\_pass: False",  
 \]  
 out.write\_text("\\n".join(lines) \+ "\\n", encoding="utf-8")  
 PY

Command 3: Export this check’s header inputs and run the PF27 canonical inline python \- \<\< 'PY' header writer shown in the Step-log header schema expectations section to write audit/qa/hde-epic030/checks/po-017/primary.log. Then append audit/qa/hde-epic030/checks/po-017/documentation\_drainage\_posture.txt to audit/qa/hde-epic030/checks/po-017/primary.log.

Required deliverables:

* audit/qa/hde-epic030/checks/po-017/primary.log  
* audit/qa/hde-epic030/checks/po-017/documentation\_drainage\_posture.txt

PASS criteria tied to deliverables:

* Documentation drainage is correctly treated as non-blocking by itself.  
* Real blockers remain explicit.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if the final interpretation says PF10 or PF09.2 drainage is required before otherwise-proven QA can pass.

Blocked posture:

* None if Step-0B and po-013 exist.

  ### **Close-out deliverables**

This runbook MUST ensure the epic produces the execution deliverables required by the Epic Process Guide:

* Discovery artifact: audit/qa/hde-epic030/checks/po-015/discovery.json  
* QA RCA & Doc Delta summary: audit/EPIC-030\_QA\_RCA.md  
* Per-check primary logs: audit/qa/hde-epic030/checks/po-001/primary.log through audit/qa/hde-epic030/checks/po-017/primary.log  
* Doc-delta surfaces: audit/docdeltas/hde-epic030\_doc\_deltas.md and audit/qa/hde-epic030/00\_meta/doc\_deltas.md  
* Drain-targets ledger: audit/docdeltas/hde-epic030\_drain\_targets.md  
* QA step logs manifest: audit/qa/hde-epic030/qa\_step\_logs\_manifest.json  
* QA step logs manifest path proof: audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.path\_proof.txt  
* Acceptance map: docs/acceptance\_map\_epic030.json  
* Token-evidence matrix: audit/qa/hde-epic030/token\_evidence\_matrix.md  
* Acceptance map viability log: audit/qa/hde-epic030/acceptance\_map\_viability.log  
* Close report: audit/EPIC-030\_close\_report.md  
* Close report path proof: audit/EPIC-030\_close\_report.md.path\_proof.txt  
* Close manifest: audit/EPIC-030\_MANIFEST.json  
* Close manifest path proof: audit/EPIC-030\_MANIFEST.json.path\_proof.txt

Closeout artifact posture before execution:

* audit/qa/hde-epic030/checks/po-015/discovery.json: NOT RUN until Step-0A runs.  
* audit/EPIC-030\_QA\_RCA.md: NOT RUN until po-016 runs.  
* audit/docdeltas/hde-epic030\_drain\_targets.md: NOT RUN until closeout packaging runs.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json: NOT RUN until closeout packaging runs.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.path\_proof.txt: NOT RUN until closeout packaging runs.  
* docs/acceptance\_map\_epic030.json: NOT RUN until closeout packaging runs.  
* audit/EPIC-030\_close\_report.md: NOT RUN until closeout packaging runs.  
* audit/EPIC-030\_MANIFEST.json: NOT RUN until closeout packaging runs.

Minimum closeout packaging command after all checks are complete:

Command 1: python \- \<\< 'PY'  
 import datetime  
 import hashlib  
 import json  
 import pathlib

root \= pathlib.Path("audit/qa/hde-epic030")  
 checks\_root \= root / "checks"  
 manifest\_path \= root / "qa\_step\_logs\_manifest.json"  
 proof\_path \= pathlib.Path(str(manifest\_path) \+ ".path\_proof.txt")  
 entries \= {}

for primary in sorted(checks\_root.glob("po-\*/primary.log")):  
 check\_id \= primary.parent.name  
 status \= "UNKNOWN"  
 try:  
 first\_line \= primary.read\_text(encoding="utf-8").splitlines()\[0\]  
 header \= json.loads(first\_line)  
 status \= str(header.get("status", "UNKNOWN"))  
 except Exception:  
 status \= "FAIL\_TOOLING"  
 rel\_log\_path \= primary.relative\_to(root).as\_posix()  
 entries\[check\_id\] \= {  
 "check\_id": check\_id,  
 "log\_path": rel\_log\_path,  
 "status": status  
 }

data \= {  
 check\_id: entries\[check\_id\]  
 for check\_id in sorted(entries)  
 }  
 manifest\_path.write\_text(json.dumps(data, sort\_keys=True, separators=(",", ":")) \+ "\\n", encoding="utf-8")

now \= datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"  
 proof\_path.write\_text(  
 "path: " \+ str(manifest\_path) \+ "\\n"  
 \+ "size\_bytes: " \+ str(manifest\_path.stat().st\_size) \+ "\\n"  
 \+ "sha256: " \+ hashlib.sha256(manifest\_path.read\_bytes()).hexdigest() \+ "\\n"  
 \+ "mtime\_utc: " \+ datetime.datetime.utcfromtimestamp(manifest\_path.stat().st\_mtime).replace(microsecond=0).isoformat() \+ "Z\\n"  
 \+ "produced\_at\_utc: " \+ now \+ "\\n",  
 encoding="utf-8",  
 )  
 PY

Command 2: python \- \<\< 'PY'  
 import json  
 import pathlib

data \= {  
 "checks": \[f"po-{i:03d}" for i in range(1, 18)\],  
 "epic\_id": "HDE-EPIC030",  
 "schema": "hde\_epic030.acceptance\_map.v1",  
 "status": "NOT\_FINAL",  
 "tokens": \[\],  
 }  
 pathlib.Path("docs/acceptance\_map\_epic030.json").write\_text(  
 json.dumps(data, sort\_keys=True, separators=(",", ":")) \+ "\\n",  
 encoding="utf-8",  
 )  
 PY

Command 3: python \- \<\< 'PY'  
 from pathlib import Path

Path("audit/qa/hde-epic030/token\_evidence\_matrix.md").write\_text(  
 "\# HDE-EPIC030 Token Evidence Matrix\\n\\nNo new tokens minted. Token claims remain empty unless directly verified by PASS-grade step evidence.\\n",  
 encoding="utf-8",  
 )  
 Path("audit/qa/hde-epic030/acceptance\_map\_viability.log").write\_text(  
 "schema: hde\_epic030.acceptance\_map\_viability.v1\\nstatus: NOT\_FINAL\\nreason: finalize after all primary logs and close-pack artifacts are reviewed.\\n",  
 encoding="utf-8",  
 )  
 Path("audit/docdeltas/hde-epic030\_drain\_targets.md").write\_text(  
 "\# HDE-EPIC030 Drain Targets\\n\\nStatus: no drain targets asserted by closeout packaging unless QA RCA or doc-delta capture records a concrete PF-canon follow-up.\\n",  
 encoding="utf-8",  
 )  
 PY

Command 4: python \- \<\< 'PY'  
 import json  
 import pathlib

key\_outputs \= {  
 "acceptance\_map": "docs/acceptance\_map\_epic030.json",  
 "acceptance\_map\_viability": "audit/qa/hde-epic030/acceptance\_map\_viability.log",  
 "close\_manifest": "audit/EPIC-030\_MANIFEST.json",  
 "close\_manifest\_path\_proof": "audit/EPIC-030\_MANIFEST.json.path\_proof.txt",  
 "close\_report": "audit/EPIC-030\_close\_report.md",  
 "close\_report\_path\_proof": "audit/EPIC-030\_close\_report.md.path\_proof.txt",  
 "doc\_deltas": "audit/docdeltas/hde-epic030\_doc\_deltas.md",  
 "drain\_targets": "audit/docdeltas/hde-epic030\_drain\_targets.md",  
 "qa\_rca": "audit/EPIC-030\_QA\_RCA.md",  
 "qa\_step\_manifest": "audit/qa/hde-epic030/qa\_step\_logs\_manifest.json",  
 "qa\_step\_manifest\_path\_proof": "audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.path\_proof.txt",  
 "token\_matrix": "audit/qa/hde-epic030/token\_evidence\_matrix.md"  
 }

close\_report \= "\\n".join(\[  
 "\# HDE-EPIC030 Close Report",  
 "",  
 "Status: NOT FINAL until PO review.",  
 "",  
 "\#\# QA Rails — Open/Close (Final PR)",  
 "",  
 "\* SAFE\_MODE and ALLOW\_NETWORK posture is recorded in per-check primary logs.",  

 "\* po-006 consumes completed OPS-02 implementation-validation evidence; it does not run a new vendor command during Live QA.",  

 "\* OPS-02 PASS, when present, supports vendor-backed birth-only no-user implementation-validation evidence only. It is not QA PASS by itself, not Live QA completion, not PF09 status change, and not epic closure.",  

 "\* Closeout packaging does not claim PF10 drainage, merge provenance, or formal SATISFIED status.",    
 "",  
 "\#\# Acceptance and evidence pointers",  
 "",  
 "\* docs/acceptance\_map\_epic030.json",  
 "\* audit/qa/hde-epic030/token\_evidence\_matrix.md",  
 "\* audit/qa/hde-epic030/acceptance\_map\_viability.log",  
 "\* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json",  
 "\* audit/docdeltas/hde-epic030\_doc\_deltas.md",  
 "\* audit/docdeltas/hde-epic030\_drain\_targets.md",  
 "\* audit/EPIC-030\_QA\_RCA.md",  
 "",  
 "\#\# Key outputs",  
 "",  
 "Key outputs are bound in audit/EPIC-030\_MANIFEST.json.",  
 "",  
 "QA RCA: audit/EPIC-030\_QA\_RCA.md",  
 "",  
 \])  
 pathlib.Path("audit/EPIC-030\_close\_report.md").write\_text(close\_report, encoding="utf-8")  
 pathlib.Path("audit/EPIC-030\_MANIFEST.json").write\_text(  
 json.dumps(  
 {"schema": "hde\_epic030.close\_manifest.v1", "epic\_id": "HDE-EPIC030", "key\_outputs": key\_outputs},  
 sort\_keys=True,  
 separators=(",", ":"),  
 ) \+ "\\n",  
 encoding="utf-8",  
 )  
 PY

Command 5: python \- \<\< 'PY'  
 import datetime  
 import hashlib  
 import pathlib

now \= datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"  
 targets \= \[  
 "audit/EPIC-030\_close\_report.md",  
 "audit/EPIC-030\_MANIFEST.json",  
 \]  
 for p in targets:  
 path \= pathlib.Path(p)  
 proof \= pathlib.Path(p \+ ".path\_proof.txt")  
 proof.write\_text(  
 "path: " \+ p \+ "\\n"  
 \+ "size\_bytes: " \+ str(path.stat().st\_size) \+ "\\n"  
 \+ "sha256: " \+ hashlib.sha256(path.read\_bytes()).hexdigest() \+ "\\n"  
 \+ "mtime\_utc: " \+ datetime.datetime.utcfromtimestamp(path.stat().st\_mtime).replace(microsecond=0).isoformat() \+ "Z\\n"  
 \+ "produced\_at\_utc: " \+ now \+ "\\n",  
 encoding="utf-8",  
 )  
 PY

Command 6: python \- \<\< 'PY'  
 from pathlib import Path  
 import json

required \= \[  
 "audit/qa/hde-epic030/qa\_step\_logs\_manifest.json",  
 "audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.path\_proof.txt",  
 "docs/acceptance\_map\_epic030.json",  
 "audit/docdeltas/hde-epic030\_drain\_targets.md",  
 "audit/EPIC-030\_close\_report.md",  
 "audit/EPIC-030\_close\_report.md.path\_proof.txt",  
 "audit/EPIC-030\_MANIFEST.json",  
 "audit/EPIC-030\_MANIFEST.json.path\_proof.txt",  
 \]  
 missing \= \[p for p in required if not Path(p).exists()\]

manifest\_errors \= \[\]

manifest\_path \= Path("audit/qa/hde-epic030/qa\_step\_logs\_manifest.json")

root \= Path("audit/qa/hde-epic030")

root\_resolved \= root.resolve()

if manifest\_path.exists():

manifest \= json.loads(manifest\_path.read\_text(encoding="utf-8"))

if not isinstance(manifest, dict):

manifest\_errors.append("manifest is not an object keyed by check\_id")

else:

for key, item in manifest.items():

if not isinstance(item, dict):

manifest\_errors.append("manifest entry is not an object")

break

if key \!= item.get("check\_id"):

manifest\_errors.append("manifest key does not match entry check\_id")

break

log\_path \= item.get("log\_path")

if not item.get("status") or not isinstance(log\_path, str) or not log\_path:

manifest\_errors.append("manifest entry missing status or log\_path")

break

log\_path\_obj \= Path(log\_path)

if log\_path\_obj.is\_absolute():

manifest\_errors.append("manifest log\_path is absolute")

break

if any(part \== ".." for part in log\_path\_obj.parts):

manifest\_errors.append("manifest log\_path contains traversal")

break

candidate \= (root / log\_path\_obj).resolve()

try:

candidate.relative\_to(root\_resolved)

except ValueError:

manifest\_errors.append("manifest log\_path escapes epic QA root")

break

expected \= (root / "checks" / key / "primary.log").resolve()

if candidate \!= expected:

manifest\_errors.append("manifest log\_path does not resolve to matching primary.log")

break

if not candidate.exists():

manifest\_errors.append("manifest log\_path target does not exist")

break

acceptance\_map\_errors \= \[\]  
 acceptance\_map\_path \= Path("docs/acceptance\_map\_epic030.json")  
 if acceptance\_map\_path.exists():  
 acceptance\_map \= json.loads(acceptance\_map\_path.read\_text(encoding="utf-8"))  
 tokens \= acceptance\_map.get("tokens")  
 if not isinstance(tokens, list):  
 acceptance\_map\_errors.append("acceptance map tokens is not a list")  
 else:  
 for token in tokens:  
 if not isinstance(token, dict):  
 acceptance\_map\_errors.append("acceptance map token entry is not an object")  
 break  
 if not isinstance(token.get("name"), str) or not token.get("name").strip():  
 acceptance\_map\_errors.append("acceptance map token entry missing non-empty name")  
 break

drain\_errors \= \[\]  
 drain\_path \= Path("audit/docdeltas/hde-epic030\_drain\_targets.md")  
 if drain\_path.exists():  
 drain\_text \= drain\_path.read\_text(encoding="utf-8")  
 if "no drain targets asserted" not in drain\_text and "drain target" not in drain\_text.lower():  
 drain\_errors.append("drain-targets ledger does not indicate empty/no drain targets or concrete drain targets")

report \= Path("audit/EPIC-030\_close\_report.md").read\_text(encoding="utf-8") if Path("audit/EPIC-030\_close\_report.md").exists() else ""  
 required\_text \= \[  
 "QA Rails — Open/Close (Final PR)",  
 "Acceptance and evidence pointers",  
 "docs/acceptance\_map\_epic030.json",  
 "audit/qa/hde-epic030/token\_evidence\_matrix.md",  
 "audit/qa/hde-epic030/acceptance\_map\_viability.log",  
 "audit/qa/hde-epic030/qa\_step\_logs\_manifest.json",  
 "audit/docdeltas/hde-epic030\_drain\_targets.md",  
 \]  
 missing\_text \= \[item for item in required\_text if item not in report\]

if missing or manifest\_errors or acceptance\_map\_errors or drain\_errors or missing\_text:  
 parts \= \[\]  
 if missing:  
 parts.append("missing close-pack artifact(s): " \+ ", ".join(missing))  
 if manifest\_errors:  
 parts.append("manifest error(s): " \+ ", ".join(manifest\_errors))  
 if acceptance\_map\_errors:  
 parts.append("acceptance map error(s): " \+ ", ".join(acceptance\_map\_errors))  
 if drain\_errors:  
 parts.append("drain-target ledger error(s): " \+ ", ".join(drain\_errors))  
 if missing\_text:  
 parts.append("missing close-report text: " \+ ", ".join(missing\_text))  
 raise SystemExit("; ".join(parts))  
 PY

Close-out PASS criteria:

* Discovery artifact exists.  
* QA RCA & Doc Delta summary exists.  
* Every guide-defined check has a primary.log or a truthful TOOLING\_BLOCKED record.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json exists and is an object keyed by check\_id.  
* Every audit/qa/hde-epic030/qa\_step\_logs\_manifest.json entry contains check\_id, status, and log\_path fields, and each entry key matches its check\_id.  
* Every log\_path value in audit/qa/hde-epic030/qa\_step\_logs\_manifest.json is relative to audit/qa/hde-epic030/.  
* Every log\_path value in audit/qa/hde-epic030/qa\_step\_logs\_manifest.json resolves within audit/qa/hde-epic030/ to the matching check primary.log.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.path\_proof.txt exists and path-proves audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.  
* docs/acceptance\_map\_epic030.json exists and includes a top-level tokens array.  
* If docs/acceptance\_map\_epic030.json records any tokens, every token entry is an object with a non-empty name field.  
* audit/docdeltas/hde-epic030\_drain\_targets.md exists and either explicitly indicates no drain targets or records concrete drain-target posture.  
* The acceptance map, token matrix, viability log, drain-targets ledger, close report, close manifest, and exact close-pack path proofs are created only after the check evidence exists.  
* key\_outputs in audit/EPIC-030\_MANIFEST.json is a JSON object, not a list.  
* audit/EPIC-030\_close\_report.md includes the heading QA Rails — Open/Close (Final PR).  
* audit/EPIC-030\_close\_report.md includes an Acceptance and evidence pointers list.  
* audit/EPIC-030\_close\_report.md includes docs/acceptance\_map\_epic030.json.  
* audit/EPIC-030\_close\_report.md includes audit/qa/hde-epic030/token\_evidence\_matrix.md.  
* audit/EPIC-030\_close\_report.md includes audit/qa/hde-epic030/acceptance\_map\_viability.log.  
* audit/EPIC-030\_close\_report.md includes audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.  
* audit/EPIC-030\_close\_report.md includes audit/docdeltas/hde-epic030\_drain\_targets.md.  
* audit/EPIC-030\_close\_report.md.path\_proof.txt exists and path-proves audit/EPIC-030\_close\_report.md.  
* audit/EPIC-030\_MANIFEST.json.path\_proof.txt exists and path-proves audit/EPIC-030\_MANIFEST.json.  
* No closeout artifact claims formal SATISFIED status before PO closeout review.

Close-out FAIL criteria:

* Any required closeout artifact is missing at final review.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json is missing, malformed, not an object keyed by check\_id, or contains an entry that lacks check\_id, status, or log\_path fields.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json contains duplicate or mismatched check\_id identity posture.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json contains a log\_path value that is absolute, contains traversal, escapes the epic QA root, does not resolve to the matching check primary.log, or targets a missing file.  
* audit/qa/hde-epic030/qa\_step\_logs\_manifest.json.path\_proof.txt is missing at final review.  
* docs/acceptance\_map\_epic030.json is missing its top-level tokens array, tokens is not an array, or a non-empty token entry lacks a non-empty name field.  
* audit/docdeltas/hde-epic030\_drain\_targets.md is missing or does not explicitly indicate empty/no drain targets or concrete drain-target posture.  
* Either exact close-pack sibling path-proof artifact is missing at final review.  
* audit/EPIC-030\_close\_report.md is missing the heading QA Rails — Open/Close (Final PR).  
* audit/EPIC-030\_close\_report.md is missing the Acceptance and evidence pointers list.  
* audit/EPIC-030\_close\_report.md is missing any required acceptance or evidence pointer string.  
* Any artifact claims drainage, merge, or formal close without evidence.  
* Any future-step artifact is marked present before execution.  
* Any step hides a FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED state.

## Review guardrails

### Hard blockers for plan approval/execution

The following block plan approval or execution:

* Missing HDE-EPIC030 ID.  
* Missing stable epic QA root audit/qa/hde-epic030/.  
* Use of EVIDENCE\_ROOT, run-id roots, timestamped roots, or per-run root selection.  
* Use of a route, script, helper, test, config, or env var not proven by repo audit, canon, or explicitly QA-created under audit/qa/hde-epic030/.  
* Any guessed DEV\_SAMPLER\_URL, port, host, or start command.  
* Any command that depends on a missing dependency without preflight and TOOLING\_BLOCKED posture.  
* Any step claiming PASS without a primary.log path in evidence\_artifacts.  
* Any non-PASS step claiming acceptance tokens.  
* Any plan step requiring PF10, PF09.2, PF19, PF27, or PF23 edits as execution outputs.  
* Any public-surface widening.  
* Any unrecorded FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED state that affects closeout.  
* Missing discovery artifact.  
* Missing QA RCA & Doc Delta summary.  
* Missing closeout artifact set at final review.

### Caveats that must be recorded but are not blockers by themselves

* PF09.2 permanent drainage remains pending.  
* PR01 through PR03 fail-closed pytest visibility is not fully proven by discovered tests, unless PO makes that visibility acceptance-decisive.  
* Optional live HTTP dev sampler subcheck is TOOLING\_BLOCKED when DEV\_SAMPLER\_URL is absent.  
* Documentation drainage gaps remain follow-up items when governed implementation proof is otherwise complete.

### Acceptance-readiness rule

A step is ready for acceptance only when:

* the step’s required deliverables exist,  
* the primary.log starts with the PF27 JSON header,  
* the PASS/FAIL classification matches the evidence,  
* dependencies were preflighted,  
* blocked posture is explicit where applicable,  
* no public-surface widening or unproven repo locus is introduced.

ASK OK?  
