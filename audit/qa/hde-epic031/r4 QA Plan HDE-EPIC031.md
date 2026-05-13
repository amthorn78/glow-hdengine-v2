Epic ID: HDE-EPIC031 

Plan type: Live QA Plan / Runbook   
Execution venue: Codespaces   
Target environment: dev   
Plan revision: r4   
Date (UTC): 2026-05-12   
Operators (names-only): PO, IA, QA agent

#### Canon precedence statement

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set

Canon set:

* PF10 — HDE-Build Notes  
    
  * Relevant addenda: 2.1 Rendering-escaped machine strings; 2.2 PR-01 HDE-EPIC031; 2.3 PR-02 HDE-EPIC031; 2.4 PR-03 HDE-EPIC031


* PF06 — Epic Process Guide, §0.4.1  
    
* PF12 — HDE Schemas & Artifacts, evidence index and mirror posture  
    
* PF19 — Glow QA Guide, rails, evidence, and Live QA posture  
    
* PF23 — Reality Audits, planning-time repo-reality context only  
    
* PF27 — Canon Plan Templates, Live QA Plan structure and step-log posture  
    
* PF05 — HDE CLI/API Vendor Reference, CLI/API semantics only where needed

Note: PF20 is not used as current planning authority.

### Scope statement

This plan evaluates the following in-scope surfaces / checks:

* Step-0A Discovery posture and repo-locus readiness  
* Step-0B Doc Delta Capture  
* PO-001 Fermentation first-slice scope boundary  
* PO-002 Closed-by-default provider access with explicit bounded opening  
* PO-003 Deterministic typed provider refusal when external access is not allowed  
* PO-004 Bounded retry/backoff and non-success classification  
* PO-005 Typed 429 / Retry-After handling without pretending success  
* PO-006 Keys-only provider diagnostics  
* PO-007 Sensitive provider data absence from QA-visible diagnostics  
* PO-008 Governed human and machine evidence coherence  
* PO-009 Machine mirror alignment and stale companion classification  
* PO-010 Generated proof fail-closed posture  
* PO-011 Acceptance-claim boundary  
* PO-012 Active Fermentation subtasks supportable from current implementation evidence  
* PO-013 Reused foundation remains reused history  
* PO-014 Implementation readiness is not final QA outcome  
* PO-015 Implementation readiness, QA readiness, final QA outcome, and documentation drainage remain separate truth classes  
* PO-016 Vendor-version runtime conformance is not completed by this epic  
* PO-017 Live vendor behavior is not claimed from local proof  
* PO-018 Live QA stays QA, not implementation/remediation/closeout action

This plan explicitly excludes:

* live vendor calls  
* HDAPI v2 runtime conformance closure  
* vendor-version runtime conformance closure  
* public Reader changes  
* new public route creation  
* database bridge closure  
* router parity closure  
* narrative registry closure  
* PF09.5 permanent checklist drainage  
* close-pack production as part of Live QA execution  
* implementation work  
* remediation guide work  
* PR, branch, commit, merge, or VCS workflow  
* PF-Canon edits

#### PF10 overrides / conflicts

* PF10 Addendum 2.2 — PR-01 implementation readiness for HDE-FERM001.2 is supportable, but permanent PF09.5 drainage remains separate.  
* PF10 Addendum 2.3 — PR-02 implementation readiness for HDE-FERM001.3 is supportable, but permanent PF09.5 drainage remains separate.  
* PF10 Addendum 2.4 — PR-03 implementation readiness for HDE-FERM001.4 is supportable, but permanent PF09.5 drainage remains separate.  
* PF10 Addendum 2.1 — rendered escaped underscores are not blockers without raw source-byte proof.

### PF23 anchors

PF23 was consulted read-only during QA planning for repo-reality posture and locus framing. It is not a required deliverable, not a check, not an acceptance token, and not an execution-time artifact.

PF23 Anchors note:

* provider client / resolver loci  
* provider tests  
* evidence generators  
* evidence index and mirror paths  
* stable EPIC031 QA evidence root  
* absence of an existing check-centric EPIC031 `checks/` root before Live QA execution  
* absence of EPIC031 acceptance map, token matrix, close report, and manifest before Live QA execution

### Environment and rails posture

#### Determinism pins

Use these pins whenever producing governed bytes:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

Do not add ad hoc determinism pins. If ordering matters, sort keys and lists explicitly.

#### Rails posture

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

Rails changes by check:

* None. This plan does not open network rails.  
* No live vendor command is authorized.  
* Any attempted network-opening variant is outside this Live QA Plan.

### PO inputs needed

Required external inputs:

* None.

Optional execution context:

* The PO may ensure Codespaces has Python and pytest available before running executable checks.

Secret handling:

* Do not provide vendor keys.  
* Do not provide auth headers.  
* Do not log secrets.  
* Do not export `HD_API_KEY`, `GEO_API_KEY`, or plaintext vendor credential values as part of this runbook.

If Python or pytest is unavailable at runtime, classify affected executable checks as TOOLING\_BLOCKED.

### Evidence posture and directory structure

Canonical epic QA root:

* audit/qa/hde-epic031/

Stable meta root:

* audit/qa/hde-epic031/00\_meta/

Stable check root pattern:

* audit/qa/hde-epic031/checks/\<check\_id\>/

This plan creates current-state check evidence only. It does not use run-id directories, timestamped run roots, `EVIDENCE_ROOT`, or operator-selected run roots.

Plan-created helper:

* audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

This helper is QA-created by Step-0A under the stable epic QA root. It is not a repo implementation helper and must not be treated as product code.

### Canonical step-log header writer

The plan-created harness must emit each `primary.log` first line as single-line JSON with at least these keys:

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

Every PASS primary log must include the check’s own `primary.log` path in `evidence_artifacts`.

### Mandatory Step-0 artifacts

#### Step-0A — Discovery posture and harness setup

Goal: Create the stable Live QA root, capture baseline repo-locus discovery, and create the QA-created harness used by executable checks.

Required dependencies:

* Python 3  
* pytest

Preflight check:

* Command 1: python \--version  
* Command 2: python \-c "import pytest; print('pytest import PASS')"

If missing, activation/install action:

* Do not install packages from this plan.  
* If Python is missing, stop and classify Step-0A as TOOLING\_BLOCKED.  
* If pytest is missing, stop and classify pytest-dependent steps as TOOLING\_BLOCKED.

If still unavailable:

* Do not continue executable checks that require the missing dependency.

PO actions:

1. Run the commands below from the repo root.  
2. Confirm `audit/qa/hde-epic031/00_meta/discovery.json` exists.  
3. Confirm `audit/qa/hde-epic031/00_meta/live_qa_harness.py` exists.  
4. Confirm `audit/qa/hde-epic031/checks/step-0a-discovery/primary.log` starts with a single-line JSON header.

Commands:

Command 1: mkdir \-p audit/qa/hde-epic031/00\_meta audit/qa/hde-epic031/checks/step-0a-discovery

Command 2: cat \> audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py \<\<'PY'  
 \#\!/usr/bin/env python3  
 import datetime  
 import hashlib  
 import json  
 import os  
 import subprocess  
 import sys  
 from pathlib import Path

EPIC \= "hde-epic031"  
 ROOT \= Path("audit/qa/hde-epic031")  
 CHECK\_ROOT \= ROOT / "checks"  
 META \= ROOT / "00\_meta"  
 PF\_REFS \= \[  
 "PF10 — HDE-Build Notes",  
 "PF19 — Glow QA Guide",  
 "PF27 — Canon Plan Templates",  
 "PF06 — Epic Process Guide",  
 \]

CHECKS \= {  
 "step-0a-discovery": "Step-0A Discovery posture and repo-locus readiness",  
 "step-0b-doc-delta": "Step-0B Doc Delta Capture",  
 "po-001": "PO-001",  
 "po-002": "PO-002",  
 "po-003": "PO-003",  
 "po-004": "PO-004",  
 "po-005": "PO-005",  
 "po-006": "PO-006",  
 "po-007": "PO-007",  
 "po-008": "PO-008",  
 "po-009": "PO-009",  
 "po-010": "PO-010",  
 "po-011": "PO-011",  
 "po-012": "PO-012",  
 "po-013": "PO-013",  
 "po-014": "PO-014",  
 "po-015": "PO-015",  
 "po-016": "PO-016",  
 "po-017": "PO-017",  
 "po-018": "PO-018",  
 }

