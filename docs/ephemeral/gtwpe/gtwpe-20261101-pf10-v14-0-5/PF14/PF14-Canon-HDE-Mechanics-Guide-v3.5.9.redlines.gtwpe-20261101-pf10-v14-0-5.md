# PF14 redlines: HDE Mechanics Guide v3.5.9, run gtwpe-20261101-pf10-v14-0-5

## Identity

| Field | Value |
| :---- | :---- |
| Target | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md`; in-document title `PF14-Canon-HDE-Mechanics-Guide`; version v3.5.9; git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`; 669,363 bytes; SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59`; 7,734 LF characters, so 7,735 lines, the last without a trailing LF |
| Target baseline | `origin/main` at `e2b7427ff418ca8f08f05587c4a541308a76da56`. `docs/pfcanon/` is unchanged from there to `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` (read 2026-11-02, again for r3) |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines; read at `e2b7427` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, triage at `142feb35144d8795f927e0c78b665ace52279064`, read again at `e0375498df16b94a8be5edb339b54416936ffa54`; task T-05; rows C-02, C-04, C-13, C-14, C-17, C-18; uncertain C-07; supporting C-06, C-12, C-16, C-20, C-21. r3 also drains C-01, C-03, C-26, C-29 and C-30 in PF14's own scope; see "Revision r3" |
| Preparing prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at step start, again for r3; last edited 2026-10-09) |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-05/prep-r3`. It supersedes `prep-r2` (commit `ea4c6cf`), which superseded `prep-r1` (commit `9de402f`). r2 was applied as `apply-r2` (commit `6eb135d`); that output is replaced by the application of r3 |
| Preparer | The T-05 document session that Nathan started, in Claude Code session `https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z`; r1 prepared 2026-11-02T00:26Z, r2 2026-11-02T00:40Z, r3 2026-11-02T02:37Z |
| Preparation outcome | `READY` |
| Proof log | `PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside this file |

## How to apply

* Resolve every locator against the unchanged original target. Apply all twenty-five redlines in one pass by original position. No redline's output is another redline's locator, and no two redlines touch the same span or gap.
* Literal convention. Each literal is the exact UTF-8 text strictly between the LF that ends its opening fence line (` ````text `) and the LF immediately before its closing fence line (` ```` `). A literal that ends with a line ending therefore shows an empty line before its closing fence. Trailing spaces inside a literal are part of it. Each literal's byte length and SHA-256 are stated beside it; the fence and info string are not part of the literal.
* Backslashes inside a literal are bytes of the target, not escapes. For example, `\<NNN\>` is six bytes of Markdown source that render as `<NNN>`.
* `REPLACE`: OLD occurs exactly once in the whole original. Replace that one span with NEW.
* `INSERT`: BEFORE immediately followed by AFTER occurs exactly once in the whole original. Insert at the boundary between them. Neither anchor is changed.
* No `FIND_AND_REPLACE` or `DELETE` operation is used.
* The original's last line has no trailing LF. No redline touches the end of the document.

## Revision r2

r1 recorded C-17's "CRD filename form" drainage row as already represented by §37.2's paragraph "CRD close-pack artifacts (canonical filenames)". A context-and-scope recheck of the selected rows found that the paragraph omits the conditional external QA RCA, which HDE Build Notes 2.8 binds to the close report's own prefix (`audit/<prefix>_QA_RCA.md`). r2 adds RL-09 for it. RL-01 to RL-08 are unchanged, byte for byte. r1 was never applied to a pushed output.

## Revision r3

Nathan's direction, 2026-11-02, in this session: "I want you to fix the defects and inconsistencies you noticed". It followed r2's report of PF14 text that conflicts with HDE Build Notes addenda the ledger routed to other documents, and of lost placeholders in PF14. It is read with GTWPE-D3 (`docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`): "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target".

* Contextual drainage, in PF14's own sections:
  * 2.15 R-1 to R-6 (C-26), with 2.16 R-3 (C-30): RL-10 (§1.1, the live compat test for every Epic) and RL-13 to RL-17 (§17.10, §17.10.5, §19.1, the two synthetic Live QA fixtures);
  * 2.16 R-1 and R-2 (C-29): RL-19 (§37.7, the a3 marker is not GATE:CORE-DET evidence) and the change to RL-02 (the generator is retired as GATE:CORE-DET evidence);
  * 2.1 D-3 (C-03): RL-12 (§9.3, the compat environment gate);
  * 2.1 D-1 (C-01): RL-18 (§22, the production vendor override);
  * 2.8, the 2026-11-01 amendment (C-18): RL-11 (§1.6.3, the Epic counterpart of the regression list's CRD admission refusal).
* Formatting repair (`DOC_HYGIENE`), RL-20 to RL-25: `<...>` placeholders lost from canonical paths and definitions, where the complete source establishes the intended text. The proof log lists every other `\\` sequence in the target and why it stays.
* 2.1 D-5 (C-05) needs no PF14 change: PF14 states no rule about gate check-row content, and the rule's owners are HDE Governance and HDE Schemas & Artifacts.
* RL-01 and RL-03 to RL-09 are unchanged, byte for byte. RL-02's OLD is unchanged; its NEW gains one sentence.
* The decisions of 2.1 D-1 and D-3 take effect as canon on publication; their implementing change (Candidate CRD Items List item 9) is open. RL-12 and RL-18 state the rules with "Implementation not claimed" nonclaims, as RL-03, RL-07 and RL-08 do for D-2 and D-4.

## Document control (reserved for TW-APPLY-10)

No redline edits the header. The baseline header in §0.1 "Header" has this native schema:

* Title: `PF14-Canon-HDE-Mechanics-Guide` (unchanged).
* Version: `v3.5.9`, in the form `v<major>.<minor>.<patch>`.
* Status: `Canon`.
* Effective date: `2026-10-26`, in the form `YYYY-MM-DD`.
* Last Update Gate: `BN 13.8.8`, in the form `BN` followed by the HDE Build Notes version that justified the update.
* Invocation tag: `INV-f2ac55d77ce9aacc`.

Source that justifies this update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (HDE Build Notes v14.0.5). The formatting repairs rest on Nathan's direction above, not on a further source file. The body does not restate the document's own version or date. The target has no change log or revision-history section, and none of its rules requires a revision-history or Doc-Delta entry for this change, so no such entry is prepared. A full scan found no Draft status, TODO or drafting note to remove. `<NNN>`, `<pack_sha>` and the like are pattern variables in canonical path forms, not drafting placeholders.

## Index

| ID | Operation | Section | Ledger rows |
| :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE` | §1.1, "BodyGraph and loader seam posture" | C-13, C-14 (DELTA-002) |
| RL-02 | `REPLACE` | §1.1, the remediation paragraph that follows it | C-13, C-14 (DELTA-002); C-29 (r3) |
| RL-03 | `INSERT` | §1.1, request-shaping list: the single permitted version classification | C-02 (D-2) |
| RL-04 | `REPLACE` | §1.1, request-shaping list: v1 is retained legacy selection | C-02 (D-2) |
| RL-05 | `REPLACE` | §1.1, request-shaping list: the non-v2 fallback is superseded | C-02 (D-2) |
| RL-06 | `REPLACE` | §1.6.3, Epic close-run family and publication API | C-17, C-18 |
| RL-07 | `INSERT` | §27.3, attestation builder output-root ownership | C-04 (D-4) |
| RL-08 | `INSERT` | §27.5, the `--log-path` bound | C-04 (D-4) |
| RL-09 | `INSERT` | §37.2, the CRD form of the conditional external QA RCA | C-17 |
| RL-10 | `REPLACE` | §1.1, "Production/user-surface open-rails proof posture" | C-26 (2.15) |
| RL-11 | `INSERT` | §1.6.3, regression list: Epic close-run admission refusal | C-18 |
| RL-12 | `REPLACE` | §9.3, the compat environment gate | C-03 (D-3) |
| RL-13 | `REPLACE` | §17.10, status scope condition | C-26, C-30 |
| RL-14 | `REPLACE` | §17.10, assumptions: the two synthetic Live QA fixtures | C-26, C-30 |
| RL-15 | `INSERT` | §17.10.5, the live compat test is not blocked by the no-user mode | C-26 |
| RL-16 | `INSERT` | §19.1, pre-Glow scope condition | C-26, C-30 |
| RL-17 | `INSERT` | §19.1, the fixture-storage exception | C-26, C-30 |
| RL-18 | `INSERT` | §22, production vendor override | C-01 (D-1) |
| RL-19 | `REPLACE` | §37.7, the a3 two-run marker is not GATE:CORE-DET evidence | C-29 (2.16) |
| RL-20 | `REPLACE` | §5.8, `DEV_SAMPLER_URL` definition | None (hygiene) |
| RL-21 | `REPLACE` | §16, narrative pack storage path | None (hygiene) |
| RL-22 | `REPLACE` | §37.2, Epic close-pack filenames | None (hygiene) |
| RL-23 | `REPLACE` | §37.2, Epic acceptance scaffold locations | None (hygiene) |
| RL-24 | `REPLACE` | §37.3, the Epic manifest path | None (hygiene) |
| RL-25 | `REPLACE` | §37.18.1, the epic-local snapshot path | None (hygiene) |

