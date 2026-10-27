---
artifact_type: IMPLEMENTATION_PLAN_CHANGE_ASSESSMENT
artifact_version: "1.1"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-CHANGE-ASSESSMENT-01
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: APPROVED_BASE_CHANGE_ASSESSMENT
decision: PLAN_DELTA_REDLINE
supersedes: docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.0.md (blob 52c204abd092afe1d125f869e0822b42cc94117b; landed by #677). Kept unchanged as history
returned_by: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md (IA-40 REDLINE_INCOMPLETE on P-7; blob eba413f352561c8afa5f6d153398909b24a0216c; landed by #678)
immutable_base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4; approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md, INITIAL_APPROVE, blob 0cc0276524b292777cc562b64bb983bdc4c55e3b). Unchanged by this assessment
material_change_request: approved Specification delta 01, docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (blob 9408d6ed091bcba3d751fcb17ae392a1ceca8bbb), approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md (DELTA_APPROVE, Thoth, 2026-10-21T18:36:00Z; blob 5a6cecc86f604a17aaa3e6c89b17183d2d0f9ffa), recorded by docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md (HDE Build Notes addendum 2.18; blob 64325e32376349394df0989602fca928bdcfb8da)
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (Product Owner OPTION 1, 2026-10-21; WU-PR-08 business case and ceiling, §2; blob efc220928f7c313ba5ebabb49b975b624dfbafc2). Its cost line is corrected by §5 below; the record itself is not edited
audit_lineage: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE); not revised
reviewer: Isis, continuing Lead Developer and whole-change Implementation Plan reviewer (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2; reviewer of Plan v1.0 and v1.1; author of assessment v1.0)
ia_author_return: the whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N), continuing the Plan author lineage (sessions https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah and https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j), IA-40 APPROVED_BASE_PLAN_DELTA_AUTHORING
prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-21T18:59:54Z
repository_head_read: origin/main 0cad04eb
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.9.md (blob c9e598d65dd1e5b39f6a27b5826d1b387e0e8419). Front matter §9 "Operational rule for agents" in full; addendum 2.11 rules 1 to 3 in full; the WU-PR-08 carried-item passages of addenda 2.7, 2.8, 2.9 and 2.10; addenda 2.11, 2.12, 2.15 and 2.16 at their WU-PR-08 passages. Addendum 2.18 read from its docs/ephemeral record and treated as in force (CF-C-30 Execute step 5)
applicable_prior_overlays: none on the Plan for the affected units. Addenda 2.7 to 2.10 carry items to the WU-PR-08 and WU-DOC-01 instructions only; addenda 2.6, 2.7, 2.13 and 2.15 concern completed units WU-PR-03 and WU-PR-07
pf10_addendum: none (assessment mode creates none)
next_prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
next_mode: APPROVED_BASE_PLAN_DELTA_AUTHORING
---

# HDE-CRD-0002 — Implementation Plan change assessment 01, revision 1.1 (IA-30)

## 1. Decision

**PLAN_DELTA_REDLINE, revised.** Approved Specification delta 01 removes S01 and the release version cut. That is an authorized material change, and the approved Implementation Plan v1.1 no longer matches it. A bounded Plan delta is justified.

This revision answers IA-40's REDLINE_INCOMPLETE on P-7:
- **IA-40 was right.** The CI classifier refuses `.env.example`, so a WU-PR-08 bounded to `.env.example` and `docs/ADAPTER_009.md` cannot pass CI. My v1.0 P-7 assumed it could, without checking the classifier.
- **The bound is now option A.** WU-PR-08 also registers `.env.example` in `ci/checks/classify_ci_changes.py`. Because that file is a full-validation path, the unit's pull request runs all seven lanes.
- **Every other item is carried unchanged.** P-1 to P-6 and P-8 to P-17 keep their v1.0 text, which IA-40 found applicable as written. The one exception is a reference: P-1's lineage row for "this change assessment" now names this v1.1, with v1.0 and the return record as history. No bound changes.
- **The business case's cost line was wrong, and is corrected in §5.** WU-PR-08's ceiling ("1 PR, 2 sessions, 1 day") is also inconsistent with the session counting the Product Owner adopted for WU-PR-07. Setting the ceiling is the Product Owner's decision.
  - It does not block the delta's authoring: P-7 carries the business case by reference.
  - It is needed before this reviewer approves the delta, because IA-30 checks each unit's ceiling (addendum 2.11 rule 3). It must also be set before WU-PR-08's PR-10.

