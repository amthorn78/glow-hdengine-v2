---
artifact_type: CLOSURE_MEMO
artifact_version: "1.0"
logical_id: HDE-EPIC041-CL-20-CLOSURE-MEMO
predecessor: none (first CL-20 output for HDE-EPIC041)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
epic_name: Separation Pass 4
closure_decision: "docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md (CHANGE_CLOSURE_DECISION v1.0; CLOSE; CHANGE_CLOSED; blob 5075f5ea5a2e; on main via amthorn78/glow-hdengine-v2#814, e971d460, 2026-11-01T16:56:33Z)"
producing_prompt: "CL-20 — Prepare Closure Memo and Post-Closure Record — 102726.1 (https://app.notion.com/p/4064590a05eb81c28ac8ff12b072826b; page state 2026-10-27T13:15:06.100Z; read in full)"
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
author: "Isis (Isis-60), continuing Lead Developer and closure authority for HDE-EPIC041 (https://claude.ai/code/session_01Q789tyhUaytmY7x273kwes)"
prepared: "2026-11-01T17:18Z"
addressed_to: Thoth; Master Scrum
delivery_state: "PREPARED, NOT DELIVERED (post-closure record §4, M-1 and M-2)"
companion: docs/ephemeral/HDE-EPIC041-CL-20-post-closure-record-v1.0.md
---

# HDE-EPIC041 — Closure memo

**To:** Thoth; Master Scrum.
**From:** Isis, Lead Developer.
**Subject:** HDE-EPIC041, Separation Pass 4, is closed.

## Decision

HDE-EPIC041 is **closed** (`CLOSE`, `CHANGE_CLOSED`).

* **Decision record.** `docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md`, decided 2026-11-01T16:39Z. It is on `main` via #814 (`e971d460`), and HDE Build Notes 2.10 records it.
* **Closure mode.** Ordinary close mutation set; no exceptional closure. The close pack and its close-run family are #812; the close-tooling repair is #811. The closure decision re-verified them on `main` with eight read-only checks, all exit 0.
* **Ordering.** For this Epic, the Product Owner ruled that the close mutation set precedes the closure decision (CCR-5, alternative B, bounded to HDE-EPIC041; HDE Build Notes 2.9).

## What was delivered

* **Scope.** HDE Build Checklist — Separation, Task HDE-SEPA006 and Subtasks .1 to .3: the non-BodyGraph chart-loader boundary correction. Specification v1.1 (approved by Thoth) holds requirements R-01 to R-04 and criteria AC-01 to AC-05, all delivered.
  * `adapter/chart_orchestration.py` is the Adapter-owned chart entry. It owns rails, clocks, the correlation id, pinned-list reads, fixture acquisition and keys-only logging.
  * `engine/charts/pure.py` is the pure Engine module. It does no time, environment, randomness, provider, logging or filesystem access, including at import.
  * `engine/charts/loader.py` is removed with no shim (Product Owner decision D-1), behind a repository-wide import guard. Its three callers are migrated.
  * No public route, flag, payload, CLI, provider-contract or release change; release 1.3.0 is unchanged.
