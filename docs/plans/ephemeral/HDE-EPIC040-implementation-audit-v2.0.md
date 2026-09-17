# HDE-EPIC040 — Whole-Change Implementation Audit v2.0

## 1. Identity, decision boundary and conclusion

| Field | Value |
| --- | --- |
| Logical identity | HDE-EPIC040-IMPLEMENTATION-AUDIT |
| Version / artifact type | 2.0 / IMPLEMENTATION_AUDIT |
| Change | EPIC / HDE-EPIC040 / Separation Pass 3 |
| State | AUDIT_COMPLETE |
| Author | The same dedicated HDE-EPIC040 whole-change IA conversation; no invented platform ID |
| Execution posture | MANUAL_PROMPT_EXECUTION |
| Intake | OPERATOR_DIRECT_RECOVERY: PO explicitly rejected the old Plan completely and ordered a fresh IA-10 Audit and Plan incorporating completed research |
| Sole native substantive input | SPECIFICATION_ID: libfile_12bab860949c8191881510875f051460 |
| Input state | HDE-EPIC040-SPECIFICATION v1.1 / SPECIFICATION_APPROVED |
| Approval lineage | Thoth-17 APPROVE, 2026-09-08T13:23:24Z, substantive predecessor v1.0 libfile_34fb7876c10081919a7f49306d08e91f |
| Capture | 2026-09-09T08:50:30Z |
| Next internal phase | Create the distinct complete replacement whole-change Implementation Plan, after this Audit is saved |
| Next independent reviewer | Isis-50, as explicitly directed by the Product Owner; Isis-49 is historical author/reviewer |

**Conclusion.** The approved scope is implementable without another unresolved Channel-classification research task. The completed research supplies source-backed assignments for all 36 rows and an exhaustive sixteen-case connection-state oracle. Fresh comparison with the current repository confirms that its recorded before-state and retained Product metadata still match. The research's Product taxonomy normalization requires explicit disposition as new Canon ADR C040-06 in the replacement Plan review; research support is not self-approval.

The repository is not already compliant. It needs corrected data and closed schemas, actual strict loading and deep immutability, the adopted Gate-based pure mechanics, bounded application projections, deterministic comparison/readiness tooling, complete release admission and coordinated generated evidence. These are concrete engineering gaps, not permission to keep issuing blocked instruction documents. The replacement Plan must own the complete path across those dependencies.

This Audit is a fresh current-state assessment, not a revision of the rejected design. It does not approve a Plan, implement code, execute HDE tests, inspect production readiness or grant PR/Ops/QA/merge authority.

## 2. Rejection, retention and source lineage

The PO's latest instruction rejects HDE-EPIC040-IMPLEMENTATION-PLAN v1.0, libfile_d477227231e48191a0d3960b5472b02e, completely as the design to proceed with. It must not be dispatched, repaired incrementally or treated as an approved current baseline. Its historical PLAN_PENDING body is not edited.

The separate review libfile_c736de2930748191ad94ec289c0dcb1e remains a historical record of Isis-49's APPROVE at 2026-09-09T03:57:16Z. It cannot approve the newly authored Plan. The former PR01 Instruction libfile_b8d9c4a0661481918225981b61e27c47 and downstream handoff packages tied to Plan v1.0 are not executable instructions for the replacement design. No PR implementation or detailed PR Plan produced by those packages is asserted.

Preserve historical Audit v1.1 libfile_86e45fed0de48191965e232c5ee3aa79 and predecessor v1.0 libfile_c8a9601b01688191a322b63a45f3c510; their G002/G003 correction history is not erased. Old proofs libfile_662f408239e48191a1b7a74ffbb34c4d, libfile_0eb44fee134881918458139b037e5440 and libfile_a8e3e65ad7108191aabe33578c90165e are audit-only, not approval objects.

The complete kickoff remains libfile_b2399ebf8778819191593946b1cdaa45, HDE-EPIC040-SPECIFICATION-KICKOFF v1.0, KICKOFF_READY. PF09.3 v1.1.3 is the immutable selected scope baseline. Current PF09.3 v1.1.5 provides status-conflict resolution evidence only.

