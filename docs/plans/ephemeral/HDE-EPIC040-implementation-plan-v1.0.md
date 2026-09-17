# HDE-EPIC040 — EPIC IMPLEMENTATION PLAN

## 1. Identity, lineage and review state

| Field | Value |
| --- | --- |
| artifact_type / plan_type | IMPLEMENTATION_PLAN / EPIC_IMPLEMENTATION_PLAN |
| logical_id / version | HDE-EPIC040-IMPLEMENTATION-PLAN / 1.0 |
| CHANGE_CLASS / CHANGE_ID | EPIC / HDE-EPIC040 |
| change_name / phase | Separation Pass 3 / Separation |
| producer_role / author | Implementation Agent; same dedicated whole-change IA that authored the Audit |
| author_session_ref | This actual IA-10 conversation, dedicated to HDE-EPIC040 by the Product Owner's supplied approved Specification; retain this conversation for IA-40 revisions and later IA work |
| predecessor_ref | None — first complete Plan |
| created_time_utc | 2026-09-08T22:01:38Z |
| state / approval_posture | PLAN_PENDING / Pending Isis review |
| SPECIFICATION_REF | libfile_12bab860949c8191881510875f051460; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-SPECIFICATION v1.1; SPECIFICATION_APPROVED; /Glow HDE 3.0 |
| Specification decision | Thoth-17 APPROVE, 2026-09-08T13:23:24Z; Isis-49 substantive v1.0 unchanged; reviewed predecessor libfile_34fb7876c10081919a7f49306d08e91f, SHA-256 c4b608c159d48160c418863cf4c5b916280004fb6ae0cdc3203eb5997350699a |
| IMPLEMENTATION_AUDIT_REF | libfile_86e45fed0de48191965e232c5ee3aa79; HDE-EPIC040-implementation-audit-v1.1.md; HDE-EPIC040-IMPLEMENTATION-AUDIT v1.1; AUDIT_COMPLETE; /Glow HDE 3.0 |
| Audit creation / ordering | Original v1.0 created 2026-09-08T21:52:59Z, saved and read back before Plan drafting; complete v1.1 created 2026-09-08T22:02:37Z, correcting only the G002/G003 coverage description, saved and read back before final Plan publication |
| upstream formation | libfile_b2399ebf8778819191593946b1cdaa45; HDE-EPIC040-SPECIFICATION-KICKOFF v1.0, KICKOFF_READY; pinned PF09.3 v1.1.3 |
| source observation | amthorn78/glow-hdengine-v2 main at 9065e6f0c01ad82a65c78687cd6c55e26ca33a1f; complete tree e07c4e4297c75fe83e0f286aa1cee46ffca6c62e, 7,042 entries, truncated:false |
| review_session_ref / PLAN_REVIEW_ID | Continuing Isis-49 / not yet produced |
| next_consumer | Isis-49 through GCFPE-ASSESS-10 then IA-30 — Review Whole-Change Implementation Plan |
| execution_posture | MANUAL_PROMPT_EXECUTION; automation held |
| output classification | EPHEMERAL_LIBRARY; complete Markdown in /Glow HDE 3.0 |

This Plan implements the complete selected configuration contract, including the canonical behavior dependencies needed for the exact golden comparison. It is proposed work decomposition, not per-file PR execution planning. No PR, Ops execution, QA selection, approval, merge, deployment, status update or closure has occurred through this artifact.

## 2. Purpose, approved scope and exclusions

Deliver one corrected, strict, immutable and release-bound Magic10 configuration capability with exact deterministic comparison and trustworthy governed evidence. The adopted default is implementation input; discretionary tuning is outside this Plan.

Selected inventory and accountability:

| PF09 unit | Exact source title | Source status | This Specification's disposition |
| --- | --- | --- | --- |
| HDE-SEPA005 | Production Magic10 mechanics configuration contract | Partial | In scope: coherent parent obligation |
| HDE-SEPA005.1 | Corrected canonical 36-Channel catalog | Partial | In scope |
| HDE-SEPA005.2 | Magic10 mechanics schema and default configuration | Partial | In scope |
| HDE-SEPA005.3 | Fail-closed mechanics configuration loader | Not done | In scope |
| HDE-SEPA005.4 | Mechanics configuration identity and deterministic comparison | Not done | In scope |
| HDE-SEPA005.5 | Separation implementation tests and governed artifacts | Not done | In scope |


All 29 Done/context units remain excluded:

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


Every selected PR/Ops unit below belongs to Separation and maps to HDE-SEPA005 and its exact applicable subtasks. The canonical core/application work advances the selected identity/comparison and fail-closed-consumption duties; it does not declare completion of a separate later-phase task. In particular, HDE-DIST008.1's complete mechanics evidence gate remains separately governed.

Other exclusions: no PF09.3 v1.1.4 substitution; public ten-category expansion, numerics or route; second emitter, scorer, configuration authority, evidence index or acceptance database; optional profiles/presets, viewer-controlled scoring, hidden flags, blending or tuning; vendor acquisition, backfill, DB schema/grant migration, production deployment or infrastructure changes; broad resolver/cache/narrative/platform conformance claims; PF20/PF30 registration or board/PF Canon mutations.

## 3. Single approved Strategy Card and assessment

The following is the approved Specification's existing §4 Card, preserved verbatim. Its author-stage phase signal remains protected historical text under the v1.1 approval overlay; the actual current phase is approved Specification → completed Audit → pending Plan.

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


