---
artifact_type: RESCOPE_PROPOSAL
artifact_id: HDE-CRD-0002-WU-PR-07-RESCOPE-PROPOSAL
artifact_version: "1.0"
status: RESCOPE_PROPOSAL_PENDING_REVIEW
approval_sentinel: "ASK OK?"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
finding: F-1 (plan v1.0 §16): the hosted closeout-validation job cannot pass its evidence-check step for any candidate
originating_stage: PR-20 — Create Detailed PR Implementation Plan — 100926.1, pre-Proceed planning (no PR_RETURN_PHASE: no Proceed, implementation workspace or code pull request exists)
product_owner_direction: "Option A, write the rescope proposal" (Nathan / Product Owner, 2026-10-20, in this session, answering plan v1.0 §16)
author: originating PR implementation author, the dedicated HDE-CRD-0002 WU-PR-07 PR engineering session, https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF (author of plan v1.0)
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002 through RS-20 (issuer of instruction v1.0; did not author this proposal)
suspended_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.0.md (PR_IMPLEMENTATION_PLAN v1.0, AWAITING_PO_PROCEED, not proceeded; blob 134685bc5503)
proposed_delta_diff: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-proposal-v1.0-prototype.diff (30 lines; 1,557 bytes; sha256 e786b30ba2719cebcf7a8808edb5423e0c21c4db17dbef37ba9ecb529cf70149; applies to 6f53552)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, approved)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, approved)
IMPLEMENTATION_AUDIT_ID: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1 → PR instruction v1.0
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (271,926 bytes; sha256 5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md §2.11, §2.12 (read in full in this session); §2.5, §2.3, §2.1 as the instruction reads them
pf10_addendum_created: none (RS-10 is not an addendum producer)
prior_rescope_proposal_or_review: none for WU-PR-07
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: RS-10 — Create Bounded Work-Unit Rescope Proposal — 100926.1 (https://app.notion.com/p/3f44590a05eb81a588c9c82aa8a2d3f2; page state as of 2026-10-12T02:29:47.386Z, fetched and read in full in this session)
repository_baseline: origin/main 6f53552
created_at: 2026-10-20T15:20:00Z
return_point: this PR-20 planning context for WU-PR-07, which writes plan v1.1 (a complete successor carrying the approved delta) and presents it at AWAITING_PO_PROCEED
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
---

# HDE-CRD-0002 WU-PR-07 — Rescope proposal v1.0

## 1. Proposal

Add one change to WU-PR-07's bounded scope: the install step of `.github/workflows/epic-closeout-validation.yml` installs the repository's runtime requirements instead of `jsonschema` alone. One assertion in the existing workflow test pins it. That is 6 added lines and 2 removed, in two files.

| Item | Path | Change |
| :- | :- | :- |
| D-1 | `.github/workflows/epic-closeout-validation.yml` (lines 67 and 68) | `- name: Install bounded validation dependency` / `run: python -m pip install 'jsonschema==4.23.0'` → `- name: Install the read-only checks' runtime requirements` / `run: python -m pip install -r requirements.txt` |
| D-2 | `tests/evidence/test_rails_ci_workflow_integration.py`, `test_manual_closeout_validation_is_isolated_read_only_and_exact_head` | four lines: the workflow has exactly one `python -m pip install` and it is `-r requirements.txt` |

The exact diff is the companion `docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-proposal-v1.0-prototype.diff`.

The Product Owner chose this route ("Option A, write the rescope proposal") over B (fix it later in a separate change) and C (change the Plan's T7). This proposal approves nothing, authorizes no implementation, rewrites no approved base, requests no Proceed and creates no PF10 addendum.

## 2. The boundary (RS-10 step 1)

- **Instruction v1.0 §7 "Exclusions"**: "**No CI change.** No new workflow, job, step or lane; the validation workflow and release-sanity stages stay as they are (ID-10)."
- **Instruction v1.0 §6** lists `.github/workflows/epic-closeout-validation.yml` as "Expected unchanged, so that a needed change is a finding under §14". §14 "Expected triggers" names "a needed change in an expected-unchanged path of §6 (the validation workflow, …)".
- **Plan v1.1 WU-PR-07 "Deliverables"** names the workflow "only where they read the schema version". The instruction resolved that condition (ID-10): the workflow reads no schema version. So the approved base authorizes no edit to it for any other reason.
- **Instruction ID-10** states the premise this finding contradicts: "The job also runs the updater's `--check`, `orientation_demo.py --check`, the hash, path, Mirror-schema and final-LF checks. ID-9 keeps them passing before HDE-CRD-0002's close pack exists."

## 3. The finding and its evidence

- **What the job is.** The manual `workflow_dispatch` validation that HDE-CRD-0002's close runs at T7 on the exact close head (Plan v1.1 WU-PR-07 (e)). Its steps are checkout, input and clean-head validation, Python 3.12, install, writer `--check`, then one step running `update_evidence_index.py --check`, `orientation_demo.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh` and `check_final_lf.sh`, then a clean-checkout assertion.
- **What fails.** It installs only `jsonschema==4.23.0`. `update_evidence_index.py --check` calls `_validate_epic038_pr02_semantics`, which imports `tools/evidence/generate_a7_transport_proofs.py`; that module imports `adapter/http_reader.py`, which imports Flask at module level.
- **Measured at 6f53552**, with CPython 3.12.3 and only `jsonschema==4.23.0` and its dependencies installed, under closed rails:
  - `update_evidence_index.py --check` exits 1 with `ModuleNotFoundError: No module named 'flask'`;
  - `orientation_demo.py --check` and `validate_evidence_paths.py` exit 0;
  - the checkout stays clean.
- **Measured on a real close state.** In the plan's T0 to T6 rehearsal (plan v1.0 §12.2), on the terminal commit C3 of both runs with the same `jsonschema`-only interpreter: the writer's `--check` exits 0 and the updater's `--check` exits 1 with the same error.
- **Never surfaced.** The GitHub Actions API lists 0 runs of `epic-closeout-validation.yml`.
- **Real input** (addendum 2.11 rule 4(b)): the hosted runner executing the repository's own workflow on `main`; no constructed input is involved.
- **Effect if unchanged.** T7 fails for HDE-CRD-0002's close and for every later close. The business case's measure ("every check mode passes … on the first attempt", disposition record §2) cannot be met.

## 4. Why this is a bounded delta, not an in-scope correction or a Specification change (step 2)

- **Not in-scope.** The edit is in a path the approved base and the instruction exclude (§2). Unchanged authority cannot make it.
- **Not a Specification change.** S21's acceptance intent is unchanged: "The writer produces a canon-conforming close report and manifest from tracked inputs for an Epic or a CRD; close-workflow run evidence has a home …; the accompanying ADR is approved". The delta makes the approved Plan's own T7 reachable; it changes no requirement or acceptance criterion. None of the Specification's eight exclusions concerns CI workflows, so all stay true. The exclusion it does change is the instruction's §7 "No CI change", for D-1 only: no workflow, job, step or lane is added, and the job keeps its step count.
- **Smallest overlay.** Two lines in one existing step, plus one existing test's pin.
- **Materiality, for the reviewer's classification.** The proposal is presented as a bounded implementation rescope, not material.
  - It touches no acceptance criterion, no data model, no external contract and no other unit's scope.
  - The workflow keeps every property `AGENTS.md` "HDE-EPIC039 current workflow posture" states: manual `workflow_dispatch`, read-only contents, exact-ref checkout, non-writing checks, clean-tree enforcement, no pull-request trigger, no credentials persistence, receipt, writeback or hosted feedback. Neither canon nor `AGENTS.md` names the job's dependency or the step's name (`git grep` of `docs/pfcanon`, `AGENTS.md`, `README.md` on `main`).
  - What widens is the set of packages the job installs: from `jsonschema` and its dependencies to `requirements.txt` (`psycopg[binary]>=3.1,<3.3`, `Flask>=2.3,<3.0`, `gunicorn>=21,<22`, `jsonschema==4.23.0`). The ordinary `test` job already installs these on every pull request. No secret is in the job's environment.
  - Budget: the RS-20 review is session 3 of the four the ceiling allows. The Product Owner accepted that cost by choosing option A.

## 5. Alternatives (with the Product Owner's choice)

| Option | Effect | Disposition |
| :- | :- | :- |
| A. This delta, in WU-PR-07 | T7 reachable; one PR; lanes already all seven | Chosen by the Product Owner; proposed |
| B. Proceed on plan v1.0; fix the workflow in a separate change before HDE-CRD-0002's T7 | A second vehicle with its own business case and route | Not chosen |
| C. Change the Plan's T7 (drop or replace the hosted dispatch) | Changes the approved terminal-state design | Not chosen |
| D. Make `update_evidence_index.py --check` importable without Flask (a lazy import, or moving `validate_catalog`/`validate_composite` out of `generate_a7_transport_proofs.py`) | Touches HDE-EPIC038 validation code outside this unit, in more lines, for the same effect | Not proposed |
| E. Install `-r requirements.txt -e .` (CI's install) | Not needed: the job runs scripts from the checkout, and the measured run in §6 used no editable install | Not proposed |

## 6. Evidence that the delta works

All in throwaway clones under the session scratchpad, closed rails, CPython 3.12.3.

| Check | Result |
| :- | :- |
| A fresh interpreter with only `pip install -r requirements.txt` (Flask 2.3.3, gunicorn 21.2.0, jsonschema 4.23.0, psycopg 3.2.13 and their dependencies; no editable install), on rehearsal run 1's terminal commit C3, running the job's seven checks with the job's own commands | all seven exit 0: writer `--check`, `update_evidence_index.py --check`, `orientation_demo.py --check`, `validate_evidence_paths.py`, `check_evidence_index_hash.sh`, `check_mirror_schema.sh`, `check_final_lf.sh`; checkout clean afterwards |
| `tests/evidence/test_rails_ci_workflow_integration.py` with D-1 and D-2 applied to the plan v1.0 prototype head | 138 passed, exit 0 |
| D-2's new assertions against the unchanged workflow | the test fails (`assert 'run: python -m pip install -r requirements.txt\n' in …`), so the pin guards the fix |
| The delta diff against 6f53552 | `git apply --check` succeeds |
| Lanes | unchanged: the classifier already selects all seven lanes for this unit, and `.github/workflows/epic-closeout-validation.yml` alone selects all seven (`tests/evidence/test_rails_ci_workflow_integration.py` line 319) |

**Stated limit.** The first hosted run of the job is still HDE-CRD-0002's T7. It cannot be dispatched before then, because it needs a tracked candidate source on the exact head. The evidence above runs the job's own commands with the job's own install, not the hosted runner.

## 7. Effects (step 3)

| Area | Effect |
| :- | :- |
| Requirements and acceptance | None changed. Acceptance (6) (lanes) and (7) (rehearsal) unchanged; the delta adds T7 reachability to the rehearsal's evidence |
| WU-PR-07 change set | +2 paths: `.github/workflows/epic-closeout-validation.yml` (+2/−2) and `tests/evidence/test_rails_ci_workflow_integration.py` (+4) |
| Instruction §6 "Expected unchanged" and §7 "No CI change" | `.github/workflows/epic-closeout-validation.yml` leaves both for exactly D-1; every other workflow, including `ci.yml`, stays expected unchanged, and no workflow, job, step or lane is added |
| Contract H-6 | becomes: unchanged inputs; the job installs `requirements.txt`; the writer stays runnable with `jsonschema==4.23.0` alone (unchanged, proven) |
| Other units | None. WU-PR-08 does not use this job; LR6-O5 (the pre-push tool's `ci.yml` pin) is unaffected because `ci.yml` is unchanged |
| Ops | None; the Product Owner's T7 dispatch is unchanged in form |
| Documentation | None owed. `AGENTS.md` and canon do not name the job's dependency |
| Tests run by PR-30 | §11 of the plan, plus `tests/evidence/test_rails_ci_workflow_integration.py` (already item 3) and the seven-check run with a `requirements.txt`-only interpreter on the rehearsal's C3 |
| Ceiling | Sessions: PR-10 (1), PR-20/PR-30 (2), this proposal's RS-20 review (3), PR-35 (4). No slack remains; a repeated stage would pass the ceiling and returns to the Product Owner |

## 8. Completed work preserved

- Plan v1.0 and its prototype diff stay as written: they are the base this delta overlays. On APPROVE, plan v1.1 is a complete successor carrying D-1 and D-2, F-1's disposition and the updated ceiling line. v1.0 is not edited.
- The prototype and every measurement in plan v1.0 §12 stay valid. The delta touches neither the writer, the updater nor the QA harness.

## 9. Return point (step 4)

- Originating stage: PR-20, pre-Proceed. No Proceed, implementation workspace or code pull request exists. The plan's pull request [amthorn78/glow-hdengine-v2#665](https://github.com/amthorn78/glow-hdengine-v2/pull/665) carries documents only.
- On APPROVE: RS-20's addendum, then this PR-20 context writes plan v1.1 and presents it at `AWAITING_PO_PROCEED`.
- On REVISION_REQUIRED: RS-30 by this author, then back to RS-20.
- On REJECT or IN_SCOPE_REPAIR: back to this PR-20 context under unchanged authority. Plan v1.0 then stands, with F-1 carried to the Product Owner.
- On SPECIFICATION_CHANGE_REQUIRED: to the Product Owner.

## 10. Risks, conflicts and unresolved facts

| Item | Treatment |
| :- | :- |
| The job installs more packages from the index | The same pinned ranges the `test` job installs; read-only permissions unchanged |
| Ceiling at four sessions with no slack | Recorded; a projected pass returns to the Product Owner before work continues |
| The hosted job is first exercised at T7 | Stated limit (§6) |
| Canon conflicts | None new; CR-1 to CR-8 carried unchanged |

## 11. TypeSafe reading for the receiving session (RS-20)

Action sent (v8.2): "Review, as the whole-change Implementation Agent in its continuing session, one new rescope proposal, not yet reviewed, for one work unit of an approved change: it asks to add a one-line dependency change in a 98-line manual validation workflow, and one four-line test assertion, to the work unit's planned scope, with the evidence measured in throwaway copies; the reviewer decides approve, revise, reject or in-scope repair and, on approval, writes one build-notes addendum; no code is implemented and no live provider call occurs; the planning session then revises its plan, and the Product Owner's Proceed, implementation and code review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.87 (confidence 0.80); rung probabilities low 0.00, medium 0.21, high 0.71, extra high 0.07, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.03, Opus 5.5 0.81, Sonnet 5.5 0.15, Haiku 5.5 0.01 (confidence 0.75). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.006, Fable 5.1 at high 0.021, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.170, Opus 5.5 at high 0.575, Opus 5.5 at extra high 0.057, Opus 5.5 at max 0.008, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.032, Sonnet 5.5 at high 0.106, Sonnet 5.5 at extra high 0.011, Sonnet 5.5 at max 0.002, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.002, Haiku 5.5 at high 0.007, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-20T15:17:25Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-20T15:17:25Z; HTTP 200 in 0.66 s; 5475 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Records.** Run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `review`, before this proposal was saved. The Notion row was not written (addendum 2.1). Nathan's pick for RS-20 is not stated; his pick for this session is not stated.

**Surface advice:** run RS-20 in the continuing whole-change IA session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt. Reproducing §6 needs:
- CPython 3.12 with package-index access, building two interpreters: one with `jsonschema==4.23.0` only, one with `-r requirements.txt` only;
- git, bash and closed rails;
- a throwaway clone with a close state. Plan v1.0 §12.2 describes the rehearsal that builds one in about 70 seconds.

No live vendor, production or database access is needed. The addendum, if any, is written under `docs/ephemeral/`.

## 12. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-07 / RS-10 / proposal 1 (F-1) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-07 (S21) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | RS-10 — Create Bounded Work-Unit Rescope Proposal — 100926.1, https://app.notion.com/p/3f44590a05eb81a588c9c82aa8a2d3f2 (page state as of 2026-10-12T02:29:47.386Z) |
| role/stage | originating PR implementation author (PR-20 context) / RS-10 |
| capture time | 2026-10-20T15:20:00Z |
| execution identity | https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF |
| inherited usage | plan v1.0 (PR-20, same session); instruction v1.0 (PR-10, session_01CCKsYD2yX5WgU3biWKb59j) |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at 6f53552.

| Topic | Sources |
| :- | :- |
| Rescope route and authorship | RS-10 — Create Bounded Work-Unit Rescope Proposal — 100926.1 (read in full); PR-20 — Create Detailed PR Implementation Plan — 100926.1, "Rescope authorship, independent review and return" and Execute step 6 |
| Materiality, budget and real inputs | PF10-HDE-Build-Notes v13.6.3 addendum 2.11 rules 3 and 4(b), read with addendum 2.12's numbering; the Product Owner disposition of 2026-10-20 §2 (the ceiling and its counting) |
| Close Gate lifecycle (why T7 must pass) | Change Process Guide (`PF06-Canon-Change-Process-Guide-v2.5.4.md`) §3.5.1 "Feedback-free terminal lifecycle" |
| Workflow posture | `AGENTS.md` "HDE-EPIC039 current workflow posture" (the workflow bullet, read whole) |
| In-flight documents | the Specification's Exclusions (read whole); instruction v1.0 §6, §7, §14, ID-10 and H-6; Plan v1.1 §7 WU-PR-07 "Deliverables" and (e); plan v1.0 §12 and §16 |

Silence: canon states no dependency rule for the closeout-validation workflow.

ASK OK?
