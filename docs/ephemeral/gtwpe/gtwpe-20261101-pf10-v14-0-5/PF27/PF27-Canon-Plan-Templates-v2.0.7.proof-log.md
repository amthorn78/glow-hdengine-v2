# Proof log: PF27-Canon-Plan-Templates v2.0.7, application of run gtwpe-20261101-pf10-v14-0-5 (task T-07)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.7.md`: the complete revised PF27, in-document title `PF27-Canon-Plan-Templates`, version v2.0.7, Status Canon, Effective date 2026-11-02, Last Update Gate `BN 14.0.5`; 331,957 bytes; 3,980 lines; SHA-256 `dbbea67326c03ad925b54b50e25c6a4b22b1d75b7d8a447dfa1a4358a650325f`; LF endings |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.7.proof-log.md` |
| Application run identity | `gtwpe-20261101-pf10-v14-0-5/T-07/apply-r1` (first application; no earlier T-07 final output existed) |
| Applier | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when this step began (page last edited 2026-10-09T11:05:22Z), run in the same Claude Code cloud session as the preparation, https://claude.ai/code/session_01Q789tyeqMDbVqbUtqxA64b, under Nathan's handoff of 2026-11-02, which authorizes both steps in sequence |
| Outcome | Applied. Fifteen content operations and three document-control operations; no diagnostic. |
| Standing | Working output under `docs/ephemeral/`. It is not authoritative publication: `docs/pfcanon/` is unchanged, and moving this text into canon is Nathan's action. It establishes no QA verdict, acceptance, Ops, deployment or closure. |

## 2. Inputs

