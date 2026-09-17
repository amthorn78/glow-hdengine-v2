# HDE-EPIC040-PR03 — PR Implementation Plan v1.0

## 1. Identity, state, and authority boundary

| Field | Value |
| --- | --- |
| artifact_type | `PR_IMPLEMENTATION_PLAN` |
| PR_IMPLEMENTATION_PLAN_ID | `HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN` |
| version | `v1.0` |
| state | `AWAITING_PO_PROCEED` |
| CHANGE_CLASS | `EPIC` |
| CHANGE_ID | `HDE-EPIC040` |
| WORK_UNIT_ID | `HDE-EPIC040-PR03` |
| work_unit_name | Pure Gate mechanics and intrinsic identity |
| producer_role | Dedicated PR engineering session for exactly HDE-EPIC040-PR03 |
| session_disposition | `INITIAL_DEDICATED_ASSIGNMENT` for PR-20; PR-30 continues this same session as `RETAIN_EXISTING` |
| role_session_ref | dedicated PR engineering session for HDE-EPIC040-PR03 |
| execution_posture | `MANUAL_PROMPT_EXECUTION` |
| planning_time_utc | `2026-09-14T07:23:20Z` |
| native_next_owner | Nathan / Product Owner for the exact PR-30 Proceed decision |

This plan is complete for the exact approved PR03 work unit and is ready for the Product Owner's decision. `AWAITING_PO_PROCEED` is not implementation authority. No repository mutation, branch, commit, push, pull request, review, CI run, merge, QA, Ops, release activation, PF10 edit, Canon drainage, or Epic closure was performed by PR-20.

The only implementation authority is Nathan / Product Owner's manual invocation of selected `PR-30 — PR Implementation Proceed — 091326.2` against this exact plan version and the exact PR instruction below. That Proceed authorizes implementation of this plan only. It supplies no merge authority.

## 2. Exact controlling lineage and source record

### 2.1 Approved and accepted change lineage

