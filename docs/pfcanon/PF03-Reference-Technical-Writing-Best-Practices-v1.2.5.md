## **0\) Front Matter — Document Control**

**Title:** PF03-Reference-Technical-Writing-Best-Practices

**Version**: v1.2.5

**Status:** Reference

**Effective date:** 2026-02-08

**Last Update Gate:** BN 9.8.2 Drain A49-51

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

PF23 contradiction posture — MUST. When PF23 contradicts PF canon, record the contradiction as a drift item (with both quotes) and route to PO adjudication. Do not resolve the contradiction by assumption inside the plan or the plan review.

Canonical references — MUST. When a PF doc references another PF doc, it must point to title (and stable section if defined as stable). Do not point to commit hashes, PR numbers, or mutable URLs as canonical references.

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

* Stop and escalate, do not grind — MUST. Once a step is clearly in a `FAIL_TOOLING` state (no evidence after multiple correct attempts), the QA plan MUST instruct the operator to stop re-running the same command, append a short failure summary to the step log, and escalate by opening a follow-up task/bug. Plans SHOULD NOT ask the operator to repeat an unchanged command indefinitely when the harness is not producing evidence.

* Separation from behavior verdicts — SHOULD. Behavior-level verdicts (for example, claims about application correctness) MUST NOT be asserted when the underlying tool or harness has not produced any evidence of running. In this case, the only honest summary is that the step is blocked on tooling, and behavior remains unproven for that run.

* Status vocabulary — MUST. Step logs MUST use the canonical status vocabulary defined in the Glow QA Guide and MUST distinguish tooling failure from behavior failure. Do not introduce ad-hoc execution statuses for core step state.

These conventions keep Live QA plans mechanical, fair to the operator, and honest about the difference between “the app failed” and “our harness is not capturing the run.”

### **12.3 Command and procedure style (QA plans)**

* Prefer directive-first steps for Live QA Plans. Steps MAY be written as objective-first directives.

* Plans MUST NOT be required to provide verbatim, syntax-perfect command lines. Require the execution transcript (step log or generator output listed as a Deliverable) to capture the exact commands used.

* If command text is included, use inline shell (as code spans) and keep it single-line when possible. Avoid multi-line command blocks; if unavoidable, keep them as one copy/paste block and keep all required substitutions explicit.

* Avoid “run this somewhere” prose. Specify repo-root relative paths and deterministic file locations.

* Do not use `<PO_INPUT>` placeholders in step lists. If PO input is needed, include it in a dedicated “PO inputs” section.

* Environment bootstrapping. If the procedure requires environment bootstrapping, explicitly reference the standard bootstrap script and run the enforcement inside a subshell (for example, `bash -lc "<SUBSHELL_COMMAND>"`).

* If evidence is generated, specify `audit/qa/<epic-id>/<run>/` and list exact files created.

### **12.4 QA runbooks & evidence documentation (Live QA)**

Live QA plans and Live QA runbooks are engineering docs. They must be runnable, auditable, and free of hand-edited evidence.

Apply these rules in addition to §12.1–§12.3 and §13.1:

* Step-level Deliverables — MUST. Every step in a QA plan or Live QA runbook MUST include a **Deliverables** list that names the minimal evidence set for that step using fully qualified file paths (for example, under `audit/qa/<epic-id>/<run>/`).

  * If the step creates new evidence, Deliverables MUST name the files that will be created.

  * If the step only reads existing artifacts, Deliverables MUST still name the files being read and state that no new files are created.

* PASS/FAIL defined by files — MUST. Each step’s PASS/FAIL criteria MUST be defined in terms of its Deliverables (existence, non-emptiness, and simple content checks). Avoid vague criteria like “looks good” or “works”; the step verdict must be reviewable from the listed files.

* Gitless runbooks — MUST. Live QA runbooks MUST NOT include git gating (including “working tree clean”) as PASS/FAIL criteria. If traceability capture is needed, it MUST be artifact-only and non-blocking (for example, record branch and commit in the README and/or a snapshot log).

* Script-generated Live QA README — MUST. A Live QA sequence MUST end with a **script-generated** summary README (for example, `audit/qa/<epic-id>/live-qa/README.md`). The README is an evidence artifact and MUST be produced by a command or tool, not by manual editing.

   The script-generated README MUST include, at minimum:

  * Run metadata: date/time (prefer UTC), branch, and commit SHA.

  * Rails posture summary (env pins and any deviations) as captured by the run.

  * Per-step commands and the per-step Deliverables (paths only).

  * Evidence file index (a list of the evidence files under the Live QA directory tree).

  * PF references (document titles and § anchors only; no version numbers).

  * Verdict and deviations/issues (including any FAIL\_TOOLING outcomes and what was escalated).

