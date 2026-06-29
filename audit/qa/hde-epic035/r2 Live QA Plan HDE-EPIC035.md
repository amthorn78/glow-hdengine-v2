### Front matter

Epic ID: HDE-EPIC035   
Plan type: Live QA Plan / Runbook   
Execution venue: Codespaces   
Target environment: dev / repo-local governed evidence review   
Plan revision: r2  
Date (UTC): 2026-06-29   
Operators (names-only): PO, Kronos

#### Canon precedence statement (required)

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

#### Canon set (explicit; stable references only)

Canon set (titles-only, names-only, no version numbers in prose):

* PF10 — HDE-Build Notes (relevant addenda: PR-01 HDE-EPIC035, PR-02 HDE-EPIC035, OPS-01 HDE-EPIC035, PR-03 HDE-EPIC035, Implementation Retrospective HDE-EPIC035, ADR — ChartResult adapter gap is accepted for HDE-EPIC035 evidence, but future runtime work must prove full BodyGraph-detail mapping)  
* PF05 — HDE CLI/API Vendor Reference  
* PF19 — Glow QA Guide  
* PF23 — Reality Audits  
* PF27 — Canon Plan Templates  
* PF09.5 — HDE Build Checklist Fermentation

Note: PF20 may be cited only for historical record context, never as a source of requirements.

### Scope statement

This plan evaluates the following in-scope surfaces / checks:

* Step-0B — Doc Delta Capture  
* PO-001 — Vendor outcome mapping classification  
* PO-002 — Retry and rate-limit interpretation  
* PO-003 — Malformed/network/unexpected-status/redirect classification  
* PO-004 — Bounded observability and secret-safe evidence  
* PO-005 — v2 chart route family vs legacy BodyGraph route family distinction  
* PO-006 — Simple v2 chart observation scope  
* PO-007 — BodyGraph-resolution route-policy gap  
* PO-008 — Response-normalization exact adapter/schema gap  
* PO-009 — Simple chart data is not sufficient BodyGraph-detail data  
* PO-010 — Future runtime compatibility requires bounded adapter/schema proof  
* PO-011 — Evidence-loop binding across provider outcome, response-normalization gap, and retained live observation  
* PO-012 — Distinction between implementation evidence, OPS observation, QA evidence, status movement, and closeout  
* PO-013 — Nonclaims for runtime conformance, public expansion, app-side ownership, raw payload persistence, and AI scope  
* PO-014 — Current repo evidence coherence with PF10 scope boundaries  
* qa-16-close-out-deliverables — Close-out deliverables

This plan explicitly excludes:

* New OPS execution  
* New live vendor call  
* HumanDesignAPI v2 full runtime conformance claim  
* HDE-FERM008 parent completion claim  
* PF09 status movement claim  
* Epic closeout claim  
* Public Reader change  
* Public route, flag, payload, or transport change  
* New HTTP home  
* App-side HumanDesignAPI credential ownership claim  
* Raw request, response, secret, or vendor payload persistence  
* AI scope  
* PF-Canon edits

#### PF10 overrides / conflicts (if any)

PF10 records HDE-EPIC035 as an evidence-slice epic for HDE-FERM008.3 through HDE-FERM008.5. PF10 records provider-outcome evidence, response-normalization exact gap evidence, retained OPS-01 open-rails observation, and PR-03 governed evidence-loop binding. PF10 also records that the evidence supports later status recommendations for specific PF09.5 subtasks but does not itself claim PF09 status movement, HDE-FERM008 parent completion, QA PASS before Live QA, OPS completion, epic closeout, full HumanDesignAPI v2 runtime conformance, or public-surface expansion.

### Open-Rails Live QA Requirement for production-affecting epics

This is a production-affecting vendor-seam epic, but this Live QA Plan does not run a new open-rails step.

Authorized omission of a new open-rails Live QA step:

* Why omitted: PF10 records retained OPS-01 bounded open-rails evidence for HDE-EPIC035, and the current Live QA scope is to validate governed evidence posture, nonclaims, binding, and closeout readiness without rerunning OPS.  
* Who authorized the omission: PF10 records OPS-01 as the bounded PO-authorized live observation and PR-03 as binding already-produced OPS-01 evidence without rerun.  
* What production claim is not being made: this Live QA Plan does not claim full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, PF09 status movement, public-surface expansion, new app-side credential ownership, raw payload persistence, or epic closeout.  
* Whether later open-rails QA is required: later open-rails QA is required before any broader runtime, production compatibility, BodyGraph-detail adapter, public Reader, public route, or full v2 conformance claim.

### PF23 anchors

PF23 was treated as planning-time repo-reality context only. It is not a required deliverable, required check, acceptance token, execution-time artifact, or operator-command source. Live repo validation and the HDE-EPIC035 repo audit are the current repo-reality sources used to ground the loci in this plan.

### Environment and rails posture

#### Determinism pins

When producing governed bytes, use:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

#### Rails posture

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

Rails change by check:

* None. All checks in this plan run closed rails.  
* Retained OPS-01 open-rails evidence is inspected as already-produced evidence only and is not rerun.

#### No VCS workflow content

This plan does not instruct branch, commit, PR, merge, rebase, checkout, push, pull, or release workflow. Repo identity was validated during planning only. PASS/FAIL does not depend on branch name, commit SHA, PR identifier, or working-tree cleanliness.

### PO inputs needed

Required external inputs:

* None for the default closed-rails Live QA checks.

If a dependency is missing at runtime, classify the affected check as TOOLING\_BLOCKED. Do not install packages or alter the repo unless the PO routes a separate remediation action.

### Evidence posture and directory structure

#### Epic QA root normalization

Canonical epic QA root:

* audit/qa/hde-epic035/

Check-centric paths:

* audit/qa/hde-epic035/checks/\<check\_id\>/primary.log  
* audit/qa/hde-epic035/checks/\<check\_id\>/primary.log.path\_proof.txt

Epic-level meta paths:

* audit/qa/hde-epic035/00\_meta/  
* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json.path\_proof.txt

No per-run root, run-id directory, EVIDENCE\_ROOT variable, latest\_run\_id pointer, or run-id correctness key is used.

#### Step-log header schema expectations

Each primary log first line must be a single-line JSON header with at least:

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

Allowed status values:

* PASS  
* FAIL\_BEHAVIOR  
* FAIL\_TOOLING  
* TOOLING\_BLOCKED  
* SKIPPED  
* WARN

PASS requires exit\_code=0. If status is not PASS, claimed\_tokens must be \[\].

Canonical step-log header writer (included once as required):

`python - << 'PY'` `import datetime` `import json` `import os` `` `def env(name: str, default: str = "") -> str:` ` value = os.environ.get(name)` ` return value if value is not None else default` `` `def env_json(name: str, default):` `raw = os.environ.get(name)` `if raw is None or raw == "":` `return default` `return json.loads(raw)` `` `schema_version = "pf27.step_log_header.v1"` `timestamp_utc = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"` `` `status = env("PASS_FAIL")` `fail_status = "" if status == "PASS" else status` `exit_code_raw = env("EXIT_CODE", "")` `exit_code = int(exit_code_raw) if exit_code_raw != "" else None` `if status == "PASS" and exit_code != 0:` `raise SystemExit("PASS requires EXIT_CODE=0")` `commands = env_json("COMMANDS_JSON", [])` `if isinstance(commands, str):` `commands = [commands]` `command = "; ".join(commands) if commands else "N/A"` `` `header = {` ` "schema_version": schema_version,` ` "timestamp_utc": timestamp_utc,` ` "check_id": env("CHECK_ID"),` ` "check_name": env("CHECK_NAME"),` ` "status": status,` ` "fail_status": fail_status,` ` "command": command,` ` "command_provenance": env("COMMAND_PROVENANCE", "Explicitly created"),` ` "exit_code": exit_code,` ` "evidence_artifacts": env_json("ARTIFACTS_JSON", []),` ` "captured_env": {` ` "SAFE_MODE": env("SAFE_MODE"),` ` "ALLOW_NETWORK": env("ALLOW_NETWORK"),` ` "APP_ENV": env("APP_ENV"),` ` "LC_ALL": env("LC_ALL"),` ` "LANG": env("LANG"),` ` "TZ": env("TZ"),` ` },` ` "pf_refs": env_json("PF_REFS_JSON", []),` ` "intended_tokens": env_json("INTENDED_TOKENS_JSON", []),` ` "claimed_tokens": env_json("CLAIMED_TOKENS_JSON", []),` `}` `` `print(json.dumps(header, ensure_ascii=False))` `PY`

This plan uses one QA-created helper under audit/qa/hde-epic035/00\_meta/ to emit the same required header keys and sibling path proofs for every check. The helper is created by Step-0B because the repo audit found no existing HDE-EPIC035 Live QA harness under the epic audit roots.

### Mandatory Step-0 artifacts

Step-0B produces the required two-surface doc-delta pair:

* audit/docdeltas/hde-epic035\_doc\_deltas.md  
* audit/qa/hde-epic035/00\_meta/doc\_deltas.md

Step-0B also creates the QA helper used by this runbook:

* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py

Step-0B records known plan/repo caveats, including:

* no pre-existing repo-resident HDE-EPIC035 Live QA harness under the audit roots, so this plan creates one under the stable QA root;  
* CLI help/parser locus for hdctl bg:resolve was not isolated by the repo audit, so this plan does not execute hdctl bg:resolve;  
* retained OPS evidence is inspected as existing evidence only and OPS-01 is not rerun;  
* some retained OPS files may not be used as PASS-gating artifacts unless a sibling path proof is present or the check predicate is proven from another governed artifact.

### Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens (optional) | PF anchors |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| step-0b-doc-delta-capture | Step-0B — Doc Delta Capture | D0 / doc-delta and QA harness setup | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | Create QA helper, then run helper check | PASS if doc-delta surfaces, helper, primary log, and path proof are created | audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log | doc-delta pair, helper, primary log, path proof | DOC\_DELTA\_PRESENT\_OK | PF27 — Canon Plan Templates |
| po-001 | PO-001 | D1 / vendor outcome mapping | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-001 | PASS if provider categories are deterministic and raw vendor data is not exposed | audit/qa/hde-epic035/checks/po-001/primary.log | primary log, path proof, provider outcome snapshot | \[\] | PF10 — HDE-Build Notes |
| po-002 | PO-002 | D2 / retry and rate-limit interpretation | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-002 | PASS if retry/rate-limit mapping is bounded and deterministic | audit/qa/hde-epic035/checks/po-002/primary.log | primary log, path proof, retry/rate-limit snapshot | \[\] | PF10 — HDE-Build Notes |
| po-003 | PO-003 | D3 / malformed/network/unexpected/redirect classification | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-003 | PASS if error categories are distinct and not collapsed to generic unavailability | audit/qa/hde-epic035/checks/po-003/primary.log | primary log, path proof, provider outcome snapshot | \[\] | PF10 — HDE-Build Notes |
| po-004 | PO-004 | D4 / bounded observability | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-004 | PASS if observability is labels-only and secret-safe | audit/qa/hde-epic035/checks/po-004/primary.log | primary log, path proof, provider outcome snapshot, response mapping snapshot | \[\] | PF10 — HDE-Build Notes |
| po-005 | PO-005 | D5 / route family distinction | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-005 | PASS if v2 chart and legacy BodyGraph route families remain distinct | audit/qa/hde-epic035/checks/po-005/primary.log | primary log, path proof, route-family evidence | \[\] | PF10 — HDE-Build Notes |
| po-006 | PO-006 | D6 / simple v2 chart observation scope | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-006 | PASS if simple chart observation is narrow and non-conformant beyond its scope | audit/qa/hde-epic035/checks/po-006/primary.log | primary log, path proof, OPS final classification, OPS binding | \[\] | PF10 — HDE-Build Notes |
| po-007 | PO-007 | D7 / BodyGraph route-policy runtime gap | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-007 | PASS if BodyGraph-resolution route-policy gap remains recorded | audit/qa/hde-epic035/checks/po-007/primary.log | primary log, path proof, OPS final classification, OPS binding | \[\] | PF10 — HDE-Build Notes |
| po-008 | PO-008 | D8 / response-normalization exact gap | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-008 | PASS if exact adapter/schema gap is preserved | audit/qa/hde-epic035/checks/po-008/primary.log | primary log, path proof, response mapping snapshot | \[\] | PF10 — HDE-Build Notes |
| po-009 | PO-009 | D9 / simple chart insufficient for BodyGraph detail | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-009 | PASS if simple chart data is not treated as sufficient BodyGraph-detail data | audit/qa/hde-epic035/checks/po-009/primary.log | primary log, path proof, response mapping snapshot | \[\] | PF10 — HDE-Build Notes |
| po-010 | PO-010 | D10 / future runtime adapter proof requirement | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-010 | PASS if future runtime compatibility requires bounded adapter/schema proof | audit/qa/hde-epic035/checks/po-010/primary.log | primary log, path proof, response mapping snapshot | \[\] | PF10 — HDE-Build Notes |
| po-011 | PO-011 | D11 / governed evidence-loop binding | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-011 | PASS if provider, response-gap, and retained OPS evidence bind coherently | audit/qa/hde-epic035/checks/po-011/primary.log | primary log, path proof, acceptance map, release binding, token matrix | \[\] | PF10 — HDE-Build Notes |
| po-012 | PO-012 | D12 / evidence category separation | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-012 | PASS if implementation evidence, OPS observation, QA evidence, status movement, and closeout remain distinct | audit/qa/hde-epic035/checks/po-012/primary.log | primary log, path proof, acceptance map, OPS binding | \[\] | PF10 — HDE-Build Notes |
| po-013 | PO-013 | D13 / explicit nonclaims | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-013 | PASS if forbidden conformance, public, app-side, payload, and AI claims remain absent | audit/qa/hde-epic035/checks/po-013/primary.log | primary log, path proof, acceptance map, response mapping, OPS binding | \[\] | PF10 — HDE-Build Notes |
| po-014 | PO-014 | D14 / current repo evidence coherence | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-014 | PASS if targeted tests and governed evidence gates exit 0 and current evidence coheres with PF10 boundaries | audit/qa/hde-epic035/checks/po-014/primary.log | primary log, path proof, tests, evidence index, mirror, acceptance map | EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK, JSON\_CANONICAL\_CHECK\_OK, TESTS\_PASS\_OK | PF10 — HDE-Build Notes |
| qa-16-close-out-deliverables | Close-out deliverables | D15 / closeout packaging | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py qa-16-close-out-deliverables | PASS if manifest, discovery artifact, and QA RCA / Doc Delta summary are produced and path-proven | audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log | primary log, path proof, manifest, discovery artifact, QA RCA / Doc Delta summary | \[\] | PF27 — Canon Plan Templates |

### Token coverage and evidence binding

Token-attached checks:

* step-0b-doc-delta-capture intends and may claim DOC\_DELTA\_PRESENT\_OK.  
* po-014 intends and may claim EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK, JSON\_CANONICAL\_CHECK\_OK, and TESTS\_PASS\_OK.

Tokenless evidence checks:

* po-001 through po-013 and qa-16-close-out-deliverables are explicit non-token evidence requirements with mechanical PASS predicates and captured artifacts.

No vendor-v2-specific acceptance token is minted or claimed.

### Check Blocks

#### CHECK step-0b-doc-delta-capture: Step-0B — Doc Delta Capture

Surface / D-goal mapping: D0 / doc-delta capture and QA helper setup Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF27 — Canon Plan Templates; PF19 — Glow QA Guide Proof class: QA evidence assembly; no product behavior proof, no OPS execution, no PF09 status movement, no epic closeout claim.

Intent:

Create the stable doc-delta surfaces, create the QA helper needed because no HDE-EPIC035 Live QA harness exists under the audited epic roots, and record current planning caveats before the PO executes the proof checks.

Dependencies required:

* Python  
* Filesystem write permission under audit/  
* Existing repo root

Preflight check:

* python \--version  
* test \-d audit  
* test \-d artifacts  
* test \-d docs

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Run this step before all other checks.

Setup:

* This step creates audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py as QA-created evidence infrastructure for this runbook.  
* This step creates the doc-delta pair under audit/docdeltas/ and audit/qa/hde-epic035/00\_meta/.

Numbered PO actions:

1. Open a Codespaces terminal at the repo root.  
2. Run Command 1 to create the QA helper.  
3. Run Command 2 to execute Step-0B.  
4. Open audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log.  
5. Confirm the first line is a JSON header with check\_id step-0b-doc-delta-capture.  
6. Confirm the body records the doc-delta surfaces and known planning caveats.  
7. Open audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt.

Command 1:

mkdir \-p audit/qa/hde-epic035/00\_meta audit/qa/hde-epic035/checks audit/docdeltas && cat \> audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py \<\<'PY'  
 from **future** import annotations  
 import datetime  
 import hashlib  
 import json  
 import os  
 import subprocess  
 import sys  
 from pathlib import Path  
 from typing import Any

EPIC\_ID \= "HDE-EPIC035"  
 QA\_ROOT \= Path("audit/qa/hde-epic035")  
 CHECKS\_ROOT \= QA\_ROOT / "checks"  
 META\_ROOT \= QA\_ROOT / "00\_meta"  
 DOCDELTA\_DRAFT \= Path("audit/docdeltas/hde-epic035\_doc\_deltas.md")  
 DOCDELTA\_CAPTURE \= META\_ROOT / "doc\_deltas.md"

class ToolingBlocked(Exception): pass  
 class FailBehavior(Exception): pass  
 class FailTooling(Exception): pass

def utc\_now() \-\> str:  
 return datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"

def sha256(path: Path) \-\> str:  
 h \= hashlib.sha256()  
 with path.open("rb") as f:  
 for chunk in iter(lambda: f.read(8192), b""):  
 h.update(chunk)  
 return h.hexdigest()

def write\_path\_proof(path: Path) \-\> Path:  
 if not path.exists():  
 raise ToolingBlocked(f"MISSING\_PATH\_FOR\_PROOF:{path}")  
 proof \= Path(str(path) \+ ".path\_proof.txt")  
 stat \= path.stat()  
 proof.write\_text(  
 "\\n".join(\[  
 f"path: {path}",  
 f"size\_bytes: {stat.st\_size}",  
 f"sha256: {sha256(path)}",  
 f"mtime\_utc: {datetime.datetime.utcfromtimestamp(stat.st\_mtime).replace(microsecond=0).isoformat()}Z",  
 f"produced\_at\_utc: {utc\_now()}",  
 "",  
 \]),  
 encoding="utf-8",  
 )  
 return proof

def read\_text(path: str | Path) \-\> str:  
 p \= Path(path)  
 if not p.exists():  
 raise ToolingBlocked(f"MISSING\_FILE:{p}")  
 return p.read\_text(encoding="utf-8")

def load\_json(path: str | Path) \-\> dict\[str, Any\]:  
 return json.loads(read\_text(path))

