# PF03 exact redlines from v1.8.7

Run: `gtwpe-20261009-pf10-v13-5`; task: `T-PF03`; package: `T-PF03/PREP-1`.
Target: `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.7.md`.
Original: main `e7265a090ad0cc8de5f36de2f19481216aa3d073`; Git blob `27a66aefde14e10e75cb8ed1d6d226a099f0d1b8`; raw UTF-8 SHA-256 `cb123d2134b634c64589c1e193ef41a0bb5045f5d0b3fc85a8ff2cd3336399f3`.
Originating preparer: Nathan-started T-PF03 document session (this conversation); executing role /root. Stable ChatGPT conversation ID and title are not exposed.
Preparation date: 2026-10-09. Exact prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Every operation is original-bound. Literal payloads preserve their shown newlines; the final newline before a closing fence is a display delimiter, not an extra payload byte. `OLD byte count` and `NEW byte count` disambiguate terminal newlines. Read each payload to that exact UTF-8 byte count.
Document-control metadata is reserved for TW-APPLY-10: v1.8.7 to v1.8.8; Reference status; actual application date; Last Update Gate `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md`. No content change-history entry is required by PF03.

## RL-001

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **2\) Roles & audience**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[1552, 1613)`.
Source-ledger rows: `A38`, `S12`.
Rationale: Express functional actor terminology as a writer-facing instruction while retaining exact labels, provenance, capability limits and the existing non-editorial boundaries.
OLD byte count: `61`. NEW byte count: `881`.

OLD literal:
````text
The primary audience is AI agents producing PF documentation.
````

NEW literal:
````text
The primary audience is AI agents producing PF documentation.

Describe an assigned actor, audit, or prompt by its function when a current source gives that function governance standing. Use functional terms such as executing agent, repository audit, Implementation Agent, and implementation prompt; do not make a provider, product, model, or effort level part of the assignment unless the current task explicitly supplies it as an execution choice. Preserve the source-established role, session, permission, and evidence boundaries.

Preserve exact product-bearing field names, controlled vocabulary values, machine identifiers, and historical or provenance text when their spelling matters. A product-specific capability statement describes that product; establish another agent's required capabilities from actual task evidence instead of assuming the same access or limitation.
````

## RL-002

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **3\) Governing editorial principles**` > `## **Truth and source fidelity**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[3139, 3326)`.
Source-ledger rows: `A29`, `A30`, `S12`.
Rationale: Make complete reading apply to the assigned full units, preserving the retrieval-failure rule and source-faithful scope instead of requiring unrelated whole-source drainage.
OLD byte count: `187`. NEW byte count: `604`.

OLD literal:
````text
Read every relied-on source completely. A cutoff, missing chunk, malformed table, unmatched fence, incomplete block, or passage ending mid-unit is a retrieval failure, not source content.
````

NEW literal:
````text
Read the complete target and each complete source unit required by the assigned scope. For selected addenda or sections, verify their current source identity and read each unit through its actual boundary, including subordinate content, tables, notes, and necessary cross-references. Search for relevant governing material rather than loading unrelated canon. Supporting reading resolves meaning or ownership; it does not expand the assigned change scope.

A cutoff, missing chunk, malformed table, unmatched fence, incomplete block, or passage ending mid-unit is a retrieval failure, not source content.
````

## RL-003

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **3\) Governing editorial principles**` > `## **Canonical ownership**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[4519, 4653)`.
Source-ledger rows: `A30`.
Rationale: Preserve generic stable-anchor routing while stating the selected title-only exception for Build Notes.
OLD byte count: `134`. NEW byte count: `433`.

OLD literal:
````text
Add a section anchor only when the owning document establishes a stable, exact anchor and the reference materially improves retrieval.
````

NEW literal:
````text
Add a section anchor only when the owning document establishes a stable, exact anchor and the reference materially improves retrieval.

A PF document other than PF10-HDE-Build-Notes names that document by title only. Do not append an addendum number, section, heading, paragraph, version, or other internal locator. Resolve relevant Build Notes authority by the current topic and scope rather than following an old numbered citation.
````

## RL-004

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **5\) Canonical ownership and cross-document routing**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[11329, 11638)`.
Source-ledger rows: `A29`, `A30`.
Rationale: Align the ownership-reading method with complete governing units and current identity; retain the five-step routing boundary and prohibition on duplicated contracts.
OLD byte count: `309`. NEW byte count: `378`.

OLD literal:
````text
1. Retrieve the candidate owning source completely.  
2. Confirm its exact in-document title.  
3. Read its scope and the complete content relied upon.  
4. Determine whether that content actually establishes ownership of the point.  
5. Route the reader by exact title without reproducing the owned contract.
````

NEW literal:
````text
1. Resolve the candidate owning source's current identity and retrieve the complete units needed to establish ownership.  
2. Confirm its exact in-document title.  
3. Read its scope and the complete content relied upon.  
4. Determine whether that content actually establishes ownership of the point.  
5. Route the reader by exact title without reproducing the owned contract.
````

## RL-005

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **6\) Source precedence in documentation**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[12459, 14079)`.
Source-ledger rows: `A08`, `A29`, `S12`.
Rationale: Update writer-facing source resolution and source roles, retaining the existing precedence list and separating a canonical Build Notes entry from permanent drainage elsewhere. No storage operation or process contract is assigned.
OLD byte count: `1620`. NEW byte count: `2301`.

