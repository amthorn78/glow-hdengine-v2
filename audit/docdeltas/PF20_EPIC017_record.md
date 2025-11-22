# PF20 — EPIC017 record (paste-ready)

## Status
- Epic ID: HDE-EPIC017 — HD Calcination Pass 2.
- Deliverables: D1–D4 **Done**, D5 **Completed** (manifest + close report + doc-deltas); EPIC011 ingest remains parked for a future epic.

## Tokens and outcomes (all OK)
- Canonical serialization: CLI_NO_ALT_JSON_OK, CLI_READER_PARITY_OK, CLI_SHOWCOMPAT_CANON_OK, CLI_STDOUT_LF_OK, JSON_CANONICAL_CHECK_OK, TWO_RUN_IDENTITY_OK, COMPOSITE_ABBA_IDENTITY_OK.
- Evidence skeleton: EVIDENCE_INDEX_UPDATED_OK, MACHINE_MIRROR_UPDATED_OK, EVIDENCE_INDEX_HASH_OK, EVIDENCE_INDEX_MIRROR_OK, EVIDENCE_PATHS_VALIDATED_OK, EVIDENCE_PATH_PROOFS_OK, CI_CHECK_MIRROR_SCHEMA_OK, CI_CHECK_FINAL_LF_OK.
- Config & registry: CONFIG_GEN_OK, UNKNOWN_IDS_FAIL_CLOSED_OK.
- Ordering: TIEBREAK_TOTAL_ORDER_OK.
- Governance: TESTS_PASS_OK, DOC_DELTA_PRESENT_OK.

## Evidence pointers
- Manifest: `audit/EPIC017_MANIFEST.json` (token→artifact map).
- Close-out: `audit/EPIC017_close_report.md`.
- Machine mirror self-record: `index.machine_mirror`.
- Ordering evidence: `engine.order.props_total_order.log`, `engine.order.abba_identity.bytes`.
- Registry: `registry.registry_report`.
- CLI canon & parity: `cli.showcompat.summary`, `cli.showcompat.ab`, `cli.showcompat.ba`, `cli.showcompat.reader_cli_parity`, `cli.showcompat.preimage_recompute`.
