## **Header**

**Title:** PF31-Reference-HDE-State-of-the-Repository

**Version:** v0.1

**Status:** Canon

**Effective date:** 2026-09-15

**Last Update Gate:** Creation

**Assessment date: September 15, 2026**  
**Repository snapshot:** `amthorn78/glow-hdengine-v2`, `main` at `9cda1b49a972da874021e8820997fab1ebaff153`  
**Latest implementation milestone in that snapshot:** EPIC040 PR03, “Pure Gate mechanics and intrinsic identity,” merged September 14\. PF10 v13.2.6 records PR01, PR02, and PR03 as accepted dependencies, with PR04 next.

## **Overall assessment**

**Glow HDE has a substantial engineering foundation and a genuinely implemented Gate-based calculation core. It does not yet have a complete, consistently integrated, production-qualified implementation of that core across its supported product surfaces.**

The most important distinction is between **the engine calculation that now exists** and **the application paths that actually serve results**. The new core computes the full internal Magic10 result from Gates and Channel states. However, the existing compatibility implementation still contains UID-hash scoring, and the Reader implementation still uses an older Type-based Harmony calculation. The approved plan explicitly assigns replacement and integration of those paths to PR04. This is unfinished integration work, not evidence that the accepted PR03 core is merely a placeholder.

My answers to your three questions are:

| Question | Assessment |
| ----- | ----- |
| **Where are we now?** | A meaningful calculation kernel has landed, supported by substantial contract validation and engineering tests. The surrounding application remains transitional, and the complete new release has not been materialized. |
| **What still needs to be done?** | Complete consumer integration, full-result comparison and readiness tooling, final release assembly, documentation, and exact-source verification. Beyond EPIC040, complete the required operator-facing product, runtime hardening, performance qualification, and deployment/rollback controls. |
| **Biggest risks and challenges?** | Different entrypoints producing different kinds of results; startup controls not being applied consistently; code, configuration, release identity, and stored chart readiness becoming misaligned; and treating scoped passing evidence as proof of a complete operating product. |

These judgments follow from the current source and the explicit remaining work recorded in PF10 and PF09.

**I would not recommend starting over. I would recommend completing and consolidating the existing implementation, while addressing the concrete startup-control issue described below before production qualification.**

### **Scope of this assessment**

I examined current repository source, selected tests, CI configuration and results, and relevant PFCanon sections, including the current implementation plan linked from PF10. I also ran one isolated, source-hash-verified reproduction of an environment-guard issue.

I did **not** rerun the repository’s full test suite, inspect production database contents, call the chart vendor, perform a load test, or verify the deployed Railway process and its settings. Accordingly, this is an engineering assessment, not an independent production-readiness certification.

---

## **1\. Where we are now**

### **1.1 The new calculation core is real and materially more complete than the active consumer paths**

The current `compute_core` implementation takes four explicit inputs:

```
compute_core(member_a, member_b, mechanics_bundle, release_id)
```

It validates normalized Gates and the admitted configuration bundle, classifies Channel relationships, calculates twenty ordered signals, and reduces them into ten ordered category scores and bands. Its result is an immutable six-field contract containing schema, configuration identity, release identity, intrinsic pair identity, signals, and categories.

Several aspects are sound engineering choices:

**Deterministic calculation.** The core uses explicit inputs, integer-based signal values, governed rounding, fixed ordering, and reproducible identity construction.

**Separation from operational effects.** The calculation function does not acquire charts, select providers, read databases, or perform filesystem operations. Those responsibilities are outside the calculation boundary.

**Intrinsic identity.** The new pair identity is based on normalized chart information and configuration/release identity, rather than allowing a user identifier to determine compatibility.

**Strict refusal behavior.** Malformed Gates, inconsistent masks, incoherent configuration identities, and malformed results are rejected rather than silently repaired into successful calculations. These properties are visible in the current implementation.

The reviewed tests also go beyond superficial schema checks. They include the sixteen endpoint-ownership combinations, fixed expected signal and category results, Balance-operation cases, invalid-input rejection, configuration mutation, and immutability checks. That is meaningful behavioral testing.

**My assessment:** the new core is an asset worth preserving. The next challenge is making it the sole calculation authority wherever the product claims to perform the new mechanics.

### **1.2 The repository currently contains different generations of calculation behavior**

This is the most important source-level finding.

