# Proof log: redlines for PF09.4-Canon-HDE-Build-Checklist-Conjunction, from v1.3.1

This is the processing report for `redlines-PF09.4-from-v1.3.1.md`, the file beside it. It records how that redlines file was prepared, from what, and what was verified. It is not a revised PF, not QA, not acceptance, not canon adoption and not a closure decision.

## 1. Artifact and identity

| Field | Value |
| :- | :- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf09-4/redlines-PF09.4-from-v1.3.1.md`: 17,856 bytes, 239 lines, SHA-256 `7060a860ac75376667062d46cf12e2bd2de7213329f2cd30333ff9b007de9271` |
| Task | T-PF09.4 of the ledger `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`: PF09 phase-file preparation (TW-DRAIN-20), followed in this same session by application (TW-APPLY-10), as Nathan's handoff authorizes |
| Run identity | `T-PF09.4-PREP-20261026-01`. First preparation run for this target and source version; no earlier output existed under `pf09-4/` |
| Preparer | Claude Code cloud session https://claude.ai/code/session_01TJJV6QvnTufZxMtDS6LUip, started by Nathan for T-PF09.4. One session, no subagent, no reviewer |
| Prompt | TW-DRAIN-20 — Prepare PF09 Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb815ebfd2cf992bec9862, body fetched live on 2026-10-26 (page last edited 2026-10-09T11:05:22.094Z) |
| Preparation outcome | `READY` |
| Save completeness | `COMPLETE_PACKAGE` (§12) |
| Prepared | 2026-10-26, between 21:34Z and 21:40Z |

## 2. Turn preflight

1. Task: preparation of exact redlines for one assigned PF09 phase document, PF09.4 (Conjunction). It creates no section and does not apply anything; application follows under TW-APPLY-10.
2. Identities and access: every file below was read from the repository with `git show origin/main:<path>` or the working tree at `0838ba08254eaefc888019df49a06aa2ae99cc6c`; both prompts were fetched live from Notion. Nothing came from Google Drive, memory or a copy.
3. Selected scope: PF10 v13.8.8 addenda 2.8 and 2.35 (ledger rows A08 and A35), each read heading to next heading; X04 read at its stated boundary. The PF10 front matter (lines 1–223) was read for the application rules.
4. Target reading: the complete PF09.4, lines 1–2,185. Output: nine redlines, about 18 KB.
5. Capabilities: Python 3 for exact-match checks, git for read-only inspection, push access to the destination branch. No production, vendor, database, Railway, TypeSafe or Google Drive access was used or needed. Closed rails stayed at their defaults; nothing was executed against a service.

## 3. Destination

- PR [amthorn78/glow-hdengine-v2#760](https://github.com/amthorn78/glow-hdengine-v2/pull/760), the ledger PR, had merged (2026-10-26T21:18:51Z, merge `0838ba0`) when this session started. Following the handoff and the ledger's continuation line, this session uses `docs/20261026-gtwpe-pf10-v13-8-8-documents`.
- At 21:34Z, `git ls-remote origin 'refs/heads/docs/20261026-gtwpe-pf10-v13-8-8*'` returned nothing, and the repository had no open pull request. This session then created the branch locally from `origin/main` at `0838ba08254eaefc888019df49a06aa2ae99cc6c`.
- Before this session pushed anything, another document session created the remote branch: commit `28184ea` (T-PF07, on `0838ba0`, 2026-10-26T21:38:20Z). That session opened the shared draft PR [amthorn78/glow-hdengine-v2#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761) at 21:39:03Z. This session fetched the branch, kept every earlier commit (`28184ea`, `253fc6b`, `3fa8745` and `6241cb7`, all outside `pf09-4/`), and rebased its own unpushed commit onto the remote tip before its first push. The tip moved once more, to `6241cb7`, while it was rebasing. The package landed as `bd4ca40` on `6241cb7`. It reuses #761 and opens no second PR.

## 4. Sources and inputs

| Role | Path | Identity | Coverage |
| :- | :- | :- | :- |
| Target and original baseline | `docs/pfcanon/PF09.4-Canon-HDE-Build-Checklist-Conjunction-v1.3.1.md` | Title `PF09.4-Canon-HDE-Build-Checklist-Conjunction`, v1.3.1, Status Canon, Effective date 2026-10-11; blob `3abe7fc79d6987006590b65d39ab9e1f60da9538`; 111,181 bytes; 2,185 LF-terminated lines, no CR; raw-byte SHA-256 `65d4b9e2a1303638cc5c66a1d02f55c721509559d24ee8e42cb04a793750ac84`. Last changed by `2ff696b` (2026-10-24); identical at the ledger baseline `9dda63dd` and at `0838ba0` | Read in full, lines 1–2,185 |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` | HDE Build Notes v13.8.8, effective 2026.10.26, the sole unlettered representation on `main`; blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`; 729,539 bytes; SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`, equal to the handoff and the ledger | Front matter and index, lines 1–223; addendum 2.8, lines 890–1002; addendum 2.35, lines 3725–3955 (through the stored `\<eof\>` marker) |
| Supporting cross-reference X04 | `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md` | blob `1d6a92a483e2` | §18, lines 753–792; lines 745–752 (the end of §17) read as context only |
| Routing record | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` | blob `74944b261c0ebb2f80a416fb004b9a913da592d1`, identical at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` and on `main` | Read in full, including "Precedence and closure controls" and "Held and deferred items" |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` | v1.8.8 | Read in full |
| Supporting reading: transport owner | `docs/pfcanon/PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.3.md` | Title `PF05-Canon-HDE-CLI-API-Vendor-Ref`, v2.5.3, blob `8b136def4c22` | Header (lines 1–14) and §5.4 "Dev harness routing and guard (dev-only)" in full (lines 2410–2475) |
| Supporting reading: approved Specification | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` | blob `c4802a5a7fa3`; SHA-256 `fb412f178fa0ecae527704b16ced4be2c28e42a84e663ccbebdbdb669b7382df` | Requirements S01–S22, Exclusions, Constraints, dependencies (lines 72–145) |
| Supporting reading: delta 01 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` | blob `9408d6ed091b`; SHA-256 `59ef9a776c6b5615333cfe68ba4d8145a3d1fe1fdd194b12bb24cf71a233b636` | §2, changes C-1 to C-14 |
| Approval evidence X10 | `docs/ephemeral/HDE-CRD-0002-specification-review-v1.1.md` | blob `c48f77a0c220` | Decision line: `INITIAL_APPROVE` (Thoth) |
| Approval evidence SR4 | `docs/ephemeral/HDE-CRD-0002-specification-delta-review-v1.0.md` | blob `5a6cecc86f60` | Identity check; DELTA_APPROVE as recorded by PF10 2.20 and the ledger |
| Closure evidence X11 | `docs/ephemeral/HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` | blob `2260eae17974` | Front matter: `decision: CLOSE`, `state: CHANGE_CLOSED`, `decision_time: 2026-10-26T16:40:00Z`, owner Isis |
| Closure evidence X12 | `docs/ephemeral/HDE-CRD-0002-CL-20-post-closure-record-v1.0.md` | blob `ac60f368f6d9` | Manual actions M-0 to M-3; M-0 (this drainage) pending |
| Closure evidence X13 | `docs/ephemeral/HDE-CRD-0002-QA120-qa-report-v1.0.md` | blob `d6cceaf3a019` | `verdict: PASS`; check table rows for checks 2, 8, 9, 17 and 20; requirement map (S02 → 17; S03 to S05 → 2; S11 to S13 → 8; S14 → 9 and 20) |
| Closure evidence X14 | `audit/HDE-CRD-0002_close_report.md` | blob `0bbc8050d3c1` | "Deferrals" read in full (34 entries): none concerns a PF09.4 location changed here |

Every blob prefix named in the handoff and the ledger matched `origin/main`. `docs/pfcanon/` has no change between `9dda63dd` and `0838ba0`, so the target and the source are at their routed baseline.

## 5. Precedence applied

- HDE Build Notes front matter §2, §5 and §9: each addendum governs its own scope; supersession is per addendum. 2.18 (withdraws the cost-ceiling passages of 2.11 to 2.16), 2.14 (narrows 2.11 rules 7 and 8) and 2.17 (amends 2.15) do not touch 2.8's or 2.35's scope. 2.11's misnumbered cross-references are not relied on. Neither 2.8 nor 2.35 supersedes anything ("It supersedes no addendum"; "Supersedes nothing and amends no earlier addendum").
- Closure: HDE-CRD-0002 is `CHANGE_CLOSED` (X11), after final QA `PASS` (X13). Nothing in this task is held on closure grounds.
- The Specification in force is v1.1 with delta 01 by overlay. S01 is removed (C-1, C-6). The release stays at `1.3.0` (C-5).
- PF09.4 §0.4 "Authority and Work-Record Routing": PF09 does not redefine transport contracts, so PF05-Canon-HDE-CLI-API-Vendor-Ref owns the harness headers. CRD work is not duplicated in PF09; the Specification's Exclusions state "No PF09 mapping of this work (Plan Templates §2A)". These redlines update existing notes about observations the target already carried. They map no CRD work into PF09.
- PF09.4 §0.3 "Repository support versus PF09 status": an existing PF09 statement does not override contradictory current repository reality.

## 6. Change and disposition ledger

Each change in the selected scope, with its disposition and the target locations that support it.

| # | Selected change (source) | Disposition | Target location and basis |
| :- | :- | :- | :- |
| C1 | 2.35 R-2: HTML 404 delivered (S02) | Actionable: RL-03 | Line 1112 named "the carried HTML-404 transport observation" (O-P06a-22, the source of S02). `main` `adapter/factory.py` lines 30–33 answer every 404 with the governed `ERR_NOT_FOUND` envelope, `no-store`, no ETag. X13 check 17 (`qa-17-deployed-not-found`, deployed target) `PASS` |
| C2 | 2.35 R-2: CLI proof test and out-of-lane failures delivered (S03) | Actionable: RL-03, RL-07, RL-08, RL-09 | Lines 1112, 2089, 2139 and 2177 kept "the legacy CLI proof failure" with its owner. `main` `tests/retired_tests.md` line 65 retires `tests/reader_v1/test_cli_proof.py` (2026-10-13) for O-P06a-03, "the stub is not a Reader surface (PF05 §5.1.6) and not proof (PF29 §16)"; the file is absent under `tests/reader_v1/`. X13 check 2 `PASS` |
| C3 | 2.35 R-2: engine-core currency and Mirror labels delivered (S11, S12) | Actionable: RL-03 to RL-09 | Lines 1112, 2089 and 2139 carried "evidence-owner currency/provenance observations"; lines 1371, 1811, 1994 and 2177 kept O-P06b-17 with the evidence/updater owner. The Specification maps S11 to O-P06a-23 and S12 to O-P06b-17. X13 check 8 (S11, S12, S13) `PASS`. Attributed to the QA record; the Mirror labels themselves were not re-inspected |
| C4 | 2.35 R-2: wheel installs removed (S01) by Product Owner decision | Actionable: RL-03, RL-07, RL-08 | Lines 1112, 2089 and 2139 carried "the wheel-distribution decision" (O-12, the source of S01). Delta 01 C-1 and C-6: S01 removed by the Product Owner's decision of 2026-10-21; "a regular wheel install outside a source checkout still does not admit the release". On `main`, `.github/workflows/ci.yml` lines 90–95 install `'setuptools>=68' wheel -r requirements.txt -r requirements-dev.txt -e .`, an editable install with the `wheel` build package. Neither workflow builds or installs a project wheel. A `git grep -i` for `wheel`, `bdist`, `.whl`, `python -m build` and `pip install .`/`dist` over `.github/workflows/` found only that line |
| C5 | 2.35 R-2: `--allow-prod-vendor` delivered (S14) | No location in this target | PF09.4 contains no `allow-prod-vendor`, `prod-vendor` or `DD-04` text (bounded search of the whole baseline, count 0). The R-2 note naming it is PF09.3's (lines 1167 and 1170; T-PF09.3). Confirmed on `main`: `engine/cli/main.py` line 52 defines `_ALLOW_PROD_VENDOR = "--allow-prod-vendor"`, with its usage refusals on lines 53–59. X13 checks 9 and 20 `PASS` |
| C6 | 2.35 R-2: code security review delivered (S19) | No location in this target | No `S19` or `security review` text in PF09.4 (count 0) |
| C7 | 2.35 R-2: no PF30 record created (CR-1) | No location in this target | PF09.4 has no "PF30 record, once entered" statement ("once entered" count 0). Line 136 is the general PF09/PF30 boundary rule and stays |
| C8 | 2.35 R-1, R-3, R-4, R-5 | Out of this target | HDE-SEPA006 (PF09.3, T-PF09.3); HDE-COAG001.9, HDE-COAG001.4, HDE-COAG003.8 and .9 (PF09.7, T-PF09.7). PF09.4's DEFERRED notes to HDE-COAG003.8 and .9 (lines 2141 and 2179) are unchanged by R-5, which 2.35 records as "listed to avoid re-recording", with the posture "unchanged" |
| C9 | 2.35 "No PF09 gap"; candidates 9 and 10; item 11 | No relevant change | No new PF09 row: no gap is found, and the Specification excludes PF09 mapping |
| C10 | 2.8 with X04 §18: OBS-P3-16 | Actionable: RL-01, RL-02 (decided: the row text changes, its status does not) | X04: HDE-CONJ001.1 says `no-store` on all harness responses, while PF05 §5.4 "Headers (A7 posture applied to harness)" sets `Cache-Control: private, max-age=0, must-revalidate` on the dev Reader's `200` and `no-store` with no `ETag` on errors. 2.8 "Required canon drainage" names the plan v2.0 §18 doc-delta candidates. The same claim appears at line 249 (HDE-CONJ001.1) and line 212 (HDE-CONJ001 task notes). On `main`, `adapter/http_reader.py` sets the dev `GET /reader` `200`, `HEAD` `200` and `304` through `_set_reader_200_headers` (lines 40–44; used at 734, 744, 751), and `artifacts/proofs/success_get.txt`, `success_head.txt` and `success_304.txt` record `cache-control=private, max-age=0, must-revalidate`. The dev sampler, dev conjunction and writer `200`s and every error set `no-store`. Status Done stays: the behavior is implemented as the owner contract requires; only the PF09 restatement was wrong |
| C11 | 2.8: CR-7 drainage, the 2.7 candidates, the other X04 §18 rows | Out of this target | HDE Schemas & Artifacts §8.8, HDE CLI/API/Vendor Ref §5.6, HDE Mechanics Guide §34, HDE Users Guide §4.1, HDE Architecture §3.4, and repository documents; routed by the ledger to T-PF12, T-PF05, T-PF14, T-PF29 and T-PF02 or to their owners |
| C12 | 2.8: LR3-O1 | Not a drain target | A PF10 publication fact (ledger, "Precedence and closure controls") |
| C13 | 2.8 "Epic, task, and status effects": no PF09 row changes status | Consistent; no status redline | Every row status below is judged unchanged |
| C14 | X04 §17 row citing HDE-CONJ001.1 for the loopback bind (line 748; context only) | Already represented | HDE-CONJ001.1 line 241 ("Bound only to loopback") and line 245 (debug reloader OFF) agree with AD-3 |

### Interpretations and inferred details

- **Scope of R-2 inside PF09.4.** 2.35 names line 1112 (HDE-CONJ005 notes) and line 2139 (HDE-CONJ010.4 notes). The same now-resolved observations are also carried at lines 2089 (HDE-CONJ010 task notes), 1371 (HDE-CONJ005.4), 1811 (HDE-CONJ008.3), 1994 (HDE-CONJ009.2) and 2177 (HDE-CONJ010.6). TW-DRAIN-20 requires judging every row the supplied change potentially affects, and the resulting PF09 must show the current state. These five locations are therefore drained on the same basis (RL-04 to RL-07, RL-09). The basis is the facts 2.35 R-2 records, not a new source.
- **Inferred mapping (labelled).** "Evidence-owner currency/provenance observations" is read as O-P06a-23 and O-P06b-17. Basis: the Specification's Source column for S11 and S12, and 2.35 R-2's "engine-core currency and Mirror labels (S11, S12)".
- **"Success family."** RL-02 names the dev Reader `GET` `200`, `HEAD` `200` and `304` as the exception. Basis: PF05 §5.4 ("Success (200)" headers; "Conditionals (dev stability)") and the `main` code and proofs cited under C10. RL-01 and RL-02 route the exact header values to PF05 by title and section rather than restating them (PF03 §5).
- **Left unchanged.** Line 204, the HDE-CONJ001 task description, says the harness "enforces no-store and canonical JSON". It makes no "on all responses" claim and agrees with `no-store` on errors and writers. Line 369 (HDE-CONJ001.4) already says `no-store` for errors.

## 7. PF09 coverage duties

| Duty | Disposition | Locations |
| :- | :- | :- |
| 1. Subtasks | Changed (notes, evidence, description); every status unchanged | HDE-CONJ001.1 (RL-02, Done), HDE-CONJ005.4 (RL-04, Done), HDE-CONJ008.3 (RL-05, Done), HDE-CONJ009.2 (RL-06, Done), HDE-CONJ010.4 (RL-08, Partial: the consumer-migration burden is untouched by HDE-CRD-0002), HDE-CONJ010.6 (RL-09, Partial: the full-matrix burden is untouched) |
| 2. Tasks | Changed (task notes); every status unchanged | HDE-CONJ001 (RL-01, Done), HDE-CONJ005 (RL-03, Done), HDE-CONJ010 (RL-07, Partial). IDs, titles, order and dependencies preserved |
| 3. Phase statuses | No relevant change | Phase master status "Not done", the Done/Partial/Not done lines and the phase notes (lines 160–191). HDE-CRD-0002 changes no phase status: no PF09 mapping, no PF09 gap, and 2.8 changes no PF09 status |
| 4. New rows | No relevant change | No source supplies a new task or subtask (C9) |
| 5. Evidence | Changed | RL-03 to RL-09 record the resolving requirement and its QA check for each carried observation. Supplied evidence is attributed to the QA Report and closure, not presented as a new inspection, except where §6 names a direct `main` inspection |
| 6. Epic information | No relevant change | HDE-CRD-0002 is a CRD, not an Epic. The HDE-EPIC040, EPIC026 to EPIC029 and "Epic or card" fields are unchanged |

## 8. Held items

None touched. H-01 to H-06 concern HDE Math Spec §§6.1–6.2, PO-2's home, HDE CLI/API/Vendor Ref §5.11.2 and §5.12, §7.1.11f, the Glow Infrastructure procedure gap and HDE Governance §9.1.1. None has a PF09.4 location.

## 9. Outside dependencies

None blocking. No unresolved change remains in the selected scope.

## 10. Document-control fields for TW-APPLY-10

| Field | Native form | Baseline value |
| :- | :- | :- |
| `**Version:**` (line 7) | dotted numeric with `v` prefix | `v1.3.1` |
| `**Effective date:**` (line 11) | `YYYY-MM-DD` | `2026-10-11` |
| `**Last Update Gate:**` (line 13) | `; `-separated source list | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md; HDE-EPIC040-CL-40-cycle-gap-scan-v1.0.md` |
| `**Status:**` (line 9) | `Canon` | not stale |
| `**Title:**` (line 5) and `**Invocation tag:**` (line 15) | — | protected; the title carries no version |

