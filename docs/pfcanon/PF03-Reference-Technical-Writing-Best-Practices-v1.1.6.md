## **0\) Front Matter — Document Control**

**Title:** PF03-Reference-Technical-Writing-Best-Practices

**Version**: v1.1.6

**Status:** Reference

**Effective date:** 2026-01-01

**Last Update Gate:** BN 8.7.7 Drain 50-51

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

Single home per truth — MUST. Each rule lives in exactly one PF doc; other docs link by title only. Do not include version numbers in cross-doc prose.

AI-first granularity — SHOULD. Prefer small, purpose-built docs to a single omnibus; keep drift low and routing clear.

Deterministic artifacts — MUST. Every doc cut includes version, date, status, changelog, invocation tag, and provenance. Paste-safe formatting is required.

Evidence parity — MUST. Update the human Evidence Index and the machine JSONL mirror in the same PR; maintain 1:1 parity.

Full-document requirement — MUST. Obtain and read the complete source before editing; proceed in partial mode only with explicit PO approval and label outputs as Partial.

Planning MUST consult PF23 — MUST. For planning artifacts (non-exhaustive: QA plans, remediation guides, implementation guides, EPIC records, stepwise runbooks), consult PF23 — Reality Audits as a primary input for component boundaries and canonical pathnames/loci. Plans SHOULD include a short “PF23 Anchors” subsection listing: (a) the component(s) used from PF23 and (b) the key pathnames/loci the plan will touch. This is traceability only; it MUST NOT duplicate PF23 contents. PF23 is PO-maintained; plans MUST NOT create tasks that assign PF23 updates.

Heading numbering stability — MUST. Existing H1/H2 numbering is immutable. New content SHOULD be added as H3/H4 within an existing H2 whenever possible. If a new H1/H2 is truly required, it MAY be added, but it MUST take the next available number and MUST NOT alter any existing numbering.

Acceptance tokens (name \+ semantics) single source of truth — MUST. Acceptance token names and their semantics are defined once in the Governance & Process Handbook token registry. Any token name used in epic acceptance rosters, QA token libraries, acceptance maps, or evidence logs MUST match registry spelling exactly. Aliases and near-matches are prohibited. If a needed token is missing from the registry, record token drift and route it through governance registration before claiming it as a required acceptance token.

Review source-retrieval guard — MUST. Do not claim a mismatch for token rosters, rails/evidence posture, or byte/contract expectations unless you have retrieved the governing canonical passages for both sides of the claim (for example, the epic roster and the token registry entry; the rails rule; the contract section). If retrieval is incomplete, mark the item **\[OPEN\]** and request the missing passage instead of asserting.

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

* Acceptance impact: `READER_SUCCESS_ENDPOINTS_OK` added; **9\) Build Notes (Living) usage**

Append-only blocks — MUST. The writer delivers a **self-contained Addenda Block**; the PO pastes it at the end under “Addenda (append-only)”.

Delete-on-merge — MUST. After the PF target is updated, the PO **deletes** the block (or archives by versioning the doc).

No in-doc edits by AI — MUST. AI lead devs are **read-only** for Build Notes; edits occur in the target PF.

PF10 reference posture — MUST. When referencing Build Notes from other documents or reviews, reference Build Notes by **addendum number \+ addendum title** (for example, “Build Notes Addendum 2.10 — Token Load Reduction…”). Do not reference PF10 by version strings or PF10 section numbers as durable anchors; the stable unit is the addendum entry itself.

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

### 12.1 Engineering docs / QA plans (Live QA pattern)

Engineering docs such as Live QA plans are action lists, not narratives. When the PO asks for a Live QA plan, the writer MUST treat it as a mechanical script that another person or agent can run without interpretation.

Live QA plans MUST follow these patterns:

* One command per step. Present the plan as a numbered list where each step is a single, copy-pasteable command string (for example, a `bash` invocation or CLI call). Describe any needed context (environment, directory, preconditions) before or after the command, not interleaved inside it.

* One primary artifact per command. For each step, name at least one expected evidence artifact (for example, a file path, log, or bundle) that the command produces. State this next to the step so the relationship is explicit.

