# Emitters

## Categories (public, Reader v1)
• Exactly one category object: {"id":"harmony","band":"Cool|Open|Warm|Glow"}
• Top-level keys: ["categories","eligible","idempotence_hash","meta","release_id"]
(See the Spec for complete constraints. Do not restate them here.)

<!-- EPIC-004 PATCH: single emitter+serializer -->
## EPIC-004 — Single-source public JSON
- **Emitter**: `engine/presenter/emitter.py`
- **Serializer**: `engine/serializer/canon.py:sercanon(obj)->bytes`
- All public responses (Reader success & error, CLI) use **emitter → serializer**; no ad-hoc JSON in public paths.
- Serializer rules: UTF-8, `ensure_ascii=false`, sorted keys, compact separators, **exactly one trailing LF**.

<!-- EPIC-004 single-source -->
## EPIC-004 — Single-source public JSON
- **Emitter**: `engine/presenter/emitter.py`
- **Serializer**: `engine/serializer/canon.py:sercanon(obj)->bytes`
- All public responses (Reader success & error, CLI) must use **emitter → serializer**; no ad-hoc JSON in public paths.
- Serializer rules: UTF-8, `ensure_ascii=false`, sorted keys, compact separators, **exactly one trailing LF**.
