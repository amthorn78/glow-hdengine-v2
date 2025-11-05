# Writer Transport Contract (EPIC-008)

- `Cache-Control: no-store`
- `ETag: <absent>`
- `Content-Encoding: <absent>`
- Never returns 304 (conditionals ignored)
- HEAD → 405 (no body) with `Allow: POST, OPTIONS`, `Content-Length: 0`
- OPTIONS → 204 (no body) with `Allow: POST, OPTIONS`, `Content-Length: 0`
