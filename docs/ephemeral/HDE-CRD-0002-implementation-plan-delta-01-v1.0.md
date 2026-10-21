---
artifact_type: MATERIAL_PLAN_DELTA
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-DELTA-01
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: PLAN_DELTA_PENDING
AUTHORING_MODE: APPROVED_BASE_PLAN_DELTA_AUTHORING
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
predecessor: none (first standalone delta authoring)
immutable_base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4), approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b). Not edited
redline_applied: docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md (IA-30 PLAN_DELTA_REDLINE, items P-1 to P-17; blob c4bfa53b6d45065946678bca05fc8ee1f7f9ba84; landed by #679). History: v1.0 of the assessment (blob 52c204abd092afe1d125f869e0822b42cc94117b; #677) and the IA-40 return docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md (REDLINE_INCOMPLETE on P-7; blob eba413f352561c8afa5f6d153398909b24a0216c; #678)
material_change: approved Specification delta 01, docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (blob 9408d6ed091bcba3d751fcb17ae392a1ceca8bbb), approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md (CF-C-30 DELTA_APPROVE, Thoth, 2026-10-21T18:36:00Z; blob 5a6cecc86f604a17aaa3e6c89b17183d2d0f9ffa)
overlays: (1) the Specification delta 01 addendum, record docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md (blob 64325e32376349394df0989602fca928bdcfb8da; numbered 2.18 in the record), which the Product Owner has added to PF10 (2026-10-21) and which is in force; cited here by title and record; (2) HDE Build Notes addendum 2.18 as published in PF10 v13.7.1, "Requirements and work units carry no cost ceiling; work continues until it is done" (record docs/ephemeral/HDE-CRD-0002-PF10-build-notes-addendum-no-cost-ceiling-v1.0.md, blob d2932079fd3da8dfb4e6f67b22178fa157fd2ae3, drafted there as 2.19; #680). Overlays carried to the WU-PR-08 instruction: addenda 2.7, 2.8, 2.9 and 2.10 at their WU-PR-08 items (see P-7)
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (Product Owner OPTION 1, 2026-10-21; blob efc220928f7c313ba5ebabb49b975b624dfbafc2). Its "Cost ceiling" row is not in force (no-ceiling addendum)
application_report: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.0-application-report.md
author: the whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N), continuing the Plan author lineage (sessions https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah and https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j)
reviewer: Isis, continuing Lead Developer and whole-change Implementation Plan reviewer (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_head_read: origin/main 7b763db
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md (blob afce167947cd44e84de10ecc2aa18fac142482de; sha256 eab61385a819c859e1cf2743a204b70813feef23c902f647b3a5d7141454114d)
created_at: 2026-10-21T20:24:34Z
return_point: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), MATERIAL_PLAN_DELTA_REVIEW, Isis
---

# HDE-CRD-0002 — Implementation Plan delta 01, v1.0 (pending)

## 1. What this delta is

This is a standalone overlay on the approved Implementation Plan v1.1. The current Plan is v1.1 with this overlay applied, once it is approved. The overlay changes only the passages in §3 below, and the Plan file is not edited.

It applies IA-30's redline P-1 to P-17 (change assessment v1.1 §3), under:
- the no-cost-ceiling addendum: no unit carries a cost ceiling, so the redline's ceiling clauses are not applied;
- the Specification delta 01 addendum.

The application, item by item, is in the application report.

**State: `PLAN_DELTA_PENDING`.** This delta is unapproved. It authorizes no PR Instruction, PR, Ops, QA, acceptance or closure, and creates no HDE Build Notes addendum.

**What it changes, in short:**
- S01 and its packaging work leave the Plan.
- No release version cut is made. The release stays at `1.3.0`, and a unit that changes a member refreshes the manifest at that version.
- WU-PR-08 becomes S16 and S17, plus one classifier registration so that `.env.example` can pass CI. Its PR runs all seven lanes.
- WU-OPS-01 verifies the candidate's `release_id` at `1.3.0` and records the live start command.
- WU-DOC-01 drops the dedicated-environment install note and states `1.3.0`.

## 2. Addendum numbering used here

PF10 v13.7.1 numbers the no-cost-ceiling addendum 2.18. The Specification delta 01 addendum's record also calls itself 2.18. The Product Owner has since added it to PF10, and this delta does not state its PF10 number. To keep every citation unambiguous, this delta names them as follows:

- **"the no-ceiling addendum"**: HDE Build Notes addendum 2.18 as published, "Requirements and work units carry no cost ceiling; work continues until it is done".
- **"the Specification delta 01 addendum"**: the addendum recorded in `docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`, "HDE-CRD-0002: Specification delta 01 is approved — requirement S01 is removed and the release keeps its version, with a same-version manifest refresh for any member change".

Where a redline item cites "addendum 2.18" for the Specification delta, the overlay text below names the Specification delta 01 addendum instead. The meaning is unchanged (application report, A-2).

## 3. Overlay text

Each row gives the Plan v1.1 anchor and the text in force under this delta. Unit, interface and risk IDs are not renumbered.

### P-1 — §2 "Lineage and sources": rows added after "Conflict register"

| Item | Exact identity |
| :---- | :---- |
| Specification delta 01 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, approved by `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`; the Specification delta 01 addendum (`docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`) |
| Product Owner scope decision | `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` |
| This change assessment | `docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md` (superseding v1.0 after IA-40's return, `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md`) |

### P-2 — §3 opening paragraph

The clause "member-changing work lands before the version-bumping release cut (S01 unit last among code units)" reads:

> each member-changing unit carries its own same-version manifest refresh (no release version cut)

The rest of the paragraph is unchanged.

### P-3 — §3 "Release-identity spine"

The sentences from "The single new release" to the end of the bullet read:

> No release version cut is made: the release stays at `1.3.0` and the admission constants do not change (Specification delta 01, C-5 and C-7). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member).

The bullet's first sentence is unchanged.

### P-4 — §4 invariant 3

The clause "admission constants change only in WU-PR-08" reads:

> the admission constants (`ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC`, `ADMITTED_RELEASE_ROSTER`) do not change in this change

The rest of the invariant is unchanged.

### P-5 — §5 IF-8 row

| ID | Interface | Shape |
| :---- | :---- | :---- |
| IF-8 | Wheel layout | Removed with S01 (Specification delta 01); not delivered |

### P-6 — §6 traceability rows

| Requirement | Unit | Phase block | Live QA class |
| :---- | :---- | :---- | :---- |
| S01 | removed (Specification delta 01, C-1 and C-6); not delivered | — | — |
| Release re-cut | same-version refresh in each member-changing unit; no version cut (Specification delta 01) | — | — |

### P-7 — §7 WU-PR-08 block (replaced from its heading through "Nonclaims")

#### WU-PR-08 — Environment template and operator documentation (PR; Coagulation)

- **Purpose.** S16 and S17 only: add the missing environment-template key, and correct the operator document's readiness and port statements. The classifier registration exists only so that S16's file change can pass CI. It adds no requirement.
- **Bounded scope.** S16, S17, and one classifier registration that makes `.env.example` a classified change surface. Nothing else.
- **Inputs.**
  - Audit §6 S16 and S17.
  - The items HDE Build Notes carries to the WU-PR-08 instruction:
    - the loopback bind statements (addenda 2.7, 2.8 and 2.9);
    - OBS-P4-5, O-19 and the production route exposure, contract F-3 (addenda 2.9 and 2.10).
  - **Not carried:** addendum 2.10's "cuts `1.4.0` from `release_id` `77204764…` (contract F-1)". The Specification delta 01 addendum approves no version cut and governs that overlapping scope (HDE Build Notes front matter §9, step 8: "apply only the highest-numbered applicable addendum to the overlapping scope"; noted in the IA-40 return record §4).
- **Deliverables.**
  1. `.env.example`: a `GEO_API_KEY` entry only.
  2. `docs/ADAPTER_009.md`: the readiness rules and port statements.
  3. `ci/checks/classify_ci_changes.py`: one registration that classifies `.env.example`. The author states its form at PR-20, choosing the smallest repository-grounded registration among the classifier's existing mechanisms.
  4. The registration's owner or pin test, only if one enumerates the registry the registration changes. The author states which, read from the repository.
  - **Repository facts for PR-20** (observed on `main` `7b763db`, identical to `a78b350` for these files; PR-20 re-reads them at its head and chooses):
    - The classifier's existing mechanism for a file that no code reads is the `_DOCUMENT_PATHS` set (`LICENSE`, `AcceptanceMap.md`, `AGENTS.md`, `ARCHITECTURE.md`, `CHANGELOG.md`, `README.md`). A path in it classifies as `documentation_only` with no lanes.
    - Nothing on `main` reads `.env.example`: no `.py`, `.sh`, `.yml`, `.toml`, `.json`, `requirements*.txt` or `Procfile` reference, and no dotenv loader. The one test hit is a literal in `tests/qa/test_generate_epic_close_pack.py` line 4338 (S16's acceptance text in a fixture). So `documentation_only` would not hide an affected change (Plan Templates, "CI lane classification and automated budget-control discipline").
    - No test enumerates `_DOCUMENT_PATHS` (searched `tests/`, `ci/` and `tools/`). The classifier's scenario table in `tests/evidence/test_rails_ci_workflow_integration.py` (`test_change_classifier_selects_expected_execution_scenarios`) pins example paths, not the set.
    - The other mechanism that fits is `_WORKFLOW_CONTROL_PATH_LANES`, a path-to-lanes map. It would select lanes for every future change to the template.
- **Dependencies and order.**
  - Eighth code unit, after WU-PR-07; the order is kept.
  - No release member changes, so there is no manifest refresh. `ci/checks/classify_ci_changes.py`, `.env.example` and `docs/ADAPTER_009.md` are not members of release `1.3.0` (45 members, `release_id` `77204764…`).
  - A change to the classifier is a full-validation path, so the PR runs all seven lanes.
  - **Lane selection, read from the classifier.** `ci/checks/classify_ci_changes.py` is in `_FULL_VALIDATION_PATHS`. In a throwaway clone of `a78b350`, one commit changed the three files: it registered `.env.example` in `_DOCUMENT_PATHS`, added `GEO_API_KEY` and corrected one port line. The classifier, called as `ci.yml` calls it with full SHAs, then exited 0 with `reason=selected_lanes` and all seven lanes (product, compat, db, rails, evidence, qa, release), and wrote 166 changed-test targets. With the registration, `.env.example` alone classified as `documentation_only`.
- **Acceptance and verification.**
  1. `.env.example` has a `GEO_API_KEY` entry and nothing else in it changed.
  2. The readiness section describes `/internal/readyz` as implemented and names the app that serves it. The port statements match the runner and Procfile bindings.
  3. Admission at the PR head reports `1.3.0`, 45 members and the base head's `release_id`, unchanged.
  4. At the PR head, the classifier run on `.env.example` alone returns a classification and no `CI_CHANGE_SURFACE_UNCLASSIFIED`.
  5. All seven lanes are green on the exact PR head, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
- **Evidence obligations.** PR result record.
- **Risks and recovery.**
  - *Misclassification.* If a later change made code read `.env.example`, a `documentation_only` registration would skip its lanes. PR-20 re-checks the readers at its head, and the registration's form records why it is safe.
  - *The full run exposes failures that are not this unit's.* A classifier change runs every lane. A failure that is also red on the base is handled under PR-35's base-red rule, not by widening this unit.
  - *Document drift.* S17's statements are checked against `adapter/wsgi.py`, `adapter/factory.py`, `Procfile` and the canonical runner at the PR head. PR-40 checks the measure on the merged head.
  - R-2 and R-6 no longer apply. Recovery is as the common §7 terms state.
- **Nonclaims.** No release cut, no CI workflow change, no QA verdict.
- **Business case.** Carried by reference for PR-10 under addendum 2.11 rule 3, as the no-ceiling addendum narrows it: beneficiary, evidence, benefit and measure from `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` §2. No cost ceiling applies, and the decision record's "Cost ceiling" row is not in force (no-ceiling addendum, rule 1 and "Epic, task, and status effects"). The corrected fact the change assessment §5 records stands: the unit changes the classifier, so its PR runs all seven lanes.

### P-8 — §7 WU-DOC-01, Bounded scope

The Bounded scope bullet reads:

> `README.md` (pre-push check usage; close-pack writer capability; test guidance); `CHANGELOG.md`; `AGENTS.md` operative passages (HDE-EPIC039 workflow posture → the extended close-pack capability and schema v2; HDE-EPIC040 current posture → release `1.3.0`, refreshed in place with no version cut, and its current `release_id`; the CI-exempt paths note verified against the workflow; pytest guidance); `docs/EVIDENCE_INDEX.md` (CRD admission, Mirror labels, close-run family); `docs/CLI_commands.md` final pass; `docs/server/reader_v1.md` (not-found limitation line removed). No canon, no generated evidence, no governed artifact by hand.

The rest of the block is unchanged.

### P-9 — §7 WU-OPS-01: Intent, Success criteria, Constraints

- **Intent.**

  > The Railway HD Engine production service runs the exact accepted candidate (the `main` head after WU-PR-08 and WU-DOC-01 merge) so that the QA Plan's bounded open-rails live steps (S02, S10 refusal in the deployed target; S14's live vendor call from the operator shell against the production rails) exercise that candidate. The deployment facts the QA Plan needs, and the live start command (Specification delta 01's stated limit; the Specification delta 01 addendum, "Unresolved obligations and owners"), are recorded presence-only.

- **Success criteria.**

  > `GET /internal/version` on the base URL reports the candidate's identity (the candidate's `release_id` at version `1.3.0`); the recorded deployment trigger, build command and start command; the presence-only binding probe; all captured under `audit/ops/hde-crd-0002/wu-ops-01/` with path proofs (Plan Templates §3 evidence posture; lower-case directory names).

- **Constraints.**

  > No production configuration change by this task; if the discovered build command differs from the checked-in declarations, record it and stop. Rollback intent: redeploy the previously deployed commit.
  >
  > **Live start command.** The task records the start command as the Railway service settings show it. It records the command line itself, never a binding value: any embedded value is recorded as REDACTED. It compares the command with `Procfile` (`web: /app/.venv/bin/python -m gunicorn 'adapter.factory:create_app()' …`). Where it does not run the engine from the checkout as `Procfile` does, the task changes no production configuration and records the difference as a Glow Infrastructure doc-delta candidate. Then:
  > - If `GET /internal/version` answers after placement with the candidate's `release_id`, the task records that and continues. The engine evidently resolves its release from the checkout.
  > - If it does not answer because admission refused at start (`MISSING_FILE`, the stated limit of Specification delta 01 C-6), the task records the refusal from the deployment log. It then redeploys the previously deployed commit under the rollback intent and stops. The Product Owner decides, because S01 is removed and not delivered.

The other WU-OPS-01 fields are unchanged.

### P-10 — §9 item 2

The opening reads "The acceptance intents S02 to S22 (S01 removed by Specification delta 01) as the Specification states them, …". "the wheel-install admission test, " is deleted. The rest of the item is unchanged.

### P-11 — §9 item 3

The clause "S01's class-2 step or its recorded exemption basis from WU-OPS-01's discovery; " is deleted. The rest of the item is unchanged.

### P-12 — §10 heading and step 2

- **Heading:** "10. Release re-cut procedure (binding method for any unit that changes a release member: a same-version refresh)".
- **Step 2:** the sentence beginning "`<V>`/`<T>` are the current constants for a refresh" reads: "`<V>`/`<T>` are the current constants (`1.3.0` / `2026-08-24T18:04:49Z`); no version bump is made (Specification delta 01)."

The other steps are unchanged.

### P-13 — §11 R-2, R-6 and R-8

| ID | Risk | Unit | Treatment |
| :---- | :---- | :---- | :---- |
| R-2 | Convergence run out of order or repeated with member changes in between. | WU-PR-03/04/05 | §10 restart rules; second-run byte stability. |
| R-6 | Removed with S01 (Specification delta 01). | — | — |
| R-8 | Three or four same-version manifest refreshes multiply convergence effort. | WU-PR-03/04/05 | Accepted: admission's byte binding leaves no alternative without rewriting the loader (a member); units are ordered to minimize refreshes. |

### P-14 — §12 Exclusions

The clause "no release re-cut beyond the refreshes admission forces and the single `1.4.0` cut" reads:

> no release version cut: the release stays at `1.3.0`, with same-version refreshes only (Specification delta 01, C-5); S01 removed and not delivered (C-6)

The rest of §12 is unchanged.

### P-15 — §13, the paragraph "No engineering decision remains open at Plan level; …"

This sentence is appended to the paragraph: "Specification delta 01 withdraws EC-11 (S01 packaging); EC-12 applies only as same-version refreshes."

### P-16 — §14 Migration and rollback

The clause "; a reverted WU-PR-08 restores the `1.3.0` constants and manifest and re-converges" is deleted.

### P-17 — Header and state

The front matter of this delta records:
- the approved base plus overlays: the immutable base, this assessment, Specification delta 01, the Specification delta 01 addendum and the no-ceiling addendum;
- the state, `PLAN_DELTA_PENDING`.

Plan v1.1's own header, §16 and §17 are not edited. §8 below takes the place of a new recovery envelope.

### Unchanged, with the reason (assessment §3.1)

- **Executed history.** Completed units WU-PR-01 to WU-PR-07, with their blocks and R-5. That includes WU-PR-05's "precede the version bump" and R-5's "Fixes precede the version bump".
- **Other sections:**
  - §1 and §8;
  - §9 items 1, 4 and 5;
  - §10 steps 1 and 3 to 12;
  - §15;
  - every interface other than IF-8;
  - every risk other than R-2, R-6 and R-8;
  - AQ-1.
- **Unit order:** WU-PR-08 → WU-DOC-01 → WU-OPS-01 → QA-10.
- **The Implementation Audit.** It is not revised. Its S01, EC-11 and §7.3 version-bump text are superseded for planning by Specification delta 01 and this delta (HDE Governance §9.1.2).

## 4. Affected requirements, dependencies, tests, Ops, documentation and downstream work

| Area | Effect |
| :- | :- |
| Requirements | S01 leaves the Plan; it is not delivered. S16 and S17 stay in WU-PR-08. No other requirement's unit, scope or acceptance changes |
| Dependencies | WU-PR-08 no longer waits on members being final, but keeps its place after WU-PR-07. WU-DOC-01 and WU-OPS-01 still follow it |
| Tests | No wheel-install test, and no pinned-identity tests rewritten to `1.4.0`. WU-PR-08 adds no test unless PR-20 finds a test that enumerates the registry it changes; none does on `main`. Its PR runs all seven lanes, with 166 changed-test targets in the rehearsal |
| CI | One registration in `ci/checks/classify_ci_changes.py`. No workflow change |
| Ops | WU-OPS-01 verifies the candidate's `release_id` at `1.3.0`, records the trigger, build command and start command, and handles a start command that differs from `Procfile` as P-9 states |
| Documentation | WU-DOC-01 drops the dedicated-environment install note and states `1.3.0` with its current `release_id`. S17's corrections to `docs/ADAPTER_009.md` ride in WU-PR-08 |
| Release identity | Unchanged: version `1.3.0`, build time `2026-08-24T18:04:49Z`, 45 members. `release_id` moves only by a same-version refresh in a unit that changes a member, and no remaining unit is planned to |
| QA | The QA Plan needs no Live QA step or exemption for S01 (Specification delta 01, C-12). §9 items 2 and 3 no longer name it |
| Downstream | WU-PR-08's PR-10 follows this delta once it is approved. It carries the decision record's business case without a ceiling, and the items in P-7's Inputs. WU-PR-08's PR-40 records whether the measure was met (no-ceiling addendum, rule 5) |

## 5. Exclusions

- Nothing beyond P-1 to P-17. No unit is added, removed or reordered, no interface is added, and no risk is added other than WU-PR-08's own, which the redline left to the author.
- No release version cut and no admission-constant change.
- No CI workflow change. The classifier change is the one registration P-7 bounds.
- No edit to Plan v1.1, the Implementation Audit, the Specification, the decision record or any HDE Build Notes addendum.
- No HDE Build Notes addendum is created by this delta. The approval addendum is IA-30's, at DELTA_APPROVE.
- No cost ceiling for any unit (no-ceiling addendum).

## 6. Conflicts

| # | Conflict | Resolution |
| :- | :- | :- |
| K-1 | Addendum 2.10 carries "WU-PR-08 (S17) cuts `1.4.0` … (contract F-1)". The Specification delta 01 addendum approves no version cut | Their scopes overlap on the version cut. HDE Build Notes front matter §9 step 8 gives the overlap to the higher-numbered addendum. The Specification delta 01 addendum is later than 2.10 whatever number it takes, and Specification delta 01 is the approved in-flight Specification. Not carried (P-7) |
| K-2 | Addendum 2.6, "Affected surfaces": "WU-PR-08's version bump changes an engine-core source, so it regenerates the purity report" | Same overlap and resolution as K-1. With no version bump, WU-PR-08 changes no engine-core source and regenerates no purity report. This is a consequence statement in 2.6, not an item carried to the instruction, so the block does not name it |
| K-3 | Assessment v1.1 §1, P-7, §5, §6 and §7, and the decision record's "Cost ceiling" row, carry a ceiling for WU-PR-08 | The no-ceiling addendum governs. It names each of these passages as not in force. The ceiling clauses are not applied (application report, A-1) |
| K-4 | Two addenda have carried the number 2.18: PF10 v13.7.1's 2.18 is the no-ceiling addendum, and the Specification delta 01 addendum's record also calls itself 2.18. The published no-ceiling text says it "follows addendum 2.18, which is pending publication", and supersedes the Specification delta 01 addendum's sentence "Its business case and cost ceiling are in the Product Owner decision record §2 (addendum 2.11 rule 1)" | This delta cites both by title and record (§2). Applying no ceiling does not depend on their numbers: the no-ceiling addendum names that sentence and supersedes it, and the Product Owner set the no-ceiling rule after approving Specification delta 01 (19:07 against 18:36 UTC). If PF10 numbers the Specification delta 01 addendum above 2.18, a mechanical reading of front matter §9 step 8 would hand that sentence the overlapping scope. This delta does not read it that way, because the later and more specific rule names the sentence. Numbering belongs to the Product Owner |
| K-5 | Plan Templates, "CI lane classification and automated budget-control discipline": "a plan or review MUST NOT invent … a change-detection mechanism". The handoff asked that the registration's form be stated from the repository | P-7 keeps the form as the author's statement at PR-20. The delta records only repository facts: the existing mechanisms and who reads `.env.example`. It invents no mechanism, and PR-20 chooses |

The canon-conflict register CR-1 to CR-3 is carried unchanged (Plan v1.1 §15).

## 7. Evidence

Measured on `main` (`a78b350` for the rehearsal; `7b763db` for the reads, where the measured files are unchanged), closed rails, CPython 3.12.3:

- **Unregistered.** `classify_paths(['.env.example'])` raises `CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`. `tools/ci/prepush_check.py --path ci/checks/classify_ci_changes.py --path .env.example --path docs/ADAPTER_009.md lanes membership` reports `lanes: FAILURE CI_CHANGE_CLASSIFIER_ERROR:CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`. Its membership report: release `1.3.0`, roster 45, `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`, all three paths not members. The tool reported the repository unchanged.
- **Registered (rehearsal, throwaway clone).** The classifier exits 0 with `reason=selected_lanes` and all seven lanes, and writes 166 changed-test targets. `.env.example` alone is `documentation_only`.
- **Classifier tests in the rehearsal.** `tests/evidence/test_rails_ci_workflow_integration.py`: 136 passed and 2 failed with the registration. The same 2 fail identically on the unchanged base in the same container, so they are environmental and not caused by the registration:
  - `test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned`: a `pytest --collect-only` subprocess exits 2;
  - `test_open_rails_producer_check_mode_has_no_repo_residue`: `OPEN_RAILS_ABBA_PREDICATES_FAILED`.

  This is not CI's result.
- **Readers of `.env.example`:** none outside the fixture literal (P-7).
- **S16 and S17 evidence still present:**
  - `.env.example` holds only `HD_API_BASE_URL`, `HD_API_KEY` and `HD_API_SECRET`.
  - `engine/providers/vendor_http_hdapi.py` requires `GEO_API_KEY`.
  - `docs/ADAPTER_009.md` "Readiness rules" describes a resolver, catalog and smoke check with a typed 503, while `adapter/wsgi.py` returns `{"ok": true, "schema": "v1"}` with 200 and `adapter/factory.py` registers no `/internal/readyz`.
  - The document gives `127.0.0.1:5000` twice, and `Procfile` binds `$PORT`.

## 8. Unresolved items, owners and return point

| Item | Owner |
| :- | :- |
| Review of this delta | Isis, IA-30 `MATERIAL_PLAN_DELTA_REVIEW` |
| The HDE Build Notes addendum for the approved delta | Isis at DELTA_APPROVE; publication by the Product Owner |
| The registration's form | WU-PR-08's PR-20 (P-7) |
| Business cases for WU-DOC-01 and WU-OPS-01: beneficiary, evidence, benefit and measure, due before DOC-10 and OPS-10 | Product Owner (no-ceiling addendum, "Epic, task, and status effects"). Not part of this delta |
| The live Railway start command, a stated limit and not a blocker | WU-OPS-01; Product Owner |
| The PF10 number of the Specification delta 01 addendum, which this delta does not depend on (K-4) | Product Owner |

**Return point.** IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), `MATERIAL_PLAN_DELTA_REVIEW`, for Isis. On `DELTA_APPROVE`, the continuation is PR-10 — Create PR Work-Unit Instructions — 100926.1, for WU-PR-08. On `DELTA_DENY`, the delta returns to this Implementation Agent through IA-40.

