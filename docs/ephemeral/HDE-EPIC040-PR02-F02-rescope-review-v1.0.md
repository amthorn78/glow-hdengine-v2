---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-EPIC040-PR02-F02-RESCOPE-REVIEW
artifact_version: 1.0
status: APPROVED_PENDING_MANUAL_PF10_DRAIN
decision: APPROVE
reviewed_artifact_type: RESCOPE_REQUEST
reviewed_artifact_id: HDE-EPIC040-PR02-F02-RESCOPE-REQUEST
reviewed_artifact_version: 1.0
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
finding_ref: HDE-EPIC040-PR02-F02
originating_stage: RS-40 continuation of proceeded PR-30
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent session
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR02 / RS-20 / F02 RESCOPE_REQUEST v1.0 / PR404
context_conflict: NONE
ecosystem_release: GCFPE-20260913.1
prompt_id: RS-20
prompt_version: 091326.2
selected_membership_count: 54
created_at_utc: 2026-09-13T17:58:38Z
---

# HDE-EPIC040-PR02 — F02 Bounded Work-Unit Rescope Review v1.0

## 1. Decision

**APPROVE.** `HDE-EPIC040-PR02-F02-RESCOPE-REQUEST` v1.0 is an evidence-supported bounded implementation rescope within the approved HDE-EPIC040 Specification intent.

The approved delta is limited to:

- a fail-closed executable-code-equivalence predicate for exactly four first-party admission modules;
- manifest-bound capture of exactly two existing helper-source owners;
- an effective synthetic complete-release roster of 44, building on the already approved and drained F01 roster of 42; and
- the explicit positive/adverse evidence, dependency effects, exclusions, and claim limits recorded below.

This decision does not approve an implementation, the preserved local attempt, an unspecified broader runtime-integrity mechanism, a deployment protocol, historical imported-source byte identity, merge readiness, or any action outside RS-20. The existing PR02 engineer must implement and prove the bounded delta after its PF10 prerequisite is satisfied.

State: `APPROVED_PENDING_MANUAL_PF10_DRAIN`.

## 2. Exact identity, authority, and lifecycle

| Field | Reviewed value |
| --- | --- |
| Reviewer | Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent session; the same IA that issued F01 review v2.0 |
| Independent approved-Plan reviewer | Isis-50; distinct from this receiving IA |
| Request | `HDE-EPIC040-PR02-F02-RESCOPE-REQUEST` v1.0 / `RESCOPE_PENDING` |
| Change / work unit | `HDE-EPIC040` / `HDE-EPIC040-PR02` |
| Originating stage | RS-40 continuation of the proceeded PR-30 implementation |
| Suspended boundary | PR02 engineering completion and merge readiness |
| Continuing engineer | `PR-02 HDE-EPIC040` |
| Repository / PR | `amthorn78/glow-hdengine-v2` / open draft PR #404 |
| Branch | `hde-epic040-pr02-immutable-admission` → `main` |
| Accepted base | `3828d4b3454259841a3e48d13039dd1475754f2f` |
| Recorded head | `eed8a63807f573abc29de6f6d5ceac54f0c8da85` |
| Recorded head tree | `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d` |
| Current connected PR observation | Open, draft, unmerged; same branch/base/head; 9 changed files; 1,305 additions / 27 deletions; 2 commits |
| Original Proceed | Preserved and valid; no new Proceed is required or created |
| PR01 | Merged PR #403 accepted and final; not reopened or rerun |

The current GitHub read confirms PR #404 remains open, draft, unmerged, and at `eed8a63807f573abc29de6f6d5ceac54f0c8da85` on the recorded branch. All seven review threads remain unresolved. No repository mutation, review disposition, commit, push, CI run, merge, or thread resolution occurred in this review.

## 3. Complete source verification

The following complete Markdown artifacts were read from their exact supplied Drive locations. Their fetched bytes matched the supplied hashes where a hash was provided.