| Existing Card key and source-defined dimensions | Plan application; changed/unchanged assessment |
| --- | --- |
| outcome_fire — outcome, success signal, scope line | Unchanged. Seven PR units and the final candidate verification cover all selected requirements. Golden and kernel dependencies are necessary to make the approved success signal falsifiable; no selected requirement is deferred to a future epic. |
| surface_water — surface statement, promise check, minimal contract phrase | Unchanged. Existing FE/BE identities and Product metadata remain compatible; one canonical result feeds bounded internal/Reader projections. Public shape stays numeric-free and uses the existing emitter. |
| boundary_air — contract name, evolution posture, data posture | Unchanged. Implement the adopted initial configuration, enforce one validated release and injected immutable inputs. No retuning, implicit default or invented coexistence scheme. Incompatible public or persistence evolution returns to the actual scope owner. |
| stewardship_earth — ownership, phase signals, safety note | Intent unchanged; current stage recorded accurately in §1. Same IA prepares/revises; Isis reviews; dedicated PR agents and the selected operator execute only their later authorized tasks. Final source and failures remain attributable; rollback restores a complete compatible prior release. |

## 4. Governing sources and current repository reality

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

The exact substantive Audit §4 supplies twelve inspected findings and §5 the full current/required comparison. The decisive current facts are: catalog Gate-order/null-substream defects; Channel schema permits the old incomplete domain; loader lacks actual schema execution, exact byte/hash closure and deep immutability; four configuration/result files and four other promoted files are absent; engine.core.core consumes precomputed scores; compat/public paths use earlier scoring; full goldens/readiness path are absent; manifest has 15 pre-Magic10 rows; the actual cutter and evidence writers are reusable but need bounded changes.

This Plan does not relabel tests as executed. It relies on source inspection and the Audit's 33 verified Git blob snapshots, with bounded reading of relevant code. Reinspect the material code and installed tools at each PR's actual base; preserve unchanged evidence when valid, and update only affected findings when source changes. The audited SHA is a citation anchor, not a global freeze or mandatory rerun trigger.

## 5. Design and integration contract

1. Correct the complete catalog and owning schema, retaining Product fields and existing bundle promises. Verify circuit/substream assignments row by row from governing source evidence; do not infer them from nulls, labels, example keynotes or model recall. The Audit established concrete defects, not a complete doctrinal assignment oracle. A row that cannot be supported goes to the Canon owner with exact missing evidence before that row is changed.
2. Implement the full initial authoritative mechanics configuration and strict pure/internal result schemas from PF01 §5.2 and PF12 §2.9. Keep the adopted default intact. Generated snapshots/FE/BE bundles remain views.
3. Load and validate exact source bytes and safe release members outside core, enforce schema and cross-source closure, and deep-freeze only a complete valid bundle. Separate lower-level source validation needed to build a candidate from active-release admission; neither API may manufacture an active release or bypass its manifest predicate.
4. Use the single canonical compute_core(member_a, member_b, mechanics_bundle, release_id). Gate normalization, Channel-state composition, signal operations and category reduction use their canonical code homes, with no import-time I/O or hidden config. Canonical serialization uses the existing serializer.
5. Establish eligibility before core/cache/pair identity, and directional orientation outside intrinsic math. Complete internal result and existing Reader projection consume the canonical result once. Existing consumer interfaces affected by these changes must preserve their owning contracts or fail closed; no successful selected path retains UID/preference/legacy rescoring.
6. Compare the entire PF12 golden collection through these production behavior homes. Expected fixtures are governed verification inputs from PF01, not outputs copied from the implementation under test. Comparison never writes expected data, selects config or repairs source bytes.
7. Complete all promoted manifest members through the owning cutter, regenerate only applicable projections/proof through actual writers, and validate the complete candidate. Commit source before generating external exact-source attestation; an attestation cannot feed back into tracked identity.

Intermediate PRs may establish canonical modules and test them against complete valid fixture releases while the final active-release boundary is not yet switched. They must not advertise or activate a partial Magic10 release. The selected final contract has no fallback, hidden activation flag or partial config. Each detailed PR plan must inspect actual deployment/branch coupling before proposing mutations; this Plan grants no deployment permission. If a safe intermediate landing would expose an incomplete active contract, bring the exact dependency to this IA for bounded work-unit correction before execution. Do not solve the dependency by weakening validation or making main falsely green.

## 6. Ordered PR/Ops work-unit map

The IDs below are stable Plan-local work-unit IDs, not already created GitHub PR numbers or external task records. The whole-change IA owns decomposition and later native instructions. Each PR receives its own dedicated PR session after exact Plan approval; each detailed PR plan later requires the Product Owner's actual Proceed invocation.

