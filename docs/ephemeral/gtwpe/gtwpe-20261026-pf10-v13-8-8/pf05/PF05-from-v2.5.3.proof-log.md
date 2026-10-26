# Proof log — PF05-from-v2.5.3.md (T-PF05 application)

This is the application report for the revised PF `PF05-from-v2.5.3.md` in this directory. It records how the revised PF was made from the original and the validated redlines, the basis of every operation, and what was verified. The revised PF is not an authoritative publication: `docs/pfcanon/` is unchanged, and canon transfer is the Product Owner's manual action. This report establishes no canon adoption, QA verdict, acceptance or closure.

## 1. Artifact and outcome

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/PF05-from-v2.5.3.md`; 327,342 bytes; 4,461 LF-terminated lines; no CR; SHA-256 `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028` |
| Document | `PF05-Canon-HDE-CLI-API-Vendor-Ref` v2.5.4, effective 2026-10-26, Status `Canon` |
| Outcome | Application succeeded from package revision 2: 8 content operations and 3 derived document-control edits applied; every check passed (§4, §6 and §7) |
| Revision | This output replaces the revision 1 output (commit `e24e05f`; 326,792 bytes; SHA-256 `910f25b578fedebb74cb0142c5320a158cb7a9f8de943b17a6e0004e1fb35da0`), which applied the 5 operations of package revision 1. Revision 2 adds RL-06 to RL-08 and widens RL-05. Git history keeps revision 1 |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b; body fetched live on 2026-10-26 (page last edited 2026-10-09T11:05:22.094Z); version line `Prompt Version: 100926.1` |
| Authorization | Nathan's handoff "GTWPE 100926.1 T-PF05 document session (TW-DRAIN-10 then TW-APPLY-10)", which authorizes this step after READY preparation in the same session. For revision 2: Nathan's direction in this session on 2026-10-26 to fix the stale sentences "in the current one" rather than in a new drain |
| Applier | Claude Code cloud session https://claude.ai/code/session_01D49VTgmgq8kpkcN9WLDdAW, in its TW-APPLY-10 step |
| Execution date | 2026-10-26 (UTC clock read at 2026-10-26T23:49:59Z, before the revision 2 application; revision 1 read it at 21:49:50Z) |

## 2. Inputs and identities

| Input | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`, v2.5.3, blob `8b136def4c22f8308169a1b0315086b3e90ead1d`; 323,966 bytes; 4,439 lines; SHA-256 `65a9ad6e9d4e75cf50c4e0ae5ac6b3cbabce35bea759de9a6ef4c77549dd6352`; read at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c` |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/redlines-PF05-from-v2.5.3.md`, package revision 2, at commit `02bc1a5`; 23,808 bytes; SHA-256 `f5224bb704bd94bdf7df496a6ee35df3e31d8f6bc13acd1cac6ffc354ae24b9e` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/redlines-PF05-from-v2.5.3.proof-log.md` at commit `02bc1a5`; SHA-256 `c0b8b2d556c7eb098c15eab1d3fa3f6d50b668eb92001df70056123f8cac18d1` |
| Preparer and run | the same session's TW-DRAIN-10 step; run `gtwpe-20261026-pf10-v13-8-8 / T-PF05 / TW-DRAIN-10 / run 1`, package revision 2; outcome `READY`, save `COMPLETE_PACKAGE` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF05; rows A07, A08, A09 (with X05), S-APR |
| Selected sources | PF10 `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` v13.8.8 (blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter lines 1–223, addenda 2.7 (688–889), 2.8 (890–1002, including S02 and S07 met at lines 933 and 937), 2.9 (1003–1101). Specification `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (blob `c4802a5a7fa33db38d42d8a7f64679cd18b50480`) lines 147–193, overlaid by delta 01 (blob `9408d6ed091bcba3d751fcb17ae392a1ceca8bbb`) C-8 to C-12. Supporting: X05, `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` lines 701–739 (blob `6baead456619af1e73e15ace1079380f5797ca85`); PF10 2.2 and 2.4 for S03; `tests/retired_tests.md` (blob `ea44b46262168fd5240451fe1e9da069c76e6a5e`). Content source for the RL-03 limits: `audit/HDE-CRD-0002_close_report.md` (blob `0bbc8050d3c197bc2fef6371cdb7064739d4c507`) |
| Branch | `docs/20261026-gtwpe-pf10-v13-8-8-documents`; shared draft PR #761 |

