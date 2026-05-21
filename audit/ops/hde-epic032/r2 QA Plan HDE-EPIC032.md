Epic ID: HDE-EPIC032

Plan type: Live QA Plan / Runbook

Execution venue: Codespaces

Target environment: dev

Plan revision: r2

Date (UTC): 2026-05-21

Operators (names-only): PO, Kronos

Canon precedence statement

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

Canon set

Canon set, titles-only:

* PF10 — HDE-Build Notes, relevant addenda: 2.1 DB bridge/provider parity proof-label posture; 2.2 Template hygiene defects are non-blocking unless they affect truth, portability, evidence identity, or execution safety; 2.3 PR-01 HDE-EPIC032; 2.4 PR-02 HDE-EPIC032; 2.5 PR-03 HDE-EPIC032; 2.6 OPS-01 HDE-EPIC032; 2.7 PR-04 HDE-EPIC032; 2.8 HDE-EPIC032 Audit Review; 2.9 HDE-EPIC032 Implementation Retrospective; 2.10 HDE-EPIC032 ADR — HDE-FERM004.2 combined-evidence supportability decision  
* PF04 — HDE-Governance, acceptance-token roster and token-claim invariants  
* PF05 — HDE CLI/API Vendor Reference, typed public error and public Reader contract posture  
* PF06 — Epic Process Guide, Discovery and QA RCA / Doc Delta expectations  
* PF09.5 — HDE Build Checklist Fermentation, active Fermentation row context only  
* PF12 — HDE Schemas and Artifacts, Human Evidence Index and Machine Mirror posture  
* PF14 — HDE Mechanics Guide, narrative router, narrative registry, and persistence-layer posture  
* PF17 — HDE Narratives Guide, Reader v1 and deterministic narrative posture  
* PF19 — Glow QA Guide, rails, evidence, step logs, and Live QA posture  
* PF23 — Reality Audits, planning-time repo-reality context only  
* PF27 — Canon Plan Templates, Live QA Plan structure and template obligations

Scope statement

This plan evaluates the following in-scope surfaces / checks:

* Step-0A Discovery posture and Live QA harness setup  
* Step-0B Doc Delta Capture  
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
* PO-015  
* PO-016  
* PO-017  
* PO-018  
* PO-019  
* PO-020  
* PO-021  
* PO-022  
* PO-023  
* PO-024

This plan explicitly excludes:

* Implementation work  
* Remediation implementation work beyond bounded Moon Loop evidence-harness or evidence-posture correction  
* PF document editing  
* Git branch, commit, PR, rebase, checkout, or merge workflow  
* Live provider execution  
* Vendor-version runtime conformance claims  
* Public Reader expansion  
* New public routes, public flags, public payload fields, or public Reader contract changes  
* Acceptance-token creation or token overclaim  
* Permanent PF09.5 checklist drainage  
* Formal epic close-pack completion

PF10 overrides / conflicts

* PF10 Addendum 2.1 → `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are non-token proof labels for HDE-EPIC032 unless Governance later registers them; `DEV_DB_BRIDGE_FALLBACK_OK` remains the canonical dev bridge-fallback acceptance token where that exact scope applies → impacted PF04 and PF09.5 references.  
* PF10 Addendum 2.2 → template hygiene defects do not block HDE-EPIC032 planning unless they affect truth, portability, evidence identity, execution safety, acceptance-token truth, source authority, public/private surface posture, or closeout truth → impacted PF27 review posture.  
* PF10 Addenda 2.3 through 2.7 → HDE-EPIC032 implementation evidence is scoped to narrative router parity/indexing, narrative registry diff/identity/indexing, database bridge/provider parity, operations support evidence, and database typed-failure/evidence coherence → impacted QA coverage scope.  
* PF10 Addendum 2.10 → combined evidence supports the HDE-FERM004.2 supportability decision while preserving separate checklist drainage and closeout posture → impacted PO-008 through PO-020 truth-class checks.

PF23 anchors

PF23 was consulted for planning-time repo-reality context and existence/locus framing only. It is not a required deliverable, required check, acceptance token, execution artifact, operator command source, or blocker source.

PF23-informed planning posture:

* Treat repo reality as inspectable but not assumed.  
* Do not require any PF23 consult artifact.  
* Do not claim `REALITY_AUDIT_OK`.  
* Treat the HDE-EPIC032 QA root as QA-created because repo discovery did not prove an existing `audit/qa/hde-epic032/` root or manifest.

Environment and rails posture

Determinism pins

Use these pins whenever producing governed bytes:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

Rails changes by check:

* None. Every check in this runbook is closed-rails and must remain SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev.

No VCS workflow content

This plan does not include branch, commit, pull request, checkout, merge, rebase, or working-tree cleanliness checks. Traceability comes from governed QA evidence under `audit/qa/hde-epic032/`, not VCS state.

PO inputs needed

Required external inputs:

* None.

Optional external inputs:

* None.

Secrets and credentials:

* Do not provide vendor keys.  
* Do not provide auth header values.  
* Do not provide database credentials.  
* Do not export live provider credentials.  
* Do not set live provider or production database bindings for this runbook.

If a required runtime prerequisite is missing, classify the affected check as TOOLING\_BLOCKED or FAIL\_TOOLING according to the step rule. Do not guess missing inputs.

Evidence posture and directory structure

Epic QA root normalization

Canonical epic QA root for this runbook:

* audit/qa/hde-epic032/

Check-centric, single-root evidence posture

* Live QA evidence is organized only by check\_id under `audit/qa/hde-epic032/checks/<check_id>/`.  
* Evidence paths are stable current-state paths.  
* Per-run roots, timestamped roots, run-id directories, and operator-set run-root variables are prohibited.  
* `run_id` and `RUN_ID` are prohibited as correctness keys.  
* Re-running a check overwrites the current-state evidence for that check under the same check directory.

Canonical current-state layout

* `audit/qa/hde-epic032/00_meta/`  
* `audit/qa/hde-epic032/checks/<check_id>/`  
* `audit/qa/hde-epic032/checks/<check_id>/primary.log`  
* `audit/qa/hde-epic032/checks/<check_id>/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`  
* `audit/docdeltas/hde-epic032_doc_deltas.md`  
* `audit/qa/hde-epic032/00_meta/doc_deltas.md`

Step-log header schema expectations

Every `primary.log` starts with a single-line JSON header containing at minimum:

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

For this runbook, every check is tokenless evidence unless a later approved close-stage process explicitly binds a registered token. The header fields must therefore use:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

Canonical step-log header writer

The following PF27 header-writer contract is included once as the canonical schema contract. The Step-0A QA-created harness writes the same required keys mechanically for every check.

`python - << 'PY'` `import datetime` `import json` `import os`

`def env(name: str, default: str = "") -> str:`     `value = os.environ.get(name)`     `return value if value is not None else default`

`def env_json(name: str, default):`     `raw = os.environ.get(name)`     `if raw is None or raw == "":`         `return default`     `return json.loads(raw)`

`schema_version = "pf27.step_log_header.v1"` `timestamp_utc = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"` `status = env("PASS_FAIL")` `fail_status = "" if status == "PASS" else status` `exit_code_raw = env("EXIT_CODE", "")` `exit_code = int(exit_code_raw) if exit_code_raw != "" else None` `if status == "PASS" and exit_code != 0:`     `raise SystemExit("PASS requires EXIT_CODE=0")` `commands = env_json("COMMANDS_JSON", [])` `if isinstance(commands, str):`     `commands = [commands]` `command = "; ".join(commands) if commands else "N/A"`

`header = {`     `"schema_version": schema_version,`     `"timestamp_utc": timestamp_utc,`     `"check_id": env("CHECK_ID"),`     `"check_name": env("CHECK_NAME"),`     `"status": status,`     `"fail_status": fail_status,`     `"command": command,`     `"command_provenance": env("COMMAND_PROVENANCE", "Explicitly created"),`     `"exit_code": exit_code,`     `"evidence_artifacts": env_json("ARTIFACTS_JSON", []),`     `"captured_env": {`         `"SAFE_MODE": env("SAFE_MODE"),`         `"ALLOW_NETWORK": env("ALLOW_NETWORK"),`         `"APP_ENV": env("APP_ENV"),`         `"LC_ALL": env("LC_ALL"),`         `"LANG": env("LANG"),`         `"TZ": env("TZ"),`     `},`     `"pf_refs": env_json("PF_REFS_JSON", []),`     `"intended_tokens": env_json("INTENDED_TOKENS_JSON", []),`     `"claimed_tokens": env_json("CLAIMED_TOKENS_JSON", []),` `}` `print(json.dumps(header, ensure_ascii=False))` `PY`

Mandatory Step-0 artifacts

Step-0A — Discovery posture and Live QA harness setup

Goal: Create the stable HDE-EPIC032 QA root, create the current-state manifest family, and create a QA-created embedded harness under the QA root. The harness is QA evidence scaffolding only; it is not product code and it does not create new implementation behavior.

Required dependencies:

* Python 3  
* Repository root in Codespaces  
* Existing repo loci referenced by this plan may be absent at runtime; if so, the affected check records TOOLING\_BLOCKED.

Preflight check:

* Command 1: python \--version

If missing, activation/install action:

* No install action is authorized by this plan.

If still unavailable:

* Step-0A is TOOLING\_BLOCKED.

Preconditions:

* Run from the repository root.  
* Do not use a per-run root.  
* Do not export secrets.

Setup:

* Step-0A creates only QA artifacts under `audit/qa/hde-epic032/`.

Numbered PO actions:

1. Confirm Python is available.  
2. Create the stable QA root and meta directory.  
3. Create the QA-created embedded harness.  
4. Run the harness Step-0A check.  
5. Confirm the Step-0A primary log and discovery output exist.  
6. Confirm the manifest and path-proof sidecar exist.

Paste-ready commands:

Command 1: python \--version

Command 2: mkdir \-p audit/qa/hde-epic032/00\_meta audit/qa/hde-epic032/checks/step-0a-discovery

Command 3: cat \> audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py \<\< 'PY'  
 \#\!/usr/bin/env python3  
 import datetime  
 import hashlib  
 import json  
 import os  
 import re  
 import subprocess  
 import sys  
 from pathlib import Path  
 from datetime import timezone

EPIC \= "hde-epic032"  
 ROOT \= Path("audit/qa/hde-epic032")  
 META \= ROOT / "00\_meta"  
 CHECKS\_ROOT \= ROOT / "checks"  
 MANIFEST \= ROOT / "qa\_step\_logs\_manifest.json"  
 MANIFEST\_PROOF \= ROOT / "qa\_step\_logs\_manifest.json.path\_proof.txt"  
 DOC\_DELTA\_DRAFT \= Path("audit/docdeltas/hde-epic032\_doc\_deltas.md")  
 DOC\_DELTA\_CAPTURE \= META / "doc\_deltas.md"

PF\_REFS \= \[  
 "PF10 — HDE-Build Notes",  
 "PF19 — Glow QA Guide",  
 "PF27 — Canon Plan Templates",  
 \]

ENV\_KEYS \= \["SAFE\_MODE", "ALLOW\_NETWORK", "APP\_ENV", "LC\_ALL", "LANG", "TZ"\]

