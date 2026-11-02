# Proof log — PF12 application — HDE Schemas and Artifacts v2.9.8 — gtwpe-20261101-pf10-v14-0-5 (T-04)

## 1. Artifact and association

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md`, the complete revised PF |
| Artifact identity | 658,081 bytes; 6,441 LF characters; UTF-8, no CR; it ends with two LF bytes, as the original does; SHA-256 `9b67dd2a22f84b4179e44df09acd7a6840de336401e0d83214db542eaa58c0eb` |
| This proof log | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.proof-log.md`, beside it. It does not record its own hash. |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1. Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when each application step began (r2, r3 and r4); "Prompt Version: 100926.1"; last edited 2026-10-09T11:05:22Z |
| Session | The one Claude Code session Nathan started for T-04. It prepared each package revision (TW-DRAIN-10) and applied it (TW-APPLY-10) as separate steps, as the handoff authorizes. No subagent, reviewer or other session took part. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-04 / application of preparation revision r4 |
| Supersedes | The application of r3 at this same path (commit `5c10ee5`; output SHA-256 `2f7be7fb829d37e42033c44256e0c6b72a9d9db624d9f777ce8de01f273209ec`; 653,450 bytes). That file was this session's own output in this run's namespace. It was inspected before being overwritten, and it remains in Git history at `5c10ee5`. |
| Authorization | Nathan's handoff for T-04 (drain, then apply), and his direction in this session on 2026-11-02 after the r3 application was reported: "fix the defects and inconsistencies you noticed". |
| Outcome | Applied. Seventeen content operations and the derived three-field header plan; validation and preservation checks passed (§§6 to 8). |
| Standing | The revised PF is a document output under `docs/ephemeral/`. It is not authoritative publication: `docs/pfcanon/` is unchanged, and placing the file there is Nathan's manual action. |

## 2. Inputs and identities

