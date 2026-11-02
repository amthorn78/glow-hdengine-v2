# Proof log — PF19-Canon-Glow-QA-Guide v3.0.8 (application) — gtwpe-20261101-pf10-v14-0-5 (T-06)

This is the application report for `PF19-Canon-Glow-QA-Guide-v3.0.8.md`, in this directory. It records how that revised PF was made from the v3.0.7 baseline and preparation revision 4 of the redlines package, what changed and on what basis, and what was verified. This application supersedes the earlier one from revision 3 (§8). The revised PF is not an authoritative publication: `docs/pfcanon/` is unchanged.

## 1. Artifact and outcome

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF19/PF19-Canon-Glow-QA-Guide-v3.0.8.md` |
| Artifact identity | 693,357 bytes; 5,724 lines; SHA-256 `1a6762a98b7d6a7e2f5b08c3c4c09b10fa06d5cf8339f6e3319a66e081158494`; git blob `6b0ae9e3ab6ae498c7255b09df87a20f9c88cb80` |
| In-document identity | Title PF19-Canon-Glow-QA-Guide; Status Canon; Version v3.0.8; Effective date 2026-11-02; Last Update Gate `BN 14.0.5`; Invocation tag `INV-f2ac55d77ce9aacc` |
| Applier | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`. It was re-fetched live when this application step began, and the page state (2026-10-09T11:05:22.207Z) is unchanged. It ran in the Claude Code session Nathan started for T-06, under his T-06 follow-up handoff of 2026-11-02. No subagent, reviewer or other session was used. |
| Application outcome | Applied: 53 content operations and a three-field metadata plan; none rejected |
| Execution date | 2026-11-02 (UTC; this application started 2026-11-02T02:42Z) |

## 2. Inputs and identities

| Role | Identity |
| :---- | :---- |
| Original baseline | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.7.md` on `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`; v3.0.7; git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b`; raw-byte SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; 682,678 bytes; 5,622 lines. It is the preparer's recorded baseline, compared byte for byte in the same raw representation. It is unchanged since the handoff baseline `e2b7427ff418ca8f08f05587c4a541308a76da56`. |
| Redlines package | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF19/PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.md`, preparation revision 4, at commit `ad418d5c7226759290a04e58c3eaba28fb25aa69`; git blob `7f1bc3e5171f5a1f8af2b2d424cb8d1e9965fb11`; SHA-256 `c515c79751cbd5303a474fbef967356cadec0619ab3d9b505a8d9b56950c56e1`, matching the preparer's proof log |
| Preparation proof log | `PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, same directory and commit |
| Preparer | TW-DRAIN-10 100926.1, the preparation step of this same session; run `gtwpe-20261101-pf10-v14-0-5` T-06, preparation revision 4; outcome `READY` / `COMPLETE_PACKAGE`, with no unresolved or blocking item. H-06 is released for this document by the Product Owner's ruling below and drained in RL-08; H-08 stays held and untouched. |
| Product Owner direction | Nathan, 2026-11-02: "fixed the defects and inconsistencies you noticed. And PF10 addenda should be referenced in any case". The preparer's proof log, §5.4, §5.5, §5.8 and §6, records how that direction is read. |
| Product Owner ruling | Nathan, 2026-11-02: “close pack should go after the decision to close is confirmed”. The T-06 follow-up handoff records it as deciding CCR-5 (HDE Build Notes v14.0.5, addendum 2.5, line 856) as alternative (A): 2.2 R-3 stands as written, its first bullet included, and the permanent documents are drained to match. It releases H-06 for this document; the change source stays HDE Build Notes v14.0.5, 2.2 R-3 (lines 547–551). The preparer's proof log, §5.4 and §5.7, records how the ruling is applied. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, unchanged on `main`. Selected units: 2.8 lines 1063–1106 and 1111–1127; 2.15 lines 1650–1804; 2.2 lines 517–551; 2.16 lines 1869–1939. These match the handoff and the ledger. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-06; rows C-17, C-18, C-26 (assigned), C-07, C-29 (uncertain, now drained), C-20, C-30 (supporting); H-06 released for this document by the ruling. Only the T-06 completion row is updated. |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, read completely in this session |

