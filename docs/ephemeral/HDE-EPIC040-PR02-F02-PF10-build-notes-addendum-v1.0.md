---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
artifact_id: HDE-EPIC040-PR02-F02-PF10-BUILD-NOTES-ADDENDUM
artifact_version: 1.0
status: READY_FOR_MANUAL_DRAIN
canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN
drain_owner: Nathan / Product Owner
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR02
finding_ref: HDE-EPIC040-PR02-F02
decision_ref: HDE-EPIC040-PR02-F02-RESCOPE-REVIEW-v1.0
decision: APPROVE
created_at_utc: 2026-09-13T17:58:38Z
---

## 2.9 HDE-EPIC040-PR02-F02 — Executing-Code Coherence Rescope

### Status and authority

The Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent approves `HDE-EPIC040-PR02-F02-RESCOPE-REQUEST` v1.0 as a bounded implementation-contract overlay for the existing HDE-EPIC040-PR02 work unit and open draft PR #404.

The approved whole-change Implementation Plan v2.1, its Isis-50 approving Review v2.1, the PR02 Instruction v1.0, the PR02 detailed Implementation Plan v1.0, and the original Product Owner Proceed remain immutable and valid. The approved F01 overlay in PF10 §2.7 remains effective within its exact member-42 and owning-Gate-schema scope. F02 neither replaces nor reopens those decisions.

PR01 and merged PR #403 remain accepted and final. No accepted PR is rerun or reopened.

### Exact decision and source lineage