- Sources that justified this update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, version 13.8.8, so the gate form is `BN 13.8.8`. X04 is supporting reading carried by 2.8, and the ledger declares that X-references are not change sources in their own right. The Specification, delta and closure records are supporting and closure evidence.
- No internal restatement of the version or date exists outside lines 7 and 11 (bounded search for `v1.3.1`, `1.3.1` and `2026-10-11`).
- The target has no change log, revision history or Doc-Delta section, and its rules require none, so no history-entry redline is prepared.
- Hygiene: the baseline carries no `Draft` status language, TODO, TBD, FIXME, unresolved drafting note or instruction to a future writer. The angle-bracket forms at lines 63, 333, 348 and 382 are canon's own deferral template and path patterns, so they stay.

## 11. Producer validation

The batch was validated against the unchanged original before the file was written. It was then validated again by parsing the saved redlines file independently and checking its literals against the baseline bytes.

| ID | Operation | Original lines | Section span (lines) | Expected | Observed | Byte span | Checks |
| :- | :- | :- | :- | :- | :- | :- | :- |
| RL-01 | REPLACE | 210–212 | 195–457 | 1 | 1 | 14629–14691 | pass |
| RL-02 | REPLACE | 249 | 232–266 | 1 | 1 | 16275–16331 | pass |
| RL-03 | REPLACE | 1112 | 1094–1374 | 1 | 1 | 55806–56181 | pass |
| RL-04 | REPLACE | 1371 | 1302–1374 | 1 | 1 | 69350–70055 | pass |
| RL-05 | REPLACE | 1811 | 1794–1840 | 1 | 1 | 86657–87294 | pass |
| RL-06 | REPLACE | 1994 | 1971–2071 | 1 | 1 | 98093–98653 | pass |
| RL-07 | REPLACE | 2089 | 2072–2186 | 1 | 1 | 103764–104122 | pass |
| RL-08 | REPLACE | 2139 | 2124–2150 | 1 | 1 | 106058–106685 | pass |
| RL-09 | REPLACE | 2177 | 2162–2186 | 1 | 1 | 109327–109984 | pass |

