---
artifact_type: IMPLEMENTATION_PLAN_CHANGE_ASSESSMENT
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-CHANGE-ASSESSMENT-01
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: APPROVED_BASE_CHANGE_ASSESSMENT
decision: PLAN_DELTA_REDLINE
immutable_base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4; approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md, INITIAL_APPROVE, blob 0cc0276524b292777cc562b64bb983bdc4c55e3b). Unchanged by this assessment
material_change_request: approved Specification delta 01, docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (blob 9408d6ed091bcba3d751fcb17ae392a1ceca8bbb), approved by docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md (DELTA_APPROVE, Thoth, 2026-10-21T18:36:00Z; blob 5a6cecc86f604a17aaa3e6c89b17183d2d0f9ffa), recorded by docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md (HDE Build Notes addendum 2.18; blob 64325e32376349394df0989602fca928bdcfb8da)
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (Product Owner OPTION 1, 2026-10-21; WU-PR-08 business case and ceiling, §2)
audit_lineage: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (AUDIT_COMPLETE); not revised
reviewer: Isis, continuing Lead Developer and whole-change Implementation Plan reviewer (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2; reviewer of Plan v1.0 and v1.1)
ia_author_return: the whole-change Implementation Agent for HDE-CRD-0002 (session lineage https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah and https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j), IA-40 APPROVED_BASE_PLAN_DELTA_AUTHORING
prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-21T18:40:57Z
repository_head_read: origin/main 0d9654e1
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.9.md (blob c9e598d65dd1e5b39f6a27b5826d1b387e0e8419; addenda 2.1 to 2.17; searched for WU-PR-08, WU-DOC-01, WU-OPS-01, S01, 1.4.0 and Plan overlays). Addendum 2.18 read from its docs/ephemeral record and treated as in force (CF-C-30 Execute step 5)
applicable_prior_overlays: none on the Plan for the affected units. Addenda 2.9 and 2.10 carry items to the WU-PR-08 and WU-DOC-01 instructions only; addenda 2.6, 2.7, 2.13 and 2.15 concern completed units WU-PR-03 and WU-PR-07
pf10_addendum: none (assessment mode creates none)
next_prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
next_mode: APPROVED_BASE_PLAN_DELTA_AUTHORING
---

# HDE-CRD-0002 — Implementation Plan change assessment 01 (IA-30)

## 1. Decision

**PLAN_DELTA_REDLINE.** Approved Specification delta 01 removes S01 and the release version cut. That is an authorized material change, and the approved Implementation Plan v1.1 no longer matches it. A bounded Plan delta is justified. No Product Owner choice is left open.

- **The base stays as it is.** Plan v1.1 is not edited, and its approval stands for everything outside §3 below.
- **The next step.** The same whole-change Implementation Agent authors one standalone pending `MATERIAL_PLAN_DELTA` in IA-40 from the redline in §3. The delta returns to this reviewer under `MATERIAL_PLAN_DELTA_REVIEW`.
- **What this authorizes.** Nothing beyond the delta's authoring: no addendum, approval, PR Instruction, PR, Ops, QA, acceptance or closure.

## 2. Assessment

| Test (IA-30, approved-base change assessment) | Finding |
| :- | :- |
| Source-supported | Yes. Specification delta 01 is approved (DELTA_APPROVE) and recorded as addendum 2.18. Its "Affected surfaces" section names the Plan passages that "are not in force against this Specification". The Product Owner's OPTION 1 decision authorizes it |
| Material | Yes, under IA-30's definition. It changes the scope of several planned units (WU-PR-08, WU-DOC-01, WU-OPS-01) and WU-PR-08's acceptance criteria. It also removes the Plan's version-cut commitment (§3 "Release-identity spine"; invariant 3) |
| Compatible with approved Specification intent | Yes. The delta implements the current Specification (base plus delta 01) and nothing else |
| Within Plan-delta authority | Yes. It is not a PR rescope (no PR is open for WU-PR-08), not remediation, and not another lane |
| Product Owner choice open | None. Scope is decided by OPTION 1. WU-PR-08's business case and ceiling were adopted in the decision record §2 (addendum 2.11 rule 3: IA-30 checks each unit's business case and ceiling) |
| Facts checked on `main` `0d9654e1` | `.env.example` lacks `GEO_API_KEY`. `docs/ADAPTER_009.md` lines 46–51 and 122/138 still carry the readiness and port statements S17 corrects. Neither file is a release member. The admission constants stand at `1.3.0` / `2026-08-24T18:04:49Z` (addendum 2.18, "Facts behind the decision") |

## 3. Bounded delta redline

The delta overlays exactly these changes on Plan v1.1.
- **Anchors** quote Plan v1.1 or name its exact location.
- **"Replace with"** gives the required wording. The author may adjust phrasing only where meaning is unchanged.
- **"Author states"** marks content the author designs inside the stated bound. This reviewer does not originate it (Plan Templates, "Source-bound review authority and exact-fix limits").
- Unit IDs, interface IDs and risk IDs are not renumbered. A removed item is marked removed.

