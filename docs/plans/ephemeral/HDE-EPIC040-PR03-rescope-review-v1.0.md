# HDE-EPIC040-PR03 — Bounded Rescope Review v1.0

```yaml
artifact_type: RESCOPE_REVIEW
RESCOPE_REVIEW_ID: HDE-EPIC040-PR03-RESCOPE-REVIEW-01
version: v1.0
state: APPROVED_PENDING_MANUAL_DRAIN
decision: APPROVE
decision_utc: 2026-09-14T10:34:33Z
reviewer: retained Product Owner-assigned whole-change HDE-EPIC040 Implementation Architect
change_class: EPIC
change_id: HDE-EPIC040
work_unit_id: HDE-EPIC040-PR03
finding_id: PR03-R02
reviewed_artifact_type: RESCOPE_REQUEST
reviewed_request_id: HDE-EPIC040-PR03-RESCOPE-REQUEST-01
reviewed_request_version: v1.0
reviewed_request_sha256: 1f5a1df21a4be089809b9ac642ca047d3205669a39cf3e2c8ce301bda5dd41e1
lifecycle: EXISTING_OPEN_PR_IMPLEMENTATION
originating_stage: PR-30
return_stage: RS-40_AFTER_VERIFIED_MANUAL_DRAIN
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: retained Product Owner-assigned whole-change HDE-EPIC040 Implementation Architect
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR03 / RS-20
context_conflict: NONE
original_PO_PROCEED: PRESERVED
base_plan_rewrite: PROHIBITED_AND_NOT_PERFORMED
repository_mutation: NOT_PERFORMED
merge_authority: NOT_GRANTED
PF10_mutation: NOT_PERFORMED
PF10_BUILD_NOTES_ADDENDUM_ID: HDE-EPIC040-PR03-R02-PF10-BUILD-NOTES-ADDENDUM
PF10_BUILD_NOTES_ADDENDUM_VERSION: v1.0
output_classification: EPHEMERAL_DRIVE
output_destination: Glow / Ephemeral Planning Files
```

## 1. Decision

**APPROVE.** `HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0` is a genuine bounded implementation rescope within the approved HDE-EPIC040 Specification intent.

The approved delta extends the existing PR02 admission owner's passive executable-equivalence coverage to exactly four newly active PR03 mechanics modules:

- `engine/core/core.py`
- `engine/magic10/composite.py`
- `engine/magic10/signals.py`
- `engine/magic10/calculators.py`

The extension must bind the code actually executing these mechanics to the exact captured, manifest-bound source used by the admitted release before an `AdmittedMechanicsBundle` can be returned and before `compute_core` can label a successful result with that release identity.

This decision does not approve the engineer's unimplemented proposal as completed code. It authorizes only the bounded correction defined in this review after the accompanying PF10 addendum has been manually drained and verified. PR03 remains suspended at the affected boundary until that prerequisite is satisfied.

## 2. Exact request, role, lifecycle, and immutable bases