* Mechanical evidence only. Copy the exact command text and path names that will appear in the repo or QA tree. Avoid paraphrasing commands or artifact locations; the plan must match what will actually be executed.

* PF-canon citations by title and section. When a step relies on a rail, token, or behavior defined in PF-canon (for example, determinism env helpers or ownership of QA tokens), cite the governing document by title and § anchor in the plan. Do not include version numbers or quote older text; routing is titles-only.

* Separate mechanics from interpretation. Keep the step list purely mechanical. Any narrative interpretation, retrospective, or ADR commentary belongs in a short notes block after the steps or in a separate doc (for example, epic closeout or Build Notes), not interleaved with the commands themselves.

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

Commands in QA plans are not suggestions or templates; they are the exact procedures the operator will run, usually in a Codespaces shell at the repo root. Extend §12.1 and §12.2 as follows:

Fully concrete commands — MUST. Every QA plan command MUST be fully concrete and free of placeholders (no `<PO: …>`, `<path>`, or “TODO” markers). If a value is variable, compute or derive it in a prior step so that the command line itself requires no manual editing.

Copy/paste-ready for Codespaces — MUST. Commands MUST be usable as-is in the intended environment (typically a Bash shell in Codespaces at the repo root). The operator SHOULD be able to select the command line and paste it directly into the shell without adding flags, editing paths, or guessing environment variables.

Interactive-shell safety — MUST NOT. Command blocks intended for copy/paste into an interactive shell MUST NOT include `exit`, `return`, or other shell-terminating control flow that can close the operator’s session. If strict enforcement requires nonzero exit codes, run the enforcement inside a subshell (for example, `bash -lc '…'`) or write rc/status files and print a PASS/FAIL line without terminating the shell.

Scope-safe defaults — MUST. The primary copy/paste command in a plan MUST be correct for the current epic/run context. If a flag is only relevant to a different epic or context (for example, `--epic-id`), it MUST NOT appear in the primary command. If such a flag is useful, present it as an explicitly optional, non-default variant and state when it should be used.

Evidence paths and outcomes — MUST. For each command, the plan MUST name one or more concrete evidence paths (for example, specific log files or artifacts under `audit/qa/...`) and state the expected high-level outcome (for example, “2 passed, 0 failed” or “HTTP 200 from Reader”). This pairs the procedure with what the operator should see if the step succeeds.

No deferred decisions to the PO — MUST NOT. QA plans MUST NOT offload key decisions (paths, ports, env vars) to the PO in prose. If a value cannot be hard-coded, the plan MUST either provide a discovery command to obtain it or delegate the derivation to a canon-named entrypoint or inline tool (see “No non-canonical QA scripts or wrappers” below), with an invocation that is itself concrete and copy/paste-ready.

Clear separation from discovery — SHOULD. When discovery is required (for example, to locate a file, determine a port, or resolve a base URL), the plan SHOULD separate the discovery step(s) from the execution/verification step(s). Discovery outputs MUST be written to evidence files (for example, `selected_base_url.txt`) and then referenced by subsequent steps.

No non-canonical QA scripts or wrappers — MUST NOT. Live QA plans MUST NOT depend on repo scripts that are not canon-named entrypoints. Acceptable patterns are:

1. A canon-named entrypoint invoked by explicit path, or

2. An inline tool whose full source is embedded in the plan step and written into the run-local QA tools directory (no hidden dependencies).

When canon is silent on an entrypoint but requires an artifact surface, the plan SHOULD implement the artifact generation/validation directly using baseline commands (explicit shell/Python one-liners, direct invocation of canon tools, `tee` for logs, explicit file writes), rather than inventing a new repo script path.

No non-canonical env pins — MUST NOT. Live QA plans MUST NOT introduce additional “required pins” beyond the canonical determinism pins and rails posture. In particular, plans MUST NOT require `PYTHONHASHSEED` as a rail/pin. Determinism must be achieved by explicit ordering and canonical serialization; if output is nondeterministic due to unordered iteration or unstable ordering, treat it as a code or harness defect to fix, not a QA-plan knob to enforce.

These rules make QA plans executable without guesswork, align them with Codespaces as the default operator environment, and prevent plans from smuggling non-canonical dependencies (scripts or env pins) into “required” execution posture.

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