* **Work units.** Each was accepted at PR-40, with merged-change attribution reconciled EXACT:
  * WU-PR-01 (#791);
  * WU-PR-02 (#796);
  * WU-PR-03 (#800), with DOC-20 `COMPLETE`.
* **Ops:** none in scope.
* **QA.**
  * QA-120 verdict `PASS`: seven of seven checks at attempt 1, under closed rails.
  * Report: `docs/ephemeral/HDE-EPIC041-QA120-final-qa-report-v1.0.md`.
  * RCA: `docs/ephemeral/HDE-EPIC041-QA120-qa-rca-v1.0.md`. No failure; five contained friction patterns.
  * No product path has changed since the QA execution source `6717b29b`.
* **Close.**
  * `audit/EPIC-041_close_report.md` records `SATISFIED`, review-trace-only, with nine criteria `MET`, 13 deferrals and seven tracked issues.
  * The close-run family is nine primaries under `audit/qa/hde-epic041/close/`.
  * It is the first Epic close with the v2 writer. CL-05 repaired four close-tooling defects (B-1 to B-4) to make it possible.
* **The one closure judgment.** The Specification §10 declared a tokenless acceptance map, and none was produced. The closure decision found its absence is not a blocker (§5.1 of the decision). Whether a tokenless Epic needs one at all stays the Product Owner's canon question (CCR-1).

## Material residual risks

None is acceptance-critical.

| Risk | Where it is held |
| :- | :- |
| IR-01: the purity proof covers patched entry points and AST deny-lists only (`os` loads transitively through `contextlib`) | Carried proof limit |
| IR-02: the import guard sees tracked files only, and no run-time-assembled names | Carried proof limit |
| Canon still describes the removed loader as current: HDE Architecture §1.1, HDE Mechanics Guide §1.1, HDE State of the Repository §2.2 (DELTA-001 to -003) | Product Owner, canon drainage |
| HDE Build Notes 2.2 R-3 still orders the closure decision before the close-pack write for every other change; the correcting addendum (CCR-5) is unpublished | Product Owner |
| Each later Epic close needs its own close-run admission in the evidence updater (HDE Build Notes 2.8) | Product Owner |
| FND-005 (compat generator still exits 2 by design), FND-006, FND-007, OBS-6 (`scripts/scratch.py`) | Product Owner; CL-40 candidates |

## Remaining administrative and optional follow-up

None of these reopens closure.

* **Board update.** The instruction for Master Scrum is below.
* **Final scan.** CL-40 — Scan for PF09 Gaps and CRD Candidates is the next managed step.
* **PF09.** Task HDE-SEPA006 and Subtasks .1 to .3 are recorded Not done; "change to Done" is supportable from repo evidence (closure decision §9). The update is the Product Owner's separately authorized post-closure action. No PF09 branch (CL-E-20 to CL-E-40) is selected.
* **Canon drainage.** Owned by the Product Owner:
  * HDE Build Notes 2.3 to 2.7, 2.9 and 2.10 for this change, and its share of 2.2 and 2.8;
  * DELTA-001 to -003;
  * CCR-1, CCR-5 and CCR-6.
* **Prompt ecosystem.** PD-1 to PD-3 (CL-05) and PD-CLE10-1 (CL-E-10), for the GCFPE-MGMT-10 owner.
* **Not needed:**
  * no conditional ADR (CL-30): the decisions are already recorded in the close-pack ADR amendment (#811) and the close report's ADR block;
  * no PF30 record, because this is an Epic;
  * no required HDE Phased Epics entry (HDE Governance §9.1.1; post-closure record §5).

## For Thoth

Your Ruling R-A (Specification review v1.0 §4.2; CCR-1) is kept as decided. The closure decision read it as deciding the Specification's contents, not as an acceptance condition. The question you sent to the Product Owner, whether tokenless Epics need an acceptance map, is still open with the Product Owner. No escalation, rescope or remediation occurred, so no ESC-30 advice was needed.

## Board-update instruction for Master Scrum

**Board.** Glow HD Engine Development Board, https://app.notion.com/p/3d54590a05eb819dacccfcfbfee8666b. The Change Process Guide §0.2 names it as the operational development board.

* **Ownership.** HDE Governance §9.1.1, "Post-closure PF10 drainage, memo delivery and board maintenance", assigns it to the authorized manual operator and the actual receiving owners.
* **Read on 2026-11-01, read-only:**
  * Board Cards has **no card for HDE-EPIC041**. A search by Name and Card ID found none; the kickoff (O-3) also recorded none.
  * The latest Epic cards are HDE-EPIC039 and HDE-EPIC040, both `DONE`.
  * Board History's highest Sequence is **078** (HDE-CRD-0002's DONE entry).

**When.** After this memo is delivered to Thoth and to Master Scrum and Master Scrum has received it, in the order HDE Governance §9.1.5 sets (post-closure record §4). Re-read the board first; what is above was its state when read.

**Instruction.**

1. **Add one Board Cards card**, following the HDE-EPIC040 card's shape:

   | Field | Value |
   | :- | :- |
   | Name | `HDE-EPIC041 — Separation Pass 4` |
   | Card ID | `HDE-EPIC041` |
   | Record Type | `Epic` |
   | State | `DONE` |
   | Owner | `Isis` |
   | Tags | `Separation`, `HD Engine` |
   | Summary | "HDE-EPIC041 closed: CLOSE / CHANGE_CLOSED by Isis-60, decision time 2026-11-01T16:39Z (docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md, #814), through the close mutation set #812 (close-tooling repair #811). QA-120 PASS, 7 of 7 (docs/ephemeral/HDE-EPIC041-QA120-final-qa-report-v1.0.md). Open follow-ups: CL-40 scan; PF09.3 HDE-SEPA006 update; canon drainage of HDE Build Notes 2.3 to 2.10, DELTA-001 to -003 and CCR-1, CCR-5, CCR-6. Post-closure administration does not reopen the change." |

2. **Add two Board History entries**, each with Card ID `HDE-EPIC041` and Card related to the new card. Use the next Sequences after the highest existing one (079 and 080 if it is still 078), as for HDE-EPIC040's 073 and 074.
   * Event `ITEM_ADDED`, Summary: "Epic added: Separation Pass 4 (HDE-EPIC041)."
   * Event `ITEM_STATE_CHANGED`, Summary: "State -> DONE (CLOSE / CHANGE_CLOSED by Isis-60 on 2026-11-01; post-closure administration does not reopen the change)."

**Do not mark as complete:**

* the CL-40 scan;
* the PF09.3 update;
* any canon drainage or PF10 drainage;
* the CCR-1, CCR-5 or CCR-6 dispositions.
