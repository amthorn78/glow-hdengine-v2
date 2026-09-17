# HDE-EPIC040 — Whole-Change Implementation Audit

## 1. Identity, lineage and disposition

| Field | Value |
| --- | --- |
| artifact_type | IMPLEMENTATION_AUDIT |
| logical_id | HDE-EPIC040-IMPLEMENTATION-AUDIT |
| version | 1.1 |
| CHANGE_CLASS / CHANGE_ID | EPIC / HDE-EPIC040 |
| change_name / phase | Separation Pass 3 / Separation |
| producer_role | Implementation Agent — dedicated whole-change IA |
| author_session_ref | This actual IA-10 conversation, dedicated to HDE-EPIC040 by the Product Owner's supplied approved Specification; no platform session ID or numbered alias invented |
| predecessor_ref | libfile_c8a9601b01688191a322b63a45f3c510; HDE-EPIC040-implementation-audit-v1.0.md; HDE-EPIC040-IMPLEMENTATION-AUDIT v1.0; complete preserved predecessor |
| created_time_utc | 2026-09-08T22:02:37Z |
| SPECIFICATION_REF | libfile_12bab860949c8191881510875f051460; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-SPECIFICATION v1.1; SPECIFICATION_APPROVED; /Glow HDE 3.0 |
| approval lineage | Isis-49 substantive v1.0; Thoth-17 APPROVE 2026-09-08T13:23:24Z; v1.1 changes approval metadata only; reviewed predecessor libfile_34fb7876c10081919a7f49306d08e91f, SHA-256 c4b608c159d48160c418863cf4c5b916280004fb6ae0cdc3203eb5997350699a |
| formation lineage | HDE-EPIC040-SPECIFICATION-KICKOFF v1.0, KICKOFF_READY, libfile_b2399ebf8778819191593946b1cdaa45; exact pinned PF09.3 v1.1.3 |
| repository / observed branch | amthorn78/glow-hdengine-v2 / main |
| inspected commit / tree | 9065e6f0c01ad82a65c78687cd6c55e26ca33a1f / e07c4e4297c75fe83e0f286aa1cee46ffca6c62e |
| state | AUDIT_COMPLETE |
| planning_disposition | SUPPORTS_COMPLETE_PLAN_WITH_EXPLICIT_DEPENDENCIES |
| next_consumer | Same dedicated IA, Plan phase within this IA-10 invocation; then Isis-49 through Analyzer and IA-30 |
| execution_posture | MANUAL_PROMPT_EXECUTION; operator-direct native intake; no preceding Analyzer result was supplied in this conversation and none is invented |
| output classification | EPHEMERAL_LIBRARY; complete Markdown in /Glow HDE 3.0; source inspection work is TRANSIENT_SCRATCH |

**Finding:** The approved scope is sufficiently defined to plan. Every requirement below has a disposition, but the selected implementation is not complete at the inspected head. The complete golden-comparison requirement has real canonical-core and bounded application-projection dependencies. They must be planned explicitly; a configuration-only implementation, generated success report or deferred golden subset cannot satisfy the selected task. No substantive Specification scope blocker has been established by the inspected evidence. The remaining source-confirmation and execution prerequisites are named below and remain subject to Isis's independent Plan review.

Version 1.1 is a complete successor correcting one golden-to-predicate description in §6: M10-G002 exercises both Balance operations; M10-G003 specifically isolates equilibrium ownership and swap behavior. No requirement, finding, planning disposition, source, scope, conflict decision or approval changes. The original Audit v1.0 was saved and read back before Plan drafting; this bounded correction is saved before final Plan publication.

The Audit was completed before the separate Implementation Plan was authored. It grants no implementation, merge, Ops, independent QA, release, PF09 status or closure authority.

## 2. Approved scope and preserved boundary

Selected source status is inventory history, not this Audit's outcome:

| PF09 unit | Exact source title | Source status | This Specification's disposition |
| --- | --- | --- | --- |
| HDE-SEPA005 | Production Magic10 mechanics configuration contract | Partial | In scope: coherent parent obligation |
| HDE-SEPA005.1 | Corrected canonical 36-Channel catalog | Partial | In scope |
| HDE-SEPA005.2 | Magic10 mechanics schema and default configuration | Partial | In scope |
| HDE-SEPA005.3 | Fail-closed mechanics configuration loader | Not done | In scope |
| HDE-SEPA005.4 | Mechanics configuration identity and deterministic comparison | Not done | In scope |
| HDE-SEPA005.5 | Separation implementation tests and governed artifacts | Not done | In scope |


All 29 Done/context units remain excluded, without reopening or fresh reacceptance:

