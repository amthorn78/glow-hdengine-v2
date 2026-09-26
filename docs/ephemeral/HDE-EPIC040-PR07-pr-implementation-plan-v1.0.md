---
artifact_type: PR_IMPLEMENTATION_PLAN
artifact_id: HDE-EPIC040-PR07-PR-IMPLEMENTATION-PLAN
artifact_version: "1.0"
artifact_state: AWAITING_PO_PROCEED
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR07
pr_instruction_id: HDE-EPIC040-PR07-PR-INSTRUCTION v1.0
authoring_context: APPROVED_BASE_WITH_OVERLAYS
execution_posture: MANUAL_PROMPT_EXECUTION
baseline_main: 48b0559701ec584491fb75916d8a19ae06e72e3f
planning_inspection_capture_utc: 2026-09-26T18:34Z (first repository read, approximate) to 2026-09-26T19:35Z
next_stage: PR-30 (Product Owner Proceed required first)
---

# HDE-EPIC040-PR07 — PR Implementation Plan v1.0

## 1. Identity, state and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR07-PR-IMPLEMENTATION-PLAN` |
| version | `v1.0` — first issue; no predecessor plan exists for this unit |
| state | `AWAITING_PO_PROCEED` — complete and executable within the approved scope plus the applicable PF10 overlays (§2.3); no boundary finding raised (§14.1); pending Nathan / Product Owner's exact PR-30 invocation against this version |
| repository_path | `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md` |
| CHANGE_CLASS / CHANGE_ID | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| WORK_UNIT_ID | `HDE-EPIC040-PR07` — final repository documentation through DOC-10; documentation only |
| PR_INSTRUCTION_ID | `HDE-EPIC040-PR07-PR-INSTRUCTION` v1.0, `INSTRUCTION_READY`, `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md`, SHA-256 `3113b4e85ff50c10ab569e0f27eb882225abb333aaaa8db2bd8e712db0cd1c7b`, 9,404 bytes, blob `a6b3ff574f72aa3ebe480c03d811773130fe23c9`. On `main` since PR [#514](https://github.com/amthorn78/glow-hdengine-v2/pull/514) merged as `18c4bba` (2026-09-26T17:38:24Z); read completely from `main` |
| IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-IMPLEMENTATION-PLAN` v2.1, immutable approved base, `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`, 146,624 bytes; §6.7 is this unit |
| SPECIFICATION_ID | `HDE-EPIC040-SPECIFICATION` v1.1, `SPECIFICATION_APPROVED`, `docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md`, SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df` |
| IMPLEMENTATION_AUDIT_ID | `HDE-EPIC040-IMPLEMENTATION-AUDIT` v2.0, `AUDIT_COMPLETE`, `docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md`, SHA-256 `9b0d8edba2aefc26e582d8f51d5449ac86961d050ec3a5675f1db20b80e0379b` |
| PLAN_REVIEW_ID (original, preserved) | `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW` v2.1, Isis-50 `APPROVE` 2026-09-09T13:36:43Z, `docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md`, SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Applicable overlays | PF10 §2.23 (`HDE-EPIC040-PR07-F01` — adds PR06a; PR07 keeps its boundary and documents Reader v2, `/api/reader` and the conformed v1 schema as delivered) and PF10 §2.25 (`HDE-EPIC040-PR06b` — C040-08 decided A; PR07 documents the v1 schema as PR06b delivered it). Also effective within their scopes and carrying explicit PR07 documentation rows: §§2.7, 2.9, 2.10, 2.12 (admission contract and its reviewed limits). No `REMEDIATION_REVIEW` applies |
| Predecessor units | PR01–PR06, PR06a and PR06b are `ACCEPTED_FINAL`. PR06a: `docs/ephemeral/HDE-EPIC040-PR06a-pr-work-unit-lineage-review-v1.0.md`, SHA-256 `19ac13b7900cd94fc7d07ccf5991e6fb32e9f47c8cce2832e824f412a34fe12b`. PR06b: `docs/ephemeral/HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md`, SHA-256 `15fbf1431b8351bd725deeba29f0b87dae3e22c747b37a5b0bed5a5a8e053018` |
| producer_role | Dedicated PR-development session for exactly HDE-EPIC040-PR07 |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` (this PR-20 run); PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | `NOT_YET_ASSIGNED` — the handoff named no reference and the operator assigned none; no platform ID is invented. Known runtime identity from the harness: `https://claude.ai/code/session_01UrEaEb4uQkqq2zHD7VTYyc` |
| invocation_binding | `HDE-EPIC040` / `HDE-EPIC040-PR07` / `PR-20` |
| context_conflict | `NONE` established |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| Authority boundary | This plan authorizes nothing. Implementation waits for the Product Owner's PR-30 Proceed for this exact version; merge is Nathan's alone. QA, OPS01, acceptance, release activation, deployment, PF-Canon edits (including any C040-06/07/08 drainage), PF09 movement and Epic closure are outside it (instruction §§4, 8, 10; Plan §6.7 *Completion*) |

## 2. Exact controlling lineage and source record

### 2.1 Approved and accepted change lineage

| Role | Artifact | Identity used here |
| --- | --- | --- |
| Approved bases | Specification v1.1; Implementation Audit v2.0; immutable Plan v2.1; Plan Review v2.1 Isis-50 `APPROVE` | read; none is rewritten. Plan v2.1 §6.7 (PR07) supplies objective, owned scope, required content, proof, recovery/security and completion; §7.2 the canonical writers; §8 the requirement allocation (K040-REQ-001, K040-REQ-002 and K040-REQ-013 name PR07) |
| Accepted predecessors | PR01 v1.1, PR02–PR06 v1.0, PR06a v1.0 and PR06b v1.0 lineage reviews under `docs/ephemeral/` | all `ACCEPTED_FINAL`; they record what PR07 documents. The PR06b review records the 45-member `1.3.0` release (`release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`) and C040-08 closed in the repository |
| This unit's instruction | `HDE-EPIC040-PR07-pr-instruction-v1.0.md` (§1) | sole native input of this plan; its §§3–13 are mapped into §§3–17 below. Where it differs from Plan §6.7 as amended by §§2.23–2.25 the plan and addenda govern (instruction §2); no difference was found |
| Overlay decisions | `docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md` (SHA-256 `0c3d4ad718cbed410f1d248fcea5f1772b140bd06bc2866bc0ecc4257a7e8a55`) and `docs/ephemeral/HDE-EPIC040-PR06b-rescope-decision-v1.0.md` (SHA-256 `cebbe8ec34a91a39d9eec4692fcc8e1832b28d37cfada523638e25ee1a62140c`) | drained as PF10 §2.23 and §2.25; they add PR06a/PR06b and state PR07's content additions |
| C040-06 decided record | ADR `HDE-EPIC040-C040-06-HD-MECHANICS-ADR` v1.0, `docs/ephemeral/HDE-EPIC040-C040-06-HD-mechanics-ADR-v1.0.md`, SHA-256 `28a7f1b641e6fbbdcd3e7a1ada9bdc84b63f1b7d1a3762d6d4ee252ab4a6eaa2`, 94,945 bytes; addendum `docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md`, SHA-256 `60bbcb2b442fef0798acef35a81ec1947493ecd6d4893b21a0c3040f4cf3d368`, drained as PF10 §2.5 | the "authoritative 36-row evidence/decision" the documentation routes to (§5.3, D-05) |
| Format precedent | `docs/ephemeral/HDE-EPIC040-PR06b-pr-implementation-plan-v1.0.md`, SHA-256 `1672b1a86315063d04a3d649ed1b929ea85fdab9b51896af82ba7ed7bba13c8b` | structure only; no content inherited |

Accepted-final PR01–PR06b are not reopened, rerun, revised or reaccepted by this plan.

### 2.2 Controlled subject-matter sources used (all from `docs/pfcanon/`, read-only)

| Source | Sections used | Bearing |
| --- | --- | --- |
| `docs/pfcanon/PF01-Canon-HDE-Math-Spec-v1.3.7.md`, SHA-256 `101576d03ed5e11f3323e0e434466eeda3a9c93004299c6afe531c119e9a5e7a` | §2.2 (Reader v1 covenant; line 217 still reads "Exposure of the full Magic-10 set is a future, versioned change"), §2.3 (public error object; line 256 "no numerics beyond `retry_after_ms`", line 263 static posture: `schema` not permitted), §§6.1–6.2 (no C040-06 conformance text present) | C040-07 and C040-08 drainage state (pending); C040-06 drainage target |
| `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.5.md`, SHA-256 `d57fd3547573b8b8e3076b8f3fa4a34423a8b677c10bca93ff58eb6d4d867c6f` | line 1117 (the dev harness `dev/reader_harness/app.py` calls `app.getattr`, treats an absent `APP_ENV` as `dev`) | O-P07-03, O-P07-04 owner context |
| `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`, SHA-256 `cb123d2134b634c64589c1e193ef41a0bb5045f5d0b3fc85a8ff2cd3336399f3` | §3 (source fidelity, canonical ownership by exact in-document title without versions, claim-state separation, ellipsis prohibition), §5 (routing without convenience summaries), §12 *Runnable guides*, §13 (security and privacy in examples), §14 (final check) | the writing rules of §5.2 |
| `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.6.md`, SHA-256 `e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696` | §8.1.2 (typed errors without `schema`), §15.2 OI-001 (line 4236; *Status:* `OPEN`) | C040-07 and C040-08 drainage state (pending) |
| `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md`, SHA-256 `a12574965dc98c96c53822c4151db38bad48c91a00e3851e973e6a7ffa33d11e` | §5 Reader transport; line 2538 (the production Reader refuses `v=2`, "unsupported values such as `v=01`, `v=1%20`, or `v=2`") | C040-07 drainage state (pending); PF10 §2.23 supersedes line 2538 while active |
| `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.5.md`, SHA-256 `d7b2e0287da884fad6f4f79c69391099157c82e7ec0e78418581e1b873d21a1d` | §2.1 *Channels* (closed vocabulary, 36 rows, non-scoring metadata; no 36-row assignment table or broad-grouping rationale), §5.1 (line 1739: version `1.1.0` for the adopted cut; no `schemas/reader.v2.schema.json` row) | C040-06/07 drainage state (pending) |
| `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.7.md` (SHA-256 `a9c376f64e1cc3bb691d1661d131b3a42f6f96d318e82b981989b4a4836bd86c`) and `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.1.md` (SHA-256 `e03cb9ec8005d1a7f18acb03b96623c608e896da1baf7d5121e5e5a1a14a4aaf`) | searched for a Reader v2 statement: none present | consequential C040-07 drainage pending |

Exact in-document titles used for routing in the edited documentation (PF03 §3 *Canonical ownership*): `PF01-Canon-HDE-Math-Spec`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref`, `PF10-HDE-Build-Notes`, `PF12-Canon-HDE-Schemas-and-Artifacts`, `PF14-Canon-HDE-Mechanics-Guide`, `PF29-Canon-HDE-Users-Guide`. No PF source was resolved from anywhere but `docs/pfcanon/`. Nothing under `docs/pfcanon/` is changed by this plan or by the unit it plans.

### 2.3 Current controlled PF10 and every applicable active addendum

- Current controlled PF10 Markdown: `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md`, SHA-256 `af292883d5d4f27bd5cc510117e29b044ec2ac0b0f522df48fd0022010c6855c`, 286,355 bytes, 2,719 lines. It is the only PF10 file on `main`. The handoff and the instruction name `PF10-HDE-Build-Notes-v13.3.6.md` (SHA-256 `cc20d134c54bcf0be3b192b063354ddd12688e51d82092f21a06160180de12e6`); PR [#515](https://github.com/amthorn78/glow-hdengine-v2/pull/515) (`48b0559`) replaced it with v13.3.7 after the instruction was issued. The delta was measured against the v13.3.6 blob at `18c4bba`: the version line (line 4) and the appended §2.26 "HDE-EPIC040-PR06b — PR Work-Unit Lineage Review v1.0" (80 lines); nothing else changed. §§2.23 and 2.25 are byte-identical to the versions the instruction read. The PF10 version actually read is recorded here as provenance; it is not a gate.
- Read: the precedence front matter, the addendum index, and completely the addenda that bear on this unit: §§2.5, 2.7, 2.9, 2.10, 2.12, 2.23, 2.24, 2.25, 2.26; §2.6 lines 720–728 (the reviewed recovery limits).
- Applicable active addenda, by repository path, with the PR07 obligation each carries:

| PF10 § (v13.3.7) | Addendum repository path | SHA-256 | PR07 bearing |
| --- | --- | --- | --- |
| 2.23 | `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` | `a69e2205de410bf6332bb558f3ee0110e3524b7143a84591bbed18ff476528e9` | *Work-unit effects*: PR07 unchanged in boundary, inherits none of F03/F05/F07, adds the delivered Reader v2 contract, the `/api/reader` production route and the conformed v1 schema. C040-07 drainage table (PF01, PF04, PF05, PF12; consequential PF14, PF29) |
| 2.25 | `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` | `63d0bdcee8d4295738bb6a05a5a93c72951a871532e12d53b7e3a449fcca14a3` | "PR07 documents the v1 schema as PR06b delivers it"; C040-08 decided A; PF01 §2.3 and PF04 §8.1.2 drainage pending |
| 2.5 | `docs/ephemeral/HDE-EPIC040-C040-06-PF10-build-notes-addendum-v1.0.md` | `60bbcb2b442fef0798acef35a81ec1947493ecd6d4893b21a0c3040f4cf3d368` | the complete 36-row table, counts, broad-grouping rationale (items 2–4) and drainage targets PF12 §2.1 / PF01 §§6.1–6.2 (item 8) |
| 2.7 | `docs/ephemeral/HDE-EPIC040-PR02-PF10-build-notes-addendum-v2.0.md` | `5ecc9850dc9f4368868ad1e4de15e249193e2bb81421e41095e4aed686c2874d` | PR07 row: "Later documentation must describe the delivered 42-member admission contract and preserve the reviewed limits" (42 members then; the current release has 45) |
| 2.9 | `docs/ephemeral/HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md` | `1c952386cd84eaf8a8aefbb33054b6a902d49ea73aa6f68239f099ad700a25fd` | PR07 row: the executable-equivalence boundary and its explicit limits (item 8: not historical raw bytes, not arbitrary in-process tamper resistance; no process-death atomicity, multi-file atomic visibility or cross-process locking) |
| 2.10 | `docs/ephemeral/HDE-EPIC040-PR02-F03-PF10-build-notes-addendum-v1.0.md` | `896b3f3ab16f7d18ce2ab3de1bb1b6599afb85e349e963a9f52421f3189e46fb` | PR07 row: manifest-binding and executable-equivalence boundaries and limits |
| 2.12 | `docs/ephemeral/HDE-EPIC040-PR03-R02-pf10-build-notes-addendum-v1.0.md` | `a44659a7754c5f6e10f0bf4a1397d6815aae32ef75a2626a866055a801ba1998` | extends the executable-equivalence owner to the four active mechanics modules (eight modules in total) |
| 2.24 / 2.26 | `docs/ephemeral/HDE-EPIC040-PR06a-pr-work-unit-lineage-review-v1.0.md` / `docs/ephemeral/HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md` | as §1 | accepted deliveries and carried observations (O-P06a-22, O-12, O-P06a-03, O-P06a-23, O-P06b-17) |

- Effective baseline: **approved base + applicable PF10 overlays** (`AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS`).

### 2.4 GCFPE execution sources

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204`, read completely at invocation (page as of 2026-09-24T15:46:52.719Z). Notion was read only; this task directs no Notion write and none was made.
- Destination verified for §17: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204` (page title confirmed by fetch in this session; read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members, confirmed from the current-selection block of the `GCFPE Membership and Release Register`. Limitation: that page exceeds the fetch window, so only its current-selection block was extracted and read, not the whole body.
- Repository instructions applied: `AGENTS.md` (closed rails, pytest readiness, redaction, QA-output placement, no hand-editing of governed evidence, "cite PF canon by title/§ only", docs-only PR posture, PR-description contract, code-review scope) and the workspace skills governing write boundaries, artifact storage and currency. This session wrote only this document, under `docs/ephemeral/`.

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline verified at planning time

| Fact | Value |
| --- | --- |
| `main` | `48b0559701ec584491fb75916d8a19ae06e72e3f` (`docs(pfcanon): replace PF10 HDE Build Notes v13.3.6 with v13.3.7 (#515)`, 2026-09-26T18:30:06Z); `origin/main` identical |
| Delta from the instruction's `baseline_main` `8999bd0` | `git diff --name-only 8999bd0 48b0559` lists exactly three paths, all documentation: `docs/ephemeral/HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md`, `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md` (#514) and `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md` (#515, reported as a rename of v13.3.6). The runtime tree equals the PR06b landed tree the PR06b review executed |
| Instruction readiness predicate | "PR-20 may begin once #514 has merged" (instruction §13): #514 merged as `18c4bba` |
| Remote branches and PRs | No PR07 implementation branch, worktree, result record or pull request exists. The PR-20 planning branch carries only this document and is not an implementation vehicle |
| Admitted release | `catalog/manifest.json`: 45 members, version `1.3.0`, `built_at_utc 2026-08-24T18:04:49Z`; SHA-256 of its bytes `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`; `load_active_mechanics_bundle()` returns `AdmittedMechanicsBundle` with version `1.3.0`, 45 source identities, `release_id` equal to the manifest digest and to `identity_meta()["release_id"]` (executed, §3.3) |
| Working tree | clean at inspection start and end; this plan is the only write of this session (`docs/ephemeral/` only) |

### 3.2 Verified delivered-state facts that shape the documentation

Each fact was established at the baseline by reading the named file or by executing the named command in the scratch worktree of §3.3, never in the checkout. PR-30 re-verifies every fact it documents (§8).

| # | Fact | Consequence for the docs |
| --- | --- | --- |
| F-01 | Four-argument core: `engine/core/core.py:209` `def compute_core(member_a, member_b, mechanics_bundle, release_id) -> CoreResult:`, docstring "Compute one complete intrinsic result; eligibility belongs to the caller." It is reached through `engine/compat/compute.py:307` `evaluate_pair` (line 346 calls `compute_core(lo.gates, hi.gates, bundle, release_id)`), whose default bundle provider is `load_active_mechanics_bundle` (line 50). Both public consumers call `evaluate_pair`: `engine/cli/main.py:745` (`showcompat`) and `adapter/http_reader.py:454` (Reader) | the supported core statement (README, INDEX, AGENTS) |
| F-02 | Strict schemas and configuration: `catalog/magic10_mechanics_v1.json` has `schema` `magic10_mechanics_config.v1`, `config_id` `m10-channel-state-v1.0.0`, `result_schema` `magic10_result.v1`, 20 signals, and a `sources` object with exactly four `{path, sha256}` rows: `caps` → `catalog/magic10_caps.json`, `categories` → `catalog/magic10.json`, `channels` → `catalog/channels_v1.json`, `thresholds` → `math/thresholds.json`. Schema homes: `schemas/magic10_mechanics_v1.schema.json`, `schemas/magic10_result_v1.schema.json`, `schemas/magic10_compat_result_v1.schema.json`, `schemas/channels_v1.schema.json`, `schemas/gates_v1.schema.json`, all release members. `engine/compat/compute.py:42–43`: `COMPAT_RESULT_SCHEMA = "magic10_compat_result.v1"`, `PURE_RESULT_SCHEMA = "magic10_result.v1"` | `docs/config_and_bundles.md` current section |
| F-03 | Admission (complete release): `engine/config/registry_loader.py:398–399` `ADMITTED_RELEASE_VERSION = "1.3.0"`, `ADMITTED_RELEASE_BUILT_AT_UTC = "2026-08-24T18:04:49Z"`, then the 45-path `ADMITTED_RELEASE_ROSTER`; admission refuses `INCOMPLETE_RELEASE_ROSTER` (line 1226) and `RELEASE_ROSTER_MISMATCH` (line 1230), compares the manifest version (line 1233, `RELEASE_VERSION_MISMATCH`) and timestamp (line 1237, `RELEASE_TIMESTAMP_MISMATCH`) with those constants, and checks member sizes (`MANIFEST_MEMBER_SIZE_MISMATCH`, line 1258) and executing sources (`EXECUTING_SOURCE_MISMATCH`, line 1367). `_admission_execution_provenance` covers exactly eight modules (lines 1284–1291): `engine/config/registry_loader.py`, `engine/serializer/canon.py`, `engine/stable/sercanon.py`, `engine/categories/registry.py`, `engine/core/core.py`, `engine/magic10/composite.py`, `engine/magic10/signals.py`, `engine/magic10/calculators.py`. `load_active_mechanics_bundle()` (line 1506) takes no argument: "Admit the exact installed complete mechanics release, or fail closed", deriving its root from execution provenance. The file is itself a release member | complete-versus-candidate release text (README, RUN, AGENTS) |
| F-04 | Cutter: `scripts/cut_release_manifest.py` options `--manifest`, `--version` (required), `--built-at-utc` (required), `--check`, `--roster-from-admission` ("construct the membership as exactly the admission owner's ADMITTED_RELEASE_ROSTER"). `--version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --check` exits 0, with and without `--roster-from-admission`; `python scripts/release_id_recompute.py --check-manifest-only` exits 0; tree clean afterwards | the cutter writes only the manifest; a version change also needs the admission constants |
| F-05 | Admission limits (PF10 §§2.9, 2.10, 2.12): executable-code equivalence for eight first-party modules; it does not prove the exact historical raw bytes the interpreter read or arbitrary in-process tamper resistance; no process-death atomicity, multi-file atomic visibility or cross-process locking. Writer recovery limits (PF10 §2.6 lines 725–726): caught-failure restoration, source/destination race refusal, no-write check paths and preservation of conflicting external changes, without crash atomicity, multi-file atomic visibility or cross-process locking | the "reviewed limits" PF10 §§2.7/2.9/2.10 require PR07 to preserve |
| F-06 | Config writers: `python tools/config/generate_config_artifacts.py --help` → `[--allow-aliases] [--check \| --publish-family \| --compare-goldens CANDIDATE_ROOT] [--goldens PATH] [--report PATH]`; `--check` "Validate committed three-primary bytes without writing" exits 0 at the baseline. The three primaries: `artifacts/registry/registry_report.json`, `artifacts/thresholds/magic10_config.json`, `artifacts/thresholds/band_edges.json` (`engine/config/bundles.py:54–56`). `tools/config/generate_bundles.py` writes `artifacts/config_bundles/fe_bundle.json` (`schema` `config_bundle.fe.v1`) and `artifacts/config_bundles/be_bundle.json` (`config_bundle.be.v1`). `python tools/generate_registry_report.py --help` offers only `[-h] [--allow-aliases]`: it has no `--check` | writer ownership; the `docs/RUN.md` line 10 correction |
| F-07 | `config/bands_4B60_v1.json` and `config/toggles_v1.json` exist, are not release members, and have no reader in `engine/`, `adapter/`, `presenter/`, `scripts/` or `tools/` (bounded search; the only `config/` reader is the presets loader's `config/presets`). Band edges are built from `math/thresholds.json` (`tools/config/artifacts.py:18`, `BAND_SOURCE`) | corrections in `docs/config_and_bundles.md` line 6 and `docs/INDEX.md` line 89 |
| F-08 | Comparator: `--compare-goldens CANDIDATE_ROOT` is read-only; exit 0 on match, 1 on mismatch, 5 on refusal; default goldens `tests/fixtures/magic10/v1/goldens.json`; `--report` writes outside the candidate root and the repository. Executed at the baseline: `ok: true`, schema `magic10_golden_comparison.v1`, eight cases `M10-G001`–`M10-G008` all `match`, `candidate_release_id` = the current `release_id`, report SHA-256 `bea29970107fe750394e0f78c1047de93ebd9193565cd82a8e6e92e7b515dca8` | comparator documentation |
| F-09 | Readiness: `tools/bodygraph/check_magic10_gate_readiness.py [--user-id UUID] [--selection-file PATH]`; report schema `magic10_gate_readiness.v1` (`readiness` `READY`/`NOT_READY`, `provider`, `read_only: true`, `selection {requested, sha256}`, `counts`, `diagnostics`); exit 0 when a report is emitted; exit 5 on refusal with one stderr token `RAILS_CLOSED_REQUIRED:<pins>`, `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID` or `READINESS_UNAVAILABLE`; selection file regular, non-symlinked, at most `SELECTION_FILE_MAX_BYTES = 1_048_576`; no `UPDATE`, `INSERT` or `DELETE`, no acquisition, repair, backfill or vendor call. Executed without a database: no selection → exit 5 `READINESS_EMPTY_SELECTION`; `SAFE_MODE=0` → exit 5 `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]` | readiness documentation; never run against a real database during PR07 |
| F-10 | Routes, all three app factories (`adapter/factory.py`, `adapter/wsgi.py`, `adapter/http_reader.py::create_app`) mount the dev/internal blueprint at the root and the production blueprint (`get_reader_api_bp`) under `/api` (executed with the Flask test client): `POST /api/reader?v=1` and `?v=2` without a database → 503 `ERR_M10_RESOLVER_UNAVAILABLE`, `no-store`, no ETag; `?v=3` → 400 `ERR_READER_INVALID_VERSION`; `GET /api/reader` → 405 `Allow: POST`; unprefixed `POST /reader` → 405 `ERR_NOT_FOUND` with `Allow: GET, HEAD`; dev `GET /reader?v=2` → 400 `ERR_READER_INVALID_VERSION`; dev `GET /reader` with bare names `a=alice.json` → 400 `ERR_READER_INVALID_PATH`. Code: body at most `_READER_MAX_BODY_BYTES = 32_768`, UTF-8 without BOM, keys exactly `a_id`/`b_id` as canonical lowercase UUIDs, else 422 `ERR_READER_INVALID_INPUT`; one read-only current-row lookup per identity (`DBAccess.for_current_env()`; unavailable → 503, missing → 404 `ERR_M10_PERSON_UNRESOLVED`); success headers `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate`, `Vary: Authorization, Accept-Encoding`, ETag removed | route documentation |
| F-11 | Dev `GET /reader` (`adapter/http_reader.py:597`): version first (`v=1` only), then `os.environ.get("APP_ENV", "dev") != "dev"` → 403 `ERR_READER_FORBIDDEN`, so an unset `APP_ENV` is treated as `dev`; `a`/`b` are paths resolved against the process working directory that must resolve inside `fixtures/charts/` (`ALLOWED_ROOT = Path("fixtures/charts").resolve()`, `_safe_load_chart`); `a_tz`/`b_tz` fill a missing chart `tz` | the `docs/server/reader_v1.md` current-state block and line 49 correction; O-P07-04 |
| F-12 | Unknown paths (O-P06a-22 reproduced): `GET /api/reader/missing` → 404 `text/html` without `Cache-Control` from `adapter.factory` and `adapter.http_reader`; 404 `application/json` `no-store` from `adapter.wsgi` | known-limitation line (carried observation, described only) |
| F-13 | Schemas and goldens: `schemas/reader.v1.schema.json` `$defs` = `band`, `category`, `category_id`, `error`, `hex64`, `meta`, `success`; success required keys `reader_version`, `eligible`, `categories`, `meta`, `release_id`, `idempotence_hash`; `meta` exactly `engine_tag`, `invocation_tag`; `$defs.error` has 17 `oneOf` pairs and `required ["schema","ok","code","error"]`. `schemas/reader.v2.schema.json` `$defs.error` has 12 pairs. Both draft 2020-12, `$id` `https://example.org/schemas/reader.v{1,2}.schema.json`. `goldens/reader/v2/` is written by `scripts/make_reader_v1_goldens.py` (`OUT_V2`). Golden bytes (with trailing LF): v1 `g01_minimal_ineligible.json` 283 B `93ab201691f61ea5ce9d657bf932b413e5f38f7155593899f1d9074e0262141b`; v1 `g03_harmony_open.json` 312 B `976c46365936b189341fb12bb380c60ef9960210a2259ae1d1726f0642df470c`; v1 `g06_error_invalid_input.json` 94 B `c5eb83aec246444fe5d207f14e089b28d2cafc35c5d84ff49bc719b01c37b27a`; v2 `g01_ineligible.json` 283 B `fcf2d41793ab62f2eee7fddb26f4ca638a37027189d25719e5de80d39d0f0803`; v2 `g03_eligible_ten_in_order.json` 603 B `695911b4297e2cbe65e86f8677979bbba4cc2099d759fab5391ef9097db88f92`; v2 `g04_error_invalid_version.json` 100 B `0e6e1929248ac37bdb5b0bbc1ad1fb655b5737030d24d886b9b643036da41fd5`. Every golden carries the synthetic `release_id` of 64 `a` characters and fixture `meta` (`Isis5`, `INV-000000`) | examples are copied from these bytes (D-02) |
| F-14 | Current Reader v1 contract page example is invalid: `docs/contracts/reader_v1_public_bytes.md:6` omits `reader_version`, uses `"meta":{}` and `<64hex>` placeholders, so it fails `schemas/reader.v1.schema.json`; lines 13–19 show the historical `{"compat":[{"id":"harmony","band":"warm"}]}` wrapper unlabelled; lines 21–25 state ETag/304/HEAD rules that hold only for dev `GET /reader` | the v1 page rewrite (§6.2) |
| F-15 | Reader↔CLI parity: `hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json --dump-reader <file>` exits 0 and its 330-byte sidecar equals dev `GET /reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=UTC&b_tz=UTC` bytes | the parity statements |
| F-16 | `showcompat` stdout (non-conjunction) is the canonical `magic10_compat_result.v1` document with keys `categories`, `config_id`, `pair_key`, `release_id`, `schema`, `signals` (executed; 3,298 bytes for alice/bob). The `hdctl --help` summary still reads "Emit canonical Reader v1 bytes from vendor JSON" (`engine/cli/main.py:79`; governed capture `artifacts/cli/help/hdctl_help.txt:8`) | O-P07-01; gap labelled in `docs/CLI_commands.md` |
| F-17 | `aux-preview`: the README Quickstart example (`--pair-file artifacts/presenter/showcompat_identity_summary.json`) exits 64 `MISSING_COMPAT_CATEGORY`; with `showcompat` stdout as the pair file, `--category harmony --band Cool --perspective shared --show-narrative` exits 0. With `--band Glow` against a `Cool` harmony pair it still exits 0 and prints the `Cool` narrative | README Quickstart correction; O-P07-02 |
| F-18 | Dev start: `scripts/dev_start_reader.sh` runs `python -m adapter.http_reader` (`create_app().run(host="0.0.0.0", port=int(os.environ.get("PORT","8000")))`). `dev/reader_harness/app.py` raises `AttributeError: 'Flask' object has no attribute 'getattr'` at import | `docs/RUN.md` line 5 correction; O-P07-03 |
| F-19 | C040-06 in the catalog (executed): `catalog/channels_v1.json` has 36 rows; `circuit_primary` counts individual 15, collective 14, tribal 7; the rows with substream `integration` are exactly `10-20`, `10-57`, `20-34` and `34-57`; `10-34` is `individual`/`centering`; `20-57` is `individual`/`knowing` — matching PF10 §2.5 items 2–4 | the Integration explanation |
| F-20 | Drainage state (PF sources of §2.2): C040-06 not drained (PF12 §2.1 has no assignment table or rationale; PF01 has no C040-06 text); C040-07 not drained (PF01 line 217; PF04 OI-001 `OPEN`; PF05 line 2538 refuses `v=2`; PF12 has no Reader v2 row and records `1.1.0`; PF14 and PF29 have no Reader v2 statement); C040-08 not drained (PF01 §2.3 lines 256/263; PF04 §8.1.2) | truthful "pending as of HDE-EPIC040-PR07" statements |
| F-21 | Packaging (O-12): a wheel built from the baseline source (scratch build, `glow_hdengine-0.0.0-py3-none-any.whl`) omits 16 of the 45 members: `adapter/schemas/error_v1.schema.json`, the five `catalog/narratives/*.json` members, `errors/token_map/token_map.json`, `migrations/005_identity.sql`, the seven `schemas/*.json` members, `tools/bodygraph/check_magic10_gate_readiness.py` | README release-identity limitation line |
| F-22 | Documentation coupling: none of the fifteen planned paths is a Human Index or Machine Mirror row (`docs/evidence/INDEX.json` and `artifacts/evidence_index.jsonl` name none) or a release member (no `.md` among the 45). Code that reads them: `tests/arch/test_arch_capture_exists.py` (existence of `ARCHITECTURE.md` only); `ci/checks/check_direct_db_contract.py` scans tracked `.md` files except `CHANGELOG.md` for retired DB keys and scans `AGENTS.md` for "bridge" lines containing active-guidance words outside refusal context (db lane) | no generated companion (D-09); P-08 |
| F-23 | EPIC039 facts still hold: `tools/evidence/run_canonical_json_gate.py` `EXPECTED_TARGET_PATHS` 26 entries and `EXPECTED_SET_RULES` 6; `catalog/narratives/keys.json` 360 rows, `templates.json` 360 entries | the EPIC039 sections stay as written; only titles move to EPIC040 (D-06) |
| F-24 | `engine/errors/envelope.py` (named by `ARCHITECTURE.md:11`) does not exist at the EPIC040 base `9065e6f` or at `main`; the envelope builder is `engine/compat/errors.py:13` `error_envelope(code, *, details=None)`. `engine/serializer/canon.py:31` defines `dumps = sercanon`, so `canon.py::dumps` references elsewhere are valid | `ARCHITECTURE.md` line 11 correction only |
| F-25 | CI: `.github/workflows/ci.yml` has one `test` job. Every planned path is `.md` outside `_DOCUMENTATION_PREFIXES` and outside every lane prefix; `_lanes_for_path` returns no lanes (`_DOCUMENT_PATHS` / `_DOCUMENT_SUFFIXES`), none is a governed Index path, so `classify_paths` returns `reason=documentation_only`, `needs_python=false`. Python setup, installs and every lane are skipped; the job checks out the exact head, classifies and ends with `CI_APPLICABILITY_AND_EXACT_HEAD_OK` | CI proves applicability and exact head only; the documentation proofs are local (§8) |
| F-26 | PF10 v13.3.7 content: the addendum index (front matter) ends at 2.25 and omits §2.26; line 1373 (in §2.11 §8) is stored as 314 bytes ending "persistence remains p" — established by a complete read of the stored 286,355 bytes | O-P07-08 (Nathan), non-gating |
| F-27 | `AGENTS.md` cites PF10 by section number ("PF10 — HDE Build Notes §2.8", "§2.3", "§2.9", "§2.11"); in v13.3.7 those numbers hold other addenda, and the cited execution-source rule ("available PF copies") is not found in v13.3.7 | O-P07-09 (Nathan); evidence that PF10 numbers are unstable (D-03) |

### 3.3 Planning verification in a scratch worktree (inference support, not PR evidence)

This session verified the facts above in a detached worktree of `48b0559` under the session scratchpad (`pr07-main`), with a virtualenv holding the repository and dev requirements and an editable install of that worktree (Python 3.11.15, pytest 8.4.2), and a separate source copy (`pr07-wheelsrc`) used only to build the wheel of F-21. Rails for every execution: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1`, with `HD_API_BASE_URL`, `HDAPI_BASE_URL`, `HD_API_KEY`, `GEO_API_KEY`, `DATABASE_URL`, `DEV_SAMPLER_URL` and `GH_TOKEN` removed from the process environment; `APP_ENV=dev` where a route needed it. The only deviation was one deliberate refusal probe (`SAFE_MODE=0` for F-09), which refused before any I/O. No vendor call or database connection occurred, and no server was started (route facts came from the Flask test client). The worktree stayed clean after every command. The five golden-named examples embedded in §§6.1–6.2 were checked as P-04 prescribes: each is byte-equal to its golden without the trailing LF, valid against its schema (Draft 2020-12), and each success example's `idempotence_hash` recomputes. None of these bytes enter the PR; PR-30 re-executes every proof on its own branch (§§8–10).

### 3.4 Documentation sweep and classification

The instruction's §6 loci were each read completely. Every tracked Markdown file outside `docs/ephemeral/`, `docs/pfcanon/` and the archive trees (`_arch*`, `.audit_src/`, `_archive/`, `.backup*`, `audit/`, `artifacts/`, `handoff/`) — 119 files — was searched for Reader routes, `/api/reader`, Reader v2, `_leader`, `compute_core`, `release_id`, manifest and core-alternative statements (`compute_pair`, precomputed scores); hits under the other CI-exempt prefixes were classified out of scope.

| Class | Paths |
| --- | --- |
| Edited, instruction §6 loci (12) | `docs/server/reader_v1.md`, `docs/contracts/reader_v1_public_bytes.md`, `README.md`, `CHANGELOG.md`, `docs/CLI_commands.md`, `docs/RUN.md`, `docs/config_and_bundles.md`, `docs/INDEX.md`, `docs/acceptance/http_transport_evidence.md`, `docs/ADAPTER_009.md`, `ARCHITECTURE.md` (line 11 only), `AGENTS.md` (additive only) |
| New (the one permitted) | `docs/contracts/reader_v2_public_bytes.md` (D-01) |
| Edited, additional affected homes (2) | `docs/architecture/emitters.md` (line 16 states Reader v1 endpoints are the only public APIs, false after C040-07); `FLASK_AUTO_RUN_GUIDE.md` (lines 131–135 and 191 describe `adapter/factory.py` as mounting one blueprint at the root; PR06a added the `/api` production mount). Classified in §14.3 |
| Unchanged, still true | `docs/EVIDENCE_INDEX.md` (EPIC039 canonical-JSON inventory, F-23), `docs/qa_harness_pattern.md`, `AcceptanceMap.md`, `docs/adr/hde/release_attestation_scaling_adr.md` (its line 15 describes the cutter tool, which still writes only the manifest) |
| Unchanged, retained history | `docs/acceptance/reader_a7_crib.md`, `docs/SYNC_LOG.md`, `docs/changes/*`, `docs/evidence/EPIC018_evidence.md`, root `hde-epic023__*.md` and `EPIC023_*.md` step reports, `notes/**`, `codex/AGENTS_RFI.md`, `_arch/**`, `.audit_src/**`, `audit/**`, `artifacts/**` |
| Out of review scope (CI-exempt storage, AGENTS.md) | `docs/crd/`, `docs/ephemeral/`, `docs/graph/`, `docs/pfcanon/`, `docs/plans/`, `docs/prompt_ecosystem_management/`, `docs/qa/`, `docs/run/` — not edited |
| Not documentation (observation only) | `VERIFY.sh` (O-P07-07), `scripts/hd_cli.py` (O-P06a-03), `engine/cli/main.py:79` help text (O-P07-01), `dev/reader_harness/app.py` (O-P07-03) |

### 3.5 CI surface for this unit

Per F-25 the implementation PR classifies as `documentation_only`: CI runs the exact-head checkout, the classifier and the final applicability audit. A green `test` job therefore establishes exact-head applicability and a clean candidate tree, not the accuracy of the documentation. The accuracy evidence is the local proof set of §8, recorded in the result artifact. The PR-35 session must not present green CI as proof of documentation accuracy.

## 4. Exact objective, completion conditions and exclusions

### 4.1 Objective (Plan §6.7; instruction §4)

Make the implemented contract, the source-backed taxonomy, ownership, comparison/readiness usage and release boundaries legible in existing repository documentation after all implementation, adding the delivered Reader v2 contract, the `/api/reader` production route and the conformed Reader v1 schema (PF10 §§2.23, 2.25).

### 4.2 Completion conditions

1. Every item of instruction §5 is present in the home §5.1 assigns, with the wording of §6 or an editorially equivalent wording that keeps every stated fact, qualifier and nonclaim.
2. The confirmed correction (`docs/server/reader_v1.md:42`) and every other correction of §6 are applied; history is preserved and labelled.
3. Proofs P-01 to P-15 (§8) pass on the committed candidate head and are recorded in the result artifact.
4. Code review and security review on the exact head, and ordinary CI (`documentation_only`, `CI_APPLICABILITY_AND_EXACT_HEAD_OK`) on the exact head, through the PR-30/PR-35 lifecycle.
5. No generated companion changes (F-22); `git status` clean after every read-only check.

Completion produces the clean final candidate for OPS01. It is not a QA verdict, acceptance, PF09 movement or closure (instruction §4).

### 4.3 Hard exclusions (instruction §8; Plan §6.7 *Recovery/security*)

No source, schema, golden, catalog, manifest or evidence byte change; no re-cut; no PF-Canon edit and no Canon drainage; no edit to historical records under `docs/ephemeral/` (the new result record is added, nothing existing is edited); no QA, OPS or deployment; no execution of write-producing evidence generators; no live vendor or database action. Carried observations O-P06a-22, O-12, O-P06a-03, O-P06a-23 and O-P06b-17 are described, never fixed (§13.3). A required change outside documentation is a finding for the whole-change IA (§14), never a documentation edit.

## 5. Documentation design

### 5.1 Content map — every required item to its home

| Required content (source) | Home(s) and section |
| --- | --- |
| Supported four-argument core (Plan §6.7) | `README.md` EPIC040 block; `docs/INDEX.md` EPIC040 orientation and developer quick-link; `AGENTS.md` EPIC040 section |
| Strict config/result schemas (Plan §6.7) | `docs/config_and_bundles.md` "Current Magic-10 configuration"; `README.md` EPIC040 block |
| Canonical writer and source ownership (Plan §6.7, §7.2) | `docs/config_and_bundles.md` writers bullet; `docs/RUN.md` line 10 correction |
| Complete versus candidate release (Plan §6.7; PF10 §§2.7, 2.9, 2.10, 2.12 PR07 rows) | `README.md` "Release identity" (new bullet; lines 123–124 amended); `docs/RUN.md` line 12 addition; `docs/CLI_commands.md` admission bullet; `AGENTS.md` release-identity bullet |
| Unchanged FE/BE and numeric-free Reader promises (Plan §6.7) | `docs/config_and_bundles.md` FE/BE bullet; both contract pages; `README.md` EPIC040 block |
| Actual comparator/readiness commands (Plan §6.7) | `docs/CLI_commands.md` new section (primary); `README.md` EPIC040 block; `docs/RUN.md` Reader section pointer; `docs/config_and_bundles.md` line 5 (kept) |
| Non-mutation and security constraints (Plan §6.7) | `docs/CLI_commands.md` new section; `docs/config_and_bundles.md` writer recovery limits; `README.md` admission limits; contract pages (bounded body, read-only lookup, `no-store` errors); `docs/server/reader_v1.md` (`APP_ENV` behaviour stated truthfully) |
| How to find the authoritative 36-row evidence/decision; why Integration uses the broad grouping (Plan §6.7) | `README.md` EPIC040 block (primary); `docs/INDEX.md` orientation (pointer); `AGENTS.md` canon bullet |
| Reader v2 (PF10 §2.23) | `docs/contracts/reader_v2_public_bytes.md` (new); pointers from `README.md`, `docs/INDEX.md`, `docs/server/reader_v1.md`, `docs/contracts/reader_v1_public_bytes.md`, `docs/architecture/emitters.md` |
| `/api/reader` production route and version selection (PF10 §2.23) | `docs/contracts/reader_v2_public_bytes.md` "Route and request"; `docs/server/reader_v1.md` current-state block; `docs/acceptance/http_transport_evidence.md` and `docs/ADAPTER_009.md` route notes; `docs/RUN.md` Reader section; `FLASK_AUTO_RUN_GUIDE.md` |
| Conformed Reader v1 schema including the error branch (PF10 §§2.23, 2.25) | `docs/contracts/reader_v1_public_bytes.md`; `ARCHITECTURE.md` line 11 |
| Retired `*_leader` identities as history (PF10 §2.23) | `docs/contracts/reader_v1_public_bytes.md` "Retired identities (history)" |
| Current release `1.3.0` with 45 members (PF10 §2.25) | `README.md` EPIC040 block; `AGENTS.md`; `CHANGELOG.md` |
| Correction of `docs/server/reader_v1.md:42` (instruction §5.3) | `docs/server/reader_v1.md` |
| Canon status of C040-06/07/08 pointing to the decided record, drainage stated truthfully (instruction §5.4) | C040-06: `README.md`, `docs/INDEX.md`; C040-07: `docs/contracts/reader_v2_public_bytes.md`; C040-08: `docs/contracts/reader_v1_public_bytes.md`; summary: `AGENTS.md`, `CHANGELOG.md` |
| No second Canon catalog; no copy of the Plan or Audit (instruction §5.4) | design rule D-03; proof P-06 |
| Carried observations described, not fixed (instruction §8) | §13.3 |

### 5.2 Writing rules (applied to every edited line)

1. **Claim state** (PF03 §3 *Claim-state separation*): current implementation is stated only where §3.2 verified it; normative canon is routed, not restated; history is labelled at the point of use; examples are labelled synthetic.
2. **Routing by exact title** (PF03 §3 *Canonical ownership*; `AGENTS.md` "cite PF canon by title/§ only"): permanent PF documents are cited by their exact in-document title and section, without version numbers. PF10 addenda are cited by `PF10-HDE-Build-Notes` plus the addendum's exact heading and the register ID, not by addendum number (F-27; §2.3 shows the PR06b addendum was §2.24 in v13.3.5 and is §2.25 now). Durable documentation names `docs/ephemeral/` records by artifact ID only and does not link into `docs/ephemeral/`, which is pruned manually.
3. **No second canon** (PF03 §5): contract pages state the delivered route, shapes and transport needed to use the Reader, and route the normative contract to its owner and the machine contract to the schema file. They do not list the governed error pairs (the schema holds them), copy the 36-row table (PF10 holds it), or reproduce Plan, Audit or review text.
4. **Time-bound status**: every drainage statement reads "as of HDE-EPIC040-PR07", so it stays true after later drainage.
5. **Examples**: byte-exact copies of the named goldens without the trailing LF (D-02); no fixture content, real chart data, UUIDs other than obvious placeholders, or secret values (PF03 §13). Environment keys appear by name only.
6. **Literals**: no ASCII three-period ellipsis and no Unicode ellipsis in added text; full identifiers and full SHA-256 values where a digest is cited.
7. **Scope discipline**: edit only the lines §6 names; do not rewrite surrounding history, relabel other sections, or normalize unrelated wording.

### 5.3 Why the C040-06 pointer names PF10 and not the ADR path

The decided record is the `PF10-HDE-Build-Notes` addendum "HDE-EPIC040 — Record the approved source-backed Channel taxonomy and existing-state conformance": it carries the complete approved thirty-six-row table, the Gate-derived Centers, the counts, the rationale (items 2–4) and the drainage targets (item 8), and it names the original ADR `HDE-EPIC040-C040-06-HD-MECHANICS-ADR` v1.0, which retains the complete source ledger and row records. Runtime reads `catalog/channels_v1.json` only (item 8: "never this Markdown"). The documentation therefore routes readers to the PF10 addendum by title, names the ADR by artifact ID, and states that the permanent homes (`PF12-Canon-HDE-Schemas-and-Artifacts` §2.1 and `PF01-Canon-HDE-Math-Spec` §§6.1–6.2) have not yet received the drainage (F-20).

## 6. Exact file plan — per-file edit specifications

Each subsection gives the anchor as it stands at `48b0559`, the operation, and the text to apply. Text inside `~~~~` blocks is the content to write (the outer fence is not part of it). PR-30 may make editorial adjustments that keep every fact, qualifier, route and nonclaim, and must re-verify every fact at C0 (§9). If a fact no longer holds at PR-30's base, PR-30 stops and returns to this session (§12 R-01).

### 6.1 `docs/contracts/reader_v2_public_bytes.md` — NEW (D-01)

Justification: the only contract home, `docs/contracts/reader_v1_public_bytes.md`, is Reader v1 by filename and scope; `docs/server/reader_v1.md` is deprecated; C040-07 defines Reader v2 as a separate versioned contract with its own schema and goldens. A sibling page in the existing `docs/contracts/` home is the smallest fit. Complete content:

~~~~markdown
# Reader v2 — Public Bytes (contract summary and examples)

Reader v2 exposes the full Magic-10 set as bands only. HDE-EPIC040-PR06a delivered it. Reader v1 is unchanged and stays available on the same route; see `docs/contracts/reader_v1_public_bytes.md`.

## Owning sources

- Normative contract: `PF10-HDE-Build-Notes`, addendum "HDE-EPIC040-PR07-F01 — Add PR06a for Reader v2 Full Magic-10 Exposure and the Deferred Reader Contract Work" (Canon conflict C040-07). While that addendum is active, it is the authoritative source for Reader v2 and supersedes conflicting permanent canon, including the statement in `PF05-Canon-HDE-CLI-API-Vendor-Ref` that the production Reader refuses `v=2`.
- Drainage: as of HDE-EPIC040-PR07, C040-07 has not been drained into `PF01-Canon-HDE-Math-Spec`, `PF04-Canon-HDE-Governance`, `PF05-Canon-HDE-CLI-API-Vendor-Ref` or `PF12-Canon-HDE-Schemas-and-Artifacts`, nor into the consequential statements of `PF14-Canon-HDE-Mechanics-Guide` and `PF29-Canon-HDE-Users-Guide`. That drainage belongs to their maintainers.
- Machine contract: `schemas/reader.v2.schema.json` with its `schemas/reader.v2.schema.json.sha256` sidecar. The schema is a release member.
- Goldens: `goldens/reader/v2/`, written by `scripts/make_reader_v1_goldens.py`.

## Route and request (current implementation)

- Route: `POST /api/reader?v=2`. The same route serves Reader v1 with `v=1`, under the same request, lookup, eligibility and transport rules.
- Version selection: the query carries exactly one `v`, with the value `1` or `2`. A missing, empty, repeated or other value returns 400 `ERR_READER_INVALID_VERSION` before the body is read.
- Body: a JSON object with exactly the keys `a_id` and `b_id`, each a lowercase canonical UUID; at most 32,768 bytes; UTF-8 without a byte-order mark. Any other body returns 422 `ERR_READER_INVALID_INPUT`.
- Lookup: each identity is resolved by one read-only current-row lookup. An unavailable lookup returns 503 `ERR_M10_RESOLVER_UNAVAILABLE`; a missing row returns 404 `ERR_M10_PERSON_UNRESOLVED`.
- Other methods: every method other than `POST` on `/api/reader` returns 405 with the `ERR_NOT_FOUND` envelope, `Allow: POST` and `Cache-Control: no-store`.
- Known limitation: a path that no route serves, such as `/api/reader/missing`, receives the framework's HTML 404 from `adapter/factory.py` and `adapter/http_reader.py`; only `adapter/wsgi.py` answers with the JSON `ERR_NOT_FOUND` envelope. This gap belongs to the HTTP transport owner.

## Success body

- Exactly six keys: `categories`, `eligible`, `idempotence_hash`, `meta`, `reader_version` and `release_id`. `reader_version` is always `"v2"`. No field is numeric.
- Eligible pair: `categories` has exactly ten `{"band","id"}` items, one per Magic-10 category, in the canonical order of `catalog/magic10.json`: `harmony`, `heat`, `communication`, `alignment`, `comfort`, `consistency`, `expansion`, `creativity`, `drive`, `balance`. The array is ordered; it is not a set. Each `band` is `Cool`, `Open`, `Warm` or `Glow`.
- Ineligible pair: `categories` is `[]`.
- `idempotence_hash` is the SHA-256 of the canonical bytes of the other five keys. Canonical JSON, AB↔BA identity and two-run identity apply as they do to Reader v1.

## Error body

- Exactly four keys: `code`, `error`, `ok` (always `false`) and `schema` (always `"v1"`: the `error_v1` envelope version, not the Reader version).
- `code` and `error` are one of the governed pairs listed in `$defs.error` of `schemas/reader.v2.schema.json`.

## Transport

- Success: 200 with `Content-Type: application/json; charset=utf-8`, `Cache-Control: private, max-age=0, must-revalidate` and `Vary: Authorization, Accept-Encoding`. There is no `ETag`: `POST` is non-conditional and `If-*` headers are ignored.
- Errors: canonical `error_v1` bytes with `Cache-Control: no-store` and no `ETag`.

## Examples (synthetic)

Each example is the named golden without its trailing LF. Its `release_id` is a synthetic 64-character value, not the current release, and `meta` carries fixture values.

Eligible pair (`goldens/reader/v2/g03_eligible_ten_in_order.json`):

```json
{"categories":[{"band":"Cool","id":"harmony"},{"band":"Open","id":"heat"},{"band":"Warm","id":"communication"},{"band":"Glow","id":"alignment"},{"band":"Cool","id":"comfort"},{"band":"Open","id":"consistency"},{"band":"Warm","id":"expansion"},{"band":"Glow","id":"creativity"},{"band":"Cool","id":"drive"},{"band":"Open","id":"balance"}],"eligible":true,"idempotence_hash":"9e51c57b9e613d9c0f52486979c3c247c265c568a690240ff4e5a11ac445dea4","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v2","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Ineligible pair (`goldens/reader/v2/g01_ineligible.json`):

```json
{"categories":[],"eligible":false,"idempotence_hash":"a2cca383ec8f8542d1d4cd04841d5ee389d38fa0ad38b41b4ca7f49b3ff1e23b","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v2","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Unsupported version (`goldens/reader/v2/g04_error_invalid_version.json`):

```json
{"code":"ERR_READER_INVALID_VERSION","error":"unsupported reader version","ok":false,"schema":"v1"}
```

## Scope

- No CLI flag emits Reader v2. Reader↔CLI dump parity (`hdctl showcompat --dump-reader`) remains a Reader v1 family.
- No Reader v2 body carries a numeric, a prompt, a narrative key, a score, a UUID or a Gate value.
- This page describes the repository implementation. It does not establish QA, acceptance, deployment, activation or PF09 status.

Tests: `tests/http/test_reader_post_v2.py`, `tests/reader_v1/test_schema.py`, `tests/reader_v1/test_goldens.py` and `tests/reader_v1/test_emitter.py`.
~~~~

### 6.2 `docs/contracts/reader_v1_public_bytes.md` — rewrite of lines 5–25, history labelled

Anchors: line 3 (kept); lines 5–6 (invalid example, F-14); lines 8–11 (notes, kept); lines 13–19 (EPIC-004 block, kept and labelled); lines 21–25 (transport, kept and scoped). Resulting file, complete:

~~~~markdown
# Reader v1 — Public Bytes (example)

This page shows a single canonical example for Reader v1. All byte rules (serializer, idempotence, AB↔BA, two-run identity) are defined in the Spec.

Owning sources: the Reader v1 covenant is owned by `PF01-Canon-HDE-Math-Spec` §2.2 and §4.7, and its transport by `PF05-Canon-HDE-CLI-API-Vendor-Ref`. The machine contract is `schemas/reader.v1.schema.json` with its `.sha256` sidecar. Goldens live in `goldens/reader/v1/` and are written by `scripts/make_reader_v1_goldens.py`. Reader v2 is documented in `docs/contracts/reader_v2_public_bytes.md`.

Compact JSON body (synthetic example: `goldens/reader/v1/g03_harmony_open.json` without its trailing LF; its `release_id` is a synthetic 64-character value, not the current release):

```json
{"categories":[{"band":"Open","id":"harmony"}],"eligible":true,"idempotence_hash":"117b9f95a965ed280482fc4f8290536aa34ded9528acb7dbf19c2140fbc351e7","meta":{"engine_tag":"Isis5","invocation_tag":"INV-000000"},"reader_version":"v1","release_id":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}
```

Notes:
• Public body is numeric-free.
• The serializer is canonical (UTF-8, sorted keys, compact separators, exactly one trailing LF).
• The idempotence_hash is computed over the canonical preimage (body without that field), then re-serialized.
• The body has exactly six keys. `reader_version` is always `"v1"`, and `meta` has exactly `engine_tag` and `invocation_tag`. An eligible pair carries exactly one `harmony` item; an ineligible pair carries `"categories":[]` (`goldens/reader/v1/g01_minimal_ineligible.json`).

## Error body (C040-08)

Reader v1 errors have exactly four keys: `code`, `error`, `ok` (`false`) and `schema` (`"v1"`). The schema's error branch (`$defs.error`) admits only the governed code/message pairs that the production route (`POST /api/reader?v=1`) and dev `GET /reader` emit. `retry_after_ms` is not part of this envelope.

HDE-EPIC040-PR06b conformed the error branch to the emitted envelope under Canon conflict C040-08, recorded in `PF10-HDE-Build-Notes`, addendum "HDE-EPIC040-PR06b — Reader v1 error-envelope schema conformance (C040-08)". As of HDE-EPIC040-PR07, drainage of C040-08 into `PF01-Canon-HDE-Math-Spec` §2.3 and `PF04-Canon-HDE-Governance` §8.1.2, which still describe the envelope without `schema`, is pending with their maintainers.

Synthetic example (`goldens/reader/v1/g06_error_invalid_input.json` without its trailing LF):

```json
{"code":"ERR_READER_INVALID_INPUT","error":"invalid Reader request","ok":false,"schema":"v1"}
```

## Retired identities (history)

Before HDE-EPIC040-PR06a, the published schema and goldens used the category identities `open_leader`, `warm_leader`, `cool_leader` and `glow_leader`, and the schema permitted a `prompt` field. PR06a retired them from the contract, and no Reader route emits them. They remain only in retained historical records and in the legacy `scripts/hd_cli.py` stub, which is not a Reader surface.

<!-- EPIC-004 PATCH: bands-only + transport -->
## EPIC-004 — Reader v1 public payload posture
**Numeric-free**, bands-only surface. The engine selects **keys** (no copy).
Historical example (EPIC-004, shape only; not the current body shown above):
```json
{"compat":[{"id":"harmony","band":"warm"}]}
```

## EPIC-004 — HTTP Transport Evidence (Reader endpoints)
These rules apply to the dev Reader `GET /reader` (and `HEAD`). The production `POST /api/reader` is non-conditional: a success carries no `ETag`, the 304 and `HEAD` rules do not apply to it, and its errors follow the last rule below.
- **200**: JSON content-type; Cache-Control `private, max-age=0, must-revalidate`; `Vary: Authorization, Accept-Encoding` (exact order, single comma+space); **ETag = strong, quoted, lowercase-hex sha256(identity LF)** (pre-compression).
- **304 (after prior 200)**: **no body** (Content-Length 0 or absent); **omit Content-Type**; repeat validators (ETag / Vary / Cache-Control) **exactly**.
- **HEAD**: include Content-Type; **no body**; `Content-Length == len(identity bytes)`; validators **equal** to 200.
- **Errors/Writers**: JSON; **no-store**; **no ETag**.
~~~~

Change accounting against the current file: line 5 (`Compact JSON body (exact shape; one trailing LF implied):`) and line 6 (the invalid example) are replaced by the owning-sources paragraph, the new lead-in and the fenced example; one bullet is appended to the notes of lines 8–11; the "Error body (C040-08)" and "Retired identities (history)" sections are inserted before line 13; line 16 (`Example (shape only):`) is relabelled; one scope sentence is inserted after the line-21 heading. Every other existing line (1, 3, 8–11, 13–15, 17–19, 21–25) stays byte-identical, so PR-30 applies this with edits, not by retyping those lines.

### 6.3 `docs/server/reader_v1.md` — current-state block, lines 42 and 49 corrected, rest history

**Edit 1 — insert after line 8.** Line 8 is:

~~~~text
- `docs/acceptance/http_transport_evidence.md` for transport acceptance
~~~~

Insert directly after it, before the blank line 9 and the line-10 `---`:

~~~~markdown
- `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md` for the current public bodies

## Current state (HDE-EPIC040)

Everything below this section is retained history. Where it disagrees with this section, this section describes the current repository implementation.

- Production Reader: `POST /api/reader?v=1` (Reader v1) and `POST /api/reader?v=2` (Reader v2). The production blueprint (`get_reader_api_bp` in `adapter/http_reader.py`) is mounted under `/api` by every app factory: `adapter/factory.py`, `adapter/wsgi.py` and `adapter/http_reader.py::create_app`. Version selection, request body, lookup, transport and error rules are shared by both versions; see `docs/contracts/reader_v2_public_bytes.md`.
- Every method other than `POST` on `/api/reader` returns the governed 405 (`ERR_NOT_FOUND`, `Allow: POST`, `no-store`).
- Dev Reader: `GET /reader?v=1` (and `HEAD`) is Reader v1 only; any other `v` returns 400 `ERR_READER_INVALID_VERSION`. When `APP_ENV` is set to a value other than `dev`, it returns 403 `ERR_READER_FORBIDDEN`; an unset `APP_ENV` is treated as `dev`. `a` and `b` are chart paths resolved against the server's working directory that must resolve inside `fixtures/charts/` (for example `fixtures/charts/alice.json`); `a_tz` and `b_tz` are required when a chart has no `tz`.
- `POST /reader` (unprefixed) is not the production Reader: it returns the governed 405 with `Allow: GET, HEAD`.
- Local start: `scripts/dev_start_reader.sh` runs `python -m adapter.http_reader`, which binds `0.0.0.0` on `PORT` (default `8000`). Run it from the repository root. The legacy notice below names `dev/reader_harness/app.py`; as of HDE-EPIC040-PR07 that file raises `AttributeError` at import, so it is not a start path.
- Known limitation: a path that no route serves receives the framework's HTML 404 from `adapter/factory.py` and `adapter/http_reader.py`; `adapter/wsgi.py` answers with the JSON `ERR_NOT_FOUND` envelope.
~~~~

**Edit 2 — replace line 42** (the current line ends with one trailing space; the replacement has none):

~~~~text
GET /api/reader?v=1&a=<rel>&b=<rel>&a_tz=<IANA>&b_tz=<IANA> → returns LF-terminated public bytes identical to CLI for the same inputs.
~~~~

with:

~~~~markdown
GET /reader?v=1&a=<chart path>&b=<chart path>&a_tz=<IANA>&b_tz=<IANA> → dev Reader v1 (`APP_ENV=dev`); returns LF-terminated public bytes identical to the CLI `--dump-reader` sidecar for the same charts. The production Reader is `POST /api/reader?v=1|2` (see "Current state (HDE-EPIC040)" above); `GET /api/reader` returns 405.
~~~~

**Edit 3 — replace line 49** (the current line ends with one trailing space; the replacement has none):

~~~~text
a, b are relative paths resolved under fixtures/charts/. Absolute paths are rejected.
~~~~

with:

~~~~markdown
a, b are chart paths resolved against the server's working directory; each must resolve inside fixtures/charts/ (for example fixtures/charts/alice.json), so run the server from the repository root.
~~~~

Everything else in the file (the DEPRECATED title, the legacy notice, §§3–8, the change note) stays as retained history under the new block's statement. Line 40 (`GET /health`) is not edited: `/health` exists only in the non-starting `dev/reader_harness/app.py` (O-P07-03), which the block already labels.

### 6.4 `README.md`

**Edit 1 — replace line 1:**

~~~~text
# Glow HD Engine — HDE-EPIC039 current documentation
~~~~

with:

~~~~markdown
# Glow HD Engine — HDE-EPIC040 current documentation
~~~~

**Edit 2 — replace line 7:**

~~~~text
- Public Reader v1 and CLI share the canonical emitter and serializer; AB↔BA and two-run identity proofs cover public bytes.
~~~~

with:

~~~~markdown
- The public Reader (Reader v1 and, since HDE-EPIC040, Reader v2) and the CLI share the canonical emitter and serializer; AB↔BA and two-run identity proofs cover public bytes.
~~~~

**Edit 3 — insert before line 10** (`- What HDE-EPIC039 establishes for Calcination Pass 6:`):

~~~~markdown
- What HDE-EPIC040 establishes for Separation Pass 3 (current as of HDE-EPIC040-PR07; PR01 through PR06, PR06a and PR06b are accepted final):
  - Core: the supported Magic-10 core is the four-argument `engine/core/core.py::compute_core(member_a, member_b, mechanics_bundle, release_id)`, which returns one complete intrinsic `magic10_result.v1`; eligibility belongs to the caller. `engine/compat/compute.py::evaluate_pair` applies eligibility, obtains the admitted bundle and, for an eligible pair, returns the `magic10_compat_result.v1` document; the Reader and `hdctl showcompat` both call it.
  - Configuration and schemas: `catalog/magic10_mechanics_v1.json` (`magic10_mechanics_config.v1`, `config_id` `m10-channel-state-v1.0.0`) is validated against `schemas/magic10_mechanics_v1.schema.json`. Results use `schemas/magic10_result_v1.schema.json` and `schemas/magic10_compat_result_v1.schema.json`; the Channel and Gate catalogs use `schemas/channels_v1.schema.json` and `schemas/gates_v1.schema.json`. Sources and writers: `docs/config_and_bundles.md`.
  - Release: the admitted release is `catalog/manifest.json` version `1.3.0` with 45 members (`release_id` `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`). Only `engine.config.registry_loader.load_active_mechanics_bundle()` admits it, and only when the release is complete; a candidate root is validated or compared, never activated. See "Release identity" below.
  - Reader: production `POST /api/reader?v=1` (Reader v1) and `POST /api/reader?v=2` (Reader v2: the ten Magic-10 bands in canonical order); dev `GET /reader` stays Reader v1. Both public bodies remain bands-only and numeric-free. Contracts: `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md`.
  - Comparison and readiness: `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root>` compares the Magic-10 golden collection read-only; `python tools/bodygraph/check_magic10_gate_readiness.py --user-id <uuid>` reports current-row Gate readiness read-only. Details: `docs/CLI_commands.md`.
  - Channel taxonomy (C040-06): `catalog/channels_v1.json` carries the approved source-backed assignment for all 36 Channels. The decided record, with the complete 36-row table and its evidence, is the `PF10-HDE-Build-Notes` addendum "HDE-EPIC040 — Record the approved source-backed Channel taxonomy and existing-state conformance"; it names the original ADR `HDE-EPIC040-C040-06-HD-MECHANICS-ADR` v1.0, which keeps the full source ledger. `circuit_primary` is the Product's broad grouping (`individual`, `collective` or `tribal`). Official broad-group exposition places Integration in Individual, so the four Integration Channels (`10-20`, `10-57`, `20-34`, `34-57`) are `individual` with substream `integration`, while Integration's separate formal structure is preserved; Channel-specific evidence keeps `10-34` as `individual`/`centering` and `20-57` as `individual`/`knowing`. As of HDE-EPIC040-PR07, drainage into `PF12-Canon-HDE-Schemas-and-Artifacts` §2.1 and `PF01-Canon-HDE-Math-Spec` §§6.1–6.2 is pending with their maintainers.
  - Canon status as of HDE-EPIC040-PR07: C040-07 (Reader v2) and C040-08 (Reader v1 error envelope) are decided and delivered; their drainage into permanent canon is pending with the maintainers named on the two contract pages.
  - Nonclaims: this documentation establishes no QA verdict, acceptance, OPS01 attestation, deployment, activation, PF09 movement or epic closure.
~~~~

**Edit 4 — replace line 123:**

~~~~text
- Runtime identity derives that digest once from the packaged manifest; release cuts never rewrite a Python identity constant. `catalog` is package data, so source checkouts and installed builds use the same bytes.
~~~~

with:

~~~~markdown
- Runtime identity derives that digest once from the packaged manifest; release cuts never rewrite a Python identity constant. `catalog` is package data, so source checkouts and installed builds carry the same manifest bytes. Known limitation: a wheel built from this tree omits 16 of the 45 release members (for example the files under `schemas/` and `catalog/narratives/`), and admission fails closed unless every member is present with its recorded bytes, so run admission-dependent commands from a source checkout. The packaging fix belongs to the packaging owner.
~~~~

**Edit 5 — replace line 124:**

~~~~text
- A release cut intentionally changes only the manifest: `python scripts/cut_release_manifest.py --version <semver> --built-at-utc <YYYY-MM-DDTHH:MM:SSZ>`. `python scripts/release_id_recompute.py --check-manifest-only` validates the committed input and declared file hashes without reading or repairing derivatives.
~~~~

with the two lines:

~~~~markdown
- The cutter writes only the manifest: `python scripts/cut_release_manifest.py --version <semver> --built-at-utc <YYYY-MM-DDTHH:MM:SSZ>` (`--roster-from-admission` builds the membership from the admission roster; `--check` compares the committed manifest with a fresh cut without writing). `python scripts/release_id_recompute.py --check-manifest-only` validates the committed input and declared file hashes without reading or repairing derivatives.
- Complete versus candidate release (HDE-EPIC040): admission accepts only the complete release pinned in `engine/config/registry_loader.py` by `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and the 45-path `ADMITTED_RELEASE_ROSTER`, with every member's bytes, hash and size matching the manifest and the executing mechanics modules equal to their admitted members. Otherwise it refuses, for example with `INCOMPLETE_RELEASE_ROSTER`, `RELEASE_ROSTER_MISMATCH`, `RELEASE_VERSION_MISMATCH` or `RELEASE_TIMESTAMP_MISMATCH`. A new release therefore changes those constants in `engine/config/registry_loader.py`, itself a member, before the cut. A candidate root is only validated or compared (for example with `--compare-goldens`); it is never activated. Limits: the executing-module check proves executable-code equivalence for eight first-party modules, not the historical bytes the interpreter read or resistance to arbitrary in-process tampering; admission provides no process-death atomicity, multi-file atomic visibility or cross-process locking.
~~~~

**Edit 6 — replace lines 142–143** (inside the Quickstart `bash` fence):

~~~~text
# Aux narrative preview for a compat tuple (admin/test)
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC hdctl aux-preview --pair-file artifacts/presenter/showcompat_identity_summary.json --category <category_slug> --band Cool --perspective shared --show-narrative
~~~~

with:

~~~~text
# Aux narrative preview for a compat tuple (admin/test): the pair file is showcompat stdout
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json > /tmp/pair.json
SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC hdctl aux-preview --pair-file /tmp/pair.json --category harmony --band Cool --perspective shared --show-narrative
~~~~

**Edit 7 — replace line 146:**

~~~~text
- Replace `<category_slug>` with a narrative category slug from the sealed Aux pack; `--band` remains sealed to `{Cool,Open,Warm,Glow}` and `--perspective` to `{shared,a_to_b,b_to_a}`.
~~~~

with:

~~~~markdown
- `--pair-file` must be a `magic10_compat_result.v1` document such as `hdctl showcompat` stdout, and `--category` a Magic-10 category id present in it (for example `harmony`); `--band` remains sealed to `{Cool,Open,Warm,Glow}` and `--perspective` to `{shared,a_to_b,b_to_a}`.
~~~~

**Edit 8 — replace line 169** ("Deeper docs"):

~~~~text
- Deeper docs: `docs/INDEX.md` (map), `docs/EVIDENCE_INDEX.md` (evidence pointers), `docs/CLI_commands.md` (CLI flags/guardrails), `docs/acceptance/http_transport_evidence.md` (A7 transport posture), and `docs/ENDPOINTS_CATALOG.json` (endpoint catalog, internal-only).
~~~~

with:

~~~~markdown
- Deeper docs: `docs/INDEX.md` (map), `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md` (Reader bodies), `docs/EVIDENCE_INDEX.md` (evidence pointers), `docs/CLI_commands.md` (CLI flags/guardrails), `docs/acceptance/http_transport_evidence.md` (A7 transport posture), and `docs/ENDPOINTS_CATALOG.json` (endpoint catalog, internal-only).
~~~~

**Edit 9 — line 176** (the `showcompat` bullet): append one space and this sentence at the end of the line:

~~~~markdown
Non-conjunction stdout is the canonical `magic10_compat_result.v1` document; Reader v1 bytes come only from the `--dump-reader` sidecar.
~~~~

**Edit 10 — append after line 209** (the last "Testing (minimal)" bullet):

~~~~markdown
- Reader v1/v2 production route, schemas and goldens: `tests/http/test_reader_post_v1.py`, `tests/http/test_reader_post_v2.py` and `tests/reader_v1/`.
- Admission, golden comparison and readiness: `tests/config/test_production_admission.py`, `tests/config/test_config_artifacts.py` and `tests/bodygraph/test_check_magic10_gate_readiness.py`.
~~~~

Lines 106–118 (history), every EPIC0xx block and every other line stay unchanged.

### 6.5 `CHANGELOG.md` — new top entry

Insert after line 2 (the blank line after `# CHANGELOG`) and before line 3, which is:

~~~~text
Unreleased — HDE-EPIC039: Calcination Pass 6 documentation alignment (README/CHANGELOG/AGENTS/docs/)
~~~~

the entry below, followed by one blank line:

~~~~markdown
Unreleased — HDE-EPIC040: Separation Pass 3 final repository documentation (README/CHANGELOG/AGENTS/docs/)

### Added
- Documented the delivered HDE-EPIC040 contract: the four-argument `compute_core(member_a, member_b, mechanics_bundle, release_id)` core reached through `evaluate_pair`; the strict `magic10_mechanics_config.v1`, `magic10_result.v1` and `magic10_compat_result.v1` schemas; canonical writers and sources; and the complete-versus-candidate boundary of the admitted `1.3.0` release with 45 members.
- Added `docs/contracts/reader_v2_public_bytes.md` for Reader v2 (`POST /api/reader?v=2`: the ten Magic-10 bands in canonical order, `[]` when ineligible, bands-only and numeric-free) and documented the production route `POST /api/reader` with its `v=1`/`v=2` selection.
- Documented the read-only golden comparator (`generate_config_artifacts.py --compare-goldens`) and Gate-readiness tool (`check_magic10_gate_readiness.py`) with their non-mutation and closed-rails constraints, and routed readers to the decided C040-06 Channel taxonomy record, including why Integration uses the broad `individual` grouping.

### Changed / Fixed
- Corrected the Reader v1 contract page: a schema-valid example from the goldens, the conformed error branch (`schema`, `ok`, `code`, `error`; governed pairs only; C040-08) and the retired `*_leader` identities recorded as history.
- Corrected live-path descriptions: `docs/server/reader_v1.md` no longer documents `GET /api/reader` (the production Reader is `POST /api/reader`; dev `GET /reader` is Reader v1); the transport-evidence pages scope the Reader 405 predicate to the unprefixed `POST /reader`; the README `aux-preview` example reads a `showcompat` stdout pair file; the release-cut guidance names the admission constants a new release must change; and configuration pages name the current Magic-10 sources.
- Recorded Canon status: C040-06, C040-07 and C040-08 are decided and delivered, and their drainage into permanent PF canon is pending with its maintainers as of HDE-EPIC040-PR07. No QA verdict, acceptance, OPS01 attestation, deployment, activation, PF09 movement or epic closure is claimed.
~~~~

`CHANGELOG.md` is excluded from the retired-key scan (F-22) but carries no retired key anyway.

### 6.6 `docs/CLI_commands.md`

**Edit 1 — insert after line 14:**

~~~~text
- `hdctl aux-preview --pair-file <compat.json> --category <slug> --band <band> --perspective <perspective> [--show-narrative] [--admin-out <ids.json>]`
~~~~

the sub-bullet:

~~~~markdown
  - `<compat.json>` is a `magic10_compat_result.v1` document such as `hdctl showcompat` stdout; `--category` is a Magic-10 category id present in it.
~~~~

**Edit 2 — in line 24, replace these two sentences** (the rest of the line stays):

~~~~text
Showcompat stdout is the canonical emitter output for compat or conjunction payloads and may include numeric scores/weights as captured in governed evidence. Reader v1 bytes are emitted via `--dump-reader` sidecar files (shared `emit_reader_public_envelope` path) and align with the Reader harness.
~~~~

with:

~~~~markdown
Showcompat stdout (non-conjunction) is the canonical `magic10_compat_result.v1` document (`schemas/magic10_compat_result_v1.schema.json`); it carries numeric scores and signals and is not a public Reader body. Conjunction mode emits the conjunction contract. Reader v1 bytes are emitted only via `--dump-reader` sidecar files (shared `emit_reader_public_envelope` path) and match dev `GET /reader` bytes for the same charts. Known gap: the one-line `hdctl --help` summary for `showcompat` still reads "Emit canonical Reader v1 bytes from vendor JSON"; the stdout contract above is current.
~~~~

**Edit 3 — insert after line 29** (the end of "## Guards"), preceded by one blank line:

~~~~markdown
## Magic-10 comparison, readiness and admission (HDE-EPIC040)

Both tools are read-only and refuse outside the closed rails (`LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0`).

- Golden comparison: `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root> [--goldens <path>] [--report <path>]`
  - Admits the explicit candidate root through the admission owner and runs the Magic-10 golden collection (default `tests/fixtures/magic10/v1/goldens.json`, cases `M10-G001` to `M10-G008`) through the canonical kernel and application entrypoints.
  - Exit codes: 0 when every case matches, 1 on any mismatch, 5 on refusal. The report (`magic10_golden_comparison.v1`) lists every mismatch; `--report` writes it to a path outside the candidate root and the repository, never over the goldens file.
  - It never writes, activates or regenerates configuration, manifest or fixtures.
- Gate readiness: `python tools/bodygraph/check_magic10_gate_readiness.py --user-id <uuid> [--user-id <uuid>]` or `--selection-file <path>` (one canonical UUID per line; blank lines and `#` comments ignored; a regular, non-symlinked file of at most 1,048,576 bytes).
  - Reads each selected current row once through `DBAccess` and reports aggregate, identity-safe counts as `magic10_gate_readiness.v1`, with `readiness` `READY` or `NOT_READY`.
  - Exit codes: 0 when a report is emitted; 5 on refusal, with one stderr token: `RAILS_CLOSED_REQUIRED:<pins>`, `READINESS_EMPTY_SELECTION`, `READINESS_SELECTION_INVALID` or `READINESS_UNAVAILABLE`. An unavailable database is never reported as ready.
  - It issues no `UPDATE`, `INSERT` or `DELETE` and performs no acquisition, repair, backfill or vendor call. It reads through the database configured by `DATABASE_URL`; never print or commit that value.
- Active admission: `engine.config.registry_loader.load_active_mechanics_bundle()` returns the admitted bundle only for the complete release and takes no root or override argument. See `README.md`, "Release identity".
~~~~

The H1 (`(HDE-EPIC027)`) and every other section stay unchanged.

### 6.7 `docs/RUN.md`

**Edit 1 — replace line 5:**

~~~~text
- Disable auto-reload when capturing evidence. Reader harness binds to http://127.0.0.1:5000 when run locally (dev helper can override port via `PORT`).
~~~~

with:

~~~~markdown
- Disable auto-reload when capturing evidence. The dev Reader helper `scripts/dev_start_reader.sh` runs `python -m adapter.http_reader`, which binds `0.0.0.0` on `PORT` (default `8000`).
~~~~

**Edit 2 — replace line 10:**

~~~~text
- Registry report spot-check: `python tools/generate_registry_report.py --check` to validate catalog inputs and serializer wiring.
~~~~

with:

~~~~markdown
- Registry and configuration spot-check: `python tools/config/generate_config_artifacts.py --check` validates the committed registry report, `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json` without writing. `python tools/generate_registry_report.py` has no check mode; it writes the registry report.
~~~~

**Edit 3 — append to line 12**, after its final sentence `This updates only the manifest; commit that input once.`, one space and:

~~~~markdown
A new release version also changes `ADMITTED_RELEASE_VERSION` (and, where they change, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER`) in `engine/config/registry_loader.py` before the cut, because admission compares the manifest with those constants and that file is itself a release member.
~~~~

**Edit 4 — insert after line 19** (the last "## Release-sanity posture" bullet), preceded by one blank line:

~~~~markdown
## Reader (HDE-EPIC040)
- Start locally from the repository root: `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PORT=8000 scripts/dev_start_reader.sh`.
- Dev Reader v1: `curl -s 'http://127.0.0.1:8000/reader?v=1&a=fixtures/charts/alice.json&b=fixtures/charts/bob.json&a_tz=UTC&b_tz=UTC'`. The bytes equal the `--dump-reader` sidecar of `hdctl showcompat --a-file fixtures/charts/alice.json --b-file fixtures/charts/bob.json --dump-reader <out.json>` for the same charts.
- Production Reader: `POST /api/reader?v=1` or `POST /api/reader?v=2` with the body `{"a_id":"<uuid>","b_id":"<uuid>"}`. It resolves both identities through a read-only current-row lookup, so it needs a configured database; without one it returns 503 `ERR_M10_RESOLVER_UNAVAILABLE`. Contracts: `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md`.
- Golden comparison, Gate readiness and admission: `docs/CLI_commands.md`, "Magic-10 comparison, readiness and admission (HDE-EPIC040)".
~~~~

The curl line is kept only if PR-30 verifies it by starting the helper (P-14). If the environment cannot bind the port, PR-30 removes the curl line, keeps the route statement and records the limitation.

### 6.8 `docs/config_and_bundles.md`

**Edit 1 — insert after line 1** (the H1), so the new section precedes line 3 (`## Governed config artifacts (D5)`):

~~~~markdown

## Current Magic-10 configuration (HDE-EPIC040)
- Mechanics configuration: `catalog/magic10_mechanics_v1.json` (`magic10_mechanics_config.v1`, `config_id` `m10-channel-state-v1.0.0`, `result_schema` `magic10_result.v1`), validated against `schemas/magic10_mechanics_v1.schema.json`. Its `sources` bind `catalog/magic10_caps.json`, `catalog/magic10.json`, `catalog/channels_v1.json` and `math/thresholds.json` by SHA-256.
- Result schemas: `schemas/magic10_result_v1.schema.json` (intrinsic core result) and `schemas/magic10_compat_result_v1.schema.json` (application result; `hdctl showcompat` stdout). Catalog schemas: `schemas/channels_v1.schema.json` and `schemas/gates_v1.schema.json`. All are release members.
- Writers (canonical owners; never hand-edit their outputs): `tools/config/generate_config_artifacts.py` writes `artifacts/registry/registry_report.json`, `artifacts/thresholds/magic10_config.json` and `artifacts/thresholds/band_edges.json` (`--check` validates them without writing; `--publish-family` publishes the scoped config family, catalog logs, bundles and required evidence companions); `tools/config/generate_bundles.py` writes `artifacts/config_bundles/fe_bundle.json` and `artifacts/config_bundles/be_bundle.json`; `tools/generate_registry_report.py` writes the registry report; `tools/evidence/update_evidence_index.py` publishes the Index/Mirror companions.
- FE/BE promise: the bundle schema identities `config_bundle.fe.v1` and `config_bundle.be.v1` are unchanged by HDE-EPIC040, and the Channel fields `primary_domain`, `domains` and `flags` remain non-scoring Product metadata (`PF12-Canon-HDE-Schemas-and-Artifacts` §2.1).
- Writer recovery limits: the config-family writers restore on caught failures, refuse source/destination races, keep check paths non-writing and preserve conflicting external changes. They do not promise crash atomicity, multi-file atomic visibility or cross-process locking.
~~~~

**Edit 2 — replace line 6:**

~~~~text
- Current governed files include `config/bands_4B60_v1.json` and `config/toggles_v1.json` (Magic-10 banding and feature toggles).
~~~~

with:

~~~~markdown
- `config/bands_4B60_v1.json` and `config/toggles_v1.json` remain in the tree, but the current Magic-10 mechanics and band-edge writers do not read them (no reader in `engine/`, `adapter/`, `presenter/`, `scripts/` or `tools/` as of HDE-EPIC040-PR07); band edges come from `math/thresholds.json`.
~~~~

Line 5 (the PR05 comparator line) and the rest stay unchanged.

### 6.9 `docs/INDEX.md`

**Edit 1 — replace line 1:**

~~~~text
# HD Engine Repo Docs — Index (HDE-EPIC039 current)
~~~~

with:

~~~~markdown
# HD Engine Repo Docs — Index (HDE-EPIC040 current)
~~~~

**Edit 2 — insert before line 3** (`## HDE-EPIC039 Calcination Pass 6 orientation`), followed by one blank line:

~~~~markdown
## HDE-EPIC040 Separation Pass 3 orientation
- Reader: production `POST /api/reader?v=1` and `POST /api/reader?v=2`; dev `GET /reader` (Reader v1). Contracts: `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md`; dev usage and route history: `docs/server/reader_v1.md`; route catalog: `docs/ENDPOINTS_CATALOG.json`.
- Core and application: `engine/core/core.py::compute_core(member_a, member_b, mechanics_bundle, release_id)`, reached through `engine/compat/compute.py::evaluate_pair`.
- Configuration, schemas and writers: `docs/config_and_bundles.md`. Release identity and the complete-versus-candidate boundary: `README.md`, "Release identity".
- Read-only comparison and readiness: `docs/CLI_commands.md`, "Magic-10 comparison, readiness and admission (HDE-EPIC040)".
- Channel taxonomy (C040-06): `catalog/channels_v1.json`; decided record: the `PF10-HDE-Build-Notes` addendum "HDE-EPIC040 — Record the approved source-backed Channel taxonomy and existing-state conformance"; the Integration rationale is in `README.md`. Drainage into `PF12-Canon-HDE-Schemas-and-Artifacts` §2.1 and `PF01-Canon-HDE-Math-Spec` §§6.1–6.2 is pending as of HDE-EPIC040-PR07.
- Nonclaims: no QA verdict, acceptance, OPS01 attestation, deployment, activation, PF09 movement or epic closure.
~~~~

**Edit 3 — replace line 80:**

~~~~text
- Engine Core compute: `engine/core/core.py::compute_core`
~~~~

with:

~~~~markdown
- Engine Core compute: `engine/core/core.py::compute_core` (four arguments: `member_a`, `member_b`, `mechanics_bundle`, `release_id`; eligibility belongs to the caller, `engine/compat/compute.py::evaluate_pair`)
~~~~

**Edit 4 — replace line 89:**

~~~~text
- Governed configs live in `config/` (Magic-10 bands, toggles). Regenerate via `tools/config/generate_config_artifacts.py` and index with PF12 discipline.
~~~~

with:

~~~~markdown
- Magic-10 configuration sources are `catalog/magic10_mechanics_v1.json`, `catalog/magic10.json`, `catalog/magic10_caps.json`, `catalog/magic10_seeds.json`, `catalog/channels_v1.json` and `math/thresholds.json`; `tools/config/generate_config_artifacts.py` writes the derived artifacts, indexed with PF12 discipline (see `docs/config_and_bundles.md`). The Magic-10 writers do not read `config/bands_4B60_v1.json` or `config/toggles_v1.json`.
~~~~

### 6.10 `docs/acceptance/http_transport_evidence.md` — route note

**Edit 1 — insert after line 18**, the last predicate bullet:

~~~~text
- `COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 typed `invalid_json`, `no-store`, no ETag (GET remains probe-only; POST is the compat compute surface).
~~~~

one blank line and:

~~~~markdown
Current routes (HDE-EPIC040): the 200, 304 and HEAD predicates above apply to the dev Reader `GET /reader`, the route the A7 transport proofs select from `docs/ENDPOINTS_CATALOG.json`. `HTTP_POST_METHOD_POSTURE_OK` keeps its original meaning, which now holds for the unprefixed `POST /reader`: it returns the governed 405 (`ERR_NOT_FOUND`, `Allow: GET, HEAD`, `no-store`, no ETag). The production Reader is `POST /api/reader?v=1` or `?v=2`: a success is 200, non-conditional and carries no ETag; its errors are `no-store` without ETag; every other method on `/api/reader` returns 405 with `Allow: POST`. See `docs/contracts/reader_v2_public_bytes.md`.
~~~~

The predicate labels and wording stay unchanged (retained identifiers keep their original meanings).

### 6.11 `docs/ADAPTER_009.md` — route note and one parity line

**Edit 1 — insert after line 174**, the last predicate bullet of the duplicated section:

~~~~text
- `COMPAT_GET_BODY_400_OK` — Compat GET with body ⇒ 400 typed `{"error":"body_not_allowed"}`, `no-store`, no ETag.
~~~~

one blank line and the same "Current routes (HDE-EPIC040)" paragraph as §6.10.

**Edit 2 — replace line 178:**

~~~~text
Bytes are LF-terminated; CLI output equals the Reader identity bytes (parity).
~~~~

with:

~~~~markdown
Bytes are LF-terminated; Reader↔CLI parity is defined via the CLI `--dump-reader` sidecar (not `showcompat` stdout), as in `docs/acceptance/http_transport_evidence.md`.
~~~~

The readiness rules (lines 46–52) and port statements are not edited (O-P07-05).

### 6.12 `AGENTS.md` — additive only

**Edit 1 — insert before line 96** (`## HDE-EPIC039 current workflow posture`), followed by one blank line:

~~~~markdown
## HDE-EPIC040 current posture (Separation Pass 3)
- Current release: `catalog/manifest.json` version `1.3.0`, 45 members. Admission (`engine.config.registry_loader.load_active_mechanics_bundle()`) accepts only the complete release pinned by `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER` in `engine/config/registry_loader.py` and fails closed otherwise; a candidate root is only validated or compared, never activated.
- Supported core: `engine/core/core.py::compute_core(member_a, member_b, mechanics_bundle, release_id)`; eligibility belongs to the caller. The Reader and `hdctl showcompat` reach it through `engine/compat/compute.py::evaluate_pair`.
- Reader: production `POST /api/reader?v=1` and `?v=2` (Reader v1 and Reader v2); dev `GET /reader` is Reader v1. Contract pages: `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md`. Both bodies stay bands-only and numeric-free.
- Read-only tools: `python tools/config/generate_config_artifacts.py --compare-goldens <candidate-root>` and `python tools/bodygraph/check_magic10_gate_readiness.py`; both refuse outside closed rails, and neither modifies the repository, activates a release, acquires data or backfills (`--report` writes only outside the candidate root and the repository).
- Canon: C040-06, C040-07 and C040-08 are decided and delivered. As of HDE-EPIC040-PR07 their drainage into permanent PF canon is pending with its maintainers, and the `PF10-HDE-Build-Notes` addenda stay authoritative until then. Cite those addenda by their heading, not by PF10 section number: addendum numbers have changed between PF10 versions.
- Nonclaims: HDE-EPIC040 documentation establishes no QA verdict, acceptance, OPS01 attestation, deployment, activation, PF09 movement or epic closure; OPS01 verifies the `1.3.0` release separately.
~~~~

**Edit 2 — insert after line 108:**

~~~~text
- Intentional cuts use `python scripts/cut_release_manifest.py --version <semver> --built-at-utc <UTC>` and change only `catalog/manifest.json`. Validate the source input with `python scripts/release_id_recompute.py --check-manifest-only`.
~~~~

the bullet:

~~~~markdown
- HDE-EPIC040 admission addition: the cutter still writes only `catalog/manifest.json`, but admission compares the manifest with `ADMITTED_RELEASE_VERSION`, `ADMITTED_RELEASE_BUILT_AT_UTC` and `ADMITTED_RELEASE_ROSTER` in `engine/config/registry_loader.py`, which is itself a release member. A new release changes those constants before the cut; `--roster-from-admission` builds the membership from that roster.
~~~~

No existing `AGENTS.md` line is changed, moved or removed. The inserted lines contain no "bridge" wording (F-22, P-08).

### 6.13 `docs/architecture/emitters.md` — line 16 (additional affected home)

**Edit 1 — replace line 16:**

~~~~text
- Public surfaces: Reader v1 endpoints and `hdctl showcompat` share the presenter/emitter and remain the only public APIs.
~~~~

with:

~~~~markdown
- Public surfaces: the Reader endpoints (Reader v1, and since HDE-EPIC040 Reader v2, on `POST /api/reader`; the dev `GET /reader` is Reader v1) and `hdctl showcompat` share the presenter/emitter and remain the only public APIs. See `docs/contracts/reader_v1_public_bytes.md` and `docs/contracts/reader_v2_public_bytes.md`.
~~~~

### 6.14 `FLASK_AUTO_RUN_GUIDE.md` — three lines (additional affected home)

**Edit 1 — replace line 131:**

~~~~text
**Code Structure**:
~~~~

with:

~~~~markdown
**Code Structure** (abridged; see `adapter/factory.py`):
~~~~

**Edit 2 — insert after line 135** (inside the `python` fence):

~~~~text
    app.register_blueprint(bp, url_prefix="")  # Register routes
~~~~

the line:

~~~~text
    app.register_blueprint(api_bp, url_prefix="/api")  # production Reader: POST /api/reader
~~~~

**Edit 3 — replace line 191:**

~~~~text
**Integration**: Blueprint is mounted at root path (`url_prefix=""`)
~~~~

with:

~~~~markdown
**Integration**: the dev/internal blueprint is mounted at the root path (`url_prefix=""`); since HDE-EPIC040 the production Reader blueprint (`api_bp`) is mounted under `/api`, serving `POST /api/reader?v=1` and `?v=2`.
~~~~

### 6.15 `ARCHITECTURE.md` — line 11 only

**Edit 1 — replace line 11:**

~~~~text
  - Errors: `engine/errors/envelope.py` (`{ok,false,code,error}`)
~~~~

with:

~~~~markdown
  - Errors: `engine/compat/errors.py::error_envelope` builds the governed `error_v1` envelope with keys `schema` (`"v1"`), `ok` (`false`), `code` and `error`, adding `details` only when a caller passes one (the Reader routes never do); the Reader error branches are `$defs.error` of `schemas/reader.v1.schema.json` and `schemas/reader.v2.schema.json`.
~~~~

Justification: line 11 states the error-envelope contract, which C040-08 decided, at a module path absent since before EPIC040 (F-24). Every other line stays (O-P07-06).

### 6.16 Generated companions and records

- Generated companions: none. No planned path is an Index/Mirror row, a path-proofed artifact, a release member or an input of any generator (F-22). Running `tools/evidence/update_evidence_index.py` or any other writer is excluded; the read-only checks of P-10 prove nothing drifted.
- Result record: PR-30 adds `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.0.md` in a separate records commit (§9 C5). No existing `docs/ephemeral/` file is edited.

## 7. Requirement-to-change-and-proof mapping

| Requirement | Change (§6) | Proof (§8) |
| --- | --- | --- |
| Instruction §5.1 / Plan §6.7 *Required content*, all nine items | §5.1 content map; §§6.4, 6.6–6.9, 6.12 | P-01, P-02, P-03, P-14, P-15 |
| Instruction §5.2 / PF10 §2.23 *Work-unit effects*: Reader v2, `/api/reader` and version selection, conformed v1 schema | §§6.1, 6.2, 6.3, 6.10, 6.11, 6.13, 6.14 | P-04, P-13, P-14 |
| PF10 §2.25 *Work-unit effects*: v1 schema as PR06b delivered it; release `1.3.0` | §§6.2, 6.4, 6.5, 6.12, 6.15 | P-04, P-13, P-14 |
| Instruction §5.2: retired `*_leader` identities as history | §6.2 | P-06, P-15 |
| Instruction §5.3: live-path corrections incl. `docs/server/reader_v1.md:42` | §§6.3, 6.4 (Edits 4–7, 9), 6.6, 6.7, 6.8, 6.9, 6.10, 6.11, 6.13, 6.14, 6.15 | P-03, P-14 |
| Instruction §5.4: C040-06/07/08 point to the decided record; drainage stated truthfully; no second canon; no Plan/Audit copy | §§5.2, 5.3, 6.1, 6.2, 6.4, 6.9, 6.12 | P-06, P-15 |
| PF10 §§2.7, 2.9, 2.10, 2.12 PR07 rows: delivered admission contract and reviewed limits | §6.4 Edits 4–5; §6.8 | P-02, P-15 |
| Instruction §7: every command, path, symbol, route, key and constant exists; examples validate; links resolve; no false claims; no secrets or real chart data; CI on the exact head | whole change | P-01 to P-12; CI |
| Instruction §8 exclusions | §4.3 | P-10, P-11 |
| K040-REQ-001 (PR07 share: final documentation completing the ordered chain) | whole change | completion §4.2 |
| K040-REQ-002 (exact source homes by stable title; C040-06 disposition; no second home) | §5.2 rules 2–3; §§6.4, 6.9 | P-06 |
| K040-REQ-013 (native exact identities; no token ceremony) | exact paths, symbols, IDs and digests; no acceptance token introduced | P-01, P-02, P-06 |
| AC040-01 (source ownership explicit; Canon conflicts with named drainage) and AC040-09 (public Reader bands-only and numeric-free; decisions attributable) | §§6.1, 6.2, 6.4, 6.12 | P-04, P-06 |

## 8. Proof design

PR-30 runs every proof on the committed candidate head in a detached scratch worktree outside the repository, under the rails of §10.1, and records each command, exit status (from a capture that carries the producer's own status, per `AGENTS.md`) and result in the result artifact.

| ID | Proof | Pass condition |
| --- | --- | --- |
| P-01 | Path existence: every backticked repository path in added or changed lines of the fifteen files (`git diff -U0 origin/main...HEAD`) exists at the head; angle-bracket placeholders, URLs, globs and route strings are excluded; `docs/ENDPOINTS_CATALOG.json` resolves through its symlink | no missing path |
| P-02 | Symbol and constant existence, by `grep -n` at the head: `def compute_core(member_a, member_b, mechanics_bundle, release_id)`; `def evaluate_pair(`; `def load_active_mechanics_bundle(`; `ADMITTED_RELEASE_VERSION = "1.3.0"`; `ADMITTED_RELEASE_BUILT_AT_UTC`; `ADMITTED_RELEASE_ROSTER`; the refusal codes `INCOMPLETE_RELEASE_ROSTER`, `RELEASE_ROSTER_MISMATCH`, `RELEASE_VERSION_MISMATCH`, `RELEASE_TIMESTAMP_MISMATCH`; `def get_reader_api_bp(`; `def error_envelope(`; `def emit_reader_public_envelope(`; `_READER_MAX_BODY_BYTES = 32_768`; `SELECTION_FILE_MAX_BYTES = 1_048_576`; `REPORT_SCHEMA = "magic10_gate_readiness.v1"`; `COMPAT_RESULT_SCHEMA = "magic10_compat_result.v1"`; `--roster-from-admission`; the eight modules named by `_admission_execution_provenance` | each found; the eight-module count confirmed by reading |
| P-03 | Command execution (closed rails): `python tools/config/generate_config_artifacts.py --check` → 0; `--compare-goldens . --report <scratch>/golden_report.json` → 0 and `ok: true`; `python tools/bodygraph/check_magic10_gate_readiness.py --help` → 0; the same without a selection → 5 `READINESS_EMPTY_SELECTION`; with `SAFE_MODE=0` → 5 `RAILS_CLOSED_REQUIRED:[('SAFE_MODE', '1')]`; `python tools/generate_registry_report.py --help` shows no `--check`; `python scripts/release_id_recompute.py --check-manifest-only` → 0; `python scripts/cut_release_manifest.py --version 1.3.0 --built-at-utc 2026-08-24T18:04:49Z --check` → 0, and again with `--roster-from-admission` → 0; admission one-liner prints `AdmittedMechanicsBundle 1.3.0 45` and a `release_id` equal to the manifest digest; `git status` clean afterwards | all as stated; the readiness tool is never run with a database configured |
| P-04 | Examples: extract every fenced `json` block from the two contract pages that names a golden (five blocks; the historical EPIC-004 `compat` example is excluded and must stay labelled historical); each equals the named golden's bytes minus the trailing LF; each validates against `schemas/reader.v1.schema.json` or `schemas/reader.v2.schema.json` (`jsonschema` Draft 2020-12, the schema matching the golden's directory); for each success example, the SHA-256 of `engine.presenter.emitter.emit_public(<the body without idempotence_hash>)` equals its `idempotence_hash` | byte-equal, valid, hash recomputes |
| P-05 | Links: every Markdown link target in the changed lines is a relative path that exists, or an external URL already present at the base | none broken |
| P-06 | Claims audit on the added lines: no `QA PASS`, `accepted` (other than "accepted final" of PR units), `deployed`, `production-ready`, `drained` or `closed` as a current claim; every drainage mention says pending and carries "as of HDE-EPIC040-PR07"; no enumeration of the governed error pairs and no copy of the 36-row table; no PF version number in durable prose; no link into `docs/ephemeral/` | reviewer-checked list recorded in the result |
| P-07 | Secret and private-data scan of the added lines: no `postgres://` or other URL with credentials, no `Bearer ` value, no `API_KEY=`/`KEY=` value, no UUID other than `<uuid>`-style placeholders, no birth date or time, no fixture content; environment keys by name only | no hit |
| P-08 | `python ci/checks/check_direct_db_contract.py` | exit 0 |
| P-09 | Classifier dry run: `python ci/checks/classify_ci_changes.py --base <full origin/main SHA> --head <full HEAD SHA> --event-name pull_request --github-output <scratch>/gh_out.txt --changed-tests-output <scratch>/changed_tests.txt` | `reason=documentation_only`, `needs_python=false`, every lane `false`, no `CI_CHANGE_SURFACE_UNCLASSIFIED` |
| P-10 | Governed evidence unchanged (read-only): `python tools/evidence/update_evidence_index.py --check`; `python tools/evidence/orientation_demo.py --check`; `python tools/evidence/refresh_step_logs_manifest.py --check`; `python tools/evidence/validate_evidence_paths.py`; `ci/checks/check_mirror_schema.sh`; `ci/checks/check_evidence_index_hash.sh`; `ci/checks/check_final_lf.sh`; `python tools/evidence/run_canonical_json_gate.py --check-only` | every exit 0; `git status` clean |
| P-11 | Diff scope: `git diff --name-only origin/main...HEAD` equals the fifteen §3.4 paths plus the result record; nothing under `schemas/`, `goldens/`, `catalog/`, `engine/`, `adapter/`, `presenter/`, `tools/`, `scripts/`, `tests/`, `artifacts/`, `audit/`, `docs/evidence/`, `docs/pfcanon/`; no existing `docs/ephemeral/` file | exact match |
| P-12 | Formatting: `git diff --check` clean; each changed file ends with exactly one LF and contains no CR; added lines contain no `U+2026` and no three-period ASCII ellipsis; fenced blocks balanced | clean |
| P-13 | Documented behaviour still holds at the head: `python -m pytest -q -p no:cacheprovider tests/http/test_reader_post_v1.py tests/http/test_reader_post_v2.py tests/http/test_endpoint_catalog.py tests/http/test_reader_a7_transport.py tests/reader_v1/test_schema.py tests/reader_v1/test_goldens.py tests/reader_v1/test_emitter.py tests/reader_v1/test_release_pack.py tests/config/test_production_admission.py tests/config/test_config_artifacts.py tests/bodygraph/test_check_magic10_gate_readiness.py tests/scripts/test_cut_release_manifest.py tests/runtime/test_identity.py tests/arch/test_arch_capture_exists.py tests/unit/test_check_direct_db_contract.py` | all pass; `tests/reader_v1/test_cli_proof.py` is not in the roster (pre-existing failure O-P06a-03) |
| P-14 | Documented invocations, executed as written: (a) the README `showcompat` → `/tmp`-style pair file → `aux-preview` pair (use a scratch path outside the repository) → both exit 0; (b) `hdctl aux-preview` with `--band Hot` fails argument validation (confirms "sealed"); (c) `showcompat --dump-reader` bytes equal dev `GET /reader` bytes; (d) start `scripts/dev_start_reader.sh` in the background from the worktree root with `APP_ENV=dev PORT=8000` (or a free port, recorded), run the `docs/RUN.md` curl command, compare with (c), stop the server; (e) Flask test-client probes of F-10, F-11 and F-12 on all three factories, plus `APP_ENV=prod` → 403 `ERR_READER_FORBIDDEN` and unset `APP_ENV` → success; (f) `APP_ENV=dev python -c "import dev.reader_harness.app"` raises `AttributeError`; (g) build a wheel (`python -m pip wheel --no-deps --no-build-isolation -w <scratch>/wheel <worktree>`) and count the absent members (16) | each as documented; if (d) cannot bind a port, apply the §6.7 fallback |
| P-15 | Content-map completeness: for each row of §5.1, quote the added sentence(s) from the head into the result, and confirm each F-fact the sentence relies on | every row covered |

## 9. Ordered implementation procedure (for PR-30, after the Product Owner's Proceed for this version)

One pull request, one documentation commit and one records commit (D-10). Documentation has no intermediate state worth a separate checkpoint. A failing proof stops the procedure at that checkpoint; it is fixed by correcting the documentation, never by changing code, evidence or canon.

### C0 — Preconditions (not implementation)

- The Product Owner's PR-30 Proceed for exactly this plan version.
- Inspect authorized local roots, worktrees, branches, pull requests and `docs/ephemeral/` records for PR07 before creating anything. At planning time none exists except the PR-20 planning branch and its pull request, which carry only this document and are not an implementation vehicle.
- Verify `origin/main`. If it moved beyond `48b0559`, list `git diff --name-only 48b0559 origin/main`; any change outside `docs/ephemeral/` and `docs/pfcanon/` that touches a documented surface (the paths of §3.2) requires re-verifying the affected F-facts before editing. A materially changed fact returns to this session (R-01).
- Confirm the plan is on `main` (merge-order dependency, §15); if not, read it from the planning pull request's head and record that.

### C1 — Environment

As §10.1: a detached worktree of the base outside the repository, a virtualenv with CI's install set, the readiness proof `python -m pytest --version`, and the closed-rails environment with the vendor and database keys absent.

### C2 — Author the edits (§6)

Apply §§6.1–6.15 on the working branch, in this order: contract pages (6.1, 6.2), server page (6.3), README (6.4), configuration and command pages (6.6, 6.7, 6.8), INDEX (6.9), transport pages (6.10, 6.11), additional homes (6.13, 6.14, 6.15), AGENTS (6.12), CHANGELOG (6.5) last, so it describes what landed.

### C3 — Proofs on the working tree

Run P-01 to P-15. Correct the documentation and re-run until every proof passes.

### C4 — Documentation commit and proofs on the committed head

Commit the fifteen paths as one documentation commit. Re-run P-01 to P-15 against the committed head in a fresh detached worktree, including P-09 with full 40-hex SHAs. Every exit status is recorded.

### C5 — Records commit and publication (PR-30's `PR_CANDIDATE_PUBLISHED`)

1. Write `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.0.md`: every proof command with its exit status and result; the diff name list; the content-map quotations (P-15); the claims audit (P-06); the P-14 execution transcript summary; the classifier outputs; the environment (Python version, the free port used); not-executed items with reasons; an *In-flight decisions* section; and the same state distinctions this plan uses. Commit it as the records commit.
2. Push the working branch and open one pull request. Its description follows `.github/pull_request_template.md` and `AGENTS.md` (Why / What changed / Checks run / Not in this PR / What merging does), with §15's merge statement.
3. Hand off to PR-35 in its own dedicated session, naming the `PR_IMPLEMENTATION_RESULT` by repository path and the pull request reference. PR-35 owns review correction, current-head CI, coherent corrective pushes and `MERGE_PENDING`; Nathan merges.

Recovery at any checkpoint: restore the fifteen documentation files together with `git restore` on the branch and restart at C2. Nothing is generated, so nothing else needs restoring.

## 10. Local validation environment and commands

### 10.1 Environment

```
python --version                      # record it; CI would use 3.12, but this PR's CI runs no Python
python -m pip install 'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e <worktree>
python -m pytest --version            # readiness proof (AGENTS.md)
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 PYTHONDONTWRITEBYTECODE=1
unset HD_API_BASE_URL HDAPI_BASE_URL HD_API_KEY GEO_API_KEY DATABASE_URL DEV_SAMPLER_URL GH_TOKEN   # for the whole session
# APP_ENV=dev only for the Reader and dev-route probes of P-14
```

`python` on `PATH` must be the virtualenv interpreter; the editable install must point at the worktree being proven.

### 10.2 Command set

The commands are those of §8, verbatim. P-10's evidence checks are the read-only forms `AGENTS.md` names; no write-producing generator runs.

## 11. Code review and security review checklist

### 11.1 Code review (the PR session, on the current substantive change)

- Every edited line is one §6 names; no other line in the fifteen files changed (`git diff` inspected file by file).
- Every stated fact traces to an F-fact re-verified at the head (P-15), and every command was executed as written (P-03, P-14).
- Examples are byte-equal to goldens and schema-valid (P-04); no example is presented as current release output.
- History is labelled, not rewritten; the corrected lines are exactly the ones §6 corrects; existing `AGENTS.md` rules are untouched.
- PF documents are cited by exact in-document title; PF10 addenda by heading plus register ID; no PF version number, no link into `docs/ephemeral/`, no second canon (P-06).
- Drainage statements are pending and time-bound; no QA, acceptance, deployment, activation, PF09 or closure claim.
- The PR description follows the template and states §15's "What merging does".

### 11.2 Security review (documentation of a public contract and developer operations)

- No secret, credential, connection string, token or unredacted environment value; `DATABASE_URL` and vendor keys appear by name only (P-07).
- No real chart data or personal data; examples are synthetic goldens; fixture paths appear only as command arguments.
- The documentation does not weaken a control: it keeps closed rails as the default, states that the tools refuse outside them, keeps the governed 405s and `no-store` errors, and does not advise disabling a gate.
- The dev `APP_ENV` behaviour is stated truthfully (an unset value is treated as `dev`), not presented as stricter than it is; the posture itself is routed as O-P07-04.
- The documentation claims no protection the implementation lacks (admission limits and writer non-atomicity are stated).
- No live vendor or database action occurs in the procedure; the readiness tool runs only in refusal modes; the Reader probes use the test client or a local helper without a database.

## 12. Risk register and recovery

| ID | Risk | Treatment |
| --- | --- | --- |
| R-01 | A documented fact changes on `main` between planning and PR-30 | C0 diff check; affected F-facts re-verified; a material change returns to this session for a successor plan |
| R-02 | An example drifts from its golden or schema | P-04 byte-equality and validation |
| R-03 | `AGENTS.md` insertion trips the DB-contract scan | no "bridge" wording (§6.12); P-08 |
| R-04 | Over-claiming QA, acceptance, drainage or production state | §5.2 rules 1 and 4; P-06; nonclaim lines |
| R-05 | PF10 renumbering makes addendum citations stale | cite addenda by heading and register ID (§5.2 rule 2; F-27) |
| R-06 | `docs/ephemeral/` pruning breaks links | durable docs never link into it (§5.2 rule 2) |
| R-07 | Green `documentation_only` CI is read as proof of accuracy | §3.5; the result records the local proofs; PR-35 checklist |
| R-08 | A reviewer asks for code fixes (help text, harness, HTML 404, `APP_ENV` default, `aux-preview --band`) | outside PR07; routed to the whole-change IA (§14.2); PR-35 replies with the route and does not push code |
| R-09 | The helper cannot bind a port in the PR-30 environment | free port, recorded; else the §6.7 fallback (drop the curl line, keep the route statement, record it) |
| R-10 | Nested fences in this plan are transcribed wrongly | the outer `~~~~` fences are not content; P-12 checks balanced fences |
| R-11 | The planning PR is unmerged when PR-30 starts | C0 reads the plan from the planning PR's head and records it |
| R-12 | Local Python differs from CI | irrelevant to this PR's CI (no Python runs); the local version is recorded |
| R-13 | OPS01 assumes documentation beyond PR07 | §15: OPS01 verifies the `1.3.0` release on the clean final candidate after PR07 lands; PR07 changes no release byte |

Recovery after landing: revert the documentation commit. No release, evidence or generated artifact depends on these files, so no convergence or re-cut follows.

## 13. Carried `CANON_CONFLICT_REGISTER`, observations and carried items

### 13.1 `CANON_CONFLICT_REGISTER` (carried from Plan v2.1 §11, Plan Review v2.1 §6, PF10 §§2.2–2.5, 2.23, 2.25, 2.26 and the instruction §11; no entry reopened, relabeled, omitted or newly decided here)

| Entry | Classification / status | Decision lineage | PR07 note |
| --- | --- | --- | --- |
| C040-01 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z (PF10 §2.2) | carried |
| C040-02 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried; current controlled PF12 is repository v2.9.5 against the register's recorded v2.9.6 (non-gating, PF12 maintainer) |
| C040-03 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-04 | `CANON_RECONCILIATION` / `APPROVED` | Thoth-17, 2026-09-08T13:23:24Z | carried |
| C040-05 | `CANON_RECONCILIATION` / `APPROVED`, alternative A | Isis-49, 2026-09-09T03:57:16Z (PF10 §2.3) | carried as recorded (PF14 §6.7 correction pending, non-gating); not re-verified here, because PR07 documents nothing that depends on it |
| C040-06 | `NEW_CANON` / `APPROVED`, alternative A | Isis-50, 2026-09-09T11:48:08Z (PF10 §2.5) | documented by pointer (§5.3); drainage to PF12 §2.1 and PF01 §§6.1–6.2 pending (verified, F-20) |
| C040-07 | `NEW_CANON` / `APPROVED` by the Product Owner, 2026-09-26 (PF10 §2.23) | Reader v2; Reader v1 unchanged | delivered by PR06a; documented in §6.1; drainage into PF01, PF04, PF05, PF12 and consequential PF14/PF29 pending (verified, F-20) |
| C040-08 | `CANON_RECONCILIATION` / `APPROVED`, alternative A | the retained whole-change IA by Product Owner direction, 2026-09-26 (PF10 §2.25) | delivered by PR06b; documented in §6.2; drainage into PF01 §2.3 and PF04 §8.1.2 pending (verified, F-20) |

No new register entry is proposed. No observation below is a Canon conflict: each concerns code, packaging, evidence or PF10 page hygiene, not two conflicting canon sources.

### 13.2 Observations — non-gating, decided by no one here

| ID | Observation | Owner and route |
| --- | --- | --- |
| O-P07-01 | The `hdctl --help` summary for `showcompat` reads "Emit canonical Reader v1 bytes from vendor JSON" (`engine/cli/main.py:79`, governed capture `artifacts/cli/help/hdctl_help.txt:8`); stdout is `magic10_compat_result.v1` (F-16). A fix changes a release member (`engine/cli/main.py`), so it needs a re-cut and capture regeneration | code defect: routed to the whole-change IA; CLI / PF05 owner. PR07 labels the gap at the point of use (§6.6) |
| O-P07-02 | `aux-preview --band` is not applied when the band comes from the pair file: `--band Glow` against a `Cool` harmony pair exits 0 with the `Cool` narrative (F-17). The pre-EPIC040 path also read the band from the file | design question: routed to the whole-change IA; CLI / narratives owner. PR07 makes no claim about `--band` beyond "sealed" |
| O-P07-03 | `dev/reader_harness/app.py` raises `AttributeError` at import (F-18); PF02 records the defect; `docs/acceptance/reader_a7_crib.md` and `VERIFY.sh` still name or import it | code defect: routed to the whole-change IA; PF02 architecture / dev-harness owner. PR07 labels it not a start path (§6.3) |
| O-P07-04 | Dev `GET /reader` treats an unset `APP_ENV` as `dev` (F-11), so a deployment that omits `APP_ENV` serves the dev route | security-relevant design question: routed to the whole-change IA; HTTP transport / PF05 owner. PR07 states the behaviour truthfully (§6.3) |
| O-P07-05 | `docs/ADAPTER_009.md` "Readiness rules" (lines 46–52) describe a `compute_pair` smoke for `/internal/readyz`; `compute_pair` exists only in archived trees at `9065e6f` and at `main`, and `adapter/wsgi.py` returns 200 unconditionally; the file's port statements are also stale. Pre-EPIC040; not an EPIC040 surface | HTTP transport / ops owner |
| O-P07-06 | `ARCHITECTURE.md` other stale statements (the `emit_compact_json` return type; the "Routing (dev only)" heading now also covering the production mount) | architecture owner (PF02) |
| O-P07-07 | `VERIFY.sh` imports the non-starting harness and calls `GET /api/reader` | Product Owner / legacy script owner |
| O-P07-08 | PF10 v13.3.7: the addendum index omits §2.26; line 1373 in §2.11 is stored truncated ("persistence remains p"), established by a complete read (F-26) | Nathan (PF10 maintainer) |
| O-P07-09 | `AGENTS.md` cites PF10 by section numbers that now hold other addenda; the cited execution-source rule is not in v13.3.7 (F-27). PR07 preserves `AGENTS.md` rules and does not change them | Nathan (`AGENTS.md` owner) |

### 13.3 Carried observations from accepted units (instruction §8: described, never fixed)

| ID | Where PR07 describes it | Fixed here |
| --- | --- | --- |
| O-P06a-22 (HTML 404 for unknown paths on two factories) | known-limitation lines in §§6.1 and 6.3 | no; HTTP transport / PF05 owner |
| O-12 (wheel omits release members) | README release-identity limitation (§6.4 Edit 4) | no; packaging owner or Product Owner |
| O-P06a-03 (`scripts/hd_cli.py` stub, `test_cli_proof.py` failure) | v1 history note names the stub as not a Reader surface (§6.2) | no; PF10 §2.24 lists its owner as "PR07 / the IA backlog", and the only PR07 share of it is this description, because a fix is code (instruction §8) |
| O-P06a-23 (engine-core currency test does not check `release_id`) | not a documentation surface; recorded in the result only | no; evidence owner |
| O-P06b-17 (Mirror labels of current-release captures) | not a documentation surface; recorded in the result only | no; evidence / updater owner |

## 14. Findings, defects routed to the whole-change IA, decisions and boundary classification

### 14.1 Findings

No `FINDING_REF` is raised. No material boundary (PR-20's definition: outcome/objective, acceptance criteria, protected architectural/security/data-model/external-contract boundary, several units' scope, accepted dependency, budget/schedule/risk) was found. Every required change is documentation within Plan §6.7's owned scope (§14.3). `PR_RETURN_PHASE` does not apply; RS-40 is ineligible.

### 14.2 Code and design defects routed to the whole-change IA

As the Product Owner directed ("Code or design defects found go to the whole-change IA and return to this session"), O-P07-01, O-P07-02, O-P07-03 and O-P07-04 go to the retained whole-change HDE-EPIC040 IA through this plan, and again through the PR07 result and the PR-40 lineage review. None blocks PR07: the documentation states the delivered behaviour truthfully and labels each gap at its point of use, and none needs a change inside PR07's authority. The IA decision on each returns to this dedicated PR07 session. A decision that changes a documented surface before PR07 merges returns here for a successor plan; this version does not anticipate it.

### 14.3 Paths outside the instruction's §6 list, classified

| Path | Why it is in scope and not a finding |
| --- | --- |
| `docs/contracts/reader_v2_public_bytes.md` | the one new file the instruction permits "only if no existing home fits Reader v2"; justified in §6.1 |
| `docs/architecture/emitters.md` | existing documentation within Plan §6.7's owned scope ("existing relevant repository documentation homes"); line 16 became false with C040-07 (instruction §5.3 "wherever they are actually affected") |
| `FLASK_AUTO_RUN_GUIDE.md` | same scope; PR06a changed the documented `adapter/factory.py` mounts |
| `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.0.md` | the PR-30 native result record; adds a record, edits none |

A required change to code, schemas, goldens, catalogs, evidence or `docs/pfcanon/` would be a finding (instruction §6); none is required.

### 14.4 Planning decisions (D-xx) and their boundary classification

| ID | Decision | Classification |
| --- | --- | --- |
| D-01 | One new file, `docs/contracts/reader_v2_public_bytes.md` | in scope: instruction §6 new-file rule, justified |
| D-02 | Examples are byte-exact goldens without the trailing LF, labelled synthetic | in scope: instruction §7 ("examples match the tested schemas"); PF03 §13 |
| D-03 | Route permanent canon by exact title and section; PF10 addenda by heading and register ID; no PF versions; no links into `docs/ephemeral/`; no second canon | in scope: `AGENTS.md`; PF03 §§3, 5; instruction §5.4 |
| D-04 | Drainage statements are time-bound ("as of HDE-EPIC040-PR07") | in scope: instruction §5.4 ("state truthfully") |
| D-05 | The C040-06 pointer names the PF10 addendum and the ADR's artifact ID, and explains the broad grouping in `README.md` | in scope: Plan §6.7 required content |
| D-06 | `README.md` and `docs/INDEX.md` titles move to HDE-EPIC040; EPIC039 sections stay verbatim (F-23) | in scope: current-documentation routing |
| D-07 | `CHANGELOG.md` gains a top entry in the established pattern | in scope: instruction §6 |
| D-08 | `AGENTS.md` changes are additive only: one section and one bullet | in scope: instruction §6 ("only if needed for truthful developer routing; its existing rules must be preserved"); needed because its release-cut rule is incomplete for a version change after EPIC040 |
| D-09 | No generated companion | in scope: F-22; instruction §6 "changed only where their current owner requires it" |
| D-10 | One PR: a documentation commit and a records commit | in scope |
| D-11 | Two additional documentation homes (§14.3) | in scope: Plan §6.7 owned scope |
| D-12 | `ARCHITECTURE.md` changes only at line 11 | in scope: the instruction's condition ("only if it states the core or Reader contract") holds for that line only |
| D-13 | `docs/RUN.md` lines 5 and 10 corrected | in scope: owned locus for Reader invocation and canonical-writer usage; both lines describe live paths wrongly (F-06, F-18) |
| D-14 | `docs/config_and_bundles.md` line 6 and `docs/INDEX.md` line 89 corrected | in scope: they contradict the canonical source ownership PR07 must document (F-07) |
| D-15 | The README `aux-preview` example corrected | in scope: EPIC040 changed the pair-file contract (F-17) |
| D-16 | The help-text gap labelled in `docs/CLI_commands.md`; the code routed to the IA | in scope: PF03 §12 (label gaps at the point of use); the code change is outside PR07 |
| D-17 | Carried observations described where a documented surface meets them (§13.3) | in scope: instruction §8 |
| D-18 | The dev harness named as not a start path, `APP_ENV` default stated | in scope: instruction §5.3; truthful security posture |
| D-19 | The curl example kept only if executed (§6.7 fallback) | in scope: instruction §7 command-existence proof |

No decision rewrites the Plan, mints a Proceed, reruns an accepted unit, edits PF-Canon, decides a Canon conflict or merges.

## 15. Manual merge and post-implementation boundary

- Merge is Nathan's alone. PR-30 ends at `PR_CANDIDATE_PUBLISHED`; PR-35 ends at `MERGE_PENDING — Ready to merge`; PR-40 runs after `MERGE_OBSERVED` (or Nathan's assertion where no such result exists) with the retained IA in its read-only role.
- **What merging does (PR07 implementation PR).** Merging makes the HDE-EPIC040 final repository documentation current on `main`: the Reader v2 contract page, the corrected Reader v1 contract page, the corrected live-path descriptions, the configuration, comparator, readiness and admission documentation, the C040-06/07/08 routing with truthful drainage status, and the `AGENTS.md` EPIC040 posture. It changes no code, schema, golden, catalog, manifest, evidence or PF-Canon byte, so the release (`1.3.0`, `release_id 52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96`) is unchanged. The included `PR_IMPLEMENTATION_RESULT` record is preserved and approves nothing (D21-C). It establishes none of: QA verdict, acceptance, OPS01 attestation, deployment, activation, PF09 movement, C040 drainage, Epic closure. The PR description states this under "What merging does".
- **What merging does (this planning PR).** It carries only this record under `docs/ephemeral/`. Merging preserves the record and approves nothing (D21-C).
- Merge-order dependencies: the planning PR should merge before PR-30 reads this plan from `main` (C0 covers the alternative). PR07 depends on no open code PR. OPS01 follows PR07's merge and verifies the `1.3.0` release on the clean final candidate (Plan §6.8; PF10 §2.25 *Work-unit effects*).

## 16. Prompt-use provenance

`GCFPE_PROMPT_USES`: `GCFPE-USE-HDE-EPIC040-PR-20-20260926-PR07-01`; prior entries carried by reference: `GCFPE-USE-HDE-EPIC040-PR-10-20260926-PR07-01` (instruction §12), `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06b-01` (PR06b review §6), `GCFPE-USE-HDE-EPIC040-PR-40-20260926-PR06a-01` (PR06a review §6).

- Prompt: PR-20 — Create Detailed PR Implementation Plan — 091426.1, `https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204` (page as of 2026-09-24T15:46:52.719Z; Notion read only).
- Release: GCFPE-20260914.1 / 091426.1 / 55 members.
- Change / unit: HDE-EPIC040 / HDE-EPIC040-PR07; Specification v1.1; instruction v1.0.
- Role / stage: dedicated PR07 PR-development session / PR-20.
- Captured: 2026-09-26T19:35Z (planning inspection from approximately 2026-09-26T18:34Z).
- Execution identity: harness session `https://claude.ai/code/session_01UrEaEb4uQkqq2zHD7VTYyc`.
- PF10 read: v13.3.7 (`af292883d5d4f27bd5cc510117e29b044ec2ac0b0f522df48fd0022010c6855c`); handoff-named v13.3.6 superseded by #515 (§2.3).
- Repository persistence: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` absent (the directory holds only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md`); `PENDING / NON_GATING`; owner: the authorized repository writer once a procedure is installed.

## 17. Continuation package

### 17.1 PR-30 package (this version's native next step)

- Receiver: PR-30 — PR Implementation Proceed — 091426.1, `https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204`; the same dedicated PR07 session (`RETAIN_EXISTING`; `invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR07 / PR-30`; `context_conflict: NONE`).
- Gate: Nathan / Product Owner's manual PR-30 Proceed for exactly `HDE-EPIC040-PR07-PR-IMPLEMENTATION-PLAN` v1.0 and `HDE-EPIC040-PR07-PR-INSTRUCTION` v1.0. `AWAITING_PO_PROCEED` is not implementation approval and authorizes no merge, publication, OPS or QA.
- Inputs by repository path: this plan (`docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md`); `docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md`; `docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md` (§6.7); `docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md` (PF10 §2.23); `docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md` (PF10 §2.25); `docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md`; the immutable bases and accepted reviews of §2.1.
- PR-30 obligations carried: inspect before creating (C0); resume the most advanced consistent state; challenge the F-facts and boundary cases at the actual base; implement only §6 in the order of §9; prove locally per §8 with the keys of §10.1 absent; one documentation commit and one records commit; deliberately publish the initial candidate; `PR_CANDIDATE_PUBLISHED`; hand off to PR-35 in its own dedicated session naming the `PR_IMPLEMENTATION_RESULT` and the pull request reference.
- PR-35 obligations carried: review retrieval and correction; local re-proof of any corrected line (the affected P-rows); coherent corrective pushes; CI economy (this PR's CI is `documentation_only`); current-head identity; required checks or a valid waiver; mergeability; genuine merge readiness; a security review on the corrected head where a correction lands; code-fix requests routed to the whole-change IA (R-08); no merge. Nathan merges; PR-40 follows `MERGE_OBSERVED`.

### 17.2 Routes not taken

No RS-10 package is emitted: no material boundary was found (§14.1). No `PR_RETURN_PHASE` or RS-40 applies. PR-50 is Nathan's alone and is not a destination. The IA routing of §14.2 is non-gating and needs no separate handoff before PR-30.

### 17.3 State summary (truthful states)

| Item | State |
| --- | --- |
| This plan | `AWAITING_PO_PROCEED` — complete, executable within approved scope plus PF10 §§2.23 and 2.25 (with §§2.5, 2.7, 2.9, 2.10, 2.12); pending the Product Owner's PR-30 invocation for v1.0 |
| Boundary finding | none raised; four code/design defects routed to the whole-change IA as non-gating (§14.2) |
| PR07 edits, PR, proofs on a real head, CI, reviews, merge | `NOT EXECUTED` |
| PR07 result artifact, OPS01, QA, OPS, activation, C040 drainage, closure | `NOT PRODUCED` / `NOT EXECUTED` |
| Delivered-state facts | verified at `48b0559` in a scratch worktree (§3.3); inference support, not PR evidence |
| Provenance persistence | `PENDING / NON_GATING` |