| Role | Exact source |
| --- | --- |
| Reviewed request | `HDE-EPIC040-PR02-F02-RESCOPE-REQUEST` v1.0, SHA-256 `cbfe94dd0530a6dbc052de5e9c9e67ddce8f1a878a9d16d1726cd53234d11b38`: https://drive.google.com/file/d/1nlCOzR3y9QvyynxFIFt9KU6U3urdUpCW/view?usp=drivesdk |
| Resumed implementation Result | `HDE-EPIC040-PR02-PR-IMPLEMENTATION-RESULT` v2.0, `RESCOPE_PENDING`, SHA-256 `33061285197b364a85d742a8faab36e839233df149be3859956d2d42bf06ebd2`: https://drive.google.com/file/d/16uYvir9dGnz8rp8fzoj1v_y67cQ_Wyc1/view?usp=drivesdk |
| Native decision | `HDE-EPIC040-PR02-F02-RESCOPE-REVIEW` v1.0, `APPROVE`, by the Product Owner-assigned continuing whole-change HDE-EPIC040 Implementation Agent, 2026-09-13 |
| Approved Specification | `HDE-EPIC040-specification-v1.1-approved.md`, Thoth-17 `APPROVE`, 2026-09-08T13:23:24Z: https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk |
| Immutable base Plan | `HDE-EPIC040-implementation-plan-v2.1.md`, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`: https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk |
| Base approval | `HDE-EPIC040-implementation-plan-review-v2.1.md`, Isis-50 `APPROVE`, 2026-09-09T13:36:43Z: https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk |
| Effective F01 overlay | PF10 §2.7, based on `HDE-EPIC040-PR02-rescope-review-v2.0.md` and its approved addendum; member 42 and owning Gate schema only |
| Current PF10 | `PF10-HDE-Build-Notes-v13.2.1.md`, SHA-256 `5c0f6f96a52b8821cb7826d492b0066322bf5eb12b48eff5b390eee002e5a7c9`: https://drive.google.com/file/d/1zCDNwfUjs9sqVZWK-nY2rGFmnpMg4RF1/view?usp=drivesdk |
| PR02 Instruction | `HDE-EPIC040-PR02-pr-instruction-v1.0.md`: https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk |
| PR02 detailed Plan | `HDE-EPIC040-PR02-pr-implementation-plan-v1.0.md`, original Proceed preserved: https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk |
| Original PR02 Result | `HDE-EPIC040-PR02-pr-implementation-result-v1.0.md`, original Proceed evidence: https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk |

### Approved bounded overlay

For HDE-EPIC040-PR02 only, the following requirements apply together with the existing immutable base and PF10 §2.7:

1. Active admission binds the already executing first-party admission implementation to the exact captured, manifest-bound Python sources that represent that implementation. Before returning an active bundle, the admission path compares retained actual module-execution code objects with compilation of the corresponding exact captured source bytes under the same interpreter and optimization semantics.
2. The executable-code comparison covers exactly these four existing modules:
   - `engine/config/registry_loader.py`
   - `engine/serializer/canon.py`
   - `engine/stable/sercanon.py`
   - `engine/categories/registry.py`
3. The effective synthetic complete-release roster adds exactly the latter two existing helper sources to the F01 42-member set. The complete synthetic admission roster is therefore 44 members. Both helper sources are captured from the same selected root and are bound through the same canonical path, exact bytes, hash, size, manifest membership, member-format checks, and unchanged-source evidence as every other admitted source.
4. The existing serializer and category registry remain the owning implementations. The temporary local attempt's duplicate `_canonical_json_bytes` implementation, copied category order, and import-time source-file hash are not approved solutions and are removed or replaced during the coherent engineering correction. The implementation does not create a second serializer or category authority.
5. Each covered module retains private, immutable provenance for the actual top-level code object that executed. The comparison uses the exact captured source and does not execute that source, reload a module, mutate `sys.modules`, change import selection, select another root, or expose a new public control.
6. Missing covered modules, unsafe or incompatible module origin, unavailable or unusable execution provenance, missing captured source, incompatible compilation semantics, or unequal executable code fails closed with an owning internal typed refusal. A disk hash, timestamp-based bytecode cache, caller-supplied module identity, unmanifested source, permissive fallback, or prior active handle cannot substitute.
7. Existing identities remain distinct and unchanged: exact per-member source identities, `config_sha256`, exact manifest-byte `manifest_sha256`, and `release_id = sha256(exact manifest bytes)`. The new predicate neither replaces those identities nor adds a public identity field.
8. The approved claim is executable-code equivalence for this four-module first-party admission closure. It does not prove the exact historical raw bytes originally read by the interpreter, arbitrary in-process tamper resistance, every imported dependency, every future executable member, universal runtime integrity, or a cryptographic trust anchor.
9. The actual current 15-member release manifest remains unchanged in PR02. Synthetic 44-member fixtures are validation evidence only. PR06 retains final manifest materialization, exact identity recomputation, convergence, and promotion of the complete effective roster after PR03–PR05.

### Requirements and acceptance effects

The approved Specification and requirement wording remain unchanged. The overlay adds implementation and evidence needed to satisfy these existing obligations:

| Requirement | F02 effect |
| --- | --- |
| `K040-REQ-006` | The single immutable manifest-bound active configuration includes the complete first-party implementation closure required for active admission; no partial or unbound implementation source qualifies. |
| `K040-REQ-007` | The strict schema-loaded immutable admission boundary verifies that its four named already executing implementation modules are equivalent to their captured, manifest-bound sources before returning a bundle. |
| `K040-REQ-008` | Stale bytecode, replaced source, missing provenance, missing helper members, origin mismatch, compilation mismatch, or code mismatch fails closed without fallback or a returned active handle. |
| `K040-REQ-009` | Source identity, executable-code equivalence, configuration identity, manifest identity, and release identity remain separate and receive distinct proof. |
| `AC040-04` | PR02 admission evidence includes successful and adverse four-module executable-code/source-coherence proof over the exact synthetic 44-member release. |
| `AC040-05` | PR02 contributes exact source/execution identity behavior; PR06 retains complete actual-manifest and final release-identity proof. |

`K040-REQ-001`–`005`, `K040-REQ-010`–`013`, and `AC040-01`–`03`, `AC040-06`–`09` retain their approved wording, owners, and completion burden. Existing evidence duties under `K040-REQ-011` and repository ownership duties under `K040-REQ-012` apply normally to the added code and tests; they are not new requirements.

### Work-unit and dependency effects

| Unit | Effect |
| --- | --- |
| PR01 / PR #403 | Accepted and final. No rerun, reopening, correction, or new acceptance. |
| PR02 / PR #404 | The same engineer completes F01, F02, and ordinary in-scope repairs coherently in the existing branch and draft PR under the original Proceed. No replacement Plan, Instruction, workspace, branch, PR, or Proceed. |
| PR03 | Dependency and mechanics scope are unchanged. It consumes only an accepted PR02 bundle and adopts the effective 44-member complete-fixture contract where applicable. |
| PR04 | Dependency, application, identity, and public/internal boundaries are unchanged. It receives no deployment selector or module-reload responsibility. |
| PR05 | Dependency and golden/readiness scope are unchanged. Future complete-release fixtures use the effective 44-member roster. |
| PR06 | Final materialization, exact member-byte refresh, identity recomputation, evidence convergence, and promotion remain solely PR06-owned. Its effective complete roster becomes 44 after earlier dependencies are accepted. |
| PR07 | Later documentation describes the delivered four-module executable-equivalence boundary and its explicit limits. No documentation work is authorized by this addendum. |
| OPS01 | Existing external verification purpose and separate action authority remain unchanged. |

The dependency order remains PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01. No work unit is added, removed, split, advanced, or rerun.

### Required implementation evidence

The completed correction proves all of the following before PR02 may claim merge readiness:

- A valid synthetic 44-member release succeeds. A 42- or 43-member release is incomplete, and an unapproved 45th or other extra member is refused.
- `engine/stable/sercanon.py` and `engine/categories/registry.py` receive missing, malformed, changed, wrong-hash, wrong-size, unsafe-path, and unbound-source adverse coverage.
- Fresh matching execution code accepts for each of the four covered modules. Materially different captured source for any covered already executing module refuses.
- A timestamp-valid stale bytecode cache containing implementation A while the source and manifest represent behaviorally different B is refused. Fresh B on the same disk inputs is separately evidenced.
- Missing or unsupported execution provenance and unsafe module origin fail closed without breaking unrelated candidate APIs or selecting a fallback. Production-origin proof cannot be satisfied solely by monkeypatching `__file__`.
- The existing shared serializer and category registry are exercised through their actual consumers. No copied implementation is accepted merely to reduce manifest closure.
- The PF10 §2.7 owning Gate schema and member-42 requirements, duplicate-aware canonical bytes, exact Gate normalization, local-schema closure, recursive freezing, alias protection, no stale active fallback, and bounded source-change checks remain covered.
- The packaged manifest is physically read once per admission attempt, with the ordinary thread `3997351895` repair and applicable adverse paths evidenced.
- Targeted tests, the default regression suite, all nine governed writer/evidence checks, changed-path ownership/classification, and clean-worktree checks pass locally before a meaningful commit or push.
- Substantive code and security review examine the exact corrected head. All applicable findings are resolved by the repository review owner before final CI. CI runs once against the exact final candidate after local validation and substantive review.

The feasibility probe recorded in the F02 request is not implementation completion, compatibility proof, security proof, review acceptance, CI evidence, or merge readiness.

### Preserved exclusions and limitations

This overlay does not authorize:

- proof of exact historical imported-source byte identity;
- module execution, import/reload machinery, import hooks, `sys.modules` mutation, or a new active selector;
- immutable-deployment infrastructure, a deployment protocol, held release descriptors, or a global source freeze;
- process-death atomicity, multi-file atomic visibility, cross-process locking, or a stronger portability guarantee;
- a public/API/CLI field, configuration override, identity change, second validator, second serializer, copied category authority, alternate calculator, remote schema fetch, or fallback;
- modification of the actual 15-member manifest in PR02, release activation, deployment, QA, Ops, live vendor/database work, PF10 mutation, merge, or Epic closure.

The explicit detailed-Plan limitation on process-death atomicity, multi-file atomic visibility, and cross-process locking remains controlling. Thread `3997351903` remains `CONFLICTS_WITH_EXPLICIT_APPROVED_LIMITATION`; its observed residual window remains disclosed and is neither repaired nor dismissed as a false positive.

### Review findings and owners

| Finding | Current authority and owner |
| --- | --- |
| `3997320377` / `3997320916` | F01 authority is approved and drained in PF10 §2.7. The PR02 engineer owns completed schema implementation and corrected-code proof. |
| `3997320380` | Preserve the existing symlink correction. Final current-head disposition remains with the repository review owner. |
| `3997320917` | Preserve the bounded inter-read correction and the approved non-atomicity limitation. Corrected-code proof remains with the engineer and reviewer. |
| `3997351895` | Ordinary in-scope PR02 repair. The engineer must establish exactly one physical packaged-manifest read with adverse proof. |
| `3997351898` / F02 | The bounded four-module executable-code/source-coherence overlay and effective 44-member synthetic roster are approved by this decision. Implementation and proof remain outstanding. |
| `3997351903` | Conflicts with the explicit approved limitation. No atomicity expansion is authorized; the repository review owner retains the thread's final disposition. |
| Security comment `5648272341` | Historical no-findings evidence for `eed8a638…` only. Changed code requires applicable current-head security review. |

No review thread is declared resolved by this addendum. Historical tests and CI at `eed8a63807f573abc29de6f6d5ceac54f0c8da85` remain evidence only for that head.

### Alternatives and rationale

| Alternative | Disposition |
| --- | --- |
| Four-module retained-code/compiled-captured-source comparison plus two manifest-bound helper members | Approved as the smallest bounded source/execution closure that preserves existing owners and the immutable release-bound design. |
| Import-time disk hash | Rejected. A valid stale bytecode cache can execute A while the disk hash and admitted manifest represent B. |
| Duplicate serializer and copied category order in the loader | Rejected. It changes ownership to avoid dependency closure and does not establish executing-code identity. |
| Keep 42 members and inspect helper source outside the manifest | Rejected. It creates unmanifested source authority. |
| Require exact historical raw imported-byte identity | Not claimed by this design. That stronger trust boundary is outside this bounded request. |
| Import hooks, reloads, immutable deployment, locking, or atomic release roots | Outside scope and unnecessary for the approved bounded executable-equivalence claim. |
| Narrow the Specification to disk-source identity only | Not selected. The existing exact-source, immutable-admission, refusal, and identity obligations remain unchanged. |

The approval is bounded to the explicit four-module executable-equivalence predicate, the two named helper members, the 44-member synthetic complete roster, and the stated evidence. It does not approve an unspecified broader runtime-integrity mechanism.

### Recovery, review, and release continuity

The existing draft PR #404, branch `hde-epic040-pr02-immutable-admission`, accepted base `3828d4b3454259841a3e48d13039dd1475754f2f`, and recorded remote head `eed8a63807f573abc29de6f6d5ceac54f0c8da85` remain the repository lineage. The recorded recovery directory remains `/workspace/scratch/b736cdb96988/pr02-recovery` and retains the complete four-file local delta carried in the F02 request. Missing Git metadata and repository files are restored around that preserved delta without replacing or discarding it. The inaccessible original workspace remains unchanged.

The existing local import-hash, duplicate-serializer, copied-category-order attempt is preserved as historical recovery evidence, not accepted code. Engineering performs one coherent correction batch covering the approved F01 and F02 overlays plus ordinary in-scope defects. Reviews take priority over CI. Local validation and substantive corrected-head review precede the next final-candidate CI run. The historical successful CI run `34715034846` remains attributed only to `eed8a638…` and cannot establish a changed head.

The actual 15-member release remains unchanged and incomplete for this Epic. PR06 retains final materialization and promotion. No production, deployment, QA, Ops, vendor, database, release, merge, PF10-edit, or closure authority is created.

### Carried Canon-conflict register

| ID | Carried decision/state |
| --- | --- |
| C040-01 | `CANON_RECONCILIATION / APPROVED` by Thoth-17, 2026-09-08T13:23:24Z; PF10 §§2.2/2.4 retained. |
| C040-02 | `CANON_RECONCILIATION / APPROVED` by Thoth-17; PF12 identity history and PF10 §§2.2/2.4 retained. |
| C040-03 | `CANON_RECONCILIATION / APPROVED` by Thoth-17; PF14 identity history and PF10 §§2.2/2.4 retained. |
| C040-04 | `CANON_RECONCILIATION / APPROVED` by Thoth-17; PF19 identity history and PF10 §§2.2/2.4 retained. |
| C040-05 | `CANON_RECONCILIATION / APPROVED`, alternative A, by Isis-49, 2026-09-09T03:57:16Z; PF10 §2.3 retained. |
| C040-06 | `NEW_CANON / APPROVED`, alternative A, by Isis-50, 2026-09-09T11:48:08Z; PF10 §2.5 retained. |
| HDE-EPIC040-PR02-F01 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED`; effective only within PF10 §2.7's member-42 and owning-Gate-schema scope. |
| HDE-EPIC040-PR02-F02 | `BOUNDED_WORK_UNIT_RESCOPE / APPROVED` by the continuing whole-change HDE-EPIC040 IA in `HDE-EPIC040-PR02-F02-RESCOPE-REVIEW` v1.0; exact four-module executable-equivalence and effective 44-member synthetic roster only. |

No prior decision is reopened, relabeled, or duplicated. No new product objective, Specification change, public contract, or permanent Canon-maintenance assignment is created.

### Resulting status

HDE-EPIC040-PR02 remains stopped for implementation until this approved overlay is available in the authoritative in-flight PF10 record. After that prerequisite is verified, the same PR02 engineering session resumes the existing work under the original Proceed through the selected RS-40 continuation. PR #404 remains open, draft, unmerged, and not ready to merge until the approved correction, complete local validation, substantive corrected-head review, and exact-final-head CI are complete.
