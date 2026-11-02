# Redlines — PF19-Canon-Glow-QA-Guide v3.0.7 — gtwpe-20261101-pf10-v14-0-5 (T-06)

## Package identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` task T-06, preparation revision 3 (supersedes revisions 1 and 2, see the proof log §11) |
| Target (original baseline) | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.7.md`, in-document title PF19-Canon-Glow-QA-Guide, v3.0.7, read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`, unchanged at `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`; git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b`; SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; 682,678 bytes; 5,622 lines |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; selected units 2.8 (lines 1063–1106, 1111–1127), 2.15 (lines 1650–1804), 2.2 (lines 517–551) and 2.16 (lines 1869–1939) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, the handoff's identity `142feb35144d8795f927e0c78b665ace52279064`, re-read at `31c91e586b30a82ba1651e0d8a8970d7da35de13` (T-06 selections unchanged); task T-06; rows C-17, C-18, C-26 (assigned), C-07, C-29 (uncertain, now drained), C-20, C-30 (supporting) |
| Product Owner direction | Nathan, 2026-11-02, in this session: “fixed the defects and inconsistencies you noticed. And PF10 addenda should be referenced in any case” |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, run in the Claude Code session Nathan started for T-06 on 2026-11-02 |
| Preparation outcome | `READY` |
| Proof log | `PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, in this directory |

## Literal conventions

* Every payload is fenced with `~~~~~~`. The literal is every byte between the line after the opening fence and the line before the closing fence, lines joined by LF, with no trailing LF. The fence lines and the labels around them are not part of the literal.
* Every old block is one or more complete, contiguous baseline lines without the final terminating LF. Each old block occurs exactly once in the whole original baseline (expected and observed count 1). Where a single line repeats in the baseline, the old block is widened upward with the preceding lines until it is unique, and the replacement reproduces those lines unchanged.
* Each replacement replaces only its old block. The baseline LF that follows the old block stays in place.
* All 52 redlines resolve independently against the unchanged original. Their line spans do not overlap and no redline's output is another's locator.
* Trailing spaces are literal. Several old blocks and replacements end lines with two U+0020 spaces, as the baseline does.

## Document-control fields for TW-APPLY-10

No redline in this package touches the header (§0.1, baseline lines 3–10). TW-APPLY-10 derives the document-control fields under its header contract. The baseline header schema and values are:

~~~~~~
**Title:** PF19-Canon-Glow-QA-Guide  
**Status:** Canon  
**Version:** v3.0.7  
**Effective date:** 2026-10-26  
**Last Update Gate:** BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md  
**Invocation tag:** INV-f2ac55d77ce9aacc
~~~~~~

Sources that justify this update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (PF10-HDE-Build-Notes, v14.0.5). The defect and consistency redlines rest on the Product Owner's direction of 2026-11-02 and on PF19's own text, not on a further source file. PF19 keeps no change log or revision-history section, so no history entry is prepared.

## Redlines

### RL-01

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-07 (2.2 R-1, R-2)
* Heading path (literal baseline heading lines, outermost first): `# **0\. Front Matter**` > `## **0.4 Principles & Single Homes (routing only)**` > `### **0.4.3 Core principles (names-only).**`
* Location: §0.4.3, the paragraph beginning “Change-process artifacts, including QA readiness” (baseline line 138)
* Old block: baseline line 138
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Change-process artifacts, including QA readiness, audit, triage, Guide, Plan, task, review, final Report, separate RCA and remediation work products, are stored in `docs/ephemeral/` and referenced by repository path. A document whose class is uncertain is stored there too. Scratch is transient preparation space. ChatGPT Library and Google Drive are neither destinations nor authorities for these documents; a specific Product Owner-directed Drive file remains non-authoritative. Notion may carry concise status and usable links, not a second artifact body; prompt bodies retain their single home in Notion. Repository-controlled code, tests, configuration and governed mechanical evidence remain at their established repository paths and writers. Existing historical artifacts and their provenance are not migrated automatically. Product Owner publication of PF10, PF23 or historical change records remains separately authorized administration.
~~~~~~

Replacement:

~~~~~~
Change-process artifacts, including QA readiness, audit, triage, Guide, Plan, task, review, final Report, separate RCA and remediation work products, are stored in `docs/ephemeral/` and referenced by repository path. A document whose class is uncertain is stored there too. Scratch is transient preparation space. ChatGPT Library and Google Drive are neither destinations nor authorities for these documents; a specific Product Owner-directed Drive file remains non-authoritative. Notion may carry concise status and usable links, not a second artifact body; prompt bodies retain their single home in Notion. Repository-controlled code, tests, configuration and governed mechanical evidence remain at their established repository paths and writers. Existing historical artifacts and their provenance are not migrated automatically. Product Owner publication of PF10, PF23 or historical change records remains separately authorized administration.

Planning documents serve planning only (HDE Build Notes). A planning document is any change-process work product stored under `docs/ephemeral/`, including the artifacts listed above. No code, test, tool, CI step, workflow, schema, QA harness, governed evidence artifact, step-logs manifest, close pack, manifest, Index or Mirror row or path proof reads, binds, hashes, resolves or requires a path under `docs/ephemeral/`; a test builds any document it needs as its own fixture. A fact a later stage needs from a planning document is recorded where that stage reads it, when it is recorded. A prose citation of a planning document in a permanent record is a reference only, so archiving or deleting the cited document invalidates nothing that depends on the record.

PF-Canon is resolved by stable identity, never by version (HDE Build Notes). PF document versions, and so file names, may change at any time. No code, test, tool, CI step, schema, QA harness, governed artifact or committed record that must remain valid pins a PF document's file name, version or content digest, or requires its bytes to stay unchanged. A tool that needs current canon resolves the one current file under `docs/pfcanon/` when it runs, by PF identity and versionless title, and refuses when that resolution is not unique; validating an already committed artifact does not re-read canon. A citation of canon names the PF document by title, and its section where needed, and names HDE Build Notes by title alone. Recording the PF versions actually used, as §10.8 requires, is attribution, and nothing depends on those versions staying current.
~~~~~~

