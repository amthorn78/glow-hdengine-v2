# HDE-EPIC040-PR02 — Bounded Work-Unit Rescope Proposal v1.0

## 1. Artifact identity and pending state

| Field | Exact value |
| --- | --- |
| Artifact | `RESCOPE_PROPOSAL` / `HDE-EPIC040-PR02-RESCOPE-PROPOSAL` / v1.0 |
| `RESCOPE_PROPOSAL_ID` | Assigned only by the required ChatGPT Library save result; no provider identity is invented inside the artifact |
| State | `RESCOPE_PROPOSAL_PENDING_REVIEW` |
| Change class / change | `EPIC` / `HDE-EPIC040` — Separation Pass 3 |
| Work unit | `HDE-EPIC040-PR02` — Strict immutable input and admission boundary |
| Originating stage | `PR-30` |
| Originating result | `HDE-EPIC040-PR02-PR-IMPLEMENTATION-RESULT` v1.0 / `RESCOPE_PENDING` |
| Primary finding | `HDE-EPIC040-PR02-F01` |
| Suspended boundary | PR02 active-admission engineering completion, review closure, exact-final-head CI eligibility and merge readiness |
| Execution posture | `MANUAL_PROMPT_EXECUTION` |
| Ecosystem | `GCFPE-20260912.1` |
| Author role | Product Owner-assigned HDE-EPIC040-PR02 bounded finding author for RS-10; no approval authority |
| `session_disposition` | `INITIAL_DEDICATED_ASSIGNMENT` |
| `role_session_ref` | This explicitly assigned RS-10 finding-author conversation; no platform session ID is asserted |
| `invocation_binding` | `EPIC / HDE-EPIC040 / HDE-EPIC040-PR02 / PR-30 / HDE-EPIC040-PR02-F01 / create one bounded pending proposal` |
| `context_conflict` | `NONE` |
| Continuing implementation session | Existing dedicated engineering session named `PR-02 HDE-EPIC040`; retain, do not replace |
| Whole-change review continuity | Existing HDE-EPIC040 IA for RS-20; continuing Isis-50 for any later IA-30 correction intake and return review |
| Storage classification | `EPHEMERAL_LIBRARY`; intended Library directory `/Glow HDE 3.0`; never Google Drive |
| Capture time | `2026-09-12T20:46:48Z` |

This is a proposal, not a rescope approval. It does not authorize implementation, a roster change, repository mutation, a push, CI, review-thread resolution, merge, PF10 publication, QA, Ops, release promotion or downstream work.

## 2. Requested decision and recommendation

### 2.1 Primary decision

`HDE-EPIC040-PR02-F01` is a genuine bounded work-unit rescope within the already approved HDE-EPIC040 Specification intent. The approved delivery requires both:

1. exact admission against the approved 41-member roster; and
2. execution of the Gate Catalog's actual owning schema from the same captured, manifest-bound release.

Those duties cannot both be met because `schemas/gates_v1.schema.json` is absent from the exact 41-member roster. The evidence proves that the current implementation can admit a synthetic complete release without executing that schema, while adding the schema as member 42 is rejected as a roster mismatch.

The recommended smallest complete correction is to authorize `schemas/gates_v1.schema.json` as one additional captured, manifest-bound required release member; change the exact admitted roster from 41 to 42; execute the existing owning Gate validator; add the corresponding adverse evidence; and reconcile the exact whole-change roster and PR06 manifest-promotion obligation.

This preserves the approved Product objective, selected HDE-SEPA005 scope, public and FE/BE promises, topology semantics, schema semantics and exclusions. It changes an approved implementation contract and therefore requires a complete successor to whole-change Implementation Plan v2.1 before corrected implementation can resume.

### 2.2 Companion decision on loaded-module/source coherence

Corrected-head review thread `3997351898` establishes a separate real ambiguity. A non-symlink source root can change after Python imports the admission modules. The current loader may then record new on-disk manifest identities while earlier imported module code remains the code actually executing.

This is not safely absorbable as an undocumented ordinary repair. The approved Plan requires one manifest-bound active configuration and distinct source identities, but it does not define what executing code is bound, when its identity is captured, or how a mismatch must refuse without creating a selector or deployment protocol. The recommended classification is `BOUNDED_PLAN_CLARIFICATION_REQUIRED`, within approved Specification intent, coupled into the same Plan-correction package as F01.

The corrected Plan must require a fail-closed coherence predicate for the PR02 code that actually performs admission and Gate normalization: an active handle may not be returned when the executing imported implementation cannot be shown to correspond to the manifest-bound source identities it claims. The IA must define the smallest local mechanism and its limits. It must not silently add a caller selector, hidden configuration authority, dynamic deployment protocol, cross-process coordination or unmanifested source. If a viable correction would require immutable-deployment infrastructure or a new product/operational promise, that portion must stop and return to Product Owner and Specification authority instead of being absorbed here.

### 2.3 Whole-change and Specification classification

| Question | Proposal conclusion |
| --- | --- |
| Genuine bounded rescope? | Yes for F01 and for the loaded-module/source coherence clarification. |
| Within approved Specification intent? | Yes, provided the module-coherence remedy remains a local fail-closed implementation contract and creates no new public, deployment or operational promise. |
| Must whole-change Implementation Plan v2.1 change? | Yes. Its exact promoted schema set and PR02/PR06 release contract omit the owning Gate schema, and its execution/source-coherence boundary is not sufficiently specified. |
| Must the approved Specification change? | No change is proposed. Objectives, outcomes, selected/excluded units, public promises and schema semantics remain unchanged. |
| Does this proposal authorize 41→42 or code work? | No. RS-20 review, the manual Product Owner/PF10 rescope disposition, and the actual Plan-correction route must complete first. |

