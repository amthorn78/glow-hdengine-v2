---
artifact_type: QA_TASK_COLLECTION
artifact_version: "1.0"
logical_id: HDE-EPIC041-QA90-QA-TASKS
QA_TASK_COLLECTION_ID: docs/ephemeral/HDE-EPIC041-QA90-qa-tasks-v1.0.md
state: TASK_READY
predecessor: none (first QA-90 output for HDE-EPIC041; no earlier task, result or attempt exists on main)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
approved_base: docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md (QA_PLAN v1.0; 748 lines; SHA-256 4f7a2d9d6d77d0aa270b9cf10033eb0c4d07adc418f820568f0fed7c66c4a64a, equal to the digest QA-70 approved; immutable, not rewritten by this collection)
overlays: "none. No QA Plan addendum, QA-80 revision or approved delta exists. PF10 read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.4.md; its addenda 2.2 to 2.5 are already applied by the approved base (Plan §2) and add nothing for this collection; 2.1 is not engaged"
QA_PLAN_ID: docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md
QA_PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md (QA-70 APPROVE, Isis, 2026-10-29; SHA-256 f90434a1b4757fc44efb5a46c2af9434644daa65d8f3bb1a6b4888c9c003d92f)
QA_AUDIT_ID: docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE; SHA-256 3002c4dd035004d7e93ea46e36201a24a72a0d2b70087a05334c7dc8af45bfe4)
LIVE_QA_GUIDE_ID: docs/ephemeral/HDE-EPIC041-QA20-live-qa-guide-v1.0.md (GUIDE_READY; SHA-256 0463c74cd9da9f341fc35065a9a39ea240627b82de0672110204651dae15a161)
QA_STEP_IDS: ALL (Product Owner selection, supplied by Nathan in the QA-90 invocation, 2026-11-01, with the direction "Be sure to clearly ID rails settings")
repository: amthorn78/glow-hdengine-v2
repository_head_read: 6b9c4c40798af3b044d2277568fd8284ee0cf977 (origin/main at authoring; outside docs/ephemeral/ identical to bba6337c and 1e2ac50e, the heads QA-70 and QA-50 read; provenance, not an execution predicate)
producer: Kronos, the continuing QA authority for HDE-EPIC041 (role continuity per D27; this session's platform identity is not directly known to it and is not invented)
prompt: QA-90 — Create Bounded QA Execution Task — 102726.1 (https://app.notion.com/p/4064590a05eb81929057e6667f7193c6; page state 2026-10-27T13:15:43.099Z; read in full at this invocation)
r1_row: GCF-23
ecosystem_release: GCFPE-20261027.1 / 102726.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.4.md (the version the Plan and QA-70 read; no newer PF10 on main; provenance, not a gate)
PF10_ADDENDUM_OUTPUT: NONE (QA-90 is not an addendum producer)
canon_conflict_register: section 10 (CCR-1 to CCR-6 carried unchanged from the QA-70 review §7)
execution_arrangement: PENDING the Product Owner's choice (PI-01); no executor, platform or session identity is required
next_stage: QA-100 — Execute Bounded QA Task — 102726.1 (https://app.notion.com/p/4064590a05eb8150bcfff1e25129b368), under the Product Owner's chosen execution arrangement
handoff: docs/ephemeral/HDE-EPIC041-QA90-handoff-to-qa100-v1.0.md
authored_at: 2026-11-01 (UTC)
GCFPE_PROMPT_USES:
  - usage_id: HDE-EPIC041-QA90-20261101
    change: HDE-EPIC041 (EPIC)
    specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
    requirements: R-01 to R-04; AC-01 to AC-05; PF09.3 HDE-SEPA006.3
    ecosystem_release: GCFPE-20261027.1 / 102726.1
    prompt: QA-90 — 102726.1 (https://app.notion.com/p/4064590a05eb81929057e6667f7193c6), revision as of 2026-10-27T13:15:43.099Z
    role_stage: continuing Kronos / GCF-23 (QA-90)
    captured_at: 2026-11-01
    runtime_identity: not directly known (D27)
    inherited_usage: HDE-EPIC041-QA70-20261029
    outcome: TASK_READY (seven QA tasks, attempt 1 each; shared publication actions P-IDX-RUN and P-EL-01)
    result_references: this collection and its handoff at the paths above; their pull request and merge commit do not exist at writing and are recorded by the stage that reads them
    repository_persistence: PENDING (no docs/changes/GCFPE_PROMPT_PROVENANCE.md on main; owner GCFPE management; non-gating)
---

# HDE-EPIC041 — Bounded QA Execution Tasks v1.0 (QA-90): TASK_READY

## 1. Result

**`TASK_READY`.** The Product Owner selected `ALL`. Every one of the seven checks of the approved QA Plan v1.0 (§11) is authored below as a complete `QA_TASK`, attempt 1, in plan order, together with the two shared publication actions the Plan makes part of every check (P-IDX-RUN, the batch indexing run; P-EL-01, the landing pull request). Nothing has been executed. Every task is `NOT_EXECUTED` until QA-100 runs it.

* **Ready now:** T-01 to T-07 need only the environment contract (§3) and the Product Owner's execution arrangement (PI-01).
* **Dependency-waiting, fully authored:** P-IDX-RUN waits on IDX-01, the writer registration work item the Product Owner must assign (PI-02). P-EL-01 waits on PI-02 (route A or C) and PI-03 (who branches, commits, pushes and opens the landing pull request). Until they are decided, the evidence stays unchanged in the execution clone (Plan §13.3 "Persistence"), and QA PASS is not reachable (Plan §19 item 2; QA-70 N-14).
* **Rails, stated once and repeated in every task:** every QA command runs under **closed rails** `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, with pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`, through the closed-environment prefix CS-ENV. **No task opens rails.** The only network use in the whole collection is outside QA execution: the dependency install of setup step S-2 (package index) and the `git push` of P-EL-01. Neither is a QA step, and neither carries `SAFE_MODE=0` or `ALLOW_NETWORK=1`.
* **No class 1 or class 3 step exists** (Plan §5; Glow QA Guide §3.5.6). Every task is class 2 (internal functional and determinism) or evidence capture. The Product Owner therefore has no Live QA vendor workload to run; any operator the Product Owner chooses may run every task (QA-70 N-11).

Authored is not executed. This collection is preparation, not an execution result, a QA verdict, evidence, acceptance or closure.

## 2. Selection reconciliation

| Order | Task | Plan step (check_id) | Plan section | Attempt | Depends on | Status now | Result maps to |
| :- | :- | :- | :- | :- | :- | :- | :- |
| 1 | T-01 | `d0-discovery` | §12.1 | 1 | S-1 to S-4 | ISSUED, NOT_EXECUTED | QA-100 result for T-01 |
| 2 | T-02 | `step-0b-doc-delta-capture` | §12.2 | 1 | T-01 `PASS` | ISSUED, NOT_EXECUTED | QA-100 result for T-02 |
| 3 | T-03 | `ac01-orchestration-entry` | §12.3 | 1 | T-01 `PASS` | ISSUED, NOT_EXECUTED | QA-100 result for T-03 |
| 4 | T-04 | `ac02-pure-module` | §12.4 | 1 | T-01 `PASS` | ISSUED, NOT_EXECUTED | QA-100 result for T-04 |
| 5 | T-05 | `ac03-caller-migration` | §12.5 | 1 | T-01 `PASS` | ISSUED, NOT_EXECUTED | QA-100 result for T-05 |
| 6 | T-06 | `ac05-tracked-files-unchanged` | §12.6 | 1 | T-03 to T-05 recorded (any status) | ISSUED, NOT_EXECUTED | QA-100 result for T-06 |
| 7 | T-07 | `qa-closeout-deliverables` | §12.7 | 1 | T-02 to T-06 recorded (any status) | ISSUED, NOT_EXECUTED | QA-100 result for T-07 |
| — | P-IDX-RUN | IDX-RUN (publication of every task) | §13.2 | 1 | T-07 recorded; IDX-01 present (PI-02) | ISSUED, DEPENDENCY-WAITING | QA-100 batch publication result |
| — | P-EL-01 | EL-01 (landing of every task) | §13.3 | 1 | P-IDX-RUN complete; PI-02; PI-03; Nathan's commit instruction | ISSUED, DEPENDENCY-WAITING | QA-100 landing result |

* **Membership.** `ALL` resolves to exactly the seven checks of Plan §11, the Plan's only step ids (QA-70 review §8 defines `ALL` the same way). All seven are issued; none is deferred; no member was added, merged, split or renamed.
* **IDX-01 is not a QA task.** It is a routed PR work item on repository tooling (Plan §13.1; Glow QA Guide §3.4.8 "Non-QA-root remediation boundary"). This collection authors no PR, author, Proceed or code for it. Its owner is whoever the Product Owner assigns under PI-02.
* **Attempt history.** None. No earlier task, result or attempt exists for HDE-EPIC041 (`audit/qa/hde-epic041/` is absent on `main`, and `tools/evidence/update_evidence_index.py` names no `EPIC041` row; observed at `6b9c4c40`).
* **Rerun lineage.** Each check has one bounded rerun (Plan §16.2), attempt 2. When the executor uses it in-run under §16.2, that is the check's sole rerun: it is recorded in the same check directory, attempt 1 preserved and registered, and QA-110 reviews it. If it is not used in-run, a later rerun needs a QA-110 decision, the unchanged Plan, the exact first-failure evidence and a bounded correction, and QA-90 then authors that `attempt: 2` task. `FAIL_BEHAVIOR` is never rerun. A second failure escalates (Plan §16.3).

## 3. Shared environment, rails and setup (every task)

### 3.1 Rails and pins (identical for T-01 to T-07 and P-IDX-RUN)

| Setting | Value | Where it is set | Changed by any task |
| :- | :- | :- | :- |
| `SAFE_MODE` | `1` | CS-ENV | No |
| `ALLOW_NETWORK` | `0` | CS-ENV | No |
| `APP_ENV` | `dev` | CS-ENV | No |
| `LC_ALL` / `LANG` / `TZ` | `C` / `C` / `UTC` | CS-ENV | No |
| Credentials (`HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`) | not passed; `env -i` clears the operator's shell | CS-ENV | No |

**CS-ENV** (Plan §9.1), the prefix for every QA command, run from the execution clone's root:

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
```

`test_safe_mode_field` in `tests/adapter/test_chart_orchestration.py` (T-03) sets `SAFE_MODE` to `1`, `0` and unset by `monkeypatch` inside its own process. That is an input to the function under test, not a rails opening; the process rails stay closed (Plan §6.2). Each primary log's `captured_env` records the six rail and pin values actually in effect; QA-100 checks they read as in the table above.

### 3.2 Setup (environment contract EC-1 to EC-5; prerequisites, not QA steps)

* **S-1 (EC-1).** A full-history clone of `amthorn78/glow-hdengine-v2` with `main` checked out at the execution source and a clean tracked tree, provided by the execution arrangement. This collection does not instruct the checkout. Record the path used.
* **S-2 (EC-2). Rails: outside QA; network to the package index for dependency setup only.** From the execution clone's root:

```bash
mkdir -p /tmp/hde-epic041-qa/home && python3.12 -m venv /tmp/hde-epic041-qa/venv && /tmp/hde-epic041-qa/venv/bin/python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .
```

  Another `/tmp` path may be used if recorded; then CS-ENV's `PATH` and `HOME` use it too.
* **S-3 (EC-3). Rails: closed (CS-ENV).** Write the four check scripts of Plan §9.2 to `/tmp/hde-epic041-qa/` by extracting them mechanically from the approved Plan (the Plan says the operator writes each listed line followed by one LF; this command does exactly that), then confirm the digests. From the execution clone's root:

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import re; names = {'SC-D0': 'd0-discovery.sh', 'SC-0B': 'step-0b-doc-delta-capture.sh', 'SC-05': 'ac05-tracked-files-unchanged.sh', 'SC-CL': 'qa-closeout-deliverables.sh'}; cur = None; buf = {}; lines = open('docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md', encoding='utf-8').read().splitlines()
for l in lines:
    m = re.match(r'\*\*Script (SC-\w+)\*\*', l)
    if m: cur = m.group(1); buf[cur] = []; continue
    if cur:
        m = re.match(r'^(\d+)\. \x60(.*)\x60$', l)
        if m: buf[cur].append(m.group(2))
        elif l.startswith('### '): cur = None
for k, v in buf.items(): open('/tmp/hde-epic041-qa/' + names[k], 'w', encoding='utf-8', newline='\n').write('\n'.join(v) + '\n'); print(k, len(v), 'lines')"
sha256sum /tmp/hde-epic041-qa/*.sh
```

  Expected (Plan §9.2): `d0-discovery.sh` 24 lines `00092b587aa0c12a32dd0b8c5053fe0de4656e27876c8c58c3dcd2a959be476a`; `step-0b-doc-delta-capture.sh` 23 lines `ceffcbcd2c20c916af3ba58a6e3cf345ec521c685a54894f821b3dd4533c8003`; `ac05-tracked-files-unchanged.sh` 10 lines `139bd41ca5a91eca0557a6ae546ab9918429d138828e9268e99f7c62e74d772d`; `qa-closeout-deliverables.sh` 8 lines `d5420d277ab7cb840efc5cb4eb95d64806addb2398f4a8ce0772dc61ead95a45`. Kronos ran this extraction at authoring against the Plan on `main` and all four digests matched. Reading the Plan to build a `/tmp` helper is not evidence and binds no `docs/ephemeral/` path into evidence (HDE Build Notes R-1); the exact bytes run are recorded in each primary log's `command` field. Writing the lines by hand instead is equally valid if the digests match.
* **S-4 (EC-4, EC-5).** `bash`, `git`, `cmp`, `grep`, `cut`, `sort`, `date`, `sha256sum` on `/usr/bin:/bin`; every QA command from the execution clone's root behind CS-ENV.

### 3.3 Shared rules for every task

* **Interpreter and context.** `python` resolves to `/tmp/hde-epic041-qa/venv/bin/python` through CS-ENV's `PATH`; working directory is the execution clone's root.
* **Evidence persistence.** QA evidence is persisted in the repository. Every file a task writes lands under `audit/qa/hde-epic041/` or `audit/docdeltas/hde-epic041_doc_deltas.md` with its sibling `.path_proof.txt`, stays unchanged in the execution clone, and reaches `main` only through P-EL-01. Nothing under `/tmp` is evidence, and evidence is never left only in `/tmp`. **Committing the evidence needs Nathan's instruction, given in the executing session as part of that pull request.**
* **VCS.** No task creates a branch, checks out, commits, pushes, merges or rebases. Read-only `git` observations are provenance only.
* **Normalization.** An operator may normalize command syntax in flight when proof target, check identity, rails, evidence identity and verdict meaning stay unchanged (Glow QA Guide §3.4.7; Plan §16.4). Record the exact command run (the primary log does), the reason (in the CS-2 provenance argument, or in the QA-100 result for a CS-1 task), and a DRIFT item through CS-5 before T-07. More than three plan-to-evidence structural mismatches pause execution for systems RCA.
* **Recovery.** `record_check` publishes atomically with rollback. After an interruption, read `audit/qa/hde-epic041/qa_step_logs_manifest.json` and resume from the first planned task without an entry; cancellation is incomplete work and consumes no rerun. Inspect an uncertain write before any retry. Never delete or regenerate an evidence file before landing (Plan §17).
* **Bounded rerun helpers** (Plan §9.1, used only under §16.2): CS-4, with `d` set to the check directory:

```bash
for f in "$d"/*; do b=$(basename "$f"); case "$b" in tmp_attempt1_*|*.path_proof.txt) ;; *) cp -p "$f" "$d/tmp_attempt1_$b";; esac; done
```

  and CS-5 (one DRIFT line appended to both doc-delta surfaces; adjust the item text to the actual event, then refresh both proofs with the CS-3 publish command of T-02 restricted to the two doc-delta files):

```bash
printf '%s\n' '- DRIFT-001 (CAVEAT; drives decision: No): check ac02-pure-module was rerun once after attempt 1 was TOOLING_BLOCKED by a missing install; its executed commands are recorded in audit/qa/hde-epic041/checks/ac02-pure-module/primary.log.' | tee -a audit/docdeltas/hde-epic041_doc_deltas.md >> audit/qa/hde-epic041/00_meta/doc_deltas.md
```

  Rerun procedure: CS-4; one-line note to `<dir>/tmp_attempt1_remediation_note.txt`; the task's run-and-record command unchanged except that its extra-evidence argument also lists every `tmp_attempt1_` file; CS-3 on the new primary, every `tmp_attempt1_` file and the manifest; CS-5 and CS-3 on the pair. Worked example: Plan §16.2 (check `ac02-pure-module`).
* **Return to QA-110 (every task).** Per task: status and exit code as printed, the primary path and its proof, every other produced path and proof, the CS-3 output line, the manifest entry (`check_id`, `log_path`, `status`), any normalization or rerun, and every gap with its owner. QA-100 returns `COMPLETE`, `PARTIAL`, `BLOCKED`, `FAILED` or `NOT_EXECUTED` truthfully (QA-90 "QA authorship and Product Owner execution choice").

## 4. Tasks

### T-01 — `d0-discovery`: D0 discovery

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.1 (check 1 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `d0-discovery`; **attempt: 1**.
* **Step class:** evidence capture.
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** S-1 to S-4 complete. First task; gates every other task.
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: clean tracked tree at the execution source; the venv; `tools/qa/qa_harness.py`; the 19 loci and nine selectors of QA Audit §5 (L-01 to L-31); script SC-D0.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Preflight: the digest must print `00092b587aa0c12a32dd0b8c5053fe0de4656e27876c8c58c3dcd2a959be476a`; otherwise stop and rebuild the script (S-3).

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev sha256sum /tmp/hde-epic041-qa/d0-discovery.sh
```

  2. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" d0-discovery "D0 discovery" TOOLING_BLOCKED "HDE-EPIC041 QA Plan v1.0 script SC-D0 as written; run and recorded by snippet CS-2" audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt,audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt,audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt,audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt /tmp/hde-epic041-qa/d0-discovery.sh
```

  3. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/d0-discovery/primary.log audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.1):
  * **PASS** if SC-D0 exits 0: `git diff --quiet HEAD` succeeds; `python -m pytest --version` succeeds; all 19 loci exist; the harness accepts `HDE-EPIC041` and the seven check ids; collection ends `43 tests collected`; `git check-ignore -v --no-index` exits 1 for the six listed evidence paths; the caller set equals QA Audit L-31 exactly (11 paths). `d0-env-rails.txt` must show `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC` and environment names only, no values.
  * **FAIL_BEHAVIOR:** not applicable; D0 decides no product behavior.
  * **FAIL_TOOLING** if CS-2 or `record_check` raises, or SC-D0 exits other than 0, 1 or 3.
  * **TOOLING_BLOCKED** if SC-D0 exits 1 or 3; `status_reason` lists every failing precondition. A caller-set difference is a plan-validity block that returns the open-rails determination to Kronos (Plan §3, §16.3); a live step would then need separate, task-specific Product Owner authorization.
* **Task notes:** If T-01 is not `PASS` after at most one bounded rerun (Plan §16.2, after environment repair only), stop: T-02 to T-07 are `NOT_EXECUTED`, and the run returns `BLOCKED` with T-01's receipt (Plan §16.1; QA-70 N-12). Supplementary, non-gating: QA-root and doc-delta presence before the check, untracked files, the `EPIC041_QA_PRIMARY_ARTIFACTS` count (0 until IDX-01), the writer `--check` baseline.
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/d0-discovery/primary.log`; `audit/qa/hde-epic041/checks/d0-discovery/d0-env-rails.txt`; `audit/qa/hde-epic041/checks/d0-discovery/d0-entrypoint-preflight.txt`; `audit/qa/hde-epic041/checks/d0-discovery/d0-gitignore-audit-qa.txt`; `audit/qa/hde-epic041/checks/d0-discovery/d0-caller-set.txt`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `d0-discovery`, `log_path` `audit/qa/hde-epic041/checks/d0-discovery/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.d0_discovery.primary.log`, `audit.qa.hde_epic041.checks.d0_discovery.d0_env_rails.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_entrypoint_preflight.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_gitignore_audit_qa.txt`, `audit.qa.hde_epic041.checks.d0_discovery.d0_caller_set.txt`, `epic041.qa_step_logs_manifest`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

### T-02 — `step-0b-doc-delta-capture`: Step-0B doc delta capture

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.2 (check 2 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `step-0b-doc-delta-capture`; **attempt: 1**.
* **Step class:** evidence capture.
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** T-01 recorded `PASS` in the manifest (SC-0B line 6 enforces it).
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: the manifest from T-01; canon files resolved at run time by versionless pattern (HDE Architecture, HDE Mechanics Guide, HDE State of the Repository; QA Audit L-29, text keys L-30); neither doc-delta surface may pre-exist.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Preflight: the digest must print `ceffcbcd2c20c916af3ba58a6e3cf345ec521c685a54894f821b3dd4533c8003`; otherwise stop and rebuild the script (S-3).

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev sha256sum /tmp/hde-epic041-qa/step-0b-doc-delta-capture.sh
```

  2. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" step-0b-doc-delta-capture "Step-0B doc delta capture" FAIL_TOOLING "HDE-EPIC041 QA Plan v1.0 script SC-0B as written; run and recorded by snippet CS-2" audit/docdeltas/hde-epic041_doc_deltas.md,audit/qa/hde-epic041/00_meta/doc_deltas.md /tmp/hde-epic041-qa/step-0b-doc-delta-capture.sh
```

  3. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log audit/docdeltas/hde-epic041_doc_deltas.md audit/qa/hde-epic041/00_meta/doc_deltas.md audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.2):
  * **PASS** if SC-0B exits 0: neither surface existed; T-01 is `PASS`; each canon pattern resolved to one file; both surfaces written and `cmp`-identical; neither names `docs/ephemeral` or `docs/pfcanon`; items DELTA-001 to DELTA-003 listed, each "CAVEAT; drives decision: No" or "resolved at this source"; `## BLOCKERS` reads `none`.
  * **FAIL_BEHAVIOR:** not applicable.
  * **FAIL_TOOLING** if SC-0B exits 1 (pair differs, forbidden path string, no item) or other than 0, 1 or 3, or recording raises.
  * **TOOLING_BLOCKED** if SC-0B exits 3: a surface already exists (preserved unchanged), T-01 is not `PASS`, a tool is missing, or a canon pattern does not resolve to exactly one file.
* **Task notes:** **Caution N-01:** if SC-0B exits 3 without writing the pair, run the publish command on the T-02 primary and the manifest only (drop the two doc-delta paths) and record that normalization; if it exits 3 because a surface exists, do not refresh that surface's proof. Bounded rerun only if SC-0B wrote no surface; otherwise preserve the surfaces and escalate. Later DRIFT items are appended only by CS-5, before T-07.
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log`; `audit/docdeltas/hde-epic041_doc_deltas.md`; `audit/qa/hde-epic041/00_meta/doc_deltas.md`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `step-0b-doc-delta-capture`, `log_path` `audit/qa/hde-epic041/checks/step-0b-doc-delta-capture/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.step_0b_doc_delta_capture.primary.log`, `epic041.doc_deltas`, `audit.qa.hde_epic041.00_meta.doc_deltas.md`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

### T-03 — `ac01-orchestration-entry`: Adapter-owned chart entry functional proof

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.3 (check 3 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `ac01-orchestration-entry`; **attempt: 1**.
* **Step class:** class 2 (internal functional and determinism); the Plan's named functional proof step for the adapter-to-engine seam.
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** T-01 recorded `PASS`. Independent of T-02, T-04 and T-05.
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: `tests/adapter/test_chart_orchestration.py` (QA Audit L-05) exercising `adapter/chart_orchestration.py`.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))" ac01-orchestration-entry "Adapter-owned chart entry functional proof" "" tests/adapter/test_chart_orchestration.py -p no:cacheprovider
```

  2. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.3):
  * **PASS** if the readiness command and pytest both exit 0; the summary is expected to read `20 passed`. A different count with exit 0 is an evidence-identity defect for QA-110, not PASS.
  * **FAIL_BEHAVIOR** if pytest exits 1.
  * **FAIL_TOOLING** if pytest exits 2, 3, 4 or negative, or a launch raises.
  * **TOOLING_BLOCKED** if readiness fails, a selector file is missing, an option is unsupported, or pytest exits 5.
* **Task notes:** Covers R-01/AC-01, R-04/AC-04, AC-05 (the entry writes no file). A failure here does not stop T-04 or T-05.
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `ac01-orchestration-entry`, `log_path` `audit/qa/hde-epic041/checks/ac01-orchestration-entry/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.ac01_orchestration_entry.primary.log`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

### T-04 — `ac02-pure-module`: Pure Engine chart module purity and interface

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.4 (check 4 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `ac02-pure-module`; **attempt: 1**.
* **Step class:** class 2 (internal functional and determinism).
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** T-01 recorded `PASS`. Independent of T-03 and T-05.
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: `tests/charts/test_chart_pure_purity.py`, `tests/charts/test_chart_pure_interface.py` (L-06, L-07) exercising `engine/charts/pure.py`.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))" ac02-pure-module "Pure Engine chart module purity and interface" "" tests/charts/test_chart_pure_purity.py tests/charts/test_chart_pure_interface.py -p no:cacheprovider
```

  2. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac02-pure-module/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.4):
  * **PASS** if readiness and pytest both exit 0; summary expected `13 passed` (a different count with exit 0 is an evidence-identity defect, not PASS).
  * **FAIL_BEHAVIOR** if pytest exits 1.
  * **FAIL_TOOLING** if pytest exits 2, 3, 4 or negative, or a launch raises.
  * **TOOLING_BLOCKED** if readiness fails, a selector is missing, an option is unsupported, or pytest exits 5.
* **Task notes:** Covers R-02/AC-02 including purity at import, R-04/AC-04. Plan §16.2's worked rerun example uses this check.
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `ac02-pure-module`, `log_path` `audit/qa/hde-epic041/checks/ac02-pure-module/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.ac02_pure_module.primary.log`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

### T-05 — `ac03-caller-migration`: Caller migration, retirement guard and retained coverage

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.5 (check 5 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `ac03-caller-migration`; **attempt: 1**.
* **Step class:** class 2 (internal functional and determinism).
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** T-01 recorded `PASS`. Independent of T-03 and T-04.
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: `tests/charts/test_chart_loader_import_guard.py`, `tests/scripts/test_make_compat_determinism_artifacts.py`, `tests/loader/test_load_chart_fixture_only.py`, `tests/loader/test_loader_logs_keys_only.py`, `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode`, `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` (L-08 to L-13). The two provider selectors prove refusal **under `SAFE_MODE=1`**; they make no vendor call.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import dataclasses, sys; from tools.qa.qa_harness import HarnessConfig, record_check, run_pytest_check; c = HarnessConfig('HDE-EPIC041'); cid, name, extra = sys.argv[1:4]; r = run_pytest_check(c, cid, sys.argv[4:], check_name=name); r = dataclasses.replace(r, evidence_artifacts=tuple(x for x in extra.split(',') if x)) if extra else r; record_check(c, r); print('status=' + r.status.value, 'exit_code=' + str(r.exit_code))" ac03-caller-migration "Caller migration, retirement guard and retained coverage" "" tests/charts/test_chart_loader_import_guard.py tests/scripts/test_make_compat_determinism_artifacts.py tests/loader/test_load_chart_fixture_only.py tests/loader/test_loader_logs_keys_only.py tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on -p no:cacheprovider
```

  2. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.5):
  * **PASS** if readiness and pytest both exit 0; summary expected `10 passed` (a different count with exit 0 is an evidence-identity defect, not PASS). Includes C-1 (`scripts/make_compat_determinism_artifacts.py`) exiting 2 with `compat_public not implemented` and writing nothing; that exit 2 is the expected behavior, not a passing compat gate.
  * **FAIL_BEHAVIOR** if pytest exits 1.
  * **FAIL_TOOLING** if pytest exits 2, 3, 4 or negative, or a launch raises.
  * **TOOLING_BLOCKED** if readiness fails, a selector is missing, an option is unsupported, or pytest exits 5.
* **Task notes:** Covers R-01/AC-01, R-03/AC-03, R-04/AC-04, AC-05; QR-02.
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `ac03-caller-migration`, `log_path` `audit/qa/hde-epic041/checks/ac03-caller-migration/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.ac03_caller_migration.primary.log`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

### T-06 — `ac05-tracked-files-unchanged`: Tracked files unchanged after the covering runs

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.6 (check 6 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `ac05-tracked-files-unchanged`; **attempt: 1**.
* **Step class:** class 2.
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** T-03, T-04 and T-05 recorded, whatever their status.
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: the execution clone's working tree after T-03 to T-05; script SC-05.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Preflight: the digest must print `139bd41ca5a91eca0557a6ae546ab9918429d138828e9268e99f7c62e74d772d`; otherwise stop and rebuild the script (S-3).

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev sha256sum /tmp/hde-epic041-qa/ac05-tracked-files-unchanged.sh
```

  2. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" ac05-tracked-files-unchanged "Tracked files unchanged after the covering runs" FAIL_BEHAVIOR "HDE-EPIC041 QA Plan v1.0 script SC-05 as written; run and recorded by snippet CS-2" "" /tmp/hde-epic041-qa/ac05-tracked-files-unchanged.sh
```

  3. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.6):
  * **PASS** if `git diff --exit-code --stat HEAD`, excluding only `audit/qa/hde-epic041`, `audit/docdeltas/hde-epic041_doc_deltas.md` and its proof, exits 0.
  * **FAIL_BEHAVIOR** if that `git diff` exits 1: a tracked file changed after the covering runs. Preserve the tree as found; do not reset it before capture.
  * **FAIL_TOOLING** if SC-05 exits other than 0, 1 or 3, or recording raises.
  * **TOOLING_BLOCKED** if SC-05 exits 3 (`git` missing or `git diff` failed).
* **Task notes:** **Caution N-03:** the supplementary untracked listing is `git status --porcelain` and also shows modified tracked files; it is non-gating. Covers AC-05's tracked-file limb (R-01, R-03, R-04).
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `ac05-tracked-files-unchanged`, `log_path` `audit/qa/hde-epic041/checks/ac05-tracked-files-unchanged/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.ac05_tracked_files_unchanged.primary.log`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

### T-07 — `qa-closeout-deliverables`: QA closeout deliverables integrity

* **Binding:** QA Plan v1.0 `docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md` §12.7 (check 7 of 7); QA-70 review `docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md` (APPROVE); QA Audit `docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md`; change HDE-EPIC041; step `qa-closeout-deliverables`; **attempt: 1**.
* **Step class:** evidence capture.
* **Rails:** **closed** — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`; set by CS-ENV on every command below; no rails change before, during or after this task; no network.
* **Environment / target:** the execution clone of `amthorn78/glow-hdengine-v2` at the `main` execution source (S-1), repository-local only; no deployed service, HTTP route, CLI command, vendor or database is exercised.
* **Dependencies:** T-02 to T-06 recorded, whatever their status; any owed DRIFT item appended first.
* **Setup / data:** S-1 to S-4 (§3.2); synthetic fixture data only, inside the tests; no secret is read. Semantic inputs: the manifest; every artifact listed in the earlier primaries' `evidence_artifacts`; the doc-delta pair; script SC-CL.
* **Commands** (from the execution clone's root; CS-ENV prefix included):

  1. Preflight: the digest must print `d5420d277ab7cb840efc5cb4eb95d64806addb2398f4a8ce0772dc61ead95a45`; otherwise stop and rebuild the script (S-3).

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev sha256sum /tmp/hde-epic041-qa/qa-closeout-deliverables.sh
```

  2. If a DRIFT item is owed, append it with CS-5 (§3.3) and refresh both doc-delta proofs, then continue.

  3. Run and record (status printed as `status=<STATUS> exit_code=<N>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import subprocess, sys; from pathlib import Path; from tools.qa.qa_harness import CheckResult, HarnessConfig, Status, record_check; c = HarnessConfig('HDE-EPIC041'); cid, name, bad, prov, extra, script = sys.argv[1:7]; text = Path(script).read_text(encoding='utf-8'); p = subprocess.run(('bash', '-c', text), cwd=c.repo_root, capture_output=True, text=True); out = p.stdout + p.stderr; s = {0: Status.PASS, 1: Status(bad), 3: Status.TOOLING_BLOCKED}.get(p.returncode, Status.FAIL_TOOLING); why = '; '.join(x[8:] for x in out.splitlines() if x.startswith('REASON: ')) or 'script exited ' + str(p.returncode); r = CheckResult(check_id=cid, status=s, status_reason='' if s is Status.PASS else why, check_name=name, command=('bash', '-c', text), command_provenance=prov, exit_code=p.returncode, output=out, evidence_artifacts=tuple(x for x in extra.split(',') if x), pf_refs=('PF06-Canon-Change-Process-Guide', 'PF19-Canon-Glow-QA-Guide', 'PF27-Canon-Plan-Templates')); record_check(c, r); print('status=' + s.value, 'exit_code=' + str(p.returncode))" qa-closeout-deliverables "QA closeout deliverables integrity" FAIL_TOOLING "HDE-EPIC041 QA Plan v1.0 script SC-CL as written; run and recorded by snippet CS-2" "" /tmp/hde-epic041-qa/qa-closeout-deliverables.sh
```

  4. Publish capture-time path proofs and verify them (prints `path proofs written and verified: <count>`):

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import sys; import tools.evidence.update_evidence_index as u; t = sys.argv[1]; ps = sys.argv[2:]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=False) for p in ps]; [u._refresh_path_proof(u.ROOT / p, default_produced_at=t, check=True) for p in ps]; print('path proofs written and verified:', len(ps))" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log audit/qa/hde-epic041/qa_step_logs_manifest.json
```

* **Expected outcome and PASS/FAIL evidence** (Plan §12.7):
  * **PASS** if SC-CL exits 0: the manifest holds the six earlier checks (any status); `_refresh_path_proof(..., check=True)` verifies every listed artifact, the manifest and both doc-delta surfaces; `cmp` finds the pair identical; neither names `docs/ephemeral` or `docs/pfcanon`.
  * **FAIL_BEHAVIOR:** not applicable.
  * **FAIL_TOOLING** if SC-CL exits 1 (a proof missing or stale, pair differs, forbidden path string) or other than 0, 1 or 3, or recording raises; an evidence-assembly defect correctable by Moon Loop within the QA root (Plan §10).
  * **TOOLING_BLOCKED** if SC-CL exits 3 (a planned check has no manifest entry, or the writer module does not import).
* **Task notes:** **Step before run (Plan §12.7 step 2):** if any DRIFT item is owed (a normalization, a rerun, a Moon Loop), append it with CS-5 and refresh both doc-delta proofs first. **Caution N-04:** expect 13 proofs verified with no rerun, 15 after one rerun; do not expect 16. This check's own proof and the final manifest proof are verified by P-IDX-RUN's validators.
* **Evidence paths (QA-created; each with a sibling `.path_proof.txt` written by the publish command):** `audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log`; `audit/qa/hde-epic041/qa_step_logs_manifest.json`. Manifest entry: `check_id` `qa-closeout-deliverables`, `log_path` `audit/qa/hde-epic041/checks/qa-closeout-deliverables/primary.log`, `status`. Primary header `pf27.step_log_header.v2`, `intended_tokens: []`, `claimed_tokens: []`.
* **Registration keys (Plan §8.3):** `audit.qa.hde_epic041.checks.qa_closeout_deliverables.primary.log`; indexed by P-IDX-RUN through `tools/evidence/update_evidence_index.py` once IDX-01 lists them.
* **Landing route:** P-EL-01 (route A, or route C if the Product Owner declines A). The files stay unchanged in the execution clone until then. Their commit needs Nathan's instruction, given in the executing session as part of that pull request.
* **Cleanup / recovery:** no write outside the QA evidence paths; `.pytest_cache` disabled; `__pycache__` is git-ignored. On interruption, read the manifest and resume. One bounded rerun under Plan §16.2 for an execution or evidence fault outside the product (CS-4, note, rerun, CS-3, CS-5); never for `FAIL_BEHAVIOR`.
* **Return to QA-110:** as §3.3, for this task.

## 5. Shared publication actions

### P-IDX-RUN — batch indexing (Plan §13.2), attempt 1

* **Plan / review / Audit / change:** QA Plan v1.0 §13.2 and §8.3; QA-70 review v1.0; QA Audit v1.0 §10.2 to §10.4; HDE-EPIC041.
* **Rails:** **closed** — CS-ENV (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`). The writer refuses to write unless the pins and closed rails hold.
* **Environment / target:** the working tree that holds the produced evidence and IDX-01's list: the landing branch under route A; the execution clone under route C (Plan §13.2).
* **Dependencies:** T-07 recorded; IDX-01 present in the working tree (an `EPIC041_QA_PRIMARY_ARTIFACTS` list with exactly one row per file the run actually produced, Plan §13.1); every listed file present. **Without IDX-01 this action is not run, and indexing stays incomplete** (Plan §13.4); report it as `NOT_EXECUTED` with owner "IDX-01 author assigned under PI-02".
* **Commands** (each behind CS-ENV, from the working tree's root):
  1. Write: `python tools/evidence/update_evidence_index.py`
  2. Read-only validation, each expected to exit 0: `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `ci/checks/check_mirror_schema.sh`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_evidence_index_hash.sh`; `python tools/evidence/check_lf_endings.py`. Never run `tools/evidence/orientation_demo.py` without `--check`.
  3. Row confirmation:

```bash
env -i PATH=/tmp/hde-epic041-qa/venv/bin:/usr/bin:/bin HOME=/tmp/hde-epic041-qa/home LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev python -c "import json; rows = sorted((r['artifact_key'], r['discovered_physical_path']) for r in json.load(open('docs/evidence/INDEX.json')) if r.get('epic_id') == 'HDE-EPIC041'); [print(k, p) for k, p in rows]; print('rows:', len(rows))"
```

* **Semantic outputs:** regenerated `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt` and their proofs, written by the canonical writer only. Never hand-edit any of them.
* **Per-task mapping** (Plan §13.2): T-01 six rows (primary, four sidecars, manifest); T-02 three rows (primary and the doc-delta pair); T-03 to T-07 one primary row each; plus any `tmp_attempt1_` file a rerun produced. Each row's proof is the capture-time proof that task's CS-3 wrote; the writer keeps it.
* **Expected outcome / PASS evidence:** write exits 0; all six validators exit 0; the row confirmation lists exactly the registration-set rows of Plan §8.3 (14 unconditional rows plus each actual rerun file) and prints that count. Before the write, `--check` is expected to report `STALE` once IDX-01 is present; that is not a failure (Plan §13.1).
* **FAIL evidence:** any validator non-zero, or a row missing or extra. Missing indexing is incomplete work or a tooling outcome, never a behavioral result and never PASS. Return it to the writer's owner without rerunning valid QA solely to index it.
* **Cleanup/recovery:** none beyond the writer's own convergence; on a failed write, inspect the tree before any retry.
* **Return to QA-110:** the write output; each validator's command, exit code and output; the row confirmation output; every gap with its owner.

### P-EL-01 — landing pull request (Plan §13.3), attempt 1

* **Rails:** not a QA command. `git` operations run in the operator's ordinary shell; `git push` uses the network to GitHub only. No product code runs; no rails value is set or changed.
* **Dependencies:** P-IDX-RUN complete (route A) or IDX-01 merged first (route C); PI-02 (route A or C); PI-03 (who performs the branch, commit, push and pull request); **Nathan's instruction to commit, given in the executing session as part of that pull request.** Nathan alone merges.
* **Route A (planned; needs the Product Owner's approval under PI-02 and CCR-6).** One pull request from branch `qa/hde-epic041-live-qa-evidence` carrying every QA-run artifact with its proof exactly as produced (not regenerated), the IDX-01 change and its owner test, and P-IDX-RUN's regenerated Index, Mirror, sentinels, orientation output and their proofs. Its body follows Change Process Guide §4.5 and AGENTS.md "PR descriptions", and states the IDX-01 tooling change separately. It merges before any close pull request.
* **Route C (only if route A is declined).** IDX-01 lands first as its own presence-gated, fail-closed PR; then an evidence-only QA PR from `qa/hde-epic041-live-qa-evidence` carries the evidence and P-IDX-RUN's outputs. A rerun file the landed registration does not list needs an IDX-01 amendment first.
* **Not allowed:** route B (landing evidence unindexed and indexing later).
* **Expected outcome / PASS evidence:** the pull request's exact-head CI passes, classifying to the `evidence` and `release` lanes, plus `product` and the writer's owner test lane when IDX-01 is included; the six validators exit 0 at its reviewed head.
* **Return to QA-110:** pull request number and URL, base, reviewed head, exact-head CI run and result, merge commit when Nathan merges; the execution source recorded by T-01 kept distinct from all of them (Plan §6.3, §19 item 3).
* **Cleanup:** `/tmp/hde-epic041-qa/` may be deleted only after the landing pull request carries the evidence.

## 6. Execution cautions carried from the QA-70 review

| Id | Carried into | Caution |
| :- | :- | :- |
| N-01 | T-02 | When SC-0B exits 3 **without writing the pair** (a missing tool, or a canon pattern that does not resolve to one file), the publish command as written fails on the absent doc-delta file. Normalize: run the CS-3 publish on the T-02 primary and the manifest only, and record the normalization. When SC-0B exits 3 because a surface already exists, do not refresh the preserved surface's proof. |
| N-02 | T-01 to T-07, return | `_refresh_path_proof` keeps an existing proof's `produced_at_utc` and `mtime_utc` and refreshes only hash and size, so a file written more than once (the manifest, a rerun primary, the pair after CS-5) carries its first capture time. Take timing facts from each primary header's `timestamp_utc`, not from proofs. |
| N-03 | T-06 | SC-05's "untracked outside the QA evidence paths" listing is `git status --porcelain` and also lists modified tracked files. It is supplementary and non-gating; the gating predicate is SC-05 line 3's `git diff`. |
| N-04 | T-07 | T-07 verifies 13 proofs with no rerun, 15 after one rerun in plan order, 16 only if T-07 already ran once before. No predicate depends on the number; do not expect 16. |
| N-11 | §1 | No class 1 or class 3 step exists; the Product Owner has no Live QA vendor workload; any operator the Product Owner chooses may run every task. |

Also carried for the readers that follow, not as task steps: N-06 (QA-120 cites the WU-PR-02 record #796 and Reality Audit §12.4 for AC-03's inventory limb), N-07 (a `record_check` raise records nothing; QA-100 classifies it `FAIL_TOOLING` in its result, and T-07 will then find the entry missing), N-12 (T-01 has one bounded rerun after environment repair; then stop).

## 7. Final-report criteria the tasks feed (Plan §19, unchanged)

A QA PASS is supportable only when T-01 to T-07 are recorded `PASS` (a rerun `PASS` only with attempt 1 preserved and registered and the DRIFT item present), each primary carries the expected header and `exit_code` 0, and T-03 to T-05 report 20, 13 and 10 passed; every QA-run artifact is on `main` through P-EL-01 with its capture-time proof and indexed; the execution source and the landing PR's base, reviewed head, merge commit and review-time HEAD are distinct recorded facts; T-01's caller set still equals the QA Audit's; the doc-delta pair is byte-identical on `main` with DELTA-001 to -003 and every DRIFT item; and limitations IR-01, IR-02 and bound evidence BE-01 to BE-05 are stated. This collection decides none of these.

### 7.1 Authoring check of this collection (not QA execution, not evidence)

On 2026-11-01 Kronos extracted every `bash` block of this file mechanically and ran S-3 and T-01 to T-07 in plan order in a throwaway clone of `main` at `6b9c4c40`, with the venv at `/tmp/hde-epic041-qa/venv` built by S-2 (Python 3.12, pip exit 0). Every command exited 0; the four script digests matched; all seven checks recorded `PASS`; T-03 to T-05 reported `20 passed`, `13 passed` and `10 passed`; `captured_env` showed `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`; only the QA evidence paths were created. The P-IDX-RUN row confirmation command ran (`rows: 0`, as expected without IDX-01); the write and validators were not run, because IDX-01 does not exist (QA-70 §3 rehearsed them). The clone and `/tmp/hde-epic041-qa/` were then deleted. This check only confirms the commands were transcribed faithfully; it is not a QA run, a result or evidence, and QA-100 runs every task afresh.

## 8. Canon relied on

Resolved from `docs/pfcanon/` on `main` at `6b9c4c40`; each stable identity resolved to one controlled Markdown file; no Google Doc, export or archive was opened. `git diff --stat bba6337 6b9c4c4 -- . ':(exclude)docs/ephemeral'` is empty, so canon, code and tools are the ones QA-50 and QA-70 read. Terms searched (`grep -n -i` over the files below and `docs/ephemeral/HDE-EPIC041-*`): normalization, QA_TASK, bounded task, execution task, attempt, rerun, class 3, vendor vs non-vendor, Addendum Index.

| Title (file) | Sections read | Used for |
| :- | :- | :- |
| Glow QA Guide (`PF19-Canon-Glow-QA-Guide-v3.0.7.md`) | §3.1.2 "Independent QA, reporting and closure"; §3.4.7 syntax-normalization paragraphs; the execution-trace requirement and reviewer hygiene rules (L1050 to L1066); §3.5.6 "Vendor vs non-vendor steps in Live QA plans" | Operators execute approved bounded tasks; Kronos retains per-task results and retry lineage; in-flight normalization record; class labelling (§1) |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.4.md`) | "Precedence, versioning, and scope" as read by QA-70; §1.1 Addendum Index; 2.2 R-1 to R-3 as applied by the Plan | No evidence binds `docs/ephemeral/`; canon by title; no close pack in QA. No new addendum since the Plan |
| Plan Templates, Change Process Guide, HDE Schemas and Artifacts | As read and cited by the approved Plan §0.1 and QA-70 §"Canon relied on"; not re-adjudicated here | Task content is the approved Plan's; this collection packages it |
| AGENTS.md | Closed rails; pytest readiness; QA output placement; "Evidence harness"; "PR descriptions" | §3; P-IDX-RUN; P-EL-01 |

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

No formally approved bounded Product Owner rescope applies.

## 9. Unresolved items and owners

* PI-01 execution arrangement; PI-02 IDX-01 author and route A or C; PI-03 landing lane: Product Owner.
* CCR-5 (before CL-05) and CCR-6 (before P-EL-01): Product Owner.
* QR-07 (`main` push CI classification): Product Owner.
* Prompt-use repository persistence: GCFPE management (non-gating).
* No `QA_PREEXECUTION_FINDING`: packaging found no material Plan defect; the QA-70 notes are carried as cautions (§6) and none changes objective, target, rails, evidence or acceptance.

## 10. CANON_CONFLICT_REGISTER

Carried unchanged from the QA-70 review v1.0 §7 (itself carrying QA Plan v1.0 §21). QA-90 adds no entry and decides none. History addition for every entry: "carried unchanged by QA-90 task collection v1.0, Kronos, 2026-11-01".

| ID | Classification | Sources and clauses | Conflict | Affected | Alternatives and recommended disposition | Interim treatment and risk | Drainage target and owner | Status | Reviewer, reviewed artifact, decision time and rationale; history |
| :- | :- | :- | :- | :- | :- | :- | :- | :- | :- |
| CCR-1 | CANON_RECONCILIATION | Plan Templates Preflight B against HDE Governance §2.0.19 and HDE Schemas and Artifacts "legacy token compatibility shape" | Is an acceptance map required for tokenless work? | Specification §10; TI-07 | No operative conflict; listed with no token roster (Ruling R-A) | Close-pack matter for CL-05 | Product Owner (possible canon change) | APPROVED | Thoth, CF-E-30 review v1.1 of Specification v1.1, 2026-10-28; confirmed by Isis, IA-30 review v1.1; carried unchanged by QA Plan v1.0 and here |
| CCR-2 | CANON_RECONCILIATION | HDE Governance §9.7.7 against Plan Templates §2 | Business Case content lists differ | Specification §2 | Specification v1.1 satisfies both | None | None needed | APPROVED | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-3 | CANON_RECONCILIATION | HDE Build Notes (S19 vendor route selection, production vendor override) against the Specification's "adjacent" reading | Possible reach into the orchestration path | TI-02 | Conditional: governs only if the entry performs resolver-selected vendor acquisition | Not triggered (Plan §3; re-checked in §5 here) | Implementation Audit determined applicability | APPROVED as conditional | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-4 | CANON_RECONCILIATION | PF09.3 Task HDE-SEPA006 notes against the current HDE Build Notes | Cited loader record no longer in PF10 | Specification §5 | No conflict; PF09.3 states the defect in full | None | None | APPROVED | Thoth, review v1.1, 2026-10-28; carried unchanged |
| CCR-5 | CANON_RECONCILIATION | HDE Build Notes (close-pack writer only at close, first bullet) against Change Process Guide §3.5.1 "Close-mutation-set stage", Glow QA Guide §3.1.3 and Plan Templates §3B "Entries and exit (normative)" | The Build Notes rule puts the closure decision before the close-pack write; the three permanent documents put the close mutation set before the closure decision | Specification §10, §6 D5; Plan v1.1 DL-04; CL-05 | (A) the Build Notes rule stands; (B) a correcting addendum restores the CL-05 entries and exit; recommended: an explicit Product Owner ruling before CL-05 | The Build Notes rule governs as written; QA planning and execution unaffected (no QA step writes a close pack) | HDE Build Notes under (B), or the three permanent documents under (A); Product Owner | PROPOSED | Not yet reviewed; proposed by Isis, QA-10 triage v1.0 (full entry and history in its §6); recorded in HDE Build Notes 2.5; carried unchanged by the Guide, QA Plan v1.0 and here. Not a QA Plan decision: it bears on CL-05 only |
| CCR-6 | CANON_RECONCILIATION | Change Process Guide §0.7 "QA branches posture" ("Allowed changes are limited to governed artifacts" of a listed set; no tooling) against Change Process Guide §3.5.2.8 "Live QA evidence landing", Glow QA Guide §3.4.3 and §3.4.8 (non-QA-root remediation is a routed work item), and PF09.3 HDE-SEPA006.3 (indexing through the existing writer) | §0.7's list names neither Epic QA-root artifacts nor the doc-delta pair, and no landing route covers evidence plus the writer registration it needs; the writer cannot index a static list before its files exist | QR-04; G-OBS-01; Specification §8, §6 D4; QA Plan §13 | (A) route A under an explicit Product Owner decision (HDE-EPIC040 D-3 precedent, CC-3); (B) route C, a presence-gated writer registration first, then an evidence-only QA PR. Recommended by Kronos: (A), decided by the Product Owner before EL-01, with a later canon clarification of §0.7 | Route A pending PI-02; risk: evidence unindexed if neither is chosen (RK-QA-01), in which case QA PASS is not reachable (Plan §19 item 2) | Change Process Guide §0.7 and §3.5.2.8; Product Owner | PROPOSED | Proposed by Kronos, QA-50 QA Audit v1.0 finding QA50-F03 and QA Plan v1.0 §21, 2026-10-29. **QA-70 assessment (Isis, this review v1.0 of QA Plan v1.0, 2026-10-29):** the Plan's treatment is sound and executable under either alternative. Both keep the same-mutation-set parity rule; both leave the tooling change to a routed PR work item rather than Moon Loop, as Glow QA Guide §3.4.8 requires; neither invents an author, PR or Proceed. Route B is correctly excluded. The IDX-01 and IDX-RUN rehearsal (§3) shows the registration and the regenerated Index validate under the §8.3 rule. The choice between A and C and any clarification of §0.7 are the Product Owner's and are not decided here. Unreviewed fields: none for the Plan's treatment; the canon disposition itself remains unreviewed |

A proposal here is not approval. Decided entries are preserved; unreviewed fields stay unreviewed.

## 11. TypeSafe reading and surface advice for QA-100

* **Method.** The installed TypeSafe scoring skill, request v8.2; its script was run once, before this collection was saved, with session kind `execution` and label "HDE-EPIC041 QA-100 QA task execution". No Notion row was written.
* **Action sent (v8.2).** "As the executing operator, run for the first time seven already-authored and smoke-validated QA execution tasks for an approved Epic (four short check scripts and three pytest runs of 43 tests in total, each recorded through an existing harness with capture-time path proofs), then a batch indexing run of a canonical evidence writer that depends on a separately routed writer-registration change, and prepare the evidence for one pull request. A complete task list exists; no product code is changed and no live run against a provider occurs, all under closed rails; an independent evidence review follows later in a separate session."
* **Reading, as printed.** `TypeSafe v8.2: Opus 5.5 at medium.` Effort score 1.48 (confidence 0.57); rung probabilities low 0.08, medium 0.47, high 0.34, extra high 0.10, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.94, Sonnet 5.5 0.04, Haiku 5.5 0.01 (confidence 0.92). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.001, Fable 5.1 at medium 0.005, Fable 5.1 at high 0.003, Fable 5.1 at extra high 0.001, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.075, Opus 5.5 at medium 0.442, Opus 5.5 at high 0.320, Opus 5.5 at extra high 0.094, Opus 5.5 at max 0.009, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.003, Sonnet 5.5 at medium 0.019, Sonnet 5.5 at high 0.014, Sonnet 5.5 at extra high 0.004, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.005, Haiku 5.5 at high 0.003, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between high and medium. Sent 2026-11-01T11:18:02Z. Nathan picks the cell. (HTTP 200 in 0.52 s; jev-1.13.0.)
* **Picks.** Nathan has stated no model or setting for this QA-90 session or for QA-100; none is recorded.
* **Surface advice (QA-100).**
  * A top-level session or operator shell chosen by the Product Owner (PI-01), with a full-history clone of `amthorn78/glow-hdengine-v2` at `main` after this collection and its handoff are merged.
  * A Linux environment with `python3.12`, `bash`, `git` and coreutils; outbound access to the package index for setup step S-2 only.
  * All QA commands under CS-ENV (closed rails); no vendor, database, Railway, deployment or open-rails access is needed, and none should be granted for this run.
  * Write access to the execution clone's working tree for `audit/qa/hde-epic041/` and `audit/docdeltas/hde-epic041_doc_deltas.md` only.
  * For P-EL-01 only, after PI-02, PI-03 and Nathan's commit instruction: push access to one `qa/hde-epic041-live-qa-evidence` branch and one pull request; GitHub read for exact-head CI.
  * The QA-100 Notion page, read-only.

## Nonclaims

This collection is authored QA preparation. It is not QA execution, a QA verdict, evidence, an indexing or landing result, acceptance of HDE-EPIC041, Ops, deployment, release, a canon change, a PF10 addendum, PF09 or board movement, a route decision under CCR-6, a ruling under CCR-5, or closure. It edits no file outside `docs/ephemeral/` and does not alter the approved Plan. Merging it preserves the record and approves nothing (D21-C).
