# HDE-EPIC038 OPS-01R Session Action Report

Report date: 2026-07-20 UTC  
Session scope: OPS-01R recovery, direct/bridge parity diagnosis, and PO disposition  
Repository: `amthorn78/glow-hdengine-v2`  
Classification: non-governed OPS action report  
Final technical result: `MIXED_PARITY_AND_POSTURE_FAILURE`  
Candidate eligibility: `NOT_ELIGIBLE`

## Executive result

The session completed one authorized, read-only Codespaces observation pass and identified the exact cause hidden by the runner's earlier generic `OPS01R_LIVE_PARITY_MISMATCH` error.

Direct database and pg-bridge results matched for grants, search path, `SELECT 1`, bounded DDL identity, approved selector identity, and canonical BodyGraph bytes. They differed only on the representation of default privileges:

- Direct database: `default_privileges = ["(none)"]`
- pg-bridge: `default_privileges = null` or the field was omitted and normalized to a missing value

This produced exactly two failed checks:

1. `direct_bridge_default_privileges_match`
2. `bridge_default_privileges_match_expected`

All other 20 required predicates passed. The failure is therefore bridge-side grants-introspection contract/normalization drift, not a database-row, BodyGraph, DDL, search-path, grants-roster, selector, or connectivity divergence.

No v5 candidate was produced. No QA PASS, PF09 status movement, database write, schema mutation, deployment change, or pg-bridge change occurred.

## Product Owner decisions and actions

The Product Owner made the following operating decision after reviewing the diagnostic:

- pg-bridge will be removed rather than repaired.
- Development work requiring database access will be performed within GitHub Codespaces.
- pg-bridge existed to give Codex database access for development work. After its removal, any development work requiring database access must be classified and authorized as an OPS task rather than ordinary development work.

This session records that decision but does not execute the pg-bridge removal. No external service, Railway variable, deployment, or repository implementation was changed to carry it out.

The new operating rule should be reflected in the next authorized governance or operating-document update. This report does not edit PF-Canon.

## Authority and scope

The Product Owner authorized:

- delegated automated OPS execution under PF10 — *HDE Build Notes* v12.3.1, §2.11;
- presence-only use of the Codespaces `DATABASE_URL` and `DB_BRIDGE_URL` values;
- exactly one new direct-and-bridge external observation pass;
- a temporary diagnostic harness;
- secret-free, non-governed diagnostic reports under `audit/ops/hde-epic038/`;
- no retry after external I/O began.

The authorization excluded:

- database writes, grants, migrations, schema changes, and variable changes;
- Railway discovery during the recovery diagnostic;
- deployment, restart, pg-bridge repair, or pg-bridge removal;
- raw credential, request, response, user-row, or BodyGraph persistence;
- QA claims, PF09 status movement, candidate integration, PR-C, and closeout.

## Source and worktree identity

Final session source state:

- Branch: `main`
- HEAD: `b3cf346cc6e84147056f0e4e739b8b2d6917db4f`
- `origin/main`: `cd4a696121e0e66749dcc18b5654ada667066ff5`
- Relationship: local `main` was one commit ahead of `origin/main`
- Worktree before recovery outputs: dirty only because the prior downloadable session report was retained as an untracked file
- Unrelated worktree state was preserved; no reset, checkout, clean, stash, pull, or force operation occurred

Relevant source lineage:

| Commit | Purpose |
|---|---|
| `ffe67e3d2c2831cb42c12dc583340ddde77d0980` | Original PR-A runner/validator source identified at the beginning of OPS-01R |
| `cd4a696121e0e66749dcc18b5654ada667066ff5` | Railway discovery integration correction on `origin/main` |
| `b3cf346cc6e84147056f0e4e739b8b2d6917db4f` | Local discovery diagnostic hardening used by the final session |

The recovery diagnostic is not described as an immutable recapture from `ffe67e3d...`. Its actual runner identity was:

- Runner: `scripts/ops/hde_epic038_ops01r.py`
- Runner SHA-256: `871dc033c35ffd8bb57823e800eb41a1b1dab80d04e83653c0daf0d49432838f`
- Validator SHA-256: `c7b97f75127fd58b95a6a8e9cfe307883c206bcb4abb5b20c7665cbaa36028da`
- DDL projector SHA-256: `72c7c1ce4b49c188769e8c28aa442fb43abe7c0d3432a520c3296c909c2f6fe7`
- Interpreter invoked: `/workspaces/glow-hdengine-v2/.venv/bin/python`
- psycopg version: `3.2.13`

## Infrastructure and canon findings

PF07 — *Glow Infrastructure*, §§2.2, 2.4, 2.6, and 3.1 established:

- provider: Railway;
- project: `ample-illumination`;
- environment: `production`;
- service: `glow-hdengine-v2`;
- database instance: `ample-illumination/production/postgres`;
- schema: `hde`;
- pg-bridge public service endpoint identity, without requiring its value to be retained in this report.

The Product Owner clarified the intended production configuration:

- `DATABASE_URL`: present on production;
- `DB_BRIDGE_URL`: intentionally absent on production;
- production is direct-database-only.

PF07's production environment inventory lists `DATABASE_URL` and omits `DB_BRIDGE_URL`, consistent with that clarification. PF29 — *HDE Users Guide*, §§12.1, 13, and 17 is vendor-configuration oriented and does not establish Railway database/bridge variable injection.

The initial production discovery failure was therefore a procedure/target-model mismatch rather than a missing production credential: the runner required both endpoints to originate from the Railway production service even though production intentionally has no bridge variable.

## Session execution chronology

### 1. Repository validation and source correction

- The repository, branch, commits, runner, validator, projector, and temporary write roots were inspected.
- The original PR-A commit was identified as `ffe67e3d...`.
- Railway CLI integration and bounded discovery diagnostics were corrected in later source states `cd4a6961...` and `b3cf346c...`.
- The active worktree was not discarded or rewritten.

### 2. Detached-source preflight

Final governed staging identity:

- Run ID: `e0b12b4ee37a44a7b798f7cd6c8abccc`
- Detached source root: `/tmp/hde-epic038-ops01r/e0b12b4ee37a44a7b798f7cd6c8abccc/source`
- Source commit: `b3cf346cc6e84147056f0e4e739b8b2d6917db4f`
- Source manifest SHA-256: `f6ac3744b5c99ff85c41bd4a79727513593e4d045165866346dacb5739927234`
- Preflight identity SHA-256: `095b9ab9b2072f4d406048476c900e31c22335a73204686ab219f733130d9de8`
- Detached state: PASS
- Clean source manifest before/after: PASS
- Temporary-only write contract: PASS

The final executed discovery authorization self-hash was:

`27713f571360645b240bb1df940b9e0d769c79e7a4f8bdc443e0a2aded97f8da`

An earlier approved discovery hash, `6db0f2304eea3eea9183ec7b7c0ff8ded694f4309ea15dd52a8c722db9206b6c`, was superseded and was not the final retained discovery contract.

### 3. Railway discovery

The six authorized read-only Railway discovery subprocesses executed using Railway CLI 5.26.2. Project, environment, and service identity resolved. The final target probe was rejected with:

`OPS01R_DISCOVERY_TARGET_AMBIGUOUS:target_identity_probe:endpoint_presence`

Cause: the runner required both `DATABASE_URL` and `DB_BRIDGE_URL` on the production service. Production intentionally provides only the direct database variable.

No live authorization, live-authority marker, v5 candidate, database/provider observation, deployment change, or tracked evidence integration resulted from that production discovery.

### 4. First Codespaces diagnostic attempt

Codespaces endpoint presence was checked by name only:

- `DATABASE_URL`: `PRESENT`
- `DB_BRIDGE_URL`: `PRESENT`

Two harness-readiness failures occurred before external I/O and did not consume a live observation:

1. Dynamic module import setup initially failed before provider construction.
2. `/usr/local/bin/python` could not import `psycopg`; this exposed a preflight defect because the earlier preflight had accepted an interpreter that was not live-runtime ready.

The repository virtual environment was then verified with psycopg 3.2.13. A bounded Codespaces observation reached the runner's final compound comparison and raised `OPS01R_LIVE_PARITY_MISMATCH`. Because that runner version retained no predicate matrix, it established connectivity but did not identify the failed predicate. No candidate or useful failure artifact resulted.

### 5. Recovery diagnostic construction

The Product Owner authorized one new read-only observation pass specifically to bypass the compound assertion and persist all predicate results.

Temporary harness:

`/tmp/hde-epic038-ops01r-diagnostic-02/ops01r_predicate_diagnostic.py`

Harness SHA-256:

`54d83d3812b4c372b464a746ff249a7651361d48adf85878774fc16c527bf8e5`

Before external I/O, static validation confirmed:

- syntax and imports: PASS;
- exact 22-check roster: PASS;
- required summary headings: PASS;
- canonical final-LF behavior: PASS;
- write-capable SQL literals: 0;
- environment enumeration: 0;
- calls to the compound `_capture_live_observations`: 0;
- raw BodyGraph output path: 0;
- output collisions: 0.

The harness reused the current repository implementations for the direct and bridge providers, `DBAccess`, BodyGraph fetcher, posture functions, DDL projection, counted connection, read-only bridge wrapper, no-redirect posture, and exact call budget.

### 6. Single external recovery observation

Exactly one recovery observation pass began and completed. No retry occurred.

Pinned rails:

- `LC_ALL=C`
- `LANG=C`
- `TZ=UTC`
- `SAFE_MODE=1`
- `ALLOW_NETWORK=0`
- `ALLOW_DB_WRITE=0`
- `APP_ENV=dev`

Exact expected and actual call counts were equal:

| Counter | Expected | Actual |
|---|---:|---:|
| `bodygraph_reads` | 2 | 2 |
| `bridge_http_requests` | 6 | 6 |
| `bridge_provider_selections` | 1 | 1 |
| `direct_connection_attempts` | 8 | 8 |
| `direct_provider_selections` | 1 | 1 |
| `direct_sql_statements` | 13 | 13 |
| `fallbacks` | 0 | 0 |
| `logical_observations` | 10 | 10 |
| `retries` | 0 | 0 |
| `vendor_requests` | 0 | 0 |

All direct SQL was guarded as `SELECT` or `SHOW`. Bridge activity was limited to the existing read-only health/introspection routes and `/query` route. Redirects were disabled.

### 7. Output representation correction

The first generated matrix correctly identified the two failed IDs but represented the observed bridge `null` as `not_applicable` because the report builder used Python `None` for both meanings. It also resolved the virtual-environment executable symlink to `/usr/local/bin/python3.11` instead of retaining the invoked lexical interpreter path.

No external observation was repeated. A non-I/O correction repackaged the already retained safe results into the required timestamped sibling directory, as required by the no-overwrite rule.

Correction helper:

`/tmp/hde-epic038-ops01r-diagnostic-02/repackage_diagnostic_outputs.py`

Correction helper SHA-256:

`21d89618bd9ee541d8b1419232a1676401d8585975f93c87e9f5ac9ff404184d`

Additional database or bridge observations during correction: `0`.

The timestamped files are the authoritative handoff. The base files are superseded and must not be used for conclusions.

## Complete predicate matrix

### Connectivity and execution

| Check ID | Status | Safe evidence |
|---|---|---|
| `direct_provider_health` | PASS | psycopg health completed |
| `bridge_provider_health` | PASS | bridge health completed |
| `call_budget_exact` | PASS | every actual count equaled the approved expected count |
| `sql_read_only_guard_held` | PASS | no read-only guard rejection; only `SELECT`/`SHOW` accepted |

### Direct-versus-bridge parity

