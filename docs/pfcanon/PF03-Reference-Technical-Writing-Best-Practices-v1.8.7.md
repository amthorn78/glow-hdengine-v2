# **0\) Front Matter — Document Control**

**Title:** PF03-Reference-Technical-Writing-Best-Practices

**Version:** v1.8.7

**Status:** Reference

**Effective date:** 2026-08-25

**Last Update Gate:** BN 12.8.9

**Invocation tag:** INV-f2ac55d77ce9aacc

# **1\) Purpose & scope**

PF03 contains writing rules for AI agents that author, revise, review, or format PF documentation. Its purpose is to make PF text clear, concise, source-grounded, structurally precise, and paste-ready.

PF03 governs the writing portion of documentation work. It covers source use, terminology, claim posture, structure, placement, redline composition, cross-references, genre-specific presentation, security in examples, output boundaries, and editorial validation.

PF03 does not govern the underlying implementation, runtime behavior, repository operations, architecture, mathematics, transport, APIs, schemas, governed artifacts or paths, infrastructure, governance, gates, acceptance-token semantics, QA or OPS execution, planning procedures, runbook procedures, evidence maintenance, registry operations, or external state.

PF03 may govern how an AI writer describes or routes an excluded subject. It must not define, summarize, reproduce, reinterpret, or create a second canonical home for the subject itself.

An instruction to write about an action does not authorize the action. PF03 does not authorize an AI agent to apply, commit, push, merge, test, deploy, approve, accept, drain, register, or otherwise change external state.

# **2\) Roles & audience**

The primary audience is AI agents producing PF documentation.

The Product Owner, reviewers, subject-matter experts, developers, QA agents, OPS agents, and maintainers are readers and consumers of those outputs. PF03 does not assign their non-editorial responsibilities.

An AI writer must:

* identify the requested artifact and exact editable scope;  
* retrieve and read the complete required sources;  
* preserve supplied document identity and protected boundaries;  
* distinguish requirements, observed facts, plans, history, examples, routing, and unknowns;  
* retain still-valid material unless an authorized source supports changing it;  
* produce the complete requested output in the required form;  
* avoid unsupported claims and duplicated canon; and  
* report the smallest material blocker when truthful writing is impossible.

The Product Owner controls the requested scope, output contract, and authorized editorial changes. The Product Owner resolves a material source or editorial decision that the allowed sources cannot resolve.

A reviewer evaluates the text for source fidelity, completeness, placement, ownership, claim posture, clarity, and output compliance. Reviewing a draft does not establish that it was approved, applied, committed, pushed, tested, accepted, or drained.

# **3\) Governing editorial principles**

## **Truth and source fidelity**

Use the current supplied artifact and the current allowed sources. Do not substitute memory, a prior conversation, an earlier draft, a summary, a snippet, or a similarly named file for a required source.

Read every relied-on source completely. A cutoff, missing chunk, malformed table, unmatched fence, incomplete block, or passage ending mid-unit is a retrieval failure, not source content.

Do not write from an incomplete source view. Reopen or retrieve the source through an allowed complete route. If complete recovery is impossible and the missing content could materially change the output, state the smallest blocker.

Unknown stays unknown. Do not invent:

* titles, versions, dates, statuses, owners, approvals, or decisions;  
* paths, filenames, commands, flags, routes, endpoints, modules, or symbols;  
* schemas, fields, environment variables, artifacts, hashes, or tokens;  
* implementation, deployment, QA, OPS, registry, evidence, or board state; or  
* relationships, dependencies, supersession, acceptance, or completion.

Web research, a plan, an issue, a review comment, or a Build Notes statement does not replace the source that controls the text being authored.

## **Canonical ownership**

Keep one canonical home for each governed truth. Do not duplicate an externally owned rule, schema, token meaning, byte contract, path contract, process, or template merely to make PF03 or another document self-contained.

Route a reader to the current owning document by its exact in-document title. Do not include a version number in durable cross-document prose.

Add a section anchor only when the owning document establishes a stable, exact anchor and the reference materially improves retrieval.

Do not assign ownership from a filename, document number, filename resemblance, historical use, memory, or partial excerpt.

PF03 may state the writer-facing consequence of a routing decision. It must not provide a condensed substitute for the routed canon.

## **Claim-state separation**

