# Capability Map — DB Bridge Fallback

| Capability | Owning Surface | Description | Evidence Hooks |
| --- | --- | --- | --- |
| Connection-time fallback | Adapter posture scripts, CLI runners | Attempt `DATABASE_URL`, fall back to Postgres-scheme `DB_BRIDGE_URL`, fail with `missing_db_config` when both unusable. | `docs/ADAPTER_DB.md`, `scripts/architecture_capture.sh` logs |
| Deterministic posture envelopes | `env-matrix` snapshots, transport harness | Freeze failure envelopes without DB connectivity; prevent environment drift in captures. | `AGENTS.md` env-matrix rule, `artifacts/db/` proofs |
| Presenter-aligned output | `engine.presenter.emitter`, adapters | Reuse shared emitter for public bytes to maintain canonical LF-terminated JSON. | `engine/presenter/emitter.py`, `VERIFY.sh` |
| Evidence cataloging | Audit snapshots | Store fallback runs with ASCII-sorted, LF-terminated artifacts for reviewers. | `artifacts/evidence_index.jsonl`, `docs/EVIDENCE_INDEX.md` |

Each capability preserves the repo invariants: canonical JSON, deduped set representations, and refusal logging discipline. The fallback surface must never bypass the presenter or alter transport/auth baselines.