## 9. TypeSafe reading for the receiving session (IA-30 delta review)

Action sent (v8.2): "Review, as the same independent reviewer who wrote its seventeen-item redline, a new 33 KB standalone pending material delta against an approved 76 KB Implementation Plan, with its item-by-item application report as the checklist: confirm each item was applied once at its unique anchor and nothing else changed, and judge the author-stated parts, namely one small work unit's block rewritten around two kept requirements plus one CI classifier registration whose existing-mechanism options and lane selection are recorded from the repository, an Ops unit's handling of a start command that differs from the checked-in one, the unit's risks, and five recorded conflicts including two addenda sharing one number; then approve with one Build Notes addendum and a continuation handoff, or return redlines. No code is written and no live run occurs; per-PR planning, a Product Owner Proceed, CI and a lineage review follow."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.38 (confidence 0.69); rung probabilities low 0.00, medium 0.04, high 0.55, extra high 0.39, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.97, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.96). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.011, Fable 5.1 at extra high 0.008, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.039, Opus 5.5 at high 0.533, Opus 5.5 at extra high 0.378, Opus 5.5 at max 0.019, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.006, Sonnet 5.5 at extra high 0.004, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: boundary between extra high and high. Sent 2026-10-21T20:22:56Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T20:22:56Z; HTTP 200 in 0.76 s; 5520 input and 71 output tokens; jev-1.13.0. Session kind "review". Rung by rule: high (nearest to the score, halves up). Model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). Flags: boundary between extra high and high.
- **One send**, taken before this delta and its application report were saved, and recorded identically in both. No Notion row was written (IA-40 handoff rule).
- **Nathan's pick for IA-30 (delta review):** not stated.
- **Nathan's pick for this IA-40 session:** not stated. Its reading is in the change assessment v1.1 §8: Opus 5.5 at high, score 1.99.

