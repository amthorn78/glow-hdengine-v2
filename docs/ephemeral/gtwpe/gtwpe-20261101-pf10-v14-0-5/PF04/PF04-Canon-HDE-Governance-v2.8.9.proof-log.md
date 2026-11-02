# Proof log — PF04-Canon-HDE-Governance v2.8.9 (application report) — gtwpe-20261101-pf10-v14-0-5 (T-01)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact produced | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.md`: the complete revised PF04, in-document title `PF04-Canon-HDE-Governance`, version v2.8.9; 596,102 bytes; 4,821 lines; SHA-256 `a92dda98a5b2037e90f898033674721a12e21243242131b3fa063ab3e167125c` |
| This report | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.9.proof-log.md` |
| Outcome | Applied: fourteen content operations and three derived document-control edits; none rejected |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b` (page last edited 2026-10-09T11:05:22.094Z), fetched live when this step began |
| Applier | The executing document agent in the Claude Code session Nathan started for T-01 (session `session_01Q789tyrM8bruo2RGNCMLM8`), acting under TW-APPLY-10 after the TW-DRAIN-10 step finished. No subagent, reviewer or other session took part. |
| Execution date | 2026-11-02 (UTC; application began 2026-11-02T00:27:58Z) |
| Publication | Not published. `docs/pfcanon/` is unchanged. This revised PF is not authoritative until Nathan publishes it. |

## 2. Inputs and preparation state