Classify each material statement according to what it actually communicates:

* Current implementation.  
* Normative requirement.  
* Plan or proposal.  
* Historical statement.  
* Example or explanation.  
* Routing or ownership.  
* Unknown or blocked.

State current implementation only to the extent supported by direct current evidence.

Static repository inspection proves checked-in bytes only. It does not prove runtime success, deployment state, external-service state, secret validity, human approval, test execution, QA PASS, OPS completion, or acceptance.

A route declaration does not prove reachability. A test definition does not prove a passing test. A configuration file does not prove deployed configuration. A generated artifact does not prove how it was generated or validated.

When evidence supports only part of a statement, write only the supported portion as current. Keep the remaining requirement, proposal, historical fact, or unknown separate.

A requirement remains a requirement when implementation is missing or contradictory. Do not rewrite an unmet requirement as planned, proposed, deferred, or future work unless an authoritative source explicitly establishes that posture.

For a negative repository statement, identify the inspected snapshot and bounded search scope. State only that the item was not found within that scope. Failed or incomplete retrieval proves nothing.

Documentation drainage is not implementation proof. A documentation update, redline, Build Notes entry, plan, checklist, review, or closeout statement does not prove that code changed or that validation passed.

## **Structure and language**

Preserve supplied section numbers, titles, order, hierarchy, and boundaries unless the Product Owner explicitly authorizes a structural change.

Keep subordinate content within the section that owns it. Do not promote a nested heading, move a requirement, or create a second canonical home merely to improve visual balance.

Use one term consistently. Preserve exact casing and spelling for identifiers, source labels, technical literals, and authored titles.

When reviewing editorial conformance, accept clear, truthful, unambiguous wording that is semantically equivalent to the required meaning. A normative template does not make every example, placeholder, sentinel, punctuation choice, or wording pattern byte-exact unless controlling authority separately establishes an exact-literal or machine-readable requirement.

Distinguish optional editorial normalization from a material defect. Do not require revision solely for a harmless presentation difference. Identify the separate material consequence before treating a wording variance as required.

Put controlling rules before exceptions and examples. Use direct sentences and short paragraphs. Use bullets for discrete requirements, constraints, inputs, outputs, or failure cases. Use tables only when repeated fields or exact comparisons are clearer than prose.

Remove repetition that adds no meaning, but do not trade away qualifications, preconditions, scope boundaries, exceptions, failure behavior, or claim-state distinctions for brevity.

PF documents must not contain an ASCII three-period ellipsis or the Unicode ellipsis character. Use one of these explicit forms when omission is authorized:

* `[OMITTED]`  
* `[OMITTED: <short reason>]`  
* `[SNIP: <n> lines omitted]`  
* `[REPEAT BLOCK]`  
* `[LIST CONTINUES]`  
* `<PLACEHOLDER_NAME>`

An omission marker must not conceal text required to establish authority, meaning, placement, or proof. Retrieve the complete text when the omitted material is relied upon.

If an exact literal cannot be reproduced without violating the prohibition, reference the authoritative supplied source by its exact locator. If no authoritative source exists, report the missing source instead of inventing the literal.

For code-like literals in narrative prose, use inline code, double quotation marks, or a `CODE:` prefix when that presentation preserves the exact content.

# **4\) AI-agent authoring boundary and method**

An AI writing task is bounded by the requested artifact, editable scope, source set, output contract, and permitted writes.

Use this authoring method:

1. Identify the requested document type, exact target, editable scope, and required output.  
2. Resolve the current target uniquely and read it completely.  
3. Retrieve and read every source required to establish the requested content.  
4. Build an internal map of the target structure, source obligations, canonical ownership, claim states, and unresolved conflicts.  
5. When current repository reality will be stated, use one identified repository snapshot consistently for every repository-dependent claim.  
6. Verify technical literals and current-state statements before drafting them.  
7. Draft only within the authorized scope while retaining still-valid content and protected boundaries.  
8. Review the complete draft for unsupported claims, omitted obligations, duplicated canon, misplaced content, structural drift, and output leakage.  
9. Return exactly the requested artifact or response form.

Search an exact known literal before using a broader conceptual search. Read enough surrounding source content to establish the meaning of every positive or contradictory claim.