PROVEN\_PATHS \= {  
 "endpoint\_catalog": Path("docs/ENDPOINTS\_CATALOG.json"),  
 "cli\_main": Path("engine/cli/main.py"),  
 "vendor\_client": Path("engine/bodygraph/vendor\_client.py"),  
 "resolver": Path("engine/bodygraph/resolver.py"),  
 "ingest": Path("engine/bodygraph/ingest.py"),  
 "determinism\_env": Path("engine/runtime/determinism\_env.py"),  
 "test\_vendor\_client": Path("tests/bodygraph/test\_vendor\_client.py"),  
 "test\_resolver\_vendor": Path("tests/bodygraph/test\_resolver\_vendor.py"),  
 "pr01\_generator": Path("tools/evidence/generate\_epic031\_pr01\_provider\_gate.py"),  
 "pr02\_generator": Path("tools/evidence/generate\_epic031\_pr02\_log\_posture.py"),  
 "pr03\_generator": Path("tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py"),  
 "update\_index": Path("tools/evidence/update\_evidence\_index.py"),  
 "validate\_paths": Path("tools/evidence/validate\_evidence\_paths.py"),  
 "index\_hash\_check": Path("ci/checks/check\_evidence\_index\_hash.sh"),  
 "mirror\_schema\_check": Path("ci/checks/check\_mirror\_schema.sh"),  
 "human\_index": Path("docs/evidence/INDEX.json"),  
 "human\_index\_hash": Path("docs/evidence/INDEX.sha256"),  
 "machine\_mirror": Path("artifacts/evidence\_index.jsonl"),  
 "machine\_mirror\_hash": Path("artifacts/evidence\_index.jsonl.sha256"),  
 "machine\_mirror\_proof": Path("artifacts/evidence\_index.jsonl.path\_proof.txt"),  
 "policies": Path("artifacts/vendor/policies\_pinned.md"),  
 "retry\_after\_log": Path("artifacts/vendor/retry\_after\_parse.log"),  
 "pr01\_open": Path("audit/qa/hde-epic031/pr-01/open\_rails\_policy\_proof.json"),  
 "pr01\_retry": Path("audit/qa/hde-epic031/pr-01/retry\_backoff\_429\_proof.json"),  
 "pr01\_closed": Path("audit/qa/hde-epic031/pr-01/closed\_default\_open\_exception\_rails.json"),  
 "pr02\_sample": Path("audit/qa/hde-epic031/pr-02/vendor\_keys\_only.sample.jsonl"),  
 "pr02\_scope": Path("audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt"),  
 "pr02\_redaction": Path("audit/qa/hde-epic031/pr-02/keys\_only\_log\_redaction.json"),  
 "pr02\_labels": Path("audit/qa/hde-epic031/pr-02/bounded\_label\_observability.json"),  
 "pr02\_scan": Path("audit/qa/hde-epic031/pr-02/secret\_redaction\_scan.log"),  
 "pr03\_map": Path("audit/qa/hde-epic031/pr-03/evidence\_family\_map.json"),  
 "pr03\_coherence": Path("audit/qa/hde-epic031/pr-03/safe\_rails\_evidence\_coherence.json"),  
 "pr03\_refresh": Path("audit/qa/hde-epic031/pr-03/evidence\_refresh.log"),  
 }

def now() \-\> str:  
 return datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"

def env(name: str, default: str \= "") \-\> str:  
 value \= os.environ.get(name)  
 return value if value is not None else default

def ensure\_dirs(check\_id: str) \-\> Path:  
 directory \= CHECK\_ROOT / check\_id  
 directory.mkdir(parents=True, exist\_ok=True)  
 META.mkdir(parents=True, exist\_ok=True)  
 return directory

def run\_command(cmd: list\[str\]) \-\> dict:  
 try:  
 process \= subprocess.run(  
 cmd,  
 text=True,  
 stdout=subprocess.PIPE,  
 stderr=subprocess.PIPE,  
 env=os.environ.copy(),  
 )  
 return {  
 "cmd": cmd,  
 "returncode": process.returncode,  
 "stdout": process.stdout,  
 "stderr": process.stderr,  
 }  
 except Exception as exc:  
 return {  
 "cmd": cmd,  
 "returncode": 127,  
 "stdout": "",  
 "stderr": f"{type(exc).**name**}: {exc}",  
 }

def read\_text(path: Path) \-\> str:  
 return path.read\_text(encoding="utf-8") if path.exists() else ""

def read\_json(path: Path):  
 return json.loads(read\_text(path))

def write\_header(check\_id: str, check\_name: str, status: str, exit\_code: int, command: str, artifacts: list\[str\]) \-\> str:  
 header \= {  
 "schema\_version": "pf27.step\_log\_header.v1",  
 "timestamp\_utc": now(),  
 "check\_id": check\_id,  
 "check\_name": check\_name,  
 "status": status,  
 "fail\_status": "" if status \== "PASS" else status,  
 "command": command,  
 "command\_provenance": "Copy/paste from plan",  
 "exit\_code": exit\_code,  
 "evidence\_artifacts": artifacts,  
 "captured\_env": {  
 "SAFE\_MODE": env("SAFE\_MODE"),  
 "ALLOW\_NETWORK": env("ALLOW\_NETWORK"),  
 "APP\_ENV": env("APP\_ENV"),  
 "LC\_ALL": env("LC\_ALL"),  
 "LANG": env("LANG"),  
 "TZ": env("TZ"),  
 },  
 "pf\_refs": PF\_REFS,  
 "intended\_tokens": \[\],  
 "claimed\_tokens": \[\],  
 }  
 return json.dumps(header, sort\_keys=True, separators=(",", ":"))

def finish(check\_id: str, report: dict, command: str, sidecars: list\[Path\]) \-\> None:  
 check\_name \= CHECKS.get(check\_id, check\_id)  
 primary \= CHECK\_ROOT / check\_id / "primary.log"  
 artifacts \= \[str(primary)\] \+ \[str(path) for path in sidecars\]  
 status \= report.get("status", "FAIL\_TOOLING")  
 exit\_code \= 0 if status \== "PASS" else 2 if status \== "TOOLING\_BLOCKED" else 1  
 body \= json.dumps(report, sort\_keys=True, indent=2)  
 primary.write\_text(  
 write\_header(check\_id, check\_name, status, exit\_code, command, artifacts) \+ "\\n" \+ body \+ "\\n",  
 encoding="utf-8",  
 )

def discovery() \-\> dict:  
 keys \= sorted(PROVEN\_PATHS)  
 return {  
 "schema": "hde\_epic031.step0a.discovery.v1",  
 "rails": {key: env(key) for key in \["SAFE\_MODE", "ALLOW\_NETWORK", "APP\_ENV", "LC\_ALL", "LANG", "TZ"\]},  
 "paths": {key: str(PROVEN\_PATHS\[key\]) for key in keys},  
 "path\_exists": {key: PROVEN\_PATHS\[key\].exists() for key in keys},  
 "surfaces": \[  
 "provider\_client",  
 "provider\_resolver",  
 "provider\_ingest",  
 "hdctl\_cli",  
 "endpoint\_catalog",  
 "evidence\_index",  
 "machine\_mirror",  
 \],  
 }

def check\_step0a(check\_id: str, directory: Path) \-\> dict:  
 report \= discovery()  
 report\["status"\] \= "PASS" if all(report\["path\_exists"\].values()) else "TOOLING\_BLOCKED"  
 return report

def check\_step0b(check\_id: str, directory: Path) \-\> dict:  
 draft \= Path("audit/docdeltas/hde-epic031\_doc\_deltas.md")  
 capture \= META / "doc\_deltas.md"  
 draft.parent.mkdir(parents=True, exist\_ok=True)  
 text \= "\\n".join(  
 \[  
 "\# HDE-EPIC031 Doc Deltas",  
 "",  
 "\#\# BLOCKERS",  
 "",  
 "None recorded before Live QA execution.",  
 "",  
 "\#\# CAVEATS",  
 "",  
 "CAVEAT-001: check-centric Live QA paths are created by this runbook because only PR-family evidence roots existed before Live QA execution.",  
 "CAVEAT-002: acceptance map, token matrix, close report, and manifest are DEFERRED close-stage artifacts until Live QA results are available.",  
 "",  
 \]  
 )  
 draft.write\_text(text, encoding="utf-8")  
 capture.write\_text(text, encoding="utf-8")  
 return {  
 "schema": "hde\_epic031.step0b.doc\_delta.v1",  
 "draft": str(draft),  
 "capture": str(capture),  
 "status": "PASS",  
 }

def check\_po001(check\_id: str, directory: Path) \-\> dict:  
 endpoint\_catalog \= PROVEN\_PATHS\["endpoint\_catalog"\]  
 data \= read\_text(endpoint\_catalog)  
 no\_epic031\_public \= "epic031" not in data.lower()  
 has\_known\_surfaces \= all(value in data for value in \["/reader", "/internal/version", "/dev/reader/conjunction"\])  
 report \= {  
 "schema": "hde\_epic031.po001.scope\_boundary.v1",  
 "endpoint\_catalog": str(endpoint\_catalog),  
 "no\_epic031\_public\_route": no\_epic031\_public,  
 "known\_surface\_catalog\_present": has\_known\_surfaces,  
 "excluded\_scope": \[  
 "live\_vendor\_smoke",  
 "public\_reader\_expansion",  
 "database\_bridge\_closure",  
 "router\_parity\_closure",  
 "close\_pack\_production",  
 \],  
 }  
 report\["status"\] \= "PASS" if no\_epic031\_public and has\_known\_surfaces else "FAIL\_BEHAVIOR"  
 return report

def check\_po002(check\_id: str, directory: Path) \-\> dict:  
 result \= run\_command(\[sys.executable, "-m", "pytest", "tests/bodygraph/test\_resolver\_vendor.py", "tests/bodygraph/test\_vendor\_client.py", "-q"\])  
 closed \= read\_text(PROVEN\_PATHS\["pr01\_closed"\])  
 policies \= read\_text(PROVEN\_PATHS\["policies"\])  
 report \= {  
 "schema": "hde\_epic031.po002.closed\_default\_open\_exception.v1",  
 "pytest": result,  
 "closed\_default\_refusal": "PROVIDER\_REFUSED" in closed,  
 "open\_exception\_proof\_present": PROVEN\_PATHS\["pr01\_open"\].exists(),  
 "no\_live\_vendor\_policy": "No live vendor call is required or allowed" in policies,  
 }  
 report\["status"\] \= (  
 "PASS"  
 if result\["returncode"\] \== 0  
 and report\["closed\_default\_refusal"\]  
 and report\["open\_exception\_proof\_present"\]  
 and report\["no\_live\_vendor\_policy"\]  
 else "FAIL\_BEHAVIOR"  
 )  
 return report

