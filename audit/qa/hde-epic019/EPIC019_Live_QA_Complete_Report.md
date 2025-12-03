# EPIC019 Live QA — Complete Session Report

**Generated:** 2025-12-03T02:54:51Z

---

## D0 — Session Overview

### Surfaces Exercised

- **D3:** dev sampler HTTP via DEV_SAMPLER_URL (closed rails)
- **D6:** scripts/qa/d6_live_vendor_qa.py (open rails)

### Rails Configuration

- **Closed rails (D3):**  `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`
- **Open rails (D6):**    `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `APP_ENV=dev`
- **Locale/TZ:**          `LC_ALL=C`, `LANG=C`, `TZ=UTC`

### High-Level Outcomes

- **D3:** FAIL_BEHAVIOR
- **D6:** OK

### Canon Anchors (D0)

- PF10 — HDE-Build Notes (EPIC019 D3/D6)
- PF19 — Glow QA Guide (D0, Live Vendor QA)
- PF20 — HDE-Phased Epics (EPIC019)
- PF14 — HDE-Mechanics Guide

### Notes

- D3: dev sampler `APP_ENV=prod` gating remains behaviorally failing; see D3 summary.
- D6: Live Vendor QA harness ran under open rails and classified OK / FAIL_VENDOR / FAIL_TOOLING as expected.

---

## D3 — Dev Sampler HTTP Live QA Summary

### Checks

| Check | Result |
|-------|--------|
| Two-run identity | OK |
| Seed-only behavior | OK |
| APP_ENV gating (prod) | FAIL_BEHAVIOR |

### Evidence Files

- `D3_env_rails.log`
- `D3_http_run1/2.headers` + `.body`
- `D3_http_seed_111.body` / `D3_http_seed_222.body`
- `D3_http_prod.headers` / `D3_http_prod.body`
- `D3_live_qa_run.log`
- dev_sampler_live_qa JSONL logs

### Canon Anchors (D3)

- PF10 — HDE-Build Notes (EPIC019 D3)
- PF19 — Glow QA Guide (Live QA classification)
- PF20 — HDE-Phased Epics (EPIC019 D3)
- PF14 — HDE-Mechanics Guide (dev sampler HTTP harness)

### Tokens (names only)

- `ENV_RAILS_POLICY_OK`
- `DISCOVERY_BASELINE_OK` (supporting evidence via D0 & rails)

### Notes

- Two-run identity and seed-only behavior matched expectations under closed rails.
- `APP_ENV=prod` scenario still returns a sampler payload in at least one harness case; currently treated as FAIL_BEHAVIOR for gating semantics.

---

## D6 — Live Vendor QA Summary

### Harness Run

| Property | Value |
|----------|-------|
| Command | `python scripts/qa/d6_live_vendor_qa.py` |
| APP_ENV | dev |
| Rails | `SAFE_MODE=0`, `ALLOW_NETWORK=1`, `LC_ALL=C`, `LANG=C`, `TZ=UTC` |

### Evidence Files

- `rails_snapshot.json`
- `happy_path.jsonl`
- `fail_vendor.jsonl`
- `fail_tooling.jsonl`
- `D6_vendor_harness_run.log`

### Classification Results

| Category | Result | Evidence |
|----------|--------|----------|
| Overall D6 result | OK | All scenarios classified correctly |
| Happy-path records | OK | At least one OK record with 2xx BodyGraph response |
| Vendor-failure records | FAIL_VENDOR | 4xx vendor error (e.g., 401 Invalid API Key) |
| Tooling-failure records | FAIL_TOOLING | Invalid base URL / connectivity issues |

### Canon Anchors (D6)

- PF10 — HDE-Build Notes (EPIC019 D6)
- PF19 — Glow QA Guide (Live Vendor QA)
- PF20 — HDE-Phased Epics (EPIC019 D6)
- PF04 — Governance (SAFE rails / env policy)

### Tokens (names only)

- `LIVE_VENDOR_TRANSPORT_OK`
- `OPEN_RAILS_ENV_OK`
- `DISCOVERY_BASELINE_OK`

### Notes

- Vendor happy path succeeded under open rails and was classified as OK.
- Vendor credential errors (e.g., 401 Invalid API Key) were classified as FAIL_VENDOR.
- Tooling/infra failures (e.g., invalid base URL) were classified as FAIL_TOOLING.

---

## Summary

### Overall EPIC019 Live QA Status

| Surface | Status | Notes |
|---------|--------|-------|
| D3 (Dev Sampler HTTP) | FAIL_BEHAVIOR | Prod gating issue; two-run identity and seed behavior OK |
| D6 (Live Vendor QA) | OK | All three classification categories (OK/FAIL_VENDOR/FAIL_TOOLING) present and correct |

### Key Findings

1. **D3 (Closed Rails)**: Two critical checks passed (identity, seed behavior), but APP_ENV=prod gating behavior failed — sampler payload returned when prod should be blocked.
2. **D6 (Open Rails)**: All vendor QA scenarios executed correctly under open-rails posture with proper classification of success, vendor errors, and tooling errors.
3. **Environment Rails**: Closed and open rails configurations were correctly applied and logged for audit.

### Deliverables Present

- Session-level overview (D0)
- Dev sampler live QA evidence (D3) with consolidated artifacts
- Live vendor QA evidence (D6) with consolidated artifacts
- All canonical references and token names documented

---

End of EPIC019 Live QA Complete Session Report.
