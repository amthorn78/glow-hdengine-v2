# Proof log: PF14 redlines, run gtwpe-20261101-pf10-v14-0-5 (T-05)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.md` (27,268 bytes; SHA-256 `68f6083df1e1134fce4bfb7c29ffd010dd9dcec6f3a1dffb4c8a55d231150d21`) |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-05/prep-r1` |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live when the step began (page state 2026-10-09T11:05:22Z) |
| Authorized sequence | Nathan's handoff authorizes TW-DRAIN-10, then TW-APPLY-10 100926.1 (page `3f44590a05eb81eebff6e3afa3d9aa5b`) in this one session, after a READY / COMPLETE_PACKAGE result |
| Preparer | The T-05 document session Nathan started, Claude Code session `https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z`. No subagent, reviewer or other session was used |
| Prepared | 2026-11-02, redlines saved about 00:30Z |
| Preparation outcome | `READY` |
| Save state | `COMPLETE_PACKAGE`: both files saved and read back in full (§9) |
| Correction route | An Apply diagnostic returns to TW-DRAIN-10 in this session, which issues a corrected package under a new run identity (`prep-r2`) |

## 2. Sources and inputs

| Role | Identity | Coverage |
| :---- | :---- | :---- |
| Target, original | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md` at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56`. Title `PF14-Canon-HDE-Mechanics-Guide`, v3.5.9, Status Canon, Effective date 2026-10-26, Last Update Gate `BN 13.8.8`. Git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`; 669,363 bytes; SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59`; 7,734 LF characters; 7,735 lines, the last (`* presence and correctness of path-proofs`) without a trailing LF | Complete. §3 gives the windows |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` at `e2b7427`. HDE Build Notes v14.0.5. Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines | The selected units, complete (§3) |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` at `e2b7427`, v1.8.8, 43,953 bytes, SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462` | Complete, lines 1–633 |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064` (22,735 bytes) | Complete. Planning and provenance only, not a change source |
| Currency check | `git diff --stat e2b7427 origin/main -- docs/pfcanon/` was empty when read (`origin/main` `84d6d1c`). Code paths cited below are also unchanged between the two commits | Read-only |
| Supporting canon | HDE CLI/API/Vendor Ref (`PF05-Canon-HDE-CLI-API-Vendor-Ref-v2.5.4.md`) §7.1.10 "Endpoint policy (explicit version-gated dual lineage)" in full; HDE Architecture (`PF02-Canon-HDE-Architecture-v2.4.7.md`) §1.1 paragraph "Non-BodyGraph chart loader classification"; HDE CRD Records (`PF30.1-Canon-HDE-CRD-Records-v0.9.2.md`), the HDE-CRD-0002 record's status line (`Closed`, line 466) | Supporting reading only; not drained |
| Closure evidence | `docs/ephemeral/HDE-EPIC041-CL-E-10-closure-decision-v1.0.md`, blob `5075f5ea5a2e60e0987ce427df4c4c5b796f662b`: `closure_state: CHANGE_CLOSED`, `outcome: CLOSE / CHANGE_CLOSED` (lines 11, 40, 45) | Read at the cited lines |

Source roles. HDE Build Notes v14.0.5 is the only change source. PF14 is the target. Canon was read from `docs/pfcanon/` on `main`. The approved HDE-EPIC041 Specification was not read: no selected row drains it, and the ledger queues no Specification edit (ledger §6).

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

One PF14 window (7337–7735) and two HDE Build Notes windows (552–753 and 1048–1145) first came back as tool-truncated previews. Each was re-read in narrower windows, the ones recorded here; no claim relies on a preview. Where a long line was first printed cut at a fixed width, its remainder was printed and read.

HDE Build Notes v14.0.5, selected units, each read completely:

