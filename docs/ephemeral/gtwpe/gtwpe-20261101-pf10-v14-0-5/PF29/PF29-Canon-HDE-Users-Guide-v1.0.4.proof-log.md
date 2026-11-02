# Proof log — PF29-Canon-HDE-Users-Guide v1.0.4 (TW-APPLY-10, gtwpe-20261101-pf10-v14-0-5, T-08)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.4.md`: the complete revised PF29-Canon-HDE-Users-Guide, v1.0.4. 81,874 bytes; 1,085 lines, LF-terminated; SHA-256 `e3ba2c95135d1a78d20708059cc6d551602d68ac3d9b10111ecf622a9353a20e`; git blob `7a6f873a575e5f8972d9e204ce59ce315d374c6b` |
| Producing prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1. Fetched live from Notion page `3f44590a05eb81eebff6e3afa3d9aa5b` when this step began, on 2026-11-02; the page records "Prompt Version: 100926.1" and was last edited 2026-10-09T11:05:22Z. |
| Applier | The same Claude Code document session that prepared the package, https://claude.ai/code/session_01Q789u3KLSaV6qHFgm3m8t4. Nathan's T-08 handoff authorizes preparation and then application in this session. No subagent, reviewer or other session took part. |
| Execution date | 2026-11-02 (UTC; the application ran at about 2026-11-02T00:27Z) |
| Outcome | Applied. 13 operations: 10 content redlines and 3 derived header fields. Both outputs were saved and read back (§8). |
| Standing | The revised PF is an ephemeral output for Nathan's review and merge. It is not a publication into `docs/pfcanon/`, and it establishes no QA, acceptance, deployment or closure. |

## 2. Inputs

| Input | Identity |
| :---- | :---- |
| Exact original (application baseline) | `docs/pfcanon/PF29-Canon-HDE-Users-Guide-v1.0.3.md` at `e2b7427ff418ca8f08f05587c4a541308a76da56`, read from the git object. Git blob `6730222d2f352221ddbe140a08c260380bbf5abc`; SHA-256 `2ef3b8a7bfabbc768bf0ae1799d29449fe3ecdc37b509a03dd7292f09f0c8301`; 76,613 bytes; 1,079 lines; no CR bytes. |
| Current authoritative copy | `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, fetched at application time. It is the same blob, and it is the only PF29 file under `docs/pfcanon/`, so there is no drift from the preparation baseline. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.md` at package commit `285bc728eb3c39de37e6d4842292ea36b421f256`. Git blob `5f45e2b218da2496cd9239809d025c8dff53fdf3`; SHA-256 `9a5b8b85e143e64e9e25d4f4c008620bcde40463008cd1175d1e35be6b91d10f`. Read from the git object. |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.3.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` at `285bc72`, git blob `48daf34f454d6acbff167f7bf0bd6239057702b2` |
| Preparer and run | TW-DRAIN-10 100926.1, this session; run `gtwpe-20261101-pf10-v14-0-5/T-08/drain-r1` |
| Preparation and save outcome | `READY` / `COMPLETE_PACKAGE`. No blocking change or dependency. H-05 (AGENTS.md) is held as not a PF target, so it does not block the package. |
| Change source | PF10-HDE-Build-Notes v14.0.5, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`. The same blob is at `e2b7427` and `84d6d1c`. |
| Selected source units | Addendum 2.1: D-1 (lines 225–276), D-2 (277–344), D-3 (345–396); context 205–224 and 491–516. These agree with Nathan's handoff and the ledger rows. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` (recorded at `142feb35144d8795f927e0c78b665ace52279064`). Task T-08; rows C-01, C-02, C-03; supporting C-06. |
| Editorial standard | PF03-Reference-Technical-Writing-Best-Practices v1.8.8, read in full in this session. No PF03 cleanup was performed at this step. |

Preflight reused the complete reading of the original from the preparation step. That reading was of the same verified blob, and its coverage is retained in the preparation proof log §2.

## 3. Intake and preparation-state verification

The intake checks used the committed package bytes, not working-tree copies:

- the redlines file ends with `END OF REDLINES`;
- it declares `READY`;
- it binds the baseline blob, the baseline SHA-256 and the baseline commit.

The preparation proof log records:

- complete target reading;
- complete reading of the selected units;
- a disposition for every item in D-1, D-2, D-3 and the C-06 context;
- no blocking item;
- `COMPLETE_PACKAGE` save verification.

