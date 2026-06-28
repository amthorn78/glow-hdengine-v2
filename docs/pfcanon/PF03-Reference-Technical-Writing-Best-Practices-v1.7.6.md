## **0\) Front Matter — Document Control**

**Title:** PF03-Reference-Technical-Writing-Best-Practices

**Version**: v1.7.6

**Status:** Reference

**Effective date:** 2026-06-27

**Last Update Gate:** BN 11.7.4 A20-34

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

Retrieval-first review posture — MUST. For plan, remediation guide, QA plan, repo audit, closeout, and related review work, AI agents must retrieve current sources before relying on memory, summaries, partial snippets, display-layer artifacts, or guessed repo loci.

Proof-first source order — MUST. Use PF10 first where it explicitly speaks, then the current artifact under review, then the owning PF canon home for each issue, then repo-reality proof for claims about paths, commands, endpoints, environment variables, test IDs, artifact paths, or component homes.

Tool-order rule — MUST. Use full-source retrieval first for uploaded or current documents. Use minimal container inventory commands only when repo reality matters. Use exact-string `rg -n --fixed-strings` before regex `rg` for known literals. Use broad semantic search only after exact search cannot prove the claim.

Known literals require exact search first — MUST. Known literals include task IDs, subtask IDs, token names, headings, route strings, command strings, filenames, artifact keys, environment variable names, and other exact strings.

Unknown stays unknown — MUST. Any unproven locus, path, route, command, flag, token spelling, or environment variable name must remain UNKNOWN or BLOCKED until proven. Do not guess it into existence.

Review findings require verbatim proof — MUST. Findings must distinguish canon requirement, observed repo reality, and inference, and must anchor blockers or approvals to verbatim source text and controlling proof.

Web lookup is not source truth for in-session artifacts — MUST NOT. Web lookup must not substitute for uploaded-file truth, PF document truth, or repo-local proof when those sources govern the review.

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
* Rendered escapes do not break placement proof — MUST. Placement quotes, proof excerpts, review quotes, and redline anchors must be judged against raw source text or the actual pasted target text, not assistant-rendered previews.  
* Quote-equivalence under rendering — MUST. If the only difference between a quote and the raw source is display-layer escaping introduced by assistant output, markdown rendering, copied chat text, or preview panes, treat the quote as source-equivalent.  
* Redline cleanup requires source-real defect — MUST. Do not draft corrective redlines solely to remove display-layer escape artifacts. A cleanup redline is allowed only when the raw target document, raw source document, or governed artifact actually contains the unwanted escape character and the defect changes meaning, placement, execution, or governed identity.  
* Reject rendered-escape cleanup blockers — MUST. When a review requests escape-character cleanup but source-level verification shows the unwanted character is absent from the raw source, reject the blocker as display-layer artifact rather than drafting a redline.  
* Non-literal command or snippet examples are allowed — SHOULD. Technical documents may include illustrative commands, snippets, helper code, heredocs, shell lines, or examples when proof intent is clear and the artifact is not claiming a canonical invocation contract.  
* Syntax cleanup is editorial polish — MUST. Do not draft redlines solely to make command syntax, helper code, heredocs, escaped strings, code-block wrapping, shell lines, or examples paste-ready or syntactically exact unless the PO specifically asks for syntax cleanup or the source-real defect changes meaning, placement, execution, proof target, authority, scope, safety, acceptance posture, or governed identity.  
* Redline cleanup must not become approval gating — MUST NOT. A syntax-polish redline may improve readability, but it must not be treated as required for plan approval, QA readiness, implementation readiness, closeout readiness, or acceptance unless the source-real defect changes a non-syntax truth or proof dimension.

**Example (good):**

* Place: `HDE-Governance §8 → INSERT AFTER "Binary markers — Implemented"` and before §9.

* Operation: `ADD` new `§8.4 "Caching & Keys (Reader) — MUST"`.

* Text: \<verbatim subsection, including the `§8.4` heading and body\>

* Acceptance impact: `READER_SUCCESS_ENDPOINTS_OK` added; **9\) Build Notes (Living) usage**

Append-only blocks — MUST. The writer delivers a **self-contained Addenda Block**; the PO pastes it at the end under “Addenda (append-only)”.

Delete-on-merge — MUST. After the PF target is updated, the PO **deletes** the block (or archives by versioning the doc).

No in-doc edits by AI — MUST. AI lead devs are **read-only** for Build Notes; edits occur in the target PF.

PF10 reference posture — MUST. When referencing Build Notes from other documents or reviews, reference Build Notes by **addendum number \+ addendum title** (for example, “Build Notes Addendum 2.10 — Token Load Reduction \[OMITTED\]”). Do not reference PF10 by version strings or PF10 section numbers as durable anchors; the stable unit is the addendum entry itself.

PF10 staging addenda for documentation outcomes — SHOULD. When a retrospective, review, audit analysis, or closeout report proposes temporary PF10 staging rather than immediate permanent drain, include these fields: addendum title, why, decision or rule or clarification, drain targets, supersedes or conflicts if any, and implementation impact.

Supportable-versus-drained staging — MUST. If the addendum stages status-drain effects, distinguish supportable-from-evidence posture from already-drained canon and preserve reused-history foundations separately from newly implemented work.

Implementation impact declaration — SHOULD. For documentation-only staging addenda, state whether the proposal changes code, acceptance tokens, evidence homes, or only documentation posture.

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

Approval-submitted planning artifacts require `ASK OK?` — MUST. Any Epic Plan, Implementation Plan, QA Plan, remediation plan, or other plan-form artifact submitted for approval before execution MUST include the `ASK OK?` approval sentinel.

`ASK OK?` is substance-bearing and non-blocking — MUST. Reviewers MUST NOT classify the sentinel as stray text, formatting noise, or a blocker merely because it appears in the document.

Approval-submission and reviewer verdict are separate surfaces — MUST. `ASK OK?` inside the plan is the plan’s approval-submission sentinel. `ASK OK` as a review response final verdict is a separate reviewer-output convention and must not be conflated with the plan sentinel.

Missing sentinel may block approval — MUST. If the artifact is submitted for approval and the required sentinel is absent, record that as a missing required approval marker rather than as a style preference.

Minimal questions — SHOULD. Ask only what blocks precision; otherwise proceed and mark unknowns **\[OPEN\]**.

Error reporting — MUST. If a tool/canvas action fails, state the failure plainly and supply the paste-ready content or JSON alternative.

Escalation — SHOULD. If doctrine conflicts, cite governing PF titles and § numbers; propose the smallest corrective redline.

QoS stop-rule for repeated structural remediation — MUST. If the same structural failure mode recurs after one corrective pass, stop incremental plan edits and escalate to a root-cause correction by updating the controlling template or canon rule, then rerun the authoring pass. Drain targets MUST describe the failure class, not the incident.

Determinism in thread — MUST. Keep terms, tokens, and headings consistent inside a session; do not rename mid-flow.

### 12.1 Engineering docs / QA plans (Live QA pattern)

Engineering docs such as Live QA plans are action lists, not narratives. When the PO asks for a Live QA plan, the writer MUST treat it as a mechanical script that another person or agent can run without interpretation.

Live QA plans MUST follow these patterns:

* One objective-first directive per step. Present each step as a directive that names the proof target, scope boundary, expected evidence family, and verdict posture. Plans MUST NOT be required to provide paste-ready, literal, or syntax-perfect command lines.  
* Non-literal proof instructions are allowed — MUST. Live QA steps may express the intended proof action in operational language, pseudocode, structured prose, approximate command form, or illustrative snippet form when the proof target, scope boundary, rails posture, and expected verification are clear.  
* Mechanical evidence only. Step PASS and FAIL decisions must be grounded in artifacts and paths. Where command details matter, require the execution transcript, step log, generator output, or other listed Deliverable rather than embedding brittle command exactness in the plan.  
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
* Runtime warnings require explicit classification — MUST. If a QA harness, tool, command, or helper emits a warning, the QA report or review must state whether the warning is tooling-blocking, fail-tooling, fail-behavior, non-fatal, or non-driving for the verdict.  
* Non-fatal warnings are not automatic blockers — MUST. A warning such as a deprecation warning does not block PASS by itself when the governed evidence records no tooling-blocked, fail-tooling, or fail-behavior condition and the required proof remains trustworthy.  
* Warning caveats must remain separate from verdicts — SHOULD. Record non-driving warnings as caveats or follow-up candidates, not as behavior failures or tooling failures, unless the warning affects evidence trust, command runability, secret posture, or verdictability.

These conventions keep Live QA plans mechanical, fair to the operator, and honest about the difference between “the app failed” and “our harness is not capturing the run.”

### **12.3 Command and procedure style (QA plans)**

* **Prefer directive-first steps — MUST.** Live QA steps SHOULD be written as objective-first instructions, not as speculative implementation narratives.  
* **Discovery-first posture — MUST.** A Live QA Plan MUST assume that any repo detail not proven is unknown until discovered during the run.  
* **No inferred repo-resident loci — MUST NOT.** Do not infer, fill in, pattern-match, or scaffold repo-resident locus strings or app-topology claims. If a plan names a repo-resident locus or an exact command string, it MUST be copied verbatim from an allowed provenance source or recorded as a discovered runtime fact in step evidence.  
  **Command-line minimalism — MUST.** Plans MUST NOT over-specify command lines. State the goal, the observable outputs that matter, and the evidence that must be captured.  
* **Runtime command capture — MUST.** The executor MUST record the exact commands actually used into the check evidence.  
* **QA-correctable command syntax defects are non-blocking — MUST.** A Live QA Plan, QA Plan, remediation plan, or plan-review artifact MUST NOT be blocked solely because a command note contains a syntax, quoting, escaping, punctuation, rendered-markup, or small local expression defect when the command identity, target check or artifact, intended classification, and proof obligation remain clear.  
* **Command identity controls over syntax perfection — MUST.** Plan reviewers MUST evaluate whether the approved command identity and proof target are preserved, not whether every command note is byte-perfect executable syntax at plan-review time.  
* **Correction boundaries — MUST.** A syntax correction is QA-correctable only when the executor can correct it without inventing a new repo locus, command source, route, artifact family, acceptance predicate, or PASS or FAIL criterion.  
* **Correction evidence — MUST.** When a QA executor corrects a plan command syntax defect during execution, the governed step evidence MUST record the exact command actually executed, the command provenance, the reason for correction, the produced evidence artifacts, and the final PASS, FAIL, or TOOLING classification.  
* **Real command blockers remain blockers — MUST.** A command defect remains blocking when it makes command identity ambiguous, points to the wrong artifact or predicate, changes acceptance semantics, depends on unavailable non-PF reconstruction, or requires guessing missing paths, endpoints, test names, token names, or repo loci.  
* **No speculative placeholders — MUST NOT.** Do not use placeholder routes, placeholder file paths, placeholder module names, placeholder commands, or “if it exists under X” scaffolding.  
* **Avoid “run this somewhere” prose — MUST.** Specify repo-root relative paths and deterministic file locations for plan-created outputs and check-scoped evidence.  
* **No `<PO_INPUT>` placeholders in step lists — MUST.** If PO input is needed, include it in a dedicated “PO inputs” section.  
  **Environment bootstrapping — MUST be explicit.** If the procedure requires environment bootstrapping, explicitly reference the standard bootstrap script and run the enforcement inside a subshell (for example, `bash -lc "<SUBSHELL_COMMAND>"`).  
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
* Governed structural-field predicates must be structural — MUST. If a QA check, remediation guide, or review depends on a required field in a governed repo artifact, the plan must define the structural predicate that proves the field exists, has the expected shape, and is semantically tied to the intended source.  
* Raw string presence is insufficient for governed fields — MUST NOT. Do not satisfy a governed JSON, manifest, mirror, artifact, or evidence-field predicate by raw substring visibility alone when the claim depends on field shape, field location, value derivation, or semantic binding.  
* Source-derived field proof must name derivation — SHOULD. When a field is required to be derived from observed attempts, provider order, runtime order, selection order, source rows, or another governed source, state that derivation explicitly in the PASS criterion or remediation proof.  
* Structural-field proof must preserve token posture — MUST. A structural-field proof must not create or imply a new acceptance-token claim unless the exact token is registered or otherwise admitted by the governing token authority.  
* Governed prose proof checks should be semantic — SHOULD. If a QA check, remediation guide, or review depends on governed prose rather than a machine-readable field, prefer stable semantic checks, case-normalized checks, or canonical machine-readable fields when available.  
* Case-only prose mismatch is not final behavior proof — MUST NOT. Do not treat casing-only or prose-format mismatch as final behavior failure when the raw artifact still supports the same semantic proof target.  
* Prose-proof remediation must preserve proof target — MUST. If a prose-bound proof check is remediated, the remediation record must state the original brittle predicate, the normalized or semantic predicate used, and why the proof target, scope boundary, rails posture, and PASS/FAIL criteria remained unchanged.  
* **Gitless runbooks — MUST.** Live QA runbooks MUST NOT include git gating (including “working tree clean”) as PASS/FAIL criteria. If traceability capture is needed, it MUST be artifact-only and non-blocking.  
* **No manual-fill placeholders — MUST NOT.** No QA evidence file may include “fill in PASS/FAIL” or other manual-entry placeholders. If a result is “no deltas,” the generator MUST emit that explicitly as produced output.

