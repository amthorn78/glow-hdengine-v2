# Combined QA Files for run_20251226t181426z_e44b4cc (Step D0.3)

## File: artifacts/math/release_id_recompute.log

```log
release_id_recompute
produced_at_utc=2025-12-26T23:55:21Z
manifest_sha256=47f42d29fb4e1196691f3dae28cfc0fa04ce5504e2511cd27eca9e325fe88921
release_id_txt=6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925
match=false
problems_count=2
problem=freeze_pack_manifest_not_equal
problem=manifest_missing_files_array
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/release_id/freeze_pack_manifest.json

```json
{"release_id":"6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925","entries":[{"path":"adapter/http_reader.py","sha256":"93431e3a80c3abfd8a7cd8f10dee39b24bf6a545f101a949837b169302a6bf93","size":4554},{"path":"engine/presenter/emitter.py","sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","size":378},{"path":"engine/serializer/canon.py","sha256":"43fb0cb5cae06242d66ced440d45f1584cbdabc08c161bdc1b9eeafea18e4adf","size":538},{"path":"migrations/005_identity.sql","sha256":"f0db0d51a8b5e0490768cf4644d50d63fd3ceab1bba000422ad0d0ee7d16485b","size":3416}]}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/release_id/release_id.txt

```plaintext
6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/release_id/release_id_recompute.log

```log
release_id_recompute
produced_at_utc=2025-12-26T23:55:21Z
manifest_sha256=47f42d29fb4e1196691f3dae28cfc0fa04ce5504e2511cd27eca9e325fe88921
release_id_txt=6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925
match=false
problems_count=2
problem=freeze_pack_manifest_not_equal
problem=manifest_missing_files_array
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log

```log
{"check_id": "D0.3", "exit_code": 10, "pf_refs": ["PF12 — HDE-Schemas and Artifacts, §6.4"], "produced_at_utc": "2025-12-26T23:55:43Z", "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "status": "FAIL_BEHAVIOR", "tokens": ["RELEASE_ID_RECOMPUTE_OK", "RELEASE_ID_FROM_MANIFEST_OK"]}

=== release_id_recompute.log ===
release_id_recompute
produced_at_utc=2025-12-26T23:55:21Z
manifest_sha256=47f42d29fb4e1196691f3dae28cfc0fa04ce5504e2511cd27eca9e325fe88921
release_id_txt=6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925
match=false
problems_count=2
problem=freeze_pack_manifest_not_equal
problem=manifest_missing_files_array
```

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
    }
  ]
}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/d0_3_verdict.txt

```plaintext
FAIL_BEHAVIOR
```

---

## Summary

**Status:** FAIL_BEHAVIOR (exit code 10)

**Problems detected:**
- `freeze_pack_manifest_not_equal` - Manifest SHA256 mismatch
- `manifest_missing_files_array` - Manifest structure issue

**Key values:**
- manifest_sha256: `47f42d29fb4e1196691f3dae28cfc0fa04ce5504e2511cd27eca9e325fe88921`
- release_id_txt: `6d8efb271281916e7c775f6b45efafba8c78d55604c40eaa0d89cc40a7eea925`
- match: `false`

**Tokens:** RELEASE_ID_RECOMPUTE_OK, RELEASE_ID_FROM_MANIFEST_OK