The research report is HDE-EPIC040-HD-mechanics-research-results-v1.0.md, libfile_4e75521ec5ec8191931024f60bf19de3. Its machine-readable evidence is HDE-EPIC040-HD-mechanics-research-evidence-v1.0.json, libfile_79ecf48f01748191a8f6a55b780992a6, source SHA-256 70ea20dc08981c991f4d8deb277b5e67a7a4ecd93b6b44781831ee60210c618a. The executed query is libfile_1ee719415ad8819181197eeb2bfbac82. RCA HDE-EPIC040-PR10-onward-RCA-v1.0.md is libfile_01b0bc6232408191bc59e9f2bb5ee7d2. These supply research/evidentiary history, not a second approved Specification.

All runtime artifacts named here reside in /Glow HDE 3.0. Historical Canon decisions C040-01 through C040-05 remain explicit decisions under their own exact source/review bindings. Rejecting the old implementation design does not silently erase them.

## 3. Complete scope

### Selected units — six

| PF09 unit | Exact source title | Source status | This Specification's disposition |
| --- | --- | --- | --- |
| HDE-SEPA005 | Production Magic10 mechanics configuration contract | Partial | In scope: coherent parent obligation |
| HDE-SEPA005.1 | Corrected canonical 36-Channel catalog | Partial | In scope |
| HDE-SEPA005.2 | Magic10 mechanics schema and default configuration | Partial | In scope |
| HDE-SEPA005.3 | Fail-closed mechanics configuration loader | Not done | In scope |
| HDE-SEPA005.4 | Mechanics configuration identity and deterministic comparison | Not done | In scope |
| HDE-SEPA005.5 | Separation implementation tests and governed artifacts | Not done | In scope |

### Excluded Done/context units — twenty-nine

The following exact pinned-source titles and identities are retained. They are excluded scope, not freshly reverified Done claims.

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

No HDE-SEPA006 family member, PF09.3 successor inventory, broad HDE-DIST008.1 completion, new public category expansion, new scoring preset, new vendor integration, database migration, production backfill or new acceptance-token system is selected. Necessary bounded adapters/tests that exercise the chosen configuration's full result contract are dependencies, not reopening entire excluded rows.

## 4. Current-source access and coverage

### 4.1 Controlled Markdown resolution

This invocation resolved and verified the direct-parent chain:

Glow (1MZXcC5tKMkI9n8EobkywIj1ifcF6IvZ3) → Core Docs (18T84WC_Jxjb75V37_eYcRqn8zOjHYgxu) → PFCanon (1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3).

The complete direct-child listing was used to select one current controlled Markdown identity per PF. Each selected file's parent matched PFCanon. Neither attached older copies, search order nor a highest-looking filename supplied current authority.

| Source | Exact fetched name | Drive file identity | Direct parent | Modified time |
| --- | --- | --- | --- | --- |
| PF01 | PF01-Canon-HDE-Math-Spec-v1.3.7.md | `1ILESkXCDr11Me6WvCBPpebfmQFwEz63p` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-01T02:58:42.000Z |
| PF02 | PF02-Canon-HDE-Architecture-v2.4.5.md | `1y4JvZKVZR_5J_wynT4p3HtYgX4cRSIB6` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-01T02:58:16.000Z |
| PF03 | PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md | `1M_PTWi-ySFs1NWIjFpd9p2IL-vsKbJEA` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-01T02:58:04.000Z |
| PF05 | PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.2.md | `1P78CNLZhAIYYTHXOAi2aX1HoImo9TuXo` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-01T02:57:23.000Z |
| PF09.3 | PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.5.md | `1JLCCfPPryE_EG_62B1PHSZ2QGKvGsolp` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-09T04:21:52.000Z |
| PF10 | PF10-HDE-Build-Notes-v13.1.5.md | `1-4cB4Yi1O0d2GzasR3UrhSk5SB5su2QV` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-09T04:52:54.000Z |
| PF12 | PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md | `1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-09T04:19:43.000Z |
| PF14 | PF14-Canon-HDE-Mechanics-Guide-v3.5.7.md | `13kNlj4Y_F1fIqE3_L4eyjeJUkdO3LkX1` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-09T04:13:05.000Z |
| PF19 | PF19-Canon-Glow-QA-Guide-v3.0.5.md | `1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-09T04:15:24.000Z |
| PF27 | PF27-Canon-Plan-Templates-v2.0.5.md | `1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-07T20:30:02.000Z |
| PF13 | PF13- Reference-Glow-Development-Philosophy v1.md | `1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-01T02:52:53.000Z |
| PF21 | PF21-Reference-7 Phases of Alchemical Engineering.md | `1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI` | `1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3` | 2026-09-01T02:50:07.000Z |

