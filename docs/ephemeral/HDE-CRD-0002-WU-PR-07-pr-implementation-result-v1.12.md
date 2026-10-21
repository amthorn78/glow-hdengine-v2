---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.12"
result: none (PR-35 checkpoint; CX7-13 fixed under PO-35-10; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.11.md (preserved unchanged)
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
remote_head_before_push: 09c08438277687108020a1dc3621da684f621e60
commits_in_this_push: c32d618 (CX7-13), 78f1eff (the ADR's PO-35-10 lines), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T03:20:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.12 (PR-35 checkpoint)

## 1. State

Nonterminal. #668 is not merge-ready until this push is reviewed and its CI is green.

- **Codex round 11** (review 5594378437 on `09c0843`) answered CX7-12 without re-raising it. It raised one new P1, CX7-13, on a real input (§3).
- **Rule 8.** Rounds 10 and 11 raised findings in the same component and contract: how the writer reads QA evidence against the canonical QA harness's ledger and primary contract. So the session stopped fixing instances and asked the Product Owner one design question (PF10 addendum 2.11 rule 8, with addendum 2.14 rule 4). The answer is PO-35-10 (§2).
- **The fix.** CX7-13 is fixed in `c32d618` and is in this push.

## 2. Product Owner decision

| ID | Question | Decision |
| :- | :- | :- |
| PO-35-10 | CX7-13 is the second consecutive finding of one class (rule 8). How should the writer close the class? The options were: accept only the harness's own bytes; import the harness's validators, which amends ID-10; or rescope | "Harness bytes only (Recommended)": the writer accepts a QA ledger only in the exact bytes the QA harness writes (strict JSON with duplicate keys refused, sorted, compact, one final LF, lowercase check IDs); anything else is `QA_LEDGER_INVALID`. With CX7-12's primary check, this covers both halves of the harness's ledger and primary contract. ID-10 is kept |

## 3. Review findings (round 11)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-12 | Codex, `52bb1f2`, P1 (thread `PRRT_kwDOP103ks6umUAb`) | `_primary_identity` | fixed in `4ef99c7` (v1.11) | — | Round 11 did not re-raise it; the thread is resolved |
| CX7-13 | Codex, `09c0843`, P1 (comment 4332536639) | `tools/qa/generate_epic_close_pack.py`, `_qa_ledger_statuses` | The writer read the QA ledger with plain `json.loads`, so a duplicated check ID kept only its last entry. A `FAIL_BEHAVIOR` entry followed by a `PASS` one let a `SATISFIED` close pack through | Yes, on the same basis as CX7-12: the operator supplies the tracked ledger through `--source`. Reproduced on `09c0843`: the writer writes and exits 0, with "Closure decision: SATISFIED" | Fixed under PO-35-10 (addendum 2.14 rule 2). The thread is answered and stays open until the next review |

The review history across eleven rounds: twelve P1s, CX7-1 to CX7-10, CX7-12 and CX7-13, all fixed, and one P2, CX7-11, with a stated limit. Two further rounds failed on the Codex usage limit.

## 4. Implementation

- **`tools/qa/generate_epic_close_pack.py`** (`c32d618`). The new `_qa_ledger(payload, directory)` reads the ledger:
  - with the writer's duplicate-refusing strict JSON loader;
  - accepting it only when its bytes equal the harness's `_manifest_content` form: sorted keys, compact separators and one final LF;
  - with every check ID in the harness's lowercase form.

  Both the closure decision and the primary-loading loop now read this one validated ledger. Before, the second step re-parsed it with `json.loads`.
- **`tests/qa/test_generate_epic_close_pack.py`** (`c32d618`):
  - two refusal cases in `test_v2_qa_ledger_is_read_before_any_decision`: the duplicate FAIL-then-PASS ledger, and an indented ledger;
  - `test_v2_qa_ledger_read_agrees_with_the_harness_crd_family_check`: 12 ledger cases, each written with a valid primary, run through both the writer and `qa_harness.validate_crd_check_family`, which must give the same verdict. Only the canonical bytes are accepted.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`78f1eff`). The ledger line states the harness-bytes rule, and the amendment line records PO-35-10.

## 5. Local checks

All runs were in this session's clone, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `c32d618` | 831 passed |
| 2 | Negative control: the ledger tests against the pre-fix writer (`09c0843`'s copy) | 14 failed. The two new refusal cases fail behaviourally: the old writer writes and exits 0 (`assert 0 == 1`). The 12 parity cases fail because `_qa_ledger` does not exist (`AttributeError`) |
| 3 | The parity test's verdicts | They agree in all 12 cases. Only the canonical bytes are accepted |
| 4 | The four tracked ledgers | All four are already in the harness's canonical bytes and still pass |
| 5 | Replay of `78f1eff`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 1,057.6 s: changed tests 4,447 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the repository unchanged |

## 6. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| The ledger parity test is against the harness's CRD family validator only | `tests/qa/test_generate_epic_close_pack.py` | The harness has no Epic validator of the flat ledger's bytes: its Epic read also admits older shapes, which the v2 writer pins out, as before. All three tracked Epic ledgers (HDE-EPIC021, HDE-EPIC039, HDE-EPIC040) are already in the canonical bytes | §5 rows 3 and 4 | the next Codex round |
| The ADR's amendment line records PO-35-10 beside PO-35-7 to PO-35-9 | `docs/adr/hde/close_pack_writer_adr.md` | PO-35-10 changes the ADR's stated ledger contract | the diff | same |

## 7. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 14 hours 5 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 11 completed, plus 2 that failed on the usage limit.
- **Hosted CI on #668:** 14 runs:
  - 9 successes: 6 on ubuntu-24.04, 1 on ubuntu-26.04 (`c9bff83`), and 2 on `ubuntu-latest` with the image not read (`52bb1f2`; `09c0843`, run 39534882929);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-10.

## 8. PR_REMOTE_ACTION_LEDGER (continues v1.11 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 74 | 02:46 | Reply on CX7-12; push `52bb1f2..09c0843`; update #668's description | pushed and read back |
| 75 | 02:46 to 03:02 | Hosted `test` on `09c0843` (run 39534882929) | success |
| 76 | 02:51 | Codex review 5594378437 on `09c0843` | CX7-12 not re-raised; CX7-13 (P1) |
| 77 | ~02:55 | The rule 8 design question to the Product Owner | PO-35-10 |
| 78 | next | Reply on CX7-13; resolve the CX7-12 thread; push `09c0843..` this record; update #668's description | — |

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-13 thread | this session; Codex | open until the next review of the pushed head answers it |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (MERGE_PENDING), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
