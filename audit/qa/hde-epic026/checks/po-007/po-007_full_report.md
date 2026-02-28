# HDE-EPIC026 — Detailed QA Report (po-007)

## Report scope

- Epic: HDE-EPIC026
- Check: `po-007`
- Check name: `PO-007 — Endpoint catalog dev endpoints + sha256 integrity`
- Approved QA plan: `r11 Live QA Plan HDE-EPIC026.md`
- Evidence root: `audit/qa/hde-epic026`
- Date (UTC): 2026-02-25

---

## Executive summary

CHECK `po-007` is **PASS** on final run.

Plan PASS conditions are satisfied:

- `catalog_sha256_check.txt` shows `match=YES`,
- `pytest_rc.txt` is `0` for `tests/http/test_endpoint_catalog.py`, and
- `catalog_extract_dev_endpoints.json` includes the three dev conjunction paths:
  - `/dev/sampler/conjunction`
  - `/dev/reader/conjunction`
  - `/dev/writer/conjunction`

---

## Detailed chronology (all steps run)

### 1) Variable import + setup preflight

- Set `EVIDENCE_ROOT=audit/qa/hde-epic026` (under `audit/qa/`, not under `docs/`).
- Verified required plan loci exist:
  - `docs/ENDPOINTS_CATALOG.json`
  - `docs/ENDPOINTS_CATALOG.json.sha256`
  - `tests/http/test_endpoint_catalog.py`
  - `audit/qa/hde-epic026/checks/po-000/qa_helpers.sh`

### 2) Procedure execution (plan-aligned)

- Ran the repo-plan-aligned `po-007` flow using the existing helper API (`qa_emit_step_log_header`, `qa_append_manifest`).
- Produced all required `po-007` artifacts:
  - sha256 sidecar comparison,
  - catalog dev endpoint extraction,
  - pytest stdout/stderr/rc,
  - `primary.log` + manifest append.

### 3) Log cleanliness remediation

- Initial `primary.log` body captured terminal control-sequence noise due terminal stream behavior.
- Rewrote `po-007` `primary.log` from clean artifact files and appended a fresh manifest row with the updated `primary.log` sha.
- Final authoritative row is the latest `po-007` manifest entry (`timestamp_utc=2026-02-25T17:20:28Z`).

---

## PASS/FAIL criteria evaluation

Plan criteria:

- PASS if:
  - `catalog_sha256_check.txt` shows `match=YES`, and
  - pytest rc is `0` for `tests/http/test_endpoint_catalog.py`, and
  - `catalog_extract_dev_endpoints.json` includes the three dev conjunction paths.

Observed in final run:

- `match=YES` in `catalog_sha256_check.txt`.
- `pytest_rc.txt` contains `0`.
- `catalog_extract_dev_endpoints.json` includes:
  - `/dev/sampler/conjunction`
  - `/dev/reader/conjunction`
  - `/dev/writer/conjunction`

Decision: **PASS**.

---

## Required deliverables and evidence contents

All expected outputs exist under `audit/qa/hde-epic026/checks/po-007/`:

- `primary.log`
- `catalog_sha256_check.txt`
- `catalog_extract_dev_endpoints.json`
- `pytest_stdout.log`
- `pytest_stderr.log`
- `pytest_rc.txt`

### 1) `primary.log`

Path: `audit/qa/hde-epic026/checks/po-007/primary.log`

```log
{"schema": "pf27-step-log-header-v1", "schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-02-25T17:20:28Z", "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "check_id": "po-007", "check_name": "PO-007 — Endpoint catalog dev endpoints + sha256 integrity", "pass_fail": "PASS", "fail_status": "", "intended_tokens": [], "claimed_tokens": [], "commands": ["python (sha256 compare docs/ENDPOINTS_CATALOG.json vs .sha256)", "python (extract dev conjunction endpoints from docs/ENDPOINTS_CATALOG.json)", "python -m pytest -q tests/http/test_endpoint_catalog.py"], "artifacts": [{"path": "catalog_sha256_check.txt", "type": "text", "desc": "catalog sha256 vs sidecar comparison"}, {"path": "catalog_extract_dev_endpoints.json", "type": "json", "desc": "catalog extract for dev conjunction endpoints"}, {"path": "pytest_stdout.log", "type": "log", "desc": "pytest stdout"}, {"path": "pytest_stderr.log", "type": "log", "desc": "pytest stderr"}, {"path": "pytest_rc.txt", "type": "text", "desc": "pytest exit code"}], "pf_refs": ["PF05 §0.2 Scope [Required-Now]", "PF19 §2.2.5 Tooling vs behavior failures (pytest and harnesses)", "PF27 §Step-log header schema expectations (minimum; required)"]}

###
rails=SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev
determinism=LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
computed_sha256=4b766ec46b69df75136611a47d03fd7268fbfed1b8b18cbb44d9b3296874d143
expected_sha256=4b766ec46b69df75136611a47d03fd7268fbfed1b8b18cbb44d9b3296874d143
match=YES

pytest_rc=0
pass_fail=PASS
```

