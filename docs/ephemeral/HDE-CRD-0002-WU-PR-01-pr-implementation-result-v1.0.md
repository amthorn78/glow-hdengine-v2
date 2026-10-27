---
artifact_type: PR_IMPLEMENTATION_RESULT
artifact_id: HDE-CRD-0002-WU-PR-01-PR-IMPLEMENTATION-RESULT
PR_IMPLEMENTATION_RESULT_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-result-v1.0.md
artifact_version: "1.0"
result: PR_CANDIDATE_PUBLISHED
phase: PR-30 (initial publication); this record is also the PR-30 publication checkpoint
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
work_unit_title: CI coverage of every test file (PR; Distillation; S03, S04, S05)
PR_INSTRUCTION_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md (v1.0, INSTRUCTION_READY; blob 24597a31fbb910a4d36106a1aa2d5b861faec976)
PR_IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md (v1.1; blob dbb9a56a91dc10eefd32a8cdf66abf20535564a4; landed on main at e3a5ed4, amthorn78/glow-hdengine-v2#626)
IMPLEMENTATION_PLAN_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4)
PLAN_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b)
SPECIFICATION_ID: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
RESCOPE_REVIEW_ID: docs/ephemeral/HDE-CRD-0002-WU-PR-01-rescope-review-v1.0.md (RS-20, APPROVE; blob eccab2187769262ecb4c99374cc9e73674dd37e6)
REMEDIATION_REVIEW_ID: none
immutable_approved_base: Specification v1.1 → Implementation Plan v1.1 + review v1.1 → PR instruction v1.0
effective_scope: approved base + PF10 addendum 2.2, as planned by PR_IMPLEMENTATION_PLAN_ID v1.1
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; read in full in this session; unchanged on main e3a5ed4)
pf10_addendum_paths: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md § 2.2 (controlled PF10); record docs/ephemeral/HDE-CRD-0002-WU-PR-01-PF10-build-notes-addendum-v1.0.md
proceed: Nathan / Product Owner's invocation of PR-30 — PR Implementation Proceed — 100926.1 for exactly PR_IMPLEMENTATION_PLAN_ID v1.1 with PR_INSTRUCTION_ID, pasted into this session on 2026-10-13 after #626 landed (e3a5ed4, 2026-10-13T00:17:17Z). It is the one Proceed for this plan
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session: dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (PR-20 and PR-30 phases), https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8; session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED (assignment owner Nathan / Product Owner)
prompt: PR-30 — PR Implementation Proceed — 100926.1 (https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14; page state as of 2026-10-12T02:30:08Z; read in full)
primary_skill: glow-hde-pr-development (revision 1.4.0)
repository: amthorn78/glow-hdengine-v2; authorized local root /home/user/glow-hdengine-v2
base: main e3a5ed4b9820964c581825f1cc9537fec133988d (git diff 9c767d2..e3a5ed4 outside docs/ephemeral/ is empty, so plan v1.1's tested baseline holds)
vehicle: branch claude/elegant-mayer-y6ppap; pull request amthorn78/glow-hdengine-v2#627 (open, ready for review, base main)
implementation_commit: 26140fee1a7c169694bf4d46bc436bd5495fde91 (tree 40e27cd063a4b1540e1c4cb959d430bf3bc09ded, the exact tree every local check ran on)
result_commit: the commit that adds this file, on the same branch and pull request (its own identity is not written into itself)
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); no new entry
next_prompt: PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1 (https://app.notion.com/p/3f44590a05eb811ebf72e949b7b1572e), in PR-35's own dedicated session (session_disposition NEW_DEDICATED)
---

# HDE-CRD-0002 WU-PR-01 — PR implementation result v1.0 (PR-30)

## 1. Result

**`PR_CANDIDATE_PUBLISHED`.** WU-PR-01 is implemented exactly as plan v1.1 states. It was tested locally on the exact committed tree and published as amthorn78/glow-hdengine-v2#627, with implementation commit `26140fe`.

PR-30 ends here. It does not own review correction, current-head CI readiness, mergeability or merge. Those belong to PR-35, in its own dedicated session (§12).

What this result does not do:
- It claims no merge readiness, CI result, review verdict, QA verdict, acceptance, PF09 movement or closure.
- It requests no second Proceed and creates no other work vehicle.

## 2. Continuity (GCF-17, nine fields)

| Field | Value |
| :- | :- |
| `WORK_UNIT_ID` | `WU-PR-01` |
| Original Product Owner Proceed | Nathan's PR-30 invocation for plan v1.1 (front matter `proceed`) |
| Workspace/worktree | `/home/user/glow-hdengine-v2` (the repository checkout). Validation used temporary detached worktrees of the same repository in the session scratchpad; all were removed after validation |
| Branch | `claude/elegant-mayer-y6ppap`, restarted from `main` `e3a5ed4` after #626 merged. The earlier remote branch of that name no longer existed when PR-30 started |
| Pull request | amthorn78/glow-hdengine-v2#627 |
| PR instruction | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md` |
| Detailed PR plan | `docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md` |
| Primary skill authority | `glow-hde-pr-development` 1.4.0 |
| Recovery/artifact lineage | instruction v1.0 → plan v1.0 → rescope request v1.0 → RS-20 review v1.0 + PF10 addendum 2.2 → plan v1.1 → this result v1.0 |

## 3. Recovery performed before creating anything

Checked on 2026-10-13, before any write:
- **Local repository.** One root, `/home/user/glow-hdengine-v2`, one worktree, no uncommitted change.
- **Branch.** `claude/elegant-mayer-y6ppap` held only plan v1.1 history, already merged by #626. The remote branch of that name no longer existed.
- **Other remote branches.** `claude/wizardly-edison-x05uwc` (the RS-20 IA branch, merged as #625), `codex/exclude-markdown-code-review` and `docs/20261012-crd0002-specification` carry no WU-PR-01 implementation.
- **Open pull requests:** none.
- **`docs/ephemeral/`:** no WU-PR-01 result, checkpoint or implementation record existed.
- **Ledger absence.** `tests/retired_tests.md` was absent on `main`.

No earlier PR-30 state existed, so there was nothing to resume. The reusable work was this session's own integrated scratch prototype (plan v1.1 §4.3), which had never been pushed. Its change set was applied to the branch, then re-verified in full against the base (§5–§6). The ledger was regenerated verbatim from plan §7 with the PR-30 date.

## 4. Implemented change (plan v1.1 §8, applied unchanged)

The implementation commit `26140fe` changes 100 files: 33 modified, 66 deleted, 1 added; 1,953 insertions and 6,387 deletions. These are the only non-test paths changed:

| Path | Change |
| :- | :- |
| `.github/workflows/ci.yml` | ordered `paths` filter for `pull_request` and `push` (plan §5.3) |
| `ci/checks/classify_ci_changes.py` | S04 suffix rule; supplemental 40 → 109; owner additions; the two B-6 keys; analyzer out of `_EVIDENCE_HELPERS_REQUIRING_OWNER`; inactive set empty |
| `pytest.ini` | 68 `testpaths` entries |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` | baseline data only (plan §5.8.1) |
| `tools/evidence/hdapi_v2_boundary_analyzer.py` | `_adapter_routes_without_presenter` only (plan §5.8.2) |

Tests:
- 27 retained files fixed (test code only), including `tests/evidence/test_hdapi_v2_contract_inventory.py` (plan §5.8.3, §5.8.4);
- `tests/evidence/test_rails_ci_workflow_integration.py` pins and new tests (plan §5.5);
- 66 files deleted;
- `tests/retired_tests.md` added: 66 rows, dated 2026-10-13, reasons verbatim from plan §7.

Unchanged, by `git diff e3a5ed4 26140fe`:
- every release member, so `catalog/manifest.json`, `engine/config/registry_loader.py` and `release_id` are unchanged;
- `engine/charts/loader.py`, `engine/provider/fixtures.py` and `artifacts/logs/loader_call.jsonl`;
- `artifacts/vendor/hdapi_v2/`, `docs/evidence/`, `artifacts/evidence_index.jsonl` and its `.sha256`, `artifacts/architecture/` and `audit/`;
- every other `tools/**` and `scripts/**` file, `ci/jobs/*.yml` and `ci/checks/run_rails_job_definitions.py`.

## 5. Inventory and dispositions

**Inventory** (instruction §5.1 definition):

| | Before (`e3a5ed4`) | After (`26140fe`) |
| :- | -: | -: |
| Tracked `tests/**/test_*.py` | 278 | 212 |
| Reached by a `ci.yml` lane token | 49 | 49 |
| Registered owner test paths | 135 | 204 |
| Full-validation targets | 94 | 163 |
| **Uncovered** | **135** | **0** |
| O-11 | 130 | 0 |
| Inactive | 5 | 0 |

**Dispositions applied:** 42 retained as is, 27 retained and fixed, 66 retired, 0 routed. Each row is exactly as plan v1.1 §7 states it. The 66 deleted paths equal the ledger's 66 path cells.

| # | Path | Disposition applied (plan v1.1 §7) |
| -: | :- | :- |
| 1 | `tests/adapter/test_cache_keys.py` | retire (b) |
| 2 | `tests/adapter/test_compat_writer_transport.py` | retain |
| 3 | `tests/adapter/test_env_guard_forbidden_matrix.py` | retain + fix |
| 4 | `tests/adapter/test_env_guard_import.py` | retain |
| 5 | `tests/adapter/test_env_guard_import_purity.py` | retain + fix |
| 6 | `tests/adapter/test_env_guard_prod_variants.py` | retain |
| 7 | `tests/adapter/test_env_guard_silence_and_idempotence.py` | retain |
| 8 | `tests/adapter/test_etag_core.py` | retire (b) |
| 9 | `tests/adapter/test_gate_auth.py` | retain |
| 10 | `tests/adapter/test_headers_and_determinism.py` | retain + fix |
| 11 | `tests/adapter/test_no_etag_on_writers_and_errors.py` | retire (b) |
| 12 | `tests/adapter/test_reader_parity.py` | retire (e) |
| 13 | `tests/adapter/test_readyz.py` | retire (b) |
| 14 | `tests/adapters/test_safe_mode.py` | retire (a) |
| 15 | `tests/arch/test_arch_capture_exists.py` | retire (c) |
| 16 | `tests/arch/test_arch_guards.py` | retain + fix |
| 17 | `tests/artifacts/test_cli_text_artifacts_bom_lf.py` | retire (b) |
| 18 | `tests/audit/test_acceptance_map_epic017.py` | retire (c) |
| 19 | `tests/audit/test_acceptance_map_epic019.py` | retire (c) |
| 20 | `tests/audit/test_acceptance_maps_index.py` | retire (c) |
| 21 | `tests/audit/test_epic017_close_report.py` | retire (c) |
| 22 | `tests/audit/test_epic017_docdeltas.py` | retire (c) |
| 23 | `tests/audit/test_epic017_manifest.py` | retire (c) |
| 24 | `tests/audit/test_epic020_acceptance_bundle_wiring.py` | retire (c) |
| 25 | `tests/bodygraph/test_bg_resolve_route_policy.py` | retain |
| 26 | `tests/bodygraph/test_resolver_vendor.py` | retain |
| 27 | `tests/canon/test_center_order_and_counts.py` | retire (a) |
| 28 | `tests/canon/test_checksums.py` | retire (a) |
| 29 | `tests/canon/test_error_envelope.py` | retire (a) |
| 30 | `tests/canon/test_loader_integrity.py` | retire (a) |
| 31 | `tests/canon/test_overrides_prod.py` | retire (a) |
| 32 | `tests/canon/test_report_determinism.py` | retire (a) |
| 33 | `tests/cli/test_cli_env_pins_epic021.py` | retire (c) |
| 34 | `tests/compat/test_cli_public_bytes_identity.py` | retire (a) |
| 35 | `tests/compat/test_thresholds_constants_pack.py` | retain |
| 36 | `tests/compat/test_ts_import_no_io.py` | retain |
| 37 | `tests/compat/test_ts_sidecar_checks_manual.py` | retire (d) |
| 38 | `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py` | retire (a) |
| 39 | `tests/compliance/test_cli_admin_gate_sidecar_perms_and_stdout_hash_invariance.py` | retain + fix |
| 40 | `tests/compliance/test_cli_release_id_resolver_precedence.py` | retire (a) |
| 41 | `tests/compliance/test_invocation_tag_accept_reject_and_roundtrip.py` | retain |
| 42 | `tests/compliance/test_log_shape_snapshot.py` | retain |
| 43 | `tests/compliance/test_meta_abba_parity.py` | retire (d) |
| 44 | `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py` | retire (a) |
| 45 | `tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py` | retire (b) |
| 46 | `tests/compliance/test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py` | retire (a) |
| 47 | `tests/compliance/test_reader_etag_and_conditional.py` | retain + fix |
| 48 | `tests/compliance/test_reader_etag_compression_invariance.py` | retain + fix |
| 49 | `tests/compliance/test_release_id_precedence_and_grep_guard.py` | retain + fix |
| 50 | `tests/config/test_config_acceptance_map.py` | retire (c) |
| 51 | `tests/em/test_em_defaults_and_ladder.py` | retire (a) |
| 52 | `tests/em/test_em_off_toggle.py` | retire (d) |
| 53 | `tests/em/test_em_throat_and_adjacency.py` | retire (a) |
| 54 | `tests/em/test_goldens_public_shape_and_identity.py` | retire (c) |
| 55 | `tests/epic003/test_error_message_map.py` | retain |
| 56 | `tests/epic003/test_http_home_single_path.py` | retain |
| 57 | `tests/epic003/test_legacy_imports_denied.py` | retain + fix |
| 58 | `tests/evidence/test_aux_preview_identity_parity.py` | retain |
| 59 | `tests/evidence/test_cli_conformance_artifacts.py` | retain |
| 60 | `tests/evidence/test_db_runtime_posture.py` | retain + fix |
| 61 | `tests/evidence/test_env_matrix_snapshot_v3.py` | retain |
| 62 | `tests/evidence/test_epic018_manifest.py` | retire (c) |
| 63 | `tests/evidence/test_epic020_bundle_index_integration.py` | retire (c) |
| 64 | `tests/evidence/test_epic030_pr01_pr03_fail_closed_evidence.py` | retain + fix |
| 65 | `tests/evidence/test_epic030_pr04_band_thresholds_evidence.py` | retain + fix |
| 66 | `tests/evidence/test_evidence_index_env.py` | retain |
| 67 | `tests/evidence/test_evidence_index_snapshot.py` | retain + fix |
| 68 | `tests/evidence/test_evidence_index_token_sets.py` | retain |
| 69 | `tests/evidence/test_hdapi_v2_contract_inventory.py` | retain + fix |
| 70 | `tests/evidence/test_hdapi_v2_live_conformance.py` | retire (c) |
| 71 | `tests/evidence/test_hdapi_v2_response_normalization.py` | retire (c) |
| 72 | `tests/evidence/test_hde_epic035_pr03_evidence_loop.py` | retire (c) |
| 73 | `tests/evidence/test_hde_epic036_pr02_evidence_loop.py` | retire (c) |
| 74 | `tests/evidence/test_hde_epic037_bg_resolve.py` | retire (c) |
| 75 | `tests/evidence/test_hde_epic037_field_sufficiency.py` | retire (c) |
| 76 | `tests/evidence/test_hde_epic037_pr05_parent_binding.py` | retire (c) |
| 77 | `tests/evidence/test_hde_epic037_v2_to_compat.py` | retire (e) |
| 78 | `tests/evidence/test_identity_provenance.py` | retain |
| 79 | `tests/evidence/test_internal_version_manifest_captures.py` | retain |
| 80 | `tests/evidence/test_presenter_evidence_ownership.py` | retain + fix |
| 81 | `tests/evidence/test_refresh_policy_snapshot.py` | retain |
| 82 | `tests/evidence/test_release_bindings.py` | retain |
| 83 | `tests/evidence/test_sampler_evidence.py` | retire (c) |
| 84 | `tests/evidence/test_sanity_evidence_index.py` | retain |
| 85 | `tests/evidence/test_v2_mapped_cache_evidence.py` | retain + fix |
| 86 | `tests/hdctl/test_cli_admin_sidecar_invariance.py` | retain + fix |
| 87 | `tests/hdctl/test_cli_read_singlebg.py` | retire (a) |
| 88 | `tests/hdctl/test_cli_showcompat_parity.py` | retain + fix |
| 89 | `tests/hdctl/test_cli_streams_and_exits.py` | retain + fix |
| 90 | `tests/hdctl/test_cli_two_run_identity.py` | retain + fix |
| 91 | `tests/identity/test_service_identity_canonical.py` | retire (c) |
| 92 | `tests/infra/test_hash_coupling.py` | retain |
| 93 | `tests/infra/test_resolver_serializer_discipline.py` | retire (a) |
| 94 | `tests/infra/test_sercanon_bytes.py` | retain |
| 95 | `tests/infra/test_serializer_guard.py` | retire (b) |
| 96 | `tests/integration/test_normalized_fixture.py` | retain |
| 97 | `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` | retire (b) |
| 98 | `tests/loader/test_load_chart_fixture_only.py` | retain + fix |
| 99 | `tests/loader/test_loader_hdapi_ignores_tz.py` | retain |
| 100 | `tests/loader/test_loader_logs_keys_only.py` | retain + fix |
| 101 | `tests/loader/test_pinned_lists_not_empty.py` | retain |
| 102 | `tests/loader/test_validators_strict.py` | retain |
| 103 | `tests/provider/test_factory_and_safemode.py` | retire (b) |
| 104 | `tests/provider/test_hdapi_error_mapping.py` | retain |
| 105 | `tests/provider/test_hdapi_json_headers.py` | retain |
| 106 | `tests/provider/test_hdapi_request_shape.py` | retire (b) |
| 107 | `tests/provider/test_provider_call_logging_keys_only.py` | retire (a) |
| 108 | `tests/provider/test_provider_interface_contract.py` | retain |
| 109 | `tests/provider/test_prtest_precedence_and_artifact.py` | retain + fix |
| 110 | `tests/provider/test_resolve_log_correlation_id.py` | retain + fix |
| 111 | `tests/provider/test_secrets_dir_invalid.py` | retain |
| 112 | `tests/provider/test_secrets_errors_typed.py` | retire (d) |
| 113 | `tests/provider/test_secrets_unknown_provider_is_misconfigured.py` | retain |
| 114 | `tests/provider/test_startup_logging.py` | retain + fix |
| 115 | `tests/provider/test_vendor_and_prod_guard.py` | retain + fix |
| 116 | `tests/provider/test_vendor_and_prod_guard_min.py` | retain + fix |
| 117 | `tests/provider/test_vendor_call_rails_and_config.py` | retain |
| 118 | `tests/provider/test_vendor_guard_min.py` | retain |
| 119 | `tests/provider/tests/provider/test_decisions_perms_and_newline.py` | retire (e) |
| 120 | `tests/qa/test_epic021_scaffolding.py` | retain |
| 121 | `tests/qa/test_epic022_acceptance_scaffold.py` | retire (c) |
| 122 | `tests/qa/test_epic022_close_pack_ready.py` | retire (c) |
| 123 | `tests/reader_v1/test_cli_proof.py` | retire (b) |
| 124 | `tests/scripts/test_dev_sampler_healthcheck.py` | retain |
| 125 | `tests/test_catalog_canon.py` | retire (a) |
| 126 | `tests/test_pipeline_properties.py` | retire (a) |
| 127 | `tests/test_pipeline_public.py` | retire (a) |
| 128 | `tests/test_resolver_prod_rules.py` | retire (a) |
| 129 | `tests/test_sercanon.py` | retire (a) |
| 130 | `tests/unit/test_channel_derivation.py` | retire (a) |
| 131 | `tests/unit/test_enum_closure.py` | retire (a) |
| 132 | `tests/unit/test_narratives_composer.py` | retain |
| 133 | `tests/unit/test_no_io_guard.py` | retain |
| 134 | `tests/unit/test_sampler_core.py` | retain |
| 135 | `tests/unit/test_viewer_prefs_normalization.py` | retain |

**Sweep.** The per-file sweep of plan v1.1 §4.2 stands. Its tested state `a8c99d1` is content-identical to `e3a5ed4` outside `docs/`, so PR-30 did not repeat it. PR-30's own runs on the candidate cover every retained file (§6).

## 6. Local validation (plan v1.1 §9 and §11)

**Common conditions.** Every check ran on tree `40e27cd`: first through an unpublished candidate commit object (`aff6117`, same tree), then confirmed identical to commit `26140fe`. The environment was:
- Python 3.12.3, with CI's install (`'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`). The §6.2 validation used a dedicated venv installed from a worktree of the candidate. The §6.1 step checks used the session's earlier venv (same Python and install) with `PYTHONPATH` set to each candidate worktree, which takes precedence over that venv's editable install;
- pytest 8.4.2, with readiness shown by `python -m pip install -r requirements-dev.txt` then `python -m pytest --version`;
- `ruby` 3.3.6 (`/usr/local/bin/ruby`);
- `env -i` with `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, so every credential variable was unset.

### 6.1 Step checks (plan §9 steps 3–5)

| Check | Result |
| :- | :- |
| S04/S05 pinned tests on the candidate | 2 passed |
| S04 negative control (classifier line reverted) | the policy test fails (1 failed), as intended |
| S05 negative control (old workflow restored) | the path-filter test fails (1 failed), as intended |
| Analyzer negative control (base analyzer, the two new cases) | positive case fails, negative case passes, as intended |
| Baseline rebuild by rule from `main`'s generator (plan §5.8.1 script) | exit 0; 21 records; the result equals the candidate generator **byte for byte** |
| Rebuilt records against plan §5.8.1's table | equal: `api_bp`/`bp` (`factory.py`, `http_reader.py`), `reader_api_bp`/`reader_bp` (`wsgi.py`); route endpoints `aux_narrative`, `reader_method_not_allowed`, `reader_post`, `reader_post_not_allowed`, `reader_v1`; no `reader_v1_post` |
| Generator `ast` data-only check (`e3a5ed4` → candidate) | identical outside the baseline value; 23 → 21 records |
| Analyzer `ast` confinement | only `_adapter_routes_without_presenter` differs; import lines identical in both tools |
| Fixture-move `ast` checks | string constants unchanged except 103 `"tmp_boundary_test"` removed; the 187 earlier test functions unchanged (189 with the two new) |
| Each of the 27 fixed files alone | all pass; for each, `git status` empty and no tracked file newer than the marker |
| The fixed files of each directory together (8 directories) | adapter 10, arch 3, compliance 8, epic003 1, evidence 338, hdctl 5, loader 3, provider 12: all passed; clean tree and mtime each |

### 6.2 Validation (plan §11)

| # | Check | Result |
| :- | :- | :- |
| 1 | `python3 ci/checks/check_agents_md_citations.py`; `ci/checks/check_env_pins.sh` | exit 0 (`AGENTS_MD_CITATIONS_OK`); exit 0 (`[env-pins] OK`) |
| 2 | Pinned suites (`test_rails_ci_workflow_integration.py`, `tests/qa/test_qa_tool_ownership.py`, `test_http_reader_ci_ownership.py`, `test_evidence_tool_ownership.py`) | 314 passed; clean |
| 3 | Changed-test step exactly as `ci.yml` runs it: detached worktree, 163 targets from the classifier's `--changed-tests-output`, one pytest process | 3,262 passed in 423.5 s; exit 0; `git diff --exit-code` 0; status empty. The mtime check shows 11 tracked files rewritten with identical bytes, the same 11 paths as plan §4.3 (OBS-4, two covered tests outside this unit) |
| 3b | The 69 retained files alone, in their own detached worktree | 489 passed in 137.2 s; clean; **no** tracked file newer than the marker |
| 4 | `tests/evidence/test_hdapi_v2_contract_inventory.py` alone, in its own detached worktree | 300 passed in 103.6 s; clean; no tracked file newer than the marker; no `tmp_boundary_test/` |
| 5 | Product lane (`generate_ordering_artifacts.py --check` and its tests) | 77 passed; clean |
| 5 | Compat lane (`check_cli_help.sh`, serializer guard and emitter proof writing outside the tree, tests) | 102 passed, 3 skipped, 2 xfailed; clean. The skips and xfails are pre-existing, in covered files outside this unit (plan OBS-7: showcompat subprocess tests skip under closed rails; OBS-3: `tests/adapter/test_jsonschema.py` xfails) |
| 5 | DB lane (`check_direct_db_contract.py` and its tests) | 249 passed; clean |
| 5 | Rails lane (`run_rails_job_definitions.py` with the three job files; integration tests) | runner exit 0; 137 passed; clean |
| 5 | Evidence lane (7 read-only checks and its tests) | all checks exit 0; 113 passed in 566.2 s; clean |
| 5 | QA lane (own detached worktree) | 488 passed; clean |
| 5 | Release lane (`git diff --exit-code`, `release_id_recompute.py --check-manifest-only`, regression tests in their own worktree, then `build_release_attestation.py --output <external empty dir> --require-clean` and `--verify`) | exit 0; 64 passed, clean; build exit 0 and verify exit 0 |
| 5 | Worktree after all root lanes | `git diff --exit-code` 0, status empty, no tracked file newer than the marker; `git diff --check` 0 |
| 6 | Classifier dry run, `--base e3a5ed4 --head <candidate> --event-name pull_request` | exit 0; `selected_lanes`; seven lanes; `needs_python=true`; `changed_tests=true`; 100 paths; 163 targets, equal to `_full_validation_test_targets()` |
| 6 | Docs-only commit on top of the candidate (throwaway worktree) | exit 0; `documentation_only`; no lane; `needs_python=false`; `changed_tests=false`; empty target list |
| 6 | `changed_test_targets` (B-6, B-9, C-1) | generator → the contract-inventory test; analyzer → that test plus `tests/evidence/test_evidence_tool_ownership.py`; `adapter/factory.py` 4, `adapter/http_reader.py` 17 and `adapter/wsgi.py` 6 targets, each including the test; `engine/bodygraph/resolver.py` includes `tests/bodygraph/test_resolver_vendor.py` |
| 7 | Inventory; deleted paths against the ledger | 0 uncovered (212 / 49 / 204 / 163); deleted 66 = ledger 66 |
| 8 | Members | `release_id_recompute.py --check-manifest-only` exit 0; the `catalog/manifest.json` and `engine/config/registry_loader.py` diff is empty |

**Without `ruby` (B-8).** Measured on the plan v1.1 prototype (`180a376`). Its tree differs from `26140fe` only in `tests/retired_tests.md` (the date and row-97 wording) and the plan document under `docs/ephemeral/`: 9 failed, 0 skipped, each with `FileNotFoundError` for `ruby`. PR-30 did not repeat it, because the file and the tools are byte-identical to that prototype.

**Not run by PR-30:**
- hosted CI, which started on #627 (§9);
- the Codex code review and security review;
- live vendor, production or database access, which is not needed and not used.

## 7. RP-1 and RP-2 evidence (PF10 addendum 2.2)

- **B-1:** the only `tools/` files changed are the two named.
- **B-2:**
  - the generator diff is data-only and reproducible by rule from `main`;
  - the 21 records match the plan's PF05 §5.1.0/§5.4 review;
  - `reader_v1_post` is absent;
  - no write-mode run took place;
  - the reading of "at `/api`" is as plan v1.1 §5.8.1 records it (F-9).
- **B-3:** the change is confined to one function, with five acceptance conditions (plan §5.8.2), and is verified by the negative control.
- **B-4:** one positive and one negative test function.
- **B-5:** the governed-path diff is empty; import lines are unchanged; `test_architecture_snapshot.py` passes in the product lane.
- **B-6, B-9:** §6.2 row 6.
- **B-7:** 103 sites moved; the file gives 300 passed with `ruby`, a clean tree and a clean mtime check; the lane shape is the changed-test step (§6.2 rows 3 and 4).
- **B-8:** `ruby` 3.3.6 locally. On hosted CI it comes from the runner image (plan §5.8.5); PR-35 records it.
- **RP-2 (B-11 to B-14):**
  - `tests/loader/test_chart_loader_uses_provider_and_is_safe_mode_default.py` is retired under (b). Its ledger row is plan §7 row 97's reason verbatim and names RS-20 review v1.0 as the route.
  - The defect in `engine/charts/loader.py` is **not fixed** and is not represented as fixed, deferred to an HDE-CRD-0002 unit, or resolved. It belongs to the Product Owner, as decision owner for HDE-SEPA006.
  - No non-test file changed for it. `artifacts/logs/loader_call.jsonl` is unchanged; the retired file was its only test writer.
  - The replacing cases `tests/provider/test_vendor_and_prod_guard_min.py::test_vendor_refuses_in_safe_mode` and `tests/provider/test_vendor_call_rails_and_config.py::test_vendor_refused_when_safe_mode_on` pass in the full-validation run.

## 8. In-flight decisions

`NONE`. The implementation follows plan v1.1 without a scope or design change.

The plan directed both the ledger's regeneration verbatim from §7 and the row-97 wording, so neither is a decision. The dedicated candidate venv for the lane emulations is a validation method, not a decision. It was needed because the session's earlier venv had an editable install pointing at a different checkout.

## 9. PR_REMOTE_ACTION_LEDGER

| Time (UTC) | Action | Identity / evidence | State |
| :- | :- | :- | :- |
| 2026-10-13 (after 00:17:17Z) | Recovery reads: branches, remote heads, open PRs (none), `docs/ephemeral/` | §3 | done |
| 00:20:09Z | Candidate commit object created locally, not pushed | `aff6117`, tree `40e27cd` | local only |
| 00:20:58Z | Step checks (§6.1, S04/S05/analyzer controls, rebuild) | scratch worktrees | pass |
| 00:27:03Z | Fixed-file runs (27 files, 8 directories) | scratch worktree | pass |
| 00:27:59Z | TypeSafe reading for PR-35 (one send) | §11 | HTTP 200 |
| 00:53:59Z | §11 validation complete | §6.2 | pass |
| 00:54:20Z | Implementation commit | `26140fe`, tree `40e27cd` | local |
| ~00:54Z | Push (new remote branch) | `git ls-remote` → `26140fee…` | verified |
| 00:54:57Z | PR created | #627, head `26140fe`, base `e3a5ed4`, 100 files, ready for review | verified by API read |
| 00:55:00Z | CI run started on the `pull_request` event (S05 filter selects it) | Actions run 38329588625, head `26140fe` | in progress at record time; not a PR-30 gate |
| after this record | Commit and push this result record on the same branch | PR head moves to the result commit | the next CI run supersedes 38329588625 (`cancel-in-progress` for pull requests) |

**Remote state at record time:** PR #627 open, not draft, `mergeable_state: unstable` (CI pending), remote head `26140fe`. No review has been requested or read yet. Codex review activity is PR-35's to retrieve.

**Remaining useful local action for PR-30:** none.

**Next evidence actions (PR-35):**
- the Codex code and security reviews, and inline threads;
- the CI run on the current head after this record's push;
- mergeability.

## 10. Constraints, unresolved items and owners

| Item | Owner |
| :- | :- |
| Hosted CI on the current head (all seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`); the evidence lane took 566 s locally | PR-35 |
| Codex code review and security review findings | PR-35 |
| Hosted `ruby` presence and version, from the job log (B-8); whether it survives `ubuntu-latest` moving to Ubuntu 26.04 | PR-35 (observation); Product Owner (OBS-12 documentation delta) |
| Legacy chart-loader defect (HDE-SEPA006) | Product Owner |
| WU-PR-03 baseline currency; WU-PR-06 `ruby` in its sweep environment | whole-change IA (PR-10 for those units) |
| Plan v1.1 §17 observations OBS-1 to OBS-15 | the owners named there |
| The F-9 reading of B-2's "at `/api`" | recorded in plan v1.1 §5.8.1; the IA may raise it |
| Merge | Nathan only |

## 11. TypeSafe reading for the receiving session (PR-35)

PF10 addendum 2.1 governs. The reading is reported as the skill printed it. No agent recommendation is given beside it.

Action sent (v6): "Resolve, as the dedicated review-and-readiness session, the first code reviews and CI of one newly published pull request of about 100 files from the first unit of an approved CRD plan (bringing 135 unrun test files into CI: 66 test deletions with a ledger, 27 test-only fixes, a CI workflow path-filter change, classifier owner registrations, and two approved bounded corrections to governed evidence tools of about 4,800 and 3,200 lines), which its implementation session validated locally end to end (about 3,300 tests, every CI lane emulated) and handed off with a task list: read the Codex code and security reviews and inline threads, fix substantive in-scope findings locally, push coherent corrections, and verify current-head CI across seven lanes and mergeability until the pull request is genuinely ready. No live provider call occurs; the Product Owner merges manually and an independent landed-lineage review follows."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.95 (confidence 0.77); rung probabilities low 0.00, medium 0.00, high 0.20, extra high 0.65, max 0.15, ultracode 0.00. Model probabilities Fable 5.1 0.15, Opus 5.5 0.85 (confidence 0.70). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.00, Opus 5.5 at high 0.17, Opus 5.5 at extra high 0.55, Opus 5.5 at max 0.13, Opus 5.5 at ultracode 0.00, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.03, Fable 5.1 at extra high 0.10, Fable 5.1 at max 0.02, Fable 5.1 at ultracode 0.00. Sent 2026-10-13T00:27:59Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-13T00:27:59Z; HTTP 200 in 0.67 s; 4317 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1).

- **One send**, taken before this artifact was saved. The Notion row was not written.
- **Nathan's pick for PR-35:** not stated.
- **Nathan's pick for this PR-30 session:** not stated (the reading for PR-30 is in plan v1.1 §21).

**Surface advice for PR-35:**
- Run it as a top-level Claude Code cloud session that Nathan creates (`session_disposition: NEW_DEDICATED`), on `amthorn78/glow-hdengine-v2`, continuing #627 and its branch. It is never a subagent of this session.
- It needs GitHub access through the connected GitHub tools: PR reads, review threads, check runs and Actions runs. Notion is read-only.
- For local retests it needs Python 3.12 with CI's install, and `ruby` on `PATH`. No live vendor, production or database access is needed.
- Subscribing to #627's activity lets review and check events arrive without polling.

## 12. Handoff to PR-35

PR-35 owns everything in §10 that the table assigns to it, under plan v1.1 §19:
- reading every Codex code and security review and its threads;
- fixing substantive in-scope findings locally and pushing coherent corrections;
- CI economy, with no `[skip ci]` without Nathan's direct authorization;
- current-head CI across seven lanes and `CI_APPLICABILITY_AND_EXACT_HEAD_OK`;
- remote-head identity and mergeability;
- recording the hosted `ruby`;
- returning `MERGE_PENDING — Ready to merge` without merging.

It works in its own dedicated session on the same branch and PR, under the same Proceed.

## 13. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-30 / WU-PR-01 / plan v1.1 / attempt 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 |
| work unit / requirements | WU-PR-01; S03, S04, S05 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-30 — PR Implementation Proceed — 100926.1, https://app.notion.com/p/3f44590a05eb8148a538f5c80588db14 (fetched 2026-10-13; page state as of 2026-10-12T02:30:08Z) |
| role/stage | dedicated WU-PR-01 PR engineering session / PR-30 |
| capture time | 2026-10-13T00:58:07Z |
| execution identity | https://claude.ai/code/session_011q4bUbzJCYk2KAF7eAceF8 |
| PR / commits | amthorn78/glow-hdengine-v2#627; implementation commit `26140fe`; this record's commit on the same branch |
| inherited prompt uses | IA-10, IA-40, IA-30, PR-10 (instruction v1.0 §20), PR-20 (plan v1.0 §22, plan v1.1 §22), RS-20 (review v1.0 §14) |
| repository persistence | PENDING / NON_GATING: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist at `e3a5ed4`; recorded here only; owner GCFPE-MGMT-10 and the Product Owner |

## Canon relied on

Read on `main` at `e3a5ed4`, where `docs/pfcanon/` is unchanged since `9c767d2`.

- **PF10-HDE-Build-Notes v13.5.3:** read in full in this session.
  - Addendum 2.2 governs the RP-1 files and the RP-2 retirement (§4, §7).
  - Addendum 2.1 governs §11.
  - Permanent canon governs the rest of S03–S05 ("Silence rule").
- **PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3:** §5.1.0 and §5.4 (the rebuilt-baseline review; read for plan v1.1 in this session).
- **PF04-Canon-HDE-Governance v2.8.7:** §9.1.1 (the dedicated PR session, Nathan's Proceed, the manual merge) and §9.7.7 (the plan approval gate), as relied on by plan v1.1.
- **PF27-Canon-Plan-Templates v2.0.5:** "CI lane classification and automated budget-control discipline" (the smallest correct lane; no administrative closeout in ordinary PR CI), as relied on by plan v1.1.
- **PF06-Canon-Change-Process-Guide v2.5.4:** §1.0.6 (CI success alone is not QA acceptance), as relied on by plan v1.1.
- **PF19-Canon-Glow-QA-Guide v3.0.6:** "Change-lane QA applicability (normative)" (no QA artifact in a PR unit), as relied on by plan v1.1.
- **Operative documentation:** `AGENTS.md` (closed rails, pytest readiness, no hand-edited governed artifacts, PR description rules, evidence attribution).
- **In-flight documents:** instruction v1.0, plan v1.1 (in full, as the executed scope), RS-20 review v1.0, addendum v1.0.
- **Prompts and skill:** PR-30 (100926.1, in full); PR-35 (100926.1, read in full for its receiver contract); `glow-hde-pr-development` 1.4.0.

## Recovery

If this session is interrupted:
- **This record was pushed:** PR-30 is complete, and PR-35 starts from the handoff naming this file.
- **This record was not pushed:** commit `26140fe` and #627 exist. The only missing step is to commit, push and read back this file on the same branch.

Nothing is re-run. No second PR or branch is created.
