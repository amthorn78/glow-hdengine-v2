# Proof log — PF04-Canon-HDE-Governance v2.8.12 (application report) — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: Appendix D.4 header-snapshot pointers)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.12.md`: the complete revised PF, version v2.8.12. 606,967 bytes; 4,932 lines; git blob `cba9a0cb2e05f400783e39371974b3c581cbe28f`; SHA-256 `af262a2f058f0039af3108324a1f548bef89a618f2e90171bdc48751392c94cb` |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when this step began (page state 2026-10-09T11:05:22Z; body "Prompt Version: 100926.1") |
| Applier | The executing document agent in the Claude Code session Nathan started for T-16 (https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR), 2026-11-02. The same session prepared the package under TW-DRAIN-10; preparation and application ran as separate steps, in order. No subagent, reviewer or other session took part. |
| Authorization | Nathan, 2026-11-02, in the T-16 session, answering the question about the four untracked D.4 header snapshots with "option 1": find the matching tracked snapshots and correct D.4 in a fourth follow-up, giving v2.8.12 |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/apply-4`, applying `drain-4` |
| Application outcome | Applied. Four operations: three content redlines and one derived header field. |
| Publication | None. `docs/pfcanon/` is unchanged; this file is not authoritative publication. Nathan transfers canon. |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 (open, not merged; head `66c4311` when this step began) |

## 2. Inputs and preparation state

| Role | Identity |
| :---- | :---- |
| Baseline (application original) | Revised PF04 v2.8.11, `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.md`, read from commit `6c979d6`; git blob `be4f1a09fb6a70a820a69bb75a6085a63f1606f3`; raw-byte SHA-256 `043110c99a7101df8b8044fa6b980e763e57026b44ca2a73f075d17f378c019f`, equal to the preparer's recorded value; 603,605 bytes; 4,895 lines. The working-tree file has the same blob after the latest fetch. |
| Current authoritative PF04 | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` on `main` `84d6d1c` (blob `0c3ce100f942`), unchanged. v2.8.9 to v2.8.12 are unpublished. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.redlines.gtwpe-20261101-pf10-v14-0-5.md`, read from commit `66c43110a1b964ffc5dd48cb74b4a0edad07659d`; 15,911 bytes; SHA-256 `4fecf9e8a7a44f69cb3aeb0a780fe4cb330096a9dabd168246a931a1d38c87e1`, equal to the preparer's recorded value |
| Preparation proof log | The same directory, `PF04-Canon-HDE-Governance-v2.8.11.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, at the same commit, read in full |
| Preparer and run | TW-DRAIN-10 100926.1, the T-16 session, run `gtwpe-20261101-pf10-v14-0-5/T-01/drain-4`, chained on T-01's `drain-1` and `drain-2` and this session's `drain-3`. Preparation outcome `READY`; save outcome `COMPLETE_PACKAGE`; no blocking item. The D.4 CI-job pointers are reported, not changed. |
| Source | No further source file. The chained revision's source is `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5 (blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`), unchanged on `main` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-01 |
| Editorial standard | PF03 Technical Writing Best Practices v1.8.8, read in full in this session |

## 3. Whole-batch validation

`apply4.py` (scratchpad, adapted from the `apply-3` script for this baseline) read the redlines from the committed blob at `66c4311` and the baseline from the committed blob at `6c979d6`. It validated every operation and the metadata plan before writing any byte:

| Check | Expected | Observed |
| :---- | :---- | :---- |
| Baseline SHA-256 | `043110c9…c019f` | equal |
| Preparation state | `READY`; `END OF REDLINES` | yes; yes |
| Operations | `REPLACE` RL-01 and RL-02, `INSERT` RL-03; no repeated-replacement operation (RL-045 rule) | as expected |
| Literal byte lengths and SHA-256 | as the package states | all seven match |
| RL-01 old block | 1 occurrence | 1 (lines 4789–4791) |
| RL-02 old block | 1 occurrence | 1 (lines 4807–4808) |
| RL-03 BEFORE / AFTER / BEFORE+AFTER | 1 / 1 / 1 | 1 / 1 / 1 (gap at the start of line 2811) |
| Header control labels in the header block (lines 1–11) | each once | each once. Two other `**Status:**` strings, at lines 4426 and 4434, are body list items, not control fields. |
| Conflicts among the four spans and gaps | none | none |

## 4. Applied operations and their basis