| Role | Identity |
| :---- | :---- |
| Original (exact application baseline) | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`, PF12-Canon-HDE-Schemas-and-Artifacts v2.9.7, read at `origin/main` `e2b7427` and unchanged on `origin/main` `84d6d1c` when applied (fetched again at application); Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3`; raw-byte SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`; 640,642 bytes; 6,264 LF characters, the last line empty |
| Redlines (r4) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` at commit `8ca919b`; SHA-256 `c45c20a53334e5a2eba96ee80da8494b4c3497de054cf73188ed2cb1dd169f44`; 54,695 bytes |
| Preparation proof log (r4) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` at commit `8ca919b`; SHA-256 `446700d5ac35b38537d0307ba41baae92c54715169eba3208eb9ffa7e4383af6` |
| Earlier packages | r3 at `4c859cc`, applied at `5c10ee5` and superseded by r4 at Nathan's direction. r2 at `2a2325b`, returned by `PF12-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` (commit `5716f60`) with zero edits applied, because its baseline byte-shape statement said "ends with one LF" against the original's LF LF. r1 at `324de26`, superseded by the preparer before any Apply. |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; unchanged on `origin/main` `84d6d1c` |
| Selected source units | 2.1 D-2 (277–344, added by Nathan's direction), D-4 (397–450), D-5 (451–490) and context (205–224, 491–516); 2.2 (517–561); 2.8 decisions and drainage table (1063–1106, 1111–1127); 2.16 status, R-1 and R-2 (1869–1939). Apart from D-2, this matches the handoff and the ledger's T-04 row. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-04; rows C-04, C-05, C-10, C-17, C-18; uncertain C-07 (decided actionable) and C-29 (actionable by context at Nathan's direction); C-02 added by Nathan's direction; supporting C-06, C-20 |
| Supporting reading (preparer) | HDE CLI/API/Vendor Ref §7.1.10 and HDE CRD Records (HDE-CRD-0002 record), named in the preparation proof log §2. Neither is a change source. |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, read in full in this session |

## 3. Intake and preparation-state verification (r4)

- Preparation outcome `READY` and save outcome `COMPLETE_PACKAGE` are recorded in both files (redlines "Package identity"; proof log §1 and the receipt in §15). The redlines file ends with `END OF REDLINES`.
- Both package files were read in full in this session, at the preparer's read-back. The committed bytes at `8ca919b`, which this step parsed, have the same SHA-256 values (above), so they are the bytes that were read.
- The originating preparer is TW-DRAIN-10 100926.1 in this same session (proof log §1). The run identity is `gtwpe-20261101-pf10-v14-0-5` / T-04 / r4.
- The baseline matches the preparer's evidence: Git blob, raw-byte SHA-256, byte count and byte shape are equal, and the original is unchanged on current `origin/main`.
- The proof log records complete target reading (18 windows covering lines 1–6,264) and complete reading of the selected units, including D-2. It records no unresolved item and no blocking dependency; the one held item (H-07) is not drafted.
- Authorization for the three operations no source file justifies (RL-06, RL-07 and RL-09): the preparation proof log quotes Nathan's direction, given in this session. TW-DRAIN-10 allows hygiene with Nathan's authorization in the handoff; this step does not re-decide it.
- Header provenance supplied by the preparer: baseline header schema, and the one source in source order, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5.

## 4. Derived document-control plan

| Field | Before | After | Basis |
| :---- | :---- | :---- | :---- |
| Version | v2.9.7 | v2.9.8 | Final numeric component incremented once from the original (the established scheme: v2.9.5, v2.9.6, v2.9.7). The superseded r3 output's v2.9.8 is not a further base: both applications start from v2.9.7. |
| Effective date | 2026-10-26 | 2026-11-02 | Actual application execution date (`date -u`: 2026-11-02T02:37Z) |
| Last Update Gate | BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md; HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md | BN 14.0.5 | The only recorded source is PF10 v14.0.5, giving `BN 14.0.5`. Nathan's direction is an authorization, not a source file, and the ledger, HDE CRD Records, HDE CLI/API/Vendor Ref and the redlines file are not gate sources. |
| Status | Canon | Canon (unchanged) | Not stale; PF12 is canon |
| Title, Invocation tag | unchanged | unchanged | Not authorized and not needed |

Each changed line keeps its native form, including the bold label and the two trailing spaces. No other document-control field exists in §0.1. No internal restatement of the current version or date needed synchronizing. The remaining `v2.9.7` and `2026-10-26` occurrences are inside the dated historical record §9.6 (output l.6071–6191) and in the redlines file name cited by §9.7, which names the original's version.

The revision-history entry required by PF12 §9.1 is RL-17's §9.7 record. It names `document_version: "v2.9.8"`, `date: "2026-11-02"`, the heading date 2026-11-02, and the `change_log_entry` "v2.9.8 / 2026-11-02". All four agree with the plan.

## 5. Operation ledger and basis

Each operation was resolved against the unchanged original. Its basis is the rationale and source-ledger reference the preparer's proof log gives (§5 there), summarized here.

| ID | Operation | Original location | Rows | Basis |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT, gap before l.551 | §1.2, after the "Canonical JSON gate artifacts" block | C-05 | 2.1 D-5: governed gate check rows carry closed issue tokens and repository-relative paths only, and diagnostics go to stderr. D-5 adds this row-content rule to §1.2 "Canonical JSON gate artifacts". The text says that current enforcement is not asserted, because the implementing change (item 9) is open. |
| RL-02 | REPLACE l.603 | §1.2 "Generic close-pack writer (normative)." | C-10, C-18, C-17 | 2.8 amendment B-1 (Epic tracked-issue ID form; `TRACKED_ISSUE_UNBOUND`) and the stated limit that a tracked issue maps only through an ADR status. 2.2 "Changes delivered" and 2.8 l.1059 (a): the v2 source records `planning_records`, `requirement_ids`, `qa_checks` and `qa_verdict`, with no plan path; the writer checks their form only (2.8 l.1090). |
| RL-03 | REPLACE l.605 | same list | C-10, C-17 | 2.2 "Changes delivered" and 2.8 decision 6 and l.1059 (b), (c): no `docs/ephemeral/` or `docs/pfcanon/` path as causal input, pointer or key output (`PLANNING_OR_CANON_INPUT_PROHIBITED`); record-text naming of planning documents; deferral register by PF title and heading (l.1095); write-time-only PF title resolution; check mode reads no PF-Canon file. |
| RL-04 | REPLACE l.607 | same list | C-18, C-17 | 2.8 decision 8 as amended by B-3: absent-tolerant `epicNNN.close_report` and `epicNNN.manifest` rows with `epic_id` for an Epic in `ADMITTED_EPIC_CLOSE`; a later Epic needs its own row (l.1103). |
| RL-05 | REPLACE l.668 | §1.2 "Same-run close evidence" paragraph | C-18, C-17 | 2.8 decision 7 as amended by B-4 (the Epic close-run family) and B-2 (the close-run pointer: a CRD must point to its own, an Epic may; `POINTER_UNRESOLVED`). It replaces the false statement "No Epic close-run family is admitted". |
| RL-06 | REPLACE l.1959 | §5.3 "Current repository posture" | Product Owner direction | The paragraph gave `52be4558`'s full digest as the current `release_id`; the current manifest digest is `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e`. The preparer verified it read-only: SHA-256 of `catalog/manifest.json` at `e2b7427` and `84d6d1c`, and `python scripts/release_id_recompute.py --check-manifest-only` exit 0 under closed rails. PF12 §9.6 already records the same value. CONSISTENCY. |
| RL-07 | REPLACE l.1968–1970 | §5.3 historical cuts table | Product Owner direction | PR06b is no longer "current"; a new row records the HDE-CRD-0002 same-version refreshes and the current digest, as HDE CRD Records states (prefixes only for the intermediate values). The ellipsis after the PR06 prefix is removed (PF03 §3). CONSISTENCY and DOC\_HYGIENE. |
| RL-08 | REPLACE l.2049 | §6.2.1 "External release attestation" | C-04 | 2.1 D-4: exclusive claim of the output root, no writes through symlinks, scoped cleanup; refusal list and interface unchanged; mechanism not fixed. The text says that current enforcement is not asserted (item 9 open). |
| RL-09 | REPLACE l.2144 | §6.4, last paragraph before "Acceptance hints" | Product Owner direction | Removes the doubled period at the end of the paragraph. DOC\_HYGIENE. |
| RL-10 | REPLACE l.2262 | §8.3 "Governed locations only." | C-07, C-10 | 2.2 R-1 (no Index or Mirror row or path proof binds `docs/ephemeral/`) and R-2 (no governed artifact pins a PF file name, version or digest), as they bear on PF12's Mirror path rules. The preparer decided this by context and scope under GTWPE-D3, and found no current row binding such a path. |
| RL-11 | REPLACE l.2971–2972 | §8.6.3.2 "Canonical JSON and topology" | C-05 | 2.1 D-5 drainage target "the Evidence Catalog entry 'Canonical JSON and topology'". The entries point to the §1.2 rule so that it keeps one home (PF12 §0.2 "Evidence Catalog"). |
| RL-12 | INSERT, gap before l.3066 | §8.6.3.3 "Compat closure artifacts" | C-29 | 2.16 facts (l.1896–1899): the generator checked the placeholder `compat_public`, which HDE-EPIC040 PR-04 replaced; it has exited 2 since; its outputs are placeholder-era captures. R-1 (l.1921) defines GATE:CORE-DET evidence as the real compat path; R-2 (l.1937) keeps the captures as history. Decided by context under GTWPE-D3, at Nathan's direction. CLARIFY, with no MUST or MAY. |
| RL-13 | INSERT, gap before l.3752 | §8.6.3.10, before the mapped-cache family | C-02 | 2.1 D-2 (277–344): only a terminal `v1` base selects the legacy route, as retained selection, not fallback; other non-v2 bases fail closed; the label `explicit_legacy_fallback` makes no fallback claim; frozen HDE-EPIC036 and HDE-EPIC037 captures stay as history. Route selection is routed by title to HDE-CLI-API-Vendor-Ref. Enforcement is not asserted, because D-2's basis records the current classifier reading any segment (l.304). CLARIFY. |
| RL-14 | REPLACE l.3772 | §8.6.3.10 mapped-cache family | C-02 | D-2 as above: the family's legacy predicate is stated as preservation of the terminal-v1 selection under its existing names. The preparer confirmed read-only that the predicate is computed from a `https://fixture.invalid/v1` base. CLARIFY. |
| RL-15 | REPLACE l.5399–5408 | §8.17 "Close-run family exception" | C-18, C-17 | 2.8 decision 7 (B-4) and the admission limit: `ADMITTED_EPIC_CLOSE` admits HDE-EPIC041 only; `publish_epic_close_run_family` and the QA harness's renderer; the Epic's QA family is neither written nor allowed to change during publication; `epic_id` on rows. It replaces "admitted CRDs only" and "No Epic close-run family is admitted". |
| RL-16 | REPLACE l.5424 | §8.17.1 `close/` bullet | C-18, C-17 | Same basis as RL-15, for the root layout list. |
| RL-17 | INSERT, gap before l.6165 | after §9.6, before Appendix A | C-02, C-04, C-05, C-07, C-10, C-17, C-18, C-29, Product Owner direction | PF12 §9.1 requires a Doc-Delta for governed-evidence rule changes. This §9.7 documentary drainage record follows the §§9.5 and 9.6 form and cites HDE Build Notes by title only (§0.2). |

