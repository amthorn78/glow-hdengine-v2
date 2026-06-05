### Front matter

Epic ID: HDE-EPIC033   
Plan type: Live QA Plan / Runbook Execution   
venue: Codespaces   
Target environment: other: repo-local closed-rails evidence verification in Codespaces Plan revision: r2   
Date (UTC): 2026-06-01   
Operators (names-only): PO, QA agent

#### Canon precedence statement (required)

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set (explicit; stable references only)

Canon set, titles-only:

* PF10 — HDE-Build Notes, relevant addenda: 2.1 Rendered Escape Artifacts Must Never Block Review or Execution; 2.2 PR-01 HDE-EPIC033  
* PF27 — Canon Plan Templates, Live QA Plan template obligations  
* PF19 — Glow QA Guide, tooling versus behavior failures; workflow placement; rails and evidence posture  
* PF23 — Reality Audits, planning-time repo-reality context only  
* PF05 — HDE CLI/API Vendor Reference, CLI/API semantics only if needed for command invocation posture  
* PF04 — HDE Governance, token registry and acceptance invariants where referenced by this runbook’s proof obligations  
* PF06 — Epic Process Guide, closeout deliverables and QA RCA / Doc Delta summary posture  
* PF09.5 — HDE Build Checklist Fermentation, HDE-FERM006 status posture only  
* PF12 — HDE Schemas and Artifacts, evidence index, Machine Mirror, path-proof, and HDAPI v2 evidence-family posture where referenced by this runbook’s proof obligations

Note: HDE Phased Epics is not used as a source of requirements in this runbook.

### Scope statement

This plan evaluates the following in-scope surfaces / checks:

* Step-0B — Doc Delta Capture  
* PO-001  
* PO-002  
* PO-003  
* PO-004  
* PO-005  
* PO-006  
* PO-007  
* PO-008  
* PO-009  
* PO-010  
* PO-011  
* PO-012  
* PO-013  
* PO-014  
* Close-out deliverables

This plan explicitly excludes:

* Runtime HumanDesignAPI v2 request shaping  
* Runtime HumanDesignAPI v2 conformance  
* Live vendor smoke  
* PO-only open-rails vendor execution  
* Public Reader byte, route, flag, or payload change proof  
* New service-surface proof  
* New HTTP home proof  
* AI, OpenAI, LLM, AI-agent, prompt, embedding, chatbot, model-call, AI-provider credential, AI rails, AI evidence-family, or AI acceptance-token proof  
* PF document edits or documentation drainage

#### PF10 overrides / conflicts

* PF10 Addendum 2.1 — rendered escape artifacts are display-layer noise unless raw source inspection proves a real defect; this affects path, command, token, artifact, and quote review posture for this runbook.  
* PF10 Addendum 2.2 — HDE-EPIC033 PR-01 is inventory-only for HDE-FERM006, preserves out-of-scope boundaries for HDE-FERM007, HDE-FERM008, runtime request shaping, open-rails vendor smoke, public Reader changes, new HTTP homes, and AI scope, and supports later change to Done for HDE-FERM006 and HDE-FERM006.1 through HDE-FERM006.4.  
* PF10 Addendum 2.2 — collateral path-proof refreshes are limited evidence-tooling convergence and do not introduce feature or contract scope.

### PF23 anchors

PF23 planning-time context was consulted read-only for repo-reality framing. It is informational only and is not a required check, required deliverable, acceptance token, or blocker source.

PF23 anchor components and loci touched by this runbook:

* Engine and direct caller families: engine, adapter, presenter, CLI, vendor seam, DB/cache, evidence/canon artifacts, and QA/CI determinism/contract harnesses.  
* Repo roots: audit, artifacts, docs, tools, tests, ci, catalog, schemas.  
* Evidence/index loci: docs/evidence/INDEX.json, docs/acceptance\_map\_epic033.json, artifacts/evidence\_index.jsonl, audit/docdeltas/hde-epic033\_doc\_deltas.md.  
* Tooling loci: tools/evidence/update\_evidence\_index.py, tools/evidence/validate\_evidence\_paths.py, tools/evidence/check\_lf\_endings.py, ci/checks/check\_mirror\_schema.sh, ci/checks/check\_evidence\_index\_hash.sh, ci/checks/check\_final\_lf.sh.  
* HDE-EPIC033 evidence family loci are taken from audit-proven paths in the runbook below, not from PF23 alone.

### Environment and rails posture

#### Determinism pins

Use these pins whenever producing governed bytes, primary logs, path proofs, manifest files, summaries, checksums, or validation output:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

Do not add PYTHONHASHSEED as a required rail or execution pin.

#### Rails posture

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

Rails changes by check:

* None.

This runbook must not run public documentation refresh, live vendor smoke, runtime request shaping, or any open-rails command. Any command requiring SAFE\_MODE=0 or ALLOW\_NETWORK=1 is out of scope for this Live QA Plan.

#### No VCS workflow content

This runbook does not require branch checks, commit checks, PR checks, merges, rebases, pushes, pulls, or VCS state as PASS/FAIL evidence. Limited read-only repo sanity may occur only as tooling context and must not be used as acceptance evidence.

### PO inputs needed

Required external inputs:

* None.

Optional auth/header inputs:

* None.

Secret handling:

* Do not paste, store, echo, redact, hash, or presence-log any secret for this runbook. This runbook is closed-rails and proof-only.

If a command unexpectedly asks for a secret or needs a credential, stop that check and classify it as TOOLING\_BLOCKED in the step log. Do not supply the secret.

### Evidence posture and directory structure

#### Epic QA root normalization

Canonical epic QA root:

* audit/qa/hde-epic033/

Check-centric evidence root:

* audit/qa/hde-epic033/checks/\<check\_id\>/

Stable epic-level meta root:

* audit/qa/hde-epic033/00\_meta/

#### Pre-existing artifacts expected before execution

The following artifacts are pre-existing, audit-proven, and inspected by this runbook:

* artifacts/vendor/hdapi\_v2/source\_inventory.json  
* artifacts/vendor/hdapi\_v2/source\_inventory.md  
* artifacts/vendor/hdapi\_v2/openapi\_validation.log  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md  
* artifacts/vendor/hdapi\_v2/endpoint\_reference.csv  
* artifacts/vendor/hdapi\_v2/contract\_map.json  
* artifacts/vendor/hdapi\_v2/source\_inventory.json.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/source\_inventory.md.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/openapi\_validation.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/endpoint\_reference.csv.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/contract\_map.json.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/source\_cache  
* artifacts/vendor/hdapi\_v2/source\_cache/api-reference.openapi.json  
* artifacts/vendor/hdapi\_v2/source\_cache/authentication.body  
* artifacts/vendor/hdapi\_v2/source\_cache/coordinates\_guide.body  
* artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt  
* artifacts/vendor/hdapi\_v2/source\_cache/llms\_txt.body  
* artifacts/vendor/hdapi\_v2/source\_cache/migration\_v1\_to\_v2.body  
* artifacts/vendor/hdapi\_v2/source\_cache/rate\_limiting.body  
* artifacts/vendor/hdapi\_v2/source\_cache/response\_format.body  
* artifacts/vendor/hdapi\_v2/source\_cache/robots\_preflight.body  
* artifacts/vendor/hdapi\_v2/source\_cache/source\_metadata.json  
* artifacts/vendor/hdapi\_v2/source\_cache/v1-routes.yaml  
* artifacts/vendor/hdapi\_v2/source\_cache/v1\_overview.body  
* artifacts/vendor/hdapi\_v2/source\_cache/v2-routes.yaml  
* artifacts/vendor/hdapi\_v2/source\_cache/v2\_coordinates\_chart\_page.body  
* artifacts/vendor/hdapi\_v2/source\_cache/v2\_full\_chart\_page.body  
* artifacts/vendor/hdapi\_v2/source\_cache/v2\_overview.body  
* artifacts/vendor/hdapi\_v2/source\_cache/v2\_simple\_chart\_page.body  
* audit/qa/hde-epic033/token\_evidence\_matrix.md  
* audit/qa/hde-epic033/acceptance\_map\_viability.log  
* audit/qa/hde-epic033/00\_meta/doc\_deltas.md  
* audit/docdeltas/hde-epic033\_doc\_deltas.md  
* docs/acceptance\_map\_epic033.json  
* docs/evidence/INDEX.json  
* docs/evidence/INDEX.sha256  
* artifacts/evidence\_index.jsonl  
* artifacts/evidence\_index.jsonl.sha256  
* docs/evidence/INDEX.json.path\_proof.txt  
* docs/evidence/INDEX.sha256.path\_proof.txt  
* artifacts/evidence\_index.jsonl.path\_proof.txt  
* artifacts/evidence\_index.jsonl.sha256.path\_proof.txt  
* tools/evidence/generate\_hdapi\_v2\_contract\_inventory.py  
* tools/evidence/update\_evidence\_index.py  
* tools/evidence/orientation\_demo.py  
* tools/evidence/validate\_evidence\_paths.py  
* tools/evidence/check\_lf\_endings.py  
* ci/checks/check\_mirror\_schema.sh  
* ci/checks/check\_evidence\_index\_hash.sh  
* ci/checks/check\_final\_lf.sh  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* requirements-dev.txt

#### QA-created artifacts

The following artifacts are NOT RUN until this runbook executes:

The following artifacts are NOT RUN until this runbook executes:

* audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log  
* audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-001/primary.log  
* audit/qa/hde-epic033/checks/po-001/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-002/primary.log  
* audit/qa/hde-epic033/checks/po-002/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-003/primary.log  
* audit/qa/hde-epic033/checks/po-003/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-004/primary.log  
* audit/qa/hde-epic033/checks/po-004/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-005/primary.log  
* audit/qa/hde-epic033/checks/po-005/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-006/primary.log  
* audit/qa/hde-epic033/checks/po-006/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-007/primary.log  
* audit/qa/hde-epic033/checks/po-007/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-008/primary.log  
* audit/qa/hde-epic033/checks/po-008/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-009/primary.log  
* audit/qa/hde-epic033/checks/po-009/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-010/primary.log  
* audit/qa/hde-epic033/checks/po-010/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-011/primary.log  
* audit/qa/hde-epic033/checks/po-011/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-012/primary.log  
* audit/qa/hde-epic033/checks/po-012/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-013/primary.log  
* audit/qa/hde-epic033/checks/po-013/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/po-014/primary.log  
* audit/qa/hde-epic033/checks/po-014/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log  
* audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic033/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic033/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic033/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt

#### Step-log header schema expectations

Each primary.log must begin with a single-line JSON header containing at minimum:

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

Every primary.log created by this runbook is governed evidence and must have a sibling primary.log.path\_proof.txt transcript in the same check directory. A PASS primary.log must include both its own primary.log path and its sibling primary.log.path\_proof.txt path in evidence\_artifacts.

The status values allowed in this plan are PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, and TOOLING\_BLOCKED.

If status is not PASS, claimed\_tokens must be \[\].

#### Canonical step-log header writer

Run Command S1 once in the same terminal before executing check commands.

Command S1: export LC\_ALL=C LANG=C TZ=UTC SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Run Command S2 once in the same terminal before executing check commands. It defines the canonical header writer, sibling path-proof writer, and session recorder used by the check commands. This creates no repo file.

Command S2:

pf27\_step\_header() {  
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
 }

pf27\_path\_proof() {  
 python \- "$1" \<\< 'PY'  
 from pathlib import Path  
 import datetime  
 import hashlib  
 import sys

path \= Path(sys.argv\[1\])  
 if not path.exists():  
 raise SystemExit(f"missing path for proof: {path}")  
 stat \= path.stat()  
 mtime \= datetime.datetime.utcfromtimestamp(stat.st\_mtime).replace(microsecond=0).isoformat() \+ "Z"  
 produced \= datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"  
 digest \= hashlib.sha256(path.read\_bytes()).hexdigest()  
 proof\_path \= Path(str(path) \+ ".path\_proof.txt")  
 proof\_path.write\_text(  
 "\\n".join(\[  
 f"path: {path}",  
 f"size\_bytes: {stat.st\_size}",  
 f"sha256: {digest}",  
 f"mtime\_utc: {mtime}",  
 f"produced\_at\_utc: {produced}",  
 "",  
 \]),  
 encoding="utf-8",  
 )  
 PY  
 }

pf27\_record\_check() {  
 check\_id="$1"  
 check\_name="$2"  
 pf\_refs\_json="$3"  
 intended\_tokens\_json="$4"  
 pass\_claimed\_tokens\_json="$5"  
 artifacts\_json="$6"  
 shift 6  
 validation\_command="$\*"  
 check\_root="audit/qa/hde-epic033/checks/$check\_id"  
 mkdir \-p "$check\_root"  
 body\_tmp="$check\_root/body.tmp"  
 primary\_path="$check\_root/primary.log"  
 primary\_proof\_path="$primary\_path.path\_proof.txt"  
 {  
 echo "check\_id=$check\_id"  
 echo "check\_name=$check\_name"  
 echo "validation\_command=$validation\_command"  
 echo "rails SAFE\_MODE=$SAFE\_MODE ALLOW\_NETWORK=$ALLOW\_NETWORK APP\_ENV=$APP\_ENV"  
 echo "pins LC\_ALL=$LC\_ALL LANG=$LANG TZ=$TZ"  
 bash \-lc "$validation\_command"  
 } \> "$body\_tmp" 2\>&1  
 rc=$?  
 if grep \-q '^TOOLING\_BLOCKED:' "$body\_tmp"; then  
 status="TOOLING\_BLOCKED"  
 elif grep \-q '^FAIL\_TOOLING:' "$body\_tmp"; then  
 status="FAIL\_TOOLING"  
 elif \[ "$rc" \-eq 0 \]; then  
 status="PASS"  
 else  
 status="FAIL\_BEHAVIOR"  
 fi  
 if \[ "$status" \= "PASS" \]; then  
 claimed\_tokens\_json="$pass\_claimed\_tokens\_json"  
 else  
 claimed\_tokens\_json="\[\]"  
 fi  
 commands\_json="$(python \-c 'import json,sys; print(json.dumps(\[sys.argv\[1\]\], ensure\_ascii=False))' "$validation\_command")"  
 computed\_artifacts\_json="$(python \- "$primary\_path" "$primary\_proof\_path" "$artifacts\_json" \<\< 'PY'  
 import json  
 import sys

primary \= sys.argv\[1\]  
 proof \= sys.argv\[2\]  
 provided \= json.loads(sys.argv\[3\]) if sys.argv\[3\] else \[\]  
 if isinstance(provided, str):  
 provided \= \[provided\]  
 ordered \= \[\]  
 for item in \[primary, proof\] \+ provided:  
 if item not in ordered:  
 ordered.append(item)  
 print(json.dumps(ordered, ensure\_ascii=False))  
 PY  
 )"  
 export CHECK\_ID="$check\_id"  
 export CHECK\_NAME="$check\_name"  
 export PASS\_FAIL="$status"  
 export EXIT\_CODE="$rc"  
 export COMMANDS\_JSON="$commands\_json"  
 export ARTIFACTS\_JSON="$computed\_artifacts\_json"  
 export PF\_REFS\_JSON="$pf\_refs\_json"  
 export INTENDED\_TOKENS\_JSON="$intended\_tokens\_json"  
 export CLAIMED\_TOKENS\_JSON="$claimed\_tokens\_json"  
 export COMMAND\_PROVENANCE="Copy/paste from plan"  
 pf27\_step\_header \> "$primary\_path"  
 cat "$body\_tmp" \>\> "$primary\_path"  
 pf27\_path\_proof "$primary\_path"  
 rm "$body\_tmp"  
 return "$rc"  
 }

#### Dependency readiness baseline

Common required dependencies for this runbook:

* bash  
* python  
* grep  
* test  
* mkdir  
* cat  
* find  
* sed

Common preflight check:

Command PF: command \-v bash \>/dev/null && command \-v python \>/dev/null && command \-v grep \>/dev/null && command \-v test \>/dev/null && command \-v mkdir \>/dev/null && command \-v cat \>/dev/null && command \-v find \>/dev/null && command \-v sed \>/dev/null

If missing, activation/install action:

* None for bash, python, grep, test, mkdir, cat, find, and sed. These are baseline Codespaces tools.

If still unavailable:

* TOOLING\_BLOCKED. Do not evaluate behavior.

For pytest-backed steps, the activation/install action is:

Command PYTEST-INSTALL: python \-m pip install \-r requirements-dev.txt

If pytest is still unavailable after that command:

* TOOLING\_BLOCKED. Do not evaluate behavior.

### Mandatory Step-0 artifacts

#### Step-0B — Doc Delta Capture

Purpose: mechanically record repo reality mismatches, missing prerequisites, and canon conflicts as BLOCKERS vs CAVEATS.

Doc-delta surfaces:

* audit/docdeltas/hde-epic033\_doc\_deltas.md  
* audit/qa/hde-epic033/00\_meta/doc\_deltas.md

Moon Loop boundary:

* Moon Loop may repair only QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under audit/qa/hde-epic033/.  
* Product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems are not Moon Loop scope.

#### Step-0C — Prod handshake

Not included. This runbook does not claim Codespaces-to-prod behavior, does not call production services, and does not use /internal/version.

### Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| step-0b-doc-delta-capture | Step-0B — Doc Delta Capture | D0 doc-delta baseline | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if both doc-delta surfaces exist, are path-proven, and state no PR-01 deltas | audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log and sibling primary.log.path\_proof.txt | doc-delta surfaces, primary log, and sibling path proofs | DOC\_DELTA\_PRESENT\_OK | PF27; PF06 |
| po-001 | PO-001 | Source inventory grounding | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if source inventory has closed-rails cache grounding and source cache files exist | audit/qa/hde-epic033/checks/po-001/primary.log and sibling primary.log.path\_proof.txt | source inventory, source cache, primary log, and sibling path proof | \[\] | PF10; PF12 |
| po-002 | PO-002 | AI/LLM docs boundary | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if AI/LLM docs are documentation-discovery-only and no AI runtime scope is claimed | audit/qa/hde-epic033/checks/po-002/primary.log and sibling primary.log.path\_proof.txt | source inventory, source cache, anomaly ledger, primary log, and sibling path proof | \[\] | PF10; PF04 |
| po-003 | PO-003 | Route validation authority | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if route specs validate and targeted pytest passes | audit/qa/hde-epic033/checks/po-003/primary.log and sibling primary.log.path\_proof.txt | validation log, targeted pytest output, primary log, and sibling path proof | TESTS\_PASS\_OK | PF10; PF12; PF19 |
| po-004 | PO-004 | Suspect OpenAPI quarantine | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if suspect OpenAPI remains quarantined and non-authoritative | audit/qa/hde-epic033/checks/po-004/primary.log and sibling primary.log.path\_proof.txt | validation log, anomaly ledger, primary log, and sibling path proof | \[\] | PF10; PF12 |
| po-005 | PO-005 | v2/v1 route-family separation | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if v2 chart routes and legacy v1 BodyGraph routes are explicitly separated | audit/qa/hde-epic033/checks/po-005/primary.log and sibling primary.log.path\_proof.txt | endpoint reference, contract map, primary log, and sibling path proof | \[\] | PF10; PF12 |
| po-006 | PO-006 | Contract-map non-guessing posture | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if contract map preserves inventory-only non-conformance posture | audit/qa/hde-epic033/checks/po-006/primary.log and sibling primary.log.path\_proof.txt | contract map, anomaly ledger, primary log, and sibling path proof | JSON\_CANONICAL\_CHECK\_OK | PF10; PF04; PF12 |
| po-007 | PO-007 | Governed evidence binding | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if Human Index, Machine Mirror, hash, path, LF, and path-proof checks pass | audit/qa/hde-epic033/checks/po-007/primary.log and sibling primary.log.path\_proof.txt | index, mirror, hash sentinel, path proofs, primary log, and sibling path proof | EVIDENCE\_INDEX\_UPDATED\_OK; MACHINE\_MIRROR\_UPDATED\_OK; EVIDENCE\_INDEX\_HASH\_OK; EVIDENCE\_PATHS\_VALIDATED\_OK; EVIDENCE\_PATH\_PROOFS\_OK | PF10; PF12; PF19 |
| po-008 | PO-008 | No vendor-v2-specific acceptance marker | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if acceptance posture uses only existing baseline tokens and no vendor-v2-specific token | audit/qa/hde-epic033/checks/po-008/primary.log and sibling primary.log.path\_proof.txt | acceptance map, token matrix, viability log, primary log, and sibling path proof | \[\] | PF10; PF04 |
| po-009 | PO-009 | HDE-FERM006 supportable completion posture | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if acceptance map binds HDE-FERM006.1 through HDE-FERM006.4 and no drain completion is claimed | audit/qa/hde-epic033/checks/po-009/primary.log and sibling primary.log.path\_proof.txt | acceptance map, viability log, primary log, and sibling path proof | \[\] | PF10; PF09.5 |
| po-010 | PO-010 | Later adapter/live-conformance scope unclaimed | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if HDE-FERM007/HDE-FERM008-style runtime work remains unclaimed | audit/qa/hde-epic033/checks/po-010/primary.log and sibling primary.log.path\_proof.txt | anomaly ledger, contract map, viability log, primary log, and sibling path proof | \[\] | PF10; PF04 |
| po-011 | PO-011 | Contract inventory is not runtime conformance | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if inventory artifacts explicitly deny runtime v2 conformance | audit/qa/hde-epic033/checks/po-011/primary.log and sibling primary.log.path\_proof.txt | source inventory, contract map, viability log, primary log, and sibling path proof | \[\] | PF10; PF04 |
| po-012 | PO-012 | No live smoke, public Reader, service, or AI-scope proof required | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if boundary artifacts preserve no-live-smoke and no-expansion posture | audit/qa/hde-epic033/checks/po-012/primary.log and sibling primary.log.path\_proof.txt | anomaly ledger, acceptance map, viability log, primary log, and sibling path proof | \[\] | PF10; PF04 |
| po-013 | PO-013 | Collateral evidence refresh convergence | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if evidence validation, LF, and mirror/hash checks pass under closed rails | audit/qa/hde-epic033/checks/po-013/primary.log and sibling primary.log.path\_proof.txt | validation command output, primary log, and sibling path proof | \[\] | PF10; PF19 |
| po-014 | PO-014 | Live QA plan separation | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | pf27\_record\_check | PASS if Live QA evidence remains under the QA root and does not claim implementation, closure, PF edits, or runtime expansion | audit/qa/hde-epic033/checks/po-014/primary.log and sibling primary.log.path\_proof.txt | QA root, primary logs, non-claim record, and sibling path proofs | \[\] | PF19; PF27 |
| qa-16-close-out-deliverables | Close-out deliverables | D0 closeout assembly | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python | PASS if manifest, discovery artifact, QA RCA / Doc Delta summary, and path proofs are produced | audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log and sibling primary.log.path\_proof.txt | manifest, discovery artifact, QA RCA / Doc Delta summary, primary log, and sibling path proofs | \[\] | PF27; PF06; PF19 |
|  |  |  |  |  |  |  |  |  |  |

### Check Blocks

Primary-log path-proof rule for all CHECK blocks:

* For every CHECK block below, each required deliverables list that includes a primary.log also includes the sibling primary.log.path\_proof.txt transcript in the same check directory.  
* pf27\_record\_check produces the primary.log sibling path proof for Step-0B and PO-001 through PO-014.  
* The close-out deliverables command produces the primary.log sibling path proof for the closeout assembly check.  
* PASS is not available for any check if its primary.log exists but its sibling primary.log.path\_proof.txt is missing, stale, or not listed in evidence\_artifacts.

#### CHECK step-0b-doc-delta-capture: Step-0B — Doc Delta Capture

Surface / D-goal mapping: D0 doc-delta baseline Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF27 — Canon Plan Templates; PF06 — Epic Process Guide

Goal: Verify that the two doc-delta surfaces for HDE-EPIC033 exist, are path-proven, and currently record no PR-01 contract-inventory deltas. This step satisfies the runbook self-honesty baseline before later checks.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* audit/docdeltas/hde-epic033\_doc\_deltas.md exists.  
* audit/qa/hde-epic033/00\_meta/doc\_deltas.md exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log.  
3. Continue only if the header status is PASS.

Command 1: pf27\_record\_check step-0b-doc-delta-capture "Step-0B — Doc Delta Capture" '\["PF27 — Canon Plan Templates","PF06 — Epic Process Guide"\]' '\["DOC\_DELTA\_PRESENT\_OK"\]' '\["DOC\_DELTA\_PRESENT\_OK"\]' '\["audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log","audit/docdeltas/hde-epic033\_doc\_deltas.md","audit/qa/hde-epic033/00\_meta/doc\_deltas.md","audit/docdeltas/hde-epic033\_doc\_deltas.md.path\_proof.txt","audit/qa/hde-epic033/00\_meta/doc\_deltas.md.path\_proof.txt"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f audit/docdeltas/hde-epic033\_doc\_deltas.md && test \-f audit/qa/hde-epic033/00\_meta/doc\_deltas.md && test \-f audit/docdeltas/hde-epic033\_doc\_deltas.md.path\_proof.txt && test \-f audit/qa/hde-epic033/00\_meta/doc\_deltas.md.path\_proof.txt && grep \-F "None recorded for PR-01 contract-inventory evidence binding." audit/docdeltas/hde-epic033\_doc\_deltas.md && grep \-F "None recorded for PR-01 contract-inventory evidence binding." audit/qa/hde-epic033/00\_meta/doc\_deltas.md'

What to look for:

* First line of primary.log is a JSON header.  
* status is PASS.  
* claimed\_tokens contains DOC\_DELTA\_PRESENT\_OK only if status is PASS.

Required deliverables:

* audit/qa/hde-epic033/checks/step-0b-doc-delta-capture/primary.log  
* audit/docdeltas/hde-epic033\_doc\_deltas.md  
* audit/qa/hde-epic033/00\_meta/doc\_deltas.md  
* audit/docdeltas/hde-epic033\_doc\_deltas.md.path\_proof.txt  
* audit/qa/hde-epic033/00\_meta/doc\_deltas.md.path\_proof.txt

PASS criteria:

* Both doc-delta surfaces exist.  
* Both path-proof files exist.  
* Both doc-delta surfaces record no PR-01 contract-inventory evidence-binding deltas.  
* primary.log includes the PF27 header and command transcript.

FAIL criteria:

* FAIL\_BEHAVIOR if a required doc-delta surface or path proof is absent or does not record the expected baseline.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root after the check command starts.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: DOC\_DELTA\_PRESENT\_OK  
* claimed\_tokens: DOC\_DELTA\_PRESENT\_OK only if PASS, else \[\]

#### CHECK po-001: PO-001

Surface / D-goal mapping: Source inventory grounding Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF12 — HDE Schemas and Artifacts

Goal: Verify that the vendor-contract inventory identifies conformance-planning source material and is grounded in actual cached source content rather than metadata-only entries.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/source\_inventory.json exists.  
* artifacts/vendor/hdapi\_v2/source\_inventory.md exists.  
* artifacts/vendor/hdapi\_v2/source\_cache exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-001/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-001/primary.log.  
3. Confirm the log proves cache paths, cache hashes, and required source-cache files.

Command 1: pf27\_record\_check po-001 "PO-001" '\["PF10 — HDE-Build Notes","PF12 — HDE Schemas and Artifacts"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-001/primary.log","artifacts/vendor/hdapi\_v2/source\_inventory.json","artifacts/vendor/hdapi\_v2/source\_inventory.md","artifacts/vendor/hdapi\_v2/source\_cache"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/source\_inventory.json && test \-f artifacts/vendor/hdapi\_v2/source\_inventory.md && test \-d artifacts/vendor/hdapi\_v2/source\_cache && grep \-F "Source mode: closed-rails-source-cache" artifacts/vendor/hdapi\_v2/source\_inventory.md && grep \-F "cache\_path" artifacts/vendor/hdapi\_v2/source\_inventory.md && grep \-F "cache\_sha256" artifacts/vendor/hdapi\_v2/source\_inventory.md && test \-f artifacts/vendor/hdapi\_v2/source\_cache/v1-routes.yaml && test \-f artifacts/vendor/hdapi\_v2/source\_cache/v2-routes.yaml && test \-f artifacts/vendor/hdapi\_v2/source\_cache/source\_metadata.json'

What to look for:

* Source mode is closed-rails-source-cache.  
* source\_inventory.md contains cache\_path and cache\_sha256.  
* v1-routes.yaml, v2-routes.yaml, and source\_metadata.json exist under the source cache.

Required deliverables:

* audit/qa/hde-epic033/checks/po-001/primary.log  
* artifacts/vendor/hdapi\_v2/source\_inventory.json  
* artifacts/vendor/hdapi\_v2/source\_inventory.md  
* artifacts/vendor/hdapi\_v2/source\_cache/v1-routes.yaml  
* artifacts/vendor/hdapi\_v2/source\_cache/v2-routes.yaml  
* artifacts/vendor/hdapi\_v2/source\_cache/source\_metadata.json

PASS criteria:

* Source inventory artifacts exist.  
* The human-readable source inventory records closed-rails cache mode.  
* The inventory records cache\_path and cache\_sha256.  
* Required source-cache route and metadata files exist.

FAIL criteria:

* FAIL\_BEHAVIOR if source inventory grounding is absent or cache source files are missing.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-002: PO-002

Surface / D-goal mapping: AI/LLM documentation-discovery boundary Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF04 — HDE Governance

Goal: Verify that AI or language-model oriented vendor documentation remains documentation-structure context only and creates no product, runtime, evidence, credential, rail, or QA scope.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/source\_inventory.md exists.  
* artifacts/vendor/hdapi\_v2/source\_cache/llms\_txt.body exists.  
* artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt exists.  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-002/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-002/primary.log.  
3. Confirm no AI feature, runtime, credential, rail, or QA scope is claimed.

Command 1: pf27\_record\_check po-002 "PO-002" '\["PF10 — HDE-Build Notes","PF04 — HDE Governance"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-002/primary.log","artifacts/vendor/hdapi\_v2/source\_inventory.md","artifacts/vendor/hdapi\_v2/source\_cache/llms\_txt.body","artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt","artifacts/vendor/hdapi\_v2/known\_anomalies.md"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/source\_inventory.md && test \-f artifacts/vendor/hdapi\_v2/source\_cache/llms\_txt.body && test \-f artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt && grep \-F "documentation-discovery-only" artifacts/vendor/hdapi\_v2/source\_inventory.md && grep \-F "creates no AI product" artifacts/vendor/hdapi\_v2/source\_inventory.md && grep \-F "AI runtime/evidence scope" artifacts/vendor/hdapi\_v2/known\_anomalies.md'

What to look for:

* The inventory uses documentation-discovery-only wording.  
* llms source-cache files exist.  
* The anomaly ledger preserves no AI runtime or evidence scope.

Required deliverables:

* audit/qa/hde-epic033/checks/po-002/primary.log  
* artifacts/vendor/hdapi\_v2/source\_inventory.md  
* artifacts/vendor/hdapi\_v2/source\_cache/llms\_txt.body  
* artifacts/vendor/hdapi\_v2/source\_cache/llms-full.endpoint-tiers.txt  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md

PASS criteria:

* AI/LLM-oriented vendor docs are present only as documentation-discovery context.  
* No AI product, runtime, evidence, credential, rail, QA, prompt, embedding, chatbot, model-call, or provider scope is claimed.

FAIL criteria:

* FAIL\_BEHAVIOR if AI/LLM docs are promoted beyond documentation-discovery context.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-003: PO-003

Surface / D-goal mapping: Machine-readable route validation Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF12 — HDE Schemas and Artifacts; PF19 — Glow QA Guide

Goal: Verify that machine-readable route descriptions are validated for vendor ownership and route family before they are treated as authoritative contract sources.

Required dependencies:

* Common dependency baseline.  
* python \-m pytest.  
* requirements-dev.txt for pytest installation if needed.

Preflight check:

Command 1: python \-m pytest \--version || python \-m pip install \-r requirements-dev.txt

If missing, activation/install action:

Command 2: python \-m pip install \-r requirements-dev.txt

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py exists.  
* artifacts/vendor/hdapi\_v2/openapi\_validation.log exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-003/.

Numbered PO actions:

1. Run Command 1 if pytest readiness has not already been proven in this terminal.  
2. Run Command 3\.  
3. Read audit/qa/hde-epic033/checks/po-003/primary.log.  
4. Confirm the targeted test and route validation strings pass.

Command 3: pf27\_record\_check po-003 "PO-003" '\["PF10 — HDE-Build Notes","PF12 — HDE Schemas and Artifacts","PF19 — Glow QA Guide"\]' '\["TESTS\_PASS\_OK"\]' '\["TESTS\_PASS\_OK"\]' '\["audit/qa/hde-epic033/checks/po-003/primary.log","artifacts/vendor/hdapi\_v2/openapi\_validation.log","tests/evidence/test\_hdapi\_v2\_contract\_inventory.py"\]' 'command \-v python \>/dev/null || { echo "TOOLING\_BLOCKED: python missing"; exit 99; }; test \-f tests/evidence/test\_hdapi\_v2\_contract\_inventory.py && test \-f artifacts/vendor/hdapi\_v2/openapi\_validation.log && grep \-F "\[v2-routes.yaml\] status=VALIDATED" artifacts/vendor/hdapi\_v2/openapi\_validation.log && grep \-F "\[v1-routes.yaml\] status=VALIDATED" artifacts/vendor/hdapi\_v2/openapi\_validation.log && grep \-F "\[route-spec-gate\] status=PASS" artifacts/vendor/hdapi\_v2/openapi\_validation.log && python \-m pytest tests/evidence/test\_hdapi\_v2\_contract\_inventory.py'

What to look for:

* v2-routes.yaml status is VALIDATED.  
* v1-routes.yaml status is VALIDATED.  
* route-spec-gate status is PASS.  
* pytest exits 0\.

Required deliverables:

* audit/qa/hde-epic033/checks/po-003/primary.log  
* artifacts/vendor/hdapi\_v2/openapi\_validation.log  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py

PASS criteria:

* Validation log proves v2 and v1 route specs are validated.  
* Targeted pytest exits 0 under closed rails and determinism pins.  
* primary.log captures the command transcript and PASS header.

FAIL criteria:

* FAIL\_BEHAVIOR if route validation status is missing or pytest runs and fails assertions.  
* TOOLING\_BLOCKED if pytest, Python, or the test file is unavailable.  
* FAIL\_TOOLING if pytest collection fails due missing dependency after the allowed install action, or if primary.log cannot be written.

Blocked posture:

* If pytest cannot be made available with requirements-dev.txt, record TOOLING\_BLOCKED.

Tokens:

* intended\_tokens: TESTS\_PASS\_OK  
* claimed\_tokens: TESTS\_PASS\_OK only if PASS, else \[\]

#### CHECK po-004: PO-004

Surface / D-goal mapping: Suspect machine-readable source quarantine Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF12 — HDE Schemas and Artifacts

Goal: Verify that any suspect machine-readable contract source remains quarantined unless vendor ownership and route-family authority are proven.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/openapi\_validation.log exists.  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-004/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-004/primary.log.  
3. Confirm suspect OpenAPI remains non-authoritative.

Command 1: pf27\_record\_check po-004 "PO-004" '\["PF10 — HDE-Build Notes","PF12 — HDE Schemas and Artifacts"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-004/primary.log","artifacts/vendor/hdapi\_v2/openapi\_validation.log","artifacts/vendor/hdapi\_v2/known\_anomalies.md"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/openapi\_validation.log && test \-f artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "\[api-reference/openapi.json\] status=QUARANTINED" artifacts/vendor/hdapi\_v2/openapi\_validation.log && grep \-F "Decision: QUARANTINED" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "not used as authority" artifacts/vendor/hdapi\_v2/known\_anomalies.md'

What to look for:

* api-reference/openapi.json status is QUARANTINED.  
* known\_anomalies.md says the suspect artifact is not used as authority.

Required deliverables:

* audit/qa/hde-epic033/checks/po-004/primary.log  
* artifacts/vendor/hdapi\_v2/openapi\_validation.log  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md

PASS criteria:

* Suspect OpenAPI is quarantined.  
* Quarantine prevents authority for vendor bytes, schemas, endpoint routes, request shaping, response mapping, runtime conformance, or architecture conformance.

FAIL criteria:

* FAIL\_BEHAVIOR if the suspect artifact is validated without proof or used as authority.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-005: PO-005

Surface / D-goal mapping: Route-family reference Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF12 — HDE Schemas and Artifacts

Goal: Verify that the vendor route reference clearly distinguishes recommended v2 chart routes from legacy v1 BodyGraph routes.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/endpoint\_reference.csv exists.  
* artifacts/vendor/hdapi\_v2/contract\_map.json exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-005/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-005/primary.log.  
3. Confirm all five required routes and route families are present.

Command 1: pf27\_record\_check po-005 "PO-005" '\["PF10 — HDE-Build Notes","PF12 — HDE Schemas and Artifacts"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-005/primary.log","artifacts/vendor/hdapi\_v2/endpoint\_reference.csv","artifacts/vendor/hdapi\_v2/contract\_map.json"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/endpoint\_reference.csv && test \-f artifacts/vendor/hdapi\_v2/contract\_map.json && grep \-F "POST,/v2/charts,recommended\_v2\_chart" artifacts/vendor/hdapi\_v2/endpoint\_reference.csv && grep \-F "POST,/v2/charts/simple,recommended\_v2\_chart" artifacts/vendor/hdapi\_v2/endpoint\_reference.csv && grep \-F "POST,/v2/charts/coordinates,recommended\_v2\_chart" artifacts/vendor/hdapi\_v2/endpoint\_reference.csv && grep \-F "POST,/v1/bodygraphs,legacy\_v1\_bodygraph" artifacts/vendor/hdapi\_v2/endpoint\_reference.csv && grep \-F "POST,/v1/bodygraphs/simple,legacy\_v1\_bodygraph" artifacts/vendor/hdapi\_v2/endpoint\_reference.csv && grep \-F "recommended\_v2\_chart" artifacts/vendor/hdapi\_v2/contract\_map.json && grep \-F "legacy\_v1\_bodygraph" artifacts/vendor/hdapi\_v2/contract\_map.json'