* No manual-fill placeholders — MUST NOT. No QA evidence file may include “fill in PASS/FAIL” or other manual-entry placeholders. If a result is “no deltas,” the generator MUST emit that explicitly as produced output.

* No manual edits to QA evidence — MUST NOT. QA plans and runbooks MUST NOT instruct an operator to open evidence files (logs, manifests, READMEs) in an editor and type changes by hand. If a summary must change, the correct procedure is to re-run the generator so the result remains reproducible.  
* **Step log header inputs — MUST.** If a plan step relies on a governed step log (for example `primary.log`) as a Deliverable, the plan MUST ensure the log is generated by the harness and includes its machine header. If the header writer depends on env var inputs, the plan MUST export the required canonical env vars in the step context (not as an ambient global). Missing required exports is a mechanical blocker for claiming PASS based on that evidence.  
* **Deferred evidence labeling in templates — MUST.** Any QA plan template, deliverables report, closure record, or rollup that enumerates step-scoped evidence paths MUST explicitly label future-step artifacts as `NOT RUN` or `DEFERRED` until the producing step has executed.  
* **Do not treat deferred artifacts as missing evidence — MUST.** When writing summaries, evidence prints, or rollups, `NOT RUN` and `DEFERRED` states MUST remain distinct from missing evidence findings. Do not describe `NOT RUN` or `DEFERRED` artifacts as missing evidence.

These are documentation rules only. They do not redefine token ownership or evidence semantics owned by other PF documents; they define how QA instructions and QA summaries must be written to remain auditable and reproducible.

### **12.5 Live QA plan approval reviews (BLOCKERS vs CAVEATS)**

For any review / approval step in Live QA plans:

* **BLOCKERS** (`BLK-01`, `BLK-02`, \[LIST CONTINUES\]): any item that prevents execution of the plan or invalidates the run.

* **CAVEATS** (`CAV-01`, `CAV-02`, \[LIST CONTINUES\]): risks, uncertainties, assumptions, or optional improvements that do not block execution.  
* **Prohibited ellipsis patterns are mechanical blockers — MUST.** Treat any occurrence of the Unicode ellipsis character (U+2026) or the ASCII triple-dot sequence as a BLOCKER in plan approval reviews. Replace with approved omission markers or move the literal string into a repo file and reference it by exact path and filename.  
* **Heading marker levels are non-reviewable — MUST NOT.** Reviewers MUST NOT block approval based on heading marker levels or require heading-level changes as a condition of approval. Review required sections by the heading text and required content, not by the markdown level.  
* **Non-blocking plan formatting variance — MUST.** Formatting variance that is purely presentation (bullet marker choice, indentation, line wrapping, extra blank lines, tables vs bullets, emphasis style) is not a blocker. Record such notes as CAVEATS or follow-ups only.  
* **Formatting becomes a blocker only when it impacts meaning or execution — MUST.** Treat as BLOCKERS only when the variance causes missing required sections or fields, changes semantics, makes commands non-copyable, breaks step IDs or evidence filenames, or otherwise prevents safe execution and evidence capture.  
* **QA prompt mode declaration — MUST.** Any QA prompt or QA-related request MUST declare its mode as `AUTHORING` or `REVIEW` before the body.  
* **No cross-mode mixing — MUST.** The response MUST follow the mode’s required structure and MUST NOT blend `AUTHORING` content (runbooks, new commands, new steps) into `REVIEW` outputs (evidence evaluation and verdict), or vice versa.

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

* **Drift assessment stub — MUST.** If PF23 contradicts PF canon:

  * Record the PF23 claim (quote).

  * Record the PF canon claim (quote, with title and § anchor).

  * Identify the impacted surface and locus.

  * Assign a tentative bucket: canon defect, implementation drift, or necessary reality shift.

  * Route to PO adjudication. Do not resolve by assumption in the plan or the plan review.

* **Routing for PR analysis — SHOULD.** When grounding PR analysis, route to the PF canon home that owns the domain under review (examples: HDE Architecture, Governance & Process Handbook, CLI/API/Vendor, HDE Schemas and Artifacts, HDE Build Checklist, HDE Mechanics Guide, Glow QA Guide, Epic Process Guide, HDE Build Notes).

## 13\) Security & privacy for writing

* No secrets in examples — MUST. Redact or use obvious placeholders; never paste API keys, cookies, or bearer tokens.  
* Keys-only logs in examples — MUST. Never show raw PII or secrets; summarize with names-only.  
* Local only — MUST. Do not imply writes to repos or external systems; all outputs are paste-ready text.  
* Evidence artifacts — SHOULD. Names/paths only in PF; bytes live outside PF and follow §4 canonical JSON rules.

