# HDE-EPIC035 PR-03 Token Evidence Matrix

Scope: compact evidence matrix for HDE-FERM008.5 evidence-loop binding. This is not a QA plan, Live QA runbook, closeout review, or OPS completion record.

| Token | Evidence paths | Role |
| --- | --- | --- |
| DOC_DELTA_PRESENT_OK | `audit/docdeltas/hde-epic035_doc_deltas.md`; `audit/qa/hde-epic035/00_meta/doc_deltas.md` | Candidate canon-drain notes only; PF-Canon not edited. |
| EVIDENCE_INDEX_UPDATED_OK | `docs/evidence/INDEX.json` | Human Evidence Index includes PR-01, PR-02, retained OPS-01, and PR-03 boundary artifacts. |
| MACHINE_MIRROR_UPDATED_OK | `artifacts/evidence_index.jsonl` | Machine Mirror includes matching rows for the Human Index entries. |
| EVIDENCE_INDEX_HASH_OK | `docs/evidence/INDEX.sha256`; `artifacts/evidence_index.jsonl.sha256` | Hash sentinels refreshed by governed tooling. |
| EVIDENCE_PATHS_VALIDATED_OK | `tools/evidence/validate_evidence_paths.py` | Path validation command verifies indexed evidence paths. |
| EVIDENCE_PATH_PROOFS_OK | sibling `.path_proof.txt` files for indexed PR-03 and promoted OPS-01 evidence | Path proofs bind bytes, size, mtime, and produced-at posture. |
| JSON_CANONICAL_CHECK_OK | `docs/acceptance_map_epic035.json`; PR-01/PR-02 JSON snapshots | Canonical JSON posture for JSON evidence and acceptance map. |
| TESTS_PASS_OK | targeted evidence tests | Targeted tests validate PR-03 evidence-loop invariants. |

Evidence roles:
- PR-01: `artifacts/vendor/hdapi_v2/error_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/rate_limit_headers.snapshot.json` bind HDE-FERM008.3 provider-outcome evidence without regeneration.
- PR-02: `artifacts/vendor/hdapi_v2/response_mapping.snapshot.json` and `artifacts/vendor/hdapi_v2/release_binding.snapshot.json` bind HDE-FERM008.4 response-normalization exact schema/adapter gap evidence without compatibility inference.
- OPS-01: retained files under `audit/ops/hde-epic035/ops-01/` are bound as already-produced open-rails evidence only; PR-03 did not rerun OPS.
- PR-03: `docs/acceptance_map_epic035.json`, this matrix, `audit/qa/hde-epic035/acceptance_map_viability.log`, and `audit/qa/hde-epic035/ops-01/ops_evidence_binding.log` bind HDE-FERM008.5 evidence-loop closure posture.

Nonclaims: no QA PASS, no OPS completion, no PF09 status movement, no HDE-FERM008 parent Done, no epic closeout, no full HumanDesignAPI v2 runtime conformance, no public Reader change, no public route, no public flag, no public payload or transport change, no new HTTP home, no app-side HumanDesignAPI credential ownership, no raw payload persistence, and no AI scope.
