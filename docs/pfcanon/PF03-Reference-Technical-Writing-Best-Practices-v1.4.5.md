## **0\) Front Matter — Document Control**

**Title:** PF03-Reference-Technical-Writing-Best-Practices

**Version**: v1.4.5

**Status:** Reference

**Effective date:** 2026-04-19

**Last Update Gate:** BN 10.5.7 A35

**Invocation tag:** INV-f2ac55d77ce9aacc

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
 • No code fences unless requested. Return paste-ready body text without triple-backtick fences unless the PO explicitly asks for code blocks.

*Provenance:* Front matter synced to PF03 baseline and updated per “PF03: Editorial Quality Controls for Canonical Redlines” addendum.

## **1\) Purpose & scope**

Purpose. Make every document change reproducible, reviewable, reversible, and easy for AI agents to apply.

Scope. Writing norms, placement rules, redline style, Build Notes usage, registry governance, and acceptance for documentation work. Routing is titles-only: transport and payload bytes live in PF05; governance tokens and A-gates live in PF04; math and thresholds live in PF01; architectural single homes live in PF02.

Out of scope. Implementations, runtime payloads, transport headers, and any byte-level specs owned by other PF documents.

## **2\) Roles & audience**

Primary audience. AI technical writers (Cyrano lineage) and the PO who pastes outputs.

Readers. Lead Devs (AI, read only), human SMEs, and the PO.

Maintainers. The PO is the source of truth for approvals and version bumps; TW sessions maintain paste-safe edits, deltas, and Evidence Index entries.

Consumers. Other PF docs and build tooling that rely on PF03 for redline style, placement precision, and acceptance tokens.

## **3\) Governing doctrine (what never changes)**

Single home per truth — MUST. Every rule or schema has one canonical home. Other documents may reference it, but must not restate or fork it.

No duplicated bytes — MUST. Do not copy architecture, transport, headers, or schema bytes across documents. Route by title to the single home.

Titles-only cross references — MUST. When referencing another PF document, refer to it by title only (no version numbers, no deep links unless the target doc defines them as stable).

Heading numbering stability — MUST. Heading numbers are immutable. New content should be added as H3/H4 within an existing H2 whenever possible. If a new H1 or H2 is truly required, it must take the next available number and must not renumber existing headings.

Acceptance tokens (name \+ semantics) single source of truth — MUST. Acceptance token names and their semantics are defined once in the Governance & Process Handbook token registry. Any token name used in epic acceptance rosters, QA token libraries, acceptance maps, or evidence logs MUST match registry spelling exactly.

Legacy spelling / alias handling (acceptance tokens) — MUST. If any PF consumer doc contains legacy spellings for a token family, the epic must normalize to the token registry spelling and record the normalization as a doc delta. Effective immediately: `QA_STEP_LOGS_CONSOLIDATED_OK` is treated as a deprecated doc-only alias for `QA_HARNESS_DISCIPLINE_OK`; acceptance artifacts MUST claim `QA_HARNESS_DISCIPLINE_OK` and MUST NOT claim `QA_STEP_LOGS_CONSOLIDATED_OK`.

Ellipsis prohibition in canonical docs and plans — MUST. Canonical documents and plans MUST NOT contain the ASCII triple-dot sequence or the Unicode ellipsis character. Use one of these approved replacement markers instead: `[OMITTED]`, `[OMITTED: <short reason>]`, `[SNIP: <n> lines omitted]`, `[REPEAT BLOCK]`, `[LIST CONTINUES]`, or `<PLACEHOLDER_NAME>`.

Prohibited-character enforcement (mechanical blocker) — MUST. In plans and in plan-review outputs, treat any occurrence of the prohibited ellipsis patterns as a mechanical blocker. If the prohibited pattern appears in a relied-on excerpt, treat it as a read failure and re-open or re-extract until the excerpt can be represented without prohibited characters (or represent the excerpt using an approved omission marker).

Literal-string fallback — MUST. If a literal string must be preserved and cannot be represented without violating the prohibition, do not embed it in the plan or redline. Place the literal string in a repo file and reference the file by exact path and filename.

Inline-code rendering — SHOULD. When presenting inline code-like literals in narrative text, prefer double quotes or prefix with `CODE:` to keep the plan copy/paste safe without requiring forbidden characters.

Evidence path binding authority order — MUST. HDE Schemas and Artifacts is the source of truth for canonical artifact paths and governed artifact naming for evidence families. HDE Mechanics Guide must not introduce alternate canonical paths. Glow QA Guide defines check execution semantics and status vocabulary. HDE Build Checklist declares which checks and gates are required, but those checks must bind to the canonical surfaces and paths.

Machine Evidence Index mirror home (names-only) — MUST. The canonical Machine Evidence Index mirror is `artifacts/evidence_index.jsonl` with companion `artifacts/evidence_index.jsonl.sha256`. Governed path-proof transcripts are sibling files using the suffix `.path_proof.txt` (do not use `.path_proof.json`). Any other mirror path strings (including `artifacts/evidence/machine_mirror.json` or any `docs/evidence/` path that includes `machine_mirror` in its filename) are non-canonical and must be treated as doc drift until drained.

Acceptance map path-of-record (names-only) — MUST. Epic acceptance maps are bound to `docs/acceptance_map_epic<NNN>.json` with a sibling `docs/acceptance_map_epic<NNN>.json.path_proof.txt`.

Evidence Index snapshot (D23) is tokenless — MUST. The D23 Evidence Index snapshot is a mechanical PASS or FAIL contract suitable for QA closure proof. It MUST NOT be represented as an acceptance token claim.

Planning MUST consult PF23 and tie QA plan milestones back to epic gates.

PF23 is a closed-epic snapshot — MUST. PF23 Reality Audits are updated at epic close and reflect the latest closed-epic snapshot, not an in-flight PR truth source.

PF23 consult scope (planning vs PR analysis) — MUST. PF23 (Reality Audits) MUST be consulted during planning (epic, implementation, QA), and MUST NOT be consulted for PR analysis, remediation review, or diff-first loops. PR analysis is grounded in the PR diff and the owning PF canonical homes for the surfaces under review.

PF23 consult is non-token — MUST NOT. PF23 consult MUST NOT appear as an acceptance token, required deliverable, or required check in a plan.

Documentation drainage is never an execution or acceptance gate — MUST. PF10 drainage and any later documentation drainage into PF04, PF06, PF07, PF09.x, PF12, PF19, PF27, or any other canon, checklist, guide, or summary home are never prerequisites, required deliverables, required checks, acceptance conditions, readiness conditions, or blockers by themselves.

Allowed blockers remain truth and proof only — MUST. Incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR, FAIL\_TOOLING, or TOOLING\_BLOCKED conditions that affect acceptance, and missing required close-gate QA artifacts remain real blockers. Documentation drainage itself is not a blocker.

PF10 is the temporary live-truth home until drain — MUST. If a canon delta or documentation correction is known but not yet drained, follow the live PF10 truth and governed evidence rather than waiting on drain.

Record first, drain later — MUST. When a documentation mismatch or canon delta is found during planning, implementation, QA, review, or closeout, record it as a follow-up, implementation gap, ADR note, or doc-delta item. Do not convert undrained documentation into a prerequisite, deliverable, check, or blocker solely because the destination PF document is not yet updated.

No artifact may require its own drainage to stand — MUST NOT. Plans, implementation guides, QA plans, review artifacts, remediation guides, closeout reports, acceptance maps, token-evidence matrices, step logs, OPS tasks, PR summaries, and epic artifacts may note later drain targets or future documentation work, but must not require that drainage already be completed for the current artifact’s verdict or recommendation to be valid.

No plan may mandate PF document updates as execution outputs — MUST NOT. Plans may reference future doc deltas or drain targets, but must not require PF document edits as tasks, deliverables, acceptance items, or completion conditions for PR work, OPS work, QA execution, step completion, or closeout readiness.

Supportable versus drained wording — MUST. If repo evidence supports a status change or canon statement that has not yet been drained, say so explicitly using supportable-from-repo-evidence language and do not imply that drain already happened.

Drain-required wording is non-conforming — MUST NOT. Wording such as "drain required before close", "cannot pass until PF10 is drained", "not ready because canon is not yet drained", or "PF update required before acceptance" is non-conforming and must be corrected.

PF23 contradiction posture — MUST. When PF23 contradicts PF canon, record the contradiction as a drift item (with both quotes) and route to PO adjudication. Do not resolve the contradiction by assumption inside the plan or the plan review.

Canonical references — MUST. When a PF doc references another PF doc, it must point to title (and stable section if defined as stable). Do not point to commit hashes, PR numbers, or mutable URLs as canonical references.

Documented dev and QA access default — MUST. In plans, implementation plans, QA plans, remediation guides, reviews, runbooks, example commands, and inline documentation, the default documented client access address for a non-prod local or local-style surface is `127.0.0.1` plus the correct port and endpoint path.

Access convention is not service identity — MUST. This documented default does not redefine provider, project, service name, canonical config key name, or real deployment identity.

Prod-facing surfaces stay explicit — MUST. Production and other prod-facing surfaces must continue to use the real hosted service URL or other real infrastructure address recorded in the owning canon. They must not be rewritten to `127.0.0.1` for superficial consistency.

Client access address, service identity, and server bind address are separate — MUST. Documentation must not collapse those concepts casually.

No guessed exceptions — MUST NOT. If a dev or QA surface truly cannot be reached at `127.0.0.1` from the intended operator context, the document must state the explicit exception and the real access route. Do not use guessed hostnames, guessed forwarded URLs, or placeholder wording.

`localhost` is no longer the preferred canonical example host for new or revised canon-aligned dev and QA documentation.

This normalization does not authorize invented ports, invented endpoints, invented config keys, or invented start commands.

Whole-block fidelity — MUST. When proposing redlines, replace or insert whole blocks. Avoid partial-sentence edits that change meaning.

Full-document requirement — MUST. Obtain and read the complete source before editing; proceed in partial mode only with explicit PO approval and label outputs as Partial.

Paste-safe formatting is required. Use markdown that can be copy-pasted and renders correctly.

Evidence parity — MUST. Update the human Evidence Index and the machine JSONL mirror in the same PR; maintain 1:1 parity.

---

## **4\) Operating mode for AI writers**

No background work. Deliver paste-ready outputs in chat; do not imply future actions.

One-lane updates. Small, revert-friendly diffs with exact placement and clear acceptance markers (tokens listed at the end of each change).

Titles-only references. Never paste canon text from one PF into another; link by document title and § only; do not include version numbers in cross-doc prose.

Evidence parity. When a section is updated, update the human Evidence Index and the machine JSONL mirror in the same PR; maintain 1:1 parity.

Paste-safe by default. Headings stand alone (blank line after), no outer bold wrappers, no empty bullets; produce Google-Docs-safe text.

Markdown headings & no fences. Emit section headings with `#`/`##` and a single blank line after each. Do not use code fences in redlines unless explicitly requested by the PO.

Determinism pins. Generate under `LC_ALL=C`; no wall clock, randomness, or floats; results must be reproducible byte-for-byte when rendered to governed artifacts.

OPS tasks posture — MUST. If a work item requires privileged access outside the repository (service config, secrets/env var changes, deploy/runtime settings, infra consoles, privileged DB operations), it is an OPS task. OPS tasks MUST be executed by the PO only. Automated agents MUST NOT attempt execution, MUST NOT claim completion, and MUST NOT simulate external state changes. Any doc that includes OPS tasks MUST separate them from PR work and MUST specify evidence capture as repo-stored, secret-free artifacts under lowercase audit paths (for example, `audit/`

## **5\) PF doc architecture (homes)**

PF02 — HDE Architecture. Single-emitter rule and single-homes map; architecture boundaries and ownership.

PF04 — Governance & Process Handbook. Acceptance, transport/A7 proofs, operational rails, FE/BE responsibilities.

PF01 — HDE Math & Technical Spec. Serializer and idempotence rules; evidence layouts and math semantics.

PF14 — HDE Mechanics Guide (Build Guide). Tasks only; points back to PF01 by title.

PF05 — HDE CLI-API-Vendor-Ref. CLI parity, flags, stdout invariants; Reader/transport shaping.

PF03 — Technical Writing Best Practices (this doc). Writing norms, placement rules, redline style, Build Notes usage, registry hygiene, and acceptance for docs.

PF12 — HDE Schemas & Artifacts. Catalogs, manifest, machine Evidence Index (JSONL), and seeds catalog governance.

PF10 — HDE Build Notes (Living). Append-only addenda blocks; drained each epic; carries invocation tag.

PF09 phased checklist set. The retired single-document PF09 is not an active reference surface. Documentation, planning, reviews, and future work must reference the relevant phased PF09 document or documents, identified as PF09.1 through PF09.7. If a clarification is needed because one phased PF09 document is thin or cross-phase context is ambiguous, place that clarification in the appropriate phased PF09 document rather than routing back to the retired single-document PF09.

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

## **7\) Change workflow for docs (writer view)**

Input → Output loop

1. Intake. PO attaches a PF bundle (or single doc) and specifies target sections and intent.  
2. Normalize. Convert asks into `doc_delta[]` items with: id, severity, change\_type, source, status, and targets each carrying `{doc_title, section_anchor, op}` where `section_anchor = "§<num> <heading>"` and `op ∈ {ADD|REPLACE|DELETE|INSERT AFTER <heading>|INSERT BEFORE <heading>}`. If the source input is an audit or drift list, also produce a Doc Delta Map (single sink) that maps each finding ID to its `doc_delta[]` item IDs and any required follow-up tasks.  
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

* Acceptance impact: `READER_SUCCESS_ENDPOINTS_OK` added; **9\) Build Notes (Living) usage**

Append-only blocks — MUST. The writer delivers a **self-contained Addenda Block**; the PO pastes it at the end under “Addenda (append-only)”.

Delete-on-merge — MUST. After the PF target is updated, the PO **deletes** the block (or archives by versioning the doc).

No in-doc edits by AI — MUST. AI lead devs are **read-only** for Build Notes; edits occur in the target PF.

PF10 reference posture — MUST. When referencing Build Notes from other documents or reviews, reference Build Notes by **addendum number \+ addendum title** (for example, “Build Notes Addendum 2.10 — Token Load Reduction \[OMITTED\]”). Do not reference PF10 by version strings or PF10 section numbers as durable anchors; the stable unit is the addendum entry itself.