### 2) `catalog_sha256_check.txt`

Path: `audit/qa/hde-epic026/checks/po-007/catalog_sha256_check.txt`

```text
computed_sha256=4b766ec46b69df75136611a47d03fd7268fbfed1b8b18cbb44d9b3296874d143
expected_sha256=4b766ec46b69df75136611a47d03fd7268fbfed1b8b18cbb44d9b3296874d143
match=YES
```

### 3) `catalog_extract_dev_endpoints.json`

Path: `audit/qa/hde-epic026/checks/po-007/catalog_extract_dev_endpoints.json`

```json
{
  "targets": [
    "/dev/reader/conjunction",
    "/dev/sampler/conjunction",
    "/dev/writer/conjunction"
  ],
  "matches": [
    {
      "a7_eligible": false,
      "blueprint_module": "adapter.http_reader",
      "classification": "dev_harness",
      "description": "Conjunction reader preview route (dev-only)",
      "env_gate": "APP_ENV in {dev,test,local}",
      "method": "GET",
      "path": "/dev/reader/conjunction",
      "rails_profile": "dev-harness closed-by-default SAFE rails"
    },
    {
      "a7_eligible": false,
      "blueprint_module": "adapter.http_reader",
      "classification": "dev_harness",
      "description": "Conjunction writer preview route (dev-only)",
      "env_gate": "APP_ENV in {dev,test,local}",
      "method": "GET",
      "path": "/dev/writer/conjunction",
      "rails_profile": "dev-harness closed-by-default SAFE rails"
    },
    {
      "a7_eligible": false,
      "blueprint_module": "adapter.http_reader",
      "classification": "dev_harness",
      "description": "Conjunction sampler preview route (dev-only)",
      "env_gate": "APP_ENV in {dev,test,local}",
      "method": "GET",
      "path": "/dev/sampler/conjunction",
      "rails_profile": "dev-harness closed-by-default SAFE rails"
    }
  ]
}
```

### 4) `pytest_stdout.log`

Path: `audit/qa/hde-epic026/checks/po-007/pytest_stdout.log`

```log
..                                                                       [100%]
2 passed in 0.03s
```

### 5) `pytest_stderr.log`

Path: `audit/qa/hde-epic026/checks/po-007/pytest_stderr.log`

```text
(empty file)
```

### 6) `pytest_rc.txt`

Path: `audit/qa/hde-epic026/checks/po-007/pytest_rc.txt`

```text
0
```

---

## Manifest trail for po-007

Source: `audit/qa/hde-epic026/checks/po-000/qa_step_logs_manifest.json`

- `2026-02-25T17:19:35Z` — `po-007` — `PASS` — `sha256=dfae1ce84644092a01d05d11348641944afa0235f15b06249ab7f69eaf751b69`
- `2026-02-25T17:20:28Z` — `po-007` — `PASS` — `sha256=58688bfedeaf1b2e4955c0a14468c26581aa592c3e0380f526233bb39e55d2d2`

Latest row corresponds to the cleaned and final `primary.log`.

---

## Integrity snapshot (sha256)

- `primary.log`: `58688bfedeaf1b2e4955c0a14468c26581aa592c3e0380f526233bb39e55d2d2`
- `catalog_sha256_check.txt`: `5ece920f6489dbf4c0b3955cd8565681d13228f109f8bf52409c8cae536a6c43`
- `catalog_extract_dev_endpoints.json`: `2497de650ba2f54c66cb50a4e72c9bc311a231ef379c083d69acdca9375587b2`
- `pytest_stdout.log`: `149e983c325e1215d8fe411fd58fb9c0fa38bc5dfa119c4a6a92d44ee61e3e10`
- `pytest_stderr.log`: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- `pytest_rc.txt`: `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`

---

## Conclusion

`po-007` is complete and PASS. Catalog sidecar integrity is proven (`match=YES`), endpoint catalog pytest passes (`rc=0`), and the extracted catalog entries include all three dev conjunction endpoint paths required by the approved plan.
