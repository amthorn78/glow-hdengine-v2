# HDE-EPIC040 — Human Design mechanics research query

Version: 1.0 · Prepared: 2026-09-09

Purpose: obtain the authoritative domain evidence needed to repair the implementability of Separation Pass 3. This is a research request, not a PR instruction, approval, implementation authorization or Canon amendment. The prompt below can be used for direct research or pasted into the Product Owner's authoritative-source session. It has not been sent to another session.

---

## Research request

Please produce a source-grounded mechanics evidence pack for the engineer responsible for HDE-EPIC040, Separation Pass 3.

The immediate need is to establish the correct classification of all 36 Human Design Channels, with enough source evidence to implement and test a catalog correction without guessing. We also need a bounded cross-check of connection-state terminology used by the downstream mechanics implementation.

Do the research and return the actual supported answers. Do not return another research plan, a list of books without extracted facts, or a statement that the engineer should investigate later. If your sources genuinely cannot settle a required fact, identify that exact fact, the conflicting or missing evidence, and the narrowest authoritative clarification needed.

The engineer retains responsibility for software architecture, interfaces, schemas, canonical writers, projections, test design, security, rollback and every PR's implementability. You are not being asked to design the application, approve its Plan, invent Product policy or alter adopted scoring mathematics.

### 1. Source access, authority and evidence rules

Start by identifying the authoritative source you can actually query: title, author/teacher, edition or version, publication details where known, and the exact accessible file or resource. Distinguish a primary text or teaching from a training derivative, secondary explanation, transcript, OCR conversion, prior AI answer and model recollection. Do not infer authority from a filename or from the confidence of an answer.

Use the Product Owner-provided authoritative source and the permitted Glow references. Do not silently substitute public-web summaries or model memory. If another source is necessary, identify it and the exact question it would answer.

Useful existing source routes:

