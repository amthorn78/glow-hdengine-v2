QA harness root for HDE-EPIC020 (Separation Pass 1 — Error & Identity Surfaces).
Use the per-surface subdirectories to store PF19-compliant QA artifacts for D1 errors, D2 CLI presenter/emitter, and D3 `/internal/version` identity runs.

## EPIC020 bundle scaffolding (Candidate 1)

- Rails: run under the closed posture expected by PF09/PF19 — `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, and `APP_ENV=dev`.
- Script: `audit/qa/hde-epic020/run_epic020_bundles.sh` builds EPIC020 bundles/manifests via `python -m tools.evidence.epic020_bundle build --epic-id HDE-EPIC020` and runs `python tools/evidence/update_evidence_index.py --epic-id HDE-EPIC020 --check` for local verification.
- Artifact lookup: the script prints the governed bundle/manifest paths discovered in `docs/evidence/INDEX.json` so QA reviewers can inspect the candidate evidence under `artifacts/epic020/bundles/`.

This scaffolding mirrors PF19/PF20 QA expectations but does not redefine the QA Plan; PF-Canon remains authoritative for tokens and coverage.