When a challenged literal is absent after the required exact verification, state `No occurrence verified`. Do not invent an explanation for its origin, and do not agree that it appeared unless its exact occurrence has been verified.

When wording depends on absence, inspect the expected locus and perform a materially different bounded search when one is available. Do not convert a failed search or failed retrieval into an absence claim.

A writing request does not authorize an AI agent to start services, execute tests, install dependencies, inspect deployment state, mutate a repository, update governed records, or change external state. If another instruction separately authorizes such work, PF03 governs only the resulting documentation.

Do not promise background work, future completion, or a later response. Produce the complete authorized writing output in the current response or state the smallest material blocker.

# **5\) Canonical ownership and cross-document routing**

Resolve ownership before writing a governed statement.

1. Retrieve the candidate owning source completely.  
2. Confirm its exact in-document title.  
3. Read its scope and the complete content relied upon.  
4. Determine whether that content actually establishes ownership of the point.  
5. Route the reader by exact title without reproducing the owned contract.

A routing sentence should communicate only what the writer or reader must consult. It must not restate the routed document’s substantive rules, fields, paths, procedures, or controlled values.

Do not create a convenience summary of:

* architecture or mathematical rules;  
* API or transport contracts;  
* schemas, canonical bytes, or artifact paths;  
* governance gates or token semantics;  
* QA, OPS, evidence, registry, or closeout procedures; or  
* plan, runbook, remediation, or execution templates.

A filename is not proof of a document’s title, currency, scope, or authority.

When ownership is absent, ambiguous, or conflicting, do not assign a home by inference. Keep the point unknown and request the smallest source or decision needed to resolve it.

# **6\) Source precedence in documentation**

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

# **7\) Revision and retention rules**

Use the output form requested by the Product Owner.

| Output form | Editable scope | Required completeness |
| ----- | ----- | ----- |
| Full-document rewrite | The complete supplied target | Return the complete revised document. Do not silently omit still-valid sections. |
| Section or range rewrite | The exact selected section or contiguous range | Return only the requested selection when the output contract requires selection-only text. Preserve the selection’s full established scope. |
| Redline | Only the changes described by independently executable redlines | Supply exact placement and complete paste text under §8. |
| Review or assessment | No source bytes are editable unless revision is also requested | Report findings and source-grounded recommendations without implying application. |

Within the authorized scope:

* retain every still-valid requirement, qualification, example, and boundary needed for meaning;  
* remove content only when it is stale, unsupported, contradictory, duplicative, out of scope, or moved to a proven canonical home;  
* do not narrow a section silently;  
* do not omit material merely because the current source guide does not mention it;  
* do not introduce a new requirement merely because it would improve consistency;  
* keep each requirement in the section that owns it;  
* preserve source-established relationships among sections; and  
* make the smallest structural change that fully resolves the authorized problem.

If a source is an audit, findings register, or review, account for every applicable finding. Map it to a resulting change, supported no-change disposition, implementation gap, or blocking decision. Do not silently drop findings.

Formatting repair may correct copied-chat damage, escaping, wrappers, indentation, line wrapping, or malformed Markdown when the complete source establishes the intended text. Do not use formatting repair to change meaning, authority, scope, placement, identity, or claim posture.

Do not change a supplied title, version, status, effective date, gate, invocation identifier, or other document-control value unless the Product Owner or a governing source explicitly authorizes the change.

Do not add an instruction to update a registry, evidence surface, board, repository, or external record unless the requested artifact calls for that instruction and an allowed current source establishes the exact target.

# **8\) Redlines and placement rules**

When the operator supplies a redline format, follow it exactly. Otherwise use the requirements in this section.

## **Required editorial fields**

Every redline must include:

* a redline number;  
* each mapped finding, source item, or exact source anchor;  
* a change type and one operation: `INSERT`, `REPLACE`, or `DELETE`;  
* the target document’s exact in-document title;  
* exact target-document evidence establishing the current text or placement;  
* the controlling source basis;  
* a concise source-grounded rationale;  
* the complete authored Markdown heading path from the outermost heading through the target;  
* one direct action against the complete original target;  
* exact original-target boundaries and uniqueness counts; and  
* complete inserted or replacement text when applicable.

Include governance, acceptance, evidence, QA, or OPS fields only when the requested redline contract requires them. Reproduce exact source-defined names without interpreting or extending their meaning.

