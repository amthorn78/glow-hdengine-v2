---
artifact_type: RESCOPE_REVIEW
artifact_id: HDE-EPIC040-PR02-RESCOPE-REVIEW
artifact_version: 2.0
status: RESCOPE_APPROVED_PENDING_MANUAL_PF10_DRAIN
decision: APPROVE
decision_scope: HDE-EPIC040-PR02-F01_ONLY
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
originating_stage: PR-30
suspended_boundary: PR02 engineering completion and merge readiness
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent session
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR02 / RS-20 / original rescope proposal v1.0 / HDE-EPIC040-PR02-F01
context_conflict: NONE
ecosystem_release: GCFPE-20260913.1
prompt_version: 091326.2
created_at_utc: 2026-09-13T13:33:56Z
next_state: MANUAL_PF10_DRAIN_REQUIRED
conditional_post_drain_prompt: RS-40 — Approved Rescope — Resume PR Implementation — 091326.2
---

# HDE-EPIC040-PR02 — Bounded Work-Unit Rescope Review v2.0

## 1. Native decision

`APPROVE` the bounded rescope `HDE-EPIC040-PR02-F01` only.

The exact 41-path PR02 admission roster cannot satisfy the already-approved requirement to execute the Gate Catalog's actual owning schema from the same captured, manifest-bound release, because `schemas/gates_v1.schema.json` is absent from that roster. Adding the schema as required member 42 and executing its existing owning validator is the smallest complete correction within the approved HDE-EPIC040 Specification intent.

This decision does not approve the separate executing-module/source-coherence proposal, expand the explicit atomicity boundary, or convert ordinary PR02 repairs into rescope. It does not rewrite the approved Plan, create a new Plan, rerun an accepted PR, issue a new instruction or Proceed, authorize implementation before PF10 drainage, merge PR #404, or perform QA, Ops, release, production, or Canon mutation.

The approved whole-change Plan v2.1 remains the immutable base. The approved delta is represented by exactly one standalone PF10 addendum overlay. Nathan / Product Owner must drain and verify that addendum before the existing PR02 engineering session may resume through RS-40 under the original Proceed.

## 2. Exact reviewed lineage

| Role | Exact identity and source |
|---|---|
| Selected RS-20 | `RS-20 — Review Bounded Work-Unit Rescope — 091326.2`, `GCFPE-20260913.1`: https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204 |
| Reviewed proposal | `HDE-EPIC040-PR02-rescope-proposal-v1.0.md`; original pending request: https://drive.google.com/file/d/1nbkt7F4td7keMifg582PFiscWna5oRkH/view?usp=drivesdk |
| Approved Specification | `HDE-EPIC040-specification-v1.1-approved.md`; Thoth-17 `APPROVE`, 2026-09-08T13:23:24Z; SHA-256 `43e1b18282233e87916058e59c1950f8fbb0379ee7a7e6ecdcd73e114341e9df`: https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk |
| Immutable base Plan | `HDE-EPIC040-implementation-plan-v2.1.md`; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`: https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk |
| Exact base approval | `HDE-EPIC040-implementation-plan-review-v2.1.md`; Isis-50 `APPROVE`, 2026-09-09T13:36:43Z; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3`: https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk |
| Current PF10 | `PF10-HDE-Build-Notes-v13.1.8.md`; applicable Addenda 2.2–2.6; SHA-256 `75772772077ff0aad90131153b833673dab6f2bc760e97672a897863248d19a8`: https://drive.google.com/file/d/1Qm-oszL0JfPt0TzVfQsws4hjGb9n83e6/view?usp=drivesdk |
| PR02 instruction | `HDE-EPIC040-PR02-pr-instruction-v1.0.md`; `INSTRUCTION_READY`; SHA-256 `429cda8e7f00bedc0509e9d00a16c72b37a49f5592054b2b8e069308e812047c`: https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk |
| PR02 detailed Plan | `HDE-EPIC040-PR02-pr-implementation-plan-v1.0.md`; original state `AWAITING_PO_PROCEED`; SHA-256 `496488109e3fc080dd238145f28edf0a0824b5bb1ff068432e209813df9998e0`: https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk |
| PR02 implementation Result | `HDE-EPIC040-PR02-pr-implementation-result-v1.0.md`; `RESCOPE_PENDING`; preserves the actual Product Owner `PROCEED`; SHA-256 `779c425ba72c7df142f7ba1806ad1489785eb90de46493dac408e31bf53004e0`: https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk |
| Governing procedure | `GCFPE-Direct-Handoff-and-Runtime-Artifact-Operating-Procedure-v3.1.0-20260913.md`; SHA-256 `c62dde03425b09e1b8bc51b6cc5d870392075e8a0e0cd21ad961c7ecdc6d8e7c`: https://drive.google.com/file/d/1KvX86E4yP4sGHC17tlcfCPRNavnhckEm/view?usp=drivesdk |
| Promotion record | `GCFPE-20260913.1-Promotion-and-Archival-Report-v3.0.md`; selected release `091326.2`, exactly 54 members: https://drive.google.com/file/d/1eyD8ctHYZBetlVZCKRK8uKxepqhGop20/view?usp=drivesdk |
| Required addendum | `HDE-EPIC040-PR02-PF10-build-notes-addendum-v2.0.md`; `READY_FOR_MANUAL_DRAIN`; read-back direct link: https://drive.google.com/file/d/17-TV-9KeP0c0KmHuhogik_uyYXyBqNPV/view?usp=drivesdk |