| Order / unit ID | Lane / phase | Purpose and bounded interface | Exact requirement / PF09 mapping | Dependencies and produced handoff | Owner |
| --- | --- | --- | --- | --- | --- |
| 1 — HDE-EPIC040-PR01 | PR / Separation | Correct catalog and establish strict adopted mechanics/result contracts; preserve Product and FE/BE schema promises. | K040-REQ-003–006, 008, 011–013; HDE-SEPA005.1, .2, .5 | Approved Specification + this approved Plan → source-proven catalog, strict schemas/default, applicable regenerated companions and contract tests. | Dedicated PR01 agent; IA creates PR-10 instructions |
| 2 — HDE-EPIC040-PR02 | PR / Separation | Strict source/manifest validation, immutable typed mechanics bundle and canonical Gate ingress outside core. | K040-REQ-004, 006–009, 011–013; HDE-SEPA005.1, .3, .4, .5 | PR01 reviewed/landed output → validated loader/Gate APIs, fail-closed mutation corpus, source/config identities and immutable bundle. | Dedicated PR02 agent |
| 3 — HDE-EPIC040-PR03 | PR / Separation | Canonical pure Channel-state, signal/category computation and intrinsic identity; migrate existing core tests. | K040-REQ-005, 007, 009–011, 013; HDE-SEPA005.2, .3, .4, .5 | PR01 exact default + PR02 frozen bundle/normalizer → single complete pure result and kernel proof. | Dedicated PR03 agent |
| 4 — HDE-EPIC040-PR04 | PR / Separation | Necessary eligibility, orientation, internal result and existing Reader/consumer projections; no second scoring path. | K040-REQ-004, 006–010, 011, 013; HDE-SEPA005.3, .4, .5 | PR02 party inputs + PR03 canonical result → bounded application integration, schema-valid internal/Reader behavior and no-rescore/refusal regressions. | Dedicated PR04 agent |
| 5 — HDE-EPIC040-PR05 | PR / Separation | Full exact read-only golden comparison and read-only current-row Gate-readiness capability. | K040-REQ-007–011, 013; HDE-SEPA005.3, .4, .5 | PR01–04 source/behavior contracts → full M10-G001–008 fixture/runner, mismatch/non-mutation proof and canon-owned readiness tool. | Dedicated PR05 agent |
| 6 — HDE-EPIC040-PR06 | PR / Separation | Final active-release binding, complete promoted manifest and coherent generated evidence/projections using existing writers. | K040-REQ-001, 006–013; HDE-SEPA005, .2, .3, .4, .5 | PR01–05 reviewed/landed implementation and primary proof → complete candidate release/config binding, coherent governed proof family and final implementation evidence. | Dedicated PR06 agent; canonical cutter/updater remain sole writers |
| 7 — HDE-EPIC040-PR07 | Final repository documentation PR / Separation | Document the actual delivered interfaces, operation, evidence and recovery after implementation results are known; complete before QA. | K040-REQ-001, 002, 006–013; HDE-SEPA005 and .5, documenting .1–.4 | PR01–06 exact delivery/review/evidence lineage → verified repository documentation and actual final source candidate. | IA prepares DOC-10 instructions; dedicated documentation PR agent |
| 8 — HDE-EPIC040-OPS01 | Bounded candidate verification / Separation | Verify unchanged final clean candidate and emit/verify external current release attestation; no production/DB/vendor mutation. | K040-REQ-001, 009, 012, 013; HDE-SEPA005, .4, .5 | Reviewed/merged PR07 plus complete PR01–06 lineage → exact-source verification receipt, external attestation and IA creator review for Isis readiness. | Named operator selected in later OPS-10 task; IA authors task and reviews receipt through OPS-30 |

All units also preserve K040-REQ-002 and 013 source/decision attribution. Order is dependency order, not a schedule or authority to dispatch. No actual PR links, commits, operator identity, task receipts or execution results exist yet. Each unit's final exact interfaces/files are resolved in its dedicated detailed Plan, within the bounds below.

## 7. Unit scope, acceptance, environment and recovery

### HDE-EPIC040-PR01 — Catalog and strict contracts

**Inputs and loci.** Approved Specification §§5.2–5.3; Audit IA040-F01–04; current PF12 §§2.1/2.9/4 and PF01 §5.2. Existing catalog/channels_v1.json and schemas/channels_v1.schema.json are the owning catalog surfaces. Add the four absent canon-owned configuration/result paths identified in the Audit. Check existing FE/BE schema definitions and generated consumers before changing a classification enum.

**Work.** Correct every circuit/substream assignment with a complete 36-row source/provenance check, ascending Gate pairs, endpoint-center projection, row uniqueness/order and schema-declared sets. Preserve primary_domain/domains/flags as non-scoring metadata. Implement exact initial default, all profiles/signals/Balance operations, source-path/hash bindings and strict pure/internal schemas. Existing source members are the input to the initial adopted default; do not misclassify its first implementation as discretionary tuning.

**Acceptance/evidence.** Actual schema execution, all-row/domain/topology checks and negative corpus; independent default-map/closure validation; strict missing/extra/duplicate/domain mutations; compatibility tests for existing bundle schema identities and metadata; canonical exact bytes. Preserve actual findings per row and do not claim Human Design classification accuracy from schema enumeration alone. Required changed projections and existing evidence companions are generated in this PR; they are not deferred wholesale to PR06.

**Environment/recovery.** Closed rails, local source/fixtures, no runtime activation or external requests. Invalid source blocks publication of successful generated artifacts. Revert the complete PR change and regenerated companions together before release; never edit generated outputs to hide a failure. If current authoritative evidence cannot decide a classification or a bundle migration is unavoidable, return the exact affected rows/contract to IA and the source/scope owner before that mutation.

### HDE-EPIC040-PR02 — Validated immutable inputs

**Inputs/loci.** PR01 catalog/default/schemas; engine/config/registry_loader.py; canon-owned new engine/bodygraph/gates.py; existing BodyGraph adapter/projection/resolver/cache boundaries where needed to expose the same normalized party data. PF01 §4/§5.2, PF12 §§2.9/4–6, PF14 §3.