Intake verification. The complete revision-4 package and its complete preparation proof log were read at this application's intake, from the bytes committed in `ad418d5`, which match the recorded SHA-256 and git blob. The complete original was read in this session at preparation, and the original read at intake is byte-identical to it. The proof log records:

* complete target coverage, in eighteen windows that sum to 682,678 bytes;
* complete selected-source coverage;
* every change accounted for;
* producer validation with a one-pass simulation;
* `READY` / `COMPLETE_PACKAGE`.

The original on `main` at application time is byte-identical to the preparer's baseline. `origin/main` is `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, and neither PF19 v3.0.7 nor HDE Build Notes v14.0.5 has changed since the handoff baseline.

## 3. Operation ledger and basis

Every content operation is a `REPLACE` of one or more whole, contiguous baseline lines, expected and observed exactly once. The change type, source rows and rationale below are the preparer's, as the package and its proof log state them.

| ID | Baseline lines | Location | Change type | Source rows and rationale | Bytes old → new |
| :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | line 138 | §0.4.3, the paragraph beginning “Change-process artifacts, including QA readiness” (baseline line 138) | NEW_CANON | C-07 (2.2 R-1, R-2) | 946 → 2,571 |
| RL-02 | line 221 | §1.4, Infra/ops ownership, the base-URL sub-bullet (baseline line 221) | DOC_HYGIENE | Defect: export-damaged link with a lost placeholder | 227 → 219 |
| RL-03 | line 406 | §2.2.11, sub-bullet beginning “Release and security, QA and audit, and closeout validation are distinct lanes.” (baseline line 406) | NEW_CANON | C-07 (2.2 R-3, second bullet; the first bullet is held with CCR-5, H-06) | 256 → 629 |
| RL-04 | line 418 | §2.2.12, its only paragraph (baseline line 418) | NEW_CANON | C-29 (2.16 R-1, R-2); support C-30 | 229 → 1,548 |
| RL-05 | line 436 | §2.3, first paragraph, beginning “Every EPIC’s PO specifies what rails posture” (baseline line 436) | CONSISTENCY | C-26 (R-1, R-2 context) | 208 → 353 |
| RL-06 | line 503 | §3.1.1, the paragraph after the assessment-state table, beginning “QA-10 is the readiness decision and remediation return point.” (baseline line 503) | NEW_CANON | C-26 (R-2, QA-10 question) | 346 → 701 |
| RL-07 | line 511 | §3.1.2, the third and last paragraph, beginning “Ops remains implementation work:” (baseline line 511) | NEW_CANON | C-26 (R-4, R-3, R-2 waiver form); support C-30; HDE Build Notes source reference; CCR-5 ruling (A), Nathan 2026-11-02: closure decision listed before the close mutation set | 448 → 2,659 |
| RL-08 | line 517 | §3.1.3, the second paragraph, beginning “The close mutation set is outside the post-closure drainage rule above.” (baseline line 517) | CANON_UPDATE | C-07 (2.2 R-3, first bullet; released from H-06 by the CCR-5 ruling (A), Nathan 2026-11-02) | 879 → 972 |
| RL-09 | line 638 | §3.4 introductory paragraph, before §3.4.1 (baseline line 638) | NEW_CANON | C-26 (R-1, R-3, R-4 routing) | 250 → 701 |
| RL-10 | line 742 | Path-grammar table row “Post-verdict close-run evidence of an admitted CRD” (baseline line 742) | CANON_UPDATE | C-18 (Epic close-run family); C-17 context; support C-20; CCR-5 ruling (A), Nathan 2026-11-02: written after the closure decision | 1,317 → 1,614 |
| RL-11 | line 782 | Approved exceptions, item 5 (baseline line 782) | CANON_UPDATE | C-18 (Epic close-run family); support C-20 | 140 → 197 |
| RL-12 | line 1073 | §3.4.10, Reviewer hygiene rules, the omission-marker bullet (baseline line 1073) | CONSISTENCY | Inconsistency: approved omission marker against §3.4.10 line 1017 and PF03 | 141 → 145 |
| RL-13 | lines 1112–1113 | Baseline line 1113, after the §3.4.11 bullet list | DOC_HYGIENE | Defect: §3.4.12 heading flattened into the last §3.4.11 bullet | 140 → 143 |
| RL-14 | line 1124 | Third paragraph of “Close-pack truthfulness and same-run execution (normative)”, beginning “For a CRD that the canonical evidence updater admits,” (baseline line 1124) | CANON_UPDATE | C-18 (Epic close-run family); C-17 context; support C-20; CCR-5 ruling (A), Nathan 2026-11-02: published after the closure decision | 482 → 566 |
| RL-15 | line 1146 | Last paragraph of “Close report requirements (validator-bound; mechanical)” before the operator-prose paragraph, beginning “The same requirements apply to a CRD close report” (baseline line 1146) | CANON_UPDATE | C-18 (Epic close-run pointer, B-2); C-17 context; support C-20 | 665 → 834 |
| RL-16 | line 1206 | §3.5.1, second bullet (baseline line 1206) | DOC_HYGIENE | Defect: lost placeholder (first of two in the line; the second is not recoverable) | 216 → 225 |
| RL-17 | line 1369 | The line “Production-affecting Live QA minimum is as follows.” (baseline line 1369) | NEW_CANON | C-26 (R-1, R-5, with the R-6 routing); support C-30; HDE Build Notes source reference | 51 → 4,005 |
| RL-18 | lines 2182–2183 | §5 playbook sub-heading “Steps” (baseline line 2183) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 112 → 114 |
| RL-19 | lines 2245–2246 | §5 playbook sub-heading “Tokens (names-only)” (baseline line 2246) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 112 → 115 |
| RL-20 | lines 2254–2255 | §5 playbook sub-heading “Failures to watch” (baseline line 2255) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 57 → 59 |
| RL-21 | lines 2262–2263 | §5 playbook sub-heading “Where it lives (titles-only)” (baseline line 2263) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 124 → 126 |
| RL-22 | lines 2279–2280 | §5 playbook sub-heading “Inputs” (baseline line 2280) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 151 → 153 |
| RL-23 | lines 2288–2289 | §5 playbook sub-heading “Scope” (baseline line 2289) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 75 → 78 |
| RL-24 | lines 2333–2334 | §5 playbook sub-heading “Evidence” (baseline line 2334) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 101 → 103 |
| RL-25 | lines 2341–2342 | §5 playbook sub-heading “Tokens (names-only)” (baseline line 2342) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 84 → 87 |
| RL-26 | lines 2377–2378 | §5 playbook sub-heading “Inputs” (baseline line 2378) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 80 → 82 |
| RL-27 | lines 2386–2387 | §5 playbook sub-heading “Scope” (baseline line 2387) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 26 → 29 |
| RL-28 | lines 2397–2398 | §5 playbook sub-heading “Steps” (baseline line 2398) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 93 → 95 |
| RL-29 | lines 2436–2437 | §5 playbook sub-heading “Evidence” (baseline line 2437) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 109 → 112 |
| RL-30 | lines 2501–2502 | §5 playbook sub-heading “Scope” (baseline line 2502) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 60 → 63 |
| RL-31 | lines 2511–2512 | §5 playbook sub-heading “Steps” (baseline line 2512) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 131 → 133 |
| RL-32 | lines 2536–2537 | §5 playbook sub-heading “Evidence” (baseline line 2537) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 130 → 132 |
| RL-33 | lines 2544–2545 | §5 playbook sub-heading “Tokens (names-only, FE pattern)” (baseline line 2545) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 95 → 98 |
| RL-34 | lines 2553–2554 | §5 playbook sub-heading “Failures to watch” (baseline line 2554) | DOC_HYGIENE | Defect: §5 playbook sub-heading flattened into a list (pattern stated at line 2157) | 57 → 59 |
| RL-35 | line 2559 | §5.4, Failures to watch, last item (baseline line 2559) | DOC_HYGIENE | Defect: stray bold on one list item | 111 → 107 |
| RL-36 | lines 3010–3011 | §5.8, Evidence, first two items (baseline lines 3010–3011) | DOC_HYGIENE | Defect: lost `<pair>` placeholder (form proved at lines 2971 and 2979) | 127 → 135 |
| RL-37 | line 3234 | §8, Gitignore rails for QA roots (baseline line 3234) | DOC_HYGIENE | Defect: lost `<epic-id>` placeholder | 282 → 292 |
| RL-38 | lines 3284–3285 | §9.1 sub-heading “9.1.2 Post-commit (general)” (baseline line 3285) | DOC_HYGIENE | Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading) | 68 → 70 |
| RL-39 | lines 3297–3298 | §9.1 sub-heading “9.1.3 Aux” (baseline line 3298) | DOC_HYGIENE | Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading) | 54 → 56 |
| RL-40 | lines 3302–3303 | §9.1 sub-heading “9.1.4 Catalog/A7” (baseline line 3303) | DOC_HYGIENE | Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading) | 51 → 53 |
| RL-41 | lines 3308–3309 | §9.1 sub-heading “9.1.5 CLI/API & SDKs” (baseline line 3309) | DOC_HYGIENE | Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading) | 60 → 62 |
| RL-42 | lines 3314–3315 | §9.1 sub-heading “9.1.6 Build/CI (PF09)” (baseline line 3315) | DOC_HYGIENE | Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading) | 58 → 60 |
| RL-43 | lines 3317–3318 | §9.1 sub-heading “9.1.7 App FE/BE (App QA docs)” (baseline line 3318) | DOC_HYGIENE | Defect: §9.1 sub-heading flattened into the glossary list (§9.1.1 at line 3280 is a heading) | 75 → 78 |
| RL-44 | line 3482 | §9.2.4, `QA_HARNESS_DISCIPLINE_OK` QA definition (baseline line 3482) | DOC_HYGIENE | Defect: lost placeholders (form proved at line 1952) | 160 → 179 |
| RL-45 | line 3485 | §9.2.4, `QA_HARNESS_DISCIPLINE_OK` evidence (baseline line 3485) | DOC_HYGIENE | Defect: lost `<epic-id>` placeholder (canonical path at line 1933) | 178 → 184 |
| RL-46 | lines 3593–3594 | §9.2.7, `CLI_ADMIN_BUNDLE_PARITY_OK` evidence (baseline lines 3593–3594) | DOC_HYGIENE | Defect: lost `<pair>` placeholder (form proved at lines 2971 and 2979) | 109 → 117 |
| RL-47 | line 3610 | §9.2.7, `ADMIN_BUNDLE_FULL_PAYLOAD_OK` evidence (baseline line 3610) | DOC_HYGIENE | Defect: lost `<pair>` placeholder (form proved at line 2971) | 192 → 196 |
| RL-48 | line 3748 | §9.2.13, `QA_HARNESS_DISCIPLINE_OK` evidence (baseline line 3748) | DOC_HYGIENE | Defect: lost `<epic-id>` placeholder (canonical path at line 1933) | 85 → 91 |
| RL-49 | line 3769 | §9.2.13, the note after the viability evidence list (baseline line 3769) | DOC_HYGIENE | Defect: lost placeholders (form proved at lines 1933 and 1952) | 199 → 225 |
| RL-50 | line 3903 | Required-elements checklist, the bullet “the completed final QA Report and separate RCA for every completed run” (baseline line 3903) | CONSISTENCY | C-26 (R-4 at the final QA Report and RCA) | 157 → 298 |
| RL-51 | line 4468 | §13, Complete flagged-unit classification ledger, row SRC-0292 (baseline line 4468) | DOC_HYGIENE | Defect: false statement about HDE Build Notes; current addenda referenced | 125 → 137 |
| RL-52 | lines 5221–5223 | §13.18, the second “Known non-goals” paragraph (baseline lines 5221–5223; line 5221 is kept) | DELETION | Defect: §13.18 repeats §13.17's non-goals paragraph (line 5223 equals line 5203) | 1,103 → 408 |
| RL-53 | line 5587 | §14.6, last row of the ownership table (baseline line 5587) | DOC_HYGIENE | Defect: list lead-in captured as a table row | 39 → 27 |

