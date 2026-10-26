# Proof log — redlines-PF09.3-from-v1.1.7.md

This is the processing report of TW-DRAIN-20 — Prepare PF09 Redlines — 100926.1 for ledger task T-PF09.3. It documents how the redlines file beside it was made and what was checked. It is not the revised PF and makes no QA, acceptance, canon-adoption or closure claim.

## 1. Artifact and run identity

| Field | Value |
| :- | :- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf09-3/redlines-PF09.3-from-v1.1.7.md` |
| Artifact bytes and SHA-256 | 22,483 bytes; `8462e62add2061aec30e3eaa76dfdf032a3a9537746040b6a15f171dfbbb9e29`; 7 redlines (RL001 to RL007), ending `END OF REDLINES` |
| Run identity | `GTWPE-20261026-PF10-v13.8.8-T-PF09.3` (the same in both files) |
| Prompt | TW-DRAIN-20 — Prepare PF09 Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862, fetched live on 2026-10-26 (page state 2026-10-09T11:05:22Z) |
| Originating preparer | The Nathan-started T-PF09.3 document session, a Claude Code cloud session: https://claude.ai/code/session_01YSdc7bi4Jf3eEwEQmcbqCc. One session, no subagents, no reviewers, as the handoff directs and the prompt requires |
| Authorized sequence | The handoff authorizes TW-DRAIN-20 then TW-APPLY-10 in this session |
| Preparation date | 2026-10-26 |
| Preparation outcome | `READY` |
| Save completeness | Recorded in §13, after complete readback |

## 2. Target and original

| Field | Value |
| :- | :- |
| Target | PF09.3-Canon-HDE-Build-Checklist-Separation, v1.1.7, Status Canon, phase Separation (Phase III) |
| Path | `docs/pfcanon/PF09.3-Canon-HDE-Build-Checklist-Separation-v1.1.7.md` |
| Read at | `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a` (the ledger baseline) and re-checked at `0838ba08254eaefc888019df49a06aa2ae99cc6c` (current `main`, which adds only the ledger) |
| Git blob | `1e8fb350a7ab46cec1c4894798db1f1b1f0a1d94` at both commits |
| Bytes | 86,650 bytes; 1,378 LF line ends; UTF-8; no BOM; no CR; no fenced code |
| SHA-256 of the raw bytes | `3f1f7c429c8de9df5c87ea680adf899e5206affc058ced47664a42f328667266` |
| Newer version on `main` | None. `docs/pfcanon/` on `main` holds only v1.1.7 of PF09.3 |
| Reading | Complete: lines 1 to 1378, every task and subtask (HDE-SEPA001 to HDE-SEPA006), the phase block and the front matter §0.1 to §0.6 |

## 3. Sources and their roles

### Change-bearing sources (selected by the handoff and ledger task T-PF09.3)

| Source | Identity | Selected units, read in full |
| :- | :- | :- |
| HDE Build Notes | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, v13.8.8, effective 2026.10.26, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, 729,539 bytes, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`; the sole unlettered logical version on `main` | Front matter lines 1 to 223 (precedence §1 to §9, cross-references, template, Addendum Index); addendum 2.2 lines 258 to 337 (A02); addendum 2.35 lines 3725 to 3955 (A35) |
| HDE-CRD-0002 Specification v1.1 (approved) | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa3`, 43,151 bytes, SHA-256 `fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df` | CR-3, lines 221 to 230 (S-CR3) |
| HDE-CRD-0002 Specification delta 01 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091b`, 21,046 bytes, SHA-256 `59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636` | The overlay of the base; its change table C-1 to C-14 (lines 46 to 67) read, C-6 (line 59) used for S01 |

PF10's supersession notes from the handoff were checked for this scope: 2.18, 2.14 and 2.17 narrow or amend 2.11 to 2.16, none of which is selected here, and 2.35 states that it supersedes nothing. A02 and A35 are applied as published.

### Closure and approval evidence (read to establish that nothing is held, and cited as evidence)