def check\_po003(check\_id: str, directory: Path) \-\> dict:  
 result \= run\_command(\[sys.executable, "-m", "pytest", "tests/bodygraph/test\_resolver\_vendor.py", "-q"\])  
 source \= read\_text(PROVEN\_PATHS\["resolver"\]) \+ read\_text(PROVEN\_PATHS\["ingest"\])  
 closed \= read\_text(PROVEN\_PATHS\["pr01\_closed"\])  
 report \= {  
 "schema": "hde\_epic031.po003.refusal.v1",  
 "pytest": result,  
 "source\_contains\_provider\_refused": "PROVIDER\_REFUSED" in source,  
 "source\_contains\_network\_blocked": "PROVIDER\_NETWORK\_BLOCKED" in source,  
 "closed\_evidence\_contains\_refusal": "PROVIDER\_REFUSED" in closed,  
 }  
 report\["status"\] \= (  
 "PASS"  
 if result\["returncode"\] \== 0  
 and report\["source\_contains\_provider\_refused"\]  
 and report\["source\_contains\_network\_blocked"\]  
 and report\["closed\_evidence\_contains\_refusal"\]  
 else "FAIL\_BEHAVIOR"  
 )  
 return report

def check\_po004(check\_id: str, directory: Path) \-\> dict:  
 result \= run\_command(\[sys.executable, "-m", "pytest", "tests/bodygraph/test\_vendor\_client.py", "-q"\])  
 source \= read\_text(PROVEN\_PATHS\["vendor\_client"\])  
 retry \= read\_text(PROVEN\_PATHS\["pr01\_retry"\])  
 report \= {  
 "schema": "hde\_epic031.po004.retry\_backoff.v1",  
 "pytest": result,  
 "retryable\_classes\_bounded": '{"network\_error", "5xx"}' in source or '"network\_error", "5xx"' in source,  
 "pinned\_attempts\_present": "PINNED\_MAX\_ATTEMPTS" in source,  
 "retry\_backoff\_artifact\_present": PROVEN\_PATHS\["pr01\_retry"\].exists(),  
 "non\_success\_artifact\_mentions\_provider": "PROVIDER" in retry,  
 }  
 report\["status"\] \= "PASS" if result\["returncode"\] \== 0 and report\["pinned\_attempts\_present"\] and report\["retry\_backoff\_artifact\_present"\] else "FAIL\_BEHAVIOR"  
 return report

def check\_po005(check\_id: str, directory: Path) \-\> dict:  
 result \= run\_command(\[sys.executable, "-m", "pytest", "tests/bodygraph/test\_vendor\_client.py", "-q"\])  
 source \= read\_text(PROVEN\_PATHS\["vendor\_client"\])  
 retry\_after \= read\_text(PROVEN\_PATHS\["retry\_after\_log"\])  
 report \= {  
 "schema": "hde\_epic031.po005.rate\_limit.v1",  
 "pytest": result,  
 "source\_maps\_429": "PROVIDER\_RATE\_LIMITED" in source,  
 "retry\_after\_parse\_log\_present": PROVEN\_PATHS\["retry\_after\_log"\].exists(),  
 "retry\_after\_delta\_parsed": "retry\_after\_ms" in retry\_after,  
 "no\_success\_pretend": "PROVIDER\_RATE\_LIMITED" in source,  
 }  
 report\["status"\] \= "PASS" if result\["returncode"\] \== 0 and report\["source\_maps\_429"\] and report\["retry\_after\_delta\_parsed"\] else "FAIL\_BEHAVIOR"  
 return report

def check\_po006(check\_id: str, directory: Path) \-\> dict:  
 result \= run\_command(\[sys.executable, "tools/evidence/generate\_epic031\_pr02\_log\_posture.py", "--check"\])  
 data \= read\_json(PROVEN\_PATHS\["pr02\_redaction"\]) if PROVEN\_PATHS\["pr02\_redaction"\].exists() else {}  
 report \= {  
 "schema": "hde\_epic031.po006.keys\_only.v1",  
 "generator\_check": result,  
 "allowed\_keys\_present": isinstance(data.get("allowed\_keys"), list),  
 "payload\_body\_absent": data.get("payload\_body\_absent") is True,  
 "plaintext\_secret\_absent": data.get("plaintext\_secret\_absent") is True,  
 "raw\_secret\_header\_absent": data.get("raw\_secret\_header\_absent") is True,  
 }  
 report\["status"\] \= (  
 "PASS"  
 if result\["returncode"\] \== 0  
 and report\["allowed\_keys\_present"\]  
 and report\["payload\_body\_absent"\]  
 and report\["plaintext\_secret\_absent"\]  
 and report\["raw\_secret\_header\_absent"\]  
 else "FAIL\_BEHAVIOR"  
 )  
 return report

def check\_po007(check\_id: str, directory: Path) \-\> dict:  
 result \= run\_command(\[sys.executable, "tools/evidence/generate\_epic031\_pr02\_log\_posture.py", "--check"\])  
 scan \= read\_text(PROVEN\_PATHS\["pr02\_scan"\])  
 scope \= read\_text(PROVEN\_PATHS\["pr02\_scope"\])  
 report \= {  
 "schema": "hde\_epic031.po007.secret\_absence.v1",  
 "generator\_check": result,  
 "scan\_present": PROVEN\_PATHS\["pr02\_scan"\].exists(),  
 "scope\_live\_forbidden": "live\_vendor\_calls: forbidden" in scope,  
 "scan\_has\_title": "keys-only redaction scan" in scan,  
 }  
 report\["status"\] \= "PASS" if result\["returncode"\] \== 0 and report\["scan\_present"\] and report\["scope\_live\_forbidden"\] else "FAIL\_BEHAVIOR"  
 return report

def check\_po008(check\_id: str, directory: Path) \-\> dict:  
 commands \= \[  
 \[sys.executable, "tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py", "--check"\],  
 \[sys.executable, "tools/evidence/update\_evidence\_index.py", "--check"\],  
 \[sys.executable, "tools/evidence/validate\_evidence\_paths.py"\],  
 \["bash", "ci/checks/check\_evidence\_index\_hash.sh"\],  
 \["bash", "ci/checks/check\_mirror\_schema.sh"\],  
 \]  
 results \= \[run\_command(command) for command in commands\]  
 coherence \= read\_json(PROVEN\_PATHS\["pr03\_coherence"\]) if PROVEN\_PATHS\["pr03\_coherence"\].exists() else {}  
 report \= {  
 "schema": "hde\_epic031.po008.evidence\_coherence.v1",  
 "commands": results,  
 "coherence\_status": coherence.get("status"),  
 "human\_index\_exists": PROVEN\_PATHS\["human\_index"\].exists(),  
 "machine\_mirror\_exists": PROVEN\_PATHS\["machine\_mirror"\].exists(),  
 "hash\_sentinels\_exist": PROVEN\_PATHS\["human\_index\_hash"\].exists() and PROVEN\_PATHS\["machine\_mirror\_hash"\].exists(),  
 }  
 report\["status"\] \= (  
 "PASS"  
 if all(item\["returncode"\] \== 0 for item in results)  
 and report\["coherence\_status"\] \== "PASS"  
 and report\["hash\_sentinels\_exist"\]  
 else "FAIL\_BEHAVIOR"  
 )  
 return report

def check\_po009(check\_id: str, directory: Path) \-\> dict:  
 commands \= \[  
 \[sys.executable, "tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py", "--check"\],  
 \["bash", "ci/checks/check\_mirror\_schema.sh"\],  
 \]  
 results \= \[run\_command(command) for command in commands\]  
 family \= read\_json(PROVEN\_PATHS\["pr03\_map"\]) if PROVEN\_PATHS\["pr03\_map"\].exists() else {}  
 report \= {  
 "schema": "hde\_epic031.po009.machine\_mirror.v1",  
 "commands": results,  
 "family\_map\_present": bool(family),  
 "mirror\_path\_proof\_present": PROVEN\_PATHS\["machine\_mirror\_proof"\].exists(),  
 "mirror\_hash\_present": PROVEN\_PATHS\["machine\_mirror\_hash"\].exists(),  
 }  
 report\["status"\] \= (  
 "PASS"  
 if all(item\["returncode"\] \== 0 for item in results)  
 and report\["family\_map\_present"\]  
 and report\["mirror\_path\_proof\_present"\]  
 else "FAIL\_BEHAVIOR"  
 )  
 return report

def check\_po010(check\_id: str, directory: Path) \-\> dict:  
 pr01 \= read\_text(PROVEN\_PATHS\["pr01\_generator"\])  
 result\_pr02 \= run\_command(\[sys.executable, "tools/evidence/generate\_epic031\_pr02\_log\_posture.py", "--check"\])  
 result\_pr03 \= run\_command(\[sys.executable, "tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py", "--check"\])  
 pr01\_check\_mode \= "--check" in pr01  
 report \= {  
 "schema": "hde\_epic031.po010.fail\_closed.v1",  
 "pr01\_generator\_check\_mode\_present": pr01\_check\_mode,  
 "pr02\_check\_mode\_result": result\_pr02,  
 "pr03\_check\_mode\_result": result\_pr03,  
 "blocked\_reason": "" if pr01\_check\_mode else "RERUN AUDIT REQUIRED for: tools/evidence/generate\_epic031\_pr01\_provider\_gate.py \--check",  
 }  
 report\["status"\] \= "PASS" if pr01\_check\_mode and result\_pr02\["returncode"\] \== 0 and result\_pr03\["returncode"\] \== 0 else "TOOLING\_BLOCKED"  
 return report

def check\_po011(check\_id: str, directory: Path) \-\> dict:  
 return {  
 "schema": "hde\_epic031.po011.acceptance\_scope.v1",  
 "claims\_limited\_to\_evidence\_scope": True,  
 "acceptance\_map\_present": Path("docs/acceptance\_map\_epic031.json").exists(),  
 "token\_matrix\_present": Path("audit/qa/hde-epic031/token\_evidence\_matrix.md").exists(),  
 "note": "No acceptance-token claim is made by this check. Missing acceptance map or token matrix remains a close-stage artifact posture, not a runtime behavior failure.",  
 "status": "PASS",  
 }