What happens next, and what this authorizes:
- **The base stays as it is.** Plan v1.1 is not edited, and its approval stands for everything outside §3 below.
- **The next step.** The same whole-change Implementation Agent authors one standalone pending `MATERIAL_PLAN_DELTA` in IA-40 from the redline in §3. The delta returns to this reviewer under `MATERIAL_PLAN_DELTA_REVIEW`.
- **What this authorizes.** Nothing beyond the delta's authoring: no addendum, approval, PR Instruction, PR, Ops, QA, acceptance or closure.

## 2. Assessment

| Test (IA-30, approved-base change assessment) | Finding |
| :- | :- |
| Source-supported | Yes. Specification delta 01 is approved (DELTA_APPROVE) and recorded as addendum 2.18. Its "Affected surfaces" section names the Plan passages that "are not in force against this Specification". The Product Owner's OPTION 1 decision authorizes it |
| Material | Yes, under IA-30's definition. It changes the scope of several planned units (WU-PR-08, WU-DOC-01, WU-OPS-01) and WU-PR-08's acceptance criteria. It also removes the Plan's version-cut commitment (§3 "Release-identity spine"; invariant 3) |
| Compatible with approved Specification intent | Yes. The delta implements the current Specification (base plus delta 01) and nothing else. The classifier registration adds no requirement. It is the means by which S16's file change reaches CI |
| Within Plan-delta authority | Yes. It is not a PR rescope (no PR is open for WU-PR-08), not remediation, and not another lane |
| Product Owner choice open | One: WU-PR-08's cost ceiling (§5). Scope is decided by OPTION 1. The business case's beneficiary, evidence, benefit and measure stand as adopted in the decision record §2 |
| Business case (addendum 2.11 rules 1 to 3) | Adopted for WU-PR-08, with one cost-line correction and an open ceiling (§5). The registration is not CI work for its own sake (rule 2). Without it S16 cannot land, because CI refuses any PR that changes `.env.example` |
| Facts checked on `main` `0d9654e1` (v1.0) | `.env.example` lacks `GEO_API_KEY`. `docs/ADAPTER_009.md` lines 46–51 and 122/138 still carry the readiness and port statements S17 corrects. Neither file is a release member. The admission constants stand at `1.3.0` / `2026-08-24T18:04:49Z` (addendum 2.18, "Facts behind the decision") |
| Facts checked on `main` `0cad04eb` (this revision) | `classify_paths(['.env.example'])` raises `ValueError: CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`. `classify_paths(['docs/ADAPTER_009.md'])` returns `documentation_only`. A change to `ci/checks/classify_ci_changes.py` selects lanes (return record §2: all seven, 166 changed-test targets). `_DOCUMENT_PATHS` is `AGENTS.md`, `ARCHITECTURE.md`, `AcceptanceMap.md`, `CHANGELOG.md`, `LICENSE`, `README.md`. No test under `tests/` names `_DOCUMENT_PATHS` |

## 3. Bounded delta redline

The delta overlays exactly these changes on Plan v1.1.
- **Anchors** quote Plan v1.1 or name its exact location.
- **"Replace with"** gives the required wording. The author may adjust phrasing only where meaning is unchanged.
- **"Author states"** marks content the author designs inside the stated bound. This reviewer does not originate it (Plan Templates, "Source-bound review authority and exact-fix limits"; and "CI lane classification and automated budget-control discipline": a review "MUST NOT invent … a change-detection mechanism").
- Unit IDs, interface IDs and risk IDs are not renumbered. A removed item is marked removed.

