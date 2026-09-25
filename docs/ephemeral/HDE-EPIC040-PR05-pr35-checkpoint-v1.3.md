# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.3 (round 4)

Durable checkpoint saved with PR-35's fourth coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0–v1.2 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md`, `…-v1.1.md`, `…-v1.2.md`), all unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 4: a fourth coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 round 1: `2dad33c889260ab13f1de8aa8e0f81c972e1b067`, records `d677f5d6fd8885267c5cff4fad3949591de3e68f`. Round 2: `ab5e6e7e23787bff59138468d989dadfd89ee40e`, records `fe5f35c5bfd4b269ae788a69c568355e8f315177`. Round 3: `88016e4812515363903c608a08c8773bbdd3a9b1`, records `9d9558d62d190aad27f5eb818afba4050ab52467` (tree `e006564f34e24c6b451734f10c6ecaada23f32f1`; the remote head after the round-3 push). Round 4: corrective `145d8a1f02b2d2bbfd7b1282a070e299d391d46a` (tree `1e02a317ee9308727d8692548d589d6fda060aaf`), and records = the commit adding this file and ledger v1.4. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-3 push (2026-09-25, UTC)

- **Round-3 push.** `fe5f35c..9d9558d` at 00:40:51Z, read back with `git ls-remote` and the PR API (8 commits, 18 files).
  - CR-07's thread was answered (`discussion_r4099899468`, naming `88016e4`) and resolved.
  - CR-06's thread was answered (`discussion_r4099899919`) and left open for its owner.
  - The PR description was updated and read back.
- **CI on `9d9558d`.** `ci.yml` run `36078652901` (#3619), job `107895443267`, started 00:40:57Z. It became stale as merge evidence at 00:45:21Z, when the round-4 findings arrived. It was not cancelled: the Actions API had refused cancellation with `403` (ledger L-29). It was not treated as a gate.
- **Codex on `9d9558d`.** Code Review `5311936628` (`COMMENTED`, 00:45:24Z, trigger "New commits") raised two P2 findings. It added no comment to the open CR-06 thread. The Security Review is still the PR-open one on `96b54dd`.
- **Fallback check-in.** `trig_01SwNYSbc65fEwCcvCxc8Cqb` (2026-09-25T01:12:00Z) remains scheduled.

## Round-4 findings and dispositions

| ID | Source | Finding | Verification at `9d9558d` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-08 | Codex P2, thread `PRRT_kwDOP103ks6l0nNL` (comment `4099918434`), `tools/config/artifacts.py:349-350` | `json.loads` accepts `NaN` and `±Infinity`, which `sercanon` reproduces, so a canonical goldens document carrying one passes validation and the report then holds bare `NaN`, which strict JSON parsers reject | G006's first expected score set to `NaN`: `--report` → `"expected":NaN`, a strict parse fails, exit 1. `Infinity` behaves the same. A fractional `25.5` also passes, although canonical JSON carries integers only | **Fixed in `145d8a1`.** The goldens parser refuses every non-integer number (`parse_constant` and `parse_float` handlers): `NaN`, `±Infinity` and any fraction or exponent are `GOLDENS_INVALID` at exit 5. This implements plan §5.1's canonical JSON (PF12 §4.1), which carries integers only; the registry loader refuses non-finite numbers in the same way |
| CR-09 | Codex P2, thread `PRRT_kwDOP103ks6l0nNM` (comment `4099918435`), `tools/config/artifacts.py:826` | The report carries the absolute candidate root, against plan §5.2's `candidate_root: str (relative-safe display only)`, exposing the host layout and making identical comparisons differ by location | The positive report's `candidate_root` held the absolute scratch path of the synthetic root. `goldens_path`, a report field PR-30 added beyond plan §5.2's list, held the absolute repository path | **Fixed in `145d8a1`** (IF-06) |

Both are ordinary in-scope corrections to PR05's own new code. Neither is material and neither needs a rescope.

**In-flight decision IF-06.** The report's `candidate_root` and `goldens_path` are display values. The absolute paths are still used internally for validation and admission.
- `.` is the repository root, which is the executing installation, so it also marks CR-06's boundary.
- A path inside the repository is shown repository-relative; the default goldens display as `tests/fixtures/magic10/v1/goldens.json`.
- Anything else, including every synthetic fixture root, is `<external>`.

Identity stays in `candidate_release_id` and `goldens_sha256`. Plan §5.2 requires "relative-safe display only" without fixing the vocabulary, so this vocabulary is the decision. It extends to `goldens_path` because that field carried the same host path.

## Corrective revision `145d8a1` (2 files, +51/−7)

| Path | Change |
| --- | --- |
| `tools/config/artifacts.py` | `_golden_refuse_non_integer`, passed as `parse_constant` and `parse_float` in `_golden_load_document` (CR-08). `_golden_display`, used for `candidate_root` and `goldens_path` in `compare_goldens`; the dataclass fields are annotated as display-only (CR-09, IF-06) |
| `tests/config/test_config_artifacts.py` | 5 new items: `test_non_integer_numbers_refuse` (`nan`, `inf`, `neg_inf`, `fraction`) and `test_reports_carry_no_host_path`. 1 updated item: `test_cli_match_report_file_and_determinism` now requires reports from two different synthetic roots to be byte-identical; it used to require their `candidate_root` to differ. With this test file, those 6 items fail at `9d9558d`; all pass at `145d8a1` |

Untouched, as in rounds 1–3: everything plan §6.5 lists, including `ci/**`, the golden fixture, `tests/config/helpers.py`, the readiness tool, every F01-enumerated file and all governed evidence. No expected golden value changed. The positive report's bytes change by design: it no longer names host paths. Two fresh synthetic roots at different paths give byte-identical 1,060-byte reports (SHA-256 `d710c92405b0e3475164e48bebe1dec0200a5a211ce49ee711a9524ef4c71e5a`, `ok: true`).

## Local validation at `145d8a1`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `145d8a1`.

| Check | Result |
| --- | --- |
| The 6 new or updated test items | pass at `145d8a1`; with this test file, all 6 fail at `9d9558d` (throwaway worktree) |
| Owner modules | 143 passed |
| Plan §10.2 focused and guard suites | 1,145 passed |
| Classifier dry-run (`--base 25b2c87… --head 145d8a1… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 18 paths, 90 changed-test targets (the same 90 as rounds 1–3) |
| Changed-test isolation (detached worktree) | 2,441 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–3 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,031 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `145d8a1` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions. The known pre-existing failures are present on both sides |
| Comparator CLI | `NaN`, `Infinity` and `25.5` in G006's expected score → exit 5 `GOLDENS_INVALID`. Two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `d710c92405b0e3475164e48bebe1dec0200a5a211ce49ee711a9524ef4c71e5a`) with `candidate_root` `<external>` and `goldens_path` `tests/fixtures/magic10/v1/goldens.json`; two runs identical. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-4 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-08 and CR-09 threads with the pushed fix, and resolve them. The CR-06 thread stays open for its owner.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. Once it completes without new findings, one bare `@codex security review` request, as checkpoint v1.0 planned.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
