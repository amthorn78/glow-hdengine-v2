# PF07 application proof log — gtwpe-20261101-pf10-v14-0-5 — T-18

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.5.md`: the complete revised PF07, in-document title `PF07-Canon-Glow-Infrastructure`, v2.3.5, effective 2026-11-02, Last Update Gate `BN 14.0.5`; 100,447 bytes; 1,446 LF characters (1,447 lines; the last line has no final LF, as in the original); SHA-256 `4768a06bef1483e618264c15ad8200db8bfbe978cf80348aaf717c9bf632a65e` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.5.proof-log.md` |
| Applier | TW-APPLY-10 "Apply Validated Redlines", Prompt Version 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b` (page last edited 2026-10-09T11:05:22Z), fetched live from Notion when this step began on 2026-11-02 |
| Session | The Claude Code document session Nathan started for T-18, in which TW-DRAIN-10 prepared the package. Nathan's handoff authorizes Apply here after a `READY` / `COMPLETE_PACKAGE` result. No subagent, reviewer or other session was used. |
| Apply run identity | `gtwpe-20261101-pf10-v14-0-5/T-18/apply-r1` |
| Execution date | 2026-11-02 (UTC; application run at 2026-11-02T00:55Z) |
| Outcome | Applied. Seven operations: four content redlines and three derived document-control fields. |
| Publication | None. `docs/pfcanon/` is unchanged. The revised PF is not authoritative until Nathan transfers it. |

## 2. Inputs

| Input | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.4.md`, v2.3.4, git blob `60fd3f0b3feff007491dc7add29a9c4491cbdf95`, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790` (raw UTF-8 bytes), 99,393 bytes, 1,443 LF characters, no CR. Read from `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` at application time; identical to the preparation baseline `e2b7427ff418ca8f08f05587c4a541308a76da56` (same blob), so there is no drift. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.md`, commit `19a92a9`, 11,600 bytes, SHA-256 `4562cef91fdfb9e202bd1989d46f44fe8244438b58bb7d3d9d10e3839e3078c3` (matches the preparation receipt) |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF07/PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, commit `19a92a9`, SHA-256 `e9d02cc025741b32b9389099f909e341eff736d0c11b5fa7754e336dbb592be1` |
| Preparer and run | TW-DRAIN-10 100926.1, run `gtwpe-20261101-pf10-v14-0-5/T-18/drain-r1`, this session |
| Preparation and save outcome | `READY` / `COMPLETE_PACKAGE` (preparation proof log §11). No blocking change or dependency (§9 there). Target and selected-source coverage complete (§3 there). |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`, unchanged at `84d6d1c` |
| Selected units | 2.1 D-2 l.277–344; 2.1 D-3 l.345–396; 2.1 context l.205–224 and l.491–516; 2.8 l.1048–1145; 2.15 l.1650–1868. These match the handoff and ledger T-18. |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `a3632c0`; task T-18 (§8); rows C-02, C-03, C-17, C-18, C-26 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, v1.8.8, blob `504712df548a02f3aa4e7b8c37027385e46a3878` |

## 3. Applied operations and their basis

| ID | Original location | Operation | Basis (preparer's rationale and ledger row) |
| :---- | :---- | :---- | :---- |
| RL-01 | §2.4 "Key-spelling and downgrade rules", l.352 | REPLACE | C-02, 2.1 D-2 l.281–289 and l.307. D-2 decides that the configured base must end in exactly v1 or v2 and that the configured-base boundary is enforced, with HDE-CLI-API-Vendor-Ref governing route selection and the boundary. "May include the vendor API version path" permitted an unversioned base. The replacement records the value every §2.4 environment holds (`https://api.humandesignapi.nl/v2`) and routes the boundary and selection by title. It states no refusal as delivered, because the implementing change for Candidate CRD Items List item 9 is open (l.506). |
| RL-02 | §2.5 "Production-affecting Live QA infrastructure posture", l.372 | REPLACE | C-26, 2.15 R-1 l.1704–1739, l.1666–1681, R-2 l.1741–1753, R-6 l.1792–1803. R-1 makes the live compat test, with its deployed-service check of the production HD Engine, part of every Epic's Live QA whatever the Epic changed, and supersedes the dependency on a finding that the Epic affects a production surface. The replacement adds that test, routed by title (HDE Build Notes for the test and its waiver, HDE-Governance for execution), names the PF07 facts it relies on, and keeps the existing per-surface requirement with "also" and "for those surfaces" added. |
| RL-03 | §2.8 "Scope.", l.538 | REPLACE | C-17 (decisions 3 and 7), C-18; wording under C-26. 2.8 decision 3 l.1068 makes a CRD's lower-case ID its directory form, and decision 7 l.1082 places CRD and Epic close-run families under the change's QA root (l.1109). PF07 owns canonical QA root paths (§0) and named only the Epic pattern. The replacement adds `audit/qa/<crd-id>/` and keeps every subtree, including `close/`, names-only. "For an Epic's QA, including its Live QA" replaces "used by Live QA" because 2.15 R-3 reserves the name and leaves CRDs undecided (l.1825). The rewritten line has no ellipsis (PF03 §3). |
| RL-04 | §8.1 "EVIDENCE_ROOT", l.1136–1137 | REPLACE | C-17 (decisions 3 and 7), C-18; same basis as RL-03. Adds the CRD pattern and the example `audit/qa/hde-crd-0002`, and reproduces the unchanged EPIC025 example line in the span. |
| META-VERSION | Header, l.4 | Derived | `**Version:** v2.3.4  ` to `**Version:** v2.3.5  `: the final numeric component of the native `v<major>.<minor>.<patch>` version, incremented once |
| META-DATE | Header, l.6 | Derived | `**Effective date:** 2026-10-26  ` to `**Effective date:** 2026-11-02  `: the application execution date, in the native ISO form |
| META-GATE | Header, l.7 | Derived | `**Last Update Gate:** BN 13.8.8  ` to `**Last Update Gate:** BN 14.0.5  `: the one source the package records, `PF10-HDE-Build-Notes-v14.0.5.md`, in `BN <version>` form |

