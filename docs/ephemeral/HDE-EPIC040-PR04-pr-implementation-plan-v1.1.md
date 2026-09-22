# HDE-EPIC040-PR04 — PR Implementation Plan v1.1

## 1. Identity, state, and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR04-PR-IMPLEMENTATION-PLAN` |
| version | `v1.1` — complete successor to v1.0 (`docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md`, SHA-256 `40e1b904b0817c42609d6f6abecf1c53a382e2da1face7720caa9b05f126ee65`, preserved unchanged) |
| state | `AWAITING_PO_PROCEED` — complete and executable within the approved scope plus the approved F01 overlay (PF10 §2.15); pending Nathan / Product Owner's exact PR-30 invocation against this version. One open candidate finding (`HDE-EPIC040-PR04-F02`, §14.3) is raised separately through RS-10 and is recorded, not folded in |
| finding_ref | `HDE-EPIC040-PR04-F01` — **dispositioned**: `APPROVE`, Isis-50, RS-20 review v2.0 at `2026-09-22T07:27:55Z`, bounded implementation rescope with exactly one PF10 addendum overlay (`docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md`; drained on `main` as PF10 §2.15) — §6.7, §14.1 |
| rescope_history | F01: RS-10 proposal v1.0 → RS-20 `REVISION_REQUIRED` (v1.0, `2026-09-22T06:48:06Z`) → RS-30 proposal v1.1 → RS-20 `APPROVE` (v2.0). F02 (§14.3): RS-10 proposal v1.0 authored by this session at `docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md`, `RESCOPE_PROPOSAL_PENDING_REVIEW`, awaiting RS-20 |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.1.md` |
| CHANGE_CLASS | `EPIC` |
| CHANGE_ID | `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR04` |
| work_unit_name | Bounded application, identity and consumer integration |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR04 |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` for PR-20; PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | `PR04-HDE-EPIC040-1` (assigned by the operator at session start; the receiving handoff carried `NOT_YET_ASSIGNED`) |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR04` / `PR-20` |
| context_conflict | `NONE` established |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| AUTHORING_CONTEXT | `APPROVED_BASE_WITH_OVERLAYS` — immutable approved base plus the applicable PF10 overlays in §2.3 |
| planning_inspection_capture_utc | v1.0 inspection `2026-09-22T01:33:19Z`; v1.1 re-verification of head, PF10 and overlays `2026-09-22T07:56:08Z`–`08:05Z`; storage commit time recorded by git |
| native_next_owner | Nathan / Product Owner for the exact PR-30 Proceed decision against this version; the F02 candidate's RS-20 decision (retained whole-change IA) is a separate, recommended-prior manual step (§14.3, §17) |

This plan is complete for the exact approved PR04 work unit and is executable within the approved scope as extended by the approved F01 overlay: every file, seam, contract, test, checkpoint, validation command, review obligation and risk is planned in §§4–12, and the nine production/CI files and four test homes the overlay admits are planned in §6.7. Version 1.0 was returned as a `DRAFT` because its completion condition (CI green) was unattainable inside the approved loci; that boundary (`HDE-EPIC040-PR04-F01`) is now dispositioned by an approved bounded implementation rescope, so this successor carries the overlay and presents `AWAITING_PO_PROCEED`. `AWAITING_PO_PROCEED` is a plan state, not an authorization. PR-20 performed no repository mutation outside the planning artifacts under `docs/ephemeral/`: no implementation, no product branch, no product commit, no pull request other than the storage pull requests for planning artifacts, no review, no CI run, no merge, no QA, no Ops, no release activation, no PF10 edit or number allocation, no addendum drainage and no Epic closure.

One candidate finding remains open and is deliberately not folded into this plan: `HDE-EPIC040-PR04-F02` (§14.3) — `adapter/http_reader.py` is both a PR04 locus PR04 must change and a committed `catalog/manifest.json` member, so the release lane's manifest content binding test fails on any PR04 candidate while PR04 may not refresh the manifest. It is raised separately through RS-10 at `docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md`. Until RS-20 dispositions it, §4.2 condition 4 cannot be met on a real candidate; the recommended sequence is F02's RS-20 decision before Nathan's PR-30 invocation, and §17 records both orders truthfully.

The Product Owner's PR-30 Proceed for PR04 does not exist at planning time. This plan does not assume it, does not request it as a precondition of anything below, and does not fabricate it. The only implementation authority is Nathan / Product Owner's manual invocation of the selected `PR-30 — PR Implementation Proceed — 091426.1` against this exact plan version (v1.1) and the exact PR instruction in §2.1. That Proceed authorizes implementation of this plan only and supplies no merge authority. `PR-50 — Abort PR and Escalate` is invocable only by Nathan / Product Owner.

## 2. Exact controlling lineage and source record

All lineage is resolved by repository path on `origin/main` at head `3b8084d09e974f15c2b71112e5a596af01b1a371` (v1.0 was resolved at `6ecacafb46d6a45ed8bcfcf0f04d262e3fd78612`; no executable path changed between them). Dead `libfile_` or `drive.google.com` links inside the bodies of earlier lineage artifacts are migration provenance, not blockers; Google Drive is not a source, store or authority for this work and was not consulted.

### 2.1 Approved and accepted change lineage

| Role | Exact repository artifact and current decision |
| --- | --- |
| Sole substantive PR-20 input | `docs/ephemeral/HDE-EPIC040-PR04-pr-instruction-v1.0.md`; `HDE-EPIC040-PR04-PR-INSTRUCTION` v1.0; `INSTRUCTION_READY`; SHA-256 `8769d12f8e4df82eed9f4869e4a48ca53ae8a99d7a6b6497df526036f30ffdcf`; 359 lines; 57,324 bytes; read completely |
| Approved Specification | `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`; `HDE-EPIC040-SPECIFICATION` v1.1; `SPECIFICATION_APPROVED` (Thoth-17); SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df`; 412 lines; 64,553 bytes |
| Fresh whole-change Audit | `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md`; `AUDIT_COMPLETE`; SHA-256 `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b`; 263 lines; 33,103 bytes |
| Immutable whole-change Plan | `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`; 985 lines; 146,624 bytes; §§4.1–4.4, 5.7, 5.8, 6.4, 7.1–7.4, 8 and 11.1 bind PR04 |
| Approving Plan review | `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md`; Isis-50 `APPROVE`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3`; 221 lines; 32,843 bytes; redline `R040-IA30-02` binds §8.3 of the instruction and §8 of this plan |
| Accepted PR01 dependency | `docs/ephemeral/HDE-EPIC040-PR01-pr-work-unit-lineage-review-v1.1.md`; `ACCEPT`; SHA-256 `f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273` |
| Accepted PR02 dependency | `docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md`; `ACCEPT`; SHA-256 `4b8d638c3f0e9232c8c2143fbce9593296f89c5dcc3d6b6da82293f21d5ab5c3` |
| Accepted PR03 dependency | `docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md`; `ACCEPTED_FINAL`; SHA-256 `07647f68bb5f5a705d8d2196f2aaaca9c17cb2b1c9f8774f8fd2b8268ae7dffa`; PR03 landed as `9cda1b49a972da874021e8820997fab1ebaff153` |
| PR03 detailed-plan format precedent | `docs/ephemeral/HDE-EPIC040-PR03-pr-implementation-plan-v1.0.md`; SHA-256 `d6fb097d009c81d71b28f97bf09ba5d71bb8429f7d458dcda5f667d0c5a6e8a9`; format precedent only, no authority over PR04 scope |
| PR-10 kickoff record | `docs/ephemeral/HDE-EPIC040-PR04-PR10-kickoff-handoff-v1.0.md`; SHA-256 `e319aa09deb1cc03f0e87a52be9160e3aa99cbe886f8c42c0fff20b127de1d69`; historical context only |
| Predecessor plan | `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-plan-v1.0.md`; v1.0 `DRAFT`; SHA-256 `40e1b904b0817c42609d6f6abecf1c53a382e2da1face7720caa9b05f126ee65`; preserved unchanged; stored through PR #453 (merged) |
| F01 rescope proposal v1.0 / v1.1 | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-proposal-v1.0.md` (SHA-256 `51eae27c2013722a3aebf22ca073587ad4d83c105176df87e970c37bc9f46bf6`); `…-v1.1.md` (SHA-256 `6bef3daf72eb4b547f43fa9efb49a548f68e97bbb8113c27f7ba13c4dec3756b`, reviewed artifact); RS-30 report `docs/ephemeral/HDE-EPIC040-PR04-F01-rs30-redline-application-report-v1.0.md` |
| F01 RS-20 decisions | `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v1.0.md` (`REVISION_REQUIRED`, Isis-50, `2026-09-22T06:48:06Z`; SHA-256 `37fd5d594981c84ec61669c75e2721eb38be698074691f750af17064e2117311`); `docs/ephemeral/HDE-EPIC040-PR04-F01-rescope-review-v2.0.md` (`APPROVE`, Isis-50, `2026-09-22T07:27:55Z`; SHA-256 `7700796fedcbd5847146f8e47c611aec662f67ec9ae99e4e8ed97279edbf5b20`; 233 lines / 29,561 bytes; read completely) |
| F01 PF10 addendum overlay | `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` (SHA-256 `86708f5c32de990be892bbb3f1ced973c5a110e30496753ca871b8f72c8082c1`; 197 lines / 20,418 bytes; read completely); drained by Nathan into PF10 as §2.15 in commit `3b8084d0…` (`2026-09-22T07:47:30Z`); the PF10 body is the canonical text |
| F02 rescope proposal | `docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md`; `RESCOPE_PROPOSAL_PENDING_REVIEW`; authored by this session with this plan version; not approved; §14.3 |

Historical artifacts with no authority over this plan: Implementation Plan v1.0 (PO-rejected) and v2.0 (DENIED), Plan Review v1.0 and v2.0, and the byte-identical duplicate copies `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1 (1).md` (same SHA-256 `47f73e62…`), `…-v2.0 (1).md` and `HDE-EPIC040-PR01-PR-40-interruption-record-20260912 (1).md`. The duplicates are recorded as observation O-08 in §13.2 and change nothing.

### 2.2 Controlled subject-matter sources used

Every PF source was resolved as the unique current controlled Markdown under `docs/pfcanon/` and read at the cited sections. No Google Doc, `.doc`, `.docx`, export, archive result, Drive copy, opaque library identifier, generated artifact, search-rank result or model memory was used as authority.

| Owner | Repository path, version and SHA-256 | Sections applied to PR04 |
| --- | --- | --- |
| PF01 — HDE Math Spec | `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`; `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a` | §4 complete `EvaluationParty`, strict Gates and self/identity eligibility; §4.5 boundary tokens; §4.6 sanctioned-resolver identity supply; §4.7 emission rule (ineligible ⇒ `categories: []`); §5.2.2 fingerprint, pair preimage and cache key `magic10:v1:<pair_key>`; §9.5 G007/G008 oracles |
| PF02 — HDE Architecture | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.5.md`; `d57fd3547573b8b8e3076b8f3fa4a34423a8b677c10bca93ff58eb6d4d867c6f` | §2.2.1 no-user proof classes and already-resolved / local-first / birth-only admission; §2.4 lifecycle; §3.1 conjunction read-only boundary; §3.2 Reader route posture; §7 privacy |
| PF03 — Technical Writing Best Practices | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md` | Source fidelity, claim-state separation and executable-plan writing only |
| PF05 — HDE CLI/API/Vendor Ref | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`; `a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e` | §3.1.1 exit-0 carriers; §3.7 no-user inputs; §4.1.2 `auto` is DB-only; §4.1.3 `showcompat` stdout is `magic10_compat_result.v1`; §5.1.0 POST Reader lookup contract; §5.2.3 Magic-10 failure tokens; §5.3 A7 transport rules; §5.5 `/api/compat/v1`; §§6, 7.1–7.4 guarded vendor routes, read-only conjunction, dry-run/non-production persistence boundaries |
| PF09.3 — Separation checklist | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md`; `0e3415e62e92f9d18c0d6ac1e513c1d8999efcacf2f71f4e1bda495fdbadec65` | Phase/task context only; the approved Plan decomposition governs |
| PF12 — HDE Schemas and Artifacts | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`; `d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d` | §2.9 Magic-10 v1 configuration and result contracts (`magic10_compat_result.v1` category rows `category_id`, `score`, `band`, `shared_key`, `personal_lo_to_hi_key`, `personal_hi_to_lo_key`), canonical JSON, validation, evidence owners and companions; version actually read is **v2.9.5** (observation O-02) |
| PF14 — HDE Mechanics Guide | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.7.md`; `a9c376f64e1cc3bb691d1661d131b3a42f6f96d318e82b981989b4a4836bd86c` | §6.7 canonical engine core module and tests under decided C040-05 alternative A; §7.2 evidence |
| PF10 — HDE Build Notes | `docs/pfcanon/PF10-HDE-Build-Notes-v13.2.9.md`; **`abcf86b82e6de7a0103534bf1deff140f5da273cb67412fd6e0a2c5838590afa`; 1,760 lines; 194,329 bytes** (content changed on `main` in `3b8084d0…` under the unchanged version label; v1.0 read the prior bytes `1421e4d6…`, and the complete delta — §2.15 added, index rows 2.14/2.15 added, formatting-only edits elsewhere — was read for this version); unique current controlled PF10 Markdown in `docs/pfcanon/` | Applicable overlays per §2.3, now including §2.15 |

### 2.3 Current controlled PF10 and every applicable active addendum

Effective baseline for this work unit: **approved base + the applicable PF10 overlays below, including the approved F01 overlay (§2.15)**. The canonical text of every overlay is PF10's; the `docs/ephemeral/` paths are the retained addendum source artifacts where the repository holds one. No overlay moves ownership into or out of PR04.

| PF10 addendum (heading line in v13.2.9) | Scope | Effect carried into PR04 | Retained repository source artifact (SHA-256) |
| --- | --- | --- | --- |
| §2.2 Canonize HDE-EPIC040 source-conflict ADR decisions (line 257) | Whole change | C040-01–C040-04 decided guidance | Published in PF10 only |
| §2.3 HDE-EPIC040 — Reconcile superseded core-test instructions (line 371) | Whole change | C040-05 alternative A: the four-argument Gate core supersedes precomputed-score passages; PR04 must not reintroduce a second calculator or a `ts_v0` scoring path | `docs/ephemeral/HDE-EPIC040-C040-05-pf10-build-notes-addendum-v1.0.md` (`071dc0263111b89746b1541b06758f31889c19f1d08a443205cb5ee26e581476`) |
| §2.4 HDE-EPIC040 — Record in-flight resolution of C040-01 through C040-04 (line 418) | Whole change | Status record only | `docs/ephemeral/HDE-EPIC040-C040-01-04-resolution-pf10-addendum-v1.0.md` (`c231f1ff7f254fd6b186dc61074115481591836cdb3ec0affc438e0eb78bb064`) |
| §2.5 HDE-EPIC040 — Record the approved source-backed Channel taxonomy and existing-state conformance (line 451) | Whole change | C040-06 36-row taxonomy and 16-case conformance are consumed through PR01–PR03 unchanged | `docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md` (`60bbcb2b442fef0798acef35a81ec1947493ecd6d4893b21a0c3040f4cf3d368`) |
| §2.6 HDE-EPIC040-PR01 — Accept Source-Proven Catalog and Exact Contract Data (line 652) | PR01 | Accepted catalog/contract data dependency | `docs/ephemeral/PF10-Addendum-HDE-EPIC040-PR01-pr-work-unit-lineage-review.md` (`2b7c817395a307da097d81b49e629955e33fffad42b18d0003df2dbc12cf161d`) |
| §2.7 HDE-EPIC040-PR02 — Rescoping (line 809) | PR02 only | Accepted PR02 admission behavior consumed unchanged; confers no PR04 scope | `docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v1.0.md` (`d54fb85ee98fd152f1dfe8e0cc8c09f90989c70d56eacad29ae0d6f6d79057c1`); `…-v2.0.md` (`5ecc9850dc9f4368868ad1e4de15e249193e2bb81421e41095e4aed686c2874d`) |
| §2.8 PF10-FORM-001 — Establish Page-Ready Canonical Form for Agent-Authored Addenda (line 923) | All agent-authored PF10 addenda | Form rule only. PR04 authors no addendum; the F01 overlay was authored under it by RS-20 | Published in PF10 only |
| §2.9 HDE-EPIC040-PR02-F02 — Executing-Code Coherence Rescope (line 956) | PR02 only | Accepted; consumed unchanged | `docs/ephemeral/HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md` (`1c952386cd84eaf8a8aefbb33054b6a902d49ea73aa6f68239f099ad700a25fd`) |
| §2.10 HDE-EPIC040-PR02-F03 — Existing Serializer Manifest Binding Refresh (line 1115) | PR02 only | Accepted serializer manifest binding consumed unchanged | `docs/ephemeral/HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md` (`896b3f3ab16f7d18ce2ab3de1bb1b6599afb85e349e963a9f52421f3189e46fb`) |
| §2.11 HDE-EPIC040-PR02 — PR Work-Unit Lineage Review v1.0 (line 1280) | PR02 | Accepted dependency status | Recorded in PF10; review body at `docs/ephemeral/HDE-EPIC040-PR02-pr-work-unit-lineage-review-v1.0.md` |
| §2.12 HDE-EPIC040-PR03-R02 — Bind Executing Mechanics to the Admitted Release (line 1365) | PR02/PR03 admission boundary | The private admission execution-provenance and executable-equivalence owner in `engine/config/registry_loader.py` covers the four active PR03 mechanics modules; PR04 preserves it and must not weaken, bypass or relocate it | `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` (`a44659a7754c5f6e10f0bf4a1397d6815aae32ef75a2626a866055a801ba1998`) |
| §2.13 HDE-EPIC040-PR03 — PR Work-Unit Lineage Review v1.0 (line 1478) | PR03 | `ACCEPTED_FINAL`; PR04/PR05 retain existing scopes; dependency order PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01 | `docs/ephemeral/HDE-EPIC040-PR03-pr-work-unit-lineage-review-v1.0.md` (`07647f68bb5f5a705d8d2196f2aaaca9c17cb2b1c9f8774f8fd2b8268ae7dffa`) |
| §2.14 Specification format authority (line 1594) | Specification authoring | Not applicable to PR04 engineering; now listed in the Addendum Index (observation O-06 resolved) | Published in PF10 only |
| **§2.15 HDE-EPIC040-PR04-F01 — Truthful Non-Admitted Gate Outcome for the PR04-to-PR06 Interval (line 1636)** | PR04 (and PR05 through the release lane) | **The approved F01 overlay.** PR04's loci extend to nine production/CI files and four test homes for one purpose: the affected gates express an explicit `RELEASE_NOT_ADMITTED` outcome (never `PASS`, never `top_level_pass: true`, never a frozen-byte substitute presented as live) and ordinary CI accepts that one outcome while the active release is not admitted; four binding conditions; ownership limit on `build_release_attestation.py`; six determinism outputs and the sanity log regenerated only by owners. Carried in full into §6.7 | `docs/ephemeral/HDE-EPIC040-PR04-F01-PF10-build-notes-addendum-v1.0.md` (`86708f5c32de990be892bbb3f1ced973c5a110e30496753ca871b8f72c8082c1`) |