| Check ID | Status | Direct | Bridge |
|---|---|---|---|
| `direct_bridge_grants_match` | PASS | exact 21-row metadata roster | identical 21-row metadata roster |
| `direct_bridge_default_privileges_match` | **FAIL** | `["(none)"]` | `null`/missing |
| `direct_bridge_search_path_match` | PASS | `hde, public` | `hde, public` |
| `direct_bridge_select_one_match` | PASS | `1` | `1` |
| `direct_bridge_ddl_projection_match` | PASS | SHA-256 `8fea6cb9dee3e1f59df8640091419c1894dade511632b605850507f65386f28b` | same SHA-256 |
| `direct_bridge_user_id_match` | PASS | approved-selector match `true` | direct match `true`; approved-selector match `true` |
| `direct_bridge_bodygraph_canonical_match` | PASS | SHA-256 `aa7ab413031736af578af64fba10cbe61d2b186bea8efd4036661d6476d34f81` | same SHA-256; in-memory equality `true` |

### Expected database posture

| Check ID | Status | Safe observed result |
|---|---|---|
| `direct_grants_match_expected` | PASS | exact approved roster |
| `bridge_grants_match_expected` | PASS | exact approved roster |
| `direct_default_privileges_match_expected` | PASS | `["(none)"]` |
| `bridge_default_privileges_match_expected` | **FAIL** | `null`/missing; expected `["(none)"]` |
| `direct_search_path_match_expected` | PASS | `hde, public` |
| `direct_select_one_match_expected` | PASS | `1` |
| `direct_selector_user_id_match_expected` | PASS | boolean match `true`; no ID retained |
| `direct_partition_lines_match_expected` | PASS | exact two-row plan |
| `direct_partition_observed_match_expected` | PASS | exact two-table roster |
| `direct_boundary_views_match_expected` | PASS | both boundary views reported read-only |
| `direct_unique_constraint_match_expected` | PASS | exact approved BodyGraph uniqueness constraint |

Mechanically derived lists:

- Failed checks: `{direct_bridge_default_privileges_match, bridge_default_privileges_match_expected}`
- Parity failures: `{direct_bridge_default_privileges_match}`
- Expected-posture failures: `{bridge_default_privileges_match_expected}`
- Classification: `MIXED_PARITY_AND_POSTURE_FAILURE`
- Candidate eligibility: `NOT_ELIGIBLE`

## Safe retained database metadata

### Grants roster

Direct and bridge both returned the same approved grants for these objects:

- `hde.body_graphs`
- `hde.body_graphs_current`
- `public.hde_body_graphs_current`

Each object had the same seven privileges:

- `DELETE`
- `INSERT`
- `REFERENCES`
- `SELECT`
- `TRIGGER`
- `TRUNCATE`
- `UPDATE`

Grantee: `postgres`.

### Default privileges

- Approved expectation: `["(none)"]`
- Direct observation: `["(none)"]`
- Bridge observation: `null` or missing

This is the only provider-parity difference.

### Search path and scalar query

- Direct search path: `hde, public`
- Bridge search path: `hde, public`
- Direct `SELECT 1`: `1`
- Bridge `SELECT 1`: `1`

### DDL identity

- Direct projection object count: 3
- Bridge projection object count: 3
- Direct canonical projection SHA-256: `8fea6cb9dee3e1f59df8640091419c1894dade511632b605850507f65386f28b`
- Bridge canonical projection SHA-256: `8fea6cb9dee3e1f59df8640091419c1894dade511632b605850507f65386f28b`
- Structural difference: none

Only the approved identity projection was retained. Raw DDL payload differences outside the bounded projection were not used as parity inputs.

### BodyGraph selector and payload

- Direct result matched the approved selector: `true`
- Bridge result matched direct: `true`
- Bridge result matched the approved selector: `true`
- Direct canonical BodyGraph SHA-256: `aa7ab413031736af578af64fba10cbe61d2b186bea8efd4036661d6476d34f81`
- Bridge canonical BodyGraph SHA-256: `aa7ab413031736af578af64fba10cbe61d2b186bea8efd4036661d6476d34f81`
- In-memory BodyGraph equality: `true`

