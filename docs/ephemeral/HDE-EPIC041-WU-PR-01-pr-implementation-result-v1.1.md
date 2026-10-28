---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-EPIC041-WU-PR-01-PR-IMPLEMENTATION-RESULT
artifact_version: "1.1"
phase: PR-35
record_kind: CHECKPOINT (after the coherent corrective push; before the wait for current-head CI and review)
result: none yet (nonterminal checkpoint; the PR-35 result is recorded by the next version)
predecessor: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-result-v1.0.md (v1.0, PR-30, PR_CANDIDATE_PUBLISHED; 15,261 bytes; blob 24e5949ba2be; sha256 9acc8c3eef5028da5abff86491d46576d30e8399755ca9876c3f129057903d00; preserved unchanged)
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC041
WORK_UNIT_ID: WU-PR-01
PR_INSTRUCTION_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-instruction-v1.0.md (v1.0; blob 455874034a8a)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-WU-PR-01-pr-implementation-plan-v1.0.md (v1.0; blob f467d6a61756)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-v1.1.md (v1.1)
PLAN_REVIEW_ID: docs/ephemeral/HDE-EPIC041-implementation-plan-review-v1.1.md (IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-EPIC041-epic-specification-v1.1.md (v1.1)
REMEDIATION_REVIEW_ID: none
RESCOPE_REVIEW_ID: none
proceed: the Product Owner's invocation of PR-30 — PR Implementation Proceed — 102726.1 for exactly PR_IMPLEMENTATION_PLAN v1.0, 2026-10-28; carried over; no new Proceed requested or created
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + IA-30 review v1.1
effective_baseline: "approved base + applicable PF10 overlays (NONE for this unit's scope)"
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.9.1.md (HDE Build Notes, the one PF10 file on main at e121e354; 48,634 bytes; sha256 300e19679173c7dbf3c077be8edc12f90e9890b89d590426e5ca2b0d55870e68; read in full, ends "<eof>"; recorded as provenance)
pf10_addenda_applicable: "the addendum \"Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close\" (numbered 2.2 in the version read), for its R-1 and R-2 rules on what code and tests may read; this unit conforms (\"Canon relied on\"). The other addendum (S19 routed findings) does not apply"
pf10_addendum_created: none (PR-35 is not an addendum producer)
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 102726.1 (https://app.notion.com/p/4064590a05eb8108a9f5cececa4b3149; page state 2026-10-27T13:13:39.046Z, read in full)
primary_skill: glow-hde-pr-development 1.5.0
session: https://claude.ai/code/session_01Q789tzt85iauNogD8xS2zg (the dedicated WU-PR-01 PR-35 session; top-level; entered from the PR-30 handoff Nathan pasted)
pull_request: amthorn78/glow-hdengine-v2#791 (https://github.com/amthorn78/glow-hdengine-v2/pull/791), open, not draft
branch: claude/wu-pr-01-implementation-plan-js521f (the PR head branch; the same branch PR-30 published)
base_at_entry: 455d39f10b3dce8d1de4e542355d887180360a4f; base_now: origin/main e121e354060afe3007a84d82b61b073df1da666b (#792)
pr_head_at_entry: c6e50a98e6820da38915c1dd3b0680cbebbc5da0 (git ls-remote at entry, about 12:24Z)
tested_source: b399cfd0b6b73473a9887703f81752d0c48b6b7c (the merge of main into c6e50a98, `e6797eab`, plus the test correction ID-35-1); this record's own commit adds only this file under docs/ephemeral/
implementation_commit: 2f7657c60f31ca95f294b0a9d83a2773b91aa3eb (unchanged: engine/charts/pure.py and adapter/chart_orchestration.py keep their blobs 49ccfb58 and f8163fad); corrective commits: e6797eab (merge of main), b399cfd0 (one test file)
canon_conflict_register: CCR-1 to CCR-4 carried unchanged from plan v1.0 §18; CCR-3 not triggered; no new entry
created_at: 2026-10-28 (UTC)
---

# HDE-EPIC041 WU-PR-01 — PR Implementation Result v1.1 (PR-35 checkpoint)

## 1. State

**Checkpoint, not a result.** PR-35 has merged `main` into #791 after [amthorn78/glow-hdengine-v2#792](https://github.com/amthorn78/glow-hdengine-v2/pull/792) (the OBS-3 fix) merged. It has also corrected one defect in this PR's own new test (§5). Local checks on the corrected head pass (§4). This record is pushed with those two commits in one push. The next version records the hosted CI and Codex review on the pushed head, and the PR-35 result.

| Item | State at this checkpoint |
| :- | :- |
| Codex code review | completed on `c6e50a98`, `has_any_findings: false`; 0 formal reviews; 0 review threads (§3) |
| Codex security review | not run (`status: null`); none is required for this change (§3) |
| Hosted CI on `c6e50a98` | `test` failure, only in `tests/qa/test_generate_epic_close_pack.py` (OBS-3, §3) |
| OBS-3 | fixed on `main` by #792 (`e121e354`); merged into this branch (§4) |
| New defect found locally | the keys-only log test failed whenever the clock read `12:34`; corrected (§5) |
| Local checks on the corrected head | pass (§4) |
| Next evidence | hosted `test` and the Codex review on the pushed head, through the active subscription |

## 2. Entry recovery and continuity

| Checked | Found |
| :- | :- |
| PR | #791 open, not draft, base `main`, head `c6e50a98`, 2 commits, 8 files, +788; `mergeable_state: unstable` (red check) |
| Remote branch head | `c6e50a98e6820da38915c1dd3b0680cbebbc5da0` (`git ls-remote`): the v1.0 record's commit, on top of the implementation commit `2f7657c6` |
| Worktree | a fresh worktree of the PR branch at `c6e50a98`, clean; no other checkout held this work unit |
| Records | instruction v1.0, plan v1.0 and its companion diff, result v1.0; no PR-35 record existed |
| `main` | `e121e354` (#792, merged 2026-10-28T12:23:16Z by amthorn78); it also replaces HDE Build Notes v13.9 with v13.9.1 |
| Subscription | `subscribe_pr_activity` on #791 confirmed; `subscription.created` received |
| Branch for pushes | the PR head branch, which the nine-field continuity list fixes; the session's harness-designated branch was not used, so no second branch or PR exists |
| Nine continuity fields | one value each, shared with PR-30: WU-PR-01; the original Proceed; the PR branch worktree; `claude/wu-pr-01-implementation-plan-js521f`; #791; instruction v1.0; plan v1.0; `glow-hde-pr-development` 1.5.0; the `docs/ephemeral/` lineage above |

## 3. Reviews and hosted CI read at entry

* **Codex.** Summary comment 6461664951: `code_review {commit_sha: c6e50a98…, has_any_findings: false, has_unresolved_findings: false, status: completed}` at 2026-10-28T05:46:15Z; `security_review` all `null`. No formal review and no review thread exist.
* **Security review.** Neither `AGENTS.md` nor plan v1.0 §14 requires one for this change (no route, credential, flag, network or environment gate). None was requested.
* **Hosted CI on `c6e50a98`.** Check run 122655520972 (run 40639811368), `test`, failure, 05:46:42Z to 05:54:44Z. The changed-tests step reported `151 failed, 4424 passed, 2 skipped`. All 151 failures are in `tests/qa/test_generate_epic_close_pack.py`, by full-log count (`FileNotFoundError` on `docs/pfcanon/PF30.1-…-v0.9.1.md` or on archived `docs/ephemeral/` records). Lanes 09 to 15 were skipped after it. This is OBS-3. PR-30's local run of the same 4,577 tests had 150 failures, all in the same file. Which test was the 151st hosted failure, and where the 2 hosted skips were, was not determined; after the merge of `main` the file is no longer selected (§4).

## 4. OBS-3 handling and local checks

**OBS-3.** Plan v1.0 §19: "when a fix exists …, port the same change into this PR and push". The fix exists on `main` as #792. As the Product Owner directed, PR-35 merged `main` into the PR branch with a merge commit, `e6797eab` (parents `c6e50a98`, `e121e354`), with no rebase and no force-push. The merge had no conflict (`ci/checks/classify_ci_changes.py` auto-merged). After it, the PR's diff from `main` is the same 8 files. No PR comment on OBS-3 was posted, because §19 asks for one only while no fix exists.

**Configuration.** CPython 3.12.3 venv with CI's install (`setuptools>=68`, `wheel`, `-r requirements.txt -r requirements-dev.txt -e .`; pytest 8.4.2); `env -i` with `HOME`, `PATH`, `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `PYTHONPATH=<checkout>`. The container's credentials were kept out of every child. **Actor:** this PR-35 session. **Limitations:** local runs; not hosted CI, not QA, not governed evidence.

| # (plan §11) | Run | On `e6797eab` (merge only) | On `b399cfd0` (merge + §5 correction) |
| :- | :- | :- | :- |
| 1 | the four new test files | 46 passed (12:27:51Z) | 46 passed (12:38:00Z) |
| 2 | `classify_ci_changes.py --base e121e354 --head <head> --event-name pull_request` | exit 0; `reason=selected_lanes;paths=8`; all seven lanes; 169 targets, including the four new files and not the close-pack test | identical; the same 169 targets |
| 3 | the 169 targets, as CI's isolated changed-tests step runs them, in a scratch clone | 4 failed, 3,664 passed (12:28:39Z to 12:35:26Z); clean tree. The 4 are explained under the table | 3,668 passed, 0 failed (12:38:15Z to 12:46:01Z), in a full-history clone; `git diff` clean; status empty |
| 4 | `prepush_check.py --base origin/main --head HEAD` with the 8 paths, `lanes membership build-notes` | PASS; not-member ×8; HDE Build Notes `docs/pfcanon/PF10-HDE-Build-Notes-v13.9.1.md` sha256 `300e1967…`; "repository unchanged" | identical |
| 5 | admission; `release_id_recompute.py --check-manifest-only` | `release_id` 77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e; exit 0 | identical |
| 6 | `prepush_check.py --base origin/main --head HEAD replay` | not run on `e6797eab` | `status=PASS` (12:46:34Z to 13:09:55Z): steps 01 to 16 SUCCESS (01, 04, 05 substituted); step 08 3,668 passed; product 77 passed; compat 119 passed, 3 skipped, 2 xfailed; db 269 passed; rails 160 passed; evidence 134 passed; qa 488 passed; release 79 passed, attestation built and verified; step 16 `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; the copy was clean afterwards. The tool exited 4 with one read-only violation: `.git/canon_relied_on_hook.json` (mtime, ctime) changed. That file is the state of the repository's own Claude Code hook (`.claude/hooks/check_canon_relied_on.py`), which this session's tool calls ran during the replay; it is not the candidate (OBS-5) |

The four failures on `e6797eab`:

* `tests/loader/test_loader_logs_keys_only.py::test_loader_emits_keys_only_log` failed: today's loader test asserts that `"12:34"` is absent from the raw line, and the run reached it at 12:34:27Z, so the line's `ts` held `12:34`. The same defect was in this PR's own `tests/adapter/test_chart_orchestration.py`, which passed in these runs only because it did not run during a `12:34` minute. That one is corrected (§5). The loader test is outside this unit (instruction §4: `tests/loader/*` must not change), so it is OBS-4 (§7).
* Three in `tests/tools/test_prepush_check.py` (`test_reports_on_a_clone_of_the_repository_are_read_only`, `test_lanes_equals_the_classifier_for_refs_and_for_given_paths`, `test_lanes_and_membership_run_the_classifier_only_in_a_throwaway_copy`) failed with `git clone into the temporary directory failed: error: Could not read e70fecb3…`. The container's repository was a shallow clone (`.git/shallow`, 2 roots), and the scratch clone copied it without the older objects. CI checks out with `fetch-depth: 0`. After `git fetch --unshallow`, these tests ran in a full-history clone (column 4).

## 5. In-flight decisions

| ID | What changed | Why it was necessary | What was tested |
| :- | :- | :- | :- |
| ID-35-1 | `tests/adapter/test_chart_orchestration.py::test_log_line_is_keys_only` (commit `b399cfd0`): `ts` is asserted to match `^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$` and the forbidden-substring check runs on the raw line with the `ts` value removed. The forbidden list and every other assertion are unchanged | The test asserted `"12:34"` (the birth time) absent from the whole raw line, including `ts`, the UTC clock. It failed on a correct implementation whenever the clock read `12:34` as HH:MM or MM:SS (about 84 seconds a day). The hosted runner's clock is a real input, so the hosted `test` job would go red at those times. AC-04 and green exact-head CI need the test to be correct at every time. It is this PR's own new file (instruction §4, "may add"; §8, "an ordinary in-scope defect is repaired in place"), and the plan's intent, "the log line carries no birth input" (plan §14), is kept | A scratch harness outside the repository pinned `adapter.chart_orchestration`'s clock. The original test failed at 2026-10-28T12:34:56Z and at 05:12:34Z, and the corrected test passed at both and at the live clock (6 cases: 2 failed as expected, 4 passed). Then plan §11 items 1 to 6 on `b399cfd0` (§4) |
| ID-35-2 | The pushes go to the PR head branch `claude/wu-pr-01-implementation-plan-js521f`, not to this session's harness-designated branch | The nine-field continuity list fixes one branch and one PR per plan cycle. The Product Owner's handoff directs the merge of `main` "into #791" and a push | remote head read back after the push (§6) |
| ID-35-3 | No Codex security review was requested | not required for this change (§3) | not applicable |

## 6. PR_REMOTE_ACTION_LEDGER (continues v1.0 §7)

| # | Time (UTC) | Action | Outcome |
| -: | :- | :- | :- |
| 4 | ~12:24 | Read #791 and #792 (details, reviews, threads, comments, check runs); fetched `origin` | #791 head `c6e50a98`, red; #792 merged at 12:23:16Z |
| 5 | ~12:25 | `subscribe_pr_activity` on #791 | confirmed; `subscription.created` received 12:25:06Z |
| 6 | ~12:26 | Read the full log of run 40639811368 | 151 failures, all in the OBS-3 file |
| 7 | ~12:27 | Local merge of `origin/main` (`e6797eab`) | no conflict; the diff from `main` is the same 8 files |
| 8 | 12:27 to 12:35 | Plan §11 items 1 to 5 on `e6797eab` | §4 |
| 9 | 12:28:53 | #792 validation: close pack `--check` on `main` | §8 |
| 10 | ~12:36 | `git fetch --unshallow origin` (local git metadata only) | full history; no repository content changed |
| 11 | ~12:37 | Correction commit `b399cfd0` (ID-35-1) | local |
| 12 | 12:38 to 13:09:55 | Plan §11 items 1 to 6 on `b399cfd0` | §4 |
| 12a | 12:40:36 | Read the `main` push run 40687380634 on `e121e354` | success on every step: the base is green |
| 13 | next | One push of `e6797eab`, `b399cfd0` and this record; read back the remote head; then hosted `test` and Codex on the pushed head, through the subscription | — |

Stale runs: none active on #791 (the one run, on `c6e50a98`, completed before entry). Remaining useful local action before the push: none.

## 7. Observations for owners (nothing outside this unit changed)

* **OBS-4.** `tests/loader/test_loader_logs_keys_only.py::test_loader_emits_keys_only_log`, an existing test of today's loader, has the same clock defect as ID-35-1. It fails whenever it runs while the UTC clock reads `12:34` as HH:MM or MM:SS, about 84 seconds a day, on any pull request that selects it, as full validation does. It is a real-input defect but outside this unit: instruction §4 forbids changing `tests/loader/*`. WU-PR-02 migrates or removes C-2 and C-3 with the loader (Plan v1.1 §6). Owner: the whole-change IA through PR-40, for WU-PR-02's instruction; until then, Nathan / Product Owner.
* **OBS-5.** Two local-environment effects, recorded for later sessions' surface advice. (a) This container's repository was a shallow clone, and a plain local clone of it fails three `tests/tools/test_prepush_check.py` tests: run `git fetch --unshallow` before local runs. (b) The repository's `.claude/hooks/check_canon_relied_on.py` writes `.git/canon_relied_on_hook.json` after this session's tool calls, so any tool call during `prepush_check.py replay` makes the replay report a read-only violation; the replay's own steps are unaffected.

## 8. #792 (watched and validated under the Product Owner's direction of 2026-10-28)

| Check | Result |
| :- | :- |
| State | merged 2026-10-28T12:23:16Z by amthorn78, as squash `e121e354` on `main`; head `31d6ff68` |
| Codex | code review completed on `31d6ff68`, `has_any_findings: false`; security review not run; 0 review threads |
| PR checks on `31d6ff68` | `validate-closeout-candidate` success (12:14:37Z to 12:14:56Z); `test` success (12:14:37Z to 12:30:36Z), observed after the merge |
| `main` push run on `e121e354` | run 40687380634: `test` success, every step, 12:23:19Z to 12:40:36Z (changed-tests step 12:23:36Z to 12:30:06Z; all seven lanes; final step success). `main` is green |
| Close pack on `main` | `tools/qa/generate_epic_close_pack.py --source audit/HDE-CRD-0002_close_candidate_source.json --check` in a clean clone at `e121e354`, closed rails: `EPIC_CLOSE_PACK_CHECK_OK:audit/HDE-CRD-0002_close_report.md:audit/HDE-CRD-0002_MANIFEST.json`, exit 0, 12:28:53Z to 12:28:59Z; tree clean |
| Review corrections on #792 by this session | none (none needed; it merged before this session acted) |

## 9. Unresolved items and owners

| Item | Owner |
| :- | :- |
| Hosted `test` and Codex on the pushed head | this PR-35 session, through the subscription |
| OBS-4 | the IA through PR-40 (WU-PR-02); Nathan / Product Owner meanwhile |
| OBS-1, OBS-2 (plan v1.0 §16) | the IA through PR-40 |
| Carried items (plan v1.0 §17) | unchanged |

## Canon relied on

Resolved from `docs/pfcanon/` on `main` at `e121e354`; this branch changes nothing there.

| Title (version read) | Sections read in full | Governs here |
| :- | :- | :- |
| HDE Build Notes (v13.9.1) | whole file, 48,634 bytes, to `<eof>`: precedence rules 1 to 9, cross-references, the index and both addenda | The addendum "Planning documents and PF-Canon versions are never inputs; the close-pack writer runs only at close": R-1 and R-2 checked against this PR's code and tests, which read no `docs/ephemeral/` or `docs/pfcanon/` path and pin no PF file name (diff search, no match); R-3 is why the close-pack test is no longer selected (169 targets). The S19 addendum does not apply (no vendor, route, compat or evidence-tool change) |
| Change Process Guide (v2.5.5) | "PR review finding disposition (every pull request; real inputs only)" | Real-input rule for ID-35-1 (the runner's clock is a real input); no review finding to disposition yet |
| Plan Templates (v2.0.6) | "Review guardrails" (finding disposition on real inputs, P1 findings, repeated finding class); "CI lane classification and automated budget-control discipline" | One coherent push; no CI on a revision known to need correction; why the close-pack test is close-stage only |
| As plan v1.0 "Canon relied on" | HDE Build Checklist — Separation (HDE-SEPA006); HDE Architecture §1.1; HDE Mechanics Guide §1.1; HDE Governance §9.1.1 to §9.1.4, §9.2, §9.7.7, §4.3.9; Change Process Guide §0.2 | Unchanged by this checkpoint; no `docs/pfcanon/` change touches them except HDE Build Notes |

Prompt and skill: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 102726.1, read in full; `glow-hde-pr-development` 1.5.0. Repository rules: `AGENTS.md` (code review scope, pre-push check, PR descriptions).

## Nonclaims

This checkpoint is not a PR-35 result, merge readiness, a merge, hosted CI, a review verdict, QA, Ops, acceptance, PF09 movement, a canon change, a PF10 addendum or closure. Local results are not governed evidence. No agent merges #791; Nathan does.
