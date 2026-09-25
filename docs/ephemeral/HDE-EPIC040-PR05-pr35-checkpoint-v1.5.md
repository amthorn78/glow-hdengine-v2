# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.5 (round 6)

Durable checkpoint saved with PR-35's sixth coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0–v1.4 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md` through `…-v1.4.md`), all unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 6: a sixth coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 rounds 1–4: as checkpoint v1.4 lists them. Round 5: `26b760a8728137380acd456596bf29419e1ff3ea`, records `78b84f989a9bb98d932e31c6e9e2a45d651d329e` (tree `20c1d59d12e61496cb8c219972e9098ec3720813`; the remote head after the round-5 push). Round 6: corrective `daa2110af8f1ff46b667fff399ed1c49bd10071a` (tree `71ebf55ef3fcb34b90ddb28ef99472d4f096445e`), and records = the commit adding this file and ledger v1.6. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-5 push (2026-09-25, UTC)

- **Round-5 push.** `4c178ef..78b84f9` at 01:58:16Z, read back with `git ls-remote` and the PR API (12 commits, 22 files).
  - CR-10's thread was answered (`discussion_r4100292424`, naming `26b760a`) and resolved.
  - CR-11's thread was answered (`discussion_r4100292912`, naming `26b760a`) and resolved.
  - CR-06's thread stays open for its owner.
  - The PR description was updated and read back.
  - A fallback check-in was scheduled: `trig_015bPQGWSWxynbr9Qrt5B7sZ`, for 03:02:00Z.
