## **0\. Front Matter — Document Control**

## **0\. Front Matter — Document Control**

Title: PF03-Reference-Technical Writing Best Practices  
 Version: v1.0.4  
 Status: Reference  
 Effective date: 2025-11-29

Last Update Gate: BN 7.8.9 Drain A27  
 Invocation tag: INV-f2ac55d77ce9aacc

Scope (titles-only)  
 Writing norms, placement rules, redline style, Build Notes usage, registry hygiene, and acceptance for documentation work. Bytes/transport live in PF05 (CLI/API/Vendor); governance tokens and A-gates live in PF04; math/thresholds live in PF01; architectural single homes live in PF02.

Tagging legend  
 • \[Implemented\] — guidance in force and reflected across PF docs  
 • \[Required-Now\] — edits demanded in the current cycle  
 • \[Speculative\] — proposals held for later review

Change policy (summary)  
 • Single homes; do not duplicate content owned by other PF docs.  
 • Cross-references are by document title only; do not include version numbers in cross-doc prose.  
 • Evidence discipline: when PF03 changes, update the human Evidence Index and the machine JSONL mirror in the same PR.

Paste-safe & canonicalization notes  
 • Sections must be Google-Docs-safe (no outer bold wrappers; blank line after headings; no empty bullets).  
 • Governed JSON artifacts referenced from PF03 comply with §4 (UTF-8, sorted keys, compact, single LF).  
 • Markdown headings only. Emit H1/H2 using `#` and `##`. Place one blank line after each heading. Do not wrap headings in bold.  
 • No code fences unless requested. Return paste-ready body text without triple‑backtick fences unless the PO explicitly asks for code blocks.

*Provenance:* Front matter synced to PF03 baseline and updated per “PF03: Editorial Quality Controls for Canonical Redlines” addendum.

## 

## 

## **1\) Purpose & scope**

Purpose. Make every document change reproducible, reviewable, reversible, and easy for AI agents to apply.

Scope. Writing norms, placement rules, redline style, Build Notes usage, registry governance, and acceptance for documentation work. Routing is titles-only: transport and payload bytes live in PF05; governance tokens and A-gates live in PF04; math and thresholds live in PF01; architectural single homes live in PF02.

Out of scope. Implementations, runtime payloads, transport headers, and any byte-level specs owned by other PF documents.

## **2\) Roles & audience**

Primary audience. AI technical writers (Cyrano lineage) and the PO who pastes outputs.

Readers. Lead Devs (AI, read only), human SMEs, and the PO.

Maintainers. The PO is the source of truth for approvals and version bumps; Cyrano maintains paste-safe edits, deltas, and Evidence Index entries.

Consumers. Other PF docs and build tooling that rely on PF03 for redline style, placement precision, and acceptance tokens.

## **3\) Governing doctrine (what never changes)**

Single home per truth — MUST. Each rule lives in exactly one PF doc; other docs link by title only. Do not include version numbers in cross-doc prose.

AI-first granularity — SHOULD. Prefer small, purpose-built docs to a single omnibus; keep drift low and routing clear.

Deterministic artifacts — MUST. Every doc cut includes version, date, status, changelog, invocation tag, and provenance. Paste-safe formatting is required.

Evidence parity — MUST. Update the human Evidence Index and the machine JSONL mirror in the same PR; maintain 1:1 parity.

Full-document requirement — MUST. Obtain and read the complete source before editing; proceed in partial mode only with explicit PO approval and label outputs as Partial.

H1/H2 invariance — MUST. Do not add, remove, or renumber H1 or H2; new sections require PO approval and must not shift existing numbering.

Whole-block fidelity — MUST. When a section (or contiguous range) is supplied for revision, return the complete revised block, including all subordinate headings and content, preserving order and anchors. Do not omit or truncate sub-sections.

No duplicated bytes — MUST. Do not copy architecture, transport, headers, or schema bytes across documents; route by title to the single home.

No shelf assumptions — MUST. Work only from attached files or canvas outputs in this chat; a website may mirror for humans, not as source of truth.

Section precision — MUST. Always cite Doc §Section numbers and exact anchors for placement.

Canonical references — MUST. Serialization, arrays-as-sets, and locale pins route to §4; generate and validate under `LC_ALL=C`.

Titles-only routing — MUST. PF05 (transport/CLI/vendor), PF04 (governance), PF01 (math), PF02 (architecture) are owners; PF03 does not duplicate their content.

