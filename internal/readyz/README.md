# /internal/readyz — Contract Snapshot (v1)

**Bodies**: UTF-8 JSON, compact, sorted keys, exactly one trailing `\n`.
**Headers**: Always `Cache-Control: no-store`, `Content-Type: application/json; charset=utf-8`.
Success adds `X-Toggles-SHA: <hex64>`; failures do not.

## 200 OK (success)
- Body: `readyz_200.json`
- Headers: `readyz_200_headers.txt`

## 503 Service Unavailable (failure)
- Body: `readyz_503.json`
- Headers: `readyz_503_headers.txt`

Notes:
- Correlation-ID in these examples is a UUID v4.
- HSTS header only in prod environments.
- Replace placeholder hex values with real runtime values.