No selector UUID, BodyGraph object, or raw user row was retained in the diagnostic outputs.

### Partition posture

Expected and observed:

- `hde.pair_evaluation RANGE (evaluated_at)`
- `hde.public_results RANGE (created_at)`

Observed table roster:

- `hde.pair_evaluation`
- `hde.public_results`

### Boundary views

Both expected boundary views matched the read-only posture:

- `hde.body_graphs_current`
- `public.hde_body_graphs_current`

For both views:

- `is_updatable: NO`
- `is_insertable_into: NO`
- `is_trigger_updatable: NO`

### Unique constraint

Observed and expected:

- Name: `body_graphs_user_id_vendor_vendor_version_input_fingerprint_key`
- Definition: `UNIQUE (user_id, vendor, vendor_version, input_fingerprint)`

## Root cause and ownership

The immediate failing surface is pg-bridge grants introspection.

The bridge consumer calls `/introspect/grants` and normalizes the returned object in `engine/db/providers/bridge_provider.py`, lines 200-235. Its grants normalization converts grant rows but does not require or normalize `default_privileges`. Consequently, a deployed bridge response that omits the field or returns `null` passes through as a missing value.

The runner compares both provider results to `["(none)"]` at `scripts/ops/hde_epic038_ops01r.py`, lines 1802-1803. That expectation agrees with the approved EPIC038 remediation CRD v1.3, lines 523-529. The runner expectation is therefore not stale relative to current authority.

If pg-bridge were retained, the correct remediation would be:

1. make the deployed `/introspect/grants` response include truthful `default_privileges` metadata;
2. represent no observed default privileges as `["(none)"]`;
3. harden `BridgeProvider._normalize_introspect` to reject a missing field rather than treating absence as valid parity evidence; and
4. validate only direct and bridge grants introspection in a newly authorized, bounded OPS read.

The Product Owner instead decided to remove pg-bridge. Therefore no bridge repair is requested. The operative follow-up is decommissioning pg-bridge under separately authorized external-change scope and enforcing Codespaces-only database access for development OPS work.

## Candidate and PF09 disposition

- v5 candidate: not produced
- Candidate eligibility: `NOT_ELIGIBLE`
- Reason: one required parity check and one required bridge posture check failed
- QA: not run and not claimed
- PF09 status movement: none
- `HDE-DIST001`: remains `Partial`
- `HDE-DIST001.4`: remains `Partial`
- `HDE-DIST001.9`: remains `Partial`
- PR-C: not executed
- Candidate integration: not executed
- Epic closeout: not claimed

The diagnostic provides actionable evidence for the bridge defect and future operating posture, but it is not a release candidate or acceptance artifact.

## Safety results and nonclaims

Verified safety results:

- External recovery observation passes: `1`
- External observations added by output correction: `0`
- Database writes: `0`
- Repository implementation writes: `0`
- Fallbacks: `0`
- Retries: `0`
- Vendor requests: `0`
- Endpoint retention: names and `PRESENT`/`ABSENT` only
- Secret values persisted: `false`
- Raw request or response bodies persisted: `false`
- Raw user data persisted: `false`
- Raw BodyGraph persisted: `false`
- Raw selector ID persisted in final diagnostic outputs: `false`
- Deployment, restart, Railway mutation, schema change, grant change, and migration: none

The only repository writes from the recovery task were the explicitly authorized non-governed diagnostic reports. No Human Index, Machine Mirror, path proof, manifest, acceptance map, token matrix, PF09, PF10, close pack, or governed hash artifact was updated.

## Evidence ledger

### Authoritative recovery outputs

1. [Predicate matrix](/workspaces/glow-hdengine-v2/audit/ops/hde-epic038/ops-01r-diagnostic-02-20260720t025107z/predicate_matrix.json)  
   SHA-256: `cf6823cba3073839e7a4ceadc7300dd7236414e0e3eb7df33cc60b30a38439d6`

