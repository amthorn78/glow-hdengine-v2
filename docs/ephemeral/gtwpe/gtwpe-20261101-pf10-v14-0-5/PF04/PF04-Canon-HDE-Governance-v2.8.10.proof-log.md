# Proof log — PF04-Canon-HDE-Governance v2.8.10 (application report) — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.md`: the complete revised PF04, in-document title `PF04-Canon-HDE-Governance`, version v2.8.10; 600,876 bytes; 4,859 lines; SHA-256 `37d58278ce65c2a736a12c391496143315edebdab24600c8418353b921a81438` |
| This report | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.proof-log.md` |
| Outcome | Applied: five content operations and one derived document-control edit (the version); none rejected |
| Contents | Every change of v2.8.9 (T-01 `drain-1`) plus the 2.1 D-2 vendor route-selection changes (`drain-2`). It supersedes v2.8.9 as the version for Nathan to publish. |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b` (page last edited 2026-10-09T11:05:22.094Z), fetched live when this step began |
| Applier | The executing document agent in the Claude Code session Nathan started for T-01 (session `session_01Q789tyrM8bruo2RGNCMLM8`), acting under TW-APPLY-10 after the `drain-2` preparation step finished. No subagent, reviewer or other session took part. |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/apply-2` |
| Execution date | 2026-11-02 (UTC; application began 2026-11-02T01:02:28Z) |
| Publication | Not published. `docs/pfcanon/` is unchanged. This revised PF is not authoritative until Nathan publishes it. |

## 2. Inputs and preparation state

| Input | Identity | Check |
| :---- | :---- | :---- |
| Baseline | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.md` (committed at `b489215f82aa156ae49a66284330afb47aa00c21`, unchanged at the branch head); git blob `cc46c5ac0108fc5a3a2eed1e0fdeb4b9518a2e76`; raw-byte SHA-256 `a92dda98a5b2037e90f898033674721a12e21243242131b3fa063ab3e167125c`; 596,102 bytes; v2.8.9 | Read as raw bytes from the committed blob. The preparer hashed the same raw-byte representation. No drift. |
| Authoritative PF04 | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` on `main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` (blob `0c3ce100f942`) | Unchanged since `drain-1`. The baseline v2.8.9 is that file plus `drain-1`'s verified edits. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.redlines.gtwpe-20261101-pf10-v14-0-5.md` at `9b9d8e68dd469e01efe3f3846b44bdf53e216984`; 20,353 bytes; SHA-256 `b5804e9aa3add4973b56f4ccec4da22de985762d74be025ea88d3e6c54658d32`; ends with `END OF REDLINES` | Read completely |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, same commit | Read completely |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; selected unit 2.1 D-2, lines 277–344, with context 205–224 and 491–516 | Unchanged on `main` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`; task T-01; row C-02 (PF04's share), added by Nathan's direction of 2026-11-02 ("yes, proceed with A") | The preparer's selection agrees with that direction |

Verified preparation facts:

* Originating preparer: this session's TW-DRAIN-10 step; run `drain-2`.
* Outcome `READY`; save completeness `COMPLETE_PACKAGE`, recorded after read-back.
* Baseline coverage: `drain-1`'s complete read of v2.8.8, plus its verified payloads; §11.1 re-read.
* Selected unit read in full.
* No unresolved or blocking item.

## 3. Whole-batch validation

Validation ran on the committed package before any output byte was written (`tools/apply2.py`, in the session scratchpad):

* Every literal's stated length and SHA-256 matched.
* Operations are `REPLACE` and `INSERT` only, so the RL-045 rule had nothing to apply to.
* Each old block occurs once in the whole baseline. The INSERT's BEFORE anchor, AFTER anchor and gap each occur once.
* The six baseline-bound spans (five content edits and one metadata edit) are disjoint, and no gap touches a replaced span.
* The required change-history entry (RL-05) opens with `v2.8.10 |` and carries `> PF04 version: v2.8.10` and `> Date / Author: 2026-11-02 /`, which agree with the derived metadata.

## 4. Applied operations and their basis

Each basis is the preparer's rationale and source-ledger reference, restated from the preparation proof log.

| ID | Operation and location | Ledger rows | Basis and rationale |
| :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE` §11.1.1, the item "Base-URL and route-policy governance" (baseline line 4075) | C-02; context C-06 | 2.1 D-2 (lines 277–344): "What governs", "Selection", "No fallback" and "The two canon rules fit together"; supporting HDE CLI/API Vendor Ref §7.1.10. States the single permitted reading of the base's terminal segment (`v2` selects charts, `v1` the retained legacy BodyGraph route, everything else fails closed before credential projection or I/O). Its scope is `bg:resolve --source vendor` and compat chart acquisition. Keeps the ambiguous-configuration rule and the other version-string prohibitions, and routes exact bytes to PF05. |
| RL-02 | `REPLACE` §11.1.1, the paragraph "`bg:resolve --source vendor` route-policy governance" (line 4078) | C-02 | D-2: the v1 path is retained legacy selection, not fallback; the classification label `explicit_legacy_fallback` stays as a wire value; v1 retirement is left to a separately versioned decision. Renames the v1 category accordingly. |
| RL-03 | `REPLACE` §11.1.1, the mapped-cache proof paragraph (line 4086) | C-02 | D-2 "No fallback" and its consequences: the EPIC038 mapped-cache predicate runs on a terminal v1 base. The proof preserves "the retained terminal-v1 legacy selection". |
| RL-04 | `REPLACE` §11.1.6 acceptance item 1 (line 4139) | C-02 | D-2 "The two canon rules fit together". The item accepts the single permitted classification and still rejects any other route or auth inference from an API-version string. |
| RL-05 | `INSERT` §9.3.1, after the v2.8.9 entry (gap between lines 2736 and 2737) | C-02 | PF04 §9.3 and §9.3.1: `NON_EPIC` entry `GOV-20261102-gtwpe-pf04-route` for v2.8.10, dated 2026-11-02 |