def require\_file(path: str | Path, body: list\[str\]) \-\> None:  
 p \= Path(path)  
 if not p.exists():  
 raise ToolingBlocked(f"MISSING\_FILE:{p}")  
 body.append(f"FILE\_OK {p} sha256={sha256(p)}")

def require\_contains(path: str | Path, needle: str, body: list\[str\]) \-\> None:  
 text \= read\_text(path)  
 if needle not in text:  
 raise FailBehavior(f"MISSING\_TEXT:{path}:{needle}")  
 body.append(f"TEXT\_OK {path} :: {needle}")

def require\_json\_value(path: str | Path, key: str, expected: Any, body: list\[str\]) \-\> None:  
 payload \= load\_json(path)  
 if key not in payload:  
 raise FailBehavior(f"MISSING\_JSON\_KEY:{path}:{key}")  
 actual \= payload\[key\]  
 if actual \!= expected:  
 raise FailBehavior(f"JSON\_VALUE\_MISMATCH:{path}:{key}:{actual\!r}\!={expected\!r}")  
 body.append(f"JSON\_OK {path} :: {key}={expected\!r}")

def require\_json\_contains\_record(path: str | Path, key: str, field: str, expected: Any, body: list\[str\]) \-\> None:  
 payload \= load\_json(path)  
 records \= payload.get(key)  
 if not isinstance(records, list):  
 raise FailBehavior(f"JSON\_NOT\_LIST:{path}:{key}")  
 for rec in records:  
 if isinstance(rec, dict) and rec.get(field) \== expected:  
 body.append(f"JSON\_RECORD\_OK {path} :: {key}.{field}={expected\!r}")  
 return  
 raise FailBehavior(f"MISSING\_JSON\_RECORD:{path}:{key}.{field}={expected\!r}")

def canonical\_json\_file(path: str | Path, body: list\[str\]) \-\> None:  
 p \= Path(path)  
 raw \= p.read\_bytes()  
 if not raw.endswith(b"\\n") or raw.endswith(b"\\n\\n") or raw.startswith(b"\\xef\\xbb\\xbf"):  
 raise FailBehavior(f"JSON\_CANONICAL\_BYTES\_FAIL:{p}")  
 payload \= json.loads(raw.decode("utf-8"))  
 expected \= json.dumps(payload, ensure\_ascii=False, sort\_keys=True, separators=(",", ":")).encode("utf-8") \+ b"\\n"  
 if raw \!= expected:  
 raise FailBehavior(f"JSON\_CANONICAL\_SORT\_FAIL:{p}")  
 body.append(f"JSON\_CANONICAL\_OK {p}")

def run\_cmd(cmd: list\[str\], body: list\[str\], tooling: bool \= False) \-\> None:  
 body.append("COMMAND " \+ " ".join(cmd))  
 try:  
 cp \= subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)  
 except FileNotFoundError as exc:  
 raise ToolingBlocked(f"COMMAND\_MISSING:{cmd\[0\]}") from exc  
 if cp.stdout:  
 body.append(cp.stdout.strip())  
 body.append(f"EXIT\_CODE {cp.returncode}")  
 if cp.returncode \!= 0:  
 if tooling:  
 raise FailTooling(f"COMMAND\_FAILED:{' '.join(cmd)}:{cp.returncode}")  
 raise FailBehavior(f"COMMAND\_FAILED:{' '.join(cmd)}:{cp.returncode}")

def require\_pytest(body: list\[str\]) \-\> None:  
 cp \= subprocess.run(\[sys.executable, "-c", "import pytest"\], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=False)  
 if cp.returncode \!= 0:  
 raise ToolingBlocked("PYTEST\_IMPORT\_MISSING")  
 body.append("PYTEST\_IMPORT\_OK")

