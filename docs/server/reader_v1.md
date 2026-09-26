# DEPRECATED — Reader v1 (server)

This document is deprecated. The **only** HTTP home for Reader is:
`adapter/http_reader.py`

See:
- `docs/RUN.md` for the canonical start command
- `docs/acceptance/http_transport_evidence.md` for transport acceptance
- `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md` for the current public bodies

## Current state (HDE-EPIC040)

Everything below this section is retained history. Where it disagrees with this section, this section describes the current repository implementation.

- Production Reader: `POST /api/reader?v=1` (Reader v1) and `POST /api/reader?v=2` (Reader v2). The production blueprint (`get_reader_api_bp` in `adapter/http_reader.py`) is mounted under `/api` by every app factory: `adapter/factory.py`, `adapter/wsgi.py` and `adapter/http_reader.py::create_app`. Version selection, request body, lookup, transport and error rules are shared by both versions; see `docs/contracts/reader_v2_public_bytes.md`.
- Every method other than `POST` on `/api/reader` returns the governed 405 (`ERR_NOT_FOUND`, `Allow: POST`, `no-store`).
- Dev Reader: `GET /reader?v=1` (and `HEAD`) is Reader v1 only; any other `v` returns 400 `ERR_READER_INVALID_VERSION`. When `APP_ENV` is set to a value other than `dev`, it returns 403 `ERR_READER_FORBIDDEN`; an unset `APP_ENV` is treated as `dev`. `a` and `b` are chart paths resolved against the server's working directory that must resolve inside `fixtures/charts/` (for example `fixtures/charts/alice.json`); `a_tz` and `b_tz` are required when a chart has no `tz`.
- `POST /reader` (unprefixed) is not the production Reader: it returns the governed 405 with `Allow: GET, HEAD`.
- Local start: `scripts/dev_start_reader.sh` runs `python -m adapter.http_reader`, which binds `0.0.0.0` on `PORT` (default `8000`). Run it from the repository root. The legacy notice below names `dev/reader_harness/app.py`; as of HDE-EPIC040-PR07 that file raises `AttributeError` at import, so it is not a start path.
- Known limitation: a path that no route serves receives the framework's HTML 404 from `adapter/factory.py` and `adapter/http_reader.py`; `adapter/wsgi.py` answers with the JSON `ERR_NOT_FOUND` envelope.

---

> **Legacy notice (to be removed):** This page describes a deprecated server/ path. The canonical HTTP adapter is `adapter/http_reader.py`. For local runs use the dev runner `dev/reader_harness/app.py` with `APP_ENV=dev`. Update examples and imports accordingly.

docs/server/reader_v1.md  

Title: Reader v1 — Dev Harness that Mirrors CLI
Version: 2.1
Owner: Cyrano (Tech Writer)
Status: Draft (HTTP Transport Evidence scope; pending ISIS-12 sign-off)
Cards: CORE-READER-A5 (body invariants), HTTP Transport Evidence transport


---

1. Purpose and scope

Reader v1 is a developer-only HTTP harness. It returns bytes identical to the CLI public stdout for the same inputs. It is not for production traffic; use it for acceptance, smoke tests, and reproducible developer testing of the public envelope.

Contract ownership. The public body shape (keys, enums, serializer rules, idempotence_hash preimage) lives in the HD Engine — Math & Technical Spec; HTTP transport semantics live in the Environment & Integration Plan (HTTP Transport Evidence). This document references both and does not redefine them. 

> HTTP Transport Evidence transport: Reader implements strong ETag, caching validators, conditional GET, and HEAD parity. Body semantics remain frozen by the Spec. 




---

2. Endpoint surface

GET /health → returns 200 and body ok\n. 

GET /reader?v=1&a=<chart path>&b=<chart path>&a_tz=<IANA>&b_tz=<IANA> → dev Reader v1 (`APP_ENV=dev`); returns LF-terminated public bytes identical to the CLI `--dump-reader` sidecar for the same charts. The production Reader is `POST /api/reader?v=1|2` (see "Current state (HDE-EPIC040)" above); `GET /api/reader` returns 405.


Parameter policy

v=1 only (version is explicit to allow future bodies without changing this harness path). 

a, b are chart paths resolved against the server's working directory; each must resolve inside fixtures/charts/ (for example fixtures/charts/alice.json), so run the server from the repository root.

a_tz, b_tz are required if the respective chart files do not include a time zone (IANA names). 



---

3. Gating and path safety

If APP_ENV != dev → return 403 and do not read from the filesystem. Body: {"error":"forbidden"}\n. 

