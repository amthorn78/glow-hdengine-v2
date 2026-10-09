# PF17 application diagnostic — preparation revision R1

Run: gtwpe-20261009-pf10-v13-5 / T-PF17. Step: TW-APPLY-10 100926.1, first fresh validation on 2026-10-09 UTC.

Original: `docs/pfcanon/PF17-Canon-HDE-Narratives-Guide-v1.5.3.md`, version v1.5.3, main/baseline `e7265a090ad0cc8de5f36de2f19481216aa3d073`, blob `a9e73a8adf03dfccabdad8503d02c4ff4e27e190`, raw UTF-8 SHA-256 `2655c959637c52868a62ab7f7f27e5e04d9c5bca5f8acb3dbcc2b5d1cfd01d1f`, 121,552 bytes.

Rejected package: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/pf17/redlines-PF17-from-v1.5.3.md` and matching `.proof-log.md`, committed and completely read back at `aa5f44037cbfb44c2dd191ff118f32268e636805`. R1 redlines SHA-256 `90c536cb4817b4414eef282a164034f0062a60858fbaec67b1dbda473af6476b`; R1 proof SHA-256 `8a9efea34cf495833400efe5dd21c89e4a559547faebb57305b1911fed4cb16e`.

Actual originating preparer: the same assistant in Nathan's T-PF17 Work document conversation, workspace `/workspace/scratch/64476f52c0c0`; no platform conversation ID is available. Correction returns to that preparer under TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff. Nathan explicitly authorized bounded originating-preparer correction followed by fresh full Apply validation in this session. No other session or reviewer is involved.

Ledger: `docs/ephemeral/gtwpe/gtwpe-20261009-pf10-v13-5/LEDGER.md`, pinned commit `f057d124176143b3e02ba7ad599880fd7e9991b1`, T-PF17 only. Selected sources remain complete A23/A24/A26/A30, S01/S06/S07/S12 and C1 at the supplied baseline. Destination: `docs/20261009-gtwpe-pf10-v13-5`, shared draft PR #596.

## Failure and exact correction required

Violated rule: current PF03 §8 requires the complete authored heading path through the target; TW-APPLY-10 requires an exact complete original-bound location and rejects a missing required field. A fence-aware hierarchy check found that three declarations stopped at the parent H2 even though their old text belongs to a named H3. Literal payloads, offsets and unique old-text counts remain valid; that does not make the incomplete paths valid.

| Redline | Declared parent path | Missing exact child heading | Expected / observed old-block count |
| --- | --- | --- | --- |
| RL-002 | `# 1\) Purpose & Ground Rules` > `## 1.1 Purpose & Non-Goals` | `### Purpose` | 1 / 1 |
| RL-003 | `# 1\) Purpose & Ground Rules` > `## 1.1 Purpose & Non-Goals` | `### Non-Goals` | 1 / 1 |
| RL-004 | `# 1\) Purpose & Ground Rules` > `## 1.3 Terminology & Posture` | `### Text, Suppressed, and pre-composition error` | 1 / 1 |

Required originating-preparer action: append each exact H3 to its corresponding complete heading path, issue the whole nine-redline package as preparation revision R2 at the same authorized filenames, document the correction and original/package lineage, and validate all counts, scopes, full heading paths, payloads and non-overlap again. The content payloads and source selection must not change. Then TW-APPLY-10 independently validates the entire corrected package.

## Failed-attempt posture

Whole R1 batch rejected. Applied edits: **0**. Original unchanged; no final PF or metadata bump produced by this attempt. No subset was applied and no locator was normalized by the applier. This diagnostic does not authorize source, canon, Specification, governed evidence, merge or production writes.

Resolution: awaiting same-session originating-preparer R2 correction and complete revalidation. The final application proof log will record its actual outcome.