| Ref | Record | Blob | What was read |
| :- | :- | :- | :- |
| X10 | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md` | `c48f77a0c220` | Decision lines: INITIAL_APPROVE by Thoth, 2026-10-12T19:39:51Z |
| SR4 | `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md` | `5a6cecc86f60` | Decision lines: DELTA_APPROVE by Thoth, 2026-10-21T18:36:00Z |
| X11 | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` | `2260eae17974` | Front matter, §0 decision table, §1: CLOSE, CHANGE_CLOSED, by Isis, decision time 2026-10-26T16:40:00Z; "Not established: Board state, PF09 or PF30 movement" |
| X12 | `docs/ephemeral/HDE-CRD-0002-CL-20-post-closure-record-v1.0.md` | `ac60f368f6d9` | Searched for PF09 and the chart-loader defect: it carries the defect to CL-40 (HDE-SEPA006) and claims no PF09 movement |
| X13 | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md` | `d6cceaf3a019` | Front matter and verdict table: verdict PASS; 21 checks, all PASS |
| X14 | `audit/HDE-CRD-0002_close_report.md` | `0bbc8050d3c1` | "Exact-source acceptance" (S01 to S22 with limitations) and "Deferrals" (34 entries, including `HDE-SEPA006`) |

HDE-CRD-0002 is closed (X11 after X13), so none of its changes is held on closure grounds (ledger, "Precedence and closure controls").

### Supporting reading (not change sources)

- PF03-Reference-Technical-Writing-Best-Practices v1.8.8 (`docs/pfcanon/`, blob `504712df548a`), read in full as the editorial standard.
- `AGENTS.md` (blob `7e358b4601d3`): canon-first, canon read-only and write-boundary rules.
- Specification v1.1 lines 60 to 238 (intake, requirements S01 to S22, exclusions, constraints, CR-1 to CR-3), to map each limitation in the HDE-SEPA005 note to its requirement.
- Repository files on `main` at `0838ba08`, read-only (§8).
- The 2026-10-09 run's PF09.3 redlines file, for the native redline layout only. Its content is an older run on an older base and was not reused.

The ledger, `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0ebb2f80a416fb004b9a913da592d1`, identical on `main`), routes the work. It is not a change source. Its "Precedence and closure controls" and "Held and deferred items" sections were read before work started.

## 4. Assigned scope and coverage

Ledger task T-PF09.3; assigned rows, as the handoff and ledger agree:

- **S-CR3:** Specification CR-3, the HDE-SEPA005 note at original line 1170.
- **A35 R-2:** original lines 1167 and 1170; delivered and removed items no longer "remain baseline".
- **A35 R-1 with A02 RP-2:** HDE-SEPA006 evidence, the legacy chart-loader defect and the retired test.

Coverage is complete: the whole target, every selected unit, and the PF10 front matter. No selected unit was read partially.

## 5. Change and disposition ledger

| Source item | Change it carries | Disposition in this target |
| :- | :- | :- |
| S-CR3 (CR-3) | Reword the HDE-SEPA005 note so that it names the Specification, not "that CRD's PF30 record, once entered" | Actionable: RL003 |
| A35 R-2, line 1167 | "`--allow-prod-vendor` gap remains with the PF05 and CLI owners": stale, because S14 delivered it | Actionable: RL002 |
| A35 R-2, line 1170 | "Remain baseline" for HTML 404 (S02), the CLI proof test and out-of-lane failures (S03), engine-core currency and Mirror labels (S11, S12) and the code security review (S19): stale, delivered. Wheel installs (S01) removed by Product Owner decision. No PF30 record (CR-1) | Actionable: RL003 |
| A35 R-2, PF09.4 lines 1112 and 2139 | HDE-CONJ005 and HDE-CONJ010.4 notes | Out of this target: T-PF09.4 |
| A35 R-1 | HDE-SEPA006 owns the legacy chart-loader defect; HDE-SEPA006.2's caller migration covers the retired test; no repair approved; not targeted for closure | Actionable: RL001, RL004, RL005, RL006, RL007. Status judgment in §6 |
| A02 RP-2 | The test retired under S03 with a recorded reason; defect facts (`_call_legacy`, `FixturesProvider`, since `6c6f4b2a`, 2025-09-28); only tests call the legacy signature; not a release member; not reached at runtime; routed to the Product Owner as decision owner for HDE-SEPA006; not fixed in HDE-CRD-0002; replacing coverage; `loader_call.jsonl` not edited | Actionable: RL004, RL006, RL007; phase statement RL001; Epic information RL005 |
| A02 RP-1, bindings, affected surfaces | Contract-inventory tools, classifier owners, test fixture changes | No relevant change in PF09.3: CI and test-tooling work of HDE-CRD-0002, not phased Separation work |
| A02 "Documentation" (OBS-12, ruby) | A documentation delta candidate | Out of this target: repository documentation (ledger A34, N) |
| A02 "Retiring the contract-inventory test with both tools as historical was not decided" | A separate Product Owner decision | No PF09.3 change; nothing to record here |
| A35 "No PF09 gap" | No new PF09 row | No new row (duty 4) |
| A35 R-3, R-4 | HDE-COAG001.9, HDE-COAG001.4 | Out of this target: T-PF09.7 |
| A35 R-5 | HDE-COAG003.8 and .9 unchanged | Already represented: original line 1167 keeps the re-homing; HDE-CRD-0002 did not reopen them (Specification Exclusions, "Not reopened") |
| A35 items 9, 10, 11 and their dispositions | Candidate CRD list and documentation deltas | Out of PF09 scope (PF09.3 §0.2 excludes documentation-only and process-only work); not recorded here. Item 9 is reflected only as "the findings it routed to the Product Owner awaiting disposition" in RL003, because the original note named the missing review |
| PF10 front matter | Application rules (§1 to §9; titles-only cross-references) | Applied: PF09.3 text cites HDE Build Notes by title only |

No held item (H-01 to H-06) was touched. §10 records one observation that sits next to H-01 and was deliberately left unchanged.

## 6. The six PF09 duties and the row judgments

| Duty | Disposition | Locations |
| :- | :- | :- |
| 1. Subtasks | HDE-SEPA005.1 to .5: no relevant change; they stay **Done**, because the CRD's changes concern the parent's notes. HDE-SEPA006.1 and .3: no relevant change; they stay **Not done**. HDE-SEPA006.2: evidence note added (RL007); it stays **Not done** | Original lines 1179 to 1277; 1318 to 1373 |
| 2. Tasks | HDE-SEPA005 stays **Done**: its notes change (RL002, RL003), but nothing changes its completion basis. HDE-SEPA006 stays **Not done**: R-1 asks no closure, no implementation exists, and PF09.3 §0.6 is unmet. Owner field (RL004), Epic field (RL005) and notes (RL006) change. HDE-SEPA001 to HDE-SEPA004: not affected | Original lines 1148 to 1177; 1280 to 1316 |
| 3. Phase statuses | Phase master status stays **Not Done** (native spelling kept). Phase notes updated (RL001): HDE-SEPA006 owns the defect, and neither closed CRD discharges the open obligations | Original lines 166 to 173 |
| 4. New rows | No relevant change. A35 finds no PF09 gap, and R-1 maps to the existing HDE-SEPA006. No identifier allocated | — |
| 5. Evidence | Changed: S14 delivery and close-report scope (RL002); HDE-CRD-0002 closure, QA verdict and delivered requirements, and the S01 limit (RL003); defect evidence, retirement record, replacing coverage and close-report deferral (RL006); the retirement as HDE-SEPA006.2 evidence (RL007) | As listed |
| 6. Epic information | Changed: HDE-SEPA006 stays unselected and is not part of HDE-CRD-0002's scope (RL005); the Product Owner is decision owner (RL004); HDE-SEPA005's carried limitations are recorded against HDE-CRD-0002's governing Specification (RL003). HDE-SEPA005's Epic field (HDE-EPIC040) is unchanged | Original lines 1159, 1170, 1293, 1297 |

## 7. Interpretations and inferred details

- **RL001.** "It also owns the legacy chart-loader defect" follows A35 ("the legacy chart-loader defect (PF09 HDE-SEPA006 owns it)"). Naming HDE-CRD-0002 beside HDE-CRD-0001 in the phase statement follows from X11 (closed) and A02 RP-2 (not fixed in HDE-CRD-0002), applied under PF09.3 §0.4 ("Neither a CRD's progress or closure nor a historical PF20/PF30 entry silently creates, transfers, closes, or updates PF09 work").
- **RL003.** The S03 wording tracks the S03 acceptance intent ("recorded failures and collection errors are fixed or retired with their files"), because the sources do not say whether the CLI proof test was fixed or retired. "Findings F01 to F09 fixed" and "the findings it routed to the Product Owner awaiting disposition" come from X14 (S19 limitation; deferrals FND-029 and X-01 to X-04). The governing record is "the Specification, as overlaid by delta 01", as the ledger's precedence control states. No PF30 wording is kept. A historical PF30.1 record may be made later by T-PF30.1, so the note does not claim that none exists.
- **RL005.** "Not an addition to the closed HDE-CRD-0001 or HDE-CRD-0002 scope" is inferred from the Specification Exclusions ("No PF09 mapping of this work") and A02 RP-2 (not fixed in, and not deferred to a unit of, HDE-CRD-0002).
- **RL006.** The first bullet's past tense is inferred from a bounded search of PF10 v13.8.8 for "September 7", "090726", "2026-09-07" and "SEPA006": the only HDE-SEPA006 and chart-loader matches are in the Addendum Index, 2.2, 2.30, 2.33 and 2.35, all about the HDE-CRD-0002 defect, so the current HDE Build Notes holds no September 7, 2026 gap-scan record. Older PF10 versions were not read (PF10 front matter §6). The defect facts are attributed to HDE Build Notes in the text, except those checked directly (§8).
- **RL007.** "A test caller of the legacy loader signature" follows A02 RP-2 (the file "exposes a product defect in the legacy signature"). The note states evidence and its limit; it adds no requirement.
- **Gate sources.** X10 to X14 and `tests/retired_tests.md` are cited inside payloads as evidence locators. The change sources are the three selected sources. Apply's Last Update Gate therefore uses only those three, as the redlines file records.

## 8. Repository claims checked read-only on `main` at `0838ba08`

| Claim used | Check | Result |
| :- | :- | :- |
| The retired test's row and reason exist | `tests/retired_tests.md` (blob `ea44b4626216`) line 57 | Present: reason, date 2026-10-13, the two replacing tests |
| The retired test is gone | `git ls-tree origin/main tests/loader/` | Absent; five other loader test files remain |
| `_call_legacy` calls `get_chart` | `engine/charts/loader.py` (blob `8ea4dce2602d`) lines 76 to 82 | Line 81: `res = provider.get_chart(user_id, correlation_id=correlation_id)` |
| `FixturesProvider` has no `get_chart` | `engine/provider/fixtures.py` (blob `642f86967a8b`) | Defines `__init__` and `get_pair_profile` only; the resolver's default provider is `fixtures` (`engine/config/provider_loader.py`) |
| The loader writes `artifacts/logs/loader_call.jsonl` | `engine/charts/loader.py` lines 57 to 73 and 167 to 173 | `_log_call` appends to that path in `load_chart`'s `finally` block; the file is tracked (blob `925569528ffc`) |
| The loader is not a release member | `catalog/manifest.json` (blob `bd42f2791d51`) | 45 members; none is `engine/charts/loader.py` |
| Replacing coverage exists | `git grep` in `tests/provider/` | Both named tests are defined |
| Close report defers HDE-SEPA006 | `audit/HDE-CRD-0002_close_report.md` "Deferrals" | Entry `HDE-SEPA006`: "Deferred to the Product Owner as decision owner" |
| Current loader callers | Bounded `git grep` for `engine.charts.loader` outside `docs/`, `audit/` and `artifacts/` | `scripts/make_compat_determinism_artifacts.py` (keyword form of the new signature) and two `tests/loader/` files (new positional signature); historical copies under `.audit_src/`. This supports, without restating, the HDE Build Notes record; the PF09 text attributes the legacy-signature caller facts to HDE Build Notes |

Not checked directly, and attributed in the text instead: the `6c6f4b2a` origin date (the clone is shallow and that commit is not present), the `AttributeError` at runtime (no test or code was run), and "not reached at runtime".

## 9. Header provenance for TW-APPLY-10

- Baseline native header: `**Title:**`, `**Version:** v1.1.7`, `**Status:** Canon`, `**Effective date:** 2026-10-11`, `**Last Update Gate:**` (five sources), `**Invocation tag:**`. Version scheme: `v`-prefixed three-component dotted numeric. Date format: `YYYY-MM-DD`.
- Sources that justified this update, in source order: `PF10-HDE-Build-Notes-v13.8.8.md` (PF10 version 13.8.8); `HDE-CRD-0002-specification-v1.1-approved.md`; `HDE-CRD-0002-specification-delta-v1.0.md`.
- Internal restatements of the version or date: none outside the header. Line 1170's "2026-10-11" is the Product Owner's CRD-drafting acceptance date, not a document-control date.
- The target has no change log, revision history or Doc-Delta section, so no history entry is prepared.
- Hygiene scan: no `Draft` status language, placeholder, TODO, unresolved drafting note or instruction to a future writer that the rule reaches. The "placeholders" hits at original lines 540, 559 and 562 are substantive evidence rules. Line 825's "IMPORTANT: Do not use or cite the token `CLI_STDERR_ONLY_ON_ERROR_OK`" is a substantive token-governance statement and stays. No hygiene redline is needed.
- No redline touches the header.

## 10. Observations left unchanged (outside the assigned rows)

- Original lines 1164 and 1174 (HDE-SEPA005) say HDE Build Notes supplies the adopted C040 decisions. The current HDE Build Notes does not appear to hold them. Whether C040 drainage is complete is held item H-01 (FND-021, Product Owner), so they are not touched. Line 1168 cites a live-vendor-call rule "required by HDE Build Notes"; it was not assessed against v13.8.8.
- Original line 356 has a doubled comma ("`CLI_READER_PARITY_OK`, , `EVIDENCE_INDEX_UPDATED_OK`"); line 1377 holds an escaped "\#" export artifact; lines 172 and 1167 call HDE-SEPA006 and HDE-COAG003.9 "new". None is in the assigned scope or is a hygiene marker, so none is changed.

## 11. Producer validation

The same checks ran twice: on the authored batch before writing, and on the saved file, parsed back from its own bytes. Every literal parsed from the saved file equals the authored literal.

| ID | Operation | Section path (resolved uniquely) | Expected / observed, whole original | Observed in section | Original location | Payload |
| :- | :- | :- | :- | :- | :- | :- |
| RL001 | REPLACE | Phase III | 1 / 1 | 1 | lines 172 to 173 | 608 characters |
| RL002 | REPLACE | Phase III > Task HDE-SEPA005 | 1 / 1 | 1 | line 1167 | 785 characters |
| RL003 | REPLACE | Phase III > Task HDE-SEPA005 | 1 / 1 | 1 | line 1170 | 1,720 characters |
| RL004 | REPLACE | Phase III > Task HDE-SEPA006 | 1 / 1 | 1 | line 1293 | 374 characters |
| RL005 | REPLACE | Phase III > Task HDE-SEPA006 | 1 / 1 | 1 | line 1297 | 136 characters |
| RL006 | REPLACE | Phase III > Task HDE-SEPA006 | 1 / 1 | 1 | lines 1314 to 1316 | 2,074 characters |
| RL007 | INSERT | Phase III > Task HDE-SEPA006 > Subtask HDE-SEPA006.2 | 1 / 1 (anchor pair) | 1 | gap at line 1355, column 1 | 409 characters |

- Operation dialects: REPLACE and INSERT only. There is no FIND AND REPLACE, so the RL-045 rule does not apply.
- Every old block is non-empty and differs from its replacement. Each INSERT anchor pair is contiguous and unique, and neither anchor is consumed. Every newline is in the literal.
- Whole-batch conflict check: no intersecting spans; the gap lies inside no span and on no span boundary; no two insertions share a gap; no edit at the header (lines 7, 11, 13).
- One-pass simulation in descending offset order against the unchanged original: 89,843 bytes, SHA-256 `ae396c4d14f8cb9787b06c1bfa08c3e1c11a4e7713699a21fc9e1af4d723214a`. A reconstruction from the untouched original intervals plus the payloads equals it. This simulation has no header changes; Apply adds them.
- Payloads contain no fence, no ASCII three-period ellipsis and no Unicode ellipsis, and they cite HDE Build Notes by title only.
- Preparer corrections before READY, within this run: the first saved file (SHA-256 `9ca35cb1bc59b6323c90892e721253af086f04f9b8e8367d5a0435a95029c57e`) was never offered for Apply. Two changes were made, and the whole batch was revalidated:
  - RL003's S03 clause was reworded.
  - RL007 had stated a new requirement ("must record it as retired") that no source gives; it now states evidence and its limit.

## 12. Dependencies, blockers and limits

- No blocking dependency, missing source or decision. No held item is drafted.
- The defect facts that could not be executed or reached in history are attributed to HDE Build Notes (§8).
- The redlines change documentation only. They prove no code change, test result, QA verdict, acceptance or closure.

## 13. Save completeness

Receipt, recorded after the saved pair was read back on 2026-10-26:

- The redlines file was read back complete: 22,483 bytes, SHA-256 `8462e62add2061aec30e3eaa76dfdf032a3a9537746040b6a15f171dfbbb9e29`. It ends with `END OF REDLINES` and parses back to seven operations equal to the authored literals.
- This proof log was read back complete, sections 1 to 13, before this receipt was added, and again after. It does not carry its own hash.

Save completeness: `COMPLETE_PACKAGE`. Preparation outcome: `READY`.

Next step: TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b), in this same document session, as the handoff authorizes. It uses:
- the original at blob `1e8fb350a7ab`;
- this redlines file and this proof log;
- ledger task T-PF09.3;
- the selected sources in §3;
- branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`.

Its outputs are `PF09.3-from-v1.1.7.md` and `PF09.3-from-v1.1.7.proof-log.md` in this directory, or `apply-diagnostic-PF09.3-from-v1.1.7.md` if Apply fails.
