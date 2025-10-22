# Impact vs Touched — EPIC-004

**Impact (why):** Enforce single canonical serializer/emitter for all public JSON (Reader success+errors, CLI) and refresh HTTP Transport Evidence (200, 200[gzip invariance], 304, HEAD, POST 405; errors no-store/no ETag). No changes to math or public schema.

**Touched (code):**
- `engine/serializer/canon.py` — add `sercanon` (EPIC004-only alias `dumps`).
- `engine/presenter/emitter.py` — emitter calls `canon.sercanon`.
- `engine/emit_public.py` — idempotence hash from `canon.sercanon(pre)`; final bytes via `emit_compact_json`.
- `adapter/http_reader.py` — `_error(...)` uses shared emitter; `@bp.post("/reader")` returns typed JSON 405 (`no-store`, no ETag).

**Touched (evidence):**
- `artifacts/epic004/headers/*.json` — lower-cased header goldens (200/304/HEAD/POST; compat* if mounted).
- `artifacts/epic004/bytes/*` — identity/gzip/cli + idempotence_provenance.
- `artifacts/epic004/validation/*` — matrix, schema report, callgraph, touched_paths, impact note, service_cmd.txt.
- `_arch/EPIC-004_<ts>/*` — tree snapshot + homes.json.

**Why this is sufficient:** Satisfies serializer/emitter single-home, hashing provenance, and transport invariants without altering public contract.
