# EPIC019 evidence overview (sampler + Engine Core)

## Evidence layers
- **Human index**: `docs/evidence/INDEX.json`
- **Machine mirror**: `artifacts/evidence_index.jsonl`
- **Path proofs**: `.path_proof.txt` siblings accompany governed artifacts.
- **Orientation demo**: `python tools/evidence/orientation_demo.py` validates mirror self-proof posture.
- **Sanity pipeline**: `python tools/evidence/run_sanity_pipeline.py` runs serializer parity plus sampler/Engine Core generators under closed rails.

## Generators (closed rails)
- Sampler evidence: `python tools/evidence/generate_sampler_evidence.py` (dev sampler CLI + HTTP harness parity; seed replay/diversity/ABBA/two-run logs).
- Engine Core evidence: `python tools/evidence/generate_engine_core_evidence.py` (purity, JSON compare, ABBA, two-run identity).
- Index updates: `python tools/evidence/update_evidence_index.py` (refreshes human index, mirror, proofs).

## Dev sampler QA families (D3)
- Harnesses: `scripts/qa/dev_sampler_healthcheck.py` (diagnostic gating) and `scripts/qa/dev_sampler_live_qa.py` (Live QA across APP_ENV permutations); both run under closed rails with APP_ENV gating.
- Artifacts: governed logs under `audit/qa/hde-epic019/dev_sampler_http/` with reader logs in subdirectories; mirrored into Index/Mirror and bound to D3 tokens in `docs/acceptance_map_epic019.json` + `docs/acceptance_maps.json`.

## D6 vendor Live QA family (open rails)
- Harness: `scripts/qa/d6_live_vendor_qa.py` (controlled vendor test identity; allows `ALLOW_NETWORK=1`, SAFE_MODE may be 0/1; not part of determinism CI).
- Outcomes: classified (`OK`, `FAIL_VENDOR`, `FAIL_TOOLING`); governed logs and rails snapshot live under `audit/qa/hde-epic019/d6-vendor-live-qa/` with `.path_proof.txt` siblings and mirror entries.
- Acceptance: bound to D6 tokens in `docs/acceptance_map_epic019.json` and reflected in `docs/acceptance_maps.json`.

See PF titles “HDE-Schemas & Artifacts”, “HDE-Mechanics Guide”, and “Glow QA Guide” for canonical behavior and token semantics.
