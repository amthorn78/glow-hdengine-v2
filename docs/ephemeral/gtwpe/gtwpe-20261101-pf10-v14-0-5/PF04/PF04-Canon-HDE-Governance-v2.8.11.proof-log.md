# Proof log — PF04-Canon-HDE-Governance v2.8.11 (application report) — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: Appendix D.4 pointer)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.md`: the complete revised PF, version v2.8.11. 603,605 bytes; 4,895 lines; git blob `be4f1a09fb6a70a820a69bb75a6085a63f1606f3`; SHA-256 `043110c99a7101df8b8044fa6b980e763e57026b44ca2a73f075d17f378c019f` |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when this step began (page state 2026-10-09T11:05:22Z; body "Prompt Version: 100926.1") |
| Applier | The executing document agent in the Claude Code session Nathan started for T-16 (https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR), 2026-11-02. The same session prepared the package under TW-DRAIN-10; preparation and application ran as separate steps, in order. No subagent, reviewer or other session took part. |
| Authorization | Nathan, 2026-11-02, in the T-16 session: "I authorize you to apply the correction to the T-01 document (PF04)" |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/apply-3`, applying `drain-3` |
| Application outcome | Applied. Three operations: two content redlines and one derived header field. |
| Publication | None. `docs/pfcanon/` is unchanged; this file is not authoritative publication. Nathan transfers canon. |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 (open, not merged) |

## 2. Inputs and preparation state

| Role | Identity |
| :---- | :---- |
| Baseline (application original) | T-01's revised PF04 v2.8.10, `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.md`, read from commit `8d4c686`; git blob `3ef2b20e6006be94e132d7063bd5047751457eca`; raw-byte SHA-256 `37d58278ce65c2a736a12c391496143315edebdab24600c8418353b921a81438`, equal to the preparer's recorded value; 600,876 bytes; 4,859 lines. The working-tree file has the same blob after the latest fetch. |
| Current authoritative PF04 | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` on `main` `84d6d1c` (blob `0c3ce100f942`), unchanged. v2.8.9 to v2.8.11 are unpublished. |
| Redlines | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.redlines.gtwpe-20261101-pf10-v14-0-5.md`, read from commit `5be8b1c425454e476f3123519b00568696d99451` |
| Preparation proof log | The same directory, `PF04-Canon-HDE-Governance-v2.8.10.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, at the same commit, read in full |
| Preparer and run | TW-DRAIN-10 100926.1, the T-16 session, run `gtwpe-20261101-pf10-v14-0-5/T-01/drain-3`, chained on T-01's `drain-1` and `drain-2`. Preparation outcome `READY`; save outcome `COMPLETE_PACKAGE`; no blocking item. The four other untracked D.4 paths are reported, not changed. |
| Source | No further source file. The chained revision's source is `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5 (blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`), unchanged on `main` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-01 |
| Editorial standard | PF03 Technical Writing Best Practices v1.8.8, read in full in this session |

## 3. Whole-batch validation

`apply_t01.py` (scratchpad) read the redlines from the committed blob at `5be8b1c` and the baseline from the committed blob at `8d4c686`. It validated every operation and the metadata plan before writing any byte:

| Check | Expected | Observed |
| :---- | :---- | :---- |
| Baseline SHA-256 | `37d58278…a81438` | equal |
| Preparation state | `READY`; `END OF REDLINES` | yes; yes |
| Operations | `REPLACE` RL-01, `INSERT` RL-02; no repeated-replacement operation (RL-045 rule) | as expected |
| Literal byte lengths and SHA-256 | as the package states | all five match |
| RL-01 old block | 1 occurrence | 1 (line 4748) |
| RL-02 BEFORE / AFTER / BEFORE+AFTER | 1 / 1 / 1 | 1 / 1 / 1 (gap at the start of line 2775) |
| Header control labels in the header block (lines 1–11) | each once | each once. Two other `**Status:**` strings, at lines 4426 and 4434, are body list items, not control fields. |
| Conflicts among the three spans and gaps | none | none |

