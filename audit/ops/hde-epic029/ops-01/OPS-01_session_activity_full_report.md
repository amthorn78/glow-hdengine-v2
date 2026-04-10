# OPS-01 Session Activity Full Report (English)

## Scope
This report consolidates the full session activity for OPS-01 (HDE-EPIC029 / Conjunction Pass 5), including:

- All actions taken during the run
- Observed run outcomes
- Verbatim contents of all produced OPS-01 evidence artifacts (D1-D8)

## Execution Context
- Repository: amthorn78/glow-hdengine-v2
- Branch: main
- Working root: /workspaces/glow-hdengine-v2
- Python environment: venv (Python 3.11.14)
- Determinism rails applied for run evidence: APP_ENV=dev, SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC, PORT=8000
- Final verification timestamp (UTC): 2026-04-10T11:00:44Z

## Chronological Action Log
1. Configured Python environment for the workspace and confirmed venv usage.
2. Created governed OPS-01 output directory under audit/ops/hde-epic029/ops-01.
3. Initialized required log artifacts:
   - stdout.log
   - stderr.log
   - exit_codes.txt
4. Wrote command-plan artifact commands.txt.
5. Started scripts/dev_start_reader.sh under closed rails and redirected output to OPS logs.
6. Ran scripts/qa/dev_sampler_healthcheck.py against canonical Codespaces DEV_SAMPLER_URL:
   - http://127.0.0.1:8000/internal/dev/sampler
7. Recorded Codespaces healthcheck exit code in exit_codes.txt.
8. Probed local-dev environment for a published local-dev sampler binding:
   - LOCAL_DEV_SAMPLER_URL was empty/not set.
   - DEV_SAMPLER_URL was set to canonical Codespaces value.
9. Recorded local-dev published PF07 DEV_SAMPLER_URL and not-yet-closed disposition (step creation + AI data indexing failure), recorded in:
   - local_dev_sampler_url.md
   - binding_disposition.md
   - exit_codes.txt (deferred marker)
10. Wrote Codespaces binding snapshot artifact with rails details.
11. Generated checksum ledger created_files_sha256.txt for D1-D7.
12. Killed persistent reader terminal after evidence capture.
13. Performed post-run verification of checksum file newline integrity.

## Outcome Summary
- Codespaces binding validation: NOT YET CLOSED (gating_discrepancy persisted: APP_ENV=prod returned 200)
- Local-dev binding validation: DEFERRED (not yet closed; published PF07 DEV_SAMPLER_URL was available, but step creation and AI data indexing failure kept disposition open)
- OPS-01 deliverables D1-D8: PRESENT

## Post-Run Verification Output
Observed verification output:

```text
utc_now=2026-04-10T11:00:44Z
contains_literal_backslash_n= False
newline_count= 7
line_count= 7
```

Interpretation:
- created_files_sha256.txt contains real newline-separated records.
- The file has 7 lines, matching D1-D7 coverage.

---

## Consolidated Evidence (Verbatim)

### D1 — commands.txt
Path: audit/ops/hde-epic029/ops-01/commands.txt

```text
APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 scripts/dev_start_reader.sh
DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC scripts/qa/dev_sampler_healthcheck.py
LOCAL_DEV flow: use published PF07 DEV_SAMPLER_URL and record OPS outcome when step creation / AI data indexing failure prevents closure.
```

### D2 — stdout.log
Path: audit/ops/hde-epic029/ops-01/stdout.log

