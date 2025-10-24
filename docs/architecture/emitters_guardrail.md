# Public emitter guardrails

## Guardrails for public emitters
• Use a single emitter for CLI and Reader; no duplicate serialization paths.
• Do not use ad-hoc json.dumps on public surfaces — use the canonical serializer.
• ETag must hash the identity bytes (pre-compression) and include the single trailing LF.
• Accept-Encoding invariance: identity vs gzip produce the same ETag; brotli optional.
• Public JSON is numeric-free; envelope keys are stable and Spec-defined.

<!-- EPIC-004 PATCH: forbidden serializers guard -->
## EPIC-004 — Forbidden in public response paths
Fail acceptance if any of these appear in Reader/CLI response code:
```
json.dumps(
jsonify(
orjson
ujson
simplejson
```
Allowed only in tests/tools/logging; public bytes must flow via **emitter → serializer.canon.sercanon**.

<!-- EPIC-004 guard -->
## EPIC-004 — Forbidden in public response paths
Fail acceptance if any of these appear in Reader/CLI response code:
```
json.dumps(
jsonify(
orjson
ujson
simplejson
```
Allowed only in tests/tools/logging; public bytes must flow via **emitter → serializer.canon.sercanon**.
