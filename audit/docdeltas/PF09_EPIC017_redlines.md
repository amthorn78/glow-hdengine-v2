# PF09 — EPIC017 redlines (paste-ready)

## Status block
- Update EPIC017 row to mark D1–D4 as **Done**; D5 complete with doc-deltas and manifest present.
- Acceptance tokens satisfied by EPIC017 artifacts: PR_OPENED_OK, TESTS_PASS_OK, DOC_DELTA_PRESENT_OK, EVIDENCE_INDEX_UPDATED_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_INDEX_HASH_OK, EVIDENCE_PATHS_VALIDATED_OK, EVIDENCE_PATH_PROOFS_OK, CI_CHECK_MIRROR_SCHEMA_OK, CI_CHECK_FINAL_LF_OK.

## Evidence pointers
- Reference `audit/EPIC017_MANIFEST.json` as the authoritative token→artifact ledger.
- Machine mirror self-record: `index.machine_mirror` with path proof.
- Ordering: `engine.order.props_total_order.log` (tie-break/total order) plus `engine.order.abba_identity.bytes` (AB↔BA identity).
- Registry: `registry.registry_report` (config gen + unknown ID fail-closed).
- CLI canon: `cli.showcompat.summary`, `cli.showcompat.ab`, `cli.showcompat.ba`, `cli.showcompat.reader_cli_parity`, `cli.showcompat.preimage_recompute`.
- Topology/path proofs: `topology.orientation_demo`.

## Notes
- CI rails: SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC; mirror/schema checks gate merges.
- EPIC011 vendor ingest remains parked; EPIC017 closes the Calcination foundations instead.