| Unit | Lines | Bytes | Role |
| :---- | :---- | ----: | :---- |
| 2.1 heading, status, chosen options, D-1, D-2 | 205–344 | 13,633 | D-2 (C-02) selected; 205–224 context (C-06). D-1 (225–276) fell inside the window and was read, not drained |
| 2.1 D-4, D-5, scope, dependencies, evidence | 397–551 (part) | 13,415 for 397–551 | D-4 (397–450, C-04) selected; 491–516 context (C-06). D-5 (451–490) read, not drained |
| 2.2 status, R-1 to R-3 | 517–551 | (within 397–551) | C-07, uncertain: the l.525 precedence scope |
| 2.2 remainder | 552–588 | 6,048 | Context for C-07 |
| 2.3 | 589–672 | 24,841 | Supporting (C-12) |
| 2.4 | 673–753 | 28,955 | DELTA-002 (C-13) |
| 2.5 | 754–883 | 20,868 | DELTA-002 wording at l.854 (C-14) |
| 2.7 | 962–1047 | 33,156 | Supporting (C-16) |
| 2.8 | 1048–1145 | 36,158 | Decisions, limits and drainage table (C-17); 2026-11-01 amendment (C-18) |
| 2.9 | 1146–1229 | 26,466 | Supporting (C-20) |
| 2.10 | 1230–1332 | 36,129 | Supporting (C-21), especially l.1309–1321 |

Not read: 2.1 D-3 (345–396), 2.6 (884–961) and 2.11 to 2.16 (1333–1976). They are not selected for T-05 and not needed as dependencies.

## 4. Change and disposition ledger

