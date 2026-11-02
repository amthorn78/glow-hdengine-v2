# Proof log — PF19-Canon-Glow-QA-Guide v3.0.8 (application) — gtwpe-20261101-pf10-v14-0-5 (T-06)

This is the application report for `PF19-Canon-Glow-QA-Guide-v3.0.8.md`, in this directory. It records how that revised PF was made from the v3.0.7 baseline and the validated redlines package, what changed and on what basis, and what was verified. The revised PF is not an authoritative publication: `docs/pfcanon/` is unchanged.

## 1. Artifact and outcome

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF19/PF19-Canon-Glow-QA-Guide-v3.0.8.md` |
| Artifact identity | 690,272 bytes; 5,674 lines; SHA-256 `5d44bfc0328f6e4dbd14f0d44499d4dd5731ed67bd29747336c022a92036cedd`; git blob `4aa22d07fe9b45e1850c16a12796f8be9c9f080d` |
| In-document identity | Title PF19-Canon-Glow-QA-Guide; Status Canon; Version v3.0.8; Effective date 2026-11-02; Last Update Gate `BN 14.0.5`; Invocation tag `INV-f2ac55d77ce9aacc` |
| Applier | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b` (fetched live when this step began; page state 2026-10-09T11:05:22.207Z), run in the same Claude Code session Nathan started for T-06, after the TW-DRAIN-10 step, as his handoff authorizes. No subagent, reviewer or other session was used. |
| Application outcome | Applied: ten content operations and a three-field metadata plan; zero rejected |
| Execution date | 2026-11-02 (UTC; started 2026-11-02T00:37Z) |

## 2. Inputs and identities

| Role | Identity |
| :---- | :---- |
| Original baseline | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.7.md` on `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`; v3.0.7; git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b`; raw-byte SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; 682,678 bytes; 5,622 lines. This is the preparer's recorded baseline, which is identical at the handoff baseline `e2b7427ff418ca8f08f05587c4a541308a76da56`. The fingerprint was compared byte for byte in the same raw representation. |
| Redlines package | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF19/PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.md`, preparation revision 2, at commit `533841af` on `claude/gtwpe-triage-authoring-j94ewf`; SHA-256 `480d35dcbca1916e04208212103fb02dbe334a082285577997c85664150c83e2`, matching the preparer's proof log |
| Preparation proof log | `PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, same directory and commit |
| Preparer | TW-DRAIN-10 100926.1, the preparation step of this same session; run `gtwpe-20261101-pf10-v14-0-5` T-06, preparation revision 2; outcome `READY` / `COMPLETE_PACKAGE`, with no unresolved or blocking item. Revision 1 (commit `137e98f`) was superseded by the preparer before any application. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, unchanged on `main`. Selected units: 2.8 lines 1063–1106 and 1111–1127; 2.15 lines 1650–1804; 2.2 lines 517–551; 2.16 lines 1869–1939. These match the handoff and the ledger. Supporting reading as the preparer records it. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-06; rows C-17, C-18, C-26 (assigned), C-07, C-29 (uncertain), C-20, C-30 (supporting) |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, read completely in this session |

Intake verification. The complete original, the complete package and the complete preparation proof log were read. The preparation proof log records:

* complete target coverage, in eighteen windows that sum to 682,678 bytes;
* complete selected-source coverage;
* every change accounted for;
* the held items H-06 and H-08, with what each waits for;
* producer validation with a one-pass simulation;
* `READY` / `COMPLETE_PACKAGE`.

The original on `main` at application time is byte-identical to the preparer's baseline, so no drift needed reconciling.

## 3. Operation ledger and basis

Every content operation is a `REPLACE` of one whole baseline line, expected and observed exactly once. The rationale and source references below are the preparer's (its proof log §5.2 and §5.3).

