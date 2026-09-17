---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
artifact_id: HDE-EPIC040-PR02-F03-PF10-BUILD-NOTES-ADDENDUM
artifact_version: 1.0
status: READY_FOR_MANUAL_DRAIN
canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
drain_owner: Nathan / Product Owner
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
finding_ref: HDE-EPIC040-PR02-F03
source_request_id: HDE-EPIC040-PR02-F03-RESCOPE-REQUEST
source_request_version: 1.0
source_decision_id: HDE-EPIC040-PR02-F03-RESCOPE-REVIEW
source_decision_version: 1.0
source_decision: APPROVE
author_role: Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent
created_at: 2026-09-13T21:12:59Z
target_pf10: PF10-HDE-Build-Notes-v13.2.2.md
target_section: 2.10
ecosystem_release: GCFPE-20260913.1
prompt_version: 091326.2
---

## 2.10 HDE-EPIC040-PR02-F03 — Existing Serializer Manifest Binding Refresh

### Status and authority

The Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent approves `HDE-EPIC040-PR02-F03-RESCOPE-REQUEST` v1.0 as a bounded implementation and evidence-maintenance overlay for the existing HDE-EPIC040-PR02 work unit and open draft PR #404.

The approved Specification v1.1, immutable whole-change Implementation Plan v2.1, Isis-50 approving Plan Review v2.1, PR02 Instruction v1.0, PR02 detailed Implementation Plan v1.0, and original Product Owner Proceed remain valid and unchanged. The F01 and F02 overlays already effective in PF10 §§2.7 and 2.9 remain approved and are not reopened.

This overlay supersedes only the statements in PF10 §§2.7 and 2.9 that the actual 15-member manifest remains byte-unchanged in PR02. It permits exactly one existing-row provenance refresh and its owner-generated evidence convergence. It does not authorize an actual-roster count change in PR02, an implementation-Plan rewrite, another Proceed, a new PR, or final release promotion.

PR01 and merged PR #403 remain accepted and final. No accepted PR is rerun or reopened.

### Exact decision and source lineage

| Role | Exact source |
| --- | --- |
| Reviewed request | `HDE-EPIC040-PR02-F03-RESCOPE-REQUEST` v1.0, SHA-256 `3939035a85b3697d2816e9d0b799326d746b0b878f2aa08fce7c386eca1a294f`: https://drive.google.com/file/d/1iKB5nFqGNXM8fbAZiC2tItvP8nVA3LaZ/view?usp=drivesdk |
| Resumed Result | `HDE-EPIC040-PR02-PR-IMPLEMENTATION-RESULT` v3.0, `RESCOPE_PENDING`, SHA-256 `20523b967bb4ba266c5f223e78b4abc9ebef0afcef09a6513905774fb3d66518`: https://drive.google.com/file/d/18yYnDiXGZWKLMLtH31ysn69Gr1hw-XeP/view?usp=drivesdk |
| Native decision | `HDE-EPIC040-PR02-F03-RESCOPE-REVIEW` v1.0, `APPROVE`, by the Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent, 2026-09-13 |
| Current PF10 | `PF10-HDE-Build-Notes-v13.2.2.md`, SHA-256 `d1db160a6a10aac25ed034e820f7026537cc9d178f22e8e978ed1620a61b0bec`: https://drive.google.com/file/d/1suxrnM-g96R3tqThIpND3ll9s1qKaopK/view?usp=drivesdk |
| Effective F01 overlay | PF10 §2.7; owning Gate schema and effective synthetic member 42 only; approved by `HDE-EPIC040-PR02-F01-RESCOPE-REVIEW` v2.0 |
| Effective F02 overlay | PF10 §2.9; four-module executable-code equivalence and effective synthetic 44-member roster only; approved by `HDE-EPIC040-PR02-F02-RESCOPE-REVIEW` v1.0: https://drive.google.com/file/d/18JGk0EwtaA5_ZD3WWZHJmacK139utjWa/view?usp=drivesdk |
| Approved Specification | `HDE-EPIC040-specification-v1.1-approved.md`, Thoth-17 `APPROVE`, 2026-09-08T13:23:24Z: https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk |
| Immutable base Plan | `HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`: https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk |
| Base approval | `HDE-EPIC040-implementation-plan-review-v2.1.md`, Isis-50 `APPROVE`, 2026-09-09T13:36:43Z: https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk |
| PR02 instruction | `HDE-EPIC040-PR02-pr-instruction-v1.0.md`, `INSTRUCTION_READY`: https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk |
| PR02 detailed Plan | `HDE-EPIC040-PR02-pr-implementation-plan-v1.0.md`; original Product Owner Proceed remains valid: https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk |
| Original PR02 Result | `HDE-EPIC040-PR02-pr-implementation-result-v1.0.md`; original Proceed and historical engineering evidence: https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk |

### Cause and approved bounded overlay

F02 requires actual top-level execution provenance for `engine/serializer/canon.py`. The prepared provenance-bearing wrapper is 795 bytes with SHA-256 `2a077c957c7526f9c0fe9c482d299b6912df05b084fa5fc9c5f63b555e23eec5`; the current actual 15-member manifest still binds the former 485-byte wrapper with SHA-256 `f56cdacfb90b7d9cb467d7e6005ad62e62e83d4b04c022c53e9f9b190e7777c3`. The unchanged owning manifest-integrity and canonical-JSON checks correctly refuse that mismatch. Restoring the old wrapper would instead violate F02 and produce `EXECUTION_PROVENANCE_UNAVAILABLE` in the isolated complete fixture.

For HDE-EPIC040-PR02 only, apply all of the following together:

1. Rebind only the existing `engine/serializer/canon.py` row in `catalog/manifest.json` to the exact final, locally validated, substantively reviewed provenance-bearing wrapper bytes. Use the existing canonical manifest writer. Change only that row's `sha256` and `size` values.
2. Keep the actual PR02 release roster at exactly 15 members. Preserve the other 14 manifest rows, row ordering, `root`, `version`, and `built_at_utc`. Do not add the F01 Gate schema, either F02 helper source, or any future member to the actual manifest during PR02.
3. Preserve `release_id = sha256(exact manifest bytes)` and distinct source, configuration, manifest, and release identities. The one-row refresh necessarily changes the manifest bytes and release identity; no stale identifier may be retained or described as unchanged.
4. Treat the recorded candidate identities only as reproduction evidence: current actual manifest SHA-256 `c0f5f24fbbcbb04d01d1613be386c26fddbfb37d53cbb0f9c65d5cf55e97c2a4`, 1,981 bytes; isolated one-row candidate SHA-256 `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856`, 1,981 bytes. The final identities must be recomputed from the exact final reviewed bytes and are not preapproved constants.
5. Permit only the corresponding existing canonical-JSON gate and evidence maintenance required by this one-row refresh. The gate owner remains `tools/evidence/run_canonical_json_gate.py`. Its six current outputs are:
   - `audit/gates/canonical_json/json_canonical_check.log`
   - `audit/gates/canonical_json/json_canon_compare.log`
   - `audit/gates/canonical_json/canonical_json.gate.json`
   - `audit/gates/json_gate/canonical/json_gate_check_log.ndjson`
   - `audit/gates/json_gate/canonical/json_gate_compare_log.ndjson`
   - `audit/gates/json_gate/canonical/json_gate_structured_record.json`
6. Regenerate the owned `.path_proof.txt` companions for those outputs where required. The sole existing evidence updater owns any resulting INDEX, Mirror, checksum, orientation, or path-proof convergence in its existing families. Do not hand-edit evidence, recapture historical vendor, QA, Ops, or CLI inputs, rewrite capture-time identity claims, introduce a new evidence family, or refresh unrelated artifacts.
7. Preserve all strict manifest-content, canonical-JSON, source-identity, ownership, and CI checks. No waiver, ignored serializer row, xfail, narrowed assertion, fake hash, unmanifested old-source authority, import hook, loader/reload scheme, `sys.modules` mutation, duplicate serializer, selector, deployment protocol, or stronger atomicity mechanism is approved.
8. PR02 remains responsible for completing F01, F02, F03, ordinary in-scope repairs, local proof, corrected-head review, and exact-final-head CI in the existing PR. PR06 retains final actual 44-member manifest materialization, complete member refresh, final identity recomputation and convergence, and promotion after PR03–PR05.