## **Operations and boundaries**

| Operation | Required original boundaries | Paste text |
| ----- | ----- | ----- |
| `INSERT` | The complete line immediately before and immediately after the insertion gap. Both remain unchanged. | Only the text inserted between the boundaries. |
| `REPLACE` | The complete first and last lines of the original inclusive range. | The complete replacement range, including unchanged content captured by widened boundaries. |
| `DELETE` | The complete first and last lines of the original inclusive range. | None. |

A one-line replacement or deletion may use the same complete line as both boundaries.

Every heading path and required boundary must match exactly once within its stated scope. Do not use a vague locator, an unexplained occurrence number, or a repeated heading by itself.

If a path or boundary is not unique, widen it to the smallest range with unique first and last lines inside one unique scope. If widening captures unchanged material, use `REPLACE` and reproduce that material in the paste text.

Each redline must execute independently against the complete original target. Redline ranges must not overlap. Consolidate overlapping edits and multiple edits to the same insertion gap.

Do not emit a redline when unique placement cannot be established.

For a contiguous replacement, emit the complete revised range in source order. Preserve all still-valid material within the range. Remove, consolidate, or redistribute content only when an allowed source or explicit instruction supports the change.

## **Structure and presentation**

Preserve protected heading numbers, titles, order, hierarchy, and section boundaries unless the requested change explicitly authorizes otherwise.

Do not wrap headings in outer bold. Place one blank line after each heading. Do not use code fences around paste text unless the Product Owner explicitly requests them.

Judge placement anchors and quoted target text against raw source bytes or the actual supplied target. Display-layer escaping does not establish a source defect.

Do not create a cleanup redline solely for a rendered escape, wrapper, line-wrap difference, or illustrative syntax issue. A redline is warranted when the source-real defect changes meaning, placement, authority, scope, identity, safety, or claim posture.

Illustrative commands, snippets, helper code, shell lines, and examples must be labeled as examples when they are not authoritative invocation contracts.

# **9\) Writing PF10-HDE-Build-Notes content**

## **Source selection and citation**

Resolve and retrieve the complete latest active PF10 base version before relying on an addendum. Use its complete unlettered document or its complete lettered document set in established order. Do not read, reuse, compare, reconcile, or carry forward content from an older base version.

For a lettered set, verify the continuous addendum sequence across every member before treating the set as complete.

Treat an addendum as relevant only to the topic its complete text explicitly addresses.

Search every document in the complete active PF10 version for all addenda relevant to the current topic. Determine each addendum’s actual scope from its complete heading and substantive content. When addendum scopes overlap, apply only the highest-numbered applicable addendum to the overlapping scope. Continue applying lower-numbered addenda only to distinct scope not superseded by the higher-numbered addendum.

Reference an addendum by its exact addendum number and title. Do not use a document version or document letter as the durable external anchor.

If supplied Build Notes content differs from the repository copy, state the source split when it affects the authored conclusion. Do not describe supplied-only text as repository-drained canon.

Preserve published addendum identities. If a historical heading is inaccurate, clarify the corrected identity in later prose when supported. Do not silently rewrite the historical heading.

## **Claim posture**

Build Notes records do not by themselves prove implementation, runtime behavior, QA PASS, OPS completion, approval, acceptance, or permanent drainage.

When those distinctions matter, state whether a point is:

* recorded in Build Notes;  
* supported by separate current evidence;  
* temporary guidance;  
* proposed for drainage;  
* already drained by an authoritative source;  
* historical; or  
* unresolved.

Do not collapse those states.

When writing temporary staging, include only source-supported information about its identity, purpose, decision, intended canonical destination, supersession or conflict, and implementation effect.

When writing about documentation-only staging, distinguish documentation posture from code, token, evidence, schema, QA, or OPS effects. Do not infer an effect that the source does not establish.

## **Output**

Follow the complete current Build Notes structure required by the target. PF03 does not define an addendum schema.

Inside PF10 body text, cite another PF by its exact in-document title and section only, never by filename or version. Do not restate the cited PF’s content in PF10.

Produce only the requested paste-ready addition or revision.

Do not invent or normalize an addendum identifier, title, timestamp, status, source, dependency, token, destination, or supersession claim.

Do not claim that drafted Build Notes text was pasted, merged, drained, archived, approved, or accepted.

