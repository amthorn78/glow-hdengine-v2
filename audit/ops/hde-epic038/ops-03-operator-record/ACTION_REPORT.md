# HDE-EPIC038 OPS-03 full action report

## Outcome

OPS-03 completed successfully on 2026-07-23 UTC.

The authorized capture used the direct `psycopg` provider under a read-only transaction. The sealed packet reports `PASS`, zero SQL writes, zero retries, zero alternate-provider attempts, and all decisive predicates true. The temporary login was subsequently disabled, its password was cleared, and the reusable reader capability remained `NOLOGIN`.

This is an OPS execution and evidence-admission record only. It is not QA PASS, acceptance-token satisfaction, PF09 status movement, deployment, migration, epic closeout, or proof of a complete database-role architecture.

## Record placement

The canonical tracked packet is at:

`audit/ops/hde-epic038/ops-03/`

That directory contains exactly the ten sealed candidate files. The approved OPS-03 contract and the repository stage-14 validator reject every other direct child except updater-generated path-proof siblings. For that reason, the authorization, terminal control state, role-provisioning evidence, this report, and the discovery report are preserved at:

`audit/ops/hde-epic038/ops-03-operator-record/`

No candidate byte was edited during admission. No path proof, Human Evidence Index row, Machine Evidence Mirror row, manifest, acceptance map, close report, or other governed companion was hand-created.

## Authority and scope

- The Product Owner authorized the role-provisioning path allowed by PF10 — HDE Build Notes, §2.18.
- The Product Owner approved the exact canonical authorization bytes for one launch.
- When live preflight disclosed the unexpected legacy roles `hde_owner` and `hde_rw`, execution stopped before mutation. The Product Owner then directed the operator to record their presence, leave them unchanged, and proceed with the originally specified target roles.
- Authorized target roles were limited to:
  - `hde_reader`: reusable, non-login read capability.
  - `hde_ops03_reader`: task-specific login inheriting only `hde_reader`, with login removed after capture.
- The provisioning phase alone was allowed to mutate database roles, grants, and default privileges.
- The OPS-03 capture retained its original direct-only, one-attempt, no-retry, read-only, no-SQL-write contract.

## Execution identity

| Field | Recorded value |
|---|---|
| Repository | `amthorn78/glow-hdengine-v2` |
| Source commit | `043dd6b9751442d7a9329ccfff9f6483a9d4fee2` |
| Run ID | `ops03-rolefix-afdd3ab792724569a7c24f83` |
| Authorization window | `2026-07-23T23:30:09Z` through `2026-07-24T01:30:09Z` |
| Authorization SHA-256 | `911cbca9d81100092605a19271fb4701f0fde332bdc9e2a3dd59f73fdfca85ae` |
| Runner SHA-256 | `5b49fdf4fa7eefe05fdafa7fd5dbd202a80602535c84b2481ebac4525547ea8f` |
| Validator SHA-256 | `eebb11ef5d8352deb882dd50a49dac6e08ed8cb10d0c729031fb5c11a3b69d8f` |
| Interpreter SHA-256 | `46d05ca7094b029959f0218e990a7f2737dbc87d5b2e783ecfc44e978937922a` |
| Application environment | `dev` |
| Database schema | `hde` |
| Search path | `hde, public` |
| Provider | `psycopg` |

The authorization binds the exact interpreter, runner, validator, source commit, target, rails, query roster, expected counts, candidate root, command vectors, and one-attempt rule. It contains no database host, DSN, password, or role value.

## Source and tooling readiness

The original shared workspace was at the required commit and Git-clean, but the strict source-readiness gate found ignored Python bytecode residue. The operator did not clean or alter the shared workspace to make the gate pass.

Instead, the operator prepared:

- a fresh external clone at the exact required commit;
- an isolated external Python environment;
- `jsonschema 4.23` and `psycopg 3.2.13` in that environment;
- external operator tooling including PostgreSQL client 17.10, Railway CLI 5.28.0, and `expect`.

The isolated source remained pristine and bytecode-free through capture. The external tools and their temporary homes are execution dependencies, not tracked evidence or product source.

## Chronological action record

### S1 — source, interpreter, and Railway target

- Confirmed the required source commit.
- Stopped on the shared workspace's ignored-bytecode condition.
- Re-established the source gate with the pristine external clone and external interpreter.
- Completed browserless Railway authentication with the Product Owner's pairing action.
- Linked to the authorized project, production environment, and PostgreSQL service.
- Captured D1 at `role-provisioning/00-railway-status.txt`.

### S2 — live preflight and stop

The preflight connected as the administrative `postgres` identity and established:

