# Proof log — PF29-Canon-HDE-Users-Guide v1.0.4 (TW-APPLY-10, gtwpe-20261101-pf10-v14-0-5, T-08)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.4.md`: the complete revised PF29-Canon-HDE-Users-Guide, v1.0.4. 83,852 bytes; 1,087 lines, LF-terminated; SHA-256 `3f7eca26b671224767c70ccb88bb70709fa337573ef44f3d3bcd04f0e19f1cad`; git blob `d3b41ae17381f22d5aa40cd6cbeff2c0eef8470c` |
| Package applied | `drain-r2`: `PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` and its `.r2.proof-log.md`, at package commit `e4506ee5fca18b0203fd81ee4698506aeb98ed4d` |
| Supersedes | The r1 application output at commit `550689fcbb40fb7c7eafa6f42fc9793078d6d5f7`: the same file name, blob `7a6f873a575e5f8972d9e204ce59ce315d374c6b`, SHA-256 `e3ba2c95135d1a78d20708059cc6d551602d68ac3d9b10111ecf622a9353a20e`, applied from package `drain-r1`. Its file and this proof log's r1 version stay in git history at that commit. Section 2 says why. |
| Commit references | Updated after a rebase onto other sessions' commits, to the pushed hashes: r1 package `285bc728eb3c39de37e6d4842292ea36b421f256`, r1 application `550689fcbb40fb7c7eafa6f42fc9793078d6d5f7`, r2 package `e4506ee5fca18b0203fd81ee4698506aeb98ed4d`, r2 application `e37d0b5731762aaff783261631e3dc00b447e0fa`. The rebase changed no file content; the r2 redlines blob is still `c805c848b69067f06bfdec0e54d1b2034db35d59`. |
| Producing prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`. Re-fetched live at the start of this application step on 2026-11-02; it still records "Prompt Version: 100926.1", last edited 2026-10-09T11:05:22Z. |
| Applier | The same Claude Code document session that prepared the package, https://claude.ai/code/session_01Q789u3KLSaV6qHFgm3m8t4. Nathan's T-08 handoff authorizes preparation, application, and correction followed by fresh application in this session. No subagent, reviewer or other session took part. |
| Execution date | 2026-11-02 (UTC; this application ran at about 2026-11-02T00:38Z) |
| Outcome | Applied. 20 operations: 17 content redlines and 3 derived header fields. Both outputs were saved and read back (§8). |
| Standing | An ephemeral output for Nathan's review and merge. It is not a publication into `docs/pfcanon/`, and it establishes no QA, acceptance, deployment or closure. |

## 2. Why this output replaces the r1 application

The r1 package (`drain-r1`, ten redlines) passed this prompt's validation and was applied at `550689f`. After that, the shared ledger, as fetched, showed a correction dated 2026-11-02. That correction applies GTWPE-D3, a binding Product Owner ruling recorded in `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`: every eligible document is updated on context and scope, not only at the drain targets an addendum names.

r1 had left several PF29 statements undrafted because D-1 and D-3 did not name them. So the preparer corrected its own package as `drain-r2`, under Nathan's handoff authority, and this step validated the corrected package afresh against the unchanged original. The final file name is unchanged, because both runs derive v1.0.4 from v1.0.3. One writer, this session, owns both runs. The r1 output is superseded, not deleted: it is kept in git history.

## 3. Inputs

| Input | Identity |
| :---- | :---- |
| Exact original | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.3.md` at `e2b7427ff418ca8f08f05587c4a541308a76da56`, read from the git object. Blob `6730222d2f352221ddbe140a08c260380bbf5abc`; SHA-256 `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`; 76,613 bytes; 1,079 lines; no CR. |
| Current authoritative copy | `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, fetched at 2026-11-02T00:37Z. Same blob, and the only PF29 file in `docs/pfcanon/`. No drift. |
| Redlines (r2) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.r2.md` at `e4506ee`. Blob `c805c848b69067f06bfdec0e54d1b2034db35d59`; SHA-256 `bf546c175417fc12fd4c78cadf23a5363a27174634da9d8eb230685903f01197`. Read from the git object. |
| Preparation proof log (r2) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.r2.proof-log.md` at `e4506ee` |
| Preparer and run | TW-DRAIN-10 100926.1, this session; run `gtwpe-20261101-pf10-v14-0-5/T-08/drain-r2`. The TW-DRAIN-10 page was fetched live at the start of preparation (r1) and was not fetched again for the r2 correction. Its pinned version 100926.1, last edited 2026-10-09, was used for both. |
| Preparation and save outcome | `READY` / `COMPLETE_PACKAGE`; no blocking item. H-05 (AGENTS.md) is held and is not a PF target. |
| Change source | PF10-HDE-Build-Notes v14.0.5, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`. Blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`. |
| Selected source units | Addendum 2.1: D-1 (225–276), D-2 (277–344), D-3 (345–396); context 205–224 and 491–516. These agree with Nathan's handoff and the ledger. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`. Task T-08; rows C-01, C-02, C-03; supporting C-06. |
| Governing decision | GTWPE-D3, `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md` (`BINDING`) |
| Editorial standard | PF03-Reference-Technical-Writing-Best-Practices v1.8.8, read in full in this session. No PF03 cleanup was performed at this step. |

