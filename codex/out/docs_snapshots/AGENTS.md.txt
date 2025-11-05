# AGENTS.md — Glow HD Engine (agent rules)

## Repository scope & invariants
- Public Reader v1 responses stay bands-only (numeric-free); see docs/server/reader_v1.md **(dev harness; deprecated)** if present.
- Emit public success bytes through engine.presenter.emitter.emit_public to share the canonical presenter/emitter path.
- Canonical JSON is UTF-8, sort_keys=True, compact separators (",",":"), with exactly one trailing LF per engine/serializer/canon.py.
- Treat arrays-as-sets by deduping and ASCII-sorting (engine/mech/helpers.py); normalize channel ids to NN-NN with the lower value first (engine/mech/compare.py).

## Environment & configuration
- Smoke base URL variable: HDE_BASE_URL (dev default: http://127.0.0.1:5000 in scripts/architecture_capture.sh). **Set explicitly for staging/prod.**

## Service entrypoints & commands
- Local adapter server: python -m adapter.http_reader (dev runner in adapter/http_reader.py).
- CLI setup and help: python -m pip -q install -e ., then hdctl --help and python -m engine.cli --help (pyproject.toml exposes hdctl via engine.cli.main:cli).
- python -m engine.cli --help must exit 0 (parity with hdctl --help).

## QA / acceptance (repo-only)
- /internal/version must serve GET and HEAD as application/json; charset=utf-8 with Cache-Control: no-store, no ETag, HEAD Content-Length equal to the GET body, and conditional GET remaining 200 (adapter/http_reader.py; tests/transport/test_internal_version_contract.py; artifacts/proofs/internal_version_headers.json).
- CLI `showcompat` must emit non-empty canonical JSON (one LF) and pass two-run identity and AB↔BA parity on a fabricated pair.
- A7 JSON success check: **Dev harness example (APP_ENV=dev)** GET "${HDE_BASE_URL:-http://127.0.0.1:5000}/api/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=Africa/Cairo&b_tz=Africa/Cairo" expecting Content-Type application/json (from VERIFY.sh). For staging/production, use a cataloged JSON success endpoint if present; otherwise record a documentation gap and skip A7.

## Evidence & artifact paths
- Machine mirror index: audit/EVIDENCE_INDEX.jsonl (one JSON object per line with keys path, bytes, sha256, added_in).
- Proof artifacts live under artifacts/proofs/; QA captures under artifacts/qa/.

## Do / Don’t
- Do use engine.presenter.emitter for public bytes, keep JSON canonical and LF-terminated, dedupe+sort arrays-as-sets, and normalize channel ids to NN-NN.
- Don’t add new env vars, bypass the shared emitter, alter transport rules, or stash specs in Build Notes.

Referenced repo paths
- docs/server/reader_v1.md
- engine/presenter/emitter.py
- engine/serializer/canon.py
- engine/mech/helpers.py
- engine/mech/compare.py
- scripts/architecture_capture.sh
- VERIFY.sh
- adapter/http_reader.py
- pyproject.toml
- tests/transport/test_internal_version_contract.py
- artifacts/proofs/internal_version_headers.json
- audit/EVIDENCE_INDEX.jsonl
- artifacts/proofs/
- artifacts/qa/
