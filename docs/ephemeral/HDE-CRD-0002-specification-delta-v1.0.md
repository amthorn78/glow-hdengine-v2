---
artifact_type: SPECIFICATION_DELTA
artifact_version: "1.0"
logical_id: HDE-CRD-0002-SPECIFICATION-DELTA-01
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
state: SPECIFICATION_PENDING
approval_sentinel: "ASK OK?"
authoring_mode: APPROVED_BASE_FIRST_DELTA_AUTHORING
author: Isis, Lead Developer and author of the HDE-CRD-0002 Specification (session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
reviewer: Thoth, CF-C-30, APPROVED_BASE_DELTA_REVIEW (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum; reviewer of Specification v1.0 and v1.1 and author of the correction assessment)
prompt: CF-C-40 — Revise CRD Specification — 100926.1 (https://app.notion.com/p/3f44590a05eb81458686cc39d8d98b2a)
prompt_release: GCFPE-20261009.1 / 100926.1
created_at: 2026-10-21T18:31:30Z
repository_head_read: origin/main 9a19c330
immutable_base: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480; reviewed source docs/ephemeral/HDE-CRD-0002-specification-v1.1.md, blob 8a3ef0a8930dcb6f610235ee84d68882bfaa80e1; approved by docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md, INITIAL_APPROVE, 2026-10-12T19:39:51Z). Unchanged by this delta
correction_assessment: docs/ephemeral/HDE-CRD-0002-specification-correction-assessment-v1.0.md (CORRECTION_REDLINE C-1 to C-14; blob f2871aa2d44206feb2c03efc2f7465e6c6149461; landed by amthorn78/glow-hdengine-v2#674 as 9a19c33)
authorizing_decision: docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md (Nathan / Product Owner, 2026-10-21, OPTION 1; blob efc220928f7c313ba5ebabb49b975b624dfbafc2; landed by #673 as bc361f4)
format_owner: PF30.1-Canon-HDE-CRD-Records v0.9.1 §4.2 (Material update) and §7 (CRD record template), as the base's governing format under PF06-Canon-Change-Process-Guide §0.1A
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.9.md (blob c9e598d65dd1e5b39f6a27b5826d1b387e0e8419); searched for "delta", S01, "1.4.0", "re-cut" and WU-PR-08; no addendum governs delta format; addenda 2.11 and 2.12 read in full for the authorizing basis
applicable_prior_overlays: NONE (no approved delta or Specification-overlay addendum exists against this base)
return_phase: IA-30 — Review Whole-Change Implementation Plan — 100926.1, APPROVED_BASE_CHANGE_ASSESSMENT, after DELTA_APPROVE
---

# HDE-CRD-0002 — Specification delta 01 (pending)

This is one pending `SPECIFICATION_DELTA` against the immutable approved HDE-CRD-0002 Specification v1.1.
- **What it is.** It overlays exactly the fourteen changes of Thoth's correction redline C-1 to C-14. It does not replace the base, edit it, or carry its approval state.
- **What it does not do.** It approves nothing and authorizes no Plan change, PR, Ops, QA, canon change, acceptance or closure.
- **How it takes effect.** On `DELTA_APPROVE`, the approved base plus this delta is the current Specification. The reviewer's HDE Build Notes addendum records the approval.

## 1. Summary of the change

| Item | Value |
| :- | :- |
| Authorizing decision | Product Owner OPTION 1, 2026-10-21: remove S01; drop the `1.4.0` version cut and keep the release at `1.3.0`; keep S16 and S17; a member change forces a same-version manifest refresh, not new admission pins |
| Requirements affected | S01 removed (ID kept, marked removed). S16 and S17 regrouped alone in the Coagulation block. No requirement added; no other requirement's scope or acceptance intent changed |
| Exclusions | Bullet 2 replaced (no release version cut). One bullet added (S01 removed, with basis and nonclaim). All other exclusions preserved |
| Constraints | Release members: the last two sentences replaced (same-version refresh). All other constraints preserved |
| Phase structure | Conjunction and Fermentation dependency cells reworded; Coagulation purpose, dependencies and boundary changed; one ordering clause deleted |
| QA posture | The Live QA table's S01 row deleted |
| Material change (HDE CRD Records §4.2) | Yes: approved scope or exclusions; phase structure or completion boundaries; dependency order; QA posture; expected outcome |
| Conflicts | NONE (correction assessment §5) |
| Business case (HDE Build Notes, addendum 2.11 rule 3) | No requirement is added, so the Specification gate has nothing new to test. The reduced WU-PR-08's business case is in the decision record §2, for that unit's PR-10 |

## 2. Approved base plus overlay: the changes

Each row gives the base location, the base text, and the delta text that replaces it. Requirement IDs are not renumbered.
- **"Base text"** quotes `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` exactly, or names an exact anchor.
- **"Delta text"** is the redline's required wording, verbatim except where noted.

| # | Base location | Base text | Delta text |
| :- | :- | :- | :- |
| C-1 | Requirements table, S01 row | `\| S01 \| 5(a), O-12 \| Package every release member with the distribution \| A regular wheel install admits the complete release outside a source checkout \|` | `\| S01 \| 5(a), O-12 \| Removed by the Product Owner's decision of 2026-10-21 (docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md) \| None — not delivered \|` |
| C-2 | Intake, analysis & bounded scope → Bounded scope | "S01 to S22 below. Each is a scope statement with its acceptance intent; the Implementation Plan decides how." | "S02 to S22 below; S01 is removed (Exclusions). Each is a scope statement with its acceptance intent; the Implementation Plan decides how." The redline's replacement covers the first sentence; the second sentence is unchanged |
| C-3 | Intake → Expected outcome | "every acceptance intent S01 to S22 holds on `main`, …" | "every acceptance intent S02 to S22 holds on `main`, …". The rest of the field ("verified by independent QA that includes the production-affecting Live QA minimum (Canon, QA & Build Notes posture); the ordinary Close Gate is available to HDE-CRD-0002 and later changes") is unchanged |
| C-4 | Intake → Affected surfaces | "`code: packaging metadata, the production HTTP adapter and its dev Reader route, …`" | "`code: the production HTTP adapter and its dev Reader route, …`". Only "packaging metadata, " is deleted; nothing else in the field changes |
| C-5 | Exclusions, bullet 2 | "No release re-cut beyond what the in-scope requirements require." | "No release version cut: the release stays at its current version, `1.3.0`, and no new admission version or build time is set (Product Owner decision of 2026-10-21)." |
| C-6 | Exclusions, new bullet placed immediately after bullet 2 | — | "S01 (5(a), O-12), every release member packaged with the distribution, is removed by the Product Owner's decision of 2026-10-21. Basis: production starts the engine from the checkout (`Procfile`: `python -m gunicorn 'adapter.factory:create_app()'`) and CI installs in editable mode, so S01 rests on no real input (HDE Build Notes, real-input rule). Not delivered: a regular wheel install outside a source checkout still does not admit the release." |
| C-7 | Constraints → Release members, from "Those of S01" to the end of the bullet | "Those of S01 (`pyproject.toml`) and S02 (`adapter/factory.py`) are not. Any requirement whose implementation changes a release member forces a manifest re-cut and new admission pins; the Implementation Audit establishes the actual set. The change converges on one coherent re-cut after the member-changing work lands." | "That of S02 (`adapter/factory.py`) is not. Any requirement whose implementation changes a release member forces a manifest refresh at the current version, not new admission pins; the Implementation Audit establishes the actual set." The bullet's first two sentences (45 members; the S07, S08, S10 and S14 loci) are unchanged |
| C-8 | Phase blocks, Conjunction row, Dependencies cell | "Coordinates with the release re-cut where a requirement changes a release member (S07, S10 by observed locus). Where S19 findings touch these surfaces, the Plan orders them coherently" | "Coordinates with a same-version manifest refresh where a requirement changes a release member (S07, S10 by observed locus). Where S19 findings touch these surfaces, the Plan orders them coherently" |
| C-9 | Phase blocks, Fermentation row, Dependencies cell | "Coordinates with the release re-cut (S08, S14 by observed locus)" | "Coordinates with a same-version manifest refresh (S08, S14 by observed locus)" |
| C-10 | Phase blocks, Coagulation row | Purpose "Durable packaging and environment discipline: S01, S16, S17"; Dependencies "S01 converges with the release re-cut"; Completion boundary "S01, S16 and S17 hold on `main`" | Purpose "Durable environment discipline: S16, S17"; Dependencies "None; S16 and S17 change no release member"; Completion boundary "S16 and S17 hold on `main`". Planned work units, status and actual references are unchanged |
| C-11 | The "Recommended ordering" line below the phase blocks | "Recommended ordering, for the Implementation Plan to confirm: S03 to S05 early, so later changes in every block are visible to CI; the release re-cut after all member-changing work lands; S22 before QA; S21 before HDE-CRD-0002's closeout." | "Recommended ordering, for the Implementation Plan to confirm: S03 to S05 early, so later changes in every block are visible to CI; S22 before QA; S21 before HDE-CRD-0002's closeout." |
| C-12 | Canon, QA & Build Notes posture → Production-affecting Live QA minimum table | The row whose Class cell begins "Production-affecting, outside the functional-feature scope; at least one bounded open-rails live step, or an explicit authorized exemption recorded in the QA Plan", Requirements cell "S01", Surface cell beginning "Packaging of the deployed service." | Row deleted. The other three rows (functional-feature class; inherits; not production-affecting) are unchanged |
| C-13 | Closure result → Superseded or rejected scope | "`None`" | "S01, removed by the Product Owner's decision of 2026-10-21 (`docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md`)" |
| C-14 | Material-change history | One row: 2026-10-12, Specification approval | One row appended on approval, as §3 states. The existing row is not overwritten (HDE CRD Records §4.2) |

**Notes on the wording:**
- **C-1.** The decision path appears without backticks inside the table cell, so the base table's pipe structure is kept. The meaning is the redline's.
- **C-2.** The redline quoted only the first sentence of the field. The second sentence stays, as the redline's "Nothing else … changes" pattern applies throughout.
- **C-6.** HDE Build Notes is cited by title alone, as the redline requires (Plan Templates, "Canon precedence for template use").

## 3. Material-change history row added on approval (C-14)

Appended after the base's existing row, which stays unchanged:

| Date | Affected fields | Approved change or deviation | Decision source | Build Notes reference |
| :---- | :---- | :---- | :---- | :---- |
| Set by the delta approval | Approved scope (S01); Bounded scope; Expected outcome; Affected surfaces; Exclusions (bullet 2 replaced; S01 bullet added); Constraints → Release members; phase structure and dependencies (Conjunction, Fermentation, Coagulation, Recommended ordering); Live QA classification (S01 row removed); Superseded or rejected scope | S01 removed; no release version cut, the release staying at `1.3.0` with a same-version manifest refresh for any member change; S16 and S17 kept as the Coagulation block | `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` (Product Owner); `docs/ephemeral/HDE-CRD-0002-specification-correction-assessment-v1.0.md` (Thoth, CORRECTION_REDLINE); the CF-C-30 delta approval of this delta | The HDE Build Notes addendum that delta approval creates |

The date and the addendum reference are filled in by the approval record, not by this pending delta. The row's other cells are fixed here. Record control's "Last material update" follows the same approval.

## 4. Preserved without change

As the correction assessment §3.1 states, and verified against the base:
- **Intake.** Observed need or requested change (it records what was observed at intake); Why warranted; the Lead Developer finding ("CRD lane: yes for S01 to S22", a finding made at intake).
- **Requirements and carried items.** Every requirement other than S01. Every exclusion other than bullet 2, including the "Not reopened" list. Every constraint other than Release members' last two sentences. CD-1 to CD-3, RD-1, and the canon-conflict register CR-1 to CR-3 as carried.
- **Record blocks.** Record control, Specification approval, and Exact-source execution & decision lineage, except as the delta-approval route records them. The kickoff open points U-1 to U-7. The pre-approval revision history.
- **Other phase-block columns.** Planned work units, status and actual references in every phase block.

A search of the base for "S01", "re-cut", "packaging" and "admission pin" finds each occurrence either changed above or preserved here: lines 61, 66, 119, 166, 167, 169, 171, 187 and 236.

## 5. Affected surfaces, dependencies and downstream work

| Area | Effect | Owner and route |
| :- | :- | :- |
| Implementation Plan v1.1 | Needs an approved-base change. The passages are listed in the decision record §3 "Later route": §3 "Release-identity spine"; §6 (the S01 row and "version bump `1.4.0` in WU-PR-08"); §7 WU-PR-08 (title, scope, deliverables, acceptance) and WU-OPS-01's success criterion ("the `1.4.0` `release_id`"); §10; §11 R-2 and R-6; §12; WU-DOC-01's AGENTS.md "release `1.4.0`" line | Isis through IA-30 `APPROVED_BASE_CHANGE_ASSESSMENT`, then the Implementation Agent through IA-40, after DELTA_APPROVE |
| WU-PR-08 | Shrinks to S16 and S17. It changes no release member, so it makes no manifest refresh and triggers no full-validation CI. Business case and ceiling are in the decision record §2 | PR-10 after the Plan change |
| QA Plan (future) | No Live QA step or exemption is needed for S01 | Kronos (QA-50), through QA-10 |
| Release identity | Unchanged rule: `release_id` stays manifest-derived. Version `1.3.0` and its build time stay as the admission constants state | `AGENTS.md` "Release identity" |
| Tests, Ops, documentation | No test, Ops task or document is required by this delta itself | — |

## 6. Unresolved items and owners

| Item | Owner |
| :- | :- |
| The live Railway start setting is unverified (Glow Infrastructure §10). If production ever ran without the checkout, admission would refuse to start (`MISSING_FILE`). This is a stated limit, not a blocker | WU-OPS-01 records the deployment facts; Product Owner |
| The Implementation Plan v1.1 change | Isis (IA-30), then the Implementation Agent (IA-40), after DELTA_APPROVE |
| The HDE Build Notes addendum recording the approved delta | Thoth at DELTA_APPROVE; publication into PF10 by the Product Owner |

## 7. Return phase

- **Now.** This pending delta goes to CF-C-30 — Review and Approve CRD Specification — 100926.1, `APPROVED_BASE_DELTA_REVIEW`, for Thoth.
- **On DELTA_APPROVE.** The affected receiver is IA-30 — Review Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb811db88dece791f1f60c), `APPROVED_BASE_CHANGE_ASSESSMENT`, for Isis as Plan reviewer. The approved delta and the Product Owner decision serve as the authorized material-change request against the immutable Plan v1.1 and its review v1.1.
- **On DELTA_DENY.** The delta returns to Isis in CF-C-40 `APPROVED_BASE_DELTA_REVISION`.

## 8. TypeSafe reading for the receiving session (CF-C-30 delta review)

Action sent (v8.2): "Review, as the same independent Specification reviewer who wrote the correction redline, one new pending Specification delta of about fourteen bounded passages against an already approved 22-requirement CRD Specification: check each passage against the redline and the immutable base, then approve the delta and write one standalone build-notes addendum, or deny it with delta redlines. It is a read-only review of Markdown records against canon: no code and no live run occur, and an Implementation Plan change assessment follows approval."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.33 (confidence 0.71); rung probabilities low 0.00, medium 0.06, high 0.58, extra high 0.34, max 0.02, ultracode 0.00. Model probabilities Fable 5.1 0.01, Opus 5.5 0.96, Sonnet 5.5 0.03, Haiku 5.5 0.00 (confidence 0.95). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.001, Fable 5.1 at high 0.006, Fable 5.1 at extra high 0.003, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.058, Opus 5.5 at high 0.557, Opus 5.5 at extra high 0.326, Opus 5.5 at max 0.019, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.017, Sonnet 5.5 at extra high 0.010, Sonnet 5.5 at max 0.001, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-21T18:31:30Z. Flags: none.
- **Detail:** v8.2 sent 2026-10-21T18:31:30Z; HTTP 200 in 0.72 s; 5441 input and 71 output tokens; jev-1.13.0. Rung by rule: high; model by rule: Opus 5.5.
- **Nathan's pick for CF-C-30:** not stated.
- **Nathan's pick for this CF-C-40 session:** not stated (reading recorded in the correction assessment §6).
- **Notion row:** not written (CF-C-40 handoff rule).

**Surface advice:** run CF-C-30 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the Thoth reviewer lineage.
- It reads from `main`: this delta, the immutable base, the correction assessment, the decision record, and `docs/pfcanon/` (HDE CRD Records §4.2 and §7; current PF10 for the next addendum number).
- It writes the decision and, on approval, one addendum under `docs/ephemeral/`.
- It needs no live vendor, production or database access. This delta's pull request should be merged to `main` first.

## Canon relied on

Read on `main` at `9a19c330`.

- **CF-C-40 — Revise CRD Specification — 100926.1** (read in full on 2026-10-12; page state unchanged since): `APPROVED_BASE_FIRST_DELTA_AUTHORING` inputs; Execute step 3 (one complete pending `SPECIFICATION_DELTA` stating the immutable base, bounded overlay, affected requirements, acceptance and dependencies, preserved exclusions, evidence, conflicts, unresolved items and return phase); the format sentence ("governed by the same canon that governs the base CRD Specification"); routing to CF-C-30.
- **CF-C-30 — Review and Approve CRD Specification — 100926.1** (read in full on 2026-10-21): `APPROVED_BASE_DELTA_REVIEW` inputs and the addendum it creates on approval (§7 return phase).
- **PF30.1-Canon-HDE-CRD-Records v0.9.1:** §4.2 "Material update", read in full (the material categories; append-only history row, for C-14 and §3); §7 (the record template fields the delta touches), read for the base.
- **PF06-Canon-Change-Process-Guide v2.5.4 §0.1A** (a delta Specification uses the applicable governing base format), read for the base.
- **PF04-Canon-HDE-Governance v2.8.7 §9.1.1** (approval applies to the exact artifact; an approved base is not patched in place) and **§9.1.2** (Product Owner dispositions and reviews govern within their scope), read for the base and the reviews.
- **PF27-Canon-Plan-Templates v2.0.5**, "Canon precedence for template use" (HDE Build Notes cited by title in derived text, C-6).
- **PF10-HDE-Build-Notes v13.6.9:** searched for "delta", "S01", "1.4.0", "re-cut" and "WU-PR-08". Addenda 2.11 (rules 1, 3, 4 and 5) and 2.12 (decision 4) were read in full for the authorizing basis; addenda 2.16 and 2.17 were searched, with no decision on S01, `1.4.0` or delta format; addendum 2.1 governs the TypeSafe reading.
- **`AGENTS.md`:** "Release identity" (manifest-derived `release_id`; the admission constants).

**In-flight documents read in full:**
- `docs/ephemeral/HDE-CRD-0002-specification-correction-assessment-v1.0.md`;
- `docs/ephemeral/HDE-CRD-0002-WU-PR-08-po-disposition-scope-v1.0.md` (this author's record);
- `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (the immutable base; this author's Specification).

## Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / CF-C-40 / approved-base first delta authoring 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (immutable base) |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Isis / CF-C-40 APPROVED_BASE_FIRST_DELTA_AUTHORING |
| capture time | 2026-10-21T18:31:30Z |
| execution identity | https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2 |
| repository persistence | recorded here only |