| Component | Current behavior | Engineering implication |
| ----- | ----- | ----- |
| **New core** | Gate/Channel-based calculation producing twenty signals and ten categories. | The intended calculation foundation exists. |
| **`engine/compat/compute.py`** | Category scores are derived from a stable hash of pair identity and category, then modified by viewer weights. | This is not the new Gate-based calculation and must not remain an alternative successful path for the integrated product. |
| **`engine/runtime/public.py`** | Calls `ts_v0` and builds a Harmony-only projection. | The Reader calculation path is not yet connected to the new core. |
| **`ts_v0.band_v0`** | Returns Warm when both Types are sacral; otherwise Open. | Existing Reader behavior is much narrower than the new mechanics. |
| **HTTP Reader** | GET is development-only and fixture-backed; POST returns 405\. | The production chart-backed Reader success path remains to be implemented. |

These are directly observable differences in the current code.

There is an important qualification: the compatibility HTTP endpoint has a production-mode guard that returns 404\. I am **not** claiming that the repository intentionally exposes UID-hash scoring as its production API. I am saying that transitional scoring remains in active development/internal paths and has not yet been replaced by the new core.

Also, **full internal Magic10 calculation does not mean expanding the public Reader to ten categories or exposing numeric scores**. The approved plan preserves the separate, numeric-free public contract while requiring the internal calculation and applicable internal outputs to use the complete governed result.

### **1.3 Current CI is green, and that deserves recognition**

The exact reviewed `main` commit has a successful hosted `test` check. The recorded run started September 14 at 12:33:19 UTC and completed successfully at 12:45:18 UTC. This assessment is therefore **not** based on an assumption that the repository is presently failing CI.

The workflow has useful safeguards: exact-candidate checkout, closed deterministic environment settings, affected-test execution in isolated worktrees, separate validation lanes, evidence-integrity checks, and clean-tree verification. Its lanes cover product behavior, compatibility, database contracts, rails, evidence, the generic QA subsystem, and release attestation.

PF10 also records substantial PR03 engineering validation:

* 730 passing focused tests.  
* 1,893 passing default-regression tests, with three existing closed-rails vendor skips.  
* 1,970 passing clean affected-suite tests.

Those counts overlap and must not be added together. They are recorded engineering results, not tests I independently reran and not independent QA/Ops acceptance. PF10 makes that distinction explicitly.

**The limitation is what those tests establish.** The core tests use a synthetic complete release fixture. A passing calculation against that fixture does not establish that the repository’s actual release pack is complete, that the HTTP consumer uses that calculation, or that real stored charts satisfy the new input requirements.

### **1.4 The actual release pack has not caught up with the new implementation**

The current `catalog/manifest.json` contains fifteen members. PF10 explicitly says that the actual release remains this incomplete manifest for the new Magic10 work, and assigns final forty-four-member materialization, identity recomputation, convergence, and promotion to PR06.

This is not, by itself, a corrupted-manifest finding. It is an **explicitly unfinished release transition**.

The engineering consequence is that these states must remain separate:

> Code merged → application integrated → complete release assembled → final candidate verified → deployment authorized → deployed behavior verified.

The current CI workflow even states that its generated attestation bundle is not consumed by an active release or deployment workflow. A successful CI attestation therefore should not be interpreted as proof that the complete new mechanics release has been deployed.

---

## **2\. What still needs to be done**

### **2.1 Finish the existing EPIC040 sequence**

The approved sequence is coherent. I would retain it rather than replace it with another broad redesign.

| Remaining unit | What it must accomplish | What completion would establish |
| ----- | ----- | ----- |
| **PR04: Application, identity, and consumer integration** | Connect the selected compatibility, CLI, HTTP, Reader, narrative, and presenter paths to the canonical Gate-based result. Remove successful UID-only substitutes and legacy scoring authority. | The implemented application actually uses the new mechanics and preserves its public/private contracts. |
| **PR05: Golden comparison and Gate-readiness tooling** | Complete comparison against all eight governed golden cases and implement read-only current-row Gate-readiness checking. | Complete outputs can be checked reproducibly, and missing or invalid chart data can be identified without acquiring or changing it. |
| **PR06: Complete release admission and evidence convergence** | Materialize the complete release roster, bind actual source/configuration bytes, and regenerate dependent artifacts through their existing owners. | The real candidate, rather than a synthetic fixture, is a coherent admitted release. |
| **PR07: Final repository documentation** | Document the actual implemented interfaces, commands, ownership, and release limitations after implementation. | The final repository describes what it actually supports. |
| **OPS01: Final clean-candidate external verification** | Verify the final post-documentation candidate without modifying the repository. | The final committed candidate has attributable external verification evidence. It does not establish deployment or independent QA acceptance. |

