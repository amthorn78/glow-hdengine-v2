# HDE-EPIC021 QA_ROOT

This directory is the EPIC021 QA_ROOT discipline home. It anchors calcination QA runs and related artifacts without changing PF12-governed evidence paths. QA runs may create subdirectories under `audit/qa/hde-epic021/<run-id>/`, where `<run-id>` is a deterministic, timestamp-free identifier (for example, derived from a git commit or CI job id consistent with existing QA tools). Epic-level, run-agnostic artifacts that live directly under this directory include:

- `token_evidence_matrix.md`
- `test_tooling_bootstrap.log` (planned in later PRs)
- `acceptance_map_viability.log` (planned in later PRs)
- Other QA manifests or summary files that demonstrate PF19/PF20 tokens for HDE-EPIC021

Notes:

- QA_ROOT is a layout discipline, not a PF12 Evidence Catalog path; PF12-governed indexing remains under `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` in later PRs.
- Existing QA_ROOT directories (e.g., `audit/qa/hde-epic020/`) remain intact and are not modified by this scaffold.
