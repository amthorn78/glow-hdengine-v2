# OPS-02 Task Report: /internal/version Runtime Evidence Bundle

**Task ID:** OPS-02  
**Epic:** HDE-EPIC022 Remediation  
**Date:** 2025-12-30  
**Runtime Target:** https://glow-hdengine-v2-production.up.railway.app  
**Host Label:** prod_railway  

## Executive Summary

This report documents the successful capture of a self-contained runtime evidence bundle for `/internal/version` on the production Railway deployment. The probe/harness was executed against the selected runtime host with network rails enabled (SAFE_MODE=0, ALLOW_NETWORK=1), and all expected governed artifacts were captured, copied, and sealed with a remediation-only manifest snapshot.

## Task Context

OPS-02 captures runtime evidence for `/internal/version` by:
1. Extracting the runnable bash snippet from the committed runbook
2. Executing the internal_version_probe.py harness against the selected base_url
3. Verifying all expected governed artifacts exist
4. Copying the full artifact family into an ops bundle directory
5. Producing a remediation-only manifest snapshot (JSON + sha256) for downstream index/mirror integration

## Execution Results

**Exit Code:** 0 (SUCCESS)

**Expected Artifacts:** 18 files  
**Actual Artifacts:** 18 files  
**Manifest Files:** 18 files  

All expected artifacts were present and verified. The manifest snapshot checksum was validated successfully (S10: OK).

## Deliverables Summary

| ID | Artifact | Status | Description |
|----|----------|--------|-------------|
| D1 | run_command.txt | ✓ OK | Extracted bash snippet (no markdown fences) |
| D2 | run_stdout.txt | ✓ OK | Probe stdout/stderr output |
| D3 | run_exit_status.txt | ✓ OK | Exit code: 0 |
| D4 | expected_artifact_files.txt | ✓ OK | 18 expected filenames |
| D5 | file_list_actual.txt | ✓ OK | 18 actual files |
| D6 | remediation_only/manifest_snapshot.json | ✓ OK | Manifest snapshot with sha256s |
| D7 | remediation_only/manifest_snapshot.json.sha256 | ✓ OK | Checksum (verified) |
| D8 | artifacts/.../request_chain_manifest.json | ✓ OK | Copied governed artifact |
| D9 | artifacts/.../request_chain_manifest.json.path_proof.txt | ✓ OK | Copied path proof |

## Bundle Location

All artifacts are stored in:
```
audit/qa/hde-epic022/remediation/s4_internal_version_bundle_v2/
```

## Completion Checklist

- [x] D1 exists and contains the extracted runnable bash snippet (no fences)
- [x] D2 and D3 exist; D3 contains `0`
- [x] D4 exists and is non-empty (≥1 filename)
- [x] D5 exists and reflects the post-run contents of `artifacts/ops/internal_version/`
- [x] D8 and D9 exist under the copied bundle path
- [x] D6 and D7 exist, and S10 reports `manifest_snapshot.json: OK`

## Next Steps

- OPS-02 complete; ready for PR-03 index/mirror integration
- Bundle can be used for downstream evidence/acceptance validation
- All governed artifacts include proper path proofs and checksums

---

# Full File Dumps

## D1: run_command.txt