## 4. Applied operations and their basis

| ID | Operation and location | Basis, from the preparer's proof log |
| :---- | :---- | :---- |
| RL-01 | `REPLACE` Appendix D.4, "Catalog/A7 artifacts", last item (line 4748) | Nathan's authorization (T-16 finding D-10). `artifacts/proofs/encoding_invariance.txt` is not tracked at `main` `84d6d1c`, and `tests/transport/test_a7_transport_proofs.py` asserts it stays absent. `artifacts/proofs/success_encoding_invariance.txt` is tracked, is produced by `tools/evidence/generate_a7_transport_proofs.py` and is the Human Evidence Index row `a7.success_encoding_invariance`. HDE Schemas and Artifacts §8.6.3.3 lists it. PF04 §9.4 refreshes Appendix D pointers when they are affected. Only the path changes. |
| RL-02 | `INSERT` §9.3.1, after the v2.8.10 entry (gap after line 2774) | PF04 §9.3 and §9.3.1: every normative change adds a Doc-Delta entry. The new NON_EPIC entry `GOV-20261102-gtwpe-pf04-a7path` carries every §9.4 field and names v2.8.11 and 2026-11-02. |
| META-1 | `REPLACE` header line 6 | `**Version:** v2.8.10` becomes `**Version:** v2.8.11`, keeping its two trailing spaces: the final numeric component of `v<major>.<minor>.<patch>` incremented once. |

## 5. Document-control metadata plan

* Version: v2.8.10 → v2.8.11, matching RL-02's entry (`PF04 version: v2.8.11` and the one-line `v2.8.11 |` summary).
* Effective date: the execution date is 2026-11-02, which equals the baseline value, so no edit is made.
* Last Update Gate: the package records no source file beyond the chained revision's `PF10-HDE-Build-Notes-v14.0.5.md`, so the gate is `BN 14.0.5`, which equals the baseline value. No edit is made.
* Title, status (`Canon`, not stale) and invocation tag are unchanged. No other restatement of the document's own version exists: the `v2.8.10` strings in §9.3.1 belong to the v2.8.10 history entry.
* All version, date, change-history and gate values agree.

## 6. Application and preservation

* Applied in descending offset order on the original-bound plan, without rematching.
* Preservation audit: every untouched baseline interval appears unchanged and in order between the payloads, through EOF. Untouched bytes: 600,771 of 600,876. The three spans consumed 105 bytes: RL-01's 83-byte old block and 22 bytes of the version line; RL-02 consumed none.
* Every payload is exactly at its position. Headings, including `>`-quoted headings, are unchanged.
* The output differs from the preparer's simulation only in the version line, as the metadata plan predicts.
* Hygiene: the output adds no `Draft` language, placeholder, TODO or drafting note. The old path now occurs only inside the new change-log record, which describes the correction as history.
* Output: 603,605 bytes; 4,895 lines; SHA-256 `043110c99a7101df8b8044fa6b980e763e57026b44ca2a73f075d17f378c019f`.

## 7. Constraints, limitations and next action

* Apply prepared nothing and changed no payload.
* Not changed, reported by the preparer: D.4 also lists `tests/transport/headers/aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` and `error_headers_utf8.snap`, which are not tracked. A further decision is needed to correct them.
* Not run: product tests, QA and CI.
* Next manual action: Nathan reviews v2.8.11. If it is accepted, Nathan transfers it into `docs/pfcanon/` by hand and merges draft PR amthorn78/glow-hdengine-v2#826. v2.8.11 supersedes T-01's v2.8.9 and v2.8.10 as the document to publish.

## 8. Save verification

* Before writing, `PF04-Canon-HDE-Governance-v2.8.11.md`, its proof log and `PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md` did not exist in the directory.
* Revised PF: written, then compared byte for byte (`cmp`) with the audited output stream: identical; same SHA-256 and blob as §1. Every changed region was read back through a full `diff` against the baseline: the version line, the 36 inserted change-log lines and the D.4 line.
* This proof log: read back in full after this section was written; its own hash is not recorded inside it.