def check\_step0b(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 META\_ROOT.mkdir(parents=True, exist\_ok=True)  
 DOCDELTA\_DRAFT.parent.mkdir(parents=True, exist\_ok=True)  
 text \= "\\n".join(\[  
 "\# HDE-EPIC035 Live QA Doc Delta Capture",  
 "",  
 "BLOCKERS:",  
 "- None at planning time.",  
 "",  
 "CAVEATS:",  
 "- No pre-existing repo-resident HDE-EPIC035 Live QA harness was found under the audited epic QA or OPS roots; this plan creates a QA helper under audit/qa/hde-epic035/00\_meta/.",  
 "- CLI help/parser locus for hdctl bg:resolve was not isolated by the repo audit; this plan does not execute hdctl bg:resolve and uses retained OPS evidence only.",  
 "- Retained OPS-01 evidence is already-produced evidence only; this plan does not rerun OPS.",  
 "- Some retained OPS files were listed by audit without sibling path-proof proof; this plan gates only on explicit artifacts and path proofs required by each check.",  
 "",  
 \])  
 DOCDELTA\_DRAFT.write\_text(text, encoding="utf-8")  
 DOCDELTA\_CAPTURE.write\_text(text, encoding="utf-8")  
 draft\_proof \= write\_path\_proof(DOCDELTA\_DRAFT)  
 capture\_proof \= write\_path\_proof(DOCDELTA\_CAPTURE)  
 body.append(f"DOC\_DELTA\_DRAFT={DOCDELTA\_DRAFT}")  
 body.append(f"DOC\_DELTA\_CAPTURE={DOCDELTA\_CAPTURE}")  
 return \[str(DOCDELTA\_DRAFT), str(draft\_proof), str(DOCDELTA\_CAPTURE), str(capture\_proof), "audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py"\], \["DOC\_DELTA\_PRESENT\_OK"\], \["DOC\_DELTA\_PRESENT\_OK"\]

def check\_po001(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json"  
 require\_file(p, body)  
 require\_json\_value(p, "artifact\_kind", "hdapi\_v2\_provider\_outcome\_mapping", body)  
 require\_json\_value(p, "epic\_id", "HDE-EPIC035", body)  
 require\_json\_value(p, "pf09\_subtask\_id", "HDE-FERM008.3", body)  
 require\_json\_contains\_record(p, "status\_mapping\_records", "provider\_code", "PROVIDER\_UNAUTHORIZED", body)  
 require\_json\_contains\_record(p, "status\_mapping\_records", "provider\_code", "PROVIDER\_RATE\_LIMITED", body)  
 require\_json\_contains\_record(p, "status\_mapping\_records", "provider\_code", "PROVIDER\_UNAVAILABLE", body)  
 require\_json\_value(p, "network\_error\_record", {"classification":"network\_error","provider\_code":"PROVIDER\_NETWORK\_ERROR","retryable":True}, body)  
 require\_json\_value(p, "no\_claims", {"full\_hdapi\_v2\_runtime\_conformance":"NONE","live\_vendor\_call":"NONE","open\_rails\_ops\_execution":"NONE","public\_reader\_change":"NONE","public\_route\_flag\_payload\_or\_transport\_change":"NONE","raw\_vendor\_payload\_persisted":"NONE"}, body)  
 return \[p\], \[\], \[\]

def check\_po002(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/rate\_limit\_headers.snapshot.json"  
 require\_file(p, body)  
 require\_json\_value(p, "artifact\_kind", "hdapi\_v2\_retry\_after\_mapping", body)  
 require\_json\_value(p, "epic\_id", "HDE-EPIC035", body)  
 require\_json\_value(p, "pf09\_subtask\_id", "HDE-FERM008.3", body)  
 require\_json\_value(p, "rate\_limit\_status\_record", {"classification":"429","provider\_code":"PROVIDER\_RATE\_LIMITED","retry\_after\_header\_supported":True,"retryable":False,"status":429}, body)  
 for case in \["delta\_seconds", "http\_date", "invalid", "overflow"\]:  
 require\_json\_contains\_record(p, "retry\_after\_records", "case", case, body)  
 return \[p\], \[\], \[\]

def check\_po003(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json"  
 require\_file(p, body)  
 require\_json\_contains\_record(p, "bad\_response\_records", "scenario", "malformed\_json\_response", body)  
 require\_json\_contains\_record(p, "bad\_response\_records", "scenario", "provider\_bad\_response", body)  
 require\_json\_contains\_record(p, "status\_mapping\_records", "status", 302, body)  
 require\_json\_value(p, "retry\_classification", {"429":False,"4xx":False,"5xx":True,"http\_status\_other":False,"network\_error":True,"redirect\_response":False}, body)  
 require\_json\_value(p, "network\_error\_record", {"classification":"network\_error","provider\_code":"PROVIDER\_NETWORK\_ERROR","retryable":True}, body)  
 return \[p\], \[\], \[\]

def check\_po004(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p1 \= "artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json"  
 p2 \= "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json"  
 require\_file(p1, body)  
 require\_file(p2, body)  
 obs \= load\_json(p1).get("observability\_posture", {})  
 for k in \["bounded\_labels\_only","keys\_only","no\_plaintext\_secret\_value","no\_raw\_request\_body","no\_raw\_response\_body","no\_raw\_secret\_header","no\_raw\_vendor\_payload"\]:  
 if obs.get(k) is not True:  
 raise FailBehavior(f"OBSERVABILITY\_FAIL:{k}")  
 body.append(f"OBSERVABILITY\_OK {p1} :: {k}=true")  
 require\_json\_value(p2, "data\_payload\_body\_emitted", False, body)  
 require\_json\_value(p2, "raw\_response\_body\_persisted" if "raw\_response\_body\_persisted" in load\_json(p2) else "runtime\_conformance\_claim", "NONE", body)  
 return \[p1, p2\], \[\], \[\]

def check\_po005(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json"  
 require\_file(p, body)  
 payload \= load\_json(p)  
 route \= payload.get("route\_family\_identity", {})  
 legacy \= json.dumps(route.get("legacy\_v1\_bodygraph\_routes", \[\]), sort\_keys=True)  
 v2 \= json.dumps(route.get("v2\_chart\_routes", \[\]), sort\_keys=True)  
 if "HD-Api-Key: \<redacted\>" not in legacy:  
 raise FailBehavior("LEGACY\_AUTH\_POSTURE\_MISSING")  
 if "Authorization: Bearer \<redacted\>" not in v2:  
 raise FailBehavior("V2\_AUTH\_POSTURE\_MISSING")  
 for resource in \["bodygraphs", "bodygraphs/simple", "charts", "charts/simple", "charts/coordinates"\]:  
 if resource not in route.get("version\_neutral\_runtime\_resource\_paths", \[\]):  
 raise FailBehavior(f"ROUTE\_FAMILY\_RESOURCE\_MISSING:{resource}")  
 body.append(f"ROUTE\_FAMILY\_OK {resource}")  
 return \[p\], \[\], \[\]

def check\_po006(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 final \= "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt"  
 binding \= "audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log"  
 require\_file(final, body)  
 require\_file(binding, body)  
 require\_contains(final, "v2\_charts\_simple=success", body)  
 require\_contains(final, "v2\_charts\_simple\_request\_shape=/v2/charts/simple", body)  
 require\_contains(final, "v2\_charts\_simple\_response\_type=ChartSimpleResult", body)  
 require\_contains(binding, "full\_runtime\_conformance\_claim=false", body)  
 require\_contains(binding, "ops\_completion\_claim=false", body)  
 return \[final, binding\], \[\], \[\]

def check\_po007(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 final \= "audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt"  
 binding \= "audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log"  
 require\_file(final, body)  
 require\_file(binding, body)  
 require\_contains(final, "bg\_resolve\_error\_code=PROVIDER\_NOT\_FOUND", body)  
 require\_contains(final, "bg\_resolve\_http\_status=404", body)  
 require\_contains(final, "runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base", body)  
 require\_contains(binding, "bg\_resolve\_runtime\_gap=legacy BodyGraph route observation against configured v2 base returned PROVIDER\_NOT\_FOUND / 404", body)  
 return \[final, binding\], \[\], \[\]

def check\_po008(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json"  
 require\_file(p, body)  
 require\_json\_value(p, "artifact\_kind", "hdapi\_v2\_response\_normalization\_gap", body)  
 require\_json\_value(p, "response\_normalization\_posture", "EXACT\_SCHEMA\_ADAPTER\_GAP\_RECORDED", body)  
 require\_json\_value(p, "schema\_gap\_status", "GAP\_RECORDED", body)  
 require\_json\_value(p, "normalized\_data\_path\_proof\_claim", "NONE", body)  
 require\_contains(p, "HDE-FERM008.4 remains an exact adapter/schema gap", body)  
 return \[p\], \[\], \[\]

def check\_po009(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json"  
 require\_file(p, body)  
 require\_contains(p, "ChartSimpleResult", body)  
 require\_contains(p, "ChartResult/ChartSimpleResult-to-BodyGraph adapter", body)  
 require\_contains(p, "schema\_gap\_recorded", body)  
 require\_contains(p, "no\_compatibility\_by\_inference", body)  
 require\_json\_value(p, "no\_compatibility\_by\_inference", True, body)  
 return \[p\], \[\], \[\]

def check\_po010(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 p \= "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json"  
 require\_file(p, body)  
 require\_contains(p, "A bounded adapter/schema proof or implementation must map v2 ChartResult/ChartSimpleResult data into the existing BodyGraph/person cache contract before compatibility can be claimed.", body)  
 require\_json\_value(p, "runtime\_conformance\_claim", "NONE", body)  
 require\_json\_value(p, "normalized\_data\_path\_proof\_claim", "NONE", body)  
 return \[p\], \[\], \[\]

def check\_po011(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 paths \= \["artifacts/vendor/hdapi\_v2/release\_binding.snapshot.json", "docs/acceptance\_map\_epic035.json", "audit/qa/hde-epic035/token\_evidence\_matrix.md"\]  
 for p in paths:  
 require\_file(p, body)  
 require\_contains(paths\[0\], "pr01\_hde\_ferm008\_3\_provider\_outcome", body)  
 require\_contains(paths\[0\], "pr02\_hde\_ferm008\_4\_response\_normalization", body)  
 require\_contains(paths\[1\], "ops\_01", body)  
 require\_contains(paths\[1\], "HDE-FERM008.5 governed evidence-loop closure", body)  
 require\_contains(paths\[2\], "HDE-FERM008.5 evidence-loop closure posture", body)  
 return paths, \[\], \[\]

def check\_po012(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 paths \= \["docs/acceptance\_map\_epic035.json", "audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log"\]  
 for p in paths:  
 require\_file(p, body)  
 for needle in \["QA PASS", "OPS completion", "PF09 status movement", "HDE-FERM008 parent Done", "epic closeout"\]:  
 require\_contains(paths\[0\], needle, body)  
 require\_contains(paths\[1\], "qa\_pass\_claim=false", body)  
 require\_contains(paths\[1\], "pf09\_status\_movement\_claim=false", body)  
 require\_contains(paths\[1\], "epic\_closeout\_claim=false", body)  
 return paths, \[\], \[\]

def check\_po013(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 paths \= \["docs/acceptance\_map\_epic035.json", "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json", "audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log"\]  
 for p in paths:  
 require\_file(p, body)  
 for needle in \["full HumanDesignAPI v2 runtime conformance", "public Reader change", "public route", "public flag", "public payload or transport change", "new HTTP home", "app-side HumanDesignAPI credential ownership", "raw payload persistence", "AI scope"\]:  
 require\_contains(paths\[0\], needle, body)  
 require\_json\_value(paths\[1\], "ai\_scope\_claim", "NONE", body)  
 require\_contains(paths\[2\], "full\_runtime\_conformance\_claim=false", body)  
 require\_contains(paths\[2\], "ai\_scope\_claim=false", body)  
 return paths, \[\], \[\]

def check\_po014(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 require\_pytest(body)  
 artifacts \= \[  
 "tests/evidence/test\_hdapi\_v2\_live\_conformance.py",  
 "tests/evidence/test\_hdapi\_v2\_response\_normalization.py",  
 "tests/evidence/test\_hdapi\_v2\_contract\_inventory.py",  
 "tests/evidence/test\_hde\_epic035\_pr03\_evidence\_loop.py",  
 "docs/evidence/INDEX.json",  
 "docs/evidence/INDEX.sha256",  
 "artifacts/evidence\_index.jsonl",  
 "artifacts/evidence\_index.jsonl.sha256",  
 "docs/acceptance\_map\_epic035.json",  
 "artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json",  
 "artifacts/vendor/hdapi\_v2/rate\_limit\_headers.snapshot.json",  
 "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json",  
 "artifacts/vendor/hdapi\_v2/release\_binding.snapshot.json",  
 \]  
 for p in artifacts:  
 require\_file(p, body)  
 for p in \["docs/acceptance\_map\_epic035.json", "artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json", "artifacts/vendor/hdapi\_v2/rate\_limit\_headers.snapshot.json", "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json", "artifacts/vendor/hdapi\_v2/release\_binding.snapshot.json"\]:  
 canonical\_json\_file(p, body)  
 run\_cmd(\[sys.executable, "-m", "pytest", "tests/evidence/test\_hdapi\_v2\_live\_conformance.py", "tests/evidence/test\_hdapi\_v2\_response\_normalization.py", "tests/evidence/test\_hdapi\_v2\_contract\_inventory.py", "tests/evidence/test\_hde\_epic035\_pr03\_evidence\_loop.py"\], body)  
 run\_cmd(\[sys.executable, "tools/evidence/validate\_evidence\_paths.py"\], body)  
 run\_cmd(\[sys.executable, "tools/evidence/check\_lf\_endings.py"\], body)  
 run\_cmd(\[sys.executable, "tools/evidence/update\_evidence\_index.py", "--check"\], body)  
 run\_cmd(\["bash", "ci/checks/check\_mirror\_schema.sh"\], body)  
 run\_cmd(\["bash", "ci/checks/check\_evidence\_index\_hash.sh"\], body)  
 run\_cmd(\["bash", "ci/checks/check\_final\_lf.sh"\], body)  
 tokens \= \["EVIDENCE\_INDEX\_UPDATED\_OK","MACHINE\_MIRROR\_UPDATED\_OK","EVIDENCE\_INDEX\_HASH\_OK","EVIDENCE\_PATHS\_VALIDATED\_OK","EVIDENCE\_PATH\_PROOFS\_OK","JSON\_CANONICAL\_CHECK\_OK","TESTS\_PASS\_OK"\]  
 for t in tokens:  
 require\_contains("docs/acceptance\_map\_epic035.json", t, body)  
 return artifacts, tokens, tokens

def check\_closeout(body: list\[str\]) \-\> tuple\[list\[str\], list\[str\], list\[str\]\]:  
 expected \= \["step-0b-doc-delta-capture"\] \+ \[f"po-{i:03d}" for i in range(1, 15)\]  
 entries \= \[\]  
 for check\_id in expected:  
 log \= CHECKS\_ROOT / check\_id / "primary.log"  
 proof \= Path(str(log) \+ ".path\_proof.txt")  
 if not log.exists():  
 raise ToolingBlocked(f"NOT\_RUN:{check\_id}:{log}")  
 if not proof.exists():  
 raise ToolingBlocked(f"MISSING\_PATH\_PROOF:{check\_id}:{proof}")  
 header \= json.loads(log.read\_text(encoding="utf-8").splitlines()\[0\])  
 entries.append({"check\_id": check\_id, "status": header.get("status"), "log\_path": str(log), "path\_proof\_path": str(proof)})  
 manifest \= QA\_ROOT / "qa\_step\_logs\_manifest.json"  
 manifest.write\_text(json.dumps({"schema\_version":"pf27.qa\_step\_logs\_manifest.v1","epic\_id":EPIC\_ID,"entries":entries}, sort\_keys=True, separators=(",",":")) \+ "\\n", encoding="utf-8")  
 manifest\_proof \= write\_path\_proof(manifest)  
 discovery \= META\_ROOT / "discovery\_artifact.md"  
 discovery.write\_text("\\n".join(\["\# HDE-EPIC035 Discovery Artifact","","Repo loci were grounded by PF10, audit, and live repo validation. OPS-01 retained open-rails evidence is inspected only and not rerun. No full v2 runtime conformance, public expansion, PF09 status movement, epic closeout, raw payload persistence, or AI scope is claimed.",""\]), encoding="utf-8")  
 discovery\_proof \= write\_path\_proof(discovery)  
 rca \= META\_ROOT / "qa\_rca\_doc\_delta\_summary.md"  
 rca.write\_text("\\n".join(\["\# HDE-EPIC035 QA RCA and Doc Delta Summary","","Coverage vs plan:","- Step-0B through PO-014 are represented by check-scoped primary logs and path proofs under audit/qa/hde-epic035/checks/.","- qa-16-close-out-deliverables created this closeout assembly evidence.","","Doc deltas:","- Existing HDE-EPIC035 doc-delta surfaces remain audit/docdeltas/hde-epic035\_doc\_deltas.md and audit/qa/hde-epic035/00\_meta/doc\_deltas.md.","","Readiness posture:","- This artifact supports QA closeout review only. It does not perform PO closeout, board update, PF edit, merge, PF09 status movement, OPS completion, full runtime conformance, public expansion, raw payload persistence, or AI scope.",""\]), encoding="utf-8")  
 rca\_proof \= write\_path\_proof(rca)  
 return \[str(manifest), str(manifest\_proof), str(discovery), str(discovery\_proof), str(rca), str(rca\_proof)\], \[\], \[\]

CHECKS \= {  
 "step-0b-doc-delta-capture": ("Step-0B — Doc Delta Capture", check\_step0b),  
 "po-001": ("PO-001", check\_po001),  
 "po-002": ("PO-002", check\_po002),  
 "po-003": ("PO-003", check\_po003),  
 "po-004": ("PO-004", check\_po004),  
 "po-005": ("PO-005", check\_po005),  
 "po-006": ("PO-006", check\_po006),  
 "po-007": ("PO-007", check\_po007),  
 "po-008": ("PO-008", check\_po008),  
 "po-009": ("PO-009", check\_po009),  
 "po-010": ("PO-010", check\_po010),  
 "po-011": ("PO-011", check\_po011),  
 "po-012": ("PO-012", check\_po012),  
 "po-013": ("PO-013", check\_po013),  
 "po-014": ("PO-014", check\_po014),  
 "qa-16-close-out-deliverables": ("Close-out deliverables", check\_closeout),  
 }

def run(check\_id: str) \-\> int:  
 if check\_id not in CHECKS:  
 print(f"UNKNOWN\_CHECK:{check\_id}", file=sys.stderr)  
 return 99  
 check\_name, fn \= CHECKS\[check\_id\]  
 check\_root \= CHECKS\_ROOT / check\_id  
 check\_root.mkdir(parents=True, exist\_ok=True)  
 primary \= check\_root / "primary.log"  
 proof \= Path(str(primary) \+ ".path\_proof.txt")  
 command \= f"python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py {check\_id}"  
 body \= \[f"check\_id={check\_id}", f"check\_name={check\_name}", f"command={command}", "rails=SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev", "pins=LC\_ALL=C LANG=C TZ=UTC"\]  
 status \= "PASS"  
 exit\_code \= 0  
 artifacts \= \[\]  
 intended \= \[\]  
 claimed \= \[\]  
 try:  
 artifacts, intended, claimed \= fn(body)  
 except ToolingBlocked as exc:  
 status \= "TOOLING\_BLOCKED"; exit\_code \= 99; claimed \= \[\]; body.append(f"TOOLING\_BLOCKED:{exc}")  
 except FailTooling as exc:  
 status \= "FAIL\_TOOLING"; exit\_code \= 2; claimed \= \[\]; body.append(f"FAIL\_TOOLING:{exc}")  
 except FailBehavior as exc:  
 status \= "FAIL\_BEHAVIOR"; exit\_code \= 1; claimed \= \[\]; body.append(f"FAIL\_BEHAVIOR:{exc}")  
 except Exception as exc:  
 status \= "FAIL\_TOOLING"; exit\_code \= 2; claimed \= \[\]; body.append(f"FAIL\_TOOLING:{type(exc).**name**}:{exc}")  
 if status \!= "PASS":  
 claimed \= \[\]  
 evidence \= \[str(primary), str(proof)\] \+ artifacts  
 header \= {  
 "schema\_version": "pf27.step\_log\_header.v1",  
 "timestamp\_utc": utc\_now(),  
 "check\_id": check\_id,  
 "check\_name": check\_name,  
 "status": status,  
 "fail\_status": "" if status \== "PASS" else status,  
 "command": command,  
 "command\_provenance": "Copy/paste from plan via QA-created helper",  
 "exit\_code": exit\_code,  
 "evidence\_artifacts": evidence,  
 "captured\_env": {"SAFE\_MODE":"1","ALLOW\_NETWORK":"0","APP\_ENV":"dev","LC\_ALL":"C","LANG":"C","TZ":"UTC"},  
 "pf\_refs": \["PF10 — HDE-Build Notes","PF19 — Glow QA Guide","PF27 — Canon Plan Templates"\],  
 "intended\_tokens": intended,  
 "claimed\_tokens": claimed,  
 }  
 primary.write\_text(json.dumps(header, ensure\_ascii=False) \+ "\\n" \+ "\\n".join(body) \+ "\\n", encoding="utf-8")  
 write\_path\_proof(primary)  
 print(f"{check\_id} status={status} exit\_code={exit\_code} primary={primary}")  
 return exit\_code

if **name** \== "**main**":  
 if len(sys.argv) \!= 2:  
 print("usage: hde035\_live\_qa\_harness.py \<check\_id\>", file=sys.stderr)  
 raise SystemExit(99)  
 raise SystemExit(run(sys.argv\[1\]))  
 PY

Command 2:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py step-0b-doc-delta-capture

What to look for:

* step-0b-doc-delta-capture status=PASS exit\_code=0.  
* audit/docdeltas/hde-epic035\_doc\_deltas.md exists.  
* audit/qa/hde-epic035/00\_meta/doc\_deltas.md exists.  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py exists.  
* audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt exists.  
* CAVEATS are recorded and no BLOCKERS are recorded.

Required deliverables:

* audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log  
* audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt  
* audit/docdeltas/hde-epic035\_doc\_deltas.md  
* audit/docdeltas/hde-epic035\_doc\_deltas.md.path\_proof.txt  
* audit/qa/hde-epic035/00\_meta/doc\_deltas.md  
* audit/qa/hde-epic035/00\_meta/doc\_deltas.md.path\_proof.txt  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py

PASS criteria tied to deliverables:

* PASS if both doc-delta surfaces exist and are path-proven.  
* PASS if the QA helper exists under audit/qa/hde-epic035/00\_meta/.  
* PASS if the primary log has the required PF27 header and sibling path proof.  
* PASS may claim DOC\_DELTA\_PRESENT\_OK.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if Python or audit/ write access is unavailable.  
* FAIL\_TOOLING if the helper, doc-delta surfaces, primary log, or path proofs cannot be written.  
* FAIL\_BEHAVIOR if Step-0B silently drops known planning caveats or claims product/OPS/PF09/closeout completion.

#### CHECK po-001: PO-001

Surface / D-goal mapping: D1 / vendor outcome mapping Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that vendor outcome mapping classifies expected provider response categories deterministically and without exposing raw vendor data.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-001/primary.log.  
3. Confirm status=PASS and exit\_code=0 in the header.  
4. Confirm provider outcome categories include unauthorized, rate-limited, unavailable, and network error records.  
5. Confirm raw vendor payload and live-conformance nonclaims are preserved.  
6. Open audit/qa/hde-epic035/checks/po-001/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-001

What to look for:

* JSON\_OK entries for artifact\_kind, epic\_id, and pf09\_subtask\_id.  
* JSON\_RECORD\_OK entries for PROVIDER\_UNAUTHORIZED, PROVIDER\_RATE\_LIMITED, and PROVIDER\_UNAVAILABLE.  
* JSON\_OK no\_claims includes no full runtime conformance, no live vendor call, no open-rails OPS execution, no public route expansion, and no raw vendor payload persistence.

Required deliverables:

* audit/qa/hde-epic035/checks/po-001/primary.log  
* audit/qa/hde-epic035/checks/po-001/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if provider outcome mapping is deterministic and includes expected provider outcome classifications.  
* PASS if no raw vendor payload exposure or full runtime conformance claim is present.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if provider outcome categories are missing, collapsed, or incorrectly classified.  
* FAIL\_BEHAVIOR if raw vendor payload or full runtime conformance is claimed.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-002: PO-002

Surface / D-goal mapping: D2 / retry and rate-limit interpretation Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that retry and rate-limit interpretation is bounded, deterministic, and distinguishes retryable from non-retryable provider outcomes.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/rate\_limit\_headers.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/rate\_limit\_headers.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-002/primary.log.  
3. Confirm status=PASS and exit\_code=0.  
4. Confirm rate-limit status 429 is bounded and non-retryable.  
5. Confirm Retry-After cases cover delta seconds, HTTP date, invalid, and overflow.  
6. Open audit/qa/hde-epic035/checks/po-002/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-002

What to look for:

* JSON\_OK rate\_limit\_status\_record.  
* JSON\_RECORD\_OK retry\_after\_records.case='delta\_seconds'.  
* JSON\_RECORD\_OK retry\_after\_records.case='http\_date'.  
* JSON\_RECORD\_OK retry\_after\_records.case='invalid'.  
* JSON\_RECORD\_OK retry\_after\_records.case='overflow'.

Required deliverables:

* audit/qa/hde-epic035/checks/po-002/primary.log  
* audit/qa/hde-epic035/checks/po-002/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/rate\_limit\_headers.snapshot.json

PASS criteria tied to deliverables:

* PASS if retry and rate-limit evidence is bounded and deterministic.  
* PASS if retryable and non-retryable provider outcomes remain distinct.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if retry/rate-limit cases are missing, unbounded, or misclassified.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-003: PO-003

Surface / D-goal mapping: D3 / malformed responses, network failures, unexpected statuses, redirect-like responses Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that malformed responses, network failures, unexpected provider statuses, and redirect-like responses are classified without collapsing them into generic vendor unavailability.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-003/primary.log.  
3. Confirm malformed\_json\_response and provider\_bad\_response are present.  
4. Confirm network\_error is distinct.  
5. Confirm status 302 is classified as http\_status\_other / provider error, not generic provider unavailable.  
6. Open audit/qa/hde-epic035/checks/po-003/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-003

What to look for:

* JSON\_RECORD\_OK bad\_response\_records.scenario='malformed\_json\_response'.  
* JSON\_RECORD\_OK bad\_response\_records.scenario='provider\_bad\_response'.  
* JSON\_RECORD\_OK status\_mapping\_records.status=302.  
* JSON\_OK retry\_classification includes network\_error=true and redirect\_response=false.

Required deliverables:

* audit/qa/hde-epic035/checks/po-003/primary.log  
* audit/qa/hde-epic035/checks/po-003/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if malformed, network, unexpected status, and redirect-like outcomes are separately classified.  
* PASS if they are not collapsed into generic vendor unavailability.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if distinct outcome classes are missing or collapsed.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-004: PO-004

Surface / D-goal mapping: D4 / bounded observability and secret safety Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that recorded observability preserves only bounded labels and safe classifications, not raw request bodies, raw response bodies, raw secrets, or uncontrolled vendor payloads.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json  
* test \-f artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-004/primary.log.  
3. Confirm bounded\_labels\_only, keys\_only, no\_plaintext\_secret\_value, no\_raw\_request\_body, no\_raw\_response\_body, no\_raw\_secret\_header, and no\_raw\_vendor\_payload are true.  
4. Confirm response mapping does not emit payload bodies.  
5. Open audit/qa/hde-epic035/checks/po-004/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-004

What to look for:

* OBSERVABILITY\_OK entries for each bounded observability field.  
* JSON\_OK data\_payload\_body\_emitted=False.  
* No raw request, response, secret, or vendor payload persistence.

Required deliverables:

* audit/qa/hde-epic035/checks/po-004/primary.log  
* audit/qa/hde-epic035/checks/po-004/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if only bounded labels and safe classifications are recorded.  
* PASS if no raw request body, response body, secret, or vendor payload is persisted.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if raw secret-bearing or raw vendor payload material is persisted.  
* FAIL\_BEHAVIOR if observability is not bounded.  
* TOOLING\_BLOCKED if a required snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-005: PO-005

Surface / D-goal mapping: D5 / route family distinction Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF05 — HDE CLI/API Vendor Reference; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that the v2 chart route family and legacy BodyGraph route family remain distinct in authentication, route intent, and proof meaning.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-005/primary.log.  
3. Confirm legacy BodyGraph routes use HD-Api-Key redacted posture.  
4. Confirm v2 chart routes use Authorization: Bearer redacted posture.  
5. Confirm bodygraphs, bodygraphs/simple, charts, charts/simple, and charts/coordinates are listed as distinct resource paths.  
6. Open audit/qa/hde-epic035/checks/po-005/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-005

What to look for:

* ROUTE\_FAMILY\_OK bodygraphs.  
* ROUTE\_FAMILY\_OK bodygraphs/simple.  
* ROUTE\_FAMILY\_OK charts.  
* ROUTE\_FAMILY\_OK charts/simple.  
* ROUTE\_FAMILY\_OK charts/coordinates.  
* Distinct auth postures are preserved.

Required deliverables:

* audit/qa/hde-epic035/checks/po-005/primary.log  
* audit/qa/hde-epic035/checks/po-005/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/error\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if v2 chart and legacy BodyGraph route families remain distinct.  
* PASS if authentication posture and route identity are not mixed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if v2 chart and legacy BodyGraph routes are conflated or auth posture is mixed.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-006: PO-006

Surface / D-goal mapping: D6 / simple v2 chart observation scope Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: retained OPS evidence inspection; no OPS rerun.

Intent:

Verify that the simple v2 chart observation proves only the narrow live behavior it actually exercised, not full BodyGraph-detail resolution or full vendor conformance.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt  
* test \-f audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.  
* This check inspects retained OPS-01 evidence only; it must not rerun OPS.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-006/primary.log.  
3. Confirm v2\_charts\_simple=success.  
4. Confirm v2\_charts\_simple\_request\_shape=/v2/charts/simple.  
5. Confirm v2\_charts\_simple\_response\_type=ChartSimpleResult.  
6. Confirm full\_runtime\_conformance\_claim=false and ops\_completion\_claim=false.  
7. Open audit/qa/hde-epic035/checks/po-006/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-006

What to look for:

* TEXT\_OK final\_classification v2\_charts\_simple=success.  
* TEXT\_OK final\_classification v2\_charts\_simple\_response\_type=ChartSimpleResult.  
* TEXT\_OK ops\_evidence\_binding full\_runtime\_conformance\_claim=false.  
* TEXT\_OK ops\_evidence\_binding ops\_completion\_claim=false.

Required deliverables:

* audit/qa/hde-epic035/checks/po-006/primary.log  
* audit/qa/hde-epic035/checks/po-006/primary.log.path\_proof.txt  
* audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if retained simple v2 chart evidence is scoped to /v2/charts/simple and ChartSimpleResult only.  
* PASS if the evidence does not claim full BodyGraph-detail resolution or full vendor conformance.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if simple chart observation is treated as full BodyGraph-detail resolution or full runtime conformance.  
* TOOLING\_BLOCKED if required retained OPS evidence or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-007: PO-007

Surface / D-goal mapping: D7 / BodyGraph-resolution workflow route-policy gap Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF05 — HDE CLI/API Vendor Reference; PF19 — Glow QA Guide Proof class: retained OPS evidence inspection; no OPS rerun.

Intent:

Verify that the current vendor-backed BodyGraph-resolution workflow is treated as a recorded runtime gap until a future explicit vendor-route policy proves the correct BodyGraph-detail path.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt  
* test \-f audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.  
* This check must not execute hdctl bg:resolve because the CLI help/parser locus was not isolated by the repo audit and OPS evidence is retained evidence only.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-007/primary.log.  
3. Confirm bg\_resolve\_error\_code=PROVIDER\_NOT\_FOUND.  
4. Confirm bg\_resolve\_http\_status=404.  
5. Confirm runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base.  
6. Confirm the OPS binding records the same gap.  
7. Open audit/qa/hde-epic035/checks/po-007/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-007

What to look for:

* TEXT\_OK final\_classification bg\_resolve\_error\_code=PROVIDER\_NOT\_FOUND.  
* TEXT\_OK final\_classification bg\_resolve\_http\_status=404.  
* TEXT\_OK final\_classification runtime\_gap=bg:resolve\_still\_uses\_legacy\_bodygraph\_route\_against\_configured\_v2\_base.  
* TEXT\_OK ops\_evidence\_binding bg\_resolve\_runtime\_gap.

Required deliverables:

* audit/qa/hde-epic035/checks/po-007/primary.log  
* audit/qa/hde-epic035/checks/po-007/primary.log.path\_proof.txt  
* audit/ops/hde-epic035/ops-01/hdapi-v2-open-rails-smoke/final\_classification.txt  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if the current BodyGraph-resolution workflow is recorded as a runtime gap.  
* PASS if no completed v2 BodyGraph-detail route-policy proof is claimed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if the evidence claims current bg:resolve is the completed correct v2 BodyGraph-detail route.  
* TOOLING\_BLOCKED if required retained evidence or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-008: PO-008

Surface / D-goal mapping: D8 / response-normalization exact adapter/schema gap Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that the response-normalization proof preserves the exact adapter/schema gap rather than inferring compatibility from partial or nearby vendor responses.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-008/primary.log.  
3. Confirm response\_normalization\_posture=EXACT\_SCHEMA\_ADAPTER\_GAP\_RECORDED.  
4. Confirm schema\_gap\_status=GAP\_RECORDED.  
5. Confirm normalized\_data\_path\_proof\_claim=NONE.  
6. Open audit/qa/hde-epic035/checks/po-008/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-008

What to look for:

* JSON\_OK response\_normalization\_posture='EXACT\_SCHEMA\_ADAPTER\_GAP\_RECORDED'.  
* JSON\_OK schema\_gap\_status='GAP\_RECORDED'.  
* JSON\_OK normalized\_data\_path\_proof\_claim='NONE'.  
* TEXT\_OK schema gap summary.

Required deliverables:

* audit/qa/hde-epic035/checks/po-008/primary.log  
* audit/qa/hde-epic035/checks/po-008/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if response-normalization posture records exact adapter/schema gap.  
* PASS if compatibility is not inferred from nearby or partial vendor responses.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if normalized data path proof or runtime compatibility is claimed without adapter/schema proof.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-009: PO-009

Surface / D-goal mapping: D9 / simple chart data insufficiency Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that simple chart data is not treated as sufficient BodyGraph-detail data unless a future proof demonstrates that all required internal fields are covered.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-009/primary.log.  
3. Confirm ChartSimpleResult appears only inside the gap posture.  
4. Confirm ChartResult/ChartSimpleResult-to-BodyGraph adapter gap is recorded.  
5. Confirm no\_compatibility\_by\_inference=True.  
6. Open audit/qa/hde-epic035/checks/po-009/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-009

What to look for:

* TEXT\_OK ChartSimpleResult.  
* TEXT\_OK ChartResult/ChartSimpleResult-to-BodyGraph adapter.  
* TEXT\_OK schema\_gap\_recorded.  
* JSON\_OK no\_compatibility\_by\_inference=True.

Required deliverables:

* audit/qa/hde-epic035/checks/po-009/primary.log  
* audit/qa/hde-epic035/checks/po-009/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if simple chart data is not treated as sufficient BodyGraph-detail data.  
* PASS if compatibility remains blocked on future proof.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if simple chart data is treated as sufficient internal BodyGraph/person/cache/compute data.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-010: PO-010

Surface / D-goal mapping: D10 / future runtime adapter/schema proof requirement Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that future runtime compatibility requires a bounded adapter or schema proof before v2 chart data is claimed to feed the existing BodyGraph, person, cache, or compute contract.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-010/primary.log.  
3. Confirm required\_follow\_up requires bounded adapter/schema proof.  
4. Confirm runtime\_conformance\_claim=NONE.  
5. Confirm normalized\_data\_path\_proof\_claim=NONE.  
6. Open audit/qa/hde-epic035/checks/po-010/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-010

What to look for:

* TEXT\_OK required\_follow\_up adapter/schema proof.  
* JSON\_OK runtime\_conformance\_claim='NONE'.  
* JSON\_OK normalized\_data\_path\_proof\_claim='NONE'.

Required deliverables:

* audit/qa/hde-epic035/checks/po-010/primary.log  
* audit/qa/hde-epic035/checks/po-010/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if future compatibility is explicitly blocked on bounded adapter/schema proof.  
* PASS if no runtime conformance or normalized data path proof is claimed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if future runtime compatibility is claimed without bounded adapter/schema proof.  
* TOOLING\_BLOCKED if the snapshot or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-011: PO-011

Surface / D-goal mapping: D11 / evidence-loop binding Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that the evidence loop binds provider-outcome mapping, response-normalization gap, and retained live observation into one coherent governed proof posture.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* artifacts/vendor/hdapi\_v2/release\_binding.snapshot.json  
* docs/acceptance\_map\_epic035.json  
* audit/qa/hde-epic035/token\_evidence\_matrix.md

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f artifacts/vendor/hdapi\_v2/release\_binding.snapshot.json  
* test \-f docs/acceptance\_map\_epic035.json  
* test \-f audit/qa/hde-epic035/token\_evidence\_matrix.md

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-011/primary.log.  
3. Confirm release binding includes pr01\_hde\_ferm008\_3\_provider\_outcome.  
4. Confirm release binding includes pr02\_hde\_ferm008\_4\_response\_normalization.  
5. Confirm acceptance map references ops\_01 and HDE-FERM008.5 governed evidence-loop closure.  
6. Confirm token matrix references HDE-FERM008.5 evidence-loop closure posture.  
7. Open audit/qa/hde-epic035/checks/po-011/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-011

What to look for:

* TEXT\_OK pr01\_hde\_ferm008\_3\_provider\_outcome.  
* TEXT\_OK pr02\_hde\_ferm008\_4\_response\_normalization.  
* TEXT\_OK ops\_01.  
* TEXT\_OK HDE-FERM008.5 governed evidence-loop closure.  
* TEXT\_OK token matrix HDE-FERM008.5 evidence-loop closure posture.

Required deliverables:

* audit/qa/hde-epic035/checks/po-011/primary.log  
* audit/qa/hde-epic035/checks/po-011/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/release\_binding.snapshot.json  
* docs/acceptance\_map\_epic035.json  
* audit/qa/hde-epic035/token\_evidence\_matrix.md

PASS criteria tied to deliverables:

* PASS if provider-outcome mapping, response-normalization gap, and retained live observation are bound into a coherent governed evidence-loop posture.  
* PASS if the binding avoids full runtime conformance and closeout/status overclaims.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if evidence-loop binding is missing, incoherent, or overclaims.  
* TOOLING\_BLOCKED if required binding artifacts or helper are missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-012: PO-012

Surface / D-goal mapping: D12 / evidence category separation Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that the evidence loop preserves the distinction between implementation evidence, operational observation, QA evidence, status movement, and closeout.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* docs/acceptance\_map\_epic035.json  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f docs/acceptance\_map\_epic035.json  
* test \-f audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-012/primary.log.  
3. Confirm QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, and epic closeout appear as nonclaims in the acceptance map.  
4. Confirm ops\_evidence\_binding has qa\_pass\_claim=false, pf09\_status\_movement\_claim=false, and epic\_closeout\_claim=false.  
5. Open audit/qa/hde-epic035/checks/po-012/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-012

What to look for:

* TEXT\_OK QA PASS.  
* TEXT\_OK OPS completion.  
* TEXT\_OK PF09 status movement.  
* TEXT\_OK HDE-FERM008 parent Done.  
* TEXT\_OK epic closeout.  
* TEXT\_OK qa\_pass\_claim=false.  
* TEXT\_OK pf09\_status\_movement\_claim=false.  
* TEXT\_OK epic\_closeout\_claim=false.

Required deliverables:

* audit/qa/hde-epic035/checks/po-012/primary.log  
* audit/qa/hde-epic035/checks/po-012/primary.log.path\_proof.txt  
* docs/acceptance\_map\_epic035.json  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if implementation evidence, OPS observation, QA evidence, PF09 status movement, and closeout remain distinct.  
* PASS if no QA PASS, OPS completion, PF09 status movement, HDE-FERM008 parent Done, or epic closeout is claimed by implementation or OPS evidence.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if evidence categories are collapsed or closeout/status movement is claimed.  
* TOOLING\_BLOCKED if required evidence or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-013: PO-013

Surface / D-goal mapping: D13 / explicit nonclaims Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide Proof class: closed-rails governed artifact inspection.

Intent:

Verify that the epic does not claim full vendor runtime conformance, public-surface expansion, app-side vendor ownership, raw payload persistence, or AI scope.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* docs/acceptance\_map\_epic035.json  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f docs/acceptance\_map\_epic035.json  
* test \-f artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* test \-f audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B has run successfully.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-013/primary.log.  
3. Confirm full HumanDesignAPI v2 runtime conformance is a nonclaim.  
4. Confirm public Reader, route, flag, payload/transport, and new HTTP home are nonclaims.  
5. Confirm app-side credential ownership, raw payload persistence, and AI scope are nonclaims.  
6. Open audit/qa/hde-epic035/checks/po-013/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-013

What to look for:

* TEXT\_OK full HumanDesignAPI v2 runtime conformance.  
* TEXT\_OK public Reader change.  
* TEXT\_OK public route.  
* TEXT\_OK new HTTP home.  
* TEXT\_OK app-side HumanDesignAPI credential ownership.  
* TEXT\_OK raw payload persistence.  
* TEXT\_OK AI scope.  
* JSON\_OK ai\_scope\_claim='NONE'.  
* TEXT\_OK full\_runtime\_conformance\_claim=false.  
* TEXT\_OK ai\_scope\_claim=false.

Required deliverables:

* audit/qa/hde-epic035/checks/po-013/primary.log  
* audit/qa/hde-epic035/checks/po-013/primary.log.path\_proof.txt  
* docs/acceptance\_map\_epic035.json  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json  
* audit/qa/hde-epic035/ops-01/ops\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if forbidden runtime, public-surface, app-side, raw-payload, and AI claims remain absent.  
* PASS if those boundaries are recorded as nonclaims.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if any forbidden claim is present.  
* TOOLING\_BLOCKED if required evidence or helper is missing.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK po-014: PO-014

Surface / D-goal mapping: D14 / current repo evidence coherence Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide; PF05 — HDE CLI/API Vendor Reference Proof class: closed-rails targeted tests and governed evidence gates.

Intent:

Verify that current repo evidence remains coherent with PF10’s recorded scope boundaries before proof coverage is drafted around this epic.

Dependencies required:

* Python  
* pytest  
* bash  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* tests/evidence/test\_hdapi\_v2\_live\_conformance.py  
* tests/evidence/test\_hdapi\_v2\_response\_normalization.py  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* tests/evidence/test\_hde\_epic035\_pr03\_evidence\_loop.py  
* tools/evidence/validate\_evidence\_paths.py  
* tools/evidence/check\_lf\_endings.py  
* tools/evidence/update\_evidence\_index.py  
* ci/checks/check\_mirror\_schema.sh  
* ci/checks/check\_evidence\_index\_hash.sh  
* ci/checks/check\_final\_lf.sh  
* docs/evidence/INDEX.json  
* docs/evidence/INDEX.sha256  
* artifacts/evidence\_index.jsonl  
* artifacts/evidence\_index.jsonl.sha256  
* docs/acceptance\_map\_epic035.json

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* python \-c "import pytest"  
* test \-f tests/evidence/test\_hdapi\_v2\_live\_conformance.py  
* test \-f tests/evidence/test\_hdapi\_v2\_response\_normalization.py  
* test \-f tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* test \-f tests/evidence/test\_hde\_epic035\_pr03\_evidence\_loop.py  
* test \-f tools/evidence/validate\_evidence\_paths.py  
* test \-f tools/evidence/check\_lf\_endings.py  
* test \-f tools/evidence/update\_evidence\_index.py  
* test \-f ci/checks/check\_mirror\_schema.sh  
* test \-f ci/checks/check\_evidence\_index\_hash.sh  
* test \-f ci/checks/check\_final\_lf.sh

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B and PO-001 through PO-013 have run or have been explicitly dispositioned.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic035/checks/po-014/primary.log.  
3. Confirm PYTEST\_IMPORT\_OK is present.  
4. Confirm targeted pytest command exited 0\.  
5. Confirm validate\_evidence\_paths.py exited 0\.  
6. Confirm check\_lf\_endings.py exited 0\.  
7. Confirm update\_evidence\_index.py \--check exited 0\.  
8. Confirm check\_mirror\_schema.sh exited 0\.  
9. Confirm check\_evidence\_index\_hash.sh exited 0\.  
10. Confirm check\_final\_lf.sh exited 0\.  
11. Confirm the primary log header claims only the intended existing governed tokens when status is PASS.  
12. Open audit/qa/hde-epic035/checks/po-014/primary.log.path\_proof.txt.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py po-014

What to look for:

* PYTEST\_IMPORT\_OK.  
* Exit code 0 for targeted pytest.  
* Exit code 0 for tools/evidence/validate\_evidence\_paths.py.  
* Exit code 0 for tools/evidence/check\_lf\_endings.py.  
* Exit code 0 for tools/evidence/update\_evidence\_index.py \--check.  
* Exit code 0 for ci/checks/check\_mirror\_schema.sh.  
* Exit code 0 for ci/checks/check\_evidence\_index\_hash.sh.  
* Exit code 0 for ci/checks/check\_final\_lf.sh.  
* JSON\_CANONICAL\_OK for docs/acceptance\_map\_epic035.json and the HDE-EPIC035 vendor snapshots.  
* claimed\_tokens includes only EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK, JSON\_CANONICAL\_CHECK\_OK, and TESTS\_PASS\_OK when status is PASS.

Required deliverables:

* audit/qa/hde-epic035/checks/po-014/primary.log  
* audit/qa/hde-epic035/checks/po-014/primary.log.path\_proof.txt  
* tests/evidence/test\_hdapi\_v2\_live\_conformance.py  
* tests/evidence/test\_hdapi\_v2\_response\_normalization.py  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* tests/evidence/test\_hde\_epic035\_pr03\_evidence\_loop.py  
* docs/evidence/INDEX.json  
* docs/evidence/INDEX.sha256  
* artifacts/evidence\_index.jsonl  
* artifacts/evidence\_index.jsonl.sha256  
* docs/acceptance\_map\_epic035.json

PASS criteria tied to deliverables:

* PASS if targeted tests exit 0\.  
* PASS if evidence-path, LF, evidence-index, mirror-schema, hash, and final-LF checks exit 0\.  
* PASS if canonical JSON checks pass for the HDE-EPIC035 acceptance map and vendor snapshots.  
* PASS if the acceptance map contains the existing governed token names.  
* PASS requires the primary log sibling path proof.  
* PASS may claim EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK, JSON\_CANONICAL\_CHECK\_OK, and TESTS\_PASS\_OK.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if a targeted test or governed evidence check executes and reports mismatch.  
* TOOLING\_BLOCKED if Python, pytest, bash, a required script, a required test, or a required governed evidence file is missing.  
* FAIL\_TOOLING if a command cannot execute due to tooling or invocation failure.  
* FAIL\_TOOLING if the primary log or path proof cannot be written.

#### CHECK qa-16-close-out-deliverables: Close-out deliverables

Surface / D-goal mapping: D15 / QA closeout packaging Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev Pins: LC\_ALL=C LANG=C TZ=UTC PF anchors: PF27 — Canon Plan Templates; PF19 — Glow QA Guide Proof class: QA closeout evidence assembly; no PO closeout, no PF edit, no board update, no merge.

Intent:

Produce the PF27-required closeout execution deliverables: QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary. This check does not perform PO closeout and does not claim epic closure.

Dependencies required:

* Python  
* audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* primary.log and primary.log.path\_proof.txt for step-0b-doc-delta-capture and po-001 through po-014

Preflight check:

* test \-f audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py  
* test \-f audit/qa/hde-epic035/checks/step-0b-doc-delta-capture/primary.log  
* test \-f audit/qa/hde-epic035/checks/po-014/primary.log

Activation or installation remediation, if allowed:

* No installation action is allowed in this plan.

If still unavailable:

* Classify as TOOLING\_BLOCKED.

Preconditions:

* Step-0B and PO-001 through PO-014 have run or have been explicitly dispositioned.

Setup:

* None.

Numbered PO actions:

1. Confirm Step-0B and PO-001 through PO-014 have produced primary logs and sibling path proofs.  
2. Run the command below.  
3. Open audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log.  
4. Confirm manifest= audit/qa/hde-epic035/qa\_step\_logs\_manifest.json is recorded.  
5. Open audit/qa/hde-epic035/qa\_step\_logs\_manifest.json.  
6. Confirm every expected check from Step-0B through PO-014 appears with status, log\_path, and path\_proof\_path.  
7. Open audit/qa/hde-epic035/00\_meta/discovery\_artifact.md.  
8. Open audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md.  
9. Confirm the summary does not claim PO closeout, board update, PF edit, PF09 status movement, full runtime conformance, public expansion, raw payload persistence, OPS completion, or AI scope.

Command 1:

SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic035/00\_meta/hde035\_live\_qa\_harness.py qa-16-close-out-deliverables

What to look for:

* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json exists.  
* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json.path\_proof.txt exists.  
* audit/qa/hde-epic035/00\_meta/discovery\_artifact.md exists.  
* audit/qa/hde-epic035/00\_meta/discovery\_artifact.md.path\_proof.txt exists.  
* audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md exists.  
* audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt exists.  
* qa-16 primary log status is PASS only if all prior check primary logs and path proofs exist.  
* closeout artifacts preserve nonclaims and do not claim formal epic closeout.

Required deliverables:

* audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log  
* audit/qa/hde-epic035/checks/qa-16-close-out-deliverables/primary.log.path\_proof.txt  
* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic035/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic035/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt

PASS criteria tied to deliverables:

* PASS if the QA step-log manifest exists and lists every expected check with status, log\_path, and path\_proof\_path.  
* PASS if the manifest path proof exists and matches the manifest path.  
* PASS if the discovery artifact exists and records no invented loci.  
* PASS if the QA RCA / Doc Delta summary exists and includes coverage vs plan accounting.  
* PASS if the qa-16 primary log has a PF27 header and sibling path proof.  
* PASS does not claim PO closeout.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if one or more expected prior check primary logs or sibling path proofs is missing.  
* FAIL\_TOOLING if a primary log exists but has an unreadable header.  
* FAIL\_TOOLING if closeout deliverables cannot be written.  
* FAIL\_BEHAVIOR if closeout deliverables claim PO closeout, runtime vendor conformance, public Reader expansion, new HTTP home, AI scope, PF edits, product implementation, or PF09 status movement.

### Close-out deliverables

The final check produces:

* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic035/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic035/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic035/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic035/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt

The QA RCA / Doc Delta summary is a closure-oriented QA artifact. It states what Live QA found, records doc-delta posture, maps coverage vs plan, preserves deferrals, and states readiness posture for QA review. It does not edit PF documents, move PF09 status, perform close-pack finalization, or claim epic closeout.

### Review guardrails

Hard blockers for plan execution:

* A required repo-resident executable locus is absent or unproven.  
* A required pre-existing governed artifact is missing.  
* Python is unavailable.  
* pytest is unavailable for PO-014.  
* A required script or test path is missing for PO-014.  
* A check needs open-rails or vendor IO to evaluate its predicate.  
* A check would require editing product code, PF documents, public contracts, acceptance tokens, evidence generators, or governed non-QA-root artifacts.  
* The helper cannot write primary.log or sibling path proof under the stable check directory.  
* A step attempts to claim full HumanDesignAPI v2 runtime conformance, HDE-FERM008 parent completion, PF09 status movement, public-surface expansion, app-side vendor credential ownership, raw payload persistence, AI scope, OPS completion, QA PASS before its check, or epic closeout.

Moon Loop posture:

* Moon Loop may repair only QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under audit/qa/hde-epic035/.  
* Moon Loop must preserve the failed or blocked primary log state in the same evidence stream and record what changed.  
* Moon Loop must not modify product code, repo tests, repo evidence generators, governed artifacts outside the approved QA root, public contracts, PF documents, acceptance tokens, or multiple subsystems.  
* Non-QA-root remediation requires an approved PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE route before the changed state can support final PASS-grade QA.

Future-step artifacts:

* All check-scoped artifacts listed in this plan are NOT RUN until the producing step executes.  
* NOT RUN / DEFERRED is not a missing-evidence failure before execution.  
* Missing-evidence failures apply only after a producing step executes and the required artifact is absent or unproven.

ASK OK?  
