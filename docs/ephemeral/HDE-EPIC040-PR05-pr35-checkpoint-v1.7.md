# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.7 (round 8)

Durable checkpoint saved with PR-35's eighth coherent corrective push and before the wait for remote-only evidence on the pushed head. It continues checkpoints v1.0–v1.6 (`docs/ephemeral/HDE-EPIC040-PR05-pr35-checkpoint-v1.0.md` through `…-v1.6.md`), all unchanged as issued. It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35 round 8: an eighth coherent corrective revision, committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session, prompt, original Proceed, repository/branch, workspace, PF10 read, subscription | unchanged from checkpoint v1.0 |
| Pull request | #492, open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30: `96b54dd870c6abe855af55140e13094ef896bbb6`, `229d1f7bab7c70f16022c190da77f6622899d702`. PR-35 rounds 1–6: as checkpoint v1.6 lists them. Round 7: `af3bc83d9fd515afa18a86f0dfd334ad98eb76dc`, records `8d92ec9bbc1a79526338cfc2cac213195cfb2b98` (tree `416ad98cf1748a7823ac9c81101bf176e81f5c22`; the remote head after the round-7 push). Round 8: corrective `130f78c6513c8df6cdb11a48ed2ef909a5197000` (tree `d86c8790898e6a4917a3eff0da19710f3225bcd9`), and records = the commit adding this file and ledger v1.8. A commit cannot embed its own SHA: the records commit and the remote head read back after this push are recorded in the PR #492 body and in the next record |

## What happened after the round-7 push (2026-09-25, UTC)

- **Round-7 push.** `8f5921c..8d92ec9` at 02:45:29Z; the branch and `refs/pull/492/head` read back with `git ls-remote` as `8d92ec9`.
  - CR-13's thread was answered (`discussion_r4100541959`, naming `af3bc83`) and resolved.
  - CR-06's thread stays open for its owner.
  - The PR description was updated and read back through the PR API: head `8d92ec9`, 16 commits, 26 changed files, `updated_at` 02:50:19Z. That update came after the round-8 finding was posted (02:49:42Z) and before this session read it, so its line calling the pushed head's review "pending" was already out of date. The round-8 update replaces it.
