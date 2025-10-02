# CHANGELOG

## 2025-10-01 — Alpha docs/playbooks refresh (v1.2)

### [A3] CLI Alpha Public Invariant (docs/CLI_commands.md v1.2)
- Public stdout pinned to canonical key set and order:
  `["categories","eligible","idempotence_hash","meta","release_id"]` (sorted-keys JSON), one trailing LF, BOM-free, ANSI-free.
- Categories rule clarified: single element with only `{"id":"harmony","band":"Cool|Open|Warm|Glow"}`.
- Idempotence preimage rule affirmed (lowercase sha256 over canonical preimage).
- Sidecar gate hardened: requires `--showmath` AND `--admin-out` AND (`--admin` OR `HD_ADMIN=1`);
  negative gate → exit **2**, **stdout empty**, no file; positive gate → **atomic**, **0600**, **LF**.
- TS‑v0 in A3/A5 remains **minimal** (no admin numerics).
- Determinism: AB↔BA parity and two‑run identity required.
- Minimal artifacts standardized: `cli_stdout_AB.json`, `cli_stdout_BA.json`, `release_id.txt`, `IDENTITY_OK.txt`, `validation.log`
  (sidecar only if gate exercised).
- Release identity discipline: `scripts/release_id.sh` prints a single **64‑hex + LF** (no args, no extra text).

### [A5] Reader v1 Minimal API (docs/server/reader_v1.md v1.2)
- Dev harness only: `APP_ENV!=dev` → 403 with `{"error":"forbidden"}\n`, no filesystem access.
- Path policy: **relative** `a`/`b` resolved under `fixtures/charts/`; reject absolute paths, traversal, symlinks.
- Transport: `Content-Type: application/json; charset=utf-8` for success & errors; **no ETag/Cache-Control**, no 304 (A6 will add).
- Public bytes equal CLI bytes for AB and BA; optional two‑run identity.
- Error bodies: single‑line JSON + LF with tokens `invalid_path|invalid_json|missing_tz_A|missing_tz_B`.
- Provenance: record `EMITTER_SHA256=<64hex>` for `engine/emit_public.py`.
- Minimal artifacts standardized: `reader_AB.json`, `reader_BA.json`, `headers_AB.txt`, `headers_BA.txt`, `validation.log`.

### [Emitters] Single Emitter Canon (docs/architecture/emitters.md v1.2)
- Canonical module `engine/emit_public.py` required by both CLI and Reader.
- Public envelope keys/order and preimage rule pinned; AB↔BA parity required.
- Purity rules: no import‑time I/O, no network, no file writes; keys‑only logs.
- Evidence: record `EMITTER_SHA256` in A5 validation log.

### [Alpha Acceptance] Consolidated Gate (docs/alpha_acceptance.md v1.2)
- Aggregates A3/A5 invariants, minimal artifacts, and minimal validation markers.
- Governance restated: **single revert‑friendly commit to `main`** with evidence under `artifacts/cards/<CARD>/`; no PRs for final approval.
- SAFE rails: acceptance runs with `SAFE_MODE=1`; network only if **both** `SAFE_MODE=0` and `ALLOW_NETWORK=1` are set.

---

**Operator note:** The repo docs above are implementation playbooks. Canonical project docs (Architecture & Design, Environment & Integration Plan, Governance/Process, Engine Math/TS‑v0) must carry the matching paste‑ready inserts and cross‑links.
