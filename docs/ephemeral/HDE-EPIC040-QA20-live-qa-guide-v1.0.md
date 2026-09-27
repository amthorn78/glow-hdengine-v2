---
artifact_type: LIVE_QA_GUIDE
artifact_id: HDE-EPIC040-LIVE-QA-GUIDE
artifact_version: "1.0"
predecessor: none
state: GUIDE_READY
AUTHORING_CONTEXT: INITIAL_OR_PREAPPROVAL_AUTHORING
change_class: EPIC
change_id: HDE-EPIC040
change_name: Separation Pass 3
author: Isis — continuing Lead Developer and whole-change readiness decision owner (Isis-50 session)
session_disposition: RETAIN_EXISTING
role_session_ref: Isis-50 (Product Owner-assigned continuing session)
invocation_binding: EPIC / HDE-EPIC040 / QA-20 / whole change
context_conflict: NONE
execution_posture: MANUAL_PROMPT_EXECUTION
prompt: QA-20 — Create Live QA Guide — 091426.1 (Notion 3db4590a05eb816daa3adff37283482b; page as of 2026-09-24T15:53:39Z; read in full)
readiness: docs/ephemeral/HDE-EPIC040-QA10-qa-readiness-v1.0.md (READY_FOR_QA)
reality_audit: docs/ephemeral/HDE-EPIC040-QA10-reality-audit-v1.0.md
change_audit_triage: docs/ephemeral/HDE-EPIC040-QA10-change-audit-triage-v1.0.md
po_disposition: docs/ephemeral/HDE-EPIC040-QA10-po-disposition-v1.0.md (Q-1 yes, Q-2 yes)
pf10: docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md (read in full; applicable addenda §§2.2–2.28)
repository_baseline: main 78351a8 (audited code state 39b9cdf; later commits change only docs/ephemeral and docs/pfcanon)
next: QA-50 — Create Whole-Change QA Audit and Plan — 091426.1 (continuing Kronos)
PF10_ADDENDUM_OUTPUT: NOT_PRODUCED_BY_QA-20
---

# HDE-EPIC040 — Live QA Guide v1.0

This Guide tells Kronos what was delivered, what QA must establish, and under which constraints. It is not the QA Audit, QA Plan, task set or report, and it pre-approves no result. Kronos audits the actual system and may find things this Guide does not name.

## 1. Readiness still holds