What to look for:

* Three v2 chart routes are classified as recommended\_v2\_chart.  
* Two v1 BodyGraph routes are classified as legacy\_v1\_bodygraph.  
* contract\_map.json preserves both route-family labels.

Required deliverables:

* audit/qa/hde-epic033/checks/po-005/primary.log  
* artifacts/vendor/hdapi\_v2/endpoint\_reference.csv  
* artifacts/vendor/hdapi\_v2/contract\_map.json

PASS criteria:

* All five required route rows are present.  
* v2 chart route family is separate from legacy v1 BodyGraph route family.  
* The check does not claim runtime request shaping.

FAIL criteria:

* FAIL\_BEHAVIOR if route-family separation is absent, collapsed, or ambiguous.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-006: PO-006

Surface / D-goal mapping: Contract-map non-guessing posture Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF04 — HDE Governance; PF12 — HDE Schemas and Artifacts

Goal: Verify that the contract map captures vendor contract facts for later request and response work without guessing unpinned infrastructure, credential, or runtime request-byte details.

Required dependencies:

* Common dependency baseline.  
* python standard library.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for Python standard library.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/contract\_map.json exists.  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-006/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-006/primary.log.  
3. Confirm contract map is canonical JSON and preserves non-conformance posture.

Command 1: pf27\_record\_check po-006 "PO-006" '\["PF10 — HDE-Build Notes","PF04 — HDE Governance","PF12 — HDE Schemas and Artifacts"\]' '\["JSON\_CANONICAL\_CHECK\_OK"\]' '\["JSON\_CANONICAL\_CHECK\_OK"\]' '\["audit/qa/hde-epic033/checks/po-006/primary.log","artifacts/vendor/hdapi\_v2/contract\_map.json","artifacts/vendor/hdapi\_v2/known\_anomalies.md"\]' 'command \-v python \>/dev/null || { echo "TOOLING\_BLOCKED: python missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/contract\_map.json && test \-f artifacts/vendor/hdapi\_v2/known\_anomalies.md && python \-c "import json, pathlib; p=pathlib.Path("artifacts/vendor/hdapi\_v2/contract\_map.json"); json.loads(p.read\_text()); assert p.read\_text().endswith("\\n")" && grep \-F "non\_conformance\_claim" artifacts/vendor/hdapi\_v2/contract\_map.json && grep \-F "Contract inventory only" artifacts/vendor/hdapi\_v2/contract\_map.json && grep \-F "no runtime v2 request shaping" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "no runtime v2 request shaping" artifacts/vendor/hdapi\_v2/contract\_map.json'

What to look for:

* contract\_map.json parses as JSON and ends with a final LF.  
* non\_conformance\_claim is present.  
* Contract inventory only posture is present.  
* Runtime request shaping remains unclaimed.

Required deliverables:

* audit/qa/hde-epic033/checks/po-006/primary.log  
* artifacts/vendor/hdapi\_v2/contract\_map.json  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md

PASS criteria:

* Contract map is parseable JSON with final LF.  
* Contract map contains non\_conformance\_claim.  
* Contract map and anomaly ledger preserve no runtime request shaping.

FAIL criteria:

* FAIL\_BEHAVIOR if contract map is non-parseable, lacks final LF, or guesses runtime request shaping, infrastructure, credential, or request-byte details.  
* TOOLING\_BLOCKED if Python or common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: JSON\_CANONICAL\_CHECK\_OK  
* claimed\_tokens: JSON\_CANONICAL\_CHECK\_OK only if PASS, else \[\]

#### CHECK po-007: PO-007

Surface / D-goal mapping: Governed evidence binding Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF12 — HDE Schemas and Artifacts; PF19 — Glow QA Guide

Goal: Verify that the governed evidence record coherently binds source inventory, validation result, anomaly posture, route reference, and contract map into human-reviewable and machine-reviewable evidence.

Required dependencies:

* Common dependency baseline.  
* python.  
* ci/checks/check\_mirror\_schema.sh.  
* ci/checks/check\_evidence\_index\_hash.sh.  
* ci/checks/check\_final\_lf.sh.  
* tools/evidence/update\_evidence\_index.py.  
* tools/evidence/validate\_evidence\_paths.py.  
* tools/evidence/check\_lf\_endings.py.

Preflight check:

* Command PF.  
* Command 1 below verifies all required scripts and checks exist.

If missing, activation/install action:

* None for these repo scripts.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* docs/evidence/INDEX.json exists.  
* artifacts/evidence\_index.jsonl exists.  
* Relevant path proofs exist.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-007/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-007/primary.log.  
3. Confirm evidence-index, mirror, hash, path validation, LF, and path-proof checks pass.

Command 1: pf27\_record\_check po-007 "PO-007" '\["PF10 — HDE-Build Notes","PF12 — HDE Schemas and Artifacts","PF19 — Glow QA Guide"\]' '\["EVIDENCE\_INDEX\_UPDATED\_OK","MACHINE\_MIRROR\_UPDATED\_OK","EVIDENCE\_INDEX\_HASH\_OK","EVIDENCE\_PATHS\_VALIDATED\_OK","EVIDENCE\_PATH\_PROOFS\_OK"\]' '\["EVIDENCE\_INDEX\_UPDATED\_OK","MACHINE\_MIRROR\_UPDATED\_OK","EVIDENCE\_INDEX\_HASH\_OK","EVIDENCE\_PATHS\_VALIDATED\_OK","EVIDENCE\_PATH\_PROOFS\_OK"\]' '\["audit/qa/hde-epic033/checks/po-007/primary.log","docs/evidence/INDEX.json","docs/evidence/INDEX.sha256","artifacts/evidence\_index.jsonl","artifacts/evidence\_index.jsonl.sha256","docs/evidence/INDEX.json.path\_proof.txt","docs/evidence/INDEX.sha256.path\_proof.txt","artifacts/evidence\_index.jsonl.path\_proof.txt","artifacts/evidence\_index.jsonl.sha256.path\_proof.txt"\]' 'command \-v python \>/dev/null || { echo "TOOLING\_BLOCKED: python missing"; exit 99; }; test \-f tools/evidence/update\_evidence\_index.py && test \-f tools/evidence/validate\_evidence\_paths.py && test \-f tools/evidence/check\_lf\_endings.py && test \-f ci/checks/check\_mirror\_schema.sh && test \-f ci/checks/check\_evidence\_index\_hash.sh && test \-f ci/checks/check\_final\_lf.sh && test \-f docs/evidence/INDEX.json && test \-f artifacts/evidence\_index.jsonl && grep \-F "artifacts/vendor/hdapi\_v2/source\_inventory.json" docs/evidence/INDEX.json && grep \-F "artifacts/vendor/hdapi\_v2/contract\_map.json" artifacts/evidence\_index.jsonl && python tools/evidence/update\_evidence\_index.py \--check && python tools/evidence/validate\_evidence\_paths.py && python tools/evidence/check\_lf\_endings.py && python ci/checks/check\_mirror\_schema.sh && bash ci/checks/check\_evidence\_index\_hash.sh && bash ci/checks/check\_final\_lf.sh'

What to look for:

* All command outputs exit 0\.  
* Evidence index and Machine Mirror include HDE-EPIC033 primary artifacts.  
* Path-proof and hash checks are coherent.

Required deliverables:

* audit/qa/hde-epic033/checks/po-007/primary.log  
* docs/evidence/INDEX.json  
* docs/evidence/INDEX.sha256  
* artifacts/evidence\_index.jsonl  
* artifacts/evidence\_index.jsonl.sha256  
* docs/evidence/INDEX.json.path\_proof.txt  
* docs/evidence/INDEX.sha256.path\_proof.txt  
* artifacts/evidence\_index.jsonl.path\_proof.txt  
* artifacts/evidence\_index.jsonl.sha256.path\_proof.txt

PASS criteria:

* All listed evidence validation commands exit 0\.  
* Human Evidence Index binds source inventory and contract map.  
* Machine Mirror binds contract map and related HDE-EPIC033 artifacts.  
* Hash and path-proof files exist and validate.

FAIL criteria:

* FAIL\_BEHAVIOR if any evidence binding, path validation, mirror schema, hash, or LF command runs and reports mismatch.  
* TOOLING\_BLOCKED if any required script/check file is absent or Python is unavailable.  
* FAIL\_TOOLING if a check cannot execute due invocation or permission issues not resolved by the specified invocation.

Blocked posture:

* If ci/checks/check\_mirror\_schema.sh is not executable, this plan uses python ci/checks/check\_mirror\_schema.sh by design. Do not use bash for that script.  
* No rerun audit is required unless one of the listed script paths is absent.

Tokens:

* intended\_tokens: EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK  
* claimed\_tokens: same list only if PASS, else \[\]

#### CHECK po-008: PO-008

Surface / D-goal mapping: Acceptance posture and token non-minting Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF04 — HDE Governance

Goal: Verify that the epic’s acceptance posture relies only on existing registry-governed acceptance markers and does not mint or imply a vendor-v2-specific marker.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* docs/acceptance\_map\_epic033.json exists.  
* audit/qa/hde-epic033/token\_evidence\_matrix.md exists.  
* audit/qa/hde-epic033/acceptance\_map\_viability.log exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-008/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-008/primary.log.  
3. Confirm the viability log says vendor\_v2\_specific\_tokens=NONE.

