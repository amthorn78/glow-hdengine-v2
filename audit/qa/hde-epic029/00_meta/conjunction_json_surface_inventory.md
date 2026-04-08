# HDE-EPIC029 PR-01 — Conjunction JSON Surface Inventory (Bounded)

## Scope guard (PF09.4 / HDE-CONJ009.1)

This inventory is intentionally bounded to conjunction JSON-emitting loci that are already repo-proven and in-scope for PR-01.

Included loci (minimum required):
- `/reader`
- `/dev/writer/conjunction`
- `/internal/dev/sampler`

Additional conjunction loci were included only when already repo-proven and in the same bounded conjunction family.
No new routes, no new proof surfaces, and no alternate serializer/emitter paths are introduced by this inventory.

## Single-emitter verification checklist

Canonical shared emitter: `engine.presenter.emitter.emit_public` (delegates to `engine.serializer.canon.sercanon`).

### 1) `/reader` (GET)
- Route defined in `adapter/http_reader.py` as `@bp.get("/reader")`.
- Success bytes are emitted by `emit_fn(...)`; the default `emit_fn` is `engine.runtime.emit_reader_public_bytes`.
- `engine.runtime.emit_reader_public_bytes` emits through `emit_public_envelope(...)`, which calls the shared emitter `emit_public`.
- Result: **uses single shared emitter path**.

### 2) `/dev/writer/conjunction` (GET)
- Route defined in `adapter/http_reader.py` as `@bp.get("/dev/writer/conjunction")`.
- Handler calls `_emit_dev_writer_conjunction_response()`, which returns `_emit_writer_response(...)`.
- `_emit_writer_response(...)` builds response bytes with `emit_public(envelope, sort_keys=...)`.
- Result: **uses single shared emitter path**.

### 3) `/internal/dev/sampler` (POST)
- Route defined in `adapter/http_reader.py` as `@bp.route("/internal/dev/sampler", methods=["POST"], ...)`.
- Handler `dev_sampler_internal()` returns bytes via `body = emit_public(response_payload, sort_keys=True)`.
- Result: **uses single shared emitter path**.

### 4) Additional bounded conjunction loci (repo-proven, same family)

#### `/dev/sampler/conjunction` (GET)
- Route calls `_emit_conjunction_response()`.
- `_emit_conjunction_response()` returns `body = emit_public(payload, sort_keys=True)`.
- Result: **uses single shared emitter path**.

#### `/dev/reader/conjunction` (GET)
- Route calls `_emit_conjunction_response()`.
- `_emit_conjunction_response()` returns `body = emit_public(payload, sort_keys=True)`.
- Result: **uses single shared emitter path**.

## Conclusion (PR-01 bounded outcome)

All inventoried conjunction JSON-emitting loci in this bounded PR-01 scope route through the single shared canonical emitter (`emit_public` -> `sercanon`).

No in-place emitter fix was needed for the inventoried loci.