| PF09 unit | Exact source title |
| --- | --- |
| HDE-SEPA001 | Persistence Layer |
| HDE-SEPA001.1 | Idempotent write path to DB |
| HDE-SEPA001.2 | Canonical byte-compare vs emitter |
| HDE-SEPA001.3 | Grants / DDL least-privilege posture |
| HDE-SEPA001.4 | No secrets/PII in logs |
| HDE-SEPA001.5 | Identity snapshot for services |
| HDE-SEPA001.6 | Persistence evidence indexing |
| HDE-SEPA002 | Error Envelope & Token Set |
| HDE-SEPA002.1 | Error envelope shape & numeric-free body |
| HDE-SEPA002.2 | Error transport headers (writers/errors) |
| HDE-SEPA002.3 | Error token map & casing |
| HDE-SEPA002.4 | Canonical JSON for error envelopes |
| HDE-SEPA002.5 | Reader↔CLI error parity & two-run identity |
| HDE-SEPA002.6 | CLI stderr/stdout discipline & usage exit 64 |
| HDE-SEPA002.7 | Writers/errors headers posture validation |
| HDE-SEPA002.8 | Error-envelope evidence & indexing |
| HDE-SEPA003 | Public Presenter / Emitter |
| HDE-SEPA003.1 | Single shared presenter/emitter symbol |
| HDE-SEPA003.2 | Canonical JSON & non-empty showcompat |
| HDE-SEPA003.3 | Streams discipline for presenter flows |
| HDE-SEPA003.4 | AB↔BA and two-run identity for presenter |
| HDE-SEPA003.5 | Preimage recompute & identity coupling |
| HDE-SEPA003.6 | Presenter evidence indexing |
| HDE-SEPA004 | Internal Ops Surface /internal/version |
| HDE-SEPA004.1 | GET/HEAD 200 parity |
| HDE-SEPA004.2 | Conditionals ignored (never 304) |
| HDE-SEPA004.3 | No-store & no ETag posture |
| HDE-SEPA004.4 | Two-run identity & identity coupling |
| HDE-SEPA004.5 | Internal ops evidence indexing |


The complete 35-unit disposition remains unchanged. No PF09.3 v1.1.4 adoption, alternative mechanics default, new public compatibility surface, public category expansion, PF20/PF30 registration, DB migration/backfill, vendor acquisition, infrastructure change, broad narrative/cache/resolver completion, or HDE-DIST008.1 completion claim is introduced. Required related code may change only where it implements this selected configuration/identity/comparison contract. A whole existing Done task is not reopened by a bounded compatibility check.

## 3. Current-source and inspection record

All PF selections below are controlled Markdown, resolved through the direct-child chain Glow → Core Docs → PFCanon. The verified IDs are Glow 1MZXcC5tKMkI9n8EobkywIj1ifcF6IvZ3, Core Docs 18T84WC_Jxjb75V37_eYcRqn8zOjHYgxu, and PFCanon 1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3. Each selected file was a unique controlled Markdown match in the complete direct-child listing, with its own metadata parent equal to PFCanon. These are runtime evidence bindings, not permanent version pins for future discovery.

| Source | Exact Drive file ID; filename / body version | Inspected governing scope |
| --- | --- | --- |
| PF01-Canon-HDE-Math-Spec | 1ILESkXCDr11Me6WvCBPpebfmQFwEz63p; 1.3.7 / 1.3.7 | Gate ingress, eligibility and identity; §5.2 full mechanics/default; §9.5 M10-G001–M10-G008 |
| PF02-Canon-HDE-Architecture | 1y4JvZKVZR_5J_wynT4p3HtYgX4cRSIB6; 2.4.5 / 2.4.5 | §2.1–2.2 pure core, I/O/application and projection ownership |
| PF03-Reference-Technical-Writing-Best-Practices | 1M_PTWi-ySFs1NWIjFpd9p2IL-vsKbJEA; 1.8.7 / 1.8.7 | Source fidelity, exact facts, scope and truthful evidence language |
| PF05-Canon-HDE-CLI-API-Vendor-Ref | 1P78CNLZhAIYYTHXOAi2aX1HoImo9TuXo; 2.5.2 / 2.5.2 | §4.1.3 complete internal output; §5.1.0 Reader eligibility, production ingress and public boundaries |
| PF09.3-Canon-HDE-Build-Checklist-Separation | 1lgyERodDNPSKIB1xUxXz6r_LlW5syBh2; 1.1.3 / 1.1.3 | Selected HDE-SEPA005 and .1–.5; phase Notes; pinned disposition in approved Specification |
| PF10-Canon-HDE-Build-Notes | 1Zx271D9HazwYTKvjFdxDsPAAO584nbmC; 13.1.2 / 13.1.2 | Addendum Index and inserted Addendum 2.2, timestamp 090826 15:30; C040-01–04 actual publication |
| PF12-Canon-HDE-Schemas-and-Artifacts | 1kDa_pHeZx7zSnjftfBelWBgYXay5zMKk; 2.9.6 / 2.9.5 | §§2.1, 2.9, 4–6, 8.1–8.3, 8.5, 8.14.1; catalog/schema/default/result, complete manifest, external attestation, evidence and projections |
| PF14-Canon-HDE-Mechanics-Guide | 1G6j4L4k0ExSvffp635-msbfV-qUjzjm8; 3.5.6 / 3.5.4 | §§2–3, 6.7, 7.2–7.3; validation/generation, canonical core and result integration |
| PF19-Canon-Glow-QA-Guide | 1AD5u5MU3RUK2K3g3GUPNJetfnEkLBmyy; 3.0.4 / 3.0.3 | §3.4.14 exact-source evidence, attribution and proportionate planning |
| PF27-Canon-Plan-Templates | 1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4; 2.0.5 / 2.0.5 | §12 Audit/class-bound Plan fields, units, boundaries and proof; exact-source posture |
| PF13-Reference-Glow Development Philosophy | 1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j; 1 / 1 | §C four-element dimensions; the approved Card remains the single Strategy Card |
| PF21-Reference-7 Phases of Alchemical Engineering | 1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI; no explicit version | Separation: choose and enforce the necessary boundary; retain later work outside this cut |

