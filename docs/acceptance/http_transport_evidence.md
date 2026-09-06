# Reader — HTTP Transport Evidence (Acceptance)

**Scope:** Reader v1 transport; public payload remains numeric-free, bands-only.

<a id="tokens-must-be-pass"></a>

## Required transport predicates and evidence

All predicates below remain required within this document's stated scope. The retained identifiers are optional historical/evidence lookup labels with their original meanings; new-work acceptance does not require token issuance or token PASS. A label alone proves no HTTP behavior. Any current acceptance claim must be established from applicable native source, tests and captured transport evidence for that predicate and candidate. This framing update does not attest current conformance or reconcile differences in retained technical wording; assess discrepancies against the actual owning sources.

- `HTTP_200_HEADERS_OK` — JSON Content-Type; Cache-Control `private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding` (exact order, single comma+space); **ETag = strong, quoted, lowercase-hex sha256(identity LF)** (pre-compression).
- `HTTP_ETAG_INVARIANCE_IDENTITY_GZIP_OK` — identity ↔ gzip ETag identical (Brotli optional via `.note.json`).
- `HTTP_304_OMIT_CONTENT_TYPE_OK` — 304 omits `Content-Type`; **no body** (Content-Length 0 or absent).
- `HTTP_304_VALIDATORS_REPEAT_OK` — 304 repeats ETag / Vary / Cache-Control identically to the prior 200.
- `HTTP_HEAD_CL_AND_CT_OK` — HEAD includes Content-Type; **no body**; `Content-Length == len(identity bytes)`; validators equal 200.
- `HTTP_ERRORS_NOSTORE_NOETAG_OK` — Errors/writers are JSON, **no-store**, **no ETag**.
- `HTTP_POST_METHOD_POSTURE_OK` — Reader POST ⇒ 405 typed JSON (`no-store`, no ETag); Compat POST ⇒ 200 non-conditional.
- `COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 typed `invalid_json`, `no-store`, no ETag (GET remains probe-only; POST is the compat compute surface).

## Evidence shape
Header proofs are plain-text captures: a status line plus ordered header lines, LF-terminated.
Reader bytes are LF-terminated; Reader↔CLI parity is defined via the CLI `--dump-reader` sidecar (not showcompat stdout).

<!-- EPIC-004 PATCH: _arch naming compatibility note -->
### Snapshot directory naming (compatibility)
- **New snapshots (recommended):** `_arch/EPIC-004_<timestamp>/…`
- **Historic snapshots (valid):** `_arch/EPIC004_<timestamp>/…`

Both forms are accepted by our docs and tools. **Do not rename** existing `_arch` folders.

# Internal Ops — HTTP Transport Evidence (EPIC-005)

**Endpoint:** `GET /internal/version` (+ `HEAD`)

**Body (200):** exactly:
```json
{"engine_tag","release_id","invocation_tag","build_commit","emitter_sha256"}
```
LF-terminated JSON; no extra fields.

**Headers (200):**

* `Content-Type: application/json; charset=utf-8`
* `Cache-Control: no-store`
* **No** `ETag`

**HEAD (200):**

* same validators as 200
* **no body**
* `Content-Length ==` 200 body bytes

**Conditionals:** `If-None-Match` ignored — still **200** (no 304)

**Override (prod):** `X-Identity-Override` ⇒ **400** JSON; `no-store`; **no `ETag`**

**Evidence (repo-relative):**

* `artifacts/headers/internal_version_200.txt`
* `artifacts/headers/internal_version_head.txt`
* `artifacts/headers/internal_version_if_none_match.txt`
* `artifacts/headers/internal_version_override_denied.txt`
* `artifacts/identity/service_identity.json`

# Writers — HTTP Transport Evidence (EPIC-008)

**Scope:** Writer endpoints only.

**Transport (must hold):**
- `Cache-Control: no-store`, **no ETag**, **no compression**, **never 304** (ignore `If-*`).
- **HEAD → 405** and **OPTIONS → 204** with no body, `Allow: POST, OPTIONS`, `Content-Length: 0`.
- Content-Type present only on 2xx bodies and typed errors (`application/json; charset=utf-8`).

**Validation (must hold):**
- Diagnostic empty-body exempt from Content-Type; otherwise require `application/json; charset=utf-8`.
- Malformed JSON/UTF-8/BOM → **400**; unknown key → **422**; other schema violations → **422**; body ≥ 32 768 bytes → **413**.

**Auth (must hold):**
- `Authorization: Bearer` with `admin:write` (401 with `WWW-Authenticate: Bearer` vs 403).

**Evidence pointers (repo-relative):**
- `artifacts/headers/writer_head_405.txt`
- `artifacts/headers/writer_204.txt`
- `artifacts/headers/writer_200_diagnostic.json`
- `artifacts/headers/writer_error_400.json`
- `artifacts/headers/writer_error_401.json`
- `artifacts/headers/writer_error_403.json`
- `artifacts/headers/writer_error_415.json`
- `artifacts/headers/writer_error_422_invalid_input.json`
- `artifacts/headers/writer_error_422_unknown_key.json`
- `artifacts/headers/writer_error_413.json`
- `artifacts/proofs/writers_no_304.txt`
- `artifacts/idempotence/preimage_compare.log`
- `artifacts/idempotence/two_run_identity.log`