* **No manual edits to QA evidence — MUST NOT.** QA plans and runbooks MUST NOT instruct an operator to open evidence files (logs, manifests, reports, or READMEs) in an editor and type changes by hand. If a summary must change, the correct procedure is to rerun the generator so the result remains reproducible.  
* **Step log header inputs — MUST.** If a plan step relies on a governed step log (for example `primary.log`) as a Deliverable, the plan MUST ensure the log is generated by the harness and includes its machine header. If the header writer depends on env var inputs, the plan MUST export the required canonical env vars in the step context (not as an ambient global). Missing required exports is a mechanical blocker for claiming PASS based on that evidence.  
* **Bounded approved deviations must be recordable — MUST.** If a step may require a bounded approved deviation from the default rails or execution posture, the plan MUST say who may approve it, what condition can trigger it, and which governed file records the approval.  
* **Default posture and executed posture must both be preserved — MUST.** The plan or later deliverables report MUST preserve both the default approved posture and the actual executed posture for that step. Do not collapse the deviation into the normal path or hide it inside narrative prose.  
* **Deviation scope stays step-local — MUST.** A bounded approved deviation for one step MUST remain tied to that step unless the plan is formally revised. Do not treat a step-local deviation as a blanket plan-wide change.  
* Bounded Moon Loop correction is QA-root limited — MUST. A bounded Moon Loop may correct only QA-created evidence harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects under the approved QA root and within the approved step scope.  
* Non-QA-root changes are remediation work — MUST. A change to product code, repo tests, repo evidence generators, governed artifacts outside the approved QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction.  
* Non-QA-root remediation must be routed — MUST. Non-QA-root remediation must be routed through an approved work item type such as PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE before a final QA review may rely on the corrected state.  
* Routing proof is required before acceptance — MUST. If a QA verdict relies on non-QA-root remediation, the report or review must cite the approved work item, routing evidence, commit lineage or equivalent governed proof, and post-remediation rerun or validation evidence.  
* Do not relabel routed remediation as QA-only correction — MUST NOT. Once a defect is corrected through PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE routing, preserve that routing in the review language and do not rewrite it as bounded Moon Loop-only correction.  
* **Deferred evidence labeling in templates — MUST.** Any QA plan template, deliverables report, closure record, or rollup that enumerates step-scoped evidence paths MUST explicitly label future-step artifacts as `NOT RUN` or `DEFERRED` until the producing step has executed.  
* **Do not treat deferred artifacts as missing evidence — MUST.** When writing summaries, evidence prints, or rollups, `NOT RUN` and `DEFERRED` states MUST remain distinct from missing evidence findings. Do not describe `NOT RUN` or `DEFERRED` artifacts as missing evidence.  
* **Plan-conditional evidence is not missing evidence — MUST.** If a plan states that a deliverable is produced only when a named condition is met, QA summaries and evidence prints MUST record the artifact as `Not applicable` or `not required because condition not met` when that condition is not met. Do not report such artifacts as missing evidence.  
* **Input-availability gates are planning defects when the plan becomes structurally unreachable — MUST.** If a step’s PASS criteria require inputs that are unavailable, invalid, or explicitly should not be expected for the current product state, the step MUST be described as blocked by an input-availability gate and treated as a planning defect or plan/product mismatch, not as a demonstrated behavior defect.  
* **Rerun posture for planning defects — MUST.** In this situation, QA summaries MUST NOT prescribe a rerun as remediation unless the required inputs later become valid or the plan is corrected. Missing downstream artifacts caused solely by the blocked precondition MUST be interpreted in light of the planning defect.  
* **Live QA role must be proof-bounded — MUST.** Live QA plans, deliverables reports, and reviews must state whether the step proves current evidence state only or also performs an authorized remediation action.  
* **Proof-only Live QA does not perform implementation or closeout — MUST.** If the step is proof-only, the report must not imply implementation work, remediation work, PF edits, closeout action, PF09 drain, acceptance-token claim, or permanent canon update.  
* **Authorized remediation stays separately labeled — MUST.** If a bounded remediation is authorized during Live QA, label it as remediation or evidence repair, preserve the failure-to-rerun history, and do not rewrite it as product implementation or closeout completion.  
* Unavailable initial failure artifacts must be declared — MUST. If an initial failing artifact, log, hash, timestamp, result body, or command capture is overwritten, unavailable, or not preserved by the time remediation begins, the remediation record must state that the initial failure artifact is unavailable.  
* Missing failure artifacts must not be reconstructed — MUST NOT. Do not reconstruct missing logs, hashes, timestamps, result bodies, command output, or evidence content from memory, surrounding summaries, later artifacts, or inferred state.  
* Later remediation proof stays later proof — MUST. If the final rerun or remediation proof is valid, write it as final proof while preserving the unavailability of the initial artifact as an evidence-history limitation.  
* **Non-claim posture must be explicit — SHOULD.** When Live QA proves that a behavior or closure class is not claimed, state the non-claim directly and keep it separate from the PASS verdict.  
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
* **Machine-sensitive escape blockers require source-byte proof — MUST.** A blocker for escaped underscores, backslashes, or similar rendered escape characters in a path, artifact path, script path, command name, check name, token name, environment variable name, endpoint string, JSON key, evidence filename, manifest filename, hash filename, or path-proof filename is valid only when the reviewer proves the literal source artifact contains the escaped characters and that the source-real escaping changes executable meaning, portability, canonical quote validity, or evidence-path validity.  
* **Rendered copies are not proof — MUST.** Reviewer output, copied quotes, chat transcripts, markdown display, retrieval formatting, or assistant-generated review text do not prove that the reviewed source document contains literal escape characters.  
* **Acceptable proof before blocking — MUST.** Before blocking on escaped machine-sensitive strings, the reviewer must use raw file text, a byte-preserving excerpt, an explicit source-view excerpt, or a deterministic source search that proves the literal escaped string exists in the artifact under review.  
* **Unavailable source-byte proof is non-blocking — MUST.** If source-byte proof is unavailable, the reviewer must not state that the plan contains escaped characters. The reviewer may state only that rendered review text shows escaped characters and source-byte proof is not available.  
* **Correct issue framing — SHOULD.** If the source is clean, write that the escaped character appeared only in rendered review output. If the source is defective, identify the raw source string and explain the executable, portability, quote-validity, or evidence-path consequence.  
* **Escape-character blocker proof packet — MUST.** A valid escape-character blocker must include the raw or source file or artifact inspected, the exact read-only command or source-view method used, the raw line showing the unwanted escape character, why the character changes executable, governed, canonical, or semantic identity, and why the issue is not merely assistant or markdown rendering.  
* **Incomplete escape-character proof is invalid — MUST.** If any part of the required proof packet is missing, the issue must be withdrawn or reclassified as a display-layer artifact.  
* **Escape-character status classification requires source proof — MUST.** Do not classify rendered escape characters as FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, acceptance failure, path-proof failure, canonical path failure, token spelling failure, quote-verbatim failure, PF locator failure, implementation blocker, or closeout blocker unless the raw or source artifact proves the underlying defect.  
* **Valid escape blocker wording must name source truth — MUST.** Use source-level wording that names the inspected source, the raw defective string, the proof method, the governing expected identity, and the material consequence.  
* **AI-rendered escape characters are categorically non-blocking — MUST.** Escape characters introduced or possibly introduced by AI rendering, markdown rendering, transcript formatting, quote formatting, assistant output, or review-ledger formatting MUST NOT be used as a Blocker in plan review.  
* **Machine-sensitive identity remains the review test — MUST.** This non-blocking rule applies even when the affected string is machine-sensitive. Reviewers must evaluate whether command identity, artifact identity, path identity, token identity, evidence identity, and proof obligation remain clear after ignoring rendered escapes.  
* **Block only on the underlying non-rendering defect — MUST.** A blocker is valid only when a substantive defect remains after removing or ignoring the rendered escape layer, such as missing command identity, missing deliverables, wrong proof target, unsafe execution posture, canon conflict, or an unproven repo locus.  
* **Do not ask authors to fix rendered escape artifacts — MUST NOT.** Reviewers must not ask the PO, plan author, or redline author to revise rendered escape characters when the source meaning and proof identity are clear.  
* **Reviewer self-check before escape-related blockers — MUST.** Before issuing any blocker that mentions escaped characters, backslashes, markdown escaping, rendered paths, rendered shell syntax, or rendered code syntax, the reviewer must ask whether the issue would still block if the rendered escape characters vanished. If not, do not emit the blocker.  
* **Required internal disposition — SHOULD.** When an escape artifact is noticed but command identity and proof target remain clear, use this disposition: Rendered escape characters ignored under PF10 2.7; no blocker because command identity and proof target remain clear.  
* **BLOCKERS** (`BLK-01`, `BLK-02`, \[LIST CONTINUES\]): any item that prevents execution of the plan or invalidates the run.  
* **CAVEATS** (`CAV-01`, `CAV-02`, \[LIST CONTINUES\]): risks, uncertainties, assumptions, or optional improvements that do not block execution.  
* **Prohibited ellipsis patterns are mechanical blockers — MUST.** Treat any occurrence of the Unicode ellipsis character (U+2026) or the ASCII triple-dot sequence as a BLOCKER in plan approval reviews. Replace with approved omission markers or move the literal string into a repo file and reference it by exact path and filename.  
* **Heading marker levels are non-reviewable — MUST NOT.** Reviewers MUST NOT block approval based on heading marker levels or require heading-level changes as a condition of approval. Review required sections by the heading text and required content, not by the markdown level.  
* **Non-blocking plan formatting variance — MUST.** Formatting variance that is purely presentation (bullet marker choice, indentation, line wrapping, extra blank lines, tables vs bullets, emphasis style) is not a blocker. Record such notes as CAVEATS or follow-ups only.  
* **Markdown-only wrappers are non-blocking when meaning is unchanged — MUST.** In Epic Plans, QA Plans, reviews, remediation guides, closeout memos, and other planning or review documents, inline backticks or other markdown-only wrappers around a label, PF title, task ID, subtask ID, token name, or human-readable literal MUST NOT block approval by themselves when the required field, content, ordering or adjacency, and meaning are unchanged.  
* **Wrapper differences cannot alter machine-sensitive literals — MUST.** This non-blocking posture does not apply when the wrapper changes or obscures executable commands, code, schemas, JSON, token spelling, path strings, endpoint strings, or other bytes whose literal interpretation matters.  
* **Substance-over-markup review test — MUST.** For required planning fields, reviewers must ask whether the required text is present in substance and in the required place, not whether the field is rendered without inline-code styling.  
* **Formatting becomes a blocker only when it impacts meaning or execution — MUST.** Treat as BLOCKERS only when the variance causes missing required sections or fields, changes semantics, makes commands non-copyable, breaks step IDs or evidence filenames, or otherwise prevents safe execution and evidence capture.  
* **Template hygiene materiality rule — MUST.** A planning artifact, review artifact, remediation guide, QA plan, implementation plan, or closeout artifact must not be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table order, heading style, punctuation, spacing, bold markers, or presentation style unless the defect materially changes truth, proof, acceptance, execution safety, source authority, portability, scope, evidence identity, evidence trust, OPS or PR boundary, public or private surface posture, canon conflict handling, or closeout truth.  
* **Template hygiene default severity — MUST.** If the issue does not materially affect one of those review-critical dimensions, classify it as a Nit, Suggestion, or Caveat rather than a Blocker.  
* **Valid blocker classes remain valid — MUST.** Valid blockers include active PF10 contradiction, unresolved ADRs on topics already resolved by PF10, routing to a new PF10 addendum when an applicable PF10 addendum already exists, unregistered acceptance-token claims, Already Implemented claims without embedded proof or allowed proof pointer, required external-source consultation by Codex, OPS work required inside Codex PR work, asserted repo loci without proof or discovery-first posture, unsupported public-surface widening, PF23 misuse as deliverable or authority, and PF20 misuse as current planning or acceptance authority.  
* **Non-blocking template hygiene examples — SHOULD.** Missing inventory rows, imperfect quote-block formatting, provenance labels such as CA vetted or vetted repo fact, section phrasing that is semantically correct but not template-perfect, inventory-row ordering, and missing titles-only polish should be raised as Caveats, Suggestions, or Nits when the artifact remains self-contained and truth, proof, portability, and execution are preserved.  
* **Epic Plan review boundary — MUST.** Epic Plans are planning records, not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories. Epic Plan reviews should block only when intended scope, PF09 completion mapping, deliverable boundaries, acceptance-token truth, canon hierarchy, phase fidelity, execution separation, or downstream planning portability cannot be safely preserved.  
* **Implementation Plan review boundary — MUST.** Implementation Plans must be concrete enough for Codex and OPS boundaries, but a formatting defect is not a blocker unless it creates real Codex ambiguity, OPS ambiguity, source-authority ambiguity, proof ambiguity, or execution ambiguity.  
* **Embedded provenance facts are portable when self-contained — MUST.** If a plan embeds the needed fact and Codex can proceed without consulting CA, audit files, attachments, chat history, implementation guides, or other non-PF sources, imperfect provenance wording or quote-block formatting is not a blocker. If the plan requires Codex to consult those external sources, it is a blocker.  
* **Reviewer burden for blockers — MUST.** A reviewer who wants to block must state the material harm and tie it to truth, proof, acceptance, execution, source authority, portability, scope, evidence trust, or closeout truth. Do not issue revise-and-resubmit language for template polish alone.  
* **Plans are not execution artifacts — MUST.** QA Plans, Epic Plans, Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, and closure-review artifacts MUST NOT be blocked, rejected, returned for revision, or classified as REVISE AND RESUBMIT solely because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, escaped character, or helper-code block is not paste-ready, literal, syntactically exact, or executable as written.  
* **Source-real syntax defects are not approval blockers by themselves — MUST.** This non-blocking posture applies even when the syntax issue appears in raw source text and even when the reviewer believes the command would fail if pasted directly, provided the proof target, step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture remain unchanged.  
* **In-flight syntax normalization is execution hygiene — MUST.** If a QA operator, Codex, Kronos, PO, or implementation owner encounters a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue during execution, the operator may normalize it in flight while preserving the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture.  
* **In-flight normalization does not require planning churn — MUST NOT.** In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or a QA Plan revision unless the underlying proof target, scope, or authority changes.  
* **Syntax-only objections cannot be disguised as truth/proof blockers — MUST NOT.** A reviewer must not disguise command syntax, paste-readiness, escaping, indentation, heredoc form, shell syntax, helper-code formatting, or command exactness complaints as truth, proof, evidence, token, path-proof, PF locator, implementation, QA-readiness, closure, behavior, tooling, or acceptance blockers.  
* **Syntax concern severity vocabulary — MUST.** Command and syntax concerns in plan review may be classified only as Non-issue, Note, In-flight normalization, or Operator caution when they do not change truth, proof, scope, authority, safety, acceptance, phase, or evidence identity.  
* **Syntax concerns are not failure states — MUST NOT.** Do not classify syntax-only concerns as Blocker, approval blocker, QA readiness blocker, implementation readiness blocker, closure blocker, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, acceptance failure, path-proof failure, evidence failure, token failure, PF locator failure, or command-validity failure requiring plan revision.  
* **Reviewer burden for revise-and-resubmit — MUST.** Any reviewer returning REVISE AND RESUBMIT must state the non-syntax truth or proof reason. If the objection can be fixed by editing command syntax, escaping, indentation, heredoc form, shell syntax, or helper-code formatting without changing the proof target, it is not a blocker.  
* **Live QA Plan approval is operational readiness — MUST.** A Live QA Plan should be approved when it is safe, self-contained, phase-bounded, and clear enough for the assigned operator to execute the QA run and produce a meaningful governed verdict.  
* **Live QA Plan approval is not byte-perfect lint — MUST NOT.** Do not block Live QA Plan approval solely for rendered escape characters, markdown or AI-rendered backslashes, heading style, bullet style, table style, quote-block formatting, code-block formatting, whitespace, punctuation, line wrapping, command syntax polish, command invocation style, interpreter choice that does not change operational behavior, exact shell spelling, exact command ordering that is not required for safety or proof, evidence-ledger byte-shape polish, path-proof transcript field polish, canonical JSON compactness wording, or step-log header polish at plan approval.  
* **Operational blocker materiality test — MUST.** A Live QA Plan approval blocker is valid only when the issue affects safe execution, required QA step coverage, required deliverable existence, explicit PASS/FAIL verdictability, rails posture, secret handling, live-provider or external-action boundary, public or private surface boundary, token truth, acceptance overclaim, source authority, self-contained execution, evidence trust, proof target identity, repo-locus truth where the plan requires an existing locus, OPS/QA/implementation category separation, phase scope, or closeout truth.  
* **Exact-command mismatch needs operational harm — MUST.** A command mismatch is a blocker only when it would likely run the wrong tool, prove the wrong target, open unsafe rails, expose secrets, mutate prohibited state, prevent the check from running, or create a false PASS or false FAIL with no safe fallback.  
* **Equivalent safe commands are caveats — SHOULD.** If a different invocation can produce the same proof under safe rails and actual command capture is required, classify the issue as a Caveat, Suggestion, or execution note rather than a blocker.  
* **QA-created harnesses need creation posture, not prior repo existence — MUST.** Reviewers must not require repo-existence proof for a harness the plan explicitly creates during QA. A QA-created harness issue is a blocker only when the creation instructions are not executable enough, the harness is unsafe or out of scope, the harness changes implementation behavior, the harness proves the wrong target, the harness cannot emit a verdict, or the harness cannot produce or point to required governed evidence.  
* **QA-created scaffolding style is non-blocking unless it blocks execution — MUST.** Formatting, indentation, line wrapping, and code style inside QA-created scaffolding are non-blocking unless they prevent creation or safe execution and no bounded correction is allowed during QA execution.  
* **Plan-approval evidence identity is enough — MUST.** At approval time, the plan must identify what each check proves, what result counts as PASS, what result counts as FAIL, where the QA run records the decisive receipt, which evidence family or evidence class supports the verdict, and how token claims are avoided unless registered and in scope.  
* **Byte-shape issues may still fail execution or closeout — MUST.** Canonical JSON compactness, field ordering, path-proof transcript shape, step-log header shape, mirror-record shape, and final evidence-index refresh mechanics may still fail QA execution or closeout validation. They are plan-approval blockers only when the plan lacks evidence identity, lacks a decisive receipt, relies on ungoverned evidence as decisive proof, or explicitly rejects required governed-evidence discipline.  
* **Live QA blocker severity mapping — MUST.** Use Blocker only when the issue prevents safe execution, invalidates the intended QA verdict, breaks source authority, creates token or acceptance overclaim, violates rails or secret posture, requires unavailable execution inputs, or makes required evidence untrustworthy. Use Caveat when there is operational risk but a safe default, bounded discovery path, or equivalent execution path preserves the QA verdict. Use Suggestion for clarity, usability, reviewability, or maintainability improvements. Use Nit for cosmetic, formatting-level, or presentation-only issues.  
* **Reviewer burden for Live QA blockers — MUST.** A reviewer who blocks a Live QA Plan must state the concrete operational harm. Exact command spelling, command wrapping, helper formatting, rendered escape characters, template polish, quote formatting, step-log header polish, and path-proof field polish are invalid blocker framing unless the reviewer ties them to concrete operational harm.  
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
* **Discoverable operational unknowns are not automatic deferrals — MUST.** When a plan, guide, QA-readiness action plan, remediation guide, or review encounters missing infrastructure, vendor, credential, environment, base URL, endpoint, route-family, OPS-root, or open-rails facts, classify the unknown explicitly. If the fact can be safely confirmed by PR discovery, QA discovery, PO-run OPS discovery, or PO-authorized open-rails work, route that bounded discovery instead of treating the item as deferred or out of scope. Do not guess values, expose secrets, or let discovery evidence claim QA PASS, OPS completion, PF09 status movement, acceptance-token satisfaction, or closure by itself.  
* **Evidence-bound scope for QA steps — MUST.** When a Live QA plan enumerates steps, each step MUST have explicit PASS and FAIL predicates and MUST identify the evidence output(s) it produces. For every token the plan intends to claim, the plan MUST name at least one step that produces the evidence needed for that token. Optional checks may be included only if explicitly labeled as informational (not acceptance).  
* **Production-affecting Live QA requires live proof — MUST.** A Live QA Plan for a production-affecting epic is not approval-ready unless it includes at least one bounded open-rails live QA step or a clear, authorized exemption. Production-affecting scope includes production surfaces, public or app-facing behavior, runtime compute, vendor ingest, external integrations, database persistence or retrieval, deployed service behavior, environment-variable or secret-binding behavior, request shaping, response mapping, authentication or authorization behavior, public Reader behavior, production-used CLI/API behavior, jobs, workers, schedulers, runtime services, or any path that must work outside isolated closed-rails fixtures.  
* **Closed-rails proof is not a substitute for required live proof — MUST NOT.** Unit tests, closed-rails fixture replay, static analysis, generated evidence, path-proof validation, Evidence Index refresh, Machine Mirror refresh, acceptance-map refresh, repo inspection, Codex audit, PF10 supportability notes, implementation review approval, QA Plan approval, written-but-unrun smoke procedures, and OPS discovery without live behavior proof may support the QA package, but they do not by themselves satisfy the required open-rails live QA step.  
* **Open-rails proof remains bounded — MUST.** The live step must be bounded, non-destructive unless explicitly approved, PO-authorized where secrets, external services, or deployed environments are involved, secret-safe, evidence-recorded, scoped to the epic’s actual production risk, clear about what it proves, and clear about what it does not prove. A successful live smoke must not be widened into full vendor conformance, full persistence proof, full public app proof, unrelated PF09 Done posture, or any broader claim not actually exercised.  
* **Validated references, no guesswork — MUST.** Plans MUST NOT assert repo paths, filenames, or module loci without validation. If a locus cannot be validated at plan time, the plan MUST include an explicit discovery step that produces repo evidence and resolves the locus before implementation proceeds.  
* **AI-safe review practices — MUST.** Reviews MUST prioritize correctness, executability, evidence binding, and token validity. Presentation-only formatting variance and heading marker levels are not approval gates (see §12.5).

