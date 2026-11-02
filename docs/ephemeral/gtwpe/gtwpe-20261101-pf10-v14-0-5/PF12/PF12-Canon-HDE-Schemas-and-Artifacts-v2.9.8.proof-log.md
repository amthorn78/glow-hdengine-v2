# Proof log — PF12 application — HDE Schemas and Artifacts v2.9.8 — gtwpe-20261101-pf10-v14-0-5 (T-04)

## 1. Artifact and association

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md`, the complete revised PF |
| Artifact identity | 653,450 bytes; 6,402 LF characters; UTF-8, no CR; it ends with two LF bytes, as the original does; SHA-256 `2f7be7fb829d37e42033c44256e0c6b72a9d9db624d9f777ce8de01f273209ec` |
| This proof log | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.proof-log.md`, beside it. It does not record its own hash. |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1. Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when the step began and again when it restarted on the corrected package; "Prompt Version: 100926.1"; last edited 2026-10-09T11:05:22Z |
| Session | The one Claude Code session Nathan started for T-04. It prepared the package (TW-DRAIN-10) and applied it (TW-APPLY-10) as separate steps, as the handoff authorizes. No subagent, reviewer or other session took part. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-04 / application of preparation revision r3 |
| Outcome | Applied. Eleven content operations and the derived three-field header plan; validation and preservation checks passed (§§6 to 8). |
| Standing | The revised PF is a document output under `docs/ephemeral/`. It is not authoritative publication: `docs/pfcanon/` is unchanged, and placing the file there is Nathan's manual action. |

## 2. Inputs and identities

| Role | Identity |
| :---- | :---- |
| Original (exact application baseline) | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`, PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7, read at `origin/main` `e2b7427` and unchanged on `origin/main` `84d6d1c` when applied; Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3`; raw-byte SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`; 640,642 bytes; 6,264 LF characters, the last line empty |
| Redlines (r3) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` at commit `4c859cc`; SHA-256 `b9c38a823fa5aa3223e8c32a4ccdb33ee65895f12d8ac721a5f48fe8db9861b3`; 38,187 bytes |
| Preparation proof log (r3) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` at commit `4c859cc`; SHA-256 `ae5c452e1c26be5acb29ca330b10e4b9a320ed8ec1af7ca8b07cd0ca80148793` |
| Earlier package and its return | r2 at `2a2325b` was returned by `PF12-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` (commit `5716f60`; SHA-256 `46d94737b6b30e5bd2d6771542936e028f98ff6ac74e0b8f6487ec1cc38f6084`). Its baseline byte-shape statement said "ends with one LF", against the original's LF LF. Zero edits were applied in that attempt. r1 at `324de26` was superseded by the preparer before any Apply. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` |
| Selected source units | 2.1 D-4 (397–450), D-5 (451–490) and context (205–224, 491–516); 2.2 (517–561); 2.8 decisions and drainage table (1063–1106, 1111–1127); 2.16 status, R-1 and R-2 (1869–1939). This matches the handoff and the ledger's T-04 row. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-04; rows C-04, C-05, C-10, C-17, C-18; uncertain C-07 (decided actionable) and C-29 (decided no PF12 home); supporting C-06, C-20 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, read in full in this session |

## 3. Intake and preparation-state verification (r3)

- Preparation outcome `READY` and save outcome `COMPLETE_PACKAGE` are recorded in both files (redlines "Package identity"; proof log §1 and the receipt in §15). The redlines file ends with `END OF REDLINES`.
- The originating preparer is TW-DRAIN-10 100926.1 in this same session (proof log §1). The run identity is `gtwpe-20261101-pf10-v14-0-5` / T-04 / r3.
- The baseline matches the preparer's evidence. Git blob, raw-byte SHA-256 and byte count are equal; the byte-shape statement (6,264 LF characters, final empty line, two final LF bytes) now matches the raw bytes; the original is unchanged on current `origin/main`.
- The proof log records complete target reading (18 windows covering lines 1–6,264) and complete reading of the selected units. It records no unresolved item and no blocking dependency, and the one held item (H-07) is not drafted.
- Header provenance supplied by the preparer: baseline header schema, and the source in source order, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5.

