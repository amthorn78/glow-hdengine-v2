# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.4 (round 5)

Durable checkpoint saved with PR-35's fifth coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0–v1.3 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md`, `…-v1.1.md`, `…-v1.2.md`, `…-v1.3.md`), all unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 5: a fifth coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 round 1: `2dad33c889260ab13f1de8aa8e0f81c972e1b067`, records `d677f5d6fd8885267c5cff4fad3949591de3e68f`. Round 2: `ab5e6e7e23787bff59138468d989dadfd89ee40e`, records `fe5f35c5bfd4b269ae788a69c568355e8f315177`. Round 3: `88016e4812515363903c608a08c8773bbdd3a9b1`, records `9d9558d62d190aad27f5eb818afba4050ab52467`. Round 4: `145d8a1f02b2d2bbfd7b1282a070e299d391d46a`, records `4c178efc6ab8aa39c5011c306a13f440ff2d81e3` (tree `06112b85ed8f48d9bcc6c90b12f34b43e409d484`; the remote head after the round-4 push). Round 5: corrective `26b760a8728137380acd456596bf29419e1ff3ea` (tree `e170ca82abfeb56099733e09f910e7f4bf9dd68c`), and records = the commit adding this file and ledger v1.5. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-4 push (2026-09-25, UTC)

- **Round-4 push.** `9d9558d..4c178ef` at 01:04:19Z, read back with `git ls-remote` and the PR API (10 commits, 20 files).
  - CR-08's thread was answered (`discussion_r4100031693`, naming `145d8a1`) and resolved.
  - CR-09's thread was answered (`discussion_r4100032147`, naming `145d8a1`) and resolved.
  - CR-06's thread stays open for its owner.
  - The PR description was updated and read back.