## 3. Exact approved and in-flight lineage

| Role in lineage | Exact artifact and state |
| --- | --- |
| Approved Specification | `SPECIFICATION_ID=libfile_12bab860949c8191881510875f051460`; HDE-EPIC040 Specification v1.1; Thoth-17 `APPROVE`; decision `2026-09-08T13:23:24Z` |
| Fresh whole-change Audit | `IMPLEMENTATION_AUDIT_ID=libfile_823ee8e9ecb0819185181ec7695265fb`; v2.0; `AUDIT_COMPLETE` |
| Effective whole-change Plan | `IMPLEMENTATION_PLAN_ID=libfile_11c992cda3f0819199827e86584e41f1`; v2.1; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| Effective Plan approval | `PLAN_REVIEW_ID=libfile_b85b81651a508191abdfd8f81803caf8`; v2.1; Isis-50 `APPROVE`; decision `2026-09-09T13:36:43Z`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Accepted PR01 dependency | `libfile_47bf2e063d208191bf57f93c71f96821`; HDE-EPIC040-PR01 lineage review v1.1; `ACCEPT`; SHA-256 `f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273`; merged PR `#403` |
| PR02 instruction | `PR_INSTRUCTION_ID=libfile_40f6b1d402808191b484e5929a6afcca`; v1.0; `INSTRUCTION_READY`; SHA-256 `429cda8e7f00bedc0509e9d00a16c72b37a49f5592054b2b8e069308e812047c` |
| PR02 detailed Plan | `PR_IMPLEMENTATION_PLAN_ID=libfile_4c88da46f3d08191a38e18f7de652fd4`; v1.0; saved `AWAITING_PO_PROCEED`; actual Product Owner decision `PROCEED`; SHA-256 `496488109e3fc080dd238145f28edf0a0824b5bb1ff068432e209813df9998e0` |
| PR02 implementation Result | `PR_IMPLEMENTATION_RESULT_ID=libfile_c20e76fad8448191af852e9f7bf15d27`; v1.0; `RESCOPE_PENDING`; file `HDE-EPIC040-PR02-pr-implementation-result-v1.0.md`; file ID `file_0000000082688210a9df5cb23b147f8b`; SHA-256 `779c425ba72c7df142f7ba1806ad1489785eb90de46493dac408e31bf53004e0` |
| Existing rescope proposal | `NOT PRODUCED` before this RS-10 invocation |
| Existing rescope review | `NOT PRODUCED` |
| Governing Plan correction instruction | `NOT PRODUCED` |
| Product Owner/manual PF10 rescope disposition | `NOT PERFORMED` |

Historical HDE-EPIC040 Implementation Plan v1.0 and its v1.0 review remain invalidated source-failure records. Neither is used as authority or revived by this proposal.

## 4. Approved Strategy Card preserved unchanged

The approved Specification's single Strategy Card remains the only Strategy source.

### `outcome_fire`

- **Outcome:** After this change, the selected production Magic10 mechanics configuration contract is implemented as one coherent, deterministic, release-bound capability spanning the corrected catalog, strict default configuration, fail-closed loading, identity/comparison and governed verification.
- **Success signal:** Exact-source evidence decides every §11 criterion against the actual candidate and all thirteen kickoff requirements, without using prior token claims or document presence as implementation proof.
- **Scope line:** HDE-SEPA005 and its five selected subtasks only; the other twenty-nine PF09.3 units remain Done/context. PF09.3 v1.1.4 is outside the selected baseline.

### `surface_water`

- **Surface statement:** One governed production mechanics configuration and its already-governed internal FE/BE projections; no second public compatibility surface.
- **Promise check:** Preserve the existing public Reader's bands-only, numeric-free covenant, non-scoring Product metadata and FE/BE bundle compatibility. No public category expansion, payload extension or alternate configuration selector is authorized.
- **Minimal contract phrase:** One trusted release configuration supplies validated mechanics inputs and governed result contracts; consumers and evidence tools use projections, not competing authorities.

### `boundary_air`

- **Contract name:** Production Magic10 mechanics configuration contract.
- **Evolution posture:** Implement the current adopted configuration contract rather than retune it. Preserve current bundle schema identities and consumer promises. Where legitimate dependency regeneration is needed, it must reflect the governed source change without silently changing the consumer contract. A genuinely incompatible migration, structural mechanics change or new public promise requires its actual owner before execution; no coexistence period or migration mechanism is invented here.
- **Data posture:** Only the governed catalog, categories, caps, thresholds, source identities, immutable configuration/release identity, result schemas and bounded comparison evidence are needed. Identity or request metadata, viewer preferences, clocks, prose and mutable configuration handles must not become intrinsic operands. Exact allowed fields and values remain in the owning Canon.

### `stewardship_earth`

- **Ownership:** Master Scrum owns the kickoff. Isis-49 is the continuing Specification author selected by the Product Owner. The continuing Thoth reviewer owns approval or denial; IA, QA, authorized environment operators and the governed PF09 owner retain their later duties.
- **Phase signals:** Entry is the complete KICKOFF_READY handoff and the PO's selected class, identity, source and disposition. This authoring output is complete but SPECIFICATION_PENDING; its immediate destination is independent Thoth review through Analyzer middleware. Approval alone permits mandatory IA-10 audit-then-plan preparation, not implementation.
- **Safety note:** Invalid, ambiguous, stale, hash-mismatched or release-incoherent configuration produces no successful mechanics result. Comparison and current-row readiness remain read-only. Rollback is one complete compatible prior release, never mixed code/configuration/schema identities. No rollback or deployment is executed or authorized by this document.