* **Use standard playbooks — SHOULD.** When a standard playbook exists in the Glow QA Guide, plans SHOULD use it as the default source of steps and evidence. Deviations are allowed only when no playbook applies; deviations SHOULD be documented and proposed as playbook improvements.

### **12.9 Planning path discipline (no fabricated repo paths)**

* **No fabricated paths — MUST.** Any asserted repo path, directory root, or module locus in a plan MUST be validated. Unvalidated path assertions are mechanical blockers in plan review.

* **Allowed validation methods — MUST use one explicit provenance method:**

  * **Canon-cited:** a direct PF canon citation grounding the home or locus (PFxx — Title, §X.Y), with the relevant quoted line(s) included in the plan.  
  * **Codex Audit observed evidence:** an explicitly supplied Codex Audit observation embedded inline in the plan as a short quote or precise observation, labeled as Observed Evidence (Codex Audit), observed repo reality (Codex Audit), CA Observed Evidence, or CA repo-reality observation. This may support planning-time repo-reality facts, existing-locus claims, reuse posture, implementation scoping, and Codex prompt context only.  
  * **CA vetted:** a verbatim quote from the planning Codex audit included inline in the plan. Use this label only when the plan claims formal CA vetted support.  
  * **IG Approved:** a verbatim quote from the Implementation Guide included inline in the plan.

* **Quote discipline for CA vetted and IG Approved — MUST.** If a plan uses the labels CA vetted or IG Approved, the supporting material MUST be quoted verbatim inline in the plan. Paraphrase is not permitted for these labels.  
* **Codex Audit non-overclaim posture — MUST.** Codex Audit observed evidence does not by itself prove acceptance-token satisfaction, QA PASS, OPS completion, PF09 status movement, epic closure, governed evidence freshness after later changes, external vendor truth, open-rails truth, secret validity, canon authority, or a new normative rule. Do not block a plan merely because bounded repo-reality support comes from a supplied Codex Audit rather than PF canon, IG Approved text, or the CA vetted quote label.  
* **If validation is not available — MUST.** The plan MUST mark the locus as unknown and include a discovery step that produces repo evidence to resolve the correct path before implementation assumes it.  
* **Plan portability — MUST.** Plans may reference planning audits inside the plan narrative, but implementation prompts to Codex MUST NOT require audits or attachments. Prompts must be self-contained and embed any Codex Audit observation they rely on as planning context.  
* **PF07-derived, live-source, or PF07-gap posture — MUST.** Any plan, implementation guide, QA plan, review artifact, remediation guide, or epic document that names an infrastructure or ops value must use one of three postures: the exact value is already present in PF07 and is cited or copied directly; the exact value is supplied by live PF10 or another approved source artifact for the current work and is carried forward with a later PF07 drain target; or the exact value is missing and the document classifies the missing fact as discoverable, blocked, unsafe, out of scope, or a valid deferral. Do not downgrade PO-supplied or live-source infrastructure facts to unknown, OPEN, or TBD merely because PF07 has not yet drained them.  
* **No external infra or ops placeholders — MUST NOT.** Do not write plans as if a separate infra or ops team exists outside this workspace and will provide missing values later. Do not leave executable steps dependent on vague external ownership, guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or bare placeholders presented as runnable inputs.  
* **Infra or ops task specificity — MUST.** When an infra or ops task is included, the document must name the concrete target facts that matter for execution and review, such as provider, project, service, repository, base URL or port, database instance or schema, config-key name, governed evidence root or QA root, and the exact value, exact live-source fact, or exact PF07 source for that value.  
* **PF07-gap and discovery posture — MUST.** If PF07 is silent and no approved live source supplies the fact, the document must identify the exact missing PF07 facts and classify the next step explicitly. Safe discoverable facts route to PR discovery, QA discovery, or PO-run OPS discovery. A blocker or deferral is valid only when discovery is unsafe, unauthorized, out of scope, phase drift, dependent on unresolved prior work, dependent on a required PO or Thoth decision, or otherwise cannot proceed without guessing.  
* **No guessed QA bindings — MUST NOT.** QA and Live QA documents must not guess or redefine environment bindings, service bindings, URLs, ports, project names, provider names, or canonical QA-root patterns that PF07 is meant to own.  
* **Review posture — MUST.** A plan or related document that refers to infra or ops work without PF07-backed values, approved live-source values, or an explicit PF07-gap discovery or blocker classification is non-conforming and must be returned for revision.  
* **PF07 scope reminder — MUST.** This rule governs where documents obtain concrete infrastructure facts. It does not move transport policy, token semantics, schema rules, or runbook procedure into PF07  
* **Environment variable discipline (no fabricated env vars) — MUST.** Any environment variable referenced in a plan, runbook, step instruction, or evidence schema MUST be canonical (repo-real or PF-canon named). Treat non-canonical env var names as mechanical blockers, equivalent to fabricated paths.  
  * **Ban `MODO_*` variables — MUST NOT.** `MODO_*` variables are non-canonical and MUST NOT appear in Glow/HDE docs. If present in legacy text, treat them as non-binding placeholders and propose deletion.  
  * **Exact spelling — MUST.** Refer to env vars only by the exact case and spelling defined by repo reality or PF-canon. Do not paraphrase, rename, or recase env vars.  
  * **Invalid env var references — MUST.** If a plan names an env var that does not exist in repo reality or PF-canon, treat it as an invalid reference and require correction (or a discovery step that validates the env var contract) before execution.  
