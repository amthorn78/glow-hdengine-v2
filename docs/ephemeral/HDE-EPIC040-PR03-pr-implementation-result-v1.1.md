# HDE-EPIC040-PR03 — PR Implementation Result v1.1

```yaml
artifact_type: PR_IMPLEMENTATION_RESULT
PR_IMPLEMENTATION_RESULT_ID: HDE-EPIC040-PR03-PR-IMPLEMENTATION-RESULT
version: v1.1
predecessor: https://drive.google.com/file/d/1TapODOwCpObTOOn-4NQoSgDyI95PscPz/view?usp=drivesdk
state: RESCOPE_PENDING
readiness: NOT_READY_TO_MERGE
capture_utc: 2026-09-14T10:21:15Z
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040
WORK_UNIT_ID: HDE-EPIC040-PR03
work_unit_title: Pure Gate mechanics and intrinsic identity
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: dedicated PR engineering session for HDE-EPIC040-PR03
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR03 / PR-30
context_conflict: NONE
PO_PROCEED: ORIGINAL_GRANTED_FOR_EXACT_PLAN_ONLY_PRESERVED
PR_IMPLEMENTATION_PLAN_ID: HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN
plan_version: v1.0
repository: amthorn78/glow-hdengine-v2
target: main
workspace: /workspace/scratch/808bf6c1dac3
worktree: /workspace/scratch/808bf6c1dac3/pr03
branch: hde-epic040-pr03-pure-gate-core
implemented_head: b33c41721ad2320f71c2cdaf00616e27d36945da
implemented_tree: 4af351d6f7347541b9853927bf5098299adcc81f
baseline_head: 5b2fb8d70924a6710b6261fc0c93d3869fed6380
baseline_tree: e43c2063599e7bc449f20d4ab045d32d95581bf4
PR_REF: https://github.com/amthorn78/glow-hdengine-v2/pull/405
source_change_during_recovery: NONE
ci_suppression_directive: REMOVED_FROM_CURRENT_PR03_HISTORY
code_review: OPEN_REPRODUCED_P1_PR03_R02
security_review: HISTORICAL_COMPLETE_NO_FINDINGS_ON_IDENTICAL_SOURCE_TREE
open_engineering_findings: 1
current_hosted_ci: COMPLETED_SUCCESS_WITH_KNOWN_OPEN_FINDING
current_ci_run_id: 34830070689
current_ci_run_number: 3569
current_ci_attempt: 1
current_ci_job_id: 103931072116
ci_cancelled: false
ci_success_establishes_merge_readiness: false
candidate_clean: true
rescope_request_id: HDE-EPIC040-PR03-RESCOPE-REQUEST-01
rescope_request_version: v1.0
rescope_decision: NOT_YET_PRODUCED
PF10_BUILD_NOTES_ADDENDUM: NOT_PRODUCED
source_correction_applied: false
merge_execution: NOT_EXECUTED
PR40_execution: NOT_EXECUTED
PR03_lineage_acceptance: NOT_YET_REVIEWED
independent_QA_Ops_deployment_release_activation_Epic_closure: NOT_EXECUTED
output_classification: EPHEMERAL_DRIVE
output_destination: Glow / Ephemeral Planning Files
output_parent_id: 1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc
```

**RESCOPE_PENDING. PR #405 is not ready to merge.** PR03-R02 is a reproduced P1: core can label a result with a coherently admitted release whose non-equivalent mechanics code it did not execute. The unauthorized CI suppression directive has been removed from the existing PR03 history, with zero source changes. Current-head CI passed, but the open correctness defect prevents readiness. The source repair has not been applied because it requires the explicit admission/execution-provenance boundary disposition in instruction §7.3 and detailed plan §14.