| Input | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.6.md`, v2.0.6, git blob `c21096d78b9865bf5aa0c531eee701e462d71a50`, SHA-256 `850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00`, 323,765 bytes, 3,938 lines. Read from `origin/main` at `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` when this step began; byte-identical to the preparation baseline at `e2b7427ff418ca8f08f05587c4a541308a76da56`. No drift. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.md`, as pushed in commit `bf5bb08`; 45,443 bytes; SHA-256 `e547b3353dbaae69d8bd86d740d759da957204c1683a4ec61248997e3bf69212`; fifteen redlines; ends with `END OF REDLINES` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.6.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, commit `bf5bb08`; SHA-256 `b7613838e89715f81ce1aa5e08414ce5d4bee9ec47ae4bbff269a3f10216b3d0` |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; same blob on `origin/main` `84d6d1ca` |
| Selected source units | 2.1 D-2, lines 277–344 (C-02), with context lines 205–224 and 491–516 (C-06); 2.2 status and R-2, lines 517–546 (C-08); 2.2 R-3, lines 547–551 (C-09); 2.15 status and R-1 to R-6, lines 1650–1804 (C-26). Read completely in this session. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-07; rows C-02, C-08, C-09, C-26; supporting C-06 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` (blob `504712df548a`), read in full in this session |

## 3. Intake and preparation-state verification

* Preparer: TW-DRAIN-10 100926.1 in this same session; run `prep-r2`, which supersedes the session's own `prep-r1` (the parent commit, never given to Apply). The preparation proof log records the correction (its §12).
* Preparation outcome `READY`; save completeness `COMPLETE_PACKAGE` (preparation proof log §13). No unresolved blocking item. H-06 and H-07 are held and not drafted; neither is a dependency of any redline.
* Coverage: the complete original (twelve recorded windows, preparation proof log §3) and every selected unit were read in this session against the same baseline blob, which this step re-confirmed on `main`.
* Baseline fingerprint: the original's SHA-256 over its raw bytes equals the package's stated value (`850dc1a3c8294a0e0521f02cb7300fb05233beccb1ecadf611b41e8ea9adfb00`, same representation).
* Selection: matches the handoff and the ledger. The redlines file's identity table labels 2.15 "(C-26: R-1, R-3, R-4)", which is the ledger's routing label; within that selected unit the package also carries R-2, R-5 and R-6, mapped by context under GTWPE-D3, as the preparation proof log §8 and §5 state. No unselected PF10 addendum is drained.

## 4. Whole-batch validation (before any edit)

Every redline was resolved independently against the unchanged original, from the pushed redlines file.

| Check | Result |
| :---- | :---- |
| Operations | Fifteen `REPLACE`; no unsupported operation; no `FIND_AND_REPLACE`, so RL-045 does not arise |
| OLD and NEW literals | Each matches its stated SHA-256 and byte length; none empty |
| OLD occurrence, expected / observed | 1 / 1 for each |
| Location | Each OLD is line-aligned and resolves to its stated line or range (RL-08: lines 1450–1453) |
| Metadata plan | Three header operations, each on a unique header line (§5) |
| Conflicts | None among the eighteen spans: no intersection, no shared boundary, no metadata span inside a content span |

## 5. Document-control plan

| Field | Original | Revised | Basis |
| :---- | :---- | :---- | :---- |
| Version | v2.0.6 | v2.0.7 | One increment of the final numeric component of the native dotted version, prefix and component count kept |
| Effective date | 2026-10-26 | 2026-11-02 | The actual application date (UTC), in the field's native `YYYY-MM-DD` form |
| Last Update Gate | BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-QA70-qa-plan-review-v1.0.md | BN 14.0.5 | The package's one recorded source, `PF10-HDE-Build-Notes-v14.0.5.md`, in source form (preparation proof log §11) |
| Status | Canon | Canon (unchanged) | Not stale |
| Title, Invocation tag | PF27-Canon-Plan-Templates; INV-f2ac55d77ce9aacc | Unchanged | Not authorized to change |

No internal restatement of the version or date exists outside the header (search for `2.0.6` and `2026-10-26` outside lines 1–16: none). The target has no change log or revision-history section, so no history entry is required. No package redline touches the header.

## 6. Operation ledger

Applied in descending original-offset order, without rematching changed text. Basis: each redline's own rationale and ledger row, as the preparation package records them.

| ID | Original lines → revised lines | Ledger row | Basis |
| :---- | :---- | :---- | :---- |
| META-VERSION | 7 → 7 | — | §5 |
| META-DATE | 11 → 11 | — | §5 |
| META-GATE | 13 → 13 | — | §5 |
| RL-01 | 112 → 112 | C-02 | 2.1 D-2 (lines 290–297, 313): the configured base's terminal `v1` or `v2` segment is the single permitted reading of a version, owned by HDE CLI/API/Vendor Ref §7.1.10, so the "Version literals" row's closed list of permitted classifications gains it; the route-construction prohibition is unchanged. |
| RL-02 | 287 → 287–289 | C-08 | 2.2 R-2 (lines 542, 543, 545): PF versions and file names may change; HDE Build Notes is cited by title alone because its addendum numbers restart with each base version; other PF references use title and section, never file name or version, including in an ADR; a derived artifact that must remain valid pins no PF file name, version or digest. |
| RL-03 | 326 → 328–329 | C-26 | 2.15 R-4 (lines 1763–1771): the QA plan carries the line `Live test:` with RAN, WAIVED or MISSING; added as a front-matter field with allowed placeholder markers. |
| RL-04 | 389 → 392–422 (new H3 at 394) | C-26 | 2.15 R-1 to R-6 and "Relation to other canon": every Epic's Live QA Plan includes and runs the live compat test, whatever the Epic changed; the CRD boundary (lines 1825, 1835); execution and controls with HDE Governance §3.4, the result Ops evidence there; a blocked live test stays `TOOLING_BLOCKED`; only the Product Owner may waive; the plan and its review carry the live-test line and MISSING blocks approval; the name "Live QA" is reserved. |
| RL-05 | 973 → 1006–1007 | C-26 | 2.15 R-4 (lines 1769, 1780): the QA RCA & Doc Delta summary carries the live-test line and, with MISSING, gives no PASS verdict. |
| RL-06 | 1168 → 1202 | C-26 | 2.15 R-4 (lines 1777–1778, 1784): a missing live compat test without a recorded Product Owner waiver joins the closed list of valid Live QA Plan approval blockers. |
| RL-07 | 1312 → 1346–1348 | C-09 | 2.2 R-3 (lines 549–550), as written: the close-pack writer writes only at the close stage, after the authorized QA verdict and the closure decision exist; its test is a close-stage test outside full validation and other ordinary required PR CI. |
| RL-08 | 1450–1453 → 1486–1489 | C-26 | 2.15 (lines 1666–1681, 1706, 1743, 1777): the Epic Specification's open-rails declaration, implementation-preservation and review-posture bullets also carry the live compat test every Epic's QA runs, waivable only by the Product Owner; line 1451 (now 1487) is unchanged. |
| RL-09 | 1459 → 1495 | C-02 | 2.1 D-2 (lines 288, 316, 323): the route-policy category "explicit legacy fallback" reads as the terminal-v1 legacy selection, is not a fallback, and routes to HDE CLI/API/Vendor Ref §7.1.10. |
| RL-10 | 2261 → 2297–2298 | C-26 | 2.15 R-4 (lines 1770, 1781): §3B's record gains the field `Live test:`; with MISSING, the close mutation set is not close-PR-ready. §3B "Entries and exit" (H-06) is unchanged. |
| RL-11 | 3120 → 3157–3158 | C-26 | 2.15 R-4 (lines 1768, 1779): §8 gains a conditional field for its use as the run's QA evidence review; with MISSING, the evidence is not acceptable. |
| RL-12 | 3218 → 3256–3258 | C-26 | 2.15 R-3 (line 1759): §9's scope states that a report with no live test starts with `No live test ran.` and names the waiver or the missing test. |
| RL-13 | 3232 → 3272–3273 | C-26 | 2.15 R-4 (line 1769): §9's QA Closeout Summary gains the field `Live test:`. |
| RL-14 | 3447 → 3488 | C-26 | 2.15 R-4 (line 1780): §9's verdict keeps its four values and is not PASS when the live-test line reads MISSING. |
| RL-15 | 3560 → 3601–3602 | C-26 | 2.15 R-4 (lines 1771, 1782): §10's Closure Decision gains the field `Live test:`; with MISSING, the closure decision is not CLOSE. |

## 7. Unchanged-content verification

* Interval check: the original splits into nineteen untouched intervals around the eighteen spans. Each appears byte-identical and in order in the revised PF, and each payload appears exactly where planned; the revised PF's length equals the sum of the intervals and payloads.
* Line-diff audit: an independent line comparison of original and revised PF finds nineteen non-equal regions, each inside or immediately after a planned operation's lines (RL-04 shows as an insertion after original line 390, the blank line that follows its anchor line 389, which is equivalent). No other line differs.
* Independent re-derivation: applying the pushed package from commit `bf5bb08` to the original read from `main` again reproduces all 331,957 bytes of the saved revised PF.
* Drain-side agreement: the revised PF differs from the preparer's content-only one-pass simulation (SHA-256 `1a955c0082b4082f3945bb60a8c0a6f5e8780a535827579f7af17fa79e76e8e4`) in exactly the three header lines of §5.
* EOF and form: both files end with the same two LF characters; no CR; no fenced code block in either; tables keep their rows (RL-01 replaces one table row with one table row).

## 8. Revised-PF checks

* Exactly one version increment (v2.0.6 to v2.0.7); the old version string no longer appears in the header.
* Effective date and Last Update Gate as in §5; Status Canon; Title and Invocation tag unchanged.
* No draft status language about the document. The only placeholders are template fields and template rules, which canon requires in a template document; the new front-matter field (RL-03) uses the allowed `<PLACEHOLDER>` form.
* No Unicode ellipsis or three-period sequence.

## 9. Limitations and unresolved items

* H-06 (CCR-5) and H-07 (CCR-1 / P-2) stay held, undrafted, with what they wait for recorded in the preparation proof log §6.
* The preparation proof log §9 records three observations: RL-07 and §3B "Entries and exit" state different orderings of the close-pack write and the closure decision until CCR-5 is ruled; R-4 does not say which live-test value a plan carries for a test it includes but has not yet run; and a duplicated bullet in "Explicit non-blockers" (now lines 1233 and 1234) is unchanged.
* These are text checks of this document, not product QA.

## 10. Next manual action

Nathan reviews the revised PF and both proof logs on draft pull request amthorn78/glow-hdengine-v2#826, branch `claude/gtwpe-triage-authoring-j94ewf`, and decides whether to move this text into `docs/pfcanon/`. Nathan alone merges.

## 11. Save verification receipt

Written after the revised PF was saved in the working tree and read back from disk, on 2026-11-02.

| File | Verification |
| :---- | :---- |
| Revised PF | Read back from disk: 331,957 bytes, 3,980 lines, SHA-256 `dbbea67326c03ad925b54b50e25c6a4b22b1d75b7d8a447dfa1a4358a650325f`; byte-identical to the independent re-derivation in §7; the new subsection (lines 392–424) was also read directly. |
| This proof log | Read back in full after it was written; one revised-line number (RL-12) and two abbreviated hashes were then corrected, and this receipt row and the line below were added and read back. Every revised-line number in §6 was checked against the saved revised PF. |

Save completeness: both required files are saved and verified. Application outcome: applied. The commit that holds them is given in the ledger row and the session's final response.