- **CI on `4c178ef`.** `ci.yml` run `36080399801` (#3620), job `107900862554`, 01:04:23Z–01:16:32Z, conclusion `success`. It became stale as merge evidence at 01:09:51Z, when the round-5 findings arrived. It was not cancelled: the Actions API had refused cancellation with `403` (ledger L-29). It was not treated as a gate.
- **Codex on `4c178ef`.** Code Review `5312116351` (`COMMENTED`, 01:09:51Z, trigger "New commits") raised two P1 findings. It added no comment to the open CR-06 thread. The Security Review is still the PR-open one on `96b54dd`.
- **Fallback check-in.** `trig_01SwNYSbc65fEwCcvCxc8Cqb` fired at 01:13:10Z (`run_once_fired`), during the round-5 remediation. Its instruction to resolve new findings locally first is what this round did.

## Round-5 findings and dispositions

| ID | Source | Finding | Verification at `4c178ef` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-10 | Codex P1, thread `PRRT_kwDOP103ks6l086c` (comment `4100061832`), `tools/config/generate_config_artifacts.py:278` | The report destination check excludes the candidate root and the repository but not the goldens file, so `--goldens X --report X` replaces the golden collection with the report | A copy of the committed goldens as X, with a synthetic complete-release root: exit 0, empty stderr, and X then held the report (its SHA-256 changed from `0fd92a9e…b1ac` to one beginning `e938121fc342a8a4`) | **Fixed in `26b760a`.** `_golden_report_destination` also refuses the resolved goldens path, so a report aimed at the goldens file is `REPORT_PATH_INVALID` at exit 5, however the path is spelled, and the file is left unchanged. This implements plan §5.2 invariant 6: nothing is written under the goldens path. The `--report` help now says "never over the goldens file" |
| CR-11 | Codex P1, thread `PRRT_kwDOP103ks6l086d` (comment `4100061833`), `tools/config/artifacts.py:685` | The G007 runner passes a working bundle provider and router and no cache spy, so it observes only the returned payload. PF01 §9.5 says a valid self-pair calls neither Engine Core, the intrinsic cache nor the narrative router | A wrapper around `evaluate_pair` that calls the bundle provider and the router for every same-UUID pair before delegating: `ok: true`, zero mismatches | **Fixed in `26b760a`** (IF-07). Plan §5.1's G007 row expects `core_cache_router_called: false`, which PR-30's fixture omitted |
| SR-04 | PR-35's own review of CR-11's class: every plan §5.1 expected value checked against the fixture and the runners | Plan §5.1's G007 adverse row expects `pair_key_created: false` (PF01 §9.5: the inconsistent self-pair "creates no pair_key"). PR-30's fixture omitted the key, and the adverse run passed plain seams and no cache, so a regression that took the admitted bundle or touched the cache before raising was not observed | A wrapper that takes the admitted bundle for the inconsistent self-pair before delegating: `ok: true`, zero mismatches | **Fixed in `26b760a`** (IF-07) |
| SR-05 | PR-35's own review of CR-08's class, on the observed side | A mismatch's observed value reaches the report unchanged. A value canonical JSON cannot carry therefore breaks the report or the CLI. A float or `NaN` is not canonical JSON (PF12 §4.1), and bare `NaN` is not JSON at all. Bytes or an arbitrary object cannot be serialized, so rendering raises | An injected `_reduce_category` returning `NaN` made the `--report` file hold bare `NaN` (a strict parse fails) at exit 1. Returning bytes or an object made `TypeError` escape the CLI: a traceback, no token, no report | **Fixed in `26b760a`** (IF-08) |

All four are ordinary in-scope corrections to PR05's own new code. None is material and none needs a rescope.

The class review found no other gap. Every other plan §5.1 expected value is carried by the fixture and observed by its runner, except four entries that are not observable values:
- G007's `not_an_error`: an exception from any case is that case's `execution` mismatch, and `evaluate_pair_result` is compared exactly.
- G006's `bounds_and_weights_from_candidate`: the runner reads the bounds and weights only from the admitted bundle.
- G002's `balance_note` and G005's `nonclaim`: prose, carried in the cases' `notes` under the annotation pin.

**In-flight decision IF-07.** G007's two "nothing is touched" expectations are observed through the three seams `evaluate_pair` accepts, each recording every call.
- The bundle provider stands for Engine Core. The canonical `evaluate_pair` reaches `compute_core`, and `intrinsic_pair_key`, only after it has taken the admitted bundle from the provider.
- The intrinsic cache is a recording spy that holds nothing: `get` returns `None` and `put` stores nothing.
- The router is a recording wrapper around the fixture router.

For the valid self-pair, in both orders (AB and BA), a call on any seam makes `core_cache_router_called` `true`. For the inconsistent self-pair (the adverse variant), reaching the bundle provider or the cache, or returning a result that carries `pair_key`, makes `pair_key_created` `true`. A router call alone is not a created pair key. Either `true` is a mismatch against the expected `false`. Plan §5.1 fixes the expected values but not how they are observed, so this mechanism is the decision.

**In-flight decision IF-08.** Every mismatch value passes through one normaliser, `_golden_reportable`, before it is reported.
- Integers, strings, booleans, `null`, and arrays and string-keyed objects of them pass unchanged. That is what canonical JSON carries.
- A float is reported as `<float R>`, with Python's `repr`: for example `<float 24.5>` or `<float nan>`.
- Anything else is reported as `<TypeName>`: for example `<bytes>`.

The descriptions are deterministic, so the report stays canonical, rendering it never fails, and exit 1 keeps its single `GOLDEN_COMPARISON_MISMATCH:<n>` token. A described value never equals an expected one: the comparison runs on the raw values, and only the reported copy is described. Plan §5.2 requires a canonical report and this exit contract but does not say how a non-canonical observation is shown, so this vocabulary is the decision.

## Corrective revision `26b760a` (4 files, +164/−10)

| Path | Change |
| --- | --- |
| `tools/config/generate_config_artifacts.py` | `_golden_report_destination` takes the goldens path and refuses a destination equal to its resolved path; the call site passes it; the `--report` help names the exclusion (CR-10) |
| `tools/config/artifacts.py` | `_GoldenCacheSpy` and `_golden_recording_seams`. `_golden_run_self_pair` runs the valid self-pair and the adverse variant with recording seams; its observed values gain `core_cache_router_called`, and each adverse row gains `pair_key_created` (CR-11, SR-04, IF-07). G007's `transcription.expected` pin in `GOLDEN_TRANSCRIPTION_SHA256` changes from `6280843e…c339` to `3a93fad1…08b4`; its `inputs` pin is unchanged. `_golden_reportable`, applied to every mismatch's `expected` and `actual` in `compare_goldens` (SR-05, IF-08) |
| `tests/fixtures/magic10/v1/goldens.json` | G007's `expected` gains `core_cache_router_called: false`, and its adverse row gains `pair_key_created: false`, both transcribed from plan §5.1's G007 row (PF01 §9.5), not from any observed output. The document is rewritten canonically: 25,972 → 26,030 bytes, SHA-256 `0fd92a9e81443308c2a968def39d191af3d0d92d3eb3445cee0bff8b9931b1ac` → `9f99c6aa633cf4713c3de9d37a1d70157fe632e08740ec1c505ecc202486ace5`. Every other case, and every other G007 value, is unchanged |
| `tests/config/test_config_artifacts.py` | 12 new items. `test_self_pair_that_reaches_core_cache_or_router_is_a_mismatch` has six: `valid-bundle_provider`, `valid-cache` and `valid-router`, each expecting exactly `M10-G007` `expected.core_cache_router_called`; `inconsistent-bundle_provider` and `inconsistent-cache`, each expecting exactly `expected.adverse[0].pair_key_created`; and `every-bundle_provider`, Codex's scenario, expecting both. `test_cli_report_path_equal_to_the_goldens_refuses` has two: the same path, and the same file through a symlinked directory. `test_non_canonical_observed_values_are_described_never_a_crash` has four: `float`, `nan`, `bytes` and `object`, each injected into G006's first observed score. Each expects exactly one mismatch with the described value, exit 1 with `GOLDEN_COMPARISON_MISMATCH:1`, and a `--report` file that parses strictly and is canonical. 2 extended items: the fixture test and the positive test assert that both G007 values are `false`. With this test file, those 14 items fail at `4c178ef` (14 failed, 104 passed); all pass at `26b760a` |

**How the commit was made.** Round 5 has one corrective commit, as rounds 1–4 did. It was reached through two local amends, and neither intermediate commit was pushed.
- `47129809e150540d425691abf661570c2c7aa5d4` (01:16:34Z) held the CR-10 and CR-11 fix.
- The SR-04 fix was folded in, giving `4cae13ee4c38c85b74cffa6c97001cdf6f3a0e6e` (01:32:42Z).
- The SR-05 fix was folded in, giving `26b760a` (01:43:58Z).

Each intermediate's validation was stopped when the next own-review finding superseded it (ledger L-79, L-83). With the final test file:
- `47129809` fails 9 items: the fixture and positive tests, the three `inconsistent`/`every` variants and the four SR-05 items;
- `4cae13e` fails the 4 SR-05 items.

Unlike rounds 1–4, the golden fixture changes. The change adds the two plan §5.1 G007 values PR-30 omitted. No existing expected value changed, and nothing was taken from actual output. Still untouched: everything else plan §6.5 lists, including `ci/**`, `tests/config/helpers.py`, the readiness tool, every F01-enumerated file and all governed evidence. Nothing outside `docs/ephemeral/` pins the fixture's digest. The positive report changes only in `goldens_sha256`, because a matching case's row carries its outcome, not its values. Two fresh synthetic roots at different paths give byte-identical 1,060-byte reports (SHA-256 `05fb8f622866961a2fef70adb2d66f3cf6cd11cab05972203b833ba664bedde7`, `ok: true`), and two runs are byte-identical. SR-05 leaves a matching report unchanged.

## Local validation at `26b760a`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `26b760a`.

| Check | Result |
| --- | --- |
| The 14 new or extended test items | pass at `26b760a`; with this test file, all 14 fail at `4c178ef` (throwaway worktree: 14 failed, 104 passed), 9 fail at `4712980` and 4 at `4cae13e` |
| Owner modules | 155 passed |
| Plan §10.2 focused and guard suites | 1,157 passed |
| Classifier dry-run (`--base 25b2c87… --head 26b760a… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 20 paths, 90 changed-test targets (the same 90 as rounds 1–4) |
| Changed-test isolation (detached worktree) | 2,453 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–4 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,043 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `26b760a` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions. The known pre-existing failures are present on both sides |
| Comparator CLI | `--goldens X --report X` → exit 5 `REPORT_PATH_INVALID`, stdout empty, X unchanged. Codex's CR-11 wrapper → `ok: false` with `M10-G007` `expected.adverse[0].pair_key_created` and `expected.core_cache_router_called`; the SR-04 wrapper → `ok: false` with `expected.adverse[0].pair_key_created`. The SR-05 injections (`NaN`, bytes or an object from `_reduce_category`) → exit 1 with the single token, and every `--report` file parses strictly. Two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `05fb8f622866961a2fef70adb2d66f3cf6cd11cab05972203b833ba664bedde7`) with `goldens_sha256` `9f99c6aa…ace5`; two runs identical. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-5 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-10 and CR-11 threads with the pushed fix, and resolve them. The CR-06 thread stays open for its owner.
3. Schedule a fallback check-in about an hour out, in case webhook events arrive late.
4. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
5. The Codex code review auto-triggered on the pushed head. Once it completes without new findings, one bare `@codex security review` request, as checkpoint v1.0 planned.
6. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
