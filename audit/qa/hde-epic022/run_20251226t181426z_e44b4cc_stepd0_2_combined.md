# Combined QA Files for run_20251226t181426z_e44b4cc (Step D0.2)

## File: audit/gates/determinism/env_pins.log

```log
{"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"produced_at_utc":"2025-12-26T23:25:01Z","status":"success","suites":["liveqa:epic022:d0.2"]}
```

---

## File: audit/gates/determinism/env_pins.log.path_proof.txt

```plaintext
path=audit/gates/determinism/env_pins.log
size_bytes=174
sha256=37b488fd841f5b9c68e006bb93144e0d3c968b345794628acd2d874131296d06
produced_at_utc=2025-12-26T23:25:20Z
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/env_pins/env_pins.log

```log
{"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"produced_at_utc":"2025-12-26T23:25:01Z","status":"success","suites":["liveqa:epic022:d0.2"]}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/snapshots/env_pins/env_pins.log.path_proof.txt

```plaintext
path=audit/gates/determinism/env_pins.log
size_bytes=174
sha256=37b488fd841f5b9c68e006bb93144e0d3c968b345794628acd2d874131296d06
produced_at_utc=2025-12-26T23:25:20Z
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.2_determinism_env_pins_emit.log

```log
{"check_id": "D0.2", "command": "D0.2 inline env_pins.log + path proof + snapshot copy (no repo scripts)", "exit_code": 0, "pf_refs": ["PF04 — HDE-Governance, §2.0.1", "PF12 — HDE-Schemas and Artifacts, §8.6.3", "PF20 — HDE-Phased Epics, §2.7.5.A4"], "produced_at_utc": "2025-12-26T23:25:39Z", "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "status": "PASS", "tokens": ["DETERMINISM_ENV_PINS_OK", "ENV_RAILS_POLICY_OK"]}

=== env_pins.log ===
{"env":{"ALLOW_NETWORK":"0","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"produced_at_utc":"2025-12-26T23:25:01Z","status":"success","suites":["liveqa:epic022:d0.2"]}


=== env_pins.log.path_proof.txt ===
path=audit/gates/determinism/env_pins.log
size_bytes=174
sha256=37b488fd841f5b9c68e006bb93144e0d3c968b345794628acd2d874131296d06
produced_at_utc=2025-12-26T23:25:20Z
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
    }
  ]
}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/d0_2_verdict.txt

```plaintext
PASS
```

---

## File: audit/qa/hde-epic022/stepd0_2_deviations.md

*File not found*
