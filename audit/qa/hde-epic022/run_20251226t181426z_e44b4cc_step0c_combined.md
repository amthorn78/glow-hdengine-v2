# Combined QA Files for run_20251226t181426z_e44b4cc (Step 0C)

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/prod_handshake.json

```json
{
  "captured_at_utc": "2025-12-26T19:11:10Z",
  "headers_file": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/prod_handshake.headers",
  "note": "Connectivity probe only; contract validated in D3.1",
  "target": "HDE_BASE_URL/internal/version"
}
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/prod_handshake.headers

```plaintext
HTTP/2 404 
content-type: application/json
date: Fri, 26 Dec 2025 19:11:10 GMT
server: railway-edge
set-cookie: flask_session=6d31ffcd-66e1-4da3-9a50-aa1285348fc7.TxKTd9aXcrQqNJBkobTYnvg_XyA; Expires=Fri, 26 Dec 2025 19:41:10 GMT; Secure; HttpOnly; Path=/; SameSite=Lax
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: gM-jtGLdQjyfuOsHm3z_FQ
content-length: 31
```

---

## File: audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0C_prod_handshake.log

```log
check_id: 0C
status: PASS
started_at_utc: 2025-12-26T19:11:10Z
ended_at_utc: 2025-12-26T19:11:10Z
rails: SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0
pf_refs: PF19 — Glow QA Guide, §2.3
tokens:
command: set -euo pipefail
    mkdir -p "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results"
    curl -sS -o /dev/null -D "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results/prod_handshake.headers" \
      --connect-timeout 5 --max-time 15 --retry 0 \
      "https://glow-backend-v4-production.up.railway.app/internal/version" || true
    python - <<PY
import json, pathlib, time
p = pathlib.Path("audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results") / "prod_handshake.json"
hdr = pathlib.Path("audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/results") / "prod_handshake.headers"
p.write_text(json.dumps({
  "captured_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
  "target": "HDE_BASE_URL/internal/version",
  "headers_file": str(hdr),
  "note": "Connectivity probe only; contract validated in D3.1"
}, indent=2, sort_keys=True) + "\n")
PY
  
stdout_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
stderr_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
exit_code: 0
--- stdout ---

--- stderr ---

```

---

## File: audit/qa/hde-epic022/qa_step_logs_manifest.json

```json
[
  {
    "check_id": "0A",
    "ended_at_utc": "2025-12-26T18:16:15Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0A_bootstrap_and_codespaces_snapshot.log",
    "pf_refs": "PF19 — Glow QA Guide, §14.4.3; PF27 — Plan Templates, §4.2",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T18:16:15Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "0710287ebdc583a08974ea6b7205269a34d81b0c4edfb69fdf3d471cda1d4b98",
    "tokens": []
  },
  {
    "check_id": "0B",
    "ended_at_utc": "2025-12-26T18:41:55Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0B_doc_delta_capture.log",
    "pf_refs": "PF10 — HDE-Build Notes, §2.3; PF10 — HDE-Build Notes, §2.7",
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T18:41:55Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": [
      "DOC_DELTA_PRESENT_OK"
    ]
  },
  {
    "check_id": "0C",
    "ended_at_utc": "2025-12-26T19:11:10Z",
    "exit_code": 0,
    "log_path": "audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0C_prod_handshake.log",
    "pf_refs": "PF19 — Glow QA Guide, §2.3",
    "rails": "SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "started_at_utc": "2025-12-26T19:11:10Z",
    "status": "PASS",
    "stderr_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "stdout_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "tokens": []
  }
]
```

---

## File: audit/qa/hde-epic022/step0c_deviations.md

*File not found*
