# Dev sampler HTTP Live QA discovery (EPIC019 D3)

- **Evidence Index**: `docs/evidence/INDEX.json` currently lists sampler evidence families limited to ABBA/seed/two-run/diversity snapshots (e.g., `sampler_abba_logs`, `sampler_pool_snapshots`, `sampler_two_run_logs`) with no dev HTTP harness entries.
- **Acceptance map (EPIC019)**: `docs/acceptance_map_epic019.json` has the D3 foundation marked done with tokens `QA_POSTCOMMIT_CHECKLIST_OK`, `SANITY_PIPELINE_OK`, and `DETERMINISM_ENV_PINS_OK`; none of the tokens reference dev sampler HTTP artifacts or harness tests.
- **EPIC019 manifest**: `audit/EPIC019_MANIFEST.json` binds tokens to sanity/determinism/core artifacts only; no dev sampler HTTP evidence or harness references are present.
- **Existing sampler HTTP QA assets**: repository search finds no scripts or audit logs under `audit/qa/hde-epic019` that exercise `/internal/dev/sampler` under closed rails; prior logs in `audit/qa/hde-epic019/live-qa-20251130/` are general sampler runs rather than the new Live QA harness.
- **Canonical start helper**: `scripts/dev_start_reader.sh` sets closed-rails pins (SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL/LANG=C, TZ=UTC) and runs `python -m adapter.http_reader` on port 8000 by default.
