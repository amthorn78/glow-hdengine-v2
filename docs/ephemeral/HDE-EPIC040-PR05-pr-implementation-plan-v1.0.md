---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR05
pr_instruction_id: HDE-EPIC040-PR05-PR-INSTRUCTION v1.0
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
planning_inspection_capture_utc: 2026-09-24T18:05:25Z to 2026-09-24T18:21:16Z
next_stage: PR-30 (Product Owner Proceed required first)
---

# HDE-EPIC040-PR05 — PR Implementation Plan v1.0

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN` |
| version | `v1.0` — first plan for this work unit; no predecessor |
| state | `AWAITING_PO_PROCEED` — complete and executable within the approved scope plus the applicable PF10 overlays (§2.3); no boundary finding; pending Nathan / Product Owner's exact PR-30 invocation against this version |
| finding_ref | none raised; no RS-10 route opened (§14) |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-plan-v1.0.md` |
| CHANGE_CLASS / CHANGE_ID | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR05` — Full golden comparison and read-only Gate readiness |
| PR_INSTRUCTION_ID | `HDE-EPIC040-PR05-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY`, `docs/ephemeral/HDE-EPIC040-PR05-pr-instruction-v1.0.md`, SHA-256 `adb01ad8c0db18a9a8e45f6bfb183c15046aebd250a5dcbd509aa6d96f5d6ce7` (landed on `main` by #490 at `cb27bcb603692345064383601bfa2d026d69930e`, 2026-09-24T18:05:58Z; byte-identical to the handoff's stated digest) |
| IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1, immutable approved base, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| SPECIFICATION_ID | `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED` |
| PLAN_REVIEW_ID (original, preserved) | `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z |
| Applicable overlay reviews | `HDE-EPIC040-PR04-F01-RESCOPE-REVIEW` v2.0 (RS-20 `RESCOPE_REVIEW`, Isis-50 `APPROVE` 2026-09-22T07:27:55Z) with its one addendum, drained as PF10 §2.15. No `REMEDIATION_REVIEW` applies |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR05 |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` for PR-20; PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | `NOT_YET_ASSIGNED` — the handoff named the operator as assignment owner at launch and the launch message assigned none; no platform ID is invented. Known runtime identity from the harness: `https://claude.ai/code/session_01FTff5iBZhV6crMfp7dkvxh` |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR05` / `PR-20` |
| context_conflict | `NONE` established |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| AUTHORING_CONTEXT | `APPROVED_BASE_WITH_OVERLAYS` — immutable approved base plus the applicable PF10 overlays in §2.3 |
| native_next_owner | Nathan / Product Owner for the exact PR-30 Proceed decision against this version; no other manual prerequisite remains |

This plan is complete for the exact approved PR05 work unit and executable within the approved scope: every file, seam, contract, test, checkpoint, validation command, review obligation and risk is planned in §§4–12. `AWAITING_PO_PROCEED` is a plan state, not an authorization. PR-20 performed no repository mutation outside this planning artifact under `docs/ephemeral/`: no implementation, no product branch, no product commit, no pull request other than the storage pull request for this artifact, no review, no CI run, no merge, no QA, no Ops, no release activation, no PF10 edit or number allocation, no addendum, no Epic closure.

The Product Owner's PR-30 Proceed for PR05 does not exist at planning time. This plan does not assume it, does not request it as a precondition of anything below and does not fabricate it. The only implementation authority is Nathan / Product Owner's manual invocation of the selected `PR-30 — PR Implementation Proceed — 091426.1` against this exact plan version (v1.0) and the PR instruction in §2.1. That Proceed authorizes implementation of this plan only and supplies no merge authority. `PR-50 — Abort PR and Escalate` is invocable only by Nathan / Product Owner.

## 2. Exact controlling lineage and source record

All lineage is resolved by repository path on `origin/main` at head `cb27bcb603692345064383601bfa2d026d69930e` (tree `63656a11835703fe41acd50f23c731ee77dc5be1`). Google Drive was not consulted and is not a source, store or authority for this work. Dead `libfile_` or `drive.google.com` links inside earlier lineage bodies are migration provenance, not blockers.

### 2.1 Approved and accepted change lineage

