Epic ID: HDE-EPIC034

Plan type: Live QA Plan / Runbook

Execution venue: Codespaces

Target environment: dev

Plan revision: r2

Date (UTC): 2026-06-26

Operators: PO, Kronos

Canon precedence statement

“PF10 supersedes all other PF docs where it speaks; otherwise follow PF-Canon.”

Canon set

* PF10 — HDE-Build Notes, relevant addenda:  
  * 2.8) PR-01 HDE-EPIC034  
  * 2.9) OPS-01 HDE-EPIC034  
  * 2.10) PR-02 HDE-EPIC034  
  * 2.11) PR-03 HDE-EPIC034  
  * 2.12) HDE-EPIC034 PR-04 Boundary-Proof Failure Loop and Escalation  
  * 2.14) W-001 Remediation PR-04 HDE-EPIC034  
  * 2.15) W-002 Remediation PR-04 HDE-EPIC034  
  * 2.16) W-003 Remediation PR-04 HDE-EPIC034  
  * 2.17) W-004 Remediation PR-04 HDE-EPIC034  
  * 2.18) W-005 Remediation PR-04 HDE-EPIC034  
  * 2.19) PR-05 HDE-EPIC034  
  * 2.22) OPS-02 HDE-EPIC034  
  * 2.23) PR-06 HDE-EPIC034  
  * 2.24) HDE-EPIC034 Implementation Retrospective  
  * 2.25) Post Implementation Audit Analysis HDE-EPIC034  
  * 2.26) Production-Affecting Epics Require At Least One Open-Rails Live QA Step  
* PF19 — Glow QA Guide  
* PF23 — Reality Audits  
* PF27 — Canon Plan Templates  
* PF05 — HDE CLI/API Vendor Reference

Scope statement

This plan evaluates the following in-scope proof obligations:

* Step-0B — Doc Delta Capture  
* PO-001 — recommended v2 chart behavior is selected distinctly from legacy v1 BodyGraph behavior  
* PO-002 — legacy v1 BodyGraph behavior remains explicitly identified as legacy behavior  
* PO-003 — vendor request construction uses canonical environment naming and version-neutral resource construction  
* PO-004 — v2 vendor authentication differs from legacy v1 authentication and no secret values are exposed  
* PO-005 — geocoding support appears only where the selected vendor route requires it and remains secret-safe  
* PO-006 — v2 response envelope preserves response type, success status, error posture, data identity, and route variant without raw vendor payload bodies  
* PO-007 — remaining v2 chart to internal BodyGraph-compatible flow gap remains visible  
* PO-008 — adapter and presenter boundary proof prevents vendor behavior from bypassing approved boundaries  
* PO-009 — boundary proof fails safely on unknown, unsupported, or unclassified current boundary behavior  
* PO-010 — public-surface drift cannot be silently ignored  
* PO-011 — offline deterministic refusal behavior is proven without live-success claim  
* PO-012 — bounded PO-authorized open-rails live vendor smoke proves only the narrow intended interaction  
* PO-013 — live vendor smoke evidence preserves secret safety and does not persist raw secrets, request bodies, response bodies, or full vendor payloads  
* PO-014 — live vendor smoke evidence is bound into governed evidence without rerunning live action  
* PO-015 — later error-handling, normalized-data-path, and full live-conformance work remain unclaimed  
* PO-016 — public Reader, public route, public flag, public payload, new service-home, and AI scope remain unclaimed  
* PO-017 — governed evidence records are coherent enough for QA planning without additional implementation, OPS, or evidence capture before QA begins  
* PO-018 — acceptance uses existing governed acceptance posture and does not create a new vendor-specific acceptance marker  
* qa-19-close-out-deliverables — closeout execution deliverables: QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary

This plan explicitly excludes:

* Running live vendor smoke outside the bounded PO-012 open-rails Live QA step.  
* Running OPS work outside the bounded PO-authorized open-rails Live QA command in PO-012.  
* Mutating product code.  
* Mutating public contracts.  
* Editing PF documents.  
* Creating acceptance tokens.  
* Public Reader expansion.  
* Public route, flag, or payload expansion.  
* New HTTP home or service-surface creation.  
* AI runtime, model, prompt, embedding, chatbot, or provider scope.  
* Completion claims for HDE-FERM008.3, HDE-FERM008.4, HDE-FERM008.5, or full HDE-FERM008 parent completion.  
* Epic closeout, merge, branch, PR, or board-state action.

PF10 overrides / conflicts

* PF10 records HDE-EPIC034 as Fermentation Pass 5 vendor-seam work centered on HumanDesignAPI v2 source selection, request shaping, response-envelope mapping, boundary proof, deterministic refusal behavior, bounded live vendor smoke, and evidence binding.  
* PF10 records that PR-06 binds already-produced OPS-02 evidence and does not rerun the live vendor smoke.  
* PF10 requires at least one bounded open-rails live QA step for production-affecting epics; this plan satisfies that requirement through PO-012.  
* PF10 records non-claims for full HumanDesignAPI v2 runtime conformance, later HDE-FERM008 subtasks, public Reader changes, public route/flag/payload expansion, new HTTP homes, and AI scope.  
* PF10 records the post-implementation audit as classification-only with no Must-act-now findings; this plan treats those audit findings as context, not as execution obligations.

PF23 anchors

PF23 consult posture: PF23 is an informational planning-time repo-reality context source only. It is not an execution artifact, acceptance token, required deliverable, operator command source, or blocker source.

Live repo validation posture: live repo access and the structured repo audit were used to validate current repo reality for executable loci before this plan was written. Live repo validation confirmed current existence of critical check scripts and resolved the repo-audit gap for ci/checks/check\_mirror\_schema.sh and ci/checks/check\_evidence\_index\_hash.sh.

REPO VALIDATION NOTE: the future PO run must still preflight dependencies in Codespaces, because live repo validation proves repo paths and scripts, not the PO’s runtime Python/pytest availability.

Environment and rails posture

Determinism pins for all checks:

* LC\_ALL=C  
* LANG=C  
* TZ=UTC

Default rails for this runbook:

* SAFE\_MODE=1  
* ALLOW\_NETWORK=0  
* APP\_ENV=dev

Rails changes by check:

* PO-012 Command 1 is the bounded PO-authorized open-rails Live QA command. It uses SAFE\_MODE=0, ALLOW\_NETWORK=1, APP\_ENV=dev, LC\_ALL=C, LANG=C, and TZ=UTC.  
* PO-012 Command 2 and all other checks run closed rails with SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev, LC\_ALL=C, LANG=C, and TZ=UTC.  
* PO-013 and PO-014 inspect the current PO-012 OPS-02 evidence and PR-06 binding evidence. They do not rerun OPS-02.

No VCS workflow content

This plan does not instruct branch, commit, merge, rebase, PR, or board operations. Any read-only repository sanity checks are non-gating and must not be used as PASS/FAIL criteria.

PO inputs needed

Required external inputs:

* PO authorization to run the bounded PO-012 open-rails Live QA command.  
* The PO execution environment must have HD\_API\_BASE\_URL, HD\_API\_KEY, and GEO\_API\_KEY set before PO-012 Command 1 runs.  
* The PO execution environment must have .venv/bin/python available before PO-012 Command 1 runs.

Secret posture:

* Do not paste or store HD\_API\_KEY, GEO\_API\_KEY, HD\_API\_BASE\_URL, or any secret value in QA artifacts.  
* PO-012 Command 1 must produce only secret-safe, redacted, summary-level evidence and must not persist raw secrets, raw request bodies, raw response bodies, or full vendor payloads.  
* PO-013 verifies the retained smoke evidence uses presence/redacted posture only.  
* If PO authorization or required secret-binding presence is unavailable for PO-012 Command 1, classify PO-012 as TOOLING\_BLOCKED and stop that check.

Evidence posture and directory structure

Canonical epic QA root:

* audit/qa/hde-epic034/

Check-centric evidence paths:

* audit/qa/hde-epic034/checks/\<check\_id\>/primary.log  
* audit/qa/hde-epic034/checks/\<check\_id\>/primary.log.path\_proof.txt

Stable meta paths:

* audit/qa/hde-epic034/00\_meta/  
* audit/qa/hde-epic034/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic034/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic034/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic034/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt

ounded PO-012 open-rails evidence paths:

* audit/ops/hde-epic034/ops-02/commands.txt  
* audit/ops/hde-epic034/ops-02/stdout.log  
* audit/ops/hde-epic034/ops-02/files\_sha256.txt  
* audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* audit/ops/hde-epic034/ops-02/request\_summary.json  
* audit/ops/hde-epic034/ops-02/result\_summary.json  
* audit/ops/hde-epic034/ops-02/ops02\_open\_rails\_smoke\_procedure.py

Per-run roots, run-id directories, EVIDENCE\_ROOT, RUN\_ID, and latest-run pointers are prohibited.

Step-log header schema expectations

Each primary.log must begin with a one-line JSON header containing:

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

Canonical PF27 header writer contract

This header-writer snippet is included exactly once as the canonical contract. The QA harness created by this plan uses the same keys and semantics.

