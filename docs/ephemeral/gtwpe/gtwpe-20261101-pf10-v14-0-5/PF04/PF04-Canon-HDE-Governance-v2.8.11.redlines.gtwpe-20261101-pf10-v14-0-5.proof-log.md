# Proof log — PF04-Canon-HDE-Governance v2.8.11 redlines — gtwpe-20261101-pf10-v14-0-5 (T-01 follow-up: Appendix D.4 header-snapshot pointers)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-01/drain-4`. It follows `drain-3` (commit `5be8b1c`, applied in `6c979d6`), which followed T-01's `drain-1` and `drain-2`. |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live when this step began (page state 2026-10-09T11:05:22Z; body "Prompt Version: 100926.1") |
| Originating preparer | The executing document agent in the Claude Code session Nathan started for T-16 (https://claude.ai/code/session_01Q789u2ywt3AZEqAwzRmdCR), 2026-11-02. No subagent, reviewer or other session took part. |
| Authorization | Nathan, 2026-11-02, in the T-16 session, answering the question about the four untracked D.4 header snapshots with "option 1": find the matching tracked snapshots and correct D.4 in a fourth follow-up. `docs/pfcanon/` stays read-only to this session. |
| Preparation outcome | `READY` |
| Save outcome | `COMPLETE_PACKAGE` (§9) |
| Branch and PR | `claude/gtwpe-triage-authoring-j94ewf`, draft PR amthorn78/glow-hdengine-v2#826 (open, not merged) |

## 2. Sources, inputs and roles

| Role | Identity | Coverage |
| :---- | :---- | :---- |
| Baseline (target) | Revised PF04 v2.8.11, `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.11.md` at commit `6c979d6`; git blob `be4f1a09fb6a70a820a69bb75a6085a63f1606f3`; SHA-256 `043110c99a7101df8b8044fa6b980e763e57026b44ca2a73f075d17f378c019f`; 603,605 bytes; 4,895 lines | §3 |
| Current authoritative PF04 | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.8.md` on `main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` (blob `0c3ce100f942`); v2.8.9 to v2.8.11 are unpublished | — |
| Authority for the corrections | Nathan's authorization (§1) | — |
| Change-source file | None beyond the chained revision's source, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (HDE Build Notes v14.0.5, blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`), unchanged on `main` | No PF10 unit is drained |
| Owning canon read (supporting) | HDE Schemas and Artifacts §8.6.3.3, "Aux Narrative (text) — header snapshots" (PF12 v2.9.7 lines 3009–3012); HDE Narratives Guide, "Evidence scope (EPIC-010)" (PF17 v1.5.4 lines 1071–1072); HDE CLI/API Vendor Ref (PF05 v2.5.4 lines 2696–2697). All on `main` `84d6d1c`, each passage read in full. A canon-wide search for the four untracked names found them only in PF04. | The path owner, the Aux evidence-scope owner and the transport owner |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, read in full in this session | — |
| Origin of the findings | `drain-3` proof log §4 and §10, which reported the four untracked D.4 snapshots | Supporting |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, task T-01 | Read |

## 3. Coverage