These responsibilities and boundaries are explicit in the current plan.

#### **PR04 is the most important remaining implementation step**

PR04 is not merely replacing one function call.

It must preserve complete chart-bearing inputs through the application, distinguish stored-user and birth-only resolution, enforce the appropriate acquisition restrictions, and ensure that all selected consumers receive the same canonical calculation. It must also preserve the public Reader’s stricter lookup and no-acquisition boundary.

The identity cases are particularly important:

**The same person with consistent chart data** must be handled as an ineligible self-pair without invoking the core, cache, or narrative router.

**The same identity with inconsistent chart projections** must be rejected.

**Different people with equal Gate masks** must not be mistaken for a self-pair. They can share intrinsic calculation identity while still requiring correct person-specific narrative orientation.

The plan requires these distinctions, including fixed identity-boundary proofs and protection against cached narrative keys being contaminated by another pair of UUIDs.

This is where correctness becomes application-level rather than purely mathematical. A correct kernel surrounded by incorrect eligibility, identity, cache, or projection logic still produces an incorrect product.

### **2.2 Complete the separate chart-loader boundary correction**

The non-BodyGraph loader under `engine/charts/loader.py` still mixes input normalization with environment inspection, clocks, provider orchestration, and filesystem logging. It also contains explicitly fixture-oriented returns, including Gates `[1, 2, 3]`, and a legacy fallback when the provider resolver is unavailable.

I am not attributing that behavior to the sanctioned HDAPI BodyGraph resolver. It is a separate, older loader boundary.

PFCanon already assigns the correction to **HDE-SEPA006**: move operational orchestration to the Adapter, retain pure validation/normalization in the Engine, identify and migrate supported callers, and prove the resulting side-effect boundaries. It is marked Required-Now and is explicitly separate from the Magic10 configuration work.

This work should have a bounded implementation and caller inventory. An import-path rename alone would not resolve it.

### **2.3 Complete the required operator-facing product, not just the calculation**

PFCanon requires more than a callable kernel before Glow App integration.

The full admin product includes both BodyGraphs, the complete internal compatibility result, and three narratives: A→B, B→A, and shared. It also requires consistent CLI/HTTP composition and authentication and audit controls. **HDE-COAG006 remains Not done.**

Likewise, generic-terminal CLI access to the full product is a required pre-Glow capability, not merely an optional developer convenience. Its checklist remains Partial and explicitly says that existing harness evidence does not establish the full payload or arbitrary-terminal production access.

**Finishing EPIC040 should therefore not be reported as finishing the entire usable HDE product.** It enables an essential part of that product.

### **2.4 Complete production packaging and lifecycle behavior**

The packaging/runtime checklist remains Partial. Its outstanding areas include reproducible images, broader environment and secrets discipline, production-path health/readiness, graceful shutdown, input hardening, and complete terminal access.

There is a concrete packaging issue worth resolving during that work: `pyproject.toml` declares version `0.0.0` and an empty project dependency list, while runtime dependencies live in `requirements.txt`. CI installs those requirements separately before installing the project in editable mode.

That can support a source-checkout workflow, but it does not demonstrate a self-sufficient distributable package.

I would require a clean installation test outside the development checkout that proves the chosen distribution includes its dependencies, schemas, catalogs, entrypoints, and required runtime data. The declared supported Python range should also match versions actually qualified by testing.

### **2.5 Complete performance and operational qualification**

The remaining operational work is substantial and explicitly recorded:

| Area | Recorded remaining work |
| ----- | ----- |
| **Performance** | Reproducible profiles, warm/cold runs, bounded concurrency, latency measurements, and parity under load. |
| **Runtime lifecycle** | Meaningful health/readiness checks and graceful shutdown evidence. |
| **Operations** | Build, release, rollback, and incident runbooks. |
| **Observability** | Production dashboards and actionable alerts for errors, latency, cache behavior, and other governed signals. |
| **Magic10 activation** | One-active-configuration checks, compatible rollback pack, real Gate-readiness inventory, and separately authorized deployment/smoke/rollback. |

The performance harness is Not done; lifecycle work is Partial; runbooks and production monitoring remain unfinished.

Building the Gate-readiness tool and running it against actual eligible stored rows are separate accomplishments. PFCanon requires incomplete rows to block activation and any refresh to occur through separately authorized operations, not through a request-time vendor or scoring fallback.

