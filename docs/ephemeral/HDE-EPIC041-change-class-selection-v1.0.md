---
artifact_type: CHANGE_CLASS_SELECTION
artifact_version: "1.0"
logical_id: HDE-EPIC041-CHANGE-CLASS-SELECTION
change_id: HDE-EPIC041
change_class: EPIC
epic_name: Separation Pass 4
state: CLASS_SELECTED
selected_by: Nathan / Product Owner
producer: Master Scrum (https://claude.ai/code/session_014G3ZYHihBTaXjPP5yrEC1N)
prompt: CF-PO-10 — Record Product Owner Change-Class Selection — 102726.1 (https://app.notion.com/p/4064590a05eb81809a74c181d50922eb; page state 2026-10-27T13:22:27.779Z, read in full)
ecosystem_release: GCFPE-20261027.1 / 102726.1
entry_mode: EVIDENCED_SELECTION_RECORDING_OR_RECOVERY
recorded_at: 2026-10-28T02:40:00Z
repository_head_read: origin/main de27c356d0aca222dd1182ef452cef671d27dde2
source_ref: docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md, Task HDE-SEPA006 and Subtasks HDE-SEPA006.1 to HDE-SEPA006.3 (blob 8b2dbf49081ea53690efa9b8eb7d8d493e8614e9; 89,754 bytes)
pf09_phase: Separation (Phase III), PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.8
next_prompt: CF-E-10
next_actor: Master Scrum
---

# HDE-EPIC041 — Change-class selection record

## 1. Result

| Field | Value |
| :- | :- |
| State | `CLASS_SELECTED` |
| Change | `HDE-EPIC041`, "Separation Pass 4" |
| Class | `EPIC` |
| Selected by | Nathan / Product Owner |
| Mode | `EVIDENCED_SELECTION_RECORDING_OR_RECOVERY`: the Product Owner's explicit decision is recorded; nothing is chosen here |
| PF09 phase | Separation (Phase III), PF09.3 v1.1.8 |
| Planned work | HDE-SEPA006 and HDE-SEPA006.1, .2 and .3 (§3) |
| Route | CF-E-10 — Prepare Epic Specification Kickoff Handoff — 102726.1 |

## 2. Selection evidence (verbatim, Product Owner)

Given in this session:
- **2026-10-28.** "Yes, run CF-PO-10 with PF09.3. This will be HDE-EPIC041, Separation pass 4".

  It answered Master Scrum's statement of the scope earlier in the same session: the next Separation Epic "would be **Separation Pass 4** [...] **HDE-EPIC041** [...] Its scope comes from PF09.3 v1.1.8. The only Separation work not yet Done is **HDE-SEPA006** [...] HDE-SEPA001 to 005 are Done, so Separation Pass 4 would be a small Epic of one task with three subtasks."
- **Earlier in the session.** The Product Owner asked: "Do these CRD items need to be resolved before or after a new Separation EPIC change begins?" The answer was recorded as Master Scrum's judgement, not a canon rule: the Epic may begin first; deciding Candidate CRD Items List items 9 and 10 before its Implementation Audit is advised.

## 3. PF09 planned-work mapping

Read on `main` at `de27c356`: `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.8.md`, version v1.1.8, status Canon, effective 2026-10-26.
- **Phase master status:** **Not Done**.
- **Units:** 39 task and subtask headings.

**Selected: every unit not Done (4).**

| Unit | Title | Source status |
| :- | :- | :- |
| Task HDE-SEPA006 | Non-BodyGraph chart-loader boundary correction | Not done |
| Subtask HDE-SEPA006.1 | Adapter-owned acquisition and pure Engine normalization | Not done |
| Subtask HDE-SEPA006.2 | Supported caller migration | Not done |
| Subtask HDE-SEPA006.3 | Boundary and behavior verification | Not done |

**Not selected: Done and context (35).** HDE-SEPA001 to HDE-SEPA005 and all their subtasks (.1 to .8 as listed in PF09.3) are recorded **Done**. They are context for the Epic, not its scope, and their statuses are preserved unchanged.

**Source facts the mapping carries (PF09.3, Task HDE-SEPA006):**
- "Epic or card: Not selected. This is separate planned product work, not an addition to the closed HDE-CRD-0001 or HDE-CRD-0002 scope."
- "Priority: Required-Now architecture correction."
- The Product Owner is the task's decision owner, including for the legacy chart-loader defect recorded in its notes.

## 4. Checks

| Check | Result |
| :- | :- |
| `HDE-EPIC041` free as a real Epic identity | Yes. It occurs on `main` only in `tests/qa/test_generate_epic_close_pack.py` (a test fixture) and in one HDE-CRD-0002 QA preflight log; no Epic record, board card or PF09 assignment uses it. The highest real Epic is HDE-EPIC040 |
| Identity syntax | Matches `^HDE-EPIC[0-9]{3}$` (`schemas/close_candidate_source.v2.json`; the generic QA identity in `AGENTS.md`) |
| Prior Epic gate (HDE Governance §1.1: an Epic "must be fully implemented, validated, and evidenced before the next Epic begins") | HDE-EPIC040 is closed (`CLOSE` / `CHANGE_CLOSED`, 2026-09-29, PF20 §2.26.1). The Development Board's only non-`DONE` Epic card is HDE-EPIC019, in `PLAN` from the 2026-09-08 import, which PF20 §2.4 records as Done: a stale board row, not an open Epic |
| Existing selection record for HDE-EPIC041 | None (`docs/ephemeral/` on `main` is empty after `de27c35`) |
| Conflicting class claim | None |
| Source read | PF09.3 v1.1.8 §0.4 "Epic and CRD boundary" and the complete Task HDE-SEPA006 section; the status line of all 39 units |

## 5. Constraints and unresolved items

- **This record approves nothing.** Selection "is not downstream approval" (HDE Governance §9.1.1). It approves no Specification, Implementation Plan, work unit or implementation.
- **No PF09 status moves.** Epic formation "preserves the exact phase, eligible inventory, identifiers, and source statuses" (PF09.3 §0.4).
- **Candidate CRD Items List items 9 and 10.** They are open and owned by no change. Item 10(b) FND-022 and item 9 X-03 and R01 touch code near HDE-SEPA006's surface (`adapter/http_reader.py`, `engine/providers/vendor_http.py`, the BodyGraph resolver path). Not decided here; owner: Product Owner. The canon-policy ADR brief for item 9 was merged in #765.
- **`main` CI.** The latest `ci` push run on `main` is still the OBS-17 failure at `1fb4731b` (run 40359063642). That run was the last code push; every later commit on `main` was documentation-only. Owner: Product Owner (Candidate item 10).
- **PF20 is not a source.** PF20 is "Historical reference only. Not for planning". Only its naming sequence was used, for the epic name (Separation Pass 1, HDE-EPIC020; Pass 2, HDE-EPIC022; Pass 3, HDE-EPIC040).

## 6. TypeSafe reading for the receiving session (CF-E-10)

Action sent (v8.2): "Prepare a sanitized Epic Specification kickoff document for one new Epic from one existing class-selection record and one already-reviewed build-checklist source: a single task with three subtasks, about 10 KB of source text, accounting for every source unit and doing a few read-only repository checks. A written prompt with its steps exists; no code, test or canon change and no live run against a provider occurs; an independent Specification author and an independent reviewer follow."

The reading as printed by the script:
- **TypeSafe v8.2: Sonnet 5.5 at medium.**
  - Effort score 1.24 (confidence 0.83). Rung probabilities: low 0.02, medium 0.75, high 0.22, extra high 0.01, max 0.00, ultracode 0.00.
  - Model probabilities: Fable 5.1 0.00, Opus 5.5 0.43, Sonnet 5.5 0.55, Haiku 5.5 0.02 (confidence 0.40).
  - Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.009, Opus 5.5 at medium 0.323, Opus 5.5 at high 0.095, Opus 5.5 at extra high 0.004, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.011, Sonnet 5.5 at medium 0.413, Sonnet 5.5 at high 0.121, Sonnet 5.5 at extra high 0.006, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.015, Haiku 5.5 at high 0.004, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000.
  - **Flags: model near tie between Sonnet 5.5 and Opus 5.5.**
  - Sent 2026-10-28T02:37:37Z. Nathan picks the cell.
- **Which request:** the installed skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "HDE-EPIC041 CF-E-10 kickoff".
  - The script's separate detail line (HTTP status, latency, token counts) was not kept from this session's output. The reading was not repeated to recover it.
  - No Notion row was written.
- **Picks.** CF-E-10: Nathan's pick is not stated. This CF-PO-10 session: not read; Nathan's pick is not stated.

**Surface advice (CF-E-10).**
- **Session.** A top-level Claude Code cloud session for Master Scrum on `amthorn78/glow-hdengine-v2`, started after this record's pull request merges.
- **Access.**
  - Read: `main`, including `docs/pfcanon/` and the code the task names; Notion, for the CF-E-10 page.
  - Write: one branch and one pull request under `docs/ephemeral/`.
- **Not needed.** Notion writes, production, vendor, Railway or database access.

## Canon relied on

Read on `main` at `de27c356`:
- PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.8: front matter; §0.4 "Epic and CRD boundary"; Task HDE-SEPA006 and Subtasks HDE-SEPA006.1 to .3, in full; the status line of every task and subtask.
- PF04-Canon-HDE-Governance v2.8.8: §1.1 (Epic gate); §9.1, "Epic and CRD change lanes"; §9.1.1, the role-table row "Epic/CRD class selection".
- PF20-Reference-HDE-Phased-Epics v1.9.6: its status line ("Historical reference only. Not for planning"); §2.4 (HDE-EPIC019 status); §2.5.1, §2.7.1 and §2.26.1 (Separation naming and HDE-EPIC040 closure).
- PF10-HDE-Build-Notes v13.8.9: "No current addenda"; nothing applies.

Prompts read in full: CF-PO-10 102726.1 and its receiver CF-E-10 102726.1 (page state 2026-10-27T13:22:24.392Z).

In-flight documents: none for HDE-EPIC041 exist. Session context: the Product Owner's statements quoted in §2.