| ID | Baseline line and location | Change type; source rows | Basis |
| :---- | :---- | :---- | :---- |
| RL-01 | 436, §2.3 first paragraph | CONSISTENCY; C-26 (R-1, R-2 context) | 2.15 R-1 (every Epic's QA runs the live compat test) and R-2 (only the Product Owner may waive it). Adds that, for an Epic, the Product Owner's rails posture always includes the open-rails live compat test unless he records a waiver, so §2.3 cannot be read as allowing a closed-rails-only acceptance without one. |
| RL-02 | 503, §3.1.1 paragraph after the assessment table | NEW_CANON; C-26 (R-2) | 2.15 R-2: an agent's finding that the surfaces are not live, or that the test cannot run meaningfully, is a question put to the Product Owner as a named decision no later than QA-10 readiness, and the QA Plan is not approval-ready until he answers. Placed in §3.1.1, the QA-10 home. |
| RL-03 | 511, end of §3.1.2 | NEW_CANON; C-26 (R-4, R-3, R-2 waiver form); support C-30 | 2.15 R-4: the `Live test:` line with `RAN`, `WAIVED` or `MISSING` in the eight listed records; the MISSING effects table; no agent override; prompts apply it. R-3: "Live QA" is reserved, other QA is "closed-rails QA", and a report without the test says "No live test ran." in its first line. R-2: only the Product Owner may waive; the waiver is written and change-specific, quotes his words with their date, and carries HDE Governance's exemption content; what is not a waiver. All of it is scoped to Epics, with the CRD question left open. |
| RL-04 | 638, §3.4 introduction | NEW_CANON; C-26 (R-1, R-3, R-4 routing) | Routes §3.4's execution pattern to the §3.5.5 minimum and the §3.1.2 line and name rules, so that following the pattern cannot be taken to make a check live. |
| RL-05 | 742, §3.4.3 path-grammar row | CANON_UPDATE; C-18; C-17 context; support C-20 | 2.8 decision 7 and the stated limit (an admitted Epic has the same close-run family; HDE-EPIC041 is the one Epic admitted; another Epic needs its own admission), and the 2026-11-01 amendment note (l.1127). Replaces the false "No Epic close-run family is admitted". Repository facts were inspected read-only (preparer's proof log §4). |
| RL-06 | 782, §3.4.3 approved exception 5 | CANON_UPDATE; C-18; support C-20 | As RL-05: adds the admitted Epic's close-run family beside the CRD's. |
| RL-07 | 1124, "Close-pack truthfulness and same-run execution" | CANON_UPDATE; C-18; C-17 context; support C-20 | As RL-05: the home of same-run close evidence for an admitted CRD or Epic. Replaces the false "No Epic close-run family is admitted". |
| RL-08 | 1146, "Close report requirements" | CANON_UPDATE; C-18 (B-2); C-17 context; support C-20 | 2.8 stated limit (l.1100), B-2: an Epic's source may point to its own close-run directory before the close run writes it, and only a CRD must. The writer at `tools/qa/generate_epic_close_pack.py` lines 2635–2655 on `main` was inspected. |
| RL-09 | 1369, §3.5.5, before "Production-affecting Live QA minimum" | NEW_CANON; C-26 (R-1, R-5, R-6 routing); support C-30 | 2.15 R-1, in full: live vendor compat and its pass predicates; the deployed-service check; SYN-A and SYN-B as Ops-stored synthetic fixtures, registered and stored per 2.16 R-3 (C-30); the Epic's own live surfaces; what does not satisfy the test. R-5: a test that cannot run is `TOOLING_BLOCKED` and never becomes a PASS, a waiver or a closure. R-6 is applied by routing to the subsection's existing execution controls. The production-affecting rules stay as additions, and the CRD question stays open. |
| RL-10 | 3903, §9.2.15.6 required-elements checklist | CONSISTENCY; C-26 (R-4) | 2.15 R-4 requires the line in the final QA Report and RCA, so the closeout checklist confirms its presence and value. |

Rows decided with no change, as the preparer records them:

* C-17: already represented at baseline l.742, l.782, l.1124 and l.1146.
* C-07: no PF19 requirement falls within the l.525 scope; the locations are in the preparer's proof log §5.4.
* C-29: PF19 states no GATE:CORE-DET evidence; there are zero occurrences of the gate or the retired entries (preparer's proof log §5.5).

Held and not applied: H-06 (CCR-5, §3.1.3, unchanged) and H-08 (CCR-6, §3.4.3 and §3.4.8 tension).

## 4. Metadata plan (document control)

| Field | Before | After | Derivation |
| :---- | :---- | :---- | :---- |
| Version | v3.0.7 | v3.0.8 | Final numeric component of the native dotted version incremented once; prefix and component count kept |
| Effective date | 2026-10-26 | 2026-11-02 | Actual application execution date, native `YYYY-MM-DD` format |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` | `BN 14.0.5` | The package records one source, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, so the gate is `BN` and that file's version |
| Status | Canon | Canon (unchanged) | Not stale: PF19's classification is Canon |
| Title, Invocation tag | unchanged | unchanged | Not authorized to change |

The header's labels, order and the two trailing spaces on each line are preserved. A whole-file search found no internal restatement of the document's own version (`v3.0.7`) or date (`2026-10-26`) outside the header, so nothing else needed synchronizing. PF19 has no change-log or revision-history section, so no history entry is required, and the package carries none. The metadata spans (lines 7–9) do not overlap any content operation; the first content operation is at line 436.

## 5. Validation and preservation

Before any edit, the whole batch was validated against the unchanged original, independently of the preparer's tools: the package was parsed from the committed file, and each old block's count and span, the operation spellings, the payloads and the metadata spans were checked. The plan had no conflicts. Nothing was rejected, so the application went ahead.

The edits were applied by original offsets, in descending order, on raw UTF-8 with LF line endings, with no rematching against changed text.

Preservation audit (offset-based, whole document):

* 14 untouched original intervals totalling 677,289 bytes are byte-identical in the output at their shifted offsets. The 13 consumed spans total 4,181 bytes. Together they account for all 682,678 original bytes.
* Each of the 13 payloads (10 content, 3 metadata) is present exactly at its planned output offset, and each content payload occurs exactly once in the output.
* The heading set is unchanged (269 headings). Code-fence count is unchanged. Table lines rose from 204 to 213, which is the new nine-line `MISSING` table in RL-03. The final LF is preserved, and no CR was introduced.
* Status and drafting markers: no `Draft` status language about the document, and no placeholder, TODO, drafting note or editorial comment was added (marker counts unchanged). No ASCII triple-dot or Unicode ellipsis was added.
* Independent cross-check: the output with its original three header lines restored has SHA-256 `5ef9cfd6e957e438582177c8329d644499c4c2c7b7ef02050cdb63b4ef43cafb`, exactly the preparer's recorded one-pass simulation of the content redlines.
* The saved file was read back in full and compared byte for byte with the produced output: identical.

These are text checks, not product QA.

## 6. Limitations and next action

* The revised PF is a reviewable output under `docs/ephemeral/`, not canon. Publishing it to `docs/pfcanon/` is Nathan's manual action, and no `docs/pfcanon/` file was edited.
* No QA, Ops or product test was run. The repository's pre-push check classifies this change as documentation-only, which starts no hosted CI run. Its result is not CI, QA or governed evidence.
* Next manual action: Nathan reviews draft PR [amthorn78/glow-hdengine-v2#826](https://github.com/amthorn78/glow-hdengine-v2/pull/826), which carries this output, and decides whether to publish PF19 v3.0.8. Nathan merges.

## 7. Save verification

* Revised PF: saved at the path in §1, read back completely, and identical to the verified output (SHA-256 above).
* This proof log: saved beside it and read back. It records no hash of itself.
