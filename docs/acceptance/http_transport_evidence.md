# Reader — HTTP Transport Evidence (Acceptance)

**Scope:** Reader v1 transport; public payload remains numeric-free, bands-only.

## Tokens (must be PASS)
- `HTTP_200_HEADERS_OK` — JSON Content-Type; Cache-Control `private, max-age=0, must-revalidate`;
  `Vary: Authorization, Accept-Encoding` (exact order, single comma+space);
  **ETag = strong, quoted, lowercase-hex sha256(identity LF)** (pre-compression).
- `HTTP_ETAG_INVARIANCE_IDENTITY_GZIP_OK` — identity ↔ gzip ETag identical (Brotli optional via `.note.json`).
- `HTTP_304_OMIT_CONTENT_TYPE_OK` — 304 omits `Content-Type`; **no body** (Content-Length 0 or absent).
- `HTTP_304_VALIDATORS_REPEAT_OK` — 304 repeats ETag / Vary / Cache-Control identically to the prior 200.
- `HTTP_HEAD_CL_AND_CT_OK` — HEAD includes Content-Type; **no body**; `Content-Length == len(identity bytes)`;
  validators equal 200.
- `HTTP_ERRORS_NOSTORE_NOETAG_OK` — Errors/writers are JSON, **no-store**, **no ETag**.
- `HTTP_POST_METHOD_POSTURE_OK` — Reader POST ⇒ 405 typed JSON (`no-store`, no ETag); Compat POST ⇒ 200 non-conditional.
- `COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 typed `{"error":"body_not_allowed"}`, `no-store`, no ETag.

## Evidence shape
Header goldens are canonical JSON: **lowercased keys**, sorted, compact, **exactly one trailing LF**.
Bytes are LF-terminated; CLI output equals the Reader identity bytes (parity).

<!-- EPIC-004 PATCH: _arch naming compatibility note -->
### Snapshot directory naming (compatibility)
- **New snapshots (recommended):** `_arch/EPIC-004_<timestamp>/…`
- **Historic snapshots (valid):** `_arch/EPIC004_<timestamp>/…`

Both forms are accepted by our docs and tools. **Do not rename** existing `_arch` folders.
