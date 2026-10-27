# T-PF12 — preparation proof log for `redlines-PF12-from-v2.9.6.md`

This proof log documents how `redlines-PF12-from-v2.9.6.md` was prepared, what it is based on and what was verified. It is the processing report of TW-DRAIN-10 100926.1 for ledger task T-PF12. It claims no QA verdict, acceptance, canon adoption, PF publication or closure; the redlines change no file in `docs/pfcanon/`.

## 1. Identity

| Item | Value |
| :- | :- |
| Run | `gtwpe-20261026-pf10-v13-8-8/T-PF12`, preparation revision `P1` |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/redlines-PF12-from-v2.9.6.md`; 48,813 bytes; 579 LF-terminated lines; SHA-256 `1fa231e84222d61d080cf51de5539de5cb02c9c3e1efe50467a12ff44a8e0dee` |
| This proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/redlines-PF12-from-v2.9.6.proof-log.md` |
| Prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live on 2026-10-26 (page state 2026-10-09T11:05:22Z) |
| Handoff | Nathan's GTWPE 100926.1 T-PF12 handoff, which authorizes TW-DRAIN-10 then TW-APPLY-10 100926.1 in this one session, with no subagent and no reviewer |
| Originating preparer | TW-DRAIN-10 in the Nathan-started T-PF12 document session, Claude Code cloud session https://claude.ai/code/session_01AaKkpYtrGxYudeyWaEnMX3 |
| Preparation outcome | `READY` |
| Save completeness | recorded in §11 after both files were read back |
| Destination | branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, shared draft PR https://github.com/amthorn78/glow-hdengine-v2/pull/761. The ledger PR #760 had merged (2026-10-26T21:18:51Z); the continuation branch and #761 already existed (created by the T-PF07 session), so this session reused them and created neither |

## 2. Target and baseline

