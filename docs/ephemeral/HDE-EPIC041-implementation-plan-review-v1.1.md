---
artifact_type: IMPLEMENTATION_PLAN_REVIEW
artifact_version: "1.1"
logical_id: HDE-EPIC041-IMPLEMENTATION-PLAN-REVIEW
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
review_mode: INITIAL_PLAN_REVIEW (re-review of the pre-approval replacement)
decision: INITIAL_APPROVE
approval_sentinel_result: ASK OK.
approved_artifact: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md
approved_artifact_version: "1.1"
approved_artifact_identity: 37,557 bytes; git blob 2ff65a377ae392396b32707313399fab3bf154e9; SHA-256 dc63d11fda3e8f64cbee3a137de908f16b2f951793cfca3568e7ac9dc5dc284a; on main at 74217b9 (merged by amthorn78/glow-hdengine-v2#787)
approved_artifact_state: PLAN_APPROVED by this decision (the file itself still reads PLAN_PENDING_REVISED / "ASK OK?" as authored; Isis does not edit the IA's artifact, and this decision record is the approval)
application_report_ref: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1-application-report.md (11,156 bytes; git blob 03edf72f6f300dee4d4178e5368a2279ef2fe46b)
predecessor_decision: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.0.md (INITIAL_DENY of v1.0, redlines RL-1 to RL-8; merged as 81d6124, #786)
superseded_artifact: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md (v1.0, denied; preserved unchanged)
implementation_audit: docs/ephemeral/HDE-EPIC041-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; unchanged)
approved_specification: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1; approved by docs/ephemeral/HDE-EPIC041-epic-specification-review-v1.1.md)
plan_author: the whole-change Implementation Agent for HDE-EPIC041 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
reviewer: Isis, the continuing Lead Developer role for HDE-EPIC041 (Isis-56; https://claude.ai/code/session_01Q789u35D8uKpsTHJ67oMCz), the same reviewer that issued review v1.0
prompt: IA-30 — Review Whole-Change Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81ebb110fb0202874d8c; page state 2026-10-27T13:21:07.780Z, read in full, unchanged since review v1.0)
ecosystem_release: GCFPE-20261027.1 / 102726.1 (register "Current selection", as read for review v1.0)
repository_head_read: origin/main 74217b9
reviewed_at: 2026-10-28
pf10_addendum: NONE (INITIAL_APPROVE produces zero PF10 addenda)
next_prompt: PR-10 — Create PR Work-Unit Instructions — 102726.1
next_work_unit: WU-PR-01
next_actor: the same whole-change Implementation Agent for HDE-EPIC041
---

# HDE-EPIC041 — Implementation Plan review (IA-30), re-review of v1.1: INITIAL_APPROVE

## 1. Decision

**INITIAL_APPROVE** of `docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md` v1.1, the exact artifact identified in the front matter.

* All eight redlines from review v1.0 are applied as written, each at its anchor and nesting level.
* No requirement, work unit, invariant, interface, test, dependency, risk, exclusion or conflict-register treatment changed except as those redlines direct.
* Every element accepted in review v1.0 §4 is unchanged, including the three work-unit business cases.
* No new blocker is raised. This is a diff-first loop, and the full gate set was applied to v1.0 (Plan Templates, "Review stability and no-moving-target discipline").

What this approval does and does not do:

* It approves the change-wide method for HDE-EPIC041: three ordered PR work units, no Ops.
* It produces zero PF10 addenda.
* It is not a PR Instruction, a per-PR Plan, a Proceed, implementation, CI, QA, Ops, acceptance, PF09 movement or closure.
* The first executable work unit, WU-PR-01, goes to PR-10.

**ASK OK.**

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `74217b9`. `git diff --stat ad662f7 74217b9 -- docs/pfcanon/` is empty, so canon is byte-identical to what review v1.0 read. This branch changes nothing under `docs/pfcanon/`. The search terms are those of review v1.0.

| Document (title; file) | Sections read in full | Decision topic it governs here |
| :- | :- | :- |
| HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`) | §9.7.7 "Plan approval gate" (read in full for review v1.0; unchanged): "Business case for every requirement and work unit", "Severity mapping and review burden", "Template-hygiene materiality rule", "Implementation Plan review boundary" | §2: the work-unit business cases still pass; §3: severity of N-5 |
| HDE Governance | §9.1.1 "Change authority and exact-artifact lineage" | Same IA author and Isis reviewer; complete replacement, prior version preserved; approval applies to the exact artifact reviewed |
| Plan Templates (`PF27-Canon-Plan-Templates-v2.0.6.md`) | §12 "General Implementation Plan (Template)"; "Canon precedence for template use"; "Review stability and no-moving-target discipline" | RL-7 table conforms; gate freeze; provenance class of N-5 |
| HDE Build Checklist — Separation (`PF09.3-…-v1.1.8.md`) | Task HDE-SEPA006 and Subtasks .1 to .3 | RL-7 rows match the exact source headings; sequencing unchanged |
| HDE Build Notes (`PF10-HDE-Build-Notes-v13.9.md`, the current controlled PF10) | Searched by term as for review v1.0; unchanged | Silent on every topic decided here, so permanent canon governs. No applicable active addendum |
| Specification v1.1 (approved, in-flight) | §4 items 3 and 4 and "Implementation preservation" | RL-1 text checked character for character |
| Review v1.1 (CF-E-30, in-flight) | §5 CANON_CONFLICT_REGISTER | CCR-1 to CCR-4 treatment unchanged |
| IA-30 review v1.0 (in-flight) | Whole document | The redlines checked in §3 |
| Plan v1.1 application report (in-flight) | Whole document | §3 cross-check |
| PR-10 — Create PR Work-Unit Instructions — 102726.1 (Notion, page state 2026-10-27T13:19:04.774Z) | "Inputs"; "Resolve the next approved Plan stage"; "Role and task" | Routing: PR-10 takes `IMPLEMENTATION_PLAN_ID`, `PLAN_REVIEW_ID` and exactly one planned `WORK_UNIT_ID` |

Scoped overrides: none. No PF10 addendum and no Product Owner rescope governs any topic decided here.

Silence: canon is still silent on the N-4 question from review v1.0, whether this change's implementation evidence must be governed. It stays with QA-10.

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 2. Work-unit business cases (the IA-30 gate)

| Work unit | Result |
| :- | :- |
| WU-PR-01 | **Passes.** Beneficiary, Evidence and Measure are unchanged. The Benefit now attributes the tracked-file benefit to WU-PR-02 (RL-4), so WU-PR-01's stop condition is its own measure |
| WU-PR-02 | **Passes** (unchanged) |
| WU-PR-03 | **Passes** (unchanged; flow-required by GCF-19) |

## 3. Redline application check

The check is a word-level diff of v1.0 against v1.1 on `main` `74217b9`. Together with the full read of v1.0 for review v1.0, that diff gives an end-to-end read of v1.1. Each inserted line's nesting level was also checked in place.

| Redline | Applied | Check |
| :- | :- | :- |
| RL-1 | Yes, as written | §11 items 3 and 4 now match Specification v1.1 §4 items 3 and 4 in full |
| RL-2 and linked edits 1, 2 | Yes, as written | §5.3 contract; I-4 sub-bullet; the orchestration `TypeError` test |
| RL-3 (a) to (d) | Yes, as written | (a) the characterization test, own file, run from the root with `_Path` patched; (b) literal-value assertions, at the orchestration-test level; (c) deletion, retirement row, `pytest.ini` and roster, in WU-PR-02 Scope after "No shim is kept."; (d) guard exclusions, at guard level |
| RL-4 | Yes, as written | WU-PR-01 Benefit |
| RL-5 | Yes, as written | I-1 |
| RL-6 | Yes, as written | WU-PR-01 Acceptance; WU-PR-02 inherits it |
| RL-7 | Yes, as written | The four-row phased accountability table follows the §7 traceability table |
| RL-8 | Yes, as written | WU-PR-02 Scope embeds the search scope and pattern |

The changes no redline states are front matter, title, opening paragraph, §1 Revision and §15. They match the application report's §3 list and are accepted as lineage and record currency. The nits N-1 to N-4 of review v1.0 were not applied, as permitted.

**N-5 (Nit; introduced by the current revision, through RL-3 (b) and (d)).** The two inserted sub-bullets follow lines that end with a full stop. In both places the list's last item now does not end the list. The meaning is unaffected. The approved base is not edited, so this note travels with this record.

## 4. Next state and routing

* **Plan.** v1.1 is approved by this decision (ASK OK.). It is the immutable approved Implementation Plan for HDE-EPIC041. Any later change goes through IA-30's approved-base routes, never by editing v1.1.
* **First executable work unit.** `WU-PR-01` (Plan v1.1 §6, "WU-PR-01 — Adapter orchestration entry and pure Engine chart interface"; HDE-SEPA006.1 and the interface part of .3).
  * Its dependency is "None. It is first", so it is dependency-ready.
  * WU-PR-02 depends on WU-PR-01 merged and accepted by its PR-40 lineage review. WU-PR-03 depends on WU-PR-02 merged and accepted.
* **Routing.** PR-10 — Create PR Work-Unit Instructions — 102726.1, run by the same whole-change IA, with:
  * `IMPLEMENTATION_PLAN_ID` = Plan v1.1;
  * `PLAN_REVIEW_ID` = this review;
  * `WORK_UNIT_ID` = `WU-PR-01`.
* **PF10 lineage.** Specification v1.1 plus applicable overlays NONE. No addendum is produced.
* **Open items and owners.** None blocks WU-PR-01.
  * TI-07 / CCR-1: Product Owner, as a possible canon change.
  * TI-02, items 9 and 10: Product Owner.
  * FND-005 to FND-007: the CL-40 scan and the Product Owner.
  * N-4: QA-10.
* **TypeSafe reading for PR-10 (WU-PR-01).**
  * Method: installed scoring skill, request v8.2, script run once, session kind `authoring`, label "HDE-EPIC041 PR-10 WU-PR-01 PR instruction".
  * No Notion row was written. This is an executing-flow session, and IA-30 writes only under `docs/ephemeral/`.
  * Action sent (v8.2): "Create a new PR work-unit instruction for the first of three planned PR work units in one approved whole-change Implementation Plan: adding a pure Engine chart validation module and an Adapter-owned orchestration entry for one legacy Python module of about 170 lines, with their tests and CI owner mappings, from the approved Plan's interfaces, invariants and test list. A written prompt with steps exists; no code is changed and no live run against a provider occurs. A per-PR plan, the Product Owner's Proceed, implementation and independent PR reviews follow later in separate sessions."
  * As printed: **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.74 (confidence 0.68); rung probabilities low 0.05, medium 0.27, high 0.58, extra high 0.09, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.53, Sonnet 5.5 0.43, Haiku 5.5 0.02 (confidence 0.37). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.001, Fable 5.1 at medium 0.005, Fable 5.1 at high 0.012, Fable 5.1 at extra high 0.002, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.027, Opus 5.5 at medium 0.143, Opus 5.5 at high 0.307, Opus 5.5 at extra high 0.048, Opus 5.5 at max 0.005, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.022, Sonnet 5.5 at medium 0.116, Sonnet 5.5 at high 0.249, Sonnet 5.5 at extra high 0.039, Sonnet 5.5 at max 0.004, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.001, Haiku 5.5 at medium 0.005, Haiku 5.5 at high 0.012, Haiku 5.5 at extra high 0.002, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Flags: model near tie between Opus 5.5 and Sonnet 5.5. Sent 2026-10-28T04:19:43Z. Nathan picks the cell.
  * Picks: Nathan has stated no pick for PR-10 and none for this IA-30 session, so none is recorded.
* **Surface advice (PR-10).**
  * Run it in the same whole-change IA role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this review's pull request merges.
  * Needs:
    * read access to `main`, including `docs/pfcanon/`, Plan v1.1, this review, the Audit v1.0, Specification v1.1 and the code the instruction names (`engine/charts/loader.py`, `engine/util/input_validators.py`, `adapter/no_io_guard.py`, `tests/core/test_engine_core_purity.py`, `tests/loader/`, `pytest.ini`, `ci/checks/classify_ci_changes.py`);
    * the PR-10 Notion page;
    * write access to one branch and one pull request under `docs/ephemeral/`.
  * Not needed: code changes, test runs, open rails, or vendor, Railway, database or Notion writes. PR-10 writes the instruction only; the dedicated PR-30 session implements after Proceed.

## 5. Nonclaims

This decision approves only the exact Plan v1.1 identified above. It establishes none of the following:

* a PR Instruction, per-PR Plan, Proceed, PR or merge authority;
* implementation, CI, QA, Ops or acceptance;
* PF09 or board movement;
* a canon change, a PF10 addendum or closure.

It does not edit the approved Plan or the Audit. Merging this file preserves the record (D21-C). The approval itself is this decision, not the merge.