# **10\) Writing about registries and governed records**

PF03 does not establish a registry, index, mirror, manifest, evidence surface, board, or other governed record.

Name one of those surfaces only when an allowed current source establishes its exact identity. Include a path, filename, field, or schema detail only when the writing task requires it and the owning source proves it.

Use these claim boundaries:

| Claim | Required writing basis |
| ----- | ----- |
| A governed record exists at a stated path | Direct current evidence for that exact path and record |
| A governed record must be updated | An applicable current owning requirement |
| A governed record was updated | Direct evidence of the completed update |
| A record was not found | A stated repository snapshot, inspected scope, and bounded search |
| The record’s state is unknown | Missing, failed, incomplete, ambiguous, or conflicting evidence |

Do not convert a document heading, example filename, historical mention, planned artifact, or requested future action into a claim that a governed record currently exists.

Do not define or summarize an externally owned schema, serialization format, update workflow, synchronization rule, checksum rule, or path contract.

When a requested document must instruct a future update, identify only the exact source-supported target and required writing. Do not claim that the update was performed.

When a record is cited as evidence, state what the record itself proves. Its presence does not automatically prove implementation, validation, acceptance, or runtime state.

# **11\) Writing about evidence, validation, approval, and completion**

## **Editorial validation**

PF03 may define validation of the written output itself.

Before delivering a draft, verify:

* the complete required sources were retrieved;  
* the target and editable scope were resolved exactly;  
* protected headings and boundaries were preserved;  
* every applicable source obligation was addressed;  
* still-valid content was retained;  
* externally owned canon was routed rather than duplicated;  
* technical literals and current-state claims have supported wording;  
* plans, requirements, history, examples, and observed facts remain distinct;  
* no unsupported completion or approval claim appears; and  
* the output contains only the material allowed by the response contract.

For redlines, also verify:

* complete authored heading paths;  
* exact target boundaries;  
* required uniqueness counts;  
* independent executability;  
* non-overlapping ranges; and  
* complete paste text.

These checks establish only the editorial condition of the draft. They do not establish an external acceptance state.

## **State language**

Use a state statement only when the corresponding evidence directly supports it.

| Statement | Minimum basis for writing it | It does not by itself prove |
| ----- | ----- | ----- |
| The draft satisfies its output contract | Completed editorial validation against the stated output contract | Product Owner approval or application |
| The draft is ready for review | The requested writing is complete and no known material authoring blocker remains | Approval, acceptance, or repository change |
| The draft was approved | Direct current approval evidence | Application, commit, push, merge, QA, or OPS completion |
| The text was applied | Direct observation of the updated target bytes | Commit, push, merge, validation, or acceptance |
| The change was committed, pushed, or merged | Direct repository evidence for the specific event | Test success, QA PASS, deployment, or acceptance |
| Validation or QA passed | Direct observed result from the applicable execution | Deployment, OPS completion, or broader acceptance |

Do not use “complete,” “accepted,” “landed,” “drained,” “closed,” “passed,” or similar language as shorthand for a different state.

Separate validation that was executed and observed from validation that is required, recommended, unavailable, or not run.

A static file, search result, configuration, test definition, expected command, checklist statement, or evidence reference does not prove execution or PASS.

## **Acceptance-token language**

PF03 contains no acceptance-token roster and defines no token semantics.

When the requested writing requires a token, retrieve the current token-owning source and verify the token’s exact name and meaning. Do not rename, alias, extend, infer, or curate the token in PF03.

When no verified token expresses a documentation condition, state the condition in plain language. Do not create uppercase token-like text.

# **12\) Communication and document-genre rules**

## **Output contract**

Follow the requested response contract exactly.

If the request requires only a file or direct link, do not add a change summary, evidence report, integration instruction, or second narrative output.

If the request requires inline text, provide the complete text without a file-only response.

If the request requires only one section or range, do not include document-level material or surrounding sections.

For advisory and review responses, lead with the outcome. Include only the source-grounded detail needed to understand or act on it.

Ask a question only when the missing answer would materially change the result. Ask for the smallest missing source or decision. Do not ask the Product Owner to restate information that the allowed sources can resolve.

Report retrieval, permission, or tool failures plainly. Do not present a tooling failure as a source defect or substantive finding.