The previous RS-20 review and its PF10 addendum were rejected by the Product Owner and are historical/nonoperative. They were not used as approval evidence. No approved PR02 rescope addendum exists in current PF10 v13.1.8.

## 3. Identity, lifecycle, and repository state

| Field | Verified value |
|---|---|
| Reviewing actor | Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent; Isis-50 remains the independent approved-Plan reviewer and is not this receiving IA |
| Continuing engineering owner | Dedicated PR02 engineering session called `PR-02 HDE-EPIC040` |
| Repository | `amthorn78/glow-hdengine-v2` |
| Pull request | PR #404, https://github.com/amthorn78/glow-hdengine-v2/pull/404 |
| Live state checked during this review | Open, draft, unmerged, mergeable; 9 changed files, 1,305 additions, 27 deletions |
| Branch | `hde-epic040-pr02-immutable-admission` → `main` |
| Accepted base | `3828d4b3454259841a3e48d13039dd1475754f2f` |
| Current verified head | `eed8a63807f573abc29de6f6d5ceac54f0c8da85` |
| Current corrected tree | `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d` |
| Ordered attributable commits | `3dda87853466fa18247654ffe5bb67561364b0f4` → `eed8a63807f573abc29de6f6d5ceac54f0c8da85` |
| Attributable recovery workspace/worktree | Recorded as `/workspace/scratch/b736cdb96988/pr02-recovery`; must be recovered and verified by the continuing PR02 session before mutation |
| Preserved original workspace | `/workspace/scratch/8d666e9ba95b/glow-hdengine-v2`; preserve unchanged; it is not the attributable publication base |
| Current release manifest | Actual 15-member manifest remains unchanged; current incomplete release refuses with `INCOMPLETE_RELEASE_ROSTER` |
| Original authority | Original Product Owner `PROCEED` for PR02 detailed Plan v1.0 remains valid for the same PR after verified drainage; no replacement Proceed exists or is needed |
| PR01 | PR #403 is accepted and final; it is not reopened or rerun |

HDE-EPIC040 transitions from the general `ALPHA_STOPPED_PENDING_GOVERNANCE_CORRECTION` checkpoint to `ALPHA_STOPPED_PENDING_MANUAL_PF10_DRAIN`. PR02 remains suspended until the exact addendum is manually drained and verified.

## 4. Evidence-supported cause

The collision is real and bounded:

1. The detailed PR02 Plan v1.0 fixes the admission roster at exactly 41 paths, rejects missing and extra members, and limits local schema resolution to captured roster-authorized sources.
2. The 41 paths omit `schemas/gates_v1.schema.json`.
3. PR02 Instruction v1.0 requires actual local closed schemas and prohibits an alternate validator.
4. Whole-change Plan v2.1 requires actual owning schemas, same-root capture, exact manifest-bound admission, and execution of schema plus relational closure before an active bundle is returned.
5. Current PF10 Addenda 2.2–2.6 preserve the approved Plan, C040 decisions, and accepted PR01 but contain no PR02 rescope overlay.
6. The implementation at recorded head calls `_load_gates(capture, validate_schema=False)`, so handwritten Gate checks execute without the owning Gate schema.
7. Read-only probes established that an otherwise exact 41-member synthetic release can be admitted while the Gate schema is absent; the existing schema-enabled validator rejects the missing schema with `MISSING_FILE`; a canonical reject-all replacement is ignored by the current pipeline while the schema-enabled route rejects it with `SCHEMA_VALIDATION_FAILED`; and adding it as member 42 currently fails with `RELEASE_ROSTER_MISMATCH`.

