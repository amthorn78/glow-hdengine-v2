---
artifact_type: PLAN_REDLINE_APPLICATION_REPORT
artifact_version: "1.0"
logical_id: HDE-EPIC041-IMPLEMENTATION-PLAN-V1.1-APPLICATION-REPORT
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
result: PLAN_PENDING_REVISED
authoring_mode: PREAPPROVAL_PLAN_REVISION
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
revised_plan: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1, PLAN_PENDING_REVISED, ASK OK?)
denied_plan: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.0.md (v1.0, 31,508 bytes, git blob cd91e2e99325b1fe2a2f880cf1855e79fe33459c; preserved unchanged)
review: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.0.md (IA-30 INITIAL_DENY, RL-1 to RL-8; merged by amthorn78/glow-hdengine-v2#786 as 81d6124f)
author: the same whole-change Implementation Agent for HDE-EPIC041 that authored v1.0 (session https://claude.ai/code/session_01Q789tzq7k4R2cJq4f6UqUj)
reviewer: the same continuing Isis role (Isis-56) at IA-30, INITIAL_PLAN_REVIEW
prompt: IA-40 — Prepare or Revise Whole-Change Implementation Plan — 102726.1 (https://app.notion.com/p/4064590a05eb81a5a137f6912fba26b9; page state 2026-10-27T13:16:58.421Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
repository_head_read: origin/main 81d6124f
authored_at: 2026-10-28 (UTC)
---

# HDE-EPIC041 — Implementation Plan v1.1: redline application report (IA-40)

All eight redlines from IA-30 review v1.0 are applied, each once, to one complete replacement, Plan v1.1. No redline was ambiguous, contradictory or without a unique target, so no `REDLINE_INCOMPLETE` arises. v1.0 is preserved unchanged. The Audit v1.0 is unchanged. Merging this file preserves the record and approves nothing (D21-C).

## Canon relied on

* **PF10.** `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.md`, the unique current controlled PF10. Its blob `cb61644d…` is identical on `b29ca84` and on `81d6124f`. It was read in full (501 lines) for IA-10 in this IA lineage and is unchanged since. Its one addendum, 2.1, does not apply (Audit §1.3). The applicable overlays are therefore NONE, and the base is Specification v1.1.
* **Canon unchanged.** `git diff --stat b29ca84 81d6124f -- docs/pfcanon/` is empty, so every canon section the Plan cites reads as it did for v1.0.
* **Read for this revision:**
  * Change Process Guide §3 "Implementation Plan" (sequencing);
  * Plan Templates §12 "General Implementation Plan (Template)", including "HDE phased accountability", for RL-7;
  * HDE Governance §9.1.1 (same author, same reviewer, complete replacement);
  * HDE Governance §9.7.7 (work-unit business cases), for RL-4;
  * Specification v1.1 §4 items 3 and 4 and "Implementation preservation", against which the RL-1 text was checked;
  * review v1.0 Ruling R-B.
* **In-flight documents read in full:**
  * IA-30 review v1.0;
  * Plan v1.0;
  * the IA-40 Notion page;
  * the IA-40 boundary: "Apply only the supplied IA-30 redlines", "preserve unaffected content".

> Applicable, active, non-superseded PF10 addenda supersede conflicting PF-Canon only for the exact scope they address; otherwise follow PF-Canon. A formally approved bounded Product Owner rescope may supersede conflicting PF-Canon only for the exact decision it adjudicates.

## 1. Method

* **Anchors.** Each anchor was confirmed to occur exactly once in v1.0 (count 1 for all 16 anchor lines).
* **Application.** The edits were applied by one scripted pass of exact line replacements and insertions, with no hand-typed redline text. A line inserted or replaced keeps the nesting level of the line it replaces or follows, which is the indentation rule review v1.0 §3 states for RL-2.
* **Result check.** Each redline's new text was confirmed to occur exactly once in v1.1. Each replaced v1.0 text was confirmed absent.

## 2. Item-by-item application

| Redline | v1.0 target (anchor) | Operation | Applied in v1.1 | Check |
| :- | :- | :- | :- | :- |
| RL-1 | §11, bullets `* **Item 3.**` and `* **Item 4.**` | Replace both | Yes, as written | Both now quote Specification §4 items 3 and 4 in full, including "No exemption or non-vendor substitute then applies. Closed-rails proof, … does not replace it." and "This Specification records no exemption …". The lead-in and **Audit determination** are unchanged |
| RL-2 | §5.3 **Orchestration entry**, sub-bullets `* Signature:`, `* It accepts the positional form`, `* Any other argument shape raises` | Replace the three | Yes, as written. The second sub-bullet's two nested form lines sit one level deeper | Signature `load_chart(*args, **kwargs) -> dict`; the two accepted forms; `TypeError` for the legacy-routed shapes, the one intended change |
| RL-2 linked 1 | §5.2 I-4, sub-bullet ``error `code` and `details.field` keep today's values;`` | Replace | Yes | Now covers message and names the one intended change |
| RL-2 linked 2 | WU-PR-01 orchestration tests, ``a bad argument shape → `TypeError`;`` | Replace | Yes | Includes each legacy-routed shape and a no-argument call |
| RL-3 (a) | WU-PR-01 **Tests and evidence**, `* A characterization test proving` | Replace | Yes | Its own file; run from the root; `_Path` patched; clean tree |
| RL-3 (b) | WU-PR-01 orchestration tests, `* a run from a temporary CWD validates the same as a run from the root.` | Insert after, same level | Yes | Literal-value assertions of the O-03 dict and the §5.3 codes, fields and messages |
| RL-3 (c) | WU-PR-02 **Scope**, bullet ending `No shim is kept.` | Insert after, same level | Yes | Characterization test deleted with the module; new `tests/retired_tests.md` row; removed from `pytest.ini` and the roster; row 57 unchanged |
| RL-3 (d) | WU-PR-02 guard sub-bullet `* a negative self-test on a synthetic source.` | Insert after, same level | Yes | The guard's exclusions are limited to its own file and its synthetic source |
| RL-4 | WU-PR-01 business case, `* *Benefit:* chart validation becomes` | Replace | Yes, as written | The tracked-file benefit is attributed to WU-PR-02 |
| RL-5 | §5.2 `* **I-1.**` | Replace | Yes, as written | Reuse of the two pure helpers allowed; the other functions named; fresh-interpreter test scope stated |
| RL-6 | WU-PR-01 **Acceptance and evidence**, `green, or a recorded valid waiver` | Replace | Yes, as written | "No CI waiver exists for HDE-EPIC041". WU-PR-02 inherits it through "Exact-head CI as WU-PR-01" |
| RL-7 | §7, after row `| D5 close baseline |` | Insert | Yes, as written | The phased accountability table with four rows follows the traceability table |
| RL-8 | WU-PR-02 **Scope**, `Re-run the Audit §5.2 inventory search` | Replace | Yes, as written | Scope and pattern embedded |

The review §3.3 nits N-1 to N-4 are not redlines and were not applied, as the review permits.

## 3. Changes no redline states

These are lineage and record-currency changes only, of the kind the prompt requires for a version advance. None changes a requirement, work unit, invariant, interface, test, dependency, risk, exclusion or conflict-register treatment.

* **Front matter.**
  * `artifact_version` is now "1.1".
  * `state` is now `PLAN_PENDING_REVISED`.
  * `prompt` is now IA-40, with v1.0's IA-10 origin kept.
  * Added: `authoring_mode`, `supersedes`, `review_ref` and `application_report`.
  * `r1_row` reads GCF-12.
  * `repository_head_planned_against` and `authored_at` record both versions.
* **Title.** Now "Plan v1.1 (GCF-10, revised under GCF-12)".
* **Opening paragraph.** Now names v1.1 as the replacement and points to this report.
* **§1.** "Revision" reads 1.1.
* **§15.**
  * The TypeSafe reading is now the one for the IA-30 re-review (below). v1.0's reading stays in v1.0.
  * The surface advice adds the inputs the re-review needs (v1.1, this report, v1.0, review v1.0) and notes that a diff of v1.0 against v1.1 is the fastest check.

## 4. TypeSafe reading and surface advice for the receiving IA-30 session

This is the same text as Plan v1.1 §15.

* **Method.** Installed scoring skill, request v8.2, script run once, session kind `review`, label "HDE-EPIC041 IA-30 Implementation Plan re-review". No Notion row was written.
* **Action sent (v8.2).** "Re-review one revised pending whole-change Implementation Plan of about 36 KB that was reviewed once and denied, checking against an item-by-item application report that eight exact redlines the reviewer wrote were applied: three blocking ones rewrite the open-rails quotation, the orchestration entry's argument contract and a characterization test's lifecycle across two of its three PR work units, and five are small business-case, invariant, CI-wording, accountability-table and search-pattern changes; the reviewer approves or returns exact redlines. A written prompt with steps exists; no code, test or canon change and no live run against a provider occurs. Per-PR plans, implementation and independent PR reviews follow later in separate sessions."
* **As printed.** **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.95 (confidence 0.89); rung probabilities low 0.00, medium 0.11, high 0.83, extra high 0.06, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 1.00, Sonnet 5.5 0.00, Haiku 5.5 0.00 (confidence 1.00). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.110, Opus 5.5 at high 0.830, Opus 5.5 at extra high 0.060, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.000, Sonnet 5.5 at high 0.000, Sonnet 5.5 at extra high 0.000, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-28T04:11:04Z. Nathan picks the cell.
* **Flags.** None printed.
* **Picks.** Nathan has stated no pick for the IA-30 re-review and none for this IA-40 session, so none is recorded.
* **Surface advice.**
  * Run it in the continuing Isis role's top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, started after this revision's pull request merges.
  * It needs read access to `main` and one branch and pull request under `docs/ephemeral/`.
  * `git diff --no-index` of Plan v1.0 against v1.1 shows exactly the §2 and §3 changes.
  * Not needed: code changes, test runs, open rails, or vendor, Railway, database or Notion writes.

## 5. Next state and nonclaims

* **Plan.** v1.1, `PLAN_PENDING_REVISED`, `ASK OK?`. It returns to the same Isis reviewer at IA-30 in `INITIAL_PLAN_REVIEW`.
* **Open items and owners** (unchanged by this revision):
  * TI-07 / CCR-1: Product Owner.
  * TI-02, items 9 and 10: Product Owner.
  * FND-005 to FND-007: CL-40 and the Product Owner.
  * N-4: QA-10.
* **Nonclaims.** This report and v1.1 establish no approval, PR Instruction, Proceed, implementation, CI result, QA, Ops, acceptance, PF09 or board movement, canon change, PF10 addendum or closure. Nothing outside `docs/ephemeral/` is changed.