The complete selected Specification and research report were read; the decisive source units were retrieved without relying on search snippets. Technical inspection covered the complete owning units needed for this Audit, not every unrelated chapter of the large Canon collection:

| Owner | Material coverage and limited authority |
| --- | --- |
| HDE-Math-Spec | §4 Gate/identity boundary; §5.2 adopted mechanics map, profiles, reducers and identity; §6.1–6.2 connection predicates; §9.5 complete golden requirements |
| HDE-Architecture | §2.1–2.2 pure core, immutable configuration and application/projection separation |
| HDE-Schemas & Artifacts | §2.1 catalog; §2.9 configuration/result contracts; canonical bytes and manifest/member form; promoted release set; §8.14–8.15 generation, comparison and release-attestation contracts |
| HDE-Mechanics Guide | §6.7 current pure-core contract and retained superseded tests; §7 configuration/generation responsibilities |
| HDE-CLI/API/Vendor Reference | §4.1.3 internal result versus public Reader; §5.1.0 production read-only UUID/current-row resolution; existing transport/rail constraints |
| Glow QA Guide | §3.4.14 exact-source criteria, evidence families and separation of whole-change planning from Live QA scripts |
| Plan Templates | §12 whole-change Audit and Plan contract |
| Technical Writing Best Practices | Complete editorial reference; source fidelity, claim-state separation and retention |
| Glow Development Philosophy / Seven Phases | Complete references; unchanged approved Strategy Card and Separation focus |
| HDE-Build Notes | Current complete relevant C040 addenda and index, including current 2.3 and 2.4 publication evidence |
| Build Checklist — Separation | Current status evidence only; pinned v1.1.3 membership remains controlled by exact Specification/kickoff |

### 4.2 Notion contract selection

IA-10 — Create Whole-Change Implementation Audit and Plan, AI Prompts / HDE IA, runtime 090826.2, GCFPE-20260908.2, page 3d54590a-05eb-8139-adb8-d20cc7054fb3, retrieved revision 2026-09-08T20:23:24.534Z, was read completely.

The current owning Membership/Release Register and manual Epic Alpha selection were inspected. Automated orchestration is held; this explicit manual operation is not blocked by that hold. IA-30 and the single GCFPE-ASSESS-10 were read as the concrete next contract/middleware, not executed. The approved exact Specification satisfies native substantive intake. No missing known approval was concealed under recovery labeling. No preceding Analyzer result for this latest operator-direct recovery is invented.

### 4.3 Repository basis and inspected loci

Repository: amthorn78/glow-hdengine-v2. Current main was refreshed in this invocation to commit 9065e6f0c01ad82a65c78687cd6c55e26ca33a1f, tree e07c4e4297c75fe83e0f286aa1cee46ffca6c62e; complete recursive tree contained 7,042 entries and was not truncated. The previously observed SHA is still current; it is an observation, not an acceptance-SHA gate.

Inspected owning files included the Channel/Gate/category/caps/manifest/threshold inputs; Channel and FE/BE schemas; registry loader and bundle builders; configuration and registry generators; core/calculators/compat/application/Reader/CLI/narrative/BodyGraph adapters; manifest/release/attestation/evidence writers; and existing core/config/compat/HTTP/CLI tests. Exact path/function evidence is attached to each finding below. AGENTS.md was read as repository task constraints. No working tree was mutated or tests imported/executed.

Absence findings below use this complete tree and the expected Canon path; a failed retrieval is not treated as file absence.

## 5. Fresh findings and engineering consequences