| Item | Value |
| :- | :- |
| Path | `docs/pfcanon/PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md`, read from `origin/main` |
| Title, version, status | `PF12-Canon-HDE-Schemas-and-Artifacts`, v2.9.6, Canon; effective date 2026-10-09 |
| Commits | handoff baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a`; `origin/main` at start `0838ba08254eaefc888019df49a06aa2ae99cc6c` (#760's merge). The PF12 blob is identical at both; `main` carries no newer PF12 version |
| Git blob | `1542a8f78846fcdd684f6a4dec7b663616ec8c02` (`git hash-object` of the extracted bytes) |
| Size and lines | 622,934 bytes (`wc -c`); 6,096 LF terminators (`wc -l`); the file ends `LF LF`, so its last line is empty; no CR bytes |
| SHA-256 | `5bf86058e30c4cfd7dbaa9532b169d9a9b0e3d64089abc254a75bbf162a2227d` |
| Longest line | 3,146 bytes (line 3514); ten lines exceed 1,500 bytes, so the target was read by byte-bounded line windows, not by a line-truncating reader |

## 3. Coverage

The whole target was read, in 27 contiguous windows of at most 24,000 bytes, each cut at a line boundary. Each window's SHA-256 was recorded when it was planned and recomputed from the bytes actually printed for reading; all 27 match. The concatenation of the 27 windows equals the 622,934 baseline bytes exactly.

| Window | Lines | Bytes | SHA-256 |
| :- | :- | -: | :- |
| 1 | 1–280 | 23,887 | `bb36649ad62c3f227b8591670f9fa212b12e620b8db7882c01d70a87cc07a790` |
| 2 | 281–627 | 23,948 | `0c02f1941cca315d8869b738dd4baef4f8759a68f7df79f250fd915bf0b6d326` |
| 3 | 628–798 | 23,625 | `3692641438dce2eda96d6d5fe54fbe27b1da92e0fa642d75fd20dacfe1e91320` |
| 4 | 799–1047 | 23,851 | `97737c6c5a39a5b9bce2b817e6fe8f0da9660ad2e7a0df05f2371552700413e6` |
| 5 | 1048–1241 | 23,875 | `4edb5862812799460b6874fdfad4f79352945571aa816295a19b9829b142a27b` |
| 6 | 1242–1510 | 23,998 | `daa9848b3c2cea4afca94f182e106a812f7a0da36b5556dce22c04396861543f` |
| 7 | 1511–1781 | 23,975 | `6c54713a11cf3ea9f5b613c3837d80953c49854565ba530dd89c82fd7a245f78` |
| 8 | 1782–2097 | 23,975 | `671b0f48dfde2207989b09748b64424f624eb56b85835439834fc8dfc9e23111` |
| 9 | 2098–2382 | 23,930 | `7dd1b64eea261c69f7f6b9343273036a16da86ae664680d9e9744cc985819bfe` |
| 10 | 2383–2801 | 23,739 | `71822405e77363713e59f3ebf4036c20085816d74833d00f39c1a55c15fd2732` |
| 11 | 2802–3065 | 23,753 | `a35d1e9441778338a693574709c2ccf2560c5b7f40a602f961b0e3596f4bf555` |
| 12 | 3066–3218 | 23,027 | `c4e24bccd9525125027ebdd84c326cc1ea5ca9d884c671eca22d973bb1643726` |
| 13 | 3219–3422 | 23,903 | `02edd84a1c2851422384c6a4e23eac7104ae1bac25d9ed51c74c55b397b70dff` |
| 14 | 3423–3530 | 23,956 | `9bb2f8285317f9678893f9901997e06ddae0793ba36e15d345b253448f856523` |
| 15 | 3531–3713 | 23,389 | `c4bab94185a348325db8ca7929274bdcb2eaffec1b81879c64776365af863cae` |
| 16 | 3714–3852 | 23,818 | `5fc8242ba5299921f2075c26ecabd73218578cff800673590e04d1ff2ffc83c7` |
| 17 | 3853–4043 | 23,830 | `ad88324867c2e47096ba73d846238a88e3cfc522fd0f2111ccfea8a30bc3fc8f` |
| 18 | 4044–4150 | 23,857 | `7d73e369a73eae5c1e6af1fb999505c256fe9776814e9bc0859f265811b40ece` |
| 19 | 4151–4250 | 22,067 | `a888f2e931a6713328f548602a88fe8ab6533db5aa33c5a59d40025d74cf4bda` |
| 20 | 4251–4342 | 23,874 | `c65bf36aa320c30eabd48e2697e2dffbd1a0875449bf6627dd87a1bd8bd7ad2d` |
| 21 | 4343–4444 | 23,928 | `66d421d03454564969b19db784ada380c1e9785a60974fb5eb0d7f4c75c5642a` |
| 22 | 4445–4641 | 23,917 | `85edf1e0ec9a6fd25d0553691ceb61076f1bffd54c77e7bd478610a7f0ac9208` |
| 23 | 4642–4911 | 23,838 | `33b31873001794ab11b2def73c9744d36698d2b87627b8d830fab0f0ae0561f2` |
| 24 | 4912–5230 | 23,989 | `b96b25257d52555539dc5dc04208f110cf8714ace3c2edfaf46879ebb6b2f157` |
| 25 | 5231–5607 | 23,979 | `e62b4f3eb4549def0a5eb2adc5cb8df02f65be427c967745098584bea075748f` |
| 26 | 5608–6025 | 23,805 | `323a9e3661da89b67aea3e044b63b7fef10bcd74b8b4471e8ebb60a808940dc6` |
| 27 | 6026–6096 | 5,201 | `9efa84594c367ddb2b445ef84a3aa2a1c34b0365ebde88e8605db026ed2dfe3e` |

A term sweep of the whole target then located every passage on the assigned topics: `PF30` (11 lines), `CRD` (20), `crd_id` (4), `key_outputs` (20), `ENDPOINTS_CATALOG` (18), `alias` (28), `mutual` (3); no occurrence of `public_aux`, `canon-retired`, `close_candidate`, `generate_epic_close_pack` or a close-run path existed before this change. Each hit was read in its section.

## 4. Sources and their roles

Change sources (read in full at their boundaries):

| Ref | Source | Identity | Read |
| :- | :- | :- | :- |
| SR1 | `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` | v13.8.8, effective 2026.10.26; blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`; 729,539 bytes; SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f` | front matter 1–223 (application rules §1 to §9); A07 = 2.7 (688–889); A08 = 2.8 (890–1002); A15 = 2.15 (1620–1690); A16 = 2.16 (1691–1825); A17 = 2.17 (1826–1955); A24 = 2.24 (2693–2790); A25 = 2.25 (2791–2899); A26 = 2.26 (2900–2986) |
| SR2 | `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` | v1.1, SPECIFICATION_APPROVED; blob `c4802a5a7fa3`; 43,151 bytes | S-APR 147–193; S-CR3 221–230; supporting: format posture and record control 30–58, CD-1 to CD-3 135–137 |
| SR3 | `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md` | delta 01; blob `9408d6ed091b`; 21,046 bytes | C-8 to C-12 (lines 61–65), with §1, §4, §5 and §6 for context |

Supporting reading (no change source in its own right):

| Ref | Source | Use |
| :- | :- | :- |
| 2.18 | SR1 lines 1956–2081 | identifies the withdrawn cost-ceiling passages of 2.15 and 2.16; none bears on PF12 |
| X03 | `docs/adr/hde/close_pack_writer_adr.md`, blob `2d91679a1981` | Decision 1 to 9 (lines 18–35), stated limits and "Epic-only identity inventory" (36–75), the canon table (76–88), nonclaims and rollback (92–98) |
| X04 | `docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v2.0.md`, blob `1d6a92a483e2`, §18 (753–792) | confirms that plan v2.0 §18's only PF12 row is §8.8 (CR-7) |
| X10, SR4 | Specification review v1.1 (`c48f77a0c220`) and review v1.0 §6 (CR-3 "as changed"); delta review v1.0 (`5a6cecc86f60`) | CR-3's approved disposition and its §8.17 addition; delta approval |
| X11 to X14 | closure decision (`2260eae17974`), post-closure record (`ac60f368f6d9`), QA-120 report (`d6cceaf3a019`), close report (`0bbc8050d3c1`) | identity checked; HDE-CRD-0002 is closed (CLOSE, CHANGE_CLOSED, Isis, 2026-10-26T16:40:00Z), so no change is held on closure grounds |
| PF03 | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, blob `504712df548a`, read in full (633 lines) | editorial standard: titles-only routing, HDE Build Notes by title only, no ellipsis, no outer-bold headings, claim-state separation |
| PF04 | HDE Governance §9.1.1 (role table, line 2401; HDE CRD Records historical) and §1.1 (line 128) | CRD identity wording for RL-001 and RL-009 |
| PF05 | HDE-CLI-API-Vendor-Ref §5.6 (lines 2535–2579) and the start of §5.7 (2581–2590) | what PF12 must register for `public_aux`, aliases and the Aux record |
| PF02, PF29 | HDE Architecture line 956; HDE Users Guide lines 105–111 | the canon-retired route set |
| PF27 | Plan Templates line 530 | the header schema name `pf27.step_log_header.v2` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7`, blob `74944b261c0e` (unchanged on `main`) | task T-PF12 and its rows; "Precedence and closure controls"; "Held and deferred items" |