**Work.** Enforce duplicate-key rejection, canonical on-disk bytes and actual schema validation before typed construction. Check safe repository-relative paths, resolved-root containment, exact path/hash/size/source closure, all required members and unique config selection. Reject booleans/int coercions and malformed Gate strings under the actual raw ingress contract; detect raw duplicates before normalized set construction. Deep-freeze nested structures. Validate full source closure and supply configuration/source digests without using evidence as input. Active admission requires the completed production manifest; lower-level validation used by the candidate builder never returns a falsely active release.

**Acceptance/evidence.** Positive canonical representations and required rejection classes, tuple/mask/fingerprint identity, same canonical value across accepted Gate representations, nested mutation attempts, wrong-root/hash/schema/member/extra/duplicate/unsafe path and release mismatch; no partially returned bundle or fallback. Source reads and generated source metadata must bind the same root and byte set. Existing tests/config/test_config_loader_unknown_ids_fail_closed.py and test_typed_bundles.py are inspected/migrated as needed, with required validators present rather than a skipped test counted as proof.

**Environment/recovery.** Local fixture release roots; no DB rows or vendor access. Loader failure propagates existing governed classifications without raw payload/secret leakage. Do not globally activate strict production loading before PR06's complete release admission. Revert dependent changes coherently if the interface must change; never make an optional default restore partial success.

### HDE-EPIC040-PR03 — Canonical pure mechanics and identity

**Inputs/loci.** PR02 normalized Gates and immutable bundle; PR01 exact default/result schema. Canonical engine/core/core.py, engine/magic10/composite.py, engine/magic10/signals.py and engine/magic10/calculators.py; current tests/core/test_engine_core_purity.py, test_engine_core_abba.py and test_engine_core_determinism.py.

**Work.** Implement the complete PF01 Channel-state → twenty-signal → ten-category pipeline in the owning modules, including both Balance operations and exact integer rounding/banding. Compute chart fingerprint/pair preimage identity at the prescribed boundary, with no person ID in intrinsic operands. Replace precomputed-score semantics in the canonical entrypoint, with four required explicit arguments and no optional CoreConfig scoring fallback. No second transitional calculator is retained as a successful canonical path.

**Acceptance/evidence.** All five Channel states; all category/signal assignments and boundaries; exact G001–G006 expectations at their defined levels; AB/BA full-result equality, equal-mask distinct members, repeated canonical bytes, identity independence and no-mutation/purity tests. Instrument or statically enforce absence of file/network/environment/clock/random/process/mutable-global access, including import time, across core/composite/signal/reducer modules. Expected values come from PF01, not a duplicate implementation of the same algorithm.

**Environment/recovery.** Pure closed-rails tests and complete valid fixture bundle/release. No app/database/vendor work inside core. A formula/source discrepancy is a failure or evidenced Canon conflict, not permission to retune fixtures. Revert the kernel and its callers/tests as a compatible set. Preserve C040-05 for actual Isis disposition; explicit current supersession controls the proposed design.

### HDE-EPIC040-PR04 — Bounded application and consumer integration

**Inputs/loci.** PR02 normalized complete party records and PR03 pure results; engine/compat/compute.py, engine/runtime/public.py, engine/narratives/router.py and presenter/reader_v1/emitter.py. Inspect affected engine/http/compat_handler.py, engine/cli/main.py, adapter/http_reader.py and BodyGraph callers only for the selected contract's interface/refusal dependencies.

**Work.** Validate complete party projections and apply valid-self versus inconsistent-same-ID versus distinct-equal-mask rules before core/cache/pair-key work. Attach directional/internal narrative keys using prescribed total orientation outside math, without rescoring. Project only the existing allowed Reader fields using its existing emitter. Propagate invalid input/configuration through existing governed errors. When existing selected consumers require adaptation to the pure result, wire that adaptation here or the final active admission in PR06; never keep successful legacy UID/preference rescoring for the selected final path.

**Acceptance/evidence.** Full G007/G008 application/internal/Reader behavior, including exact preimages and hashes from PF01; forbidden-call spies for valid self; unequal complete same-ID projections refuse; equal-mask different people remain eligible and intrinsic identity-independent. Validate complete internal result and numeric-free public schema, AB/BA and repeated bytes, non-scoring Product fields, no new public keys/routes/emitter and secret-safe failures. Bounded existing consumer regressions establish compatibility, not end-to-end platform completion.

**Environment/recovery.** Resolved chart fixtures and deterministic narrative stubs where the goldens prescribe them; test doubles do not prove vendor/DB/runtime availability. Production request contracts cannot be replaced with a test-only inline-config interface. No DB schema/grant or cache migration is planned. If a wider incompatible migration is indispensable, return evidence before execution. Restore complete prior compatible application/core interfaces on rollback.

### HDE-EPIC040-PR05 — Comparison and Gate readiness

**Inputs/loci.** PR01–04 canonical behavior and PF01 §9.5 / PF12 §8.14.1. Create the governed tests/fixtures/magic10/v1/goldens.json and tools/bodygraph/check_magic10_gate_readiness.py. A comparison command/helper may be added as a bounded implementation locus chosen in the detailed PR Plan; it is not a new authority or an already installed command.

**Work.** Load the complete eight-member golden collection; validate fixture structure/membership, call actual canonical owners at the correct fixture level, and compare every required expected field/byte. Separate fixtures that directly test kernel state/reduction from resolved-party/application fixtures. Return a failure for absent/duplicate cases, omitted expected fields, wrong config/release identities, genuine mismatch or invalid input. A comparison run has no update-goldens, select-config, activate or repair behavior.