### RL-02

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: export-damaged link with a lost placeholder
* Heading path (literal baseline heading lines, outermost first): `# **1\. Environments & surfaces map (names-only)**` > `## **1.4 Shared tools and evidence system**`
* Location: §1.4, Infra/ops ownership, the base-URL sub-bullet (baseline line 221)
* Old block: baseline line 221
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
      * a corresponding base URL and port per environment (for example Codespaces vs local dev), from which concrete URLs such as DEV\_SAMPLER\_URL=[http://127.0.0.1](http://127.0.0.1/):\\/internal/dev/sampler can be derived.  
~~~~~~

Replacement:

~~~~~~
      * a corresponding base URL and port per environment (for example Codespaces vs local dev), from which concrete URLs such as `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` (§14.5.1) can be derived.  
~~~~~~

### RL-03

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-07 (2.2 R-3, second bullet; the first bullet is held with CCR-5, H-06)
* Heading path (literal baseline heading lines, outermost first): `# **2\. Pre-commit QA (local/CI)**` > `## **2.2 Checklist (to be instantiated in PF09 CI)**` > `### **2.2.11 Evidence-governed CI sequence (names-only)**`
* Location: §2.2.11, sub-bullet beginning “Release and security, QA and audit, and closeout validation are distinct lanes.” (baseline line 406)
* Old block: baseline line 406
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
  * Release and security, QA and audit, and closeout validation are distinct lanes. Evidence generation, audit work, or closeout work MUST NOT substitute for ordinary required PR CI or become required PR CI solely because it was required during one epic.  
~~~~~~

Replacement:

~~~~~~
  * Release and security, QA and audit, and closeout validation are distinct lanes. Evidence generation, audit work, or closeout work MUST NOT substitute for ordinary required PR CI or become required PR CI solely because it was required during one epic.  
  * The close-pack writer's test is a close-stage test (HDE Build Notes). CI selects it when the writer, a close-candidate source schema, the closeout validation workflow or the test itself changes; it is not part of full validation or of any other ordinary required pull-request CI (Plan Templates, “CI lane classification and automated budget-control discipline”).  
~~~~~~

### RL-04

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-29 (2.16 R-1, R-2); support C-30
* Heading path (literal baseline heading lines, outermost first): `# **2\. Pre-commit QA (local/CI)**` > `## **2.2 Checklist (to be instantiated in PF09 CI)**` > `### **2.2.12 Engine serializer/composer determinism**`
* Location: §2.2.12, its only paragraph (baseline line 418)
* Old block: baseline line 418
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Prove two-run identity and AB↔BA parity (where defined) for Engine serializer/composer behavior. Ban RNG/time/FS/network in pure paths; governed outputs follow canonical JSON rules. Tokens live in PF04/PF09; bytes in PF14/PF12.
~~~~~~

Replacement:

~~~~~~
Prove two-run identity and AB↔BA parity (where defined) for Engine serializer/composer behavior. Ban RNG/time/FS/network in pure paths; governed outputs follow canonical JSON rules. Tokens live in PF04/PF09; bytes in PF14/PF12.

For compat, GATE:CORE-DET evidence is the real compat path (HDE Build Notes), in two parts:

* Closed rails: the CI owner tests that exercise the real compat path, run as CI selects them: `tests/core/test_engine_core_abba.py`, `tests/core/test_engine_core_determinism.py`, `tests/compat/test_evaluate_pair_eligibility.py`, `tests/compat/test_compat_public_ab_ba_identity.py` and `tests/cli/test_showcompat_parity_and_identity.py`. A change that removes or weakens one of them needs its owner's review, like any other gate test.
* Open rails: each run of the live compat test (§3.5.5), which is Ops evidence.

The Reader goldens remain evidence for canonical emission and the Reader covenant; they are not evidence of compat AB↔BA. These entries are retired from GATE:CORE-DET evidence, and no QA record may cite them as current proof: `scripts/make_compat_determinism_artifacts.py`; `artifacts/cards/A3/IDENTITY_OK.txt`; `ci/jobs/preimage_recompute_and_compare.yml`, `ci/jobs/ab_ba_parity_bytecompare.yml` and `ci/jobs/two_run_identity_bytecompare.yml`; and `fixtures/composite/abba/*.json`, `audit/gates/determinism/abba_compare.log`, `fixtures/composite/integration_abba/*.json` and `audit/gates/determinism/abba_compare_integration.log`. The gate's pass conditions and evidence lists remain with HDE Governance.
~~~~~~

### RL-05

* Operation: `REPLACE`
* Change type: CONSISTENCY
* Source rows: C-26 (R-1, R-2 context)
* Heading path (literal baseline heading lines, outermost first): `# **2\. Pre-commit QA (local/CI)**` > `## **2.3 Rails & environment posture — PO/epic mandated rails**`
* Location: §2.3, first paragraph, beginning “Every EPIC’s PO specifies what rails posture” (baseline line 436)
* Old block: baseline line 436
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Every EPIC’s PO specifies what rails posture must be used to accept the epic (open rails vs closed rails). This posture is non-negotiable: it informs which tests must be run and how results are interpreted.
~~~~~~

Replacement:

~~~~~~
Every EPIC’s PO specifies what rails posture must be used to accept the epic (open rails vs closed rails). This posture is non-negotiable: it informs which tests must be run and how results are interpreted. For an Epic, that posture always includes the open-rails live compat test of §3.5.5, unless the Product Owner records a waiver of it (§3.1.2).
~~~~~~

### RL-06

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-2, QA-10 question)
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.1 Intent**` > `### **3.1.1 Integrated implementation audit and readiness**`
* Location: §3.1.1, the paragraph after the assessment-state table, beginning “QA-10 is the readiness decision and remediation return point.” (baseline line 503)
* Old block: baseline line 503
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
QA-10 is the readiness decision and remediation return point. There is no separate mandatory QA-15 stage, and neither Guide authoring nor QA Plan authoring acquires another readiness gate. PF23/PF10 publication of informational proposals is manual Product Owner work and does not gate progression. Actual scope and approval decisions still apply.
~~~~~~

Replacement:

~~~~~~
QA-10 is the readiness decision and remediation return point. There is no separate mandatory QA-15 stage, and neither Guide authoring nor QA Plan authoring acquires another readiness gate. PF23/PF10 publication of informational proposals is manual Product Owner work and does not gate progression. Actual scope and approval decisions still apply. For an Epic, a finding that the Epic's surfaces are not on a live path, or that the live compat test of §3.5.5 cannot run meaningfully, is put to the Product Owner as a named decision no later than QA-10's readiness decision. Such a finding is a question, not a waiver, and the QA Plan is not approval-ready until the Product Owner answers it (§3.1.2).
~~~~~~

