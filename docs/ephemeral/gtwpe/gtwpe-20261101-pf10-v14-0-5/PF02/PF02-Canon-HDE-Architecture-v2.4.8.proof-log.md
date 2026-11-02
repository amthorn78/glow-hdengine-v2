# Proof log: PF02-Canon-HDE-Architecture v2.4.8 (application of gtwpe-20261101-pf10-v14-0-5 T-09 redlines)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/PF02-Canon-HDE-Architecture-v2.4.8.md`: the complete revised PF, version v2.4.8. Git blob `4a009006d553f27c3e86abc66e67bec5040e7ef7`; SHA-256 `a27880ab8934fe6e6e137a7874e99b20f6604643cb9c2c2fc1455540a7cfbe05`; 143,457 bytes; 1,628 LF characters and no final LF |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when this step began (page state 2026-10-09T11:05:22Z) |
| Applier | The T-09 document session Nathan started (Claude Code, https://claude.ai/code/session_01Q789u3YHoFbcNNPspHj1tZ), 2026-11-02. The same session prepared the package under TW-DRAIN-10 as a separate, earlier step. No subagent, reviewer or other session took part. |
| Authorization | Nathan's handoff "GTWPE document session — T-09 — HDE Architecture (drain, then apply)" authorizes this step after a `READY` / `COMPLETE_PACKAGE` preparation |
| Application outcome | Applied: 1 content redline and 3 derived document-control edits; all checks passed |
| Execution date | 2026-11-02 (UTC) |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 |

The revised PF is a working output under `docs/ephemeral/`. It is not publication: `docs/pfcanon/` is unchanged, and the Product Owner transfers canon.

## 2. Inputs

| Role | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF02-Canon-HDE-Architecture-v2.4.7.md`, title `PF02-Canon-HDE-Architecture`, v2.4.7. Read at `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` for this step; git blob `9a23eec67198b86768d3b7fcef2e1b864cb9d998`, equal to the blob the preparer read at `e2b7427ff418ca8f08f05587c4a541308a76da56`. SHA-256 `fc0001e215e5a42bcf91f1e043f0f88a94867e00edae2ab387535869b855a149` (raw bytes, compared with the preparer's raw-byte hash); 142,444 bytes; 1,624 LF characters and no final LF |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/PF02-Canon-HDE-Architecture-v2.4.7.redlines.gtwpe-20261101-pf10-v14-0-5.md`, read from commit `a58b9533` (SHA-256 `bfac02aa737e1811ce93299c2077396c5e6a0f99e11db729aee226869abb745c`, 7,771 bytes) |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF02/PF02-Canon-HDE-Architecture-v2.4.7.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, commit `a58b9533` (SHA-256 `c4d5cf6e4e832a6d7e580943298096e59339e287a2ce0f64c5b157b86ae467ef`) |
| Preparer and run | TW-DRAIN-10 100926.1 in this session; run `gtwpe-20261101-pf10-v14-0-5` / T-09 / preparation revision `r1`; outcome `READY` / `COMPLETE_PACKAGE`; no unresolved item; one held item (H-03), which is not a target |
| Selected incoming source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5, blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; addendum 2.4 (lines 673–753) and addendum 2.5 (lines 754–883). These boundaries match the handoff and the ledger. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-09; rows C-13, C-14 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` on `origin/main` |

Baseline drift check: `git diff --stat e2b7427 origin/main -- docs/pfcanon/` is empty, so the original has not changed since preparation.

## 3. Applied operations and their basis

| ID | Operation | Original location | Old bytes | New bytes | Basis |
| :---- | :---- | :---- | :---- | :---- | :---- |
| META-VERSION | Derived header edit | Line 4, bytes 65–84 | `**Version:** v2.4.7` | `**Version:** v2.4.8` | Patch bump, once, of the native `v<major>.<minor>.<patch>` scheme |
| META-DATE | Derived header edit | Line 7, bytes 106–136 | `**Effective date:** 2026-10-26` | `**Effective date:** 2026-11-02` | Actual application date, native ISO format |
| META-GATE | Derived header edit | Line 9, bytes 138–169 | `**Last Update Gate:** BN 13.8.8` | `**Last Update Gate:** BN 14.0.5` | The one source the package records: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, version v14.0.5, so `BN 14.0.5` |
| RL-01 | `REPLACE`, expected 1, observed 1 | Line 198 in `# 1\. Architectural Principles \[Required-Now\]` > `## 1.1 Single homes`; bytes 18,782–19,847 | 1,065 bytes: the "Non-BodyGraph chart loader classification" paragraph | 2,078 bytes: three paragraphs (the kept `[Required-Now]` classification, a `[Implemented]` current-repository statement at commit `e2b7427`, and a "Static inspection cannot establish" statement) | Ledger rows C-13 and C-14; DELTA-001 in HDE Build Notes addendum 2.4 (l.707, l.723, l.729) and addendum 2.5 (l.853): replace "remains current repository reality until separately remediated" with the delivered boundary. The preparer's rationale: the paragraph described a removed module as current; HDE-EPIC041 delivered and closed the boundary, so the paragraph keeps its normative classification and states the inspected current boundary, verified read-only at `e2b7427` and `84d6d1c` |

Header fields kept unchanged: Title `PF02-Canon-HDE-Architecture`, Status `Canon` (not stale: PF02 is current canon), Invocation tag `INV-f2ac55d77ce9aacc`. PF02 has no other restatement of its own version or date (a whole-document search for `2.4.7`, `2026-10-26` and `13.8.8` found only lines 4, 7 and 9), and no change log or revision-history format, so no history entry was due. The package contained no header redline, so no duplicate authorization arose.

## 4. Validation

All checks ran before any output byte was written, against the original from `origin/main` and the redlines file as committed:

- Package state: `READY` / `COMPLETE_PACKAGE`; `END OF REDLINES` present; one redline, RL-01, with an exact nonempty old block, a complete replacement and an expected count of 1.
- RL-01: old block found once in the whole original, inside §1.1 (lines 190 to 237).
- Each metadata line found once as a whole line.
- Edit plan: four spans in original coordinates (65–84, 106–136, 138–169, 18,747–19,812 characters). No two intersect. Edits were applied in descending offset order without rematching.
- Preservation: the output equals the expected stream rebuilt from the original's untouched intervals and the four payloads. `diff` between original and output shows exactly the four planned hunks (lines 4, 7, 9 and 198 to 198–202). With those lines removed from both, the remaining text is identical. The last 300 bytes are identical, and the file still ends `gate homes.` with no final LF, as the original does.
- Post-application: the phrase "remains current repository reality until separately remediated" is absent; `v2.4.7`, `2026-10-26` and `BN 13.8.8` are absent; each new header value occurs once; no U+2026 and no three consecutive full stops; no `Draft`, `DRAFT`, `TODO` or `TBD`. The two existing mentions of placeholders (lines 181 and 1225) are canon rules and stay.
- Version, date and gate agree with one another and with the one recorded source.
- Save: before writing, `PF02-Canon-HDE-Architecture-v2.4.8.md` did not exist in the output directory. After writing, the saved file is byte-identical (`cmp`) to the verified output; SHA-256 and size as in §1.

These are text checks. They are not product QA.

## 5. Constraints and interpretations

- This step applied the package as prepared. It made no wording change of its own and did no PF03 cleanup.
- Last Update Gate takes the PF10 form `BN <version>`. It records the source used, not a citation of HDE Build Notes.
- The effective date is the application date, not the preparation date. Both are 2026-11-02.

## 6. Limitations and deviations

- None affects the output.
- The same session prepared and applied the package. The handoff authorizes this, and the two steps ran under their own pinned prompts in order.

## 7. Next manual action

Nathan reviews the revised PF and its proof log on draft PR amthorn78/glow-hdengine-v2#826 and, if he accepts them, transfers the file into `docs/pfcanon/` himself. Merging the PR preserves the record and approves nothing; it does not publish canon.
