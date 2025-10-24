# Reader v1 — Public Bytes (example)

This page shows a single canonical example for Reader v1. All byte rules (serializer, idempotence, AB↔BA, two-run identity) are defined in the Spec.

Compact JSON body (exact shape; one trailing LF implied):
{"categories":[{"id":"harmony","band":"Open"}],"eligible":true,"idempotence_hash":"<64hex>","meta":{},"release_id":"<64hex>"}

Notes:
• Public body is numeric-free.
• The serializer is canonical (UTF-8, sorted keys, compact separators, exactly one trailing LF).
• The idempotence_hash is computed over the canonical preimage (body without that field), then re-serialized.

<!-- EPIC-004 PATCH: bands-only + transport -->
## EPIC-004 — Reader v1 public payload posture
**Numeric-free**, bands-only surface. The engine selects **keys** (no copy).
Example (shape only):
```json
{"compat":[{"id":"harmony","band":"warm"}]}
```

## EPIC-004 — HTTP Transport Evidence (Reader endpoints)
- **200**: JSON content-type; Cache-Control `private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding` (exact order, single comma+space); **ETag = strong, quoted, lowercase-hex sha256(identity LF)** (pre-compression).
- **304 (after prior 200)**: **no body** (Content-Length 0 or absent); **omit Content-Type**; repeat validators (ETag / Vary / Cache-Control) **exactly**.
- **HEAD**: include Content-Type; **no body**; `Content-Length == len(identity bytes)`; validators **equal** to 200.
- **Errors/Writers**: JSON; **no-store**; **no ETag**.