## 4. Derived document-control plan

| Field | Before | After | Basis |
| :---- | :---- | :---- | :---- |
| Version | v2.9.7 | v2.9.8 | Final numeric component incremented once (the established scheme: v2.9.5, v2.9.6, v2.9.7) |
| Effective date | 2026-10-26 | 2026-11-02 | Actual application execution date (`date -u`: 2026-11-02T00:36Z at the first validation; same date when applied) |
| Last Update Gate | BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md | BN 14.0.5 | The only recorded source is PF10 v14.0.5, giving `BN 14.0.5`; the ledger and the redlines file are not gate sources |
| Status | Canon | Canon (unchanged) | Not stale; PF12 is canon |
| Title, Invocation tag | unchanged | unchanged | Not authorized and not needed |

Each changed line keeps its native form, including the bold label and the two trailing spaces. No other document-control field exists in §0.1. No internal restatement of the current version or date needed synchronizing. The remaining `v2.9.7` and `2026-10-26` occurrences are inside the dated historical record §9.6 (output l.6062–6181), which keeps its values.

The revision-history entry required by PF12 §9.1 is RL-11's §9.7 record. It names `document_version: "v2.9.8"`, `date: "2026-11-02"`, the heading date 2026-11-02, and the `change_log_entry` "v2.9.8 / 2026-11-02". All four agree with the plan.

## 5. Operation ledger and basis

Each operation was resolved against the unchanged original. Its basis is the rationale and source-ledger reference the preparer's proof log gives, summarized here.

| ID | Operation | Original location | Rows | Basis |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT, gap before l.551 | §1.2, after the "Canonical JSON gate artifacts" block | C-05 | 2.1 D-5: governed gate check rows carry closed issue tokens and repository-relative paths only, and diagnostics go to stderr. D-5 adds this row-content rule to §1.2 "Canonical JSON gate artifacts". The text says that current enforcement is not asserted, because the implementing change (item 9) is open. |
| RL-02 | REPLACE l.603 | §1.2 "Generic close-pack writer (normative)." | C-10, C-18, C-17 | 2.8 amendment B-1 (Epic tracked-issue ID form; `TRACKED_ISSUE_UNBOUND`) and the stated limit that a tracked issue maps only through an ADR status. 2.2 "Changes delivered" and 2.8 l.1059 (a): the v2 source records `planning_records`, `requirement_ids`, `qa_checks` and `qa_verdict`, with no plan path; the writer checks their form only (2.8 l.1090). |
| RL-03 | REPLACE l.605 | same list | C-10, C-17 | 2.2 "Changes delivered" and 2.8 decision 6 and l.1059 (b), (c): no `docs/ephemeral/` or `docs/pfcanon/` path as causal input, pointer or key output (`PLANNING_OR_CANON_INPUT_PROHIBITED`); record-text naming of planning documents; deferral register by PF title and heading (l.1095); write-time-only PF title resolution; check mode reads no PF-Canon file. |
| RL-04 | REPLACE l.607 | same list | C-18, C-17 | 2.8 decision 8 as amended by B-3: absent-tolerant `epicNNN.close_report` and `epicNNN.manifest` rows with `epic_id` for an Epic in `ADMITTED_EPIC_CLOSE`; a later Epic needs its own row (l.1103). |
| RL-05 | REPLACE l.668 | §1.2 "Same-run close evidence" paragraph | C-18, C-17 | 2.8 decision 7 as amended by B-4 (the Epic close-run family) and B-2 (the close-run pointer: a CRD must point to its own, an Epic may; `POINTER_UNRESOLVED`). It replaces the false statement "No Epic close-run family is admitted". |
| RL-06 | REPLACE l.2049 | §6.2.1 "External release attestation" | C-04 | 2.1 D-4: exclusive claim of the output root, no writes through symlinks, scoped cleanup; refusal list and interface unchanged; mechanism not fixed. The text says that current enforcement is not asserted (item 9 open). |
| RL-07 | REPLACE l.2262 | §8.3 "Governed locations only." | C-07, C-10 | 2.2 R-1 (no Index or Mirror row or path proof binds `docs/ephemeral/`) and R-2 (no governed artifact pins a PF file name, version or digest), as they bear on PF12's Mirror path rules. The preparer decided this by context and scope under GTWPE-D3, and found no current row binding such a path. |
| RL-08 | REPLACE l.2971–2972 | §8.6.3.2 "Canonical JSON and topology" | C-05 | 2.1 D-5 drainage target "the Evidence Catalog entry 'Canonical JSON and topology'". The entries point to the §1.2 rule so that it keeps one home (PF12 §0.2 "Evidence Catalog"). |
| RL-09 | REPLACE l.5399–5408 | §8.17 "Close-run family exception" | C-18, C-17 | 2.8 decision 7 (B-4) and the admission limit: `ADMITTED_EPIC_CLOSE` admits HDE-EPIC041 only; `publish_epic_close_run_family` and the QA harness's renderer; the Epic's QA family is neither written nor allowed to change during publication; `epic_id` on rows. It replaces "admitted CRDs only" and "No Epic close-run family is admitted". |
| RL-10 | REPLACE l.5424 | §8.17.1 `close/` bullet | C-18, C-17 | Same basis as RL-09, for the root layout list. |
| RL-11 | INSERT, gap before l.6165 | after §9.6, before Appendix A | C-04, C-05, C-07, C-10, C-17, C-18 | PF12 §9.1 requires a Doc-Delta for governed-evidence rule changes. This §9.7 documentary drainage record follows the §§9.5 and 9.6 form and cites HDE Build Notes by title only (§0.2). |