Addenda Block (template)

### **\[\<NEW|SUPERCEDES|CONFLICT\>\] DD-\#\#\#\# — \<Short, action-based title\> — YYYY-MM-DDThh:mm:ssZ**

Severity: major|minor|critical · Change: add|modify|supersede|remove · Status: merge-ready  
 Targets:

* Doc:  
   Section: §  
   Summary (1–2 lines)

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

### 11.1 Required artifacts — MUST

* Redline block with exact placement and verbatim text.  
* Changelog line and version bump for the target doc.  
* Provenance block in the target doc (version, date, invocation tag, editor, sources).  
* Registry update (delta→applied or withdrawn, plus progress bump).  
* Evidence parity: update the human Evidence Index (titles and paths only) and the machine JSONL mirror in the same PR (1:1).  
* Dual-home clarification: governed evidence bytes remain in their canonical homes (for example under audit/), while docs may provide indexes and anchors (titles and paths only) that point to those artifacts for discoverability and review. Do not duplicate full artifact bytes into docs to satisfy discoverability.  
* Header–index parity check: header Title, Version, and Status match the registry entry.  
* Delta report: concise summary and minimal \+/- lines for the applied change.  
* Structure Map: complete list of H1 and H2 headings in order (H3 if relevant).  
* H1/H2 preservation proof: confirmation that H1/H2 text and order are unchanged.  
* Cross-reference sweep: confirm titles-only cross-refs; list any fixes applied.  
* Section deltas list: dependency-ordered list of updated sections with a one-line rationale each.  
* If from Build Notes: Addenda Block for paste, or confirmation to delete after merge (delete-on-merge).

### 11.2 Acceptance tokens (standard)

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

## 

### 11.3 Docs-only PR evidence posture (minimum) — MUST

* Docs-only PRs MUST capture at least one verification proof line in PR artifacts when updating documentation.

* Minimum acceptable proof (choose one):

  * A markdown sanity check output (command and pass indicator line).

  * A doc lint output (command and pass indicator line).

* If the docs-only change asserts contract-level strings (token strings, endpoint lists, exit/error identifiers, or owned path lists), the PR analysis record MUST state how each assertion was verified (evidence pointer, repo search, or test output) or record the assertion as unverified under DOC\_RISKS\_NOTED\_OK.

* If no proof is recorded in PR artifacts, the PR analysis record MUST:

  * State that no CI/test proof is recorded.

  * Include the search method used to verify absence (where searched and strings searched).

  * Record the gap under DOC\_RISKS\_NOTED\_OK and request follow-up capture.

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

QoS stop-rule for repeated structural remediation — MUST. If the same structural failure mode recurs after one corrective pass, stop incremental plan edits and escalate to a root-cause correction by updating the controlling template or canon rule, then rerun the authoring pass. Drain targets MUST describe the failure class, not the incident.

Determinism in thread — MUST. Keep terms, tokens, and headings consistent inside a session; do not rename mid-flow.

### 12.1 Engineering docs / QA plans (Live QA pattern)

Engineering docs such as Live QA plans are action lists, not narratives. When the PO asks for a Live QA plan, the writer MUST treat it as a mechanical script that another person or agent can run without interpretation.

Live QA plans MUST follow these patterns:

* One command per step. Present the plan as a numbered list where each step is a single, copy-pasteable command string (for example, a `bash` invocation or CLI call). Describe any needed context (environment, directory, preconditions) before or after the command, not interleaved inside it.

* One objective-first directive per step. Present the plan as a numbered list where each step states its objective and directive. Plans MUST NOT be required to provide verbatim, syntax-perfect command lines.  
* One objective-first directive per step. Present the plan as a numbered list where each step states its objective and directive. Plans MUST NOT be required to provide verbatim, syntax-perfect command lines.  
* Mechanical evidence only. Step PASS and FAIL decisions must be grounded in artifacts and paths. Where command details matter, require the execution transcript (step log or generator output listed as a Deliverable) rather than embedding brittle commands in the plan.

* PF-canon citations by title and section. When a step relies on rails, tokens, or a canon rule, cite the governing PF document by title and § anchor in the plan. Do not include version numbers.  
* Separate mechanics from interpretation. Keep the step list purely mechanical. Any narrative interpretation, retrospective, or ADR commentary belongs in a short notes block after the steps or in a separate doc (for example, epic closeout or Build Notes), not interleaved with the steps themselves.

These rules apply only to how Live QA plans are written and presented. They do not redefine where rails, tokens, or behaviors are owned in PF-canon; those remain in their existing single-home documents.

### 12.2 Tool runs & FAIL\_TOOLING in QA plans

For QA plans, steps that say “run this tool/script” (for example, a sanity pipeline) are only useful if they define what it means for the tool to have actually run and been observed. Extend the §12.1 pattern as follows:

* Run-evidence definition — MUST. For every “run this tool/script” step, the plan MUST state what evidence shows that the tool ran. This can be a specific log file path, a named section inside a step log, or explicit pass/fail lines that the operator should see. Without this, the step is underspecified.

* No-output classification — MUST. If the operator follows the step as written (including any reasonable reruns requested by the plan) and the expected evidence remains completely absent (no log section, no pass/fail lines, no error output), the outcome MUST be classified as a tooling or harness failure, not as a QA execution or application behavior failure. Use a distinct status marker such as `FAIL_TOOLING` in the step log to make this explicit.

* **Stream-silent success is not the same as no-output failure — MUST.** If a command emits no stdout or stderr but another authoritative artifact proves successful execution, the plan MUST not automatically classify the step as `FAIL_TOOLING`.  
* **Required governed output logs must remain non-empty — MUST.** When the plan requires a governed output log under the stable check root, the plan MUST define a minimal non-empty capture rule for stream-silent success rather than allowing a zero-byte log.  
* **Authoritative success artifact must be named — MUST.** The plan MUST state which artifact remains authoritative for success or failure when the governed output log is only a sentinel capture, such as the rc file, primary log, or structured result file.  
* **Sentinel text must be factual and minimal — SHOULD.** The sentinel should say only that the command produced no stdout or stderr and name the authoritative success artifact. It should not add narrative interpretation or duplicate the PASS or FAIL claim.  
* **Review posture for stream-silent success — MUST.** Reviewers must judge the step from the authoritative success artifact plus the non-empty sentinel capture, not from the empty stream alone.  
* Stop and escalate, do not grind — MUST. Once a step is clearly in a `FAIL_TOOLING` state (no evidence after multiple correct attempts), the QA plan MUST instruct the operator to stop re-running the same command, append a short failure summary to the step log, and escalate by opening a follow-up task/bug. Plans SHOULD NOT ask the operator to repeat an unchanged command indefinitely when the harness is not producing evidence.

* Separation from behavior verdicts — SHOULD. Behavior-level verdicts (for example, claims about application correctness) MUST NOT be asserted when the underlying tool or harness has not produced any evidence of running. In this case, the only honest summary is that the step is blocked on tooling, and behavior remains unproven for that run.

* Status vocabulary — MUST. Step logs MUST use the canonical status vocabulary defined in the Glow QA Guide and MUST distinguish tooling failure from behavior failure. Do not introduce ad-hoc execution statuses for core step state.

These conventions keep Live QA plans mechanical, fair to the operator, and honest about the difference between “the app failed” and “our harness is not capturing the run.”

### **12.3 Command and procedure style (QA plans)**

* **Prefer directive-first steps — MUST.** Live QA steps SHOULD be written as objective-first instructions, not as speculative implementation narratives.

* **Discovery-first posture — MUST.** A Live QA Plan MUST assume that any repo detail not proven is unknown until discovered during the run.

* **No inferred repo-resident loci — MUST NOT.** Do not infer, fill in, pattern-match, or scaffold repo-resident locus strings or app-topology claims. If a plan names a repo-resident locus or an exact command string, it MUST be copied verbatim from an allowed provenance source or recorded as a discovered runtime fact in step evidence.

* **Command-line minimalism — MUST.** Plans MUST NOT over-specify command lines. State the goal, the observable outputs that matter, and the evidence that must be captured.

* **Runtime command capture — MUST.** The executor MUST record the exact commands actually used into the check evidence.

* **No speculative placeholders — MUST NOT.** Do not use placeholder routes, placeholder file paths, placeholder module names, placeholder commands, or “if it exists under X” scaffolding.

* **Avoid “run this somewhere” prose — MUST.** Specify repo-root relative paths and deterministic file locations for plan-created outputs and check-scoped evidence.

* **No `<PO_INPUT>` placeholders in step lists — MUST.** If PO input is needed, include it in a dedicated “PO inputs” section.

* **Environment bootstrapping — MUST be explicit.** If the procedure requires environment bootstrapping, explicitly reference the standard bootstrap script and run the enforcement inside a subshell (for example, `bash -lc "<SUBSHELL_COMMAND>"`).

* **Check-scoped evidence paths — MUST.** If evidence is generated, specify stable check-scoped paths under `audit/qa/<epic-id>/checks/<check_id>/` and list exact files created.

* **Approval gate — MUST.** Any plan that includes inferred repo-resident loci, speculative topology claims, invented helper scripts, or unproven exact command lines MUST be returned for revision.

### **12.4 QA runbooks & evidence documentation (Live QA)**

Live QA plans and Live QA runbooks are engineering docs. They must be runnable, discovery-led, auditable, and free of hand-edited evidence.

Apply these rules in addition to §12.1–§12.3, §12.12, and §13.1:

* **PF23 consult in QA planning — MUST.** PF23 (Reality Audits) is a required, read-only input during QA planning and QA plan review when repo-reality context or locus framing is needed. QA plans and QA execution MUST NOT require PF23 edits; PF23 maintenance remains PO-only.

* **Repo-resident locus provenance lock — MUST.** In QA planning artifacts, the only allowed provenance sources for repo-resident locus claims are HDE Build Notes, PF-Canon, and the initial QA Audit for the epic.

* **Verbatim-only repo-reality claims — MUST.** If a repo-resident locus string is used, it MUST be copied character-for-character from an allowed provenance source. Do not invent, infer, normalize, paraphrase, or fill in repo-resident locus strings.

* **Unknown loci are handled by discovery, not by placeholders — MUST.** If a required repo-resident locus is not proven at planning time, the plan MUST state the discovery intent, the discovery acceptance, the evidence that will record the discovered locus verbatim, and the BLOCKED condition if discovery cannot resolve the ambiguity without guessing.  
* **Per-step dependency posture — MUST.** Any Live QA step that depends on a command-line tool, interpreter, module, environment activation, or helper binary MUST name the exact dependency set for that step.  
* **Dependency preflight before behavior — MUST.** Before the main behavior command runs, the step MUST define the explicit preflight check or checks that prove each required dependency is present and runnable.  
* **Activation or installation action when allowed — MUST.** If the execution venue allows activation or installation, the step MUST state the exact activation or installation action to take when dependency preflight fails.  
* **Unknown remediation is a tooling block — MUST.** If the plan cannot truthfully specify the activation or installation action, it MUST say so and classify unresolved dependency readiness as `FAIL_TOOLING` or `BLOCKED` rather than as a behavior failure.  
* **Dependency readiness evidence — MUST.** The preflight result, any activation or installation action taken, and the final ready or not-ready outcome MUST be captured in the step’s governed evidence.  
* **Shared bootstrap does not remove step responsibility — MUST NOT.** A shared bootstrap step does not eliminate per-step dependency posture. Each later step MUST either restate the required dependency preflight or explicitly depend on the bootstrap step and include a short step-local readiness check before the main command.  
* **Dependency posture omission is structural incompleteness — MUST.** If a pytest-backed or other tool-backed Live QA step omits its dependency set, preflight command or commands, or remediation posture from the approved QA Plan, the plan is structurally incomplete and must be returned for revision before approval.  
* **Execution-time correction does not erase the plan defect — MUST.** If a later accepted run adds a step-local dependency preflight or remediation action that the approved plan omitted, reviews and closeout summaries must preserve both truths: the step may still PASS if its evidence is sound, and the plan still had a structural omission.  
* **Bounded rerun branches must record rerun basis — MUST.** If a step may use a bounded Moon Loop or other approved rerun branch, the plan or later deliverables report MUST record the approval requirement, the rerun basis, any rails exception, and the governed artifact that captures the actual executed command sequence.  
* **Stream-silent rerun artifacts still follow the named-success-artifact rule — MUST.** When a bounded rerun relies on a successful but stream-silent governed artifact, the plan MUST name the authoritative success artifact and require the non-empty sentinel capture described in §12.2.  
* **Step-level Deliverables — MUST.** Every step in a QA plan or Live QA runbook MUST include a **Deliverables** list that names the minimal evidence set for that step using fully qualified, check-scoped file paths under the stable epic QA root (for example, under `audit/qa/<epic-id>/checks/<check_id>/`).  
  * If the step creates new evidence, Deliverables MUST name the files that will be created.

  * If the step only reads existing artifacts, Deliverables MUST still name the files being read and state that no new files are created.

* **Plan-created outputs are allowed and expected — MUST.** When a plan requires creating a file (script, report, manifest, log, capture, or other on-disk artifact), the plan MUST name the exact repo-relative path and filename, include runnable creation instructions, and state why the file is required.

* **Plan-created scripts are constrained — MUST.** A plan MUST NOT invent or assume helper scripts exist. If a plan-created script is required, it MUST be minimal, purpose-bound to the deliverable, and created at the exact repo-relative path named in the plan.

* **Provenance labeling posture — SHOULD.** The plan SHOULD label mentioned files as repo-resident or plan-created. Missing labels are non-blocking only when the file is clearly run-produced and the plan already provides exact path, creation instructions, and purpose.

* **PASS/FAIL/BLOCKED defined by files and discovery — MUST.** Each step’s PASS, FAIL, and BLOCKED criteria MUST be defined in terms of its Deliverables and any required discovery evidence. Avoid vague criteria like “looks good” or “works”; the step verdict must be reviewable from the listed files.

* **Gitless runbooks — MUST.** Live QA runbooks MUST NOT include git gating (including “working tree clean”) as PASS/FAIL criteria. If traceability capture is needed, it MUST be artifact-only and non-blocking.

* **No manual-fill placeholders — MUST NOT.** No QA evidence file may include “fill in PASS/FAIL” or other manual-entry placeholders. If a result is “no deltas,” the generator MUST emit that explicitly as produced output.

