# CLI & Commands — Compat v1 (Alpha)

> The Compat endpoint is internal (dev). Success = 200 JSON; errors = envelope + `Cache-Control: no-store`. Use **POST** for any JSON payloads.

## Endpoint
- `POST /api/compat/v1` — full payloads or large prefs
- `GET /api/compat/v1?a_id=<ID>&b_id=<ID>` — ids-only (defaults applied); **no JSON body**

## Success (alpha)
- **200 OK**
- **Headers:** `Content-Type: application/json; charset=utf-8`
- **Body (summary):** `{"categories":[{id,score:int,band,personal_key,shared_key}×10],"meta":{"engine_tag","release_id","invocation_tag"}}`
  - Category order is fixed: heat, harmony, communication, alignment, comfort, consistency, expansion, creativity, drive, balance
  - Bands by inclusive maxima; 100 ⇒ Glow; scores are ints (0..100), round-half-up then clamp 0..100

## Errors (alpha)
- **400 Bad Request**
- **Headers:** `Cache-Control: no-store` (no ETag)
- **Envelope:** `{"ok":false,"code":"lower_snake","error":"human_readable"}`
  - `invalid_json` — malformed or mixed id/payload
  - `invalid_prefs` — `viewer_prefs.weights` must include all 10 categories as integers 0..100

## CLI parity
- CLI MUST emit **identical bytes** to service (single emitter/serializer path).
- Recommended hook for parity testing: env `HDE_CLI_SHOWCOMPAT` shelling `hdctl showcompat`.