Implement current-row Gate-readiness inspection against the existing read-only resolution/data boundary. Inspect actual current rows only when given an authorized target. Missing/malformed Gates remain findings; no fetch, vendor fallback, write, repair, backfill or replacement data acquisition is allowed.

**Acceptance/evidence.** G001–G008 complete and exact; intentionally remove/corrupt expectations, alter output/identity/input and verify refusal/mismatch; before/after source/config/selection identity plus denied-write instrumentation proves non-mutation. Readiness fixture tests include ready, missing, malformed, duplicate, stale/unresolved cases and attempted write/vendor paths. Report fixture behavior distinctly from any real reachable row observations. No production readiness claim is produced by local fixture proof.

**Environment/recovery.** Closed rails; exact immutable input snapshot; deterministic local fixtures. Preserve prior output/evidence if checking fails; do not overwrite the oracle or active config. Actual future live observation belongs to separately selected QA/Ops work and is not implicitly authorized here.

### HDE-EPIC040-PR06 — Complete release and evidence integration

**Inputs/loci.** PR01–05 complete implementation and primary proof; catalog/manifest.json, scripts/cut_release_manifest.py and existing release-ID tools; tools/generate_registry_report.py, tools/config/generate_config_artifacts.py, tools/config/artifacts.py, engine/config/bundles.py; canonical evidence/JSON-gate writers.

**Work.** Complete final active-release consumption so the one validated mechanics bundle supplies all selected consumers. Use the owning cutter to preserve legitimate existing members and add/refresh exactly the PF12 promoted roster. Validate every member's format and exact bytes, then the finalized manifest before deriving release identity. Use the adopted cut's governed metadata; do not invent current wall-clock manifest values.

Strengthen source-root/digest consistency in existing generators. Produce prerequisite schema/domain/topology/set/canonical evidence before a successful registry report, then current configuration/FE/BE projections. All outputs bind the same validated input bytes. Integrate changes into the actual canonical JSON gate inventory/schema/tests where its current owner permits; if a governed fixed inventory prevents the required new coverage, obtain the exact bounded Canon reconciliation before altering that contract. A frozen old count cannot be silently retained as proof of an expanded input set.

Use tools/evidence/update_evidence_index.py for applicable Human Index, Mirror, orientation, hash and path-proof updates. Do not manually edit generated evidence, invent a generic closure_report, or index verification inputs by implication. This unit reconciles integrated evidence; it does not defer the same-PR companions required of earlier units.

**Acceptance/evidence.** All selected mutations and golden/refusal/compatibility tests on the integrated source; exact full release closure and current config identity; generated view compatibility; complete matching primary evidence and companions, writer check/idempotence, stale/mismatched/non-input-extra refusal. Final candidate source validation uses current installed commands and actual results. An initial attestation may be retained for its actual candidate but is never represented as covering later documentation commits.

**Environment/recovery.** Closed rails and deterministic pins; repository-scoped source/generator mutations only after detailed PR Proceed. No production deployment, config activation in a running service, DB action or PF edit is authorized by the Plan. If generation or publication fails, preserve actual failure and recover through the owning transactional writer/revert procedure; no hand-repaired evidence. Runtime rollback, if later authorized, selects one complete compatible prior code/config/schema/manifest release.

### HDE-EPIC040-PR07 — Final repository documentation

**Inputs/loci.** Actual PR01–06 landed/reviewed lineage, delivered interfaces, validation results and limitations. Discover current README/CHANGELOG/AGENTS/developer/operations documentation loci through DOC-10 and the dedicated documentation PR Plan; do not copy PF owners into a second normative document.

**Work/acceptance.** Document the single active config source, schemas and source binding; loading and governed refusal; config/source/manifest/repository identity distinctions; actual comparison and readiness command usage and limits; FE/BE/internal/public boundaries; generated artifacts versus authoritative inputs; exact verification workflow and complete-release recovery. Link actual tests/evidence and explain unexecuted production/QA claims. Verify examples against the delivered interfaces and required docs checks. Documentation must reflect implementation evidence; unresolved behavior is fixed through the owning implementation unit, not explained away.

**Environment/recovery.** Repository documentation mutation only under its later approved detailed Plan. No PF Canon edits or manual generated-evidence rewrites. Revert incorrect docs as a bounded PR correction. Final documentation must be reviewed/merged before independent QA; its final source commit is the input to OPS01, preventing stale-attestation claims.

### HDE-EPIC040-OPS01 — Final clean-candidate verification

**Why separate.** PF12's current attestation must bind the unchanged final clean source commit/tree. PR07 changes source after implementation evidence is known. A bounded operator verification after final documentation establishes that exact final candidate without embedding a self-referential attestation in tracked source. It is not a deployment or production-change task.

**Task inputs.** Later OPS-10 record must name the exact approved Plan/review, final PR01–07 merged lineage and source commit, selected operator and accessible environment, actual installed validation commands, complete manifest/config identities, and an empty output directory outside the source tree. These action-time values do not exist yet and are not fabricated in this Plan.

**Operation/acceptance.** Under closed rails, establish clean exact source; run the current governed source/manifest checks and build/verify the external release attestation against unchanged source. PF12 §6.2.1 owns exact commands/schema/admission predicates. Receipt binds commands, environment pins, exits, source commit/tree, manifest/config identity, external attestation/inventory and limitations. Return the actual receipt to this IA for creator review via OPS-30, then include it in Isis readiness. Success is exact candidate attestation, not QA PASS or release/deployment permission.

