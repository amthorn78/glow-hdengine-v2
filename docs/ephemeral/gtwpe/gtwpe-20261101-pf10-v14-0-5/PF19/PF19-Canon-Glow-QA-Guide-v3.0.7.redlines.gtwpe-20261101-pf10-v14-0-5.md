# Redlines — PF19-Canon-Glow-QA-Guide v3.0.7 — gtwpe-20261101-pf10-v14-0-5 (T-06)

## Package identity

| Field | Value |
| :---- | :---- |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` task T-06, preparation revision 1 |
| Target (original baseline) | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.7.md`, in-document title PF19-Canon-Glow-QA-Guide, v3.0.7, read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b`; SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; 682,678 bytes; 5,622 lines |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; selected units 2.8 (lines 1063–1106, 1111–1127), 2.15 (lines 1650–1804), 2.2 (lines 517–551) and 2.16 (lines 1869–1939) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-06; rows C-17, C-18, C-26 (assigned), C-07, C-29 (uncertain), C-20, C-30 (supporting) |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, run in the Claude Code session Nathan started for T-06 on 2026-11-02 |
| Preparation outcome | `READY` |
| Proof log | `PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, in this directory |

## Literal conventions

* Every payload is fenced with `~~~~~~`. The literal is every byte between the line after the opening fence and the line before the closing fence, lines joined by LF, with no trailing LF. The fence lines and the labels around them are not part of the literal.
* Every old block is one complete baseline line without its terminating LF. Each old block occurs exactly once in the whole original baseline (expected and observed count 1).
* Each replacement replaces only its old block. The baseline LF that follows the old block stays in place, so no neighbouring blank line, heading or table row is consumed.
* All seven redlines resolve independently against the unchanged original. Their spans do not overlap and no redline's output is another's locator.
* Trailing spaces are literal. RL-04's old block and its replacement each end with two U+0020 spaces, as the baseline list item does.

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

Sources that justify this update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (PF10-HDE-Build-Notes, v14.0.5). PF19 keeps no change log or revision-history section, so no history entry is prepared.

## Redlines

### RL-01

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-4, R-3); support C-30
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.1 Intent**` > `### **3.1.2 Independent QA, reporting and closure**`
* Location: §3.1.2, the third and last paragraph, beginning “Ops remains implementation work:” (baseline line 511)
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

`WAIVED` needs the Product Owner's own written waiver for the change. Silence, reviewer agreement, convenience, closed-rails success and an agent's finding that the test does not apply are not waivers. `MISSING` blocks each stage:

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

Both rules are expressly scoped to Epics (§0.2); §3.5.5 records the open CRD question.
~~~~~~

### RL-02

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-1, R-3, R-4 routing)
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
* Location: §3.4 introductory paragraph, before §3.4.1 (baseline line 638)
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

### RL-03

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run family); C-17 context; support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.3 Evidence layout: current-state first (new posture)**` > `#### **QA evidence and work-product path grammar (normative)**`
* Location: Path-grammar table row “Post-verdict close-run evidence of an admitted CRD” (baseline line 742)
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
| Post-verdict close-run evidence of an admitted CRD | `audit/qa/<crd-id>/close/<check_id>/primary.log`, with its sibling `primary.log.path_proof.txt` | Introduced by HDE Build Notes for a CRD that the canonical evidence updater admits; `<crd-id>` is the CRD's lower-case directory form, for example `hde-crd-0002`. Each close-run check has one primary holding same-run mechanical evidence of the change's close workflow, rendered from that check's captured command, exit code and output as a Plan Templates v2 step-log header, with the PASS, FAIL or BLOCKED posture that “Close-pack truthfulness and same-run execution” requires. Only the canonical evidence updater writes the family, after the final QA verdict; it neither reopens nor adds to `qa_step_logs_manifest.json` or any `checks/` primary. Its members are the validated primaries and path proofs under `close/`, and anything else there is refused. This membership rule is a scoped exception, for `close/` only, to the rule against inferring state by enumerating subdirectories (§4.4.2); that rule continues to govern `checks/` and every other part of the QA root, where `qa_step_logs_manifest.json` stays the authoritative index. No Epic close-run family is admitted. HDE Schemas & Artifacts and HDE Build Notes govern the family's artifact contract. |
~~~~~~

Replacement:

~~~~~~
| Post-verdict close-run evidence of an admitted CRD or Epic | `audit/qa/<crd-id>/close/<check_id>/primary.log` for a CRD, or `audit/qa/<epic-id>/close/<check_id>/primary.log` for an Epic, each with its sibling `primary.log.path_proof.txt` | Introduced by HDE Build Notes for a CRD that the canonical evidence updater admits and extended to an Epic whose close run it admits; `<crd-id>` is the CRD's lower-case directory form, for example `hde-crd-0002`, and `<epic-id>` is the Epic's, for example `hde-epic041`. Each close-run check has one primary holding same-run mechanical evidence of the change's close workflow, rendered from that check's captured command, exit code and output as a Plan Templates v2 step-log header, with the PASS, FAIL or BLOCKED posture that “Close-pack truthfulness and same-run execution” requires. Only the canonical evidence updater writes the family, after the final QA verdict; it neither reopens nor adds to `qa_step_logs_manifest.json` or any `checks/` primary. Its members are the validated primaries and path proofs under `close/`, and anything else there is refused. This membership rule is a scoped exception, for `close/` only, to the rule against inferring state by enumerating subdirectories (§4.4.2); that rule continues to govern `checks/` and every other part of the QA root, where `qa_step_logs_manifest.json` stays the authoritative index. An Epic has the family only after its own explicit admission; HDE-EPIC041 is the first Epic admitted. HDE Schemas & Artifacts and HDE Build Notes govern the family's artifact contract. |
~~~~~~