Read-only repository inspection on `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c` (no writer, test or evidence tool was run):

| Surface | Blob | Facts relied on |
| :- | :- | :- |
| `schemas/close_candidate_source.v2.json` | `e80266a81189` | JSON Schema 2020-12; closed; `schema_version` const `close_candidate_source.v2`; `change_id` pattern `^HDE-(?:EPIC[0-9]{3}\|CRD-[0-9]{4,})$`; `key_outputs` 5 to 64 string-valued entries, keys `^[a-z][a-z0-9_]{0,63}$`, required `close_manifest`, `close_report`, `doc_deltas`, `drain_targets`, `qa_step_logs_manifest`; closure decision `SATISFIED` or `NOT SATISFIED` with posture `review_trace_only`; tracked issue `{id, adr_status}` only |
| `schemas/epic_close_candidate_source.v1.json` | (read) | `schema_version` const `epic_close_candidate_source.v1`; `epic_id` `^HDE-EPIC[0-9]{3}$` |
| `tools/qa/generate_epic_close_pack.py` | (read) | `EPIC_RE` (line 44); v2 selected by `schema_version` |
| `tools/qa/epic021_qa.py`, `tools/qa/generate_epic025_close_pack.py` to `generate_epic029_close_pack.py` | (listed) | present |
| `tools/evidence/update_evidence_index.py` | `ad441edbea3c` | `ADMITTED_CRD_QA` (HDE-CRD-0001, HDE-CRD-0002 with root and key prefix); index entries with both `epic_id` and `crd_id` refused; close-run key `<prefix>.close.<check_id>.primary.log`, role `log`; close-run membership checks; absent-tolerant close-pack rows `hde_crd_nnnn.close_report` / `.manifest` with `crd_id`; `publish_crd_close_run_family` (one transaction, whole-family replacement, recorded QA family required) |
| `ci/checks/check_mirror_schema.sh` | `e72ebba9a1c0` | admits `crd_id`; `EPIC_CRD_EXCLUSIVE` when both keys appear |
| `tools/qa/qa_harness.py` | `37fd7116d2da` | `crd_id` in the Mirror and Human Index optional fields; `validate_check_id` requires a lower-case ASCII safe path segment |
| `tests/evidence/test_evidence_skeleton.py` | `f2e0b855c13a` | `crd_id` in `optional_fields` |
| `docs/evidence/INDEX.json` | (read) | 653 rows; 2 carry `crd_id`; 0 carry both keys; 9 HDE-CRD-0002 close-run rows |
| `audit/HDE-CRD-0002_MANIFEST.json`, `audit/qa/hde-crd-0002/close/` | (read) | `key_outputs` holds exactly the five required keys; 9 close-run primaries with path proofs |
| `docs/ENDPOINTS_CATALOG.json` | symlink `5d041e91a8c0` to `../artifacts/audit/ENDPOINTS_CATALOG.json` | 18 records; one `public_aux` record (`GET /aux/narrative`, aliases `["/api/aux/narrative"]`); `success_endpoints` `[GET /reader]` |
| `tools/evidence/generate_a7_transport_proofs.py` | `b5f71b9c704d` | `validate_catalog`: class set includes `public_aux` (comment: "not yet PF12-registered"); alias rules; aliases only on the Aux record; canon-retired refusal; public sentinel only on non-internal records |
| `tests/http/test_endpoint_catalog.py` | `22d98b22ee7e` | exclusion classes (a) to (d) with bases; the three factories; stale-exclusion and unmounted-record failures |
| `catalog/manifest.json` | (hashed) | SHA-256 `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` at both `9dda63dd` and `0838ba0c` |

