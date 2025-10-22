# Public emitter guardrails

## Guardrails for public emitters
• Use a single emitter for CLI and Reader; no duplicate serialization paths.
• Do not use ad-hoc json.dumps on public surfaces — use the canonical serializer.
• ETag must hash the identity bytes (pre-compression) and include the single trailing LF.
• Accept-Encoding invariance: identity vs gzip produce the same ETag; brotli optional.
• Public JSON is numeric-free; envelope keys are stable and Spec-defined.