| Source | Exact verified identity |
| --- | --- |
| F02 request | `HDE-EPIC040-PR02-F02-RESCOPE-REQUEST` v1.0; SHA-256 `cbfe94dd0530a6dbc052de5e9c9e67ddce8f1a878a9d16d1726cd53234d11b38`; https://drive.google.com/file/d/1nlCOzR3y9QvyynxFIFt9KU6U3urdUpCW/view?usp=drivesdk |
| Resumed Result | `HDE-EPIC040-PR02-PR-IMPLEMENTATION-RESULT` v2.0; SHA-256 `33061285197b364a85d742a8faab36e839233df149be3859956d2d42bf06ebd2`; https://drive.google.com/file/d/16uYvir9dGnz8rp8fzoj1v_y67cQ_Wyc1/view?usp=drivesdk |
| Approved F01 review | `HDE-EPIC040-PR02-rescope-review-v2.0.md`; SHA-256 `86509f67869c0a95e8b9e1035dc0dbebe4ca19f9d3ea8005127426bed075ffc8`; https://drive.google.com/file/d/1rNSVietXHUCA8OG2xUWHeOHcQbFsUmKK/view?usp=drivesdk |
| Approved F01 addendum | `HDE-EPIC040-PR02-PF10-build-notes-addendum-v2.0.md`; SHA-256 `5ecc9850dc9f4368868ad1e4de15e249193e2bb81421e41095e4aed686c2874d`; https://drive.google.com/file/d/17-TV-9KeP0c0KmHuhogik_uyYXyBqNPV/view?usp=drivesdk |
| Current PF10 | `PF10-HDE-Build-Notes-v13.2.1.md`; SHA-256 `5c0f6f96a52b8821cb7826d492b0066322bf5eb12b48eff5b390eee002e5a7c9`; https://drive.google.com/file/d/1zCDNwfUjs9sqVZWK-nY2rGFmnpMg4RF1/view?usp=drivesdk |
| Original F01 proposal | `HDE-EPIC040-PR02-rescope-proposal-v1.0.md`; https://drive.google.com/file/d/1nbkt7F4td7keMifg582PFiscWna5oRkH/view?usp=drivesdk |
| Approved Specification | `HDE-EPIC040-specification-v1.1-approved.md`; SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df`; Thoth-17 `APPROVE`, 2026-09-08T13:23:24Z; https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk |
| Immutable Plan | `HDE-EPIC040-implementation-plan-v2.1.md`; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`; https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk |
| Plan approval | `HDE-EPIC040-implementation-plan-review-v2.1.md`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3`; Isis-50 `APPROVE`, 2026-09-09T13:36:43Z; https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk |
| PR02 Instruction | `HDE-EPIC040-PR02-pr-instruction-v1.0.md`; SHA-256 `429cda8e7f00bedc0509e9d00a16c72b37a49f5592054b2b8e069308e812047c`; https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk |
| PR02 detailed Plan | `HDE-EPIC040-PR02-pr-implementation-plan-v1.0.md`; SHA-256 `496488109e3fc080dd238145f28edf0a0824b5bb1ff068432e209813df9998e0`; original Proceed preserved; https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk |
| Original PR02 Result | `HDE-EPIC040-PR02-pr-implementation-result-v1.0.md`; SHA-256 `779c425ba72c7df142f7ba1806ad1489785eb90de46493dac408e31bf53004e0`; https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk |
| Operating procedure | `GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v3.1.0-20260913.md`; SHA-256 `c62dde03425b09e1b8bc51b6cc5d870392075e8a0e0cd21ad961c7ecdc6d8e7c`; https://drive.google.com/file/d/1KvX86E4yP4sGHC17tlcfCPRNavnhckEm/view?usp=drivesdk |

The selected RS-20 page was fetched from `AI Prompts / HDE IA`: `RS-20 — Review Bounded Work-Unit Rescope — 091326.2`, GCFPE-20260913.1, last edited 2026-09-13T11:33:42.699Z. The supplied selected register binds exactly 54 members.

## 4. Evidence-supported cause

The current published loader derives a fixed lexical repository root and captures current disk sources, but Python may already be executing cached module code imported before those disk sources changed. The remote head therefore can admit a manifest representing source B while executing previously imported source A.

The preserved local attempt does not close that gap. Its import-time disk hash can also record B while timestamp-valid cached bytecode still executes A. The F02 request's adverse experiment demonstrates a behaviorally material A/B mismatch: cached A accepts the B source/manifest identity while fresh B on the same disk inputs refuses.

The admission path already executes two unrostered first-party owners through its rostered modules:

- `engine/serializer/canon.py` delegates canonical serialization to `engine/stable/sercanon.py`;
- `engine/config/registry_loader.py` imports `FROZEN_MAGIC10_ORDER` from `engine/categories/registry.py`.

Inspecting or validating those helper sources outside the manifest would create unbound source authority. Copying their behavior into the loader would create competing owners. The smallest coherent source/execution closure therefore includes those exact two helper sources and no others.

## 5. Scope classification and rationale

Classification: `BOUNDED_WORK_UNIT_RESCOPE_WITHIN_APPROVED_SPECIFICATION_INTENT`.

The approved Specification requires one coherent deterministic release-bound mechanics configuration, exact source identities, immutable configuration/release identity, fail-closed loading, and no competing authority. Whole-change Plan §5.5 requires one root, authoritative captured bytes, actual validation of those captured bytes, rejection of inconsistent capture, exact member identities, and no fallback. The detailed PR02 Plan §§5.1–5.5 assign the exact capture/admission/identity closure to PR02 and require every active release member to be captured and manifest-bound before a bundle is returned.

F02 changes no product objective, public promise, selected/excluded unit, mathematical rule, schema shape, API/CLI surface, identity formula, release version, or dependency order. It specifies how PR02 must close an implementation/source coherence gap inside its existing admission responsibility. The two added members are existing first-party owners already executed by that path, not new product functionality.

The proposed retained-code/compiled-captured-source comparison is eligible for approval because it checks the actual already executing top-level module code without executing captured source, reloading modules, changing selection, or adding deployment/concurrency authority. Its feasibility probe supports the mechanism category, while the approval expressly leaves implementation correctness, safe origin, interpreter compatibility, error behavior, complete tests, and independent review to the PR02 engineering lifecycle.

This approval is for executable-code equivalence only. It does not claim the exact historical raw bytes originally consumed by the interpreter. Requiring that stronger fact would be a different trust boundary and is not silently absorbed into this decision.

## 6. Approved bounded delta

The approved overlay is the exact delta stated in the associated PF10 addendum:

1. Compare retained actual top-level execution code objects with compilation of exact captured, manifest-bound source for exactly:
   - `engine/config/registry_loader.py`;
   - `engine/serializer/canon.py`;
   - `engine/stable/sercanon.py`; and
   - `engine/categories/registry.py`.
2. Add exactly `engine/stable/sercanon.py` and `engine/categories/registry.py` to the already effective F01 42-member roster. The synthetic complete roster becomes 44.
3. Preserve the actual shared serializer and category registry. Remove or replace the unapproved duplicate serializer, copied category order, and import-time disk-hash approach during the coherent correction.
4. Bind both added sources through the existing root, capture, canonical-path, byte, hash, size, member-format, manifest, and unchanged-source checks.
5. Fail closed on missing or unsafe module origin, missing/unusable execution provenance, missing captured source, incompatible compilation semantics, or code mismatch. Do not accept caller-supplied module identities, unmanifested sources, disk-hash guesses, timestamp caches, fallbacks, or prior handles.
6. Preserve all existing configuration/source/manifest/release identities and the exact manifest-byte release rule.
7. Keep the actual 15-member manifest unchanged in PR02. PR06 retains final materialization and promotion of the effective 44-member release.

No broader source-execution or deployment guarantee is approved.

## 7. Requirement, acceptance, and dependency effects

| Contract | Approved effect |
| --- | --- |
| `K040-REQ-006` | The active bundle's manifest-bound source closure includes the four executed first-party admission modules and no unbound implementation authority. |
| `K040-REQ-007` | PR02 verifies executable equivalence of those modules to their captured sources before returning the strict immutable bundle. |
| `K040-REQ-008` | Stale bytecode, replaced source, missing/unusable provenance, source mismatch, helper-member omission, and unsafe origin receive fail-closed adverse proof. |
| `K040-REQ-009` | Executable equivalence remains distinct from exact source, config, manifest, and release identities. |
| `AC040-04` | PR02 admission/schema execution evidence adds four-module source/execution-coherence proof over the 44-member synthetic release. |
| `AC040-05` | PR02 proves its source/execution identity contribution; PR06 retains complete actual manifest/release identity. |

All requirement text remains unchanged. `K040-REQ-011` continues to require complete adverse evidence and `K040-REQ-012` continues to require the actual owning test/classifier lanes; neither is reworded or reassigned.

PR03–PR05 retain their approved scope and dependency order. They consume only an accepted PR02 boundary and use the effective roster in future complete fixtures. PR06's final roster becomes 44 and it retains sole ownership of actual manifest materialization, exact identity recomputation, convergence, and promotion. PR07 later documents the delivered boundary and limits. OPS01 remains separately authorized final external verification. No unit is created, removed, split, advanced, or rerun.

## 8. Required proof and completion boundary

Approval does not convert the F02 experiment or preserved local files into completed implementation. The PR02 engineer must establish:

- exact 44-member synthetic success and refusal of 42-, 43-, and unapproved 45-member sets;
- missing, malformed, changed, wrong-hash, wrong-size, unsafe-path, and unbound tests for both added helper members;
- matching success and behaviorally material mismatch refusal for all four covered modules;
- stale timestamp-valid bytecode A against source/manifest B refusal, with fresh B separately demonstrated;
- fail-closed behavior for unavailable/unsafe provenance and incompatible compilation semantics;
- continued use of the shared serializer/category owners and removal of duplicate implementations;
- preserved F01 schema execution, source identity, recursive freezing, one packaged-manifest read, no stale fallback, and ordinary source-change checks;
- targeted, regression, nine governed writer/evidence, changed-path ownership/classification, and clean-worktree local success;
- substantive code and security review of the exact corrected head; and
- one final CI run on the exact final candidate only after local validation and review blockers are resolved.

The historical 472 targeted passes, 1,724 regression passes with three existing closed-rails vendor skips, nine writer/evidence checks, security no-findings comment, and seven-lane CI run 34715034846 remain evidence only for `eed8a638…`. They do not prove the uncommitted recovery delta or a future corrected head.

## 9. Separate findings and owners

| Finding | RS-20 classification and owner |
| --- | --- |
| `3997320377` / `3997320916` | F01 authority already approved and drained. The PR02 engineer owns completed schema implementation and proof; repository reviewer owns final thread disposition. |
| `3997320380` | Existing bounded symlink correction remains preserved. Final current-head disposition belongs to the repository review owner. |
| `3997320917` | Existing bounded inter-read correction remains preserved. It does not create atomic visibility. Engineer/reviewer own corrected-head proof and disposition. |
| `3997351895` | `IN_SCOPE_REPAIR`. The PR02 engineer owns one physical packaged-manifest read and its adverse proof in the coherent repair batch. |
| `3997351898` / F02 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVE` within the exact four-module, two-helper, 44-member, executable-equivalence limits in this review. |
| `3997351903` | `CONFLICTS_WITH_EXPLICIT_APPROVED_LIMITATION`. The residual window remains disclosed; no atomicity, locking, immutable-deployment, or portability expansion is approved. Repository reviewer retains final thread disposition. |
| Security comment `5648272341` | Historical exact-head evidence only. Changed code receives applicable current-head security review. |