## 4. Intake checks

All checks used committed bytes:

- the r2 redlines file ends with `END OF REDLINES`;
- it declares run `drain-r2` and `READY`;
- it binds the baseline blob, the baseline SHA-256 and the commit.

The r2 preparation proof log records complete target and selected-unit reading, a whole-PF29 contextual scan with a disposition for every hit line, no blocking item, and `COMPLETE_PACKAGE`. No unselected PF10 addendum was needed.

## 5. Operation ledger and basis

Each operation was resolved independently against the unchanged original before any byte was written. Expected and observed occurrence is 1 for each, every span is line-bounded, and the spans are strictly disjoint. The basis for each operation is restated from the r2 preparation proof log: its rationale, then the ledger row and the PF10 2.1 lines it drains. Every `\[Current gap\]` statement rests on the preparer's bounded read-only inspection at `e2b7427`; the r2 proof log §5 gives the paths, blobs and lines.

| ID | Original lines | Basis |
| :---- | :---- | :---- |
| RL-01 | §1.1, 81 | Records the snapshot `e2b7427` inspected for every new current-gap statement, as PF29 §0.2 requires. CONSISTENCY; C-01 to C-03. |
| RL-02 | §1.1, 92 | The `bg:resolve` row restated the non-v2 fallback that D-2 supersedes. It now states the terminal-v1 route and the gap. CONSISTENCY; C-02 (277–344). |
| RL-03 | §1.1, 100 | The `POST /api/compat/v1` row gains D-3's dev/admin gate (exact `dev`, `test` or `local`) and the gap. C-03 (349–354). |
| RL-04 | §1.2, 122 | The production-public compat row gains D-3's wider-exposure rule: serving it beyond dev/admin needs a later decision. C-03 (359–361). |
| RL-05 | §7.2, 417 | The method-posture bullet gains the `ERR_WRITER_FORBIDDEN` (403) non-production refusal, with the gap. C-03 (350–354). |
| RL-06 | §7.5, 483–485 | The showcompat vendor recipe now sets `APP_ENV=dev`, as D-1's environment classification requires; checked-in behavior is unchanged. An added note states the override, the route selection and the gap. C-01 (229–235, 272); C-02 (281–283). |
| RL-07 | §9.2, 589 | Conjunction vendor acquisition gains D-1's override and D-2's route selection, with the gap. C-01 (229–233); C-02 (281–283). |
| RL-08 | §11.3, 710–714 | D-2 supersedes §11.3 as a section. The heading becomes "Terminal-v1 legacy BodyGraph route", keeping its number, level and labels. The legacy route is reached only with a base whose final segment is exactly `v1`; it is not fallback; every other non-v2 base must fail with `PROVIDER_ROUTE_UNSUPPORTED`. Checked-in code does not yet fail closed. C-02 (281–298, 312–314). |
| RL-09 | §12.2, 771 | The base-URL guidance gains D-2's configured-base boundary (absolute HTTPS, host, no userinfo, query or fragment, terminal `v2` or `v1`), routed to PF05-Canon-HDE-CLI-API-Vendor-Ref. The gap: only the HTTPS scheme is checked. C-02 (285–287). |
| RL-10 | §13.3, 838 | D-2 supersedes "With a non-v2 configured base, explicit legacy fallback may proceed". C-02 (314). |
| RL-11 | §13.3, 848 | D-1 extends the production override to `showcompat --source vendor` and vendor-selecting conjunction: same classification, initiator rule, audit, codes and carrier; exit 64 when no vendor acquisition is selected. Marked with the gap. The fallback sentence follows D-2. C-01 (229–244, 265); C-02 (314). |
| RL-12 | §16, 963 | D-3: the compat namespace is dev/admin-only. Outside production-like posture it is served only with exact `dev`, `test` or `local`, and otherwise refuses with 403. Marked with the gap. C-03 (349–364, 386). |
| RL-13 | §16, 969 | D-2 supersedes "For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved". C-02 (314). |
| RL-14 | §16, 985 | D-1 drains into the production-override limit, with the gap. C-01 (229–237, 265). |
| RL-15 | §17, 998 | D-3: the row "HTTP 404 from POST /api/compat/v1 in prod" gains the non-production refusal. PF10's "§16" label resolves to PF29 §17. C-03 (351–354, 386). |
| RL-16 | §17, 1005 | The `PROVIDER_CONFIG_INVALID` row gains D-1's environment classification for showcompat and conjunction, with the gap. C-01 (233, 272). |
| RL-17 | §17, 1006 | The row for `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID` and `PROVIDER_AUDIT_UNAVAILABLE` gains the showcompat scope, with the gap. C-01 (242–244, 265). |
| META-VERSION | §0.1, 7 | Standing document-control authority of TW-APPLY-10 |
| META-DATE | §0.1, 11 | Standing document-control authority of TW-APPLY-10 |
| META-GATE | §0.1, 13 | Standing document-control authority of TW-APPLY-10 |