### RL-07

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-4, R-3, R-2 waiver form); support C-30; HDE Build Notes source reference
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.1 Intent**` > `### **3.1.2 Independent QA, reporting and closure**`
* Location: §3.1.2, the third and last paragraph, beginning “Ops remains implementation work:” (baseline line 511)
* Old block: baseline line 511
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Ops remains implementation work: IA prepares and reviews through its responsible chain; the authorized operator executes. Kronos may consume Ops evidence for QA but does not acquire Ops approval authority. Specification, Plan, PR Proceed, execution, PR acceptance and closure retain their actual owners. A Product Owner's PR Proceed is the approval for its exact detailed work unit; do not add another binder approval for the same unchanged design.
~~~~~~

Replacement:

~~~~~~
Ops remains implementation work: IA prepares and reviews through its responsible chain; the authorized operator executes. Kronos may consume Ops evidence for QA but does not acquire Ops approval authority. Specification, Plan, PR Proceed, execution, PR acceptance and closure retain their actual owners. A Product Owner's PR Proceed is the approval for its exact detailed work unit; do not add another binder approval for the same unchanged design.

Live test line (normative; Epics). For an Epic, each of these records carries a line `Live test:` with exactly one value: `RAN`, with references to the evidence of the live compat test in §3.5.5; `WAIVED`, with the Product Owner's quoted words and their date; or `MISSING`:

* the QA readiness record;
* the QA Plan and its review;
* the QA task set;
* the QA execution result;
* the QA evidence review;
* the final QA Report and the RCA;
* the close mutation set result; and
* the closure decision.

Only the Product Owner may decide that the live compat test, or any part of it, does not apply to an Epic. `WAIVED` needs the Product Owner's own written waiver, specific to the change, that quotes the Product Owner's words with their date and carries the exemption content HDE Governance requires. Silence, reviewer agreement, convenience, closed-rails success and an agent's finding that the test does not apply are not waivers; without a recorded waiver, the live compat test applies in full. `MISSING` blocks each stage:

| Stage | Effect of `MISSING` |
| :---- | :---- |
| QA readiness | Not `READY_FOR_QA` |
| QA Plan | Not approval-ready |
| QA Plan review | Not approvable |
| QA evidence review | Not acceptable |
| Final QA Report | No PASS verdict |
| Close mutation set | Not close-PR-ready |
| Closure decision | Not `CLOSE` |

No agent may override that block; only the Product Owner may waive the live compat test or any part of it. Every prompt that produces one of these records applies this rule, and until a prompt is updated to carry it, the agent running that prompt applies it.

“Live QA” name (normative; Epics). A Guide, Plan, task set, evidence branch, Report or verdict may carry the name “Live QA” only when it covers or records the live compat test or a recorded Product Owner waiver of it. Any other QA is called “closed-rails QA” in its title, branch name and verdict line. A QA Report without the live test says so in its first line, “No live test ran.”, and names the waiver or the missing test.

Both rules are expressly scoped to Epics (§0.2), and §3.5.5 records the open CRD question. HDE Build Notes records the Product Owner's direction that sets them.
~~~~~~

### RL-08

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-1, R-3, R-4 routing)
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
* Location: §3.4 introductory paragraph, before §3.4.1 (baseline line 638)
* Old block: baseline line 638
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
This section describes a manual Live QA execution pattern that is generalized across epics. It is designed to produce mechanical, reviewable evidence under the epic QA root without introducing hidden dependencies, git gates, or non-canonical runners.
~~~~~~

Replacement:

~~~~~~
This section describes a manual Live QA execution pattern that is generalized across epics. It is designed to produce mechanical, reviewable evidence under the epic QA root without introducing hidden dependencies, git gates, or non-canonical runners.

For an Epic, Live QA always includes the live compat test of §3.5.5; only QA that covers or records that test, or a recorded Product Owner waiver of it, carries the name “Live QA”, and each QA record carries the live test line of §3.1.2. This pattern governs how a Live QA check is run and evidenced. Following it does not make a check live: a QA run whose checks all ran under closed rails is closed-rails QA, whatever its records are titled.
~~~~~~

### RL-09

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run family); C-17 context; support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.3 Evidence layout: current-state first (new posture)**` > `#### **QA evidence and work-product path grammar (normative)**`
* Location: Path-grammar table row “Post-verdict close-run evidence of an admitted CRD” (baseline line 742)
* Old block: baseline line 742
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
| Post-verdict close-run evidence of an admitted CRD | `audit/qa/<crd-id>/close/<check_id>/primary.log`, with its sibling `primary.log.path_proof.txt` | Introduced by HDE Build Notes for a CRD that the canonical evidence updater admits; `<crd-id>` is the CRD's lower-case directory form, for example `hde-crd-0002`. Each close-run check has one primary holding same-run mechanical evidence of the change's close workflow, rendered from that check's captured command, exit code and output as a Plan Templates v2 step-log header, with the PASS, FAIL or BLOCKED posture that “Close-pack truthfulness and same-run execution” requires. Only the canonical evidence updater writes the family, after the final QA verdict; it neither reopens nor adds to `qa_step_logs_manifest.json` or any `checks/` primary. Its members are the validated primaries and path proofs under `close/`, and anything else there is refused. This membership rule is a scoped exception, for `close/` only, to the rule against inferring state by enumerating subdirectories (§4.4.2); that rule continues to govern `checks/` and every other part of the QA root, where `qa_step_logs_manifest.json` stays the authoritative index. No Epic close-run family is admitted. HDE Schemas & Artifacts and HDE Build Notes govern the family's artifact contract. |
~~~~~~

Replacement:

~~~~~~
| Post-verdict close-run evidence of an admitted CRD or Epic | `audit/qa/<crd-id>/close/<check_id>/primary.log` for a CRD, or `audit/qa/<epic-id>/close/<check_id>/primary.log` for an Epic, each with its sibling `primary.log.path_proof.txt` | Introduced by HDE Build Notes for a CRD that the canonical evidence updater admits and extended to an Epic whose close run it admits; `<crd-id>` is the CRD's lower-case directory form, for example `hde-crd-0002`, and `<epic-id>` is the Epic's, for example `hde-epic041`. Each close-run check has one primary holding same-run mechanical evidence of the change's close workflow, rendered from that check's captured command, exit code and output as a Plan Templates v2 step-log header, with the PASS, FAIL or BLOCKED posture that “Close-pack truthfulness and same-run execution” requires. Only the canonical evidence updater writes the family, after the final QA verdict; it neither reopens nor adds to `qa_step_logs_manifest.json` or any `checks/` primary. Its members are the validated primaries and path proofs under `close/`, and anything else there is refused. This membership rule is a scoped exception, for `close/` only, to the rule against inferring state by enumerating subdirectories (§4.4.2); that rule continues to govern `checks/` and every other part of the QA root, where `qa_step_logs_manifest.json` stays the authoritative index. An Epic has the family only after its own explicit admission; HDE-EPIC041 is the first Epic admitted. HDE Schemas & Artifacts and HDE Build Notes govern the family's artifact contract. |
~~~~~~