OLD literal:
````text
Apply each source only within the role it can prove.

1. The current operator instruction controls the requested output, editable scope, and authorized editorial changes.  
2. The complete supplied target controls its existing bytes, terminology, structure, and section boundaries.  
3. The current topic-owning canon controls externally governed requirements within its demonstrated scope.  
4. PF10-HDE-Build-Notes controls a point only when a complete, exact addendum explicitly addresses that point.  
5. One identified repository snapshot controls observed checked-in repository reality at that snapshot.

An operator instruction may authorize a rewrite or output form. It does not authorize unsupported factual claims.

The target document remains authoritative for its valid existing content unless a more authoritative allowed source explicitly supersedes the exact point.

PF10-HDE-Build-Notes may record decisions, clarifications, staging, history, or drainage intent. It does not independently prove current implementation or permanent canon.

Do not combine competing source versions or silently harmonize conflicting statements. Use an explicit current designation, supersession statement, governing-source resolution, or Product Owner decision.

Do not select a source merely because its filename, date, or version appears later. If the current source cannot be resolved uniquely, request the smallest necessary selection.

When a supplied source and a repository copy differ, identify the split whenever it affects the wording or conclusion. Do not represent supplied-only content as repository content.


````

NEW literal:
````text
Apply each source only within the role it can prove.

For PF writing, resolve current controlled PF text from `docs/pfcanon/` on `main`, record the actual path and repository snapshot, and retain each document's declared standing. A native document, external copy, navigation page, or PF-named file outside that location is not a substitute for the current controlled source.

Retrieve a change-process input by its actual repository path in `docs/ephemeral/`. Preserve whether it is an approved Specification, a working Plan, a review decision, or another source type. Attribute historical external copies as historical sources; do not give a pointer or board entry the authority of the controlling file.

1. The current operator instruction controls the requested output, editable scope, and authorized editorial changes.  
2. The complete supplied target controls its existing bytes, terminology, structure, and section boundaries.  
3. The current topic-owning canon controls externally governed requirements within its demonstrated scope.  
4. PF10-HDE-Build-Notes controls a point only when a complete, exact addendum explicitly addresses that point.  
5. One identified repository snapshot controls observed checked-in repository reality at that snapshot.

An operator instruction may authorize a rewrite or output form. It does not authorize unsupported factual claims.

The target document remains authoritative for its valid existing content unless a more authoritative allowed source explicitly supersedes the exact point.

PF10-HDE-Build-Notes may record decisions, clarifications, staging, history, or drainage intent. It does not independently prove current implementation or drainage into another permanent PF document.

Do not combine competing source versions or silently harmonize conflicting statements. Use an explicit current designation, supersession statement, governing-source resolution, or Product Owner decision.

Do not select a source merely because its filename, date, or version appears later. If the current source cannot be resolved uniquely, request the smallest necessary selection.

When a supplied source and a repository copy differ, identify the split whenever it affects the wording or conclusion. Do not represent supplied-only content as repository content.


````

## RL-006

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **9\) Writing PF10-HDE-Build-Notes content**` > `## **Source selection and citation**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[20177, 21619)`.
Source-ledger rows: `A29`, `A30`.
Rationale: Replace whole-version reading and external numbered-citation instructions with current scoped-source reading and title-only PF references, retaining overlap, source-split and historical-identity protections.
OLD byte count: `1442`. NEW byte count: `1861`.

OLD literal:
````text
Resolve and retrieve the complete latest active PF10 base version before relying on an addendum. Use its complete unlettered document or its complete lettered document set in established order. Do not read, reuse, compare, reconcile, or carry forward content from an older base version.

For a lettered set, verify the continuous addendum sequence across every member before treating the set as complete.

Treat an addendum as relevant only to the topic its complete text explicitly addresses.

Search every document in the complete active PF10 version for all addenda relevant to the current topic. Determine each addendum’s actual scope from its complete heading and substantive content. When addendum scopes overlap, apply only the highest-numbered applicable addendum to the overlapping scope. Continue applying lower-numbered addenda only to distinct scope not superseded by the higher-numbered addendum.

Reference an addendum by its exact addendum number and title. Do not use a document version or document letter as the durable external anchor.