| ID | Current evidence and finding | Required consequence; source/requirement |
| --- | --- | --- |
| IA040R-F01 | catalog/channels_v1.json has 36 rows, but fresh research join identifies 32 changed rows: 24 circuit_primary corrections, 30 substream corrections and five nonascending Gate arrays. Four rows already match: 04-63, 17-62, 20-57, 28-38. | Apply complete source-backed row assignments, not null-only filling. Preserve all metadata. PF12 §2.1; K040-REQ-003/004; C040-06 proposed. |
| IA040R-F02 | schemas/channels_v1.schema.json admits null substream and omits ego from its non-null enum. Enumeration alone does not establish any row's proper assignment. | Close the schema to all seven adopted non-null values and enforce roster, pair and topology relationships independently. Existing be.v1/fe.v1 identities remain compatible. K040-REQ-003/004/008. |
| IA040R-F03 | Four Canon-required files are absent: catalog/magic10_mechanics_v1.json and schemas/magic10_mechanics_v1.schema.json, magic10_result_v1.schema.json, magic10_compat_result_v1.schema.json. | Construct the exact adopted default, nested profiles/responses, twenty signals, two Balance operations and closed pure/internal schemas from PF01/PF12. No tuning research is needed. K040-REQ-005/006. |
| IA040R-F04 | engine/config/registry_loader.py uses json.loads before duplicate-key detection; some fields are coerced; Channel Gates are sorted during loading; complete governing schema execution, exact source-byte/hash closure and recursive immutability are not supplied. A frozen outer bundle leaves nested mappings mutable. | Validate raw representation before normalization, reject duplicate object keys, execute local owning schemas and relational checks, verify canonical bytes and actual hashes, then recursively freeze. Never admit a malformed source by coercion. K040-REQ-007/008/009. |
| IA040R-F05 | tools/config/artifacts.py build_band_edges(root) reads global BAND_SOURCE. tools/generate_registry_report.py mixes a supplied root with module ROOT metadata reads. engine/config/bundles.py hashes disk primaries while deriving projections from a loaded bundle, without complete equality closure to those primaries. | Bind every read/hash/write to one resolved root and captured source set; check primary payload equals the derived data being attributed to its hash. Fix when those generators are first affected, not only at release. K040-REQ-004/009/012. |
| IA040R-F06 | engine/core/core.py consumes ParticipantState.compat_score and optional CoreConfig, computes a precomputed-score average and returns the old shape; existing test_engine_core_* files test that scaffold. | Replace with exact four-argument Gate-based compute_core, complete twenty-signal/ten-category result and deterministic pair identity. Retire successful old paths and update actual callers/tests. PF01/PF02; C040-05; K040-REQ-005/007/009/010. |
| IA040R-F07 | engine/compat/compute.py _score_for uses pair/person-derived hashes and viewer weights; _person_from_resolved discards Gates. Resolution can reduce a chart to identity hints. engine/runtime/public.py derives bands from ts_v0 and defaults eligibility. | Route validated complete projections to one intrinsic computation; keep UUID eligibility and directional narrative orientation outside it; no UID-only success or old scalar fallback. Preserve legal existing input acquisition boundaries. K040-REQ-007–011. |
| IA040R-F08 | engine/bodygraph/projection.py copies an unnormalized gates value. The Canon shared engine/bodygraph/gates.py and tools/bodygraph/check_magic10_gate_readiness.py paths are absent. | One strict Gate normalizer reused at ingress, mapping/persistence, loading/application, and read-only readiness. Reject bad/missing/duplicate Gates before success; do not backfill or fetch vendor data in readiness. K040-REQ-007/008/011. |
| IA040R-F09 | adapter/http_reader.py's existing reader_v1_post returns method_not_allowed 405; public configuration/result projection does not establish the current PF05 §5.1.0 UUID/current-row success path. HTTP compatibility wiring also contains identity-only seams. | Include only the existing required Reader/current-row and internal projection dependencies needed by exact golden/application contracts. Implement that existing contracted POST path, not a new public route or new payload; retain numeric-free six-key Reader and read-only resolution. K040-REQ-010/011 and AC040-09. |
| IA040R-F10 | Current internal calculation and router output do not establish complete magic10_compat_result.v1 with required shared and both directional personal keys, normalized outside pure math. | Assemble symmetric internal results per eligible evaluation, validate exact schemas, keep numerics internal and identity-free intrinsic cache separate from directional augmentation. K040-REQ-005/007/010. |
| IA040R-F11 | Canon requires the complete eight golden cases, including kernel-only G002/G003 and application/Reader G007/G008. Old scalar tests and a report presence cannot establish that collection. | Build one read-only comparator over canonical implementation; preserve independent fixed expected values and byte/hash oracles, exact identities, all eight members, mismatch and non-mutation cases. No second calculator or expected-output regeneration from current output. K040-REQ-010/011. |
| IA040R-F12 | catalog/manifest.json has fifteen members and does not close the adopted Magic-10 promoted set. Eight promoted required paths are absent in the tree: the four config/schema paths in F03 and gates.py, composite.py, signals.py, check_magic10_gate_readiness.py. | Preserve legitimate existing members, add all required promoted members, validate their owning formats before exact hash/size, and compute release identity only from the complete canonical manifest. A local candidate is not an active release. K040-REQ-006/009/012. |
| IA040R-F13 | Existing canonical writers and evidence index machinery exist, but their presence proves neither regenerated companions nor same-candidate acceptance. External attestation must occur after final repository documentation. | Changed-input primaries and required derived companions move together through owning writers; complete final documentation precedes clean-candidate external attestation. No manual generated-evidence edits or circular proof hash feedback. K040-REQ-012/013. |
| IA040R-F14 | Earlier research gate was passed onward unresolved; earlier instruction had demonstrable none-response and profile-shape errors recorded in the RCA. | Replacement design must include complete row evidence and exact config examples; zero response is valid, zero weight is invalid, and profiles use nested responses. Correct acceptance ownership and distinguish per-PR local verification from release admission. All selected requirements; RCA040 findings. |

