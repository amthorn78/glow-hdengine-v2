# HDE-EPIC040-PR04 — PR_REMOTE_ACTION_LEDGER v1.0

Compact record of actual local checks, commits, pushes, PR reuse, review reads, CI state and remaining actions for the one authorized work vehicle. Intent never proves a remote effect; every remote fact below was read back after the action.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR04 |
| Session | `PR04-HDE-EPIC040-1` |
| Phase | PR-30 → same-session PR-35 |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/peaceful-gauss-jhyezn` |
| Pull request | #467 (reused) |
| Base | `origin/main` merge-base `3b8084d09e974f15c2b71112e5a596af01b1a371` |

## Entries (UTC, 2026-09-22)

| # | Kind | Actual event | Evidence |
| --- | --- | --- | --- |
| L-01 | recovery | Existing workspace, branch and open PR #467 for this work unit verified; prior head `02a303b4` (plan v1.2 commit) | `git status`, `git log` |
| L-02 | local checks | C1–C3 implemented; §10.2 focused suites 517 passed / 3 skipped; `testpaths` roster 1916 passed / 3 skipped (two runs); read-only evidence checks all exit 0; canonical gate `--check-only` 0; five pre-existing failures unchanged. After an aborted whole-tree exploration run mutated tracked artifacts, the tree was restored (`git checkout`) and Index/Mirror recovered through the owner chain (updater → pipeline canonical run → updater → pipeline fixed point, gate wrapper 3); every read-only check 0 and the roster 1916 passed / 3 skipped were re-run on the recovered tree | result record §8 |
| L-03 | owner evidence | manifest re-cut (one row), canonical gate write (once), sanity pipeline canonical run (NOT_ADMITTED transition, fixed point verified), updater run ×2 | result record §6–§7 |
| L-04 | local gate rehearsal | rails runner exit 3 with `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; attestation rehearsal in fresh venv on a committed scratch snapshot → receipt `release_not_admitted` (stage `closure_write_and_check`, rc 3) | result record §8 |
| L-05 | commit | Implementation commit `881cc2df6ca79ab8564bba9d9e20013807ecf077` (tree `475ba9b440fbcac6336e49cca2739097991dea88`); records commit = the commit adding the result record, this ledger and the checkpoint (its SHA is recorded verbatim in the PR #467 body and in L-13 at PR-35 entry) | `git log` |
| L-06 | push | `git push -u origin claude/peaceful-gauss-jhyezn` (single push of both commits); remote head read back with `git ls-remote`, equal to the records commit, recorded verbatim in the PR #467 body and in L-13 at PR-35 entry | `git ls-remote`, PR body |
| L-07 | PR reuse | PR #467 title/body updated to the candidate; no new PR; no merge, auto-merge or `[skip ci]` | GitHub read-back |
| L-08 | reviews | Codex code/security review: not yet read (PR-35 entry action) | — |
| L-09 | CI | Hosted CI for the pushed head: not yet observed (PR-35 entry action); expected accepted outcomes `RAILS_LANE:RELEASE_NOT_ADMITTED`, `RELEASE_LANE:RELEASE_NOT_ADMITTED` | — |
| L-10 | mergeability | not yet read | — |
| L-11 | remaining useful local action | none before review/CI evidence arrives | — |
| L-12 | next evidence action | PR-35: read Codex reviews and inline threads, read the exact-head CI run (all seven lanes), resolve findings locally, push one coherent corrective revision if needed (re-cut the manifest if `adapter/http_reader.py` changes) | — |

## PR-35 entries (UTC, 2026-09-22) — successor session

Phase PR-35 is executed by a Product Owner-directed successor session after the PR-30 session `PR04-HDE-EPIC040-1` stopped for context limits. Same work unit, work vehicle, branch, PR, artifacts and original Proceed; no new Proceed, PR or approval object. The interrupted session released its PR subscription and check-in; this session subscribed to PR #467 itself.

| # | Kind | Actual event | Evidence |
| --- | --- | --- | --- |
| L-13 | recovery | Remote head at PR-30 publication `e7c5323a6db0eb651db3bf81c90c40efd95d3f70`; branch head at PR-35 entry `73b9812ab09124333a313b2cbf1c638412d17468` (entry-checkpoint commit, docs-only) read back and equal to local `HEAD`; PR #467 open, not draft, not merged, base `main` `3b8084d09e974f15c2b71112e5a596af01b1a371`, head `73b9812a`, `mergeable_state` `unstable` | `git ls-remote`, `git rev-parse`, GitHub PR read |
| L-14 | reviews | Codex **Code Review completed on `73b9812`** (the current head), two unresolved inline threads: **P1** `adapter/http_reader.py:407-408` "Bound the request stream before buffering it"; **P2** `engine/compat/compute.py:329` "Ship the admission roster with installed packages". Codex **Security Review completed only on `e927ed0`** (PR-open head) — a current-head security review is owed. No other reviewer; Claude Code Review was not installed, triggered or configured | GitHub reviews / review-threads / comments read |
| L-15 | CI | Run 35741951421 (`ci.yml` #3593, head `e7c5323a`) failed at "Run affected behavioral tests in isolation" — 4 failed / 2392 passed; all seven lanes skipped in consequence. Treated as the diagnosis source, not a gate on a revision already known to need corrections; no re-run was requested on that stale revision | entry checkpoint, Actions run/job logs |
| L-16 | local repro | All four failures reproduced exactly in a detached worktree under closed rails before any edit (C-1 422, C-2 503, C-3/C-4 `ValueError`) | §8.1 |
| L-17 | finding disposition | P1 accepted and fixed (P-21) with a measured before/after (5,000,102 → 32,769 bytes consumed) and a new regression test. P2 verified accurate but **not fixed here**: pre-existing, outside this PR's diff, unreachable in the CI (`pip install -e .`) and deployment (repo-rooted `gunicorn`) shapes, and fixing it would change the distribution surface beyond the bounded work unit — recorded as O-12 and answered on its thread | §4 P-21, §10 O-12 |
| L-18 | owner evidence | `adapter/http_reader.py` changed, so `cut_release_manifest.py --version 1.0.0 --built-at-utc 2025-12-26T00:00:00Z` re-cut one row (`release_id` `5fd293bf…` → `a6db0106…`); the canonical JSON gate was then written once by its owner and the Index/Mirror refreshed once by the sole updater. Nothing governed hand-edited | §6 PR-35 re-cut, §7 |
| L-19 | local checks | CI changed-tests step reproduced exactly at the corrective head: **2397 passed**, `git diff --exit-code` 0, tree clean. Roster 1916 passed / 3 skipped. All seven lane equivalents green, including the accepted `RAILS_LANE:RELEASE_NOT_ADMITTED` and `RELEASE_LANE:RELEASE_NOT_ADMITTED` outcomes. Five pre-existing failures unchanged | §8.1 |
| L-20 | commit | Corrective commit `7b2bc5c95aa558961069a0a904ad7e4869a8469f` (18 files: source, four test modules, re-cut manifest, owner-written gate outputs, Index/Mirror); PR-35 records commit adds the result-record update, these entries and the PR-35 checkpoint | `git log` |
| L-21 | push | One push of both commits with `git push -u origin claude/peaceful-gauss-jhyezn`; remote head read back with `git ls-remote` — recorded in L-23 | `git ls-remote` |
| L-22 | PR reuse | PR #467 reused; body Publication section updated to the corrective head. No new PR, no merge, no auto-merge, no `[skip ci]` | GitHub read-back |
| L-23 | remote head after corrective push | `ed432acd50bcaf3dc39b089b9ddc83430f294923`, read back with `git ls-remote` and equal to local `HEAD`. One follow-up docs-only commit completes the checkpoint with that verbatim SHA and becomes the final branch head; that head is read back after its push and recorded in the PR #467 body. It supersedes the CI run on `ed432ac` via `cancel-in-progress`, so exact-head CI evidence lands on the final head | `git ls-remote`, PR head |
| L-24 | next evidence action | Verify exact-head CI (all seven lanes) and current-head Codex code **and security** review; request `@codex security review` once if it does not re-run for new commits; return `MERGE_PENDING` only when every predicate holds. Nathan merges manually | — |
