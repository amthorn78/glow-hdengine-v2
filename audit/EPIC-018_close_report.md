# HDE-EPIC018 — Calcination Pass 3 Close Report

## Overview
HDE-EPIC018 delivered Calcination Pass 3 by consolidating canonical CLI serialization evidence, determinism rails, CLI guard captures, sanity/orientation coverage, governed config artifacts, and deterministic FE/BE bundles. The new machine-readable manifest (audit/EPIC-018_MANIFEST.json) maps each epic token to its governing artifacts and tests, while this report provides the narrative roll-up.

## D1 — Canonical serializer/emitter completion
Status: **Complete**
- Scope: Canonical CLI JSON snapshots, AB↔BA parity, two-run identity, and Reader↔CLI parity captures.
- Evidence: `cli.showcompat.ab`, `cli.showcompat.ba`, `cli.showcompat.summary`, `cli.showcompat.reader_dump`, `cli.showcompat.reader_cli_parity`, `audit.canonical_json.cli_surfaces`.
- Tests: `tests/cli/test_cli_canonical_bytes.py` (canonical bytes, dumps) and `tests/cli/test_showcompat_parity_and_identity.py` (two-run identity, AB↔BA, reader parity).

## D2 — Determinism env rails helper and evidence
Status: **Complete**
- Scope: Determinism env pins helper and recorded env rails log under closed rails.
- Evidence: `audit.determinism.env_pins`.
- Tests: `tests/invariance/test_determinism_env_helper.py` and `tests/invariance/test_locale_tz.py`.

## D3 — CLI serializer guard and emitter symbol proof
Status: **Complete** (NEW CANON PROPOSALS recorded)
- Scope: Serializer grep guard and emitter symbol proof captures for CLI surfaces.
- Evidence: `cli.guard.serializer_grep`, `cli.guard.emitter_symbol_proof`.
- Tests: `tests/cli/test_serializer_guards.py` (pass and detection coverage). Tokens `SERIALIZER_GREP_GUARD_OK` and `EMITTER_SYMBOL_PROOF_OK` are marked as NEW CANON PROPOSAL pending PF19/PF04 updates.

## D4 — Evidence skeleton, orientation, and sanity pipeline
Status: **Complete**
- Scope: Evidence skeleton integrity, orientation demo refresh, and sanity pipeline log.
- Evidence: `index.machine_mirror`, `topology.orientation_demo`, `sanity.pipeline.log`.
- Tests: `tests/evidence/test_evidence_skeleton.py`, `tests/evidence/test_orientation_demo.py`, `tests/evidence/test_sanity_pipeline.py`.

## D5 — Governed config artifacts and acceptance map
Status: **Complete**
- Scope: Registry report, Magic10 thresholds, band edges, and EPIC-018 acceptance map wiring.
- Evidence: `registry.registry_report`, `config.magic10`, `config.band_edges`, `epic018.config.acceptance_map`.
- Tests: `tests/config/test_registry_report.py`, `tests/config/test_config_artifacts.py`, `tests/config/test_config_acceptance_map.py`.

## D6 — Typed FE/BE bundles
Status: **Complete** (NEW CANON PROPOSAL token)
- Scope: Deterministic FE/BE config bundles built from governed configs and registry data.
- Evidence: `config_bundle.fe`, `config_bundle.be`.
- Tests: `tests/config/test_typed_bundles.py`. Token `CONFIG_BUNDLES_DETERMINISTIC_OK` is marked NEW CANON PROPOSAL pending PF doc updates.

## Issues & Follow-ups
- Tokens flagged as NEW CANON PROPOSAL (`SERIALIZER_GREP_GUARD_OK`, `EMITTER_SYMBOL_PROOF_OK`, `CONFIG_BUNDLES_DETERMINISTIC_OK`) require PF19/PF04 updates in a follow-on doc PR.
- No additional gaps were observed during close-out; PF-Canon docs remain read-only in this pack. The machine-readable manifest holds the canonical token→artifact→test mapping; this report is informational and intentionally excluded from the evidence index.