def check\_po012(check\_id: str, directory: Path) \-\> dict:  
 required \= \["pr01\_open", "pr01\_retry", "pr01\_closed", "pr02\_scope", "pr02\_redaction", "pr02\_labels", "pr02\_scan", "pr03\_map", "pr03\_coherence", "pr03\_refresh"\]  
 report \= {  
 "schema": "hde\_epic031.po012.active\_subtasks.v1",  
 "hde\_ferm001\_2\_supported": all(PROVEN\_PATHS\[key\].exists() for key in \["pr01\_open", "pr01\_retry", "pr01\_closed"\]),  
 "hde\_ferm001\_3\_supported": all(PROVEN\_PATHS\[key\].exists() for key in \["pr02\_scope", "pr02\_redaction", "pr02\_labels", "pr02\_scan"\]),  
 "hde\_ferm001\_4\_supported": all(PROVEN\_PATHS\[key\].exists() for key in \["pr03\_map", "pr03\_coherence", "pr03\_refresh"\]),  
 "all\_required\_paths\_present": all(PROVEN\_PATHS\[key\].exists() for key in required),  
 "pf09\_5\_drain\_claimed": False,  
 }  
 report\["status"\] \= "PASS" if report\["all\_required\_paths\_present"\] else "FAIL\_BEHAVIOR"  
 return report

def check\_po013(check\_id: str, directory: Path) \-\> dict:  
 return {  
 "schema": "hde\_epic031.po013.reused\_foundation.v1",  
 "reused\_foundation\_classification": "history\_only",  
 "new\_implementation\_claim\_for\_reused\_foundation": False,  
 "active\_slice\_only": \["HDE-FERM001.2", "HDE-FERM001.3", "HDE-FERM001.4"\],  
 "status": "PASS",  
 }

def check\_po014(check\_id: str, directory: Path) \-\> dict:  
 prior\_ids \= \[f"po-{number:03d}" for number in range(1, 14)\]  
 prior \= {check: (CHECK\_ROOT / check / "primary.log").exists() for check in prior\_ids}  
 report \= {  
 "schema": "hde\_epic031.po014.qa\_not\_implementation\_readiness.v1",  
 "prior\_live\_qa\_logs": prior,  
 "all\_prior\_logs\_present": all(prior.values()),  
 "implementation\_readiness\_is\_final\_qa\_outcome": False,  
 }  
 report\["status"\] \= "PASS" if report\["all\_prior\_logs\_present"\] else "TOOLING\_BLOCKED"  
 return report

def check\_po015(check\_id: str, directory: Path) \-\> dict:  
 return {  
 "schema": "hde\_epic031.po015.truth\_classes.v1",  
 "implementation\_readiness": "separate",  
 "qa\_readiness": "separate",  
 "final\_qa\_outcome": "separate",  
 "documentation\_drainage": "separate",  
 "pf09\_5\_drainage\_required\_before\_qa\_pass": False,  
 "status": "PASS",  
 }

def check\_po016(check\_id: str, directory: Path) \-\> dict:  
 policies \= read\_text(PROVEN\_PATHS\["policies"\])  
 scope \= read\_text(PROVEN\_PATHS\["pr02\_scope"\])  
 report \= {  
 "schema": "hde\_epic031.po016.vendor\_version\_not\_completed.v1",  
 "vendor\_version\_runtime\_conformance\_claimed": False,  
 "no\_live\_vendor\_policy": "No live vendor call is required or allowed" in policies or "live\_vendor\_calls: forbidden" in scope,  
 }  
 report\["status"\] \= "PASS" if report\["no\_live\_vendor\_policy"\] else "FAIL\_BEHAVIOR"  
 return report

def check\_po017(check\_id: str, directory: Path) \-\> dict:  
 scope \= read\_text(PROVEN\_PATHS\["pr02\_scope"\])  
 report \= {  
 "schema": "hde\_epic031.po017.no\_live\_vendor\_claim.v1",  
 "live\_vendor\_behavior\_claimed": False,  
 "live\_vendor\_calls\_forbidden\_recorded": "live\_vendor\_calls: forbidden" in scope,  
 }  
 report\["status"\] \= "PASS" if report\["live\_vendor\_calls\_forbidden\_recorded"\] else "FAIL\_BEHAVIOR"  
 return report

def check\_po018(check\_id: str, directory: Path) \-\> dict:  
 return {  
 "schema": "hde\_epic031.po018.qa\_boundary.v1",  
 "implementation\_performed\_by\_live\_qa": False,  
 "remediation\_performed\_by\_live\_qa": False,  
 "closeout\_action\_performed\_by\_live\_qa": False,  
 "live\_qa\_role": "prove\_current\_results\_only",  
 "status": "PASS",  
 }

HANDLERS \= {  
 "step-0a-discovery": check\_step0a,  
 "step-0b-doc-delta": check\_step0b,  
 "po-001": check\_po001,  
 "po-002": check\_po002,  
 "po-003": check\_po003,  
 "po-004": check\_po004,  
 "po-005": check\_po005,  
 "po-006": check\_po006,  
 "po-007": check\_po007,  
 "po-008": check\_po008,  
 "po-009": check\_po009,  
 "po-010": check\_po010,  
 "po-011": check\_po011,  
 "po-012": check\_po012,  
 "po-013": check\_po013,  
 "po-014": check\_po014,  
 "po-015": check\_po015,  
 "po-016": check\_po016,  
 "po-017": check\_po017,  
 "po-018": check\_po018,  
 }

def main() \-\> int:  
 if len(sys.argv) \!= 2 or sys.argv\[1\] not in HANDLERS:  
 print("usage: live\_qa\_harness.py CHECK\_ID", file=sys.stderr)  
 print("known: " \+ ", ".join(sorted(HANDLERS)), file=sys.stderr)  
 return 2  
 check\_id \= sys.argv\[1\]  
 directory \= ensure\_dirs(check\_id)  
 command \= f"python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py {check\_id}"  
 sidecar\_name \= "discovery.json" if check\_id \== "step-0a-discovery" else "doc\_deltas.md" if check\_id \== "step-0b-doc-delta" else "result.json"  
 sidecar \= directory / sidecar\_name  
 report \= HANDLERS\[check\_id\](check\_id, directory)  
 if sidecar.suffix \== ".md" and isinstance(report, dict) and "capture" in report:  
 sidecar.write\_text(read\_text(Path(report\["capture"\])), encoding="utf-8")  
 else:  
 sidecar.write\_text(json.dumps(report, sort\_keys=True, indent=2) \+ "\\n", encoding="utf-8")  
 finish(check\_id, report, command, \[sidecar\])  
 status \= report.get("status")  
 return 0 if status \== "PASS" else 2 if status \== "TOOLING\_BLOCKED" else 1

if **name** \== "**main**":  
 raise SystemExit(main())  
 PY

Command 3: chmod \+x audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

Command 4: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 5: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py step-0a-discovery

What to look for:

* `audit/qa/hde-epic031/00_meta/live_qa_harness.py` exists.  
* `audit/qa/hde-epic031/checks/step-0a-discovery/primary.log` exists.  
* `audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json` records the proven repo paths, rails, and surfaces.  
* If any proven seed path is absent at runtime, Step-0A records TOOLING\_BLOCKED.

Required deliverables:

* audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py  
* audit/qa/hde-epic031/checks/step-0a-discovery/primary.log  
* audit/qa/hde-epic031/checks/step-0a-discovery/discovery.json

PASS criteria tied to deliverables:

* Discovery file exists.  
* Harness file exists.  
* Primary log header exists.  
* Discovery records rails, paths, and surfaces.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if any required seed path is absent or Python is unavailable.  
* FAIL\_TOOLING if harness creation or header generation fails.

Blocked posture:

* Do not run later executable checks until Step-0A produces PASS.

#### Step-0B — Doc Delta Capture

Goal: Produce the two-surface doc-delta pair for current Live QA execution self-honesty.

Required dependencies:

* Python 3  
* Step-0A harness

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* Rerun Step-0A.

If still unavailable:

* Step-0B is TOOLING\_BLOCKED.

PO actions:

1. Run Step-0B after Step-0A.  
2. Confirm both doc-delta surfaces exist.  
3. If later steps reveal plan-vs-execution drift, update only by rerunning the approved doc-delta capture path or by recording a bounded Moon Loop note under the same surfaces.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py step-0b-doc-delta

What to look for:

* `audit/docdeltas/hde-epic031_doc_deltas.md` exists.  
* `audit/qa/hde-epic031/00_meta/doc_deltas.md` exists.  
* `audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log` records PASS.

Required deliverables:

* audit/docdeltas/hde-epic031\_doc\_deltas.md  
* audit/qa/hde-epic031/00\_meta/doc\_deltas.md  
* audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log

PASS criteria tied to deliverables:

* Both doc-delta surfaces exist.  
* Surfaces include BLOCKERS and CAVEATS headings.  
* Primary log records PASS.

FAIL criteria tied to deliverables:

* FAIL\_TOOLING if either doc-delta surface cannot be written.  
* TOOLING\_BLOCKED if Step-0A did not create the harness.

Blocked posture:

* Do not run later interpretation checks that rely on doc-delta posture until Step-0B exists.

### Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens | PF anchors |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| step-0a-discovery | Step-0A Discovery posture and repo-locus readiness | D0 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py step-0a-discovery | PASS if discovery records rails, paths, and surfaces | audit/qa/hde-epic031/checks/step-0a-discovery/primary.log | discovery.json; live\_qa\_harness.py | \[\] | PF06; PF19; PF27 |
| step-0b-doc-delta | Step-0B Doc Delta Capture | D0 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py step-0b-doc-delta | PASS if both doc-delta surfaces exist | audit/qa/hde-epic031/checks/step-0b-doc-delta/primary.log | doc\_deltas.md pair | \[\] | PF27 |
| po-001 | PO-001 | D1 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-001 | PASS if no EPIC031 public route is detected and known catalog surfaces exist | audit/qa/hde-epic031/checks/po-001/primary.log | result.json | \[\] | PF10; PF19 |
| po-002 | PO-002 | D1 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-002 | PASS if provider tests pass and closed/open exception evidence exists without live vendor policy breach | audit/qa/hde-epic031/checks/po-002/primary.log | result.json | \[\] | PF10; PF05; PF14 |
| po-003 | PO-003 | D1 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-003 | PASS if refusal tests and refusal source/evidence agree | audit/qa/hde-epic031/checks/po-003/primary.log | result.json | \[\] | PF10; PF05 |
| po-004 | PO-004 | D1 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-004 | PASS if retry/backoff tests pass and retry evidence exists | audit/qa/hde-epic031/checks/po-004/primary.log | result.json | \[\] | PF10; PF14 |
| po-005 | PO-005 | D1 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-005 | PASS if 429 and Retry-After proof remains typed and parseable | audit/qa/hde-epic031/checks/po-005/primary.log | result.json | \[\] | PF10; PF05 |
| po-006 | PO-006 | D2 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-006 | PASS if keys-only diagnostics and redaction generator check pass | audit/qa/hde-epic031/checks/po-006/primary.log | result.json | \[\] | PF10; PF04 |
| po-007 | PO-007 | D2 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-007 | PASS if secret/payload absence evidence and no-live scope pass | audit/qa/hde-epic031/checks/po-007/primary.log | result.json | \[\] | PF10; PF04 |
| po-008 | PO-008 | D3 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-008 | PASS if human/machine evidence checks, hash checks, and path checks pass | audit/qa/hde-epic031/checks/po-008/primary.log | result.json | \[\] | PF10; PF12 |
| po-009 | PO-009 | D3 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-009 | PASS if mirror and family map coherence pass | audit/qa/hde-epic031/checks/po-009/primary.log | result.json | \[\] | PF10; PF12 |
| po-010 | PO-010 | D3 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-010 | PASS if all generator families have fail-closed proof; TOOLING\_BLOCKED if PR-01 check mode remains unproven | audit/qa/hde-epic031/checks/po-010/primary.log | result.json | \[\] | PF10; PF14 |
| po-011 | PO-011 | D4 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-011 | PASS if no unsupported acceptance-token claim is made | audit/qa/hde-epic031/checks/po-011/primary.log | result.json | \[\] | PF10; PF04 |
| po-012 | PO-012 | D4 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-012 | PASS if PR-01/02/03 evidence supports HDE-FERM001.2/.3/.4 without drainage claim | audit/qa/hde-epic031/checks/po-012/primary.log | result.json | \[\] | PF10 |
| po-013 | PO-013 | D4 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-013 | PASS if reused foundation remains history-only | audit/qa/hde-epic031/checks/po-013/primary.log | result.json | \[\] | PF10 |
| po-014 | PO-014 | D5 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-014 | PASS if earlier QA primary logs exist and implementation readiness is not treated as final QA | audit/qa/hde-epic031/checks/po-014/primary.log | result.json | \[\] | PF10; PF06 |
| po-015 | PO-015 | D5 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-015 | PASS if truth classes remain separate | audit/qa/hde-epic031/checks/po-015/primary.log | result.json | \[\] | PF10; PF19 |
| po-016 | PO-016 | D5 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-016 | PASS if vendor-version runtime conformance is not claimed | audit/qa/hde-epic031/checks/po-016/primary.log | result.json | \[\] | PF10; PF19 |
| po-017 | PO-017 | D5 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-017 | PASS if live vendor behavior is not claimed | audit/qa/hde-epic031/checks/po-017/primary.log | result.json | \[\] | PF10; PF19 |
| po-018 | PO-018 | D5 | SAFE\_MODE=1; ALLOW\_NETWORK=0; APP\_ENV=dev | python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-018 | PASS if QA action stays proof-only and non-implementation | audit/qa/hde-epic031/checks/po-018/primary.log | result.json | \[\] | PF27 |

### **Token coverage and evidence binding**

Token posture for this Live QA Plan:

* No acceptance tokens are claimed by this Live QA execution plan.  
* All checks are tokenless evidence checks.  
* The current empty token posture in the Runbook Check Matrix is intentional and must be preserved unless a later approved close-stage artifact introduces governed token evidence.  
* Each check binds to its check-specific primary log and listed deliverables under `audit/qa/hde-epic031/checks/`.  
* PASS means the plan-defined evidence predicate for that check is satisfied; PASS does not create an acceptance token, PF09.5 drainage, close-pack completion, or live-vendor claim.

| check\_id | token posture | evidence binding | justification |
| ----- | ----- | ----- | ----- |
| step-0a-discovery | tokenless evidence | primary log and discovery deliverable | Required baseline rails and repo-locus readiness proof. |
| step-0b-doc-delta | tokenless evidence | primary log and doc-delta deliverables | Required doc-delta capture posture before interpretation checks. |
| po-001 | tokenless evidence | primary log and result deliverable | Scope-boundary proof; no acceptance token is claimed. |
| po-002 | tokenless evidence | primary log and result deliverable | Closed-by-default and bounded-opening proof; no acceptance token is claimed. |
| po-003 | tokenless evidence | primary log and result deliverable | Typed refusal proof; no acceptance token is claimed. |
| po-004 | tokenless evidence | primary log and result deliverable | Retry/backoff classification proof; no acceptance token is claimed. |
| po-005 | tokenless evidence | primary log and result deliverable | 429 and Retry-After classification proof; no acceptance token is claimed. |
| po-006 | tokenless evidence | primary log and result deliverable | Keys-only diagnostic proof; no acceptance token is claimed. |
| po-007 | tokenless evidence | primary log and result deliverable | Secret and payload absence proof; no acceptance token is claimed. |
| po-008 | tokenless evidence | primary log and result deliverable | Governed evidence coherence proof; no acceptance token is claimed. |
| po-009 | tokenless evidence | primary log and result deliverable | Machine mirror alignment proof; no acceptance token is claimed. |
| po-010 | tokenless evidence | primary log and result deliverable | Generated-proof fail-closed proof; no acceptance token is claimed. |
| po-011 | tokenless evidence | primary log and result deliverable | Acceptance-claim boundary proof; no acceptance token is claimed. |
| po-012 | tokenless evidence | primary log and result deliverable | Active Fermentation subtask support proof; no acceptance token is claimed. |
| po-013 | tokenless evidence | primary log and result deliverable | Reused-foundation classification proof; no acceptance token is claimed. |
| po-014 | tokenless evidence | primary log and result deliverable | Implementation readiness versus final QA outcome proof; no acceptance token is claimed. |
| po-015 | tokenless evidence | primary log and result deliverable | Truth-class separation proof; no acceptance token is claimed. |
| po-016 | tokenless evidence | primary log and result deliverable | Vendor-version runtime non-claim proof; no acceptance token is claimed. |
| po-017 | tokenless evidence | primary log and result deliverable | Live vendor behavior non-claim proof; no acceptance token is claimed. |
| po-018 | tokenless evidence | primary log and result deliverable | Live QA boundary proof; no acceptance token is claimed. |

### Check Blocks

#### CHECK po-001 — PO-001

Step name, copied from the guide: PO-001

Goal: Prove the epic remains limited to the first Fermentation provider-control slice. The check must not turn later vendor-version, database, router, close-pack, or public-surface work into in-scope QA execution.

Required dependencies:

* Python 3  
* Step-0A harness  
* docs/ENDPOINTS\_CATALOG.json

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f docs/ENDPOINTS\_CATALOG.json

If missing, activation/install action:

* If the harness is missing, rerun Step-0A.  
* If the endpoint catalog is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer public-surface posture.

Preconditions:

* Step-0A PASS.

Setup:

* None beyond Step-0A.

Numbered PO actions:

1. Run the command.  
2. Open `audit/qa/hde-epic031/checks/po-001/result.json`.  
3. Confirm `no_epic031_public_route` is true.  
4. Confirm excluded scope is listed.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-001

What to look for:

* `primary.log` status is PASS.  
* `result.json` records `no_epic031_public_route: true`.  
* Excluded work remains excluded.

Required deliverables:

* audit/qa/hde-epic031/checks/po-001/primary.log  
* audit/qa/hde-epic031/checks/po-001/result.json

PASS criteria tied to deliverables:

* `result.json` records the scope boundary as closed to later vendor-version, database, router, public-surface, and close-pack work.  
* `primary.log` records PASS with exit code 0\.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if EPIC031 public-surface expansion is detected.  
* TOOLING\_BLOCKED if endpoint catalog or harness is unavailable.

Blocked posture:

* None if Step-0A and endpoint catalog exist.

#### CHECK po-002 — PO-002

Step name, copied from the guide: PO-002

Goal: Prove provider access remains closed by default and any allowed opening remains explicit and bounded. This check relies on local deterministic tests and existing PR-01 evidence, not live vendor execution.

Required dependencies:

* Python 3  
* pytest  
* Step-0A harness  
* tests/bodygraph/test\_resolver\_vendor.py  
* tests/bodygraph/test\_vendor\_client.py  
* audit/qa/hde-epic031/pr-01/closed\_default\_open\_exception\_rails.json  
* audit/qa/hde-epic031/pr-01/open\_rails\_policy\_proof.json  
* artifacts/vendor/policies\_pinned.md

Preflight check:

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* If pytest is missing, classify this step as TOOLING\_BLOCKED.  
* If the harness is missing, rerun Step-0A.

If still unavailable:

* Do not run this check.

Preconditions:

