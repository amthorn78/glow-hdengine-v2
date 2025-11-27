# CLI commands — Compat v1 (EPIC018)

The CLI shares the canonical emitter and serializer with the Reader harness. Run all commands under closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`), enforced by `engine.runtime.determinism_env.ensure_determinism_env`.

## Usage
- `hdctl showcompat --pair-file <pair.json>`
- `hdctl showcompat --a-file <A.json> --b-file <B.json>`
- `hdctl showcompat` (reads one pair from stdin)
- Flags for QA sidecars: `--dump-reader <out.json> --dump-admin-dir <dir>`

Exit codes: 0 success, 64 usage error, 2 typed failure. Errors print to stderr only. CLI output is numeric-free, canonical JSON (UTF-8, sorted keys, compact separators, one trailing LF) and matches Reader bytes (AB↔BA identity, two-run identity).

## Guards (D3)
- Serializer grep guard: `python tools/cli/serializer_grep_guard.py` → `artifacts/cli/guards/serializer_grep_guard.log`
- Emitter symbol proof: `python tools/cli/emitter_symbol_proof.py` → `artifacts/cli/guards/emitter_symbol_proof.txt`
Both guards fail fast if determinism rails are not pinned.

## Evidence discipline (D4)
- Guard outputs, QA dumps, and other governed artifacts must have `.path_proof.txt` siblings plus entries in `docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl`. Use `python tools/evidence/update_evidence_index.py` to refresh.
- Orientation and sanity checks: `python tools/evidence/orientation_demo.py` and `python tools/evidence/run_sanity_pipeline.py`.

See PF05 — CLI/API/Vendor Ref and PF12 — Schemas & Artifacts for canonical rules (title references only).