This step did not re-decide domain correctness, and it did not alter any payload.

## 6. Document-control plan

| Field | Before | After | Derivation |
| :---- | :---- | :---- | :---- |
| Version | `v1.0.3` | `v1.0.4` | The final numeric component is incremented once; the prefix and the three components are kept. |
| Effective date | `2026-10-26` | `2026-11-02` | The actual application execution date, native `YYYY-MM-DD`. It is the same date as the superseded r1 application. |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` | `BN 14.0.5` | The one recorded source: PF10-HDE-Build-Notes v14.0.5, file `PF10-HDE-Build-Notes-v14.0.5.md` |
| Status | `Canon` | `Canon` | Not stale |
| Title, Invocation tag | `PF29-Canon-HDE-Users-Guide`, `INV-f2ac55d77ce9aacc` | unchanged | Protected |

- Internal restatements: none exist outside §0.1.
- Change history: PF29 has no change-log or Doc-Delta section, so none was needed.
- Overlap: the package has no header redline, and the header spans (lines 7, 11, 13) overlap no content span.
- Agreement: all values agree.

## 7. Application and preservation

The operations were applied once, in descending original offset, without rematching. Text was handled as UTF-8 and written as raw bytes.

- Preservation audit: every untouched original interval is byte-identical in the output. That is 70,250 of 76,550 original characters, which is all of them outside the 20 consumed spans. Every payload sits at its planned position, and the tail is identical.
- `diff` of the original against the output: the only hunks are at original lines 7, 11, 13, 81, 92, 100, 122, 417, 483, after 486 (an addition), 589, 710, 712, 714, 771, 838, 848, 963, 969, 985, 998 and 1005–1006. Each is a planned operation. RL-06 and RL-08 each show as more than one hunk, because unchanged lines lie inside or beside their spans.
- `diff` of the r2 preparer's simulated body (SHA-256 `785e0ec09d177672edf11d5d53e675cc2b8af137b06e8165523767c2c33f59da`) against the output differs only at lines 7, 11 and 13.

Text checks, all passing:

- one final LF and no CR;
- fence-line and table-row counts unchanged;
- heading lines unchanged except the planned §11.3 retitle;
- exactly one `Version` (`v1.0.4`), one `Effective date` (`2026-11-02`) and one `Last Update Gate` (`BN 14.0.5`);
- Status, Title and Invocation tag unchanged;
- no `1.0.3` restatement;
- no ellipsis;
- no `Draft`, `TODO`, `TBD` or `FIXME`.

The command placeholders in operator recipes are baseline example inputs, not drafting markers, and they are unchanged.

Byte counts: the original is 76,613 bytes and 1,079 lines; the output is 83,852 bytes and 1,087 lines. These are text checks, not product QA.

## 8. Save verification

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.4.md` | 83,852 | `3f7eca26b671224767c70ccb88bb70709fa337573ef44f3d3bcd04f0e19f1cad` | Complete. All bytes were read from disk, hashed, and compared by full `diff` with the original and with the expected stream. |
| This proof log | — | — | Complete, after writing. No self-referential hash. |

## 9. Limitations and deviations

- The `\[Current gap\]` statements describe checked-in bytes at `e2b7427`, not runtime or deployed behavior. When Candidate CRD Items List item 9 is delivered, they become stale and need a later drain.
- Nathan should review these preparer decisions:
  - the §11.3 retitle (RL-08);
  - the edits outside the handoff's named sections (RL-01 to RL-07, RL-09, RL-16), made under GTWPE-D3;
  - the decision to add no troubleshooting row for `PROVIDER_ROUTE_UNSUPPORTED`.
- H-05, the AGENTS.md edits under D-1 and D-2, is held for the Product Owner's explicit instruction and is not drafted.

## 10. Next manual action

Nathan reviews the revised PF on draft PR amthorn78/glow-hdengine-v2#826, branch `claude/gtwpe-triage-authoring-j94ewf`, and decides on merge and on publication into `docs/pfcanon/`. Neither step is performed here.
