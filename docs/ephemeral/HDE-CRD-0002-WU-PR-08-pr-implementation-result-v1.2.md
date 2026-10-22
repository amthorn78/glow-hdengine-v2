---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-08-PR-IMPLEMENTATION-RESULT
artifact_version: "1.2"
result_state: CHECKPOINT (PR-35 in progress). v1.1's MERGE_PENDING is withdrawn; the run on this record's own commit decides the next state (§5)
phase: PR-35 (review resolution and merge readiness), dedicated session
predecessor: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-result-v1.1.md (v1.1, MERGE_PENDING; preserved unchanged, withdrawn for state by this record)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-08
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-instruction-v1.0.md (v1.0)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-08-pr-implementation-plan-v1.0.md (v1.0)
lineage_ids: as v1.1's front matter (Specification, Implementation Plan and delta, reviews, PF10 v13.7.1 and addenda); unchanged
proceed: Nathan / Product Owner, PR Implementation Proceed for exactly plan v1.0 (unchanged; no second Proceed)
sessions: PR-30 https://claude.ai/code/session_01QezXHuju1GXwpubx7zDvTA; PR-35 https://claude.ai/code/session_01VASdh3cjEKqEVYa35EwCEn
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e)
primary_skill: glow-hde-pr-development 1.4.0
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/687 (open)
branch: claude/awesome-einstein-ig69r1 (PO-35-1, v1.1 §7)
base: origin/main 977a9c7f13db9302d33670494f77549cdbf6d5dd
previous_head: e1cb6d18e701b816ad8d54a1bbc470a02c09cd97 (v1.1's commit)
implementation_commit: 9b93cf0e36121260ceb694cea91fa3546863ca4d (unchanged; no PR-35 correction)
created_at: 2026-10-22T00:01:00Z
canon_conflict_register: CR-1 to CR-8 carried unchanged; no new entry
---

# HDE-CRD-0002 WU-PR-08 — PR implementation result v1.2 (PR-35 checkpoint)

## 1. State

**v1.1's `MERGE_PENDING` is withdrawn.** v1.1 said a failed run on its own commit would withdraw it, and that run failed.

- **What failed:** one test in `tests/tools/test_prepush_check.py`, which WU-PR-06 delivered and this PR does not change (§2, §3).
- **The code under test** is the same as on `bf32d20`, whose run passed all seven lanes. `git diff bf32d20 e1cb6d1 -- . ':(exclude)docs/ephemeral'` is empty.
- **Codex reviewed `e1cb6d1`:** no findings (§4).
- **This record's own commit** gets one hosted run on the same code. That run is the confirming run (§5).

This record is not a merge, QA verdict, acceptance, Ops act or closure.

## 2. The failure

Run 39695867041, job 119552964702, `test`, on `e1cb6d1`, 23:49:26Z to 23:55:58Z: **failure**.

| Item | Value |
| :- | :- |
| Image | `ubuntu-26.04` 20261018.168.1; git 2.55.0 (the same image and git as the passing run 39693139601 on `bf32d20`) |
| Classification | `reason=selected_lanes;paths=5;lanes=product,compat,db,rails,evidence,qa,release` |
| Changed-tests step | **1 failed**, 4,520 passed, 2 skipped, in 366.94 s. The step exited 1, so the lane steps did not run, and the final step failed |
| The failing test | `tests/tools/test_prepush_check.py::test_build_notes_requires_exactly_one_file[names2-False]` (`tests/tools/test_prepush_check.py:83`, the test's read-only assertion in `_run`) |
| The tool's own output | `build-notes: FAILURE expected exactly one … found 2` (the test's expected result), then `PREPUSH_CHECK_RESULT: FAIL build-notes=FAIL; repository unchanged (tree, ignored files, directories, HEAD and git metadata)` |
| The assertion's diff | only one item differs between the test's `before` and `after` snapshots of its synthetic repository: `.git/objects`, size 260 → 240 and mtime and ctime 1792626945094981634 → 1792626945095981623. That is one entry fewer, about 1 ms later. Every other entry is identical ("Omitting 57 identical items"), and no key is added or missing |

**Log coverage.** `get_job_logs` returned the last 1,500 of the log's 1,512 lines. The 12 not returned are the runner-provisioning header that comes before the image group.
- **Read directly:** the returned lines 440 to 500, 715 to 740 and 840 to 937 (the failure, the assertion and its whole snapshot diff), and 1,388 to 1,392 (the step result).
- **Scanned:** the rest, for step results, errors and the git version.

## 3. Cause (probable) and disposition

**Probable cause: a race in the test fixture, not in the tool.**

1. `_synthetic` (`tests/tools/test_prepush_check.py` line 106) builds the repository with `git commit`, through `_git` and `IDENTITY` (lines 33 and 46). Neither disables automatic maintenance.
2. git's documentation (git-scm.com, `git-maintenance`, read 2026-10-21):
   - `maintenance.auto`: "controls whether some commands run `git maintenance run --auto` after doing their normal work. Defaults to true."
   - `maintenance.autoDetach`: "controls whether this automatic maintenance shall happen in the foreground or whether the maintenance process shall detach and continue to run in the background. … Defaults to true if both are unset, meaning that the maintenance process will detach."
   - "Each `git maintenance run` command takes a lock on the repository's object database."
3. So on the runner's git 2.55.0, `git commit` can return while a detached maintenance child still holds, and then releases, a lock entry in `.git/objects`.
4. The diff fits that exactly. `os.walk` reads `.git/objects`'s `lstat` (size 260, with the extra entry) before it lists that directory. By the listing, the entry was gone, so neither snapshot names it. The directory then reads 240 with a mtime 1 ms later.
5. The tool's own before-and-after check, which starts after that moment, reports "repository unchanged".

**Not reproduced locally.** This container has git 2.43.0. The same test passed here on `bf32d20` (v1.1 §4 row 4), on the runner on `bf32d20` (run 39693139601), and at PR-30. The mechanism is therefore stated as probable, from the log and the git documentation.

**Disposition:**
- **Not this PR's.** The test and the tool are WU-PR-06's (#660, accepted; `git log` shows only `b963ed4` for the test file). Neither is in this PR's diff. This PR runs the test because its classifier change selects every lane and 166 changed-test targets (plan §13.1).
- **Real input, real defect, routed.** The input is the hosted CI runner, a real input under PF10 addendum 2.11 rule 4(b). It is a test-robustness defect in another unit's test, with no finding against this PR's code.
- **No fix exists.** #687 is the only open PR, and `main` has not changed the test since `b963ed4`.
- **Not applied here.** Plan v1.0 §9 and §20 limit this PR to three files. While a run on the unchanged code can pass, the fix is not necessary to deliver WU-PR-08 (glow-hde-pr-development, "Decide it during work", step 3), so it is recorded as a candidate for its owner.
- **Candidate PR35-C1** (owner: the whole-change IA, through PR-40, as a later-change candidate for the Product Owner). Proposed patch, untested: in `tests/tools/test_prepush_check.py`, add `"-c", "maintenance.auto=false"` to `IDENTITY`, so that the fixture's `git commit` starts no maintenance child:

  ```diff
  -IDENTITY = ("-c", "user.name=prepush-test", "-c", "user.email=prepush-test@invalid", "-c", "commit.gpgsign=false")
  +IDENTITY = ("-c", "user.name=prepush-test", "-c", "user.email=prepush-test@invalid", "-c", "commit.gpgsign=false",
  +            "-c", "maintenance.auto=false")
  ```

## 4. Reviews on the current head

- **Codex code review of `e1cb6d1`,** trigger "New commits": running from 23:49:26Z, completed 23:50:34Z, `has_any_findings: false`, `has_unresolved_findings: false` (summary comment [6328780869](https://github.com/amthorn78/glow-hdengine-v2/pull/687#issuecomment-6328780869)).
- **Threads and reviews:** 0 review threads; 0 formal reviews.
- **Relation to v1.1 §3:** v1.1 explained why no review was requested. Codex then reviewed the new commit on its own (trigger "New commits"), so the current head has a review of its own. No request was made.
- **Security review:** not in the chain (PF10 addendum 2.3).

## 5. Next: the confirming run, and what each outcome means

The run on this record's commit is the one confirming run on the unchanged code. No separate re-run of run 39695867041 was requested: this push would cancel it under the workflow's pull-request concurrency rule (`ci.yml` lines 39–40).

| Outcome | Meaning |
| :- | :- |
| Success, with all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | Every predicate of v1.1 §2 holds on this record's commit. The run on `e1cb6d1` was the §3 race, and PR35-C1 carries the fix. The session returns `MERGE_PENDING` for this commit and names the run in its final response. This record is then the final checkpoint: each further record commit would start another seven-lane run that tests nothing new. PR-40 verifies the run independently |
| Failure of the same test | A second failure on the same code is treated as real. The session stops treating it as intermittent and asks the Product Owner one question: apply the PR35-C1 patch in this PR (a fourth file, outside plan §9), or route it to a separate change |
| Any other failure | Root-caused as new evidence before any other action |

## 6. In-flight decisions

NONE. No code, test or plan was changed. Routing the failing test's fix as PR35-C1 is a recorded candidate, not a change.

## 7. PR_REMOTE_ACTION_LEDGER (continues v1.1 §8)

| # | Time (UTC) | Action | Outcome |
| :- | :- | :- | :- |
| 14 | 23:49:19 | Push `bf32d20..e1cb6d1` (v1.1); remote head read back; v1.1 read back (23,577 bytes, sha256 e418bb8d…, blob e8801e83) | pushed |
| 15 | ~23:49 to 23:50 | #687 description: PR-35 local re-run and hosted CI on `bf32d20` added under "Checks run" | updated |
| 16 | 23:49:26 to 23:50:34 | Codex code review of `e1cb6d1` ("New commits") | no findings |
| 17 | 23:49:26 to 23:55:58 | Run 39695867041 `test` on `e1cb6d1`; `check_run.completed` delivered 23:56:01Z | failure (§2) |
| 18 | 23:56 to 00:00 | Log read (§2); fixture and helpers read; git documentation read; open PRs listed (only #687); TypeSafe v8.2 re-read for the PR-40 handoff (§8) | cause probable (§3); no existing fix |
| 19 | next | One comment on #687 naming the failing check, why it is not this PR's, that no fix exists, and the proposed patch; push this record; observe the confirming run through the subscription | — |

Safety-net check-in `trig_0167bFDgNL8RWusvjok3Pog4`, due 2026-10-22T00:24:00Z, stays armed.

Remaining useful local action: none. Next evidence action: the confirming run.

## 8. TypeSafe reading for the PR-40 handoff (replaces v1.1 §9's reading)

v1.1's reading was taken on facts that have since changed: 3 commits then, 4 now, and one failed run. So the reading was taken again, once, on the revised text. The installed TypeSafe scoring skill's `score_v8.py` and `request-v8.2.json` were used, session kind `review`, label "PR-40 — HDE-CRD-0002 WU-PR-08 (revised)". The reading, as the skill prints it:

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.97 (confidence 0.66); rung probabilities low 0.00, medium 0.27, high 0.49, extra high 0.24, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.98, Sonnet 5.5 0.02, Haiku 5.5 0.00 (confidence 0.97). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.265, Opus 5.5 at high 0.480, Opus 5.5 at extra high 0.235, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.005, Sonnet 5.5 at high 0.010, Sonnet 5.5 at extra high 0.005, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-22T00:00:03Z. Nathan picks the cell.
- **Detail:** v8.2 sent 2026-10-22T00:00:03Z; HTTP 200 in 0.47 s; 5545 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model). No flag was printed.
- **Action text sent:** "Independent post-merge lineage review of one already-reviewed pull-request work unit, HDE-CRD-0002 WU-PR-08 (requirements S16 and S17): check against the repository that merged pull request #687 (4 commits; three existing files changed by about 20 lines: one placeholder key in an environment template, six corrected readiness and port statements in an operator document mapped line by line in the plan, one entry in a CI change classifier; plus three record files) delivered the work unit's five acceptance items from its existing instruction and plan; two Codex review rounds with no findings, no Product Owner design decisions in the review phase, hosted CI green on all seven lanes on the reviewed head, and one later run on identical code that failed on an intermittent test outside the change, recorded with its cause and routed to its owner. There is no live run of new code against a provider, and QA and the change's close gate follow as later independent gates."
- **Records.** The Notion row was not written (the PR-35 prompt's handoff rule; PF10 addendum 2.1). Nathan's picks for PR-40 and for this session are not stated.

**Surface advice for PR-40:** as v1.1 §9, plus GitHub read access to runs 39695867041 and the confirming run.

## 9. Unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| The confirming run on this record's commit | this session, through the subscription | pending at writing (§5) |
| PR35-C1, the fixture race in `tests/tools/test_prepush_check.py` | the whole-change IA, through PR-40; then the Product Owner | candidate with a proposed patch (§3) |
| Merge of #687 | Product Owner | not yet: it waits on the confirming run |
| F-1, F-2 and the plan §18 carried items | as v1.1 §11 | unchanged |

**Nonclaims:** as v1.1 §11. This record is not intended to support a later PF-canon drain and recommends no status change.

## 10. Prompt-use provenance (GCFPE_PROMPT_USES)

As v1.1 §12, with: usage HDE-CRD-0002 / WU-PR-08 / PR-35 / result 3 (v1.2); capture time 2026-10-22T00:01:00Z.

## Canon relied on

As v1.1 "Canon relied on", which this record applies without change. In addition:

| Decision topic | Sources | How it governs here |
| :- | :- | :- |
| The failing run: whether the input is real, and the disposition | PF10-HDE-Build-Notes v13.7.1, addendum 2.11, rules 4(b) and 5 (read in full this session) | the runner is a real input, so the defect is real; it is routed to its owner, not declined and not modelled |
| Scope: no widening of the PR | plan v1.0 §9 and §20; glow-hde-pr-development 1.4.0, "Decide it during work" | the fix is a candidate for its owner (§3) |
| CI economy: one confirming run, no empty commit, no suppression | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, "Review-first and action-efficient execution" steps 6 to 9 and "Remote-action ledger and durable checkpoints" | §5: this checkpoint's commit carries the confirming run; no `[skip ci]` |
