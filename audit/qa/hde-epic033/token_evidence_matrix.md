# HDE-EPIC033 Token Evidence Matrix

This baseline matrix uses existing registry-valid tokens only and does not mint a vendor-v2-specific token.

| Token | Evidence | Status | Boundary |
| --- | --- | --- | --- |
| TESTS_PASS_OK | tests/evidence/test_hdapi_v2_contract_inventory.py | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
| DOC_DELTA_PRESENT_OK | audit/docdeltas/hde-epic033_doc_deltas.md; audit/qa/hde-epic033/00_meta/doc_deltas.md | baseline_pointer_present | Contract inventory only; no runtime v2 conformance or AI scope |
| EVIDENCE_INDEX_UPDATED_OK | docs/evidence/INDEX.json; artifacts/evidence_index.jsonl | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
| MACHINE_MIRROR_UPDATED_OK | artifacts/evidence_index.jsonl | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
| EVIDENCE_INDEX_HASH_OK | docs/evidence/INDEX.sha256 | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
| EVIDENCE_PATHS_VALIDATED_OK | tools/evidence/validate_evidence_paths.py | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
| EVIDENCE_PATH_PROOFS_OK | artifacts/vendor/hdapi_v2/*.path_proof.txt | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
| JSON_CANONICAL_CHECK_OK | artifacts/vendor/hdapi_v2/source_inventory.json; artifacts/vendor/hdapi_v2/contract_map.json | supported_by_pr_validation | Contract inventory only; no runtime v2 conformance or AI scope |