* **No manual edits to QA evidence — MUST NOT.** QA plans and runbooks MUST NOT instruct an operator to open evidence files (logs, manifests, reports, or READMEs) in an editor and type changes by hand. If a summary must change, the correct procedure is to rerun the generator so the result remains reproducible.

* **Step log header inputs — MUST.** If a plan step relies on a governed step log (for example `primary.log`) as a Deliverable, the plan MUST ensure the log is generated by the harness and includes its machine header. If the header writer depends on env var inputs, the plan MUST export the required canonical env vars in the step context (not as an ambient global). Missing required exports is a mechanical blocker for claiming PASS based on that evidence.  
* **Bounded approved deviations must be recordable — MUST.** If a step may require a bounded approved deviation from the default rails or execution posture, the plan MUST say who may approve it, what condition can trigger it, and which governed file records the approval.  
* **Default posture and executed posture must both be preserved — MUST.** The plan or later deliverables report MUST preserve both the default approved posture and the actual executed posture for that step. Do not collapse the deviation into the normal path or hide it inside narrative prose.  
* **Deviation scope stays step-local — MUST.** A bounded approved deviation for one step MUST remain tied to that step unless the plan is formally revised. Do not treat a step-local deviation as a blanket plan-wide change.

* **Deferred evidence labeling in templates — MUST.** Any QA plan template, deliverables report, closure record, or rollup that enumerates step-scoped evidence paths MUST explicitly label future-step artifacts as `NOT RUN` or `DEFERRED` until the producing step has executed.

* **Do not treat deferred artifacts as missing evidence — MUST.** When writing summaries, evidence prints, or rollups, `NOT RUN` and `DEFERRED` states MUST remain distinct from missing evidence findings. Do not describe `NOT RUN` or `DEFERRED` artifacts as missing evidence.  
* **Plan-conditional evidence is not missing evidence — MUST.** If a plan states that a deliverable is produced only when a named condition is met, QA summaries and evidence prints MUST record the artifact as `Not applicable` or `not required because condition not met` when that condition is not met. Do not report such artifacts as missing evidence.

* **Input-availability gates are planning defects when the plan becomes structurally unreachable — MUST.** If a step’s PASS criteria require inputs that are unavailable, invalid, or explicitly should not be expected for the current product state, the step MUST be described as blocked by an input-availability gate and treated as a planning defect or plan/product mismatch, not as a demonstrated behavior defect.

* **Rerun posture for planning defects — MUST.** In this situation, QA summaries MUST NOT prescribe a rerun as remediation unless the required inputs later become valid or the plan is corrected. Missing downstream artifacts caused solely by the blocked precondition MUST be interpreted in light of the planning defect.

* **Approval gate — MUST.** Any plan that contains an unproven repo-resident locus string or a required plan-created file without exact path, runnable creation instructions, and a stated reason MUST be returned for revision.

These are documentation rules only. They do not redefine token ownership or evidence semantics owned by other PF documents; they define how QA instructions and QA summaries must be written to remain auditable and reproducible.

### **12.5 Live QA plan approval reviews (BLOCKERS vs CAVEATS)**

For any review / approval step in Live QA plans

* Template adherence is structural only — MUST. In plan approval reviews, evaluate PF-template adherence only for structural completeness (required sections present, required gates present, and any required end marker present). Header styling and heading marker levels are not part of structural adherence.  
* Heading and formatting-only deltas are not approval conditions — MUST NOT. Reviewers MUST NOT request redlines that only change heading levels, add or remove bold or italics, or reformat headings when the meaning and executability are unchanged.  
* Minor formatting artifacts are non-blocking — MUST. Treat the following as presentation-only artifacts that MUST NOT block plan approval: escaped Markdown list markers, backslashes inserted for Markdown escaping, whitespace-only differences, bold or italics differences, bullet character variance, list indentation variance, and table layout variance. Record these as CAVEATS or optional follow-ups only.  
* **Display-layer escape artifacts are non-blocking unless proven source-real and materially harmful — MUST.** Visible escape characters that plausibly arise from AI processing, markdown rendering, display normalization, or retrieval formatting must not block approval by themselves.  
* **Rendered escape characters are not source truth — MUST.** Reviewers must judge the underlying source content, not the rendered display alone. A blocker based on escape characters is valid only when the characters are proven to exist in the source text and materially change meaning, runability, or proof posture.  
* **Re-open before blocking on escape characters — MUST.** If a relied-on passage may contain display-only escape artifacts, re-open or re-retrieve the source until raw-text truth is clear before issuing a blocker.  
* **Conforming review language — SHOULD.** Use wording such as "Rendered escape characters appear to be display artifacts only and are non-blocking" or "Approval is based on source meaning and runability, not markdown-safe rendering artifacts."  
* **Non-conforming review language — MUST NOT.** Do not block approval only because the rendered view shows backslashes or other markdown-safe escapes without proving that the source text itself is corrupted in a materially harmful way.  
* **BLOCKERS** (`BLK-01`, `BLK-02`, \[LIST CONTINUES\]): any item that prevents execution of the plan or invalidates the run.  
* **CAVEATS** (`CAV-01`, `CAV-02`, \[LIST CONTINUES\]): risks, uncertainties, assumptions, or optional improvements that do not block execution.  
* **Prohibited ellipsis patterns are mechanical blockers — MUST.** Treat any occurrence of the Unicode ellipsis character (U+2026) or the ASCII triple-dot sequence as a BLOCKER in plan approval reviews. Replace with approved omission markers or move the literal string into a repo file and reference it by exact path and filename.  
* **Heading marker levels are non-reviewable — MUST NOT.** Reviewers MUST NOT block approval based on heading marker levels or require heading-level changes as a condition of approval. Review required sections by the heading text and required content, not by the markdown level.  
* **Non-blocking plan formatting variance — MUST.** Formatting variance that is purely presentation (bullet marker choice, indentation, line wrapping, extra blank lines, tables vs bullets, emphasis style) is not a blocker. Record such notes as CAVEATS or follow-ups only.  
* **Formatting becomes a blocker only when it impacts meaning or execution — MUST.** Treat as BLOCKERS only when the variance causes missing required sections or fields, changes semantics, makes commands non-copyable, breaks step IDs or evidence filenames, or otherwise prevents safe execution and evidence capture.  
* **QA prompt mode declaration — MUST.** Any QA prompt or QA-related request MUST declare its mode as `AUTHORING` or `REVIEW` before the body.  
* **No cross-mode mixing — MUST.** The response MUST follow the mode’s required structure and MUST NOT blend `AUTHORING` content (runbooks, new commands, new steps) into `REVIEW` outputs (evidence evaluation and verdict), or vice versa.  
* **Step-local approved deviation review posture — MUST.** If a step later passes using a bounded approved deviation from the default plan posture, reviewers MUST keep the step verdict separate from the planning defect or caveat created by the missing or unplanned branch.  
* **Do not rewrite proved PASS as behavior failure — MUST NOT.** When governed evidence is trustworthy and the stated PASS criteria are met, do not convert the step into behavior failure solely because the deviation had to be approved during execution.  
* **Deviation record requirements in review — MUST.** The review MUST state the default approved posture, the actual executed posture, the approval source, the reason for the deviation, the evidence path that records it, and whether the deviation is acceptable only for the named step.  
* **REVIEW-mode remediation exception — MUST.** If a `REVIEW` output requires remediation guidance, any command lines included MUST be copied verbatim from the approved plan or its caveats, and MUST be explicitly labeled as remediation-only.  
* **Mechanical enforcement of mode — SHOULD.** Workflows and harnesses SHOULD enforce mode with a required mode header token and a mode-specific required section list.

### **12.6 Tokens in Live QA plans (load reduction \+ registry validity)**

* Keep token usage minimal in Live QA plans. Prefer evidence artifacts \+ explicit checks over token proliferation.  
* If a token string is referenced in a consumer doc but is absent from the Governance & Process Handbook token registry, it MUST NOT be claimed as a requirement. Record CAVEAT: `UNREGISTERED_TOKEN` and treat as doc drift until drained.  
* Legacy alias exception (temporary; do not mint a new token): `QA_STEP_LOGS_CONSOLIDATED_OK` is treated as a deprecated doc-only alias for `QA_HARNESS_DISCIPLINE_OK`. Acceptance artifacts MUST claim `QA_HARNESS_DISCIPLINE_OK` and MUST NOT claim `QA_STEP_LOGS_CONSOLIDATED_OK`. If the alias appears in PF text, interpret it as `QA_HARNESS_DISCIPLINE_OK`, normalize to the registry spelling in acceptance artifacts, and record the normalization as a doc delta.

### **12.7 Repo reality execution posture (DOC\_DRIFT capture)**

Live QA must remain executable and evidence-producing even when canonical docs contain stale operational details (paths, filenames, script locations, or command shapes). If a canonical doc’s operational detail conflicts with repo reality, QA MUST:

* Use the repo-real invocation/paths to execute the checks and capture evidence.

* Record the mismatch as a CAVEAT: `DOC_DRIFT` (include the doc title and the mismatched detail) for later drain.

Do not block execution unless the mismatch prevents knowing what to run or how to verify.

Codespaces Live QA plans MUST include a Step-0 discovery snapshot and Doc Delta Capture step. The step MUST capture rails baseline and any required connectivity/prerequisite checks for the run environment. If no deltas are found, the step MUST record “no deltas” explicitly as produced output (not as a manual-fill placeholder).

### **12.8 Simplified QA planning and deterministic acceptance (plan boundaries)**

* **Canonical tokens only for acceptance — MUST.** Plans MUST express acceptance criteria only in terms of acceptance tokens defined in the Governance & Process Handbook token registry. If a plan needs a concept not covered by an existing token, it MUST be handled as an out-of-scope issue requiring an ADR to create or extend a token, not via invented local terms.

* **No stepwise QA in initial plans — MUST.** Epic Plans and initial Implementation Plans MUST NOT include step-by-step QA runbooks or Live QA execution scripts. These early plans should specify what will be proven (tokens and evidence outputs) and defer step-level execution detail to a later Live QA plan or runbook.  
* **Epic Plans must include a Business Case section — MUST.** Every Epic Plan MUST include a clearly labeled Business Case section that explains what the epic is solving (user pain plus benefit, not internal-only framing), why it matters (product value, user outcome, operational leverage), how to measure success (key outcomes or criteria), and what is explicitly not included (scope boundaries). This section MUST be readable by a non-technical stakeholder. If an Epic Plan lacks a Business Case section, or if the Business Case is purely technical and does not explain the product reason for the w**ork, the plan MUST be returned for revision before implementation work begins.**  
* **Epic Plans must include a Contract-change Justification section — MUST.** If the epic introduces or changes a user-visible contract (for example: a new flag, a new endpoint, a new output schema, a new file format, or a changed default behavior), the plan MUST explain why the contract change is required and how backward compatibility is preserved (defaults, opt-in gating, migrations, and any follow-up deprecation or migration plan, if applicable).  
* **Implementation planning must not require QA evidence production — MUST.** Implementation Plans and Implementation Guides MAY state QA objectives and closeout proof obligations, but MUST NOT require generating or attaching extensive QA evidence artifacts as part of the planning deliverable. Step-level QA execution and governed QA evidence production belong in the later Live QA plan and QA execution artifacts.

* **Ops tasks are not QA tasks — MUST.** Ops tasks are tracked and evidenced as implementation work, not QA work. Ops evidence MUST NOT be treated as a substitute for governed QA evidence.

* **Keep delivery streams distinct — MUST.** Planning artifacts MUST keep these categories distinct: implementation deliverables, ops tasks, QA planning, and QA execution (including evidence capture and indexing).

* **Evidence-bound scope for QA steps — MUST.** When a Live QA plan enumerates steps, each step MUST have explicit PASS and FAIL predicates and MUST identify the evidence output(s) it produces. For every token the plan intends to claim, the plan MUST name at least one step that produces the evidence needed for that token. Optional checks may be included only if explicitly labeled as informational (not acceptance).

* **Validated references, no guesswork — MUST.** Plans MUST NOT assert repo paths, filenames, or module loci without validation. If a locus cannot be validated at plan time, the plan MUST include an explicit discovery step that produces repo evidence and resolves the locus before implementation proceeds.

* **AI-safe review practices — MUST.** Reviews MUST prioritize correctness, executability, evidence binding, and token validity. Presentation-only formatting variance and heading marker levels are not approval gates (see §12.5).

* **Use standard playbooks — SHOULD.** When a standard playbook exists in the Glow QA Guide, plans SHOULD use it as the default source of steps and evidence. Deviations are allowed only when no playbook applies; deviations SHOULD be documented and proposed as playbook improvements.

### **12.9 Planning path discipline (no fabricated repo paths)**

* **No fabricated paths — MUST.** Any asserted repo path, directory root, or module locus in a plan MUST be validated. Unvalidated path assertions are mechanical blockers in plan review.

* **Allowed validation methods — MUST use exactly one:**

  * **Canon-cited:** a direct PF canon citation grounding the home or locus (PFxx — Title, §X.Y), with the relevant quoted line(s) included in the plan.

  * **CA vetted:** a verbatim quote from the planning Codex audit included inline in the plan.

  * **IG Approved:** a verbatim quote from the Implementation Guide included inline in the plan.

