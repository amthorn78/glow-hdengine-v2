# STEP-02 Report — HDE-EPIC022 / HDE Separation Pass 6 (qapass6)

- Evidence bundle: [audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc)
- Step: STEP-02 (internal_version_capture); Run ID: 20260103T015609Z; Status: PASS (exit_code=0)
- Rails captured: SAFE_MODE=0, ALLOW_NETWORK=1, APP_ENV=prod, LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0
- Target URL: ${HDE_PROD_BASE_URL}/internal/version; Auth header was not set.
- Upstream evidence root pointer (from meta/evidence_root.txt): audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc

## Step Results
- GET/HEAD returned 200; JSON validated (body_json_valid=1)
- Response identity: engine_tag=hdengine@prod, build_commit=9479d28, release_id=077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5
- Stdout/stderr empty; predicates satisfied.

## Repository Changes
- New report file: this document. No code or artifact modifications beyond recorded evidence.

## Evidence files (indexed)
- [meta/evidence_root.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/meta/evidence_root.txt)
- [results/step-02.result.env](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/results/step-02.result.env)
- [step_logs/step-02.log](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/step_logs/step-02.log)
- [stdout/step-02.stdout.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/stdout/step-02.stdout.txt)
- [stderr/step-02.stderr.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/stderr/step-02.stderr.txt)
- [artifacts/internal_version_capture/http_get.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/artifacts/internal_version_capture/http_get.txt)
- [artifacts/internal_version_capture/http_head.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/artifacts/internal_version_capture/http_head.txt)
- [artifacts/internal_version_capture/headers_get.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/artifacts/internal_version_capture/headers_get.txt)
- [artifacts/internal_version_capture/headers_head.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/artifacts/internal_version_capture/headers_head.txt)
- [artifacts/internal_version_capture/body_json_valid.txt](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/artifacts/internal_version_capture/body_json_valid.txt)
- [artifacts/internal_version_capture/body_get.json](audit/qa/hde-epic022/hde_epic022_step02_qapass6/run_20260103_042853_utc/artifacts/internal_version_capture/body_get.json)

## Filedump

### meta/evidence_root.txt
```text
audit/qa/hde-epic022/hde_epic022_step01_qapass6/run_20260103_015545_utc
```

### results/step-02.result.env
```dotenv
STEP_ID=STEP-02
STATUS=PASS
EXIT_CODE=0
HTTP_GET=200
HTTP_HEAD=200
BODY_JSON_VALID=1
```

### step_logs/step-02.log
```log
{"epic_id": "HDE-EPIC022", "run_id": "20260103T015609Z", "check_id": "STEP-02", "step_name": "internal_version_capture", "command": "set -euo pipefail\n\nif [ -z \"${HDE_PROD_BASE_URL:-}\" ]; then\n  echo \"[STEP-02] Missing required input: HDE_PROD_BASE_URL\" >&2\n  exit 20\nfi\n\nURL=\"${HDE_PROD_BASE_URL}/internal/version\"\nAUTH_HEADER=\"${HDE_INTERNAL_VERSION_AUTH_HEADER:-}\"\n\nOUT_DIR=\"${EVIDENCE_ROOT}/artifacts/internal_version_capture\"\nmkdir -p \"${OUT_DIR}\"\n\nif [ -n \"${AUTH_HEADER}\" ]; then\n  curl -sS -D \"${OUT_DIR}/headers_get.txt\" -o \"${OUT_DIR}/body_get.json\" -w \"%{http_code}\\n\" -H \"${AUTH_HEADER}\" \"${URL}\" > \"${OUT_DIR}/http_get.txt\"\nelse\n  curl -sS -D \"${OUT_DIR}/headers_get.txt\" -o \"${OUT_DIR}/body_get.json\" -w \"%{http_code}\\n\" \"${URL}\" > \"${OUT_DIR}/http_get.txt\"\nfi\n\nif [ -n \"${AUTH_HEADER}\" ]; then\n  curl -sS -I -D \"${OUT_DIR}/headers_head.txt\" -o /dev/null -w \"%{http_code}\\n\" -H \"${AUTH_HEADER}\" \"${URL}\" > \"${OUT_DIR}/http_head.txt\"\nelse\n  curl -sS -I -D \"${OUT_DIR}/headers_head.txt\" -o /dev/null -w \"%{http_code}\\n\" \"${URL}\" > \"${OUT_DIR}/http_head.txt\"\nfi\n\npython - <<PY\nimport json, sys\np=\"${OUT_DIR}/body_get.json\"\ntry:\n    v=json.load(open(p,\"r\",encoding=\"utf-8\"))\n    ok = isinstance(v, dict)\nexcept Exception:\n    ok = False\nopen(\"${OUT_DIR}/body_json_valid.txt\",\"w\",encoding=\"utf-8\").write(\"1\\n\" if ok else \"0\\n\")\nPY", "captured_env": {"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "prod", "LC_ALL": "C", "LANG": "C", "TZ": "UTC", "PYTHONHASHSEED": "0"}, "rails": "SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0", "pf_refs": ["PF10 — HDE-Build Notes §2.12", "PF10 — HDE-Build Notes §2.16", "PF10 — HDE-Build Notes §2.13", "PF10 — HDE-Build Notes §2.5"], "intended_tokens": [], "claimed_tokens": [], "status": "PASS", "exit_code": 0, "started_at_utc": "2026-01-03T04:29:23Z", "ended_at_utc": "2026-01-03T04:29:23Z"}

---- STDOUT ----


---- STDERR ----

```

### stdout/step-02.stdout.txt
```text
<empty>
```

### stderr/step-02.stderr.txt
```text
<empty>
```

### artifacts/internal_version_capture/http_get.txt
```text
200
```

### artifacts/internal_version_capture/http_head.txt
```text
200
```

### artifacts/internal_version_capture/headers_get.txt
```text
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Sat, 03 Jan 2026 04:29:23 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: gjbIB1hWRreUpQS9YqdHTg
content-length: 347
```

### artifacts/internal_version_capture/headers_head.txt
```text
HTTP/2 200 
cache-control: no-store
content-type: application/json; charset=utf-8
date: Sat, 03 Jan 2026 04:29:23 GMT
server: railway-edge
x-railway-edge: railway/europe-west4-drams3a
x-railway-request-id: EKloJj2jRvOD-NhGjUJq2g
content-length: 347
```

### artifacts/internal_version_capture/body_json_valid.txt
```text
1
```

### artifacts/internal_version_capture/body_get.json
```json
{"engine_tag":"hdengine@prod","build_commit":"9479d28","invocation_tag":"INV-f2ac55d77ce9aacc","invocation_sha256":"3f119e727a2a1f8a5332fe8f159321ea5274988e6a05633103fe0a5ae42c6e69","emitter_sha256":"c828effe645deae150593adbc90589f67141ab20fab1e719171cd8effad9bc19","release_id":"077bcb55b30c5384be754567c388c210ca3004f2fd9f9187d6861e2faffe58f5"}
```