### RL-10

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run family); support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.3 Evidence layout: current-state first (new posture)**` > `#### **Approved exceptions and external evidence families (normative)**`
* Location: Approved exceptions, item 5 (baseline line 782)
* Old block: baseline line 782
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
5. exact owner-defined closeout surfaces, including the post-verdict close-run family of an admitted CRD under `audit/qa/<crd-id>/close/`;  
~~~~~~

Replacement:

~~~~~~
5. exact owner-defined closeout surfaces, including the post-verdict close-run family of an admitted CRD under `audit/qa/<crd-id>/close/` or of an admitted Epic under `audit/qa/<epic-id>/close/`;  
~~~~~~

### RL-11

* Operation: `REPLACE`
* Change type: CONSISTENCY
* Source rows: Inconsistency: approved omission marker against §3.4.10 line 1017 and PF03
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.10 Plan validity lint (blockers-only; deterministic)**`
* Location: §3.4.10, Reviewer hygiene rules, the omission-marker bullet (baseline line 1073)
* Old block: baseline line 1073
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Approved omission markers are `[SNIP: lines omitted]` and `[SNIP: paragraph omitted]`. Any other omission marker is treated as non-canon.  
~~~~~~

Replacement:

~~~~~~
* Approved omission markers are `[SNIP: <n> lines omitted]` and `[SNIP: paragraph omitted]`. Any other omission marker is treated as non-canon.  
~~~~~~

### RL-12

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §3.4.12 heading flattened into the last §3.4.11 bullet
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.11 Vendor and DB safety constraints (names-only)**`
* Location: Baseline line 1113, after the §3.4.11 bullet list
* Old block: baseline lines 1112–1113
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Live QA must use dry-run or closed-rails stubs where the canon requires it.  
  **3.4.12 Doc-alignment steps (mechanical, not narrative)**
~~~~~~

Replacement:

~~~~~~
* Live QA must use dry-run or closed-rails stubs where the canon requires it.  

### **3.4.12 Doc-alignment steps (mechanical, not narrative)**
~~~~~~

### RL-13

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run family); C-17 context; support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.11 Vendor and DB safety constraints (names-only)**`
* Location: Third paragraph of “Close-pack truthfulness and same-run execution (normative)”, beginning “For a CRD that the canonical evidence updater admits,” (baseline line 1124)
* Old block: baseline line 1124
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
For a CRD that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/` (§3.4.3): one primary log per close-run check, each with its sibling path proof, published after the final QA verdict without reopening or adding to the change's approved QA step-logs manifest or any `checks/` primary. No Epic close-run family is admitted; an Epic needs its own explicit admission before it has one.
~~~~~~

Replacement:

~~~~~~
For a CRD or an Epic that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/` or `audit/qa/<epic-id>/close/` (§3.4.3): one primary log per close-run check, each with its sibling path proof, published after the final QA verdict without reopening or adding to the change's approved QA step-logs manifest or any `checks/` primary. An Epic has that family only after its own explicit admission; HDE-EPIC041 is the first Epic admitted.
~~~~~~

### RL-14

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run pointer, B-2); C-17 context; support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.11 Vendor and DB safety constraints (names-only)**`
* Location: Last paragraph of “Close report requirements (validator-bound; mechanical)” before the operator-prose paragraph, beginning “The same requirements apply to a CRD close report” (baseline line 1146)
* Old block: baseline line 1146
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
The same requirements apply to a CRD close report, for example `audit/HDE-CRD-0002_close_report.md`. The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD: the heading `QA Rails — Open/Close (Final PR)` verbatim, and the “Acceptance and evidence pointers” list with one entry for each pointer the source records. For a CRD, the change's close-run family root, `audit/qa/<crd-id>/close/`, is a required pointer, and the writer refuses a source that omits it. HDE Mechanics Guide, HDE Schemas & Artifacts and Change Process Guide own the writer, its source schema and the close-pack paths of record.
~~~~~~

Replacement:

~~~~~~
The same requirements apply to a CRD close report, for example `audit/HDE-CRD-0002_close_report.md`. The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD: the heading `QA Rails — Open/Close (Final PR)` verbatim, and the “Acceptance and evidence pointers” list with one entry for each pointer the source records. For a CRD, the change's close-run family root, `audit/qa/<crd-id>/close/`, is a required pointer, and the writer refuses a source that omits it. An Epic's source may record its own close-run family root, `audit/qa/<epic-id>/close/`, as a pointer before the close run writes that directory, but is not required to. HDE Mechanics Guide, HDE Schemas & Artifacts and Change Process Guide own the writer, its source schema and the close-pack paths of record.
~~~~~~

### RL-15

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost placeholder (first of two in the line; the second is not recoverable)
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.5 Live QA via Codespaces → Railway (cross-epic crib)**` > `### **3.5.1 Prod and console roles**`
* Location: §3.5.1, second bullet (baseline line 1206)
* Old block: baseline line 1206
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* it stores each check’s QA artifacts under `audit/qa/<epic-id>/checks/<check_id>/` in the repo, where \\ is the lower-case epic identifier (for example `hde-epic018`) and the approved plan resolves the concrete \\
~~~~~~

Replacement:

~~~~~~
* it stores each check’s QA artifacts under `audit/qa/<epic-id>/checks/<check_id>/` in the repo, where `<epic-id>` is the lower-case epic identifier (for example `hde-epic018`) and the approved plan resolves the concrete \\
~~~~~~

### RL-16

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-1, R-5, with the R-6 routing); support C-30; HDE Build Notes source reference
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.5 Live QA via Codespaces → Railway (cross-epic crib)**` > `### **3.5.5 PO Live QA sessions (vendor-first rails)**`
* Location: The line “Production-affecting Live QA minimum is as follows.” (baseline line 1369)
* Old block: baseline line 1369
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Production-affecting Live QA minimum is as follows.
~~~~~~

Replacement:

~~~~~~
Live compat test minimum (normative; Epics).