```text
[dev-start] APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0
[dev-start] LC_ALL=C LANG=C TZ=UTC
[dev-start] Binding port 8000 via python -m adapter.http_reader (host=0.0.0.0)
 * Serving Flask app 'http_reader'
 * Debug mode: off
[2026-04-10T10:53:46.696225+00:00] dev_sampler_url=http://127.0.0.1:8000/internal/dev/sampler
[2026-04-10T10:53:46.696410+00:00] rails_snapshot={'APP_ENV': 'dev', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0', 'LC_ALL': 'C', 'LANG': 'C', 'TZ': 'UTC'}
[2026-04-10T10:53:46.696547+00:00] starting_reader mode=dev host=127.0.0.1 port=8000 rails={'APP_ENV': 'dev', 'PORT': '8000', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0', 'LC_ALL': 'C', 'LANG': 'C', 'TZ': 'UTC'}
[2026-04-10T10:53:46.712643+00:00] sampler_response mode=dev status=200 http_version=HTTP/1.1 body={"body": {"candidate_ids": ["dev-cand-1", "dev-cand-2"], "meta": {"seed": "healthcheck"}, "viewer_id": "dev-healthcheck-viewer"}, "headers": {"Cache-Control": "no-store", "Connection": "close", "Content-Length": "113", "Content-Type": "application/json; charset=utf-8", "Date": "Fri, 10 Apr 2026 10:53:46 GMT", "Server": "Werkzeug/3.1.6 Python/3.11.14"}}
[2026-04-10T10:53:46.714199+00:00] starting_reader mode=prod host=127.0.0.1 port=8000 rails={'APP_ENV': 'prod', 'PORT': '8000', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0', 'LC_ALL': 'C', 'LANG': 'C', 'TZ': 'UTC'}
[2026-04-10T10:53:46.721879+00:00] sampler_response mode=prod status=200 http_version=HTTP/1.1 body={"body": {"candidate_ids": ["dev-cand-1", "dev-cand-2"], "meta": {"seed": "healthcheck"}, "viewer_id": "dev-healthcheck-viewer"}, "headers": {"Cache-Control": "no-store", "Connection": "close", "Content-Length": "113", "Content-Type": "application/json; charset=utf-8", "Date": "Fri, 10 Apr 2026 10:53:46 GMT", "Server": "Werkzeug/3.1.6 Python/3.11.14"}}
[2026-04-10T10:53:46.725210+00:00] gating_diagnostic expected=403? actual_status=200 body_keys=['candidate_ids', 'meta', 'viewer_id']
[2026-04-10T10:53:46.725361+00:00] gating_discrepancy observed: APP_ENV=prod did not return 403
```

### D3 — stderr.log
Path: audit/ops/hde-epic029/ops-01/stderr.log

```text
[31m[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.[0m
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://10.0.1.193:8000
[33mPress CTRL+C to quit[0m
127.0.0.1 - - [10/Apr/2026 10:53:46] "POST /internal/dev/sampler HTTP/1.1" 200 -
127.0.0.1 - - [10/Apr/2026 10:53:46] "POST /internal/dev/sampler HTTP/1.1" 200 -
```

### D4 — exit_codes.txt
Path: audit/ops/hde-epic029/ops-01/exit_codes.txt

```text
codespaces_healthcheck=0
local_dev_healthcheck=NOT_CLOSED_STEP_CREATION_AND_AI_DATA_INDEXING_FAILURE
```

### D5 — codespaces_dev_sampler_url.md
Path: audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md

```text
environment: codespaces
dev_sampler_url: http://127.0.0.1:8000/internal/dev/sampler
app_env: dev
safe_mode: 1
allow_network: 0
lc_all: C
lang: C
tz: UTC
notes: remediation rerun captured gating_discrepancy observed (APP_ENV=prod did not return 403); Codespaces remains not yet closed pending clean validation.
```

### D6 — local_dev_sampler_url.md
Path: audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md

```text
environment: local_dev
dev_sampler_url: http://127.0.0.1:8000/internal/dev/sampler
status: not yet closed
reason: PF07 publishes DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler, but OPS outcome remained not yet closed due step creation and AI data indexing failure.
```

### D7 — binding_disposition.md
Path: audit/ops/hde-epic029/ops-01/binding_disposition.md

```text
codespaces: not yet closed - remediation rerun recorded gating_discrepancy observed (APP_ENV=prod did not return 403) in stdout.log.
local_dev: not yet closed - PF07 published DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler, but OPS recorded step creation and AI data indexing failure.
```

### D8 — created_files_sha256.txt
Path: audit/ops/hde-epic029/ops-01/created_files_sha256.txt

```text
8921960ab9153dd28663b3a5883fe0d49bf99b69fe7d9c16ed3d254462e75d1c  audit/ops/hde-epic029/ops-01/commands.txt
9a8bf85603389752a2a4991265e27bff1161bf6608074eb98c27886d1b26872f  audit/ops/hde-epic029/ops-01/stdout.log
99dda4af95f223a831e1e3d8427a4b0ec46c9a3cf990322dc981daca04f4bb7d  audit/ops/hde-epic029/ops-01/stderr.log
28656388378da089abd5ad6db74ebedd40fe46d9cb534f39bf5da8a1e6803811  audit/ops/hde-epic029/ops-01/exit_codes.txt
b2dd8457e7027ceb414c66b463f7b97718528b9bbe23bb20fa03c9b542bb7911  audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md
aaf8b0fd222b3afbfeeeb5526687ca29efcab9614758df7fc8318ae6d914ee66  audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md
30990460fd2a0a9668b49ce5f4dd47cffb4a2165265153088c110fb5129e7adc  audit/ops/hde-epic029/ops-01/binding_disposition.md
```

## Final Session Status
OPS-01 evidence generation is complete for this session with explicit, non-overstated closure status:

- codespaces: not yet closed
- local_dev: not yet closed
