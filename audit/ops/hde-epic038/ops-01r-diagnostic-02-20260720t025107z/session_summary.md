# OPS-01R Recovery Diagnostic Summary

## Result

Classification: **MIXED_PARITY_AND_POSTURE_FAILURE**.

The single authorized external observation pass completed. Twenty of the twenty-two required predicates passed. Two failed.

This timestamped report supersedes the base diagnostic report for handoff. It corrects only report representation from already retained safe metadata; it performed `0` additional database or bridge observations.

## Exact Failed Predicates

- `direct_bridge_default_privileges_match` — **FAIL**. Direct returned `["(none)"]`; bridge returned `null`. The current runner checks this surface at `scripts/ops/hde_epic038_ops01r.py:1802-1803`.
- `bridge_default_privileges_match_expected` — **FAIL**. Expected `["(none)"]`; bridge returned `null`. The direct expected-posture check passed.

## Direct-vs-Bridge Conclusion

Direct and bridge matched on grants, search path, `SELECT 1`, the bounded DDL identity projection, selector identity, and canonical BodyGraph bytes. They did **not** fully match because the bridge grants-introspection result omitted or returned `null` for `default_privileges`, while direct returned `["(none)"]`.

The canonical BodyGraph SHA-256 was identical on both sides: `aa7ab413031736af578af64fba10cbe61d2b186bea8efd4036661d6476d34f81`. The DDL projection SHA-256 was also identical: `8fea6cb9dee3e1f59df8640091419c1894dade511632b605850507f65386f28b`.

## Expected-Posture Conclusion

This is not a case where both providers agree but differ from a stale runner expectation. Direct matched every expected-posture predicate. Bridge matched the expected grants roster but failed only the explicit default-privilege representation. The approved EPIC038 remediation CRD v1.3, lines 523-529, agrees with the runner that no default privileges must be observed, so the acceptance expectation itself is not stale.

## Candidate Eligibility

**NOT_ELIGIBLE**. A required provider-parity predicate and a required bridge expected-posture predicate failed.

## Required Correction

The next correction belongs to the pg-bridge grants-introspection response contract, not to production Railway configuration and not to the database schema. The deployed `/introspect/grants` response must include truthful `default_privileges` metadata and represent no observed rows as `["(none)"]`, matching direct introspection and the approved CRD.

The local bridge consumer currently passes missing grants fields through at `engine/db/providers/bridge_provider.py:218-235`; it should be hardened to reject a missing `default_privileges` field rather than silently treating absence as valid evidence. The runner expectations at `scripts/ops/hde_epic038_ops01r.py:1802-1803` should remain unchanged unless the PO separately changes the approved CRD/PF authority.

The smallest next validation is one newly authorized read of only the bridge `/introspect/grants` surface plus the direct grants-introspection surface. Railway discovery, BodyGraph reads, DDL reads, and unrelated posture checks do not need to be repeated to validate this correction.

PO disposition: pg-bridge will be removed rather than repaired. Development work requiring database access will be performed within Codespaces. Because pg-bridge was created to provide Codex with database access for development work, its removal establishes that any development work requiring database access must be classified and authorized as an OPS task rather than ordinary development work.

## Safety and Nonclaims

- External observation passes: `1`; correction-pass observations: `0`.
- Exact call budget held: 8 direct connections, 13 direct read-only SQL statements, 6 bridge HTTP requests, 10 logical observations, and 2 BodyGraph reads.
- Database writes: `0`.
- Repository implementation writes: `0`.
- Secret values persisted: `false`.
- Raw user data persisted: `false`.
- Raw BodyGraph persisted: `false`.
- No QA PASS, PF09 status movement, candidate integration, deployment, Railway mutation, schema change, grant change, migration, or closeout is claimed.

## Source and Output Identities

- Repository HEAD: `b3cf346cc6e84147056f0e4e739b8b2d6917db4f`.
- Branch: `main`.
- Worktree state before diagnostic outputs: `DIRTY` due to the retained untracked prior session report; unrelated state was preserved.
- Runner SHA-256: `871dc033c35ffd8bb57823e800eb41a1b1dab80d04e83653c0daf0d49432838f`.
- Interpreter: `/workspaces/glow-hdengine-v2/.venv/bin/python`.
- psycopg: `3.2.13`.
- Predicate matrix: `/workspaces/glow-hdengine-v2/audit/ops/hde-epic038/ops-01r-diagnostic-02-20260720t025107z/predicate_matrix.json`.
- Predicate matrix SHA-256: `cf6823cba3073839e7a4ceadc7300dd7236414e0e3eb7df33cc60b30a38439d6`.
- Session summary: `/workspaces/glow-hdengine-v2/audit/ops/hde-epic038/ops-01r-diagnostic-02-20260720t025107z/session_summary.md`.
