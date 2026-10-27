---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-CRD-0002-WU-PR-01-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-01
work_unit_title: CI coverage of every test file (PR; Distillation; S03, S04, S05)
AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS
applicable_pf10_overlays: NONE
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
SPECIFICATION_REF: docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md (v1.1, SPECIFICATION_APPROVED, "ASK OK."; blob c4802a5a7fa33db38d42d8a7f64679cd18b50480)
IMPLEMENTATION_PLAN_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md (v1.1; blob abffa2ccbd447a7e13727fc5e53e83341d35f0f4; 75,920 bytes; approved by PLAN_REVIEW_REF)
PLAN_REVIEW_REF: docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md (v1.1, IA-30 INITIAL_APPROVE, "ASK OK."; blob 0cc0276524b292777cc562b64bb983bdc4c55e3b; landed on main at a429c7c, amthorn78/glow-hdengine-v2#622)
IMPLEMENTATION_AUDIT_REF: docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md (v1.0, AUDIT_COMPLETE; blob b39ac9f276dbb06fa2222dfb9d7f5ecf05740f3c) — lineage only; every execution-critical fact this unit needs is carried in §5
pf10_ref: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md (v13.5.2; blob ec71eeecec8b0fcff1645d317211258bc708712c; sha256 c53dac75b7a6e7b7ed303c5b032e6d9a05a7285b89819104abd793bb1767222d; read in full; addendum 2.1 only, governing §19 only)
pf10_addendum_paths: none (no PF10_BUILD_NOTES_ADDENDUM exists for HDE-CRD-0002)
issuer: whole-change Implementation Agent (IA) for HDE-CRD-0002, same IA role and artifact lineage as the Audit and Plan (Audit and Plan v1.0 in session https://claude.ai/code/session_012nUipT8gpdYtjzA5UQk5ah; Plan v1.1 in session https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j; this instruction in session https://claude.ai/code/session_01WiUd7gGCtJvGgBixQNUjg1)
prompt: PR-10 — Create PR Work-Unit Instructions — 100926.1 (https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a)
prompt_release: GCFPE-20261009.1 / 100926.1 (GCFPE Membership and Release Register, "Current selection — GCFPE-20261009.1 / 100926.1", exactly 55 members; read 2026-10-12)
created_at: 2026-10-12T21:24:08Z
repository_baseline: origin/main a429c7cb921a8eb031502cdc102a8dd81594e8ef (no file outside docs/ephemeral/ changed between the Audit head 982071b and a429c7c)
receiver: dedicated HDE-CRD-0002 WU-PR-01 PR engineering session (session_disposition INITIAL_DEDICATED_ASSIGNMENT; role_session_ref NOT_YET_ASSIGNED, assigned by Nathan / Product Owner at launch)
next_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
canon_conflict_register: CR-1, CR-2, CR-3 carried unchanged (APPROVED_AS_CHANGED); no new entry (§16)
---

# HDE-CRD-0002 WU-PR-01 — PR Work-Unit Instruction v1.0

## 1. Result and authority boundary

**INSTRUCTION_READY.** This is the one complete, self-contained PR instruction for work unit WU-PR-01 of HDE-CRD-0002, issued by the whole-change IA from the approved Implementation Plan v1.1. A dedicated PR-20 session can plan the unit from this instruction and the linked current repository and canon, without reconstructing upstream intent (§17).

What it does not do:
- It is not the detailed per-file implementation plan. That is PR-20's output.
- It authorizes no implementation, commit, pull request, merge, deployment, Ops, QA, acceptance or closure. Only Nathan / Product Owner's `PR Implementation Proceed` (PR-30) for the exact PR-20 plan authorizes implementation. Only Nathan merges.
- It changes no canon and creates no PF10 addendum.

## 2. Identity and lineage

| Field | Value |
| :- | :- |
| `CHANGE_CLASS` / `CHANGE_ID` | `CRD` / `HDE-CRD-0002` — Post-HDE-EPIC040 Repair: Carried Defects, Code Security Review, Pre-Push Check and Close-Pack Writer |
| `WORK_UNIT_ID` | `WU-PR-01` — CI coverage of every test file; PR; Distillation phase block; requirements S03, S04, S05 |
| `SPECIFICATION_REF` | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 approved (Thoth, CF-C-30 INITIAL_APPROVE, `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md`) |
| `IMPLEMENTATION_PLAN_REF` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1. Its saved body keeps `PLAN_PENDING_REVISED` / `ASK OK?`; the approved representation is that unchanged body plus `PLAN_REVIEW_REF` |
| `PLAN_REVIEW_REF` | `docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md`, Isis, IA-30 `INITIAL_APPROVE`, `ASK OK.`, no PF10 addendum |
| Implementation Audit | `docs/ephemeral/HDE-CRD-0002-implementation-audit-v1.0.md`, `AUDIT_COMPLETE` (lineage; HDE Governance §9.7 "Planning audit posture") |
| `AUTHORING_CONTEXT` | `APPROVED_BASE_WITH_OVERLAYS`: authored from an approved base. The overlay set is empty |
| Immutable approved base | Specification v1.1 (approved) → Implementation Plan v1.1 + review v1.1 (approved). Neither is rewritten here |
| Effective baseline | approved base + applicable PF10 overlays = the base above + NONE |
| PF10 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.5.2.md`, the unique current controlled PF10 (one unlettered document). Addendum index: `2.1` only, which governs TypeSafe readings (§19). PF10 is silent on S03–S05, so permanent canon governs them (PF10 "Silence rule") |
| Active addendum paths | none |
| `EXECUTION_POSTURE` | `MANUAL_PROMPT_EXECUTION` |
| Prompt release | GCFPE-20261009.1 / 100926.1 / 55 (register read back 2026-10-12) |

## 3. Unit selection and dependency state

- **Plan approval.** Isis approved exactly Plan v1.1 (blob `abffa2cc…`) in review v1.1 §1: "It permits PR Instruction creation (PR-10) in the Plan's dependency order, starting with WU-PR-01." Confirmed on `main` at `a429c7c`.
- **Unit type.** PR unit (Plan v1.1 §7 heading "WU-PR-01 — CI coverage of every test file (PR; Distillation)").
- **Dependency state: ready.** Plan v1.1 §7: "First. No upstream dependency." No unit of HDE-CRD-0002 has landed. Review v1.1 §5 records the same. No PR, Proceed, QA Guide, QA Plan or Ops receipt is a prerequisite.
- **Order.** WU-PR-01 → WU-PR-02 → WU-PR-03 → WU-PR-04 → WU-PR-05 → WU-PR-06 → WU-PR-07 → WU-PR-08 → WU-DOC-01 → WU-OPS-01 (Plan §7). WU-PR-02, WU-PR-06 and WU-PR-07 may be prepared in parallel but merge in order.
- **Downstream dependents of this unit** (contracts in §8): WU-PR-03 and WU-PR-04 ("their surfaces' tests are in the uncovered set"); WU-PR-06 ("after WU-PR-01 (lane lists and sweep definition final)").
- **Open owner decision.** AQ-1 (Product Owner, S21 ADR) does not gate WU-PR-01.

## 4. Required behavior

The acceptance intents, verbatim from the approved Specification (Requirements table):

| ID | Scope | Acceptance intent (what must be true) |
| :- | :- | :- |
| S03 | Bring every test file into a CI lane or retire it with a recorded reason | No test file runs in no CI lane; each retirement has a recorded reason; recorded failures and collection errors are fixed or retired with their files |
| S04 | Unregistered `tools/qa/` sources get the same fail-closed treatment as `tools/bodygraph/` | An unregistered `tools/qa/` source, `.sh` and `.sql` included, cannot pass classification without an owner test |
| S05 | Align the CI workflow's documentation skip list with the classifier's documentation prefixes | A PR touching only classifier documentation prefixes starts no CI run |

Specification constraint "Uncovered tests" (verbatim): "S03 may expose real defects that enlarge the work. Running the uncovered files in the repository tree can rewrite tracked evidence (O-11), so any sweep runs in a throwaway copy." Phase block Distillation: "S04 and S05 travel with S03. S20 follows S03 to S05." Live QA class of S03, S04, S05: not production-affecting.

Plan v1.1 §7 purpose (IP Approved): "Make every test file in the repository run in a CI lane or retire it with a recorded reason, and close the two classifier and workflow gaps that travel with it."

Approved engineering choices this unit applies (Plan §5 and §7, carried here so the executor needs no other source):
- **EC-1 (S05).** Align the workflow skip list to the classifier's eight prefixes with explicit negations for governed primaries under them (today `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json`), pinned by a test that reads `docs/evidence/INDEX.json`. Reason: the classifier itself gives those two files the evidence lane, and skipping CI for them would remove protection the acceptance intent does not ask to remove. "Classifier documentation prefixes" therefore means paths the classifier returns no lanes for; a governed primary is not one.
- **EC-3 (S03).** Record every retirement reason in a tracked ledger `tests/retired_tests.md` as well as in the PR record.
- **S04 rule.** `_qa_tool_owner_targets` (or the prefix rule) treats every `_UNKNOWN_SOURCE_SUFFIXES` file under `tools/qa/` as the bodygraph rule does: registered owner, or `CI_QA_OWNER_TEST_MISSING`.

## 5. Current repository and reference baseline (verified at `a429c7c`)

The tested states are stated for each fact. `git diff --stat 982071b a429c7c -- . ':!docs/ephemeral'` is empty, so facts measured at `982071b` hold at `a429c7c`. PR-20 re-verifies at its own head before planning edits (Plan Templates "Repository loci and file minting"; observed facts prove planning-time reality only).

### 5.1 Test inventory (re-computed read-only by this IA at `a429c7c`)

| Set | Count |
| :- | -: |
| Tracked `tests/**/test_*.py` files | 278 |
| Reached by a fixed `ci.yml` lane pytest command (file named, or under a named directory) | 49 |
| `_registered_owner_test_paths()` entries | 135 (133 files plus the directories `tests/db` and `tests/order`) |
| `_full_validation_test_targets()` | 94 |
| Under a `pytest.ini` `testpaths` root | 70 |
| **Strict uncovered set:** reached by no lane command and by no full-validation target (what CI can never run) | **135** |
| Of which reached by neither lane, nor registered owner, nor `pytest.ini` root (HDE-EPIC040 PR05 O-11 definition) | 130 |
| Of which the five `_FULL_VALIDATION_INACTIVE_TESTS` (under a `pytest.ini` root, fail-closed by the classifier) | 5 |

**Computation (binding definition for acceptance (1) and for WU-PR-06's `sweep`).** For each tracked `tests/**/test_*.py`: covered when the path equals, or lies under, a `tests/...` token in a `python -m pytest` command of a `.github/workflows/ci.yml` lane step, or equals, or lies under, an entry of `_full_validation_test_targets()` imported from `ci/checks/classify_ci_changes.py`; otherwise uncovered. Import the classifier without writing bytecode into the tree (`PYTHONDONTWRITEBYTECODE=1`, and not `python -I`, which ignores that variable; or a throwaway copy).

**The 135 files at `a429c7c`** (the five inactive files are `tests/cli/test_cli_env_pins_epic021.py`, `tests/config/test_config_acceptance_map.py` and the three `tests/qa/` files):

- `tests/adapter/` (13): `test_cache_keys.py`, `test_compat_writer_transport.py`, `test_env_guard_forbidden_matrix.py`, `test_env_guard_import.py`, `test_env_guard_import_purity.py`, `test_env_guard_prod_variants.py`, `test_env_guard_silence_and_idempotence.py`, `test_etag_core.py`, `test_gate_auth.py`, `test_headers_and_determinism.py`, `test_no_etag_on_writers_and_errors.py`, `test_reader_parity.py`, `test_readyz.py`
- `tests/adapters/` (1): `test_safe_mode.py`
- `tests/arch/` (2): `test_arch_capture_exists.py`, `test_arch_guards.py`
- `tests/artifacts/` (1): `test_cli_text_artifacts_bom_lf.py`
- `tests/audit/` (7): `test_acceptance_map_epic017.py`, `test_acceptance_map_epic019.py`, `test_acceptance_maps_index.py`, `test_epic017_close_report.py`, `test_epic017_docdeltas.py`, `test_epic017_manifest.py`, `test_epic020_acceptance_bundle_wiring.py`
- `tests/bodygraph/` (2): `test_bg_resolve_route_policy.py`, `test_resolver_vendor.py`
- `tests/canon/` (6): `test_center_order_and_counts.py`, `test_checksums.py`, `test_error_envelope.py`, `test_loader_integrity.py`, `test_overrides_prod.py`, `test_report_determinism.py`
- `tests/cli/` (1): `test_cli_env_pins_epic021.py`
- `tests/compat/` (4): `test_cli_public_bytes_identity.py`, `test_thresholds_constants_pack.py`, `test_ts_import_no_io.py`, `test_ts_sidecar_checks_manual.py`
- `tests/compliance/` (12): `test_429_retry_after_mapping_seconds_and_date.py`, `test_cli_admin_gate_sidecar_perms_and_stdout_hash_invariance.py`, `test_cli_release_id_resolver_precedence.py`, `test_invocation_tag_accept_reject_and_roundtrip.py`, `test_log_shape_snapshot.py`, `test_meta_abba_parity.py`, `test_override_guard_engine_env_and_app_env_alias.py`, `test_preset_schema_gate_legacy_missing_both_present.py`, `test_public_payload_goldens_success_error_lf_and_no_etag_on_errors.py`, `test_reader_etag_and_conditional.py`, `test_reader_etag_compression_invariance.py`, `test_release_id_precedence_and_grep_guard.py`
- `tests/config/` (1): `test_config_acceptance_map.py`
- `tests/em/` (4): `test_em_defaults_and_ladder.py`, `test_em_off_toggle.py`, `test_em_throat_and_adjacency.py`, `test_goldens_public_shape_and_identity.py`
- `tests/epic003/` (3): `test_error_message_map.py`, `test_http_home_single_path.py`, `test_legacy_imports_denied.py`
- `tests/evidence/` (28): `test_aux_preview_identity_parity.py`, `test_cli_conformance_artifacts.py`, `test_db_runtime_posture.py`, `test_env_matrix_snapshot_v3.py`, `test_epic018_manifest.py`, `test_epic020_bundle_index_integration.py`, `test_epic030_pr01_pr03_fail_closed_evidence.py`, `test_epic030_pr04_band_thresholds_evidence.py`, `test_evidence_index_env.py`, `test_evidence_index_snapshot.py`, `test_evidence_index_token_sets.py`, `test_hdapi_v2_contract_inventory.py`, `test_hdapi_v2_live_conformance.py`, `test_hdapi_v2_response_normalization.py`, `test_hde_epic035_pr03_evidence_loop.py`, `test_hde_epic036_pr02_evidence_loop.py`, `test_hde_epic037_bg_resolve.py`, `test_hde_epic037_field_sufficiency.py`, `test_hde_epic037_pr05_parent_binding.py`, `test_hde_epic037_v2_to_compat.py`, `test_identity_provenance.py`, `test_internal_version_manifest_captures.py`, `test_presenter_evidence_ownership.py`, `test_refresh_policy_snapshot.py`, `test_release_bindings.py`, `test_sampler_evidence.py`, `test_sanity_evidence_index.py`, `test_v2_mapped_cache_evidence.py`
- `tests/hdctl/` (5): `test_cli_admin_sidecar_invariance.py`, `test_cli_read_singlebg.py`, `test_cli_showcompat_parity.py`, `test_cli_streams_and_exits.py`, `test_cli_two_run_identity.py`
- `tests/identity/` (1): `test_service_identity_canonical.py`
- `tests/infra/` (4): `test_hash_coupling.py`, `test_resolver_serializer_discipline.py`, `test_sercanon_bytes.py`, `test_serializer_guard.py`
- `tests/integration/` (1): `test_normalized_fixture.py`
- `tests/loader/` (6): `test_chart_loader_uses_provider_and_is_safe_mode_default.py`, `test_load_chart_fixture_only.py`, `test_loader_hdapi_ignores_tz.py`, `test_loader_logs_keys_only.py`, `test_pinned_lists_not_empty.py`, `test_validators_strict.py`
- `tests/provider/` (17): `test_factory_and_safemode.py`, `test_hdapi_error_mapping.py`, `test_hdapi_json_headers.py`, `test_hdapi_request_shape.py`, `test_provider_call_logging_keys_only.py`, `test_provider_interface_contract.py`, `test_prtest_precedence_and_artifact.py`, `test_resolve_log_correlation_id.py`, `test_secrets_dir_invalid.py`, `test_secrets_errors_typed.py`, `test_secrets_unknown_provider_is_misconfigured.py`, `test_startup_logging.py`, `test_vendor_and_prod_guard.py`, `test_vendor_and_prod_guard_min.py`, `test_vendor_call_rails_and_config.py`, `test_vendor_guard_min.py`, `tests/provider/test_decisions_perms_and_newline.py` (nested; full path `tests/provider/tests/provider/test_decisions_perms_and_newline.py`)
- `tests/qa/` (3): `test_epic021_scaffolding.py`, `test_epic022_acceptance_scaffold.py`, `test_epic022_close_pack_ready.py`
- `tests/reader_v1/` (1): `test_cli_proof.py`
- `tests/scripts/` (1): `test_dev_sampler_healthcheck.py`
- `tests/` (5): `test_catalog_canon.py`, `test_pipeline_properties.py`, `test_pipeline_public.py`, `test_resolver_prod_rules.py`, `test_sercanon.py`
- `tests/unit/` (6): `test_channel_derivation.py`, `test_enum_closure.py`, `test_narratives_composer.py`, `test_no_io_guard.py`, `test_sampler_core.py`, `test_viewer_prefs_normalization.py`

### 5.2 Sweep result (one run; tested state `982071b`, equal to `a429c7c` outside `docs/ephemeral/`)

Recorded by the IA's Implementation Audit run: the 130 O-11 files were run once in a throwaway clone under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; vendor, geocode and database keys unset), Python 3.12.3, CI's install, `pytest -q -p no:cacheprovider --continue-on-collection-errors`. Result: **79 failed, 523 passed, 14 errors in 160 s; exit 1.** The run **rewrote 27 tracked files** and created `tmp/`: `artifacts/epic020/bundles/*` (16 files), `artifacts/evidence_index.jsonl` and its `.sha256` and path proofs, `docs/evidence/INDEX.json`, `INDEX.sha256` and their path proofs, `artifacts/goldens/public_success.json` and `.sha256`, `artifacts/logs/loader_call.jsonl`, `artifacts/release_id.txt`. These files must never be run in the repository tree.

| Class | Files |
| :- | :- |
| Collection errors: imports of removed legacy trees (`core.canon`, `core.pipeline`, `core.config`, `core.stable`, `core.catalog`, `adapters.hdapi`, `adapters._net`) — 14 | `tests/adapters/test_safe_mode.py`; `tests/canon/{test_center_order_and_counts,test_checksums,test_loader_integrity,test_overrides_prod,test_report_determinism}.py`; `tests/em/test_em_defaults_and_ladder.py`; `tests/test_catalog_canon.py`; `tests/test_pipeline_properties.py`; `tests/test_pipeline_public.py`; `tests/test_resolver_prod_rules.py`; `tests/test_sercanon.py`; `tests/unit/test_channel_derivation.py`; `tests/unit/test_enum_closure.py`. `ARCHITECTURE.md` "Deprecated/archived trees": `core/`, `server/`, `adapters/` removed; active code must not import them |
| Files with at least one failure — 37 | 21 failures in `tests/evidence/test_hdapi_v2_contract_inventory.py`; 3 each in `tests/compliance/test_preset_schema_gate_legacy_missing_both_present.py`, `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py`, `tests/compliance/test_cli_release_id_resolver_precedence.py`, `tests/arch/test_arch_guards.py`, `tests/adapter/test_readyz.py`, `tests/adapter/test_reader_parity.py`; 2 each in seven `tests/provider/*` files, `tests/hdctl/test_cli_read_singlebg.py`, `tests/em/test_em_throat_and_adjacency.py`, `tests/compliance/test_429_retry_after_mapping_seconds_and_date.py`, `tests/adapter/test_headers_and_determinism.py`; 1 each in sixteen further files, including `tests/reader_v1/test_cli_proof.py` (the HDE-EPIC040 O-P06a-03 baseline failure) and `tests/compat/test_cli_public_bytes_identity.py` |
| Passed completely — 79 | the remainder of the 130 |

Not measured: the five inactive files (fail-closed by design). Not diagnosed: 21 failures in `tests/evidence/test_hdapi_v2_contract_inventory.py` and one in `tests/evidence/test_hde_epic037_pr05_parent_binding.py` that HDE-EPIC040 PR05 (Python 3.11.15) did not see (57 failed / 546 passed / 13 errors over 129 files). Environment or drift: PR-20 re-runs the sweep on Python 3.12 in a throwaway copy and diagnoses them.

### 5.3 Classifier facts (`ci/checks/classify_ci_changes.py`, 1,958 lines, at `a429c7c`)

- `LANES = ("product", "compat", "db", "rails", "evidence", "qa", "release")` (line 25).
- Full validation (every lane) for `.github/` and `.claude/` prefixes and the paths `.gitignore`, `ci/checks/classify_ci_changes.py`, `pyproject.toml`, `pytest.ini`, `requirements-dev.txt`, `requirements.txt`, `tests/evidence/test_rails_ci_workflow_integration.py` (lines 28–40). This unit therefore runs every lane.
- `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` (lines 41–82) and `_FULL_VALIDATION_INACTIVE_TESTS` (lines 83–92, five files, comment: "Administrative or source-writing checks that are intentionally outside the current behavioral suite. Direct edits fail closed until a current consumer and safe execution owner are established").
- `_DOCUMENTATION_PREFIXES` (lines 108–117): `docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/`.
- `_FIXED_LANE_TEST_DIRECTORIES` (`tests/db` → db, `tests/order` → product) and `_FIXED_LANE_TEST_PROVIDERS` (lines 820–864) mirror the `ci.yml` lane lists.
- `_UNKNOWN_SOURCE_SUFFIXES = {".py", ".sh", ".sql"}` (line 865).
- `_load_governed_primary_paths` reads `docs/evidence/INDEX.json` `discovered_physical_path` values (lines 905–935) so a governed primary under a documentation prefix still selects the evidence lane.
- `_registered_owner_test_paths()` (line 964) unions the fixed providers, the supplement and every owner registry (`_PRODUCT_TEST_OWNER_PATHS`, `_PRODUCT_TEST_OWNER_PREFIXES`, `_EVIDENCE_GENERATOR_TEST_OWNERS`, `_EVIDENCE_HELPER_TEST_OWNERS`, `_QA_TOOL_TEST_OWNERS`, `_CONFIG_WRITER_TEST_OWNERS`, `_BODYGRAPH_TOOL_TEST_OWNERS`, `_TEST_SUPPORT_OWNER_PATHS`, `_FIXTURE_TEST_OWNER_PREFIXES`). `_full_validation_test_targets()` (line 989) returns every registered owner that is not inactive and not supplied by a fixed lane.
- `_qa_tool_owner_targets` (lines 1174–1199) fails closed (`CI_QA_OWNER_TEST_MISSING`) only for `.py` under `tools/qa/`. `_bodygraph_tool_owner_targets` (lines 1209–1229) fails closed (`CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING`) for every `_UNKNOWN_SOURCE_SUFFIXES` file under its prefix.
- The unknown-source refusal `CI_SOURCE_OWNER_TEST_MISSING` applies only when `_lanes_for_path` returns `None` (lines 1578–1582); `_lanes_for_path` (line 1590) returns `{"evidence", "qa"}` for every `tools/qa/` and `tests/qa/` path (line 1657), so an unregistered `tools/qa/*.sh` or `*.sql` passes today.
- `tools/qa/` holds no `.sh` or `.sql` file today.
- `_RELEASE_IMPLEMENTATION_PATHS` (lines 148–182) names `tests/evidence/test_internal_version_manifest_captures.py`, one of the 135.
- CLI: `python3 ci/checks/classify_ci_changes.py --base <sha> --head <sha> --event-name {pull_request,push} [--repo-root PATH]` plus the two output options used by `ci.yml` (lines 1902–1920).

### 5.4 Workflow and pytest facts

- `.github/workflows/ci.yml` (404 lines): `paths-ignore` on `pull_request` and on `push` to `main` lists four prefixes, `docs/pfcanon/**`, `docs/ephemeral/**`, `docs/graph/**`, `docs/prompt_ecosystem_management/**` (lines 5–17). A PR touching only `docs/crd/`, `docs/plans/`, `docs/qa/` or `docs/run/` therefore starts a run that selects no lane.
- One `test` job; pull-request-only cancellation of superseded runs (line 24); classification step (lines 53–58); Python 3.12 and install `python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .` (lines 64–80); changed-test isolation in a detached worktree under closed rails with `git diff --exit-code` and an empty `git status --short --untracked-files=all` afterwards (lines 91–117); seven lanes with explicit pytest lists (`product` 126–130, `compat` 141–151, `db` 160–167, `rails` 203, `evidence` 218–224, `qa` 243–250, `release` 277–281); final marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK` (line 404).
- `pytest.ini` `testpaths` (twelve roots): `tests/bodygraph/test_gates.py`, `tests/mech`, `tests/categories`, `tests/config`, `tests/evidence/test_evidence_tool_ownership.py`, `tests/invariance`, `tests/transport`, `tests/support`, `tests/cli`, `tests/db`, `tests/qa`, `tests/m10`. No `ci.yml` step runs bare `pytest`, so these roots reach CI only through lane lists and changed-test targets.
- `tests/evidence/test_rails_ci_workflow_integration.py` pins workflow text (for example lines 94–110) and classifier expectations, including governed-primary cases for `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json` (lines 278–279, 1151–1187) and a documentation-only case returning reason `documentation_only` with no lanes (lines 1423–1431). It also uses `tests/adapter/test_env_guard_prod_variants.py`, one of the 135, as a changed-test example (lines 301, 364–370, 1135, 1245–1253, 1323–1339) and pins rails job commands that name `tests/bodygraph/test_resolver_vendor.py` (lines 1591–1595).
- Governed primaries under the eight documentation prefixes, from `docs/evidence/INDEX.json` at `a429c7c`: exactly `docs/run/EPIC011_TEST_IDENTITIES.md` and `docs/run/PROD_ENDPOINTS.json`. None of the 135 test files is an Index primary.

### 5.5 Current consumers of uncovered files (retirement feasibility)

Found by `git grep` of the 135 paths at `a429c7c` outside `docs/ephemeral/` and `docs/pfcanon/`:

| Consumer | Uncovered file it executes or names |
| :- | :- |
| `tools/evidence/regenerate_identity_closure.py` lines 278–283 (closure step) and 372–381 (run inside the release attestation's isolated copy) | `tests/evidence/test_internal_version_manifest_captures.py`; `tests/evidence/test_aux_preview_identity_parity.py` |
| `ci/checks/run_rails_job_definitions.py` lines 54, 61; `ci/jobs/rails_closed_refusal.yml` line 11; `ci/jobs/logs_keys_only_redaction.yml` line 16 | `tests/bodygraph/test_resolver_vendor.py` |
| `tools/evidence/generate_epic031_pr01_provider_gate.py` line 35; `tools/evidence/generate_epic031_pr02_log_posture.py` line 251 | `tests/bodygraph/test_resolver_vendor.py` |
| `tools/evidence/generate_hde_epic036_bg_resolve_route_policy.py` line 39 | `tests/bodygraph/test_bg_resolve_route_policy.py` |
| `tools/evidence/generate_hdapi_v2_contract_inventory.py` line 4647 | `tests/evidence/test_hdapi_v2_contract_inventory.py` |
| `tests/evidence/test_release_attestation.py` lines 617–618 (asserts absence from a source) | `tests/qa/test_epic022_acceptance_scaffold.py`; `tests/qa/test_epic022_close_pack_ready.py` |
| `tests/qa/test_epic021_harness_entrypoint.py` line 152; `tests/qa/test_viability_generator_wrappers.py` line 626 | `tests/qa/test_epic021_scaffolding.py`; `tests/unit/test_viewer_prefs_normalization.py` |
| `ci/checks/classify_ci_changes.py` lines 87–91 (inactive set), 155 (`_RELEASE_IMPLEMENTATION_PATHS`) | the five inactive files; `tests/evidence/test_internal_version_manifest_captures.py` |
| Historical governed records (frozen; never edited): `docs/acceptance_map_epic019.json`, `docs/acceptance_map_epic022.json`, `docs/acceptance_map_epic033.json`–`epic036.json`, and many `audit/**` and `artifacts/**` records | various |

### 5.6 New-file absence proof

`tests/retired_tests.md` does not exist at `a429c7c` (`ls tests/retired_tests.md` → "No such file or directory"). Predicate for PR-20 and PR-30: `test ! -e tests/retired_tests.md` at the planning and implementation base → PASS means the file is new; FAIL means stop and record what exists before writing.

## 6. Bounded files and components

Each locus is IP Approved: Plan v1.1 §7 WU-PR-01 "Deliverables", verbatim: "`.github/workflows/ci.yml` (lane lists; `paths-ignore` aligned to the classifier's eight documentation prefixes with negations for governed primaries); `ci/checks/classify_ci_changes.py` (owner and lane registrations for retained files; `tools/qa/` fail-closed treatment for `.py`, `.sh`, `.sql`; the inactive set resolved); `pytest.ini` where roots change; the retained test files, fixed where they fail or write tracked artifacts; the retired test files removed; `tests/retired_tests.md` (new ledger: path, reason, date, replacing coverage if any); `tests/evidence/test_rails_ci_workflow_integration.py` (pinned expectations, including the governed-primary negation test that reads `docs/evidence/INDEX.json`)."

| Path | Bound |
| :- | :- |
| `.github/workflows/ci.yml` | Lane pytest lists; `paths-ignore` for `pull_request` and `push` per EC-1. No new job, no change to the exact-head, install, isolation or marker mechanics beyond what lane membership needs |
| `ci/checks/classify_ci_changes.py` | Owner and lane registrations for retained files; S04 fail-closed rule for `.py`, `.sh`, `.sql` under `tools/qa/`; `_FULL_VALIDATION_INACTIVE_TESTS` resolved (each file registered or retired) |
| `pytest.ini` | Only where `testpaths` roots change |
| The 135 files of §5.1 | Each retained (registered, and fixed where it fails or writes tracked artifacts) or retired (deleted). Fixes stay inside test code and test-local fixtures |
| `tests/retired_tests.md` | New ledger (§5.6): one row per retired file with path, reason, date and replacing coverage (or "none") |
| `tests/evidence/test_rails_ci_workflow_integration.py` | Pinned workflow and classifier expectations, including the governed-primary negation test that reads `docs/evidence/INDEX.json`, the S04 refusal cases and the documentation-only case |
| `docs/ephemeral/` PR result record | The PR-30 result record (evidence obligations, §10) |

Any other file the work needs is a finding: route it under §14 before changing it.

## 7. Exclusions

- No release member changes. WU-PR-01's loci are non-members (`ci/**`, `.github/workflows/ci.yml`, `tests/**`, `pytest.ini`), so `catalog/manifest.json`, `engine/config/registry_loader.py` and the admission constants do not change. A fix that needs a non-test source change, above all in a release member, is outside this unit (§14).
- No change to any `tools/**` or `scripts/**` file, to `ci/jobs/*.yml` or to `ci/checks/run_rails_job_definitions.py`. The consumers in §5.5 stay as they are.
- No governed artifact is regenerated or hand-edited: no Index, Mirror, path proof, acceptance map, token matrix, close pack or frozen capture. Historical records that name a retired file stay unchanged; the ledger row records that they do.
- No skipped, disabled, `xfail`-marked or quarantined test to reach green (Plan §7 R-1: "never skip, disable or quarantine a test to get green"). Retirement is deletion with a recorded reason, never a skip marker or an exclusion list.
- No new required CI job or workflow; the lane assignment is the smallest correct lane (Plan Templates "CI lane classification and automated budget-control discipline"). The YAML arrangement is PR-20's to select; this instruction invents none.
- No QA artifact, QA evidence or `audit/qa/hde-crd-0002/` content; no PF09 mapping; no canon edit; no `AGENTS.md` or `README.md` edit (WU-DOC-01 owns operative documentation).
- No live vendor, production or database call; all runs under closed rails.
- Nothing from WU-PR-02 to WU-PR-08: no S10, S14 or other behavior change to the surfaces the uncovered tests exercise.

## 8. Interface contracts with other units

| Contract | Consumer | Binding content |
| :- | :- | :- |
| C-1 `tests/bodygraph/test_resolver_vendor.py` retained and registered | WU-PR-04 (its deliverables list it as "registered by WU-PR-01"; it will extend the file) | Retained, registered to a lane or as an active owner target, passing against current resolver behavior |
| C-2 `tests/adapter/test_gate_auth.py` retained with a registered owner | WU-PR-03 (dependency: "registered owners for `tests/adapter/test_gate_auth.py` and the http_reader owner guard") | Retained and registered, passing against current `GET /reader` behavior. WU-PR-03 changes the behavior and the test with S10. The PR-20 plan states whether it joins `_HTTP_READER_TEST_OWNERS` (classifier lines 283–306) or another owner registry |
| C-3 Coverage definition | WU-PR-06 (`sweep` must reproduce this set) | The §5.1 computation stays a pure function of `ci.yml` lane commands and `_full_validation_test_targets()`. If PR-20 changes how coverage is derived, it records the new definition in the PR result record |
| C-4 Final lane lists | WU-PR-06 (`replay` covers every lane step name in `ci.yml`) | Lane names and step structure stay; lists grow or shrink by registration only |
| C-5 No member change | WU-PR-03 to WU-PR-05 refresh the manifest at `1.3.0`; WU-PR-08 cuts `1.4.0` | WU-PR-01 leaves the `1.3.0` manifest and `release_id` untouched |
| C-6 Owner registry shape | WU-PR-04, WU-PR-06, WU-PR-07 register new modules | The S04 rule fails closed for `.py`, `.sh`, `.sql` under `tools/qa/` exactly as `_bodygraph_tool_owner_targets` does for its prefix |

## 9. Disposition rules PR-20 must apply and record

1. **One disposition per file.** Each of the 135 files gets exactly one disposition: fixed lane (named), registered owner target (owner path named), or retired (reason). The PR-20 plan carries the per-file table.
2. **Fix-versus-retire criterion (review v1.0 N2, carried by review v1.1 §4).** The PR-20 plan states when a failing file of current behavior is fixed rather than retired. It must cover at least the files that test surfaces this CRD changes: `tests/compliance/test_override_guard_engine_env_and_app_env_alias.py` and `tests/provider/test_vendor_and_prod_guard*.py` (S14 environment classification) and `tests/adapter/test_gate_auth.py` (S10). A file that tests current, governed behavior is fixed, not retired, unless the plan records why its coverage is redundant and which retained test replaces it.
3. **Legacy-tree imports.** The 14 collection-error files import removed trees. Retiring them is the expected disposition; `ARCHITECTURE.md` "Deprecated/archived trees" is the reason basis. Re-pointing one to current code is a fix and is allowed only when it tests current behavior.
4. **Tracked writes.** A retained file that writes tracked artifacts is fixed to write under `tmp_path`, or it runs only in the detached-worktree changed-test step, whose clean-tree assertion catches writes. Any lane it joins must leave `git diff --exit-code` and `git status --short --untracked-files=all` empty.
5. **Consumers first (§5.5).** A file that a current tool, job definition, closure step or other test executes or names is retained unless the plan proves the consumer keeps working. Retiring `tests/evidence/test_internal_version_manifest_captures.py` or `tests/evidence/test_aux_preview_identity_parity.py` would break the release identity closure. Retiring `tests/bodygraph/test_resolver_vendor.py` would break C-1 and the rails job definitions. Changing those consumers is outside §6 (§14).
6. **Inactive set.** Each of the five `_FULL_VALIDATION_INACTIVE_TESTS` is registered with a safe execution owner or retired with its reason; the set is resolved (Plan deliverable "the inactive set resolved"). `tests/evidence/test_release_attestation.py` lines 617–618 assert two of them are absent from a source; keep that assertion true.
7. **Undiagnosed failures.** The 22 failures §5.2 lists as undiagnosed are diagnosed on Python 3.12 before disposition.
8. **Real defects.** A failure that exposes a real product defect is not fixed by changing the test's expectation. If fixing it needs a non-test change, route it (§14); the file's disposition waits on that route, and the plan records it.
9. **Ledger.** `tests/retired_tests.md` lists every retirement with path, reason, date and replacing coverage (or "none"). Retirement reasons are also in the PR result record.

## 10. Acceptance, tests and evidence

**Acceptance (Plan v1.1 §7 WU-PR-01 "Acceptance and verification (done means)", verbatim):**
1. "The Audit §3(b) computation at the PR head returns zero files outside lane-or-target coverage, and the ledger explains every retirement." The computation is the one in §5.1.
2. "Every retained file passes under closed rails in its lane shape in a detached worktree with `git diff --exit-code` and an empty status afterwards."
3. "An unregistered `.sh` or `.sql` under `tools/qa/` fails classification in a unit test."
4. "The classifier dry run on a documentation-only path set selects no lane, and the workflow's path filter ignores exactly the classifier's prefixes minus governed primaries."
5. "All seven lanes green on the exact head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`."

**Evidence obligations (Plan, verbatim):** "PR result record with the before/after inventory (130/135 → 0), the per-file disposition table (lane or target, or retirement reason), the sweep transcript summary and the lane counts; no QA artifact." The record lives under `docs/ephemeral/` and names every check actually run with its counts.

| Requirement | Acceptance item | Proof | Evidence stage |
| :- | :- | :- | :- |
| S03 | (1), (2), (5) | §5.1 computation at the PR head returns 0; per-file table; ledger; each retained file passing in a detached worktree with a clean tree afterwards; lane counts | PR-30 local validation; PR-35 exact-head CI |
| S04 | (3), (5) | Unit tests in `tests/evidence/test_rails_ci_workflow_integration.py` (or the classifier's existing test home the plan names) for an unregistered `tools/qa/*.sh` and `tools/qa/*.sql` raising `CI_QA_OWNER_TEST_MISSING`; registered `tools/qa/*.py` unchanged | PR-30 local; CI rails lane |
| S05 | (4), (5) | Classifier dry run on a documentation-only path set (reason `documentation_only`, no lane); a test that derives the expected `paths-ignore` from `_DOCUMENTATION_PREFIXES` and the governed primaries in `docs/evidence/INDEX.json` and compares it with both `ci.yml` filters | PR-30 local; CI rails lane |

**Validation shape.** Closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`, vendor, geocode and database keys unset). Python 3.12 with CI's install. `AGENTS.md` pytest readiness: `python -m pip install -r requirements-dev.txt`, then `python -m pytest --version`. Any run of an uncovered or newly registered file happens in a throwaway copy or detached worktree, never in the working tree. `ci/checks/check_env_pins.sh` and `python3 ci/checks/check_agents_md_citations.py` stay green.

**Nonclaims (Plan):** "CI green is not QA; no PF09 mapping."

## 11. Migration and security constraints

- **Migration:** none. No data, schema, catalog or stored BodyGraph change. Rollback is Nathan's revert of the squash commit; no manifest refresh is needed because no member changes.
- **Security:** the workflow keeps `permissions: contents: read`, the exact-head checkout, closed rails in every lane and the isolation step. `paths-ignore` must not skip CI for any governed primary. The S04 change narrows what passes classification and never widens it. Retired tests that guarded security-relevant behavior (rails, keys-only logging, secret handling, environment guards) need a named replacing test or a recorded reason why the behavior no longer exists. No secret, token or key value appears in tests, logs or the PR record.

## 12. Engineering, review, CI and merge obligations

- **PR-20** (dedicated PR session): reads this instruction and its lineage, the repository files in §5 and §6, and canon on `main`; writes one complete `PR_IMPLEMENTATION_PLAN` under `docs/ephemeral/` with the per-file table, the N2 criterion, the YAML and classifier approach, ordered steps, the requirement-to-change/test map, risks and recovery; returns `AWAITING_PO_PROCEED` only for a complete plan within this scope. It mutates nothing outside its own artifact.
- **PR-30** (after Nathan's Proceed for that exact plan): recovers existing work before creating a vehicle; implements only the authorized scope; tests locally under §10; forms one coherent commit; publishes the initial candidate (`PR_CANDIDATE_PUBLISHED`); hands off to PR-35 in its own session.
- **PR-35** (its own dedicated session): retrieves and resolves review findings (Codex code review and security review on the PR), retests locally, pushes coherent corrections, uses CI economically, verifies current-head CI and mergeability, and returns `MERGE_PENDING` without merging. No CI waiver exists for HDE-CRD-0002; any waiver is Nathan's direct decision.
- **PR description:** `.github/pull_request_template.md` headings with the `AGENTS.md` content rules (Why; What changed by path; Checks run with counts; Not in this PR; What merging does, naming what becomes current on `main` and that QA, acceptance and closure are not established).
- **Merge:** Nathan merges, manually. No agent merges, enables auto-merge, enqueues or schedules a merge, or asks to merge as routine.
- **PR-40:** after the merge is observed (`MERGE_OBSERVED`) or asserted by Nathan, this IA reviews the landed lineage (PR-40) and, on ACCEPT, issues the next unit's instruction (WU-PR-02).
- **Delivery of attributable lineage:** the PR result records, the PR reference and the squash commit are the lineage PR-40 verifies.

## 13. Recovery

- Interruption: resume in the same dedicated phase session from its last saved artifact; inspect existing worktrees, branches, PRs and `docs/ephemeral/` artifacts before creating anything.
- An ordinary defect in this instruction returns to this IA through PR-10 (same-owner correction); a corrected instruction is a new version, never an edit of v1.0.
- Abort is only Nathan's manual PR-50 instruction. No agent routes to it.

## 14. Rescope behavior

- **Material** means a change to an approved acceptance intent, a protected architecture, security, data-model or external-contract boundary, several units' scope, an accepted dependency, or budget, schedule or risk needing Product Owner direction. A planned approach found incomplete or impractical is not by itself material.
- Before Proceed, the PR-20 author owns any rescope proposal (RS-10, optional support; RS-30 for revisions), and this IA reviews it through RS-20. The decision returns to the PR-20 planning context. After Proceed, the PR-30 or PR-35 phase records `PR_RETURN_PHASE`: prepublication resumes PR-30 directly; an open PR resumes through RS-40. `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan.
- Expected triggers in this unit (Plan R-1): a real defect needing a non-test or member change; a consumer in §5.5 that must change; more retirements of current-behavior tests than the N2 criterion supports; a lane-runtime cost needing Product Owner direction. A finding that belongs to a later unit's surface (S10 in WU-PR-03, S14 in WU-PR-04) is routed to that unit's owner with evidence, not absorbed here.

## 15. Unresolved items and owners

| Item | Owner | Deadline |
| :- | :- | :- |
| Diagnosis of the 22 undiagnosed sweep failures (§5.2) | PR-20 session | Before the plan reaches `AWAITING_PO_PROCEED` |
| N2 fix-versus-retire criterion and per-file table (§9) | PR-20 session | In the plan |
| Exact `ci.yml` path-filter arrangement and classifier change design | PR-20 session (Plan Templates forbids this instruction inventing YAML) | In the plan |
| Whether `test_gate_auth.py` joins `_HTTP_READER_TEST_OWNERS` (C-2) | PR-20 session | In the plan |
| AQ-1 (S21 ADR) | Nathan / Product Owner | Before WU-PR-07 merges; does not gate this unit |

## 16. Canon-conflict register

`CANON_CONFLICT_REGISTER` carried from the approved Specification and Plan, unchanged:
- **CR-1** (CANON_RECONCILIATION; PF30 record and "CRD Plan" wording versus HDE Governance §9.1.1) — `APPROVED_AS_CHANGED` (Thoth, review v1.0 §6; confirmed review v1.1 §4). Interim: no PF30 entry. Affects no requirement of this unit.
- **CR-2** (CANON_RECONCILIATION; planned units in a Specification) — `APPROVED_AS_CHANGED`. Interim: the Plan, not the Specification, carries units. Affects no requirement of this unit.
- **CR-3** (CANON_RECONCILIATION; "stable CRD ID recorded in PF30") — `APPROVED_AS_CHANGED`. Interim: `HDE-CRD-0002` is the Product Owner-assigned ID; QA root `audit/qa/hde-crd-0002/`. Not touched by this unit.

No new conflict: the canon searched for this unit (§20) is consistent with the Plan's treatment. Drainage stays with the Product Owner.

## 17. Semantic readiness comparison

| Source clause | Intended meaning | Instruction meaning | Owned by | Acceptance | Evidence stage |
| :- | :- | :- | :- | :- | :- |
| S03 intent "No test file runs in no CI lane" | Every tracked `tests/**/test_*.py` is reachable by CI | §5.1 computation returns 0 at the PR head | WU-PR-01 | (1) | PR-30 local; PR-35 CI |
| S03 "each retirement has a recorded reason" | Reason durable in the repository | Ledger plus PR record (EC-3) | WU-PR-01 | (1) | PR-30 |
| S03 "recorded failures and collection errors are fixed or retired with their files" | Nothing retained fails; nothing collected fails | Rules §9.3–§9.8; acceptance (2) | WU-PR-01 | (2) | PR-30; CI |
| S03 constraint "any sweep runs in a throwaway copy" | No tracked rewrite | §5.2 warning; §9.4; validation shape §10 | WU-PR-01 | (2) | PR-30 |
| S04 intent | `.sh` and `.sql` under `tools/qa/` fail without an owner | §4 S04 rule; C-6 | WU-PR-01 | (3) | PR-30; CI rails |
| S05 intent "classifier documentation prefixes" | Paths with no lanes; governed primaries excluded (EC-1) | Eight prefixes with negations for the two primaries, pinned by an Index-reading test | WU-PR-01 | (4) | PR-30; CI rails |
| Plan "All seven lanes green on the exact head" | Exact-head CI | Full validation runs because `ci.yml` and the classifier change | WU-PR-01 | (5) | PR-35 |
| Plan dependency for WU-PR-03 and WU-PR-04 | Their surfaces' tests are covered before they change | C-1, C-2 | WU-PR-01 → WU-PR-03/04 | (1) | PR-40 |
| Plan dependency for WU-PR-06 | Sweep definition and lane lists final | C-3, C-4 | WU-PR-01 → WU-PR-06 | (1), (4) | PR-40 |
| Plan R-1 | Size bounded; RS-10 if enlarged; no skip | §7 bullet 4, §14 | WU-PR-01 | — | PR-20 onward |
| Specification Exclusions and constraint "Release members" | No unneeded re-cut | §7 bullet 1; C-5 | WU-PR-01 | (5) | PR-35 |

Checks made against the full PR-20 contract: its sole substantive input is `PR_INSTRUCTION_ID`; the instruction embeds the Specification, Audit, Plan and review lineage, the PF10 path and the empty overlay set; it states the baseline, loci, exclusions, interfaces, dependencies, acceptance, evidence, migration, security, recovery, rescope, merge ownership and return owner. No decisive comparison fails. Numeric facts (135, 130, 5, 49, 94, 70, 278, 79/523/14, 27) were re-computed or carried from a named tested state, never invented.

## 18. Return owner and next step

- **INSTRUCTION_READY → PR-20 — Create Detailed PR Implementation Plan — 100926.1** (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba), in the dedicated WU-PR-01 PR engineering session (`session_disposition: INITIAL_DEDICATED_ASSIGNMENT`; `role_session_ref: NOT_YET_ASSIGNED`, assigned by Nathan / Product Owner at launch). Sole substantive input: this instruction's repository path.
- **Return to the IA:** PR-40 lineage review after Nathan's merge; rescope review through RS-20; same-owner correction of this instruction through PR-10.
- **Prerequisite:** the pull request carrying this instruction is merged to `main` before PR-20 runs.

## 19. TypeSafe reading for the receiving session (PR-20, WU-PR-01)

Action sent (v6): "Write, as the dedicated PR planning session for the first unit of an approved CRD Implementation Plan, a new detailed PR implementation plan that gives each of 135 test files outside every CI lane (14 that cannot be collected, 37 with 79 failures, 27 tracked files rewritten when run) a planned lane, owner registration, fix or recorded retirement, plus fail-closed classification of unregistered tools/qa shell and SQL sources and a CI skip list aligned with the classifier's eight documentation prefixes while governed primaries stay under CI, in a 1,958-line classifier and a 404-line workflow. It reads the repository and may re-run the uncovered sweep in a throwaway copy; no code is written, no live provider call occurs, and a Product Owner Proceed, implementation, code and security review and an independent lineage review follow."

- **TypeSafe v6: Opus 5.5, extra high.** Effort score 2.76 (confidence 0.59); rung probabilities low 0.00, medium 0.01, high 0.41, extra high 0.43, max 0.11, ultracode 0.04. Model probabilities Fable 5.1 0.27, Opus 5.5 0.73 (confidence 0.46). Twelve cells, computed from the two answers: Opus 5.5 at low 0.00, Opus 5.5 at medium 0.01, Opus 5.5 at high 0.30, Opus 5.5 at extra high 0.31, Opus 5.5 at max 0.08, Opus 5.5 at ultracode 0.03, Fable 5.1 at low 0.00, Fable 5.1 at medium 0.00, Fable 5.1 at high 0.11, Fable 5.1 at extra high 0.12, Fable 5.1 at max 0.03, Fable 5.1 at ultracode 0.01. Flags: boundary between high and extra high. Sent 2026-10-12T21:22:43Z. Nathan picks the cell.
- **Detail:** v6 sent 2026-10-12T21:22:43Z; HTTP 200 in 0.7 s; 4292 input and 54 output tokens; jev-1.13.0. Rung by rule: extra high (nearest to the score, halves up); model by rule: Opus 5.5 (P(most capable) 0.5 or more is Fable 5.1). Flags: boundary between high and extra high.
- **One send**, taken before this artifact was saved. No Notion row was written (PR-10 directs that it is not).
- **Nathan's pick for PR-20:** not stated.
- **Nathan's pick for this PR-10 session:** not stated (the reading for PR-10 is recorded in review v1.1 §6).

**Surface advice:** run PR-20 as a top-level Claude Code cloud session on `amthorn78/glow-hdengine-v2`, with Notion read access, in the dedicated WU-PR-01 PR engineering role. It reads this instruction, the four lineage artifacts, `docs/pfcanon/` on `main`, and `ci/checks/classify_ci_changes.py`, `.github/workflows/ci.yml`, `pytest.ini`, `tests/evidence/test_rails_ci_workflow_integration.py` and the 135 files. It needs Python 3.12 with CI's install and room for one throwaway clone to re-run the uncovered sweep (about three minutes); the sweep must never run in the working tree. It needs no live vendor, production or database access and writes only its plan artifact under `docs/ephemeral/`. The pull request carrying this instruction should be merged to `main` first.

## 20. Prompt-use provenance (GCFPE_PROMPT_USES)

| Field | Value |
| :- | :- |
| usage | HDE-CRD-0002 / PR-10 / WU-PR-01 / instruction 1 |
| change | CRD HDE-CRD-0002 |
| specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, v1.1 (approved) |
| plan | `docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`, v1.1 (approved by review v1.1) |
| work unit / requirements | WU-PR-01; S03, S04, S05 |
| release | GCFPE-20261009.1 / 100926.1 |
| prompt | PR-10 — Create PR Work-Unit Instructions — 100926.1, https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a (retrieved 2026-10-12) |
| role/stage | whole-change IA / PR-10 |
| capture time | 2026-10-12T21:24:08Z |
| execution identity | https://claude.ai/code/session_01WiUd7gGCtJvGgBixQNUjg1 |
| inherited prompt uses | IA-10 (Audit v1.0 front matter), IA-40 (Plan v1.1 front matter), IA-30 (review v1.1 §7) |
| repository persistence | PENDING / NON_GATING: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` does not exist at `a429c7c` (`docs/changes/` holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`), so no installed procedure or writer exists. Recorded here only; owner of any later installation: GCFPE-MGMT-10 and the Product Owner |

PR-20's plan carries this usage reference and the provenance status forward; the write of any provenance record stays subject to an installed procedure and the Product Owner's Proceed.

## Canon relied on

Read on `main` at `a429c7c`; `docs/pfcanon/` is unchanged since `df23bbf` (#614).

- PF04-Canon-HDE-Governance v2.8.7: §9.1.1 role table (the IA issues PR Instructions; approval map); §9.7 "Planning audit posture" (the planning audit is not referenced as execution authority; execution instructions are self-contained and carry execution-critical facts explicitly), path validation methods (Canon-cited, CA vetted, IP Approved with verbatim quotes), file minting with absence proof, and "No fabricated required paths" (read in full, lines 2895–2945).
- PF27-Canon-Plan-Templates v2.0.5: "CI lane classification and automated budget-control discipline" (read in full): smallest correct lane, no invented YAML arrangement, no hiding of failed or unexecuted work behind green.
- PF06-Canon-Change-Process-Guide v2.5.4: §1.0.6 (CI success is not QA acceptance) and §3.5.1 (PR route, each PR self-contained), as applied by the approved Plan and review.
- PF10-HDE-Build-Notes v13.5.2: read in full; addendum 2.1 governs §19 only; silent on S03–S05.
- PF19-Canon-Glow-QA-Guide v3.0.6: "Change-lane QA applicability" (the QA lane follows delivery; no QA artifact in a PR unit), as applied by the Plan.
- `AGENTS.md`: canon-first rule; canon read-only; closed rails; pytest readiness rule; PR description headings; QA output placement; "Code review scope — CI-exempt paths" (the eight prefixes are `_DOCUMENTATION_PREFIXES`); sole Index/Mirror writer; no manual edits to governed artifacts.

Searched without a governing match for this unit: `git grep` of `docs/pfcanon/` on `main` for `paths-ignore`, "uncovered test", "every test file", "quarantin", "retire(d) test" and "PR Instruction" found no clause that conflicts with or adds to the Plan's treatment of S03–S05.

**In-flight documents read in full:** the approved Specification v1.1; the Implementation Plan v1.1; the Plan review v1.1; the Implementation Audit v1.0. Read by section: Plan review v1.0 §4 (N1–N6). **Precedent consulted:** `docs/ephemeral/HDE-EPIC040-PR06b-pr-instruction-v1.0.md` (format). **Prompts read:** PR-10 — Create PR Work-Unit Instructions — 100926.1 (in full); PR-20 — Create Detailed PR Implementation Plan — 100926.1 (in full, receiver contract); the hub `HDE IA — GCFPE-20261009.1 — 100926.1`; the GCFPE Membership and Release Register, current-selection section.

**Repository facts read at `a429c7c`:** `.github/workflows/ci.yml` (lines 1–30, 50–120, all pytest commands); `pytest.ini`; `ci/checks/classify_ci_changes.py` (lines 25–120, 140–182, 283–306, 815–1005, 1170–1232, 1570–1662, 1902–1920); `docs/evidence/INDEX.json` (governed primaries under the eight prefixes; none of the 135 indexed); `tests/evidence/test_rails_ci_workflow_integration.py` (pins named in §5.4); `tools/evidence/regenerate_identity_closure.py` lines 275–290 and 372–382; `git grep` of the 135 paths (§5.5); `tools/qa/` listing; absence of `tests/retired_tests.md`; `docs/changes/` listing. The inventory in §5.1 was re-computed by importing the classifier read-only; the import's bytecode cache was removed afterwards and the tree left clean.

---

**State:** `INSTRUCTION_READY` — PR work-unit instruction v1.0 for HDE-CRD-0002 WU-PR-01, issued by the whole-change IA under PR-10 from approved Plan v1.1; next: PR-20 in the dedicated WU-PR-01 session.