---

## **4\) Operating mode for AI writers**

No background work. Deliver paste-ready outputs in chat; do not imply future actions.

One-lane updates. Small, revert-friendly diffs with exact placement and clear acceptance markers (tokens listed at the end of each change).

Titles-only references. Never paste canon text from one PF into another; link by document title and § only; do not include version numbers in cross-doc prose.

Evidence parity. When a section is updated, update the human Evidence Index and the machine JSONL mirror in the same PR; maintain 1:1 parity.

Paste-safe by default. Headings stand alone (blank line after), no outer bold wrappers, no empty bullets; produce Google-Docs-safe text.

Markdown headings & no fences. Emit section headings with `#`/`##` and a single blank line after each. Do not use code fences in redlines unless explicitly requested by the PO.

Determinism pins. Generate under `LC_ALL=C`; no wall clock, randomness, or floats; results must be reproducible byte-for-byte when rendered to governed artifacts.

## **5\) PF doc architecture (homes)**

PF02 — HDE Architecture. Single-emitter rule and single-homes map; architecture boundaries and ownership.

PF04 — Governance & Process Handbook. Acceptance, transport/A7 proofs, operational rails, FE/BE responsibilities.

PF01 — HDE Math & Technical Spec. Serializer and idempotence rules; evidence layouts and math semantics.

PF14 — HDE Mechanics Guide (Build Guide). Tasks only; points back to PF01 by title.

PF05 — HDE CLI-API-Vendor-Ref. CLI parity, flags, stdout invariants; Reader/transport shaping.

PF03 — Technical Writing Best Practices (this doc). Writing norms, placement rules, redline style, Build Notes usage, registry hygiene, and acceptance for docs.

PF12 — HDE Schemas & Artifacts. Catalogs, manifest, machine Evidence Index (JSONL), and seeds catalog governance.

PF10 — HDE Build Notes (Living). Append-only addenda blocks; drained each epic; carries invocation tag.

PF06 — Epic Process Guide. PR discipline; “update Evidence Index in the same PR” rule.

PF07 — Glow Infrastructure. Provider/environment maps and names-only runtime topology.

## **6\) Supersession & precedence**

When multiple versions compete, resolve in this order:

1. Explicit Supersedes (header field or PO-declared addendum).  
2. Status (Final \> Approved \> Review \> Revise \> Living/TBD).  
3. Effective date (latest wins).  
4. Version (semantic version comparison).

Applied rule. While a \[SUPERCEDES\] addendum is merge-ready and approved, it temporarily overrides prior guidance until merged; the change must update the human Evidence Index and the machine JSONL mirror in the same PR.

Clarifications. Cross-doc references are titles-only (no version numbers); precedence is decided at the document level, not by quoting older text from another PF.

# 

## **7\) Change workflow for docs (writer view)**

Input → Output loop

1. Intake. PO attaches a PF bundle (or single doc) and specifies target sections and intent.  
2. Normalize. Convert asks into `doc_delta[]` items with: id, severity, change\_type, source, status, and targets each carrying `{doc_title, section_anchor, op}` where `section_anchor = "§<num> <heading>"` and `op ∈ {ADD|REPLACE|DELETE|INSERT AFTER <heading>|INSERT BEFORE <heading>}`.  
3. Structure map. Extract H1 and H2 in order (H3 if relevant); attach as the Structure Map for this edit.  
4. Cross-reference sweep. Verify all cross-doc references are titles-only (no versions); list fixes to apply.  
5. Dependency-ordered plan. Produce a short, dependency-ordered list of sections to update (one-line rationale each); get PO approval.  
6. Draft. Produce paste-ready redlines with exact anchors and the verbatim text to paste; list the acceptance tokens affected.  
7. PO paste & confirm. PO pastes the redlines into the doc and confirms acceptance (or returns pinpoint edits).  
8. Registry & versioning. Update the doc registry (applied/withdrawn/pending), bump patch version, set Effective date, add a changelog line; ensure header/version parity with the registry.  
9. Evidence parity. Update the human Evidence Index (titles/paths only) and the machine JSONL mirror in the same PR/commit (1:1 parity).  
10. Drain Build Notes. If an addendum triggered the change, paste an Applied Slip or delete the block per delete-on-merge policy.  
11. Finalize. Store the delta report (summary and minimal \+/- lines) and risks; confirm H1/H2 preserved, titles-only cross-refs, and no duplicated bytes.