C-02 and DELTA-002 both change §1.1. Their spans are disjoint: DELTA-002 covers original lines 179 and 181, and C-02 covers the gap after line 214 and lines 222 and 226. RL-10 covers line 257. The proof log gives the byte offsets.

## RL-01

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-13, C-14 (DELTA-002); support C-12, C-16, C-21
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 166 `## **1.1 Capabilities the repo must provide**`
* Location: Paragraph "BodyGraph and loader seam posture" (original line 179, one line)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.4, "Required canon drainage" (DELTA-002) and "Retained decisions and requirements" (C-4 and D-1: loader removed with no shim); addendum 2.5, "Required canon drainage" DELTA-002 (l.854: same pattern as DELTA-001, replace the drift sentence with the delivered boundary); addendum 2.10, "PF09 row-closure" (text drain only) and "Path and surface reality ledger" PSR-001 to PSR-003. Repository inspection at `e2b7427`: `adapter/chart_orchestration.py` and `engine/charts/pure.py` tracked, `engine/charts/loader.py` absent, `load_chart` raises `TypeError` for other argument shapes.
* Rationale: The paragraph still describes the removed `engine/charts/loader.py` as current drift. The replacement states the delivered boundary and keeps every still-valid allocation rule unchanged.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [15061, 15936), original line(s) 179–179.

OLD (875 bytes; SHA-256 `baaf1ca6ab552401ee2d0bb8fdb17b9b57ed5ea439bfd71bf0e80a8687bf02fe`; ends with LF: no):

````text
BodyGraph and loader seam posture. BodyGraph resolution and ingest remain the sanctioned BodyGraph I/O seam described in §19.1. The non-BodyGraph loader responsibility represented by `engine/charts/loader.py` is implementation drift, not a sanctioned Engine I/O seam; HDE Architecture §1.1 owns this classification and HDE-Build Notes records the required correction. Environment/SAFE-rails evaluation, provider selection, chart acquisition, clocks, correlation context, operational logging and filesystem writes belong in Adapter-owned application/infrastructure orchestration. Vendor and database acquisition must use the existing sanctioned BodyGraph resolver/ingest boundary. Only explicit data-in/data-out chart validation or normalization may remain under Engine ownership, with no time, randomness, environment, network, provider, logging or filesystem side effects.
````

NEW (1158 bytes; SHA-256 `ee5bb8d8de2e255b079c40403559ac1d9dc0a5d13f1e5e4dfd4b42aedc4026e3`; ends with LF: no):

````text
BodyGraph and loader seam posture. BodyGraph resolution and ingest remain the sanctioned BodyGraph I/O seam described in §19.1. Non-BodyGraph chart loading is split between the Adapter-owned chart entry `adapter/chart_orchestration.py::load_chart` and the pure Engine module `engine/charts/pure.py`; HDE Architecture §1.1 owns this classification, and HDE-Build Notes records the delivered correction. The former `engine/charts/loader.py`, which mixed those responsibilities as implementation drift, is removed with no shim, and its legacy `load_chart(user_id)` signature is retired: the Adapter entry raises `TypeError` for any other argument shape. Environment/SAFE-rails evaluation, provider selection, chart acquisition, clocks, correlation context, operational logging and filesystem writes belong in Adapter-owned application/infrastructure orchestration. Vendor and database acquisition must use the existing sanctioned BodyGraph resolver/ingest boundary. Only explicit data-in/data-out chart validation or normalization may remain under Engine ownership, with no time, randomness, environment, network, provider, logging or filesystem side effects.
````

## RL-02

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-13, C-14 (DELTA-002); support C-12, C-16, C-21
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 166 `## **1.1 Capabilities the repo must provide**`
* Location: Remediation paragraph after "BodyGraph and loader seam posture" (original line 181, one line)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.4, "Required canon drainage" (DELTA-002 covers the loader seam posture and the remediation paragraph), "Retained decisions and requirements" (C-1 generator migration, the import guard, I-1 to I-3); addendum 2.10, "Retained decisions and requirements" (residual risk FND-005: the generator still exits 2) and PSR-003. Repository inspection at `e2b7427`: `scripts/make_compat_determinism_artifacts.py` imports `adapter.chart_orchestration.load_chart` and prints `compat_public not implemented` before its chart call; `tests/charts/test_chart_loader_import_guard.py` and `tests/charts/test_chart_pure_purity.py` tracked; the entry logs `"route": "loader.load_chart"`. Addendum 2.16 R-2 (r3): the generator is retired as GATE:CORE-DET evidence, and it and its test that pins exit 2 stay as history; Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: The paragraph is a pre-delivery remediation instruction that says removal has not occurred. The replacement states the delivered caller posture, the guards and the retained limits, and keeps the PF09 nonclaim. r3 adds the addendum 2.16 R-2 retirement.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [15938, 16486), original line(s) 181–181.

OLD (548 bytes; SHA-256 `fad91334c374b3f720c355f57768f484b259aee6c3f266f9dc4c967e7cc1317f`; ends with LF: no):

````text
Remediation must migrate active callers, including compatibility/determinism and generator callers, to that orchestration and provide meaningful boundary tests. It must preserve existing canonical outputs and public/vendor contracts; it does not authorize fallback behavior, an Engine Core I/O exception or a second resolver. This is a required mechanics disposition, not a claim that relocation, caller migration or removal has occurred. The source proposes phased PF09 coverage separately; PF14 neither allocates its row/ID nor claims its status.
````

NEW (1181 bytes; SHA-256 `54a36673ce864b4eaa527acbb6dd4aae6f84a115f6ed674f79b62b5b66f2df75`; ends with LF: no):

````text
Callers of the chart path use the Adapter entry or the pure interface. The compatibility/determinism generator `scripts/make_compat_determinism_artifacts.py` imports the Adapter entry; its compat computation is not restored, and it still exits 2 with `compat_public not implemented` before its chart call. The generator is retired as GATE:CORE-DET evidence; it and its test that pins exit 2 stay as history, and no record may cite it as current proof. Do not restore `engine/charts/loader.py`, add a shim for it, or put time, environment, filesystem, provider or logging access under `engine/charts/`. `tests/charts/test_chart_loader_import_guard.py` fails if the removed module path or a tracked import of it returns, and `tests/charts/test_chart_pure_purity.py` fails if `engine/charts/pure.py` gains a forbidden dependency or side effect. The boundary preserves existing canonical outputs and public/vendor contracts; it does not authorize fallback behavior, an Engine Core I/O exception or a second resolver. The route string `loader.load_chart` in the entry's log line is a label, not a module. PF14 neither allocates the related HDE-Build Checklist row nor claims its status.
````

## RL-03

