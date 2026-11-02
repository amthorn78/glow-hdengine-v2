# Proof log — PF06-Canon-Change-Process-Guide-v2.5.6 (application report)

This is the application report for `PF06-Canon-Change-Process-Guide-v2.5.6.md`, which sits beside it in `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/`. It records how that revised PF was produced from the original and the validated redlines, and what was verified. The revised PF is a working output under `docs/ephemeral/`; it is not publication into `docs/pfcanon/`.

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/PF06-Canon-Change-Process-Guide-v2.5.6.md`; in-document title `PF06-Canon-Change-Process-Guide`, version `v2.5.6`; SHA-256 `8dc7b239df9200f3596efa9fc72fe001ab2b5685db037c4e111472e90f869692`; 445,209 bytes; 4,720 lines; UTF-8, LF only |
| Run identity | `gtwpe-20261101-pf10-v14-0-5` / task T-03 / package revision `r1` |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b` (page last edited 2026-10-09T11:05:22.094Z), fetched live when this step began on 2026-11-02 |
| Authorization | Nathan's T-03 document-session handoff, which authorizes TW-DRAIN-10 and then, after a `READY` / `COMPLETE_PACKAGE` result, TW-APPLY-10 in the same session |
| Applier | The same T-03 document session that prepared the package: a Claude Code session on `amthorn78/glow-hdengine-v2`, session `session_01Q789tyV3UxPrkptsceraud`. The Apply step ran under its own prompt and did not alter the package. |
| Execution date | 2026-11-02 (UTC) |
| Outcome | Applied. Six content redlines and the derived document-control plan applied in one pass; every verification passed (section 6). Save completeness: `COMPLETE_PACKAGE` (section 8). |

## 2. Inputs

| Input | Identity | Read |
| :---- | :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.5.md`, v2.5.5; git blob `e9f4d7d6146364f7c59ed360990d8c4ec633a59f`; SHA-256 `d046d7eeed6eee029b63392bc32cd67d9073f7c31ff9676a0448c11a2bce21c2`; 439,442 bytes; 4,684 lines. The preparer's baseline is `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. Current `origin/main` at application, `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, carries the same blob, and PF06 v2.5.5 is the only PF06 file there, so there was no drift. | Complete. Read in full in this session in eleven recorded windows (preparer proof log section 4). Byte-identical to the file used at application (SHA-256 recomputed). |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.md` at commit `7e710d5c5a69617f896fb1db8bb07ad515491e0f`; SHA-256 `66440a90596f23626285229621427564a953c38b10a79b76a66c8979402548a2`; 19,172 bytes | Complete; ends with `END OF REDLINES` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/PF06-Canon-Change-Process-Guide-v2.5.5.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md` at `7e710d5`; SHA-256 `1d6202da7611465982d47357823314e0f359585ec638abe0e7ffddc4473a6d6c` | Complete |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`, unchanged on current `origin/main` | Selected units, as the preparer's selection records them: 2.2 lines 517–561; 2.8 lines 1063–1106 and 1111–1127, with 1060; 2.15 lines 1650–1804. Supporting: 2.8 lines 1048–1062, 1107–1110 and 1128–1145; 2.9 lines 1146–1229; 2.16 lines 1940–1948. All were read completely in this session. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-03; rows C-10, C-17, C-18, C-26; uncertain C-07; supporting C-20 | Complete |
| Editorial standard | `PF03-Reference-Technical-Writing-Best-Practices` v1.8.8 (blob `504712df548a02f3aa4e7b8c37027385e46a3878`) | Complete |

Preparation-state verification. The preparation proof log records the facts below, and each was checked against the files:

* the preparer and session, and the run and package identity;
* the original's identity and fingerprint representation, raw-byte SHA-256 of the Markdown file, which was compared with the same representation;
* the source version and the selected boundaries, which match the handoff and ledger;
* complete coverage of the target and the selected units;
* the preparation outcome `READY` and save completeness `COMPLETE_PACKAGE`.

The three held items, H-06, H-07 and H-08, are named with what each waits for and are not part of the package. No blocking item is open.

## 3. Operation ledger and basis

Every operation was resolved independently against the unchanged original, then the whole batch, with the header plan, was checked for conflict before any byte was written. Rationale and source rows are those the preparation proof log gives (its sections 5 and 6).