The five nonascending baseline arrays are 02-14, 05-15, 06-59, 07-31 and 09-52. Fourteen baseline null substreams are 01-08, 02-14, 03-60, 05-15, 07-31, 09-52, 10-20, 10-34, 13-33, 20-34, 21-45, 25-51, 29-46 and 42-53. The replacement addresses another sixteen incorrect non-null substreams as well; limiting correction to fourteen nulls would leave a known defect.

## 6. Research closure, authority and accessible Canon home

### 6.1 What is now established

The saved research includes thirty-six unique closed Channel IDs, each with endpoint Gates, two Gate-derived Centers, source circuit/system terminology, normalized circuit_primary/substream, exact source references and extracted rationale. It also retains all current primary_domain/domains/flags metadata, 64 Gate-to-Center evidence records, sixteen presence-state cases, adverse checks and a seven-entry ambiguity history.

This invocation performed a static JSON/data comparison, not an HDE application test: 36/36 research IDs matched the freshly fetched catalog; 108/108 metadata fields matched; Gate-pair change count was five; primary/substream change counts were twenty-four/thirty; no Center-set correction was indicated. The result does not assert that repository rows have been changed.

The source-supported normalization is Individual 15, Collective 14, Tribal 7; Knowing 9, Centering 2, Integration 4, Logic 7, Sensing 7, Ego 5, Defense 2. The four Integration Channels are 10-20, 10-57, 20-34 and 34-57. 10-34 remains Centering; 20-57 remains Knowing. The Product Owner supplied corroborating Integration research and retains credit for it.

### 6.2 Why an ADR is necessary

Older structural teaching describes Integration separately from the six circuits and three circuit groups; current Jovian broad circuitry language places Integration within Individual. The proposed Product projection keeps the already adopted three-value primary enum by encoding these four rows as individual/integration while retaining the structural distinction and source terminology in documentation. It must not falsely claim that all six pairings among Gates 10/20/34/57 are Integration Channels.

C040-06 is NEW_CANON because the authoritative row-assignment/provenance and explicit normalization need a durable controlled home. The research does not create new mathematics, choose new signal mappings, calibrate response profiles or approve itself. The replacement Plan's existing IA-30 review must explicitly decide it. No second approval object is introduced.

### 6.3 Permanent drainage proposal

Primary target: HDE-Schemas & Artifacts, existing Channel Catalog §2.1, for the complete thirty-six-row assignment table, typed normalization and provenance/maintenance rule. Secondary target: HDE-Math-Spec §6.1–6.2, for a reference to that classification home and complete sixteen-case conformance clarification tied to its existing predicates. PF01 retains all mathematical authority; PF12 retains catalog/schema authority.

