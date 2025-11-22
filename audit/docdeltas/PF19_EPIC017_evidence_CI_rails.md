# PF19 — EPIC017 evidence & CI rails (paste-ready)

## Default rails
- Run evidence/CI jobs with SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC.
- Machine mirror generation and ordering artifacts use closed-rails data only; no DB/network calls.

## mtime semantics
- NEW CANON (EPIC017 WS-D4): `mtime_utc` in path proofs records the refresh-time mtime (seconds precision), monotone vs. stat(); drift across clones is tolerated if produced_at_utc is earlier or equal.

## Mirror and schema checks
- `artifacts/evidence_index.jsonl` must include `index.machine_mirror` self-record; hash over body-only lines; size_bytes includes the full mirror.
- CI gates: `ci/checks/check_mirror_schema.sh` (schema), tests under `tests/ops/test_evidence_index.py` (mtime monotonicity), plus final LF checks on governed artifacts.

## Orientation demo & proofs
- `topology.orientation_demo` remains the exemplar for evidence path-proofs and mirror wiring; include it in PF19 acceptance tables.
