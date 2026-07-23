# HDE-EPIC038 OPS-03 discovery findings

## Summary

The direct read-only posture capture passed after explicitly provisioning and verifying the two authorized target roles. The most important discovery is that the live database already contained two legacy HDE-named roles, `hde_owner` and `hde_rw`, even though PF10 — HDE Build Notes, §2.18 stated categorically that no Glow/HDE database roles existed.

The supported narrower statement is:

> Before this task, neither dedicated OPS-03 target role (`hde_reader` or `hde_ops03_reader`) existed.

The two legacy roles were recorded, assessed as unsuitable for the OPS-03 contract, and left unchanged under explicit Product Owner direction.

## Finding F-01 — PF10 role-existence statement conflicts with live state

**Classification:** current external-state conflict  
**Strength:** sealed D2 evidence plus PO direction  
**Disposition:** recorded; no PF-Canon edit made

D2 records these non-system roles before target-role provisioning:

| Role | Login | Superuser | Create DB | Create role | Replication | Bypass RLS |
|---|---|---|---|---|---|---|
| `hde_owner` | false | false | false | false | false | false |
| `hde_rw` | false | false | false | false | false | false |

D2 also records that `hde_reader` and `hde_ops03_reader` were absent.

This conflicts with the blanket statement in PF10 — HDE Build Notes, §2.18 that no Glow/HDE database roles exist and that no project-created owner or service role has been defined, provisioned, granted, or verified.

The live finding does not establish when, how, or by whom the legacy roles were created. It proves only their observed presence and the flags shown above. The task made no PF-Canon change.

## Finding F-02 — repository history already named both legacy roles

**Classification:** historical repository evidence  
**Strength:** tracked historical artifacts; not a substitute for current live inspection  
**Disposition:** retained as provenance context

Existing tracked artifacts already reference `hde_owner` and `hde_rw`:

- `artifacts/db/discovery_report.md`
- `audit/ASSESSMENT_part1.md`
- `artifacts/db_discovery/20251113/00_schemas_and_search_path.txt`
- `artifacts/db_discovery/20251113/postgres_schema_only.sql`
- `audit/db_plan/REPORT.md`

The historical schema-only dump records:

- `GRANT USAGE ON SCHEMA hde TO hde_rw`;
- `SELECT, INSERT` on `hde.chart_snapshot`;
- `SELECT` on `hde.meta`;
- `SELECT, INSERT` on `hde.pair_evaluation`;
- `SELECT, INSERT` on `hde.public_results`.

These files show that the role names and an older privilege posture were already known to the repository. They do not prove the complete current privilege graph and must not replace D2 or a current live privilege inspection.

No tracked `CREATE ROLE`, `ALTER ROLE`, role-membership lifecycle, credential-rotation record, or current canonical owner for these legacy roles was found in the scoped inspection.

## Finding F-03 — neither legacy role satisfied the OPS-03 contract

**Classification:** live privilege suitability  
**Strength:** operator-session read-only diagnostic; D2 independently proves only role presence and cluster flags  
**Disposition:** both roles left untouched

The bounded diagnostic found:

- `hde_owner` lacked the required `hde` access and read coverage.
- `hde_rw` had write-capable relation privileges, including `INSERT` on named HDE relations.
- `hde_rw` lacked required current coverage for `hde.body_graphs` and both boundary views.

Accordingly:

- `hde_owner` could not satisfy the metadata-visibility requirements.
- `hde_rw` could not satisfy `relation_write=false`.
- Neither role was a valid substitute for the dedicated OPS-03 login.

Because the detailed diagnostic was not separately sealed, these particulars are reported as operator-session findings. The definitive sealed facts are the D2 role roster/flags and the successful D4 verification of the newly provisioned login.

## Finding F-04 — target-role provisioning reached the required minimum posture

**Classification:** current external-state result  
**Strength:** sealed D3, D4, and D7 evidence  
**Disposition:** retained

The final role model is:

| Role | Final login state | Membership | Purpose |
|---|---|---|---|
| `hde_reader` | `NOLOGIN` | Capability role | Read-only schema/table/sequence capability |
| `hde_ops03_reader` | `NOLOGIN`; password cleared after capture | Member of `hde_reader` | Task-specific OPS-03 principal retained without standing login |

D4 proves all seven merged runner flags false:

- `rolsuper`;
- `rolcreatedb`;
- `rolcreaterole`;
- `rolreplication`;
- `rolbypassrls`;
- `schema_create`;
- `relation_write`.

D4 also proves the required BodyGraph columns, constraints, boundary views, and partition metadata were visible. D7 proves final login-disabled/password-cleared posture and retained membership.

This is sufficient for the bounded OPS-03 role prerequisite. It is not a general database-role architecture.

## Finding F-05 — preflight object and PUBLIC-privilege posture passed

**Classification:** live preflight  
**Strength:** sealed D2 evidence  
**Disposition:** satisfied for this task

D2 established:

- schemas `hde` and `public` present;
- `hde.body_graphs` present;
- `hde.body_graphs_current` present;
- `public.hde_body_graphs_current` present;
- `hde.pair_evaluation` present;
- `hde.public_results` present;
- no result from the bounded query for a non-`USAGE` schema privilege granted to `PUBLIC`;
- no result from the bounded query for a non-`SELECT` table privilege granted to `PUBLIC`.

The finding is limited to the exact preflight queries. It is not a complete database security audit.

## Finding F-06 — the instructed S4 URI transport form was not portable to the installed client

**Classification:** operator-procedure defect  
**Strength:** operator-session observation  
**Disposition:** recovered without weakening the database predicate

The task placed the full PostgreSQL URI in `PGDATABASE`. PostgreSQL client 17 treated it as a database name in this environment and attempted the default local socket instead of establishing the intended remote connection.

The failure occurred before the reader connection. The operator immediately executed the prescribed complete role rollback, then re-provisioned with a new password. On the successful sequence, the URI was decomposed in memory into standard libpq connection fields. No secret was placed in a command argument or evidence file.

This was a client-invocation correction only. The D4 queries, expected values, role flags, metadata checks, and rollback semantics were unchanged.

## Finding F-07 — source cleanliness required an external pristine clone

**Classification:** local execution-environment issue  
**Strength:** operator-session observation and final source checks  
**Disposition:** recovered without source-tree mutation

The shared checkout was at the required commit and Git-clean, but ignored Python bytecode caused the stricter S1 source gate to stop. The operator used an external pristine clone at the exact commit and an external isolated interpreter instead of deleting user files or installing into the repository.

The bound clone remained Git-clean and bytecode-free through capture. This demonstrates that Git cleanliness alone was insufficient for the OPS-03 source-manifest gate.

## Finding F-08 — Railway control-plane DNS was unavailable during mandatory cleanup

**Classification:** external control-plane incident  
**Strength:** operator-session observation; sealed D7 proves final result  
**Disposition:** mandatory cleanup completed

Two Railway connection attempts failed at DNS resolution during S8. The OPS-03 capture was not retried.

The operator used secured administrative PostgreSQL connection data in memory to run only the prescribed login-disable/password-clear operation and verification. D7 proves that cleanup completed. No evidence supports a broader Railway outage conclusion.

## Finding F-09 — capture packet proves the bounded direct/read-only posture

**Classification:** sealed OPS evidence  
**Strength:** canonical candidate, independent receipt, checksums, and terminal control  
**Disposition:** PASS for the packet's exact claims

The packet proves:

- provider `psycopg`;
- one provider selection;
- two direct connections;
- one health statement;
- one read-only posture transaction;
- ten posture statements;
- eleven SQL statements total;
- zero SQL writes;
- zero retries;
- zero alternate-provider attempts;
- exact `hde, public` search path;
- least-privilege runtime flags;
- DDL identity projection valid;
- constraints, boundary views, and partition posture observed;
- secret values absent.

The packet does not prove Railway inventory, database writes, retired transport availability, application behavior, or a complete security review.

## Finding F-10 — tracked placement is intentionally split

**Classification:** repository contract constraint  
**Strength:** current repository validator and approved OPS-03 packet contract  
**Disposition:** canonical root preserved

`tools/evidence/run_sanity_pipeline.py` allows the direct children of `audit/ops/hde-epic038/ops-03/` to be only:

- the ten sealed candidate primaries; and
- later updater-generated `.path_proof.txt` siblings for those primaries.

An action report, discovery report, authorization, role evidence, control file, or subdirectory under that exact root would cause stage 14 to fail with an unexpected-entry error.

The canonical packet therefore remains exact, while all ancillary records are in `audit/ops/hde-epic038/ops-03-operator-record/`. This is a placement constraint, not an omission of evidence.

## Finding F-11 — full PR-06R-B integration is not yet implemented

**Classification:** downstream repository gap  
**Strength:** current repository inspection  
**Disposition:** remains follow-up

The current repository state does not yet contain:

- the required generated `artifacts/runtime/direct_db_selection.snapshot.json`;
- OPS-03 primary bindings in `tools/evidence/update_evidence_index.py`;
- the seven OPS-03 schema bindings in that updater;
- final PR-06R-B release-gate behavior.

Consequently, this intake does not run the updater or hand-create its outputs. Path proofs, Index/Mirror rows, orientation refresh, and final nineteen-stage release PASS remain downstream PR-06R-B work.

## Finding F-12 — broader role ownership remains unresolved

**Classification:** architecture/lifecycle gap  
**Strength:** task boundary plus scoped repository inspection  
**Disposition:** out of scope

This task did not decide:

- application or runtime login ownership;
- writer or migration roles;
- owner-role semantics;
- secret storage and rotation;
- break-glass recovery;
- deployment ordering;
- revocation/retirement ownership;
- whether the legacy roles should be retained, migrated, or removed.

Those decisions require a separate authorized role-architecture action. The successful OPS-03 packet must not be used to imply that they are complete.

## Nonclaims

These findings do not:

- alter PF10 or any other PF-Canon file;
- move any PF09 item;
- establish QA PASS or token satisfaction;
- authorize writes or migration;
- prove deployment;
- complete PR-06R-B;
- close HDE-EPIC038.

