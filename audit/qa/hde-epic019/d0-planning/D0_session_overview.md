# EPIC019 Live QA — D0 Session Overview

## Surfaces Exercised

- D3: dev sampler HTTP via DEV_SAMPLER_URL (closed rails)
- D6: scripts/qa/d6_live_vendor_qa.py (open rails)

## Rails

- Closed rails (D3):  SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev
- Open rails (D6):    SAFE_MODE=0, ALLOW_NETWORK=1, APP_ENV=dev
- Locale/TZ:          LC_ALL=C, LANG=C, TZ=UTC

## Outcomes (high-level)

- D3: FAIL_BEHAVIOR
- D6: OK

## Canon Anchors

- PF10 — HDE-Build Notes (EPIC019 D3/D6)
- PF19 — Glow QA Guide (D0, Live Vendor QA)
- PF20 — HDE-Phased Epics (EPIC019)
- PF14 — HDE-Mechanics Guide

## Notes

- D3: dev sampler APP_ENV=prod gating remains behaviorally failing; see D3 summary.
- D6: Live Vendor QA harness ran under open rails and classified OK / FAIL_VENDOR / FAIL_TOOLING as expected.
