# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.8 (round 9)

Durable checkpoint saved with PR-35's ninth coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0–v1.7 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md` through `…-v1.7.md`), all unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 9: a ninth coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 rounds 1–7: as checkpoint v1.7 lists them. Round 8: `130f78c6513c8df6cdb11a48ed2ef909a5197000`, records `98f75d6ef711df8d597e3129c7e85da373da01e9` (tree `8d01f297c562e6d4627bafd4b4f7e34774e25601`; the remote head after the round-8 push). Round 9: corrective `511827f7dbdea2ad86bc325b3b09f1d1fec61e48` (tree `85cfc7486d28e715db28f8ba9a2eb23d119fb4bd`), and records = the commit adding this file and ledger v1.9. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-8 push (2026-09-25, UTC)

- **Round-8 push.** `8d92ec9..98f75d6` at 03:10:24Z; the branch and `refs/pull/492/head` read back with `git ls-remote` as `98f75d6` at 03:10:41Z.
  - CR-14's thread was answered (`discussion_r4100670697`, naming `130f78c`) and resolved.
  - CR-06's thread stays open for its owner.
  - The PR description was updated and read back: head `98f75d6`, 18 commits, 28 changed files.
- **Automatic Codex review of `98f75d6`.** The Code Review (trigger "New commits") completed at 03:14:09Z and added no review, comment or thread. The PR carries one 👍, Codex's documented no-findings signal.
- **Security review request.** One bare `@codex security review` comment (`5826076458`, 03:14:52Z), made after that clean review.
  - Codex routed it to the Code Review track: trigger "Manual request", running from 03:15:05Z. The Security Review stayed the PR-open one on `96b54dd`.
  - That manual code review, `5312904130` (`COMMENTED`, 03:19:12Z), raised the two round-9 findings below. It added no comment to the open CR-06 thread.
  - No further security review request is made; PR04's requests were routed the same way.