* **Configuration-owned version boundaries — MUST.** When a canonical configuration value or environment variable owns an API version boundary, plans, runbooks, OPS instructions, QA prompts, Codex prompts, evidence generators, and reviews MUST preserve that boundary. Do not hardcode versioned vendor route segments as active runtime route-construction inputs, do not require code changes to test a future configured API version, and do not infer auth behavior from version-path string checks when the owning contract requires explicit route or contract metadata.  
* **Version-path literal classification — MUST.** Literal strings such as `/v1` or `/v2` are not automatically forbidden. Classify each occurrence by role: historical evidence, artifact-family name, non-runtime documentation or provenance, test input proving configurable-version behavior, legacy route-family label, or active runtime route construction. Only active runtime route construction belongs in the defect path; allowed provenance or test literals must not be rewritten into false runtime claims.

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
* **Codex prompts must ignore display-layer escapes — MUST.** Codex-facing prompts must treat escaped display text as non-authoritative unless the escape characters are present inside a raw source file Codex opens.  
* **Do not create escaped repo identities from rendered text — MUST NOT.** Codex prompts must not instruct Codex to create, rename, inspect, or remediate alternate escaped paths, filenames, commands, modules, endpoints, token names, artifact keys, or environment variable names because assistant-rendered text displayed backslashes.  
* **Source-level correction requirement — MUST.** A Codex prompt may direct escape-character correction only when the raw source file contains the unwanted escape character and the plan explicitly identifies the correction as source-real.  
* **Prompt rendering guard — SHOULD.** Review, redline, plan-revision, QA-review, remediation-review, and Codex-audit prompts should state that rendered escape characters in assistant-visible output are not source evidence and must be ignored unless raw or source artifact inspection proves the escaped character is present and materially harmful.  
* **Prompt syntax guard — SHOULD.** Plan-review, QA Plan review, implementation-plan review, remediation-plan review, redline-generation, QA-readiness review, closure-review, and Codex-audit prompts should state that plan commands, snippets, helper code, heredocs, shell lines, and examples do not need to be paste-ready or literal.  
* **Prompt syntax defects are normalization notes — MUST.** Prompt instructions should state that syntax defects, escape characters, markdown rendering artifacts, indentation issues, and command exactness must never block plan approval unless they reveal a separate non-syntax truth, proof, scope, authority, safety, acceptance, phase, or evidence-identity defect.

### **12.11 Acceptance token minting and claim rules (no plan-local tokens)**

* **Token authority — MUST.** Token definitions and the canonical token registry are owned in the Governance & Process Handbook. Plans MUST NOT fork or invent token semantics locally.

* **Claims vs obligations — MUST distinguish.**

  1. A **token claim** asserts a specific acceptance token will be satisfied and is only valid when the token exists in the registry.

  2. An **obligation** is a plain-language requirement used when no suitable token exists yet. Obligations are not acceptance tokens and must not be written in token format.

* **Token-like proof labels are not acceptance tokens — MUST.** A token-shaped or token-like string used as a proof label, evidence label, row label, or implementation label is not an acceptance token unless it is registered in HDE-Governance or minted by a live higher-numbered PF10 addendum.  
* **Proof-label evidence may proceed without token claim — MUST.** Plans, PR summaries, OPS evidence, QA logs, acceptance maps, token-evidence matrices, and closeout artifacts may describe governed proof obligations using plain-language labels, but they must not claim those labels as satisfied acceptance tokens unless the exact token names are admitted.  
* **Unregistered-token acceptance overclaim is a blocker — MUST.** If a planning or review artifact claims an unregistered proof label as an acceptance token, classify the issue as an acceptance-token truth defect, not as formatting or inventory polish.  
* **Token admission remains Governance-owned — MUST.** If a proof label must become a gated acceptance predicate, the token name and semantics must be admitted through HDE-Governance or a live PF10 minting addendum before any acceptance artifact claims it.  
* **No plan-local minting — MUST.** Plans MUST NOT mint new tokens locally. A plan may claim a token only if the token exists in the Governance & Process Handbook token registry or has been minted in HDE Build Notes.

* **Token spellings — MUST be exact.** Token claims MUST use exact token spellings; no aliases or local variants.

* **Evidence before claim — MUST.** Every token claim in a plan MUST name the evidence output(s) that will be produced for that token (exact paths and filenames where possible).

* **Tokenless QA evidence must not imply token satisfaction — MUST.** If a Live QA check records no claimed tokens, the review must not infer an acceptance-token claim from PASS status, evidence presence, or adjacent close-stage posture.  
* **Close-stage artifacts are not runtime behavior proof — MUST.** Missing acceptance maps, token matrices, close-pack records, or other close-stage artifacts must not be classified as runtime behavior failure for a tokenless Live QA check unless the plan required that artifact as a current check deliverable.  
* **Evidence-bound claim scope — SHOULD.** When a check explicitly limits claims to evidence scope, preserve that limitation in review language and do not widen the result into acceptance completion or formal closeout completion.  
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

  ### **12.13 Comprehensive PR review posture (multi-attempt, PF09 status posture, and later-drain statements)**