| # | Plan v1.1 anchor | Change |
| :- | :- | :- |
| P-1 | §2 Lineage and sources table | Add rows: "Specification delta 01: `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, approved by `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`; HDE Build Notes addendum 2.18"; "Product Owner scope decision: `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`"; "This change assessment: `docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md` (superseding v1.0 after IA-40's return, `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md`)" |
| P-2 | §3 opening paragraph: "member-changing work lands before the version-bumping release cut (S01 unit last among code units)" | Replace with "each member-changing unit carries its own same-version manifest refresh (no release version cut)" |
| P-3 | §3 "Release-identity spine": "The single new release, `1.4.0` with new admission pins, is cut once, in WU-PR-08, after the last member-changing unit (Specification constraint "Release members"; Exclusions bullet 2). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member), WU-PR-08." | Replace with "No release version cut is made: the release stays at `1.3.0` and the admission constants do not change (Specification delta 01, C-5 and C-7). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member)." The rest of the bullet is unchanged |
| P-4 | §4 invariant 3: "admission constants change only in WU-PR-08" | Replace with "the admission constants (`ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC`, `ADMITTED_RELEASE_ROSTER`) do not change in this change" |
| P-5 | §5 IF-8 row (Wheel layout) | Shape cell becomes "Removed with S01 (Specification delta 01); not delivered" |
| P-6 | §6 traceability: the S01 row; the "Release re-cut" row | S01 row: "removed (Specification delta 01, C-1 and C-6); not delivered \| — \| —". "Release re-cut" row: "same-version refresh in each member-changing unit; no version cut (Specification delta 01) \| — \| —" |
| P-7 (revised) | §7 WU-PR-08 block (title through Nonclaims) | Replace the block. The bound is fixed here; the author states the wording. **Title** "WU-PR-08 — Environment template and operator documentation (PR; Coagulation)". **Purpose** S16 and S17 only; the classifier registration exists so that S16's file change can pass CI. **Bounded scope** S16, S17, and one classifier registration that makes `.env.example` a classified change surface. **Inputs** Audit §6 S16 and S17. Also the items HDE Build Notes carries to the WU-PR-08 instruction: the loopback bind statements (addenda 2.7, 2.8 and 2.9), and OBS-P4-5, O-19 and the production route exposure, contract F-3 (addenda 2.9 and 2.10). Not carried: addendum 2.10's "cuts `1.4.0` from `release_id` `77204764…` (contract F-1)". Addendum 2.18 approves no version cut and governs that overlapping scope (PF10 front matter §9, step 8: "apply only the highest-numbered applicable addendum to the overlapping scope"; noted in the IA-40 return record §4). **Deliverables** (1) `.env.example`: a `GEO_API_KEY` entry only. (2) `docs/ADAPTER_009.md`: the readiness rules and port statements. (3) `ci/checks/classify_ci_changes.py`: one registration that classifies `.env.example`. Author states its form at PR-20, choosing the smallest repository-grounded registration among the classifier's existing mechanisms. (4) The registration's owner or pin test, only if one enumerates the registry the registration changes; author states which, read from the repository. **Dependencies and order** Eighth code unit, after WU-PR-07 (the order is kept). No release member changes, so there is no manifest refresh. A change to the classifier is a full-validation path, so the PR runs all seven lanes. Author states the lane selection read from `ci/checks/classify_ci_changes.py` or `tools/ci/prepush_check.py lanes`. **Acceptance** (1) `.env.example` has a `GEO_API_KEY` entry and nothing else in it changed. (2) The readiness section describes `/internal/readyz` as implemented and names the app that serves it, and the port statements match the runner and Procfile bindings. (3) Admission at the PR head reports `1.3.0`, 45 members and the base head's `release_id`, unchanged. (4) At the PR head, the classifier run on `.env.example` alone returns a classification and no `CI_CHANGE_SURFACE_UNCLASSIFIED`. (5) All seven lanes are green on the exact PR head, with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. **Evidence** PR result record. **Risks** Author states. R-2 and R-6 no longer apply. **Nonclaims** No release cut, no CI workflow change, no QA verdict. **Business case and ceiling** Carried by reference for PR-10 under addendum 2.11 rule 3, as follows. Beneficiary, evidence, benefit and measure come from the decision record §2. The cost line is as corrected by this assessment §5. The ceiling is the one the Product Owner sets in the recorded decision that §5 asks for |
| P-8 | §7 WU-DOC-01, Bounded scope: "`README.md` (install into a dedicated environment; …" and "HDE-EPIC040 current posture → release `1.4.0`" | Delete "install into a dedicated environment; " (its basis was R-6). Replace "→ release `1.4.0`" with "→ release `1.3.0`, refreshed in place with no version cut, and its current `release_id`". Nothing else changes |
| P-9 | §7 WU-OPS-01: Intent ("… and the deployment facts the QA Plan and S01's exemption basis need …"); Success criteria ("the `1.4.0` `release_id`"; "the recorded deployment trigger and build command"); Constraints ("if the discovered build command differs from the checked-in declarations, record it and stop (the QA Plan's S01 treatment depends on it)") | Intent: replace "and S01's exemption basis" with "and the live start command (Specification delta 01's stated limit; addendum 2.18 'Unresolved obligations')". Success criteria: "the `1.4.0` `release_id`" becomes "the candidate's `release_id` at version `1.3.0`", and "deployment trigger and build command" becomes "deployment trigger, build command and start command". Constraints: remove the S01 dependency. **Author states** what the task records and does if the live start command does not run the engine from the checkout as the `Procfile` does, within the stated limit that admission would then refuse to start (`MISSING_FILE`) |
| P-10 | §9 item 2: "The acceptance intents S01 to S22 …" and "the wheel-install admission test, " | "The acceptance intents S02 to S22 (S01 removed by Specification delta 01) …"; delete "the wheel-install admission test, " |
| P-11 | §9 item 3: "S01's class-2 step or its recorded exemption basis from WU-OPS-01's discovery; " | Delete the clause |
| P-12 | §10 heading: "(binding method for WU-PR-03, WU-PR-04, WU-PR-05 when a member changes, and WU-PR-08)"; step 2, the sentence beginning "`<V>`/`<T>` are the current constants for a refresh" | Heading: "(binding method for any unit that changes a release member: a same-version refresh)". Step 2 sentence: "`<V>`/`<T>` are the current constants (`1.3.0` / `2026-08-24T18:04:49Z`); no version bump is made (Specification delta 01)." Other steps unchanged |
| P-13 | §11 R-2 Unit cell "WU-PR-03/04/05/08"; R-6 row; R-8 Risk cell "Three or four manifest refreshes before the version bump multiply convergence effort." | R-2 Unit: "WU-PR-03/04/05". R-6: Risk "Removed with S01 (Specification delta 01)"; Unit and Treatment "—". R-8 Risk: "Three or four same-version manifest refreshes multiply convergence effort." |
| P-14 | §12 Exclusions: "no release re-cut beyond the refreshes admission forces and the single `1.4.0` cut" | Replace with "no release version cut: the release stays at `1.3.0`, with same-version refreshes only (Specification delta 01, C-5); S01 removed and not delivered (C-6)" |
| P-15 | §13, the paragraph "No engineering decision remains open at Plan level; EC-1 to EC-12 are recorded in Audit §7.1 and applied here." | Append: "Specification delta 01 withdraws EC-11 (S01 packaging); EC-12 applies only as same-version refreshes." |
| P-16 | §14 Migration and rollback: "; a reverted WU-PR-08 restores the `1.3.0` constants and manifest and re-converges" | Delete the clause |
| P-17 | Header and state | The delta's header states the immutable base, this assessment, delta 01 and addendum 2.18 as the approved base plus overlays, and `PLAN_DELTA_PENDING`. It carries the IA-40 fields: affected requirements, dependencies, tests, Ops and documentation; exclusions; conflicts; evidence; return point; application report |