- **CI on `98f75d6`.** `ci.yml` run `36089278811` (#3624), job `107927945458`, 03:10:32Z–03:22:25Z, conclusion `success`. It became stale as merge evidence at 03:19:12Z, when the round-9 findings arrived. It was not cancelled: the Actions API had refused cancellation with `403` (ledger L-29). It was not treated as a gate.
- **Fallback check-in.** `trig_01HHijetSRcLLoWNYKQ4PjPM` (04:04:00Z) remains scheduled.

## Round-9 findings and disposition

| ID | Source | Finding | Verification at `98f75d6` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-15 | Codex P2, thread `PRRT_kwDOP103ks6l2iCk` (comment `4100708133`), `tools/bodygraph/check_magic10_gate_readiness.py:128-134` | A stored payload nested deeply enough in any BodyGraph field makes the current-row read reach the recursive projection validator and raise `RecursionError`, which no handler covers. One corrupt row therefore aborts the whole readiness scan with a traceback instead of being counted `payload_invalid` | A 1,200-deep and a 5,000-deep `bodygraph.authority`, both decoded and as stored text: `RecursionError` escaped `observe()` in all four cases | **Fixed in `511827f`** (IF-12) |
| CR-16 | Codex P2, thread `PRRT_kwDOP103ks6l2iCi` (comment `4100708131`), `tools/bodygraph/check_magic10_gate_readiness.py:99-102` | `--selection-file` is read with `read_text()`, so a FIFO or an unbounded device can block the run or exhaust memory before any result; these paths are readable, so round 1's unreadable-file handling does not apply | Each case ran in its own subprocess with `timeout 8`, closed rails and `DATABASE_URL` unset. A FIFO with no writer blocked until killed (exit 124). `/dev/zero`, under a 1.2 GB address-space cap, ended in a `MemoryError` traceback. `/dev/null` was accepted as an empty selection (`READINESS_EMPTY_SELECTION`). A symlink and an 8 MiB regular file were read and accepted (`READINESS_UNAVAILABLE`) | **Fixed in `511827f`** (IF-13) |

PR-35 reviewed both classes.
- **CR-15, other exceptions from corrupt rows.** A scratchpad diagnostic sent 178 corrupt stored payloads through `observe()`. They covered deep lists and objects in each BodyGraph field, non-finite and huge numbers, non-JSON Python types, invalid UTF-8, lone surrogates and whole-payload corruption.
  - At `98f75d6`, `RecursionError` was the only exception that escaped (56 rows).
  - At `511827f`, none escapes, and 166 rows are classified.
  - At both heads, 12 rows are counted ready: a huge integer or a lone surrogate in a descriptive field. The Reader's per-row path accepts all 12 too, because the projection does not type the descriptive fields, so readiness and the Reader still agree.
- **CR-16, other file inputs in PR05's tools.** The comparator already refuses these before any read, each promptly at exit 5:
  - `--goldens` as a FIFO, `/dev/zero`, `/dev/null` or a symlink: `GOLDENS_INVALID`, since it requires a non-symlinked regular file;
  - `--report` aimed at a FIFO: `REPORT_PATH_INVALID`;
  - a FIFO as the candidate root: `CANDIDATE_ROOT_INVALID`.

  It needed no change. It reads a regular goldens file whole, as its canonical-bytes check requires.

Both are ordinary in-scope corrections to PR05's own new code. Neither is material, and neither needs a rescope.

**In-flight decision IF-12.** A row whose stored payload is nested past the recursion limit is `payload_invalid`, with the diagnostic code `DB_PAYLOAD_INVALID`, the read path's own code for a payload it cannot decode.
- The rest of the selection is still observed.
- Plan §5.3 maps `DB_PAYLOAD_INVALID` to `payload_invalid`. It does not name `RecursionError`, which no owner turns into a typed refusal, so how that error is classified is the decision.
- The report keys, tokens and exit codes are unchanged, and such a row is never ready.

**In-flight decision IF-13.** The selection file must be a regular, non-symlinked file of at most `SELECTION_FILE_MAX_BYTES`, 1,048,576 bytes, which is about 28,000 canonical UUID lines.
- It is opened without following a final symlink and without blocking. Its type is checked on the opened descriptor, so the check has no race with the read, and at most one byte past the bound is read.
- Anything else is refused with the existing `READINESS_SELECTION_INVALID` before any database access.
- The tool imports `os`, which plan §8.2 item 8 already lists, and `stat`. The import-purity allow-list gains both.

## Corrective revision `511827f` (2 files, +131/−14)

| Path | Change |
| --- | --- |
| `tools/bodygraph/check_magic10_gate_readiness.py` | `read_selection_file()` opens the selection with `O_RDONLY \| O_NOFOLLOW \| O_NONBLOCK`, requires `S_ISREG` on the descriptor and reads at most `SELECTION_FILE_MAX_BYTES + 1` bytes; `parse_selection` uses it (CR-16, IF-13). `observe()` counts a `RecursionError` as `payload_invalid` with `DB_PAYLOAD_INVALID` and continues (CR-15, IF-12). The module docstring states the selection-file rule |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | 7 new items: `test_a_payload_nested_past_the_recursion_limit_is_payload_invalid` ×2 (decoded, text; the deep row sorts first and the row after it is still read); `test_special_symlinked_or_oversized_selection_files_refuse_before_any_read` ×4 (`fifo`, `device`, `symlink`, `oversized`), under a 2-second alarm whose exception is not an `OSError`, so a blocking read fails the test instead of hanging it; `test_selection_file_at_the_size_bound_is_read` (a valid file of exactly the bound is read). 1 updated item: `test_unreadable_selection_file_refuses_before_any_database_access` injects its permission failure at `os.open`, the new read seam. The import-purity allow-list gains `os` and `stat`. With this test file, 8 fail at `98f75d6` (8 failed, 51 passed); all 59 pass at `511827f` |

The readiness tool is a release-roster member, so its new bytes change the synthetic release's identity, and the comparator's positive report changes only in `candidate_release_id`. Two fresh synthetic roots at different paths give byte-identical 1,060-byte reports (SHA-256 `e2b3ec663e848259cb3a5191c64c5e3353f057c52c7c4958317ec731c9e61390`, `ok: true`, all eight cases `match`), and two runs are byte-identical. Untouched: the comparator and its CLI, the golden fixture, `ci/**`, `tests/config/**`, every F01-enumerated file and all governed evidence.

## Local validation at `511827f`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `511827f`.

| Check | Result |
| --- | --- |
| The 7 new test items and the updated one | pass at `511827f`; with this test file, 8 fail at `98f75d6` (throwaway worktree: 8 failed, 51 passed) |
| Corrupt-payload diagnostic (scratchpad) | 178 stored payloads: 56 `RecursionError` escapes at `98f75d6`; none at `511827f`, where 166 are classified and the 12 counted ready are accepted by the Reader's per-row path too |
| Owner modules (detached worktree) | 182 passed |
| Plan §10.2 focused and guard suites (detached worktree) | 1,184 passed, diff 0, tree clean |
| Classifier dry-run (`--base 25b2c87… --head 511827f… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 28 paths, 90 changed-test targets (the same 90 as rounds 1–8) |
| Changed-test isolation (detached worktree) | 2,480 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–8 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,048 passed, 3 skipped, diff 0, tree clean (unchanged: the readiness test module lies outside the roster) |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `511827f` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions |
| Readiness CLI (each in a subprocess with `timeout 8`, `DATABASE_URL` unset) | a FIFO, `/dev/zero` (under a 1.2 GB address-space cap), `/dev/null`, a symlink and an 8 MiB file each refuse promptly at exit 5 with `READINESS_SELECTION_INVALID`, stdout empty; a regular selection file proceeds to `READINESS_UNAVAILABLE`; `SAFE_MODE=0` → `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]` before the selection is read |
| Comparator CLI | two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `e2b3ec663e848259cb3a5191c64c5e3353f057c52c7c4958317ec731c9e61390`, `ok: true`, all eight cases `match`), differing from round 8's only in `candidate_release_id`; two runs identical. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER`. `--goldens` as a FIFO, `/dev/zero`, `/dev/null` or a symlink → `GOLDENS_INVALID`; a FIFO as `--report` → `REPORT_PATH_INVALID`; a FIFO as the candidate root → `CANDIDATE_ROOT_INVALID`; each at exit 5 |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-9 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-15 and CR-16 threads with the pushed fix, and resolve them. The CR-06 thread stays open for its owner.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. The one security review request is spent and is not repeated.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation, and the missing current-head security review as a limitation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