PATHS \= {  
 "router\_key\_table": "audit/gates/narratives/keys\_10x4.table.json",  
 "registry\_diff": "audit/gates/narratives/registry.diff.json",  
 "pack\_identity": "audit/gates/narratives/pack\_identity.txt",  
 "router\_parity\_abba": "artifacts/narratives/router/parity\_abba.log",  
 "router\_cli\_http\_parity": "artifacts/narratives/router/cli\_http\_parity.log",  
 "db\_provider\_parity": "artifacts/db\_bridge/provider\_parity.proof.json",  
 "db\_adapter\_selection": "artifacts/db\_bridge/adapter\_selection.snapshot.json",  
 "env\_nondev\_failure": "artifacts/runtime/env\_connectivity.nondev\_failure.json",  
 "env\_connectivity": "artifacts/runtime/env\_connectivity.snapshot.json",  
 "ops\_provider\_closure": "audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json",  
 "ops\_provider\_closure\_proof": "audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json.path\_proof.txt",  
 "human\_index": "docs/evidence/INDEX.json",  
 "human\_index\_hash": "docs/evidence/INDEX.sha256",  
 "machine\_mirror": "artifacts/evidence\_index.jsonl",  
 "machine\_mirror\_hash": "artifacts/evidence\_index.jsonl.sha256",  
 "endpoint\_catalog": "docs/ENDPOINTS\_CATALOG.json",  
 "http\_reader": "adapter/http\_reader.py",  
 "cli\_main": "engine/cli/main.py",  
 "registry\_generator": "tools/evidence/generate\_narrative\_registry\_diff.py",  
 "db\_generator": "tools/evidence/generate\_db\_bridge\_parity.py",  
 "index\_updater": "tools/evidence/update\_evidence\_index.py",  
 "path\_validator": "tools/evidence/validate\_evidence\_paths.py",  
 "lf\_checker": "tools/evidence/check\_lf\_endings.py",  
 "mirror\_schema": "ci/checks/check\_mirror\_schema.sh",  
 "index\_hash": "ci/checks/check\_evidence\_index\_hash.sh",  
 "test\_router": "tests/unit/test\_narratives\_router.py",  
 "test\_db\_adapter": "tests/db/test\_adapter\_selection.py",  
 "test\_db\_nondev": "tests/evidence/test\_generate\_db\_bridge\_parity\_nondev.py",  
 "test\_cli\_aux": "tests/cli/test\_aux\_preview.py",  
 "test\_transport\_aux": "tests/transport/test\_aux\_narrative.py",  
 "pyproject": "pyproject.toml",  
 "readme": "README.md",  
 "changelog": "CHANGELOG.md",  
 "agents": "AGENTS.md",  
 "docs\_index": "docs/INDEX.md",  
 "narrative\_manifest": "catalog/narratives/manifest.json",  
 }

CHECK\_NAMES \= {  
 "step-0a-discovery": "Step-0A Discovery posture and Live QA harness setup",  
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
 "po-019": "PO-019",  
 "po-020": "PO-020",  
 "po-021": "PO-021",  
 "po-022": "PO-022",  
 "po-023": "PO-023",  
 "po-024": "PO-024",  
 }

def utc\_now():  
 return datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"

def mtime\_utc(p):  
 value \= datetime.datetime.fromtimestamp(p.stat().st\_mtime, tz=timezone.utc).replace(microsecond=0)  
 return value.strftime("%Y-%m-%dT%H:%M:%SZ")

def env(name, default=""):  
 value \= os.environ.get(name)  
 return value if value is not None else default

def path(key):  
 return Path(PATHS\[key\])

def exists(key):  
 return path(key).exists()

def text(key):  
 p \= path(key)  
 return p.read\_text(encoding="utf-8", errors="replace") if p.exists() else ""

def sha256\_file(p):  
 h \= hashlib.sha256()  
 with p.open("rb") as handle:  
 for chunk in iter(lambda: handle.read(65536), b""):  
 h.update(chunk)  
 return h.hexdigest()

def write\_path\_proof(artifact\_path, produced\_at=None):  
 artifact\_path \= Path(artifact\_path)  
 produced\_at \= produced\_at or utc\_now()  
 proof\_path \= Path(str(artifact\_path) \+ ".path\_proof.txt")  
 proof\_path.parent.mkdir(parents=True, exist\_ok=True)  
 body \= (  
 f"path: {artifact\_path}\\n"  
 f"sha256: {sha256\_file(artifact\_path)}\\n"  
 f"size\_bytes: {artifact\_path.stat().st\_size}\\n"  
 f"mtime\_utc: {mtime\_utc(artifact\_path)}\\n"  
 f"produced\_at\_utc: {produced\_at}\\n"  
 )  
 proof\_path.write\_text(body, encoding="utf-8")  
 return proof\_path

def canonical\_json\_bytes(value):  
 return (json.dumps(value, sort\_keys=True, separators=(",", ":"), ensure\_ascii=False) \+ "\\n").encode("utf-8")

def run\_cmd(cmd):  
 try:  
 proc \= subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, env=os.environ.copy())  
 return {"cmd": cmd, "returncode": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr}  
 except Exception as exc:  
 return {"cmd": cmd, "returncode": 127, "stdout": "", "stderr": f"{type(exc).**name**}: {exc}"}

def check\_pytest\_available():  
 return run\_cmd(\[sys.executable, "-c", "import pytest; print('pytest import PASS')"\])

def missing(keys):  
 return \[PATHS\[k\] for k in keys if not exists(k)\]

def has\_all\_strings(blob, values):  
 return all(v in blob for v in values)

def status\_from(blockers, tooling\_failures, behavior\_failures):  
 if blockers:  
 return "TOOLING\_BLOCKED"  
 if tooling\_failures:  
 return "FAIL\_TOOLING"  
 if behavior\_failures:  
 return "FAIL\_BEHAVIOR"  
 return "PASS"

def result\_base(check\_id):  
 return {  
 "schema": f"hde\_epic032.{check\_id.replace('-', '\_')}.v1",  
 "check\_id": check\_id,  
 "checked\_at\_utc": utc\_now(),  
 "rails": {k: env(k) for k in ENV\_KEYS},  
 }

def evaluate\_step0a():  
 ROOT.mkdir(parents=True, exist\_ok=True)  
 META.mkdir(parents=True, exist\_ok=True)  
 CHECKS\_ROOT.mkdir(parents=True, exist\_ok=True)  
 repo\_paths \= {k: {"path": v, "exists": Path(v).exists()} for k, v in PATHS.items()}  
 r \= result\_base("step-0a-discovery")  
 r.update({  
 "epic\_qa\_root": str(ROOT),  
 "meta\_root": str(META),  
 "checks\_root": str(CHECKS\_ROOT),  
 "qa\_root\_created": ROOT.exists(),  
 "repo\_locus\_discovery": repo\_paths,  
 "status": "PASS",  
 })  
 return r

def evaluate\_step0b():  
 DOC\_DELTA\_DRAFT.parent.mkdir(parents=True, exist\_ok=True)  
 META.mkdir(parents=True, exist\_ok=True)  
 body \= "\\n".join(\[  
 "\# HDE-EPIC032 Doc Deltas",  
 "",  
 "\#\# BLOCKERS",  
 "",  
 "No deltas recorded before Live QA execution.",  
 "",  
 "\#\# CAVEATS",  
 "",  
 "No deltas recorded before Live QA execution.",  
 "",  
 \])  
 DOC\_DELTA\_DRAFT.write\_text(body, encoding="utf-8")  
 DOC\_DELTA\_CAPTURE.write\_text(body, encoding="utf-8")  
 r \= result\_base("step-0b-doc-delta")  
 r.update({  
 "draft\_path": str(DOC\_DELTA\_DRAFT),  
 "capture\_path": str(DOC\_DELTA\_CAPTURE),  
 "draft\_exists": DOC\_DELTA\_DRAFT.exists(),  
 "capture\_exists": DOC\_DELTA\_CAPTURE.exists(),  
 "blockers\_heading\_present": "\#\# BLOCKERS" in body,  
 "caveats\_heading\_present": "\#\# CAVEATS" in body,  
 })  
 r\["status"\] \= "PASS" if r\["draft\_exists"\] and r\["capture\_exists"\] and r\["blockers\_heading\_present"\] and r\["caveats\_heading\_present"\] else "FAIL\_TOOLING"  
 return r

