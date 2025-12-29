# Combined Release ID and Manifest Check Report

Run ID: `run_20251226t181426z_e44b4cc`  
Generated: 2025-12-27  
Check: D0.3 - Release ID Recompute and Manifest Validation

---

## File: artifacts/math/release_id_recompute.log

```log
release_id_recompute
produced_at_utc=2025-12-27T22:15:28Z
manifest_path=catalog/manifest.json
freeze_pack_manifest_path=artifacts/math/freeze_pack_manifest.json
release_id_path=artifacts/math/release_id.txt
manifest_sha256=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id_txt=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
match=true
problems_count=0
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/release_id/release_id.txt

```plaintext
077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/release_id/release_id_recompute.log

```log
release_id_recompute
produced_at_utc=2025-12-27T22:15:28Z
manifest_path=catalog/manifest.json
freeze_pack_manifest_path=artifacts/math/freeze_pack_manifest.json
release_id_path=artifacts/math/release_id.txt
manifest_sha256=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id_txt=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
match=true
problems_count=0
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/release_id/freeze_pack_manifest.json

```json
{"built_at_utc":"2025-12-26T00:00:00Z","files":[{"path":"adapter/http_reader.py","sha256":"b1aafa6819389274b38bd8575bef1ca1ae09a46fd5bfa236fd0d21adf0ce39e6","size":29862},{"path":"catalog/magic10.json","sha256":"ef4ec8dd591294f15ca870f038678116b7932782023301fd8885b1a870b07e64","size":124},{"path":"catalog/magic10_caps.json","sha256":"ecd1f536717fc8ff32cd30cde7a2e6164a58effdd1c63ba67429985cba61b05b","size":900},{"path":"catalog/magic10_seeds.json","sha256":"446ca6dcbe3d25286e40f9acbac6f492d36eb7416280f0c29a3ff43cacac5b45","size":357},{"path":"engine/presenter/emitter.py","sha256":"5a47195420a0d58a74cd51b723c9d1ac8fcbc3077de7c08755d2689594376def","size":1008},{"path":"engine/serializer/canon.py","sha256":"f56cdacfb90b7d9cb467d7e6005ad62e62e83d4b04c022c53e9f9b190e7777c3","size":485},{"path":"math/thresholds.json","sha256":"5a9805ac3da14c1d7a9e693a52c7faa5b1e5b9b5fc7a62972e1a8a45561f25a4","size":82},{"path":"migrations/005_identity.sql","sha256":"10ae2aefba0cb48855245ac307f7cc47c1dac3bfb961bfd13fd091ef08b13128","size":3733}],"root":"catalog/","version":"1.0.0"}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log

```log
{"check_id": "D0.3", "command": "D0.3 inline release_id recompute (sha256(canonical manifest bytes)) + freeze_pack_manifest byte-identity + manifest schema closure check", "exit_code": 0, "pf_refs": ["PF10 — HDE-Build Notes, §2.23", "PF10 — HDE-Build Notes, §2.8", "PF12 — HDE-Schemas and Artifacts, §6.4"], "produced_at_utc": "2025-12-27T22:16:34Z", "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC", "status": "PASS", "tokens": ["RELEASE_ID_RECOMPUTE_OK", "RELEASE_ID_FROM_MANIFEST_OK"]}

=== artifacts/math/release_id_recompute.log ===
release_id_recompute
produced_at_utc=2025-12-27T22:15:28Z
manifest_path=catalog/manifest.json
freeze_pack_manifest_path=artifacts/math/freeze_pack_manifest.json
release_id_path=artifacts/math/release_id.txt
manifest_sha256=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
release_id_txt=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
match=true
problems_count=0
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
    },
    {
      "check_id": "D0.3",
      "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log",
      "recorded_at_utc": "2025-12-27T22:16:48Z",
      "status": "PASS"
    }
  ]
}
```

---

## File: audit/qa/hde-epic022/stepd0_3_deviations.md

**Status**: File not found (does not exist in repository)

---

## Summary

**Status**: PASS (current run)  
**Tokens claimed**: 
- `RELEASE_ID_RECOMPUTE_OK`
- `RELEASE_ID_FROM_MANIFEST_OK`

**Release ID**: `077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5`

**Validation results**:
- ✓ Manifest SHA256 matches release_id.txt
- ✓ Byte-identity confirmed (match=true)
- ✓ Zero problems detected (problems_count=0)
- ✓ Freeze-pack manifest contains 8 files
- ✓ Exit code: 0

**Historical runs** (from qa_step_logs_manifest.json):
1. 2025-12-26T23:55:51Z - FAIL_BEHAVIOR
2. 2025-12-27T22:16:48Z - PASS (current)

**PF References**:
- PF10 § 2.23 (HDE-Build Notes)
- PF10 § 2.8 (HDE-Build Notes)
- PF12 § 6.4 (Schemas and Artifacts)

**Determinism rails**: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC`
