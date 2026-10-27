---
artifact_type: IA_SESSION_CONTINUITY_RECORD
artifact_id: HDE-CRD-0002-IA-SESSION-CONTINUITY
artifact_version: "1.0"
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
role: the continuing whole-change Implementation Agent (IA) for HDE-CRD-0002
handing_over_session: https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
earlier_ia_session: https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah
receiving_session: the new dedicated IA session titled "HDE-CRD-0002-2", created at the Product Owner's direction of 2026-10-21 ("create a new session to carry on with this work. It will be a new dedicated IA session for HDE-CRD. The ID will be HDE-CRD-0002-2.")
captured_at: 2026-10-21T01:20:00Z
repository_state_read: origin/main 390bc99; #668 head 0b57143; #669 head 8e069b3; #670 head 84e1c26
---

# HDE-CRD-0002 — IA session continuity record v1.0

This record hands the whole-change IA role for HDE-CRD-0002 to a new dedicated session, "HDE-CRD-0002-2". It records where the work stands, the open decisions and what the IA does next. It decides nothing. Every fact below is from the repository or the pull requests at the time above. The receiving session re-verifies each one before relying on it.

## 1. Approved base and canon

- Specification v1.1: `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (approved, "ASK OK.").
- Implementation Audit v1.0: `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md`.
- Implementation Plan v1.1 and its IA-30 review v1.1 (Isis, INITIAL_APPROVE): `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md`.
- Order of units: WU-PR-01 to WU-PR-08, WU-DOC-01, WU-OPS-01, then QA-10 (Plan v1.1 §7).
- PF10 (HDE Build Notes):
  - on `main`: `docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md`, addenda up to 2.12;
  - on #668's branch: v13.6.6, which adds 2.13 (closeout-validation install), 2.14 (P1 findings are addressed until resolved) and 2.15 (AQ-1: the S21 ADR approved with changes; the close-run evidence family introduced). These land on `main` when #668 merges.
- Product Owner rules in force for this change: addendum 2.11 (business case, cost ceiling, real inputs, no emulation, finding disposition, rule 8), read with 2.12's numbering; addendum 2.14 (a P1 on a real input is always fixed).

## 2. Work units

| Unit | State | Record |
| :- | :- | :- |
| WU-PR-01 to WU-PR-06 | accepted | PF10 addenda 2.4, 2.5, 2.8, 2.9, 2.10, 2.12 |
| WU-PR-07 (S21: close-pack writer, close-run family, ADR) | PR-35 in progress on #668, in session https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA; latest record `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.8.md` on #668's branch | instruction v1.0, plans v1.0 and v1.1, rescope review v1.0 (addendum 2.13), AQ-1 review v1.0 (addendum 2.15), result records v1.0 to v1.8 |
| WU-PR-08 (S01, S16, S17, the 1.4.0 cut) | not started | needs its addendum 2.11 business case and the S01 real-input fact (the Railway build command and deploy trigger; addendum 2.12 decision 4) from the Product Owner before its PR-10 |
| WU-DOC-01, WU-OPS-01, QA-10 | not started | Plan v1.1 §7 and §9 |

## 3. WU-PR-07: open items at handover

- **AQ-1.** Decided by the Product Owner: approved with changes (addendum 2.15; review `docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md`). The PR-35 session applied conditions C-1 to C-3 and the redlines in `aa94c34` (as its commit message and result v1.7 state; the receiving IA verifies at PR-40).
- **Hosted CI red on `ubuntu-26.04`.** GitHub moved `ubuntu-latest` from 24.04 to 26.04. Seven tests fail on that image, `main` included: five atime comparisons in `tests/qa/test_generate_epic_close_pack.py`, and two cross-filesystem moves in `tests/evidence/test_v2_mapped_cache_evidence.py` (result v1.8 §5).
  - The IA recommended fixing the tests, not pinning the runner and not waiving them. The five are fixed in #668, which is in the unit's bounded set. The two are fixed in a separate PR to `main`, which is now #670.
  - Whether the Product Owner adopted that recommendation is not recorded in the repository. The receiving IA asks or reads the PR-35 record.
- **CX7-10 (P1).** A deferral in the drain-target form is not checked against the drain-targets ledger. The conflict between texts is the IA's drafting error:
  - The review's R-2 redline, now in the approved ADR, applies the ledger check to the ADR-status form only, as HDE Schemas & Artifacts §1.2 requires.
  - Addendum 2.15's one-line summary says both forms.
  - The IA recommended "every deferral in ledger": the ADR is reworded to match 2.15, with a sweep of every v2 field that names a path, ID or pointer, fixing any unchecked one in the same push.
  - Whether the Product Owner adopted that recommendation is not recorded in the repository yet.
- **Ceiling** (Product Owner disposition `docs/ephemeral/HDE-CRD-0002-WU-PR-07-po-disposition-business-case-v1.0.md`): one PR; at most 4 sessions or 3 days from PR-10 (started by 2026-10-20T13:14:32Z) to merge, excluding Product Owner waits. Projected at 4 of 4 sessions since the rescope (rescope review v1.0 §7).

## 4. Open pull requests

| PR | Content | Owner of the next action |
| :- | :- | :- |
| [amthorn78/glow-hdengine-v2#668](https://github.com/amthorn78/glow-hdengine-v2/pull/668) | WU-PR-07 implementation | the PR-35 session; the Product Owner merges |
| [amthorn78/glow-hdengine-v2#669](https://github.com/amthorn78/glow-hdengine-v2/pull/669) | the IA's page-ready texts of addenda 2.14 and 2.15, the AQ-1 ADR review, and this record | the Product Owner merges (records only) |
| [amthorn78/glow-hdengine-v2#670](https://github.com/amthorn78/glow-hdengine-v2/pull/670) | the mapped-cache test fix for `ubuntu-26.04` (opened by the WU-PR-07 PR-35 session) | the Product Owner merges; then #668 merges `main` in |

## 5. What the IA does next

1. **Now.** Recover the role. Verify sections 1 to 4 against the repository and the pull requests. Answer the Product Owner's questions on WU-PR-07 decisions as they arise.
2. **After #668 merges: PR-40 lineage review of WU-PR-07** (PR-40 — Review PR Work-Unit Lineage — 100926.1). Besides the usual review, it records:
   - the unit's cost against its ceiling (addendum 2.11 rule 3);
   - the option A line (WU-PR-06 disposition): any hosted CI failure the local replay would have caught. The `ubuntu-26.04` failures were not caught locally, because the local replay ran on the session's own image;
   - the IA's own defects in instruction v1.0: ID-10's unverified premise (F-1, rescope review v1.0 §3.3), and §4.1's omission of Change Process Guide §3.5.4 and HDE Governance §2.0.19 (AQ-1 review §3);
   - addendum 2.15's R-2 summary and how it was resolved (CX7-10);
   - the ruby observation on `ubuntu-26.04` (result v1.8 §5), against addendum 2.2's open item;
   - OBS-17, LR-O2 and LR6-O5 as carried.
3. **WU-PR-08's PR-10**, once the Product Owner supplies its business case and the S01 real-input fact.

## 6. Working rules carried

- Write only under `docs/ephemeral/`, on the session's designated branch, through a pull request the Product Owner merges. Never edit `docs/pfcanon/`. PF10 addenda are written as page-ready texts under `docs/ephemeral/`, and the Product Owner publishes them.
- Search canon on `main` before deciding (`AGENTS.md` canon-first rule). Every review or decision artifact carries a "Canon relied on" block.
- Report to the Product Owner with the answer first and one named state line (DECISION NEEDED, NOTHING NEEDED or IN FLIGHT). End a handoff with one `text` NEXT_PROMPT_HANDOFF block.
- Run the TypeSafe scoring skill once for each receiving session. The Notion row is not written (addendum 2.1).
- Never decline a P1 finding on a real input (addendum 2.14). Measure before claiming, and state plainly what was not verified.