### **13.1 Evidence & log naming (QA)**

QA evidence logs are text artifacts and follow the same naming hygiene as all examples in this doc. When you design or update a Live QA plan or QA harness, apply these rules:

* Run-root location — MUST. Each QA run defines a single run root directory (for example, `QA_ROOT`). The primary step logs for that run MUST live directly under that run root; do not scatter primary step logs into ad-hoc subdirectories such as `logs/` without a clear pointer from the root.

* Deterministic step-log names — MUST. Within a given run root, name step logs using a single, consistent pattern. Two accepted patterns are:

  * `D<goal>_<shortname>.log` (for example, `D4_sampler_evidence_index.log`), or

  * `stepN_<shortname>.log` (for example, `step5_sampler_evidence_index.log`).  
     Pick one pattern per epic or QA run and use it consistently for all steps in that context.

* One primary log per step — MUST. For each QA plan step, choose a single primary step log file at the run root and append all tests and checks for that step to that log (pytest output, greps, summary lines). Do not split the same step’s evidence across multiple unnamed or unreferenced logs.

* No mixed schemes in the same context — MUST NOT. Within a single run root, do not mix different step-log naming schemes (for example, `D3-http-*`, `step4_*`, `D1D2-*` side by side). Mixed schemes make evidence hard to trace and review.

* Temporary scratch files — SHOULD. Temporary request/response bodies or scratch outputs SHOULD:

  * Use a `tmp_` prefix in the filename, and

  * Either live next to the step log they support, or live under a dedicated `tmp/` subdirectory under the run root.

These rules do not change how sampler/core or other tests are written; they set expectations for the quality and traceability of QA evidence artifacts and keep log naming consistent with the Evidence artifacts guidance in this section.

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

Use this structure for any QA plan or Live QA runbook step that includes executable commands. This template enforces §12.4.

Step \<N\> — \<short step title\>

Check ID: \<stable id for this step\>  
 PF refs: \<PF document title § anchor list\>  
 Tokens (names only): \<token list, if applicable\>

Directive: \<objective-first instruction for this step\>

Command (optional; verified only): \<single copy/paste-ready command string\>

Deliverables (paths only):

* \<fully qualified path 1\> — \<one-line description\>

* \<fully qualified path 2\> — \<one-line description\>

PASS criteria (file-based):

* \<what must be true in the Deliverables, stated in terms of existence/non-emptiness/simple checks\>

FAIL criteria (file-based):

* \<what would constitute failure, stated in terms of Deliverables and their content\>

Final status marker: `PENDING` → `PASS` | `FAIL` | `FAIL_TOOLING` (recorded in the primary step log)

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

RCA (required when any failure, bug, or CI failure is evidenced)

RCA-001

* A) Failure statement (quoted): \<VERBATIM\_FAILURE\_LINE\>

* B) Where it occurred: \<ATTEMPT\_OR\_CONTEXT\>

* C) Root cause(s): \<CAUSE\_STATEMENT\>

* D) Fix progression across attempts: \<WHAT\_CHANGED\_OVER\_ATTEMPTS\>

* E) Fix verification: \<PASS\_PROOF\_LINE\>

* Residual risk (evidenced): \<NONE or DESCRIBE\>

Findings (includes diff review)

* Observed: \<FACT\>

* Why it matters: \<IMPACT\>

* Evidence pointer: \<PATH or PR-ARTIFACT-HEADING\>

* Evidence hygiene risk (if any): \<NONE or DESCRIBE\>

Requirement Satisfaction Crosswalk (required when plan requirements are explicit)

* Requirement: \<REQUIREMENT\_TEXT\>

* Status by attempt: \<ATTEMPT\_0\_STATUS\> → \<ATTEMPT\_1\_STATUS\> → \<ATTEMPT\_2\_STATUS\>

* Evidence pointer(s): \<POINTERS\>

Doc Deltas (PF-Canon only; always include when any PF canon doc needs change)

Doc: \<PF\_TITLE\>

Section: \<SECTION\_ANCHOR\>

Delta: \<WHAT\_NEEDS\_TO\_CHANGE\>

Why: \<WHY\>

PF excerpt (verbatim, 1–5 lines): \<PASTE\_VERBATIM\>

PR behavior evidence: \<POINTER\_TO\_DIFF\_OR\_PROOF\>

Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

* \<TOKEN\_NAME\_1\> | \<TOKEN\_NAME\_2\> | None