## 3. Preparation-state verification

- **Package read in full.** The original and both package files were read in full in this session. The redlines file was re-extracted from commit `02bc1a5`, and its bytes equal the working-tree file.
- **Preparation state.** Outcome `READY` with `COMPLETE_PACKAGE`. Target and selected-source coverage complete. No unresolved required change. H-03 and H-04 held by the ledger and not drafted. O-1 resolved by RL-06 to RL-08. O-2 to O-4 are reported, not required changes.
- **Selection.** The ledger's T-PF05 selection is A07 and A08 (CR-7, §5.6), A09 with X05 (§7.1.11 DD-04 paragraph, §7.2.0 posture) and S-APR (DD-04 status). Nathan's direction extends the editable scope to §4.1.6, §5.1.0 and §5.1.7, with A08's S02 and S07 records and S03 as their basis. H-03 and H-04 stay held.
- **Baseline match and drift.** The original's SHA-256 equals the preparer's recorded baseline digest; both are raw-byte digests of the same representation. Immediately before the revision 2 application, `git fetch origin main` showed `main` still at `0838ba08254eaefc888019df49a06aa2ae99cc6c`, with PF05 at blob `8b136def4c22`. There is no material drift and no newer PF05 version.

## 4. Whole-batch validation

The saved revision 2 redlines were parsed again from the committed bytes, independently of the preparation:
- every payload's stated byte length and SHA-256 matched its extracted bytes;
- every locator resolved exactly once in the original;
- the original-bound plan, content and metadata spans together, has no intersection, no shared boundary and no insertion at or inside a replaced span;
- `END OF REDLINES` is present;
- the operations are `REPLACE` and `INSERT` only, so the RL-045 dialect question does not arise;
- validation exited 0, and its simulated content output matches the preparer's recorded simulation, SHA-256 `c157925a8cb796023ca2ac07dc19bedb0e518f6b6c1bb7c5e8d8b1cacc7c1915`.

## 5. Operation ledger and basis

Spans are original byte offsets, in document order. The basis is the preparer's rationale and source-ledger reference, restated here.

