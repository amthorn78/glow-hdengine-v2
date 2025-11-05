# Writer Request Validation (EPIC-008)

- Require `Content-Type: application/json; charset=utf-8` (diagnostic empty-body exempt)
- 415 invalid content type
- 400 invalid JSON/UTF-8/BOM
- 422 unknown_key / invalid_input
- Size cap: 32 768 bytes pre-parse (413)