* Baseline. v2.8.11 is v2.8.10 plus `drain-3`'s two payloads and the version field, which this session authored. The `drain-3` application proved that composition byte for byte (`PF04-Canon-HDE-Governance-v2.8.11.proof-log.md` §6). v2.8.10's own coverage (T-01's complete reading of v2.8.8 plus verified payloads, independently checked by the full v2.8.8-to-v2.8.10 diff) is recorded in the `drain-3` proof log §3. That chain is reused against this exact, verified baseline.
* Read in full in this session: Appendix D of the lineage (during `drain-3`) and the D.4 section of v2.8.11 (lines 4770–4818), plus §9.3.1's last entry and the §9.4 boundary.
* A complete mechanical scan of v2.8.11 found `aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` and `error_headers_utf8.snap` only in D.4 (lines 4789–4791 and 4807).
* Not done: a fresh line-by-line reading of all 4,895 lines by this session. The reuse above stands in for it, as the prompt allows.

## 4. Change and disposition ledger

| Item | Disposition | Location |
| :---- | :---- | :---- |
| `tests/transport/headers/aux_suppression.snap` (untracked) | Actionable, RL-01: replaced by the tracked `tests/transport/headers/aux_suppression_200.snap` | Line 4791 |
| `tests/transport/headers/aux_head.snap` and `aux_304.snap` (untracked, never committed to `main`) | Actionable, RL-01: removed, with no counterpart. HDE Narratives Guide puts Aux HEAD and 304 captures out of scope, and the path owner lists exactly two Aux snapshots. | Lines 4789–4790 |
| `tests/transport/headers/error_headers_utf8.snap` (untracked, never committed to `main`) | Actionable, RL-02: removed. The tracked `no_store_writers_errors.snap`, which D.4 keeps, records the error headers, including the UTF-8 `content-type`. | Line 4807 |
| PF04 §9.3 change-history rule | Actionable, RL-03: v2.8.12 entry `GOV-20261102-gtwpe-pf04-headersnaps` | Gap after line 2810 |
| D.4 "CI jobs (titles-only)": `ci/jobs/transport_etag_200.yml`, `transport_conditional_304.yml`, `transport_head_parity.yml`, `transport_no_store_writers_errors.yml` (lines 4812–4815), and the same `transport_no_store_writers_errors.yml` in Appendix B (line 4624) | Not changed: untracked, but outside Nathan's "option 1", which covered the four snapshots. Reported for Nathan (§10). | As listed |

## 5. Constraints and interpretations

* Scope is the four snapshot pointers Nathan approved, plus the change-log entry PF04's rules require.
* "Find the matching tracked snapshots": one pointer has a tracked match (`aux_suppression_200.snap`). The other three have none, and owning canon explains why: Aux HEAD and 304 are out of scope, and writer and error headers live in `no_store_writers_errors.snap`. Removing those pointers is the correction that makes D.4 match canon and the repository. No replacement path is invented.
* Removal is a pointer refresh in an informative routing appendix (PF04 §9.4). It changes no gate, no obligation and no evidence.
* The chaining, gate and change-log form follow `drain-3` (its proof log §5).
* "Never committed to `main`" rests on GitHub's path-filtered commit list for `main` at `84d6d1c`. Other branches were not searched.

## 6. Repository inspection

Read-only, at `main` `84d6d1c`:

* `git ls-tree tests/transport/headers/`: `aux_suppression_200.snap`, `aux_suppression_200.snap.path_proof.txt`, `aux_text_200.snap`, `aux_text_200.snap.path_proof.txt` and `no_store_writers_errors.snap`. No other file.
* GitHub `list_commits` with `path` on `84d6d1c`: no commit for `tests/transport/headers/aux_head.snap`, `aux_304.snap`, `aux_suppression.snap` or `error_headers_utf8.snap`.
* `docs/evidence/INDEX.json`: `transport.aux.headers.text` maps to `tests/transport/headers/aux_text_200.snap`, and `transport.aux.headers.suppression` to `tests/transport/headers/aux_suppression_200.snap`.
* `tests/transport/headers/no_store_writers_errors.snap` has a `[success]` section (status 200) and an `[error]` section (status 401), each with `cache-control: no-store` and `content-type: application/json; charset=utf-8`. `tests/transport/test_writers_errors_headers.py` line 14 reads it.
* `ci/jobs/transport_etag_200.yml`, `transport_conditional_304.yml`, `transport_head_parity.yml` and `transport_no_store_writers_errors.yml` are not tracked.

These are static checked-in facts. No test was run.

## 7. Producer validation

`validate_t01.py` (scratchpad) parsed the saved redlines file, checked every literal's stated byte length and SHA-256, and simulated the batch against the v2.8.11 bytes, which equal the committed blob:

| Check | Expected | Observed |
| :---- | :---- | :---- |
| Operations | `REPLACE` RL-01, RL-02; `INSERT` RL-03 | as expected |
| Literal byte lengths and SHA-256 | as stated | all seven match |
| RL-01 old block | 1 | 1, at code point 595,202 (line 4789) |
| RL-02 old block | 1 | 1, at code point 595,931 (line 4807) |
| RL-03 BEFORE / AFTER / BEFORE+AFTER | 1 / 1 / 1 | 1 / 1 / 1; gap at code point 376,257 (start of line 2811) |
| Overlap | none | none |
| Payload ellipsis | none | none |
| Headings (including `>`-quoted headings) | unchanged | unchanged |
| ID `GOV-20261102-gtwpe-pf04-headersnaps` in the baseline | 0 | 0 |
| Simulated result (content only, before header derivation) | — | 606,967 bytes; 4,932 lines; SHA-256 `360ba0fa07fe11f52aa92834adcdf7c667d6f457768c920f5b45409be4391031` |
| Simulated D.4 | Aux list names `aux_text_200.snap` and `aux_suppression_200.snap`; writer and error list names `no_store_writers_errors.snap` | as expected |
| Spacing at the new entry | one blank line before; two blank lines and `> ---` after | as expected |

## 8. Header provenance for TW-APPLY-10

* Baseline header (lines 5–10): `PF04-Canon-HDE-Governance`, `v2.8.11`, `Canon`, `2026-11-02`, `BN 14.0.5`, `` `INV-f2ac55d77ce9aacc` ``, in the native `**Field:** value` form, each line ending with two spaces except the invocation tag's.
* Source, in source order: `PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5, the chained revision's only source. This correction adds no source file.
* RL-03 names v2.8.12 and 2026-11-02.

## 9. Save verification

Save completeness: `COMPLETE_PACKAGE`. Both files were saved in the working tree of `claude/gtwpe-triage-authoring-j94ewf` and read back on 2026-11-02:

* Redlines file: 15,911 bytes, 161 lines, SHA-256 `4fecf9e8a7a44f69cb3aeb0a780fe4cb330096a9dabd168246a931a1d38c87e1`. It ends with `END OF REDLINES` and one line feed, and the parse in §7 ran on the saved file.
* This proof log: read back in full after this section was written; its own hash is not recorded inside it.
* Before writing, neither name existed in the PF04 directory.

## 10. Unresolved items and next step

* Reported for Nathan, not changed: D.4's "CI jobs (titles-only)" list names four untracked job files (lines 4812–4815), and Appendix B names `ci/jobs/transport_no_store_writers_errors.yml` (line 4624). CI runs from `.github/workflows/ci.yml`. Which of its steps, if any, these entries should name is not established here.
* Next step: TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`) applies this package to v2.8.11 in this session, under Nathan's authorization. Final output: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-Canon-HDE-Governance-v2.8.12.md` and its `.proof-log.md`. Diagnostic path: `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF04/PF04-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`.
