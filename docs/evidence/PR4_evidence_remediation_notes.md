# PR4 evidence remediation notes (WS-D4)

- `update_evidence_index.py --check` could report `STALE` for the machine mirror because the mirror was rendered twice with different defaults (proof-driven produced_at vs freshly computed), causing hash/size drift between write and check runs.
- `_render_mirror` now derives the self-record only from the rendered body and uses a single `produced_at_utc` baseline, making write + `--check` idempotent when artifacts are unchanged.
- Path-proof writes remain centralized with stable `{path,size_bytes,sha256,mtime_utc,produced_at_utc}` blocks to keep mirror entries, proofs, and on-disk bytes aligned across runs.
- Regenerated all governed path-proofs so `mtime_utc` reflects the current artifact stat timestamps and re-indexed `engine.order.abba_identity.bytes` from the canonical generator, eliminating the prior SHA/SIZE drift reported by CI.
