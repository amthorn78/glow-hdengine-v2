# HDE-EPIC040 — Separation Pass 3 — Epic Specification

## 1. Artifact Lineage and Approval State

| Field | Value |
| --- | --- |
| artifact_type | `SPECIFICATION` |
| schema_version | `glow-specification/3.0` |
| logical_id | `HDE-EPIC040-SPECIFICATION` |
| version | `1.1` |
| CHANGE_CLASS | `EPIC` |
| CHANGE_ID | `HDE-EPIC040` |
| change_name | Separation Pass 3 |
| substantive_author | Isis |
| producer_role | Thoth — Head of Development; approval decision owner and approved-representation publisher |
| substantive_author_role | Isis — Lead Developer and Specification author; substantive version 1.0 unchanged |
| author_session_ref | Isis-49 — Product Owner-selected continuing author of the reviewed HDE-EPIC040 Specification v1.0 |
| created_date_utc | 2026-09-08 |
| state | `SPECIFICATION_APPROVED` |
| approval_posture | `APPROVED` |
| predecessor_ref | `libfile_34fb7876c10081919a7f49306d08e91f`; `HDE-EPIC040-specification-v1.0.md`; logical ID `HDE-EPIC040-SPECIFICATION`, version `1.0`, `SPECIFICATION_PENDING`; exact reviewed substantive predecessor |
| review_session_ref | Thoth-17 — this actual continuing conversation, bound to HDE-EPIC040 by this first CF-E-30 review; all Specification rereviews return here |
| approval_decision | `APPROVE` — Thoth, Head of Development |
| approval_time_utc | 2026-09-08T13:23:24Z |
| reviewed_predecessor_sha256 | `c4b608c159d48160c418863cf4c5b916280004fb6ae0cdc3203eb5997350699a` |
| publication_delta | Section 1 approval/lineage metadata only; Sections 2–13 unchanged except terminal `ASK OK?` becomes `ASK OK.` |
| KICKOFF_HANDOFF_ID | `libfile_b2399ebf8778819191593946b1cdaa45` |
| kickoff_identity | `HDE-EPIC040-SPECIFICATION-KICKOFF`, version `1.0`, `SPECIFICATION_KICKOFF`, `glow-kickoff/3.0`, `KICKOFF_READY`, producer Master Scrum |
| kickoff_file | `HDE-EPIC040-specification-kickoff-handoff-v1.0.md`, `/Glow HDE 3.0` |
| source_inventory | `PF09.3-Canon-HDE-Build-Checklist-Separation`, selected runtime baseline `v1.1.3`, Status Canon, Phase Separation |
| source_disposition | 35 units: 6 selected planned-work units and 29 existing Done/context units |
| native_next_consumer | IA-10 — Create Whole-Change Implementation Audit and Plan; dedicated whole-change Implementation Agent, reached through GCFPE-ASSESS-10 middleware |

The complete kickoff is the sole native formation input. Its separate creation proof is audit-only. No raw inventory replacement, Implementation Plan, PF20 entry, PF30 entry, separate PO approval object, or prior Epic's acceptance is used as Specification authority. The Product Owner's explicit instruction to proceed in this conversation establishes the continuing Isis author context; no platform session identifier is invented. This continuity instruction changes neither technical scope nor Thoth's independent decision.

### 1.1 Source-use record

The kickoff was read completely, including its 35-unit disposition, thirteen requirement labels, Strategy Card, exclusions and unresolved source facts. PF09.3 v1.1.4 was not substituted, merged or used to expand scope. The complete PF13 and PF21 sources were read for philosophy; the complete relevant technical sections listed below were inspected for their owning claims. Controlled Markdown was resolved in `Glow / Core Docs / PFCanon`; source copies attached earlier to the conversation were not silently treated as current versions.

These are execution-source identities, not additional reusable policy or version pins for future discovery:

| Source title | Retrieved file identity and filename version | Declared body version | Content used |
| --- | --- | --- | --- |
| PF13-Reference-Glow Development Philosophy | `1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j`; v1 | v1 | Complete philosophy and four-element Card dimensions |
| PF21-Reference-7 Phases of Alchemical Engineering | `1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI`; no version suffix | No explicit version | Complete reference; Separation meaning |
| PF03-Reference-Technical-Writing-Best-Practices | `1M_PTWi-ySFs1NWIjFpd9p2IL-vsKbJEA`; v1.8.7 | v1.8.7 | Complete editorial reference |
| PF01-Canon-HDE-Math-Spec | `1ILESkXCDr11Me6WvCBPpebfmQFwEz63p`; v1.3.7 | v1.3.7 | Gate ingress and eligibility boundary; §5 mechanics, configuration, identity, bands and release coupling |
| PF02-Canon-HDE-Architecture | `1y4JvZKVZR_5J_wynT4p3HtYgX4cRSIB6`; v2.4.5 | v2.4.5 | Scope and pure Engine Core versus I/O, configuration and projection boundaries |
| PF05-Canon-HDE-CLI-API-Vendor-Ref | `1P78CNLZhAIYYTHXOAi2aX1HoImo9TuXo`; v2.5.2 | v2.5.2 | Magic10 Reader/internal failure and public/private transport boundaries |
| PF12-Canon-HDE-Schemas-and-Artifacts | `1kDa_pHeZx7zSnjftfBelWBgYXay5zMKk`; v2.9.6 | v2.9.5 | §§2.1, 2.9, 6, 8.1 and 8.14.1: catalog, authoritative configuration, result schemas, promoted release inputs and projection/golden boundaries |
| PF14-Canon-HDE-Mechanics-Guide | `1G6j4L4k0ExSvffp635-msbfV-qUjzjm8`; v3.5.6 | v3.5.4 | Programmatic configuration, typed bundles, canonical generation and evidence responsibilities |
| PF19-Canon-Glow-QA-Guide | `1AD5u5MU3RUK2K3g3GUPNJetfnEkLBmyy`; v3.0.4 | v3.0.3 | §3.4.14 exact-source criteria, evidence families and planning tiering |
| PF27-Canon-Plan-Templates | `1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4`; v2.0.5 | v2.0.5 | Exact-source evidence, legacy-token posture, distinct decision states and substantive-change attribution |

PF12, PF14 and PF19 have filename/body-version discrepancies. Both values above are retained; no corrected header or successor content is inferred. The actual retrieved content supplies the cited technical clauses. These metadata discrepancies do not by themselves establish a conflicting technical rule or authorize a PF edit. Under the Product Owner's additional direction during authoring, every identified Canon document conflict requires an ADR proposal carried into the Implementation Plan for Thoth to approve or change and for later Canon drainage. Section 10.3 records the present proposals; no decision is presumed from their inclusion.

