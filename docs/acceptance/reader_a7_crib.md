# Reader v1 — A7 crib sheet (dev)

Dev runner (APP_ENV=dev):
  python dev/reader_harness/app.py

Probes (use curl):
1) 200 OK: strong quoted ETag over identity bytes (with the trailing LF). Body matches CLI.
2) HEAD parity: same validators as 200; Content-Length equals identity bytes.
3) Conditional GET: After a 200, repeat with If-None-Match → expect 304 with empty body; ETag present; Cache-Control present.
4) Accept-Encoding: identity vs gzip produce same ETag (brotli optional; if unavailable, skip).
5) Errors/writers: JSON one line + final LF; Cache-Control: no-store.

For full acceptance details, see “Governance & Process (Acceptance)”.
