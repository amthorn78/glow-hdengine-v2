# Math Inventory Overview

## Executive summary
- Total items documented: 15
- Categories covered: hashing, time, rounding, normalization, banding, scoring, random, constraint.
- Primary concentration in `engine` package (11 items), with supplemental logic in `adapter`, `scripts`, and SQL migrations.

## By category

### Rounding
- **engine.compat.compute._round_half_up** — `floor(x + 0.5)` converts floats to nearest int (half-up), constant 0.5. 【engine/compat/compute.py†L8-L9】

### Normalization
- **engine.compat.compute._clamp** — clamps scores into `[0, 100]` via nested ternary. 【engine/compat/compute.py†L11-L12】

### Banding
- **engine.compat.compute.band_for** — applies inclusive thresholds 24/49/74 to produce `Cool/Open/Warm/Glow`. 【engine/compat/compute.py†L14-L18】【engine/compat/thresholds.py†L9-L13】

### Scoring
- **engine.compat.compute._score_for** — hashes pair+category, mods 101, scales by `(0.5 + 0.5*w)`, rounds half-up, and clamps to 0–100. Constants: 101, 0.5. 【engine/compat/compute.py†L20-L27】

### Hashing
- **engine.compat.ordering.normalize_pair** — orders records by UID, breaking ties with SHA-256 of sorted payload. 【engine/compat/ordering.py†L7-L20】
- **engine.compat.ordering.pair_key** — builds `uid_a|uid_b` composite key from normalized pair. 【engine/compat/ordering.py†L13-L24】
- **engine.config.provider_loader._ensure_cid** — deterministically derives `CID-` + first 8 hex of SHA-256(seed). 【engine/config/provider_loader.py†L114-L119】
- **scripts.release_id_tools.main (release_id_generation)** — computes SHA-256 of manifest bytes and rechecks for equality. 【scripts/release_id_tools.py†L20-L33】

### Random
- **engine.util.input_validators.ensure_cid** — validates CID tokens; otherwise emits `CID-` + `secrets.token_hex(8)` (crypto RNG). 【engine/util/input_validators.py†L59-L70】

### Time
- **engine.util.input_validators.parse_date_yyyy_mm_dd** — regex + `datetime.strptime` for calendar dates. 【engine/util/input_validators.py†L21-L28】
- **engine.util.input_validators.parse_time_hh_mm** — splits HH:MM, casts to ints, guards hour ≤23. 【engine/util/input_validators.py†L30-L36】
- **adapter.retry_after.parse_retry_after_ms** — seconds→ms via `*1000`; HTTP-date path uses `max(0, Δ)` before int cast. Constants: 1000. 【adapter/retry_after.py†L4-L27】
- **engine.providers.vendor_http_hdapi._to_dd_mmm_yyyy** — regex extracts Y/M/D and maps month numbers to English abbreviations. 【engine/providers/vendor_http_hdapi.py†L26-L41】

### Constraint
- **scripts.release_id_tools.validate_manifest (manifest_entry_size_check)** — flags manifest entries whose `size` is missing, non-int, or `<0`. Constant: 0. 【scripts/release_id_tools.py†L6-L16】
- **migrations/005_identity.sql (hde.meta_invocation_checks)** — SQL `CHECK` constraints enforcing INV-prefixed IDs and 64-hex SHA fields. 【migrations/005_identity.sql†L6-L12】

## Determinism & randomness
Only `engine.util.input_validators.ensure_cid` uses nondeterministic entropy via `secrets.token_hex(8)` when synthesizing correlation IDs; all other computations are deterministic given inputs.

## Open questions / gaps
- Wider repository math (e.g., deprecated modules, vendor fallbacks) not yet cataloged; additional hashing/normalization logic may exist beyond the 15 documented items.
- Dynamic provider overrides might introduce alternative CID generation paths that were not examined in this static pass.