* Token search method (if None): \<WHERE\_YOU\_SEARCHED\>

B) Evidence artifacts produced or updated

* Path: \<REPO\_PATH\>

* Type: \<json | jsonl | log | txt | sha256 sidecar | other\>

* Key proof facts (verbatim, short): \<1–5 lines\>

* Evidence pointer: \<POINTER\>

C) Test or CI proof

* Command: \<SINGLE\_COMMAND\> (or `None recorded`)

* Pass indicator (verbatim): \<PASS\_LINE\> (or `None recorded`)

* Where it appears: \<PR\_ARTIFACT\_SECTION\> (or `Not present in PR artifacts`)

* Search method (required if any field is `None recorded`): \<WHERE\_YOU\_SEARCHED\>

* Risk note (required for docs-only PRs with contract-level assertions): \<1–2 sentences; note drift risk for token strings, endpoint lists, exit/error identifiers, or owned path lists\>

* Docs-only PRs: apply §15.13 Docs-only PR evidence posture checklist (minimum).


### **15.13 Docs-only PR evidence posture checklist (minimum)**

Use this checklist when the PR diff is docs-only (documentation files only).

* Scope confirmation (docs-only):

  * List files changed (expected vs unexpected) and confirm no code or config changes.

* Verification capture (minimum):

  * Capture at least one proof line in PR artifacts (command and pass indicator) for a markdown sanity check or doc lint run.

* Contract-level assertions:

  * If documentation asserts token strings, endpoint lists, exit/error identifiers, or owned path lists, state how each assertion was verified (evidence pointer, repo search, or test output).

  * If any such claim is not verified, mark it as unverified and record it under DOC\_RISKS\_NOTED\_OK.

* PR analysis record:

  * In the PR analysis record template, complete Evidence Print C) Test or CI proof.

  * If no proof is recorded, include the search method and record the gap under DOC\_RISKS\_NOTED\_OK.

### **15.14 Reality audit report template (Audit Summary \+ Doc Delta Map)**

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

Use this when you need a paste-ready decision record for one QA check (PASS, FAIL, or NOT RUN). This is appropriate as a PF10 addendum entry or as a standalone QA decision note.

Title line format:

* `\<ADDENDUM_ID\> \<EPIC_ID\> QA: \<CHECK_ID\> — Decision: \<PASS | FAIL | NOT RUN\>`

Required sections and fields:

Review Summary

* 2–6 sentences. State what was checked, what evidence was produced, and which pass or fail criteria were applied.

* If the decision is NOT RUN, state why it was not run and what evidence is missing.

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

* Artifacts relied on (paths only; include `primary.log` when a step ran):

  * \<path 1\>

  * \<path 2\>

* Key proof facts (verbatim quotes, 1–5 lines each):

  * \<quote block 1\>

  * \<quote block 2\>

* Execution trace (if applicable):

  * Command (verbatim): \<command line\>

  * Command provenance: \<Plan | Scaffolding | Manual | Unknown\>

  * Exit code (if known): \<0 | non-zero | Unknown\>

QA Verdict and Optional Follow-ups

* Verdict: \<PASS | FAIL | NOT RUN\>

* Rationale: \<2–6 sentences; must align with the Findings marked Drives decision: Yes\>

* Optional follow-ups (do not mix with the verdict rationale):

  * \<follow-up 1\>

  * \<follow-up 2\>

Evidence pointer format guidance (recommended)

* Prefer a pointer that names the source doc and the exact excerpt you relied on.

* One acceptable format is a pipe-delimited pointer:

* Evidence pointer: | \<Source doc\>: \<section locator\> | "\<verbatim line 1\>" | "\<verbatim line 2\>" | "\<verbatim line 3\>"

Notes

* Do not paste long JSON blobs into the decision record. Instead, point to the file and quote only the 1–3 fields that drive the decision.

* If you cannot verify a claim due to missing artifacts, treat it as Unknown and say so explicitly.

### **15.17 Final QA closeout review template (closeout summary \+ QA RCA)**

Use this when you need a final QA closeout narrative that combines (a) a coverage and readiness statement and (b) a QA RCA suitable for preventing recurrence.

Title line format:

* `\<ADDENDUM_ID\> Final QA Closeout Review + QA RCA — \<EPIC_ID\>`

QA Closeout Summary

* Scope: \<list the QA plan checks covered by this closeout\>

* Readiness verdict: \<READY | READY WITH CAVEATS | NOT READY\>

* One-paragraph summary of why the verdict is correct.

* If readiness is READY WITH CAVEATS, state whether the caveats are process failures, product failures, or both.

Canonical RCA requirement basis (cite canon, do not paraphrase)

