---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.5"
result: none (PR-35 checkpoint after the fourth corrective commit; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session, re-entered from the v1.4 handoff
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.4.md (REMOTE_EVIDENCE_PENDING; preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.5.md (on this branch; read as provenance)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session; re-entry RETAIN_EXISTING)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: 0d50b0645bbbfc84c3ab62b3fed644b315bbe081
corrective_commit: 57170082f98fa0c4c98cf6a51aa9547f729897ad
adr_proposal: docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.0.md (first published with this record)
created_at: 2026-10-20T22:50:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.5 (PR-35 checkpoint)

## 1. State

Nonterminal. The session re-entered from the v1.4 handoff. The re-entry handoff's condition line was not filled in; the Product Owner's interrupted message said "try to trigger a review agai[n]", so the session posted one `@codex review` at 22:36Z (comment 6303310088) and Codex ran it.

Codex round 4, on `0d50b06`, completed at 22:38:27Z:
- It did not re-raise CX7-4 or CX7-5. Their fixes are answered, and both threads were resolved at about 22:39Z (addendum 2.14).
- It raised one P1, CX7-6, in the same class. Under PO-35-1 and addendum 2.14 rule 4, the session asked the Product Owner one design question and got PO-35-3 (§2).

The fix is `5717008`, pushed with this record and the AQ-1 ADR proposal.

## 2. Product Owner decisions in this round

**PO-35-3 (rule 8 design question, round 4).** The options offered:
- bind the format to the change (recommended);
- also bind the document's identity;
- rescope.

No stated-limit option was offered, because addendum 2.14 rule 4 excludes it for a P1 on a real input. **Answer: "Bind format to change (Recommended)".** The option's text:
- a CRD source reads only `| S<NN> |` rows;
- `HDE-EPIC<NNN>` reads only its own `**K<NNN>-REQ-NNN.**` and `| AC<NNN>-NN —` rows, with its own NNN;
- otherwise the writer refuses with `REQUIREMENTS_TABLE_ABSENT`;
- the Epic fixture test moves to K041 and AC041 rows, with tests on both real Specifications.

**ADR proposal direction.** The Product Owner said: "also if you need an ADR decision you need to draft the ADR proposal for the IA session." AQ-1 is needed before merge (Plan v1.1 §13; instruction ID-12). The proposal is `docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-proposal-v1.0.md`.
- The selected HDE IA family has no ADR-review prompt, so the proposal records itself as the Product Owner's direct task.
- It contains a proposed text delta for the ADR's Decision section, not yet applied. The delta waits for the IA's review and the Product Owner's decision.

## 3. Review findings (round 4)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-6 | Codex, `0d50b06`, P1 (thread `PRRT_kwDOP103ks6ujYZU`, comment 4331081277) | `_requirement_ids` | All three formats were read for any change, so an Epic source could bind a CRD Specification's S-rows and close `SATISFIED` without its own criteria, and the reverse | Yes. A candidate source is authored by the operator through the writer's `--source` interface. The repository's own test `test_v2_epic_dry_run_uses_the_epic_prefix` closed `HDE-EPIC041` against S01 to S22 | Fixed in `5717008` (PO-35-3) |

Answered by round 4 and resolved: CX7-4 (`PRRT_kwDOP103ks6ueSLc`) and CX7-5 (`PRRT_kwDOP103ks6ueSLp`).

## 4. Local checks on `5717008`

Detached clone, closed rails, CPython 3.12.3, CI's install (as v1.1 §4).

**Negative control.** The new test file against the pre-fix writer (`0d50b06`), on the affected selection: 7 failed, 1 passed.
- The behavioral control is `test_v2_epic_close_refuses_a_crd_specification`: the old writer wrote an Epic close pack against CRD rows, with exit 0 where 1 is expected.
- The other six fail on the new `(payload, change_id)` signature or on the cross-kind refusals.

**Writer test file** (`tests/qa/test_generate_epic_close_pack.py`): 482 passed (478 + 4), exit 0, 22:42:05 to 22:43:30. The copy was clean afterwards.

**Real Specifications.**
- HDE-CRD-0002 v1.1, read as a CRD: S01 to S22.
- HDE-EPIC040 v1.1, read as HDE-EPIC040: K040-REQ-001 to 013 and AC040-01 to 09.
- Each read under the other change kind, and HDE-EPIC040's read as HDE-EPIC041: `REQUIREMENTS_TABLE_ABSENT`.

**Replay** of `prepush_check.py --base 0d50b06 --head 32ecc53`: **PASS**, 22:44 to 22:55:53. Lanes `evidence,qa` (4 paths); `ci.yml` the pinned one; step 08 changed tests 628 passed; step 13 evidence 134 passed; step 14 qa 488 passed; step 16 SUCCESS; copy clean; repository unchanged. Not CI's result.

## 5. In-flight decisions

| Decision | Why | Tested by |
| :- | :- | :- |
| One `@codex review` at re-entry | The Product Owner's interrupted direction; review capacity was the recorded blocker | Codex ran: summary "Manual request", completed |
| PO-35-3 implemented as stated (§2) | Product Owner decision | §4 |
| ADR stated-limit line: "one pinned requirement-ID format per change kind" | Keeps the ADR's limits true after PO-35-3 | — (Markdown) |
| ADR proposal drafted and first published with this push; the ADR Decision-section delta is proposed, not applied | Product Owner's direction; AQ-1 is the Product Owner's, and the IA reviews first | — |

## 6. Spend against the ceiling (instruction ID-1)

- **Sessions:** 4 of 4. This is the same PR-35 session, re-entered.
- **Codex rounds:** 4 completed, plus two that failed on the usage limit.
- **Elapsed:** within 3 days, excluding Product Owner waits.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.4 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 25 | 20:15 | Codex review attempt on `0d50b06` (new commits) | failed: usage limit (comment 6300519846) |
| 26 | 20:37 | Hosted `test` on `0d50b06` (run 39490424564) | success; stale as a gate after round 4 |
| 27 | 22:36 | `@codex review` (comment 6303310088) | review ran; completed 22:38:27Z |
| 28 | 22:39 | Resolve CX7-4 and CX7-5 threads | resolved |
| 29 | ~22:40 | Rule 8 question (CX7-6) | PO-35-3 |
| 30 | 22:43 | Local fix and checks (§4) | pass |
| 31 | next | Reply on CX7-6; push `9813970`, `5717008`, `32ecc53` and this record; CX7-6 thread open until Codex's next review answers it (2.14) | — |

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| AQ-1 (S21 ADR) | IA review of the proposal, then the Product Owner | proposal published with this push |
| Codex review and hosted CI on the new head | PR-35 | after push |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment or closure.