Every Epic's QA Plan includes, and its QA run executes, the live compat test below, whatever the Epic changed and whether or not its own surfaces are on a production path. Compat is the product, so a QA verdict that has not seen compat work live says nothing about whether the product works. The test is part of the Epic's QA Plan and QA run whichever class its steps carry and whoever executes them; the class rules above govern the Product Owner's session workload, not this minimum.

* Live vendor compat. Run `hdctl showcompat --source vendor` under `SAFE_MODE=0` and `ALLOW_NETWORK=1`, step-local, on synthetic birth data only, at the Epic's QA execution source. Run at least two distinct pairs, each as AB and as BA, and run one pair twice. Each of these must hold:
  * each output has the canonical result shape and the release identity of the source;
  * AB and BA are byte-identical;
  * the two runs are byte-identical;
  * the Reader bytes stay `{id, band}` only; and
  * the two pairs produce different results.
* Deployed-service check. Compare the production HD Engine's `/internal/version` release identity with the release on `main`, and have the production Reader, for each Reader version, score the two synthetic stored people SYN-A and SYN-B in both orders. Each answer must be eligible and bands-only, and AB and BA must be byte-identical. Report as findings with the QA result any mismatch between the deployed release and `main`, and any difference between the deployed bands and the CLI bands for the same birth data.
* SYN-A and SYN-B. The production Reader scores only people whose charts are stored in the production database, so two synthetic people are kept there as permanent QA fixtures under fixed UUIDs: SYN-A, `9cff60ae-6eb6-5618-aec5-8acaa4f290d2`, born 1990-01-01 at 12:00 in Amsterdam, Netherlands; and SYN-B, `57f0c055-ff09-5fdb-aedb-def880437e6f`, born 1985-07-15 at 08:30 in London, United Kingdom. Their identities are registered in the EPIC011 test-identity record and the engine's synthetic identity map. They are synthetic fixtures stored through the engine's own write path under the Product Owner's write authorization, not app users; QA does not create or store them, and the §3.3 prohibition on QA-created user records stands. If either is missing when a QA run starts, the deployed-service check is `TOOLING_BLOCKED` until it is stored again.
* A live test that cannot run. A live compat test that cannot run, for missing credentials, missing target facts, an unavailable vendor or a missing authorization, is `TOOLING_BLOCKED` under HDE Governance. The Epic waits: a blocked live test never becomes a PASS, a waiver or a closure, and the Product Owner decides how to proceed.
* The Epic's own live surfaces. When the Epic's own surfaces are on a production or vendor path, the QA Plan also includes at least one open-rails step that exercises those surfaces live, under the production-affecting minimum below and HDE Governance.
* What does not satisfy the test: closed-rails tests, fixture replay, mocks, static analysis, governed evidence artifacts, review approval and an unrun procedure.

The live compat test is Ops evidence under HDE Governance, and the execution controls at the end of this subsection apply to it in full. Only the Product Owner may waive it or any part of it (§3.1.2). The production-affecting minimum below adds to this test for an Epic and does not replace it; no exemption, closed-rails substitution or live non-vendor step under that minimum exempts an Epic from it.

This minimum, and the live test line and “Live QA” name rules in §3.1.2, are expressly scoped to Epics (§0.2). Whether a CRD that changes runtime code also runs the live compat test is a Product Owner decision that HDE Build Notes leaves open; this guide does not decide it. HDE Build Notes records the Product Owner's direction that sets this minimum.

Production-affecting Live QA minimum is as follows.
~~~~~~

### RL-17

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.1 HD Engine — Catalog/A7 (HDE-specific)**` > `### **Inputs**`
* Location: §5 playbook sub-heading “Steps” (baseline line 2183)
* Old block: baseline lines 2182–2183
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* The current Endpoint Catalog entry (by title only) that identifies the route and its env-gate.  
  **Steps**  
~~~~~~

Replacement:

~~~~~~
* The current Endpoint Catalog entry (by title only) that identifies the route and its env-gate.  

### **Steps**

~~~~~~

### RL-18

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.1 HD Engine — Catalog/A7 (HDE-specific)**` > `### **Evidence**`
* Location: §5 playbook sub-heading “Tokens (names-only)” (baseline line 2246)
* Old block: baseline lines 2245–2246
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Index updates must be in the same PR that introduces or refreshes these artifacts.  
  **Tokens (names-only)**
~~~~~~

Replacement:

~~~~~~
* Index updates must be in the same PR that introduces or refreshes these artifacts.  

### **Tokens (names-only)**
~~~~~~

### RL-19

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.1 HD Engine — Catalog/A7 (HDE-specific)**` > `### **Evidence**`
* Location: §5 playbook sub-heading “Failures to watch” (baseline line 2255)
* Old block: baseline lines 2254–2255
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `A7_ENCODING_INVARIANCE_OK`  
  **Failures to watch**  
~~~~~~

Replacement:

~~~~~~
* `A7_ENCODING_INVARIANCE_OK`  

### **Failures to watch**

~~~~~~

### RL-20

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.1 HD Engine — Catalog/A7 (HDE-specific)**` > `### **Evidence**`
* Location: §5 playbook sub-heading “Where it lives (titles-only)” (baseline line 2263)
* Old block: baseline lines 2262–2263
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Evidence captured but not indexed in both human and machine indices in the same PR.  
  **Where it lives (titles-only)**  
~~~~~~

Replacement:

~~~~~~
* Evidence captured but not indexed in both human and machine indices in the same PR.  

### **Where it lives (titles-only)**

~~~~~~

### RL-21

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)**` > `### **Intent**`
* Location: §5 playbook sub-heading “Inputs” (baseline line 2280)
* Old block: baseline lines 2279–2280
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* ensuring the CLI uses the same emitter and cannot silently “suppress” narratives due to missing tuples or mis-wired composition.  
  **Inputs**  
~~~~~~

Replacement:

~~~~~~
* ensuring the CLI uses the same emitter and cannot silently “suppress” narratives due to missing tuples or mis-wired composition.  

### **Inputs**

~~~~~~

### RL-22

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)**` > `### **Intent**`
* Location: §5 playbook sub-heading “Scope” (baseline line 2289)
* Old block: baseline lines 2288–2289
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
  * can emit header snapshots for text and suppression cases.  
* **Scope**
~~~~~~

Replacement:

~~~~~~
  * can emit header snapshots for text and suppression cases.  

### **Scope**
~~~~~~

