# Combined D2.1 Showcompat Artifacts and Tests Report

Run ID: `run_20251226t181426z_e44b4cc`  
Generated: 2025-12-27  
Check: D2.1 - Showcompat artifacts + canonical bytes + usage/errors

---

## File: artifacts/cli/showcompat/stdout.json

```json
{"a":{"birth":{"birthdate":"1990-01-10","birthtime":"14:05","location":"Chicago, US"},"person_uid":"cli-2fef6bdbe4fd0a00350f05da3af3303c"},"b":{"birth":{"birthdate":"1992-03-04","birthtime":"08:15","location":"Berlin, DE"},"person_uid":"cli-cbc24d9435431d2196c9ff1d1b865049"},"compat":{"categories":[{"band":"Cool","id":"heat","personal_key":"heat_cool_personal_v1","score":23,"shared_key":"heat_cool_shared_v1"},{"band":"Warm","id":"harmony","personal_key":"harmony_warm_personal_v1","score":71,"shared_key":"harmony_warm_shared_v1"},{"band":"Cool","id":"communication","personal_key":"communication_cool_personal_v1","score":11,"shared_key":"communication_cool_shared_v1"},{"band":"Cool","id":"alignment","personal_key":"alignment_cool_personal_v1","score":5,"shared_key":"alignment_cool_shared_v1"},{"band":"Open","id":"comfort","personal_key":"comfort_open_personal_v1","score":35,"shared_key":"comfort_open_shared_v1"},{"band":"Cool","id":"consistency","personal_key":"consistency_cool_personal_v1","score":20,"shared_key":"consistency_cool_personal_v1"},{"band":"Cool","id":"expansion","personal_key":"expansion_cool_personal_v1","score":24,"shared_key":"expansion_cool_shared_v1"},{"band":"Open","id":"creativity","personal_key":"creativity_open_personal_v1","score":38,"shared_key":"creativity_open_shared_v1"},{"band":"Open","id":"drive","personal_key":"drive_open_personal_v1","score":26,"shared_key":"drive_open_shared_v1"},{"band":"Cool","id":"balance","personal_key":"balance_cool_personal_v1","score":7,"shared_key":"balance_cool_shared_v1"}],"meta":{"engine_tag":"hdengine-dev","invocation_tag":"INV-EPIC022-D2","release_id":"0000000000000000000000000000000000000000000000000000000000000000"}},"viewer_prefs":{"top_category":"heat","weights":{"alignment":50,"balance":50,"comfort":50,"communication":50,"consistency":50,"creativity":50,"drive":50,"expansion":50,"harmony":50,"heat":50}}}
```

---

## File: artifacts/cli/showcompat/args.json

```json
{"argv":["/workspaces/glow-hdengine-v2/.venv/bin/python","scripts/hdctl.py","showcompat"],"artifacts":{"stdout":"artifacts/cli/showcompat/stdout.json","stdout_sha256":"artifacts/cli/showcompat/stdout.json.sha256"},"env":{"ALLOW_NETWORK":"0","ENGINE_TAG":"hdengine-dev","LANG":"C","LC_ALL":"C","PRODUCT_INVOCATION_TAG":"INV-EPIC022-D2","RELEASE_ID":"0000000000000000000000000000000000000000000000000000000000000000","SAFE_MODE":"1","TZ":"UTC"},"generator":"tools/cli/generate_showcompat_artifacts.py","input":{"source":"stdin","stdin_payload":{"left":{"birthdate":"1990-01-10","birthtime":"14:05","location":"Chicago, US"},"right":{"birthdate":"1992-03-04","birthtime":"08:15","location":"Berlin, DE"}},"stdin_sha256":"66d5d4e0cef821ba6fc5eb5c429a190a7241f594fa792923226e347d50813ce6","trailing_lf":true}}
```

---

## File: artifacts/cli/showcompat/stdout.json.sha256

```plaintext
affb9ce0b9cb1d69932287ac7913ac243562005b10e7ba8cade9b0d27d26232f  artifacts/cli/showcompat/stdout.json
```

---

## File: artifacts/cli/showcompat/stdout.sha256

```plaintext
affb9ce0b9cb1d69932287ac7913ac243562005b10e7ba8cade9b0d27d26232f  artifacts/cli/showcompat/stdout.json
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/D2.1_generate_showcompat_artifacts.log

```log

```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/D2.1_pytest_cli_canonical_bytes.log

```log
.                                                                        [100%]
1 passed in 0.12s
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/D2.1_pytest_cli_usage_and_errors.log

```log
.....                                                                    [100%]
5 passed in 11.29s
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D2.1_showcompat_artifacts_and_tests.log

```log
{"check_id": "D2.1", "command": "D2.1 generate_showcompat_artifacts + sha sidecars + pytest canonical bytes + pytest stream discipline", "exit_code": 0, "pf_refs": ["PF12 — HDE-Schemas and Artifacts, §8.6.3", "PF10 — HDE-Build Notes, §2.5"], "produced_at_utc": "2025-12-27T22:49:25Z", "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "status": "PASS", "tokens": ["CLI_STDOUT_LF_OK"]}

=== generator log ===


=== pytest: test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical ===
.                                                                        [100%]
1 passed in 0.12s


=== pytest: tests/cli/test_cli_usage_and_errors.py ===
.....                                                                    [100%]
5 passed in 11.29s
```

---

## Files: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/showcompat/*

- args.json
- args.json.path_proof.txt
- stdout.json
- stdout.json.path_proof.txt
- stdout.json.sha256
- stdout.json.sha256.path_proof.txt
- stdout.sha256

---

## File: audit/qa/hde-epic022/qa_step_logs_manifest.json

```json
{
  "steps": [
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T22:51:25Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T23:01:49Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log",
      "recorded_at_utc": "2025-12-26T23:07:36Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.2",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.2_determinism_env_pins_emit.log",
      "recorded_at_utc": "2025-12-26T23:25:46Z",
      "status": "PASS"
    },
    {
      "check_id": "D0.3",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log",
      "recorded_at_utc": "2025-12-26T23:55:51Z",
      "status": "FAIL_BEHAVIOR"
    },
    {
      "check_id": "D0.3",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log",
      "recorded_at_utc": "2025-12-27T22:16:48Z",
      "status": "PASS"
    },
    {
      "check_id": "D2.1",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D2.1_showcompat_artifacts_and_tests.log",
      "recorded_at_utc": "2025-12-27T22:49:41Z",
      "status": "PASS"
    }
  ]
}
```

---

## Summary

**Status**: PASS  
**Tokens claimed**: 
- `CLI_STDOUT_LF_OK`

**Artifacts validated**:
- stdout.json SHA256: `affb9ce0...` matches in both sidecars
- Canonical bytes test: 1 passed
- Usage and errors tests: 5 passed

**Determinism rails**: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`
