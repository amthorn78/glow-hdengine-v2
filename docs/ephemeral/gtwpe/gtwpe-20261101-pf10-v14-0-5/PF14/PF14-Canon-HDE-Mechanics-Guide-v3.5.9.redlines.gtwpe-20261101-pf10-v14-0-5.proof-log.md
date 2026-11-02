# Proof log: PF14 redlines, run gtwpe-20261101-pf10-v14-0-5 (T-05)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.md` (r3: 71,306 bytes; SHA-256 `b67170fef2a9c2c60f1d21b125d5e219c53b9369febb2b034145b940bbf62b5c`) |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-05/prep-r3`. It supersedes `prep-r2` (redlines 30,050 bytes, SHA-256 `af0883ccc9366cbf7a23b0ca162c4a76df666d602f53978e848316b3f6346fff`, commit `ea4c6cf`), which superseded `prep-r1` (27,268 bytes, SHA-256 `68f6083df1e1134fce4bfb7c29ffd010dd9dcec6f3a1dffb4c8a55d231150d21`, commit `9de402f`). §12 and §13 record why |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live when each preparation step began, the last time for r3 (page state 2026-10-09T11:05:22Z, unchanged) |
| Authorized sequence | Nathan's handoff authorizes TW-DRAIN-10, then TW-APPLY-10 100926.1 (page `3f44590a05eb81eebff6e3afa3d9aa5b`) in this one session, after a READY / COMPLETE_PACKAGE result. Nathan's later direction in this session widens the edit scope (§13) |
| Preparer | The T-05 document session Nathan started, Claude Code session `https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z`. No subagent, reviewer or other session was used |
| Prepared | 2026-11-02: r1 saved about 00:30Z; r2 about 00:42Z; r3 about 02:40Z |
| Preparation outcome | `READY` |
| Save state | `COMPLETE_PACKAGE`: both files saved and read back in full (§9) |
| Correction route | An Apply diagnostic returns to TW-DRAIN-10 in this session, which issues a corrected package under a new run identity |

## 2. Sources and inputs

| Role | Identity | Coverage |
| :---- | :---- | :---- |
| Target, original | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md` at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. Title `PF14-Canon-HDE-Mechanics-Guide`, v3.5.9, Status Canon, Effective date 2026-10-26, Last Update Gate `BN 13.8.8`. Git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`; 669,363 bytes; SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59`; 7,734 LF characters; 7,735 lines, the last (`* presence and correctness of path-proofs`) without a trailing LF | Complete. §3 gives the windows |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` at `e2b7427`. HDE Build Notes v14.0.5. Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines | The selected units, complete (§3) |
| Direction | Nathan, 2026-11-02, in this session, after the r2 application report: "I want you to fix the defects and inconsistencies you noticed" | Governs r3's scope (§13) |
| Decision record | `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md` (blob `1c65c85339cb`), GTWPE-D3 (lines 114 onward): "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target"; "Canon sets the timing" | Read lines 114–150 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` at `e2b7427`, v1.8.8, 43,953 bytes, SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462` | Complete, lines 1–633 |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at triage `142feb35144d8795f927e0c78b665ace52279064`, and as corrected 2026-11-02, read again at `e0375498df16b94a8be5edb339b54416936ffa54` (§1 correction note, §2 register, §3 rows, §4, §8) | Planning and provenance only, not a change source. The correction leaves T-05's row unchanged |
| Currency check | `git diff --stat e2b7427 origin/main -- docs/pfcanon/` is empty at `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`; the target's SHA-256 at `origin/main` is the baseline's | Read-only, repeated for r3 |
| Supporting canon (r1, r2) | HDE CLI/API/Vendor Ref (`PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`) §7.1.10 in full; HDE Architecture (`PF02-Canon-HDE-Architecture-v2.4.7.md`) §1.1 paragraph "Non-BodyGraph chart loader classification"; HDE CRD Records (`PF30.1-Canon-HDE-CRD-Records-v0.9.2.md`), the HDE-CRD-0002 status line (`Closed`, line 466) | Supporting reading only |
| Supporting canon (r3), on `origin/main` | HDE Governance (`PF04-Canon-HDE-Governance-v2.8.8.md`, blob `0c3ce100f942`) §4.1.4, "Dev/admin APP_ENV gating"; HDE CLI/API/Vendor Ref (blob `53e6a9028dfa`) headings §5.5 (line 2476) and §7.1.11 (line 3505); Glow Infrastructure (`PF07-Canon-Glow-Infrastructure-v2.3.4.md`, blob `60fd3f0b3fef`) line 1227; HDE Narratives Guide (`PF17-Canon-HDE-Narratives-Guide-v1.5.4.md`, blob `3cc04c021812`) line 845; HDE Schemas & Artifacts (`PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.7.md`, blob `d5bc01f83078`) line 1992; HDE Architecture (blob `9a23eec67198`) lines 119 and 1056; HDE Phased Epics (`PF20-Reference-HDE-Phased-Epicsv1.9.6.md`, blob `e168dc0eba81`) line 4377; HDE Build Checklist Conjunction (`PF09.4`) line 333; HDE Build Checklist Fermentation (`PF09.5`) line 1051 | Read at the cited sections and lines, for ownership and the intended text of the formatting repairs |
| Closure evidence | `docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md`, blob `5075f5ea5a2e60e0987ce427df4c4c5b796f662b`: `closure_state: CHANGE_CLOSED`, `outcome: CLOSE / CHANGE_CLOSED` (lines 11, 40, 45) | Read at the cited lines |

