---
artifact_type: EPIC_SPECIFICATION_REVIEW
artifact_version: "1.1"
logical_id: HDE-EPIC041-EPIC-SPECIFICATION-REVIEW
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
review_mode: INITIAL_SPECIFICATION_REVIEW (re-review of the pre-approval replacement)
decision: INITIAL_APPROVE
approved_artifact: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md
approved_artifact_version: "1.1"
approved_artifact_identity: 51,861 bytes; git blob a41b10b58ce9ff26b7999ce33eca5787e9800b28; SHA-256 2fda3254c6417bb5e5db539f4bda3d208bfd21105e7797923d26fbda04154841; on main at 9299724 (merged by amthorn78/glow-hdengine-v2#783)
approval_sentinel_result: ASK OK
approved_artifact_state: SPECIFICATION_APPROVED by this decision (the file itself still reads SPECIFICATION_PENDING / "ASK OK?" as authored; Thoth does not edit Isis's artifact, and this decision record is the approval)
application_record_ref: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1-application-record.md (11,327 bytes; git blob 49ed50417f55f20702516d8355280693161d733c)
predecessor_decision: docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md (INITIAL_DENY of v1.0, redlines RL-1 to RL-7; merged as 0891314, #782)
superseded_artifact: docs/ephemeral/HDE-EPIC041-epic-specification-v1.0.md (v1.0, denied; preserved unchanged)
kickoff_ref: docs/ephemeral/HDE-EPIC041-epic-specification-kickoff-v1.0.md (KICKOFF_READY; #780)
class_selection_ref: docs/ephemeral/HDE-EPIC041-change-class-selection-v1.0.md (CLASS_SELECTED, EPIC; #779)
reviewer: Thoth (Thoth-20; https://claude.ai/code/session_01Q789u24G3yiuVFFZofiVfx), the same continuing Thoth reviewer that issued review v1.0 (HDE Governance §9.1.1)
author_of_approved_artifact: Isis (v1.0 Isis-55; v1.1 Isis-56, the same continuing Isis role)
prompt: CF-E-30 — Review and Approve Epic Specification — 102726.1 (https://app.notion.com/p/4064590a05eb81a88f00d49a698027bb; page state 2026-10-27T13:21:53.464Z, read in full, unchanged since review v1.0)
ecosystem_release: GCFPE-20261027.1 / 102726.1
repository_head_read: origin/main 9299724
reviewed_at: 2026-10-28
pf10_addendum: NONE (initial approval emits no PF10 addendum)
next_prompt: IA-10 — Create Whole-Change Implementation Audit and Plan — 102726.1
next_actor: the dedicated whole-change Implementation Agent for HDE-EPIC041 (not yet bound)
---

# HDE-EPIC041 — Epic Specification review (CF-E-30), re-review of v1.1: INITIAL_APPROVE

## 1. Decision

**INITIAL_APPROVE** of `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md` v1.1, the exact artifact identified in the front matter. The approval sentinel result is **ASK OK**.

* All seven redlines from review v1.0 are applied as written, and no stale reference to the removed R-05 or AC-06 remains.
* Every requirement now has a business case that meets HDE Governance §9.7.7 and Plan Templates §2.
* The Epic-level Business Case carries every item §9.7.7 lists.
* Every element accepted in review v1.0 §4 is unchanged.
* No new blocker is raised. This is a diff-first loop, and the gate set was applied in full to v1.0 (Plan Templates, "Review stability and no-moving-target discipline").

What this approval does and does not do:

* It authorizes the Implementation Audit and Implementation Plan preparation only, not implementation (HDE Governance §9.1.1).
* It creates no PF10 addendum.
* It approves no Implementation Audit, Plan, PR, Proceed, Ops, QA, PF09 movement or closure.
* An approved Specification never ends the flow. The next step is IA-10.

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `9299724`.

* `git diff --stat 34445a3 9299724 -- docs/pfcanon/` is empty, so the canon is byte-identical to what review v1.0 read.
* This branch changes nothing under `docs/pfcanon/`.
* Search terms are those of review v1.0, plus: re-review, review stability, gate freeze, redline application, canon conflict register.

| Document (title; file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §9.7.7 "Plan approval gate": "Business Case section required (Epic Specifications)", "Business case for every requirement and work unit", "Template-hygiene materiality rule", "Severity mapping", "Specification review boundary" (read for review v1.0; unchanged) | §2: business cases of the Epic and of R-01 to R-04; severity of the Nits in §4 |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" | Same author and reviewer; the replacement is complete and the prior artifact preserved; approval applies to the exact artifact reviewed; approval authorizes Audit and Plan preparation only |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | §2 "Epic Record Template (Normative)", Business Case and "Requirement and work-unit business case"; "Canon precedence for template use"; "Review stability and no-moving-target discipline" (read in full for this re-review); "Redline bundle construction discipline" | §2 and §3: RL-4 and RL-5 applied, gate freeze, blocker provenance classes |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks .1 to .3 | RL-3: every R-05 source obligation is still carried, by R-01 (SEPA006.1, "Do not introduce fallback data or an additional Engine I/O carve-out"), by R-03 (SEPA006.2, "Preserve governed caller output and failure behavior") and by the §8 obligation (Task, "Deliverables and required evidence") |
| HDE Schemas and Artifacts; HDE Governance §2.0.19 | As in review v1.0 | Canon conflict register entry CCR-1 |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.md`, the current controlled PF10) | Searched by term again; the one active addendum (S19 routed security findings) as in review v1.0 | Silent on this Epic's topics, so permanent canon governs every decision here. Its S19 decisions bear only on CCR-3 |
| Review v1.0 (in-flight, `docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.0.md`) | Whole document | The redlines checked in §3; Rulings R-A to R-C, which this decision keeps unchanged |
| Application record (in-flight, `docs/ephemeral/HDE-EPIC041-epic-specification-v1.1-application-record.md`) | Whole document | §3 cross-check; its §6 observation, decided in §4 |
| IA-10 — Create Whole-Change Implementation Audit and Plan — 102726.1 (Notion, page state 2026-10-27T13:16:07.631Z, read in full) | "Entry modes and inputs: FIRST_ENTRY" | The receiver contract: this decision records the `CANON_CONFLICT_REGISTER` (§5) and the IA binding state (§6) |

Scoped overrides: none. No PF10 addendum and no Product Owner rescope governs any topic decided here.

Silence: canon is silent on one question, whether a tokenless Epic still needs an acceptance map. It stays reported, not resolved (CCR-1).

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Business-case check on v1.1 (the blocking gate)

| Item | Beneficiary | Evidence | Benefit | Measure | Result |
| :- | :- | :- | :- | :- | :- |
| Epic Business Case (§2.1) | Delivery team; Glow-user and production-operator impact explicitly not observed or claimed | E-1, E-2, E-3 | Risk reduction: a broken call path and a test-time mutation of a tracked file removed | "What success looks like", checked by AC-01 to AC-05 | **Passes.** All seven §9.7.7 items are present; "If not done" was added by RL-1b |
| R-01 | Delivery team | E-1, E-2 (observed defects); E-4 only locates the concerns | Stated as risk: no tracked-file write, and no Engine path calling a method the default provider lacks | AC-01; AC-05's tracked-files limb | **Passes.** It now rests on observed defects, not on conformance to canon |
| R-02 | Delivery team | E-2, E-4 | As accepted in review v1.0 | AC-02, AC-05 | Passes (unchanged) |
| R-03 | Delivery team | E-1, E-3, E-5 | As accepted. The appended preservation sentence is a constraint covered by R-03's own case: a migration that changed caller output would not close the E-1/E-3 defect cleanly | AC-03, AC-05 | Passes |
| R-04 | Delivery team; QA | E-2, E-3 | As accepted | AC-04, AC-05 | Passes (unchanged) |
| R-05 | — | — | — | — | Removed by RL-3. Its obligations are carried as constraints and a governed-evidence obligation, so none is lost (Canon relied on, PF09.3 row) |

## 3. Redline application check

Checked by a word-level diff of v1.0 against v1.1 on `main` `9299724`. That diff, together with the full read of v1.0 for review v1.0, gives an end-to-end read of v1.1. Each item was also searched for directly in v1.1.

| Redline | Applied | Check |
| :- | :- | :- |
| RL-1a | Yes, as written | The §2.1 Problem-statement sentence was replaced exactly |
| RL-1b | Yes, as written | The "If not done" bullet sits directly after "Why now" |
| RL-2 | Yes, as written | The §2.4 R-01 row matches the redline text |
| RL-3 (items 1 to 11) | Yes | The R-05 rows are gone from §2.4 and §3, and the AC-06 row from §3. The R-01 and R-03 sentences are appended. AC-05 binds R-01, R-03 and R-04. The §8 obligation sentence is present. Both §8 ranges read "AC-01 to AC-05". The D4 heading reads "R-04". §4 reads "(R-03)". A search of v1.1 finds no `AC-06`; the only `R-05` is the §13 nonclaim describing RL-3 |
| RL-4 | Yes, as written | The precedence block quote follows the §0 canon table |
| RL-5 | Yes, all three | No "addendum 2.1" remains. The §0 file identity "v13.9" is kept, as permitted |
| RL-6 | Yes, as written | The TI-02 Scope sentence is present |
| RL-7 | Yes, as written | The TI-03 Scope sentence is present |

The changes no redline states are front matter, §0 lineage and canon rows, and the §13 rewrite. They match the application record's §3 list. None changes a requirement, criterion, exclusion, posture or tracked-issue disposition. They are accepted as lineage and record currency.

## 4. Non-blocking observations

Every observation is classed by the Plan Templates review-stability provenance classes. None blocks approval, and none is a redline. An approved base is not edited, so these travel to the Implementation Audit as context through this record.

* **N-1 (Nit; introduced by the current revision, through RL-1a).** The §2.1 Problem statement now names E-1 and E-2 twice: the RL-1a sentence, then the retained "Two defects are observed …" sentence. Meaning and evidence are unaffected.
* **N-2 (Nit; previously visible, not raised in review v1.0).** TI-07's disposition cell still reads "Thoth to confirm the reading". Ruling R-A confirmed the reading, and v1.1 §13 records that, so the current state is clear. It is not raised as a blocker, under the gate-freeze rule.
* **N-3 (Caveat; newly supplied input, the application record §6).** `.audit_src/` also holds a copy of the loader itself (`.audit_src/engine/charts/loader.py`), `.audit_src/adapter/http_reader.py` and an archived `server/app.py`. Both of the first two were confirmed tracked by `git ls-files` on `9299724`. No Specification change is needed, for two reasons:
  * TI-03 already places the complete caller inventory, beyond the paths searched, with the Implementation Audit;
  * R-03 keeps historical audit captures unchanged.

  The Implementation Audit inventories these paths with the RL-7 copies and classifies each one as a supported caller or as a historical audit capture.

## 5. CANON_CONFLICT_REGISTER (for IA-10 FIRST_ENTRY)

The Specification records its conflicts in §11 (TI-02, TI-07). This register records each one with Thoth's decision.

| ID | Conflict or tension | Sources | Decision for this Epic | Owner of any change |
| :- | :- | :- | :- | :- |
| CCR-1 | Is an acceptance map required for tokenless work? | Plan Templates Preflight B (an unconditional minimum) against HDE Governance §2.0.19 and HDE Schemas and Artifacts' "legacy token compatibility shape" clarification | No operative conflict: Preflight B is the "separate current scoped requirement" §2.0.19 allows. The Specification lists the acceptance map with no token roster (Ruling R-A). TI-07 stays Open | Product Owner (possible canon change); no canon edited |
| CCR-2 | Epic Business Case content lists differ | HDE Governance §9.7.7 (seven items, including "If not done") against the Plan Templates §2 list (eight items, without "If not done") | No operative conflict for this Epic. v1.1 satisfies both lists | None needed for this Epic |
| CCR-3 | Possible reach of HDE Build Notes' S19 decisions into the new orchestration path | HDE Build Notes (decisions on vendor route selection and on the production vendor override scope) against the Specification's "adjacent" reading | Conditional. If the Adapter-owned orchestration entry performs resolver-selected vendor acquisition, those decisions govern that path (TI-02, RL-6) | Implementation Audit determines applicability |
| CCR-4 | PF09.3's Task notes cite a Build Notes record of the loader defect that is no longer in the current PF10 | PF09.3 Task HDE-SEPA006 notes against HDE Build Notes, current file | No conflict. PF09.3 states the defect in full. The Specification records that no gap results (§5) | None |

## 6. Next state

* **Specification:** v1.1 is approved by this decision (ASK OK) and is the immutable approved base for HDE-EPIC041. Any later change goes through the approved-base routes of CF-E-30, never by editing v1.1.
* **IA binding state:** no whole-change Implementation Agent is bound yet. IA-10 FIRST_ENTRY binds one. The Isis reviewer for IA-30 is the continuing Isis role.
* **Denied or unavailable access facts:** none.
* **Open items and owners:**
  * D-1 / TI-01: Product Owner. IA-10 needs it for the Plan.
  * TI-02 to TI-06 and N-3: the Implementation Audit.
  * TI-07 / CCR-1: report to the Product Owner.
* **TypeSafe reading for IA-10.**
  * Method: installed scoring skill, request v8.2, script run once, session kind `authoring`, label "HDE-EPIC041 IA-10 Implementation Audit and Plan". No Notion row was written.
  * Action sent (v8.2): "Create a new whole-change Implementation Audit and then a new initial Implementation Plan for one approved Epic Specification: one task with three subtasks, four requirements and five acceptance criteria, correcting the Engine/Adapter boundary of one legacy Python module of about 170 lines and its few callers, by inspecting the current repository for every requirement and then ordering a small number of PR work units with dependencies and business cases. A written prompt with steps exists; no code is changed, no test is required to run and no live run against a provider occurs. The Plan is reviewed independently afterwards, and implementation follows later in separate sessions."
  * As printed: **TypeSafe v8.2: Opus 5.5 at high.** Effort score 2.10 (confidence 0.84); rung probabilities low 0.00, medium 0.07, high 0.77, extra high 0.15, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.08, Opus 5.5 0.59, Sonnet 5.5 0.32, Haiku 5.5 0.01 (confidence 0.45). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.006, Fable 5.1 at high 0.062, Fable 5.1 at extra high 0.012, Fable 5.1 at max 0.001, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.041, Opus 5.5 at high 0.454, Opus 5.5 at extra high 0.088, Opus 5.5 at max 0.006, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.022, Sonnet 5.5 at high 0.246, Sonnet 5.5 at extra high 0.048, Sonnet 5.5 at max 0.003, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.001, Haiku 5.5 at high 0.008, Haiku 5.5 at extra high 0.002, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T03:22:05Z. Nathan picks the cell.
  * Flags: none printed.
  * Picks: Nathan has stated no pick for IA-10 and none for this CF-E-30 session, so none is recorded.
* **Surface advice (IA-10):**
  * Run it in a dedicated top-level Claude Code cloud session for the whole-change IA role on `amthorn78/glow-hdengine-v2`, started after this decision's pull request merges.
  * Needs:
    * read access to the whole repository on `main`, including `engine/`, `adapter/`, `scripts/`, `tests/`, `.audit_src/`, `ci/`, `pytest.ini` and `docs/pfcanon/`;
    * the IA-10 Notion page;
    * write access to one branch and one pull request under `docs/ephemeral/`.
  * Local read-only inspection commands are useful for the Audit, such as `git grep` and `git log` for TI-05's commits on an unshallowed clone. Running the two retained-coverage tests (TI-04) under closed rails is optional.
  * Not needed: production, vendor, Railway or database access, Notion writes, or any open-rails run.

## 7. Nonclaims

This decision approves only the exact Specification v1.1 identified above. It establishes none of the following:

* an Implementation Audit, Plan, PR, Proceed or merge authority;
* Ops, QA or acceptance;
* PF09 or board movement;
* a canon change, a PF10 addendum or closure.

It does not edit the approved artifact. Merging this file preserves the record (D21-C). The approval itself is this decision, not the merge.