The new standalone C040-06 ADR must carry the full evidence table and exact proposed disposition so future developers do not need this conversation. Existing governed PF12/PF01 maintainers own permanent drainage through separately authorized Canon work. Any approved-decision PF10 addendum is prepared by the actual approving reviewer under IA-30; manual publication is separate. Nothing is published to Canon by this Audit.

## 7. Requirement and acceptance coverage

| Requirement | Audited conclusion | Decisive implementation coverage required |
| --- | --- | --- |
| K040-REQ-001 | Parent not satisfied by partial registry | Coherent data → strict bundle → core → application → verification → complete release |
| K040-REQ-002 | Current owners established; C040-06 proposed | Explicit ADR review, source index and permanent single-home drainage |
| K040-REQ-003 | Full 36-row correction necessary and now source-backed | Exact row table, ordered Gates, roster/topology/schema checks |
| K040-REQ-004 | Existing metadata/FE/BE compatibility can be preserved | Exact metadata joins; unchanged schema identities; generated projections |
| K040-REQ-005 | Adopted values are fully defined; implementation missing | All twenty signals, nested profiles, Balance, caps and result schemas |
| K040-REQ-006 | No complete admitted active Magic10 bundle currently shown | Immutable configuration and complete promoted release closure |
| K040-REQ-007 | Loader/core/input validation incomplete | One typed frozen bundle, Gate normalizer and actual result validation |
| K040-REQ-008 | Coercion, malformed input and old fallback risks evidenced | Raw-form/schema/relational/identity rejection and secret-safe failure |
| K040-REQ-009 | Identity homes exist normatively, not fully implemented | Source/config exact hashes, canonical pair and complete release identity |
| K040-REQ-010 | Complete golden comparison depends on real core/application | All eight exact cases and read-only mismatch/identity checks |
| K040-REQ-011 | Required adverse/readiness coverage missing | Mutation matrix, Gate ingress, read-only current-row capability |
| K040-REQ-012 | Writers reusable but require integration/root fixes | Primary-before-derived, complete companions and final external attestation |
| K040-REQ-013 | Exact-source lineage sufficient | No inherited token rosters or extra universal approval registry |

| Acceptance criterion | Audit coverage / required proof family |
| --- | --- |
| AC040-01 | All 35 pinned units retained, exact Spec approval and carried ADR decisions |
| AC040-02 | Complete corrected catalog, Product metadata equality and FE/BE compatibility |
| AC040-03 | Strict default mechanics and both result schemas; positive/adverse validation |
| AC040-04 | Actual schema execution, relational checks, raw Gate rejection, deep immutability |
| AC040-05 | Config/source/manifest/release identity changes and mismatch refusal |
| AC040-06 | Eight-case exact golden comparison; canonical path and non-mutation proof |
| AC040-07 | Shared Gate normalization and current-row read-only readiness capability |
| AC040-08 | Owning test/evidence families, canonical writers, index/mirror/hash/path companions |
| AC040-09 | Pure versus application/public boundary, privacy/rails, rollback and no partial release |

No criterion is marked PASS by this Audit. This table is source and design-burden coverage.

## 8. Carried Canon decisions — present state, not renewed approvals

C040-01–04 were APPROVED unchanged by Thoth-17 at 2026-09-08T13:23:24Z against Specification v1.0, represented in exact approved v1.1. Their matching decision batch remains published as PF10 Addendum 2.2. Current PF09.3 v1.1.5 Notes agree with Done statuses; PF12 filename/body agree at v2.9.6, PF14 at v3.5.7, PF19 at v3.0.5. The four original conflict predicates and corresponding source corrections are resolved. Their former discrepancies remain historical; do not carry them as pending drainage or adopt a successor inventory.

The complete C040-01–04 informational resolution record is libfile_e0a486859cf88191ab9474a0c8dd0c22. Current PF10 v13.1.5 now contains its body and index entry as Addendum 2.4. Prior assertions of publication pending are historical, not current.

C040-05 was APPROVED exactly as proposed, alternative A, by Isis-49 at 2026-09-09T03:57:16Z against Plan v1.0. Its complete standalone addendum is libfile_1f57caadf8688191a393f4b2a710149c. PF10 v13.1.5 contains both body and index entry for Addendum 2.3. Current inserted 2.3/2.4 bodies retain stale preparation/status wording: **body and index insertion verified; stale preparation/historical-status wording reconciliation pending**, non-gating. Do not duplicate either body or decision.