**Safety/recovery.** No source modification, commit, merge, database access, vendor/network request, deployment or service-config mutation. Write only the separately declared empty external evidence destination. Refuse nonempty/symlinked/inside-source targets per the owning builder. Preserve failures and exact outputs; never overwrite or relabel an earlier attestation. A changed final source requires a new correctly bound observation, with earlier evidence preserved. Actual required operator authorization and environment availability are established in the bounded Ops task, not supplied by generic Plan approval.

## 8. Complete requirement-to-delivery and acceptance map

| Requirement | Planned units | Decisive completion evidence |
| --- | --- | --- |
| K040-REQ-001 | PR01–07; OPS01 | Six selected units integrate; all criteria addressed; merged/reviewed lineage, final docs and actual candidate receipt. |
| K040-REQ-002 | Every unit; explicit PR07 and IA review | Single owning source per claim; complete C040 decisions/history; no hidden scope or PF mutation. |
| K040-REQ-003 | PR01, PR02 | Complete 36-row source-backed classification/topology/schema/canonical-byte proof and negative controls. |
| K040-REQ-004 | PR01, PR02, PR04, PR06 | Metadata and FE/BE compatibility; raw duplicate rejection; set/ordered distinctions; no Product-metadata scoring. |
| K040-REQ-005 | PR01, PR03 | Full adopted default and strict schemas; all profiles/signals/Balance operations and exact category results. |
| K040-REQ-006 | PR01, PR02, PR04, PR06 | One complete valid immutable active release config; projections use it without selection or fallback. |
| K040-REQ-007 | PR02–05 | Actual schemas/source closure, immutable injected input and governed Gate/result validation. |
| K040-REQ-008 | PR01, PR02, PR04–06 | Complete invalid-class mutation/refusal corpus; no partial success/fallback; secret-safe public error. |
| K040-REQ-009 | PR02, PR03, PR06; OPS01 | Distinct correct digests/config/fingerprint/pair/manifest/release/git identities with changed-byte and mismatch controls. |
| K040-REQ-010 | PR03–05 | Exact full M10-G001–008 comparison through canonical behavior, deliberate mismatches and non-mutation proof. |
| K040-REQ-011 | PR01–06 | Schema/Gate/canonical/closure/identity/comparison/readiness positive and negative implementation evidence; live facts distinguished. |
| K040-REQ-012 | Each emitting PR; PR06; OPS01 | Actual writer-produced primary proof plus coherent required companions; final external attestation stays separate. |
| K040-REQ-013 | Every unit and later reviews | Native source/test/PR/workflow/evidence identities, attributable decisions and preserved legacy metadata without new token bureaucracy. |

No separate software feature is required for K040-REQ-002 or 013: these constrain every unit and the resulting documentation/evidence. Their underlying source/decision predicates remain mandatory; absence of a new token feature is intentional.

| Acceptance criterion | Delivery/verification allocation |
| --- | --- |
| AC040-01 | Whole Plan coverage, actual Isis review and complete register; all units preserve six selected/29 excluded disposition. |
| AC040-02 | PR01–02 catalog/schema/source-backed classification; PR04/06 consumer and bundle compatibility. |
| AC040-03 | PR01 default/schema closure; PR02 validation; PR03 canonical mechanics. |
| AC040-04 | PR02 immutable admission; PR03 pure injection; PR04/06 refusal propagation and final consumption. |
| AC040-05 | PR02/03 identities; PR06 full manifest; OPS01 exact final clean candidate. |
| AC040-06 | PR03–05 all eight goldens and read-only comparison, full expected-output coverage. |
| AC040-07 | PR02 Gate ingress; PR05 readiness capability; later separately selected live observation only if requested. |
| AC040-08 | PR01–06 actual integrated implementation proof and companions; OPS01 exact-candidate verification; PR07 docs. |
| AC040-09 | PR04/06 bounded public/internal/security regressions; all native decision and evidence attribution. |

## 9. Evidence ownership and integrity

| Governed output / proof | Producer and required relationship | Limits |
| --- | --- | --- |
| catalog schema/domain/topology/set proof | Implementing registry validation job; artifacts/catalog/catalog_schema_validation.log, artifacts/catalog/domain_closure_report.log, artifacts/topology/topology_coherence_report.log, artifacts/canonical/arrays_as_sets_report.log | Each primary binds the actual validated inputs; a row count or registry report is insufficient. |
| Exact canonical-byte comparison | Actual canonical JSON gate/writer; audit/gates/json_gate/canonical/json_gate_compare_log.ndjson | Coordinate any inventory/schema change with its governing contract. Never misstate a fixed older inventory as new complete coverage. |
| Registry projection | tools/generate_registry_report.py → artifacts/registry/registry_report.json | Validated prerequisite evidence first; same source/root/digest bindings. No extra domain_snapshot, registry_checksums or generic closure_report. |
| Configuration views | Existing tools/config generators → artifacts/thresholds/magic10_config.json and band_edges.json; engine/config/bundles.py → artifacts/config_bundles/fe_bundle.json and be_bundle.json | Keep owning schema identities and fields; no active config selection or incidental release/hash metadata extensions. |
| Golden verification input | tests/fixtures/magic10/v1/goldens.json from PF01 exact collection, consumed read-only | Verification input does not become manifest member or Index row by implication. It is not rewritten by comparison. |
| Implementation tests and comparison/readiness observations | Dedicated PR's actual test runs, command outputs and workflow results, with precise source and fixture coverage | Use existing governed family where one applies. A new command/test name is explicitly planned until created; no invented PASS report or universal token roster. |
| Human Index/Mirror/hash/path proof/orientation | tools/evidence/update_evidence_index.py; same implementing PR as changed governed output | Primary proof and companions remain distinct; schema, parity, safe paths, self-record and check-mode rules from PF12 apply. Never manual generated-file edits. |
| Manifest/release identity | scripts/cut_release_manifest.py and current release validation tools | Validate all legitimate/promoted member formats and exact bytes before identity. Evidence, logs, mirrors and external attestation do not become inputs. |
| Final external attestation | OPS01 operator using tools/evidence/build_release_attestation.py, exact schema and clean-candidate predicate | Outside repository, unchanged source, no overwrite. Not historical checked-in evidence relabeled current; not independent QA or deployment. |