## **8\) Redlines & placement rules**

Always include (mandatory):

* Doc title; exact § number and heading; operation `ADD` / `REPLACE` / `DELETE` / `INSERT AFTER "<heading>"` / `INSERT BEFORE "<heading>"`; verbatim text to paste.

* Acceptance tokens added, changed, or removed (names only).

Never use vague locators (for example, “under acceptance,” “near the top”). If a target § does not exist, specify the parent § and the relative anchor (before/after a named heading).

**Placement anchors (precision):**

* Prefer a single unambiguous anchor such as `§X.Y → INSERT AFTER "<Subheading>"`.

* If a heading repeats, include the full path of headings (for example, `§8 → "Binary markers" (first occurrence)`).

* For multi-insert edits, enumerate numbered sub-operations (A, B, C or 1, 2, 3\) and state the anchor for each.

**Operation tokens (normative):**

* `ADD`

* `REPLACE`

* `DELETE`

* `INSERT AFTER "<heading>"`

* `INSERT BEFORE "<heading>"`

**Completeness & format (mandatory):**

* The verbatim text to paste includes the target section’s **own headings** in Markdown (`#`, `##`) so it can be dropped straight into the doc.

* Do **not** wrap headings in outer bold; leave one blank line after each heading.

* Do **not** use code fences in redlines unless the PO explicitly requests them.

* For contiguous range edits, emit the **entire** revised range (all included sub-sections), preserving order and anchors; do not silently drop or compress sub-sections.

**Example (good):**

* Place: `HDE-Governance §8 → INSERT AFTER "Binary markers — Implemented"` and before §9.

* Operation: `ADD` new `§8.4 "Caching & Keys (Reader) — MUST"`.

* Text: \<verbatim subsection, including the `§8.4` heading and body\>

* Acceptance impact: `READER_SUCCESS_ENDPOINTS_OK` added; `JSON_CANONICAL_CHECK_OK` unchanged.

  ## **9\) Build Notes (Living) usage**

Append-only blocks — MUST. The writer delivers a **self-contained Addenda Block**; the PO pastes it at the end under “Addenda (append-only)”.

Delete-on-merge — MUST. After the PF target is updated, the PO **deletes** the block (or archives by versioning the doc).

No in-doc edits by AI — MUST. AI lead devs are **read-only** for Build Notes; edits occur in the target PF.

Addenda Block (template)

### **\[\<NEW|SUPERCEDES|CONFLICT\>\] DD-\#\#\#\# — \<Short, action-based title\> — YYYY-MM-DDThh:mm:ssZ**

Severity: major|minor|critical · Change: add|modify|supersede|remove · Status: merge-ready  
 Targets:

* Doc:  
   Section: §  
   Summary (1–2 lines)  
* 

Proposed text (merge-ready)  
 \<Verbatim insert/replace for the target §.\>  
 Acceptance impact

* \<Markers added/changed/removed\>  
   Notes (optional)  
* Source: \<who/where\>  
* Dependencies:

  ## **10\) Registry governance (PF-RepoDocs-Inventory.json)**

Purpose. Machine index for PF docs and the doc-delta queue; the only index agents use.

Doc rules. JSON **MUST** be UTF-8, **sorted keys**, compact separators, **exactly one trailing LF**, no BOM.

Fields (minimum viable)  
 • `bundle`: `{name, sha256}`  
 • `pf_docs[]`: `{slug, title, status, version, file, sha256, single_home:"PF", owner:"Cyrano"}`  
 • `doc_map[]`: `{doc, group, precedence}` (routing aid)  
 • `doc_delta[]`: `{id, title, change_type, impact_zone, severity, source, status, targets[], applied_*|withdrawn_*}` where each target is `{doc_title, section_anchor, op}`  
 • `progress`: `{applied, pending, total}`  
 • `version`, `updated`, `invocation_tag`

Example (compact, sorted keys, with trailing LF)  
 {"bundle":{"name":"PF\_bundle\_2025-11-01.zip","sha256":""},"doc\_delta":\[{"change\_type":"add","id":"DD-0020","impact\_zone":"governance.transport","severity":"major","source":"Build Notes v6","status":"pending","targets":\[{"doc\_title":"PF04-Canon-HDE-Governance","op":"ADD","section\_anchor":"§8.6 Evidence minimums"}\],"title":"Evidence minimums pointer"}\],"doc\_map":\[{"doc":"PF04-Canon-HDE-Governance","group":"governance","precedence":1}\],"invocation\_tag":"INV-f2ac55d77ce9aacc","pf\_docs":\[{"file":"PF03-Technical Writing Best Practices v1.0.2.md","owner":"Cyrano 19","sha256":"","single\_home":"PF","slug":"PF03","status":"reference","title":"Technical Writing Best Practices","version":"v1.0.2"}\],"progress":{"applied":0,"pending":1,"total":1},"updated":"2025-11-01","version":"0.0.2"}

