---
artifact_type: QA_TASK_COLLECTION
artifact_id: HDE-CRD-0002-QA90-QA-TASK-COLLECTION
artifact_version: "1.3"
predecessor: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.2.md (TASK_READY; T16 to T20, executed by QA-100 results v1.2; unchanged)
state: TASK_READY
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
change_class: CRD
change_id: HDE-CRD-0002
author: Kronos (Claude Code CLI session on the Product Owner's workstation, local session 5c9c7c47-41bd-437a-a9ee-63879dec618b, no URL)
invocation_binding: CRD / HDE-CRD-0002 / QA-90 / approved QA_PLAN v1.3 check 21, attempt 1
prompt: QA-90 — Create Bounded QA Execution Task — 100926.1 (https://app.notion.com/p/3f44590a05eb81bea720f004a7e1a6d8; page state 2026-10-12T02:30:51.327Z; unchanged)
ecosystem_release: GCFPE-20261009.1 (100926.1)
approved_base: docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.3.md (blob 3aea6033e3c0; SHA-256 30f4a83cfa62276523c6bad5222f521cdf361eed8ebe59408387b24e8c2ec35a; immutable)
approving_review: docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.4.md (APPROVE)
qa_audit: docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md (AUDIT_COMPLETE)
selection: SEL-110-1 member check 21, re-selected by the Product Owner on 2026-10-25 ("let's just run the check 21 now, I closed the rails")
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.8.md (SHA-256 439775924392a206ceffb70952b0af1975c24d4214fc73d4ed98fcf94220e13c; unchanged)
routing: QA-100 — Execute Bounded QA Task — 100926.1, executed in this session by Product Owner direction
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-90
created_at: 2026-10-25T23:55:00Z
---

# HDE-CRD-0002 — QA Task Collection v1.3 (QA-90): check 21 under QA Plan v1.3

## 1. Result

| Field | Value |
| --- | --- |
| Result | `TASK_READY` |
| Task | T21 `qa-21-evidence-admission` (S22), attempt 1 (§3) |
| Selection | Check 21, re-selected by the Product Owner after QA-100 results v1.2 |
| Dependency | Checks 1 to 20 published (any status): met. `validate_crd_check_family` lists 20 checks on the evidence branch `qa/hde-crd-0002-t16-t20-evidence` at `2861558b` (QA-100 results v1.2 §5) |
| Pre-execution findings | None |
| Arrangement | Kronos executes in this session, by the Product Owner's direction; the evidence-only commit grant of collection v1.2 §4.8 carries to this check on the same branch |
| Normalizations | NZ-01, NZ-06 (collection v1.2 §4.10); NZ-08 (collection v1.1 §4.10, `TMPDIR` unset); NZ-30, NZ-31 (§4) |

This collection is preparation, not an execution result.

## 2. Sources

- Approved base: Plan v1.3 CHECK 21, §3.1, §5.4 to §5.6, §7 rule A (check 21's test copy and evidence checkout bullets), §8, §9.
- Aids: the QA-70 review v1.2 N-202 (check 21 naming; the block and rule A govern); QA-110 review v1.0 §6 O-2 and review v1.1 §6 O-5 (path-proof timestamps), owned by Kronos at check 21's review, recorded by the task and not judged by it.
- Contract reused unchanged: collection v1.2 §4.6 (body), §4.7 (helper, spec, call, six validators), §4.8 (commit boundary).

## 3. Task

### T21 `qa-21-evidence-admission` — The first real HDE-CRD-0002 publication validates; existing inputs still validate (Plan v1.3 check 21; S22)

- **Binding:** Plan v1.3 check 21; attempt 1; default closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev`, exported explicitly in every command (NZ-30); class 2, local/offline.
- **Environments:**
  - the evidence checkout `/tmp/hde-crd-0002-evidence` (branch `qa/hde-crd-0002-t16-t20-evidence`, holding checks 1 to 20) for step 1, validation only, interpreter `/tmp/hde-crd-0002-evid-venv/bin/python`;
  - a throwaway copy `/tmp/hde-crd-0002-qa21-copy` made with `cp -a /tmp/hde-crd-0002-evidence /tmp/hde-crd-0002-qa21-copy` for step 2, with its own venv `/tmp/hde-crd-0002-qa21-venv` (CPython 3.12, CI's full install from the copy, so `engine` resolves inside the copy). Tests never run in the evidence checkout.
  - E-L hygiene for step 2 (Plan §3.2): `HD_API_KEY`, `GEO_API_KEY`, `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `DATABASE_URL`, `GH_TOKEN`, `GITHUB_TOKEN`, `HDE_VENDOR_OVERRIDE_AUDIT_PATH`, `ENGINE_ENV` unset; `XDG_STATE_HOME=/tmp/hde-crd-0002-xdg-state` (empty); `TMPDIR` unset after recording its prior value (NZ-08).
- **Readiness** (Plan §7 rule A):
  - evidence checkout: `git rev-parse HEAD`; `git status --porcelain`; `python --version` (3.12.x); `python -c "import flask"`.
  - test copy: `git diff --stat 22a3bc040a60c75b089a629172a5d829f20d8e98 -- . ':!docs/ephemeral' ':!docs/pfcanon' ':!audit/qa/hde-crd-0002' ':!docs/evidence/INDEX.*' ':!artifacts/evidence_index.jsonl*' ':!audit/gates/topology/orientation_demo.txt*'` and the same paths through `git status --porcelain --untracked-files=all`, each empty; `python --version` (3.12.x); `python -m pytest --version`; `python -c "import engine; print(engine.__file__)"` inside the copy.
  - A failed read → `TOOLING_BLOCKED`.
- **Actions** (Plan check 21, unchanged):
  1. From the evidence checkout root:
     - `python -c "import pathlib; from tools.qa.qa_harness import HarnessConfig, validate_crd_check_family as v; print(v(HarnessConfig(crd_id='HDE-CRD-0002', repo_root=pathlib.Path.cwd())))"` and the same with `crd_id='HDE-CRD-0001'`;
     - the five read-only validators of Plan §5.4;
     - the Index read (NZ-31): `python -c "import json; ks={e['artifact_key'] for e in json.load(open('docs/evidence/INDEX.json'))}; ids=[l.split()[1] for l in open('/tmp/hde-crd-0002-qa/qa-21-ids.txt')]; need=['audit.qa.hde_crd_0002.qa_step_logs_manifest']+['audit.qa.hde_crd_0002.checks.'+i+'.primary.log' for i in ids]; print(len(need), sum(k in ks for k in need), [k for k in need if k not in ks])"`, where `/tmp/hde-crd-0002-qa/qa-21-ids.txt` lists Plan §6's twenty check IDs for checks 1 to 20, one per line as `<n> <check_id>`;
     - for each of the twenty, the manifest status compared with the primary header's `status`.
  2. From the test copy root, as four separate invocations:
     - `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_index_missing_state.py -k crd`
     - `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_skeleton.py::test_mirror_schema_and_parity`
     - `python -m pytest -q -p no:cacheprovider tests/qa/test_generic_qa_harness.py -k crd`
     - `python -m pytest -q -p no:cacheprovider tests/qa/test_epic021_acceptance_alignment.py::test_current_acceptance_inputs_are_strictly_viable`
- **PASS** (Plan check 21, unchanged):
  - HDE-CRD-0002 validates with exactly the twenty IDs of checks 1 to 20, each manifest status equal to its header;
  - HDE-CRD-0001 validates with its ten checks;
  - the five validators exit 0;
  - all twenty-one Index keys are present;
  - step 2 reports "31 passed", "1 passed", "81 passed", "1 passed" with the real root present.
- **Outcomes:** a validator or test failure caused by the published family → `FAIL_BEHAVIOR` against S22; an assembly fault → `FAIL_TOOLING`; Plan rule B otherwise.
- **Publication:** one call through collection v1.2 §4.7's helper; `captured_env` the closed rails as exported; `pf_refs` `["PF12-Canon-HDE-Schemas-and-Artifacts","PF14-Canon-HDE-Mechanics-Guide","PF19-Canon-Glow-QA-Guide"]`; `captured_at_utc` the actual finalization time, read from `date -u` at assembly. Then the six validators.
- **Final receipt** (Plan §5.6), after check 21 is published: re-run the six validators and record them, with `validate_crd_check_family` listing all twenty-one checks, in the QA-100 result. No primary claims the graph that includes itself.
- **Deliverable:** `audit/qa/hde-crd-0002/checks/qa-21-evidence-admission/primary.log`.
- **Notes the primary carries:** O-2 and O-5 (path-proof `produced_at_utc` and `mtime_utc`) as observed on the published family, recorded for Kronos and not judged; QA-100 results v1.2 G-1 (check 16 header timestamp) noted as present in the validated family.
- **Nonclaims:** the remedy's measure (1) is the evidence pull request's hosted result, read by QA-110; measure (2) belongs to the close-pack pull request.
- **Cleanup:** delete `/tmp/hde-crd-0002-qa21-copy`, `/tmp/hde-crd-0002-qa21-venv` and `/tmp/hde-crd-0002-xdg-state` after publication.

## 4. Normalizations added

| ID | Normalization | Basis |
| :- | :- | :- |
| NZ-30 | The session's base shell holds `SAFE_MODE=0` and `ALLOW_NETWORK=1`; every check 21 command exports the default closed rails explicitly, and the body records both the prior and the exported values | Plan §3.1; the Product Owner closed the rails for this check |
| NZ-31 | "Read the Index for the key" is done with one `python -c` read of `docs/evidence/INDEX.json` (a list of entries keyed by `artifact_key`) | Plan check 21 step 1 |

## 5. Nonclaims

Preparation only; no execution, publication, verdict or acceptance.

## Canon relied on

As collection v1.2; plus HDE-Schemas & Artifacts §8.17 and HDE-Mechanics Guide §1.6.3 as Plan check 21 cites them (read by the Plan's author and the QA-70 reviews; unchanged).

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-QA-90-20261025-05 |
| unit | Plan v1.3 check 21; task T21, attempt 1 |
| role/stage | Kronos, QA-90 (`TASK_READY`) |
| capture time | 2026-10-25T23:55:00Z |
| execution identity | Claude Code CLI session 5c9c7c47-41bd-437a-a9ee-63879dec618b |
| repository persistence | PENDING / NON_GATING |