| ID | Operation and location | Basis, from the preparer's proof log |
| :---- | :---- | :---- |
| RL-01 | `REPLACE` Appendix D.4, "Aux Narrative (text) snapshots (headers-only)", the last three items (lines 4789–4791) | Nathan's "option 1". `tests/transport/headers/aux_suppression.snap` becomes the tracked `tests/transport/headers/aux_suppression_200.snap`, the Human Evidence Index row `transport.aux.headers.suppression`. `aux_head.snap` and `aux_304.snap` are removed: neither has a commit in the history of `main`, HDE Narratives Guide ("Evidence scope (EPIC-010)") puts Aux HEAD and 304 captures out of scope, and HDE Schemas and Artifacts §8.6.3.3 lists exactly two Aux header snapshots. `aux_text_200.snap`, already in D.4, is kept. |
| RL-02 | `REPLACE` Appendix D.4, "Writer/error posture (headers-only)" (lines 4807–4808) | Nathan's "option 1". `tests/transport/headers/error_headers_utf8.snap` is removed: it has no commit in the history of `main`. The tracked `tests/transport/headers/no_store_writers_errors.snap`, which stays, records the error headers, including the UTF-8 `content-type`. |
| RL-03 | `INSERT` §9.3.1, after the v2.8.11 entry (gap after line 2810) | PF04 §9.3 and §9.3.1: every normative change adds a Doc-Delta entry. The new NON_EPIC entry `GOV-20261102-gtwpe-pf04-headersnaps` carries every §9.4 field and names v2.8.12 and 2026-11-02. |
| META-1 | `REPLACE` header line 6 | `**Version:** v2.8.11` becomes `**Version:** v2.8.12`, keeping its two trailing spaces: the final numeric component of `v<major>.<minor>.<patch>` incremented once. |

## 5. Document-control metadata plan

* Version: v2.8.11 → v2.8.12, matching RL-03's entry (`PF04 version: v2.8.12` and the one-line `v2.8.12 |` summary).
* Effective date: the execution date is 2026-11-02, which equals the baseline value, so no edit is made.
* Last Update Gate: the package records no source file beyond the chained revision's `PF10-HDE-Build-Notes-v14.0.5.md`, so the gate is `BN 14.0.5`, which equals the baseline value. No edit is made.
* Title, status (`Canon`, not stale) and invocation tag are unchanged. No other restatement of the document's own version exists: the `v2.8.11` strings in §9.3.1 belong to the v2.8.11 history entry.
* All version, date, change-history and gate values agree.

## 6. Application and preservation

* Applied in descending offset order on the original-bound plan, without rematching.
* Preservation audit: every untouched baseline interval appears unchanged and in order between the payloads, through EOF. Untouched bytes: 603,338 of 603,605. The four spans consumed 267 bytes: RL-01's 135-byte old block, RL-02's 110-byte old block and 22 bytes of the version line; RL-03 consumed none.
* Every payload is exactly at its position. Headings, including `>`-quoted headings, are unchanged.
* The output differs from the preparer's simulation (SHA-256 `360ba0fa…391031`) only in the version line, as the metadata plan predicts.
* Hygiene: the output adds no placeholder, TODO or drafting note. `Draft` occurs once more than in the baseline, as the §9.4 field label `Draft / binding surface:` in the new entry, the same label every other entry carries. The removed paths now occur only inside the new change-log record, which describes the correction as history.
* Resulting D.4: the Aux list names `tests/transport/headers/aux_text_200.snap` and `tests/transport/headers/aux_suppression_200.snap` (output lines 4828–4829); the writer and error list names `tests/transport/headers/no_store_writers_errors.snap` (line 4845).
* Output: 606,967 bytes; 4,932 lines; SHA-256 `af262a2f058f0039af3108324a1f548bef89a618f2e90171bdc48751392c94cb`.

## 7. Constraints, limitations and next action

* Apply prepared nothing and changed no payload.
* Correction to the preparer's report. The `drain-4` proof log (§4 and §10) says Appendix B names one untracked CI job, `ci/jobs/transport_no_store_writers_errors.yml`, at line 4624. That understates it. Appendix B.4 names all four transport jobs, at v2.8.11 lines 4621–4624, the same four D.4 names at lines 4812–4815. The `drain-4` proof log is left as committed; this entry records the correction.
* Not changed, and wider than D.4. v2.8.11 names 25 distinct `ci/jobs/*.yml` files on 31 lines. At `main` `84d6d1c` only three are tracked: `logs_keys_only_redaction.yml`, `rails_closed_refusal.yml` and `rails_open_conformance.yml`. Across `docs/pfcanon/` on `main`, 25 distinct `ci/jobs/*.yml` names occur in PF04, PF09.5, PF09.6, PF12, PF14, PF16 and PF20, and 22 of them are untracked. Ordinary CI runs as the one `test` job in `.github/workflows/ci.yml`. Whether these "titles-only" entries are meant as repository paths, and what they should name, is a canon decision across several documents, not a pointer refresh in T-01. Nothing here decides it.
* Not run: product tests, QA and CI.
* Next manual action: Nathan reviews v2.8.12. If it is accepted, Nathan transfers it into `docs/pfcanon/` by hand and merges draft PR amthorn78/glow-hdengine-v2#826. v2.8.12 supersedes T-01's v2.8.9 and v2.8.10 and this session's v2.8.11 as the document to publish.

## 8. Save verification

* Before writing, `PF04-Canon-HDE-Governance-v2.8.12.md`, its proof log and `PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` did not exist in the directory or on the remote branch.
* Revised PF: written, then compared byte for byte (`cmp`) with the audited output stream: identical; same SHA-256 and blob as §1. Every changed region was read back through a full `diff` against the baseline (42 lines added, 5 removed): the version line, the 40 inserted change-log lines, the D.4 Aux list and the D.4 writer and error list.
* This proof log: read back in full after this section was written; its own hash is not recorded inside it.
