---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.13"
result: none (PR-35 checkpoint; CX7-14 fixed; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.12.md (preserved unchanged)
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
remote_head_before_push: 170051e5742b9c4af1206fe9c6173c80a9fa83e6
commits_in_this_push: 8f2b640 (CX7-14), 8040d72 (the ADR's vocabulary line), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T04:10:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.13 (PR-35 checkpoint)

## 1. State

Nonterminal. #668 is not merge-ready until this push is reviewed and its CI is green.

- **Hosted CI on `170051e` passed** (run 39537894250).
- **Codex round 12.** The first review of `170051e` failed on the Codex usage limit. The Product Owner re-requested it, and review 5594732375 did not re-raise CX7-13, so that thread is resolved. It raised one new P1, CX7-14, on a real input (§2).
- **Rule 8 is not triggered.** Round 11's finding (CX7-13, the QA ledger read) and round 12's (CX7-14, the later-drain vocabulary in the schema) are in different components and contracts (PF10 addendum 2.11 rule 8).
- **The fix.** CX7-14 is fixed in `8f2b640` and is in this push.

## 2. Review findings (round 12)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-13 | Codex, `09c0843`, P1 (thread `PRRT_kwDOP103ks6umvYU`) | `_qa_ledger_statuses` | fixed in `c32d618` under PO-35-10 (v1.12) | — | Round 12 did not re-raise it; the thread is resolved |
| CX7-14 | Codex, `170051e`, P1 (comment 4332835067) | `schemas/close_candidate_source.v2.json`, `later_drain_statements[].close_expectation` | The schema took the epic-close expectation as free text. A `SATISFIED` close report could therefore state a drainage timing outside canon's vocabulary, as the fixture's own "Drained after closure by its owner." did | Yes: the operator supplies the candidate source through `--source`. On the pre-fix schema, the writer writes that value and exits 0 (§4 row 2) | Fixed (addendum 2.14 rule 2). The thread is answered and stays open until the next review |

The canon read:
- HDE Governance, "Required later-drain fields", requires "the epic-close expectation (`at epic close`, `after an additional PR or OPS slice`, or `after a separate canon-only drain step`)".
- The Glow QA Guide, "Exact PF19 QA vocabulary and semantics", says it "MUST use exactly one of" the same three values, and that near-match variants such as `drain at epic close` "are not additional allowed values".
- HDE Schemas & Artifacts §1.2 lists the field without a vocabulary. Plan v1.1 PD-1 therefore enumerated only the action and the readiness classification.

The review history across twelve rounds: thirteen P1s, CX7-1 to CX7-10 and CX7-12 to CX7-14, all fixed, and one P2, CX7-11, with a stated limit. Three further rounds failed on the Codex usage limit.

## 3. Implementation

- **`schemas/close_candidate_source.v2.json`** (`8f2b640`): `close_expectation` is now an enum of the three canonical values. Anything else is `SOURCE_SCHEMA_INVALID`.
- **`tests/qa/test_generate_epic_close_pack.py`** (`8f2b640`):
  - the fixture's value is now `after a separate canon-only drain step`;
  - `test_v2_close_expectation_uses_the_canonical_vocabulary` checks that each canonical value writes and renders, and that the reviewer's free text and the near-match `drain at epic close` are refused and write nothing.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`8040d72`): the report-content line says that the action and readiness use HDE Schemas & Artifacts §1.2's vocabulary, and the epic-close expectation uses HDE Governance's three values.

## 4. Local checks

All runs were in this session's clone, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `8f2b640` | 836 passed |
| 2 | Negative control: the new test against the pre-fix schema (`170051e`'s copy) | 2 failed, both behaviourally: the old schema accepts both values and the writer writes and exits 0 (`assert 0 == 1`). The three canonical cases pass |
| 3 | Replay of `8040d72`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 1,018.3 s: changed tests 4,452 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the repository unchanged |

## 5. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| The schema's other free-text fields stay free text | `schemas/close_candidate_source.v2.json` | Each was checked against HDE Governance, the Change Process Guide, HDE Schemas & Artifacts and the Glow QA Guide on `main`. None of them is pinned there to a closed set. The tracked-issue ADR status line comes nearest: the Change Process Guide §3.5.2.1 says it "records Deferred with drain targets", but HDE Governance has the same line identify the governing ADR. So it is not a closed set, and the PR is not widened for it | the canon search | the next Codex round |

## 6. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 14 hours 55 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 12 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 15 runs:
  - 10 successes: 6 on ubuntu-24.04, 1 on ubuntu-26.04 (`c9bff83`), and 3 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-10. None is new in this record.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.12 §8)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 78 | 03:19 | Reply on CX7-13; resolve the CX7-12 thread; push `09c0843..170051e`; update #668's description | pushed and read back |
| 79 | 03:19 to 03:33 | Hosted `test` on `170051e` (run 39537894250) | success |
| 80 | 03:19 | Codex review of `170051e` | failed on the usage limit (comment 6307179262) |
| 81 | 03:40 | The Product Owner's `@codex review` (comment 6307454480) | review started |
| 82 | 03:47 | Codex review 5594732375 on `170051e` | CX7-13 not re-raised; CX7-14 (P1) |
| 83 | ~03:50 | Resolve the CX7-13 thread; cancel this session's 05:40 re-trigger check-in | done |
| 84 | next | Reply on CX7-14; push `170051e..` this record; update #668's description | — |

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-14 thread | this session; Codex | open until the next review of the pushed head answers it |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (MERGE_PENDING), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
