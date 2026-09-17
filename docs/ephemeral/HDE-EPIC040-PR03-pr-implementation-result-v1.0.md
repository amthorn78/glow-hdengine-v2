# HDE-EPIC040-PR03 — PR Implementation Result v1.0

```yaml
artifact_type: PR_IMPLEMENTATION_RESULT
PR_IMPLEMENTATION_RESULT_ID: HDE-EPIC040-PR03-PR-IMPLEMENTATION-RESULT
version: v1.0
state: MERGE_PENDING
readiness: Ready to merge
capture_utc: 2026-09-14T09:09:46Z
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040
WORK_UNIT_ID: HDE-EPIC040-PR03
work_unit_title: Pure Gate mechanics and intrinsic identity
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: dedicated PR engineering session for HDE-EPIC040-PR03
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR03 / PR-30
context_conflict: NONE
PO_PROCEED: GRANTED_FOR_EXACT_PLAN_ONLY
PR_IMPLEMENTATION_PLAN_ID: HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN
plan_version: v1.0
repository: amthorn78/glow-hdengine-v2
target: main
branch: hde-epic040-pr03-pure-gate-core
implemented_head: ad1fb9251cfbcb00405905aec4b8381a7ec54f4c
implemented_tree: 4af351d6f7347541b9853927bf5098299adcc81f
reviewed_source_head: c79bd090aa97627cfb72215762140a55992134eb
reviewed_source_tree: 4af351d6f7347541b9853927bf5098299adcc81f
baseline_head: 5b2fb8d70924a6710b6261fc0c93d3869fed6380
baseline_tree: e43c2063599e7bc449f20d4ab045d32d95581bf4
PR_REFS:
  - https://github.com/amthorn78/glow-hdengine-v2/pull/405
code_review: COMPLETE
security_review: COMPLETE
open_engineering_findings: 0
final_hosted_ci: SUCCESS
final_ci_run_id: 34824825198
final_ci_attempt: 1
final_ci_job_id: 103914417233
candidate_clean: true
merge_execution: NOT_EXECUTED
PR40_execution: NOT_EXECUTED
PR03_lineage_acceptance: NOT_YET_REVIEWED
RESCOPE_REQUEST: NOT_PRODUCED
PF10_BUILD_NOTES_ADDENDUM: NOT_PRODUCED
independent_QA_Ops_deployment_release_activation_Epic_closure: NOT_EXECUTED
output_classification: EPHEMERAL_DRIVE
output_destination: Glow / Ephemeral Planning Files
output_parent_id: 1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc
```