* List the canonical requirements that make an RCA required and that define its minimum contents.

* Use a no-outs locator gate for each canon reference:

* Canon locator: \<PF doc title\> \<section locator\>

* Canon proof excerpt (verbatim, 1–3 lines): \<paste verbatim\>

RCA completeness checklist (include each item explicitly)

* Evidence-grounded outcomes: the RCA is anchored in observed evidence, not in speculation.

* Remediation loop accounting: repeated structural remediation is called out, including stop points or limits.

* Rails posture accounting: where a check required open rails or elevated capabilities, it is stated explicitly.

* Plan vs evidence cross-check: mismatches between planned and observed reality are enumerated with evidence pointers.

Timeline reconstruction (UTC)

* Provide only the minimum timeline needed to support the RCA.

* Format each entry as:

* \<YYYY-MM-DD HH:MM UTC\> — \<event summary\> (Evidence pointer: \<pointer\>)

Coverage vs QA plan

Coverage status rubric (use these exact labels)

* Fully evidenced: the check ran and the expected evidence artifacts exist.

* Partially evidenced: the check ran but one or more required artifacts are missing or incomplete.

* Not evidenced: the check is claimed but evidence artifacts are missing.

* Not run: the check did not run in the covered execution window.

Coverage matrix (one row per check)

* Check ID | Status | Evidence artifacts | Notes

Plan vs reality mismatches (if any)

* For each mismatch:

* Mismatch: \<one sentence\>

* Evidence pointers:

  * \<pointer 1\>

  * \<pointer 2\>

* Closeout impact: \<Non-blocker | Blocker | Unknown\>

* Remediation status: \<Resolved | Open | Not applicable\>

QA RCA (root causes and fixes)

Root causes (PF10-grounded)

* Primary root cause: \<one sentence\>

* Contributing factors:

  * \<factor 1\>

  * \<factor 2\>

Fix proposals (each fix must include a verification hook)

* Fix: \<one sentence\>

* Verification hook: \<how you will detect success in a future run\>

Common fix themes to consider (cite the applicable canon section when used)

* QoS stop-rule for repeated structural remediation.

* Rails posture truthfulness and explicitness in plans and rollups.

* Prompt mode separation (planning and authoring vs review) to prevent plan text from being mistaken for executed evidence.

* Artifact-list invariants, including `primary.log` when a step ran.

* Closure record semantics for deferred checks: do not list future or deferred step artifacts as required primary evidence for the current run.

### **15.18 Epic closure review template (docs-only closure assessment)**

Use this when you need to evaluate whether an epic is ready to close based on the available documentation and evidence artifacts.

Title line format:

* `\<ADDENDUM_ID\> Epic Closure Review — \<EPIC_ID\>`

Inputs posture (high-stakes for closure)

* What I reviewed (sources of truth):

  * \<doc or artifact 1\>

  * \<doc or artifact 2\>

* What I could not review (explicit blind spots):

  * \<blind spot 1\>

  * \<blind spot 2\>

Closure registers (what closure artifacts exist, and whether they are consistent)

* Closure artifacts reviewed (paths and purpose):

  * \<artifact path\> — \<purpose\>

  * \<artifact path\> — \<purpose\>

* Cross-check results:

  * \<cross-check 1 result\>

  * \<cross-check 2 result\>

Canon compliance cross-check (record Unknowns explicitly)

* Environment variable governance: confirm no non-canonical env var minting is present in captured environments (Evidence pointer: \<pointer\>).

* Root directory discipline: confirm evidence artifacts live under governed roots, and note any new top-level roots (Evidence pointer: \<pointer\>).

* Determinism posture: if any check required open rails or other non-default posture for determinism, state it explicitly (Evidence pointer: \<pointer\>).

* Path-proof adjacency: for any governed closure artifact, confirm the required path-proof sibling file exists per the applicable canon (Evidence pointer: \<pointer\>).

Closure decision

* Decision: \<CLOSE | CLOSE WITH CAVEATS | DO NOT CLOSE\>

* Rationale: \<3–8 sentences tied to evidence\>

* If CLOSE WITH CAVEATS or DO NOT CLOSE, list the minimum follow-ups.

Follow-ups (minimum necessary)

* \<follow-up 1\>

* \<follow-up 2\>

Retrospective (optional but recommended)

* What succeeded:

  * \<item 1\>

  * \<item 2\>

* What failed:

  * \<item 1\>

  * \<item 2\>

PF-canon doc deltas (titles-only)

* \<PF doc title\>: \<one sentence delta\>

* \<PF doc title\>: \<one sentence delta\>

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

