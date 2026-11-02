# Proof log — PF06 redlines package r2, gtwpe-20261101-pf10-v14-0-5

This is the processing report for `PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md`, which sits beside it in `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/`. Package r2 is complete and supersedes package r1. This log stands on its own; where it repeats r1 facts, it says so.

## 1. Artifact, identity and lineage

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-03 / package revision `r2` |
| Supersedes | Package `r1`: `PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.md` and its `.proof-log.md` (commit `7e710d5c5a69617f896fb1db8bb07ad515491e0f`), applied as `PF06-Canon-Change-Process-Guide-v2.5.6.md` in commit `ac5870fe2d8466fbad791c61f3b72011d9dfd37f` (SHA-256 `8dc7b239df9200f3596efa9fc72fe001ab2b5685db037c4e111472e90f869692`). The r1 files stay in place as the record of the first preparation. r1 was not defective as applied; r2 widens it under the decisions in section 2. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`. Re-fetched live when the r2 step began on 2026-11-02; page last edited 2026-10-09T11:05:22.094Z, the same as for r1. |
| Originating preparer | The T-03 document session: a Claude Code session on `amthorn78/glow-hdengine-v2`, session `session_01Q789tyV3UxPrkptsceraud`, started by Nathan. No subagent, reviewer or other session took part. |
| Preparation outcome | `READY` |
| Save outcome | `COMPLETE_PACKAGE` (section 11) |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 |

## 2. Decisions applied

| Decision | Source | Effect on r2 |
| :---- | :---- | :---- |
| Nathan's instruction, in this session, 2026-11-02, after reading the r1 report: "fix the defects and inconsistencies you noticed" | This conversation | Authorizes repairing the defects and inconsistencies r1 recorded as observations O-1 to O-4. TW-DRAIN-10 requires Nathan's authorization for DOC_HYGIENE; this is that authorization, quoted here so it is in an accessible file. |
| GTWPE-D3, "Every PF10 addendum is drained, and a prompt in the run evaluates the drain targets" | `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md` (blob `1c65c85339cb0dc3fc438cc8a0e7509257b43be4`, the same on `main` and the branch), lines 114–170, read in full. Nathan, 2026-10-07: "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target." The ledger's 2026-11-02 correction banner quotes it. | The selected units are mapped onto PF06 by context and scope, not only onto the sections the ledger named. r1 drained 2.15 into §3.5.2.8 only and left R-2, R-3, R-5 and R-6 to other tasks; r2 drains them where PF06's own text bears on them. |
| The Product Owner's CCR-5 ruling, 2026-11-02: "close pack should go after the decision to close is confirmed" | Recorded in the T-07 preparation proof log, `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, section 2. That log records that the ruling chooses CCR-5 alternative (A): R-3 stands, the closure decision precedes the close-pack write, and the permanent documents drain to match. It also records that the ruling bears on Change Process Guide §3.5.1 (its observation O-1). | The T-03 handoff had said "the alternative (A) drain of §3.5.1 is not authorized". That was before the ruling. |
| The Product Owner's answer in this session, 2026-11-02 | The question was whether T-03's corrected package should also drain (A) into §3.5.1. Answer: "Yes, drain (A) into §3.5.1 (Recommended)" | H-06 is released for this document. RL-40 drains (A) into §3.5.1, worded like Plan Templates §3B as revised under the same ruling (T-07 RL-16 to RL-18). |

## 3. Target

| Field | Value |
| :---- | :---- |
| Path | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.5.md` |
| In-document title | `PF06-Canon-Change-Process-Guide` (Change Process Guide), version `v2.5.5` |
| Baseline | `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; git blob `e9f4d7d6146364f7c59ed360990d8c4ec633a59f`. Current `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` carries the same blob, so there is no drift. |
| Bytes | SHA-256 `d046d7eeed6eee029b63392bc32cd67d9073f7c31ff9676a0448c11a2bce21c2`; 439,442 bytes; 4,684 lines; UTF-8, LF only |
| Coverage | Read completely in this session in eleven recorded windows (r1 proof log section 4: lines 1–65, 66–494, 495–848, 849–1426, 1427–1995, 1996–2521, 2522–2923, 2924–3274, 3275–3799, 3800–4432 and 4433–4684, summing to 439,442 bytes). The same verified bytes were reused for r2; nothing changed. |

Document-control block for TW-APPLY-10's header derivation (lines 1–13), unchanged from r1:

* Title `PF06-Canon-Change-Process-Guide` (line 3).
* Version `v2.5.5` (line 5).
* Status `Canon` (line 7).
* Effective date `2026-10-26` (line 9; label written `**Effective date**:`).
* Last Update Gate `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` (line 11).
* Invocation tag `INV-f2ac55d77ce9aacc` (line 13).