2. [Recovery summary](/workspaces/glow-hdengine-v2/audit/ops/hde-epic038/ops-01r-diagnostic-02-20260720t025107z/session_summary.md)  
   SHA-256 after PO disposition note: `61628d0114e92a6b90efd683ebc32ee72dcf0e75863b9ce03302f31173ccfb36`

### Prior session narrative

3. [Initial session report](/workspaces/glow-hdengine-v2/codex/out/OPS-01R-session-report-2026-07-20.md)  
   SHA-256: `a47f8e991432cf43f18bac963f5b7dd401e7a4636080c659cda799fa52d6b7f1`

### Superseded recovery renderings — do not use for handoff

4. `audit/ops/hde-epic038/ops-01r-diagnostic-02/predicate_matrix.json`  
   SHA-256: `e1296c09b7cfa3eaa3fa36ab564af55f2b8664267c2693e66d80c54f2c34a609`

5. `audit/ops/hde-epic038/ops-01r-diagnostic-02/session_summary.md`  
   SHA-256: `f7392530b0845e609d15e75b777cc4feb76b1a645de53fd63a5cfff2ca4236ec`

These two base files came from the same valid one-pass observation but contain the report-representation issue described above. The timestamped files supersede them.

### Temporary execution helpers

6. `/tmp/hde-epic038-ops01r-diagnostic-02/ops01r_predicate_diagnostic.py`  
   SHA-256: `54d83d3812b4c372b464a746ff249a7651361d48adf85878774fc16c527bf8e5`

7. `/tmp/hde-epic038-ops01r-diagnostic-02/repackage_diagnostic_outputs.py`  
   SHA-256: `21d89618bd9ee541d8b1419232a1676401d8585975f93c87e9f5ac9ff404184d`

Temporary helpers are not governed evidence and may not persist beyond the workspace lifecycle.

## Action register

| Action | Owner | Status | Scope note |
|---|---|---|---|
| Identify exact generic-mismatch predicate | Delegated OPS executor | Completed | One read-only recovery pass |
| Confirm direct/bridge BodyGraph and DDL parity | Delegated OPS executor | Completed | Both passed |
| Confirm bridge default-privilege mismatch | Delegated OPS executor | Completed | Direct `["(none)"]`; bridge `null`/missing |
| Produce downloadable consolidated action report | Delegated OPS executor | Completed | This file |
| Remove pg-bridge | Product Owner / infrastructure owner | Decided; not executed | Requires separate external-change authorization |
| Use Codespaces for development database access | Product Owner / development operators | Directed | Database access remains OPS-scoped |
| Classify all database-access development as OPS | Product Owner / governance owner | Directed; documentation follow-up pending | PF-Canon not edited in this session |
| Run another parity or candidate attempt | Product Owner | Not authorized and not recommended | Candidate remains ineligible; pg-bridge removal supersedes repair path |

## Final conclusion

The process ultimately answered the operational question:

- Connectivity was healthy.
- Direct and bridge data/DDL/BodyGraph parity was healthy except for one metadata field.
- The exact failure was pg-bridge returning a missing or `null` default-privilege value while direct returned `["(none)"]`.
- The approved posture expectation was not stale.
- The v5 candidate remained ineligible.
- The PO chose to retire pg-bridge and make Codespaces the database-access context for OPS-authorized development.

This report is the single-file action handoff for the session. It is non-governed and must not be used as a QA PASS, PF09 status-change artifact, release candidate, or closeout record.

## Authority references

- PF07 — *PF07-Canon-Glow-Infrastructure*, §§2.2, 2.4, 2.6, 3.1
- PF09.6 — *PF09.6-Canon-HDE-Build-Checklist-Distillation*, task `HDE-DIST001`, subtasks `HDE-DIST001.4` and `HDE-DIST001.9`
- PF10 — *HDE Build Notes* v12.3.1, §§2.9 and 2.11
- PF29 — *HDE Users Guide*, §§12.1, 13, 17
- Approved Rescoping CRD HDE-EPIC038 Post-PR359 Remediation v1.3, lines 523-529
