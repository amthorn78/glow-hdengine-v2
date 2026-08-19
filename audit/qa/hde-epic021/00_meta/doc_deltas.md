# HDE-EPIC021 Current-State Acceptance Migration — Doc Deltas

This QA slice records later PF-Canon drainage targets only. It does not edit PF-Canon,
move a PF09/PF20 status, claim token satisfaction, or rewrite historical EPIC021 run evidence.

- Normalize `CLI_READER_EMITTER_PARITY_OK` to `CLI_READER_PARITY_OK`, and retire
  `CLI_SERIALIZER_GUARD_OK` while retaining its guard evidence under
  `CLI_NO_ALT_JSON_OK`. (PF04 — HDE Governance, §2.0.)
- Normalize `QA_STEP_LOGS_CONSOLIDATED_OK` to `QA_HARNESS_DISCIPLINE_OK`, and
  retire `SANITY_PIPELINE_LOGGED_OK` while binding its intent through
  `SANITY_PIPELINE_OK` and `QA_HARNESS_DISCIPLINE_OK`. (PF04 — HDE Governance, §2.0.)
- Replace active run identity and `step_*` acceptance mechanics with stable
  `checks/<check_id>/primary.log` receipts, a flat check-keyed manifest, and the
  governed root viability ledger. (PF14 — HDE Mechanics Guide, §1.6.3.)
- Keep only the plan-owned lowercase `d00-bootstrap` receipt in the current
  canonical checks namespace; immutable historical run directories remain unchanged
  and non-gating. (PF14 — HDE Mechanics Guide, §1.6.3.)
- Publish this exact document at both the draft and epic-scoped capture paths.
  (PF06 — Epic Process Guide, §0.5.)