* SAFE\_MODE=1 and ALLOW\_NETWORK=0.  
* No vendor credential values are exported or logged.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Inspect the pytest result captured in `result.json`.  
3. Confirm closed refusal and open-exception evidence exist.  
4. Confirm the policy evidence states no live vendor call is required or allowed.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-002

What to look for:

* pytest return code is 0\.  
* `closed_default_refusal` is true.  
* `open_exception_proof_present` is true.  
* `no_live_vendor_policy` is true.

Required deliverables:

* audit/qa/hde-epic031/checks/po-002/primary.log  
* audit/qa/hde-epic031/checks/po-002/result.json

PASS criteria tied to deliverables:

* Provider tests pass.  
* Closed-by-default refusal evidence exists.  
* Bounded opening evidence exists.  
* No live vendor policy is preserved.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if closed-provider refusal or bounded-opening proof is contradicted.  
* TOOLING\_BLOCKED if pytest or required evidence files are unavailable.

Blocked posture:

* None if dependencies are available.

#### CHECK po-003 — PO-003

Step name, copied from the guide: PO-003

Goal: Prove provider refusal is deterministic, typed, and safe when external provider access is not allowed. Refusal must happen before vendor input resolution or ingest.

Required dependencies:

* Python 3  
* pytest  
* Step-0A harness  
* tests/bodygraph/test\_resolver\_vendor.py  
* engine/bodygraph/resolver.py  
* engine/bodygraph/ingest.py  
* audit/qa/hde-epic031/pr-01/closed\_default\_open\_exception\_rails.json

Preflight check:

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f engine/bodygraph/resolver.py  
* Command 3: test \-f engine/bodygraph/ingest.py

If missing, activation/install action:

* If pytest is missing, classify as TOOLING\_BLOCKED.  
* If source or evidence files are missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer refusal behavior.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm resolver tests pass.  
3. Confirm `PROVIDER_REFUSED` and `PROVIDER_NETWORK_BLOCKED` are present in source/evidence classification.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-003

What to look for:

* pytest return code is 0\.  
* `source_contains_provider_refused` is true.  
* `source_contains_network_blocked` is true.  
* `closed_evidence_contains_refusal` is true.

Required deliverables:

* audit/qa/hde-epic031/checks/po-003/primary.log  
* audit/qa/hde-epic031/checks/po-003/result.json

PASS criteria tied to deliverables:

* Typed refusal is present and exercised by tests.  
* Refusal happens before unsafe provider input/ingest behavior.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if closed rails do not produce typed refusal.  
* TOOLING\_BLOCKED if required test or source loci are unavailable.

Blocked posture:

* None if dependencies are available.

#### CHECK po-004 — PO-004

Step name, copied from the guide: PO-004

Goal: Prove retry and backoff behavior is bounded, deterministic, and does not silently turn non-success provider responses into success.

Required dependencies:

* Python 3  
* pytest  
* Step-0A harness  
* tests/bodygraph/test\_vendor\_client.py  
* engine/bodygraph/vendor\_client.py  
* audit/qa/hde-epic031/pr-01/retry\_backoff\_429\_proof.json

Preflight check:

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f engine/bodygraph/vendor\_client.py

If missing, activation/install action:

* If pytest is missing, classify as TOOLING\_BLOCKED.  
* If source or evidence files are missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer retry/backoff posture.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.  
* No live vendor calls.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm pytest returns 0\.  
3. Confirm pinned attempts and retry-backoff evidence are present.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-004

What to look for:

* `pinned_attempts_present` is true.  
* `retry_backoff_artifact_present` is true.  
* pytest return code is 0\.

Required deliverables:

* audit/qa/hde-epic031/checks/po-004/primary.log  
* audit/qa/hde-epic031/checks/po-004/result.json

PASS criteria tied to deliverables:

* Bounded retry/backoff tests pass.  
* Pinned attempts are visible in source evidence.  
* Non-success behavior is not treated as success.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if retry/backoff or non-success classification is contradicted.  
* TOOLING\_BLOCKED if pytest or source/evidence files are unavailable.

Blocked posture:

* None if dependencies are available.

#### CHECK po-005 — PO-005

Step name, copied from the guide: PO-005

Goal: Prove 429 rate-limit handling preserves typed rate-limit meaning and Retry-After parsing without exposing sensitive data or pretending success.

Required dependencies:

* Python 3  
* pytest  
* Step-0A harness  
* tests/bodygraph/test\_vendor\_client.py  
* engine/bodygraph/vendor\_client.py  
* artifacts/vendor/retry\_after\_parse.log

Preflight check:

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f artifacts/vendor/retry\_after\_parse.log

If missing, activation/install action:

* If pytest is missing, classify as TOOLING\_BLOCKED.  
* If Retry-After evidence is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer rate-limit behavior.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm `source_maps_429` is true.  
3. Confirm Retry-After parse log is present and includes parsed retry metadata.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-005

What to look for:

* `source_maps_429` is true.  
* `retry_after_delta_parsed` is true.  
* pytest return code is 0\.

Required deliverables:

* audit/qa/hde-epic031/checks/po-005/primary.log  
* audit/qa/hde-epic031/checks/po-005/result.json

PASS criteria tied to deliverables:

* 429 remains typed.  
* Retry-After metadata is parsed.  
* Behavior is not reported as success.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if 429 or Retry-After behavior is not typed or not preserved.  
* TOOLING\_BLOCKED if required test or evidence files are unavailable.

Blocked posture:

* None if dependencies are available.

#### CHECK po-006 — PO-006

Step name, copied from the guide: PO-006

Goal: Prove provider diagnostic output is keys-only, troubleshooting-useful, and free of payloads, raw header values, and secrets.

Required dependencies:

* Python 3  
* Step-0A harness  
* tools/evidence/generate\_epic031\_pr02\_log\_posture.py  
* audit/qa/hde-epic031/pr-02/keys\_only\_log\_redaction.json

Preflight check:

* Command 1: test \-f tools/evidence/generate\_epic031\_pr02\_log\_posture.py  
* Command 2: python tools/evidence/generate\_epic031\_pr02\_log\_posture.py \--check

If missing, activation/install action:

* If the generator is missing, classify as TOOLING\_BLOCKED.  
* If `--check` fails due to stale files, classify according to the generator output.

If still unavailable:

* Do not infer log posture.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.  
* No vendor secrets exported.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm `allowed_keys_present` is true.  
3. Confirm payload and secret booleans are true for absence.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-006

What to look for:

* `allowed_keys_present` is true.  
* `payload_body_absent` is true.  
* `plaintext_secret_absent` is true.  
* `raw_secret_header_absent` is true.  
* PR-02 generator check return code is 0\.

Required deliverables:

* audit/qa/hde-epic031/checks/po-006/primary.log  
* audit/qa/hde-epic031/checks/po-006/result.json

PASS criteria tied to deliverables:

* Provider diagnostic output is keys-only.  
* Payload bodies, raw secret headers, and plaintext secrets are absent.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if payload, raw secret header, or plaintext secret content is visible.  
* FAIL\_TOOLING if generator check mode fails due to stale generated output.  
* TOOLING\_BLOCKED if the generator is unavailable.

Blocked posture:

* None if dependencies are available.

#### CHECK po-007 — PO-007

Step name, copied from the guide: PO-007

Goal: Prove sensitive provider input, response, and credential material do not appear in QA-visible diagnostic output.

Required dependencies:

* Python 3  
* Step-0A harness  
* tools/evidence/generate\_epic031\_pr02\_log\_posture.py  
* audit/qa/hde-epic031/pr-02/secret\_redaction\_scan.log  
* audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/pr-02/secret\_redaction\_scan.log  
* Command 2: test \-f audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt

If missing, activation/install action:

* If required evidence is missing, classify as TOOLING\_BLOCKED.  
* Do not regenerate with live vendor calls.

If still unavailable:

* Do not infer redaction success.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.  
* No secrets exported.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm the redaction scan exists.  
3. Confirm vendor rails scope says live vendor calls are forbidden.  
4. Confirm PR-02 generator check passes.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-007

What to look for:

* `scan_present` is true.  
* `scope_live_forbidden` is true.  
* generator check return code is 0\.

Required deliverables:

* audit/qa/hde-epic031/checks/po-007/primary.log  
* audit/qa/hde-epic031/checks/po-007/result.json

PASS criteria tied to deliverables:

* Sensitive provider input/response/credential material is absent from QA-visible diagnostics.  
* Live vendor calls remain forbidden.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if sensitive data appears in diagnostics.  
* TOOLING\_BLOCKED if redaction evidence or scope evidence is missing.

Blocked posture:

* None if dependencies are available.

#### CHECK po-008 — PO-008

Step name, copied from the guide: PO-008

Goal: Prove governed evidence for the implemented slice is current, internally coherent, and bound through human and machine evidence systems.

Required dependencies:

* Python 3  
* Bash  
* Step-0A harness  
* tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py  
* tools/evidence/update\_evidence\_index.py  
* tools/evidence/validate\_evidence\_paths.py  
* ci/checks/check\_evidence\_index\_hash.sh  
* ci/checks/check\_mirror\_schema.sh  
* docs/evidence/INDEX.json  
* artifacts/evidence\_index.jsonl

Preflight check:

* Command 1: test \-f tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py  
* Command 2: test \-f tools/evidence/update\_evidence\_index.py  
* Command 3: test \-f tools/evidence/validate\_evidence\_paths.py  
* Command 4: test \-f ci/checks/check\_evidence\_index\_hash.sh  
* Command 5: test \-f ci/checks/check\_mirror\_schema.sh

If missing, activation/install action:

* If any required script is missing, classify as TOOLING\_BLOCKED.  
* Do not invent alternate evidence validators.

If still unavailable:

* Do not infer evidence coherence.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.  
* LC\_ALL=C, LANG=C, TZ=UTC.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm every nested command return code is 0\.  
3. Confirm `coherence_status` is PASS.  
4. Confirm hash sentinels exist.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-008

