# HDE-EPIC040-PR03 — PR Work-Unit Instruction v1.0

## 1. Identity and state

| Field | Value |
| --- | --- |
| Artifact type | `PR_INSTRUCTION` |
| Logical ID | `HDE-EPIC040-PR03-PR-INSTRUCTION` |
| Version | `1.0` |
| State | `INSTRUCTION_READY` |
| Change class | `EPIC` |
| Change ID | `HDE-EPIC040` |
| Change name | Separation Pass 3 |
| Work-unit ID | `HDE-EPIC040-PR03` |
| Work-unit name | Pure Gate mechanics and intrinsic identity |
| Author / role | Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Architect |
| Author-session disposition | `RETAIN_EXISTING` |
| Execution posture | `MANUAL_PROMPT_EXECUTION` |
| Invocation binding | `HDE-EPIC040 / HDE-EPIC040-PR03 / PR-10` |
| Context conflict | `NONE` |
| Capture time | `2026-09-14T06:50:55Z` |
| Output class / destination | `EPHEMERAL_DRIVE` / `Glow / Ephemeral Planning Files` |

This instruction defines exactly one approved work unit. It is not a detailed per-file implementation plan, Product Owner Proceed, implementation authorization, merge instruction, QA or Ops execution, PF10 edit, release activation, or Epic closure.

## 2. Exact approved lineage