| Row | Change | Disposition for PF14 | Evidence |
| :---- | :---- | :---- | :---- |
| C-02 | 2.1 D-2: vendor route selection fails closed outside a terminal `v1` or `v2` | Actionable: RL-03, RL-04, RL-05 in §1.1 | D-2 names two PF14 §1.1 changes ("Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback" superseded; "infer runtime behavior from vendor API version path strings" added to). RL-04 is the consistency change that D-2's Decision and Basis require for line 222. D-2's other targets (HDE Users Guide, HDE CLI/API/Vendor Ref §7.1.10 and §7.2.0, Plan Templates, AGENTS.md) belong to other tasks or to H-05 and H-09 |
| C-04 | 2.1 D-4: evidence tools own their output root | Actionable: RL-07 (§27.3), RL-08 (§27.5) | D-4 "Canon superseded or added to" and "Drainage targets" name §27.3 and §27.5. Its HDE Schemas & Artifacts §6.2.1 and HDE Governance §4.1.8 shares belong to T-04 and T-01 |
| C-06 | 2.1 status, scope, dependencies, evidence | Supporting | Each decision is canon from publication and governs until drained (l.211). The implementing change, Candidate CRD Items List item 9, is open (l.506), so RL-03, RL-07 and RL-08 carry a nonclaim. Item 9 itself is H-10 |
| C-07 | 2.2 R-1 precedence scope (l.525): where HDE Mechanics Guide requires a close pack, tool, test or record to read or bind a planning document, or to name a PF document by file name or version, 2.2 supersedes that requirement | No change. PF14 states no requirement in that scope | Complete read, plus bounded searches of the baseline for `docs/ephemeral`, `docs/pfcanon`, `plan_path`, planning records, `requirement_ids`, versioned PF file names, `prepush`, Build Notes versions and close-pack ordering. Hits: lines 37 and 39 (where canon and change-process documents are read and stored; 2.2 excludes storage), 164 and 783 (non-pinning of file names), 4967 and 4998 (storage of new process documents). The step-log contract's `pf_refs` (§1.6.3 table) requires exact PF titles only, and §37.2's QA closeout summary refers to "a PF10 addendum" with no file name or version; both conform to R-1 and R-2. PF14 says nothing on when the close pack is written, so R-3 (drained to Plan Templates by T-07) needs no PF14 change |
| C-12 | 2.3 WU-PR-01: Adapter entry and pure module | Supporting for RL-01 and RL-02 | 2.3 "Requirement coverage" (§3.1 boundary; §3.2 I-1 purity) |
| C-13 | 2.4 WU-PR-02: loader removed with no shim; DELTA-002 recorded | Actionable: RL-01, RL-02 | 2.4 "Required canon drainage": §1.1 "the loader seam posture and remediation paragraph" describe `engine/charts/loader.py` as current reality |
| C-14 | 2.5 QA-10 triage: DELTA-002 confirmed (l.854) | Actionable: RL-01, RL-02 (DELTA-002 wording). Its other items are not PF14's: DELTA-003 is H-03, the PF09 rows H-01, CCR-5 H-06, PF23 #19–#27 H-04 | 2.5 "Required canon drainage", DELTA-002: replace the drift sentence with the delivered boundary |
| C-16 | 2.7 QA-120 PASS | Supporting | Verdict PASS (l.962–1000); DELTA-002 drains after all QA tasks and is never a close blocker ("Required canon drainage") |
| C-17 | 2.8 close-pack writer ADR, decisions 1–9, stated limits, drainage table | Row 1, generator: already represented. Row 1, close-run API: CRD API already represented; the Epic API is RL-06 (with C-18). Row 2, CRD filename form: already represented. Row 2, v2 `key_outputs` minimum: already represented. Decisions 1–6, 8 and 9 and the other limits drain to other homes | Equivalence locations: §37.2 "Close-pack generator (mechanics; single-writer; normative)", line 5035 ("For a `close_candidate_source.v2` source, Epic or CRD, the generic close-pack generator is `tools/qa/generate_epic_close_pack.py`", with its single `--source`, `--write`/`--check`, tracked-input and manifest-last rules, beside the EPIC-025 entrypoint); §1.6.3 line 919 (`publish_crd_close_run_family(...)`, family membership, Index key form); §37.2 "CRD close-pack artifacts (canonical filenames)", line 5033; §37.3 lines 5130–5138 (the five-key v2 minimum and `OUTPUT_BINDING_MISMATCH`). The table routes the other decisions to Change Process Guide, HDE Schemas & Artifacts, Glow QA Guide and HDE Governance |
| C-18 | 2.8 amendment of 2026-11-01: Epic close-run family; Epic tracked-issue ID form | Epic close-run family: actionable, RL-06. Epic tracked-issue ID form: not PF14's share | The amendment lists two canon consequences (l.1127). PF14 has no tracked-issue content: a bounded search for `TI-`, "tracked issue", `ISSUE-EPIC` and `close_candidate_source` finds only §1.6.3 and §37.2/§37.3 text unrelated to tracked issues. The ID form is a schema and close-pack-content rule, routed by PF14 to HDE-Schemas & Artifacts, and owned for close PR content by Change Process Guide §3.5.2.1 form (b) and Plan Templates "Tracked Issues". B-2 (pointer rule) and B-3 (Epic Index rows) are not among the listed consequences, and PF14 has no pointer or close-pack-row rule that they contradict |
| C-20 | 2.9 CL-05: B-1 to B-4; CCR-5 bounded | Supporting for RL-06 | 2.9 B-4 row (`publish_epic_close_run_family` and Epic close-run discovery). CCR-5 is H-06 and not PF14's |
| C-21 | 2.10 HDE-EPIC041 closure | Closure evidence for C-12 to C-16; supporting for RL-01 and RL-02 | `CLOSE / CHANGE_CLOSED`, 2026-11-01T16:39Z. PF09 row-closure table (l.1309–1321): DELTA-002, "No status change recommended (text drain only)", "Supportable from repo evidence", "after a separate canon-only drain step". PSR-001 to PSR-003 |

Closure gate. Nothing in the selected scope waits for an open Epic or CRD. HDE-EPIC041 is closed (2.10; the closure record). 2.1 is a Product Owner decision with no Epic or CRD, in effect from publication. 2.8 carries HDE-CRD-0002, whose HDE CRD Records status is `Closed`, and HDE-EPIC041.

Held, not drafted:

* H-03. DELTA-003 targets HDE State of the Repository §2.2 (PF31), which is not a target of this ledger, and 2.5 (l.855) calls it a candidate that is not adopted. It waits for the Product Owner to adopt the candidate and for a route to an eligible home for HDE State of the Repository.

## 5. Substantive changes and their basis