* **Quote discipline for CA vetted and IG Approved — MUST.** If a plan uses the labels CA vetted or IG Approved, the supporting material MUST be quoted verbatim inline in the plan. Paraphrase is not permitted for these labels.  
* **If validation is not available — MUST.** The plan MUST mark the locus as unknown and include a discovery step that produces repo evidence to resolve the correct path before implementation assumes it.  
* **Plan portability — MUST.** Plans may reference planning audits inside the plan narrative, but implementation prompts to Codex MUST NOT reference audits or attachments. Prompts must be self-contained and use only PF canon references and repo paths.  
* **PF07-derived or PF07-gap posture — MUST.** Any plan, implementation guide, QA plan, review artifact, remediation guide, or epic document that names an infrastructure or ops value must use one of only two postures: either the exact value is already present in PF07 and is cited or copied directly, or the exact value is missing from PF07 and the document marks the item blocked by missing PF07 infrastructure inventory.  
* **No external infra or ops placeholders — MUST NOT.** Do not write plans as if a separate infra or ops team exists outside this workspace and will provide missing values later. Do not leave executable steps dependent on vague external ownership, guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or bare placeholders presented as runnable inputs.  
* **Infra or ops task specificity — MUST.** When an infra or ops task is included, the document must name the concrete target facts that matter for execution and review, such as provider, project, service, repository, base URL or port, database instance or schema, config-key name, governed evidence root or QA root, and the exact value or the exact PF07 source for that value.  
* **PF07-gap blocker posture — MUST.** If PF07 is silent, the document must identify the exact missing PF07 facts, mark the affected task or claim as blocked by missing PF07 inventory, and record the intended PF07 update only as a drain target or doc-delta candidate for PO action.  
* **No guessed QA bindings — MUST NOT.** QA and Live QA documents must not guess or redefine environment bindings, service bindings, URLs, ports, project names, provider names, or canonical QA-root patterns that PF07 is meant to own.  
* **Review posture — MUST.** A plan or related document that refers to infra or ops work without PF07-backed values, or without an explicit PF07-gap blocker, is non-conforming and must be returned for revision.  
* **PF07 scope reminder — MUST.** This rule governs where documents obtain concrete infrastructure facts. It does not move transport policy, token semantics, schema rules, or runbook procedure into PF07.  
* **Environment variable discipline (no fabricated env vars) — MUST.** Any environment variable referenced in a plan, runbook, step instruction, or evidence schema MUST be canonical (repo-real or PF-canon named). Treat non-canonical env var names as mechanical blockers, equivalent to fabricated paths.  
  * **Ban `MODO_*` variables — MUST NOT.** `MODO_*` variables are non-canonical and MUST NOT appear in Glow/HDE docs. If present in legacy text, treat them as non-binding placeholders and propose deletion.  
  * **Exact spelling — MUST.** Refer to env vars only by the exact case and spelling defined by repo reality or PF-canon. Do not paraphrase, rename, or recase env vars.  
  * **Invalid env var references — MUST.** If a plan names an env var that does not exist in repo reality or PF-canon, treat it as an invalid reference and require correction (or a discovery step that validates the env var contract) before execution.

### **12.10 File minting procedure for new epics (canon-first validation)**

* **Minting is allowed — MUST remain canon-aligned.** Plans MAY create new files and directories under canon-defined homes. The control is not "no new files"; the control is "do not invent homes, roots, or paths."

* **Minimum canon consult before minting paths — MUST.** Before asserting a surface root, directory home, or module locus, the author MUST consult HDE Architecture and Reality Audits to ground the single-home posture and current repo reality.

* **New roots and second homes — prohibited by default.** A plan MUST NOT propose a new top-level surface root (or a second home for an owned component) unless it includes:

  * The canon alignment rationale (Architecture single-home posture).

  * A CA vetted quote showing the repo does not already contain an appropriate canonical root for the purpose.

  * An explicit statement of why existing canonical homes cannot be used.

* **Evidence file minting — MUST be deterministic.**

  * Plans MUST name the primary governed evidence outputs that will be committed and indexed for the epic or PR.

  * Plans SHOULD avoid vague family phrases and SHOULD avoid wildcards in evidence-output lines.

  * If a tool produces a high-churn set of member logs, the plan MAY treat a manifest or bundle as the single primary governed artifact, provided the plan names the primary artifact by exact path and filename and states that member files are referenced by that artifact.

* **Codex portability rule — MUST.** Final instructions given to Codex for implementation MUST NOT reference CA vetted, IG Approved, the planning audit, or any attachments. Prompts must be self-contained and use only PF canon references and repo paths.

### **12.11 Acceptance token minting and claim rules (no plan-local tokens)**

* **Token authority — MUST.** Token definitions and the canonical token registry are owned in the Governance & Process Handbook. Plans MUST NOT fork or invent token semantics locally.

* **Claims vs obligations — MUST distinguish.**

  1. A **token claim** asserts a specific acceptance token will be satisfied and is only valid when the token exists in the registry.

  2. An **obligation** is a plain-language requirement used when no suitable token exists yet. Obligations are not acceptance tokens and must not be written in token format.

* **No plan-local minting — MUST.** Plans MUST NOT mint new tokens locally. A plan may claim a token only if the token exists in the Governance & Process Handbook token registry or has been minted in HDE Build Notes.

* **Token spellings — MUST be exact.** Token claims MUST use exact token spellings; no aliases or local variants.

* **Evidence before claim — MUST.** Every token claim in a plan MUST name the evidence output(s) that will be produced for that token (exact paths and filenames where possible).

* **Token Inventory step — MUST.** Any plan that uses acceptance tokens MUST include a Token Inventory that lists:

  1. The exact token spelling to be claimed.

  2. Where it is defined (registry or Build Notes).

  3. The evidence output(s) that will support the claim.

* **When a new token is warranted — MUST follow the conservative workflow.**

  1. Confirm no existing token covers the concept (search the registry).

  2. Draft an ADR proposing the token definition and claimable evidence contract.

  3. If approved, mint the token in HDE Build Notes.

  4. Only after minting, update the plan to claim the token.

  5. Drain the minted token into the Governance & Process Handbook token registry.

* **Downstream document rule — MUST.** Documentation MUST NOT invent or reformat tokens. If a document references a token that is not present in the registry, record it as drift and use the unregistered-token caveat posture (see §12.6).

### **12.12 PF23 consult scope and drift assessment stub**

* **Planning-only consult — MUST.** PF23 (Reality Audits) MUST be consulted during:

  * Epic planning.

  * Implementation planning.

  * QA planning.

* **PR analysis exclusion — MUST NOT.** PF23 MUST NOT be consulted for PR analysis, remediation review, or diff-first loops. PR analysis is grounded in the PR diff and the relevant PF canonical homes for the surfaces under review.

* **Non-token posture — MUST.** PF23 consult is not an acceptance token, required deliverable, or required check.

* **No plan-mandated PF updates — MUST NOT.** Plans MAY require checking PF canon (and PF23) for grounding, but MUST NOT mandate updates to PF documents as required tasks, acceptance items, or deliverables.

* **Reality Audits updates are PO-only — MUST.** Updates to PF23 (Reality Audits) are a manual PO operation. Plans and PR scopes MUST NOT include edits to PF23 or claim that a PR will update PF23.

* **Doc delta capture note is optional and non-mandatory — MAY.** Plans MAY include a brief note listing possible doc delta candidates for PO review, but it MUST be explicitly non-mandatory and MUST NOT be framed as required work.

* **Plan review posture — MUST.** If a plan contains a required PF update task, treat it as a portability defect and return for revision.  
* **Drift assessment stub — MUST.** If PF23 contradicts PF canon:

  * Record the PF23 claim (quote).

  * Record the PF canon claim (quote, with title and § anchor).

  * Identify the impacted surface and locus.

  * Assign a tentative bucket: canon defect, implementation drift, or necessary reality shift.

  * Route to PO adjudication. Do not resolve by assumption in the plan or the plan review.

* **Routing for PR analysis — SHOULD.** When grounding PR analysis, route to the PF canon home that owns the domain under review (examples: HDE Architecture, Governance & Process Handbook, CLI/API/Vendor, HDE Schemas and Artifacts, HDE Build Checklist, HDE Mechanics Guide, Glow QA Guide, Epic Process Guide, HDE Build Notes).

  ### **2.13 Comprehensive PR review posture (multi-attempt, PF09 status posture, and later-drain statements)**

* **Multi-attempt review posture — SHOULD.** When a PR review depends on the cumulative result of an original PR plus one or more remediations, preserve the attempt chain explicitly and evaluate the final decision against cumulative branch truth rather than treating each attempt as a disconnected artifact.  
* **Lifecycle-grounded review summary — SHOULD.** A comprehensive PR review summary may describe how earlier attempt defects were corrected in later attempts, but it should separate attempt-specific defects from final-branch truth.  
* **Finding-source labeling — SHOULD.** In a comprehensive PR review, each finding should identify the source attempt or bundle when that source matters to the conclusion.  
* **Crosswalk-by-attempt — SHOULD.** When requirement satisfaction changes across attempts, the Requirement Satisfaction Crosswalk should record each attempt in chronological order with its status and evidence pointers instead of compressing the story into only original versus final state.  
* **Negative-claim proof — SHOULD.** If a review asserts that a prior drift item, diff, or scope leak is absent in a later attempt, record the search method and zero-hit result.  
* **Exact phased PF09 mapped unit controls — MUST.** If the reviewed work maps to an exact phased PF09 task or subtask, that exact mapped unit controls acceptability language and later-drain posture. Parent-summary language is not enough when an exact subtask exists.  
* **Multiple mapped phased PF09 units — MUST.** If one slice claims to close more than one phased PF09 task or subtask, each claimed mapped unit must be complete in substance and supportable for later drain before acceptable-status language is allowed.  
* **Current phased PF09 recorded status is not a pre-drain gate — MUST NOT.** Do not treat the status text currently recorded in phased PF09 as the closure gate, QA-entry gate, PR acceptability gate, or OPS acceptability gate.  
* **Live-truth acceptability posture — MUST.** Before drain, judge acceptability from approved implementation state, approved OPS state where applicable, governed evidence, truthful review and approval artifacts, and the live in-flight PF10 record where PF10 speaks.  
* **Approved-task scope controls review unit — MUST.** Review only the approved task in question and its explicitly approved scope. Do not widen the review to later PRs, later OPS tasks, later validation runs, or whole-epic closure work unless the approved task explicitly includes them.  
* **Non-closure steps are reviewed on their own approved job — MUST.** If the approved task is a bounded intermediate step, such as validation, gap classification, sequencing correction, evidence capture, or another explicitly non-closure step, judge the task on whether it truthfully and correctly completes that approved job.  
* **PF09 closure is not a gate for non-closure steps — MUST NOT.** If the approved task does not claim to bring a mapped phased PF09 task or subtask to closure, do not block, fail, or reject it solely because the mapped row remains open for later approved work.  
* **Closure gate applies only to closure-claiming tasks — MUST.** A phased PF09 closure gate applies only when the approved task explicitly claims that it brings a mapped task or subtask to Done, supports a Done recommendation now, or performs final closure, final binding, final acceptance promotion, or equivalent closure-claiming work.  
* **Review language must keep task acceptance distinct from row closure — MUST.** Distinguish task-level acceptance of the approved step from phased PF09 closure status of the mapped row.  
* **Same rule for OPS tasks — MUST.** A bounded OPS task may be accepted for truthful execution of its own approved purpose even when the mapped phased PF09 row remains open for later work.  
* **Allowed pre-close language — MUST.** If the mapped work is not yet complete in substance, use contributory, intermediate, review-clean, bounded, or supportable from repo evidence. Do not use acceptable, accepted, satisfied, complete-for-close, or supportable for later drain to Done until the mapped work is complete in substance and the live truth supports later drain.  
* **Current phased PF09 recorded status may be cited only as the current drained record — MUST.** It is evidence of canon-as-recorded, not proof that the work is still incomplete in substance.  
* **Real blockers remain real blockers — MUST.** Incomplete implementation work, incomplete OPS work, incomplete evidence, and execution ambiguity still block closure. Describe those as real blockers, not as PF09-text blockers.  
* **Later-drain PF-canon update statement — MUST.** Any PR final review, PR remediation acceptance review, OPS final review, final close-pack review, or other approval artifact intended to support later PF-canon drain must state the affected PF canon home or homes, the exact affected locator or locators, the current canon posture if established, the supported later-drain action, the drain readiness classification, the evidence basis, and the epic-close expectation.  
* **Supported later-drain action vocabulary — MUST.** Use exactly one supported later-drain action in the approval artifact: change to Done, change to Partial, change to Not done, change to Consolidation pending, change to Optional, or No status change recommended.  
* **Drain readiness classification vocabulary — MUST.** Use exactly one drain readiness classification in the approval artifact: Supportable from repo evidence, Not yet supportable from repo evidence, or Already drained into PF-canon.  
* **Later-drain wording must be explicit — MUST NOT.** Do not stop at accepted, complete, merge-ready, approved, or no further remediation needed when the practical intent is to support later PF-canon drain.  
* **This does not move canon drain earlier — MUST NOT.** The required later-drain statement records intent at approval time; it does not authorize early PF edits during implementation or OPS work.  
* **Supported later-drain status must be distinct from current recorded status — MUST.** Reviews and closeout artifacts must distinguish current phased PF09 recorded status, supported later-drain status, actual implemented state, actual OPS state, and actual governed evidence state.  
* **Phased PF09 impact & status posture — SHOULD.** If the reviewed work maps to phased PF09 tasks or subtasks, include the exact phased PF09 document, the task ID, any subtask IDs, the current status if evidenced, the status recommendation, why that posture is supported, the evidence pointers, the linked findings, and any linked doc-delta items.  
* **PF proof excerpts when phased PF09 is relied on — SHOULD.** When a status recommendation or impact claim depends on phased PF09 wording, include short verbatim PF proof excerpts from the relevant phased PF09 sections.  
* **No proven phased PF09 impact is an allowed outcome — SHOULD.** If the review does not prove phased PF09 impact, say so explicitly as no proven phased PF09 impact.  
* **Retired PF09 surface — MUST NOT.** Never cite the retired single-document PF09 in this summary. Use the relevant phased PF09 document instead.  
* **Status recommendation posture — SHOULD.** When the reviewed PR proves merge-readiness or an evidence slice but does not itself justify a checklist-status drain, it is acceptable for the review to state no status change recommended.  
* **Whole-PR-lifecycle Evidence Print — SHOULD.** For reviews that span multiple attempts, Evidence Print should include acceptance coverage evidence and a short closure-of-gaps-across-attempts summary that states which earlier gaps were closed and by which later attempt.  
* **Mixed-state governed evidence families are invalid — MUST.** If a bounded PR, OPS task, remediation bundle, or close-pack review relies on a governed evidence family, that family must express one authoritative posture for the same closure dimension. Contradictory states inside the same family are a documentation or evidence failure and block approval until normalized.  
* **Documentation or evidence failure must be classified separately from runtime failure — MUST.** If runtime facts are stable but governed artifacts disagree, classify the issue as documentation or evidence failure. If runtime behavior is wrong, classify it as runtime or implementation failure. Do not demand additional reruns unless runtime facts are actually missing, changed, or contradicted.  
* **Documentation-only normalization is allowed when runtime facts are unchanged — MUST.** A bounded remediation may normalize all governed artifacts in the affected family, including indices, checksum sidecars, and sibling path-proofs, without a new runtime rerun when no new runtime fact is being claimed and the closure interpretation is explicit.  
* **Closure mode must be explicit when equivalence is used — MUST.** If a review accepts closure by equivalence rather than by an independently exercised runtime, the approval artifact must state that closure mode explicitly and must not leave parallel governed artifacts in an older contradictory posture.