The preparer and the applier are the same session, and the handoff authorizes both steps. No unselected PF10 addendum was needed.

## 4. Operation ledger and basis

Each operation was resolved independently against the unchanged original before any byte was written. Expected and observed occurrence is 1 for each. Every span is line-bounded, and the sorted spans are strictly disjoint. The basis for each content redline is restated from the preparation proof log: its rationale, followed by the ledger row and the PF10 2.1 lines it drains.

| ID | Kind | Original lines | Basis |
| :---- | :---- | :---- | :---- |
| RL-01 | content, CONSISTENCY | §1.1, 81 | Records the repository snapshot inspected for the new current-gap statements (`e2b7427`), as PF29 §0.2 requires and PF03 §4 expects. C-01, C-02, C-03. |
| RL-02 | content, CONSISTENCY | §1.1, 92 | The `hdctl bg:resolve` row restated "Non-v2 configured bases preserve explicit legacy BodyGraph fallback", which D-2 supersedes. It now states the terminal-v1 route and `\[Current gap\]`. C-02 (2.1 D-2, lines 277–344). |
| RL-03 | content, CANON_UPDATE | §11.3, 712–714 | D-2 supersedes §11.3. The legacy route is reached only with a base whose final path segment is exactly `v1`; it is retained legacy selection, not fallback; every other non-v2 base must fail with `PROVIDER_ROUTE_UNSUPPORTED`. The checked-in classifier does not yet fail closed, so the text is marked `\[Current gap\]`. C-02 (lines 281–298, 312–314). |
| RL-04 | content, CANON_UPDATE | §13.3, 838 | D-2 supersedes "With a non-v2 configured base, explicit legacy fallback may proceed". C-02 (line 314). |
| RL-05 | content, CANON_UPDATE | §13.3, 848 | D-1 extends the production override to `showcompat --source vendor` and vendor-selecting conjunction: the same classification, initiator rule, audit, codes and carrier, and exit 64 when no vendor acquisition is selected. The checked-in CLI does not do this yet, so the text is marked `\[Current gap\]`. The §13.3 fallback sentence follows D-2. C-01 (lines 229–244, 265); C-02 (line 314). |
| RL-06 | content, CANON_UPDATE | §16, 963 | D-3: the compat namespace is dev/admin-only. Outside production-like posture it is served only when `APP_ENV` is exactly `dev`, `test` or `local`; otherwise it refuses with `ERR_WRITER_FORBIDDEN` (403). The checked-in guard refuses only production-like posture, so the text is marked `\[Current gap\]`. C-03 (lines 349–364, 386). |
| RL-07 | content, CANON_UPDATE | §16, 969 | D-2 supersedes "For non-v2 configured bases, explicit legacy BodyGraph fallback is preserved". C-02 (line 314). |
| RL-08 | content, CANON_UPDATE | §16, 985 | D-1 drains into the §16 production-override limit, with the current gap. C-01 (lines 229–237, 265). |
| RL-09 | content, CANON_UPDATE | §17, 998 | D-3: the row "HTTP 404 from POST /api/compat/v1 in prod" gains the non-production refusal, with the current gap. C-03 (lines 351–354, 386). PF10 cites the row under "§16"; in PF29 it is in §17, and it was resolved by its unique literal text. |
| RL-10 | content, CANON_UPDATE | §17, 1006 | D-1: the row for `PROVIDER_PROD_OVERRIDE_REQUIRED`, `PROVIDER_PROD_OVERRIDE_INVALID` and `PROVIDER_AUDIT_UNAVAILABLE` gains the showcompat scope, with the current gap. C-01 (lines 242–244, 265). |
| META-VERSION | header | §0.1, 7 | Standing document-control authority of TW-APPLY-10 |
| META-DATE | header | §0.1, 11 | Standing document-control authority of TW-APPLY-10 |
| META-GATE | header | §0.1, 13 | Standing document-control authority of TW-APPLY-10 |

The current-gap qualifiers rest on the preparer's bounded read-only inspection at `e2b7427`, recorded with paths, blobs and lines in the preparation proof log §4. This Apply step did not re-decide domain correctness, and it did not change any payload.

## 5. Document-control plan

