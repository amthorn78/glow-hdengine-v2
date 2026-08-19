# HDE-EPIC021 Current-State Acceptance Migration — Doc Deltas

This QA slice records later PF-Canon drainage targets only. It does not edit PF-Canon,
move a PF09/PF20 status, or rewrite historical EPIC021 evidence.

- Normalize `CLI_READER_EMITTER_PARITY_OK` to `CLI_READER_PARITY_OK`.
- Retire `CLI_SERIALIZER_GUARD_OK`; retain its guard evidence under `CLI_NO_ALT_JSON_OK`.
- Normalize `QA_STEP_LOGS_CONSOLIDATED_OK` to `QA_HARNESS_DISCIPLINE_OK`.
- Retire `SANITY_PIPELINE_LOGGED_OK`; bind its intent through `SANITY_PIPELINE_OK`
  and `QA_HARNESS_DISCIPLINE_OK`.
- Replace run-id and `step_*` acceptance mechanics with stable
  `checks/<check_id>/primary.log` receipts, a flat check-keyed manifest, and the
  governed root viability ledger.
- Supersede the nonconforming uppercase `D00_bootstrap` current binding with
  the plan-owned `d00-bootstrap` check. Preserve the former receipt and proof
  as unindexed historical evidence rather than a second current authority.

The historical run directories remain unchanged and non-gating.
