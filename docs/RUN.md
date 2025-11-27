# RUN — Developer flight checks (EPIC018)

## Rails
- Pin determinism env: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0` (or call `engine.runtime.determinism_env.ensure_determinism_env`).
- Disable auto-reload when capturing evidence. Reader harness binds to http://127.0.0.1:5000 when run locally.

## Quick checks
- Env pins: `python scripts/ensure_env.py` → expect `[ENV] OK` with rails above.
- Serializer parity: `pytest -q tests/test_sercanon.py` (runs under pinned locale/timezone).

## Evidence and guard workflow
```bash
# CLI guards (D3)
python tools/cli/serializer_grep_guard.py
python tools/cli/emitter_symbol_proof.py

# Evidence skeleton updates (D4)
python tools/evidence/update_evidence_index.py
python tools/evidence/orientation_demo.py
python tools/evidence/run_sanity_pipeline.py
```
Outputs are governed and require `.path_proof.txt` plus INDEX/mirror updates.

## Config & bundles (D5/D6)
```bash
python tools/config/generate_config_artifacts.py
python tools/config/generate_bundles.py
python tools/evidence/update_evidence_index.py  # index generated artifacts under PF12 discipline
```
The config acceptance map lives at `audit/EPIC-018_config_acceptance_map.json` (governed).

## Service entry (dev harness)
```bash
python -m adapter.http_reader
```
APP_ENV gating applies; use for local parity checks only. Closed rails remain required for captures.