* Operation: `INSERT`
* Change type: NEW_CANON
* Ledger rows: C-02 (D-2); support C-06
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 166 `## **1.1 Capabilities the repo must provide**`
* Location: "HDAPI v2 request-shaping and response-mapping mechanics" list: new bullet between original lines 214 and 215
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-2 "Decision" ("What governs"; "The two canon rules fit together as follows") and "Canon superseded or added to" (HDE Mechanics Guide §1.1, "infer runtime behavior from vendor API version path strings": added to, with the single permitted classification).
* Rationale: D-2 adds one permitted version reading to the §1.1 prohibition and keeps every other prohibition in force.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 22698, immediately after original line 214. Neither anchor is changed.

BEFORE (293 bytes; SHA-256 `80aa81d548c1b66693b1f43b385ef9ac463ddc2f2d9c39ca45f073587c3f7617`; ends with LF: yes):

````text
* Runtime request construction MUST NOT hardcode `/v1` or `/v2` as active route-construction constants, append versioned vendor paths to `HD_API_BASE_URL`, double-prefix configured versions, normalize away configured prefixes, or infer runtime behavior from vendor API version path strings.  

````

AFTER (66 bytes; SHA-256 `77251bb584578b094a60c0cd697d72682b2137b4e8a6c0d2341e5f3c77b48147`; ends with LF: no):

````text
* Versioned vendor endpoint strings MAY remain as source inventory
````

INSERT (914 bytes; SHA-256 `074586b44bc28055995c0d2cae79a97dbe73b57017a1e3bfe15abc8da9ad3b9c`; ends with LF: yes):

````text
* The single permitted reading of a version from the configured base is the route-selection classification governed by HDE-CLI-API-Vendor-Ref §7.1.10, for every resolver-selected vendor acquisition: `bg:resolve --source vendor` and compat chart acquisition by `hdctl showcompat` and conjunction. It is one exact, case-sensitive comparison of the validated terminal path segment against the two allow-listed values `v1` and `v2`, made once, before any route is built. The selected route's resource, payload family and credential projection then come from that route's contract metadata. The prohibitions in this list govern everything else: nothing may hardcode `/v1` or `/v2` as a route-construction constant, append or normalize a version, select auth by path prefix, or key any other runtime behavior on a version string. This states required behavior; it does not claim that the current classifier conforms.  

````

## RL-04

* Operation: `REPLACE`
* Change type: CONSISTENCY
* Ledger rows: C-02 (D-2); support C-06
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 166 `## **1.1 Capabilities the repo must provide**`
* Location: "HDAPI v2 request-shaping and response-mapping mechanics" list, original line 222
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-2 "Decision" ("The v1 path is retained legacy selection, not fallback. Its retirement still needs the separately versioned decision §7.1.10 requires."), "Basis" (the byte-contract home has decided in §7.1.10) and "Left undecided" (retirement stays a separate, versioned decision).
* Rationale: The bullet waits for a decision on whether v1 remains a fallback. D-2 records that decision; only retirement stays open.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [23833, 23999), original line(s) 222–222.

OLD (166 bytes; SHA-256 `5374472165ccc8baa8f5688035c01dccac3a1d3cbd2cd5ace321a24a77113891`; ends with LF: no):

````text
* Preserve v1 BodyGraph behavior as explicit legacy behavior until the owning architecture and byte-contract homes decide whether v1 remains a fallback or is retired.
````

NEW (246 bytes; SHA-256 `4723c851b2401d446a61b6cf1e3a0940f098194f0d5b2dd5a64aa13abac828b3`; ends with LF: no):

````text
* Preserve v1 BodyGraph behavior as retained legacy selection, not fallback, for a configured base ending in exactly `v1`. Retirement of the v1 legacy route requires the separately versioned decision that HDE-CLI-API-Vendor-Ref §7.1.10 requires.
````

## RL-05

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-02 (D-2); support C-06
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 166 `## **1.1 Capabilities the repo must provide**`
* Location: "HDAPI v2 request-shaping and response-mapping mechanics" list, original line 226
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-2 "Canon superseded or added to" (HDE Mechanics Guide §1.1, "Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback" is superseded; a terminal v1 base keeps the legacy route-family posture; no other non-v2 base selects a route), "Decision" ("No fallback"; "Classification label").
* Rationale: D-2 supersedes the bullet's permission for every non-v2 base. The replacement keeps the terminal-v1 posture and records the label's meaning.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [24811, 25020), original line(s) 226–226.

OLD (209 bytes; SHA-256 `4c96f68aceb82906b1d666bcf297b351aaf59e749fb3cc48d03429c70e44fd5f`; ends with LF: no):

````text
* Non-v2 configured bases MAY preserve explicit legacy BodyGraph fallback only as a legacy route-family posture with `HD-Api-Key` auth, governed geokey handling, and no v2 BodyGraph-detail compatibility claim.
````

NEW (585 bytes; SHA-256 `8959aed9e3bd16894638af5821e3b288e0d4250ccf5ef198d4306911b54a104b`; ends with LF: no):

````text
* A configured base ending in exactly `v1` keeps the legacy BodyGraph route-family posture, with `HD-Api-Key` auth, governed geokey handling, and no v2 BodyGraph-detail compatibility claim. No other non-v2 configured base selects a route, and no non-v2 base reaches `bodygraphs` by fallback; HDE-CLI-API-Vendor-Ref §7.1.10 governs that refusal and the configured-base boundary. The emitted classification label `explicit_legacy_fallback` for a terminal `v1` base stays an existing wire value in governed evidence; it names the retained v1 legacy selection and makes no fallback claim.
````