| Source | Exact location | Role and limitation |
| --- | --- | --- |
| Human Design Reference Index v1.1.0 | [Glow / HD Refs index](https://drive.google.com/file/d/15nTQLpokmquFSFBDIsYtFwnnqdLNKHHv/view) | Source routing and authority distinctions; not itself classification evidence. Relevant routes are M02, M04, M05 and M06. |
| PF08 — Human Design System | [Current controlled Markdown](https://drive.google.com/file/d/1BhLsOTIliAyeP7ZQgHT2uvm2Ym_QmTK7/view) | Designated doctrinal root within actual coverage; transformed-copy and diagram limitations must be respected. |
| PF11 — The Rave I Ching | [Current controlled Markdown](https://drive.google.com/file/d/1Ou6zy_vm_6jMQSP1Znwrc7_3ER1YQAQy/view) | Designated root containing Gate, harmonic, Channel, center and circuit captions. A Gate-scoped caption must not automatically be assigned to every incident Channel. Some content is transformed or summarized. |
| RAVE ABC 2 3 6, Level I Student Modules | [Original illustrated PDF](https://drive.google.com/file/d/1jDumjx09Ybta84GM9xXxkuaLN1NTGj6b/view); [OCR search companion](https://drive.google.com/file/d/1j3Fb-ygtiITiyNEFcIcGxaGC3DW3mKXY/view) | Theresa Blanding, based on Ra Uru Hu's teaching; Jovian Archive copyright 2005. The index designates it an affiliated training derivative. Module 2 covers circuitry. Use it for navigation/corroboration; disputed detail needs appropriate primary-source support. Verify mechanics-sensitive diagrams and numbers in the PDF, not uncorrected OCR alone. |
| Formats and Transcendence: The Abstract System | [Retained specialist text](https://drive.google.com/file/d/1H1Aevpy-I1zdIpEb5vDgsCArQgp2J3Aj/view) | Direct specialist teaching, limited to its actual Abstract/Sensing coverage; not a complete circuit-classification authority. |
| PF12 v2.9.6, §2.1 | [Controlled Product contract](https://drive.google.com/file/d/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ/view) | Owns the target catalog vocabulary and shape. Allowed enum values do not prove individual assignments. |
| PF01 v1.3.7, §§5.2 and 6.1–6.2 | [Controlled Product mathematics](https://drive.google.com/file/d/1ILESkXCDr11Me6WvCBPpebfmQFwEz63p/view) | Owns the adopted score configuration and connection-state algorithm. This request does not reopen its mathematics. |

The source list is a starting route, not a claim that every necessary fact is already established. If an exact resource is unavailable to you, say which one. Do not claim to have inspected an inaccessible source or diagram. A faithful text derivative may establish clear prose; image-dependent or disputed claims require adequate original-page verification.

For each material claim, preserve the source's actual statement separately from any inference or machine-label normalization. Cite exact pages/clauses/headings and a short identifying excerpt or precise paraphrase. For PDFs, distinguish physical PDF page from printed page when they differ. Shared citations and explicit source-backed derivations are acceptable; 36 separate books or unique quotations are not required.

### 2. Required output A — complete 36-Channel evidence matrix

Return one row for every ID below, in this order. These are the closed Product identities; no row may be added, dropped, duplicated or replaced.

```text
01-08, 02-14, 03-60, 04-63, 05-15, 06-59, 07-31, 09-52,
10-20, 10-34, 10-57, 11-56, 12-22, 13-33, 16-48, 17-62,
18-58, 19-49, 20-34, 20-57, 21-45, 23-43, 24-61, 25-51,
26-44, 27-50, 28-38, 29-46, 30-41, 32-54, 34-57, 35-36,
37-40, 39-55, 42-53, 47-64
```

Each row must contain:

| Field | Required answer |
| --- | --- |
| `channel_id` | Exact closed identity above. |
| `gates` | The two distinct numeric endpoints in ascending order. Preserve a source's reversed display order in its citation, not in the canonical pair. |
| `gate_centers` | The center belonging to each endpoint, with source support. |
| `derived_center_set` | The two distinct centers derived from those endpoint facts. |
| `source_circuit_group` | The source's actual group/family description, including exceptions or overlapping classifications. |
| `source_circuit_or_substream` | The source's actual circuit/substream/system description. Preserve its terminology. |
| `circuit_primary` | Supported mapping to the target Product vocabulary, or an explicit unresolved mapping—not a forced assignment. |
| `substream` | Supported mapping to the target vocabulary, or an explicit unresolved mapping. |
| `evidence_refs` | Exact source identities and locators supporting topology, classification and any normalization rule. |
| `extracted_fact_and_derivation` | What the source actually establishes, and how that yields this row. |
| `status_and_ambiguity` | `SUPPORTED`, `CONTRADICTORY` or `UNRESOLVED`, with a precise explanation where needed. |

Current required machine vocabularies are:

```text
centers:
  ajna, ego, g, head, root, sacral, solar_plexus, spleen, throat

circuit_primary:
  individual, collective, tribal

substream:
  knowing, logic, sensing, ego, defense, centering, integration
```

The final runtime catalog requires a non-null `substream`. That does not authorize inventing a value when the research cannot establish one. A research record may explicitly leave a proposed mapping unresolved; it is not a publishable catalog row.

The existing Product fields `primary_domain`, `domains` and `flags` must remain unchanged and non-scoring. Their values are repository evidence, not HD doctrine. The engineer will join the verified classification to the existing rows and prove these fields were preserved. Do not invent, reinterpret or reassign them, or declare preservation verified without the actual before/after data.

Research all 36 rows, not just the known nulls. For context only, the prior repository audit found five reversed Gate arrays and fourteen null substreams; it did not prove that all other classifications were correct. Current labels, examples, nulls and schema enumeration are not assignment evidence.

### 3. Resolve the taxonomy questions explicitly

Answer these before presenting the matrix as complete:

1. What is the exact relationship among a circuit group, circuit, substream, stream and Integration in the sources used? Which names are genuine synonyms, and which describe different structures?
2. Is Integration a circuit, a separate system, a member of the Individual group, or described differently at different teaching levels? Give the source-specific answer. Then state whether the Product's three-value `circuit_primary` field can represent it directly, requires an already-governed normalization rule, or leaves a real Product decision unresolved.
3. Resolve these six incident Channel identities individually: `10-20`, `10-34`, `10-57`, `20-34`, `20-57`, `34-57`. Do not assign all six the same substream merely because their Gates occur in an Integration diagram. Distinguish Channel membership from a Gate's participation in several structures.
4. PF11's Gate 10 and Gate 34 records carry Centering captions, while Gate 20 and Gate 57 records carry Knowing captions and list overlapping Channel identities. Explain the scope of those captions using authoritative context; do not treat endpoint captions as a complete Channel-classification algorithm.
5. The Rave ABC OCR companion has relevant Integration/group material around physical PDF pages 24–28 and 36–38. These are research leads, not verified final assignments. Check original illustrations and appropriate primary-source context where they matter.
6. Explain supported normalization of Understanding/Logic, Abstract/Sensing and Defence/Defense. PF12 explicitly permits the human-facing Logic/Understanding and Defense/Defence spellings; do not infer every other taxonomy equivalence from that allowance. Distinguish `ego` as a center ID from `ego` as a circuit/substream label.
7. Are the required classifications static properties of the Channel, independent of whether that Channel is activated in one chart or formed between two charts? Identify any source-supported qualifications relevant to catalog use.

If the taxonomy needs a small hierarchy diagram to make the distinction clear, include one with cited relationships, or an equivalent table. Do not draw unsupported hierarchy edges. A source disagreement must be reported, not silently resolved by selecting whichever label fits the schema.

### 4. Required output B — bounded connection-mechanics cross-check

The downstream implementation uses the following adopted PF01 §6.1 predicates, in this priority order. They are supplied as the existing Product contract, not as a request for you to invent a relationship-scoring system:

| Priority | State | Adopted predicate | Ownership |
| --- | --- | --- | --- |
| 1 | `companionship` | Both members possess both endpoints of the same Channel. | No owner field. |
| 2 | `compromise` | Exactly one member possesses both endpoints; the other possesses exactly one. | Full-Channel owner. |
| 3 | `dominance` | Exactly one member possesses both endpoints; the other possesses neither. | Full-Channel owner. |
| 4 | `electromagnetic` | Neither possesses the full Channel; they exclusively possess opposite endpoints. | No owner field. |
| 5 | `none` | All remaining endpoint-presence patterns. | No owner field. |

Provide authoritative support for the underlying connection terminology and its boundaries. Identify any genuine mismatch with the adopted rules precisely; do not silently change the rules. `none` is the Product's residual classifier state and need not be presented as a historical teaching term.

Return all 16 ordered cases from:

```text
A_presence × B_presence
where each presence is one of: 00, 10, 01, 11
and the two bits refer to the same ordered Channel endpoints.
```

For each case provide the state, full-Channel owner A/B where applicable, and a concise explanation. Distinguish results obtained by evaluating the supplied Product predicates from statements explicitly present in the teaching source. These are proposed test inputs/oracles, not executed tests or accepted goldens.

Address the specific adverse cases: same-end hanging Gates; one unmatched half; both ends present in one member only; full Channel plus one matching half; both members with the same full Channel; reversed member order; and unrelated Gates outside the selected Channel. Explain why a Gate activation and a complete Channel are not interchangeable facts.

Source-supported statements about combining Personality and Design activations may be included where necessary to explain endpoint presence. Do not introduce chart calculation, ephemeris, transit acquisition, substructure interpretation or a new ingestion policy. The software's validated Gate-ingress contract remains separately owned.

The engineer will implement normalized owner identities, pair ordering, hashing, deduplication and public/internal projections under existing Product contracts. Do not derive compatibility scores, weights, rankings, category assignments, medical claims or personal relationship advice from these classifications.

### 5. Return format and completion test

Return, in order:

1. A short conclusion: whether the complete classification is supported, and the exact remaining questions if not.
2. A source register identifying actual reads, authority, edition/version, locators and extraction/visual limitations.
3. The complete 36-row human-readable matrix.
4. Machine-readable JSON containing the same 36 research rows, with source IDs and a source register. This is an evidence interchange format, not an authorized replacement runtime schema. Unresolved research fields must be explicit and must not masquerade as valid runtime assignments.
5. The taxonomy explanation and any necessary small diagram/table.
6. The 16-case connection-state table and its evidence/derivation distinction.
7. An ambiguity register with the affected exact rows/fields, competing source statements, why existing sources do not settle them, and the smallest clarification needed from a named source or governed owner if known. Do not invent an owner.

Check that there are exactly 36 unique Channel IDs, no missing or extra rows, ascending endpoint pairs matching the IDs, and a supported center mapping covering the endpoint Gates. Reused source-backed rules should be cited once and referenced from all dependent rows. Count `SUPPORTED`, `CONTRADICTORY` and `UNRESOLVED` rows; their sum must be 36. Separately identify any unresolved group-to-Product normalization that affects otherwise supported topology.

Do not claim the pre-mutation prerequisite has been satisfied merely because the matrix has 36 rows. Every required assignment and normalization must actually be supported and any required Product decision governed. If that standard is not met, deliver the completed research and the precise remaining gap—not fabricated completeness.

### 6. Engineering boundary and use of the answer

The engineer will use this evidence to repair the existing HDE-EPIC040 design, not enlarge its scope. The pinned six-unit HDE-SEPA005 family remains the scope; later HDE-SEPA006 work is excluded. The approved whole-change Plan and review remain historical records until any correction is made through the applicable workflow. This research creates no new approval.

For orientation, the engineering work is divided as follows. You are supplying domain evidence, not being asked to perform these tasks:

| Unit | Architecture that the engineer must make implementable |
| --- | --- |
| PR01 — Catalog and strict contracts | Exact source-supported catalog rows; strict adopted mechanics/result contracts; compatibility with retained metadata and FE/BE schemas; affected validators and primary-before-derived canonical writers in the correct PR. |
| PR02 — Validated immutable inputs | Parsing, schema execution, duplicate rejection, path/hash/source closure, deep immutability, Gate ingress and distinct local/candidate versus active-release admission. |
| PR03 — Canonical pure mechanics and identity | One four-argument Gate-based core; complete Channel-state/signal/category pipeline; adopted integer rounding and bands; identity and deterministic, pure behavior. |
| PR04 — Bounded application integration | Party eligibility and orientation, current callers, internal results and numeric-free bands-only Reader projection; no new public surface or rescoring. |
| PR05 — Comparison and Gate readiness | All eight adopted goldens at the correct layer; exact comparison; negative tests; read-only readiness inspection with no implied live-readiness result. |
| PR06 — Complete release and evidence | Complete promoted manifests, same-root evidence, canonical writers and active-release integration; no partial release advertised as complete. |
| PR07 — Final documentation | Documentation of delivered interfaces, examples, evidence, recovery and limits after PR01–PR06. |
| OPS01 — Final clean-candidate verification | Separately authorized external attestation of the unchanged final candidate after documentation; no implied deployment or QA authority. |

The engineer must also correct already-identified instruction errors independently of this research: zero is valid for the adopted `none` response; profile response maps retain their required nesting; PR ownership and acceptance mappings must be correct; and unresolved factual dependencies must not be passed off as implementation-ready design.

Your answer supplies evidence, not permission to mutate a catalog, schema, projection, repository or Canon document. It does not approve any PR, execute tests, create a pull request, authorize Proceed, merge, deploy, perform Ops/QA or select another session.

---

End of research prompt.