- PostgreSQL 17.6;
- schemas `hde` and `public`;
- all five required relations present;
- no prohibited `PUBLIC` schema or relation privilege returned by the bounded checks;
- both target roles, `hde_reader` and `hde_ops03_reader`, absent;
- two unexpected non-system roles present: `hde_owner` and `hde_rw`.

Both legacy roles were `NOLOGIN` and had every elevated cluster-level flag shown by D2 set to false. Their appearance contradicted the blanket role-absence statement in PF10 — HDE Build Notes, §2.18, so the operator stopped before mutation.

A bounded, read-only session inspection found that neither legacy role could be substituted for the OPS-03 login:

- `hde_owner` did not have the required schema and read coverage.
- `hde_rw` had write-capable relation grants and lacked required current BodyGraph/boundary coverage.

Those detailed privilege observations are operator-session findings rather than rows sealed in D2. The Product Owner directed the operator to record both legacy roles, leave them untouched, and continue with the two named target roles. D2 is preserved at `role-provisioning/01-role-preflight.txt`.

### S3/S4 — first provisioning attempt and complete rollback

The first provisioning sequence created the two target roles and the specified grants/default privileges. The first S4 client command then failed before establishing the reader database connection because PostgreSQL client 17 did not interpret the full URI when supplied through `PGDATABASE` in the instructed form.

Because D4 had not passed, the operator followed the prescribed failure boundary:

- disabled login and cleared the temporary password;
- revoked the four new default-privilege grants;
- revoked membership;
- dropped objects owned by each new role;
- dropped `hde_ops03_reader`;
- dropped `hde_reader`;
- verified the target roles were absent before beginning again.

No OPS-03 authorization was generated or consumed during this failed pre-authorization sequence. No capture attempt occurred.

This rollback is an operator-session action record; the final D1-D8 set does not contain a standalone rollback transcript.

### S3/S4 — successful provisioning and reader verification

The operator generated a new high-entropy password, repeated the authorized provisioning, and retained the successful D3 output at `role-provisioning/02-role-provisioning.txt`.

For S4, the admin URI was parsed in memory into standard libpq connection fields so the password remained out of command arguments and output files. The dedicated reader connected successfully. D4 at `role-provisioning/03-reader-verification.txt` proves:

- effective role `hde_ops03_reader`;
- transaction read-only true;
- exact search path true;
- `rolsuper=false`;
- `rolcreatedb=false`;
- `rolcreaterole=false`;
- `rolreplication=false`;
- `rolbypassrls=false`;
- `schema_create=false`;
- `relation_write=false`;
- BodyGraph column metadata visible;
- BodyGraph constraint metadata visible;
- both boundary views visible;
- both expected partitioned tables visible.

The verification selected metadata only and rolled back its read-only transaction.

### S5/S6 — source binding and authorization

- Reconfirmed the exact source commit, clean external clone, bytecode-free state, and dependency imports.
- Generated a new run ID and canonical two-hour authorization.
- Validated the authorization before marker creation.
- Displayed the complete secret-free bytes for Product Owner review.
- Received explicit Product Owner approval for those exact bytes and one launch.

The preserved authorization is `authorization.json`.

### S7 — single capture attempt

Exactly one authorized OPS-03 capture attempt ran. No Railway CLI action occurred within the capture.

The terminal result was:

- process exit: exact `0` plus LF;
- stdout: exact `OPS03_CAPTURE_PASS` plus LF;
- stderr: empty;
- capture result: `PASS`;
- independent validation receipt: `PASS`;
- candidate inventory: exactly ten files;
- failure directory: absent;
- launch consumed: true;
- candidate finalized: true;
- candidate sealed: true.

The capture counts were:

| Counter | Observed |
|---|---:|
| Provider selections | 1 |
| Health connections | 1 |
| Health SQL statements | 1 |
| Posture transactions | 1 |
| Posture SQL statements | 10 |
| Direct connections | 2 |
| Total SQL statements | 11 |
| SQL writes | 0 |
| Retries | 0 |
| Alternate-provider attempts | 0 |

All capture predicates were true:

- authorization match;
- direct provider only;
- read-only transaction;
- exact search path;
- least-privilege role;
- valid DDL identity projection;
- constraints observed;
- boundary views read-only;
- partition posture observed;
- exact counts;
- secret values absent.

All independent receipt predicates were also true:

- authorization valid;
- source identity valid;
- schemas valid;
- canonical bytes valid;
- inventory valid;
- counts valid;
- secret scan valid;
- nonclaims valid.

### S8 — mandatory login cleanup

The first two attempts to reopen the Railway control-plane connection for cleanup encountered Railway DNS resolution failure. The operator did not retry the OPS-03 capture.

Because leaving the temporary login enabled was prohibited, the operator used the already authorized administrative PostgreSQL connection data in memory and executed only the prescribed cleanup and verification SQL. D7 at `role-provisioning/04-login-disabled.txt` records:

- `hde_ops03_reader` login disabled;
- `hde_ops03_reader` password cleared;
- `hde_reader` remains `NOLOGIN`;
- membership of `hde_ops03_reader` in `hde_reader` retained.

The Railway DNS failures and direct cleanup route are operator-session facts; the sealed D7 proves the resulting database posture.

### S9/S10 — sealing and handoff

- Generated D8 over exactly D1, D2, D3, D4, and D7.
- Verified both external checksum ledgers.
- Ran secret-safety checks over the candidate, authorization, control state, and role evidence.
- Unset secret-bearing shell variables.
- Confirmed the isolated source remained pristine and bytecode-free.
- Preserved the exact external artifacts for tracked admission.
- Revalidated the source-bound candidate before copy.
- Copied the ten candidate files byte-for-byte into the canonical tracked packet root.
- Copied the ancillary operator record into its contract-safe sibling root.

## Database mutation ledger

| Phase | Database mutation | Final disposition |
|---|---|---|
| First provisioning sequence | Created `hde_reader` and `hde_ops03_reader`; granted membership, connect, read access, and default read privileges; set role defaults; enabled temporary login | Fully reversed before authorization after S4 connection-command failure |
| Successful provisioning | Recreated the same bounded role/grant/default-privilege model and temporarily enabled the dedicated login | Retained as the authorized minimum role structure |
| OPS-03 capture | None; one health `SELECT`, one ten-statement read-only posture transaction, rollback | `sql_writes=0`; no commit |
| Mandatory cleanup | `ALTER ROLE hde_ops03_reader NOLOGIN PASSWORD NULL` | Login disabled and password cleared |
| Legacy roles | None | `hde_owner` and `hde_rw` left untouched |

The retained role model is deliberately narrow. It does not establish application, writer, migration, owner, deployment, rotation, recovery, or general service credential architecture.

## Evidence inventory and integrity

### Canonical candidate

| File | SHA-256 | Bytes |
|---|---|---:|
| `checksums.sha256` | `e26e1b5de37755b4f276a8d8d0f7c4bcec63c2f79dfce7080f84e3be0a16bc12` | 744 |
| `commands.txt` | `3d08535a6c97433e8cd2c8af8c1b5aa9c3556601779a4747856db40122682b7a` | 918 |
| `db_posture_summary.json` | `bce8cc6fb2bb82d9f7bc6010517abbb673abdfe03f23c7fbf4e998b2f687e0ed` | 3256 |
| `env_presence.json` | `c9cdc9d648967d5ccede735e3bd9da97e03881f603dfa8e907eeb0ef3d33a0e6` | 446 |
| `exit_code.txt` | `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa` | 2 |
| `nonclaims.json` | `a7a7144c52a758c9a83b269895ca7aa6e573a015e2f64b4808a86071b33f94d9` | 306 |
| `result_summary.json` | `2946b4addd10aa35e8ec5c3adee75e31c442fec33258151dcbde6eeed3d8fae6` | 793 |
| `stderr.log` | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 |
| `stdout.log` | `b2b5cec3fbe92c3554243cbad0c43042319d8be8e9574eed561e97e30ffdded9` | 19 |
| `validation_receipt.json` | `a9b351bba2480d09b384dc4867e986f45d3d3ed964f457d763777dc332798d1f` | 583 |

The candidate ledger covers the nine other primaries and excludes itself as required. The terminal control record independently binds all ten hashes.

### Role-provisioning evidence

| Deliverable | File | SHA-256 | Bytes |
|---|---|---|---:|
| D1 | `00-railway-status.txt` | `1c48d9b22edff608bd6f9ce46c0b6e0caa01db39596071642eb29c1fb1114f61` | 1014 |
| D2 | `01-role-preflight.txt` | `d123feebd82f0bf8d20f9f4a0c889a85823cf22af6da1b63e46338829fbf421d` | 1369 |
| D3 | `02-role-provisioning.txt` | `12037d50787dd31bc3bdef8970e68390c12240a368d9eac36b7b71c46f779901` | 795 |
| D4 | `03-reader-verification.txt` | `ec35a41329cab7b1251aaf900dbc5812abe4542d7639747c47e78cb47e015c18` | 767 |
| D7 | `04-login-disabled.txt` | `e9c60edb3434dac266c94cb208ece0fca0aec73cadbf7fdf803a6ea1cc62877a` | 288 |
| D8 | `checksums.sha256` | `909189ddbd0fced6937c94c58d3c4e45b74ec69bd71009a5da1d2169a766c36d` | 448 |

D8 covers exactly D1, D2, D3, D4, and D7 and excludes itself as required.

### Authorization and terminal control state

