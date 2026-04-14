# W-004 Full Session Log and All Evidence Outputs

## Task Identity
- Work item: W-004
- Epic: HDE-EPIC029 / Conjunction Pass 5
- Mode: OPS closure remediation rerun (evidence-first)
- Repository root: /workspaces/glow-hdengine-v2
- Evidence source family: audit/ops/hde-epic029/ops-01/
- Session reference timestamp: 2026-04-13T20:20:15Z

## Session Log (Chronological)
1. Reinitialized OPS-01 evidence ledgers for W-004.
2. Captured execution context probe indicating this run venue is Codespaces.
3. Started dev Reader helper under closed rails with APP_ENV=dev and pinned locale/timezone.
4. Ran sampler healthcheck against DEV_SAMPLER_URL for Codespaces.
5. Captured expected behavior checks:
   - dev path success (HTTP 200)
   - prod path refusal (HTTP 403)
6. Applied the EPIC029 W-004 closure rule for local_dev as explicit binding-equivalence to the canonical Codespaces loopback binding (not a separate runtime-host proof).
7. Recorded per-environment URL/disposition files and final binding disposition.
8. Regenerated OPS-01 checksum ledger over finalized evidence outputs.

## Evidence Output: commands.txt (Verbatim)

```text
# OPS-01 remediation rerun (2026-04-13T20:20:15Z)
# context_probe: hostname=codespaces-62e220 CODESPACES=true
APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC PORT=8000 scripts/dev_start_reader.sh
DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC scripts/qa/dev_sampler_healthcheck.py # codespaces
# local_dev_closure: satisfied by binding-equivalence to the same canonical loopback DEV_SAMPLER_URL validated in Codespaces for EPIC029 (not an independent runtime-host proof).
```

## Evidence Output: stdout.log (Verbatim)

```text
[dev-start] APP_ENV=dev SAFE_MODE=1 ALLOW_NETWORK=0
[dev-start] LC_ALL=C LANG=C TZ=UTC
[dev-start] Binding port 8000 via python -m adapter.http_reader (host=0.0.0.0)
 * Serving Flask app 'http_reader'
 * Debug mode: off
=== CODESPACES_HEALTHCHECK_START ===
[2026-04-13T20:20:19.239514+00:00] dev_sampler_url=http://127.0.0.1:8000/internal/dev/sampler
[2026-04-13T20:20:19.239641+00:00] rails_snapshot={'APP_ENV': 'dev', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0', 'LC_ALL': 'C', 'LANG': 'C', 'TZ': 'UTC'}
[2026-04-13T20:20:19.239757+00:00] starting_reader mode=dev host=127.0.0.1 port=8000 rails={'APP_ENV': 'dev', 'PORT': '8000', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0', 'LC_ALL': 'C', 'LANG': 'C', 'TZ': 'UTC'}
[2026-04-13T20:20:19.503217+00:00] sampler_response mode=dev status=200 http_version=HTTP/1.1 body={"body": {"candidate_ids": ["dev-cand-1", "dev-cand-2"], "meta": {"seed": "healthcheck"}, "viewer_id": "dev-healthcheck-viewer"}, "headers": {"Cache-Control": "no-store", "Connection": "close", "Content-Length": "113", "Content-Type": "application/json; charset=utf-8", "Date": "Mon, 13 Apr 2026 20:20:19 GMT", "Server": "Werkzeug/3.1.6 Python/3.11.14"}}
[2026-04-13T20:20:19.508008+00:00] starting_reader mode=prod host=127.0.0.1 port=8000 rails={'APP_ENV': 'prod', 'PORT': '8000', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0', 'LC_ALL': 'C', 'LANG': 'C', 'TZ': 'UTC'}
[2026-04-13T20:20:19.763631+00:00] sampler_response mode=prod status=403 http_version=HTTP/1.1 body={"body": {"code": "ERR_WRITER_FORBIDDEN", "error": "insufficient scope", "ok": false, "schema": "v1"}, "headers": {"Cache-Control": "no-store", "Connection": "close", "Content-Length": "86", "Content-Type": "application/json; charset=utf-8", "Date": "Mon, 13 Apr 2026 20:20:19 GMT", "Server": "Werkzeug/3.1.6 Python/3.11.14"}}
[2026-04-13T20:20:19.767017+00:00] gating_diagnostic expected=403? actual_status=403 body_keys=['code', 'error', 'ok', 'schema']
=== CODESPACES_HEALTHCHECK_END ===
```

## Evidence Output: stderr.log (Verbatim)

```text
\u001b[31m\u001b[1mWARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\u001b[0m
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8000
 * Running on http://10.0.2.168:8000
\u001b[33mPress CTRL+C to quit\u001b[0m
```

## Evidence Output: exit_codes.txt (Verbatim)

```text
dev_start_probe=124
codespaces_healthcheck=0
codespaces_disposition=CLOSED
local_dev_healthcheck=BINDING_EQUIVALENCE_CLOSURE
local_dev_disposition=CLOSED_BY_BINDING_EQUIVALENCE
```

## Evidence Output: codespaces_dev_sampler_url.md (Verbatim)

```text
environment: codespaces
dev_sampler_url: http://127.0.0.1:8000/internal/dev/sampler
app_env: dev
safe_mode: 1
allow_network: 0
lc_all: C
lang: C
tz: UTC
notes: healthcheck passed with dev success and prod-mode refusal diagnostic (expected 403).
```

## Evidence Output: local_dev_sampler_url.md (Verbatim)

```text
environment: local_dev
dev_sampler_url: http://127.0.0.1:8000/internal/dev/sampler
status: closed
reason: local_dev closed by binding-equivalence to the canonical Codespaces loopback DEV_SAMPLER_URL for EPIC029; this is not a separate runtime-host proof.
```

## Evidence Output: binding_disposition.md (Verbatim)

```text
codespaces: closed - rerun validated APP_ENV=dev success and prod-mode refusal diagnostic without discrepancy.
local_dev: closed - binding-equivalence closure to the canonical Codespaces loopback DEV_SAMPLER_URL for EPIC029; not an independently exercised second runtime.
```

## Evidence Output: created_files_sha256.txt (Verbatim)

```text
2d215d0f179b47ab979ec32c2c17934ea0115d76a728e825e321366ee4723744  audit/ops/hde-epic029/ops-01/commands.txt
da52bdde9e7c67656ac25ee488bbf1ad117744eacd51e1c8d947fe6f534d95ca  audit/ops/hde-epic029/ops-01/stdout.log
52a3132920798171a5fd5998e8c22091c23718c570a2e4986cbe0639194414bc  audit/ops/hde-epic029/ops-01/stderr.log
61d0894406051bdbe2a843b54885285b26d6057afcb79efa16791bb3dc139b6f  audit/ops/hde-epic029/ops-01/exit_codes.txt
9aef8d9536790b204c3ee619bb4907193251e6aef617d05de9b8e79b9cfcc74e  audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md
cfc3e1c1975e8529203cddf9970899a5472f9410868afb82b91cbef1e1797b30  audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md
1076d0b2d2b5531d2ccab0cdc38232ab9bed7f85a5e1b752316ed213fe4c04ea  audit/ops/hde-epic029/ops-01/binding_disposition.md
```

## Ops Task Final Review
- Codespaces closure evidence: PASS in this session log.
- local_dev closure evidence: CLOSED BY BINDING-EQUIVALENCE in this session log (explicitly not an independent local runtime-host proof).
- Decision: bounded documentation-and-evidence remediation complete for the W-004 local_dev closure rule mismatch.