Current application note, separate from the unchanged Card: PR01 is accepted and merged; PR02 is preserved in draft PR #404 at `RESCOPE_PENDING`; this RS-10 artifact requests review of a bounded Plan correction. The Card is carried verbatim, including its historical formation-phase Analyzer sentence; the current RS-10 contract uses direct native handoff and requires no Analyzer step. The proposed correction strengthens the already approved one-release, fail-closed, exact-source contract and changes no Strategy dimension. A remedy requiring a new deployment guarantee would change `boundary_air` and must use the Product Owner/Specification path rather than this bounded proposal.

## 5. Repository baseline and preserved work

| Evidence | Exact value |
| --- | --- |
| Repository | `amthorn78/glow-hdengine-v2` |
| PR | `#404`; open, draft, unmerged |
| Branch | `hde-epic040-pr02-immutable-admission` → `main` |
| Accepted base | `3828d4b3454259841a3e48d13039dd1475754f2f` |
| Base tree | `529306a74268f2a46765bf40defdae49026d103e` |
| Initial PR02 commit | `3dda87853466fa18247654ffe5bb67561364b0f4` |
| Initial tree | `083a787c16a06328622cde0ca93f22508f16146b` |
| Corrected current head | `eed8a63807f573abc29de6f6d5ceac54f0c8da85` |
| Corrected tree | `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d` |
| Current change set | 9 files; 1,305 additions; 27 deletions |
| Actual current release manifest | Unchanged 15-member manifest; active admission refuses it with `INCOMPLETE_RELEASE_ROSTER` |

The attributable lineage is base → `3dda8785…` → `eed8a638…`. The original recovered workspace remains preserved unchanged. The separate attributable reconstruction, draft PR, both commits, current review evidence and historical CI remain valid evidence. They must be reused, not replaced, discarded or rewritten as synthetic accepted lineage.

Synthetic 41- or 42-member fixtures are test evidence only. They are not production conformance, current-manifest promotion, release activation or permission to edit the actual 15-member manifest.

The nine attributable changed paths are `ci/checks/classify_ci_changes.py`, `engine/bodygraph/gates.py`, `engine/config/registry_loader.py`, `pytest.ini`, `tests/bodygraph/test_gates.py`, `tests/config/helpers.py`, `tests/config/test_manifest_schema.py`, `tests/config/test_production_admission.py` and `tests/evidence/test_rails_ci_workflow_integration.py`.

### 5.1 Review and CI chronology preserved

| Evidence | Exact status |
| --- | --- |
| Initial code reviews | Reviews `5187749091` and `5187749601`; both supplied code findings rather than acceptance |
| Corrected-head code review | Review `5187778352`; commit `eed8a63807`; completed `2026-09-12T19:49:24.108800Z`; three P1 findings retained |
| Dedicated security review | Comment `5648272341`; commit `eed8a63807`; completed `2026-09-12T19:48:23.633602Z`; no security issues found; not a waiver of code findings |
| Historical exact-head CI | Workflow `.github/workflows/ci.yml`, ID `192291018`; run `34715034846`, number `3565`, attempt `1`; check suite `94030719315`; job/check `103610646326`; exact head `eed8a63807f573abc29de6f6d5ceac54f0c8da85`; success |
| CI terminal evidence | All seven applicable lanes passed; marker `CI_APPLICABILITY_AND_EXACT_HEAD_OK` at `2026-09-12T19:56:04.3970662Z`; run completed `2026-09-12T19:56:07Z` |

All seven review threads remain unresolved in the captured evidence. Historical green CI and the no-findings security result do not satisfy merge readiness while code-review blockers remain, and neither can be reused as final proof after another code change.

## 6. Evidence-supported cause

### 6.1 Controlling contract collision

1. Detailed PR Plan v1.0 §5.3 fixes the admitted release at exactly 41 paths and rejects missing or extra members. Its complete roster omits `schemas/gates_v1.schema.json`.
2. Detailed PR Plan §5.2 permits local schemas only when captured and roster-authorized.
3. Detailed PR Plan §5.4 requires the existing actual schema and shared relational implementation, not a duplicate validator.
4. PR Instruction §6 item 5 requires execution of actual local closed schemas; §4 prohibits an alternate validator.
5. Approved whole-change Plan v2.1 §5.5 requires actual owning schemas and exact manifest-bound admission. Its §5.10 exact promoted schema set also omits `schemas/gates_v1.schema.json`.
6. Current controlled PF12 v2.9.6 §2.1 identifies `schemas/gates_v1.schema.json` as the Gate Catalog's owning declarative schema. PF12 §3.1 requires a catalog with an owning schema to validate against it.
7. Detailed Plan §12 explicitly treats a changed approved final roster/manifest identity as a material boundary requiring RS-10/RS-20 rather than implementation improvisation.

### 6.2 Current implementation behavior

The corrected head calls `_load_gates(capture, validate_schema=False)` and documents that the Gate schema is bypassed because it is outside the exact roster. The existing `_load_gates` implementation otherwise calls `_validate_local_schema(capture, 'schemas/gates_v1.schema.json', raw)` when schema validation is enabled. The active path therefore possesses an owning validator but intentionally does not execute it.

### 6.3 Read-only substantiation

| Probe | Observed result |
| --- | --- |
| Exact 41-member fixture with owning Gate schema absent | Current active pipeline returns `AdmittedMechanicsBundle` |
| Same condition through existing schema-enabled Gate validator | Refuses with `MISSING_FILE` |
| Canonical reject-all Gate schema present but unlisted | Current active pipeline still returns a bundle |
| Same reject-all schema through existing schema-enabled validator | Refuses with `SCHEMA_VALIDATION_FAILED` |
| Gate schema added as manifest member 42 | Refuses with `RELEASE_ROSTER_MISMATCH` |
| Unchanged actual repository release | Refuses with `INCOMPLETE_RELEASE_ROSTER` |

