# HDE-EPIC040-PR05 — PR Implementation Result v1.0 (PR-30)

| Field | Value |
| --- | --- |
| Artifact | `PR_IMPLEMENTATION_RESULT` — `HDE-EPIC040-PR05-PR-IMPLEMENTATION-RESULT` v1.0 (initial; no predecessor) |
| `WORK_UNIT_ID` | HDE-EPIC040-PR05 — Full golden comparison and read-only Gate readiness |
| Change | `EPIC / HDE-EPIC040 / Separation Pass 3`; `HDE-EPIC040-SPECIFICATION` v1.1 (`SPECIFICATION_APPROVED`) |
| Producer | The dedicated PR05 PR-development session, PR-30 phase; `EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION` |
| Result | `PR_CANDIDATE_PUBLISHED` |
| Prompt | PR-30 — PR Implementation Proceed — 091426.1 (`https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`) |
| Repository / branch | `amthorn78/glow-hdengine-v2` / `claude/beautiful-ritchie-6uvevf` |
| Pull request | [#492](https://github.com/amthorn78/glow-hdengine-v2/pull/492) — opened by this phase; the one work vehicle |
| Base (`origin/main`, merge-base) | `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` (the merge of the plan PR #491) |
| Implementation commit / tree | `96b54dd870c6abe855af55140e13094ef896bbb6` / tree `c6d2238d2ff757626c6c1aee4d75c72adcd544c7` (9 files, +1,704 / −9) |
| Remote head after the implementation push | `96b54dd870c6abe855af55140e13094ef896bbb6`, read back with `git ls-remote` |
| Records commit (this file, the ledger, the checkpoint) | the commit that adds these three files; a commit cannot embed its own SHA. Its SHA and the remote head after its push are recorded verbatim in the PR #492 body and in the ledger at PR-35 entry |
| Recorded by | the dedicated PR05 session (runtime `https://claude.ai/code/session_01FTff5iBZhV6crMfp7dkvxh`), 2026-09-24 (UTC) |

## 1. Outcome

One coherent, locally validated candidate for the exact approved plan is published on pull request #492. Everything below is PR-30 implementation evidence: the implemented scope, the planning decisions applied, one in-flight decision, every local validation command with its exit status and counts, the comparator's and readiness tool's observed CLI behaviour, and the limitations. It is **not** a QA verdict, acceptance, release admission, PF09 movement, Ops, deployment, merge or closure, and it claims no hosted CI result (PR-35 reads and drives those). Nathan / Product Owner merges manually; nothing here enables or schedules a merge.

## 2. Authority, identity and controlling sources

| Source | Exact identity | Repository path |
| --- | --- | --- |
| Product Owner Proceed | Nathan's pasted PR-30 invocation: "this invocation by Nathan / Product Owner is the PR-30 Proceed for exactly HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN v1.0 together with HDE-EPIC040-PR05-PR-INSTRUCTION v1.0. No additional approval object is required." Authorizes implementation and publication only | pasted invocation (this session) |
| Detailed PR plan | `HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN` v1.0, SHA-256 `d50a6f1f8215124ee04fbce00538480352cf2513159b8df5030956b565675709`, re-verified from `main` at Proceed time | `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-plan-v1.0.md` |
| PR instruction | `HDE-EPIC040-PR05-PR-INSTRUCTION` v1.0, SHA-256 `adb01ad8c0db18a9a8e45f6bfb183c15046aebd250a5dcbd509aa6d96f5d6ce7` | `docs/ephemeral/HDE-EPIC040-PR05-pr-instruction-v1.0.md` |
| Immutable approved base | `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1 (`10732f93…61be`) with Plan Review v2.1 (`47f73e62…d0b3`, original `PLAN_REVIEW_ID` preserved); Specification v1.1; Implementation Audit v2.0; accepted PR01–PR04 lineage — all as plan §2.1 lists them | plan §2.1 |
| Current PF10 read | PF10 — HDE Build Notes v13.3, SHA-256 `d79e41102a88ded2cf9823787925c0ac243622cf2a3e59a3e5c1da28387e6f91`; the same bytes the plan and the instruction resolved; Addendum Index 2.1–2.19 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md` |
| Active overlays applied | §2.15 PR04-F01 (PR05 covered): governed gates and the attestation end `RELEASE_NOT_ADMITTED`; no synthetic release fed to a gate or the attestation; no `PR06R_B_FINAL_PASS`; F01-enumerated files untouched. §2.12 PR03-R02: every candidate root admitted through `_load_active_mechanics_bundle_from_root`. §2.3 C040-05: the four-argument core is the only calculator. §2.5 C040-06. The rest as plan §2.3 | plan §2.3 |
| Subject-matter canon | PF01 v1.3.7 §9.5 (goldens), PF12 v2.9.5, PF05 v2.5.2 §3.4, PF02 v2.4.5, PF14 v3.5.7 §6.7, PF03 v1.8.7 — resolved as plan §2.2 records; `docs/pfcanon/` was read only | plan §2.2 |
| Session identity | `session_disposition: RETAIN_EXISTING` (the same dedicated PR05 session that produced the plan); `role_session_ref: NOT_YET_ASSIGNED` (operator assignment; none was supplied, none invented); `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR05 / PR-30`; `context_conflict: NONE` | — |

No Google Doc, DOC, DOCX or Drive copy was opened; Notion was read only (the PR-30 prompt page, reported revision `2026-09-24T15:47:45.499Z`); no Notion page was written.

## 3. Recovery and baseline verification before any work vehicle was created

- Open pull requests in `amthorn78/glow-hdengine-v2` read through the GitHub API: **none**. The remote branch `claude/beautiful-ritchie-6uvevf` did not exist at PR-30 entry (`git ls-remote --heads` empty; the plan PR #491 from this branch was merged and its remote branch removed). No PR05 worktree, partial result or work vehicle existed anywhere accessible.
- Local branch `claude/beautiful-ritchie-6uvevf` re-based on `origin/main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a` (the #491 merge), tree clean before implementation.
- The plan and instruction bytes on `main` hash exactly to the values in §2.

## 4. Implemented scope (plan §§5–6; checkpoints C1–C3)

| Path | Change | Size / SHA-256 at the implementation commit |
| --- | --- | --- |
| `tests/fixtures/magic10/v1/goldens.json` | **New.** PF01 §9.5 M10-G001–G008 transcribed per plan §5.1; canonical bytes (`sercanon`, sort_keys, one LF); closed top-level keys `schema`, `source`, `constants`, `cases`; every case carries `case_type`, `kind`, `realizable_chart_claim`, `input_provenance`, `inputs`, `expected`, `notes`. Values transcribed from PF01, never derived from tool output; agreement with the PF01 literals is a test | 25,972 B / `0fd92a9e81443308c2a968def39d191af3d0d92d3eb3445cee0bff8b9931b1ac` |
| `tools/config/artifacts.py` | **Modified** (+577). Appended the read-only comparator: `GoldenComparisonRefusal`, `Mismatch`, `CaseOutcome`, `GoldenComparison`, `compare_goldens(candidate_root, goldens_path=GOLDENS_DEFAULT_PATH)`, `render_golden_report`, the `_golden_*` loaders/validators/admission/runners/diff. Rails first; goldens validated (regular non-symlink file, canonical-bytes identity, duplicate-key refusal, closed schema, membership, case-type table) before admission; admission exactly once through `_load_active_mechanics_bundle_from_root`; per-kind runners call only the canonical kernel/application entrypoints; leaf diff plus canonical-bytes comparison; sorted mismatches; `"<absent>"` marks a missing leaf | 749 lines |
| `tools/config/generate_config_artifacts.py` | **Modified** (+74). `--compare-goldens CANDIDATE_ROOT` in the mutually exclusive mode group; `--goldens PATH`; `--report PATH`; `_golden_report_destination` (refuses paths inside the candidate root or the repository, symlinks, missing parents → `REPORT_PATH_INVALID`); `_write_golden_report` (temp file + `os.replace`); `_compare_goldens_main` (exit `0` report on stdout / `1` `GOLDEN_COMPARISON_MISMATCH:<n>` / `5` refusal token; stdout empty on non-zero). `--allow-aliases` with the mode, and `--goldens`/`--report` without it, are `parser.error` (exit 2) | 353 lines |
| `tools/bodygraph/check_magic10_gate_readiness.py` | **New.** Read-only Magic-10 Gate readiness per plan §5.3: strict canonical-UUID selection (`--user-id` repeated and/or `--selection-file`), sorted and duplicate-refusing; `DBAccess.for_current_env()`; per UUID `read_current_mapped_bodygraph` (one parameterized read-only `SELECT`, D-01); outcomes `ready`/`missing`/`duplicate`/`row_invalid`/`payload_invalid`/`gates_invalid`; abort as `READINESS_UNAVAILABLE` on `DB_QUERY_FAILED`/`AdapterError`; aggregate identity-free report `magic10_gate_readiness.v1` on stdout at exit 0; refusal tokens on stderr at exit 5; never 3. No `__init__.py` (namespace subpackage like `tools/cli`) | 6,752 B / `4af35c248c9f0bc228323a22e21dc06f2236570462daac240cf76ab1f0cab484` |
| `tests/config/helpers.py` | **Modified** (D-02). `_SYNTHETIC_PLACEHOLDERS` is now empty; the synthetic complete release copies the real readiness member bytes (synthetic `release_id` becomes `486ef2d1961fb57d8801a6d3b2a1edddfa3d0ed92eda8c06acac380f589c92c2`) | 5 lines removed, 4 added |
| `ci/checks/classify_ci_changes.py` | **Modified** (+42). `_TEST_SUPPORT_OWNER_PATHS["tests/fixtures/magic10/v1/goldens.json"] = ("tests/config/test_config_artifacts.py",)`; new `_BODYGRAPH_TOOL_PREFIX`, `_BODYGRAPH_TOOL_LANES = {"db","product","release"}`, `_BODYGRAPH_TOOL_TEST_OWNERS`, `_bodygraph_tool_owner_targets` (fail closed `CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING:<path>` / `CI_BODYGRAPH_TOOL_OWNER_TEST_INVALID`), wired into `changed_test_targets` and `_registered_owner_test_paths`; `_lanes_for_path` rule for `tools/bodygraph/`. `_CONFIG_WRITER_TEST_OWNERS`, `_FULL_VALIDATION_*`, `_DOCUMENTATION_PREFIXES`, fixed-lane providers and PR04 registrations unchanged (see IF-01) | — |
| `tests/config/test_config_artifacts.py` | **Modified** (+517). Third section "HDE-EPIC040-PR05" with the comparator tests of plan §8.1 (IF-01 places them here): 20 test functions, 60 collected items for the module | 893 lines |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | **New.** Readiness tests of plan §8.2: 18 test functions, 36 collected items | `cb2fa05fed9edb3864770a3c05a537e05979b8e3b4ceab1e9d4aa5868b25e875` |
| `docs/config_and_bundles.md` | **Modified** (+1). One bullet describing `--compare-goldens` | — |

**Explicitly unchanged** (plan §6.5): `engine/**`, `catalog/**` (including `catalog/manifest.json`), `schemas/**`, `migrations/**`, `adapter/**`, `presenter/**`, `goldens/**`, `.github/workflows/ci.yml`, `ci/jobs/**`, other `ci/checks/*`, `tools/evidence/**`, `tools/cli/**`, `tests/support/pr04_fixtures.py`, `tests/compat/test_evaluate_pair_eligibility.py`, `tests/core/**`, `tests/evidence/**` (including the F01-enumerated `tests/evidence/test_rails_ci_workflow_integration.py`), `docs/pfcanon/**`, all generated evidence. No governed artifact was regenerated, no evidence writer ran, no Index/Mirror row, hash sentinel, path proof or acceptance token was added (plan §6.3).

### 4.1 Contracts as landed (plan §§5.2–5.4, verified by tests and by the CLI runs in §7.7–§7.8)

- Comparator API and CLI exactly as plan §5.2: `compare_goldens` → `GoldenComparison(schema="magic10_golden_comparison.v1", candidate_root, goldens_path, goldens_sha256, candidate_release_id, config_id, cases, mismatches, ok)`; report keys `candidate_release_id, candidate_root, cases, config_id, goldens_path, goldens_sha256, mismatches, ok, schema`; refusal tokens `GOLDENS_INVALID`, `GOLDENS_MEMBERSHIP_INVALID`, `GOLDENS_CASE_TYPE_INVALID`, `CANDIDATE_ROOT_INVALID`, `CANDIDATE_ADMISSION_REFUSED:<code>`, `REPORT_PATH_INVALID`, existing `RAILS_CLOSED_REQUIRED:<…>`; mismatch token `GOLDEN_COMPARISON_MISMATCH:<n>`; exits `0`/`1`/`5` (+ argparse `2`).
- Readiness exactly as plan §5.3: report `{"schema":"magic10_gate_readiness.v1","readiness","provider","read_only":true,"selection":{"requested","sha256"},"counts":{ready,missing,duplicate,row_invalid,payload_invalid,gates_invalid},"diagnostics":[{"code","count"}…]}`; tokens `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE`; exits `0`/`5` (+ argparse `2`); never `3`.
- Neither tool is a gate stage, a job-definition step, an evidence writer or an HTTP surface; no public route, flag, payload field or transport changed.

## 5. Planning decisions applied (plan §14)

| ID | Applied | Evidence |
| --- | --- | --- |
| D-01 | Yes — `DBAccess.query` through `read_current_mapped_bodygraph`; no `exec`, `tx` or `readonly_tx` | `test_lookup_is_the_parameterized_read_only_current_row_statement` (pins `mapped_cache.CURRENT_ROW_SQL`), the `exec`/`tx` spies in the readiness module's autouse fixture, `test_module_imports_only_read_paths_and_is_a_valid_release_member` |
| D-02 | Yes — placeholder removed; real member bytes copied | `test_synthetic_release_copies_the_real_tool_and_still_admits`; the twelve `tests/config/helpers.py` owner suites are among the 90 changed-test targets (§7.3, 2394 passed) |
| D-03 | Yes — every application case runs with the fixture router stub; the default router is never used | `test_runs_leave_candidate_goldens_repository_and_seams_untouched` (spies on `route_keys`/`get_pack`/`load_pack`, seam snapshots, narrative-mount snapshots before/after) |
| D-04 | Yes — kinds `signal_vector` (G001, G002), `signal_operation` (G003), `core` (G004), `reducer` (G006), `evaluate_pair` (G005, G007, G008); kernel cases never call the application path | `GOLDEN_CASE_TABLE`; `test_positive_comparison_matches_all_eight_cases`; `test_membership_type_and_schema_refusals` |
| D-05 | Yes — `--compare-goldens`/`--goldens`/`--report`; exits `0`/`1`/`5` and `0`/`5`; no tool exits `3` | `test_refusal_and_mismatch_exit_codes_never_collide_with_release_not_admitted`; `test_usage_errors_keep_the_parser_exit_and_never_exit_three`; §7.7–§7.8 |

## 6. In-flight decisions

One decision was taken without a rescope. It is non-material (no objective, acceptance criterion, protected boundary, multi-unit scope, dependency or budget item changes), obvious, necessary to deliver the approved scope and consistent with the Epic's objective and controlling constraints.

| ID | What changed | Why it was necessary | What was tested (identity → outcome) |
| --- | --- | --- | --- |
| IF-01 | The comparator tests live in the existing owner module `tests/config/test_config_artifacts.py` (a third section, "HDE-EPIC040-PR05") instead of the new module `tests/config/test_golden_comparison.py` that plan §8.1 and §6.2 named; consequently `_CONFIG_WRITER_TEST_OWNERS` is **not** extended and the fixture owner in `_TEST_SUPPORT_OWNER_PATHS` is `tests/config/test_config_artifacts.py`. The test content of plan §8.1 is unchanged | `tests/evidence/test_rails_ci_workflow_integration.py` — an F01-enumerated file PR05 must not touch (PF10 §2.15; plan §6.5) — pins the exact `_CONFIG_WRITER_TEST_OWNERS` tuples (`test_pr01_config_writers_select_publication_owners_and_lanes`) and requires every module under the configured `pytest.ini` testpaths, which include `tests/config/`, to be a fixed-lane, supplemental or inactive member (`test_full_validation_roster_is_exhaustive_nonoverlapping_and_owned`). A new `tests/config/test_golden_comparison.py` fails both assertions unless that file is edited. Placing the tests in the module that already owns `tools/config/artifacts.py` and `tools/config/generate_config_artifacts.py` satisfies plan §8.1 and §6.2's intent (exact owner coverage) without touching an enumerated file | `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_http_reader_ci_ownership.py tests/qa/test_qa_tool_ownership.py tests/evidence/test_rails_ci_workflow_integration.py` → **310 passed**; `test_classifier_binds_the_fixture_and_tools_to_this_module` → passed (`changed_test_targets(ROOT, [fixture]) == ("tests/config/test_config_artifacts.py",)`); classifier dry-run manifest 90 targets (§7.2), i.e. the 89-target full-validation roster plus the one genuinely new owner module — the plan's "89 → 91" expectation was written for two new modules and becomes 90 under IF-01 |

No other deviation from the plan text exists. Plan step C1.3 says "update the module docstring"; `tools/config/generate_config_artifacts.py` has no module docstring on `main` and none was added — its `--help` text carries the mode description (observation O-09).

## 7. Local validation

All runs under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, `GH_TOKEN` unset in worktrees. Interpreter: Python 3.11.15 (`/usr/local/bin/python`), pytest 8.4.2; CI uses Python 3.12 (limitation L-04). Dependencies installed as `.github/workflows/ci.yml` installs them: `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; `python -m pytest --version` → `pytest 8.4.2` (exit 0); `ci/checks/check_env_pins.sh` → `[env-pins] OK: ALLOW_NETWORK=0,LANG=C,LC_ALL=C,SAFE_MODE=1,TZ=UTC` (exit 0).

### 7.1 Focused behavioural and ownership suites (plan §10.2), on the working tree whose content is the committed tree `c6d2238d…`

| Command | Exit | Result |
| --- | --- | --- |
| `python -m pytest -q -p no:cacheprovider tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_http_reader_ci_ownership.py tests/qa/test_qa_tool_ownership.py tests/evidence/test_rails_ci_workflow_integration.py` | 0 | 310 passed |
| `python -m pytest -q -p no:cacheprovider tests/config tests/core tests/bodygraph/test_gates.py tests/compat/test_evaluate_pair_eligibility.py tests/http/test_reader_post_v1.py tests/bodygraph/test_check_magic10_gate_readiness.py` | 0 | 788 passed in 57.77s |
| `git status --short --untracked-files=all` before the commit | 0 | exactly the nine intended paths; empty after the commit |

### 7.2 Classifier dry-run at the committed head (plan §10.3, as `ci.yml` runs it)

`python ci/checks/classify_ci_changes.py --base 25b2c87baa9298956e4cb62f53b9e2acfa95fc1a --head 96b54dd870c6abe855af55140e13094ef896bbb6 --event-name pull_request --github-output <tmp>/classify.out --changed-tests-output <tmp>/changed_tests.txt` → exit 0; stdout `CI_CHANGE_CLASSIFICATION:event=pull_request;reason=selected_lanes;paths=9;lanes=product,compat,db,rails,evidence,qa,release`; outputs `product=true compat=true db=true rails=true evidence=true qa=true release=true needs_python=true changed_tests=true reason=selected_lanes path_count=9`. Changed-test manifest: **90** targets, including `tests/bodygraph/test_check_magic10_gate_readiness.py` (line 4) and `tests/config/test_config_artifacts.py` (line 28).

### 7.3 Changed-test isolation (plan §10.3; detached worktree at `96b54dd`, `PYTHONPATH` = the worktree)

`python -m pytest -q -p no:cacheprovider -- $(cat changed_tests.txt)` → exit 0, **2394 passed in 184.29s**; `git diff --exit-code` → 0; `git status --short --untracked-files=all` → empty.

### 7.4 Lane-equivalent validation (plan §10.4; each lane's commands exactly as `ci.yml` defines them at the candidate head; `git diff --exit-code` 0 and an empty status after every lane)

| Lane | Commands (as `ci.yml`) | Exit | Result |
| --- | --- | --- | --- |
| product | `python tools/order/generate_ordering_artifacts.py --check`; `pytest -q tests/order tests/mech/test_order_properties.py tests/evidence/test_architecture_snapshot.py` | 0 | 20 passed |
| compat | `ci/checks/check_cli_help.sh`; `serializer_grep_guard.py --output <tmp>`; `emitter_symbol_proof.py --output <tmp>`; its ten-module pytest list | 0 | 101 passed, 3 skipped, 2 xfailed |
| db | `python ci/checks/check_direct_db_contract.py`; its seven-target pytest list | 0 | 249 passed |
| rails | `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml` → **exit 3** after `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED` (job suites 4, 112 and 39 passed; `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED` accepted with `INCOMPLETE_RELEASE_ROSTER` observed; `RAILS_GATE_EVIDENCE_OK`); independent probe → 0; marker `RAILS_LANE:RELEASE_NOT_ADMITTED`; `pytest -q tests/evidence/test_rails_ci_workflow_integration.py` | 0 (lane) | 133 passed; the accepted F01 outcome |
| evidence | `update_evidence_index.py --check`; `orientation_demo.py --check`; `refresh_step_logs_manifest.py --check`; `check_evidence_index_hash.sh`; `validate_evidence_paths.py`; `check_mirror_schema.sh`; `check_final_lf.sh`; its six-module pytest list | 0 | every read-only check exit 0; 111 passed in 562.14s (the duration reflects concurrent local load, not the suite) |
| qa | its seven-module pytest list in a detached worktree at `96b54dd` | 0 | 488 passed in 17.13s; worktree diff 0, status empty |
| release | `git diff --exit-code`; `python scripts/release_id_recompute.py --check-manifest-only` (0); `pytest -q tests/runtime/test_identity.py tests/evidence/test_release_attestation.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py` in a detached worktree (63 passed, worktree clean); then `python tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean` — see the two rows below | — | — |
| release (builder, container interpreter) | as above with `/usr/local/bin/python` (system setuptools 68.1.2, Debian-patched) | 1 | receipt `{"code":"isolated_package_install_failed","returncode":1,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"build_package_wheel"}` — an environment defect, not a PR05 defect: reproduced on a tracked source copy, `pip wheel --no-index --no-deps --no-build-isolation` fails with `AttributeError: install_layout` inside the Debian-patched `setuptools/_distutils` (`/usr/lib/python3/dist-packages`). The stage precedes every admission and source-identity stage, so nothing of PR05 was exercised (limitation L-03, observation O-10) |
| release (builder, fresh venv rehearsal — PR04's method) | `python -m venv <tmp>/venv`; the CI install command in that venv (Python 3.11.15, setuptools 79.0.1, wheel 0.48.0); `<venv>/bin/python tools/evidence/build_release_attestation.py --output <external empty dir> --require-clean` from the clean main tree | 1 | receipt `{"code":"release_not_admitted","returncode":3,"schema":"hde.release_attestation.failure.v1","secret_values_recorded":false,"stage":"closure_write_and_check"}`; independent probe → 0; marker `RELEASE_LANE:RELEASE_NOT_ADMITTED` — **the accepted F01 outcome**; `--verify` skipped as `ci.yml` skips it; tree diff 0 and status empty before and after (13 s) |

### 7.5 Candidate-wide roster (plan §10.5; detached worktree at `96b54dd`)

`python -m pytest -q -p no:cacheprovider --ignore=tests/em` → exit 0, **1985 passed, 3 skipped in 145.56s**; worktree diff 0, status empty. The configured `testpaths` roster contains none of the known pre-existing failures, so none appears here; they are covered by §7.6.

### 7.6 Base-versus-head sweep of the test files no lane, no changed-test target and no `testpaths` root covers (not a plan command; PR04 result §8.8's standing lesson)

129 of the 276 `tests/**/test_*.py` files are reached by neither a `ci.yml` lane command, nor the 90 changed-test targets, nor a `pytest.ini` testpaths root. Each set was run once at the approved base `25b2c87b…` and once at `96b54dd8…`, in throwaway worktrees, with `--continue-on-collection-errors`, and the `FAILED`/`ERROR` node-ID lists were diffed.

| | files | result | failure lines |
| --- | --- | --- | --- |
| base `25b2c87b` | 129 | 57 failed, 546 passed, 13 errors in 114.97s | 70 |
| head `96b54dd8` | 129 | 57 failed, 546 passed, 13 errors in 113.74s | 70 |

`diff` of the two sorted lists: **empty** — zero regressions, zero fixes. The seven node IDs plan §10.5 names are present, unchanged, on both sides: `tests/compat/test_cli_public_bytes_identity.py::test_cli_public_bytes_two_run`; `tests/adapter/test_reader_parity.py::test_get_200_has_etag_and_bytes_and_headers`, `::test_get_304_on_exact_match_empty_body_and_parity_headers`, `::test_head_miss_200_empty_body_and_etag_present_and_compression_invariance`; `tests/reader_v1/test_cli_proof.py::test_cli_stdout_lf_hash_and_admin_sidecar_invariance`; `tests/evidence/test_dev_conjunction_identity.py::test_check_mode_neutralizes_database_url_and_preserves_artifacts` and `::test_dev_conjunction_identity_evidence_is_current_and_nonwriting` (F07, PR07). The 13 collection errors are the pre-existing missing-module errors PR04 recorded (`tests/canon`, `tests/adapters`, `tests/test_*.py`, `tests/unit/test_channel_derivation.py`, `tests/unit/test_enum_closure.py`, …). None is repaired, skipped or hidden. These uncovered tests rewrote 28 tracked artifacts (`artifacts/epic020/bundles/*`, `artifacts/evidence_index.jsonl*`, `artifacts/goldens/public_success.json*`, `artifacts/logs/loader_call.jsonl`, `artifacts/release_id.txt`, `docs/evidence/INDEX*`) and wrote `tmp/` residue **inside the throwaway worktrees only** — identically at base and at head — which is why the sweep ran there; the main tree stayed clean throughout and the worktrees were removed.

### 7.7 Comparator CLI evidence (plan §10.6: report bytes against the synthetic root; refusal against the repository root)

Synthetic complete-release root built with `tests/config/helpers.py::synthetic_complete_release_root` under the scratch directory: 44 manifest members, version `1.1.0`, `built_at_utc` `2026-08-24T18:04:49Z`, `release_id` `486ef2d1961fb57d8801a6d3b2a1edddfa3d0ed92eda8c06acac380f589c92c2` (labeled, non-production; test-only admission, never release admission).

| Invocation (`python tools/config/generate_config_artifacts.py …`) | Exit | stdout | stderr |
| --- | --- | --- | --- |
| `--compare-goldens <synthetic root> --report <external path>` | 0 | 1,212 bytes, SHA-256 `2f8326b1c5ac20da3e60699e29850baa189eeefbfaf2d98e0b4f97513b104a4f`; `--report` file byte-identical, ends with one LF | empty |
| `--compare-goldens <synthetic root>` (second run) | 0 | byte-identical to the first run | empty |
| `--compare-goldens /home/user/glow-hdengine-v2` (the repository root) | 5 | empty | `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` — the truthful F01-interval result, not a golden mismatch |
| `--compare-goldens <synthetic root> --report <synthetic root>/report.json` | 5 | empty | `REPORT_PATH_INVALID` |
| `--goldens x` (without `--compare-goldens`) | 2 | empty | argparse usage error `--goldens and --report apply only to --compare-goldens` |
| `--compare-goldens <synthetic root>` with `SAFE_MODE=0` | 5 | empty | `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]` |

Report content at exit 0: `schema` `magic10_golden_comparison.v1`; `ok` `true`; `candidate_release_id` `486ef2d1…92c2`; `config_id` `m10-channel-state-v1.0.0`; `goldens_sha256` `0fd92a9e…31ac`; `mismatches` `[]`; eight case rows, each `outcome: "match"`: G001 kernel/`signal_vector`, G002 kernel/`signal_vector`, G003 kernel/`signal_operation`, G004 kernel/`core`, G005 application/`evaluate_pair`, G006 kernel/`reducer`, G007 application/`evaluate_pair`, G008 application/`evaluate_pair`. The main tree was clean after every run.

### 7.8 Readiness tool evidence (plan §10.6: fake-DB outcomes; real CLI with `DATABASE_URL` unset)

Real CLI, `DATABASE_URL` unset (`python tools/bodygraph/check_magic10_gate_readiness.py …`): `--user-id 00000000-0000-0000-0000-000000000001` → exit 5, stdout empty, stderr `READINESS_UNAVAILABLE`; no arguments → exit 5, `READINESS_EMPTY_SELECTION`; `--user-id not-a-uuid` → exit 5, `READINESS_SELECTION_INVALID`.

Fake-DB outcomes (`tests/bodygraph/test_check_magic10_gate_readiness.py`, 36 passed in every run above): `test_good_rows_are_ready_with_identity_safe_aggregate_report` (READY report, exit 0, no UUID/payload/DSN in any stream); `test_bad_rows_are_counted_without_a_false_ready` (16-row matrix: `missing`, `duplicate`, `row_invalid`, `payload_invalid`, `gates_invalid` with the exact `MappedCacheError`/`BodyGraphProjectionError` codes, NOT_READY); `test_missing_row_is_not_ready_and_mixed_diagnostics_are_sorted`; `test_duplicate_row_message_is_pinned_against_mapped_cache`; `test_empty_selection_refuses_before_any_query`; `test_invalid_selection_refuses_before_any_query`; `test_selection_file_and_flags_combine_sorted_and_deduplicated_checked`; `test_missing_database_url_is_unavailable_without_a_connection`; `test_retired_bridge_key_is_unavailable_without_a_connection`; `test_connect_failure_is_unavailable`; `test_query_failure_mid_selection_aborts_without_partial_report`; `test_missing_result_set_is_unavailable`; `test_lookup_is_the_parameterized_read_only_current_row_statement`; `test_two_runs_are_byte_identical`; `test_usage_errors_keep_the_parser_exit_and_never_exit_three`; `test_module_imports_only_read_paths_and_is_a_valid_release_member` (import purity; `_parse_release_member_bytes` accepts the file); `test_synthetic_release_copies_the_real_tool_and_still_admits`; `test_classifier_owns_the_readiness_tool_and_fails_closed_for_siblings`. No live row was observed (limitation L-02).

## 8. Code review and security review self-check (plan §11)

| Check | Result |
| --- | --- |
| No arithmetic in the comparator; every value from the canonical entrypoints; only hashing is the PF05 §9.2 idempotence recheck | Verified by reading the runners and by `test_compare_path_is_structurally_unable_to_reach_write_activation_or_generation` (AST guard over `compare_goldens`, the `_golden_*` helpers and the `_GOLDEN_RUNNERS` dispatch: no reference to `write_magic10_config`, `write_band_edges`, `_publish_prepared`, `generate_config_artifacts`, `publish_config_family`, `generate_catalog_logs`, `_ConfigWriteTransaction`, `update_evidence_index`, `_publish_staged`, `cut_release_manifest`, `route_keys`, `get_pack`, `load_pack`) |
| Validation before admission; admission before execution; refusals never `match`; every leaf mismatch reported; deterministic sorted output | `test_membership_type_and_schema_refusals`, `test_noncanonical_or_invalid_bytes_refuse`, `test_symlinked_or_missing_goldens_refuse`, `test_admission_refusals_are_never_equality` (incomplete manifest → `INCOMPLETE_RELEASE_ROSTER`; tampered member → `MANIFEST_MEMBER_HASH_MISMATCH`), `test_each_alteration_yields_exactly_its_mismatches`, `test_several_alterations_are_all_reported_in_sorted_order`, `test_added_or_missing_expected_keys_are_mismatches`, `test_cli_match_report_file_and_determinism` |
| No module-level seam set; no default router; nothing written under the candidate root, the goldens path or the repository | `test_runs_leave_candidate_goldens_repository_and_seams_untouched` (byte snapshots of the candidate root and goldens, `git status` of the repository, `compute._BUNDLE_PROVIDER`/`narrative_state._PACK` unchanged, narrative-mount snapshot unchanged) |
| Readiness read-only; per-outcome mapping; abort on `DB_QUERY_FAILED`/`AdapterError`; closed report keys; no identity in any stream; exits `0`/`5`, never `3` | §7.8 tests; `FORBIDDEN_STRINGS` scan of stdout/stderr for UUIDs, `"gates":`, DSN fragments |
| Classifier registrations exact and fail-closed; new tests are ordinary changed-test targets, not fixed-lane providers | `test_classifier_binds_the_fixture_and_tools_to_this_module`, `test_classifier_owns_the_readiness_tool_and_fails_closed_for_siblings`, §7.1 guard suites (310 passed), §7.2 |
| Fixture holds only synthetic UUIDs and synthetic chart fields; no secrets, birth data or real people | Reading `tests/fixtures/magic10/v1/goldens.json`; `test_fixture_bytes_are_canonical_and_agree_with_pf01` |
| `--report` refuses candidate-root/repository/symlink/missing-parent paths; writes atomic and external | `test_cli_report_path_inside_candidate_or_repository_refuses`, `test_cli_refusals_and_usage`; §7.7 rows 4–5 |
| No network, subprocess, HTTP route, public flag, payload field or transport change in either tool | Reading both modules; import-purity test; `ALLOW_NETWORK=0` throughout |
| Test names canonical, no symlinks, no tracked-artifact writes, no wall-clock values written | `git status` empty after every run; `ci/checks/check_final_lf.sh` in the evidence lane |

## 9. Limitations

- **L-01 No admitted release.** Every governed gate and the attestation end `RELEASE_NOT_ADMITTED` (`INCOMPLETE_RELEASE_ROSTER`, 44-member roster versus the 15-member `catalog/manifest.json`) on this candidate, as PF10 §2.15 defines for the PR04-to-PR06 interval. The comparator's success is proven only against the labeled synthetic fixture root; against the repository root it refuses truthfully.
- **L-02 No live rows.** The readiness tool was exercised only against fake current-view rows and against a missing `DATABASE_URL`. Current production rows are unobserved; a live readiness claim needs separately authorized observation outside PR05.
- **L-03 Attestation builder in this container.** With the container's system interpreter the builder fails at `build_package_wheel` for an environment reason (§7.4). The accepted `release_not_admitted` outcome was reproduced with a fresh venv carrying the CI install; hosted CI (Python 3.12, stock setuptools) is the authoritative run and is unobserved at this phase.
- **L-04 Interpreter.** Local runs used Python 3.11.15; `ci.yml` installs 3.12.
- **L-05 Not QA, acceptance or admission.** Local results are engineering checks under the approved work unit. Hosted CI, Codex review, mergeability and PR-40 acceptance are later phases.

## 10. Observations (non-gating; carried for their owners; plan §13.2 holds O-01–O-08)

| ID | Observation | Owner |
| --- | --- | --- |
| O-09 | `tools/config/generate_config_artifacts.py` has no module docstring on `main`; plan step C1.3's "update the module docstring" had nothing to update, and none was added. `--help` carries the mode description; PR07/DOC-10 owns fuller documentation (plan O-06) | PR07 |
| O-10 | `tools/evidence/build_release_attestation.py` builds the package wheel with `--no-build-isolation` using `sys.executable`'s setuptools; under Debian's patched setuptools 68.1.2 the build fails with `AttributeError: install_layout` before any admission stage. Hosted CI is unaffected (stock setuptools). A local rehearsal needs a venv with the CI install, as PR04 also found | `tools/evidence` owner; not PR05 |
| O-11 | 129 test files are outside every CI lane, every changed-test owner and the `testpaths` roster; 57 fail and 13 error at the approved base for pre-existing reasons, and some of them rewrite tracked evidence artifacts when run in the repository tree (§7.6). Unchanged by PR05 | Repository test-hygiene owner (PR04 O-08 lineage) |
| O-12 | The `pytest.ini` `testpaths` roster (1985 tests) includes `tests/config/` and `tests/db/` but not `tests/bodygraph/` beyond `test_gates.py`; the new readiness suite reaches CI only as a changed-test target and registered owner (plan O-05), which is the intended coverage | None |

## 11. `CANON_CONFLICT_REGISTER`

Carried unchanged from plan §13.1 (C040-01 … C040-06, all `APPROVED`; the PF01 §4.5 versus PF05 §5.2.3 token-naming tension remains plan observation O-01 / PR04 result O-16 with the PF01/PF05 maintainers). PR05 opens no entry, reopens none, relabels none and edits no canon. Source coverage for this statement: the plan's register, the instruction §13 and PF10 v13.3 §2.2–§2.5.

## 12. Publication

| Field | Value |
| --- | --- |
| Implementation push | `git push -u origin claude/beautiful-ritchie-6uvevf` of `96b54dd870c6abe855af55140e13094ef896bbb6` (branch created on the remote); remote head read back `96b54dd870c6abe855af55140e13094ef896bbb6` |
| Pull request | #492 opened from `claude/beautiful-ritchie-6uvevf` into `main`, ready for review (not draft), title "HDE-EPIC040-PR05: full golden comparison and read-only Gate readiness"; body per `.github/pull_request_template.md` headings; read back after creation (open, not draft, not merged, head `96b54dd870c6abe855af55140e13094ef896bbb6`, base `main` `25b2c87baa9298956e4cb62f53b9e2acfa95fc1a`, 1 commit, 9 files (+1,704/−9), `mergeable_state` `unstable` (checks pending), created 2026-09-24T19:20:03Z) |
| Records push | the commit adding this file, the ledger and the PR-30 checkpoint; pushed after the PR existed so the records can name it; its SHA and the remote head after that push are recorded verbatim in the PR #492 body |
| Not done | no merge, no auto-merge, no merge request, no `[skip ci]`, no review request to any reviewer product other than the repository's existing Codex integration, no Notion write, no PF-Canon edit, no governed-evidence write |

## 13. Prompt-use provenance

`GCFPE_PROMPT_USES` (this phase; the PR-20 entry `GCFPE-USE-HDE-EPIC040-PR-20-20260924-PR05-01` stays in plan §16 and is not restated):

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-30-20260924-PR05-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`; `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`; `work_unit_id`: `HDE-EPIC040-PR05`
- `requirements`: `K040-REQ-010`, `K040-REQ-011` principal; portions of `K040-REQ-001`, `-008`, `-012`, `-013`; `AC040-06`, `-07`, `-08`, `-09`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members (register readback recorded in plan §2.4)
- `prompt`: `PR-30 — PR Implementation Proceed — 091426.1`, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`, reported revision `2026-09-24T15:47:45.499Z`
- `role_stage`: dedicated PR05 PR-development session / PR-30 implementation and initial publication; `execution_posture`: `MANUAL_PROMPT_EXECUTION`; `session_disposition`: `RETAIN_EXISTING`; `role_session_ref`: `NOT_YET_ASSIGNED`
- `capture_time`: PR-30 execution from the Proceed intake after `25b2c87b` landed (`2026-09-24T18:37:22Z`) to publication (`2026-09-24T19:20:03Z`); implementation commit `2026-09-24T19:02:46Z`
- `runtime_identity`: `https://claude.ai/code/session_01FTff5iBZhV6crMfp7dkvxh` (from the harness attribution, directly known)
- `result`: `HDE-EPIC040-PR05-PR-IMPLEMENTATION-RESULT v1.0`, state `PR_CANDIDATE_PUBLISHED`; `result_refs`: this path, PR #492, commits `96b54dd8…` and the records commit
- `repository_provenance`: `docs/changes` still holds no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination; repository persistence of this use entry is `PENDING / NON_GATING` for a later authorized writer

## 14. Continuation

PR-30 ends here with `PR_CANDIDATE_PUBLISHED`. PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1 continues the same work unit, original Proceed, workspace, branch, pull request #492, instruction, plan, primary skill authority and lineage in its own dedicated session, without another Proceed: it reads the Codex code and security reviews and the exact-head CI run (all seven lanes; the rails and release lanes are expected to end in the accepted `RELEASE_NOT_ADMITTED` outcomes), resolves findings locally, pushes coherent corrective revisions if any, verifies the current head and returns `MERGE_PENDING — Ready to merge` without merging. Nathan / Product Owner merges manually. `PR-50` is invocable only by Nathan / Product Owner.
