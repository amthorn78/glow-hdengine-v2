# Proof log — PF04-Canon-HDE-Governance v2.8.10 redlines — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: Appendix D.4 encoding-invariance pointer)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-3`. It follows T-01's `drain-1` (commit `3ad779e`, applied in `b489215`) and `drain-2` (commit `9b9d8e6`, applied in `8d4c686`). |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live when this step began (page state 2026-10-09T11:05:22Z; body "Prompt Version: 100926.1") |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-16 (https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR), 2026-11-02. T-01's own session (`session_01Q789tyrM8bruo2RGNCMLM8`) prepared `drain-1` and `drain-2`. No subagent, reviewer or other session took part. |
| Authorization | Nathan, 2026-11-02, in the T-16 session: "I authorize you to apply the correction to the T-01 document (PF04)". The correction is the one the T-16 redlines proof log reports as D-10. "Apply" here means the TW flow on T-01's unpublished document: this package, then TW-APPLY-10. `docs/pfcanon/` stays read-only to this session; publication remains Nathan's manual action. |
| Preparation outcome | `READY` |
| Save outcome | `COMPLETE_PACKAGE` (§9) |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 (open, not merged) |

## 2. Sources, inputs and roles

| Role | Identity | Coverage |
| :---- | :---- | :---- |
| Baseline (target) | T-01's revised PF04 v2.8.10, `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.10.md` at commit `8d4c686`; in-document title `PF04-Canon-HDE-Governance`; git blob `3ef2b20e6006be94e132d7063bd5047751457eca`; SHA-256 `37d58278ce65c2a736a12c391496143315edebdab24600c8418353b921a81438`; 600,876 bytes; 4,859 lines | §3 |
| Current authoritative PF04 | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` on `main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, blob `0c3ce100f9429435bce8e021f36e405120159e4a`, 580,196 bytes. v2.8.9 and v2.8.10 are unpublished. | The full diff from v2.8.8 to v2.8.10 was read (§3) |
| Authority for the correction | Nathan's authorization of 2026-11-02 (§1) | — |
| Change-source file | None beyond the chained revision's source, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (HDE Build Notes v14.0.5, blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`), unchanged on `main` | No PF10 unit is drained by this package |
| Supporting reading | HDE Schemas and Artifacts §8.6.3.3, "Endpoint Catalog and A7 proofs" (`docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md` on `main`, lines 2996–3007), read in full; PF04 v2.8.10 §9.3, §9.3.1 and §9.4 (lines 2589–2848) and Appendix D (lines 4677–4859), read in full | Owner of the A7 proof paths; change-log rules and template; the section being corrected |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a02f3aa4e7b8c37027385e46a3878` | Read in full in this session |
| Origin of the finding | T-16 redlines proof log (`docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF09.6/PF09.6-Canon-HDE-Build-Checklist-Distillation-v1.1.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`), D-10 | Supporting |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-01 | Read |

## 3. Coverage

* Baseline. v2.8.10 is canon v2.8.8 plus T-01's `drain-1` and `drain-2` payloads and header fields. T-01's `drain-1` read v2.8.8 completely (eleven windows, 580,196 bytes). Both T-01 applications proved their composition byte for byte (`drain-1` and `drain-2` application proof logs, preservation audits). Under TW-DRAIN-10's reuse rule, that coverage is reused against this exact, verified baseline.
* Independent check in this session. `diff` of canon v2.8.8 against v2.8.10 gives 23 hunks (35,352 bytes of diff), read in full. Every hunk is a T-01 payload or header field at the locations T-01's packages name: lines 6, 8–9, 584, 914, 978, 1192–1200, 1313, 1394, 2439, 2443, 2452 and 2666 (`drain-1`), and 4004, 4007, 4015 and 4068 (`drain-2`), plus 4206–4208, 4450–4453, 4602–4604 and 4617–4618 (`drain-1`). Appendix D.4, which this package corrects, is byte-identical to v2.8.8.
* Read in full in this session: v2.8.10 §9.3 to §9.4 and Appendix D.
* A complete mechanical scan of v2.8.10 found the corrected literal `encoding_invariance.txt` once (line 4748) and no other A7 encoding-invariance path.
* Not done: a fresh line-by-line reading of all 4,859 lines by this session. The reuse above stands in for it, as the prompt allows.

## 4. Change and disposition ledger

| Item | Disposition | Location |
| :---- | :---- | :---- |
| D-10: Appendix D.4 names `artifacts/proofs/encoding_invariance.txt`, which is not tracked | Actionable: RL-01 replaces the path with `artifacts/proofs/success_encoding_invariance.txt` | Line 4748 |
| PF04 §9.3 change-history rule for RL-01 | Actionable: RL-02 adds the v2.8.11 §9.3.1 entry, `GOV-20261102-gtwpe-pf04-a7path`, NON_EPIC, with every §9.4 field | Gap after line 2774 |
| Other untracked paths in D.4: `tests/transport/headers/aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` and `error_headers_utf8.snap` (found while reading D.4) | Not changed: outside the correction Nathan authorized. Reported for Nathan (§10). | D.4, lines 4753–4755 and 4771 |
| Pre-existing ellipsis path patterns (T-01 `drain-1` observation O-2) | Not changed: T-01 judged them path patterns, not drafting markers; this package keeps that judgment | As `drain-1` records |

## 5. Constraints and interpretations

* Scope is exactly the one correction Nathan authorized, plus the change-log entry PF04's own rules require. Nothing else in PF04 is edited.
* Chaining on v2.8.10 follows T-01's own `drain-2` precedent, so one revised PF carries all three runs and Nathan transfers one file.
* Appendix D.4 is current routing guidance, not a historical record, so the pointer is replaced in place. PF04 §9.4 calls Appendix D "an informative routing aid" that "is refreshed when its pointers are affected".
* Last Update Gate: the package adds no source file, so the gate stays `BN 14.0.5`, the chained revision's source. This follows the T-16 and T-06 precedents for direction-based corrections.
* The §9.3.1 entry follows the v2.8.10 entry's form exactly: one-line summary, a blank line, then the §9.4 fields as `>` lines separated by `>` lines.
* PF03: canonical ownership (the path owner is routed by title), claim-state separation (static inspection only), no ellipsis in payloads.

## 6. Repository inspection

Read-only, at `main` `84d6d1c`:

* `git ls-tree`: `artifacts/proofs/encoding_invariance.txt` is not tracked; `artifacts/proofs/success_encoding_invariance.txt` and its `.path_proof.txt` are tracked.
* `tools/evidence/generate_a7_transport_proofs.py` line 31 lists `artifacts/proofs/success_encoding_invariance.txt` among its proofs.
* `tests/transport/test_a7_transport_proofs.py` lines 141–142, `test_obsolete_encoding_invariance_absent`, assert that `artifacts/proofs/encoding_invariance.txt` does not exist.
* `docs/evidence/INDEX.json` maps `a7.success_encoding_invariance` to `artifacts/proofs/success_encoding_invariance.txt`.
* The D.4 paths in §4's third row are not tracked; the other D.4 artifact and catalog paths are.

These are static checked-in facts. No test was run.

## 7. Producer validation

`validate_t01.py` (scratchpad) parsed the saved redlines file. For every literal it checked the stated byte length and SHA-256, then resolved and simulated the batch against the v2.8.10 bytes read from the working tree, which equal the committed blob:

| Check | Expected | Observed |
| :---- | :---- | :---- |
| Operations | `REPLACE` RL-01, `INSERT` RL-02 | as expected |
| Literal byte lengths and SHA-256 | as stated in the package | all five match |
| RL-01 old block count | 1 | 1, at code point 592,295 (line 4748) |
| RL-02 BEFORE / AFTER / BEFORE+AFTER | 1 / 1 / 1 | 1 / 1 / 1; gap at code point 373,541 (start of line 2775) |
| Overlap | none | none |
| Payload ellipsis | none | none |
| Headings (including `>`-quoted headings) | unchanged | unchanged |
| Change-log ID `GOV-20261102-gtwpe-pf04-a7path` in the baseline | 0 (new and unique) | 0 |
| Simulated result (content only, before header derivation) | — | 603,605 bytes; 4,895 lines; SHA-256 `ad77bac813cd8e64d2a9e9c508a8cabb9a0be56f40061d39fa9385538085e71c` |
| Spacing at the new entry | one blank line before it; two blank lines and `> ---` after it, as before | as expected |

## 8. Header provenance for TW-APPLY-10

* Baseline header (lines 5–10): `PF04-Canon-HDE-Governance`, `v2.8.10`, `Canon`, `2026-11-02`, `BN 14.0.5`, `` `INV-f2ac55d77ce9aacc` ``, in the native `**Field:** value` form.
* Source, in source order: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5, the chained revision's only source. This correction adds no source file.
* RL-02 names v2.8.11 and 2026-11-02.

## 9. Save verification

Save completeness: `COMPLETE_PACKAGE`. Both files were saved in the working tree of `claude/gtwpe-triage-authoring-j94ewf` and read back on 2026-11-02:

* Redlines file: 12,789 bytes, 131 lines, SHA-256 `e366e52e784dfa69710d5a42b4458da2ae1843a06f03df318431c827f878aadc`. It ends with `END OF REDLINES` and one line feed, and the parse in §7 ran on the saved file.
* This proof log: read back in full after this section was written; its own hash is not recorded inside it.
* Before writing, neither name existed in `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/`.

## 10. Unresolved items and next step

* Reported for Nathan, not changed: D.4 also names four untracked header snapshots, `tests/transport/headers/aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` and `error_headers_utf8.snap`. Which tracked files they correspond to is not established here. Changing them needs a further decision.
* Next step: TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) applies this package to the v2.8.10 baseline in this session, under Nathan's authorization. Final output: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.md` and its `.proof-log.md`. Diagnostic path: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`.
