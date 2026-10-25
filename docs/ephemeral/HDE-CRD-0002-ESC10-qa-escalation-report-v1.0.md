---
artifact_type: QA_ESCALATION_REPORT
artifact_id: HDE-CRD-0002-ESC10-QA-ESCALATION-REPORT-QA110-F01
artifact_version: "1.0"
predecessor: none (the first QA escalation report for HDE-CRD-0002)
state: AWAITING_THOTH_REMEDIATION
change_class: CRD
change_id: HDE-CRD-0002
change_name: "Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer"
finding: QA110-F01 — QA Plan v1.2 check 13 `qa-13-prepush-check` (requirement S20), task T13, attempt 1: the delivered pre-push tool exits 4 with PREPUSH_CHECK_READ_ONLY_VIOLATION although all five of its reports are status=PASS
author: Kronos, the continuing QA authority for HDE-CRD-0002 (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
receiving_owner: Thoth, the continuing HDE-CRD-0002 Head of Development and remediation author (session https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum, as the FND-001 remediation records name it)
session_disposition: continuing Kronos context, as the QA-110 handoff to ESC-10 v1.0 routes it
invocation_binding: CRD / HDE-CRD-0002 / ESC-10 / QA_EVIDENCE_REVIEW v1.0 member T13
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: ESC-10 — Create QA Escalation Report — 100926.1 (https://app.notion.com/p/3f44590a05eb81f2af47fff48995f272; page state 2026-10-12T02:29:32.722Z; read in full in this session)
ecosystem_release: GCFPE-20261009.1 (100926.1)
intake: QA_EVIDENCE_REVIEW_ID docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md (ESCALATION_REQUIRED; blob 0a797250aa81; SHA-256 d8f2a89942b70ddfa57faec186f601652a27b641c70ea61e8cb6cc09c0830724; on main through amthorn78/glow-hdengine-v2#728)
tested_source: 2e03a2686af87ab0607c6cfb9afb4ad79bcdb171 (code outside docs/ephemeral/ and docs/pfcanon/ identical to 0b15328d; tools/ci/prepush_check.py blob 4dc098566620, the blob WU-PR-06 landed)
evidence_of_record: audit/qa/hde-crd-0002/checks/qa-13-prepush-check/primary.log on main (blob 4c6d826ae0ac; 35,842 bytes; SHA-256 71a0d11afff1b89a76a9c7624d0cfa93d22845f5714a3618a87c7967b9593ef7; landed by amthorn78/glow-hdengine-v2#726, squash faa2246)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md (SHA-256 42459e54e4a14eb89a1cd3be80eae8458a5b1c2c50e1fca1b1ce9882b05e6f9b; 519,440 bytes; read completely at this invocation, front matter and addenda 2.1 to 2.26)
observed_revision: dba9e09 (origin/main at authoring; nothing outside docs/ephemeral/ changed since faa2246)
routing: ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, the continuing Thoth session
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_ESC-10 (ESC-10 is not an addendum producer)
created_at: 2026-10-25T01:40:00Z
---

# HDE-CRD-0002 — QA Escalation Report v1.0 (ESC-10): QA110-F01, the pre-push tool's read-only guard (check 13, S20)

## 1. Result

| Field | Value |
| --- | --- |
| State | `AWAITING_THOTH_REMEDIATION` |
| Finding | QA110-F01. `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay` exits 4 with `PREPUSH_CHECK_READ_ONLY_VIOLATION: the repository's tree, ignored files, directories, HEAD or git metadata changed`. Every report it runs is `status=PASS`, and no `PREPUSH_CHECK_RESULT` line is printed |
| Requirement | S20, "writing nothing to the repository" (Specification v1.1) |
| Status | `FAIL_BEHAVIOR` (QA Plan v1.2 check 13 Outcomes: "Exit 4 (repository changed) → `FAIL_BEHAVIOR`") |
| QA-110 decision | `ESCALATION_REQUIRED` (review §6) |
| Attempts | One attempt (attempt 1) with two executions. The second execution was a Product Owner-directed Moon Loop. Check 13's one ordinary rerun is consumed (review ruling R-2) |
| Reproducibility | Observed twice in one venue (the Product Owner's workstation, git 2.53.0). Not observed in two earlier venues (git 2.43.0 and one unrecorded). The underlying git behaviour is reproduced in scratch repositories (§6) |
| Cause | Not established. One mechanism is demonstrated, but which file changed and which step wrote it were not observed (§7, §8) |
| Remedy | Not chosen here (the ESC-10 contract excludes diagnosing the remedy and approving remediation) |
| Return owner | Kronos, for check 13's verification after an approved and delivered repair (§12) |
| Next | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1, Thoth |

## 2. Intake and identities

| Item | Identity |
| :- | :- |
| Originating stage | QA-110 — Review QA Evidence and Route the Next Action — 100926.1, Kronos; review `docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md` §6 (member T13) |
| Task and result | QA-90 collection `docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.0.md` task T13. QA-100 results `docs/ephemeral/HDE-CRD-0002-QA100-qa-execution-results-v1.0.md` §4 T13 and §5.2 |
| Approved QA Plan | `docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md` (blob 66f6016cc75b; APPROVE by the QA-70 review v1.2): check 13, §7 rule B, §9 |
| QA Audit and Guide | `docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md` (§7 item 9) and `docs/ephemeral/HDE-CRD-0002-QA20-live-qa-guide-v1.0.md` (blob d4f245c118a0) |
| Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (blob c4802a5a7fa3), with Specification delta 01 `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` (blob 9408d6ed091b; HDE Build Notes addendum 2.20). S20 is unchanged by the delta |
| Implementation Plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md` (blob abffa2ccbd44; IA-30 `INITIAL_APPROVE`), with Plan delta 01 v1.1 `docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md` (blob 5103fe29d588; addendum 2.19) and the FND-001 remediation overlay (addenda 2.23, 2.24) |
| S20's delivery | WU-PR-06: instruction v1.0 (blob f3a6a8855ec0), plan v1.0 (blob 2848847e8bee) and amthorn78/glow-hdengine-v2#660 (squash b963ed4). Accepted by PR-40 lineage review v1.0 (blob 1b69f1370c80; addendum 2.12). Postmortem v1.1 (blob 738bb5232b22) |
| Repository | `amthorn78/glow-hdengine-v2`; tested source `2e03a268`; evidence on `main` at `faa2246`; `main` at authoring `dba9e09`. `tools/ci/prepush_check.py` is blob 4dc098566620 on all three, equal to WU-PR-06's landed blob (addendum 2.12) |
| Venue of the failure | The QA-100 executor, a Claude Code local CLI session (abab87ae-fdb9-4eb6-b2b9-de5380cee6cb), chosen by the Product Owner. It ran on the Product Owner's workstation: Ubuntu 26.04.1 LTS, kernel 7.0.0-38-generic, git 2.53.0, CPython 3.12.15 (uv build), `/tmp` on tmpfs and `TMPDIR` on ext4 (results §2) |
| Prior repair and escalation lineage | One earlier remediation in this change: QA-10 finding FND-001 (pre-QA; S22). Its records are remediation proposal v1.0 and v1.1 (Thoth, ESC-30), remediation review v1.0 (`APPROVE_AS_CHANGED`) and v1.1 (`APPROVE`) (Isis, ESC-40), and work unit WU-REM-01 (amthorn78/glow-hdengine-v2#716, accepted). It returned to the Isis QA-10 reassessment (addenda 2.23 to 2.26). No earlier QA escalation exists. FND-001 concerned other files and is closed |

## 3. Criterion and expected behaviour

- **Specification S20:** "One read-only command reports CI lanes and release membership for given paths, the current Build Notes path and hash, the uncovered-test sweep run in a throwaway copy, and a `ci.yml` replay in a throwaway worktree, writing nothing to the repository".
- **Implementation Plan v1.1, WU-PR-06 acceptance (1):** "Each IF-9 report runs and the repository tree is byte-identical before and after (asserted by the tool and by its test)".
- **WU-PR-06 instruction v1.0, ID-2** ("Writing nothing to the repository" (binding reading)):
  - "The repository is the session's checkout: its working tree, ignored files included, and its `.git` directory."
  - "No report may create, modify or delete any file there. That includes files `.gitignore` hides (`__pycache__/`, `*.pyc`, `.pytest_cache/`) and git metadata: `HEAD`, refs, the index, `config`, `hooks/` and the worktree registry under `.git/worktrees/`."
  - "Measured feasible: `git clone --shared` plus a detached checkout".

  ID-3: "Every invocation first asserts a clean tree, then runs the reports, then asserts the tree is still clean and `HEAD` is unchanged."
- **Glow QA Guide §2.2.11:** "A non-writing check MUST NOT mutate the repository or external state."
- **QA Plan v1.2 check 13, PASS predicate for step 1:** exit 0; the lanes, membership, build-notes and sweep lines as predicated; `status=PASS` for each of the five reports; "a final `PREPUSH_CHECK_RESULT: PASS` line that reports the repository unchanged".
- **QA Plan v1.2 check 13, Outcomes:** "Exit 4 (repository changed) → `FAIL_BEHAVIOR`". The PR35-C1 signature in `tests/tools/test_prepush_check.py` is `FAIL_TOOLING`.
- **The tool's own definition of "unchanged"** (`tools/ci/prepush_check.py` at blob 4dc098566620):
  - `repository_state()` compares HEAD, `git status --porcelain=v1 -z --untracked-files=all`, the lstat identity of every tracked and ignored file and directory, and `_metadata_digest` of the git directory.
  - `_metadata_digest` hashes, for every file under `.git`, "every file's lstat identity" (mode, size, `st_mtime_ns`, `st_ctime_ns`), `objects/` included, and the bytes of files outside `objects/`.
  - `make_copy()` clones each throwaway copy with `git clone --quiet --shared --no-checkout`.

## 4. Attempts and evidence

All within attempt 1, both in one primary (QA-100 results §5.2; the primary's COMMANDS and NOTES):

| Execution | Window (UTC, 2026-10-25) | Venue change | Step 1 | Replay | Steps 2 to 4 |
| :- | :- | :- | :- | :- | :- |
| 1 | 00:02:22Z to 00:16:57Z | none | exit 4, `PREPUSH_CHECK_READ_ONLY_VIOLATION` | `status=FAIL` at step 08: 2 failed, 4,521 passed, both in `tests/ops/test_hde_epic038_ops03.py` (`OSError: [Errno 18] Invalid cross-device link`); steps 09 to 15 `SKIPPED` | passed; step 3 "137 passed"; step 4 empty |
| 2 (Moon Loop, PO-3) | after 00:16:57Z; primary finalized 00:56:35Z | `TMPDIR` unset in the check shell; two leftover directories under `/tmp/hde-epic038-ops03` removed | exit 4, the same stderr line | `status=PASS`; steps 01 to 16 `SUCCESS`; step 08 "4521 passed, 2 skipped"; `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; "copy after replay: clean" | passed; step 3 "137 passed"; step 4 empty |

The Product Owner's direction for execution 2 was "That means this environment needs a fix, so resolve it as a moon loop". QA-110 accepted it as an execution deviation that removed a venue cause and left the failure (review §6.3).

**Executor observation** (results §5.2; read as stated, not a predicate):
- In both executions, no tracked, ignored or working-tree directory entry of the source clone changed.
- The only `.git` file whose mtime and ctime moved in the check window was `.git/objects/pack/pack-0702e37ebe0101b3b80d126c73ab6880b2aff2bc.pack`, last at 00:16:40Z and 00:56:17Z. Both times fall inside step 3 (the owner test), which ran after step 1, so any step-1 change was overwritten before it was inspected.
- An executor diagnostic in scratch repositories (git 2.53.0) showed that `clone --shared` plus checkout leave the source pack untouched. Writing, from inside the copy, an object that already exists in the source pack updates the source pack's mtime.

**Kronos verification at QA-110** (review §6.2; scratch repositories only, no check rerun):
- Under git 2.43.0, a source repository with its objects packed and a `git clone --shared --no-checkout` copy checked out detached: clone and checkout leave the source pack's mtime and ctime unchanged.
- `git hash-object -w` in the copy, of a blob the source pack holds, moves both (1792891042 to 1792891045). Writing a new blob does not.
- With the tool's own functions imported from `tools/ci/prepush_check.py` at `aae2047` (code equal to the tested source), `repository_state(src)` is equal before and after `make_copy(src, head, copy)`. It differs, in the `metadata` field only, after one such write in the copy.

**Hosted CI.** The tool is not run on hosted CI as a command. Its owner test `tests/tools/test_prepush_check.py` passes there (for example, run 39699657729, all seven lanes, at `1a4c8ab`) and passed in both QA-100 executions (step 3).

## 5. Expected versus observed

| | Expected | Observed (both executions) |
| :- | :- | :- |
| Exit | 0 | 4 (`EXIT_READ_ONLY_VIOLATION`) |
| Reports | five `status=PASS` | five `status=PASS` in execution 2; `replay` `FAIL` in execution 1 for a venue cause |
| Final line | `PREPUSH_CHECK_RESULT: PASS <five reports>; repository unchanged (tree, ignored files, directories, HEAD and git metadata)` | absent; `PREPUSH_CHECK_READ_ONLY_VIOLATION` on stderr |
| Source checkout | tree, ignored files, directories, HEAD and git metadata unchanged | tree, ignored files, directories and HEAD unchanged; git status empty after; the guard's git-metadata digest differs. Which file differed is not recorded by the tool |

## 6. Reproducibility and environment limits

| Run | Venue | Source repository | Result |
| :- | :- | :- | :- |
| PR-40 lineage review of WU-PR-06 on `fc51620` (HDE Build Notes addendum 2.12, "The review's independent checks") | the reviewing session's scratch clones, made with `--no-hardlinks` from the session's checkout; CPython 3.12.3; git 2.43.0 | scratch clone `m` | `replay --full` exit 0, `PREPUSH_CHECK_RESULT: PASS replay=PASS; repository unchanged`; "m identical before and after" |
| QA Audit v1.0 §7 item 9 on `0b15328d` (2026-10-24T02:48:22Z to 03:12:05Z) | throwaway clones in the Kronos session's scratchpad; CPython 3.12.3; git version not recorded (this container reports git 2.43.0 now) | fresh clone | check 13's step 1 exit 0, every line as predicated |
| QA-100, executions 1 and 2 on `2e03a268` (code identical to `0b15328d`) | Product Owner workstation; Ubuntu 26.04.1; git 2.53.0 | E-L full-history clone, used first for checks 1 to 12, 14 and 15 (its status stayed empty throughout) | exit 4 both times |

**Limits.**
- No run on a third venue with git 2.53 or later was made.
- The guard names no file.
- Check 13 was not rerun by QA-110 or by this report: one ordinary rerun is consumed (R-2), and ESC-10 executes no QA.
- The workstation is a real operating environment for the tool: the operator's shell (addendum 2.11 rule 4(b); `AGENTS.md` "Code review guidelines").
- Hosted CI's image is ubuntu-26.04 with git 2.55.0 since mid-October (addenda 2.16, 2.21). The tool is not run there.

## 7. Evidence and hypotheses, kept apart

**Established by evidence**
- E-1. In the QA-100 venue, the delivered tool exited 4 twice on the same tested source, with the read-only stderr line and no result line (§4).
- E-2. In that venue the source checkout's tree, ignored files, directories, HEAD and status stayed unchanged. Only the guard's git-metadata comparison failed (§5; results §5.2).
- E-3. `make_copy()` uses `git clone --shared`, and `_metadata_digest` includes the mtime and ctime of every file under `.git/objects/` (§3).
- E-4. Writing, inside a `--shared` copy, an object the source repository already packs updates the source pack's mtime and ctime under git 2.43.0 (Kronos) and git 2.53.0 (executor). The tool's own `repository_state()` then reports a `metadata` difference (§4).
- E-5. The same command exited 0 with "repository unchanged" in two earlier venues (§6).
- E-6. The execution-1 replay failure was a venue cause (`TMPDIR` on a different filesystem from `/tmp`). Removing it did not change the exit 4 (§4).

**Hypotheses** (none is proven; listed for Thoth's diagnosis, not ranked)
- H-1. During step 1, a replayed or reporting step wrote, inside a `--shared` copy, an object the source clone already packs. Git then freshened the source pack, and the guard's lstat digest changed. This is consistent with E-3 and E-4, but which step wrote and which file changed were not observed.
- H-2. The venue difference comes from git's version (2.53.0 against 2.43.0). Some operation the replay or a report performs may write, or freshen, an existing object under 2.53 that it does not under 2.43.
- H-3. The difference comes from the source repository's object layout. Examples are a source made by a plain `git clone` from GitHub against a `--no-hardlinks` local clone, or loose against packed objects after the source's earlier use for checks 1 to 12, 14 and 15. Under this hypothesis, the objects a step rewrites exist in the source in one venue and not in another.
- H-4. Another `.git` file changed during step 1, for example the index, logs, a maintenance lock, `FETCH_HEAD` or a commit-graph file. The post-run inspection, which followed step 3, could not show it. The tool's stated limit "concurrent git activity in the checkout fails the read-only check (IF-35-24)" (addendum 2.12, LR6-O7) belongs to this family. No concurrent activity in the source is recorded for either execution.

## 8. Facts Thoth must resolve

1. **Which file.** Which `.git` path of the source changed during step 1, and in which field (mtime, ctime, size or bytes)?
2. **Which step.** Which report, and which replayed step, made the change?
3. **The venue.** Why the guard held at `fc51620` and at `0b15328d` and did not in the QA-100 venue (H-2, H-3 or another cause), and whether a git ≥ 2.53 venue, such as a Claude Code cloud container on ubuntu-26.04 or the operator's workstation, reproduces it on demand.
4. **The meaning of a timestamp-only change.** Whether a timestamp-only change to a pack file, made by git's own freshening, is a "write to the repository" under S20 as ID-2 reads it ("No report may create, modify or delete any file there"). That is, whether the defect lies in the copy mechanism, in the guard's precision, or in both. This is a reading for Thoth, then Isis, to settle. If it would change S20's approved meaning, it is a Specification decision (ESC-30 step 5).
5. **The Product Owner decisions that bear on scope** (§9).
6. **O-1.** Whether the OPS03 tests' cross-device failure is in scope for this change (§10).

## 9. Affected requirements, dependencies and impacts

- **S20 / check 13:** not met in the QA-100 venue. Steps 2 to 4 and four of the five reports are met (§11).
- **Close of HDE-CRD-0002 (S21's writer):** blocked while check 13 stands as `FAIL_BEHAVIOR`. Under addendum 2.17 resolution A, a check recorded `FAIL_BEHAVIOR` blocks a v2 `SATISFIED` decision.
- **Whole-change QA:** the QA-120 report and verdict wait on this check and on Plan checks 16 to 21. Those checks are unselected and independent of this finding (review §10).
- **Check 21 (S22):** depends on checks 1 to 20 being published (Plan §8). Check 13 is published (as `FAIL_BEHAVIOR`), so this finding does not block publication. Check 13's later verification republishes the same `check_id` (Glow QA Guide §3.4.3).
- **Open Product Owner decisions that bear on scope. Not decided here, and named so that Thoth does not miss them:**
  - **D-1 / LR6-O1** (addendum 2.12): "whether S20 is removed by a later Specification delta".
  - **FND-028** (addendum 2.26; addendum 2.16, "Option A line"): "option A stop rule met: no PR-40 review of WU-PR-07, WU-PR-08 or WU-DOC-01 recorded a hosted CI failure a local replay would have caught; removal of the replay report is a later change, the Product Owner's decision".

  Either decision would change approved scope and goes through its native route (ESC-30 step 5; addendum 2.11 rule 3). Neither is a remedy this report selects.
- **Related standing rules:**
  - Addendum 2.11 rule 7, as narrowed by addendum 2.14: "fix only a wrong result on a real input, or a breach of the read-only or no-secrets guarantees". PO-35-6: "A snapshot-precision finding is a hypothetical-input finding unless it shows a write that the tool itself, or code it runs in the checkout, can make".
  - QA110-F01 rests on a real input, the operator's shell (addendum 2.11 rule 4(b)).
  - Rule 8, repeated finding class: WU-PR-06's class C findings (snapshot precision; addendum 2.11) concerned the guard missing writes. QA110-F01 concerns the guard reporting a change the source's content does not show.
- **Accepted-final lineage:** WU-PR-06 is accepted (addendum 2.12) and is not reopened by QA. A repair is a new routed work item under Glow QA Guide §10.6, as WU-REM-01 was for FND-001.
- **Product Owner direction PO-2** (`docs/ephemeral/HDE-CRD-0002-po-direction-tool-version-pinning-v1.0.md`; `PENDING_DRAINAGE`): "Function matters, not tool versions." It bears on whether a git-version-dependent result is acceptable. It is not canon yet and decides nothing here.
- **Not affected:** production, the deployed service, release identity (1.3.0; `release_id` `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`), and every release member. `tools/ci/prepush_check.py` is not a release member. S20's Live QA class is "Not production-affecting".

## 10. Second observed failure in the same check (O-1)

- **What failed:** execution 1's replay failed `tests/ops/test_hde_epic038_ops03.py::test_candidate_replacement_failure_is_persisted_before_cleanup` and `::test_validator_rejects_authorized_candidate_symlink`.
- **Why:** the OPS03 tool's fixed `RUN_ROOT` `/tmp/hde-epic038-ops03` (tmpfs) and pytest's `tmp_path` under `TMPDIR` (ext4) are on different filesystems, and a link or rename between them fails with `EXDEV`.
- **What it is, and is not:** a repository-test portability failure in a real venue. S20's replay reported it truthfully. It is not the S20 defect, and no HDE-CRD-0002 requirement names OPS03.
- **Owner:** Thoth decides whether it is in scope. If it is independent, it needs separate Product Owner disposition (Glow QA Guide §3.4.8, "An independent or opportunistic defect requires separate Product Owner disposition").
- It changes neither the QA-110 decision nor this report's finding.

## 11. Why ordinary completion or the bounded rerun cannot resolve it

- The defect is in the delivered tool's design or in its reading of S20 (E-3, E-4). A venue cause has already been removed without changing the result (E-6). QA-110 Execute rule 3 allows a bounded rerun only when "the sole defect is an execution/evidence fault".
- Check 13's one ordinary rerun is consumed (review R-2).
- The repair touches `tools/ci/prepush_check.py`, its owner test or S20's reading. That is non-QA-root remediation, which no Moon Loop can make (Glow QA Guide §3.4.8; Plan §9).
- Plan §9 routes "any `FAIL_BEHAVIOR`" to the ESC-10 remediation route. Glow QA Guide §10.6 does the same for a "behavior defect".

## 12. Preserved results, residual state, containment and return

- **Preserved valid results (QA-110 `ACCEPT`):**
  - checks 1 to 12, 14 and 15 (T01 to T12, T14, T15), with their primaries on `main`;
  - check 13's steps 2 to 4;
  - its lanes, membership, build-notes and sweep reports, at their predicated values;
  - its replay's 16 `SUCCESS` steps in execution 2.

  These are not reopened by this finding.
- **Residual state outside the repository** (results §9; review O-3): uv CPython 3.13.17 on the workstation; two OPS03 test directories under `/tmp/hde-epic038-ops03/`; the QA-100 evidence checkout and working files. Owner: the Product Owner. None affects production or the repository.
- **Containment:** none is needed and none is authorized. The tool is a local developer tool. It changes no tracked, ignored or working-tree file of the source in either run (E-2), and it is not part of hosted CI.
- **Verification owner and return point:**
  - Kronos, at QA, for check 13 after an approved repair is delivered and accepted (Glow QA Guide §10.6 step 5: "Later QA retains Kronos's evidence/Plan responsibilities and actual return stage").
  - If the approved repair leaves Plan v1.2 check 13's objective, target, predicates and outcome map valid, the verification runs as a QA-90 task for check 13 under the remediation return. That task is not an ordinary attempt 2, and it does not reset attempts.
  - If the repair changes check 13's predicate, target or scope, Plan v1.2 is revised first through QA-80 and QA-70.
  - Which applies follows from the approved remedy. This report does not decide it.

## 13. Risks

- **Venue-dependent green.** A repair verified only in a git 2.43 venue could pass there and still fail on the operator's workstation, because both earlier passing venues were 2.43 or unrecorded (§6).
- **Over-correction.** Narrowing the guard could hide a real write to the source; S20's read-only guarantee is a breach class under addendum 2.11 rule 7. Leaving the copy mechanism unchanged could leave the freshening path open.
- **Scope drift.** The open decisions D-1 and FND-028 could make part of a repair moot. Choosing a remedy that presumes either decision would bypass its owner.
- **Test-suite hazards in the replay:**
  - PR35-C1 (addendum 2.21): git auto-maintenance in `tests/tools/test_prepush_check.py` on git 2.55.0;
  - OBS-17;
  - O-1.

  These can make a verification run red for reasons other than QA110-F01. Plan v1.2 check 13's Outcomes classify the PR35-C1 signature as `FAIL_TOOLING`.

## 14. ESC-30 intake (complete)

| ESC-30 required input | Provided |
| :- | :- |
| `ORIGINATING_FINDING_REF` | This `QA_ESCALATION_REPORT` (finding QA110-F01), with its intake `docs/ephemeral/HDE-CRD-0002-QA110-qa-evidence-review-v1.0.md` §6 |
| Change and class | CRD HDE-CRD-0002 |
| Originating prompt, owner, session and return point | QA-110, then ESC-10; Kronos (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV); return point §12 |
| Approved Specification | Specification v1.1-approved with delta 01 (§2) |
| Affected immutable Plan, Guide, QA Plan and reviews | Implementation Plan v1.1 (WU-PR-06 block, acceptance (1)) with delta 01 and the FND-001 overlay; WU-PR-06 instruction v1.0 (ID-2, ID-3) and plan v1.0; QA Plan v1.2 (check 13, §7 rule B, §9) with the QA-70 review v1.2; Live QA Guide v1.0; QA Audit v1.0 §7 item 9 |
| PF canon, PF10 and addenda | HDE Build Notes v13.7.8, read completely. Applicable: 2.11 (rules 4 to 8, as 2.14 and 2.18 narrow them), 2.12 (WU-PR-06's acceptance, stated limits and D-1), 2.14, 2.16 (option A line), 2.17 (resolution A), 2.18, 2.21 (PR35-C1), 2.23 to 2.26 (the FND-001 cycle and FND-028). Glow QA Guide §2.2.11, §3.4.8, §10.6 |
| Repository and environment evidence | §2, §4, §6; the check 13 primary on `main`; QA-100 results §2 and §5.2 |
| Conflict register | §15 |
| Continuing lineage | Thoth (remediation author); Isis (ESC-40, decision owner); the whole-change Implementation Agent and its PR lanes for delivery (Glow QA Guide §10.6 steps 2 to 4) |
| Discovery results, attempts, delivery evidence, prior proposal and Isis redlines | Attempts in §4. No discovery, delivery, prior proposal or redline exists for QA110-F01 |

## 15. CANON_CONFLICT_REGISTER (carried)

Carried unchanged from QA Plan v1.2 §13, the QA-90 collection §6, the QA-100 results §10 and the QA-110 review §12. The full entries are in Plan v1.2 §13. ESC-10 adds none: the finding is a behavior defect, and §8 item 4 is a reading question for Thoth and Isis, not a recorded conflict between sources.

| Entry | Status | Reviewer / record |
| :- | :- | :- |
| CR-1 to CR-3 | `APPROVED_AS_CHANGED` | Thoth; Specification v1.1 lineage |
| CR-4 | `APPROVED` | Product Owner; WU-PR-01 disposition §2 |
| CR-5 | `APPROVED_AS_CHANGED` | Product Owner; same record §3 |
| CR-6 | `APPROVED`, alternative (a) | Implementation Agent through RS-20; addendum 2.6 |
| CR-7, CR-8 | `APPROVED`, alternative (a) | Product Owner direction of 2026-10-14; addendum 2.7 |
| CR-9 | `PROPOSED`; unreviewed | Isis, IA-30 boundary |
| CR-10 | `APPROVED`, alternative (a) | Isis, ESC-40; addendum 2.24 |
| CR-11 | `APPROVED_AS_CHANGED`, alternative (a) | QA-70 review v1.0; applied in check 1 |

## 16. TypeSafe reading for the receiving session (ESC-30)

Action sent (v8.2): "Diagnose one escalated QA failure of a delivered developer tool, already described in a QA escalation report: a read-only pre-push command whose repository-unchanged guard reports a violation in one venue but not in two earlier ones, while every report it runs passes. Separate the proven cause from the hypotheses, and either author one bounded discovery task or one new, complete, bounded remediation proposal covering the affected requirement, code, tests, verification and the delivery and return owners, without implementing or approving it. No task list exists; no live run against a provider occurs; an independent remediation review follows; the work is one unit, not many independent units."

The reading as printed by the script:

- **TypeSafe v8.2: Fable 5.1 at high.** Effort score 2.36 (confidence 0.74); rung probabilities low 0.00, medium 0.02, high 0.72, extra high 0.15, max 0.11, ultracode 0.00. Model probabilities Fable 5.1 0.70, Opus 5.5 0.22, Sonnet 5.5 0.08, Haiku 5.5 0.00 (confidence 0.60). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.014, Fable 5.1 at high 0.504, Fable 5.1 at extra high 0.105, Fable 5.1 at max 0.077, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.004, Opus 5.5 at high 0.158, Opus 5.5 at extra high 0.033, Opus 5.5 at max 0.024, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.002, Sonnet 5.5 at high 0.058, Sonnet 5.5 at extra high 0.012, Sonnet 5.5 at max 0.009, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-25T01:37:40Z. Nathan picks the cell.
- **Detail (as printed):** v8.2 sent 2026-10-25T01:37:40Z; HTTP 200 in 0.55 s; 5475 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Fable 5.1 (the most probable of the four options, a tie going to the higher-priced model). Flags: none printed.
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "ESC-30 HDE-CRD-0002 QA110-F01 diagnosis and remediation proposal", before this report was saved.
- **Records:** the Notion row was not written.
- **Picks:**
  - ESC-30: Nathan's pick is not stated.
  - This ESC-10: Nathan's pick is not stated. Its reading is in the QA-110 review §14 (Sonnet 5.5 at high, score 1.68).

**Surface advice for ESC-30.**
- **Session:** the continuing Thoth session for HDE-CRD-0002 (https://claude.ai/code/session_01QDA4Gim8zTtX2KqAEWnaum), or a top-level Claude Code session the Product Owner creates for that role, on `amthorn78/glow-hdengine-v2`. Notion read access is needed for the prompt.
- **Reads:**
  - this report;
  - the QA-110 review §6;
  - the check 13 primary and the QA-100 results §5.2;
  - `tools/ci/prepush_check.py` (`main`, `repository_state`, `make_copy`, `_metadata_digest`, the replay) and `tests/tools/test_prepush_check.py`;
  - the WU-PR-06 instruction (ID-2, ID-3), plan v1.0, lineage review v1.0 and postmortem v1.1;
  - Plan v1.2 check 13;
  - HDE Build Notes addenda 2.11, 2.12, 2.14, 2.16, 2.18, 2.21, 2.26.
- **Venue for discovery:** answering §8 items 1 to 3 needs a shell with git 2.53 or later (the observed failing version) as well as git 2.43. A fresh full-history clone with CI's full install on Python 3.12 under closed rails is also needed. One run of the full command takes about 24 to 40 minutes. A narrower instrumented run is a discovery design choice.
- **Not needed:** production, vendor, Railway or database access.
- **Writes:** only its remediation record, a discovery task if one is needed, the checkpoint and the handoff under `docs/ephemeral/`, by pull request.

## 17. Nonclaims

This report records an escalation. It chooses no remedy, diagnoses no root cause beyond the evidence in §7, executes no QA or Ops, and changes no product, test, generator, governed artifact or PF file. It approves nothing. It does not establish or withdraw:
- a QA verdict, acceptance or closure;
- deployment;
- PF09 or PF30 movement;
- any Product Owner decision named in §9.

## Canon relied on

Read from `docs/pfcanon/` on `main` at `dba9e09`; this branch edits no `docs/pfcanon/` file.

| Topic | Governing source read |
| :- | :- |
| The report's contract, intake and routing | ESC-10 — Create QA Escalation Report — 100926.1 (page state 2026-10-12T02:29:32.722Z), read in full: "Required inputs", "Execute" 1 to 4, "Required result", "Result routing" |
| The receiver's intake | ESC-30 — Diagnose and Propose Bounded Remediation — 100926.1 (page state 2026-10-12T02:29:51.552Z), read in full: "Required inputs", "Execute" 1 to 6, "Result routing" |
| HDE Build Notes | `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md`, read completely at this invocation: front matter §1 to §9 and addenda 2.1 to 2.26. Applicable to this finding: 2.11 rules 4 to 8; 2.12 (WU-PR-06's acceptance, the read-only checks at `fc51620`, LR6-O1 and LR6-O7); 2.14 rules 1 to 6; 2.16 ("Option A line"); 2.17 resolution A; 2.18; 2.21 (PR35-C1); 2.23 to 2.26 (the FND-001 cycle as precedent; FND-024, FND-028) |
| The remediation route and the return owner | PF19-Canon-Glow-QA-Guide v3.0.6 §10.6 "Common remediation cycle and return owner", read in full |
| Moon Loop limits and independent defects | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.8, read in full |
| The non-mutating rule | PF19-Canon-Glow-QA-Guide v3.0.6 §2.2.11 "Evidence-governed CI sequence (names-only)", read in full |
| Stable check directory on republication | PF19-Canon-Glow-QA-Guide v3.0.6 §3.4.3 (opening) |
| Classification | PF27-Canon-Plan-Templates v2.0.5 "Exact status predicates" and "Causal precedence" (read at QA-110 in this session) |
| Real input | `AGENTS.md` "Code review guidelines" (repository rule) and addendum 2.11 rule 4 |
| In-flight documents | The QA-110 review v1.0 (author's own record), the QA-100 results v1.0 and the check 13 primary (read in full at QA-110), QA Plan v1.2 check 13 and §9, the Specification v1.1 S20 row, the WU-PR-06 instruction v1.0 (§3, ID-2, ID-3, §5.8), the WU-PR-06 postmortem v1.1 (D-1 rows) and the remediation review FND-001 v1.1 (lineage) |

## Provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | GCFPE-USE-HDE-CRD-0002-ESC-10-20261025-01 |
| change | CRD HDE-CRD-0002 (Specification v1.1-approved with delta 01) |
| unit | Requirement S20; QA Plan v1.2 check 13 `qa-13-prepush-check`; task T13, attempt 1; finding QA110-F01 |
| prompt | ESC-10 — Create QA Escalation Report — 100926.1, page state of 2026-10-12T02:29:32.722Z |
| release | GCFPE-20261009.1 / 100926.1 |
| role/stage | Kronos, ESC-10 (`AWAITING_THOTH_REMEDIATION`) |
| capture time | 2026-10-25T01:40:00Z |
| execution identity | https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV (no worker subagents) |
| earlier uses | GCFPE-USE-HDE-CRD-0002-QA-110-20261025-01 and those it lists, each in its artifact |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); owner: the authorized repository writer when the procedure is installed |
