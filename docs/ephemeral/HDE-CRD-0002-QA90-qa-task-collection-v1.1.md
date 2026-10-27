---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-CRD-0002-QA90-QA-TASK-COLLECTION
artifact_version: "1.1"
predecessor: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.0.md (TASK_READY; tasks T01 to T15 of QA Plan v1.2, attempt 1 each; blob 7c29ea65b3c8; executed by QA-100 and reviewed by QA-110 v1.0; unchanged)
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
author: Kronos, the continuing QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV, the session that wrote QA Plan v1.0 to v1.3 and collection v1.0)
session_disposition: continuing Kronos context, as the QA-70 handoff to QA-90 v1.1 routes it (Product Owner direction D-3)
invocation_binding: CRD / HDE-CRD-0002 / QA-90 / approved QA_PLAN v1.3 check 13, remediation verification (HDE Build Notes 2.27 V-6; Plan §9)
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-90 — Create Bounded QA Execution Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8; page state 2026-10-12T02:30:51.327Z; read in full at this invocation, unchanged since collection v1.0)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (QA_PLAN v1.3; blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a; 119,368 bytes; immutable)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.4.md (QA_PLAN_REVIEW v1.4, APPROVE by Isis (Isis-53), 2026-10-25T16:38:19Z; blob 10adabfe9fce; on main through amthorn78/glow-hdengine-v2#739)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE)
selection: Product Owner, "create reverification instruction for check 13" with the QA-90 handoff of 2026-10-25 = QA Plan v1.3 check 13 `qa-13-prepush-check`, remediation verification only; checks 16 to 21 not selected
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c; unchanged since the approval; addenda 2.27 and 2.28 read in full in this session at QA-80)
observed_revision: 3cf79ff99ee30893865844fddda743b6a181e16a (origin/main at authoring; amthorn78/glow-hdengine-v2#739 merged); tree outside docs/ephemeral/ and docs/pfcanon/ equal to 22a3bc0's
routing: QA-100 — Execute Bounded QA Task — 100926.1, under the Product Owner's chosen execution arrangement
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90 (QA-90 is not an addendum producer)
created_at: 2026-10-25T16:55:00Z
---

# HDE-CRD-0002 — QA Task Collection v1.1 (QA-90): check 13's remediation verification under QA Plan v1.3

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Task | T13-RV1, check 13 `qa-13-prepush-check` (S20), the remediation verification of finding QA110-F01 (§5) |
| Attempt label | `RV-1`: remediation verification 1 of check 13. It follows attempt 1 and is not attempt 2 or a reset (Plan §9; QA-110 ruling R-2; HDE Build Notes 2.28). Set by Kronos (§4.2) |
| Selection | Product Owner: "create reverification instruction for check 13". Checks 16 to 21 are not selected (§3) |
| Pre-execution findings | None. No `QA_PREEXECUTION_FINDING`: check 13 and its §9 bullet are complete under Plan v1.3 and resolve to current repository loci (§2.5) |
| Execution arrangement | Not stated by the Product Owner. The task is executor-neutral; QA-100 records the actual executor, tools and venue (§4.1) |
| Evidence-only commit grant | Not stated. Without it the Product Owner commits the published evidence (§4.8) |
| Normalizations | NZ-01, NZ-06 and NZ-08 (§4.10). Each keeps the Plan's objective, target, rails, evidence identity and predicates |
| Publication | One `publish_crd_check_family` call through the QA-created helper of §4.7. It republishes `qa-13-prepush-check` by `check_id`, a path smoke-validated at `main` (§2.4 row 1) |

This collection is preparation, not an execution result. It selects no step, executes no check, accepts no evidence and declares no PASS. T01 to T15 of collection v1.0 are not reissued.

## 2. Sources and lineage

### 2.1 Approved base (immutable)

`docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md`, exactly blob `3aea6033e3c0` (SHA-256 `30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a`), approved by the QA-70 review v1.4 and on `main` at `3cf79ff9`. The governing text: §2 (state (b)), §3.2 E-L, §5.2 to §5.5, §7 rule A (the E-L bullet and its state-(b) sub-bullet) and rule B, CHECK 13, §9 "Remediation verification (check 13, QA110-F01)".

### 2.2 Overlays

None. HDE Build Notes v13.8 is unchanged since the approval and carries no addendum after it. The Product Owner direction (`docs/ephemeral/HDE-CRD-0002-po-direction-qa110-f01-c1-route-v1.0.md`, D-3) routes this task. It does not change the Plan.

### 2.3 Aids (not overlays)

- The QA-70 review v1.4: N-301 to N-303, and the carried N-201 of review v1.3 (record the shell's `TMPDIR` posture; O-1).
- The QA-110 review v1.0 §6 and the check 13 attempt-1 primary on `main` (blob `4c6d826ae0ac`, landed at `faa2246`): the failure signature to quote.
- The WU-REM-02 lineage review v1.0 §8: V-1 (141 passed), V-2 (step 1 exit 0 in 1,625 s at `22a3bc0`, source pack unchanged) and V-3 (the negative control).
- Collection v1.0 §4: the common contract this collection restates for Plan v1.3.

### 2.4 Authoring observations (planning validation, not QA evidence)

Observed by Kronos in throwaway full-history clones of `main` at `3cf79ff9` (git 2.43.0; CPython 3.12.3 venv with CI's install; `ruby` 3.3.6), each command under `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` and an empty `HOME`. Nothing was committed or pushed from them.

| # | Object | What ran | Result (observed) |
| :- | :- | :- | :- |
| 1 | Republication of `qa-13-prepush-check` (Glow QA Guide §3.4.8 "Execution-critical helper readiness") | In a clone on branch `qa/hde-crd-0002-evidence`, from its root: the §4.7 helper with a PASS stand-in spec for `qa-13-prepush-check`; then §4.7's six read-only validators | `PUBLISHED` with the primary and manifest paths, exit 0. Every validator exits 0. `validate_crd_check_family` lists 15 checks with `qa-13-prepush-check` replaced (stand-in status PASS). The committed attempt-1 primary is still blob `4c6d826ae0ac` at `faa2246` in history. Changed paths: the primary, the manifest, their two `.path_proof.txt` files and the four Mirror files (`artifacts/evidence_index.jsonl` with its `.sha256` and two proofs). `docs/evidence/INDEX.*` and the orientation output were unchanged, because the Index keys already exist |
| 2 | Rule A's state-(b) candidate reads (T13-RV1 step 0) | `git rev-parse HEAD` and `HEAD^{tree}`; `--is-shallow-repository`; `git cat-file -e '7136040^{commit}'`; `git diff --stat 22a3bc040a60c75b089a629172a5d829f20d8e98 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'`; `sha256sum catalog/manifest.json`; `hdctl --version` | `3cf79ff99ee30893865844fddda743b6a181e16a`, tree `209506af39c3`; `false`; exit 0; empty; `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`; `hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)` |
| 3 | Check 13 step 2 | `python tools/ci/prepush_check.py --path docs/ADAPTER_009.md lanes` | `lanes: classification reason=documentation_only;paths=1;lanes=none`; `PREPUSH_CHECK_RESULT: PASS lanes=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`; exit 0; status empty |
| 4 | Check 13 step 3's count | `python -m pytest -p no:cacheprovider --collect-only -q tests/tools/test_prepush_check.py` (at QA-80, `main` `40d2a5d5`, the same code) | `141 tests collected`. The full run was not repeated here; "141 passed" is the lineage review's V-1 and review v1.3 §2 row 2 |

Step 1 (about 25 minutes) was not run at authoring. Its result at `22a3bc0` is the lineage review's V-2.

### 2.5 Pre-execution assessment

Check 13 is complete under Plan v1.3: environment (E-L), readiness (rule A with the state-(b) sub-bullet), actions, PASS predicate ("141 passed"), Outcomes line, deliverable and publication (§5), and the §9 identity of this execution. Every locus it uses exists on `main` (§2.4). No substantive Plan defect was found, so there is no `QA_PREEXECUTION_FINDING`.

Three execution-time conditions are recorded, not defects:
- **The build-notes line names v13.8.** Step 1's predicate admits "the single PF10 file then on `main`, recorded as a CAVEAT" (review v1.3 N-202). Expected: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md`, `sha256=439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c`, unless PF10 changes again before execution.
- **`TMPDIR`.** O-1 (OPS03 `EXDEV`) is open. With `TMPDIR` on another filesystem than `/tmp`, replay step 08 fails two OPS03 tests, independent of S20 (HDE Build Notes 2.28). NZ-08 records and unsets it (§4.10).
- **git version.** QA110-F01 was observed under git 2.53.0 and the remedy's V-2 under git 2.43.0. The task records `git --version`. Any git version the executor's E-L venue has is valid (Plan §3.2 sets none).

### 2.6 Carried lineage

- Plan v1.2 → checks 1 to 15 executed (collection v1.0; QA-100 results v1.0) → QA-110 v1.0: 14 `ACCEPT`, check 13 `ESCALATION_REQUIRED` (QA110-F01; R-2 consumed check 13's ordinary rerun) → ESC-10 → ESC-30 → ESC-40 `APPROVE_AS_CHANGED` (HDE Build Notes 2.27) → WU-REM-02 (amthorn78/glow-hdengine-v2#734, squash `22a3bc0`) → PR-40 `ACCEPT` → Product Owner direction D-1 to D-3 (CR-12) → QA-70 v1.3 `DENY` → Plan v1.3 (QA-80) → QA-70 v1.4 `APPROVE` → this collection.
- Attempt history of check 13: attempt 1 (`FAIL_BEHAVIOR`, two executions in one primary, published at `faa2246`). The one ordinary rerun is consumed (R-2). This task is the remediation verification, labelled `RV-1`.

## 3. Selection reconciliation

| Plan check | `check_id` | Selected | Task | Attempt | Depends on | State |
| :- | :- | :- | :- | :- | :- | :- |
| 1 to 12, 14, 15 | `qa-01-preflight` to `qa-15-s01-removal` (not 13) | No | collection v1.0 T01 to T12, T14, T15 | 1 | — | Executed and accepted (QA-110 v1.0); state (a); not re-executed (Plan §2) |
| 13 | `qa-13-prepush-check` | Yes | T13-RV1 | `RV-1` (after attempt 1) | Plan v1.3 on `main` (done at `3d7c40ea`); a state-(b) commit (§4.5) | Issued |
| 16 to 21 | `qa-16-deployed-identity` to `qa-21-evidence-admission` | No | none | none | — | Not selected; each needs its own Product Owner selection. Check 21 depends on checks 1 to 20 being published (Plan §8) |

## 4. Common execution contract

### 4.1 Executor, venue and authority (Plan §2; QA-90 "Product Owner execution choice")

- The Product Owner has not stated the executor, tools or venue. Any executor the Product Owner chooses may run T13-RV1, Kronos included. No human initiator is required: the check makes no vendor call.
- Venue: any Linux shell that can form E-L (Plan §3.2): CPython 3.12, CI's full install, `ruby`, `bash`, `curl`, `git`, network access to GitHub and the package index for setup only. The QA-100 workstation of attempt 1 and a Claude Code cloud container (§2.4) each meet it.
- QA-100 records the actual executor, venue, git version, interpreter paths and times. Execution authority is not acceptance authority: evidence returns to Kronos at QA-110.

### 4.2 Attempt identity (Plan §9 "Remediation verification"; §5.5)

- The label is `RV-1`. It is recorded in the spec's `command_provenance`, in the primary's notes and in the QA-100 result, and returned under Plan §5.5 as the attempt.
- `RV-1` is not attempt 2 and does not reset attempts (Glow QA Guide §10.6 "Nominal remediation cycles must not reset attempts or bypass that limit").
- The executor never reruns on its own. Any outcome other than `PASS`, including a `FAIL_TOOLING` with the PR35-C1 signature, goes to Kronos at QA-110 with its evidence. A second `FAIL_BEHAVIOR` of check 13 is escalated (Plan §9 "Escalation").

### 4.3 Setup (not a check)

Fixed scratch locations, all outside every repository (another location may be used if recorded, NZ-01):

```text
/tmp/hde-crd-0002-rv1-el         E-L clone (full history)
/tmp/hde-crd-0002-rv1-venv       E-L venv (CPython 3.12, CI's full install)
/tmp/hde-crd-0002-xdg-state      E-L's empty XDG_STATE_HOME
/tmp/hde-crd-0002-evidence       evidence checkout (full history), branch qa/hde-crd-0002-rv1-evidence
/tmp/hde-crd-0002-qa             helper and spec and body files
```

Remove any leftover of these paths from attempt 1 before starting.

1. `git clone https://github.com/amthorn78/glow-hdengine-v2 /tmp/hde-crd-0002-rv1-el` (no `--depth`). Then `git -C /tmp/hde-crd-0002-rv1-el checkout --detach origin/main`. Record `git -C /tmp/hde-crd-0002-rv1-el rev-parse HEAD` as the tested commit, a state-(b) commit (§4.5 step 0 proves it).
2. `python3.12 -m venv /tmp/hde-crd-0002-rv1-venv`, then from `/tmp/hde-crd-0002-rv1-el`: `/tmp/hde-crd-0002-rv1-venv/bin/python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` and `/tmp/hde-crd-0002-rv1-venv/bin/python -m pytest --version`.
3. `mkdir -p /tmp/hde-crd-0002-xdg-state /tmp/hde-crd-0002-qa/qa-13-prepush-check`. `XDG_STATE_HOME` must be an empty directory.
4. `git clone https://github.com/amthorn78/glow-hdengine-v2 /tmp/hde-crd-0002-evidence` (no `--depth`); `git -C /tmp/hde-crd-0002-evidence checkout -b qa/hde-crd-0002-rv1-evidence origin/main`. Its history holds `22a3bc0`, and its code equals state (b) (Plan §5.4). It already holds the published family of checks 1 to 15. Then create a separate venv for it, or reuse the E-L venv only if `python -c "import engine; print(engine.__file__)"` run from `/tmp/hde-crd-0002-evidence` prints a path inside `/tmp/hde-crd-0002-evidence` (the current directory is first on `sys.path` for `python -c`). Record which.
5. Write the helper of §4.7 to `/tmp/hde-crd-0002-qa/publish_check.py`.
6. The check's shell exports the default rails and the E-L environment, recording first the prior `TMPDIR` value (or `UNSET`) and `stat -f -c '%T'` of `/tmp` and of that value (NZ-08):

```text
echo "TMPDIR(prior)=${TMPDIR-UNSET}"; stat -f -c '%T' /tmp; [ -n "${TMPDIR-}" ] && stat -f -c '%T' "$TMPDIR"
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
export XDG_STATE_HOME=/tmp/hde-crd-0002-xdg-state
export PATH=/tmp/hde-crd-0002-rv1-venv/bin:$PATH
unset HD_API_KEY GEO_API_KEY HD_API_BASE_URL HDAPI_BASE_URL DATABASE_URL GH_TOKEN GITHUB_TOKEN HDE_VENDOR_OVERRIDE_AUDIT_PATH ENGINE_ENV TMPDIR
cd /tmp/hde-crd-0002-rv1-el
```

### 4.4 Rails and `captured_env`

The check runs under the default rails (Plan §3.1). The spec carries `captured_env` `{"LC_ALL":"C","LANG":"C","TZ":"UTC","SAFE_MODE":"1","ALLOW_NETWORK":"0","APP_ENV":"dev"}`, read from the check's shell when it ran (Plan §5.3 rule 2). If a value differs, record the actual value and stop: the check is `TOOLING_BLOCKED`, rails not as planned.

### 4.5 Step-local readiness (Plan §7 rule A, E-L bullet and state-(b) sub-bullet)

Before step 1, from `/tmp/hde-crd-0002-rv1-el`, recorded under `=== CONTEXT ===`:

**Step 0a, the state-(b) candidate reads:**

```text
git rev-parse HEAD                                   # recorded; the tested commit of this execution
git rev-parse HEAD^{tree}                            # recorded
git rev-parse --is-shallow-repository                # false
git cat-file -e '7136040^{commit}'                   # exit 0
git diff --stat 22a3bc040a60c75b089a629172a5d829f20d8e98 HEAD -- . ':!docs/ephemeral' ':!docs/pfcanon'   # empty
sha256sum catalog/manifest.json                      # 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e
hdctl --version                                      # hdctl 0.0.0 (hdengine@prod;77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e)
```

A shallow clone or an unresolvable `7136040` is `TOOLING_BLOCKED` (history unavailable; reclone). A non-empty diff or a different `release_id` is `TOOLING_BLOCKED` ("candidate changed"): publish the primary and route to Kronos.

**Step 0b, the E-L readiness reads:**

```text
git rev-parse HEAD                                   # equals step 0a's recorded commit
git status --porcelain                               # empty
python --version                                     # Python 3.12.x
python -m pytest --version
python -c "import engine; print(engine.__file__)"    # /tmp/hde-crd-0002-rv1-el/engine/__init__.py
ruby --version; bash --version; curl --version; git --version
```

A failed read makes the check `TOOLING_BLOCKED` (never `FAIL_BEHAVIOR`). No installation happens inside the check; the environment is repaired outside it, and the case goes to Kronos.

### 4.6 Capture, body and status

- **Files** (QA-created scratch, never committed): `/tmp/hde-crd-0002-qa/qa-13-prepush-check/body.txt` (the primary's body) and `/tmp/hde-crd-0002-qa/qa-13-prepush-check/spec.json` (§4.7).
- **Body** (Plan §5.2), in this order:
  - `=== CONTEXT ===`: tested commit and tree; environment class E-L; interpreter path and version; git version; rails; a `SET`/`UNSET` presence table for `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `ENGINE_ENV`; the `TMPDIR` posture of §4.3 step 6; the actor; start and end time; the reads of §4.5.
  - `=== COMMANDS ===`: each child command, its exit code, stdout and stderr, separated.
  - `=== PREDICATES ===`: each predicate, observed value, PASS or FAIL.
  - `=== NOTES ===`: opens with the attempt-1 failure signature and the remedy (§5 T13-RV1, notes line), then the attempt label `RV-1`, the normalizations applied, observations and nonclaims. For a `TOOLING_BLOCKED` outcome: the blocking precondition, why it could not be satisfied, whether it blocks closeout and the required follow-up.
- **LF only** (Plan §5.3 rule 1): before writing `body.txt`, normalize any CRLF with `sed 's/\r$//'` and note "CRLF normalized to LF".
- **Secret scan** (Plan §5.3 rule 3), from the check's shell: `python -c "import os,sys; t=open(sys.argv[1],encoding='utf-8').read(); v=[os.environ[n] for n in ('HD_API_KEY','GEO_API_KEY','HD_API_BASE_URL','HDAPI_BASE_URL','DATABASE_URL') if os.environ.get(n)]; print('HIT' if any(x in t for x in v) or any(h in t for h in ('Authorization: Bearer ','HD-Api-Key: ','HD-Geocode-Key: ')) and '<redacted>' not in t else 'NO_HIT')" /tmp/hde-crd-0002-qa/qa-13-prepush-check/body.txt`. E-L leaves the names unset, so `NO_HIT` is expected. A `HIT` quarantines the body outside the repository and makes the check `FAIL_TOOLING`.
- **`command` and `exit_code`** (Plan §5.2): `command` lists each executed child argv in order (steps 1 to 4); `exit_code` is step 1's status, the decisive child (precedent: QA-110 v1.0 D-04).
- **Status:** the task's PASS predicate and Outcomes line, else Plan §7 rule B in its order (`FAIL_TOOLING`, `TOOLING_BLOCKED`, `FAIL_BEHAVIOR`, `PASS`). A non-PASS status needs a one-line `status_reason`.

### 4.7 Publication and indexing (Plan §5.4 and §5.5)

**Helper** (QA-created, outside the repository; the helper of collection v1.0 §4.7, unchanged and smoke-validated for a republication at `main`, §2.4 row 1). Content of `/tmp/hde-crd-0002-qa/publish_check.py`:

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

**Spec** (`/tmp/hde-crd-0002-qa/qa-13-prepush-check/spec.json`), one JSON object:
- `check_id` `"qa-13-prepush-check"`; `check_name` `"One read-only command with all five reports"`;
- `status`; `status_reason` (`""` for PASS);
- `command` (a list of the four argv lists; `[]` when nothing ran);
- `command_provenance` `"QA Plan v1.3 check 13; QA-90 collection v1.1 task T13-RV1, remediation verification RV-1 of QA110-F01 (not attempt 2; Plan §9); normalizations: <those applied>"` (`"Not executed"` when nothing ran);
- `exit_code` (step 1's integer status, or `null` when nothing ran);
- `output_file` the body path; `evidence_artifacts` `[]`; `pf_refs` `["PF19-Canon-Glow-QA-Guide"]`;
- `captured_env` (§4.4); `captured_at_utc` (the check's finalization time, `date -u +%Y-%m-%dT%H:%M:%SZ`).

**Call**, from `/tmp/hde-crd-0002-evidence` under the default rails (§4.3 step 6 exports, with `cd /tmp/hde-crd-0002-evidence` and the interpreter recorded in §4.3 step 4):

```text
python -c "exec(open('/tmp/hde-crd-0002-qa/publish_check.py').read())" /tmp/hde-crd-0002-qa/qa-13-prepush-check/spec.json
```

STOP if the output does not start with `PUBLISHED`. A refused publication changes nothing: correct the assembly from the preserved transcript and publish again; that is not a rerun. A second refusal goes to Kronos.

The call merges by `check_id`: it replaces `qa-13-prepush-check`'s primary and manifest status, and the attempt-1 primary stays in git history at `faa2246` (blob `4c6d826ae0ac`) as the visible failure context (Plan §9).

**Then, read-only, from `/tmp/hde-crd-0002-evidence`** (Plan §5.4), each exit status and output recorded in the QA-100 result:

```text
python tools/evidence/update_evidence_index.py --check
python tools/evidence/orientation_demo.py --check
python tools/evidence/validate_evidence_paths.py
python ci/checks/check_mirror_schema.sh
python tools/evidence/check_lf_endings.py
python -c "import pathlib; from tools.qa.qa_harness import HarnessConfig, validate_crd_check_family as v; print(v(HarnessConfig(crd_id='HDE-CRD-0002', repo_root=pathlib.Path.cwd())))"
```

Expected: each exits 0, and `validate_crd_check_family` lists the same 15 checks with `qa-13-prepush-check` at this execution's status.

**Registration set** (Plan §5.5): `audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log` and `primary.log.path_proof.txt`; its manifest entry in `audit/qa/hde-crd-0002/qa_step_logs_manifest.json` and that file's `.path_proof.txt`; Index keys `audit.qa.hde_crd_0002.checks.qa-13-prepush-check.primary.log` and `audit.qa.hde_crd_0002.qa_step_logs_manifest` with their Mirror rows; and the ten updater-owned graph files of Plan §2, of which a republication changes only those the writer rewrites (§2.4 row 1). Never hand-edit any of them, and never run the updater in write mode separately.

### 4.8 Evidence files and commit boundary (Plan §2, §5.6)

- Only the writer of §4.7 writes in the evidence checkout. Nothing else is written under `audit/qa/hde-crd-0002/`.
- **Evidence-only commit grant: not stated.** If the Product Owner grants it at execution, the executor may commit and push, on the one branch `qa/hde-crd-0002-rv1-evidence`, only `audit/qa/hde-crd-0002/**`, the ten graph files of Plan §2 and its own QA-100 result record under `docs/ephemeral/`, and open one pull request; no other path, no merge, no force-push. Without the grant, the executor leaves the published files uncommitted in `/tmp/hde-crd-0002-evidence`, reports `git status --porcelain` there, and the Product Owner commits. (Attempt 1's precedent: PO-4 granted it, HDE Build Notes 2.28.)
- Expected CI selection for the evidence pull request: lanes `evidence` and `release`. Named risks: FND-024 (PR35-C1) and IR-7. A red run is classified from its log before any re-run.

### 4.9 Stop, recovery and cleanup (Plan §9)

- A `TOOLING_BLOCKED` readiness or candidate read stops the task: publish the primary and route to Kronos.
- If interrupted before publication, the task restarts from §4.5 in the same clone only if its status is still empty; otherwise reclone. Record the interruption.
- Cleanup after publication: delete `/tmp/hde-crd-0002-rv1-el`, `/tmp/hde-crd-0002-rv1-venv` and `/tmp/hde-crd-0002-xdg-state`. Keep `/tmp/hde-crd-0002-evidence` and `/tmp/hde-crd-0002-qa` until the evidence is committed and QA-110 has read the QA-100 result.

### 4.10 Normalizations (Glow QA Guide §3.4.7; QA-90 Execute step 5)

Each keeps the Plan's objective, target, rails, evidence identity and predicates. The executor records the ones it applies in `command_provenance` and the body.

| ID | Normalization | Basis |
| :- | :- | :- |
| NZ-01 | The fixed scratch paths of §4.3 instantiate the Plan's "throwaway clone"; another location may be used if recorded | Plan §3.2; collection v1.0 NZ-01 |
| NZ-06 | Publication runs the helper file through `python -c "exec(open(<helper path>).read())"` from the evidence checkout's root: the `python -c` invocation Plan §5.4 names, with the code read from a recorded file | Plan §5.4; collection v1.0 NZ-06 |
| NZ-08 | The check's shell unsets `TMPDIR`, after recording its prior value and the filesystem types of `/tmp` and that value, so the tool's children use `/tmp` as on hosted CI. E-L names no `TMPDIR` value, so this is environment wiring within the class. It removes O-1's venue cause (OPS03 `EXDEV`, independent of S20), as attempt 1's Moon Loop did. It does not decide O-1 | Plan §3.2 E-L; review v1.3 N-201 carried by review v1.4; HDE Build Notes 2.28 (PO-3 Moon Loop; O-1) |

### 4.11 Return to QA-110

QA-100 returns: the state (`COMPLETE`, `PARTIAL`, `BLOCKED`, `FAILED` or `NOT_EXECUTED`); the check's status; the label `RV-1`; the tested commit and tree with step 0a's reads; the primary's path, size and SHA-256; its manifest entry; the two Index keys present; the path proofs validating; §4.7's six validator results; the evidence commit and pull request (or the uncommitted state when no grant); the executor, venue and git version; the `TMPDIR` posture; and every normalization and gap. Missing indexing is reported as incomplete work, never as PASS.

## 5. Task

### T13-RV1 `qa-13-prepush-check` — One read-only command with all five reports (Plan v1.3 check 13; S20; remediation verification `RV-1` of QA110-F01)

- **Binding:** change HDE-CRD-0002; approved Plan v1.3 (blob `3aea6033e3c0`), check 13 and §9 "Remediation verification"; review v1.4; Audit v1.0; label `RV-1`; default rails; publication by §4.7; return per §4.11.
- **Env:** E-L at state (b) (Plan §2): a full-history clone, `ruby`, `bash`, `curl` on `PATH`, clean. **Depends on:** Plan v1.3 on `main` (done). **Readiness:** §4.5 steps 0a and 0b. Expected duration of step 1: about 25 to 27 minutes (lineage review v1.0 §8 V-2: 1,625 s).
- **Actions** (Plan check 13, unchanged):
  1. `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay`.
  2. `python tools/ci/prepush_check.py --path docs/ADAPTER_009.md lanes`.
  3. `python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py`.
  4. `git status --porcelain`.
- **PASS:**
  - step 1 exits 0 and prints `lanes: classification reason=selected_lanes;paths=2;lanes=product,compat,release`, `membership: member engine/cli/main.py`, `membership: not-member docs/ADAPTER_009.md`, `build-notes: path=docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md` with `sha256=42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b` or the single PF10 file then on `main` recorded as a CAVEAT (expected now: `PF10-HDE-Build-Notes-v13.8.md`, `sha256=439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c`), `uncovered=0`, `status=PASS` for all five reports and a final `PREPUSH_CHECK_RESULT: PASS` line reporting the repository unchanged;
  - step 2 prints `lanes: classification reason=documentation_only;paths=1;lanes=none` and exits 0;
  - step 3 "141 passed";
  - step 4 empty.
- **Outcomes** (Plan check 13, unchanged): the PR35-C1 race signature (a maintenance child changing `.git/objects` during a read-only snapshot in `tests/tools/test_prepush_check.py`) in step 3, or in step 1's `replay` at a step running that file → `FAIL_TOOLING`, routed to Kronos (§4.2); any other test or report failure → `FAIL_BEHAVIOR`; exit 4 (repository changed) → `FAIL_BEHAVIOR`. If exit 4 recurs, the remedy's R-2 makes the tool name the changed entries on stderr (`PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: <entry>`); record those lines verbatim.
- **Notes line, first in `=== NOTES ===`** (Plan §9): "Remediation verification RV-1 of check 13 (QA110-F01), not attempt 2 and not a reset. Attempt 1: exit 4, PREPUSH_CHECK_READ_ONLY_VIOLATION, every report PASS, FAIL_BEHAVIOR; primary published at faa2246 (blob 4c6d826ae0ac). Remedy: WU-REM-02, amthorn78/glow-hdengine-v2#734, squash 22a3bc0 (HDE Build Notes 2.27)."
- **Spec:** as §4.7. **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log` (republished by `check_id`).
- **Nonclaims:** the tool's result is not CI's result; FND-028, D-1/LR6-O1, O-1 and O-A stay with their owners.

## 6. CANON_CONFLICT_REGISTER (carried)

Held in full in the approved Plan v1.3 §13; carried unchanged:

| ID | Status | Decision owner | Bearing on this task |
| :- | :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth | None |
| CR-4 | `APPROVED` | Product Owner | None |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner | None |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20 | None |
| CR-7, CR-8 | `APPROVED`, alternative (a) each | Product Owner | None |
| CR-9 | `PROPOSED`, unreviewed | Isis, IA-30 boundary | None (check 16 not selected) |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40 | §4.7 publication (the `crd_id` key) |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | Isis, QA-70 review v1.0 | None (check 1 not re-executed) |
| CR-12 | `APPROVED`, alternative (a) | Product Owner, 2026-10-25 | The route to this task (direction D-3) |

QA-90 proposes no new conflict.

## 7. Constraints, open inputs and unresolved items

| Item | Owner | State |
| :- | :- | :- |
| Executor, tools and venue for T13-RV1 | Product Owner, at QA-100 | Not stated |
| Evidence-only commit grant | Product Owner, at execution | Not stated; without it the Product Owner commits |
| Selection of checks 16 to 21; check 20's venue and initiator | Product Owner | Not selected |
| O-1 (OPS03 `EXDEV`) | Thoth; Product Owner if independent | Open; NZ-08 records and avoids its venue cause only |
| O-A, D-1/LR6-O1, FND-028 | Product Owner | Unchanged |
| CR-9 | Isis, IA-30 boundary | `PROPOSED` |
| G-1, PO-2 and PO-5 drainage, O-2 to O-4 | As HDE Build Notes 2.28 records them | Unchanged |

## 8. Working state

QA-90 for check 13's remediation verification is complete at `TASK_READY`. No task has run. Next: QA-100 under the Product Owner's arrangement. On a repeated QA-90 invocation for this selection, reuse T13-RV1 unchanged unless a QA-110 decision says otherwise.

## 9. TypeSafe reading for the receiving session (QA-100)

Action sent (v8.2): "Execute one existing, already-reviewed bounded QA task for one change request, following its written commands: set up a clean full-history clone and a test environment, record the candidate reads that pin the fixed code, run one previously failed local check of a read-only pre-push tool (four steps; its main command runs about 25 minutes, then a 141-test owner suite), judge it against its written pass predicates, and publish its one evidence log through the repository's canonical evidence writer with read-only validation, recording the results in a Markdown result record. It re-verifies a merged three-file fix; no live run against a provider occurs, and an independent evidence review follows."

The reading as printed by the script:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.54 (confidence 0.65); rung probabilities low 0.00, medium 0.53, high 0.41, extra high 0.06, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.98, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.005, Fable 5.1 at high 0.004, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.519, Opus 5.5 at high 0.402, Opus 5.5 at extra high 0.059, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.005, Sonnet 5.5 at high 0.004, Sonnet 5.5 at extra high 0.001, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and medium. Sent 2026-10-25T16:50:52Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-25T16:50:52Z; HTTP 200 in 0.57 s; 5478 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between high and medium.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "QA-100 HDE-CRD-0002 task T13-RV1 (check 13 remediation verification)", before this collection was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - QA-100: Nathan's pick is not stated.
  - This QA-90: Nathan's pick is not stated. Its reading is in the QA-70 review v1.4 §7 (Opus 5.5 at medium, score 1.20).

**Surface advice.**
- **Session.** QA-100 runs in the session or shell of the executor the Product Owner chooses (§4.1); this collection names none. Any Linux shell that meets E-L serves: the attempt-1 workstation (git 2.53.0, where QA110-F01 was observed) or a Claude Code cloud session on `amthorn78/glow-hdengine-v2` (git 2.43.0 at authoring). Recording the git version matters more than which one is used.
- **Time.** Setup and install about 5 minutes; step 1 about 25 to 27 minutes; step 3 about 2 minutes; publication and validation a few minutes.
- **Access.** GitHub read for the clones; the package index for the install. No production, vendor, Railway or database access is used or needed.
- **Writes.** Only in the evidence checkout (the canonical writer's paths, §4.7 and §4.8) and the executor's QA-100 result record under `docs/ephemeral/`.
- **Inputs Nathan supplies with the handoff:** the executor, tools and venue, and whether an evidence-only commit grant applies (§7).
- **Reads.** This collection; Plan v1.3 check 13, §7 rule A and §9; the QA-70 review v1.4; the check 13 attempt-1 primary on `main`.

## 10. Nonclaims

This collection is preparation. It executes no check, publishes no evidence, makes no QA verdict, accepts nothing, and establishes no S-requirement, closure, deployment or release activation. Check 13 stays `FAIL_BEHAVIOR` until its verification returns and Kronos decides at QA-110.

## Canon relied on

Read on `main` at `3cf79ff9` (`docs/pfcanon/` last changed by `21141b39`, byte-identical to what QA-80 and the QA-70 reviews v1.3 and v1.4 read; this branch edits no `docs/pfcanon/` file).
- QA-90 — Create Bounded QA Execution Task — 100926.1 (page state 2026-10-12T02:30:51.327Z), read in full at this invocation: indexing, authorship and execution choice, inputs and selection, `APPROVED_BASE_WITH_OVERLAYS`, operation semantics, Execute steps 1 to 6 (step 4: this is not the ordinary rerun), result routing.
- PF19-Canon-Glow-QA-Guide v3.0.6: §10.6 "Common remediation cycle and return owner" step 5, the attempt-limit paragraph and "Evidence-package caveats and failure history" (read in full at ESC-10 in this session); §3.4.7 (command normalization) and §3.4.8 "Execution-critical helper readiness" (read at collection v1.0; unchanged).
- PF27-Canon-Plan-Templates v2.0.5 "Exact status predicates", "Causal precedence" and "Bounded step-level rerun posture" (read at QA-80; unchanged).
- HDE Build Notes v13.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md`): addenda 2.27 (C-1, V-6, R-2 of the remedy) and 2.28 (R-2 ruling, O-1, PO-3, PO-4), read in full at QA-80 in this session; 2.21 (PR35-C1). No addendum post-dates the approval.
- In-flight: approved Plan v1.3 (this author's own; check 13, §7 rule A, §9 re-read here), the QA-70 review v1.4 (read in full), review v1.3 N-201, the Product Owner direction v1.0 (D-3), the QA-110 review v1.0 (this author's own), the WU-REM-02 lineage review v1.0 §8, collection v1.0 §4 (this author's own).

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-90-20261025-02 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | S20; QA Plan v1.3 check 13; task T13-RV1, label `RV-1`; finding QA110-F01; remedy WU-REM-02 |
| prompt | QA-90 — Create Bounded QA Execution Task — 100926.1, page state of 2026-10-12T02:30:51.327Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, QA-90 (`TASK_READY`) |
| capture time | 2026-10-25T16:55:00Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-90-20261024-01 (collection v1.0); GCFPE-USE-HDE-CRD-0002-QA-80-20261025-03 (Plan v1.3); GCFPE-USE-HDE-CRD-0002-QA-70-20261025-04 and -05 (reviews v1.3 and v1.4); each in its artifact |
| task/result mapping | T13-RV1 → Plan v1.3 check 13 → QA-100 result pending |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
