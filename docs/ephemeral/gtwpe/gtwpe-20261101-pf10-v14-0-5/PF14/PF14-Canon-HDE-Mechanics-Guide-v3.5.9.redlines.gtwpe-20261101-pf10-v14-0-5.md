# PF14 redlines: HDE Mechanics Guide v3.5.9, run gtwpe-20261101-pf10-v14-0-5

## Identity

| Field | Value |
| :---- | :---- |
| Target | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md`; in-document title `PF14-Canon-HDE-Mechanics-Guide`; version v3.5.9; git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`; 669,363 bytes; SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59`; 7,734 LF characters, so 7,735 lines, the last without a trailing LF |
| Target baseline | `origin/main` at `e2b7427ff418ca8f08f05587c4a541308a76da56`. `docs/pfcanon/` is unchanged from there to `origin/main` `84d6d1c` (read 2026-11-02) |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`; HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 1,976 lines; read at `e2b7427` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `142feb35144d8795f927e0c78b665ace52279064`; task T-05; rows C-02, C-04, C-13, C-14, C-17, C-18; uncertain C-07; supporting C-06, C-12, C-16, C-20, C-21 |
| Preparing prompt | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at step start) |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-05/prep-r1` |
| Preparer | The T-05 document session that Nathan started, in Claude Code session `https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z`; prepared 2026-11-02T00:26Z |
| Preparation outcome | `READY` |
| Proof log | `PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, beside this file |

## How to apply

* Resolve every locator against the unchanged original target. Apply all eight redlines in one pass by original position. No redline's output is another redline's locator, and no two redlines touch the same span or gap.
* Literal convention. Each literal is the exact UTF-8 text strictly between the LF that ends its opening fence line (` ````text `) and the LF immediately before its closing fence line (` ```` `). A literal that ends with a line ending therefore shows an empty line before its closing fence. Trailing spaces inside a literal are part of it. Each literal's byte length and SHA-256 are stated beside it; the fence and info string are not part of the literal.
* `REPLACE`: OLD occurs exactly once in the whole original. Replace that one span with NEW.
* `INSERT`: BEFORE immediately followed by AFTER occurs exactly once in the whole original. Insert at the boundary between them. Neither anchor is changed.
* No `FIND_AND_REPLACE` or `DELETE` operation is used.
* The original's last line has no trailing LF. No redline touches the end of the document.

## Document control (reserved for TW-APPLY-10)

No redline edits the header. The baseline header in §0.1 "Header" has this native schema:

* Title: `PF14-Canon-HDE-Mechanics-Guide` (unchanged).
* Version: `v3.5.9`, in the form `v<major>.<minor>.<patch>`.
* Status: `Canon`.
* Effective date: `2026-10-26`, in the form `YYYY-MM-DD`.
* Last Update Gate: `BN 13.8.8`, in the form `BN` followed by the HDE Build Notes version that justified the update.
* Invocation tag: `INV-f2ac55d77ce9aacc`.

Source that justifies this update, in source order: `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md` (HDE Build Notes v14.0.5). The body does not restate the document's own version or date. The target has no change log or revision-history section, and none of its rules requires a revision-history or Doc-Delta entry for this change, so no such entry is prepared. A full scan found no Draft status, placeholder, TODO or drafting note to remove.

## Index

| ID | Operation | Section | Ledger rows |
| :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE` | §1.1, "BodyGraph and loader seam posture" | C-13, C-14 (DELTA-002) |
| RL-02 | `REPLACE` | §1.1, the remediation paragraph that follows it | C-13, C-14 (DELTA-002) |
| RL-03 | `INSERT` | §1.1, request-shaping list: the single permitted version classification | C-02 (D-2) |
| RL-04 | `REPLACE` | §1.1, request-shaping list: v1 is retained legacy selection | C-02 (D-2) |
| RL-05 | `REPLACE` | §1.1, request-shaping list: the non-v2 fallback is superseded | C-02 (D-2) |
| RL-06 | `REPLACE` | §1.6.3, Epic close-run family and publication API | C-17, C-18 |
| RL-07 | `INSERT` | §27.3, attestation builder output-root ownership | C-04 (D-4) |
| RL-08 | `INSERT` | §27.5, the `--log-path` bound | C-04 (D-4) |

C-02 and DELTA-002 both change §1.1. Their spans are disjoint: DELTA-002 covers original lines 179 and 181, and C-02 covers the gap after line 214 and lines 222 and 226. The proof log gives the byte offsets.

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
* Controlling basis: HDE Build Notes v14.0.5 addendum 2.4, "Required canon drainage" (DELTA-002 covers the loader seam posture and the remediation paragraph), "Retained decisions and requirements" (C-1 generator migration, the import guard, I-1 to I-3); addendum 2.10, "Retained decisions and requirements" (residual risk FND-005: the generator still exits 2) and PSR-003. Repository inspection at `e2b7427`: `scripts/make_compat_determinism_artifacts.py` imports `adapter.chart_orchestration.load_chart` and prints `compat_public not implemented` before its chart call; `tests/charts/test_chart_loader_import_guard.py` and `tests/charts/test_chart_pure_purity.py` tracked; the entry logs `"route": "loader.load_chart"`.
* Rationale: The paragraph is a pre-delivery remediation instruction that says removal has not occurred. The replacement states the delivered caller posture, the guards and the retained limits, and keeps the PF09 nonclaim.
* Expected occurrence of OLD in the whole original: 1. Observed: 1. Original UTF-8 byte span: [15938, 16486), original line(s) 181–181.

OLD (548 bytes; SHA-256 `fad91334c374b3f720c355f57768f484b259aee6c3f266f9dc4c967e7cc1317f`; ends with LF: no):

````text
Remediation must migrate active callers, including compatibility/determinism and generator callers, to that orchestration and provide meaningful boundary tests. It must preserve existing canonical outputs and public/vendor contracts; it does not authorize fallback behavior, an Engine Core I/O exception or a second resolver. This is a required mechanics disposition, not a claim that relocation, caller migration or removal has occurred. The source proposes phased PF09 coverage separately; PF14 neither allocates its row/ID nor claims its status.
````

NEW (1035 bytes; SHA-256 `2365340a62692e3ae08d4fe92553e5208205de6f44da08c9c9f611df64869ddf`; ends with LF: no):

````text
Callers of the chart path use the Adapter entry or the pure interface. The compatibility/determinism generator `scripts/make_compat_determinism_artifacts.py` imports the Adapter entry; its compat computation is not restored, and it still exits 2 with `compat_public not implemented` before its chart call. Do not restore `engine/charts/loader.py`, add a shim for it, or put time, environment, filesystem, provider or logging access under `engine/charts/`. `tests/charts/test_chart_loader_import_guard.py` fails if the removed module path or a tracked import of it returns, and `tests/charts/test_chart_pure_purity.py` fails if `engine/charts/pure.py` gains a forbidden dependency or side effect. The boundary preserves existing canonical outputs and public/vendor contracts; it does not authorize fallback behavior, an Engine Core I/O exception or a second resolver. The route string `loader.load_chart` in the entry's log line is a label, not a module. PF14 neither allocates the related HDE-Build Checklist row nor claims its status.
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

END OF REDLINES