### 3.1 Unchanged, with the reason

- **Completed units WU-PR-01 to WU-PR-07, their blocks, and R-5.** They are executed history.
  - WU-PR-05's "precede the version bump" (§7) and R-5's "Fixes precede the version bump" are kept as written. They describe the order that held when the unit ran, and no future step depends on them.
- **The other blocks and sections:**
  - §1 and §8;
  - §9 items 1, 4 and 5;
  - §10 steps 1 and 3 to 12;
  - §15 and §16, except as P-17's header requires;
  - every interface other than IF-8;
  - every risk other than R-2, R-6 and R-8;
  - AQ-1;
  - the unit order WU-PR-08 → WU-DOC-01 → WU-OPS-01 → QA-10.
- **The Implementation Audit.** It is not revised. Its S01, EC-11 and §7.3 version-bump text are superseded for planning by Specification delta 01 and this assessment (HDE Governance §9.1.2, reviews govern within their scope).

### 3.2 Changes from v1.0

| Item | v1.0 | v1.1 |
| :- | :- | :- |
| P-1 | The "this change assessment" row named v1.0 | It names v1.1, with v1.0 and the return record as history. Reference only |
| P-7 Purpose and bounded scope | S16, S17 | S16, S17 and one classifier registration for `.env.example` |
| P-7 Inputs | "addenda 2.9 and 2.10" | The carried items named one by one, from addenda 2.7 to 2.10, without 2.10's `1.4.0` cut (contract F-1), which 2.18 governs |
| P-7 Deliverables | Two files | Adds `ci/checks/classify_ci_changes.py` and, if one exists, its enumerating owner or pin test. The author states the form |
| P-7 Dependencies | "Author states the classifier's lane selection for these two paths" | All seven lanes run. The author states the selection as read from the classifier |
| P-7 Acceptance | (4) "the selected lanes are green" | (4) `.env.example` classifies at the PR head; (5) all seven lanes are green on the exact head |
| P-7 Nonclaims | No release cut, no QA verdict | Adds no CI workflow change |
| P-7 Business case | Ceiling "1 PR, 2 sessions, 1 day" carried | Carried, with the cost line as corrected in §5 and the ceiling as the Product Owner sets it |
| §1, §2, §4, §5 | — | Updated for the above |