| Role | Exact authoritative artifact or decision |
| --- | --- |
| `SPECIFICATION_REF` | [HDE-EPIC040 Specification v1.1](https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk), logical ID `HDE-EPIC040-SPECIFICATION`, `SPECIFICATION_APPROVED`; Thoth-17 `APPROVE` at `2026-09-08T13:23:24Z` |
| `IMPLEMENTATION_AUDIT_REF` | [HDE-EPIC040 Implementation Audit v2.0](https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk), logical ID `HDE-EPIC040-IMPLEMENTATION-AUDIT`, `AUDIT_COMPLETE` |
| `IMPLEMENTATION_PLAN_REF` | [HDE-EPIC040 whole-change Implementation Plan v2.1](https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk), logical ID `HDE-EPIC040-IMPLEMENTATION-PLAN`, immutable approved base; SHA-256 `10732f9338b209e3ce19e81936119e47c9551ea912298a27c731c9e60e2a61be` |
| `PLAN_REVIEW_REF` | [HDE-EPIC040 Implementation Plan Review v2.1](https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk), logical ID `HDE-EPIC040-IMPLEMENTATION-PLAN-REVIEW`; Isis-50 `APPROVE` at `2026-09-09T13:36:43Z`; SHA-256 `47f73e627fe86bab310327668c89f8818c6603df45bb94c8de807da70057b0d3` |
| Accepted dependency 1 | [HDE-EPIC040-PR01 PR Work-Unit Lineage Review v1.1](https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk), `ACCEPT`; SHA-256 `f103798f7c8344e8cec763f0496d82a9ca81f82ea9cb8e6ac4cf0cd4c59e3273`; PR #403 accepted and final |
| Accepted dependency 2 | [HDE-EPIC040-PR02 PR Work-Unit Lineage Review v1.0](https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk), logical ID `HDE-EPIC040-PR02-PR-WORK-UNIT-LINEAGE-REVIEW`, `ACCEPT`; PR #404 accepted and final |
| Current PF10 | [PF10-HDE-Build-Notes v13.2.4](https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk), unique current controlled Markdown direct child of `Glow / Core Docs / PFCanon` at instruction time |
| Governing PR-10 prompt | [PR-10 — Create PR Work-Unit Instructions — 091326.2](https://app.notion.com/p/3da4590a05eb81c594a0f9bf5cb151a7?pvs=204), selected release `GCFPE-20260913.1`, exactly 54 members |

The handoff named PF10 v13.2.3. Current-source resolution found the non-conflicting complete successor v13.2.4. Its §2.11 canonically records the already supplied PR02 acceptance and return to this IA. PF10 §§2.7, 2.9, and 2.10 remain the approved F01/F02/F03 overlays for PR02 only; they do not amend PR03 mathematics, expand this work unit, or reopen PR02.

The approved Specification, Audit, Plan, and Plan Review are immutable bases. No accepted PR, approved Plan, or original Proceed is reauthored or rerun.

## 3. Current repository and source baseline

### 3.1 Repository baseline

- Repository: [amthorn78/glow-hdengine-v2](https://github.com/amthorn78/glow-hdengine-v2).
- Target branch: `main`.
- Current verified `main` head: [`5b2fb8d70924a6710b6261fc0c93d3869fed6380`](https://github.com/amthorn78/glow-hdengine-v2/commit/5b2fb8d70924a6710b6261fc0c93d3869fed6380).
- Current verified tree: `e43c2063599e7bc449f20d4ab045d32d95581bf4`.
- That commit is the accepted PR02 / PR #404 squash merge. Its parent is accepted PR01 head `3828d4b3454259841a3e48d13039dd1475754f2f`.
- No PR03 branch, commit, pull request, detailed PR Plan, Product Owner Proceed, implementation result, review, CI result, or merge exists at instruction time.

The current repository still contains the superseded `compat_score` / optional `CoreConfig` three-argument scaffold in `engine/core/core.py`, legacy Decimal/file-loading calculator behavior in `engine/magic10/calculators.py`, and legacy tests in the three `tests/core/test_engine_core_*` files. `engine/magic10/composite.py` and `engine/magic10/signals.py` are not present. These are verified implementation gaps, not permission to preserve two successful mechanics paths.

PR02 supplies the accepted strict Gate normalizer and immutable admission types, including `NormalizedGates` and `AdmittedMechanicsBundle`. The actual repository manifest remains an intentionally incomplete 15-member release and correctly refuses full production admission. PR03 must not promote or expand that actual manifest. Bounded tests may use validated synthetic complete-release fixtures through existing safe fixture seams; fixture success is not release promotion.

### 3.2 Current controlled subject-matter sources

Use the unique current controlled Markdown files in `Glow / Core Docs / PFCanon`. The resolved PR03 sources are:

- [PF01-Canon-HDE-Math-Spec v1.3.7](https://drive.google.com/file/d/1ILESkXCDr11Me6WvCBPpebfmQFwEz63p/view?usp=drivesdk): §§5.2, 6.1–6.2 and applicable deterministic fixtures; owns the five-state classifier, integer kernel, signal/category formulas, intrinsic fingerprints and pair identity.
- [PF02-Canon-HDE-Architecture v2.4.5](https://drive.google.com/file/d/1y4JvZKVZR_5J_wynT4p3HtYgX4cRSIB6/view?usp=drivesdk): owns pure-core boundaries, injected configuration, component ownership, dependency direction, and application separation.
- [PF03-Reference-Technical-Writing-Best-Practices v1.8.7](https://drive.google.com/file/d/1M_PTWi-ySFs1NWIjFpd9p2IL-vsKbJEA/view?usp=drivesdk): source fidelity and precise technical change descriptions only.
- [PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.2](https://drive.google.com/file/d/1P78CNLZhAIYYTHXOAi2aX1HoImo9TuXo/view?usp=drivesdk): existing error and transport ownership; PR03 creates no new public surface.
- [PF09.3-Canon-HDE-Build-Checklist-Separation v1.1.5](https://drive.google.com/file/d/1JLCCfPPryE_EG_62B1PHSZ2QGKvGsolp/view?usp=drivesdk): phase/task context subject to the approved Plan decomposition.
- [PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6](https://drive.google.com/file/d/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ/view?usp=drivesdk): §2.9 result/configuration schemas, canonical JSON, validation, evidence owners, companions, and manifest/release distinctions.
- [PF14-Canon-HDE-Mechanics-Guide v3.5.7](https://drive.google.com/file/d/13kNlj4Y_F1fIqE3_L4eyjeJUkdO3LkX1/view?usp=drivesdk): §6.7 exact four-argument core contract and migrated core test surface, with C040-05 governing its contradictory legacy paragraphs.
- [PF10-HDE-Build-Notes v13.2.4](https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk): applicable scoped overlays and PR02 acceptance status.

Do not use Google Docs/DOC/DOCX twins, repository PF copies, historical filenames, generated artifacts, model memory, or this instruction as an independent mechanics authority where the sources above own the fact.

## 4. Work-unit objective and completion boundary

Implement one deterministic, immutable, integer-only pure kernel from two eligible normalized Gate members and the injected admitted mechanics bundle to a complete `magic10_result.v1`.

PR03 completes all of the following as one coherent unit:

1. Classify each of the 36 canonical Channels exactly once into the closed five-state model, with normalized owner only for `dominance` and `compromise`.
2. Produce all 20 ordered signal values from the admitted configuration using the exact ordinary and Balance operations.
3. Cap and reduce the 20 signals into exactly 10 ordered category scores and bands.
4. Compute intrinsic chart fingerprints and the intrinsic pair identity from Gate masks, configuration identity, release identity, and result schema only.
5. Return and validate the complete pure result schema with exact ordering and domains.
6. Replace the old successful precomputed-score/CoreConfig path and migrate its core tests and signature-dependent bounded callers/evidence writer.
7. Prove purity, complete AB↔BA identity, equal-mask behavior, two-run determinism, exact rounding/bands, fixed oracles, and decisive fail-closed cases through local tests, substantive code/security review, and final exact-head CI.

Completion is bounded to the pure kernel and its own evidence. It does not establish application eligibility, canonical-person identity, directional narrative orientation, cache persistence, Reader/CLI/HTTP behavior, golden-readiness tooling, actual 44-member release materialization, deployment, QA, Ops, or Epic completion.

## 5. Required interfaces

### 5.1 Canonical entrypoint

The canonical entrypoint is exactly:

```python
compute_core(member_a, member_b, mechanics_bundle, release_id)
```

- `member_a` and `member_b` are eligible, already normalized, immutable member values carrying at least the ascending nonempty Gate tuple, unsigned 64-bit Gate mask, and exactly 16 lowercase hexadecimal `gate_mask_hex`. They contain no score seed, identity, narrative key, viewer preference, or mutable Gate collection.
- `mechanics_bundle` is the one immutable typed `AdmittedMechanicsBundle` produced outside Engine Core by the accepted PR02 boundary. Core consumes it; it does not load, select, freeze, mutate, repair, or replace it.
- `release_id` is a lowercase 64-hex active release identity injected explicitly and must agree with the admitted bundle. It is not a caller override or repository commit identity.
- The result is the closed pure `magic10_result.v1` object defined in §8.

Remove the successful optional `CoreConfig`, precomputed `compat_score`, three-argument overload, custom `band_priority`, UID ordering/seed, old directional `PerspectiveBreakdown`, and old result-shape path from canonical success behavior and migrated tests. Do not retain an overloaded alternate calculator to satisfy the contradictory legacy PF14 paragraphs resolved by C040-05.

### 5.2 Dependency direction

The pure dependency direction is:

`normalized members + injected admitted bundle + release_id → Channel states → signals → category results → intrinsic identities/result`

Core and its pure mechanics modules must not import application, CLI/HTTP, persistence, cache, narrative, acquisition, vendor, database, filesystem-loader, clock, randomness, process, or environment behavior. Canonical serialization may be used only through the existing owning serializer and only over already pure values.

## 6. Exact required behavior

### 6.1 Five-state Channel classification

For every validated Channel with endpoint Gates `x` and `y`, determine ownership booleans for each member. Apply the first matching rule:

| Priority | State | Exact predicate | Owner |
| --- | --- | --- | --- |
| 1 | `companionship` | both members own both endpoints | absent |
| 2 | `compromise` | exactly one member owns both endpoints and the other owns exactly one | normalized full-Channel owner |
| 3 | `dominance` | exactly one member owns both endpoints and the other owns neither | normalized full-Channel owner |
| 4 | `electromagnetic` | neither member is full and the two members exclusively own opposite endpoints | absent |
| 5 | `none` | every remaining pattern | absent |

Normalize the full-Channel owner as `member_lo` or `member_hi` using numeric Gate-mask order. For equal masks, intrinsic members remain equal and no person identity breaks the tie. Channel-state rows are duplicate-free and ASCII-sorted by canonical `channel_id`. Cover all 16 combinations of the four endpoint-ownership booleans, the four approved Integration Channels (`10-20`, `10-57`, `20-34`, `34-57`), and the `10-34` centering / `20-57` knowing exceptions. Hanging-Gate provenance may support this single classification but must not add a second contribution.

Missing, ambiguous, invalid, or non-closed topology yields no partial vector or result.

### 6.2 Signal production

Signal order is exactly the flattened ordered pair of inputs for each category in `catalog/magic10.json` order as joined through `catalog/magic10_caps.json`. All mappings, profiles, operations, weights, and scales come from the injected validated mechanics bundle; code must not duplicate the 90-member map as a second authority.

The exact category/signal roster is:

| Category | Signal 1 | Signal 2 |
| --- | --- | --- |
| `harmony` | `rapport_delta` | `resonance_strength` |
| `heat` | `spark_intensity` | `momentum_flux` |
| `communication` | `signal_clarity` | `exchange_density` |
| `alignment` | `vector_cohesion` | `axis_agreement` |
| `comfort` | `soothe_index` | `buffer_resilience` |
| `consistency` | `pattern_integrity` | `variance_stability` |
| `expansion` | `growth_tendency` | `horizon_reach` |
| `creativity` | `novelty_factor` | `expression_flow` |
| `drive` | `willpower_current` | `focus_pressure` |
| `balance` | `equilibrium_score` | `counterweight_ratio` |

For an ordinary signal with positive integer Channel weights `w`, profile responses `r` in basis points, total weight `W`, and weighted response sum `N`, compute exactly:

`q = floor((N + 25 * W) / (50 * W))`

This is one half-up rounding after the complete weighted sum. `q` is an exact integer in `0..200`. No float or Decimal path is permitted in the canonical kernel.

For Balance `equilibrium_score`, only `dominance` and `compromise` contribute their normalized owners. With mapped owner masses `m_lo`, `m_hi`, `m = min(m_lo, m_hi)`, and total mapped weight `W`, compute:

`q = floor((800 * m + W) / (2 * W))`

For Balance `counterweight_ratio`, with `M` equal to mapped weight in `companionship` or `electromagnetic` and total mapped weight `W`, compute:

`q = floor((400 * M + W) / (2 * W))`

Do not reinterpret these Glow-authored numerical responses as empirical relationship effects, clinical doctrine, fairness, reciprocity, destiny, safety, or outcome prediction.

### 6.3 Category reduction and bands

For category bounds `L` and `U`, cap each half-score input `q_i` before reduction:

`q'_i = min(2 * U, max(2 * L, q_i))`

With positive integer category-input weights `b_i`, `B = sum(b_i)`, and `Q = sum(b_i * q'_i)`, compute exactly:

`raw_score = floor((Q + B) / (2 * B))`

Then apply `score = min(100, max(0, raw_score))` once. Apply inclusive band maxima `[24,49,74,100]` after the clamp: `0..24 Cool`, `25..49 Open`, `50..74 Warm`, `75..100 Glow`.

Each Channel is classified once, each signal is evaluated once, and each category is reduced once. Do not add bonuses, dampeners, presets, early rounding, UID seeds, caller-selected knobs, alternate thresholds, or hidden multipliers.

### 6.4 Intrinsic fingerprints and pair identity

For each normalized member, canonicalize exactly:

```json
{"gate_mask_hex":"<16 lowercase hex>","schema":"magic10_chart_fingerprint.v1"}
```

The `chart_fingerprint` is the SHA-256 of those canonical bytes.

Order members by numeric Gate mask as `member_lo`, `member_hi`; equal masks remain two equal adjacent members. Canonicalize exactly the pair preimage fields:

- `schema = "magic10_pair_preimage.v1"`
- `members = [chart_fingerprint_lo, chart_fingerprint_hi]`
- `config_id = mechanics_bundle` configuration identity
- `release_id =` the validated injected release identity
- `result_schema = "magic10_result.v1"`

The `pair_key` is the SHA-256 of that canonical preimage. Names, UIDs, UUIDs, request order, request IDs, timestamps, viewer preferences, relationship history, narrative keys, and application orientation do not enter the preimage or any score.

PR03 may define the pure intrinsic cache-key string `magic10:v1:<pair_key>` where needed for interface conformance, but it must not create cache I/O, persistence, stale-cache application behavior, or new infrastructure. Those application concerns remain PR04.

### 6.5 Complete/fail-closed behavior

The kernel must reject or refuse without returning a partial successful result when any required normalized member, Channel state, signal mapping, profile, operation, weight, cap, threshold, configuration identity, release identity, source relation, output value, result field, ordering, or schema validation is missing, malformed, incoherent, out of domain, mutable where immutability is required, or stale.

The kernel must not catch an invalid contract and continue through a default, legacy calculator, partial matrix, caller configuration, generated snapshot, Markdown, old result, or alternate source.

## 7. Bounded files and components

### 7.1 Required owned loci

- New `engine/magic10/composite.py`: pure 36-Channel classifier and bounded state value types.
- New `engine/magic10/signals.py`: pure ordinary and Balance signal operations.
- `engine/magic10/calculators.py`: replace the transitional Decimal/file-loading category path with the adopted injected integer reducer behavior; no import-time repository reads.
- `engine/core/core.py`: canonical four-argument coordinator and pure result/identity construction.
- `engine/magic10/__init__.py` and `engine/core/__init__.py`: only the imports/exports required for the coherent new contract.
- `tests/core/test_engine_core_purity.py`.
- `tests/core/test_engine_core_abba.py`.
- `tests/core/test_engine_core_determinism.py`.

### 7.2 Bounded dependent loci allowed only when actual signature/evidence inspection requires them

- Existing signature-dependent callers of `compute_core` needed to keep the repository coherent. Application behavior remains PR04.
- Existing core evidence writer `tools/evidence/generate_engine_core_evidence.py`, its already governed four primary outputs, existing schemas, and actual required Human Index / Machine Mirror / hash / path-proof companions.
- Existing focused test helpers/fixtures needed to construct validated normalized members and an immutable synthetic admitted bundle without changing production admission.

PR-20 must inspect the current repository and name the exact files within this bounded set before implementation. It may not turn this allowance into a generic refactor, new evidence family, or release-manifest expansion. If a required file is outside this boundary for a material reason, preserve the finding and use the rescope path in §12.

### 7.3 Preserved predecessor surfaces

PR03 consumes but does not reopen or rewrite accepted PR01 catalog/config/schema data or accepted PR02 admission, normalizer, manifest, release, and execution-provenance behavior. An ordinary signature import adjustment is permitted only where directly required by the new PR03 contract and must preserve the predecessor's accepted semantics and tests.

## 8. Exact pure result contract

The complete pure result has schema identity `magic10_result.v1` and exactly these top-level fields:

- `schema`
- `config_id`
- `release_id`
- `pair_key`
- `signals`
- `categories`

`signals` contains exactly 20 rows in flattened caps-input order. Each row has exactly `signal_id` and integer `q` in `0..200`.

`categories` contains exactly 10 rows in canonical category order. Each row has exactly `category_id`, integer `score` in `0..100`, and `band` in `Cool`, `Open`, `Warm`, `Glow`.

`release_id` and `pair_key` are lowercase 64-hex strings. The result contains no person identity, request metadata, Gate payload, config copy, mutable handle, viewer preference, narrative key, shared/personal key, timestamp, cache record, or transport field.

Validate the produced result against the existing owning `schemas/magic10_result_v1.schema.json` and relational order/identity constraints at the proper pure boundary. PR03 does not produce the augmented `magic10_compat_result.v1`; PR04 owns that application augmentation and must not change PR03 scalars or intrinsic identities.

## 9. Acceptance, tests, and evidence

### 9.1 Requirement coverage

| Requirement / criterion | PR03 obligation and decisive evidence |
| --- | --- |
| `K040-REQ-001`, `AC040-01` | Deliver the complete planned PR03 slice without absorbing PR04–PR07/OPS01; preserve accepted dependencies and exact source ownership. |
| `K040-REQ-002`, `AC040-09` | Use PF01/PF02/PF12/PF14 owners and the decided C040-05/C040-06 interpretations; create no second mechanics, result, schema, or public home. |
| `K040-REQ-005`, `AC040-03` | Execute the exact five-state, 20-signal, 10-category, integer-only default mechanics against the admitted configuration and closed result schema. |
| `K040-REQ-007`, `AC040-04` | Consume only normalized Gates and injected immutable admitted configuration; validate the complete result; no core I/O or default. |
| `K040-REQ-008`, `AC040-04` | Decisive invalid/missing/incoherent inputs fail without partial success or legacy fallback. |
| `K040-REQ-009`, `AC040-05` | Exact chart fingerprint and pair identity remain distinct from config, source, manifest/release, and repository identities. |
| `K040-REQ-010`, `AC040-06` | Canonical behavior, AB↔BA and deterministic fixed oracles are implemented here; PR05 retains complete eight-case golden comparison/read-only tooling. |
| `K040-REQ-011`, `AC040-07/08` | Cover classifier, rounding, identity, result, immutability, purity, and adverse cases; readiness remains PR05. |
| `K040-REQ-012`, `AC040-08` | Refresh only applicable existing core evidence through its authorized writer and complete required companions; no generic new family or unrelated Distillation claim. |
| `K040-REQ-013` | Preserve exact source, test, commit, PR, workflow, evidence, prompt-use, and decision identities as they actually arise. |

`K040-REQ-003`, `K040-REQ-004`, and `K040-REQ-006` are accepted predecessor/interface obligations for this unit. PR03 must preserve them but does not claim to redeliver or reaccept them.

### 9.2 Positive proof

The dedicated PR Plan and implementation must include, at minimum:

1. All 16 ownership-bit classifier cases, including every first-match priority interaction and owner normalization.
2. Explicit Integration membership and `10-34` / `20-57` exception coverage.
3. Ordinary-signal and both Balance-operation exact-value tests, including all-none, one-sided owner mass, balanced owner mass, companionship/EM mass, and maximum responses.
4. Exact half-up rounding and category-band boundaries at 24/25, 49/50, 74/75, and 100.
5. Fixed G001–G006 core/kernel oracles from the authoritative source values; expected outputs must be independently fixed and must not call the function under test to calculate themselves.
6. AB and BA equality of the complete pure result and canonical bytes.
7. Distinct eligible people with equal Gate masks producing a complete identity-independent result with two equal intrinsic members.
8. Two identical runs over the same four explicit arguments producing identical values and canonical bytes.
9. Changing person identity alone not changing pure bytes or `pair_key`; changing a Gate mask, config identity, or release identity changing the appropriate intrinsic identity or refusing when inconsistent.
10. Exact 20-signal order, 10-category order, result-schema validation, and no extra field.

### 9.3 Adverse and purity proof

Prove rejection or no-success for:

- malformed/mutable/unvalidated member data and invalid Gate-mask/hex correspondence;
- missing/extra/duplicate/unknown Channel, signal, category, operation, profile, owner, or result field;
- booleans, floats, strings, zero or negative values where positive exact integers are required;
- out-of-domain q/score/band, cap/closure/order mismatch, and wrong or malformed release identity;
- caller-selected configuration, old `compat_score`, optional/default `CoreConfig`, legacy three-argument calls, and alternate calculator success;
- file, network, database, vendor, environment, locale, time, clock, randomness, process, cache, narrative, UUID, request-ID, and import-time side effects in core/composite/signals/reducer code;
- partial matrix/result after any failure;
- expected-output rewrites, self-confirming goldens, or generated snapshots used as mechanics authority.

### 9.4 Engineering review, CI, and evidence discipline

- Run the focused PR03 suites plus the complete applicable default regression suite locally under the repository's closed rails.
- Run each applicable governed writer/check and preserve primary/companion distinction. An index or hash is not the primary proof.
- Classify every changed path against all CI lanes. A skipped lane requires a scoped, evidence-backed non-applicability reason; no inherited exception or historical green run substitutes.
- Obtain substantive code review and security review of the actual final candidate. Address findings coherently, rerun affected local tests, and obtain corrected-code review where required.
- Reviews take priority over CI. Do not spend a CI run on code already known to require another push. After the final candidate has passed local validation and substantive review, run CI against that exact final head and preserve run/attempt/job/head identities.
- Counts may overlap and must not be summed. Synthetic fixture success is not actual release promotion, independent QA, or work-unit acceptance.
- Engineering completion stops at a truthful `MERGE_PENDING` result. Nathan / Product Owner owns any later manual merge. PR-40 independently decides lineage acceptance after the merge.

## 10. Exclusions and unchanged obligations

PR03 must not:

- change the approved mathematics, signal roster/map, profiles, weights, operations, caps, thresholds, category order, result schema, pair preimage, or configuration/release formula;
- modify accepted PR01 or PR02 behavior, rerun their accepted work, replace their Plans, or request another Proceed for them;
- create PR04 application eligibility, same-person handling, canonical UUID ordering, directional narrative keys, internal augmentation, cache I/O, Reader/CLI/HTTP presentation, or transport behavior;
- create PR05 complete eight-case golden collection/comparator or current-row readiness capability;
- modify the actual 15-member manifest, materialize the final 44-member release, recompute the final promoted identity, activate a release, or perform PR06 work;
- perform PR07 documentation, OPS01 final external attestation, QA, Ops, deployment, vendor/database access, PF10 edits, permanent Canon drainage, or Epic closure;
- add a public/API/CLI field, alternate config selector, hidden flag, duplicate serializer, duplicate catalog or schema owner, remote schema resolution, new persistent cache, or stronger multi-file/cross-process atomicity guarantee;
- claim HDE-DIST008.1, unrelated evidence families, or later work units complete from PR03 tests.

The actual PR03 implementation may reveal ordinary defects inside this bounded unit; the same PR03 engineer owns those repairs. A genuine scope, architecture, requirement, Canon, or design change is not absorbed as an implementation detail.

## 11. Migration, security, and recovery

### 11.1 Migration and compatibility

This is a code-contract migration from the superseded precomputed-score scaffold to the already approved four-argument Gate kernel. Update actual signature-dependent internal callers and tests in this PR as needed for a coherent build, but do not enable the PR04 application path early. No public schema, API, CLI, database, vendor, or production-data migration is authorized.

The result schema already exists from PR01 and the immutable admitted bundle already exists from PR02. A discovered need to change either accepted contract beyond an ordinary import/signature adaptation is a boundary finding, not permission to rewrite an accepted predecessor.

### 11.2 Security and privacy

Use only synthetic Gate fixtures. Do not put names, birth data, UUIDs, complete user records, secrets, tokens, environment values, or live vendor/database material in core results or evidence. Failures must not echo sensitive payloads. Pure modules may not traverse filesystems, resolve remote schemas, contact services, or use mutable globals.

### 11.3 Recovery

Before editing, preserve the exact repository baseline, worktree status, and any user changes. Do not discard or overwrite unrelated work. If implementation is interrupted, retain the same dedicated PR03 session, workspace/worktree, branch, commits, test results, review state, and uncommitted delta; report the exact resume point.

Rollback/restoration must treat core, pure mechanics modules, signature-dependent callers, tests, and actually affected evidence as one compatible set. Do not restore only the old core while leaving migrated callers, or hide a mismatch by retuning configuration or rewriting expected outputs. Leave the accepted PR01/PR02 data/admission boundary and actual 15-member release untouched.

## 12. Rescope and owner boundaries

If implementation or PR planning establishes a genuine material mismatch with the approved scope:

1. Preserve all completed PR03 planning/engineering work and exact evidence.
2. Assign a stable `FINDING_REF` bound to HDE-EPIC040-PR03.
3. Stop only the affected boundary and return the evidence to the retained whole-change HDE-EPIC040 IA through `RS-10 — Create Bounded Work-Unit Rescope Proposal`, followed by `RS-20 — Review Bounded Work-Unit Rescope`.
4. An approved bounded delta becomes a separate PF10 build-notes addendum overlay. Nathan / Product Owner alone manually drains and verifies it before the existing PR implementation resumes through the applicable native return.
5. Do not rewrite the immutable whole-change Plan, mint a replacement Proceed, rerun an accepted PR, or treat a proposal/review as implementation authority.

An ordinary in-scope defect stays with the PR03 engineering owner. A true product-objective, exclusion, or Specification change returns to Nathan and the existing Specification/Thoth delta path. No role self-approves its own boundary change.

## 13. Complete carried Canon-conflict register

| ID | Current decision | Effect carried into PR03 | Remaining owner/state |
| --- | --- | --- | --- |
| `C040-01` | `CANON_RECONCILIATION / APPROVED` exactly as proposed by Thoth-17 at `2026-09-08T13:23:24Z` | Preserve explicit Done exclusions and current PF09.3 agreement; do not reopen rows. | Source correction resolved; no new decision. |
| `C040-02` | `CANON_RECONCILIATION / APPROVED`, same Thoth decision | Use current PF12 v2.9.6 Markdown and preserve historical identity mismatch only as history. | Source correction resolved. |
| `C040-03` | `CANON_RECONCILIATION / APPROVED`, same Thoth decision | Use current PF14 v3.5.7 Markdown; C040-05 separately controls contradictory core-test text. | Historical version mismatch resolved. |
| `C040-04` | `CANON_RECONCILIATION / APPROVED`, same Thoth decision | QA identity history is preserved; PR03 performs engineering checks, not independent QA. | Historical version mismatch resolved. |
| `C040-05` | `CANON_RECONCILIATION / APPROVED`, alternative A, Isis-49 at `2026-09-09T03:57:16Z` | The exact four-argument Gate-based `compute_core` supersedes the successful precomputed-score/CoreConfig passages. Remove/migrate the old path and tests; do not keep a second calculator. | Permanent PF14 §6.7 maintenance remains with its governed maintainer; pending maintenance is non-gating. |
| `C040-06` | `NEW_CANON / APPROVED`, alternative A, Isis-50 at `2026-09-09T11:48:08Z` | Use the complete 36-row taxonomy and 16-case state conformance; four Integration members and the `10-34` / `20-57` exceptions; no changed weights. | Permanent PF12 §2.1 / PF01 §§6.1–6.2 maintenance remains with governed maintainers; pending maintenance is non-gating. |

F01/F02/F03 are approved and drained PR02-only rescope overlays. Their engineering effects are accepted through the PR02 lineage review; they are not new register entries or PR03 change authority.

No conflict is reopened, relabeled, omitted, or newly decided here. The rejected Plan v1.0 and denied Plan v2.0 remain historical artifacts with no authority over this instruction.

## 14. Ownership, return, and current truth

- Instruction author and whole-change return owner: Product Owner-assigned retained whole-change HDE-EPIC040 Implementation Architect.
- PR-20 receiver: one dedicated PR engineering session for `HDE-EPIC040-PR03`. The operator selects that existing/created dedicated session; this handoff does not create it or repurpose the whole-change IA.
- PR03 engineering owner after Product Owner Proceed: that same dedicated PR03 session.
- Manual merge owner: Nathan / Product Owner.
- PR-40 lineage reviewer after actual merge: the retained whole-change HDE-EPIC040 Implementation Architect in its established read-only lineage-review role, not the PR03 engineer and not Isis-50.
- Isis-50 remains the independent reviewer of the immutable whole-change Plan; this instruction does not request another Plan review.

Current truth at instruction publication: PR03 instruction ready; detailed PR Plan `NOT PRODUCED`; Product Owner Proceed `NOT REQUESTED` and `NOT EXECUTED`; implementation/branch/commit/PR/review/CI/merge `NOT EXECUTED`; QA/Ops/release/closure `NOT EXECUTED`.

## 15. Prompt-use and provenance continuity

`GCFPE_PROMPT_USE`:

- `usage_id`: `GCFPE-USE-HDE-EPIC040-PR-10-20260914-PR03-01`
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`
- `work_unit_id`: `HDE-EPIC040-PR03`
- `component`: pure Gate mechanics and intrinsic identity
- `requirements`: `K040-REQ-001`, `K040-REQ-002`, `K040-REQ-005`, `K040-REQ-007`–`K040-REQ-013`; acceptance criteria `AC040-01`, `AC040-03`–`AC040-09` as allocated in §9
- `ecosystem_release`: `GCFPE-20260913.1`, exactly 54 members
- `prompt`: `PR-10 — Create PR Work-Unit Instructions — 091326.2`
- `prompt_page`: `https://app.notion.com/p/3da4590a05eb81c594a0f9bf5cb151a7?pvs=204`
- `role_stage`: retained whole-change IA / PR03 instruction creation
- `capture_time`: `2026-09-14T06:50:55Z`
- `runtime_identity`: not asserted beyond the Product Owner-assigned role/session reference
- `result`: this `HDE-EPIC040-PR03-PR-INSTRUCTION v1.0`, `INSTRUCTION_READY`

Repository inspection found no installed GCFPE prompt-provenance procedure under `docs/changes`; only `AUDIT_RESULTS.json` and `AUDIT_SUMMARY.md` were present. Repository persistence is therefore `PENDING / NON_GATING` for a later authorized writer under an actually installed supported procedure. No procedure, schema, writer, or repository destination is invented by this instruction.

## 16. Direct PR-20 native handoff

```plain text
NEXT_PROMPT_HANDOFF

Run PR-20 — Create Detailed PR Implementation Plan — 091326.2:
https://app.notion.com/p/3da4590a05eb8147b34ccfabf608c2e3?pvs=204

Act as the dedicated PR engineering session for exactly HDE-EPIC040-PR03. This is the initial dedicated PR03 planning assignment. Do not repurpose the retained whole-change IA, Isis-50, the PR01/PR02 engineering sessions, or any accepted lineage-review role.

EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: INITIAL_DEDICATED_ASSIGNMENT
role_session_ref: dedicated PR engineering session for HDE-EPIC040-PR03
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR03 / PR-20
context_conflict: NONE

Sole substantive input:
- PR_INSTRUCTION_ID: HDE-EPIC040-PR03-PR-INSTRUCTION v1.0, INSTRUCTION_READY
- Direct Drive link: https://drive.google.com/file/d/1Zj5BResRRxtGarmZ2d3sIAfIVeLD42rs/view?usp=drivesdk

The instruction contains the complete approved lineage and source package. Preserve these controlling bases:
- HDE-EPIC040 Specification v1.1, Thoth-17 APPROVE:
  https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk
- HDE-EPIC040 Implementation Audit v2.0, AUDIT_COMPLETE:
  https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk
- Immutable HDE-EPIC040 Implementation Plan v2.1:
  https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk
- Approving Plan Review v2.1, Isis-50 APPROVE:
  https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk
- Accepted PR01 lineage review v1.1:
  https://drive.google.com/file/d/15JiKkcctc46gJ3fqshCtmvHxzEymhj_i/view?usp=drivesdk
- Accepted PR02 lineage review v1.0:
  https://drive.google.com/file/d/1S82tr4pdi_rbOM-5YrcD4slRzro01zge/view?usp=drivesdk
- Current controlled PF10 Markdown v13.2.4:
  https://drive.google.com/file/d/136EVMhrQAkC-u4hzvUlzCl4wYIY0pZ8b/view?usp=drivesdk

Current repository baseline:
- Repository: amthorn78/glow-hdengine-v2
- Target: main
- Head: 5b2fb8d70924a6710b6261fc0c93d3869fed6380
- Tree: e43c2063599e7bc449f20d4ab045d32d95581bf4
- PR01/#403 and PR02/#404 are accepted and final. Do not reopen or rerun them.
- No PR03 branch, commit, pull request, detailed Plan, Proceed, implementation, review, CI, or merge exists.

Work unit:
- HDE-EPIC040-PR03 — Pure Gate mechanics and intrinsic identity.
- Build the exact four-argument pure Gate kernel, five-state classification, 20 ordered signals, 10 category scores/bands, intrinsic chart fingerprints and pair identity, and closed magic10_result.v1.
- Replace the successful precomputed-score/CoreConfig scaffold and migrate bounded core tests and signature-dependent evidence/callers.
- Consume accepted PR02 normalized Gates and injected immutable bundle. Do not load configuration in core or promote the actual incomplete 15-member release.

Preserve exclusions:
- PR04 application eligibility/orientation/cache/transports; PR05 complete golden readiness; PR06 actual 44-member release materialization/promotion; PR07 documentation; OPS01; QA/Ops/deployment/PF10 edits/Epic closure.
- No new public/API/CLI field, selector, hidden bypass, duplicate mechanics/schema/serializer owner, remote schema, persistent cache, live vendor/database access, stronger atomicity guarantee, or alternate calculator.
- PR02 F01/F02/F03 overlays remain effective only for accepted PR02 and do not grant PR03 scope changes.

Required action:
Read the complete PR_INSTRUCTION and its exact linked sources and inspect all affected repository files. Create one complete executable PR_IMPLEMENTATION_PLAN for this exact work unit with actual files/components, implementation order, interface seams, requirement-to-change/test mapping, local validation, governed evidence writers/companions, code/security review, final exact-head CI, risks, recovery, exclusions, carried Canon-conflict register, manual merge boundary, and direct PR-30 handoff. Do not mutate the repository in PR-20.

If and only if the plan is complete and within the approved scope, save/read back it in Glow / Ephemeral Planning Files and return AWAITING_PO_PROCEED with its exact direct Drive link. That state does not authorize implementation. A genuine material boundary returns the completed bounded planning draft and exact RS-10 route; do not rewrite an approved base or request a replacement Proceed.

Expected output:
One saved and read-back HDE-EPIC040-PR03 PR_IMPLEMENTATION_PLAN with exact version, direct Drive link, truthful state, and one complete paste-ready PR-30 handoff for Nathan / Product Owner to invoke against that exact plan. Do not implement, commit, push, create a PR, merge, run QA/Ops, edit PF10, activate a release, or close the Epic.
```