Unchanged header fields: Title `PF07-Canon-Glow-Infrastructure`; Status `Canon` (current, not stale); Invocation tag `INV-f2ac55d77ce9aacc`. The package carries no header redline, so there is no duplicate authorization to reconcile. PF07 has no change log, revision history or Doc-Delta entry section, so no history entry is required and none is carried. There is no internal restatement of the document's own version or date to synchronize: `2.3.4` occurs only at l.4 and in the section number "2.3.4 Canonical bytes & evidence" (l.232), which is not a version; `2026-10-26` only at l.6; `13.8.8` only at l.7.

## 4. Whole-batch validation (before any output byte was written)

The saved redlines file was parsed independently of the preparer's tools. Each block's operation, expected count and the two four-backtick literals were read from the file, and every operation was resolved against the unchanged original.

| ID | Kind | Original character offsets | Expected / observed | OLD / NEW bytes |
| :---- | :---- | :---- | :---- | :---- |
| META-VERSION | metadata | [68, 89) | 1 / 1 | 21 / 21 |
| META-DATE | metadata | [110, 142) | 1 / 1 | 32 / 32 |
| META-GATE | metadata | [143, 176) | 1 / 1 | 33 / 33 |
| RL-01 | content | [24848, 24973) | 1 / 1 | 125 / 276 |
| RL-02 | content | [26311, 27156) | 1 / 1 | 845 / 1,440 |
| RL-03 | content | [39539, 39677) | 1 / 1 | 138 / 305 |
| RL-04 | content | [75300, 75379) | 1 / 1 | 79 / 220 |

- Every operation is `REPLACE` of whole original lines, with a nonempty OLD and a NEW that differs. No `FIND_AND_REPLACE`, `INSERT` or `DELETE`, so the RL-045 preflight has nothing to reject.
- All seven spans are disjoint. No content operation touches the header block (l.1–8, before the first `---`).
- Version, date and gate values agree with one another and with the package's recorded source.

