# Reader v2 — Public Bytes (contract summary and examples)

Reader v2 exposes the full Magic-10 set as bands only. HDE-EPIC040-PR06a delivered it. Reader v1 is unchanged and stays available on the same route; see `docs/contracts/reader_v1_public_bytes.md`.

## Owning sources

- Normative contract: `PF10-HDE-Build-Notes`, addendum "HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work" (Canon conflict C040-07). While that addendum is active, it is the authoritative source for Reader v2 and supersedes conflicting permanent canon, including the statement in `PF05-Canon-HDE-CLI-API-Vendor-Ref` that the production Reader refuses `v=2`.
- Drainage: as of HDE-EPIC040-PR07, C040-07 has not been drained into `PF01-Canon-HDE-Math-Spec`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref` or `PF12-Canon-HDE-Schemas-and-Artifacts`, nor into the consequential statements of `PF14-Canon-HDE-Mechanics-Guide` and `PF29-Canon-HDE-Users-Guide`. That drainage belongs to their maintainers.
- Machine contract: `schemas/reader.v2.schema.json` with its `schemas/reader.v2.schema.json.sha256` sidecar. The schema is a release member.
- Goldens: `goldens/reader/v2/`, written by `scripts/make_reader_v1_goldens.py`.

## Route and request (current implementation)

- Route: `POST /api/reader?v=2`. The same route serves Reader v1 with `v=1`, under the same request, lookup, eligibility and transport rules.
- Version selection: the query carries exactly one `v`, with the value `1` or `2`. A missing, empty, repeated or other value returns 400 `ERR_READER_INVALID_VERSION` before the body is read.
- Body: a JSON object with exactly the keys `a_id` and `b_id`, each a lowercase canonical UUID; at most 32,768 bytes; UTF-8 without a byte-order mark. Any other body returns 422 `ERR_READER_INVALID_INPUT`.
- Lookup: each identity is resolved by one read-only current-row lookup. An unavailable lookup returns 503 `ERR_M10_RESOLVER_UNAVAILABLE`; a missing row returns 404 `ERR_M10_PERSON_UNRESOLVED`.
- Other methods: every method other than `POST` on `/api/reader` returns 405 with the `ERR_NOT_FOUND` envelope, `Allow: POST` and `Cache-Control: no-store`.
- Known limitation: a path that no route serves, such as `/api/reader/missing`, receives the framework's HTML 404 from `adapter/factory.py` and `adapter/http_reader.py`; only `adapter/wsgi.py` answers with the JSON `ERR_NOT_FOUND` envelope. This gap belongs to the HTTP transport owner.

## Success body

- Exactly six keys: `categories`, `eligible`, `idempotence_hash`, `meta`, `reader_version` and `release_id`. `reader_version` is always `"v2"`. No field is numeric.
- Eligible pair: `categories` has exactly ten `{"band","id"}` items, one per Magic-10 category, in the canonical order of `catalog/magic10.json`: `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`. The array is ordered; it is not a set. Each `band` is `Cool`, `Open`, `Warm` or `Glow`.
- Ineligible pair: `categories` is `[]`.
- `idempotence_hash` is the SHA-256 of the canonical bytes of the other five keys. Canonical JSON, AB↔BA identity and two-run identity apply as they do to Reader v1.

## Error body

- Exactly four keys: `code`, `error`, `ok` (always `false`) and `schema` (always `"v1"`: the `error_v1` envelope version, not the Reader version).
- `code` and `error` are one of the governed pairs listed in `$defs.error` of `schemas/reader.v2.schema.json`.

## Transport

- Success: 200 with `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate` and `Vary: Authorization, Accept-Encoding`. There is no `ETag`: `POST` is non-conditional and `If-*` headers are ignored.
- Errors: canonical `error_v1` bytes with `Cache-Control: no-store` and no `ETag`.

## Examples (synthetic)

Each example is the named golden without its trailing LF. Its `release_id` is a synthetic 64-character value, not the current release, and `meta` carries fixture values.

Eligible pair (`goldens/reader/v2/g03_eligible_ten_in_order.json`):

```json
{"categories":[{"band":"Cool","id":"harmony"},{"band":"Open","id":"heat"},{"band":"Warm","id":"communication"},{"band":"Glow","id":"alignment"},{"band":"Cool","id":"comfort"},{"band":"Open","id":"consistency"},{"band":"Warm","id":"expansion"},{"band":"Glow","id":"creativity"},{"band":"Cool","id":"drive"},{"band":"Open","id":"balance"}],"eligible":true,"idempotence_hash":"9e51c57b9e613d9c0f52486979c3c247c265c568a690240ff4e5a11ac445dea4","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v2","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Ineligible pair (`goldens/reader/v2/g01_ineligible.json`):

```json
{"categories":[],"eligible":false,"idempotence_hash":"a2cca383ec8f8542d1d4cd04841d5ee389d38fa0ad38b41b4ca7f49b3ff1e23b","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v2","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Unsupported version (`goldens/reader/v2/g04_error_invalid_version.json`):

```json
{"code":"ERR_READER_INVALID_VERSION","error":"unsupported reader version","ok":false,"schema":"v1"}
```

## Scope

- No CLI flag emits Reader v2. Reader↔CLI dump parity (`hdctl showcompat --dump-reader`) remains a Reader v1 family.
- No Reader v2 body carries a numeric, a prompt, a narrative key, a score, a UUID or a Gate value.
- This page describes the repository implementation. It does not establish QA, acceptance, deployment, activation or PF09 status.

Tests: `tests/http/test_reader_post_v2.py`, `tests/reader_v1/test_schema.py`, `tests/reader_v1/test_goldens.py` and `tests/reader_v1/test_emitter.py`.
