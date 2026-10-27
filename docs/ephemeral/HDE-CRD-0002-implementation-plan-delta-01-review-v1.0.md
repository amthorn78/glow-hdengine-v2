---
artifact_type: IMPLEMENTATION_PLAN_DELTA_REVIEW
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-DELTA-01-REVIEW
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
review_mode: MATERIAL_PLAN_DELTA_REVIEW
decision: DELTA_DENY
reviewed_delta: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.0.md (MATERIAL_PLAN_DELTA v1.0, PLAN_DELTA_PENDING; landed by #681 as bb263fc)
application_report: docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.0-application-report.md
immutable_base: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4), approved by docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (INITIAL_APPROVE). Unchanged
redline_lineage: docs/ephemeral/HDE-CRD-0002-implementation-plan-change-assessment-v1.1.md (PLAN_DELTA_REDLINE P-1 to P-17), superseding v1.0 after docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-redline-return-v1.0.md (REDLINE_INCOMPLETE on P-7)
material_change: docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md (DELTA_APPROVE, docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md), recorded by docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md
authorizing_decisions: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (OPTION 1); the Product Owner's deployment direction of 2026-10-21, recorded first in §2 of this review
ia_author: the whole-change Implementation Agent for HDE-CRD-0002, session "HDE-CRD-0002-2" (https://claude.ai/code/session_01U3QLYTkfUepeRbSGZNPj9N)
reviewer: Isis, continuing Lead Developer and whole-change Implementation Plan reviewer (Isis-53, continuing from session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2; this session https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
prompt: IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c; page state of 2026-10-12T02:29:54Z, read in full in this invocation)
prompt_release: GCFPE-20261009.1 / 100926.1
repository_head_read: origin/main bb263fcb0a04cbddddb0fef78292204961a5b861
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.1.md
pf10_addendum: none (DELTA_DENY creates none)
created_at: 2026-10-21T20:40:00Z
next_prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
---

# HDE-CRD-0002 — Implementation Plan delta 01 v1.0: review (IA-30, DELTA_DENY)

## 1. Decision

**DELTA_DENY.** The delta applies redline P-1 to P-17 correctly. It is returned for one reason only: the Product Owner's direction of 2026-10-21 on deployments (§2) contradicts its WU-OPS-01 text (P-9) and two base passages of the same unit, and with them risk R-9. The redlines in §4 bring those passages into line with that direction. Everything else in the delta is accepted as written (§3), and the revision carries it unchanged.

No addendum is created. The approved Plan v1.1 is unchanged, and this review authorizes no PR Instruction, PR, Ops, QA, acceptance or closure.

## 2. Product Owner direction recorded here

The Product Owner, Nathan, 2026-10-21, in his handoff to this review: "deploys come from github commits, this should already be well established."

What it means for this change, as the handoff states it:
- The candidate reaches the Railway HD Engine service when its commit lands on `main` of `amthorn78/glow-hdengine-v2`.
- `GET /internal/version` on the service returning the candidate's `release_id` is the proof that the candidate is deployed.
- WU-OPS-01 discovers and records no deployment trigger, build command or start command.

Its standing:
- It is a Product Owner disposition, and governs within its scope (HDE Governance §9.1.2).
- It is a PO-provided deployed environment fact. Glow Infrastructure §2.4 says such facts "MUST NOT be downgraded to `OPEN/TBD`". So the Plan treats the deploy source as known, not as a PF07 gap left for OPS discovery.
- It supersedes the start-command parts of change assessment v1.1 P-9 (this reviewer's own redline), which required WU-OPS-01 to record the live start command.
- It discharges the unresolved obligation that the Specification delta 01 addendum assigned to "WU-OPS-01 records the deployment facts; Product Owner" (its "Unresolved obligations and owners"). The owner named there has decided. The Specification text itself is unchanged: C-6's stated limit (admission refuses `MISSING_FILE` if production ever ran without the checkout) stays as written. The `/internal/version` proof shows whether admission accepted the candidate's release in production.

## 3. Review of the delta as authored

| Check | Result |
| :- | :- |
| Immutable base | Plan v1.1 on `main` is blob `abffa2cc…`, unchanged |
| Anchors | All 25 anchor strings occur exactly once in the base (counted by this reviewer). No two items' spans overlap. P-7 replaces the whole WU-PR-08 block |
| P-2 to P-6, P-8, P-10 to P-16 | Applied as written. Accepted |
| P-1, P-17 (A-2, A-8) | Accepted. Naming the two addenda by title and record (delta §2, K-4) is unambiguous, and the delta does not depend on their numbers |
| P-7 (A-1, A-3 to A-5) | Accepted. The block is within the bound. The ceiling is correctly left out (HDE Build Notes 2.18, the no-ceiling addendum, rule 1). The registration's form stays the PR-20 author's choice, and the delta records only repository facts (K-5) |
| P-7 repository facts, re-checked by this reviewer on `bb263fc` | `ci/checks/classify_ci_changes.py` is in `_FULL_VALIDATION_PATHS`. `_DOCUMENT_PATHS` is `AGENTS.md`, `ARCHITECTURE.md`, `AcceptanceMap.md`, `CHANGELOG.md`, `LICENSE`, `README.md`. `classify_paths(['.env.example'])` raises `CI_CHANGE_SURFACE_UNCLASSIFIED:.env.example`. `docs/ADAPTER_009.md` alone is `documentation_only`. No file under `tests/`, `ci/` or `tools/` names `_DOCUMENT_PATHS` except the classifier itself. The non-documentation files that name `.env.example` are the fixture literal in `tests/qa/test_generate_epic_close_pack.py` and historical hash lists and notes (`manifest_pre.sha256`, `manifest_post.sha256`, `handoff/…`, `notes/…`). No code reads those lists (only audit inventories mention them) |
| P-9 (A-6, A-7) | The application of the redline as written is correct. Its content is superseded by §2: see D-1 to D-3. A-7's reviewer note is answered by D-3, because the build-command stop goes with the build-command discovery |
| Conflicts K-1 to K-5 | Accepted |
| §4 to §8 | Accepted, except the rows D-7 names |
| Exclusions | Accepted. No unit added, removed or reordered. No version cut. No workflow change |

## 4. Delta redlines

Each item names its anchor exactly. The text in quotation marks is the required wording. The author may adjust phrasing only where meaning is unchanged. "Author states" marks content the author designs inside the stated bound; this reviewer does not originate it (Plan Templates, "Source-bound review authority and exact-fix limits"). D-1 to D-3 replace the delta's own P-9 overlay text. D-4 to D-6 are new overlay items on Plan v1.1 passages, which the delta lists in its overlay as P-18 to P-20 (numbering is the author's).

| # | Anchor | Change |
| :- | :- | :- |
| D-1 | Delta §3 P-9, **Intent** | Replace the second sentence ("The deployment facts the QA Plan needs, and the live start command (…), are recorded presence-only.") with: "The candidate reaches the service when its commit lands on `main` (Product Owner direction of 2026-10-21, recorded in `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.0.md` §2)." The first sentence is unchanged |
| D-2 | Delta §3 P-9, **Success criteria** | Replace with: "`GET /internal/version` on the base URL reports the candidate's identity (the candidate's `release_id` at version `1.3.0`), which proves the candidate is deployed; the presence-only binding probe; all captured under `audit/ops/hde-crd-0002/wu-ops-01/` with path proofs (Plan Templates §3 evidence posture; lower-case directory names)." The trigger, build command and start command are not recorded |
| D-3 | Delta §3 P-9, **Constraints** | Replace the whole overlay, including the "Live start command" paragraph, with: "No production configuration change by this task. The task does not discover or record the deployment trigger, build command or start command. Rollback intent: redeploy the previously deployed commit." **Author states** what the task records and does when `GET /internal/version` does not report the candidate's `release_id` after the candidate's commit has landed on `main`. Bound: no production configuration change; no discovery of the trigger, build command or start command; the rollback intent as stated; no secret values or raw bodies recorded (the unit's Secret posture); the Product Owner decides any next step beyond that |
| D-4 | Plan v1.1 §7 WU-OPS-01, **PF07 posture**: the sentences from "PF07-gap (discoverable by OPS): the service's deployment trigger" to "it does not guess them." | Replace with: "Deploy source: the candidate reaches the service when its commit lands on `main` of `amthorn78/glow-hdengine-v2` (Product Owner direction of 2026-10-21; a PO-provided deployed environment fact, which Glow Infrastructure §2.4 does not allow to be downgraded to `OPEN/TBD`). The build and start commands are not discovered or recorded; `GET /internal/version` reporting the candidate's `release_id` is the proof of deployment. The deploy-source fact is a Glow Infrastructure doc-delta candidate (§3.1, §4.1), owner the Product Owner." The PF07-derived sentence before it is unchanged |
| D-5 | Plan v1.1 §7 WU-OPS-01, **External execution classification**: "Hosted-service operation (deployment or redeploy of the accepted commit; read of `/internal/version`; presence-only probe of the bindings)." | Replace with: "Hosted-service operation (read of `/internal/version`; presence-only probe of the bindings; a redeploy of the previously deployed commit only under the rollback intent). The candidate is deployed by its commit landing on `main`, not by this task." "No vendor call, no database write." is unchanged |
| D-6 | Plan v1.1 §11, the R-9 row | Risk: "Removed: the deploy source is known; the candidate reaches the service when its commit lands on `main` (Product Owner direction of 2026-10-21)." Unit and Treatment: "—" |
| D-7 | Delta §1 ("WU-OPS-01 verifies the candidate's `release_id` at `1.3.0` and records the live start command"); §4 "Ops" row; §8 row "The live Railway start command, a stated limit and not a blocker" | §1 and §4: WU-OPS-01 verifies the candidate's `release_id` at `1.3.0` after its commit lands on `main`, and records no trigger, build command or start command. §8: the row is removed; the start-command question is closed by the Product Owner's direction (this review §2). Add the Glow Infrastructure doc-delta candidate for the deploy source as an unresolved item, owner the Product Owner. **Author states** one conflict row recording that the direction supersedes assessment v1.1 P-9's start-command parts and discharges the Specification delta 01 addendum's WU-OPS-01 obligation, as §2 here states |
| D-8 | Delta front matter, §8 return point; application report | The revision is `artifact_version: "1.1"`, with v1.0 as its predecessor and this review as its denial lineage. The application report adds D-1 to D-7, each applied once at its anchor, and records that A-7's reviewer note is answered by D-3. Everything outside D-1 to D-8 is carried unchanged from v1.0 |

## 5. Effects

| Area | Effect |
| :- | :- |
| WU-OPS-01 | Smaller: identity proof by `/internal/version` and the presence-only binding probe. No Railway settings discovery |
| WU-PR-08, WU-DOC-01, release identity, QA | Unchanged from delta v1.0 |
| Risks | R-9 removed. No other risk changes beyond delta v1.0 |
| PF07 | One doc-delta candidate (deploy source), owner the Product Owner. No canon edit |

## 6. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The revised delta v1.1 and its application report (§4) | The whole-change Implementation Agent, IA-40 |
| Review of the revised delta | Isis, IA-30 `MATERIAL_PLAN_DELTA_REVIEW` |
| The HDE Build Notes addendum for the approved delta | Isis at DELTA_APPROVE; publication by the Product Owner |
| Glow Infrastructure doc-delta candidate: the deploy source (commits landing on `main`) | Product Owner |
| Business cases for WU-DOC-01 and WU-OPS-01 (beneficiary, evidence, benefit, measure), due before DOC-10 and OPS-10 | Product Owner |
| Correction of addendum 2.11's cross-references; PF10 numbering of the Specification delta 01 addendum | Product Owner |

## 7. Return point

DELTA_DENY routes the pending delta and these redlines to IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16), for the same whole-change Implementation Agent (session "HDE-CRD-0002-2"). The revised delta returns to IA-30 `MATERIAL_PLAN_DELTA_REVIEW`, for Isis.

## 8. TypeSafe reading for the receiving session (IA-40 delta revision)

Action sent (v8.2): "Revise, as the whole-change Implementation Agent, a 36 KB standalone pending material delta to an approved 76 KB Implementation Plan that its reviewer has denied once with a short list of exact redlines: rewrite one Ops unit's intent, success criteria, constraints, execution classification and infrastructure-posture passages and one risk row to follow a Product Owner direction that deployments come from commits landing on the main branch, keep every other applied item unchanged, and update the application report. No code is written and no live run occurs; the same reviewer reviews the revised delta before an addendum is issued."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.79 (confidence 0.81); rung probabilities low 0.00, medium 0.25, high 0.71, extra high 0.04, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.88, Sonnet 5.5 0.12, Haiku 5.5 0.00 (confidence 0.84). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.220, Opus 5.5 at high 0.625, Opus 5.5 at extra high 0.035, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.030, Sonnet 5.5 at high 0.085, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T20:32:48Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-21T20:32:48Z; HTTP 200 in 0.5 s; 5459 input and 71 output tokens; jev-1.13.0. Session kind "correction". Rung by rule: high; model by rule: Opus 5.5. No flags.
- **Nathan's pick for IA-40:** not stated. **Nathan's pick for this IA-30 session:** not stated (its reading is in the delta §9).
- **Notion row:** not written (IA-30 handoff rule).

**Surface advice:** run IA-40 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the whole-change Implementation Agent role. It reads from `main` this review, the delta v1.0 and its application report, Plan v1.1, and `docs/pfcanon/` (Glow Infrastructure §2.4, §3.1, §4.1, §10). It writes the delta v1.1 and its application report under `docs/ephemeral/`. It needs no Railway, vendor, production or database access. This review's pull request should be merged first.

## Canon relied on

Read on `main` at `bb263fc`.

| Decision topic | Governing source, sections read |
| :- | :- |
| Review mode, outcomes, materiality, no addendum on deny, routing | IA-30 — Review Whole-Change Implementation Plan — 100926.1, read in full in this invocation: "Material Plan-delta review"; "Qualifying addendum and idempotency"; "Required results and routing"; "Storage and handoff" |
| How an approved Plan changes; scope of reviews and Product Owner dispositions | PF04-Canon-HDE-Governance v2.8.7 §9.1.1 and §9.1.2, as cited by Plan review v1.0 and assessment v1.1; not re-read in this invocation |
| Reviewer's limits; "Author states" | PF27-Canon-Plan-Templates v2.0.5, "Source-bound review authority and exact-fix limits", read for Plan review v1.0; "CI lane classification and automated budget-control discipline", read for assessment v1.1 (no change-detection mechanism invented by the reviewer, P-7) |
| Deployment facts, PF07-gap and PO-provided facts (D-1 to D-6) | PF07-Canon-Glow-Infrastructure v2.3.3, read in this invocation: §0 "PF07 as the required infrastructure source", "PF07-derived and PF07-gap postures", "PS discovery for discoverable infrastructure facts"; §2.4 "Env Deployment Inventory" including "PO-provided deployed environment facts MUST NOT be downgraded to `OPEN/TBD`"; §3.1 Railway; §3.3 GitHub; §4.1 HD Engine; §10 "Service start declarations" (10.1, 10.4). Searched all of `docs/pfcanon/` for deploy triggers, auto-deploy and deploy-from-commit: no PF document states the deploy source. Glow Infrastructure records the live start setting as unverified (§10) and the build artifact as TBD (§4.1). The Product Owner's direction (§2) fills that gap |
| PF10 | PF10-HDE-Build-Notes v13.7.1: front matter §5 "Individual-addendum supersession" and §9 "Operational rule for agents", read in full in this session's read-in; addendum 2.11 rules 1 to 8, read in full; addendum 2.18 "Requirements and work units carry no cost ceiling; work continues until it is done", located in v13.7.1 and read in full from its record (#680); the Addendum Index. Addenda 2.6 to 2.10 at their WU-PR-08 items are as assessment v1.1 read them |
| The Specification delta 01 addendum | Read in full from its record `docs/ephemeral/HDE-CRD-0002-specification-delta-01-PF10-build-notes-addendum-v1.0.md`, and treated as in force |
| CI facts (P-7) | `AGENTS.md` "HDE-EPIC039 current workflow posture"; `ci/checks/classify_ci_changes.py`, run on `bb263fc` (§3) |

**In-flight documents read in full:**
- the delta v1.0 and its application report;
- change assessment v1.1 (this reviewer's own) and the IA-40 return record;
- the Specification delta 01 and its addendum record;
- the no-ceiling addendum record;
- the WU-PR-08 decision record.

**Read in part:** Plan v1.1: §3, §7 WU-PR-08, WU-DOC-01 and WU-OPS-01 in full, §9 to §15, and every anchor of P-1 to P-17 and D-4 to D-6.

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-30 / material Plan delta review 1 (delta 01 v1.0) |
| change | CRD HDE-CRD-0002 |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis / IA-30 MATERIAL_PLAN_DELTA_REVIEW |
| capture time | 2026-10-21T20:40:00Z |
| execution identity | https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok |
| repository persistence | recorded here only |