| ID | Op | Original span | Old to new bytes | Basis (ledger rows and source) | Rationale |
| :-- | :-- | :-- | :-- | :-- | :-- |
| MD-VERSION | metadata | [111, 132) line 6 | 21 to 21 | Header contract: one bump of the native dotted version | `v2.5.3` to `v2.5.4` |
| MD-DATE | metadata | [153, 185) line 8 | 32 to 32 | Header contract: execution date in native `YYYY-MM-DD` | `2026-10-09` to `2026-10-26` |
| MD-GATE | metadata | [186, 308) line 9 | 122 to 109 | Header contract: the sources that justified the update, in recorded order | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` to `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md`; the line's three trailing spaces are kept |
| RL-01 | REPLACE | [18262, 18377) line 125 | 115 to 96 | S-APR (Specification "Canon, QA & Build Notes posture", S14 status drainage); A09 with X05 | §1 restates the DD-04 status; S14 delivered the override, so "the unimplemented production override requirement" becomes "the production vendor override" |
| RL-06 | REPLACE | [76816, 77298) line 837 | 482 to 728 | Nathan's direction; A08 (S07 met); supporting PF10 2.2 and 2.4 and `tests/retired_tests.md` (S03) | The §4.1.6 limitations bullet says the parser still describes Reader v1 bytes and that the legacy `scripts/hd_cli.py` / `tests/reader_v1/test_cli_proof.py` failure stands. S07 changed the help, and S03 retired the test with a recorded reason. The bullet's other limitations stay |
| RL-07 | REPLACE | [153354, 153495) line 2071 | 141 to 178 | Nathan's direction; A08 (S02 met) | §5.1.0's last sentence retained a factory HTML 404 limitation that S02 removed; unknown descendant paths receive the governed §5.2 `404 ERR_NOT_FOUND` |
| RL-08 | REPLACE | [166307, 166948) line 2253 | 641 to 797 | Nathan's direction; A08 (S02, S07 met); supporting S03 | §5.1.7's known-limits paragraph is restated: all three factories answer unknown paths with the governed JSON error, showcompat help describes compat stdout, and the legacy CLI proof test is retired. The wheel-install limit, the carried findings and the nonclaim sentence stay |
| RL-02 | REPLACE | [199202, 199654) line 2577 | 452 to 1,669 | A07 (AD-1, CR-7, the §5.6 doc-delta candidate); A08 ("Required canon drainage": CR-7 into §5.6); X04 §18 | The §5.6 state at `aa58e93` predates S15's Aux record and CR-7's removal of the five canon-retired records (23 to 18). The new paragraph states the Catalog verified at `main@0838ba0` and routes the population rule to HDE Schemas & Artifacts |
| RL-03 | REPLACE | [259142, 259836) line 3500 | 694 to 1,986 | S-APR; A09 with X05 (§17 row for the paragraph); A09 LR4-O2; carried OBS-W4-1 with the close report's `FND-012`; the close report's S14 line | S14 delivered `--allow-prod-vendor` and its audit gate, so the held-gap paragraph and its "do not invoke or describe the flag as operational" are stale. The replacement gives the delivery, the implementation verified at `main@0838ba0` and the recorded limits. The §7.1.11a to §7.1.11f contract and §7.1.11f's clock term (H-04) are untouched |
| RL-04 | REPLACE | [267539, 268073) line 3605 | 534 to 631 | A09 with X05 (§17 row for §7.2.0) | The delivered override leaves the gap list. The other two gaps, broad non-v2 legacy selection and retry configuration outside the five tuples, are re-verified and pinned to `main@0838ba0` |
| RL-05 | INSERT | gap at 307197 (after line 4126) | 0 to 363 | PF05 §0.4 "Editorial vs. normative" and §11.1 "Policy" and "Entry style" | RL-03 lifts a canon directive, a normative delta, so the Change Log gains a one-line `v2.5.4` entry naming every changed section, with `Sentinel updated: NO` |

## 6. Document-control plan

- **Header.** The document-control header is the block under `## **0.1 Header**` (lines 3–10). It has one each of Title, Version, Status, Effective date, Last Update Gate and Invocation tag. No field is duplicated or conflicting, and none was added.
- **Version.** `v2.5.3` is native dotted numeric with three components, so one increment of the last component gives `v2.5.4`. The output has exactly one `**Version:**` field, reading `v2.5.4`. Revision 2 does not bump again: it remakes the same revision from the same baseline.
- **Effective date.** The only control date that records the revision. It is set to the execution date, `2026-10-26`.
- **Last Update Gate.** The sources the package records, deduplicated and in order:
  1. the PF10 file `PF10-HDE-Build-Notes-v13.8.8.md`, giving `BN 13.8.8`, which covers RL-01 to RL-04 and RL-06 to RL-08;
  2. `HDE-CRD-0002-specification-v1.1-approved.md`;
  3. `HDE-CRD-0002_close_report.md`.

  No PF document other than PF10 is a source. `tests/retired_tests.md` is repository evidence, not a source document. Delta 01 justified no change.