The document has no change log or revision history section, so no history-entry redline is prepared. No redline touches the header.

Source-file header provenance, in source order: 1. `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5. This is the only change source. The decisions in section 2 decide conflicts and authorize hygiene; they are not source files, and they do not enter the Last Update Gate.

## 4. Sources and inputs

| Role | Identity | Read |
| :---- | :---- | :---- |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5; blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines | Selected units, read completely: 2.2 lines 517–588; 2.8 lines 1048–1145; 2.15 lines 1650–1804. Supporting, read completely: 2.9 lines 1146–1229; 2.16 R-1 to R-3, lines 1919–1948; 2.1 D-5, lines 451–490 (for the context check in section 7); 2.5 line 856 (the CCR-5 alternatives). |
| Editorial standard | PF03-Reference-Technical-Writing-Best-Practices v1.8.8, blob `504712df548a02f3aa4e7b8c37027385e46a3878` | Whole document |
| Decision record | GTWPE decision record, as in section 2 | GTWPE-D3, lines 114–170 |
| Ledger (routing only) | `LEDGER.md`: the handoff pin `142feb3`, and the branch head `7b84281` read for the 2026-11-02 correction banner, §8 and the H-06 to H-08 rows | The T-03 rows are unchanged by other sessions |
| Ruling record | T-07 preparation proof log and redlines (PF27), as in section 2 | Section 2 and RL-16 to RL-18 of that package |
| Supporting canon | HDE Governance §3.4 (lines 1171–1210); Plan Templates heading "Tracked Issues" (line 1647) | As for r1 |
| Supporting repository record | `docs/run/EPIC011_TEST_IDENTITIES.md` (SYN-A and SYN-B), unchanged since the baseline | As for r1 |

## 5. Redlines in r2

| IDs | Kind | Lines | Change |
| :---- | :---- | :---- | :---- |
| RL-01, RL-02, RL-04, RL-05, RL-06 | Carried from r1, byte-identical | 3004, 3011, 3195, 3200, 3348 | As r1 (r1 proof log sections 5 and 6) |
| RL-03 | Carried from r1, INSERT payload extended | gap after 3182 | r1's live compat test, live-test line and MISSING table, plus: the waiver's form and the rule that an agent's non-applicability finding is a named question to the Product Owner no later than QA readiness (R-2); a blocked live test is `TOOLING_BLOCKED`, the Epic waits and nothing converts it to PASS, waiver or closure (R-5); and the reserved name "Live QA", "closed-rails QA" and the report's first line "No live test ran." (R-3) |
| RL-09 | CONSISTENCY (O-3) | 600 | The separate QA RCA file is `audit/<prefix>_QA_RCA.md` with the close report's own prefix: the epic form and the CRD form |
| RL-19, RL-36 | CONSISTENCY (O-1) | 1106 (§0.6.2), 1843 (§1.1.5A) | Every Epic's QA plan includes the live compat test in §3.5.2.8, whatever the Epic changed. §1.1.5A governs only the open-rails proof of the Epic's own surfaces; none of its findings or exemptions applies to the live compat test, which only the Product Owner may waive. |
| RL-40 | CONSISTENCY (CCR-5 alternative (A)) | 2954–2960 (§3.5.1) | The close-mutation-set stage follows the closure decision. Entry: a closure decision of `CLOSE`, the close mutation set and close pack written only after it. Exit: the Product Owner's merge of the close PR. The stage starts only after the closure authority has decided to close and does not revisit that decision. "What it owns" and "What it never does" are reproduced unchanged. The `DO_NOT_CLOSE` entry is removed, for the reason T-07 gives: it existed only for a closure decision that judged a missing, incomplete or defective close mutation set, which the closure decision no longer does. |
| RL-07, RL-08, RL-10 to RL-18, RL-20 to RL-35, RL-37 to RL-39, RL-41 to RL-49 | DOC_HYGIENE (O-4) | 402–403, 544, 677–678, 963–964, 967–970, 975–976, 983, 995, 997, 1006–1007, 1010, 1147, 1164, 1170, 1197, 1251, 1255, 1263, 1283, 1572, 1579, 1585, 1587–1588, 1602, 1608, 1765, 1837, 1913, 2121, 2883–2884, 2992–2995, 2997, 3201, 3212, 3242, 3257, 3352, 3755, 4212 | 48 damaged placeholders in path patterns restored, as described below |

The O-4 placeholder repairs (RL-12 and RL-41 are widened upward with unchanged context lines, because lines 969–970 and 2994–2995 are otherwise identical):

* `audit/EPIC-\\` becomes `audit/EPIC-\<NNN\>`.
* `hde-epic\\` becomes `hde-epic\<NNN\>`.
* The epic-number definition (lines 963–964) and the §3.5.2.1 sentence at line 2997 become `\<NNN\>`.
* `audit/qa//` and `audit/qa/\\/` become `audit/qa/\<epic-id\>/`; `audit/ops/\\/` becomes `audit/ops/\<epic-id\>/`.
* A second path variable after the epic directory becomes `\<SUBPATH\>`.
* `checks/\\` becomes `checks/\<check\_id\>`.

