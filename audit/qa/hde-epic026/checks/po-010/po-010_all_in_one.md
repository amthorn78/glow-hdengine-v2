# HDE-EPIC026 — CHECK po-010 All-in-One Report

## Scope

- Epic: HDE-EPIC026
- Check: po-010
- Plan reference: r11 Live QA Plan HDE-EPIC026.md
- Evidence root: `audit/qa/hde-epic026`
- Check directory: `audit/qa/hde-epic026/checks/po-010`

---

## Final status

- Outcome: PASS
- pass_fail: PASS
- fail_status: NONE
- Recorded check timestamp (primary header): 2026-02-26T21:42:01Z

PASS basis for this run:

1. `hdctl showcompat --help` succeeded (`showcompat_help_rc=0`).
2. Catalog extract includes expected dev conjunction endpoints (`/dev/reader/conjunction`, `/dev/writer/conjunction`, `/dev/sampler/conjunction`).

---

## Actions taken (execution trace)

1. Set deterministic pins and closed rails posture:
   - `LC_ALL=C`, `LANG=C`, `TZ=UTC`
   - `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`
2. Validated required prerequisites:
   - `docs/ENDPOINTS_CATALOG.json` exists.
   - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh` exists.
3. Created check-scoped evidence directory:
   - `audit/qa/hde-epic026/checks/po-010/`
4. Captured CLI help surface:
   - `hdctl showcompat --help > showcompat_help.txt 2> showcompat_help.err`
5. Extracted dev conjunction endpoints from endpoint catalog into JSON evidence.
6. Evaluated PASS/FAIL per plan criteria.
7. Wrote `primary.log` header/body and appended manifest linkage via helper.
8. Verified required deliverables exist.

---

## Required deliverables (plan authoritative)

- `audit/qa/hde-epic026/checks/po-010/primary.log` ✅
- `audit/qa/hde-epic026/checks/po-010/showcompat_help.txt` ✅
- `audit/qa/hde-epic026/checks/po-010/catalog_extract_dev_endpoints.json` ✅

---

## Evidence inventory (all artifacts in check directory)

### Required

- `primary.log`
  - sha256: `c42dc1684d02d48a20b095240ea4e5eb90011a82cc2f55867d73bd634fe988ad`
  - Purpose: step header + PASS/FAIL + embedded evidence appendix.
- `showcompat_help.txt`
  - sha256: `f9cdc8861dee7e3fb5f34c244e56a66f4660f679f29e6cd0badf28690ea82035`
  - Purpose: captured `hdctl showcompat --help` output.
- `catalog_extract_dev_endpoints.json`
  - sha256: `40328de2e1a590f17d24eb43972c9e9be4a91ae9e74dbad82c6895435d841c1e`
  - Purpose: machine-readable extraction of expected dev conjunction endpoints.

### Supporting (non-required, run-generated)

- `showcompat_help.err`
  - sha256: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
  - Notes: empty file (no stderr output captured).
- `artifacts.json`
  - sha256: `1d1e2da3aa1072806eed334b10b232db2f64815caa4fa41fe6b623774ff36d76`
  - Notes: local artifact-role mapping used by `qa_append_manifest`.

---

## Key proof facts from artifacts

### A) `primary.log`

- `pass_fail: PASS`
- `fail_status: NONE`
- `captured_env`: `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`
- `commands`: `[{"cmd":"hdctl showcompat --help"}]`
- Body contains `showcompat_help_rc=0`.

### B) `showcompat_help.txt`

- Help output includes conjunction support:
  - `--conjunction`
  - `--user-a`
  - `--user-b`

### C) `catalog_extract_dev_endpoints.json`

- `targets` include:
  - `/dev/reader/conjunction`
  - `/dev/sampler/conjunction`
  - `/dev/writer/conjunction`
- `matches` contains all 3 expected dev conjunction endpoints in this run.

---

## Manifest linkage note

Remediation has been applied using the canonical helper flow (`qa_append_manifest`) with the correct argument order.

Current manifest state:

- A prior malformed `po-010` row remains in history (from initial append call with misordered args).
- A corrected `po-010` row is present and canonical:
  - `check_id`: `po-010`
  - `status`: `PASS`
  - `log_path`: `checks/po-010/primary.log`
  - `sha256`: `c42dc1684d02d48a20b095240ea4e5eb90011a82cc2f55867d73bd634fe988ad`
- Manifest/path-proof consistency:
  - `qa_step_logs_manifest.json` sha256: `0f0ddd07f69b97b9bdb69b69ff77c2c5f2fec069042a71ed259bc9588529ccbd`
  - `qa_step_logs_manifest.json.path_proof.txt` `manifest_sha256` matches the same value.

---

## Raw evidence references

- `audit/qa/hde-epic026/checks/po-010/primary.log`
- `audit/qa/hde-epic026/checks/po-010/showcompat_help.txt`
- `audit/qa/hde-epic026/checks/po-010/showcompat_help.err`
- `audit/qa/hde-epic026/checks/po-010/catalog_extract_dev_endpoints.json`
- `audit/qa/hde-epic026/checks/po-010/artifacts.json`
- `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`