### RL-04

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run family); support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.3 Evidence layout: current-state first (new posture)**` > `#### **Approved exceptions and external evidence families (normative)**`
* Location: Approved exceptions, item 5 (baseline line 782)
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
5. exact owner-defined closeout surfaces, including the post-verdict close-run family of an admitted CRD under `audit/qa/<crd-id>/close/`;  
~~~~~~

Replacement:

~~~~~~
5. exact owner-defined closeout surfaces, including the post-verdict close-run family of an admitted CRD under `audit/qa/<crd-id>/close/` or of an admitted Epic under `audit/qa/<epic-id>/close/`;  
~~~~~~

### RL-05

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run family); C-17 context; support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.11 Vendor and DB safety constraints (names-only)**`
* Location: Third paragraph of “Close-pack truthfulness and same-run execution (normative)”, beginning “For a CRD that the canonical evidence updater admits,” (baseline line 1124)
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
For a CRD that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/` (§3.4.3): one primary log per close-run check, each with its sibling path proof, published after the final QA verdict without reopening or adding to the change's approved QA step-logs manifest or any `checks/` primary. No Epic close-run family is admitted; an Epic needs its own explicit admission before it has one.
~~~~~~

Replacement:

~~~~~~
For a CRD or an Epic that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/` or `audit/qa/<epic-id>/close/` (§3.4.3): one primary log per close-run check, each with its sibling path proof, published after the final QA verdict without reopening or adding to the change's approved QA step-logs manifest or any `checks/` primary. An Epic has that family only after its own explicit admission; HDE-EPIC041 is the first Epic admitted.
~~~~~~

### RL-06

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Source rows: C-18 (Epic close-run pointer, B-2); C-17 context; support C-20
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**` > `### **3.4.11 Vendor and DB safety constraints (names-only)**`
* Location: Last paragraph of “Close report requirements (validator-bound; mechanical)” before the operator-prose paragraph, beginning “The same requirements apply to a CRD close report” (baseline line 1146)
* Expected occurrence of the old block in the whole baseline: 1

Old block:

~~~~~~
The same requirements apply to a CRD close report, for example `audit/HDE-CRD-0002_close_report.md`. The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD: the heading `QA Rails — Open/Close (Final PR)` verbatim, and the “Acceptance and evidence pointers” list with one entry for each pointer the source records. For a CRD, the change's close-run family root, `audit/qa/<crd-id>/close/`, is a required pointer, and the writer refuses a source that omits it. HDE Mechanics Guide, HDE Schemas & Artifacts and Change Process Guide own the writer, its source schema and the close-pack paths of record.
~~~~~~

Replacement:

~~~~~~
The same requirements apply to a CRD close report, for example `audit/HDE-CRD-0002_close_report.md`. The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD: the heading `QA Rails — Open/Close (Final PR)` verbatim, and the “Acceptance and evidence pointers” list with one entry for each pointer the source records. For a CRD, the change's close-run family root, `audit/qa/<crd-id>/close/`, is a required pointer, and the writer refuses a source that omits it. An Epic's source may record its own close-run family root, `audit/qa/<epic-id>/close/`, as a pointer before the close run writes that directory, but is not required to. HDE Mechanics Guide, HDE Schemas & Artifacts and Change Process Guide own the writer, its source schema and the close-pack paths of record.
~~~~~~

### RL-07

* Operation: `REPLACE`
* Change type: NEW_CANON
* Source rows: C-26 (R-1, with the R-6 routing); support C-30
* Heading path (literal baseline heading lines, outermost first): `# **3\. Post-commit QA (staging/prod)**` > `## **3.5 Live QA via Codespaces → Railway (cross-epic crib)**` > `### **3.5.5 PO Live QA sessions (vendor-first rails)**`
* Location: The line “Production-affecting Live QA minimum is as follows.” (baseline line 1369)
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
* The Epic's own live surfaces. When the Epic's own surfaces are on a production or vendor path, the QA Plan also includes at least one open-rails step that exercises those surfaces live, under the production-affecting minimum below and HDE Governance.
* What does not satisfy the test: closed-rails tests, fixture replay, mocks, static analysis, governed evidence artifacts, review approval and an unrun procedure.

The live compat test is Ops evidence under HDE Governance, and the execution controls at the end of this subsection apply to it in full. Only the Product Owner may waive it or any part of it (§3.1.2). The production-affecting minimum below adds to this test for an Epic and does not replace it; no exemption, closed-rails substitution or live non-vendor step under that minimum exempts an Epic from it.

This minimum, and the live test line and “Live QA” name rules in §3.1.2, are expressly scoped to Epics (§0.2). Whether a CRD that changes runtime code also runs the live compat test is a Product Owner decision that HDE Build Notes leaves open; this guide does not decide it.

Production-affecting Live QA minimum is as follows.
~~~~~~

END OF REDLINES