- Checks per redline: OLD count over the whole original is exactly 1; it starts at the stated line; it lies inside the deepest heading's section; each heading in the path occurs once (headings inside fences excluded) and nests in the one before; OLD and NEW are nonempty and differ; no payload contains a fence; no NEW contains an ellipsis.
- Batch: all nine spans are disjoint and share no boundary. The document-control lines 7, 11 and 13 lie outside every span. No `FIND_AND_REPLACE`, so RL-045 does not arise.
- Word-level diffs of OLD against NEW show only the intended changes; the retyped unchanged text of RL-04 to RL-09 matches the original.
- One-pass simulation (descending offsets, content redlines only): 112,928 bytes, SHA-256 `8ac7b2c6beec10444a426e8f89dcc9d8bdb330f892c67cba59c89463382eef90`; each NEW present once, no OLD left, line count unchanged. Apply adds the header plan to this.
- Saved file: nine redlines parsed, payloads byte-equal to the validated batch, terminal `END OF REDLINES` present.
- Correction during preparation: RL-08's retirement reason was widened, before the file was written, to "neither a Reader surface nor proof", matching `tests/retired_tests.md` line 65. The whole batch was revalidated after that change.

## 12. Save verification

- `redlines-PF09.4-from-v1.3.1.md` was read back completely after writing: 239 lines, 17,856 bytes, SHA-256 `7060a860ac75376667062d46cf12e2bd2de7213329f2cd30333ff9b007de9271`, parsed and revalidated (§11).
- This proof log was read back completely after writing, at 2026-10-26T21:40Z. It was corrected (full Specification and delta hashes in place of shortened ones; two ellipses removed by rewording) and read back again. §3 was corrected at 21:44Z, when the remote branch and #761 were found, and the file was read back again.
- Result: `COMPLETE_PACKAGE`; outcome `READY`. This receipt was added after both files were verified.

