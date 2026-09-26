---
artifact_type: PR_WORK_UNIT_INSTRUCTION
artifact_id: HDE-EPIC040-PR07-PR-INSTRUCTION
artifact_version: "1.0"
artifact_state: INSTRUCTION_READY
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR07
authoring_context: APPROVED_BASE_WITH_OVERLAYS
issuer: retained whole-change HDE-EPIC040 Implementation Architect (PR-10)
capture_time_utc: 2026-09-26T18:05:00Z
baseline_main: 8999bd0
receiver: dedicated HDE-EPIC040-PR07 PR-development session (PR-20)
---

# HDE-EPIC040-PR07 — PR Work-Unit Instruction v1.0

## 1. Identity

| Field | Value |
| --- | --- |
| Work unit | `HDE-EPIC040-PR07`: final repository documentation through DOC-10. Documentation only |
| Base | Plan v2.1 §6.7 (`docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f93…`) |
| Amended by | PF10 §2.23 (PR06a overlay: PR07 keeps its boundary, inherits none of F03/F05/F07, and documents Reader v2, `/api/reader` and the conformed v1 schema as delivered). PF10 §2.25, the PR06b overlay, adds the v1 error schema and the `1.3.0` release |
| Order | `PR01 → … → PR06 → PR06a → PR06b → PR07 → OPS01`. PR01–PR06, PR06a and PR06b are `ACCEPTED_FINAL` |

## 2. Lineage

**Immutable bases:** Specification v1.1, Audit v2.0, Plan v2.1 and Plan Review v2.1.

**Accepted reviews:** PR01 v1.1, PR02–PR06 v1.0, PR06a v1.0 (`19ac13b7…`) and PR06b v1.0.