Acceptance (registry updates)  
 • `PF_REGISTRY_UPDATED_OK` — Entry added/modified with sorted keys, trailing LF.  
 • `DOC_DELTA_APPLIED_OK` — Delta moved to applied with `applied_in`, `applied_date`.  
 • `PF_SUPERSESSION_MATRIX_OK` — No conflicting homes after update.  
 • `PF_HEADER_INDEX_PARITY_OK` — Header (Title/Version/Status) matches registry entry.

## **11\) Evidence & acceptance for documentation work**

For each doc change, the deliverable includes:

11.1 Required artifacts — MUST

* Redline block with exact placement and verbatim text.  
* Changelog line and version bump for the target doc.  
* Provenance block in the target doc (version, date, invocation tag, editor, sources).  
* Registry update (delta→applied or withdrawn, plus progress bump).  
* Evidence parity: update the human Evidence Index (titles and paths only) and the machine JSONL mirror in the same PR (1:1).  
* Header–index parity check: header Title, Version, and Status match the registry entry.  
* Delta report: concise summary and minimal \+/- lines for the applied change.  
* Structure Map: complete list of H1 and H2 headings in order (H3 if relevant).  
* H1/H2 preservation proof: confirmation that H1/H2 text and order are unchanged.  
* Cross-reference sweep: confirm titles-only cross-refs; list any fixes applied.  
* Section deltas list: dependency-ordered list of updated sections with a one-line rationale each.  
* If from Build Notes: Addenda Block for paste, or confirmation to delete after merge (delete-on-merge).

11.2 Acceptance tokens (standard)

* DOC\_SECTION\_ANCHORED\_OK — precise § anchors provided.  
* DOC\_CHANGELOG\_BUMPED\_OK — changelog updated and version bumped.  
* DOC\_PROVENANCE\_PRESENT\_OK — machine-checkable provenance exists.  
* PF\_REGISTRY\_UPDATED\_OK — registry updated correctly.  
* DOC\_DELTA\_APPLIED\_OK — registry delta moved to applied with applied\_in and applied\_date.  
* PF\_HEADER\_INDEX\_PARITY\_OK — header matches registry (Title, Version, Status).  
* EVIDENCE\_INDEX\_UPDATED\_OK — human Evidence Index updated in same PR.  
* EVIDENCE\_MIRROR\_PARITY\_OK — machine JSONL mirror updated; 1:1 parity with human index.  
* DOC\_STRUCTURE\_MAP\_OK — structure map captured and attached.  
* H1H2\_PRESERVED\_OK — H1 and H2 text and order verified unchanged.  
* CROSSREF\_TITLES\_ONLY\_OK — all cross-doc references are titles-only.  
* NO\_DUPLICATED\_BYTES\_OK — no contract bytes duplicated across documents.  
* DOC\_SECTION\_DELTAS\_OK — dependency-ordered section deltas provided.  
* DOC\_RISKS\_NOTED\_OK — risks and open issues recorded.

  ## **12\) Communication rules (writer ↔ PO)**

Single paste-ready messages — MUST. CRDs, asks, and approvals are paste-ready; no partial promises or background work.

Two-block reply format — MUST. “Logically formatted update” then “Detailed delta report,” nothing else.

Titles-only references — MUST. Never embed version numbers in prose; keep titles stable. Use document titles and § anchors only.

Crisp, testable language — MUST. Use RFC 2119 terms (MUST/SHOULD/MAY) and tie claims to acceptance tokens.

Paste-safe by default — MUST. Headings stand alone (blank line after), no outer bold wrappers, no empty bullets; text should be Google-Docs-safe.

Pinpoint requests — SHOULD. PO provides the exact section text to edit; writer returns exact “Place / Operation / Text” redlines.

Minimal questions — SHOULD. Ask only what blocks precision; otherwise proceed and mark unknowns **\[OPEN\]**.

Error reporting — MUST. If a tool/canvas action fails, state the failure plainly and supply the paste-ready content or JSON alternative.