- **CI on `78b84f9`.** `ci.yml` run `36084293735` (#3621), job `107912629760`, started 01:58:21Z. It completed at 02:10:21Z with conclusion `success`. It became stale as merge evidence at 02:02:21Z, when the round-6 finding arrived. It was not cancelled: the Actions API had refused cancellation with `403` (ledger L-29). It was not treated as a gate.
- **Codex on `78b84f9`.** Code Review `5312419770` (`COMMENTED`, 02:02:21Z, trigger "New commits") raised one P2 finding, on the readiness tool. It added no comment to the open CR-06 thread, and nothing on the round-5 changes. The Security Review is still the PR-open one on `96b54dd`.

## Round-6 finding and disposition

| ID | Source | Finding | Verification at `78b84f9` (same venv) | Disposition |
| --- | --- | --- | --- | --- |
| CR-12 | Codex P2, thread `PRRT_kwDOP103ks6l1jXE` (comment `4100311449`), `tools/bodygraph/check_magic10_gate_readiness.py:156` | Under `SAFE_MODE=0`, `ALLOW_NETWORK=1` or missing locale and timezone pins, the readiness tool goes straight to `DBAccess.for_current_env()`, unlike the comparison mode, which refuses before doing any work; AGENTS.md requires the closed determinism rails for QA surfaces | With `SAFE_MODE=0`, with `ALLOW_NETWORK=1`, and with `TZ` unset, a spy on `DBAccess.for_current_env` recorded the provider being constructed | **Fixed in `daa2110`** (IF-09) |

It is an ordinary in-scope correction to PR05's own new code. It is not material and needs no rescope.
- Plan §5.3 already says the tool "never opens rails". It lists the tool's refusal tokens without a rails refusal.
- Plan §5.4 reuses the existing `RAILS_CLOSED_REQUIRED:<…>` token unchanged.
- In this repository `SAFE_MODE` and `ALLOW_NETWORK` gate vendor acquisition (`engine/bodygraph/resolver.py`), not database reads. The engine CLI's `_fetch_db_bodygraph` (`engine/cli/main.py`) and the Reader's `_reader_current_rows` (`adapter/http_reader.py`) construct `DBAccess` and read current rows with no rails check. So a separately authorized live readiness observation still runs under closed rails, with `DATABASE_URL` set.

The class review found no other PR05 entrypoint that works outside closed rails. The comparator checks the rails first, in both `compare_goldens` and its CLI. The readiness tool's `observe()` receives an injected provider and constructs none.

**In-flight decision IF-09.** The readiness tool requires the closed determinism rails: the `engine.runtime.determinism_env` pins `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `SAFE_MODE=1` and `ALLOW_NETWORK=0`.
- The check runs after argument parsing and before the tool reads the selection or constructs a database provider, so a usage error keeps argparse's exit 2.
- Outside the rails, the tool refuses at exit 5 with stdout empty and one stderr line, `RAILS_CLOSED_REQUIRED:<pins>`. That token has the comparator's format: it names each unmet pin with its required value, for example `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]`, and never the value found in the environment.

Plan §5.3 lists the tool's refusal tokens without a rails refusal, so adding the existing token is the decision.

## Corrective revision `daa2110` (2 files, +46/−4)

| Path | Change |
| --- | --- |
| `tools/bodygraph/check_magic10_gate_readiness.py` | `require_closed_rails()`, called first in `main` after argument parsing; the import of `DETERMINISM_ENV_PINS` and `expected_env` from `engine.runtime.determinism_env`; the module docstring names the rails and the token (CR-12, IF-09) |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | 4 new items: `test_open_or_unpinned_rails_refuse_before_any_database_access` (`safe_mode_open`, `network_allowed`, `tz_unset`, `locale_unpinned`). Each asserts the exact token, empty stdout, no leak, a database seam that fails the test if reached, and that the rails refusal comes before an empty or unreadable selection. The import-purity allow-list gains `engine.runtime.determinism_env`. With this test file, the 4 new items fail at `78b84f9` (4 failed, 37 passed); all pass at `daa2110` |

The readiness tool is a release-roster member, so its new bytes change the synthetic release's identity. Nothing outside `docs/ephemeral/` pins its bytes or path. The comparator's positive report therefore changes only in `candidate_release_id`. Two fresh synthetic roots at different paths give byte-identical 1,060-byte reports (SHA-256 `8c0915df75756821492642b9e82549678346aa06b712e091b92aef465b54206f`, `ok: true`), and two runs are byte-identical. Untouched: the comparator, the golden fixture, `ci/**`, `tests/config/helpers.py`, every F01-enumerated file and all governed evidence.

## Local validation at `daa2110`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `daa2110`.

| Check | Result |
| --- | --- |
| The 4 new test items | pass at `daa2110`; with this test file, all 4 fail at `78b84f9` (throwaway worktree: 4 failed, 37 passed) |
| Owner modules | 159 passed |
| Plan §10.2 focused and guard suites | 1,161 passed |
| Classifier dry-run (`--base 25b2c87… --head daa2110… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 22 paths, 90 changed-test targets (the same 90 as rounds 1–5) |
| Changed-test isolation (detached worktree) | 2,457 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–5 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,043 passed, 3 skipped, diff 0, tree clean (unchanged from round 5: the readiness test module lies outside the roster, because `pytest.ini` `testpaths` names only `tests/bodygraph/test_gates.py` from that directory) |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `daa2110` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions. The known pre-existing failures are present on both sides |
| Readiness CLI | `SAFE_MODE=0`, `ALLOW_NETWORK=1`, or `TZ` unset or empty → exit 5, stdout empty, stderr `RAILS_CLOSED_REQUIRED:` naming only the unmet pin with its required value (for example `[('SAFE_MODE', '1')]`). Closed rails without `DATABASE_URL` → exit 5 `READINESS_UNAVAILABLE`; empty selection → `READINESS_EMPTY_SELECTION` |
| Comparator CLI | two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `8c0915df75756821492642b9e82549678346aa06b712e091b92aef465b54206f`), differing from round 5's only in `candidate_release_id`; two runs identical. The CR-10, CR-11, SR-04 and SR-05 behaviours are unchanged. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-6 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-12 thread with the pushed fix, and resolve it. The CR-06 thread stays open for its owner.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. Once it completes without new findings, one bare `@codex security review` request, as checkpoint v1.0 planned.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