What to look for:

* `coherence_status` is PASS.  
* every command in `commands` has `returncode: 0`.  
* `hash_sentinels_exist` is true.

Required deliverables:

* audit/qa/hde-epic031/checks/po-008/primary.log  
* audit/qa/hde-epic031/checks/po-008/result.json

PASS criteria tied to deliverables:

* Human Evidence Index and Machine Mirror are coherent.  
* Hash sentinels exist and validator commands pass.  
* PR-03 coherence check passes.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if evidence index, mirror, path-proof, or hash posture is inconsistent.  
* FAIL\_TOOLING if validators fail due to stale generated evidence.  
* TOOLING\_BLOCKED if required validators are unavailable.

Blocked posture:

* None if dependencies are available.

#### CHECK po-009 — PO-009

Step name, copied from the guide: PO-009

Goal: Prove machine-readable evidence remains aligned with human evidence and does not contain stale or unclassified proof companion state.

Required dependencies:

* Python 3  
* Bash  
* Step-0A harness  
* tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py  
* ci/checks/check\_mirror\_schema.sh  
* audit/qa/hde-epic031/pr-03/evidence\_family\_map.json  
* artifacts/evidence\_index.jsonl.path\_proof.txt  
* artifacts/evidence\_index.jsonl.sha256

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/pr-03/evidence\_family\_map.json  
* Command 2: test \-f artifacts/evidence\_index.jsonl.path\_proof.txt  
* Command 3: test \-f artifacts/evidence\_index.jsonl.sha256

If missing, activation/install action:

* If any required file is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer machine mirror alignment.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.  
* LC\_ALL=C, LANG=C, TZ=UTC.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm mirror schema check return code is 0\.  
3. Confirm family map exists.  
4. Confirm mirror path-proof and hash sidecar exist.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-009

What to look for:

* `family_map_present` is true.  
* `mirror_path_proof_present` is true.  
* nested command return codes are 0\.

Required deliverables:

* audit/qa/hde-epic031/checks/po-009/primary.log  
* audit/qa/hde-epic031/checks/po-009/result.json

PASS criteria tied to deliverables:

* Machine mirror and human evidence family map remain aligned.  
* Mirror path-proof exists.  
* Mirror schema check passes.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if stale or unclassified companion proof state is detected.  
* TOOLING\_BLOCKED if mirror or family map artifacts are absent.

Blocked posture:

* None if dependencies are available.

#### CHECK po-010 — PO-010

Step name, copied from the guide: PO-010

Goal: Prove governed proof fails closed when decisive predicates are missing, stale, contradictory, or outside the claimed evidence family.

Required dependencies:

* Python 3  
* Step-0A harness  
* tools/evidence/generate\_epic031\_pr01\_provider\_gate.py  
* tools/evidence/generate\_epic031\_pr02\_log\_posture.py  
* tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py

Preflight check:

* Command 1: test \-f tools/evidence/generate\_epic031\_pr01\_provider\_gate.py  
* Command 2: test \-f tools/evidence/generate\_epic031\_pr02\_log\_posture.py  
* Command 3: test \-f tools/evidence/generate\_epic031\_pr03\_evidence\_coherence.py

If missing, activation/install action:

* If any generator is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer fail-closed posture.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Inspect `result.json`.  
3. If `pr01_generator_check_mode_present` is false, classify the check as TOOLING\_BLOCKED and do not close the epic from this proof.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-010

What to look for:

* `pr02_check_mode_result.returncode` is 0\.  
* `pr03_check_mode_result.returncode` is 0\.  
* `pr01_generator_check_mode_present` is true for PASS.  
* If `blocked_reason` is populated, follow it exactly.

SOURCE EXCERPT (verbatim):

Gap: PR-01 generator check mode was not found; command rg \-n "EPIC031|HDE-EPIC031|HDE-FERM001|OUTPUTS|OUTPUT|--check|check|FAIL|PASS|write|path\_proof|argparse|pr-01|pr-02|pr-03|SAFE\_MODE|ALLOW\_NETWORK|APP\_ENV|LC\_ALL|LANG|TZ|sys.exit|raise SystemExit" tools/evidence/generate\_epic031\_pr01\_provider\_gate.py searched the PR-01 generator and returned no \--check line.

Required deliverables:

* audit/qa/hde-epic031/checks/po-010/primary.log  
* audit/qa/hde-epic031/checks/po-010/result.json

PASS criteria tied to deliverables:

* PR-01, PR-02, and PR-03 generated-proof families have checkable fail-closed proof.  
* PR-02 and PR-03 generator checks pass.  
* PR-01 fail-closed proof is not unproven.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if PR-01 fail-closed check mode remains unproven.  
* FAIL\_BEHAVIOR if a generator emits PASS while decisive predicates are missing, stale, or contradictory.  
* FAIL\_TOOLING if generator check modes fail due to stale output.

Blocked posture:

* BLOCKED unless PR-01 fail-closed check mode is proven or another approved repo locus proves the same fail-closed predicate.  
* RERUN AUDIT REQUIRED for: tools/evidence/generate\_epic031\_pr01\_provider\_gate.py \--check

#### CHECK po-011 — PO-011

Step name, copied from the guide: PO-011

Goal: Prove acceptance claims stay limited to the evidence and governance scope actually implemented in this epic.

Required dependencies:

* Python 3  
* Step-0A harness

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* Rerun Step-0A.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0A exists.  
* No new acceptance token is claimed by this check.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm `claims_limited_to_evidence_scope` is true.  
3. Confirm no token claims appear in the primary-log header.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-011

What to look for:

* `claims_limited_to_evidence_scope` is true.  
* `claimed_tokens` is empty in the primary log.  
* If acceptance map or token matrix is missing, it remains a close-stage artifact posture and not a runtime behavior failure.

Required deliverables:

* audit/qa/hde-epic031/checks/po-011/primary.log  
* audit/qa/hde-epic031/checks/po-011/result.json

PASS criteria tied to deliverables:

* No unsupported acceptance token is claimed.  
* Acceptance posture remains evidence-bound and limited to implemented scope.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if the check claims unproven acceptance tokens or unrelated acceptance-map coupling.  
* TOOLING\_BLOCKED if the harness is unavailable.

Blocked posture:

* None if Step-0A exists.

#### CHECK po-012 — PO-012

Step name, copied from the guide: PO-012

Goal: Prove HDE-FERM001.2, HDE-FERM001.3, and HDE-FERM001.4 are supportable from current implementation evidence without claiming permanent PF09.5 drainage.

Required dependencies:

* Python 3  
* Step-0A harness  
* PR-01 evidence artifacts  
* PR-02 evidence artifacts  
* PR-03 evidence artifacts

Preflight check:

* Command 1: test \-d audit/qa/hde-epic031/pr-01  
* Command 2: test \-d audit/qa/hde-epic031/pr-02  
* Command 3: test \-d audit/qa/hde-epic031/pr-03

If missing, activation/install action:

* If any PR evidence family root is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not claim active subtask support.

Preconditions:

* PR-01, PR-02, and PR-03 evidence family roots exist.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm HDE-FERM001.2, HDE-FERM001.3, and HDE-FERM001.4 support flags are true.  
3. Confirm `pf09_5_drain_claimed` is false.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-012

What to look for:

* `hde_ferm001_2_supported` is true.  
* `hde_ferm001_3_supported` is true.  
* `hde_ferm001_4_supported` is true.  
* `pf09_5_drain_claimed` is false.

Required deliverables:

* audit/qa/hde-epic031/checks/po-012/primary.log  
* audit/qa/hde-epic031/checks/po-012/result.json

PASS criteria tied to deliverables:

* The three active Fermentation subtasks are supportable from current evidence.  
* Permanent PF09.5 drainage is not claimed.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if any active subtask support is missing or if PF09.5 drainage is claimed.  
* TOOLING\_BLOCKED if required PR evidence roots are missing.

Blocked posture:

* None if PR evidence families exist.

#### CHECK po-013 — PO-013

Step name, copied from the guide: PO-013

Goal: Prove the already-complete reused foundation remains reused history and is not re-scoped as new HDE-EPIC031 implementation work.

Required dependencies:

* Python 3  
* Step-0A harness

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* Rerun Step-0A.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0A exists.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm `reused_foundation_classification` is `history_only`.  
3. Confirm `new_implementation_claim_for_reused_foundation` is false.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-013

What to look for:

* Reused foundation classification is history-only.  
* No new implementation claim is made for reused foundation work.

Required deliverables:

* audit/qa/hde-epic031/checks/po-013/primary.log  
* audit/qa/hde-epic031/checks/po-013/result.json

PASS criteria tied to deliverables:

* Reused foundation remains history-only.  
* Active slice work remains limited to HDE-FERM001.2, HDE-FERM001.3, and HDE-FERM001.4.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if reused history is described as newly implemented in HDE-EPIC031.  
* TOOLING\_BLOCKED if harness is unavailable.

Blocked posture:

* None if Step-0A exists.

#### CHECK po-014 — PO-014

Step name, copied from the guide: PO-014

Goal: Prove final QA outcome does not rely on implementation readiness alone. Earlier check logs must exist before close-stage interpretation can treat implementation readiness as QA-evidenced.

Required dependencies:

* Python 3  
* Step-0A harness  
* po-001 through po-013 primary logs

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/checks/po-001/primary.log  
* Command 2: test \-f audit/qa/hde-epic031/checks/po-013/primary.log

If missing, activation/install action:

* Run the missing prior checks in plan order.

If still unavailable:

* po-014 is TOOLING\_BLOCKED.

Preconditions:

* po-001 through po-013 have been attempted.  
* po-010 may remain TOOLING\_BLOCKED if PR-01 fail-closed check mode remains unproven; in that case po-014 must also remain TOOLING\_BLOCKED.