This is a bounded in-flight implementation and evidence-maintenance correction within the approved Specification intent. It changes no objective, exclusion, requirement text, mathematics, taxonomy, public/API/CLI contract, identity formula, work-unit order, or Product Owner scope.

### Requirements and acceptance effects

| Requirement | F03 effect |
| --- | --- |
| `K040-REQ-007` | The immutable admission boundary may retain F02's required provenance-bearing serializer wrapper while remaining exactly bound by the actual PR02 manifest. |
| `K040-REQ-008` | Stale or mismatched wrapper/manifest identities continue to fail closed; the correction updates the owned binding rather than weakening refusal. |
| `K040-REQ-009` | Source, configuration, exact manifest-byte, and release identities remain distinct and are recomputed from actual bytes. |
| `K040-REQ-011` | Existing canonical-JSON and evidence owners regenerate only the affected outputs and prove convergence without fabricating historical captures. |
| `K040-REQ-012` | The canonical manifest writer, canonical-JSON gate owner, and sole evidence updater remain the only writers for their owned outputs. |
| `AC040-04` | PR02 proves a coherent manifest-bound F01/F02/F03 admission candidate without changing the actual 15-member roster. |
| `AC040-05` | PR02 proves its exact source/manifest/release identity behavior; PR06 retains final 44-member materialization and promotion proof. |

All other approved requirement and acceptance-criterion text, allocation, and completion burden remain unchanged. This overlay satisfies no later unit in advance.

### Work-unit and dependency effects

| Unit | Effect |
| --- | --- |
| PR01 / PR #403 | Accepted and final. No rerun, reopening, repair, or new acceptance. |
| PR02 / PR #404 | After verified PF10 drain, the same engineer applies the one-existing-row refresh and owner-generated evidence convergence together with the preserved F01/F02 correction and ordinary repairs. No new Plan, Instruction, Proceed, workspace, branch, or PR. |
| PR03 | Scope and dependency remain unchanged. It begins only after PR02 acceptance. |
| PR04 | Scope and dependency remain unchanged. No selector, deployment, import, or identity responsibility is transferred. |
| PR05 | Scope and dependency remain unchanged. Later complete-release fixtures use the effective 44-member roster. |
| PR06 | Retains sole ownership of final actual 44-member manifest materialization, all-member refresh, final identity recomputation/convergence, and promotion after PR03–PR05. F03 does not materialize 44 members early. |
| PR07 | Later documentation records the delivered manifest-binding and executable-equivalence boundaries and limits. No documentation work is executed here. |
| OPS01 | Existing external verification purpose and separate action authority remain unchanged. |

The dependency order remains PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01. No unit is added, removed, split, advanced, or rerun.

### Required completion evidence

PR02 cannot claim completion or merge readiness until the engineer demonstrates all applicable existing F01/F02 evidence plus the following F03-specific evidence:

- The exact final `engine/serializer/canon.py` bytes match the sole existing manifest row's final `sha256` and `size`.
- The actual manifest remains 15 members with the other 14 rows, ordering, `root`, `version`, and `built_at_utc` unchanged.
- The exact final manifest SHA-256 and `release_id` are freshly recomputed from the final exact manifest bytes and remain distinct from source and configuration identities.
- The canonical writer is the only manifest writer; repeated generation converges without an unowned byte change.
- The canonical-JSON owner regenerates only the six listed outputs and their required companions; the sole evidence updater converges only the affected existing families.
- A stale wrapper row is refused by the owning manifest-integrity and canonical-JSON checks. The restored old wrapper is refused by F02's execution-provenance requirement. The valid refreshed binding passes both boundaries.
- Targeted tests, default regression, all governed writer/evidence checks, changed-path classification, all selected CI-lane ownership checks, whitespace checks, and clean candidate/worktree evidence pass on the complete coherent correction.
- Substantive code and security review examine the exact corrected head. Applicable review blockers are resolved before CI is allowed to run. Final CI runs once against the exact final reviewed PR head.