**Surface advice:** run IA-30 `MATERIAL_PLAN_DELTA_REVIEW` as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the continuing Isis reviewer lineage.
- **Reads from `main`:**
  - this delta and its application report;
  - Plan v1.1 and its review v1.1;
  - the change assessment v1.1 and the IA-40 return record;
  - Specification delta 01 and its addendum record;
  - the no-ceiling addendum (PF10);
  - the decision record;
  - `docs/pfcanon/`;
  - for P-7, `ci/checks/classify_ci_changes.py` and `tests/evidence/test_rails_ci_workflow_integration.py`.
- **Writes:** its review artifact and, at DELTA_APPROVE, the addendum, both under `docs/ephemeral/`.
- **Needs:** no live vendor, production or database access. The pull request carrying this delta should be merged to `main` first.

## Canon relied on

Read on `main` at `7b763db` unless stated.

- **IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1**, read in full (page state of 2026-10-12T02:29:25Z). Governs:
  - `APPROVED_BASE_PLAN_DELTA_AUTHORING`: inputs; one standalone delta from the exact `PLAN_DELTA_REDLINE`; the delta's required contents (base and review identity, bounded overlay, affected areas, exclusions, conflicts, evidence, return point, application report);
  - `PLAN_DELTA_PENDING`;
  - "Apply only the supplied IA-30 redlines";
  - the handoff and TypeSafe rules.
