---
artifact_type: QA_PLAN_REVIEW
artifact_id: HDE-EPIC040-QA70-QA-PLAN-REVIEW
artifact_version: "1.0"
predecessor: none (first QA-70 review for this change)
REVIEW_MODE: INITIAL_QA_PLAN_REVIEW
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
decision: APPROVE
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
reviewer: Isis — continuing Lead Developer and QA Plan reviewer (Isis-50 session)
session_disposition: RETAIN_EXISTING
role_session_ref: Isis-50 (Product Owner-assigned continuing session)
invocation_binding: EPIC / HDE-EPIC040 / QA-70 / QA_PLAN v1.0
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-70 — Review Whole-Change QA Plan — 091426.1 (Notion 3db4590a05eb8143bf26d1459fbbcad7; page as of 2026-09-24T15:55:17Z; read in full)
reviewed_plan: docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.0.md (QA_PLAN v1.0, PLAN_PENDING; 86,589 chars read in full)
qa_audit: docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md (QA_AUDIT v1.0, AUDIT_COMPLETE; 49,905 chars read in full)
author: Kronos (execution identity https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md (read in full for QA-20 in this session; unchanged since)
observed_revision: efbe874 (origin/main after #535)
decision_time_utc: 2026-09-27
PF10_ADDENDUM_OUTPUT: NONE (initial approval produces no addendum)
---

# HDE-EPIC040 — QA Plan Review v1.0 (QA-70)

## 1. Decision

**`APPROVE`.** QA Plan v1.0 is coherent, complete, bounded and executable. It covers every acceptance criterion, both Product Owner dispositions and every Live QA Guide obligation. It gives each check explicit PASS, FAIL and blocked predicates, and its rerun, Moon Loop, escalation and report rules match PF19 and PF27.

This is an initial approval, so no PF10 addendum is produced. Approval is not task selection, execution, QA PASS, merge or closure.

`C040-09` is decided below (§4).

## 2. What was reviewed

| Area | Result | Basis |
| --- | --- | --- |
| Coverage | Complete | AC040-01 to AC040-09 each map to checks (Plan §2, §14; Audit §5); AC040-01 is documentary and assessed at QA-120, which is sound |
| Guide obligations | Complete | Plan §2.1 maps every Guide item, including Q-1 (check 10, with 9 and 13) and Q-2 (check 11) |
| PF05 §7.3.9 | Satisfied | Check 11 is a bounded, PO-only open-rails step that separates exercised from inferred behaviour, as §7.3.9 requires |
| Live readiness | Planned | Check 12, read-only with before/after row digests; no data is reported as `TOOLING_BLOCKED`, never PASS |
| Environments | Sound | Four classes (§5.2). Unsetting `DATABASE_URL` for closed-rails checks is correct: closed rails do not gate DB access (Audit QA50-F03, confirmed: `engine/db` has no rails check) |
| Dependencies and order | Sound | §11; dependents of a non-PASS check are `TOOLING_BLOCKED` without consuming a rerun |
| Evidence | Sound | QA root `audit/qa/hde-epic040/`; `record_check` primary logs and manifest; path proofs through the updater's `_refresh_path_proof`; bounded evidence-only commit (§7.2); Index/Mirror registration left to the evidence owner (QA50-F01) without a ledger-bound claim |
| Status and recovery | Sound | Five-state vocabulary; one ordinary-lane rerun only from tooling or execution faults; `FAIL_BEHAVIOR` goes to ESC-10 through QA-110 |
| Destructive modes | Controlled | Only `--compare-goldens` and `--check` modes of the comparator, and only `--check-manifest-only` of the recompute script, are allowed (QA50-F04). `bg:resolve`, upserts and writer routes are excluded |
| Report and RCA | Sound | §13 requires per-check accounting, per-criterion conclusions with proof classes, and a separate RCA |

## 3. Executable semantics verified against the code

The Plan's expected outcomes were checked against the source at `efbe874`:

| Plan expectation | Code | Result |
| --- | --- | --- |
| S-12/S-13: 32,769-byte body, with and without `Content-Length` → 422 `ERR_READER_INVALID_INPUT` | `adapter/http_reader.py` L467–475: limit 32,768; bounded read of limit+1 | Matches |
| S-07–S-11 malformed, BOM, extra key, upper-case UUID, empty → 422 | L476–488 | Matches |
| S-02/S-03 with `DATABASE_URL` unset → 503 `ERR_M10_RESOLVER_UNAVAILABLE` | L492–498: `DBAccess.for_current_env()` raises `PrimaryUnavailable`, an `AdapterError` (`engine/db/errors.py` L19) | Matches |
| R-02/R-03 unknown UUIDs → 404 `ERR_M10_PERSON_UNRESOLVED` | L503–505 | Matches |
| S-22 dev `GET /reader` under `APP_ENV=prod` → 403 `ERR_READER_FORBIDDEN` | L598–604 (version check, then the env gate) | Matches |
| S-23–S-25 → 403 `ERR_WRITER_FORBIDDEN`, `no-store` | `_dev_admin_gate` L818–823 via `_writer_error` (no-store, charset content type) | Matches |
| S-01 `/internal/version` has no env gate | L1090–1110 | Matches |
| Check 7 refusals, including `READINESS_UNAVAILABLE` with no DSN | `tools/bodygraph/check_magic10_gate_readiness.py` L211–224: rails, then selection, then DB | Matches |
| Check 12 count cross-check (zero rows → `missing`; more than one → `duplicate`) | `observe` L154–196 with `read_current_mapped_bodygraph` L184–187 | Matches |
| Check 6 mismatch: n ≥ 2, including `transcription.expected` for `M10-G001` | `tools/config/artifacts.py` L258–262, L405–414; fixture `expected.signals[0]` is `{"q": 0, "signal_id": "rapport_delta"}` | Matches |
| Check 11 stdout: six keys, 20 signals, 10 categories | `schemas/magic10_compat_result_v1.schema.json` required keys and min/max items; `engine/cli/main.py` L765–767 | Matches |
| Check 14 bands | `presenter/reader_v1/emitter.py` L8 `{"Cool","Open","Warm","Glow"}` | Matches |

No expectation was found to contradict the code.

## 4. Canon-conflict register decision

| Field | Value |
| --- | --- |
| ID | C040-09 |
| Classification | CANON_CONFLICT (QA process) |
| Sources | PF07-Canon-Glow-Infrastructure §2.8 (no git operations or run-time scripts in Live QA runbooks) versus PF19-Canon-Glow-QA-Guide §3.4.9, §3.6 and PF27-Canon-Plan-Templates ("Embedded harness checks") |
| Decision | **APPROVED**, alternative (a) as proposed |
| Reviewer / artifact / time | Isis-50; QA_PLAN v1.0 and QA_AUDIT v1.0; 2026-09-27 |
| Rationale | PF07 §2.8 itself routes the execution rail to PF19. PF19 §10.8 requires tested-source attribution, which needs read-only git observations. Alternative (b) would remove that attribution. The Plan's interim treatment is bounded: git reads are for attribution only and never a PASS gate, no script file is created, and only existing harness APIs are called |
| Scope | This QA Plan and its tasks only |
| Drainage | PF07 §2.8 wording; PF07 maintainer; documentation drainage, non-gating (Plan DD-02) |

C040-01 to C040-08 are carried unchanged from the QA Audit §11.

## 5. Other audit items resolved here

| Item | Resolution |
| --- | --- |
| QA50-S01 (birth tuples in vendor evidence) | The Plan's reading is accepted. PF19 §3.3 requires the substituted birth-input record, and Plan v2.1 §7.4 forbids persisting a person's birth record. So the tuples must be synthetic. **QA-90 constraint:** the check 11 task records the Product Owner's confirmation that the tuples used (the L-51 defaults or others he names) are synthetic, not a real person's data. Without that confirmation, check 11 is `TOOLING_BLOCKED` |
| QA50-F11 (Guide §8 attestation candidate) | Accepted as a correction to the Guide: the attestation binds `6f53d82`, and `6e4b3a1` is the supplemental A-5 to A-7 candidate. It has no effect on QA; recorded as DD-06 |
| QA50-S02 (population of "current rows") | Product Owner-supplied selection, reported in aggregate. Accepted |

## 6. Constraints carried to QA-90

1. The check 11 task carries the Product Owner's synthetic-tuple confirmation (§5).
2. The QA-90 task names the evidence branch and any execution-agent delegation for the ENV-C and ENV-S checks (Plan §6).
3. Checks 11 to 14 stay Product Owner-executed (Plan §7.1).

## 7. Unresolved items and owners

| Item | Owner | Blocking |
| --- | --- | --- |
| QA50-F01 Index/Mirror registration of QA evidence | Evidence owner, through the whole-change IA PR route | No (blocks only a ledger-bound claim) |
| QA50-F05 selection of existing current rows | Product Owner | Checks 12 and 14 are `TOOLING_BLOCKED` without it |
| QA50-B01 `--allow-prod-vendor` gap | PF05 and CLI owners | No |
| DD-01 to DD-12 | Named owners | No |

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-70-20260927-01
  change: EPIC / HDE-EPIC040 (Specification v1.1)
  prompt: QA-70 — Review Whole-Change QA Plan — 091426.1; Notion 3db4590a05eb8143bf26d1459fbbcad7; release GCFPE-20260914.1
  role_stage: continuing Isis, QA-70
  result: QA_PLAN_REVIEW v1.0, INITIAL_QA_PLAN_REVIEW, APPROVE; C040-09 APPROVED
  execution_identity: https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq
  repository_persistence: PENDING / NON_GATING
```

ASK OK.