Source roles. HDE Build Notes v14.0.5 is the only change source. Nathan's direction sets r3's scope and authorizes the formatting repairs; it is not a source of canon text. PF14 is the target. Canon was read from `docs/pfcanon/` on `main`. The approved HDE-EPIC041 Specification was not read: no selected row drains it, and the ledger queues no Specification edit (ledger §6).

## 3. Coverage

PF14 was read completely, in 31 recorded windows. Byte counts are UTF-8 bytes, each line counted with one line ending; their sum is 669,364, which is the file's 669,363 bytes plus the count for its final, unterminated line.

| Lines | Bytes | Lines | Bytes | Lines | Bytes |
| :---- | ----: | :---- | ----: | :---- | ----: |
| 1–218 | 23,546 | 2723–3029 | 23,510 | 5572–5830 | 23,533 |
| 219–395 | 24,158 | 3030–3306 | 23,621 | 5831–6042 | 23,829 |
| 396–630 | 23,503 | 3307–3586 | 23,687 | 6043–6274 | 23,588 |
| 631–872 | 23,627 | 3587–3887 | 23,583 | 6275–6501 | 23,642 |
| 873–1103 | 23,699 | 3888–4257 | 23,666 | 6502–6699 | 23,597 |
| 1104–1277 | 23,674 | 4258–4651 | 23,619 | 6700–6949 | 23,674 |
| 1278–1608 | 23,500 | 4652–4967 | 23,637 | 6950–7336 | 23,649 |
| 1609–1862 | 23,709 | 4968–5140 | 16,796 | 7337–7350 | 1,885 |
| 1863–2161 | 23,616 | 5141–5268 | 6,744 | 7351–7540 | 15,680 |
| 2162–2430 | 23,543 | 5269–5571 | 23,545 | 7541–7735 | 13,794 |
| 2431–2722 | 23,510 | | | | |

One PF14 window (7337–7735) and two HDE Build Notes windows (552–753 and 1048–1145) first came back as tool-truncated previews. Each was re-read in narrower windows, the ones recorded here; no claim relies on a preview. Where a long line was first printed cut at a fixed width, its remainder was printed and read. For r3, every changed line and its neighbors were printed again from the original, and every line containing a double backslash was listed by script (§10).

HDE Build Notes v14.0.5, selected units, each read completely:

| Unit | Lines | Role |
| :---- | :---- | :---- |
| 2.1 heading, status, chosen options, D-1, D-2 | 205–344 | D-2 (C-02) selected; 205–224 context (C-06). D-1 (225–276, C-01) drained in r3 |
| 2.1 D-3 | 345–396 | C-03, drained in r3 |
| 2.1 D-4, D-5, scope, dependencies, evidence | 397–516 | D-4 (397–450, C-04) selected; D-5 (451–490, C-05) assessed in r3, no change; 491–516 context (C-06) |
| 2.2 | 517–588 | C-07, uncertain: the l.525 precedence scope |
| 2.3 | 589–672 | Supporting (C-12) |
| 2.4 | 673–753 | DELTA-002 (C-13) |
| 2.5 | 754–883 | DELTA-002 wording at l.854 (C-14) |
| 2.7 | 962–1047 | Supporting (C-16) |
| 2.8 | 1048–1145 | Decisions, limits and drainage table (C-17); 2026-11-01 amendment (C-18) |
| 2.9 | 1146–1229 | Supporting (C-20) |
| 2.10 | 1230–1332 | Supporting (C-21), especially l.1309–1321 |
| 2.15 | 1650–1868 | C-26 (R-1 to R-6), C-27 (disposition, history), C-28 (nonconforming items, scope, dependencies, evidence), read in r3 |
| 2.16 | 1869–1976 | C-29 (R-1, R-2), C-30 (R-3, scope, dependencies, evidence), read in r3 |

Not read: 2.6 (884–961) and 2.11 to 2.14 (1333–1649). They bear on HDE-EPIC041 history, the PF09 route and the HDE Phased Epics entry, not on PF14.

## 4. Change and disposition ledger