These are documentation rules only. They do not redefine token ownership or evidence semantics owned by other PF documents; they define how QA instructions and QA summaries must be written to remain auditable and reproducible.

### **12.5 Live QA plan approval reviews (BLOCKERS vs CAVEATS)**

When reviewing a Live QA plan for approval, findings MUST be separated into two lists:

* **BLOCKERS** (`BLK-01`, `BLK-02`, …): issues that prevent the operator from executing the plan as written in Codespaces **or** prevent reviewers from determining PASS/FAIL for the in-scope feature behavior with confidence.  
   Examples: missing required PO inputs (base URL/auth); commands not runnable or not copy/paste-ready; evidence capture paths not specified; PASS/FAIL criteria not defined in terms of evidence files; plan depends on manual-fill placeholders; plan matrix references step IDs that have no corresponding executable step definition; plan requires production code changes.

* **CAVEATS** (`CAV-01`, `CAV-02`, …): everything else. Any issue that does not block execution or verification MUST be recorded as a CAVEAT, not a Blocker.  
   Examples: incomplete token rosters; token registry mismatch that does not affect test interpretation; documentation drift that can be captured via doc-delta; formatting imperfections that do not obstruct execution; requests for additional “failure choreography” or extra enforcement beyond what is required for execution and file-based PASS/FAIL.

Review outcome rule:

* If and only if BLOCKERS exist → plan is rejected for revision.

* If no BLOCKERS exist → plan is approved even if CAVEATS exist.

No excerpt-based blockers — MUST. A reviewer MUST NOT assert a token/rails/bytes mismatch as a Blocker unless they have retrieved the governing canonical passages for both sides of the claim (see §3, Review source-retrieval guard).

### **12.6 Tokens in Live QA plans (load reduction \+ registry validity)**

Token handling SHOULD be reduced by default in Live QA plans. Plans SHOULD map steps to in-scope surfaces/flows and D-goals and define evidence capture and pass/fail criteria. Plans MAY omit a full token roster and MAY omit per-step token claims unless a token is required to interpret pass/fail for a specific check.

If tokens are listed or claimed for acceptance:

* Token names MUST be exact matches to the Governance & Process Handbook token registry. Do not introduce aliases, synonyms, or near-matches.

* If an epic roster or QA doc references a token name that is absent from the registry, record a CAVEAT: `UNREGISTERED_TOKEN` and do not claim that token as satisfied until it is registered. Do not invent substitute token names.

### **12.7 Repo reality execution posture (DOC\_DRIFT capture)**

Live QA must remain executable and evidence-producing even when canonical docs contain stale operational details (paths, filenames, script locations, or command shapes). If a canonical doc’s operational detail conflicts with repo reality, QA MUST:

* Use the repo-real invocation/paths to execute the checks and capture evidence.

* Record the mismatch as a CAVEAT: `DOC_DRIFT` (include the doc title and the mismatched detail) for later drain.

Do not block execution unless the mismatch prevents knowing what to run or how to verify.

Codespaces Live QA plans MUST include a Step-0 discovery snapshot and Doc Delta Capture step. The step MUST capture rails baseline and any required connectivity/prerequisite checks for the run environment. If no deltas are found, the step MUST record “no deltas” explicitly as produced output (not as a manual-fill placeholder).

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

---

### **15.4 Live QA step template (Deliverables-first)**

Use this structure for any QA plan or Live QA runbook step that includes executable commands. This template enforces §12.4.

Step \<N\> — \<short step title\>

Check ID: \<stable id for this step\>  
 PF refs: \<PF document title § anchor list\>  
 Tokens (names only): \<token list, if applicable\>

Command: \<single copy/paste-ready command string\>

Deliverables (paths only):

* \<fully qualified path 1\> — \<one-line description\>

* \<fully qualified path 2\> — \<one-line description\>

PASS criteria (file-based):

* \<what must be true in the Deliverables, stated in terms of existence/non-emptiness/simple checks\>

FAIL criteria (file-based):

* \<what would constitute failure, stated in terms of Deliverables and their content\>

Final status marker: `PENDING` → `PASS` | `FAIL` | `FAIL_TOOLING` (recorded in the primary step log)