### 2.4 GCFPE execution sources

- PR-20 source: `PR-20 — Create Detailed PR Implementation Plan — 091426.1`, page `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, retrieved revision `2026-09-21T22:56:47.757Z`, selected in ecosystem release `GCFPE-20260914.1`, contract `091426.1`, 55 members (Register selection confirmed 2026-09-21).
- PR-30 destination: `PR-30 — PR Implementation Proceed — 091426.1`, page `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`.
- PR-35 continuation: `PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1`, page `https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204`.
- PR-40 conditional lineage review: page `https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204`.
- Rescope route: RS-10 `https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4?pvs=204`; RS-20 `https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204`.
- Notion state of record: Flow Index page `https://app.notion.com/p/3db4590a05eb81de9736ea69bac61016` (sole operative Alpha state block).

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline re-verified at planning time

| Field | Observed value |
| --- | --- |
| Repository | `amthorn78/glow-hdengine-v2` |
| Target branch | `main` |
| Verified `main` head | `3b8084d09e974f15c2b71112e5a596af01b1a371`; tree `11e81c99b9194c38471b494c59b149d4f4553659`; committed `2026-09-22T07:47:30Z` (PF10 §2.15 drainage). v1.0 planned at `6ecacafb…`; the RS-20 decision re-verified at `0f47079f…`; every commit between them is documentation (`docs/`) |
| Instruction-time head | `d1c8ae25ad313500a2e5d8d4115ea2cfa5212c10` (recorded in instruction §3.1) |
| PR03 landing | `9cda1b49a972da874021e8820997fab1ebaff153`; tree `cbc6f35834253dcee3907bf4669bc7cdd1e396a2`; committed `2026-09-14T12:33:13Z` |
| Executable-path delta since PR03 | `git diff --stat 9cda1b4..3b8084d -- . ':(exclude)docs/'` is empty; every later commit is documentation. The executable PR04 baseline is exactly the accepted PR03 state |
| PR04 work vehicle | None exists: no PR04 product branch, product commit, product pull request, Proceed, implementation result, review, CI result or merge. Storage PRs for planning artifacts: #453 (plan v1.0, merged), #462/#463/#465 (F01 rescope lineage, merged) |
| Planning working tree | `git status --short` empty after removing one untracked directory `narratives/4cc79e05…/` that an in-process narrative-pack probe created at `2026-09-22T01:20:32Z` (observation O-07). The baseline test run executed in a `git archive` scratch copy, not in the repository tree |
| Tooling | Python 3 with `requirements.txt` and `requirements-dev.txt` installed (pytest 8.4.2, jsonschema 4.23.0, flask 2.3.3); `rg` absent (`grep`/`find` used); `hdctl` console script not installed in the planning environment (`pyproject` `[project.scripts] hdctl = "engine.cli.main:cli"`; CI installs it with `pip install -e .`) |

### 3.2 Baseline behavior facts that shape this plan

1. **Admission refuses in the real repository.** `engine/config/registry_loader.py::load_active_mechanics_bundle()` refuses with `INCOMPLETE_RELEASE_ROSTER` because `catalog/manifest.json` (15 members; release_id `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856`) does not cover the 44-member `ADMITTED_RELEASE_ROSTER`. Between PR04 and PR06 no real CLI, HTTP or evidence-generator success path can produce a Gate-based result without an injected fixture bundle. The only truthful positive proofs are in-process tests that inject the synthetic complete release through the existing test-only seam `_load_active_mechanics_bundle_from_root(tests.config.helpers.synthetic_complete_release_root(tmp_path))`. PR04 does not weaken, bypass or relocate admission (PF10 §2.12).
2. **CI classifier fails closed.** `ci/checks/classify_ci_changes.py` raises `CI_PRODUCT_OWNER_TEST_MISSING` for any changed product path without a `_PRODUCT_TEST_OWNER_PATHS`/`_PRODUCT_TEST_OWNER_PREFIXES` registration. Registered today among the PR04 loci: `adapter/http_reader.py` (with the HTTP-reader ownership guard family: `_HTTP_READER_TEST_OWNERS`, `_HTTP_READER_DYNAMIC_TEST_OWNER_SHA256`, guard test `tests/evidence/test_http_reader_ci_ownership.py`, which requires every test module importing `adapter.http_reader` to be registered) and `engine/narratives/router.py` (prefix `engine/narratives/` → `tests/unit/test_narratives_router.py`, `tests/unit/test_narratives_loader.py`, `tests/cli/test_aux_preview.py`). Unregistered and therefore fail-closed: `engine/compat/compute.py`, `engine/bodygraph/resolver.py`, `engine/bodygraph/projection.py`, `engine/bodygraph/v2_adapter.py`, `engine/bodygraph/mapped_cache.py`, `engine/bodygraph/ingest.py`, `engine/runtime/public.py`, `engine/cli/main.py`, `engine/http/compat_handler.py`, `presenter/reader_v1/emitter.py`, `engine/compat/error_tokens.py`. Further fail-closed rules that bind PR04: `fixtures/charts/*` has no lane mapping (`CI_CHANGE_SURFACE_UNCLASSIFIED`); an unregistered `tools/evidence/generate_*.py` raises `CI_EVIDENCE_OWNER_TEST_MISSING` (only five generators are registered today, none of PR04's); `tools/evidence/run_canonical_json_gate.py` is a registered evidence helper; `tools/cli/generate_showcompat_artifacts.py` is a `_RELEASE_IMPLEMENTATION_PATHS` member (evidence + release lanes, no owner requirement); `errors/token_map/token_map.json` is a governed primary in `docs/evidence/INDEX.json` and classifies to the evidence lane; `tests/config/helpers.py` is a registered test-support owner path and stays unchanged. Changing the classifier is itself a full-validation input: all seven lanes, the `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` roster (40 modules, including `tests/cli/test_showcompat_sources.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`, `tests/cli/test_cli_file_inputs.py`, `tests/transport/test_a7_transport_proofs.py`) and every registered owner outside the fixed lanes run for the PR04 candidate.
3. **CI enforces a clean candidate tree** after every pytest invocation and at the final step (`git diff --exit-code`; `test -z "$(git status --short --untracked-files=all)"`; final marker `CI_CANDIDATE_TREE_NOT_CLEAN` on failure). `engine/narratives/state.py::get_pack()` lazily calls `load_pack()` with the default mount root `Path("narratives")`, which writes `narratives/<pack_sha>/` into the current working directory; the tracked mount is the stale `narratives/64e17c9c…/` while the current pack sha is `4cc79e0535d93acece861fff5e725a26b62ab22ee2c03c9bae2632a5570953a0`. Any PR04 test or generator that reaches `route_keys` must preset `engine.narratives.state._PACK` from a temporary mount exactly as `tests/cli/test_aux_preview.py` and `tools/evidence/run_canonical_json_gate.py` already do (risk R-09).
4. **Current consumers are the gaps the instruction names.** `engine/compat/compute.py::compat_public` is a sha256 hash scorer over `pair_key:category`; `conjunction_public_resolved._resolve_party` returns UID-only `{"person_uid": …}` results and calls `resolve_bodygraph(source="vendor", upsert=True, dry_run=False, …)`; `engine/runtime/public.py::emit_reader_public_envelope` derives the band from `ts_v0`; `adapter/http_reader.py` has `@bp.post("/reader")` returning `_error("method_not_allowed", 405)`; `engine/cli/main.py` synthesizes charts in `_chart_for`, derives `cli-` hash UIDs in `_derive_uid`, falls back from `auto` to `vendor` when birth flags are present, prints the legacy `{a, b, viewer_prefs, compat}` wrapper and emits admin dumps from `ts_v0`; `engine/http/compat_handler.py` returns the hash result plus a `keys` list; `tests/compat/test_conjunction_no_user_boundary.py` asserts only non-empty `person_uid` values and AB/BA byte stability with `local_lookup` returning `None`.
5. **Reader blueprint paths.** `adapter/http_reader.py` registers `Blueprint("reader_v1", __name__)` at `url_prefix=""`; the declared routes are `GET /reader` (dev-gated fixture route requiring `v=1`, `tz_a`/`tz_b`, `_require_tz_or_raise`, ETag/304/HEAD handling, `_set_reader_200_headers`) and `POST /reader`. The instruction's `POST /api/reader?v=1` spelling and the repository's declared `POST /reader` name the same existing declared route in this application (the blueprint has no `/api` prefix); PR04 implements the success path at the existing declared `@bp.post("/reader")` and adds no route (observation O-03 covers the catalog).
6. **Oracles reproduce.** PF01 §9.5 G007 (Reader preimage hash `8214324e…`) and G008 (fingerprint `7567338a…`, pair_key `8a75eafc…`) were recomputed at planning time with the current emitter/core recipe (`engine/core/core.py::_chart_fingerprint`, `_digest`, `presenter/reader_v1/emitter.py`); no new formula is needed.
7. **Narrative pack coverage is complete.** `catalog/narratives` (pack sha `4cc79e05…`) covers 10 categories × 4 bands × 3 perspectives (120 primaries) with two governed suppressions; `engine/narratives/router.py::route_keys(category, band, perspective)` returns personal/shared keys or the `MISSING_NARRATIVE_KEY` sentinel.
8. **Baseline test state.** In the scratch copy under closed rails, `python -m pytest -q --ignore=tests/em` gave 667 passed, 3 skipped, 5 failed. `tests/em/test_em_defaults_and_ladder.py` has a pre-existing collection error (`core.config` missing) and is outside every CI lane. The 5 failures are pre-existing and outside CI lanes: `tests/compat/test_cli_public_bytes_identity.py::test_cli_public_bytes_two_run` (retired `--birthdate/--place/--tz` flags → exit 64), `tests/adapter/test_reader_parity.py` ×3 (GET `/reader` without `v=1` → 400), `tests/reader_v1/test_cli_proof.py` (`scripts/hd_cli.py` `ADMIN_FLAG_REQUIRED` exit 2). PR04 must not turn these into false greens and must not repair them silently (observation O-05).
9. **Complete mapped fixtures exist.** `tests/fixtures/bodygraph/source_invariance/{vendor_chart_result.v1.json, db_cached_payload.v1.json, normalized_input.v1.json}` carry complete mapped `ChartResult` projections (gates `["10","20","34"]`, UUID-bearing identities). `tests/config/helpers.py::synthetic_complete_release_root(tmp_path)` and `tests/core/test_engine_core_abba.py` supply the fixture-bundle pattern.
10. **Migration `011_body_graphs_durability.sql`** defines `hde.body_graphs`, the view `hde.body_graphs_current` (`DISTINCT ON (user_id, vendor)`) and the public view `public.hde_body_graphs_current` with columns `user_id, vendor, vendor_version, input_fingerprint, payload, created_at, refreshed_at, ttl_at`. PR04 adds no DDL.
11. **Three ordinary-CI gates execute live success paths.** The rails lane runs `python tools/evidence/generate_open_rails_abba_proof.py --check-current` (via `ci/jobs/rails_open_conformance.yml`); the release lane runs `python tools/evidence/build_release_attestation.py --output … --require-clean`, which executes all fifteen release-sanity stages in an isolated copy and fails with `final_sanity_pass_missing` unless stage `04 Reader-to-CLI, AB-to-BA, two-run, and preimage checks` (`generate_determinism_gate_proofs.build()`, `generate_open_rails_abba_proof.build_fixture_proof()`) and stage `05 A7 Catalog transport` (`generate_a7_transport_proofs.build()`, live `GET /reader` 200 and `POST /reader` 405) pass; the full-validation roster runs `tests/transport/test_a7_transport_proofs.py`, which calls that live build. All three require a Gate-based success that item 1 shows is unavailable until PR06 — finding F01, dispositioned by the approved overlay PF10 §2.15 and planned in §6.7. The RS-20 reviewer confirmed the effect by executing a PR04-shaped change: rails chain 18 failures in `tests/evidence/test_open_rails_abba_proof.py` plus 1 in `tests/evidence/test_rails_ci_workflow_integration.py`; release chain `tests/runtime/test_identity.py` and `tests/evidence/test_release_manifest_content_binding.py` failing with `tests/evidence/test_release_attestation.py` fully green; full-validation roster 14 failures across `tests/cli/test_showcompat_sources.py`, `tests/cli/test_cli_file_inputs.py`, `tests/cli/test_cli_install_help.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`, `tests/transport/test_a7_transport_proofs.py`; `run_canonical_json_gate.py --check-only` rc=1 (engineering observations, not a QA verdict).
12. **Manifest content binding (candidate finding F02, §14.3).** `adapter/http_reader.py` is the first of the fifteen committed members of `catalog/manifest.json` (row `sha256 9f0cde20055e7a94db50fb506bace9ddc51b3f9184fc1192a498c5b2fd243592`, `size 35655`; manifest `version 1.0.0`, `built_at_utc 2025-12-26T00:00:00Z`). `tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` asserts every entry's hash and size equal the repository bytes and runs in the release lane (`.github/workflows/ci.yml` release step pytest list). Any PR04 change to `adapter/http_reader.py` fails it, independent of admission state, while §4.3 excludes manifest expansion/activation and §6.6 lists `catalog/manifest.json` as unchanged. No other PR04 locus is a committed manifest member (`engine/presenter/emitter.py` is a member and is unchanged; PR04's `presenter/reader_v1/emitter.py` is not a member). The PF10 §2.10 precedent (PR02-F03) is scoped to PR02 alone.

## 4. Exact objective, completion conditions, and exclusions

### 4.1 Objective (Plan §6.4)

Make the existing selected consumers use valid Gate-based results and preserve public/private contracts: complete chart-bearing resolution for already-resolved, stored-user and birth-only/no-user inputs; canonical internal identity through the existing birth-seed and `resolve_db_user_id` bridge; complete normalized projection to `EvaluationParty`; eligibility decided before core, intrinsic cache and router; the contracted Reader POST success path at its existing declared route; and the six separate no-user success, refusal and prohibited-side-effect proofs of `R040-IA30-02`.

### 4.2 Completion conditions

PR04 is complete when all of the following hold on one coherent candidate:

1. Every owned locus in §6.1 implements the behavior in §5 with no remaining successful hash, `ts_v0`, UID-only, synthesized-chart or `cli-` identity path.
2. Every requirement row in §7 has its named tests present, passing under closed rails, and registered as classifier owners.
3. The six `R040-IA30-02` proof classes in §8.2 pass in-process with the synthetic complete release bundle and truthful refusals without it.
4. All seven CI lanes pass on the exact candidate head with `CI_APPLICABILITY_AND_EXACT_HEAD_OK`; no test is skipped, disabled or quarantined to get green; the candidate tree is clean. Under the approved F01 overlay (PF10 §2.15; §6.7) the rails and release lanes pass by accepting the one explicit `RELEASE_NOT_ADMITTED` outcome while the active release is not admitted — a truthful non-pass gate outcome, not a waiver. **Open dependency:** the release lane's `tests/evidence/test_release_manifest_content_binding.py` remains red on any PR04 candidate until candidate finding F02 (§14.3) is dispositioned; this plan does not assume that disposition.
5. Code review and security review findings on the corrected code are resolved under PR-35; the PR reaches `MERGE_PENDING — Ready to merge` without merging.

PR04 claims no completion of broader Reader, admin, narrative, vendor or cache capability, no live-data readiness, no QA verdict, no acceptance and no release admission.

### 4.3 Hard exclusions

