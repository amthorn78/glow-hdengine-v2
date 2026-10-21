---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.7"
result: none (PR-35 checkpoint; AQ-1 conditions C-1 to C-5 applied; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.6.md (preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (Product Owner's upload, placed on this branch in abdb6df at the Product Owner's direction, replacing v13.6.5; sha256 6604d8906d66c05e647109158894cce601e5c116f6ffbe51cca09a3ace37de86; adds addendum 2.15, the AQ-1 decision; read in full as provenance)
aq1_review: docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md on branch claude/jolly-johnson-xh6rb0 (pull request #669, open; read in full)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: b0a7305f45c57b78ec31bf0e6f52db360427b3d5
commits_in_this_push: abdb6df (PF10 v13.6.6), aa94c34 (C-1 to C-5), 41e8897 (CX7-8 test), and this record
created_at: 2026-10-20T23:50:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.7 (PR-35 checkpoint)

## 1. State

Nonterminal.

- **AQ-1 is decided.** The Product Owner directed "Update this version of PF10 in your PR. This decides your ADR". PF10 v13.6.6 (addendum 2.15) replaces v13.6.5. It records AQ-1 as approved with changes, on condition that C-1 to C-4 land in #668 before merge. It also introduces the close-run evidence family.
- **C-1 to C-5 are implemented** in `aa94c34`, with the ADR status line transcribed from 2.15.
- **Codex round 6** (on `b0a7305`) did not re-raise CX7-7, so that thread is resolved. It raised CX7-8, which C-2 already fixes; `41e8897` pins it on the real input.
- **Hosted CI is red on two heads** (§5). The failure is not this PR's code: the runner's `/tmp` moved to a different filesystem. One comment on the PR records it (6304300592).

## 2. Product Owner decisions in this round

**AQ-1 (addendum 2.15)**: approved with changes. Its conditions, from the IA review `HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md` §4:
- **C-1:** ADR block.
- **C-2:** the current approved Specification as the requirements source.
- **C-3:** HDE Governance's literal TI fields.
- **C-4:** redlines R-1 to R-4 in the ADR.
- **C-5:** the status line.
- **C-6:** validation.
- **C-7:** the ceiling.

**C-5's timing.** The status line is in the same push as C-1 to C-4. Addendum 2.15 says "When C-1 to C-4 are pushed, the ADR's status line reads: …"; the review's C-5 says "After C-1 to C-4 are pushed". Addendum 2.15 governs, and a single push satisfies "when" without a further CI run and Codex round. Recorded as an in-flight decision (§6).

## 3. Implementation (`aa94c34`)

| Condition | Change |
| :- | :- |
| C-1 | **Schema:** `adr_block` is required: `{decisions (1 to 64), closure_override?}`.<br>**Each decision:** `label`, `statement`, `decision_point`, `options_considered` (empty, or at least 2), `bounding_canon` (PF titles, at least 1), `final_decision`, `scope` (`canonical` or `change_specific`), `doc_delta_targets` (PF titles).<br>**PF titles** pinned to `^[A-Z][A-Za-z &'/-]*[A-Za-z]$`, so no section numbers.<br>**Closure override:** `label`, `accepted_gaps[]` (`gap`, bound `evidence_bindings`, `drain_targets`); its bindings must resolve (`BINDING_UNRESOLVED`).<br>**Report:** a new "ADR block" section after "Tracked-issue closeout mapping" |
| C-2 | `requirements_binding` must be `docs/ephemeral/<change-id>-specification-v<N>.<N>-approved.md` of the source's own change, at the highest version tracked, with versions compared numerically. Otherwise `REQUIREMENTS_SOURCE_NOT_CURRENT`. Uses the writer's existing tracked tree; no new I/O |
| C-3 | A tracked issue renders `- TI-<id> pointers: …` or `- TI-<id> ADR status line: …` |
| C-4 | The ADR's item 4 carries R-1, with C-2's path rule and PO-35-4's QA-ledger rule, and R-2, with C-3 and the ADR block. Item 5 and the "neutral writer, weighed" section carry R-3. New item 9 describes the ADR block (C-1). Item 7 names addendum 2.15 as introducing the close-run family. The canon table gains R-4's five rows |
| C-5 | Status line: "Status: Approved with changes by the Product Owner on 2026-10-20 (AQ-1; HDE Build Notes addendum 2.15; review docs/ephemeral/HDE-CRD-0002-WU-PR-07-adr-review-v1.0.md)." |

## 4. Review findings (round 6)

| ID | Reviewer, revision | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- |
| CX7-8 | Codex, `b0a7305`, P1 (thread `PRRT_kwDOP103ks6ukJ80`, comment 4331414355) | A CRD source could bind any tracked file with S-rows, such as `docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-instruction-v1.0.md` (S21 only), and pass coverage | Yes; the file is on `main` | Fixed by C-2 (`aa94c34`), pinned by `test_v2_real_document_with_a_requirement_row_is_not_a_requirements_source` (`41e8897`). No new design question: this is the Product Owner's C-2 decision |

CX7-7 was answered by round 6 and its thread resolved. Rule 8: the class recurred in round 6, and its answer is the Product Owner's own AQ-1 condition C-2.

## 5. Hosted CI red on `45e4cef` and `b0a7305`

| Run | Head | Result |
| :- | :- | :- |
| 39511628248 | `45e4cef` | failure: changed-tests step, 7 failed, 4,091 passed |
| 39514356279 | `b0a7305` | failure: changed-tests step, 7 failed, 4,102 passed |

The same 7 tests failed in both runs:
- `tests/evidence/test_v2_mapped_cache_evidence.py`, 2 tests: `Invalid cross-device link` from `$RUNNER_TEMP/hde-epic038-pr05-*` into `/tmp/pytest-of-runner/…`.
- `tests/qa/test_generate_epic_close_pack.py`, 5 v1 tests: `st_atime_ns` changes between two snapshots, with size, mtime, ctime and inode unchanged.

**Root cause, as established.**
- The same tests passed on the seven earlier runs of this PR, the last on `0d50b06` (run 39490424564, 20:37Z).
- The cross-device error proves `$RUNNER_TEMP` and `/tmp` are now on different filesystems; they were one filesystem when that test passed.
- The writer's reads all open with `O_NOATIME`. The atime moves come from the tests' own steps between snapshots under the new `/tmp`'s access-time behaviour: `read_bytes()`, `git add`/`git commit`, and `readlink` on the tracked symlink.
- Locally, putting `TMPDIR` on a different filesystem (tmpfs) reproduces the 2 mapped-cache failures exactly.
- Not established: the 5 atime failures did not reproduce locally on tmpfs with `relatime`, so the exact access-time policy of the runner's new `/tmp` is not known.

**What was done about it.**
- **Re-run:** attempted and refused (`403 Resource not accessible by integration`). The push carrying this record re-tests.
- **Fix:** none within WU-PR-07's bounded files. The proposed patch is outside them, since `ci.yml` is expected-unchanged under instruction §6: export `TMPDIR="$RUNNER_TEMP/pytest-tmp"` in the changed-tests step.
- **PR comment:** one comment, 6304300592, records all of this.
- **If the next run fails the same way:** the Product Owner decides — a ci.yml change through the rescope route, a scoped CI waiver, or a re-run from an account that has permission.

## 6. Local checks

Detached clones, closed rails, CPython 3.12.3, CI's install.

| Check | Result |
| :- | :- |
| Negative control, C-1 to C-3 tests against `b0a7305` | 10 failed as intended, 5 passed. The 5 are schema-refusal guards that the old closed schema also refuses, through its unknown `adr_block` |
| Negative control, C-2 and CX7-8 behaviour against `b0a7305` with the fixture's `adr_block` removed | Both fail as intended: the old writer writes (exit 0) against the real superseded v1.0 Specification (21 rows) and against the real WU-PR-07 instruction (S21 only) |
| `tests/qa/test_generate_epic_close_pack.py` on `41e8897` | 508 passed, exit 0, 23:42:56 to 23:44:22; copy clean |
| The 24 updater consumers + `tests/qa/test_generic_qa_harness.py` on `aa94c34` (C-6, "every updater consumer") | 1,680 passed, exit 0, 23:41:39 to 23:55:07; copy clean |
| `prepush_check.py --base b0a7305 --head aa94c34 replay` (evidence and qa lanes) | **PASS**, 23:41 to 23:56:54. The schema change widens the lanes to `product,compat,evidence,qa,release` (6 paths); `ci.yml` the pinned one. Results: changed tests 653 passed; product 77; compat 119 passed, 3 skipped, 2 xfailed; evidence 134; qa 488; release 79, with the attestation built and verified; step 16 SUCCESS; copy clean. Not CI's result. `41e8897` adds one test to the writer test file, covered by the 508-pass row |
| Local run of CI's full changed-tests target list (166 targets) on `b0a7305` | 4,100 passed, 11 failed. All 11 are this harness's own environment, which leaves `ruby` off `PATH`: 9 HDAPI-v2 inventory tests and 2 pre-push sweep tests. None of the runner's 7 failed |

## 7. In-flight decisions

| Decision | Why | Tested by |
| :- | :- | :- |
| PF10 v13.6.6 replaces v13.6.5 on this branch (`abdb6df`) | Product Owner's direction | `cmp` identical; one PF10 file |
| C-5's status line in the same push as C-1 to C-4 | Addendum 2.15's "When … pushed" governs; it saves a CI run and a Codex round | — |
| `adr_block` as an object holding a required `decisions` list and an optional `closure_override` | C-1 needs an optional closure override, and the schema keeps every top-level property required | `test_v2_schema_is_closed_and_shares_the_v1_feedback_refusal` |
| PF titles pinned to letters, spaces, `&`, `'`, `/` and `-` | §3.5.4's "titles-only" canon references; one refusal for anything else (addendum 2.11 rule 5) | the `section_in_title` case |
| The R-1 text also carries PO-35-4's QA-ledger rule | The rule postdates the review, and the ADR must describe the writer as it is | — |
| `requirements_document_without_table` renamed to `requirements_source_not_a_specification`, now refused earlier with `REQUIREMENTS_SOURCE_NOT_CURRENT` | C-2 makes the earlier refusal the correct one | 508 passed; the table-absent refusal is still covered end to end by `test_v2_epic_close_refuses_a_crd_specification` |

## 8. Spend against the ceiling (instruction ID-1)

- **Sessions:** 4 of 4.
- **Codex rounds:** 6 completed, plus two that failed on the usage limit.
- **Elapsed:** within 3 days, excluding Product Owner waits.

The C-1 to C-4 work stayed in this session (C-7).

## 9. PR_REMOTE_ACTION_LEDGER (continues v1.6 §7)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 36 | 23:20 | Reply on CX7-7; push `45e4cef..b0a7305` | pushed and read back (proposal v1.1 sha256 7f1be9fe…; v1.6 sha256 90df057a…) |
| 37 | 23:02 | Hosted `test` on `45e4cef` | failure (§5) |
| 38 | 23:27 | Hosted `test` on `b0a7305` | failure (§5) |
| 39 | 23:27 | Codex review on `b0a7305` | CX7-8; CX7-7 answered |
| 40 | ~23:35 | Product Owner PF10 v13.6.6 (AQ-1 decided) | `abdb6df` |
| 41 | ~23:38 | Re-run attempt of run 39490424564 | 403 |
| 42 | ~23:40 | PR comment on the CI failure | 6304300592 |
| 43 | ~23:41 | Resolve CX7-7 thread | resolved |
| 44 | next | Reply on CX7-8; push `abdb6df`, `aa94c34`, `41e8897` and this record; CX7-8 thread open until Codex's next review answers it | — |

## 10. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Hosted CI on the new head | PR-35; the Product Owner if it fails again the same way (§5) | after push |
| Codex review of the new head | PR-35 | after push |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent of #668's merge |
| Drainage named by addenda 2.13 to 2.15 | their owners | unperformed |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment or closure.