There is also further planned integration work, including TypeScript/Python SDKs. Optional production caching should remain distinguished from required launch work rather than being allowed to inflate the immediate critical path.

---

## **3\. Biggest risks and challenges**

### **Risk 1: Successful output from the wrong calculation path**

**Priority: Highest product-correctness risk.**

The danger is not limited to exceptions or crashes. A transitional calculation can produce valid JSON, correct ordering, stable hashes, and plausible bands while using the wrong underlying mechanics.

The current UID-hash compatibility path and Type-only Reader calculation make that a concrete migration concern. Their existence is known and planned for, but integration must prove that the intended successful paths no longer reach them.

**What would reduce this risk:** tests that begin at the supported CLI and HTTP entrypoints, use complete chart inputs, and verify fixed expected results from the new mechanics. Those tests should also prove the absence of legacy fallback, not merely the presence of a new core call somewhere in the source.

This is why PR04 and the complete comparison work matter more now than adding more standalone calculation features.

### **Risk 2: Runtime controls differ between application entrypoints**

**Priority: High. Concrete source-level finding with an isolated reproduction.**

The repository’s Procfile starts:

```
adapter.factory:create_app()
```

That factory registers routes and some response handling, but it does not install the logging filter or invoke the startup environment guard found in `adapter/wsgi.py`. The WSGI module also adds health/readiness routes and common headers that are not established by the same initialization path.

Several tests and a local application entrypoint use the WSGI factory instead. Consequently, a passing test against that factory does not automatically prove the same initialization behavior in the Procfile-selected application.

There is a second, more specific problem. The WSGI factory calls:

```
validate_or_fail(app)
```

The guard’s coercion wrapper selects `app.config` when given an app-shaped object. That is different from validating the process environment. The factory does not populate the relevant environment keys into that configuration before making the call.

I tested the exact guard source, verified against its Git blob hash, using synthetic production settings and a minimal app-shaped configuration object:

| Isolated check | Result |
| ----- | ----- |
| Guard reads the synthetic process environment directly | Rejected all 21 prohibited-setting cases. |
| Guard receives the app-shaped configuration used by the startup call pattern | Allowed all 21 cases. |
| Guard receives the explicit environment mapping | Rejected all 21 cases. |

The 21 cases cover three production aliases and seven prohibited override keys. **This was not a full Flask startup test or a test of your deployed environment.** It confirms the configuration-selection problem in the isolated call pattern.

Download the isolated guard reproduction results

**What would reduce this risk:** one authoritative production bootstrap, explicit validation of the intended configuration source, and negative tests through the actual configured entrypoint. Those tests should demonstrate that prohibited production settings prevent startup and that required logging and lifecycle behavior are installed there.

I would treat this as a bounded engineering correction, not as a reason to reopen unrelated accepted mechanics work.

### **Risk 3: Code, release identity, cache identity, and chart readiness diverge during cutover**

**Priority: High integration and availability risk.**

The current core is stricter than the transitional consumers. That is desirable, but it means previously tolerated UID-only or incomplete chart inputs cannot continue to succeed.

The plan requires complete chart preservation, strict eligibility, stale intrinsic-cache validation, deterministic person-specific augmentation, and refusal when a valid admitted release is unavailable.

A technically correct fail-closed implementation can therefore still produce an operational failure at activation if the actual data and release pack are not ready.

The answer is **not** a fallback scorer. It is preflight evidence that the deployed code, configuration, schemas, release identity, and eligible chart rows form a compatible set.

Rollback must also restore that compatible set. Reverting code while retaining incompatible configuration or cached results is not a reliable rollback strategy; the plan already calls for restoring compatible code/configuration/schema/projection/manifest combinations.

### **Risk 4: Green CI is not the same as enforced release safety**

**Priority: High process-control risk.**

The retrieved branch settings report `main` as unprotected, with required status-check enforcement disabled. A separate ruleset query was unavailable because the API returned a feature/access restriction, so I did not establish whether any additional ruleset control exists.

The concern is the gap between **having a good CI workflow** and **making successful exact-head validation a mandatory condition of merging or releasing**.

I would verify and enforce the applicable repository controls so that a merge cannot accidentally rely on a previous green commit, incomplete review, or an informal expectation that CI will finish later.

At the same time, I would preserve the current cost-aware affected-test approach. The classifier explicitly attempts to fail safely on unknown paths and maintains test-ownership mappings. That mechanism should remain tested as code evolves; its existence should not be confused with universal test coverage.