Command 1: pf27\_record\_check po-008 "PO-008" '\["PF10 — HDE-Build Notes","PF04 — HDE Governance"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-008/primary.log","docs/acceptance\_map\_epic033.json","audit/qa/hde-epic033/token\_evidence\_matrix.md","audit/qa/hde-epic033/acceptance\_map\_viability.log"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f docs/acceptance\_map\_epic033.json && test \-f audit/qa/hde-epic033/token\_evidence\_matrix.md && test \-f audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "baseline\_existing\_tokens\_only" docs/acceptance\_map\_epic033.json && grep \-F "vendor\_v2\_specific\_tokens=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "uses existing registry-valid tokens only" audit/qa/hde-epic033/token\_evidence\_matrix.md && grep \-F "does not mint a vendor-v2-specific token" audit/qa/hde-epic033/token\_evidence\_matrix.md'

What to look for:

* baseline\_existing\_tokens\_only is present.  
* vendor\_v2\_specific\_tokens=NONE is present.  
* Token matrix explicitly states existing registry-valid tokens only.

Required deliverables:

* audit/qa/hde-epic033/checks/po-008/primary.log  
* docs/acceptance\_map\_epic033.json  
* audit/qa/hde-epic033/token\_evidence\_matrix.md  
* audit/qa/hde-epic033/acceptance\_map\_viability.log

PASS criteria:

* No vendor-v2-specific acceptance token is minted or implied.  
* Acceptance posture remains baseline existing tokens only.

FAIL criteria:

* FAIL\_BEHAVIOR if a vendor-v2-specific token is present, implied, or claimed.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-009: PO-009

Surface / D-goal mapping: HDE-FERM006 supportable completion posture Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF09.5 — HDE Build Checklist Fermentation

Goal: Verify that the in-scope Fermentation contract-inventory checklist rows are supportable as complete in substance, while keeping checklist drainage separate from repo-supported completion.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* docs/acceptance\_map\_epic033.json exists.  
* audit/qa/hde-epic033/acceptance\_map\_viability.log exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-009/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-009/primary.log.  
3. Confirm all four HDE-FERM006 subtasks are present and no drain completion is claimed.

Command 1: pf27\_record\_check po-009 "PO-009" '\["PF10 — HDE-Build Notes","PF09.5 — HDE Build Checklist Fermentation"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-009/primary.log","docs/acceptance\_map\_epic033.json","audit/qa/hde-epic033/acceptance\_map\_viability.log"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f docs/acceptance\_map\_epic033.json && test \-f audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "HDE-FERM006.1" docs/acceptance\_map\_epic033.json && grep \-F "HDE-FERM006.2" docs/acceptance\_map\_epic033.json && grep \-F "HDE-FERM006.3" docs/acceptance\_map\_epic033.json && grep \-F "HDE-FERM006.4" docs/acceptance\_map\_epic033.json && grep \-F "runtime\_v2\_conformance\_claim=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log'

What to look for:

* HDE-FERM006.1 through HDE-FERM006.4 are present in the acceptance map.  
* runtime\_v2\_conformance\_claim=NONE is present.

Required deliverables:

* audit/qa/hde-epic033/checks/po-009/primary.log  
* docs/acceptance\_map\_epic033.json  
* audit/qa/hde-epic033/acceptance\_map\_viability.log

PASS criteria:

* HDE-FERM006.1 through HDE-FERM006.4 are bound in the acceptance map.  
* primary.log states this is supportable from repo evidence only, not already drained into PF09.5 unless separately proven by PF09.5.

FAIL criteria:

* FAIL\_BEHAVIOR if one or more HDE-FERM006 subtasks is missing or runtime conformance is claimed.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-010: PO-010

Surface / D-goal mapping: Later adapter/live-conformance work remains unclaimed Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF04 — HDE Governance

Goal: Verify that later vendor-adapter architecture and live-conformance work remains unclaimed by this epic.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/known\_anomalies.md exists.  
* artifacts/vendor/hdapi\_v2/contract\_map.json exists.  
* audit/qa/hde-epic033/acceptance\_map\_viability.log exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-010/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-010/primary.log.  
3. Confirm later request shaping, live conformance, and open-rails smoke are unclaimed.

Command 1: pf27\_record\_check po-010 "PO-010" '\["PF10 — HDE-Build Notes","PF04 — HDE Governance"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-010/primary.log","artifacts/vendor/hdapi\_v2/known\_anomalies.md","artifacts/vendor/hdapi\_v2/contract\_map.json","audit/qa/hde-epic033/acceptance\_map\_viability.log"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/known\_anomalies.md && test \-f artifacts/vendor/hdapi\_v2/contract\_map.json && test \-f audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "no runtime v2 request shaping" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "open-rails vendor smoke" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "no HumanDesignAPI v2 runtime request shaping" artifacts/vendor/hdapi\_v2/contract\_map.json && grep \-F "runtime\_v2\_conformance\_claim=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log'

What to look for:

* no runtime v2 request shaping is present.  
* open-rails vendor smoke is named as not introduced or not claimed.  
* runtime\_v2\_conformance\_claim=NONE is present.

Required deliverables:

* audit/qa/hde-epic033/checks/po-010/primary.log  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md  
* artifacts/vendor/hdapi\_v2/contract\_map.json  
* audit/qa/hde-epic033/acceptance\_map\_viability.log

PASS criteria:

* Runtime request shaping is unclaimed.  
* Live vendor smoke is unclaimed.  
* Runtime conformance remains unclaimed.  
* The check does not create any open-rails execution.

FAIL criteria:

* FAIL\_BEHAVIOR if later adapter/live-conformance scope is claimed by HDE-EPIC033 evidence.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-011: PO-011

Surface / D-goal mapping: Inventory is not runtime conformance Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF04 — HDE Governance

Goal: Verify that the QA plan does not treat contract inventory as proof of runtime vendor conformance.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/source\_inventory.md exists.  
* artifacts/vendor/hdapi\_v2/contract\_map.json exists.  
* audit/qa/hde-epic033/acceptance\_map\_viability.log exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-011/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-011/primary.log.  
3. Confirm the evidence says inventory only and no runtime conformance.

Command 1: pf27\_record\_check po-011 "PO-011" '\["PF10 — HDE-Build Notes","PF04 — HDE Governance"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-011/primary.log","artifacts/vendor/hdapi\_v2/source\_inventory.md","artifacts/vendor/hdapi\_v2/contract\_map.json","audit/qa/hde-epic033/acceptance\_map\_viability.log"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/source\_inventory.md && test \-f artifacts/vendor/hdapi\_v2/contract\_map.json && test \-f audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "does not claim runtime v2 conformance" artifacts/vendor/hdapi\_v2/source\_inventory.md && grep \-F "Contract inventory only" artifacts/vendor/hdapi\_v2/contract\_map.json && grep \-F "runtime\_v2\_conformance\_claim=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log'

What to look for:

* source\_inventory.md says it does not claim runtime v2 conformance.  
* contract\_map.json says Contract inventory only.  
* viability log says runtime\_v2\_conformance\_claim=NONE.

Required deliverables:

* audit/qa/hde-epic033/checks/po-011/primary.log  
* artifacts/vendor/hdapi\_v2/source\_inventory.md  
* artifacts/vendor/hdapi\_v2/contract\_map.json  
* audit/qa/hde-epic033/acceptance\_map\_viability.log

PASS criteria:

* Contract inventory evidence does not claim runtime vendor conformance.  
* The runbook does not execute any runtime vendor conformance command.

FAIL criteria:

* FAIL\_BEHAVIOR if inventory evidence is used or worded as runtime conformance.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-012: PO-012

Surface / D-goal mapping: No live smoke, public Reader, new service, or AI-scope proof required Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF04 — HDE Governance

Goal: Verify that this runbook does not require live vendor smoke, runtime request shaping proof, public Reader change proof, new service-surface proof, or AI-scope proof for this epic.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* artifacts/vendor/hdapi\_v2/known\_anomalies.md exists.  
* docs/acceptance\_map\_epic033.json exists.  
* audit/qa/hde-epic033/acceptance\_map\_viability.log exists.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-012/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-012/primary.log.  
3. Confirm the runbook and evidence stay proof-only and closed-rails.

Command 1: pf27\_record\_check po-012 "PO-012" '\["PF10 — HDE-Build Notes","PF04 — HDE Governance"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-012/primary.log","artifacts/vendor/hdapi\_v2/known\_anomalies.md","docs/acceptance\_map\_epic033.json","audit/qa/hde-epic033/acceptance\_map\_viability.log"\]' 'command \-v grep \>/dev/null || { echo "TOOLING\_BLOCKED: grep missing"; exit 99; }; test \-f artifacts/vendor/hdapi\_v2/known\_anomalies.md && test \-f docs/acceptance\_map\_epic033.json && test \-f audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "no runtime v2 request shaping" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "open-rails vendor smoke" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "public Reader byte change" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "new HTTP home" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "AI runtime/evidence scope" artifacts/vendor/hdapi\_v2/known\_anomalies.md && grep \-F "public\_reader\_surface\_change=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "ai\_scope=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log'

What to look for:

* no runtime v2 request shaping.  
* open-rails vendor smoke appears only as an unclaimed boundary.  
* no public Reader surface change.  
* no AI runtime or evidence scope.

Required deliverables:

* audit/qa/hde-epic033/checks/po-012/primary.log  
* artifacts/vendor/hdapi\_v2/known\_anomalies.md  
* docs/acceptance\_map\_epic033.json  
* audit/qa/hde-epic033/acceptance\_map\_viability.log

PASS criteria:

* Boundary evidence preserves no live vendor smoke, no public Reader change, no new HTTP home, and no AI scope.  
* No command in this check opens rails or calls a live provider.

FAIL criteria:

* FAIL\_BEHAVIOR if the runbook or evidence requires a live vendor smoke, runtime request shaping, public Reader change, service-surface, or AI-scope proof.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-013: PO-013

Surface / D-goal mapping: Collateral evidence refresh convergence Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide

Goal: Verify that collateral evidence refreshes are treated as evidence-tooling convergence only and are not interpreted as feature or contract expansion.

