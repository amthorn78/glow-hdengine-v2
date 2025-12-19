# HDE-EPIC022 Token ↔ Evidence Matrix

| Token name | PF owner (doc + section title only) | Evidence artifacts (titles / paths / artifact_keys) | CI jobs / tests (names or node ids) | QA_ROOT logs (audit/qa/hde-epic022/...) | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| PR_OPENED_OK | PF20 — HDE-Phased Epics (EPIC022 record) | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| DOC_DELTA_PRESENT_OK | PF03 — Technical Writing §Single-home | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| EVIDENCE_INDEX_UPDATED_OK | PF12 — HDE-Schemas and Artifacts §Evidence Index | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| EVIDENCE_INDEX_HASH_OK | PF12 — HDE-Schemas and Artifacts §Evidence Hashing | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| EVIDENCE_INDEX_MIRROR_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| EVIDENCE_PATHS_VALIDATED_OK | PF12 — HDE-Schemas and Artifacts §Path Proofs | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| MACHINE_MIRROR_UPDATED_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| ENV_RAILS_POLICY_OK | PF19 — Glow QA Guide §Env Pins | audit/gates/determinism/env_pins.log; audit/gates/determinism/env_pins.log.path_proof.txt | ci/checks/check_env_pins.sh | audit/gates/determinism/env_pins.log | Pending | Closed rails enforced for EPIC022 parity runs |
| DETERMINISM_ENV_PINS_OK | PF19 — Glow QA Guide §Env Pins | audit/gates/determinism/env_pins.log; audit/gates/determinism/env_pins.log.path_proof.txt | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| SANITY_PIPELINE_OK | PF19 — Glow QA Guide §Sanity Pipeline | TBD | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| CLOSE_PACK_FILES_PRESENT_OK | PF20 — HDE-Phased Epics (EPIC022 record) | audit/EPIC-022_close_report.md; audit/EPIC-022_MANIFEST.json; audit/qa/hde-epic022/token_evidence_matrix.md; docs/acceptance_map_epic022.json | TBD | TBD | Pending | Baseline token; scaffolded in PR1 |
| ERROR_JSON_CANON_OK | PF20 — HDE-Phased Epics (HDE-SEPA002) | tests/cli/test_errors_parity.py::test_http_and_cli_parity; parity/errors_reader_cli.invalid_json.http.json; parity/errors_reader_cli.invalid_viewer_prefs.http.json; parity/errors_reader_cli.db_unavailable.http.json; parity/errors_reader_cli.vendor_attempt_closed_rails.http.json | tests/cli/test_errors_parity.py::test_http_and_cli_parity | TBD | Pending | D1 parity scope |
| ERROR_TOKEN_MAP_OK | PF20 — HDE-Phased Epics (HDE-SEPA002) | tests/cli/test_errors_parity.py::test_http_and_cli_parity; errors/token_map/token_map.json | tests/cli/test_errors_parity.py::test_http_and_cli_parity | TBD | Pending | D1 parity scope |
| CLI_READER_PARITY_OK | PF20 — HDE-Phased Epics (HDE-SEPA002.5) | tests/cli/test_errors_parity.py::test_http_and_cli_parity; parity/errors_reader_cli.invalid_json.http.json; parity/errors_reader_cli.invalid_json.cli.txt; parity/errors_reader_cli.invalid_viewer_prefs.http.json; parity/errors_reader_cli.invalid_viewer_prefs.cli.txt; parity/errors_reader_cli.db_unavailable.http.json; parity/errors_reader_cli.db_unavailable.cli.txt; parity/errors_reader_cli.vendor_attempt_closed_rails.http.json; parity/errors_reader_cli.vendor_attempt_closed_rails.cli.txt | tests/cli/test_errors_parity.py::test_http_and_cli_parity | TBD | Pending | D1 parity scope |
| TWO_RUN_IDENTITY_OK | PF20 — HDE-Phased Epics (HDE-SEPA002.5; HDE-SEPA004.4) | tests/cli/test_errors_parity.py::test_http_and_cli_parity; parity/errors_reader_cli.invalid_json.http.json; parity/errors_reader_cli.invalid_json.cli.txt; parity/errors_reader_cli.invalid_viewer_prefs.http.json; parity/errors_reader_cli.invalid_viewer_prefs.cli.txt; parity/errors_reader_cli.db_unavailable.http.json; parity/errors_reader_cli.db_unavailable.cli.txt; parity/errors_reader_cli.vendor_attempt_closed_rails.http.json; parity/errors_reader_cli.vendor_attempt_closed_rails.cli.txt | tests/cli/test_errors_parity.py::test_http_and_cli_parity | TBD | Pending | D1 parity scope binding to parity harness |
| CLI_STDOUT_LF_OK | PF20 — HDE-Phased Epics (HDE-SEPA003.3) | TBD | TBD | TBD | Pending | D2 stream discipline placeholder |
| INTERNAL_VERSION_200_CTYPE_JSON_UTF8_OK | PF04 — Canon-HDE-Governance §/internal/version tokens | artifacts/ops/internal_version/body_get.json | TBD | TBD | Pending | D3 internal/version placeholder |
| INTERNAL_VERSION_HEAD_PARITY_OK | PF04 — Canon-HDE-Governance §/internal/version tokens | artifacts/ops/internal_version/headers_head.txt | TBD | TBD | Pending | D3 internal/version placeholder |
| INTERNAL_VERSION_CONDITIONALS_IGNORED_OK | PF04 — Canon-HDE-Governance §/internal/version tokens | artifacts/ops/internal_version/cond_if_none_match_headers.txt; artifacts/ops/internal_version/cond_if_modified_since_headers.txt | TBD | TBD | Pending | D3 internal/version placeholder |
| INTERNAL_VERSION_NO_ETAG_OK | PF04 — Canon-HDE-Governance §/internal/version tokens | artifacts/ops/internal_version/headers_get.txt | TBD | TBD | Pending | D3 internal/version placeholder |
| INTERNAL_VERSION_NO_STORE_OK | PF04 — Canon-HDE-Governance §/internal/version tokens | artifacts/ops/internal_version/headers_get.txt | TBD | TBD | Pending | D3 internal/version placeholder |
| RELEASE_ID_RECOMPUTE_OK | PF04 — Canon-HDE-Governance §Pack identity tokens | artifacts/math/release_id_recompute.log | TBD | TBD | Pending | D3 identity coupling placeholder |
| RELEASE_ID_FROM_MANIFEST_OK | PF04 — Canon-HDE-Governance §Pack identity tokens | artifacts/math/release_id.txt; artifacts/math/freeze_pack_manifest.json | TBD | TBD | Pending | D3 identity coupling placeholder |

NOTE: Registry check needed for: CLOSE_PACK_FILES_PRESENT_OK, CLI_STDOUT_LF_OK, QA_PRECOMMIT_CHECKLIST_OK, QA_POSTCOMMIT_CHECKLIST_OK.
