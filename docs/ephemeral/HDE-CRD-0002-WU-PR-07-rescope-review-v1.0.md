---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-CRD-0002-WU-PR-07-RESCOPE-REVIEW
artifact_version: "1.0"
artifact_state: COMPLETE
decision: APPROVE
approval_sentinel: "ASK OK."
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
items_decided: D-1 (approved bounded implementation delta; the closeout-validation job installs requirements.txt) and D-2 (approved; the workflow test pins it), for finding F-1
proposal_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-proposal-v1.0.md (v1.0, RESCOPE_PROPOSAL, RESCOPE_PROPOSAL_PENDING_REVIEW; blob c9fb675f6dd5; 19,818 bytes; read in full)
proposal_delta_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-proposal-v1.0-prototype.diff (blob 6844465484c7; 1,557 bytes; SHA-256 e786b30ba2719cebcf7a8808edb5423e0c21c4db17dbef37ba9ecb529cf70149, equal to the proposal's stated digest; read in full)
proposal_author: the dedicated HDE-CRD-0002 WU-PR-07 PR engineering session (PR-20 pre-Proceed planning, through RS-10), session https://claude.ai/code/session_01QyRBYtK2fkzC8aj95eAgPF
reviewer: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002, this session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j (PR-10 author of the WU-PR-07 instruction v1.0)
author_reviewer_independence: VERIFIED. Distinct sessions and roles; this IA did not author the proposal, the suspended plan or either prototype diff. Disclosure: this IA authored instruction v1.0, whose ID-10 carries the unverified premise F-1 contradicts (§3.3)
producing_prompt: RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c; page state as of 2026-10-12T02:29:57.795Z, fetched and read in full in this invocation); release GCFPE-20261009.1 / 100926.1
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
originating_stage: PR-20 pre-Proceed planning. No Proceed, implementation vehicle or code pull request exists. PR_RETURN_PHASE: not applicable
vehicle_state_relied_on: no open pull request on amthorn78/glow-hdengine-v2 (GitHub listing, state open, zero results, at about 15:37Z); origin/main a9fd343b6d638569d5cc93f50d1fc47795572c46 (tree 501440b1655a; #665 merged at 2026-10-20T15:25:30Z, carrying the proposal, its delta, plan v1.0 and the plan prototype); 0 runs of .github/workflows/epic-closeout-validation.yml (GitHub Actions API)
suspended_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.0.md (PR_IMPLEMENTATION_PLAN v1.0, AWAITING_PO_PROCEED, not proceeded; blob 134685bc5503; read in full; preserved) with companion docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.0-prototype.diff (blob 9612266486e2; SHA-256 33ee8bef36df7c29b6931eed9c0c8ce87af885ed39aa996bb2469d6b2f1199bf, equal to the plan's stated digest)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md (v1.0; blob 3df86c4c6a43; unchanged by this decision; the addendum overlays the clauses §6 names)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE by Isis; blob 0cc0276524b2)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa3)
product_owner_disposition: docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md (the business case and cost ceiling); the Product Owner's direction "Option A, write the rescope proposal" (2026-10-20, recorded by the proposal)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
immutable_approved_base: Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved) → PR instruction v1.0. None is rewritten by this decision
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md (v13.6.3; blob 41d5cfd2da6d; 271,926 bytes; SHA-256 5c26c80b3eb6b36e305ee22b998a8e5d41156c5702d659827dd9b8fdc513ff35; unchanged on main since 043fa91). Read: addenda 2.11 and 2.12 in full, 2.5 in full, and 2.6 in full (the format precedent of an RS-20 approval), all in this session; a search for the next free number finds none above 2.12
applicable_prior_addenda: 2.11 (business case, real inputs, finding disposition), read with 2.12's numbering; 2.12; 2.5; 2.3 (review chain). None is superseded by this decision
addendum_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-07-PF10-build-notes-addendum-v1.0.md (the one PF10_BUILD_NOTES_ADDENDUM this APPROVE creates; proposed number 2.13)
checkpoint_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0-checkpoint.md
handoff_ref: docs/ephemeral/HDE-CRD-0002-WU-PR-07-rescope-review-v1.0-handoff.md
created_at: 2026-10-20T15:50:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry (§10)
---

# HDE-CRD-0002 WU-PR-07 — Rescope Review v1.0

## 1. Decision and authority

**APPROVE**, one state for the one proposal. Its two items are approved together as one bounded implementation delta:
- **D-1.** In `.github/workflows/epic-closeout-validation.yml`, the install step becomes `- name: Install the read-only checks' runtime requirements` / `run: python -m pip install -r requirements.txt`, replacing `- name: Install bounded validation dependency` / `run: python -m pip install 'jsonschema==4.23.0'`.
- **D-2.** In `tests/evidence/test_rails_ci_workflow_integration.py::test_manual_closeout_validation_is_isolated_read_only_and_exact_head`, four lines pin it: exactly one `python -m pip install` in the workflow, and it is `run: python -m pip install -r requirements.txt`.

The exact text is the proposal's companion diff (§2 digest). Nothing else in WU-PR-07's scope changes.

This decision is the IA's bounded `RESCOPE_REVIEW` only. It does not decide product intent, rewrite the approved base, approve a Plan, authorize implementation, create a Proceed, merge, edit PF10 or invoke Isis. The approval is within the approved Specification's intent (§4): it changes no Epic-level commitment, acceptance criterion, protected boundary, other work unit, accepted dependency or Product Owner matter.

## 2. Vehicle state and proposal completeness: verified

- **Vehicle.** Pre-Proceed. No open pull request (listing at review time: zero) and no Proceed. #665, which carried the proposal, is merged (2026-10-20T15:25:30Z); it held documents only. `PR_RETURN_PHASE` does not apply.
- **Authorship.** The proposal's author is the originating PR implementation author (the WU-PR-07 PR-20 session, author of plan v1.0). This reviewer is independent (header).
- **Required contents.** The proposal carries the exact finding (§3), the approved Specification, the immutable base, the current PF10 and active addenda, the explicit delta (its §1 and the diff), the originating stage, owner and session, author and reviewer lineage, the preserved valid work (§8), affected requirements, dependencies, tests, Ops, documentation and downstream work (§7), evidence (§6), risks, exclusions and conflicts (§10), alternatives with the Product Owner's choice (§5) and the return point (§9). No prior decision exists for WU-PR-07.
- **Digests.** Both diffs on `main` hash to the values their documents state. The proposal's delta applies to `a9fd343` and on top of the plan prototype (`git apply --check`).

## 3. The finding, verified by this reviewer

### 3.1 Reproduction

All runs in throwaway clones under this session's scratchpad, with the job's own environment (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0 GIT_NO_LAZY_FETCH=1`, an otherwise empty environment), CPython 3.12.3, and two fresh venvs built here:
- **J**, `pip install 'jsonschema==4.23.0'` only: attrs 26.1.0, jsonschema 4.23.0, jsonschema-specifications 2025.9.1, referencing 0.37.0, rpds-py 2026.9.1, typing_extensions 4.16.0;
- **R**, `pip install -r requirements.txt` only, no editable install: adds Flask 2.3.3, gunicorn 21.2.0, psycopg and psycopg-binary 3.2.13, Werkzeug 3.1.9, Jinja2 3.1.6 and their dependencies.

The job's step "Run retained read-only evidence checks" runs six commands. Each was run with the job's command text:

| Command | J at `a9fd343` | R at `a9fd343` | R at the plan prototype head |
| :- | :- | :- | :- |
| `python tools/evidence/update_evidence_index.py --check` | **exit 1**, `ModuleNotFoundError: No module named 'flask'` | exit 0 | exit 0 |
| `python tools/evidence/orientation_demo.py --check` | exit 0 | exit 0 | exit 0 |
| `ci/checks/check_evidence_index_hash.sh` | exit 0 | exit 0 | exit 0 |
| `python tools/evidence/validate_evidence_paths.py` | exit 0 | exit 0 | exit 0 |
| `ci/checks/check_mirror_schema.sh` | exit 0 | exit 0 | exit 0 |
| `ci/checks/check_final_lf.sh` | exit 0 | exit 0 | exit 0 |
| Checkout afterwards | clean | clean | clean |

The plan prototype head is `a9fd343` plus the plan's companion diff (8 files, +1,789/−13), committed only in the scratch clone. It carries the absent-tolerant registration and the close-run reconciler, so the R column shows the new updater code imports and checks cleanly under the job's proposed install. The writer's `--check` needs a tracked candidate source; this reviewer did not rebuild the rehearsal's C3 and relies on the plan's §12.2 and the proposal's §6 for the writer and the seven-check run on C3 (§3.4).

### 3.2 Mechanism and history

- `tools/evidence/update_evidence_index.py` line 3474, `_validate_epic038_pr02_semantics`, imports `tools.evidence.generate_a7_transport_proofs`, which reaches `adapter/http_reader.py`; that module imports Flask at line 6.
- That import entered the updater in `1f0f214` (#375, 2026-07-28). The workflow was added in `a74558c` (#396, HDE-EPIC039 PR-05, 2026-08-21) with the `jsonschema`-only install. So the job's evidence-check step could not pass from the day it landed. It has never been dispatched (0 runs), which is why no record shows it.
- Real input (addendum 2.11 rule 4(b)): the hosted runner executing the repository's own workflow file on `main`. No constructed input is involved.

### 3.3 The premise in instruction v1.0 was this IA's error

Instruction v1.0 ID-10 states: "The job also runs the updater's `--check`, `orientation_demo.py --check`, the hash, path, Mirror-schema and final-LF checks. ID-9 keeps them passing before HDE-CRD-0002's close pack exists." This IA measured the updater's `--check` only with CI's full install (§5.4) and did not run the job's checks under the job's own install. The claim was unverified, and it is false. The PR-20 author found it at baseline re-check (plan v1.0 §4). The addendum overlays ID-10 and the clauses that rest on it (§6); no instruction successor is issued, because an overlay is the route for an approved delta.

### 3.4 What this reviewer did not reproduce

- The writer's `--check` on a real close state under J and R, and the seven-check run on the rehearsal's C3: taken from plan v1.0 §12.2 and §12.3 and proposal §6, not re-run here. The writer's imports are the standard library plus `jsonschema` (instruction §5.3; plan §12.3), so R, a superset of J, cannot remove an import the writer needs.
- The hosted runner itself. The first hosted run of the job is HDE-CRD-0002's T7, because a dispatch needs a tracked candidate source on the exact head (proposal §6 stated limit, accepted).

## 4. Boundary and classification

- **The base does not authorize the edit.** Plan v1.1 WU-PR-07 Deliverables names the workflow "only where they read the schema version"; the workflow reads none (instruction ID-10, confirmed). Instruction v1.0 §6 lists the workflow as expected unchanged and §7 says "No CI change … the validation workflow and release-sanity stages stay as they are". §14 names "a needed change in an expected-unchanged path of §6 (the validation workflow, …)" as an expected rescope trigger. Hence not `IN_SCOPE_REPAIR`.
- **The Specification's intent includes it.** Specification v1.1 constraint "Close-pack writer": "S21 touches the release-sanity and close-validation lanes." S21's acceptance intent ("The writer produces a canon-conforming close report and manifest from tracked inputs … the accompanying ADR is approved") is unchanged, and the Plan's own terminal-state design needs T7 to pass (Plan v1.1 WU-PR-07 (e); Change Process Guide §3.5.1 "Feedback-free terminal lifecycle": an ordinary Close Gate lifecycle "MUST be terminally reachable"). None of the Specification's Exclusions concerns this workflow's install. Hence not `SPECIFICATION_CHANGE_REQUIRED`.
- **Not material** under RS-20's definition:
  - no outcome, acceptance criterion, data model, external contract, other unit's scope or accepted dependency changes;
  - the workflow keeps every property `AGENTS.md` "HDE-EPIC039 current workflow posture" states (manual `workflow_dispatch`, read-only contents permission, exact-ref checkout, non-writing checks, clean-tree enforcement, no pull-request trigger, no credentials persistence, receipt, source writeback or hosted-result feedback). Its step count, step order and permissions are unchanged (parsed with Ruby's YAML loader on the delta head: 7 steps, `permissions: contents: read`);
  - canon names no dependency for this job (`git grep` of `docs/pfcanon/` on `main` for the workflow's name finds only HDE Phased Epics' archival HDE-EPIC039 D5 entry, which names the file);
  - budget: within the ceiling (§7).
- **Necessary.** Without it, the business-case measure ("every check mode passes … on the first attempt") fails at T7 for HDE-CRD-0002 and every later close.
- **Smallest safe scope.** Two lines in one existing step and four lines in one existing test (§5).

## 5. Alternatives

| Option | Reviewer's assessment |
| :- | :- |
| A. D-1 and D-2 in WU-PR-07 (proposed; the Product Owner's choice) | Approved. One PR, same lanes (a workflow change already selects all seven); the job's pins come from the same `requirements.txt` the `test` job installs, so there is one source of version truth |
| A′. Install `jsonschema` plus `Flask` with explicit pins | Rejected: duplicates `requirements.txt`'s pins in a second place that can drift; no measured benefit |
| B. Proceed on plan v1.0 and fix the workflow separately | Not chosen by the Product Owner; a second vehicle with its own business case |
| C. Change the Plan's T7 | Not chosen; changes the approved terminal-state design |
| D. Make the updater's `--check` importable without Flask | Rejected: changes HDE-EPIC038 validation code outside this unit, a larger diff for the same effect |
| E. Install `-r requirements.txt -e .` | Not needed: the job runs scripts from the checkout, and R (no editable install) passes every check (§3.1) |

**Security.** The job's environment holds no secret; its permissions stay `contents: read`; the checkout keeps `persist-credentials: false`. The added packages are the ones the ordinary `test` job installs on every pull request, from the same file. A candidate head's `requirements.txt` is part of the exact bytes the Product Owner dispatches against. The Codex code review covers the change on the implementation PR (addendum 2.3); declining any security finding on it goes to the Product Owner first (addendum 2.11 rule 7).

## 6. Binding conditions

1. **Files.** WU-PR-07's bounded files gain exactly two: `.github/workflows/epic-closeout-validation.yml` (D-1: the two lines of the install step, nothing else) and `tests/evidence/test_rails_ci_workflow_integration.py` (D-2: the four lines in the one named test; the file was already in instruction §6 for classifier pins). `git diff` from base to head for the workflow is exactly D-1.
2. **Overlaid clauses of instruction v1.0** (the instruction file is not edited):
   - §6 "Expected unchanged": the validation workflow leaves the list for D-1 only. `ci.yml` and every other workflow, and `tools/evidence/run_sanity_pipeline.py`, stay expected unchanged.
   - §7 "No CI change" reads: "No new workflow, job, step or lane; the release-sanity stages stay as they are; the validation workflow changes only by D-1 (its install step installs `requirements.txt`)."
   - ID-10's sentence "ID-9 keeps them passing before HDE-CRD-0002's close pack exists" is replaced by: "With D-1, the job installs `requirements.txt`, and its six read-only checks pass at the base and at the prototype head (rescope review v1.0 §3.1); ID-9 keeps them passing before HDE-CRD-0002's close pack exists." ID-10's writer constraint stays: the writer and the v2 schema keep standard library plus `jsonschema` imports.
   - Contract H-6 reads: "unchanged inputs; the job installs `requirements.txt` (D-1); the writer stays runnable with `jsonschema==4.23.0` alone".
   - §14's trigger "a needed change in an expected-unchanged path of §6 (the validation workflow, …)" no longer applies to D-1; any other change to that workflow remains a trigger.
3. **Validation PR-30 adds** to plan v1.0 §11:
   - the job's seven checks (writer `--check` and the six of §3.1) with a fresh interpreter holding only `-r requirements.txt`, on the rehearsal's terminal commit C3, each exit 0 and the checkout clean;
   - the writer's `--check` on C3 with a `jsonschema`-only interpreter, exit 0 (the retained ID-10 constraint);
   - D-2's negative control: the new assertions fail against the unchanged workflow (this reviewer: 1 failed), and the whole test file passes with D-1 and D-2 (this reviewer: 138 passed, twice; §8).
4. **Plan v1.1.** The PR-20 author writes plan v1.1 as the complete successor of plan v1.0, carrying D-1 and D-2 in its files table, sequence, validation and contracts; F-1 dispositioned as folded in by this decision; and the ceiling statement updated (§7). Plan v1.0 and its prototype diff are preserved. The companion prototype for v1.1 is plan v1.0's diff plus this delta, or one combined diff that applies to `main`.
5. **The PR description** of the implementation PR names D-1 as a change to the closeout-validation workflow approved by this review, and states that the job's first hosted run is HDE-CRD-0002's T7.
6. **Unchanged:** acceptance (1) to (7), ID-1 to ID-9 and ID-11 to ID-17, contracts H-1 to H-5, the other exclusions and nonclaims, AQ-1, the PR-30/PR-35 split, and the classifier lanes (all seven already).
7. Any further change outside the bounded files as extended here is a new finding to this IA through the rescope lane.

## 7. Ceiling

- **Ceiling** (disposition record §2): one PR; at most 4 sessions or 3 days from PR-10 to merge, excluding Product Owner waits.
- **Count.** The proposal counts this RS-20 review as session 3. This review runs in the PR-10 session (session 1), so by the disposition's counting text it is not "a further session". Plan v1.1, however, is a repeat of the PR-20 stage, which "counts toward the four". Under either reading the projected total is 4 of 4: PR-10 (1), PR-20/PR-30 (2), the PR-20 repeat or this review (3), PR-35 (4). No slack remains.
- **Days.** PR-10 started by 2026-10-20T13:14:32Z; this review is saved by 15:50Z. About 2.6 hours of 3 days are spent.
- **Within the ceiling.** The Product Owner chose option A with this cost stated (plan v1.0 §16: "Cost: the RS-20 review is session 3 of 4, leaving no slack after PR-35"). So the approval is not a change of budget needing new Product Owner direction. A projected pass (for example a second PR-35 session, or a second rescope) returns to the Product Owner before work continues (instruction ID-1).

## 8. Effects, preserved work and observations

| Area | Effect |
| :- | :- |
| Requirements, acceptance | none changed; T7 becomes reachable |
| WU-PR-07 change set | +2 paths (+6/−2 lines) |
| Other units | none. WU-PR-08 does not use this job; LR6-O5 (the pre-push tool's `ci.yml` pin) is unaffected, since `ci.yml` is unchanged |
| Ops | none; the Product Owner's T7 dispatch keeps its inputs |
| Documentation | none owed: `AGENTS.md` and canon name no dependency for the job |
| Preserved | plan v1.0, its prototype diff and every measurement in its §12; the proposal; instruction v1.0 |

**Observation (not a finding on the delta).** The first full run of `tests/evidence/test_rails_ci_workflow_integration.py` on the delta head here gave 137 passed and 1 failed: `test_fixture_backed_open_rails_tests_do_not_reach_real_network`, which runs `tests/bodygraph/test_vendor_client.py` in a subprocess with a 120 s timeout. That run took 145.7 s against 26 to 27 s for later runs. The test then passed alone, and the whole file passed 138 on both the delta head and unchanged `main`, run concurrently. The failure output was not captured (the run was piped to `tail`), so its message is not stated here. It is environmental in this container as far as the evidence shows; the delta does not touch the vendor client or that test. If it recurs on the implementation PR's hosted run, PR-35 root-causes it.

## 9. Evidence against each excluded decision

- **REJECT:** the finding is real, reproduced and blocking for the business case's measure; the delta is necessary, safe and within this IA's bounded authority.
- **REVISION_REQUIRED:** the proposal is complete (§2), its evidence reproduces (§3), and its wording is exact (a diff with a matching digest). The ceiling miscount (§7) does not change the outcome or the cost the Product Owner accepted.
- **SPECIFICATION_CHANGE_REQUIRED:** the Specification already names the close-validation lane as touched by S21, and no acceptance intent or exclusion changes (§4).
- **IN_SCOPE_REPAIR:** the Plan's deliverable condition and the instruction's §6, §7 and §14 exclude the edit (§4).

## 10. Canon-conflict register

`CANON_CONFLICT_REGISTER` is carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 (CANON_RECONCILIATION) | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED, alternative (a) | this IA through RS-20 | WU-PR-03 rescope review v1.0 §12; addendum 2.6 |
| CR-7, CR-8 | APPROVED, alternative (a) each | Product Owner direction of 2026-10-14 | decision record §6; addendum 2.7 |

No new conflict: canon is silent on this job's dependency, and the delta keeps every property `AGENTS.md` states for it.

## 11. Return

- **Next:** PR-20 — Create Detailed PR Implementation Plan — 100926.1, in the WU-PR-07 PR engineering session (the proposal's author), to write plan v1.1 under the approved base, addenda 2.11, 2.12, 2.5, 2.3 and the new 2.13 overlay, ending at `AWAITING_PO_PROCEED`. The handoff file holds the continuation.
- **Prerequisite:** the pull request carrying this review, the addendum, the checkpoint and the handoff is merged.
- **Not routed here:** AQ-1 (the Product Owner's, before the implementation PR merges); the Proceed (the Product Owner's, against plan v1.1).

## 12. TypeSafe reading and surface advice for the receiving session (PR-20, WU-PR-07 plan v1.1)

Action sent (v8.2): "Revise, in the same planning session that wrote it, one detailed PR implementation plan already written once and not yet proceeded, into a complete successor version that carries one approved rescope: a two-line dependency change in a 98-line manual validation workflow and a four-line test assertion, added to an already prototyped change of about 1,800 lines across eight files; the prototype, its tests and its end-to-end rehearsal exist and stay valid, so the session re-checks the baseline, applies and checks the small delta in a throwaway copy, and updates the plan's scope, validation, ceiling and findings sections; no live provider call occurs, and a Product Owner Proceed, implementation, code review and lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.77 (confidence 0.77); rung probabilities low 0.00, medium 0.29, high 0.65, extra high 0.06, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.92, Sonnet 5.5 0.08, Haiku 5.5 0.00 (confidence 0.89). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.267, Opus 5.5 at high 0.598, Opus 5.5 at extra high 0.055, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.023, Sonnet 5.5 at high 0.052, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-20T15:36:28Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-20T15:36:28Z; HTTP 200 in 0.59 s; 5490 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag printed.
- **Records.** Run once with the installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json`, session kind `planning`, before this review was saved. The Notion row was not written (addendum 2.1). Nathan's pick for the receiving session is not stated; his pick for this RS-20 session is not stated (the proposal §11 holds its reading).

**Surface advice:** the receiving work continues in the WU-PR-07 PR engineering session, a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt. Re-checking the delta needs CPython 3.12 with package-index access to build a `requirements.txt`-only interpreter and a `jsonschema`-only one, git, bash and closed rails, in throwaway clones. The rehearsal that builds C3 took about 70 s per run in that session. No live vendor, production or database access is needed.

## 13. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-07 / RS-20 / review 1 (F-1) |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-07 (S21) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | RS-20 — Review Bounded Work-Unit Rescope — 100926.1, https://app.notion.com/p/3f44590a05eb81be9566cd6397c9424c (page state as of 2026-10-12T02:29:57.795Z) |
| role/stage | continuing whole-change IA / RS-20 |
| capture time | 2026-10-20T15:50:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| inherited usage | proposal v1.0 (RS-10) and plan v1.0 (PR-20), session_01QyRBYtK2fkzC8aj95eAgPF; instruction v1.0 (PR-10), this session |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`; pending, non-gating) |

## Canon relied on

Read on `main` at `a9fd343` (`docs/pfcanon/` unchanged since `043fa91`).

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

| Decision topic | Sources and sections |
| :- | :- |
| Rescope route, authorship, decision matrix, materiality, addendum contract | RS-20 — Review Bounded Work-Unit Rescope — 100926.1 (read in full); PR-20 — Create Detailed PR Implementation Plan — 100926.1 ("Rescope authorship, independent review and return", read for the return point) |
| Authority; in-flight documents | HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2, as read for instruction v1.0 in this session |
| Addendum format and precedence | Change Process Guide (`docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`) §0.1A (read in full here); Plan Templates (`docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md`) "Canon precedence for template use" (read in full here); PF10 addendum 2.6 (the format precedent) |
| Why T7 must pass (§4) | Change Process Guide §3.5.1 "Requirement", "Feedback-free terminal lifecycle" (read in full for instruction v1.0 in this session) |
| Business case, ceiling, real inputs, finding disposition (§3.2, §5, §7) | PF10-HDE-Build-Notes v13.6.3 addendum 2.11 rules 1, 3, 4(b) and 7, with 2.12's numbering (read in full in this session); the Product Owner disposition §2 (ceiling and counting) |
| Carried items | PF10 addendum 2.5 (LR-O2; OBS-17) and 2.12 (LR6-O5) |
| Workflow posture (§4) | `AGENTS.md` "HDE-EPIC039 current workflow posture"; HDE Phased Epics (`docs/pfcanon/PF20-Reference-HDE-Phased-Epicsv1.9.6.md`) HDE-EPIC039 D5 (the workflow's origin, #396) |
| In-flight documents | Specification v1.1: S21, constraint "Close-pack writer", Exclusions; Plan v1.1 §7 WU-PR-07 Deliverables and (e); instruction v1.0 §6, §7, §8 H-6, §14 and ID-10; plan v1.0 in full; proposal v1.0 in full |

Silence: canon names no dependency rule for the closeout-validation workflow (search of `docs/pfcanon/` for the workflow's name and for its install step); the approved delta governs it.