The preparer's read-only repository inspection at `e2b7427` (its proof log §8) supports the literal names used: `ADMITTED_EPIC_CLOSE`, `publish_epic_close_run_family`, the refusal codes and the `ti_id` pattern. Application did not re-run that inspection; it adds no new repository claim.

## 6. Whole-batch validation

An application script independent of the preparer's builder parsed the committed r3 file by its literal-block convention.

| ID | Operation | Expected | Observed | Original span or gap (characters) | Payload length | Payload occurrences in output |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT | 1 | 1 | gap 42,968 | 974 | 1 |
| RL-02 | REPLACE | 1 | 1 | 47,027–47,259 | 1,134 | 1 |
| RL-03 | REPLACE | 1 | 1 | 47,570–48,072 | 1,107 | 1 |
| RL-04 | REPLACE | 1 | 1 | 48,350–48,766 | 870 | 1 |
| RL-05 | REPLACE | 1 | 1 | 53,920–54,660 | 1,164 | 1 |
| RL-06 | REPLACE | 1 | 1 | 190,147–190,560 | 1,505 | 1 |
| RL-07 | REPLACE | 1 | 1 | 210,464–210,690 | 461 | 1 |
| RL-08 | REPLACE | 1 | 1 | 256,293–256,424 | 245 | 1 |
| RL-09 | REPLACE | 1 | 1 | 587,223–589,738 | 3,225 | 1 |
| RL-10 | REPLACE | 1 | 1 | 590,517–590,721 | 249 | 1 |
| RL-11 | INSERT | 1 | 1 | gap 630,886 | 7,337 | 1 |
| Version | REPLACE (metadata) | 1 | 1 | 114–135 | 21 | 1 |
| Effective date | REPLACE (metadata) | 1 | 1 | 156–188 | 32 | 1 |
| Last Update Gate | REPLACE (metadata) | 1 | 1 | 189–314 | 33 | 1 |