Each executing unit records the actual base/head, tested source commit/content, commands/workflows and outcomes, failures and corrections, evidence locations, later storage commit where distinct, and review-time lineage. Later evidence-only SHA movement does not by itself mean behavior must be rerun; changed decisive source or required exact-current attestation does require the appropriate fresh binding. No CI waiver from HDE-CRD-0001 is inherited.

## 10. Cross-cutting safety, migration and recovery

**Data/security.** Governed catalogs and deterministic synthetic fixtures are sufficient for implementation. Gate payloads, credentials, vendor responses and raw chart data are excluded from public diagnostics and indiscriminate logs. Identity is used only at its owning eligibility/orientation boundary. OPS01 does not access live personal rows. Least-privilege live readiness observation, if later selected, remains a separate bounded task.

**Compatibility/migration.** Preserve existing public Reader schema/emitter and FE/BE bundle schema identities; Product fields remain non-scoring. Internal canonical core migration is required and all affected selected callers/tests must migrate coherently. There is no planned DB migration, cache backfill, new public version, alternate profile adoption or customer-facing migration. If actual evidence proves an incompatible external contract change is indispensable, stop that affected unit and return to the real scope/Canon owner; do not absorb it under “integration.”

**Release/rollout.** Repository work establishes an admitted candidate, not deployment. Complete all promoted paths and exact hash/size checks; no partial manifest shortcut. Initial adopted config remains the specified default. Subsequent governed-source/config changes take their actual new immutable config/release/adoption consequences under PF01/PF12; this Plan supplies no future tuning/adoption authority.

**Recovery.** Local invalid inputs produce no successful active bundle/result and cannot repair production source. Generator/index failures use the existing canonical writer's transactional recovery and preserve failure evidence. PR rollback reverts coherent code/config/schema/evidence changes. A later authorized runtime rollback selects one complete compatible prior release; no mixed old/new configuration, schema or code. External attestation failures preserve the original directory/output and produce no current-success claim.

**Environment.** Closed-rails implementation and candidate verification use SAFE_MODE=1, ALLOW_NETWORK=0, LC_ALL=C, LANG=C, TZ=UTC under the governing source. Exact installed dependencies and commands are verified in the detailed unit Plan; dependency-unavailable or skipped validation is reported as tooling/evidence unavailable, not behavior PASS. No vendor/open-rails/production permission is inferred.

## 11. CANON_CONFLICT_REGISTER

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

The complete carried register has five entries: C040-01–04 APPROVED and already published as the verified matching PF10 batch; C040-05 PROPOSED for explicit Isis-49 disposition in IA-30 under the selected current workflow. No item is silently approved, rejected, erased or re-numbered. Permanent Canon maintenance remains separately owned.

## 12. Risks, unresolved decisions and change control

| Item | Current truth / consequence | Resolution owner and boundary |
| --- | --- | --- |
| Plan review | PLAN_PENDING; no unit creation/dispatch is authorized yet. | Isis-49 reviews exact v1.0 and upstream Audit/Specification via IA-30. |
| C040-05 | Newly proposed PF14 reconciliation; current explicit supersession supports planning, but proposal is undecided. | Isis-49 gives explicit disposition at the same Plan review; later PF14 maintainer drains. |
| Full catalog assignment evidence | Static audit proves specific defects, not every corrected classification. | PR01 must establish complete source-backed assignment evidence in detailed planning; missing decisive row evidence returns to governed Canon owner before mutation. No invented row values. |
| Scope-sensitive consumers | Canonical goldens require bounded integration; exact caller deltas need detailed base inspection. | PR04/PR06 and this IA; wider incompatible public/persistence scope returns through Isis/Thoth before action. |
| Canonical JSON gate inventory | Existing writer has a fixed inventory/schema. Required new input coverage cannot be represented with false unchanged counts. | PR06 resolves actual owned inventory/schema extension; a true Canon contract conflict follows the existing register/review path. |
| Final candidate/operator | No final commit, task, operator environment or receipt exists yet. | IA OPS-10 and selected operator establish actual values after final docs, then IA OPS-30 review. These are future unit inputs, not missing Plan lineage. |
| Live readiness/deployment | Not observed or selected; fixture capability does not prove current production rows. | Later specifically selected QA/Ops owner; no backfill/vendor/deployment in this Plan. |
| PF source metadata drainage | C040-01–04 already decided/published; permanent Notes/version alignment remains outstanding. | Named governed PF maintainers; non-gating unless materially different evidence arises. |
| GCFPE repository provenance | Installed procedure not found at audited head. | Later actually authorized repository writer after valid procedure discovery/authorization; preserve current metadata meanwhile, pending non-gating. |
| PF04 anomaly | Unrelated Astra Max stall report remains unresolved. | Existing ecosystem owner; no inferred model causality, Epic040 defect or reason to change scope. |

