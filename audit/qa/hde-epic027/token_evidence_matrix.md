# HDE-EPIC027 Token ↔ Evidence Matrix

| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| EVIDENCE_INDEX_UPDATED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | python tools/evidence/update_evidence_index.py | checks/gate_update_evidence_index_write/primary.log | Implemented | Refresh executed in-generator before close report emission. |
| EVIDENCE_INDEX_HASH_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.sha256 | python tools/evidence/update_evidence_index.py --check | checks/gate_update_evidence_index_check/primary.log | Implemented | Index hash validation executed in-generator. |
| EVIDENCE_INDEX_MIRROR_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | ci/checks/check_mirror_schema.sh | checks/gate_mirror_schema/primary.log | Implemented | Mirror schema gate executed in-generator. |
| EVIDENCE_PATHS_VALIDATED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | python tools/evidence/validate_evidence_paths.py | checks/gate_evidence_paths_validation/primary.log | Implemented | Evidence-path validator executed in-generator. |
| CI_CHECK_MIRROR_SCHEMA_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/evidence_index.jsonl; docs/evidence/INDEX.json | ci/checks/check_mirror_schema.sh | checks/gate_mirror_schema/primary.log | Implemented | Records-only mirror schema conformance passed. |
| CI_CHECK_FINAL_LF_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/acceptance_map_epic027.json; audit/qa/hde-epic027/token_evidence_matrix.md | python tools/evidence/check_lf_endings.py | checks/gate_lf_endings/primary.log | Implemented | Final-LF gate executed in-generator. |
