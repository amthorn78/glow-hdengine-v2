# HDE-EPIC021 current-state QA harness

This directory is the governed QA_ROOT for EPIC021. Run the canonical entrypoint
from the repository root under already-closed rails:

```bash
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC APP_ENV=dev \
  python tools/qa/epic021_qa.py
```

The entrypoint validates the supplied rails without modifying them. A successful
transaction publishes one flat, check-keyed `qa_step_logs_manifest.json` whose
current receipts are:

- `checks/d00-bootstrap/primary.log`
- `checks/bootstrap-tooling-classification/primary.log`
- `checks/po-epic021-live-qa/primary.log`
- `checks/po-precommit/primary.log`
- `checks/po-postcommit/primary.log`
- `checks/acceptance-map-viability/primary.log`

`acceptance_map_viability.log` is the governed epic-level viability ledger. The
QA_ROOT-owned binding artifacts are:

- `token_evidence_matrix.md`
- `checks/d00-bootstrap/primary.log`
- `qa_step_logs_manifest.json`
- `acceptance_map_viability.log`

The PF12 evidence graph remains outside QA_ROOT at these exact paths:

- `docs/evidence/INDEX.json`
- `docs/evidence/INDEX.sha256`
- `artifacts/evidence_index.jsonl`

The acceptance map, QA_ROOT artifacts, primary receipts, path proofs, PF12
evidence graph, and orientation receipt are refreshed and verified as one
recoverable transaction.

Historical run-id directories and `step_*` logs remain immutable historical
records. They are not imported into current correctness and are not executable
inputs to this harness.
