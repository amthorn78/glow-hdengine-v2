---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-07-PR-IMPLEMENTATION-RESULT
artifact_version: "1.9"
result: none (PR-35 checkpoint; CX7-10 and the schema-field audit fixed; #670's ubuntu-26.04 fixes merged in; nonterminal)
phase: PR-35 (review resolution and merge readiness), dedicated session
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-07
supersedes_for_state: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-result-v1.8.md (preserved unchanged)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-07-pr-implementation-plan-v1.1.md (v1.1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.6.md (on this branch; read as provenance; governing canon read from main)
proceed: the Product Owner's PR-30 Proceed for exactly PR_IMPLEMENTATION_PLAN v1.1 (unchanged; no second Proceed)
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
session: https://claude.ai/code/session_01JnnPXsPjVQT9y49m9Z8qLA (dedicated PR-35 session)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/668
companion_pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/670 (against main; head 606e1b4, hosted CI green on ubuntu-26.04; the Product Owner merges it)
branch: claude/gallant-cerf-ysdde5
remote_head_before_push: 0b57143907a25dc49fc6f08794831f072914ef5f
commits_in_this_push: b50c79b (five atime tests), d7f51b9 (CX7-10 and the schema-field audit), cf39b95 (merge of #670's head 606e1b4), and this record
created_at: 2026-10-21T01:45:00Z
---

# HDE-CRD-0002 WU-PR-07 — PR implementation result v1.9 (PR-35 checkpoint)

## 1. State

Nonterminal.

- **Hosted CI.** CI was red on every head since `45e4cef`. The cause is GitHub's move of `ubuntu-latest` from `ubuntu-24.04` to `ubuntu-26.04` (v1.8 §5). On 26.04, `/tmp` is a separate, `strictatime`, size-limited tmpfs, which breaks three things in `main`'s own tests: a cross-device move, atime-sensitive snapshots, and the quota. The fixes are tests and test configuration only, with the runner unpinned and nothing waived (PO-35-6). They are in #670, whose hosted CI is green on ubuntu-26.04. This push merges #670's head into #668 ahead of #670's merge (§8), so #668 needs no further wait.
- **Codex round 8** (review 5593585931, on `0b57143`) did not re-raise CX7-9, so that thread is resolved. It raised one P1, CX7-10. Under addendum 2.14 rule 4 the session asked the Product Owner one design question, and got PO-35-7 and its schema-field audit (§2, §5).

## 2. Product Owner decisions

| ID | Question | Decision (the Product Owner's words, where given) |
| :- | :- | :- |
| PO-35-6 | Hosted CI red on `ubuntu-latest` (v1.8 §8: pin, rescope or waive) | "Not A, B or C. Fix the tests; do not pin the runner and do not waive." The five atime tests are fixed so that each takes its "after" metadata before its own reads, or reads without moving atime, keeping `st_atime_ns` in the comparison. The mapped-cache cross-device pair goes in "one small separate PR against main" (#670). "Then merge main into #668 … CI runs on ubuntu-latest (26.04), unpinned." Later: "All CI is failing, which is your primary mandate failing. This needs to be resolved. This task has sprawled badly." |
| PO-35-7 | CX7-10 | "Every deferral in ledger. The writer checks every deferral's ID, in both forms, against the drain-targets ledger (DEFERRAL_UNBOUND otherwise). Reword the ADR's R-2 line to match PF10 addendum 2.15's summary, and record this as my decision of today changing the approved ADR text. The PF12 §1.2 basis is the drain-targets ledger plus the single-posture rule; for the pointer form this is stricter than §1.2 requires." Also: list every v2 schema field that names a path, ID, heading or pointer, with how the writer validates it, and fix any unvalidated one that could let a wrong `SATISFIED` through on a real input; ask once for a design change |
| PO-35-8 | Audit: the TI pointer form (one ask) | "Pin to the register (Recommended)": `pointer.binding` must resolve to the change kind's register, a PF09 HDE Build Checklist file for an Epic or a PF30 HDE CRD Records file for a CRD, and the heading must be there |
| PO-35-9 | Audit: `plan_path` (same ask) | "Pin like the Specification (Recommended)": the change's own `docs/ephemeral/<change-id>-implementation-plan-v<N>.<N>.md` at the highest version tracked |

## 3. Review findings (round 8)

| ID | Reviewer, revision | Location | Finding | Real input? | Disposition |
| :- | :- | :- | :- | :- | :- |
| CX7-10 | Codex, `0b57143`, P1 (thread `PRRT_kwDOP103ks6ulM_K`, comment 4331867678) | `_require_v2_semantics` | A `drain_target`-form deferral was never checked against the drain-targets ledger, so a `SATISFIED` close could carry a deferral that no ledger names | Yes: operators author candidate sources through `--source` | Fixed in `d7f51b9` (PO-35-7) |

Answered by round 8 and resolved: CX7-9 (`PRRT_kwDOP103ks6ukn1h`). Rule 8 (addendum 2.14 rule 4): the class recurred in round 8. Its answer is PO-35-7 together with the audit, which closes the class's remaining open fields (§5).

## 4. Hosted CI on ubuntu-26.04: what failed and what fixes it

| Failure on `main`'s own tests | Cause | Fix | Where |
| :- | :- | :- | :- |
| 2 `tests/evidence/test_v2_mapped_cache_evidence.py` tests: `EXDEV` and a `ValueError` | The test sent the producer's destinations to `tmp_path`, on a different filesystem from the producer's stage beside the checkout | An `isolated_root` fixture beside the checkout | #670 `84e1c26` |
| 5 v1 tests in `tests/qa/test_generate_epic_close_pack.py`: `st_atime_ns` moved | Under `strictatime`, the tests' own reads between snapshots move atime: a `read_bytes()`, and git's re-read of racy index entries during `git add`/`git commit`. For the symlink test, the move is the writer's one documented exemption (`readlink`) | Each test now brackets only the writer (§6) | #670 `367afbd`; the same change is #668's `b50c79b` |
| 43 evidence-lane tests: `OSError: [Errno 122] Disk quota exceeded` (#670 run 39523821233) | Evidence tests copy the checkout into `tmp_path`, and pytest kept every copy until the session ended | `pytest.ini`: `tmp_path_retention_policy = failed` | #670 `606e1b4` |

Measured on `main` `390bc99`, evidence lane, `basetemp` on local disk, disk use sampled every 2 s: with pytest's default retention the copies reached 2,742 MB after 2.5 minutes and were still growing. With `tmp_path_retention_policy = failed` the peak was 137 MB.

## 5. Schema-field audit (PO-35-7)

Every field of `schemas/close_candidate_source.v2.json` that names a path, ID, heading or pointer, with how the writer validates it on `d7f51b9`.

| Field | Names | How the writer validates it | Change in this push |
| :- | :- | :- | :- |
| `change_id` | ID | Schema `^HDE-(?:EPIC[0-9]{3}\|CRD-[0-9]{4,})$`. It derives the report, manifest, supporting-ledger and QA paths, and selects the requirement-ID format and the register | — |
| `plan_path` | path | Admitted causal input, read as a tracked regular file at HEAD. It must be the change's current implementation plan (`PLAN_SOURCE_NOT_CURRENT`) | **added** (PO-35-9) |
| `evidence_inputs[].binding` | binding ID | Schema pattern; unique (`EVIDENCE_BINDING_AMBIGUOUS`) | — |
| `evidence_inputs[].path` | path | Admitted causal input, tracked at HEAD; unique; must not collide with the schema, source, plan or outputs | — |
| `requirements_binding` | binding | Resolves (`BINDING_UNRESOLVED`). The bound file is the change's current approved Specification (`REQUIREMENTS_SOURCE_NOT_CURRENT`) | — |
| `acceptance[].criterion_id` | ID | Unique (`ACCEPTANCE_AMBIGUOUS`). One of the Specification's IDs in the change kind's format (`REQUIREMENT_ID_UNBOUND`). `SATISFIED` needs every ID (`REQUIREMENT_COVERAGE_INCOMPLETE`) | — |
| `acceptance[].evidence_bindings[]` | binding | Resolves | — |
| `deferrals[].id` | ID | Unique (`DEFERRAL_AMBIGUOUS`). Occurs in the drain-targets ledger, in both forms (`DEFERRAL_UNBOUND`) | **widened to both forms** (PO-35-7, CX7-10) |
| `deferrals[].drain_target` | pointer text | Schema `causal_text`; made auditable by the ledger check on the deferral's ID | none further (PO-35-7) |
| `later_drain_statements[].canon_homes[]`, `locators[]` | canon homes and locators | Schema `causal_text` | none: HDE Schemas & Artifacts §1.2 makes later-drain statements support records only, never gates |
| `later_drain_statements[].evidence_bindings[]` | binding | Resolves | — |
| `tracked_issues[].id` | ID | Schema `^TI-[0-9]{3,}$`; unique; an ADR-status item occurs in the ledger (`TRACKED_ISSUE_UNBOUND`) | — |
| `tracked_issues[].pointer.binding` | binding | Resolves. The bound file must be the change kind's register (`TRACKED_ISSUE_POINTER_UNBOUND`) | **added** (PO-35-8) |
| `tracked_issues[].pointer.heading` | heading | A Markdown heading line in the bound file (`TRACKED_ISSUE_POINTER_UNBOUND`) | — |
| `adr_block.decisions[].bounding_canon[]`, `doc_delta_targets[]` | PF titles | Schema `pf_title` (titles only, no section numbers) | none: ADR-block content, not an input to the closure decision |
| `adr_block.closure_override.accepted_gaps[].evidence_bindings[]` | binding | Resolves | — |
| `adr_block.closure_override.accepted_gaps[].drain_targets[]` | PF titles | Schema `pf_title` | none: as above |
| `superseded[].binding` | binding | Resolves | — |
| `qa_rca.binding` | binding | Resolves | — |
| `pointers[]` | path or directory | Schema `causal_pointer`; the required set is present (`POINTER_MISSING`). Each names a tracked file or a directory holding one, except a CRD's close-run directory, which is written after the verdict (`POINTER_UNRESOLVED`) | **added** (audit: an unresolvable pointer let a `SATISFIED` report cite evidence that does not exist) |
| `key_outputs.*` | path | Close report and manifest equal the derived paths; the three supporting ledgers equal their canonical paths; every other value is a bound evidence path (`OUTPUT_BINDING_MISMATCH`) | — |
| QA ledger `log_path` (inside the bound ledger) | path | Pinned format; the primary is tracked and its header agrees (`QA_LEDGER_INVALID`) | — (PO-35-5) |

## 6. Implementation

**`b50c79b`: five v1 tests.** `st_atime_ns` stays in every comparison:
- lifecycle: the "after" snapshot precedes the test's own `read_bytes()`;
- both-staged and publication-failure: the "before" snapshot follows the test's own `git add`/`git commit`;
- recovery `[same_tree_head]`: the drift is injected with `commit-tree` and `update-ref`, which read no worktree file;
- tracked symlink: held to the writer's documented exemption through the existing `_assert_only_symlink_atime_may_differ`. That helper gains the never-backwards bound of the writer's own predicate. Equality cannot hold there under `strictatime`, because the read is the writer's own `readlink`.

**`d7f51b9`: CX7-10 and the audit.**
- Writer: `_current_version` generalises the Specification lookup; it is used for both the Specification and the plan. New: `IMPLEMENTATION_PLAN_RE`, `EPIC_REGISTER_RE` and `CRD_REGISTER_RE`, plus the four checks in §5.
- Tests:
  - Fixtures bind the pinned plan path and list `DEF-2` in the ledger. Each v2 fixture repository carries the real PF30.1 and PF09.5 files.
  - Six new refusal cases. Seven cases pass through the real PF30.1 heading `**4.2 Material update**` and the real PF09.5 heading `**Subtask HDE-FERM001.3 — Observability & log posture (SAFE rails)**`.
  - Plan tests on the real HDE-CRD-0002 v1.0 and v1.1 plans and the HDE-EPIC040 v2.1 plan.
- ADR: an amendment line under the status line records the Product Owner's 2026-10-21 decisions. Item 4's deferral and tracked-issue text and the stated limits follow them.

## 7. Local checks

Detached clones, closed rails, CPython 3.12.3, CI's install.

| Check | Result |
| :- | :- |
| Reproduction of the five atime failures (`0b57143`), `--basetemp` on a `strictatime` tmpfs, with a demonstration-only plugin that backdates `.git/index` before each test `git add`/`git commit`, so git re-reads racy files as on a fast runner | 5 failed, 3 runs of 3: exactly CI's five. Control on `relatime` with the plugin: 6 passed |
| The same, on the fixed tests | 6 passed, 3 runs of 3 |
| Negative control, `d7f51b9`'s tests against the pre-fix writer (`b50c79b`) | 9 failed, 2 passed. All 9 failures are behavioural: the old writer writes (exit 0) where a refusal is expected. The 2 passes are accepted-path guards |
| `tests/qa/test_generate_epic_close_pack.py` on `d7f51b9` | 527 passed, exit 0 (01:11:54 to 01:13:23). With `--basetemp` on the `strictatime` tmpfs: 525 passed, 2 skipped (the relatime-only symlink tests skip by design), exit 0 |
| #670 (`606e1b4`) on hosted CI, ubuntu-26.04 image 20261018.168.1 (run 39526496622) | **success**, 01:18:02 to 01:37:37: changed tests 4,021 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 130; qa 488; release 79; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. This is CI's result |
| `prepush_check.py --base 390bc99 replay` of this push's tree (`1f9a160d…`, built as `089d407` in a clone; `cf39b95` has the same tree), in a private mount namespace where `/tmp` is a 2 GB `strictatime` tmpfs and the checkout, replay copy and `RUNNER_TEMP` stay on disk, with an empty `HOME` (no global git config, as on a runner) | **PASS**, 01:31:23 to 01:49:04, all 16 steps: lanes `product,compat,db,rails,evidence,qa,release` (25 paths); changed tests 4,143 passed, 2 skipped; product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134; qa 488; release 79, with the attestation built and verified; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; copy clean; repository unchanged. Not CI's result. An earlier attempt with the session's own `HOME` failed in 253 tests on `cannot exec '/tmp/code-sign'`: the session's git signing program, which the namespace's `/tmp` hid and a runner does not have |

## 8. In-flight decisions (instruction ID-16)

| Decision | Path | Why | Validation | Review coverage |
| :- | :- | :- | :- | :- |
| The five atime fixes, as PO-35-6 directs | `tests/qa/test_generate_epic_close_pack.py` (in the bounded set) | CI red on ubuntu-26.04 | §7 rows 1, 2 and 4 | the next Codex round; hosted CI |
| The symlink test is held to the writer's documented exemption rather than to equality | same | Nothing in the test reads the link: the only read is the writer's `readlink`, which HDE-EPIC039 documents as the sole exemption. Equality cannot hold under `strictatime`. `st_atime_ns` stays in the comparison, as the writer's own predicate states it | §7 row 2 | same |
| #670's head is merged into #668 now, ahead of #670's merge, not after it as the Product Owner first sequenced | `pytest.ini`, `tests/evidence/test_v2_mapped_cache_evidence.py` (by the merge) | #670's fixes exist and are green on hosted 26.04. Porting them now gets #668 green without waiting, and it no-ops when `main` carries #670. A container restart at about 01:22 had shown that held, unpushed commits are at risk | the tree equals the emulated head (§7) | hosted CI; the Product Owner may redirect |
| The quota fix and the same five fixes are also on `main`, through #670 | `pytest.ini`, `tests/qa/test_generate_epic_close_pack.py`, `tests/evidence/test_v2_mapped_cache_evidence.py` on #670 | `pytest.ini` is a full-validation path, and so is this PR's own change set: both run all 166 changed-test targets on 26.04, including `main`'s copies of the five tests | §7 rows 5 and 6 | #670's CI and review |
| `POINTER_UNRESOLVED` | `tools/qa/generate_epic_close_pack.py` | The audit's one unvalidated field that could let a wrong `SATISFIED` through without a design change | §7 row 3 | the next Codex round |

## 9. Spend against the ceiling (instruction ID-1)

The ceiling: "At most 4 sessions or 3 days from PR-10 to merge."
- **Sessions:** 4 of 4. #670 was opened from this same PR-35 session, at the Product Owner's direction.
- **Elapsed:** from PR-10's start (2026-10-20T13:14:32Z) to this record, within the 3 days, waits included.
- **Codex rounds:** 8 completed, plus two that failed on the usage limit.
- **Hosted CI on #668:** 11 runs: 6 successes on 24.04 (`f42dd52` to `0d50b06`), 4 failures on 26.04, and 1 cancelled. **On #670:** 1 run, failed on the quota.
- **Product Owner decisions in PR-35:** PO-35-1 to PO-35-9.

## 10. PR_REMOTE_ACTION_LEDGER (continues v1.8 §10)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 52 | 00:28 | Reply on CX7-9; push `abc0254..0b57143` | pushed and read back (v1.8 sha256 32b31bfc…) |
| 53 | 00:29 | Update PR comment 6304300592 with the established root cause | edited |
| 54 | 00:28 to 00:35 | Hosted `test` on `0b57143` (run 39521569087) | failure: the same 7 |
| 55 | 00:45 | Codex review 5593585931 on `0b57143` | CX7-10 (P1); CX7-9 answered |
| 56 | ~00:50 | Push branch `claude/mapped-cache-test-same-filesystem`; open #670 | opened |
| 57 | 00:51 to 00:56 | Hosted `test` on #670 `84e1c26` (run 39523821233) | changed tests 18 passed; evidence lane failed on the quota (43 failed, 86 passed, 1 error) |
| 58 | ~00:52 | Resolve CX7-9 thread | resolved |
| 59 | ~00:55 | Rule 8 question (CX7-10) | PO-35-7 |
| 60 | ~01:00 | Audit design questions (one ask) | PO-35-8, PO-35-9 |
| 61 | 01:17 | Push #670 `84e1c26..606e1b4`; update #670's description | pushed and read back |
| 62 | 01:18 to 01:37 | Hosted `test` on #670 `606e1b4` (run 39526496622) | **success**, all seven lanes, ubuntu-26.04 |
| 63 | 01:20 | Codex review of #670 `606e1b4` | no findings |
| 64 | ~01:22 | Container restart | the local commits and scratchpad survived; one local emulation run lost |
| 65 | 01:45 | Merge #670's head into #668 (`cf39b95`) | tree `1f9a160d…`, equal to the emulated head |
| 66 | next | Reply on CX7-10; push `0b57143..` with this record; update #668's description. The CX7-10 thread stays open until Codex's next review answers it | — |

## 11. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Merge of #670 | Product Owner | CI green on ubuntu-26.04; Codex: no findings; ready |
| Hosted CI and Codex review of this push | PR-35 | after the push |
| Merge of #669 (the AQ-1 review and addendum records) | Product Owner | open; independent of #668 |
| Drainage named by addenda 2.13 to 2.15 | their owners | unperformed |

Nonclaims: no merge readiness, QA verdict, acceptance, Ops, deployment or closure.
