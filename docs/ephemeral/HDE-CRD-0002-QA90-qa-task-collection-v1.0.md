---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-CRD-0002-QA90-QA-TASK-COLLECTION
artifact_version: "1.0"
predecessor: none (the first QA-90 collection for HDE-CRD-0002)
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV, the session that wrote QA Plan v1.0 to v1.2)
session_disposition: continuing Kronos context, as the QA-70 handoff to QA-90 v1.0 routes it
invocation_binding: CRD / HDE-CRD-0002 / QA-90 / QA_PLAN v1.2 checks 1 to 15
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8; page state 2026-10-12T02:30:51.327Z; read in full at this invocation)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md (QA_PLAN v1.2; blob 66f6016cc75bd1ab4ff9730ea89e5e25c7ec629c; SHA-256 8068ea350a9239c83e692a552bac8d5561a914d8694835faf4d38e0ab69f64e9; 107,529 bytes; immutable; read at the head of amthorn78/glow-hdengine-v2#724, f9adfd754098b9953ecb7896490991f8c0d42cb3)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md (QA_PLAN_REVIEW v1.2, APPROVE by Isis (Isis-53), 2026-10-24T14:52:19Z; on main through amthorn78/glow-hdengine-v2#725)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE)
selection: Product Owner, "Steps: Checks 1 through 15" in the QA-90 handoff of 2026-10-24 = QA Plan v1.2 checks 1 to 15
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; unchanged since the approval)
observed_revision: 197c2234 (origin/main at authoring; amthorn78/glow-hdengine-v2#725 merged 2026-10-24T14:58:07Z; amthorn78/glow-hdengine-v2#724 open); code outside docs/ephemeral/ and docs/pfcanon/ identical to 0b15328d
routing: QA-100 — Execute Bounded QA Task — 100926.1, under the Product Owner's chosen execution arrangement
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90 (QA-90 is not an addendum producer)
created_at: 2026-10-24T15:16:40Z
---

# HDE-CRD-0002 — QA Task Collection v1.0 (QA-90): checks 1 to 15 of QA Plan v1.2

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Tasks | T01 to T15, one per selected check, each at attempt 1 (§5) |
| Selection | Product Owner "Steps: Checks 1 through 15" = Plan v1.2 checks 1 to 15; checks 16 to 21 are not selected (§3) |
| Pre-execution findings | None. No `QA_PREEXECUTION_FINDING`: every selected block is complete and resolves to current repository loci (§2.5) |
| Execution prerequisite | amthorn78/glow-hdengine-v2#724 merged, so Plan v1.2 is on `main` (check 1's Step-0B reads it from the clone; §2.5) |
| Execution arrangement | Not stated by the Product Owner. The tasks are executor-neutral; QA-100 records the actual executor, tools and venue (§4.1) |
| Evidence-only commit grant | Not stated. Without it the Product Owner commits the published evidence (§4.8) |
| Normalizations | NZ-01 to NZ-07 (§4.10). Each keeps the Plan's objective, target, rails, evidence identity and predicates |
| Publication | One `publish_crd_check_family` call per check through the QA-created helper of §4.7, smoke-validated (§2.4 row 1) |

This collection is preparation, not an execution result. It selects no step, executes no check, accepts no evidence and declares no PASS.

## 2. Sources and lineage

### 2.1 Approved base (immutable)

`docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md`, exactly blob `66f6016cc75b` (SHA-256 `8068ea350a9239c83e692a552bac8d5561a914d8694835faf4d38e0ab69f64e9`), approved by the QA-70 review v1.2. At authoring the file was on the head of amthorn78/glow-hdengine-v2#724 (open), not yet on `main`; the bytes read there equal the approved blob (verified with `git rev-parse` of the blob and `sha256sum`). The approval binds to those bytes; if amthorn78/glow-hdengine-v2#724 lands different bytes, neither the approval nor these tasks cover them.

### 2.2 Overlays

None. HDE Build Notes v13.7.8 is unchanged since the approval and carries no addendum after it. The approving review's notes are operator cautions, not overlays.

### 2.3 Aids (not overlays)

- The QA-70 reviews v1.0, v1.1 and v1.2: operator cautions N-1, N-4, N-5, N-8 (v1.0), N-101 (v1.1), N-201 and N-202 (v1.2), and the named risks FND-024 and IR-1 to IR-11.
- The QA Audit v1.0 (§5 facts; §7 inspection ledger).
- The QA-80 redline application reports v1.0 and v1.1.

### 2.4 Authoring observations (planning validation, not QA evidence)

Observed by Kronos in throwaway clones of `main` at `197c2234` (code identical to `0b15328d`), CPython 3.12.3 with CI's full install, closed rails, vendor and database names unset. Nothing was committed or pushed from them.

| # | Object | What ran | Result (observed) |
| :- | :- | :- | :- |
| 1 | Publication helper (§4.7; review v1.0 N-5; Glow QA Guide §3.4.8 "Execution-critical helper readiness") | In a fresh full-history clone on a branch, from its root, under the closed rails: the helper of §4.7 run as `python -c "exec(open(...).read())" <spec>` for (a) a PASS stand-in for `qa-01-preflight`, (b) a `TOOLING_BLOCKED` stand-in for `qa-02-ci-coverage` with no command, (c) a PASS stand-in whose body holds a CR byte; then §4.7's six read-only validators | (a) and (b) print `PUBLISHED` with the primary and manifest paths and exit 0; the manifest holds both checks. (c) prints `REFUSED: CR byte ...` and exits 1 before any write. The five command-line validators each exit 0; `validate_crd_check_family` lists the two checks. Changed paths: the ten updater-owned graph files and `audit/qa/hde-crd-0002/`. Repository-root resolution, imports, argument handling, closed-rails startup and the refusal path are thereby established |
| 2 | Check 12 counting (review v1.0 N-4) | §5 T12 step 1's section-scoped `awk` counters on the S19 record | `per-file rows 49`; `fixed rows 9 without disposition 0`; `routed rows 7 without disposition 0`. A naive `grep -c '^| S19-F'` gives 18, because §10 repeats the IDs |
| 3 | E-D interpreters (check 3) | `find_spec` of `setuptools` and `_distutils_system_mod` for each `/usr/bin/python3*`; venvs made with `--system-site-packages` and CI's requirements | `/usr/bin/python3` is 3.11.15 here; its venv seeds its own `setuptools` 79.0.1, so it does not meet E-D. `/usr/bin/python3.12` (3.12.3) imports dist-packages `setuptools` 68.1.2 but supplies `_distutils_system_mod`, so it does not meet E-D either. `/usr/bin/python3.13` (3.13.12): its venv imports `setuptools` 68.1.2 from `/usr/lib/python3/dist-packages` and `_distutils_system_mod` is not importable, which is E-D (NZ-02) |
| 4 | Check 3 build and verify | In a fresh full-history clone of `main` at `197c2234` (status empty), with the `/usr/bin/python3.13` venv of row 3 and CI's requirements: T03 steps 1 to 4 and 6 exactly as written, with `env -i` and no `HOME` in the allowlist, the scratch paths substituted (NZ-01). T03 step 5 was not run here | Step 1: `68.1.2 /usr/lib/python3/dist-packages/setuptools/__init__.py None`. Build exit 0; verify exit 0; `attestation.json` 28,163 bytes with `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, `validation_result` `PASS`, `release_admission` `PR06R_B_FINAL_PASS`, `source_commit` `197c2234`; compat line count 1; clone status empty. An earlier run with `HOME` added gave the same exits, count and status |
| 5 | Check 4 sentence | `hdctl --help` and `python -m engine.cli --help` with `COLUMNS` removed; whitespace collapsed | Both exit 0, stderr empty, stdouts byte-identical, the full S07 sentence occurs once. `COLUMNS` is unset in this container (NZ-03) |

### 2.5 Pre-execution assessment

Every selected block of Plan v1.2 is complete: environment, dependencies (§7 rule A), actions, PASS predicates and outcomes (block lines or rule B), deliverables and publication (§5). Every repository locus the tasks use is Audit-proven, canon-defined or proven at run time by check 1's Step-0B discovery (Plan §0 provenance block). No substantive Plan defect was found, so there is no `QA_PREEXECUTION_FINDING`.

Two execution-time conditions are recorded, not defects:
- **amthorn78/glow-hdengine-v2#724 must be merged** before T01 runs: Step-0B confirms "the QA Plan version in use is the approved one" from the clone (T01 step 6). If it is not merged, T01 records a Step-0B BLOCKER and the run stops (`TOOLING_BLOCKED`, routed to Kronos).
- **Check 3's interpreter** is chosen by E-D's defining properties (Plan §3.2; check 3's outcome "no interpreter meets step 1 in the venue"), not by the literal `/usr/bin/python3`, which is 3.11 in some venues (§2.4 row 3; NZ-02).

### 2.6 Carried lineage

- Plan v1.0 → review v1.0 `DENY` → v1.1 (QA-80) → review v1.1 `DENY` → v1.2 (QA-80) → review v1.2 `APPROVE`.
- CR-11 `APPROVED_AS_CHANGED`, alternative (a), applied in check 1 step 6 (T01).
- No earlier QA-90 task, QA-100 result or QA-110 decision exists for this change: every task is attempt 1.

## 3. Selection reconciliation

| Plan check | `check_id` | Selected | Task | Attempt | Depends on | State |
| :- | :- | :- | :- | :- | :- | :- |
| 1 | `qa-01-preflight` | Yes | T01 | 1 | amthorn78/glow-hdengine-v2#724 merged | Issued |
| 2 | `qa-02-ci-coverage` | Yes | T02 | 1 | T01 published | Issued |
| 3 | `qa-03-attestation-debian` | Yes | T03 | 1 | T01 published | Issued |
| 4 | `qa-04-showcompat-help` | Yes | T04 | 1 | T01 published | Issued |
| 5 | `qa-05-aux-preview-band` | Yes | T05 | 1 | T01 published | Issued |
| 6 | `qa-06-dev-harness-retired` | Yes | T06 | 1 | T01 published | Issued |
| 7 | `qa-07-dev-reader-gate` | Yes | T07 | 1 | T01 published | Issued |
| 8 | `qa-08-release-evidence-tooling` | Yes | T08 | 1 | T01 published | Issued |
| 9 | `qa-09-override-matrix` | Yes | T09 | 1 | T01 published | Issued |
| 10 | `qa-10-endpoint-catalog` | Yes | T10 | 1 | T01 published | Issued |
| 11 | `qa-11-template-and-documents` | Yes | T11 | 1 | T01 published | Issued |
| 12 | `qa-12-security-review` | Yes | T12 | 1 | T01 published | Issued |
| 13 | `qa-13-prepush-check` | Yes | T13 | 1 | T01 published | Issued |
| 14 | `qa-14-close-pack-writer` | Yes | T14 | 1 | T01 published | Issued |
| 15 | `qa-15-s01-removal` | Yes | T15 | 1 | T01 published | Issued |
| 16 to 21 | `qa-16-deployed-identity` to `qa-21-evidence-admission` | No | none | none | — | Not selected; each needs its own Product Owner selection. Check 21 depends on checks 1 to 20 being published (Plan §8) |

Order: T01 first; T02 to T15 in any order after T01 is published (Plan §8: checks 2 to 15 are independent). Caller order T01 to T15 is kept here. Grouping the fifteen into one execution session transports them; it grants no collective approval, and each check is still published by its own call.

## 4. Common execution contract

### 4.1 Executor, venue and authority (Plan §2; QA-90 "Product Owner execution choice")

- The Product Owner has not stated the executor, tools or venue. Any executor the Product Owner chooses may run T01 to T15, Kronos included; no human initiator is required, because no selected check makes a vendor call.
- Venue: any Linux shell that can form E-L (Plan §3.2): CPython 3.12, CI's full install, `ruby`, `bash`, `curl`, `git`, network access to GitHub and the package index for setup only. A Claude Code cloud container meets it (§2.4).
- QA-100 records the actual executor, venue, interpreter paths and times. Execution authority is not acceptance authority: evidence returns to Kronos at QA-110.

### 4.2 Attempts

Every task is attempt 1. Attempt 2 of any check exists only after Kronos's actual QA-110 decision on a first eligible fault (Plan §9). The executor never reruns a check on its own.

### 4.3 Setup before T01 (not a check)

Fixed scratch locations, all outside every repository (another location may be used if recorded, NZ-01):

```text
/tmp/hde-crd-0002-el           E-L clone (full history)
/tmp/hde-crd-0002-el-venv      E-L venv (CPython 3.12, CI's full install)
/tmp/hde-crd-0002-xdg-state    E-L's empty XDG_STATE_HOME
/tmp/hde-crd-0002-evidence     evidence checkout (full history), branch qa/hde-crd-0002-evidence
/tmp/hde-crd-0002-qa           helper and per-check spec and body files
```

1. `git clone https://github.com/amthorn78/glow-hdengine-v2 /tmp/hde-crd-0002-el` (no `--depth`). Then `git -C /tmp/hde-crd-0002-el checkout --detach origin/main`. Record `git -C /tmp/hde-crd-0002-el rev-parse HEAD` as the tested commit.
2. `python3.12 -m venv /tmp/hde-crd-0002-el-venv`, then from `/tmp/hde-crd-0002-el`: `/tmp/hde-crd-0002-el-venv/bin/python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` and `/tmp/hde-crd-0002-el-venv/bin/python -m pytest --version`.
3. `mkdir -p /tmp/hde-crd-0002-xdg-state /tmp/hde-crd-0002-qa`.
4. `git clone https://github.com/amthorn78/glow-hdengine-v2 /tmp/hde-crd-0002-evidence` (no `--depth`); `git -C /tmp/hde-crd-0002-evidence checkout -b qa/hde-crd-0002-evidence origin/main`. Its `main` must be at or after the tested commit with identical code (Plan §5.4).
5. Write the helper of §4.7 to `/tmp/hde-crd-0002-qa/publish_check.py`.
6. The shell for every check exports the default rails and the E-L environment:

```text
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
export XDG_STATE_HOME=/tmp/hde-crd-0002-xdg-state
export PATH=/tmp/hde-crd-0002-el-venv/bin:$PATH
unset HD_API_KEY GEO_API_KEY HD_API_BASE_URL HDAPI_BASE_URL DATABASE_URL GH_TOKEN GITHUB_TOKEN HDE_VENDOR_OVERRIDE_AUDIT_PATH ENGINE_ENV COLUMNS
cd /tmp/hde-crd-0002-el
```

### 4.4 Rails and `captured_env`

All fifteen checks run under the default rails (Plan §3.1). Every spec carries `captured_env` `{"LC_ALL":"C","LANG":"C","TZ":"UTC","SAFE_MODE":"1","ALLOW_NETWORK":"0","APP_ENV":"dev"}`, read from the check's shell when it ran (Plan §5.3 rule 2); if a value differs, record the actual value and stop (the check is `TOOLING_BLOCKED`, rails not as planned).

### 4.5 Step-local readiness (Plan §7 rule A)

Before its main commands, every task T02 to T15 runs and records under `=== CONTEXT ===`, from `/tmp/hde-crd-0002-el`:

```text
git rev-parse HEAD                          # equals the tested commit T01 recorded
git rev-parse --is-shallow-repository       # false
git status --porcelain                      # empty
python --version                            # Python 3.12.x
python -m pytest --version
python -c "import engine; print(engine.__file__)"   # /tmp/hde-crd-0002-el/engine/__init__.py
```

plus `--version` of each further tool the task names. T03 also reruns its step 1 read of the E-D venv. A failed read makes the check `TOOLING_BLOCKED` (never `FAIL_BEHAVIOR`); no installation happens inside a check; the environment is repaired outside the check before any later attempt.

### 4.6 Capture, body and status

- **Per-check files** (QA-created scratch, never committed): `/tmp/hde-crd-0002-qa/<check_id>/` holds `body.txt` (the primary's body) and `spec.json` (§4.7); for example `/tmp/hde-crd-0002-qa/qa-02-ci-coverage/body.txt`.
- **Body** (Plan §5.2), in this order: `=== CONTEXT ===` (tested commit and tree, environment class, interpreter path and version, rails, a `SET`/`UNSET` presence table for `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `ENGINE_ENV`, `COLUMNS`, the actor, start and end time, the readiness reads of §4.5); `=== COMMANDS ===` (each child command, its exit code, stdout and stderr, separated); `=== PREDICATES ===` (each predicate, observed value, PASS or FAIL); `=== NOTES ===` (normalizations applied, observations, nonclaims, and for a `TOOLING_BLOCKED` check the blocking precondition, why it could not be satisfied, whether it blocks closeout and the required follow-up; review v1.0 N-8).
- **LF only** (Plan §5.3 rule 1): before writing `body.txt`, normalize any CRLF with `sed 's/\r$//'` and note "CRLF normalized to LF".
- **Secret scan** (Plan §5.3 rule 3): before publishing, from the check's shell: `python -c "import os,sys; t=open(sys.argv[1],encoding='utf-8').read(); v=[os.environ[n] for n in ('HD_API_KEY','GEO_API_KEY','HD_API_BASE_URL','HDAPI_BASE_URL','DATABASE_URL') if os.environ.get(n)]; print('HIT' if any(x in t for x in v) or any(h in t for h in ('Authorization: Bearer ','HD-Api-Key: ','HD-Geocode-Key: ')) and '<redacted>' not in t else 'NO_HIT')" /tmp/hde-crd-0002-qa/qa-02-ci-coverage/body.txt` (example path for T02). E-L leaves the names unset, so `NO_HIT` is expected; a `HIT` quarantines the body outside the repository and makes the check `FAIL_TOOLING`.
- **`command` and `exit_code`** (Plan §5.2): `command` lists each executed child argv in order and `exit_code` is the last decisive child's status. T01, T06, T09 and T11 expect non-zero child exits; each runs its listed sequence as one `bash -c` script that asserts every child's expected status and exits 0 only if all hold, records that single invocation as `command`, and puts each child's real exit code and output in the body (Plan §5.2; review v1.1 N-101 for T01).
- **Status**: the task's PASS predicate and Outcomes line, else Plan §7 rule B in its order (`FAIL_TOOLING`, `TOOLING_BLOCKED`, `FAIL_BEHAVIOR`, `PASS`). A non-PASS status needs a one-line `status_reason`.

### 4.7 Publication and indexing (Plan §5.4 and §5.5; review v1.0 N-5)

**Helper** (QA-created, outside the repository, smoke-validated, §2.4 row 1). Content of `/tmp/hde-crd-0002-qa/publish_check.py`:

```text
import json, pathlib, sys
from tools.qa import qa_harness as qa
from tools.evidence import update_evidence_index as writer

spec = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding="utf-8"))
body = pathlib.Path(spec["output_file"]).read_bytes()
if b"\r" in body:
    raise SystemExit("REFUSED: CR byte in the primary body; normalize CRLF to LF first (Plan §5.3)")
result = qa.CheckResult(
    check_id=spec["check_id"],
    status=qa.Status(spec["status"]),
    status_reason=spec["status_reason"],
    check_name=spec["check_name"],
    command=tuple(tuple(argv) for argv in spec["command"]),
    command_provenance=spec["command_provenance"],
    exit_code=spec["exit_code"],
    output=body.decode("utf-8"),
    evidence_artifacts=tuple(spec["evidence_artifacts"]),
    pf_refs=tuple(spec["pf_refs"]),
    captured_env=tuple(sorted(spec["captured_env"].items())),
)
config = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=pathlib.Path.cwd())
primaries, manifest = writer.publish_crd_check_family(config, [result], captured_at_utc=spec["captured_at_utc"])
print("PUBLISHED", *[str(p) for p in primaries], str(manifest))
```

**Spec** (`/tmp/hde-crd-0002-qa/<check_id>/spec.json`), one JSON object with: `check_id`; `check_name` (the task's name); `status`; `status_reason` (`""` for PASS); `command` (a list of argv lists; `[]` when nothing ran); `command_provenance` (`"QA Plan v1.2 check N; QA-90 task TNN attempt 1; <normalizations applied, or none>"` written out, for example `"QA Plan v1.2 check 2; QA-90 task T02 attempt 1; normalizations: none"`; `"Not executed"` when nothing ran); `exit_code` (integer, or `null` when nothing ran); `output_file` (the body path); `evidence_artifacts` (`[]` unless the task names consumed evidence); `pf_refs` (the task's list); `captured_env` (§4.4); `captured_at_utc` (the check's finalization time, `date -u +%Y-%m-%dT%H:%M:%SZ`).

**Call**, one per check, from `/tmp/hde-crd-0002-evidence` under the default rails (§4.3 step 6 exports, with `cd /tmp/hde-crd-0002-evidence`):

```text
python -c "exec(open('/tmp/hde-crd-0002-qa/publish_check.py').read())" /tmp/hde-crd-0002-qa/qa-02-ci-coverage/spec.json
```

(the example is T02's; each task names its own spec). STOP if the output does not start with `PUBLISHED` (a refused publication changes nothing: correct the assembly from the preserved transcript and publish again; that is not a rerun. A second refusal of the same check goes to Kronos.)

**Then, read-only, from `/tmp/hde-crd-0002-evidence`** (Plan §5.4), each exit status and output recorded in the QA-100 result:

```text
python tools/evidence/update_evidence_index.py --check
python tools/evidence/orientation_demo.py --check
python tools/evidence/validate_evidence_paths.py
python ci/checks/check_mirror_schema.sh
python tools/evidence/check_lf_endings.py
python -c "import pathlib; from tools.qa.qa_harness import HarnessConfig, validate_crd_check_family as v; print(v(HarnessConfig(crd_id='HDE-CRD-0002', repo_root=pathlib.Path.cwd())))"
```

**Registration set per check** (Plan §5.5), shown for T02 (each task substitutes its own `check_id`): `audit/qa/hde-crd-0002/checks/qa-02-ci-coverage/primary.log` and `primary.log.path_proof.txt`; its manifest entry in `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` and that file's `.path_proof.txt`; Index keys `audit.qa.hde_crd_0002.checks.qa-02-ci-coverage.primary.log` and `audit.qa.hde_crd_0002.qa_step_logs_manifest` with their Mirror rows; and the ten updater-owned graph files (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.json.path_proof.txt`, `docs/evidence/INDEX.sha256`, `docs/evidence/INDEX.sha256.path_proof.txt`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.path_proof.txt`, `artifacts/evidence_index.jsonl.sha256`, `artifacts/evidence_index.jsonl.sha256.path_proof.txt`, `audit/gates/topology/orientation_demo.txt`, `audit/gates/topology/orientation_demo.txt.path_proof.txt`). Never hand-edit any of them, and never run the updater in write mode separately.

### 4.8 Evidence files and commit boundary (Plan §2, §5.6)

- Only the writer of §4.7 writes in the evidence checkout. Nothing else is written under `audit/qa/hde-crd-0002/` (no sidecar, no `00_meta/` file).
- **Evidence-only commit grant: not stated.** If the Product Owner grants it at execution, the executor may commit and push, on the one branch `qa/hde-crd-0002-evidence`, only `audit/qa/hde-crd-0002/**`, the ten graph files of §4.7 and its own QA-100 result record under `docs/ephemeral/`, and open one pull request; no other path, no merge, no force-push. Without the grant, the executor leaves the published files uncommitted in `/tmp/hde-crd-0002-evidence`, reports `git status --porcelain` there, and the Product Owner commits.
- Preserve attempt 1 (Plan §9): a published primary is committed before any attempt 2 republishes the same `check_id`.
- Expected CI selection for the evidence pull request: lanes `evidence` and `release`. Named risks: FND-024 (PR35-C1) and IR-7. A red run is classified from its log before any re-run.

### 4.9 Stop, recovery and cleanup (Plan §9)

- T01 `TOOLING_BLOCKED` (candidate changed, history unavailable, a Step-0B BLOCKER) stops the run: publish T01's primary and route to Kronos; T02 to T15 do not start.
- A readiness failure in one task blocks only that task.
- An interrupted run resumes at the first selected check without a published primary.
- Cleanup after the last task: delete `/tmp/hde-crd-0002-el`, `/tmp/hde-crd-0002-el-venv`, `/tmp/hde-crd-0002-xdg-state`, `/tmp/hde-crd-0002-qa03`, `/tmp/hde-crd-0002-qa05` and the E-D build clone. Keep `/tmp/hde-crd-0002-evidence` and `/tmp/hde-crd-0002-qa` until the evidence is committed and QA-110 has read the QA-100 result.

### 4.10 Normalizations (Glow QA Guide §3.4.7; QA-90 Execute step 5)

Each keeps the Plan's objective, target, rails, evidence identity and predicates; the executor records the ones it applies in `command_provenance` and the body.

| ID | Normalization | Basis |
| :- | :- | :- |
| NZ-01 | The fixed scratch paths of §4.3 instantiate the Plan's "throwaway clone" and "scratch directory"; another location may be used if recorded | Plan §3.2; check 3 step 2's substitution rule |
| NZ-02 | Check 3's E-D venv is made with the first of `/usr/bin/python3`, `/usr/bin/python3.13`, `/usr/bin/python3.12`, `/usr/bin/python3.11` whose venv meets step 1's properties (dist-packages `setuptools`; `_distutils_system_mod` not importable), each tried interpreter recorded. Python 3.11 venvs seed their own `setuptools`, and Ubuntu's 3.12 supplies the module, so in an Ubuntu 24.04 container the 3.13 interpreter is the one that meets it (§2.4 row 3). If none does, the check is `TOOLING_BLOCKED` as its Outcomes line states | Plan §3.2 E-D (defined by its properties); check 3's Outcomes ("no interpreter meets step 1 in the venue") and substitution rule |
| NZ-03 | `COLUMNS` is unset in the E-L shell (§4.3 step 6) and its prior presence recorded, so argparse wraps the check 4 help at the default width | Review v1.0 N-1 |
| NZ-04 | Check 12 step 1's counts use the section-scoped commands of T12 | Review v1.0 N-4 |
| NZ-05 | T01, T06, T09 and T11 run their expected-non-zero sequences in one asserting `bash -c` script; T01's `ls -l` of an absent doc-delta surface (exit 2) is asserted there | Plan §5.2; review v1.1 N-101 |
| NZ-06 | Publication runs the helper file through `python -c "exec(...)"` from the evidence checkout's root: the same `python -c` invocation Plan §5.4 names, with the code read from a recorded file | Plan §5.4; review v1.0 N-5 |
| NZ-07 | Check 3's builder commands keep the Plan's `env -i` allowlist exactly; the executor adds no variable (not `HOME`) to it. As written, without `HOME`, the build and verify exit 0 here (§2.4 row 4) | Plan check 3 step 2 |

### 4.11 Return to QA-110

QA-100 returns, per task: the state (`COMPLETE`, `PARTIAL`, `BLOCKED`, `FAILED` or `NOT_EXECUTED`); the check's status; the primary's path, size and SHA-256; its manifest entry; the two Index keys present; the path proofs validating; §4.7's six validator results; the evidence commit and pull request (or the uncommitted state when no grant); the attempt number; the executor and venue; and every normalization and gap. Missing indexing is reported as incomplete work, never as PASS.

## 5. Tasks

Every task: change HDE-CRD-0002; approved Plan v1.2 (blob `66f6016cc75b`); review v1.2; Audit v1.0; attempt 1; default rails; publication by §4.7 with the spec values listed; return per §4.11. "Env" names the Plan class; §4.3 instantiates it.

### T01 `qa-01-preflight` — Candidate, environment and Step-0B preflight (Plan check 1)

- **Env:** E-L. **Depends on:** amthorn78/glow-hdengine-v2#724 merged. **Bootstrap:** this task is the readiness bootstrap; its steps 1 to 4 are its own readiness.
- **Actions** (from `/tmp/hde-crd-0002-el`; steps 1, 6 and 7 run inside one asserting `bash -c` script, NZ-05):
  1. `git rev-parse HEAD`; `git rev-parse HEAD^{tree}`; `git rev-parse --is-shallow-repository`; `git cat-file -e '7136040^{commit}'`; `git diff --stat 0b15328d585a764c124936b4524b766525daf1d9 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'`.
  2. `sha256sum catalog/manifest.json`; `python -c "import json; m=json.load(open('catalog/manifest.json')); print(m['version'], m['built_at_utc'], len(m['files']))"`; `hdctl --version`.
  3. `python --version`; `python -m pytest --version`; `ruby --version`; `bash --version`; `curl --version`; `git --version`; `python -c "import engine; print(engine.__file__)"`.
  4. Presence (`SET`/`UNSET`) of `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `ENGINE_ENV`: `for n in HD_API_KEY GEO_API_KEY HD_API_BASE_URL HDAPI_BASE_URL DATABASE_URL GH_TOKEN GITHUB_TOKEN HDE_VENDOR_OVERRIDE_AUDIT_PATH ENGINE_ENV; do [ -n "${!n+x}" ] && echo "$n SET" || echo "$n UNSET"; done`.
  5. `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/validate_evidence_paths.py`; `python ci/checks/check_mirror_schema.sh`; `python tools/evidence/check_lf_endings.py`; `python scripts/release_id_recompute.py --check-manifest-only`.
  6. Step-0B (Plan check 1 step 6; CR-11 as decided):
     - Discovery: `python -m pytest -p no:cacheprovider --collect-only -q` for each selector of Plan checks 2 to 14 and 21, exactly as those blocks name them (twenty selectors; Audit §7 item 2 counts); `test -e` each of `tools/ci/prepush_check.py`, `tools/evidence/build_release_attestation.py`, `tools/evidence/generate_a7_transport_proofs.py`, `ci/checks/check_cli_help.sh`, `scripts/release_id_recompute.py`; `git ls-files -- tests/retired_tests.md docs/acceptance/reader_a7_crib.md docs/adr/hde/close_pack_writer_adr.md` (output recorded verbatim); `ls docs/pfcanon | grep PF10` and `sha256sum` of that file; `git hash-object docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md` (expected `66f6016cc75bd1ab4ff9730ea89e5e25c7ec629c`, the approved blob).
     - Doc-delta surfaces: `git ls-files -- audit/docdeltas/hde-crd-0002_doc_deltas.md audit/qa/hde-crd-0002/00_meta/doc_deltas.md`; `ls -l audit/docdeltas/hde-crd-0002_doc_deltas.md audit/qa/hde-crd-0002/00_meta/doc_deltas.md` (exit 2 when absent, asserted, NZ-05). An existing surface: record its path, size and SHA-256 and leave it untouched.
     - Capture: BLOCKERS `S0B-B01` upward and CAVEATS `S0B-C01` upward, each generated from the outputs above; plan-versus-execution drift recorded with the executed command; "no deltas" only when both lists are empty and neither surface exists.
  7. `git status --porcelain`.
- **PASS:** step 1 prints `false` for the shallow read, `7136040` resolves, the diff is empty; manifest SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, `1.3.0 2026-08-24T18:04:49Z 45`, `hdctl --version` prints exactly `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)`; Python 3.12.x, pytest, `ruby`, `bash`, `curl`, `git` present; `engine` under `/tmp/hde-crd-0002-el`; every step 4 name `UNSET`; every validator exits 0; every selector collects at least its Audit count; the three documents listed; the Plan blob equals the approved one; both doc-delta surfaces recorded; Step-0B has no BLOCKER; status empty.
- **Outcomes** (Plan check 1; never `FAIL_BEHAVIOR`): shallow or `7136040` unresolvable → `TOOLING_BLOCKED` (reclone per §4.3); missing tool or install, or validator crash → `TOOLING_BLOCKED` or `FAIL_TOOLING` with the cause; non-empty diff or different `release_id` → `TOOLING_BLOCKED` ("candidate changed"), stop the run, route to Kronos; a Step-0B BLOCKER (missing entrypoint, selector, document, or a Plan blob other than the approved one) → `TOOLING_BLOCKED`, stop, route to Kronos.
- **Spec:** `check_name` "Candidate, environment and Step-0B preflight"; `pf_refs` `["PF27-Canon-Plan-Templates","PF19-Canon-Glow-QA-Guide"]`; `command` the single `bash -c` script invocation plus the step 2 to 5 argvs in order.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-01-preflight/primary.log`. Publish T01 before any other task.

### T02 `qa-02-ci-coverage` — Every test in a lane, owner refusal, filter equality (Plan check 2; S03, S04, S05)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:**
  1. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py::test_every_tracked_test_module_is_reached_by_a_lane_or_full_validation_target tests/evidence/test_rails_ci_workflow_integration.py::test_workflow_path_filter_skips_exactly_the_classifier_no_lane_documentation_paths tests/tools/test_prepush_check.py::test_coverage_matches_the_binding_definition_and_the_guard_on_the_repository`.
  2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_rails_ci_workflow_integration.py -k qa_tool`.
  3. `` awk -F' [|] ' '/^[|] `tests\//{n++; if ($2 ~ /^ *$/ || $3 !~ /^20[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/) print "BAD", $1} END{print n" rows"}' tests/retired_tests.md ``, then `` git ls-files -- $(grep -o '^| `tests/[^`]*`' tests/retired_tests.md | tr -d '|` ') | wc -l ``.
  4. Record, without re-running, hosted push run 39699657729 on `1a4c8ab` (all seven lanes `success`, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; Reality Audit E-003) as cited context.
- **PASS:** "3 passed"; "2 passed"; no `BAD` line, `66 rows`, tracked count `0`; exit 0 each. **Outcomes:** test failure → `FAIL_BEHAVIOR` with the node; collection or environment error → `FAIL_TOOLING`.
- **Spec:** `check_name` "Every test in a lane, owner refusal, filter equality"; `pf_refs` `["PF19-Canon-Glow-QA-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-02-ci-coverage/primary.log`.

### T03 `qa-03-attestation-debian` — Attestation builds under a distribution-patched setuptools (Plan check 3; S06)

- **Env:** E-D (E-L plus a second venv; NZ-02) and a second fresh full-history clone for the build. **Depends on:** T01 published. **Readiness:** §4.5 for the E-L clone and venv (steps 5 and 6), plus step 1 below for the E-D venv.
- **E-D setup** (not a check step; recorded): for each candidate in NZ-02's order, `rm -rf /tmp/hde-crd-0002-qa03/venv && <candidate> -m venv --system-site-packages /tmp/hde-crd-0002-qa03/venv && /tmp/hde-crd-0002-qa03/venv/bin/python -m pip install -r /tmp/hde-crd-0002-el/requirements.txt -r /tmp/hde-crd-0002-el/requirements-dev.txt`, written out per candidate (for example `/usr/bin/python3.13 -m venv --system-site-packages /tmp/hde-crd-0002-qa03/venv`), then step 1; stop at the first candidate meeting step 1's predicate. Build clone: `git clone https://github.com/amthorn78/glow-hdengine-v2 /tmp/hde-crd-0002-qa03/build` and `git -C /tmp/hde-crd-0002-qa03/build checkout --detach` the tested commit.
- **Actions:**
  1. `/tmp/hde-crd-0002-qa03/venv/bin/python -c "import setuptools, importlib.util; print(setuptools.__version__, setuptools.__file__, importlib.util.find_spec('_distutils_system_mod'))"`.
  2. From `/tmp/hde-crd-0002-qa03/build`, with `/tmp/hde-crd-0002-qa03/out` absent: `env -i LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PATH=/tmp/hde-crd-0002-qa03/venv/bin:/usr/bin:/bin /tmp/hde-crd-0002-qa03/venv/bin/python tools/evidence/build_release_attestation.py --output /tmp/hde-crd-0002-qa03/out --require-clean`.
  3. `env -i LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PATH=/tmp/hde-crd-0002-qa03/venv/bin:/usr/bin:/bin /tmp/hde-crd-0002-qa03/venv/bin/python tools/evidence/build_release_attestation.py --verify /tmp/hde-crd-0002-qa03/out --require-clean`.
  4. `wc -c /tmp/hde-crd-0002-qa03/out/attestation.json`; `sha256sum /tmp/hde-crd-0002-qa03/out/attestation.json`; `python -c "import json; a=json.load(open('/tmp/hde-crd-0002-qa03/out/attestation.json')); print(a.get('release_id'), a.get('validation_result'), a.get('release_admission'))"`; `grep -c build_backend_compat=distribution_install_layout /tmp/hde-crd-0002-qa03/out/build.log`.
  5. From `/tmp/hde-crd-0002-el` in the E-L venv: `python -m pytest -q -p no:cacheprovider tests/evidence/test_release_attestation.py -k "layout_compat or wheel_build_env"`.
  6. `git -C /tmp/hde-crd-0002-qa03/build status --porcelain`.
- **PASS:** step 1 shows a `setuptools` path under `/usr/lib/python3/dist-packages` and `None`; steps 2 and 3 exit 0; `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, `validation_result` `PASS`, `release_admission` `PR06R_B_FINAL_PASS`; compat line count 1; step 5 "11 passed"; status empty.
- **Outcomes:** no candidate interpreter meets step 1 → `TOOLING_BLOCKED` (Debian condition unavailable; no claim); the build fails `isolated_package_install_failed` → `FAIL_BEHAVIOR`; any other build failure → classify from `/tmp/hde-crd-0002-qa03/out/failure.json`, `FAIL_TOOLING` unless it is product behaviour.
- **Spec:** `check_name` "Attestation builds under a distribution-patched setuptools"; `pf_refs` `["PF12-Canon-HDE-Schemas-and-Artifacts","PF14-Canon-HDE-Mechanics-Guide"]`; the body records the interpreter chosen and every candidate tried. No attestation file is copied into the repository. **Nonclaims:** no release cut, activation or deployment.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-03-attestation-debian/primary.log`.

### T04 `qa-04-showcompat-help` — The showcompat help summary on the operator CLI (Plan check 4; S07)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5. `COLUMNS` unset (NZ-03).
- **Actions:**
  1. `hdctl --help > /tmp/hde-crd-0002-qa/qa-04-showcompat-help/hdctl.out 2> /tmp/hde-crd-0002-qa/qa-04-showcompat-help/hdctl.err`; `python -m engine.cli --help > /tmp/hde-crd-0002-qa/qa-04-showcompat-help/module.out 2> /tmp/hde-crd-0002-qa/qa-04-showcompat-help/module.err`; `cmp` the two `.out` files; `wc -c` the two `.err` files; `python -c "import re,sys; t=re.sub(r'\s+',' ',open(sys.argv[1]).read()); print(t.count('Emit the canonical magic10_compat_result.v1 document for a pair (stdin or files); Reader v1 bytes only via --dump-reader'))" /tmp/hde-crd-0002-qa/qa-04-showcompat-help/hdctl.out`.
  2. `bash ci/checks/check_cli_help.sh`.
  3. `python -m pytest -q -p no:cacheprovider tests/cli/test_cli_install_help.py::test_hdctl_and_module_help tests/cli/test_cli_usage_and_errors.py::test_top_level_help_names_the_showcompat_stdout_contract`.
- **PASS:** both help commands exit 0 with empty stderr; stdouts byte-identical; the sentence count `1`; step 2 exit 0; step 3 "2 passed". **Outcomes:** sentence absent or altered → `FAIL_BEHAVIOR`; tooling failure → `FAIL_TOOLING`.
- **Spec:** `check_name` "The showcompat help summary on the operator CLI"; `pf_refs` `["PF05-Canon-HDE-CLI-API-Vendor-Ref","PF19-Canon-Glow-QA-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-04-showcompat-help/primary.log`.

### T05 `qa-05-aux-preview-band` — `--band` applies to pair-file input (Plan check 5; S08)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5. Label: local/offline.
- **Actions:**
  1. `mkdir -p /tmp/hde-crd-0002-qa05 && hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json > /tmp/hde-crd-0002-qa05/pair.json`; `sha256sum /tmp/hde-crd-0002-qa05/pair.json`; `python -c "import json; d=json.load(open('/tmp/hde-crd-0002-qa05/pair.json')); print([(c.get('id') or c.get('category_id'), c.get('band')) for c in d['categories']])"`.
  2. For B = `Open`, then `Warm`, then `Glow`, each written out: `hdctl aux-preview --pair-file /tmp/hde-crd-0002-qa05/pair.json --category harmony --band Open --show-narrative > /tmp/hde-crd-0002-qa05/file-Open.txt` and `hdctl aux-preview --category harmony --band Open --perspective shared --show-narrative > /tmp/hde-crd-0002-qa05/flag-Open.txt` (and the same with `Warm`, `Glow`).
  3. `hdctl aux-preview --pair-file /tmp/hde-crd-0002-qa05/pair.json --category harmony --show-narrative > /tmp/hde-crd-0002-qa05/file-none.txt`; `hdctl aux-preview --category harmony --band Cool --perspective shared --show-narrative > /tmp/hde-crd-0002-qa05/flag-Cool.txt`; then `cmp` each step 2 pair, `cmp /tmp/hde-crd-0002-qa05/file-none.txt /tmp/hde-crd-0002-qa05/flag-Cool.txt`, and `cmp` each step 2 file output with `file-none.txt`.
  4. `python -m pytest -q -p no:cacheprovider tests/cli/test_aux_preview.py -k pair_file`.
- **PASS:** every command exits 0 with empty stderr; each step 2 pair byte-identical and different from `file-none.txt`; `file-none.txt` equal to `flag-Cool.txt`; "7 passed". If `harmony` is not `Cool` in step 1, use the three bands that differ from it and record the substitution. **Outcomes:** override not applied → `FAIL_BEHAVIOR`; fixture or tool failure → `FAIL_TOOLING`.
- **Spec:** `check_name` "--band applies to pair-file input"; `pf_refs` `["PF05-Canon-HDE-CLI-API-Vendor-Ref","PF19-Canon-Glow-QA-Guide"]`. Narrative text is public Aux output and may be recorded.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-05-aux-preview-band/primary.log`.

### T06 `qa-06-dev-harness-retired` — Dev Reader harness retired; `VERIFY.sh` uses the canonical runner (Plan check 6; S09)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions** (steps 1 and 2 in one asserting `bash -c` script, NZ-05):
  1. `git ls-files dev/reader_harness` (prints nothing); `test ! -e dev/reader_harness/app.py` (exit 0).
  2. `grep -c -i harness VERIFY.sh docs/acceptance/reader_a7_crib.md` (prints `VERIFY.sh:0` and `docs/acceptance/reader_a7_crib.md:0`; exit 1 asserted).
  3. `python -m pytest -q -p no:cacheprovider tests/scripts/test_dev_start_reader.py -k verify`.
- **PASS:** nothing tracked and the file absent; counts 0 and 0; "4 passed". **Outcomes:** rule B.
- **Spec:** `check_name` "Dev Reader harness retired; VERIFY.sh uses the canonical runner"; `pf_refs` `["PF05-Canon-HDE-CLI-API-Vendor-Ref","PF14-Canon-HDE-Mechanics-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-06-dev-harness-retired/primary.log`.

### T07 `qa-07-dev-reader-gate` — Exact `dev` gate and canonical runner profile (Plan check 7; S10)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:** 1. `python -m pytest -q -p no:cacheprovider tests/http/test_reader_a7_transport.py tests/scripts/test_dev_start_reader.py -k "not verify"`. 2. `grep -n 'os.environ.get("APP_ENV") == "dev"' adapter/http_reader.py`.
- **PASS:** "33 passed"; one match. O-23: the governed env-gate proof is not decisive here. **Outcomes:** rule B.
- **Spec:** `check_name` "Exact dev gate and canonical runner profile"; `pf_refs` `["PF05-Canon-HDE-CLI-API-Vendor-Ref"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-07-dev-reader-gate/primary.log`.

### T08 `qa-08-release-evidence-tooling` — Drift test, release labels, root-bound closure probe (Plan check 8; S11, S12, S13)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:**
  1. `python -m pytest -q -p no:cacheprovider tests/evidence/test_engine_core_evidence.py -k release_id`.
  2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_index_missing_state.py -k "release_label or release_capture or capture_rows or capture_labels"`.
  3. `python -m pytest -q -p no:cacheprovider tests/evidence/test_release_attestation.py -k closure_probe`.
  4. `grep -c -F 'current-release capture: release 1.3.0, release_id 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e' artifacts/evidence_index.jsonl` (supporting; 27 at `0b15328d`).
- **PASS:** "2 passed", "6 passed", "4 passed"; step 4 recorded, not decisive. **Outcomes:** rule B.
- **Spec:** `check_name` "Drift test, release labels, root-bound closure probe"; `pf_refs` `["PF12-Canon-HDE-Schemas-and-Artifacts","PF14-Canon-HDE-Mechanics-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-08-release-evidence-tooling/primary.log`.

### T09 `qa-09-override-matrix` — Override matrix, order and refusals, local (Plan check 9; S14)

- **Env:** E-L with `XDG_STATE_HOME=/tmp/hde-crd-0002-xdg-state` (empty; `find /tmp/hde-crd-0002-xdg-state -type f` prints nothing before step 2). **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:**
  1. `python -m pytest -q -p no:cacheprovider tests/bodygraph/test_vendor_prod_override.py tests/cli/test_bg_resolve.py tests/bodygraph/test_resolver_vendor.py`.
  2. One asserting `bash -c` script (NZ-05) running, each with stdout and stderr captured separately:
     - (a) `hdctl bg:resolve --user qa-hde-crd-0002-local1 --source vendor --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL"` (expect exit 1);
     - (b) the same plus `--allow-prod-vendor HDE-CRD-0002/qa/qa-20-live-vendor-override` (exit 1);
     - (c) the same as (a) plus `--allow-prod-vendor "bad ref"` (exit 64);
     - (d) the same as (a) plus `--allow-prod-vendor A --allow-prod-vendor A` (exit 64);
     - (e) `hdctl bg:resolve --user qa-hde-crd-0002-local1 --source db --birthdate 1990-01-01 --birthtime 12:34 --location "Amsterdam, NL" --allow-prod-vendor HDE-CRD-0002/qa/qa-20-live-vendor-override` (exit 64).
  3. `find "$XDG_STATE_HOME" -type f`; `git status --porcelain`.
- **PASS:** "256 passed"; (a) and (b) exit 1 with a `status` `error` envelope and code `PROVIDER_REFUSED`, stderr empty; (c), (d), (e) exit 64, stdout empty, one stderr line not containing the flag value; step 3 prints nothing twice. **Outcomes:** any rail or matrix deviation → `FAIL_BEHAVIOR`; otherwise rule B. **Nonclaims:** no vendor I/O.
- **Spec:** `check_name` "Override matrix, order and refusals, local"; `pf_refs` `["PF05-Canon-HDE-CLI-API-Vendor-Ref"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-09-override-matrix/primary.log`.

### T10 `qa-10-endpoint-catalog` — Every served pair catalogued or excluded with a reason (Plan check 10; S15)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:** 1. `python -m pytest -q -p no:cacheprovider tests/http/test_endpoint_catalog.py`. 2. `python tools/evidence/generate_a7_transport_proofs.py --check`. 3. `cmp docs/ENDPOINTS_CATALOG.json artifacts/audit/ENDPOINTS_CATALOG.json`; `python -c "import json; print(len(json.load(open('docs/ENDPOINTS_CATALOG.json'))['endpoints']))"`.
- **PASS:** "247 passed"; exit 0; `cmp` silent and `18`. **Outcomes:** rule B (the generator is a delivered surface under test for S15). **Nonclaims:** catalog membership proves no reachability.
- **Spec:** `check_name` "Every served pair catalogued or excluded with a reason"; `pf_refs` `["PF05-Canon-HDE-CLI-API-Vendor-Ref","PF12-Canon-HDE-Schemas-and-Artifacts"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-10-endpoint-catalog/primary.log`.

### T11 `qa-11-template-and-documents` — Environment template and operator documents match the code (Plan check 11; S16, S17, S18)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions** (one asserting `bash -c` script, NZ-05; each "no" count's grep exit 1 asserted):
  1. `grep -c -x -F 'GEO_API_KEY=changeme' .env.example`; `python -c "from ci.checks import classify_ci_changes as c; print(c.classify_paths(['.env.example']).reason)"`.
  2. `grep -c -F 'GET /internal/readyz — always 200' docs/ADAPTER_009.md`; `grep -c -F '/internal/readyz is registered only by' docs/ADAPTER_009.md`; `grep -c -F '@app.get("/internal/readyz")' adapter/wsgi.py`; `grep -c readyz adapter/factory.py adapter/http_reader.py` (no: `0` each); `grep -c -F 'Bind target for captures: http://127.0.0.1:8000' docs/ADAPTER_009.md`; `grep -c -F "$(sed -n 's/^web: //p' Procfile)" docs/ADAPTER_009.md`; `grep -c -F 'host="127.0.0.1"' adapter/http_reader.py`.
  3. `` grep -c -F 'built from the `invalid_json` alias (emitted `code`: `ERR_COMPAT_INVALID_JSON`)' docs/ADAPTER_009.md ``; `grep -c -F 'error_envelope("invalid_json")' engine/http/compat_handler.py`; `grep -c -F 'emit_public(envelope, *, sort_keys=True) -> bytes' ARCHITECTURE.md`; `grep -c -x '## Routing and mounts' ARCHITECTURE.md` and the three factory names in that section; `grep -n 'def emit_public' engine/presenter/emitter.py` (its signature returns `bytes`).
- **PASS:** every "contains" count 1 or more and every "no" count 0; step 1 prints `documentation_only`. **Outcomes:** a statement absent or contradicted by the code → `FAIL_BEHAVIOR`. **Nonclaims:** FND-017 and FND-018's other stale lines stay with the Product Owner.
- **Spec:** `check_name` "Environment template and operator documents match the code"; `pf_refs` `["PF19-Canon-Glow-QA-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-11-template-and-documents/primary.log`.

### T12 `qa-12-security-review` — The S19 record and its fixes' regression tests (Plan check 12; S19)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:**
  1. Counting (NZ-04), on `docs/ephemeral/HDE-CRD-0002-S19-code-security-review-v1.0.md`: `awk '/^## 6\. /{s=1;next} /^## /{s=0} s && /^\| [0-9]+ \| /{n++} END{print "per-file rows", n}'` and `` awk -F' [|] ' '/^## 4\. /{s=1;next} /^## /{s=0} s && /^\| S19-F[0-9][0-9] \|/{n++; if ($9 ~ /^ *$/) bad++} s && /^\| S19-R[0-9][0-9][ |(]/{r++; if ($7 ~ /^ *$/) rbad++} END{print "fixed rows", n, "without disposition", bad+0; print "routed rows", r, "without disposition", rbad+0}' `` on that file.
  2. `python -m pytest -q -p no:cacheprovider tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/transport/test_writers_errors_headers.py tests/http/test_compat_endpoint_contract.py tests/http/test_dev_conjunction_http.py tests/cli/test_cli_usage_and_errors.py tests/http/test_endpoint_catalog.py tests/bodygraph/test_resolver_vendor.py tests/bodygraph/test_ingest.py tests/cli/test_cli_file_inputs.py tests/config/test_manifest_schema.py tests/scripts/test_cut_release_manifest.py tests/config/test_config_artifacts.py -k s19`.
- **PASS:** `per-file rows 49`; `fixed rows 9 without disposition 0`; `routed rows 7 without disposition 0`; "268 passed". **Outcomes:** rule B. **Deployed classes and nonclaims** as Plan check 12 states (F01, F03 deployed in checks 19 and 18, not selected; F05, F06 at check 20, not selected; R01 to R07 with the Product Owner).
- **Spec:** `check_name` "The S19 record and its fixes' regression tests"; `pf_refs` `["PF19-Canon-Glow-QA-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-12-security-review/primary.log`.

### T13 `qa-13-prepush-check` — One read-only command with all five reports (Plan check 13; S20)

- **Env:** E-L (`ruby`, `bash`, `curl` on `PATH`; clean clone). **Depends on:** T01 published. **Readiness:** §4.5 plus `ruby --version`, `curl --version`. Expected duration of step 1: about 24 minutes (Audit §7 item 9).
- **Actions:**
  1. `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay`.
  2. `python tools/ci/prepush_check.py --path docs/ADAPTER_009.md lanes`.
  3. `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py`.
  4. `git status --porcelain`.
- **PASS:** step 1 exits 0 and prints `lanes: classification reason=selected_lanes;paths=2;lanes=product,compat,release`, `membership: member engine/cli/main.py`, `membership: not-member docs/ADAPTER_009.md`, `build-notes: path=docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` with `sha256=42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b` (another single PF10 file then on `main` is recorded as a CAVEAT), `uncovered=0`, `status=PASS` for all five reports and a final `PREPUSH_CHECK_RESULT: PASS` reporting the repository unchanged; step 2 prints `lanes: classification reason=documentation_only;paths=1;lanes=none` and exits 0; step 3 "137 passed"; step 4 empty.
- **Outcomes:** the PR35-C1 race signature (a maintenance child changing `.git/objects` during a read-only snapshot in `tests/tools/test_prepush_check.py`) in step 3, or in step 1's `replay` at a step running that file → `FAIL_TOOLING`, routed to Kronos for any attempt 2; any other test or report failure → `FAIL_BEHAVIOR`; exit 4 → `FAIL_BEHAVIOR`. **Nonclaims:** the tool's result is not CI's result; FND-028 stays with the Product Owner.
- **Spec:** `check_name` "One read-only command with all five reports"; `pf_refs` `["PF19-Canon-Glow-QA-Guide"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log`.

### T14 `qa-14-close-pack-writer` — The v2 close-pack writer, the close-run home and the ADR (Plan check 14; S21)

- **Env:** E-L. **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:** 1. `python -m pytest -q -p no:cacheprovider tests/qa/test_generate_epic_close_pack.py` (about 2.5 minutes). 2. `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_index_missing_state.py -k close`. 3. `sed -n 3p docs/adr/hde/close_pack_writer_adr.md`; `test -f schemas/close_candidate_source.v2.json`.
- **PASS:** "905 passed"; "4 passed"; line 3 begins `Status: Approved with changes by the Product Owner on 2026-10-20 (AQ-1; HDE Build Notes addendum 2.15;` followed by the review reference; the schema exists. **Outcomes:** rule B. **Nonclaims:** no close pack or candidate source is produced; FND-020 stays with the Product Owner.
- **Spec:** `check_name` "The v2 close-pack writer, the close-run home and the ADR"; `pf_refs` `["PF06-Canon-Change-Process-Guide","PF12-Canon-HDE-Schemas-and-Artifacts"]`.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-14-close-pack-writer/primary.log`.

### T15 `qa-15-s01-removal` — S01 is removed as approved and its stated limit holds (Plan check 15; S01, removal evidence only)

- **Env:** E-L (full history). **Depends on:** T01 published. **Readiness:** §4.5.
- **Actions:**
  1. `grep -c '^decision: DELTA_APPROVE' docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`; `grep -c '^## 2.20 HDE-CRD-0002: Specification delta 01 is approved' docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` (or the PF10 file then in force, recorded).
  2. `grep -c '^ADMITTED_RELEASE_VERSION = "1.3.0"' engine/config/registry_loader.py`; `grep -c '^ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"' engine/config/registry_loader.py`; the manifest version from T01.
  3. `git log --oneline 7136040^..HEAD -- pyproject.toml`.
  4. `grep -c 'omits 16 of the 45' README.md`; `cat Procfile` (starts `adapter.factory:create_app()`).
- **PASS:** every count `1`; step 3 prints nothing. **Outcomes:** shallow clone or `7136040` unresolvable → `TOOLING_BLOCKED` (step 3 not judged); `FAIL_BEHAVIOR` only for a commit touching `pyproject.toml` in that range in a full-history clone, or a count other than 1. **Nonclaims:** a regular wheel install outside a source checkout still does not admit the release; the close representation of S01 (G-1) is not decided here.
- **Spec:** `check_name` "S01 is removed as approved and its stated limit holds"; `pf_refs` `["PF14-Canon-HDE-Mechanics-Guide"]` (the body cites HDE Build Notes 2.19 and 2.20 by title).
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-15-s01-removal/primary.log`.

## 6. CANON_CONFLICT_REGISTER (carried)

Held in full in the approved Plan v1.2 §13; carried unchanged:

| ID | Status | Decision owner | Bearing on these tasks |
| :- | :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth | None |
| CR-4 | `APPROVED` | Product Owner | None |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner | None |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20 (HDE Build Notes 2.6) | T07 (exact `dev`) |
| CR-7, CR-8 | `APPROVED`, alternative (a) each | Product Owner (HDE Build Notes 2.7) | T07, T10 |
| CR-9 | `PROPOSED` | Isis, IA-30 boundary | None selected (check 16) |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40 | §4.7 publication (the `crd_id` key) |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | Isis, QA-70 review v1.0 | T01 step 6 |

QA-90 proposes no new conflict.

## 7. Constraints, open inputs and unresolved items

| Item | Owner | State |
| :- | :- | :- |
| Merge of amthorn78/glow-hdengine-v2#724 (Plan v1.2 on `main`) | Product Owner | Before T01 |
| Executor, tools and venue for T01 to T15 | Product Owner, at QA-100 | Not stated |
| Evidence-only commit grant | Product Owner, at execution | Not stated; without it the Product Owner commits |
| Selection of checks 16 to 21 (deployed, vendor and admission checks) | Product Owner | Not selected in this invocation |
| Check 20 venue and human initiator; review v1.2 N-201 (P4 directory mode `0700`) | Product Owner; Kronos at the QA-90 for check 20 | Not applicable to this selection |
| CR-9 | Isis, IA-30 boundary | `PROPOSED` |
| G-1, the close representation of S01 | Close mutation set and Isis; Product Owner if needed | Open; T15 supplies the evidence |
| Audit §7 item 7's phrasing (the E-DEB condition "reproducible in an ordinary cloud container") holds for `/usr/bin/python3.13`, not for a `/usr/bin/python3` that resolves to 3.11 | Kronos (record only) | Recorded here; the Audit v1.0 is not edited |

## 8. Working state

QA-90 for checks 1 to 15 is complete at `TASK_READY`. No task has run. Next: QA-100 under the Product Owner's arrangement, after amthorn78/glow-hdengine-v2#724 merges. On a repeated QA-90 invocation for this selection, reuse T01 to T15 unchanged unless a QA-110 decision authorizes an attempt 2 for a named check.

## 9. TypeSafe reading for the receiving session (QA-100)

Action sent (v8.2): "Execute an existing, already-reviewed bounded QA task collection of 15 tasks for one change request, following its written commands: set up a clean clone and test environment, run local, offline checks (a test suite of about 1,900 tests, a pre-push replay of roughly 24 minutes, a release attestation build and verify, CLI and tool checks), judge each against its written pass predicate, and publish each check's evidence through the canonical evidence writer once per check, then return results. A task list exists; no live run against a provider occurs; the work decomposes into 15 independent units that must each be checked; an independent QA evidence review follows."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.65 (confidence 0.53); rung probabilities low 0.02, medium 0.44, high 0.43, extra high 0.09, max 0.01, ultracode 0.01. Model probabilities Fable 5.1 0.00, Opus 5.5 1.00, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 1.00). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.020, Opus 5.5 at medium 0.440, Opus 5.5 at high 0.430, Opus 5.5 at extra high 0.090, Opus 5.5 at max 0.010, Opus 5.5 at ultracode 0.010, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and medium. Sent 2026-10-24T15:14:56Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-24T15:14:56Z; HTTP 200 in 0.53 s; 5481 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and medium.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-100 HDE-CRD-0002 tasks T01 to T15", before this collection was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - QA-100: Nathan's pick is not stated.
  - This QA-90: Nathan's pick is not stated. Its reading is in the QA-70 review v1.2 §9 (Opus 5.5 at high, score 2.39).

**Surface advice.**
- **Session.** QA-100 runs in the session or shell of the executor the Product Owner chooses (§4.1); this collection names none. A Claude Code cloud session on `amthorn78/glow-hdengine-v2`, or any Linux shell, serves when it meets E-L and E-D as §4.3 and §4.5 state: `git`, CPython 3.12 for E-L, an interpreter meeting the E-DEB condition for E-D (NZ-02; `/usr/bin/python3.13` met it at authoring).
- **Access.** GitHub read for the clones; the package index for the installs (§4.3). No production, vendor, Railway or database access is used or needed by T01 to T15.
- **Writes.** Only in the evidence checkout (the canonical writer's paths, §4.7 and §4.8) and the executor's QA-100 result record under `docs/ephemeral/`. Nothing is committed to `main`; the evidence-only commit follows §4.8.
- **Inputs Nathan supplies with the handoff:** the executor, tools and venue, and whether an evidence-only commit grant applies (§7). amthorn78/glow-hdengine-v2#724 must be merged before T01 (§2.1).
- **Reads.** This collection, the approved Plan v1.2, the QA-70 review v1.2, the QA Audit v1.0, and from `docs/pfcanon/` on `main`: Glow QA Guide §3.4.7, §3.4.8 and §10.6; Plan Templates "Exact status predicates", "Causal precedence" and "Bounded step-level rerun posture"; HDE Build Notes v13.7.8.

## 10. Nonclaims

This collection is preparation. It executes no check, publishes no evidence, makes no QA verdict, accepts nothing, and establishes no S-requirement, closure, deployment or release activation.

## Canon relied on

Read on `main` at `197c2234` (`docs/pfcanon/` byte-identical to the commits the reviews read; this branch edits no `docs/pfcanon/` file).
- QA-90 — Create Bounded QA Execution Task — 100926.1 (page state 2026-10-12T02:30:51.327Z), read in full: inputs, selection, `APPROVED_BASE_WITH_OVERLAYS`, operation semantics, Execute steps 1 to 6, result routing.
- PF19-Canon-Glow-QA-Guide v3.0.6: §3.4.7 (command normalization, read in full); §3.4.8 including "Execution-critical helper readiness" (read); §10.6's ordinary-fault paragraph (attempt 2 only on Kronos's QA-110 decision; read in this lineage at QA-80); §3.5.10 and §3.5.2 (read at QA-80; not selected here).
- PF27-Canon-Plan-Templates v2.0.5: "Exact status predicates", "Causal precedence", "Bounded step-level rerun posture", Step-0B and the CHECK template's "Dependency posture" (read in full at QA-80).
- PF04-Canon-HDE-Governance v2.8.7 §9.8.2 "Dependency posture is required per step" and "Blocked-step minimum fields" (read at QA-80).
- PF14-Canon-HDE-Mechanics-Guide v3.5.8 §1.6.3 (CRD publication; read at QA-50).
- HDE Build Notes v13.7.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md`), the version in force; addenda 2.4, 2.9, 2.15 to 2.21 and 2.23 to 2.26 bear on these tasks; no addendum post-dates the approval.
- In-flight: the approved Plan v1.2 (read in full at amthorn78/glow-hdengine-v2#724's head), the QA-70 review v1.2 (read in full) and its handoff, reviews v1.0 and v1.1 (their notes), the QA Audit v1.0, the S19 record (§4 and §6 structure), WU-PR-02's implementation plan v1.0 (the E-DEB definition, F-1 and PD-1).

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-90-20261024-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | QA Plan v1.2 checks 1 to 15 (S01 removal; S03 to S22 as mapped); tasks T01 to T15, attempt 1 each |
| prompt | QA-90 — Create Bounded QA Execution Task — 100926.1, page state of 2026-10-12T02:30:51.327Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-90 (`TASK_READY`) |
| capture time | 2026-10-24T15:16:40Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-50-20261024-01; GCFPE-USE-HDE-CRD-0002-QA-70-20261024-01, -02 and -03; GCFPE-USE-HDE-CRD-0002-QA-80-20261024-01 and -02; each in its artifact |
| task/result mapping | T01 to T15 → Plan checks 1 to 15 → QA-100 results pending |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