### **Risk 5: The verification system is becoming a significant system to maintain**

**Priority: High maintainability and delivery risk.**

The repository has sophisticated configuration admission, source identity, generated evidence, companion proofs, indexing, and CI selection. Those controls provide real benefits, but they also create dependencies that must remain correct.

For example, the current registry loader handles frozen domain contracts and admission structures, while the core independently checks admitted bundle coherence and source projections. The CI classifier maintains explicit ownership and selection rules. PF10 also records bounded executable-equivalence verification over eight executing owners.

My concern is not that these controls are inherently wrong. It is that their maintenance can consume attention while the usable application remains incomplete.

I would keep the near-term engineering emphasis on a small number of externally meaningful outcomes: the supported entrypoint uses the correct calculation; invalid inputs fail correctly; the real release is coherent; an operator can retrieve the required product; and the service can be deployed and rolled back safely.

That does not require another governance layer. It requires keeping existing evidence directly attached to those behaviors.

### **Risk 6: “The service starts” is being asked to stand in for operational readiness**

**Priority: High before production use.**

The alternate WSGI module’s health/readiness handlers return unconditional success payloads. Those responses do not inspect whether the intended mechanics configuration and release are ready to serve the product. Meanwhile, PFCanon’s required readiness behavior includes initialization of relevant components and verified runtime state.

Performance is also unqualified by the evidence reviewed here. The core performs substantial coherence validation, and the application adds resolution, serialization, identity, and potentially cache work. Those costs should be measured under the intended service workload rather than inferred from unit-test speed. The required performance harness remains Not done.

I would not assign a throughput capacity, latency expectation, or production reliability level from the current evidence.

---

## **4\. How I would prioritize the remaining work**

### **First: Preserve the accepted foundation and finish real integration**

Continue the approved PR04 integration work without redesigning the accepted calculation kernel. Address the startup/control-wiring finding through the appropriate bounded engineering owner before production qualification.

The key milestone is not “all modules import.” It is:

> The supported application entrypoints produce the governed result from complete chart data, preserve identity and public/private boundaries, and cannot silently use a transitional scorer.

### **Second: Finish the actual release, not another representative fixture**

Complete the golden comparison, actual manifest assembly, dependent artifact convergence, final documentation, and final clean-candidate external verification.

A candidate should be described as complete only when those checks apply to the actual final committed source. The current plan already provides this sequence; it should not be replaced with a new parallel acceptance mechanism.

### **Third: Prove the required operator experience and operating posture**

Before declaring the broader HDE product ready, demonstrate the required full admin bundle through the supported terminal/API paths, then qualify the actual production bootstrap, data readiness, performance, monitoring, shutdown, deployment, and rollback behavior under the applicable authorizations. These obligations remain separate from EPIC040’s final source verification.

## **5\. What I would require before calling this “ready”**

| Readiness question | Required evidence |
| ----- | ----- |
| **Does the application use the correct mechanics?** | Entry-point tests prove canonical Gate-based calculation and no reachable successful legacy fallback. |
| **Are identity and data boundaries correct?** | Self-pair, inconsistent-identity, equal-mask/different-person, missing-Gate, and narrative-orientation cases behave correctly. |
| **Is the real release complete?** | Final source, complete manifest, configuration, generated artifacts, and external verification agree. |
| **Can the operator use the actual product?** | The required full bundle is retrievable through the supported authenticated CLI/admin interfaces. |
| **Is the deployed runtime the tested runtime?** | The configured bootstrap has verified environment guards, logging, meaningful readiness, and lifecycle behavior. |
| **Can it operate and recover safely?** | Measured performance, actionable monitoring, verified chart readiness, and a compatible, tested rollback procedure. |

These are an engineering summary of the existing integration, admin-product, and operational requirements, not a new expansion of EPIC040’s scope.

## **Bottom line**

**The repository is not empty, and the recent mechanics work is not superficial. There is a credible, tested calculation foundation to build on.**

**The largest remaining gap is turning that foundation into one consistent, usable, safely operated product.** The active consumer paths, actual release pack, operator-facing bundle, and production lifecycle have not all reached the same level of completion.

I would describe the current state as **a partially integrated implementation with a substantial new core, rather than a production-ready HDE**. The strongest path forward is to finish the existing integration and release sequence, correct the runtime-control discrepancy, and judge completion by demonstrated end-to-end behavior rather than by the number of accepted PRs or accumulated evidence files.

