# HDE-EPIC021 Token ↔ Evidence Matrix

| Token name | PF owner (doc + section title only) | Evidence artifacts (titles / paths / artifact_keys) | CI jobs / tests (names or node ids) | QA_ROOT logs (audit/qa/hde-epic021/...) | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| PR_OPENED_OK | PF20 — HDE-Phased Epics (EPIC021 record) | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| TESTS_PASS_OK | PF19 — Glow QA Guide §9A | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| DOC_DELTA_PRESENT_OK | PF03 — Technical Writing §Single-home | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| EVIDENCE_INDEX_UPDATED_OK | PF12 — HDE-Schemas and Artifacts §Evidence Index | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (baseline) |
| MACHINE_MIRROR_UPDATED_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 |
| EVIDENCE_INDEX_HASH_OK | PF12 — HDE-Schemas and Artifacts §Evidence Hashing | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 |
| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| ENV_RAILS_POLICY_OK | PF19 — Glow QA Guide §Env Pins | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| EVIDENCE_INDEX_MIRROR_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (baseline) |
| EVIDENCE_PATHS_VALIDATED_OK | PF12 — HDE-Schemas and Artifacts §Path Proofs | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 |
| DETERMINISM_ENV_PINS_OK | PF19 — Glow QA Guide §Env Pins | TBD (PR 2+) | TBD (PR 2+) | TBD (PR 2+) | Planned | EPIC: HDE-EPIC021 |
| SANITY_PIPELINE_OK | PF19 — Glow QA Guide §Sanity Pipeline | TBD (PR 4+) | TBD (PR 4+) | TBD (PR 4+) | Planned | EPIC: HDE-EPIC021 |
| CLI_READER_EMITTER_PARITY_OK | PF20 — HDE-Phased Epics (EPIC021 record); PF19 — Glow QA Guide §Emitter Canon | `tests/cli/test_showcompat_parity_and_identity.py` parity outputs (`artifacts/cli/ab.json`, `artifacts/presenter/reader_cli_parity.bytes`); `tests/cli/test_bg_resolve.py` canonical parity runs | `pytest tests/cli/test_showcompat_parity_and_identity.py tests/cli/test_bg_resolve.py` | TBD (PR 4) | Implemented | EPIC: HDE-EPIC021; extends parity to EPIC021 CLI/Reader surfaces |
| CLI_NO_ALT_JSON_OK | PF20 — HDE-Phased Epics (EPIC021 record); PF05 — CLI/API/Vendor Ref §6 | `tests/cli/test_cli_canonical_bytes.py` canonical stdout/admin dumps; `tests/cli/test_bg_resolve.py` canonical emit checks; `tests/cli/test_aux_preview.py` parity vs Reader text | `pytest tests/cli/test_cli_canonical_bytes.py tests/cli/test_bg_resolve.py tests/cli/test_aux_preview.py` | TBD (PR 4) | Implemented | EPIC: HDE-EPIC021; governed CLI emits only canonical JSON/text |
| JSON_CANONICAL_CHECK_OK | PF19 — Glow QA Guide §Emitter Canon; PF14 — Mechanics Guide §Emitter Canon | Canonical re-emit assertions in `tests/cli/test_bg_resolve.py`; sercanon identity checks in `tests/cli/test_cli_canonical_bytes.py` | `pytest tests/cli/test_bg_resolve.py tests/cli/test_cli_canonical_bytes.py` | TBD (PR 4) | Implemented | EPIC: HDE-EPIC021; canonical serializer shared across surfaces |
| ERROR_JSON_CANON_OK | PF19 — Glow QA Guide §Emitter Canon; PF05 — CLI/API/Vendor Ref §Error schema | Error-path canonical JSON in `tests/cli/test_bg_resolve.py::test_bg_resolve_vendor_refused_under_safe_rails` and `::test_bg_resolve_vendor_missing_inputs` | `pytest tests/cli/test_bg_resolve.py -k vendor` | TBD (PR 4) | Implemented | EPIC: HDE-EPIC021; CLI error envelopes emitted via canonical serializer |
| CLI_SERIALIZER_GUARD_OK | PF19 — Glow QA Guide §Serializer Guards; PF20 — EPIC021 record | Guard logs `artifacts/cli/guards/serializer_grep_guard.log`, `artifacts/cli/guards/emitter_symbol_proof.txt`; coverage test `tests/cli/test_serializer_guards.py`; guard scope extended to Reader adapter | `pytest tests/cli/test_serializer_guards.py`; `python tools/cli/serializer_grep_guard.py`; `python tools/cli/emitter_symbol_proof.py` | TBD (PR 4) | Implemented | EPIC: HDE-EPIC021 |
| EVIDENCE_INDEX_UPDATED_OK | PF12 — HDE-Schemas and Artifacts §Evidence Index | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| EVIDENCE_INDEX_MIRROR_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| EVIDENCE_INDEX_HASH_OK | PF12 — HDE-Schemas and Artifacts §Evidence Hashing | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| EVIDENCE_PATHS_VALIDATED_OK | PF12 — HDE-Schemas and Artifacts §Path Proofs | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| CI_CHECK_MIRROR_SCHEMA_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 |
| MACHINE_MIRROR_UPDATED_OK | PF12 — HDE-Schemas and Artifacts §Evidence Mirror | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| DETERMINISM_ENV_PINS_OK | PF19 — Glow QA Guide §Env Pins | TBD (PR 3) | TBD (PR 3) | TBD (PR 3) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| SANITY_PIPELINE_OK | PF19 — Glow QA Guide §Sanity Pipeline | TBD (PR 4+) | TBD (PR 4+) | TBD (PR 4+) | Planned | EPIC: HDE-EPIC021 (D2 scope) |
| SANITY_PIPELINE_LOGGED_OK | PF19 — Glow QA Guide §Sanity Pipeline | TBD (PR 4+) | TBD (PR 4+) | TBD (PR 4+) | Planned | EPIC: HDE-EPIC021 |
| QA_STEP_LOGS_CONSOLIDATED_OK | PF19 — Glow QA Guide §QA Logs | TBD (PR 4+) | TBD (PR 4+) | TBD (PR 4+) | Planned | EPIC: HDE-EPIC021 |
| PF04-DD-QA-BOOTSTRAP-TOKENS | PF04 — Governance Docs (Doc Delta) | TBD (PR 4+) | TBD (PR 4+) | TBD (PR 4+) | Token-incomplete | EPIC: HDE-EPIC021 |
| PF19-DD-QA-PLAN-VIABILITY-TOKENS | PF19 — Glow QA Guide (Doc Delta) | TBD (PR 4+) | TBD (PR 4+) | TBD (PR 4+) | Token-incomplete | EPIC: HDE-EPIC021 |