## **Claim language**

Use direct, testable sentences.

Use `MUST`, `SHOULD`, and `MAY` only when stating normative requirements. Do not use them merely for emphasis.

Identify whether a statement is observed, required, proposed, historical, explanatory, routed, or unknown whenever the distinction could affect interpretation.

Never imply approval, mutation, runtime behavior, QA PASS, OPS completion, acceptance, commit, push, merge, or drainage without direct supporting evidence.

Do not use future tense to weaken a current requirement. Use planned, proposed, optional, deferred, or future language only when an authoritative source establishes that posture.

## **Syntax normalization**

An AI writer may repair quoting, escaping, Markdown wrappers, indentation, line wrapping, copied-chat damage, or illustrative syntax when the correction preserves the original objective, meaning, scope, identity, source authority, and technical content.

Do not use syntax normalization to invent:

* a command, path, route, endpoint, helper, or artifact;  
* a token, field, schema, acceptance predicate, or evidence surface;  
* an authorization, owner, status, phase, or dependency; or  
* a PASS, FAIL, readiness, or completion claim.

Formatting alone is not a substantive blocker when it can be repaired faithfully. Block only when the defect prevents recovery of the intended text or materially changes meaning, authority, scope, safety, identity, placement, or executable intent.

## **Task, plan, and execution-document writing**

When asked to write an execution-oriented document, use objective-first directives.

State:

* the exact objective;  
* the authorized scope;  
* the required output or observable result;  
* the governing constraints;  
* the known inputs;  
* the relevant failure or blocked posture; and  
* the distinction between an action, its evidence, and its interpretation.

Use exact source-established commands, paths, routes, modules, flags, and identifiers. Label an example as an example. Do not turn illustrative text into an asserted canonical invocation.

PF03 governs the clarity and truthfulness of plans, runbooks, remediation documents, and execution instructions. It does not define their domain templates, workflow, acceptance criteria, or operational authority.

## **Reports and retrospectives**

Identify the primary source that controls the report’s live subject. State the limited role of any plan, guide, or historical source used only for framing.

Use only source-supported task, epic, pass, phase, artifact, and outcome identities. If an input label conflicts with the controlling source, state the mismatch rather than silently normalizing it.

When the operator explicitly asks whether a PF09 row can be closed, answer `Yes` or `No` before explaining the evidence.

If later inspection disproves a finding, state that the earlier conclusion was wrong, identify the analytical or evidentiary failure, and withdraw every downstream PR, OPS, documentation, or plan task based solely on that finding. Do not preserve the task merely because it has already appeared in a plan.

Keep these categories separate:

* implementation evidence;  
* validation or QA evidence;  
* OPS evidence;  
* approval or acceptance evidence;  
* closeout evidence;  
* historical context; and  
* unresolved evidence gaps.

A framing source does not prove execution. An artifact-only fact does not automatically establish permanent canon or Build Notes history.

When repository-observable facts are available through allowed current evidence, inspect them directly. Do not manufacture a report-only remediation or require operator capture merely because no persistent report destination exists. If no actionable code, canon, governed-artifact, status, or other persistent defect remains, state that conclusion rather than inventing a documentation task.

State accepted deviations, evidence limitations, unresolved gaps, and later documentation work separately from a verdict or closure claim.

When evidence is missing, state what is missing and why it matters. Name an expected source or locus only when an allowed current source establishes it.

## **Runnable guides and usage documentation**

A runnable guide is not a canonical home for the contracts it uses.

Route governed details to their owning documents. Do not redefine schemas, tokens, paths, policies, or acceptance rules in workflow prose.

Before describing a command, route, workflow, payload, or operational surface as available or runnable, verify that claim against current allowed evidence.

Label planned, intended, blocked, diagnostic, restricted, legacy, or gap-recording material at the point of use.

When an example could imply public availability, production readiness, external authorization, full conformance, QA PASS, OPS completion, or closure, state the supported limitation explicitly.

Keep an observed diagnostic or error path separate from a source-supported success path. Do not promote a gap, fallback, or legacy surface into the canonical workflow.

# **13\) Security and privacy in documentation**

Do not place secrets, credentials, cookies, bearer tokens, API keys, private keys, unredacted environment values, private payloads, or unnecessary personal data in documentation, redlines, examples, templates, logs, or evidence summaries.