- Operations: `REPLACE` and `INSERT` only. No `DELETE`, no repeated replacement, so the RL-045 preflight does not apply.
- Conflicts: none. No spans intersect, no insertion sits at or inside a replaced boundary, no two insertions share a gap, and the metadata lines do not touch any content operation.
- Agreement: version, effective date, gate and the §9.7 record agree (§4).
- Stale markers: none. The only `DRAFT` match in the output is the canon decision name `SCHEMA-DRAFT`, also present in the original. No TODO, placeholder or drafting note was added.

## 7. Application and preservation

- Applied in descending original offset, in one pass, without rematching changed text; UTF-8 handled as text with no line-ending conversion.
- Reconstruction audit: the expected stream built from the 15 untouched original intervals and the 14 payloads equals the output exactly.
- Mapped-offset audit: each of the 15 untouched intervals and each payload sits at its mapped output offset.
- EOF and whitespace: the output ends with two LF bytes, as the original does; there is no CR in either file; trailing double spaces on list and header lines are preserved; tables and code fences outside the edited spans are untouched intervals.
- Cross-check with the preparer: with the three header lines reverted, the output's SHA-256 is `07331ff4e0c41b1acb75fafb2718624d9d692a8adfaac38b1da71dc34ffe83f1`, the preparer's recorded simulation.
- Line diff against the original: 16 hunks, at original lines 6, 8–9, after 550, 603, 605, 607, 668, 2049, 2262, 2971–2972, 5399, after 5401, 5404, 5407–5408, 5424 and after 6162, all inside the operations above. The last hunk is RL-11; `diff` aligns that insertion two lines earlier than its true gap, before l.6165, because the lines around the gap repeat.
- Byte counts: original 640,642 bytes (SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`); output 653,450 bytes (SHA-256 `2f7be7fb829d37e42033c44256e0c6b72a9d9db624d9f777ce8de01f273209ec`).

These are text checks. They are not product QA, not a test run and not governed evidence.

## 8. Read-back of the saved output

- `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md` was written by copying the audited output, and `cmp` confirms it is byte-identical. Its SHA-256 and size match §1.
- Every changed line was read back from the saved file, through a line diff against the original.
- Every unchanged byte is proven equal to the original by the reconstruction and mapped-offset audits. The original itself was read in full in this session.
- This proof log was read back after writing; §10 records the receipt.

## 9. Constraints, limitations and next action

- No PF canon was edited. Placing v2.9.8 in `docs/pfcanon/`, and retiring v2.9.7 there, is Nathan's manual action. Until then PF12 v2.9.7 on `main` stays the governing canon, together with HDE Build Notes.
- RL-06 and RL-01 state requirements whose implementing change is open; the revised PF says so.
- Items the preparer reported for Nathan, not acted on here (preparation proof log §13):
  - a possible D-2 routing to PF12 §8.6.3.10;
  - a possible 2.16 qualification of PF12 §8.6.3.3 "Compat closure artifacts";
  - the stale `release_id` in §5.3;
  - a Unicode ellipsis at original l.1968 and a doubled period at l.2144.
- H-07 (CCR-1, the acceptance-map question) stays held; PF12 "Optional token compatibility" is unchanged.
- Next manual action: Nathan reviews the shared draft PR, amthorn78/glow-hdengine-v2#826, and merges when ready, then publishes the revised PF to canon if he accepts it.

## 10. Save verification and completion receipt

Both required outputs are in `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/` and were verified from disk before this receipt was written:

- `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md`: 653,450 bytes; SHA-256 `2f7be7fb829d37e42033c44256e0c6b72a9d9db624d9f777ce8de01f273209ec`; verified as in §8.
- this proof log: read back in full; after that, only this receipt was added, and it was read back too.

Application outcome: applied and verified. The commit that holds both files is reported in the session's final response and in the ledger's T-04 row; this log does not carry its own commit.
