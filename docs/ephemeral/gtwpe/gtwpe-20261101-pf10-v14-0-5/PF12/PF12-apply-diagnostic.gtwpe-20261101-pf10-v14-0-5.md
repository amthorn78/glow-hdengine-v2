# TW-APPLY-10 diagnostic — PF12 — gtwpe-20261101-pf10-v14-0-5 (T-04)

## Outcome

Application stopped before any output was delivered. Zero edits were applied, the original is unchanged, and no revised PF was written to the repository. This diagnostic returns the package to its preparer, TW-DRAIN-10 in this same session; Nathan's handoff authorizes that return and a fresh validation of the corrected package.

| Field | Value |
| :---- | :---- |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live; "Prompt Version: 100926.1") |
| Package received | `PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` and its proof log, revision r2, at commit `2a2325b`. Redlines SHA-256 `f8909c9cf6957030cb4e8318bbd94e2f6f70a3158bf2e3e2ab1b83584b8515e0`; proof log SHA-256 `c4f15f4fe7ed68c4c989be9813cec4bbd84ce17d361a08e6116d60cbd47e242c` |
| Originating preparer | TW-DRAIN-10 100926.1, in the one Claude Code session Nathan started for T-04 (run `gtwpe-20261101-pf10-v14-0-5` / T-04 / r2) |
| Original | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`, v2.9.7, Git blob `d5bc01f83078bebe04f0854385317b47c1cd2de3`, unchanged on `origin/main` `84d6d1c`; raw-byte SHA-256 `54d8c4ad2c1a629de6e80b44de14d11e154de6169a8fb048090e30a33d4516cc`; 640,642 bytes |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-04 |
| Execution date | 2026-11-02 (UTC) |

## Failing condition (package level)

Rule: TW-APPLY-10 "Intake and preparation-state verification": match the exact original baseline to the preparer's evidence, including its fingerprint representation.

- The package's raw-byte identity matches: Git blob, SHA-256 and byte count are equal.
- Its stated byte shape does not. The redlines file (line 25, "Original baseline" table, row Size) says "640,642 bytes; 6,264 lines; ends with one LF". The proof log (line 31, §3, row "Target (original baseline)") says "one final LF".
- Observed in the original's raw bytes: the file ends with `.\n\n`, a final empty line, so the last two bytes are LF LF. It holds 6,264 LF characters, and line 6,264 is empty.
- Affected source and redlines: none. No redline's literal touches the end of the file, and the metadata plan does not either.

## What else was checked (all passed)

- Package state: `READY` and `COMPLETE_PACKAGE` in the proof log's receipt; the redlines file ends with `END OF REDLINES`.
- Selected scope: the proof log's §4 selection equals the handoff's (2.1 D-4, D-5 and context; 2.2 lines 517–561; 2.8 decisions and drainage table; 2.16 status, R-1 and R-2).
- All eleven operations (nine `REPLACE`, two `INSERT`), parsed independently from the committed package: each locator observed once; no overlap, no insertion at a replaced boundary, no shared gap.
- Derived metadata plan: Version v2.9.7 to v2.9.8; Effective date 2026-10-26 to 2026-11-02; Last Update Gate to `BN 14.0.5`; Status Canon unchanged. It agrees with the §9.7 record in RL-11 (`document_version: "v2.9.8"`, `date: "2026-11-02"`, `v2.9.8 / 2026-11-02`, heading date 2026-11-02).
- Trial application, made in the scratchpad only and not delivered: the reconstructed expected stream equals the output; all 15 untouched intervals and every payload sit at their mapped offsets; EOF is preserved as in the original. With the three header lines reverted, the output's SHA-256 is `07331ff4e0c41b1acb75fafb2718624d9d692a8adfaac38b1da71dc34ffe83f1`, the preparer's recorded simulation.

## Correction needed from the preparer

1. Correct the baseline byte-shape statement in the redlines file (line 25) and the proof log (line 31). The original ends with a final empty line: its last two bytes are LF LF.
2. Issue the corrected package as revision r3, with its revision identity and the correction recorded. Its operations need no change.
3. Repeat producer validation and the save verification, then return the package for fresh validation by TW-APPLY-10.

## Correction invocation (same session, authorized by Nathan's handoff)

TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`). Inputs:

- original `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md` at `e2b7427`;
- package r2 at `2a2325b`, under `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF12/`;
- this diagnostic;
- ledger rows C-04, C-05, C-07, C-10, C-17 and C-18; uncertain C-29; supporting C-06 and C-20;
- the selected source units as above;
- branch `claude/gtwpe-triage-authoring-j94ewf`, and the same output paths.

Afterwards, TW-APPLY-10 100926.1 (page `3f44590a05eb81eebff6e3afa3d9aa5b`) validates the whole corrected package afresh.