The preparer's read-only repository inspection (its proof log §8) supports the literal names and facts used. Application did not re-run that inspection; it adds no new repository claim.

## 6. Whole-batch validation

An application script independent of the preparer's builder parsed the committed r4 file by its literal-block convention.

| ID | Operation | Expected | Observed | Original span or gap (characters) | Payload length | Payload occurrences in output |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | INSERT | 1 | 1 | gap 42,968 | 974 | 1 |
| RL-02 | REPLACE | 1 | 1 | 47,027–47,259 | 1,134 | 1 |
| RL-03 | REPLACE | 1 | 1 | 47,570–48,072 | 1,107 | 1 |
| RL-04 | REPLACE | 1 | 1 | 48,350–48,766 | 870 | 1 |
| RL-05 | REPLACE | 1 | 1 | 53,920–54,660 | 1,164 | 1 |
| RL-06 | REPLACE | 1 | 1 | 182,071–182,564 | 493 | 1 |
| RL-07 | REPLACE | 1 | 1 | 183,398–184,002 | 1,032 | 1 |
| RL-08 | REPLACE | 1 | 1 | 190,147–190,560 | 1,505 | 1 |
| RL-09 | REPLACE | 1 | 1 | 198,510–198,744 | 233 | 1 |
| RL-10 | REPLACE | 1 | 1 | 210,464–210,690 | 461 | 1 |
| RL-11 | REPLACE | 1 | 1 | 256,293–256,424 | 245 | 1 |
| RL-12 | INSERT | 1 | 1 | gap 265,592 | 671 | 1 |
| RL-13 | INSERT | 1 | 1 | gap 365,753 | 883 | 1 |
| RL-14 | REPLACE | 1 | 1 | 367,637–368,279 | 756 | 1 |
| RL-15 | REPLACE | 1 | 1 | 587,223–589,738 | 3,225 | 1 |
| RL-16 | REPLACE | 1 | 1 | 590,517–590,721 | 249 | 1 |
| RL-17 | INSERT | 1 | 1 | gap 630,886 | 9,871 | 1 |
| Version | REPLACE (metadata) | 1 | 1 | 114–135 | 21 | 1 |
| Effective date | REPLACE (metadata) | 1 | 1 | 156–188 | 32 | 1 |
| Last Update Gate | REPLACE (metadata) | 1 | 1 | 189–314 | 33 | 1 |