* **Multi-attempt review posture — SHOULD.** When a PR review depends on the cumulative result of an original PR plus one or more remediations, preserve the attempt chain explicitly and evaluate the final decision against cumulative branch truth rather than treating each attempt as a disconnected artifact.  
* **Lifecycle-grounded review summary — SHOULD.** A comprehensive PR review summary may describe how earlier attempt defects were corrected in later attempts, but it should separate attempt-specific defects from final-branch truth.  
* **Finding-source labeling — SHOULD.** In a comprehensive PR review, each finding should identify the source attempt or bundle when that source matters to the conclusion.  
* **Crosswalk-by-attempt — SHOULD.** When requirement satisfaction changes across attempts, the Requirement Satisfaction Crosswalk should record each attempt in chronological order with its status and evidence pointers instead of compressing the story into only original versus final state.  
* **Negative-claim proof — SHOULD.** If a review asserts that a prior drift item, diff, or scope leak is absent in a later attempt, record the search method and zero-hit result.  
* **Negative audit proof is valid proof — MUST.** If the approved check is intended to prove absence, zero hits, no drift, no widening, or no forbidden content, a clean negative result is evidence for that claim.  
* **Do not demand rerun solely because proof is negative — MUST NOT.** Do not classify an intended negative audit result as missing evidence or require a rerun only because the proof found nothing. Block only when the source, scope, pattern, command identity, or captured result is missing, wrong, or insufficient.  
* **Negative proof must remain reviewable — MUST.** Record the searched source, exact pattern or command, scope, and zero-hit or absence result so the negative claim can be audited.  
* **Exact phased PF09 mapped unit controls — MUST.** If the reviewed work maps to an exact phased PF09 task or subtask, that exact mapped unit controls acceptability language and later-drain posture. Parent-summary language is not enough when an exact subtask exists.  
* **Multiple mapped phased PF09 units — MUST.** If one slice claims to close more than one phased PF09 task or subtask, each claimed mapped unit must be complete in substance and supportable for later drain before acceptable-status language is allowed.  
* **Current phased PF09 recorded status is not a pre-drain gate — MUST NOT.** Do not treat the status text currently recorded in phased PF09 as the closure gate, QA-entry gate, PR acceptability gate, or OPS acceptability gate.  
* **Live-truth acceptability posture — MUST.** Before drain, judge acceptability from approved implementation state, approved OPS state where applicable, governed evidence, truthful review and approval artifacts, and the live in-flight PF10 record where PF10 speaks.  
* **Approved-task scope controls review unit — MUST.** Review only the approved task in question and its explicitly approved scope. Do not widen the review to later PRs, later OPS tasks, later validation runs, or whole-epic closure work unless the approved task explicitly includes them.  
* **Stricter alias hardening is not permissive drift — SHOULD.** If a PR maps an ambiguous or newly handled runtime alias to an existing stricter guarded posture, and the evidence proves that the change blocks or narrows behavior rather than widening it, classify the change as hardening rather than permissive scope drift.  
* **Alias hardening review proof — MUST.** The review must state the prior ambiguity, the stricter governed posture now applied, the guard condition, the regression or evidence that proves the stricter posture, and the owning PF home for any later durable alias wording.  
* **Do not create policy by review prose — MUST NOT.** A review may describe that the PR follows an existing stricter policy, but it must not define new runtime policy, transport policy, or infrastructure aliases as PF03 truth. Route durable environment or infrastructure alias language to the owning PF home.  
* **Non-closure steps are reviewed on their own approved job — MUST.** If the approved task is a bounded intermediate step, such as validation, gap classification, sequencing correction, evidence capture, or another explicitly non-closure step, judge the task on whether it truthfully and correctly completes that approved job.  
* **PF09 closure is not a gate for non-closure steps — MUST NOT.** If the approved task does not claim to bring a mapped phased PF09 task or subtask to closure, do not block, fail, or reject it solely because the mapped row remains open for later approved work.  
* **Closure gate applies only to closure-claiming tasks — MUST.** A phased PF09 closure gate applies only when the approved task explicitly claims that it brings a mapped task or subtask to Done, supports a Done recommendation now, or performs final closure, final binding, final acceptance promotion, or equivalent closure-claiming work.  
* **Review language must keep task acceptance distinct from row closure — MUST.** Distinguish task-level acceptance of the approved step from phased PF09 closure status of the mapped row.  
* **Same rule for OPS tasks — MUST.** A bounded OPS task may be accepted for truthful execution of its own approved purpose even when the mapped phased PF09 row remains open for later work.  
* **Carry-forward OPS evidence retains its evidence class — MUST.** If a PR indexes, binds, refreshes, or references prior OPS evidence, the PR review must preserve that evidence as OPS evidence unless the current PR, QA step, or closeout evidence proves a different evidence class.  
* **OPS evidence indexing does not create QA PASS — MUST NOT.** Do not write indexed OPS evidence as QA evidence, Live QA completion, acceptance-token satisfaction, PF09 status movement, epic closure, or permanent canon drain merely because the PR binds it into governed evidence surfaces.  
* **Carry-forward OPS support must name the current claim boundary — MUST.** When OPS evidence contributes to a PR’s evidence coherence, state the exact claim it supports and the claims it does not make.  
* **Standalone status movement still requires its own proof — MUST.** Carry-forward OPS evidence may support later status movement only when the later PR, QA, closeout, or drain artifact explicitly proves that status action.  
* **Combined-evidence supportability decisions — SHOULD.** If multiple approved PR, OPS, QA, or closeout slices each preserve accurate non-claim posture, a later review or PF10 addendum may still record a combined-evidence supportability decision when the combined governed evidence satisfies the mapped row’s substantive proof burden.  
* **Slice-local non-move language stays local — MUST.** Earlier no status move, no PF09 move, no QA PASS, no epic closure, or no acceptance-token satisfaction language must be read at the scope of the individual slice unless the source explicitly makes it a permanent prohibition.  
* **Combined supportability must preserve non-claims — MUST.** A combined-evidence supportability decision must state what it supports, what it does not claim, and which evidence classes remain distinct, including OPS evidence versus QA evidence, PR evidence versus OPS evidence, supportable status versus drained status, and proof labels versus registered acceptance tokens.  
* **QA-readiness supportability is not automatic closure — MUST.** If the decision supports QA readiness, it must not imply QA has already passed, epic closure, PF09 drainage, permanent canon update, live vendor proof, or additional proof-label token admission unless the source evidence proves that exact claim.  
* **No extra work required must be grounded — SHOULD.** If a combined supportability decision states that no additional implementation, OPS, evidence capture, or canon action is required before QA, tie that statement to the combined approved state and governed evidence.  
* **Allowed pre-close language — MUST.** If the mapped work is not yet complete in substance, use contributory, intermediate, review-clean, bounded, or supportable from repo evidence. Do not use acceptable, accepted, satisfied, complete-for-close, or supportable for later drain to Done until the mapped work is complete in substance and the live truth supports later drain.  
* **Current phased PF09 recorded status may be cited only as the current drained record — MUST.** It is evidence of canon-as-recorded, not proof that the work is still incomplete in substance.  
* **Real blockers remain real blockers — MUST.** Incomplete implementation work, incomplete OPS work, incomplete evidence, and execution ambiguity still block closure. Describe those as real blockers, not as PF09-text blockers.  
* **Later-drain PF-canon update statement — MUST.** Any PR final review, PR remediation acceptance review, OPS final review, final close-pack review, or other approval artifact intended to support later PF-canon drain must state the affected PF canon home or homes, the exact affected locator or locators, the current canon posture if established, the supported later-drain action, the drain readiness classification, the evidence basis, and the epic-close expectation.  
* **Canon basis vocabulary for PR analysis — MUST.** PR analysis records and remediation reviews that include CHG items MUST classify each CHG as exactly one of `CANON ALIGNED`, `CANON SILENCE`, or `CANON MISMATCH`.  
* **CANON ALIGNED use — MUST.** Use `CANON ALIGNED` when the reviewed behavior or output is already supported by the owning PF home and no PF-canon delta is proposed for that CHG.  
* **CANON ALIGNED is not a drain target — MUST NOT.** Do not convert a `CANON ALIGNED` CHG into a doc-delta proposal or later-drain action. It may support review traceability, but it does not by itself require a PF-canon edit.  
* **CANON SILENCE use — MUST.** Use `CANON SILENCE` only when the owning PF home has no current rule or row covering the reviewed behavior after retrieval.  
* **CANON MISMATCH use — MUST.** Use `CANON MISMATCH` when current PF text exists but the reviewed evidence proves that the text is stale, incomplete, contradicted, or ready for a status or action change.  
* **Mismatch proof — MUST.** For `CANON MISMATCH`, include the current PF excerpt, the behavior evidence, and the target doc, section, or closest stable home.  
* **CHG linkage — SHOULD.** When CHG items support a phased PF09 status action, link each CHG to the impacted task or subtask IDs, findings, and evidence pointers that make the later-drain recommendation reviewable.  
* **Supported later-drain action vocabulary — MUST.** Use exactly one supported later-drain action in the approval artifact: change to Done, change to Partial, change to Not done, change to Consolidation pending, change to Optional, or No status change recommended.  
* **Drain readiness classification vocabulary — MUST.** Use exactly one drain readiness classification in the approval artifact: Supportable from repo evidence, Not yet supportable from repo evidence, or Already drained into PF-canon.  
* **Later-drain wording must be explicit — MUST NOT.** Do not stop at accepted, complete, merge-ready, approved, or no further remediation needed when the practical intent is to support later PF-canon drain.  
* **This does not move canon drain earlier — MUST NOT.** The required later-drain statement records intent at approval time; it does not authorize early PF edits during implementation or OPS work.  
* **Supported later-drain status must be distinct from current recorded status — MUST.** Reviews and closeout artifacts must distinguish current phased PF09 recorded status, supported later-drain status, actual implemented state, actual OPS state, and actual governed evidence state.  
* **Reused-history and active-scope rows must be separated — MUST.** If a review, QA report, closeout report, or later-drain statement contains both reused historical rows and active rows, it must list or otherwise distinguish the reused-history rows from the active-scope rows.  
* **No new-implementation claim for reused history — MUST NOT.** Do not write reused-history rows as newly implemented work, newly evidenced work, or current-epic closure work unless the source evidence actually proves new implementation or new evidence for those rows.  
* **Reused-history evidence posture — SHOULD.** When reused-history rows are material to the verdict, state whether they are reused as prior foundation, historical closure, prerequisite context, or another explicit non-new-implementation role.  
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
* **False-positive generator fixes require negative-control proof — SHOULD.** If PR artifacts or RCA show that an evidence generator could emit PASS while a decisive predicate failed, the review should cite a regression or negative-control test that forces that failed predicate and observes FAIL, or state why that proof is unavailable.  
* **Top-level PASS derivation must be explicit — MUST.** When accepting remediation for a false-positive generator defect, state that the top-level PASS now derives from the decisive predicate set, not from previous-run drift, stale artifact bytes, partial local state, or an unbound helper result.  
* **Stale artifact risk must be closed before approval — MUST.** If generator logic changed after governed artifacts were produced, approval language is allowed only after the final governed artifacts and their proof companions are regenerated or otherwise proven to reflect the final generator logic.  
* **Generated proof-family PASS requires complete fail-closed coverage — MUST.** If a review claim depends on multiple generated proof families, PASS language is allowed only when every generated proof family used by the epic, step, PR, or remediation bundle has explicit fail-closed proof or is explicitly ruled not applicable.  
* **Partial generated-proof coverage is tooling-blocked — MUST.** If any generated proof family in scope lacks explicit fail-closed proof, classify the review as tooling-blocked or blocked under the governing plan. Do not mark the step PASS on adjacent proof families alone.  
* **Fail-closed visibility artifact — SHOULD.** When final PASS depends on closing a generated-proof-family gap, the review should cite the artifact or test output that lists each family as proven, not proven, or not applicable.  
* **Evidence-generator PASS claims must be predicate-bound — MUST.** A generator PASS claim is reviewable only when the decisive predicates for the claimed evidence family are evaluated directly. Format-only checks, regex-only hash shape checks, or parsed-object equality are insufficient when byte identity, recomputed identity, index parity, or proof-companion coherence is the actual claim.  
* **Generated observed-state proof must be source-observed — MUST.** When generated evidence claims environment posture, provider order, selection attempts, typed error class, typed error code, public-output posture, secret posture, probe posture, or comparable runtime state, the review must verify that those values came from observed runtime or governed source facts rather than hardcoded constants, assumed defaults, or synthetic placeholder outputs.  
* **Synthetic unexpected outputs are not proof — MUST NOT.** A generator must not serialize unexpected success, unexpected failure, wrong environment, wrong order, or unknown state as valid proof when the approved claim requires fail-closed behavior.  
* **Hardcoded attempt or selection order is not acceptable proof — MUST.** If the proof claim depends on observed attempt order or selection order, approval language is allowed only when the review cites evidence that the order was derived from the actual runtime attempt sequence or another governed observed source.  
* **Typed-failure proof must fail closed — MUST.** If the approved claim requires a typed failure, the generator or checker must fail closed when the observed class, code, environment, order, probe posture, public-output posture, or secret posture does not match the expected predicate set.  
* **Corrected generator proof must show both behavior and regression coverage — SHOULD.** When remediation corrects wrong posture, synthetic output, or hardcoded observed-state evidence, cite the regenerated governed artifact and the focused regression or check that prevents the same false proof from returning.  
* **Evidence-checker PASS claims must be predicate-bound — MUST.** A checker PASS claim is reviewable only when the checker rejects the decisive failure states for the claimed evidence family.  
* **False-PASS checker fixes require rejection proof — MUST.** If a checker could present missing, skipped, unavailable, errored, stale, partial, or non-comparable rows as PASS, the remediation review must cite final proof that those states are rejected or explicitly classified as unavailable rather than passed.  
* **Truth-preserving skip posture must be separate from PASS — MUST.** If a skipped or unavailable condition is truthful and allowed, the review must state that it is a truth-preserving unavailable or skipped posture, not provider parity PASS, behavior PASS, or acceptance completion.  
* **Checker regression proof — SHOULD.** Reviews should cite the unit test, fixture, or governed check that forces the false-PASS condition and proves the corrected checker fails or classifies it correctly.  
* **Generator logic changes require final governed artifact regeneration — MUST.** When generator logic changes, the final governed artifacts, path proofs, index or mirror rows, and checksum companions that depend on that generator must be regenerated or otherwise proven current under the final logic before approval language is allowed.  
* **Generator execution proof is distinct from index proof — MUST.** When approval depends on generated evidence, an index, mirror, hash, path-proof, or schema check of committed bytes does not by itself prove that the generator was run under the final logic.  
* **Generated evidence freshness requires generator run or check proof — MUST.** If stale generated evidence is a risk, the review must cite the final generator command, generator check, pipeline step, or test that proves the generator executed before the downstream updater, index, mirror, hash, or path validation step.  
* **Pipeline ordering remediation must be explicit — MUST.** If RCA states that stale generated evidence could survive because the generator was not part of the governed pipeline, the review must state the final ordering and the evidence proving generator execution precedes index or mirror validation.  
* **Updater PASS cannot mask stale generator state — MUST NOT.** Do not approve a generated-evidence claim from updater or index checks alone when the material defect was missing generator execution, missing generator check mode, or stale generated bytes.  
* **Governed token-overclaim remediation must start at the source row — MUST.** If governed evidence overclaims an unsupported acceptance token, a remediation review must prove that the unsupported token claim was removed from the source row or source generator, not only from a rendered report.  
* **Dependent governed evidence must be regenerated or proven current — MUST.** After a token-overclaim source correction, approval language is allowed only when the dependent Human Evidence Index, Machine Mirror, hash sentinels, path proofs, and generated evidence surfaces are regenerated or otherwise proven to reflect the corrected token posture.  
* **Removed-token search proof — SHOULD.** Reviews should cite a search or equivalent proof that the removed unsupported token no longer appears in the source row and generated evidence surfaces that previously carried the overclaim.  
* **Unsupported-token remediation remains acceptance-posture remediation — MUST.** Do not classify the corrected PR as behavior failure when the implementation behavior is sound and the defect is an evidence-token overclaim. Preserve the distinction between implementation behavior, acceptance posture, and governed evidence truth.  
* **Final approval must cover prior blocker checks — MUST.** If an earlier attempt failed or omitted a named test, evidence check, or proof check that caused a blocker, the final approval must cite a final passing rerun of that same check or state why it is no longer applicable.  
* **Bounded evidence refresh side effects are not automatic scope drift — SHOULD.** If a review observes companion path-proof, checksum, mirror, or orientation refreshes outside the direct slice, classify them as bounded evidence-side churn when they remain in existing governed families, are validated by the evidence checks, and do not introduce new runtime, route, payload, or artifact-family scope.  
* **Side-effect classification must include mirror rows — MUST.** When an evidence updater or generator refreshes governed proof companions outside the direct target family, the run evidence must name both the refreshed proof-companion paths and the corresponding Machine Mirror artifact keys and discovered paths.  
* **Side-effect PASS must fail closed — MUST.** A classified outside-family refresh may support PASS only when each classified path exists, each proof companion validates against its target, and each classified Machine Mirror row matches artifact key, proof anchor, sha256, and size.  
* **Check mode remains strict for self-generated evidence — MUST.** Write-time self-hash recursion handling must not weaken final check mode. Final check mode must validate the final Machine Mirror sha256 and size bindings for every self-generated row claimed by the PR or remediation.  
* **Side-effect classification vocabulary — SHOULD.** Classify outside-family governed evidence churn as expected updater convergence, required dependency refresh, or unexpected drift.  
* **Governed evidence path collisions are blockers until repaired — MUST.** If a PR writes slice-specific evidence into a shared governed evidence path, overwrites another evidence family, or makes the same governed path appear to carry two different proof families, the review must classify that as an evidence-path collision.  
* **Collision remediation must preserve both families — MUST.** A collision is repaired only when the shared evidence path is restored to its proper family posture and the slice-specific evidence is moved, indexed, or regenerated at its own governed path.  
* **Final path ownership must be reviewable — MUST.** After collision remediation, the review must state which final paths carry the shared family, which final paths carry the slice-specific family, and which evidence index or mirror rows prove the final binding.  
* **Do not accept path-only repair claims — MUST NOT.** Do not approve a collision repair solely because changed paths exist. The review must verify that the shared path was not silently repurposed and that the moved evidence remains governed, path-proven, and tied to the intended PR or QA slice.  
* **Governed artifact-key collisions are blockers until repaired — MUST.** If two evidence rows or registrations can bind the same physical artifact path under different artifact keys, or if a slice-specific key can override a canonical key by discovered path, classify the issue as a governed artifact-key collision.  
* **Canonical key must control when one exists — MUST.** When a canonical artifact key exists, final review language must prove that the physical path maps to that canonical key and that any superseded slice-specific key is removed, filtered, or otherwise unable to override the canonical key.  
* **Key-collision remediation must update the source registration — MUST.** A key-collision repair is not complete if only rendered reports or downstream indexes change. The review must prove that the source registration, updater, generator, or normalization logic that created the collision is corrected.  
* **Dependent evidence must be regenerated or proven current — MUST.** After artifact-key collision repair, approval language is allowed only when the Human Evidence Index, Machine Mirror, hash sentinels, path proofs, and relevant tests or checks reflect the corrected final key binding.  
* **Key-collision proof — SHOULD.** Cite the canonical key, the superseded key, the final physical path, the source-row or updater correction, the generated index or mirror row, and the final passing check that proves the collision is closed.

