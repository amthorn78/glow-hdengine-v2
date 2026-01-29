# Reader v1 — HTTP Transport Evidence crib sheet (dev)

Dev runner (APP_ENV=dev):
  python dev/reader_harness/app.py

Probes (use curl):
1) 200 OK: strong quoted ETag over identity bytes (with the trailing LF). Body matches CLI `--dump-reader` bytes.
2) HEAD parity: same validators as 200; **Content-Type equals GET**; Content-Length equals identity bytes.
3) Conditional GET: After a 200, repeat with If-None-Match → expect 304 with empty body; ETag present; Cache-Control present.
4) Accept-Encoding: identity vs gzip produce same ETag (brotli optional; if unavailable, skip).
5) Errors/writers: JSON one line + final LF; Cache-Control: no-store.

Proof artifacts (optional): set `HDE_WRITE_A7_PROOFS=1` when running `tests/http/test_reader_a7_transport.py` to emit proof files under `artifacts/proofs/`:
- `success_get.txt`, `success_head.txt`, `success_304.txt`
- `encoding_invariance.txt`
- `success_writers_errors.txt`
- `endpoints_env_gate_proof.log`

For full acceptance details, see “Governance & Process (Acceptance)”.
