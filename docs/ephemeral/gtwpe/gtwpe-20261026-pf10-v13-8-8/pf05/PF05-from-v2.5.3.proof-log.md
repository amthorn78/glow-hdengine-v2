# Proof log — PF05-from-v2.5.3.md (T-PF05 application)

This is the application report for the revised PF `PF05-from-v2.5.3.md` in this directory. It records how the revised PF was made from the original and the validated redlines, the basis of every operation, and what was verified. The revised PF is not an authoritative publication: `docs/pfcanon/` is unchanged, and canon transfer is the Product Owner's manual action. This report establishes no canon adoption, QA verdict, acceptance or closure.

## 1. Artifact and outcome

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/PF05-from-v2.5.3.md`; 326,792 bytes; 4,461 LF-terminated lines; no CR; SHA-256 `910f25b578fedebb74cb0142c5320a158cb7a9f8de943b17a6e0004e1fb35da0` |
| Document | `PF05-Canon-HDE-CLI-API-Vendor-Ref` v2.5.4, effective 2026-10-26, Status `Canon` |
| Outcome | Application succeeded: 5 content operations and 3 derived document-control edits applied; every check passed (§4, §6 and §7) |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b; body fetched live on 2026-10-26 (page last edited 2026-10-09T11:05:22.094Z); version line `Prompt Version: 100926.1` |
| Authorization | Nathan's handoff "GTWPE 100926.1 T-PF05 document session (TW-DRAIN-10 then TW-APPLY-10)", which authorizes this step after READY preparation in the same session |
| Applier | Claude Code cloud session https://claude.ai/code/session_01D49VTgmgq8kpkcN9WLDdAW, in its TW-APPLY-10 step |
| Execution date | 2026-10-26 (UTC clock read at 2026-10-26T21:49:50Z, before application) |

## 2. Inputs and identities

| Input | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md`, v2.5.3, blob `8b136def4c22f8308169a1b0315086b3e90ead1d`; 323,966 bytes; 4,439 lines; SHA-256 `65a9ad6e9d4e75cf50c4e0ae5ac6b3cbabce35bea759de9a6ef4c77549dd6352`; read at `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c` |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/redlines-PF05-from-v2.5.3.md` at commit `431661b`; 16,530 bytes; SHA-256 `bcc4c6061c07a292c777016f6a4a659c9f4824d03d04d28f42e8a1db2d853c15` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf05/redlines-PF05-from-v2.5.3.proof-log.md` at commit `431661b`; SHA-256 `b446a6dc186b1a229515abd4a84c6115e1d84ce545aaf9e0e7069eb38318efed` |
| Preparer and run | the same session's TW-DRAIN-10 step; run `gtwpe-20261026-pf10-v13-8-8 / T-PF05 / TW-DRAIN-10 / run 1`; outcome `READY`, save `COMPLETE_PACKAGE` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, task T-PF05; rows A07, A08, A09 (with X05), S-APR |
| Selected sources | PF10 `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` v13.8.8 (blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter lines 1–223, addenda 2.7 (688–889), 2.8 (890–1002), 2.9 (1003–1101). Specification `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (blob `c4802a5a7fa33db38d42d8a7f64679cd18b50480`) lines 147–193, overlaid by delta 01 (blob `9408d6ed091bcba3d751fcb17ae392a1ceca8bbb`) C-8 to C-12. Supporting: X05, `docs/ephemeral/HDE-CRD-0002-WU-PR-04-pr-implementation-plan-v1.0.md` lines 701–739 (blob `6baead456619af1e73e15ace1079380f5797ca85`). Content source for the RL-03 limits: `audit/HDE-CRD-0002_close_report.md` (blob `0bbc8050d3c197bc2fef6371cdb7064739d4c507`) |
| Branch | `docs/20261026-gtwpe-pf10-v13-8-8-documents`; shared draft PR #761 |

## 3. Preparation-state verification

- **Package read in full.** The original, the redlines file and the preparation proof log were read in full in this session. The redlines file was re-extracted from commit `431661b`, and its bytes equal the working-tree file (SHA-256 above).
- **Preparation state.** Outcome `READY` with `COMPLETE_PACKAGE`. Target and selected-source coverage complete. No unresolved required change. H-03 and H-04 held by the ledger and not drafted. Observations O-1 to O-4 are reported, not required changes.
- **Selection.** The preparer's selection matches the handoff and the ledger's T-PF05 row: A07 and A08 (CR-7, §5.6), A09 with X05 (§7.1.11 DD-04 paragraph, §7.2.0 posture), S-APR (DD-04 status), with H-03 and H-04 held. No unselected PF10 addendum was needed.
- **Baseline match and drift.** The original's SHA-256 equals the preparer's recorded baseline digest; both are raw-byte digests of the same representation. Immediately before application, `git fetch origin main` showed `main` still at `0838ba08254eaefc888019df49a06aa2ae99cc6c`, with PF05 at blob `8b136def4c22` and PF10 at blob `680b0accb0bd`. There is no material drift and no newer PF05 version.

## 4. Whole-batch validation

The saved redlines were parsed again, independently of the preparation, from the committed bytes:
- every payload's stated byte length and SHA-256 matched its extracted bytes;
- every locator resolved exactly once in the original;
- the original-bound plan, content and metadata spans together, has no intersection, no shared boundary and no insertion at or inside a replaced span;
- `END OF REDLINES` is present;
- the operations are `REPLACE` and `INSERT` only, so no `FIND AND REPLACE` or `FIND_AND_REPLACE` dialect occurs (RL-045 does not arise);
- validation exited 0, and its simulated content output matches the preparer's recorded simulation, SHA-256 `13cb56bca5913c0599261fd2a2992d77f031ee78fb233381f83e2892f749bad2`.

## 5. Operation ledger and basis

Spans are original byte offsets. The basis is the preparer's rationale and source-ledger reference, restated here.

| ID | Op | Original span | Old to new bytes | Basis (ledger rows and source) | Rationale |
| :-- | :-- | :-- | :-- | :-- | :-- |
| MD-VERSION | metadata | [111, 132) line 6 | 21 to 21 | Header contract: one bump of the native dotted version | `v2.5.3` to `v2.5.4` |
| MD-DATE | metadata | [153, 185) line 8 | 32 to 32 | Header contract: execution date in native `YYYY-MM-DD` | `2026-10-09` to `2026-10-26` |
| MD-GATE | metadata | [186, 308) line 9 | 122 to 109 | Header contract: the sources that justified the update, in recorded order | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` to `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md`; the line's three trailing spaces are kept |
| RL-01 | REPLACE | [18262, 18377) line 125 | 115 to 96 | S-APR (Specification "Canon, QA & Build Notes posture", S14 status drainage); A09 with X05 | §1 restates the DD-04 status; S14 delivered the override, so "the unimplemented production override requirement" becomes "the production vendor override" |
| RL-02 | REPLACE | [199202, 199654) line 2577 | 452 to 1,669 | A07 (AD-1, CR-7, the §5.6 doc-delta candidate); A08 ("Required canon drainage": CR-7 into §5.6); X04 §18 | The §5.6 state at `aa58e93` predates S15's Aux record and CR-7's removal of the five canon-retired records (23 to 18). The new paragraph states the Catalog verified at `main@0838ba0` and routes the population rule to HDE Schemas & Artifacts |
| RL-03 | REPLACE | [259142, 259836) line 3500 | 694 to 1,986 | S-APR; A09 with X05 (§17 row for the paragraph); A09 LR4-O2; carried OBS-W4-1 with the close report's `FND-012`; the close report's S14 line | S14 delivered `--allow-prod-vendor` and its audit gate, so the held-gap paragraph and its "do not invoke or describe the flag as operational" are stale. The replacement gives the delivery, the implementation verified at `main@0838ba0`, and the recorded limits. The §7.1.11a to §7.1.11f contract and §7.1.11f's clock term (H-04) are untouched |
| RL-04 | REPLACE | [267539, 268073) line 3605 | 534 to 631 | A09 with X05 (§17 row for §7.2.0) | The delivered override leaves the gap list. The other two gaps, broad non-v2 legacy selection and retry configuration outside the five tuples, are re-verified and pinned to `main@0838ba0` |
| RL-05 | INSERT | gap at 307197 (after line 4126) | 0 to 252 | PF05 §0.4 "Editorial vs. normative" and §11.1 "Policy" and "Entry style" | RL-03 lifts a canon directive, which is a normative delta, so the Change Log gains a one-line `v2.5.4` entry in the target's format, with `Sentinel updated: NO` |

## 6. Document-control plan

- **Header.** The document-control header is the block under `## **0.1 Header**` (lines 3–10). It has one each of Title, Version, Status, Effective date, Last Update Gate and Invocation tag. No field is duplicated or conflicting, and none was added.
- **Version.** `v2.5.3` is native dotted numeric with three components, so one increment of the last component gives `v2.5.4`. The output has exactly one `**Version:**` field, reading `v2.5.4`.
- **Effective date.** The only control date that records the revision. It is set to the execution date, `2026-10-26`, not the preparation date (also 2026-10-26) and not a stale date.
- **Last Update Gate.** The sources the package records, deduplicated and in order:
  1. the PF10 file `PF10-HDE-Build-Notes-v13.8.8.md`, giving `BN 13.8.8`;
  2. `HDE-CRD-0002-specification-v1.1-approved.md`;
  3. `HDE-CRD-0002_close_report.md`.

  No PF document other than PF10 is a source. The redlines and report filenames are not used. Delta 01 justified no change, so it is not in the gate.
- **Unchanged fields.** Title, Status (`Canon`, not stale) and Invocation tag. The title carries no version, so nothing restates the version or date. Line 835's dated inspection and the v2.5.3 Change Log entry are history.
- **Change history.** RL-05's entry names `v2.5.4`, equal to the derived version. The format records no date. Version, date, gate and change history agree.
- **Conflicts.** The metadata spans end at byte 308 and the first content span starts at 18262, so they are disjoint. No package operation edits the header, so there is no duplicate authorization.

## 7. Exact application and preservation

- **Method.** All eight operations were applied in descending offset order to the raw original bytes, without rematching changed text. No line-ending conversion, trimming or normalization was performed.
- **Reconstruction.** An expected stream was rebuilt from the nine untouched original intervals and the eight payloads. It equals the applied output byte for byte. Each untouched interval sits in the output at its shifted offset, unchanged.
- **Operation checks.**
  - Every OLD block is absent from the output, and every NEW block, the inserted entry and the three header lines are present.
  - Header lines 6, 8 and 9 read exactly `**Version:** v2.5.4  `, `**Effective date:** 2026-10-26  ` and `**Last Update Gate:** BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002_close_report.md   `.
- **Diff audit.** `git diff --no-index -U0` of the original against the output shows exactly seven hunks: `-6 +6`, `-8,2 +8,2`, `-125 +125`, `-2577 +2577,8`, `-3500 +3507,15`, `-3605 +3626` and `-4126,0 +4148`. In total 29 insertions and 7 deletions. Below the header, the output is byte-identical to the preparer's simulation.
- **Integrity checks.**
  - The whole file decodes as UTF-8, has no CR and ends with one LF. Its last bytes, `\n\n---\n\n`, are unchanged.
  - The counts of code fences and table rows are unchanged.
  - The counts of TODO, TBD, FIXME and ellipsis markers are unchanged (zero, zero, zero and the pre-existing count).
- **Status language.** The revised PF carries no `Draft` status language about the document, no placeholder outside examples and templates, no drafting note or instruction to a future writer, and no stale status.
- **Byte counts.**

| Identity | Bytes | Lines | SHA-256 |
| :-- | --: | --: | :-- |
| Original | 323,966 | 4,439 | `65a9ad6e9d4e75cf50c4e0ae5ac6b3cbabce35bea759de9a6ef4c77549dd6352` |
| Revised PF | 326,792 | 4,461 | `910f25b578fedebb74cb0142c5320a158cb7a9f8de943b17a6e0004e1fb35da0` |

These are text checks on the document, not product QA.

## 8. Limits, held items and carried observations

- **Revised PF.** The revised PF is a working file under `docs/ephemeral/`. It does not change `docs/pfcanon/` or adopt canon.
- **Repository statements.** RL-02 to RL-04 state static inspection at `main@0838ba08254eaefc888019df49a06aa2ae99cc6c` only.
- **Held, untouched.** H-03 (LR5-O1, §5.11.2 and §5.12) and H-04 (OBS-W4-4, §7.1.11f "governed clock boundary").
- **Carried from the preparation proof log §10, for Nathan.**
  - **O-1.** S02 and S07 leave stale sentences outside this task's named sections: §4.1.6 line 837, §5.1.0 line 2071 and §5.1.7 line 2253 of v2.5.3. They need routing.
  - **O-2.** The §3.7 and §4.6 dry-run flows are now subject to the §7.1.11 gate in a production-like environment; unchanged.
  - **O-3.** Pre-existing ellipses; unchanged.
  - **O-4.** The §5.6 transport-facts table omits three catalogued ops routes; unchanged.

## 9. Next manual action

- **Review and transfer.** Nathan reviews the revised PF and, if they accept it, transfers it to `docs/pfcanon/` manually.
- **PR.** Nathan alone merges shared draft PR #761.
- **O-1.** O-1 needs a routing decision, for example a later T-PF05 drainage of S02 and S07 into §4.1.6, §5.1.0 and §5.1.7.

## 10. Save verification receipt

The revised PF was read back in full from its repository path, as all 326,792 bytes:
- it decoded as UTF-8;
- `cmp` with the validated output showed equal bytes;
- its SHA-256 matched §1;
- the diff audit in §7 was repeated on that saved copy.

This report was written after that verification and does not carry its own hash.
