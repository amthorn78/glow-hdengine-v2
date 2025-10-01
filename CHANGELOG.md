# CHANGELOG

## 2025-10-01

### [A3] CLI Alpha Public Invariant
- Deterministic, numeric-free stdout (bands only), LF-terminated, BOM-free, ANSI-free.
- Idempotence preimage rule pinned; embedded `idempotence_hash` verified.
- AB<->BA byte identity and two-run identity required.
- TS-v0 mapping fix: Generator and Manifesting Generator -> "Wait to respond"; Projector -> "Wait for the invitation"; Manifestor -> "Inform"; Reflector -> "Wait a lunar cycle".
- Features clarified: `strategy_match`, `sacral_pair` (true only when both are Generator/MG), `projector_to_generator`.
- Admin sidecar gate enforced (requires `--showmath` AND `--admin-out` AND (`--admin` OR `HD_ADMIN=1`)); negative gate -> exit 2; sidecar 0600 and LF.
- Exit codes and acceptance markers documented; artifact paths standardized under `artifacts/cards/A3/`.

### [A5] Reader v1 Minimal API
- Single emitter canon: both CLI and Reader use `engine/emit_public.py` for public bytes.
- Reader body equals CLI body for identical inputs (AB and BA); two-run identity required.
- Minimal transport for A5: `Content-Type: application/json; charset=utf-8` only; no ETag/Cache-Control (added in A6).
- Dev harness only: APP_ENV gating required; path whitelist `fixtures/charts/*`; deny traversal and symlinks.
- Error bodies are one-line JSON with trailing LF.
- Provenance pins added (`EMITTER_SHA256`); artifact names standardized under `artifacts/cards/A5/`.

---

**Operating mode note:** Acceptance delivery is a single revert-friendly commit to `main` with evidence under `artifacts/cards/<CARD>/`. No PRs for final approval; PO runs the closeout.