```py
python - << 'PY'
import datetime
import json
import os

def env(name: str, default: str = "") -> str:
    value = os.environ.get(name)
    return value if value is not None else default

def env_json(name: str, default):
    raw = os.environ.get(name)
    if raw is None or raw == "":
        return default
    return json.loads(raw)

schema_version = "pf27.step_log_header.v1"
timestamp_utc = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
status = env("PASS_FAIL")
fail_status = "" if status == "PASS" else status
exit_code_raw = env("EXIT_CODE", "")
exit_code = int(exit_code_raw) if exit_code_raw != "" else None
if status == "PASS" and exit_code != 0:
    raise SystemExit("PASS requires EXIT_CODE=0")
commands = env_json("COMMANDS_JSON", [])
if isinstance(commands, str):
    commands = [commands]
command = "; ".join(commands) if commands else "N/A"
header = {
    "schema_version": schema_version,
    "timestamp_utc": timestamp_utc,
    "check_id": env("CHECK_ID"),
    "check_name": env("CHECK_NAME"),
    "status": status,
    "fail_status": fail_status,
    "command": command,
    "command_provenance": env("COMMAND_PROVENANCE", "Explicitly created"),
    "exit_code": exit_code,
    "evidence_artifacts": env_json("ARTIFACTS_JSON", []),
    "captured_env": {
        "SAFE_MODE": env("SAFE_MODE"),
        "ALLOW_NETWORK": env("ALLOW_NETWORK"),
        "APP_ENV": env("APP_ENV"),
        "LC_ALL": env("LC_ALL"),
        "LANG": env("LANG"),
        "TZ": env("TZ"),
    },
    "pf_refs": env_json("PF_REFS_JSON", []),
    "intended_tokens": env_json("INTENDED_TOKENS_JSON", []),
    "claimed_tokens": env_json("CLAIMED_TOKENS_JSON", []),
}
print(json.dumps(header, ensure_ascii=False))
PY
```

Shared setup — QA-created harness

Purpose: create a QA-only harness under the stable epic QA root. This harness reads current repo artifacts, writes PF27-shaped primary logs, writes sibling path proofs, and creates closeout deliverables. It does not create product behavior, run live vendor calls, edit PF documents, edit product code, install packages, or mutate non-QA artifacts.

Run this once before Step-0B.

Required dependencies:

* Python 3  
* mkdir  
* cat  
* Existing repository checkout in Codespaces

Preflight check:

* Command 1 creates audit/qa/hde-epic034/00\_meta/ if missing and writes the QA-created harness there.

If missing, activation/install action:

* None. If Python 3, mkdir, or cat is unavailable, stop and classify affected checks as TOOLING\_BLOCKED.

If still unavailable:

* TOOLING\_BLOCKED.

Command 1: mkdir \-p audit/qa/hde-epic034/00\_meta && cat \> audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py \<\<'PY' from **future** import annotations

import datetime import hashlib import json import os import re import subprocess import sys from pathlib import Path from typing import Callable

ROOT \= Path(".") EPIC\_ID \= "HDE-EPIC034" EPIC\_QA\_ROOT \= Path("audit/qa/hde-epic034") CHECKS\_ROOT \= EPIC\_QA\_ROOT / "checks" META\_ROOT \= EPIC\_QA\_ROOT / "00\_meta"

class ToolingBlocked(Exception): pass

class FailBehavior(Exception): pass

def utc\_now() \-\> str: return datetime.datetime.utcnow().replace(microsecond=0).isoformat() \+ "Z"

def sha256(path: Path) \-\> str: h \= hashlib.sha256() with path.open("rb") as f: for chunk in iter(lambda: f.read(8192), b""): h.update(chunk) return h.hexdigest()

def write\_path\_proof(path: Path) \-\> Path: if not path.exists(): raise ToolingBlocked(f"MISSING\_PATH\_FOR\_PROOF:{path}") proof \= Path(str(path) \+ ".path\_proof.txt") st \= path.stat() proof.write\_text( "\\n".join( \[ f"path: {path}", f"size\_bytes: {st.st\_size}", f"sha256: {sha256(path)}", f"mtime\_utc: {datetime.datetime.utcfromtimestamp(st.st\_mtime).replace(microsecond=0).isoformat()}Z", f"produced\_at\_utc: {utc\_now()}", "", \] ), encoding="utf-8", ) return proof

def read\_text(path: str | Path) \-\> str: p \= Path(path) if not p.exists(): raise ToolingBlocked(f"MISSING\_FILE:{p}") return p.read\_text(encoding="utf-8")

def load\_json(path: str | Path): return json.loads(read\_text(path))

def require\_file(path: str | Path, body: list\[str\]) \-\> None: p \= Path(path) if not p.exists(): raise ToolingBlocked(f"MISSING\_FILE:{p}") body.append(f"FILE\_OK {p} sha256={sha256(p)}")

def require\_contains(path: str | Path, needle: str, body: list\[str\]) \-\> None: text \= read\_text(path) if needle not in text: raise FailBehavior(f"MISSING\_TEXT:{path}:{needle}") body.append(f"TEXT\_OK {path} :: {needle}")

def require\_regex(path: str | Path, pattern: str, body: list\[str\]) \-\> None: text \= read\_text(path) if not re.search(pattern, text): raise FailBehavior(f"MISSING\_REGEX:{path}:{pattern}") body.append(f"REGEX\_OK {path} :: {pattern}")

def require\_json\_value(path: str | Path, dotted: str, expected, body: list\[str\]) \-\> None: value \= load\_json(path) for part in dotted.split("."): if isinstance(value, dict) and part in value: value \= value\[part\] else: raise FailBehavior(f"MISSING\_JSON\_KEY:{path}:{dotted}") if value \!= expected: raise FailBehavior(f"JSON\_VALUE\_MISMATCH:{path}:{dotted}:{value\!r}\!={expected\!r}") body.append(f"JSON\_OK {path} :: {dotted}={expected\!r}")

def run\_readonly(cmd: list\[str\], body: list\[str\], \*, behavior\_failure: bool \= True) \-\> None: body.append("COMMAND " \+ " ".join(cmd)) try: res \= subprocess.run(cmd, cwd=ROOT, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False) except FileNotFoundError as exc: raise ToolingBlocked(f"COMMAND\_MISSING:{cmd\[0\]}") from exc out \= res.stdout.strip() if out: body.append(out) body.append(f"EXIT\_CODE {res.returncode}") if res.returncode \!= 0: if behavior\_failure: raise FailBehavior(f"COMMAND\_FAILED:{' '.join(cmd)}:{res.returncode}") raise ToolingBlocked(f"COMMAND\_FAILED:{' '.join(cmd)}:{res.returncode}")

def require\_pytest(body: list\[str\]) \-\> None: res \= subprocess.run(\[sys.executable, "-c", "import pytest"\], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False) if res.returncode \!= 0: raise ToolingBlocked("PYTEST\_MISSING")

def check\_step0b(body: list\[str\]) \-\> None: require\_file("audit/docdeltas/hde-epic034\_doc\_deltas.md", body) require\_file("audit/qa/hde-epic034/00\_meta/doc\_deltas.md", body) body.append("DOC\_DELTA\_PRESENT\_OK")

