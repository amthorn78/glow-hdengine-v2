# HDE-EPIC040-PR05 — PR-35 corrective-push checkpoint v1.0

Durable checkpoint saved with the one PR-35 coherent corrective push and before the wait for remote-only evidence (exact-head CI and current-head Codex review). It changes no result, authority or scope and issues no PR-35 result. The PR-30 result stands: `PR_CANDIDATE_PUBLISHED`, `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md`.

| Field | Value |
| --- | --- |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Phase | PR-35: one coherent corrective revision committed and validated locally, pushed with this checkpoint; awaiting exact-head CI and current-head Codex review |
| Session | the dedicated PR-35 session for HDE-EPIC040-PR05, a top-level session Nathan created by pasting the PR-30 handoff (runtime `https://claude.ai/code/session_01H2pqAmxXnAYZPF55mPLXTQ`); `session_disposition: INITIAL_DEDICATED_ASSIGNMENT`; `role_session_ref: NOT_YET_ASSIGNED` (operator assignment; none supplied, none invented); `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR05 / PR-35`; `context_conflict: NONE`; `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Prompt | PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1, `https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`, read completely (reported revision `2026-09-24T15:48:24.405Z`); primary skill `glow-hde-pr-development` 1.3.1 |
| Original Proceed | Nathan / Product Owner's PR-30 invocation for exactly `HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN` v1.0 (SHA-256 `d50a6f1f8215124ee04fbce00538480352cf2513159b8df5030956b565675709`) with `HDE-EPIC040-PR05-PR-INSTRUCTION` v1.0 (`adb01ad8c0db18a9a8e45f6bfb183c15046aebd250a5dcbd509aa6d96f5d6ce7`); PR-35 continues under it; no second Proceed exists or was requested |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/beautiful-ritchie-6uvevf` — PR #492's head branch, the same branch as PR-30 |
| Workspace | this session's checkout at `/home/user/glow-hdengine-v2`, a fresh container clone. PR-30's container is not reachable from here; the branch, the pull request and the `docs/ephemeral/` records establish continuity, and nothing of PR-30's work was reconstructed |
| Pull request | #492 (`https://github.com/amthorn78/glow-hdengine-v2/pull/492`), open, not draft, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` |
| Commits | PR-30 implementation `96b54dd870c6abe855af55140e13094ef896bbb6`; PR-30 records `229d1f7bab7c70f16022c190da77f6622899d702` (remote head at PR-35 entry); PR-35 corrective `2dad33c889260ab13f1de8aa8e0f81c972e1b067` (tree `e21c9bc7f219e7a8d75a4f4759700f3c5de3c425`); PR-35 records = the commit adding this file and ledger v1.1. A commit cannot embed its own SHA: the records commit and the remote head read back after the push are recorded in the PR #492 body and in the next ledger version |
| PF10 read | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md`, 2,156 lines / 235,187 bytes, SHA-256 `d79e41102a88ded2cf9823787925c0ac243622cf2a3e59a3e5c1da28387e6f91` — the unique PF10 on `main` `25b2c87b`, read completely at PR-35 entry. Applicable: §2.15 (PR05 covered, line 1726), §2.12, §2.3, §2.5; §2.16–§2.18 remain PR07's. PF10 is silent on these tools' refusal tokens, so plan §§5.2–5.4 govern |
| PR activity subscription | active: the subscribe call's result confirmed this session receives PR #492's events |

**Session branch note.** The container's harness named `claude/friendly-goldberg-p04mba` as this session's development branch. That branch does not exist on `origin`, and nothing was committed to it or pushed from it. The handoff binds PR-35 to PR-30's branch and pull request (the GCF-17 continuity list), so every PR-35 commit is on `claude/beautiful-ritchie-6uvevf`.

## Remote state read at PR-35 entry (2026-09-24, UTC)

- **Remote head** `229d1f7bab7c70f16022c190da77f6622899d702` (`git ls-remote`: `refs/heads/claude/beautiful-ritchie-6uvevf` = `refs/pull/492/head`), fetched 22:55:53Z.
- **PR #492**: open, not draft, not merged, `mergeable_state: clean`, 2 commits, 12 files (+1,989/−9).
- **CI**: `ci.yml` run `36047574275`, job `107794931780` (`test`), `success` on `229d1f7` (19:21:42Z–19:33:15Z). Stale as merge evidence, because that head carries two verified review findings. It had completed before PR-35 entry, so there was nothing to cancel. The combined-status API returns 403 to this integration; check runs are read instead.
- **Codex**: Code Review `5309127743` (`COMMENTED`) on `96b54dd` with two unresolved P2 threads; Security Review completed on `96b54dd` (PR-open trigger) with no thread; summary comment `5820657559` records `mergeGateEnabled: false`, `blockingSeverityThreshold: P0`. No other reviewer. No reviewer product was installed, triggered or configured by this session.

## Findings and dispositions

| ID | Source | Finding | Verification (at `229d1f7`, Python 3.12.3 venv with the CI install, closed rails) | Disposition |
| --- | --- | --- | --- | --- |
| CR-01 | Codex P2, thread `PRRT_kwDOP103ks6lu91K`, `tools/config/generate_config_artifacts.py:306-308` | An `OSError` from `mkstemp`, the write or `os.replace` escapes the handler, which catches only `GoldenComparisonRefusal`: exit 1 with a traceback, although exit 1 is reserved for a completed comparison with mismatches | `--compare-goldens <synthetic root> --report /proc/golden-report.json` passes the destination pre-checks, the comparison matches all eight cases, then `mkstemp` raises `FileNotFoundError`: exit 1, stdout empty, traceback | **Fixed in `2dad33c`.** An `OSError` from `_write_golden_report` is the refusal `REPORT_WRITE_FAILED` (exit 5, stdout empty, one stderr line; in-flight decision IF-02); an `OSError` while inspecting the destination is `REPORT_PATH_INVALID` |
| CR-02 | Codex P2, thread `PRRT_kwDOP103ks6lu91R`, `tools/bodygraph/check_magic10_gate_readiness.py:81-82` | A missing, unreadable or non-UTF-8 `--selection-file` raises `OSError`/`UnicodeError` before any refusal: exit 1 with a traceback that includes the local path | Missing file, a directory and a non-UTF-8 file each exit 1 with a traceback naming the path | **Fixed in `2dad33c`.** `parse_selection` maps `OSError`/`UnicodeError` to `READINESS_SELECTION_INVALID` (exit 5, stdout empty) before `DBAccess.for_current_env()` is reached |
| SR-01 | PR-35's own review of the diff; the same class as CR-01/CR-02 | A goldens path or candidate root that cannot be inspected or read escapes `compare_goldens` instead of refusing | `--goldens /proc/self/mem` (a regular file whose read fails with `EIO`) exits 1 with `OSError` | **Fixed in `2dad33c`.** Such a goldens path is `GOLDENS_INVALID` and such a candidate root `CANDIDATE_ROOT_INVALID`, at exit 5 |
| SR-02 | PR-35's own review of the diff | An application case whose inputs the canonical entrypoints refuse raises `CompatBoundaryError`, which is not in the per-case failure tuple `(KeyError, TypeError, ValueError, AttributeError)`, and an empty G005 `pairs` list raises `IndexError`. Either aborts the whole comparison (exit 1, traceback, no report), contrary to plan §5.2 invariant 5 and §8.1 item 3 (an altered identity yields a mismatch) | Canonical-byte goldens variants against the synthetic root: G008 `person_uid` upper-cased, G008 Gate `0` and G005 `pairs: []` each escape (`CompatBoundaryError: ERR_READER_INVALID_CHART:…`, `IndexError`) | **Fixed in `2dad33c`.** Any exception raised while executing one case is that case's `execution` mismatch; the other seven cases are still compared and the CLI exits 1 with `GOLDEN_COMPARISON_MISMATCH:1` and a complete report. `pytest.fail` spies derive from `BaseException` and still fail their tests |

All four are ordinary in-scope corrections to PR05's own new code. None changes an objective, acceptance criterion, protected architectural, security, data-model or external-contract boundary, multi-unit scope, dependency or budget item; no rescope was raised.

**In-flight decision IF-02.** `REPORT_WRITE_FAILED` joins the tool-local refusal tokens of plan §5.4. `REPORT_PATH_INVALID` would misdescribe a failure of a valid destination (full disk, read-only filesystem, failed replace), and plan R-12 lets PR-35 adjust the CLI/exit-code design within scope as a recorded decision. Numeric-free, one stderr line, exit 5, never exit 3. Tested by `test_cli_report_write_failure_is_a_refusal_never_a_mismatch` (four items). IF-01 (PR-30) is unchanged.

## Corrective revision `2dad33c` (5 files, +152/−15)

| Path | Change |
| --- | --- |
| `tools/config/generate_config_artifacts.py` | CR-01: `REPORT_WRITE_FAILED`; destination inspection errors → `REPORT_PATH_INVALID` |
| `tools/bodygraph/check_magic10_gate_readiness.py` | CR-02: selection-file read errors → `READINESS_SELECTION_INVALID`; no new import; still a valid release member |
| `tools/config/artifacts.py` | SR-01 and SR-02 |
| `tests/config/test_config_artifacts.py` | 11 items: `test_a_case_that_cannot_execute_is_its_own_mismatch_never_a_crash` (3), `test_inputs_that_cannot_be_inspected_or_read_refuse` (3), `test_cli_report_write_failure_is_a_refusal_never_a_mismatch` (4), `test_cli_report_path_that_cannot_be_inspected_refuses` (1) |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | 1 item: `test_unreadable_selection_file_refuses_before_any_database_access` (missing, directory, non-UTF-8, permission denied; the database seam fails the test if reached) |

Untouched: everything plan §6.5 lists, including `engine/**`, `catalog/**`, `.github/workflows/ci.yml`, `ci/**` (the classifier included), `tools/evidence/**`, every F01-enumerated file, `docs/config_and_bundles.md`, `docs/pfcanon/**` and all governed evidence. No evidence writer ran.

## Local validation at `2dad33c`

All runs used closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`) with a Python 3.12.3 venv (the CI interpreter version) holding the `ci.yml` install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` → pytest 8.4.2, setuptools 84.0.0). `ci/checks/check_env_pins.sh` → OK. Each lane ran command-for-command as `.github/workflows/ci.yml` defines it at the candidate head. `git diff --exit-code` was 0 and the tree clean after every lane.

| Check | Where | Exit | Result |
| --- | --- | --- | --- |
| New tests prove the corrections | corrected tree, and `229d1f7` with the new tests copied into a throwaway worktree | 0 / 1 | 12 passed at the correction; the same 12 failed at `229d1f7` |
| Owner modules (`tests/config/test_config_artifacts.py`, `tests/bodygraph/test_check_magic10_gate_readiness.py`) | working tree = `2dad33c` | 0 | 108 passed (PR-30: 96) |
| Plan §10.2 focused and ownership guard suites | working tree = `2dad33c` | 0 | 1,110 passed (PR-30: 310 + 788) |
| Classifier dry-run `--base 25b2c87b… --head 2dad33c8… --event-name pull_request` | `2dad33c` | 0 | `reason=selected_lanes;paths=12;lanes=product,compat,db,rails,evidence,qa,release`; 90 changed-test targets, including both owner modules |
| Changed-test isolation (the `ci.yml` step) | detached worktree at `2dad33c`, `PYTHONPATH` = worktree | 0 | 2,406 passed in 204.65s (PR-30: 2,394); diff 0; tree clean |
| product lane | main tree at `2dad33c` | 0 | `generate_ordering_artifacts.py --check` OK; 20 passed |
| compat lane | main tree | 0 | CLI help, serializer guard, emitter proof OK; 101 passed, 3 skipped, 2 xfailed |
| db lane | main tree | 0 | `DIRECT_DB_CONTRACT_OK`; 249 passed |
| rails lane | main tree | 0 (lane) | runner exit 3 after `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED` (job suites 4, 112, 39 passed; `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` accepted with `INCOMPLETE_RELEASE_ROSTER` observed; `RAILS_GATE_EVIDENCE_OK`); independent probe 0; `RAILS_LANE:RELEASE_NOT_ADMITTED`; 133 passed. The accepted F01 outcome |
| evidence lane | main tree | 0 | `update_evidence_index.py --check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh` all exit 0; 111 passed in 694.33s (the duration reflects concurrent local load) |
| qa lane | detached worktree at `2dad33c` | 0 | 488 passed; diff 0; tree clean |
| release lane | main tree, with a detached worktree for its regression suites | 0 (lane) | `git diff --exit-code` 0; `release_id_recompute.py --check-manifest-only` 0; regression suites 63 passed, worktree clean; `build_release_attestation.py --output <external empty dir> --require-clean` exits 1 with the receipt `{"code":"release_not_admitted","returncode":3,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"closure_write_and_check"}`; independent probe 0; `RELEASE_LANE:RELEASE_NOT_ADMITTED`; `--verify` skipped, as `ci.yml` skips it. The accepted F01 outcome. The builder ran directly under the CI-equivalent venv, so PR-30's container-setuptools limitation (result v1.0 L-03) did not arise |
| Candidate-wide roster `pytest -q -p no:cacheprovider --ignore=tests/em` | detached worktree at `2dad33c` | 0 | 1,996 passed, 3 skipped in 159.29s (PR-30: 1,985 + the 11 new config items); diff 0; tree clean |
| Base-vs-head sweep of the 129 test files outside every lane, changed-test target and `testpaths` root (PR-30's set; `tests/em` excluded, as the roster excludes it) | throwaway worktrees at `229d1f7` and `2dad33c` | 1 / 1 | 57 failed, 546 passed, 13 errors on both sides (70 failure lines each). The diff of the sorted FAILED/ERROR node IDs is empty: zero regressions, zero fixes. The known pre-existing failures are unchanged, including F07's two in `tests/evidence/test_dev_conjunction_identity.py` |

## Awaiting, and the next actions

1. Push the corrective commit and this records commit together (`git push -u origin claude/beautiful-ritchie-6uvevf`), then read back the remote head and PR #492.
2. Reply on both Codex threads with the pushed fix, and resolve them.
3. Exact-head CI on the pushed head: all seven lanes, with the accepted `RAILS_LANE:RELEASE_NOT_ADMITTED` and `RELEASE_LANE:RELEASE_NOT_ADMITTED` outcomes and the final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK`.
4. Current-head Codex code review. It re-ran on new heads in PR04, so it is not requested; once it completes, one bare `@codex security review` request for a security review of the corrected code (instruction §11). If that request is routed to the code-review track, as both of PR04's were, the absence is recorded as a stated limitation, not a satisfied predicate.
5. Then: final records (`PR_IMPLEMENTATION_RESULT` v1.1, ledger v1.2, final checkpoint) and `MERGE_PENDING` only if every predicate holds on one unchanged head. Nathan merges manually; nothing here enables, schedules or requests a merge.

## Constraints carried (unchanged from the PR-30 checkpoint)

Closed rails for every run; plan §§4–6 scope only; governed evidence only through its owners, and none written; no synthetic release fed to a governed gate or the attestation; no `PR06R_B_FINAL_PASS`; neither tool exits 3; no test skipped, disabled, quarantined or weakened; no expected golden value rewritten from actual output; `tests/evidence/test_rails_ci_workflow_integration.py` untouched (IF-01); Codex reviews only; no merge, auto-merge or `[skip ci]`; `docs/pfcanon/` read-only; no Notion write.