- **IA-30 — Review Whole-Change Implementation Plan — 100926.1**, read in full (page state of 2026-10-12T02:29:54Z): `MATERIAL_PLAN_DELTA_REVIEW` inputs; "material"; the addendum at DELTA_APPROVE.
- **PF10-HDE-Build-Notes v13.7.1:**
  - front matter §1, §2 and §9 "Operational rule for agents" (steps 5 to 9);
  - addendum 2.18, the no-ceiling addendum, read in full (it matches its record, blob `d2932079`, except for its number);
  - addendum 2.11 rules 1 to 3, as the no-ceiling addendum restates its gates. 2.11 was read in full in v13.6.9 for the IA-40 return, and v13.7.1 changes no line of it: from v13.6.9 the diff adds only the no-ceiling addendum and its index line, and changes the version line;
  - addenda 2.7, 2.8, 2.9 and 2.10 at their WU-PR-08 carried items (the loopback bind at 2.7 "Affected surfaces", 2.8 and 2.9; OBS-P4-5 at 2.9 and 2.10; O-19, F-3 and the `1.4.0` cut at 2.10);
  - addendum 2.6 "Affected surfaces", at its WU-PR-08 sentence (K-2);
  - addendum 2.1 for the TypeSafe reading.
- **The Specification delta 01 addendum**, read in full from its record. The Product Owner added it to PF10 on 2026-10-21, and it is in force.
- **PF27-Canon-Plan-Templates v2.0.5:**
  - "CI lane classification and automated budget-control discipline", read in full: the smallest safe repository-grounded design belongs to the implementation task; a plan must not invent a change-detection mechanism; heavy validation is selected by affected change; nothing affected may be misclassified as irrelevant;
  - "Source-bound review authority and exact-fix limits", as the assessment cites it;
  - "Redline bundle construction discipline", read in full: the items were checked for anchor overlap against the unchanged base.
