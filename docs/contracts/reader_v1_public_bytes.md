# Reader v1 — Public Bytes (example)

This page shows a single canonical example for Reader v1. All byte rules (serializer, idempotence, AB↔BA, two-run identity) are defined in the Spec.

Owning sources: the Reader v1 covenant is owned by `PF01-Canon-HDE-Math-Spec` §2.2 and §4.7, and its transport by `PF05-Canon-HDE-CLI-API-Vendor-Ref`. The machine contract is `schemas/reader.v1.schema.json` with its `.sha256` sidecar. Goldens live in `goldens/reader/v1/` and are written by `scripts/make_reader_v1_goldens.py`. Reader v2 is documented in `docs/contracts/reader_v2_public_bytes.md`.

Compact JSON body (synthetic example: `goldens/reader/v1/g03_harmony_open.json` without its trailing LF; its `release_id` is a synthetic 64-character value, not the current release):

```json
{"categories":[{"band":"Open","id":"harmony"}],"eligible":true,"idempotence_hash":"117b9f95a965ed280482fc4f8290536aa34ded9528acb7dbf19c2140fbc351e7","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v1","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Notes:
• Public body is numeric-free.
• The serializer is canonical (UTF-8, sorted keys, compact separators, exactly one trailing LF).
• The idempotence_hash is computed over the canonical preimage (body without that field), then re-serialized.
• The body has exactly six keys. `reader_version` is always `"v1"`, and `meta` has exactly `engine_tag` and `invocation_tag`. An eligible pair carries exactly one `harmony` item; an ineligible pair carries `"categories":[]` (`goldens/reader/v1/g01_minimal_ineligible.json`).

## Error body (C040-08)

Reader v1 errors have exactly four keys: `code`, `error`, `ok` (`false`) and `schema` (`"v1"`). The schema's error branch (`$defs.error`) admits only the governed code/message pairs that the production route (`POST /api/reader?v=1`) and dev `GET /reader` emit. `retry_after_ms` is not part of this envelope.

HDE-EPIC040-PR06b conformed the error branch to the emitted envelope under Canon conflict C040-08, recorded in `PF10-HDE-Build-Notes`, addendum "HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08)". As of HDE-EPIC040-PR07, drainage of C040-08 into `PF01-Canon-HDE-Math-Spec` §2.3 and `PF04-Canon-HDE-Governance` §8.1.2, which still describe the envelope without `schema`, is pending with their maintainers.

Synthetic example (`goldens/reader/v1/g06_error_invalid_input.json` without its trailing LF):

```json
{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}
```

## Retired identities (history)

Before HDE-EPIC040-PR06a, the published schema and goldens used the category identities `open_leader`, `warm_leader`, `cool_leader` and `glow_leader`, and the schema permitted a `prompt` field. PR06a retired them from the contract, and no Reader route emits them. They remain only in retained historical records and in the legacy `scripts/hd_cli.py` stub, which is not a Reader surface.

<!-- EPIC-004 PATCH: bands-only + transport -->
## EPIC-004 — Reader v1 public payload posture
**Numeric-free**, bands-only surface. The engine selects **keys** (no copy).
Historical example (EPIC-004, shape only; not the current body shown above):
```json
{"compat":[{"id":"harmony","band":"warm"}]}
```

## EPIC-004 — HTTP Transport Evidence (Reader endpoints)
These rules apply to the dev Reader `GET /reader` (and `HEAD`). The production `POST /api/reader` is non-conditional: a success carries no `ETag`, the 304 and `HEAD` rules do not apply to it, and its errors follow the last rule below.
- **200**: JSON content-type; Cache-Control `private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding` (exact order, single comma+space); **ETag = strong, quoted, lowercase-hex sha256(identity LF)** (pre-compression).
- **304 (after prior 200)**: **no body** (Content-Length 0 or absent); **omit Content-Type**; repeat validators (ETag / Vary / Cache-Control) **exactly**.
- **HEAD**: include Content-Type; **no body**; `Content-Length == len(identity bytes)`; validators **equal** to 200.
- **Errors/Writers**: JSON; **no-store**; **no ETag**.