If APP_ENV == dev → allow reads only from fixtures/charts/*; deny .. traversal and symlinks. 



---

4. Transport policy (HTTP Transport Evidence)

Success (200 OK)

Content-Type: application/json; charset=utf-8

Cache-Control: private, max-age=0, must-revalidate

Vary: Authorization, Accept-Encoding

ETag: "<sha256(final LF-terminated body bytes)>" (strong, quoted; computed on the pre-compression entity)

Invariance: the ETag is identical for identity, gzip, and br responses. 


Conditional GET (304 Not Modified)

Accept comma-separated If-None-Match; ignore weak W/ tokens; ignore *.

Return 304 with no body. Include ETag, Vary, Cache-Control. Content-Length: 0 or absent; Content-Type optional. 


HEAD parity

Same validators as GET 200. No body.

Content-Length == len(identity GET body). 


Errors (4xx/5xx)

One-line JSON + LF. Content-Type: application/json; charset=utf-8.

No ETag. Cache-Control: no-store. 


Framework controls

Disable any auto-ETag/auto-cache features. 



---

5. Public contract and equivalence to CLI

Public JSON is numeric-free and bands-only for SPA use.

Canonical serializer: UTF-8, sort_keys=True, separators=(',',':'), ensure_ascii=False, exactly one trailing \n.

Top-level keys (sorted): ["categories","eligible","idempotence_hash","meta","release_id"].

categories: array with exactly one item in v1 whose only fields are {"id":"harmony","band":"Cool|Open|Warm|Glow"}.

Output MUST end with one \n, be BOM-free and ANSI-free.

AB↔BA parity and two-run identity MUST hold.

Reader v1 MUST call the single emitter to produce bytes; do not duplicate serializer logic in the handler. 


> Contract source: See Math & Tech Spec §1 for the authoritative public body rules (keys, enums, idempotence_hash preimage, serializer discipline).




---

6. Error responses

Error bodies are single-line JSON with a trailing LF.

400: {"error":"invalid_path"} | {"error":"invalid_json"} | {"error":"missing_tz_A"} | {"error":"missing_tz_B"}

403: {"error":"forbidden"}\n
(Align exact tokens with the Spec’s canonical list.) 



---

7. HTTP Transport Evidence acceptance — evidence-only

Purpose. Prove Reader transport behavior and CLI equivalence without prescribing commands in this doc.

7.1 Required artifacts (exact paths)

artifacts/cards/A7/reader_AB.json
artifacts/cards/A7/headers_AB.txt
artifacts/cards/A7/headers_AB_gzip.txt
artifacts/cards/A7/headers_AB_br.txt
artifacts/cards/A7/headers_304.txt
artifacts/cards/A7/headers_head.txt
artifacts/cards/A7/headers_health.txt
artifacts/cards/A7/error.json
artifacts/cards/A7/headers_err.txt
artifacts/cards/A7/validation.log

(AB/BA CLI outputs are referenced from the A3 artifacts for byte-equality checks.)

7.2 PASS markers (names only)

READER_HEALTH_OK
READER_EQ_CLI_AB_OK
READER_EQ_CLI_BA_OK
READER_PREIMAGE_OK
READER_200_CT_OK
READER_200_CACHECTL_OK
READER_200_VARY_OK
READER_200_ETAG_PRESENT="<etag>"
READER_200_ETAG_MATCH=OK
READER_200_GZIP_ETAG_SAME=OK
READER_200_BR_ETAG_SAME=OK
READER_304_STATUS_OK
READER_304_EMPTY_BODY_OK
READER_HEAD_ETAG_OK
READER_HEAD_CL_MATCH_OK
READER_400_STATUS_OK
READER_400_NO_ETAG_OK
READER_400_NOSTORE_OK
READER_400_CT_OK
READER_AUTOTAG_DISABLED_OK

(Transport validator meanings are owned by the Environment & Integration Plan.)


---

8. Appendix

Query parameter rules

a and b MUST be relative and resolved beneath fixtures/charts/. Reject absolute paths, traversal, and symlinks.

a_tz and b_tz MUST be valid IANA names if not present in the chart files. 


Parser and serializer

Use the same sercanon and preimage rule as the CLI. Do not introduce a second serializer or alternate idempotence code path. 



---

Change note (2.1): Converted §7 from command snippets to evidence-only (artifacts + PASS markers), clarified contract ownership pointers, and kept HTTP Transport Evidence transport text aligned with the Env Plan. 

