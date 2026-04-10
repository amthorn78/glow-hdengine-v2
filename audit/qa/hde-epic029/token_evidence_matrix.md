# HDE-EPIC029 Token ↔ Evidence Matrix

| token_name | owner_pf | evidence_artifacts | ci_tests_jobs | qa_root_logs | status | notes |
| --- | --- | --- | --- | --- | --- | --- |
| DOC_DELTA_PRESENT_OK | PF04 — HDE Governance §2.0.0 | audit/docdeltas/hde-epic029_doc_deltas.md; audit/docdeltas/hde-epic029_drain_targets.md | Bound by close-pack generator outputs | acceptance_map_viability.log | Implemented | Doc-delta and drain-target ledgers are generated and bound for this close pack. |
| EVIDENCE_INDEX_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Index | docs/evidence/INDEX.json | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | Bound only when INDEX.json and INDEX.json.path_proof.txt are present. |
| MACHINE_MIRROR_UPDATED_OK | PF12 — Schemas & Artifacts §Evidence Mirror | artifacts/evidence_index.jsonl | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | Bound only when evidence_index.jsonl and evidence_index.jsonl.path_proof.txt are present. |
| EVIDENCE_INDEX_HASH_OK | PF12 — Schemas & Artifacts §Evidence Hash Discipline | docs/evidence/INDEX.sha256; artifacts/evidence_index.jsonl.sha256 | tools/evidence/update_evidence_index.py | acceptance_map_viability.log | Implemented | Bound only when sha256 sidecars and path proofs exist and hashes match current bytes. |
| ENV_RAILS_POLICY_OK | PF10 — HDE Build Notes §Closed Rails | artifacts/proofs/env_pins.txt | ci/checks/check_env_pins.sh (via sanity pipeline) | acceptance_map_viability.log | Implemented | Determinism env pins evidence remains present for closed-rails posture. |
| JSON_CANONICAL_CHECK_OK | PF10 — HDE Build Notes §Canonical JSON Gate | audit/gates/json_gate/canonical/json_gate_structured_record.json; audit/gates/canonical_json/json_canonical_check.log | tools/evidence/run_canonical_json_gate.py (governed) | acceptance_map_viability.log | Implemented | Canonical JSON gate evidence is bound without introducing new token names. |
| TESTS_PASS_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log | Existing epic-close live QA output only | acceptance_map_viability.log | Implemented | Bound to existing live QA primary log. |
| QA_PRECOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-precommit/primary.log | Existing precommit checklist output only | acceptance_map_viability.log | Implemented | Bound to existing precommit primary log. |
| QA_POSTCOMMIT_CHECKLIST_OK | PF19 — Glow QA Guide §QA Rails | audit/qa/hde-epic029/checks/po-postcommit/primary.log | Existing postcommit checklist output only | acceptance_map_viability.log | Implemented | Bound to existing postcommit primary log. |

## PF09 scope bindings (status-only; not acceptance tokens)

- `HDE-CONJ009` / `HDE-CONJ009.1`: bound via `audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md`.
- `HDE-CONJ008` / `HDE-CONJ008.1`: bound via `artifacts/writer/conjunction_write_readback.log` and `artifacts/writer/conjunction_writer_summary.json`.
- `HDE-CONJ001` / `HDE-CONJ001.4`: bound via OPS disposition; remains not done while codespaces/local_dev are not yet closed.