All seven threads remain unresolved in the current connected GitHub record. This review does not resolve, waive, dismiss, or mark any thread false-positive.

## 10. Preserved exclusions and nonclaims

The approval creates no authority for:

- exact historical imported-source byte proof or universal runtime integrity;
- source execution, imports/reloads, import hooks, `sys.modules` mutation, a new selector, or caller-controlled module identity;
- an unmanifested source, duplicate serializer, copied category authority, second validator, alternate calculator, or fallback;
- process-death atomicity, multi-file atomic visibility, cross-process locking, immutable-deployment infrastructure, or a deployment protocol;
- public/API/CLI fields, product-objective or Specification changes, mathematics, schemas, identity formulas, release activation, or scope beyond the four modules;
- actual 15-member manifest mutation in PR02 or PR06's final materialization work;
- a replacement Plan, Plan review, PR instruction, detailed PR Plan, Proceed, branch, PR, or engineering session;
- PR01 reopening or rerun;
- implementation, commit, push, CI, thread resolution, merge, PF10 mutation, QA, Ops, vendor/database access, deployment, release activation, or Epic closure by this RS-20 review.

The detailed Plan §12 limitation on process-death atomicity, multi-file atomic visibility, and cross-process locking remains controlling.

## 11. Recovery and repository continuity