### **12.14 Implementation reports and lead retrospectives (source posture, evidence gaps, and closure questions)**

* **Primary-source posture — MUST.** Use the designated live source of truth as the default narrative basis for an implementation report or lead retrospective.  
* **Narrow gap-filling fallback — MAY.** If that primary source does not restate the original business case or the single consolidated PR and OPS sequence, the report may use an approved epic plan or approved implementation plan for those exact gaps only. The report must say that this limited fallback is being used and why.  
* **Retrospective source-role split — MUST.** Implementation reports and lead retrospectives must state the primary live source, the role of PF-Canon where the primary source is silent, and the narrow role of any plan or guide used only for intended-scope framing.  
* **Retrospective epic identity must be source-supported — MUST.** If an implementation report or lead retrospective names an epic, pass, phase, or short label, the identity must be supported by the primary live source or by the reviewed source set.  
* **Retrospective name mismatch must be stated — MUST.** If a prompt, operator label, artifact label, or earlier report names the epic differently from the controlling source set, state the mismatch, cite the controlling source, and use the source-supported identity in the retrospective.  
* **Do not silently normalize retrospective identity — MUST NOT.** Do not silently replace an unsupported epic name, pass number, phase name, or short label. Preserve the mismatch as a traceability note when it affects review identity.  
* **PF23 in retrospectives is context, not proof — MUST.** If PF23 is used in an implementation report or lead retrospective, label it as current-reality context only. Do not write PF23 as closure proof, acceptance authority, a gate, or a blocker by itself.  
* **PF20 retrospective posture — SHOULD.** If PF20 was not used, say so directly when the source set is being named. If PF20 is used, label it historical-only and do not use it as current planning, QA, acceptance, or closure authority.  
* **Framing-only inputs must stay framing-only — MUST.** If an Implementation Guide, QA Plan, or similar input is used only for intended goals, scope framing, or expected requirement framing, preserve that limitation and do not treat the input as proof that execution occurred.  
* **Implementation-report grounding — SHOULD.** When present, the implementation report should preserve a single consolidated PR and OPS sequence, the major surfaces affected, and the evidence inventory.  
* **Per-claim source-gap annotations — SHOULD.** When an implementation report, epic closure review, or lead retrospective relies on an in-session plan, PR artifact, docs PR artifact, or other non-primary source for a detail that PF10 or PF-Canon does not fully restate, add a short source-gap note beside that claim. The note should state what the primary PF source confirms and what remains available only in the reviewed artifact.  
* **Do not promote artifact-only facts to canon — MUST.** If a detail is available only in a reviewed non-PF artifact, do not write it as if it is already PF10 or permanent PF-Canon truth. Keep it as evidence-grounded report content with a source-gap note or evidence pointer.  
* **Implementation-slice evidence is not close-pack evidence — MUST.** When repo docs, implementation reports, or retrospectives describe PR-slice evidence families, label them as implementation evidence, PR-slice evidence, or implementation closure evidence unless close-pack artifacts are actually proven. Do not describe implementation evidence as close-pack output.  
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
* Controlled external smoke tasks require an operator-ready completion contract — MUST. An OPS task or remediation guide that allows controlled external or vendor-backed smoke MUST state the command-discovery prerequisite, safe secret posture, target posture, target fact requirements, input-shape constraints, explicit source posture, required prior PR or remediation binding, evidence-output contract, and stop condition before execution.  
* Allowed and forbidden inputs must be explicit — MUST. If the task depends on a no-user, birth-only, source-specific, or otherwise constrained command shape, the contract MUST name the allowed caller or command inputs and the forbidden caller or command inputs. User identity, app identity, DB-backed identity, source mode, endpoint, flag, and inline-secret constraints must be stated as machine-sensitive content.  
* Target model must be named — MUST. The contract MUST state whether the smoke target is a local CLI command, hosted HTTP service, vendor API, database-backed path, or other target model. Do not borrow infrastructure facts from another target model. If the target model changes, require a new target fact set before execution.  
* Preflight matrix is required for external smoke — MUST. The contract MUST include a preflight matrix or equivalent checklist that maps each prerequisite to required proof and a status rule. Missing command proof, unresolved placeholders, missing required inputs, missing credential presence, missing safe rails, missing PO authorization, or contradicted prerequisite proof must classify as `TOOLING_BLOCKED` unless the governing plan defines a narrower tooling-block label.  
* Execution wrapper must be fixed before execution — MUST. The contract MUST define the execution wrapper or execution capture method before the PO runs the smoke. The wrapper must capture stdout, stderr, exit code, and deterministic capture posture where applicable.  
* No guessed external facts — MUST NOT. Do not modify a command, host, port, URL, service binding, target, environment fact, credential posture, source posture, flag, or input value by guesswork to force a PASS. If the fact is not proven, classify the step as blocked under the governing plan.  
* PO-only external execution — MUST. Any controlled external or vendor-backed smoke that requires privileged external access, credentials, open rails, or vendor calls MUST be PO-only and IA-guided. Automated agents MUST NOT run the external call, claim completion, or simulate the external state change.  
* Required evidence outputs must be named — MUST. The contract MUST name the evidence root, required files, required content for each file, checksum or integrity ledger if required, and the file that records the final outcome classification.  
* Classification for blocked versus failed external proof — MUST. If the exact command, credentials, target facts, safe execution posture, required inputs, or PO authorization are missing, classify the result as `TOOLING_BLOCKED` or the plan-defined tooling block, not as `FAIL_BEHAVIOR`. If all prerequisites are proven and runtime output contradicts the expected behavior, classify it as `FAIL_BEHAVIOR`.  
* PASS is implementation-validation only unless the source proves more — MUST. A successful controlled external smoke may support implementation-validation evidence, but it MUST NOT be written as QA PASS, Live QA completion, acceptance completion, PF09 status change, epic closure, public contract change, or PF-canon drain completion unless the governing source and evidence prove that exact claim.  
* Secret persistence failure — MUST. If secret-bearing output is written to logs, summaries, command captures, stdout, stderr, JSON, checksum ledgers, or other persisted evidence, classify the run as `FAIL_TOOLING` and do not treat it as valid acceptance evidence.  
* Secret-bearing artifacts must be quarantined — MUST. If secret-bearing output is persisted, the review or result summary MUST name the affected artifact, mark it excluded from proof, and state that the affected artifact cannot support acceptance.

OPS final review structure — SHOULD. If an OPS task later receives a final review, that review should use three top-level sections: Review Summary, Findings, and Evidence Print.

OPS final review findings — SHOULD. Each finding should state what was observed, why it matters, the expected requirement from the governing plan or canon source, and whether the issue is a blocker for acceptance.

OPS final review Evidence Print — SHOULD. When applicable, structure the evidence print in three distinct parts:

* Required deliverables satisfied.  
* Commands or actions evidence.  
* Configuration or infrastructure state evidence.  
* Decisive OPS content must be exposed — SHOULD. When an OPS final review relies on a consolidated report, the Evidence Print should expose the decisive content that supports the verdict, including the command or action, target disposition, prerequisite binding, request or input summary, result summary, runtime outputs, execution classification, and checksum or integrity ledger when applicable.  
* Task-labeled OPS evidence mapping — SHOULD. When an OPS final review relies on task-labeled command blocks, the Evidence Print should map each command label to its stdout, stderr, exit-code evidence, produced artifact, and final validation signal.  
* Command transcript labels must match result labels — MUST. If acceptance depends on a replayable command transcript, the command transcript labels, stdout labels, stderr labels, exit-code labels, and final validation labels must align. Unlabeled, mismatched, or narrative-only command evidence remains a blocker until repaired.  
* Inventory provenance must match output structure — MUST. If a final inventory, checksum ledger, or manifest binding is part of the verdict, the review must state the inventory structure, named binding map, checksum-row posture, and path-proof posture. Do not accept an inventory whose displayed structure conflicts with the command or provenance claimed for it.  
* Superseded evidence reports must be named — SHOULD. If a later evidence report replaces earlier flawed evidence reports, state which earlier reports are superseded and which corrected report controls.  
* Evidence-packaging-only non-claim posture — MUST. A packaging-only OPS task must not imply QA reruns, vendor calls, implementation changes, PF-canon edits, PF09 drain, or new acceptance claims unless the source evidence proves those separately.  
* **OPS safety and reversibility posture — SHOULD.** When an OPS review accepts an evidence-capture, validation-only, classification-only, or other bounded OPS task, state whether the reviewed evidence shows irreversible infrastructure changes, unsafe operations, external side effects, secret exposure, QA reruns, vendor calls, or implementation changes.  
* **No-irreversible-change claims require source evidence — MUST.** A review may claim that no irreversible infrastructure change or unsafe operation is evidenced only when the OPS evidence or governing source record supports that posture.  
* **Evidence-capture classification stays bounded — MUST.** If the task is evidence capture only and secret-safe outputs are proven, classify it on its own bounded evidence-capture purpose. Do not widen that classification into system safety, infrastructure safety, permanent operating policy, or closure proof unless the source evidence proves that exact claim.  
* Path-only OPS claims are insufficient when content carries the verdict — MUST. If the OPS verdict depends on facts inside the evidence files, the review must quote or summarize those decisive facts. A list of paths alone is not enough to support PASS, FAIL, TOOLING\_BLOCKED, non-claim posture, or later-drain support language.  
* **Optional PF09.x later-drain support block for OPS reviews — SHOULD.** If the approved OPS task is tied to a phased PF09 task, subtask, completion claim, close claim, or later-drain posture, the OPS final review should include a distinct PF09.x later-drain support block after the OPS Evidence Print.  
* **No PF09.x support proven is an allowed OPS outcome — MUST.** If an OPS task is acceptable as OPS evidence but does not itself prove a phased PF09 status move, state the supported later-drain action as no PF09.x support proven or No status change recommended, as appropriate to the artifact’s vocabulary.  
* **OPS close-candidate language is bounded — MUST.** An OPS close-candidate or acceptance-candidate label means only that the OPS task appears acceptable for its approved purpose. It does not imply QA PASS, PF09 status movement, epic closure, acceptance-token satisfaction, or permanent PF-canon drain unless the source evidence proves that exact claim.  
* **OPS evidence may support later work without moving status now — SHOULD.** When OPS evidence is suitable support for a later PR, QA step, closeout, or canon drain, state that later dependency explicitly and keep it separate from the current OPS verdict.

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

Proof classes must be labeled — MUST. Remediation guides, QA plans, PR reviews, OPS reviews, and closeout reviews MUST label materially different proof classes separately when a claim depends on more than one kind of proof, such as public output proof, internal compute proof, local test proof, grep proof, controlled external smoke proof, vendor-backed proof, or closure evidence.

Do not substitute local proof for live-behavior proof — MUST NOT. Local pytest, grep, fixture-only, canonicalization, serializer, math, or internal-compute proof may support only the claim it actually exercises. It MUST NOT be written as a substitute for vendor-backed, live, external, or runtime behavior proof when that is the claim under review.

Proof outputs cannot overclaim — MUST. Evidence outputs that support remediation verification MUST NOT be described as QA PASS, Live QA completion, acceptance completion, epic closure, or production behavior proof unless the source evidence directly proves that exact class of claim.

Final evidence class must match the claim — MUST. If a remediation claim requires a specific proof class, the review must state whether that class is present, missing, blocked, or not applicable. Do not blur missing proof into a passing adjacent proof class.

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
* Connector-only repo access limits — MUST. If review uses GitHub connector access, PR artifacts, or other read-only non-executable repo access rather than an executable local checkout, state that validation posture explicitly. Do not claim local command reruns, mutable working-tree cleanliness, file edits, regenerated artifacts, package installs, service starts, or QA execution unless the reviewed source proves that exact action. Report PR-body test results as reported results unless an independent execution log, workflow status, or governed artifact proves the run.  
* Tooling portability defects require explicit RCA — MUST. If PR artifacts show a tool or evidence generator failed under normal repo-root invocation and later passed only after import-path or environment bootstrapping was repaired, the review must classify that as a tooling portability defect, not as application behavior failure.  
* Final invocation proof for repaired tools — MUST. The RCA or Evidence Print must quote the final passing direct invocation and state whether success depends on caller-supplied environment manipulation. If the final proof still requires an unplanned ambient dependency, record it as a remaining portability caveat or blocker according to the approved plan.

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