### **12.14 Implementation reports and lead retrospectives (source posture, evidence gaps, and closure questions)**

* **Primary-source posture — MUST.** Use the designated live source of truth as the default narrative basis for an implementation report or lead retrospective.  
* **Narrow gap-filling fallback — MAY.** If that primary source does not restate the original business case or the single consolidated PR and OPS sequence, the report may use an approved epic plan or approved implementation plan for those exact gaps only. The report must say that this limited fallback is being used and why.  
* **Implementation-report grounding — SHOULD.** When present, the implementation report should preserve a single consolidated PR and OPS sequence, the major surfaces affected, and the evidence inventory.  
* **Accepted execution deviations — SHOULD.** When an implementation report, epic closure review, or lead retrospective depends on an approved rerun, rails exception, dependency-preflight correction, or other bounded deviation, surface that deviation explicitly and keep it separate from the final PASS or closure verdict.  
* **Auditability caveat for summary-source closure authority — SHOULD.** If the decisive source states closure or supportable posture through evidence-basis prose rather than direct `Evidence pointer:` lines, say so explicitly as an auditability caveat and distinguish that auditability weakness from the underlying closure-truth claim.  
* **Later-drain separation — SHOULD.** Distinguish current evidence-grounded closure or supportable posture from later documentation drain or canon updates; do not write later-drain language as though the drain already happened.  
* **Evidence gaps section — SHOULD.** If raw artifacts were not reviewed directly, or if the report relies on summary sources for artifact existence or pass or fail posture, include an Evidence gaps section that states what is missing, what would prove it, and where that proof should exist if known.  
* **Canon-alignment and documentation outcomes — SHOULD.** When relevant, include canon references used, proposed addenda or doc-delta intents, token or evidence semantics notes, and unresolved documentation outcomes that affect later documentation drain.  
* **Open closure items or questions — SHOULD.** When closure posture remains unresolved, include explicit open closure items or questions tied to exact mapped work, later-drain posture, or remaining evidence gaps.  
* **Keep closure questions concrete — SHOULD.** Phrase questions against exact mapped work, later-drain posture, or remaining evidence gaps rather than vague epic-summary questions.

## 13\) Security & privacy for writing

* No secrets in examples — MUST. Redact or use obvious placeholders; never paste API keys, cookies, or bearer tokens.  
* Keys-only logs in examples — MUST. Never show raw PII or secrets; summarize with names-only.  
* Local only — MUST. Do not imply writes to repos or external systems; all outputs are paste-ready text.  
* Evidence artifacts — SHOULD. Names/paths only in PF; bytes live outside PF and follow §4 canonical JSON rules.

### **13.1 Evidence & log naming (QA)**

QA evidence logs are text artifacts and follow the same naming hygiene as all examples in this doc. When you design or update a Live QA plan or QA harness, apply these rules:

* **Checks-only evidence layout — MUST.** Live QA evidence MUST live under a stable epic-scoped QA root (for example, `audit/qa/<epic-id>/`) and under check-scoped subdirectories `checks/<check_id>/`.

* **No per-run nesting — MUST NOT.** Do not introduce run-id directories, timestamped run directories, “fresh directory for this run” layouts, or other per-run roots. Re-running QA MUST reuse the same stable check directories.

* **No operator-set per-run roots — MUST NOT.** QA plans and reviews MUST NOT require an operator to set a fresh evidence root for each run. Use the stable epic-scoped root and the stable check directories.

* **One primary log per check — MUST.** Each check directory MUST contain one primary step log (for example, `primary.log`) that records the authoritative step narrative, status markers, and exact commands actually used when relevant.

* **Deterministic companion file names — MUST.** Within a given check directory, use a single, consistent naming scheme for companion artifacts. Re-running the same check MUST reuse the same artifact names.

* **No mixed naming schemes in the same check context — MUST NOT.** Do not mix ad-hoc naming schemes for the same artifact role inside one check directory.

* **Temporary scratch files — SHOULD.** Temporary request or response bodies or scratch outputs SHOULD use a `tmp_` prefix and live inside the same check directory or a dedicated `tmp/` subdirectory under that check directory.

* **Plan-created deliverables live under checks — MUST.** Deliverables created by the plan MUST live under the stable check directory for the step that produces them.

* **Approval gate — MUST.** Any Live QA Plan or review that introduces per-run nesting or per-run root selection MUST be returned for revision.

These rules do not change how sampler/core or other tests are written; they set expectations for the quality and traceability of QA evidence artifacts and keep QA evidence stable across reruns.

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

### **`15.1 Standard PF header`**

`Title:`  
 `Version: vX.Y.Z`  
 `Status: <Final | Approved | Review | Living>`  
 `Effective date:`  
 `Last Update Gate: <Epic/Decision ID>`  
 `Invocation tag: <INV_TAG>`

**`Provenance (machine-checkable)`**  
 `{"author":"","sources":"","invocation_tag":"<INV_TAG>"}`

---

### **15.2 Redline block**

**Always** redline with:

* Change type: NEW CANON / CANON UPDATE / CLARIFICATION / CONSISTENCY / DOC HYGIENE / DELETION

* Evidence basis: cite the source blob

* Placement: section anchor \+ operation \+ text to paste

**Example redline block**

Redline N —  
 Change type: CLARIFICATION  
 Reason: clarify placement mechanics

Placement:  
 Doc: PFxx  
 Section anchor: “\<exact line from PFxx\>”  
 Operation: INSERT AFTER “\<exact line\>”

Text to paste:  
 (paste verbatim)

**Example anchor**

Use: “after `Binary markers`” not “after the binary markers section”.

---

### **15.3 Build Notes Addenda Block**

See §9 for the Build Notes Addenda template and usage.

---

### **15.4 Live QA step template (Deliverables-first)**

Use this structure for any QA plan or Live QA runbook step. This template enforces §12.3, §12.4, and §13.1.

Step \<N\> — \<short step title\>

Check ID: \<stable id for this step\>  
 PF refs: \<PF document title § anchor list\>  
 Tokens (names only): \<token list, if applicable\>

Intent: \<what this step must discover, prove, or validate\>

Discovery step (only if needed):

* Objective: \<what must be located or verified to exist\>

* Discovery acceptance: \<what proves the locus is correct\>

* Evidence that records the discovered locus: \<path under audit/qa/\<epic-id\>/checks/\<check\_id\>/\>

* BLOCKED if: \<when discovery cannot proceed without guessing\>

Minimal test step:

* Directive: \<objective-first instruction\>

* Command (optional; verified only): \<single command string if proven or runtime-resolved\>

* Runtime record: exact commands actually used MUST be captured in the primary log or step evidence

Plan-created outputs (if any):

* Path: \<exact repo-relative path and filename\>

* Creation instructions: \<runnable creation step\>

* Why: \<what deliverable or proof obligation this file satisfies\>

Deliverables (paths only):

* \<fully qualified path 1\> — \<one-line description\>

* \<fully qualified path 2\> — \<one-line description\>

Conditional deliverables (only if the stated condition is met):

* Condition: \<named condition from the plan\>

* Conditional deliverable path: \<fully qualified path\> — \<one-line description\>

* If the condition is not met: record as `Not applicable` or `not required because condition not met`, not as missing evidence

PASS criteria (file-based):

* \<what must be true in the Deliverables or discovery evidence\>

FAIL criteria (file-based):

* \<what would constitute failure in the Deliverables or discovery evidence\>

BLOCKED criteria:

* \<what prevents proceeding without guessing or due to missing prerequisites\>

Final status marker: `PENDING` → `PASS` | `FAIL` | `FAIL_TOOLING` | `BLOCKED` (recorded in the primary step log)

### **15.5 OPS task record template (PO-only; IA-guided; not PR work)**

**OPS task record:**

* Task title:

* Owner:

* Date:

* Scope:

* Preconditions:

* Procedure:

* Evidence to capture:

* Evidence storage path:

  * `audit/ops/<epic-id>/<relative_path>/` or `audit/qa/<epic-id>/<relative_path>/`

* Rollback plan:

* Completion criteria:  
* Canon-grounded instructions are required when available. If canon already provides concrete operator steps, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules for the OPS task, the task record must include those instructions explicitly rather than staying only at the level of intent, constraints, or outcome.  
* No invented OPS procedure. If canon is silent, incomplete, or ambiguous, the task record must state that the missing instruction is unknown and must not fabricate steps.  
* Titles-only canon references remain required. Any PF references used to ground OPS instructions must remain titles-only.  
* PF07-backed infra facts still apply. When the OPS task depends on infrastructure facts, use the PF07-derived or PF07-gap posture defined in planning discipline.

OPS final review structure — SHOULD. If an OPS task later receives a final review, that review should use three top-level sections: Review Summary, Findings, and Evidence Print.

OPS final review findings — SHOULD. Each finding should state what was observed, why it matters, the expected requirement from the governing plan or canon source, and whether the issue is a blocker for acceptance.

OPS final review Evidence Print — SHOULD. When applicable, structure the evidence print in three distinct parts:

* Required deliverables satisfied.  
* Commands or actions evidence.  
* Configuration or infrastructure state evidence.

Bounded validation or classification OPS tasks — SHOULD. If an approved OPS task is read-only validation, gap classification, evidence collection, or another explicitly non-closure step, the final review should judge it on whether it truthfully completes that bounded purpose.

Task purpose must be stated explicitly — SHOULD. The review summary should say whether the task is validation-only, classification-only, evidence-only, sequencing-only, or other bounded non-closure work, and should say that it does not itself close mapped phased PF09 rows when that is true.

Classification deliverables may be the core acceptable outcome — SHOULD. When the approved OPS task’s main product is a classification result or other bounded determination, it is acceptable for the final review to accept the task on that basis without requiring later implementation or closure work to be complete.

No overclaim — MUST. The OPS final review must not imply that later PRs, later OPS tasks, or mapped phased PF09 closure work are already complete when the approved task only supplies a bounded input to that later work.

Truthful not-yet-closed states are acceptable — SHOULD. An OPS final review may accept a truthful not-yet-closed state when the evidence bundle is internally consistent and aligns with the governing plan or canon. The review should not force a false closed status merely to simplify closure language.

* 

---

### **15.6 Remediation Implementation Guide writing constraints (DEV/OPS only)**

These constraints apply to Remediation Implementation Guides used for escalations and remediation execution.

Step types — MUST. A Remediation Implementation Guide MUST use only two step types: DEV and OPS. No other step types are permitted (no QA, DOC, REVIEW, or “verification-only” steps).

Verification embedding — MUST. All verification MUST be embedded inside the owning DEV or OPS step and MUST produce concrete, repo-stored evidence outputs (paths and filenames specified in the step).

OPS linkage — MUST. Any step labeled OPS MUST follow the OPS posture in §4 and the OPS task record template in §15.5 (PO-only execution, IA-guided, not PR work, secret-free evidence, lowercase audit paths).

Dependency-line rule (locked) — MUST. If a step depends on outputs produced by a prior step in the other lane, the dependent step MUST include exactly one cross-lane dependency line in this exact form (and only when needed):  
 Inputs needed from Step S\<N\> during implementation: \<exact items\>  
 Rules: S\<N\> MUST be the actual producing Step ID (no placeholders such as Sx). The line MUST appear exactly once in the dependent step. If there is no cross-lane dependency, the line MUST be omitted (no placeholder lines).

Observed Evidence vs canon — MUST. If a remediation guide or OPS tooling references a behavior that is not canonized (example class: auth posture for an endpoint), it MUST NOT be stated as canon. The statement MUST be explicitly labeled as Observed Evidence (non-PF), and the guide MUST specify what evidence is required to canonize the behavior (secret-free, repo-stored, lowercase audit path, presence-only/redacted/hashed as needed).

Portability vs provenance (non-PF evidence) — MUST. Remediation guides MAY include a short “Evidence inventory reviewed (non-PF)” list for provenance, but MUST NOT require the executor to open external files to perform the work. If any non-PF fact is required to execute downstream steps (command outputs, headers, error strings, observed paths, status lines), the guide MUST embed that fact directly as a short quote or precise paraphrase in an “Observed Evidence Snapshot” subsection. If an Artifact Map is included, it MUST explicitly label non-PF inputs as: “provenance only; not required to execute”. When a non-PF observation drives a branching decision, the guide MUST include: the observation to look for (exact string/status/shape), the decision rule, and the output artifact path where the observation is captured (lowercase file path including filename).

Explicit invariant checklist for governed evidence — MUST. If a remediation guide produces governed /internal/version evidence (via a QA step or probe tool), the guide MUST explicitly enumerate the canon-critical invariants being verified and MUST NOT imply those checks by referencing PF sections only. The guide MUST also specify that \*\_OK claims are gated on verifying the corresponding invariant against the same captured bytes being written as evidence for that run (no “false OK” on FAIL\_TOOLING, and no mixed-target/redirect drift). Use the /internal/version checklist snippet in §15.10 when applicable.

Canonical template home — MUST. Remediation Implementation Guides MUST follow the canonical section ordering and step schema defined in the Plan Templates document. PF03 does not redefine that ordering; it defines the writing constraints above to prevent lane drift, portability blockers, and implied verification.

### **15.7 PF23 Anchors (planning traceability snippet)**

Use this subsection in any planning artifact (QA plans, remediation guides, implementation guides, EPIC records, runbooks). This is a traceability anchor only; it MUST NOT duplicate PF23 contents. It MUST NOT be used for PR analysis or remediation review.

PF23 Anchors  
 Component(s) (from PF23):  
 Key pathnames/loci touched (from PF23):

Notes (optional): If PF23 appears stale or missing coverage, record as observation only; do not assign PF23 update tasks.

PF23 contradiction record (required only if PF23 contradicts PF canon):  
 PF23 claim (quote):  
 PF canon claim (quote \+ title \+ § anchor):  
 Impacted surface and locus:  
 Tentative bucket (choose one): canon defect, implementation drift, necessary reality shift  
 PO adjudication status: PENDING or RESOLVED

