---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.15"
result: none (PR-35 checkpoint; CX7-16 fixed under PO-35-12; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.14.md (preserved unchanged)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (on this branch; read as provenance; governing canon read from main)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
companion_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/670 (against main; head 606e1b4, hosted CI green on ubuntu-26.04; carried by #668; the Product Owner merges it)
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: f6e1ad0ca8668d129ed0c128e3a131206a6cf266
commits_in_this_push: 9fe2684 (CX7-16), 0e4ef98 (the ADR's PO-35-12 lines), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T12:08:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.15 (PR-35 checkpoint)

## 1. State

Nonterminal. #668 is not merge-ready until this push is reviewed and its CI is green.

- **Hosted CI on `f6e1ad0` passed** (run 39545335936).
- **Codex round 14** (review 5595087584 on `f6e1ad0`) did not re-raise CX7-15, so that thread is resolved. It raised one new P1, CX7-16, on a real input (§3).
- **A design question.** Canon gives no entry format for either supporting ledger and no empty literal for the drain-targets ledger. So the session asked the Product Owner once, as PO-35-7 directs for a design change. The answer is PO-35-12 (§2).
- **The fix.** CX7-16 is fixed in `9fe2684` and is in this push.

## 2. Product Owner decision

| ID | Question | Decision |
| :- | :- | :- |
| PO-35-12 | CX7-16: arbitrary text in the doc-deltas ledger, and in the drain-targets ledger when nothing drains, let a `SATISFIED` close pack through. Which minimum should the writer enforce? The options were: an empty line or a list; strict entries that each name a PF title; or doc deltas only | "Empty line or list (Recommended)":<br>• the doc-deltas ledger contains the exact line `Doc Deltas: None` or at least one Markdown list item, not both;<br>• the drain-targets ledger, with no deferral and no TI, contains the line `Drain Targets: None`; otherwise it names every ID, as before;<br>• a tracked `audit/qa/<change>/00_meta/doc_deltas.md` is byte-identical to the doc-deltas ledger;<br>• all refusals are typed |

## 3. Review findings (round 14)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-15 | Codex, `3eb31c3`, P1 (thread `PRRT_kwDOP103ks6unxtj`) | the tracked-issue pointer | fixed in `6cd8649` under PO-35-11 (v1.14) | — | Round 14 did not re-raise it; the thread is resolved |
| CX7-16 | Codex, `f6e1ad0`, P1 (comment 4333142444) | `tools/qa/generate_epic_close_pack.py`, the supporting-ledger binding check | The writer checked only that the doc-deltas ledger was bound, not that it enumerates deltas or states `Doc Deltas: None` | Yes: the operator supplies the tracked ledgers the source names through `--source`. Reproduced on `f6e1ad0`: the doc-deltas ledger `this is not a doc-delta ledger` writes a close pack and exits 0. So does a drain-targets ledger of arbitrary text when the source has no deferral and no TI item | Fixed under PO-35-12 (addendum 2.14 rule 2), together with the drain-targets sibling of the same gap. The thread is answered and stays open until the next review |

Rule 8 is not triggered: round 13's finding (CX7-15, the TI pointer) and round 14's are in different contracts.

The canon read:
- The HDE Mechanics Guide, "Doc deltas capture file (minimum content; generated)": "MUST enumerate canon deltas found during the run. If none exist, it MUST state: "Doc Deltas: None"."
- HDE Schemas & Artifacts §1.2: both ledgers "MUST explicitly indicate when empty", and a QA-root copy "MUST be byte-identical".

The review history across fourteen rounds: fifteen P1s, CX7-1 to CX7-10 and CX7-12 to CX7-16, all fixed, and one P2, CX7-11, with a stated limit. Three further rounds failed on the Codex usage limit.

## 4. Implementation

- **`tools/qa/generate_epic_close_pack.py`** (`9fe2684`). After the drain-ledger ID checks:
  - the doc-deltas ledger must contain exactly one of the line `Doc Deltas: None` or a Markdown list item; otherwise `DOC_DELTAS_INVALID`;
  - a tracked `audit/qa/<change-dir>/00_meta/doc_deltas.md` must have the same Git tree entry (mode and blob) as the doc-deltas ledger, that is, the same bytes; otherwise `DOC_DELTAS_INVALID`;
  - the drain-targets ledger must contain the line `Drain Targets: None` exactly when the source has no deferral and no tracked issue; otherwise `DRAIN_TARGETS_INVALID`.

  `_require_v2_semantics` now takes the tree mapping, which it was already given, rather than bare paths.
- **`tests/qa/test_generate_epic_close_pack.py`** (`9fe2684`): `test_v2_supporting_ledgers_meet_their_minimum_content`, nine cases:
  - accepted: `Doc Deltas: None`; an enumerated ledger; an identical QA-root copy; `Drain Targets: None` when nothing drains;
  - refused: the reviewer's arbitrary text; `None` beside entries; a drifted QA-root copy; arbitrary drain-targets text when nothing drains; `Drain Targets: None` beside real deferrals.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`0e4ef98`): a stated-limit entry for the ledgers' minimum content, and the amendment line's record of PO-35-12. The writer checks structure only and does not judge whether each listed entry is a true canon delta.

## 5. Local checks

All runs were in this session's clone, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `9fe2684` | 844 passed |
| 2 | Negative control: the new test against the pre-fix writer (`f6e1ad0`'s copy) | 5 failed, all behaviourally: the old writer writes and exits 0 (`assert 0 == 1`). The 4 accepted cases pass on both |
| 3 | Replay of `0e4ef98`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 1,115.3 s: changed tests 4,460 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the repository unchanged |

## 6. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| A `Drain Targets: None` line beside real deferrals is refused | `tools/qa/generate_epic_close_pack.py` | HDE Governance's single-posture rule: one ledger cannot say both that nothing drains and that items do | §5 rows 1 and 2 | the next Codex round |
| The QA-root copy is compared by Git tree entry, not by reading it | same | Equal mode and blob ID is byte identity in the committed tree, and the copy is not otherwise a causal input | §5 row 1 | same |

## 7. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 22 hours 53 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 14 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 17 runs:
  - 12 successes: 6 on ubuntu-24.04, 1 on ubuntu-26.04 (`c9bff83`), and 5 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`, `3eb31c3`; `f6e1ad0`, run 39545335936);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-12.

## 8. PR_REMOTE_ACTION_LEDGER (continues v1.14 §8)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 89 | 04:40 | Reply on CX7-15; push `3eb31c3..f6e1ad0`; update #668's description | pushed and read back |
| 90 | 04:40 to 04:52 | Hosted `test` on `f6e1ad0` (run 39545335936) | success |
| 91 | 04:49 | Codex review 5595087584 on `f6e1ad0` | CX7-15 not re-raised; CX7-16 (P1) |
| 92 | ~05:35 | Resolve the CX7-15 thread | resolved |
| 93 | ~05:35 to ~11:40 | The session's worker restarted; the design question to the Product Owner was answered after it | PO-35-12 |
| 94 | next | Reply on CX7-16; push `f6e1ad0..` this record; update #668's description | — |

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-16 thread | this session; Codex | open until the next review of the pushed head answers it |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (MERGE_PENDING), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