## RL-06

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-17, C-18 (2.8 drainage table, 2026-11-01 amendment B-4); support C-20
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 750 `  ## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**` > line 894 `### **1.6.3 Generic Epic/CRD QA harness (local records, governed publication, legacy viability)**`
* Location: "Current-family validation and publication" list: the end of the close-run-family bullet (original line 919), which gains a following bullet
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8, "Required canon drainage" row HDE Mechanics Guide ("§1.6.3 gains the close-run publication API") and its note (the 2026-11-01 amendment's Epic close-run family is an additional drainage item); decision 7 (Epic family and `publish_epic_close_run_family`); stated limits ("An Epic close run needs its own explicit admission"; HDE-EPIC041 the one Epic admitted in `ADMITTED_EPIC_CLOSE`). Supporting: addendum 2.9 B-4. Repository inspection at `e2b7427`: `ADMITTED_EPIC_CLOSE` admits `HDE-EPIC041` with `audit/qa/hde-epic041` and `audit.qa.hde_epic041`; signature and behavior of `publish_epic_close_run_family`; row key form and `epic_id`.
* Rationale: §1.6.3 already carries the CRD close-run API; its sentence "No Epic close-run family is admitted." is superseded by the 2026-11-01 admission.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [105086, 105188), original line(s) 919–919.

OLD (102 bytes; SHA-256 `b0461c1969a5ed8134d183562d506c490a90e60d9407db37076c9a018d1e5113`; ends with LF: yes):

````text
Human Index keys are `<prefix>.close.<check_id>.primary.log`. No Epic close-run family is admitted.  

````

NEW (1322 bytes; SHA-256 `c47df9a1dc249c77c28f2ce7e8a5ad2ffa3abd62e5f0c8deac11f00436b8e389`; ends with LF: yes):

````text
Human Index keys are `<prefix>.close.<check_id>.primary.log`.  
* An Epic close run needs its own explicit admission. Source-owned updater admission for Epic close runs is the `ADMITTED_EPIC_CLOSE` table in `tools/evidence/update_evidence_index.py`. It admits `HDE-EPIC041` only, with QA root `audit/qa/hde-epic041/` and Human Index key prefix `audit.qa.hde_epic041`; another Epic needs its own row. An admitted Epic has the same post-verdict close-run family, `audit/qa/<epic-dir>/close/<check_id>/primary.log` with its sibling `primary.log.path_proof.txt`, published only through `tools.evidence.update_evidence_index.publish_epic_close_run_family(config, results, *, captured_at_utc=None, coherence_verifier=None)` for an Epic `HarnessConfig`, a Python API in the same updater module. It requires a nonempty result family, renders each primary through the QA harness's own renderer with the own-primary path under `close/`, requires the Epic's recorded QA step-logs manifest and primaries, writes neither `qa_step_logs_manifest.json` nor any `checks/` file, refuses if either changes during publication, and replaces the whole family inside one outer recovery transaction with the bounds stated for `publish_crd_check_family`. Membership and the Human Index key form are as for a CRD, and each row carries `epic_id`.  

````

## RL-07

* Operation: `INSERT`
* Change type: NEW_CANON
* Ledger rows: C-04 (D-4, attestation builder); support C-06
* Heading path (raw original heading lines): line 4368 `# **27\) Release and Provenance Packaging**` > line 4423 `## **27.3 External release attestation**`
* Location: New paragraph and list between the builder's MUST list (ends original line 4442) and the paragraph "Direct source-tree execution" (original line 4444)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-4 "Decision for the release attestation builder" (interface unchanged; exclusive claim; no writes through symlinks; scoped cleanup; unchanged), "Canon superseded or added to" (HDE Mechanics Guide §27.3: added to) and "Left undecided" (the claim mechanism belongs to the implementing change). Supporting: 2.1 "Scope, exclusions and nonclaims" and "Dependencies" (item 9 open).
* Rationale: D-4 adds the output-root ownership rules to §27.3; the refusal list stands.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 388603, immediately after original line 4443. Neither anchor is changed.

BEFORE (42 bytes; SHA-256 `6aac1f0ed2f29bfacd86f41fd0c4b7ed86dfb3674a54d641fc1269298b5b078e`; ends with LF: yes):

````text
* leave the source checkout byte-stable.


````

AFTER (81 bytes; SHA-256 `e925fc193f048214957535d496dcb74a1dad963c884dd6e5371f5215fd3bc799`; ends with LF: no):

````text
Direct source-tree execution of the write-capable identity closure is prohibited.
````

INSERT (1183 bytes; SHA-256 `e5f5f394e7567834c3a5c60fd6a02f435a5adf17cf3e6ee00c2b1f1a8798ecd6`; ends with LF: yes):

````text
Output-root ownership. The documented `--output <external-empty-directory>` interface is unchanged: the builder creates an absent output root and accepts an existing, empty, non-symlinked directory outside the source repository. Within that interface the builder MUST:

* claim the output root exclusively for the run before any other write, by an atomic create that fails if another run holds the root;  
* refuse a root it cannot claim with a typed failure code before any write;  
* add no member to a successful bundle beyond the `hde.release_attestation.v1` contract through that claim;  
* write below the output root only to paths this run created, and refuse, not follow, a pre-existing or substituted symlink anywhere below the root; and  
* on failure, remove only the files and directories this run created, then write its failure receipt, and never remove a path it did not create.

The mechanism of the exclusive claim belongs to the implementing change. The refusals above, the isolated build, the byte-stable checkout and the success and failure contracts below are unchanged. These rules state required behavior; they do not claim that the current builder conforms.


````

## RL-08

* Operation: `INSERT`
* Change type: NEW_CANON
* Ledger rows: C-04 (D-4, --log-path bound); support C-06
* Heading path (raw original heading lines): line 4368 `# **27\) Release and Provenance Packaging**` > line 4486 `## **27.5 Sanity pipeline (release & provenance)**`
* Location: New paragraph between "Current generic gate (bounded baseline observation)" (original line 4488) and the nested heading at original line 4490 `### Historical EPIC038 nineteen-stage family (records-only)`; the text belongs to §27.5 itself, not to the nested historical subsection
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-4 "Decision for the sanity pipeline" and "Canon superseded or added to" (HDE Mechanics Guide §27.5: added to, with the `--log-path` bound). Supporting: 2.1 "Dependencies" (item 9 open).
* Rationale: Canon was silent on `--log-path`; D-4 bounds it.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 392984, immediately after original line 4489. Neither anchor is changed.

BEFORE (713 bytes; SHA-256 `9410d093d51307f629e07b4e300e109d7fb064378587327d948568be7519d653`; ends with LF: yes):

````text
Current generic gate (bounded baseline observation). The accepted EPIC040 release path uses the fifteen-stage generic chain implemented by `tools/evidence/run_sanity_pipeline.py`, with its gate wrapper and external attestation owner. It preserves closed rails, source cleanliness, current byte/evidence integrity and fail-closed admission. A non-admitted release is reported explicitly as `RELEASE_NOT_ADMITTED`/`NOT_ADMITTED`, never as PASS or an ordinary behavior failure; successful admission ends that temporary interval, rather than authorizing a permanent skip or frozen-byte success substitute. The accepted complete cut and synthetic OPS verification are scoped records, not a current execution receipt.


````

AFTER (59 bytes; SHA-256 `62a6d4644a06b8f5d60d887c97484b7507ffa874c0f5d223b804b21b2d76533d`; ends with LF: no):

````text
### Historical EPIC038 nineteen-stage family (records-only)
````

INSERT (580 bytes; SHA-256 `f4547191846b1a0a6e832d6c560917f872fb76042aca3d0c45ed9dea06f5f451`; ends with LF: yes):

````text
Log-path bound (normative). `tools/evidence/run_sanity_pipeline.py --log-path` accepts, inside the repository, only the canonical log `audit/gates/sanity_pipeline/sanity_pipeline.log`. Outside the repository it accepts a target only when the target is not a symlink and no component of its path is a symlink, its parent directory exists, and it names a regular file or no existing file. A refused target fails with a typed, numeric-free error before any step runs or any byte is written. This bound states required behavior; it does not claim that the current pipeline conforms.


````

## RL-09

* Operation: `INSERT`
* Change type: CANON_UPDATE
* Ledger rows: C-17 (2.8 drainage table, CRD filename form; decision 4 and the QA RCA stated limit)
* Heading path (raw original heading lines): line 4984 `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > line 4996 `  ## **37.2 Governance & homes**`
* Location: Paragraph "CRD close-pack artifacts (canonical filenames)" (original line 5033): new sentence after the doc-delta ledger sentence
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8, "Required canon drainage" row HDE Mechanics Guide ("§37.2 epic-scoped close-pack filename list": add the CRD filename form); decision 3 (a CRD uses its ID as the prefix); decision 4 (the QA RCA, embedded or bound as `audit/<prefix>_QA_RCA.md`); stated limit ("A bound QA RCA must be `audit/<prefix>_QA_RCA.md`, using the close report's own prefix").
* Rationale: The CRD filename paragraph names the close report, manifest and doc-delta ledger but not the conditional external QA RCA, so the CRD filename form was only partly represented; preparation r1 recorded it as fully represented.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 431037, inside original line 5033. Neither anchor is changed.

BEFORE (74 bytes; SHA-256 `e731315d9c3c835d64c8bf7def597cdba6d28cfc6cea286eef3d73ae44fe203f`; ends with LF: no):

````text
so its doc-delta ledger is `audit/docdeltas/hde-crd-<NNNN>_doc_deltas.md`.
````

AFTER (105 bytes; SHA-256 `9304555caca8291d838a13cdc76ab574137fe94cd254539129fb1bea8dabb475`; ends with LF: no):

````text
 These are governed artifacts and must not be duplicated under alternate spellings.

Close-pack generator
````

INSERT (149 bytes; SHA-256 `0cffc4b4f9745df1e7f4e36062a4c89b6d8555043b67db373fff1b81cd4cb71d`; ends with LF: no):

````text
 When its QA RCA summary is not embedded in the close report, the conditional external QA RCA uses the same prefix, `audit/HDE-CRD-<NNNN>_QA_RCA.md`.
````

## RL-10

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-26 (2.15 R-1 to R-6); support C-30
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 166 `## **1.1 Capabilities the repo must provide**`
* Location: Paragraph "Production/user-surface open-rails proof posture" (original line 257, one line)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15, R-1 (every Epic's QA plan includes and its QA run executes the live compat test, whatever the Epic changed; the deployed-service check; an Epic's own live surfaces add their own step; what does not satisfy R-1), R-2 (only the Product Owner may waive any part; an agent's finding is a question; silence is not a waiver), R-3 ("Live QA" reserved; other QA is "closed-rails QA"), R-4 (stage enforcement), R-5 (a test that cannot run is TOOLING_BLOCKED and never a PASS, waiver or closure), R-6 (execution controls unchanged), and "Relation to other canon" (supersedes the dependency on whether the Epic touches a production surface). Supporting: addendum 2.16 R-3. Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: The paragraph makes live proof depend on whether the Epic touches a production surface and lets an explicit exemption discharge it. Addendum 2.15 supersedes both for the live compat test. The replacement keeps the own-surface live test and every unchanged control.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [30389, 31221), original line(s) 257–257.

OLD (832 bytes; SHA-256 `1f57211c7797b149f89213dfc050a5230791ce8568aa3ef9aae9f63e1459955b`; ends with LF: no):

````text
Production/user-surface open-rails proof posture. Every Epic or QA plan that touches a feature, component or function the HD Engine will use in production MUST include at least one bounded, intentional, secret-safe, evidence-recorded live vendor test of the affected runtime behavior, with `SAFE_MODE=0` and `ALLOW_NETWORK=1` for that step. Closed-rails fixtures, source inspection, DB or service checks, or an explicit exemption do not discharge that test. Closed-rails control-flow proof remains separate. Restore the applicable rails posture after the step; the Product Owner authorizes the identified executor under the controls above. PF14 records the mechanical proof distinction only; QA planning, acceptance, gates and closeout remain in their single homes. An OPS smoke is not planned QA merely because it calls the vendor.
````

NEW (1872 bytes; SHA-256 `c12456b384274d468241321fcbc4143d7bf332e5371bcf6fdd96940347b11fb3`; ends with LF: no):

````text
Production/user-surface open-rails proof posture. Every Epic's QA plan includes, and its QA run executes, the live compat test, whatever the Epic changed and whether or not its own surfaces are on a production path: `hdctl showcompat --source vendor` with `SAFE_MODE=0` and `ALLOW_NETWORK=1` for that step only, on synthetic birth data only, and the deployed-service check of the production HD Engine, which compares its `/internal/version` release identity with the release on `main` and has the production Reader score the two synthetic Live QA fixtures of §17.10 in both orders. Every Epic or QA plan that touches a feature, component or function the HD Engine will use in production MUST also include at least one bounded, intentional, secret-safe, evidence-recorded live vendor test of the affected runtime behavior, with `SAFE_MODE=0` and `ALLOW_NETWORK=1` for that step. Only a recorded Product Owner waiver sets aside either test or any part of it. Closed-rails fixtures, fixture replay, mocks, source inspection, DB or service checks, governed evidence artifacts, review approval, an unrun procedure, or an agent's finding that a test does not apply do not discharge it. A live test that cannot run is `TOOLING_BLOCKED`; it never becomes a PASS, a waiver or a closure. QA without the live compat test is closed-rails QA, not Live QA. Closed-rails control-flow proof remains separate. Restore the applicable rails posture after the step; the Product Owner authorizes the identified executor under the controls above. PF14 records the mechanical proof distinction only. The live compat test's pass predicates, waiver form, naming and stage enforcement are owned by HDE-Governance, the Glow QA Guide and HDE-Build Notes, and QA planning, acceptance, gates and closeout remain in their single homes. An OPS smoke is not planned QA merely because it calls the vendor.
````

## RL-11

* Operation: `INSERT`
* Change type: CONSISTENCY
* Ledger rows: C-18 (2.8 amendment of 2026-11-01, Epic close-run family); support C-20
* Heading path (raw original heading lines): line 162 `  # **1\) Repository & Tooling Skeleton (capabilities, not paths)**` > line 750 `  ## **1.6 QA tooling bootstrap & Live QA harness (mechanics)**` > line 894 `### **1.6.3 Generic Epic/CRD QA harness (local records, governed publication, legacy viability)**`
* Location: "Closed-rails regression responsibilities" list, second bullet (original line 1160): new clause before its final full stop
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.8, the 2026-11-01 amendment (Epic close-run family) and its stated limit ("An Epic close run needs its own explicit admission"); addendum 2.9 B-4. Repository inspection at `84d6d1c`: `publish_epic_close_run_family` refuses a configuration whose `epic_id` is not in `ADMITTED_EPIC_CLOSE` with a message naming the admitted set; `tests/evidence/test_evidence_index_missing_state.py::test_epic_close_run_publication_refuses_scope_and_restores_on_failure` asserts that refusal for `HDE-EPIC040` and for a CRD configuration. Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: The regression list names only the CRD admission refusal. RL-06 adds the Epic close-run admission, so the list gains its Epic counterpart.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 127750, inside original line 1160. Neither anchor is changed.

BEFORE (82 bytes; SHA-256 `a24c13efb8568a83e5bc0dfd89ecd72b53b4e5ff8d0efbe40797817d4dc9e8cc`; ends with LF: no):

````text
refused by name by both the check-family and the close-run publication entrypoints
````

AFTER (42 bytes; SHA-256 `6215f45a61a9e56d79de9a75f5e7215f537b770151f8d93f53756d479eb60234`; ends with LF: no):

````text
.  
* Exercise the actual canonical writer
````

INSERT (211 bytes; SHA-256 `b1588303ff546bd84c702709e0d8a07953254b78ec7aa1f6bd7ef7643281970e`; ends with LF: no):

````text
; and governed Epic close-run admission limited to the `ADMITTED_EPIC_CLOSE` set, with an unadmitted Epic or a CRD configuration refused by the Epic close-run publication entrypoint, which names the admitted set
````

## RL-12

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-03 (D-3); support C-06
* Heading path (raw original heading lines): line 2092 `# **9\) Reader & Compat endpoints**` > line 2269 `  ## **9.3 Compat (pair; internal/admin) \[Implemented (dev/admin)\]**`
* Location: Paragraph "Prod gate (hard)" (original line 2275, one line)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-3 "Decision" (classification; gate order; authentication; wider exposure), "Canon superseded or added to" and "Dependencies and unresolved obligations" (item 9, the implementing change, is open). Supporting reading: HDE-Governance §4.1.4 "Dev/admin APP_ENV gating"; HDE-CLI-API-Vendor-Ref §5.5. Repository inspection at `84d6d1c`: `engine/http/compat_handler.py` line 112 refuses only the production-like posture (`_compute_env_mode(os.environ) == "prod"`). Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: The paragraph gates only `APP_ENV=prod`. D-3 makes the compat namespace a dev/admin surface with a two-step gate. The replacement states the gate and keeps a nonclaim, because the 403 refusal is not implemented.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [223504, 223583), original line(s) 2275–2275.

OLD (79 bytes; SHA-256 `0a43aa32b82f268fc3140178533acb28b700030f431009d9fcd5027eacb8b6bb`; ends with LF: no):

````text
Prod gate (hard). If APP\_ENV=prod, /api/compat/v1 MUST return 404 (Not Found).
````

NEW (1129 bytes; SHA-256 `2e4f410a59fda4dc05e27e66a1fd523313b1cad7156d926843e9297ba4b3517a`; ends with LF: no):

````text
Environment gate (hard; dev/admin surface). The compat namespace, `/api/compat/v1` and its descendants, is a dev/admin-only surface. On every method, before any compat computation, database read or vendor call: a production-like posture (`prod`, `production` or `live`, read from trimmed, case-folded nonempty `APP_ENV`, otherwise `ENGINE_ENV`) MUST return 404 (Not Found) with `ERR_NOT_FOUND`; any other request MUST be served only when `APP_ENV` is exactly `dev`, `test` or `local`, with no trimming, case-folding or default, and is otherwise refused with 403 `ERR_WRITER_FORBIDDEN`; `ENGINE_ENV` never admits the surface. No credential is required while the surface is admitted only under that `APP_ENV` rule; before it is served in any other environment, a later decision must require an admin credential and its logging rules. Response bytes, headers and method rules are owned by HDE-CLI-API-Vendor-Ref §5.5, and the dev/admin allow-list by HDE-Governance §4.1.4. Implementation not claimed: current code refuses only the production-like posture, and the 403 refusal belongs to an implementing change that has not landed.
````

## RL-13

* Operation: `REPLACE`
* Change type: CONSISTENCY
* Ledger rows: C-26 (2.15 R-1, the two synthetic stored people); C-30 (2.16 R-3)
* Heading path (raw original heading lines): line 3003 `# **17\) CLI Components**` > line 3164 `  ## **17.10 Interim no-user QA mode (pre-Glow prod)**`
* Location: Paragraph "Status (normative)" (original line 3166): the end of its first sentence
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15 R-1 ("The two synthetic stored people": SYN-A and SYN-B kept in the production database as permanent QA fixtures) and addendum 2.16 R-3 (both stored and registered). Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: The section's scope condition says no user-bound BodyGraph rows exist, which is no longer true once the two fixtures are stored. The mode still applies to everything except them.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [295199, 295309), original line(s) 3166–3166.

OLD (110 bytes; SHA-256 `015405ae1195ce036d3a13f1262f85239b14aeeafb7b1f0df83d0a97be769440`; ends with LF: no):

````text
where there is no app-level user model and no persistent user-bound BodyGraph rows configured in the database.
````

NEW (168 bytes; SHA-256 `719fd61465678e1242290dfb97f7ed9f90c282c44282e639d1664f8e6077c92b`; ends with LF: no):

````text
where there is no app-level user model and no persistent user-bound BodyGraph rows configured in the database other than the two synthetic Live QA fixtures named below.
````

## RL-14

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-26 (2.15 R-1, R-5); C-30 (2.16 R-3)
* Heading path (raw original heading lines): line 3003 `# **17\) CLI Components**` > line 3164 `  ## **17.10 Interim no-user QA mode (pre-Glow prod)**`
* Location: "Assumptions (pre-Glow prod)" list, second bullet (original line 3171)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15 R-1 (the fixtures' UUIDs; stored through the engine's own write path under the Product Owner's write authorization by an Ops task; TOOLING_BLOCKED while either is missing), R-5 and R-6; addendum 2.16 R-3. Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: The assumption is stale. The replacement names the two fixtures and records that storing them is Ops work, not a QA or mechanics step, so the next bullet's prohibition on app-like user records still holds.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [295638, 295698), original line(s) 3171–3171.

OLD (60 bytes; SHA-256 `33a6a8763463c7ad019616fb49ccdd9613477915ef0a062462728802121e5fe4`; ends with LF: no):

````text
* No persistent user-bound BodyGraphs exist in production.  
````

NEW (589 bytes; SHA-256 `0fc6712b085cc50dd767f38dbefa965c60866213e49434cbdcca2392ad043ac1`; ends with LF: no):

````text
* No persistent user-bound BodyGraphs exist in production other than the two synthetic Live QA fixtures, SYN-A (`9cff60ae-6eb6-5618-aec5-8acaa4f290d2`) and SYN-B (`57f0c055-ff09-5fdb-aedb-def880437e6f`). They are permanent QA fixtures, not app users or app-like user records. They are stored, and stored again if missing, only through the engine's own write path under the Product Owner's write authorization, as Ops work, not as a QA or mechanics step. The deployed-service check of the live compat test (§1.1) reads only these two, and it is `TOOLING_BLOCKED` while either is missing.  
````

## RL-15

* Operation: `INSERT`
* Change type: CONSISTENCY
* Ledger rows: C-26 (2.15 R-1)
* Heading path (raw original heading lines): line 3003 `# **17\) CLI Components**` > line 3164 `  ## **17.10 Interim no-user QA mode (pre-Glow prod)**` > line 3400 `  ### **17.10.5 Forward plan (routing only)**`
* Location: Final paragraph of §17.10.5 (original line 3407): new sentence at its end
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15 R-1 (the deployed-service check scores SYN-A and SYN-B, and its missing-fixture case is TOOLING_BLOCKED, not blocked by environment). Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: Without it, the deployed-service check could be read as a requirement that assumes existing users and so as blocked by this mode.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 315375, inside original line 3407. Neither anchor is changed.

BEFORE (70 bytes; SHA-256 `5d9372b5dce904209fde3b1adfce1d775ca5609410ff6b18c37dca66ba52561a`; ends with LF: no):

````text
satisfied instead using the no-user QA mode described in this section.
````

AFTER (62 bytes; SHA-256 `67ad3a7b00ac579e55c577926740072de7d9f006063267c099559b03842c9961`; ends with LF: no):

````text


## **17.11 Admin QA bundle surfaces (full product payload)**
````

INSERT (166 bytes; SHA-256 `d75c86ab9387899abbbf78eb6e6f98952e6e6f79b17e2b8d02809b2acd8797f4`; ends with LF: no):

````text
 The live compat test of §1.1, including its deployed-service check of the two synthetic Live QA fixtures, is not such a requirement and is not blocked by this mode.
````

## RL-16

* Operation: `INSERT`
* Change type: CONSISTENCY
* Ledger rows: C-26 (2.15 R-1); C-30 (2.16 R-3)
* Heading path (raw original heading lines): line 3686 `# **19\) Vendor Ingest Pipeline — source policy & proofs (normative)**` > line 3688 `## **19.1 Policy (normative)**`
* Location: "Pre-Glow prod (no users)" bullet (original line 3693): new words before its colon
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15 R-1 and addendum 2.16 R-3. Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: Same scope condition as RL-13, in §19.1.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 338282, inside original line 3693. Neither anchor is changed.

BEFORE (68 bytes; SHA-256 `a60dfded8b9e40c255aa9e7f6d3e968a65b63bfefe46751c64ad68ad88055600`; ends with LF: no):

````text
and no persistent user-bound BodyGraph rows configured in production
````

AFTER (96 bytes; SHA-256 `e21cfc7b653e51e57439facddb50871bd6608714fedfcc3ebe24eb92abde3e98`; ends with LF: no):

````text
:  
  * Mechanics and QA MUST NOT create app-like user records in prod via CLI or vendor ingest.
````

INSERT (57 bytes; SHA-256 `82081af2a3f536ed29922d3092d0f0c7c2aefc6b6fc4c19855f80773abaf890b`; ends with LF: no):

````text
 other than the two synthetic Live QA fixtures of §17.10
````

## RL-17

* Operation: `INSERT`
* Change type: CONSISTENCY
* Ledger rows: C-26 (2.15 R-1, R-6); C-30 (2.16 R-3)
* Heading path (raw original heading lines): line 3686 `# **19\) Vendor Ingest Pipeline — source policy & proofs (normative)**` > line 3688 `## **19.1 Policy (normative)**`
* Location: "Pre-Glow prod (no users)" bullet: new sub-bullet between original lines 3695 and 3696
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.15 R-1 (stored through the engine's own write path, under the Product Owner's write authorization, by an Ops task) and R-6; addendum 2.16 R-3. Repository inspection at `84d6d1c`: `audit/ops/hde-epic041/postclose-ops01/run.log` records `w_store_a` and `w_store_b` (`hdctl bg:resolve`, `rows_written=1`, `read_back_match=True`) for the two UUIDs. Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: §19.1 forbids creating app-like user records and `bg:resolve --source=vendor --upsert` in prod. The fixtures were stored through the engine's write path in production under addendum 2.15, so §19.1 needs that exception. Both prohibitions otherwise stand.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 338575, immediately after original line 3695. Neither anchor is changed.

BEFORE (78 bytes; SHA-256 `e29c0773a085abd5e43f0f37caaae50f76d22cb9231b0dec40487c53e38a806a`; ends with LF: yes):

````text
only DB/auto stub behavior and vendor dry-run semantics as described below.  

````

AFTER (39 bytes; SHA-256 `91058eb2c785d5c85adc94e7d71880bd81995bc29ccd0fb84ea1979b62789946`; ends with LF: no):

````text
* Dev. Direct vendor calls are allowed;
````

INSERT (262 bytes; SHA-256 `a21a52a936ca68d0471f34a141c5c46d6777060b15a7a2c71a2156be250aff1d`; ends with LF: yes):

````text
  * These two prohibitions do not cover storing the two synthetic Live QA fixtures of §17.10, or storing either again if it is missing. That is Ops work on the engine's own write path under the Product Owner's write authorization, not a QA or mechanics step.  

````

## RL-18

* Operation: `INSERT`
* Change type: NEW_CANON
* Ledger rows: C-01 (D-1); support C-06
* Heading path (raw original heading lines): line 4083 `# **22\) SAFE Rails and Provider Gate**`
* Location: Opening bullet list of §22: new last bullet between original lines 4090 and 4091
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.1, D-1 "Decision" (the three paths; flag scope; order; scope of one authorization; audit; error carrier), "Canon superseded or added to" and "Dependencies and unresolved obligations" (item 9 open). Supporting reading: HDE-CLI-API-Vendor-Ref §7.1.11. Repository inspection at `84d6d1c`: `engine/cli/main.py` lines 52 to 59 accept `--allow-prod-vendor` only for `bg:resolve --source vendor`. Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: §22 states the provider gate but not the production vendor override, which D-1 extends to showcompat and vendor-selecting conjunction. The bullet routes to the owner and keeps a nonclaim, because the extension is not implemented.
* Expected occurrence of the BEFORE+AFTER gap in the whole original: 1. Observed: 1 (BEFORE alone: 1; AFTER alone: 1). Original UTF-8 byte offset of the gap: 368252, immediately after original line 4090. Neither anchor is changed.

BEFORE (106 bytes; SHA-256 `fb8032f8d312ae7b7d162498c18849392e5ba4f8e3e55d3770050e4414f27b72`; ends with LF: yes):

````text
vendor transport matrices remain single-homed in HDE-Governance and HDE-CLI-API-Vendor-Ref (titles-only).

````

AFTER (56 bytes; SHA-256 `eb616aa5e6a85f366d63bee477169f77d8d3561b5409ecefa033327477dae0bd`; ends with LF: no):

````text

Conjunction resolution surfaces (SAFE rails; required).
````

INSERT (988 bytes; SHA-256 `ab68e1f6ad2020017a8d9bdf4de6934fdc3ac7c1e5ff6dff0cb16f19983ec926`; ends with LF: yes):

````text
* Production vendor override. In a production-like environment, `hdctl bg:resolve --source vendor`, `hdctl showcompat --source vendor`, and `hdctl showcompat --conjunction` whenever the invocation selects vendor acquisition for either party, acquire from the vendor only under the production vendor override `--allow-prod-vendor <AUTHORIZATION_REF>`, and each such invocation that reaches override evaluation writes one audit event before any I/O. The flag is accepted by those three paths and by no other command. One valid flag authorizes at most one acquisition per party and opens no closed rail, and every refusal makes zero outbound attempts. The flag, environment classification, matrix, order, audit event and error carrier are owned by HDE-CLI-API-Vendor-Ref §7.1.11. Implementation not claimed: current code accepts the flag only on `hdctl bg:resolve --source vendor`, and extending the gate to showcompat and conjunction belongs to an implementing change that has not landed.

````

## RL-19

* Operation: `REPLACE`
* Change type: CANON_UPDATE
* Ledger rows: C-29 (2.16 R-1, R-2)
* Heading path (raw original heading lines): line 4984 `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > line 7067 `## **37.7 CLI parity & determinism (public bytes)**`
* Location: "Two-run marker" label and its one-item list (original lines 7078 to 7080)
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.16, R-1 (GATE:CORE-DET evidence is the CI owner tests and each run of the live compat test), R-2 (the upper-case `artifacts/cards/A3/IDENTITY_OK.txt` entry retired; the lower-case a3 marker stays as it is). Repository inspection at `84d6d1c`: `tools/evidence/generate_determinism_gate_proofs.py` writes the lower-case marker ("HDE-EPIC038 PR-02 deterministic predicate evidence only"), and `tools/evidence/regenerate_identity_closure.py` lists it among the closure step's outputs (lines 90 to 96 and 233). Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets).
* Rationale: §37.7 lists the a3 marker as the two-run marker of CLI determinism. Under 2.16 R-1, GATE:CORE-DET evidence is the CI owner tests and the live compat test runs only. The marker is still generated, so the redline states its status and does not call it frozen.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [622454, 622508), original line(s) 7078–7080.

OLD (54 bytes; SHA-256 `11cea6cbcb6769479da42c7f5e359d802565b605cf97d19d9824982599a4af38`; ends with LF: no):

````text
Two-run marker:

* artifacts/cards/a3/IDENTITY\_OK.txt
````

NEW (399 bytes; SHA-256 `697ba5b86a7dd233dd6df7e04ea347d1584d65d3ab3a4dd4544d3289e22172e5`; ends with LF: no):

````text
Two-run marker (not GATE:CORE-DET evidence):

* artifacts/cards/a3/IDENTITY\_OK.txt is kept, but it is not GATE:CORE-DET evidence, and no record may cite it as current two-run identity proof. GATE:CORE-DET evidence, which covers AB↔BA and two-run identity, is the CI owner tests of the real compat path and each run of the live compat test (§1.1), as HDE-Governance and HDE-Build Notes define it.
````

## RL-20

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Ledger rows: None (DOC_HYGIENE; Nathan's direction of 2026-11-02)
* Heading path (raw original heading lines): line 1590 `# **5\) Deterministic Tie-Break & Total-Order Module \[Required-Now\]**` > line 1665 `  ## **5.8 Dev sampler HTTP harness (internal/dev-only)**`
* Location: DEV_SAMPLER_URL definition (original line 1743, one line)
* Controlling basis: PF03 Technical Writing Best Practices §7 "Revision and retention rules" (formatting repair may correct escaping when the complete source establishes the intended text) and §8 "Structure and presentation" (a redline is warranted when the source-real defect changes meaning or identity); Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets), which authorizes this hygiene. Intended text: Glow Infrastructure, `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler` (PF07 line 1227; also HDE Build Checklist Conjunction line 333).
* Rationale: The raw bytes `\\= \\/internal` render as `\= \/internal`, which drops the base-URL placeholder from a definition. The repair restores it and the plain `=`.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [177012, 177059), original line(s) 1743–1743.

OLD (47 bytes; SHA-256 `4d19f76dc9a412af9f0c9d8ca21ee4bba49b403153095b9fa5bada7fde9f0c8e`; ends with LF: no):

````text
* DEV\_SAMPLER\_URL \\= \\/internal/dev/sampler
````

NEW (56 bytes; SHA-256 `5528fd090be0fc0830e2328f094eeeee4cf536c45240e7173e094065182870a8`; ends with LF: no):

````text
* DEV\_SAMPLER\_URL = \<base\_url\>/internal/dev/sampler
````

## RL-21

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Ledger rows: None (DOC_HYGIENE; Nathan's direction of 2026-11-02)
* Heading path (raw original heading lines): line 2897 `  # **16\) Narrative Key Registry and Manifests**`
* Location: "Pack identity (routing)" list, second bullet (original line 2908)
* Controlling basis: PF03 Technical Writing Best Practices §7 "Revision and retention rules" (formatting repair may correct escaping when the complete source establishes the intended text) and §8 "Structure and presentation" (a redline is warranted when the source-real defect changes meaning or identity); Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets), which authorizes this hygiene. Intended text: HDE Narratives Guide, "Runtime (titles-only)" (PF17 line 845) and HDE Schemas & Artifacts (PF12 line 1992), `/narratives/<pack_sha>/<PACK_MEMBER>`; the previous line defines `pack_sha`.
* Rationale: The raw bytes render as `/narratives/\/\.`, which drops both path segments. The repair uses the owners' path form.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [272423, 272469), original line(s) 2908–2908.

OLD (46 bytes; SHA-256 `dd5646c9f14727ba332d1df37dffd8c03e029da0aadb1dd189918dd6504b1a7b`; ends with LF: no):

````text
immutable object storage at /narratives/\\/\\.
````

NEW (71 bytes; SHA-256 `216d01171ff33809b88dd43b2fc0f324326397a544c6b63519193dafb5aeb04d`; ends with LF: no):

````text
immutable object storage at /narratives/\<pack\_sha\>/\<PACK\_MEMBER\>.
````

## RL-22

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Ledger rows: None (DOC_HYGIENE; Nathan's direction of 2026-11-02)
* Heading path (raw original heading lines): line 4984 `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > line 4996 `  ## **37.2 Governance & homes**`
* Location: Epic close-pack filenames, conditional QA RCA, path-proof transcripts and the "Where" sentence (original lines 5016 to 5031)
* Controlling basis: PF03 Technical Writing Best Practices §7 "Revision and retention rules" (formatting repair may correct escaping when the complete source establishes the intended text) and §8 "Structure and presentation" (a redline is warranted when the source-real defect changes meaning or identity); Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets), which authorizes this hygiene. Intended text: this guide's §37.2 line 5037 (`audit/EPIC-\<NNN\>\_QA\_RCA.md`) and §37.3 (`<prefix>` is `EPIC-<NNN>`); HDE Governance and HDE Schemas & Artifacts (`audit/EPIC-<NNN>_close_report.md`, `audit/EPIC-<NNN>_MANIFEST.json`, `audit/docdeltas/hde-epic<NNN>_doc_deltas.md`).
* Rationale: Each `\\` renders as `\`, so the canonical filenames lose their epic number and the "Where" sentence defines nothing. Every `\\` in the span becomes `\<NNN\>`; nothing else changes.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [429841, 430485), original line(s) 5016–5031.

OLD (644 bytes; SHA-256 `5598906bea076d9747b4b94012cf3832e6325cf654af819fee9d95c3c36bb5e3`; ends with LF: no):

````text
* audit/EPIC-\\\_close\_report.md  
* audit/EPIC-\\\_MANIFEST.json  
* audit/docdeltas/hde-epic\\\_doc\_deltas.md

Conditional external QA RCA artifact (only when the QA RCA summary is not embedded in the close report):

* audit/EPIC-\\\_QA\_RCA.md

Close-pack path-proof transcripts (minimum required):

* audit/EPIC-\\\_close\_report.md.path\_proof.txt  
* audit/EPIC-\\\_MANIFEST.json.path\_proof.txt

These path-proof siblings MUST be produced alongside the close-pack artifacts above and are treated as placement transcripts (CI-safe scaffold checks), not as primary evidence.

Where \\ is a zero-padded 3-digit epic number (example: 022).
````

NEW (679 bytes; SHA-256 `035354f9c2568bc93d04f18ff7fb5bfae7f95506abe82404ce443babfec73ded`; ends with LF: no):

````text
* audit/EPIC-\<NNN\>\_close\_report.md  
* audit/EPIC-\<NNN\>\_MANIFEST.json  
* audit/docdeltas/hde-epic\<NNN\>\_doc\_deltas.md

Conditional external QA RCA artifact (only when the QA RCA summary is not embedded in the close report):

* audit/EPIC-\<NNN\>\_QA\_RCA.md

Close-pack path-proof transcripts (minimum required):

* audit/EPIC-\<NNN\>\_close\_report.md.path\_proof.txt  
* audit/EPIC-\<NNN\>\_MANIFEST.json.path\_proof.txt

These path-proof siblings MUST be produced alongside the close-pack artifacts above and are treated as placement transcripts (CI-safe scaffold checks), not as primary evidence.

Where \<NNN\> is a zero-padded 3-digit epic number (example: 022).
````

## RL-23

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Ledger rows: None (DOC_HYGIENE; Nathan's direction of 2026-11-02)
* Heading path (raw original heading lines): line 4984 `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > line 4996 `  ## **37.2 Governance & homes**`
* Location: "Acceptance scaffolds (epic-scoped; canonical locations)" list (original lines 5071 and 5072)
* Controlling basis: PF03 Technical Writing Best Practices §7 "Revision and retention rules" (formatting repair may correct escaping when the complete source establishes the intended text) and §8 "Structure and presentation" (a redline is warranted when the source-real defect changes meaning or identity); Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets), which authorizes this hygiene. Intended text: HDE Architecture line 119 (`docs/acceptance_map_epic<NNN>.json`) and the canonical Epic QA root `audit/qa/hde-epic<NNN>/` (HDE Schemas & Artifacts and Glow QA Guide).
* Rationale: Both canonical locations lose their epic number in rendering.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [436804, 436890), original line(s) 5071–5072.

OLD (86 bytes; SHA-256 `5cfe37b46c35158431d85909c72cf8e083bba4496c4398613e541c9043ff0758`; ends with LF: no):

````text
* audit/qa/hde-epic\\/token\_evidence\_matrix.md  
* docs/acceptance\_map\_epic\\.json
````

NEW (96 bytes; SHA-256 `c31bcda194e61a7bed72a50fca86345b754a9d17660cce3e225bd1bd3aa00a2d`; ends with LF: no):

````text
* audit/qa/hde-epic\<NNN\>/token\_evidence\_matrix.md  
* docs/acceptance\_map\_epic\<NNN\>.json
````

## RL-24

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Ledger rows: None (DOC_HYGIENE; Nathan's direction of 2026-11-02)
* Heading path (raw original heading lines): line 4984 `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > line 5112 `  ## **37.3 Conventions**`
* Location: key_outputs bullet (original line 5127): its opening path
* Controlling basis: PF03 Technical Writing Best Practices §7 "Revision and retention rules" (formatting repair may correct escaping when the complete source establishes the intended text) and §8 "Structure and presentation" (a redline is warranted when the source-real defect changes meaning or identity); Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets), which authorizes this hygiene. Intended text: as RL-22, `audit/EPIC-<NNN>_MANIFEST.json`.
* Rationale: The manifest path loses its epic number in rendering.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [441013, 441069), original line(s) 5127–5127.

OLD (56 bytes; SHA-256 `b1df6e94a9bf8f2375a156b4f603187637028aa4ec2a6f4220b7f160a3845564`; ends with LF: no):

````text
* audit/EPIC-\\\_MANIFEST.json MUST include key\_outputs
````

NEW (61 bytes; SHA-256 `599af968d591ad979b821c007df6193f5b95afdf3c1d2780309180053c95e292`; ends with LF: no):

````text
* audit/EPIC-\<NNN\>\_MANIFEST.json MUST include key\_outputs
````

## RL-25

* Operation: `REPLACE`
* Change type: DOC_HYGIENE
* Ledger rows: None (DOC_HYGIENE; Nathan's direction of 2026-11-02)
* Heading path (raw original heading lines): line 4984 `# **37\) Documentation Artifacts and Registry \[Required-Now\]**` > line 7490 `  ## **37.18 Index & synchronization**` > line 7505 `  ### **37.18.1 EPIC027 close-pack and same-run ledger refresh**`
* Location: Paragraph "Non-canonical epic-local variant (normative)" (original line 7538): its path
* Controlling basis: PF03 Technical Writing Best Practices §7 "Revision and retention rules" (formatting repair may correct escaping when the complete source establishes the intended text) and §8 "Structure and presentation" (a redline is warranted when the source-real defect changes meaning or identity); Nathan's direction of 2026-11-02 in this session, "I want you to fix the defects and inconsistencies you noticed", read with GTWPE-D3 (every eligible document is updated on context and scope, not on named drain targets), which authorizes this hygiene. Intended text: the canonical Epic QA root `audit/qa/hde-epic<NNN>/`, and HDE Phased Epics line 4377 (`audit/qa/hde-epic023/evidence_index_snapshot.json`, a concrete instance).
* Rationale: The path loses its epic number in rendering, so the rule names no file.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [655360, 655431), original line(s) 7538–7538.

OLD (71 bytes; SHA-256 `8fe1d2ed65760efd987d44bc3d766e9bad1b7de39a7922f6a300c187da61d0fb`; ends with LF: no):

````text
audit/qa/hde-epic\\/evidence\_index\_snapshot.json is non-authoritative
````

NEW (76 bytes; SHA-256 `e605751673d7fa04d4d434b7a4aeadc2c7806bf8a382b638ea2b3bf019aac35d`; ends with LF: no):

````text
audit/qa/hde-epic\<NNN\>/evidence\_index\_snapshot.json is non-authoritative
````

END OF REDLINES