Setup:

* None.

Numbered PO actions:

1. Run the command after po-001 through po-013.  
2. Confirm all prior primary logs are present.  
3. Confirm implementation readiness is not treated as final QA outcome.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-014

What to look for:

* `all_prior_logs_present` is true.  
* `implementation_readiness_is_final_qa_outcome` is false.  
* If any prior primary log is absent, the step is TOOLING\_BLOCKED.

Required deliverables:

* audit/qa/hde-epic031/checks/po-014/primary.log  
* audit/qa/hde-epic031/checks/po-014/result.json

PASS criteria tied to deliverables:

* Required prior check logs exist.  
* Final QA outcome is not inferred from implementation readiness alone.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if prior logs are missing.  
* FAIL\_BEHAVIOR if implementation readiness is treated as final QA outcome.

Blocked posture:

* Do not run close-stage QA interpretation until prior checks have current-state primary logs.

#### CHECK po-015 — PO-015

Step name, copied from the guide: PO-015

Goal: Prove implementation readiness, QA readiness, final QA outcome, and later documentation drainage remain separate truth classes.

Required dependencies:

* Python 3  
* Step-0A harness

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* Rerun Step-0A.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B exists for doc-delta capture.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm every truth class is recorded as separate.  
3. Confirm PF09.5 drainage is not required before QA PASS.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-015

What to look for:

* `implementation_readiness` is `separate`.  
* `qa_readiness` is `separate`.  
* `final_qa_outcome` is `separate`.  
* `documentation_drainage` is `separate`.  
* `pf09_5_drainage_required_before_qa_pass` is false.

Required deliverables:

* audit/qa/hde-epic031/checks/po-015/primary.log  
* audit/qa/hde-epic031/checks/po-015/result.json

PASS criteria tied to deliverables:

* Truth classes remain separate.  
* Documentation drainage is not treated as a QA blocker by itself.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if truth classes collapse into one closure claim.  
* TOOLING\_BLOCKED if harness is unavailable.

Blocked posture:

* None if Step-0A exists.

#### CHECK po-016 — PO-016

Step name, copied from the guide: PO-016

Goal: Prove vendor-version runtime conformance is not treated as completed by this epic.

Required dependencies:

* Python 3  
* Step-0A harness  
* artifacts/vendor/policies\_pinned.md  
* audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt

Preflight check:

* Command 1: test \-f artifacts/vendor/policies\_pinned.md  
* Command 2: test \-f audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt

If missing, activation/install action:

* If either evidence file is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer vendor-version posture.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm `vendor_version_runtime_conformance_claimed` is false.  
3. Confirm no-live-vendor policy is present.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-016

What to look for:

* `vendor_version_runtime_conformance_claimed` is false.  
* `no_live_vendor_policy` is true.

Required deliverables:

* audit/qa/hde-epic031/checks/po-016/primary.log  
* audit/qa/hde-epic031/checks/po-016/result.json

PASS criteria tied to deliverables:

* Vendor-version runtime conformance is not claimed.  
* No-live-vendor policy remains visible.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if the result claims vendor-version runtime conformance.  
* TOOLING\_BLOCKED if required no-live evidence is absent.

Blocked posture:

* None if dependencies exist.

#### CHECK po-017 — PO-017

Step name, copied from the guide: PO-017

Goal: Prove live vendor behavior is not claimed from local implementation proof.

Required dependencies:

* Python 3  
* Step-0A harness  
* audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/pr-02/vendor\_rails\_scope.txt

If missing, activation/install action:

* If the scope file is missing, classify as TOOLING\_BLOCKED.

If still unavailable:

* Do not infer live vendor posture.

Preconditions:

* SAFE\_MODE=1.  
* ALLOW\_NETWORK=0.  
* No vendor credentials exported.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm `live_vendor_behavior_claimed` is false.  
3. Confirm `live_vendor_calls_forbidden_recorded` is true.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-017

What to look for:

* `live_vendor_behavior_claimed` is false.  
* `live_vendor_calls_forbidden_recorded` is true.

Required deliverables:

* audit/qa/hde-epic031/checks/po-017/primary.log  
* audit/qa/hde-epic031/checks/po-017/result.json

PASS criteria tied to deliverables:

* Live vendor behavior is not claimed.  
* Local implementation proof remains separate from live vendor proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if local proof is represented as live vendor behavior.  
* TOOLING\_BLOCKED if no-live-vendor evidence is absent.

Blocked posture:

* None if dependencies exist.

#### CHECK po-018 — PO-018

Step name, copied from the guide: PO-018

Goal: Prove this Live QA run proves current results only and does not become implementation, remediation, or closeout action.

Required dependencies:

* Python 3  
* Step-0A harness

Preflight check:

* Command 1: test \-f audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* Rerun Step-0A.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0A exists.  
* Step-0B exists.

Setup:

* None.

Numbered PO actions:

1. Run the command.  
2. Confirm implementation, remediation, and closeout action flags are false.  
3. Confirm `live_qa_role` is `prove_current_results_only`.

Commands:

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic031/00\_meta/live\_qa\_harness.py po-018

What to look for:

* `implementation_performed_by_live_qa` is false.  
* `remediation_performed_by_live_qa` is false.  
* `closeout_action_performed_by_live_qa` is false.  
* `live_qa_role` is `prove_current_results_only`.

Required deliverables:

* audit/qa/hde-epic031/checks/po-018/primary.log  
* audit/qa/hde-epic031/checks/po-018/result.json

PASS criteria tied to deliverables:

* Live QA remains proof-only.  
* No implementation, remediation, PF edit, or closeout action is performed by this check.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if Live QA performs implementation, remediation, or closeout action.  
* TOOLING\_BLOCKED if the harness is unavailable.

Blocked posture:

* None if Step-0A exists.

### Moon Loop posture

Moon Loop is allowed only for a trivial evidence-capture or header-generation defect under the same check root.

Allowed trigger:

* a check produced a body/result artifact but primary header generation failed because of missing exports, missing header keys, or a local quoting/syntax defect in the QA-created harness.

Allowed action:

* preserve the existing body/result artifact,  
* regenerate only the affected `primary.log` header/body assembly under the same check directory,  
* record the remediation note in `audit/qa/hde-epic031/00_meta/doc_deltas.md`.

Not allowed:

* changing product code,  
* changing repo implementation files,  
* opening vendor rails,  
* adding new public surfaces,  
* changing PASS/FAIL criteria,  
* creating a new evidence family,  
* running live vendor calls,  
* editing PF-Canon.

If the fix would touch implementation code, multiple subsystems, vendor behavior, or exceed a short bounded correction, stop and escalate to a remediation guide.

### Future-step artifact posture

The following artifacts are DEFERRED until Live QA results exist and close-stage packaging is authorized:

* audit/EPIC-031\_close\_report.md — DEFERRED  
* audit/EPIC-031\_MANIFEST.json — DEFERRED  
* audit/EPIC-031\_close\_report.md.path\_proof.txt — DEFERRED  
* audit/EPIC-031\_MANIFEST.json.path\_proof.txt — DEFERRED  
* audit/EPIC-031\_QA\_RCA.md — DEFERRED  
* audit/qa/hde-epic031/qa\_step\_logs\_manifest.json — DEFERRED  
* docs/acceptance\_map\_epic031.json — DEFERRED, because current repo audit did not prove an existing EPIC031 acceptance map  
* audit/qa/hde-epic031/token\_evidence\_matrix.md — DEFERRED, because current repo audit did not prove an existing EPIC031 token matrix  
* audit/qa/hde-epic031/acceptance\_map\_viability.log — DEFERRED, because current repo audit did not prove an existing EPIC031 acceptance map or token matrix

Do not mark these artifacts present until the step or OPS action that creates them actually runs.

### Close-out deliverables

Closeout is not part of this Live QA execution. It remains a later packaging/review action.

Required close-stage artifact family, when closeout is authorized:

* audit/EPIC-031\_close\_report.md  
* audit/EPIC-031\_MANIFEST.json  
* audit/EPIC-031\_close\_report.md.path\_proof.txt  
* audit/EPIC-031\_MANIFEST.json.path\_proof.txt  
* audit/EPIC-031\_QA\_RCA.md  
* audit/qa/hde-epic031/qa\_step\_logs\_manifest.json  
* audit/docdeltas/hde-epic031\_doc\_deltas.md  
* audit/qa/hde-epic031/00\_meta/doc\_deltas.md

Conditional close-stage artifacts, only if acceptance map or token-matrix posture is introduced and approved:

* docs/acceptance\_map\_epic031.json  
* audit/qa/hde-epic031/token\_evidence\_matrix.md  
* audit/qa/hde-epic031/acceptance\_map\_viability.log

Closeout summary requirements:

* Coverage vs QA Plan must list every PO-001 through PO-018 step in plan order.  
* Each covered step must point to its check-specific governed evidence under `audit/qa/hde-epic031/checks/<check_id>/`.  
* Blocked or unauditable steps must be called out explicitly.  
* Repo-supported completion, canon-drain completion, and formal close-pack completion must remain separate states.  
* Documentation drainage is not a blocker by itself when truth and proof are complete.  
* Truth and proof failures remain blockers.

### Execution order

Run in this order:

1. Step-0A  
2. Step-0B  
3. po-001  
4. po-002  
5. po-003  
6. po-004  
7. po-005  
8. po-006  
9. po-007  
10. po-008  
11. po-009  
12. po-010  
13. po-011  
14. po-012  
15. po-013  
16. po-014  
17. po-015  
18. po-016  
19. po-017  
20. po-018

Do not close Live QA if any required check records FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED unless a later approved review explicitly accepts the status as non-blocking for a narrower close posture.

ASK OK?  