- **PF04-Canon-HDE-Governance v2.8.7** §9.1.1 (an approved Plan changes only through its delta route) and §9.1.2 (reviews govern within their scope).
- **PF30.1-Canon-HDE-CRD-Records v0.9.1** §4.2: a change to planned work units is material.
- **`AGENTS.md`:**
  - "HDE-EPIC039 current workflow posture" (the one `test` job; seven change-aware lanes; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`);
  - "Release identity" and "HDE-EPIC040 current posture" (release `1.3.0`, 45 members, admission constants);
  - the redaction rule (P-9's start command).
- **In-flight documents read in full:**
  - the change assessment v1.1;
  - Plan v1.1;
  - the IA-40 return record;
  - the Specification delta 01 addendum record;
  - the no-ceiling addendum record;
  - the decision record §1 to §3.
- **In-flight documents read in part:** Specification delta 01 (C-1 to C-14, as its addendum restates them in full) and its review (front matter and decision, read for the IA-40 return).
- **Not re-read in this session:** PF04 §9.1.1 and §9.1.2, and PF30.1 §4.2. They are cited as Plan v1.1 and the assessment cite them.
- **Repository read:**
  - `ci/checks/classify_ci_changes.py`: `_FULL_VALIDATION_PATHS`, `_DOCUMENTATION_PREFIXES`, `_DOCUMENT_PATHS`, `_WORKFLOW_CONTROL_PATH_LANES`, `_lanes_for_path` and `classify_paths`;
  - `tests/evidence/test_rails_ci_workflow_integration.py`, the scenario table;
  - `.env.example`, `docs/ADAPTER_009.md`, `adapter/wsgi.py`, `adapter/factory.py`, `Procfile` and `engine/providers/vendor_http_hdapi.py`;
  - `tools/ci/prepush_check.py`.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-40 / approved-base Plan delta authoring 1, second invocation (first standalone delta) |
| change | CRD HDE-CRD-0002 |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | whole-change Implementation Agent / IA-40 APPROVED_BASE_PLAN_DELTA_AUTHORING |
| capture time | 2026-10-21T20:24:34Z |
| execution identity | https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`) |
