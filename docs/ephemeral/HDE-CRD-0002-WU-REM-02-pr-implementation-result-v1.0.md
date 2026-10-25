---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-REM-02-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result: PR_CANDIDATE_PUBLISHED
phase: PR-30
predecessor: none (the first result for WU-REM-02)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-REM-02
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-implementation-plan-v1.0.md (v1.0, AWAITING_PO_PROCEED at issue; blob a68208664607; #733, squash a2c6d8f), with docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-implementation-plan-v1.0-prototype.diff (blob 32a3e5272805; sha256 8e1a93ba2c0948c3e8e1b9313c5f80413664258e4d29e59737d76dd6120dcd96)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 54409080c04f; #732)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd44), with Plan delta 01 v1.1
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1; blob c4802a5a7fa3), S20, with Specification delta 01
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
REMEDIATION_REVIEW_ID: HDE-CRD-0002-REMEDIATION-REVIEW-QA110-F01 v1.0, docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md (APPROVE_AS_CHANGED, C-1)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.7.9.md (sha256 204a7ad6de7167678503819e31dee42fdd6d7d58135e51725975fcbdd37dbe4e; read as provenance; §2.27 the remedy)
effective_baseline: approved base + applicable PF10 overlays, as plan v1.0 front matter states
proceed: the Product Owner's invocation of PR-30 — PR Implementation Proceed — 100926.1 for plan v1.0, pasted into this session on 2026-10-25, after #733 merged (verified: origin/main a2c6d8f carries the plan blob a68208664607 and the diff blob 32a3e5272805)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: https://claude.ai/code/session_01SPJuyNDoQNA2MrC44oFKSs (the dedicated WU-REM-02 PR engineering session; PR-20, then PR-30)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository_baseline: origin/main a2c6d8f (#733). Against the plan's baseline 6246993 it adds only the plan and its diff under docs/ephemeral/
branch: claude/hde-crd-0002-pr-plan-66tkpi (the session's designated branch; its PR-20 pull request #733 was merged, so it was restarted from origin/main a2c6d8f)
pull_request: https://github.com/amthorn78/glow-hdengine-v2/pull/734
implementation_commit: 0245b77dec1d5cf95f7f98755c953a8e4c52e288 (parent a2c6d8f)
next_prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e), in its own dedicated session
created_at: 2026-10-25T13:52:00Z
canon_conflict_register: carried unchanged from plan v1.0 §19; no new entry
---

# HDE-CRD-0002 WU-REM-02 — PR Implementation Result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** The approved three-file change is implemented, tested locally and published as [amthorn78/glow-hdengine-v2#734](https://github.com/amthorn78/glow-hdengine-v2/pull/734), head `0245b77`.

- The commit is plan v1.0's companion diff applied byte for byte: the three resulting blobs equal plan §7's (`b0d5319c5309`, `d852682656dd`, `343550ed715a`), 3 files, +164/−19.
- V-1 to V-3 and the pre-push check pass on `0245b77` (§4).
- V-4 (hosted CI), review resolution and merge readiness are PR-35's. This result claims none of them.

## 2. Recovery and baseline (plan §8 steps 1 and 2)

| Checked | Found |
| :- | :- |
| Open pull requests on the repository | none |
| Remote branches for this work unit | none; `claude/hde-crd-0002-pr-plan-66tkpi` was deleted after #733 merged |
| `docs/ephemeral/HDE-CRD-0002-WU-REM-02-*` on `main` | the instruction v1.0, the plan v1.0 and its diff; no result record |
| Local checkout and worktrees | one worktree, the session checkout, clean, on the designated branch at the merged plan commit `7fc500e` |
| `main` against the plan's baseline `6246993` | `a2c6d8f`; outside `docs/ephemeral/` nothing differs (`git diff --stat 6246993 a2c6d8f -- . ':!docs/ephemeral'` is empty), so the plan's §4 facts stand and no re-measure is needed |
| PF10 on `main` | v13.7.9, unchanged since the plan |