| ID | Operation | Expected / observed | Original location | Output location | Change and basis |
| :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | REPLACE | 1 / 1 | §3.5.2 > §3.5.2.1 "Close-pack files", line 3004, bytes [301684, 302463) | bytes [301639, 303956) | Extends the close-run-family paragraph to an Epic admitted in the canonical evidence updater's Epic close admission, defines `<change-dir>` for a CRD and an Epic, and states that an Epic close run needs its own explicit Product Owner admission, with HDE-EPIC041 the one Epic admitted. Adds the v2 source's planning-record fields, the absence of a plan path or planning binding, the `docs/ephemeral/` and `docs/pfcanon/` input refusal (`PLANNING_OR_CANON_INPUT_PROHIBITED`), record-text naming, drain targets by PF title, and write-time-only PF-title resolution. Rows C-18, C-17, C-10, C-07. Basis: HDE Build Notes v14.0.5 2.8, l.1059, l.1060 (B-3, B-4), decision 7 l.1082, stated limit l.1103, l.1109, l.1117, l.1127; 2.2 l.525, l.533–545, l.556 |
| RL-02 | REPLACE | 1 / 1 | §3.5.2.1, tracked-issue bullet, line 3011, bytes [303163, 303854) | bytes [304656, 305551) | Adds the Epic tracked-issue ID form `ISSUE-EPIC<NNN>-TI-<nn>` beside `TI-NNN` and the `TRACKED_ISSUE_UNBOUND` refusal. Rows C-18, C-17. Basis: 2.8 l.1060 (B-1), stated limit l.1099, l.1127; supporting 2.9 l.1179 |
| RL-03 | INSERT | gap 1 / 1 (BEFORE 1, AFTER 1) | §3.5.2 > §3.5.2.8 "Live QA via harness (required for epic closeout)", the gap after line 3182, byte 317228 | bytes [318925, 322782) | Adds the live compat test every Epic's QA plan includes and its QA run executes: live vendor compat, the deployed-service check, the SYN-A and SYN-B fixtures, the Epic's own live surfaces, what does not satisfy it, and the other controls that still govern. Then adds the `Live test:` line at every stage, the `MISSING` effects table, the Product Owner-only waiver and the prompt rule. Row C-26 (R-1, R-4). Basis: 2.15 l.1666–1681, R-1 l.1704–1740, R-4 l.1761–1786; supporting 2.16 R-3 l.1940–1948 |
| RL-04 | REPLACE | 1 / 1 | §3.5.2.8, functional-proof exemption bullet, line 3195, bytes [318797, 319145) | bytes [324351, 324801) | The IG-validated functional-proof exemption never exempts an Epic from the live compat test, which only the Product Owner may waive. Row C-26 (R-1). Basis: 2.15 R-1 l.1706, R-2 l.1743 as R-4 l.1784 restates it, l.1671–1676 |
| RL-05 | REPLACE | 1 / 1 | §3.5.2.8, Live QA plan rails bullet, line 3200, bytes [319311, 319436) | bytes [324967, 325159) | The plan's rails posture names the step-local open-rails steps of the live compat test. Row C-26 (R-1). Basis: 2.15 R-1 l.1706, l.1708 |
| RL-06 | REPLACE | 1 / 1 | §3.5.4 "ADR block in the close-pack (all epics)", line 3348, bytes [333530, 334066) | bytes [339253, 339833) | "every check of the change's current QA plan" becomes "each of the change's QA plan checks, as recorded in the candidate source (`qa_checks`)". Rows C-17, C-07. Basis: 2.8 decision 4 l.1073, stated limit l.1093, l.1059; 2.2 l.525 |

No operation is a repeated-replacement operation, so the RL-045 preflight had nothing to reject. No conflict exists: the six content spans and gap are pairwise disjoint, and no insertion touches a replaced boundary.

## 4. Document-control header

Derived under TW-APPLY-10's header contract. No package redline touched the header, so no duplicate or conflicting header authorization exists.