The repository Gate schema was unchanged and had SHA-256 `b3308ca513a1f3e4490ce6c526124675fad1fdcdb5c6abce7257af99d76ed13a` in the captured evidence. The controlled PF12 predicate was established through the exact direct folder chain Glow `1MZXcC5tKMkI9n8EobkywIj1ifcF6IvZ3` → Core Docs `18T84WC_Jxjb75V37_eYcRqn8zOjHYgxu` → PFCanon `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3`, selecting PF12 v2.9.6 file `1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ` as its direct controlled Markdown child.

The observed contradiction is structural. Passing tests, a green CI run, a no-findings security result, a handwritten validation subset or a synthetic fixture cannot resolve it.

## 7. Smallest complete bounded delta

Subject to RS-20 approval and the required downstream authority sequence, the corrected governing package should do all of the following as one coherent delta:

1. Add `schemas/gates_v1.schema.json` to the exact promoted and admitted source set.
2. Reconcile the approved exact admitted roster from 41 to 42 paths while keeping the manifest itself excluded.
3. Require that the Gate schema be captured from the same selected root, listed in the same manifest, hash/size checked from the same owned bytes, resolved only through local captured references, and covered by final unchanged-source verification.
4. Execute the existing owning Gate schema validator in the production admission path. Preserve the shared relational Gate/Channel/Center checks as additional closure; do not replace schema execution with handwritten equivalence.
5. Preserve the actual 15-member manifest unchanged in PR02. PR06 remains the owner of final manifest materialization and release convergence after PR03–PR05; its corrected obligation becomes the approved 42-member complete roster if that change is ultimately authorized.
6. Add positive and adverse tests proving the owning schema actually governs admission: absent schema, unlisted schema, reject-all/invalid schema, remote/local-reference escape, schema hash/size mismatch, changed schema bytes, missing/extra roster members and unchanged incomplete actual release refusal.
7. Add a Plan-level source/execution-coherence predicate for directly executing PR02 admission code. Require fail-closed behavior when an executing imported implementation cannot be tied to the manifest-bound source identity it claims. The corrected Plan must name the bounded code set, capture point, comparison point, refusal behavior and evidence limit without introducing a new public selector, hidden authority or deployment protocol.
8. Preserve the explicit lack of any process-death atomicity, multi-file atomic visibility or cross-process locking guarantee. The source/execution clarification must not be used to smuggle in that stronger guarantee.
9. Correct the affected whole-change Plan first. Then create complete successor PR02 instruction and detailed Plan artifacts, carry the preserved PR #404 lineage, and obtain a new exact Product Owner Proceed for the changed implementation contract before the dedicated PR02 engineer acts.
10. When engineering resumes, batch the authorized schema/coherence work with the ordinary manifest-single-read repair; validate locally; obtain substantive corrected-code and security review; resolve applicable findings; and only then run CI once on the exact final PR head.

No new Gate topology, scoring rule, schema vocabulary, public field, caller-supplied root, caller configuration, fallback, network resolution, database/vendor behavior, current release promotion or second validator is proposed.

## 8. Finding-by-finding authority classification

| Finding / evidence | Current factual status | Authority classification and destination |
| --- | --- | --- |
| Owning Gate schema bypass — threads `3997320377`, `3997320916`; replies `3997326039`, `3997326077` | Open material blocker; independently reproduced; current active path disables the owning schema | `BOUNDED_WORK_UNIT_RESCOPE_WITHIN_APPROVED_SPECIFICATION`; include as F01 in RS-20. Requires whole-Plan correction and later corrected PR artifacts before engineering. |
| Deployment symlink defect — thread `3997320380`; reply `3997339517` | Ordinary defect corrected in `eed8a638…`; original thread remains unresolved and outdated; corrected review found a distinct module-coherence issue | `ORDINARY_IN_SCOPE_REPAIR_COMPLETED_PENDING_FINAL_REVIEW_DISPOSITION`; no new rescope. Preserve and re-review on the eventual exact corrected head. |
| Earlier-source mutation during verification — thread `3997320917`; reply `3997339568` | Ordinary inter-read race corrected in `eed8a638…`; original thread remains unresolved; the remaining post-final-observation window is separate | `ORDINARY_IN_SCOPE_REPAIR_COMPLETED_PENDING_FINAL_REVIEW_DISPOSITION`; no new rescope. Preserve explicit atomicity limit. |
| Packaged manifest physically read twice — thread `3997351895`; reply `3997361338` | Open ordinary implementation defect; final verification rereads cached manifest path | `ORDINARY_IN_SCOPE_REPAIR`; stays with the existing dedicated PR02 engineer after governing rescope approval. Add an adverse physical-read-count proof. |
| Executing imported modules not bound to admitted source bytes — thread `3997351898`; reply `3997361375` | Open, independently reproduced design ambiguity; current source has no import-time execution-identity comparison | `BOUNDED_PLAN_CLARIFICATION_REQUIRED` within approved intent, subject to RS-20. Include in the same Plan-correction package. Escalate only if the remedy requires a new deployment/product promise. |
| Requested atomic final multi-file source boundary — thread `3997351903`; reply `3997361287` | Residual ordered-check window is real; current detailed Plan expressly disclaims multi-file atomic visibility and cross-process locking | `REVIEWER_REQUEST_CONFLICTS_WITH_EXPLICIT_APPROVED_LIMITATION`; no implementation repair or bounded delta is recommended. RS-20 should preserve the limitation. A stronger guarantee would require separate Product Owner and applicable Specification/architecture authority. |
| Dangling local schema reference self-review | Corrected before initial publication; regression tests pass | `ORDINARY_IN_SCOPE_REPAIR_COMPLETED`; preserve in evidence; revalidate after later changes. |
| Writable frozen-record dictionaries / retained aliases | Corrected in `eed8a638…`; traversal and alias tests pass | `ORDINARY_IN_SCOPE_REPAIR_COMPLETED_PENDING_FINAL_REVIEW_DISPOSITION`; preserve in eventual re-review. |
| Dedicated security review comment `5648272341` | No security issues reported for `eed8a638…` | Evidence only, not acceptance or waiver. A changed head requires applicable final security review. |