The reported `562 passed, 1 failed`, `1,800 passed, 3 skipped`, and `8 passed, 1 failed` results truthfully describe the pre-F03 paused local candidate. They are not completion evidence. The three regression skips remain the existing closed-rails vendor skips, not waivers. Historical CI run `34715034846` and security comment `5648272341` remain attributable only to `eed8a63807f573abc29de6f6d5ceac54f0c8da85` and cannot prove a changed head.

### Preserved exclusions and limitations

This overlay does not authorize:

- a 16-member actual PR02 manifest or early 44-member actual manifest;
- any new manifest member, second manifest, unmanifested source, fake identity, ignored row, or weakened check;
- exact historical imported-source byte identity beyond F02's approved four-module executable-code-equivalence claim;
- module execution, import or reload machinery, an import hook, `sys.modules` mutation, a selector, deployment protocol, or immutable-deployment infrastructure;
- process-death atomicity, multi-file atomic visibility, cross-process locking, a held global release descriptor, or any stronger portability promise;
- a second serializer, copied category owner, alternate validator, alternate calculator, remote schema fetch, or public/API/CLI field;
- unrelated evidence refresh, historical recapture, live vendor/database access, QA, Ops, deployment, release activation, PF10 editing, merge, or Epic closure.

The approved detailed-Plan limitation on process-death atomicity, multi-file atomic visibility, and cross-process locking remains controlling. Thread `3997351903` remains `CONFLICTS_WITH_EXPLICIT_APPROVED_LIMITATION`; the observed ordered-check window remains disclosed and is neither repaired nor dismissed as a false positive.

### Review findings and owners

| Finding | Preserved authority and owner |
| --- | --- |
| `3997320377` / `3997320916` | F01 authority is approved and drained. The PR02 engineer owns complete schema implementation and corrected-code proof; the repository review owner retains final thread disposition. |
| `3997320380` | Preserve the existing symlink correction. Final current-head disposition remains with the repository review owner. |
| `3997320917` | Preserve the bounded inter-read correction and explicit non-atomicity limit. Corrected-code proof and final disposition remain with the engineer and reviewer. |
| `3997351895` | Ordinary in-scope PR02 repair. Preserve the prepared one-physical-manifest-read correction and test, then establish it on the final candidate. The repository reviewer retains final disposition. |
| `3997351898` / F02 | F02 is approved and drained. The engineer owns coherent implementation and proof. F03 removes the specific owned-manifest publication blocker without expanding F02. |
| `3997351903` | Conflicts with the explicit approved limitation. No atomicity expansion is authorized; final thread disposition remains with the repository review owner. |
| F03 | Approved only as the one-existing-row manifest refresh and bounded owner-generated evidence convergence stated here. It has no invented GitHub thread ID. |
| Security comment `5648272341` | Historical no-findings evidence for `eed8a638…` only. Changed code requires applicable current-head security review. |

All seven existing repository review threads remain unresolved at this decision point. This addendum does not resolve GitHub threads, approve code, or establish merge readiness.

### Alternatives and rationale

| Alternative | Disposition |
| --- | --- |
| Rebind the one existing serializer row and regenerate only owner-governed affected evidence | Approved. This is the smallest complete correction that satisfies F02 while preserving strict manifest identity, current roster size, writer ownership, and PR06 boundaries. |
| Restore the 485-byte serializer wrapper | Rejected. It removes the top-level execution provenance required by approved F02 and reproduces `EXECUTION_PROVENANCE_UNAVAILABLE`. |
| Keep the stale row and waive or narrow integrity checks | Rejected. It breaks exact source/manifest identity and turns a valid fail-closed gate into a bypass. |
| Use the old wrapper as unmanifested authority | Rejected. It violates same-root, captured, manifest-bound source authority. |
| Add a 16th actual member or materialize all 44 members in PR02 | Rejected. No new member is needed for F03, and full 44-member materialization remains PR06-owned. |
| Defer the stale binding until PR06 | Rejected. PR02 cannot complete or be accepted with an internally inconsistent admitted source and manifest. |
| Rewrite the approved Plan, rerun PR-30 or PR01, issue a new Proceed, or replace PR #404 | Prohibited and unnecessary under the in-flight PF10 overlay contract. |