## 5. Application and preservation

- Applied once, in descending offset order, to the decoded original string, without rematching changed text. UTF-8 in and out; LF line endings, no CR, trailing double spaces and the unterminated last line preserved.
- Preservation: the output was rebuilt independently from the eight untouched original intervals and the seven payloads, and the two streams are identical. A walk of the output confirmed each untouched interval at its shifted offset: 97,606 of the original's 98,879 characters, all outside the seven spans, are unchanged.
- Cross-check with preparation: reverting the three header values in the output gives SHA-256 `6d07d8d3713cd603f52b9dc9daf094e408998f2aca8f52bd60a4eef50247952e`, the one-pass result the preparer recorded. The content edits are therefore byte-identical to the validated package.
- `git diff --no-index -U0` from the original to the saved output shows exactly seven hunks: l.4; l.6–7; l.352; l.372, which becomes l.372–374; l.538, now l.540; l.1136, now l.1138; and one added line after the original l.1137 (now l.1140). Nothing else differs.
- Post-application text checks:
  - each NEW occurs exactly once and no OLD survives;
  - `v2.3.4`, `2026-10-26` and `BN 13.8.8` are absent, and `v2.3.5`, `2026-11-02` and `BN 14.0.5` each occur once;
  - code fence runs 6 / 6 and table rows 15 / 15 (original / output);
  - the output still ends `token names.` with no final LF, as the original does.
- Drafting-marker check: the output has the same marker counts as the original. `TBD` 119, `placeholder`/`Placeholder` 3, and `TODO`, `FIXME`, `Draft`, `draft` and `Proposed` 0. Every `TBD` and `OPEN/TBD` is the unconfirmed-fact value that PF07's own rules require (l.65, l.917, l.1084, l.1199, l.1310 and l.1317 of the output), and "Replace TBD as facts are confirmed" (l.149, l.190) is PF07's no-guessing maintenance rule. Neither is a drafting note or an instruction left by a writer. The three "placeholder" uses are normative. No status language about the document and no stale status remain.
- Ellipses: eight ASCII three-period forms and one U+2026 in the original; seven and one in the output, the difference being RL-03's rewritten line. They are not drafting markers. Apply does no PF03 cleanup.

These are text checks of the revised document, not product QA.

## 6. Constraints and limitations

- The revised PF is a working output under `docs/ephemeral/`. Apply does not edit `docs/pfcanon/` and publishes nothing.
- Preparation and application ran in the same session, as the handoff authorizes, with the two prompt roles kept separate: Apply corrected nothing in the package.
- The redlines change wording and routing only. They establish no implementation of 2.1 D-2 or D-3 (Candidate CRD Items List item 9 is open), no Live QA run, no QA verdict, acceptance, Ops, deployment or closure.
- The preparation proof log's observations O-1 to O-9 (pre-existing PF07 drift and later-drain notes, including the Reader v2 route gap that 2.15 R-1's deployed check exposes) are carried unchanged. Apply makes no change for them.

## 7. Next manual action

Nathan reviews the revised PF on draft PR amthorn78/glow-hdengine-v2#826 and, if he accepts it, transfers it into `docs/pfcanon/` himself. Nathan merges. No further prompt runs for T-18.

## 8. Save verification

Recorded after the revised PF was written and read back in full: whole-file SHA-256 and byte count, and the complete diff against the original (§5).

| File | Bytes | SHA-256 | Read back |
| :---- | :---- | :---- | :---- |
| `PF07-Canon-Glow-Infrastructure-v2.3.5.md` | 100,447 | `4768a06bef1483e618264c15ad8200db8bfbe978cf80348aaf717c9bf632a65e` | Complete |
| This proof log | Not self-hashed | Not self-hashed | Complete, after this receipt was added |

Save outcome: `COMPLETE_PACKAGE`.