## 5. Precedence applied

- PF10 front matter §1 to §9: each addendum governs its own scope; supersession is per addendum. 2.17 amends 2.15 (C-3's pointer clause; resolution A extends C-1). 2.18 withdraws the ceiling sentence of 2.15 ("A projected pass of the unit's cost ceiling") and the cost passages of 2.16; only surviving text was used. 2.14 and 2.11 are not selected and nothing here depends on them.
- The Specification in force is the approved base v1.1 plus delta 01 (ledger "Precedence and closure controls"; PF10 2.20).
- HDE-CRD-0002 is closed (X11), so none of its changes is held on closure grounds.
- Inside PF12 text, HDE Build Notes is named by title only; addendum numbers and locators stay in this proof log (PF12 §0.2; AGENTS.md; PF03 §3).

## 6. Change and disposition ledger

Every change in the selected sources is accounted for below. "Equivalent" means the target already says it, at the cited baseline line.

| Row | Source item | Disposition | Where |
| :- | :- | :- | :- |
| A07 | AD-1 accounting rule, classes (a) to (d), canon-retired exclusion and validator refusal (CR-7) | Redline | RL-008 (with RL-007 for class (b) aliases and RL-006 for `public_aux`) |
| A07 | AD-1 "Unchanged": `success_endpoints` stays `GET /reader` | Equivalent | §8.8 lines 4691–4701 |
| A07 | AD-1 S15 reading (canon-retired removal stays with its canon owner) | Redline | RL-008, third bullet |
| A07 | AD-6 enumeration test and canon trace | Redline | RL-008, fifth and sixth bullets |
| A07 | AD-2 exact `APP_ENV` comparison; CR-8 | Equivalent for PF12 ("explicitly gated by `APP_ENV=dev`", line 4687); wording targets are HDE-CLI-API-Vendor-Ref §5.6 and HDE Mechanics Guide §34 | T-PF05, T-PF14 |
| A07 | AD-3 runner profile; AD-4 production exposure | Out of PF12 ownership | T-PF14, T-PF05, T-PF02 |
| A07 | AD-5 corrective same-version refresh | Not routed to PF12 by the ledger; see observation O-1 | — |
| A07 | Doc-delta candidates for HDE-CLI-API-Vendor-Ref §5.6, HDE Mechanics Guide §34, HDE Architecture §3.4 | Out of PF12 ownership | T-PF05, T-PF14, T-PF02 |
| A08 | Required drainage: CR-7 into §8.8 | Redline | RL-006, RL-007, RL-008 |
| A08 | 2.7 and plan v2.0 §18 candidates (X04) | §8.8 is X04's only PF12 row (covered above); the rest are other documents | T-PF05, T-PF14, T-PF02, T-PF29, T-PF09.4 |
| A08 | LR3-O1 to LR3-O5 | PF10 publication fact, instruction wording, lessons and repository documents | N |
| A15 | One writer, closed v2 schema for Epic and CRD, v1 unchanged | Redline | RL-002 |
| A15 | CRD paths of record and directory form | Redline | RL-002 |
| A15 | Rendering from tracked inputs; `key_outputs` map of path strings | Redline | RL-002, RL-004 |
| A15 | Feedback-dependency refusal kept; requirement text by reference | Redline | RL-002 |
| A15 | Absent-tolerant CRD close-pack Index rows | Redline | RL-002 |
| A15 | Dependency direction (causal inputs to close report and manifest to Index; close-run primaries to Index) | Redline (the writer refuses Index, proofs, orientation, close-run family and manifest as causal inputs; the manifest carries no digest of them); consistent with §6.2.2 | RL-002, RL-004 |
| A15 | Close-run family: path, holdings, PF27 v2 header, posture, post-verdict status, sole writer and transaction, whole-family replacement, QA-family precondition | Redline | RL-003, RL-010 |
| A15 | Membership and the `close/`-only exception to §8.17 "Current-state evidence" | Redline | RL-010, RL-011, RL-012 |
| A15 | No Epic close-run family | Redline | RL-003, RL-010 |
| A15 | C-1 ADR block | Equivalent for PF12 (the same close report, manifest and related contracts "apply to both lanes", line 592); its content rule drains to Change Process Guide §3.5.4 and HDE Governance §2.0.19 | T-PF06, T-PF04 |
| A15 | C-2 current approved Specification; C-3 tracked-issue fields; C-4 ADR text | Out of PF12 ownership (close report content: Change Process Guide, HDE Governance; ADR is not PF); routed by title in RL-002 | T-PF06, T-PF04 |
| A15 | Validation and scope items; nonclaims | Process record; no PF12 text | N |
| A15 | Ceiling sentence | Out of force (2.18) | — |
| A15 | Close-run drainage into Glow QA Guide §3.4.3 | Out of PF12 ownership | T-PF19 |
| A16 | Required drainage: HDE Schemas & Artifacts §1.2 "Close-pack artifacts" | Redline | RL-002, RL-003, RL-004 |
| A16 | Change Process Guide §3.5.2 and §3.5.2.1; Glow QA Guide sections; HDE Governance §2.0.19 (LR7-O9) | Out of PF12 ownership | T-PF06, T-PF19, T-PF04 |
| A16 | LR7-O1 (ADR line 65) | Resolved by 2.17; ADR text is not PF | N |
| A16 | Cost against the ceiling | Historical; withdrawn by 2.18 | — |
| A17 | Rules 1 and 2 (the ADR defers to HDE Build Notes) | Equivalent in kind (PF12 §0.2 states HDE Build Notes supersession); the rule concerns the ADR | N |
| A17 | Amended design table PO-35-4 to PO-35-21 | PO-35-20 posture: Redline RL-002. PO-35-12 ledger minimum content: Equivalent with §1.2's explicit-empty rule (lines 646–647). PO-35-17 deferral drain target in the change kind's register: Equivalent with lines 591 and 652. The other decisions are writer checks recorded in the ADR's stated limits | RL-002; lines 591, 646–647, 652 |
| A17 | Resolution A (TOOLING_BLOCKED under a closure override) | Out of PF12 ownership; drains to Change Process Guide §3.5.4 and HDE Governance §2.0.19; routed by title | RL-002, last-but-one bullet; T-PF06, T-PF04 |
| A17 | Resolution B (v2 tracked issue: ADR status only) | Out of PF12 ownership; PF12 states no tracked-issue pointer form, so no PF12 text conflicts | T-PF06, T-PF04 |
| A24 | CR-10: where the `epic_id`/`crd_id` mutual exclusion is enforced | Redline | RL-005 |
| A24 | R-1 to R-5, V-1 to V-5, business case, CR-9, the 12 Epic viabilities | Implementation, tests and owner items | N |
| A25 | CR-10 drainage: the key set gaining `crd_id` | Equivalent (`crd_id` is already an optional key, line 2310); the enforcement sentence is RL-005 | line 2310; RL-005 |
| A26 | CR-10 drainage into §8.3 | Redline | RL-005 |
| A26 | FND-040 (HDE Mechanics Guide §1.6.3 admission text) | Out of PF12 ownership; PF12 §8.17 already requires the admission extension (line 5277); RL-010 names the admission table only where the close-run family needs it | T-PF14 |
| A26 | FND-021 (C040 drainage into HDE Math Spec §§6.1–6.2) | Held (ledger H-01, Product Owner); not drafted | H-01 |
| A26 | FND-017 to FND-020 | Repository documents | N |
| S-APR | S21 canon impact: which writer, where close-workflow run evidence lives; HDE Schemas & Artifacts §1.2 | Redline | RL-002, RL-003, RL-004, RL-010, RL-011, RL-012 |
| S-APR | S22 implements §8.17's compatibility duty without changing it | Equivalent | line 5277 |
| S-APR | S14 status drainage | Out of PF12 ownership | T-PF05, T-PF29 |
| S-APR | Approval block, phase blocks, QA posture; delta C-8 to C-12 | No PF12 content; C-8 to C-12 change only re-cut wording and the S01 Live QA row | N |
| S-CR3 | §1.2 and §8.17 "the stable CRD ID recorded in PF30" | Redline | RL-001, RL-009 |
| S-CR3 | HDE-SEPA005 note | Out of PF12 ownership | T-PF09.3 |
| X03 | Canon table rows for HDE Schemas & Artifacts (§1.2; §8.17 and §8.17.1) | Redline | RL-002, RL-003, RL-004, RL-010, RL-011, RL-012 |
| X03 | Other canon table rows | Out of PF12 ownership | T-PF06, T-PF19, T-PF14, T-PF04 |
| — | Change-history entry required by §9.1 | Redline | RL-013 |

Held items touched: none. H-01 (FND-021) is recorded above and not drafted; H-02 to H-06 do not bear on PF12.

## 7. Redline summary and producer validation

Thirteen `REPLACE` operations. Validation ran twice: on the in-memory batch, then on the literals re-parsed from the saved redlines file, both against the unchanged baseline bytes.

| Redline | Original lines | Original byte span | Count expected / observed | OLD bytes / SHA-256 prefix | NEW bytes / SHA-256 prefix | Result |
| :- | :- | :- | :- | :- | :- | :- |
| RL-001 | 590 | 44,897–45,130 | 1 / 1 | 233 / `46e22eab9f617e88` | 383 / `ef403e26c2908a59` | OK |
| RL-002 | 595 | 45,683–45,898 | 1 / 1 | 215 / `e2debffc70dd2b02` | 2,929 / `5bbb14155731f9b8` | OK |
| RL-003 | 654 | 50,820–51,050 | 1 / 1 | 230 / `43f0a78c290aed8c` | 973 / `9336d2f610f87dda` | OK |
| RL-004 | 926 | 85,792–85,898 | 1 / 1 | 106 / `49ca846fd5d9be53` | 841 / `b3a77c50bd260f01` | OK |
| RL-005 | 2318 | 210,006–210,269 | 1 / 1 | 263 / `2796b25885bcc8bf` | 953 / `81af8e0417481fc1` | OK |
| RL-006 | 4708–4709 | 527,707–528,171 | 1 / 1 | 464 / `b12b0ca15a015b21` | 572 / `ec5e05e380465439` | OK |
| RL-007 | 4716 | 528,485–528,670 | 1 / 1 | 185 / `e40e3d48f6dfc7df` | 794 / `8126bc33e4669b8c` | OK |
| RL-008 | 4720 | 528,704–528,918 | 1 / 1 | 214 / `1d08fefd49d8e946` | 2,498 / `a86f2b3573f2c494` | OK |
| RL-009 | 5273 | 572,026–572,213 | 1 / 1 | 187 / `5f2697d0b1d302c8` | 334 / `f5691ba9ce2bcb28` | OK |
| RL-010 | 5362 | 578,886–579,038 | 1 / 1 | 152 / `890aa564a6c44f9d` | 2,669 / `5eefa1d9a8e5c877` | OK |
| RL-011 | 5377 | 579,620–579,816 | 1 / 1 | 198 / `465743ebb960c51c` | 406 / `f6fe42dfc7efbb53` | OK |
| RL-012 | 5395–5396 | 581,009–581,345 | 1 / 1 | 336 / `77bc4f3f409ebad9` | 419 / `216c3987e59ee0d9` | OK |
| RL-013 | 5994–5995 | 613,123–613,187 | 1 / 1 | 64 / `deb71c1f1b16b6eb` | 6,780 / `29091cfe2f7328bc` | OK |

Checks performed for every redline: the operation is a supported `REPLACE`; the OLD block is nonempty, occurs exactly once (non-overlapping count) and starts at its expected original offset; it starts at a line start and ends at a line end; NEW differs from OLD; NEW contains no CR or TAB; the authored text contains no ellipsis and no PF10 locator or version; the saved file's OLD and NEW literals equal the prepared ones byte for byte. Batch checks: the thirteen spans, sorted by original offset, neither intersect nor touch; a one-pass simulated application on original offsets (no rematching on mutated text) preserves every untouched byte in order; the simulated revision has balanced fences and exactly one `## 9.6` heading. Simulated revision (Apply verifies it independently): 640,638 bytes; 6,264 LF terminators; still ending `LF LF`; SHA-256 `1cc5ec2ad4ee326c27144e4e1ba01af23e442ab80f9dcb3585039bef3b3fa4c2`.

Corrections during preparation: RL-001's rationale first cited HDE Governance §9.1.1 for the "controlled CRD identity" line, which sits under §1.1; corrected before save. RL-003's location note contained an ellipsis; reworded. Both corrections were re-validated with the whole batch.

## 8. Header provenance for TW-APPLY-10

- Native header (baseline lines 3–10, `## **0.1 Header**`): `**Title:**`, `**Version:**`, `**Status:**`, `**Effective date:**`, `**Last Update Gate:**`, `**Invocation tag:**`, each line ending with two spaces except the last.
- Version scheme: the previous drainage moved v2.9.5 to v2.9.6 (§9.5 record), a single patch increment. RL-013 names v2.9.7.
- Date: preparation date 2026-10-26; RL-013 uses it as the revision date.
- Sources that justified the update, in source order: `BN 13.8.8` (PF10 v13.8.8, in the established `BN <version>` form); `HDE-CRD-0002-specification-v1.1-approved.md`; `HDE-CRD-0002-CL-C-10-closure-decision-v1.2.md` (closure evidence that permits the drainage, matching the established gate's inclusion of the closure decision). Delta 01 (`HDE-CRD-0002-specification-delta-v1.0.md`) justified no PF12 change and is not listed. The ADR (X03) and plan v2.0 (X04) are supporting cross-references, not sources.
- Status `Canon`, Title and Invocation tag are unchanged. Internal restatements of the document's own version and date occur only in the header (lines 6 and 8); §9.5's `v2.9.6` and `2026-10-09` are history and stay.
- The revised PF carries no Draft status, TODO, placeholder marker or drafting note: none exists in the baseline, and the redlines add none.

## 9. Observations not drafted (no source in the assigned rows directs them)

| ID | Observation | Location | Suggested route |
| :- | :- | :- | :- |
| O-1 | §5.3 "Current repository posture" names release_id `52be45584acbaa327da2d1cac724857dcdc999ca8c7a8f65108427942a4afe96` as current; `catalog/manifest.json` on `main` hashes to `77204764c225b6458e748d8ba6ca2b196dd741b88a7250221a94a1640666c51e` after HDE-CRD-0002's same-version refreshes (2.7 AD-5 and later units). RL-013 states that §5.3 is not refreshed | lines 1939–1956 | Product Owner: a later drainage route |
| O-2 | §0.2 "PF09 and PF30 work accountability" says CRD-originated work resolves to "a registered CRD in the PF30 CRD Register"; §8.3's `crd_id` bullet routes lineage to "PF30 CRD Register". HDE Governance §9.1.1 makes HDE CRD Records historical. CR-3 names only §1.2 and §8.17, so these were left as they are | lines 145–157, 2310 | Product Owner (CR-1's PF30 wording family) |
| O-3 | §8.17 shows damaged placeholders such as `audit/qa/\\/` in its heading and several lines, where an `<epic-id>` form was lost | lines 5258, 5343, 5357, 5360, 5362, 5370 | Product Owner: formatting repair needs its own authorization |
| O-4 | §5.3's table carries a Unicode ellipsis after the prefix `988ed2a7`, which Technical Writing Best Practices forbids; the text says the source supplies only a prefix | line 1950 | Product Owner |
| O-5 | §8.8 calls `docs/ENDPOINTS_CATALOG.json` the authoritative file and `artifacts/audit/ENDPOINTS_CATALOG.json` an audit copy; on `main` the docs path is a symlink to the artifacts file | lines 4662, 4666–4675 | Product Owner |
| O-6 | `validate_catalog` requires a `description` key on every record; §8.8's minimum field list does not name it (the list says "at least") | line 4703 | Product Owner |

## 10. Limits

- Repository statements rest on static inspection of checked-in bytes at `0838ba0c`; no test, validator, writer or updater was executed (closed rails kept; no network, production, vendor, database or Railway access was used or needed).
- The revised PF is produced by TW-APPLY-10, not by this preparer. These redlines state no Apply outcome.

## 11. Save verification

Recorded after both files were saved and read back; see the line below.

Both files were saved under `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf12/` and read back completely. The redlines file is 48,813 bytes and 579 lines, SHA-256 `1fa231e84222d61d080cf51de5539de5cb02c9c3e1efe50467a12ff44a8e0dee`, and ends with `END OF REDLINES` and one LF. Validation re-run from the saved file: all 13 redlines OK, simulated revised PF 640,638 bytes, 6,264 LF, SHA-256 `1cc5ec2ad4ee326c27144e4e1ba01af23e442ab80f9dcb3585039bef3b3fa4c2`. Package status: COMPLETE_PACKAGE; batch status: READY.