Any new public route, public flag, public payload field or transport change; a new CLI identity flag; a birth-to-Gates calculator; HDE-SEPA006 loader migration; new persistent cache infrastructure; database DDL, backfill, account creation or any production mutation; new vendor routes or credentials; live vendor or database operation; opening rails; release promotion, manifest expansion or activation; PR05 golden comparison and read-only Gate readiness; PR06 release admission and evidence convergence (including regenerating governed success captures that require an admitted release); PR07 DOC-10 documentation; OPS01 external verification; independent QA or Ops execution; deployment; PF10 editing, number allocation or addendum drainage; PF-Canon edits; Epic closure; any change to PR01 catalog data, PR02 normalizer/admission types, or the PR03 core, composite, signals and calculators modules.

## 5. Designed interfaces, invariants and contracts

Every interface below is private application structure unless marked public. Names are proposals binding on the PR04 engineer only as behavior; a renamed private symbol with identical behavior is an in-scope engineering choice, not a rescope.

### 5.1 Resolution seam — `engine/bodygraph/resolver.py`

```text
@dataclass(frozen=True)
class ResolvedCompatChart:            # private; not a public JSON schema
    canonical_person_id: str          # lowercase canonical RFC-4122 UUID string
    mapped_chart: Mapping[str, Any]   # complete mapped shape {bodygraph{10 fields}, person{person_uid}, person_uid}
    source: str                       # "resolved" | "db" | "local" | "vendor_v2_dry_run" | "legacy_v1_dry_run"
    user_id: str | None               # bound resolver/DB user id (row identity), None for file/stdin
    vendor: str | None                # "hdapi" when row/adapter context supplies it
    vendor_version: int | None
    input_fingerprint: str | None     # vendor request fingerprint when the source supplies it; never the birth seed

def resolve_compat_chart(raw_party, *, source_policy, env, local_lookup=None, acquisition=None) -> ResolvedCompatChart
```

Behavior:

- **Input class 1 — already-resolved chart with trusted identity/provenance.** A complete mapped chart with a resolver/DB `user_id`, or an admitted internal engine alias. Canonicalize UUID spelling; route an alias through the existing `resolve_db_user_id` bridge, then `str(UUID(resolved))`. Cross-check every supplied identity slot (`person_uid`, `person.person_uid`, `user_id`, `canonical_person_id`) against its provenance; any two independently supplied, non-equivalent identities refuse. Preserve the complete mapped BodyGraph. A complete file/stdin projection needs no DB or vendor lookup and gets none. A chart with neither identity provenance nor a complete sanctioned birth tuple is missing required internal metadata and refuses; identity is never derived from Gates.
- **Input class 2 — stored-user / admin lookup.** Resolve the admitted engine key with `resolve_db_user_id`, canonicalize, and use that canonical value for the parameterized read-only lookup (`engine/cli/main.py::_fetch_db_bodygraph` or the injected `local_lookup`). The lookup returns payload plus verified row identity and source metadata; resolver status, UID or cache metadata alone is not a chart. Validate a hit; an invalid hit refuses and no vendor fallback hides it. A miss is the existing missing-chart failure.
- **Input class 3 — complete birth-only / no-user tuple.** Validate the existing birth input contract (`birthdate`, `birthtime`, `location`, all present and shaped as today's normalizer requires), reuse `_derived_birth_uid` unchanged as the `birth-` seed, pass the seed through `resolve_db_user_id`, canonicalize the returned UUID. Try the permitted local lookup for that canonical key first; a verified complete hit succeeds with network rails closed and no user-row creation. On a miss, acquire only when `source_policy` permits acquisition, the invocation's existing route and operator authority permit it, and the existing `SAFE_MODE`/`ALLOW_NETWORK`/route guards pass; otherwise return the owning refusal (`PROVIDER_REFUSED` / `PROVIDER_NETWORK_BLOCKED`). A birth input or derived UUID alone never yields Gates, type, scores or success.
- **Acquisition** reuses the existing configured full-`ChartResult` v2 route through `_resolve_vendor_v2_chart` / `V2ChartAdapterContext` / `adapt_v2_chart_payload` in **dry-run, no-upsert** posture; the adapter `resolved` mapping and verified context are retained. For the preserved legacy v1 route, `ingest_vendor_bodygraph(..., dry_run=True)` is used only read-only and its `IngestOutcome.payload` is admitted to Gate-based success only when it already supplies the complete governed mapped projection; otherwise the typed invalid/missing-chart refusal is preserved. No v1 field translation is guessed and no v2 fields are substituted into an incomplete v1 response. `ChartSimpleResult`, missing full-result fields and route/context mismatches refuse.
- **Rails.** The resolver never turns rails on for itself. The scoped acquisition capability (the temporary env view handed to the vendor client) is closed in a `finally` block before normalization and evaluation and on every exception path; the caller's original environment is restored; no process-wide setting is edited; no second HTTP client, no route inference from a base URL, no default timezone, no retry against another source.
- **Logging seam (`engine/bodygraph/ingest.py`).** The dry-run no-user path must not inherit `_append_jsonl` success/retry logging of `user_id`; the seam accepts a `None` log target (or an explicit `log_private_values=False` posture) so that only value-free operational keys are emitted. This is the only change to `ingest.py` besides passing the preserved payload through.
- **Identity-slot rules.** `person-…` labels are display/provenance metadata and are never accepted literally as canonical UUIDs; where a mapped chart carries them, both the top-level and nested labels must match each other and the trusted resolver context that created them before the application copy's label slots are replaced by the verified canonical UUID. No prefix stripping with assumed ownership, no override of an independently conflicting identity, no `cli-` fallback UID, no identity from Gate masks. Contradictory charts under the same resolved identity take the inconsistent-self failure path; distinct trusted identities are preserved even when masks coincide.

### 5.2 Projection and `EvaluationParty` — `engine/bodygraph/projection.py`, `engine/compat/compute.py`

```text
@dataclass(frozen=True)
class EvaluationParty:
    canonical_person_id: str                 # validated lowercase RFC-4122 UUID
    projection: Mapping[str, Any]            # complete normalized projection from project_bodygraph, label slots = canonical UUID
    gates: NormalizedGates                   # PR02 normalize_gates(...) result: (gates tuple, mask, mask_hex)
    chart_fingerprint: str                   # engine.core.core._chart_fingerprint over the validated Gate tuple
```

- `project_bodygraph` remains the single projector (exact keys `bodygraph` with ten fields, `person{person_uid}`, `person_uid`; the only removable transient is `source`). PR04 adds strict raw-Gates validation **at every mapped ingress before deduplication or persistence**: a nonempty array of integers 1..64 or canonical decimal strings; bools, whitespace, signs, leading zeroes, floats, missing/empty values, duplicates including integer/string equivalents, out-of-range values and unresolved catalog references refuse (`BodyGraphProjectionError(code, field_path)` codes reused, mapped per §5.6). Sorting happens only after validation. All other projection fields are retained for equality; no default or synthesized mechanics value is introduced.
- `gates` is produced only by PR02's `engine/bodygraph/gates.py::normalize_gates`; `EvaluationParty` holds the exact `NormalizedGates` instance the PR03 core requires (`type(member) is NormalizedGates`). Mask and fingerprint derive from the validated tuple only; no source or identity metadata contaminates them.
- Both parties are validated independently before eligibility.

### 5.3 Eligibility, orientation, evaluation — `engine/compat/compute.py`

```text
def validate_pair_eligibility(a: EvaluationParty, b: EvaluationParty) -> Literal["eligible", "ineligible_self"]
    # same UUID + equal complete projection  -> "ineligible_self"
    # same UUID + any unequal projection     -> raise ERR_READER_INVALID_CHART (inconsistent self)
    # distinct UUIDs (equal masks allowed)   -> "eligible"

def orient(a, b) -> tuple[EvaluationParty, EvaluationParty]
    # lo/hi by (gate_mask, canonical_person_id); UUID ASCII order breaks only equal-mask ties

def evaluate_pair(a, b, *, bundle_provider=_BUNDLE_PROVIDER, cache=None, router=route_keys) -> dict
    # 1 eligibility; 2 orientation; 3 bundle = bundle_provider() (AdmittedMechanicsBundle; refusal propagates);
    # 4 cache lookup by "magic10:v1:<pair_key>" only when a cache seam is injected; a hit must validate schema and
    #   embedded pair_key/config_id/release_id, else recompute with both valid Gate sets or refuse ERR_M10_STALE_RESULT;
    # 5 compute_core(lo.gates, hi.gates, bundle, bundle.release_id).to_payload();
    # 6 router augmentation for every category row in both normalized directions:
    #   route_keys(category_id, band, "shared") lo->hi and hi->lo must agree on shared_key, else ERR_MISSING_NARRATIVE_KEY;
    #   personal_lo_to_hi_key / personal_hi_to_lo_key from the two directional perspectives; MISSING_NARRATIVE_KEY refuses;
    # 7 structural validation of the augmented result against schemas/magic10_compat_result_v1.schema.json;
    # 8 return the canonical result mapping (never cached by identity-free pair_key alone; cache value carries pair_key,
    #   config_id, release_id and both chart fingerprints).
```

- `_BUNDLE_PROVIDER` defaults to `engine.config.registry_loader.load_active_mechanics_bundle`; tests inject the fixture bundle through this seam and never through a relaxed admission. `release_id` for evaluation and for the Reader envelope is the admitted bundle's `release_id` (== `sha256(canonical_bytes(catalog/manifest.json))` under real admission); no evidence path or identity environment value is read.
- `conjunction_public(left_resolved, right_resolved, *, viewer_top, viewer_weights, engine_tag, release_id, invocation_tag)` becomes a thin pure entry receiving two already-validated `EvaluationParty` values and returning `evaluate_pair`'s result; it acquires nothing, invents no identity and runs no second scoring formula. `compat_public` (hash scorer) and `_score_for` are removed with no successful replacement path. `viewer_top`/`viewer_weights` are accepted only where an existing caller still passes them and are not scoring operands; the presentation of a caller-personal direction remains separately owned.
- `conjunction_public_resolved(left, right, *, …, env=None, local_lookup=None, acquisition=None)` orchestrates: `resolve_compat_chart` for each party under the caller's source policy → `EvaluationParty` → `evaluate_pair`. Its payload shape is `{"conjunction": {"left": {"person_uid": lo_uuid}, "right": {"person_uid": hi_uuid}, "compat": <magic10_compat_result.v1>}}` for eligible pairs, where `left`/`right` are the normalized lo/hi identities so AB and BA bytes are identical; the valid ineligible self-pair returns the canonical ineligible carrier of §5.5 with no core, cache, router or `pair_key`. The stable-hash success for lookup misses is removed.

### 5.4 Reader envelope — `engine/runtime/public.py`, `presenter/reader_v1/emitter.py`

- `emit_reader_public_envelope(a_chart, b_chart, *, engine_tag, invocation_tag, release_id, eligible, harmony_band=None)` keeps its symbol name (allowlisted by `tools/cli/emitter_symbol_proof.py`) and takes the band from the validated result's `harmony` category row instead of `ts_v0`; `eligible=False` emits `categories: []`. The envelope stays exactly `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`; `idempotence_hash` keeps the existing emitter preimage (G007 oracle). No `q`, score, UUID, Gate data, narrative key, config object or `pair_key` leaks. `presenter/reader_v1/emitter.py` remains the single emitter; it changes only if the band-input signature requires it, with no new presenter.

### 5.5 Public and internal carriers

| Surface | Post-PR04 contract |
| --- | --- |
| `POST /reader` (existing declared route, production; `v=1` required) | Body exactly `{"a_id": <uuid>, "b_id": <uuid>}` with lowercase canonical RFC-4122 strings; strict grammar check before any lookup (the internal alias bridge is unreachable here). Parameterized read-only `SELECT user_id, vendor, vendor_version, input_fingerprint, payload FROM public.hde_body_graphs_current WHERE user_id = %s AND vendor = 'hdapi'` per party through the existing DB-access abstraction (`engine.db.adapter.DBAccess`/`psycopg`, `DATABASE_URL` only); both rows must supply complete normalized projections. Success: 200, `magic10`-derived Reader envelope through the single emitter, headers `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`, no ETag, POST non-conditional (PF05 §5.3 A7). Errors: `no-store`, no ETag, tokens per §5.6. No writes, no vendor call, no UUID5 conversion, no fallback. Retains the current dev/production gating structure of the blueprint; `APP_ENV` gating is not loosened. |
| `GET /reader` (existing dev fixture route) | Path/`tz` contract unchanged (`ALLOWED_ROOT = fixtures/charts`, `_require_tz_or_raise`, ETag/304/HEAD); charts read from fixtures must be complete mapped projections with identities; the `tz` values are consumed by the existing route validation and stripped before the resolution seam. Fixtures `fixtures/charts/alice*.json`/`bob*.json` are upgraded to complete charts with UUID identities. |
| `hdctl showcompat` (eligible) | stdout is exactly the canonical `magic10_compat_result.v1` document plus one LF (PF05 §4.1.3); no `{a,b,viewer_prefs,compat}` wrapper. `--source db`/`auto` are DB-only (PF05 §4.1.2); the `auto`→`vendor` birth fallback is removed; `--source vendor` with birth flags goes through `resolve_compat_chart` class 3 (birth seed → `resolve_db_user_id` → local-first → guarded dry-run acquisition), never through `_derive_uid`, `_chart_for` synthesis or a parallel hash identity; `--a-file/--b-file`/stdin must carry complete mapped charts with identity (UUID, admitted alias, or a complete birth tuple in the file's declared birth fields; `person-` labels are not accepted literally). |
| `hdctl showcompat --dump-reader` / admin dumps | `--dump-reader` emits the envelope via `emit_reader_public_envelope(eligible=…, harmony_band=…)`; admin sidecars (`_emit_admin_dumps`) derive from the validated result (categories, bands, pair_key, config_id, release_id); `ts_v0` constants and feature dumps are removed. `aux_preview` pair-file parsing reads the `magic10_compat_result.v1` document (`meta`-free: `release_id` and `config_id` are top-level) instead of `data["compat"]["meta"]`. |
| `hdctl showcompat --conjunction` and dev conjunction HTTP routes | Payload `{"conjunction": {"left", "right", "compat"}}` as in §5.3; `left.person_uid`/`right.person_uid` are the normalized canonical UUIDs; dev routes no longer fabricate `local_people[uid] = {"person_uid": uid}` under open rails. Routes stay `APP_ENV` dev/test/local gated. |
| `POST /api/compat/v1` | Returns the `magic10_compat_result.v1` document (PF05 §5.5) with no top-level `keys`; `a_id`/`b_id` requests resolve through input class 2 (stored-user DB lookup with canonical UUID grammar); `a`/`b` inline objects must be complete mapped charts (class 1). Existing prod 404 guard and GET probe unchanged. |
| Valid complete self-pair (same UUID, equal projection) on internal/admin matrix surfaces (`showcompat`, conjunction, `/api/compat/v1`) | Exit 0 / 200 with the canonical JSON document `{"categories": [], "eligible": false}` plus one LF inside the existing `canonical_json` carrier — PF01 §4.7 emission carried onto the existing exit-0 carrier (PF05 §3.1.1) without fabricating a pure or internal result. **Decision D-03, flagged for Product Owner visibility in §14**; the Reader surfaces emit `eligible:false, categories: []` through the single emitter. |

### 5.6 Failure mapping

| Condition | Application boundary (`compute`, CLI, `/api/compat/v1`, dev conjunction) | `POST /reader` transport (PF05 §5.2.3) |
| --- | --- | --- |
| Missing chart / missing or empty Gates / missing required resolved identity | `ERR_READER_MISSING_PARAM` (existing token; CLI exit per existing governed mapping, stderr only) | `ERR_M10_BODYGRAPH_INCOMPLETE` 503 / `ERR_M10_GATES_MISSING` 422 |
| Invalid chart or Gates / conflicting identity slots / inconsistent self / wrong-row provenance | `ERR_READER_INVALID_CHART` | `ERR_M10_GATES_INVALID` 422 / `ERR_M10_BODYGRAPH_INCOMPLETE` 503 |
| Caller UUID grammar failure (`a_id`/`b_id`) | `ERR_COMPAT_INVALID_JSON` / existing 400 mapping on `/api/compat/v1` | `ERR_READER_INVALID_INPUT` 422 |
| Person row absent | existing missing-chart path (`ERR_NOT_FOUND` where the surface already uses it) | `ERR_M10_PERSON_UNRESOLVED` 404 |
| DB access unavailable | existing typed non-dev DB failure | `ERR_M10_RESOLVER_UNAVAILABLE` 503 |
| Admission refused (`INCOMPLETE_RELEASE_ROSTER`, manifest/config mismatch) | existing admission refusal propagated unchanged (no fallback) | `ERR_M10_CONFIG_SCHEMA_MISMATCH` / `ERR_M10_MANIFEST_SCHEMA_MISMATCH` 503 |
| Augmented result fails structural validation | `ERR_M10_RESULT_SCHEMA_MISMATCH` (internal), never printed as a matrix | 503 same token |
| Cache hit stale and not recomputable | `ERR_M10_STALE_RESULT` | 503 same token |
| Router key missing / shared_key disagreement | `ERR_MISSING_NARRATIVE_KEY` (existing) | 503 `ERR_M10_RESULT_SCHEMA_MISMATCH` (no narrative key leaks) |
| Closed rails on a permitted acquisition | `PROVIDER_REFUSED` / `PROVIDER_NETWORK_BLOCKED` at the provider boundary | not reachable (Reader never acquires) |
| Legacy type-only / birth-only file input on a file surface | `ERR_M10_LEGACY_INPUT_UNSUPPORTED` 422-class refusal on CLI/compat carriers | not reachable |

**Decision D-04.** The `ERR_M10_*` and `ERR_READER_INVALID_INPUT` tokens are exact current Canon (PF05 §5.2.3; the instruction §6.4 itself requires `ERR_M10_STALE_RESULT`) and are absent from `engine/compat/error_tokens.py` today. They are registered there and regenerated into `errors/token_map/token_map.json` **only through the owner generator** `python tools/errors/generate_error_artifacts.py`; no token is invented and no existing token, status or message changes. Application boundaries keep the existing `ERR_READER_MISSING_PARAM` / `ERR_READER_INVALID_CHART` mapping the instruction §6.6 prescribes. The PF01 §4.5 versus PF05 §5.2.3 naming tension is recorded as observation O-01 and decided by no one here. If the Product Owner prefers that PR04 register no new tokens, the `POST /reader` column collapses onto the existing `ERR_READER_*` tokens with the PF05 status codes; that is an ordinary in-scope adjustment within the same owned files, not a rescope.

## 6. Exact file and component plan

### 6.1 Owned implementation loci (instruction §7.1)

| Path | Exact change | Owner tests registered in §6.5 |
| --- | --- | --- |
| `engine/bodygraph/resolver.py` | Add private `ResolvedCompatChart` and `resolve_compat_chart` (§5.1); identity-slot cross-check helpers; dry-run/no-upsert acquisition wrapper around the existing `_resolve_vendor_v2_chart` / `V2ChartAdapterContext` / `adapt_v2_chart_payload` path and the preserved legacy `ingest_vendor_bodygraph(..., dry_run=True)` path; scoped env restore in `finally`. `resolve_bodygraph`'s public `bg:resolve` envelope, `_resolve_user_identity` and every existing entry point are preserved | `tests/bodygraph/test_resolve_compat_chart.py` (new), `tests/cli/test_bg_resolve.py`, `tests/db/test_bg_resolve_v2_mapped_cache.py` |
| `engine/bodygraph/projection.py` | Strict raw-Gates validation at mapped ingress before deduplication (`_validate_raw_gates`), identity-slot consistency helper, unchanged output keys of `project_bodygraph`; `BodyGraphProjectionError(code, field_path)` codes extended only with ingress codes | `tests/bodygraph/test_projection_gate_ingress.py` (new), `tests/bodygraph/test_gates.py` (unchanged PR02 owner, run as roster member) |
| `engine/bodygraph/v2_adapter.py` | Retain the complete `resolved` mapping together with the verified `V2ChartAdapterContext` on the adapter result; no fabricated field; `ChartSimpleResult`/missing-field/context-mismatch refusals unchanged | `tests/compat/test_hde_epic037_v2_adapter_to_compat.py`, `tests/bodygraph/test_resolve_compat_chart.py` |
| `engine/bodygraph/mapped_cache.py` | Read-only accessor returning the complete stored mapped payload with bound row identity for a canonical key, or `None`; no write path added or changed; closed-rails zero-I/O posture preserved | `tests/db/test_bg_resolve_v2_mapped_cache.py`, `tests/bodygraph/test_resolve_compat_chart.py` |
| `engine/bodygraph/ingest.py` | `resolve_db_user_id` unchanged; `ingest_vendor_bodygraph` dry-run path keeps `IngestOutcome.payload`; `_append_jsonl` callers tolerate a `None`/value-free log posture so the no-user dry-run seam emits no `user_id`; nothing else | `tests/db/test_ingest.py`, `tests/compat/test_conjunction_no_user_boundary.py` |
| `engine/compat/compute.py` | Remove `compat_public` and `_score_for` (hash scorer) with no successful replacement; add `EvaluationParty`, `validate_pair_eligibility`, `orient`, `evaluate_pair`, `_BUNDLE_PROVIDER`, injectable cache seam; rewrite `conjunction_public`, `conjunction_public_resolved`, `_resolve_party` (both UID-only returns replaced by chart-bearing results); keep `_derived_birth_uid` byte-identical | `tests/compat/test_evaluate_pair_eligibility.py` (new), `tests/compat/test_conjunction_no_user_boundary.py`, `tests/compat/test_hde_epic037_v2_adapter_to_compat.py` |
| `engine/http/compat_handler.py` | POST returns `magic10_compat_result.v1` (no `keys`); `a_id`/`b_id` → input class 2 with canonical UUID grammar; inline `a`/`b` → class 1; error mapping per §5.6; prod 404 guard and GET probe unchanged | `tests/http/test_compat_endpoint_contract.py`, `tests/adapter/test_compat_http_dev.py`, `tests/adapter/test_compat_http_parity.py` |
| `engine/runtime/public.py` | `emit_reader_public_envelope(..., eligible, harmony_band=None)`; band from the validated result; `ts_v0` import/use removed; symbol name retained for `tools/cli/emitter_symbol_proof.py` | `tests/runtime/test_identity.py`, `tests/http/test_reader_post_v1.py` (new) |
| `engine/narratives/router.py` | Expected unchanged. Touched only if the both-directions helper (`route_pair_keys(category, band)` → shared, personal lo→hi, personal hi→lo) is placed here instead of `compute.py`; behavior of `route_keys` never changes | `tests/unit/test_narratives_router.py`, `tests/unit/test_narratives_loader.py`, `tests/cli/test_aux_preview.py` (prefix owners) |
| `engine/cli/main.py` | Remove `_derive_uid` `cli-` synthesis, `_chart_for` type synthesis and the `auto`→`vendor` birth fallback; `_normalize_party`, `_person_and_chart_from_payload`, `_party_from_normalized`, `_conjunction_party_from_payload` preserve the complete chart and trusted identity context (names retained; incomplete input refuses); `_vendor_inputs_from_args` feeds input class 3 through `resolve_compat_chart`; `showcompat` stdout = `magic10_compat_result.v1`; `_emit_admin_dumps` derives from the validated result; `--dump-reader` uses the new envelope signature; `aux_preview` pair-file parsing reads the v1 result document; conjunction payload per §5.3; exit codes and stderr-only error carriers preserved | `tests/cli/test_showcompat_sources.py`, `tests/cli/test_showcompat_parity_and_identity.py`, `tests/cli/test_cli_file_inputs.py`, `tests/cli/test_cli_usage_and_errors.py`, `tests/cli/test_cli_canonical_bytes.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`, `tests/cli/test_aux_preview.py` |
| `adapter/http_reader.py` | Implement the `@bp.post("/reader")` success path (§5.5) through the existing DB-access abstraction; GET dev route consumes complete fixture charts and strips `tz` before the seam; dev conjunction routes stop fabricating `local_people[uid] = {"person_uid": uid}`; `_error`/`_writer_error` mapping for the §5.6 tokens; `_set_reader_200_headers` reused with POST non-conditional posture; `APP_ENV` gates unchanged | existing `_HTTP_READER_TEST_OWNERS` plus `tests/http/test_reader_post_v1.py` (new, registered as a direct owner) |
| `presenter/reader_v1/emitter.py` | Only if the band input signature requires it; single emitter; preimage unchanged (G007) | `tests/reader_v1/test_goldens.py`, `tests/reader_v1/test_schema.py`, `tests/runtime/test_identity.py` |
| `engine/compat/error_tokens.py` | Register the §5.6 PF05 §5.2.3 tokens (D-04) with their status codes and messages; no existing token changes | `tests/cli/test_errors_parity.py`, `tests/http/test_reader_post_v1.py` |
| `errors/token_map/token_map.json` (+ `errors/schema_check/*`, `parity/*` outputs of the same generator) | Regenerated only by `python tools/errors/generate_error_artifacts.py`; never hand-edited; path proof refreshed by the updater | `tests/cli/test_errors_parity.py` |

### 6.2 Necessary dependents (coherence, CI lanes and import safety)

| Path | Why it must change | Exact change |
| --- | --- | --- |
| `tools/evidence/run_canonical_json_gate.py` (release lane via sanity stage 03; a direct predicate input to the rails-lane gate through `generate_open_rails_abba_proof.py::canonical_gate()` and the determinism builder; registered evidence helper) | Imports `_party_from_normalized`, `compat_public`, `conjunction_public` and recomputes showcompat/conjunction capture bytes live; recompute cannot succeed without an admitted release (rc=1 under the RS-20 simulation) | Dual treatment, both stated: (a) necessary dependent — drop the removed imports; convert `_expected_showcompat_capture_bytes` / `_expected_conjunction_capture_bytes` to validation against the existing `_FROZEN_GENERATED_SHA256` entries; keep the 26 `EXPECTED_TARGET_PATHS` and six `EXPECTED_SET_RULES` unchanged; `--check-only` remains read-only and is expected to return 0 after (a); (b) F01 overlay file (§6.7 row 7) — only if C3 establishes that a check in this file necessarily requires live success may it express `RELEASE_NOT_ADMITTED`, never `PASS` |
| `tools/evidence/generate_open_rails_abba_proof.py` + `tests/evidence/test_open_rails_abba_proof.py` (rails lane `--check-current`; release-sanity stage 04) | `reader_bytes` uses `_party_from_normalized`; `cli_reader_bytes` shells out to `hdctl showcompat --dump-reader`; `build_fixture_proof()` predicates require Reader and CLI success | **F01 overlay file (§6.7 row 1).** Its test converts to in-process fixture-bundle injection for the success matrix and gains the non-admitted case; `--check-current` and `build_fixture_proof()` express `RELEASE_NOT_ADMITTED` per §6.7; frozen primary bytes stay frozen; write mode is not run. Register the generator in `_EVIDENCE_GENERATOR_TEST_OWNERS` → its test |
| `tools/cli/generate_showcompat_artifacts.py` + `tests/cli/test_showcompat_parity_and_identity.py::test_governed_showcompat_capture_uses_immutable_identity` (compat lane) | Birth-only stdin PAIR captures can no longer succeed and admission refuses pre-PR06 | `--check` validates the frozen captures under `artifacts/cli/showcompat/` by sha; generation refuses truthfully with `REQUIRES_ADMITTED_RELEASE`; the test asserts the frozen identity and the refusal. This generator is not a live CI gate, so the treatment is in scope; it is listed with F01 only because the same admission fact drives it |
| `tools/evidence/generate_hde_epic037_v2_to_compat.py` + `tests/compat/test_hde_epic037_v2_adapter_to_compat.py` | `_compat` calls `conjunction_public` with `person-epic037-pr04-a` labels | `_compat` builds `ResolvedCompatChart`-derived `EvaluationParty` values and calls `evaluate_pair` with the injected fixture bundle in check mode; frozen EPIC037 artifacts stay with a nonclaim; register the generator → its test |
| `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` + `tests/evidence/test_epic030_pr05_category_framework_evidence.py` | Module-level `from engine.compat.compute import compat_public` breaks at import | Migrate the `compat_admin` computation to `evaluate_pair` behind the fixture-bundle seam; check mode preserved; write mode not run; register the generator → its test |
| `tools/evidence/generate_determinism_gate_proofs.py` + `tests/evidence/test_determinism_gate_proofs.py` | Module-level import of `_normalize_party`, `_party_from_normalized`; write-mode test `test_main_write_mode_produces_exact_expected_files` runs generation; its `build()` is release-sanity stage 04 | Names remain importable; in tests generation runs with complete fixture charts and the injected bundle inside redirected outputs; committed evidence unchanged (`test_check_mode_model_matches_committed_after_generation` guards it); as an F01 overlay file (§6.7 row 3) `build()` expresses `RELEASE_NOT_ADMITTED` when admission refuses and writes nothing; register the generator → its test |
| `tools/evidence/generate_bodygraph_policy_proofs.py` (owner of `artifacts/bodygraph/source_selection.snapshot.json`, `source_invariance/{ab,ba,summary}.json`) | Source-selection policy changes (auto fallback removed; local-first no-user; dry-run posture) change the snapshot content | Regenerate in write mode from the candidate root, then updater; `--check` in CI. Register the generator → `tests/evidence/test_bodygraph_policy_proofs.py` |
| `tests/runtime/test_identity.py` (release lane) | `emit_reader_public_envelope` signature | Update call sites; identity assertions unchanged |
| `fixtures/charts/alice*.json`, `bob*.json` | GET dev route and A7/reader tests need complete charts with UUID identities | Complete mapped projections; classifier rule for `fixtures/charts/` (§6.5) |
| `tests/compat/test_compat_public_ab_ba_identity.py`, `tests/compat/test_compat_public_lf_bom.py`, `tests/epic003/test_meta_invocation_ok.py` | Import `compat_public` | Convert to `evaluate_pair`/`conjunction_public` over complete fixtures with the injected bundle; assertions keep their meaning (AB/BA identity, LF/no-BOM bytes, meta/invocation) |
| `tests/http/test_dev_conjunction_http.py`, `tests/http/test_reader_a7_transport.py`, `tests/http/test_endpoint_catalog.py` | Dev conjunction payload shape; `POST /reader` no longer 405; catalog unchanged | Convert expectations (bundle injection; POST without a JSON body → 422 `no-store`, no ETag); the catalog test is unchanged in substance |
| `tools/evidence/generate_a7_transport_proofs.py` + `tests/transport/test_a7_transport_proofs.py` (release-sanity stage 05; full-validation roster) | `capture()` requires live `GET /reader` 200 and `POST /reader` 405; six roster tests call `build()` live | **F01 overlay file (§6.7 row 2).** The POST expectation becomes the PF05 §5.3 non-conditional POST fact (422 `no-store`, no ETag, `If-None-Match` ignored); `build()` expresses `RELEASE_NOT_ADMITTED` when the GET path refuses on admission; the tests inject the bundle in-process for the success path and assert the non-admitted path; committed A7 artifacts stay frozen with a nonclaim (observation O-03). Register the generator → its test |
| `scripts/cli/canonical_harness.py`, `scripts/make_compat_determinism_artifacts.py`, `tools/presenter/generate_presenter_artifacts.py` | Import-safe after PR04 (`_party_from_normalized` retained; `getattr(mod, "compat_public", None)` degrades) and outside every CI lane's execution path | Untouched, known-stale write mode; owner PR06 |

`engine/emit_public.py` was checked and does not use any removed helper; it is unchanged.

### 6.3 Existing evidence families: what PR04 regenerates and what stays frozen

| Family | Owner writer | PR04 action |
| --- | --- | --- |
| `artifacts/bodygraph/source_selection.snapshot.json`, `artifacts/bodygraph/source_invariance/{ab,ba,summary}.json` (+ path proofs) | `tools/evidence/generate_bodygraph_policy_proofs.py` | Regenerate (write) from the candidate root, primary bytes first, if and only if the snapshot content changes; then updater; then `--check` |
| `errors/token_map/token_map.json`, `errors/schema_check/*`, `parity/*` | `tools/errors/generate_error_artifacts.py` | Regenerate after token registration; then updater |
| Canonical JSON gate frozen SHAs and logs under `audit/gates/json_gate/canonical/` | `tools/evidence/run_canonical_json_gate.py` | Validation logic changes only; `--check-only` must pass against existing frozen bytes; a write run happens only if the gate's own log format changes, which this plan does not require |
| EPIC022 D2 CLI captures `artifacts/cli/showcompat/*`, compat AB/BA determinism artifacts, presenter parity bytes, A7 transport proofs, open-rails ABBA primary bytes, EPIC030 PR-05 evidence, EPIC037 PR-04 v2-to-compat evidence, EPIC038 evidence | their existing writers | **Frozen capture-time records with explicit nonclaims.** They cannot be truthfully regenerated before PR06 admits a complete release; PR06 owns convergence. Check modes that are pytest-only convert to frozen-byte validation plus in-test bundle injection; check modes that are live CI gates (open-rails `--check-current`, sanity stages 04/05, A7 live build) express `RELEASE_NOT_ADMITTED` under the approved F01 overlay (§6.7) |
| `goldens/reader/v1/*` (G001–G008) | none (governed goldens) | Unchanged; `tests/reader_v1/test_goldens.py` and `test_schema.py` keep passing |
| `docs/ENDPOINTS_CATALOG.json`, `artifacts/audit/ENDPOINTS_CATALOG.json` | catalog owner | Unchanged by PR04 (no new route; POST success at the declared route); the missing `POST /reader` success row is observation O-03 for PR07/PO |
| `schemas/reader.v1.schema.json` | schema owner | Unchanged (observation O-04) |

### 6.4 Canonical updater-owned companions

After every primary byte in §6.1–§6.3 is final, run once: `python tools/evidence/update_evidence_index.py` (owns `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256`, `audit/gates/topology/orientation_demo.txt` and proof companions as one transaction). Then only read-only validation: `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `ci/checks/check_mirror_schema.sh`, `python tools/evidence/validate_evidence_paths.py`, `python tools/evidence/check_lf_endings.py`, `ci/checks/check_evidence_index_hash.sh`, `ci/checks/check_final_lf.sh`. No governed artifact is hand-edited; the mirror self-record row is never dropped.

### 6.5 CI ownership seam — `ci/checks/classify_ci_changes.py`

| Registration | Entries |
| --- | --- |
| `_PRODUCT_TEST_OWNER_PATHS` additions | `engine/compat/compute.py` → (`tests/compat/test_evaluate_pair_eligibility.py`, `tests/compat/test_conjunction_no_user_boundary.py`, `tests/compat/test_hde_epic037_v2_adapter_to_compat.py`); `engine/bodygraph/resolver.py` → (`tests/bodygraph/test_resolve_compat_chart.py`, `tests/cli/test_bg_resolve.py`, `tests/db/test_bg_resolve_v2_mapped_cache.py`); `engine/bodygraph/projection.py` → (`tests/bodygraph/test_projection_gate_ingress.py`, `tests/bodygraph/test_resolve_compat_chart.py`); `engine/bodygraph/v2_adapter.py` → (`tests/compat/test_hde_epic037_v2_adapter_to_compat.py`, `tests/bodygraph/test_resolve_compat_chart.py`); `engine/bodygraph/mapped_cache.py` → (`tests/db/test_bg_resolve_v2_mapped_cache.py`, `tests/bodygraph/test_resolve_compat_chart.py`); `engine/bodygraph/ingest.py` → (`tests/db/test_ingest.py`, `tests/compat/test_conjunction_no_user_boundary.py`); `engine/runtime/public.py` → (`tests/runtime/test_identity.py`, `tests/http/test_reader_post_v1.py`); `engine/cli/main.py` → (`tests/cli/test_showcompat_sources.py`, `tests/cli/test_showcompat_parity_and_identity.py`, `tests/cli/test_cli_file_inputs.py`, `tests/cli/test_cli_usage_and_errors.py`, `tests/cli/test_cli_canonical_bytes.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`); `engine/http/compat_handler.py` → (`tests/http/test_compat_endpoint_contract.py`, `tests/adapter/test_compat_http_dev.py`, `tests/adapter/test_compat_http_parity.py`); `presenter/reader_v1/emitter.py` → (`tests/reader_v1/test_goldens.py`, `tests/reader_v1/test_schema.py`, `tests/runtime/test_identity.py`); `engine/compat/error_tokens.py` → (`tests/cli/test_errors_parity.py`, `tests/http/test_reader_post_v1.py`) |
| `_HTTP_READER_TEST_OWNERS` addition | `tests/http/test_reader_post_v1.py` (direct importer of `adapter.http_reader`; `tests/evidence/test_http_reader_ci_ownership.py` must keep passing) |
| `_EVIDENCE_GENERATOR_TEST_OWNERS` additions | `tools/evidence/generate_open_rails_abba_proof.py` → `tests/evidence/test_open_rails_abba_proof.py`; `tools/evidence/generate_hde_epic037_v2_to_compat.py` → `tests/compat/test_hde_epic037_v2_adapter_to_compat.py`; `tools/evidence/generate_epic030_pr05_category_framework_evidence.py` → `tests/evidence/test_epic030_pr05_category_framework_evidence.py`; `tools/evidence/generate_determinism_gate_proofs.py` → `tests/evidence/test_determinism_gate_proofs.py`; `tools/evidence/generate_bodygraph_policy_proofs.py` → `tests/evidence/test_bodygraph_policy_proofs.py` |
| New lane rule | `fixtures/charts/` → `{product, compat, release}` with owners (`tests/http/test_reader_a7_transport.py`, `tests/http/test_reader_post_v1.py`) so the fixture upgrade classifies instead of raising `CI_CHANGE_SURFACE_UNCLASSIFIED` |
| Unchanged | `_FULL_VALIDATION_*`, `_DOCUMENTATION_PREFIXES`, `_HISTORICAL_PREFIXES`, `_RELEASE_EVIDENCE_PREFIXES`, `tests/config/helpers.py` registration, PR03 registrations |

Every owner target must exist as a regular file at the candidate head (`_validated_owner_targets` raises `CI_PRODUCT_OWNER_TEST_INVALID` otherwise), so new test modules land in the same commit as their registrations. Because the classifier changes, the candidate runs under full validation. The §6.7 files need no further registration: `run_sanity_pipeline.py`, `run_sanity_pipeline_gate.py`, `build_release_attestation.py` and `run_canonical_json_gate.py` are registered evidence helpers; the three generators are registered above; `.github/workflows/ci.yml` is a full-validation prefix; `ci/jobs/*.yml` classify to rails + release; the four test homes are existing test modules.

### 6.6 Explicitly unchanged paths

`engine/core/core.py`, `engine/magic10/*`, `engine/bodygraph/gates.py`, `engine/config/registry_loader.py`, `engine/config/bundles.py`, `catalog/**` (including `catalog/manifest.json`), `schemas/magic10_*.json`, `schemas/channels_v1.schema.json`, `schemas/reader.v1.schema.json`, `migrations/**`, `engine/db/**`, `engine/bodygraph/vendor_client.py`, `tests/config/helpers.py`, `goldens/**`, `docs/pfcanon/**`, `docs/ENDPOINTS_CATALOG.json`, `.github/workflows/ci.yml` (no lane-list change is expected; new tests run as registered owners and roster members), `ci/jobs/rails_closed_refusal.yml`, `ci/jobs/logs_keys_only_redaction.yml`, `tools/evidence/run_sanity_pipeline_gate.py`'s and `tools/evidence/build_release_attestation.py`'s success paths and schema (changed only within the §6.7 bounds), `tests/evidence/test_release_attestation.py` (excluded on execution: fully green under the RS-20 simulation; it pins `PR06R_B_FINAL_PASS`, which binding condition 4 forbids changing), `tests/evidence/test_release_manifest_content_binding.py` (untouched; its failure is candidate finding F02, §14.3), and every known-stale write-mode script in the last row of §6.2.

### 6.7 Approved F01 overlay — truthful non-admitted gate outcome (PF10 §2.15)

Purpose, exactly as approved: the affected gates express an explicit `RELEASE_NOT_ADMITTED` outcome instead of an ambiguous failure, and ordinary CI accepts that one outcome while the active release is not admitted. Binding conditions carried verbatim in substance: (1) the outcome is never `PASS`, never `top_level_pass: true`, never a frozen-byte substitute presented as a live result; (2) CI acceptance keys on that one explicit outcome **and** on the observed non-admitted state of the active release — never on a generic failure, a lane name, a job name or a time window, and never on an unrelated failure in those lanes; (3) the acceptance is self-extinguishing by construction (conditioned on the runtime-observable admission state; once PR06 admits the 44-member roster the branch is never taken) — no removal is owed and no cleanup unit or PR is created; (4) no change to the `hde.release_attestation.v1` success schema or the `PR06R_B_FINAL_PASS` wire value. Ownership limit: the touch on `build_release_attestation.py` is bounded to emitting the distinct non-admitted code on the existing failure-receipt path and to the withholding the builder already performs; success attestation, promoted roster, release identity, manifest cut and the owning attestation validator remain PR06's.

**Admission-state discriminator (shared design, no new file).** Each gate probes the admission owner through its public entry `engine.config.registry_loader.load_active_mechanics_bundle()` and classifies exactly one refusal as non-admitted: the `SchemaValidationError` whose code is `INCOMPLETE_RELEASE_ROSTER` (observed message: `release manifest does not yet contain the complete adopted roster`). Every other exception, and every failure after a successful admission, remains an ordinary failure. C3 verifies the exact exception attribute carrying the code before relying on it; the probe is read-only and never relaxes, bypasses or relocates admission (PF10 §2.12). The synthetic test-only release is never fed to any gate or to the attestation.

| # | File | Exact change |
| --- | --- | --- |
| 1 | `tools/evidence/generate_open_rails_abba_proof.py` | `build_fixture_proof()` probes admission first; when non-admitted it returns a proof with `outcome: "RELEASE_NOT_ADMITTED"`, `top_level_pass: False`, every live predicate `False`/unevaluated and `transport_call_count: 0`, and performs no live Reader or CLI capture. `validate_current_fixture()` / `--check-current` exit with a distinct documented code (not 0, not the generic failure) after printing `OPEN_RAILS_ABBA_CHECK:RELEASE_NOT_ADMITTED`, write nothing and validate that the frozen primary at its recorded path is byte-identical to its recorded hash (a frozen-byte *check*, never presented as a live proof). When admitted, behavior is unchanged. |
| 2 | `tools/evidence/generate_a7_transport_proofs.py` | `capture()`'s POST requirement becomes the PF05 §5.3 A7 non-conditional POST fact (`POST /reader` with query-only input → 422 `ERR_READER_INVALID_INPUT`, `Cache-Control: no-store`, no ETag, `If-None-Match` ignored). When `GET /reader` refuses on admission, `build()` raises a typed `ReleaseNotAdmitted` (not `AssertionError`); `main --check` prints `A7_TRANSPORT_CHECK:RELEASE_NOT_ADMITTED` and exits with the distinct code; write mode refuses. The composite/proof schemas and `PROOFS` roster are unchanged; committed A7 artifacts stay frozen (O-03). |
| 3 | `tools/evidence/generate_determinism_gate_proofs.py` | `build()` probes admission; when non-admitted it raises `ReleaseNotAdmitted` before any live Reader envelope or CLI subprocess; `main --check` prints `DETERMINISM_GATE_CHECK:RELEASE_NOT_ADMITTED` and exits with the distinct code; write mode writes none of its six outputs (`audit/gates/parity/reader_cli/ab.json`, `ba.json`, `summary.json`, `audit/gates/determinism/abba.bytes`, `audit/gates/determinism/tworun_identity.sha256`, `artifacts/cards/a3/IDENTITY_OK.txt`). |
| 4 | `tools/evidence/run_sanity_pipeline.py` | Stage 04 and 05 validators catch `ReleaseNotAdmitted` (and the distinct exit code from subprocess commands) and return a third status; `_run_stage` returns a distinct code for it; `_render_log` renders `check NN <name>:NOT_ADMITTED` (a third token beside `OK`/`FAIL`), later stages still execute, and the summary renders `summary:NOT_ADMITTED` with `first_failed_stage:NONE` when no stage failed and at least one is `NOT_ADMITTED`; `summary:PASS` requires every stage `OK` exactly as today. The pipeline exit code for `NOT_ADMITTED` is the distinct code, never 0. |
| 5 | `tools/evidence/run_sanity_pipeline_gate.py` | Recognizes the `NOT_ADMITTED` rendering as a distinct valid non-pass log (byte-exact model), exits with the distinct code, and continues to fail on `summary:FAIL`, malformed logs or a log that is neither the exact PASS model nor the exact NOT_ADMITTED model. |
| 6 | `tools/evidence/build_release_attestation.py` | When the `release_sanity` stage ends `NOT_ADMITTED`, raise `AttestationBuildError("release_not_admitted")` so the existing failure-receipt path writes `hde.release_attestation.failure.v1` with `code: release_not_admitted`, `stage: release_sanity`; no bundle, no success attestation, no `PR06R_B_FINAL_PASS`; existing behavior otherwise unchanged. |
| 7 | `tools/evidence/run_canonical_json_gate.py` | Primary treatment is §6.2 (frozen-SHA validation; expected rc 0). Only where C3 proves a check necessarily needs live success does it express `RELEASE_NOT_ADMITTED` (distinct code, explicit line), never `PASS`. |
| 8 | `.github/workflows/ci.yml` | Rails step: unchanged command; the job-definition runner surfaces the open-conformance job's accepted outcome (row 9). Release step: run `build_release_attestation.py --output … --require-clean`; on a non-zero exit, accept **only** when the written failure receipt has `code == release_not_admitted` **and** an independent read-only probe of `load_active_mechanics_bundle()` in the same step observes `INCOMPLETE_RELEASE_ROSTER`; then log `RELEASE_LANE:RELEASE_NOT_ADMITTED`, skip `--verify` (no bundle exists), and keep the clean-tree assertions. Any other non-zero exit fails as today. |
| 9 | `ci/jobs/rails_open_conformance.yml` | The `--check-current` step declares the distinct non-admitted exit code as its accepted outcome alongside 0, in the job definition's native shape, and its `proves` list states the corrected behavior. No change to `ci/checks/run_rails_job_definitions.py`. |

Test homes (four): `tests/evidence/test_sanity_pipeline.py` (third status token, `NOT_ADMITTED` summary, gate-wrapper acceptance of the exact NOT_ADMITTED model, rejection of everything else, PASS model unchanged); `tests/evidence/test_open_rails_abba_proof.py` (positive matrix under injected bundle; non-admitted proof shape; `--check-current` distinct code; no write); `tests/evidence/test_rails_ci_workflow_integration.py` (updated workflow/job-definition pins, including the residue test under `INCOMPLETE_RELEASE_ROSTER`); `tests/transport/test_a7_transport_proofs.py` (success matrix under injected bundle; `ReleaseNotAdmitted` path; POST 422 fact). `tests/evidence/test_release_attestation.py` stays out and must stay green.

Governed evidence: the tracked `audit/gates/sanity_pipeline/sanity_pipeline.log` (+ path proof) is regenerated only by its owner if the owner's canonical run changes its bytes; the six determinism outputs are regenerated only by their owner and only if the owner can truthfully render them — under non-admission it writes nothing, so they stay frozen with their path proofs; then `python tools/evidence/update_evidence_index.py` once. Nothing is hand-edited. The result record (§10.6) states which of these were regenerated and which stayed frozen, and why.

## 7. Requirement-to-change-and-test mapping

| Requirement / criterion (Specification v1.1) | PR04-owned portion | Change (§6) | Decisive tests |
| --- | --- | --- | --- |
| `K040-REQ-001` one coherent implementation burden | The successful no-user/admin resolution boundary per Plan §§5.8/6.4 delivered as one coherent slice | §6.1 complete; §6.2 dependents; §6.5 ownership | Whole §8 suite green under full validation; `CI_APPLICABILITY_AND_EXACT_HEAD_OK` |
| `K040-REQ-004` preserve non-scoring Product metadata and FE/BE compatibility | Public Reader six-key envelope and `magic10_compat_result.v1` unchanged in shape; no public field added | §5.4, §5.5 | `tests/reader_v1/test_schema.py`, `tests/reader_v1/test_goldens.py`, `tests/http/test_reader_post_v1.py` forbidden-field assertions, `tests/http/test_compat_endpoint_contract.py` |
| `K040-REQ-005` governed result schemas, no second scoring implementation | Consumers emit only `compute_core` results validated against `schemas/magic10_compat_result_v1.schema.json`; hash scorer removed | §5.3 step 7; `compat_public` removal | `tests/compat/test_evaluate_pair_eligibility.py::test_result_validates_against_governed_schema`, grep-guard test that `compat_public`/`_score_for`/`ts_v0` no longer exist in `engine/compat/compute.py`, `engine/runtime/public.py`, `engine/cli/main.py` |
| `K040-REQ-007` one immutable typed bundle loaded outside Engine Core; one active configuration per release | Consumers obtain the bundle only via `_BUNDLE_PROVIDER` (default `load_active_mechanics_bundle`); `release_id` from the bundle; no reload/re-admit/bypass | §5.3 | `test_bundle_provider_refusal_propagates_without_fallback` (real provider → `INCOMPLETE_RELEASE_ROSTER` refusal), `test_release_id_equals_bundle_release_id` |
| `K040-REQ-008` reject missing/extra/duplicate/malformed/out-of-domain/unresolved/stale inputs without partial result or fallback | Gate ingress refusals; identity refusals; stale cache refusal; admission refusal propagation; no vendor/DB fallback | §5.1, §5.2, §5.3, §5.6 | §8.2 adverse matrix; `tests/bodygraph/test_projection_gate_ingress.py`; `tests/cli/test_showcompat_sources.py` no-fallback spies |
| `K040-REQ-010` exact golden comparison, read-only | G007/G008 oracles reproduced through canonical behavior; goldens untouched; PR05 owns full comparison | §3.2 item 6 | `test_g007_reader_preimage_oracle`, `test_g008_fingerprint_and_pair_key_oracle` in `tests/compat/test_evaluate_pair_eligibility.py`; `tests/reader_v1/test_goldens.py` |
| `K040-REQ-011` raw Gate-ingress rejection and canonical normalization; canonical bytes; deterministic identity; read-only current-row capability | Ingress rejection at every mapped ingress; canonical JSON + single LF on every carrier; AB/BA identity; POST `/reader` read-only current-row lookup (readiness capability itself is PR05) | §5.2, §5.5 | `tests/cli/test_cli_canonical_bytes.py`, `tests/cli/test_showcompat_parity_and_identity.py`, `tests/http/test_reader_post_v1.py::test_lookup_is_parameterized_read_only_current_rows` |
| `K040-REQ-012` produce and index governed evidence through owners | Affected families regenerated by their writers; updater run; check modes green | §6.3, §6.4 | `tests/evidence/test_bodygraph_policy_proofs.py`, `tests/cli/test_errors_parity.py`, evidence lane checks |
| `K040-REQ-013` exact identities; no replacement token system | Result record carries exact commit/PR/test identities; no acceptance token issued | §10.4, §15 | Result artifact review under PR-35 |
| `AC040-03` closed pure/internal result schemas | Every emitted matrix validates against the governed schema; no extra keys | §5.3 | `test_result_validates_against_governed_schema`, `tests/http/test_compat_endpoint_contract.py::test_no_keys_field` |
| `AC040-04` immutable fail-closed consumption | Bundle consumed through the seam; each decisive invalid class refuses without fallback | §5.3, §5.6 | §8.2 rows; `test_bundle_provider_refusal_propagates_without_fallback` |
| `AC040-06` exact read-only comparison; AB/BA and repeated identity | AB/BA byte identity on compute, CLI stdout, `/api/compat/v1`, conjunction and Reader; repeated-run identity | §5.3 | `test_ab_ba_bytes_identical_*` in every carrier home; `tests/compat/test_compat_public_ab_ba_identity.py` (converted) |
| `AC040-07` Gate ingress and current-row readiness | Ingress refusal matrix; POST `/reader` current-row read-only lookup with no acquisition | §5.2, §5.5 | `tests/bodygraph/test_projection_gate_ingress.py`; `tests/http/test_reader_post_v1.py` |
| `AC040-08` integrated selected proof and governed artifacts | Six `R040-IA30-02` proof classes; evidence regenerated by owners with coherent Index/Mirror/hash/path-proof | §8.1, §6.3–6.4 | §8.1 homes; `update_evidence_index.py --check`; `check_mirror_schema.sh` |
| F01 overlay — PF10 §2.15 (`K040-REQ-012`, `AC040-08`, CI clause of completion) | Truthful `RELEASE_NOT_ADMITTED` outcome in the affected gates; attestation withholds; CI accepts the one outcome only while non-admitted | §6.7 | §8.7 tests; release lane accepted-outcome log; failure receipt `code == release_not_admitted`; `tests/evidence/test_release_attestation.py` green |
| `AC040-09` boundary and decision integrity | Reader bands-only/numeric-free; no new surface; internal projections do not rescore or change identity; attributable native evidence | §5.4, §5.5, §15 | `tests/http/test_reader_post_v1.py::test_forbidden_fields_absent`, `tests/cli/test_showcompat_sources.py`, PR-35 review record |

## 8. Detailed test design

All tests run under `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1` with `-p no:cacheprovider`. Every positive test injects the synthetic complete release through `engine.compat.compute._BUNDLE_PROVIDER` (monkeypatched to return `_load_active_mechanics_bundle_from_root(synthetic_complete_release_root(tmp_path))`) and presets `engine.narratives.state._PACK = load_pack(Path("catalog/narratives"), tmp_path / "narratives")` in an autouse fixture, so no test writes into the repository tree. Fixtures are complete source-bound mapped `ChartResult` projections derived from `tests/fixtures/bodygraph/source_invariance/*.json`, with every projection field, valid Gates and synthetic UUIDs; no fixture claims a live vendor result.

### 8.1 The six `R040-IA30-02` proof classes

| Class | Home | Input, seam and decisive assertions |
| --- | --- | --- |
| 1. Successful no-user boundary | `tests/compat/test_conjunction_no_user_boundary.py::test_birth_only_no_user_success_through_real_boundary` | Call the real `conjunction_public_resolved` with two complete birth tuples and no `person_uid`/`user_id`/app ID. A fixture `local_lookup` keyed by canonical UUID returns complete charts. Assert: each key equals `str(UUID(resolve_db_user_id(_derived_birth_uid(raw))))`; the `EvaluationParty` values captured at the handoff (spy on `evaluate_pair` that delegates to the real function) carry canonical UUIDs, complete projections, `NormalizedGates` and fingerprints; the real `compute_core` ran (spy count 1, delegating); AB and BA bytes identical; two runs identical; no vendor client call; no ingest write; no `user_id` in captured logs |
| 2. Successful permitted acquisition seam | `tests/compat/test_conjunction_no_user_boundary.py::test_local_miss_permitted_acquisition_returns_complete_chart` and `tests/bodygraph/test_resolve_compat_chart.py` | Local miss with `source_policy="vendor"`, guarded test-only acquisition: a fake transport returns a complete full `ChartResult` payload into the existing `_resolve_vendor_v2_chart`/`adapt_v2_chart_payload` path in dry-run posture. Assert: context identity comes from the resolver; complete chart retained; the scoped env is restored and closed before `evaluate_pair` is entered (ordering spy); no DB or account write (`ingest_vendor_bodygraph` not called with `dry_run=False`; mapped-cache write seam not called); no network socket opened (fake transport only); no rails opened by the resolver |
| 3. Closed-rails miss | `tests/compat/test_conjunction_no_user_boundary.py::test_closed_rails_miss_refuses_without_evaluation` (conversion of the current stable-hash success case) | Two valid birth tuples, `local_lookup` → `None`, `SAFE_MODE=1 ALLOW_NETWORK=0`. Assert the owning refusal (`PROVIDER_REFUSED`/`PROVIDER_NETWORK_BLOCKED` mapped per §5.6), `evaluate_pair`, cache and router never called, no vendor call, no write, no `person_uid` success value anywhere |
| 4. Missing/invalid chart and identity | `tests/compat/test_evaluate_pair_eligibility.py`, `tests/bodygraph/test_projection_gate_ingress.py`, `tests/cli/test_cli_file_inputs.py`, `tests/http/test_reader_post_v1.py` | Parametrized rows: missing chart; missing Gates; empty Gates; `[10, "10"]`; `[true]`; `"010"`; `" 10"`; `"+10"`; `10.0`; `0`; `65`; unresolved catalog ref; malformed full shape (missing `profile`); unresolved identity; identity-slot mismatch; wrong-row provenance; profile-only inconsistent self → refuse before evaluator/cache/router with the §5.6 token. Positive controls: distinct-person/equal-mask success; valid complete-self ineligible |
| 5. Source and prohibited-side-effect matrix | `tests/cli/test_showcompat_sources.py` plus boundary homes | Spies on `_fetch_db_bodygraph`, vendor client `post`, `ingest_vendor_bodygraph`, mapped-cache write and `DBAccess` execute: complete file/stdin → no DB, no vendor; `db`/`auto` miss → no vendor, missing-chart failure; explicit `vendor` → guard honored, no silent DB substitution; local-first hit → no vendor; every conjunction path → no write; POST `/reader` and readiness → no vendor, no write on success and failure; stderr/stdout contain no birth tuple, chart, UUID (on error paths) or key; legacy-wrapper assertions replaced by the full internal matrix contract |
| 6. Separate Reader/internal regressions | `tests/http/test_reader_post_v1.py`, `tests/reader_v1/*`, `tests/runtime/test_identity.py`, `tests/cli/test_showcompat_parity_and_identity.py` | Strict caller-UUID Reader tests and the G007/G008 oracles stay separate from internal alias/admin tests and from class 1. A successful Reader fixture satisfies no no-user obligation. All eight G001–G008 goldens, full result schema/byte/hash assertions preserved |

### 8.2 Eligibility, identity and orientation matrix (`tests/compat/test_evaluate_pair_eligibility.py`)

| Case | Expected |
| --- | --- |
| Same UUID, equal complete projection | `ineligible_self`; `compute_core`, cache and router spies untouched; carrier `{"categories": [], "eligible": false}`; Reader `eligible:false, categories: []` |
| Same UUID, profile-only difference | `ERR_READER_INVALID_CHART`; nothing evaluated |
| Same UUID, Gate difference | `ERR_READER_INVALID_CHART` |
| Distinct UUIDs, equal masks | eligible; full result; orientation tie broken by UUID ASCII order; AB == BA bytes |
| Distinct UUIDs, distinct masks | eligible; lo/hi by mask; AB == BA bytes |
| Router `shared_key` disagreement between directions (fault-injected pack) | `ERR_MISSING_NARRATIVE_KEY`; no partial result |
| Missing narrative key sentinel | `ERR_MISSING_NARRATIVE_KEY` |
| Injected cache hit with valid schema and matching `pair_key`/`config_id`/`release_id` | served; `compute_core` spy 0 |
| Injected cache hit with mismatched `release_id` and both Gate sets valid | recomputed; result equals fresh compute |
| Injected cache hit stale and one party invalid | `ERR_M10_STALE_RESULT` |
| Alternate UUID pair with identical masks/Gates | cache key differs only when identity differs and the cache value binds both fingerprints; no cross-pair narrative contamination |
| Real `_BUNDLE_PROVIDER` (no injection) | `INCOMPLETE_RELEASE_ROSTER` refusal propagates; no fallback; no partial result |
| Result structural validation | validates against `schemas/magic10_compat_result_v1.schema.json`; `release_id == bundle.release_id`; `config_id == bundle.config_id`; category rows carry `category_id, score, band, shared_key, personal_lo_to_hi_key, personal_hi_to_lo_key` |
| G007 / G008 | Reader preimage hash `8214324e…`, fingerprint `7567338a…`, pair_key `8a75eafc…` reproduced from the PF01 §9.5 inputs |

### 8.3 Reader POST (`tests/http/test_reader_post_v1.py`, Flask test client, `DBAccess` faked at the abstraction boundary)

Missing `v=1` → existing version error; body not exactly `{a_id, b_id}` / uppercase or braced UUID / extra keys → `ERR_READER_INVALID_INPUT` 422 with `no-store`, no lookup performed; unknown person → `ERR_M10_PERSON_UNRESOLVED` 404; DB unavailable → `ERR_M10_RESOLVER_UNAVAILABLE` 503; row payload incomplete → `ERR_M10_BODYGRAPH_INCOMPLETE` 503; invalid Gates in row → `ERR_M10_GATES_INVALID` 422; admission refused → 503 schema-mismatch token; success → 200, six keys only, band-only category row, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`, no `ETag`, `If-None-Match` ignored (no 304), identical bytes for `(a_id,b_id)` and `(b_id,a_id)`, same UUID twice with equal rows → `eligible:false`, `categories: []`; the SQL passed to the fake is parameterized (`%s` placeholders, `vendor = 'hdapi'`, view `public.hde_body_graphs_current`) and read-only (no `INSERT`/`UPDATE`/`DELETE`/`CALL` ever issued); vendor client never imported/called; production `APP_ENV` behaves per existing gates. GET dev route regression: `tz` still required; fixtures complete; ETag/304/HEAD behavior unchanged.

### 8.4 CLI and compat HTTP carriers

`tests/cli/test_showcompat_sources.py`, `tests/cli/test_cli_file_inputs.py`, `tests/cli/test_showcompat_parity_and_identity.py`, `tests/cli/test_cli_canonical_bytes.py`, `tests/cli/test_cli_usage_and_errors.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`, `tests/cli/test_aux_preview.py`, `tests/http/test_compat_endpoint_contract.py`, `tests/adapter/test_compat_http_dev.py`, `tests/adapter/test_compat_http_parity.py`, `tests/http/test_dev_conjunction_http.py`: stdout is the canonical `magic10_compat_result.v1` document + one LF (no wrapper); stderr carries errors only; exit codes unchanged per the existing governed mapping; `--dump-reader` envelope six keys; admin sidecars derived from the validated result with no `ts_v0` constant; `auto` with birth flags refuses/misses without vendor; file inputs with `person-` labels and no trusted context refuse; `aux-preview` reads the v1 document; `/api/compat/v1` returns the document with no `keys`; dev conjunction payload shape per §5.3; self-pair carrier per D-03.

### 8.5 Conversions of existing tests

`tests/compat/test_conjunction_no_user_boundary.py` (stable-hash success → class 3 negative + classes 1–2 positives); `tests/compat/test_compat_public_ab_ba_identity.py`, `tests/compat/test_compat_public_lf_bom.py`, `tests/epic003/test_meta_invocation_ok.py` (to `evaluate_pair`); `tests/http/test_compat_endpoint_contract.py` (`keys` assertions removed; document assertions added); `tests/cli/test_showcompat_parity_and_identity.py::test_governed_showcompat_capture_uses_immutable_identity` (frozen capture + refusal); `tests/runtime/test_identity.py` (signature); `tests/http/test_dev_conjunction_http.py` (payload shape); `tests/evidence/test_open_rails_abba_proof.py`, `tests/evidence/test_determinism_gate_proofs.py`, `tests/evidence/test_epic030_pr05_category_framework_evidence.py`, `tests/compat/test_hde_epic037_v2_adapter_to_compat.py` (in-process fixture-bundle paths, frozen-byte checks). Type-only and empty-Gate fixtures become negative cases or receive authentic complete fixture data. No test is skipped, disabled or quarantined; the five pre-existing failures in §3.2 item 8 remain outside CI lanes and are neither hidden nor claimed fixed.

### 8.6 Adverse matrix rows binding on PR04 (Plan §7.3)

Gates row (integer domain, boolean exclusion, cross-type duplicates, no leading zeroes/signs/whitespace/floats), Identity/application row (identity-slot conflicts, wrong-row provenance, alias bridge unreachable on the public Reader, no Gate-derived identity), Public/internal row (forbidden fields, no numeric leak, no new surface, single emitter) and Bytes-and-path row (canonical bytes, single LF, sha256 sidecars and path proofs for every regenerated companion) are each implemented as explicit test rows above. None is an observed PASS at planning time.

### 8.7 Non-admitted outcome tests (F01 overlay)

For each of the three generators: (a) with the injected synthetic complete release the existing positive matrix passes unchanged in meaning; (b) with the real admission owner (no injection) the gate returns/raises the typed non-admitted outcome, exits with the distinct code, prints its explicit line, writes no file and performs no live capture (spies on the Flask client, the CLI subprocess and the vendor client show zero calls); (c) any other exception is not classified as non-admitted. For the pipeline: a fake stage returning the distinct code renders `NOT_ADMITTED` and the summary `NOT_ADMITTED`; a mix with a `FAIL` renders `FAIL`; all-`OK` renders `PASS` byte-identically to the current model; the gate wrapper accepts exactly the two models. For the attestation builder: a `NOT_ADMITTED` sanity result yields the failure receipt `code == release_not_admitted`, no bundle and no success payload; `test_v1_schema_preserves_the_pf12_wire_contract` unchanged. For CI configuration: `tests/evidence/test_rails_ci_workflow_integration.py` pins the updated rails/release step text and the job definition's accepted-outcome declaration.

## 9. Ordered implementation procedure

One pull request. Four local checkpoints, each proven before the next begins. PR-30 forms one coherent initial commit from the completed checkpoints and publishes it; PR-35 pushes coherent corrective commits. No checkpoint is executed by PR-20.

**Preconditions:** Nathan / Product Owner's PR-30 Proceed against this exact plan version (truthfully `NOT PRODUCED`). Recommended prior: the RS-20 disposition of candidate finding `HDE-EPIC040-PR04-F02` (§14.3), without which §4.2 condition 4 cannot be met on a real candidate; if Proceed precedes it, PR-30 executes C1–C3 and holds publication of a green candidate until F02 is dispositioned (an approved F02 overlay during PR-30 prepublication resumes PR-30 directly).

### C1 — Seams, adapters, tokens, ownership (no consumer switch yet)

1. Register the §5.6 tokens in `engine/compat/error_tokens.py`; run `python tools/errors/generate_error_artifacts.py`; confirm `tests/cli/test_errors_parity.py`.
2. `engine/bodygraph/projection.py`: `_validate_raw_gates` and the identity-slot helper; new `tests/bodygraph/test_projection_gate_ingress.py`.
3. `engine/bodygraph/v2_adapter.py` (resolved + context retention), `engine/bodygraph/mapped_cache.py` (read-only accessor), `engine/bodygraph/ingest.py` (value-free logging posture, payload pass-through).
4. `engine/bodygraph/resolver.py`: `ResolvedCompatChart`, `resolve_compat_chart`, scoped dry-run acquisition with `finally` restore; new `tests/bodygraph/test_resolve_compat_chart.py` covering input classes 1–3 with fakes under closed rails.
5. `engine/compat/compute.py`: `EvaluationParty`, `validate_pair_eligibility`, `orient`, `evaluate_pair`, `_BUNDLE_PROVIDER`, cache seam; new `tests/compat/test_evaluate_pair_eligibility.py` (§8.2 matrix, G007/G008, structural validation, real-provider refusal).
6. `ci/checks/classify_ci_changes.py`: every §6.5 registration and the `fixtures/charts/` rule, in the same checkpoint as the new test modules; `tests/evidence/test_http_reader_ci_ownership.py` and `tests/evidence/test_evidence_tool_ownership.py` green.

Checkpoint proof: focused suites green; `git status --short --untracked-files=all` empty; classifier dry-run (§10.3) classifies every changed path with no `CI_*` error.

### C2 — Consumer switch and test conversion

7. `engine/runtime/public.py` (band from validated result; `ts_v0` removed), `presenter/reader_v1/emitter.py` only if required; `tests/runtime/test_identity.py` updated.
8. `engine/compat/compute.py`: rewrite `conjunction_public`, `conjunction_public_resolved`, `_resolve_party`; delete `compat_public`/`_score_for`; convert `tests/compat/test_conjunction_no_user_boundary.py` (classes 1–3), `tests/compat/test_compat_public_ab_ba_identity.py`, `tests/compat/test_compat_public_lf_bom.py`, `tests/epic003/test_meta_invocation_ok.py`.
9. `engine/cli/main.py`: all §6.1 changes; convert `tests/cli/test_showcompat_sources.py`, `tests/cli/test_cli_file_inputs.py`, `tests/cli/test_showcompat_parity_and_identity.py`, `tests/cli/test_cli_canonical_bytes.py`, `tests/cli/test_cli_usage_and_errors.py`, `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`, `tests/cli/test_aux_preview.py`. Success paths invoke `engine.cli.main.cli(argv)` in-process with the injected bundle (pattern: `tests/cli/test_aux_preview.py`); subprocess invocations remain only for usage-error and refusal paths, because a subprocess cannot receive the fixture bundle.
10. `engine/http/compat_handler.py`; convert `tests/http/test_compat_endpoint_contract.py`, `tests/adapter/test_compat_http_dev.py`, `tests/adapter/test_compat_http_parity.py`.
11. `adapter/http_reader.py`: POST success path, GET fixture route, dev conjunction routes; new `tests/http/test_reader_post_v1.py`; convert `tests/http/test_reader_a7_transport.py` (bundle injection; POST with no JSON body → 422 `no-store`, no ETag) and `tests/http/test_dev_conjunction_http.py`; upgrade `fixtures/charts/*.json` to complete charts with UUID identities.

Checkpoint proof: `python -m pytest -q -p no:cacheprovider --ignore=tests/em` shows only the five pre-existing failures of §3.2 item 8; clean tree; no `narratives/<pack_sha>/` residue.

### C3 — CI and evidence coupling

12. `tools/evidence/run_canonical_json_gate.py`: frozen-SHA validation for showcompat/conjunction captures; `--check-only` green.
13. Generators exercised through pytest — `tools/evidence/generate_hde_epic037_v2_to_compat.py`, `tools/evidence/generate_epic030_pr05_category_framework_evidence.py`, `tools/evidence/generate_determinism_gate_proofs.py` — migrated to the corrected helpers/seams; their tests inject the bundle; owners registered.
14. `tools/evidence/generate_bodygraph_policy_proofs.py` write mode from the candidate root; `--check` green.
15. **F01 overlay (§6.7, PF10 §2.15)** — implement the admission-state discriminator and the non-admitted outcome in rows 1–7, then the CI acceptance in rows 8–9, then the four test homes and §8.7; verify locally that (a) with the real admission owner the rails job and the release-lane builder end in the accepted `RELEASE_NOT_ADMITTED` outcome and (b) `tests/evidence/test_release_attestation.py` stays green; `tools/cli/generate_showcompat_artifacts.py` follows §6.2 (not an overlay file).
16. `python tools/evidence/update_evidence_index.py`, then the read-only checks of §6.4.

Checkpoint proof: evidence lane commands green; rails job and release-lane builder end in the accepted `RELEASE_NOT_ADMITTED` outcome with the independent probe observing `INCOMPLETE_RELEASE_ROSTER`; `git status --short --untracked-files=all` empty. Known open item: `tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` fails until F02 is dispositioned (§14.3) — recorded, not hidden.

### C4 — Candidate-wide validation and result record

17. Run §10 in full; record every command, exit status and outcome in `docs/ephemeral/HDE-EPIC040-PR04-pr-implementation-result-v1.0.md` (PR-30 output) with the exact commit SHA and tree, the five pre-existing failures, the F01 treatment applied and every limitation.
18. PR-30: one coherent commit; deliberate publication of the initial candidate; same-session handoff to PR-35. PR-35: review retrieval and correction, retests, corrective pushes, CI economy, current-head verification, `MERGE_PENDING — Ready to merge` without merging.

## 10. Local validation and evidence commands

### 10.1 Environment

```text
python -m pip install -r requirements.txt -r requirements-dev.txt -e .
python -m pytest --version
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
ci/checks/check_env_pins.sh
hdctl --help            # console script installed by `-e .`; CI installs it the same way
```

### 10.2 Focused behavioral and ownership suites

```text
python -m pytest -q -p no:cacheprovider \
  tests/bodygraph/test_projection_gate_ingress.py tests/bodygraph/test_resolve_compat_chart.py \
  tests/compat/test_evaluate_pair_eligibility.py tests/compat/test_conjunction_no_user_boundary.py \
  tests/compat/test_hde_epic037_v2_adapter_to_compat.py tests/compat/test_compat_public_ab_ba_identity.py \
  tests/compat/test_compat_public_lf_bom.py tests/epic003/test_meta_invocation_ok.py \
  tests/cli/test_showcompat_sources.py tests/cli/test_cli_file_inputs.py tests/cli/test_showcompat_parity_and_identity.py \
  tests/cli/test_cli_canonical_bytes.py tests/cli/test_cli_usage_and_errors.py tests/cli/test_errors_parity.py tests/cli/test_aux_preview.py \
  tests/qa/test_cli_admin_dumps.py tests/qa/test_cli_admin_parity.py \
  tests/http/test_reader_post_v1.py tests/http/test_reader_a7_transport.py tests/http/test_compat_endpoint_contract.py \
  tests/http/test_dev_conjunction_http.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_http_parity.py \
  tests/reader_v1/test_goldens.py tests/reader_v1/test_schema.py tests/runtime/test_identity.py \
  tests/db/test_ingest.py tests/db/test_bg_resolve_v2_mapped_cache.py tests/cli/test_bg_resolve.py \
  tests/unit/test_narratives_router.py tests/evidence/test_http_reader_ci_ownership.py tests/evidence/test_evidence_tool_ownership.py \
  tests/evidence/test_open_rails_abba_proof.py tests/evidence/test_determinism_gate_proofs.py \
  tests/evidence/test_epic030_pr05_category_framework_evidence.py tests/evidence/test_bodygraph_policy_proofs.py \
  tests/transport/test_a7_transport_proofs.py
git status --short --untracked-files=all    # must be empty
```

### 10.3 Classifier dry-run and changed-test isolation (as `.github/workflows/ci.yml` runs them)

```text
python ci/checks/classify_ci_changes.py --base "$(git merge-base origin/main HEAD)" --head HEAD \
  --event-name pull_request --github-output "$TMP/classify.out" --changed-tests-output "$TMP/changed_tests.txt"
cat "$TMP/classify.out"                      # expect all seven lanes true (classifier change ⇒ full validation)
git worktree add --detach "$TMP/changed" "$(git rev-parse HEAD)"
( cd "$TMP/changed" && export PYTHONPATH="$PWD" && python -m pytest -q -p no:cacheprovider -- $(cat "$TMP/changed_tests.txt") \
  && git diff --exit-code && test -z "$(git status --short --untracked-files=all)" )
```

### 10.4 Lane-equivalent validation

Run each lane exactly as `.github/workflows/ci.yml` at the candidate head defines it (the workflow file is the authority; the verified step contents at planning time are listed here): product lane — `python tools/order/generate_ordering_artifacts.py --check` plus its pytest list; compat lane — `ci/checks/check_cli_help.sh`, `python tools/cli/serializer_grep_guard.py --output <tmp>`, `python tools/cli/emitter_symbol_proof.py --output <tmp>`, plus its pytest list (includes `tests/cli/test_showcompat_parity_and_identity.py`, `tests/http/test_compat_endpoint_contract.py`); db lane — `python ci/checks/check_direct_db_contract.py` plus its pytest list; rails lane — `python ci/checks/run_rails_job_definitions.py ci/jobs/rails_closed_refusal.yml ci/jobs/rails_open_conformance.yml ci/jobs/logs_keys_only_redaction.yml` (the open-conformance job runs `tests/bodygraph/test_vendor_client.py`, `tests/evidence/test_open_rails_abba_proof.py` and `python tools/evidence/generate_open_rails_abba_proof.py --check-current`) and `python -m pytest -q tests/evidence/test_rails_ci_workflow_integration.py`; evidence lane — `python tools/evidence/update_evidence_index.py --check`, `python tools/evidence/orientation_demo.py --check`, `python tools/evidence/refresh_step_logs_manifest.py --check`, `ci/checks/check_evidence_index_hash.sh`, `python tools/evidence/validate_evidence_paths.py`, `ci/checks/check_mirror_schema.sh`, `ci/checks/check_final_lf.sh`; qa lane — its pytest list in isolation; release lane — `python scripts/release_id_recompute.py --check-manifest-only`, `python -m pytest -q tests/runtime/test_identity.py tests/evidence/test_release_attestation.py tests/evidence/test_release_manifest_content_binding.py tests/evidence/test_sanity_pipeline.py` in a detached worktree, then `python tools/evidence/build_release_attestation.py --output <external-empty-dir> --require-clean` and `--verify <same dir> --require-clean` (this build runs `tools/evidence/run_sanity_pipeline_gate.py`; under non-admission its accepted end state is the failure receipt `code == release_not_admitted` with the independent admission probe observing `INCOMPLETE_RELEASE_ROSTER`, and `--verify` is skipped because no bundle exists). After every lane: `git diff --exit-code` and an empty `git status --short --untracked-files=all`.

### 10.5 Candidate-wide roster

```text
python -m pytest -q -p no:cacheprovider --ignore=tests/em
```

Record the five pre-existing failures of §3.2 item 8 by node ID as pre-existing and outside CI lanes; do not repair, skip or hide them. Additionally run the `_FULL_VALIDATION_SUPPLEMENTAL_TESTS` roster as the classifier emits it in the changed-test manifest.

### 10.6 Result record

The PR-30 result records: candidate commit SHA and tree; base `origin/main` SHA; every command above with exit status; the classifier output; each lane outcome; the F01 treatment implemented and its RS-20 decision reference; evidence files regenerated with their owners; the updater run; limitations (no admitted release, frozen families, pre-existing failures); and the fact that local results are not QA, acceptance or release admission.

## 11. Code review and security review checklist

### 11.1 Code review

- No second calculator: `compat_public`, `_score_for`, `ts_v0` and hash scoring are absent from `engine/compat/compute.py`, `engine/runtime/public.py`, `engine/cli/main.py`, `engine/http/compat_handler.py` (grep-guard test); the only mechanics entry is `engine.core.core.compute_core`.
- `EvaluationParty.gates` is the exact `NormalizedGates` from `engine/bodygraph/gates.py::normalize_gates`; fingerprint from `engine.core.core._chart_fingerprint`; no metadata in mask/fingerprint.
- `release_id` and `config_id` come from the admitted bundle; no evidence path, `RELEASE_ID` environment value or identity file is read for evaluation.
- Eligibility runs after complete resolution and before bundle/cache/core/router; three UUID cases distinct; `(gate_mask, canonical_person_id)` orientation; router invoked in both normalized directions with `shared_key` agreement; ineligible self never touches core, cache, router or `pair_key`.
- Cache seam validates schema and embedded `pair_key`/`config_id`/`release_id`; stale → recompute only with two valid Gate sets else `ERR_M10_STALE_RESULT`; no identity-free caching of the augmented result; no new persistent cache.
- Error mapping matches §5.6 exactly; no invented token; tokens registered only through the owner generator; stderr-only error carriers; single trailing LF; canonical JSON bytes.
- Reader envelope six keys; band-only category row; single emitter; G007 preimage unchanged.
- CLI: `auto`/`db` DB-only; explicit `vendor` guarded; birth flags through `resolve_compat_chart` class 3; no `_derive_uid` `cli-` identity; no `_chart_for` synthesis; wrapper removed; admin dumps from validated result; exit codes preserved.
- Helper names `_normalize_party`, `_party_from_normalized`, `_person_and_chart_from_payload`, `_conjunction_party_from_payload` retained with corrected behavior (import safety for `tools/evidence/generate_determinism_gate_proofs.py`, `tools/presenter/generate_presenter_artifacts.py`, `scripts/cli/canonical_harness.py`).
- Classifier registrations complete for every touched product path, generator and new http_reader-importing test module; owner files exist; `tests/config/helpers.py` and the sha-pinned `tests/db/test_conn_env_only.py`, `tests/db/test_no_import_time_connect.py` untouched.
- No test skipped, disabled, quarantined or weakened; converted tests keep their decisive meaning; every router-reaching test presets the narrative pack from a temporary mount; success-path CLI tests run in-process.
- Governed artifacts produced only by owners; updater run last; check modes green; frozen families carry explicit nonclaims; nothing hand-edited.
- F01 overlay binding conditions: no surface renders `PASS`/`top_level_pass: true` under non-admission; CI acceptance keys on `release_not_admitted` plus the independent probe and nothing else; the acceptance has no time window or lane-name key; `hde.release_attestation.v1` and `PR06R_B_FINAL_PASS` untouched; `build_release_attestation.py` touched only on the failure-receipt path; no test skipped.

### 11.2 Security review

- `POST /reader`: strict lowercase canonical UUID grammar before any lookup; alias bridge unreachable; parameterized SQL through `engine.db.adapter.DBAccess`; read-only statements only; `vendor = 'hdapi'` fixed; least privilege; no writes, no vendor call, no fallback; errors `no-store` without ETag; success `private, max-age=0, must-revalidate`; POST non-conditional; no import-time DB connection in `adapter/http_reader.py`.
- Resolver never opens rails; scoped env restored in `finally`; no process-wide mutation; no second HTTP client; no route inference from base URL; no timezone default; no retry to another source.
- Dry-run/no-upsert acquisition; no user-row creation; no persisted alias map; no backfill; no DDL.
- Logs: value-free operational keys only; no birth tuple, chart, credential, `user_id`, person label or identity-bearing dump; keys-only redaction tests remain green.
- Fixtures synthetic; evidence contains no secrets, birth records or full Gate payloads beyond governed fixture files; GET fixture route confined to `fixtures/charts` (`ALLOWED_ROOT`), no traversal.
- Fakes and spies assert absence of forbidden effects (calls, writes, sockets), not only status flags.
- `APP_ENV` gates unchanged for dev routes; production restrictions of `engine/http/compat_handler.py` preserved.

## 12. Risk register and recovery

| ID | Risk | Treatment |
| --- | --- | --- |
| R-01 | **Dispositioned — F01 (§14.1).** Ordinary CI gates that execute live success paths cannot pass truthfully between PR04 and PR06 | Approved overlay PF10 §2.15 implemented per §6.7; binding conditions 1–4 are review items in §11 |
| R-19 | **Open — candidate F02 (§14.3).** `adapter/http_reader.py` is a committed manifest member; the release lane's manifest content binding test fails on any PR04 candidate; PR04 may not refresh the manifest | Raised separately through RS-10 (`docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md`); not folded in; PR-30 sequencing per §9 preconditions |
| R-20 | The exact exception attribute carrying `INCOMPLETE_RELEASE_ROSTER` differs from the plan's assumption, or another refusal is misclassified as non-admitted | C3 verifies the attribute against `engine/config/registry_loader.py` read-only; tests assert that any other exception is an ordinary failure |
| R-02 | Classifier fail-closed on unregistered paths, unclassified `fixtures/charts/`, unregistered generators | §6.5 registrations in the same checkpoint as new tests; dry-run in §10.3 before publication |
| R-03 | HTTP-reader ownership guard rejects a new test module importing `adapter.http_reader` | Register `tests/http/test_reader_post_v1.py`; keep `tests/evidence/test_http_reader_ci_ownership.py` green |
| R-04 | Hidden importers of removed/changed helpers break at import (15 importers verified in §6.2) | Names retained where dependents import them; every listed test converted; full roster run locally |
| R-05 | Governed evidence drift (token map, bodygraph policy snapshot, Index/Mirror, path proofs) | Owners only, primary bytes first, updater last, `--check` modes in the evidence lane |
| R-06 | Product Owner does not accept decision D-03 (valid self-pair exit-0 carrier) | A changed carrier contract is a bounded design question for RS-10; recorded in §14 as a potential second finding, not raised now |
| R-07 | Product Owner does not accept decision D-04 (registering PF05 §5.2.3 tokens) | In-scope collapse onto existing `ERR_READER_*` tokens with PF05 status codes; same owned files |
| R-08 | `DBAccess` API shape for the Reader SELECT differs from the plan's sketch; import-time connect regression | Verify the API at C1; fake at the abstraction boundary; `tests/db/test_no_import_time_connect.py` stays green and untouched |
| R-09 | Narrative pack mount residue (`narratives/<pack_sha>/`) fails CI's clean-tree checks | Autouse `_PACK` preset from a temporary mount in every router-reaching test; generators load into temp roots; tree check after every local run |
| R-10 | Five pre-existing failing tests outside CI lanes are mistaken for PR04 regressions or silently repaired | Recorded by node ID in the result; untouched |
| R-11 | PF01 §4.5 versus PF05 §5.2.3 token naming tension (observation O-01) | Application/transport split of §5.6; decided by no one here |
| R-12 | Sha-pinned dynamic http_reader owners (`_HTTP_READER_DYNAMIC_TEST_OWNER_SHA256`) | Do not touch `tests/db/test_conn_env_only.py`, `tests/db/test_no_import_time_connect.py` |
| R-13 | Full-validation CI cost per push | Batch coherent corrections under PR-35; local lane-equivalent runs before every push |
| R-14 | Subprocess-based success tests cannot receive the fixture bundle | In-process `cli(argv)` for success paths; subprocess only for usage/refusal |
| R-15 | `tests/http/test_reader_a7_transport.py` pair-file test uses a birth-only pair through the CLI subprocess | Convert to complete chart files in-process; assert refusal for birth-only under closed rails |
| R-16 | `tools/errors/generate_error_artifacts.py` also writes `errors/schema_check/*` and `parity/*` | Treat as governed outputs of the owner; run the updater; commit together |
| R-17 | `tests/qa/test_cli_admin_dumps.py`, `tests/qa/test_cli_admin_parity.py`, `tests/cli/test_cli_file_inputs.py` in the supplemental roster assert legacy dump/wrapper shapes | Converted in C2 |
| R-18 | The instruction's `POST /api/reader?v=1` spelling versus the blueprint's declared `POST /reader` | Same declared route in this application (blueprint prefix ""); recorded as observation O-11; no new route |

**Recovery.** Rollback restores application, kernel and configuration interfaces together as one PR04 slice; no successful UID, hash or `ts_v0` fallback is retained after rollback; the previously active complete release stays untouched. Mismatched cache or evidence inputs are quarantined as failures, never edited into equality. Complete temporary outputs are validated before any canonical primary is replaced; no partial publication on failure. If a valid admitted release is unavailable, canonical integrated success refuses (this is the designed interim state that F01 makes visible in CI).

## 13. Carried Canon-conflict register and observations

### 13.1 `CANON_CONFLICT_REGISTER` (carried, not decided)

| ID | Current decision | Effect carried into PR04 | Remaining owner / state |
| --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION / APPROVED` exactly as proposed, Thoth-17 at `2026-09-08T13:23:24Z` | Preserve explicit `Done` exclusions and the current PF09.3 agreement; no rows reopened | Source correction resolved; no new decision |
| `C040-02` | `CANON_RECONCILIATION / APPROVED`, same Thoth decision | Use the current controlled PF12 Markdown; the repository-resolved current PF12 is v2.9.5 (observation O-02); historical identity mismatch preserved as history only | PF12 version currency is ordinary maintenance with the governed PF12 maintainer |
| `C040-03` | `CANON_RECONCILIATION / APPROVED`, same Thoth decision | Use current PF14 v3.5.7; C040-05 separately controls contradictory core-test text | Historical version mismatch resolved |
| `C040-04` | `CANON_RECONCILIATION / APPROVED`, same Thoth decision | QA identity history preserved; PR04 performs engineering checks, not independent QA | Historical version mismatch resolved |
| `C040-05` | `CANON_RECONCILIATION / APPROVED`, alternative A, Isis-49 at `2026-09-09T03:57:16Z` | The four-argument Gate core supersedes the precomputed-score/`CoreConfig` passages; PR04 consumes that one core and reintroduces no second calculator or `ts_v0` scoring path (§5.3, §11.1) | Permanent PF14 §6.7 maintenance with its governed maintainer; pending, non-gating |
| `C040-06` | `NEW_CANON / APPROVED`, alternative A exactly, Isis-50 at `2026-09-09T11:48:08Z` | Complete 36-row taxonomy and 16-case conformance consumed through PR01–PR03; no changed weights | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage with governed maintainers; pending, non-gating |

F01/F02/F03 are approved, published PR02-only rescope overlays (PF10 §§2.7, 2.9, 2.10) and R02 is the approved PR03 admission overlay (PF10 §2.12); their engineering effects reach PR04 only as accepted predecessor behavior to preserve. No entry is reopened, relabeled, omitted or newly decided here. Finding `HDE-EPIC040-PR04-F01` (§14) is a work-unit boundary finding, not a Canon conflict, and is not added to this register. Plan v1.0 (PO-rejected) and Plan v2.0 (DENIED) remain historical.

### 13.2 Observations — non-gating, decided by no one here

| ID | Observation | Owner |
| --- | --- | --- |
| O-01 | PF01 §4.5 names Reader-boundary tokens differently from PF05 §5.2.3's Magic-10 failure tokens; PF01 §4.6 routes transport tokens to PF05. Plan decision D-04 follows the PF05 token set for `POST /reader` transport and the instruction's `ERR_READER_*` mapping at application boundaries | Governed PF01/PF05 maintainers |
| O-02 | The unique current controlled PF12 in `docs/pfcanon/` is v2.9.5; the approved Plan register and PR03 lineage recorded v2.9.6 from the prior Drive-based store | Governed PF12 maintainer |
| O-03 | `docs/ENDPOINTS_CATALOG.json` carries no `POST /reader` success row and `tools/evidence/generate_a7_transport_proofs.py` `PROOFS[4]` records `POST /reader status=405` as a capture-time fact that PR04 makes historical; the catalog is documentation-owned (PR07 / Product Owner direction), and the A7 family is part of finding F01 | Catalog owner; PR07; F01 route |
| O-04 | `schemas/reader.v1.schema.json` category-id enum (`*_leader`) diverges from the runtime `harmony` id, and its error branch is not token-enforced; pre-existing, unchanged by PR04 | Schema owner |
| O-05 | Five pre-existing failing tests outside CI lanes (§3.2 item 8) and one pre-existing collection error in `tests/em/` | Their native owners |
| O-06 | Resolved on `main` `3b8084d0…`: the PF10 Addendum Index now lists 2.14 and 2.15 | — |
| O-12 | PF10 content changed on `main` (`3b8084d0…`, §2.15 drained, index and formatting edits) while the file name and front-matter version label stay `v13.2.9`; recorded as provenance (v1.0 read `1421e4d6…`, v1.1 read `abcf86b8…`) | Governed PF10 maintainer |
| O-07 | `engine/narratives/state.py::get_pack()` mounts `narratives/<pack_sha>/` into the process working directory by default; an in-process probe during planning created untracked `narratives/4cc79e05…/`, removed before commit; the tracked `narratives/64e17c9c…/` mount is a stale pack sha | Narrative loader owner; risk R-09 for PR04 tests |
| O-08 | Byte-identical duplicate copies with a ` (1)` suffix exist in `docs/ephemeral/` for the Plan Review v2.1, Plan Review v2.0 and the PR01 PR-40 interruption record | Nathan (manual pruning of `docs/ephemeral/`) |
| O-09 | Notion Alpha Run Notes 20260914.1 still reads `ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR` (last edited 2026-09-14) while the Flow Index's sole operative Alpha state block is current (`ALPHA_RESUMED`, PR04 / PR-10 as of the handoff); drift to be reconciled by its owner | GCFPE management / Nathan |
| O-10 | PF14 v3.5.7 and PF05 v2.5.2 still describe Drive PFCanon as authoritative planning source; the selected `091426.1` contract and the Product Owner's 2026-09-21 direction resolve PF only from `docs/pfcanon/` | GCFPE management with governed PF14/PF05 maintainers |
| O-11 | The instruction spells the Reader route `POST /api/reader?v=1`; the repository declares `@bp.post("/reader")` on a blueprint registered with `url_prefix=""`. They name the same existing declared route in this application; PR04 adds no route | PR-10 author (transcription note only) |

## 14. Material boundaries: dispositioned, carried and raised

### 14.1 `HDE-EPIC040-PR04-F01` — dispositioned (APPROVE, bounded implementation rescope)

The v1.0 finding (verified cause: PR04 must remove every legacy success path and consume only the admitted bundle, which refuses with `INCOMPLETE_RELEASE_ROSTER` until PR06; three ordinary-CI gates execute live success paths — rails lane `--check-current`, release-lane attestation sanity stages 04/05, the A7 live build in the full-validation roster) was routed through RS-10 and decided by RS-20: `REVISION_REQUIRED` (Isis-50, `2026-09-22T06:48:06Z`, against proposal v1.0), then `APPROVE` (Isis-50, `2026-09-22T07:27:55Z`, against proposal v1.1) with exactly one PF10 addendum overlay, drained by Nathan as PF10 §2.15. Classification settled and not reopened here: bounded implementation rescope; not `IN_SCOPE_REPAIR`; not `SPECIFICATION_CHANGE_REQUIRED`; not a defect in PR01–PR03; candidate D (the interim posture executed inside PR04 under the overlay). PR05 is covered by the same overlay and receives no new loci. §6.7 carries the delta into this plan; nothing in the overlay is widened here. RS-20 also recorded that exclusion X-11's stated reason was false (`tests/runtime/test_identity.py` does fail under a PR04-shaped change) while its disposition stands on the correct ground that §6.2 already carries that test as a necessary dependent.

### 14.2 Decision D-03 — carried, not raised

Decision D-03 (§5.5: a valid complete self-pair on internal/admin matrix surfaces exits 0 / returns 200 with the canonical `{"categories": [], "eligible": false}` document inside the existing `canonical_json` carrier) is this plan's reading of PF01 §4.7 and PF05 §3.1.1. If the Product Owner rejects it, the alternative is a carrier-contract change and would be raised as a separate bounded finding through RS-10; it is not bundled into F01 or F02 (unresolved item U-02 of the RS-20 record).

### 14.3 `HDE-EPIC040-PR04-F02` — raised separately through RS-10; not approved; not folded in

**Statement.** `adapter/http_reader.py` is simultaneously an approved PR04 locus that instruction §6.5 requires PR04 to change and the first of the fifteen committed members of `catalog/manifest.json`. `tests/evidence/test_release_manifest_content_binding.py::test_committed_release_manifest_entries_match_repository_bytes` (release lane) asserts every committed entry's `sha256` and `size` equal the repository bytes and fails on any PR04 candidate — independent of admission state and with a fully admitted release too — while §4.3 excludes manifest expansion/activation and §6.6 lists `catalog/manifest.json` as unchanged. The PF10 §2.10 precedent (PR02-F03: one existing-row rebind through the canonical manifest writer, roster held at fifteen, release identity recomputed from actual bytes, canonical-JSON gate and updater convergence) is scoped "For HDE-EPIC040-PR02 only" and reserves complete member refresh to PR06, so it does not extend to PR04.

**Route.** RS-10 proposal authored by this session as the finding author: `docs/ephemeral/HDE-EPIC040-PR04-F02-rescope-proposal-v1.0.md`, `RESCOPE_PROPOSAL_PENDING_REVIEW`, ending `ASK OK?`, for RS-20 in the retained whole-change IA session. RS-20 decided nothing about F02, scoped no remedy and pre-approved nothing; this plan assumes no outcome. Effect on this plan: §4.2 condition 4 cannot be met on a real candidate until F02 is dispositioned; §6.6's `catalog/manifest.json` entry changes only if an RS-20 `APPROVE` overlay says so, in which case this session issues plan v1.2 carrying that overlay (or PR-30 resumes directly if the Proceed already exists and the PR is prepublication). No other PR04 locus is a committed manifest member.

### 14.4 Rescope discipline preserved

No route restarts IA-30/IA-40, rewrites the immutable Plan v2.1, mints a Proceed, reruns accepted PR01–PR03, merges or invokes PR-50. RS-20 `REJECT` on F02 would return here with the plan unable to reach a green release lane until a Product Owner decision; `REVISION_REQUIRED` goes to RS-30 with the same author; `SPECIFICATION_CHANGE_REQUIRED` returns to Nathan and the Specification owners.

## 15. Manual merge and post-implementation boundary

PR-30 and PR-35 ownership is preserved exactly and not reassigned: PR-30 recovers or establishes the one authorized work vehicle, implements only the authorized scope, tests locally, forms one coherent commit and deliberately publishes the initial candidate (`PR_CANDIDATE_PUBLISHED`), then hands the same dedicated PR04 session, workspace/worktree, branch, open PR, instruction, plan, original Proceed, completed work, tests and unresolved lineage to PR-35 without another Proceed. PR-35 owns review retrieval and correction, local retesting, coherent corrective pushes, CI economy, current-head verification, mergeability and genuine readiness, and returns `MERGE_PENDING — Ready to merge` without merging.

Nathan / Product Owner alone performs any manual merge unless a later direct, specific instruction expressly authorizes the identified action. No agent enables auto-merge, schedules a merge, asks for a merge as routine, or treats tests, review or CI as merge evidence. After actual manual merge evidence exists, Nathan may invoke the read-only PR-40 against the exact landed lineage; PR-40 independently decides work-unit acceptance. PR04 implementation, merge or acceptance performs no QA/Ops, promotes no release, edits no PF10 and closes no Epic. `PR-50 — Abort PR and Escalate` is invocable only by Nathan / Product Owner.

## 16. Prompt-use provenance

`GCFPE_PROMPT_USE` (this version):

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-02`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`; `work_unit_id`: `HDE-EPIC040-PR04`; `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1
- `prompt`: `PR-20 — Create Detailed PR Implementation Plan — 091426.1`, page `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, retrieved revision `2026-09-21T22:56:47.757Z`; ecosystem `GCFPE-20260914.1` / `091426.1` / 55
- `role_stage`: dedicated PR04 session `PR04-HDE-EPIC040-1` / PR-20 successor plan after the approved F01 rescope; `execution_posture`: `MANUAL_PROMPT_EXECUTION`; `session_disposition`: `RETAIN_EXISTING`
- `capture_time`: `2026-09-22T07:56:08Z` (re-verification start); storage commit time recorded by git
- `result`: `HDE-EPIC040-PR04-PR-IMPLEMENTATION-PLAN v1.1`, `AWAITING_PO_PROCEED`; companion `HDE-EPIC040-PR04-F02-RESCOPE-PROPOSAL v1.0`, `RESCOPE_PROPOSAL_PENDING_REVIEW` (its own RS-10 use entry is in that file)
- preserved earlier entries by exact reference: `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-02` (review v2.0 §11), `GCFPE-USE-HDE-EPIC040-RS-30-20260922-PR04-F01-01` (proposal v1.1 §13), `GCFPE-USE-HDE-EPIC040-RS-20-20260922-PR04-F01-01` (review v1.0 §13), `GCFPE-USE-HDE-EPIC040-RS-10-20260922-PR04-F01-01` (proposal v1.0 §13), `GCFPE-USE-HDE-EPIC040-PR-10-20260922-PR04-01` (instruction §15), and the v1.0 entry below
- `repository_provenance`: `PENDING / NON_GATING` (no installed `docs/changes/GCFPE_PROMPT_PROVENANCE.md` procedure)

`GCFPE_PROMPT_USE` (v1.0, preserved):

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-20-20260922-PR04-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `specification_ref`: `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`
- `work_unit_id`: `HDE-EPIC040-PR04`
- `requirements`: `K040-REQ-001`, `K040-REQ-004`, `K040-REQ-005`, `K040-REQ-007`, `K040-REQ-008`, `K040-REQ-010`–`K040-REQ-013`; `AC040-03`, `AC040-04`, `AC040-06`–`AC040-09`
- `ecosystem_release`: `GCFPE-20260914.1`, selected contract `091426.1`, 55 members
- `prompt`: `PR-20 — Create Detailed PR Implementation Plan — 091426.1`
- `prompt_page`: `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`
- `prompt_retrieved_revision`: `2026-09-21T22:56:47.757Z`
- `role_stage`: dedicated PR04 PR-development session `PR04-HDE-EPIC040-1` / PR-20 initial detailed planning
- `execution_posture`: `MANUAL_PROMPT_EXECUTION`
- `capture_time`: planning inspection `2026-09-22T01:33:19Z`; storage commit time recorded by git
- `runtime_identity`: not asserted beyond the operator-assigned session reference
- `result`: `HDE-EPIC040-PR04-PR-IMPLEMENTATION-PLAN v1.0`, state `DRAFT`, finding `HDE-EPIC040-PR04-F01`, route RS-10 → RS-20
- `result_refs`: repository path in §1; branch, commit and pull-request identities are populated in the handoff only after they exist
- `repository_provenance`: `docs/changes` contains only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`; no installed `GCFPE_PROMPT_PROVENANCE.md` procedure, schema, writer or destination exists; repository persistence of this use entry is `PENDING / NON_GATING` for a later authorized writer. Earlier uses in this change's lineage remain in their own artifacts under `docs/ephemeral/` and are not restated.

## 17. Continuation package

### 17.1 PR-30 package (this version's native next step)

The PR-20 user-facing return ends with one paste-ready `NEXT_PROMPT_HANDOFF` to `PR-30 — PR Implementation Proceed — 091426.1` (`https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`) for this same dedicated PR04 session `PR04-HDE-EPIC040-1` with `RETAIN_EXISTING`. The package: Product Owner invocation of PR-30 for the exact visible `HDE-EPIC040-PR04-PR-IMPLEMENTATION-PLAN` v1.1 and `HDE-EPIC040-PR04-PR-INSTRUCTION` v1.0 (no additional approval object); this plan and the instruction by repository path; `HDE-EPIC040-SPECIFICATION` v1.1, Implementation Audit v2.0, Implementation Plan v2.1, Plan Review v2.1 (original `PLAN_REVIEW_ID` preserved) and the accepted PR01–PR03 lineage; PF10 v13.2.9 (`abcf86b8…`) with the §2.3 overlays including §2.15; the exact `main` head/tree baseline re-verified at Proceed time; §§4–12 in full; the register of §13.1; the manual merge boundary of §15; and PR-30's result contract `PR_CANDIDATE_PUBLISHED` (or `RESCOPE_PENDING`, `RECOVERY_PENDING`, `PRODUCT_OWNER_DECISION_REQUIRED`). Explicit manual prerequisites: (1) Nathan's PR-30 Proceed for this exact version; (2) recommended before it, RS-20's disposition of `HDE-EPIC040-PR04-F02` (§14.3) — its RS-10 proposal carries its own complete RS-20 handoff. PR-30 then hands the same session to PR-35 without another Proceed.

### 17.2 If F02 is dispositioned first

An RS-20 `APPROVE` on F02 creates one PF10 addendum overlay; this session issues plan v1.2 as a complete successor carrying it, in state `AWAITING_PO_PROCEED`, and the PR-30 package above binds to v1.2. A `REJECT` or `SPECIFICATION_CHANGE_REQUIRED` returns to this session and Nathan respectively, and the plan cannot truthfully reach a green release lane until a Product Owner decision exists. No implementation begins until Nathan / Product Owner invokes PR-30 against the exact persisted plan version.