No Product tuning or discretionary architecture choice is left for an executor to invent. Routine implementation choices stay within the defined interfaces and current Canon. Any required correction to this Plan is a complete same-IA successor with exact predecessor and application report, reviewed by the same Isis; changing approved Specification objectives/exclusions first requires their existing formation owners. No new approval token is created.

## 13. Integration completion and Isis QA-readiness handoff

This Plan's implementation-completion package is the approved Plan/review plus:
- exact ordered PR01–PR07 lineage, actual merged state and scoped PR review outcomes;
- requirement/criterion coverage tied to actual source, implementation tests and governed evidence, with failures/limitations retained;
- coherent current configuration/default/schemas, source digests and complete manifest/release validation;
- PR07 repository documentation verification against actual delivered interfaces;
- OPS01 exact final clean-source receipt, external attestation/verification and this IA's creator-review decision;
- complete C040 register with actual decisions/publication/drainage posture, remaining true prerequisites, and preserved prompt-use lineage.

Isis continues through the owning QA-readiness operation (QA-10) to audit actual implementation, compare history, triage findings and establish readiness before QA Guide creation. This Plan does not create a QA Plan, select tasks, choose ALL, count a QA attempt, approve QA or declare PASS. The intended independent QA burden includes every AC040 criterion, full ten-category/domain/golden coverage, decisive rejection and read-only boundaries, actual evidence integrity and source attribution. Any later live readiness task must explicitly distinguish reachable observations from unobserved environments.

Pending informational PF10/PF09 metadata drainage, board administration and prompt-provenance installation are not invented readiness gates. Actual missing implementation, review, final documentation, required candidate receipt or decisive source evidence prevents the affected readiness conclusion. The exact artifact/version and changed-source impact, not a summary alone, controls any later correction.

## 14. Prompt-use provenance and next action

GCFPE_PROMPT_USES:
- usage_id: GCFPE-USE-HDE-EPIC040-IA-10-20260908-01, shared with the preceding Audit and its bounded v1.1 correction in this one invocation.
- Source prompt: IA-10 — Create Whole-Change Implementation Audit and Plan; AI Prompts / HDE IA; 090826.2; GCFPE-20260908.2; page 3d54590a-05eb-8139-adb8-d20cc7054fb3; retrieved revision 2026-09-08T20:23:24.682Z.
- Actor/stages: same dedicated whole-change IA; GCF-09 Audit then GCF-10 Plan; capture 2026-09-08T22:01:38Z.
- Exact Specification: libfile_12bab860949c8191881510875f051460 / HDE-EPIC040-SPECIFICATION / 1.1. Exact Audit: libfile_86e45fed0de48191965e232c5ee3aa79 / HDE-EPIC040-IMPLEMENTATION-AUDIT / 1.1.
- Components and task mappings: §6/§8 map every local PR/Ops unit to K040 requirements and HDE-SEPA005 subtasks. No actual PR numbers/commits or attempts are supplied before they exist.
- Prior uses remain through exact approved Specification §§1.2/1.4 and kickoff: CF-E-10/20/30 author/review history at their actual 090826.1 release; no rewritten chronology.
- Actual human model/reasoning selection: not observed. Header/Analyzer recommendations are not execution configuration evidence.
- Selected register: 3d24590a-05eb-81ce-942a-d994cfca9fa1; release GCFPE-20260908.2; MANUAL_PROMPT_EXECUTION permitted, automation held.
- Downstream read only: complete IA-30 page 3d54590a-05eb-81e7-8e48-cb924a65c39c, 090826.2, retrieved revision 2026-09-08T20:23:24.903Z; GCFPE-ASSESS-10 in AI Prompts / HDE Change Flow. Neither independent review nor Analyzer assessment is claimed executed.
- Results: complete Audit v1.0 saved before Plan drafting; complete successor Audit v1.1 saved before final publication of this Plan v1.0; actual Plan/provider reference and short supporting proof references are returned after save, not invented inside their own bodies.
- Repository writer/capture: each later authorized PR writer captures actual prompt/unit/base/head/result uses in its allowed instructions, detailed Plan and result; Ops captures task/attempt/receipt; QA/review/closure owners retain late uses in their permitted outputs. Only an actually installed authorized writer may persist metadata to the repository's discovered supported schema. docs/changes/GCFPE_PROMPT_PROVENANCE.md was absent at audited head. Pending, non-gating; no prompt bodies, invented installed schema or implicit installation task.

Next: run the separate assessment-only GCFPE-ASSESS-10 transition in this producing IA conversation, then carry its unchanged native IA-30 invocation and this complete Plan to existing Isis-49. The sole native substantive input is IMPLEMENTATION_PLAN_ID; the Plan provides exact retrievable approved Specification and Audit lineage plus complete conflict register. No new Isis session or hidden message is authorized. If Isis denies, return its exact review/redlines to this same IA through Analyzer and IA-40 for a complete successor and application report.

Approval authority: Isis-49. Review decision and time: not yet produced. No PR/Ops dispatch until the exact Plan is approved; later per-PR Proceed and action-specific authority remain separate.

ASK OK?
