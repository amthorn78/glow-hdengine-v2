# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.11 (round 11)

This durable checkpoint is saved with PR-35's eleventh coherent corrective push.
- It continues checkpoints v1.0–v1.10 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md` through `…-v1.10.md`), all unchanged as issued.
- **Result v1.2 and handoff v1.1 no longer stand.** Codex CR-18 and CR-19 arrived on result v1.2's own records head, `e4e9d38`. Both stay unchanged as issued.
- This push issues result v1.3 (`MERGE_PENDING`), ledger v1.12 and the conditional PR-40 handoff v1.2. The pushed head's CI and Codex review are verified after the push.
- It changes no authority or scope. The PR-30 result stands unchanged: `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 11: an eleventh coherent corrective revision, committed and validated locally, and pushed with this checkpoint, result v1.3, ledger v1.12 and handoff v1.2. Awaiting exact-head CI and the Codex review of the pushed head |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, not merged; base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a`, unchanged since PR-30 |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 rounds 1–10: as checkpoint v1.10 lists them, and round 10's records commit `e4e9d38deb4d37208d5ac79b4bf2bd0a0c9ccfc9` (tree `93b85c733a050c221b039c94724adf5ac7bf8854`; the remote head before this push). Round 11: corrective `2842282e82b8e3bea5631b32ebfb2088e2cd91e4` (tree `c5eae5c7c32fa7adf0313cb68d1dec4d8292dcf8`); records: the commit adding this file, result v1.3, ledger v1.12 and handoff v1.2. A commit cannot embed its own SHA, so the records commit and the remote head read back after this push are recorded in the PR #492 body and the PR-35 return |

## What happened after the push of result v1.2 (2026-09-25, UTC)

- **Push.** `0e3a9c1..e4e9d38` at 04:41:45Z. The branch read back as `e4e9d38` at 04:41:47Z, and `refs/pull/492/head` at 04:42:05Z.
- **CR-17 reply.** The thread was answered at 04:42:00Z (`discussion_r4101158886`), naming `d47a7cb`, and resolved.
- **PR description.** It was updated with round 10 and read back, identical to the posted text: 61,702 characters, SHA-256 `e42a357eda3c28dc77f6b3a8523b38213f17f2a4c9ab613bd1b299170f44b4cc`. The PR showed head `e4e9d38`, 23 commits and 38 changed files.
- **Codex's automatic review of `e4e9d38`.** Code Review `5313479520` (`COMMENTED`, 04:45:57Z, trigger "New commits") raised the two round-11 findings below. It added no comment to the CR-06 thread. Result v1.2 had made its `MERGE_PENDING` conditional on a clean review of that head (its §1), so from here that result no longer stands.
- **CI on `e4e9d38`.** Run `36095483387` (#3627), job `107946759450`, ran 04:41:55Z–04:53:44Z and concluded `success`. All seven lanes reproduced round 10's local counts, and the run ended with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. It is stale as merge evidence from 04:45:57Z. It was not cancelled, because the Actions API refuses cancellation with `403` (ledger L-29), and it was not treated as a gate. The PR then read `mergeable_state: clean`.
- **Fallback check-in.** `trig_01QSPEPU5TXtjqKXr8QAKZaW` fired at 05:07:56Z, during round 11. It asks for exactly the round-11 work, so nothing further was owed. A new check-in is scheduled after this push.

## Round-11 findings and disposition

| ID | Source | Finding | Verification at `e4e9d38` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-18 | Codex P2, thread `PRRT_kwDOP103ks6l3qfg` (comment `4101175976`), `ci/checks/classify_ci_changes.py:1153` | The BodyGraph tool owner lookup applies only to `.py`. The prefix's lane mapping makes `_lanes_for_path()` non-null and so bypasses the unknown-source failure. An unregistered `.sh` or `.sql` tool under `tools/bodygraph/` therefore gets lanes with no owner test | `refresh.sh` and `probe.sql` under the prefix: lanes `db`, `product`, `release`, `changed_test_targets` `[]`. The base classifier raises `CI_SOURCE_OWNER_TEST_MISSING` for both | **Fixed in `2842282`** (IF-15) |
| CR-19 | Codex P2, thread `PRRT_kwDOP103ks6l3qff` (comment `4101175972`), `tools/config/artifacts.py:360` | `--goldens` is read whole before it is validated, so a sparse or oversized file can exhaust memory instead of being refused with `GOLDENS_INVALID` | A 3 GiB sparse file under `ulimit -v 1500000`: `MemoryError` traceback, exit 1. An 8 MiB file: read whole, then exit 5 | **Fixed in `2842282`** (IF-16) |
| SR-06 | PR-35's own review of CR-19's class | `os.fdopen` refuses a directory descriptor without closing it, so a bounded reader leaked the descriptor it had opened for a directory path. Round 9's selection reader has this code, and the drafted goldens reader copied it | A directory as `--selection-file`: `READINESS_SELECTION_INVALID`, with one more open descriptor afterwards (`/proc/self/fd`) | **Fixed in `2842282`** |

**Class review.**
- **CR-18.** All 7,144 tracked paths classify identically at `e4e9d38` and `2842282`, with the same lanes and the same changed-test targets or errors. Non-source files under the prefix keep plan §6.2's lanes with no owner target. On `main`, the `tools/qa/` prefix treats its files the same way, `.sh` and `.sql` included (observation O-22, for the classifier owner).
- **CR-19.** The comparator never reads the report path. The admission owner reads each candidate member whole before comparing its size and hash with the manifest (`engine/config/registry_loader.py::_read_captured_file`). That is outside PR05's scope and is recorded as observation O-21 for the admission owner. The config writer's whole reads predate PR05 and read only the repository's own outputs. Round 9's class review of CR-16 had covered FIFOs, devices and symlinks as `--goldens`, but not an oversized regular file.
- **SR-06.** In PR05's changed files, the two bounded readers were the only instances. The report writer's `os.fdopen` wraps a `mkstemp` file, which is always regular.

All three are ordinary in-scope corrections to PR05's own code. None is material, and none needs a rescope.

**In-flight decisions.**
- **IF-15.** The BodyGraph tool owner rule covers every `_UNKNOWN_SOURCE_SUFFIXES` suffix (`.py`, `.sh`, `.sql`), not only the `*.py` that plan §6.2 names. The lanes, the registered owner and the 90 changed-test targets are unchanged.
- **IF-16.** A goldens document must be a regular, non-symlinked file of at most `GOLDENS_MAX_BYTES`, 1,048,576 bytes; the committed collection is 26,030 bytes. It is read through an `O_RDONLY | O_NOFOLLOW | O_NONBLOCK` descriptor, type-checked on that descriptor and closed on every path. Anything else is `GOLDENS_INVALID`, exit 5, before admission.

## Corrective revision `2842282` (5 files, +167/−15)

| Path | Change |
| --- | --- |
| `ci/checks/classify_ci_changes.py` | The fail-closed owner lookup applies to every `_UNKNOWN_SOURCE_SUFFIXES` suffix under `tools/bodygraph/` (CR-18, IF-15) |
| `tools/config/artifacts.py` | `GOLDENS_MAX_BYTES` and `_golden_read_bounded`: the bounded, type-checked read of the goldens, which closes its descriptor on every path (CR-19, IF-16, SR-06) |
| `tools/bodygraph/check_magic10_gate_readiness.py` | `read_selection_file()` checks the type on the raw descriptor and closes the descriptor on every path (SR-06) |
| `tests/config/test_config_artifacts.py` | 6 new items: the bound pin; a sparse 8 GiB file under a 2 GiB address-space cap, in a subprocess; FIFO, device, directory and oversized files, each leaving no descriptor open. 2 updated items: the goldens `open` and `read` failures are injected at the new reader's seams |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | 4 new items: `test_every_unregistered_bodygraph_source_fails_closed` ×3 and the selection-file `[directory]` variant. Every selection-file refusal now also leaves no descriptor open |

The comparator's positive report changes only in `candidate_release_id`, because the readiness tool is a release-roster member of the synthetic release: 1,060 bytes, SHA-256 `3bd47e505583fa29bf819750b5030d203e768dcc7b5365b8a8c8df7aed77065a`.

Untouched: the comparator's CLI, the golden fixture, `tests/config/helpers.py`, every other classifier rule, every F01-enumerated file and all governed evidence.

## Local validation at `2842282`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `2842282`.

| Check | Result |
| --- | --- |
| The round-11 test items | 10 new and 6 updated or extended items pass at `2842282`. With both test files, 19 items were run at `e4e9d38`, the 3 unchanged guards included, and 7 of them failed there (throwaway worktree: 7 failed, 12 passed), each for its named cause. A mutation check, the leaking draft of the goldens reader, fails only the `[directory]` item |
| CR-18 and CR-19 reproduction (scratchpad) | at `e4e9d38`: `tools/bodygraph/refresh.sh` and `probe.sql` get lanes with `changed_test_targets` `[]`; a 3 GiB sparse `--goldens` file under `ulimit -v 1500000` ends in a `MemoryError` traceback at exit 1, and an 8 MiB file is read whole before `GOLDENS_INVALID`. At `2842282`: both tools raise `CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING`, and both goldens files exit 5 `GOLDENS_INVALID` in about 0.18 s |
| Classifier comparison over every tracked path | 7,144 paths: identical lanes and changed-test targets or errors at `e4e9d38` and `2842282` |
| Owner modules (detached worktree) | 201 passed |
| Plan §10.2 focused and guard suites (detached worktree) | 1,203 passed, diff 0, tree clean |
| Classifier dry-run (`--base 25b2c87… --head 2842282… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 38 paths, 90 changed-test targets (the same 90 as rounds 1–10) |
| Changed-test isolation (detached worktree) | 2,499 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–10 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,063 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `2842282` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions |
| Comparator CLI (run from the scratchpad) | two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `3bd47e505583fa29bf819750b5030d203e768dcc7b5365b8a8c8df7aed77065a`, `ok: true`, all eight cases `match`); two runs identical. Only `candidate_release_id` differs from round 10's report, because the readiness tool, a synthetic-roster member, changed. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-11 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-18 and CR-19 threads with the pushed fix and resolve them. The CR-06 thread stays open for its owner.
3. Update the PR description with the round-11 revision and the records.
4. Watch exact-head CI and the Codex Code Review of the pushed head through the subscription, with a fallback check-in about an hour out. The one security review request is spent and is not repeated.
5. If both are clean, return `MERGE_PENDING` with the conditional PR-40 handoff v1.2. If either shows a finding or a failure, act on it; result v1.3 then no longer stands. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