RL-03's source-rows field keeps revision 3's note that 2.2 R-3's first bullet is held with CCR-5 (H-06). In revision 4 that bullet is drained by RL-08 under the ruling, as the preparer's proof log §5.4 and §5.7 state. RL-03's payload is unchanged from revision 3, and the stale note does not affect it.

Basis, by group, as the preparer's proof log gives it:

* **C-07, HDE Build Notes 2.2 (RL-01, RL-03, RL-08).**
  * R-1: planning documents serve planning only. Nothing that executes, validates or is governed evidence binds a `docs/ephemeral/` path.
  * R-2: PF-Canon is resolved by stable identity and cited by title. The §10.8 version record is attribution only.
  * R-3's second bullet: the close-pack writer's test is a close-stage test.
  * R-3's first bullet (RL-08), drained under the Product Owner's CCR-5 ruling. The close-pack writer writes a close pack only at the close stage, at the end of a full work-unit cycle, after the authorized QA verdict and the closure decision exist. §3.1.3's second paragraph now makes the stage's entry a closure decision of `CLOSE` and removes the `DO_NOT_CLOSE` entry. The set is produced only after that decision confirms the close and never reopens implementation, QA or the closure decision. The exit is the Product Owner's merge of the close pull request, and the set is no longer a prerequisite that precedes the closure decision.
  * PF19 is the home because its §0.4.3 rules on change-process artifacts and its §2.2.11 CI-lane rules bear on the same subject. The drain follows GTWPE-D3 and Nathan's 2026-11-02 direction.
