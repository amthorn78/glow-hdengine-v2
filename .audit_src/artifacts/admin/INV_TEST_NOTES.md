# INV test evidence — FIX-CLI-ADMIN-SIDECAR-INV-TEST-001R

## Commands & env (redacted)
- SAFE_MODE=1
- ALLOW_NETWORK / ENGINE_PROVIDER / HD_API_KEY / GEO_API_KEY unset
- Invocations:
  1) hdctl showcompat --a-birthdate 1990-05-04 --a-birthtime 14:22 --a-place "Austin, US" --a-tz Europe/Amsterdam \
                      --b-birthdate 1992-07-19 --b-birthtime 08:05 --b-place "New York, US" --b-tz Europe/Amsterdam
  2) hdctl showcompat [same args] --showmath <test-scoped path>

## Interface note
- Current interface uses `--showmath <path>` (no `--admin-out` flag yet). Sidecar path was passed explicitly.
  If standardized later, the test will prefer `--admin-out <path>`.

## Sidecar path (relative)
- Set by the test under `tmp_path/admin_inv/compat_math.json`.

## Stdout hexdump tail (final `0a`)
- Both runs’ stdout end with byte `0x0a` (newline). See test assertions in
  `tests/hdctl/test_cli_admin_sidecar_invariance.py`.

## Permissions
- Sidecar written with mode **0600** (verified via `stat` in test).

## Notes
- Stdout bytes identical between runs (invariant).
- Stderr empty; public stdout LF/BOM hygiene OK; no CR.
- Test is hermetic (no global scans) and SAFE-pinned (no network).
