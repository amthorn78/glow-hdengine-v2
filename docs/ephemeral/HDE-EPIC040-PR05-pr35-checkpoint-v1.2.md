# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.2 (round 3)

Durable checkpoint saved with PR-35's third coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0 and v1.1 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md`, `…-v1.1.md`), both unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 3: a third coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 round 1: `2dad33c889260ab13f1de8aa8e0f81c972e1b067`, records `d677f5d6fd8885267c5cff4fad3949591de3e68f`. PR-35 round 2: `ab5e6e7e23787bff59138468d989dadfd89ee40e`, records `fe5f35c5bfd4b269ae788a69c568355e8f315177` (tree `de2a36c2ab7fa582e70e1b8a0afa9543c2fffe31`; the remote head after the round-2 push). PR-35 round 3: corrective `88016e4812515363903c608a08c8773bbdd3a9b1` (tree `c6719558e1f79ccd082a6aac83d222bd8bc84992`), and records = the commit adding this file and ledger v1.3. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-2 push (2026-09-25, UTC)

- **Round-2 push.** `d677f5d..fe5f35c` at 00:09:26Z, read back with `git ls-remote` and the PR API. The three round-2 Codex threads were answered, each naming `ab5e6e7`, and resolved:
  - `discussion_r4099743469` (CR-03);
  - `discussion_r4099743943` (CR-04);
  - `discussion_r4099744231` (CR-05).

  The PR description was updated and read back.
