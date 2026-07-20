# OPS-01R Recovery Diagnostic Summary

## Result

Classification: **MIXED_PARITY_AND_POSTURE_FAILURE**.

External observation passes: `1`.

## Exact Failed Predicates

- `direct_bridge_default_privileges_match` — **FAIL** — `{"reason":"default_privilege_metadata_differs"}` — locus `scripts/ops/hde_epic038_ops01r.py:1803`
- `bridge_default_privileges_match_expected` — **FAIL** — `{"reason":"bridge_default_privileges_differ_from_expected"}` — locus `scripts/ops/hde_epic038_ops01r.py:1803`

## Direct-vs-Bridge Conclusion

Direct and bridge did not match on every required parity predicate. Failed parity IDs: `direct_bridge_default_privileges_match`.

## Expected-Posture Conclusion

One or more observations differed from the runner's hard-coded posture. Failed posture IDs: `bridge_default_privileges_match_expected`.

## Candidate Eligibility

**NOT_ELIGIBLE**. A v5 candidate is presently not eligible.

## Required Correction

Correct only the failing provider surface shown above. Grants, default privileges, search path, or DDL mismatches belong first to the pg-bridge introspection/normalization owner; selector or BodyGraph mismatches belong first to the bridge `/query` result-normalization/target-identity owner. The smallest next validation is a newly authorized read of only the failing surface against the same Codespaces endpoints; unrelated Railway discovery is not required. External state was not repaired in this task.

## Safety and Nonclaims

- Database writes: `0`.
- Repository implementation writes: `0`.
- Secret values persisted: `false`.
- Raw user data persisted: `false`.
- Raw BodyGraph persisted: `false`.
- No QA PASS, PF09 status movement, candidate integration, deployment, Railway mutation, schema change, grant change, migration, or closeout is claimed.

## Source and Output Identities

- Repository HEAD: `b3cf346cc6e84147056f0e4e739b8b2d6917db4f`.
- Branch: `main`.
- Worktree state before diagnostic outputs: `DIRTY`.
- Runner SHA-256: `871dc033c35ffd8bb57823e800eb41a1b1dab80d04e83653c0daf0d49432838f`.
- Interpreter: `/usr/local/bin/python3.11`.
- psycopg: `3.2.13`.
- Predicate matrix: `/workspaces/glow-hdengine-v2/audit/ops/hde-epic038/ops-01r-diagnostic-02/predicate_matrix.json`.
- Predicate matrix SHA-256: `e1296c09b7cfa3eaa3fa36ab564af55f2b8664267c2693e66d80c54f2c34a609`.
- Session summary: `/workspaces/glow-hdengine-v2/audit/ops/hde-epic038/ops-01r-diagnostic-02/session_summary.md`.