Permanent C040-05 correction of PF14 §6.7 legacy test passages remains pending with the governed PF14 maintainer. Preserve four-argument Gate-based tests and the separate HDE-DIST008.1 boundary. No second calculator or optional scoring configuration is permitted.

The complete original proposals, affected requirements, alternatives, interim treatments, risks, owners and exact decision history will be carried verbatim as historical records in the new Plan, with the current-state overlay above. C040-06 is the sole newly proposed decision identified by this rebuild. No C040 entry is REJECTED or APPROVED_AS_CHANGED; the PO-rejected Plan artifact is a different object from the retained decision register.

## 9. Feasibility constraints, security and recovery

A coherent design can be built from the exact adopted defaults, the completed row evidence and reusable current writers. It must explicitly distinguish local authoring/candidate validation from production release admission. A partial candidate must never acquire a successful active-release identity. Component PRs may be implemented and verified against their bounded inputs; final release admission must include every promoted source and every completed dependency.

The current Reader resolver, vendor acquisition and database behavior must not be blended. Production Reader UUID lookup and readiness remain read-only; no request-time vendor acquisition or arbitrary-string UUID conversion. Existing authorized nonproduction acquisition paths retain their existing rails and cannot invent Gate data on a miss. Any requirement for a new DB schema, new public contract or incompatible FE/BE migration would exceed this design boundary and return before affected mutation.

No test, CI workflow, live service, deployed release, credential, database content or current-row readiness result was executed or verified. The unrelated PF04 Astra Max stall remains unresolved and unattributed. No model causality or consequence for this Epic is inferred.

Recovery design must restore complete compatible code/configuration/schema/release sets, not an isolated stale catalog. Evidence publication failure must preserve validated primaries without claiming companions complete. Read-only tools must never alter a candidate to make it match expectations. Formula mismatches must not rewrite golden expected values.

## 10. Prompt-use and Audit completion

GCFPE_PROMPT_USES:

- Usage: GCFPE-USE-HDE-EPIC040-IA-10-20260909-02.
- Prompt: IA-10, runtime 090826.2, GCFPE-20260908.2, page 3d54590a-05eb-8139-adb8-d20cc7054fb3, revision 2026-09-08T20:23:24.534Z.
- Role/stage: same dedicated whole-change IA / fresh Audit then replacement Plan / operator-direct recovery.
- Capture: 2026-09-09T08:50:30Z.
- Input: exact approved Specification v1.1 libfile_12bab860949c8191881510875f051460.
- Scope: all six selected units, K040-REQ-001 through K040-REQ-013 and AC040-01 through AC040-09.
- Result at this phase: HDE-EPIC040-IMPLEMENTATION-AUDIT v2.0 / AUDIT_COMPLETE; its provider reference is supplied after actual persistence.
- Actual executing model/reasoning: not recorded as an observed configuration; none inferred from human launch advice.
- Prior uses: retain exact CF-E uses in Specification/kickoff; GCFPE-USE-HDE-EPIC040-IA-10-20260908-01; GCFPE-USE-HDE-EPIC040-IA-30-20260909-01; old PR-10 GCFPE-USE-HDE-EPIC040-PR-10-20260909-01 and actual assessment history in their preserved artifacts. A prepared assessment identifier is not evidence of execution.
- Repository provenance procedure: docs/changes/GCFPE_PROMPT_PROVENANCE.md absent in the complete current tree. Persistence remains pending, non-gating, for an actually authorized writer under an installed supported procedure. No installation is invented.
- Attempts/results: static reads and static data integrity comparison only; no implementation, PR, CI, QA, Ops or repository result.

Audit completeness checks: exact approved intake and approval inspected; selected/excluded population 6 + 29 = 35; all thirteen requirements and nine criteria accounted for; current sources and repository uniquely resolved; completed research assessed; new and retained ADR states separated; actual implementation gaps identified with owning loci and constraints.

**AUDIT_COMPLETE.** Save and read back this complete artifact before beginning the distinct replacement Plan. This internal Audit-to-Plan phase change does not receive an intervening Analyzer. A short separate proof records actual persistence/checks without becoming substantive authority.