If supplied Build Notes content differs from the repository copy, state the source split when it affects the authored conclusion. Do not describe supplied-only text as repository-drained canon.

Preserve published addendum identities. If a historical heading is inaccurate, clarify the corrected identity in later prose when supported. Do not silently rewrite the historical heading.


````

NEW literal:
````text
Resolve the current active PF10 base version from `docs/pfcanon/` on `main`. Use one logical version: its unlettered document or its contiguous lettered set in established order. Do not mix representations or carry forward an older version as current authority.

For a selected-addenda assignment, verify each selected addendum's identity and complete heading-to-next-heading boundary, including any continuation across parts, and read it in full. Inspect source inventory and part metadata as needed to establish that identity. Read the whole logical source only when the assignment requires whole-source coverage.

Search the current logical version as needed to identify governing material for the topic. Determine applicability from complete scope and substantive content, not an old number, index summary, or filename. For overlapping scopes, apply the later applicable rule only to the overlap and retain lower-numbered rules for distinct unsuperseded scope. Identify necessary unselected dependencies as supporting reading; do not turn them into additional drainage.

In a PF document other than PF10-HDE-Build-Notes, cite Build Notes by its exact in-document title only. Do not use its addendum number, section, heading, paragraph, version, or another internal locator as a durable reference. Build Notes addenda may cite other Build Notes addenda. Historical records keep their original wording and provenance; their citations are not rewritten as current guidance.

If supplied Build Notes content differs from the repository copy, state the source split when it affects the authored conclusion. Do not describe supplied-only text as repository-drained canon.

Preserve published addendum identities. If a historical heading is inaccurate, clarify the corrected identity in later prose when supported. Do not silently rewrite the historical heading.


````

## RL-007

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **9\) Writing PF10-HDE-Build-Notes content**` > `## **Output**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[22500, 22614)`.
Source-ledger rows: `A08`, `S12`.
Rationale: Add the selected page-ready authoring instructions as presentation and claim-posture rules, without creating subject-matter authority or authorizing publication.
OLD byte count: `114`. NEW byte count: `1184`.

OLD literal:
````text
Follow the complete current Build Notes structure required by the target. PF03 does not define an addendum schema.
````

NEW literal:
````text
Follow the complete current Build Notes structure required by the target. PF03 does not define a substantive addendum schema.

For an agent-authored addendum, apply the source-established page-ready form: one H2 heading with the next continuous addendum number and a descriptive title; subordinate headings at H3 or deeper. Resolve the current number and format before writing. Include a source-supported unique identifier or distinguishing metadata in the title when needed for retrieval and lineage.

Write the addendum's subject matter directly: supported decisions, requirements, status effects, exceptions, scope boundaries, nonclaims, evidence anchors, dependencies, consequences, and unresolved work. Use declarative present tense for a durable decision while preserving distinctions among completed work, future work, recommendations, exclusions, and unproven facts.

Keep role-addressed handling, publication, routing, and record-maintenance instructions out of the addendum. Planning, rescoping, escalation, and other addendum genres use the same canonical writing posture; the authored text is complete enough to stand on its own page without external procedural narration.
````

## RL-008

Operation: `REPLACE`.
Change type: `CLARIFY` / `CONSISTENCY`.
Target document: `PF03-Reference-Technical-Writing-Best-Practices`.
Section path: `# **12\) Communication and document-genre rules**` > `## **Task, plan, and execution-document writing**`.
Expected original literal block count: **1**. Observed: **1**. Original byte span: `[30828, 31040)`.
Source-ledger rows: `A14`, `S12`.
Rationale: Use current Specification terminology and route permanent-record formatting to its owner without reproducing a record template, schema, approval workflow or process gate in PF03.
OLD byte count: `212`. NEW byte count: `1089`.

OLD literal:
````text
PF03 governs the clarity and truthfulness of plans, runbooks, remediation documents, and execution instructions. It does not define their domain templates, workflow, acceptance criteria, or operational authority.
````

NEW literal:
````text
Use CRD Specification and Epic Specification for the permanent scope records; distinguish them from an Implementation Plan's working direction and a kickoff's transient scaffolding. Preserve an actual historical artifact's identity and wording when reporting its provenance.

When writing a Specification or a Specification delta, retrieve the current owning permanent-record format and cite the resolved owner by exact title and supported section. Do not derive its structure or schema identifier from a prompt-local outline, a neighbouring artifact, a retired `glow-specification` or `glow-kickoff` token, or the superseded thirteen-section structure. A kickoff or Implementation Plan may use the producing prompt's authorized format. If the governing format cannot be resolved and read, report that source-resolution blocker instead of authoring against an assumed format.

PF03 governs the clarity and truthfulness of plans, runbooks, remediation documents, and execution instructions. It does not define their domain templates, workflow, acceptance criteria, or operational authority.
````

END OF REDLINES