- **CI on `8d92ec9`.** `ci.yml` run `36087583667` (#3623), job `107922785472`, 02:45:37Z–02:53:34Z, conclusion `success`. It became stale as merge evidence at 02:49:42Z, when the round-8 finding arrived. It was not cancelled: the Actions API had refused cancellation with `403` (ledger L-29). It was not treated as a gate.
- **Codex on `8d92ec9`.** Code Review `5312729056` (`COMMENTED`, 02:49:42Z; the summary shows it completed at 02:49:45Z, trigger "New commits") raised one P2 finding, on the readiness tool. It added no comment to the open CR-06 thread, and nothing on the round-7 change. The Security Review is still the PR-open one on `96b54dd`.
- **Fallback check-in.** `trig_015bPQGWSWxynbr9Qrt5B7sZ` fired at 03:02:53Z. Its instructions described the round-5 state, which PR-35 had already passed, so this session only verified the current state: the branch and `refs/pull/492/head` read back as `8d92ec9` with `git ls-remote` at 03:03:46Z; its check run `107922785472` was `success` and stale, as above; CR-14 was unresolved and under correction here. The next check-in is `trig_01HHijetSRcLLoWNYKQ4PjPM`, for 04:04:00Z.

## Round-8 finding and disposition

| ID | Source | Finding | Verification at `8d92ec9` (same venv, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-14 | Codex P2, thread `PRRT_kwDOP103ks6l2Lf_` (comment `4100564650`), `tools/bodygraph/check_magic10_gate_readiness.py:145` | `read_current_mapped_bodygraph` checks the row key and the payload's self-consistency, not that the payload names the selected user. A current row keyed to the selected UUID, whose two consistent `person_uid` fields name another UUID, is therefore counted `READY`. The production Reader passes the same row through `resolve_compat_chart` and `bind_projection_identity` and refuses it with `IDENTITY_CONFLICT` | Three payload labels were each counted `READY`: another UUID, a `person-` label for another UUID, and a non-UUID label. The Reader's own resolution call refused each with `identity_conflict`/`IDENTITY_CONFLICT`: `resolve_compat_chart({"user_id": …}, source_policy="local", env=None, local_lookup=…)`, as `adapter/http_reader.py` makes it. The production Reader route answered `503 ERR_M10_BODYGRAPH_INCOMPLETE`. Both accepted the same-identity spellings: `person-` plus the selected UUID, and an uppercase spelling | **Fixed in `130f78c`** (IF-11) |

PR-35's review of the class compared the tool's per-row outcome with the Reader's whole per-row path: the same current-row read, then the route's resolution call, then `evaluation_party`, which re-applies the shared Gate predicate and requires the bound identity. After the read, the identity binding was the only per-row check the Reader applied that the tool did not.

A scratchpad diagnostic built 1,080 synthetic current rows: 18 payload labels × 3 nested-label variants × 10 Gate lists × 2 row keys.
- At `8d92ec9`, 30 rows were counted ready although the Reader refused them.
- All 30 carry a payload identity the Reader refuses with `IDENTITY_CONFLICT`: another UUID, a `person-` label for another UUID, `PERSON-` or `person-` with an uppercase UUID, a `birth-` seed, `person-x`, or a non-UUID label.
- At `130f78c`, the tool and the Reader agree on all 1,080 rows (26 ready). The tool reports each of the 30 as `IDENTITY_CONFLICT`.

It is an ordinary in-scope correction to PR05's own new code. It is not material and needs no rescope.
- Plan §5.3 maps every `BodyGraphProjectionError` without a Gate-ingress code to `payload_invalid`. `IDENTITY_CONFLICT` is one of these, so no count key, token or exit code changes.
- Plan §5.3 also says "the tool adds no validator". The tool still adds none of its own: it calls the projection owner's existing identity binding, the one the Reader applies.

**In-flight decision IF-11.** The readiness tool binds each returned row's payload identity to the selected UUID with `bind_projection_identity` from `engine.bodygraph.projection`, as the production Reader does through `resolve_compat_chart`.
- The binding runs only for a returned row, right after `read_current_mapped_bodygraph`, inside the existing refusal handling.
- A refusal takes that row's existing `BodyGraphProjectionError` outcome: `payload_invalid`, with the diagnostic code `IDENTITY_CONFLICT`.
- Accepted spellings of the same identity stay ready: the canonical UUID, `person-` plus it, and any other spelling of it.
- Plan §8.2 item 8 names three symbols the tool imports from `engine.bodygraph.projection`. `bind_projection_identity` is a fourth from the same module, which the import-purity test already allows.

## Corrective revision `130f78c` (2 files, +38/−3)

| Path | Change |
| --- | --- |
| `tools/bodygraph/check_magic10_gate_readiness.py` | `observe()` calls `bind_projection_identity(row.payload, user_id)` for each returned row, inside the existing refusal handling; the import gains `bind_projection_identity`; the module docstring names the binding (CR-14, IF-11) |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | 9 new items. `test_bad_rows_are_counted_without_a_false_ready` gains three rows whose payload names another UUID, a `person-` label for another UUID, or a non-UUID label; each is `payload_invalid` with `IDENTITY_CONFLICT`, beside a good row. `test_a_row_is_ready_exactly_when_the_reader_resolves_it` (×6) runs the same current row through the tool and through the Reader's resolution call. The three same-identity spellings are `READY` and resolve. The three conflicting identities are `NOT_READY` with `IDENTITY_CONFLICT`, and the Reader refuses them with `identity_conflict`. With this test file, 6 fail at `8d92ec9` (6 failed, 46 passed) and all pass at `130f78c`; the three same-identity items pass at both |

The readiness tool is a release-roster member, so its new bytes change the synthetic release's identity, and the comparator's positive report changes only in `candidate_release_id`. Two fresh synthetic roots at different paths give byte-identical 1,060-byte reports (SHA-256 `0508803b446c7593b99aba8b6f5f1f2572e023e6e49fe0bf8582eff94ba51fe7`, `ok: true`, all eight cases `match`), and two runs are byte-identical. Untouched: the comparator and its CLI, the golden fixture, `ci/**`, `tests/config/**`, every F01-enumerated file and all governed evidence.

## Local validation at `130f78c`

Python 3.12.3 venv carrying the `ci.yml` install (pytest 8.4.2, setuptools 84.0.0). Closed rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`. Every lane was run command-for-command as `ci.yml` defines it, at the committed head `130f78c`.

| Check | Result |
| --- | --- |
| The 9 new test items | pass at `130f78c`; with this test file, 6 fail at `8d92ec9` (throwaway worktree: 6 failed, 46 passed) and the 3 same-identity items pass there |
| Class diagnostic (scratchpad) | 1,080 synthetic rows: 30 disagreements with the Reader's per-row path at `8d92ec9`, all identities the Reader refuses with `IDENTITY_CONFLICT`; none at `130f78c` (26 ready), where the tool reports each of the 30 as `IDENTITY_CONFLICT` |
| Owner modules (detached worktree) | 175 passed |
| Plan §10.2 focused and guard suites (detached worktree) | 1,177 passed, diff 0, tree clean |
| Classifier dry-run (`--base 25b2c87… --head 130f78c… --event-name pull_request`) | all seven lanes, `reason=selected_lanes`, 26 paths, 90 changed-test targets (the same 90 as rounds 1–7) |
| Changed-test isolation (detached worktree) | 2,473 passed, diff 0, tree clean |
| product | 20 passed |
| compat | 101 passed, 3 skipped, 2 xfailed |
| db | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails | runner exit 3 after `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` (accepted: `INCOMPLETE_RELEASE_ROSTER` observed) and `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED`; probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; then 133 passed |
| evidence | every read-only check exit 0; 111 passed |
| qa (detached worktree) | 488 passed, diff 0, tree clean |
| release | `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed (detached worktree); the attestation builder exited 1 with the receipt `release_not_admitted` (stage `closure_write_and_check`, inner return code 3); probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`. Identical to rounds 1–7 |
| Roster `python -m pytest -q -p no:cacheprovider --ignore=tests/em` (detached worktree) | 2,048 passed, 3 skipped, diff 0, tree clean (unchanged from round 7: the readiness test module lies outside the roster) |
| Sweep of the 129 uncovered test files, `25b2c87` (base) vs `130f78c` | 57 failed, 546 passed, 13 errors on both sides; identical 70-line failure lists; zero regressions |
| Readiness CLI | closed rails without `DATABASE_URL` → exit 5 `READINESS_UNAVAILABLE`, stdout empty; `SAFE_MODE=0` → exit 5 `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]`, stdout empty |
| Reader agreement (scratchpad) | The six CR-14 identity variants were run through the tool, the Reader's resolution call and the production Reader route (Flask test client over a fake current view). The three conflicting identities are `NOT_READY` with `IDENTITY_CONFLICT`; the resolution call refuses them and the route answers `503 ERR_M10_BODYGRAPH_INCOMPLETE`. The three same-identity spellings are `READY`; they resolve, and the route answers `200` |
| Comparator CLI | two fresh synthetic roots at different paths → exit 0, byte-identical 1,060-byte reports (SHA-256 `0508803b446c7593b99aba8b6f5f1f2572e023e6e49fe0bf8582eff94ba51fe7`, `ok: true`, all eight cases `match`), differing from round 7's only in `candidate_release_id`; two runs identical. Repository root → exit 5 `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` |
| `git diff --check` | clean |
| Tree | clean after every lane |

## Awaiting, and the next actions

1. Push the round-8 corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on the CR-14 thread with the pushed fix, and resolve it. The CR-06 thread stays open for its owner.
3. Exact-head CI on the pushed head, with all seven lanes, the accepted `RELEASE_NOT_ADMITTED` lane outcomes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. The Codex code review auto-triggered on the pushed head. Once it completes without new findings, one bare `@codex security review` request, as checkpoint v1.0 planned.
5. Then the final records and `MERGE_PENDING`, only if every predicate holds on one unchanged head. CR-06 is disclosed there as an open, owner-routed observation. Nathan merges manually.

## Constraints carried

Unchanged from checkpoint v1.0.