| Role | Exact source and status |
| --- | --- |
| Reviewed request | [HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0](https://drive.google.com/file/d/1Cg6LglLhgqPVrHr6uL374kkdiP2Zqzu6/view?usp=drivesdk), `RESCOPE_PENDING`, SHA-256 `1f5a1df21a4be089809b9ac642ca047d3205669a39cf3e2c8ce301bda5dd41e1`; exact-text readback reported as 270 lines / 31,251 bytes |
| Current implementation record | [HDE-EPIC040-PR03 PR Implementation Result v1.1](https://drive.google.com/file/d/1UZZYqgpVrbraGMGrlOFnPwGqFCUp4ZmF/view?usp=drivesdk), `RESCOPE_PENDING` |
| Incident and CI-control record | [HDE-EPIC040-PR03 Session Completion and CI Control RCA v1.1](https://drive.google.com/file/d/1EOOqIiuaVxPv42Oh9sf3kxNF0WhmC2NK/view?usp=drivesdk) |
| PR instruction | [HDE-EPIC040-PR03 PR Instruction v1.0](https://drive.google.com/file/d/1Zj5BResRRxtGarmZ2d3sIAfIVeLD42rs/view?usp=drivesdk), `INSTRUCTION_READY` |
| Detailed PR Plan | [HDE-EPIC040-PR03 PR Implementation Plan v1.0](https://drive.google.com/file/d/1wPpcIQkDLVNwdvK2ujfDpkssUh4KwAoO/view?usp=drivesdk); Nathan's original Proceed remains valid |
| Approved Specification | [HDE-EPIC040 Specification v1.1](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk), Thoth-17 `APPROVE` |
| Implementation Audit | [HDE-EPIC040 Implementation Audit v2.0](https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk), `AUDIT_COMPLETE` |
| Immutable whole-change Plan | [HDE-EPIC040 Implementation Plan v2.1](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk) |
| Approving Plan review | [HDE-EPIC040 Implementation Plan Review v2.1](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk), Isis-50 `APPROVE` |
| Accepted predecessors | [PR01 lineage review v1.1](https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk), `ACCEPT`; [PR02 lineage review v1.0](https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk), `ACCEPT` |
| Current PF10 | [PF10 — HDE Build Notes v13.2.4](https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk), unique controlled Markdown resolved through `Glow / Core Docs / PFCanon` |

The reviewer identity is the retained Product Owner-assigned whole-change HDE-EPIC040 Implementation Architect. The lifecycle is the existing, proceeded, open PR03 implementation. The return owner remains the dedicated PR03 engineering session. Isis-50 remains the independent reviewer of the immutable whole-change Plan and is not substituted for this RS-20 decision.

PR01 / #403 and PR02 / #404 remain accepted and final. This review does not reopen either work unit or any accepted PR02 F01/F02/F03 overlay.

## 3. Evidence-supported finding

PR03-R02 is independently reproduced against the preserved PR03 worktree at head `b33c41721ad2320f71c2cdaf00616e27d36945da`, tree `4af351d6f7347541b9853927bf5098299adcc81f`.

The bounded reproduction:

1. imported the actual PR03 core and mechanics modules;
2. constructed and admitted the existing synthetic complete release;
3. changed only the temporary fixture's `engine/magic10/signals.py` arithmetic from addition to subtraction;
4. confirmed that the altered source compiled;
5. regenerated the fixture manifest and release identity through the existing fixture owner; and
6. admitted and computed again without changing the already imported runtime implementation.

Observed result:

| Predicate | Actual observation |
| --- | --- |
| Baseline fixture admission | `PASS` |
| Altered, coherently rehashed fixture admission | `PASS` |
| Release identity changed | `true` |
| Computed signals remained unchanged | `true` |
| Computed categories remained unchanged | `true` |
| Result carried the altered release ID | `true` |
| Finding | `REPRODUCED` |

The executing source SHA-256 was `c1d3829c21934452ed1a34b7ba32d8f84664033730f1ec0ebdea354d24f2c690`; the altered fixture source SHA-256 was `fa51ef85f2cc711fee24a58139214945214bc3a6630ed14d648279808cae232c`.

The repository remained clean after the independent reproduction. No source correction was applied.

The current admission path captures and verifies every manifest member but performs passive executable-equivalence validation only for these accepted PR02 owners:

- `engine/config/registry_loader.py`
- `engine/serializer/canon.py`
- `engine/stable/sercanon.py`
- `engine/categories/registry.py`

The newly active PR03 modules are members of the effective synthetic 44-member release roster but are not part of that execution-provenance comparison. Syntax validation and coherent source/manifest hashes therefore do not establish that their already imported code is equivalent to the admitted bytes.

The demonstrated defect is false release-to-execution attribution within the supported synthetic complete-release path. It does not establish a production incident, arbitrary in-process tamper resistance, vendor/database exposure, release promotion, or a defect in the unchanged actual 15-member incomplete release.

## 4. Authority classification and rationale

The request is **not** an `IN_SCOPE_REPAIR` under the unchanged detailed Plan.

PR03 Instruction v1.0 §7.3 preserves accepted PR02 admission and execution-provenance behavior and permits only a direct signature import adjustment that preserves those semantics. Detailed PR Implementation Plan v1.0 §14 explicitly classifies a change to accepted PR02 admission or execution-coherence behavior beyond direct import adaptation as a material boundary requiring a formal PR-30 `RESCOPE_REQUEST` and RS-20 disposition.

The proposed correction changes the accepted admission owner's covered executable-module set from four predecessor modules to eight total modules. That is a prospective expansion of the admission/execution-coherence contract, even though it is technically narrow and uses the existing owner. Treating it as an ordinary repair would disregard the Plan's explicit reservation.

The request is also **not** `SPECIFICATION_CHANGE_REQUIRED`. It preserves and strengthens the approved Specification's existing intent:

- one immutable, manifest-bound active configuration per release;
- fail-closed source/hash/release coherence;
- distinct source, configuration, manifest/release, and repository identities;
- pure computation with loading outside core; and
- no partial successful result when governing inputs are incoherent.

The immutable whole-change Plan already requires captured source identities and manifest-derived release identity to remain distinct and requires PR03 to consume the admitted bundle. The bounded overlay closes an integration gap between those two approved responsibilities without changing product objectives, mathematics, result fields, public behavior, exclusions, or later-unit ownership.

## 5. Approved bounded overlay

### 5.1 Production boundary

The PR03 engineer may extend only the existing private admission execution-provenance and executable-equivalence mechanism in `engine/config/registry_loader.py` so it covers exactly these additional owners:

1. `engine/core/core.py`
2. `engine/magic10/composite.py`
3. `engine/magic10/signals.py`
4. `engine/magic10/calculators.py`

The owning validation must:

- compare actual retained top-level module execution code objects with passive compilation of the exact captured, manifest-bound bytes;
- establish safe common source origin and compatible interpreter optimization/cache semantics through the existing owner;
- refuse unavailable or partial execution provenance, unsafe origin, incompatible compilation semantics, missing manifest binding, captured-source compilation failure, and executable mismatch before returning an admitted bundle;
- retain the current typed internal refusal ownership and avoid exposing new public/API/CLI failure fields;
- execute no captured source and perform no dynamic module reload;
- keep all file reads, source capture, compilation, and admission logic outside the pure four-argument core; and
- preserve the existing four PR02-covered owners and their accepted behavior.

The additional mechanics modules may retain only the passive, private top-level execution provenance needed by the existing admission owner. They may not become loaders, source readers, compilers, manifest owners, selectors, or independent validators.

### 5.2 Bounded files

Production changes are limited to:

- `engine/config/registry_loader.py`
- `engine/core/core.py`
- `engine/magic10/composite.py`
- `engine/magic10/signals.py`
- `engine/magic10/calculators.py`

Focused tests are limited to the existing applicable owners:

- `tests/config/test_production_admission.py`
- `tests/core/test_engine_core_determinism.py`
- `tests/core/test_engine_core_purity.py`
- `tests/config/helpers.py`, only if the existing synthetic complete-release fixture owner requires a bounded adaptation

Existing evidence may change only when source-identity changes require regeneration through:

- `tools/evidence/generate_engine_core_evidence.py`; and
- its already governed outputs and companions through `tools/evidence/update_evidence_index.py`.

No new evidence family or writer is authorized. A need for any production, schema, manifest, public, or evidence-owner file outside this boundary is a new material finding and is not silently absorbed.

### 5.3 Roster and identity limits

- The effective synthetic complete-release roster remains exactly 44 members. The four mechanics sources already belong to it; this overlay adds no roster member.
- The actual repository manifest remains exactly 15 members and remains incomplete. It is not refreshed or promoted by PR03.
- PR06 retains sole ownership of final actual 44-member materialization, complete identity recomputation, convergence, and promotion after PR03 through PR05.
- Any release/configuration/source identity change caused by the correction must be reported truthfully and regenerated only through the existing authorized writers. It does not itself authorize release promotion.

## 6. Requirements and acceptance effects

No Specification requirement or acceptance criterion is rewritten. This overlay strengthens implementation and evidence needed for existing requirements.

| Existing requirement / criterion | Approved effect |
| --- | --- |
| `K040-REQ-006`, `AC040-03` | The manifest-bound mechanics configuration cannot be treated as authoritative for PR03 execution when the newly active executing code is not equivalent to the captured source. |
| `K040-REQ-007`, `AC040-04` | The external loader/admission owner extends its fail-closed executable-equivalence check to the four PR03 mechanics owners while core remains pure. |
| `K040-REQ-008`, `AC040-04`, `AC040-09` | Non-equivalent, unavailable, unsafe-origin, partially initialized, or incompatibly compiled executing mechanics refuse without a successful labelled result or fallback. |
| `K040-REQ-009`, `AC040-05` | Release/source identities must remain attributable to the mechanics code that actually executes; manifest agreement alone is insufficient for the covered modules. |
| `K040-REQ-011`, `AC040-08` | Focused adverse tests cover coherently rehashed semantic changes after import for each of the four mechanics modules, plus equivalent-source success and provenance failure cases. |
| `K040-REQ-012`, `AC040-08` | Any affected governed evidence is regenerated only through its existing owner and required companions. |
| `K040-REQ-013`, `AC040-09` | The repaired candidate, review, CI, source, commit, request, review, addendum, and decision identities remain separately attributable. |

`K040-REQ-001`, `K040-REQ-002`, `K040-REQ-003`, `K040-REQ-004`, `K040-REQ-005`, and `K040-REQ-010` remain unchanged. The exact formulas, taxonomy, signal/category order, thresholds, caps, result schema, fingerprint preimage, pair preimage, serializer owner, and four-argument entrypoint remain unchanged.

## 7. Required implementation and proof after verified drain

The resumed PR03 engineer must complete all of the following before restoring `MERGE_PENDING`:

1. Preserve the current reproducer as the before-state failure and implement the approved owner-level correction in the same worktree, branch, and PR.
2. Prove that a syntax-valid semantic source change in each of the four newly covered modules is refused even after coherent fixture manifest/release regeneration.
3. Cover source replacement after import, equivalent captured/executing source at a supported separate fixture root, unavailable or partial provenance, unsafe common origin, incompatible optimization/cache semantics, captured compilation failure, and safe module-initialization ordering.
4. Prove that the correction executes no captured source, reloads no module, and does not add file, schema, environment, clock, network, database, vendor, cache, randomness, or process access to core/composite/signals/calculators computation.
5. Preserve the fixed G004 values and all existing classifier, signal, category, identity, immutability, AB/BA, determinism, malformed-input, threshold-refusal, PR02 admission, and actual-incomplete-release refusal tests.
6. Run the focused affected suites first, then the complete applicable local regression and governed writer/check set. Regenerate only actually affected evidence through existing writers. Preserve exact commands, environment, counts, outputs, source/commit identities, and limitations without summing overlapping test counts.
7. Obtain substantive code review of the corrected candidate and explicit disposition of PR03-R02. Obtain applicable security review of the actual corrected source.
8. Do not request or knowingly permit another hosted CI run while an applicable review defect remains open. After the corrected candidate passes local proof and substantive review, run the one required final exact-head CI and record the actual workflow/run/attempt/job/head outcome.
9. Return a truthful PR-30 implementation result under the original Proceed. `MERGE_PENDING` requires the corrected-source evidence, resolved review finding, and final exact-head CI; it is not established by the historical green runs.

The prior 592 focused passes, 1,822 default passes with three existing closed-rails vendor skips, 1,899 affected tests, governed evidence checks, reviews, and CI #3568/#3569 remain attributable historical evidence for their exact heads. They do not prove or approve the unimplemented correction.

## 8. Dependency and work-unit effects

| Work unit | Effect |
| --- | --- |
| PR01 / #403 | Accepted and final; no rerun, revision, or new obligation. |
| PR02 / #404 | Accepted and final; its original four-module execution-coherence coverage remains intact. No PR02 rerun or Plan revision. |
| PR03 / #405 | Remains `RESCOPE_PENDING` until manual PF10 drain and verification; then resumes in the same engineering session/worktree/branch/PR under the original Proceed. |
| PR04 | Scope unchanged. It must consume only a successfully admitted PR03 result whose release attribution satisfies this overlay. No application behavior moves into PR03. |
| PR05 | Scope unchanged. Golden/readiness evidence must exercise the accepted corrected PR03 behavior when its dependency becomes available. |
| PR06 | Scope unchanged. Retains final actual 44-member materialization, identity convergence, and promotion; may not promote a release whose covered mechanics execution/source equivalence fails. |
| PR07 and OPS01 | Scope and order unchanged. No early documentation, operations, deployment, or external verification is authorized. |

The ordered dependency chain remains PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01.

## 9. Alternatives and decision rationale

| Alternative | Decision |
| --- | --- |
| Extend the existing admission owner to the four newly active PR03 mechanics modules | **Approved.** It is the smallest complete correction that binds admitted source to the mechanics actually executing while preserving one loader/admission owner and a pure kernel. |
| Treat the issue as an ordinary PR03 repair | Rejected as a classification. It conflicts with Instruction §7.3 and detailed Plan §14, which expressly reserve changes to accepted PR02 execution-coherence behavior beyond direct import adaptation. |
| Read, compile, reload, or validate source inside pure core | Rejected. It violates the approved pure injected-kernel boundary and duplicates admission ownership. |
| Add a new loader, selector, validator, bundle field, schema field, public error, or calculator | Rejected. It creates a second authority or public/contract scope not required by the defect. |
| Accept coherent manifest/source hashes as sufficient | Rejected. The independent reproduction proves those facts can coexist with non-equivalent already imported execution while the result receives the altered release ID. |
| Reopen PR02, rewrite an approved Plan, obtain a replacement Proceed, or defer to PR06 | Rejected. These routes violate accepted-final lineage or leave the PR03 attribution defect unresolved. |

## 10. Preserved exclusions and nonclaims

This approval does not authorize:

- any change to PF01 mathematics, the 36-Channel taxonomy, profiles, weights, operations, caps, thresholds, band boundaries, signal/category order, schemas, result fields, fingerprint or pair-key formulas;
- a new public/API/CLI field, selector, error taxonomy, hidden bypass, duplicate owner, alternate calculator, remote schema, persistent cache, transport, narrative, UUID, application, or deployment behavior;
- source reads, source compilation, dynamic import, reload, environment access, time, randomness, network, database, vendor access, or mutable global state in pure computation;
- historical imported-source byte identity or universal runtime-integrity claims;
- stronger multi-file atomic visibility, cross-process locking, immutable deployment infrastructure, or arbitrary in-process tamper resistance;
- modification or promotion of the actual 15-member incomplete release;
- PR04–PR07 or OPS01 implementation, independent QA/Ops, deployment, release activation, PF10 editing by this IA, permanent Canon drainage, Epic acceptance, or Epic closure;
- a replacement branch, PR, worktree, session, instruction, Plan, Proceed, accepted-work rerun, or agent merge.

## 11. Complete carried Canon-conflict register

| ID | Classification and decision | Preserved effect and remaining owner |
| --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION / APPROVED` by Thoth-17 at `2026-09-08T13:23:24Z` | Preserve explicit Done exclusions and current PF09.3 agreement. Source correction resolved; no new decision. |
| `C040-02` | `CANON_RECONCILIATION / APPROVED` by Thoth-17 at the same decision time | Current PF12 controlled Markdown governs; historical identity mismatch remains history only. |
| `C040-03` | `CANON_RECONCILIATION / APPROVED` by Thoth-17 at the same decision time | Current PF14 controlled Markdown governs; C040-05 separately controls superseded core-test text. |
| `C040-04` | `CANON_RECONCILIATION / APPROVED` by Thoth-17 at the same decision time | QA identity history remains preserved; PR03 engineering proof is not independent QA. |
| `C040-05` | `CANON_RECONCILIATION / APPROVED`, alternative A, by Isis-49 at `2026-09-09T03:57:16Z` | The four-argument Gate kernel supersedes the precomputed-score/CoreConfig path. Permanent PF14 §6.7 maintenance remains with its governed maintainer and is non-gating. |
| `C040-06` | `NEW_CANON / APPROVED`, alternative A, by Isis-50 at `2026-09-09T11:48:08Z` | Preserve the approved 36-row taxonomy and 16-case conformance. Permanent PF12/PF01 maintenance remains with governed maintainers and is non-gating. |

PR02 F01/F02/F03 remain approved and drained only for PR02. This PR03-R02 approval is a separate bounded overlay and does not reopen, reinterpret, relabel, omit, or expand those decisions.

## 12. Repository, recovery, and unresolved owners

| Item | Preserved state / owner |
| --- | --- |
| Repository and PR | `amthorn78/glow-hdengine-v2`; [PR #405](https://github.com/amthorn78/glow-hdengine-v2/pull/405) remains open, non-draft, and unmerged. |
| Baseline | Head `5b2fb8d70924a6710b6261fc0c93d3869fed6380`; tree `e43c2063599e7bc449f20d4ab045d32d95581bf4`. |
| Current PR03 candidate | Head `b33c41721ad2320f71c2cdaf00616e27d36945da`; tree `4af351d6f7347541b9853927bf5098299adcc81f`. |
| Engineering state | Worktree `/workspace/scratch/808bf6c1dac3/pr03`, branch `hde-epic040-pr03-pure-gate-core`, clean before and after independent reproduction. |
| PR03-R02 | Reproduced and open at [discussion 4004034876](https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4004034876). Correction, tests, review disposition, and final CI remain owned by the same PR03 engineer after verified drain. |
| Current CI | Run #3569 passed on `b33c4172`, but it does not cover the unimplemented correction and does not establish merge readiness. |
| Manual PF10 drain | Pending. Nathan / Product Owner owns insertion and verification of the exact accompanying addendum. |
| Merge | Not authorized or performed. Nathan retains any later manual merge decision after genuine renewed merge readiness. |
| Repository prompt-use persistence | Pending/non-gating for an authorized writer under an actually installed supported procedure. No procedure or destination is invented here. |

No implementation work is discarded. The current same worktree, branch, PR, request evidence, reproducer, commit history, test evidence, review history, CI history, and original Proceed remain intact.

## 13. Prompt-use record

`GCFPE_PROMPT_USE: GCFPE-USE-HDE-EPIC040-RS-20-20260914-PR03-R02-01; change HDE-EPIC040; work unit HDE-EPIC040-PR03; request HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0; prompt RS-20 — Review Bounded Work-Unit Rescope — 091326.2; Notion page 3da4590a-05eb-81d3-adf1-ecac218d0beb; retrieved page revision 2026-09-13T11:33:42.943Z; ecosystem GCFPE-20260913.1; role retained Product Owner-assigned whole-change HDE-EPIC040 Implementation Architect; execution posture MANUAL_PROMPT_EXECUTION; decision APPROVE; capture 2026-09-14T10:34:33Z.`

Preserve the earlier PR-10, PR-20, and PR-30 prompt-use records in the instruction, detailed Plan, and implementation result. This RS-20 use does not claim RS-40 execution, PF10 drainage, implementation, review resolution, CI, merge, QA, Ops, release, or closure.

## 14. Approval package and native return

This review approves exactly one bounded overlay and therefore produces exactly one standalone PF10 build-notes addendum:

- `HDE-EPIC040-PR03-R02-PF10-BUILD-NOTES-ADDENDUM v1.0`
- State: `READY_FOR_MANUAL_DRAIN`
- Canonicality: `NON_CANONICAL_PENDING_MANUAL_DRAIN`
- Drain owner: Nathan / Product Owner
- Direct Drive link: https://drive.google.com/file/d/1AKBfTpnV3C6jALe18COqDFadk2DplVb7/view?usp=drivesdk

The addendum is page-ready as PF10 §2.12. This IA has not edited PF10 or asserted drainage. The approved overlay cannot be used for repository correction until Nathan has manually drained the exact addendum into the current controlled PF10 Markdown and verified that the complete substantive section was preserved.

After that verified manual prerequisite, the selected native return is `RS-40 — Approved Rescope — Resume PR Implementation — 091326.2` to the same dedicated PR03 engineering session, same worktree, branch, PR, and original Proceed. No new Proceed is required or created.

## 15. Conditional direct native handoff

```plain text
NEXT_PROMPT_HANDOFF

Run RS-40 — Approved Rescope — Resume PR Implementation — 091326.2 only after Nathan / Product Owner has manually drained and verified the exact approved addendum below:
https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3?pvs=204

Continue as the same dedicated PR engineering session for HDE-EPIC040-PR03. Preserve the existing session, worktree, branch, PR, commits, tests, reviews, CI history, reproducer, and original Product Owner Proceed. Do not repurpose the retained whole-change IA, Isis-50, or the accepted PR01/PR02 sessions.

EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: dedicated PR engineering session for HDE-EPIC040-PR03
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR03 / RS-40 / PR03-R02
context_conflict: NONE
lifecycle: EXISTING_OPEN_PR_IMPLEMENTATION
originating_stage: PR-30
original_PO_PROCEED: PRESERVED

Manual prerequisite:
- Nathan / Product Owner must first drain the complete page-ready §2.12 body from the approved addendum into the current controlled PF10 Markdown and verify substantive equality.
- Do not rely on the overlay or resume implementation until Nathan supplies that completed-drain assertion.

Approved decision package:
- RESCOPE_REQUEST: HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0
  https://drive.google.com/file/d/1Cg6LglLhgqPVrHr6uL374kkdiP2Zqzu6/view?usp=drivesdk
- RESCOPE_REVIEW: HDE-EPIC040-PR03-RESCOPE-REVIEW-01 v1.0, APPROVE
  https://drive.google.com/file/d/1QygaPftN2OnucTvZgMPtpKn5eCemXUyE/view?usp=drivesdk
- PF10_BUILD_NOTES_ADDENDUM: HDE-EPIC040-PR03-R02-PF10-BUILD-NOTES-ADDENDUM v1.0
  status: READY_FOR_MANUAL_DRAIN
  canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN until Nathan's verified insertion
  drain_owner: Nathan / Product Owner
  https://drive.google.com/file/d/1AKBfTpnV3C6jALe18COqDFadk2DplVb7/view?usp=drivesdk
- Current controlled PF10 before this drain: PF10-HDE-Build-Notes-v13.2.4.md
  https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk

Preserved PR03 authority and records:
- PR Instruction v1.0, INSTRUCTION_READY:
  https://drive.google.com/file/d/1Zj5BResRRxtGarmZ2d3sIAfIVeLD42rs/view?usp=drivesdk
- Detailed PR Implementation Plan v1.0; original Proceed remains valid:
  https://drive.google.com/file/d/1wPpcIQkDLVNwdvK2ujfDpkssUh4KwAoO/view?usp=drivesdk
- PR Implementation Result v1.1, RESCOPE_PENDING:
  https://drive.google.com/file/d/1UZZYqgpVrbraGMGrlOFnPwGqFCUp4ZmF/view?usp=drivesdk
- Session Completion and CI Control RCA v1.1:
  https://drive.google.com/file/d/1EOOqIiuaVxPv42Oh9sf3kxNF0WhmC2NK/view?usp=drivesdk

Immutable approved lineage:
- Specification v1.1, Thoth-17 APPROVE:
  https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk
- Implementation Audit v2.0, AUDIT_COMPLETE:
  https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk
- Whole-change Implementation Plan v2.1:
  https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk
- Approving Plan Review v2.1, Isis-50 APPROVE:
  https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk
- Accepted PR01 lineage review v1.1:
  https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk
- Accepted PR02 lineage review v1.0:
  https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk

Repository continuity:
- Repository: amthorn78/glow-hdengine-v2
- Target: main
- Baseline head/tree: 5b2fb8d70924a6710b6261fc0c93d3869fed6380 / e43c2063599e7bc449f20d4ab045d32d95581bf4
- Worktree: /workspace/scratch/808bf6c1dac3/pr03
- Branch: hde-epic040-pr03-pure-gate-core
- PR: https://github.com/amthorn78/glow-hdengine-v2/pull/405
- Current head/tree: b33c41721ad2320f71c2cdaf00616e27d36945da / 4af351d6f7347541b9853927bf5098299adcc81f
- PR03-R02: https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4004034876
- PR remains open, non-draft, and unmerged. Worktree is clean. No source correction has been applied.

Approved bounded correction:
- Extend the existing engine/config/registry_loader.py passive execution-provenance and executable-equivalence owner to exactly engine/core/core.py, engine/magic10/composite.py, engine/magic10/signals.py, and engine/magic10/calculators.py.
- Compare actual retained top-level execution code with passive compilation of exact captured, manifest-bound bytes before returning an admitted bundle.
- Fail closed for unavailable/partial provenance, unsafe origin, incompatible compilation semantics, missing manifest binding, captured compilation failure, or executable mismatch.
- Preserve the existing four PR02-covered owners, safe common-origin checks, typed internal refusals, captured-byte discipline, one loader/admission owner, and all accepted tests.
- Keep all loading, file reads, source capture, and compilation outside pure core. Do not execute captured source or reload modules.
- Add focused adverse and success tests through the existing test and synthetic-fixture owners. Regenerate only actually affected governed evidence through existing writers.

Unchanged constraints:
- Preserve the four-argument kernel, mathematics, taxonomy, signal/category order, caps, thresholds, schemas, result fields, fingerprint/pair identities, serializer owner, actual 15-member release, and effective synthetic 44-member roster.
- PR01/#403 and PR02/#404 remain accepted-final. Do not reopen, rerun, or revise them.
- PR02 F01/F02/F03 overlays grant no additional PR03 scope.
- Do not create a loader, selector, alternate calculator, public/API/CLI field, schema/bundle field, persistent cache, remote schema, deployment protocol, stronger atomicity guarantee, or arbitrary tamper-resistance claim.
- Do not enter PR04–PR07 or OPS01 scope, perform QA/Ops/deployment, contact live vendors/databases, edit PF10, promote a release, merge, or close the Epic.
- Preserve C040-01 through C040-06 and their existing decisions and maintenance owners.

Required action after verified drain:
Implement only the approved correction in the same PR03 worktree/branch/PR under the original Proceed. Prove the current failure first, repair it, run the focused adverse/equivalent-source/provenance/purity tests and applicable full local validation, regenerate only affected governed evidence through its owners, obtain substantive corrected-source code and applicable security review, resolve PR03-R02 through the repository reviewer, then run final exact-head CI once. Return the complete truthful PR-30 implementation result and genuine merge-readiness state. Do not discard existing work or execute a merge.

Expected output:
A resumed and read-back HDE-EPIC040-PR03 PR_IMPLEMENTATION_RESULT for the same PR lifecycle, with exact corrected commit/tree, local test/evidence results, review dispositions, final exact-head CI evidence, unresolved items, and either genuine MERGE_PENDING or the exact native boundary return. No replacement Proceed, branch, PR, Plan, accepted-work rerun, PF10 edit, merge, QA/Ops, release activation, or Epic closure.
```

ASK OK.