- Operations: `REPLACE` and `INSERT` only. No `DELETE`, no repeated replacement, so the RL-045 preflight does not apply.
- Conflicts: none. No spans intersect, no insertion sits at or inside a replaced boundary, no two insertions share a gap, and the metadata lines do not touch any content operation.
- Agreement: version, effective date, gate and the §9.7 record agree (§4).
- Stale markers: none. The `draft` matches in the output are canon names or schema terms also present in the original (`SCHEMA-DRAFT`, JSON Schema draft identifiers, `Draft-07`, "doc delta draft/capture"). No TODO, placeholder or drafting note was added.

## 7. Application and preservation

- Applied in descending original offset, in one pass, without rematching changed text; UTF-8 handled as text with no line-ending conversion.
- Reconstruction audit: the expected stream built from the 21 untouched original intervals and the 20 payloads equals the output exactly.
- Mapped-offset audit: each of the 21 untouched intervals and each payload sits at its mapped output offset.
- EOF and whitespace: the output ends with two LF bytes, as the original does; there is no CR in either file; trailing double spaces on list and header lines are preserved; tables and code fences outside the edited spans are untouched intervals.
- Cross-check with the preparer: with the three header lines reverted, the output's SHA-256 is `a0308f1d4e86589e485ff6775d77d571acd93e009b5402109f9f6df63790ae4d`, the preparer's recorded simulation.
- Line diff against the original: hunks at original lines 6, 8–9, after 550, 603, 605, 607, 668, 1959, 1968, 1970, 2049, 2144, 2262, 2971–2972, after 3065, after 3751, 3772, 5399, after 5401, 5404, 5407–5408, 5424 and after 6162, all inside the operations above. `diff` aligns RL-17's insertion two lines earlier than its true gap, before l.6165, because the lines around the gap repeat. RL-12's and RL-13's gaps follow a blank line, so `diff` reports them after l.3065 and l.3751.
- Byte counts: original 640,642 bytes (SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`); output 658,081 bytes (SHA-256 `9b67dd2a22f84b4179e44df09acd7a6840de336401e0d83214db542eaa58c0eb`).

These are text checks. They are not product QA, not a test run and not governed evidence.

## 8. Read-back of the saved output

- `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md` was written by copying the audited output, and `cmp` confirms it is byte-identical. Its SHA-256 and size match §1.
- Every changed line was read back from the saved file through a line diff against the original. Long lines were displayed to their first 330 characters; their complete text is the package payload, which was read in full, and the audits in §7 prove the saved bytes equal it.
- Every unchanged byte is proven equal to the original by the reconstruction and mapped-offset audits. The original itself was read in full in this session.
- This proof log was read back after writing; §10 records the receipt.

## 9. Constraints, limitations and next action

- No PF canon was edited. Placing v2.9.8 in `docs/pfcanon/`, and retiring v2.9.7 there, is Nathan's manual action. Until then PF12 v2.9.7 on `main` stays the governing canon, together with HDE Build Notes.
- RL-01, RL-08 and RL-13 state requirements whose implementing change is open or not recorded as delivered; the revised PF says so.
- The four observations reported with r3 (D-2 and 2.16 bearing on PF12, the stale §5.3 `release_id`, the ellipsis and the doubled period) are applied here. One remaining observation is outside this target: HDE CLI/API/Vendor Ref's summary list (l.119) still says that non-v2 bases keep an explicit legacy fallback, which conflicts with its own §7.1.10 and with D-2; that document belongs to T-02 (preparation proof log §13).
- H-07 (CCR-1, the acceptance-map question) stays held; PF12 "Optional token compatibility" is unchanged.
- Next manual action: Nathan reviews the shared draft PR, amthorn78/glow-hdengine-v2#826, and merges when ready, then publishes the revised PF to canon if he accepts it.

## 10. Save verification and completion receipt

Both required outputs are in `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/` and were verified from disk before this receipt was written:

- `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.8.md`: 658,081 bytes; SHA-256 `9b67dd2a22f84b4179e44df09acd7a6840de336401e0d83214db542eaa58c0eb`; verified as in §8.
- this proof log: read back in full; the read-back found two inaccuracies (the line range of §9.6, and how the package files were read in §3), both corrected before this receipt. After that, only this receipt was added, and it was read back too.

Application outcome: applied and verified. The commit that holds both files is reported in the session's final response and in the ledger's T-04 row; this log does not carry its own commit.
