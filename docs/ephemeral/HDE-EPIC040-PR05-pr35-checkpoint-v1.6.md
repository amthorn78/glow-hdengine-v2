# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.6 (round 7)

Durable checkpoint saved with PR-35's seventh coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0–v1.5 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md` through `…-v1.5.md`), all unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 7: a seventh coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 rounds 1–5: as checkpoint v1.4 lists them. Round 6: `daa2110af8f1ff46b667fff399ed1c49bd10071a`, records `8f5921ca0367a9d1620e48865a6802f6af600584` (tree `5f367084e1d8fe53e9177b3877d0aee43be4175f`; the remote head after the round-6 push). Round 7: corrective `af3bc83d9fd515afa18a86f0dfd334ad98eb76dc` (tree `cfcc7fa61e91aab4ac699d922de7ab29a405fbae`), and records = the commit adding this file and ledger v1.7. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-6 push (2026-09-25, UTC)

- **Round-6 push.** `78b84f9..8f5921c` at 02:21:59Z; the branch and `refs/pull/492/head` read back with `git ls-remote` as `8f5921c`.
  - CR-12's thread was answered (`discussion_r4100409734`, naming `daa2110`) and resolved.
  - CR-06's thread stays open for its owner.
  - The PR description was updated.
- **CI on `8f5921c`.** `ci.yml` run `36085958849` (#3622), job `107917797052`, 02:22:05Z–02:31:21Z, conclusion `success`. It became stale as merge evidence at 02:26:27Z, when the round-7 finding arrived. It was not cancelled: the Actions API had refused cancellation with `403` (ledger L-29). It was not treated as a gate.
- **Codex on `8f5921c`.** Code Review `5312566233` (`COMMENTED`, 02:26:27Z, trigger "New commits") raised one P2 finding, on the comparator's CLI arguments. It added no comment to the open CR-06 thread, and nothing on the round-6 change. The Security Review is still the PR-open one on `96b54dd`.
- **Fallback check-in.** `trig_015bPQGWSWxynbr9Qrt5B7sZ` (03:02:00Z) remains scheduled.

## Round-7 finding and disposition

| ID | Source | Finding | Verification at `8f5921c` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-13 | Codex P2, thread `PRRT_kwDOP103ks6l11M9` (comment `4100427886`), `tools/config/generate_config_artifacts.py:344-345` | The CLI tests `--goldens` and `--report` by truthiness, so an empty value (an unset variable expanded by automation) reads as absent: `--goldens ""` compares the committed default collection and can report a false success, and `--report ""` exits 0 without writing the requested report | Against a synthetic complete-release root, `--goldens ""` gave exit 0, with the report naming the default goldens. `--report ""` gave exit 0 and wrote no report file | **Fixed in `af3bc83`** (IF-10) |

PR-35's review of the same class found two more cases in the same code, both fixed in `af3bc83`.
- `--compare-goldens ""` became `Path("")`, which is the current directory. Run from inside a synthetic root, it compared that directory: exit 0.
- Outside `--compare-goldens`, `--goldens ""` or `--report ""` skipped the "apply only to `--compare-goldens`" usage check and fell through to the default writer mode, `generate_config_artifacts(ROOT)`. With a spy in place of every writer mode, both calls returned 0 and reached `generate_config_artifacts`. No writer ran for real.

The readiness tool already refuses an empty `--user-id` or `--selection-file`: an empty path becomes the current directory, which cannot be read as a file, so both give `READINESS_SELECTION_INVALID`. It needed no change. All of this is an ordinary in-scope correction to PR05's own new code. None of it is material, and none needs a rescope.

**In-flight decision IF-10.** `_compare_goldens_main` receives the raw arguments and refuses an empty path at exit 5, with the token of the input it names: `REPORT_PATH_INVALID`, `GOLDENS_INVALID` or `CANDIDATE_ROOT_INVALID`.
- The check runs after the rails check and in the comparator's existing validation order: the report destination, then the goldens, then the candidate root.
- `None` still means "not given": the default goldens, or no report.
- The usage check tests `is not None`, so `--goldens` or `--report` outside `--compare-goldens`, empty or not, is argparse's exit 2 and never reaches a writer mode.

The existing tokens keep an unusable comparison input at plan §5.2's refusal exit 5, as a missing goldens file or an invalid candidate root already is. How an empty argument is treated is the decision.

## Corrective revision `af3bc83` (3 files, +44/−9)

| Path | Change |
| --- | --- |
| `tools/config/generate_config_artifacts.py` | `_compare_goldens_main(candidate_root: str, goldens: str \| None, report: str \| None)` refuses an empty path, then converts the arguments itself; `_main` passes the raw arguments and tests `--goldens`/`--report` with `is not None` (CR-13, IF-10) |
| `tests/config/test_config_artifacts.py` | 5 new items. `test_cli_empty_path_arguments_refuse` has three: `candidate_root`, `goldens` and `report`. Each runs from inside a valid synthetic root, so an empty root cannot pass by being the current directory. Each asserts the token, empty stdout and an unchanged root snapshot. `test_golden_arguments_without_compare_goldens_are_usage_errors_even_when_empty` has two: `--goldens` and `--report`. Each asserts exit 2 for an empty and a non-empty value, with every writer mode replaced by a spy that fails the test if reached. With this test file, all 5 fail at `8f5921c`; all pass at `af3bc83` |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | 2 new guard items in `test_invalid_selection_refuses_before_any_query`: `--user-id ""` and `--selection-file ""`. Both already pass at `8f5921c` |

Neither the CLI nor `tools/config/artifacts.py` is a release-roster member, and the readiness tool is unchanged. The comparator's positive report is therefore byte-identical to round 6's: 1,060 bytes, SHA-256 `8c0915df75756821492642b9e82549678346aa06b712e091b92aef465b54206f`. Untouched: the golden fixture, the readiness tool, `ci/**`, `tests/config/helpers.py`, every F01-enumerated file and all governed evidence.

## Local validation at `af3bc83`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `af3bc83`.

| Check | Result |
| --- | --- |
| The 5 new comparator items and 2 readiness guards | pass at `af3bc83`; with these test files, the 5 fail at `8f5921c` (throwaway worktree: 5 failed, 161 passed) and the 2 guards pass there |
| Owner modules | 166 passed |
| Plan §10.2 focused and guard suites | 1,168 passed |
| Classifier dry-run (`--base 25b2c87… --head af3bc83… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 24 paths, 90 changed-test targets (the same 90 as rounds 1–6) |
| Changed-test isolation (detached worktree) | 2,464 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–6 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,048 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `af3bc83` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions |
| Comparator CLI | `--goldens ""` → exit 5 `GOLDENS_INVALID`; `--report ""` → exit 5 `REPORT_PATH_INVALID`; `--compare-goldens ""` from inside a synthetic root → exit 5 `CANDIDATE_ROOT_INVALID`; each with stdout empty. `--goldens ""` or `--report ""` without `--compare-goldens` → exit 2, no writer mode reached (spies). A named `--report` still writes the canonical report, equal to stdout's. Positive report byte-identical to round 6's (1,060 bytes, SHA-256 `8c0915df75756821492642b9e82549678346aa06b712e091b92aef465b54206f`). Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-7 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-13 thread with the pushed fix, and resolve it. The CR-06 thread stays open for its owner.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. Once it completes without new findings, one bare `@codex security review` request, as checkpoint v1.0 planned.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