| Input | Identity | Check |
| :---- | :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`; git blob `0c3ce100f9429435bce8e021f36e405120159e4a`; raw-byte SHA-256 `7a50dbe3d4eb67a1d01bab89e55d6ed0c0570258b5f7b9c4251626277c76ee72`; 580,196 bytes; 4,748 LF lines; v2.8.8 | Read as raw bytes from the git blob. Current `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` holds the same blob and has no change under `docs/pfcanon/`, so the baseline has not drifted. The preparer hashed the same raw-byte representation. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.8.redlines.gtwpe-20261101-pf10-v14-0-5.md`, read from commit `3ad779e59ef3715f3b914b3e5fdef3dfc6ee5935`; 52,073 bytes; SHA-256 `992b46396e5be5586645135f63e39521fc963f8da633b464d02323bb0cc31958`; ends with `END OF REDLINES` | Read completely |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.8.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, same commit | Read completely |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` | Same blob on current `main` |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` | Read in full in this session |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` (baseline commit `142feb35144d8795f927e0c78b665ace52279064`); task T-01; rows C-03, C-04, C-05, C-07, C-08, C-17, C-18, C-26, C-29; supporting C-06, C-20, C-30; held H-07 | The preparer's selection agrees with the handoff and the ledger row |

Verified preparation facts, from the package and its proof log:

* Originating preparer: the TW-DRAIN-10 step of this same session; run identity `gtwpe-20261101-pf10-v14-0-5/T-01/drain-1`.
* Outcome `READY`; save completeness `COMPLETE_PACKAGE`, recorded after read-back.
* Complete target coverage: eleven windows totalling 580,196 bytes. Complete selected-source coverage: 2.1 D-3 to D-5 with context (205–224, 345–516), 2.2 status, R-1 and R-2 (517–546), 2.8 (1048–1145), 2.15 status and R-1 to R-6 (1650–1804), 2.16 status, R-1 and R-2 (1869–1939).
* No blocking item. H-07 is held with what it waits for (the Product Owner's CCR-1 / P-2 decision), and none of the fourteen redlines touches the acceptance-map wording it protects.

## 3. Whole-batch validation

Validation ran on the committed package before any output byte was written (`tools/apply_package.py`, in the session scratchpad, using raw UTF-8 with no normalization):

* Each literal's stated byte length and SHA-256 matched the fenced literal, read under the package's §2 convention.
* Operations are `REPLACE` and `INSERT` only. No `FIND AND REPLACE` or `FIND_AND_REPLACE`, so the RL-045 rule had nothing to apply to.
* Every `REPLACE` old block occurs once in the whole original. Every `INSERT` BEFORE anchor, AFTER anchor and contiguous gap occurs once.
* The seventeen original-bound spans (fourteen content, three metadata) are disjoint. No insertion gap touches a replaced span or another gap.
* The required change-history entry (RL-10) agrees with the derived metadata: it opens with `v2.8.9 |`, carries `> PF04 version: v2.8.9` and `> Date / Author: 2026-11-02 /`.

## 4. Applied operations and their basis

Each basis below is the preparer's rationale and source-ledger reference for the redline, restated from the preparation proof log.

| ID | Operation and location | Ledger rows | Basis and rationale |
| :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE` §2.0.10, the `LOGS_KEYS_ONLY_OK` item (original line 584) | C-05; context C-06 | HDE Build Notes v14.0.5, 2.1 D-5 (lines 451–490): governed gate check rows are governed logs under `LOGS_KEYS_ONLY_OK` and §7.1, carry closed tokens and repository-relative paths only, and send diagnostics to stderr. The item now names gate check rows and gains a nested item with the row-content rule. |
| RL-02 | `REPLACE` §2.0.19, "Close report minimal content", the item "Tracked-issue items under the generic v2 writer" (line 914) | C-18; supporting C-17, C-20 | 2.8 amendment B-1 (line 1060) and the tracked-issue stated limit (line 1099): a tracked-issue ID is `TI-NNN` or the Epic's own `ISSUE-EPIC<NNN>-TI-<nn>`, and one naming another Epic is refused. PF04's share of the unapportioned amendment (line 1127). |
| RL-03 | `INSERT` §2.0.19, after "Same-run evidence pointer rule" (gap between lines 978 and 979) | C-18 with C-17 decision 7 | 2.8 decision 7 (line 1082), the pointer stated limit (line 1100) and amendment B-2 and B-4 (line 1060): the v2 close report's same-run evidence is the change's post-verdict close-run family; a CRD's close report must, and an Epic's may, name that directory before the close run writes it. Path, admission and publication stay with their owners, named by title. |
| RL-04 | `REPLACE` §3.4, from "Production-functional epic live-proof requirement" through "Other production-affecting scope" (lines 1192–1200) | C-26; supporting C-30 | 2.15 R-1, R-2 and R-5 (lines 1650–1804), relation to other canon (1666–1682), dependencies (1846); 2.16 R-3 (1940–1947). Adds the live compat test every Epic runs, with its deployed-service check on SYN-A and SYN-B; the Product Owner-only waiver; and the blocked-test rule. Aligns the existing production-functional and production-affecting paragraphs with them. R-6's controls stay in force in the execution-controls paragraph. |
| RL-05 | `INSERT` §4.1.4, after the dev/admin `APP_ENV` gating rule (gap between lines 1313 and 1314) | C-03; context C-06 | 2.1 D-3 (lines 345–396): the compat namespace `/api/compat/v1` is a dev/admin surface, with gate order, no credential while gated, the wider-exposure rule and the accepted residual risk. Exact bytes are routed to HDE CLI/API Vendor Ref; §8.3 is unchanged. |
| RL-06 | `INSERT` §4.1.8 "Sanity log artifact", as its last item (gap between lines 1394 and 1395) | C-04; context C-06 | 2.1 D-4 (lines 397–450), sanity-pipeline decision: the `--log-path` bound. |
| RL-07 | `INSERT` §9.1.2, after the persistent-authority paragraph (gap between lines 2439 and 2440) | C-08 | 2.2 R-2 (lines 540–546), active from publication (line 524): PF-Canon is resolved by stable identity, never by version. |
| RL-08 | `INSERT` §9.1.2, after the in-flight documents paragraph (gap between lines 2443 and 2444) | C-07 | 2.2 R-1 (lines 533–539) and its relation to other canon (line 525): planning documents serve planning only. |
| RL-09 | `REPLACE` §9.1.3, the `REPOSITORY_CONTROLLED` row (line 2452) | C-07 | 2.2 R-1: a consistency pointer from the storage rule to §9.1.2 |
| RL-10 | `INSERT` §9.3.1, after the v2.8.8 entry (gap between lines 2665 and 2666) | All rows above | PF04 §9.3 and §9.3.1: every normative change adds a Doc-Delta entry. `NON_EPIC` entry `GOV-20261102-gtwpe-pf04` for v2.8.9, dated 2026-11-02. |
| RL-11 | `REPLACE` §12.2 GATE:CORE-DET evidence items (lines 4206–4208) | C-29; supporting C-30 | 2.16 R-1 and R-2 (lines 1919–1938) and relation to other canon (1883–1890): GATE:CORE-DET evidence is the compat-path owner tests and the live compat test runs; the Reader goldens remain, relabeled; the R-2 entries are retired as history. |
| RL-12 | `REPLACE` Appendix B.2 CI job list (lines 4450–4453) | C-29 | 2.16 R-2 (line 1934): the three CI jobs retired. CI enforcement is the owner tests; open rails is the live test. |
| RL-13 | `REPLACE` Appendix D.1 items (lines 4602–4604) | C-29 | 2.16 R-2 (lines 1932, 1935) and the D.1 sub-entry mapping (lines 1888, 1932–1935): the generator and the composite and integration entries are retired; the owner tests and the live test are listed. |
| RL-14 | `REPLACE` Appendix D.3 items (lines 4617–4618) | C-29 | 2.16 R-2 (lines 1932–1933) and the owner-test preimage-recompute fact (line 1913) |