| Field | Before (line) | After | Rule applied |
| :---- | :---- | :---- | :---- |
| Version | `v2.5.5` (5) | `v2.5.6` | Final numeric component of the native dotted version incremented once; prefix `v` and three components kept |
| Effective date | `2026-10-26` (9) | `2026-11-02` | The actual application execution date, in the field's native `YYYY-MM-DD` form; label style `**Effective date**:` kept |
| Last Update Gate | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` (11) | `BN 14.0.5` | From the one source that justified the update, as the package records it: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5, written `BN 14.0.5` |
| Title | `PF06-Canon-Change-Process-Guide` (3) | unchanged | Carries no embedded version |
| Status | `Canon` (7) | unchanged | Not stale; the document is permanent canon |
| Invocation tag | `INV-f2ac55d77ce9aacc` (13) | unchanged | Not authorized for change |

Internal restatements of the document's own version or date: none besides the header lines. Before application, `v2.5.5`, `2.5.5` and `2026-10-26` each occurred exactly once, on their header lines. Afterwards `v2.5.5`, `2.5.5`, `2026-10-26` and `BN 13.8.8` occur zero times and `v2.5.6` once. The target has no change log, revision history or Doc-Delta entry section, so no history entry is required; the preparer recorded the same finding. Version, date and gate agree with one another.

The revised output file name follows the target's naming scheme with the derived version: `PF06-Canon-Change-Process-Guide-v2.5.6.md`, as the handoff and ledger expected.

## 5. Constraints and interpretations

* The package was applied exactly as saved. Apply prepared no edit, changed no wording and repaired no locator.
* The original's literal Markdown escapes (for example `3\)` in headings and `\_` in prose) are source bytes, not display escapes. They were matched and preserved raw. No escape was decoded or normalized.
* Drafting-marker check: the output contains the same 43 occurrences of `TODO`, `TBD`, `FIXME`, `Draft`, `draft` and `placeholder` as the original. Every one is normative text about plans, a template that canon requires, or a name such as "Asset Draft Pack". None is status language about the document, and the payloads add none.
* The revised PF is not publication. Transferring it into `docs/pfcanon/` is Nathan's action.

## 6. Verification

Run with `apply_redlines.py`, the Apply step's own script, kept in the session scratchpad and not committed. It is separate from the preparer's validator. It parses the saved redlines file strictly, then validates the following before writing anything:

* every operation, with its counts, anchors and payloads;
* the header plan, with field uniqueness and shape;
* restatement literals;
* whole-batch conflict.

It then applies the plan in descending offset order on the original bytes.

| Check | Result |
| :---- | :---- |
| Reconstructed expected byte stream equals the output | PASS |
| Every untouched original interval preserved at its computed output offset (10 intervals; 436,835 bytes) | PASS |
| Every payload present at its computed output offset (6 content payloads, 3 header lines) | PASS |
| EOF shape unchanged (the original and the output both end with one LF after the last line, followed by one empty line) | PASS |
| No CR introduced; no ellipsis form introduced | PASS |
| Version appears once at `v2.5.6`; `v2.5.5` absent | PASS |
| Status `Canon` unchanged and not Draft; title and invocation tag unchanged | PASS |
| Heading inventory identical (no heading added, removed or changed) | PASS |
| Cross-check: the preparer's simulated output, with the three header lines replaced, is byte-identical to the output | PASS |

Byte counts: original 439,442 bytes and 4,684 lines; output 445,209 bytes and 4,720 lines. Diff hunks, original to output: lines 5, 9 and 11 (header); 3004 (one line becomes three); 3011; the insertion after 3182 (34 lines); 3195; 3200; 3348. There are no others.

These are text checks of the document. They are not product QA and establish no QA verdict, acceptance, drainage into `docs/pfcanon/`, or closure.

## 7. Unresolved items, limitations and deviations

* Held, not part of this revision:
  * H-06 (CCR-5, §3.5.1) waits for the Product Owner's correcting HDE Build Notes addendum.
  * H-07 (CCR-1, the acceptance-map question at §3.5.2.1) waits for the Product Owner's decision.
  * H-08 (CCR-6, §0.7 and the §3.5.2.8 "Live QA evidence landing" paragraph) waits for the Product Owner's canon disposition.
  * Their spans are unchanged in the output.
* The observations outside the assigned scope, O-1 to O-5, are recorded in the preparation proof log, section 8. None was acted on.
* Deviations: none. The package was applied as validated, with no correction round.

## 8. Save and completion receipt

| File | Repository path | Verified |
| :---- | :---- | :---- |
| Revised PF | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF06/PF06-Canon-Change-Process-Guide-v2.5.6.md` | Read back in full and compared byte for byte with the verified output: identical, SHA-256 `8dc7b239df9200f3596efa9fc72fe001ab2b5685db037c4e111472e90f869692`, 445,209 bytes |
| Application report | This file, beside the revised PF | Read back in full after writing |

Save completeness: `COMPLETE_PACKAGE`.

Next manual action: Nathan reviews the shared draft PR amthorn78/glow-hdengine-v2#826 and decides whether and when to transfer the revised Change Process Guide into `docs/pfcanon/` and merge. No further TW step is owed for T-03.