### RL-23

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)**` > `### **Steps**`
* Location: §5 playbook sub-heading “Evidence” (baseline line 2334)
* Old block: baseline lines 2333–2334
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Ensure these index updates occur in the same PR as the new or updated snapshots.  
  **Evidence**  
~~~~~~

Replacement:

~~~~~~
* Ensure these index updates occur in the same PR as the new or updated snapshots.  

### **Evidence**

~~~~~~

### RL-24

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.2 Aux & CLI preview (cross-component, BE \+ HDE emitter)**` > `### **Steps**`
* Location: §5 playbook sub-heading “Tokens (names-only)” (baseline line 2342)
* Old block: baseline lines 2341–2342
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Index updates must be in the same PR as the snapshots.  
  **Tokens (names-only)**
~~~~~~

Replacement:

~~~~~~
* Index updates must be in the same PR as the snapshots.  

### **Tokens (names-only)**
~~~~~~

### RL-25

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.3 App Backend (non-HDE endpoints)**` > `### **Intent**`
* Location: §5 playbook sub-heading “Inputs” (baseline line 2378)
* Old block: baseline lines 2377–2378
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* enforcing the same evidence/index parity rules used elsewhere  
  **Inputs**  
~~~~~~

Replacement:

~~~~~~
* enforcing the same evidence/index parity rules used elsewhere  

### **Inputs**

~~~~~~

### RL-26

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.3 App Backend (non-HDE endpoints)**` > `### **Intent**`
* Location: §5 playbook sub-heading “Scope” (baseline line 2387)
* Old block: baseline lines 2386–2387
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
  * `TZ=UTC`  
* **Scope**
~~~~~~

Replacement:

~~~~~~
  * `TZ=UTC`  

### **Scope**
~~~~~~

### RL-27

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.3 App Backend (non-HDE endpoints)**` > `### **Intent**`
* Location: §5 playbook sub-heading “Steps” (baseline line 2398)
* Old block: baseline lines 2397–2398
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Internal-only service-to-service calls that are not part of any QA surface.  
  **Steps**  
~~~~~~

Replacement:

~~~~~~
* Internal-only service-to-service calls that are not part of any QA surface.  

### **Steps**

~~~~~~

### RL-28

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.3 App Backend (non-HDE endpoints)**` > `### **Intent**`
* Location: §5 playbook sub-heading “Evidence” (baseline line 2437)
* Old block: baseline lines 2436–2437
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
    * enforce that the Human Index and mirror entries exist for all governed App BE evidence  
* **Evidence**
~~~~~~

Replacement:

~~~~~~
    * enforce that the Human Index and mirror entries exist for all governed App BE evidence  

### **Evidence**
~~~~~~

### RL-29

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.4 App Frontend**` > `### **Inputs**`
* Location: §5 playbook sub-heading “Scope” (baseline line 2502)
* Old block: baseline lines 2501–2502
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
  * basic accessibility and performance probes  
* **Scope**
~~~~~~

Replacement:

~~~~~~
  * basic accessibility and performance probes  

### **Scope**
~~~~~~

### RL-30

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.4 App Frontend**` > `### **Inputs**`
* Location: §5 playbook sub-heading “Steps” (baseline line 2512)
* Old block: baseline lines 2511–2512
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Detailed UX specs, design review, or full accessibility audits (these are owned by product and design documents).  
  **Steps**  
~~~~~~

Replacement:

~~~~~~
* Detailed UX specs, design review, or full accessibility audits (these are owned by product and design documents).  

### **Steps**

~~~~~~

### RL-31

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.4 App Frontend**` > `### **Inputs**`
* Location: §5 playbook sub-heading “Evidence” (baseline line 2537)
* Old block: baseline lines 2536–2537
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* Use titles-only descriptions for FE QA artifacts in the human index; schemas and mirror rules remain in PF12.  
  **Evidence**  
~~~~~~

Replacement:

~~~~~~
* Use titles-only descriptions for FE QA artifacts in the human index; schemas and mirror rules remain in PF12.  

### **Evidence**

~~~~~~

### RL-32

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.4 App Frontend**` > `### **Inputs**`
* Location: §5 playbook sub-heading “Tokens (names-only, FE pattern)” (baseline line 2545)
* Old block: baseline lines 2544–2545
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
    with FE artifacts described by title only per PF12.  
* **Tokens (names-only, FE pattern)**
~~~~~~

Replacement:

~~~~~~
    with FE artifacts described by title only per PF12.  

### **Tokens (names-only, FE pattern)**
~~~~~~

### RL-33

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.4 App Frontend**` > `### **Inputs**`
* Location: §5 playbook sub-heading “Failures to watch” (baseline line 2554)
* Old block: baseline lines 2553–2554
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `MACHINE_MIRROR_UPDATED_OK`  
  **Failures to watch**  
~~~~~~

Replacement:

~~~~~~
* `MACHINE_MIRROR_UPDATED_OK`  

### **Failures to watch**

~~~~~~

### RL-34

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: stray bold on one list item
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.4 App Frontend**` > `### **Inputs**`
* Location: §5.4, Failures to watch, last item (baseline line 2559)
* Old block: baseline line 2559
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* **FE QA artifacts added without corresponding updates to the human index and machine mirror in the same PR.**
~~~~~~

Replacement:

~~~~~~
* FE QA artifacts added without corresponding updates to the human index and machine mirror in the same PR.
~~~~~~

### RL-35

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost `<pair>` placeholder (form proved at lines 2971 and 2979)
* Heading path (literal baseline heading lines, outermost first): `# **5\. Component playbooks (how to run QA per surface)**` > `## **5.8 Admin bundle surfaces (CLI & HTTP, HDE-only)**` > `### **Evidence**`
* Location: §5.8, Evidence, first two items (baseline lines 3010–3011)
* Old block: baseline lines 3010–3011
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* artifacts/admin/cli\_bundle\_\\.json — CLI admin bundle.  
* artifacts/admin/http\_bundle\_\\.json — HTTP admin bundle.  
~~~~~~

Replacement:

~~~~~~
* `artifacts/admin/cli_bundle_<pair>.json` — CLI admin bundle.  
* `artifacts/admin/http_bundle_<pair>.json` — HTTP admin bundle.  
~~~~~~