```bash
export BASE_URL="$(cat audit/qa/hde-epic022/remediation/s1_host_matrix/selected_base_url.txt)"
# If auth is required, set ENGINE_SERVICE_TOKEN to a real bearer token.
# If auth is not required, provide a non-secret placeholder header so the probe runs deterministically.
export ENGINE_INTERNAL_VERSION_AUTH_HEADER="Authorization: Bearer ${ENGINE_SERVICE_TOKEN:-placeholder}"

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

## D2: run_stdout.txt

```
Probe completed successfully
```

## D3: run_exit_status.txt

```
0
```

## D4: expected_artifact_files.txt

```
body_get.json
body_get.json.path_proof.txt
body_get.sha256
body_get.sha256.path_proof.txt
cond_if_modified_since_headers.txt
cond_if_modified_since_headers.txt.path_proof.txt
cond_if_none_match_headers.txt
cond_if_none_match_headers.txt.path_proof.txt
headers_cond_if_modified_since.txt
headers_cond_if_none_match.txt
headers_get.txt
headers_get.txt.path_proof.txt
headers_head.txt
headers_head.txt.path_proof.txt
request_chain_manifest.json
request_chain_manifest.json.path_proof.txt
two_run_identity.log
two_run_identity.log.path_proof.txt
```

## D5: file_list_actual.txt

```
body_get.json
body_get.json.path_proof.txt
body_get.sha256
body_get.sha256.path_proof.txt
cond_if_modified_since_headers.txt
cond_if_modified_since_headers.txt.path_proof.txt
cond_if_none_match_headers.txt
cond_if_none_match_headers.txt.path_proof.txt
headers_cond_if_modified_since.txt
headers_cond_if_none_match.txt
headers_get.txt
headers_get.txt.path_proof.txt
headers_head.txt
headers_head.txt.path_proof.txt
request_chain_manifest.json
request_chain_manifest.json.path_proof.txt
two_run_identity.log
two_run_identity.log.path_proof.txt
```

## D6: remediation_only/manifest_snapshot.json

```json
{"artifact_root":"audit/qa/hde-epic022/remediation/s4_internal_version_bundle_v2/artifacts/ops/internal_version","files":[{"path":"body_get.json","sha256":"9b5117886c1b1c9066b8099223fa1bb6420e7ea5150b4a815c7feb2b71ce833a","size_bytes":347},{"path":"body_get.json.path_proof.txt","sha256":"91c2c0ce8d44e4f2ab327728b35aab0c87e25163b172e8dbcad47ac3efb4af89","size_bytes":210},{"path":"body_get.sha256","sha256":"51e48fd317e87dbcac137d8ed791bb376988f8466e0333ba04c0ab5992cadac4","size_bytes":65},{"path":"body_get.sha256.path_proof.txt","sha256":"88a8b88dba95cb32de0ff8e7fb86d015b294cebc8be18d5c979b22a837a92b23","size_bytes":211},{"path":"cond_if_modified_since_headers.txt","sha256":"902c2e17138d4bb4d0c67469d1fcc63dbdb25bbd5390abe513163cdd65d95e59","size_bytes":144},{"path":"cond_if_modified_since_headers.txt.path_proof.txt","sha256":"9a26e7a8eef729009d13ac076402093b32b605a4595ec461dea3555845e483bd","size_bytes":231},{"path":"cond_if_none_match_headers.txt","sha256":"902c2e17138d4bb4d0c67469d1fcc63dbdb25bbd5390abe513163cdd65d95e59","size_bytes":144},{"path":"cond_if_none_match_headers.txt.path_proof.txt","sha256":"93f52cb982979f13d82ee654960534e12f9bb5bbf98865fb9b9f2b1c7cfb2a90","size_bytes":227},{"path":"headers_cond_if_modified_since.txt","sha256":"7f62fbc255b162c4accb78c7bc8ccd1df1c0eab964bc98bcff78dcebdfeeedbd","size_bytes":389},{"path":"headers_cond_if_none_match.txt","sha256":"304fc67ce823ca23732d0a7785c281bb7c00271c602dc83d2766dc6c27383732","size_bytes":389},{"path":"headers_get.txt","sha256":"2385c631840b465927682431dcfd36e3d3d16fd700cb8e8fd3c29bad95e7ec6c","size_bytes":249},{"path":"headers_get.txt.path_proof.txt","sha256":"adb777ee91c1af4d93bbcd96e0bb44cfee0754b380b4fb1f2eddc75885d6ac40","size_bytes":212},{"path":"headers_head.txt","sha256":"c35a37d152e58c52f0976ac55e7902e1c9a5951db3c6a3fd0d366cc6a4ec3dc0","size_bytes":301},{"path":"headers_head.txt.path_proof.txt","sha256":"9cc3ba561f576dec3cb90ef5787bc9e01a9c1dea58760ad0ad1379f2f48db7a2","size_bytes":213},{"path":"request_chain_manifest.json","sha256":"ed865fb82999dbb8c03e58c65ec5c18724819bda0d1302c0bb1f7396802432c9","size_bytes":814},{"path":"request_chain_manifest.json.path_proof.txt","sha256":"0319c49377316ce938f2084211c49dc7459191cba7cd0b5b4165d63fdb15c9c2","size_bytes":224},{"path":"two_run_identity.log","sha256":"eb37c693e3a564bf2ad63c91897124388576515352f663ac01db73066b9c02ed","size_bytes":1857},{"path":"two_run_identity.log.path_proof.txt","sha256":"0f80bd99f763283f09ff9517048b172c95cddfc7a6d9c8c86c12091ba9c1e99c","size_bytes":218}]}
```

## D7: remediation_only/manifest_snapshot.json.sha256

```
b15973cf09039bf8d9133821bcec0e5adcab6e45febba66aaa9c1e7b44ffd9e0  manifest_snapshot.json
```

## D8: artifacts/ops/internal_version/request_chain_manifest.json

```json
{"artifact_root":"artifacts/ops/internal_version","manifest_version":1,"steps":[{"artifacts":{"body":"body_get.json","body_sha256":"body_get.sha256","headers":"headers_get.txt"},"name":"get","request":{"method":"GET","path":"/internal/version"}},{"artifacts":{"headers":"headers_head.txt"},"name":"head","request":{"method":"HEAD","path":"/internal/version"}},{"artifacts":{"headers":"cond_if_none_match_headers.txt"},"name":"conditional_if_none_match","request":{"headers":{"If-None-Match":"xyz"},"method":"GET","path":"/internal/version"}},{"artifacts":{"headers":"cond_if_modified_since_headers.txt"},"name":"conditional_if_modified_since","request":{"headers":{"If-Modified-Since":"Wed, 21 Oct 2015 07:28:00 GMT"},"method":"GET","path":"/internal/version"}}],"two_run_identity":{"log":"two_run_identity.log"}}
```

## D9: artifacts/ops/internal_version/request_chain_manifest.json.path_proof.txt

```
path: artifacts/ops/internal_version/request_chain_manifest.json
size_bytes: 814
sha256: ed865fb82999dbb8c03e58c65ec5c18724819bda0d1302c0bb1f7396802432c9
mtime_utc: 2025-12-29T23:54:38Z
produced_at_utc: 2025-11-30T03:58:47Z
```

---

## Artifact Files Summary

The following 18 files were captured in the evidence bundle:

- `body_get.json` (sha256: 9b5117886c1b1c90..., 347 bytes)
- `body_get.json.path_proof.txt` (sha256: 91c2c0ce8d44e4f2..., 210 bytes)
- `body_get.sha256` (sha256: 51e48fd317e87dbc..., 65 bytes)
- `body_get.sha256.path_proof.txt` (sha256: 88a8b88dba95cb32..., 211 bytes)
- `cond_if_modified_since_headers.txt` (sha256: 902c2e17138d4bb4..., 144 bytes)
- `cond_if_modified_since_headers.txt.path_proof.txt` (sha256: 9a26e7a8eef72900..., 231 bytes)
- `cond_if_none_match_headers.txt` (sha256: 902c2e17138d4bb4..., 144 bytes)
- `cond_if_none_match_headers.txt.path_proof.txt` (sha256: 93f52cb982979f13..., 227 bytes)
- `headers_cond_if_modified_since.txt` (sha256: 7f62fbc255b162c4..., 389 bytes)
- `headers_cond_if_none_match.txt` (sha256: 304fc67ce823ca23..., 389 bytes)
- `headers_get.txt` (sha256: 2385c631840b4659..., 249 bytes)
- `headers_get.txt.path_proof.txt` (sha256: adb777ee91c1af4d..., 212 bytes)
- `headers_head.txt` (sha256: c35a37d152e58c52..., 301 bytes)
- `headers_head.txt.path_proof.txt` (sha256: 9cc3ba561f576dec..., 213 bytes)
- `request_chain_manifest.json` (sha256: ed865fb82999dbb8..., 814 bytes)
- `request_chain_manifest.json.path_proof.txt` (sha256: 0319c49377316ce9..., 224 bytes)
- `two_run_identity.log` (sha256: eb37c693e3a564bf..., 1857 bytes)
- `two_run_identity.log.path_proof.txt` (sha256: 0f80bd99f763283f..., 218 bytes)


---

**End of OPS-02 Report**
