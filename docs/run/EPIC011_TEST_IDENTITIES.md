# EPIC011 Synthetic Test Identity

## Canonical identity (single home)
EPIC011 harnesses share one synthetic profile so DB rows, ingest proofs, and parity captures all talk about the same BodyGraph. The profile is pinned in `engine/bodygraph/ingest.py` via `SYNTHETIC_USER_ID_MAP` and surfaced in repo-wide AGENT rules.

| Property | Value | Notes |
| --- | --- | --- |
| user_id | `epic011-s10-invariance-1` | Alias string used in all CLI/HTTP calls. Mapped to UUID `3fa85f64-5717-4562-b3fc-2c963f66afab` inside the ingest/resolver path so the DB row remains stable. |
| birthdate | `1990-01-01` | Synthetic metadata that accompanies the identity during ingest/vendor captures. |
| birthtime | `12:00` | Synthetic metadata. |
| location | `Amsterdam, Netherlands` | Synthetic metadata. |

The alias map ensures QA can pass the mnemonic `epic011-s10-invariance-1` everywhere (CLI, HTTP, scripts) without exposing or depending on a real user UUID. When the engine needs a UUID (for example `hde.body_graphs.user_id`), it deterministically swaps this alias for the pinned UUID.

## Where this identity is used today
- **Source invariance + parity harnesses (S9/S10/S11)** — `artifacts/bodygraph/source_invariance/*.json`, presenter parity logs, and `tools/evidence/generate_rails_closed_phase1.py` all reference this identity, proving ingest↔DB stability without touching a production user.
- **Resolver + ingest code paths** — `engine/bodygraph/ingest.resolve_db_user_id` and CLI commands such as `python -m engine.cli bg:resolve --user epic011-s10-invariance-1 --source vendor --upsert` exercise the alias bridge and write rows keyed to the mapped UUID.
- **Dev/CI QA plans** — Any harness that needs a deterministic EPIC011 BodyGraph (fixtures, pytest `epic011` marker suites, or `scripts/db_bridge/*`) should use this exact identity and metadata bundle.

If a downstream system needs to translate the synthetic alias to an app-specific identifier, perform that mapping outside the engine and keep it 1:1 so the alias continues to land on the canonical DB row.

## Guidance for QA operators (dev + prod)
1. Treat this identity as the only approved EPIC011 test identity. Do not substitute a “consented prod UUID.”
2. CLI/HTTP examples should refer to the symbolic name `<EPIC011_TEST_USER>` and resolve to `epic011-s10-invariance-1` when run.
3. Populate ingest env vars as:
   ```bash
   export INGEST_TEST_USER_ID=epic011-s10-invariance-1
   export INGEST_TEST_BIRTHDATE=1990-01-01
   export INGEST_TEST_BIRTHTIME=12:00
   export INGEST_TEST_LOCATION="Amsterdam, Netherlands"
   ```
4. Prod QA runbooks (e.g., `RUN_PROD_QA.md`) defer to this document whenever they reference the “EPIC011 synthetic test identity.” Operators only need to ensure any upstream mapping (if their environment expects a UUID) still targets the alias-mapped UUID described above.

## QA notes / RCA
Earlier QA instructions referenced a “consented prod test UUID,” but the engine’s ingest/resolver stack has always been wired to the synthetic alias documented here. This PR closes that doc/QA gap by declaring the alias as the single source of truth and updating the production runbook to reference it directly. No ingest, math, or DB behavior changed.