Read-only or no-diff PR exception — MUST. If the approved PR scope is read-only discovery, boundary inspection, source-skew analysis, or other no-change review work, and the PR artifacts prove that no diff hunks exist, the review MUST keep the Diff Review section but MUST NOT invent DR items.

No-diff proof requirement — MUST. The review MUST state the exact search method or artifact evidence proving no diff hunks, changed files, created files, or deleted files exist.

Duplicate diff-hunk grouping — SHOULD. If PR artifacts contain duplicated occurrences of the same file hunk or repeated evidence-refresh hunk, the Diff Review may group those occurrences under one DR item when the same file or hunk locators, risk assessment, and plan linkage apply.

Behavior-bearing changes must remain separated — MUST. Do not hide behavior-bearing changes, source-of-truth changes, token changes, evidence-family changes, or acceptance-relevant changes inside a grouped churn item.

Grouped churn still needs a scope statement — SHOULD. When broad path-proof, checksum, mirror, or evidence-refresh churn is grouped, state why it is bounded and whether it changes product behavior, evidence class, token posture, or PF09 status posture.

Discovery proof surface — MUST. For approved read-only PRs, acceptance proof may come from command ledgers, source-inspection excerpts, discovery findings, and zero-hit searches. Tests or CI proof are required only when the approved plan requires them.

Status posture for read-only discovery — MUST. A read-only discovery PR MUST use `No status change recommended` unless it produces governed evidence that truthfully supports a status change. It MUST NOT imply QA PASS, Live QA completion, PF09 status change, epic closure, implementation completion, or OPS completion by discovery alone.

Follow-up recommendations stay non-execution — SHOULD. A read-only discovery PR may name safe follow-up loci, risks to avoid, and later checks to run, but the review must label them as future implementation or QA guidance rather than as work completed by the read-only PR.

DR-001

* Change summary: \<what changed, stated mechanically\>

* Risk assessment: \<Low | Medium | High\>

* Why it matters: \<impact on contract, evidence, or safety\>

* Evidence pointer: \<PATH or PR-ARTIFACT-HEADING\>

* Plan linkage: \<PLAN\_SECTION\_OR\_REQUIREMENT\_ID\>

RCA (required only if RCA trigger is active; trigger \= fix/remediation language in PR artifacts, or evidenced failure/bug/CI failure)

Multiple-failure RCA posture — MUST. When PR artifacts report more than one validation bug, remediation loop, or CI failure, the RCA must preserve the distinct failure classes instead of collapsing them into one generic failure.

Numbered root causes — SHOULD. When the source reports multiple root causes, number the root cause statements and keep each tied to its own evidence pointer.

Fix summary across root causes — SHOULD. The fix section should state the concrete remediation actions that close each material root-cause class.

Fix verification must map to the reported failures — MUST. Verification must cite final passing proof for each material failure class or state why a reported failure class no longer applies.

Residual risk must be sourced — MUST. If the RCA says no residual risk remains, cite the source line or evidence basis that supports that statement. If residual risk remains, describe it separately from the final PASS or approval posture.

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

Canon-basis template guard — MUST. Each CHG item must set Canon basis to exactly one of `CANON ALIGNED`, `CANON SILENCE`, or `CANON MISMATCH`.

`CANON ALIGNED` template posture — MUST. Use `CANON ALIGNED` when the CHG records behavior or output already supported by the owning PF home and no PF-canon delta is proposed.

`CANON SILENCE` template posture — MUST. Use `CANON SILENCE` when no current PF rule or row covers the reviewed behavior after retrieval.

`CANON MISMATCH` template posture — MUST. Use `CANON MISMATCH` when current PF text exists but reviewed evidence proves the text is stale, incomplete, contradicted, or ready for a status or action change.

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

* If no repo-local markdown or link-check command is discovered, record the exact search method and state that no repo-local command was found.  
* When no repo-local docs lint or link-check exists, record the fallback validation actually performed, such as final-newline checks, representative path-existence checks, or evidence-navigation checks.  
* Do not claim docs lint or link-check coverage unless a committed repo-local command or captured run proves it.  
* **Repo-proof notes for docs-only claims — MUST.** When a docs-only PR mentions a command, flag, workflow, file path, module path, service name, endpoint, config key, environment variable, artifact path, token name, validation claim, or artifact home, the PR artifacts must record how that claim was verified.  
* **Allowed proof sources for docs-only claims — MUST.** Verification may come from repo proof, PF10 or PF-canon contract text, captured command output, test output, path-existence proof, or an explicit search result. Do not infer the claim from implementation intent alone.  
* **Docs-only scope validation — MUST.** When a PR claims docs-only scope, the PR artifacts must include a changed-files scope check that confirms whether code, tests, schemas, generated evidence, governed evidence indexes, PF-canon documents, or other non-doc surfaces changed.  
* **Unexpected non-doc changes are scope drift — MUST.** If a docs-only PR changes non-doc surfaces, the review must classify the result as scope drift unless the approved scope explicitly allowed those changes.  
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

Reality-audit summary counts — SHOULD. The audit summary should state the count of findings, the count of Must-act-now findings, proposal homes, and the main drift themes when those facts are available.

PF homes consulted versus receiving proposals — SHOULD. Reality audit summaries should state both the PF homes consulted for classification and the PF homes receiving proposals when those facts are available.

No receiving proposals must be explicit — SHOULD. If the audit consulted PF homes but proposes no PF doc deltas in the current pass, say that directly rather than leaving proposal routing implicit.

Consulted homes are not automatic drain targets — MUST. Do not treat a PF home consulted for classification as a receiving proposal home, drain target, or required doc-delta destination unless the audit actually proposes a change for that home.

Classification deltas are not automatic task deltas — MUST. If audit findings are canon-routing or classification deltas rather than new dev, ops, or remediation work, say that explicitly and do not imply PF09.x task scope.

PF09.x target specificity — SHOULD. When the PF09.x task-delta lane is used, state the exact phased PF09.x target. When it is not used, state that no PF09.x task delta is proposed.

Finding duplicate check — SHOULD. When an audit includes an existing issues list or previous-drift ledger, each finding should state whether it duplicates an existing issue and cite the duplicate or say no duplicate was found.

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

ADR overview table — SHOULD. When multiple ADRs are summarized together, include a compact overview table with ADR, Finding, Cleaned disposition, and Current action before the detailed ADR list.

Cleaned disposition labels — SHOULD. Use cleaned disposition wording to distinguish new decision required, existing PF10 coverage, permanent PF-Canon already governs, no ADR needed, optional improvement, and new classification or routing decision. Do not force an ADR when the issue is a proof gap, optional improvement, or already-governed requirement.

Current action column — SHOULD. Use current action wording to state the immediate writing, evidence, or drain posture without creating new implementation, OPS, evidence-home, or token scope by implication.

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

* Stale planned artifact path with equivalent proof — SHOULD. If the plan names a stale artifact path but PF10 or the governing source and the final report support a different implemented artifact that proves the same obligation, the deviation record should state the stale path, the implemented path, the governing source, the same-proof rationale, and the search result or other proof that the stale path was not the final deliverable.  
* Missing-but-redundant planned artifact classification — SHOULD. When the planned artifact is absent but the alternate implemented artifact is present, non-empty, governed, and proves the same goal, classify the gap as a planning or path mismatch rather than a behavior failure. Do not hide the missing planned path.  
* Precondition remediation may govern after rerun — SHOULD. If a step cannot be validly interpreted until a required precondition artifact exists, and an approved precondition step produces that artifact before the final rerun, the final rerun may govern the step outcome when it satisfies the approved criteria.  
* Attempt history remains part of the record — MUST. The earlier blocked, failed, or uninterpretable attempt must remain visible in the deviation record. Do not rewrite the step as though it passed without remediation.  
* Deviation does not change criteria by implication — MUST. If the accepted deviation does not change required deliverables or PASS/FAIL criteria, say so explicitly.  
* **Conflicting action-line references do not override required deliverables — SHOULD.** If a plan action line names a different path than the required deliverables list, and the current evidence satisfies the required deliverable path and PASS criteria, classify the difference as a planning or path-reference mismatch rather than a behavior failure.  
* **Required deliverables and PASS criteria control the deviation review — MUST.** When reviewing an accepted deviation, evaluate the governed files and criteria the plan actually required for PASS. Do not let a conflicting non-required action reference override current check-root evidence that satisfies the required deliverables.  
* **Suggested inspection-key mismatch is non-driving when proof is broader and governed — SHOULD.** If the plan suggests checking one result key but the final report proves the same or broader scope-boundary claim with a different governed key, record the mismatch and state why it does or does not drive the verdict.  
* **QA-created harness predicate defects may be planning defects — SHOULD.** If a QA-created helper or harness predicate produces a false behavior failure while stronger governed evidence proves the intended criterion, classify the defect as a planning, harness, or evidence-interpretation defect when remediation stays within the approved evidence path.  
* **Planning or harness predicate remediation must remain auditable — MUST.** The deviation record must preserve the failure signature, the changed predicate or helper path, the remediation note, the rerun PASS excerpt, the changed-files or delta artifact, and the reason the remediated evidence satisfies the governing criteria.  
* **Do not relabel remediated harness defects as product failures — MUST NOT.** When the issue is the plan-created predicate or helper logic and final governed evidence satisfies the approved criteria, do not classify the final posture as product behavior failure.  
* Truncated or malformed pasted transcript reconstruction — SHOULD. If an interactive transcript, pasted helper transcript, or chat-visible command block is truncated, malformed, or not directly runnable, but the approved plan and final governed artifacts prove the same proof target, the deviation record may classify reconstruction as acceptable.  
* Direct artifact reads control over chat transcript — MUST. When chat transcript content is truncated, malformed, display-layer-only, or otherwise not reliable, review must rely on direct artifact reads, governed deliverables, and path-proofed evidence rather than the chat transcript.  
* Reconstruction record shape — MUST. The deviation record must state what transcript or command block was unavailable, truncated, malformed, or reconstructed; what approved source was used; what was actually run; which governed files record the result; and why the proof target, scope boundary, rails posture, token posture, and PASS/FAIL criteria were unchanged.  
* Ephemeral helper reconstruction stays execution-only — MUST. If a helper wrapper is reconstructed in a temporary location for execution, the review must state that it is execution-only unless the approved plan makes it a governed deliverable. Do not treat temporary helper scripts as evidence artifacts by implication.

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

* Source-of-truth posture must be stated, including the primary live source, the role of QA/process canon where the live source is silent, the role of process or template canon where used, and any input source used only for intended-scope framing.  
* D0, Step-0, discovery, and baseline rails posture must be covered when the QA plan or reviewed source includes those steps.  
* Coverage vs QA Plan accounting must be explicit, step-by-step, complete, in plan order, and auditable.  
* Coverage accounting must distinguish original and accepted receipts — MUST. If a step has both an original failed, blocked, or superseded receipt and an accepted remediation receipt, the closeout review must list or otherwise distinguish both receipt classes.  
* Final accepted proof basis must be named — MUST. For any remediated step, the coverage accounting must identify which receipt is the final accepted proof basis and why earlier receipts do not control the final verdict.  
* Failed original receipts remain evidence history — MUST. Do not overwrite, hide, or collapse original failure receipts when accepted remediation receipts are present.  
* Execution venue provenance accounting — SHOULD. Final QA closeout reviews should state whether Codespaces or other governed venue provenance is proven by a distinct artifact, by step-scoped Live QA records, or not proven.  
* No distinct venue artifact must be stated — SHOULD. If no distinct closeout venue-provenance artifact is present, say that directly and identify which Live QA records, if any, support venue posture.  
* QA timeline must include QA steps, remediation loops, ADR or decision events, and the ordering rule used when timestamps are absent or incomplete.  
* Findings must include classification and evidence pointers. When useful, include an anomaly label and PF touchpoint.  
* Findings classification must preserve the observed issue class — MUST. Use a source-faithful classification such as evidence posture gap, implementation gap, tooling-infra gap, process-rail gap, plan-guidance ambiguity, source-of-truth mismatch, plan-to-evidence drift, or other. Do not flatten distinct issue classes into a single generic defect label.  
* Root cause analysis must distinguish the primary root cause, contributing factors, what made the issue hard to detect, and what made the issue hard to close confidently.  
* Remediation loop assessment must retain the failure signature, remediation note, rerun outcome, and scope-boundary effect for each loop that materially shaped the verdict.  
* Implementation gaps and proposed fixes must be listed separately from findings. Each gap should include symptom, expected behavior, evidence pointer, likely locus only when the source names one, high-level proposed fix, and verification hook.  
* Doc deltas must be PF-Canon only and must exclude PF10 as a drain target. PF10 may be the live source basis, but the proposed permanent-home delta must route to the owning PF-canon document.  
* Explicit verdict and recommendation must state readiness, caveats, non-claims, and suggested follow-up without collapsing QA readiness into PF09 drain, formal close-pack completion, or implementation completion unless the evidence proves that exact claim.  
* Closure-axis separation — SHOULD. When a closeout recommendation supports readiness or closure, state separately whether each relevant closure axis is claimed, not claimed, unknown, or deferred: repo-supported completion, formal close-pack completion, board update, canon-drain completion, merge provenance, QA readiness, and implementation completion.  
* Follow-up recommendations must preserve axis separation — MUST. Do not write a suggested follow-up as though repo support, formal closure, board status, drain status, merge status, QA readiness, and implementation completion are the same state.  
* Step-level PASS evidence trust must be manifest-bound — MUST. Final QA closeout reviews must not treat a step’s PASS result or result JSON summary as sufficient by itself when the governing QA evidence posture requires manifest, primary-log, header, path-proof, or tokenless-posture proof.  
* Final QA closeout must surface per-step trust proof — MUST. For each executed step cluster being approved, the closeout review must expose or point to the manifest entry, primary-log header, captured\_env, evidence\_artifacts, intended\_tokens, claimed\_tokens, and path-proof binding when those fields are required by the governing QA posture.  
* Missing manifest or header proof is an evidence posture gap — MUST. If a reviewed step claims PASS but lacks required manifest binding, primary-header trust proof, or path-proof evidence, classify it as an evidence posture gap until restored.

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