| # | Plan v1.1 anchor | Change |
| :- | :- | :- |
| P-1 | §2 Lineage and sources table | Add rows: "Specification delta 01: `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, approved by `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md`; HDE Build Notes addendum 2.18"; "Product Owner scope decision: `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`"; "This change assessment: `docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.0.md`" |
| P-2 | §3 opening paragraph: "member-changing work lands before the version-bumping release cut (S01 unit last among code units)" | Replace with "each member-changing unit carries its own same-version manifest refresh (no release version cut)" |
| P-3 | §3 "Release-identity spine": "The single new release, `1.4.0` with new admission pins, is cut once, in WU-PR-08, after the last member-changing unit (Specification constraint "Release members"; Exclusions bullet 2). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member), WU-PR-08." | Replace with "No release version cut is made: the release stays at `1.3.0` and the admission constants do not change (Specification delta 01, C-5 and C-7). Member-changing units: WU-PR-03, WU-PR-04, WU-PR-05 (only if a confirmed finding changes a member)." The rest of the bullet is unchanged |
| P-4 | §4 invariant 3: "admission constants change only in WU-PR-08" | Replace with "the admission constants (`ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC`, `ADMITTED_RELEASE_ROSTER`) do not change in this change" |
| P-5 | §5 IF-8 row (Wheel layout) | Shape cell becomes "Removed with S01 (Specification delta 01); not delivered" |
| P-6 | §6 traceability: the S01 row; the "Release re-cut" row | S01 row: "removed (Specification delta 01, C-1 and C-6); not delivered \| — \| —". "Release re-cut" row: "same-version refresh in each member-changing unit; no version cut (Specification delta 01) \| — \| —" |
| P-7 | §7 WU-PR-08 block (title through Nonclaims) | Replace the block. The bound is fixed here; the author states the wording: **Title** "WU-PR-08 — Environment template and operator documentation (PR; Coagulation)". **Purpose** S16 and S17 only. **Bounded scope** S16, S17. **Inputs**: Audit §6 S16 and S17; the items HDE Build Notes carries to the WU-PR-08 instruction (addenda 2.9 and 2.10). **Deliverables**: `.env.example` (`GEO_API_KEY` entry only); `docs/ADAPTER_009.md` (readiness rules and port statements). **Dependencies and order**: eighth code unit, after WU-PR-07 (the order is kept); no release member changes, so no manifest refresh. Author states the classifier's lane selection for these two paths, read from `ci/checks/classify_ci_changes.py`. **Acceptance**: (1) `.env.example` has a `GEO_API_KEY` entry and nothing else changed; (2) the readiness section describes `/internal/readyz` as implemented and on which app, and the port statements match the runner and Procfile bindings; (3) admission at the PR head reports `1.3.0`, 45 members and the base head's `release_id` unchanged; (4) the selected lanes are green. **Evidence**: PR result record. **Risks**: author states; R-2 and R-6 no longer apply. **Nonclaims**: no release cut, no QA verdict. **Business case and ceiling**: carried by reference from the decision record §2 (beneficiary, evidence, benefit, measure, ceiling 1 PR, 2 sessions, 1 day), for PR-10 under addendum 2.11 rule 3 |
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

## 4. Effects

| Area | Effect |
| :- | :- |
| Requirements | S01 leaves the Plan; S16 and S17 stay in WU-PR-08 |
| Dependencies | WU-PR-08 no longer depends on members being final. Its place after WU-PR-07 is kept |
| Tests | No wheel-install test. No pinned-identity test rewrite to `1.4.0` |
| Ops | WU-OPS-01 verifies the `1.3.0` `release_id` and records the start command |
| Documentation | WU-DOC-01 drops the dedicated-environment install note and states `1.3.0` |
| Downstream | WU-PR-08's PR-10 follows the approved Plan delta, carrying the decision record's business case and ceiling. WU-PR-08's PR-40 records option A's measure (WU-PR-06) |

## 5. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The live Railway start command, a stated limit and not a blocker | WU-OPS-01; Product Owner |
| Business cases and ceilings for WU-DOC-01 and WU-OPS-01 (addendum 2.11 rules 1 and 3) | Product Owner. Due before DOC-10 and OPS-10. Not part of this delta |
| The HDE Build Notes addendum for the approved Plan delta | This reviewer at DELTA_APPROVE (IA-30); publication into PF10 by the Product Owner |

## 6. Return point

- **Now.** IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16), `APPROVED_BASE_PLAN_DELTA_AUTHORING`, for the same whole-change Implementation Agent.
- **Then.** IA-30 `MATERIAL_PLAN_DELTA_REVIEW`, for Isis.
- **On DELTA_APPROVE.** The continuation is PR-10 — Create PR Work-Unit Instructions — 100926.1, for WU-PR-08.

