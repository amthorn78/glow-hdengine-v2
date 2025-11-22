# HDE-EPIC017 — HD Calcination Pass 2 (Close-out)

## Overview
HD Calcination hardened the matching core so contributors and reviewers can see how the engine makes choices and verify every step. The work delivers a single canonical way to explain compatibility, a transparent evidence ledger, a programmatic registry for charts and relationships, and deterministic ordering that keeps results stable and fair. Evidence for each area is cataloged in `audit/EPIC017_MANIFEST.json` and mirrored in the machine ledger.

## D1 — Canonical Serialization Package
- Canonical CLI/Reader compatibility path with one auditable emitter and parity between AB/BA runs.
- Preimage recompute and two-run identity harnesses keep the JSON stable and LF-terminated.
- Compatibility explanations remain numeric-free and share a single stdout path.

| Capability | Internal token references | Evidence (see manifest) |
| --- | --- | --- |
| Compatible connections are consistent and explainable | CLI_NO_ALT_JSON_OK, CLI_SHOWCOMPAT_CANON_OK, CLI_STDOUT_LF_OK | `cli.showcompat.summary`, `cli.showcompat.ab`, `cli.showcompat.ba` |
| CLI and Reader stay in lockstep | CLI_READER_PARITY_OK, COMPOSITE_ABBA_IDENTITY_OK | `cli.showcompat.reader_cli_parity`, `engine.order.abba_identity.bytes` |
| Canonical JSON and two-run identity | JSON_CANONICAL_CHECK_OK, TWO_RUN_IDENTITY_OK | `cli.showcompat.ab`, `cli.showcompat.preimage_recompute` |

## D2 — Evidence & Transparency
- Human and machine ledgers stay in sync with path proofs and a machine mirror self-record for every governed artifact.
- Orientation demo and path-proof checks show how topology evidence is captured and replayed without surprises.
- CI checks validate mirror shape, hashes, and final LF discipline.

| Capability | Internal token references | Evidence (see manifest) |
| --- | --- | --- |
| Ledger and mirror updated in one place | EVIDENCE_INDEX_UPDATED_OK, MACHINE_MIRROR_UPDATED_OK, EVIDENCE_INDEX_HASH_OK | `index.machine_mirror` |
| Path proofs and topology coverage | EVIDENCE_PATHS_VALIDATED_OK, EVIDENCE_PATH_PROOFS_OK | `topology.orientation_demo` |
| CI rails for evidence shape | CI_CHECK_MIRROR_SCHEMA_OK, CI_CHECK_FINAL_LF_OK | `index.machine_mirror`, `cli.showcompat.ab` |

## D3 — Config & Registry
- A typed registry loader emits a canonical registry report with LF-terminated JSON and deterministic ordering.
- Unknown IDs fail closed; the registry report is indexed with path proofs alongside the mirror.

| Capability | Internal token references | Evidence (see manifest) |
| --- | --- | --- |
| Programmatic registry generation | CONFIG_GEN_OK | `registry.registry_report` |
| Strict IDs and canonical JSON | UNKNOWN_IDS_FAIL_CLOSED_OK, JSON_CANONICAL_CHECK_OK | `registry.registry_report` |

## D4 — Matching Logic & Fairness
- Deterministic comparators and ordering artifacts prove that tie-breaks are stable and reproducible.
- Ordering logs and AB↔BA identity captures show the same rank results regardless of input order.

| Capability | Internal token references | Evidence (see manifest) |
| --- | --- | --- |
| Total order and fairness | TIEBREAK_TOTAL_ORDER_OK, JSON_CANONICAL_CHECK_OK | `engine.order.props_total_order.log` |
| AB↔BA identity holds | COMPOSITE_ABBA_IDENTITY_OK | `engine.order.abba_identity.bytes` |

## D5 — Paper Trail and PF Updates
- This PR ships doc-delta drafts for PF09, PF10, PF12, PF14, PF19, PF20, and PF04 in `audit/docdeltas/` so governance can update canon by hand.
- `audit/EPIC017_MANIFEST.json` and this close-out report are indexed with path proofs to make the EPIC017 record auditable.
- EPIC011’s ingest track remains parked; EPIC017 delivers the hardened matching and evidence foundations that replace it for Phase I work.