| ID | Change | Basis |
| :---- | :---- | :---- |
| RL-01 | §1.1 "BodyGraph and loader seam posture": the drift sentence about `engine/charts/loader.py` is replaced by the delivered boundary (Adapter entry `adapter/chart_orchestration.py::load_chart`, pure module `engine/charts/pure.py`, loader removed with no shim, legacy signature retired). The allocation rules that follow are unchanged | DELTA-002 (2.4, 2.5 l.854, 2.10 l.1309–1321); repository inspection (§6) |
| RL-02 | §1.1 remediation paragraph: the pre-delivery remediation instruction and its "not a claim that removal has occurred" are replaced by the delivered caller posture, the generator's retained exit-2 limit, the no-restore rule, the two guard tests, the unchanged contract limits, the log-label note and the PF09 nonclaim | DELTA-002 (2.4 covers "the remediation paragraph"); 2.4 C-1, I-1 to I-3, the import guard; 2.10 FND-005; repository inspection |
| RL-03 | §1.1 request-shaping list: new bullet stating the single permitted version classification, its scope and the prohibitions that still govern, with a nonclaim | 2.1 D-2 Decision and "Canon superseded or added to" |
| RL-04 | §1.1: "until the homes decide whether v1 remains a fallback" becomes "retained legacy selection, not fallback"; retirement still needs the separately versioned decision | 2.1 D-2 Decision, Basis and "Left undecided"; HDE CLI/API/Vendor Ref §7.1.10 "Legacy and claim boundary" agrees |
| RL-05 | §1.1: the permission for every non-v2 base is replaced by the terminal-`v1` posture, the refusal of every other base by routing to HDE CLI/API/Vendor Ref §7.1.10, and the meaning of the `explicit_legacy_fallback` label | 2.1 D-2 "Canon superseded or added to", "No fallback", "Classification label" |
| RL-06 | §1.6.3: "No Epic close-run family is admitted." becomes a new bullet for Epic close-run admission (`ADMITTED_EPIC_CLOSE`, HDE-EPIC041 only) and `publish_epic_close_run_family` | 2.8 drainage table row and note, decision 7, stated limits; 2.9 B-4; repository inspection |
| RL-07 | §27.3: new "Output-root ownership" rules for the attestation builder (exclusive claim, no writes through symlinks, scoped cleanup), with the unchanged interface and a nonclaim | 2.1 D-4 builder decision |
| RL-08 | §27.5: new "Log-path bound" for `tools/evidence/run_sanity_pipeline.py --log-path`, with a nonclaim | 2.1 D-4 sanity-pipeline decision |

C-02 and DELTA-002 in §1.1. The uncertainty was resolved by proving the spans disjoint (UTF-8 byte offsets in the original): RL-01 [15061, 15936), RL-02 [15938, 16486), RL-03 gap at 22698, RL-04 [23833, 23999), RL-05 [24811, 25020). No two touch, and no gap lies at or inside a replaced span. Combining them was unnecessary.

## 6. Current-repository claims and how each was checked

All checks are read-only, on `e2b7427`, with code paths unchanged at `origin/main` `84d6d1c`.