No thread is marked resolved by this proposal. No completed repair is called accepted merely because its current tests pass or a later review identified different issues.

## 9. Requirements, acceptance and dependency impact

### 9.1 Changed implementation allocation; requirement intent unchanged

F01's exact source-identified impact is `K040-REQ-003`, `K040-REQ-006`, `K040-REQ-007`, `K040-REQ-008`, `AC040-04` and `AC040-07`. The separate loaded-module/source clarification additionally touches the identity and no-partial-release allocations identified below; that companion mapping does not enlarge F01's original recorded set.

| Requirement / criterion | Impact of proposed correction |
| --- | --- |
| `K040-REQ-003` | Gate/Channel schema conformance becomes demonstrably enforced through the actual owning Gate schema in the admitted release. Requirement text and topology semantics remain unchanged. |
| `K040-REQ-006` | The authoritative immutable manifest-bound configuration includes its Gate owning schema; projections remain non-authoritative. Requirement text remains unchanged. |
| `K040-REQ-007` | Actual owning-schema execution and source/execution coherence become explicit prerequisites to returning the immutable typed bundle. No second validator is created. |
| `K040-REQ-008` | Missing, unlisted, invalid, changed or identity-incoherent owning schema/executing source must fail without a partial handle or fallback. |
| `K040-REQ-009` | The Plan must distinguish captured disk source identities from the code actually executing admission, while preserving config, source, release and repository identities as separate facts. |
| `AC040-04` | PR02's schema-loaded immutable admission proof must include the owning Gate schema and the approved execution-coherence boundary. |
| `AC040-05` | PR02 source identity and PR06 complete manifest identity remain coherent after the roster correction; no current release claim is introduced. |
| `AC040-07` | Existing shared normalization and strict refusal remain; schema bypass cannot count as successful shared validation. |
| `AC040-09` | No-partial-release and boundary behavior remain intact; no new public or caller-selected surface is permitted. |

`K040-REQ-001`, `002`, `004`, `005`, `010`, `011`, `012` and `013`, and `AC040-01`, `02`, `03`, `06` and `08`, retain their approved text, owners and completion burdens. Their evidence may need regenerated or rerun only where the eventual authorized code change actually affects it.

### 9.2 Work-unit and dependency impact

| Unit | Impact |
| --- | --- |
| PR01 | Accepted dependency remains unchanged and attributable to merged PR #403. No source/data correction is reopened. |
| PR02 | Suspended. Its exact roster, owning-schema execution, source/execution coherence and adverse proof contract require corrected authority. Preserve PR #404 and completed work. |
| PR03 | Remains not executed and dependent on accepted PR02. Pure Gate math, classifier and intrinsic identity scope do not change. It must consume only the eventually accepted admitted interface. |
| PR04 | Remains not executed and dependent on PR01–PR03. Application, identity, eligibility and Reader/internal boundaries do not change. |
| PR05 | Remains not executed and dependent on PR01–PR04. Golden comparison/readiness scope does not change. Any fixture roster must use the finally approved contract. |
| PR06 | Still owns actual final manifest materialization, source admission and evidence convergence. If approved, its exact complete roster/count changes to include the Gate schema; it must recut identities from final bytes. |
| PR07 | Final documentation must describe the delivered 42-member contract and the reviewed coherence/atomicity limits if approved and implemented. No documentation is written now. |
| OPS01 | Its later action-specific clean-candidate verification remains unchanged in purpose. It must verify the final approved manifest/release identity; no Ops action is authorized now. |

The dependency order remains PR01 → PR02 → PR03 → PR04 → PR05 → PR06 → PR07 → OPS01. No unit is split, added, removed or advanced.

## 10. Tests, evidence, documentation, security and recovery

### 10.1 Required future proof after authority is corrected

- Positive admission of one exact synthetic complete release using the approved 42-member roster and the actual owning Gate schema.
- Negative proof for missing Gate schema (`MISSING_FILE`), invalid/reject-all Gate schema (`SCHEMA_VALIDATION_FAILED`), unlisted schema, extra/missing roster member, hash/size mismatch, source mutation and unsafe/local-reference escape.
- A proof that altering only the captured owning Gate schema changes admission outcome, demonstrating that handwritten checks are not standing in for schema execution.
- A bounded source/execution-coherence proof against the exact mechanism approved in the corrected Plan, including a real non-symlink source-root replacement/update after import.
- One physical packaged-manifest read per admission attempt, with an adverse read-count test.
- Existing Gate normalization, deep immutability, source mutation, symlink, candidate/admitted separation, incomplete actual release refusal and no-fallback suites.
- All affected governed writer/evidence checks, changed-path ownership classification, complete local targeted and default regression suites, and substantive code/security re-review.
- Only after review blockers applicable to the final head are resolved: one complete exact-final-head CI run with all seven applicable lanes and final applicability guard.