## 5. Document-control metadata plan

| Field | Original (line) | Revised | Derivation |
| :---- | :---- | :---- | :---- |
| Version | `v2.8.8` (6) | `v2.8.9` | Final numeric component incremented once; prefix and three components kept |
| Effective date | `2026-10-26` (8) | `2026-11-02` | The actual application execution date, in the native `YYYY-MM-DD` form |
| Last Update Gate | `BN 13.8.8` (9) | `BN 14.0.5` | The package's only recorded source: `PF10-HDE-Build-Notes-v14.0.5.md`, giving `BN` and its version |
| Status | `Canon` (7) | unchanged | Not stale: the document is permanent canon |
| Title, invocation tag | lines 5 and 10 | unchanged | Not authorized to change |

* Each header line keeps its label, order and two trailing spaces; the invocation-tag line keeps its lack of them.
* No internal restatement of the document's own version or date exists outside the header, apart from §9.3.1 history entries, which are history and unchanged.
* The required change-history entry is RL-10, and its values agree with this plan.
* No package operation edits the header, so no duplicate header authorization arose.

## 6. Application and preservation

* The seventeen edits were applied in one pass in descending original offsets, with no rematching.
* Preservation audit: walking the original in offset order, every untouched interval between edits appears byte-identical at its shifted position in the output, and every payload appears exactly. Untouched bytes verified: 574,526; bytes consumed by replaced spans: 5,670; together they equal the original's 580,196 bytes.
* The last 200 bytes of the output equal the original's, which ends with a text line, an empty line and a final LF.
* Cross-check: the output differs from the preparer's simulation (596,102 bytes, SHA-256 `844d90aa6e8bb4d605ba3c8abd4d0ec61de3391b5e9a262d1cf30a84dbfb2e11`) only on lines 6, 8 and 9, the three derived header fields.
* Status and marker checks on the revised PF:
  * no `Draft` status language;
  * `TODO`, `FIXME` and `[OMITTED`: 0 each;
  * `TBD` (4), `fill later` (1) and `Proposed` (1): the same normative and quoted-example occurrences as the original;
  * the ellipsis count is unchanged at 16, all in original text that this task does not change (preparation proof log, O-2).
* Original: 580,196 bytes, 4,748 lines. Output: 596,102 bytes, 4,821 lines, SHA-256 `a92dda98a5b2037e90f898033674721a12e21243242131b3fa063ab3e167125c`.

These are text checks of the document only. No product test, QA or Ops step ran.

## 7. Constraints, limitations and next action

* Constraints: Apply prepared no edit, changed no wording, repaired no locator and normalized no content. PF canon and the source were read-only.
* Carried forward from preparation, unchanged here:
  * the outside observations O-1 to O-5, including the §9.8.3 dangling-pointer wording against the close-run pointer rule;
  * the held item H-07;
  * the routing of 2.15 R-3 and R-4 to Change Process Guide, Glow QA Guide and Plan Templates (T-03, T-06, T-07).
* Limitations: the revised PF states requirements only. It does not establish that the compat route, the sanity pipeline, the gate tool or any QA stage conforms today, and it establishes no QA verdict, acceptance, Ops result, deployment or closure.
* Next manual action: Nathan reviews the revised PF on draft PR amthorn78/glow-hdengine-v2#826 and, if he accepts it, publishes it to `docs/pfcanon/` as his own action. Nathan merges.

## 8. Save verification

Both outputs were saved in the working tree of `claude/gtwpe-triage-authoring-j94ewf` and read back completely on 2026-11-02:

* Revised PF: 596,102 bytes, 4,821 lines, SHA-256 `a92dda98a5b2037e90f898033674721a12e21243242131b3fa063ab3e167125c`; valid UTF-8 with no CR byte. A fresh re-application of the saved package to the original git blob, with the same metadata plan, produced a byte-identical file (`cmp`). The changed regions were read back in place, and the header now reads v2.8.9, 2026-11-02 and `BN 14.0.5`.
* This application report: read back in full after this section was written; its own hash is not recorded inside it.

The commit that holds both outputs is reported in the session's final response and in the ledger's T-01 row.
