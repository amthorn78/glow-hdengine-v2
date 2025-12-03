# D6 Live Vendor QA — Consolidated Artifacts

**Step 4 — D6 Live Vendor QA harness (open rails)**

Generated: 2025-12-03T02:54:51Z

---

## File: D0_env_rails_open.log

Open-rails environment snapshot (SAFE_MODE=0, ALLOW_NETWORK=1):

```log
ALLOW_NETWORK=1
APP_ENV=dev
HDAPI_BASE_URL=https://api.humandesignapi.nl/v1
LANG=C
LC_ALL=C
SAFE_MODE=0
TZ=UTC
```

---

## File: D6_vendor_harness_run.log

Full stdout/stderr from `python scripts/qa/d6_live_vendor_qa.py`:

```
(Empty — harness completed successfully with no output)
```

---

## File: rails_snapshot.json

JSON snapshot of open-rails posture and vendor /bodygraphs surface:

```json
{
  "notes": "Open-rails vendor QA per PF04/PF19 with classification log",
  "payload_keys": [
    "birthdate",
    "birthtime",
    "location"
  ],
  "pf_canon_refs": [
    "PF04 — HDE-Governance",
    "PF05 — HDE-CLI-API-Vendor-Ref",
    "PF07 — Glow Infrastructure",
    "PF19 — Glow QA Guide"
  ],
  "rails": {
    "ALLOW_NETWORK": "1",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "0",
    "TZ": "UTC"
  },
  "schema": "epic019-d6-vendor-live-qa",
  "surface": "engine.cli vendor HTTP POST /bodygraphs",
  "vendor_host": "api.humandesignapi.nl"
}
```

---

## File: happy_path.jsonl

Classification log for vendor success cases (result: OK, 2xx BodyGraph responses):

```jsonl
{"rails": {"ALLOW_NETWORK": "1", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "0", "TZ": "UTC"}, "request": {"headers_present": ["Accept", "Content-Type", "HD-Api-Key", "HD-Geocode-Key"], "method": "POST", "payload_keys": ["birthdate", "birthtime", "location"], "url": "https://api.humandesignapi.nl"}, "response": {"body_excerpt": {"activations": {"design": {"earth": "21.5", "jupiter": "59.2", "mars": "33.1", "mercury": "50.6", "moon": "2.1", "neptune": "26.2", "north_node": "40.3", "pluto": "57.5", "saturn": "47.4", "south_node": "37.3", "sun": "48.5", "uranus": "43.1", "venus": "32.6"}, "personality": {"earth": "39.3", "jupiter": "40.5", "mars": "64.4", "mercury": "10.4", "moon": "62.4", "neptune": "26.5", "north_node": "59.1", "pluto": "32.1", "saturn": "6.5", "south_node": "55.1", "sun": "38.3", "uranus": "43.6", "venus": "13.2"}}, "authority": "Emotional", "birth_date_UTC": "1980-01-03T08:30:00.000Z", "centers": ["Ajna", "Ego", "G", "Head", "Root", "Sacral", "Solar Plexus", "Spleen", "Throat"], "channels_long": ["Perfected Form (10-57)", "The Prodigal (13-33)", "Community (37-40)", "Emoting (39-55)", "Abstraction (47-64)", "Intimacy (6-59)"], "channels_short": ["10-57", "13-33", "37-40", "39-55", "47-64", "6-59"], "circuitries": "Individual, Collective Abstract, Tribal", "cognition": "Inner Vision", "definition": "Triple Split Definition", "determination": "Indirect Light", "distraction": "Wanting", "environment": "Wet Kitchens", "gates": ["38", "39", "59", "55", "62", "10", "64", "13", "40", "6", "43", "26", "32", "48", "21", "37", "2", "50", "33", "47", "57"], "incarnation_cross": "Right Angle Cross of Tension (38/39 | 48/21)", "motivation": "Guilt", "not_self_theme": "Frustration", "perspective": "Survival", "profile": "3/5", "signature": "Satisfaction", "strategy": "Wait to Respond", "transference": "Need", "type": "Generator", "variables": "PRL DRL"}, "body_keys": ["activations", "authority", "birth_date_UTC", "centers", "channels_long", "channels_short", "circuitries", "cognition", "definition", "determination", "distraction", "environment", "gates", "incarnation_cross", "motivation", "not_self_theme", "perspective", "profile", "signature", "strategy", "transference", "type", "variables"], "duration_ms": 132.83, "status": 200}, "result": "OK", "scenario": "happy_path", "timestamp_utc": "2025-12-03T02:54:51.044880+00:00", "vendor_host": "api.humandesignapi.nl"}
```

---

## File: fail_vendor.jsonl

Classification log for vendor failure scenarios (result: FAIL_VENDOR, vendor 4xx/5xx):

```jsonl
{"rails": {"ALLOW_NETWORK": "1", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "0", "TZ": "UTC"}, "request": {"headers_present": ["Accept", "Content-Type", "HD-Api-Key", "HD-Geocode-Key"], "method": "POST", "payload_keys": ["birthdate", "birthtime", "location"], "url": "https://api.humandesignapi.nl"}, "response": {"body_excerpt": {"code": 401, "message": "Invalid API Key", "status": "error"}, "body_keys": ["code", "message", "status"], "duration_ms": 46.07, "status": 401}, "result": "FAIL_VENDOR", "scenario": "invalid_credentials", "timestamp_utc": "2025-12-03T02:54:51.178392+00:00", "vendor_host": "api.humandesignapi.nl"}
```

---

## File: fail_tooling.jsonl

Classification log for tooling/infra failure scenarios (result: FAIL_TOOLING only):

```jsonl
{"rails": {"ALLOW_NETWORK": "1", "LANG": "C", "LC_ALL": "C", "SAFE_MODE": "0", "TZ": "UTC"}, "request": {"headers_present": ["Accept", "Content-Type", "HD-Api-Key", "HD-Geocode-Key"], "method": "POST", "payload_keys": ["birthdate", "birthtime", "location"], "url": "https://invalid.invalid"}, "response": {"body_keys": [], "duration_ms": 14.81, "status": null}, "result": "FAIL_TOOLING", "scenario": "bad_base_url", "timestamp_utc": "2025-12-03T02:54:51.225013+00:00", "vendor_host": "invalid.invalid"}
```

---

## Summary

**Artifacts present:**
- ✓ `D0_env_rails_open.log` — Open-rails environment (SAFE_MODE=0, ALLOW_NETWORK=1)
- ✓ `D6_vendor_harness_run.log` — Harness run log (empty, no errors)
- ✓ `rails_snapshot.json` — Open-rails posture + vendor surface snapshot
- ✓ `happy_path.jsonl` — Success case (result: OK, 200 status from vendor)
- ✓ `fail_vendor.jsonl` — Vendor failure (result: FAIL_VENDOR, 401 unauthorized)
- ✓ `fail_tooling.jsonl` — Tooling failure (result: FAIL_TOOLING, bad base URL)

**Classification results:**
- Happy path: 1 OK entry
- Vendor failures: 1 FAIL_VENDOR entry (invalid credentials)
- Tooling failures: 1 FAIL_TOOLING entry (network/URL issue)

---

End of consolidated D6 vendor QA artifacts.