Each `\\` is what remains of an escaped `\<VAR\>` once the `<VAR>` was stripped. Each repair restores `\<VAR\>` in the line's own escaping style.

The variable names come from the target itself:

* `audit/qa/<epic-id>/<SUBPATH>` (line 1906);
* `audit/qa/<epic-id>/logs/` (line 1415);
* `audit/EPIC-<NNN>_QA_RCA.md` (line 600) and the epic `EPIC-NNN` form (line 2999);
* §0.5.1's definition of the shorthand QA root as the epic QA root, with its example `audit/qa/hde-epic022/` (lines 995–997);
* the `check_id` field of the step-logs manifest (line 1257).

The validator proves every DOC_HYGIENE redline changes nothing but those placeholders (section 9).

## 6. Change and disposition ledger (changes from r1)

r1's ledger (r1 proof log section 6) stands for C-10, C-17, C-18 and C-07, with these additions.

* **C-26, 2.15 R-2** (l.1741–1753): drained by context into §3.5.2.8 (RL-03 waiver and question rule), §0.6.2 and §1.1.5A (RL-19, RL-36). The waiver's required content is routed to HDE Governance §3.4, which already requires an exemption's reason, authorizing owner, accepted risk, substitute proof, withheld claim and future obligation (line 1200).
* **C-26, 2.15 R-3** (l.1755–1759): drained into §3.5.2.8 (RL-03). PF06's existing use of "Live QA" for the required QA stage of every Epic is consistent with R-3, because that stage now always includes the live compat test.
* **C-26, 2.15 R-5** (l.1787–1790): drained into §3.5.2.8 (RL-03).
* **C-26, 2.15 R-6** (l.1792–1804): routed in RL-03 "Other controls" to HDE Governance §3.4, as in r1.
* **C-07/C-09, 2.2 R-3 first bullet** (l.549): drained into §3.5.1 under CCR-5 (A) (RL-40). R-3's second bullet, that the writer's test is a close-stage test and not ordinary required CI, is already represented at §0.2 "Automated CI budget control" (line 187: "Epic-closeout preparation or validation MUST NOT become ordinary required PR CI unless a specific control independently protects the merge boundary").
* **O-3, 2.8 decision 4 and the stated limit on the QA RCA path:** RL-09.
* **O-5 (r1):** not a defect. It recorded that RL-03 routes waiver content to HDE Governance §3.4, which carries it. No change.

## 7. Context checks with no change

* **2.16 R-2 retired evidence entries:** no PF06 change. A de-escaped search of PF06 found none of `make_compat_determinism_artifacts`, `IDENTITY_OK.txt`, the three retired CI jobs or the `abba_compare` logs as evidence entries. PF06 §4.5 lists `artifacts/cli/showcompat/preimage_recompute.log` and `two_run_identity.log` (lines 3724–3725), which R-2 does not retire. The identity token names in §4.1 (lines 3466–3541) are template requirement families, not GATE:CORE-DET evidence entries. `CORE-DET` and `compat_public` do not occur.
* **2.1:** no PF06 change. `--allow-prod-vendor`, `PROVIDER_ROUTE_UNSUPPORTED`, "legacy BodyGraph", `/api/compat/v1` and `build_release_attestation` do not occur. D-5's row-content rule for governed gate rows belongs to HDE Governance §2.0.10 and HDE Schemas and Artifacts §1.2. PF06 §1.1.10.4 (lines 2124–2154) validates the canonical JSON gate family's location and pass records and does not conflict.
* **§0.6.4 "PO Live QA vendor-first scope":** no change. This corrects r1's observation O-1, which named §0.6.4 among the sections that tie live testing to a production finding. On re-reading, §0.6.4 governs only what belongs in a Product Owner-run session's workload; it does not make the minimum live test conditional.

## 8. Held items and remaining defects

Held items:

* **H-06, CCR-5:** released for §3.5.1 by the decisions in section 2 and drained as RL-40.
* **H-07, CCR-1:** still held. The acceptance-map wording is unchanged.
  * The acceptance-evidence bullets (lines 3006–3010) are untouched.
  * In the close-pack file list (lines 2992–3002), RL-41 and RL-42 change only the damaged `<NNN>` placeholder in the two file names and in the "Where `<NNN>` is" sentence; the list of files is unchanged.
