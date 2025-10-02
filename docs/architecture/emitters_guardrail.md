# Emitters — Single-emitter guardrail (normative)

## Purpose
Prevent serializer drift: the CLI and Reader MUST produce byte-identical public outputs by importing a single canonical emitter.

## Requirement (MUST)
- The public emitter entrypoint is `engine/emit_public.py`. CLI (`scripts/hdctl.py`) and Reader (`server/app.py` handler`) MUST import and call this emitter instead of re-serializing in-place.

## Example import pattern (Python)
```py
# canonical usage (example)
from engine.emit_public import emit_public_bytes
# emit_public_bytes returns bytes: UTF-8, sorted keys, separators(',',':'), ensure_ascii=False, trailing '\n'
body_bytes = emit_public_bytes(a_path, b_path, opts)
return Response(body_bytes, content_type="application/json; charset=utf-8")