- **CI on `fe5f35c`.** `ci.yml` run `36076225717` (#3618), job `107887920581`, 00:09:31Z–00:21:17Z, conclusion `success`.
  - It became stale as merge evidence at 00:13:50Z, when the round-3 findings arrived.
  - It was not cancelled: the Actions API had refused cancellation with `403` in round 1 (ledger L-29), so no retry was made. It was not waited on and was not treated as a gate.
  - Its success confirms that hosted CI agrees with the local lane equivalents for the round-2 code.
- **Codex on `fe5f35c`.** Code Review `5311755820` (`COMMENTED`, 00:13:50Z, trigger "New commits") raised two P1 findings. The Security Review is still the PR-open one on `96b54dd`.
- **Fallback check-in.** A new self check-in is scheduled (`send_later`, trigger `trig_01SwNYSbc65fEwCcvCxc8Cqb`, 2026-09-25T01:12:00Z).

## Round-3 findings and dispositions

| ID | Source | Finding | Verification at `fe5f35c` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-06 | Codex P1, thread `PRRT_kwDOP103ks6l0Pn2` (comment `4099764480`), `tools/config/artifacts.py:406` | The application runners execute the executing installation's modules. Admission binds executing code to the candidate's bytes only for the admission owner's eight covered modules, so a manifest-consistent candidate whose application member cannot run is still reported `ok: true` | A synthetic root whose `engine/compat/compute.py` is replaced by `raise RuntimeError(…)`, manifest re-cut: admitted; `compare_goldens` → `ok: true`; CLI exit 0 | **Not fixable within PR05; routed to its owner** (observation O-17; thread left open for that owner). The `compare_goldens` docstring now states the boundary |
| CR-07 | Codex P1, thread `PRRT_kwDOP103ks6l0Pn4` (comment `4099764484`), `tools/config/artifacts.py:338-341` | The annotation pin excludes `inputs` and `expected`, so a collection carrying the canonical identity with consistently altered content reports `ok: true` | G006's first pair `[48,48]` → `[50,50]` with its expected row → `{"q": [50,50], "score": 25, "band": "Open"}`: `ok: true`, CLI exit 0. Swapping G004's member Gate sets, which leaves every output unchanged: `ok: true` | **Fixed in `88016e4`** (IF-05) |

**Why CR-06 is routed rather than fixed, and why it is not a rescope.**

- **Its fix lies outside PR05.**
  - Binding executing code to captured candidate bytes has one owner: the admission execution-provenance and executable-equivalence owner in `engine/config/registry_loader.py`. Its coverage is the eight modules that retain `_MODULE_EXECUTION`.
  - PF10 §2.12 (PR03-R02) extended that coverage only through an approved rescope overlay, and it keeps a single owner. A comparator-local check would be a second admission authority.
  - Extending the coverage to `engine/compat/compute.py`, `engine/bodygraph/*` and `presenter/reader_v1/emitter.py` changes `engine/**` and `presenter/**`, both hard exclusions of this work unit (plan §4.3).
  - Executing the candidate's own implementation would need a subprocess, which plan §11.2 excludes, or an in-process import of unverified candidate code.
- **The approved plan already scopes the case.** Plan §5.2 invariant 3 says a fixture candidate's success is test-only and never release admission. In the intended release use after PR06, the candidate root is the repository root, which is the executing installation itself. PR05's approved scope is delivered as designed, so no change is needed to deliver it.
- **Precedent.** The accepted PR04 lineage (PF10 §2.19) routed its review findings O-12, O-20 and O-21 the same way: to their owners, with threads intentionally left open.
- **Owner.** Whether the application modules join the executable-equivalence coverage is for the admission owner and the IA (the PR03-R02 precedent), and for PR06, which owns complete release admission. It is recorded for PR-40.

**In-flight decision IF-05.** Each case's `inputs` and `expected` are bound to the committed PF01 §9.5 transcription by `GOLDEN_TRANSCRIPTION_SHA256`. For each case, the pin holds the SHA-256 of `sercanon(case["inputs"])` and of `sercanon(case["expected"])`: 16 digests of the committed fixture, never of comparator output.
- A differing collection still runs, so an altered value yields its own mismatches.
- The difference itself is that case's `transcription.inputs` or `transcription.expected` mismatch, so a consistently altered case is never a match.
- It is a mismatch rather than a refusal because plan §8.1 item 3 requires altered goldens documents, including a changed G008 UUID, to report their mismatches, and plan §8.3 makes an identity mismatch a mismatch.
- It completes IF-03: identity, annotations and content are all bound to the transcription.

## Corrective revision `88016e4` (2 files, +102/−14)

| Path | Change |
| --- | --- |
| `tools/config/artifacts.py` | `GOLDEN_TRANSCRIPTION_SHA256` and `_golden_transcription_mismatches`, appended to each case's mismatches in `compare_goldens` (CR-07, IF-05). The `compare_goldens` docstring states that the entrypoints are the executing installation's and that admission proves executable equivalence only for the admission owner's covered modules, so another candidate root is a fixture candidate (CR-06) |
| `tests/config/test_config_artifacts.py` | 3 new items: `test_transcription_digests_pin_the_committed_cases`, and `test_a_consistently_altered_case_is_never_a_match` with `g006_inputs_and_expected` (Codex's exact example) and `g004_members_swapped`. 22 existing items now also expect the transcription row: `test_each_alteration_yields_exactly_its_mismatches` (6), `test_several_alterations_are_all_reported_in_sorted_order` (1), `test_unconsumed_or_unknown_input_fields_are_mismatches` (10), `test_a_case_that_cannot_execute_is_its_own_mismatch_never_a_crash` (3), `test_added_or_missing_expected_keys_are_mismatches` (1) and `test_cli_mismatch_is_a_single_token_and_the_report_holds_every_mismatch` (1). With this test file, those 25 items fail at `fe5f35c`; all pass at `88016e4` |

Untouched, as in rounds 1 and 2: everything plan §6.5 lists, including `ci/**`, the golden fixture, `tests/config/helpers.py`, the readiness tool, every F01-enumerated file and all governed evidence. No expected golden value changed. The positive report is unchanged: byte-identical to the report at `229d1f7` and `ab5e6e7` for the same candidate root.

## Local validation at `88016e4`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `88016e4`.

| Check | Result |
| --- | --- |
| The 25 new or updated test items | pass at `88016e4`; with this test file, all 25 fail at `fe5f35c` (throwaway worktree) |
| Owner modules | 138 passed |
| Plan §10.2 focused and guard suites | 1,140 passed |
| Classifier dry-run (`--base 25b2c87… --head 88016e4… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 16 paths, 90 changed-test targets (the same 90 as rounds 1 and 2) |
| Changed-test isolation (detached worktree) | 2,436 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1 and 2 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,026 passed, 3 skipped, diff 0, tree clean |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `88016e4` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions. The known pre-existing failures are present on both sides |
| Comparator CLI | synthetic complete-release root: exit 0, all eight cases `match`, two runs byte-identical and byte-identical to the report at `229d1f7` for the same root (1,210 bytes, SHA-256 `77208a05b85e50363f15798c398ea5a692996d0151fb5a11ec65fe92d6c60300`). Codex's G006 example: exit 1, `GOLDEN_COMPARISON_MISMATCH:2`. Repository root: exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER`. CR-06's scenario still exits 0, as its disposition records |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-3 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-07 thread with the pushed fix and resolve it. Reply on the CR-06 thread with the disposition and leave it open for its owner.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. Once it completes, one bare `@codex security review` request, as checkpoint v1.0 planned.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
