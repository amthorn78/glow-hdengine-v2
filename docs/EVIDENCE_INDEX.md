> **Note:** The canonical human Evidence Index lives at `docs/evidence/INDEX.json`.
> Add new entries there first, then mirror key pointers here for quick navigation. Update the skeleton (`docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl` + `.path_proof.txt`) in the same PR whenever governed bytes change.
> Refresh order: run `python tools/evidence/update_evidence_index.py` (write) before `python tools/evidence/orientation_demo.py` (write), then their `--check` variants, and finish with `ci/checks/check_mirror_schema.sh`. Mirror path proofs include both `sha256` and `mirror_body_sha256` for the self-record entry in `artifacts/evidence_index.jsonl`.

# Appendix-D — Evidence Index (EPIC-025)

## QA ledger and close-pack
* QA step manifest: `audit/qa/hde-epic025/qa_step_logs_manifest.json`
* Per-check logs: `audit/qa/hde-epic025/checks/<check_id>/primary.log`
* Close-pack artifacts: `audit/EPIC-025_MANIFEST.json`, `audit/EPIC-025_close_report.md`
* Doc deltas: `audit/docdeltas/hde-epic025_doc_deltas.md`

## Endpoint catalog + A7 proofs (/reader)
* Endpoint catalog: `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`
* Env-gate proof: `artifacts/proofs/endpoints_env_gate_proof.log`
* Success headers: `artifacts/proofs/success_get.txt`, `artifacts/proofs/success_head.txt`
* 304 posture: `artifacts/proofs/success_304.txt`
* Writer/error posture: `artifacts/proofs/success_writers_errors.txt`
* Encoding invariance: `artifacts/proofs/encoding_invariance.txt`
* Proof generator: `tests/http/test_reader_a7_transport.py` (set `HDE_WRITE_A7_PROOFS=1` to emit artifacts under `artifacts/proofs/`).

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
* QA logs: `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`, `audit/qa/hde-epic025/checks/gate_lf_endings/primary.log`

## Arrays-as-sets evidence
* Report artifact: `artifacts/canonical/arrays_as_sets_report.log`
* Generator: `python tools/evidence/generate_arrays_as_sets_report.py`
* Proof test: `python -m pytest tests/compare/test_arrays_as_sets.py`

# Appendix-D — Evidence Index (EPIC-022)

## Close-pack and acceptance bindings
* Close-pack artifacts are complete: `audit/EPIC-022_MANIFEST.json`, `audit/EPIC-022_close_report.md`, `audit/qa/hde-epic022/token_evidence_matrix.md`, `docs/acceptance_map_epic022.json`.
* Env pins and sanity pipeline: `audit/gates/determinism/env_pins.log` (+ `.path_proof.txt`), `artifacts/sanity/sanity.log` (+ `.path_proof.txt`).

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
* Headers: `artifacts/ops/internal_version/headers_get.txt`, `artifacts/ops/internal_version/headers_head.txt`, `artifacts/ops/internal_version/cond_if_none_match_headers.txt`, `artifacts/ops/internal_version/cond_if_modified_since_headers.txt`
* Two-run identity log: `artifacts/ops/internal_version/two_run_identity.log`
* Freeze-Pack SoT and schema: `catalog/manifest.json` (top-level keys exactly `root`, `version`, `built_at_utc`, `files`; no self-listing) with canonical bytes (UTF-8, ASCII-sorted keys, compact separators, one trailing `\n`); `release_id = sha256(canonical_bytes(catalog/manifest.json))`.
* Evidence copy and evidence-only summaries: `artifacts/math/freeze_pack_manifest.json` is byte-identical to the SoT; `artifacts/math/manifest_snapshot.json` is evidence-only (not an identity input). Alternate manifest-like artifacts must be quarantined under different names/paths.
* Supporting identity artifacts (must exist and be non-empty): `artifacts/math/release_id.txt`, `artifacts/math/release_id_recompute.log`, `artifacts/math/checksums_audit.log`, `artifacts/math/manifest_snapshot.json`, `artifacts/proofs/env_pins.txt`.
* Validation entrypoints (closed rails; Python entrypoints in CI): `python scripts/release_id_recompute.py --check`, `python ci/checks/check_release_identity.sh` (runs the recompute check, schema/bytes validation, and evidence presence), and `python tools/evidence/run_sanity_pipeline.py` (runs the gate alongside other deterministic checks). `--check` writes the recompute log and sha sidecar; run in a clean workspace or discard local changes.
* All governed with `.path_proof.txt` siblings and indexed in `docs/evidence/INDEX.json` / `artifacts/evidence_index.jsonl`
* Known canon mismatch: PF20 references a provenance note for D3, while implementation follows the PF10 posture via the governed two-run/coupling log as the provenance proof.

# Appendix-D — Evidence Index (EPIC-021)

## Registry report and sanity pipeline
* `artifacts/registry/registry_report.json` (generated by `tools/generate_registry_report.py`)
* `artifacts/registry/registry_report.json.path_proof.txt`
* `artifacts/sanity/sanity.log`
* `artifacts/sanity/sanity.log.path_proof.txt`
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

## Bridge adapter & rails-open scope
* `artifacts/db_bridge/adapter_selection.snapshot.json`
* `artifacts/db_bridge/health.json`
* `artifacts/db_bridge/root.json`
* `artifacts/db_bridge/query_select_1.json`
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
