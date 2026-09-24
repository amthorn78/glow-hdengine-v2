# Config governance and bundles (EPIC018 D5/D6)

## Governed config artifacts (D5)
- Generated with `python tools/config/generate_config_artifacts.py` under closed rails (determinism helper required).
- `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root>` is the read-only Magic-10 golden comparison mode (HDE-EPIC040-PR05): it admits the explicit candidate root through the admission owner, runs `tests/fixtures/magic10/v1/goldens.json` (PF01 §9.5 M10-G001–G008) through the canonical kernel and application entrypoints, reports every mismatch, and cannot write, activate or generate anything; `--report <external path>` saves the complete report.
- Current governed files include `config/bands_4B60_v1.json` and `config/toggles_v1.json` (Magic-10 banding and feature toggles).
- Governed outputs must be path-proofed and indexed (`docs/evidence/INDEX.json`, `artifacts/evidence_index.jsonl`). No manual edits.
- Acceptance mapping: `audit/EPIC-018_config_acceptance_map.json` links PF09 tasks to config artifacts, tokens, and tests; treat it as governed evidence with `.path_proof.txt`.

## Typed bundles (D6)
- Generated with `python tools/config/generate_bundles.py` under the same rails.
- Schemas: `docs/schemas/config_bundle_fe.json` (frontend) and `docs/schemas/config_bundle_be.json` (backend). Bundles mirror governed config and registry state.
- Bundle outputs are governed: add `.path_proof.txt` siblings and update evidence indexes via `tools/evidence/update_evidence_index.py`.

## Registry alignment
- Config and bundles align with the registry report produced by the ordering/mechanics stack; use PF14 — Mechanics for canonical definitions.
- Token coverage and epic-level acceptance are recorded in the EPIC018 manifest and close report; do not invent new tokens outside those documents.