* **H-08, CCR-6:** still held. §0.7 (lines 1397–1426) is untouched. In the §3.5.2.8 "Live QA evidence landing" paragraph (lines 3240–3249), RL-45 changes only the damaged placeholders on line 3242.

Remaining defects, not repaired:

* **Damaged template field values.** 161 `\\` occurrences remain on 126 lines. All but one are template field values whose names neither the target nor any source establishes: the review-pack and evidence-print templates, the machine headers in §2–§4, the Asset Draft Pack, the ADR template in §0.6.1 (line 1082) and the Canceled Notes line in §6.4. PF03 §7 allows formatting repair only where the complete source establishes the intended text, and these names are not established. Repairing them would mean inventing placeholder names. Also not repaired:
  * line 265 ("would fit at" a path);
  * the command examples at lines 1814 and 1826–1827;
  * the harness example `--epic` at line 3199;
  * the template headings at lines 3670 and 3834, which also fall under PF03's heading protection;
  * the YAML profile rule at line 2592.

  The one exception is the code capsule `canon_serializer_v1` (line 2546), whose `"\\n"` is legitimate escaped code.
* **Line 4617** (Appendix C, a deliverable-path example made of `audit/qa/` and three damaged placeholders). Its third path variable is not attested anywhere, so a two-variable repair would change the example. It is left as is.

Knock-on of CCR-5 (A), for the CCR-6 disposition (not drafted): the H-08 landing paragraph lets Live QA evidence land "inside the epic close mutation set" (line 3247). Under (A) the close mutation set follows the closure decision, so that route would place QA evidence after the decision it supports. Glow QA Guide §3.1.3 (T-06) still states the old order.

## 9. Validation

The validator is `validate_redlines_r2.py`, a scratchpad script that is not committed. It parses the saved r2 file and compares it with the committed r1 file. Every check listed for r1 passed again:

* counts, line-start alignment, LF termination and spans inside their sections;
* non-overlap, insert-gap conflicts and a one-pass simulation;
* each payload present once;
* no ellipsis form, no Build Notes addendum or version citation, and no PF file name in new prose;
* no drafting marker;
* heading inventory, front matter and end-of-file shape unchanged.

New checks for r2:

* RL-01, RL-02, RL-04, RL-05 and RL-06 are byte-identical to r1, and RL-03 differs.
* Every DOC_HYGIENE redline is placeholder-only. Removing the restored tokens from REPLACE, and `\\` from both blocks, yields identical text. No damaged `\\` is left in any hygiene payload.
* §0.7 (lines 1397–1426) and the H-07 acceptance-evidence bullets (lines 3006–3010) are untouched.
* Inside the H-07 file list (lines 2992–3002) and the H-08 landing paragraph (lines 3240–3249), only DOC_HYGIENE redlines occur: RL-41 and RL-42, and RL-45.
* The old ordering sentence "It sits between the final QA Report and the closure decision" is absent from the simulated output.
* New inserted prose uses no gendered pronoun.
* Damaged path tokens: 48 before, 1 after (line 4617).

Result: `RESULT PASS: 49 redlines; 48 REPLACE; 1 INSERT; no overlap; strict held spans untouched`. The simulated output is a validation product only.

## 10. Constraints and interpretations

* GTWPE-D3 widens mapping by context and scope inside the selected units and the target. It does not let this task edit another document. Glow QA Guide §3.1.3 belongs to T-06.
* RL-40 follows the ruling's own words and T-07's §3B wording, so the two documents state one order.
* Restored placeholders are written as backslash-escaped `\<VAR\>`, matching each line's existing escaping, so that Markdown renders them rather than hiding them as HTML tags.

## 11. Save and completion receipt

| File | Repository path | Verified |
| :---- | :---- | :---- |
| Redlines r2 | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` | Read back completely from this path by the validator, which parsed all 49 redlines and re-ran every check; SHA-256 `dea4fe28ba9e19aa4d09c396e0c6a329eef7da49504d6d3f2ddb528b90ce6aae`, 88,712 bytes, 1,350 lines; revalidated from this path: PASS; simulated output SHA-256 `ee2a078c897209d319d09fd5a100afaa491974410e0ece141e59807a555aca36`, identical to the pre-save simulation |
| Proof log r2 | This file, beside the redlines file | Read back in full after writing |

Both files agree on the original and source identities, the preparer, the run identity `gtwpe-20261101-pf10-v14-0-5` package `r2`, and the outcome `READY`. Save completeness: `COMPLETE_PACKAGE`.

Next step: TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`), run in this session against the original above and this package. The expected output is `PF06-Canon-Change-Process-Guide-v2.5.6.md` with its proof log, replacing the r1 output of the same name in the same run namespace; the application report records the supersession. A diagnostic returns to this preparer.