Required dependencies:

* Common dependency baseline.  
* python.  
* tools/evidence/validate\_evidence\_paths.py.  
* tools/evidence/check\_lf\_endings.py.  
* tools/evidence/orientation\_demo.py.  
* ci/checks/check\_final\_lf.sh.  
* ci/checks/check\_mirror\_schema.sh.  
* ci/checks/check\_evidence\_index\_hash.sh.

Preflight check:

* Command PF.  
* Command 1 below verifies script existence.

If missing, activation/install action:

* None for these repo scripts.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* The evidence tool scripts listed above exist.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-013/.

Numbered PO actions:

1. Run Command 1\.  
2. Read audit/qa/hde-epic033/checks/po-013/primary.log.  
3. Confirm all evidence-convergence checks exit 0 and no feature expansion is claimed.

Command 1: pf27\_record\_check po-013 "PO-013" '\["PF10 — HDE-Build Notes","PF19 — Glow QA Guide"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-013/primary.log","tools/evidence/validate\_evidence\_paths.py","tools/evidence/check\_lf\_endings.py","tools/evidence/orientation\_demo.py","ci/checks/check\_final\_lf.sh","ci/checks/check\_mirror\_schema.sh","ci/checks/check\_evidence\_index\_hash.sh"\]' 'command \-v python \>/dev/null || { echo "TOOLING\_BLOCKED: python missing"; exit 99; }; test \-f tools/evidence/validate\_evidence\_paths.py && test \-f tools/evidence/check\_lf\_endings.py && test \-f tools/evidence/orientation\_demo.py && test \-f ci/checks/check\_final\_lf.sh && test \-f ci/checks/check\_mirror\_schema.sh && test \-f ci/checks/check\_evidence\_index\_hash.sh && python tools/evidence/validate\_evidence\_paths.py && python tools/evidence/check\_lf\_endings.py && python tools/evidence/orientation\_demo.py \--check && python ci/checks/check\_mirror\_schema.sh && bash ci/checks/check\_evidence\_index\_hash.sh && bash ci/checks/check\_final\_lf.sh && grep \-F "runtime\_v2\_conformance\_claim=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "public\_reader\_surface\_change=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log && grep \-F "ai\_scope=NONE" audit/qa/hde-epic033/acceptance\_map\_viability.log'

What to look for:

* Evidence validation and LF checks exit 0\.  
* Viability log preserves no runtime conformance, no public Reader surface change, and no AI scope.  
* Any collateral refresh remains evidence posture only.

Required deliverables:

* audit/qa/hde-epic033/checks/po-013/primary.log

PASS criteria:

* Evidence path validation passes.  
* LF checks pass.  
* Orientation check passes.  
* Mirror/hash checks pass.  
* Viability log preserves non-expansion boundaries.

FAIL criteria:

* FAIL\_BEHAVIOR if evidence validation reports incoherence or boundary artifacts claim feature or contract expansion.  
* TOOLING\_BLOCKED if a required script or Python is unavailable.  
* FAIL\_TOOLING if a command cannot execute due invocation or permission issues.

Blocked posture:

* No blocked locus is expected.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK po-014: PO-014

Surface / D-goal mapping: Live QA plan separation and evidence location Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF19 — Glow QA Guide; PF27 — Canon Plan Templates

Goal: Verify that this Live QA Plan is a separate proof work product that verifies accepted scope without embedding implementation work, closure decisions, or runbook content into implementation artifacts.

Required dependencies:

* Common dependency baseline.  
* No pytest required.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for common tools.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* audit/qa/hde-epic033 exists.  
* audit/qa/hde-epic033/checks exists after check execution begins.

Setup:

* The command creates audit/qa/hde-epic033/checks/po-014/.

Numbered PO actions:

1. Run Command 1 after prior PO checks have run or after intentionally deciding to record partial coverage.  
2. Read audit/qa/hde-epic033/checks/po-014/primary.log.  
3. Confirm Live QA evidence stays under audit/qa/hde-epic033 and no implementation, PF-edit, or runtime-expansion claim is made.

Command 1: pf27\_record\_check po-014 "PO-014" '\["PF19 — Glow QA Guide","PF27 — Canon Plan Templates"\]' '\[\]' '\[\]' '\["audit/qa/hde-epic033/checks/po-014/primary.log","audit/qa/hde-epic033"\]' 'test \-d audit/qa/hde-epic033 && test \-d audit/qa/hde-epic033/checks && find audit/qa/hde-epic033/checks \-name primary.log \-type f | grep \-F "primary.log" && echo "non\_claims: no implementation work; no PF document edit; no runtime vendor conformance; no public Reader change; no new HTTP home; no AI scope; no epic closure action"'

What to look for:

* Primary logs are under audit/qa/hde-epic033/checks/.  
* The log records the non-claims explicitly.

Required deliverables:

* audit/qa/hde-epic033/checks/po-014/primary.log  
* audit/qa/hde-epic033/checks/\*/primary.log for checks already executed

PASS criteria:

* Live QA evidence is under the stable QA root.  
* The step records no implementation work, no PF document edit, no runtime vendor conformance, no public Reader change, no new HTTP home, no AI scope, and no epic closure action.

FAIL criteria:

* FAIL\_BEHAVIOR if Live QA evidence is outside the stable QA root or claims implementation, PF edits, runtime expansion, or closure action.  
* TOOLING\_BLOCKED if common tools are unavailable.  
* FAIL\_TOOLING if primary.log cannot be written under the QA root.

Blocked posture:

* If no prior check primary logs exist because execution has not started, classify this check as TOOLING\_BLOCKED until at least one prior check log exists.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

#### CHECK qa-16-close-out-deliverables: Close-out deliverables

Surface / D-goal mapping: D0 closeout assembly Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF27 — Canon Plan Templates; PF06 — Epic Process Guide; PF19 — Glow QA Guide

Goal: Produce the PF27-required closeout execution deliverables: QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary. This check does not perform PO closeout and does not claim epic closure.

Required dependencies:

* Common dependency baseline.  
* python standard library.

Preflight check:

* Command PF.

If missing, activation/install action:

* None for Python standard library.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* At least Step-0B has executed and has primary.log.  
* All executed checks have primary.log under audit/qa/hde-epic033/checks/.

Setup:

* The command creates audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/.  
* The command creates or refreshes audit/qa/hde-epic033/qa\_step\_logs\_manifest.json and its path proof.  
* The command creates or refreshes audit/qa/hde-epic033/00\_meta/discovery\_artifact.md and its path proof.  
* The command creates or refreshes audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md and its path proof.

Numbered PO actions:

1. Run Command 1 after all intended checks have run.  
2. Read audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.  
3. Confirm the manifest lists every executed check and that the summary includes coverage vs plan accounting.  
4. Do not treat this check as PO closeout.

Command 1: python \- \<\< 'PY'  
 from pathlib import Path  
 import datetime  
 import hashlib  
 import json  
 import os  
 import sys

root \= Path("audit/qa/hde-epic033")  
 check\_id \= "qa-16-close-out-deliverables"  
 check\_name \= "Close-out deliverables"  
 check\_root \= root / "checks" / check\_id  
 meta \= root / "00\_meta"  
 check\_root.mkdir(parents=True, exist\_ok=True)  
 meta.mkdir(parents=True, exist\_ok=True)

expected \= \[  
 "step-0b-doc-delta-capture",  
 "po-001",  
 "po-002",  
 "po-003",  
 "po-004",  
 "po-005",  
 "po-006",  
 "po-007",  
 "po-008",  
 "po-009",  
 "po-010",  
 "po-011",  
 "po-012",  
 "po-013",  
 "po-014",  
 \]  
 entries \= \[\]  
 coverage\_lines \= \[\]  
 status \= "PASS"  
 rc \= 0

for cid in expected:  
 log \= root / "checks" / cid / "primary.log"  
 proof\_log \= Path(str(log) \+ ".path\_proof.txt")  
 if not log.exists():  
 entries.append({"check\_id": cid, "status": "NOT RUN", "log\_path": str(log), "path\_proof\_path": str(proof\_log)})  
 coverage\_lines.append(f"\* {cid}: NOT RUN — {log}")  
 status \= "TOOLING\_BLOCKED"  
 rc \= 99  
 continue  
 if not proof\_log.exists():  
 entries.append({"check\_id": cid, "status": "MISSING\_PATH\_PROOF", "log\_path": str(log), "path\_proof\_path": str(proof\_log)})  
 coverage\_lines.append(f"\* {cid}: MISSING\_PATH\_PROOF — {proof\_log}")  
 status \= "TOOLING\_BLOCKED"  
 rc \= 99  
 continue  
 first \= log.read\_text(encoding="utf-8").splitlines()\[0\]  
 try:  
 header \= json.loads(first)  
 hstatus \= header.get("status", "UNKNOWN")  
 except Exception:  
 hstatus \= "UNREADABLE\_HEADER"  
 status \= "FAIL\_TOOLING"  
 rc \= 2  
 entries.append({"check\_id": cid, "status": hstatus, "log\_path": str(log), "path\_proof\_path": str(proof\_log)})  
 coverage\_lines.append(f"\* {cid}: {hstatus} — {log}")

manifest \= {  
 "schema\_version": "pf27.qa\_step\_logs\_manifest.v1",  
 "epic\_id": "HDE-EPIC033",  
 "entries": entries,  
 }  
 manifest\_path \= root / "qa\_step\_logs\_manifest.json"  
 manifest\_path.write\_text(json.dumps(manifest, sort\_keys=True, separators=(",", ":")) \+ "\\n", encoding="utf-8")

def sha(path: Path) \-\> str:  
 return hashlib.sha256(path.read\_bytes()).hexdigest()