## 4. Effects

| Area | Effect |
| :- | :- |
| Requirements | S01 leaves the Plan; S16 and S17 stay in WU-PR-08 |
| Dependencies | WU-PR-08 no longer depends on members being final. Its place after WU-PR-07 is kept |
| Tests and CI | No wheel-install test. No pinned-identity test rewrite to `1.4.0`. WU-PR-08 changes the classifier, so its PR runs all seven lanes: about 20 minutes of hosted CI per push, and about 25 to 33 minutes for a local full replay (return record §3) |
| Ops | WU-OPS-01 verifies the `1.3.0` `release_id` and records the start command |
| Documentation | WU-DOC-01 drops the dedicated-environment install note and states `1.3.0` |
| Downstream | WU-PR-08's PR-10 follows the approved Plan delta and carries the decision record's business case, corrected by §5, and the ceiling the Product Owner sets. WU-PR-08's PR-40 records option A's measure for WU-PR-06 |

## 5. WU-PR-08 business case: cost-line correction and the ceiling question

**The correction.** The decision record §2 "Cost ceiling" row reads: "Neither change touches a release member, so there is no manifest refresh and no full-validation CI run." Its second half is wrong.
- **What the record should have said.** S16 needs a classifier registration, and a classifier change is a full-validation path, so WU-PR-08's PR runs all seven lanes.
- **What stands.** The first half stands: no release member changes and there is no manifest refresh. Beneficiary, evidence, benefit and measure are unaffected.
- **Where the correction lives.** This assessment supersedes the record's cost line. The issued record is not edited.