Workflow authority is the selected GCFPE release and the locked R1 actor/artifact contracts, not historical implementation-status labels in the R1 audit. Consulted R1 records: `Canonical Change Flow Authority Register`, version `20260831.1`, `libfile_42595a0333f48191b523aa3bf56d11c2`, AR-004–AR-008; and `Canonical Change Flow Contract Matrix`, version `20260831.1`, `libfile_a5ed1529785481919faa99a38921b7b1`, complete GCF-03/GCF-04 rows, both in `/Glow HDE 3.0`. Current selected CF-E-20 and CF-E-30 are runtime version `090826.1`, ecosystem `GCFPE-20260908.1`. Automation remains inactive during this PO-initiated manual alpha use.

### 1.2 GCFPE_PROMPT_USES

- `usage_id`: `GCFPE-USE-HDE-EPIC040-CF-E-20-20260908-01`.
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`.
- `specification_ref_version`: `HDE-EPIC040-SPECIFICATION / 1.0`; its actual saved provider reference is returned after persistence, not invented within its own body.
- `component_requirement_ids`: `HDE-SEPA005`, `HDE-SEPA005.1`, `HDE-SEPA005.2`, `HDE-SEPA005.3`, `HDE-SEPA005.4`, `HDE-SEPA005.5`; `K040-REQ-001` through `K040-REQ-013`.
- `ecosystem_release`: `GCFPE-20260908.1`.
- `prompt_identity`: `CF-E-20 — Create Epic Specification`.
- `prompt_version`: `090826.1`.
- `prompt_directory`: `AI Prompts / HDE Change Flow`.
- `prompt_notion_page_id`: `3d54590a-05eb-8113-adfd-f08c48249c14`.
- `retrieved_revision`: Notion `page_last_edited_at` `2026-09-08T09:07:05.449Z`; complete selected prompt read.
- `role_stage`: Isis / Specification authoring / GCF-03.
- `capture_time_utc`: `2026-09-08T12:38:27Z`.
- `actual_model`: Unknown as an exact model-configuration evidence fact; no model-picker setting is inferred from a recommendation.
- `prior_usage`: Preserve `GCFPE-USE-HDE-EPIC040-CF-E-10-20260908-01` exactly through the complete kickoff's Prompt-Use Provenance section. Its pending Specification reference remains historical capture truth. The preceding Analyzer result in this conversation remains assessment-only, not approval or worker-configuration proof.
- `result_artifact`: `HDE-EPIC040-specification-v1.0.md`; no PR or implementation commit is produced by this authoring operation.
- `repository_persistence`: Pending, non-gating. The exact `docs/changes/GCFPE_PROMPT_PROVENANCE.md` path was absent from the complete inspected tracked tree. No installed procedure, schema or authorized repository writer was established. A later separately authorized repository writer owns any supported persistence; this stage preserves usage here without inventing an installation task.

CF-E-30 was read to prepare the next package. That read is not evidence that Thoth review ran.

### 1.3 Embedded Thoth decision — CF-E-30

**Decision: APPROVE.** Thoth-17 approves the exact Isis-authored substantive Specification v1.0 identified above. This v1.1 is its complete approved representation, not a substantive revision. The first review binds this actual continuing Thoth conversation for HDE-EPIC040; the separate HDE-CRD-0001 review does not supply this Epic's approval or continuity by itself. Isis-49 remains the substantive author.

All thirteen `K040-REQ-*` requirements, the six selected HDE-SEPA005 units, the twenty-nine Done/context exclusions, the complete four-key Strategy Card and its PF13 §C dimensions, constraints, static fact posture, dependencies, nine acceptance criteria, Canon impacts and mandatory IA continuation were reviewed. No material correction remains. No implementation, CI, QA, Ops, current data-readiness, production release, PF09 status or closure result is established by this decision.

**Canon conflict dispositions.** Thoth approves each §10.3 proposal exactly as written, without amendment:

| Proposal | Actual Thoth disposition | Remaining responsibility |
| --- | --- | --- |
| C040-01 | APPROVED AS PROPOSED: retain the explicit Done/context disposition and PO-selected exclusion; clarify the contradictory phase Notes without reopening work | The governed PF09 source owner performs later authorized clarification; the selected PF09.3 v1.1.3 baseline is unchanged |
| C040-02 | APPROVED AS PROPOSED: preserve the retrieved PF12 content and both version labels; verify intended version from actual history before metadata alignment | PF12 source owner verifies and drains the bounded metadata correction |
| C040-03 | APPROVED AS PROPOSED: preserve the retrieved PF14 content and both version labels; verify intended version from actual history before metadata alignment | PF14 source owner verifies and drains the bounded metadata correction |
| C040-04 | APPROVED AS PROPOSED: preserve the retrieved PF19 content and both version labels; verify intended version from actual history before metadata alignment | PF19 source owner verifies and drains the bounded metadata correction |

The complete proposals, exact source bindings, these actual decisions and remaining drainage owners travel into the IA Plan under the already recorded PO direction. Approval of those treatments does not establish an intended version number, prove a Canon edit, allocate repository ADR numbers or authorize a PF write. Any newly demonstrated substantive conflict follows the existing owner/ADR route.

The exact-golden obligation belongs to the selected PF09.3 task. Sections 6, 9 and 10 already require IA to identify the canonical-behavior and complete-release dependencies without replacing the goldens, weakening a manifest predicate, silently expanding scope or deferring a selected requirement. That is a defined audit/planning responsibility, not an approval-decisive missing product choice at this Specification stage. An actual blocker discovered by IA remains a blocker for its affected work and returns to the appropriate owner.

Sections 1.1–1.2 retain author-stage source/use history. The original formation wording preserved in Sections 2–13, including proposed-status wording and the author-stage forward handoff, remains historical author text under CF-E-30's verbatim-preservation rule. This Section 1 decision supplies the current approval, ADR dispositions and next consumer; it does not rewrite that protected substance.

**Continuation:** supply this exact complete approved representation as the sole native `SPECIFICATION_ID` to IA-10 in `AI Prompts / HDE IA`, after the separate GCFPE-ASSESS-10 invocation in this continuing source conversation. The Product Owner selects a dedicated whole-change IA session. IA must complete the whole-change Implementation Audit before its separate complete Implementation Plan in the same IA-10 invocation; Isis-49 then performs the independent Plan review through IA-30. There is no implementation Proceed, QA selection, inherited CRD CI exception or new approval object here.

### 1.4 GCFPE_PROMPT_USES — review capture

- `usage_id`: `GCFPE-USE-HDE-EPIC040-CF-E-30-20260908-01`.
- `change_identity`: `EPIC / HDE-EPIC040 / Separation Pass 3`.
- `reviewed_specification_ref_version`: `libfile_34fb7876c10081919a7f49306d08e91f / HDE-EPIC040-SPECIFICATION / 1.0`.
- `result_identity`: `HDE-EPIC040-SPECIFICATION / 1.1 / SPECIFICATION_APPROVED`; actual saved provider reference is returned after persistence.
- `component_requirement_ids`: `HDE-SEPA005`, `HDE-SEPA005.1`, `HDE-SEPA005.2`, `HDE-SEPA005.3`, `HDE-SEPA005.4`, `HDE-SEPA005.5`; `K040-REQ-001` through `K040-REQ-013`; `AC040-01` through `AC040-09`.
- `ecosystem_release`: `GCFPE-20260908.1`; selected through the current Membership and Release Register and complete prompt catalog.
- `prompt_identity`: `CF-E-30 — Review and Approve Epic Specification`.
- `prompt_version`: `090826.1`.
- `prompt_directory`: `AI Prompts / HDE Change Flow`.
- `prompt_notion_page_id`: `3d54590a-05eb-813b-be71-db5619aa6bf9`.
- `retrieved_revision`: Notion complete page representation as of `2026-09-08T09:07:12.584Z`.
- `role_stage`: Thoth, Head of Development / initial Specification review and approved handoff / GCF-04 and GCF-08.
- `review_session_ref`: Thoth-17 — this continuing conversation, bound for this Epic by this first review.
- `capture_time_utc`: `2026-09-08T13:23:24Z`.
- `actual_model`: Unknown as an exact observed model-configuration fact; no picker setting is inferred from the prompt header or a recommendation.
- `prior_usage`: Preserve the CF-E-20 use in §1.2 and the CF-E-10 use through the exact kickoff reference. No earlier use is rewritten.
- `repository_observation`: `amthorn78/glow-hdengine-v2`, commit `9065e6f0c01ad82a65c78687cd6c55e26ca33a1f`, complete recursive tree `e07c4e4297c75fe83e0f286aa1cee46ffca6c62e`, 7,042 entries, `truncated:false`. Exact `docs/changes/GCFPE_PROMPT_PROVENANCE.md` and a separately named prompt-provenance procedure were not found in this tracked-tree search. No installed writer/schema is inferred.
- `repository_persistence`: Pending, non-gating; a later separately authorized repository writer owns any supported persistence. This review writes no repository record and invents no installation task.
- `downstream_prompt_reads`: Complete selected IA-10 and GCFPE-ASSESS-10 prompts, both `090826.1`, read only to prepare the handoff. Neither operation was executed.

## 2. Change Identity and Class

This is Epic `HDE-EPIC040`, named **Separation Pass 3**, selected by the Product Owner on 2026-09-08. It is not CRD HDE-CRD-0001 and does not inherit that change's approvals, CI exceptions, QA results or closure.

The pinned Separation inventory is Canon with phase status `Not Done`, effective 2026-08-25. Its complete population is five parent tasks and thirty subtasks. The selected scope is exactly:

| PF09 unit | Exact source title | Source status | This Specification's disposition |
| --- | --- | --- | --- |
| HDE-SEPA005 | Production Magic10 mechanics configuration contract | Partial | In scope: coherent parent obligation |
| HDE-SEPA005.1 | Corrected canonical 36-Channel catalog | Partial | In scope |
| HDE-SEPA005.2 | Magic10 mechanics schema and default configuration | Partial | In scope |
| HDE-SEPA005.3 | Fail-closed mechanics configuration loader | Not done | In scope |
| HDE-SEPA005.4 | Mechanics configuration identity and deterministic comparison | Not done | In scope |
| HDE-SEPA005.5 | Separation implementation tests and governed artifacts | Not done | In scope |

Source statuses are transcribed inventory facts, not new assessment results. No row moves to Done through this Specification. The other twenty-nine units are preserved in §6.

## 3. Problem or Planned Capability and Warrant

Glow needs one trustworthy production Magic10 mechanics configuration contract: corrected Channel topology/classification, strict configuration and result schemas, validated immutable inputs, deterministic identity and comparison, and governed evidence that these parts agree. A partial registry and generated configuration views do not establish that contract.

The warrant is the Product Owner-selected, sanitized PF09.3 scope in the complete kickoff. Bounded repository inspection adds concrete feasibility context: a populated Channel catalog and reusable typed registry/bundle machinery exist, but the inspected catalog includes non-ascending Gate arrays and null substreams; the authoritative mechanics configuration and three associated schema paths are absent. These are checked-in-source observations, not executed QA findings. §8 gives exact scope and references.

Separation is the appropriate phase because this Epic selects and makes explicit a single configuration boundary and its proof obligations. It does not reopen exploratory mechanics, promote optional presets, launch new public surfaces, or absorb later integration merely because current Canon describes a larger end-to-end Magic10 capability. The complete selected burden remains code, configuration, tooling, tests and governed artifacts; a document-only declaration cannot satisfy it.

## 4. Desired Outcomes

On completion of the separately authorized implementation and verification lifecycle, the six selected units form a coherent, deterministic configuration capability that later consumers can trust. The catalog, configuration, loader, identities, schemas, comparison results and evidence must agree with their owning Canon. Current partial components may be reused only to the extent that exact evidence supports their required behavior.

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

## 5. In-Scope Requirements

The `K040-REQ-*` labels retain their kickoff meanings. They are local requirement identifiers, not PF09 rows, acceptance tokens or implementation work units. Exact schema fields, formulas, defaults, error bytes and artifact contracts stay single-homed in current Canon; this section states the Epic's obligations against those owners.

### 5.1 Coherent parent contract — HDE-SEPA005

**K040-REQ-001.** Deliver the selected code, configuration, tooling, tests and governed evidence as one coherent implementation burden across all five subtasks. Individual file presence or a partially validated configuration does not satisfy the parent.

**K040-REQ-002.** Bind every technical claim to the current controlling owner by stable document title. Do not create a second mechanics, schema, catalog, artifact, QA, process or acceptance home. The runtime source record in §1 documents what was actually read without rewriting the owners. The additional PO direction requires any Canon document conflict found at any process stage to become an explicit ADR proposal in the Implementation Plan, with Thoth approval or change and a named later Canon-drainage destination. The conflict cannot disappear into a caveat or an assumed resolution.

### 5.2 Corrected canonical catalog — HDE-SEPA005.1

**K040-REQ-003.** Correct all circuit and substream rows, canonical ascending Gate pairs, Center-set projection, schema conformance and row order across the complete canonical 36-Channel catalog. Enforce the governed roster, endpoint and canonical-identity relationships, not just a matching row count.

**K040-REQ-004.** Preserve non-scoring Product metadata and existing FE/BE bundle compatibility while enforcing Channel identity, uniqueness, topology and schema-declared arrays-as-sets behavior. Correcting a topology/classification row does not authorize deleting or repurposing its non-scoring metadata. Ordered collections retain their owning order; raw duplicate Gate input must be rejected, not silently repaired under set-normalization language.

### 5.3 Strict configuration and result contracts — HDE-SEPA005.2

**K040-REQ-005.** Implement the complete twenty-signal map, all required response profiles, the two Balance operations, category/caps closure, exact governed source hashes, governed result schemas and strict mechanics configuration schema. The adopted default is the baseline; optimization, empirical calibration and discretionary tuning are not prerequisites. Exact signal maps, operations, profile values, reducers and domains come from PF01-Canon-HDE-Math-Spec; strict configuration and result shapes come from PF12-Canon-HDE-Schemas-and-Artifacts.

**K040-REQ-006.** Provide one authoritative canonical, schema-valid, manifest-bound and immutable active mechanics configuration per release. Its field shapes, source identities, fixed invariants, tuning limits and pure/internal result distinctions must conform to those owners. Generated configuration evidence and FE/BE bundles remain projections. They cannot become fallbacks or independent formula, source-hash or release authorities.

### 5.4 Fail-closed loader — HDE-SEPA005.3

**K040-REQ-007.** Provide one immutable typed bundle loaded outside Engine Core, with exact source-path/hash closure, governed Gate normalization, result-schema validation and one active configuration per release. The loader must actually enforce the applicable owning schemas and cross-source relationships; typed classes or frozen outer wrappers alone do not prove deep immutability or complete validation.

**K040-REQ-008.** Reject missing, extra, duplicate, malformed, out-of-domain, unresolved, stale, ambiguous, schema-invalid, hash-mismatched and release-incoherent inputs. Refusal must propagate without a successful partial result or fallback to Markdown, tuning candidates, generated snapshots, caller configuration, hidden flags or blended configuration. No secrets, Gate payloads or internal diagnostics may leak through public failure projection. Error classifications remain owned by PF05-Canon-HDE-CLI-API-Vendor-Ref and its governed schemas, not invented here.

### 5.5 Identity and deterministic comparison — HDE-SEPA005.4

**K040-REQ-009.** Implement canonical hashes for the mechanics configuration and referenced source bundle, preserving the governing immutable-configuration and release-identity consequences of changed bytes. Evidence must distinguish configuration identity, source-byte digests, manifest/release identity and repository commit identity. None substitutes for the others.

**K040-REQ-010.** Provide exact golden-output comparison with an explicit read-only guarantee. Comparison cannot select, activate, rewrite or otherwise change production configuration. It exercises the canonical behavior homes and the PF12-governed golden collection, not a second scoring implementation or hand-authored success report. Changed or invalid inputs, wrong identities, incomplete expected-output coverage and genuine mismatches cannot report equality.

### 5.6 Tests and governed artifacts — HDE-SEPA005.5

**K040-REQ-011.** Cover the schema mutation matrix; raw Gate-ingress rejection and canonical normalization; canonical-byte behavior; catalog/caps/threshold closure; deterministic identity and comparison; and the read-only current-row Gate-readiness capability. Both valid inputs and decisive rejection/mismatch/non-mutation cases require evidence. A current-row readiness check must not modify stored rows, acquire vendor data, backfill missing Gates or represent unavailable observations as readiness.

**K040-REQ-012.** Produce and index the applicable governed implementation evidence through the current Human Evidence Index, Machine Mirror, hash, path-proof, manifest and artifact contracts owned by PF12-Canon-HDE-Schemas-and-Artifacts and the applicable evidence/QA homes. Use their actual authorized writers. Keep primary proof distinct from its index, digest and path-proof companions; do not hand-edit generated evidence or invent a new generic evidence family.

**K040-REQ-013.** Use exact PF09, requirement, test, schema, artifact, repository, commit, PR, workflow, evidence and decision identities as applicable. Historical acceptance-token names remain their original optional bounded compatibility metadata. No new default token, exhaustive roster, ceremony, per-step token declaration, token/evidence matrix or replacement universal acceptance database is required when native exact-source identifiers suffice. Preserve still-applicable schema compatibility and the substantive predicates behind any explicit historical claim.

## 6. Exclusions and Non-Goals

### 6.1 Complete preserved Done/context disposition

Every row below is `Done` in the pinned source and excluded from this Epic's planned work. This is a source disposition, not fresh verification or reacceptance.

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

Together with the six §2 rows, this preserves all 35 source units exactly once in the disposition tables. The source Notes call HDE-SEPA003/HDE-SEPA004 extracted non-done rows, despite their explicit Done statuses. The inconsistency is retained in §10; it does not reopen those units.

### 6.2 Other boundaries

- No substitution, merging or inferred additions from PF09.3 v1.1.4 without a new PO source selection.
- No unrelated persistence, error-envelope, presenter, internal-version, narrative, vendor, database, infrastructure or downstream-phase work. Related compatibility checks preserve existing promises; they do not reopen whole Done tasks.
- No second mechanics formula, catalog, schema catalog, configuration source/selector, result authority, evidence index, acceptance database, public surface or presenter/emitter. Implementing the exact canon-owned missing configuration and result-schema paths is not a second authority.
- No alternate profiles, presets, discretionary default retuning, scoring experiments, caller-selected configuration, hidden flags or production blending. No public ten-category expansion or numeric public result.
- No claim that this bounded configuration Epic completes every end-to-end Reader, resolver, intrinsic-cache, narrative or deployment gap described elsewhere in current Canon. Necessary in-scope dependency work must be identified by IA; actual scope conflicts return to their owner, not silently deferred or absorbed.
- No PF20/PF30 creation, update or registration prerequisite. No PF09, PF10, other PF Canon, repository, board or prompt-control mutation in this authoring operation.
- No atomic implementation tasks, file-edit instructions, executable commands, planned PR identities, planned Ops units, QA runbook, credentials or execution receipts in this Specification.
- No implementation, tests, CI, QA, Ops, acceptance, deployment, release readiness, PF09 closure or Epic closure claim from this pending artifact.
- No GCFPE automation activation. The PF04 Astra Max stall remains an unresolved ecosystem anomaly, not evidence about this Epic's software or a reason to change its requirements.

## 7. Constraints and Invariants

The following are requirement-level consequences of the selected source and current owners, not new canonical definitions.

1. **Single source and immutable consumption.** Configuration loading and I/O are outside Engine Core. The core remains pure data-in/data-out: no time, network, file I/O, randomness, environment reads, import-time side effects or caller-selected configuration.
2. **Topology closure.** The governed 36 primary Channel identities are unique and use canonical min-first zero-padded identity, two distinct known Gates and consistent Center-set projection. Canonical ordering and schema-declared set normalization must not erase input defects or change ordered signal/category semantics.
3. **Closed mechanics contract.** Category membership and iteration order, caps-owned input pairs, required profiles and Balance operations retain their owning semantics. The required result is complete-or-fail-closed for an eligible pair, deterministic, identity-independent and AB↔BA-neutral. Exact normative values, maps and rounding stay in PF01 and PF12.
4. **Eligibility and Gate boundary.** Invalid or missing Gate input is not a successful ineligible result. Valid self-pair, same-identity/inconsistent-chart and distinct-person/equal-mask cases remain distinct wherever the selected contract or its verification exercises them. This does not authorize replacing existing public eligibility wiring as an unplanned side task.
5. **Release coupling.** Configuration/source-byte changes have their actual canon-owned configuration, manifest and release consequences. A partial manifest, missing promoted member or mismatched schema cannot be described as a complete production Magic10 release. This Specification neither cuts nor activates a release.
6. **Projection boundaries.** Pure and internal/admin results retain their separate schemas. Narrative augmentation and FE/BE or public projections cannot rescore, reorder or change mechanics identity. Generated snapshots are not production configuration. Internal numbers do not become public values.
7. **Public promise.** The existing Reader remains the single bands-only, numeric-free public compatibility surface. No route, public payload or second presenter is introduced. Applicable errors remain secret-safe under their owning contract.
8. **Deterministic evidence without write feedback.** Golden comparison is read-only and uses canonical behavior. Evidence generation cannot select production configuration or make hosted outcomes an input to authoritative source bytes. Index, mirror, manifest and proof requirements retain their separate meanings and writers.
9. **Layered decisions.** Repository presence, actual CI outcome, implementation validation, authorized QA, acceptance, PF09 status and terminal closure are distinct. No historical result is transferred to a new candidate. Source actually tested, later evidence storage and review-time source remain separately attributable; SHA movement alone is not a new rerun or approval gate.

## 8. Known Verified System Facts

All repository observations below are read-only static inspection of `amthorn78/glow-hdengine-v2` at commit `9065e6f0c01ad82a65c78687cd6c55e26ca33a1f`, observed as `main` on 2026-09-08. The recursive tree was complete (`truncated:false`, 7,042 entries). That SHA is an observation and citation anchor, not a freeze or acceptance gate for later work. No repository code, tests, services, DB operations or generators were executed.

| Fact | Direct inspected evidence | Limited conclusion and consequence |
| --- | --- | --- |
| F040-01 | [main observation](https://api.github.com/repos/amthorn78/glow-hdengine-v2/branches/main); commit above | The observed head is the #402 QA-evidence retention merge, not HDE-EPIC040 implementation. It supplies no Epic040 QA or approval. |
| F040-02 | [Channel catalog](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/catalog/channels_v1.json) | The populated 36-row catalog retains Product metadata. For example, `02-14` stores Gates `[14,2]`; `01-08` has null `substream`. These bytes do not meet the required ascending-Gate/non-null-substream contract. This bounded observation is not a full circuit-classification audit. |
| F040-03 | [Registry loader](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/engine/config/registry_loader.py), complete source | Existing code declares frozen Gate/Channel rosters, endpoint-Center checks, ordered caps inputs, typed records and refusal branches. It loads topology, categories/caps/seeds and a structurally parsed manifest. It does not load the new mechanics bundle or execute the owning mechanics/result schemas in this source. Frozen outer dataclasses contain mutable mappings; their presence alone is not deep-immutability proof. Existing checks are reuse candidates, not PASS evidence. |
| F040-04 | Complete tracked tree plus the loader and generator sources | No exact path was found for `catalog/magic10_mechanics_v1.json`, `schemas/magic10_mechanics_v1.schema.json`, `schemas/magic10_result_v1.schema.json` or `schemas/magic10_compat_result_v1.schema.json`. These paths are PF12-owned requirements, not invented file destinations. The missing files and inspected loader prevent asserting current contract completion. |
| F040-05 | [Configuration artifacts](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/tools/config/artifacts.py); [bundles](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/engine/config/bundles.py), complete sources | Existing tools build a `magic10_config.v1` order/caps/seeds projection, band edges and FE/BE bundles. These are not the PF12 authoritative mechanics configuration. Their existence establishes a compatibility seam to preserve, not validated new-config support. |
| F040-06 | [Engine Core](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/engine/core/core.py); [transitional calculators](https://github.com/amthorn78/glow-hdengine-v2/blob/9065e6f0c01ad82a65c78687cd6c55e26ca33a1f/engine/magic10/calculators.py), complete sources | The inspected core accepts precomputed participant scores/bands; the calculator averages supplied category inputs and reads catalogs at import. Neither inspected file is evidence of the complete required Gate-to-Channel-state-to-signal recipe. A comparison tool cannot treat those transitional results as the new contract's golden authority. This is bounded feasibility context, not authorization for all downstream runtime integration. |
| F040-07 | Complete tracked tree; exact PF12-governed loci | `engine/bodygraph/gates.py`, `tools/bodygraph/check_magic10_gate_readiness.py` and `tests/fixtures/magic10/v1/goldens.json` were not found at those exact paths. The current-row readiness and golden obligations therefore cannot be claimed already delivered from path presence. Alternative behavior under uninspected names remains unverified; IA must assess actual reuse. |
| F040-08 | Complete tracked tree under `docs/changes` and exact procedure-path check | `docs/changes/GCFPE_PROMPT_PROVENANCE.md` was absent; the inspected directory contains audit summary/results, not that installed procedure. Prompt-use persistence remains pending without blocking authoring. |

The source is available for bounded review. No decisive external-service or deployment fact was needed to state the selected configuration requirements. Live data quality, full current repository conformance, applicable future CI and actual implementation/QA outcomes remain unknown. None is fabricated from the sources above.

## 9. Dependencies and Risks

| Dependency or risk | Effect on this Epic | Required treatment and owner |
| --- | --- | --- |
| Corrected catalog before trusted configuration closure | Wrong topology/classification would invalidate downstream maps and source hashes | IA must account for the complete selected catalog obligation and existing validation reuse; no sequence of PRs is prescribed here. |
| Configuration, schemas, source hashes and release membership are coupled | Individually valid files can form an incoherent bundle | Preserve one coherent governed contract. IA must identify actual dependency coverage; candidate evidence must not label a subset a complete release. |
| The promoted Magic10 release roster spans broader runtime components | A full production cut may involve work owned outside this Separation scope | Preserve the exact release invariant and selected phase boundary. IA must identify any concrete blocker or scope conflict for the actual owner; do not invent a partial-release exception, pull all integration into this Epic or silently defer a selected requirement. |
| Existing FE/BE and generated views | Removing non-scoring metadata or repurposing snapshot schemas would break consumers | Preserve existing contracts and use their owning generation boundary. Any demonstrated incompatible change requires actual owner review before execution. |
| Transitional scoring versus canonical comparison | A self-confirming or legacy-output comparator could falsely prove the new configuration | Bind exact governed goldens and canonical behavior; prove mismatch and non-mutation cases. Implementation design remains with IA. |
| Current-row Gate availability | Actual rows may be absent, malformed or incomplete | Build/test the selected read-only readiness capability. A later live observation requires bounded authorized access; no vendor repair, backfill, secret collection or fabricated readiness is implied. |
| Generated evidence and release identity | Feedback, hand edits or stale companions can obscure source truth | Use actual single writers and retain source/output/identity distinctions. Evidence presence is not a verdict. |
| Canon filename/header discrepancies and PF09 Notes inconsistency | Unqualified version or status claims would misstate lineage | Preserve both source facts and the §10.3 ADR proposals. IA carries them into the Plan; Thoth must approve or change each. Later manual drainage is distinct from the decision; a material unsafe technical ambiguity cannot be bypassed. |
| PF04 Astra Max stall | Reported ecosystem anomaly without demonstrated causal relation | Preserve as unresolved context; no CI/model investigation or software conclusion follows. |

PF13 supplies a single-home, coherent-surface and reversible-change lens. PF21 supplies phase meaning, not a new delivery procedure. The selected workflow supplies actor and approval order. Their roles must not be interchanged.

## 10. Required Decisions and Explicit Unknowns

### 10.1 Decisions already supplied

The PO's class selection, exact change identity, corrected name, PF09.3 v1.1.3 selection, six-unit scope and Done/context boundary are explicit in the kickoff. The PO has directed this continuing Isis conversation to proceed. No additional product choice is required to submit this pending Specification. Thoth's approval or denial is still required and is not predetermined.

### 10.2 Preserved unknowns

| Item | What is unresolved | Disposition, owner and effect |
| --- | --- | --- |
| U040-01 | PF09 phase Notes call HDE-SEPA003/HDE-SEPA004 extracted non-done rows while every explicit status in those groups is Done | Preserve the inconsistency and ADR proposal C040-01. The PO's explicit disposition keeps all those units excluded. Thoth must approve or change the proposed resolution; the governed source owner performs later drainage. Reopening still requires new scope authority. |
| U040-02 | Exact remaining implementation delta and reusable portions of Partial HDE-SEPA005.1/.2 | §8 resolves specific static facts only. Mandatory IA-10 owns the full implementation audit before planning. Partial is not converted into either complete or wholly absent. |
| U040-03 | Complete circuit/substream correctness and all decisive test/validator behavior | The catalog counterexamples are bounded; exhaustive correction and proof remain selected implementation duties. No authored table or test-definition count supplies PASS. |
| U040-04 | Exact implementation loci beyond those actually governed or inspected, and safe dependency/decomposition design | Discover in IA and subsequent authorized work. Do not invent commands, test names, PR IDs, Ops units or per-file edits in this Specification. |
| U040-05 | Actual current-row Gate readiness and deployed configuration | No live inspection occurred. A future authorized observation must report what was actually reachable and tested. The capability is in scope; this authoring stage grants no DB/vendor/production access or successful-readiness claim. |
| U040-06 | Any incompatibility requiring a new bundle version or a wider integrated release | Preserve current compatibility now. If IA establishes an unavoidable scope or product conflict, route the concrete decision to PO/Thoth and the affected Canon owner before executing it. This is not permission to weaken manifest closure. |
| U040-07 | PF12/PF14/PF19 filename/header version alignment | Exact provider identities and both labels remain in §1. ADR proposals C040-02, C040-03 and C040-04 go to Thoth and into the Plan. No silent correction, inferred version adoption or source substitution is permitted. |
| U040-08 | Specification review session and decision | The first CF-E-30 review records the actual continuing Thoth reference, then all rereviews return there. No approval, review time or platform session ID is invented. |
| U040-09 | Implementation candidate, CI, QA, Ops, acceptance, authorized PF09 update and closure | None has been produced for this Epic in this authoring operation. Later native stages and owners decide from their actual evidence. There is no QA selection or attempt to count here. |
| U040-10 | Repository prompt-use installation and PF04 ecosystem anomaly | Preserve allowed provenance; later authorized owner handles installation/persistence if selected. Keep the unrelated stall unresolved. Neither creates an extra authoring gate. |

Ordinary authoring decisions have been made here: preserve the adopted default, retain existing consumer compatibility, distinguish configuration verification from downstream integration, and use native exact-source acceptance identifiers. None introduces a new product formula or waives a selected obligation.

### 10.3 Canon conflict ADR proposals — PO-directed Plan carry-forward

The Product Owner directed during this invocation: “Canonical doc conflicts found during any part of the process require an ADR proposal as part of the plan, for later drainage into canon. Thoth must approve or change.” This is an actual runtime direction, not a claim that the reusable prompts or PF Canon already contain it.

The following `C040-*` labels are Specification-local proposal references, not allocated repository ADR numbers. All are **Proposed — awaiting Thoth approval or change**. The later IA Implementation Plan must contain the complete proposals and exact source bindings, or their actual Thoth-approved replacements, with decisions and remaining drainage owners kept explicit. No separate Plan is authored here.

| Proposal | Exact conflict and source binding | Proposed decision for Thoth | Consequence and later drainage |
| --- | --- | --- | --- |
| C040-01 — PF09 phase Notes versus explicit statuses | Complete pinned PF09.3 v1.1.3 disposition preserved in the kickoff: Notes describe HDE-SEPA003/HDE-SEPA004 as “extracted non-done task rows”; both tasks and all their subtasks explicitly say Done | Retain the explicit Done statuses and the PO-selected exclusion. Treat the contradictory Notes as a documentation inconsistency; correct the phase Notes to agree with the governed disposition without reopening, reaccepting or silently changing any row. Thoth may approve this resolution or provide its precise replacement. | Preserve the pinned kickoff unchanged. The governed PF09 source owner applies the approved clarification to the appropriate current Canon through later drainage; this does not adopt v1.1.4 for this Epic. |
| C040-02 — PF12 version identity mismatch | Controlled Markdown file `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`, Drive ID `1kDa_pHeZx7zSnjftfBelWBgYXay5zMKk`; §0.1 declares v2.9.5 | Retain the exact retrieved content and both identity labels for present traceability. Have the source owner establish the intended document version from its actual revision history, then align the filename and control header without introducing substantive changes by inference. No choice between v2.9.5 and v2.9.6 is fabricated here. Thoth must approve or change this bounded resolution. | IA Plan retains the verification/drainage responsibility. PF12's governed maintainer owns the approved version-control correction; any discovered substantive conflict requires its own explicit ADR resolution before dependent action. |
| C040-03 — PF14 version identity mismatch | Controlled Markdown file `PF14-Canon-HDE-Mechanics-Guide-v3.5.6.md`, Drive ID `1G6j4L4k0ExSvffp635-msbfV-qUjzjm8`; §0.1 declares v3.5.4 | Preserve exact retrieved content and both labels; establish the intended revision through the source owner's actual history before aligning filename and header. Do not assume two intervening revisions exist or introduce their supposed content. Thoth must approve or change this resolution. | PF14's governed maintainer owns later approved metadata drainage. No mechanics implementation or changed authority follows solely from the filename. |
| C040-04 — PF19 version identity mismatch | Controlled Markdown file `PF19-Canon-Glow-QA-Guide-v3.0.4.md`, Drive ID `1AD5u5MU3RUK2K3g3GUPNJetfnEkLBmyy`; §0.1 declares v3.0.3 | Preserve exact retrieved content and both labels; have the source owner verify the intended version, then align document-control metadata without inferring changed QA requirements. Thoth must approve or change this resolution. | PF19's governed maintainer owns later approved metadata drainage. QA criteria and actual outcomes remain unchanged unless a substantive change is separately established and decided. |

These proposals distinguish documentation identity/status inconsistencies from unproven technical contradictions. The separate relationship between the complete promoted Magic10 release and this bounded Separation scope remains an IA dependency question; it is not silently classified as an adjudicated Canon conflict. If further inspection establishes a genuine conflict there or elsewhere, add an exact ADR proposal rather than inventing a resolution.

Each later proposal must retain the conflicting sources and precise clauses, overlap, affected requirements, proposed resolution, alternatives or unresolved choice, interim treatment, Thoth's actual decision or requested change, and target Canon/drainage owner. An approved ADR records the decision pending drainage; it does not claim the permanent document has already changed. If Thoth changes a proposal in this Specification review, the normal exact-redline/same-Isis revision path applies; the author does not silently implement a reviewer decision.

Thoth's required ADR disposition and later manual drainage are separate. Pending physical drainage alone does not reopen or duplicate completed work. A decisive unresolved technical conflict still blocks the affected unsafe claim or action. No proposal here is an acceptance token, independent approval object, implementation Proceed or authorization to edit PF files.

## 11. High-Level Acceptance and Evidence Expectations

These are falsifiable criteria for later implementation and independent QA, not executed steps or current PASS claims. Local labels `AC040-*` provide traceability only. The whole-change IA/QA owners must resolve actual supported evidence loci and execution detail without duplicating authoritative records.

| Criterion | Required observable outcome | Requirements and PF09 coverage | Evidence family and decisive rejection boundary |
| --- | --- | --- | --- |
| AC040-01 — Complete scope and ownership | All thirteen requirements are accounted for within the six selected units; all twenty-nine Done/context units remain excluded; source ownership is explicit; identified Canon conflicts have Plan-carried ADR proposals with actual Thoth approval or change and named later drainage | K040-REQ-001, K040-REQ-002 and the additional PO conflict direction; HDE-SEPA005 | Exact Specification/Plan/review lineage and bounded coverage record. Missing selected burden, unauthorized expansion or silent conflict resolution fails the criterion. Physical Canon drainage remains a separate later act. |
| AC040-02 — Corrected catalog and compatibility | The complete 36-Channel catalog conforms to governed identity, all circuit/substream assignments, ascending Gate endpoints, Center projection, schema and ordering; Product metadata and FE/BE promises are preserved | K040-REQ-003, K040-REQ-004; HDE-SEPA005.1 | Owning schema execution, cross-catalog positive/negative validation, canonical-byte/topology proof and bundle compatibility evidence. Count-only proof, null/invalid substreams, inconsistent endpoints, invalid set normalization or unintended metadata/schema change is insufficient. |
| AC040-03 — Adopted default and closed schemas | The actual authoritative default, all twenty signals, required profiles, both Balance operations, category/caps relationships and pure/internal result schemas conform to PF01/PF12 and exact source bytes | K040-REQ-005, K040-REQ-006; HDE-SEPA005.2 | Strict schema and cross-source closure evidence against actual configuration/result artifacts. Missing/extra/duplicate members, invalid operations/profiles, incorrect default map or hash, and an evidence snapshot used as authority must be rejected. |
| AC040-04 — Immutable fail-closed consumption | Actual schema execution and path/hash/release checks produce the immutable typed bundle outside Engine Core; valid input is accepted and each decisive invalid class refuses without fallback | K040-REQ-007, K040-REQ-008; HDE-SEPA005.3 | Loader/schema mutation evidence, deep-immutability and pure-boundary checks, governed result-validation proof. Frozen wrappers alone, swallowed refusal, partial successful output or caller/hidden configuration selection fails. |
| AC040-05 — Configuration and source identity | Identical governed bytes reproduce configuration/source identity; material input/configuration byte changes and wrong manifest/source bindings cannot retain a falsely valid active identity | K040-REQ-009; HDE-SEPA005.4 | Canonical configuration/source digest, manifest/member and release-coupling evidence under owning contracts. A repository SHA or index record cannot substitute for the necessary digest or complete release predicate. |
| AC040-06 — Exact read-only comparison | The complete PF12-governed golden collection and exact expected outputs are compared through canonical behavior; AB/BA and repeated-input identity hold where applicable; comparison leaves production selection and bytes unchanged | K040-REQ-010; HDE-SEPA005.4 | Exact golden/result and identity comparison, deliberate mismatch/invalid-input cases and before/after non-mutation evidence. A copied expected result, transitional formula, incomplete collection or comparator that mutates/activates configuration fails. |
| AC040-07 — Gate ingress and current-row readiness | Governed valid Gate representations normalize consistently; malformed, empty, duplicate, noncanonical and out-of-domain inputs refuse; current-row readiness reports actual supported readiness without changing rows or acquiring replacement data | K040-REQ-007, K040-REQ-011; HDE-SEPA005.3/.5 | Gate-normalization/rejection corpus and bounded read-only readiness proof. Synthetic fixtures prove only fixture behavior; unavailable live facts remain unavailable. No backfill, vendor fallback or unevaluated readiness may pass. |
| AC040-08 — Integrated selected proof and governed artifacts | Tests cover schema mutation, canonical bytes, catalog/caps/threshold closure, loader, identity/comparison and readiness; actual evidence is generated through its owner with coherent applicable Index/Mirror/hash/path-proof/manifest bindings | K040-REQ-001, K040-REQ-011, K040-REQ-012; HDE-SEPA005/.5 and dependencies | Exact implementation/test outcomes plus primary governed artifacts and separate integrity companions. Retained failures, stale pairs, incomplete predicate coverage, manual generated-file edits or unsupported PASS aggregation fail the affected claim. |
| AC040-09 — Boundary and decision integrity | Public Reader remains bands-only/numeric-free with no new surface; internal projections do not rescore or change identity; native evidence and actual authorized decisions remain attributable without a replacement token system | K040-REQ-002, K040-REQ-004, K040-REQ-006, K040-REQ-008, K040-REQ-012, K040-REQ-013; all six selected units | Bounded regression/security evidence, actual source/tested-state attribution and scoped reviews. Public numeric leakage, second authority, inherited acceptance or mandatory new token bureaucracy is nonconforming. |

Evidence expectations are proportional to the selected surface and risk. Canon-owned examples of relevant loci include PF12's catalog schema/domain proof families, registry and generated configuration/bundle projections, mechanics/result schemas and the governed Magic10 goldens. Naming them does not prove they currently exist, pass, require a new evidence-index row, or belong in the release manifest. Each artifact's own contract decides that distinction.

Acceptance must retain actual failed outcomes, limitations, source chronology and any authorized deviations. A passing helper or local check is not independent QA; a workflow result is not role acceptance; acceptance is not PF09 mutation or closure. Missing decisive evidence prevents the affected conclusion. Missing optional token metadata or a later evidence-storage SHA alone does not.

No numerical tolerance is invented. Where the owner requires exact bytes, identity or golden output, the comparison is exact. This section supplies no live QA script, task selection, attempted run, CI waiver or success verdict.

## 12. Canon and PF Impact

| Owning home | Impact of this Epic | Boundary |
| --- | --- | --- |
| PF09.3-Canon-HDE-Build-Checklist-Separation | Existing HDE-SEPA005 and five subtasks remain the sole selected inventory home | No new PF09 IDs, status changes or v1.1.4 adoption; governed owner applies any later supported change |
| PF01-Canon-HDE-Math-Spec | Adopted mechanics defaults, Gate semantics, deterministic identities, invariants and release consequences constrain implementation and comparison | No new formulas, retuning or empirical compatibility claim |
| PF12-Canon-HDE-Schemas-and-Artifacts | Implement and validate the exact catalog/configuration/result/golden and applicable manifest/evidence contracts | New canon-owned missing files are implementations of existing requirements; no alternate schema/artifact home or partial release exception |
| PF02-Canon-HDE-Architecture | Preserve pure core, external loading and one-way consumer/projection boundaries | No new public or I/O boundary, no independent rescoring in projections |
| PF05-Canon-HDE-CLI-API-Vendor-Ref | Preserve applicable public/private and failure contracts | No public route/payload expansion, vendor work or independent error taxonomy |
| PF14-Canon-HDE-Mechanics-Guide | Preserve reusable loader, bundles, serialization, generator and evidence responsibilities | A generated configuration view does not displace PF12's authoritative active mechanics configuration |
| PF19-Canon-Glow-QA-Guide and PF27-Canon-Plan-Templates | Later plans use exact-source criteria, proportional evidence and distinct verdict/acceptance states | No runbook here, no new token roster, no implementation-before-audit shortcut |
| PF03-Reference-Technical-Writing-Best-Practices | Source-faithful writing, exact identifiers and qualified observations | Editorial completeness is not implementation or approval |
| PF13-Reference-Glow Development Philosophy and PF21-Reference-7 Phases of Alchemical Engineering | Strategy and Separation discipline | No philosophical metaphor becomes code, payload, approval or technical evidence |
| PF10-HDE-Build-Notes and governed documentation owners | Canon conflicts require explicit Plan-carried ADR proposals, Thoth approval or change, and later owner-directed drainage under the PO direction | No PF10 source was substituted from an older change; no addendum, approval, drainage or current PF10 ruling is claimed here |

No PF mutation is authorized here. The four §10.3 ADR proposals and any later identified Canon conflicts must be carried into the Plan for Thoth approval or change and later Canon drainage. A document-control discrepancy is not silently transformed into a new technical rule, and physical drainage is not substituted for the decision. If actual implementation needs an owning contract change rather than conformance, retain the precise conflict and decision through the established route. PF20 and PF30 remain historical/reference-only for this runtime flow.

## 13. Implementation Boundary and Downstream Handoff

This is the complete initial pending Epic Specification, not an Implementation Audit, Plan, PR/Ops decomposition, implementation Proceed, QA selection, acceptance record or closure decision. It grants no repository, PF Canon, board, production, vendor, DB or prompt-control mutation authority.

The next substantive operation is **CF-E-30 — Review and Approve Epic Specification**, in `AI Prompts / HDE Change Flow`, performed by the continuing **Thoth, Head of Development** reviewer for HDE-EPIC040. Its sole native input is `SPECIFICATION_ID`, the exact saved representation of this complete document. At the first review Thoth records the actual operator-selected review conversation; that same bound session owns every rereview. The creation proof is separate audit evidence and not an additional native input or approval object.

Transport the completed native package first through a separate **GCFPE-ASSESS-10 — Assess the Next GCFPE Workload** invocation in this continuing Isis context. The Analyzer assesses workload and returns the destination-native invocation; it does not review or approve the Specification, change the actor, dispatch messages or authorize worker configuration. The Product Owner remains responsible for manual session selection/transport. No attachment is assumed transferred merely because a filename is named.

On **DENY**, preserve this pending base and Thoth's exact redline; the same Isis author revises through CF-E-40 and returns to the same Thoth reviewer through Analyzer middleware. On **APPROVE**, Thoth publishes the exact approved representation with its own embedded decision. Only that approved Specification permits **IA-10 — Create Whole-Change Implementation Audit and Plan**: a mandatory whole-change Implementation Audit must precede the change-wide Plan. Later Plan review, per-PR Proceed, authorized execution, independent QA, acceptance and Isis closure remain distinct native duties. No additional token, PF20/PF30 record or synthetic approval object is added.

The unresolved source Notes, exact static repository limitations, source-version label discrepancies, four explicit Canon-conflict ADR proposals, additional PO direction, absence of a verified repository provenance procedure and unrelated ecosystem anomaly travel with this document. Thoth must approve or change the ADR proposals, and the later Implementation Plan must retain their exact decisions and outstanding Canon drainage. None is represented as resolved by artifact persistence. No current requirement is waived, and no implementation or QA success is claimed.

ASK OK.