| File | SHA-256 |
|---|---|
| `authorization.json` | `911cbca9d81100092605a19271fb4701f0fde332bdc9e2a3dd59f73fdfca85ae` |
| `control/.capture.committed` | `a35c3318268c31d66661400c4c0bfee16d7420b8a76f6d9226e607f8ba08e0c5` |
| `control/authorization_consumed.json` | `409d17ad7803bf06233fb7c47f760cedc1c636af1be703e90ac573396407b2ff` |
| `control/launch.marker` | `48f7223cde9f8e7a08abc360609e61bdb7899ed6ec49837f8516abf3416755c7` |

The control record reports `launch_consumed=true`, `finalized=true`, and `sealed=true`. No failure packet exists.

## Secret and data-safety posture

- Candidate JSON records the database URL only as `SET_REDACTED`.
- Retired transport keys are recorded only as `UNSET`.
- No password, password hash, DSN, URI userinfo, API key, authorization-header credential, private key, or raw database row is present in the admitted records.
- The posture packet contains names, booleans, counts, query IDs, and hashes, not data rows.
- All audited text is UTF-8/LF; no CR or NUL was found.
- D1 contains internal Railway operational metadata, including identifiers and public service metadata, but no credential. It should remain within the intended evidence repository.

The external authorization and role-evidence source files had permissive file mode `0646` inside mode-`0700` temporary directories. Directory traversal remained owner-only and no content leak was observed. This is a procedural file-mode anomaly, not a byte-integrity failure; the repository copies do not preserve that temporary-directory access model.

## Deviations and recoveries

| Event | Classification | Recovery and effect |
|---|---|---|
| Shared workspace contained ignored Python bytecode | Source-readiness stop | Used a pristine external clone and external interpreter; did not clean or alter shared source |
| Unexpected `hde_owner` and `hde_rw` | Required S2 stop / PF10 conflict | Stopped before mutation; performed bounded read-only inspection; obtained PO direction to record and leave untouched |
| First S4 `PGDATABASE` URI form failed before connection | Instruction/client compatibility defect | Immediately disabled login and fully rolled back first provisioning; generated no authorization |
| S4 needed decomposed libpq fields | Minimal execution deviation | Parsed the URI in memory; kept secrets out of arguments and files; D4 passed |
| Railway control-plane DNS failed during S8 | Mandatory-cleanup transport issue | Used the secured admin DSN in memory for only the prescribed cleanup SQL; did not retry capture |
| Initial manual intake-validator invocation omitted the validator's required `SAFE_MODE`, `ALLOW_NETWORK`, and `ALLOW_DB_WRITE` environment keys | Read-only intake invocation error | Re-ran with the exact closed validator environment; the source-bound validator passed and no bytes changed |
| Supplemental records requested with canonical packet | Repository contract conflict | Kept the exact ten-file root intact and placed supplemental records in the adjacent operator-record root |

## Validation performed for admission

- Exact source-bound external validator: PASS.
- Candidate `sha256sum -c`: PASS.
- Role-provisioning `sha256sum -c`: PASS.
- Candidate inventory and regular-file check: PASS.
- Canonical JSON and exact LF/stream checks: PASS.
- Candidate-to-tracked byte comparison: PASS.
- Repository offline OPS-03 tracked-packet validator: PASS.
- Retained-evidence secret-safety scan: PASS.
- Supplemental secret-pattern scan: PASS.

The complete PR-06R-B integration is not claimed here. The current canonical updater does not yet register the OPS-03 primaries, the seven OPS-03 schemas, or the direct-selection primary, and the required direct-selection artifact is not present. Those are implementation prerequisites before updater-owned path proofs, Index/Mirror refresh, orientation, the final nineteen-stage pipeline, or PF09 supportability can be claimed.

## Source-strength labels

- **Sealed evidence:** the ten candidate files, D1-D4/D7-D8, authorization bytes, and terminal control records copied into this repository.
- **Repository reality:** current validator behavior, current updater bindings, current tracked historical files, and current Git state observed during intake.
- **Operator-session record:** first-attempt rollback, detailed legacy-role privilege diagnostic, S4 URI handling, and S8 Railway DNS failure. These actions/findings were observed during execution but do not have separate raw transcripts in D1-D8.
- **PO direction:** exact authorization approval and the instruction to record, preserve, and not alter the two unexpected legacy roles.

## Explicit nonclaims

This report does not claim:

- acceptance-token satisfaction;
- QA PASS;
- PF09 wording or status movement;
- production write authorization;
- database migration;
- deployment;
- Railway inventory proof beyond the bounded D1 target record;
- retired transport availability;
- complete application/writer/migration/owner/rotation/recovery role architecture;
- complete PR-06R-B;
- HDE-EPIC038 closeout.