## 13. Observations outside this task's scope (not changed)

No selected source raises these, so they are reported, not drafted.

- HDE-CONJ001.1 cites `tests/harness/test_end_to_end.py` as evidence (line 265). No such file, and no `tests/harness/` directory, exists on `main` at `0838ba0`, and the path has no history there. Owner: the PF09 owner.
- Line 1401 begins `**tatus (Drain 10.3.3 — 15-19 HDE-EPIC028 CHECK po-006):**`, missing its first letter.
- Line 382 contains the Unicode ellipsis character U+2026 directly after `audit/qa/<epic>/`. PF03 §3 prohibits that character in PF documents.
- HDE-CONJ005.3 (lines 1247–1300) wraps its description, notes, tokens and evidence in inline code spans.

## 14. Canon relied on

- PF10-HDE-Build-Notes v13.8.8 (HDE Build Notes): front matter "Precedence, versioning, and scope" §1 to §9 and "Cross-references"; addendum 2.8 ("Required canon drainage"; "Epic, task, and status effects"); addendum 2.35 ("PF09 row-closure record", relation R-2; "Required canon drainage").
- PF09.4-Canon-HDE-Build-Checklist-Conjunction v1.3.1: §0.3 "Task, Status, and Deferral Conventions" ("Repository support versus PF09 status"); §0.4 "Authority and Work-Record Routing" ("Epic and CRD boundary"); §0.5; §0.6.
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3: §5.4 "Dev harness routing and guard (dev-only)", "Headers (A7 posture applied to harness)" and "Conditionals (dev stability)".
- PF03-Reference-Technical-Writing-Best-Practices v1.8.8: §3 "Canonical ownership" and "Claim-state separation"; §5; §7; §8 (the operator's TW-DRAIN-20 format governs); §11.
- `AGENTS.md`: "Canon-first rule", "PF canon is read-only unless the prompt explicitly directs a change", "Truncation/retrieval-failure guardrail".

## 15. Next step

TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b), run in this same session as Nathan's handoff authorizes. Its inputs: the original baseline above, this package, ledger task T-PF09.4 with rows A35 and A08/X04, branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, outputs `pf09-4/PF09.4-from-v1.3.1.md` and its proof log, or `pf09-4/apply-diagnostic-PF09.4-from-v1.3.1.md` on failure.