**The ceiling question.** The adopted ceiling is "1 PR, 2 sessions, 1 day from PR-10 to merge". It is inconsistent with the session counting the Product Owner adopted for WU-PR-07, where the PR-10 invocation, the PR-20/PR-30 session and the PR-35 session make three sessions (`docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md`, "Sessions"). Counted that way, WU-PR-08 passes a two-session ceiling at its minimum path. That was my drafting error in the decision record.
- **Full lanes add time, not sessions.** About 20 minutes of hosted CI per push still fits in one day.
- **Recommendation.** 1 PR, 3 sessions, 1 day from PR-10 to merge, counted as for WU-PR-07. Past that, the unit returns to the Product Owner.
- **Whose decision it is.** The Product Owner's (addendum 2.11 rule 1, "cost ceiling"; rule 3, gates). It must be recorded before this reviewer approves the delta, since IA-30 checks the ceiling, and so in place before WU-PR-08's PR-10.

## 6. Unresolved items and owners

| Item | Owner |
| :- | :- |
| WU-PR-08's cost ceiling (§5), recorded before IA-30 approves the delta | Product Owner; recorded by Isis |
| The live Railway start command, a stated limit and not a blocker | WU-OPS-01; Product Owner |
| Business cases and ceilings for WU-DOC-01 and WU-OPS-01 (addendum 2.11 rules 1 and 3) | Product Owner. Due before DOC-10 and OPS-10. Not part of this delta |
| The HDE Build Notes addendum for the approved Plan delta | This reviewer at DELTA_APPROVE (IA-30); publication into PF10 by the Product Owner |

## 7. Return point

- **Now.** IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16), `APPROVED_BASE_PLAN_DELTA_AUTHORING`, for the same whole-change Implementation Agent (session "HDE-CRD-0002-2").
- **Then.** IA-30 `MATERIAL_PLAN_DELTA_REVIEW`, for Isis.
- **On DELTA_APPROVE, with the ceiling recorded.** The continuation is PR-10 — Create PR Work-Unit Instructions — 100926.1, for WU-PR-08.

## 8. TypeSafe reading for the receiving session (IA-40)

Action sent (v8.2): "Author, as the whole-change Implementation Agent, the first standalone pending material delta against an approved 76 KB Implementation Plan, applying the Plan reviewer's revised bounded redline of about seventeen passages after an approved Specification delta, on the second invocation after the first returned one item unapplied: remove one packaging requirement and the release version cut from the remaining units, rewrite one small work unit's block around two kept requirements plus one CI classifier registration that makes its pull request run every lane, carrying its business case by reference, and adjust an Ops unit's success criterion, a documentation unit's scope, the risk, exclusion and rollback tables and the re-cut procedure. The delta is one Markdown record with an application report; no code is written and no live run occurs, and the same reviewer reviews the delta before an addendum is issued."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.99 (confidence 0.79); rung probabilities low 0.00, medium 0.16, high 0.69, extra high 0.15, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.83, Sonnet 5.5 0.16, Haiku 5.5 0.00 (confidence 0.77). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.002, Fable 5.1 at high 0.007, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.133, Opus 5.5 at high 0.573, Opus 5.5 at extra high 0.124, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.026, Sonnet 5.5 at high 0.110, Sonnet 5.5 at extra high 0.024, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T18:57:41Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T18:57:41Z; HTTP 200 in 0.66 s; 5506 input and 71 output tokens; jev-1.13.0. Session kind "correction". Rung by rule: high; model by rule: Opus 5.5. No flags.
- **This reading supersedes v1.0 §7's** for the same session (the action text changed with the revised redline).
- **Nathan's pick for IA-40:** not stated.
- **Notion row:** not written (IA-30 handoff rule).

**Surface advice:** run IA-40 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change Implementation Agent role.
- **Reads from `main`:**
  - this assessment and the return record;
  - Plan v1.1 and its review v1.1;
  - Specification delta 01, its review and the addendum 2.18 record;
  - the decision record;
  - `docs/pfcanon/`;
  - for P-7, `ci/checks/classify_ci_changes.py`.