The prior corrected-head results—472 targeted passes, 1,724 passes/3 existing closed-rails vendor skips, all nine writer/evidence checks, seven applicable lanes and successful run `34715034846`—remain historical evidence for `eed8a638…`. They are not reusable as final proof after code changes.

### 10.2 Documentation and evidence boundaries

- Corrected whole-change Plan, its application report and approval must record the exact 42-member roster and module-coherence decision.
- Corrected PR02 instruction and detailed Plan must carry the exact approved delta, unchanged limits, owners, tests and recovery.
- PR06 and PR07 must receive the exact changed roster and documentation obligation through normal handoffs.
- Existing evidence is preserved; no hand-edited success report, rewritten historical result or counterfeit current CI identity is permitted.
- PF10 insertion/publication is not performed here. No final addendum number is chosen.

### 10.3 Recovery and CI-cost controls

Recovery reuses PR #404 at `eed8a63807f573abc29de6f6d5ceac54f0c8da85` / tree `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d`, preserves the original workspace, and refreshes main/head/worktree/reviews/checks before any later action. The actual 15-member manifest remains untouched until PR06 authority.

When implementation authority is restored, the existing PR02 engineer must batch coherent fixes and complete local tests before pushing. Reviews take priority over CI. Active PR02 CI must not continue while review blockers remain; no new run starts until the corrected code is locally validated and substantively reviewed. Then CI runs once against the exact final head. Repository-wide workflow behavior is not changed merely to enforce this operating order.

Rollback restores the compatible PR02 loader/Gate module/tests/ownership set and preserves the previously active release. There is still no promise of process-death atomicity, multi-file atomic visibility or cross-process locking.

## 11. Alternatives considered

| Alternative | Assessment |
| --- | --- |
| A. Add the Gate schema as captured manifest-bound member 42 and execute the existing owning validator | **Recommended.** Smallest correction that satisfies both exact ownership and manifest-bound admission without changing schema semantics or public behavior. |
| B. Keep 41 members and retain handwritten Gate checks | Rejected. It cannot truthfully prove that the owning schema ran and violates the no-alternate-validator and actual-schema requirements. |
| C. Load the Gate schema outside the captured manifest-bound set | Rejected. It creates a second, unbound authority and permits source/payload identity divergence. |
| D. Defer Gate-schema enforcement until PR06 | Rejected. PR02 completion and PR03 dependency explicitly require schema-loaded immutable admission before later consumers; PR06 owns materialization, not retrospective PR02 validation. |
| E. Reclassify the Gate schema as non-owning or remove the schema requirement | Rejected for this bounded route. That would change current Canon/Specification meaning and is unnecessary to meet approved intent. It would require its actual Product Owner/Specification/Canon owners. |
| F. Silently add an import reload, caller root selector or deployment switch for module coherence | Rejected. It introduces undocumented authority or protocol and weakens the fixed no-argument boundary. |
| G. Add cross-process locking or immutable-deployment infrastructure to close every ordered-read window | Not proposed. The approved detailed Plan expressly disclaims that guarantee. If desired, it is a separate Product Owner/Specification/architecture decision. |
| H. Preserve completed code and approve a bounded fail-closed execution/source predicate in the Plan | **Recommended companion direction.** It keeps the product objective intact while forcing IA and review to define exactly what can be proven locally and where the guarantee stops. |

## 12. Complete Canon-conflict register

| Entry | Preserved disposition |
| --- | --- |
| `C040-01 CANON_RECONCILIATION` | Thoth-17 `APPROVED` exactly at `2026-09-08T13:23:24Z`; selected/excluded inventory and Addenda 2.2/2.4 history retained. No reopening. |
| `C040-02 CANON_RECONCILIATION` | Same Thoth approval; PF12 filename/body resolved at v2.9.6. No reopening. |
| `C040-03 CANON_RECONCILIATION` | Same Thoth approval; PF14 filename/body resolved at v3.5.7; C040-05 remains separate. No reopening. |
| `C040-04 CANON_RECONCILIATION` | Same Thoth approval; PF19 filename/body resolved at v3.0.5. No QA or new scope authority inferred. |
| `C040-05 CANON_RECONCILIATION` | Isis-49 `APPROVED` alternative A exactly at `2026-09-09T03:57:16Z`; four-argument Gate core; no optional scoring configuration or second calculator. PF14 §6.7 drainage pending/non-gating; Addendum 2.3 published; HDE-DIST008.1 separate. |
| `C040-06 NEW_CANON` | Isis-50 `APPROVED` alternative A exactly at `2026-09-09T11:48:08Z`; original ADR `libfile_c9897950d9588191a2c822b65e7b31a8` unchanged; exact 36 assignments, 64 Gate facts and 16 states. PF10 Addendum 2.5 verified; permanent PF12/PF01 drainage pending/non-gating. |
| `HDE-EPIC040-PR02-F01` | `PROPOSED`; exact roster/owning-schema conflict in this artifact. Not reviewed, approved, rejected or published. Reviewer/session, reviewed artifact ID, decision time and rationale remain not yet produced. Recommended destination: RS-20. |

No decided entry is relabeled `REJECTED` or `APPROVED_AS_CHANGED`; no decision, reviewer or drainage owner is fabricated. The loaded-module/source issue is carried as an implementation-Plan clarification associated with F01, not silently promoted into a new Canon decision. The final atomicity request is a review-scope question against an explicit approved limitation, not a new Canon entry.

## 13. Manual prerequisites and correction route

If RS-20 approves this as an ordinary bounded rescope within approved Specification intent, the following sequence remains mandatory:

1. Preserve the RS-20 review identity and its exact decision.
2. Obtain the actual Product Owner manual rescope/PF10 disposition. This proposal and RS-20 do not supply it. PF10 publication remains a separate Product Owner-controlled action; no addendum number or publication is created here.
3. Because whole-change Plan v2.1 must change and no governing correction instruction exists, return the exact Plan v2.1, approving Review v2.1, Specification v1.1, RS-10 proposal, RS-20 review and evidence delta to the existing same-Isis IA-30 correction intake.
4. Only the real correction instruction from that intake authorizes the retained whole-change IA to execute IA-40 and create a complete Plan successor with an item-by-item application report.
5. Return that successor to the continuing Isis-50 IA-30 review. Do not fabricate `PLAN_REVIEW_ID` or treat RS-20 as Plan approval.
6. After the corrected Plan is actually approved, correct the PR02 instruction and detailed Plan through their applicable native owners, preserve PR #404, and obtain a new exact Product Owner Proceed for the changed engineering contract.
7. Resume the same dedicated `PR-02 HDE-EPIC040` engineering session for the authorized coherent repair batch.

If RS-20 determines that the loaded-module remedy necessarily changes Product intent, an exclusion, a public promise or deployment architecture, route that portion to the Product Owner and existing Specification author Isis-49 / continuing Thoth review before Plan correction. F01's owning-schema/roster correction remains separable and must not be denied merely because a broader optional guarantee is not authorized.

## 14. Unchanged obligations and prohibitions

- Preserve the six selected HDE-SEPA005 units and all twenty-nine Done/context exclusions.
- Preserve no-new-math, no tuning, no second calculator, no fabricated Gates, no caller UUID/configuration/root selector, no persistent identity-model addition and no new public fields.
- Preserve exact integer-versus-bool/float/string handling, raw duplicate-key/nonfinite/surrogate refusal, canonical bytes and strict local schema/reference behavior.
- Preserve candidate-versus-active separation, recursive immutability, source/config/release/repository identity distinctions and refusal without fallback or partial handle.
- Preserve the actual 15-member current manifest and PR06 ownership of eventual complete manifest materialization.
- Preserve primary-before-derived generation, owning writers, companion evidence and same-root closure.
- Preserve no live vendor/database operation, release activation, deployment, QA, Ops, merge, Canon mutation or PF10 publication in this task.
- Preserve all historical reviews, failures, fixes, replies and CI evidence at their actual commits. Do not claim tests ran on a future or merged SHA.
- Preserve PR #404, its branch, exact commits and all user work.
- Preserve the explicit no-process-death-atomicity, no-multi-file-atomic-visibility and no-cross-process-locking limitation unless separately changed by proper authority.
- Preserve repository prompt-use persistence as pending/non-gating while its installed procedure/writer is absent; do not invent or install one.

## 15. Prompt-use record

| Field | Value |
| --- | --- |
| Usage ID | `GCFPE-USE-HDE-EPIC040-RS-10-20260912-PR02-F01-01` |
| Prompt | `RS-10 — Create Bounded Work-Unit Rescope Proposal — 091226.1` |
| Prompt directory | `AI Prompts / HDE IA` |
| Prompt page | `https://app.notion.com/p/3d94590a05eb816497bce16364afb4ae?pvs=204` |
| Retrieved revision | `2026-09-12T13:40:30.633Z` |
| Change / work unit | `EPIC / HDE-EPIC040 / HDE-EPIC040-PR02` |
| Component / finding | `HDE-EPIC040-PR02-F01`: `K040-REQ-003`, `006`, `007`, `008`; `AC040-04`, `07`. Companion module-coherence clarification: `K040-REQ-006`, `007`, `008`, `009`; `AC040-04`, `05`, `09` |
| Specification | `libfile_12bab860949c8191881510875f051460`; v1.1; approved |
| Ecosystem | `GCFPE-20260912.1` |
| Role / stage | Explicitly assigned bounded finding author / RS-10 / originating PR-30 |
| Execution posture | `MANUAL_PROMPT_EXECUTION` |
| Capture | `2026-09-12T20:46:48Z` |
| Repository persistence | Pending/non-gating; no installed authorized provenance writer was established and no repository mutation is authorized |

Earlier PR10, PR20 and PR30 uses remain preserved in the exact instruction, detailed Plan and implementation Result. This record does not rewrite them or assert unobserved runtime/model/session identifiers.

## 16. Complete direct native handoff to RS-20

`NEXT_PROMPT_HANDOFF`

**Destination prompt:** `RS-20 — Review Bounded Work-Unit Rescope — 091226.1`

**Direct Notion reference:** `https://app.notion.com/p/3d94590a05eb81579754f0819f7f6298?pvs=204`

**Verified directory:** `AI Prompts / HDE IA`

**Receiving role/session:** Retain the existing whole-change HDE-EPIC040 IA for RS-20. Retain continuing Isis-50 for any later same-Isis IA-30 correction intake and return review. Do not create, replace, dispatch or repurpose a session.

**Invocation binding:** Review this exact HDE-EPIC040-PR02 v1.0 pending bounded rescope proposal arising from PR-30 finding `HDE-EPIC040-PR02-F01`, with PR02 engineering completion and merge readiness suspended.

**Required proposal input:** The complete saved `HDE-EPIC040-PR02-RESCOPE-PROPOSAL` v1.0 and its actual returned `RESCOPE_PROPOSAL_ID`; state `RESCOPE_PROPOSAL_PENDING_REVIEW`; author/session identity from §1; proposal ends `ASK OK?`.

**Exact upstream inputs:**

