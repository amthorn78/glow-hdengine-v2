# PF07 redlines proof log, revision r3 — gtwpe-20261101-pf10-v14-0-5 — T-18

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r3.md` (48 `REPLACE` redlines, RL-01 to RL-48, ending `END OF REDLINES`) |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r3.proof-log.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-18/drain-r3` |
| Supersedes | Package `drain-r2` (`.r2.md` and `.r2.proof-log.md`, commit `286bc56`), which stays in place and in git history. RL-01 to RL-43 are carried byte-identical, blocks included. RL-44 to RL-48 are new. |
| Why a revision | The r2 proof log §7 left five formatting lines for Nathan's decision. After the r2 report, Nathan directed on 2026-11-02, in this session: "yes fix those formatting lines". That direction is the authorization TW-DRAIN-10 requires for hygiene. |
| Preparer | TW-DRAIN-10 "Prepare PF Document Redlines", Prompt Version 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff` (last edited 2026-10-09T11:05:22Z). Fetched live again during this revision, before the redlines file was finalized; it is unchanged from the version used for drain-r1 and drain-r2. |
| Session | The Claude Code document session Nathan started for T-18 on 2026-11-02. No subagent, reviewer or other session was used. |
| Preparation outcome | `READY` |
| Save outcome | Recorded in §7 after read-back |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`; draft PR amthorn78/glow-hdengine-v2#826 (open) |

## 2. Sources and inputs

The inputs are those of drain-r2 (its proof log §2), unchanged:

- target `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.4.md`, blob `60fd3f0b3feff007491dc7add29a9c4491cbdf95`, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790`, unchanged from `e2b7427` to `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`;
- source `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`;
- editorial standard PF03-Reference-Technical-Writing-Best-Practices v1.8.8;
- ledger `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `a3632c0`, task T-18, rows C-02, C-03, C-17, C-18, C-26 and C-01.

RL-44 to RL-48 rest on Nathan's direction quoted in §1 and on PF03 §7 "Revision and retention rules" (formatting repair of indentation and malformed Markdown when the complete source establishes the intended text). They use no new source, so the Last Update Gate source stays `PF10-HDE-Build-Notes-v14.0.5.md` alone.

## 3. New redlines

| ID | Original lines | Defect | Fix |
| :---- | :---- | :---- | :---- |
| RL-44 | 837–839 | `  ---` at the end of §5.1.6, indented under the last list item | Indent removed; the following blank line and `## **5.2 Glow Backend repo**` reproduced unchanged |
| RL-45 | 858–859 | The §5.3 note's blockquote opens with an empty quoted line (`>` and three spaces) | Empty quoted line removed; the `> **Note:**` line reproduced unchanged |
| RL-46 | 1161–1163 | `  ---` in §8.1 after the Deprecated / unused list | Indent removed; the blank line and `**BodyGraph and vendor tuning keys**` reproduced unchanged |
| RL-47 | 1173–1175 | `  ---` in §8.1 after the BodyGraph and vendor tuning keys list | Indent removed; the blank line and `**Notes**` reproduced unchanged |
| RL-48 | 1365–1367 | `  ---` at the end of §9.4, indented under the §9.4 list | Indent removed; the blank line and `# **10\) Service start declarations**` reproduced unchanged |

- Each `  ---` line follows a whitespace-only or empty line (l.836, l.1160, l.1172, l.1364). After the fix, Markdown reads each as a thematic break, never as a setext heading underline.
- The exact line `  ---` occurs four times, so each OLD takes the two lines that follow it to be unique. Those lines are reproduced unchanged.
- None of the five spans touches an r2 span. The nearest are RL-28 and RL-29 around RL-44 and RL-45, RL-04 and RL-33 around RL-46 and RL-47, and RL-39 and RL-40 around RL-48.

## 4. Coverage and dispositions

Unchanged from drain-r2 (its proof log §3 to §6). The r2 proof log §7 items are now handled as follows:

- the five formatting lines: RL-44 to RL-48;
- bold-wrapped headings: left unchanged, because headings are protected text;
- the "HDE-Schemas & Artifacts" title form: left unchanged, because it resolves to PF12's title.

## 5. Producer validation

Validated against the unchanged original before the file was written, and again against the saved file with the independent parser used in drain-r1 and drain-r2.

- RL-01 to RL-43: the carried blocks are byte-identical to the r2 file (SHA-256 `6b9fe687a715b69b7e0ace84f92ac342b2a54041d62918aab9af5cb4bb95443e`, checked by the builder). Their spans and counts are as in the r2 proof log §8.
- RL-44 to RL-48, expected / observed 1 / 1, original character spans:

| ID | Span |
| :---- | :---- |
| RL-44 | [59751, 59786) |
| RL-45 | [60310, 60471) |
| RL-46 | [76870, 76913) |
| RL-47 | [77117, 77133) |
| RL-48 | [94137, 94181) |

- All 48 spans are disjoint. Every OLD is one or more whole original lines and occurs exactly once. No `FIND_AND_REPLACE` is used.
- Every section-path segment matches exactly one complete original line.
- Simulated one-pass application: 101,220 bytes, 1,445 LF characters, SHA-256 `01a97bb6023c0bdcc4f779a52f8ae6de1bb0d830b3da2d75e90d9965d532e8a0`. Compared with r2's result, the content is 13 bytes and one line shorter: four two-space indents and one four-byte empty quote line, with its LF.
- Result checks:
  - lines that are exactly `  ---`: 0;
  - empty quote lines: 0;
  - top-level `---` rules: 24, the original's 20 plus the 4 restored;
  - ellipses 0 / 0, indented headings 0, and the other r2 checks unchanged.
- Correction before READY: the package header first said the prompt was fetched "at the start of this revision". It was fetched during the revision, before the file was finalized, and the wording now says so. No literal changed, and the batch was revalidated with the same spans and digest.

## 6. Outside dependencies

None.

## 7. Save verification

Recorded after both files were written and read back in full, before commit.

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.r3.md` | 56,811 | `2f356457ec8abfbd5f4df4cb2c92a5cb762730be2889e9dfd9d9730e67ce0f3c` | Complete, 1,254 lines. The header and RL-44 to RL-48 were read directly; RL-01 to RL-43 were verified byte-identical to the read r2 file. The file has 48 RL blocks and its last line is `END OF REDLINES`, followed by one LF. |
| This proof log | Not self-hashed | Not self-hashed | Complete, after this receipt was added |

Save outcome: `COMPLETE_PACKAGE`. Preparation outcome: `READY`. Next step: TW-APPLY-10 100926.1 in this session, fetched live, against the unchanged original and this package. Its output again takes the name `PF07-Canon-Glow-Infrastructure-v2.3.5.md` and supersedes the apply-r2 output at `ed56edb`.