| Claim in the redlines | Inspection |
| :---- | :---- |
| `adapter/chart_orchestration.py` and `engine/charts/pure.py` are tracked; `engine/charts/loader.py` is absent | `git ls-files engine/charts adapter/chart_orchestration.py` (as the handoff required) printed the two files only; `git ls-tree -r e2b7427 -- engine/charts` likewise |
| `load_chart` raises `TypeError` for any other argument shape; the legacy signature is retired | `adapter/chart_orchestration.py` docstring and the three `raise TypeError("Invalid arguments to load_chart")` lines |
| The entry's log line uses the route string `loader.load_chart` | `adapter/chart_orchestration.py` line 105 |
| The generator imports the Adapter entry and exits 2 before its chart call | `scripts/make_compat_determinism_artifacts.py` lines 9, 18–19 and 25; `engine/compat/compute.py` contains no `compat_public` (count 0) |
| The two guard tests exist and test what RL-02 says | `tests/charts/test_chart_loader_import_guard.py` (`test_no_tracked_python_file_imports_the_retired_loader`, `test_the_retired_module_path_does_not_exist`); `tests/charts/test_chart_pure_purity.py` (`test_pure_module_has_no_forbidden_dependency_or_call`, side-effect tests). Their passing is not claimed |
| `ADMITTED_EPIC_CLOSE` admits `HDE-EPIC041` with `audit/qa/hde-epic041` and `audit.qa.hde_epic041` | `tools/evidence/update_evidence_index.py` lines 62–64 |
| `publish_epic_close_run_family` signature and behavior | Same file, line 5568 onward: refuses an unadmitted Epic; requires a nonempty `CheckResult` family; renders through `qa_harness._primary_log_content` with the own-primary path moved to `close/`; requires the recorded manifest and primaries (`_epic_qa_family_snapshot`); writes no manifest or `checks/` file; refuses if the QA family or a primary changes; one `_WriteTransaction` |
| Membership and key form as for a CRD; rows carry `epic_id` | `_epic_close_run_entry` (line 4179) and `_epic_close_run_check_ids` (line 4211) |
| D-2 and D-4 are not yet implemented, so nonclaims are needed | `engine/bodygraph/vendor_client.py` `_configured_base_version` still lower-cases and searches any path segment (lines 102–109). Item 9 is open (2.1 l.506) |

## 7. Constraints, interpretations and assumptions

* PF14 cites HDE Build Notes by title only, with no addendum number (PF03 §3 "Canonical ownership"). The redlines file and this log cite addendum numbers because they are working records, not PF text.
* Cross-references in the new text use titles PF14 already uses in §1.1 ("HDE-CLI-API-Vendor-Ref", "HDE Architecture", "HDE-Build Notes") and no version numbers.
* Requirements stay requirements where implementation is missing (PF03 §3 "Claim-state separation"). RL-03, RL-07 and RL-08 state the canon rule and say they make no conformance claim.
* Historical records keep their wording (PF03 §9). The records-only HDE-EPIC030 closure trace at line 5697, which names `engine/charts/loader.py` as current-reality context at that review, is not changed.
* Redline format. TW-DRAIN-10's exact contract requires literal fenced payloads, so they are used even though PF03 §8 says paste text is unfenced by default; PF03 §8 and §15 defer to an operator-supplied format.
* Change types are report labels only (NEW_CANON, CANON_UPDATE, CONSISTENCY).
* `ADMITTED_EPIC_CLOSE` also admits an Epic's writer close-pack Index rows (2.8 decision 8). RL-06 describes only the close-run family, which is the consequence 2.8 lists for PF14.

## 8. Producer validation

Two independent passes, both against the unchanged original, with scripts kept outside the repository.

1. Batch validation and one-pass simulation from the edit specification: for each redline, the literal's exact count in the whole original (OLD 1 for each `REPLACE`; BEFORE 1, AFTER 1 and BEFORE+AFTER 1 for each `INSERT`); the containing heading chain at each span or gap; a pairwise check for overlapping spans, shared gaps and gaps at or inside a replaced span (none); one-pass application by original offset; after application, each NEW or INSERT text present exactly once and each OLD text absent; no ellipsis in any payload. Result: PASS.
2. Re-parse of the saved redlines file without the specification: every literal extracted by the stated fence convention, its byte length, SHA-256 and final-LF flag checked against the values printed beside it, every count and the overlap check repeated, and the batch applied in one pass. Result: PASS, eight items, and a revised text byte-identical to pass 1.