def check\_po001(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json" require\_file(p, body) require\_contains(p, '"recommended\_internal\_vendor\_route\_family":"recommended\_v2\_chart"', body) require\_contains(p, '"route\_family":"recommended\_v2\_chart"', body) require\_contains(p, '"route\_variant":"coordinates\_chart"', body) require\_contains(p, '"runtime\_conformance\_claim":"NONE"', body)

def check\_po002(body: list\[str\]) \-\> None: require\_file("artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json", body) require\_file("artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log", body) require\_contains("artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json", '"legacy\_v1\_bodygraph\_route\_family":"legacy\_v1\_bodygraph"', body) require\_contains("artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log", "legacy\_v1\_bodygraph", body) require\_contains("artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log", "status=PASS", body)

def check\_po003(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json" require\_file(p, body) require\_file("engine/bodygraph/vendor\_client.py", body) require\_contains(p, '"version\_owner":"HD\_API\_BASE\_URL"', body) require\_contains(p, '"resource\_path":"charts/coordinates"', body) require\_contains(p, '"no\_double\_prefix\_posture":true', body) require\_contains("engine/bodygraph/vendor\_client.py", "def join\_vendor\_resource\_url", body) require\_contains("engine/bodygraph/vendor\_client.py", "HD\_API\_BASE\_URL", body)

def check\_po004(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json" require\_file(p, body) require\_contains(p, '"v2\_auth\_header\_posture":"Authorization: Bearer "', body) require\_contains(p, '"v1\_legacy\_auth\_header\_posture":"HD-Api-Key: "', body) require\_contains(p, '"credential\_env\_var":"HD\_API\_KEY"', body) require\_regex(p, r"", body)

def check\_po005(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json" require\_file(p, body) require\_contains(p, '"geocode\_env\_var":"GEO\_API\_KEY"', body) require\_contains(p, '"geocode\_header\_posture":"HD-Geocode-Key: "', body) require\_contains(p, '"geocode\_key\_requirement":"required"', body) require\_contains(p, '"geocode\_key\_requirement":"not needed"', body) require\_contains(p, '"geocode\_env\_var":"not applicable"', body)

def check\_po006(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json" require\_file(p, body) require\_contains(p, '"response\_envelope\_fields":\["timestamp","success","message","errorCode","type","data"\]', body) require\_contains(p, '"success\_status\_handling"', body) require\_contains(p, '"errorCode\_handling"', body) require\_contains(p, '"data\_payload\_body\_emitted":false', body) require\_contains(p, '"route\_variant":"coordinates\_chart"', body)

def check\_po007(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json" require\_file(p, body) require\_contains(p, '"schema\_gap\_status":"GAP\_RECORDED"', body) require\_contains(p, '"no\_compatibility\_by\_inference":true', body) require\_contains(p, '"normalized\_data\_path\_proof\_claim":"NONE"', body)

def check\_po008(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log" require\_file(p, body) require\_contains(p, "adapter/presenter boundary taxonomy proof", body) require\_contains(p, "adapter routes resolve to sanctioned presenter/emitter calls", body) require\_contains(p, "bounded\_static\_grammar\_posture", body)

def check\_po009(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log" require\_file(p, body) require\_regex(p, r"fail\[- \]closed", body) require\_contains(p, "unproven route-shaped forms fail closed", body) require\_contains(p, "unknown", body)

def check\_po010(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log" require\_file(p, body) require\_contains(p, "public\_route\_drift\_proof\_repair", body) require\_contains(p, "typed analyzer-owned route records replace string-first drift proof", body) require\_contains(p, "route\_proof\_contract\_required\_fields", body)

def check\_po011(body: list\[str\]) \-\> None: p \= "artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt" require\_file(p, body) require\_contains(p, "typed\_refusal\_posture=PROVIDER\_REFUSED before outbound transport under closed rails", body) require\_contains(p, "no\_dns\_socket\_http\_external\_io\_posture", body) require\_contains(p, "status=PASS", body) require\_contains(p, "no\_live\_vendor\_call\_claim=NONE", body)

def check\_po012(body: list\[str\]) \-\> None: p \= "audit/ops/hde-epic034/ops-02/result\_summary.json" require\_file(p, body) require\_json\_value(p, "classification", "PASS", body) require\_json\_value(p, "vendor\_attempted", True, body) require\_json\_value(p, "full\_v2\_conformance\_claim", False, body) require\_json\_value(p, "hde\_ferm008\_parent\_completion\_claim", False, body) require\_json\_value(p, "pf09\_subtask\_id", "HDE-FERM008.2", body)

def check\_po013(body: list\[str\]) \-\> None: for p in \[ "audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json", "audit/ops/hde-epic034/ops-02/request\_summary.json", "audit/ops/hde-epic034/ops-02/result\_summary.json", \]: require\_file(p, body) require\_contains("audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json", '"HD\_API\_KEY":"SET"', body) require\_contains("audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json", '"GEO\_API\_KEY":"SET"', body) require\_json\_value("audit/ops/hde-epic034/ops-02/result\_summary.json", "raw\_secret\_persisted", False, body) require\_json\_value("audit/ops/hde-epic034/ops-02/result\_summary.json", "full\_vendor\_payload\_persisted", False, body) require\_contains("audit/ops/hde-epic034/ops-02/request\_summary.json", '"input\_tuple\_posture":"synthetic non-PII coordinates tuple; full request body not persisted"', body)

def check\_po014(body: list\[str\]) \-\> None: p \= "audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log" require\_file(p, body) require\_contains(p, "ops02\_classification=PASS", body) require\_contains(p, "validation\_rails=closed rails for PR-06 binding; OPS-02 open-rails smoke not rerun", body) require\_contains(p, "final\_classification=PASS\_PR06\_EVIDENCE\_BINDING\_ONLY", body)

def check\_po015(body: list\[str\]) \-\> None: p \= "audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log" require\_file(p, body) require\_contains(p, "nonclaim\_hde\_ferm008\_3\_error\_retry\_rate\_limit\_mapping=true", body) require\_contains(p, "nonclaim\_hde\_ferm008\_4\_normalized\_live\_data\_path\_proof=true", body) require\_contains(p, "nonclaim\_hde\_ferm008\_5\_full\_live\_conformance\_evidence\_loop=true", body) require\_contains(p, "nonclaim\_full\_humandesignapi\_v2\_runtime\_conformance=true", body)

def check\_po016(body: list\[str\]) \-\> None: p \= "audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log" require\_file(p, body) for s in \[ "nonclaim\_public\_reader\_change=true", "nonclaim\_public\_route=true", "nonclaim\_public\_flag=true", "nonclaim\_public\_payload\_change=true", "nonclaim\_new\_http\_home=true", "nonclaim\_ai\_scope=true", \]: require\_contains(p, s, body)

def check\_po017(body: list\[str\]) \-\> None: require\_pytest(body) for p in \[ "tests/bodygraph/test\_vendor\_client.py", "tests/evidence/test\_hdapi\_v2\_contract\_inventory.py", "tools/evidence/validate\_evidence\_paths.py", "tools/evidence/check\_lf\_endings.py", "tools/evidence/update\_evidence\_index.py", "ci/checks/check\_mirror\_schema.sh", "ci/checks/check\_evidence\_index\_hash.sh", "ci/checks/check\_final\_lf.sh", "docs/evidence/INDEX.json", "docs/evidence/INDEX.sha256", "artifacts/evidence\_index.jsonl", "artifacts/evidence\_index.jsonl.sha256", "docs/acceptance\_map\_epic034.json", \]: require\_file(p, body) run\_readonly(\[sys.executable, "-m", "pytest", "tests/bodygraph/test\_vendor\_client.py", "tests/evidence/test\_hdapi\_v2\_contract\_inventory.py"\], body) run\_readonly(\[sys.executable, "tools/evidence/validate\_evidence\_paths.py"\], body) run\_readonly(\[sys.executable, "tools/evidence/check\_lf\_endings.py"\], body) run\_readonly(\[sys.executable, "tools/evidence/update\_evidence\_index.py", "--check"\], body) run\_readonly(\[sys.executable, "ci/checks/check\_mirror\_schema.sh"\], body) run\_readonly(\["bash", "ci/checks/check\_evidence\_index\_hash.sh"\], body) run\_readonly(\["bash", "ci/checks/check\_final\_lf.sh"\], body) require\_contains("docs/acceptance\_map\_epic034.json", '"EVIDENCE\_INDEX\_UPDATED\_OK"', body) require\_contains("docs/acceptance\_map\_epic034.json", '"MACHINE\_MIRROR\_UPDATED\_OK"', body) require\_contains("docs/acceptance\_map\_epic034.json", '"TESTS\_PASS\_OK"', body)

def check\_po018(body: list\[str\]) \-\> None: p \= "docs/acceptance\_map\_epic034.json" require\_file(p, body) require\_contains(p, '"acceptance\_claims\_mode":"baseline\_existing\_tokens\_only"', body) require\_contains(p, "No vendor-v2-specific acceptance token is minted or claimed.", body) text \= read\_text(p) if "VENDOR\_V2\_" in text or "HDAPI\_V2\_ACCEPTANCE" in text: raise FailBehavior("VENDOR\_SPECIFIC\_TOKEN\_PRESENT") body.append("NO\_VENDOR\_SPECIFIC\_ACCEPTANCE\_MARKER\_OK")

def check\_closeout(body: list\[str\]) \-\> None: expected \= \["step-0b-doc-delta-capture"\] \+ \[f"po-{i:03d}" for i in range(1, 19)\] entries \= \[\] for cid in expected: log \= CHECKS\_ROOT / cid / "primary.log" proof \= Path(str(log) \+ ".path\_proof.txt") if not log.exists(): raise ToolingBlocked(f"NOT\_RUN:{cid}:{log}") if not proof.exists(): raise ToolingBlocked(f"MISSING\_PATH\_PROOF:{cid}:{proof}") try: header \= json.loads(log.read\_text(encoding="utf-8").splitlines()\[0\]) except Exception as exc: raise ToolingBlocked(f"UNREADABLE\_HEADER:{cid}") from exc entries.append( { "check\_id": cid, "status": header.get("status", "UNKNOWN"), "log\_path": str(log), "path\_proof\_path": str(proof), } ) manifest \= EPIC\_QA\_ROOT / "qa\_step\_logs\_manifest.json" manifest.write\_text( json.dumps( {"schema\_version": "pf27.qa\_step\_logs\_manifest.v1", "epic\_id": EPIC\_ID, "entries": entries}, sort\_keys=True, separators=(",", ":"), )

+ "\\n", encoding="utf-8", ) write\_path\_proof(manifest) discovery \= META\_ROOT / "discovery\_artifact.md" discovery.write\_text( "\\n".join( \[ "\# HDE-EPIC034 Live QA Discovery Artifact", "", "Discovery posture: repo loci used by this Live QA plan were prechecked from current repo reality, structured repo audit, or QA-created output posture.", "Rails posture: SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev for Live QA proof checks.", "Out-of-scope boundaries: no live vendor rerun, no public Reader expansion, no new HTTP home, no AI scope, no acceptance-token minting.", "", \] ), encoding="utf-8", ) write\_path\_proof(discovery) rca \= META\_ROOT / "qa\_rca\_doc\_delta\_summary.md" rca.write\_text( "\\n".join( \[ "\# HDE-EPIC034 QA RCA and Doc Delta Summary", "", "Coverage vs plan:", *\[f"* {row\['check\_id'\]}: {row\['status'\]} — {row\['log\_path'\]}" for row in entries\], "", "Doc-delta posture:", "Step-0B records the current HDE-EPIC034 doc-delta surfaces. No PF document edit is performed by this runbook.", "", "Known non-claims:", "No full HumanDesignAPI v2 runtime conformance, no later HDE-FERM008.3/8.4/8.5 completion, no public Reader change, no public route/flag/payload expansion, no new HTTP home, and no AI scope is claimed by this Live QA run.", "", "Closeout posture:", "This closeout assembly check creates QA evidence deliverables only. It does not perform PO closeout, board update, merge, or canon drain.", "", \] ), encoding="utf-8", ) write\_path\_proof(rca) body.append(f"manifest={manifest}") body.append(f"discovery\_artifact={discovery}") body.append(f"qa\_rca\_doc\_delta\_summary={rca}")

CHECKS: dict\[str, tuple\[str, Callable\[\[list\[str\]\], None\], list\[str\], list\[str\], list\[str\]\]\] \= { "step-0b-doc-delta-capture": ("Step-0B — Doc Delta Capture", check\_step0b, \["audit/docdeltas/hde-epic034\_doc\_deltas.md", "audit/qa/hde-epic034/00\_meta/doc\_deltas.md"\], \["DOC\_DELTA\_PRESENT\_OK"\], \["DOC\_DELTA\_PRESENT\_OK"\]), "po-001": ("PO-001", check\_po001, \["artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json"\], \[\], \[\]), "po-002": ("PO-002", check\_po002, \["artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json", "artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log"\], \[\], \[\]), "po-003": ("PO-003", check\_po003, \["artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json", "engine/bodygraph/vendor\_client.py"\], \[\], \[\]), "po-004": ("PO-004", check\_po004, \["artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json"\], \[\], \[\]), "po-005": ("PO-005", check\_po005, \["artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json"\], \[\], \[\]), "po-006": ("PO-006", check\_po006, \["artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json"\], \[\], \[\]), "po-007": ("PO-007", check\_po007, \["artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json"\], \[\], \[\]), "po-008": ("PO-008", check\_po008, \["artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log"\], \[\], \[\]), "po-009": ("PO-009", check\_po009, \["artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log"\], \[\], \[\]), "po-010": ("PO-010", check\_po010, \["artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log"\], \[\], \[\]), "po-011": ("PO-011", check\_po011, \["artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt"\], \[\], \[\]), "po-012": ("PO-012", check\_po012, \["audit/ops/hde-epic034/ops-02/result\_summary.json"\], \[\], \[\]), "po-013": ("PO-013", check\_po013, \["audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json", "audit/ops/hde-epic034/ops-02/request\_summary.json", "audit/ops/hde-epic034/ops-02/result\_summary.json"\], \[\], \[\]), "po-014": ("PO-014", check\_po014, \["audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log"\], \[\], \[\]), "po-015": ("PO-015", check\_po015, \["audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log"\], \[\], \[\]), "po-016": ("PO-016", check\_po016, \["audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log"\], \[\], \[\]), "po-017": ("PO-017", check\_po017, \["tests/bodygraph/test\_vendor\_client.py", "tests/evidence/test\_hdapi\_v2\_contract\_inventory.py", "docs/evidence/INDEX.json", "docs/evidence/INDEX.sha256", "artifacts/evidence\_index.jsonl", "artifacts/evidence\_index.jsonl.sha256", "docs/acceptance\_map\_epic034.json"\], \["EVIDENCE\_INDEX\_UPDATED\_OK", "MACHINE\_MIRROR\_UPDATED\_OK", "EVIDENCE\_INDEX\_HASH\_OK", "EVIDENCE\_PATHS\_VALIDATED\_OK", "EVIDENCE\_PATH\_PROOFS\_OK", "TESTS\_PASS\_OK"\], \["EVIDENCE\_INDEX\_UPDATED\_OK", "MACHINE\_MIRROR\_UPDATED\_OK", "EVIDENCE\_INDEX\_HASH\_OK", "EVIDENCE\_PATHS\_VALIDATED\_OK", "EVIDENCE\_PATH\_PROOFS\_OK", "TESTS\_PASS\_OK"\]), "po-018": ("PO-018", check\_po018, \["docs/acceptance\_map\_epic034.json"\], \[\], \[\]), "qa-19-close-out-deliverables": ("Close-out deliverables", check\_closeout, \["audit/qa/hde-epic034/qa\_step\_logs\_manifest.json", "audit/qa/hde-epic034/00\_meta/discovery\_artifact.md", "audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md"\], \[\], \[\]), }

def run(check\_id: str) \-\> int: if check\_id not in CHECKS: print(f"UNKNOWN\_CHECK:{check\_id}", file=sys.stderr) return 99 check\_name, func, extra\_artifacts, intended, claimed\_on\_pass \= CHECKS\[check\_id\] check\_root \= CHECKS\_ROOT / check\_id check\_root.mkdir(parents=True, exist\_ok=True) primary \= check\_root / "primary.log" primary\_proof \= Path(str(primary) \+ ".path\_proof.txt") command\_text \= f"python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py {check\_id}" body: list\[str\] \= \[ f"check\_id={check\_id}", f"check\_name={check\_name}", f"command={command\_text}", "rails=SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev", "pins=LC\_ALL=C LANG=C TZ=UTC", \] status \= "PASS" rc \= 0 try: func(body) except ToolingBlocked as exc: status \= "TOOLING\_BLOCKED" rc \= 99 body.append(f"TOOLING\_BLOCKED:{exc}") except FailBehavior as exc: status \= "FAIL\_BEHAVIOR" rc \= 1 body.append(f"FAIL\_BEHAVIOR:{exc}") except Exception as exc: status \= "FAIL\_TOOLING" rc \= 2 body.append(f"FAIL\_TOOLING:{type(exc).**name**}:{exc}") artifacts \= \[str(primary), str(primary\_proof), \*extra\_artifacts\] header \= { "schema\_version": "pf27.step\_log\_header.v1", "timestamp\_utc": utc\_now(), "check\_id": check\_id, "check\_name": check\_name, "status": status, "fail\_status": "" if status \== "PASS" else status, "command": command\_text, "command\_provenance": "Copy/paste from plan via QA-created harness", "exit\_code": rc, "evidence\_artifacts": artifacts, "captured\_env": { "SAFE\_MODE": os.environ.get("SAFE\_MODE", ""), "ALLOW\_NETWORK": os.environ.get("ALLOW\_NETWORK", ""), "APP\_ENV": os.environ.get("APP\_ENV", ""), "LC\_ALL": os.environ.get("LC\_ALL", ""), "LANG": os.environ.get("LANG", ""), "TZ": os.environ.get("TZ", ""), }, "pf\_refs": \["PF10 — HDE-Build Notes", "PF19 — Glow QA Guide", "PF27 — Canon Plan Templates"\], "intended\_tokens": intended, "claimed\_tokens": claimed\_on\_pass if status \== "PASS" else \[\], } primary.write\_text(json.dumps(header, ensure\_ascii=False) \+ "\\n" \+ "\\n".join(body) \+ "\\n", encoding="utf-8") write\_path\_proof(primary) print(f"{check\_id} status={status} exit\_code={rc} primary={primary}") return rc

if **name** \== "**main**": if len(sys.argv) \!= 2: print("usage: hde034\_live\_qa\_harness.py \<check\_id\>", file=sys.stderr) raise SystemExit(99) raise SystemExit(run(sys.argv\[1\])) PY

Runbook Check Matrix

| check\_id | check\_name | D-goal | rails posture | command | expected result | primary evidence | deliverables | tokens | PF anchors |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| step-0b-doc-delta-capture | Step-0B — Doc Delta Capture | D0 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py step-0b-doc-delta-capture | PASS if doc-delta surfaces exist | audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log | primary log, path proof, doc-delta surfaces | DOC\_DELTA\_PRESENT\_OK | PF27, PF19 |
| po-001 | PO-001 | D1 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-001 | PASS if v2 recommended chart selection is present | audit/qa/hde-epic034/checks/po-001/primary.log | primary log, path proof, source-selection snapshot | none | PF10, PF19 |
| po-002 | PO-002 | D1 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-002 | PASS if v1 BodyGraph remains legacy | audit/qa/hde-epic034/checks/po-002/primary.log | primary log, path proof, v1 guard | none | PF10, PF19 |
| po-003 | PO-003 | D2 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-003 | PASS if version-neutral resource construction and HD\_API\_BASE\_URL posture are present | audit/qa/hde-epic034/checks/po-003/primary.log | primary log, path proof, request snapshot, vendor client | none | PF10, PF05 |
| po-004 | PO-004 | D2 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-004 | PASS if v2/v1 auth postures are distinct and redacted | audit/qa/hde-epic034/checks/po-004/primary.log | primary log, path proof, request snapshot | none | PF10, PF05 |
| po-005 | PO-005 | D2 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-005 | PASS if geocode posture is route-specific and secret-safe | audit/qa/hde-epic034/checks/po-005/primary.log | primary log, path proof, request snapshot | none | PF10, PF05 |
| po-006 | PO-006 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-006 | PASS if v2 envelope mapping proof is present and raw vendor payload body is not emitted | audit/qa/hde-epic034/checks/po-006/primary.log | primary log, path proof, response snapshot | none | PF10, PF19 |
| po-007 | PO-007 | D3 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-007 | PASS if schema gap remains visible | audit/qa/hde-epic034/checks/po-007/primary.log | primary log, path proof, response snapshot | none | PF10, PF19 |
| po-008 | PO-008 | D4 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-008 | PASS if adapter/presenter boundary proof shows sanctioned boundary posture | audit/qa/hde-epic034/checks/po-008/primary.log | primary log, path proof, boundary proof | none | PF10, PF19 |
| po-009 | PO-009 | D4 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-009 | PASS if unknown/unproven boundary behavior fails closed | audit/qa/hde-epic034/checks/po-009/primary.log | primary log, path proof, boundary proof | none | PF10, PF19 |
| po-010 | PO-010 | D4 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-010 | PASS if public-route drift proof is typed and cannot silently disable itself | audit/qa/hde-epic034/checks/po-010/primary.log | primary log, path proof, boundary proof | none | PF10, PF19 |
| po-011 | PO-011 | D5 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-011 | PASS if closed-rails refusal is proven without external I/O or live-success claim | audit/qa/hde-epic034/checks/po-011/primary.log | primary log, path proof, closed-rails refusal | none | PF10, PF19 |
| po-012 | PO-012 | D6 | Command 1: SAFE\_MODE=0 ALLOW\_NETWORK=1 APP\_ENV=dev; Command 2: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | Command 1: SAFE\_MODE=0 ALLOW\_NETWORK=1 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC .venv/bin/python audit/ops/hde-epic034/ops-02/ops02\_open\_rails\_smoke\_procedure.py; Command 2: python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-012 | PASS if bounded PO-authorized open-rails live smoke runs once and remains bounded/nonconformant | audit/qa/hde-epic034/checks/po-012/primary.log | primary log, path proof, OPS command/stdout/checksum/env/request/result summaries | none | PF10, PF19 |
| po-013 | PO-013 | D6 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-013 | PASS if current live-smoke evidence is redacted and no raw payloads are persisted | audit/qa/hde-epic034/checks/po-013/primary.log | primary log, path proof, OPS request/result/env summaries | none | PF10, PF19 |
| po-014 | PO-014 | D6 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-014 | PASS if PR-06 binds OPS evidence without rerunning live action in this check | audit/qa/hde-epic034/checks/po-014/primary.log | primary log, path proof, ops-smoke binding log | none | PF10, PF19 |
| po-015 | PO-015 | D7 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-015 | PASS if later HDE-FERM008 work remains unclaimed | audit/qa/hde-epic034/checks/po-015/primary.log | primary log, path proof, ops-smoke binding log | none | PF10, PF19 |
| po-016 | PO-016 | D7 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-016 | PASS if public and AI non-claims remain present | audit/qa/hde-epic034/checks/po-016/primary.log | primary log, path proof, ops-smoke binding log | none | PF10, PF19 |
| po-017 | PO-017 | D8 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-017 | PASS if targeted tests and evidence gates pass | audit/qa/hde-epic034/checks/po-017/primary.log | primary log, path proof, tests, ledgers, index/mirror artifacts | EVIDENCE\_INDEX\_UPDATED\_OK, MACHINE\_MIRROR\_UPDATED\_OK, EVIDENCE\_INDEX\_HASH\_OK, EVIDENCE\_PATHS\_VALIDATED\_OK, EVIDENCE\_PATH\_PROOFS\_OK, TESTS\_PASS\_OK | PF10, PF19 |
| po-018 | PO-018 | D8 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-018 | PASS if acceptance map uses baseline existing tokens only and no vendor-specific marker is present | audit/qa/hde-epic034/checks/po-018/primary.log | primary log, path proof, acceptance map | none | PF10, PF19 |
| qa-19-close-out-deliverables | Close-out deliverables | D9 | SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev | python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py qa-19-close-out-deliverables | PASS if manifest, discovery artifact, and QA RCA / Doc Delta summary are created and path-proven | audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log | primary log, path proof, manifest, discovery artifact, RCA/doc-delta summary | none | PF27, PF19 |

Check Blocks

#### CHECK step-0b-doc-delta-capture: Step-0B — Doc Delta Capture

Goal: Verify the current HDE-EPIC034 doc-delta surfaces exist before later Live QA checks rely on closeout or doc-delta posture. This step does not edit PF documents.

Required dependencies:

* Shared QA harness created.  
    
* Python.  
    
* Existing doc-delta surfaces:  
    
  * audit/docdeltas/hde-epic034\_doc\_deltas.md  
  * audit/qa/hde-epic034/00\_meta/doc\_deltas.md

Preflight check:

* The harness checks both doc-delta surfaces and writes the step primary log plus sibling path proof.

Preconditions:

* Run shared setup first.

Setup:

* None beyond shared setup.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log.  
3. Confirm the first line is a PF27 JSON header.  
4. Confirm audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt exists.  
5. Confirm DOC\_DELTA\_PRESENT\_OK appears only when status is PASS.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py step-0b-doc-delta-capture

What to look for:

* status=PASS in the primary log header.  
* DOC\_DELTA\_PRESENT\_OK in the primary log body.  
* claimed\_tokens includes DOC\_DELTA\_PRESENT\_OK only if status is PASS.

Required deliverables:

* audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log  
* audit/qa/hde-epic034/checks/step-0b-doc-delta-capture/primary.log.path\_proof.txt  
* audit/docdeltas/hde-epic034\_doc\_deltas.md  
* audit/qa/hde-epic034/00\_meta/doc\_deltas.md

PASS criteria tied to deliverables:

* PASS if both doc-delta surfaces exist and the primary log records DOC\_DELTA\_PRESENT\_OK.  
* PASS requires the primary log sibling path proof to exist and be listed in evidence\_artifacts.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if either required doc-delta surface is missing.  
* FAIL\_TOOLING if the primary log or sibling path proof cannot be written.

Blocked posture:

* If TOOLING\_BLOCKED, stop later checks until PO decides whether the missing doc-delta surface is expected.

#### CHECK po-001: PO-001

Goal: Verify that recommended v2 chart behavior is selected distinctly from legacy v1 BodyGraph behavior.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json.

Preflight check:

* The harness checks that the source-selection snapshot exists and contains recommended\_v2\_chart, coordinates\_chart, and no runtime conformance claim.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-001/primary.log.  
3. Confirm recommended\_v2\_chart and coordinates\_chart are recorded as proof lines.  
4. Confirm the sibling path proof exists.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-001

What to look for:

* TEXT\_OK lines for recommended\_v2\_chart.  
* TEXT\_OK line for coordinates\_chart.  
* runtime\_conformance\_claim remains NONE.

Required deliverables:

* audit/qa/hde-epic034/checks/po-001/primary.log  
* audit/qa/hde-epic034/checks/po-001/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json

PASS criteria tied to deliverables:

* PASS if source-selection evidence records recommended\_v2\_chart as the selected internal vendor route family and includes the v2 coordinates chart route variant.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if recommended\_v2\_chart is absent or runtime conformance is claimed.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing source-selection evidence locus.

#### CHECK po-002: PO-002

Goal: Verify that legacy v1 BodyGraph behavior remains explicitly identified as legacy behavior and is not treated as the recommended v2 path.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json.  
* artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log.

Preflight check:

* The harness checks both source-selection and legacy-guard evidence.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-002/primary.log.  
3. Confirm legacy\_v1\_bodygraph is recorded.  
4. Confirm the v1 legacy guard status is PASS.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-002

What to look for:

* TEXT\_OK lines for legacy\_v1\_bodygraph.  
* TEXT\_OK line for status=PASS in v1\_legacy\_guard.log.

Required deliverables:

* audit/qa/hde-epic034/checks/po-002/primary.log  
* audit/qa/hde-epic034/checks/po-002/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/source\_selection.snapshot.json  
* artifacts/vendor/hdapi\_v2/v1\_legacy\_guard.log

PASS criteria tied to deliverables:

* PASS if v1 BodyGraph is explicitly classified as legacy and the v1 legacy guard is PASS.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if legacy v1 is collapsed into the recommended v2 route family.  
* TOOLING\_BLOCKED if required artifacts are missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing legacy guard or source-selection locus.

#### CHECK po-003: PO-003

Goal: Verify that vendor request construction uses canonical environment naming and version-neutral resource construction rather than hardcoded versioned runtime paths.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.  
* engine/bodygraph/vendor\_client.py.

Preflight check:

* The harness checks request-shaping evidence and current vendor-client code surface.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-003/primary.log.  
3. Confirm version\_owner=HD\_API\_BASE\_URL and resource\_path posture are recorded.  
4. Confirm no\_double\_prefix\_posture is true.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-003

What to look for:

* HD\_API\_BASE\_URL as version owner.  
* version-neutral resource\_path.  
* no\_double\_prefix\_posture=true.  
* join\_vendor\_resource\_url appears in the vendor client.

Required deliverables:

* audit/qa/hde-epic034/checks/po-003/primary.log  
* audit/qa/hde-epic034/checks/po-003/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json  
* engine/bodygraph/vendor\_client.py

PASS criteria tied to deliverables:

* PASS if request-shaping evidence and code surface support HD\_API\_BASE\_URL ownership and version-neutral resource construction.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if request shaping depends on hardcoded runtime versioned path ownership.  
* TOOLING\_BLOCKED if required artifacts are missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing request-shaping or vendor-client locus.

#### CHECK po-004: PO-004

Goal: Verify that v2 vendor authentication differs from legacy v1 authentication and that no secret values are exposed.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.

Preflight check:

* The harness checks redacted v2 and legacy v1 auth postures.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-004/primary.log.  
3. Confirm Authorization: Bearer is present for v2.  
4. Confirm HD-Api-Key: is present for legacy v1.  
5. Confirm no raw secret value is emitted by the check.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-004

What to look for:

* v2\_auth\_header\_posture is Authorization: Bearer .  
* v1\_legacy\_auth\_header\_posture is HD-Api-Key: .  
* credential\_env\_var is HD\_API\_KEY.  
* Only redacted values appear.

Required deliverables:

* audit/qa/hde-epic034/checks/po-004/primary.log  
* audit/qa/hde-epic034/checks/po-004/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json

PASS criteria tied to deliverables:

* PASS if v2 and v1 auth are distinct and secret-safe.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if v2 auth uses the v1 legacy header or any raw secret value appears in proof.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing request-shaping locus.

#### CHECK po-005: PO-005

Goal: Verify that geocoding support is included only where the selected vendor route requires it and remains secret-safe.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json.

Preflight check:

* The harness checks route-specific geocode requirements and redacted geocode header posture.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-005/primary.log.  
3. Confirm required and not-needed geocode postures are both represented.  
4. Confirm HD-Geocode-Key appears only as redacted posture.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-005

What to look for:

* GEO\_API\_KEY as the geocode environment variable.  
* HD-Geocode-Key: .  
* geocode\_key\_requirement=required where applicable.  
* geocode\_key\_requirement=not needed for coordinates route.

Required deliverables:

* audit/qa/hde-epic034/checks/po-005/primary.log  
* audit/qa/hde-epic034/checks/po-005/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/request\_shaping.snapshot.json

PASS criteria tied to deliverables:

* PASS if geocode proof is route-specific and redacted.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if geocode is treated as universal or raw geocode credentials appear.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing request-shaping locus.

#### CHECK po-006: PO-006

Goal: Verify that the v2 response envelope preserves response type, success status, error posture, data identity, and route variant without emitting raw vendor payload bodies.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json.

Preflight check:

* The harness checks response-mapping evidence.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-006/primary.log.  
3. Confirm response envelope fields are present.  
4. Confirm data\_payload\_body\_emitted=false.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-006

What to look for:

* timestamp, success, message, errorCode, type, and data fields.  
* success\_status\_handling.  
* errorCode\_handling.  
* data\_payload\_body\_emitted=false.  
* route\_variant evidence.

Required deliverables:

* audit/qa/hde-epic034/checks/po-006/primary.log  
* audit/qa/hde-epic034/checks/po-006/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if response-envelope mapping posture is present and raw vendor payload bodies are not emitted.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if raw vendor payload bodies are emitted or response envelope fields are absent.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing response-mapping locus.

#### CHECK po-007: PO-007

Goal: Verify that any remaining gap between v2 chart data and existing internal BodyGraph-compatible flows remains visible and is not hidden by inference.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json.

Preflight check:

* The harness checks schema-gap and normalized-data-path non-claim evidence.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-007/primary.log.  
3. Confirm schema\_gap\_status=GAP\_RECORDED.  
4. Confirm normalized\_data\_path\_proof\_claim=NONE.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-007

What to look for:

* schema\_gap\_status=GAP\_RECORDED.  
* no\_compatibility\_by\_inference=true.  
* normalized\_data\_path\_proof\_claim=NONE.

Required deliverables:

* audit/qa/hde-epic034/checks/po-007/primary.log  
* audit/qa/hde-epic034/checks/po-007/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/response\_mapping.snapshot.json

PASS criteria tied to deliverables:

* PASS if the schema/compatibility gap is explicit and normalized data path completion is not claimed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if compatibility is inferred or normalized-data-path proof is claimed.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing response-mapping locus.

#### CHECK po-008: PO-008

Goal: Verify that the adapter and presenter boundary proof shows vendor behavior does not bypass approved engine, presentation, or serialization boundaries.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.

Preflight check:

* The harness checks the adapter/presenter boundary proof log.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-008/primary.log.  
3. Confirm adapter/presenter boundary taxonomy evidence is present.  
4. Confirm sanctioned presenter/emitter posture is present.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-008

What to look for:

* adapter/presenter boundary taxonomy proof.  
* adapter routes resolve to sanctioned presenter/emitter calls.  
* bounded\_static\_grammar\_posture.

Required deliverables:

* audit/qa/hde-epic034/checks/po-008/primary.log  
* audit/qa/hde-epic034/checks/po-008/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log

PASS criteria tied to deliverables:

* PASS if the boundary proof records sanctioned adapter/presenter posture and does not show vendor bypass.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if vendor behavior bypasses approved boundaries or proof cannot classify the boundary.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing adapter-boundary proof locus.

#### CHECK po-009: PO-009

Goal: Verify that the boundary proof fails safely on unknown, unsupported, or unclassified current boundary behavior.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.

Preflight check:

* The harness checks fail-closed boundary proof language.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-009/primary.log.  
3. Confirm fail-closed posture appears.  
4. Confirm unknown/unproven boundary behavior is not PASS-capable by silence.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-009

What to look for:

* fail closed / fail-closed proof posture.  
* unproven route-shaped forms fail closed.  
* unknown boundary language appears in the proof artifact.

Required deliverables:

* audit/qa/hde-epic034/checks/po-009/primary.log  
* audit/qa/hde-epic034/checks/po-009/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log

PASS criteria tied to deliverables:

* PASS if unknown or unproven boundary behavior is treated as fail-closed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if unknown/unproven behavior is PASS-capable or silently accepted.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing adapter-boundary proof locus.

#### CHECK po-010: PO-010

Goal: Verify that public-surface drift cannot be silently ignored or treated as acceptable without classification.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log.

Preflight check:

* The harness checks public-route drift repair posture.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-010/primary.log.  
3. Confirm public\_route\_drift\_proof\_repair is present.  
4. Confirm route proof required fields are recorded.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-010

What to look for:

* public\_route\_drift\_proof\_repair.  
* typed analyzer-owned route records.  
* route\_proof\_contract\_required\_fields.

Required deliverables:

* audit/qa/hde-epic034/checks/po-010/primary.log  
* audit/qa/hde-epic034/checks/po-010/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/adapter\_boundary\_proof.log

PASS criteria tied to deliverables:

* PASS if public-surface drift is typed and classified rather than silently ignored.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if route comparison disables itself or public drift is accepted without classification.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing adapter-boundary proof locus.

#### CHECK po-011: PO-011

Goal: Verify offline deterministic refusal behavior for the implemented vendor path without making a live-success claim.

Required dependencies:

* Shared QA harness created.  
* Python.  
* artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt.

Preflight check:

* The harness checks closed-rails refusal proof.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-011/primary.log.  
3. Confirm PROVIDER\_REFUSED appears before outbound transport.  
4. Confirm no live vendor call claim is made.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-011

What to look for:

* typed\_refusal\_posture=PROVIDER\_REFUSED before outbound transport under closed rails.  
* no\_dns\_socket\_http\_external\_io\_posture.  
* no\_live\_vendor\_call\_claim=NONE.  
* status=PASS.

Required deliverables:

* audit/qa/hde-epic034/checks/po-011/primary.log  
* audit/qa/hde-epic034/checks/po-011/primary.log.path\_proof.txt  
* artifacts/vendor/hdapi\_v2/closed\_rails\_refusal.txt

PASS criteria tied to deliverables:

* PASS if closed-rails refusal is proven without external I/O or live-success claim.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if outbound live behavior is attempted or live success is claimed in this closed-rails check.  
* TOOLING\_BLOCKED if required artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing closed-rails refusal locus.

  #### **CHECK po-012: PO-012**

Goal: Verify that the bounded live vendor smoke proves only the narrow live interaction it was designed to prove and is not treated as full v2 conformance. This is the one bounded PO-authorized open-rails Live QA step required for this production-affecting epic.

Required dependencies:

* Shared QA harness created.  
* Python.  
* .venv/bin/python.  
* PO authorization to run the bounded open-rails Live QA command.  
* HD\_API\_BASE\_URL, HD\_API\_KEY, and GEO\_API\_KEY present in the PO execution environment.  
* audit/ops/hde-epic034/ops-02/ops02\_open\_rails\_smoke\_procedure.py.  
* audit/ops/hde-epic034/ops-02/result\_summary.json after Command 1 runs.

Preflight check:

* Command 1 is the bounded open-rails live smoke procedure. It must run with SAFE\_MODE=0 and ALLOW\_NETWORK=1.  
* Command 2 runs the QA harness under closed rails to verify the retained OPS-02 result summary and write the PO-012 primary log plus sibling path proof.

If missing, activation/install action:

* If .venv/bin/python or the OPS-02 procedure script is unavailable, classify PO-012 as TOOLING\_BLOCKED and stop.  
* If PO authorization or required secret-binding presence is unavailable, classify PO-012 as TOOLING\_BLOCKED and stop.  
* Do not paste secret values into the terminal, plan, or evidence.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.  
* The PO has explicitly authorized the bounded open-rails live QA command for this step.

Setup:

* None.

Numbered PO actions:

1. Confirm PO authorization to run the bounded open-rails live QA command.  
2. Confirm HD\_API\_BASE\_URL, HD\_API\_KEY, and GEO\_API\_KEY are set in the Codespaces environment without printing their values.  
3. Run Command 1 exactly once.  
4. Run Command 2 after Command 1 completes.  
5. Open audit/qa/hde-epic034/checks/po-012/primary.log.  
6. Confirm classification=PASS for OPS-02.  
7. Confirm full\_v2\_conformance\_claim=false and HDE-FERM008 parent completion claim is false.  
8. Confirm the PO-012 primary log and sibling path proof exist.

Command 1:  
 SAFE\_MODE=0 ALLOW\_NETWORK=1 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC .venv/bin/python audit/ops/hde-epic034/ops-02/ops02\_open\_rails\_smoke\_procedure.py

Command 2:  
 SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-012

What to look for:

* OPS-02 result summary exists after Command 1\.  
* classification=PASS.  
* vendor\_attempted=true in retained OPS evidence.  
* full\_v2\_conformance\_claim=false.  
* hde\_ferm008\_parent\_completion\_claim=false.  
* pf09\_subtask\_id=HDE-FERM008.2.  
* command\_to\_output\_provenance=PASS in the retained OPS command transcript.  
* No raw secret values, full request bodies, full response bodies, or full vendor payload bodies are printed or persisted.

Required deliverables:

* audit/qa/hde-epic034/checks/po-012/primary.log  
* audit/qa/hde-epic034/checks/po-012/primary.log.path\_proof.txt  
* audit/ops/hde-epic034/ops-02/commands.txt  
* audit/ops/hde-epic034/ops-02/stdout.log  
* audit/ops/hde-epic034/ops-02/files\_sha256.txt  
* audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* audit/ops/hde-epic034/ops-02/request\_summary.json  
* audit/ops/hde-epic034/ops-02/result\_summary.json

PASS criteria tied to deliverables:

* PASS if the bounded open-rails command runs once under PO authorization and the retained OPS-02 evidence is bounded to HDE-FERM008.2.  
* PASS if the retained OPS-02 evidence does not claim full v2 conformance or HDE-FERM008 parent completion.  
* PASS if the retained OPS-02 evidence remains secret-safe.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if full v2 conformance or HDE-FERM008 parent completion is claimed.  
* FAIL\_BEHAVIOR if raw secrets, raw request bodies, raw response bodies, or full vendor payload bodies are persisted.  
* TOOLING\_BLOCKED if PO authorization, required secret-binding presence, .venv/bin/python, the OPS-02 procedure, or required retained OPS artifacts are missing.  
* FAIL\_TOOLING if the open-rails command, primary log, or sibling path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing OPS-02 live-smoke procedure or retained OPS-02 evidence locus.

  #### **CHECK po-013: PO-013**

Goal: Verify that the current PO-012 live vendor smoke evidence preserves secret safety and does not persist raw secrets, raw request bodies, raw response bodies, or full vendor payloads.

Required dependencies:

* Shared QA harness created.  
* Python.  
* PO-012 completed or explicitly dispositioned.  
* audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json.  
* audit/ops/hde-epic034/ops-02/request\_summary.json.  
* audit/ops/hde-epic034/ops-02/result\_summary.json.

Preflight check:

* The harness reads the current PO-012 OPS-02 redacted and summary evidence under closed rails. It does not rerun OPS-02.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.  
* PO-012 Command 1 has produced or refreshed the bounded open-rails OPS-02 evidence, or PO-012 has been explicitly classified as TOOLING\_BLOCKED.

Setup:

* None.

Numbered PO actions:

1. Run the command below after PO-012.  
2. Open audit/qa/hde-epic034/checks/po-013/primary.log.  
3. Confirm the evidence uses presence/redacted posture only.  
4. Confirm raw\_secret\_persisted=false and full\_vendor\_payload\_persisted=false.

Command 1:  
 SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-013

What to look for:

* HD\_API\_KEY and GEO\_API\_KEY appear only as presence/status, not values.  
* raw\_secret\_persisted=false.  
* full\_vendor\_payload\_persisted=false.  
* synthetic non-PII input tuple posture.  
* No raw request body, raw response body, or full vendor payload is present in the retained evidence.

Required deliverables:

* audit/qa/hde-epic034/checks/po-013/primary.log  
* audit/qa/hde-epic034/checks/po-013/primary.log.path\_proof.txt  
* audit/ops/hde-epic034/ops-02/env\_presence\_redacted.json  
* audit/ops/hde-epic034/ops-02/request\_summary.json  
* audit/ops/hde-epic034/ops-02/result\_summary.json

PASS criteria tied to deliverables:

* PASS if current PO-012 live-smoke evidence is secret-safe and does not persist raw secrets or full vendor payloads.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if raw secrets, raw request bodies, raw response bodies, or full vendor payloads are persisted.  
* TOOLING\_BLOCKED if PO-012 did not run or required retained OPS artifacts are missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing secret-safety OPS artifact locus.

  #### **CHECK po-014: PO-014**

Goal: Verify that the current PO-012 live vendor smoke evidence is bound into governed evidence without rerunning the live action in this check.

Required dependencies:

* Shared QA harness created.  
* Python.  
* PO-012 completed or explicitly dispositioned.  
* audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log.

Preflight check:

* The harness reads the PR-06 evidence-binding log under closed rails. It does not rerun OPS-02.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.  
* PO-012 has produced or verified the bounded open-rails live-smoke evidence.

Setup:

* None.

Numbered PO actions:

1. Run the command below after PO-012 and PO-013.  
2. Open audit/qa/hde-epic034/checks/po-014/primary.log.  
3. Confirm ops02\_classification=PASS.  
4. Confirm validation\_rails says OPS-02 open-rails smoke was not rerun in the PR-06 binding check.

Command 1:  
 SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-014

What to look for:

* ops02\_classification=PASS.  
* final\_classification=PASS\_PR06\_EVIDENCE\_BINDING\_ONLY.  
* validation\_rails=closed rails for PR-06 binding; OPS-02 open-rails smoke not rerun.

Required deliverables:

* audit/qa/hde-epic034/checks/po-014/primary.log  
* audit/qa/hde-epic034/checks/po-014/primary.log.path\_proof.txt  
* audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if PR-06 binds OPS-02 evidence without rerunning live action in this check.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if this check reruns live smoke or treats PR-06 binding as full conformance.  
* TOOLING\_BLOCKED if required PR-06 evidence-binding artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing PR-06 evidence-binding locus.

#### CHECK po-015: PO-015

Goal: Verify that later error-handling, normalized-data-path, and full live-conformance work remain unclaimed.

Required dependencies:

* Shared QA harness created.  
* Python.  
* audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log.

Preflight check:

* The harness checks PR-06 non-claim lines for later HDE-FERM008 subtasks.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-015/primary.log.  
3. Confirm the HDE-FERM008.3, HDE-FERM008.4, and HDE-FERM008.5 non-claims.  
4. Confirm full v2 runtime conformance is not claimed.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-015

What to look for:

* nonclaim\_hde\_ferm008\_3\_error\_retry\_rate\_limit\_mapping=true.  
* nonclaim\_hde\_ferm008\_4\_normalized\_live\_data\_path\_proof=true.  
* nonclaim\_hde\_ferm008\_5\_full\_live\_conformance\_evidence\_loop=true.  
* nonclaim\_full\_humandesignapi\_v2\_runtime\_conformance=true.

Required deliverables:

* audit/qa/hde-epic034/checks/po-015/primary.log  
* audit/qa/hde-epic034/checks/po-015/primary.log.path\_proof.txt  
* audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if later HDE-FERM008 work remains unclaimed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if later HDE-FERM008 completion or full runtime conformance is claimed.  
* TOOLING\_BLOCKED if required binding artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing PR-06 evidence-binding locus.

#### CHECK po-016: PO-016

Goal: Verify that public Reader expansion, public route expansion, public flag expansion, public payload expansion, new service-home creation, and AI scope remain unclaimed.

Required dependencies:

* Shared QA harness created.  
* Python.  
* audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log.

Preflight check:

* The harness checks PR-06 public and AI non-claim lines.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-016/primary.log.  
3. Confirm all public and AI non-claim lines are present.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-016

What to look for:

* nonclaim\_public\_reader\_change=true.  
* nonclaim\_public\_route=true.  
* nonclaim\_public\_flag=true.  
* nonclaim\_public\_payload\_change=true.  
* nonclaim\_new\_http\_home=true.  
* nonclaim\_ai\_scope=true.

Required deliverables:

* audit/qa/hde-epic034/checks/po-016/primary.log  
* audit/qa/hde-epic034/checks/po-016/primary.log.path\_proof.txt  
* audit/qa/hde-epic034/pr-06/ops\_smoke\_evidence\_binding.log

PASS criteria tied to deliverables:

* PASS if public and AI expansion remain unclaimed.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if public Reader, public route, public flag, public payload, new HTTP home, or AI scope is claimed.  
* TOOLING\_BLOCKED if required binding artifact is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing PR-06 evidence-binding locus.

#### CHECK po-017: PO-017

Goal: Verify that governed evidence records are coherent enough to support QA planning without requiring additional implementation, OPS, or evidence capture before QA begins.

Required dependencies:

* Shared QA harness created.  
* Python.  
* pytest importable in the current Codespaces environment.  
* tests/bodygraph/test\_vendor\_client.py.  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py.  
* tools/evidence/validate\_evidence\_paths.py.  
* tools/evidence/check\_lf\_endings.py.  
* tools/evidence/update\_evidence\_index.py.  
* ci/checks/check\_mirror\_schema.sh.  
* ci/checks/check\_evidence\_index\_hash.sh.  
* ci/checks/check\_final\_lf.sh.  
* docs/evidence/INDEX.json.  
* docs/evidence/INDEX.sha256.  
* artifacts/evidence\_index.jsonl.  
* artifacts/evidence\_index.jsonl.sha256.  
* docs/acceptance\_map\_epic034.json.

Preflight check:

* The harness checks Python and pytest availability before running targeted tests and evidence gates.

If missing, activation/install action:

* Do not install packages inside this plan. If pytest is missing, classify the check as TOOLING\_BLOCKED and ask the PO to supply the approved environment or authorize a separate dependency-remediation action.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.  
* PO-001 through PO-016 have produced primary logs or are explicitly accepted as not blocking.

Setup:

* None beyond shared setup.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-017/primary.log.  
3. Confirm targeted pytest ran.  
4. Confirm evidence path validation, LF checks, evidence-index check, mirror schema, evidence hash, and final LF checks ran.  
5. Confirm intended\_tokens and claimed\_tokens match only if status is PASS.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-017

What to look for:

* Exit code 0 for targeted pytest.  
* Exit code 0 for tools/evidence/validate\_evidence\_paths.py.  
* Exit code 0 for tools/evidence/check\_lf\_endings.py.  
* Exit code 0 for tools/evidence/update\_evidence\_index.py \--check.  
* Exit code 0 for ci/checks/check\_mirror\_schema.sh.  
* Exit code 0 for ci/checks/check\_evidence\_index\_hash.sh.  
* Exit code 0 for ci/checks/check\_final\_lf.sh.  
* Acceptance map contains the existing governed token names.

Required deliverables:

* audit/qa/hde-epic034/checks/po-017/primary.log  
* audit/qa/hde-epic034/checks/po-017/primary.log.path\_proof.txt  
* tests/bodygraph/test\_vendor\_client.py  
* tests/evidence/test\_hdapi\_v2\_contract\_inventory.py  
* docs/evidence/INDEX.json  
* docs/evidence/INDEX.sha256  
* artifacts/evidence\_index.jsonl  
* artifacts/evidence\_index.jsonl.sha256  
* docs/acceptance\_map\_epic034.json

PASS criteria tied to deliverables:

* PASS if targeted tests and evidence gates exit 0 and the acceptance map contains the existing governed tokens.  
    
* PASS requires the primary log sibling path proof.  
    
* PASS may claim these tokens only when the primary log status is PASS:  
    
  * EVIDENCE\_INDEX\_UPDATED\_OK  
  * MACHINE\_MIRROR\_UPDATED\_OK  
  * EVIDENCE\_INDEX\_HASH\_OK  
  * EVIDENCE\_PATHS\_VALIDATED\_OK  
  * EVIDENCE\_PATH\_PROOFS\_OK  
  * TESTS\_PASS\_OK

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if a proven test/check executes and reports mismatch.  
* TOOLING\_BLOCKED if pytest, Python, a required script, or a required evidence file is missing.  
* FAIL\_TOOLING if a command cannot execute due to invocation or permission issue.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing test/check/script/evidence locus not already validated by current repo reality.

#### CHECK po-018: PO-018

Goal: Verify that acceptance for this epic relies only on existing governed acceptance posture and does not create a new vendor-specific acceptance marker.

Required dependencies:

* Shared QA harness created.  
* Python.  
* docs/acceptance\_map\_epic034.json.

Preflight check:

* The harness checks the acceptance map’s baseline token posture and scans for obvious vendor-specific token strings.

Preconditions:

* Step-0B completed or explicitly accepted as not blocking.

Setup:

* None.

Numbered PO actions:

1. Run the command below.  
2. Open audit/qa/hde-epic034/checks/po-018/primary.log.  
3. Confirm baseline\_existing\_tokens\_only appears.  
4. Confirm NO\_VENDOR\_SPECIFIC\_ACCEPTANCE\_MARKER\_OK appears only when status is PASS.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py po-018

What to look for:

* acceptance\_claims\_mode=baseline\_existing\_tokens\_only.  
* “No vendor-v2-specific acceptance token is minted or claimed.”  
* NO\_VENDOR\_SPECIFIC\_ACCEPTANCE\_MARKER\_OK.  
* claimed\_tokens is \[\].

Required deliverables:

* audit/qa/hde-epic034/checks/po-018/primary.log  
* audit/qa/hde-epic034/checks/po-018/primary.log.path\_proof.txt  
* docs/acceptance\_map\_epic034.json

PASS criteria tied to deliverables:

* PASS if the acceptance map uses existing governed acceptance posture and does not contain an obvious vendor-specific acceptance marker.  
* PASS requires the primary log sibling path proof.

FAIL criteria tied to deliverables:

* FAIL\_BEHAVIOR if a vendor-specific acceptance token is present or implied.  
* TOOLING\_BLOCKED if the acceptance map is missing.  
* FAIL\_TOOLING if the log or path proof cannot be written.

Blocked posture:

* RERUN AUDIT REQUIRED for any missing acceptance-map locus.

#### CHECK qa-19-close-out-deliverables: Close-out deliverables

Goal: Produce the PF27-required closeout execution deliverables: QA step-log manifest, discovery artifact, and QA RCA / Doc Delta summary. This check does not perform PO closeout and does not claim epic closure.

Required dependencies:

* Shared QA harness created.  
* Python.  
* Existing primary logs and sibling path proofs for Step-0B and PO-001 through PO-018.

Preflight check:

* The harness checks every expected prior check primary log and sibling path proof before writing closeout deliverables.

If missing, activation/install action:

* Rerun the missing planned check under this Live QA Plan.  
* Do not invent a missing primary log.

If still unavailable:

* TOOLING\_BLOCKED.

Preconditions:

* Step-0B and PO-001 through PO-018 have run.

Setup:

* None beyond shared setup.

Numbered PO actions:

1. Run the command below after all prior checks have run.  
2. Open audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log.  
3. Open audit/qa/hde-epic034/qa\_step\_logs\_manifest.json.  
4. Confirm every expected check from Step-0B through PO-018 appears in the manifest.  
5. Open audit/qa/hde-epic034/00\_meta/discovery\_artifact.md.  
6. Open audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md.  
7. Confirm the closeout assembly does not claim PO closeout.

Command 1: SAFE\_MODE=1 ALLOW\_NETWORK=0 APP\_ENV=dev LC\_ALL=C LANG=C TZ=UTC python audit/qa/hde-epic034/00\_meta/hde034\_live\_qa\_harness.py qa-19-close-out-deliverables

What to look for:

* qa\_step\_logs\_manifest.json exists and is path-proven.  
* discovery\_artifact.md exists and is path-proven.  
* qa\_rca\_doc\_delta\_summary.md exists and is path-proven.  
* The qa-19 primary log has a PF27 header.  
* The qa-19 primary log status is PASS only if all expected prior check logs and sibling path proofs exist.  
* The closeout summary states that PO closeout is not claimed.  
* The manifest preserves PO-012 as the bounded open-rails Live QA step.  
* The manifest does not treat PO-013 or PO-014 as live-rerun checks.

Required deliverables:

* audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log  
* audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log.path\_proof.txt  
* audit/qa/hde-epic034/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic034/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic034/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic034/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt

PASS criteria tied to deliverables:

* PASS if the QA step-log manifest exists and lists every expected check with status, log\_path, and path\_proof\_path.  
* PASS if the manifest path proof exists and matches the manifest path.  
* PASS if discovery artifact exists and records no invented loci.  
* PASS if QA RCA / Doc Delta summary exists and includes coverage vs plan accounting.  
* PASS if the qa-19 primary log has a PF27 header and sibling path proof.  
* PASS does not claim PO closeout.

FAIL criteria tied to deliverables:

* TOOLING\_BLOCKED if one or more expected prior check primary logs or sibling path proofs is missing.  
* FAIL\_TOOLING if a primary log exists but has an unreadable header.  
* FAIL\_BEHAVIOR if closeout deliverables claim PO closeout, runtime vendor conformance, public Reader expansion, new HTTP home, AI scope, PF edits, or product implementation.

Blocked posture:

* If any prior check is NOT RUN or missing a path proof, stop the closeout assembly and rerun or disposition the missing check before using the closeout deliverables as complete coverage evidence.

Moon Loop and deviation posture

Moon Loop may repair only QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under audit/qa/hde-epic034/.

Moon Loop must not change product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, runtime conformance claims, public Reader claims, AI claims, or multiple implementation subsystems.

The bounded PO-012 open-rails Live QA command is planned QA execution, not Moon Loop remediation.

Non-QA-root remediation is not Moon Loop correction. If a later check would require changing product code, repo tests, evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems, stop and require an approved PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE route before using the changed state for final PASS-grade QA.

If a QA-created harness or header defect is corrected, preserve the earlier failed or blocked state in the same evidence stream and record the correction in the affected primary log. Do not reconstruct missing bytes.

Future-step artifact posture

Before a step runs, its primary log and sibling path proof are NOT RUN.

Before qa-19-close-out-deliverables runs, the manifest, discovery artifact, and QA RCA / Doc Delta summary are DEFERRED.

No future-step artifact may be treated as present until the step creates or verifies it.

Review guardrails for the PO

* Do not rerun OPS-02 outside PO-012 Command 1 unless the PO separately authorizes a new bounded open-rails action.  
* Do not treat PASS for PO-013 or PO-014 as permission to rerun OPS-02.  
* Do not treat PASS for PO-014 as full v2 live conformance.  
* Do not treat PO-017 token claims as new vendor-specific acceptance markers.  
* Do not treat qa-19-close-out-deliverables as PO closeout, merge, board update, or canon drain.  
* If any check reports TOOLING\_BLOCKED, do not reinterpret it as FAIL\_BEHAVIOR.  
* If any check reports FAIL\_BEHAVIOR, preserve the primary log and path proof before any remediation discussion.  
* If a missing dependency prevents a check from running, the correct result is TOOLING\_BLOCKED or FAIL\_TOOLING, not FAIL\_BEHAVIOR.  
* 

Closeout deliverables

When the full run is complete, the PO should have these stable closeout deliverables:

The PO should also retain the bounded PO-012 open-rails OPS-02 evidence outputs listed in the PO-012 check block. They are approval evidence for the PF10 live-truth requirement, not formal closeout deliverables.

* audit/qa/hde-epic034/qa\_step\_logs\_manifest.json  
* audit/qa/hde-epic034/qa\_step\_logs\_manifest.json.path\_proof.txt  
* audit/qa/hde-epic034/00\_meta/discovery\_artifact.md  
* audit/qa/hde-epic034/00\_meta/discovery\_artifact.md.path\_proof.txt  
* audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md  
* audit/qa/hde-epic034/00\_meta/qa\_rca\_doc\_delta\_summary.md.path\_proof.txt  
* audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log  
* audit/qa/hde-epic034/checks/qa-19-close-out-deliverables/primary.log.path\_proof.txt

ASK OK?  