* **C-29, HDE Build Notes 2.16 (RL-04).**
  * R-1: GATE:CORE-DET evidence is the real compat path, that is, the five CI owner tests and the live compat test. The Reader goldens prove emission only.
  * R-2: the retired entries are not current proof.
  * PF19's home is §2.2.12, its determinism and AB↔BA rule. The gate's lists stay with HDE Governance.
* **C-26, HDE Build Notes 2.15 (RL-05 to RL-07, RL-09, RL-17, RL-50).**
  * R-1 to R-5, as applied in revision 2.
  * RL-07 and RL-17 also reference HDE Build Notes as the source of the Product Owner's direction.
  * Under the CCR-5 ruling, RL-07 lists the closure decision before the close mutation set result, in both §3.1.2's record list and its `MISSING` table.
* **C-18, HDE Build Notes 2.8 amendment (RL-10, RL-11, RL-14, RL-15).** The Epic close-run family and the Epic pointer, as applied in revision 2. Under the CCR-5 ruling, RL-10 (path grammar) and RL-14 (close-pack truthfulness) say the close-run family is written after the final QA verdict and the closure decision of `CLOSE`. The family's HDE Build Notes 2.8 name, "post-verdict", is kept, because it is still true.
* **Defects and inconsistencies (RL-02, RL-12, RL-13, RL-16, RL-18 to RL-49, RL-51 to RL-53).** These are Nathan's 2026-11-02 direction. Each fix is proved by PF19's own text (preparer's proof log §5.8):
  * 24 headings flattened by the export are restored (§3.4.12, seventeen §5 playbook sub-headings, §9.1.2 to §9.1.7);
  * eleven lines with lost placeholders are restored, each proved by intact text elsewhere;
  * the false SRC-0292 claim now references current HDE Build Notes addenda;
  * the duplicated §13.18 paragraph is deleted;
  * the stray §14.6 table row becomes a paragraph again;
  * one stray bold is removed;
  * the broken §1.4 example URL is replaced;
  * the §3.4.10 omission marker is aligned.
  * Placeholders PF19 cannot prove are left as they are and listed in the preparer's proof log §5.8.

Rows decided with no change: C-17, already represented (baseline l.742, l.782, l.1124, l.1146). Held and not applied: H-08 (CCR-6). H-06 (CCR-5) is released for this document by the ruling and drained in RL-08. The historical closure record at baseline line 5307 (output line 5408), which names a superseded `DO_NOT_CLOSE` decision, keeps its wording.

## 4. Metadata plan (document control)

| Field | Before | After | Derivation |
| :---- | :---- | :---- | :---- |
| Version | v3.0.7 | v3.0.8 | Final numeric component of the native dotted version incremented once |
| Effective date | 2026-10-26 | 2026-11-02 | Actual application execution date, native `YYYY-MM-DD` format |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` | `BN 14.0.5` | The package records one source file, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`. The Product Owner's direction is not a source file. |
| Status | Canon | Canon (unchanged) | Not stale |
| Title, Invocation tag | unchanged | unchanged | Not authorized to change |

The header's labels, order and trailing spaces are preserved. No internal restatement of the document's own version or date exists outside the header. PF19 has no change-log section, so no history entry is required. The metadata spans (lines 7–9) do not overlap any content operation; the first content operation starts at line 138.

## 5. Validation and preservation

Before any edit, the whole batch and the metadata plan were validated against the unchanged original, independently of the preparer's tools. The package was parsed from the committed file, and each old block's count and span, the operation spellings, the payloads and the conflicts were checked. Nothing was rejected.

The edits were applied by original offsets, in descending order, on raw UTF-8 with LF line endings, with no rematching against changed text.

Preservation audit (offset-based, whole document):

* 57 untouched original intervals totalling 669,594 bytes are byte-identical in the output at their shifted offsets. The 56 consumed spans total 11,876 bytes. Together they account for all 682,678 original bytes.
* Each of the 56 payloads (53 content, 3 metadata) is present exactly at its planned output offset.
* Headings: the 269 original headings are preserved in order with their text and level. The only additions are the 24 planned restorations, for 293 in all.
* Code-fence count is unchanged. Table lines went from 204 to 212: the new nine-line `MISSING` table in RL-07, less the stray §14.6 row (RL-53).
* The final LF is preserved, and no CR was introduced.
* No `Draft` status language about the document, placeholder marker, TODO, drafting note or editorial comment was added; the marker counts are unchanged. No ASCII triple-dot or Unicode ellipsis was added.
* "No Epic close-run family is admitted" and "has no current addenda" no longer occur.
* `DO_NOT_CLOSE` now occurs only in the historical closure record at output line 5408. No passage puts the close pack or close mutation set before the closure decision.
* Independent cross-check: the output with its original three header lines restored has SHA-256 `d90aa4c1a0b4fea1330b8d53da9f2ece2a8646ffa1d5994886b2650d96206da2`, exactly the preparer's recorded simulation of revision 4.
* The saved file was read back in full and compared byte for byte with the produced output: identical.

These are text checks, not product QA.

## 6. Limitations and next action

* The revised PF is a reviewable output under `docs/ephemeral/`, not canon. Publishing it to `docs/pfcanon/` is Nathan's manual action, and no `docs/pfcanon/` file was edited.
* H-08 (CCR-6) stays held. This application does not touch it.
* RL-03's source-rows field in the package keeps a stale revision-3 note (§3). Correcting it needs a new preparation revision, and its payload and this output would not change.
* PF19 still contains lost placeholders whose original text it does not prove. The preparer's proof log §5.8 lists them, and recovering them needs Nathan's original wording.
* No QA, Ops or product test was run. The pre-push check classifies the change as documentation-only, which starts no hosted CI. Its result is not CI, QA or governed evidence.
* Next manual action: Nathan reviews draft PR [amthorn78/glow-hdengine-v2#826](https://github.com/amthorn78/glow-hdengine-v2/pull/826) and decides whether to publish PF19 v3.0.8. Nathan merges.

## 7. Save verification

* Revised PF: saved at the path in §1, read back completely, and identical to the verified output.
* This proof log: saved beside it and read back. It records no hash of itself.

## 8. Supersession

This application replaces the earlier v3.0.8 output and its proof log, which were applied from preparation revision 3 at commit `376b9f4afa3dbe950d39b71bb3f15be3573d68c8` (SHA-256 `910a547a48cca507c6c254b16e62a0c0838c33e50853e8795e43b4d995baec53`). That output had itself replaced the revision-2 application at commit `e56a1833c1e175e9178eee7cde5558ebe3e10c8b` (SHA-256 `5d44bfc0328f6e4dbd14f0d44499d4dd5731ed67bd29747336c022a92036cedd`). All belong to the same run, T-06, and keep the same file names. The earlier bytes remain in the branch history at those commits. The version is v3.0.8 in each, because each is one increment from the v3.0.7 baseline.

Against the revision-3 output, this output differs only in the four passages the ruling changes: §3.1.2 (RL-07), §3.1.3 (RL-08), the path-grammar row (RL-10) and the close-pack truthfulness paragraph (RL-14).
