---
artifact_type: IMPLEMENTATION_PLAN_REDLINE_APPLICATION_REPORT
artifact_version: "1.0"
logical_id: HDE-CRD-0002-IMPLEMENTATION-PLAN-V1.1-APPLICATION-REPORT
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
AUTHORING_MODE: PREAPPROVAL_PLAN_REVISION
author: whole-change Implementation Agent (IA) for HDE-CRD-0002 (Audit and Plan v1.0 lineage, session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah; this revision in execution session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j)
reviewer: Isis, continuing Lead Developer and independent whole-change Implementation Plan reviewer (review v1.0 in session https://claude.ai/code/session_012tPq26JWVhCYZmcqTidpV2)
prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16)
prompt_release: GCFPE-20261009.1 / 100926.1 (register current selection read 2026-10-12)
created_at: 2026-10-12T21:01:00Z
repository_head_read: origin/main ffdba6a77d8101902826bbaed4b4bc72144b8053
denied_artifact: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.0.md (v1.0, PLAN_PENDING, "ASK OK?", blob b0eefc0bd68eb67ee58d667602864c266db18458; matches the review's reviewed_artifact_blob)
review_ref: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.0.md (IA-30 INITIAL_DENY, R1–R4, N1–N6; blob 1a5227b484647ed775b8580786b5b14fb71ebfc5; amthorn78/glow-hdengine-v2#620)
revised_artifact: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1, PLAN_PENDING_REVISED, "ASK OK?")
pf10_addendum: none
---

# HDE-CRD-0002 — Implementation Plan v1.1 application report

This report lists, item by item, how Implementation Plan v1.1 applies Isis's IA-30 review v1.0. It approves nothing. Plan v1.1 is `PLAN_PENDING_REVISED` with `ASK OK?` and returns to IA-30 `INITIAL_PLAN_REVIEW` for the same reviewer, Isis. No PF10 addendum is created. Plan v1.0 is not edited.

**Verification before applying.** The denied Plan's blob on `main` (`b0eefc0`, 61,599 bytes) equals the review's `reviewed_artifact_blob`. The redline set is complete for that version: each of R1–R4 names its target in v1.0, the operation, the replacement or the content to supply, the reason and the linked edits. None is ambiguous, contradictory or unsupported, so nothing returns to the reviewer unapplied. `docs/pfcanon/` is unchanged since `df23bbf` (#614), the same canon the review read.

## 1. Required redlines

| # | Redline (review v1.0 §3) | Applied | Where in v1.1 | How |
| :- | :- | :- | :- | :- |
| R1.1 | §5 IF-10, third cell: explicit-`dev` gate | Yes, verbatim | §5, IF-10 row | Replaced with the review's exact text: served only when `APP_ENV` is explicitly `dev`; unset, empty and every other value, including `test` and `local`, refuse with `ERR_READER_FORBIDDEN` 403; canon cited; `scripts/dev_start_reader.sh` defaults `APP_ENV=dev` |
| R1.2 | §5 IF-6: `/reader` `env_gate` stays `APP_ENV=dev` | Yes, verbatim | §5, IF-6 row | "`/reader` rows' `env_gate` becomes `APP_ENV in {dev,test,local}`;" → "`/reader` rows' `env_gate` stays `APP_ENV=dev`;" |
| R1.3 | §7 WU-PR-03 acceptance (2) | Yes, verbatim | §7, WU-PR-03, Acceptance and verification (2) | First clause replaced with the review's text (served for `APP_ENV=dev`; refused for unset, empty, `test`, `local`, `prod`, `production`, `live` and arbitrary values). The rest of item (2) is unchanged |
| R1.4 | §15: append the S10 explicit-`dev` sentence | Yes, verbatim | §15, final sentence | Appended as given |
| R2.1 | §7 WU-PR-07, Dependencies and order | Yes, verbatim | §7, WU-PR-07, Dependencies and order | Bullet text replaced with the review's text: the ADR draft is this unit's deliverable; the Product Owner decides AQ-1 before merging it; revision to the approved decision before merge (RS-10 where the bounded scope changes); S21 completes before the ordinary Close Gate |
| R2.2 | §9 item 1: insert ", and AQ-1 is decided" | Yes, verbatim | §9, item 1 | Inserted after "WU-OPS-01 is planned (OPS-10) or executed" |
| R2.3 | §9 item 4 | Yes, verbatim | §9, item 4 | "the S21 ADR's approval is a Close Gate prerequisite, not a QA-entry prerequisite;" → the review's text (decided before WU-PR-07 merges, and so before QA-10) |
| R2.4 | §9 item 5 | Yes, verbatim | §9, item 5 | First sentence replaced with the review's text; "(Change Process Guide §3.5.1 "Exceptional closure record"); this Plan does not pre-decide it." kept as "the rest of the item" |
| R2.5 | §11 R-4 row | Yes, verbatim | §11, R-4 | Risk, Unit and Treatment cells replaced with the review's text |
| R2.6 | §13 AQ-1 row | Yes, verbatim | §13, AQ-1 | Effect and Stage deadline cells replaced with the review's text; Decision and Owner cells unchanged |
| R3.1 | §7 WU-PR-07: add a **Terminal-state reachability** bullet after Deliverables, stating (a)–(e) from the IA's own design | Yes, IA-designed content | §7, WU-PR-07, new bullet between Deliverables and Dependencies and order | See §2 below for the design summary and its basis |
| R3.2 | §7 WU-PR-07 acceptance: add item (7) | Yes, verbatim | §7, WU-PR-07, Acceptance and verification (7) | Appended after item (6) |
| R3.3 | §9 item 5: append "The path is the one WU-PR-07 states under Terminal-state reachability." | Yes, verbatim | §9, item 5, final sentence | Appended after the R2.4 text |
| R4.1 | §4 invariant 6 | Yes, verbatim | §4, invariant 6 | "close-pack prefix `CRD-0002`" → "close-pack filename prefix `HDE-CRD-0002` (`audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json`)" |
| R4.2 | §5 IF-3 | Yes, verbatim | §5, IF-3 row | "(`EPIC-NNN` / `CRD-NNNN`)" → "(`EPIC-NNN` for an Epic; the CRD ID itself, `HDE-CRD-NNNN`, for a CRD)" |
| R4.3 | §15 | Yes, verbatim | §15 | "close-pack prefix `CRD-0002`" → "close-pack filename prefix `HDE-CRD-0002`" |

**Linked edits named by the review.**
- R1: "None elsewhere in the Plan." None made. The Audit's S10 "Required behavior" and EC-4 wording about `_dev_admin_gate` semantics stay as written; the review supersedes them for the gate's value set. EC-4's dev-runner default stands and is carried in IF-10.
- R2: §16 `open_question` stays "AQ-1 (Product Owner; non-blocking for review)". It is kept, with "; decided before WU-PR-07 merges" added so the checkpoint agrees with §13. The Audit's §7.2 and §8 AQ-1 deadline text stays as written; the review supersedes it for timing.
- R3: "If the stated design puts any close-run evidence or close-pack byte in hosted CI's output, the unit must change its design." The stated design puts none there (§2 below, (c) and (e)).
- R4: none in the Plan. The Audit's §6 S21 "(`EPIC-NNN` / `CRD-NNNN`)" mapping stays as written; the review supersedes it for the CRD prefix.

A residue search of v1.1 for `CRD-0002_`, `` `CRD-0002` ``, `CRD-NNNN`, `{dev, test, local}`, `dev,test,local`, "Close Gate prerequisite" and "gates reliance" finds no stale occurrence. The one remaining `{dev, test, local, stage, staging}` is IF-1's vendor-override non-production set (HDE-CLI-API-Vendor-Ref §7.1.11), which the review did not touch.

## 2. R3 design (what the new bullet states, and why)

The design rests on facts re-read on `main` at `ffdba6a`:
- `tools/qa/generate_epic_close_pack.py`: `--write` and `--check` both require a clean tree at a tracked HEAD; "existing candidate outputs are not causal inputs"; closed rails are required (`CLOSED_RAILS_REQUIRED`); check mode refuses any mutation (`CHECK_MODE_MUTATION`).
- `tools/evidence/update_evidence_index.py`: indexes earlier close packs as rows (`EPIC022_PRIMARY_ARTIFACTS`, lines 352–362); writes path proofs through `_write_path_proof`; `publish_crd_check_family` shows the transaction-with-in-boundary-verification pattern.
- `.github/workflows/epic-closeout-validation.yml`: `workflow_dispatch` only, `contents: read`, writer `--check` plus read-only evidence checks, and a clean-checkout assertion afterwards.

| R3 element | Stated in v1.1 |
| :- | :- |
| (a) Terminal state | The close report, the manifest and their path proofs at the canonical `HDE-CRD-0002` filenames; the IF-4 close-run family; the Index trio and its companions; and the tracked causal inputs (candidate source and the two docdeltas ledgers). All are committed before hosted validation |
| (b) Ordered transitions | T0 preconditions: the QA verdict and family are on `main`, AQ-1 is decided, and the Product Owner has authorized the close set. T1: authored inputs (C1). T2: writer `--write`. T3: updater write (C2). T4: same-run check set on clean C2. T5: the IF-4 close-run publication by the updater, with in-transaction verification (C3, the terminal state). T6: local re-validation on C3. T7: hosted check-mode validation, then the Product Owner merge. Each transition names its tool, inputs and outputs, and all run under closed rails. Restart rules: a causal-input change restarts at T1; a base change restarts at T2 |
| (c) Actor and venue | The executing agent of the close mutation set, a dedicated top-level close PR session under the Product Owner's authorization, or the Product Owner, in a local clean clone. No close byte comes from, or is written back from, a hosted workflow |
| (d) Bindings, no cycle | The Index indexes the close report, the manifest and the close-run family. The manifest does not bind the Index: the v2 writer refuses as causal inputs the Index trio, sentinels, path proofs, the orientation output, `audit/qa/<change-id>/close/**`, the close-pack outputs and `catalog/manifest.json`, and `key_outputs` carries paths of record without digests. Every edge points toward the Index. The close-run primaries record only T2–T4 against C1 and C2 |
| (e) Hosted CI | The ordinary `test` job at the exact head, and the Product Owner's dispatch of `epic-closeout-validation.yml` on C3. Both run check modes only, write nothing, and record their results on the PR, never in the candidate |

Two points are bounded for the per-PR plan and stated as such in the bullet:
- The candidate-source path `audit/HDE-CRD-0002_close_candidate_source.json` is to be recorded in the ADR.
- If rendering a close-run primary needs a change to `tools/qa/qa_harness.py`, the PR-20 plan names it inside S21's bound.

No other WU-PR-07 deliverable, scope line or interface row changed.

## 3. Non-gating notes (review v1.0 §4)

| # | Note | Applied as an edit | Disposition |
| :- | :- | :- | :- |
| N1 | Same-version manifest refreshes leave several `release_id` values labelled `1.3.0` on `main` | No | No correction required. The Plan already requires each PR result record to name its refreshed `release_id` (WU-PR-03 evidence obligations, §10) |
| N2 | Fix-versus-retire criterion for failing uncovered files of current behavior | No | Carried to the WU-PR-01 PR-20 detailed plan, as the review directs. "Never skip, disable or quarantine a test to get green" stands |
| N3 | §9 item 3 parenthetical "S15 catalog-only after EC-8" | No | No correction required; §6 and Audit §7.4 classify S15 correctly |
| N4 | Override actor principal and sink key | No | Carried to the WU-PR-04 PR-20 plan and the QA Plan; R-3 already carries it |
| N5 | `/aux/narrative` catalog row ahead of the PF12 registration | No | R-7 already records that no catalog conformance is claimed |
| N6 | Stale Notion board card for HDE-CRD-0002 | No | Its owner's. This session writes no Notion row |

## 4. Other edits (state and provenance only)

- Header: the version, state, prompt, mode, predecessor, review reference, report reference, release-selection check, creation time and head.
- A revision note under the title.
- §1: the state token `PLAN_PENDING` becomes `PLAN_PENDING_REVISED`.
- §16: the checkpoint.
- §17: the TypeSafe reading for the IA-30 re-review (below).
- The canon list: an "IA-40 revision reads" paragraph.
- The closing state line.

`ASK OK?` is kept. No requirement, unit, interface, order, risk, exclusion or decision outside R1–R4 changed. A line diff of v1.0 against v1.1 shows changes only at these places and at the R1–R4 anchors.

## 5. Results, unresolved items and owners

- **Result:** `PLAN_PENDING_REVISED`. R1–R4 have each been applied once. Return to IA-30 — Review Whole-Change Implementation Plan — 100926.1, `INITIAL_PLAN_REVIEW`, with the same reviewer, Isis.
- **Tests and validation:** none run. This is a planning artifact; no code or evidence changed.
- **Unresolved:**
  - AQ-1, ADR approval: owned by the Product Owner, due before WU-PR-07 merges.
  - N2 and N4: carried to the respective PR-20 plans.
  - The candidate-source path and any `qa_harness.py` touch: bounded to the WU-PR-07 PR-20 plan.
- **Constraints:**
  - No PF canon edited.
  - No PF10 addendum.
  - No implementation, Ops, QA, PR Instruction or approval is authorized by this revision.

## 6. TypeSafe reading for the receiving session (IA-30 re-review)

Recorded identically in Plan v1.1 §17. The reading was sent once, before either artifact was saved.

Action sent (v6): "Re-review, as the same independent reviewer who denied it once, a revised 75 KB change-wide Implementation Plan (v1.1) and its item-by-item application report, checking that four bounded required redlines were applied exactly and nothing else changed: a dev route's environment gate in two interface rows and one acceptance item, a Product Owner ADR decision moved before one unit's merge across the unit, QA-readiness, risk and decision tables, a new author-designed terminal-state reachability path for a close-pack writer unit (ordered local close-session transitions, evidence-index versus close-manifest bindings and why they form no cycle, check-mode-only hosted validation) plus one end-to-end rehearsal acceptance item, and a canonical close-pack filename prefix in three places; then approve or return redlines. No code is written and no live run occurs; a Product Owner Proceed per PR and independent QA follow."

- **TypeSafe v6: Opus 5.5, high.** Effort score 2.33 (confidence 0.75); rung probabilities low 0.00, medium 0.03, high 0.64, extra high 0.32, max 0.01, ultracode 0.00. Model probabilities Fable 5.1 0.02, Opus 5.5 0.98 (confidence 0.96). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.03, Opus 5.5 at high 0.63, Opus 5.5 at extra high 0.31, Opus 5.5 at max 0.01, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.01, Fable 5.1 at extra high 0.01, Fable 5.1 at max 0.00, Fable 5.1 at ultracode 0.00. Sent 2026-10-12T20:59:06Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T20:59:06Z; HTTP 200 in 0.63 s; 4294 input and 54 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags printed by the script: none.
- **Nathan's pick for IA-30 (re-review):** not stated.
- **Nathan's pick for this IA-40 session:** not stated.

**Surface advice:** as in Plan v1.1 §17. Run IA-30 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the Isis reviewer lineage. It needs:
- a line diff of v1.0 against v1.1;
- review v1.0 §3 and this report;
- for R3, `tools/qa/generate_epic_close_pack.py`, `tools/evidence/update_evidence_index.py` and `.github/workflows/epic-closeout-validation.yml` on `main`;
- `docs/pfcanon/` on `main`.

It needs no live vendor, production or database access. It writes only its review artifact under `docs/ephemeral/`.

## Canon relied on

As listed in Plan v1.1 under "IA-40 revision reads", read on `main` at `ffdba6a`:
- PF04-Canon-HDE-Governance v2.8.7 §9.1.2;
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.6 (`/reader` row);
- PF06-Canon-Change-Process-Guide v2.5.4 §1.0.4–§1.0.6, §3.5.1, §3.5.2.1, §3.5.2.3;
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §1.2 "Close-pack artifacts" and "Change-container compatibility (normative)", and Endpoint Catalog "Reader surface routes and distinct contracts (normative)";
- PF19-Canon-Glow-QA-Guide v3.0.6 "Close-pack truthfulness and same-run execution (normative)" and "Close report requirements";
- PF27-Canon-Plan-Templates v2.0.5 "Materiality-based blocker discipline (required for Epic Specification and Implementation Plan review)";
- PF30.1-Canon-HDE-CRD-Records v0.9.1, CRD ID syntax;
- PF10-HDE-Build-Notes v13.5.2 (addendum 2.1 for §6 only; silent on R1–R4).

**Prompt:** IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1.

**Register:** GCFPE Membership and Release Register, current-selection section.

## 7. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / IA-40 / preapproval plan revision 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (from v1.0) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | IA-40 — Prepare or Revise Whole-Change Implementation Plan — 100926.1, https://app.notion.com/p/3f44590a05eb81ca83ecdac0960a6f16 |
| role/stage | whole-change IA / IA-40 `PREAPPROVAL_PLAN_REVISION` |
| capture time | 2026-10-12T21:01:00Z |
| execution identity | https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j |
| repository persistence | recorded here only |