### RL-36

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost `<epic-id>` placeholder
* Heading path (literal baseline heading lines, outermost first): `# **8\. Evidence & indexing reference (quick rules)**` > `## **Gitignore rails for QA roots**`
* Location: §8, Gitignore rails for QA roots (baseline line 3234)
* Old block: baseline line 3234
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
When a new audit/qa/\\ tree is introduced, the build/infra owner MUST ensure that .gitignore has no entries that match audit/qa, unless explicit allow rules keep per-epic QA evidence trees visible to git while still allowing narrowly targeted ignores for non-evidence scratch files.
~~~~~~

Replacement:

~~~~~~
When a new `audit/qa/<epic-id>/` tree is introduced, the build/infra owner MUST ensure that .gitignore has no entries that match audit/qa, unless explicit allow rules keep per-epic QA evidence trees visible to git while still allowing narrowly targeted ignores for non-evidence scratch files.
~~~~~~

### RL-37

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.1 Historical token glossary (names-only; sources in PF04/PF09)**` > `### **9.1.1 Pre-commit**`
* Location: §9.1 sub-heading “9.1.2 Post-commit (general)” (baseline line 3285)
* Old block: baseline lines 3284–3285
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `COMPOSITE_ABBA_IDENTITY_OK`  
  **9.1.2 Post-commit (general)**  
~~~~~~

Replacement:

~~~~~~
* `COMPOSITE_ABBA_IDENTITY_OK`  

### **9.1.2 Post-commit (general)**

~~~~~~

### RL-38

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.1 Historical token glossary (names-only; sources in PF04/PF09)**` > `### **9.1.1 Pre-commit**`
* Location: §9.1 sub-heading “9.1.3 Aux” (baseline line 3298)
* Old block: baseline lines 3297–3298
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `QA_ACCEPTANCE_MAP_VIABILITY_OK`  
  **9.1.3 Aux**  
~~~~~~

Replacement:

~~~~~~
* `QA_ACCEPTANCE_MAP_VIABILITY_OK`  

### **9.1.3 Aux**

~~~~~~

### RL-39

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.1 Historical token glossary (names-only; sources in PF04/PF09)**` > `### **9.1.1 Pre-commit**`
* Location: §9.1 sub-heading “9.1.4 Catalog/A7” (baseline line 3303)
* Old block: baseline lines 3302–3303
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `NARR_VARY_AUTH_AE_OK`  
  **9.1.4 Catalog/A7**  
~~~~~~

Replacement:

~~~~~~
* `NARR_VARY_AUTH_AE_OK`  

### **9.1.4 Catalog/A7**

~~~~~~

### RL-40

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.1 Historical token glossary (names-only; sources in PF04/PF09)**` > `### **9.1.1 Pre-commit**`
* Location: §9.1 sub-heading “9.1.5 CLI/API & SDKs” (baseline line 3309)
* Old block: baseline lines 3308–3309
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `A7_ENCODING_INVARIANCE_OK`  
  **9.1.5 CLI/API & SDKs**  
~~~~~~

Replacement:

~~~~~~
* `A7_ENCODING_INVARIANCE_OK`  

### **9.1.5 CLI/API & SDKs**

~~~~~~

### RL-41

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.1 Historical token glossary (names-only; sources in PF04/PF09)**` > `### **9.1.1 Pre-commit**`
* Location: §9.1 sub-heading “9.1.6 Build/CI (PF09)” (baseline line 3315)
* Old block: baseline lines 3314–3315
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `ADMIN_AUTH_REQUIRED_OK`  
  **9.1.6 Build/CI (PF09)**  
~~~~~~

Replacement:

~~~~~~
* `ADMIN_AUTH_REQUIRED_OK`  

### **9.1.6 Build/CI (PF09)**

~~~~~~

### RL-42

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.1 Historical token glossary (names-only; sources in PF04/PF09)**` > `### **9.1.1 Pre-commit**`
* Location: §9.1 sub-heading “9.1.7 App FE/BE (App QA docs)” (baseline line 3318)
* Old block: baseline lines 3317–3318
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* `QA_HARNESS_ENTRYPOINT_SELFTEST_OK`  
  **9.1.7 App FE/BE (App QA docs)**
~~~~~~

Replacement:

~~~~~~
* `QA_HARNESS_ENTRYPOINT_SELFTEST_OK`  

### **9.1.7 App FE/BE (App QA docs)**
~~~~~~

### RL-43

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost placeholders (form proved at line 1952)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.4 Evidence skeleton & sanity tokens**`
* Location: §9.2.4, `QA_HARNESS_DISCIPLINE_OK` QA definition (baseline line 3482)
* Old block: baseline line 3482
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
    * The manifest is current-state only. Any per-run retention logs under runs/\\/\\ are optional and non-canonical, and MUST NOT be referenced by log\_path.  
~~~~~~

Replacement:

~~~~~~
    * The manifest is current-state only. Any per-run retention logs under `runs/<run_id>/<RUN_SUBPATH>` are optional and non-canonical, and MUST NOT be referenced by log\_path.  
~~~~~~

### RL-44

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost `<epic-id>` placeholder (canonical path at line 1933)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.4 Evidence skeleton & sanity tokens**`
* Location: §9.2.4, `QA_HARNESS_DISCIPLINE_OK` evidence (baseline line 3485)
* Old block: baseline line 3485
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
  * The epic maintains audit/qa/\\/qa\_step\_logs\_manifest.json as a per-epic index keyed by check\_id, mapping each required check to its canonical primary log via log\_path.  
~~~~~~

Replacement:

~~~~~~
  * The epic maintains `audit/qa/<epic-id>/qa_step_logs_manifest.json` as a per-epic index keyed by check\_id, mapping each required check to its canonical primary log via log\_path.  
~~~~~~

### RL-45

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost `<pair>` placeholder (form proved at lines 2971 and 2979)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.7 CLI/API & SDK tokens**` > `#### **CLI\_ADMIN\_BUNDLE\_PARITY\_OK**`
* Location: §9.2.7, `CLI_ADMIN_BUNDLE_PARITY_OK` evidence (baseline lines 3593–3594)
* Old block: baseline lines 3593–3594
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
    * artifacts/admin/cli\_bundle\_\\.json (CLI), and  
    * artifacts/admin/http\_bundle\_\\.json (HTTP),  
~~~~~~

Replacement:

~~~~~~
    * `artifacts/admin/cli_bundle_<pair>.json` (CLI), and  
    * `artifacts/admin/http_bundle_<pair>.json` (HTTP),  
~~~~~~