The actual 15-member release remains incomplete and refused. Synthetic fixtures establish the contract collision; they do not establish production conformance or release promotion.

## 5. Approved bounded delta

The effective overlay consists of all and only these connected changes:

1. Add `schemas/gates_v1.schema.json` as required captured admission member 42.
2. Bind that schema to the same selected repository root and manifest as `catalog/gates_v1.json`; validate its exact path, bytes, hash, size, canonical form, and local reference closure through the existing admission capture.
3. Execute the existing owning Gate schema validator before returning an active immutable bundle, followed by the approved shared relational checks. Handwritten checks cannot substitute for the owning schema.
4. Refuse missing, unlisted, invalid, malformed, noncanonical, hash/size-mismatched, source-changed, schema-rejecting, or extra schema/member inputs with the owning typed failure and no partial handle or stale fallback.
5. Update synthetic complete-release fixtures and roster tests from 41 to 42, and add adverse proof for absent, invalid, reject-all, changed, unbound, missing-member, and extra-member cases.
6. Keep the actual current 15-member manifest unchanged in PR02. PR06 later owns actual complete-manifest materialization, release identity recomputation, admission convergence, and promotion of the 42-member roster.

The delta is within approved Specification intent. It makes the already-required owning-schema and manifest-bound admission obligations simultaneously executable. It changes no product objective, requirement text, exclusion, public/API/CLI shape, math, taxonomy, numeric behavior, identity formula, release activation, QA/Ops authority, or unit order.

The immutable whole-change Plan v2.1 and approving Review v2.1 do not change. The approved overlay is carried solely by this decision and the one PF10 addendum after manual drainage.

## 6. Requirement, acceptance, and dependency effects

| Requirement | Approved effect; text unchanged |
|---|---|
| `K040-REQ-003` | Gate Catalog conformance must be enforced by its actual owning schema. |
| `K040-REQ-006` | The immutable manifest-bound source set includes the Gate owning schema. |
| `K040-REQ-007` | The schema-loaded admission path executes the owning schema before producing an immutable bundle. |
| `K040-REQ-008` | Missing, extra, invalid, changed, or unbound Gate schema inputs fail closed. |
| `AC040-04` | PR02 evidence must prove actual owning-schema execution and immutable admission against an exact 42-member synthetic complete release. |
| `AC040-07` | The existing shared Gate normalization remains strict; schema bypass cannot count as successful validation. |

All other `K040-REQ-*` and `AC040-*` requirements retain their approved wording, owners, and burdens. `K040-REQ-009` and `AC040-05` source/release identity duties remain applicable but are not expanded by this F01 approval.

| Unit | Dependency effect |
|---|---|
| PR01 | Accepted/final; no effect and no rerun. |
| PR02 | Same open PR resumes after drain to implement the overlay and complete authorized in-scope repairs. |
| PR03 | Still not executed; still waits for accepted PR02; mechanics scope unchanged. |
| PR04 | Still not executed; still waits for PR01–PR03; application scope unchanged. |
| PR05 | Still not executed; still waits for PR01–PR04; future complete fixtures use the effective roster. |
| PR06 | Still owns final manifest materialization and release/evidence convergence; effective complete roster becomes 42. |
| PR07 | Later documentation records the delivered 42-member contract and preserved limitations. |
| OPS01 | Later separately authorized final-candidate verification uses the actual final manifest identity; purpose unchanged. |

The dependency sequence remains PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01.

## 7. Finding-by-finding authority classification