## 5. Document-control metadata plan

| Field | Baseline (line) | Revised | Derivation |
| :---- | :---- | :---- | :---- |
| Version | `v2.8.9` (6) | `v2.8.10` | Final numeric component incremented once; prefix and three components kept |
| Effective date | `2026-11-02` (8) | unchanged | Already the actual application execution date |
| Last Update Gate | `BN 14.0.5` (9) | unchanged | The package's only source, `PF10-HDE-Build-Notes-v14.0.5.md`, gives `BN 14.0.5` |
| Status | `Canon` (7) | unchanged | Not stale |
| Title, invocation tag | lines 5 and 10 | unchanged | Not authorized to change |

The label, order and two trailing spaces of the version line are kept. The baseline restates its own version and date nowhere else except as history in §9.3.1, which is unchanged.

## 6. Application and preservation

* The six edits were applied in one pass in descending baseline offsets, with no rematching.
* Preservation audit: every untouched baseline interval is byte-identical at its shifted position, and every payload is exact. Untouched bytes verified: 594,497; bytes consumed by replaced spans: 1,605; together they equal the baseline's 596,102 bytes.
* The last 200 bytes equal the baseline's.
* Cross-check: the output differs from the preparer's simulation (600,875 bytes, SHA-256 `086d09e4622e6877a50215e745d6e7b6bf04c5337f6e0838c1a805ee1ddbafe9`) only on line 6, the version.
* Marker checks:
  * no `Draft` status language;
  * `TODO`, `FIXME` and `[OMITTED`: 0 each;
  * `TBD` (4), `fill later` (1) and `Proposed` (1): the same occurrences as the baseline;
  * the ellipsis count is unchanged at 16, all in original text;
  * no CR byte.
* Baseline: 596,102 bytes, 4,821 lines. Output: 600,876 bytes, 4,859 lines, SHA-256 `37d58278ce65c2a736a12c391496143315edebdab24600c8418353b921a81438`.

These are text checks of the document only. No product test, QA or Ops step ran.

## 7. Constraints, limitations and next action

* Constraints: Apply prepared no edit, repaired no locator and normalized no content. PF canon and the source were read-only.
* Dependency: this revision is chained on the unpublished v2.8.9. Publishing v2.8.10 publishes both runs' changes together. If v2.8.9 were changed before publication, this package would need reconciliation by its preparer.
* Limitations:
  * The revised PF states requirements only. It does not establish that the vendor classifier, the resolver or any QA stage conforms today; Candidate CRD Items List item 9 carries that implementing change.
  * It establishes no QA verdict, acceptance, Ops result, deployment or closure.
  * D-2's targets in other documents remain with T-02, T-05, T-07, T-08, H-05 and H-09.
* Next manual action: Nathan reviews v2.8.10 on draft PR amthorn78/glow-hdengine-v2#826 and, if he accepts it, publishes it to `docs/pfcanon/` in place of v2.8.8 as his own action. Nathan merges.

## 8. Save verification

Both outputs were saved in the working tree of `claude/gtwpe-triage-authoring-j94ewf` and read back completely on 2026-11-02:

* Revised PF: 600,876 bytes, 4,859 lines, SHA-256 `37d58278ce65c2a736a12c391496143315edebdab24600c8418353b921a81438`; valid UTF-8 with no CR byte. A fresh re-application of the committed package to the committed v2.8.9 blob, with the same metadata plan, produced a byte-identical file (`cmp`). The header and the changed §9.3.1, §11.1.1 and §11.1.6 text were read back in place.
* This application report: read back in full after this section was written; its own hash is not recorded inside it.

The commit that holds both outputs is reported in the session's final response and in the ledger's T-01 row.