Filename/body discrepancies are retained under already approved C040-02–04. Attached older copies and the native PF09.3 v1.1.4 document were not substituted. PF08 was separately resolved as controlled Markdown (1BhLsOTIliAyeP7ZQgHT2uvm2Ym_QmTK7) and its Channels passage checked as doctrinal background; that passage does not establish a complete circuit/substream assignment oracle. No row-by-row doctrinal PASS is claimed.

Workflow sources: selected IA-10 and IA-30, version 090826.2, release GCFPE-20260908.2, in Notion AI Prompts / HDE IA; GCFPE-ASSESS-10 in AI Prompts / HDE Change Flow; current GCFPE Membership and Release Register at the verified Flow Index directory. The complete IA-10 and IA-30 prompt bodies were read. Immutable R1 Authority Register 20260831.1 (libfile_42595a0333f48191b523aa3bf56d11c2, AR-010–013) and Contract Matrix 20260831.1 (libfile_a5ed1529785481919faa99a38921b7b1, GCF-09–11) bind actor/sequence, with current accepted workflow corrections. Their historical repair-status labels are not current execution blockers.

The complete approved Specification was read, including its protected original proposals, approval overlay, exclusions, Card, thirteen requirements and nine criteria. The GitHub recursive tree had 7,042 entries and truncated:false. The inspected head is the #402 HDE-CRD-0001 QA-evidence retention merge; no result from that different change is inherited.

Inspection used repository source and static parsing, not repository execution. Thirty-three retrieved repository file snapshots were checked against their Git blob identities from the pinned tree; all matched exact blob bytes. AGENTS.md was read completely. The repository-wide tree search establishes absence only for the exact governed paths reported below. The file observations are bounded to the named loci; this is not a claim that all 7,042 entries received a code review. No tests, services, generators, CI workflows, live DB query, vendor request or production operation ran. Source-date, tested-candidate and later evidence-storage identities must remain distinct in subsequent work.

## 4. Verified implementation observations