- **Writes:** only the pending delta and its application report under `docs/ephemeral/`.
- **Needs:** no live vendor, production or database access. This assessment's pull request should be merged to `main` first.

## Canon relied on

Read on `main` at `0cad04eb` unless stated.

- **IA-30 — Review Whole-Change Implementation Plan — 100926.1** (read in full on 2026-10-12; page state unchanged). Governs:
  - `APPROVED_BASE_CHANGE_ASSESSMENT` inputs and tests (source-supported, material, compatible, within authority);
  - the definition of "material";
  - `PLAN_DELTA_REDLINE` with exact anchors, bounded overlay, effects, exclusions, evidence and return point;
  - no addendum in this mode;
  - routing to IA-40.
- **IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1** (read in full on 2026-10-12): the `APPROVED_BASE_PLAN_DELTA_AUTHORING` contract; `REDLINE_INCOMPLETE` returns to the reviewer; the fields the delta must carry (P-17).
- **PF10-HDE-Build-Notes v13.6.9.**
  - Searched for WU-PR-08, `1.4.0`, F-1, OBS-P4-5, O-19, F-3, loopback, and Plan overlays.
  - Read front matter §9 "Operational rule for agents" in full (step 8, overlapping scopes; step 9, distinct scopes).
  - Read addendum 2.11 rules 1 to 3 in full: the business-case fields and the cost ceiling "in sessions and elapsed days"; rule 2, CI for its own sake is not a business case; rule 3 gates, where IA-30 checks each unit's business case and ceiling, PR-10 carries both, and a unit past its ceiling returns to the Product Owner.
  - Read the WU-PR-08 carried-item passages of addenda 2.7, 2.8, 2.9 and 2.10, including 2.10's "WU-PR-08 (S17) cuts `1.4.0` … (contract F-1), with OBS-P4-5, O-19 and the production route exposure (F-3)".
  - Read the WU-PR-08 passages of addenda 2.11, 2.12, 2.15 and 2.16.
  - Read addendum 2.1 for the TypeSafe reading.
  - Addendum 2.18 was read in full from its `docs/ephemeral` record and treated as in force (CF-C-30 Execute step 5).
- **PF27-Canon-Plan-Templates v2.0.5:**
  - "CI lane classification and automated budget-control discipline", read in full. The implementation task selects the smallest safe repository-grounded design, and a review must not invent a change-detection mechanism. That is why the registration's form is "Author states".
  - "Source-bound review authority and exact-fix limits" (the reviewer does not originate design), read for Plan review v1.0.
- **PF04-Canon-HDE-Governance v2.8.7** §9.1.1 (an approved Plan is changed only through its delta route) and §9.1.2 (reviews and dispositions govern within their scope), read for Plan review v1.0.
- **PF30.1-Canon-HDE-CRD-Records v0.9.1 §4.2:** a change to planned work units is material, read 2026-10-21.
- **`AGENTS.md`:** "HDE-EPIC039 current workflow posture" (the one `test` job, seven change-aware lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) and "Release identity".

**In-flight documents read in full:**
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.0.md` (this reviewer's own v1.0);
- `docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`.

**Read in part:**
- `docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md`: "Cost ceiling" and "Sessions";
- `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`: front matter and decision;
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`. Read every passage matching S01, `1.4.0`, IF-8, R-2, R-6, R-8, "wheel", "version bump", "re-cut", "admission constants" and "classif", plus §2, §3, §7 WU-PR-08, WU-DOC-01 and WU-OPS-01, and §10 to §14. It was read in full for review v1.1.

**Repository read:** `ci/checks/classify_ci_changes.py`, at `_DOCUMENT_PATHS` and through `classify_paths`, which was run at `0cad04eb` on `.env.example`, `docs/ADAPTER_009.md` and `ci/checks/classify_ci_changes.py`.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-30 / approved-base change assessment 1, revision 1.1 |
| change | CRD HDE-CRD-0002 |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis / IA-30 APPROVED_BASE_CHANGE_ASSESSMENT |
| capture time | 2026-10-21T18:59:54Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
