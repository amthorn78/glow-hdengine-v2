# PF14 — EPIC017 mechanics & CI (paste-ready)

## Ordering and single-emitter rules
- Ordering layer lives under `engine/order/`; comparators enforce deterministic tie-breaks and AB↔BA identity (`engine.order.abba_identity.bytes`).
- Single-emitter rule: CLI and Reader share the canonical emitter; compatibility artifacts remain numeric-free and LF-terminated.

## Evidence pipeline
- Evidence refresh scripts: `tools/evidence/update_evidence_index.py`, `tools/order/generate_ordering_artifacts.py`, `tools/evidence/orientation_demo.py`.
- Sequence: render/update artifacts → update human index → run `python tools/evidence/update_evidence_index.py` → run CI mirror schema check.
- Path proofs required for every governed artifact; mtime_utc records refresh time (monotone, not expected to equal stat()).

## CI posture
- Rails for EPIC017 work: SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC.
- CI checks: mirror schema (`CI_CHECK_MIRROR_SCHEMA_OK`), final LF (`CI_CHECK_FINAL_LF_OK`), ordering determinism (`TIEBREAK_TOTAL_ORDER_OK` evidence), and doc-delta presence (`DOC_DELTA_PRESENT_OK`).
- Machine mirror self-record (`index.machine_mirror`) must be regenerated whenever governed artifacts change.