---

### **15.8 Evidence inventory reviewed \+ Observed Evidence Snapshot (non-PF portability)**

Use this template when you need to record evidence review in non-PF docs without copying full evidence logs.

Evidence inventory reviewed: YES/NO

Observed Evidence Snapshot:

* Claim: \<what you observed\>

* Source: \<repo file path\>

* Capture path (lowercase, includes filename): \<CAPTURE\_PATH\> (for example, `audit/qa/<epic-id>/<run>/<file>.txt`)

* Verification step: \<command or check used\>

* Result: PASS/FAIL/UNKNOWN

* Notes: \<brief\>

---

### **15.9 Governed evidence indices/mirror: exact filenames quick reference**

Use this list verbatim in plans/tasks that touch governed evidence indices/mirrors. Treat each file as a first-class deliverable. Path proofs are co-located siblings; do not place them in alternate directories.

Evidence index (human-readable):

* `docs/evidence/INDEX.json`

* `docs/evidence/INDEX.sha256`

* `docs/evidence/INDEX.json.path_proof.txt`

* `docs/evidence/INDEX.sha256.path_proof.txt`

Evidence index mirror (machine-readable):

* `artifacts/evidence_index.jsonl`

* `artifacts/evidence_index.jsonl.path_proof.txt`

* `artifacts/evidence_index.jsonl.sha256`

* `artifacts/evidence_index.jsonl.sha256.path_proof.txt`

Evidence Index snapshot (D23) artifacts (QA closure proof; tokenless):

