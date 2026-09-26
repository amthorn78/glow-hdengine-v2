# Config governance and bundles (EPIC018 D5/D6)

## Current Magic-10 configuration (HDE-EPIC040)
- Mechanics configuration: `catalog/magic10_mechanics_v1.json` (`magic10_mechanics_config.v1`, `config_id` `m10-channel-state-v1.0.0`, `result_schema` `magic10_result.v1`), validated against `schemas/magic10_mechanics_v1.schema.json`. Its `sources` bind `catalog/magic10_caps.json`, `catalog/magic10.json`, `catalog/channels_v1.json` and `math/thresholds.json` by SHA-256.
- Result schemas: `schemas/magic10_result_v1.schema.json` (intrinsic core result) and `schemas/magic10_compat_result_v1.schema.json` (application result; `hdctl showcompat` stdout). Catalog schemas: `schemas/channels_v1.schema.json` and `schemas/gates_v1.schema.json`. All are release members.
- Writers (canonical owners; never hand-edit their outputs): `tools/config/generate_config_artifacts.py` writes `artifacts/registry/registry_report.json`, `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json` (`--check` validates them without writing; `--publish-family` publishes the scoped config family, catalog logs, bundles and required evidence companions); `tools/config/generate_bundles.py` writes `artifacts/config_bundles/fe_bundle.json` and `artifacts/config_bundles/be_bundle.json`; `tools/generate_registry_report.py` writes the registry report; `tools/evidence/update_evidence_index.py` publishes the Index/Mirror companions.
- FE/BE promise: the bundle schema identities `config_bundle.fe.v1` and `config_bundle.be.v1` are unchanged by HDE-EPIC040, and the Channel fields `primary_domain`, `domains` and `flags` remain non-scoring Product metadata (`PF12-Canon-HDE-Schemas-and-Artifacts` §2.1).
- Writer recovery limits: the config-family writers restore on caught failures, refuse source/destination races, keep check paths non-writing and preserve conflicting external changes. They do not promise crash atomicity, multi-file atomic visibility or cross-process locking.

## Governed config artifacts (D5)
- Generated with `python tools/config/generate_config_artifacts.py` under closed rails (determinism helper required).
- `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root>` is the read-only Magic-10 golden comparison mode (HDE-EPIC040-PR05): it admits the explicit candidate root through the admission owner, runs `tests/fixtures/magic10/v1/goldens.json` (PF01 §9.5 M10-G001–G008) through the canonical kernel and application entrypoints, reports every mismatch, and cannot write, activate or generate anything; `--report <external path>` saves the complete report.
- `config/bands_4B60_v1.json` and `config/toggles_v1.json` remain in the tree, but the current Magic-10 mechanics and band-edge writers do not read them (no reader in `engine/`, `adapter/`, `presenter/`, `scripts/` or `tools/` as of HDE-EPIC040-PR07); band edges come from `math/thresholds.json`.
- Governed outputs must be path-proofed and indexed (`docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`). No manual edits.
- Acceptance mapping: `audit/EPIC-018_config_acceptance_map.json` links PF09 tasks to config artifacts, tokens, and tests; treat it as governed evidence with `.path_proof.txt`.

## Typed bundles (D6)
- Generated with `python tools/config/generate_bundles.py` under the same rails.
- Schemas: `docs/schemas/config_bundle_fe.json` (frontend) and `docs/schemas/config_bundle_be.json` (backend). Bundles mirror governed config and registry state.
- Bundle outputs are governed: add `.path_proof.txt` siblings and update evidence indexes via `tools/evidence/update_evidence_index.py`.

## Registry alignment
- Config and bundles align with the registry report produced by the ordering/mechanics stack; use PF14 — Mechanics for canonical definitions.
- Token coverage and epic-level acceptance are recorded in the EPIC018 manifest and close report; do not invent new tokens outside those documents.
