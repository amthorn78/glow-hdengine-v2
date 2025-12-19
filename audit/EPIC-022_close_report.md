# HDE-EPIC022 — Separation Pass 2 Close Report

## Executive overview
- Close-pack artifacts are complete: token matrix, acceptance map, manifest, and this close report now bind every PF20 §2.7.5 token without placeholders.
- Evidence index + machine mirror refreshed under closed rails; sanity pipeline log and determinism pins proofs are indexed with path proofs.
- D1 parity, D2 stream discipline, and D3 internal/version identity evidence remain aligned with stored artifacts and contract tests; acceptance bindings match the governed INDEX.json entries.
- Structural QA adds epic-closeable validation for token roster, forbidden-token absence, determinism binding, and required artifact presence.
- Rails posture remained closed throughout (SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC) via engine.runtime.determinism_env.ensure_determinism_env and ci/checks/check_env_pins.sh.

## Rails posture
- Closed rails enforced for all captures and checks: SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC.
- Determinism pins evidence: audit/gates/determinism/env_pins.log (INDEX artifact_key audit.determinism.env_pins → audit/gates/determinism/env_pins.log; proof anchor audit/gates/determinism/env_pins.log.path_proof.txt).
- Sanity pipeline evidence: artifacts/sanity/sanity.log (INDEX artifact_key sanity.pipeline.log → artifacts/sanity/sanity.log; proof anchor artifacts/sanity/sanity.log.path_proof.txt).

## D0 — Discovery and scaffolding
- Close-pack files: audit/qa/hde-epic022/token_evidence_matrix.md; docs/acceptance_map_epic022.json; audit/EPIC-022_MANIFEST.json; audit/EPIC-022_close_report.md.
- Tests: tests/qa/test_epic022_acceptance_scaffold.py; tests/qa/test_epic022_close_pack_ready.py.
- Indexed evidence referenced by scaffolding:
  - audit/gates/determinism/env_pins.log (artifact_key audit.determinism.env_pins → audit/gates/determinism/env_pins.log).
  - artifacts/sanity/sanity.log (artifact_key sanity.pipeline.log → artifacts/sanity/sanity.log).
  - artifacts/evidence_index.jsonl (artifact_key index.machine_mirror → artifacts/evidence_index.jsonl).

## D1 — Error Envelope Parity Pass 2
- Tests: tests/cli/test_errors_parity.py::test_http_and_cli_parity.
- Evidence artifacts (INDEX artifact_key ERRORS_READER_CLI_PARITY_V1):
  - parity/errors_reader_cli.invalid_json.http.json
  - parity/errors_reader_cli.invalid_json.cli.txt
  - parity/errors_reader_cli.invalid_viewer_prefs.http.json
  - parity/errors_reader_cli.invalid_viewer_prefs.cli.txt
  - parity/errors_reader_cli.db_unavailable.http.json
  - parity/errors_reader_cli.db_unavailable.cli.txt
  - parity/errors_reader_cli.vendor_attempt_closed_rails.http.json
  - parity/errors_reader_cli.vendor_attempt_closed_rails.cli.txt
- Token map evidence: errors/token_map/token_map.json (INDEX artifact_key ERROR_TOKEN_MAP_V1 → errors/token_map/token_map.json).

## D2 — Presenter Flow Stream Discipline Closeout
- Tests: tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical; tests/cli/test_cli_usage_and_errors.py.
- Evidence artifacts and INDEX bindings:
  - artifacts/cli/showcompat/stdout.json (artifact_key cli.showcompat.stdout → artifacts/cli/showcompat/stdout.json).
  - artifacts/cli/showcompat/stdout.json.sha256 (artifact_key cli.showcompat.stdout_sha256 → artifacts/cli/showcompat/stdout.json.sha256).
  - artifacts/cli/showcompat/args.json (artifact_key cli.showcompat.args → artifacts/cli/showcompat/args.json).

## D3 — /internal/version Identity Coupling and Indexing Closeout
- Tests: tests/transport/test_internal_version_contract.py::test_internal_version_invariants_and_artifacts; tests/cli/test_showcompat_parity_and_identity.py::test_two_run_identity_and_reemit.
- Evidence artifacts and INDEX bindings:
  - artifacts/ops/internal_version/body_get.json (artifact_key INTVER_BODY_GET_V1 → artifacts/ops/internal_version/body_get.json).
  - artifacts/ops/internal_version/body_get.sha256 (artifact_key INTVER_BODY_GET_SHA256_V1 → artifacts/ops/internal_version/body_get.sha256).
  - artifacts/ops/internal_version/headers_get.txt (artifact_key INTVER_HEADERS_GET_V1 → artifacts/ops/internal_version/headers_get.txt).
  - artifacts/ops/internal_version/headers_head.txt (artifact_key INTVER_HEADERS_HEAD_V1 → artifacts/ops/internal_version/headers_head.txt).
  - artifacts/ops/internal_version/cond_if_none_match_headers.txt (artifact_key INTVER_HEADERS_COND_IF_NONE_MATCH_V1 → artifacts/ops/internal_version/cond_if_none_match_headers.txt).
  - artifacts/ops/internal_version/cond_if_modified_since_headers.txt (artifact_key INTVER_HEADERS_COND_IF_MODIFIED_SINCE_V1 → artifacts/ops/internal_version/cond_if_modified_since_headers.txt).
  - artifacts/ops/internal_version/two_run_identity.log (artifact_key INTVER_TWO_RUN_IDENTITY_V1 → artifacts/ops/internal_version/two_run_identity.log).
- Identity coupling/supporting artifacts (referenced by contract test; not separately indexed): artifacts/audit/cli/two_run_identity.log; artifacts/math/release_id_recompute.log; artifacts/math/freeze_pack_manifest.json; artifacts/math/release_id.txt.

## Token/Evidence binding summary
- Acceptance artifacts now bind all PF20 §2.7.5 tokens with concrete evidence, indexed where governed: see audit/qa/hde-epic022/token_evidence_matrix.md and docs/acceptance_map_epic022.json.
- Live QA is still required for epic close; planning and execution are deferred to the Live QA phase.