This is a complete successor to [result v1.0](https://drive.google.com/file/d/1TapODOwCpObTOOn-4NQoSgDyI95PscPz/view?usp=drivesdk), whose readiness and manual skip-directive cleanup instructions are superseded. The predecessor's original source/test/review/CI facts remain historical evidence; they are not relabelled as tests of this or a future corrected commit. Nathan's original Proceed, the same dedicated engineering session/worktree/branch/PR, accepted PR01/PR02 and all immutable bases remain preserved.

## Current decision package and receiving owner

| Artifact | Exact identity and verification | Direct link |
| --- | --- | --- |
| Bounded rescope request | `HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0`, `RESCOPE_PENDING`; 31,251 bytes / 270 lines; SHA-256 `1f5a1df21a4be089809b9ac642ca047d3205669a39cf3e2c8ce301bda5dd41e1`; exact-text readback verified | [Request](https://drive.google.com/file/d/1Cg6LglLhgqPVrHr6uL374kkdiP2Zqzu6/view?usp=drivesdk) |
| Incident RCA | `HDE-EPIC040-PR03-SESSION-COMPLETION-AND-CI-CONTROL-RCA v1.1`; 27,235 bytes / 197 lines; SHA-256 `a360f20edc5e02915fbb3541d1d1a52bae6e64b0d2ef6d14fad237b3e4af8fae`; exact-text readback verified; platform cause remains undetermined, code defect reproduced | [RCA](https://drive.google.com/file/d/1EOOqIiuaVxPv42Oh9sf3kxNF0WhmC2NK/view?usp=drivesdk) |
| Current code finding | `PR03-R02`, P1, open; discussion `4004034876`; review `5196297648`, posted `2026-09-14T09:55:45Z` at `b33c4172` | [Finding](https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4004034876) |

The native receiver is the **retained Product Owner-assigned whole-change HDE-EPIC040 Implementation Architect**, through [RS-20 — Review Bounded Work-Unit Rescope — 091326.2](https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204). The request contains the complete executable reproduction, exact observed output, controlling boundary, proposed bounded owner/file/test delta, preserved evidence, conflicts, exclusions and return predicates. It is the one substantive rescope intake, not a replacement implementation plan.

## Controlling authority and preserved lineage

The Product Owner manually invoked PR-30 for exactly `HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN v1.0`. That original Proceed remains the sole implementation authority. This result reports engineering delivery only; it does not grant merge authority or work-unit acceptance.

| Artifact | Exact controlling version / decision | Direct source |
| --- | --- | --- |
| PR instruction | `HDE-EPIC040-PR03-PR-INSTRUCTION v1.0`, `INSTRUCTION_READY`; SHA-256 `4f45fff6ecd79b85f7b0d97f57056d1bd8e896eaff53fce81567ee0d08446895`; 462 lines / 39,975 bytes | [Instruction](https://drive.google.com/file/d/1Zj5BResRRxtGarmZ2d3sIAfIVeLD42rs/view?usp=drivesdk) |
| Detailed PR implementation plan | `HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN v1.0`; historical state at Proceed `AWAITING_PO_PROCEED`; SHA-256 `d6fb097d009c81d71b28f97bf09ba5d71bb8429f7d458dcda5f667d0c5a6e8a9`; 555 lines / 53,091 bytes | [Detailed plan](https://drive.google.com/file/d/1wPpcIQkDLVNwdvK2ujfDpkssUh4KwAoO/view?usp=drivesdk) |
| Specification | HDE-EPIC040 v1.1, Thoth-17 `APPROVE` | [Specification](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk) |
| Implementation Audit | HDE-EPIC040 v2.0, `AUDIT_COMPLETE` | [Audit](https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk) |
| Immutable whole-change Implementation Plan | HDE-EPIC040 v2.1; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` | [Whole-change plan](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk) |
| Approving Plan Review | v2.1, Isis-50 `APPROVE`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` | [Plan review](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk) |
| Accepted PR01 lineage | v1.1, `ACCEPT`; #403 remains accepted and final | [PR01 acceptance](https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk) |
| Accepted PR02 lineage | v1.0, `ACCEPT`; #404 remains accepted and final | [PR02 acceptance](https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk) |
| Current controlled PF10 Markdown | v13.2.4; §2.11 records PR02 acceptance and does not alter PR03 scope | [PF10](https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk) |

The complete instruction, detailed plan, and exact linked source package were read during PR-20. PR-30 recovered that same dedicated session, fetched the complete controlling instruction/plan and approved lineage again, verified the exact controlling bytes, and rechecked the applicable current Canon and repository seams before mutation. Earlier artifacts remain immutable historical records; their pre-implementation states were not rewritten.

Controlled PF source resolution was proved through direct parents: root `0ANCzbmSbmO_HUk9PVA` → Glow `1MZXcC5tKMkI9n8EobkywIj1ifcF6IvZ3` → Core Docs `18T84WC_Jxjb75V37_eYcRqn8zOjHYgxu` → PFCanon `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3`. Only the unique controlled Markdown children were used. PF authorities carried from the complete plan source record are PF01 v1.3.7, PF02 v2.4.5, PF03 v1.8.7, PF05 v2.5.2, PF09.3 v1.1.5, PF10 v13.2.4, PF12 v2.9.6, and PF14 v3.5.7. Their exact direct references and requirement clauses remain in detailed plan §2.2. PR-30 specifically re-read the applicable math, taxonomy, core, evidence, and PF10 acceptance clauses. No Google Doc twin was used as PFCanon authority.

Recovery independently rechecked the direct PF10 parent chain and complete current Markdown. It remains v13.2.4, 148,829 bytes, SHA-256 `fe350b609c49d926586384afb0e774fde7829fc673849caac9d469679e518f2d`, exactly equal to the retained source. No PR03 scope overlay is inferred from the accepted PR02 F01/F02/F03 material.

## New defect and reason the repair is pending

The decisive reproduction changes the temporary complete fixture's `signals.py` from addition to subtraction, compiles it successfully, and regenerates the manifest through the existing fixture owner. Both baseline and altered fixtures admit successfully. The resulting release ID changes, but all computed signals/categories remain the old values and the result carries the altered ID. Executing source hash: `c1d3829c21934452ed1a34b7ba32d8f84664033730f1ec0ebdea354d24f2c690`; altered fixture source hash: `fa51ef85f2cc711fee24a58139214945214bc3a6630ed14d648279808cae232c`. The temporary fixture is removed after execution; the repository remains clean.

PR03 validates source/manifest record agreement without binding its four newly active mechanics modules to the code actually executed. The existing accepted admission mechanism compares passive top-level execution provenance with captured source compilation for exactly the loader, serializer wrapper, stable serializer and category registry. Core/composite/signals/calculators are outside that fixed coverage. This is a real missed integration proof, not an indication that changed band thresholds are admissible or that PR03-R01 should reopen.

Instruction §7.3 explicitly preserves accepted admission and execution-provenance behavior except necessary signature imports. Plan §14 routes changes to admission/normalizer/manifest/execution-coherence behavior beyond a direct import adaptation through a formal bounded request. The proposed repair extends the existing admission owner's check to the four new PR03 mechanics owners, with passive provenance and focused refusal/purity tests. It introduces no core I/O, new loader, changed mathematics, schema/bundle/public field, actual release promotion or broader atomicity/tamper-resistance claim. No such extension has yet been implemented or self-approved.

The request asks the retained IA to make the native substantive scope decision. An approved bounded overlay requires the receiver's standalone addendum and Nathan's manual drain/verification before the same PR03 session resumes through RS-40 under its original Proceed. An `IN_SCOPE_REPAIR` decision supplies its rationale and returns through PR-30 with authority unchanged. The engineer does not request a replacement Proceed, accepted PR02 rerun, plan rewrite or early merge.

## CI control correction and current Git attribution

The agent introduced the original `[skip ci]` directive without approval and wrongly assigned its removal to Nathan at handoff. Nathan rejected that action. The engineer corrected the existing branch itself, after checking the remote expected head, and preserved the original commits as history.

| Attribution | Head / parent | Source tree / effect |
| --- | --- | --- |
| Accepted main baseline | `5b2fb8d70924a6710b6261fc0c93d3869fed6380` | `e43c2063599e7bc449f20d4ab045d32d95581bf4`; unchanged |
| Original reviewed implementation | `c79bd090aa97627cfb72215762140a55992134eb` | `4af351d6f7347541b9853927bf5098299adcc81f`; historical review/local evidence |
| Original CI head | `ad1fb9251cfbcb00405905aec4b8381a7ec54f4c` | Same tree; original CI #3568 |
| Corrected implementation message | `dd52ba0dc1224abd629a31d5618104dc5a605832`, parent accepted main | Same PR03 tree; removes unapproved directive and deferral wording |
| Current head | `b33c41721ad2320f71c2cdaf00616e27d36945da`, parent `dd52ba0d` | Same PR03 tree; records metadata correction; zero source diff |

Only branch `hde-epic040-pr03-pure-gate-core` was updated; PR #405 is still the sole PR03 PR and remains open/unmerged, out of draft. Original commits are retained locally under `refs/archive/hde-epic040-pr03-before-ci-directive-removal`. The remote Git objects were restored exactly into local Git with object-hash verification. The final local and remote head agree, the worktree is clean, and all current PR03 commit messages were checked: no recognized CI skip directive or `skip-checks: true` trailer remains. No future manual cleanup is assigned to Nathan.

## Current and historical review disposition

| Finding or review | Actual disposition |
| --- | --- |
| PR03-R01 threshold finding | Historical resolved thread `PRRT_kwDOP103ks6iCnlF`; the accepted loader refuses coherently rehashed non-adopted thresholds with `INITIAL_THRESHOLDS_MISMATCH`. The original same-head re-review reported no major issues and the engineer recorded resolution. No threshold or accepted admission change was made. |
| Original security review | Completed with no findings on `c79bd090`, including the ready-for-review pass. [Security result](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661215092). Its evidence covers the identical source bytes; it is not claimed to approve a future repair. |
| Original final code review | [Completed re-review](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661392031) at `2026-09-14T08:48:22.602140Z`, before original CI. The later P1 demonstrates a missed case; this historical result does not override it. |
| New configured code review | Triggered by new commit identities after metadata correction, same source tree; [review 5196297648](https://github.com/amthorn78/glow-hdengine-v2/pull/405#pullrequestreview-5196297648) identifies the P1. |
| PR03-R02 executing mechanics binding | Confirmed/reproduced, thread `PRRT_kwDOP103ks6iD-lB` remains unresolved. No corrective code review, resolution or waiver is claimed. |

After native scope disposition and repair, this same engineering owner must run the focused local correction proof and required affected regression/evidence checks, obtain substantive code and applicable security review, then record all seven lanes on the final candidate. Review findings take priority over spending CI runs on known defective code. No CI suppression mechanism may be reintroduced without Nathan's explicit approval.

## Current hosted CI result and limits

One ordinary workflow run followed the commit-message correction: [CI #3569 / 34830070689](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34830070689), attempt 1, on exact head `b33c41721ad2320f71c2cdaf00616e27d36945da`. Job/check `103931072116`, named `test`, started `2026-09-14T09:50:30Z` and completed `10:02:14Z`, `success`; the run completed by `10:02:15Z`. Setup, exact checkout, classification and closed deterministic environment checks also succeeded.

| Actual CI step | Conclusion | UTC interval on September 14, 2026 |
| --- | --- | --- |
| Run affected behavioral tests in isolation | `success` | `2026-09-14T09:50:47Z` → `2026-09-14T09:52:47Z` |
| Run product mechanics and ordering lane | `success` | `2026-09-14T09:52:47Z` → `2026-09-14T09:52:58Z` |
| Run CLI and compatibility lane | `success` | `2026-09-14T09:52:58Z` → `2026-09-14T09:53:05Z` |
| Run database and runtime-contract lane | `success` | `2026-09-14T09:53:05Z` → `2026-09-14T09:53:17Z` |
| Run rails policy and secret-safety lane | `success` | `2026-09-14T09:53:17Z` → `2026-09-14T09:53:48Z` |
| Run governed evidence integrity lane | `success` | `2026-09-14T09:53:48Z` → `2026-09-14T10:00:18Z` |
| Run approved generic QA subsystem lane in isolation | `success` | `2026-09-14T10:00:18Z` → `2026-09-14T10:00:40Z` |
| Build and verify exact-source release attestation | `success` | `2026-09-14T10:00:40Z` → `2026-09-14T10:02:13Z` |
| Verify truthful applicability and clean candidate tree | `success` | `2026-09-14T10:02:13Z` → `2026-09-14T10:02:13Z` |

The seven lanes are steps in one check, not seven independent GitHub checks. This successful run includes evidence convergence and clean candidate proof for the current bytes. The P1 was posted while the run was in progress. The run was not cancelled: cancellation was unavailable through the connected GitHub tools, there was no supported terminal cancellation path, and a prohibited browser substitution was not used. No cancellation or additional post-finding CI request is claimed.

Current CI success does not establish correctness of the reproduced case, satisfy corrected-code review, or confer merge readiness. The historical run [#3568 / 34824825198](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34824825198) remains success on original head `ad1fb925`, job `103914417233`, completed `09:02:58Z`. Neither run is future repair evidence.

## Preserved delivery and local validation

The following complete delivery and validation record is retained for the unchanged source tree. It explains what exists and was tested; it is not a renewed declaration that every PR03 obligation is complete. The original local attempts, environment correction and evidence ownership remain as recorded in v1.0. No broad suite was rerun during this recovery solely because commit IDs changed. The newly embedded PR03-R02 reproduction is the additional decisive test.

## Delivered behavior and interface seams

The exact entrypoint is `compute_core(member_a, member_b, mechanics_bundle, release_id)`: four required positional-or-keyword arguments, no defaults, variadic option, selector, or CoreConfig. It consumes accepted PR02 `NormalizedGates` and an injected `AdmittedMechanicsBundle`. It neither normalizes malformed inputs into success nor loads configuration or schemas.

| Owner | Delivered responsibility |
| --- | --- |
| `engine/magic10/composite.py` | Immutable Channel classifications; one traversal of the accepted 36-row registry; five-state priority; numerically ordered masks and `member_lo`/`member_hi` ownership only for dominance and compromise |
| `engine/magic10/signals.py` | Immutable signal rows; strict injected profile/operation/channel/weight checks; integer-only ordinary, equilibrium, and counterweight calculations; exactly 20 rows in flattened caps order |
| `engine/magic10/calculators.py` | Two-input caps in doubled-q units; exact positive integer weights; one half-up weighted reduction and final clamp; fixed inclusive Cool/Open/Warm/Glow bands |
| `engine/core/core.py` | Input and admitted graph invariants; source/config/release record coherence (PR03-R02 executing-code gap remains open); one classification call; ordered assembly; intrinsic chart fingerprints and pair key; immutable six-field result and final relational closure checks |
| Both package `__init__.py` files | Remove old precomputed-score/calculator exports; expose only the coherent core entrypoint/result surface |

Ordinary signal q is `(N + 25*W) // (50*W)`. Equilibrium q is `(800*min(lo_mass, hi_mass) + W) // (2*W)`. Counterweight q is `(400*matching_mass + W) // (2*W)`. Category scores use capped half-unit q values and `(weighted_q + total_weight) // (2*total_weight)`, clamped once to `0..100`. The implementation consumes the admitted map and values; it does not define another runtime signal map or retune profiles, caps, weights, or formulas.

Each chart fingerprint hashes exactly `schema=magic10_chart_fingerprint.v1` plus a 16-character lowercase Gate mask. The pair preimage has exactly config ID, ordered fingerprint members, release ID, result schema, and `schema=magic10_pair_preimage.v1`. Numeric mask order controls membership; equal masks retain two equal fingerprints. Canonical bytes come only from the unchanged shared serializer. No person UUID, birth data, viewer, request, clock, random value, cache, narrative, or repository commit is a core identity input.

`CoreResult` has exactly `schema`, `config_id`, `release_id`, `pair_key`, `signals`, and `categories`. Frozen slotted records and tuples preserve the in-process result. Projection returns ordinary dict/list scalars without mutating that result. The unchanged PR01 result schema validates projected output; order, types, ranges, and bands are also checked before return. Invalid input is refused as the value-free `ValueError("invalid pure core contract")`, with no partial result or successful legacy fallback.

## Requirement coverage

The following records previously exercised behavior. PR03-R02 demonstrates that execution-to-release binding remains incomplete; the K040-REQ-007/008/009 completeness claim is withheld pending the correction. These historical tests do not clear the new finding.

| Requirement / acceptance allocation | Actual implementation and decisive evidence |
| --- | --- |
| K040-REQ-001 / AC040-01 | The bounded changed-file inventory; no application, release materialization, OPS, PF10, or later-unit source change |
| K040-REQ-002 / AC040-09 | Single pure classifier/signal/reducer/core owners; unchanged serializer/result schema; AST and guarded import/compute tests; removed alternative success exports |
| K040-REQ-005 / AC040-03 | All 16 endpoint cases and state counts; exact Integration exceptions; 20 signal and 10 category order checks; ordinary and both Balance formulas; fixed G001–G006 source oracles |
| K040-REQ-007 / AC040-04 | Exact PR02 types consumed; mutable, forged, cyclic, malformed, and incoherent objects refused; strict release/config/source relationships; closed projected result |
| K040-REQ-008 / AC040-04 | Missing/extra/duplicate/unknown fields and rows, invalid operation/profile/owner, bool/float/string and numeric bounds tests; no old overload or partial success |
| K040-REQ-009 / AC040-05 | Independent canonical-preimage derivation and three literal chart digests; numeric-mask ordering; equal-member duplication; coherent different release changes pair identity |
| K040-REQ-010 / AC040-06 | Complete two-run and AB/BA value/canonical-byte equality; fixed independent expected values; explicitly bounded synthetic evidence |
| K040-REQ-011 / AC040-07/08 | Adverse types/arity/caps/rounding/band cases, taxonomy and owner-mass tests, immutability, purity, and side-effect guards |
| K040-REQ-012 / AC040-08 | Existing core evidence writer and four closed schemas; current-source and fixed-oracle assertions; no-change bytes/mtime test; canonical updater and all companion checks |
| K040-REQ-013 | Actual base/head/tree, commits, PR, review triggers/results, local command outcomes, and final hosted CI identities in this result |

K040-REQ-003, K040-REQ-004, and K040-REQ-006 remain accepted predecessor/interface obligations. Their integration tests were used as required regression coverage; no accepted PR01/PR02 work or lineage review was reopened or redelivered. Complete PR05 golden readiness and G007/G008/comparator work are not claimed.

The G004 literal oracle is A Gates `{5,19,20,34,43,49}`, B Gates `{9,12,15,22,23,52}`, q values `[25,63,0,38,40,20,0,25,50,38,50,0,0,0,50,20,0,60,0,33]`, and category scores `[22,10,15,6,22,13,0,18,15,8]`, all Cool. Tests and the evidence writer refuse an otherwise schema-valid result that contradicts this source oracle. Expected values are not generated from the calculator under test.

## Governed evidence ownership and convergence

The existing `tools/evidence/generate_engine_core_evidence.py` owns the same four primary paths and artifact keys. It builds a synthetic complete fixture outside core through the accepted admission loader, runs the actual guarded purity tests, computes repeated/reversed/equal-mask results, validates the owning result schema, verifies the fixed G004 oracle, and records actual predicates and source identities.

| Artifact key | Primary path | Existing schema path |
| --- | --- | --- |
| `engine_core_purity_report` | `artifacts/core/purity/purity_report.json` | `docs/schemas/core/engine_core_purity_report.schema.json` |
| `engine_core_two_run_logs` | `artifacts/core/two_run/identity.json` | `docs/schemas/core/engine_core_two_run_logs.schema.json` |
| `engine_core_abba_logs` | `artifacts/core/abba/ab_ba_parity.json` | `docs/schemas/core/engine_core_abba_logs.schema.json` |
| `engine_core_json_compare_logs` | `artifacts/core/json_compare/core_result_json_compare.json` | `docs/schemas/core/engine_core_json_compare_logs.schema.json` |

The evidence schemas reference the unchanged `schemas/magic10_result_v1.schema.json` through a locally populated resolver. No remote schema retrieval or second pure-result schema owner is introduced. Evidence is labelled `synthetic_complete_release_only` and binds the 12 relevant runtime/config/result-schema sources, the fixture's admitted identities, observed UTC capture, closed rail pins, and actual checks.

After primary/schema bytes were complete, `tools/evidence/update_evidence_index.py` alone produced eight sibling proofs and the Machine Mirror/checksum/proof changes. The mirror's eight affected core rows and self-record converged. Existing Human Index registrations, sentinel, and orientation bytes remained unchanged. No generated companion was hand-edited, and no new evidence family or stronger publication atomicity guarantee was added. A repeated identical proof preserves original observed capture time, bytes, and mtimes.

All planned read-only checks passed: updater `--check`, orientation `--check`, step-log manifest `--check`, evidence mirror hash, evidence path validation, mirror schema, final LF, canonical JSON `--check-only`, and `git diff --check`. The final clean-tree evidence is recorded with CI below.

## Local validation and resolved implementation issues

All local commands used a dedicated Python 3.12 virtual environment outside the repository, with installed `requirements-dev.txt`, `requirements.txt`, editable project, setuptools and wheel. Pytest readiness was verified. Applicable commands used `LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1`; no live vendor or database request was made.

| Validation group | Result | Evidence location in recovered workspace |
| --- | --- | --- |
| Complete focused plan suite | 592 passed | `focused-final.xml`, `focused-final.log` |
| Configured default suite, separately | 1,822 passed, 3 skipped | `default-final.xml`, `default-final.log` |
| Actual classifier-selected 70 test files, isolated clean worktree | 1,899 passed | `clean-lanes/changed-tests.xml` |
| Product lane | 20 passed; ordering check passed | `local-lanes/product-1.xml` and command logs |
| Compatibility lane | 62 passed, 3 skipped, 2 xfailed; CLI help and serializer/emitter guards passed | `local-lanes/compat-3.xml` and command logs |
| Database/runtime-contract lane | 249 passed; direct-only contract check passed | `local-lanes/db-1.xml` and command logs |
| Rails lane | Job definitions passed: 4, 108, and 39 test groups plus existing proof check modes; workflow integration 124 passed | `local-lanes/rails-0.log`, `rails-1.xml` |
| Governed evidence lane | 111 passed and all read-only integrity checks passed | `local-lanes/evidence-9.xml` and command logs |
| Generic QA subsystem regression lane, isolated clean worktree | 488 passed | `clean-lanes/qa.xml` |
| Release regression lane, isolated clean worktree | 52 passed; manifest-only check passed | `clean-lanes/release.xml`, `manifest.log` |
| External exact-source attestation | Build and verify passed with `--require-clean`; 15-stage generic release sanity completed | `clean-lanes/attestation-build.log`, `attestation-verify.log`, `attestation-record.json` |

Counts overlap and must not be summed. Default skips are the three vendor-dependent showcompat tests under closed rails. The compatibility roster also preserves two existing `/internal/version` expected failures (xfail), which JUnit encodes as skipped entries; they are not ordinary skips. No PR03 behavior test was skipped. The named QA/release lanes are repository engineering regressions, not independent QA, OPS01, release activation, or Epic acceptance.

The focused failure harness first established the missing new core contract. During implementation, the old admission hash-corruption test stopped corrupting its fixture because PR03 replaced the placeholder module. Its corruption step now flips one byte, preserving length and the same hash-mismatch assertion. This is a necessary fixture adaptation; accepted PR02 admission behavior is unchanged.

The first complete default-suite attempt had 23 environment failures: 14 isolated subprocess tests could not see user-site `jsonschema`, and nine CLI/admin tests could not find `hdctl` on PATH. A dedicated virtual environment and PATH corrected that setup without a repository dependency or configuration change. The complete focused/default suites then passed as shown above. Developmental failures are preserved as attempts, not reported as successful runs.

The plan's external attestation example named a JSON file for `--output`; the actual repository command requires an external empty directory. Execution used the existing tool/workflow's directory interface and `--require-clean` for build and verify. The generated bundle was removed after its result was recorded; this did not change the approved plan or implement OPS01. The local result binds source commit `c79bd090aa97627cfb72215762140a55992134eb`, exact source-tree digest `14d92556dd7450f411645385f5a6f9b80c9155b483a6e8ea45bae5e7eb31ba71`, and unchanged manifest identity `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856`. Its attestation-record SHA-256 is `695748ee88273939a51fa97321a9789c9f394e82aa41ac877660514f70b16dee`. The existing safety filter omitted 14 retained-history files/companions; that scoped behavior was preserved, not treated as new PR03 evidence or a release promotion.

## Canon-conflict register carried unchanged

The complete original register lineage, sources, alternatives, evidence, rationales, and reviewed artifact identities remain incorporated by the exact Specification, immutable whole-change Plan/review, PR instruction §13, and detailed plan §13 links above. This table carries their operative decisions without a new disposition.

| ID | Classification / decision | PR03 treatment and remaining owner |
| --- | --- | --- |
| C040-01 | `CANON_RECONCILIATION / APPROVED`, Thoth-17, `2026-09-08T13:23:24Z` | Preserve Done exclusions and resolved PF09 agreement; no reopening |
| C040-02 | `CANON_RECONCILIATION / APPROVED`, same Thoth-17 decision | Current PF12 v2.9.6 used; historical identity mismatch remains history |
| C040-03 | `CANON_RECONCILIATION / APPROVED`, same Thoth-17 decision | Current PF14 v3.5.7 used; C040-05 separately controls old core-test text |
| C040-04 | `CANON_RECONCILIATION / APPROVED`, same Thoth-17 decision | QA identity history preserved; PR03 checks do not constitute independent QA |
| C040-05 | `CANON_RECONCILIATION / APPROVED`, alternative A, Isis-49, `2026-09-09T03:57:16Z` | Old CoreConfig/precomputed-score/three-argument success path removed; separate HDE-DIST008.1 scope preserved; permanent PF14 §6.7 drainage remains with its governed maintainer and is non-gating |
| C040-06 | `NEW_CANON / APPROVED`, alternative A, Isis-50, `2026-09-09T11:48:08Z` | Accepted 36-row taxonomy, four Integration members, `10-34`/`20-57` exceptions, and 16-case conformance implemented with no weight/formula change; permanent PF12 §2.1/PF01 §§6.1–6.2 drainage remains with governed maintainers and is non-gating |

PR02 F01/F02/F03 overlays remain effective only for accepted PR02. PF10 v13.2.4 §2.11 accepts PR02 without granting PR03 scope changes. No conflict was reopened, relabelled, omitted, or decided anew. PR03-R02 now produces the bounded rescope request linked below; it supplies no Canon decision or PF10 addendum.

## Exact bounded file inventory at the preserved candidate

All rows below are the complete main-to-current-head inventory: **39 paths**, 1,962 additions and 1,039 deletions, across the two ordered PR03 commits. SHA-256 values identify current file bytes at Git tree `4af351d6f7347541b9853927bf5098299adcc81f`; paths are repository-relative. The metadata-correction commit itself has zero file differences from the reviewed checkpoint. Governed generated files remain at their existing registered paths.

| Final repository path | Bytes | SHA-256 |
| --- | ---: | --- |
| `artifacts/core/abba/ab_ba_parity.json` | 6431 | `c9667229c56810f25fc58eae1a08ce1c29e6e5f20501914e86dd24ef66fdbd72` |
| `artifacts/core/abba/ab_ba_parity.json.path_proof.txt` | 204 | `d5790ed1d7410e843c47e40db539512043eae02a195e032fc47e591b15953ae1` |
| `artifacts/core/json_compare/core_result_json_compare.json` | 3422 | `4032adc29d04f578fef729f10a7fa7db67f14c61018cbf2c91cce3586947745d` |
| `artifacts/core/json_compare/core_result_json_compare.json.path_proof.txt` | 224 | `9b442a2ff19877358c22d25654042e22458cac41f2c257942b40b30ddd746fb9` |
| `artifacts/core/purity/purity_report.json` | 1859 | `4d7095d6e31be437fefab389ef6d327e513818a7e9851ab8fa598adafd168474` |
| `artifacts/core/purity/purity_report.json.path_proof.txt` | 207 | `de5cc6e46a9a84db92208251ee9d749dbc572ce8c3dc011a2365e1cfeb24969b` |
| `artifacts/core/two_run/identity.json` | 4813 | `93ff556addb645848343b41419117d6486dc05347d70c595e800520f18ed673a` |
| `artifacts/core/two_run/identity.json.path_proof.txt` | 203 | `078694d834b4caa1f1af2740e310b5876f4b317855efbcffd6f82c6f51671366` |
| `artifacts/evidence_index.jsonl` | 289697 | `41516114997429e93802f3a736a3888056c656099f1d967d615f382379addc84` |
| `artifacts/evidence_index.jsonl.path_proof.txt` | 284 | `77c18b5c47b2dd1a9abd88b6a9ecfaa1e782e4c8e024f2b8243a42de194f4be3` |
| `artifacts/evidence_index.jsonl.sha256` | 97 | `3f7047f7fd4e434315d194f0a503d8da6e3df48bf47920eb932e67c7bb8f8b43` |
| `artifacts/evidence_index.jsonl.sha256.path_proof.txt` | 202 | `99b23729fdd33b40813b8c0bed6b34b651ab5703fb582823afc0f4b00f07b397` |
| `ci/checks/classify_ci_changes.py` | 60824 | `6e4e610bfe33456adb5c1afdd14cf6272fe3594afdec921e58794b345458e4f6` |
| `docs/schemas/core/engine_core_abba_logs.schema.json` | 5327 | `f021843dfb6a284f60835150344b7145d9cd44a1a438707ed5c7e2ea1d9f93b4` |
| `docs/schemas/core/engine_core_abba_logs.schema.json.path_proof.txt` | 218 | `4a22885f03a485d4b1df2b87c72b71a35ad327646baa9aabdbbe3385259c2271` |
| `docs/schemas/core/engine_core_json_compare_logs.schema.json` | 5220 | `025faef8d810339409de5e85c1ab9694fcfd4aa106d7da9fae35ac0b2427533e` |
| `docs/schemas/core/engine_core_json_compare_logs.schema.json.path_proof.txt` | 226 | `27ecc1ca767e2429673115d8d4bf92b7085a62ad52a9356665211501b086aee3` |
| `docs/schemas/core/engine_core_purity_report.schema.json` | 5034 | `9017ce9a2a1ae044d361536cbdf23f0e45d58cfff84f1f23d70a5765d60c2db3` |
| `docs/schemas/core/engine_core_purity_report.schema.json.path_proof.txt` | 222 | `e8497f4aab5c82f5e63dad4c167d67de1b6dba17ae035ced29bb425c4e891fd6` |
| `docs/schemas/core/engine_core_two_run_logs.schema.json` | 4992 | `6a11ee9b93f21c7d3491cfeeec6f358f7aabdb34cf22b6148c3e2aa4bbe2ac2b` |
| `docs/schemas/core/engine_core_two_run_logs.schema.json.path_proof.txt` | 221 | `792484a66de73338f382ca5e1ec6e8078666ef7df522722e9038b05747a9b058` |
| `engine/core/__init__.py` | 131 | `c86ee4c120f6aeea098ea6cccd80375426a7b6b3b20ed9981014d1c9bb496929` |
| `engine/core/core.py` | 12567 | `53f215607a427313137e832526b04f51975294912738228ffe5f277ac6571893` |
| `engine/magic10/__init__.py` | 78 | `5363b7dde23ce8a8737b9ba09b06ebcfaa56ca8ce351bb105d65bfa76f06f772` |
| `engine/magic10/calculators.py` | 1479 | `70a8fd5e29288eb7e377b18fad97fa378d9fddffd4cd916aa94892d7d211552f` |
| `engine/magic10/composite.py` | 1311 | `a20215f122da296b0053a553d0b5eb5e9e6a62d9cbf20fbcbeae600f24da8f1b` |
| `engine/magic10/signals.py` | 5662 | `c1d3829c21934452ed1a34b7ba32d8f84664033730f1ec0ebdea354d24f2c690` |
| `tests/config/helpers.py` | 4476 | `ab12b3d123927f5207acaa32ea6a6b8b7879fa56d76624787a4734bb963982e4` |
| `tests/config/test_production_admission.py` | 27949 | `9f2fbd14fd15b3b13dcbb9435c4f0362d3467f921fabad5cbe81cce5f6708e76` |
| `tests/core/test_engine_core_abba.py` | 3166 | `142843f168f1115b06a7b6e1b5125569396884aeb85a039c82161e3135b261e9` |
| `tests/core/test_engine_core_determinism.py` | 15999 | `b815e2d4f3e10796a51d6edd167dece949acad3405c9a1b70825780e74cbb0e7` |
| `tests/core/test_engine_core_purity.py` | 4401 | `3130cb7a119344eaeb723d998b3be77e3ffcc88f228b4ac47556f08b545180ca` |
| `tests/evidence/test_canonical_json_gate_check_outputs.py` | 52774 | `1fbee1ba99552154938c9513cdf7cfb4ceb21bc1117913f84de147e84e67f801` |
| `tests/evidence/test_engine_core_evidence.py` | 6879 | `b8409a0ac042136a95e79c394e066c24900f4158b49de9cba8ddfae4278451ec` |
| `tests/evidence/test_rails_ci_workflow_integration.py` | 76540 | `1d878dc455cf1a1589c4628e3484571ea655d885e465413edce77c707178ae92` |
| `tests/m10/test_defs_order.py` | 1326 | `f9e1a53f347749858290d4bcb70bb11ee455474e109f229c975ee688351f1bb3` |
| `tests/m10/test_m10_symmetry_identity.py` | 805 | `4802d857ca4e14b77ca031e52d5cc512ade7bc3aeb23e1424cdd8fded32abc27` |
| `tests/m10/test_thresholds_rounding.py` | 1731 | `6d5a8286bf68b768e8637754e3c71c52a6675d73a0b1792ace83ef860f7431e4` |
| `tools/evidence/generate_engine_core_evidence.py` | 9624 | `6cba625cc348497d28adc0f65b595e56d4567b7533777b000237371f53464caa` |

The four core primaries were generated at `2026-09-14T08:04:56Z`. Their synthetic fixture release identity is `ff877c1219e965765607375a8ba5e25bb7f9f847e86c7a43e40b71d50f94fd4e`; it is not an active production release. The actual retained 15-member manifest identity remains `e0d5c9805408640a987c757426937be90c770e55ee949f962aa1a2154af49856`. The primary hashes, schema/proof hashes and mirror hash in this inventory are the converged final bytes checked locally and in hosted CI.

## Incident RCA and user-visible completion

The [complete RCA v1.1](https://drive.google.com/file/d/1EOOqIiuaVxPv42Oh9sf3kxNF0WhmC2NK/view?usp=drivesdk) establishes the unapproved CI-control decision and its correction, the missing timely visible completion, and the separate code defect. Original CI completed at `09:02:58Z`, the historical implementation result was saved to Drive at `09:10:05.145Z`, and the PR recorded completion by `09:11:13Z`, while the supplied pre-status conversation still ended with waiting commentary. Exact user-message timestamps and turn/scheduler/final-message/client-delivery diagnostics are unavailable; no technical platform root cause or precise user-wait duration is invented.

The verified operational failure is completion/status visibility. The underlying platform cause remains undetermined. PR03-R02 is not evidence of a runtime deadlock or a reason the original final message was absent. Meaningful updates while the assistant is running are required; they cannot guarantee a heartbeat from a paused runtime. No platform fix, autonomous monitor, new skill policy or persistent liveness service is claimed.

## Preserved exclusions, risks and recovery ownership

The actual release remains at 15 members and has not been materialized as the final 44-member release, promoted or activated. Synthetic complete fixtures and engineering lane results do not constitute actual release readiness, independent QA, OPS01, acceptance or Epic closure. Source correction is not yet applied and the false-attribution path is still present at the current head. That is the outstanding engineering risk and the reason this result is pending.

Preserve PR04 application eligibility/orientation/cache/transports; PR05 complete golden readiness; PR06 release materialization/promotion; PR07 documentation; OPS01; independent QA/Ops/deployment; PF10 edits/Canon drainage; release activation and Epic closure as exclusions. No new public/API/CLI field, selector, hidden bypass, duplicate mechanics/schema/serializer/loader owner, remote schema, persistent cache, live vendor/database access, stronger atomicity guarantee or alternate calculator is authorized by this result. PR01/#403 and PR02/#404 remain accepted-final and are not reopened or rerun.

Recovery stays in `/workspace/scratch/808bf6c1dac3/pr03`, branch `hde-epic040-pr03-pure-gate-core`, PR #405 at the exact head/tree above, using the existing dedicated environment and original Proceed. Retain the source, all original logs and artifacts, old/corrected commit lineage, review threads, current CI jobs record and embedded reproducer. No repository source was modified during this recovery; no accepted worktree was repurposed. The source repair, new review and final gate after repair remain with the same PR03 engineering owner after native disposition.

## Prompt-use provenance and exact next action

Preserve `GCFPE-USE-HDE-EPIC040-PR-10-20260914-PR03-01` in instruction §15, `GCFPE-USE-HDE-EPIC040-PR-20-20260914-PR03-01` in detailed plan §16, and `GCFPE-USE-HDE-EPIC040-PR-30-20260914-PR03-01` from historical result v1.0. This is recovery of that same PR-30 invocation, selected release `GCFPE-20260913.1`, prompt version `091326.2`, dedicated PR03 engineer, approved Specification v1.1, same work-unit/requirement allocation. The exact PR30 source remains [PR Implementation Proceed](https://app.notion.com/p/3da4590a05eb81c0aee0d0862b242e09?pvs=204). Actual recovery capture time and commit/artifact references are recorded here. Repository persistence is pending/non-gating for its authorized writer under a genuinely installed procedure; no prompt or registry was edited.

RS-20 was resolved and read solely to prepare the complete native intake. It has not been executed by this engineer. The sole next receiver is the retained Product Owner-assigned whole-change HDE-EPIC040 Implementation Architect at [RS-20 — Review Bounded Work-Unit Rescope — 091326.2](https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb?pvs=204), with exactly `HDE-EPIC040-PR03-RESCOPE-REQUEST-01 v1.0` and the immutable linked bases, complete current result/RCA, current PF10, actual open PR/head and original Proceed.

The expected next result is one substantive `RESCOPE_REVIEW`. An approved bounded overlay produces exactly one standalone `PF10_BUILD_NOTES_ADDENDUM`, `READY_FOR_MANUAL_DRAIN` / `NON_CANONICAL_PENDING_MANUAL_DRAIN`, drain owner Nathan / Product Owner; the receiver saves/readbacks both and returns the conditional RS-40 handoff to this same engineering session after Nathan's manual drain and verification. `IN_SCOPE_REPAIR` instead returns to selected PR-30 under original authority without an addendum. Other dispositions follow RS-20's native return. No decision rewrites the approved base, creates a replacement Proceed or reruns accepted PR work.

This result does not authorize a merge or invoke PR-40. The previously prepared post-merge handoff is not the current next action. The final user-facing return carries this result's actual direct Drive link only after its successful upload/readback and ends with the single complete RS-20 invocation.