All repository paths in this Audit resolve under [the inspected source commit](https://github.com/amthorn78/glow-hdengine-v2/tree/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f). Function names and exact paths identify the inspected loci.

| Finding | Direct evidence | Observed behavior and practical consequence |
| --- | --- | --- |
| IA040-F01 — Partial catalog | catalog/channels_v1.json | Exactly 36 rows and sorted row IDs exist. Five Gate pairs are non-ascending: 02-14, 05-15, 06-59, 07-31, 09-52. Fourteen substreams are null: 01-08, 02-14, 03-60, 05-15, 07-31, 09-52, 10-20, 10-34, 13-33, 20-34, 21-45, 25-51, 29-46, 42-53. Existing centers arrays are sorted; this alone does not prove every center projection or classification. |
| IA040-F02 — Schema does not enforce adopted catalog | schemas/channels_v1.schema.json; schemas/channels_catalog_v1.schema.json | The owning Channel schema allows null substream and omits ego from its non-null values. Count/shape validation under this schema cannot prove the current PF12 §2.1 contract. Product metadata must survive correction. |
| IA040-F03 — Loader foundation is reusable but incomplete | engine/config/registry_loader.py: load_registry_config, channel and manifest parsing | Closed Gate/center/Channel roster checks, caps/order checks and typed errors exist. JSON parsing collapses duplicate object keys; Gate endpoints are int-coerced and sorted before return; actual owning JSON Schema execution, strict canonical source-byte rejection and complete manifest member hash/size validation are not established by this implementation. Frozen dataclasses contain mutable dictionaries. No active mechanics configuration/result-schema load exists here. |
| IA040-F04 — Required files absent | Complete tree: catalog/magic10_mechanics_v1.json; schemas/magic10_mechanics_v1.schema.json; schemas/magic10_result_v1.schema.json; schemas/magic10_compat_result_v1.schema.json | All four exact authoritative paths are absent. Generated magic10_config output cannot stand in for them. |
| IA040-F05 — Generated projections exist | engine/config/bundles.py; tools/config/artifacts.py; tools/config/generate_config_artifacts.py; tools/generate_registry_report.py | FE/BE bundle schema identities and Product metadata projections can be retained. Current magic10_config projects order/caps/seeds, not the full active mechanics contract. Closed-rails and canonical-serializer calls exist. These generators do not yet prove complete validated prerequisites. The registry report uses ROOT-based source metadata even with an alternate base; candidate/root binding requires repair within the same source-validation work. |
| IA040-F06 — Core is a precomputed-score scaffold | engine/core/core.py: ParticipantState, CoreConfig, compute_core | ParticipantState contains compat_score; compute_core has an optional third config argument and averages precomputed scores. It is not the required four-argument Gate-based canonical computation. Existing core tests target that scaffold. |
| IA040-F07 — Other scoring paths cannot prove full goldens | engine/magic10/calculators.py; engine/compat/compute.py; engine/compat/type_strategy_v0.py; engine/compat/ts_v0.py | Existing category/scaffold computations and UID-hash/viewer-preference scoring do not implement the adopted full Channel-state → signal → category contract. They cannot become the comparator's oracle or substitute for engine.core.core. |
| IA040-F08 — Gate and identity dependency | engine/bodygraph/projection.py, v2_adapter.py, resolver.py, mapped_cache.py; complete tree | Existing BodyGraph flow is reusable context, but the canon-owned engine/bodygraph/gates.py is absent. The inspected projection retains generic Gate material, not a demonstrated shared strict normalizer/mask contract. No complete Gate fingerprint/pair identity path was established. |
| IA040-F09 — Bounded application/public projection gap | engine/compat/compute.py; engine/runtime/public.py; engine/http/compat_handler.py; presenter/reader_v1/emitter.py | Compat currently loses canonical Gate operands into older scoring. Public runtime computes older harmony and emits a harmony category even when passed eligible=false. Canonical Reader serialization/preimage support exists and can be reused. Exact G007/G008 require application eligibility and internal/Reader projection through these owners, without a new emitter or public payload. |
| IA040-F10 — Manifest incomplete for adopted cut | catalog/manifest.json; scripts/cut_release_manifest.py; scripts/release_id_tools.py | Current manifest is v1.0.0 with 15 rows. Twenty-six of the 31 PF12 promoted-path rows are absent from that manifest, and eight promoted files themselves are absent. The cutter refreshes listed rows but does not populate the required promoted roster. Hashing this old manifest cannot prove the v1.1.0 Magic10 release. |
| IA040-F11 — Comparison/readiness missing | Complete tree; PF12 §8.14.1; PF01 §9.5 | tests/fixtures/magic10/v1/goldens.json and tools/bodygraph/check_magic10_gate_readiness.py are absent. A full read-only comparison facility was not established in the inspected loci. No live current-row readiness observation exists for this Epic. |
| IA040-F12 — Evidence infrastructure reusable | tools/evidence/update_evidence_index.py: _run_once, _converge_and_publish; tools/evidence/run_canonical_json_gate.py | The existing canonical updater owns Index, hash sentinel, Machine Mirror, orientation and path-proof generation with staged convergence/check behavior. Canonical JSON gate has a fixed inventory and schema; it cannot be silently extended while retaining contradictory fixed counts. Primary validation evidence must precede indexing and bind identical source bytes. |

The eight absent promoted paths are the four IA040-F04 files plus engine/bodygraph/gates.py, engine/magic10/composite.py, engine/magic10/signals.py, and tools/bodygraph/check_magic10_gate_readiness.py. Existing release members still need exact format/hash/size validation; “present” is not “correct.”

## 5. Requirement-by-requirement disposition

| Requirement | Current versus required behavior | Disposition and implementation consequence | Governing source / decisive evidence |
| --- | --- | --- | --- |
| K040-REQ-001 | Pieces exist, but catalog, active config, core, comparison and proof do not form one validated contract. | GAP — plan all selected subtasks as one integrated dependency sequence, with final documentation and attributable evidence. | Specification §§2,5,11; IA040-F01–12; all AC040 criteria |
| K040-REQ-002 | Approved source ownership and four decided conflicts are available; PF14 still retains incompatible old test instructions. | PROCESS/RECONCILIATION — preserve exact owners, complete C040 register and review history; propose C040-05 without self-approval. No second source or new acceptance registry. | Specification §10.3/approval overlay; PF10 Addendum 2.2; PF14 §6.7; current IA-10/IA-30 |
| K040-REQ-003 | Complete row count exists; five Gate-order counterexamples and fourteen null substreams refute conformance. Full circuit/substream correctness remains unverified. | GAP — exhaustive 36-row correction and provenance-backed classification review, schema/topology/canonical-byte and negative proof. No guessed replacement assignments. | PF12 §§2.1,4,8.1–8.2; PF14 §2; IA040-F01–02 |
| K040-REQ-004 | Current Product fields and bundle identities are reusable. Loader normalization can conceal defective source values; nested mappings are mutable. | PARTIAL — retain Product fields and current FE/BE schema promises; reject duplicates before normalization; preserve ordered category/signal collections and normalize only governed sets. | PF12 §§2.1,2.9,4; bundle code; IA040-F02–05 |
| K040-REQ-005 | Authoritative default and three strict schema files absent; full canonical mechanics not implemented. | GAP — implement the exact adopted default, all 20 signals/three profiles/two Balance operations and both result contracts; execute schema and closure checks. No tuning prerequisite. | PF01 §5.2; PF12 §2.9; IA040-F04,F06–07 |
| K040-REQ-006 | Generated snapshots exist but cannot load or prove one complete immutable release configuration. | GAP — one active canonical configuration per validated release; runtime and FE/BE/report views consume the validated bundle as projections. No fallback or selector. | PF12 §§2.9,5–6,8.14.1; PF14 §3; IA040-F03–05,F10 |
| K040-REQ-007 | Typed loader and generic BodyGraph plumbing exist; strict schemas, deep freezing, shared Gate normalization and result validation are missing. | GAP — load/freeze outside core; enforce exact safe paths and source bytes; inject four explicit arguments; validate pure/internal results at owned boundaries. | PF01 Gate ingress/§5.2; PF12 §2.9; PF02 §2; IA040-F03,F08 |
| K040-REQ-008 | Some unknown-ID errors exist; coercion, duplicate JSON keys, weak manifest validation and partial consumer wiring leave refusal gaps. | GAP — full mutation/refusal matrix, complete-or-fail-closed propagation, zero fallback/partial result and secret-safe public errors. | PF12 §§2.9,4–6; PF05 §5.1.0; IA040-F03,F09–10 |
| K040-REQ-009 | Manifest hashing helpers exist but current closure is insufficient; canonical configuration and Gate-based result identity do not exist. | GAP — distinguish source/configuration digests, immutable config_id, validated manifest/release_id, fingerprint/pair_key and repository commit. Bind changed bytes to the owning adoption/release rules. | PF01 §5.2; PF12 §§2.9,5–6; IA040-F04,F08,F10 |
| K040-REQ-010 | Golden path absent; core and application boundaries cannot produce the full canonical expectations. | GAP WITH NECESSARY DEPENDENCIES — implement canonical kernel plus eligibility/orientation/internal/Reader projection necessary for all eight goldens; exact read-only comparator, deliberate mismatch cases and non-mutation proof. | PF01 §9.5; PF12 §8.14.1; PF14 §§6.7,7.2; IA040-F06–11 |
| K040-REQ-011 | Existing config/core tests cover earlier limited contracts. Shared Gate normalizer and readiness tool absent; no live observations. | GAP — migrate meaningful tests, add complete schema mutation/closure/canonical-byte/identity/comparison corpus and read-only current-row readiness capability. Fixtures do not prove deployed data readiness. | PF19 §3.4.14; PF12/PF14 owning predicates; IA040-F03,F08,F11 |
| K040-REQ-012 | Canonical evidence updater exists; selected new primary evidence and complete release predicate not established. | PARTIAL — reuse/extend actual writers for governed families, synchronize companions in the same implementing PR, and obtain final clean-candidate external attestation separately. Index presence never supplies missing primary proof. | PF12 §§5–6,8.1–8.5,8.14.1; PF14 §§2–3; IA040-F05,F10,F12 |
| K040-REQ-013 | Native requirement/repository identities suffice; legacy evidence metadata remains in existing schemas. | PRESERVE / NO STANDALONE FEATURE — retain exact identities and historical bounded metadata; no new mandatory token system. Carry provenance through implementation/review/QA/closure artifacts. | Specification §5.6; PF19 §3.4.14; PF27 §12; AGENTS.md |

No requirement is silently deferred. “GAP” is a static source finding, not FAIL_BEHAVIOR from an executed test. “PRESERVE” does not mean an unrelated historical acceptance is re-certified.

## 6. Feasibility and necessary dependency boundary

The design dependency is: corrected catalog and strict default/result contracts → verified immutable bundle and Gate ingress → canonical pure mechanics/identity → bounded internal and Reader projection → complete exact read-only comparison → coherent release/proof/documentation. This is a required implementation consequence of K040-REQ-010 and the approved Specification §1.3, §6.2 and §10, not a new Product objective.

The kernel must live in engine.core.core, using canon-owned Gate/composite/signal/reducer homes. The full golden collection includes kernel fixtures and public/application identity cases. G001/G002 prove all 36 neutral states and all ten results; G002 also exercises both Balance operations; G003 isolates equilibrium ownership/swap behavior; G004 the exact mixed Gate pair; G005 identity independence; G006 all required inclusive-high boundaries; G007 valid self/inconsistent same-identity behavior with no forbidden core/cache/router/pair-key work; G008 distinct equal-mask identity, orientation, complete internal result and Reader preimage. The comparator must call actual canonical functions, compare the complete prescribed output fields/bytes, and fail when members or expectations are omitted.

The minimal application dependency performs eligibility, canonical-person orientation and schema-valid projections once around the core and uses the existing Reader emitter. It does not authorize a second harness-only implementation. It also does not authorize rewriting all vendor/DB/HTTP/resolver/cache/narrative behavior to claim end-to-end platform completion. Existing consumers of changed internal APIs need compatibility or refusal checks; no successful path in the selected contract may retain UID/preference rescoring. Detailed PR inspection must identify affected callers and keep each edit inside that contract.

Full release membership is required even for unchanged listed members. Adding a member to the manifest does not reopen its whole historical task, but its exact format/hash/size must validate. Manifest correctness and whole-platform functional completeness are separate claims; neither substitutes for the other.

Implementation may proceed only through later approved work units. If detailed source inspection shows a required golden or immutable-consumption boundary cannot be satisfied without an incompatible public promise, new persistence migration or wider approved-scope change, the affected unit stops and returns exact evidence to this IA and Isis/Thoth under the existing Specification correction route. It must not weaken the golden, skip a promoted member or silently absorb that wider work.

## 7. Validation, evidence and risk assessment

| Concern | Required proof and failure boundary | Owner / risk disposition |
| --- | --- | --- |
| Schema and topology | Execute owning schemas with an available validator; strict duplicate-key handling, raw type rejection including booleans/floats, canonical bytes and exhaustive 36-row identity/classification/topology checks. Mutations must include unknown, missing, extra, duplicate, malformed and valid controls. | Implementing PR sessions; all-row circuit/substream provenance remains an implementation input to verify, not an asserted current oracle. If a canonical assignment cannot be sourced, surface the exact row to the Canon owner before changing it. |
| Immutability and source binding | Attempt nested mutation; swapped source/root, wrong digest/size, unsafe/symlink escape, stale derived artifact, incomplete manifest and multiple config selection must refuse. Read one bound byte set, freeze only after successful validation; no successful partial publication. | Loader/generator owners; high consequence because silent normalization and hash-only checks can appear valid. |
| Math and identity | Migrate existing core tests; independent expected values from the full governed goldens, full result equality, AB/BA and repeated runs, identifier independence, boundary arithmetic, eligibility and equal-mask distinctions. | Canonical core and application owners; no second scorer used as the oracle. |
| Read-only behavior | Compare before/after tracked/config/source identities and use write-denial/instrumentation where feasible. Golden checking cannot update expected outputs or activate config. Readiness tests deny writes/vendor acquisition. | Comparison/readiness implementers; fixture data and live current rows explicitly distinguished. |
| Evidence correctness | Primary schema/domain/topology/set/canonical reports share source bindings; index/mirror/path proofs and hashes generated by actual writers in same change. Fixed canonical-gate inventory must be reconciled with its owning schema/tests, not silently widened. | Evidence writer owner; no generic closure report or unsupported green aggregation. |
| Release | Complete promoted membership, correct exact bytes and clean candidate; owning cutter and recompute/checks; external current attestation created and verified against unchanged clean source after final source changes. | Authorized PR/release writer; no repository evidence feedback into identity or current relabel of historical evidence. |
| Public/consumer regression | Existing numeric-free Reader shape, no second emitter, no scoring from Product metadata/viewer identity, and governed secret-safe refusal. | Bounded consumer integration owner; live deployment behavior remains unobserved. |

No Ops mutation is demonstrated necessary for authoring or closed-rails implementation. Current-row readiness capability is selected; production readiness, vendor fetch/backfill and deployment are not. A later live run requires its actual selected QA/Ops task, target/access and operator evidence. No such task or attempt is fabricated here.

## 8. Acceptance coverage and current limits

| Criterion | Audit conclusion and required planning coverage |
| --- | --- |
| AC040-01 | All 13 requirements and 35 source dispositions accounted for; four actual decisions preserved; C040-05 proposed. Review remains independent. |
| AC040-02 | Counterexamples established; exhaustive catalog/schema/classification and FE/BE compatibility work required. |
| AC040-03 | Default/result contracts absent; exact full contract implementation required. |
| AC040-04 | Loader partial; deep immutability/schema/hash/source/refusal work required. |
| AC040-05 | Existing manifest identity insufficient; complete configuration/source/release coupling required. |
| AC040-06 | Full comparison absent; all eight goldens and canonical dependencies required without mutation. |
| AC040-07 | Shared Gate/readiness capability absent; fixture and later authorized live claims separated. |
| AC040-08 | Reusable evidence infrastructure identified; selected primary proof and companions must be produced together. |
| AC040-09 | Bounded public/internal regression and exact native decision attribution required; no inherited CRD waiver or acceptance. |

Remaining unknowns are execution results, deployed data/configuration, exhaustive doctrinal row correctness, final caller deltas from detailed per-PR inspection, actual candidate/PR/CI lineage, and later QA selection. They are not represented as successes or as invented approval gates. Final per-file plans belong to dedicated PR sessions. An indispensable source or compatibility conflict found there must be resolved before its affected mutation.

## 9. Strategy consistency

The approved Specification §4 is the single Card. All its named dimensions remain unchanged:

| Key | Audit assessment against the existing Card dimensions |
| --- | --- |
| outcome_fire | Outcome/success/scope require the complete selected contract, not file presence. Kernel and exact comparison are necessary proof dependencies; all 29 exclusions remain. |
| surface_water | Single surface/promise/minimal contract require existing FE/BE metadata compatibility and the Reader's numeric-free promise. Bounded projections share canonical results rather than rescore. |
| boundary_air | Contract/evolution/data require one explicitly injected immutable configuration and release, no implicit default, identifiers or mutable handles in math. Initial adopted v1 is implemented as specified; no arbitrary coexistence/tuning scheme is invented. |
| stewardship_earth | Ownership/phase/safety require same-IA continuity, independent Isis review, actual evidence and complete-release rollback. The Card's original SPECIFICATION_PENDING author-stage wording is preserved as history under its v1.1 approval overlay, not mistaken for current status. |

## 10. CANON_CONFLICT_REGISTER

The complete original Specification proposals are preserved here. Their historical proposed wording is governed by the actual approval records immediately below.

| Proposal | Exact conflict and source binding | Proposed decision for Thoth | Consequence and later drainage |
| --- | --- | --- | --- |
| C040-01 — PF09 phase Notes versus explicit statuses | Complete pinned PF09.3 v1.1.3 disposition preserved in the kickoff: Notes describe HDE-SEPA003/HDE-SEPA004 as “extracted non-done task rows”; both tasks and all their subtasks explicitly say Done | Retain the explicit Done statuses and the PO-selected exclusion. Treat the contradictory Notes as a documentation inconsistency; correct the phase Notes to agree with the governed disposition without reopening, reaccepting or silently changing any row. Thoth may approve this resolution or provide its precise replacement. | Preserve the pinned kickoff unchanged. The governed PF09 source owner applies the approved clarification to the appropriate current Canon through later drainage; this does not adopt v1.1.4 for this Epic. |
| C040-02 — PF12 version identity mismatch | Controlled Markdown file `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`, Drive ID `1kDa_pHeZx7zSnjftfBelWBgYXay5zMKk`; §0.1 declares v2.9.5 | Retain the exact retrieved content and both identity labels for present traceability. Have the source owner establish the intended document version from its actual revision history, then align the filename and control header without introducing substantive changes by inference. No choice between v2.9.5 and v2.9.6 is fabricated here. Thoth must approve or change this bounded resolution. | IA Plan retains the verification/drainage responsibility. PF12's governed maintainer owns the approved version-control correction; any discovered substantive conflict requires its own explicit ADR resolution before dependent action. |
| C040-03 — PF14 version identity mismatch | Controlled Markdown file `PF14-Canon-HDE-Mechanics-Guide-v3.5.6.md`, Drive ID `1G6j4L4k0ExSvffp635-msbfV-qUjzjm8`; §0.1 declares v3.5.4 | Preserve exact retrieved content and both labels; establish the intended revision through the source owner's actual history before aligning filename and header. Do not assume two intervening revisions exist or introduce their supposed content. Thoth must approve or change this resolution. | PF14's governed maintainer owns later approved metadata drainage. No mechanics implementation or changed authority follows solely from the filename. |
| C040-04 — PF19 version identity mismatch | Controlled Markdown file `PF19-Canon-Glow-QA-Guide-v3.0.4.md`, Drive ID `1AD5u5MU3RUK2K3g3GUPNJetfnEkLBmyy`; §0.1 declares v3.0.3 | Preserve exact retrieved content and both labels; have the source owner verify the intended version, then align document-control metadata without inferring changed QA requirements. Thoth must approve or change this resolution. | PF19's governed maintainer owns later approved metadata drainage. QA criteria and actual outcomes remain unchanged unless a substantive change is separately established and decided. |


| ID | Classification; affected requirements | Alternatives and interim treatment | Actual status, reviewer, reviewed artifact and decision | Rationale, remaining risk and permanent drainage |
| --- | --- | --- | --- | --- |
| C040-01 | CANON_RECONCILIATION; K040-REQ-001, 002, 013; AC040-01 | Alternatives: follow contradictory phase Notes and reopen work, or preserve explicit Done disposition. Interim: preserve all 29 exclusions and pinned 1.1.3. | APPROVED; Thoth-17; HDE-EPIC040-SPECIFICATION v1.0, represented by approved v1.1 libfile_12bab860949c8191881510875f051460; 2026-09-08T13:23:24Z; approved exactly as proposed. | Explicit PO selection and row statuses control this scope. Risk: future readers misread Notes. Governed PF09 source owner clarifies current phase Notes; no reacceptance or row mutation here. |
| C040-02 | CANON_RECONCILIATION; K040-REQ-002, 005–012 | Alternatives: guess a version or verify history. Interim: use exact retrieved PF12 content with both labels. | APPROVED; same Thoth-17 decision, reviewed predecessor and time as C040-01. | No inferred substantive revisions. PF12 governed maintainer verifies actual history, then aligns filename/control metadata; intended version remains unproven. |
| C040-03 | CANON_RECONCILIATION; K040-REQ-002, 006–012 | Alternatives: infer missing revisions or verify history. Interim: preserve PF14 3.5.6 filename / 3.5.4 body and exact clauses. | APPROVED; same Thoth-17 decision, reviewed predecessor and time as C040-01. | Metadata cannot invent mechanics authority. PF14 governed maintainer owns bounded history verification and metadata drainage; no intended version inferred. |
| C040-04 | CANON_RECONCILIATION; K040-REQ-002, 011–013 | Alternatives: infer changed QA policy or verify history. Interim: preserve PF19 3.0.4 filename / 3.0.3 body and exact clauses. | APPROVED; same Thoth-17 decision, reviewed predecessor and time as C040-01. | QA outcomes and criteria do not change from filename alone. PF19 governed maintainer verifies history and aligns metadata; intended version remains unproven. |

Publication history for C040-01–04: current PF10 v13.1.2, exact file 1Zx271D9HazwYTKvjFdxDsPAAO584nbmC, modified 2026-09-08T15:44:01Z, contains both the Addendum Index entry and inserted Addendum 2.2 “Canonize HDE-EPIC040 source-conflict ADR decisions,” timestamp 090826 15:30. The inserted text identifies this exact Specification, Thoth-17 and approval time, and says the four bounded decisions need no repeated Thoth decision absent materially different evidence. Publication is verified; permanent PF09/PF12/PF14/PF19 drainage is still outstanding and non-gating. Do not recreate this matching addendum batch. No rejected entries were present in the supplied register.

### C040-05 — PF14 retains superseded precomputed-score test obligations

- Classification: CANON_RECONCILIATION; a newly evidenced editorial/normative overlap, not a proposed change to the adopted mathematics.
- Exact sources: current PF14 file 1G6j4L4k0ExSvffp635-msbfV-qUjzjm8, filename v3.5.6 / body v3.5.4, §6.7. Its opening Scope explicitly supersedes the precomputed-score scaffold; the first AB↔BA/determinism paragraphs require the four-argument Gate-based compute_core and complete magic10_result.v1. Later in the same section, paragraphs beginning “AB↔BA behavior tests live under” and “Determinism and JSON-compatibility tests live under” still require compat_score/CoreConfig, three-argument calls and custom band_priority. PF01 v1.3.7 §5.2 and PF02 v2.4.5 §2.1–2.2 independently support the Gate-based pure core.
- Repository evidence: engine/core/core.py and the three tests/core/test_engine_core_* files at the audited commit still implement the older scaffold. This demonstrates why the retained instructions could perpetuate the wrong contract; it is not a test execution result.
- Conflict statement: both test passages retain MUST language while prescribing incompatible inputs and outputs. The explicit supersession supplies a safe present reading, but the unlabelled older text remains misleading.
- Affected obligations: K040-REQ-002, 005, 007, 009–011; AC040-04, 05, 06, 08.
- Alternatives: (A) remove or clearly mark the old three-argument/precomputed-score test passages as historical while preserving the current contract; (B) retain them unchanged and rely on the opening supersession; (C) restore the old scaffold, which conflicts with the approved requirement and is not recommended.
- Proposed disposition: A. Keep the current exact four-argument contract and required Gate-based tests. Drain only the contradictory legacy passages; preserve the separate HDE-DIST008.1 evidence-wiring boundary and source history.
- Interim treatment: the explicit current supersession and PF01/PF02 control planned implementation. Do not keep a second calculator or optional scoring config to satisfy the old passage.
- Unresolved risk: another implementer could follow the obsolete tests; no mathematical uncertainty or approval is inferred.
- Permanent drainage target/owner: PF14 §6.7; governed PF14 maintainer through separately authorized Canon maintenance.
- Status: PROPOSED. Reviewer/session, reviewed artifact/version, decision time and decision rationale: not yet reviewed/decided. Next existing review boundary: Isis-49 in IA-30 for this Plan, under selected 090826.2 “Carried Canon-conflict register.” The Specification-era Thoth decisions and original PO wording remain preserved; this entry receives no invented Thoth decision.
- Decision history: first recorded by this dedicated IA during IA-10; no rejected predecessor, changed approval or PF publication exists for C040-05. If approved, IA-30 owns the standalone PF10 addendum preparation for this new disposition; manual publication remains separate.

## 11. Canon, repository documentation and operational impacts

Permanent Canon values remain single-homed. Implementation evidence may support later PF12/PF14 static-posture updates, PF09 authorized status review and the existing metadata/Notes drainage; this stage performs none. C040-05 is a proposed PF14 editorial reconciliation. No new mathematical design, schema authority, workflow policy or repository ADR number is invented.

A final repository documentation PR is necessary after implementation evidence is known and before independent QA. It must document the delivered configuration loading/failure contract, exact generated/source distinction, comparison/readiness interfaces, compatibility, release verification and complete-release recovery, with actual source and test references. It cannot serve as PF Canon drainage or an Epic closure record. Earlier implementing PRs still update their required local developer notes and evidence companions.

## 12. Provenance and continuation

GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-IA-10-20260908-01.
- Specification: libfile_12bab860949c8191881510875f051460 / HDE-EPIC040-SPECIFICATION / 1.1.
- Components: HDE-SEPA005 and HDE-SEPA005.1–.5; K040-REQ-001–013; AC040-01–09.
- Source: IA-10 — Create Whole-Change Implementation Audit and Plan; AI Prompts / HDE IA; 090826.2; GCFPE-20260908.2; Notion page 3d54590a-05eb-8139-adb8-d20cc7054fb3; retrieved revision 2026-09-08T20:23:24.682Z.
- Register: 3d24590a-05eb-81ce-942a-d994cfca9fa1, selected release GCFPE-20260908.2. Manual alpha permitted; automation remains held.
- Actor/stages: this dedicated whole-change IA; GCF-09 then GCF-10. One combined invocation, no inter-phase Analyzer or audit approval.
- Capture: 2026-09-08T21:52:59Z. Actual human-selected model/reasoning: not observed; recommendations do not prove configuration.
- Prior uses: exact Specification §§1.2 and 1.4 preserve CF-E-20 and CF-E-30 at 090826.1 / GCFPE-20260908.1; CF-E-10 retained through exact kickoff. Their historical versions are not rewritten.
- Results: this complete substantive Audit v1.1, predecessor v1.0 preserved; actual saved reference is returned after persistence. The final separate Plan and proofs follow in the same invocation; no PR/commit or execution attempt is created.
- Downstream reads: complete IA-30 page 3d54590a-05eb-81e7-8e48-cb924a65c39c, 090826.2, revision 2026-09-08T20:23:24.903Z, and selected GCFPE-ASSESS-10 were read to prepare transport; neither destination operation ran.
- Repository persistence: pending, non-gating. Exact docs/changes/GCFPE_PROMPT_PROVENANCE.md was absent from the complete inspected tree; no installed schema/writer procedure was established. An actually authorized future repository writer owns supported persistence after discovery/authorization. No installation work is silently added.
- PF04 anomaly: the Specification carries an unrelated Astra Max stall report. Cause, model attribution and recovery outcome remain unproven; no Epic040 defect or gate is inferred.

Continue immediately to the separate complete EPIC_IMPLEMENTATION_PLAN in this same dedicated IA conversation. Preserve this Audit and its exact reference. The pending Plan goes to continuing Isis-49 via the separate GCFPE-ASSESS-10 transition and IA-30. No IA-20 request is needed for ordinary success.