* Snapshot JSON: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json`

* Snapshot path-proof transcript: `audit/gates/evidence_index_snapshot/evidence_index_snapshot.json.path_proof.txt`

Rules (normative):

* If a task edits any index/mirror file, the sibling `.path_proof.txt` update is part of the same task’s outputs and embedded verification.

* Governed path-proof transcript suffix is `.path_proof.txt` and the transcript is a sibling of the governed artifact. `.path_proof.json` is non-canonical and MUST NOT be used.

* Machine Evidence Index mirror home is `artifacts/evidence_index.jsonl`. Any other mirror path strings (including `artifacts/evidence/machine_mirror.json` or any `docs/evidence/` path that includes `machine_mirror` in its filename) are non-canonical and must be treated as doc drift until drained.

* D23 is a mechanical PASS or FAIL contract. It MUST NOT be represented as an acceptance token claim. When documenting D23 statuses, use Glow QA Guide status vocabulary for tool gating (for example: missing canonical inputs is `TOOLING_BLOCKED`; evaluated predicate fails is `FAIL_BEHAVIOR`).

* If a plan proposes a new file under governed surfaces, it MUST state whether the file is intended to appear in the indices/mirror; absence of that statement is a mechanical blocker.

* Remediation-only diagnostics/manifests MUST NOT be introduced under governed artifact surfaces unless explicitly framed as an ADR-worthy governance change; default is remediation audit paths (for example, `audit/qa/<epic-id>/<run>/remediation/<relative_path>`) and not indexed.

---

### **15.10 /internal/version proof checklist snippet (minimum; no implied checks)**

Use this checklist inside any QA step, remediation guide, or probe plan that produces governed /internal/version evidence. Do not imply these checks by referencing PF sections only.

Token naming (normative):

* Conditional semantics token name MUST be `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`. Aliases (for example, `INTERNAL_VERSION_COND_200_NO_304_OK`) are non-canon and MUST NOT be emitted or required.

Auth posture non-invention (normative):

* Auth posture for /internal/version is not canonized. Do not state auth requirements as canon. Any statement MUST be labeled as Observed Evidence (non-PF).

* Evidence required to canonize auth posture (OPS discovery): capture status line \+ headers for the canonical deployment context under two conditions: (1) with no auth header and (2) with the expected auth header present (value redacted or presence-only). Store secret-free evidence under a lowercase audit path.

Invariant checklist (minimum set):  
 A) Transport

* GET returns 200

* HEAD returns 200 (parity expectations satisfied)

* Conditional requests (If-None-Match, If-Modified-Since) do not yield 304; they return 200

B) Headers

* `Cache-Control: no-store` present

* `Content-Type: application/json; charset=utf-8` present

* `ETag` absent

* `Last-Modified` absent

C) Body (identity payload)

* Body is fixed-schema JSON with exactly these keys (no extras): `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`

* Body bytes satisfy the canon identity-bytes posture where applicable to the proof surface (canonical bytes including LF termination)

HTTP capture hygiene (normative):

* Stderr separation — MUST. Header artifacts MUST NOT mix curl warnings or other stderr output into the header file. Capture stderr separately (for example, to a `curl_stderr*.txt` sibling) or filter non-header lines so header files contain only the status line and header lines.

Token emission gating (normative):

* Do not emit any `*_OK` token unless the corresponding invariant is verified against the same captured bytes being written as evidence for that run.

* If the run is FAIL\_TOOLING (or equivalent), do not emit `*_OK` tokens for invariants that did not pass. Do not emit “integrity success” tokens (for example, path-proof match or two-run identity) unless those checks demonstrably passed on produced artifacts.

* Evidence coupling is required: emitted tokens, captured headers, captured body, and any digest MUST refer to the same resolved target/response chain. If coupling cannot be established, the run fails and MUST NOT emit `*_OK` tokens.


### **15.11 Remediation Task Plan template (DEV PRs \+ OPS tasks)**

Use this template for remediation tasks during epics.

Task summary:

* Goal:

* Scope:

* Out of scope:

* Risk level:

Task list:

DEV tasks — PRs only: `PR-01`, `PR-02`, \[LIST CONTINUES\]  
 OPS tasks — PO-run procedures only: `OPS-01`, `OPS-02`, \[LIST CONTINUES\]

For each task:

* Task ID: \<PR-01 | PR-02 | \[LIST CONTINUES\] | OPS-01 | OPS-02 | \[LIST CONTINUES\]\>  
* Status (optional): \<Not done | In progress | Done | Optional\>

* Task type (optional): \<Canon update | Debt/confirm | Clarification | Doc hygiene | Other\>

* Must-act-now (optional): \<YES | NO\>

* Source finding (optional; if derived from an audit): \<FND-\#\#\#\>

* Owner:

* Steps:

* Evidence to capture:

* Acceptance tokens impacted (if any; must be registry-valid):

Outputs / Deliverables:

* PR links (if any):

* Files created:

* Evidence paths:

* Notes:

* If an acceptance map is produced or updated, bind it to `docs/acceptance_map_epic<NNN>.json` with a sibling `docs/acceptance_map_epic<NNN>.json.path_proof.txt` (example: EPIC024 → `docs/acceptance_map_epic024.json`).

Governed index/mirror touchpoints:

* Evidence Index updated? YES/NO

* Machine mirror updated? YES/NO

* Path proof updated? YES/NO

Close-out checklist:

* Preconditions satisfied:

* Evidence captured:

* Acceptance updated:

* Review complete:

### **15.12 PR analysis record template (diff-first review narrative)**

Use this template when producing a diff-first PR analysis or remediation review narrative. The intent is to make the review reproducible, evidence-linked, and audit-friendly without copying entire diffs or logs.

Hard rules:

* Tokens are names-only. Do not invent tokens.

* Evidence pointers must refer to repo paths, PR artifact section headings, or captured evidence files. Do not reference private tools, external links, or unstated files.

* Doc Deltas are PF-Canon only. Do not propose canon edits to non-PF docs inside this block.

PR analysis record — \<PR\_ID\>

Provenance (required; primary)

* Lifecycle chain: \<ATTEMPT\_CHAIN\> (example format: Original → Remediation 1 → Remediation 2\)

* Primary scope source: \<PLAN\_OR\_IMPLEMENTATION\_DOC\_NAME\>

* Evidence pointers reviewed (titles only):

  * \<EVIDENCE\_POINTER\_1\>

  * \<EVIDENCE\_POINTER\_2\>

Attempt History (recommended when more than one attempt exists)

* Attempt 0 (Original): \<STATUS\> | Evidence pointer: \<POINTER\>

* Attempt 1 (Remediation 1): \<STATUS\> | Evidence pointer: \<POINTER\>

* Attempt 2 (Remediation 2): \<STATUS\> | Evidence pointer: \<POINTER\>

Review Summary

* \<3–8 sentences summarizing what changed, whether it satisfies plan requirements, and what risks remain\>

* RCA section included: \<YES | NO\> (trigger: \<BRIEF\_REASON\>)

Files Changed or Added (scope drift check)

* Paths: \<PATH\_LIST\>

* Expected vs unexpected: \<OK | DRIFT\>

* Evidence pointer: \<POINTER\_TO\_PR\_FILE\_LIST\_OR\_DIFF\>

Diff Review (required; primary technical review)

DR-001

* Change summary: \<what changed, stated mechanically\>

* Risk assessment: \<Low | Medium | High\>

* Why it matters: \<impact on contract, evidence, or safety\>

* Evidence pointer: \<PATH or PR-ARTIFACT-HEADING\>

* Plan linkage: \<PLAN\_SECTION\_OR\_REQUIREMENT\_ID\>

RCA (required only if RCA trigger is active; trigger \= fix/remediation language in PR artifacts, or evidenced failure/bug/CI failure)

RCA-001

* A) Bug or failure statement (quoted): \<VERBATIM\_FAILURE\_LINE\>

* B) Root cause(s): \<CAUSE\_STATEMENT\>

* C) Fix across attempts: \<WHAT\_CHANGED\_OVER\_ATTEMPTS\>

* D) Fix verification: \<PASS\_PROOF\_LINE\>

* Optional context (where it occurred): \<ATTEMPT\_OR\_CONTEXT\>

* Residual risk (evidenced): \<NONE or DESCRIBE\>

Findings (includes diff review)

* Observed: \<FACT\>

* Why it matters: \<IMPACT\>

* Evidence pointer: \<PATH or PR-ARTIFACT-HEADING\>

* Evidence hygiene risk (if any): \<NONE or DESCRIBE\>

Requirement Satisfaction Crosswalk (required when plan requirements are explicit; Original step → Remediated satisfaction; whole PR outcome)

If requirement satisfaction materially affects phased PF09 mapping, each crosswalk item should note the impacted phased PF09 task ID(s) and subtask ID(s), if proven.

If phased PF09 status posture is part of the review, add a PF09 Impact & Status Posture block after the crosswalk. For each impacted phased PF09 task or subtask, state the current phased PF09 recorded status, the status recommendation, why that posture is supported, the evidence pointers, short PF proof excerpts when phased PF09 wording is relied on, and linked finding numbers when useful.

`No status change recommended` is an allowed outcome for a bounded non-closure step.

RS-001

* Requirement label: \<PLAN\_SECTION\_OR\_REQUIREMENT\_ID\>

* Requirement text: \<REQUIREMENT\_TEXT\>

* Original attempt status: \<STATUS\>

* Evidence pointer(s) supporting Original status: \<POINTERS\>

* Remedial change that closed the gap (if applicable): \<WHAT\_CHANGED\>

* Current status after remediation: \<STATUS\>

* Evidence pointer(s) supporting Current status: \<POINTERS\>

* Notes (optional; 1 line): \<NOTE or NONE\>

Doc Deltas (PF-Canon only; required; with Canon Check Gate)

CHG-001 (or `CHG-001:` \<one-line change claim\>)

* Change claim: \<ONE\_SENTENCE\_DELTA\>

* Doc (optional): \<PF\_TITLE\> (or `TBD`)

* Section (optional): \<SECTION\_ANCHOR\> (or `TBD`)

* Why (one sentence): \<WHY\>

* Evidence pointer: \<POINTER\>

* Canon basis: CANON SILENCE

* PF excerpt (verbatim, 1–5 lines; required unless Canon basis is CANON SILENCE): \<VERBATIM\_PF\_SNIPPET\>

* PR behavior evidence: \<POINTER\_TO\_DIFF\_OR\_PROOF\>

Evidence Print (PASS PROOF; required; whole PR outcome)

A) Acceptance coverage evidence (Plan or Implementation Doc)

* Plan or implementation doc: \<PLAN\_OR\_IMPLEMENTATION\_DOC\_NAME\>

* Coverage pointer: \<PLAN\_SECTION\_OR\_REQUIREMENT\_ID\>

* Evidence pointer(s): \<POINTERS\>

B) Evidence and verification posture now satisfied

* \<1–2 sentences stating what evidence is now present and what gap is closed\>

* Evidence pointer(s): \<POINTERS\>

C) Token and gate evidence (names-only; do not invent)

* \<TOKEN\_OR\_GATE\_NAME\_1\>

  * Evidence pointer(s): \<POINTERS\>

* \<TOKEN\_OR\_GATE\_NAME\_2\>

  * Evidence pointer(s): \<POINTERS\>

* None

* Token search method (required if None): \<WHERE\_YOU\_SEARCHED\>

D) Test or CI proof

* Command (verbatim): \<SINGLE\_COMMAND\> (or `None recorded`)

* Pass indicator (verbatim): \<PASS\_LINE\> (or `n/a` or `✅`)

* Where it appears: \<PR\_ARTIFACT\_SECTION\> (or `Not present in PR artifacts`)

* Search method (required if any field is `None recorded`): \<WHERE\_YOU\_SEARCHED\>

E) Artifact and evidence outputs

* Paths: \<REPO\_PATH\_LIST\> (or `None`)

* Type(s): \<json | jsonl | log | txt | sha256 sidecar | other\>

* Key proof facts (verbatim, short): \<1–5 lines\>

* Evidence pointer(s): \<POINTERS\>

* Risk note (required for docs-only PRs with contract-level assertions): \<1–2 sentences; note drift risk for token strings, endpoint lists, exit/error identifiers, or owned path lists\>

* Docs-only PRs: apply §15.13 Docs-only PR evidence posture checklist (minimum).


### **15.13 Docs-only PR evidence posture checklist (minimum)**

Use this checklist when the PR diff is docs-only (documentation files only).

* Scope confirmation (docs-only):

  * List files changed (expected vs unexpected) and confirm no code or config changes.

* Verification capture (minimum):

  * Capture at least one proof line in PR artifacts (command and pass indicator) for a markdown sanity check or doc lint run.

* Contract-level assertions:

  * For any doc claim that asserts token strings, endpoint lists, exit/error identifiers, or owned path lists, include how the claim was verified.

  * For CLI flag, arg, or syntax claims, capture the exact command and a short `--help` output excerpt showing the asserted syntax and flags. The command and excerpt MUST be included in PR artifacts (or a governed evidence artifact referenced by the PR). Do not rely on narrative-only statements such as "verified locally" without the captured command and output.

  * If any such claim is not verified, mark it as unverified and record it under DOC\_RISKS\_NOTED\_OK.

* PR analysis record:

  * In the PR analysis record template, complete Evidence Print C) Test or CI proof.

  * If no proof is recorded, include the search method and record the gap under DOC\_RISKS\_NOTED\_OK.

### **15.14 Reality audit report template (Audit Summary \+ Doc Delta Map)**

Finding-level home selection — MUST. Each finding in a reality audit must name the correct canon-home selection for PF09 task delta, PF14 mechanics delta, PF02 architecture delta, other PF doc delta(s), and PF20 historical correction when any of those lanes are relevant to the finding.

No-delta findings are allowed — MUST. A finding may conclude with no proposed doc delta in the current pass when it is confirmatory, descriptive, or otherwise does not expose a new canon-home gap. Say that outcome explicitly rather than forcing an artificial delta.

Home-selection justification — MUST. After the home-selection block, add a short "Why these are the correct homes" sentence tied to the audit evidence and the plan linkage when one exists.

Grouped proposal posture — SHOULD. Reality-audit doc delta proposals may be grouped by target family or target doc title when that improves traceability. State "None." for any target family that has no proposal in the current pass.

Canon-proof posture for proposals — SHOULD. When a proposed delta relies on existing canon wording, include a short PF proof excerpt and one sentence stating why the chosen target doc is the correct home.

Open questions for the PO — SHOULD. When routing or scope remains unresolved, include a short open-questions block that states the question, why it matters, and the evidence pointer that makes the answer consequential.

Use this template for any repo-vs-canon reality audit output.

**Audit Report:** \<AUDIT ID\>

**Audit Summary:**

* Purpose: \<one sentence\>

* Audit inputs: \<repo snapshot \+ canon snapshot\>

* What was checked: \<architecture | mechanics | evidence posture | other\>

* Outcome: \<Aligned | Drift | Mixed\>

* High-risk notes (optional): \<1 to 5 bullets\>  
* Count of findings: \<integer\>

* Count of Must-act-now findings: \<integer\>

**Drift themes (roll-up):**

* Theme: \<one line\>

* Classification: \<Aligned | Drift | Mixed\>

* Evidence pointer(s): \<paths, PRs, or other stable references\>

* Notes (optional): \<one line\>

**Findings → Doc Delta Map (required; single sink):**

* Rule: every finding gets a stable Finding ID and maps to one or more `doc_delta[]` items, plus optional follow-up tasks.

* Rule: do not maintain a second list of doc deltas elsewhere in the audit report. This is the single sink for finding-to-delta mapping.

For each finding:

* Finding ID: \<FND-\#\#\#\>

* Finding (one sentence): \<what is true in the repo\>

* Audit anchor (verbatim line): "\<VERBATIM LINE\>"

* Audit evidence pointer(s): \<paths, PRs, or other stable references\>

* Plan linkage (optional; one sentence): \<how the plan expects this to work\>

* Plan anchor (optional; verbatim line or N/A): "\<VERBATIM LINE OR N/A\>"

* Must-act-now: \<YES | NO\>

* Doc deltas required (targets only; at least one):

  * PF09 task delta: \<YES | NO\>

  * PF02 architecture delta: \<YES | NO\>

  * PF14 mechanics delta: \<YES | NO\>

  * Other PF doc delta(s): \<PF\#\#-Title-Here | None\>

**Doc Delta Proposals (grouped by target doc title):**

* Target doc: \<PF\#\#-Title-Here\>

* For each proposed doc delta:

  * Doc delta ID: \<DOC DELTA ID\>

  * Target section anchor: `§<num> <heading>`

  * Operation: \<ADD | REPLACE | DELETE | INSERT BEFORE | INSERT AFTER\>

  * Evidence basis (verbatim or pointer): \<SOURCE SNIPPET OR POINTER\>

  * Draft text: \<paste-ready text or a PF03 redline block\>

### **15.15 Post-audit ADR template (decision \+ canon drain)**

Audit-derived ADR framing — SHOULD. State the ADR topic first, then a short "Why it matters" explanation tied to the exact audit ambiguity or repeated dispute.

Canon touchpoints — MUST. Name the relevant PF homes and exact sections that the ADR is interpreting or clarifying before giving the decision.

Final decision — MUST. State the chosen boundary in direct language, say what it does not authorize, and keep the decision tied to the named canon touchpoints rather than to repo habit alone.

Boundary and example posture — SHOULD. If the ADR chooses a bounded pattern instead of a reusable wildcard, or a general rule with examples instead of a snapshot list, say that choice explicitly in the final decision so later drains do not widen scope by implication.

Net-result recap — SHOULD. When two or more related audit decisions are being closed together, end with a short net-result summary that states the practical outcome in one glance.

Use this template when an audit reveals repeated ambiguity, conflicting interpretations, or a drift rubric that must be made explicit.

**ADR ID:** \<ADR ID\>

**Title:** \<one line\>

**Date:** \<YYYY-MM-DD\>

**Status:** \<Proposed | Accepted | Superseded\>

**Decision owner:** \<role or name\>

**Context:**

* What ambiguity or repeated dispute exists (one paragraph)

* What audit output or repo evidence triggered this ADR (evidence pointer\[s\])

**Decision:**

* Decision statement(s) using MUST, MUST NOT, SHOULD, or MAY

* Definitions for any loaded terms introduced by the decision

* Rationale (KISS): \<one sentence\>  
* Explicit carve-outs and non-goals

**Alternatives considered (optional):**

* A1) \<one line\>

* A2) \<one line\>

**Consequences:**

* What canon statements become wrong or incomplete

* What must change in docs, tests, or implementations (titles only)

**Canon impact (doc-delta targets):**

* \<PF\#\#-Title-Here\>

* \<PF\#\#-Title-Here\>

**Non-goals (optional):**

* \<one line\>

**Doc deltas (paste-ready) to drain this ADR into canon:**

* Rule: each doc delta includes a current proof excerpt (verbatim) and an exact replacement block.

For each doc delta:

* Doc delta ID: \<DOC DELTA ID\>

* Target doc title: \<PF\#\#-Title-Here\>

* Target section anchor: `§<num> <heading>`

* Current proof excerpt (verbatim): "\<VERBATIM EXCERPT\>"

* Operation: \<ADD | REPLACE | DELETE | INSERT BEFORE | INSERT AFTER\>

* Paste-ready text: \<exact new text to add or replace\>

* Why (KISS): \<one sentence\>

  ### **15.16 QA check decision record template (single check)**

Use this when you need a paste-ready decision record for one QA check. This is appropriate as a PF10 addendum entry or as a standalone QA decision note.

Title line format:

* `\<ADDENDUM_ID\> \<EPIC_ID\> QA: \<CHECK_ID\> — Decision: \<PASS | FAIL | NOT RUN | BLOCKED | REMEDIATION DEFERRED DUE TO PLANNING DEFECT\>`

Required sections and fields:

Review Summary

* 2–6 sentences. State what was checked, what evidence was produced, and which pass or fail criteria were applied.

* If there is a non-blocking planning or wording defect, state it explicitly and say whether it drives the decision.

* If the step is blocked or deferred due to a planning defect, state why the step is not executable as written and whether the blocker is an input-availability gate, a plan defect, or both.

* Evidence trust statement (optional but recommended when layout or root compliance matters): \<one sentence stating whether evidence trust is acceptable and why\>

Findings

* For each finding, use the four-line block below.

* Keep findings atomic. One claim per block.

* Observed: \<one sentence fact\>

* Evidence pointer: \<pointer to exact source lines\>

* Why it matters: \<one sentence impact\>

* Drives decision: \<Yes | No\>

Evidence Print

* Plan criteria relied on (paste minimally, and keep it verbatim):

  * \<criterion 1\>

  * \<criterion 2\>

A) Required deliverables checklist (from plan or caveats for this step)

* Deliverable name or label (plan quote): \<quoted plan deliverable line\>

* Expected path: \<path\>

* Present in DELIVERABLES\_REPORT\_FILE: \<Yes | No — Missing | Not applicable\>

* Evidence pointer: \<pointer to exact source lines\>

* If missing:

  * Negative-claim proof: \<where and how you searched for the exact path or label\>

  * Alternate proof available: \<Yes | No\>

  * Alternate proof pointers: \<pointer(s) or None\>

* If conditional:

  * Condition source (plan): \<quoted plan condition\>

  * Condition not met or intentionally skipped (deliverables report): \<pointer or short quote\>

B) Evidence artifacts relied on

* Path or label: \<path\>

* Evidence pointer: \<pointer to exact source lines\>

* Key proof facts: \<short verbatim facts or field values\>

C) Tokens or gates (plan-named only; do not invent)

* If no token or gate is named in the plan or caveats for this step, record:

  * None observed for this step in plan/caveats.

  * Evidence pointer: \<pointer to exact source lines showing absence of a plan-named token or gate\>

* If a token or gate is named, use one block per item:

  * Token or gate name: \<name\>

  * Evidence pointer: \<pointer to exact source lines\>

  * Execution trace (if applicable):

    * Command (verbatim): \<command line\>

    * Command provenance: \<Plan | Scaffolding | Manual | Unknown\>

    * Exit code (if known): \<0 | non-zero | Unknown\>

QA Verdict and Optional Follow-ups

* Verdict line: \<PASS | FAIL | NOT RUN | BLOCKED | REMEDIATION DEFERRED DUE TO PLANNING DEFECT\>

* If revised disposition is needed:

  * Revised disposition: \<updated disposition\>

  * Why the original framing is misleading: \<one sentence\>

* Rationale: \<2–6 sentences; must align with the Findings marked Drives decision: Yes\>

* Optional follow-ups (do not mix with the verdict rationale):

  * \<follow-up 1\>

  * \<follow-up 2\>

ADRs — Deviations (optional; use when actual run differs from the plan or caveats but the step may still be acceptable)

ADR-DEV-01

* What changed: \<one sentence\>

* Evidence pointer: \<pointer to exact source lines\>

* Why it changed: \<one sentence or Unknown\>

* Evidence pointer: \<pointer to exact source lines\>

* Plan or caveat reference: \<pointer to exact source lines\>

* What was actually run: \<one sentence or command summary\>

* Evidence pointer: \<pointer to exact source lines\>

* Evidence impact: \<one sentence stating whether deliverables, PASS criteria, or evidence trust changed\>

* Evidence pointer: \<pointer to exact source lines\>

* Decision: \<Acceptable for this step | Not acceptable\>

* Evidence pointer: \<pointer to exact source lines\>

* Canon impact: \<one sentence stating whether canon already permits this or whether a doc delta is needed\>

* Evidence pointer: \<pointer to exact source lines\>

Evidence pointer format guidance (recommended)

* Prefer a pointer that names the source doc and the exact excerpt you relied on.

* One acceptable format is a pipe-delimited pointer:

* Evidence pointer: | \<Source doc\>: \<section locator\> | "\<verbatim line 1\>" | "\<verbatim line 2\>" | "\<verbatim line 3\>"

Notes

* Do not paste long JSON blobs into the decision record. Instead, point to the file and quote only the 1–3 fields that drive the decision.

* If you cannot verify a claim due to missing artifacts, treat it as Unknown and say so explicitly.

* If missing deliverables result solely from an unmet plan-stated condition or an input-availability gate, explain that gate explicitly and use the appropriate verdict or revised disposition above.

  ### **15.17 Final QA closeout review template (closeout summary \+ QA RCA)**

Use this when you need a final QA closeout narrative that combines an evidence-grounded readiness statement, explicit coverage-vs-plan accounting, and a QA RCA suitable for preventing recurrence.

Title line format:

* `\<ADDENDUM_ID\> \<EPIC_ID\> QA Closeout Summary`

QA Closeout Summary

* Epic / label: \<EPIC\_ID and short label\>

* Reviewed inputs: \<list the source sets actually reviewed\>

* Overall readiness (evidence-grounded): \<READY | READY WITH CAVEATS | NOT READY\>

* One-line root cause category: \<one sentence\>

* Implementation Guide goal framing (non-executional; optional): \<goal statement quoted or paraphrased narrowly\>

Canonical RCA requirement basis (cite canon, do not paraphrase)

* List the canonical requirements that make the RCA or closeout required and that define its minimum contents.

* Use a no-outs locator gate for each canon reference:

* Canon locator: \<PF doc title\> \<section locator\>

* Canon proof excerpt (verbatim, 1–3 lines): \<paste verbatim\>

Checklist of required RCA or closeout elements

* Coverage vs QA Plan accounting must be explicit, step-by-step, complete, and auditable.

* Token or evidence posture must not accept pass language without concrete evidence pointers.

* Closeout artifacts and their required paths must be stated explicitly.

* Remediation loops must retain failure signature, remediation note, and rerun outcome when applicable.

Compliance statement (this deliverable vs canon checklist)

* Coverage vs QA Plan accounting: \<Complete | Partial | Missing\> — \<one sentence\>

* Token or evidence posture: \<Satisfied | Partially satisfied | Not satisfied\> — \<one sentence\>

* Closeout artifacts: \<Satisfied | Partially satisfied | Not satisfied\> — \<one sentence\>

* Remediation posture: \<Satisfied | Partially satisfied | Not satisfied\> — \<one sentence\>

Source-of-Truth posture

* Primary SoT: \<PF10 | other named source\>

* Implementation Guide used: \<Yes | No\> — \<framing only | execution basis | other narrow role\>

* QA Plan used: \<Yes | No\> — \<intended requirements framing only | other narrow role\>  
* Decisive PF10 close-authority pointer posture (if applicable) — record one of: Direct evidence-pointer lines, Evidence-basis prose only, or Not applicable.  
* If the decisive PF10 close-authority addendum uses evidence-basis prose only, record an explicit auditability caveat — MUST. State that the addendum summarizes evidence basis instead of embedding direct evidence pointers, and state whether the artifact chain had to be reconstructed from surrounding governed evidence.

* High-level source mismatches (if any):

  * \<mismatch 1\>

  * \<mismatch 2\>

QA Timeline (reconstructed)

* Reconstruction rule: \<how dates, ordering, or phase grouping were derived\>

* Use only the minimum timeline needed to support the readiness statement or RCA.

* Format each entry as:

* \<YYYY-MM-DD\> — \<event summary\>

* Evidence pointer: \<pointer\>

Coverage vs QA Plan

Coverage status rubric (use these exact labels)

* Fully evidenced: the check ran and the expected evidence artifacts exist.

* Partially evidenced: the check ran but one or more required artifacts are missing, incomplete, or compromised.

* Not evidenced: the check is claimed but evidence pointers are insufficient to audit the claim.

* Not run: the check did not run in the covered execution window.

Coverage matrix (one entry per check)

* Check ID: \<stable step identifier\>

* Plan intent: \<short quoted or paraphrased intent\>

* Coverage status: \<Fully evidenced | Partially evidenced | Not evidenced | Not run\>

* Evidence pointers:

  * \<pointer 1\>

  * \<pointer 2\>

* Deviations or mismatches vs QA Plan: \<one sentence or None\>

* Closeout impact: \<Non-blocker | Blocker | Unknown\>

Findings (numbered; single shared list for closeout \+ RCA)

FND-001

* What happened: \<one sentence fact\>

* Evidence pointers:

  * \<pointer 1\>

  * \<pointer 2\>

* Why it matters: \<one sentence impact\>

* PF touchpoint (optional): \<PF doc title and section\>

* Proof excerpt (optional; verbatim, 1–3 lines): \<paste verbatim\>

* Classification: \<Evidence posture gap | SoT mismatch | Plan-to-evidence drift | Other\>

* Negative-claim proof (required when absence is asserted):

  * Searched source: \<source name\>

  * Pattern(s): \<exact search pattern list\>

  * Result: \<what was or was not found\>

QA RCA (root causes and fixes)

Root causes (PF10-grounded or other named primary SoT)

* Primary root cause: \<one sentence\>

* Contributing factors:

  * \<factor 1\>

  * \<factor 2\>

Fix proposals (each fix must include a verification hook)

* Fix: \<one sentence\>

* Verification hook: \<how future evidence would prove the fix held\>

Common fix themes to consider (cite the applicable canon section when used)

* QoS stop-rule for repeated structural remediation.

* Rails posture truthfulness and explicitness in plans and rollups.

* Prompt mode separation (planning and authoring vs review) to prevent plan text from being mistaken for executed evidence.

* Artifact-list invariants, including `primary.log` when a step ran.

* Closure record semantics for deferred checks: do not list future or deferred step artifacts as required primary evidence for the current run.

  ### **15.18 Epic closure review template (closure registers \+ trace ledger)**

Use this when you need to determine whether an epic can be formally closed, and if not, the minimal follow-ups required to make closure defensible and canon-aligned.

* **Title line format — SHOULD.** Write `Epic Closure Review —` followed by the epic ID.  
* **Input naming — SHOULD.** When the actual inputs are an Implementation Guide and a QA Plan, name them that way rather than using more generic plan labels. If other inputs were reviewed, list only the inputs actually used.  
* **Source-of-truth role split — SHOULD.** In the inputs posture, state not only the primary source of truth but also which canon homes supplied closeout requirements or close-gate deliverable posture when that matters to the judgment.  
* **Deliverables register detail — SHOULD.** For each deliverable entry, prefer a human-readable deliverable label, record the source, include a verbatim anchor quote, list any required evidence, path, or token strings verbatim when present, and add at least one evidence pointer.  
* **QA verification register detail — SHOULD.** For each QA step, prefer a human-readable verification label, include the verbatim check anchor, state the required evidence outputs and stated pass or fail posture, and add the decisive evidence pointer.  
* **PF10 results register detail — SHOULD.** Prefer a short result claim summary rather than an opaque result ID. Record whether the decisive PF10 addendum gives direct `Evidence pointer:` lines or only evidence-basis prose, and say `none provided` explicitly when no direct pointer lines exist.  
* **PF23 reality summary detail — SHOULD.** For each PF23 reality item, summarize the surface or component, list the verbatim paths or components, and state the closeout impact as supports, partial, not addressed, or contradicts.  
* **Closure trace ledger evidence hooks — SHOULD.** Each closure-trace entry should map the deliverable to its QA verification items, PF10 result claims, PF23 reality check, status, why, and the decisive evidence pointers.  
* **Path and surface reality ledger — SHOULD.** When closure depends on both repo paths and surfaced routes, use a path-and-surface reality ledger. Record the verbatim path or surface string, the proving source or sources, the status, whether it is required for closure, and why it matters.  
* **Accepted execution deviations — SHOULD.** If the closure judgment depends on an approved rerun, dependency-preflight correction, rails exception, or other bounded deviation, surface that deviation explicitly in the closure review rather than leaving it implicit inside PASS-only prose.  
* **Auditability caveat for decisive PF10 authority — SHOULD.** If the decisive PF10 close-authority addendum uses evidence-basis prose rather than direct `Evidence pointer:` lines, state that explicitly as an auditability caveat and keep it separate from the closure-truth judgment.  
* **Closure decision prose — SHOULD.** In the final closure decision, state the binary verdict, then explain the verdict with short evidence-grounded prose rather than only a label.

Purpose

* Determine whether the epic can be formally closed, and if not, the minimum follow-ups required.

Inputs posture

* Optional inputs provided:

  * Implementation Plan: \<Yes | No\>

  * Live QA Plan: \<Yes | No\>

  * Other named inputs: \<list or None\>

* SoT posture:

  * PF10 is the primary record of what happened and what was implemented.

  * PF23 is required for reality alignment when components, pathnames, or surfaced loci matter.

  * PF-Canon is normative where PF10 is silent.

  * Check-scoped deliverables reports are admissible QA proof only when they land under the canonical epic QA root and check directory, and do not rely on per-run nesting as a correctness key.

Closure registers (anchor-based; no invented rows)

A) Deliverables list (from Implementation Plan)

* Deliverable or PR: \<identifier\>

* Source: \<source doc and section\>

* Anchor quote: "\<verbatim line\>"

* Explicit required evidence, path, or token strings (verbatim, where present):

  * \<string 1\>

  * \<string 2\>

B) QA verification list (from Live QA Plan)

* Check ID: \<stable step identifier\>

* Source: \<source doc and section\>

* Anchor quote: "\<verbatim line\>"

* Pass or fail posture: \<Present | Missing | Partial\>

C) PF10 results list (closure-relevant)

* Result ID: \<stable result identifier\>

* Source: \<source doc and section\>

* Anchor quote: "\<verbatim line\>"

* Evidence pointers or paths (verbatim, where present):

  * \<path or pointer 1\>

  * \<path or pointer 2\>

* Outcome label (verbatim as written): "\<verbatim line\>"

* Note (optional): \<integrity or labeling note\>

D) PF23 reality surfaces list (closure-relevant)

* Surface ID: \<stable surface identifier\>

* Source: \<source doc and section\>

* Anchor quote: "\<verbatim line\>"

* Paths or components (verbatim):

  * \<path or component 1\>

  * \<path or component 2\>

Closure trace ledger (mandatory)

* Deliverable or PR: \<identifier\>

* Mapped QA step(s):

  * \<check 1\>

  * \<check 2\>

* Mapped PF10 result(s):

  * \<result 1\>

  * \<result 2\>

* PF23 reality check: \<Confirmed | Not asserted | Partial\>

* Status: \<Satisfied | Partially satisfied | Not satisfied\>

* Why: \<one sentence grounded in evidence\>

Path proof ledger (closure-critical; no placeholders)

* Path string (verbatim): \<path\>

* Normalized audit/qa form: \<normalized path or n/a\>

* Required for closure: \<Yes | No\>

* Status: \<Proven in PF10 | Proven in PF23 | Proven in report | Plan-only | Not present\>

* Notes: \<one sentence\>

* Mixed-case audit/qa drift: \<None observed | Describe\>

Closure decision (binary)

* Epic closure decision: \<SATISFIED | NOT SATISFIED\>

If NOT SATISFIED: minimal follow-ups required

* \<follow-up 1\>

* \<follow-up 2\>

### **15.19 Lead dev epic retrospective template**

Use this when you need a grounded retrospective after closure or near-close that summarizes what the epic delivered, what worked, what failed, and what should change next.

* **Executive summary grounding — SHOULD.** State what the epic set out to do, what it actually delivered, the biggest wins, and the biggest remaining risks or gaps, and ground those statements in the reviewed source set.  
* **Implementation report shape — SHOULD.** When the epic was delivered through PRs, OPS tasks, and QA steps, break the implementation report down that way. For each item, record the purpose, key changes, key surfaces touched, tests or evidence produced, the outcome, and the decisive evidence pointer.  
* **Evidence inventory and evidence gaps — SHOULD.** Include both the concrete evidence inventory and an Evidence gaps subsection when raw artifact bodies were not reviewed directly or when a decisive source relied on summary prose.  
* **Process retrospective specificity — SHOULD.** Keep separate blocks for what went well, what did not go well, and what was learned about process. Surface accepted execution deviations or remediation-loop lessons explicitly when they materially shaped the outcome.  
* **Application or system retrospective specificity — SHOULD.** Keep system lessons separate from process lessons. Track remaining risk or debt under Must-fix, Should-fix, and Nice-to-have so the priority signal is preserved.  
* **ADR record completeness — SHOULD.** For each ADR, record the decision point, the options considered when visible, the PF-canon constraints relied on, the final decision for this epic, whether it should become canonical for future work, and the decisive evidence pointer.  
* **ADR disposition labeling — SHOULD.** When helpful, label the ADR as NEW CANON PROPOSAL, Epic-only clarification, or Historical only so the future-drain posture is explicit.  
* **PF-canon doc-delta completeness — SHOULD.** Do not stop at a bare doc title. For each proposed PF-canon delta, record the target doc, the target section or closest stable home, the delta itself, why that doc is the correct home, and the supporting evidence pointer.  
* **Future-work record shape — SHOULD.** For each build improvement or future-work item, record the short description, where it should live, which PF docs would be touched if pursued, and whether it depends on PF23-identified reality drift.  
* **Recommendation-only closeout posture — SHOULD.** End with a recommendation-only section that states the readiness or closure recommendation, the most important process improvement, the most important system-level follow-up, whether any additional hard requirement appears necessary before close, and the final implementation posture recommendation.

Title line format:

* `\<ADDENDUM_ID\> Lead Dev Epic Retrospective — \<EPIC_ID\>`

Executive Summary

* What the epic set out to do and what it delivered (grounded): \<short paragraph\>

* Biggest wins:

  * \<win 1\>

  * \<win 2\>

* Biggest remaining risks or gaps:

  * \<risk 1\>

  * \<risk 2\>

Implementation Report (What happened in the repo)

* PR or step breakdown:

  * \<PR or step 1\> — \<purpose, evidence, outcome\>

  * \<PR or step 2\> — \<purpose, evidence, outcome\>

* Major surfaces affected:

  * \<surface 1\>

  * \<surface 2\>

* Evidence inventory:

  * \<artifact or evidence family 1\>

  * \<artifact or evidence family 2\>

Retrospective (Process)

* What went well:

  * \<item 1\>

  * \<item 2\>

* What did not go well:

  * \<item 1\>

  * \<item 2\>

* What we learned (Process):

  * \<lesson 1\>

  * \<lesson 2\>

Retrospective (Application / System)

* What we learned about the system itself:

  * \<lesson 1\>

  * \<lesson 2\>

* Known remaining risks or debt:

  * Must-fix: \<item or None\>

  * Should-fix: \<item or None\>

  * Nice-to-have: \<item or None\>

ADRs and Ambiguity Resolution

* ADR-01

  * Decision point: \<one sentence\>

  * Options considered:

    * \<option 1\>

    * \<option 2\>

  * PF-Canon constraints: \<PF doc title and section\>

  * Final decision: \<one sentence\>

PF-Canon Doc Deltas (Dev / Process)

* Doc Deltas: \<None | list of PF titles and short deltas\>

Build improvements and future work

* Improvement: \<one sentence\>

  * Where: \<future tooling card | backlog | future epic\>

  * Depends on observed risk: \<Yes | No\>

Recommendations and closeout posture (recommendation only)

* Phase-close recommendation: \<recommended | not recommended\>

* Most important improvements (non-blocking):

  * \<improvement 1\>

  * \<improvement 2\>

* Implementation posture recommendation: \<READY | READY WITH CAVEATS | NOT READY\>

---

## 

## **Appendix A — Full Document Assessment Protocol (Technical Writing)**

### **Policy (normative)**

1. Never alter document control fields, title, version, status, effective date, or update gate. If drift exists, report it, but do not redline it.

2. Use “placement anchors” copied verbatim from the target PF doc, not the source blob.

3. If any relied-on passage appears truncated or incomplete, stop and re-open until complete.

4. Prefer H3/H4 for in-between additions (for example, add `### 12.4` under `## 12 <SECTION_TITLE>`) so you do not need new H2s.