| Field | Before | After | Derivation |
| :---- | :---- | :---- | :---- |
| Version | `v1.0.3` | `v1.0.4` | The final numeric component of the native dotted version is incremented once. The `v` prefix and the three components are kept. |
| Effective date | `2026-10-26` | `2026-11-02` | The actual application execution date, in the native `YYYY-MM-DD` format |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` | `BN 14.0.5` | The one source the package records, PF10-HDE-Build-Notes v14.0.5 (file `PF10-HDE-Build-Notes-v14.0.5.md`), written as `BN` and its version. No other source justified this update. |
| Status | `Canon` | `Canon` | Not stale; it is unchanged |
| Title, Invocation tag | `PF29-Canon-HDE-Users-Guide`, `INV-f2ac55d77ce9aacc` | unchanged | Protected |

- Internal restatements: the original contains no other occurrence of `1.0.3`, `2026-10-26` or the old gate, so nothing else needed synchronizing.
- Change history: PF29 has no change-log, revision-history or Doc-Delta section, and its rules require no history entry, so none was needed.
- Overlap: the package has no header redline, so no duplicate authorization needed reconciling, and the header spans (lines 7, 11, 13) do not overlap any content span.
- Agreement: all version, date and gate values agree with one another.

## 6. Application and preservation

The operations were applied once, in descending original offset, without rematching changed text. Text was handled as UTF-8 and written as raw bytes.

Preservation audit. The script walked the original and the output in step. Every untouched original interval is byte-identical in the output: 72,456 of 76,550 original characters, which is all of them outside the 13 consumed spans. Every payload sits at its planned position. The untouched tail is identical.

Independent cross-checks:

- `diff` of the original against the output shows exactly 14 hunks for the 13 operations, at lines 7, 11, 13, 81, 92, 712, 714, 838, 848, 963, 969, 985, 998 and 1006 of the original. RL-03 appears as two hunks, at 712 and 714, because its unchanged blank line 713 separates them.
- `diff` of the preparer's simulated body (SHA-256 `c5fefd1f89330a5ed5c9a160cb6d2bcc11b975e161c25a33d7678be12195cfd8`) against the output differs only in the three header lines.

Text checks, all passing:

- one final LF and no CR;
- fence-line count, table-row count and the full list of heading lines unchanged;
- exactly one each of `Version`, `Effective date` and `Last Update Gate`, with the planned values;
- Status, Title and Invocation tag unchanged;
- no `1.0.3` restatement left;
- no ASCII or Unicode ellipsis;
- no `Draft`, `TODO`, `TBD` or `FIXME` marker.

The baseline's command placeholders, such as `<AUTHORIZATION_REF>`, `<user_a>` and `YYYY-MM-DD`, are example inputs in operator recipes. They are not drafting placeholders, and they are unchanged.

Byte counts: the original is 76,613 bytes and 1,079 lines; the output is 81,874 bytes and 1,085 lines. These are text checks, not product QA.

## 7. Limitations and deviations

- The `\[Current gap\]` statements describe checked-in bytes at `e2b7427`. They prove no runtime or deployed behavior. When Candidate CRD Items List item 9 is delivered, those statements become stale and need a later drain.
- The preparer recorded these items for Nathan; they are carried forward unchanged:
  - RL-01 and RL-02 edit §1.1, outside the handoff's named sections, as CONSISTENCY;
  - the §11.3 heading "Non-v2 legacy fallback" is kept, because renaming it needs Nathan's explicit authorization;
  - §7.5, §9.2, the §17 `PROVIDER_CONFIG_INVALID` row and the compat 404 lines elsewhere were not drafted.
- H-05, the AGENTS.md edits under D-1 and D-2, is held for the Product Owner's explicit instruction and is not drafted.

## 8. Save verification

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF29/PF29-Canon-HDE-Users-Guide-v1.0.4.md` | 81,874 | `e3ba2c95135d1a78d20708059cc6d551602d68ac3d9b10111ecf622a9353a20e` | Complete. All bytes were read from disk, hashed, and compared by full `diff` with the original and with the expected stream. |
| This proof log | — | — | Complete, after writing. A self-referential hash is not recorded. |

## 9. Next manual action

Nathan reviews the revised PF on draft PR amthorn78/glow-hdengine-v2#826, branch `claude/gtwpe-triage-authoring-j94ewf`, and decides on merge and on publication into `docs/pfcanon/`. Neither step is performed here.