| Finding/evidence | RS-20 classification and owner |
|---|---|
| `HDE-EPIC040-PR02-F01`; threads `3997320377` and `3997320916` | `APPROVE / BOUNDED_WORK_UNIT_RESCOPE_WITHIN_APPROVED_SPECIFICATION`. The manifest-bound member-42/owning-schema delta is approved pending PF10 drain. Implementation and proof return to the same PR02 engineer through RS-40 after drain. |
| Deployment-symlink defect; thread `3997320380` | `IN_SCOPE_REPAIR_COMPLETED_PENDING_FINAL_CURRENT_HEAD_REVIEW`. Preserve the correction already present at `eed8a638…`; the original thread is outdated but unresolved. Repository review owner controls final thread disposition. |
| Earlier-source inter-read mutation; thread `3997320917` | `IN_SCOPE_REPAIR_COMPLETED_PENDING_FINAL_CURRENT_HEAD_REVIEW`. Preserve the bounded second-pass correction and its explicit non-atomicity limit. |
| Packaged manifest physically read more than once; thread `3997351895` | `IN_SCOPE_REPAIR`. The same PR02 engineer owns a coherent local repair and physical read-count adverse test after drain. No additional rescope is required. |
| Executing-module/source coherence; thread `3997351898` | `UNRESOLVED_MATERIAL_BOUNDARY_QUESTION`, excluded from this approval. No selector, unmanifested authority, import/reload scheme, immutable-deployment requirement, or deployment protocol is authorized. The PR02 engineer may preserve and investigate the evidence. If no compliant local repair exists within the immutable base plus F01 overlay, preserve the PR and return one new exact `RESCOPE_REQUEST` to the same whole-change IA through selected RS-20. |
| Requested atomic final multi-file source boundary; thread `3997351903` | `CONFLICTS_WITH_EXPLICIT_APPROVED_LIMITATION`. The remaining ordered-check window is acknowledged evidence, but no process-death atomicity, multi-file atomic visibility, cross-process locking, or immutable-deployment guarantee is required or authorized. A stronger product/architecture promise requires a separate Product Owner/Specification decision. This is not called repaired, waived, or a false positive. |
| Security comment `5648272341` | `HISTORICAL_CURRENT_HEAD_SECURITY_EVIDENCE`: no security issues reported at `eed8a638…`; not acceptance and not a waiver. Applicable review repeats after a changed head. |

All seven recorded review threads were unresolved in the accessible current collection. This RS-20 decision resolves only F01's authority question; it does not manipulate or mark GitHub threads resolved.

## 8. Tests, review, CI, documentation, and recovery

### 8.1 Required resumed evidence

- Prove positive admission of an exact 42-member synthetic complete release using the actual owning Gate schema.
- Prove a 41-member release is incomplete and an unapproved 43rd/extra member is rejected.
- Prove missing, malformed, noncanonical, reject-all, wrong-hash, wrong-size, changed, and unbound Gate schema cases fail through the owning typed boundary with no active handle.
- Prove the schema is read only from the captured manifest-bound selected root and no remote or hidden source is consulted.
- Prove the packaged manifest is physically read once per admission attempt while retaining the approved capture/change-detection evidence.
- Preserve duplicate-key, exact-type, Gate normalization, canonical-byte, safe-root, source-identity, recursive-freeze, mutation, and no-stale-fallback coverage.
- Preserve all unaffected current behavior and regenerate only evidence actually affected by the corrected code.

### 8.2 Existing evidence and required economical order

Recorded corrected-head evidence remains historical: 472 targeted tests passed; the default suite reported 1,724 passed and 3 existing closed-rails vendor skips; all nine governed writer/evidence checks passed; all seven CI lanes passed on run `34715034846` at exact head `eed8a638…`; and security review reported no findings. That evidence does not prove merge readiness while material review findings remain and cannot be reused as exact-head evidence after another commit.

On resume: verify the same workspace/worktree/branch/PR/head and user work; stop or avoid active PR02 CI while known review blockers remain; implement a coherent authorized batch; run targeted, regression, writer, classification, and clean-worktree checks locally; obtain substantive corrected-code review and security review; resolve applicable findings; then run CI once on the exact final PR head. Do not modify repository-wide workflow behavior merely to enforce this ordering.

### 8.3 Documentation and recovery

No documentation is written during RS-20. PR02 records the effective overlay and proof in its revised implementation Result. PR06 carries the effective 42-member final-manifest duty. PR07 documents the delivered contract and explicit limits after implementation.

Recovery reuses PR #404, branch `hde-epic040-pr02-immutable-admission`, its attributable commits, recorded recovery worktree, and original Proceed. Preserve the original workspace unchanged. Do not reconstruct accepted work, discard either workspace, create a replacement PR, rewrite the approved Plan, rerun PR01, or restart PR-30. Rollback restores the compatible loader/Gate/test set and leaves the actual 15-member manifest and previously active release unchanged.

## 9. Preserved exclusions and nonauthorization