### Repository, recovery, and release continuity

The existing open draft PR #404, branch `hde-epic040-pr02-immutable-admission`, accepted base `3828d4b3454259841a3e48d13039dd1475754f2f`, ordered commits `3dda87853466fa18247654ffe5bb67561364b0f4` and `eed8a63807f573abc29de6f6d5ceac54f0c8da85`, and recorded tree `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d` remain the repository lineage. The recorded recovery directory remains `/workspace/scratch/b736cdb96988/pr02-recovery`.

The preserved local correction is not accepted code and is not discarded: 47,076 textual bytes, SHA-256 `a2644c0e7c8b802c274e46c8074db569e1e02e7c339f9188ac73a5690bae8af2`. The original inaccessible workspace at `/workspace/scratch/8d666e9ba95b/glow-hdengine-v2` remains unchanged. The five separately Product Owner-authorized historical archive removals and exact ignore rules remain separate housekeeping, not part of F03. The restored `artifacts/engine/order/abba_identity.bytes` remains generator-owned and carries no tracked change.

The actual release remains the existing 15-member release. This approval changes only the permission to refresh one existing row and the resulting exact manifest/release identity in the PR02 candidate. It does not activate or promote a release.

### Carried Canon-conflict register

| ID | Carried decision/state |
| --- | --- |
| C040-01 | `CANON_RECONCILIATION / APPROVED` by Thoth-17, 2026-09-08T13:23:24Z; PF10 §§2.2/2.4 retained. |
| C040-02 | `CANON_RECONCILIATION / APPROVED` by Thoth-17; PF12 identity history and PF10 §§2.2/2.4 retained. |
| C040-03 | `CANON_RECONCILIATION / APPROVED` by Thoth-17; PF14 identity history and PF10 §§2.2/2.4 retained. |
| C040-04 | `CANON_RECONCILIATION / APPROVED` by Thoth-17; PF19 identity history and PF10 §§2.2/2.4 retained. |
| C040-05 | `CANON_RECONCILIATION / APPROVED`, alternative A, by Isis-49, 2026-09-09T03:57:16Z; PF10 §2.3 retained. |
| C040-06 | `NEW_CANON / APPROVED`, alternative A, by Isis-50, 2026-09-09T11:48:08Z; PF10 §2.5 retained. |
| HDE-EPIC040-PR02-F01 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED`; effective only within PF10 §2.7's owning-Gate-schema and effective synthetic member-42 scope. |
| HDE-EPIC040-PR02-F02 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED`; effective only within PF10 §2.9's four-module executable-equivalence and effective synthetic 44-member scope. |
| HDE-EPIC040-PR02-F03 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED`; exactly one existing serializer manifest-row hash/size refresh, resulting exact manifest/release identity recomputation, and bounded existing-owner canonical evidence convergence. |

No prior decision is reopened, relabeled, or duplicated. No new product objective, Specification change, public contract, or permanent Canon-maintenance assignment is created.

### Resulting status

HDE-EPIC040-PR02 remains stopped at `RESCOPE_PENDING` until this exact approved overlay is manually drained into the current authoritative PF10 Markdown and the substantive match is verified. After that prerequisite, the same PR02 engineering session resumes the existing work under the original Proceed through the selected RS-40 continuation. PR #404 remains open, draft, unmerged, and not ready to merge until the complete coherent correction, local validation, substantive exact-head review, and final exact-head CI succeed.

<eof>
