# Reader v1 — Alpha acceptance (summary)

## Purpose
Gate Reader v1 behavior at a high level. Details of A7 transport/caching are defined in Governance & Process (Acceptance). This page summarizes only what to probe.

## Probes (summary)
• 200 OK — strong quoted ETag over identity bytes; body matches CLI; one trailing LF
• HEAD parity — same validators as 200; Content-Length matches identity bytes
• 304 Not Modified — empty body; ETag present; Cache-Control present
• Accept-Encoding invariance — identity vs gzip (br optional)
• Errors & writers — JSON one line + final LF; Cache-Control: no-store

## Evidence pointers
• Headers and parity: tests/test_reader_transport.py
• Byte identity and serializer: tests/test_emitter_determinism.py

<!-- EPIC-004 PATCH: alpha acceptance pointer -->
### Transport validation reference (EPIC-004)
Reader transport is validated per **HTTP Transport Evidence**:
`docs/acceptance/http_transport_evidence.md`
