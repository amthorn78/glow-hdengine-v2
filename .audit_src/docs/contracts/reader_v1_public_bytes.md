# Reader v1 — Public Bytes (example)

This page shows a single canonical example for Reader v1. All byte rules (serializer, idempotence, AB↔BA, two-run identity) are defined in the Spec.

Compact JSON body (exact shape; one trailing LF implied):
{"categories":[{"id":"harmony","band":"Open"}],"eligible":true,"idempotence_hash":"<64hex>","meta":{},"release_id":"<64hex>"}

Notes:
• Public body is numeric-free.
• The serializer is canonical (UTF-8, sorted keys, compact separators, exactly one trailing LF).
• The idempotence_hash is computed over the canonical preimage (body without that field), then re-serialized.
