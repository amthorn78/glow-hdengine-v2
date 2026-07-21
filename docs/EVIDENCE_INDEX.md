> **Note:** The canonical human Evidence Index lives at `docs/evidence/INDEX.json`.
> Add new entries there first, then mirror key pointers here for quick navigation. Update the skeleton (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` + `.path_proof.txt` companions) in the same PR whenever governed bytes change.

## HDE-EPIC037 evidence navigation

- PR-01 field sufficiency: `artifacts/vendor/hdapi_v2/hde_epic037_field_sufficiency_proof.json`, `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract.snapshot.json`, `artifacts/vendor/hdapi_v2/hde_epic037_adapter_contract_nonclaims.json`, `audit/docdeltas/hde-epic037_doc_deltas.md`, and `audit/qa/hde-epic037/00_meta/doc_deltas.md`.
- PR-02 deterministic v2 ChartResult adapter mapping: `artifacts/vendor/hdapi_v2/hde_epic037_adapter_mapping.snapshot.json`, `artifacts/vendor/hdapi_v2/hde_epic037_adapter_negative_fixtures.json`, `artifacts/vendor/hdapi_v2/hde_epic037_no_raw_payload_persistence.json`, and `artifacts/vendor/hdapi_v2/hde_epic037_public_reader_no_change.json`.
- PR-03 configured-v2 bg:resolve dry-run route/request/closed-rails/legacy-fallback evidence: `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_v2_route_policy.snapshot.json`, `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_request_shape.snapshot.json`, `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_closed_rails_no_io.json`, and `artifacts/vendor/hdapi_v2/hde_epic037_bg_resolve_legacy_fallback.snapshot.json`.
- PR-04 mapped v2-to-compat evidence: `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_proof.json`, `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_two_run.json`, `artifacts/vendor/hdapi_v2/hde_epic037_v2_to_compat_pair_order.json`, and `artifacts/vendor/hdapi_v2/hde_epic037_admin_public_boundary.json`.
- OPS-01 PO-produced bounded open-rails smoke evidence: `audit/ops/hde-epic037/ops-hde-epic037-001/commands.txt`, `stdout.log`, `stderr.log`, `exit_codes.txt`, `env_presence_redacted.json`, `request_summary.json`, `result_summary.json`, `adapter_mapping_result_summary.json`, `compat_path_result_summary.json`, `failure_classification.json`, `files_sha256.txt`, and QA pointer `audit/qa/hde-epic037/ops-hde-epic037-001/ops_evidence_pointer.md`.
- PR-05 parent binding: `docs/acceptance_map_epic037.json`, `audit/qa/hde-epic037/token_evidence_matrix.md`, `audit/qa/hde-epic037/acceptance_map_viability.log`, `audit/qa/hde-epic037/parent_evidence_binding.log`, `audit/docdeltas/hde-epic037_pr05_parent_binding_doc_deltas.md`, and `audit/qa/hde-epic037/00_meta/pr05_parent_binding_doc_deltas.md`.
- Nonclaim boundary: `parent_posture=supportable_to_done` is a later-drain support statement only; EPIC037 evidence does not claim QA PASS, OPS completion by PR work, PF09 status movement/drainage, PO closeout, board update, production deployment, epic closeout, broad HumanDesignAPI v2 platform conformance, public Reader or public route/flag/payload/transport change, new HTTP home, app-side HumanDesignAPI ownership, raw secret/request/response/vendor payload persistence, or AI scope.

## Historical HDE-EPIC036 evidence navigation

- PR-01 route-policy classification: `audit/qa/hde-epic036/route_policy_decision.log`, `artifacts/vendor/hdapi_v2/bg_resolve_route_policy.snapshot.json`, `artifacts/vendor/hdapi_v2/bg_resolve_bodygraph_detail_proof.json`, `artifacts/vendor/hdapi_v2/bg_resolve_runtime_nonclaims.json`, `artifacts/vendor/hdapi_v2/bg_resolve_request_shape.snapshot.json`, and `artifacts/vendor/hdapi_v2/bg_resolve_policy_binding.snapshot.json`.
- PR-02 evidence-loop binding: `docs/acceptance_map_epic036.json`, `audit/qa/hde-epic036/token_evidence_matrix.md`, `audit/qa/hde-epic036/acceptance_map_viability.log`, `audit/docdeltas/hde-epic036_doc_deltas.md`, and `audit/qa/hde-epic036/00_meta/doc_deltas.md`.
- Route-policy posture: configured v2 bases select `unsupported_runtime_nonclaim` for `hdctl bg:resolve --source vendor` before any legacy `bodygraphs` request is constructed; non-v2 configured bases preserve explicit legacy BodyGraph fallback. Closed-rails refusal remains earlier than route-policy logic.
- Scope guardrails: this evidence supports HDE-FERM008.6 for later PF09.5 HDE Build Checklist Fermentation drainage only. It does not claim QA PASS, OPS completion, OPS execution, live vendor observation, PF09.5 status movement, HDE-FERM008 parent Done, epic closeout, full HumanDesignAPI v2 runtime conformance, public Reader change, public route/flag/payload/transport change, new HTTP home, app-side credential ownership, raw payload persistence, or AI scope.

## HDE-EPIC034 evidence navigation

- Source selection / v1 legacy isolation: `audit/qa/hde-epic034/pr-01/source_selection_check.log`, `artifacts/vendor/hdapi_v2/source_selection.snapshot.json`, and `artifacts/vendor/hdapi_v2/v1_legacy_guard.log`.
- Request shaping and auth/base-url posture: `audit/qa/hde-epic034/pr-02/request_shaping_check.log` and `artifacts/vendor/hdapi_v2/request_shaping.snapshot.json`; `HD_API_BASE_URL` owns the versioned base URL while route resources remain version-neutral.
- Response-envelope mapping and adapter boundary proof: `audit/qa/hde-epic034/pr-03/response_mapping_check.log`, `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json`, `audit/qa/hde-epic034/pr-04/boundary_check.log`, and `artifacts/vendor/hdapi_v2/adapter_boundary_proof.log`.
- Closed-rails deterministic shaping/refusal and PR-06 OPS-02 binding: `audit/qa/hde-epic034/pr-05/closed_rails_check.log`, `artifacts/vendor/hdapi_v2/closed_rails_refusal.txt`, `audit/qa/hde-epic034/pr-06/ops_smoke_evidence_binding.log`, and retained OPS-02 evidence under `audit/ops/hde-epic034/ops-02/`.
- Acceptance/doc-delta anchors: `docs/acceptance_map_epic034.json`, `audit/docdeltas/hde-epic034_doc_deltas.md`, and `audit/qa/hde-epic034/00_meta/doc_deltas.md`. OPS-02 / PR-06 supports HDE-FERM008.2 only; it does not claim HDE-FERM008 parent completion, later HDE-FERM008 subtasks, full HumanDesignAPI v2 runtime conformance, public Reader changes, new HTTP homes, OPS execution by docs agents, or AI scope.

> Refresh order: run `python tools/evidence/update_evidence_index.py` (write) before `python tools/evidence/orientation_demo.py` (write), then their `--check` variants, and finish with `ci/checks/check_mirror_schema.sh`. Mirror path proofs include both `sha256` and `mirror_body_sha256` for the self-record entry in `artifacts/evidence_index.jsonl`.

# Appendix-D — Evidence Index (EPIC-037 + historical pointers)

## EPIC033 contract-inventory evidence family (PR-01, not runtime conformance)
* Contract inventory artifacts: `artifacts/vendor/hdapi_v2/source_inventory.json`, `artifacts/vendor/hdapi_v2/source_inventory.md`, `artifacts/vendor/hdapi_v2/openapi_validation.log`, `artifacts/vendor/hdapi_v2/known_anomalies.md`, `artifacts/vendor/hdapi_v2/endpoint_reference.csv`, and `artifacts/vendor/hdapi_v2/contract_map.json`. Each governed artifact has a sibling `.path_proof.txt`.
* Source-cache inputs: `artifacts/vendor/hdapi_v2/source_cache/` contains the cached public documentation inputs used by the default closed-rails replay, including `v2-routes.yaml`, `v1-routes.yaml`, `api-reference.openapi.json`, `llms_txt.body`, and `llms-full.endpoint-tiers.txt`.
* Acceptance and QA pointers: `docs/acceptance_map_epic033.json`, `audit/qa/hde-epic033/token_evidence_matrix.md`, `audit/qa/hde-epic033/acceptance_map_viability.log`, `audit/docdeltas/hde-epic033_doc_deltas.md`, and `audit/qa/hde-epic033/00_meta/doc_deltas.md`.
* Generator posture: `python tools/evidence/generate_hdapi_v2_contract_inventory.py` is the governed generator; default generation is closed-rails source-cache replay. Public documentation refresh uses `python tools/evidence/generate_hdapi_v2_contract_inventory.py --refresh-public-docs` with `SAFE_MODE=0` and `ALLOW_NETWORK=1`; this is not credentialed runtime vendor smoke.
* Scope guardrails: inventory only for HDE-FERM006.1 through HDE-FERM006.4; no runtime v2 request shaping, source selection, live conformance, public Reader change, open-rails vendor smoke, new HTTP home, vendor-v2-specific acceptance token, or AI scope is claimed. HDE-FERM007 and HDE-FERM008 remain follow-up/out of scope. The current inventory quarantines suspect `api-reference/openapi.json` and treats `llms.txt` / `llms-full.txt` as documentation-discovery-only context.

## EPIC031 SAFE rails evidence families (implementation slice, not close-pack)
* PR-01 provider-gate policy: `audit/qa/hde-epic031/pr-01/open_rails_policy_proof.json`, `audit/qa/hde-epic031/pr-01/retry_backoff_429_proof.json`, `audit/qa/hde-epic031/pr-01/closed_default_open_exception_rails.json`, plus supporting policy artifacts `artifacts/vendor/policies_pinned.md` and `artifacts/vendor/retry_after_parse.log`.
* PR-02 keys-only vendor log posture: `audit/qa/hde-epic031/pr-02/vendor_keys_only.sample.jsonl`, `audit/qa/hde-epic031/pr-02/vendor_rails_scope.txt`, `audit/qa/hde-epic031/pr-02/keys_only_log_redaction.json`, `audit/qa/hde-epic031/pr-02/bounded_label_observability.json`, and `audit/qa/hde-epic031/pr-02/secret_redaction_scan.log`. These are vendor-specific evidence files and are separate from historical DB-bridge artifacts under `artifacts/logs/` and `artifacts/ops/`.
* PR-03 evidence/index coherence: `audit/qa/hde-epic031/pr-03/evidence_family_map.json`, `audit/qa/hde-epic031/pr-03/safe_rails_evidence_coherence.json`, and `audit/qa/hde-epic031/pr-03/evidence_refresh.log`.
* Scope guardrails: the PR-03 coherence artifact records no new acceptance tokens, no follow-up HDAPI v2 scope implementation, no live vendor call, and no public Reader contract change.
* Path-proof discipline: each EPIC031 artifact above has a sibling `.path_proof.txt`; Index/Mirror entries are in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`.
* Repo-supported validation references include `ci/jobs/rails_closed_refusal.yml`, `ci/jobs/rails_open_conformance.yml`, `ci/jobs/logs_keys_only_redaction.yml`, `python tools/evidence/generate_epic031_pr02_log_posture.py --check`, `python tools/evidence/generate_epic031_pr03_evidence_coherence.py --check`, `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `python tools/evidence/validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_evidence_index_hash.sh`, and `python tools/evidence/check_lf_endings.py`.

## EPIC030 PR-slice evidence families (implementation closure, not close-pack)
* PR-01 normalization: `audit/qa/hde-epic030/pr-01/zero_weight_handoff.json`, `audit/qa/hde-epic030/pr-01/invalid_viewer_prefs.log`, `audit/qa/hde-epic030/pr-01/normalization_canonical_compare.log`
* PR-02 dev sampler harness: `audit/qa/hde-epic030/pr-02/dev_sampler_http_headers.txt`, `audit/qa/hde-epic030/pr-02/dev_sampler_http_body.json`, `audit/qa/hde-epic030/pr-02/dev_sampler_seed_only.json`, `audit/qa/hde-epic030/pr-02/dev_sampler_two_run_identity.json`
* PR-03 compat bindings: `audit/qa/hde-epic030/pr-03/category_order_binding.log`, `audit/qa/hde-epic030/pr-03/compat_identity_binding.log`, `audit/qa/hde-epic030/pr-03/compat_parity_binding.log`
* PR-04 band-threshold/tuning bindings: `audit/qa/hde-epic030/pr-04/band_edges_binding.log`, `audit/qa/hde-epic030/pr-04/band_thresholds_diff.json`, `audit/qa/hde-epic030/pr-04/band_thresholds_identity_hash.txt`
* PR-05 category-framework closure: `audit/qa/hde-epic030/pr-05/per_channel_mechanics.json`, `audit/qa/hde-epic030/pr-05/category_canonical_compare.log`, `audit/qa/hde-epic030/pr-05/category_framework_binding.log`
* Path-proof discipline: each EPIC030 PR-slice artifact above has a sibling `.path_proof.txt`; index/mirror entries are in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`.

## Historical EPIC027 QA ledger and close-pack (not EPIC030 outputs)
* Acceptance map: `docs/acceptance_map_epic027.json`
* Token matrix: `audit/qa/hde-epic027/token_evidence_matrix.md`
* Acceptance-map viability: `audit/qa/hde-epic027/acceptance_map_viability.log`
* Per-check logs: `audit/qa/hde-epic027/checks/<check_id>/primary.log`
* Close-pack artifacts: `audit/EPIC-027_MANIFEST.json`, `audit/EPIC-027_close_report.md`

## Endpoint catalog + A7 proofs (/reader)
* Endpoint catalog: `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`
* Env-gate proof: `artifacts/proofs/endpoints_env_gate_proof.log`
* Success headers: `artifacts/proofs/success_get.txt`, `artifacts/proofs/success_head.txt`
* 304 posture: `artifacts/proofs/success_304.txt`
* Writer/error posture: `artifacts/proofs/success_writers_errors.txt`
* Encoding invariance: `artifacts/proofs/encoding_invariance.txt`
* Proof generator: `tests/http/test_reader_a7_transport.py` (set `HDE_WRITE_A7_PROOFS=1` to emit artifacts under `artifacts/proofs/`).

## Conjunction CLI artifacts (EPIC026)
* Pair fixtures and captures: `artifacts/audit/cli/pair.json`, `artifacts/audit/cli/pair_ba.json`, `artifacts/audit/cli/showcompat_ab.json`, `artifacts/audit/cli/showcompat_ba.json`
* Determinism/parity logs: `artifacts/audit/cli/ab_ba_compare.log`, `artifacts/audit/cli/two_run_identity.log`, `artifacts/audit/cli/det1_compare.log`
* Sidecar artifact: `artifacts/cli/abba_sidecar.json` (plus `.sha256` + `.path_proof.txt`)

## Compat identity-hash + writer/readback artifacts (EPIC027)
* Compat identity hash: `artifacts/compat/identity_hash.txt`
* Writer readback log: `artifacts/writer/conjunction_write_readback.log`
* Writer summary: `artifacts/writer/conjunction_writer_summary.json`
* Generator posture: `python tools/evidence/generate_conjunction_writer_evidence.py` requires explicit open rails from the caller (`SAFE_MODE=0` and `ALLOW_NETWORK=1`) when resolver/provider acquisition is needed.

## CLI installability/help/version artifacts (EPIC027)
* Installability summary: `artifacts/cli/install/installability_summary.json`
* Entrypoints proof: `artifacts/cli/install/entrypoints.txt`
* Help captures: `artifacts/cli/help/hdctl_help.txt`, `artifacts/cli/help/showcompat_help.txt`
* Generator: `python tools/cli/generate_cli_conformance_artifacts.py`

## CLI showcompat capture + guards
* Showcompat stdout bytes: `artifacts/cli/showcompat/stdout.json`
* Showcompat stdout sha256: `artifacts/cli/showcompat/stdout.json.sha256`
* Showcompat args/env record: `artifacts/cli/showcompat/args.json`
* Serializer guard log: `artifacts/cli/guards/serializer_grep_guard.log`

## Canonical JSON gate (closed rails)
* Gate runner: `python tools/evidence/run_canonical_json_gate.py` (`--check-only` available for read-only validation)
* Check log: `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`
* Compare log: `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`
* Structured record: `audit/gates/json_gate/canonical/json_gate_structured_record.json`
* All gate artifacts have co-located `.path_proof.txt` siblings and are enforced in CI (see `.github/workflows/ci.yml` step “Run canonical JSON gate (closed rails)”). The legacy catalog check report remains at `audit/gates/canonical_json/json_canonical_check.log`.

## Evidence index snapshot gate (closed rails)
* Gate runner: `python tools/evidence/generate_evidence_index_snapshot.py` (use `--check` for read-only validation)
* Snapshot artifact: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`
* Path proof: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`
* Validation behavior: RFC3339 UTC validation for `generated_at_utc`, and non-object JSONL lines in the mirror fail validation (see `python -m pytest tests/evidence/test_evidence_index_snapshot.py`).

## Evidence-paths + LF endings gates
* Path validation runner: `python tools/evidence/validate_evidence_paths.py`
* LF endings runner: `python tools/evidence/check_lf_endings.py`
* QA logs: `audit/qa/hde-epic027/checks/gate_evidence_paths_validation/primary.log`, `audit/qa/hde-epic027/checks/gate_lf_endings/primary.log`

## Arrays-as-sets evidence
* Report artifact: `artifacts/canonical/arrays_as_sets_report.log`
* Generator: `python tools/evidence/generate_arrays_as_sets_report.py`
* Proof test: `python -m pytest tests/compare/test_arrays_as_sets.py`

# Appendix-D — Evidence Index (EPIC-022)

## Close-pack and acceptance bindings
* Close-pack artifacts are complete: `audit/EPIC-022_MANIFEST.json`, `audit/EPIC-022_close_report.md`, `audit/qa/hde-epic022/token_evidence_matrix.md`, `docs/acceptance_map_epic022.json`.
* Env pins and current sanity pipeline authority: `audit/gates/determinism/env_pins.log` (+ `.path_proof.txt`), `audit/gates/sanity_pipeline/sanity_pipeline.log` (+ `.path_proof.txt`). `artifacts/sanity/sanity.log` remains only as historical, unbound close-pack material and is not refreshed.

## CLI stream discipline and showcompat capture (D2)
* Deterministic capture generator: `tools/cli/generate_showcompat_artifacts.py`
* Stdout bytes: `artifacts/cli/showcompat/stdout.json`
* Stdout sha256 sidecar: `artifacts/cli/showcompat/stdout.json.sha256`
* Args/env record: `artifacts/cli/showcompat/args.json`
* Evidence Index + sentinel: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`
* Machine mirror: `artifacts/evidence_index.jsonl`

## Error-envelope parity and env pins (D1)
* Env pins gate: `ci/checks/check_env_pins.sh`; log and proof under `audit/gates/determinism/env_pins.log` and `.path_proof.txt`
* Closed-rails refusal parity: `parity/errors_reader_cli.db_unavailable.{cli.txt,http.json}` and `parity/errors_reader_cli.vendor_attempt_closed_rails.{cli.txt,http.json}` (all with `.path_proof.txt` siblings)
* CLI/Reader error parity harness: `tests/cli/test_errors_parity.py::test_http_and_cli_parity` validates both scenarios
* Acceptance scaffolding: `docs/acceptance_map_epic022.json`, `audit/qa/hde-epic022/token_evidence_matrix.md`, `audit/EPIC-022_MANIFEST.json`, `audit/EPIC-022_close_report.md`

## /internal/version identity bundle (D3)
* Body and sha sidecar: `artifacts/ops/internal_version/body_get.json`, `artifacts/ops/internal_version/body_get.sha256`
* Headers: `artifacts/ops/internal_version/headers_get.txt`, `artifacts/ops/internal_version/headers_head.txt`, `artifacts/ops/internal_version/headers_cond_if_none_match.txt`, `artifacts/ops/internal_version/headers_cond_if_modified_since.txt`
* Two-run identity log: `artifacts/ops/internal_version/two_run_identity.log`
* Freeze-Pack SoT and schema: `catalog/manifest.json` (top-level keys exactly `root`, `version`, `built_at_utc`, `files`; no self-listing) with canonical bytes (UTF-8, ASCII-sorted keys, compact separators, one trailing `\n`); `release_id = sha256(canonical_bytes(catalog/manifest.json))`.
* Evidence copy and evidence-only summaries: `artifacts/math/freeze_pack_manifest.json` is byte-identical to the SoT; `artifacts/math/manifest_snapshot.json` is evidence-only (not an identity input). Alternate manifest-like artifacts must be quarantined under different names/paths.
* Supporting identity artifacts (must exist and be non-empty): `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`, `artifacts/math/manifest_snapshot.json`, `artifacts/proofs/env_pins.txt`.
* Validation entrypoints (closed rails; Python entrypoints in CI): `python scripts/release_id_recompute.py --check`, `python ci/checks/check_release_identity.sh` (runs the recompute check, schema/bytes validation, and evidence presence), and `python tools/evidence/run_sanity_pipeline.py` (runs the gate alongside other deterministic checks). `--check` is read-only and fails if any governed release artifact differs from deterministic expected bytes.
* All governed with `.path_proof.txt` siblings and indexed in `docs/evidence/INDEX.json` / `artifacts/evidence_index.jsonl`
* Known canon mismatch: PF20 references a provenance note for D3, while implementation follows the PF10 posture via the governed two-run/coupling log as the provenance proof.

# Appendix-D — Evidence Index (EPIC-021)

## Registry report and sanity pipeline
* `artifacts/registry/registry_report.json` (generated by `tools/generate_registry_report.py`)
* `artifacts/registry/registry_report.json.path_proof.txt`
* `audit/gates/sanity_pipeline/sanity_pipeline.log`
* `audit/gates/sanity_pipeline/sanity_pipeline.log.path_proof.txt`
* Historical material only: `artifacts/sanity/sanity.log` (+ `.path_proof.txt`) is not refreshed and is not indexed as `sanity.pipeline.log`.
* Evidence Index + sentinel: `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`
* Machine mirror: `artifacts/evidence_index.jsonl`

## QA harness (EPIC021)
* QA_ROOT bootstrap: `audit/qa/hde-epic021/test_tooling_bootstrap.log`
* Per-run bootstrap log: `audit/qa/hde-epic021/<run-id>/D0_bootstrap.log`
* QA step manifest: `audit/qa/hde-epic021/qa_step_logs_manifest.json`
* Acceptance-map viability: `audit/qa/hde-epic021/acceptance_map_viability.log`
* Token evidence matrix: `audit/qa/hde-epic021/token_evidence_matrix.md`

# Appendix-D — Evidence Index (EPIC-020)

## Error envelopes and parity
* `errors/` canonical error envelopes (typed tokens, `error_v1` schema)
* `parity/` error parity harness outputs and schema checks

## Presenter identity
* `artifacts/presenter/showcompat_ab.bytes` (AB)
* `artifacts/presenter/showcompat_ba.bytes` (BA)
* `artifacts/presenter/reader_cli_parity.bytes`
* `artifacts/presenter/showcompat_identity_summary.json`
* `artifacts/presenter/preimage_recompute.log`

## Internal identity (`/internal/version`)
* `artifacts/ops/internal_version/body_get.json`
* `artifacts/ops/internal_version/body_get.sha256`
* `artifacts/ops/internal_version/headers_get.txt`
* `artifacts/ops/internal_version/headers_head.txt`
* `artifacts/ops/internal_version/two_run_identity.log`
* `artifacts/math/release_id.txt`

## Rails and env pins
* `audit/gates/determinism/env_pins.log`
* EPIC020 QA checklist: `docs/QA_CHECKLIST_EPIC020.md`

# Appendix-D — Evidence Index (EPIC-017)

## Close-out artifacts
* Manifest: `audit/EPIC017_MANIFEST.json` (token→artifact map)
* Close report: `audit/EPIC017_close_report.md`
* Acceptance map: `docs/acceptance_map_epic017.json`
* PF doc-deltas: `audit/docdeltas/` (PF09, PF10, PF12, PF14, PF19, PF20, PF04)

## Canonical compatibility & ordering
* `artifacts/cli/summary.json`, `artifacts/cli/ab.json`, `artifacts/cli/ba.json`
* `artifacts/cli/reader_cli_parity.json` (parity harness)
* `artifacts/cli/preimage_recompute.log`
* `artifacts/engine/order/props_total_order.log` (deterministic ordering)
* `artifacts/engine/order/abba_identity.bytes`

## Registry and evidence ledger
* `artifacts/registry/registry_report.json`
* `artifacts/evidence_index.jsonl` (machine mirror self-record)
* `topology.orientation_demo` under `artifacts/gates/` (path-proof exemplar)

---

# Appendix-D — Evidence Index (EPIC-011)

## Historical bridge adapter evidence
* `artifacts/db_bridge/adapter_selection.snapshot.json` — historical; does not prove current runtime support.
* `artifacts/db_bridge/health.json` — historical; does not prove current runtime support.
* `artifacts/db_bridge/root.json` — historical; does not prove current runtime support.
* `artifacts/db_bridge/query_select_1.json` — historical; does not prove current runtime support.

## Current direct DB posture & rails-open scope
* `artifacts/db/introspect.search_path.json`
* `artifacts/db/introspect.grants.json`
* `artifacts/db/introspect.fingerprint.json`
* `artifacts/engine/db_adapter.version.json`
* `artifacts/engine/db_adapter.search_path.json`
* `artifacts/engine/db_adapter.fingerprint.json`
* `artifacts/logs/keys_only.sample.jsonl`
* `artifacts/ops/rails_open_scope.txt`

## Env-matrix (selection-only)
* `artifacts/runtime/env_matrix.snapshot.json`
* `artifacts/runtime/env_matrix.diff.json`
* `artifacts/runtime/env_matrix.prev.json`

## Indices & proofs (PF12)
* `docs/evidence/INDEX.json`
* `docs/evidence/INDEX.sha256`
* `artifacts/evidence_index.jsonl`
* `*.path_proof.txt` siblings for every governed artifact

## Ops rails refusal (historical)
* `artifacts/ops/rails_refusal_proof.txt`
* `artifacts/ops/no_io_guard.txt`

## Aux Narrative (EPIC-010)
* `audit/gates/narratives/keys_10x4.table.json`
* `tests/transport/headers/aux_text_200.snap`
* `tests/transport/headers/aux_suppression_200.snap`

## QA Runs (EPIC-009)
* `artifacts/qa/epic009_precommit_report.json`

---

# Appendix-D — Evidence Index (EPIC-007)
## Step6
* `artifacts/epic007/ACCEPTANCE_NOTE.txt` — bytes: 79, sha256: 29567dac1cba71373a9eaa3125e4bce8118b4e62f8e94469317fecc229c6d2a0, added_in: EPIC007/Step6
* `artifacts/epic007/CLOSE_NOTE.txt` — bytes: 295, sha256: 911e6bfe3618a427f9602f34f75c9539b2aa15fc17d02642be7a41b3725d18a3, added_in: EPIC007/Step6

## Admin-QA
* `artifacts/admin/qa/M10_AB.json` — bytes: 1672, sha256: 2a6d96226a71c600b1d7eb38f4830d114fc6580f36cd41724576bcd2b7b84f09, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_BA.json` — bytes: 1672, sha256: d5f9955ad726086e469d9c5bc4fb086edf11e0016ad568c0054a5e8f68a0ca02, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/Composite_AB.json` — bytes: 1348, sha256: 361211e377e35e5d1257b99fc3692dbe9aa0186226839b356fd32dfa82266695, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_scores.csv` — bytes: 662, sha256: cbe5f03db6a914ecf2d6cd597a530fb4ffc7eb330826019ea3e207f705ea5c5e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_reader_AB.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_reader_BA.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_cli_AB.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/public_cli_BA.json` — bytes: 314, sha256: cd9c054901e6dec7b8d92ad9a03ab8f4c9ee8f0220c4b4d191eca6ca50b2864e, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_AB.idempotence.sha256` — bytes: 65, sha256: f3c76a76460bcea5145fe3bf09b224a5c9257912cdb5e0f8bae97e13845cc1ef, added_in: EPIC007/Admin-QA
* `artifacts/admin/qa/M10_BA.idempotence.sha256` — bytes: 65, sha256: f3c76a76460bcea5145fe3bf09b224a5c9257912cdb5e0f8bae97e13845cc1ef, added_in: EPIC007/Admin-QA

## Step5
* `proofs/AB_BA_PARITY.txt` — bytes: 16, sha256: 7a7771ab8f5279a3bcde8b103d6ecaddd01a342b1c7dc870f5479aee894a00dd, added_in: EPIC007/Step5
* `proofs/TWO_RUN_IDENTITY.txt` — bytes: 20, sha256: b171a2d116394deebe5518f5f22c56b9073e681ae02dea22d3962f0873d408de, added_in: EPIC007/Step5

## Step3
* `artifacts/m10/thresholds_edge_cases.txt` — bytes: 471, sha256: 4279a194ff980dd90a95aff371fff26b0ce518e28bb53292972fc7d6b16a3fe2, added_in: EPIC007/Step3

## Step4
* `proofs/HELP_OK.txt` — bytes: 37, sha256: 644df560f3493b7f39888a6736f1b2a4592c55242c90da98d2be8b9a726adbd7, added_in: EPIC007/Step4
* `proofs/SERIALIZER_GUARD.txt` — bytes: 18, sha256: eaaa46f94c37817dc93a7d6e831c0a9bb32227053b6d67fd69344e5bf7a2a636, added_in: EPIC007/Step4
* `proofs/SUCCESS_SHAPE.txt` — bytes: 28, sha256: 1f3e4ca57e3515506702dfdad8610a406f7a33d39abbacb3c1067fe659056676, added_in: EPIC007/Step4
* `proofs/READER_CLI_PARITY.txt` — bytes: 28, sha256: de5004f9eaceae9f195410efbc3dcb70f5a4711a702afda7876adc649c4b231a, added_in: EPIC007/Step4

## Step2B
* `catalog/magic10_caps.json` — bytes: 900, sha256: ecd1f536717fc8ff32cd30cde7a2e6164a58effdd1c63ba67429985cba61b05b, added_in: EPIC007/Step2B
* `catalog/magic10_seeds.json` — bytes: 357, sha256: 446ca6dcbe3d25286e40f9acbac6f492d36eb7416280f0c29a3ff43cacac5b45, added_in: EPIC007/Step2B
* `catalog/manifest.json` — bytes: 1000, sha256: 47f42d29fb4e1196691f3dae28cfc0fa04ce5504e2511cd27eca9e325fe88921, added_in: EPIC007/Step2B
* `artifacts/math/release_id.txt` — bytes: 65, sha256: 7810de3f2201a8f30874af3dc2ac226a1ef13f2a75b64c3a1a2c7c97a72c867e, added_in: EPIC007/Step2B

## Step2A
* `catalog/magic10.json` — bytes: 124, sha256: ef4ec8dd591294f15ca870f038678116b7932782023301fd8885b1a870b07e64, added_in: EPIC007/Step2A
* `math/thresholds.json` — bytes: 82, sha256: 2148630897b32d037ce244a8602a5d8c811441d21c0ad47be9ebb1379d1d9185, added_in: EPIC007/Step2A

# Appendix-D — Evidence Index (EPIC-006)
**Transport — `/internal/version` (headers-only proofs)**
* `artifacts/proofs/internal_version_headers.json`
* `artifacts/proofs/internal_version_headers.txt`
**CLI proofs**
* `artifacts/proofs/cli_install.txt`
* `artifacts/proofs/cli_implemented_set.txt`
* `artifacts/proofs/cli_grep_guard.txt`
* `artifacts/proofs/cli_reader_parity.txt`
**QA artifacts**
* `artifacts/qa/cli/pair.reader.json`
* `artifacts/qa/cli/pair.reader.json.sha256`
* `artifacts/admin/qa/pair.left.bodygraph.json`
* `artifacts/admin/qa/pair.left.bodygraph.json.sha256`
* `artifacts/admin/qa/pair.right.bodygraph.json`
* `artifacts/admin/qa/pair.right.bodygraph.json.sha256`
* `artifacts/admin/qa/pair.composite.bodygraph.json`
* `artifacts/admin/qa/pair.composite.bodygraph.json.sha256`
* `artifacts/admin/qa/pair.compat.proof.json`
* `artifacts/admin/qa/pair.compat.proof.json.sha256`
**Mechanics**
* `artifacts/mech/constants_snapshot.json`
* `artifacts/mech/ordering_examples.jsonl`
* `artifacts/mech/identity_hash.txt`
**Identity & Math**
* `artifacts/identity/service_identity.json`
* `artifacts/math/release_id.txt`
* `artifacts/math/release_id_recompute.log`
* `artifacts/identity/emitter_sha256.txt`
**Database (present but out of scope)**
* `artifacts/db/conn_env.txt`
* `artifacts/db/attempts.json`
* `artifacts/db/check_schema.txt`
* `artifacts/db/grants.txt`
* `artifacts/db/rw_smoke.txt`
* `artifacts/db/read_guards.txt`
* `artifacts/db/check_constraints.txt`
* `artifacts/db/partition_plan.txt`
* `artifacts/db/ddl_applied.sql`
* `artifacts/ddl/DDL_BASELINE.sql`
**Ops pins**
* `artifacts/validation/service_cmd.txt`
* `artifacts/prod/exposure_note.md`

---

# Appendix-D — Evidence Index (EPIC-005, historical)

**Transport — `/internal/version`**

* `artifacts/headers/internal_version_200.txt`
* `artifacts/headers/internal_version_head.txt`
* `artifacts/headers/internal_version_if_none_match.txt`
* `artifacts/headers/internal_version_override_denied.txt`

**Identity & Math**

* `artifacts/identity/service_identity.json`
* `artifacts/math/release_id.txt`
* `artifacts/math/release_id_recompute.log`
* `artifacts/identity/emitter_sha256.txt`

**Database**

* `artifacts/db/ddl_applied.sql`
* `artifacts/db/check_schema.txt`
* `artifacts/db/check_constraints.txt`
* `artifacts/db/partition_plan.txt`
* `artifacts/db/grants.txt`

**Ops pins**

* `artifacts/validation/service_cmd.txt`
* `artifacts/prod/exposure_note.md`