Root causes

* Primary root cause — SHOULD. State the main failure class in one evidence-grounded sentence.  
* Contributing factors — SHOULD. List the concrete factors that made the failure possible, confusing, or hard to classify.  
* Detection difficulty — SHOULD. State what made the issue hard to detect earlier, especially when adjacent proof signals were green before the decisive predicate was complete.  
* Closure difficulty — SHOULD. State what made the issue hard to close confidently, especially when multiple source layers, proof classes, remediation loops, or non-claim boundaries had to be reconciled.

Remediation Loop Assessment

* Loop summary — SHOULD. For each material remediation loop, state the check or task, initial status, approved remediation action, rerun or validation action, final status, and evidence pointer.  
* Boundary preservation — MUST. State whether the loop reduced uncertainty without widening scope, changing PASS/FAIL criteria, opening rails, rerunning external calls, or editing PF-canon during QA execution.  
* Repeatable lesson — SHOULD. If a remediation loop exposes a general class of defect, state the rule or future-review posture that would prevent recurrence.

Evidence Hygiene Assessment

* **Evidence hygiene assessment — SHOULD.** When QA closeout depends on multiple evidence families, include a short assessment that separates strong evidence posture from repeatable risk.  
* **Strong evidence posture — SHOULD.** Name which evidence controls increased trust, such as step logs, path proofs, evidence validators, checksums, close-pack binding, or non-claim posture.  
* **Evidence risk posture — SHOULD.** Name risks that could recur in future epics, especially green-looking generated evidence, missing decisive predicates, blurred proof classes, weak vendor-backed proof, or later-drain ambiguity.

What Would Prevent Recurrence

* **Prevention actions — SHOULD.** List the canon, template, harness, review, or process changes that would prevent the same failure class from recurring.  
* **Prevention actions are not automatic blockers — MUST.** Do not convert prevention follow-ups into blockers unless the reviewed source defines them as required for the current closeout verdict.

Implementation Gaps and Proposed Fixes

* Gap record shape — SHOULD. For each gap, record symptom, expected behavior, evidence pointer, likely locus only if the source names one, high-level proposed fix, and verification hook.  
* Locus discipline — MUST. Do not invent a likely locus. If the source does not name a component, surface, file, or command, write the locus as not named in reviewed sources.  
* Verification hook required — MUST. Each proposed fix must include the evidence or check that would prove the fix held.

Doc Deltas

* PF-Canon only — MUST. Doc deltas in final QA closeout RCA must target permanent PF-canon homes only and must exclude PF10 as a drain target.  
* Targeted delta shape — SHOULD. For each doc delta, record target doc, target section, delta text or delta claim, tag, and evidence basis.  
* No optional delta inflation — SHOULD. If no optional other PF doc deltas are needed, state that directly.

QA Verdict and Recommendation

* Verdict label — MUST. Use a clear readiness label such as READY, READY WITH CAVEATS, or NOT READY.  
* Caveats — SHOULD. State caveats separately from blockers and distinguish QA closeout readiness from PF09 drainage, formal close-pack completion, implementation completion, and permanent canon drain.  
* Suggested follow-up — SHOULD. Include only follow-up that preserves source truth and does not imply the follow-up is already complete.

Common fix themes to consider

* QoS stop-rule for repeated structural remediation.  
* Rails posture truthfulness and explicitness in plans and rollups.  
* Prompt mode separation between planning, authoring, and review to prevent plan text from being mistaken for executed evidence.  
* Artifact-list invariants, including `primary.log` when a step ran.  
* Closure record semantics for deferred checks: do not list future or deferred step artifacts as required primary evidence for the current run.

  ### **15.18 Epic closure review template (closure registers \+ trace ledger)**

Use this when you need to determine whether an epic can be formally closed, and if not, the minimal follow-ups required to make closure defensible and canon-aligned.

* **Title line format — SHOULD.** Write `Epic Closure Review —` followed by the epic ID.  
* **Input naming — SHOULD.** When the actual inputs are an Implementation Guide and a QA Plan, name them that way rather than using more generic plan labels. If other inputs were reviewed, list only the inputs actually used.  
* **Input-name mismatch must be source-adjudicated — MUST.** If the prompt, artifact map, or operator label names an epic, phase, pass, or artifact differently from PF10 and the reviewed source set, evaluate under the controlling source identity and preserve the prompt label only as a non-authoritative artifact-map value.  
* **Do not normalize source identity silently — MUST.** State the mismatch, cite the controlling source or sources, and state which identity governs the review.  
* **Prompt labels are not source truth — MUST.** A prompt label may be recorded for traceability, but it must not override PF10, PF-Canon, or the artifact under review when those sources explicitly identify the epic or phase.  
* **Source-of-truth role split — SHOULD.** In the inputs posture, state not only the primary source of truth but also which canon homes supplied closeout requirements or close-gate deliverable posture when that matters to the judgment.  
* **PF23 reality context is not closure authority — MUST.** In epic closure reviews, PF23 may supply current-reality context, drift signals, path framing, locus framing, or classification questions. PF23 must not be written as closure proof, a gate, an acceptance source, or a blocker by itself.  
* **PF20 exclusion must be explicit when relevant — SHOULD.** If PF20 was not used, say that directly. If PF20 is mentioned for historical context, label it historical-only and do not use it as current planning, QA, acceptance, or closure authority.  
* **Intended-scope inputs stay framing-only unless evidence proves more — MUST.** If an Implementation Guide or QA Plan is used only for intended epic goals, expected requirements, or expected evidence framing, state that role explicitly and do not treat the input as proof that execution occurred.  
* **Deliverables register detail — SHOULD.** For each deliverable entry, prefer a human-readable deliverable label, record the source, include a verbatim anchor quote, list any required evidence, path, or token strings verbatim when present, and add at least one evidence pointer.  
* **Deferred or excluded scopes should be carried as boundary rows — SHOULD.** If reviewed sources name adjacent scope that was explicitly deferred, excluded, or not absorbed, closure registers should include it as an exclusion or boundary row when that helps prevent later scope drift.  
* **Boundary rows are not closure deliverables — MUST.** A deferred or excluded-scope row must not be treated as a required closure deliverable, missing evidence item, or acceptance blocker when the source marks it outside the epic’s closure burden.  
* **Adjacent deferred scope must not be silently absorbed — MUST.** When adjacent public, vendor, live-provider, route, smoke, or runtime surfaces are explicitly out of scope, the closure review must preserve that boundary and must not imply those surfaces were changed, validated, or closed.  
* **QA verification register detail — SHOULD.** For each QA step, prefer a human-readable verification label, include the verbatim check anchor, state the required evidence outputs and stated pass or fail posture, and add the decisive evidence pointer.  
* **PF10 results register detail — SHOULD.** Prefer a short result claim summary rather than an opaque result ID. Record whether the decisive PF10 addendum gives direct `Evidence pointer:` lines or only evidence-basis prose, and say `none provided` explicitly when no direct pointer lines exist.  
* **PF23 reality summary detail — SHOULD.** For each PF23 reality item, summarize the surface or component, list the verbatim paths or components, and state the closeout impact as supports, partial, not addressed, or contradicts.  
* **Closure trace ledger evidence hooks — SHOULD.** Each closure-trace entry should map the deliverable to its QA verification items, PF10 result claims, PF23 reality check, status, why, and the decisive evidence pointers.  
* **Path and surface reality ledger — SHOULD.** When closure depends on both repo paths and surfaced routes, use a path-and-surface reality ledger. Record the verbatim path or surface string, the proving source or sources, the status, whether it is required for closure, and why it matters.  
* **Accepted execution deviations — SHOULD.** If the closure judgment depends on an approved rerun, dependency-preflight correction, rails exception, or other bounded deviation, surface that deviation explicitly in the closure review rather than leaving it implicit inside PASS-only prose.  
* **Auditability caveat for decisive PF10 authority — SHOULD.** If the decisive PF10 close-authority addendum uses evidence-basis prose rather than direct `Evidence pointer:` lines, state that explicitly as an auditability caveat and keep it separate from the closure-truth judgment.  
* **Closure decision prose — SHOULD.** In the final closure decision, state the binary verdict, then explain the verdict with short evidence-grounded prose rather than only a label.  
* **Source-recorded path casing must be preserved — MUST.** Path and surface ledgers must copy path strings exactly as the source records them. Do not lowercase, rename, or normalize uppercase close-pack filenames or other source-recorded path strings inside the review.  
* **Unusual path casing must be classified, not silently corrected — SHOULD.** If a path appears to conflict with a general naming rail but is source-recorded or canon-patterned, label that posture in the Notes field and route any naming concern as a doc-delta or drift question rather than changing the path text.  
* **Closure axes remain separate — MUST.** In an epic closure review, SATISFIED means the reviewed closure trace is supported by the cited sources. QA evidence, PF09 status drainage, PO closeout, board state, merge provenance, PF-canon drainage, implementation completion, and permanent canon update are separate axes. Do not collapse them. A review, Lead report, QA evidence package, PF10 record, board event, PR merge, or later-drain recommendation may support another axis only when the evidence proves that exact action.  
* **Documentation drainage alone is not a closure gate — MUST NOT.** PF09 status drainage, PF-canon drainage, and other documentation/status-drain work must not block QA, implementation acceptance, or closure review when PF10 records the current live truth, governed evidence supports it, and no truth, proof, execution, safety, secret, scope, token, phase, production-functionality, or unresolved source-of-truth ambiguity remains.

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
* **Risk and debt item shape — SHOULD.** For each Must-fix, Should-fix, and Nice-to-have item, record the evidence status, the evidence pointer, why it matters, and what would prove resolution or improvement.  
* **Unknown risk posture — SHOULD.** If the reviewed sources do not prove whether a closeout, QA, drain, validation, or tooling item exists, label the evidence status as Unknown from reviewed sources rather than treating the item as proven missing.  
* **Proof-to-close wording — SHOULD.** State what would prove the risk closed using concrete artifact, validation, or decision evidence when known.  
* **ADR record completeness — SHOULD.** For each ADR, record the decision point, the options considered when visible, the PF-canon constraints relied on, the final decision for this epic, whether it should become canonical for future work, and the decisive evidence pointer.  
* **ADR disposition labeling — SHOULD.** When helpful, label the ADR as NEW CANON PROPOSAL, Epic-only clarification, or Historical only so the future-drain posture is explicit.  
* **PF-canon doc-delta completeness — SHOULD.** Do not stop at a bare doc title. For each proposed PF-canon delta, record the target doc, the target section or closest stable home, the delta itself, why that doc is the correct home, and the supporting evidence pointer.  
* **No PF-canon doc-delta outcome must be explicit — SHOULD.** If a lead dev retrospective concludes that no PF-canon doc deltas are required, state that directly in the PF-Canon Doc Deltas section and cite the evidence basis or reviewed source that supports the no-delta posture.  
* **No-delta posture is not no-review posture — MUST.** Do not leave the doc-delta section blank. A no-delta conclusion must still be reviewable as a stated outcome.  
* **Future-work record shape — SHOULD.** For each build improvement or future-work item, record the short description, where it should live, which PF docs would be touched if pursued, and whether it depends on PF23-identified reality drift.  
* **Recommendation-only closeout posture — SHOULD.** End with a recommendation-only section that states the readiness or closure recommendation, the most important process improvement, the most important system-level follow-up, whether any additional hard requirement appears necessary before close, and the final implementation posture recommendation.  
* **Internal retrospective title may omit repeated addendum identity — SHOULD.** If the parent PF10 addendum heading or enclosing artifact already carries the addendum identifier, the internal lead retrospective title may use `Lead Dev Epic Retrospective —` followed by the epic ID without repeating the addendum identity.  
* **Standalone retrospective title still needs durable identity — MUST.** If the retrospective is not enclosed by a parent addendum heading or other durable artifact identity, the title line must include enough identity to route and audit the artifact without guessing.

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

