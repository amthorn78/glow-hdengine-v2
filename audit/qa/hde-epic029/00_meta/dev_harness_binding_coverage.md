# HDE-EPIC029 Dev Harness Binding Coverage

## OPS-01 single-source disposition
- Source of truth: `audit/ops/hde-epic029/ops-01/binding_disposition.md`.
- Codespaces remains **not yet closed** because accepted remediation evidence recorded `gating_discrepancy observed (APP_ENV=prod did not return 403)`.
- Local dev remains **not yet closed**; PF07 publishes `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler`, but OPS disposition recorded step-creation and AI-data-indexing failure.
- Therefore `HDE_CONJ001_4_DEV_HARNESS_CLOSURE_OK` remains `token_incomplete` in this close-pack.

## OPS-01 files bound by this PR
- `audit/ops/hde-epic029/ops-01/commands.txt`
- `audit/ops/hde-epic029/ops-01/stdout.log`
- `audit/ops/hde-epic029/ops-01/stderr.log`
- `audit/ops/hde-epic029/ops-01/exit_codes.txt`
- `audit/ops/hde-epic029/ops-01/codespaces_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/local_dev_sampler_url.md`
- `audit/ops/hde-epic029/ops-01/binding_disposition.md`
- `audit/ops/hde-epic029/ops-01/created_files_sha256.txt`

## Epic-close Live QA outputs disposition
- `audit/qa/hde-epic029/checks/po-epic-close-live-qa/primary.log`: missing (deferred; no synthetic PASS claim).
- `audit/qa/hde-epic029/checks/po-precommit/primary.log`: missing (deferred; no synthetic PASS claim).
- `audit/qa/hde-epic029/checks/po-postcommit/primary.log`: missing (deferred; no synthetic PASS claim).