| Check | Result |
| --- | --- |
| Commits since the audited state `39b9cdf` | `fcb02f1` (#532, QA-10 records) and `78351a8` (#533, PF10 v13.3.9 and PF23 v1.2.1): `docs/ephemeral/` and `docs/pfcanon/` only. No product, test, CI, schema, catalog or evidence byte changed |
| PF10 v13.3.9 | Adds §2.28, which records the QA-10 triage. It contains no objective failure or new gate (see §11) |
| Product Owner dispositions | Q-1 security QA step required; Q-2 PF05 §7.3.9 open-rails step applies, no exemption |

Readiness `READY_FOR_QA` stands. No return to QA-10 is needed.

## 2. What was delivered

| Surface | Delivered behaviour | Source |
| --- | --- | --- |
| Catalog | 36 Channels, ascending Gate pairs, no null substreams | `catalog/channels_v1.json`; PR01 |
| Mechanics config and schemas | `catalog/magic10_mechanics_v1.json` (`m10-channel-state-v1.0.0`: 20 signals, 3 profiles, 10 category weights, 2 Balance operations); `schemas/magic10_mechanics_v1.schema.json`, `…result_v1…`, `…compat_result_v1…` | PR01 |
| Admission | `engine.config.registry_loader.load_active_mechanics_bundle()` admits only release 1.3.0 with exactly the 45-member roster; typed refusals `INCOMPLETE_RELEASE_ROSTER`, `RELEASE_ROSTER_MISMATCH`, `RELEASE_VERSION_MISMATCH`, `RELEASE_TIMESTAMP_MISMATCH`, `MISSING_FILE` | PR02, PR03, PR06, PR06a, PR06b |
| Core | Pure `compute_core(member_a, member_b, mechanics_bundle, release_id)`; intrinsic `pair_key`; reached through `engine/compat/compute.py::evaluate_pair` | PR03, PR04 |
| Reader v1 | `POST /api/reader?v=1`: harmony only, numeric-free, six-key envelope; four-key error envelope per C040-08 | PR04, PR06a, PR06b |
| Reader v2 | `POST /api/reader?v=2`: ten `{id, band}` items in canonical Magic-10 order when eligible, `[]` when ineligible | PR06a (C040-07) |
| Route rules | Every non-POST method on `/api/reader` → governed 405 (`ERR_NOT_FOUND`, `Allow: POST`, `no-store`) on all three factories; invalid `v` → 400 `ERR_READER_INVALID_VERSION` | PR06a |
| Dev routes | `GET /reader` (Reader v1, `APP_ENV=dev`); `/dev/{sampler,reader,writer}/conjunction` gated to `dev\|test\|local` | PR04, PR06a |
| CLI | `hdctl showcompat` stdout = canonical `magic10_compat_result.v1` + one LF; `--dump-reader`; `--conjunction`; `bg:resolve` | PR04 |
| Golden comparison | `python tools/config/generate_config_artifacts.py --compare-goldens <root>`: 0 match, 1 mismatch, 5 refusal; 8 cases `M10-G001`–`G008` | PR05 |
| Gate readiness | `python tools/bodygraph/check_magic10_gate_readiness.py`: closed rails only, read-only, typed `READINESS_*` refusals | PR05 |
| Release attestation | `python tools/evidence/build_release_attestation.py --output <external-empty-dir> --require-clean` → `PR06R_B_FINAL_PASS`; OPS01 verified 1.3.0 and adverse checks A-1–A-7 | PR06, OPS01 |
| Documentation | README, AGENTS, CHANGELOG, `docs/contracts/reader_v{1,2}_public_bytes.md`, `docs/server/reader_v1.md`, `docs/CLI_commands.md` | PR07, DOC-20 |

## 3. Acceptance obligations QA must cover

The criteria are the Specification §11 `AC040-*` rows. What QA should establish for each:

| Criterion | What QA establishes | Already evidenced (not re-proof) |
| --- | --- | --- |
| AC040-01 scope | Coverage record: 13 requirements across the delivered units, C040 register decided | Lineage reviews, readiness §3 |
| AC040-02 catalog | Schema-valid catalog; negative cases (duplicate/descending gates, null substream) rejected; FE/BE bundle compatibility | PR01 tests and evidence |
| AC040-03 schemas | Mutation matrix: missing/extra/duplicate members, invalid operations and profiles rejected | PR01/PR02 tests |
| AC040-04 fail-closed | Each decisive invalid class refuses with no partial result or fallback; bundle immutable | PR02/PR03 tests |
| AC040-05 identity | Byte change to a member or wrong manifest cannot keep a valid identity; `release_id` recomputes | OPS01 A-5–A-7; `release_id_recompute --check-manifest-only` rc 0 |
| AC040-06 comparison | 8 of 8 goldens match at the repository root; a deliberate mismatch reports mismatch; nothing mutated before/after | DOC-20 R6 (IA-run) |
| AC040-07 ingress and readiness | Gate normalization/rejection corpus; **live readiness observation against current rows**, read-only, no backfill | Offline only (PF10 §2.20) |
| AC040-08 integrated proof | Owner-generated evidence coherent; validators pass | QA-10 E-D01–E-D06 |
| AC040-09 boundary | Public Reader v1/v2 numeric-free; no new public surface beyond the approved Reader v2; no secret or internal leakage in errors | Code inspection only |

## 4. Required QA steps set by decisions

1. **Open-rails step (PF05 §7.3.9, PO Q-2).** HDE-EPIC040 changed CLI behaviour and the vendor-backed resolution path. At least one bounded open-rails step is required. It must be PO-authorized, secret-safe, bounded and stored as governed evidence, and must distinguish exercised from inferred route behaviour. The AGENTS.md showcompat posture applies: `hdctl showcompat` with birth-argument inputs and `--source vendor` under `SAFE_MODE=0 ALLOW_NETWORK=1`, env probes recorded as SET/UNSET only. HumanDesignAPI only; no AI provider calls.
2. **Security step (PO Q-1).** One bounded security check of `POST /api/reader` (v=1, v=2, invalid v, malformed body, oversize body, every non-POST method) and of admission refusal propagation: no secret, stack trace, Gate payload or internal diagnostic in any public response, and consistent `no-store`. Accepted PRs are not reopened; a defect found is a finding for the owner route.
3. **Live Gate readiness.** One read-only run of the readiness tool against current rows, under the tool's closed rails, with a real `DATABASE_URL` supplied by the operator. Prove non-mutation (row counts or checksums before and after).

## 5. Environment and setup

- Python 3.12 matches CI (`ci.yml`); the audit container had 3.11. Record the interpreter used.
- Install `requirements.txt`, `requirements-dev.txt` and `-e .` in a fresh venv. Debian-patched setuptools breaks the attestation builder's wheel stage (O-10); OPS01 worked around it this way.
- Default rails are closed: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`. Open rails only for the step in §4.1.
- `DATABASE_URL` is the only DB surface. Retired bridge keys must be absent; their presence is refused.
- Vendor keys: `HD_API_BASE_URL`, `HD_API_KEY` (and `GEO_API_KEY` where used). Never print values.
- Serve HTTP via `adapter.factory:create_app()`, which is what the Procfile uses. `adapter.wsgi` behaves differently for unknown paths (O-P06a-22); test the factory production uses and note the others.

## 6. Integration risks

| Risk | Why it matters | Evidence |
| --- | --- | --- |
| Admission is exact and ordered | Any environment with a modified or partial checkout refuses; QA must run from a clean tree at a known commit | Audit E-B04 |
| Wheel installs refuse (O-12) | Installing the package non-editably will fail admission; use the source tree | PF10 §2.22 |
| HTML 404 on the production factory (O-P06a-22) | Unknown `/api/*` paths return HTML, not the governed JSON | Audit E-C02 |
| APP_ENV asymmetry (O-P07-04) | Dev `GET /reader` treats unset as dev and refuses `test`; conjunction routes do the opposite for unset | Audit RA-06 |
| `--band` ignored with `--pair-file` (O-P07-02) | A QA step using both would get the pair-file band silently | Audit RA-07 |
| `bg:resolve` output bypasses the LF guard | Do not assume showcompat's stdout guarantees for `bg:resolve` | Audit flow table |

## 7. Required evidence

- Store QA outputs under `audit/qa/hde-epic040/` (the change's evidence root; it does not exist yet), never in the repository root.
- Each step records: tested commit, interpreter, env pins, command, exit code (captured from the producer), outputs or digests, actor, time, limitations.
- Status vocabulary: `PASS`, `FAIL_BEHAVIOR`, `FAIL_TOOLING`, `TOOLING_BLOCKED`, `PARKED`. Unavailable prerequisites are not PASS.
- Open-rails evidence redacts keys, tokens and base URLs; logs are keys-only.
- Publication into the Index/Mirror, if any, only through `tools/evidence/update_evidence_index.py`.

## 8. Known limitations and baseline

- Failing before QA, and baseline rather than results: `tests/reader_v1/test_cli_proof.py` (O-P06a-03); 57 failures and 13 collection errors among test files outside the CI lanes (PR05 count). 189 test files are named by no fixed lane or roster.
- Security review never covered the implementation deltas of PR04, PR05, PR06 and PR06a.
- OPS01's attestation proves release integrity at candidate `6e4b3a1`, not runtime behaviour.
- Canon drainage of C040-05–08 is pending; PF01, PF04, PF05 and PF12 still describe Reader v2 as future. The PF10 addenda govern.

## 9. Permitted and forbidden actions

| Permitted | Forbidden |
| --- | --- |
| Run tests, CLI, local servers and read-only tools under closed rails | Editing product code, tests, schemas, catalog, manifest or governed evidence |
| The bounded open-rails step, once PO-authorized in its task | Any AI-provider call; unbounded vendor traffic |
| One read-only readiness run against current rows | Any DB write, backfill, migration or upsert (`bg:resolve --upsert` included) |
| Writing QA logs under `audit/qa/hde-epic040/` | Release cuts, deployment, activation, merges, PF-Canon or PF10 edits |

## 10. Recovery

- A behaviour contradiction is `FAIL_BEHAVIOR` with evidence and goes to the owner route (ESC-30 for an objective failure); it is not fixed in QA.
- Tooling or environment failure is `FAIL_TOOLING` or `TOOLING_BLOCKED`; retry within the QA retry rule, never by editing product files.
- A failed vendor or DB prerequisite leaves that step blocked, not passed.

## 11. PF10 lineage and carried register

PF10 read: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.9.md` (SHA-256 `54e660e3…`, 298,265 chars, read in full); HDE-EPIC040 addenda §§2.2–2.28 apply. §2.28 records the QA-10 triage: "Objective failures: none evidenced", no doc delta required before QA, and RA-10 requires the open-rails step in the QA plan (satisfied here by §4.1). PR07's acceptance is recorded in `docs/ephemeral/HDE-EPIC040-PR07-pr-work-unit-lineage-review-v1.0.md` (ACCEPTED_FINAL), not in a PF10 addendum.

`CANON_CONFLICT_REGISTER` is carried unchanged from the QA-10 readiness record §5: C040-01–04 resolved; C040-05–08 decided, drainage pending, non-gating.

## 12. Unresolved items and owners

| Item | Owner |
| --- | --- |
| O-12, O-P06a-22, O-P07-01–04, O-P06a-03, O-P06a-23, O-P06b-17, O-OPS01-01/02 | As recorded in the QA-10 triage §2 |
| PF10 §2.11 truncated sentence (O-P06-21) | Resolved in v13.3.9: the sentence at L1376 is complete, and §2.27 and §2.28 are indexed. §2.28's internal line references to §2.19/§2.20 are off by two in v13.3.9 (informational, PF10 drain owner) |
| Doc deltas RA-06, RA-13, FND-017 | Their owners (triage §4) |

## Provenance

```text
GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-QA-20-20260927-01
  change: EPIC / HDE-EPIC040 (Specification v1.1)
  prompt: QA-20 — Create Live QA Guide — 091426.1; Notion 3db4590a05eb816daa3adff37283482b; release GCFPE-20260914.1
  role_stage: continuing Isis, QA-20
  result: LIVE_QA_GUIDE v1.0, GUIDE_READY
  execution_identity: https://claude.ai/code/session_015Y2tpUnUNcpBoCzwN3aRXq
  repository_persistence: PENDING / NON_GATING
```
