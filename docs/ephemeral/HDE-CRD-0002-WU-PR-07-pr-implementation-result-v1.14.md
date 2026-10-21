---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.14"
result: none (PR-35 checkpoint; CX7-15 fixed under PO-35-11; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.13.md (preserved unchanged)
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
remote_head_before_push: 3eb31c3e96d2a616e86b0f04de25589997a46533
commits_in_this_push: 6cd8649 (CX7-15), 12bc437 (the ADR's PO-35-11 lines), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T04:43:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.14 (PR-35 checkpoint)

## 1. State

Nonterminal. #668 is not merge-ready until this push is reviewed and its CI is green.

- **Codex round 13** (review 5594897560 on `3eb31c3`) did not re-raise CX7-14, so that thread is resolved. It raised one new P1, CX7-15, on a real input (§3).
- **A design question.** The fix needed a design change rather than a check, so the session asked the Product Owner once, as PO-35-7 directs for such a case. The answer is PO-35-11 (§2).
- **The fix.** CX7-15 is fixed in `6cd8649` and is in this push.

## 2. Product Owner decision

| ID | Question | Decision |
| :- | :- | :- |
| PO-35-11 | CX7-15: a TI item's register pointer can name any existing heading, such as PF09.5's `0.1 Header`, and still yield a `SATISFIED` close pack. No PF09 or PF30 file cites a TI ID, so the writer cannot tie a heading to that issue. The options were: the ADR-status form only; the section must cite the TI ID (and, for an Epic, be a Done subtask); or a Done subtask only | "ADR-status form only (Recommended)". The v2 schema drops the pointer form. Every TI item maps through an ADR status whose ID the drain-targets ledger names, which is the Change Process Guide §3.5.2.1's form (b). This replaces PO-35-8's register pointer |

## 3. Review findings (round 13)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-14 | Codex, `170051e`, P1 (thread `PRRT_kwDOP103ks6uncIa`) | `close_expectation` | fixed in `8f2b640` (v1.13) | — | Round 13 did not re-raise it; the thread is resolved |
| CX7-15 | Codex, `3eb31c3`, P1 (comment 4332978263) | `tools/qa/generate_epic_close_pack.py`, the tracked-issue pointer check | A pointer was checked only for the register's filename and the heading's existence, not for showing that TI's closure | Yes: the operator supplies the candidate source through `--source`. Reproduced on `3eb31c3`: an Epic's TI pointer to PF09.5's real `0.1 Header` writes a close pack with "Closure decision: SATISFIED" and exits 0 | Fixed under PO-35-11 (addendum 2.14 rule 2). The thread is answered and stays open until the next review |

Rule 8 is not triggered: round 12's finding (CX7-14, later-drain vocabulary) and round 13's are in different contracts.

The canon read:
- The Change Process Guide §3.5.2.1 lets a TI item map to "either (a) PF09 subtask pointers (repo path plus section heading) that demonstrate closure, or (b) an ADR status line in the close report that records Deferred with drain targets".
- HDE Governance's closeout-record content names the literal `TI-<id> pointers:` and `ADR status line:` fields.
- No PF09.1 to PF09.7 or PF30.1 file cites a TI ID: 0 occurrences of `TI-NNN`.

The review history across thirteen rounds: fourteen P1s, CX7-1 to CX7-10 and CX7-12 to CX7-15, all fixed, and one P2, CX7-11, with a stated limit. Three further rounds failed on the Codex usage limit.

## 4. Implementation

- **`schemas/close_candidate_source.v2.json`** (`6cd8649`): `tracked_issues[]` items are now only `{id, adr_status}`, and the pointer branch of the `oneOf` is removed. A pointer in any form is `SOURCE_SCHEMA_INVALID`.
- **`tools/qa/generate_epic_close_pack.py`** (`6cd8649`):
  - every TI item's ID must occur in the drain-targets ledger (`TRACKED_ISSUE_UNBOUND`);
  - the register regexes, the heading check and `TRACKED_ISSUE_POINTER_UNBOUND` are removed;
  - the report renders each TI item as HDE Governance's `ADR status line:` field.
- **`tests/qa/test_generate_epic_close_pack.py`** (`6cd8649`):
  - `test_v2_tracked_issue_maps_only_through_an_adr_status`, for an Epic and a CRD: the ADR-status form writes its `ADR status line:`, and the reviewer's pointer to the real `0.1 Header` is refused and writes nothing;
  - `test_v2_schema_admits_only_the_adr_status_form_of_a_tracked_issue`: four pointer and missing-status forms are refused;
  - the two pointer-success tests and four pointer-specific semantic refusal cases are removed, because their input is now a schema refusal.
- **`docs/adr/hde/close_pack_writer_adr.md`** (`12bc437`): the report-content line, the stated-limit line and the HDE Governance drainage row describe the ADR-status-only mapping, and the amendment line records PO-35-11.

## 5. Local checks

All runs were in this session's clone, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `6cd8649` | 835 passed |
| 2 | Negative control: the new tests against the pre-fix writer and schema (`3eb31c3`'s copies) | 3 failed:<br>• the Epic case fails behaviourally: the old writer writes and exits 0 (`assert 0 == 1`);<br>• the CRD case was refused under another code (`TRACKED_ISSUE_POINTER_UNBOUND`);<br>• the old schema admits the structured pointer |
| 3 | Replay of `12bc437`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation) | PASS, all 16 steps, 1,009.7 s: changed tests 4,451 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the repository unchanged |

## 6. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| The fixtures still copy the real PF09.5 and PF30.1 registers into each v2 repository | `tests/qa/test_generate_epic_close_pack.py` | PF30.1 stays the tracked non-plan input of the `plan_not_an_implementation_plan` case, and both registers are the real files the new refusal test binds | §5 row 1 | the next Codex round |

## 7. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** 15 hours 28 minutes, from PR-10's start (2026-10-20T13:14:32Z) to this record, with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 13 completed, plus 3 that failed on the usage limit.
- **Hosted CI on #668:** 16 runs:
  - 11 successes: 6 on ubuntu-24.04, 1 on ubuntu-26.04 (`c9bff83`), and 4 on `ubuntu-latest` with the image not read (`52bb1f2`, `09c0843`, `170051e`; `3eb31c3`, run 39542393862);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-11.

## 8. PR_REMOTE_ACTION_LEDGER (continues v1.13 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 84 | 04:08 | Reply on CX7-14; push `170051e..3eb31c3`; update #668's description | pushed and read back |
| 85 | 04:08 to 04:24 | Hosted `test` on `3eb31c3` (run 39542393862) | success |
| 86 | 04:16 | Codex review 5594897560 on `3eb31c3` | CX7-14 not re-raised; CX7-15 (P1) |
| 87 | ~04:20 | The design question to the Product Owner | PO-35-11 |
| 88 | ~04:30 | Resolve the CX7-14 thread | resolved |
| 89 | next | Reply on CX7-15; push `3eb31c3..` this record; update #668's description | — |

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-15 thread | this session; Codex | open until the next review of the pushed head answers it |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (MERGE_PENDING), with a fresh TypeSafe reading | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