Escalation — SHOULD. If doctrine conflicts, cite governing PF titles and § numbers; propose the smallest corrective redline.

Determinism in thread — MUST. Keep terms, tokens, and headings consistent inside a session; do not rename mid-flow.

### **12.1 Engineering docs / QA plans (Live QA pattern)**

Engineering docs such as Live QA plans are action lists, not narratives. When the PO asks for a Live QA plan, the writer MUST treat it as a mechanical script that another person or agent can run without interpretation.

Live QA plans MUST follow these patterns:

* One command per step. Present the plan as a numbered list where each step is a single, copy-pasteable command string (for example, a `bash` invocation or CLI call). Describe any needed context (environment, directory, preconditions) before or after the command, not interleaved inside it.

* One primary artifact per command. For each step, name at least one expected evidence artifact (for example, a file path, log, or bundle) that the command produces. State this next to the step so the relationship is explicit.

* Mechanical evidence only. Copy the exact command text and path names that will appear in the repo or QA tree. Avoid paraphrasing commands or artifact locations; the plan must match what will actually be executed.

* PF-canon citations by title and section. When a step relies on a rail, token, or behavior defined in PF-canon (for example, determinism env helpers or ownership of QA tokens), cite the governing document by title and § anchor in the plan. Do not include version numbers or quote older text; routing is titles-only.

* Separate mechanics from interpretation. Keep the step list purely mechanical. Any narrative interpretation, retrospective, or ADR commentary belongs in a short notes block after the steps or in a separate doc (for example, epic closeout or Build Notes), not interleaved with the commands themselves.

These rules apply only to how Live QA plans are written and presented. They do not redefine where rails, tokens, or behaviors are owned in PF-canon; those remain in their existing single-home documents.

## **13\) Security & privacy for writing**

* No secrets in examples — MUST. Redact or use obvious placeholders; never paste API keys, cookies, or bearer tokens.  
* Keys-only logs in examples — MUST. Never show raw PII or secrets; summarize with names-only.  
* Local only — MUST. Do not imply writes to repos or external systems; all outputs are paste-ready text.  
* Evidence artifacts — SHOULD. Names/paths only in PF; bytes live outside PF and follow §4 canonical JSON rules.

  ## **14\) “Run-this-now” (writer’s quick path)**

1. Confirm the latest PF bundle (or changed file) is attached and named in the registry.  
2. Create `doc_delta[]` items with precise `section_anchor` (Doc § and heading) and `op` (ADD|REPLACE|DELETE|INSERT AFTER|INSERT BEFORE).  
3. Draft paste-ready redlines with exact anchors, verbatim text, and the acceptance tokens impacted.  
4. Deliver in two blocks: “logically formatted update” then “detailed delta report.”  
5. On PO confirmation, prepare the registry update snippet (header–index parity check: Title/Version/Status match).  
6. Evidence parity in the same PR: update the human Evidence Index (titles/paths only) and the machine JSONL mirror (JSONL records).  
7. If the change originated in Build Notes, hand the Addenda Block for paste or the delete-on-merge instruction.  
8. File the short delta report (summary and minimal \+/- lines) and close.

## **15\) Templates**

### **15.1 Standard PF header**

Title:  
 Version: vX.Y.Z  
 Status: \<Final | Approved | Review | Living\>  
 Effective date:  
 Last Update Gate: \<Epic/Decision ID\>  
 Invocation tag: \<INV-…\>

**Provenance (machine-checkable)**  
 `{"author":"","sources":"","invocation_tag":"<INV-…>"}`

---

### **15.2 Redline block**

Place: § → \<relative anchor, e.g., after “Binary markers …”\>  
 Operation: `ADD` | `REPLACE` | `DELETE` \<§ or heading\>

Text: *(Paste-ready; include the target section’s headings in Markdown `#`/`##`; one blank line after headings; no code fences unless requested.)*

**Note:** For contiguous-range edits, include the **entire** revised range (all sub-sections), preserving order and anchors.

Acceptance impact: \<TOKENS\_ADDED | TOKENS\_CHANGED | TOKENS\_REMOVED\>

---

### **15.3 Build Notes Addenda Block**

See §9 for the Build Notes Addenda template and usage.

## 

## **16\) Changelog**

