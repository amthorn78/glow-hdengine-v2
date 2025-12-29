# Internal version probe (runtime) — runbook snippet

Use the existing `internal_version_probe.py` harness to capture `/internal/version` evidence against the selected runtime base URL, then seal the deterministic request-chain manifest and its path proof.

```bash
export BASE_URL="$(cat audit/qa/hde-epic022/remediation/s1_host_matrix/selected_base_url.txt)"
export ENGINE_INTERNAL_VERSION_AUTH_HEADER="Authorization: Bearer ${ENGINE_SERVICE_TOKEN:?set auth token}"

env SAFE_MODE=0 ALLOW_NETWORK=1 LC_ALL=C LANG=C TZ=UTC \
python audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/tools/internal_version_probe.py \
  --base-url "$BASE_URL" \
  --out-dir artifacts/ops/internal_version \
  --auth-header-env ENGINE_INTERNAL_VERSION_AUTH_HEADER && \
python - <<'PY'
from tools.ops.internal_version_artifacts import ensure_request_chain_manifest

ensure_request_chain_manifest("artifacts/ops/internal_version", allow_create=True)
PY
```

Artifacts are written to `artifacts/ops/internal_version/` and are expected to include (all files should be non-empty, with matching `*.path_proof.txt` where present):

- `body_get.json`
- `body_get.json.path_proof.txt`
- `body_get.sha256`
- `body_get.sha256.path_proof.txt`
- `cond_if_modified_since_headers.txt`
- `cond_if_modified_since_headers.txt.path_proof.txt`
- `cond_if_none_match_headers.txt`
- `cond_if_none_match_headers.txt.path_proof.txt`
- `headers_cond_if_modified_since.txt`
- `headers_cond_if_none_match.txt`
- `headers_get.txt`
- `headers_get.txt.path_proof.txt`
- `headers_head.txt`
- `headers_head.txt.path_proof.txt`
- `request_chain_manifest.json`
- `request_chain_manifest.json.path_proof.txt`
- `two_run_identity.log`
- `two_run_identity.log.path_proof.txt`

Success signal: the command exits 0 and the files above exist under `artifacts/ops/internal_version/` with the manifest proof matching the manifest bytes.