Use obvious placeholders for secret values.

Preserve an exact environment-key, header, field, or credential type only when a current source establishes the name and the writing requires it. Never infer or reconstruct the secret value.

Use synthetic, minimal examples. Do not copy production identifiers, private records, complete request or response bodies, or logs containing sensitive values merely to make an example concrete.

When redaction would remove information required to establish a claim, do not invent a replacement. Reference the authorized source or state that the available redacted material cannot prove the point.

Include only the minimum evidence locator needed for the writing purpose. Do not reproduce externally governed evidence schemas, canonical JSON, mirrors, manifests, checksums, or path-proof contracts.

Do not imply that an external system, repository, service, credential, environment, or private record was accessed or changed unless the authorized action occurred and its result was directly observed.

# **14\) AI-agent final editorial check**

Before delivering PF documentation, confirm:

* The output matches the requested artifact type and exact editable scope.  
* Every required source was retrieved completely.  
* The current target and relied-on owning sources were resolved uniquely.  
* Every retained factual or normative statement is supported by an allowed source.  
* Current implementation, requirements, plans, history, examples, routing, and unknowns remain distinct.  
* Every technical literal preserves its exact supported spelling and casing.  
* Externally owned canon is routed by title rather than duplicated.  
* Protected headings, numbering, order, hierarchy, and section boundaries are preserved unless change was authorized.  
* No still-valid requirement, qualification, example, or mapped finding was silently omitted.  
* Redlines, when requested, have unique placement, non-overlapping ranges, and complete paste text.  
* Formatting is valid, paste-ready Markdown with no empty bullets or outer bold heading wrappers.  
* Authorized omission markers are used instead of prohibited ellipsis forms.  
* Examples contain no secrets, private values, or unsupported production identifiers.  
* No external action, approval, validation, QA, OPS, repository, registry, evidence, or acceptance state is overstated.  
* The response contains no preface, appendix, report, or surrounding material prohibited by the output contract.

If a material source, boundary, authority, or decision remains unresolved, do not conceal the uncertainty inside the draft. State the smallest blocker that prevents truthful completion.

# **15\) PF03-owned editorial templates**

PF03 contains only editorial templates for documentation forms it governs.

When the operator supplies a stricter or different output format, use the supplied format instead.

PF03 does not supply plan, runbook, remediation, QA, OPS, evidence, registry, audit, closeout, or retrospective templates.

## **15.1 Document-control transcription pattern**

This pattern is a transcription aid. It does not establish which document-control fields a target must contain or what their values mean.

Use only the fields and order established by the target document or requested output.

* Title: `<exact supplied in-document title>`  
* Version: `<exact authorized version>`  
* Status: `<exact authorized status>`  
* Effective date: `<exact authorized date>`  
* Last Update Gate: `<exact authorized gate or decision identifier>`  
* Invocation tag: `<exact authorized invocation tag>`  
* Provenance: `<exact source-supported provenance when required>`

Do not invent, infer, normalize, or increment a document-control value.

For a full-document rewrite, preserve the supplied values unless the Product Owner or a governing source explicitly authorizes their revision.

## **15.2 Redline block**

* Redline number: `<N>`  
* Findings or source items: `<exact IDs, titles, or source anchors>`  
* Change type: `<source-supported editorial classification>`  
* Operation: `<INSERT | REPLACE | DELETE>`  
* Target document: `<exact in-document title>`  
* Target-document evidence: `<verbatim original target text>`  
* Controlling basis: `<exact current source title and stable anchor when available>`  
* Rationale: `<one concise source-grounded statement>`  
* Section path: `"<outer authored heading>" > "<target authored heading>"`  
* Action: `<INSERT | REPLACE | DELETE> ONCE <complete action wording>`  
* Uniqueness: `section-path matches=1 | each required boundary matches within scope=1`  
* First boundary: `<complete original-target line>`  
* Last boundary: `<complete original-target line>`  
* Paste text: `<inserted text or complete replacement range; omit for DELETE>`  
* Source-required external fields: `<include only when the requested contract requires them>`

Each redline must execute independently against the complete original target.

Do not use a vague locator, an unexplained occurrence number, an overlapping range, reconstructed text when raw source is available, or a boundary that cannot be proved unique.