### **15.5 OPS task record template (PO-only; IA-guided; not PR work)**

Use this record whenever a plan, remediation guide, or epic execution includes an OPS task (any step requiring privileged access outside the repo).

Task ID: \<stable ID\>  
 Owner: PO  
 Facilitator: IA  
 Target system/service (name only): \<no secrets\>  
 Intent / desired end state: \<what changes; what “done” looks like\>  
 Constraints / safety rails: \<what must remain true while executing\>  
 Success criteria: \<observable outcomes\>  
 Evidence to capture (minimum): exact commands actually run (verbatim) \+ stdout \+ stderr \+ exit code \+ produced artifacts \+ verification outputs for any integrity claims (for example, checksum validation output)  
 Evidence storage path (lowercase): `audit/ops/<epic-id>/...` or `audit/qa/<epic-id>/...`  
 Rollback intent: \<what “revert” means at a high level\>  
 Secret handling note: no plaintext secrets in docs or evidence (presence-only/redacted/hashed allowed)

Rules (normative):

* OPS tasks MUST be executed by the PO only; agents MUST NOT claim execution or completion.

* OPS tasks MUST NOT be represented as implementable PR work.

* Command transcript required — MUST. OPS evidence MUST include the exact commands run (verbatim) and their stdout/stderr and exit status, captured as repo-stored artifacts under the declared evidence storage path.

* No asserted verification — MUST. If the OPS record includes any “OK” integrity claim (for example, checksum verified), the proving command output line(s) MUST be captured as evidence and referenced by path.

* Evidence MUST be sufficient to verify the intended state and MUST be secret-free.

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

Use this subsection in any planning artifact (QA plans, remediation guides, implementation guides, EPIC records, runbooks). This is a traceability anchor only; it MUST NOT duplicate PF23 contents.

PF23 Anchors  
 Component(s) (from PF23):  
 Key pathnames/loci touched (from PF23):  
 Notes (optional): If PF23 appears stale or missing coverage, record as observation only; do not assign PF23 update tasks.

---

### **15.8 Evidence inventory reviewed \+ Observed Evidence Snapshot (non-PF portability)**

Use these blocks when a plan or guide reviewed non-PF inputs.

Evidence inventory reviewed (non-PF)  
 Label: provenance only; not required to execute

* \<name of non-PF input\> — \<why it was reviewed\>

* \<name of non-PF input\> — \<why it was reviewed\>

Observed Evidence Snapshot (non-PF)  
 Embed any non-PF fact required to execute downstream steps as a short quote or precise paraphrase. Do not require the executor to open external files to find the fact.

* Observation: \<exact string/status/shape\>

* Context: \<where it was observed\>

* Decision rule: \<how this observation changes actions\>

* Capture path (lowercase, includes filename): \<audit/qa/.../file.txt\>

Excerpt hygiene (normative):

* No terminal control sequences — MUST. If an observation includes terminal output or a log excerpt copied from a terminal, it MUST be plain text and free of terminal control sequences (ANSI escapes, OSC codes). Prefer capturing the underlying file bytes directly rather than copying terminal-rendered output.

* Verification outputs must be embedded — MUST. If a decision rule relies on a verification claim (for example, a checksum match or a schema validation pass), embed the exact command and the exact output line(s) that substantiate the claim, and capture that verification output under the declared capture path.

Artifact Map labeling rule (normative): If an Artifact Map (or equivalent) is included, it MUST explicitly label non-PF inputs as “provenance only; not required to execute” or it becomes an execution dependency (portability blocker).

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

Rules (normative):

* If a task edits any index/mirror file, the sibling `.path_proof.txt` update is part of the same task’s outputs and embedded verification.

* If a plan proposes a new file under governed surfaces, it MUST state whether the file is intended to appear in the indices/mirror; absence of that statement is a mechanical blocker.

* Remediation-only diagnostics/manifests MUST NOT be introduced under governed artifact surfaces unless explicitly framed as an ADR-worthy governance change; default is remediation audit paths (for example, `audit/qa/.../remediation/...`) and not indexed.

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


---

### **15.11 Remediation Task Plan template (DEV PRs \+ OPS tasks)**

