# HDE-EPIC027 Token ↔ Evidence Matrix

| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| EVIDENCE_INDEX_UPDATED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | python tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | D4 global index/mirror refresh and hash sentinel update. |
| EVIDENCE_INDEX_HASH_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.sha256 | python tools/evidence/update_evidence_index.py --check | acceptance_map_viability.log | Implemented | Hash sentinel refreshed with index update. |
| EVIDENCE_INDEX_MIRROR_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | ci/checks/check_mirror_schema.sh | acceptance_map_viability.log | Implemented | Human index and machine mirror refreshed in one close slice. |
| EVIDENCE_PATHS_VALIDATED_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | python tools/evidence/validate_evidence_paths.py | acceptance_map_viability.log | Implemented | Path-proof coherence validated on governed outputs. |
| CI_CHECK_MIRROR_SCHEMA_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | artifacts/evidence_index.jsonl; docs/evidence/INDEX.json | ci/checks/check_mirror_schema.sh | acceptance_map_viability.log | Implemented | Mirror schema remains records-only and sorted. |
| CI_CHECK_FINAL_LF_OK | PF04 — Canon-HDE-Governance §2.0 Acceptance Tokens | docs/acceptance_map_epic027.json; audit/qa/hde-epic027/token_evidence_matrix.md | python tools/evidence/check_lf_endings.py --check | acceptance_map_viability.log | Implemented | Final-LF discipline enforced on new close-pack ledgers. |