The designated branch was restarted from `origin/main` (`a2c6d8f`), because its earlier pull request (#733) is merged history.

## 3. Implementation (plan §8 steps 3 and 4)

1. `git apply --check`, then `git apply`, of `docs/ephemeral/HDE-CRD-0002-WU-REM-02-pr-implementation-plan-v1.0-prototype.diff` on `a2c6d8f`: clean.
2. `git diff --stat`: `tools/ci/prepush_check.py` +75/−18, `tests/tools/test_prepush_check.py` +87/−0, `README.md` +2/−1.
3. `git hash-object`: `b0d5319c5309`, `d852682656dd`, `343550ed715a`, as plan §7 states.
4. One commit, `0245b77` (`fix(ci): pre-push check copies own their objects and a read-only violation names what changed (HDE-CRD-0002 WU-REM-02, QA110-F01)`).

## 4. Validation (plan §10)

**Environment.** This cloud container: 4 CPUs, git 2.43.0, CPython 3.12.3, `ruby` 3.3.6, `bash`, `curl`. Closed rails through `env -i`: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `HOME` a fresh empty scratch directory per run, `USER`, `LOGNAME`, `SHELL` set, `PATH` the venv, `/usr/local/bin`, `/usr/bin`, `/bin`.
- Clones: `c1`, `c2`, `c3`, each a `--no-hardlinks` clone at `0245b77` of a full-history scratch clone (`shallow=false`, no alternates). Each has its own venv with CI's install (pip exit 0; `python -m pytest --version`: pytest 8.4.2).
- `c3` carries the V-3 revert as scratch commit `fa0e19ec` (5 lines), never pushed.
- Nothing from the clones is committed or pushed.

| # | Check | Command | Result |
| :- | :- | :- | :- |
| 1 | Classifier, as `ci.yml` calls it | `python3 ci/checks/classify_ci_changes.py --base a2c6d8f6990b24f1fe19ec02c3c729cada7b29de --head 0245b77dec1d5cf95f7f98755c953a8e4c52e288 --event-name pull_request …` in `c1` | exit 0; `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=3;lanes=product,release`; `changed_tests=true`; one target, `tests/tools/test_prepush_check.py` |
| 1 | AGENTS citations | `python3 ci/checks/check_agents_md_citations.py` in `c1` | `AGENTS_MD_CITATIONS_OK`, exit 0 |
| 2 | **V-1** | `PYTHONPATH=<c1> python -m pytest -q -p no:cacheprovider tests/tools/test_prepush_check.py` in `c1`, 13:16:23Z to 13:18:54Z | **141 passed in 150.32s**, exit 0; then `git diff --exit-code` clean and `git status --short --untracked-files=all` empty. It ran beside V-2 and V-3; plan §11.2 measured 108.0 s alone |
| 3 | **V-2** step 1 | `python tools/ci/prepush_check.py --full --path engine/cli/main.py --path docs/ADAPTER_009.md lanes membership build-notes sweep replay` in `c2`, 13:16:01Z to 13:49:30Z | **exit 0** in 2,009.6 s; stderr empty (0 bytes). Results below this table |
| 3 | V-2 step 2 | `python tools/ci/prepush_check.py --path docs/ADAPTER_009.md lanes` in `c2`, to 13:49:34Z | **exit 0**; `lanes: classification reason=documentation_only;paths=1;lanes=none`; result line `PASS … repository unchanged …` |
| 4 | **V-3** step 1 | the same step-1 command in `c3` (head `fa0e19ec`), 13:16:10Z to 13:28:00Z | **exit 4** in 709.4 s. Results below this table |
| 4 | V-3 step 2 | as V-2 step 2, in `c3` | exit 0; `documentation_only` |
| 5 | Pre-push check | `python tools/ci/prepush_check.py lanes build-notes` in the session checkout (shallow, at `0245b77`) | exit 0; lanes `base=origin/main->a2c6d8f`, `reason=selected_lanes;paths=3;lanes=product,release`, target `tests/tools/test_prepush_check.py`; `build-notes: path=docs/pfcanon/PF10-HDE-Build-Notes-v13.7.9.md bytes=530939 sha256=204a7ad6de7167678503819e31dee42fdd6d7d58135e51725975fcbdd37dbe4e`; "repository unchanged" |
| 5 | Pre-push check | `python tools/ci/prepush_check.py --path tools/ci/prepush_check.py --path tests/tools/test_prepush_check.py --path README.md membership` | exit 0; release 1.3.0, roster 45, `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; all three not-member; "repository unchanged" |

**V-2 step 1 results:**
- Reports: `lanes: classification reason=selected_lanes;paths=2;lanes=product,compat,release`; `membership: member engine/cli/main.py`, `membership: not-member docs/ADAPTER_009.md`; `build-notes` PF10 v13.7.9; `sweep: … uncovered=0`. All five `status=PASS`.
- Replay steps 01 to 16 `SUCCESS`:
  - step 08: "4527 passed in 692.97s";
  - product 77; compat 119 passed, 3 skipped, 2 xfailed; db 269; rails 138; evidence 134 (1,002.3 s); qa 488; release 79;
  - `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; "copy after replay: clean"; replay 1,993.1 s.
- Result line: `PREPUSH_CHECK_RESULT: PASS lanes=PASS membership=PASS build-notes=PASS sweep=PASS replay=PASS; repository unchanged (tree, ignored files, directories, HEAD and git metadata)`.
- Source state: `git status --porcelain` empty before and after. The pack (57,253,767 bytes) has mtime 1792903534.000000000 and ctime 1792934091.360047318 before step 1, after step 1 and after step 2.

**V-3 step 1 results:**
- stderr is the existing violation line, then seven lines:
  - `PREPUSH_CHECK_READ_ONLY_VIOLATION: changed: git metadata <c3>/.git/objects/pack/pack-d5d88524f3a45f030d6bdebc189ef5aeaece729e.pack (mtime, ctime)`;
  - six loose objects of the scratch commits, each `(mtime, ctime)`: `4b63625a`, `4d253409`, `6c11c8e9`, `c0cde982`, `d8526826`, `de63ceea`.
- Reports: `lanes`, `membership`, `build-notes` and `sweep` each `PASS`.
- Replay: step 08 `FAILURE`, "3 failed, 4524 passed". The three are R-4 (a) packed, (a) loose and (b): the copy carries the reverted code and the tests detect it. Step 16 `FAILURE`; `replay: status=FAIL`; no result line.
- Source state: status empty before and after. The pack's size is unchanged; its mtime and ctime moved to 13:27:03Z.

**Readings.**
- V-1 holds: 141 passed.
- V-2 holds: exit 0, every report `PASS`, and the repository unchanged, git metadata included, on a full-history checkout.
- V-3 holds: with only `make_copy` reverted, the command exits 4, and R-2 names the pack's `(mtime, ctime)`. The named loose objects are the same object IDs PR-20's V-3 named (plan §11.3); the scratch commits' content is the same.
- The counts equal plan §11's. The times are longer than plan §11's, because V-1, V-2 and V-3 shared 4 CPUs here.

## 5. In-flight decisions

| Decision | Why | Tested |
| :- | :- | :- |
| NONE | — | — |

The designated branch was restarted from `origin/main`. That follows plan §8 step 2 and the session's branch rule for a merged pull request; it is not a scope decision.

## 6. Publication

| Action | Result |
| :- | :- |
| `git push -u origin claude/hde-crd-0002-pr-plan-66tkpi` | new remote branch; `git ls-remote` reads `0245b77dec1d5cf95f7f98755c953a8e4c52e288` |
| Pull request | [#734](https://github.com/amthorn78/glow-hdengine-v2/pull/734), opened ready for review, base `main`, with the `.github/pull_request_template.md` headings filled under the `AGENTS.md` "PR descriptions" rules |
| This record | committed as the pull request's second commit, `docs/ephemeral/` only; it adds no CI lane (plan §9) |

## 7. PR_REMOTE_ACTION_LEDGER

| Item | State |
| :- | :- |
| Local checks | classifier, citations, V-1, V-2, V-3, pre-push check: all as §4 |
| Commits | `0245b77` (implementation); this record's commit |
| Pushes | 1 for `0245b77`; 1 for this record |
| Pull request | #734 created; no other pull request for this unit |
| Review reads | none (PR-35's) |
| Finding dispositions | none (PR-35's) |
| Hosted CI | not read by PR-30; the record-only push changes no lane (`docs/ephemeral/`), so the run on `0245b77` stays the candidate's run |
| Remote head | after this record's push, the record commit, whose parent is `0245b77`; PR-35 verifies it at entry |
| Mergeability | not evaluated by PR-30 |
| Remaining useful local action | none in PR-30 |
| Next evidence action | PR-35: read Codex code review and hosted CI on the current head |

## 8. Constraints and unresolved items

| Item | Owner |
| :- | :- |
| Codex code review findings on #734; disposition under addendum 2.11 rule 7 and addendum 2.14; no Codex security review (addendum 2.3) | PR-35 |
| V-4: hosted CI on the current head (product and release lanes and the changed-test step, ending `CI_APPLICABILITY_AND_EXACT_HEAD_OK`); mergeability; `MERGE_PENDING` | PR-35 |
| Re-running V-1 after any correction, and V-2 and V-3 when a correction touches `make_copy`, the guard or `main`'s violation output (plan §10) | PR-35 |
| The merge | Product Owner |
| V-5, PR-40 lineage review, with the owner test's collected count (141) | Whole-change Implementation Agent |
| C-1's QA Plan delta; V-6, check 13's verification | Kronos; Isis at QA-70 |
| PR35-C1 / FND-024: a red changed-test run with that signature is a known execution fault | As recorded (addendum 2.21) |
| O-1, O-A, D-1/LR6-O1, FND-028; plan OBS-3 | Product Owner, unchanged |

**Nonclaims.** No QA verdict, acceptance, Ops, deployment, PF09 or PF30 movement, drainage or closure; no canon edit; no release change; no HDE-CRD-0002 QA evidence produced or edited; no merge readiness claimed.

## 9. TypeSafe reading for the receiving session (PR-35, WU-REM-02)

Action sent (v8.2): "Resolve, as the dedicated review-resolution session for an already published pull request, its automated code review findings and current-head CI until the pull request is genuinely ready to merge: one remediation work unit changing three files of a Python developer tool (its throwaway-copy mechanism and read-only violation message, four regression test items, two documentation lines; about 164 added and 19 removed lines), whose implementation, local tests and two long command-level runs have already passed. The plan and the result record give the task list; any correction is retested locally (the owner test of about 141 tests, plus two command-level runs of up to about 25 minutes each only when the copy mechanism, the guard or the violation output changes); no live run against a provider occurs; the work is one unit, not many independent units; the Product Owner merges and an independent lineage review follows."

- **TypeSafe v8.2: Opus 5.5 at high.** Effort score 1.99 (confidence 0.87); rung probabilities low 0.00, medium 0.10, high 0.81, extra high 0.09, max 0.00, ultracode 0.00. Model probabilities Fable 5.1 0.00, Opus 5.5 0.99, Sonnet 5.5 0.01, Haiku 5.5 0.00 (confidence 0.99). Twenty-four cells, computed from the two answers: Fable 5.1 at low 0.000, Fable 5.1 at medium 0.000, Fable 5.1 at high 0.000, Fable 5.1 at extra high 0.000, Fable 5.1 at max 0.000, Fable 5.1 at ultracode 0.000, Opus 5.5 at low 0.000, Opus 5.5 at medium 0.099, Opus 5.5 at high 0.802, Opus 5.5 at extra high 0.089, Opus 5.5 at max 0.000, Opus 5.5 at ultracode 0.000, Sonnet 5.5 at low 0.000, Sonnet 5.5 at medium 0.001, Sonnet 5.5 at high 0.008, Sonnet 5.5 at extra high 0.001, Sonnet 5.5 at max 0.000, Sonnet 5.5 at ultracode 0.000, Haiku 5.5 at low 0.000, Haiku 5.5 at medium 0.000, Haiku 5.5 at high 0.000, Haiku 5.5 at extra high 0.000, Haiku 5.5 at max 0.000, Haiku 5.5 at ultracode 0.000. Sent 2026-10-25T13:50:29Z. Nathan picks the cell.
- **Flags:** none printed.
- **Detail (as printed):** v8.2 sent 2026-10-25T13:50:29Z; HTTP 200 in 0.46 s; 5523 input and 71 output tokens; jev-1.13.0. Rung by rule: high (nearest to the score, halves up); model by rule: Opus 5.5 (the most probable of the four options, a tie going to the higher-priced model).
- **Which request:** the installed TypeSafe scoring skill's request v8.2 and `score_v8.py`, run once with session kind `review` and label "PR-35 HDE-CRD-0002 WU-REM-02 review resolution on #734", before this record was saved.
- **Records:** the Notion row was not written. Nathan's pick for PR-35 is not stated. Nathan's pick for this PR-30 session is not stated; its reading is plan v1.0 §21.

**Surface advice:** run PR-35 in a new top-level Claude Code cloud session that Nathan creates on `amthorn78/glow-hdengine-v2`, dedicated to WU-REM-02's PR-35 phase. It needs GitHub access to read #734's reviews and checks, push corrections to its branch and subscribe to its activity, and Notion read access for the prompt.
- **Local reruns** need CI's full install on Python 3.12, `ruby`, `bash` and `curl`, under closed rails through `env -i`. V-1 takes about 2 to 3 minutes. V-2 and V-3, if a correction requires them, each need a full-history `--no-hardlinks` clone with nothing else touching it, and up to about 35 minutes when run side by side.
- **Not needed:** production, vendor, Railway and database access.

## 10. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | `GCFPE-USE-HDE-CRD-0002-PR-30-20261025-WU-REM-02-01` |
| change / specification | CRD HDE-CRD-0002 / Specification v1.1-approved with delta 01 |
| requirement / work unit | S20; QA110-F01; WU-REM-02 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08.672Z, read in full in this session) |
| role/stage | dedicated WU-REM-02 PR engineering session / PR-30 |
| capture time | 2026-10-25T13:52:00Z |
| execution identity | https://claude.ai/code/session_01SPJuyNDoQNA2MrC44oFKSs (no worker subagents) |
| result | PR_CANDIDATE_PUBLISHED; #734; next PR-35 |
| inherited usage | plan v1.0 (`GCFPE-USE-HDE-CRD-0002-PR-20-20261025-WU-REM-02-01`) and those it lists |
| repository persistence | PENDING / NON_GATING (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent on `main`); recorded here only |

## Canon relied on

As plan v1.0 "Canon relied on", unchanged on `main` at `a2c6d8f` (`docs/pfcanon/` last changed by `c491590`, PF10 v13.7.9). In addition:
- PR-30 — PR Implementation Proceed — 100926.1, read in full: "Mandatory PR-development execution contract", "Execute" 1 to 6, "Required result", "Direct native handoff rules";
- the `glow-hde-pr-development` skill 1.4.0: recovery, the two-phase lifecycle, the remote-action ledger;
- `AGENTS.md`: "Pre-push check", "PR descriptions", closed rails, pytest readiness.