| Row | Change | Disposition for PF14 | Evidence |
| :---- | :---- | :---- | :---- |
| C-01 | 2.1 D-1: the production vendor override covers bg:resolve, showcompat and vendor-selecting conjunction | Actionable (r3): RL-18 in §22 | §22 states the SAFE rails and provider gate and routes policy to HDE-Governance and HDE-CLI-API-Vendor-Ref; PF14 nowhere mentions the override (a search of the baseline for `allow-prod-vendor`, `PROVIDER_PROD`, "vendor override" and `7.1.11` finds nothing). D-1's byte rules belong to HDE CLI/API/Vendor Ref §7.1.11 (T-02) |
| C-02 | 2.1 D-2: vendor route selection fails closed outside a terminal `v1` or `v2` | Actionable: RL-03, RL-04, RL-05 in §1.1 | D-2 names two PF14 §1.1 changes ("Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback" superseded; "infer runtime behavior from vendor API version path strings" added to). RL-04 is the consistency change that D-2's Decision and Basis require for line 222. D-2's other targets belong to other tasks or to H-05 and H-09 |
| C-03 | 2.1 D-3: `/api/compat/v1` is a dev/admin surface | Actionable (r3): RL-12 in §9.3 | §9.3 line 2275 gates only `APP_ENV=prod`. D-3's byte rules belong to HDE CLI/API/Vendor Ref §5.5 (T-02), and the allow-list to HDE Governance §4.1.4 (T-01). The §32.1A route inventory names the route without a gate rule and needs no change |
| C-04 | 2.1 D-4: evidence tools own their output root | Actionable: RL-07 (§27.3), RL-08 (§27.5) | D-4 "Canon superseded or added to" and "Drainage targets" name §27.3 and §27.5. Its HDE Schemas & Artifacts §6.2.1 and HDE Governance §4.1.8 shares belong to T-04 and T-01 |
| C-05 | 2.1 D-5: governed gate check rows carry closed tokens and repository-relative paths only | No change (r3). PF14 states no rule on row content | PF14 names the canonical check log `audit/gates/json_gate/canonical/json_gate_check_log.ndjson` in §16.8, §17.8, §18.5 and §37.9 and says nothing about what a check row may contain. The rule's owners are HDE Governance §2.0.10 and HDE Schemas & Artifacts §1.2 (ledger C-05, T-01 and T-04) |
| C-06 | 2.1 status, scope, dependencies, evidence | Supporting | Each decision is canon from publication and governs until drained (l.211). The implementing change, Candidate CRD Items List item 9, is open (l.506), so RL-03, RL-07, RL-08, RL-12 and RL-18 carry nonclaims. Item 9 itself is H-10 |
| C-07 | 2.2 R-1 precedence scope (l.525) | No change. PF14 states no requirement in that scope | As in r1: bounded searches for `docs/ephemeral`, `docs/pfcanon`, `plan_path`, planning records, `requirement_ids`, versioned PF file names, `prepush`, Build Notes versions and close-pack ordering. Hits at lines 37, 39, 164, 783, 4967 and 4998 concern storage or non-pinning, and conform to R-1 and R-2. PF14 says nothing on when the close pack is written, so R-3 needs no PF14 change |
| C-12 | 2.3 WU-PR-01: Adapter entry and pure module | Supporting for RL-01 and RL-02 | 2.3 "Requirement coverage" (§3.1 boundary; §3.2 I-1 purity) |
| C-13 | 2.4 WU-PR-02: loader removed with no shim; DELTA-002 recorded | Actionable: RL-01, RL-02 | 2.4 "Required canon drainage": §1.1 "the loader seam posture and remediation paragraph" describe `engine/charts/loader.py` as current reality |
| C-14 | 2.5 QA-10 triage: DELTA-002 confirmed (l.854) | Actionable: RL-01, RL-02. Its other items are not PF14's: DELTA-003 is H-03, the PF09 rows H-01, CCR-5 H-06, PF23 #19–#27 H-04 | 2.5 "Required canon drainage", DELTA-002 |
| C-16 | 2.7 QA-120 PASS | Supporting | Verdict PASS (l.962–1000) |
| C-17 | 2.8 close-pack writer ADR | Row 1, generator: already represented. Row 1, close-run API: CRD API already represented; the Epic API is RL-06 (with C-18). Row 2, CRD filename form: partly represented; RL-09 adds the conditional external QA RCA form. Row 2, v2 `key_outputs` minimum: already represented. The other decisions drain to other homes | Equivalence locations: §37.2 "Close-pack generator", line 5035; §1.6.3 line 919; §37.2 "CRD close-pack artifacts (canonical filenames)", line 5033; §37.3 lines 5130–5138 |
| C-18 | 2.8 amendment of 2026-11-01: Epic close-run family; Epic tracked-issue ID form | Epic close-run family: actionable, RL-06, and in r3 RL-11 (the regression list's Epic counterpart). Tracked-issue ID form: not PF14's share | PF14 has no tracked-issue content (search for `TI-`, "tracked issue", `ISSUE-EPIC`). The test of RL-11's requirement exists (§6) |
| C-20 | 2.9 CL-05: B-1 to B-4; CCR-5 bounded | Supporting for RL-06 and RL-11 | 2.9 B-4 row. CCR-5 is H-06 |
| C-21 | 2.10 HDE-EPIC041 closure | Closure evidence for C-12 to C-16; supporting for RL-01 and RL-02 | `CLOSE / CHANGE_CLOSED`, 2026-11-01T16:39Z; PF09 row-closure table (l.1309–1321) |
| C-26 | 2.15 R-1 to R-6: every Epic's QA runs the live compat test | Actionable (r3): RL-10 (§1.1), RL-13 to RL-17 (§17.10, §17.10.5, §19.1) | §1.1 line 257 made the live test depend on the Epic touching a production surface and let an explicit exemption discharge it; 2.15 "Relation to other canon" supersedes that dependency for R-1 to R-4's scopes. §17.10 and §19.1 assumed no user-bound BodyGraph rows in production and forbade the write that stored the two fixtures. R-2 to R-4's waiver form, naming and stage lines belong to HDE Governance §3.4, Change Process Guide §3.5.2.8, Glow QA Guide and Plan Templates (T-01, T-03, T-06, T-07); PF14 routes to them. 2.15 leaves CRDs undecided, so RL-10 speaks of Epics only |
| C-27 | 2.15 "HDE-EPIC041 disposition" | History, not PF14's | T-10 |
| C-28 | 2.15 known nonconforming items | Supporting. The SYN-A and SYN-B items are closed by 2.16 R-3; the environment-label guard is the Product Owner's | Read in full |
| C-29 | 2.16 R-1, R-2: GATE:CORE-DET evidence; retired entries | Actionable (r3): RL-19 (§37.7) and RL-02's added sentence | §37.7 lists the lower-case a3 marker as the two-run marker of CLI determinism, which R-1 excludes from GATE:CORE-DET evidence; RL-02 named the generator without its retirement. The other retired entries (`ci/jobs/*`, `fixtures/composite/*`, `audit/gates/determinism/abba_compare*.log`, upper-case `A3`) do not occur in PF14 (search). §9.3.1 requires `artifacts/compat/identity_hash.txt` only for conjunction compat closure, which 2.16 excludes; no change |
| C-30 | 2.16 R-3: SYN-A and SYN-B stored and registered | Supporting for RL-13 to RL-17 | Read in full |

Closure gate. Nothing drafted waits for an open Epic or CRD. HDE-EPIC041 is closed (2.10; the closure record). 2.1 is a set of Product Owner architecture decisions with no Epic or CRD, in effect from publication; its implementing change has no CRD identity yet, so its rules drain with nonclaims. 2.15 and 2.16 are Product Owner rules in effect from publication (ledger §2 status reading). 2.8 carries HDE-CRD-0002, whose HDE CRD Records status is `Closed`, and HDE-EPIC041.

Held, not drafted:

* H-03. DELTA-003 targets HDE State of the Repository §2.2 (PF31), which is not a target of this ledger, and 2.5 (l.855) calls it a candidate that is not adopted. It waits for the Product Owner to adopt the candidate and for a route to an eligible home for HDE State of the Repository.

## 5. Substantive changes and their basis

| ID | Change | Basis |
| :---- | :---- | :---- |
| RL-01 | §1.1 "BodyGraph and loader seam posture": the drift sentence about `engine/charts/loader.py` is replaced by the delivered boundary. The allocation rules that follow are unchanged | DELTA-002 (2.4, 2.5 l.854, 2.10 l.1309–1321); repository inspection (§6) |
| RL-02 | §1.1 remediation paragraph: replaced by the delivered caller posture, the generator's exit-2 limit and (r3) its retirement as GATE:CORE-DET evidence, the no-restore rule, the two guard tests, the unchanged contract limits, the log-label note and the PF09 nonclaim | DELTA-002; 2.4 C-1, I-1 to I-3; 2.10 FND-005; 2.16 R-2 (r3) |
| RL-03 | §1.1: new bullet stating the single permitted version classification, with a nonclaim | 2.1 D-2 |
| RL-04 | §1.1: v1 is retained legacy selection, not fallback | 2.1 D-2 |
| RL-05 | §1.1: the terminal-`v1` posture replaces the permission for every non-v2 base | 2.1 D-2 |
| RL-06 | §1.6.3: Epic close-run admission (`ADMITTED_EPIC_CLOSE`, HDE-EPIC041 only) and `publish_epic_close_run_family` | 2.8 drainage table row and note, decision 7, stated limits; 2.9 B-4 |
| RL-07 | §27.3: "Output-root ownership" rules for the attestation builder, with a nonclaim | 2.1 D-4 |
| RL-08 | §27.5: "Log-path bound" for `--log-path`, with a nonclaim | 2.1 D-4 |
| RL-09 | §37.2: the CRD form of the conditional external QA RCA | 2.8 drainage table row; decisions 3 and 4; stated limit |
| RL-10 | §1.1 "Production/user-surface open-rails proof posture": every Epic's QA plan includes and its run executes the live compat test (vendor showcompat under step-local open rails on synthetic data, plus the deployed-service check), whatever the Epic changed; an Epic touching production surfaces adds its own live test; only a recorded Product Owner waiver sets either aside; the R-1 list of what does not satisfy it, plus an agent's finding of non-applicability; a test that cannot run is `TOOLING_BLOCKED`; QA without it is closed-rails QA; pass predicates, waiver form, naming and stage enforcement routed to their owners | 2.15 R-1 to R-6 and "Relation to other canon" |
| RL-11 | §1.6.3 regression list: governed Epic close-run admission limited to `ADMITTED_EPIC_CLOSE`, with an unadmitted Epic or a CRD configuration refused by the Epic entrypoint, which names the admitted set | 2.8 amendment and stated limit; 2.9 B-4; repository inspection |
| RL-12 | §9.3: the compat namespace's dev/admin environment gate (404 for production-like posture; otherwise served only under `APP_ENV` exactly `dev`, `test` or `local`, else 403 `ERR_WRITER_FORBIDDEN`; `ENGINE_ENV` never admits; no credential while admitted that way; a later decision before wider exposure), routed to its byte and allow-list owners, with a nonclaim | 2.1 D-3 |
| RL-13 | §17.10 status: the scope condition excepts the two synthetic Live QA fixtures | 2.15 R-1; 2.16 R-3 |
| RL-14 | §17.10 assumptions: the two fixtures by name and UUID; permanent QA fixtures, not app users; stored only through the engine's write path under the Product Owner's write authorization, as Ops work; the deployed-service check reads only them and is `TOOLING_BLOCKED` while either is missing | 2.15 R-1, R-5, R-6; 2.16 R-3 |
| RL-15 | §17.10.5: the live compat test and its deployed-service check are not a requirement that the no-user mode blocks | 2.15 R-1 |
| RL-16 | §19.1 pre-Glow scope condition: excepts the two fixtures | 2.15 R-1; 2.16 R-3 |
| RL-17 | §19.1: the two pre-Glow prohibitions do not cover storing the fixtures, which is Ops work under the Product Owner's write authorization | 2.15 R-1, R-6; 2.16 R-3; the Part W run log (§6) |
| RL-18 | §22: the production vendor override for the three vendor-acquiring CLI paths, routed to HDE-CLI-API-Vendor-Ref §7.1.11, with a nonclaim | 2.1 D-1 |
| RL-19 | §37.7: the lower-case a3 marker is kept but is not GATE:CORE-DET evidence, and no record may cite it as current two-run identity proof; GATE:CORE-DET evidence is the CI owner tests and each live compat test run | 2.16 R-1, R-2; repository inspection |
| RL-20 to RL-25 | Formatting repair: `<...>` placeholders restored in §5.8 (`DEV_SAMPLER_URL`), §16 (narrative pack path), §37.2 (Epic close-pack filenames, path proofs, the "Where" sentence, acceptance scaffolds), §37.3 (the manifest path) and §37.18.1 (the epic-local snapshot path) | PF03 §7 "Revision and retention rules" and §8 "Structure and presentation"; Nathan's direction; the intended text in the owners named in each redline |

C-02 and DELTA-002 in §1.1. The spans are disjoint (UTF-8 byte offsets in the original): RL-01 [15061, 15936), RL-02 [15938, 16486), RL-03 gap at 22698, RL-04 [23833, 23999), RL-05 [24811, 25020). r3's RL-10 [30389, 31221) is also disjoint from them.

## 6. Current-repository claims and how each was checked

All checks are read-only, at `e2b7427` for r1 and r2 and at `origin/main` `84d6d1c` for r3. The clone is shallow (graft at `e72c9ba`), so no claim rests on file history.

| Claim in the redlines | Inspection |
| :---- | :---- |
| `adapter/chart_orchestration.py` and `engine/charts/pure.py` are tracked; `engine/charts/loader.py` is absent | `git ls-files engine/charts adapter/chart_orchestration.py` printed the two files only |
| `load_chart` raises `TypeError` for any other argument shape | `adapter/chart_orchestration.py` docstring and its three `raise TypeError` lines |
| The entry's log line uses the route string `loader.load_chart` | `adapter/chart_orchestration.py` line 105 |
| The generator imports the Adapter entry and exits 2 before its chart call | `scripts/make_compat_determinism_artifacts.py` lines 9, 18–19 and 25; `engine/compat/compute.py` contains no `compat_public` |
| The two guard tests exist | `tests/charts/test_chart_loader_import_guard.py`; `tests/charts/test_chart_pure_purity.py`. Their passing is not claimed |
| `ADMITTED_EPIC_CLOSE` admits `HDE-EPIC041` | `tools/evidence/update_evidence_index.py` lines 62–64 |
| `publish_epic_close_run_family` signature and behavior; an unadmitted configuration is refused with a message naming the admitted set | Same file, line 5568 onward (`"governed Epic close-run publication admits only " + ", ".join(sorted(ADMITTED_EPIC_CLOSE)) + f"; refused {refused}"`) |
| The Epic admission refusal is tested | `tests/evidence/test_evidence_index_missing_state.py`, `test_epic_close_run_publication_refuses_scope_and_restores_on_failure`, which asserts `"admits only HDE-EPIC041"` for `HDE-EPIC040` and for a CRD configuration. Its passing is not claimed |
| D-2 and D-4 are not implemented | `engine/bodygraph/vendor_client.py` `_configured_base_version` lines 102–109; item 9 open (2.1 l.506) |
| D-3 is not implemented: the compat handler refuses only the production-like posture | `engine/http/compat_handler.py` line 112 (`if _compute_env_mode(os.environ) == "prod": return compat_error_response(404)`); no other `APP_ENV` check in the file |
| D-1 is not implemented: only `bg:resolve --source vendor` accepts `--allow-prod-vendor` | `engine/cli/main.py` lines 52–59 (`"hdctl: --allow-prod-vendor is accepted only by bg:resolve --source vendor"`) |
| The fixtures were stored in production through the engine's own write path | `audit/ops/hde-epic041/postclose-ops01/run.log` lines 31–34 (`w_store_a` and `w_store_b`: `status=ok`, the two UUIDs, `rows_written=1`, `read_back_match=True`); `S_CLASSIFICATION_NOTE.txt` line 4 (`hdctl bg:resolve JSON`). RL-14 and RL-17 do not name the command |
| The a3 marker is tracked and still generated, so RL-19 does not call it frozen | `git ls-files artifacts/cards` lists `artifacts/cards/a3/IDENTITY_OK.txt` and its path proof. Its content reads `IDENTITY_OK` and "HDE-EPIC038 PR-02 deterministic predicate evidence only; no acceptance token satisfaction claimed." `tools/evidence/generate_determinism_gate_proofs.py` sets its path (line 30) and its content (line 75) among the outputs it builds; `tools/evidence/regenerate_identity_closure.py` lists it among the outputs of that generator's closure step (lines 90–96, 231–233); `tools/evidence/update_evidence_index.py` line 3027 indexes it as `epic038.pr02.a3_identity_ok` |

## 7. Constraints, interpretations and assumptions

* PF14 cites HDE Build Notes by title only, with no addendum number (PF03 §3 "Canonical ownership"). The redlines file and this log cite addendum numbers because they are working records, not PF text.
* Cross-references in new text use titles PF14 already uses ("HDE-CLI-API-Vendor-Ref", "HDE-Governance", "Glow QA Guide", "HDE-Build Notes") and no version numbers. Section numbers of other PF documents follow PF14's existing practice (for example "HDE-CLI-API-Vendor-Ref §5.2").
* Requirements stay requirements where implementation is missing (PF03 §3 "Claim-state separation"). RL-03, RL-07, RL-08, RL-12 and RL-18 state the rule and make no conformance claim.
* Historical records keep their wording (PF03 §2, on preserving historical and provenance text, and §3 "Claim-state separation"; r1 and r2 cited §9 here in error). The HDE-EPIC030 closure trace at line 5697, §17.9.1's informative observation "There are no persistent user-bound BodyGraphs in production" (line 3102, an earlier Build Notes observation), and §17.10's PR-01 discovery facts that name `compat_public` are not changed.
* r3 scope. Nathan's direction widens T-05 to the defects and inconsistencies this session reported. Under GTWPE-D3 these are contextual drainage of addenda the ledger routed to other documents; T-05 changes only PF14's own sections and routes the other documents' rules to their owners. No other task's file or row is touched.
* Formatting repair. PF03 §7 permits repair of escaping "when the complete source establishes the intended text". PF03 §8 warrants a redline when the source-real defect "changes meaning, placement, authority, scope, identity, safety, or claim posture", and bars a cleanup redline "solely for a rendered escape, wrapper, line-wrap difference, or illustrative syntax issue". RL-20 to RL-25 restore placeholders lost from canonical paths and a definition. Lost placeholders in examples and command shapes, and rendered escapes whose meaning is intact, are left (§10). TW-DRAIN-10 requires Nathan's authorization for hygiene; his direction gives it.
* In RL-20, the adjacent `\\=` escape on the same line is also repaired to `=`, because the line is already changed; the same cosmetic escape elsewhere is left.
* RL-21 uses `<PACK_MEMBER>`, the form of HDE Narratives Guide (the narratives owner) and HDE Schemas & Artifacts. HDE Architecture line 1056 writes `<OBJECT_KEY>` for the same segment; that difference is outside PF14 (§10).
* Change types are report labels only (NEW_CANON, CANON_UPDATE, CONSISTENCY, DOC_HYGIENE).

## 8. Producer validation

Two independent passes, both against the unchanged original, with scripts kept outside the repository.

1. Batch validation and one-pass simulation from the edit specification: each literal's exact count in the whole original (OLD 1 for each `REPLACE`; BEFORE 1, AFTER 1 and BEFORE+AFTER 1 for each `INSERT`); the heading chain at each span or gap; a pairwise check for overlapping spans, shared gaps and gaps at or inside a replaced span (none); one-pass application by original offset; after application, each NEW or INSERT text present exactly once and each OLD text absent; no ellipsis in any payload. Result: PASS, no conflicts.
2. Re-parse of the saved redlines file without the specification: every literal extracted by the stated fence convention, its byte length, SHA-256 and final-LF flag checked against the values printed beside it, every count and the overlap check repeated, and the batch applied in one pass. Result: PASS, twenty-five items, and a revised text byte-identical to pass 1. Compared with r2: RL-01 and RL-03 to RL-09 are identical; RL-02 differs only in NEW.

| ID | Op | Count (expected 1) | Original lines | UTF-8 span or gap | Section, by heading chain |
| :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE` | OLD 1 | 179 | [15061, 15936) | §1 > §1.1 |
| RL-02 | `REPLACE` | OLD 1 | 181 | [15938, 16486) | §1 > §1.1 |
| RL-03 | `INSERT` | gap 1 (BEFORE 1, AFTER 1) | after 214 | 22698 | §1 > §1.1 |
| RL-04 | `REPLACE` | OLD 1 | 222 | [23833, 23999) | §1 > §1.1 |
| RL-05 | `REPLACE` | OLD 1 | 226 | [24811, 25020) | §1 > §1.1 |
| RL-06 | `REPLACE` | OLD 1 | 919 | [105086, 105188) | §1 > §1.6 > §1.6.3 |
| RL-07 | `INSERT` | gap 1 | after 4443 | 388603 | §27 > §27.3 |
| RL-08 | `INSERT` | gap 1 | after 4489 | 392984 | §27 > §27.5, before the nested heading at line 4490 |
| RL-09 | `INSERT` | gap 1 | inside 5033 | 431037 | §37 > §37.2 |
| RL-10 | `REPLACE` | OLD 1 | 257 | [30389, 31221) | §1 > §1.1 |
| RL-11 | `INSERT` | gap 1 | inside 1160 | 127750 | §1 > §1.6 > §1.6.3 |
| RL-12 | `REPLACE` | OLD 1 | 2275 | [223504, 223583) | §9 > §9.3 |
| RL-13 | `REPLACE` | OLD 1 | 3166 | [295199, 295309) | §17 > §17.10 |
| RL-14 | `REPLACE` | OLD 1 | 3171 | [295638, 295698) | §17 > §17.10 |
| RL-15 | `INSERT` | gap 1 | inside 3407 (its end) | 315375 | §17 > §17.10 > §17.10.5 |
| RL-16 | `INSERT` | gap 1 | inside 3693 | 338282 | §19 > §19.1 |
| RL-17 | `INSERT` | gap 1 | after 3695 | 338575 | §19 > §19.1 |
| RL-18 | `INSERT` | gap 1 | after 4090 | 368252 | §22 |
| RL-19 | `REPLACE` | OLD 1 | 7078–7080 | [622454, 622508) | §37 > §37.7 |
| RL-20 | `REPLACE` | OLD 1 | 1743 | [177012, 177059) | §5 > §5.8 |
| RL-21 | `REPLACE` | OLD 1 | 2908 | [272423, 272469) | §16 |
| RL-22 | `REPLACE` | OLD 1 | 5016–5031 | [429841, 430485) | §37 > §37.2 |
| RL-23 | `REPLACE` | OLD 1 | 5071–5072 | [436804, 436890) | §37 > §37.2 |
| RL-24 | `REPLACE` | OLD 1 | 5127 | [441013, 441069) | §37 > §37.3 |
| RL-25 | `REPLACE` | OLD 1 | 7538 | [655360, 655431) | §37 > §37.18 > §37.18.1 |

Simulated revision (body edits only; the header is left to TW-APPLY-10): 679,576 bytes, SHA-256 `4442694b4b664cd807940fafe67c6845ab073efff77ece88b335cd6bc9b1cd15`, 7,750 LF characters, still without a final LF.

## 9. Save verification

* The output directory `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/` holds only this run's files. r3 replaces the r2 redlines file and this proof log under the same names, which the run owns; r2 stays in commit `ea4c6cf`.
* The redlines file was saved, read back in full and re-parsed (§8, pass 2). Its identity is in §1.
* This proof log was saved and read back in full before the package was reported READY. A log cannot carry its own hash; the final response and the commit give its identity.

## 10. Unresolved items, limits and observations

* None blocks this package.
* Double-backslash sequences left as they are, by line of the original:
  * Rendered escapes with intact meaning (PF03 §8, no cleanup redline): `\\=` and `\\==` (lines 50, 51, 101, 1263, 1391–1395, 1456–1460, 1825, 2145, 2154, 2222, 2362, 2371, 2380, 2470, 2533, 2537, 2563, 2579–2581, 2719, 2785, 2824, 2843, 2895, 2907, 4139, 4222, 4253, 4579, 4592, 4679, 5204, 5205); `\\n`, which renders as the intended `\n` (407, 1550, 2943, 3743, 4783, 4791, 5116); `\\\<=` (2627); `\\b`, a regex word boundary (3628).
  * Lost placeholders in examples, call shapes and command shapes, whose meaning is intact and whose intended placeholder is not established (PF03 §8, illustrative syntax): 787 (`python -m pytest`), 1560 and 2044 (`json.dumps`, `jsonify`), 1732 and 1741 (example host and port), 2586 (`viewer_prefs{}`), 2810 (§14.5, an informative example), 2936 and 2937 (`hdctl showcompat`, `hdctl sample`), 3803 (example vendor URL), 3878 (the legacy flat layout).
  * 825, "(no \\ placeholders)": the sense, no angle-bracket placeholders in copy/paste-ready commands, survives; the intended wording is not established.
  * Not repairable: 7488, §37.17 "Snapshot root", `audit/gates/arch/*arch/\\*\\/\\`. Three segments are lost, and no canon on `main` or tracked path under `audit/gates/arch/` establishes the intended path. Repairing it needs the intended text from Nathan or the section's owner.
* Observation outside PF14: HDE Architecture line 1056 names the narrative pack path `/narratives/<pack_sha>/<OBJECT_KEY>`, and HDE Narratives Guide line 845 and HDE Schemas & Artifacts line 1992 name `/narratives/<pack_sha>/<PACK_MEMBER>`.
* Discrepancy for Nathan, not a blocker. 2.16 "The facts that prompted it" calls `artifacts/cards/a3/IDENTITY_OK.txt` "a frozen marker last changed by HDE-EPIC024 (2026-01-22)". On `main` its content names HDE-EPIC038 PR-02, and `tools/evidence/generate_determinism_gate_proofs.py` still writes it as a step of the release identity closure (§6). 2.16's rules do not depend on that fact: R-1 defines GATE:CORE-DET evidence without it, and R-2 keeps the marker as it is. RL-19 therefore states the rule and drops the word "frozen". The shallow clone cannot show when the file last changed. Whether 2.16's fact needs a correction, and whether the determinism proof generator is itself GATE:CORE-DET evidence, are Nathan's questions.
* Checked before the r3 push, after rebasing onto the shared branch at `224d9f0`: the Product Owner's CCR-5 ruling of 2026-11-02, recorded by the T-06 and T-07 sessions ("close pack should go after the decision to close is confirmed"). PF14 states no ordering of the close pack against the closure decision. A search of the baseline finds only the records-only HDE-EPIC027 step at line 5296 and the chronology rule at line 7532. The ruling therefore needs no PF14 change.
* The handoff's "7,734 lines" is the LF count. The file has 7,735 lines because the last has no line ending.

## 11. Next step

READY / COMPLETE_PACKAGE. Nathan's handoff authorizes TW-APPLY-10 100926.1 in this session, fetched live from Notion when that step begins. Its inputs: this original, the redlines file and this proof log; the same ledger rows, plus the rows r3 drains (C-01, C-03, C-26, C-29, C-30); branch `claude/gtwpe-triage-authoring-j94ewf` (draft PR amthorn78/glow-hdengine-v2#826, open); the final file under the name TW-APPLY-10 derives (expected `PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md`, replacing r2's application) with its `.proof-log` beside it; and, if needed, the diagnostic `PF14-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`, all in this directory.

## 12. Revision r2

* What changed. RL-09 was added. RL-01 to RL-08 are unchanged, byte for byte.
* Why. After the r1 package was pushed (`9de402f`), the shared branch showed that the T-04 and T-06 document sessions had revised their own packages to apply GTWPE-D3 within their assigned rows. This session rechecked its own equivalence claims the same way. r1 had recorded C-17's "CRD filename form" row as already represented by §37.2 line 5033. That was only partly true: 2.8 decision 4 and its stated limit bind a CRD's external QA RCA to the close report's own prefix, and the paragraph omits it.
* Other rows rechecked, no further change: C-02, C-04, C-13, C-14, C-18, C-07.
* Lineage. r1 was applied once in a local, unpushed commit, discarded before r2. No output of r1 exists on the branch.

## 13. Revision r3

* Direction. Nathan, 2026-11-02, after the r2 application report: "I want you to fix the defects and inconsistencies you noticed". The r2 report and r2 §10 had listed: PF14 text that conflicts with addenda 2.15, 2.16 and 2.1 D-1, D-3 and D-5, which the ledger routed to other documents; the rendered-escape damage to placeholders; §9.3's compat gate against D-3; and the §1.6.3 regression list naming only the CRD refusal.
* What changed. RL-10 to RL-25 were added, and RL-02's NEW gained one sentence (2.16 R-2). RL-01 and RL-03 to RL-09 are unchanged, byte for byte.
* Dispositions. 2.15 and 2.16: RL-10, RL-13 to RL-17, RL-19, RL-02. D-3: RL-12. D-1: RL-18. D-5: no change (§4, C-05). §1.6.3: RL-11. Placeholders: RL-20 to RL-25, with every other `\\` sequence accounted for in §10.
* Reading added for r3: 2.1 D-3 in full; 2.15 and 2.16 in full; 2.1 D-1 and D-5 again; the supporting canon and repository inspections in §2 and §6; TW-DRAIN-10, fetched again.
* Lineage. r2 was applied as `apply-r2` (commit `6eb135d`), producing `PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md`. That file was never published to `docs/pfcanon/`. Applying r3 replaces it under the same name, and its proof log records the lineage.
* Validation. Both passes in §8 were run on r3 and pass.