- `PR_INSTRUCTION_ID=libfile_40f6b1d402808191b484e5929a6afcca`, v1.0, `INSTRUCTION_READY`, SHA-256 `429cda8e7f00bedc0509e9d00a16c72b37a49f5592054b2b8e069308e812047c`.
- `PR_IMPLEMENTATION_PLAN_ID=libfile_4c88da46f3d08191a38e18f7de652fd4`, v1.0, saved `AWAITING_PO_PROCEED`, actual PO `PROCEED`, SHA-256 `496488109e3fc080dd238145f28edf0a0824b5bb1ff068432e209813df9998e0`.
- `PR_IMPLEMENTATION_RESULT_ID=libfile_c20e76fad8448191af852e9f7bf15d27`, v1.0, `RESCOPE_PENDING`, SHA-256 `779c425ba72c7df142f7ba1806ad1489785eb90de46493dac408e31bf53004e0`.
- `SPECIFICATION_ID=libfile_12bab860949c8191881510875f051460`, v1.1, Thoth-17 `APPROVE` at `2026-09-08T13:23:24Z`.
- `IMPLEMENTATION_AUDIT_ID=libfile_823ee8e9ecb0819185181ec7695265fb`, v2.0, `AUDIT_COMPLETE`.
- `IMPLEMENTATION_PLAN_ID=libfile_11c992cda3f0819199827e86584e41f1`, v2.1, SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be`.
- `PLAN_REVIEW_ID=libfile_b85b81651a508191abdfd8f81803caf8`, v2.1, Isis-50 `APPROVE` at `2026-09-09T13:36:43Z`, SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3`.
- Accepted PR01 review `libfile_47bf2e063d208191bf57f93c71f96821`, v1.1, `ACCEPT`, SHA-256 `f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273`, PR #403.

**Repository evidence:** PR #404 remains open/draft/unmerged on `hde-epic040-pr02-immutable-admission`; accepted base `3828d4b3454259841a3e48d13039dd1475754f2f`; corrected head `eed8a63807f573abc29de6f6d5ceac54f0c8da85`; corrected tree `b0cc12ae82b597bd4f7f226b4812a8cf7dfa7a8d`; nine changed files. Preserve the PR and its work.

**Primary evidence and proposed delta:** Read §§6–7 above. The exact 41-member contract omits the actual owning Gate schema. The active path bypasses it. Read-only probes prove 41 can admit without it, the schema-enabled route refuses absent/invalid schema, and adding it as member 42 currently fails exact-roster validation. Review the proposed manifest-bound member-42 correction and its PR06 effect.

**Separate authority classifications:** Review every row in §8. In particular, keep the physical manifest reread as ordinary PR02 repair; classify the executing-module/source coherence issue as a bounded Plan clarification unless it requires a new deployment/product promise; and preserve the explicit approved atomicity limitation rather than silently adding locking or immutable deployment.

**Whole-change Plan effect:** This proposal concludes Plan v2.1 must change. If RS-20 approves, preserve the required manual Product Owner/PF10 rescope disposition, then route the exact package to the existing same-Isis IA-30 correction intake. Its real instruction must precede IA-40 and the continuing Isis-50 return review. RS-20 approval is not Plan approval.

**Specification boundary:** No Specification, Product objective, exclusion, public promise, schema semantic or Strategy Card change is proposed. If the module-coherence remedy would require such a change, classify only that portion `SPECIFICATION_CHANGE_REQUIRED` and return it to the Product Owner, Isis-49 and continuing Thoth path. Do not convert F01's separable owning-schema correction into an unnecessary product change.

**Canon-conflict register:** Carry §12 complete and unchanged. `C040-01` through `C040-06` retain their exact decisions. `HDE-EPIC040-PR02-F01` remains `PROPOSED`; no review or PF10 disposition exists yet.

**Manual prerequisites:** `RESCOPE_REVIEW_ID=NOT PRODUCED`; governing Plan correction instruction=`NOT PRODUCED`; Product Owner/manual PF10 rescope disposition=`NOT PERFORMED`. No roster change or implementation authority exists until the native sequence completes.

**Required tools, stores, environment and access limitations:** Read the complete current RS-20 prompt and exact Library proposal/upstream artifacts; use connected Notion, controlled Drive and authenticated GitHub read surfaces as required; preserve `MANUAL_PROMPT_EXECUTION` and the automation hold. The check-annotation body and private security task report remain unavailable; their absence does not erase accessible review findings or successful check evidence. No repository, Drive, Notion, PF, CI, review-thread, QA/Ops or release mutation is authorized by this handoff.

**Expected receiving output:** One native `RESCOPE_REVIEW` with exact proposal identity/version, independent evidence assessment, separate classification of every finding, actual `APPROVE`, `DENY`/redline or `SPECIFICATION_CHANGE_REQUIRED`, unchanged obligations, Plan/Specification effect, manual prerequisites, return owner and complete next native handoff. Do not execute correction, implementation or another role.

**Handoff status:** `READY_FOR_NEXT_TASK` only after the proposal has a successful Library save/readback and its actual `RESCOPE_PROPOSAL_ID` is inserted into the transport package; otherwise `BLOCKED` solely at persistence with this complete local body preserved.

## 17. Persistence checkpoint

The complete substantive proposal has been authored and validated as `HDE-EPIC040-PR02-rescope-proposal-v1.0.md`. The required ChatGPT Library create action is unavailable in this execution surface, so no Library write or Library readback is claimed and no `RESCOPE_PROPOSAL_ID`, Library file ID or Library version is invented. Google Drive and Notion are not substitute destinations.

Current handoff state: `BLOCKED` solely on required Library persistence. Recovery owner: Product Owner/operator using a continuation with an available authenticated ChatGPT Library create action. Resume point: save these exact preserved bytes once under `/Glow HDE 3.0`, read the saved artifact back once, record the returned identity/version and byte evidence, and populate the §16 transport fields without reauthoring or executing RS-20.

ASK OK?