## 7. TypeSafe reading for the receiving session (IA-40)

Action sent (v8.2): "Author, as the whole-change Implementation Agent, the first standalone pending material delta against an approved 76 KB Implementation Plan, applying the Plan reviewer's bounded redline of about seventeen passages after an approved Specification delta: remove one packaging requirement and the release version cut from the remaining units, rewrite one small work unit's block around two kept requirements with its adopted business case and ceiling, and adjust an Ops unit's success criterion, a documentation unit's scope, the risk, exclusion and rollback tables and the re-cut procedure. The delta is one Markdown record with an application report; no code is written and no live run occurs, and the same reviewer reviews the delta before an addendum is issued."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.92 (confidence 0.73); rung probabilities low 0.00, medium 0.24, high 0.61, extra high 0.14, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.55, Sonnet 5.5 0.42, Haiku 5.5 0.01 (confidence 0.40). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.005, Fable 5.1 at high 0.012, Fable 5.1 at extra high 0.003, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.132, Opus 5.5 at high 0.336, Opus 5.5 at extra high 0.077, Opus 5.5 at max 0.006, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.101, Sonnet 5.5 at high 0.256, Sonnet 5.5 at extra high 0.059, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.002, Haiku 5.5 at high 0.006, Haiku 5.5 at extra high 0.001, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: model near tie between Opus 5.5 and Sonnet 5.5. Sent 2026-10-21T18:40:56Z.
- **Detail:** v8.2 sent 2026-10-21T18:40:56Z; HTTP 200 in 0.69 s; 5478 input and 71 output tokens; jev-1.13.0. Rung by rule: high; model by rule: Opus 5.5.
- **Nathan's pick for IA-40:** not stated.
- **Notion row:** not written (IA-30 handoff rule).

**Surface advice:** run IA-40 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change Implementation Agent role.
- **Reads from `main`:**
  - this assessment;
  - Plan v1.1 and its review v1.1;
  - Specification delta 01, its review and the addendum 2.18 record;
  - the decision record;
  - `docs/pfcanon/`;
  - for P-7, `ci/checks/classify_ci_changes.py`.
- **Writes:** only the pending delta and its application report under `docs/ephemeral/`.
- **Needs:** no live vendor, production or database access. This assessment's pull request should be merged to `main` first.

## Canon relied on

Read on `main` at `0d9654e1`.

- **IA-30 — Review Whole-Change Implementation Plan — 100926.1** (read in full on 2026-10-12; page state unchanged). Governs:
  - `APPROVED_BASE_CHANGE_ASSESSMENT` inputs and tests (source-supported, material, compatible, within authority);
  - the definition of "material";
  - `PLAN_DELTA_REDLINE` with exact anchors, bounded overlay, effects, exclusions, evidence and return point;
  - no addendum in this mode;
  - routing to IA-40.
- **IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1** (read in full on 2026-10-12): the `APPROVED_BASE_PLAN_DELTA_AUTHORING` contract and the fields the delta must carry (P-17).
- **PF10-HDE-Build-Notes v13.6.9.** Searched for WU-PR-08, WU-DOC-01, WU-OPS-01, S01, `1.4.0` and Plan overlays. Read:
  - addendum 2.11 in full (rule 1 business-case fields; rule 3, IA-30 checks each unit's business case and ceiling);
  - the passages of addenda 2.9 and 2.10 that carry items to WU-PR-08 and WU-DOC-01;
  - addendum 2.1 for the TypeSafe reading.

  Addendum 2.18 was read in full from `docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`, treated as in force (CF-C-30 Execute step 5).
- **PF04-Canon-HDE-Governance v2.8.7** §9.1.1 (an approved Plan is changed only through its delta route; the IA may not reinterpret the Specification) and §9.1.2 (reviews and dispositions govern within their scope), read for Plan review v1.0.
- **PF27-Canon-Plan-Templates v2.0.5**, "Source-bound review authority and exact-fix limits" (the reviewer does not originate design; the "Author states" items), read for Plan review v1.0.
- **PF30.1-Canon-HDE-CRD-Records v0.9.1 §4.2:** a change to planned work units is material, read 2026-10-21.
- **`AGENTS.md`:** "Release identity" (admission constants; `release_id` manifest-derived).

**In-flight documents read in full:**
- `docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` (this reviewer's own delta as Specification author);
- `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` (this reviewer's record of the Product Owner decision).

**Read in part:**
- `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md` (front matter and decision);
- `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, every passage matching S01, `1.4.0`, IF-8, R-2, R-6, R-8, "wheel", "version bump", "re-cut" and "admission constants", plus §2, §3, §7 WU-PR-08, WU-DOC-01 and WU-OPS-01, §10 to §14 (read in full for review v1.1).

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-30 / approved-base change assessment 1 |
| change | CRD HDE-CRD-0002 |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis / IA-30 APPROVED_BASE_CHANGE_ASSESSMENT |
| capture time | 2026-10-21T18:40:57Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