def evaluate\_po001():  
 req \= \["endpoint\_catalog", "http\_reader", "ops\_provider\_closure", "db\_provider\_parity"\]  
 blockers \= missing(req)  
 endpoint \= text("endpoint\_catalog")  
 ops \= text("ops\_provider\_closure")  
 provider \= text("db\_provider\_parity")  
 behavior \= \[\]  
 if not has\_all\_strings(endpoint, \["/reader", "/dev/reader/conjunction"\]):  
 behavior.append("endpoint\_catalog\_missing\_reader\_or\_dev\_reader\_surface")  
 if re.search(r'"qa\_pass\_claimed"\\s\*:\\s*true', ops):*  
 *behavior.append("ops\_evidence\_overclaims\_qa\_pass")*  
 *if any(label in provider and re.search(rf'{label}.*"type"\\s\*:\\s\*"token"', provider) for label in \["DB\_PROVIDER\_PARITY\_OK", "DB\_BRIDGE\_CAPS\_OK", "DB\_BRIDGE\_FALLBACK\_OK"\]):  
 behavior.append("db\_proof\_label\_claimed\_as\_token")  
 r \= result\_base("po-001")  
 r.update({"required\_missing": blockers, "reader\_surface\_seen": "/reader" in endpoint, "dev\_reader\_surface\_seen": "/dev/reader/conjunction" in endpoint, "db\_proof\_labels\_checked": True, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po002():  
 req \= \["test\_router", "router\_key\_table", "router\_parity\_abba"\]  
 blockers \= missing(req)  
 pytest\_check \= check\_pytest\_available()  
 tooling \= \[\]  
 command \= None  
 if pytest\_check\["returncode"\] \!= 0:  
 blockers.append("pytest import unavailable")  
 else:  
 command \= run\_cmd(\[sys.executable, "-m", "pytest", "-q", PATHS\["test\_router"\]\])  
 if command\["returncode"\] \!= 0:  
 tooling.append("router pytest nonzero")  
 r \= result\_base("po-002")  
 r.update({"pytest\_preflight": pytest\_check, "pytest": command, "required\_missing": blockers, "router\_key\_table\_exists": exists("router\_key\_table"), "router\_parity\_abba\_exists": exists("router\_parity\_abba")})  
 r\["status"\] \= status\_from(blockers, tooling, \[\])  
 return r

def evaluate\_po003():  
 req \= \["router\_key\_table", "router\_cli\_http\_parity", "endpoint\_catalog", "http\_reader"\]  
 blockers \= missing(req)  
 endpoint \= text("endpoint\_catalog")  
 reader \= text("http\_reader")  
 key\_table \= text("router\_key\_table")  
 behavior \= \[\]  
 if "/reader" not in endpoint:  
 behavior.append("reader\_route\_not\_visible")  
 if "APP\_ENV" not in reader:  
 behavior.append("app\_env\_gate\_not\_visible")  
 if "prose" in key\_table.lower():  
 behavior.append("router\_key\_table\_contains\_prose\_marker")  
 r \= result\_base("po-003")  
 r.update({"required\_missing": blockers, "reader\_route\_visible": "/reader" in endpoint, "app\_env\_gate\_visible": "APP\_ENV" in reader, "keys\_only\_marker": "prose" not in key\_table.lower(), "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po004():  
 req \= \["test\_router", "router\_parity\_abba"\]  
 blockers \= missing(req)  
 pytest\_check \= check\_pytest\_available()  
 tooling \= \[\]  
 command \= None  
 if pytest\_check\["returncode"\] \!= 0:  
 blockers.append("pytest import unavailable")  
 else:  
 command \= run\_cmd(\[sys.executable, "-m", "pytest", "-q", PATHS\["test\_router"\]\])  
 if command\["returncode"\] \!= 0:  
 tooling.append("identity pytest nonzero")  
 parity \= text("router\_parity\_abba")  
 behavior \= \[\]  
 if not re.search(r"PASS|pass|abba|AB", parity):  
 behavior.append("parity\_abba\_log\_lacks\_identity\_pass\_marker")  
 r \= result\_base("po-004")  
 r.update({"pytest\_preflight": pytest\_check, "pytest": command, "required\_missing": blockers, "parity\_log\_has\_identity\_marker": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, tooling, behavior)  
 return r

def evaluate\_po005():  
 req \= \["registry\_generator", "registry\_diff", "pack\_identity", "narrative\_manifest"\]  
 blockers \= missing(req)  
 command \= run\_cmd(\[sys.executable, PATHS\["registry\_generator"\], "--check"\]) if not blockers else None  
 tooling \= \[\]  
 if command and command\["returncode"\] \!= 0:  
 tooling.append("registry generator check nonzero")  
 reg \= text("registry\_diff")  
 pack \= text("pack\_identity")  
 behavior \= \[\]  
 if "HDE-EPIC032" not in reg:  
 behavior.append("registry\_diff\_missing\_epic\_id")  
 if "pack" not in pack.lower() and "sha" not in pack.lower():  
 behavior.append("pack\_identity\_lacks\_pack\_or\_sha\_marker")  
 r \= result\_base("po-005")  
 r.update({"generator\_check": command, "required\_missing": blockers, "registry\_diff\_contains\_epic": "HDE-EPIC032" in reg, "pack\_identity\_marker\_present": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, tooling, behavior)  
 return r

def evaluate\_po006():  
 req \= \["human\_index", "machine\_mirror", "router\_key\_table"\]  
 blockers \= missing(req)  
 index \= text("human\_index") \+ "\\n" \+ text("machine\_mirror")  
 behavior \= \[\]  
 if "NARR\_REGISTRY\_CLOSURE\_OK" in index and "keys\_10x4" in index:  
 behavior.append("possible\_router\_key\_table\_registry\_token\_overclaim")  
 r \= result\_base("po-006")  
 r.update({"required\_missing": blockers, "unsupported\_registry\_token\_claim\_seen": bool(behavior), "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po007():  
 req \= \["registry\_diff", "pack\_identity", "human\_index", "machine\_mirror"\]  
 blockers \= missing(req)  
 draft\_exists \= DOC\_DELTA\_DRAFT.exists() or Path(PATHS\["readme"\]).exists()  
 behavior \= \[\]  
 reg \= text("registry\_diff")  
 if "HDE-FERM003.2" not in reg and "HDE-EPIC032" not in reg:  
 behavior.append("registry\_diff\_not\_bound\_to\_epic\_or\_row")  
 r \= result\_base("po-007")  
 r.update({"required\_missing": blockers, "doc\_delta\_surface\_available": draft\_exists, "registry\_diff\_bound": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po008():  
 req \= \["db\_generator", "db\_provider\_parity", "db\_adapter\_selection", "ops\_provider\_closure"\]  
 blockers \= missing(req)  
 command \= run\_cmd(\[sys.executable, PATHS\["db\_generator"\], "--check"\]) if not blockers else None  
 tooling \= \[\]  
 if command and command\["returncode"\] \!= 0:  
 tooling.append("db bridge parity check nonzero")  
 provider \= text("db\_provider\_parity")  
 ops \= text("ops\_provider\_closure")  
 behavior \= \[\]  
 if "DB\_PROVIDER\_PARITY\_OK" not in provider:  
 behavior.append("provider\_parity\_label\_not\_visible")  
 if "provider\_parity\_closure\_status" not in ops:  
 behavior.append("ops\_closure\_status\_not\_visible")  
 r \= result\_base("po-008")  
 r.update({"generator\_check": command, "required\_missing": blockers, "provider\_parity\_label\_visible": "DB\_PROVIDER\_PARITY\_OK" in provider, "ops\_closure\_status\_visible": "provider\_parity\_closure\_status" in ops, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, tooling, behavior)  
 return r

def evaluate\_po009():  
 req \= \["ops\_provider\_closure", "ops\_provider\_closure\_proof"\]  
 blockers \= missing(req)  
 ops \= text("ops\_provider\_closure")  
 behavior \= \[\]  
 if re.search(r'"qa\_pass\_claimed"\\s\*:\\s\*true', ops):  
 behavior.append("ops\_evidence\_claims\_qa\_pass")  
 if "provider\_parity\_closure\_status" not in ops:  
 behavior.append("provider\_parity\_closure\_status\_missing")  
 r \= result\_base("po-009")  
 r.update({"required\_missing": blockers, "ops\_status\_visible": "provider\_parity\_closure\_status" in ops, "ops\_qa\_pass\_not\_claimed": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po010():  
 req \= \["db\_provider\_parity", "db\_adapter\_selection", "ops\_provider\_closure"\]  
 blockers \= missing(req)  
 provider \= text("db\_provider\_parity")  
 adapter \= text("db\_adapter\_selection")  
 ops \= text("ops\_provider\_closure")  
 behavior \= \[\]  
 if "DB\_PROVIDER\_PARITY\_OK" not in provider:  
 behavior.append("provider\_parity\_proof\_missing")  
 if "selection\_order" not in provider \+ adapter:  
 behavior.append("selection\_order\_missing")  
 if "drain" in ops.lower() and "claimed" in ops.lower() and "false" not in ops.lower():  
 behavior.append("possible\_checklist\_drainage\_overclaim")  
 r \= result\_base("po-010")  
 r.update({"required\_missing": blockers, "combined\_provider\_and\_adapter\_evidence\_seen": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po011():  
 req \= \["test\_db\_adapter", "test\_db\_nondev", "env\_nondev\_failure"\]  
 blockers \= missing(req)  
 pytest\_check \= check\_pytest\_available()  
 tooling \= \[\]  
 command \= None  
 if pytest\_check\["returncode"\] \!= 0:  
 blockers.append("pytest import unavailable")  
 else:  
 command \= run\_cmd(\[sys.executable, "-m", "pytest", "-q", PATHS\["test\_db\_adapter"\], PATHS\["test\_db\_nondev"\]\])  
 if command\["returncode"\] \!= 0:  
 tooling.append("db typed failure pytest nonzero")  
 nondev \= text("env\_nondev\_failure")  
 behavior \= \[\]  
 for marker in \["numeric\_free", "missing\_bridge\_url", "BridgeUnavailable"\]:  
 if marker not in nondev:  
 behavior.append(f"nondev\_failure\_missing\_{marker}")  
 r \= result\_base("po-011")  
 r.update({"pytest\_preflight": pytest\_check, "pytest": command, "required\_missing": blockers, "numeric\_free\_seen": "numeric\_free" in nondev, "missing\_bridge\_url\_seen": "missing\_bridge\_url" in nondev, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, tooling, behavior)  
 return r

def evaluate\_po012():  
 req \= \["env\_nondev\_failure", "db\_adapter\_selection", "test\_db\_adapter"\]  
 blockers \= missing(req)  
 nondev \= text("env\_nondev\_failure")  
 behavior \= \[\]  
 if "no\_proactive\_probes" not in nondev:  
 behavior.append("no\_proactive\_probes\_missing")  
 if "adapter\_path\_only" not in nondev:  
 behavior.append("adapter\_path\_only\_missing")  
 if "missing\_bridge\_url" not in nondev:  
 behavior.append("typed\_failure\_missing")  
 r \= result\_base("po-012")  
 r.update({"required\_missing": blockers, "no\_proactive\_probes\_seen": "no\_proactive\_probes" in nondev, "typed\_failure\_seen": "missing\_bridge\_url" in nondev, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po013():  
 req \= \["human\_index", "human\_index\_hash", "machine\_mirror", "machine\_mirror\_hash", "index\_updater", "path\_validator"\]  
 blockers \= missing(req)  
 commands \= \[\]  
 tooling \= \[\]  
 if not blockers:  
 for cmd in (\[sys.executable, PATHS\["index\_updater"\], "--check"\], \[sys.executable, PATHS\["path\_validator"\]\]):  
 res \= run\_cmd(cmd)  
 commands.append(res)  
 if res\["returncode"\] \!= 0:  
 tooling.append("evidence coherence command nonzero")  
 r \= result\_base("po-013")  
 r.update({"commands": commands, "required\_missing": blockers, "human\_index\_present": exists("human\_index"), "machine\_mirror\_present": exists("machine\_mirror")})  
 r\["status"\] \= status\_from(blockers, tooling, \[\])  
 return r

def evaluate\_po014():  
 req \= \["human\_index", "machine\_mirror", "mirror\_schema", "path\_validator", "machine\_mirror\_hash"\]  
 blockers \= missing(req)  
 commands \= \[\]  
 tooling \= \[\]  
 if not blockers:  
 for cmd in (\[sys.executable, PATHS\["mirror\_schema"\]\], \[sys.executable, PATHS\["path\_validator"\]\]):  
 res \= run\_cmd(cmd)  
 commands.append(res)  
 if res\["returncode"\] \!= 0:  
 tooling.append("mirror alignment command nonzero")  
 r \= result\_base("po-014")  
 r.update({"commands": commands, "required\_missing": blockers, "human\_machine\_loci\_present": exists("human\_index") and exists("machine\_mirror")})  
 r\["status"\] \= status\_from(blockers, tooling, \[\])  
 return r

def evaluate\_po015():  
 req \= \["registry\_generator", "db\_generator", "index\_updater", "path\_validator", "index\_hash", "mirror\_schema", "lf\_checker"\]  
 blockers \= missing(req)  
 commands \= \[\]  
 tooling \= \[\]  
 if not blockers:  
 for cmd in (  
 \[sys.executable, PATHS\["registry\_generator"\], "--check"\],  
 \[sys.executable, PATHS\["db\_generator"\], "--check"\],  
 \[sys.executable, PATHS\["index\_updater"\], "--check"\],  
 \[sys.executable, PATHS\["path\_validator"\]\],  
 \["bash", PATHS\["index\_hash"\]\],  
 \[sys.executable, PATHS\["mirror\_schema"\]\],  
 \[sys.executable, PATHS\["lf\_checker"\]\],  
 ):  
 res \= run\_cmd(cmd)  
 commands.append(res)  
 if res\["returncode"\] \!= 0:  
 tooling.append("fail\_closed\_or\_coherence\_command\_nonzero")  
 r \= result\_base("po-015")  
 r.update({"commands": commands, "required\_missing": blockers, "all\_commands\_green": bool(commands) and all(c\["returncode"\] \== 0 for c in commands)})  
 r\["status"\] \= status\_from(blockers, tooling, \[\])  
 return r

def evaluate\_po016():  
 req \= \["db\_provider\_parity", "human\_index", "machine\_mirror"\]  
 blockers \= missing(req)  
 blob \= text("db\_provider\_parity") \+ "\\n" \+ text("human\_index") \+ "\\n" \+ text("machine\_mirror")  
 behavior \= \[\]  
 for label in \["DB\_PROVIDER\_PARITY\_OK", "DB\_BRIDGE\_CAPS\_OK", "DB\_BRIDGE\_FALLBACK\_OK"\]:  
 if label in blob and re.search(rf'{label}.*"type"\\s*:\\s\*"token"', blob):  
 behavior.append(f"{label}\_claimed\_as\_token")  
 r \= result\_base("po-016")  
 r.update({"required\_missing": blockers, "db\_labels\_token\_overclaim\_detected": bool(behavior), "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po017():  
 req \= \["db\_provider\_parity"\]  
 blockers \= missing(req)  
 blob \= text("db\_provider\_parity")  
 behavior \= \[\]  
 if "DEV\_DB\_BRIDGE\_FALLBACK\_OK" in blob and "dev" not in blob.lower():  
 behavior.append("dev\_bridge\_fallback\_token\_scope\_unclear")  
 for label in \["DB\_BRIDGE\_FALLBACK\_OK", "DB\_PROVIDER\_PARITY\_OK", "DB\_BRIDGE\_CAPS\_OK"\]:  
 if label in blob and re.search(rf'{label}.*"type"\\s*:\\s\*"token"', blob):  
 behavior.append(f"{label}\_scope\_broadened\_to\_token")  
 r \= result\_base("po-017")  
 r.update({"required\_missing": blockers, "fallback\_scope\_checked": True, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po018():  
 req \= \["router\_key\_table", "registry\_diff", "db\_provider\_parity", "ops\_provider\_closure"\]  
 blockers \= missing(req)  
 behavior \= \[\]  
 ops \= text("ops\_provider\_closure")  
 if "drain" in ops.lower() and re.search(r'"pf09.*claimed"\\s*:\\s\*true', ops.lower()):  
 behavior.append("pf09\_drainage\_claimed")  
 r \= result\_base("po-018")  
 r.update({"required\_missing": blockers, "active\_evidence\_families\_present": len(blockers) \== 0, "pf09\_drainage\_not\_claimed": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po019():  
 req \= \["readme", "changelog", "docs\_index"\]  
 blockers \= missing(req)  
 blob \= text("readme") \+ "\\n" \+ text("changelog") \+ "\\n" \+ text("docs\_index")  
 behavior \= \[\]  
 if "HDE-EPIC032" not in blob:  
 behavior.append("epic032\_repo\_docs\_marker\_missing")  
 r \= result\_base("po-019")  
 r.update({"required\_missing": blockers, "reused\_foundation\_checked\_from\_repo\_docs": "HDE-EPIC032" in blob, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po020():  
 req \= \["ops\_provider\_closure"\]  
 blockers \= missing(req)  
 ops \= text("ops\_provider\_closure")  
 behavior \= \[\]  
 for marker in \["qa\_pass\_claimed", "epic\_closure", "checklist"\]:  
 if marker in ops and re.search(rf'"{marker}"\\s\*:\\s\*true', ops):  
 behavior.append(f"truth\_class\_overclaim\_{marker}")  
 r \= result\_base("po-020")  
 r.update({"required\_missing": blockers, "truth\_classes\_remain\_separate": not behavior, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po021():  
 req \= \["ops\_provider\_closure", "db\_provider\_parity"\]  
 blockers \= missing(req)  
 blob \= text("ops\_provider\_closure") \+ "\\n" \+ text("db\_provider\_parity")  
 behavior \= \[\]  
 if re.search(r"vendor.version.\*conformance.\*true", blob.lower()):  
 behavior.append("vendor\_version\_runtime\_conformance\_claimed")  
 r \= result\_base("po-021")  
 r.update({"required\_missing": blockers, "vendor\_version\_runtime\_conformance\_claimed": bool(behavior), "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po022():  
 req \= \["ops\_provider\_closure", "db\_provider\_parity"\]  
 blockers \= missing(req)  
 blob \= text("ops\_provider\_closure") \+ "\\n" \+ text("db\_provider\_parity")  
 behavior \= \[\]  
 if re.search(r"live.\*provider.\*pass", blob.lower()) and "unavailable" not in blob.lower() and "false" not in blob.lower():  
 behavior.append("live\_provider\_behavior\_claimed")  
 r \= result\_base("po-022")  
 r.update({"required\_missing": blockers, "live\_provider\_behavior\_claimed": bool(behavior), "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po023():  
 req \= \["endpoint\_catalog", "http\_reader"\]  
 blockers \= missing(req)  
 endpoint \= text("endpoint\_catalog")  
 reader \= text("http\_reader")  
 behavior \= \[\]  
 if "/api/reader-proof/v1" in endpoint \+ reader:  
 behavior.append("invented\_reader\_proof\_route\_seen")  
 if "/reader" not in endpoint:  
 behavior.append("reader\_route\_missing\_from\_catalog")  
 r \= result\_base("po-023")  
 r.update({"required\_missing": blockers, "reader\_route\_visible": "/reader" in endpoint, "invented\_reader\_proof\_route\_absent": "/api/reader-proof/v1" not in endpoint \+ reader, "behavior\_failures": behavior})  
 r\["status"\] \= status\_from(blockers, \[\], behavior)  
 return r

def evaluate\_po024():  
 r \= result\_base("po-024")  
 r.update({  
 "live\_qa\_planning\_or\_execution\_performed\_implementation": False,  
 "live\_qa\_planning\_or\_execution\_performed\_pf\_edit": False,  
 "live\_qa\_planning\_or\_execution\_performed\_closeout\_action": False,  
 "live\_qa\_role": "prove\_current\_results\_only",  
 "status": "PASS",  
 })  
 return r

EVALUATORS \= {  
 "step-0a-discovery": evaluate\_step0a,  
 "step-0b-doc-delta": evaluate\_step0b,  
 "po-001": evaluate\_po001,  
 "po-002": evaluate\_po002,  
 "po-003": evaluate\_po003,  
 "po-004": evaluate\_po004,  
 "po-005": evaluate\_po005,  
 "po-006": evaluate\_po006,  
 "po-007": evaluate\_po007,  
 "po-008": evaluate\_po008,  
 "po-009": evaluate\_po009,  
 "po-010": evaluate\_po010,  
 "po-011": evaluate\_po011,  
 "po-012": evaluate\_po012,  
 "po-013": evaluate\_po013,  
 "po-014": evaluate\_po014,  
 "po-015": evaluate\_po015,  
 "po-016": evaluate\_po016,  
 "po-017": evaluate\_po017,  
 "po-018": evaluate\_po018,  
 "po-019": evaluate\_po019,  
 "po-020": evaluate\_po020,  
 "po-021": evaluate\_po021,  
 "po-022": evaluate\_po022,  
 "po-023": evaluate\_po023,  
 "po-024": evaluate\_po024,  
 }

def write\_manifest(check\_id, status, primary\_log, primary\_proof):  
 ROOT.mkdir(parents=True, exist\_ok=True)  
 existing \= \[\]  
 if MANIFEST.exists():  
 try:  
 loaded \= json.loads(MANIFEST.read\_text(encoding="utf-8"))  
 if isinstance(loaded, list):  
 existing \= \[row for row in loaded if row.get("check\_id") \!= check\_id\]  
 except Exception:  
 existing \= \[\]  
 entry \= {  
 "check\_id": check\_id,  
 "log\_path": str(primary\_log),  
 "log\_path\_proof": str(primary\_proof),  
 "status": status,  
 "updated\_at\_utc": utc\_now(),  
 }  
 existing.append(entry)  
 existing.sort(key=lambda row: row.get("check\_id", ""))  
 MANIFEST.write\_bytes(canonical\_json\_bytes(existing))  
 write\_path\_proof(MANIFEST)

def write\_primary(check\_id, result, command):  
 check\_dir \= CHECKS\_ROOT / check\_id  
 check\_dir.mkdir(parents=True, exist\_ok=True)  
 primary \= check\_dir / "primary.log"  
 primary\_proof \= Path(str(primary) \+ ".path\_proof.txt")  
 result\_path \= check\_dir / "result.json"  
 result\_path.write\_text(json.dumps(result, indent=2, sort\_keys=True) \+ "\\n", encoding="utf-8")  
 status \= result.get("status", "FAIL\_TOOLING")  
 exit\_code \= 0 if status \== "PASS" else 2 if status \== "TOOLING\_BLOCKED" else 1  
 header \= {  
 "schema\_version": "pf27.step\_log\_header.v1",  
 "timestamp\_utc": utc\_now(),  
 "check\_id": check\_id,  
 "check\_name": CHECK\_NAMES.get(check\_id, check\_id),  
 "status": status,  
 "fail\_status": "" if status \== "PASS" else status,  
 "command": command,  
 "command\_provenance": "Copy/paste from plan",  
 "exit\_code": exit\_code,  
 "evidence\_artifacts": \[str(primary), str(primary\_proof), str(result\_path)\],  
 "captured\_env": {k: env(k) for k in ENV\_KEYS},  
 "pf\_refs": PF\_REFS,  
 "intended\_tokens": \[\],  
 "claimed\_tokens": \[\],  
 }  
 body \= json.dumps(result, indent=2, sort\_keys=True)  
 primary.write\_text(json.dumps(header, ensure\_ascii=False, sort\_keys=True) \+ "\\n" \+ body \+ "\\n", encoding="utf-8")  
 primary\_proof \= write\_path\_proof(primary)  
 write\_manifest(check\_id, status, primary, primary\_proof)  
 return exit\_code

def main():  
 if len(sys.argv) \!= 2 or sys.argv\[1\] not in EVALUATORS:  
 print("usage: live\_qa\_harness.py CHECK\_ID", file=sys.stderr)  
 print("known: " \+ ", ".join(sorted(EVALUATORS)), file=sys.stderr)  
 return 2  
 check\_id \= sys.argv\[1\]  
 for k, v in {"SAFE\_MODE": "1", "ALLOW\_NETWORK": "0", "APP\_ENV": "dev", "LC\_ALL": "C", "LANG": "C", "TZ": "UTC"}.items():  
 os.environ.setdefault(k, v)  
 ROOT.mkdir(parents=True, exist\_ok=True)  
 META.mkdir(parents=True, exist\_ok=True)  
 CHECKS\_ROOT.mkdir(parents=True, exist\_ok=True)  
 command \= f"python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py {check\_id}"  
 result \= EVALUATORScheck\_id  
 return write\_primary(check\_id, result, command)

if **name** \== "**main**":  
 raise SystemExit(main())  
 PY

Command 4: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py step-0a-discovery

What to look for:

* `audit/qa/hde-epic032/00_meta/live_qa_harness.py` exists.  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log` exists.  
* `audit/qa/hde-epic032/checks/step-0a-discovery/result.json` exists.  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json` exists.  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt` exists.

Required deliverables:

* `audit/qa/hde-epic032/00_meta/live_qa_harness.py`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

PASS criteria tied to deliverables:

* The stable epic QA root exists.  
* The QA-created harness exists.  
* Step-0A primary log exists and records PASS with exit\_code 0\.  
* The manifest and path-proof sidecar exist.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if Python is unavailable.  
* FAIL\_TOOLING if harness creation or evidence assembly fails.

Step-0B — Doc Delta Capture

Goal: Mechanically create the two doc-delta surfaces required for runbook self-honesty. The initial contents may record no deltas; later blocked checks, plan drift, or Moon Loop deviations must be added to the same surfaces.

Required dependencies:

* Python 3  
* Step-0A harness

Preflight check:

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py

If missing, activation/install action:

* Run Step-0A.

If still unavailable:

* Step-0B is TOOLING\_BLOCKED.

Preconditions:

* Step-0A completed enough to create the harness.

Setup:

* Step-0B creates the doc-delta draft and epic-scoped capture files.

Numbered PO actions:

1. Run the preflight command.  
2. If the helper is missing, run Step-0A.  
3. Run the Step-0B command.  
4. Confirm both doc-delta surfaces exist.  
5. Confirm both surfaces contain BLOCKERS and CAVEATS headings.

Paste-ready commands:

Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py

Command 2: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 3: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py step-0b-doc-delta

What to look for:

* `audit/docdeltas/hde-epic032_doc_deltas.md` exists.  
* `audit/qa/hde-epic032/00_meta/doc_deltas.md` exists.  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log` records PASS.

Required deliverables:

* `audit/docdeltas/hde-epic032_doc_deltas.md`  
* `audit/qa/hde-epic032/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log.path_proof.txt`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json`

PASS criteria tied to deliverables:

* Both doc-delta surfaces exist.  
* Both surfaces include BLOCKERS and CAVEATS headings.  
* Primary log records PASS with exit\_code 0\.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if the Step-0A harness is unavailable.  
* FAIL\_TOOLING if either doc-delta surface cannot be written.

Moon Loop posture

A bounded Moon Loop is allowed only for QA-created evidence-harness, header, manifest, path-proof, or doc-delta assembly defects. It must not change product code, implementation files, acceptance-token claims, PF documents, public routes, public flags, live vendor behavior, or deferred scope.

Allowed Moon Loop trigger:

* A required check is blocked because the QA-created harness, header, manifest, doc-delta surface, or QA-created evidence assembly is malformed, missing, or unable to record an otherwise observable proof target.

Allowed Moon Loop action:

* Correct only the QA-created file under `audit/qa/hde-epic032/`.  
* Preserve the original failed or blocked evidence stream.  
* Record a remediation note in `audit/qa/hde-epic032/00_meta/doc_deltas.md`.  
* Record changed files and hashes under `audit/qa/hde-epic032/00_meta/delta/`.  
* Rerun only the affected check under the same rails.

Stop condition:

* If the needed change touches product code, tests, evidence generators outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems, stop and classify the affected check as FAIL\_TOOLING or TOOLING\_BLOCKED according to the observed state.

Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | commands (PO-only) | expected result | primary evidence | deliverables | tokens | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| step-0a-discovery | Step-0A Discovery posture and Live QA harness setup | D0 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py step-0a-discovery | PASS if QA root, helper, manifest, and discovery result exist | audit/qa/hde-epic032/checks/step-0a-discovery/primary.log | primary.log; primary.log.path\_proof.txt; result.json; qa\_step\_logs\_manifest.json; qa\_step\_logs\_manifest.json.path\_proof.txt | \[\] | PF27 — Canon Plan Templates |
| step-0b-doc-delta | Step-0B Doc Delta Capture | D0 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py step-0b-doc-delta | PASS if doc-delta draft and capture surfaces exist | audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log | primary.log; primary.log.path\_proof.txt; result.json; doc\_deltas.md surfaces | \[\] | PF27 — Canon Plan Templates |
| po-001 | PO-001 | D1 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-001 | PASS if scope remains Fermentation Pass 3 and no deferred scope is absorbed | audit/qa/hde-epic032/checks/po-001/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-002 | PO-002 | D1 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-002 | PASS if router deterministic key-selection proof is observable | audit/qa/hde-epic032/checks/po-002/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF14 — HDE Mechanics Guide |
| po-003 | PO-003 | D1 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-003 | PASS if router proof is keys-only and public Reader is not expanded | audit/qa/hde-epic032/checks/po-003/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF17 — HDE Narratives Guide |
| po-004 | PO-004 | D1 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-004 | PASS if repeated-run and AB↔BA identity proof is observable | audit/qa/hde-epic032/checks/po-004/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF17 — HDE Narratives Guide |
| po-005 | PO-005 | D2 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-005 | PASS if registry diff and pack identity proof are coherent | audit/qa/hde-epic032/checks/po-005/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF14 — HDE Mechanics Guide |
| po-006 | PO-006 | D2 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-006 | PASS if registry proof does not claim unsupported acceptance semantics | audit/qa/hde-epic032/checks/po-006/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-007 | PO-007 | D2 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-007 | PASS if doc-delta identity is coherent with registry proof | audit/qa/hde-epic032/checks/po-007/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF17 — HDE Narratives Guide |
| po-008 | PO-008 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-008 | PASS if DB bridge/provider parity proof chain is combined and governed | audit/qa/hde-epic032/checks/po-008/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF14 — HDE Mechanics Guide |
| po-009 | PO-009 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-009 | PASS if OPS provider parity evidence remains support evidence only | audit/qa/hde-epic032/checks/po-009/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-010 | PO-010 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-010 | PASS if combined DB proof supports the row without PF09.5 drainage claim | audit/qa/hde-epic032/checks/po-010/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-011 | PO-011 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-011 | PASS if non-dev DB failure is typed, numeric-free, and observed | audit/qa/hde-epic032/checks/po-011/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF05 — HDE CLI/API Vendor Reference |
| po-012 | PO-012 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-012 | PASS if DB runtime avoids proactive probes and preserves typed failure posture | audit/qa/hde-epic032/checks/po-012/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF14 — HDE Mechanics Guide |
| po-013 | PO-013 | D4 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-013 | PASS if human and machine evidence are coherent | audit/qa/hde-epic032/checks/po-013/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF12 — HDE Schemas and Artifacts |
| po-014 | PO-014 | D4 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-014 | PASS if mirror alignment has no stale or contradictory companion state | audit/qa/hde-epic032/checks/po-014/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF12 — HDE Schemas and Artifacts |
| po-015 | PO-015 | D4 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-015 | PASS if generated proof fails closed when predicates are missing or stale | audit/qa/hde-epic032/checks/po-015/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF14 — HDE Mechanics Guide |
| po-016 | PO-016 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-016 | PASS if DB parity labels are not claimed as unregistered tokens | audit/qa/hde-epic032/checks/po-016/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-017 | PO-017 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-017 | PASS if dev bridge fallback token scope is not broadened | audit/qa/hde-epic032/checks/po-017/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF04 — HDE-Governance |
| po-018 | PO-018 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-018 | PASS if active rows are supportable without PF09.5 drainage claim | audit/qa/hde-epic032/checks/po-018/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-019 | PO-019 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-019 | PASS if reused foundation is not re-scoped as new work | audit/qa/hde-epic032/checks/po-019/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-020 | PO-020 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-020 | PASS if implementation readiness, OPS evidence, QA result, drainage, and closure stay separate | audit/qa/hde-epic032/checks/po-020/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF19 — Glow QA Guide |
| po-021 | PO-021 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-021 | PASS if vendor-version runtime conformance is not claimed | audit/qa/hde-epic032/checks/po-021/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF10 — HDE-Build Notes |
| po-022 | PO-022 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-022 | PASS if live provider behavior is not claimed from local proof | audit/qa/hde-epic032/checks/po-022/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF19 — Glow QA Guide |
| po-023 | PO-023 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-023 | PASS if public Reader behavior remains unchanged | audit/qa/hde-epic032/checks/po-023/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF05 — HDE CLI/API Vendor Reference |
| po-024 | PO-024 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-024 | PASS if Live QA remains proof-only | audit/qa/hde-epic032/checks/po-024/primary.log | primary.log; primary.log.path\_proof.txt; result.json | \[\] | PF27 — Canon Plan Templates |
|  |  |  |  |  |  |  |  |  |  |

Token coverage and evidence binding

* This plan treats every check as tokenless evidence.  
* `intended_tokens` must be `[]` in every primary log header.  
* `claimed_tokens` must be `[]` in every primary log header.  
* `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are non-token proof labels for this epic unless Governance later registers them.  
* `DEV_DB_BRIDGE_FALLBACK_OK` must not be broadened beyond its existing dev bridge-fallback scope by this Live QA plan.  
* No check in this runbook claims acceptance-token satisfaction, final QA outcome, PF09.5 drainage, or epic closeout by itself.

Check Blocks

CHECK step-0a-discovery: Step-0A Discovery posture and Live QA harness setup

Surface / D-goal mapping: D0 / discovery posture

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF27 — Canon Plan Templates; PF19 — Glow QA Guide

Repo-resident loci:

* QA-created: `audit/qa/hde-epic032/00_meta/live_qa_harness.py`  
* QA-created: `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`  
* QA-created: `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
* QA-created: `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

Dependencies required:

* Python 3

Preflight command(s):

* Command 1: python \--version

Activation or installation remediation, if allowed:

* No install action is authorized by this plan.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py step-0a-discovery

Expected result:

PASS if:

* The stable QA root exists.  
* The QA-created harness exists.  
* Step-0A primary log and result sidecar exist.  
* Manifest and manifest path-proof sidecar exist.

FAIL\_TOOLING if:

* The QA-created harness cannot write governed evidence under the stable QA root.

TOOLING\_BLOCKED if:

* Python is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`

Deliverables:

* `audit/qa/hde-epic032/00_meta/live_qa_harness.py`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/primary.log`  
* `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
* `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK step-0b-doc-delta: Step-0B Doc Delta Capture

Surface / D-goal mapping: D0 / doc-delta capture

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF27 — Canon Plan Templates; PF19 — Glow QA Guide

Repo-resident loci:

* QA-created: `audit/docdeltas/hde-epic032_doc_deltas.md`  
* QA-created: `audit/qa/hde-epic032/00_meta/doc_deltas.md`  
* QA-created: `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py step-0b-doc-delta

Expected result:

PASS if:

* Both doc-delta surfaces exist.  
* Both doc-delta surfaces include BLOCKERS and CAVEATS headings.  
* The Step-0B primary log records PASS.

FAIL\_TOOLING if:

* Either doc-delta surface cannot be written.

TOOLING\_BLOCKED if:

* The Step-0A harness is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`

Deliverables:

* `audit/docdeltas/hde-epic032_doc_deltas.md`  
* `audit/qa/hde-epic032/00_meta/doc_deltas.md`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/primary.log`  
* `audit/qa/hde-epic032/checks/step-0b-doc-delta/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-001: PO-001

Goal: The epic must remain limited to its Fermentation Pass 3 scope and must not absorb deferred vendor-version, live-provider, public-surface, or later runtime-conformance work.

Surface / D-goal mapping: D1 / Fermentation scope boundary

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide

Repo-resident loci:

* Audit-proven: `docs/ENDPOINTS_CATALOG.json`  
* Audit-proven: `adapter/http_reader.py`  
* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-001/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-001/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f docs/ENDPOINTS\_CATALOG.json  
* Command 3: test \-f adapter/http\_reader.py  
* Command 4: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json  
* Command 5: test \-f artifacts/db\_bridge/provider\_parity.proof.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-001

Expected result:

PASS if:

* Reader and dev Reader catalog surfaces are visible.  
* OPS evidence does not claim QA pass by itself.  
* DB proof labels are not treated as registered acceptance tokens.  
* Deferred vendor-version, live-provider, and public-surface scope is not absorbed.

FAIL\_BEHAVIOR if:

* A DB parity/capability/fallback proof label is treated as a token.  
* OPS support evidence claims QA pass by itself.  
* Public Reader expansion is detected.

TOOLING\_BLOCKED if:

* Required repo evidence loci are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-001/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-001/primary.log`  
* `audit/qa/hde-epic032/checks/po-001/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-002: PO-002

Goal: The narrative router must produce deterministic key-selection behavior across required parity, identity, and missing-key scenarios.

Surface / D-goal mapping: D1 / narrative router deterministic key selection

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF14 — HDE Mechanics Guide; PF17 — HDE Narratives Guide

Repo-resident loci:

* Audit-proven: `tests/unit/test_narratives_router.py`  
* Audit-proven: `audit/gates/narratives/keys_10x4.table.json`  
* Audit-proven: `artifacts/narratives/router/parity_abba.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-002/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-002/result.json`

Dependencies required:

* Python 3  
* pytest  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 3: test \-f tests/unit/test\_narratives\_router.py  
* Command 4: test \-f audit/gates/narratives/keys\_10x4.table.json  
* Command 5: test \-f artifacts/narratives/router/parity\_abba.log

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No package installation is authorized by this plan.

If readiness cannot be established:

* TOOLING\_BLOCKED when pytest or required repo loci are unavailable.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-002

Expected result:

PASS if:

* Router tests return exit code 0\.  
* Key-table evidence exists.  
* AB↔BA parity evidence exists.

FAIL\_BEHAVIOR if:

* Deterministic router behavior is contradicted by the test result.

FAIL\_TOOLING if:

* pytest invocation fails for tooling reasons after readiness was established.

TOOLING\_BLOCKED if:

* pytest or required repo loci are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-002/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-002/primary.log`  
* `audit/qa/hde-epic032/checks/po-002/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-003: PO-003

Goal: Narrative router proof must remain key-based and must not become prose generation, public Reader expansion, or a new public narrative contract.

Surface / D-goal mapping: D1 / keys-only router proof and Reader non-expansion

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF17 — HDE Narratives Guide; PF05 — HDE CLI/API Vendor Reference

Repo-resident loci:

* Audit-proven: `audit/gates/narratives/keys_10x4.table.json`  
* Audit-proven: `artifacts/narratives/router/cli_http_parity.log`  
* Audit-proven: `docs/ENDPOINTS_CATALOG.json`  
* Audit-proven: `adapter/http_reader.py`  
* QA-created: `audit/qa/hde-epic032/checks/po-003/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-003/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/gates/narratives/keys\_10x4.table.json  
* Command 3: test \-f artifacts/narratives/router/cli\_http\_parity.log  
* Command 4: test \-f docs/ENDPOINTS\_CATALOG.json  
* Command 5: test \-f adapter/http\_reader.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-003

Expected result:

PASS if:

* Router key-table evidence remains keys-only.  
* Reader route posture is visible but not expanded into a new proof route.  
* APP\_ENV gating is visible for internal/dev surfaces.

FAIL\_BEHAVIOR if:

* Router proof becomes prose generation.  
* An invented Reader proof route is detected.  
* Public Reader contract expansion is detected.

TOOLING\_BLOCKED if:

* Required evidence or catalog loci are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-003/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-003/primary.log`  
* `audit/qa/hde-epic032/checks/po-003/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-004: PO-004

Goal: Narrative router behavior must preserve deterministic identity behavior across repeated runs and reversed-pair comparisons where applicable.

Surface / D-goal mapping: D1 / repeated-run and AB↔BA identity

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF17 — HDE Narratives Guide

Repo-resident loci:

* Audit-proven: `tests/unit/test_narratives_router.py`  
* Audit-proven: `artifacts/narratives/router/parity_abba.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-004/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-004/result.json`

Dependencies required:

* Python 3  
* pytest  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 3: test \-f tests/unit/test\_narratives\_router.py  
* Command 4: test \-f artifacts/narratives/router/parity\_abba.log

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No package installation is authorized by this plan.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-004

Expected result:

PASS if:

* Router pytest command returns exit code 0\.  
* AB↔BA or identity marker evidence exists in the router parity log.

FAIL\_BEHAVIOR if:

* Repeated-run or reversed-pair identity behavior is contradicted.

FAIL\_TOOLING if:

* pytest fails for tooling reasons after readiness was established.

TOOLING\_BLOCKED if:

* pytest or required evidence files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-004/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-004/primary.log`  
* `audit/qa/hde-epic032/checks/po-004/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-005: PO-005

Goal: Narrative registry proof must show stable, canonical, keys-only registry diffing and pack identity behavior.

Surface / D-goal mapping: D2 / registry diff and pack identity

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF14 — HDE Mechanics Guide; PF17 — HDE Narratives Guide

Repo-resident loci:

* Audit-proven: `tools/evidence/generate_narrative_registry_diff.py`  
* Audit-proven: `audit/gates/narratives/registry.diff.json`  
* Audit-proven: `audit/gates/narratives/pack_identity.txt`  
* Audit-proven: `catalog/narratives/manifest.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-005/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-005/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f tools/evidence/generate\_narrative\_registry\_diff.py  
* Command 3: test \-f audit/gates/narratives/registry.diff.json  
* Command 4: test \-f audit/gates/narratives/pack\_identity.txt  
* Command 5: test \-f catalog/narratives/manifest.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-005

Expected result:

PASS if:

* Registry generator check returns exit code 0\.  
* Registry diff evidence is bound to HDE-EPIC032.  
* Pack identity evidence records pack or sha identity posture.

FAIL\_BEHAVIOR if:

* Registry diff or pack identity evidence contradicts stable, canonical, keys-only identity.

FAIL\_TOOLING if:

* Generator check fails after readiness was established.

TOOLING\_BLOCKED if:

* Required generator or evidence files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-005/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-005/primary.log`  
* `audit/qa/hde-epic032/checks/po-005/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-006: PO-006

Goal: Narrative registry proof must not claim unsupported acceptance semantics beyond the governed registry and canonical-identity evidence actually implemented.

Surface / D-goal mapping: D2 / registry proof non-overclaim

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF04 — HDE-Governance

Repo-resident loci:

* Audit-proven: `docs/evidence/INDEX.json`  
* Audit-proven: `artifacts/evidence_index.jsonl`  
* Audit-proven: `audit/gates/narratives/keys_10x4.table.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-006/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-006/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f docs/evidence/INDEX.json  
* Command 3: test \-f artifacts/evidence\_index.jsonl  
* Command 4: test \-f audit/gates/narratives/keys\_10x4.table.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-006

Expected result:

PASS if:

* Registry evidence does not claim unsupported acceptance semantics.  
* Router key-table evidence does not overclaim `NARR_REGISTRY_CLOSURE_OK`.

FAIL\_BEHAVIOR if:

* Unsupported registry acceptance semantics are claimed.  
* Removed or unapproved registry token posture reappears.

TOOLING\_BLOCKED if:

* Human or machine evidence records are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-006/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-006/primary.log`  
* `audit/qa/hde-epic032/checks/po-006/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-007: PO-007

Goal: Documentation-delta identity for narrative registry work must be coherent with the registry proof and must not create an ungoverned documentation claim.

Surface / D-goal mapping: D2 / registry doc-delta identity

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF17 — HDE Narratives Guide; PF12 — HDE Schemas and Artifacts

Repo-resident loci:

* Audit-proven: `audit/gates/narratives/registry.diff.json`  
* Audit-proven: `audit/gates/narratives/pack_identity.txt`  
* Audit-proven: `docs/evidence/INDEX.json`  
* Audit-proven: `artifacts/evidence_index.jsonl`  
* QA-created: `audit/qa/hde-epic032/checks/po-007/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-007/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness  
* Step-0B doc-delta surfaces

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/qa/hde-epic032/00\_meta/doc\_deltas.md  
* Command 3: test \-f audit/gates/narratives/registry.diff.json  
* Command 4: test \-f audit/gates/narratives/pack\_identity.txt  
* Command 5: test \-f docs/evidence/INDEX.json  
* Command 6: test \-f artifacts/evidence\_index.jsonl

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* Run Step-0B if doc-delta surfaces are missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-007

Expected result:

PASS if:

* Registry diff is bound to HDE-EPIC032 or the scoped registry row.  
* Registry proof, pack identity, and evidence records are present.  
* Doc-delta posture does not create an ungoverned documentation claim.

FAIL\_BEHAVIOR if:

* Registry documentation proof is unbound or contradictory.  
* Documentation identity is overclaimed.

TOOLING\_BLOCKED if:

* Required registry, index, or doc-delta surfaces are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-007/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-007/primary.log`  
* `audit/qa/hde-epic032/checks/po-007/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-008: PO-008

Goal: Database bridge fallback, bridge capability, and provider parity must be proven as a combined governed proof chain rather than as an isolated implementation-only or operations-only claim.

Surface / D-goal mapping: D3 / DB bridge and provider parity proof chain

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF14 — HDE Mechanics Guide

Repo-resident loci:

* Audit-proven: `tools/evidence/generate_db_bridge_parity.py`  
* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* Audit-proven: `artifacts/db_bridge/adapter_selection.snapshot.json`  
* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-008/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-008/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f tools/evidence/generate\_db\_bridge\_parity.py  
* Command 3: test \-f artifacts/db\_bridge/provider\_parity.proof.json  
* Command 4: test \-f artifacts/db\_bridge/adapter\_selection.snapshot.json  
* Command 5: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-008

Expected result:

PASS if:

* DB bridge parity generator check returns exit code 0\.  
* Provider parity proof is present.  
* Adapter-selection evidence is present.  
* OPS closure decision evidence is present.

FAIL\_BEHAVIOR if:

* DB proof chain is isolated, contradictory, or claims unsupported QA pass by itself.  
* Provider parity proof labels are treated as unregistered acceptance tokens.

FAIL\_TOOLING if:

* Generator check fails after readiness was established.

TOOLING\_BLOCKED if:

* Required repo loci are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-008/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-008/primary.log`  
* `audit/qa/hde-epic032/checks/po-008/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-009: PO-009

Goal: Operations evidence for provider parity must remain evidence support and must not be treated by itself as QA success, epic closure, or standalone checklist completion.

Surface / D-goal mapping: D3 / OPS evidence non-claim boundary

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide

Repo-resident loci:

* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json.path_proof.txt`  
* QA-created: `audit/qa/hde-epic032/checks/po-009/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-009/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json  
* Command 3: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json.path\_proof.txt

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing OPS evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-009

Expected result:

PASS if:

* OPS closure status is visible.  
* OPS support evidence does not claim QA pass by itself.  
* OPS support evidence does not claim standalone checklist completion or epic closure.

FAIL\_BEHAVIOR if:

* OPS support evidence claims QA success, epic closure, or checklist completion by itself.

TOOLING\_BLOCKED if:

* OPS evidence or path-proof files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-009/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-009/primary.log`  
* `audit/qa/hde-epic032/checks/po-009/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-010: PO-010

Goal: The combined database bridge and provider parity evidence must support the relevant Fermentation row without claiming that permanent checklist drainage has already happened.

Surface / D-goal mapping: D3 / DB supportability without drainage claim

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF09.5 — HDE Build Checklist Fermentation

Repo-resident loci:

* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* Audit-proven: `artifacts/db_bridge/adapter_selection.snapshot.json`  
* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-010/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-010/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f artifacts/db\_bridge/provider\_parity.proof.json  
* Command 3: test \-f artifacts/db\_bridge/adapter\_selection.snapshot.json  
* Command 4: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-010

Expected result:

PASS if:

* Provider parity proof is present.  
* Adapter-selection evidence is present.  
* Selection-order evidence is visible.  
* No permanent PF09.5 drainage claim is made by this check.

FAIL\_BEHAVIOR if:

* Combined DB support is missing or contradictory.  
* PF09.5 drainage is claimed by Live QA evidence.

TOOLING\_BLOCKED if:

* Required DB evidence files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-010/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-010/primary.log`  
* `audit/qa/hde-epic032/checks/po-010/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-011: PO-011

Goal: Non-development database failure behavior must be deterministic, typed, numeric-free, secret-free, and based on observed selection behavior rather than synthetic or hardcoded evidence.

Surface / D-goal mapping: D3 / non-dev DB typed failure behavior

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF05 — HDE CLI/API Vendor Reference; PF14 — HDE Mechanics Guide

Repo-resident loci:

* Audit-proven: `tests/db/test_adapter_selection.py`  
* Audit-proven: `tests/evidence/test_generate_db_bridge_parity_nondev.py`  
* Audit-proven: `artifacts/runtime/env_connectivity.nondev_failure.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-011/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-011/result.json`

Dependencies required:

* Python 3  
* pytest  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: python \-c "import pytest; print('pytest import PASS')"  
* Command 2: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 3: test \-f tests/db/test\_adapter\_selection.py  
* Command 4: test \-f tests/evidence/test\_generate\_db\_bridge\_parity\_nondev.py  
* Command 5: test \-f artifacts/runtime/env\_connectivity.nondev\_failure.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No package installation is authorized by this plan.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-011

Expected result:

PASS if:

* DB adapter/non-dev evidence tests return exit code 0\.  
* Non-dev failure evidence includes numeric-free posture.  
* Non-dev failure evidence includes `missing_bridge_url`.  
* Non-dev failure evidence includes `BridgeUnavailable`.

FAIL\_BEHAVIOR if:

* Non-dev DB failure behavior is untyped, numeric-bearing, secret-bearing, synthetic-only, or contradictory.

FAIL\_TOOLING if:

* pytest invocation fails for tooling reasons after readiness was established.

TOOLING\_BLOCKED if:

* pytest or required repo loci are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-011/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-011/primary.log`  
* `audit/qa/hde-epic032/checks/po-011/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-012: PO-012

Goal: Database runtime behavior must avoid proactive probing beyond the sanctioned access path and must preserve typed failure posture when required runtime inputs are unavailable.

Surface / D-goal mapping: D3 / DB runtime access-path and failure posture

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF14 — HDE Mechanics Guide

Repo-resident loci:

* Audit-proven: `artifacts/runtime/env_connectivity.nondev_failure.json`  
* Audit-proven: `artifacts/db_bridge/adapter_selection.snapshot.json`  
* Audit-proven: `tests/db/test_adapter_selection.py`  
* QA-created: `audit/qa/hde-epic032/checks/po-012/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-012/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f artifacts/runtime/env\_connectivity.nondev\_failure.json  
* Command 3: test \-f artifacts/db\_bridge/adapter\_selection.snapshot.json  
* Command 4: test \-f tests/db/test\_adapter\_selection.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-012

Expected result:

PASS if:

* `no_proactive_probes` evidence is present.  
* `adapter_path_only` evidence is present.  
* Typed `missing_bridge_url` failure evidence is present.

FAIL\_BEHAVIOR if:

* Runtime posture shows proactive probing or untyped failure behavior.

TOOLING\_BLOCKED if:

* Required DB runtime evidence files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-012/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-012/primary.log`  
* `audit/qa/hde-epic032/checks/po-012/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-013: PO-013

Goal: Database posture evidence must remain governed, coherent, and aligned between human-readable and machine-readable evidence records.

Surface / D-goal mapping: D4 / human and machine evidence coherence

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF12 — HDE Schemas and Artifacts; PF19 — Glow QA Guide

Repo-resident loci:

* Audit-proven: `docs/evidence/INDEX.json`  
* Audit-proven: `docs/evidence/INDEX.sha256`  
* Audit-proven: `artifacts/evidence_index.jsonl`  
* Audit-proven: `artifacts/evidence_index.jsonl.sha256`  
* Audit-proven: `tools/evidence/update_evidence_index.py`  
* Audit-proven: `tools/evidence/validate_evidence_paths.py`  
* QA-created: `audit/qa/hde-epic032/checks/po-013/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-013/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f docs/evidence/INDEX.json  
* Command 3: test \-f docs/evidence/INDEX.sha256  
* Command 4: test \-f artifacts/evidence\_index.jsonl  
* Command 5: test \-f artifacts/evidence\_index.jsonl.sha256  
* Command 6: test \-f tools/evidence/update\_evidence\_index.py  
* Command 7: test \-f tools/evidence/validate\_evidence\_paths.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing evidence-index files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-013

Expected result:

PASS if:

* Human index exists.  
* Machine mirror exists.  
* Hash sentinels exist.  
* Evidence update check and path validation commands return exit code 0\.

FAIL\_BEHAVIOR if:

* Human and machine evidence records are incoherent.

FAIL\_TOOLING if:

* Evidence update/check commands fail due to stale or malformed generated evidence.

TOOLING\_BLOCKED if:

* Required ledgers, mirrors, sentinels, or validation scripts are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-013/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-013/primary.log`  
* `audit/qa/hde-epic032/checks/po-013/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-014: PO-014

Goal: Machine-readable evidence records must remain aligned with the human evidence record and must not carry stale, contradictory, or unclassified companion proof state.

Surface / D-goal mapping: D4 / Machine Mirror alignment

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF12 — HDE Schemas and Artifacts

Repo-resident loci:

* Audit-proven: `docs/evidence/INDEX.json`  
* Audit-proven: `artifacts/evidence_index.jsonl`  
* Audit-proven: `artifacts/evidence_index.jsonl.sha256`  
* Audit-proven: `ci/checks/check_mirror_schema.sh`  
* Audit-proven: `tools/evidence/validate_evidence_paths.py`  
* QA-created: `audit/qa/hde-epic032/checks/po-014/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-014/result.json`

Dependencies required:

* Python 3  
* Bash  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f docs/evidence/INDEX.json  
* Command 3: test \-f artifacts/evidence\_index.jsonl  
* Command 4: test \-f artifacts/evidence\_index.jsonl.sha256  
* Command 5: test \-f ci/checks/check\_mirror\_schema.sh  
* Command 6: test \-f tools/evidence/validate\_evidence\_paths.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing mirror files or scripts.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-014

Expected result:

PASS if:

* Human index and machine mirror exist.  
* Mirror schema check returns exit code 0\.  
* Evidence path validation returns exit code 0\.

FAIL\_BEHAVIOR if:

* Stale, contradictory, or unclassified companion proof state is detected.

FAIL\_TOOLING if:

* Mirror or path-validation tooling fails after readiness was established.

TOOLING\_BLOCKED if:

* Mirror files or validation scripts are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-014/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-014/primary.log`  
* `audit/qa/hde-epic032/checks/po-014/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-015: PO-015

Goal: Generated proof for this epic must fail closed when decisive evidence, proof companions, or check-mode predicates are missing, stale, contradictory, or outside the claimed proof family.

Surface / D-goal mapping: D4 / generated-proof fail-closed posture

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF14 — HDE Mechanics Guide; PF12 — HDE Schemas and Artifacts

Repo-resident loci:

* Audit-proven: `tools/evidence/generate_narrative_registry_diff.py`  
* Audit-proven: `tools/evidence/generate_db_bridge_parity.py`  
* Audit-proven: `tools/evidence/update_evidence_index.py`  
* Audit-proven: `tools/evidence/validate_evidence_paths.py`  
* Audit-proven: `tools/evidence/check_lf_endings.py`  
* Audit-proven: `ci/checks/check_evidence_index_hash.sh`  
* Audit-proven: `ci/checks/check_mirror_schema.sh`  
* QA-created: `audit/qa/hde-epic032/checks/po-015/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-015/result.json`

Dependencies required:

* Python 3  
* Bash  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f tools/evidence/generate\_narrative\_registry\_diff.py  
* Command 3: test \-f tools/evidence/generate\_db\_bridge\_parity.py  
* Command 4: test \-f tools/evidence/update\_evidence\_index.py  
* Command 5: test \-f tools/evidence/validate\_evidence\_paths.py  
* Command 6: test \-f tools/evidence/check\_lf\_endings.py  
* Command 7: test \-f ci/checks/check\_evidence\_index\_hash.sh  
* Command 8: test \-f ci/checks/check\_mirror\_schema.sh

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing proof scripts.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-015

Expected result:

PASS if:

* Narrative registry check mode returns exit code 0\.  
* DB bridge parity check mode returns exit code 0\.  
* Evidence index check mode returns exit code 0\.  
* Path validation, index hash, mirror schema, and LF checks return exit code 0\.

FAIL\_BEHAVIOR if:

* Generated proof passes despite missing, stale, contradictory, or outside-family decisive evidence.

FAIL\_TOOLING if:

* A generated-proof validator fails due to stale generated evidence or tooling posture.

TOOLING\_BLOCKED if:

* Any required proof script or checker is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-015/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-015/primary.log`  
* `audit/qa/hde-epic032/checks/po-015/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-016: PO-016

Goal: Database provider parity, bridge capability, and bridge fallback labels must not be treated as acceptance tokens unless Governance has registered those names.

Surface / D-goal mapping: D5 / DB proof-label non-token posture

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF04 — HDE-Governance

Repo-resident loci:

* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* Audit-proven: `docs/evidence/INDEX.json`  
* Audit-proven: `artifacts/evidence_index.jsonl`  
* QA-created: `audit/qa/hde-epic032/checks/po-016/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-016/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f artifacts/db\_bridge/provider\_parity.proof.json  
* Command 3: test \-f docs/evidence/INDEX.json  
* Command 4: test \-f artifacts/evidence\_index.jsonl

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing DB proof or evidence-index files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-016

Expected result:

PASS if:

* DB provider parity, bridge capability, and bridge fallback labels are not treated as acceptance tokens.  
* The result preserves non-token proof-label posture.

FAIL\_BEHAVIOR if:

* `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, or `DB_BRIDGE_FALLBACK_OK` is treated as a claimed acceptance token.

TOOLING\_BLOCKED if:

* Required DB proof or evidence-index files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-016/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-016/primary.log`  
* `audit/qa/hde-epic032/checks/po-016/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-017: PO-017

Goal: The existing database bridge fallback acceptance token may be used only for the scope it actually governs, and related unregistered labels must remain non-token proof obligations.

Surface / D-goal mapping: D5 / bridge fallback token-scope boundary

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF04 — HDE-Governance

Repo-resident loci:

* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-017/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-017/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f artifacts/db\_bridge/provider\_parity.proof.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing DB proof files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-017

Expected result:

PASS if:

* `DEV_DB_BRIDGE_FALLBACK_OK` is not broadened beyond dev bridge fallback scope.  
* Related unregistered proof labels remain non-token proof obligations.

FAIL\_BEHAVIOR if:

* `DB_BRIDGE_FALLBACK_OK`, `DB_PROVIDER_PARITY_OK`, or `DB_BRIDGE_CAPS_OK` is treated as a claimed acceptance token.  
* Existing dev bridge fallback token scope is broadened.

TOOLING\_BLOCKED if:

* Required DB proof file is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-017/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-017/primary.log`  
* `audit/qa/hde-epic032/checks/po-017/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-018: PO-018

Goal: The active in-scope Fermentation rows must be proven supportable to completion from current implementation and governed evidence without claiming physical checklist drainage ahead of its assigned maintenance step.

Surface / D-goal mapping: D5 / active Fermentation rows supportability without drainage

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF09.5 — HDE Build Checklist Fermentation

Repo-resident loci:

* Audit-proven: `audit/gates/narratives/keys_10x4.table.json`  
* Audit-proven: `audit/gates/narratives/registry.diff.json`  
* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-018/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-018/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/gates/narratives/keys\_10x4.table.json  
* Command 3: test \-f audit/gates/narratives/registry.diff.json  
* Command 4: test \-f artifacts/db\_bridge/provider\_parity.proof.json  
* Command 5: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-018

Expected result:

PASS if:

* Narrative router evidence exists.  
* Narrative registry evidence exists.  
* DB bridge/provider parity evidence exists.  
* OPS support evidence exists.  
* PF09.5 physical drainage is not claimed by this check.

FAIL\_BEHAVIOR if:

* Active-row support evidence is missing or contradictory.  
* PF09.5 physical drainage is claimed by Live QA.

TOOLING\_BLOCKED if:

* Required evidence family files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-018/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-018/primary.log`  
* `audit/qa/hde-epic032/checks/po-018/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-019: PO-019

Goal: Previously completed foundation rows must remain reused foundation and must not be re-scoped as new HDE-EPIC032 implementation work.

Surface / D-goal mapping: D5 / reused foundation boundary

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes; PF19 — Glow QA Guide

Repo-resident loci:

* Audit-proven: `README.md`  
* Audit-proven: `CHANGELOG.md`  
* Audit-proven: `docs/INDEX.md`  
* QA-created: `audit/qa/hde-epic032/checks/po-019/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-019/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f README.md  
* Command 3: test \-f CHANGELOG.md  
* Command 4: test \-f docs/INDEX.md

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing repo-doc anchors.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-019

Expected result:

PASS if:

* HDE-EPIC032 repo-doc markers are visible.  
* Current epic evidence remains scoped to the active narrative/database posture rows.  
* Reused foundation is not reclassified as new implementation work.

FAIL\_BEHAVIOR if:

* Reused foundation is claimed as newly implemented by HDE-EPIC032.

TOOLING\_BLOCKED if:

* Repo-doc anchor files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-019/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-019/primary.log`  
* `audit/qa/hde-epic032/checks/po-019/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-020: PO-020

Goal: Live QA must distinguish implementation readiness, operations evidence, QA result, permanent checklist drainage, and final epic closure as separate truth classes.

Surface / D-goal mapping: D5 / truth-class separation

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF19 — Glow QA Guide; PF10 — HDE-Build Notes

Repo-resident loci:

* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-020/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-020/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing OPS evidence.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-020

Expected result:

PASS if:

* OPS evidence remains support evidence.  
* QA result is not inferred from OPS evidence alone.  
* PF09.5 drainage is not claimed.  
* Final epic closure is not claimed by this check.

FAIL\_BEHAVIOR if:

* Implementation readiness, OPS evidence, QA result, checklist drainage, or closure collapse into a single claim.

TOOLING\_BLOCKED if:

* Required OPS evidence is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-020/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-020/primary.log`  
* `audit/qa/hde-epic032/checks/po-020/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-021: PO-021

Goal: The epic must not claim vendor-version runtime conformance from the narrative, registry, or database proof completed here.

Surface / D-goal mapping: D5 / vendor-version runtime non-claim

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF10 — HDE-Build Notes

Repo-resident loci:

* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-021/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-021/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json  
* Command 3: test \-f artifacts/db\_bridge/provider\_parity.proof.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-021

Expected result:

PASS if:

* Vendor-version runtime conformance is not claimed.  
* Narrative, registry, and database local proof are not overread as vendor-version runtime conformance.

FAIL\_BEHAVIOR if:

* Vendor-version runtime conformance is claimed from this epic’s local proof.

TOOLING\_BLOCKED if:

* Required evidence files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-021/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-021/primary.log`  
* `audit/qa/hde-epic032/checks/po-021/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-022: PO-022

Goal: The epic must not claim live provider behavior from local implementation proof, operations evidence, or database bridge evidence unless live-provider proof is separately scoped and governed.

Surface / D-goal mapping: D5 / live provider non-claim

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF19 — Glow QA Guide; PF10 — HDE-Build Notes

Repo-resident loci:

* Audit-proven: `audit/ops/hde-epic032/db-provider-parity/provider_parity_closure_decision.json`  
* Audit-proven: `artifacts/db_bridge/provider_parity.proof.json`  
* QA-created: `audit/qa/hde-epic032/checks/po-022/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-022/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f audit/ops/hde-epic032/db-provider-parity/provider\_parity\_closure\_decision.json  
* Command 3: test \-f artifacts/db\_bridge/provider\_parity.proof.json

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing evidence files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-022

Expected result:

PASS if:

* Live provider behavior is not claimed.  
* Closed-rails local implementation proof and OPS evidence remain separate from live provider proof.

FAIL\_BEHAVIOR if:

* Local proof, OPS evidence, or DB bridge evidence is represented as live provider behavior.

TOOLING\_BLOCKED if:

* Required evidence files are unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-022/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-022/primary.log`  
* `audit/qa/hde-epic032/checks/po-022/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-023: PO-023

Goal: Public Reader behavior must remain unchanged by this epic.

Surface / D-goal mapping: D5 / public Reader non-expansion

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF05 — HDE CLI/API Vendor Reference; PF17 — HDE Narratives Guide

Repo-resident loci:

* Audit-proven: `docs/ENDPOINTS_CATALOG.json`  
* Audit-proven: `adapter/http_reader.py`  
* QA-created: `audit/qa/hde-epic032/checks/po-023/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-023/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py  
* Command 2: test \-f docs/ENDPOINTS\_CATALOG.json  
* Command 3: test \-f adapter/http\_reader.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.  
* No remediation is authorized for missing Reader/catalog files.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-023

Expected result:

PASS if:

* `/reader` remains visible as the public Reader surface.  
* Invented proof routes such as `/api/reader-proof/v1` are absent.  
* Internal/dev routes remain APP\_ENV-gated and do not become public Reader expansion.

FAIL\_BEHAVIOR if:

* A new or invented public Reader proof route is detected.  
* Public Reader behavior is expanded by this epic’s proof.

TOOLING\_BLOCKED if:

* Endpoint catalog or Reader adapter source is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-023/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-023/primary.log`  
* `audit/qa/hde-epic032/checks/po-023/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

CHECK po-024: PO-024

Goal: Kronos must evaluate current proof obligations without turning Live QA planning into implementation, remediation, evidence fabrication, or closeout action.

Surface / D-goal mapping: D5 / Live QA role boundary

Rails: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev

Pins: LC\_ALL=C LANG=C TZ=UTC

PF anchors: PF27 — Canon Plan Templates; PF19 — Glow QA Guide

Repo-resident loci:

* QA-created: `audit/qa/hde-epic032/checks/po-024/primary.log`  
* QA-created: `audit/qa/hde-epic032/checks/po-024/result.json`

Dependencies required:

* Python 3  
* Step-0A QA-created harness

Preflight command(s):

* Command 1: test \-f audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py

Activation or installation remediation, if allowed:

* Run Step-0A if the harness is missing.

If readiness cannot be established:

* TOOLING\_BLOCKED.

PO command(s):

* Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC  
* Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-024

Expected result:

PASS if:

* Live QA remains proof-only.  
* No implementation action is performed by Live QA.  
* No remediation action beyond bounded QA evidence posture is performed.  
* No PF edit is performed.  
* No closeout action is performed by this check.

FAIL\_BEHAVIOR if:

* Live QA performs implementation, PF editing, evidence fabrication, or closeout action.

TOOLING\_BLOCKED if:

* The Step-0A harness is unavailable.

Primary evidence artifact:

* `audit/qa/hde-epic032/checks/po-024/primary.log`

Deliverables:

* `audit/qa/hde-epic032/checks/po-024/primary.log`  
* `audit/qa/hde-epic032/checks/po-024/result.json`

Tokens:

* intended\_tokens: \[\]  
* claimed\_tokens: \[\]

Execution order

Run checks in this order:

1. Step-0A Discovery posture and Live QA harness setup  
2. Step-0B Doc Delta Capture  
3. PO-001  
4. PO-002  
5. PO-003  
6. PO-004  
7. PO-005  
8. PO-006  
9. PO-007  
10. PO-008  
11. PO-009  
12. PO-010  
13. PO-011  
14. PO-012  
15. PO-013  
16. PO-014  
17. PO-015  
18. PO-016  
19. PO-017  
20. PO-018  
21. PO-019  
22. PO-020  
23. PO-021  
24. PO-022  
25. PO-023  
26. PO-024

Batch execution option

After Step-0A and Step-0B are complete, the PO may run the full remaining sequence with these paste-ready commands.

Command 1: export SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC

Command 2: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-001

Command 3: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-002

Command 4: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-003

Command 5: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-004

Command 6: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-005

Command 7: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-006

Command 8: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-007

Command 9: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-008

Command 10: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-009

Command 11: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-010

Command 12: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-011

Command 13: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-012

Command 14: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-013

Command 15: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-014

Command 16: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-015

Command 17: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-016

Command 18: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-017

Command 19: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-018

Command 20: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-019

Command 21: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-020

Command 22: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-021

Command 23: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-022

Command 24: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-023

Command 25: python audit/qa/hde-epic032/00\_meta/live\_qa\_harness.py po-024

Important batch posture:

* If any command exits nonzero, inspect that check’s `primary.log` and `result.json`.  
* Nonzero exit due to TOOLING\_BLOCKED means the required dependency or evidence locus is unavailable.  
* Nonzero exit due to FAIL\_TOOLING means tooling or generated evidence posture failed.  
* Nonzero exit due to FAIL\_BEHAVIOR means the observed proof contradicts the check’s PASS predicate.  
* Do not skip later checks silently; if a dependency chain is broken, record the blocked state.

Close-out deliverables

This runbook’s execution deliverables are:

* Discovery artifact: `audit/qa/hde-epic032/checks/step-0a-discovery/result.json`  
* Step logs: `audit/qa/hde-epic032/checks/<check_id>/primary.log`  
* Step log path proofs: `audit/qa/hde-epic032/checks/<check_id>/primary.log.path_proof.txt`  
* Step result sidecars: `audit/qa/hde-epic032/checks/<check_id>/result.json`  
* Manifest: `audit/qa/hde-epic032/qa_step_logs_manifest.json`  
* Manifest path proof: `audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt`  
* Doc-delta draft surface: `audit/docdeltas/hde-epic032_doc_deltas.md`  
* Doc-delta epic capture surface: `audit/qa/hde-epic032/00_meta/doc_deltas.md`  
* QA RCA & Doc Delta summary: NOT RUN until the final QA closeout review is assigned.  
* 

QA RCA & Doc Delta summary requirements

The final QA closeout review must:

* State what Live QA found.  
* Include Coverage vs QA Plan accounting for Step-0A, Step-0B, and PO-001 through PO-024 in plan order.  
* Point covered steps to governed evidence under `audit/qa/hde-epic032/checks/<check_id>/`.  
* Record unresolved FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED states as blockers when they affect acceptance.  
* Keep implementation readiness, operations evidence, QA result, PF09.5 drainage, formal close-pack completion, vendor-version runtime conformance, and live provider behavior as separate truth classes.  
* Treat documentation drainage as a follow-up unless truth/proof evidence is incomplete or untrusted.  
* Preserve non-claims for vendor-version runtime conformance, live provider behavior, public Reader expansion, PF edits, implementation action, and closeout action.

Review guardrails

Hard blockers for plan approval/execution:

* Any required executable repo locus not proven by PF10, PF-Canon, or the initial repo audit is blocked unless it is QA-created under `audit/qa/hde-epic032/`.  
* Any step that requires an unavailable repo path must record TOOLING\_BLOCKED.  
* Any step that needs pytest when pytest is unavailable must record TOOLING\_BLOCKED.  
* Any generated-proof or validation command that fails after readiness was established must record FAIL\_TOOLING unless the failure proves behavior contradiction.  
* Any observed behavior contradicting PASS predicates must record FAIL\_BEHAVIOR.  
* Any acceptance-token overclaim is FAIL\_BEHAVIOR.  
* Any vendor-version runtime conformance claim from this epic’s local proof is FAIL\_BEHAVIOR.  
* Any live provider behavior claim from local proof or OPS evidence is FAIL\_BEHAVIOR.  
* Any public Reader expansion is FAIL\_BEHAVIOR.  
* Any PF09.5 drainage claim made by this Live QA run is FAIL\_BEHAVIOR.  
* Any attempt by Live QA to implement product behavior, edit PF documents, create close-pack artifacts, or perform closeout is FAIL\_BEHAVIOR.

Documentation drainage posture:

* Documentation drainage is not an execution blocker by itself.  
* Truth and proof failures remain blockers.  
* Undrained doc deltas must remain visible in doc-delta surfaces.  
* PF10 live truth controls only where it explicitly speaks.

Evidence-root posture:

* Do not create run-id directories.  
* Do not use `EVIDENCE_ROOT`.  
* Do not use per-run root selection.  
* Do not use VCS state as evidence.  
* Every executed check must appear in `audit/qa/hde-epic032/qa_step_logs_manifest.json`.  
* Every PASS check must include its `primary.log` path in `evidence_artifacts`.

Future-step artifact posture:

* Until a step executes, its artifacts are NOT RUN.  
* Do not mark future-step artifacts as present.  
* Do not claim PASS from planned steps.  
* Do not claim closeout from this plan alone.

ASK OK?  