| Role | Exact artifact and current decision |
| --- | --- |
| PR instruction | [HDE-EPIC040-PR03 PR Work-Unit Instruction v1.0](https://drive.google.com/file/d/1Zj5BResRRxtGarmZ2d3sIAfIVeLD42rs/view?usp=drivesdk); `HDE-EPIC040-PR03-PR-INSTRUCTION`; `INSTRUCTION_READY`; SHA-256 `4f45fff6ecd79b85f7b0d97f57056d1bd8e896eaff53fce81567ee0d08446895`; 462 lines; 39,975 bytes |
| Approved Specification | [HDE-EPIC040 Specification v1.1](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk); `HDE-EPIC040-SPECIFICATION`; Thoth-17 `APPROVE` |
| Fresh whole-change Audit | [HDE-EPIC040 Implementation Audit v2.0](https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk); `AUDIT_COMPLETE` |
| Immutable whole-change Plan | [HDE-EPIC040 Implementation Plan v2.1](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk); SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| Approving Plan review | [HDE-EPIC040 Implementation Plan Review v2.1](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk); Isis-50 `APPROVE`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Accepted PR01 dependency | [HDE-EPIC040-PR01 Lineage Review v1.1](https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk); `ACCEPT`; PR #403 accepted-final |
| Accepted PR02 dependency | [HDE-EPIC040-PR02 Lineage Review v1.0](https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk); `ACCEPT`; PR #404 accepted-final |
| Current Build Notes overlay | [PF10 — HDE Build Notes v13.2.4](https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk); unique current controlled Markdown; §2.11 records PR02 acceptance |

The accepted PR02 F01, F02, and F03 overlays remain effective only for the accepted PR02 work unit. They do not rescope PR03, reopen PR02, authorize another roster or manifest change, or move any PR04 through PR07 responsibility.

### 2.2 Controlled subject-matter sources used

The planning source predicate was proven through Drive direct-parent traversal: My Drive root `0ANCzbmSbmO_HUk9PVA` → `Glow` `1MZXcC5tKMkI9n8EobkywIj1ifcF6IvZ3` → `Core Docs` `18T84WC_Jxjb75V37_eYcRqn8zOjHYgxu` → `PFCanon` `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3`. Only direct-child controlled Markdown was used; no Google Doc, DOC, or DOCX PF item was used.

| Owner | Selected controlled Markdown and applicable scope |
| --- | --- |
| PF01 — HDE Math Spec | [v1.3.7](https://drive.google.com/file/d/1ILESkXCDr11Me6WvCBPpebfmQFwEz63p/view?usp=drivesdk); §5.2 Gate-state mechanics, signal/category math, fingerprint/pair identity and G001–G006; §§6.1–6.2 state predicates |
| PF02 — HDE Architecture | [v2.4.5](https://drive.google.com/file/d/1y4JvZKVZR_5J_wynT4p3HtYgX4cRSIB6/view?usp=drivesdk); §§2.1–2.2 single pure core and data-in/data-out boundary |
| PF03 — Technical Writing Best Practices | [v1.8.7](https://drive.google.com/file/d/1M_PTWi-ySFs1NWIjFpd9p2IL-vsKbJEA/view?usp=drivesdk); truth/source fidelity, claim-state separation and executable-plan writing |
| PF05 — HDE CLI/API/Vendor Ref | [v2.5.2](https://drive.google.com/file/d/1P78CNLZhAIYYTHXOAi2aX1HoImo9TuXo/view?usp=drivesdk); failure/privacy boundary only; PR03 adds no public carrier |
| PF09.3 — Separation checklist | [v1.1.5](https://drive.google.com/file/d/1JLCCfPPryE_EG_62B1PHSZ2QGKvGsolp/view?usp=drivesdk); status/context only; the approved Epic scope remains the pinned six-unit selection |
| PF12 — HDE Schemas and Artifacts | [v2.9.6](https://drive.google.com/file/d/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ/view?usp=drivesdk); §2.9 config/result closure and §8.6.3.8 core evidence family/index companions |
| PF14 — HDE Mechanics Guide | [v3.5.7](https://drive.google.com/file/d/13kNlj4Y_F1fIqE3_L4eyjeJUkdO3LkX1/view?usp=drivesdk); §§6–7 pure mechanics and evidence; legacy §6.7 passages are governed by decided C040-05 alternative A |
| PF10 — HDE Build Notes | [v13.2.4](https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk); §§2.3, 2.5, 2.7, 2.9, 2.10 and 2.11 |

### 2.3 GCFPE execution sources

- PR-20 source: [PR-20 — Create Detailed PR Implementation Plan — 091326.2](https://app.notion.com/p/3da4590a05eb8147b34ccfabf608c2e3?pvs=204), selected in release `GCFPE-20260913.1`, retrieved revision `2026-09-13T11:35:45.616Z`.
- PR-30 destination: [PR-30 — PR Implementation Proceed — 091326.2](https://app.notion.com/p/3da4590a05eb81c0aee0d0862b242e09?pvs=204), selected in the same release.
- Direct-Handoff and Runtime Artifact Operating Procedure revision 3.1.0 applies. The active automation hold permits this explicit manual prompt execution and prohibits hidden, scheduled, or automated dispatch.

## 3. Repository baseline and planning inspection

### 3.1 Exact baseline

| Field | Observed value |
| --- | --- |
| Repository | `amthorn78/glow-hdengine-v2` |
| Target branch | `main` |
| Target head | `5b2fb8d70924a6710b6261fc0c93d3869fed6380` |
| Target tree | `e43c2063599e7bc449f20d4ab045d32d95581bf4` |
| Local inspection reference | clean accepted PR02 pre-squash head `d534e0f16c067c7f1b35980e804397083c2c5b9a`, with the same exact tree `e43c2063599e7bc449f20d4ab045d32d95581bf4` |
| Existing PR03 state | no PR03 branch, commit, pull request, detailed Plan, Proceed, implementation, review, CI, or merge found or supplied |

The local PR02 branch is inspection evidence only and must not be repurposed. PR-30 first recovers any genuinely matching PR03 state; if none exists, it creates a dedicated PR03 worktree and branch from the then-current verified `main`. An unrelated head movement is not automatically a material boundary. Any change touching this plan's owned interfaces must be compared against the approved contract; incompatible drift returns through the bounded rescope route before affected implementation.

### 3.2 Current implementation facts

- `engine/core/core.py` is the superseded DISS004 scaffold. It accepts two `ParticipantState` values with `compat_score`, accepts optional/default `CoreConfig`, averages precomputed scores, and returns the legacy participant/perspective shape.
- `engine/magic10/calculators.py` reads `catalog/magic10_caps.json` and `catalog/magic10.json` at import, converts arbitrary values through `Decimal(str(value))`, registers a category calculator globally, and exposes the old payload-to-score API.
- `engine/magic10/thresholds.py` remains a legacy direct helper. PR03 does not modify it, import it from the new pure path, or expose it through `engine.magic10`; retaining its unrelated source file does not preserve an alternate successful core path.
- `engine/magic10/composite.py` and `engine/magic10/signals.py` do not exist in the accepted tree.
- The only direct `compute_core` callers are the two bounded core behavioral tests and `tools/evidence/generate_engine_core_evidence.py`. No PR04 application source currently calls `compute_core`.
- The three `tests/m10/test_*` modules and `tests/evidence/test_canonical_json_gate_check_outputs.py` import transitional `CATEGORY_INPUTS`, `calculator_ids`, or `compute_category`; they require bounded migration when those exports are removed.
- PR02 supplies frozen `NormalizedGates` in `engine/bodygraph/gates.py` and frozen `AdmittedMechanicsBundle` in `engine/config/registry_loader.py`. The actual installed 15-member manifest intentionally refuses complete admission; `tests/config/helpers.py::synthetic_complete_release_root` supplies the labeled 44-member complete test release.
- The pure result schema already exists at `schemas/magic10_result_v1.schema.json`. It is not modified by PR03.
- The existing core evidence writer owns four primary paths and four existing schema companions. The Evidence Index updater owns the Human Index, sentinel, Machine Mirror, mirror digest, orientation output and path proofs.
- `ci/checks/classify_ci_changes.py` currently has no product-owner mapping for the PR03 core modules and no evidence-generator owner entry for `generate_engine_core_evidence.py`. Without a bounded ownership update, a generator change fails with `CI_EVIDENCE_OWNER_TEST_MISSING`.

## 4. Exact objective, completion conditions, and exclusions

### 4.1 Objective

Replace the successful precomputed-score scaffold with one exact four-argument, injected, integer-only, pure Gate kernel:

```python
compute_core(member_a, member_b, mechanics_bundle, release_id)
```

The kernel consumes two already validated `NormalizedGates`, one already admitted immutable `AdmittedMechanicsBundle`, and the exact release identity. It classifies all 36 Channels once; computes the 20 ordered signals and 10 ordered category scores/bands; constructs intrinsic chart fingerprints and pair identity; and returns one closed, immutable `magic10_result.v1` value. It performs no configuration loading, I/O, environment access, clock/random use, identity/UUID processing, caching, narratives, transport, or persistence.

### 4.2 Completion conditions

PR03 reaches engineering `MERGE_PENDING` only when all of the following are true on one exact final head:

1. The old three-argument/default `CoreConfig` and `compat_score` success paths and their exports/tests are absent.
2. The new pure implementation satisfies all 16 classifier cases, exact formulas, ordered result closure, G001–G006, AB↔BA, equal-mask and two-run proofs.
3. The output is immutable in-process and its projected payload validates against the unchanged `schemas/magic10_result_v1.schema.json` with exact relational order/identity checks.
4. Every directly affected test and evidence owner has been migrated; no application behavior is enabled.
5. The four existing core evidence primaries, four schemas, all required updater-owned companions, and their focused validation agree.
6. Focused tests, the complete configured default suite, every locally applicable CI command, substantive code review, substantive security review, and final exact-head hosted CI have successful current evidence.
7. The actual 15-member manifest, accepted PR01/PR02 behavior, public/API/CLI surfaces, PF10 and later-unit scope remain unchanged.

### 4.3 Hard exclusions

This plan excludes PR04 eligibility, UUID/self handling, application orientation, narrative keys, internal augmentation, cache I/O, Reader/CLI/HTTP/transport projection; PR05 complete G001–G008 comparator/readiness; PR06 actual 44-member manifest materialization, identity convergence, release promotion; PR07 documentation; OPS01; independent QA; deployment; vendor/database access; PF10 edits; permanent Canon drainage; Epic acceptance or closure.

It also excludes a new public field, API/CLI selector, hidden flag, optional configuration, alternate calculator, duplicate catalog/schema/serializer owner, remote schema resolution, persistent cache, live data, stronger multi-file/cross-process atomicity guarantee, configuration retuning, or expected-output regeneration from current output.

## 5. Designed internal interfaces and invariants

### 5.1 Immutable value types

Use `@dataclass(frozen=True, slots=True)` for internal/result records and tuples for ordered collections. Proposed private/internal records are:

- `ChannelClassification(channel_id, state, owner)`, where `state` is exactly `none`, `companionship`, `compromise`, `dominance`, or `electromagnetic`; `owner` is `member_lo`, `member_hi`, or absent and is present only for compromise/dominance.
- `SignalValue(signal_id, q)`.
- `CategoryValue(category_id, score, band)`.
- `CoreResult(schema, config_id, release_id, pair_key, signals, categories)`, with exactly those six fields and no participant/config/request metadata.

Keep these records in their owning modules and export only the minimum coherent result/entrypoint surface through `engine.core`. Do not add caller-configurable knobs. A private, value-free `ValueError` subclass or equivalent internal refusal may distinguish contract failures for tests, but it is not exported as a public/API/CLI token and must never echo input payloads.

### 5.2 Pure input guard

At `compute_core` entry:

1. Require exact `NormalizedGates` instances. Recheck nonempty ascending unique exact built-in integers in `1..64`; recompute `mask`; require `0 < mask < 2**64`; require exact `mask_hex == f"{mask:016x}"`. This rejects directly forged inconsistent frozen objects without re-normalizing malformed input into success.
2. Require an exact `AdmittedMechanicsBundle`, recursively immutable mappings/tuples for the computation-relevant graph, and the admitted registry/mechanics relationships required below. Do not call either loader or schema I/O.
3. Require `release_id` to be an exact built-in string matching lowercase `[0-9a-f]{64}` and exactly equal to `mechanics_bundle.release_id` and `mechanics_bundle.manifest_sha256`.
4. Require exact `result_schema == "magic10_result.v1"`, nonempty exact `config_id`, complete 36-Channel registry, complete ordered 20-signal mechanics, complete ordered 10-category weights and caps closure.
5. Refuse before producing any `CoreResult` when any invariant is missing, extra, duplicated, unknown, mutable, malformed, out of order, out of range, or incoherent.

This is a consumer invariant check over a PR02-admitted object, not a second loader or schema parser. PR02 retains all raw bytes, path, canonicalization, manifest and schema admission ownership.

### 5.3 `engine/magic10/composite.py`

Implement one pure classifier over the bundle's 36 ASCII-sorted canonical Channel rows. For each Channel, derive lower/higher endpoint presence from the two masks and apply the exact first-match priority:

1. companionship: both members have both endpoints;
2. compromise: one member has both endpoints and the other exactly one endpoint;
3. dominance: one member has both endpoints and the other neither endpoint;
4. electromagnetic: neither has both endpoints and they hold opposite single endpoints;
5. none: all remaining cases.

Before classification, order the two intrinsic members by numeric Gate mask as `member_lo` and `member_hi`. Normalize a full owner only for compromise/dominance. Equal masks remain two equal intrinsic members and never use identity as a tie-break. Classify each Channel exactly once. The complete result is 36 records in ASCII Channel-ID order. Explicitly assert that `10-20`, `10-57`, `20-34`, and `34-57` are the catalog's Integration members while `10-34` is Centering and `20-57` is Knowing; these are catalog conformance checks, not scoring branches.

### 5.4 `engine/magic10/signals.py`

Consume the classified tuple and the injected frozen mechanics rows. Validate exact operation/profile/channel membership and positive built-in integer weights before arithmetic.

- Ordinary signal: `N = Σ(weight * response_for_state)`, `W = Σ(weight)`, `q = (N + 25*W) // (50*W)`.
- `equilibrium_score`: accumulate the selected one-owner Channel mass separately for `member_lo` and `member_hi`; with `m = min(lo_mass, hi_mass)` and `W = Σ(weight)`, compute `q = (800*m + W) // (2*W)`.
- `counterweight_ratio`: with `M` the selected weight whose state is companionship or electromagnetic and `W = Σ(weight)`, compute `q = (400*M + W) // (2*W)`.

Require `W > 0`; require every result to be an exact integer in `0..200`; round only through these formulas. Emit exactly 20 `SignalValue` rows in flattened caps-input order, not alphabetical order. No Decimal, float, string coercion, global calculator registry, file read, or mutable cache is permitted.

### 5.5 `engine/magic10/calculators.py`

Replace the old file-loading registry with a small injected integer reducer:

1. Receive one category's two already computed `q` values, its caps-owned lower/upper bounds, and its two mechanics-owned positive integer weights.
2. Compute `c_i = min(2*upper, max(2*lower, q_i))`.
3. With `B = w0 + w1` and `Q = w0*c0 + w1*c1`, compute `raw = (Q + B) // (2*B)` and clamp once to `0..100`.
4. Resolve exact inclusive bands: `0..24 Cool`, `25..49 Open`, `50..74 Warm`, `75..100 Glow`.

The unchanged admitted bundle has already verified `math/thresholds.json` against those adopted maxima; this pure reducer does not import the legacy file-reading `thresholds.py`. Remove `Magic10Result`, `Magic10Calculator`, `_CALCULATORS`, `CATEGORY_INPUTS`, `compute_category`, and `calculator_ids` as successful alternative runtime surfaces. Provide only private/internal helpers needed by `compute_core`, plus minimal imports if the module contract requires them.

### 5.6 `engine/core/core.py`

Coordinate without reclassification or alternate formulas:

1. Validate explicit arguments and bundle invariants.
2. Numeric-order the two masks and classify all Channels once through `composite.py`.
3. Produce 20 signals through `signals.py`.
4. Join each canonical category to exactly its two caps inputs and one category-weight row; reduce through `calculators.py`; emit 10 category rows in `registry.magic10_order`.
5. Build each chart fingerprint by SHA-256 of canonical bytes for a two-entry object whose `gate_mask_hex` value is the normalized numeric mask rendered as exactly 16 lowercase hexadecimal characters and whose `schema` value is exactly `magic10_chart_fingerprint.v1`.
6. Build `pair_key` by SHA-256 of canonical bytes for an object with exactly these lexicographically serialized entries: `config_id` equal to the admitted bundle config ID; `members` equal to `[fingerprint_lo, fingerprint_hi]`; `release_id` equal to the admitted bundle release ID; `result_schema` equal to `magic10_result.v1`; and `schema` equal to `magic10_pair_preimage.v1`. The members are in numeric mask order; equal masks retain two equal fingerprints.
7. Use `engine.serializer.canon.sercanon` for canonical bytes. That shared serializer is injected by import only and performs no I/O.
8. Construct the immutable six-field result, project it to ordinary dict/list scalars for schema/byte tests and evidence, and validate exact keys, order, ranges, identities and relational closure before returning. Do not load the JSON Schema in core.

The result cannot vary with participant identity because participant identity is not an argument. Gate-mask changes change the applicable chart fingerprint and pair key. Config/release incoherence refuses; a coherent different admitted config/release changes pair identity through its exact preimage.

## 6. Exact file and component plan

### 6.1 Authored implementation and focused tests

| Path | Planned change and ownership |
| --- | --- |
| `engine/magic10/composite.py` | New pure 36-Channel classifier, immutable state/owner record, mask-only presence logic and catalog exception assertions |
| `engine/magic10/signals.py` | New pure ordinary/equilibrium/counterweight integer operations and ordered 20-signal assembly |
| `engine/magic10/calculators.py` | Remove import-time JSON/Decimal/global registration path; implement injected integer category reduction and fixed band selection |
| `engine/core/core.py` | Replace legacy participant/CoreConfig coordinator with exact four-argument Gate core, immutable result records and intrinsic hashing |
| `engine/magic10/__init__.py` | Remove transitional calculator/threshold exports and import-time threshold side effect; export no alternate public calculator |
| `engine/core/__init__.py` | Remove `ParticipantState`, `CoreConfig`, `PerspectiveBreakdown`; export only `compute_core` and the minimum immutable result types |
| `tests/core/test_engine_core_purity.py` | Expand AST/import/monkeypatch guards across core, composite, signals and calculators; prove no I/O/env/time/random/process/cache/narrative/UUID/import side effects, no optional/default signature and no old symbols |
| `tests/core/test_engine_core_abba.py` | Complete AB↔BA result/canonical-byte equality, owner swap, reversed one-sided mass, equal-mask and identity-independence proofs |
| `tests/core/test_engine_core_determinism.py` | All 16 cases, explicit taxonomy exceptions, signal operations, reducer/bands, fixed G001–G006, exact order/schema, two-run and adverse matrix |

### 6.2 Necessary signature and fixture dependents

| Path | Why it is necessary and bounded change |
| --- | --- |
| `tests/m10/test_defs_order.py` | Remove tests of `calculator_ids`/`compute_category`; verify the injected reducer has no registry/file-loading surface and that bundle-driven category order closes exactly |
| `tests/m10/test_m10_symmetry_identity.py` | Replace arbitrary precomputed payload symmetry with actual four-argument kernel symmetry and two-run behavior using normalized Gates and the admitted synthetic bundle |
| `tests/m10/test_thresholds_rounding.py` | Test integer reducer/cap/band boundaries directly with exact q/weight/bounds inputs; reject coercions and zero/negative weights |
| `tests/evidence/test_canonical_json_gate_check_outputs.py` | Remove the `CATEGORY_INPUTS` runtime-sentry import/assertion; bind caps order to the admitted bundle/current canonical-gate owner without a duplicate runtime map |
| `tests/config/helpers.py` | Remove `engine/magic10/composite.py` and `engine/magic10/signals.py` from `_SYNTHETIC_PLACEHOLDERS` so the labeled 44-member fixture copies the real PR03 bytes; do not alter the actual manifest or PR02 admission rules |

There is no application-source change. `engine/compat/compute.py`, `engine/runtime/public.py`, CLI, HTTP, Reader, narrative and cache paths remain PR04-owned and untouched.

### 6.3 Existing core evidence family

| Path | Planned change |
| --- | --- |
| `tools/evidence/generate_engine_core_evidence.py` | Replace legacy participant/config fixtures with normalized Gates and one immutable synthetic admitted bundle; project the exact six-field result; generate current purity, two-run, AB↔BA and canonical-JSON comparison evidence; retain the same four artifact keys/paths and call the canonical updater for publication |
| `tests/evidence/test_engine_core_evidence.py` | Validate exact new evidence shapes, unchanged artifact-key/path registration, schema conformance, hashes/sizes and proof anchors; assert every reported behavioral predicate is true |
| `docs/schemas/core/engine_core_purity_report.schema.json` | Close purity rows to the four-module pure surface and exact check/result fields |
| `docs/schemas/core/engine_core_two_run_logs.schema.json` | Replace legacy participant/config/result definitions with normalized Gate input identity, config/release identity and exact pure result definitions |
| `docs/schemas/core/engine_core_abba_logs.schema.json` | Replace viewer/perspective predicates with complete result equality, canonical-byte equality, classification owner reversal and equal-mask fields |
| `docs/schemas/core/engine_core_json_compare_logs.schema.json` | Describe exact projected `magic10_result.v1`, canonical digest/byte equality and owning schema-validation outcome |
| `artifacts/core/purity/purity_report.json` | Regenerate through the existing core writer |
| `artifacts/core/two_run/identity.json` | Regenerate through the existing core writer |
| `artifacts/core/abba/ab_ba_parity.json` | Regenerate through the existing core writer |
| `artifacts/core/json_compare/core_result_json_compare.json` | Regenerate through the existing core writer |

The schema identities and four primary paths stay unchanged. PR03 does not create a new evidence family or claim HDE-DIST008.1.

### 6.4 Canonical updater-owned companions

After all eight primary/schema bytes are final, run `tools/evidence/update_evidence_index.py` once in write mode. Inspect the actual staged/working-tree delta and retain only owner-produced changes required by that writer, including:

- the eight sibling `*.path_proof.txt` files for the four core primaries and four core schemas;
- `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256` and their path proofs;
- `artifacts/evidence_index.jsonl`, `artifacts/evidence_index.jsonl.sha256` and their path proofs;
- `audit/gates/topology/orientation_demo.txt` and its path proof only if the canonical updater rewrites them as part of its convergent transaction.

Do not hand-edit any item in this subsection. If the updater produces another companion, classify it against its actual source dependency and retain it only when the canonical writer requires it. A broad unrelated churn is a writer/integrity defect to diagnose, not a plan license.

### 6.5 CI ownership seam

| Path | Planned change |
| --- | --- |
| `ci/checks/classify_ci_changes.py` | Register exact behavioral owners for `engine/core/core.py`, both new magic10 modules, `calculators.py`, and the two package export files; register `tools/evidence/generate_engine_core_evidence.py` to `tests/evidence/test_engine_core_evidence.py`. Do not broaden a directory to unrelated legacy sources. |
| `tests/evidence/test_rails_ci_workflow_integration.py` | Prove each PR03 source resolves to the intended focused tests, the core evidence generator no longer fails ownership classification, removed/invalid owners still fail closed, and the complete proposed changed-path set is truthfully classified. |

Because `ci/checks/classify_ci_changes.py` is itself a full-validation input, the final PR03 candidate selects all seven hosted lanes: `product`, `compat`, `db`, `rails`, `evidence`, `qa`, and `release`, plus changed behavioral tests. No lane is skipped or waived in this plan.

### 6.6 Explicitly unchanged paths

- `catalog/manifest.json` and its 15 rows;
- `schemas/magic10_result_v1.schema.json` and all accepted PR01 contract bytes;
- `engine/bodygraph/gates.py`, `engine/config/registry_loader.py`, `engine/serializer/canon.py`, `engine/stable/sercanon.py`, and accepted PR02 behavior;
- `engine/magic10/thresholds.py` as an unimported legacy module outside the new pure path;
- all PR04 through PR07, OPS, public, persistence, Canon and deployment paths.

A need to change an unchanged accepted contract beyond a direct import/signature repair is a material boundary.

## 7. Requirement-to-change-and-test mapping

| Requirement / criterion | Implementation locus | Decisive proof |
| --- | --- | --- |
| K040-REQ-001 / AC040-01 | All §6 PR03 files only | Changed-path inventory contains no PR04–PR07/OPS/PF10/release materialization; final result states bounded nonclaims |
| K040-REQ-002 / AC040-09 | core/composite/signals/calculators; unchanged shared serializer/schema | Purity/import tests, absence of duplicate loader/serializer/map, C040-05/C040-06 conformance tests |
| K040-REQ-005 / AC040-03 | composite, signals, calculators, core | 16 cases; all 20 exact signal rows; both Balance operations; 10 reductions; band boundaries; G001–G006 |
| K040-REQ-007 / AC040-04 | core input guard; PR02 types consumed unchanged | exact `NormalizedGates` and `AdmittedMechanicsBundle`; forged/mutable/incoherent inputs refused; schema-valid result only |
| K040-REQ-008 / AC040-04 | all pure modules | missing/extra/duplicate/unknown Channel/signal/category/profile/operation/owner fields; strict numeric types; wrong release; no partial result or old fallback |
| K040-REQ-009 / AC040-05 | core intrinsic hash construction | fixed chart-preimage digest tests; numeric mask ordering; equal masks retained twice; config/release/pair/repository identities remain distinct |
| K040-REQ-010 / AC040-06 | core plus ABBA/determinism tests | G001–G006 fixed independent oracles, AB↔BA complete values/canonical bytes, two-run identity; PR05 G007/G008/comparator excluded |
| K040-REQ-011 / AC040-07/08 | all focused and adverse tests | taxonomy exceptions, owner mass, rounding edges, result order/closure, immutability and pure side-effect guards; readiness excluded |
| K040-REQ-012 / AC040-08 | existing core writer, four schemas, updater and companions | writer output validates; INDEX/Mirror/proofs/hashes converge; check mode clean; no new evidence key |
| K040-REQ-013 | plan, commits, PR, review and CI result | exact source/head/test/run/attempt/job identities recorded only after they exist; counts not summed |

K040-REQ-003, K040-REQ-004 and K040-REQ-006 remain accepted predecessor/interface obligations. PR03 preserves them without claiming redelivery or acceptance.

## 8. Detailed test design

### 8.1 Classifier and taxonomy

- Table-drive all 16 lower/higher endpoint presence combinations from PF10 §2.5, asserting state, pre-normalization A/B owner and post-mask-order `member_lo`/`member_hi` owner.
- Assert aggregate counts: seven none, four compromise, two dominance, two electromagnetic and one companionship.
- Assert priority with both-full, full-plus-hanging, full-plus-none and opposite single halves; same-end hanging Gates remain none; no hanging Gate creates an independent contribution.
- Assert reversal preserves state and swaps owner when an owner exists.
- Assert the exact four Integration Channel IDs and the `10-34`/`20-57` exceptions from the accepted bundle.

### 8.2 Signals and category math

- Ordinary signals: all-none gives q=0; companionship, dominance, compromise and electromagnetic use the exact selected profile response; maximum responses give q=200; mixed weighted inputs prove one final half-up operation.
- Equilibrium: all none/companionship/EM gives zero owner mass; all mass on one owner gives q=0; equal owner mass at 3/3 of six unit weights gives q=200; unequal and reversed owner masses prove min and symmetry.
- Counterweight: zero qualifying mass gives q=0; all selected mass companionship/EM gives q=200; mixed masses prove the exact half-up result.
- Category reducer: lower/upper caps applied in doubled-q units; exact integer weights only; scores and bands at 0, 24, 25, 49, 50, 74, 75 and 100; outlying q values cap before reduction; final clamp occurs once.
- Reject bools, floats, strings, zero or negative weights, invalid bounds, wrong arity, extra members, unknown operation/profile/state and q outside `0..200`.

### 8.3 Fixed source oracles

- G001: all Channels none; all 20 q values zero; all 10 categories score 0/Cool.
- G002: all Channels companionship; categories exactly harmony 100/Glow, heat 50/Warm, communication 75/Glow, alignment 100/Glow, comfort 100/Glow, consistency 100/Glow, expansion 50/Warm, creativity 63/Warm, drive 50/Warm, balance 50/Warm.
- G003: equilibrium selected mass split 3/3 gives q=200; all one side gives q=0.
- G004: independently encode A Gates `{5,19,20,34,43,49}` and B Gates `{9,12,15,22,23,52}`. Assert states `05-15 electromagnetic`, `09-52 dominance/member B`, `12-22 dominance/member B`, `19-49 dominance/member A`, `20-34 dominance/member A`, `23-43 electromagnetic`, rest none. Assert q vector `[25,63,0,38,40,20,0,25,50,38,50,0,0,0,50,20,0,60,0,33]`; category scores `[22,10,15,6,22,13,0,18,15,8]`; all Cool.
- G005: intrinsic identity independence; no person/request identity exists in arguments or output.
- G006: reducer boundary bands at 24, 25, 49, 50, 74, 75 and 100.

Expected values are literal source oracles. No fixture helper may call `compute_core`, a reducer under test, or generated output to derive them.

### 8.4 Result, identity and immutability

- Assert the result record has exactly six declared fields; projected payload keys are exactly schema/config/release/pair/signals/categories; signal/category rows have exact keys and order.
- Validate the projected payload against unchanged `schemas/magic10_result_v1.schema.json`, then independently validate relational order against admitted caps/category order.
- Compute chart fingerprint and pair-key digests independently in tests from literal preimage objects and the shared serializer; also compare fixed known digest literals after first independent derivation/review.
- Assert AB and BA complete projected canonical bytes equal.
- Assert two equal normalized masks yield two equal fingerprint members without a UUID tie and a complete result.
- Assert mutation attempts against result records, tuples, admitted maps and normalized members fail or leave source unchanged.
- Assert direct forged `NormalizedGates` mask/hex mismatch, mutable/forged bundle members, wrong release and structural closure defects refuse without any returned partial record.

### 8.5 Purity and retired-path proof

- AST-scan all four pure modules for forbidden roots and calls: filesystem/path/json loading, `os`, environment, locale, time/datetime, random, socket/network, subprocess/process, database/vendor, cache, narrative and UUID/request identity.
- Monkeypatch representative I/O/clock/random/environment entrypoints and import/reload the pure surface; any call fails the test.
- Inspect the exact `compute_core` signature: four required positional arguments; no default, variadic option or `CoreConfig`.
- Assert old names are neither defined nor exported and old three-argument/`compat_score` calls fail.
- Search the candidate for active imports/calls of removed calculator exports; only historical docs/audit text may remain.

## 9. Ordered implementation procedure

1. **Recover exact state.** Verify repository identity, current `main`, clean status, existing PR03 worktrees/branches/PRs/artifacts and user changes. Reuse a genuine matching PR03 state; otherwise create a dedicated worktree/branch from verified current main. Never reuse the PR02 worktree/branch as PR03.
2. **Reconfirm source and drift boundary.** Read this exact plan/instruction and current PF10 controlled Markdown. Diff the current target against §3/§6. If affected accepted contracts have materially changed, preserve evidence and use §14; otherwise record the compatible base and proceed.
3. **Create the focused failure harness.** Migrate `tests/config/helpers.py` for real composite/signals fixture bytes; rewrite core/m10 tests to the four-argument injected contract and fixed oracles. Confirm failures are attributable to missing/new behavior, not fixture admission drift.
4. **Implement classification.** Add immutable types and exhaustive classifier in `composite.py`; run classifier/taxonomy tests.
5. **Implement signal math.** Add strict integer operations in `signals.py`; run ordinary/Balance/adverse tests.
6. **Implement category reduction.** Replace `calculators.py`; remove import-time reads/Decimal/global registry/old exports; run reducer/boundary and purity tests.
7. **Replace the core.** Implement four-argument validation, single classification, signal/category assembly, fingerprint/pair identity and immutable result in `core.py`; migrate package exports; run all core and m10 tests.
8. **Migrate exact dependent tests.** Update the canonical-gate binding test and confirm no remaining active caller/import of old surfaces. Do not edit PR04 sources.
9. **Bind CI owners.** Add narrow classifier mappings and integration assertions; verify the core generator maps to its exact evidence test and the complete candidate selects all seven lanes.
10. **Migrate evidence contracts.** Update the existing writer, four evidence schemas and focused evidence test. Run the writer through its synthetic bundle and validate the four primaries before index publication.
11. **Publish governed companions.** Invoke the canonical updater once after primaries/schemas are final. Inspect exact changes, then run every read-only evidence/hash/path/LF check. Never hand-edit generated companions.
12. **Local candidate validation.** Run §10 in closed rails. Correct defects locally and repeat affected tests. Before every meaningful commit/push, run the focused suite and applicable checks for that checkpoint.
13. **Coherent checkpoints.** Commit a locally tested pure-kernel/test/CI-owner checkpoint, then a locally tested evidence/convergence checkpoint if separation improves review. Each commit remains buildable; do not push a known-broken intermediate. Record actual SHAs only after creation.
14. **Publish one PR03 proposal.** Push deliberately and open/update one PR against `main` with exact scope/nonclaims and validation evidence. No auto-merge.
15. **Review before paid CI.** Obtain substantive code review and security review on the actual candidate. Resolve every finding locally, rerun affected/full validation, push one coherent correction, and obtain corrected-head review where required. Do not spend a final CI attempt on code already known to require another push.
16. **Final exact-head CI.** After local success and substantive reviews, verify remote PR head equals the reviewed local head and run/observe `.github/workflows/ci.yml`. Require all seven selected lanes, changed tests and terminal `CI_APPLICABILITY_AND_EXACT_HEAD_OK` on that exact head. Record run, attempt, job, base, head and tree identities.
17. **Engineering result.** Save/read back one PR implementation result. Return `MERGE_PENDING`, `Ready to merge`, the actual PR/head/review/CI/evidence record and the conditional selected PR-40 handoff for use only after Nathan's manual merge evidence exists. Do not merge or poll indefinitely.

## 10. Local validation and evidence commands

Run from the dedicated PR03 worktree. Install test dependencies before pytest and keep closed rails for every applicable command:

```bash
python -m pip install -r requirements-dev.txt
python -m pip install -r requirements.txt -e .
python -m pytest --version
export LC_ALL=C LANG=C TZ=UTC SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev PYTHONDONTWRITEBYTECODE=1
ci/checks/check_env_pins.sh
```

### 10.1 Focused behavioral and ownership suite

```bash
python -m pytest -q \
  tests/core/test_engine_core_purity.py \
  tests/core/test_engine_core_abba.py \
  tests/core/test_engine_core_determinism.py \
  tests/m10/test_defs_order.py \
  tests/m10/test_m10_symmetry_identity.py \
  tests/m10/test_thresholds_rounding.py \
  tests/config/test_magic10_contracts.py \
  tests/config/test_production_admission.py \
  tests/config/test_typed_bundles.py \
  tests/evidence/test_canonical_json_gate_check_outputs.py \
  tests/evidence/test_engine_core_evidence.py \
  tests/evidence/test_evidence_tool_ownership.py \
  tests/evidence/test_rails_ci_workflow_integration.py
```

Run the complete configured default suite separately because `pytest.ini` does not include `tests/core` or the focused core-evidence test:

```bash
python -m pytest -q
```

Counts overlap and must be reported separately.

### 10.2 Existing evidence writer and companions

```bash
python tools/evidence/generate_engine_core_evidence.py --skip-index
python -m pytest -q tests/evidence/test_engine_core_evidence.py
python tools/evidence/update_evidence_index.py
python tools/evidence/update_evidence_index.py --check
python tools/evidence/orientation_demo.py --check
python tools/evidence/refresh_step_logs_manifest.py --check
ci/checks/check_evidence_index_hash.sh
python tools/evidence/validate_evidence_paths.py
ci/checks/check_mirror_schema.sh
ci/checks/check_final_lf.sh
python tools/evidence/run_canonical_json_gate.py --check-only
```

After write mode, run `git diff --check`, inspect every changed governed path and rerun the focused evidence test. A failed publication preserves the valid primary evidence but does not claim companions complete; diagnose and rerun only through the owning writer.

### 10.3 Candidate-wide CI-equivalent validation

Since the classifier itself changes, locally execute the current commands for all seven lanes from `.github/workflows/ci.yml`, including:

```bash
python tools/order/generate_ordering_artifacts.py --check
ci/checks/check_cli_help.sh
python tools/cli/serializer_grep_guard.py --output /tmp/hde-pr03-serializer-grep.log
python tools/cli/emitter_symbol_proof.py --output /tmp/hde-pr03-emitter-symbol.txt
python ci/checks/check_direct_db_contract.py
python ci/checks/run_rails_job_definitions.py \
  ci/jobs/rails_closed_refusal.yml \
  ci/jobs/rails_open_conformance.yml \
  ci/jobs/logs_keys_only_redaction.yml
python scripts/release_id_recompute.py --check-manifest-only
```

Run the exact fixed pytest rosters and isolated-worktree cleanliness checks shown by the candidate's current `.github/workflows/ci.yml` for product, compat, db, rails, evidence, qa and release. For the release lane, create and validate one external temporary directory, then run:

```bash
pr03_attestation_dir="$(mktemp -d)"
python tools/evidence/build_release_attestation.py \
  --output "$pr03_attestation_dir/release-attestation.json" \
  --require-clean
python tools/evidence/build_release_attestation.py \
  --verify "$pr03_attestation_dir/release-attestation.json"
```

After results are recorded, remove only the exact directory named by `pr03_attestation_dir`. This validation does not activate or promote a release.

Finally:

```bash
git diff --check
git status --short --untracked-files=all
```

The final candidate must be clean after committed generated evidence. Hosted CI, not the local emulation, supplies the final exact-head CI outcome.

## 11. Code review and security review checklist

### 11.1 Code review

- Verify single classification and single calculator ownership; no precomputed-score fallback, overload, duplicate map or expected-output self-generation.
- Trace every signal row from admitted caps/mechanics order to the exact state response and final q; trace both Balance masses separately.
- Trace every category from two ordered q values through doubled caps, weighted half-up reducer, one clamp and exact band.
- Recompute representative G002/G004 outputs and fingerprint/pair digests independently.
- Confirm complete result field/order/schema closure and immutable in-process representation.
- Confirm actual unchanged `schemas/magic10_result_v1.schema.json` validates output and no accepted PR01/PR02 behavior was silently edited.
- Confirm direct callers and exports are coherent; application surfaces remain untouched.
- Confirm classifier ownership routes every changed source to meaningful tests and generator ownership no longer fails closed.
- Confirm governed changes were produced by their owners and the index/mirror/path-proof graph agrees.

### 11.2 Security review

- No filesystem, environment, locale, process, network, database, vendor, clock/time, random, cache, narrative, UUID or request identity dependency in the pure path.
- No path or remote-schema input accepted by core; no dynamic import/eval/exec; no caller configuration or hidden bypass.
- No secrets, names, birth values, UUIDs, Gate payload dumps, full user records or environment values in output/evidence/errors.
- Strict built-in integer checks reject bools and coercions; exact release identity and immutable bundle relationships prevent confused-deputy use of a forged/stale configuration.
- Arithmetic denominators are validated positive; q/score bounds and list cardinalities prevent overflow-like or partial-shape behavior in the approved domain.
- Failure is complete and value-free; no partial matrix/result is returned or logged.
- Shared serializer remains the sole canonical-byte owner; no second serializer is introduced.

## 12. Risk register and recovery

| Risk | Prevention / detection | Recovery |
| --- | --- | --- |
| Bundle is frozen but directly forgeable | Pure consumer invariant checks; forged-object adverse tests | Refuse before computation; repair guard/tests without changing PR02 loader contract |
| Owner normalized before mask order | Classifier keeps input owner and post-order owner distinct in 16-case/reversal tests | Fix classifier only; rerun all signal/ABBA/G004 evidence |
| Early or float rounding | Integer formulas centralized once; exact mixed and boundary oracles | Revert reducer/signal checkpoint; never retune expected values |
| Equal masks accidentally use identity | Core has no identity argument; equal-member preimage test | Remove identity dependency; regenerate only affected core evidence through owner |
| Duplicate mechanics authority | No static 20-signal map in runtime code; iterate admitted config/caps | Delete duplicate; retain only test literals as independent expected oracles |
| Legacy import-time read survives package import | package export cleanup plus AST/monkeypatch purity tests | Remove import from new surface; do not expand scope into unrelated threshold rewrite |
| Synthetic 44-member fixture mistaken for actual release | Explicit fixture label; actual manifest remains 15; nonclaims in PR/result | Stop any promotion claim; restore manifest unchanged; PR06 retains ownership |
| Evidence graph churn or partial publication | Primary-first, updater-owned convergent transaction, check mode and clean diff | Preserve valid primaries; rerun owner after diagnosis; never hand-edit companions |
| CI owner map too broad/narrow | Exact-path mappings and integration tests | Correct mapping and rerun all lanes because classifier changed |
| Main advances during work | compare current base/affected paths; ordinary compatible changes handled in PR session | Rebase/merge only under existing PR workflow; material contract conflict routes to §14 |
| Review finding arrives after CI | review-before-final-CI ordering | fix locally, test, push once, re-review, then run a new exact-head CI attempt |

Interrupted implementation retains the same dedicated PR03 session, worktree, branch, open PR, coherent commits, tests, review state and uncommitted delta. Record the exact resume point. Never reset away user work. Rollback treats core, pure mechanics modules, exports, migrated tests, CI ownership and affected evidence as one compatible set; never restore only the old core or rewrite configuration/oracles to hide mismatch.

## 13. Carried Canon-conflict register

| ID | Classification and status | PR03 treatment | Remaining owner/risk |
| --- | --- | --- | --- |
| C040-01 | `CANON_RECONCILIATION`; Thoth-17 `APPROVED` | Carry history; no PR03 action | PF09 source correction resolved; no reopening |
| C040-02 | `CANON_RECONCILIATION`; Thoth-17 `APPROVED` | Use current verified PF12 v2.9.6; no metadata inference | Governed PF12 maintainer only if future actual maintenance remains |
| C040-03 | `CANON_RECONCILIATION`; Thoth-17 `APPROVED` | Use current verified PF14 v3.5.7 | Governed PF14 maintainer; no PR03 metadata edit |
| C040-04 | `CANON_RECONCILIATION`; Thoth-17 `APPROVED` | Carry history; no QA-owner change | Governed PF19 maintainer if needed; not a PR03 gate |
| C040-05 | `CANON_RECONCILIATION`; Isis-49 `APPROVED`, alternative A | Remove the legacy precomputed-score/CoreConfig/three-argument success path and migrate tests; preserve separate HDE-DIST008.1 scope | Permanent PF14 §6.7 drainage remains with governed PF14 maintainer; non-gating |
| C040-06 | `NEW_CANON`; Isis-50 `APPROVED`, alternative A | Use accepted 36-row taxonomy, exact Integration exceptions and 16-case conformance; no weight/formula change | Permanent PF12 §2.1 and PF01 §§6.1–6.2 drainage remains with governed maintainers; non-gating |

No entry is reopened, relabeled, silently resolved or newly approved by this plan. PF10 v13.2.4 is current; its §2.11 PR02 acceptance changes no PR03 scope. C040-05/C040-06 permanent drainage and repository prompt-use persistence remain non-gating external ownership.

## 14. Material boundary and rescope route

Ordinary defects within the exact files/behavior above are repaired by the PR03 engineer under the original Proceed. Stop only the affected work and preserve valid state if implementation requires any of the following:

- change to accepted PR01 config/result schema/data or PR02 admission/normalizer/manifest/execution-coherence behavior beyond a direct import adaptation;
- new or changed mathematics, signal/category roster/order, profiles, weights, caps, thresholds, state taxonomy, pair preimage or result fields;
- PR04 application/identity/cache/narrative/public behavior;
- actual manifest roster change/release promotion, new evidence family, public/API/CLI/schema surface, persistent storage or new serializer/loader authority;
- a newly evidenced Canon contradiction or architecture requirement not resolved by the carried register.

For a material planning boundary discovered before Proceed, return the completed bounded planning draft and exact evidence to selected `RS-10 — Create Bounded Work-Unit Rescope Proposal`; do not rewrite the approved bases or ask for a replacement Proceed. During PR-30 implementation, preserve the same worktree/branch/open PR, create the formal `RESCOPE_REQUEST`, and hand directly to the same whole-change IA through selected RS-20 as PR-30 requires. An approved/drained RS-40 continuation preserves the original Proceed.

No material boundary is presently identified. This plan is therefore `AWAITING_PO_PROCEED`.

## 15. Manual merge and post-implementation boundary

PR-30 engineering ends at `MERGE_PENDING` and the phrase `Ready to merge` with the actual PR reference. Nathan / Product Owner alone performs any manual merge unless a later direct, specific instruction expressly authorizes the identified action. Do not enable auto-merge, schedule a merge, ask the PR engineer to merge, or treat successful tests/review/CI as merge evidence.

After actual manual merge evidence exists, Nathan may invoke the selected read-only PR-40 against the exact landed lineage. PR-40 independently decides work-unit acceptance. PR03 implementation, merge, or PR-40 acceptance does not perform QA/Ops, promote the 44-member release, edit PF10, or close the Epic.

## 16. Prompt-use provenance

`GCFPE_PROMPT_USE`:

- usage_id: `GCFPE-USE-HDE-EPIC040-PR-20-20260914-PR03-01`
- change/work unit: `HDE-EPIC040` / `HDE-EPIC040-PR03`
- Specification: `HDE-EPIC040-SPECIFICATION v1.1`, Thoth-17 `APPROVE`
- prompt: `PR-20 — Create Detailed PR Implementation Plan — 091326.2`
- prompt page: `https://app.notion.com/p/3da4590a05eb8147b34ccfabf608c2e3?pvs=204`
- ecosystem release: `GCFPE-20260913.1`
- retrieved revision: `2026-09-13T11:35:45.616Z`
- role/stage: dedicated PR03 engineering session / PR-20 initial detailed planning
- execution posture: `MANUAL_PROMPT_EXECUTION`
- capture time: `2026-09-14T07:23:20Z`
- result: `HDE-EPIC040-PR03-PR-IMPLEMENTATION-PLAN v1.0`, `AWAITING_PO_PROCEED`
- repository provenance: `docs/changes/GCFPE_PROMPT_PROVENANCE.md` was not found in the inspected exact tree; authorized repository persistence remains pending and non-gating. PR-30 carries this exact use entry alongside later observed PR/commit lineage only within the proceeded scope.

## 17. PR-30 continuation package

The PR-20 user-facing return supplies one complete paste-ready `NEXT_PROMPT_HANDOFF` with this saved file's exact direct Drive URL. The handoff binds:

- selected PR-30 v091326.2 and its exact Notion URL;
- the same dedicated PR03 engineering session with `RETAIN_EXISTING`;
- this exact plan v1.0 and PR instruction v1.0 by direct Drive links;
- all approved lineage and current PF10 v13.2.4;
- the exact main head/tree baseline and accepted PR01/PR02 dependencies;
- the complete scope, exclusions, Canon-conflict register, validation/review/CI order, recovery and manual merge boundary in this plan;
- the Product Owner's manual invocation as the sole Proceed for this plan;
- expected result `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED` under PR-30's exact result contract.

No implementation begins until Nathan / Product Owner invokes that handoff against this exact persisted plan.
