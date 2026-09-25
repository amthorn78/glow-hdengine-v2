# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.10 (round 10)

This durable checkpoint is saved with PR-35's tenth coherent corrective push.
- It continues checkpoints v1.0–v1.9 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md` through `…-v1.9.md`), all unchanged as issued.
- **Result v1.1 and handoff v1.0 no longer stand.** Codex CR-17 arrived on result v1.1's own records head, `0e3a9c1`. Both stay unchanged as issued.
- This push issues result v1.2 (`MERGE_PENDING`), ledger v1.11 and the conditional PR-40 handoff v1.1. The pushed head's CI and Codex review are verified after the push.
- It changes no authority or scope. The PR-30 result stands unchanged: `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 10: a tenth coherent corrective revision, committed and validated locally, and pushed with this checkpoint, result v1.2, ledger v1.11 and handoff v1.1. Awaiting exact-head CI and the Codex review of the pushed head |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, not merged; base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a`, unchanged since PR-30 |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 rounds 1–9: as checkpoint v1.9 lists them. Final records of result v1.1: `0e3a9c1818b83c4112614a200d2fae397e5ef212` (tree `683f80041e6dcc5f35b885234becbe0c48e3f3e2`; the remote head before this push). Round 10: corrective `d47a7cbed7ef70b2a0ce342c96ed4ed8521e42e4` (tree `73a12a3c13fcabf4230491b05270022181727c63`); records: the commit adding this file, result v1.2, ledger v1.11 and handoff v1.1. A commit cannot embed its own SHA, so the records commit and the remote head read back after this push are recorded in the PR #492 body and the PR-35 return |

## What happened after the push of result v1.1 (2026-09-25, UTC)

- **Push.** `dcb2716..0e3a9c1` at 04:00:48Z. The branch read back as `0e3a9c1` at 04:00:50Z, and `refs/pull/492/head` at 04:01Z.
- **PR description.** It was updated with the final records and read back. The stored body is identical to the posted text except for the final newline, which it lacks: 56,785 characters, SHA-256 `95d61d2e22325b245ae7f87859f8c661b7567008c336417eadc3482823367ac2`. The PR showed head `0e3a9c1`, 21 commits and 34 changed files.
- **Fallback check-in.** `trig_01HHijetSRcLLoWNYKQ4PjPM` fired at 04:04:27Z. Its round-8 instructions had all been carried out already, so nothing was owed. The next check-in is `trig_01QSPEPU5TXtjqKXr8QAKZaW`, at 05:06:00Z.
- **Codex's automatic review of `0e3a9c1`.** Code Review `5313189218` (`COMMENTED`, 04:06:27Z, trigger "New commits") raised the round-10 finding below. It added no comment to the CR-06 thread. Result v1.1 had made its `MERGE_PENDING` conditional on a clean review of that head (its §9), so from here that result no longer stands.
- **CI on `0e3a9c1`.** Run `36092693372` (#3626), job `107938250001`, ran 04:00:58Z–04:12:51Z and concluded `success`. It is stale as merge evidence from 04:06:27Z, when CR-17 arrived. It was not cancelled, because the Actions API refuses cancellation with `403` (ledger L-29), and it was not treated as a gate.

## Round-10 finding and disposition

| ID | Source | Finding | Verification at `0e3a9c1` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-17 | Codex P1, thread `PRRT_kwDOP103ks6l3IMg` (comment `4100949533`), `tools/config/artifacts.py:620-622` | The golden runners' router stub ignores the category and band and answers every perspective other than `a_to_b` with the reverse key. An `evaluate_pair` that routes with an invalid or wrong argument can therefore still match, although the canonical `route_keys` answers the missing key and production evaluation refuses | `compute._route` was regressed seven ways, and each left all eight cases matching (`ok: true`): the reverse perspective as `typo` and as `shared`, a lower-cased band, a category the candidate lacks, an unexpected keyword, another valid category (`heat`) and another valid band (`Glow`). For the same arguments, `route_keys` answers the missing key (the missing personal key for `shared`), and it raises `TypeError` for the keyword | **Fixed in `d47a7cb`** (IF-14) |

**Class review.** PR-35 checked every other stand-in in the comparator against the canonical seam it replaces:
- The bundle-provider lambda and the G007 cache spy are no more permissive than the real seams.
- The Reader bytes are built from the enriched envelope through the canonical emitter that plan §5.1 names. A harmony band outside the Reader's bands would already mismatch G008's expected band and Reader hash.
- The router stub was the only lenient stand-in.

**A local artifact from the reproduction, removed.** The scratch reproduction's first run called `route_keys` from the repository's working directory. That loaded the narrative pack, which mounted an untracked `narratives/4cc79e05…/` there.
- It was removed at once. The tracked `narratives/64e17c9c…/` was untouched, and `git status` was clean before any commit.
- Later runs used the scratchpad as their working directory.

CR-17 is an ordinary in-scope correction to PR05's own new code. It is not material and needs no rescope.

**In-flight decision IF-14.** The golden router stub is held to the canonical router's contract.
- **Signature and refusals.** The stub has `route_keys`'s signature and answers the missing key wherever `route_keys` does. That covers a category outside the candidate's categories, a band outside the narrative bands, a perspective outside the narrative perspectives, and the personal key of the `shared` perspective. An unexpected keyword is a `TypeError`. `evaluate_pair` then refuses as it would in production, and the case records an `execution` mismatch.
- **Routing check.** For every G005 and G008 evaluation, the recorded calls must equal, as a set, the tuples the evaluation's own result rows require in both normalized directions. Any other routing is that case's `router_calls` mismatch, and repeated identical calls are harmless.
- **What is unchanged.** The fixture, the report keys and the tokens.

## Corrective revision `d47a7cb` (2 files, +120/−7)

| Path | Change |
| --- | --- |
| `tools/config/artifacts.py` | `_golden_router(constants, bundle, calls)` has `route_keys`'s signature, answers the missing key where `route_keys` does, and records every call. `_golden_check_routing(calls, result)` holds each evaluation's calls to its result rows in both directions. The G005 and G008 runners check routing after every `evaluate_pair` call (CR-17, IF-14). The G007 runner passes the new stub through its recording seams, unchanged |
| `tests/config/test_config_artifacts.py` | 9 new items. `test_a_misrouting_evaluate_pair_is_never_a_match` ×7 (`reverse_perspective_typo`, `reverse_perspective_shared`, `band_not_a_narrative_band`, `category_not_the_candidates`, `unexpected_keyword`, `another_valid_category`, `another_valid_band`) expects exactly its mismatch paths for G005 and G008. `test_the_router_stub_answers_as_the_canonical_router_does` checks the stub's signature and answers. `test_repeated_identical_routing_is_not_a_mismatch` is a guard. With this test file, 8 fail at `0e3a9c1` (8 failed, 1 passed) and all 9 pass at `d47a7cb` |

`tools/config/artifacts.py` is not a release-roster member, so the comparator's positive report is byte-identical to round 9's: 1,060 bytes, SHA-256 `e2b3ec663e848259cb3a5191c64c5e3353f057c52c7c4958317ec731c9e61390`.

Untouched: the readiness tool, the comparator's CLI, the golden fixture, `ci/**`, `tests/config/helpers.py`, every F01-enumerated file and all governed evidence.

## Local validation at `d47a7cb`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `d47a7cb`.

| Check | Result |
| --- | --- |
| The 9 new test items | pass at `d47a7cb`; with this test file, 8 fail at `0e3a9c1` and the guard passes (throwaway worktree: 8 failed, 1 passed) |
| CR-17 reproduction (scratchpad) | the seven misrouting variants give `ok: true` at `0e3a9c1` and `ok: false` at `d47a7cb`: G005 and G008 `execution` mismatches for the five routings `route_keys` refuses, `router_calls` mismatches for the two valid-value misroutings; the unpatched baseline stays `ok: true` |
| Owner modules (detached worktree) | 191 passed |
| Plan §10.2 focused and guard suites (detached worktree) | 1,193 passed, diff 0, tree clean |
| Classifier dry-run (`--base 25b2c87… --head d47a7cb… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 34 paths, 90 changed-test targets (the same 90 as rounds 1–9) |
| Changed-test isolation (detached worktree) | 2,489 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–9 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,057 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `d47a7cb` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions |
| Comparator CLI (run from the scratchpad) | two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `e2b3ec663e848259cb3a5191c64c5e3353f057c52c7c4958317ec731c9e61390`, `ok: true`, all eight cases `match`), the same bytes as round 9's; two runs identical. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-10 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-17 thread with the pushed fix and resolve it. The CR-06 thread stays open for its owner.
3. Update the PR description with the round-10 revision and the records.
4. Watch exact-head CI and the Codex Code Review of the pushed head through the subscription. The one security review request is spent and is not repeated.
5. If both are clean, return `MERGE_PENDING` with the conditional PR-40 handoff v1.1. If either shows a finding or a failure, act on it; result v1.2 then no longer stands. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