def proof(path: Path) \-\> None:  
 stat \= path.stat()  
 mtime \= datetime.datetime.utcfromtimestamp(stat.st\_mtime).replace(microsecond=0).isoformat() \+ "Z"  
 produced \= datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"  
 proof\_path \= Path(str(path) \+ ".path\_proof.txt")  
 proof\_path.write\_text(  
 "\\n".join(\[  
 f"path: {path}",  
 f"size\_bytes: {stat.st\_size}",  
 f"sha256: {sha(path)}",  
 f"mtime\_utc: {mtime}",  
 f"produced\_at\_utc: {produced}",  
 "",  
 \]),  
 encoding="utf-8",  
 )

discovery\_path \= meta / "discovery\_artifact.md"  
 discovery\_path.write\_text(  
 "\\n".join(\[  
 "\# HDE-EPIC033 Live QA Discovery Artifact",  
 "",  
 "Discovery posture: audit-proven repo loci were used; no unproven repo helper, route, endpoint, command, or evidence root was invented.",  
 "Rails posture: SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev.",  
 "Out-of-scope boundaries: no runtime vendor conformance, no live vendor smoke, no public Reader change, no new service surface, and no AI scope.",  
 "",  
 \]),  
 encoding="utf-8",  
 )

summary\_path \= meta / "qa\_rca\_doc\_delta\_summary.md"  
 summary\_path.write\_text(  
 "\\n".join(\[  
 "\# HDE-EPIC033 QA RCA and Doc Delta Summary",  
 "",  
 "Live QA found:",  
 "Coverage vs plan:",  
 \*coverage\_lines,  
 "",  
 "Doc deltas:",  
 "Use audit/docdeltas/hde-epic033\_doc\_deltas.md and audit/qa/hde-epic033/00\_meta/doc\_deltas.md as the current doc-delta surfaces.",  
 "",  
 "Known deferrals:",  
 "Runtime request shaping, live vendor smoke, public Reader changes, new HTTP homes, and AI scope remain unclaimed by this Live QA run.",  
 "",  
 "Readiness and closeout recommendation:",  
 "No PO closeout action is claimed by this artifact. Any readiness statement must be made only after every required step is PASS or explicitly dispositioned, and after manifest/header/path-proof trust is reviewed.",  
 "",  
 "Drainage posture:",  
 "Documentation drainage itself is not a blocker. Repo-supported completion, canon-drain completion, and formal close-pack completion remain separate states.",  
 "",  
 \]),  
 encoding="utf-8",  
 )

for p in \[manifest\_path, discovery\_path, summary\_path\]:  
 proof(p)

body\_lines \= \[  
 f"manifest={manifest\_path}",  
 f"discovery\_artifact={discovery\_path}",  
 f"qa\_rca\_doc\_delta\_summary={summary\_path}",  
 f"derived\_status={status}",  
 \]  
 commands \= \["python closeout deliverables assembly embedded in runbook"\]  
 primary \= check\_root / "primary.log"  
 primary\_proof \= Path(str(primary) \+ ".path\_proof.txt")  
 header \= {  
 "schema\_version": "pf27.step\_log\_header.v1",  
 "timestamp\_utc": datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z",  
 "check\_id": check\_id,  
 "check\_name": check\_name,  
 "status": status,  
 "fail\_status": "" if status \== "PASS" else status,  
 "command": "; ".join(commands),  
 "command\_provenance": "Copy/paste from plan",  
 "exit\_code": rc,  
 "evidence\_artifacts": \[  
 str(primary),  
 str(primary\_proof),  
 str(manifest\_path),  
 str(Path(str(manifest\_path) \+ ".path\_proof.txt")),  
 str(discovery\_path),  
 str(Path(str(discovery\_path) \+ ".path\_proof.txt")),  
 str(summary\_path),  
 str(Path(str(summary\_path) \+ ".path\_proof.txt")),  
 \],  
 "captured\_env": {  
 "SAFE\_MODE": os.environ.get("SAFE\_MODE", ""),  
 "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK", ""),  
 "APP\_ENV": os.environ.get("APP\_ENV", ""),  
 "LC\_ALL": os.environ.get("LC\_ALL", ""),  
 "LANG": os.environ.get("LANG", ""),  
 "TZ": os.environ.get("TZ", ""),  
 },  
 "pf\_refs": \["PF27 — Canon Plan Templates", "PF06 — Epic Process Guide", "PF19 — Glow QA Guide"\],  
 "intended\_tokens": \[\],  
 "claimed\_tokens": \[\],  
 }  
 primary.write\_text(json.dumps(header, ensure\_ascii=False) \+ "\\n" \+ "\\n".join(body\_lines) \+ "\\n", encoding="utf-8")  
 proof(primary)  
 print(f"wrote {primary}")  
 print(f"wrote {primary\_proof}")  
 sys.exit(rc)  
 PY

What to look for:

* audit/qa/hde-epic033/qa\_step\_logs\_manifest.json exists.  
* audit/qa/hde-epic033/qa\_step\_logs\_manifest.json.path\_proof.txt exists.  
* audit/qa/hde-epic033/00\_meta/discovery\_artifact.md exists.  
* audit/qa/hde-epic033/00\_meta/discovery\_artifact.md.path\_proof.txt exists.  
* audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md exists.  
* audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt exists.  
* audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log exists.  
* audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path\_proof.txt exists.  
* primary.log status is PASS only if every expected check primary.log exists, every expected check primary.log.path\_proof.txt exists, and every expected check primary.log has a parseable PF27 header.

Required deliverables:

* audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log  
* audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path\_proof.txt  
* audit/qa/hde-epic033/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic033/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic033/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic033/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt

PASS criteria:

* The QA step-log manifest exists and lists every expected check with status and log\_path.  
* The manifest path proof exists and matches the manifest path.  
* Discovery artifact exists and records no invented loci.  
* QA RCA / Doc Delta summary exists and includes coverage vs plan accounting.  
* primary.log for this closeout assembly check has a PF27 header.

FAIL criteria:

* FAIL\_TOOLING if a primary log exists but has an unreadable header.  
* TOOLING\_BLOCKED if one or more expected check primary logs is NOT RUN.  
* FAIL\_BEHAVIOR if closeout deliverables claim PO closeout, PF edits, runtime vendor conformance, public Reader expansion, new HTTP home, or AI scope.

Blocked posture:

* If prior check logs are NOT RUN, rerun the missing planned checks before using the closeout summary as complete coverage evidence.

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

### Close-out deliverables

This runbook requires these closeout execution deliverables:

* Closeout assembly primary log: audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log  
* Closeout assembly primary log path proof: audit/qa/hde-epic033/checks/qa-16-close-out-deliverables/primary.log.path\_proof.txt  
* Discovery artifact: audit/qa/hde-epic033/00\_meta/discovery\_artifact.md  
* Discovery artifact path proof: audit/qa/hde-epic033/00\_meta/discovery\_artifact.md.path\_proof.txt  
* QA RCA / Doc Delta summary: audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* QA RCA / Doc Delta summary path proof: audit/qa/hde-epic033/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt  
* QA step-log manifest: audit/qa/hde-epic033/qa\_step\_logs\_manifest.json  
* QA step-log manifest path proof: audit/qa/hde-epic033/qa\_step\_logs\_manifest.json.path\_proof.txt

The QA step-log manifest must include, for every planned check, the check status, primary log path, and primary log path-proof path.

The QA RCA / Doc Delta summary must include:

* What Live QA found, or “no new deltas found”.  
* Coverage vs QA Plan accounting for Step-0B, PO-001 through PO-014, and closeout deliverables.  
* Evidence pointer for every COVERED step.  
* BLOCKED or UNEXECUTABLE posture for any step without evidence.  
* Any Moon Loop work, if used, with failure signature, remediation note, and rerun output.  
* Known open issues and deferred work with disposition.  
* Explicit separation of repo-supported completion, canon-drain completion, and formal close-pack completion.  
* Statement that documentation drainage itself is not a blocker.

This runbook does not itself create the formal close pack unless the PO separately assigns that action.

### Review guardrails

Hard blockers for plan execution:

* A required executable locus is absent and no QA-created alternative is explicitly defined under audit/qa/hde-epic033/.  
* A check requires SAFE\_MODE=0 or ALLOW\_NETWORK=1.  
* A check requires live vendor smoke, runtime request shaping, production service access, secrets, or public Reader behavior proof.  
* A required primary.log cannot be created under audit/qa/hde-epic033/checks/\<check\_id\>/.  
* A required primary.log.path\_proof.txt cannot be created beside its primary.log.  
* A PASS primary.log lacks a PF27 header, captured\_env, evidence\_artifacts, intended\_tokens, or claimed\_tokens.  
* A PASS primary.log omits its own primary.log from evidence\_artifacts.  
* A PASS primary.log omits its own primary.log.path\_proof.txt from evidence\_artifacts.  
* claimed\_tokens contains any token not actually proven by that check.  
* A non-PASS primary.log claims tokens.  
* Documentation drainage is treated as a prerequisite for step verdict, readiness, or closeout recommendation.  
* HDE-FERM007 or HDE-FERM008 runtime work is claimed as proven by this plan.  
* A rendered escape artifact is treated as a defect without raw source proof.

Classification rules:

* Use PASS only when all PASS criteria for the step are met and primary.log records exit\_code 0\.  
* Use FAIL\_BEHAVIOR when the current artifact or runtime behavior contradicts the step’s proof obligation after tooling is available.  
* Use FAIL\_TOOLING when execution or evidence capture is contaminated or invalid after the command starts.  
* Use TOOLING\_BLOCKED when a dependency, command, script, file, prerequisite, or safe input is unavailable and the step cannot proceed without guessing.

ASK OK?  