- **Unchanged fields.** Title, Status (`Canon`, not stale) and Invocation tag. The title carries no version. Line 835's dated inspection and the v2.5.3 Change Log entry are history.
- **Change history.** RL-05's entry names `v2.5.4`, equal to the derived version, and names §§4.1.6, 5.1.0, 5.1.7, 5.6, 7.1.11, 1 and 7.2.0. The format records no date. Version, date, gate and change history agree.
- **Conflicts.** The metadata spans end at byte 308 and the first content span starts at 18262, so they are disjoint. No package operation edits the header.

## 7. Exact application and preservation

- **Method.** All eleven operations were applied in descending offset order to the raw original bytes, without rematching changed text. No line-ending conversion, trimming or normalization was performed.
- **Reconstruction.** An expected stream was rebuilt from the twelve untouched original intervals and the eleven payloads. It equals the applied output byte for byte. Each untouched interval sits in the output at its shifted offset, unchanged.
- **Operation checks.** Every OLD block is absent from the output, and every NEW block, the inserted entry and the three derived header lines are present. Lines 6, 8 and 9 read exactly:
  - `**Version:** v2.5.4  `;
  - `**Effective date:** 2026-10-26  `;
  - `**Last Update Gate:** BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md   `.
- **Diff audit.** `git diff --no-index -U0` of the original against the saved output shows exactly ten hunks, 32 insertions and 10 deletions:

  `-6 +6`, `-8,2 +8,2`, `-125 +125`, `-837 +837`, `-2071 +2071`, `-2253 +2253`, `-2577 +2577,8`, `-3500 +3507,15`, `-3605 +3626`, `-4126,0 +4148`.

  Below the header, the output is byte-identical to the preparer's simulation.
- **Integrity checks.**
  - The whole file decodes as UTF-8, has no CR and ends with one LF. Its last bytes are unchanged.
  - The counts of code fences and table rows are unchanged.
  - The counts of TODO, TBD, FIXME and ellipsis markers are unchanged.
  - The revised PF carries no `Draft` status language about the document, no placeholder outside examples and templates, no drafting note or instruction to a future writer, and no stale status.
- **Byte counts.**

| Identity | Bytes | Lines | SHA-256 |
| :-- | --: | --: | :-- |
| Original | 323,966 | 4,439 | `65a9ad6e9d4e75cf50c4e0ae5ac6b3cbabce35bea759de9a6ef4c77549dd6352` |
| Revised PF (revision 2) | 327,342 | 4,461 | `1de30cbb6cde8be9c7ae3f0a518e871d22cc47b02a87b3209723e8b3d1213028` |

These are text checks on the document, not product QA.

## 8. Limits, held items and carried observations

- **Revised PF.** It is a working file under `docs/ephemeral/`. It does not change `docs/pfcanon/` or adopt canon.
- **Repository statements.** RL-02, RL-03, RL-04, RL-06 and RL-08 state static inspection at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` only.
- **Held, untouched.** H-03 (LR5-O1, §5.11.2 and §5.12) and H-04 (OBS-W4-4, §7.1.11f "governed clock boundary").
- **Carried from the preparation proof log §10.** These stay unchanged; no source names their passages.
  - **O-2.** The §3.7 and §4.6 dry-run flows are now subject to the §7.1.11 gate in a production-like environment.
  - **O-3.** Pre-existing ellipses.
  - **O-4.** The §5.6 transport-facts table omits three catalogued ops routes.

## 9. Next manual action

- **Review and transfer.** Nathan reviews the revised PF and, if they accept it, transfers it to `docs/pfcanon/` manually.
- **PR.** Nathan alone merges shared draft PR #761.

## 10. Save verification receipt

The revised PF was read back in full from its repository path, as all 327,342 bytes:
- it decoded as UTF-8;
- `cmp` with the validated output showed equal bytes;
- its SHA-256 matched §1;
- the diff audit in §7 was repeated on that saved copy.

This report was written after that verification and does not carry its own hash.
