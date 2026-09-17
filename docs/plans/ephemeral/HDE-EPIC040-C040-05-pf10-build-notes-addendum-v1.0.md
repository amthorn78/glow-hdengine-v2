# HDE-EPIC040 — Reconcile superseded core-test instructions

Timestamp: 2026-09-09T03:57:16Z
Details:

## Artifact identity and preparation status

- Artifact type: PF10_BUILD_NOTES_ADDENDUM.
- Logical identity: HDE-EPIC040-C040-05-PF10-BUILD-NOTES-ADDENDUM.
- Version: 1.0.
- Change: EPIC / HDE-EPIC040 — Separation Pass 3.
- Producer: Isis-49, continuing Lead Developer and IA-30 reviewer.
- Preparation status: COMPLETE.
- ADR decision status: APPROVED, exactly as proposed; not a proposal awaiting disposition.
- PF10 insertion/publication status: NOT PERFORMED; separate Product Owner-controlled manual action.
- Permanent Canon drainage status: PENDING; separately authorized governed source maintenance.
- Final PF10 addendum number: not assigned.

This standalone text is ready for the Product Owner's manual PF10 insertion. It records the actual approved Plan-stage reconciliation; preparation does not make it a published PF10 addendum. The exact unchanged Plan plus its review already carries the decision for HDE-EPIC040. Pending informational insertion does not block that approved Plan.

## Approval and exact source record

- Exact Plan: HDE-EPIC040-implementation-plan-v1.0.md; HDE-EPIC040-IMPLEMENTATION-PLAN v1.0; libfile_d477227231e48191a0d3960b5472b02e.
- Exact review: HDE-EPIC040-implementation-plan-review-v1.0.md; HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW v1.0; §§1 and 10.
- Plan decision: APPROVE, Isis-49, 2026-09-09T03:57:16Z.
- C040-05 decision: APPROVED exactly as proposed, alternative A, in that same review.
- Approved Specification: HDE-EPIC040-specification-v1.1-approved.md; libfile_12bab860949c8191881510875f051460; Thoth-17 APPROVE at 2026-09-08T13:23:24Z.
- Complete original proposal and history: exact Plan §11, preserved verbatim in review §9; actual new decision overlay in review §10.
- Artifact home for Plan, review and this addendum: /Glow HDE 3.0.

The review's actual returned provider identity is recorded in the accompanying creation proof and handoff after saving. This addendum does not require its own future identity or hash and creates no second approval object.

## C040-05 — Decided reconciliation

**Classification:** CANON_RECONCILIATION.

**Conflict.** HDE Mechanics Guide §6.7 explicitly supersedes the precomputed-score scaffold and requires the current four-argument Gate-based core and complete result contract. Later in the same section, the passages beginning “AB↔BA behavior tests live under” and “Determinism and JSON-compatibility tests live under” retain MUST instructions for compat_score, CoreConfig, three-argument calls and custom band_priority. These retained instructions prescribe an incompatible old test contract. HDE Math Spec §5.2 and HDE Architecture §§2.1–2.2 independently support the current pure-core contract.

**Exact runtime source binding.** The current controlled HDE Mechanics Guide Markdown was selected through Glow / Core Docs / PFCanon; file 1G6j4L4k0ExSvffp635-msbfV-qUjzjm8 presented filename version 3.5.6 and body version 3.5.4. Both labels remain preserved under C040-03. Supporting current controlled HDE Math Spec is version 1.3.7 and HDE Architecture is version 2.4.5. Their exact selection/parent/coverage records are in the review §2.2. This reconciliation does not decide a new intended PF14 metadata version.

**Approved decision.** Preserve the current exact four-argument contract, compute_core(member_a, member_b, mechanics_bundle, release_id), the Gate-based mechanics tests and complete magic10_result.v1 result obligations. Remove the contradictory legacy test passages or clearly mark them as historical so they no longer impose the superseded three-argument/precomputed-score contract. Preserve source history and the separate HDE-DIST008.1 evidence-wiring boundary. This is the approved alternative A, not a change to the adopted mathematics.

**Interim treatment.** Until permanent source drainage, the explicit current supersession and the owning Math/Architecture clauses control the planned implementation. Do not retain a second calculator, optional scoring configuration, precomputed-score input or alternate active configuration authority to satisfy obsolete instructions.

**Rationale and alternatives.** Leaving both unlabelled MUST passages unchanged would preserve a real implementation ambiguity. Restoring the older scaffold conflicts with the approved Specification and owning math/architecture. Removing or marking only the superseded passages resolves the textual conflict without inventing new calculations, interfaces, acceptance tokens or Product scope.

**Repository context, not execution proof.** Static inspection at 9065e6f0c01ad82a65c78687cd6c55e26ca33a1f shows the precomputed-score scaffold in engine/core/core.py, with the corresponding legacy tests documented in the complete Implementation Audit. This supports the practical risk of misleading instructions. It is not an executed test result, implementation completion or acceptance claim.

## Affected scope and implementation boundaries

Affected obligations remain K040-REQ-002, K040-REQ-005, K040-REQ-007, K040-REQ-009, K040-REQ-010 and K040-REQ-011; AC040-04, AC040-05, AC040-06 and AC040-08.

The approved Plan already assigns the canonical kernel/test migration and necessary application projections to its bounded units. This addendum does not expand them. The six selected PF09 units and twenty-nine Done/context exclusions remain unchanged; the pinned PF09.3 baseline is not replaced. Full golden comparison still uses actual canonical functions, not a second test-only scorer.

The public Reader remains bands-only and numeric-free. Product metadata is non-scoring. No caller-selected configuration, configuration blending, new public surface, replacement token system, DB migration, vendor action, tuning or deployment is introduced.

## Permanent drainage target and owner

- Owning source: HDE Mechanics Guide §6.7.
- Exact passage anchors: “AB↔BA behavior tests live under” and “Determinism and JSON-compatibility tests live under,” including their incompatible legacy MUST obligations.
- Owner: the governed HDE Mechanics Guide maintainer through separately authorized Canon maintenance.
- Allowed editorial outcome: remove or clearly historical-label the superseded passages while preserving the current normative core/test contract, source history and the separate HDE-DIST008.1 evidence-wiring boundary.
- Completion evidence: actual revised controlled source identity, identification of the affected passages, confirmation that current four-argument/Gate-based/result requirements and unrelated duties are unchanged. If the exact source has already been correctly drained, record that actual evidence rather than fabricate an edit.
- Remaining risk before drainage: a future reader may follow obsolete tests. This risk does not establish mathematical uncertainty or an executed failure.

The separate C040-03 metadata correction remains owned by the same source's governed maintainer under its earlier decision; this addendum does not combine or silently complete it.

## Existing decisions and publication boundary

C040-01–04 retain Thoth-17's actual 2026-09-08T13:23:24Z approvals. Their matching publication is verified in current HDE Build Notes v13.1.2, Addendum Index and inserted Addendum 2.2, “Canonize HDE-EPIC040 source-conflict ADR decisions.” Do not recreate that batch or seek the same decisions again absent materially different evidence. Their permanent source drainage remains outstanding.

The Product Owner separately controls insertion of this C040-05 text into HDE Build Notes and its index. No final addendum number is allocated here. Publication must be reported only from actual insertion evidence, not from this file's prepared or saved status.

This artifact does not edit or publish HDE Build Notes or any permanent PF; mutate a repository or board; approve a detailed PR plan; supply Proceed; authorize implementation, merge, CI, QA, Ops or production; reaccept a task; or decide closure. It records one approved reconciliation for later manual publication and permanent drainage.
