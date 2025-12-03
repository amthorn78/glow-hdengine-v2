# EPIC019 D6 — Live Vendor QA Summary

## Harness Run

- Command:   python scripts/qa/d6_live_vendor_qa.py
- APP_ENV:   dev
- Rails:     SAFE_MODE=0, ALLOW_NETWORK=1, LC_ALL=C, LANG=C, TZ=UTC

## Files

- rails_snapshot.json
- happy_path.jsonl
- fail_vendor.jsonl
- fail_tooling.jsonl
- D6_vendor_harness_run.log

## Classification (EPIC019 D6)

- Overall D6 result:            OK
- Happy-path records (OK):      at least one OK record with 2xx BodyGraph
- Vendor-failure records:       at least one FAIL_VENDOR record for 4xx vendor error (e.g. 401 Invalid API Key)
- Tooling-failure records:      at least one FAIL_TOOLING record for invalid base URL / connectivity

## Canon Anchors

- PF10 — HDE-Build Notes (EPIC019 D6)
- PF19 — Glow QA Guide (Live Vendor QA)
- PF20 — HDE-Phased Epics (EPIC019 D6)
- PF04 — Governance (SAFE rails / env policy)

## Tokens (names only)

- LIVE_VENDOR_TRANSPORT_OK
- OPEN_RAILS_ENV_OK
- DISCOVERY_BASELINE_OK

## Notes

- Vendor happy path succeeded under open rails and was classified as OK.
- Vendor credential errors (e.g. 401 Invalid API Key) were classified as FAIL_VENDOR.
- Tooling/infra failures (e.g. invalid base URL) were classified as FAIL_TOOLING.