PR #404 remains the same open draft PR on `hde-epic040-pr02-immutable-admission`. The accepted base, ordered commits, head, and recorded tree remain distinct from the preserved uncommitted recovery delta.

The recorded recovery directory `/workspace/scratch/b736cdb96988/pr02-recovery` currently lacks Git metadata and many repository files. Its four-file delta is fully carried by the F02 request. Engineering recovery restores the missing checkout structure and Git metadata around that preserved delta in the same recorded directory before mutation; it does not discard, overwrite, or relabel the preserved work. The inaccessible earlier workspace remains unchanged.

The import-time disk-hash, duplicate serializer, and copied category order remain historical unapproved attempt content. Their preservation is evidence, not implementation acceptance. The engineer batches F01, F02, and ordinary in-scope corrections coherently, validates locally, obtains substantive re-review, and then runs final-candidate CI once.

## 12. PF10 addendum and form conflict

Exactly one qualifying `PF10_BUILD_NOTES_ADDENDUM` was created for this approval, uploaded to `Glow / Ephemeral Planning Files`, and read back byte-for-byte: [HDE-EPIC040-PR02-F02-PF10-build-notes-addendum-v1.0.md](https://drive.google.com/file/d/1I1O6_r4FVrE29m902lUqndR9uMXBiove/view?usp=drivesdk), SHA-256 `1c952386cd84eaf8a8aefbb33054b6a902d49ea73aa6f68239f099ad700a25fd`.

An actual governance-form conflict is preserved:

- selected RS-20 091326.2 requires the standalone transport artifact to state `status: READY_FOR_MANUAL_DRAIN`, `canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN`, and `drain_owner: Nathan / Product Owner`, and it requires Nathan's verified manual drain before RS-40 may rely on the delta;
- current PF10 §2.8 says an agent-authored addendum is page-ready, uses the next continuous H2 number, contains subject-matter authority only, contains no role-addressed publication/routing language, and is canonical in form at creation.

This run does not repair prompt policy or edit PF10. The single standalone file preserves the RS-20-required transport fields in a YAML artifact envelope and places the complete subject-matter content under the sole page-ready H2 heading `2.9 HDE-EPIC040-PR02-F02 — Executing-Code Coherence Rescope`. Its subordinate headings are H3, and its body contains no role-addressed publication or routing instructions. Nathan's manual insertion should use the H2 body, not the transport envelope. The conflict remains recorded for GCFPE management; it does not change the bounded technical decision or authorize affected implementation before the selected manual-drain prerequisite is verified.

## 13. Canon-conflict register

| ID | Preserved decision/current treatment |
| --- | --- |
| C040-01 | `CANON_RECONCILIATION / APPROVED` by Thoth-17, 2026-09-08T13:23:24Z; PF10 §§2.2/2.4 retained. |
| C040-02 | Same approved Thoth-17 decision; PF12 identity history and PF10 §§2.2/2.4 retained. |
| C040-03 | Same approved Thoth-17 decision; PF14 identity history and PF10 §§2.2/2.4 retained. |
| C040-04 | Same approved Thoth-17 decision; PF19 identity history and PF10 §§2.2/2.4 retained. |
| C040-05 | `CANON_RECONCILIATION / APPROVED`, alternative A, by Isis-49, 2026-09-09T03:57:16Z; PF10 §2.3 retained. |
| C040-06 | `NEW_CANON / APPROVED`, alternative A, by Isis-50, 2026-09-09T11:48:08Z; PF10 §2.5 retained. |
| HDE-EPIC040-PR02-F01 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED`; PF10 §2.7 is effective only for the manifest-bound owning Gate schema and member-42 correction. |
| HDE-EPIC040-PR02-F02 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVE` in this review; exact four-module executable equivalence, two added helper-source owners, and effective 44-member synthetic roster only; manual PF10 prerequisite pending. |

No decided item is reopened, reinterpreted, relabeled, or duplicated. No new product-objective, Specification, or permanent-Canon decision is created.

## 14. Native return and next state

The only conditional continuation is `RS-40 — Approved Rescope — Resume PR Implementation — 091326.2` in the same `PR-02 HDE-EPIC040` engineering session, using the same recorded recovery directory, branch, open draft PR #404, and original Proceed. Nathan's manual PF10 drain and verification of the exact §2.9 subject-matter body is a prerequisite. This approval is not itself implementation or merge authority.

Until that prerequisite is verified:

- HDE-EPIC040 remains `ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION`;
- HDE-EPIC040-PR02 remains `APPROVED_PENDING_MANUAL_PF10_DRAIN` at the rescope boundary;
- PR #404 remains open, draft, unmerged, and not ready to merge; and
- no affected implementation, review completion, CI, merge, QA, Ops, deployment, release, PF10 mutation, or closure is authorized.

## 15. Prompt-use record

| Field | Value |
| --- | --- |
| Usage ID | `GCFPE-USE-HDE-EPIC040-PR02-RS20-F02-20260913-01` |
| Change / work unit | `HDE-EPIC040` / `HDE-EPIC040-PR02` |
| Ecosystem / prompt | `GCFPE-20260913.1` / RS-20 091326.2 |
| Prompt source | https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204 |
| Retrieved page revision | 2026-09-13T11:33:42.699Z |
| Role/stage | continuing whole-change IA / F02 bounded-rescope review |
| Capture | 2026-09-13T17:58:38Z |
| Result | `APPROVE`; one F02 review and exactly one qualifying PF10 addendum; no downstream execution |
| Repository prompt-use persistence | Not attempted by this read-only review; remains non-gating for the next authorized repository writer under an actually installed supported procedure |

ASK OK.
