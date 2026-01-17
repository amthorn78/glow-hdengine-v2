# QA harness pattern (non-canonical summary)

This note summarizes how epics use the shared QA harness introduced for EPIC021. PF10 — HDE-Build Notes (generic harness addendum) and PF19 — Glow QA Guide govern the authoritative process; this file is a quick reference for future epic authors.

## Define harness configuration

Create a `HarnessConfig` with the epic’s identifiers and file layout, mirroring the EPIC021 setup:

- `epic_id`: the epic label used in logs.
- `qa_root`: QA_ROOT base directory (e.g., `audit/qa/<epic-id>/`).
- `acceptance_map_path`: path to the acceptance map viability log.
- `token_matrix_path`: optional token evidence matrix path.
- `step_names`: ordered step identifiers that drive log naming.

## Provide a wrapper entrypoint

Each epic supplies a thin script (for EPIC021 this is `tools/qa/epic021_qa.py`, for EPIC024 this is `tools/qa/run_hde_epic024_harness.py`) that:

1. Validates closed-rails pins via `engine.runtime.determinism_env.ensure_determinism_env`.
2. Determines the run id (prefer an `EPIC*_QA_RUN_ID` environment override, otherwise fall back to the harness default such as `determine_run_id()`).
3. Invokes the generic harness runner with the configured `HarnessConfig`.

EPIC021 is the first client, and EPIC024 extends the pattern with a single QA root (`audit/qa/hde-epic024/`) that records per-check logs, a token matrix, and an acceptance-map viability gate whose PASS/FAIL_BEHAVIOR status affects the harness exit code. Future epics should adopt the same pattern to keep QA_ROOT layouts, manifests, and viability tracking consistent while leaving epic-specific logic inside the harness configuration.
