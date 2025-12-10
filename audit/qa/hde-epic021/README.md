# HDE-EPIC021 QA harness usage (QA_ROOT discipline)

This directory is the QA_ROOT home for EPIC021 calcination QA runs. All runs must execute under closed rails using the determinism pins enforced by the harness: `SAFE_MODE`, `ALLOW_NETWORK`, `LC_ALL`, `LANG`, and `TZ`. Live QA operators should run the harness via the entrypoint and provide a deterministic run id.

## Live QA command (closed rails)

Run the harness with explicit pins and a Live QA run id:

```bash
SAFE_MODE=1 \
ALLOW_NETWORK=0 \
LC_ALL=C \
LANG=C \
TZ=UTC \
EPIC021_QA_RUN_ID=live-qa-1 \
python tools/qa/epic021_qa.py
```

- `EPIC021_QA_RUN_ID` should be set to a Live QA identifier such as `live-qa-1`, `live-qa-2`, etc.
- CI uses a separate namespace (for example, `ci-selftest-epic021`) to keep Live QA evidence distinct. CI runs are not part of Live QA acceptance.

## Expected artifacts for a successful run

After a successful Live QA run, QA_ROOT contains the following under `audit/qa/hde-epic021/<run-id>/`:

- `D0_bootstrap.log` with environment summary and harness bootstrap details.
- Per-step logs (`step_bootstrap.log`, `step_serializer_cli_d1.log`, `step_evidence_d2.log`, `step_sanity_d2.log`, `step_acceptance_map_d3.log`).
- `qa_step_logs_manifest.json` updated with one entry for `<run-id>` containing all PASS statuses and log paths.
- `acceptance_map_viability.log` updated to reflect the run.

QA_ROOT is a layout discipline for QA evidence; PF-Canon governs formal evidence catalog paths.