### RL-46

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost `<pair>` placeholder (form proved at line 2971)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.7 CLI/API & SDK tokens**` > `#### **ADMIN\_BUNDLE\_FULL\_PAYLOAD\_OK**`
* Location: §9.2.7, `ADMIN_BUNDLE_FULL_PAYLOAD_OK` evidence (baseline line 3610)
* Old block: baseline line 3610
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
  * At least one governed admin bundle artifact (for example artifacts/admin/cli\_bundle\_\\.json) per test match, produced via the canonical admin bundle builder under determinism env pins.  
~~~~~~

Replacement:

~~~~~~
  * At least one governed admin bundle artifact (for example `artifacts/admin/cli_bundle_<pair>.json`) per test match, produced via the canonical admin bundle builder under determinism env pins.  
~~~~~~

### RL-47

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost `<epic-id>` placeholder (canonical path at line 1933)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.13 Live vendor and discovery QA conditions**` > `#### **QA\_HARNESS\_DISCIPLINE\_OK**`
* Location: §9.2.13, `QA_HARNESS_DISCIPLINE_OK` evidence (baseline line 3748)
* Old block: baseline line 3748
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
    * a consolidated step logs manifest (audit/qa/\\/qa\_step\_logs\_manifest.json)  
~~~~~~

Replacement:

~~~~~~
    * a consolidated step logs manifest (`audit/qa/<epic-id>/qa_step_logs_manifest.json`)  
~~~~~~

### RL-48

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: lost placeholders (form proved at lines 1933 and 1952)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.13 Live vendor and discovery QA conditions**` > `#### **QA\_HARNESS\_DISCIPLINE\_OK**`
* Location: §9.2.13, the note after the viability evidence list (baseline line 3769)
* Old block: baseline line 3769
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Note: Under current QA posture, the manifest is a current-state index keyed by check\_id. Optional per-run retention paths under audit/qa/\\/runs/\\/\\ may exist, but are not required for this token.
~~~~~~

Replacement:

~~~~~~
Note: Under current QA posture, the manifest is a current-state index keyed by check\_id. Optional per-run retention paths under `audit/qa/<epic-id>/runs/<run_id>/<RUN_SUBPATH>` may exist, but are not required for this token.
~~~~~~

### RL-49

* Operation: `REPLACE`
* Change type: CONSISTENCY
* Source rows: C-26 (R-4 at the final QA Report and RCA)
* Heading path (literal baseline heading lines, outermost first): `# **9\. Legacy QA acceptance-token compatibility**` > `## **9.2 Legacy QA Acceptance Token Library (optional compatibility)**` > `### **9.2.15 Review rails for optional legacy token metadata**` > `#### **9.2.15.6 Final QA closeout review required elements (required; closeout gate)**`
* Location: Required-elements checklist, the bullet “the completed final QA Report and separate RCA for every completed run” (baseline line 3903)
* Old block: baseline line 3903
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
* the completed final QA Report and separate RCA for every completed run, including all-PASS, with actual doc-delta and failure/causal limitations retained  
~~~~~~

Replacement:

~~~~~~
* the completed final QA Report and separate RCA for every completed run, including all-PASS, with actual doc-delta and failure/causal limitations retained  
* for an Epic, the live test line of §3.1.2 in the final QA Report and RCA, with its value and the evidence references or waiver it cites  
~~~~~~

### RL-50

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: false statement about HDE Build Notes; current addenda referenced
* Heading path (literal baseline heading lines, outermost first): `# **13\. Change QA History**` > `## **Classification and current-owner routing**` > `### **Complete flagged-unit classification ledger**`
* Location: §13, Complete flagged-unit classification ledger, row SRC-0292 (baseline line 4468)
* Old block: baseline line 4468
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
| 13.8 | SRC-0292 | H | Retain the temporary PF10 clarification as historical; PF10-HDE-Build-Notes has no current addenda. |
~~~~~~

Replacement:

~~~~~~
| 13.8 | SRC-0292 | H | Retain the temporary PF10 clarification as historical; current HDE Build Notes addenda govern where they speak. |
~~~~~~

### RL-51

* Operation: `REPLACE`
* Change type: DELETION
* Source rows: Defect: §13.18 repeats §13.17's non-goals paragraph (line 5223 equals line 5203)
* Heading path (literal baseline heading lines, outermost first): `# **13\. Change QA History**` > `## **13.18 HDE-EPIC039 — QA learnings snapshot for reusable QA orchestration, exact-head CI, Moon Loop correction, evidence normalization, and closure-axis separation**`
* Location: §13.18, the second “Known non-goals” paragraph (baseline lines 5221–5223; line 5221 is kept)
* Old block: baseline lines 5221–5223
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
Known non-goals: this entry does not redefine canonical JSON mechanics, arrays-as-sets semantics, evidence publication or Machine Mirror mechanics, exact repository paths, commands, tests, hashes, artifacts, PF09 row text or status, close-pack bytes, token semantics, workflow syntax, implementation state, deployment state, or current repository state. PF19 records the QA posture and review learnings only.

Known non-goals: this entry does not redefine token semantics, A7 byte rules, transport bytes, public Reader posture, exact vendor endpoint bytes, exact auth header values, exact request-body fields, exact response-envelope bytes, exact credential values, exact evidence paths, exact tests, exact PF09.5 status rows, exact Live QA runbook bytes, final QA closeout report bytes, QA RCA bytes, AI runtime scope, public Reader changes, new HTTP homes, PF23 audit requirements, PF29 workflow text, mapped-cache implementation work, production upsert authorization, or concrete PF02, PF03, PF05, PF09.5, PF12, PF14, PF20, PF27, or PF29 doc deltas. PF19 records QA posture and review learnings only.
~~~~~~

Replacement:

~~~~~~
Known non-goals: this entry does not redefine canonical JSON mechanics, arrays-as-sets semantics, evidence publication or Machine Mirror mechanics, exact repository paths, commands, tests, hashes, artifacts, PF09 row text or status, close-pack bytes, token semantics, workflow syntax, implementation state, deployment state, or current repository state. PF19 records the QA posture and review learnings only.
~~~~~~

### RL-52

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Source rows: Defect: list lead-in captured as a table row
* Heading path (literal baseline heading lines, outermost first): `# **14\. Codespaces QA environments (environment details)**` > `## **14.6 Ownership and maintenance**`
* Location: §14.6, last row of the ownership table (baseline line 5587)
* Old block: baseline line 5587
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
| Update trigger(s) include: |  |  |  |
~~~~~~

Replacement:

~~~~~~

Update trigger(s) include:
~~~~~~

END OF REDLINES
