---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-03-PR-IMPLEMENTATION-RESULT
artifact_version: "1.0"
result_state: PR_CANDIDATE_PUBLISHED
phase: PR-30
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; landed at 20f16d0, #639; overlaid by addendum 2.6 for the clauses rescope review v1.0 §7.1 B-2 names)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md (v1.1; landed at 1735d94, #642); companion docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.0-prototype.diff (preserved)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; immutable)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md (v1.0, RS-20, APPROVE; binding conditions B-1 to B-12)
REMEDIATION_REVIEW_ID: none
effective_baseline: approved base (Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0) + PF10 addenda 2.2, 2.3, 2.5 + addendum 2.6 (record docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md; published as §2.6 of PF10 v13.5.7, §10)
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md on main at Proceed (blob 9c5468fb69e4; sha256 8663ab94…; read for addenda 2.2, 2.3 and 2.5; unchanged since ad11821). This pull request replaces it with docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md (sha256 dfb4478c88d712a9205b0d0907c77212eb5de9a86334d9f0235c7d0cb5748123; read in full) on the Product Owner's direction (§10)
pf10_addendum_paths: PF10 §2.2, §2.3, §2.5; §2.6 (v13.5.7) = docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md
proceed: Nathan / Product Owner, by pasting in this session the PR-30 invocation that names exactly plan v1.1 at its repository path, after #642 merged (main 1735d94; 2026-10-14, after 03:05:07Z, the plan's creation). PR-30 resolves that unambiguous reference directly; no other approval object exists or is required
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (PR-20 and PR-30 phases), https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ; role_session_ref NOT_YET_ASSIGNED (Nathan assigns)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08Z; read in full); primary skill glow-hde-pr-development 1.4.0
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2 (cloud container)
repository_baseline: origin/main 1735d9449a02629566b6f4c618d6931f299d2e10 (#642; 150feab plus plan v1.1 under docs/ephemeral/ only)
branch: claude/nifty-cray-w86vmp (restarted from origin/main; §2)
pull_request: amthorn78/glow-hdengine-v2#643 (https://github.com/amthorn78/glow-hdengine-v2/pull/643; open, base main, not draft)
commits: 7811f43 (hand-edited source); 7f6da26 (owner-produced refresh and convergence; the tested code and evidence head); 2d914e9 (PF10 v13.5.7, Product Owner directed); 2d26e2b (merge of the merged-history head f0601ab; tree unchanged); the record commit that adds this file (docs/ephemeral/ only)
canon_conflict_register: CR-1 to CR-6 carried unchanged (CR-6 APPROVED, rescope review v1.0 §12); no new entry
created_at: 2026-10-14T03:41:00Z
next_phase: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e), in its own dedicated session (session_disposition NEW_DEDICATED)
---

# HDE-CRD-0002 WU-PR-03 — PR Implementation Result v1.0 (PR-30)

## 1. Result

**PR_CANDIDATE_PUBLISHED.** Work unit WU-PR-03 is implemented as plan v1.1 §5 to §8 specify:
- S02, S07, S09, S10, S15 and S18;
- ID-3 and ID-4;
- RP-1 and RP-3 of addendum 2.6;
- the same-version release refresh and its convergence.

