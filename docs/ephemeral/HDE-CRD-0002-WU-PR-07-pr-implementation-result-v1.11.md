---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.11"
result: none (PR-35 checkpoint; v1.10's MERGE_PENDING is withdrawn; CX7-12 fixed; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.10.md (preserved unchanged)
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
remote_head_before_push: 52bb1f275111937951471ac2311397eb66e67946
commits_in_this_push: 4ef99c7 (CX7-12), 2b03694 (the ADR limit line), and this record
canon_conflict_register: CR-1 to CR-8 carried unchanged, all decided; no new entry
created_at: 2026-10-21T02:48:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.11 (PR-35 checkpoint)

## 1. State

Nonterminal. **v1.10's `MERGE_PENDING` is withdrawn, and #668 is not merge-ready until this push is reviewed and its CI is green.**

- **Why.** Codex round 10 (review 5594151205 on `52bb1f2`, the v1.10 record's commit) raised one P1, CX7-12, on a real input. Under PF10 addendum 2.14 rule 2, a pull request with an open P1 thread on a real input is not merge-ready. v1.10 was written before that review, so its readiness claim did not hold.
- **The fix.** CX7-12 is fixed in `4ef99c7` and is in this push (§2, §3). Its thread stays open until the next Codex review of the pushed head answers it.
- **Unchanged.** #670 is still green on ubuntu-26.04, and Codex found nothing on it. #668 carries its commits.

## 2. Review findings (round 10)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-12 | Codex, `52bb1f2`, P1 (thread `PRRT_kwDOP103ks6umUAb`, comment 4332349641) | `tools/qa/generate_epic_close_pack.py`, `_primary_identity` | The writer compared each QA ledger entry only with its primary's `check_id` and `status`. A primary whose header was only `{schema_version, check_id, status}` could therefore carry `PASS` over a failed command into a `SATISFIED` close report | Yes. The operator supplies the candidate source and its tracked primaries through `--source`. On the pre-fix writer, the identity-only `PASS` header writes a close pack and exits 0 (§4 row 2) | Fixed (addendum 2.14 rule 2). The thread is answered and stays open until the next review |

Rule 4 is not triggered: round 9's finding (CX7-11, symlinked close-pack members in the updater) is of a different class.

The review history across ten rounds: eleven P1s, CX7-1 to CX7-10 and CX7-12, all fixed, and one P2, CX7-11, with a stated limit. Two further rounds failed on the Codex usage limit.

## 3. Implementation

- **`tools/qa/generate_epic_close_pack.py`** (`4ef99c7`). `_primary_identity(payload, primary_rel, *, crd)` now returns an identity only for a primary that meets the canonical QA harness's whole PF27 v2 header contract:
  - `qa_harness._parse_primary_header`: the exact field set, the check ID, the status, command and exit-code consistency, PASS causality, a non-PASS reason, the evidence list, PF titles, the captured environment, the timestamp, no claimed tokens, and the nonclaim line for intended tokens;
  - the harness's own-primary self-binding: `evidence_artifacts` names the primary;
  - for a CRD, `_parse_crd_primary`'s further rules: canonical LF bytes, a compact sorted header, no PARKED with commands and no FAIL_BEHAVIOR without one.

  Anything else is `QA_LEDGER_INVALID`. The contract is restated in the writer, not imported (§5).
- **`tests/qa/test_generate_epic_close_pack.py`** (`4ef99c7`):
  - the fixture primaries are now complete PF27 v2 headers;
  - two new refusal cases: the reviewer's identity-only header with a failed command in its body, and a complete header that claims `PASS` with exit code 1;
  - `test_v2_primary_check_agrees_with_the_shared_pf27_parser`: 288 cases (24 header cases × 6 payload cases × a CRD and an Epic), each run through both the writer and `qa_harness`, which must give the same verdict;
  - the real-ledger test now runs the full check over all 42 primaries of the four tracked ledgers.
- **`docs/adr/hde/close_pack_writer_adr.md`.** The QA-primary limit line now states the whole-header check. It says the contract is restated because of ID-10, and that a test holds the two in agreement. The body is still not judged beyond the nonclaim line, the same as the shared parser.

## 4. Local checks

All runs were in this session's clone, under closed rails, with CPython 3.12.3 and CI's install. None of them is CI's result.

| # | Check | Result |
| :- | :- | :- |
| 1 | `tests/qa/test_generate_epic_close_pack.py` on `4ef99c7` | 817 passed |
| 2 | Negative control: the new tests against the pre-fix writer (`52bb1f2`'s copy) | 6 failed. The two new refusal cases fail behaviourally: the old writer writes and exits 0 (`assert 0 == 1`). The four real-ledger cases fail on the new signature (`TypeError`) |
| 3 | The parity test's verdicts | They agree in all 288 cases. The writer accepts 5 of the 144 CRD cases and 21 of the 144 Epic cases. The difference is the CRD-only byte and status rules |
| 4 | The four tracked ledgers under the new check | 42 of 42 primaries pass: HDE-CRD-0001 10, HDE-EPIC021 6, HDE-EPIC039 14, HDE-EPIC040 12 |
| 5 | The writer under `python3 -I` with no repository install (`jsonschema` present, no Flask or pytest) | It loads and parses its arguments, and imports no `tools` or `engine` module (ID-10) |
| 6 | Replay of `4ef99c7`, all 16 steps of `.github/workflows/ci.yml`, in a mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs (the ubuntu-26.04 emulation of v1.9 §7) | PASS, all 16 steps, 1,075.7 s: changed tests 4,433 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the repository unchanged |

The ADR commit (`2b03694`) and this record change only `docs/adr/` and `docs/ephemeral/`.

## 5. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| The PF27 v2 contract is restated in the writer, not imported from `tools/qa/qa_harness.py` as the reviewer suggested | `tools/qa/generate_epic_close_pack.py`, `tests/qa/test_generate_epic_close_pack.py` | The instruction's ID-10 keeps the writer at the standard library and `jsonschema` ("the v2 writer and schema keep that"), and the closeout job runs the writer without the repository installed. An import would also load `engine.runtime`. Restating the contract keeps ID-10, and the parity test makes drift fail | §4 rows 1, 3 and 5 | the next Codex round; hosted CI |
| The writer applies the harness's current, non-legacy check-ID rule for an Epic, not the legacy rule `_read_supported_primary_header` also admits | same | The v2 writer already requires PF27 v2 headers. All 42 real primaries use lowercase IDs, and the generic harness publishes only those | §4 row 4 | same |
| The ADR's QA-primary limit line is reworded to match | `docs/adr/hde/close_pack_writer_adr.md` | The old line ("reads the header line only") no longer described the check | the diff | the next Codex round |

## 6. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. No new session.
- **Elapsed:** from PR-10's start (2026-10-20T13:14:32Z) to this record (02:48Z), 13 hours 33 minutes with waits included. That is within the 3 days, so the ceiling is not passed.
- **Codex rounds:** 10 completed, plus 2 that failed on the usage limit.
- **Hosted CI on #668:** 13 runs:
  - 8 successes: 6 on ubuntu-24.04, 1 on ubuntu-26.04 (`c9bff83`) and 1 on `ubuntu-latest` with its image not read (`52bb1f2`, run 39531867247, job 118999392317);
  - 4 failures on ubuntu-26.04;
  - 1 cancelled (`1080f77`).
- **Hosted CI on #670:** 2 runs: 1 failure (the quota) and 1 success.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-9. None is new in this record.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.10 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 71 | 02:14 | Push `c9bff83..52bb1f2` (the v1.10 record) | pushed and read back |
| 72 | 02:14 to 02:33 | Hosted `test` on `52bb1f2` (run 39531867247) | success |
| 73 | 02:16 | Codex review 5594151205 on `52bb1f2` | CX7-12 (P1); v1.10's MERGE_PENDING withdrawn |
| 74 | next | Reply on CX7-12; push `52bb1f2..` this record; update #668's description | — |

## 8. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| CX7-12 thread | this session; Codex | open until the next review of the pushed head answers it |
| Hosted CI on the pushed head | this session | pending |
| The terminal PR-35 record (MERGE_PENDING), with a fresh TypeSafe reading, because the PR-40 action text's counts change | this session | after CI is green and the review is clean |
| Merge of #670 | Product Owner | ready: CI green, Codex no findings. #668 carries its commits, so either order works |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent |
| Drainage named by addenda 2.13 to 2.15; documentation WU-DOC-01 | their owners | unperformed |

Nonclaims: no merge, QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure.