5. Never renumber headings.

6. If a change is too large, propose it as a bounded task plan with stepwise acceptance.  
---

### **Workflow**

2. Structure map extraction: list all H1 and H2 in order (H3 if relevant); attach as evidence. **If new H1/H2 sections are added, ensure the structure map includes them and that all existing numbering remains unchanged.**

3. Editing: use the requested authoring surface; **preserve existing H1/H2 numbering, titles, and order exactly;** keep changes minimal and localized. Prefer adding content under existing H2s as H3/H4. If a new H1/H2 is required, append it using the next available number and do not shift any existing numbering.

4. Verification: confirm **existing H1/H2 numbering and order are unchanged;** confirm titles-only cross-refs; confirm no duplicated bytes.

---

### **Acceptance & Evidence**

H1H2\_PRESERVED\_OK — **Existing** H1 and H2 numbering, titles, and order verified unchanged. If any new H1/H2 sections were added, they use the next available number and do not alter existing numbering.

---

### **Verification checklist**

\[ \] Existing H1/H2 preserved (numbering, titles, order unchanged; any new H1/H2 uses next available number)  
 \[ \] Titles-only cross-refs  
 \[ \] No duplicated bytes  
 \[ \] Doc delta prepared  
 \[ \] Registry and Evidence Index updated