The candidate was locally validated (§6), committed coherently and published as [amthorn78/glow-hdengine-v2#643](https://github.com/amthorn78/glow-hdengine-v2/pull/643).

The pull request also carries PF10 HDE Build Notes v13.5.7, which replaces v13.5.6 on the Product Owner's explicit direction (§10).

PR-35 owns:
- review retrieval and correction;
- hosted current-head CI;
- merge readiness.

Nothing here is merged. Nothing here claims merge readiness, QA, acceptance or closure.

## 2. Recovery

| Check | Observation |
| :- | :- |
| Open pull requests | none (GitHub listing, state open, before any write) |
| Local root, worktrees, branches | one worktree, `/home/user/glow-hdengine-v2`, on `claude/nifty-cray-w86vmp` at `f0601ab` (the plan v1.1 commit, squash-merged as `1735d94` by #642), clean; no other local branch for WU-PR-03 |
| WU-PR-03 artifacts on `main` | instruction v1.0, plan v1.0 and its prototype diff, rescope request v1.0, rescope review v1.0 with its checkpoint and handoff, addendum record v1.0, plan v1.1; no earlier implementation result, vehicle or code commit |
| `git diff 150feab origin/main` | `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md` only, so every plan §4 code, tool and evidence fact holds; `docs/pfcanon/` unchanged since `ad11821` |
| `git diff f0601ab 1735d94` | empty (the squash merge carries the same tree) |
| Companion diff | `git apply --check` on `1735d94`: succeeds |
| Action | `git checkout -B claude/nifty-cray-w86vmp origin/main`, keeping the designated name. The remote branch still held `f0601ab`. A `--force-with-lease` push over that merged-only history was refused by this session's permission policy, so `f0601ab` was merged instead (`2d26e2b`); the tree did not change (`afd5ccd75a12…` before and after) and the push fast-forwarded |

## 3. Authority, Proceed and lineage

- **Proceed.** Nathan invoked PR-30 for exactly plan v1.1 (front matter). This is the one Proceed for this plan. PR-35 and any recovery continue under it without another Proceed.
- **Immutable base.**
  - Specification v1.1;
  - Implementation Plan v1.1 and its review v1.1;
  - PR instruction v1.0.
- **Overlays.**
  - PF10 addendum 2.2: the WU-PR-03 downstream item and binding requirements (ID-4);
  - addendum 2.3: the reviewer chain without the Codex security review;
  - addendum 2.5: carried LR-O1 to LR-O3;
  - addendum 2.6: RP-1 and RP-3 approved deltas, RP-2 in scope; binding conditions B-1 to B-12 of rescope review v1.0 §7.
- **PF10 read.**
  - `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md`, the controlled PF10 on `main` at Proceed: addendum 2.2 (approved delta, binding requirements, downstream work) re-read; addenda 2.3 and 2.5 as recorded in the plan.
  - `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md`, supplied by the Product Owner during this phase: read in full, and its difference from v13.5.6 compared line by line (§10).
  - Both are recorded as provenance; neither gates the work.

## 4. Implementation (commit `7811f43`)

**Starting point.** The plan's companion diff was applied to `1735d94`; it changed 21 paths. Every hunk was then re-read against plan v1.1 §6:
- `adapter/factory.py` and `adapter/http_reader.py`: §6.1 and PD-1 to PD-4;
- the gate: §6.2 and PD-5;
- the help string: §6.3;
- `VERIFY.sh` and the documents: §6.4, B-3 and B-5;
- catalog rows and validator: §6.5, PD-9 and PD-10;
- S18 texts: §6.6;
- classifier keys: §6.7;
- ID-4 data: §6.8;
- tests: §6.9;
- roster line: B-7.

**Corrections.** Two differences from the plan were corrected; both are recorded as in-flight decisions D-1 and D-2 (§11).

**One plan inconsistency, resolved by §6.1.**
- Plan §7.1's `adapter/http_reader.py` row names `governed_not_found_response`. That is the name of the first design's cross-module helper, which the boundary analyzer rejects (F-13).
- Plan §6.1 and PD-1 instead specify one nested `_governed_error_response` with no module-level function.
- The companion diff follows §6.1, and so does the implementation (OBS-P3-11).

**ID-4.** The baseline rebuild (plan §6.8) was run from the edited adapters:
- `discover_route_registrations(ADAPTER_BOUNDARY_CANONICAL_ADAPTER_LOCI)` was filtered exactly as `_public_route_pass_state` filters.
- Result: 23 records discovered, 23 in the baseline, equal in order. The `pprint.pformat` literal (103,310 characters) appears verbatim in `tools/evidence/generate_hdapi_v2_contract_inventory.py`.
- The record diff is in §8.
- The addendum 2.2 item 1 pins hold: `reader_post`, `reader_method_not_allowed` and `reader_post_not_allowed` are present, and `reader_v1_post` is absent.

**Changed-surface tests before the refresh** (plan §8 step 6):
- `tests/http/test_reader_a7_transport.py` and `tests/cli/test_cli_usage_and_errors.py` with `-k 'help or dev_reader or a7'`: 17 passed;
- `ci/checks/check_cli_help.sh`: exit 0.

**Hand-edited set** (21 paths; `git show --stat 7811f43`: 756 insertions, 108 deletions):
- adapters: `adapter/factory.py`, `adapter/http_reader.py`;
- CLI: `engine/cli/main.py`, `engine/emit_public.py`;
- tools: `tools/evidence/generate_a7_transport_proofs.py`, `tools/evidence/generate_hdapi_v2_contract_inventory.py`, `tools/evidence/update_evidence_index.py`;
- classifier: `ci/checks/classify_ci_changes.py`;
- scripts: `VERIFY.sh`; `dev/reader_harness/__init__.py` and `dev/reader_harness/app.py` (deleted);
- documents: `ARCHITECTURE.md`, `docs/ADAPTER_009.md`, `docs/CLI_commands.md`, `docs/acceptance/reader_a7_crib.md`, `docs/server/reader_v1.md`;
- tests: `tests/cli/test_cli_usage_and_errors.py`, `tests/http/test_endpoint_catalog.py`, `tests/http/test_reader_a7_transport.py`, `tests/runtime/test_emit_public_legacy_helper.py`, `tests/scripts/test_dev_start_reader.py` (new).

## 5. Release refresh and convergence (commit `7f6da26`)

**Setup.**
- Run in the implementation branch's working tree, after the member bytes were final and committed (`7811f43`).
- Python 3.12.3 venv with CI's install (§6).
- Closed rails, with vendor, geocode, database and `GH_TOKEN` variables unset.
- Script: steps 2 and 3 once, then steps 3b to 10 twice. A snapshot of `git diff HEAD` followed each pass.

| Step | Commands (owner) | Result |
| :- | :- | :- |
| 1 | member bytes final: `adapter/http_reader.py`, `engine/cli/main.py` (one final LF each) | committed in `7811f43`; no updater run before the cut |
| 2 | `scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --roster-from-admission`; `scripts/release_id_recompute.py --check-manifest-only`; the cutter with `--check` | all exit 0. Manifest SHA-256 = `release_id` `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f` (equal to plan rehearsal 3 and to rescope review §4.2). Two manifest rows changed: `adapter/http_reader.py`, `engine/cli/main.py` |
| 3 | admission one-liner; `generate_config_artifacts.py --compare-goldens . --report <outside>` | `72fca4c3… 45 1.3.0`; goldens exit 0 both passes |
| 3b | `HDE_WRITE_A7_PROOFS=1 generate_a7_transport_proofs.py`; `--check` | exit 0 both passes |
| 4 | `run_canonical_json_gate.py`; `--check-only` | exit 0 both passes |
| 5 | `update_evidence_index.py`; `--check` | exit 0 both passes |
| 6 | `generate_config_artifacts.py --publish-family`; updater `--check` | exit 0 both passes |
| 7 | A7 write and `--check`; `generate_determinism_gate_proofs.py`; `SAFE_MODE=0 ALLOW_NETWORK=1 generate_open_rails_abba_proof.py` (fixture mode, keys absent); `FROZEN_OPEN_ABBA_SHA256` set to the new `open_rails_abba.json` digest; `generate_conjunction_writer_evidence.py`; `generate_engine_core_evidence.py` | exit 0 both passes. The open-rails digest was `64553c25ada7a04c89dd5c1a2651463a5e907a4b77ccb37bd40ed9a0167135d9` in both passes, replacing `c78740b3…` |
| 8 | updater; `--check`; `orientation_demo.py --check`; `validate_evidence_paths.py`; `check_mirror_schema.sh`; `check_evidence_index_hash.sh`; `check_lf_endings.py`; `check_final_lf.sh`; `refresh_step_logs_manifest.py --check` | exit 0 both passes |
| 9 | `run_sanity_pipeline.py --log-path <outside>`; the canonical run; `run_sanity_pipeline_gate.py`; updater `--check` | exit 0 both passes; `summary:PASS` both passes |
| 10 | `generate_showcompat_artifacts.py --check`; `generate_cli_conformance_artifacts.py --check`; `generate_rails_gate_evidence.py --check`; `generate_env_matrix_snapshot.py --check` | exit 0 both passes (frozen families unchanged) |
| 11 | stale-binding sweep | §8 |

**Byte stability.** Each pass made 32 owner and validator runs, all exiting 0. After pass 1 and after pass 2:
- 61 paths differed from `7811f43`;
- `git diff HEAD` had SHA-256 `55afec8f3eb407fecb233404855aecfa1a5684d61233e3f2782acb7f1381ede1`.

The second pass therefore reproduced the first byte for byte.

**Changed set** (61 paths): `catalog/manifest.json`, the constant file and 59 regenerated evidence files. Those 59 are 29 primaries and 30 path proofs, the set plan §6.10 expected, all from their owners.

| Family | Primaries (each with its `.path_proof.txt`) |
| :- | :- |
| Catalog | `artifacts/audit/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json.sha256`, `docs/ENDPOINTS_CATALOG.json.sha256`; plus `docs/ENDPOINTS_CATALOG.json.path_proof.txt` (the docs path stays a symlink, mode 120000, blob unchanged; F-1) |
| A7 success proofs | `artifacts/proofs/{reader_success_get_head_304.json,success_304.txt,success_encoding_invariance.txt,success_get.txt,success_head.txt}` |
| Config | `artifacts/catalog/{catalog_schema_validation,domain_closure_report}.log` |
| Engine core | `artifacts/core/{abba/ab_ba_parity,json_compare/core_result_json_compare,two_run/identity}.json` (`purity/purity_report.json` byte-stable, F-9) |
| F07 writer | `artifacts/writer/{conjunction_write_readback.log,conjunction_writer_summary.json}` |
| Canonical JSON gate | `audit/gates/canonical_json/{json_canon_compare,json_canonical_check}.log`, `audit/gates/json_gate/canonical/{json_gate_check_log,json_gate_compare_log}.ndjson` |
| Determinism and parity | `audit/gates/determinism/{abba.bytes,open_rails_abba.json,tworun_identity.sha256}`, `audit/gates/parity/reader_cli/{ab,ba,summary}.json` |
| Index and Mirror | `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256` |
| Constant | `FROZEN_OPEN_ABBA_SHA256` in `tools/evidence/generate_open_rails_abba_proof.py` |

**Rewritten byte-identically** (so not in the diff):
- `artifacts/proofs/endpoints_env_gate_proof.log`;
- `artifacts/proofs/success_writers_errors.txt`;
- `artifacts/reader/endpoints_snapshot.json`;
- the canonical sanity log.

## 6. Local validation (plan §10)

**Environment.**
- `/usr/bin/python3.12 -m venv`, CPython 3.12.3, with `pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` (pytest 8.4.2).
- Readiness proof: `python -m pytest --version` printed `pytest 8.4.2`.
- `ruby` 3.3.6 at `/usr/local/bin/ruby`, `bash` at `/usr/bin/bash`, `curl` 8.5.0.
- Rails: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, geocode, database and `GH_TOKEN` variables unset.

**Tested state.** Commit `7f6da26` on base `1735d94`. Each run that can write tracked files used a fresh detached worktree and ended with `git diff --exit-code` and an empty `git status --short --untracked-files=all`. Run window: 2026-10-14, about 03:10Z to 03:36Z.

| # | Check (plan §10 item) | Result |
| :- | :- | :- |
| 1 | Classifier dry run, `--base 1735d94… --head 7f6da26… --event-name pull_request` (item 1) | `reason=selected_lanes`; product, compat, db, rails, evidence, qa and release all `true`; `needs_python`, `changed_tests` true; 82 paths; 164 changed-test targets |
| 2 | Changed-tests step: the 164 targets, as CI runs them (item 2) | **3,483 passed** (343 s); clean tree |
| 3a | Product lane: `generate_ordering_artifacts.py --check` and its four test paths | 77 passed |
| 3b | Compat lane: `check_cli_help.sh`, serializer grep guard, emitter symbol proof and ten test files | 103 passed, 3 skipped, 2 xfailed |
| 3c | DB lane: `check_direct_db_contract.py` and seven test paths | 249 passed |
| 3d | Rails lane: `run_rails_job_definitions.py` over the three job files (`RAILS_JOB_DEFINITIONS_OK`, `RAILS_GATE_EVIDENCE_OK`) and `test_rails_ci_workflow_integration.py` | 138 passed |
| 3e | Evidence lane: updater `--check`, `orientation_demo.py --check`, `refresh_step_logs_manifest.py --check`, `check_evidence_index_hash.sh`, `validate_evidence_paths.py`, `check_mirror_schema.sh`, `check_final_lf.sh` and six test files | all exit 0; 130 passed (444 s) |
| 3f | QA lane: seven test files | 488 passed; clean tree |
| 3g | Release lane: `git diff --exit-code`; `release_id_recompute.py --check-manifest-only`; four test files | 79 passed. Then `build_release_attestation.py --output <external empty dir> --require-clean` and `--verify` both exit 0: `validation_result: PASS`, `release_admission: PR06R_B_FINAL_PASS`, `release_id` and `manifest_sha256` `72fca4c3…`, `source_commit` `7f6da26…`, `source_commit_exact: true`; clean tree |
| 3h | Final audit: `git diff --check`, `git diff --exit-code`, no untracked files | `CI_APPLICABILITY_AND_EXACT_HEAD_OK_LOCAL` (the local equivalent of CI's marker; hosted CI not yet observed) |
| 4 | **B-9 full sweep** (LR-O2 applies): `python -m pytest -q -p no:cacheprovider tests`, with `ruby`, `bash` and `curl` on `PATH` | **4,747 passed, 3 skipped, 2 xfailed, 0 failed** (5 warnings; 866 s); `git diff --exit-code` 0; empty status |
| 5 | `VERIFY.sh` from the repository root with a free `VERIFY_PORT` (item 5) | `APP_ENV=dev`: exit 0, 12 of 12 tokens `_OK` (SERIALIZER_ONE_LF, PREIMAGE, TWO_RUN_IDENTITY, AB_BA, READER_200_STATUS, READER_200_HEADERS, READER_200_ETAG_PRESENT, READER_200_ETAG_MATCH, READER_304_STATUS, READER_304_EMPTY_BODY, READER_HEAD_CL_MATCH, ETAG_INVARIANCE); `APP_ENV` unset: exit 2, standard error `VERIFY_APP_ENV_NOT_DEV: run with APP_ENV=dev (effective: <UNSET>)`, empty standard output; the working tree stayed clean |
| 6 | Informative: the 24 `_HTTP_READER_TEST_OWNERS` files with `APP_ENV` unset (item 6) | 777 passed; no test depends on CI's `APP_ENV=dev`; clean tree |
| 7 | Frozen families' `--check` modes and the evidence validators (item 7) | every run exit 0 in both convergence passes (§5 steps 8 and 10) and again in the evidence lane (3e) |
| 8 | B-1 and B-7 diff checks against `origin/main` (item 8) | `git diff origin/main HEAD -- scripts/dev_start_reader.sh` is empty. `git diff origin/main HEAD -- tools/evidence/update_evidence_index.py` is exactly `-    "artifacts/core/purity/purity_report.json",`. Plan §7.3's expected-unchanged set is unchanged: `adapter/wsgi.py`, `engine/http/compat_handler.py`, `engine/presenter/**`, `engine/config/registry_loader.py`, `tools/evidence/hdapi_v2_boundary_analyzer.py`, `.github/workflows/ci.yml`, `pytest.ini`, `artifacts/vendor/hdapi_v2/**`, `artifacts/architecture/**`, `artifacts/cli/**`, `artifacts/identity/**`, `artifacts/math/**`, `audit/ops/**`, `artifacts/reader/endpoints_snapshot.json`, `.body200.json`, `.code304.txt` and the `docs/ENDPOINTS_CATALOG.json` symlink |
| 9 | On `2d914e9` (the PF10 commit), in a detached worktree | Classifier: same seven lanes and an identical 164-target list (84 paths). `check_agents_md_citations.py` → `AGENTS_MD_CITATIONS_OK`. The six test files that read `docs/pfcanon` (`tests/unit/test_check_agents_md_citations.py` and five under `tests/qa/`): 456 passed. Clean tree |

**Collected counts on the final state** (they match plan §4.3):

| Test file | Tests collected |
| :- | :- |
| `tests/scripts/test_dev_start_reader.py` | 10 |
| `tests/http/test_endpoint_catalog.py` | 201 |
| `tests/http/test_reader_a7_transport.py` | 16 |
| `tests/cli/test_cli_usage_and_errors.py` | 7 |
| `tests/evidence/test_hdapi_v2_contract_inventory.py` | 300 |
| `tests/evidence/test_evidence_index_missing_state.py` | 62 |
| `tests/evidence/test_http_reader_ci_ownership.py` | 4 |
| `tests/evidence/test_rails_ci_workflow_integration.py` | 138 |
| `tests/transport/test_a7_transport_proofs.py` | 26 |
| `tests/runtime/test_emit_public_legacy_helper.py` | 5 |

**Not run here:** hosted CI. It is PR-35's.

## 7. Acceptance (instruction §10; acceptance (2) as overlaid by addendum 2.6)

| Item | Evidence |
| :- | :- |
| (1) S02 unknown paths answer the IF-11 envelope; compat and `api_bp` unchanged | `test_unknown_paths_return_the_governed_not_found_envelope` (180 cases: 3 factories × 5 paths × 6 methods × `APP_ENV` dev/prod; status, exact body, `application/json; charset=utf-8`, `no-store`, no ETag, HEAD empty); `test_unrouted_methods_return_the_governed_405_with_allow` (8; sorted `Allow`); `test_compat_and_production_reader_shaping_is_unchanged` (2); every existing compat, Reader POST v1/v2 and transport test in the sweep |
| (2) S10 `GET /reader` served for `APP_ENV=dev`, refused (403 `ERR_READER_FORBIDDEN`) for unset, empty, `test`, `local`, `prod`, `production`, `live` and arbitrary values; the script with `APP_ENV=dev` serves and with `APP_ENV` unset or empty propagates that state and the runner refuses | `test_dev_reader_is_served_only_for_explicit_dev` (`dev`, ` DEV `, `Dev`); `test_dev_reader_refuses_every_other_environment` (unset, empty, blank, `test`, `local`, `prod`, `production`, `live`, `staging`, `development`, `dev1`; `v` validated first); `tests/scripts/test_dev_start_reader.py` 10 passed, in the changed-tests step and the sweep (dev serves; `<UNSET>` banner and 403; `test`, `local`, `prod` and empty kept and refused; `VERIFY.sh` passes with `dev` and refuses unset, empty and `test` with exit 2); the A7 env-gate proof regenerated byte-identically (`endpoints_env_gate_proof.log`, `APP_ENV=prod`) |
| (3) S07 `hdctl --help` names the `magic10_compat_result.v1` contract; `check_cli_help.sh` exit 0; CLI conformance `--check` exit 0 | `test_top_level_help_names_the_showcompat_stdout_contract`; compat lane; §5 step 10 (frozen family untouched; nonclaim §8) |
| (4) S09 `dev/reader_harness/app.py` gone; `VERIFY.sh` uses the canonical runner; no active file references the harness | Both files deleted. `VERIFY.sh` run §6 item 5. Outside the historical prefixes of instruction §5.4, `docs/pfcanon/` and `docs/ephemeral/`, `git grep reader_harness` finds only two stated exceptions: the two `dev/reader_harness/*` classifier keys of ID-3 (needed to classify the deletion), and `CHANGELOG.md` line 333 (WU-DOC-01) |
| (5) S15 every `(method, path)` has a row under ID-1; the validator accepts the IF-6 model; the catalog equals its mirror; `success_endpoints` unchanged | `test_every_served_pair_has_one_catalog_row_or_a_reasoned_exclusion` (53 served = 23 catalogued + 30 excluded); `test_aux_record_follows_the_pf05_projection`; `test_validator_rejects_aliases_off_the_aux_record_and_alias_collisions`; A7 `--check`; updater `--check`; `cmp docs/ENDPOINTS_CATALOG.json artifacts/audit/ENDPOINTS_CATALOG.json` equal (symlink, F-1); `success_endpoints` `[{"method":"GET","path":"/reader"}]` |
| (6) S18 the documents state `invalid_json`, the emitter's return type and the production mounts | Quoted in §8 |
| (7) Admission `1.3.0`, 45 members, the refreshed `release_id`; every convergence step byte-stable; recompute exit 0; all lanes green | §5; §6 items 1 to 3. All seven lanes pass locally; hosted CI is PR-35's |

## 8. Evidence obligations (plan §12)

**Release.**
- `release_id` `72fca4c341d871dc75a828140ee1494714b322a13656bac93f66164060ea390f`: `1.3.0`, `built_at_utc` `2026-08-24T18:04:49Z`, 45 members.
- It supersedes `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`.
- It is the refresh base for WU-PR-04 and WU-PR-05 (contract E-3).
- The regenerated families and their paths are listed in §5.

**Catalog diff (10 → 23 rows).** The 13 rows of plan §6.5 were appended in plan order; the existing 10 rows keep their bytes and order. All 13 have `a7_eligible: false`.

| Rows | blueprint_module | classification | internal | env_gate | rails_profile | Extra |
| :- | :- | :- | :- | :- | :- | :- |
| `GET`, `HEAD`, `OPTIONS /api/compat/v1` | `engine.http.compat_handler` | `internal_admin` | true | `APP_ENV!=prod` | `internal-admin writer no-store` | |
| `GET /aux/narrative` | `adapter.http_reader` | `public_aux` | false | `not_applicable_public` | `public-read-only; vendor-network-disabled` | `aliases: ["/api/aux/narrative"]` |
| `GET /ops/db/unavailable`; `GET`, `POST /ops/rails/refusal` | `adapter.http_reader` | `ops` | true | `operator-network-only` | `ops diagnostic no-io writer no-store` | |
| `GET /ops/probe/env` | `adapter.http_reader` | `ops` | true | `operator-network-only` | `ops probe no-store` | |
| `POST`, `HEAD`, `OPTIONS /ops/writer/diagnostic` | `adapter.http_reader` | `ops` | true | `operator-network-only` | `ops writer admin-scope no-store` | the POST row carries `route_id: "ops.writer.diagnostic.v1"` |
| `GET /internal/healthz`, `GET /internal/readyz` | `adapter.wsgi` | `ops` | true | `operator-network-only` | `ops-only no-store` | |

Further catalog facts:
- `CLASS` is the HDE Schemas & Artifacts §8.8 closed set plus `public_aux`. Neither `public_aux` nor `aliases` is registered in that canon yet, so no conformance is claimed (R-7).
- The `/reader` rows keep `APP_ENV=dev`.
- `generated_at_utc` stays `2026-08-24T18:04:49Z`.

**ID-1 exclusion table.** 30 pairs, in `tests/http/test_endpoint_catalog.py::_EXCLUDED_PAIRS`, as plan §6.5 lists them:

| Class | Pairs |
| :- | :- |
| (a) governed refusal | 6 `/api/reader` non-POST pairs, and `POST /reader` |
| (b) alias | `GET /api/aux/narrative` |
| (c) framework-implicit | 22 pairs |

**ID-3 registry keys** (`ci/checks/classify_ci_changes.py`, with a two-line HDE-CRD-0002 WU-PR-03 (S09) comment):
- `_WORKFLOW_CONTROL_PATH_LANES`: `"VERIFY.sh"`, `"dev/reader_harness/__init__.py"` and `"dev/reader_harness/app.py"`, each `{"product"}`;
- `_PRODUCT_TEST_OWNER_PATHS["scripts/dev_start_reader.sh"] = ("tests/scripts/test_dev_start_reader.py",)`.

**ID-4 baseline diff** (21 → 23 records):

| Change | Records |
| :- | :- |
| Added | `adapter/factory.py` `errorhandler_decorator` 404 `_governed_not_found` and 405 `_governed_method_not_allowed` |
| Renamed | `adapter/http_reader.py` 404 `_compat_scoped_not_found` → `_governed_not_found`; 405 `_compat_scoped_method_not_allowed` → `_governed_method_not_allowed` |
| Unchanged | every route, registration, `before_request` and `after_request` record |

The generator's outputs, schema, family, refusal codes, flags and write paths are unchanged. It was not run in write mode. `artifacts/vendor/hdapi_v2/**` and `artifacts/architecture/**` are byte-unchanged. `tests/evidence/test_hdapi_v2_contract_inventory.py` passed 300 of 300 with `ruby`. Re-run mechanism: that test owns the three factories (`_PRODUCT_TEST_OWNER_PATHS`, `_HTTP_READER_TEST_OWNERS`), so any later route change re-runs it (addendum 2.2).

**S18 statements as landed.**
- `docs/ADAPTER_009.md` line 174: "`COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 error_v1 envelope built from the `invalid_json` alias (emitted `code`: `ERR_COMPAT_INVALID_JSON`), `no-store`, no ETag."
- `ARCHITECTURE.md` line 9: "Emission: `engine/presenter/emitter.py::emit_public(envelope, *, sort_keys=True) -> bytes`; `emit_compact_json(envelope, *, sort_keys=True) -> tuple[bytes, dict]` is a compatibility alias of `emit_public_with_envelope`".
- `ARCHITECTURE.md` "Emitter/serializer discipline": `engine.presenter.emitter.emit_public(envelope: dict, *, sort_keys: bool = True) -> bytes`.
- `ARCHITECTURE.md` "Routing and mounts":
  - the three factories with their mounts: `adapter/factory.py` (the production app, `Procfile`); `adapter/wsgi.py` (adds the two health routes); `adapter/http_reader.py` (the dev runner);
  - `docs/ENDPOINTS_CATALOG.json` named as the route inventory, with its owner.

**S10 environment matrix result.**
- Served: `dev`, ` DEV `, `Dev`.
- Refused 403 `ERR_READER_FORBIDDEN`: unset, empty, blank, `test`, `local`, `prod`, `production`, `live`, `staging`, `development`, `dev1`. Each refusal has `no-store`, JSON and no ETag; HEAD carries no body.
- `v=2` is still refused 400 `ERR_READER_INVALID_VERSION` before the gate.

**Nonclaim (S07; EC-6).** These still show the earlier `showcompat` help text and stay frozen:
- `artifacts/cli/help/*` (`FROZEN_SHA256` unchanged; `generate_cli_conformance_artifacts.py --check` exit 0);
- `artifacts/audit/cli/help*.txt`;
- `artifacts/audit/cli_help_*.txt`;
- `audit/codex/epic011_r17c/cli/help.txt`.

They are historical captures, not current help.

**RP-3 (B-10).** `tools/evidence/update_evidence_index.py` changed by exactly one deletion: `"artifacts/core/purity/purity_report.json",` left `CURRENT_RELEASE_CAPTURE_PATHS`, so the roster now holds 22 paths.
- **Reason.** The engine-core purity report binds the SHA-256 of 12 engine-core, serializer, mechanics-catalog and schema sources. It does not bind the release, so a same-version refresh leaves it byte-stable. It therefore fails the roster's own criterion.
- **Effect.** The updater's own runs removed the `notes` label from the one row `engine_core_purity_report` (`artifacts/core/purity/purity_report.json`) in the Index and the Mirror. No governed artifact was hand-edited.
- **State after the last updater run:**
  - the purity row has no `notes`;
  - the 27 labelled Mirror rows (the 22 roster paths) all end with `release_id` `72fca4c3…`;
  - the Index holds no `52be4558` and 27 occurrences of the new id;
  - the step-11 sweep has no purity hit.
- **Nonclaims.** The purity report is not a release-bound capture. This change does not modify WU-PR-02's accepted delivery, which stays accepted-final.
- **Decision record:** rescope review v1.0 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md` §4 and §7.2) and addendum 2.6.
- **B-9 counts:** §6 item 4.

**RP-1.**
- `scripts/dev_start_reader.sh` has an empty base-to-head diff (B-1).
- Acceptance (2) was verified as overlaid (§7).
- `VERIFY.sh` refusal run: §6 item 5.
- The two documents state `APP_ENV=dev scripts/dev_start_reader.sh` and that the script never defaults `APP_ENV` (B-5; see D-1).

**Stale-binding sweep (step 11).** `git grep -l` outside `docs/`, `.audit_src/`, `handoff/`, `manifest_pre.sha256` and `manifest_post.sha256`:

| Pattern | Hits | Classification |
| :- | :- | :- |
| `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` (full id) | `README.md` | WU-DOC-01 (F-10) |
| same | `audit/ops/hde-epic040/ops01/attestation.json` and 13 files under `audit/qa/hde-epic040/` (`ac040-04-05-admission-identity`, `ac040-06-golden-comparison`, `d0-discovery`, `open-rails-showcompat-vendor`, `sec-reader-http-live`) | frozen HDE-EPIC040 QA and Ops captures; not edited |
| `52be4558` (prefix) | the files above, and `tests/retired_tests.md` line 54 | A dated (2026-10-13) retirement-ledger row of accepted-final WU-PR-01 reads "release_id 12523fec..., current 52be4558...". It is a descriptive statement, not a binding: no tool reads it as identity. It is outside this unit's bounds (B-12), so it is not edited; OBS-P3-10 |
| `c78740b3` (former open-rails digest) | `audit/ops/hde-epic040/ops01/attestation.json` | frozen HDE-EPIC040 Ops capture |
| purity report | none | B-8 |

## 9. Stale documents, observations and carried items (not in this pull request)

**Stale documents.** This unit makes them stale but may not change them (instruction §9.9; plan §17).

| Document | Owner |
| :- | :- |
| HDE-CLI-API-Vendor-Ref §5.1.7 "Known limits" and §5.1.0's reference (HTML 404 on unknown non-compat paths) | Product Owner (canon doc-delta) |
| HDE-CLI-API-Vendor-Ref §5.6 "Implementation and acceptance state" (catalog lacks the Aux record) | Product Owner (canon doc-delta) |
| HDE Architecture §3.8.1 "Current repository discrepancy"; HDE Math Spec §12 "Dev Reader harness" bullet | Product Owner (canon doc-delta; ID-2) |
| HDE Mechanics Guide §34 "Current repository posture" ("The Reader handler treats missing `APP_ENV` as dev") | Product Owner (canon doc-delta; addendum 2.6) |
| HDE Schemas & Artifacts §8.8 (`public_aux`, `aliases`, the ID-1 population rule) | Product Owner (canon doc-delta; R-7) |
| `docs/contracts/reader_v2_public_bytes.md` line 19 (HTML 404 limitation) | WU-DOC-01 |
| `docs/acceptance/reader_a7_crib.md` line 13 (proof producer and file name) | WU-DOC-01 |
| `README.md` line 13 (superseded `release_id`) | WU-DOC-01 |
| `CHANGELOG.md` line 333 (`dev/reader_harness/app.py`) | WU-DOC-01 |
| `AGENTS.md` and `README.md` start-command wording (OBS-P3-8) | WU-DOC-01 |
| The frozen CLI help captures (§8) | nonclaim only |

**Observations** (owner: the whole-change IA, who routes them):

| ID | Observation | Suggested route |
| :- | :- | :- |
| OBS-P3-1 | `adapter/http_reader.py::create_app`'s `after_request` never fires its `/internal/` ETag strip or diagnostic Content-Length rule (F-5) | WU-PR-05 or the Product Owner |
| OBS-P3-2 | The production factory's compat 405 `Allow` order follows the hash seed (F-4); kept for byte identity | IA |
| OBS-P3-3 | `adapter/wsgi.py`'s 405 has no `Allow` | IA |
| OBS-P3-4 | The `/ops/*` probes and health routes have no code-level environment gate and are mounted by the production app | WU-PR-05 (S19) |
| OBS-P3-5 | A `VERIFY.sh`-only change selects `product` but not the owner test that runs it | WU-PR-06 |
| OBS-P3-6 | Tracked root files `.body200.json`, `.code304.txt` are leftovers of the old `VERIFY.sh` | Product Owner |
| OBS-P3-7 | Step 3b is needed whenever a unit changes the catalog validator | IA, for WU-PR-04, WU-PR-05, WU-PR-08 |
| OBS-P3-8 | `AGENTS.md` and `README.md` should state the start command with `APP_ENV=dev` | WU-DOC-01 |
| OBS-P3-9 | The purity-report roster entry (a WU-PR-02 defect) | resolved here by RP-3; the IA carries the 22-path roster to WU-PR-04, WU-PR-05, WU-PR-08 |
| **OBS-P3-10** (new) | `tests/retired_tests.md` line 54 (WU-PR-01's dated retirement ledger) calls `52be4558…` "current"; after this refresh it is not | IA; WU-DOC-01, or the next owner of that ledger |
| **OBS-P3-11** (new) | Plan v1.1 has two editorial residues: §7.1 names `governed_not_found_response` (the rejected first design) where §6.1/PD-1 govern; §6.4 says "three classifier keys" where two keys contain `reader_harness` | IA (lesson only; no effect on the implementation) |

**Carried items:**
- OBS-W3-1 (Product Owner).
- LR-O1 and LR-O3 applied (§5).
- LR-O2 applied (B-9).
- OBS-17: a qa-lane failure of `tests/qa/test_generate_epic_close_pack.py` on this PR is recorded as OBS-17, never "fixed" here. It passed locally in the sweep.
- O-6: the hosted `ruby` version; PR-35 records it if the job log shows it.
- AQ-1 gates WU-PR-07 only.

## 10. PF10 v13.5.7 (Product Owner-directed canon change; commit `2d914e9`)

- **Direction.** During this phase, Nathan / Product Owner uploaded `PF10-HDE-Build-Notes-v13.5.7.md` and wrote: "I authorize direct commit of this PF10 version in this PR and removal of the old vertsion". That is an explicit direction for this particular file (`AGENTS.md`, "PF canon is read-only unless the prompt explicitly directs a change").
- **Change made, and only that change.**
  - `git rm docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md`;
  - `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md` added byte-for-byte as supplied: 85,836 bytes; SHA-256 `dfb4478c88d712a9205b0d0907c77212eb5de9a86334d9f0235c7d0cb5748123`; no final LF, like v13.5.6; no CR.
  - Git records it as a rename: 160 insertions, 2 deletions.
- **Content against v13.5.6:**
  - the version line (`v13.5.6` → `v13.5.7`);
  - the index, which adds the line for 2.6 (the 2.5 line gains two trailing spaces);
  - appended addendum 2.6, "HDE-CRD-0002 WU-PR-03: the dev Reader start helper keeps propagating APP_ENV exactly, as canon requires, and the engine-core purity report leaves the current-release label roster".
- **Addendum 2.6 against its record.** It matches the record `docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md` in substance, item by item. Its delta is the one this unit implements, so nothing in the implementation changes.
- **No other path references the removed filename.** The only other PF10 mentions are:
  - a fixture name `v13.4.1` in `tests/unit/test_check_agents_md_citations.py`;
  - `v13.2.6` in `docs/graph/parts/global.json`;
  - two historical HDE-CRD-0001 QA logs.
- **CI effect.** `docs/pfcanon/` is a CI-exempt prefix (§6 item 9).
- **Currentness.** Until the merge, the controlled PF10 on `main` remains v13.5.6. After the merge, v13.5.7 is current.

## 11. In-flight decisions

| ID | What changed | Why it was necessary | Tested by (outcome) |
| :- | :- | :- | :- |
| D-1 | `docs/server/reader_v1.md` line 19: the companion diff's sentence "`VERIFY.sh` starts the same runner with its own `APP_ENV` (default `dev`)" became "`VERIFY.sh` starts the same runner and requires `APP_ENV=dev`: it never defaults `APP_ENV` and refuses with `VERIFY_APP_ENV_NOT_DEV` (exit 2) otherwise." | The diff's sentence contradicts B-3 and plan §6.4; the plan governs where the diff differs (plan §4.4). Documentation only | `VERIFY.sh` runs (§6 item 5: exit 0 with `dev`; exit 2 unset); `tests/scripts/test_dev_start_reader.py` 10 passed; text read against B-3 and B-5 |
| D-2 | `tests/http/test_endpoint_catalog.py`: `copy` and `pytest` imported once at module top, replacing the diff's function-local imports and a mid-module `import pytest as _pytest` | Module-level imports in the file's usual idiom, for reviewability; no assertion, case or name changes | the file collected 201 tests and passed in the changed-tests step (3,483 passed) and the full sweep (4,747 passed) |
| D-3 | The branch's stale remote head `f0601ab` (already squash-merged) was merged (`2d26e2b`) instead of being force-replaced | A `--force-with-lease` push over merged-only history was refused by this session's permission policy. A merge keeps the history and changes no content | tree `afd5ccd75a12…` identical before and after; push fast-forwarded |

## 12. PR_REMOTE_ACTION_LEDGER

| Time (UTC, 2026-10-14) | Action | Evidence |
| :- | :- | :- |
| before any write | Open-PR listing | none |
| after the local runs of §6 | push of `claude/nifty-cray-w86vmp` | first attempt rejected as non-fast-forward (remote `f0601ab`); `--force-with-lease` refused by the session's permission policy; after the merge `2d26e2b`, push `f0601ab..2d26e2b` succeeded; `git ls-remote` → `2d26e2baaa8ee88a6dd7c2868cf36cf31437e3b7` |
| 03:38:50 | Created #643 (base `main`, head `claude/nifty-cray-w86vmp` at `2d26e2b`, not draft) | https://github.com/amthorn78/glow-hdengine-v2/pull/643; read back at 03:42: open, 83 files, 5 commits, `mergeable_state: unstable` (checks pending), 1 comment present (not read by PR-30; review retrieval is PR-35's) |
| after this record is written | record commit and push (docs/ephemeral/ only) | the read-back below; the pushed head is recorded in the session's final reply and is verified by PR-35 at entry |
| — | Reviews read | none yet (PR-35) |
| — | Hosted CI | not observed (PR-35). The PR opened at `2d26e2b`; the record push supersedes that head, and CI's pull-request concurrency cancels a superseded run |
| — | Mergeability | not yet read (PR-35) |
| — | Remaining useful local action | none for PR-30 |
| — | Next evidence action | PR-35: subscribe to #643, read the Codex code review and the CI on the current head |

## 13. Constraints, unresolved items and owners

| Item | Owner | State |
| :- | :- | :- |
| Codex code review findings on #643 (addendum 2.3: no Codex security review) | PR-35 | pending |
| Hosted CI on the current head: all seven lanes, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; OBS-17 and O-6 if they occur | PR-35 | pending |
| Mergeability and readiness (`MERGE_PENDING`) | PR-35 | pending |
| Restart rules for any correction | PR-35 | a member change re-runs plan §6.10 from step 2; an evidence-primary change from step 3b; steps 3b to 10 must be byte-stable on a second run |
| Merge | Nathan only | — |
| Lineage review | the whole-change IA (PR-40) | after the merge |
| OBS-P3-1 to OBS-P3-11, the doc-delta candidates and WU-DOC-01 items | §9 owners | recorded |
| Persistence of prompt-use provenance | Product Owner (installed writer `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent) | pending, non-gating |

Constraints preserved throughout:
- closed rails;
- no live vendor, production or database call;
- no hand edit of a governed artifact;
- no skipped, disabled, `xfail` or quarantined test;
- no canon edit other than the Product Owner-directed PF10 file;
- no route added or removed;
- no admission-constant change.

## 14. Canon-conflict register

`CANON_CONFLICT_REGISTER`, carried unchanged:

| ID | Status | Decision owner | Record |
| :- | :- | :- | :- |
| CR-1, CR-2, CR-3 | APPROVED_AS_CHANGED | Thoth | Specification v1.1 lineage |
| CR-4 | APPROVED | Product Owner | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-po-disposition-cr-4-cr-5-v1.0.md` §2 |
| CR-5 | APPROVED_AS_CHANGED | Product Owner | same record §3 |
| CR-6 | APPROVED (alternative (a), canon governs) | the whole-change IA through RS-20 | rescope review v1.0 §12; addendum 2.6 |

No new conflict was found during implementation.

## 15. TypeSafe reading and surface advice for the receiving session (PR-35, WU-PR-03)

**Action sent (v6):** "Resolve, in a new dedicated session that continues one open pull request, the automated code review of one work unit of an approved change and bring it to merge readiness: the pull request is new and not yet reviewed, with twenty-one hand-edited files (governed not-found handlers on two web app factories, an explicit-dev route gate, a CLI help string, a retired dev harness and its verify script, an endpoint catalog grown from 10 to 23 rows with its validator and route-enumeration test, a CI classifier registration with one new owner test, a data-only contract-inventory baseline and one evidence-updater line) plus sixty-one owner-regenerated evidence files from a same-version release manifest refresh, all already locally tested with a full test sweep; retrieve the review, fix each in-scope finding locally, re-run the dozen-step governed-evidence convergence from its restart point if a release member or evidence primary changes, push coherent corrections, and verify all seven CI lanes and mergeability on the current head without merging. No live vendor, production or database run; an independent lineage review follows the Product Owner's manual merge."

**The reading, as the skill printed it:**
- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.66 (confidence 0.65).
- Rung probabilities: low 0.00, medium 0.02, high 0.40, extra high 0.49, max 0.09, ultracode 0.00.
- Model probabilities: Fable 5.1 0.18, Opus 5.5 0.82 (confidence 0.64).
- Twelve cells, computed from the two answers:
  - Opus 5.5 at low 0.00, Opus 5.5 at medium 0.02, Opus 5.5 at high 0.33, Opus 5.5 at extra high 0.40, Opus 5.5 at max 0.07, Opus 5.5 at ultracode 0.00;
  - Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.07, Fable 5.1 at extra high 0.09, Fable 5.1 at max 0.02, Fable 5.1 at ultracode 0.00.
- Flags: boundary between high and extra high.
- Sent 2026-10-14T03:18:21Z. Nathan picks the cell.

**Detail:**
- v6 sent 2026-10-14T03:18:21Z; HTTP 200 in 0.63 s; 4345 input and 54 output tokens; jev-1.13.0.
- Rung by rule: extra high (nearest to the score, halves up).
- Model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).
- Flags: boundary between high and extra high.

**Records:**
- Notion row: not written, as PR-30 directs.
- Nathan's pick for PR-35: not stated.
- Nathan's pick for this PR-30 session: not stated (the reading for PR-30 is in plan v1.1 §20).

**Surface advice for PR-35:**
- **Session.** Run PR-35 as a new top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access for the prompt and GitHub access to #643. At entry it subscribes to the pull request's activity.
- **Environment, if a correction needs local re-runs.**
  - Python 3.12 with CI's install (package-index access);
  - `ruby` on `PATH` for the contract-inventory test;
  - `bash` and `curl` for the runner propagation test and `VERIFY.sh`.
  - All were present in this session's cloud container.
- **Run times observed in this phase:**
  - the full sweep, about 15 minutes;
  - the changed-tests step, about 6;
  - the evidence lane, about 7;
  - the two-pass convergence, about 4 (258 s of step time);
  - the release lane, about 2 (97 s, including the attestation build and verify).
- **Discipline.** Run the convergence in the branch's working tree only after member edits are final. Run every other check that can write tracked files in a detached worktree.
- **Access.** No live vendor, production or database access is needed.
- **Order.** Nathan merges nothing before PR-35 reports readiness.

## 16. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / WU-PR-03 / PR-30 / result 1, version 1.0 |
| change / specification | CRD HDE-CRD-0002 / `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` v1.1 |
| work unit | WU-PR-03 (S02, S07, S09, S10, S15, S18) |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (page state as of 2026-10-12T02:30:08Z). Receiver contract read: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e (page state as of 2026-10-12T02:30:15Z) |
| role/stage | dedicated WU-PR-03 PR engineering session / PR-30 |
| capture time | 2026-10-14T03:41:00Z |
| execution identity | https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ |
| inherited usage | PR-10 instruction 1 (instruction §20); PR-20 plan v1.0, request v1.0 and plan v1.1 (their own entries); RS-20 rescope review 1 (review §15) |
| pull request and commits | #643; `7811f43`, `7f6da26`, `2d914e9`, `2d26e2b`, and this record's commit |
| repository persistence | recorded here only (`docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent; pending, non-gating; owner the Product Owner) |

## 17. Next phase

PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e).
- **Session.** Its own new dedicated session (`session_disposition: NEW_DEDICATED`), entered from this phase's handoff, which Nathan pastes.
- **Continuity.** It continues #643 under the original Proceed. It shares this phase's work unit, workspace, branch, pull request, instruction, plan v1.1, primary skill and recovery lineage.
- **Inputs:**
  - this record;
  - plan v1.1;
  - instruction v1.0;
  - rescope review v1.0;
  - addendum record 2.6;
  - the immutable Specification v1.1, Implementation Plan v1.1 and review v1.1 named in the front matter;
  - PF10 as resolved at entry.
- **Branch and head.** PR-35 verifies both at entry from #643.

## Canon relied on

Canon was read on `main` at `1735d94`; `docs/pfcanon/` is unchanged since `ad11821`. This branch's PF10 v13.5.7 is the Product Owner's directed change (§10), read in full.

| Topic | Sources and sections |
| :- | :- |
| Phase authority, Proceed, results and handoff | PR-30 — PR Implementation Proceed — 100926.1 (read in full); PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (receiver contract, read in full); skill `glow-hde-pr-development` 1.4.0; HDE Governance (`docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md`) §9.1.1 and §9.1.2, as cited by plan v1.1 |
| Overlays | PF10-HDE-Build-Notes v13.5.6 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.6.md`) addendum 2.2 (approved delta, binding requirements, downstream work; re-read), 2.3 and 2.5 (as carried by plan v1.1); addendum record 2.6 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-PF10-build-notes-addendum-v1.0.md`, read in full); PF10-HDE-Build-Notes v13.5.7 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md`, read in full; §2.6) |
| Approved rescope | rescope review v1.0 (`docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md`, read in full; §7 B-1 to B-12) |
| Subject matter (S02, S07, S09, S10, S15, S18, ID-1 to ID-4, RP-1) | as read and recorded by plan v1.1 "Canon relied on": HDE-CLI-API-Vendor-Ref (`docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`) §5.1.0, §5.1.7, §5.2, §5.4, §5.5, §5.6, §5.10; HDE Schemas & Artifacts (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`) §8.8; HDE Architecture (`docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.6.md`) §3.8.1; HDE Mechanics Guide (`docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`) §5.6 and §34; Glow Infrastructure (`docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.3.md`) §8.1; HDE Build Checklist — Conjunction (`docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md`) HDE-CONJ001.4; Glow QA Guide (`docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`) §13.9; HDE Math Spec (`docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.8.md`) §12. The canon search at this phase's start (`git grep` on `origin/main -- docs/pfcanon/` for the unit's terms) found the same sources and no change since the plan read them |
| In-flight documents | Specification v1.1; Implementation Plan v1.1 §7 and §10; review v1.1; PR instruction v1.0 (read in full); plan v1.1 (read in full) |
| Operative documentation | `AGENTS.md`: canon-first rule; PF canon read-only unless directed (applied in §10); closed rails; pytest readiness; sole Index/Mirror writer; no hand edits; endpoint catalog source of truth; PR descriptions; evidence attribution |

Read-back: this file is read back completely after commit and push, and its body, identity, path, version, state and next consumer are confirmed. The read-back is recorded in the session's final reply.