v1.0.3 \- 2025-11-17 Tightened TW quality controls: updated front matter (v1.0.3 metadata, invocation tag), added paste-safe rules for Markdown H1/H2 and “no fences unless requested,” strengthened §3 governing doctrine with whole-block fidelity, extended §4 operating mode with explicit heading/fence rules, clarified §8 redlines & placement rules (mandatory anchors, completeness and format), and hardened §15 templates (PF header \+ redline block) to require headings-included, paste-ready text and full-range redlines.

v1.0.2 \- 2025-11-01 Standardized header and provenance; adopted Appendix A (Full Document Assessment Protocol); added doctrine pins (full-document requirement, H1/H2 invariance, no duplicated bytes); expanded §7 workflow; expanded §11 evidence and tokens; strengthened §12 communication rules; updated §14 quick path and §15 templates; enforced Evidence Index \+ JSONL mirror parity; added registry/header parity token.

v1.0.0 \- 2025-10-09 Initial comprehensive, AI-first best-practices: single-home doctrine, Build Notes append-only blocks, precise § anchors, registry governance, acceptance tokens, and paste-ready templates.

## Appendix A — Full Document Assessment Protocol (Technical Writing)

Purpose & Scope

Ensure every edit starts from the complete document, preserves heading structure, and keeps cross-document references synchronized by title only.

Applies to all Glow documentation families (PF Canon, Review, Living). PF03 remains titles-only and process-owned; bytes live in their single homes.

Policy (normative)

Full-document requirement — MUST. Obtain and read the complete source before editing. If only a fragment is available, pause and request the full doc; proceed in partial mode only with explicit PO approval and label outputs as Partial.

H1/H2 invariance — MUST. Do not add, remove, or renumber H1 or H2. New sections require PO approval and must not shift existing numbering.

Titles-only cross-references — MUST. Use stable document titles only; do not include version numbers in cross-doc prose. Section names are allowed.

No duplicated bytes — MUST. Do not copy architecture, transport, headers, or schema bytes across docs; route by title to the single home.

Style and naming hygiene — SHOULD. Plain English; avoid em dashes; keep heading formatting consistent; always spell the brand as Glow; use RFC 2119 terms carefully.

Evidence discipline — MUST. Provide acceptance evidence and maintain parity between the human Evidence Index and the machine JSONL mirror in the same PR.

Workflow

Intake → Structure map → Cross-reference sweep → Dependency-ordered update plan → Edit → Verification → Doc-delta and index → Closeout.

1\. Intake and inventory: confirm family and status; record invocation tag, date, and source path.

2\. Structure map extraction: list all H1 and H2 in order (H3 if relevant); attach as evidence.

3\. Cross-reference sweep: locate all cross-doc pointers; convert to titles-only; note corrections.

4\. Dependency-ordered update plan: list sections to update with a one-line rationale each; get PO approval.

5\. Editing: use the requested authoring surface; preserve H1/H2 exactly; keep changes minimal and localized.

6\. Verification: confirm H1/H2 preserved; confirm titles-only cross-refs; confirm no duplicated bytes.

7\. Doc delta and index upkeep: produce a doc-delta snippet; update the registry and both Evidence Indexes in the same PR.

8\. Closeout: provide artifacts, hashes where applicable, and a one-paragraph summary of changes and risks.

Acceptance & Evidence

To accept an edit for this protocol, the writer provides:

DOC\_STRUCTURE\_MAP\_OK — structure map captured and attached.

H1H2\_PRESERVED\_OK — H1 and H2 text and order verified unchanged.

CROSSREF\_TITLES\_ONLY\_OK — all cross-doc references are titles-only.

NO\_DUPLICATED\_BYTES\_OK — no contract bytes duplicated across documents.

DOC\_SECTION\_DELTAS\_OK — dependency-ordered section deltas provided.

DOC\_RISKS\_NOTED\_OK — risks and open issues recorded.

Templates

Structure Map

Document: \<Title\>

Collected: \<YYYY-MM-DD\>

H1

1\. \<Title\>  

2\. \<Title\>


H2

1.1 \<Title\>

1.2 \<Title\>

2.1 \<Title\>

2.2 \<Title\>

Dependency-ordered update plan

1\. \<Section anchor\> — \<Change summary\>  

2\. \<Section anchor\> — \<Change summary\>


Rationale: \<Why this order\>

Verification checklist

\[ \] H1/H2 preserved

\[ \] Titles-only cross-refs

\[ \] No duplicated bytes

\[ \] Doc delta prepared

\[ \] Registry and Evidence Index updated