Use this template for remediation task plans submitted for approval. It is distinct from the stepwise Remediation Implementation Guide format.

Approval gate scope (tight): Plan approval MUST focus on: correct task model (OPS vs DEV; DISCOVERY vs CHANGE; no mixed tasks), correct sequencing and explicit cross-lane dependencies, concrete deliverables (lowercase paths \+ filenames), and concrete verification success criteria (what “done” means). Detailed command lines and step-by-step failure handling are not required as approval blockers, but evidence posture remains non-negotiable.

Required sections (minimum):

1. Overview  
    Intent:  
    Constraints / safety rails:  
    Verification definition (what “done” means):

2. PF23 Anchors  
    (Use §15.7)

3. Tasks (only two types; enumerated)  
    DEV tasks — PRs only: `PR-01`, `PR-02`, …  
    OPS tasks — PO-run procedures only: `OPS-01`, `OPS-02`, …

Each task MUST include:

* Task ID: `PR-01` or `OPS-01`

* Task type: DEV or OPS

* Task intent: DISCOVERY or CHANGE

* Owner: Codex (for PR) or PO (for OPS)

* Inputs (concrete):

* Outputs / Deliverables (concrete lowercase file paths including filename; not directories):

* Embedded verification (must produce evidence at declared paths):

DEV task rule (normative): Each `PR-xx` task MUST embed a paste-ready Codex Prompt inside the task. A PR task missing its Codex Prompt is a mechanical blocker.

OPS task rule (normative): OPS tasks are PO-only execution. Exact command selection and failure-handling MAY be developed in flight during execution, but OPS execution MUST still capture and store, under a lowercase audit path with explicit filenames: (a) exact commands actually run (verbatim), (b) stdout/stderr \+ exit code (or equivalent output), (c) produced artifacts at the declared output paths, and (d) deviation notes explaining any change in command/flag. Evidence MUST be secret-free (presence-only/redacted/hashed allowed).

Cross-lane dependency line (locked; task-level): If a task depends on outputs from a prior task in the other lane, the dependent task MUST include exactly one dependency line in this exact form (omit if not needed):  
 Inputs needed from Task \<ID\> during implementation: \<exact items\>  
 Placeholders in this line are a mechanical blocker.

4. Evidence portability blocks (non-PF)  
    (Use §15.8 if any non-PF inputs were reviewed or any non-PF fact is required for execution.)

5. Governed index/mirror touchpoints (only if applicable)  
    If any task touches governed evidence indices/mirrors, include the exact filenames list and sibling path-proof rule (use §15.9) as task outputs and embedded verification checks.

6. /internal/version proof checklist (only if applicable)  
    If any task produces governed /internal/version evidence, include the explicit checklist (use §15.10) inside the relevant task’s embedded verification.

## **Appendix A — Full Document Assessment Protocol (Technical Writing)**

### **Policy (normative)**

Full-document requirement — MUST. Obtain and read the complete source before editing. If only a fragment is available, pause and request the full doc; proceed in partial mode only with explicit PO approval and label outputs as Partial.

**Heading numbering stability — MUST.** Existing H1/H2 numbering is immutable. New content SHOULD be added as H3/H4 within an existing H2 whenever possible. If a new H1/H2 is truly required, it MAY be added, but it MUST take the next available number and MUST NOT alter any existing numbering.

Practical guardrails (optional):

* Prefer H3/H4 for in-between additions (for example, add `### 12.4` under `## 12 …`) so you do not need new H2s.

* Never reuse an existing number for a different section.

* If you add a new H1/H2, update any structure map or cross-reference lists so they include the new number, but do not change old ones.

Titles-only cross-references — MUST. Use stable document titles only; do not include version numbers in cross-doc prose. Section names are allowed.

No duplicated bytes — MUST. Do not copy architecture, transport, headers, or schema bytes across docs; route by title to the single home.

Style and naming hygiene — SHOULD. Plain English; avoid em dashes; keep heading formatting consistent; always spell the brand as Glow; use RFC 2119 terms carefully.

Evidence discipline — MUST. Provide acceptance evidence and maintain parity between the human Evidence Index and the machine JSONL mirror in the same PR.

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