**MERGE_PENDING — Ready to merge [PR #405](https://github.com/amthorn78/glow-hdengine-v2/pull/405).** The proceeded pure Gate kernel, intrinsic identity, bounded test/caller migrations, and governed evidence are complete. Code and security reviews completed before final exact-head hosted CI. All seven selected lanes succeeded on `ad1fb9251cfbcb00405905aec4b8381a7ec54f4c`; there are no open engineering findings. The current PR is open, out of draft, mergeable, and clean, with no auto-merge enabled. Nathan's manual merge and the separate PR-40 lineage verdict remain future facts.

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

## Delivered behavior and interface seams

The exact entrypoint is `compute_core(member_a, member_b, mechanics_bundle, release_id)`: four required positional-or-keyword arguments, no defaults, variadic option, selector, or CoreConfig. It consumes accepted PR02 `NormalizedGates` and an injected `AdmittedMechanicsBundle`. It neither normalizes malformed inputs into success nor loads configuration or schemas.

| Owner | Delivered responsibility |
| --- | --- |
| `engine/magic10/composite.py` | Immutable Channel classifications; one traversal of the accepted 36-row registry; five-state priority; numerically ordered masks and `member_lo`/`member_hi` ownership only for dominance and compromise |
| `engine/magic10/signals.py` | Immutable signal rows; strict injected profile/operation/channel/weight checks; integer-only ordinary, equilibrium, and counterweight calculations; exactly 20 rows in flattened caps order |
| `engine/magic10/calculators.py` | Two-input caps in doubled-q units; exact positive integer weights; one half-up weighted reduction and final clamp; fixed inclusive Cool/Open/Warm/Glow bands |
| `engine/core/core.py` | Input and admitted graph invariants; source/config/release coherence; one classification call; ordered assembly; intrinsic chart fingerprints and pair key; immutable six-field result and final relational closure checks |
| Both package `__init__.py` files | Remove old precomputed-score/calculator exports; expose only the coherent core entrypoint/result surface |

Ordinary signal q is `(N + 25*W) // (50*W)`. Equilibrium q is `(800*min(lo_mass, hi_mass) + W) // (2*W)`. Counterweight q is `(400*matching_mass + W) // (2*W)`. Category scores use capped half-unit q values and `(weighted_q + total_weight) // (2*total_weight)`, clamped once to `0..100`. The implementation consumes the admitted map and values; it does not define another runtime signal map or retune profiles, caps, weights, or formulas.

Each chart fingerprint hashes exactly `schema=magic10_chart_fingerprint.v1` plus a 16-character lowercase Gate mask. The pair preimage has exactly config ID, ordered fingerprint members, release ID, result schema, and `schema=magic10_pair_preimage.v1`. Numeric mask order controls membership; equal masks retain two equal fingerprints. Canonical bytes come only from the unchanged shared serializer. No person UUID, birth data, viewer, request, clock, random value, cache, narrative, or repository commit is a core identity input.

`CoreResult` has exactly `schema`, `config_id`, `release_id`, `pair_key`, `signals`, and `categories`. Frozen slotted records and tuples preserve the in-process result. Projection returns ordinary dict/list scalars without mutating that result. The unchanged PR01 result schema validates projected output; order, types, ranges, and bands are also checked before return. Invalid input is refused as the value-free `ValueError("invalid pure core contract")`, with no partial result or successful legacy fallback.

## Requirement coverage

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

PR02 F01/F02/F03 overlays remain effective only for accepted PR02. PF10 v13.2.4 §2.11 accepts PR02 without granting PR03 scope changes. No conflict was reopened, relabelled, omitted, or decided anew. No material PR03 boundary or qualifying PF10 addendum was produced.

## Exclusions, risks, and recovery ownership

The actual manifest still has 15 members. PR03 tests and core evidence consume explicitly synthetic complete fixtures; no actual 44-member release was materialized, promoted, activated, or claimed ready. Accepted result/config contract bytes, Gate normalization, admission/loader behavior, serializer ownership, and PR04 application sources remain unchanged.

PR04 application eligibility, same-person handling, orientation, cache, transport and narratives; PR05 complete golden readiness; PR06 release materialization/promotion; PR07 documentation; OPS01; independent QA/Ops; deployment; PF10 or other Canon edits/drainage; and Epic closure are not delivered here. No public/API/CLI field, selector, bypass, alternate calculator, persistent cache, remote schema, live vendor/database access, or stronger atomicity guarantee was introduced.

Engineering results apply to the identified source/tree and synthetic fixtures. They do not establish later application behavior or actual release readiness. Those are deliberately deferred work-unit obligations. Permanent C040-05/C040-06 Canon maintenance and repository prompt-use persistence remain with their authorized owners and are non-gating.

Recovery retains the same dedicated PR03 session, `/workspace/scratch/808bf6c1dac3/pr03`, branch `hde-epic040-pr03-pure-gate-core`, the ordered commits and PR #405, local logs, governed evidence, and original Proceed. The accepted PR02 worktree at `/workspace/scratch/b736cdb96988/pr02-recovery` was not repurposed. The exact main commit was recovered from authenticated GitHub commit data and verified by its Git object hash before creating the fresh PR03 worktree. Terminal Git authentication and `gh` were unavailable; authenticated GitHub tools handled remote publication, and exact remotely created commits were restored locally with SHA verification. This is a completed supported recovery, not an unresolved access dependency.

An ordinary future in-scope defect stays with this PR03 engineering owner under the original Proceed and preserved PR. A genuine material implementation boundary requires a formal bounded `RESCOPE_REQUEST` directly to the same retained whole-change IA through selected RS-20; no approved base is rewritten and no replacement Proceed is requested. This result does not execute that route.

## Engineering review and finding disposition

Substantive code and security review used the repository's configured `chatgpt-codex-connector` review mechanism against the complete candidate. These are engineering reviews, not PR-40 acceptance or Isis approval. The engineer's own inline replies are not counted as independent reviews.

| Review event | Actual evidence / result |
| --- | --- |
| Code review request | [Request](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661170021), exact head `c79bd090aa97627cfb72215762140a55992134eb`, all 39 changed paths and controlling plan |
| Security review request | [Request](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661170238) |
| Security result | [Substantive result](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661215092): completed with no security issues found, reviewed commit `c79bd090aa`; the ready-for-review pass also completed at `2026-09-14T08:37:20.438139Z` |
| First code review result | [Review 5195614146](https://github.com/amthorn78/glow-hdengine-v2/pull/405#pullrequestreview-5195614146), `COMMENTED`, `2026-09-14T08:40:26Z`; one P2 threshold finding |
| Finding investigation and reproduction | [Source-backed reply](https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4003526009); real loader refuses coherently rehashed tuned thresholds before returning an admitted bundle |
| Requested re-evaluation | [Same-head re-review request](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661344028) |
| Final substantive code result | [Code re-review result](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661392031): no major issues found on unchanged `c79bd090aa`; completed `2026-09-14T08:48:22.602140Z` |
| Finding disposition | [Resolution record](https://github.com/amthorn78/glow-hdengine-v2/pull/405#discussion_r4003568397), `2026-09-14T08:50:15Z`; thread `PRRT_kwDOP103ks6iCnlF` was resolved by the PR engineering owner after the source-backed investigation and completed re-review |
| Current review summary | [Configured review summary](https://github.com/amthorn78/glow-hdengine-v2/pull/405#issuecomment-5661172743); both required reviews complete |

**PR03-R01 — P2, threshold injection:** The reviewer proposed carrying tuned threshold values through the admitted bundle and using them in reduction/result validation. Engineering disposition is **NOT_APPLICABLE_TO_ADOPTED_INITIAL_RELEASE / RESOLVED**, not a waiver or a claimed code fix. The accepted active loader always calls `_validate_initial_mechanics`; it refuses any edges other than `[24,49,74,100]` with `INITIAL_THRESHOLDS_MISMATCH`. The lower-level domain validator is not an admission path. Detailed plan §5.5 explicitly requires the adopted fixed inclusive bands and relies on that accepted admission check. PF01 §5.2.8 treats band tuning as a separately adopted public-contract change, while §5.3 specifies the present maxima. Future tuning support cannot be introduced by silently changing accepted PR02 scope.

The actual closed-rails reproduction used the complete synthetic release helper, admitted its unchanged baseline, changed only the temporary threshold edges to `[20,45,70,100]`, updated the mechanics threshold-source hash, and regenerated all manifest member hashes/sizes with the owning fixture writer. Active admission refused with `INITIAL_THRESHOLDS_MISMATCH`; no tuned admitted bundle was returned and core was not reached. This was read-only review analysis of PR03's consumed interface, not reopening accepted PR02 delivery or lineage review. The repository remained clean.

Reproduction evidence retained in the recovery workspace:

- `threshold-review-repro.py`, SHA-256 `3f2db01a5c4382adb4cb2b48a530ad1f48e5c9f097dff329477dd92695786b82`.
- `threshold-review-repro.log`, SHA-256 `8778018f4475edb61437b7ba8a6070785fa490f8be608058168b6418eaecd821`.
- Observed results: `baseline_admission=PASS`; `tuned_admission=REFUSED`; `refusal_code=INITIAL_THRESHOLDS_MISMATCH`; `tuned_AdmittedMechanicsBundle=NOT_RETURNED`.

No code correction, accepted bundle/schema change, mathematical tuning, approved-base rewrite, rescope, or new Proceed was needed. The final code re-review was read in full alongside the original finding, complete inline replies, security result, and actual resolved-thread state. No in-scope engineering finding remains open.

## Publication and exact source attribution

| Order | Commit | Parent | Tree | Purpose |
| --- | --- | --- | --- | --- |
| Baseline | `5b2fb8d70924a6710b6261fc0c93d3869fed6380` | `3828d4b3454259841a3e48d13039dd1475754f2f` | `e43c2063599e7bc449f20d4ab045d32d95581bf4` | Accepted PR01/PR02 target main |
| PR03 1 | `c79bd090aa97627cfb72215762140a55992134eb` | `5b2fb8d70924a6710b6261fc0c93d3869fed6380` | `4af351d6f7347541b9853927bf5098299adcc81f` | Complete locally tested implementation, bounded tests/CI owners, and converged evidence; reviewed candidate |
| PR03 2 | `ad1fb9251cfbcb00405905aec4b8381a7ec54f4c` | `c79bd090aa97627cfb72215762140a55992134eb` | `4af351d6f7347541b9853927bf5098299adcc81f` | Empty source-diff commit created after review completion to trigger final exact-head CI |

There is exactly one PR03 PR: [amthorn78/glow-hdengine-v2 #405](https://github.com/amthorn78/glow-hdengine-v2/pull/405), branch `hde-epic040-pr03-pure-gate-core`, target `main`. It was deliberately published after complete local validation. The draft-to-ready transition triggered the repository's configured review pass, which was allowed to finish before final CI.

The review checkpoint used [GitHub's documented CI-skip commit directive](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/skip-workflow-runs) to defer hosted CI during review. The observed workflow-run list for that exact checkpoint was empty before final publication. After both reviews and the finding disposition were complete, the final commit preserved the identical Git tree and changed no files. Pre-publication clean/diff and governed integrity checks passed again; the remote ref advanced by fast-forward. Review and local behavioral evidence therefore cover the final source bytes; final hosted CI separately identifies the later exact head. No earlier run is relabelled as having executed the later commit.

**Manual squash-message consideration:** The repository currently uses `squash_merge_commit_message=COMMIT_MESSAGES`. A default squash message would inherit the review checkpoint's CI-skip directive and could suppress the later main push workflow. For Nathan's manual squash merge, omit that review-only directive. A clean proposed merge message is:

```text
HDE-EPIC040-PR03: Pure Gate mechanics and intrinsic identity (#405)

Implement the proceeded four-argument pure Gate kernel, ordered Magic10
signals and categories, intrinsic identity, and closed immutable result.
Migrate bounded tests and existing core evidence through their owners.
Preserve accepted PR01/PR02 contracts and the actual 15-member manifest.
```

This is concrete merge-message guidance, not another approval object or permission for an agent to merge. No merge, auto-merge, merge queue, deployment, or release activation was performed.

## Prompt-use provenance and next owner

`GCFPE_PROMPT_USES` is carried in this permitted runtime result. No prompt body or new provenance procedure was added to the repository.

| Usage | Exact lineage |
| --- | --- |
| Inherited PR-10 | `GCFPE-USE-HDE-EPIC040-PR-10-20260914-PR03-01`; complete retrievable use entry in controlling instruction §15; [PR-10 091326.2](https://app.notion.com/p/3da4590a05eb81c594a0f9bf5cb151a7?pvs=204) |
| Inherited PR-20 | `GCFPE-USE-HDE-EPIC040-PR-20-20260914-PR03-01`; complete retrievable use entry in detailed plan §16; [PR-20 091326.2](https://app.notion.com/p/3da4590a05eb8147b34ccfabf608c2e3?pvs=204) |
| Current PR-30 | `GCFPE-USE-HDE-EPIC040-PR-30-20260914-PR03-01`; `EPIC / HDE-EPIC040 / HDE-EPIC040-PR03`; approved Specification v1.1; K040-REQ-001/002/005/007–013 as allocated; `GCFPE-20260913.1`, 54 members; [PR-30 — PR Implementation Proceed — 091326.2](https://app.notion.com/p/3da4590a05eb81c0aee0d0862b242e09?pvs=204); retrieved revision `2026-09-13T11:35:45.977Z`; role/stage dedicated PR03 engineer / PR-30; capture time is this result's actual UTC capture; execution identity is the supplied dedicated-session role reference, with no invented platform ID; actual PR and ordered commits are recorded above |

`docs/changes/GCFPE_PROMPT_PROVENANCE.md` was absent in the inspected repository. Repository persistence remains `PENDING / NON_GATING` for a later authorized repository writer under an actually installed supported procedure. PR-40 was resolved and read only to prepare the conditional handoff; it was **NOT EXECUTED** and no PR-40 use or verdict is claimed.

The next native receiver, only after Nathan's actual manual merge, is the **retained whole-change HDE-EPIC040 Implementation Architect in its established read-only PR lineage-review role**, as instruction §14 specifies. It is not the PR03 engineer or Isis-50. The exact selected destination is [PR-40 — Review PR Work-Unit Lineage — 091326.2](https://app.notion.com/p/3da4590a05eb813c8b47e77f94ff1def?pvs=204), retrieved revision `2026-09-13T11:35:46.151Z`.

That receiver must consume this exact implementation result, the complete instruction and detailed plan, all approved whole-change and accepted dependency lineage, ordered PR #405/commit evidence, actual merge facts, engineering review/CI evidence, exclusions, the carried Canon register, and any actual recovery limits. It independently returns one `PR_WORK_UNIT_LINEAGE_REVIEW` with `ACCEPT`, `REJECT`, or `PENDING` and its native owner handoff. Existing PR01/PR02 acceptance remains final. PR03 engineering readiness does not supply the later merge or acceptance fact.

## Final exact-head hosted CI and current repository facts

The final gate is [CI run 34824825198](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34824825198), workflow `ci` / ID `192291018`, run number `3568`, attempt `1`, event `pull_request`. GitHub reports `completed / success` for exact head `ad1fb9251cfbcb00405905aec4b8381a7ec54f4c`. It was created at `2026-09-14T08:51:08Z`, after final code re-review (`08:48:22Z`) and finding resolution (`08:50:15Z`), and completed by `2026-09-14T09:02:59Z`.

The associated [check/job 103914417233](https://github.com/amthorn78/glow-hdengine-v2/actions/runs/34824825198/job/103914417233) is named `test`, started `2026-09-14T08:51:11Z`, completed `2026-09-14T09:02:58Z`, and reports `success` on that same head. The repository exposes these seven lanes as steps in this one check; this result does not invent seven separate GitHub checks. The legacy combined-status endpoint contains no legacy statuses; the actual Actions check/run and complete logs supply the gate evidence.

| Selected hosted step / lane | Actual conclusion and observed test results |
| --- | --- |
| Exact candidate checkout / classification | SUCCESS; head `ad1fb9251cfbcb00405905aec4b8381a7ec54f4c`; 39 changed paths; all seven lanes selected |
| Python/dependencies/pytest/closed environment | SUCCESS; Python 3.12; required closed deterministic pins verified |
| Affected behavioral tests, isolated clean source | SUCCESS; 1,899 passed in 118.58s |
| product | SUCCESS; ordering checks and 20 passed |
| compat | SUCCESS; CLI/serializer/emitter checks and 62 passed, 3 skipped, 2 xfailed |
| db | SUCCESS; direct runtime-contract checks and 249 passed |
| rails | SUCCESS; three definition test groups 4 / 108 / 39 passed, their proof checks, and workflow integration 124 passed |
| evidence | SUCCESS; all read-only governed integrity checks and 111 passed in 388.58s |
| qa | SUCCESS; approved generic subsystem regression roster, 488 passed in isolated source |
| release | SUCCESS; 52 passed, unchanged actual-manifest check, external exact-source attestation build and verify with `--require-clean` |
| Truthful applicability / clean candidate audit | SUCCESS; every selected outcome is success; diff checks and untracked-file check clean; actual `CI_APPLICABILITY_AND_EXACT_HEAD_OK` at `2026-09-14T09:02:55.4469982Z` |

The three compatibility skips are the existing vendor-dependent tests under closed rails; the two expected failures are the existing `/internal/version` untouched-scope cases, matching the local roster. No lane or PR03 requirement was waived. Hosted and local counts overlap and are not summed. No later source mutation, fixup, merge, or CI rerun occurred after this successful final candidate.

The complete decoded hosted job log is preserved in the recovery workspace as `pr03-final-hosted-ci.log` (65,384 bytes; SHA-256 `97b11f525387db448066a626e456d00a34d50e62d1a56f0689ba8128304692e4`). The saved structured run/check/step/PR/thread snapshot is `pr03-final-ci-snapshot.json` (SHA-256 `3beb53c1ade99d7ccf6c19e4e205316a79500db73864d0f7ce23aa19c5762167`). Direct GitHub run, job, review, and commit links above remain the independently retrievable hosted evidence. The full log was inspected for applicability, exact head, per-lane results, external attestation, and final clean-tree outcome.

The post-CI remote read shows PR #405 open, `draft=false`, `merged=false`, `mergeable=true`, `mergeable_state=clean`, `auto_merge=null`, two commits and 39 changed paths. Head remains `ad1fb9251cfbcb00405905aec4b8381a7ec54f4c`; target main remains `5b2fb8d70924a6710b6261fc0c93d3869fed6380`. The local head/tree match and `git status --porcelain=v1` is empty. GitHub's provisional merge-test SHA is not treated as an actual merge fact. All inline threads are resolved.

## Exact bounded file inventory

All rows below are the complete main-to-final-head inventory: **39 paths**, 1,962 additions and 1,039 deletions, across the two ordered PR03 commits. SHA-256 values identify final file bytes at Git tree `4af351d6f7347541b9853927bf5098299adcc81f`; paths are repository-relative. The final commit itself has zero file differences from the reviewed checkpoint. Governed generated files remain at their existing registered paths.

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

## Final boundary and exact next action

No outstanding in-scope implementation, evidence, review, or CI defect remains. The bounded limitations are the intentionally incomplete actual release, future application/full-golden work, the already assigned permanent Canon drainage, and non-gating prompt-use repository persistence. These limitations are carried to PR-40; they are not converted into PR03 success claims for later units.

Nathan / Product Owner performs the manual merge of PR #405 when ready. If squashing, use the clean proposed message in this result and omit the review-only CI skip directive from the default concatenated message. The dedicated PR03 engineering session performs no merge action and does not wait for or poll that manual act.

Only after actual manual merge, invoke **PR-40 — Review PR Work-Unit Lineage — 091326.2**, [direct selected prompt](https://app.notion.com/p/3da4590a05eb813c8b47e77f94ff1def?pvs=204), in the retained whole-change HDE-EPIC040 Implementation Architect's established read-only lineage-review role. Pass this exact result v1.0, instruction v1.0, detailed plan v1.0, all approved/accepted lineage and current PF10 links in this result, ordered PR #405/commit identities, review/finding/CI evidence, carried Canon register, exact preserved recovery ownership, and actual merge evidence. The final operator return supplies the result's direct Drive link after its upload and complete readback; no future provider ID is invented here.

PR-40 independently verifies actual merged state and attributable landed PR03 behavior against the immutable approved bases. An unmerged PR or missing merge evidence is pending, even though this historical PR-30 result is MERGE_PENDING/Ready to merge. That reviewer saves and reads back one PR_WORK_UNIT_LINEAGE_REVIEW with ACCEPT, REJECT, or PENDING and the native owner handoff. It does not rewrite this historical result to fabricate later facts, reopen accepted PR01/PR02, implement, perform QA/Ops, edit PF10/Canon, activate releases, or close the Epic.
