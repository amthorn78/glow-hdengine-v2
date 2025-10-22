# CLI commands

## 1. Purpose
Document CLI usage for Reader v1. Public body examples live in the Spec; transport/caching acceptance lives in Governance. This page does not restate those rules.

## Reader Output (v1)
The CLI emits the exact same bytes as Reader v1 (public surface is numeric-free).

Example body (compact JSON; one trailing LF implied):
{"categories":[{"id":"harmony","band":"Open"}],"eligible":true,"idempotence_hash":"<64hex>","meta":{},"release_id":"<64hex>"}

## Transport & caching (delegated)
Transport/caching acceptance (ETag, 304, HEAD/GET parity, Vary, no-store for errors/writers) is defined in Governance & Process (Acceptance). Do not restate it here.

## Evidence pointers (tests)
• CLI acceptance and parity tests: tests/cli/*
• Serializer/parity: tests/test_emitter_determinism.py, tests/test_reader_transport.py