**PR06b review on the merge path:** `docs/ephemeral/HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md` (SHA-256 `15fbf143…3018`) is carried by the open PR [#514](https://github.com/amthorn78/glow-hdengine-v2/pull/514). It is not on `main` at this instruction's baseline. **Merge-order dependency:** #514 should merge before PR-20 reads it.

**PF10 read:** `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.6.md`, SHA-256 `cc20d134c54bcf0be3b192b063354ddd12688e51d82092f21a06160180de12e6`. It is the only PF10 file on `main`. Where this instruction differs from Plan §6.7 as amended by §§2.23–2.25, the plan and addenda govern.

## 3. Delivered state to document (verified at `8999bd0`)

**Release**
- 45 members, version `1.3.0`, `release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`.
- Admission returns `ADMITTED`.

**Reader routes**
- `POST /api/reader?v=1|2` is the production Reader.
- Dev `GET /reader` is Reader v1.
- `POST /reader` is a governed 405 stub.
- Every other method on `/api/reader` gets the governed 405.
- A missing, unsupported or duplicated `v` returns 400 `ERR_READER_INVALID_VERSION`.

**Reader v2** (`schemas/reader.v2.schema.json`)
- Six-key numeric-free envelope with `reader_version` `"v2"`.
- When eligible, ten `{id,band}` items in canonical order: `harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance`.
- `[]` when ineligible.

**Reader v1** (`schemas/reader.v1.schema.json`)
- Success returns `harmony` only, with an exact six-key closure.
- The error branch requires `schema:"v1"`, `ok`, `code` and `error`, restricted to the governed pairs (C040-08 A).
- The `*_leader` identities are retired from the contract.

**Earlier deliveries:** the PR01–PR06 core, config, schema, writer and comparator deliveries are described in their results and reviews. They are to be documented as Plan §6.7 *Required content* lists them.

## 4. Objective and completion

**Objective (Plan §6.7).** Make the implemented contract, the source-backed taxonomy, ownership, comparison/readiness usage and release boundaries legible in existing repository documentation after all implementation.

**Completion.** Final docs and any owner-required generated companions are committed through the PR-30/PR-35 lifecycle, with code review and ordinary CI on the exact head. This produces the clean final candidate for OPS01. It is not a QA verdict, acceptance, PF09 movement or closure.

## 5. Required content

1. **Plan §6.7 list:**
   - the supported four-argument core;
   - strict config/result schemas;
   - canonical writer and source ownership;
   - the distinction between a complete release and a candidate release;
   - the unchanged FE/BE and numeric-free Reader promises;
   - actual comparator/readiness commands;
   - non-mutation and security constraints;
   - how to find the authoritative 36-row evidence/decision (C040-06);
   - why Integration uses the broad grouping.
2. **§2.23 / §2.25 additions:**
   - Reader v2;
   - the `/api/reader` production route and its version selection;
   - the conformed Reader v1 schema, including the error branch;
   - the retired `*_leader` identities, as history rather than live paths;
   - the current release `1.3.0` with 45 members.
3. **Corrections:** remove or correct misleading live-path descriptions wherever they are actually affected, while preserving history. One confirmed instance: `docs/server/reader_v1.md:42` documents `GET /api/reader?v=1…`, but the production route is `POST`.
4. **Canon status:**
   - C040-06, C040-07 and C040-08: point to the decided record, and state truthfully whether PF01/PF04/PF05/PF12 drainage is still pending.
   - Do not create a second Canon catalog.
   - Do not copy the Plan or Audit into the repository.

## 6. Owned loci (resolved from the delivered tree)

The candidate homes below are existing documentation that currently mentions the affected surfaces. PR-20 confirms each one by reading it, and edits only where content is actually affected:

| Path | Anchor |
| --- | --- |
| `docs/server/reader_v1.md` | Reader routes (the `:42` correction); v2 coverage or a pointer |
| `docs/contracts/reader_v1_public_bytes.md` | v1 success/error contract |
| `README.md`, `CHANGELOG.md` | Current contract and release summary; CHANGELOG entry for HDE-EPIC040 |
| `docs/CLI_commands.md`, `docs/RUN.md` | Comparator/readiness commands, Reader invocation |
| `docs/config_and_bundles.md` | Strict config, writers, bundles |
| `docs/INDEX.md` | Routing to the above |
| `docs/acceptance/http_transport_evidence.md`, `docs/ADAPTER_009.md` | Only where they misdescribe current live paths |
| `ARCHITECTURE.md` | Only if it states the core or Reader contract |
| `AGENTS.md` | Only if needed for truthful developer routing; its existing rules must be preserved |

Rules for these loci:
- **New files:** at most one, and only if no existing home fits Reader v2. The plan must justify it.
- **Generated companions:** changed only where their current owner requires it.
- **Findings:** a required change to code, schemas, goldens, catalogs, evidence or `docs/pfcanon/` is a finding (§9), not a documentation edit.

## 7. Proof

- Every command, path, symbol, route, schema key and constant cited exists in the delivered tree, and each is checked by reading or execution.
- Examples match the tested schemas: v1/v2 examples validate against `schemas/reader.v{1,2}.schema.json`.
- Every link targets an existing artifact or home.
- There are no false claims of production, QA, approval or Canon drainage.
- There are no secrets and no real chart data.
- Ordinary CI passes on the exact head.

## 8. Exclusions

- No source, schema, golden, catalog, manifest or evidence behaviour change.
- No re-cut.
- No PF-Canon edit.
- No edit to the historical records under `docs/ephemeral/`.
- No QA, OPS or deployment.
- Carried observations stay with their owners and are only described, never fixed: O-P06a-22, O-12, O-P06a-03, O-P06a-23, O-P06b-17.

## 9. Rescope route

A newly found code or design defect is a finding. It goes to the whole-change IA under change control and is not silently fixed (Plan §6.7 *Recovery/security*). The decision returns to the PR07 session.

## 10. Sessions, merge and CI

- PR-20 runs in the dedicated PR07 session (`session_disposition: INITIAL_DEDICATED_ASSIGNMENT`, `role_session_ref: NOT_YET_ASSIGNED`).
- PR-30 and PR-35 each run in their own dedicated session.
- Nathan alone gives Proceed and merges. There is no auto-merge.
- Ordinary CI is the single `test` job.

## 11. Register

`CANON_CONFLICT_REGISTER`: C040-01 to C040-08 are carried unchanged. C040-06, C040-07 and C040-08 drainage stays with their maintainers.

## 12. Provenance

`GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR07-01`, from PR-10 — Create PR Work-Unit Instructions — 091426.1, on GCFPE-20260914.1 / 091426.1 / 55. Repository persistence is `PENDING / NON_GATING`. This instruction implements nothing and requests no Proceed.

## 13. Readiness

`INSTRUCTION_READY`. PR-20 may begin once #514 has merged.

## 14. PR-20 handoff

```text
Run PR-20 — Create PR Implementation Plan — 091426.1
https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204

Receiver: dedicated HDE-EPIC040-PR07 PR-development session
(session_disposition: INITIAL_DEDICATED_ASSIGNMENT; role_session_ref: NOT_YET_ASSIGNED).

Inputs:
- docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md — PR07 instruction v1.0, INSTRUCTION_READY
- docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md — immutable plan (§6.7 PR07)
- docs/ephemeral/HDE-EPIC040-PR06a-pr-work-unit-lineage-review-v1.0.md — PR06a ACCEPTED_FINAL
- docs/ephemeral/HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md — PR06b ACCEPTED_FINAL
- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.6.md — current PF10 (§§2.23–2.25)

Issue the PR07 implementation plan in state AWAITING_PO_PROCEED. Code or design defects found go to the whole-change IA and return to this session.
```