| Role | Exact repository artifact and current decision | SHA-256 |
| --- | --- | --- |
| `PR_INSTRUCTION_REF` | `docs/ephemeral/HDE-EPIC040-PR05-pr-instruction-v1.0.md` — `INSTRUCTION_READY`; sole substantive input; read completely (299 lines, 32,963 bytes) | `adb01ad8c0db18a9a8e45f6bfb183c15046aebd250a5dcbd509aa6d96f5d6ce7` |
| `SPECIFICATION_REF` | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md` — v1.1, `SPECIFICATION_APPROVED`, Thoth-17 `APPROVE` 2026-09-08T13:23:24Z; §5 requirements and §11 criteria read | `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| `IMPLEMENTATION_AUDIT_REF` | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md` — v2.0, `AUDIT_COMPLETE` | `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b` |
| `IMPLEMENTATION_PLAN_REF` | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` — v2.1, immutable approved base; §§4.3, 4.4, 5.9, 6.5, 6.6, 7, 8, 9, 10, 11.1 read completely | `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| `PLAN_REVIEW_REF` | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md` — v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z, binding the exact Plan bytes above | `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Approved overlay (F01) | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` — RS-20 `RESCOPE_REVIEW` v2.0, Isis-50 `APPROVE` 2026-09-22T07:27:55Z; §7 "PR05 is covered" read | `7700796fedcbd5847146f8e47c611aec662f67ec9ae99e4e8ed97279edbf5b20` |
| F01 addendum source | `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` — drained as PF10 §2.15 | `86708f5c32de990be892bbb3f1ced973c5a110e30496753ca871b8f72c8082c1` |
| Accepted PR01 | `docs/ephemeral/HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md` — `ACCEPT` (#403) | `f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273` |
| Accepted PR02 | `docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md` — `ACCEPT` (#404) | `4b8d638c3f0e9232c8c2143fbce9593296f89c5dcc3d6b6da82293f21d5ab5c3` |
| Accepted PR03 | `docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` — `ACCEPTED_FINAL` (#405) | `07647f68bb5f5a705d8d2196f2aaaca9c17cb2b1c9f8774f8fd2b8268ae7dffa` |
| Required predecessor PR04 | `docs/ephemeral/HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md` — `ACCEPT`, `ACCEPTED_FINAL`, 2026-09-22T21:35:55Z; landed squash `cd6f9e6ca4541f448f77b206269f3882cb919f36` (#467), tree `72f0868de3635494916097b36656af302b914003` | `08bff31889c9c76b65cf788826f2a602a388e64c4247eaef7e5ca89df086dba4` |
| PR04 instruction / plan / result (context only) | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md`; `…-PR04-pr-implementation-plan-v1.2.md`; `…-PR04-pr-implementation-result-v1.0.md` — read for the landed seams, test pins, classifier registrations and F01 implementation facts | `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf`; `dc005adc9ec0acd4541241f1893712d5c780f01632a09284aa6bd3d779779160`; `734e69f24cc4891dfb72c10d10137c774af7e3a586384df1a462bcb6313243e5` |
| PR04 deferrals F03 / F05 / F07 | `docs/ephemeral/HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md`; `…-F05-…`; `…-F07-…` — inherited, PR07-owned | `3f592509bf6a852f4a5947ad49b3044bcd4511c6c5fbcd57eb262263619b10a0`; `2cc921e297c3b1cc5fa9b92113ab5b51c9c89cfa735bbca04655950f01060375`; `78d32798ebfd0e8d45c86cca30df11b033c8f1d4e12d23fcc878b68899b31ab5` |

No accepted PR, approved base or original Proceed is reauthored or rerun. PR01–PR04 are `ACCEPTED_FINAL`. The instruction's `AUTHORING_CONTEXT` and overlay type ("RS-20 `RESCOPE_REVIEW`, not an ESC-40 `REMEDIATION_REVIEW`") are carried as stated.

### 2.2 Controlled subject-matter sources used

Each resolved as the unique current controlled Markdown in `docs/pfcanon/`; no Google Doc, `.doc`, `.docx`, export, archive result or search hit was opened, compared or cited.

| Source | Path (SHA-256) | Decisive use |
| --- | --- | --- |
| PF01 v1.3.7 | `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md` (`101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a`) | §9.5 "Canonical Magic10 v1 goldens" (lines 1859–2018) read completely: sole authority for M10-G001–G008 inputs, metadata, synthetic UUIDs, expected outputs and hashes; §4.5 validation fixtures; §4.7 emission rule (line 532) |
| PF12 v2.9.5 | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md` (`d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d`) | Line 1733: `tools/bodygraph/check_magic10_gate_readiness.py` in the promoted "Gate persistence and resolution" class; lines 4756–4762: config tooling must fail closed and must not activate a candidate; the golden identity `tests/fixtures/magic10/v1/goldens.json` is a deterministic verification input only; §4.1 (line 1607) canonical JSON rules |
| PF09.3 v1.1.5 | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md` (`0e3415e62e92f9d18c0d6ac1e513c1d8999efcacf2f71f4e1bda495fdbadec65`) | HDE-SEPA005.4 (line 1192) and HDE-SEPA005.5 (line 1203), both `Not done` (line 171); PR05 contributes and moves no status |
| PF05 v2.5.2 | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md` (`a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e`) | §3.4 exit-code taxonomy (line 347) and §8.3 summary (line 3897) for the two new command surfaces; §5.2 `ERR_M10_*` / `ERR_READER_*` tokens (lines 2228–2256) |
| PF02 v2.4.5 | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.5.md` (`d57fd3547573b8b8e3076b8f3fa4a34423a8b677c10bca93ff58eb6d4d867c6f`) | Pure-core / application separation; readiness-style surfaces are side-effect-free (lines 941–954, 1307) |
| PF14 v3.5.7 | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.7.md` (`a9c376f64e1cc3bb691d1661d131b3a42f6f96d318e82b981989b4a4836bd86c`) | §6.7 under C040-05: the four-argument core is the only calculator |
| PF03 v1.8.7 | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` | Source fidelity for the fixture transcription |
| PF27 v2.0.4 | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.4.md` (`aa4ac7201e83beb46d43be80999049edcb43a2d24798a8b51ca6c2cce67b5248`) | Checked: it holds no per-PR plan template; this plan follows the PR-20 contract and the accepted PR04 plan shape |
| PF09.6 v1.1.9 | `docs/pfcanon/PF09.6-Canon-HDE-Build-Checklist-Distillation-v1.1.9.md` | HDE-DIST008 (line 1798) is later-phase context only; PR05 claims no HDE-DIST008 completion |

### 2.3 Current controlled PF10 and every applicable active addendum

Current controlled PF10, resolved from `docs/pfcanon/` at planning: **`docs/pfcanon/PF10-HDE-Build-Notes-v13.3.md`**, 2,156 lines / 235,187 bytes, SHA-256 `d79e41102a88ded2cf9823787925c0ac243622cf2a3e59a3e5c1da28387e6f91` — the same bytes the instruction resolved. Its Addendum Index (lines 184–207) lists 2.1–2.19; body and index agree. Effective baseline: **approved base + the applicable PF10 overlays below.** The canonical text of every overlay is PF10's; the `docs/ephemeral/` paths are the retained addendum source artifacts where the repository holds one. No overlay moves ownership into or out of PR05.

| PF10 addendum (heading line in v13.3) | Scope | Effect carried into PR05 | Retained repository source artifact (SHA-256) |
| --- | --- | --- | --- |
| §2.2 Canonize HDE-EPIC040 source-conflict ADR decisions (261) | Whole change | C040-01–C040-04 decided guidance | Published in PF10 only |
| §2.3 Reconcile superseded core-test instructions (375) | Whole change | C040-05 alternative A: the four-argument core is the only calculator; the comparator orchestrates canonical functions and implements no formula | `docs/ephemeral/HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md` (`071dc0263111b89746b1541b06758f31889c19f1d08a443205cb5ee26e581476`) |
| §2.4 Record in-flight resolution of C040-01 through C040-04 (422) | Whole change | Status record only | `docs/ephemeral/HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md` (`c231f1ff7f254fd6b186dc61074115481591836cdb3ec0affc438e0eb78bb064`) |
| §2.5 Record the approved source-backed Channel taxonomy and existing-state conformance (455) | Whole change | C040-06: the goldens exercise the 36-row taxonomy and 16-case conformance as delivered | `docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md` (`60bbcb2b442fef0798acef35a81ec1947493ecd6d4893b21a0c3040f4cf3d368`) |
| §2.6 PR01 — Accept Source-Proven Catalog and Exact Contract Data (656) | PR01 | Accepted catalog/contract data consumed unchanged | `docs/ephemeral/PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md` (`2b7c817395a307da097d81b49e629955e33fffad42b18d0003df2dbc12cf161d`) |
| §2.7 PR02 — Rescoping (813) | PR02 only | Accepted admission behavior consumed unchanged | `docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md` (`d54fb85ee98fd152f1dfe8e0cc8c09f90989c70d56eacad29ae0d6f6d79057c1`); `…-v2.0.md` (`5ecc9850dc9f4368868ad1e4de15e249193e2bb81421e41095e4aed686c2874d`) |
| §2.8 PF10-FORM-001 (927) | Agent-authored addenda | Form rule only; PR05 authors no addendum | Published in PF10 only |
| §2.9 PR02-F02 — Executing-Code Coherence Rescope (960) | PR02 only | Consumed unchanged | `docs/ephemeral/HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md` (`1c952386cd84eaf8a8aefbb33054b6a902d49ea73aa6f68239f099ad700a25fd`) |
| §2.10 PR02-F03 — Existing Serializer Manifest Binding Refresh (1119) | PR02 only | Consumed unchanged | `docs/ephemeral/HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md` (`896b3f3ab16f7d18ce2ab3de1bb1b6599afb85e349e963a9f52421f3189e46fb`) |
| §2.11 PR02 — Lineage Review v1.0 (1284) | PR02 | Accepted dependency status | Review body `docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md` (`4b8d638c3f0e9232c8c2143fbce9593296f89c5dcc3d6b6da82293f21d5ab5c3`) |
| §2.12 PR03-R02 — Bind Executing Mechanics to the Admitted Release (1369) | Admission boundary | The private admission execution-provenance and executable-equivalence owner in `engine/config/registry_loader.py` stays the owning boundary; PR05 loads every candidate root through `_load_active_mechanics_bundle_from_root`, so the complete check runs; PR05 must not weaken, bypass or relocate it | `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` (`a44659a7754c5f6e10f0bf4a1397d6815aae32ef75a2626a866055a801ba1998`) |
| §2.13 PR03 — Lineage Review v1.0 (1482) | PR03 | `ACCEPTED_FINAL`; order `PR01 → … → PR05 → PR06 → PR07 → OPS01` fixed | `docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` (`07647f68bb5f5a705d8d2196f2aaaca9c17cb2b1c9f8774f8fd2b8268ae7dffa`) |
| §2.14 Specification format authority (1598) | Specification authoring | Not applicable to PR05 engineering | Published in PF10 only |
| **§2.15 PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval (1640)** | PR04; **PR05 covered (line 1726)** | Inherited condition: governed gates and the attestation end `RELEASE_NOT_ADMITTED` on any PR05 candidate; ordinary CI accepts exactly that outcome; PR05 owns none of the enumerated files, must not feed a synthetic release to a governed gate or the attestation, must not bypass admission and must not emit `PR06R_B_FINAL_PASS`; pytest may use the fixture seam (§7 of the instruction) | `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` (`86708f5c32de990be892bbb3f1ced973c5a110e30496753ca871b8f72c8082c1`) |
| §2.16 PR04-F03 deferral (1764); §2.17 PR04-F05 deferral (1841); §2.18 PR04-F07 deferral (1907) | PR07 | Inherited, not fixed by PR05 (§4.3, §12) | `docs/ephemeral/HDE-EPIC040-PR04-F03-deferral-decision-v1.0.md`, `…-F05-…`, `…-F07-…` (§2.1) |
| §2.19 PR04-LINEAGE-001 (1990) | PR04 | PR04 accepted; PR05 is the next planned unit; instruction-stage eligibility only | `docs/ephemeral/HDE-EPIC040-PR04-pr-work-unit-lineage-review-v1.0.md` (`08bff31889c9c76b65cf788826f2a602a388e64c4247eaef7e5ca89df086dba4`) |

### 2.4 GCFPE execution sources

- Governing prompt: `PR-20 — Create Detailed PR Implementation Plan — 091426.1`, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, read completely; reported page revision `2026-09-24T15:46:52.719Z`.
- Register readback: `GCFPE Membership and Release Register` (`https://app.notion.com/p/3d24590a05eb81ce942ad994cfca9fa1`), page last edited `2026-09-23T17:43:39.489Z`: "Selected GCFPE contract: `GCFPE-20260914.1` / `091426.1`, exactly 55 members … Selected 2026-09-21 by Nathan / Product Owner." The hub `HDE IA — GCFPE-20260914.1 — 091426.1` (`https://app.notion.com/p/3db4590a05eb8195a2ccf7c0959a8b6e`) supplies the direct member bindings used in §17.
- Destination prompt for the continuation: `PR-30 — PR Implementation Proceed — 091426.1`, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`, read completely for its input predicates.
- Notion was read only. No Notion page was written; this artifact lands by pull request under `docs/ephemeral/`.

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline re-verified at planning time

- `origin/main` head `cb27bcb603692345064383601bfa2d026d69930e`, tree `63656a11835703fe41acd50f23c731ee77dc5be1`, committed 2026-09-24T18:05:58Z — the merge of #490 (the instruction). Since PR04 landed (`cd6f9e6`), the only changes outside `docs/` are `.github/pull_request_template.md` (new) and `AGENTS.md` (+6 lines); `git diff --stat cd6f9e6 origin/main -- .github/workflows/ci.yml ci/ tools/ engine/ tests/ catalog/ schemas/` is empty. **The executable baseline for PR05 is PR04's landed tree**, exactly as the instruction states.
- No PR05 branch, commit, pull request, Proceed, implementation, review, CI result or merge exists. The working tree was clean before and after every read-only probe below (`git status --short --untracked-files=all` empty).
- Environment used for probes: Python 3.11.15, pytest 8.4.2, CI-equivalent install (`python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`; `hdctl` on PATH), closed rails `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`.

### 3.2 Verified baseline facts that shape this plan

1. **Admission refuses on the real root.** `load_active_mechanics_bundle()` raises `SchemaValidationError` with `code == "INCOMPLETE_RELEASE_ROSTER"`; `ADMITTED_RELEASE_ROSTER` has 44 members, `catalog/manifest.json` has 15 rows. The comparator's application cases therefore refuse truthfully against the repository root until PR06 (§7 of the instruction).
2. **Every PF01 golden value reproduces through the landed canonical code** under the synthetic complete-release fixture root (`tests/config/helpers.py::synthetic_complete_release_root`, admitted through `_load_active_mechanics_bundle_from_root`, `config_id == "m10-channel-state-v1.0.0"`). Observed: G001 all-none injected vector → 20 zeros; G002 all-companionship injected vector → q `[200,200,100,100,150,150,200,200,200,200,200,200,100,100,100,150,100,100,0,200]`, scores `[100,50,75,100,100,100,50,63,50,50]`, bands `[Glow,Warm,Glow,Glow,Glow,Glow,Warm,Warm,Warm,Warm]`; G003 `twice_min_owner_mass_v1` over the six `equilibrium_score` Channels (`02-14, 07-31, 21-45, 26-44, 32-54, 37-40`, weight 1 each) → 200 for a 3/3 owner split and 0 for 6/0; G004 → q `[25,63,0,38,40,20,0,25,50,38,50,0,0,0,50,20,0,60,0,33]`, scores `[22,10,15,6,22,13,0,18,15,8]`, all `Cool`, active states exactly PF01's six; G006 reducer pairs `(48,48)→24 Cool, (50,50)→25 Open, (98,98)→49 Open, (100,100)→50 Warm, (148,148)→74 Warm, (150,150)→75 Glow, (200,200)→100 Glow` (harmony bounds `0..100`, weights `(1,1)`); G007 Reader preimage hash `8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15`; G008 fingerprint `7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b`, pair key under release `a`×64 `8a75eafcc4af664e073c1c4daec55f073f416af2c461039539f01717ac01d501` (through `engine.compat.compute.intrinsic_pair_key`), Reader hash `ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e`; G008 kernel result all zero. **No golden-value disagreement exists at planning time** (instruction §5.1); the PR04 pins `G007_READER_HASH`, `G008_FINGERPRINT`, `G008_PAIR_KEY`, `G008_READER_HASH` in `tests/compat/test_evaluate_pair_eligibility.py:45–48` equal PF01 §9.5.
3. **`compute_core` binds `release_id` to the bundle.** `compute_core(a, b, bundle, "a"*64)` raises `ValueError("invalid pure core contract")` because `_validate_bundle` requires `release_id == bundle.release_id`. PF01's G008 pair key under release `a`×64 is therefore reproducible only through the canonical preimage function `intrinsic_pair_key(lo, hi, config_id=…, release_id="a"*64)` (exactly as PR04 pins it), never by feeding a foreign release identity to the core. The plan's identity checks follow this (§5.1, §5.2).
4. **Kernel entrypoints and shapes.** `engine.magic10.composite._classify_channels(mask_a, mask_b, channels) -> tuple[ChannelClassification(channel_id, state, owner), ...]` (36 rows in registry order); `engine.magic10.signals._compute_signals(classified, mechanics, expected_order)` (requires exactly 36 distinct channel rows) and `_signal_q(operation, channels, classifications, responses=None)`; `engine.magic10.calculators._reduce_category(category_id, (q, q), bounds, weights)`; `engine.core.core.compute_core(member_a, member_b, mechanics_bundle, release_id) -> CoreResult` with `.to_payload()`; `engine.core.core._chart_fingerprint(NormalizedGates)`. Signal order is the concatenation of `registry.magic10_caps[category].inputs` over `registry.magic10_order` (`harmony, heat, communication, alignment, comfort, consistency, expansion, creativity, drive, balance`).
5. **Application entrypoints.** `engine.compat.compute.evaluate_pair(a, b, *, bundle_provider=None, cache=None, router=None)`; `evaluation_party(ResolvedCompatChart(canonical_person_id, mapped_chart, source, user_id, vendor, vendor_version, input_fingerprint))`; `validate_pair_eligibility`, `orient`, `intrinsic_pair_key`, `harmony_band`, `ineligible_self_carrier`; `presenter.reader_v1.emitter.emit_reader_v1(enriched) -> (bytes, envelope)` with `enriched = {eligible, categories:[{id,band}], meta:{engine_tag, invocation_tag}, release_id}`; `engine.runtime.public.emit_reader_public_envelope` delegates to it. A valid self-pair returns `{"categories": [], "eligible": False}` and touches no core, cache, router or pair key; a same-UUID unequal projection raises `CompatBoundaryError(reason="inconsistent_self", token="ERR_READER_INVALID_CHART")`.
6. **The default router mounts a narrative pack into the working tree.** `evaluate_pair` with `router=None` calls `engine.narratives.router.route_keys → engine.narratives.state.get_pack() → load_pack()` whose default `mount_root` is `Path("narratives")` relative to the current directory (PR04 result O-18; PR04 plan C2 "no `narratives/<pack_sha>/` residue"). A non-mutating comparator must therefore pass an explicit router for every application case (§5.2 D-03) and never touch `engine.narratives.state._PACK`.
7. **`DBAccess.readonly_tx` is roster-locked.** `engine/db/providers/psycopg_provider.py::validate_readonly_statements` refuses any batch whose first statement is not `SET TRANSACTION READ ONLY` and whose statement signatures are not exactly the three OPS03 signatures (`readonly_tx_roster_mismatch`). A readiness `SELECT` cannot pass through `readonly_tx` without changing `engine/db`, which is not a PR05 locus and is not pre-authorized. `DBAccess.query` is the plain read path the PR04 production Reader uses (`adapter/http_reader.py:432–439` → `read_current_mapped_bodygraph`, one parameterized `SELECT` on `public.hde_body_graphs_current`, `vendor = 'hdapi'` fixed in the statement). See D-01.
8. **Current-row read path.** `engine.bodygraph.mapped_cache.read_current_mapped_bodygraph(db, canonical_user_id) -> MappedBodyGraphRow | None` refuses a non-canonical UUID (`PROVIDER_INPUT_INVALID`), wraps `AdapterError` as `MappedCacheError("DB_QUERY_FAILED")`, treats `rows is None` as `DB_QUERY_FAILED`, more than one row as `DB_ROW_CONTRACT_VIOLATED`, bad shape/identity/vendor/version/fingerprint as `DB_ROW_CONTRACT_VIOLATED`, non-JSON or non-object payload as `DB_PAYLOAD_INVALID`, and projects the payload through `project_bodygraph`, which applies the shared Gate predicate (`validate_raw_gates → normalize_gates`) and raises `BodyGraphProjectionError(code)` with the normalizer's own codes `GATES_NOT_LIST`, `GATES_EMPTY`, `GATE_VALUE_INVALID`, `GATE_DUPLICATE` or a shape code (`INVALID_SHAPE`, `PERSON_UID_MISMATCH`, …). No second validator is needed or permitted.
9. **CI classifier facts (dry-run through `ci.checks.classify_ci_changes`).** `tests/fixtures/magic10/v1/goldens.json` → lanes `{product, release}` but `changed_test_targets` raises `CI_TEST_SUPPORT_OWNER_MISSING`; `tools/config/artifacts.py` and `generate_config_artifacts.py` → `{evidence, release}` with owners `tests/config/test_config_artifacts.py`, `tests/config/test_typed_bundles.py`; `tools/bodygraph/check_magic10_gate_readiness.py` → `classify_paths` raises `CI_CHANGE_SURFACE_UNCLASSIFIED` and `changed_test_targets` raises `CI_SOURCE_OWNER_TEST_MISSING`; new test modules under `tests/config/` and `tests/bodygraph/` → `{product, release}` and are their own targets; `tests/config/helpers.py` → 12 registered owner targets; `ci/checks/classify_ci_changes.py` → all seven lanes and the 89-target full-validation roster. The candidate must therefore register paths (§6.2) and, because it changes the classifier, runs full validation.
10. **Release-member format for the readiness tool.** `tools/bodygraph/check_magic10_gate_readiness.py` is a member of `ADMITTED_RELEASE_ROSTER`; `_parse_release_member_bytes` accepts a `.py` member only when it is UTF-8 without BOM, has no `\r`, ends with exactly one `\n`, is non-empty and parses with `ast`. `tests/config/helpers.py::_SYNTHETIC_PLACEHOLDERS` currently substitutes a one-line placeholder for this path in the synthetic release root ("Synthetic nonfunctional future-owner placeholder"); no test references the placeholder bytes (grep of `tests/`, `tools/`, `engine/`). See D-02.
11. **PR04 fixture support.** `tests/support/pr04_fixtures.py` provides `complete_chart(uid, gates)`, `build_bundle(tmp_root)`, `build_pack`, `inject_seams`, `RowStore` and `FakeCurrentViewDB` (a `DBAccess` stand-in whose `query` serves the five current-view columns and whose `tx`/`exec` raise). It is registered under `_TEST_SUPPORT_OWNER_PATHS` with 18 owners; PR05 tests may import it without changing it.
12. **Baseline suites.** Under the CI-equivalent install: `tests/config/test_config_artifacts.py` 22 passed; the combined run of `tests/config/test_config_artifacts.py tests/core/test_engine_core_determinism.py tests/core/test_engine_core_abba.py tests/compat/test_evaluate_pair_eligibility.py tests/bodygraph/test_gates.py tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_http_reader_ci_ownership.py` gave 248 passed plus the one `test_config_publication_refuses_another_root` case that failed only before `requirements.txt` was installed (`ModuleNotFoundError` from `adapter/http_reader.py:6`) and passes after it. Not a baseline defect; recorded so PR-30 installs exactly as CI does (§10.1).
13. **Frozen or unaffected homes.** `goldens/reader/v1/*` (legacy Reader identities; F05) is untouched and not consulted for oracle values; `schemas/reader.v1.schema.json` is not used to validate the G007/G008 envelopes (F05 would fail it); `catalog/manifest.json` is untouched (PR06); no governed evidence family is declared for the comparator or the readiness tool (PF12 checked; instruction §8.4), so no writer run, no Index/Mirror row and no updater transaction is planned.
14. **Notion timestamps.** The fetch tool reports page revisions ("as of" and `page_last_edited_at`) that read about two hours behind this container's UTC clock; they are recorded as reported, not corrected.

## 4. Exact objective, completion conditions and exclusions

### 4.1 Objective (Plan §6.5; instruction §4)

Deliver the complete deterministic, non-mutating golden comparison capability and the current-row Gate-readiness tool.

### 4.2 Completion conditions

1. `tests/fixtures/magic10/v1/goldens.json` holds exactly M10-G001–G008 with explicit case type, full PF01 §9.5 metadata and synthetic UUIDs, in canonical JSON bytes (§5.1).
2. The comparator (§5.2) runs all eight cases through the canonical entrypoints for their type, compares every field, order, identity and byte, reports every mismatch deterministically, refuses membership/type/admission defects as refusals, and is structurally unable to reach any write, activation or generation helper (AST proof + runtime spies).
3. The readiness tool (§5.3) enumerates only the explicitly selected current rows through `DBAccess`, applies the shared Gate predicate through the existing projection, performs no `UPDATE`/`INSERT`/`DELETE`, no acquisition, no auto-repair, no backfill and no vendor call, treats unavailable or denied data as `READINESS_UNAVAILABLE` and an empty selection as `READINESS_EMPTY_SELECTION` (never ready), and emits identity-safe aggregate diagnostics with no birth tuple, Gate payload, chart, person label or UUID.
4. `ci/checks/classify_ci_changes.py` classifies every PR05 path with owner targets (§6.2); `tests/config/helpers.py` copies the real readiness tool into the synthetic release root (D-02).
5. All focused suites (§8), the classifier dry-run, the changed-test isolation step and the seven lanes (§10) pass locally on the candidate head, with the F01-defined `RAILS_LANE:RELEASE_NOT_ADMITTED` and `RELEASE_LANE:RELEASE_NOT_ADMITTED` outcomes and a clean tree; the PR-30 result record (§9, §10.6) is written and read back.
6. **Not part of completion**: a live current-row readiness verdict, any QA PASS, the comparator against the real repository root succeeding (it refuses with `INCOMPLETE_RELEASE_ROSTER` until PR06), release admission, PF09 movement.

### 4.3 Hard exclusions

PR06 (complete release admission, 44-member manifest, promotion, evidence convergence including the sanity log's `NOT_ADMITTED → PASS` transition), PR07 (DOC-10 documentation; F03, F05, F07), OPS01 (final external verification); any live DB or vendor operation; any write to a database; independent QA; Ops; deployment; PF10 edit or numbering; Canon drainage; PF09 movement; Epic closure; any change to `engine/**`, `catalog/**`, `schemas/**`, `migrations/**`, `adapter/**`, `presenter/**`, `.github/workflows/ci.yml`, `ci/jobs/**`, `tools/evidence/**`, `docs/pfcanon/**`, generated evidence, `goldens/reader/v1/*`; any new acceptance token, Machine Mirror key or evidence family; any `[skip ci]` directive.

## 5. Designed interfaces, invariants and contracts

### 5.1 Golden fixture — `tests/fixtures/magic10/v1/goldens.json`

**Bytes.** Canonical JSON per PF12 §4.1, produced by `engine.serializer.canon.sercanon(payload, sort_keys=True)`: UTF-8, no BOM, ASCII-sorted keys at every level, compact separators, exactly one trailing LF, integers only. Array order is schema-declared and preserved (cases, signals, categories, channel states, scenarios, pairs). The fixture is input data only: not a manifest member, not an Index/Mirror entry, not a formula, not a `config.magic10` payload.

**Top level (closed keys):** `schema` = `"magic10_goldens.v1"`; `source` = `{"document": "PF01-Canon-HDE-Math-Spec", "version": "1.3.7", "section": "9.5 Canonical Magic10 v1 goldens", "sha256": "101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a"}`; `constants` = `{"release_id": "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "config_id": "m10-channel-state-v1.0.0", "meta": {"engine_tag": "m10-test", "invocation_tag": "m10-identity-boundary"}, "uuid_1": "00000000-0000-0000-0000-000000000001", "uuid_2": "00000000-0000-0000-0000-000000000002", "uuid_3": "00000000-0000-0000-0000-000000000003", "uuid_4": "00000000-0000-0000-0000-000000000004", "synthetic_projection_fields": {"authority": "Emotional", "birthDateUtc": "2000-01-01T00:00:00Z", "centers": ["Ajna", "Solar Plexus"], "channelsLong": ["10-20"], "channelsShort": ["34-20"], "definition": "Single", "profile": "1/3", "strategy": "Wait to Respond", "type": "Manifesting Generator"}, "router_stub": {"personal_lo_to_hi": "m10.test.personal.lo_to_hi", "personal_hi_to_lo": "m10.test.personal.hi_to_lo", "shared": "m10.test.shared.equal_mask"}}`; `cases` = the eight case objects in order.

**Every case (closed keys):** `case_id` (`M10-G001`…`M10-G008`), `title` (PF01 heading text), `case_type` (`"kernel"` | `"application"`), `kind` (kernel: `"signal_vector"` | `"signal_operation"` | `"reducer"` | `"core"`; application: `"evaluate_pair"`), `realizable_chart_claim` (`false` for G001, G002, G003, G006; `true` for G004; `null` for application cases), `input_provenance` (a non-empty array of tags from the closed vocabulary `"pf01_9_5"` — PF01 states the input; `"synthetic_projection_fields"` — G005, G007, G008 carry the declared synthetic chart fields; `"fixture_selected_within_pf01_rule"` — G006's concrete pairs and G005's UUID and Gate-set assignment), `inputs`, `expected`. Unknown keys refuse.

**Case contents (transcribed from PF01 §9.5, lines 1859–2018; nothing invented beyond the declared synthetic fields):**

| Case | `kind` | `inputs` | `expected` |
| --- | --- | --- | --- |
| M10-G001 no relationship Channels | `signal_vector` | `channel_states`: 36 rows `{channel_id, state: "none", owner: null}` in ASCII channel-ID order (the registry's 36 IDs) | `signals`: 20 rows `{signal_id, q: 0}` in signal order; `categories`: 10 rows `{category_id, score: 0, band: "Cool"}` in category order |
| M10-G002 homogeneous companionship kernel fixture | `signal_vector` | 36 rows `state: "companionship", owner: null` | `signals` q `[200,200,100,100,150,150,200,200,200,200,200,200,100,100,100,150,100,100,0,200]` (PF01 §5.2 profile responses for `companionship`: activation 100, coherence 200, expression 150 half-units; Balance per §9.5: `equilibrium_score` 0, `counterweight_ratio` 200); `categories` scores `[100,50,75,100,100,100,50,63,50,50]`, bands `[Glow,Warm,Glow,Glow,Glow,Glow,Warm,Warm,Warm,Warm]`; `balance_note`: "equilibrium_score receives no one-owner mass while counterweight_ratio is 100" |
| M10-G003 Balance ownership split | `signal_operation` | `signal_id: "equilibrium_score"`, `operation: "twice_min_owner_mass_v1"`, `channels`: `[{channel_id, weight: 1}]` for `02-14, 07-31, 21-45, 26-44, 32-54, 37-40`; `scenarios`: `split_3_3` (first three owned by `member_lo`, last three by `member_hi`, state `dominance`), `all_member_lo`, `all_member_hi` | per scenario `q`: 200, 0, 0; `swap_invariant: true` (owners swapped → same q) |
| M10-G004 sparse end-to-end Gate sets | `core` | `member_a_gates: [5,19,20,34,43,49]`, `member_b_gates: [9,12,15,22,23,52]` | `channel_states`: 36 rows — `05-15` electromagnetic/null, `09-52` dominance/`member_hi`, `12-22` dominance/`member_hi`, `19-49` dominance/`member_lo`, `20-34` dominance/`member_lo`, `23-43` electromagnetic/null, all others none/null (PF01's "dominance by B/A" mapped to the numerically ordered members: B's mask is `hi`, A's is `lo`); `signals` q `[25,63,0,38,40,20,0,25,50,38,50,0,0,0,50,20,0,60,0,33]`; `categories` scores `[22,10,15,6,22,13,0,18,15,8]`, all `Cool`; `ab_ba_identity: true`; `two_run_identity: true`; `identities`: `{"schema": "magic10_result.v1", "config_id_matches_candidate": true, "release_id_matches_candidate": true, "pair_key_hex64": true}` |
| M10-G005 identity independence | `evaluate_pair` | `pairs`: `[{a: uuid_1, b: uuid_2}, {a: uuid_3, b: uuid_4}]`, each with `member_a_gates`/`member_b_gates` = G004's sets and the synthetic projection fields; `router_stub` reference | `pair_key_equal_across_pairs: true`; `intrinsic_bytes_equal_across_pairs: true` over `{schema, config_id, release_id, pair_key, signals, categories[category_id, score, band]}`; intrinsic `signals`/`categories` equal G004's expected vectors; `nonclaim`: "eligibility, directional narrative orientation and public Reader bytes are not asserted identity-independent" |
| M10-G006 category boundary matrix | `reducer` | `category_id: "harmony"`, `pairs`: `[[48,48],[50,50],[98,98],[100,100],[148,148],[150,150],[200,200]]` | per pair `score`/`band`: `24 Cool, 25 Open, 49 Open, 50 Warm, 74 Warm, 75 Glow, 100 Glow`; `bounds_and_weights_from_candidate: true` |
| M10-G007 valid self-pair boundary | `evaluate_pair` | `a: {id: uuid_1, gates: [1]}`, `b: {id: uuid_1, gates: [1]}`, byte-identical complete projections (synthetic fields), `release_id: a×64`, `meta`; `adverse`: `[{id: "unequal_projection_same_uuid", mutate: {party: "b", field: "bodygraph.profile", value: "2/4"}}]` | `eligible: false`; `evaluate_pair_result: {"categories": [], "eligible": false}`; `core_cache_router_called: false`; `no_pair_key: true`; `reader_categories: []`; `reader_idempotence_hash: "8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15"`; `reader_two_run_and_ab_ba_identical: true`; `not_an_error: true`; adverse expected `{token: "ERR_READER_INVALID_CHART", reason: "inconsistent_self", success_body: false, pair_key_created: false}` |
| M10-G008 distinct people with equal Gate masks | `evaluate_pair` | `a: {id: uuid_1, gates: [1]}`, `b: {id: uuid_2, gates: [1]}`, synthetic fields, `release_id`, `meta`, `router_stub` | `eligible: true`; `gate_mask_hex: "0000000000000001"` each; `chart_fingerprint: "7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b"` each; `pair_key_under_release: {"config_id": "m10-channel-state-v1.0.0", "release_id": a×64, "pair_key": "8a75eafcc4af664e073c1c4daec55f073f416af2c461039539f01717ac01d501"}`; `channel_states`: all 36 none; `signals` all q 0; `categories` all score 0 `Cool`; `orientation: {lo: uuid_1, hi: uuid_2}`; `router_keys: {personal_lo_to_hi_key, personal_hi_to_lo_key, shared_key}` = the stub values on every category row; `reversed_order_bytes_identical: true`; `reader: {eligible: true, categories: [{"id": "harmony", "band": "Cool"}], idempotence_hash: "ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e", hash_independent_of_pair_key: true, hash_equals_sha256_of_preimage_bytes: true}` |

`realizable_chart_claim: false` records PF01's own statements for G002, G003 and G006; G001's all-none vector is likewise an injected kernel vector. G004's "dominance by A/B" is stored in member terms (`member_lo`/`member_hi`) because that is the kernel's vocabulary; the comparator derives them from the numerically ordered masks (`orient`-equivalent `sorted((mask_a, mask_b))` inside `_classify_channels`).

### 5.2 Comparator — `tools/config/artifacts.py` and `tools/config/generate_config_artifacts.py`

**Public API (in `tools/config/artifacts.py`):**

```text
compare_goldens(candidate_root: Path, goldens_path: Path) -> GoldenComparison
render_golden_report(result: GoldenComparison) -> bytes          # canonical JSON, one LF
class GoldenComparisonRefusal(RuntimeError): code: str            # e.g. "GOLDENS_INVALID"
@dataclass(frozen=True) class GoldenComparison:
    schema = "magic10_golden_comparison.v1"; candidate_root: str (relative-safe display only);
    goldens_sha256: str; candidate_release_id: str; config_id: str;
    cases: tuple[CaseOutcome, ...]      # (case_id, kind, outcome "match"|"mismatch", observed, expected)
    mismatches: tuple[Mismatch, ...]    # (case_id, path, expected, actual), deterministic order
    ok: bool                            # all eight match
```

**Invariants:**

1. `require_closed_rails()` first (the tooling home's determinism rails; read-only itself).
2. **Inputs validated before anything runs.** `candidate_root` must be an existing directory, not a symlink, absolute after `os.path.abspath`; `goldens_path` must be a regular non-symlink file whose bytes equal `sercanon(json.loads(bytes), sort_keys=True)` (canonical identity) and whose document satisfies the closed schema of §5.1, else `GOLDENS_INVALID`. Membership: exactly the eight `case_id`s in order; a missing, duplicate or unknown case → `GOLDENS_MEMBERSHIP_INVALID`; a `case_type`/`kind` pair outside the declared table → `GOLDENS_CASE_TYPE_INVALID`.
3. **Admission** through `engine.config.registry_loader._load_active_mechanics_bundle_from_root(candidate_root)` exactly once; any `SchemaValidationError` (including `INCOMPLETE_RELEASE_ROSTER` on the real root, `MANIFEST_MEMBER_HASH_MISMATCH`, `EXECUTING_SOURCE_MISMATCH`, …) → `GoldenComparisonRefusal("CANDIDATE_ADMISSION_REFUSED:<code>")`. A refusal is never equality. A fixture candidate's success is test-only and is never release admission.
4. **Execution per kind** (the comparator orchestrates; every number comes from canonical code):
   - `signal_vector`: build `ChannelClassification` rows from the fixture; refuse (mismatch) if the row IDs are not exactly the candidate registry's 36 IDs; `_compute_signals(rows, bundle.mechanics, signal_order)`; then for each category in `registry.magic10_order`, `_reduce_category(category, (q_a, q_b), caps.bounds, tuple(weights))` with the candidate's caps/weights; observed = ordered `signals` + `categories`.
   - `signal_operation`: locate the candidate signal definition by `signal_id`; observed includes the candidate's `operation` and `channels` (compared to the fixture); per scenario `_signal_q(operation, channels, rows)`; swap owners and recompute.
   - `reducer`: candidate caps/weights for `category_id`; `_reduce_category` per pair.
   - `core`: `normalize_gates` both; `_classify_channels(a.mask, b.mask, registry.channels)`; `compute_core(a, b, bundle, bundle.release_id)` twice (two-run) and reversed (AB/BA); observed = channel states, `to_payload()` signals/categories, identity checks (`schema`, `config_id == bundle.mechanics["config_id"]`, `release_id == bundle.release_id`, 64-hex `pair_key`, AB/BA and two-run byte identity of `sercanon(payload)`).
   - `evaluate_pair`: build each party with `evaluation_party(ResolvedCompatChart(uuid, chart, "resolved", None, None, None, None))` where `chart = {"bodygraph": {synthetic fields…, "gates": [...]}, "person": {"person_uid": uuid}, "person_uid": uuid}`; call `evaluate_pair(a, b, bundle_provider=lambda: bundle, router=stub)` with the fixture router stub (D-03); observed per case as in §5.1 (eligibility carrier, `orient`, `intrinsic_pair_key` under the fixture's `release_id`/`config_id` and under the candidate's, `_classify_channels` on the party masks, router key occupancy, `sercanon` byte identity for reversed order and two runs, Reader envelope via `emit_reader_v1({"eligible", "categories": [{"id": "harmony", "band": harmony_band(result)}] if eligible else [], "meta", "release_id"})`, `hashlib.sha256(sercanon(preimage)).hexdigest()` recheck, `idempotence_hash != pair_key`); for G007's adverse variant, `evaluate_pair` must raise `CompatBoundaryError` with the expected `reason`/`token` and no result.
5. **Comparison.** Observed and expected are compared as canonical bytes (`sercanon(observed) == sercanon(expected)`) and as a recursive leaf diff; every differing leaf becomes one `Mismatch(case_id, path, expected, actual)`; missing/extra keys are mismatches; no early exit; results are sorted by `(case_id, path)`. Refused admission, source/config/manifest incoherence and structural surprises are never reported as equality.
6. **Read-only, structurally.** The compare implementation (function `compare_goldens` and helpers prefixed `_golden_`) references none of `write_magic10_config`, `write_band_edges`, `_publish_prepared`, `generate_config_artifacts`, `publish_config_family`, `generate_catalog_logs`, `_ConfigWriteTransaction`, `update_evidence_index`, `_publish_staged`, `cut_release_manifest`; it opens files read-only, writes nothing under `candidate_root`, the repository root or the goldens path, never modifies an expected value, never repairs a mismatch, never activates a candidate, never sets `compute._BUNDLE_PROVIDER` or `narrative_state._PACK`, never calls `route_keys`/`get_pack`/`load_pack`. Proven by the AST guard and runtime spies in §8.1.

**CLI (in `tools/config/generate_config_artifacts.py`)** — the new spelling proposed under Plan §5.9:

```text
python tools/config/generate_config_artifacts.py --compare-goldens <CANDIDATE_ROOT> [--goldens PATH] [--report PATH]
```

- `--compare-goldens` joins the existing mutually exclusive mode group with `--check` and `--publish-family`; `--allow-aliases` with it is a `parser.error`; `--goldens` defaults to `<repository root>/tests/fixtures/magic10/v1/goldens.json`; `--report` writes the complete canonical report (match or mismatch) atomically (temp file + `os.replace`) to a path that is not inside the candidate root or the repository root, is not a symlink and whose parent exists, else `REPORT_PATH_INVALID`.
- Exit and streams (PF05 §3.4 discipline): `0` — all eight match: the canonical report on stdout, stderr empty; `1` — one or more mismatches: stdout empty, stderr exactly one line `GOLDEN_COMPARISON_MISMATCH:<count>` (the details are in the API result and in `--report`); `5` — refusal: stdout empty, stderr exactly one line with the refusal token (`GOLDENS_INVALID`, `GOLDENS_MEMBERSHIP_INVALID`, `GOLDENS_CASE_TYPE_INVALID`, `CANDIDATE_ROOT_INVALID`, `CANDIDATE_ADMISSION_REFUSED:<code>`, `REPORT_PATH_INVALID`, `RAILS_CLOSED_REQUIRED:<missing>`); argparse usage errors keep the parser's existing exit (`2`).
- The dispatch branch in `_main` calls only `artifacts.compare_goldens`, `artifacts.render_golden_report` and the report writer; it never reaches `generate_config_artifacts`, `check_config_artifacts` or `publish_config_family`.
- Against the repository root on `main` today the CLI ends `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` at exit 5 — the truthful result under PF10 §2.15, not a PR05 defect and not a golden mismatch.

### 5.3 Readiness — `tools/bodygraph/check_magic10_gate_readiness.py`

**Contract:**

```text
python tools/bodygraph/check_magic10_gate_readiness.py (--user-id <canonical-uuid>)... | --selection-file PATH
```

- **Selection.** Explicit canonical UUIDs only (`engine.bodygraph.projection.strict_canonical_uuid`), from repeated `--user-id` and/or `--selection-file` (one per line, `#` comments and blank lines ignored). The selection is deduplicated-checked (a repeated UUID is `READINESS_SELECTION_INVALID`), sorted, and bounded by its own size — no "all rows" mode, no `LIMIT`, no scanning. An empty selection is `READINESS_EMPTY_SELECTION`.
- **Access.** `DBAccess.for_current_env()` (`DATABASE_URL` is the only transport configuration; retired bridge keys are refused by the adapter). `PrimaryUnavailable`, `RetiredBridgeConfiguration` and any `AdapterError` → `READINESS_UNAVAILABLE`. The tool never opens rails, never reads `HD_API_KEY`/`GEO_API_KEY`, never imports `engine.bodygraph.resolver`, `vendor_client`, `ingest`, `psycopg` or `mapped_cache.persist_mapped_bodygraph` (import-purity test).
- **Read path.** For each selected UUID in sorted order, `read_current_mapped_bodygraph(db, uid)` — one parameterized read-only `SELECT` on `public.hde_body_graphs_current` with `vendor = 'hdapi'` fixed (D-01). Outcomes: row → `ready`; `None` → `missing`; `MappedCacheError("DB_ROW_CONTRACT_VIOLATED", …more than one row…)` → `duplicate`; other `DB_ROW_CONTRACT_VIOLATED` → `row_invalid`; `DB_PAYLOAD_INVALID` → `payload_invalid`; `BodyGraphProjectionError` with a Gate-ingress code (`GATES_NOT_LIST`, `GATES_EMPTY`, `GATE_VALUE_INVALID`, `GATE_DUPLICATE`) → `gates_invalid`; any other `BodyGraphProjectionError` → `payload_invalid`; `DB_QUERY_FAILED` or an `AdapterError` at any point → abort the run as `READINESS_UNAVAILABLE` (no partial report, never all-ready). The shared Gate predicate is `normalize_gates` via `project_bodygraph`; the tool adds no validator.
- **Verdict.** `READY` iff every requested UUID is `ready`; otherwise `NOT_READY`. Neither is inferred from an unavailable dataset.
- **Report** (stdout, canonical JSON via `engine.serializer.canon.sercanon`, exactly one LF, exit 0):

```text
{"schema":"magic10_gate_readiness.v1","readiness":"READY"|"NOT_READY","provider":"<db.provider_name>","read_only":true,
 "selection":{"requested":N,"sha256":"<sha256 of sercanon(sorted requested UUIDs)>"},
 "counts":{"ready":n,"missing":n,"duplicate":n,"row_invalid":n,"payload_invalid":n,"gates_invalid":n},
 "diagnostics":[{"code":"<MappedCacheError or BodyGraphProjectionError code>","count":n}, ... ASCII-sorted by code]}
```

  No UUID, birth tuple, Gate payload, chart, person label, DSN, environment value or timestamp appears in stdout, stderr or logs. Two runs over the same fake rows are byte-identical.
- **Exit and streams:** `0` report (READY or NOT_READY); `5` refusal with one stderr token line: `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE`; argparse usage errors keep the parser's exit (`2`). The tool never exits `3`, so the F01 `RELEASE_NOT_ADMITTED` exit-code convention cannot be confused with it (R-07).
- **Offline only in this unit.** Fake-DB tests prove behavior. Current production rows are unobserved; an actual live readiness claim requires separately authorized observation outside PR05 (Plan §5.9; instruction §5.3).
- **Member format.** The file is UTF-8 without BOM, LF-only, exactly one final LF, valid Python (§3.2 item 10), because it is a promoted release input that PR06 will materialize.

### 5.4 Failure tokens

All new tokens are tool-local, numeric-free, LF-terminated single lines on stderr; none is a PF05 §5.2 public error token, none is an acceptance token, none maps to an HTTP surface. They are: `GOLDEN_COMPARISON_MISMATCH:<n>`, `GOLDENS_INVALID`, `GOLDENS_MEMBERSHIP_INVALID`, `GOLDENS_CASE_TYPE_INVALID`, `CANDIDATE_ROOT_INVALID`, `CANDIDATE_ADMISSION_REFUSED:<code>`, `REPORT_PATH_INVALID`, `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID`, `READINESS_UNAVAILABLE`. Existing `RAILS_CLOSED_REQUIRED:<…>` is reused unchanged.

## 6. Exact file and component plan

### 6.1 Owned loci (instruction §6.1)

| Path | Change | Content |
| --- | --- | --- |
| `tests/fixtures/magic10/v1/goldens.json` | new | §5.1, canonical bytes |
| `tools/config/artifacts.py` | changed | `compare_goldens`, `render_golden_report`, `GoldenComparison`, `CaseOutcome`, `Mismatch`, `GoldenComparisonRefusal`, `_golden_*` helpers (§5.2); existing write helpers untouched |
| `tools/config/generate_config_artifacts.py` | changed | `--compare-goldens`, `--goldens`, `--report` (§5.2); existing modes untouched; module docstring/help updated |
| `tools/bodygraph/check_magic10_gate_readiness.py` | new | §5.3 with `main(argv) -> int` and `if __name__ == "__main__": raise SystemExit(main())`; no `tools/bodygraph/__init__.py` (the `tools/cli/` precedent imports through the implicit namespace subpackage and the 44-member roster names only this file) |
| `tests/config/test_golden_comparison.py` | new | §8.1 |
| `tests/bodygraph/test_check_magic10_gate_readiness.py` | new | §8.2 |
| `tests/config/helpers.py` | changed (D-02) | remove the `tools/bodygraph/check_magic10_gate_readiness.py` entry from `_SYNTHETIC_PLACEHOLDERS` so the synthetic release root copies the real member bytes; keep the dictionary and the copy loop |
| `docs/config_and_bundles.md` | changed (one sentence) | names the `--compare-goldens` read-only mode next to the existing generator sentence (line 4); classifies `documentation_only`; PR07/DOC-10 owns any fuller documentation |

### 6.2 Necessary dependents — `ci/checks/classify_ci_changes.py` (instruction §6.3; coherence registration, no gate semantics)

| Registration | Exact change |
| --- | --- |
| `_TEST_SUPPORT_OWNER_PATHS` | add `"tests/fixtures/magic10/v1/goldens.json": ("tests/config/test_golden_comparison.py",)` |
| `_CONFIG_WRITER_TEST_OWNERS` | append `"tests/config/test_golden_comparison.py"` to the tuples for `tools/config/artifacts.py` and `tools/config/generate_config_artifacts.py` |
| new `_BODYGRAPH_TOOL_TEST_OWNERS` | `{"tools/bodygraph/check_magic10_gate_readiness.py": ("tests/bodygraph/test_check_magic10_gate_readiness.py",)}` |
| new `_bodygraph_tool_owner_targets(repo_root, path)` | for `tools/bodygraph/*.py`: registered → `_validated_owner_targets(..., error_code="CI_BODYGRAPH_TOOL_OWNER_TEST_INVALID")`; unregistered → `raise ValueError(f"CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING:{path}")` (fail closed, like `_qa_tool_owner_targets`); wired into `changed_test_targets` beside `_qa_tool_owner_targets` |
| `_registered_owner_test_paths` | include `_BODYGRAPH_TOOL_TEST_OWNERS` values so full validation runs the new owner (the two new test modules are then members of `_full_validation_test_targets()` automatically: 89 → 91) |
| `_lanes_for_path` | before the final `return None`: `if path.startswith("tools/bodygraph/"): return {"db", "product", "release"}` (a `DBAccess` consumer, an engine consumer, and a promoted release input per PF12 line 1733) |
| Unchanged | `_FULL_VALIDATION_*`, `_DOCUMENTATION_PREFIXES`, `_FIXED_LANE_TEST_PROVIDERS`, `_FIXED_LANE_TEST_DIRECTORIES` (the new tests must stay ordinary changed-test targets; registering them as fixed-lane providers without a `ci.yml` list entry would silence them), PR04 registrations, `_RELEASE_IMPLEMENTATION_PATHS` |

Every owner target must exist as a regular file at the candidate head (`_validated_owner_targets`), so the new test modules land in the same commit as their registrations. `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_http_reader_ci_ownership.py`, `tests/qa/test_qa_tool_ownership.py` and `tests/evidence/test_rails_ci_workflow_integration.py` must keep passing unchanged; the new rules are pinned by the ownership assertions in §8.2 and §8.1.

### 6.3 Evidence families

None is declared for the comparator or the readiness tool (PF12 checked; instruction §8.4). PR05 regenerates no governed artifact, runs no evidence writer, adds no Index/Mirror row, hash sentinel, path proof, acceptance token or Machine Mirror key, and does not touch `catalog/manifest.json`. The evidence for `AC040-06`/`-07`/`-09` is the PR test and CI record with exact source commit and test identity (§10.6). Frozen families stay frozen with their nonclaims.

### 6.4 Consequence for CI lanes (instruction §6.4)

Because `ci/checks/classify_ci_changes.py` is a `_FULL_VALIDATION_PATHS` member, the PR05 candidate runs full validation: all seven lanes, the changed-tests isolation step over the full-validation roster plus every changed test, and the exact-head summary `CI_APPLICABILITY_AND_EXACT_HEAD_OK`. The rails lane ends `RAILS_LANE:RELEASE_NOT_ADMITTED` and the release lane `RELEASE_LANE:RELEASE_NOT_ADMITTED` (F01, PF10 §2.15) — accepted outcomes keyed on the observed non-admitted state, not waivers. PR05 touches none of the F01 enumerated files.

### 6.5 Explicitly unchanged paths

`engine/**` (including `engine/db/**`, `engine/bodygraph/mapped_cache.py`, `engine/config/registry_loader.py`, `engine/core/**`, `engine/magic10/**`, `engine/compat/**`, `engine/narratives/**`), `catalog/**`, `schemas/**`, `migrations/**`, `adapter/**`, `presenter/**`, `goldens/**`, `.github/workflows/ci.yml`, `ci/jobs/**`, `ci/checks/*` other than the classifier, `tools/evidence/**`, `tools/cli/**`, `tests/support/pr04_fixtures.py`, `tests/compat/test_evaluate_pair_eligibility.py` (its pins are consumed, not edited), `tests/core/**`, `tests/evidence/**`, `docs/pfcanon/**`, all generated evidence, `docs/evidence/**`, `artifacts/**`, `audit/**`.

## 7. Requirement-to-change-and-test mapping

| Requirement / criterion (instruction §8.1) | PR05 change | Deciding tests |
| --- | --- | --- |
| `K040-REQ-010` exact read-only comparison through canonical homes; no second implementation; changed/invalid inputs, wrong identities, incomplete coverage and genuine mismatches cannot report equality | §5.1 fixture; §5.2 comparator and CLI | §8.1 positive 8/8, altered field/order/byte/identity → every mismatch reported, membership/type refusals, admission refusal ≠ equality, AST guard, spies, non-mutation snapshots |
| `K040-REQ-011` deterministic identity/comparison evidence; read-only current-row readiness that modifies no row, acquires no vendor data, backfills nothing and never represents unavailable as ready | §5.3 tool | §8.2 rows matrix, empty/invalid selection, denied/unavailable, spies, no-leak, determinism |
| `K040-REQ-001` ordered chain portion | PR05 consumes PR01–PR04 unchanged; PR06 follows | §8.1 uses only landed seams; §6.5 unchanged paths |
| `K040-REQ-008` refusal matrix portion | refusal tokens §5.4; fail-closed readiness | §8.1 refusals; §8.2 unavailable/never-ready |
| `K040-REQ-012` evidence portion | PR test and CI record; no invented family | §10.6 result record |
| `K040-REQ-013` exact identities | fixture pins PF01 values verbatim; identities compared through canonical functions; no new tokens | §8.1 agreement test against PF01 literals |
| `AC040-06` complete golden and non-mutation | §5.1–5.2 | §8.1 |
| `AC040-07` read-only readiness capability | §5.3 | §8.2 |
| `AC040-08` evidence coherence | no governed artifact changed; CI record | §10 |
| `AC040-09` read-only boundary | structural non-reachability; no public surface change | §8.1 AST + spies; §8.2 import purity |

Obligations owned by PR06, PR07 or OPS01 are not claimed.

## 8. Detailed test design

### 8.1 `tests/config/test_golden_comparison.py`

Fixtures: module-scoped `bundle_root = synthetic_complete_release_root(tmp_path_factory.mktemp("pr05-goldens"))`; `goldens = ROOT / "tests/fixtures/magic10/v1/goldens.json"`; closed rails via `monkeypatch.setenv`; a `snapshot(root)` helper (`{relative path: sha256}` over every regular file plus the goldens bytes).

1. **Fixture bytes and agreement.** Bytes equal `sercanon(json.loads(bytes))`; final LF, no CRLF, no BOM; exactly eight `case_id`s in order; the G007/G008 constants equal the PF01 §9.5 literals (`8214324e…`, `7567338a…`, `8a75eafc…`, `ae435ccc…`) — the same values `tests/compat/test_evaluate_pair_eligibility.py` pins — and G004/G002 vectors equal PF01's tables.
2. **Positive.** `compare_goldens(bundle_root, goldens)` → `ok is True`, eight `match` outcomes, zero mismatches, `candidate_release_id == bundle.release_id`, `config_id == "m10-channel-state-v1.0.0"`; per case the observed record carries the PF01 values (assert a representative field per case, including G004 channel states, G007 `evaluate_pair_result`, G008 `pair_key_under_release`).
3. **Every mismatch is reported.** For a copied goldens document in `tmp_path`: alter one signal q (G004), reorder two category rows (G002), change one byte of the G008 Reader hash, change a G008 UUID so orientation flips, change a G007 hash — each yields exactly the expected `Mismatch` paths; a document with several alterations reports all of them (count and sorted order asserted); `ok is False`.
4. **Refusals.** Missing G006 → `GOLDENS_MEMBERSHIP_INVALID`; duplicate G003 → same; unknown `M10-G009` → same; G004 relabeled `application` → `GOLDENS_CASE_TYPE_INVALID`; non-canonical bytes (pretty-printed, or CRLF, or two final LFs) → `GOLDENS_INVALID`; unknown top-level key → `GOLDENS_INVALID`; symlinked goldens path → `GOLDENS_INVALID`; candidate root with one roster member removed → `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER`; one member's bytes changed after the manifest was cut → `CANDIDATE_ADMISSION_REFUSED:MANIFEST_MEMBER_HASH_MISMATCH`; the repository root itself → `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER` (truthful under F01; asserted as refusal, never as a mismatch of golden values); non-directory or symlinked candidate root → `CANDIDATE_ROOT_INVALID`.
5. **Non-mutation.** Snapshots of the candidate root and goldens are identical before and after the positive run, the multi-mismatch run and each refusal run; `git status --short --untracked-files=all` of the repository is empty after all runs; no `narratives/` directory appears under the repository root or the test cwd; `narrative_state._PACK` is unchanged.
6. **Spies.** With `monkeypatch` raising `AssertionError` on `artifact_tools.write_magic10_config`, `write_band_edges`, `_publish_prepared`, `config_tools.generate_config_artifacts`, `check_config_artifacts`, `publish_config_family`, `generate_catalog_logs`, `tools.evidence.update_evidence_index._publish_staged`, `engine.narratives.router.route_keys`, `engine.narratives.state.get_pack` and `engine.narratives.loader.load_pack`, the positive, mismatch and refusal runs complete without touching any of them; `compute._BUNDLE_PROVIDER` is still `load_active_mechanics_bundle` afterwards.
7. **AST structural guard.** Parse `tools/config/artifacts.py`; collect `compare_goldens` and every module function reachable from it by name; assert the forbidden set of §5.2 invariant 6 appears in none of their bodies; parse `_main` in `generate_config_artifacts.py` and assert the `compare_goldens` branch's call names ⊆ `{compare_goldens, render_golden_report, _write_golden_report, print/sys.stdout.buffer.write}`.
8. **CLI.** In-process `config_tools.main([...])` with `capsys`: match → exit 0, stdout bytes equal `render_golden_report(...)` and end with one LF, stderr empty; mismatch (tmp goldens) → exit 1, stdout empty, stderr exactly `GOLDEN_COMPARISON_MISMATCH:<n>\n`; refusal → exit 5 and the token line; `--report` under `tmp_path` receives the canonical report for match and mismatch runs (every mismatch present); `--report` inside the candidate root or repository root → `REPORT_PATH_INVALID`; `--compare-goldens --allow-aliases` → parser error; rails unset → `RAILS_CLOSED_REQUIRED:` token, nothing run.
9. **Determinism.** Two positive runs produce byte-identical reports; a run against a second identical synthetic root yields the same report except `candidate_root`.
10. **Classifier coherence.** `classifier.changed_test_targets(ROOT, ["tests/fixtures/magic10/v1/goldens.json"])` resolves to this module; `classifier._config_writer_owner_targets(ROOT, "tools/config/artifacts.py")` includes this module.

### 8.2 `tests/bodygraph/test_check_magic10_gate_readiness.py`

Fixtures: `FakeCurrentViewDB` from `tests/support/pr04_fixtures.py` (unchanged) plus small local subclasses for `duplicate` (returns two rows), `malformed` (non-JSON payload; payload missing keys; `person_uid` mismatch), `failing` (`SqlExecError`), `none_result` (returns `None`); `monkeypatch.setattr(readiness.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: fake))`; closed rails; `DATABASE_URL` deleted by default.

1. **Good rows** → exit 0, `readiness == "READY"`, counts `ready == requested`, `diagnostics == []`, `selection.sha256` equals `sha256(sercanon(sorted uuids))`, output has exactly one LF.
2. **Bad rows matrix** (each with a good row alongside): empty Gate list → `gates_invalid` with diagnostic `GATES_EMPTY`; `["10", "10"]` → `GATE_DUPLICATE`; `[True]`/`[0]`/`[65]`/`["01"]` → `GATE_VALUE_INVALID`; gates not a list → `GATES_NOT_LIST`; missing row → `missing`; two rows → `duplicate`; wrong vendor / bool version / bad fingerprint → `row_invalid`; non-JSON / non-object / missing keys / `person_uid` mismatch → `payload_invalid`; each ends `NOT_READY` at exit 0 with the exact counts.
3. **Empty selection** (no `--user-id`, or a selection file of blank lines) → exit 5, stderr `READINESS_EMPTY_SELECTION`, stdout empty, no query issued. **Invalid selection** (uppercase UUID, non-UUID, duplicate UUID) → exit 5 `READINESS_SELECTION_INVALID`, no query issued.
4. **Unavailable / denied** → exit 5 `READINESS_UNAVAILABLE`, stdout empty, no partial report: `DATABASE_URL` absent with the real `DBAccess.for_current_env` (raises `PrimaryUnavailable(missing_database_url)`, no connection attempted); `for_current_env` raising `PrimaryUnavailable("primary_connect_failed")`; a retired bridge key present (`DB_BRIDGE_URL`) → `RetiredBridgeConfiguration`; `SqlExecError` from `query` on the second of three users (no report, no false ready); `query` returning `None`.
5. **Spies.** `tx`/`exec` on the fake raise; `readonly_tx` is absent from the fake and never needed; `engine.bodygraph.resolver.HdApiClient.from_env`, `ingest_vendor_bodygraph`, `persist_mapped_bodygraph` and `engine.bodygraph.vendor_client` constructors monkeypatched to fail — none fires across the whole matrix; the SQL seen by the fake is exactly `mapped_cache.CURRENT_ROW_SQL` with one bound parameter per lookup, in sorted UUID order, and contains no `INSERT`, `UPDATE`, `DELETE`, `CALL`.
6. **No leakage.** For every run, stdout and stderr contain none of the UUIDs, the strings `birthDateUtc`, `gates`, `bodygraph`, `Emotional`, `2000-01-01`, any Gate number list, `DATABASE_URL`, `postgres://` or a DSN; the report's keys are exactly the §5.3 set.
7. **Determinism.** Two runs → byte-identical stdout; ordering of `diagnostics` is ASCII-sorted.
8. **Import purity and member format.** `ast` of the module imports only from `argparse`, `hashlib`, `os`, `sys`, `pathlib`, `typing`, `engine.db`, `engine.db.errors`, `engine.bodygraph.mapped_cache` (read function and `MappedCacheError` only), `engine.bodygraph.projection` (`strict_canonical_uuid`, `BodyGraphProjectionError`, `is_gate_ingress_code`) and `engine.serializer.canon`; the file's bytes pass `registry_loader._parse_release_member_bytes(raw, "tools/bodygraph/check_magic10_gate_readiness.py")`; importing the module performs no DB connection (`for_current_env` spy untouched at import).
9. **Synthetic release coherence (D-02).** `synthetic_complete_release_root(tmp_path)` copies the real tool bytes (`sha256` of the copy equals the repository file) and `_load_active_mechanics_bundle_from_root` still admits it.
10. **Classifier ownership guard.** `classifier._lanes_for_path("tools/bodygraph/check_magic10_gate_readiness.py") == {"db", "product", "release"}`; `classifier.changed_test_targets(ROOT, [that path])` resolves to this module; an unregistered `tools/bodygraph/other.py` raises `CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING`; `classifier.classify_paths([path])` selects `db`, `product`, `release`.

### 8.3 Adverse matrix rows binding on PR05 (Plan §7.3 "Comparison/readiness")

Missing/extra/wrong expected case → refusal or mismatch (§8.1 items 3–4); identity mismatch → mismatch (§8.1 item 3); candidate/fixture write → impossible by construction, proven by snapshots, spies and AST (§8.1 items 5–7); DB/vendor call where prohibited → spies (§8.2 item 5); unavailable becomes ready → never (§8.2 item 4). Each row is a requirement for PR-30's evidence, not an observed PASS.

## 9. Ordered implementation procedure

One pull request. Three local checkpoints, each proven before the next begins. PR-30 forms one coherent initial commit from the completed checkpoints and publishes it; PR-35 pushes coherent corrective commits. No checkpoint is executed by PR-20.

**Precondition:** Nathan / Product Owner's PR-30 Proceed against this exact plan version (truthfully `NOT PRODUCED` at issue time). No other prerequisite remains.

### C1 — Fixture and comparator

1. Author `tests/fixtures/magic10/v1/goldens.json` from PF01 §9.5 per §5.1; serialize through `canon.sercanon`; verify the bytes round-trip and that the values equal the PF01 literals before any comparator code exists. Never derive an expected value from tool output; a disagreement with the landed implementation is a finding routed per instruction §10.
2. Implement `compare_goldens`, `render_golden_report`, the dataclasses, the refusal class and the `_golden_*` helpers in `tools/config/artifacts.py` (§5.2 invariants 1–6).
3. Implement `--compare-goldens`, `--goldens`, `--report` in `tools/config/generate_config_artifacts.py`; update the module docstring and help; add the one sentence to `docs/config_and_bundles.md`.
4. Write `tests/config/test_golden_comparison.py` (§8.1).

Checkpoint proof: `python -m pytest -q -p no:cacheprovider tests/config/test_golden_comparison.py tests/config/test_config_artifacts.py tests/config/test_typed_bundles.py tests/compat/test_evaluate_pair_eligibility.py tests/core` green; `python tools/config/generate_config_artifacts.py --compare-goldens <synthetic root copy under /tmp>` exits 0 with the report; against the repository root exits 5 with `CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER`; `git status --short --untracked-files=all` shows only the intended new/changed files.

### C2 — Readiness tool

5. Implement `tools/bodygraph/check_magic10_gate_readiness.py` (§5.3); confirm the member format with `_parse_release_member_bytes`.
6. Remove the placeholder entry in `tests/config/helpers.py::_SYNTHETIC_PLACEHOLDERS` (D-02); run the twelve `helpers.py` owner suites.
7. Write `tests/bodygraph/test_check_magic10_gate_readiness.py` (§8.2).

Checkpoint proof: `python -m pytest -q -p no:cacheprovider tests/bodygraph/test_check_magic10_gate_readiness.py tests/config tests/bodygraph/test_gates.py tests/http/test_reader_post_v1.py` green; in-process CLI runs with the fake DB behave per §5.3; `python tools/bodygraph/check_magic10_gate_readiness.py --user-id 00000000-0000-0000-0000-000000000001` with `DATABASE_URL` unset exits 5 with `READINESS_UNAVAILABLE` and prints nothing on stdout; clean tree apart from intended files.

### C3 — CI coherence and candidate-wide validation

8. Register every §6.2 entry in `ci/checks/classify_ci_changes.py` in the same checkpoint as the new test modules; run `tests/evidence/test_evidence_tool_ownership.py`, `tests/evidence/test_http_reader_ci_ownership.py`, `tests/qa/test_qa_tool_ownership.py`, `tests/evidence/test_rails_ci_workflow_integration.py`.
9. Run §10.3 (classifier dry-run: all seven lanes, the changed-test manifest includes both new modules and the 89-target roster) and the changed-test isolation step in a detached worktree; run §10.4 lanes and §10.5.
10. Write `docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` (§10.6) and read it back.
11. PR-30: one coherent commit (fixture, comparator, CLI, readiness tool, helpers change, classifier registrations, tests, doc sentence, result record); deliberate publication of the initial candidate through the one pull request; save and read back the PR-30 checkpoint under `docs/ephemeral/`; hand off to PR-35 in its own dedicated session with `PR_CANDIDATE_PUBLISHED`. PR-35: review retrieval and correction (Codex review; security review of corrected code), retests, corrective pushes, CI economy, current-head verification, `MERGE_PENDING — Ready to merge` without merging.

## 10. Local validation and evidence commands

### 10.1 Environment (exactly as `.github/workflows/ci.yml` installs)

```text
python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .
python -m pytest --version
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
ci/checks/check_env_pins.sh
```

### 10.2 Focused behavioral and ownership suites

```text
python -m pytest -q -p no:cacheprovider \
  tests/config/test_golden_comparison.py tests/bodygraph/test_check_magic10_gate_readiness.py \
  tests/config tests/core tests/bodygraph/test_gates.py \
  tests/compat/test_evaluate_pair_eligibility.py tests/http/test_reader_post_v1.py \
  tests/evidence/test_evidence_tool_ownership.py tests/evidence/test_http_reader_ci_ownership.py \
  tests/qa/test_qa_tool_ownership.py tests/evidence/test_rails_ci_workflow_integration.py
git status --short --untracked-files=all          # only intended paths before the commit; empty after it
```

### 10.3 Classifier dry-run and changed-test isolation (as `ci.yml` runs them)

```text
python ci/checks/classify_ci_changes.py --base "$(git merge-base origin/main HEAD)" --head HEAD \
  --event-name pull_request --github-output "$TMP/classify.out" --changed-tests-output "$TMP/changed_tests.txt"
cat "$TMP/classify.out"      # expect all seven lanes true (classifier change ⇒ full validation)
grep -c . "$TMP/changed_tests.txt"   # 89-target roster + both new modules (+ the modules' own paths de-duplicated)
git worktree add --detach "$TMP/changed" "$(git rev-parse HEAD)"
( cd "$TMP/changed" && export PYTHONPATH="$PWD" && python -m pytest -q -p no:cacheprovider -- $(cat "$TMP/changed_tests.txt") \
  && git diff --exit-code && test -z "$(git status --short --untracked-files=all)" )
```

### 10.4 Lane-equivalent validation

Run each lane exactly as `.github/workflows/ci.yml` at the candidate head defines it (the workflow file is the authority; verified step contents at planning time): product — `python tools/order/generate_ordering_artifacts.py --check` and `pytest tests/order tests/mech/test_order_properties.py tests/evidence/test_architecture_snapshot.py`; compat — `ci/checks/check_cli_help.sh`, `python tools/cli/serializer_grep_guard.py --output <tmp>`, `python tools/cli/emitter_symbol_proof.py --output <tmp>`, its ten-module pytest list; db — `python ci/checks/check_direct_db_contract.py` and its pytest list (`tests/db`, `tests/unit/test_check_direct_db_contract.py`, `tests/bodygraph/test_bg_resolve_v2_mapped_cache.py`, `tests/bodygraph/test_hde_epic038_mapped_cache_smoke.py`, `tests/bodygraph/test_ingest.py`, `tests/ops/test_capture_rails_open_scope.py`, `tests/ops/test_http_logging.py`); rails — `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml` (accepted end state exit 3 with `RAILS_JOB_DEFINITIONS:RELEASE_NOT_ADMITTED` and the independent probe observing `INCOMPLETE_RELEASE_ROSTER`) then `pytest tests/evidence/test_rails_ci_workflow_integration.py`; evidence — `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `python tools/evidence/refresh_step_logs_manifest.py --check`, `ci/checks/check_evidence_index_hash.sh`, `python tools/evidence/validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_final_lf.sh`, its six-module pytest list; qa — its seven-module pytest list in a detached worktree; release — `python scripts/release_id_recompute.py --check-manifest-only`, `pytest tests/runtime/test_identity.py tests/evidence/test_release_attestation.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py` in a detached worktree, then `python tools/evidence/build_release_attestation.py --output <external-empty-dir> --require-clean` (accepted end state: failure receipt `code == release_not_admitted` with the probe observing `INCOMPLETE_RELEASE_ROSTER`; `--verify` skipped). After every lane: `git diff --exit-code` and an empty `git status --short --untracked-files=all`.

### 10.5 Candidate-wide roster

```text
python -m pytest -q -p no:cacheprovider --ignore=tests/em
```

Record the pre-existing failures outside CI lanes by node ID as pre-existing (F07's two tests in `tests/evidence/test_dev_conjunction_identity.py` and the others PR04's result §8.8 lists); do not repair, skip or hide them; do not report them as PR05 regressions.

### 10.6 Result record

`docs/ephemeral/HDE-EPIC040-PR05-pr-implementation-result-v1.0.md` records: candidate commit SHA and tree; base `origin/main` SHA; every command above with exit status and counts (no aggregation of overlapping counts); the classifier output and changed-test manifest length; each lane outcome including the accepted `RELEASE_NOT_ADMITTED` results; the comparator's report bytes against the synthetic root and its refusal token against the repository root; the readiness tool's fake-DB outcomes; the planning decisions D-01–D-05 applied; an *In-flight decisions* section (`NONE` or one row per decision: what changed, why necessary, what was tested by test identity and outcome); limitations (no admitted release; no live rows observed; local results are not QA, acceptance or release admission); and `GCFPE_PROMPT_USES` for PR-30 (and later PR-35).

## 11. Code review and security review checklist

### 11.1 Code review

- The comparator implements no arithmetic on q, scores, bands, masks, fingerprints or pair keys; every value is produced by `_classify_channels`, `_compute_signals`, `_signal_q`, `_reduce_category`, `compute_core`, `_chart_fingerprint`, `normalize_gates`, `evaluate_pair`, `orient`, `intrinsic_pair_key`, `harmony_band`, `emit_reader_v1`; the only hashing is the PF05 §9.2 idempotence recheck (`sha256` over `sercanon` bytes).
- Membership/type/canonical-bytes validation precedes admission; admission precedes execution; refusals never become `match`; every leaf mismatch is reported; outputs are deterministic and sorted.
- No reference from the compare path to any write, activation, generation, transaction, updater or narrative-mount helper (AST guard); no module-level seam is set; no default router.
- Readiness: selection strictly canonical; `read_current_mapped_bodygraph` reused unchanged; per-outcome mapping matches §5.3; abort on `DB_QUERY_FAILED`/`AdapterError`; no verdict without observation; report keys closed; no UUID/payload/DSN in any stream; exit codes exactly `0`/`5` (+ argparse `2`); never `3`.
- Classifier registrations are exact, fail closed for unregistered `tools/bodygraph/*.py`, and the new tests are not fixed-lane providers.
- `tests/config/helpers.py` change limited to the placeholder entry; the twelve owner suites pass.
- Test names are canonical (`test_*.py`), no symlinks, no tracked-artifact writes, no wall-clock values written anywhere (PR04's CI run 35770839639 lesson).

### 11.2 Security review

- Fixture holds only synthetic UUIDs and synthetic chart fields; no birth records, secrets, real people.
- Readiness prints no identity, payload, DSN or environment value; `DATABASE_URL` is read only by `DBAccess.for_current_env`; retired bridge keys are refused; no vendor client, ingest or persistence import; no rail is opened; no `exec`/`tx`.
- `--report` refuses paths inside the candidate root or repository, symlinks and missing parents; writes are atomic and external; the candidate root is opened through the admission owner's safe-path capture (`_safe_source_path`, symlink refusal).
- No remote schema resolution, no network, no subprocess in either tool; no new HTTP route, public flag, payload field or transport change.
- The comparator cannot be used to admit or activate a release: it returns a `GoldenComparison`, never a bundle or handle.

## 12. Risk register and recovery

| ID | Risk | Mitigation / recovery |
| --- | --- | --- |
| R-01 | Default router mounts a narrative pack into the working tree (§3.2 item 6) | Explicit router stub for every application case; spies on `route_keys`/`get_pack`/`load_pack`; snapshot and clean-tree checks |
| R-02 | `readonly_tx` roster lock (§3.2 item 7) | D-01: `DBAccess.query` through `read_current_mapped_bodygraph`; SQL asserted read-only; `exec`/`tx` spies |
| R-03 | Classifier fail-closed errors (`CI_TEST_SUPPORT_OWNER_MISSING`, `CI_CHANGE_SURFACE_UNCLASSIFIED`, `CI_SOURCE_OWNER_TEST_MISSING`) | §6.2 registrations in the same commit as the new files; §10.3 dry-run before publication |
| R-04 | All seven lanes run (classifier change); rails and release lanes end in F01's accepted `RELEASE_NOT_ADMITTED` outcomes | Rehearse §10.4 locally; treat those outcomes as defined, not as failures; any other failure is PR05's to root-cause |
| R-05 | Fixture drift from PF01 or from PR04's pins | §8.1 item 1 agreement test against PF01 literals; values transcribed from PF01, never from output |
| R-06 | Comparator refusal against the repository root read as a defect | §5.2 refusal semantics and token; recorded in the result record as the truthful F01-interval result |
| R-07 | Exit-code laundering into the F01 `exit 3` acceptance | Neither tool exits 3; neither is a gate stage or job-definition step |
| R-08 | Placeholder removal changes the synthetic root bytes for twelve owner suites | Run them at C2; the real file passes `_parse_release_member_bytes`; fall back to keeping the placeholder only if a suite proves the real bytes cannot be captured (then record it as an in-flight decision) |
| R-09 | Non-canonical goldens bytes | Serialize with `canon.sercanon`; §8.1 item 1 round-trip check; `ci/checks/check_final_lf.sh` |
| R-10 | F05: the G008 Reader envelope carries `harmony`, which `schemas/reader.v1.schema.json` rejects | The comparator compares against PF01's oracle hash and does not validate the envelope against that schema; recorded explicitly; PR07 owns F05 |
| R-11 | Test pollution: a test writes under the repository | All roots under `tmp_path`; the changed-tests step asserts a clean tree |
| R-12 | Review round trips on CLI/exit-code design | Contract stated in §5.2–5.4; PR-35 may adjust within scope as an in-flight decision, recorded with its tests |

**Recovery.** On any error the configuration, fixtures and release selection stay unchanged and the exact mismatched case or refused source is reported. Restore tools, tests and fixtures together (one commit); never rewrite an expected value from failing actual output. If a golden-value disagreement appears during PR-30, stop the affected case, determine whether the transcription, the landed implementation or PF01 is wrong, and route per instruction §10; PF01 is not edited.

## 13. Carried `CANON_CONFLICT_REGISTER` and observations

### 13.1 `CANON_CONFLICT_REGISTER` (carried unchanged from Plan v2.1 §11.1, the instruction §13 and PF10 §2.19; no entry reopened, relabeled, omitted or newly decided; PR05 opens none)

| ID | Classification / status / decision | Effect carried into PR05 | Remaining owner |
| --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION` / `APPROVED`, Thoth-17 2026-09-08T13:23:24Z | `Done` exclusions and PF09.3 agreement preserved | Resolved |
| `C040-02` | `CANON_RECONCILIATION` / `APPROVED`, same | Use current controlled PF12 (repository v2.9.5) | PF12 version currency is ordinary maintenance |
| `C040-03` | `CANON_RECONCILIATION` / `APPROVED`, same | Current PF14 v3.5.7; C040-05 governs its core-test text | Resolved |
| `C040-04` | `CANON_RECONCILIATION` / `APPROVED`, same | PR05 performs engineering checks, not QA | Resolved |
| `C040-05` | `CANON_RECONCILIATION` / `APPROVED` alternative A, Isis-49 2026-09-09T03:57:16Z | The comparator calls the one four-argument core and its kernel functions; no second calculator | PF14 §6.7 maintenance pending, non-gating |
| `C040-06` | `NEW_CANON` / `APPROVED` alternative A, Isis-50 2026-09-09T11:48:08Z | Goldens exercise the 36-row taxonomy and 16-case conformance as delivered | PF12 §2.1 / PF01 §§6.1–6.2 drainage pending, non-gating |

The PF01 §4.5 versus PF05 §5.2.3 token-naming tension stays plan observation O-01 / PR04 result O-16 with the governed PF01/PF05 maintainers, decided by no one here.

### 13.2 Observations — non-gating, decided by no one here

| ID | Observation | Owner |
| --- | --- | --- |
| O-01 | `readonly_tx` is roster-locked to the OPS03 batch in `engine/db/providers/psycopg_provider.py`; a generic read-only transaction seam would need an `engine/db` change | `engine/db` owner; not PR05 |
| O-02 | PF12 currency: repository-resolved v2.9.5 versus the register/Plan's v2.9.6 (unchanged since PR04) | The governed PF12 maintainer |
| O-03 | PF10 v13.3's Addendum Index now lists 2.1–2.19 and includes §2.14; PR04 lineage review U-05 is closed (as the instruction records) | None |
| O-04 | `tests/config/helpers.py::_SYNTHETIC_PLACEHOLDERS` keeps the dictionary after D-02 with no entries; a later owner may remove the mechanism | `tests/config/helpers.py` owners |
| O-05 | The `tests/` lane rule sends the readiness test to `{product, release}` (no `db` marker in its path); it executes as a changed-test target and a registered owner, which is the intended coverage | None |
| O-06 | `docs/config_and_bundles.md` and `docs/RUN.md` mention the generator without its modes; PR07/DOC-10 owns fuller documentation of `--compare-goldens` and the readiness tool | PR07 |
| O-07 | The instruction's §5.3 wording "Use `readonly_tx`" is unsatisfiable against the real provider without an `engine/db` change (§3.2 item 7); its substantive requirement (read-only, no `exec`/`tx`) is met by D-01 | Recorded for the IA at PR-40 |
| O-08 | Notion fetch timestamps read about two hours behind this container's UTC clock (§3.2 item 14) | Operator |

## 14. Material boundaries and planning decisions

No material change to the Epic-level commitment was found: no outcome/objective, acceptance-criterion, protected architectural/security/data-model/external-contract boundary, multi-unit scope, accepted dependency or budget/schedule/risk item is affected. No RS-10 route is opened. The following planning decisions are non-material, obvious, necessary to deliver the approved scope and consistent with the Epic's objective and controlling constraints; PR-30 records them under *In-flight decisions* only if it changes them.

| ID | Decision | Why |
| --- | --- | --- |
| D-01 | Readiness reads through `DBAccess.query` via `read_current_mapped_bodygraph`, never `exec`, `tx` or `readonly_tx` | §3.2 item 7: `readonly_tx` is roster-locked; `engine/db` is not a PR05 locus; the requirement is read-only behavior, which a fixed parameterized `SELECT` satisfies and spies prove |
| D-02 | Remove the readiness placeholder from `tests/config/helpers.py::_SYNTHETIC_PLACEHOLDERS` | The real member exists after PR05; `tests/config/` is an owned test home; keeps the synthetic release truthful and exercises the real member bytes through `_parse_release_member_bytes` |
| D-03 | Every application case runs with an explicit fixture router stub; the comparator never uses the default router | §3.2 item 6: the default router mounts a pack into the working tree; PF01 G008 names the stub; G005/G007 assert nothing about narrative keys |
| D-04 | Kernel case kinds `signal_vector`, `signal_operation`, `reducer`, `core`; G001, G002, G003, G006 as injected vectors, G004 through `compute_core`; G005, G007, G008 through `evaluate_pair`; kernel cases never call the application path | Instruction §5.1–5.2 and Plan §6.5 "kernel-only cases remain kernel-only"; PF01 phrasing for each case |
| D-05 | CLI spelling `--compare-goldens` on `generate_config_artifacts.py` with `--goldens`/`--report`; exit `0`/`1`/`5`; readiness exit `0`/`5`; no tool exits `3` | Plan §5.9 makes the spelling a PR-level proposal with tests and docs; PF05 §3.4 stream discipline; R-07 |

## 15. Manual merge and post-implementation boundary

PR-30 and PR-35 ownership is preserved exactly and not reassigned: PR-30 recovers or establishes the one authorized work vehicle, implements only the authorized scope, tests locally, forms one coherent commit and deliberately publishes the initial candidate (`PR_CANDIDATE_PUBLISHED`), then hands the same work unit, workspace/worktree, branch, open PR, instruction, plan, original Proceed, completed work, tests and unresolved lineage to PR-35 in its own dedicated session without another Proceed. PR-35 owns review retrieval and correction, local retesting, coherent corrective pushes, CI economy, current-head verification, mergeability and genuine readiness, and returns `MERGE_PENDING — Ready to merge` without merging.

Nathan / Product Owner alone performs any manual merge unless a later direct, specific instruction expressly authorizes the identified action. No agent enables auto-merge, schedules a merge, asks for a merge as routine, or treats tests, review or CI as merge evidence. After actual manual merge evidence exists, Nathan may invoke the read-only PR-40 against the exact landed lineage; PR-40 independently decides work-unit acceptance. PR05 implementation, merge or acceptance performs no QA/Ops, promotes no release, edits no PF10 and closes no Epic. `PR-50 — Abort PR and Escalate` is invocable only by Nathan / Product Owner.

## 16. Prompt-use provenance

`GCFPE_PROMPT_USES` (this version):

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-20-20260924-PR05-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`; `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`; `work_unit_id`: `HDE-EPIC040-PR05`
- `requirements`: `K040-REQ-010`, `K040-REQ-011` principal; portions of `K040-REQ-001`, `-008`, `-012`, `-013`; `AC040-06`, `-07`, `-08`, `-09`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members (register read back 2026-09-24; page last edited `2026-09-23T17:43:39.489Z`)
- `prompt`: `PR-20 — Create Detailed PR Implementation Plan — 091426.1`, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, reported revision `2026-09-24T15:46:52.719Z`
- `role_stage`: dedicated PR05 PR-development session / PR-20 initial detailed planning; `execution_posture`: `MANUAL_PROMPT_EXECUTION`; `session_disposition`: `INITIAL_DEDICATED_ASSIGNMENT`; `role_session_ref`: `NOT_YET_ASSIGNED`
- `capture_time`: planning inspection `2026-09-24T18:05:25Z`–`18:21:16Z`; storage commit time recorded by git
- `runtime_identity`: `https://claude.ai/code/session_01FTff5iBZhV6crMfp7dkvxh` (from the harness attribution, directly known)
- `result`: `HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN v1.0`, state `AWAITING_PO_PROCEED`
- `result_refs`: repository path in §1; the storage pull request and commit are populated in the handoff only after they exist
- `repository_provenance`: `docs/changes` contains only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`; no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination exists; repository persistence of this use entry is `PENDING / NON_GATING` for a later authorized writer. Earlier uses in this change's lineage remain in their own artifacts under `docs/ephemeral/`, including `GCFPE-USE-HDE-EPIC040-PR-10-20260924-PR05-01` (instruction §15) and `GCFPE-USE-HDE-EPIC040-PR-40-20260922-PR04-01` (PR04 lineage review §14), and are not restated.

## 17. Continuation package

### 17.1 PR-30 package (this version's native next step)

The PR-20 user-facing return ends with one paste-ready `NEXT_PROMPT_HANDOFF` to `PR-30 — PR Implementation Proceed — 091426.1` (`https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`) for this same dedicated PR05 session with `RETAIN_EXISTING`. The package: Product Owner invocation of PR-30 for the exact visible `HDE-EPIC040-PR05-PR-IMPLEMENTATION-PLAN` v1.0 and `HDE-EPIC040-PR05-PR-INSTRUCTION` v1.0 (no additional approval object); this plan and the instruction by repository path; `HDE-EPIC040-SPECIFICATION` v1.1, Implementation Audit v2.0, Implementation Plan v2.1, Plan Review v2.1 (original `PLAN_REVIEW_ID` preserved), the F01 `RESCOPE_REVIEW` v2.0 with its addendum, and the accepted PR01–PR04 lineage (§2.1); PF10 v13.3 (`d79e4110…6f91`) with the §2.3 overlays including §2.15; the exact `main` head/tree baseline re-verified at Proceed time; §§4–12 in full; the register of §13.1; the manual merge boundary of §15; and PR-30's result contract `PR_CANDIDATE_PUBLISHED` (or `RESCOPE_PENDING`, `RECOVERY_PENDING`, `PRODUCT_OWNER_DECISION_REQUIRED`). The only manual prerequisite is Nathan's PR-30 Proceed for this exact version. PR-30 then hands off to PR-35 in its own dedicated session without another Proceed; Nathan alone merges.