- No approved Specification objective, exclusion, requirement text, or work-unit membership changes.
- No new public/API/CLI field, input, selector, config override, schema identity, math, scoring behavior, Gate taxonomy, or persistent identity model.
- No alternate validator or out-of-manifest schema source.
- No manifest promotion or release activation in PR02; actual manifest remains 15 members until PR06 authority.
- No process-death atomicity, multi-file atomic visibility, cross-process locking, immutable-deployment infrastructure, or universal concurrency guarantee.
- No PR01 rerun, no replacement Plan, no reauthored PR02 Plan/instruction, no replacement Proceed, no duplicate workspace/branch/PR, and no use of the rejected RS-20 output.
- No implementation, commit, push, CI trigger, thread resolution, merge, PF10 edit, QA, Ops, vendor/database action, deployment, release, or closure by this review.

## 10. Complete carried Canon-conflict register

| ID | Current decision and history |
|---|---|
| `C040-01` | `CANON_RECONCILIATION / APPROVED` exactly by Thoth-17, 2026-09-08T13:23:24Z. Source predicate resolved; existing PF10 Addenda 2.2 and 2.4 retained. |
| `C040-02` | `CANON_RECONCILIATION / APPROVED` by the same Thoth-17 decision. PF12 identity history and existing Addenda 2.2/2.4 retained. |
| `C040-03` | `CANON_RECONCILIATION / APPROVED` by the same Thoth-17 decision. PF14 identity history and existing Addenda 2.2/2.4 retained. |
| `C040-04` | `CANON_RECONCILIATION / APPROVED` by the same Thoth-17 decision. PF19 identity history and existing Addenda 2.2/2.4 retained. |
| `C040-05` | `CANON_RECONCILIATION / APPROVED`, alternative A, by Isis-49, 2026-09-09T03:57:16Z. Existing PF10 Addendum 2.3 retained; permanent PF14 drainage remains separately owned. |
| `C040-06` | `NEW_CANON / APPROVED`, alternative A, by Isis-50, 2026-09-09T11:48:08Z. Exact 36-row taxonomy and 16-state conformance retained; existing PF10 Addendum 2.5 retained. |
| `HDE-EPIC040-PR02-F01` | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED_PENDING_MANUAL_PF10_DRAIN` by the continuing whole-change IA in this exact v2.0 review. The approval is limited to member 42 and actual owning-schema execution. It becomes an effective canonical overlay only after Nathan's verified manual drain of the linked addendum. |

No existing decision is reopened, reinterpreted, omitted, renumbered, or duplicated. The executing-module/source question is not silently promoted into F01 or a new Canon decision. The atomicity request remains a separate review-scope conflict with an explicit approved limitation.

## 11. Manual prerequisite and actual native return

Nathan / Product Owner must manually publish the exact linked `PF10_BUILD_NOTES_ADDENDUM` into the current PF10 Markdown and verify the drained text, identity, and applicable status. This is the only Product Owner action required by this review. Nathan is not required to perform the technical analysis, rewrite or re-review a Plan, author a replacement instruction or Proceed, rerun PR01, implement code, resolve reviews, or operate CI.

Until that drain is verified:

- review state is `RESCOPE_APPROVED_PENDING_MANUAL_PF10_DRAIN`;
- Alpha state is `ALPHA_STOPPED_PENDING_MANUAL_PF10_DRAIN`;
- PR02 implementation remains suspended;
- PR #404 remains open/draft/unmerged; and
- neither this review nor the undrained addendum is implementation authority.

After verified drainage, the sole continuation is [RS-40 — Approved Rescope — Resume PR Implementation — 091326.2](https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204), invoked in the same dedicated PR02 engineering session under the original Proceed. RS-40 must verify this review, the exact addendum, current PF10 with the drained overlay, and the manual-drain evidence before mutation. It resumes; it does not restart PR-30.

## 12. Prompt-use record

| Field | Value |
|---|---|
| usage_id | `GCFPE-USE-HDE-EPIC040-RS-20-20260913-PR02-PROPOSALV10-01` |
| change/work | `EPIC / HDE-EPIC040 / HDE-EPIC040-PR02` |
| prompt | `RS-20 — Review Bounded Work-Unit Rescope — 091326.2` |
| prompt URL | https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204 |
| retrieved observation | `2026-09-13T11:33:42.943Z` |
| ecosystem | `GCFPE-20260913.1` |
| role/stage | continuing whole-change IA / bounded PR02 rescope review from PR-30 |
| capture time | `2026-09-13T13:33:56Z` |
| result | `APPROVE`; one PF10 addendum created; manual drain required before RS-40 |
| repository mutation | none |

Repository prompt-use persistence remains pending/non-gating unless an authorized repository writer later applies the actually installed procedure. This review supplies no repository-write authority.

ASK OK.