| ID | Op | Count (expected 1) | Original lines | Section, by heading chain |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE` | OLD 1 | 179 | §1.1 |
| RL-02 | `REPLACE` | OLD 1 | 181 | §1.1 |
| RL-03 | `INSERT` | gap 1 (BEFORE 1, AFTER 1) | after 214 | §1.1 |
| RL-04 | `REPLACE` | OLD 1 | 222 | §1.1 |
| RL-05 | `REPLACE` | OLD 1 | 226 | §1.1 |
| RL-06 | `REPLACE` | OLD 1 | 919 | §1.6 > §1.6.3 |
| RL-07 | `INSERT` | gap 1 (BEFORE 1, AFTER 1) | after 4443 | §27 > §27.3 |
| RL-08 | `INSERT` | gap 1 (BEFORE 1, AFTER 1) | after 4489 | §27 > §27.5. The gap lies immediately before the nested heading at line 4490, so the inserted text belongs to §27.5 itself |

Simulated revision (body edits only; the header is left to TW-APPLY-10): 674,486 bytes, SHA-256 `9418462d18b20c295d19e8a278bed2a8c7dc853cfc4424d0b2b69e2bf93d4fe7`, 7,748 LF characters, still without a final LF.

## 9. Save verification

* The output directory `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/` did not exist before this run, so no name collided.
* The redlines file was saved, read back in full and re-parsed (§8, pass 2). Its identity is in §1.
* This proof log was saved and read back in full before the package was reported READY. A log cannot carry its own hash; the final response and the commit give its identity.

## 10. Unresolved items, limits and observations

* None blocks this package.
* Observations outside the selected scope, not redlined:
  * Pre-existing rendered-escape damage in PF14 placeholders: for example §37.2's `audit/EPIC-\\\_close\_report.md` and "Where \\ is a zero-padded 3-digit epic number", §37.2's `audit/qa/hde-epic\\/token\_evidence\_matrix.md`, and §37.17's snapshot root. No selected source authorizes the repair. It is reported for Nathan.
  * §9.3 "Prod gate (hard)" for `/api/compat/v1` was not assessed against 2.1 D-3, because the ledger routes C-03 to T-02, T-01 and T-08, not to T-05.
  * §1.6.3 "Closed-rails regression responsibilities" names refusal of an unadmitted CRD only. No selected source states a matching Epic regression requirement for PF14, so none was added.
* The handoff's "7,734 lines" is the LF count. The file has 7,735 lines because the last has no line ending.
* Scope question for Nathan (not a blocker for this package). Before the first push, the shared branch carried a ledger correction dated 2026-11-02. It finds that the triage routed by named drain targets rather than by context and scope, contrary to GTWPE-D3 ("all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target"), and it adds tasks T-11 to T-18. It leaves T-05's row and selection unchanged, and the handoff limits drainage to its selected units. This package therefore drains only those units. PF14 also has text that, in context, bears on addenda outside T-05's selection. These anchors come from the full read of PF14. D-1 and D-5 were read inside the 2.1 windows but are not selected; D-3, 2.15 and 2.16 were not read. Whether each anchor needs a change is not assessed:
  * 2.15 (the ledger's C-26, "Every Epic's Live QA runs the live compat test"): §1.1 "Production/user-surface open-rails proof posture" (line 257), §17.10.1 (from line 3174) and §19.1 "Live vendor transport proofs" (line 3789).
  * 2.16 (the ledger's C-29, retired GATE:CORE-DET evidence): §37.7 "Two-run marker", `artifacts/cards/a3/IDENTITY_OK.txt` (line 7080); the ledger's §8 records that 2.16 R-2 retires `artifacts/cards/A3/IDENTITY_OK.txt`.
  * 2.1 D-3 (`POST /api/compat/v1` is a dev/admin surface): §9.3 "Prod gate (hard)" (line 2275) and the §32.1A route inventory.
  * 2.1 D-5 (gate check rows): §2.3 and §37.9, the canonical JSON gate logs.
  * 2.1 D-1 (production vendor override): the §1.1 HDAPI rails mechanics and §17.10.1's vendor-backed smoke.

  Widening T-05 to these is Nathan's decision. A later contextual pass on PF14 would need its own selection.

## 11. Next step

READY / COMPLETE_PACKAGE. Nathan's handoff authorizes TW-APPLY-10 100926.1 in this session, fetched live from Notion when that step begins. Its inputs: this original, the redlines file and this proof log; the same ledger rows and selected source boundaries; branch `claude/gtwpe-triage-authoring-j94ewf` (draft PR amthorn78/glow-hdengine-v2#826, open); the final file under the name TW-APPLY-10 derives (expected `PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md`) with its `.proof-log` beside it; and, if needed, the diagnostic `PF14-apply-diagnostic.gtwpe-20261101-pf10-v14-0-5.md`, all in this directory.
