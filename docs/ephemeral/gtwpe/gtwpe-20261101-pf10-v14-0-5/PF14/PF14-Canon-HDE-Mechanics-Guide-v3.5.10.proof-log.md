# Proof log: PF14 HDE Mechanics Guide v3.5.10, application of run gtwpe-20261101-pf10-v14-0-5 (T-05)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md`: the complete revised PF. In-document title `PF14-Canon-HDE-Mechanics-Guide`, version v3.5.10, effective date 2026-11-02, Last Update Gate `BN 14.0.5`. 679,577 bytes; SHA-256 `7bd3ebbf193b470f0f251fb62c659b6d8b5bdcde7156395f27aff7e1ddca2c0a`; 7,750 LF characters, no trailing LF (as in the original) |
| Status of the artifact | A revised PF stored under `docs/ephemeral/`. It is not published canon: `docs/pfcanon/` is unchanged, and placing the file there is Nathan's action |
| Applying prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when the step began, again for r3 (page state 2026-10-09T11:05:22Z, unchanged) |
| Application run identity | `gtwpe-20261101-pf10-v14-0-5/T-05/apply-r3`, applying package `prep-r3`. It replaces `apply-r2`'s output (commit `6eb135d`) under the same file name (§8) |
| Applied by | The same T-05 document session that prepared the package, Claude Code session `https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z`, under Nathan's handoff authorizing both steps and his direction of 2026-11-02 that led to r3. No subagent, reviewer or other session was used |
| Application execution date | 2026-11-02 (UTC) |
| Outcome | Applied. Twenty-five content redlines and three derived header fields. Validation, application and preservation checks all PASS (§6) |

## 2. Inputs

| Role | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md`, read at `origin/main` `84d6d1cad95c67788336d174dc4b8922d9bb0cb2` on 2026-11-02, the same blob as the preparer's baseline at `e2b7427ff418ca8f08f05587c4a541308a76da56`: git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`; 669,363 bytes; raw-byte SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59` (compared to the same raw-byte representation). `git diff --stat e2b7427 origin/main -- docs/pfcanon/` was empty, so the original has not drifted |
| Redlines (package) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.md`, revision r3, read from commit `1717c69`: 71,306 bytes; SHA-256 `b67170fef2a9c2c60f1d21b125d5e219c53b9369febb2b034145b940bbf62b5c`; ends with `END OF REDLINES` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, revision r3, read from commit `1717c69`: SHA-256 `e131ec5f08e1c4a3abd72f536641527e4272cefb84c4cebbebc6105d3081eb94` |
| Preparer and preparation run | TW-DRAIN-10 100926.1, run `gtwpe-20261101-pf10-v14-0-5/T-05/prep-r3` (superseding `prep-r2` of `ea4c6cf` and `prep-r1` of `9de402f`), this same document session. Outcome `READY`; save state `COMPLETE_PACKAGE`; no blocking item; complete target reading and complete reading of the selected units recorded (preparation proof log §3). Its non-blocking items are in §7 below |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, unchanged on `origin/main` `84d6d1c`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` |
| Selected source boundaries | The handoff's selection: 2.1 D-2 (277–344) and D-4 (397–450), with context 205–224 and 491–516; 2.2 517–551 (C-07, uncertain); 2.4 (673–753); 2.5 (754–883); 2.8 (1048–1145), including the 2026-11-01 amendment. Added for r3 on Nathan's direction, under GTWPE-D3: 2.1 D-1 (225–276), D-3 (345–396) and D-5 (451–490); 2.15 (1650–1868); 2.16 (1869–1976). Supporting only: 2.3, 2.7, 2.9, 2.10 |
| Scope direction | Nathan, 2026-11-02, in this session: "I want you to fix the defects and inconsistencies you noticed". It also authorizes the formatting repairs RL-20 to RL-25 |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, pinned by the handoff at `142feb35144d8795f927e0c78b665ace52279064` and read again on the branch; task T-05; rows C-02, C-04, C-13, C-14, C-17, C-18; uncertain C-07; supporting C-06, C-12, C-16, C-20, C-21. r3 also drains C-01, C-03, C-26, C-29 and C-30 in PF14's own sections, and assesses C-05 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` (read in full during preparation, same baseline) |

## 3. Applied operations and their basis

Each basis is restated from the preparation proof log (§4, §5 and §6 there) and the redline's own rationale.

| ID | Operation and location (original) | What changed | Basis | Ledger rows |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE`, §1.1 "BodyGraph and loader seam posture", line 179 | The drift sentence about `engine/charts/loader.py` becomes the delivered boundary: Adapter entry `adapter/chart_orchestration.py::load_chart`, pure module `engine/charts/pure.py`, loader removed with no shim, legacy signature retired. The allocation rules that follow are unchanged | DELTA-002: HDE Build Notes 2.4 "Required canon drainage"; 2.5 l.854; 2.10 PF09 row-closure table and PSR-001 to PSR-003. Repository checked | C-13, C-14; support C-12, C-16, C-21 |
| RL-02 | `REPLACE`, §1.1 remediation paragraph, line 181 | The pre-delivery remediation instruction becomes the delivered caller posture; the generator still exits 2 and is retired as GATE:CORE-DET evidence, kept with its exit-2 test as history; no restore and no shim; the two guard tests; the unchanged contract limits; `loader.load_chart` is a log label; the PF09 nonclaim | DELTA-002 (2.4); 2.4 C-1 and the import guard; 2.10 FND-005; 2.16 R-2 (added in r3) | C-13, C-14, C-29; support C-12, C-16, C-21 |
| RL-03 | `INSERT`, §1.1 request-shaping list, after line 214 | The single permitted version classification under HDE-CLI-API-Vendor-Ref §7.1.10, with a nonclaim | 2.1 D-2 "Decision" and "Canon superseded or added to"; item 9 open | C-02; support C-06 |
| RL-04 | `REPLACE`, §1.1, line 222 | v1 is retained legacy selection, not fallback; retirement needs a separately versioned decision | 2.1 D-2 "Decision", "Basis", "Left undecided" | C-02; support C-06 |
| RL-05 | `REPLACE`, §1.1, line 226 | The terminal-`v1` posture replaces the permission for every non-v2 base; the `explicit_legacy_fallback` label makes no fallback claim | 2.1 D-2 "Canon superseded or added to", "No fallback", "Classification label" | C-02; support C-06 |
| RL-06 | `REPLACE`, §1.6.3, line 919 | "No Epic close-run family is admitted." gives way to a bullet on Epic close-run admission (`ADMITTED_EPIC_CLOSE`, HDE-EPIC041 only) and `publish_epic_close_run_family` | 2.8 drainage table row and note; decision 7; stated limits; 2.9 B-4. Repository checked | C-17, C-18; support C-20 |
| RL-07 | `INSERT`, §27.3, after line 4443 | "Output-root ownership" rules for the attestation builder, with a nonclaim | 2.1 D-4 builder decision | C-04; support C-06 |
| RL-08 | `INSERT`, §27.5, after line 4489 | "Log-path bound (normative)" for `--log-path`, with a nonclaim | 2.1 D-4 sanity-pipeline decision | C-04; support C-06 |
| RL-09 | `INSERT`, §37.2, inside line 5033 | The CRD form of the conditional external QA RCA, `audit/HDE-CRD-<NNNN>_QA_RCA.md` | 2.8 drainage table row; decisions 3 and 4; stated limit | C-17 |
| RL-10 | `REPLACE`, §1.1 "Production/user-surface open-rails proof posture", line 257 | Every Epic's QA plan includes and its run executes the live compat test (`hdctl showcompat --source vendor`, step-local open rails, synthetic data, plus the deployed-service check), whatever the Epic changed; an Epic touching production surfaces adds its own live test; only a recorded Product Owner waiver sets either aside; what does not discharge it; a test that cannot run is `TOOLING_BLOCKED`; QA without it is closed-rails QA; ownership of predicates, waiver form, naming and stage enforcement routed | 2.15 R-1 to R-6 and "Relation to other canon" (supersedes the dependency on touching a production surface). The paragraph had let an explicit exemption discharge the test | C-26; support C-30 |
| RL-11 | `INSERT`, §1.6.3 regression list, inside line 1160 | Governed Epic close-run admission limited to `ADMITTED_EPIC_CLOSE`, with an unadmitted Epic or a CRD configuration refused by the Epic entrypoint, which names the admitted set | 2.8 amendment and stated limit; 2.9 B-4. The refusal and its test exist on `main` | C-18; support C-20 |
| RL-12 | `REPLACE`, §9.3 "Prod gate (hard)", line 2275 | The compat namespace's dev/admin environment gate: production-like posture 404; otherwise served only under `APP_ENV` exactly `dev`, `test` or `local`, else 403 `ERR_WRITER_FORBIDDEN`; `ENGINE_ENV` never admits; no credential while admitted that way; a later decision before wider exposure; routed to HDE-CLI-API-Vendor-Ref §5.5 and HDE-Governance §4.1.4; nonclaim, because current code refuses only the production-like posture | 2.1 D-3 "Decision", "Canon superseded or added to", and item 9 open | C-03; support C-06 |
| RL-13 | `REPLACE`, §17.10 status, line 3166 | The scope condition excepts the two synthetic Live QA fixtures | 2.15 R-1; 2.16 R-3 | C-26, C-30 |
| RL-14 | `REPLACE`, §17.10 assumptions, line 3171 | SYN-A and SYN-B by UUID; permanent QA fixtures, not app users; stored only through the engine's write path under the Product Owner's write authorization, as Ops work; the deployed-service check reads only them and is `TOOLING_BLOCKED` while either is missing | 2.15 R-1, R-5, R-6; 2.16 R-3 | C-26, C-30 |
| RL-15 | `INSERT`, §17.10.5, end of line 3407 | The live compat test and its deployed-service check are not a requirement that the no-user mode blocks | 2.15 R-1 | C-26 |
| RL-16 | `INSERT`, §19.1, inside line 3693 | The pre-Glow scope condition excepts the two fixtures | 2.15 R-1; 2.16 R-3 | C-26, C-30 |
| RL-17 | `INSERT`, §19.1, after line 3695 | The two pre-Glow prohibitions do not cover storing the fixtures, which is Ops work under the Product Owner's write authorization | 2.15 R-1, R-6; 2.16 R-3; the POSTCLOSE-OPS01 run log | C-26, C-30 |
| RL-18 | `INSERT`, §22, after line 4090 | The production vendor override for `bg:resolve --source vendor`, `showcompat --source vendor` and vendor-selecting conjunction, routed to HDE-CLI-API-Vendor-Ref §7.1.11; nonclaim, because only `bg:resolve` accepts the flag today | 2.1 D-1 "Decision", "Canon superseded or added to", and item 9 open | C-01; support C-06 |
| RL-19 | `REPLACE`, §37.7, lines 7078–7080 | The a3 two-run marker is kept but is not GATE:CORE-DET evidence, and no record may cite it as current two-run identity proof; GATE:CORE-DET evidence is the CI owner tests and each live compat test run | 2.16 R-1 and R-2. The marker is still written by a current generator, so the redline does not call it frozen | C-29 |
| RL-20 | `REPLACE`, §5.8, line 1743 | `DEV_SAMPLER_URL = <base_url>/internal/dev/sampler` restored | Formatting repair (PF03 §7 and §8; Nathan's direction); intended text from Glow Infrastructure | None |
| RL-21 | `REPLACE`, §16, line 2908 | `/narratives/<pack_sha>/<PACK_MEMBER>` restored | Formatting repair; intended text from HDE Narratives Guide and HDE Schemas & Artifacts | None |
| RL-22 | `REPLACE`, §37.2, lines 5016–5031 | `<NNN>` restored in the Epic close-pack filenames, the conditional QA RCA, the path proofs and the "Where" sentence | Formatting repair; intended text from §37.2 line 5037, §37.3, HDE Governance and HDE Schemas & Artifacts | None |
| RL-23 | `REPLACE`, §37.2, lines 5071–5072 | `<NNN>` restored in the token matrix and acceptance map locations | Formatting repair; intended text from HDE Architecture line 119 and the canonical Epic QA root | None |
| RL-24 | `REPLACE`, §37.3, line 5127 | `<NNN>` restored in the manifest path | Formatting repair; as RL-22 | None |
| RL-25 | `REPLACE`, §37.18.1, line 7538 | `<NNN>` restored in the epic-local snapshot path | Formatting repair; the canonical Epic QA root and HDE Phased Epics line 4377 | None |

Rows with no PF14 change, as the preparer recorded them: C-05 (PF14 states no rule on gate check-row content); C-07 (no PF14 requirement in the 2.2 l.525 scope); C-17's generator and v2 `key_outputs` rows (already represented at §37.2 line 5035 and §37.3 lines 5130–5138); C-18's Epic tracked-issue ID form (not PF14's share). Held: H-03 (DELTA-003 targets HDE State of the Repository, not a target of this ledger). The Product Owner's CCR-5 ruling of 2026-11-02 needs no PF14 change: PF14 states no close-pack ordering.

## 4. Document-control metadata plan

Derived under TW-APPLY-10's standing header authority, validated before any edit, and included in the conflict check.

| Field | Before | After | Rule |
| :---- | :---- | :---- | :---- |
| Version | `v3.5.9` | `v3.5.10` | The final numeric component of the native `v<major>.<minor>.<patch>` version, incremented once from the original |
| Effective date | `2026-10-26` | `2026-11-02` | The application execution date, in the native `YYYY-MM-DD` form |
| Last Update Gate | `BN 13.8.8` | `BN 14.0.5` | The one source the package records, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`: `BN` and its version. Nathan's direction is a scope decision, not a source file |
| Title | `PF14-Canon-HDE-Mechanics-Guide` | unchanged | Embeds no version |
| Status | `Canon` | unchanged | Not stale |
| Invocation tag | `INV-f2ac55d77ce9aacc` | unchanged | No authorization to change it |

The version is derived from the unchanged original, so replacing `apply-r2`'s output does not bump it twice. No other field records this revision. The body restates neither the document's own version (0 occurrences of `v3.5.9` in the revised PF) nor its date (0 occurrences of `2026-10-26`). PF14 has no change log or revision-history section and no rule requiring such an entry, and the package carries no header redline. Version, date and gate agree with one another.

## 5. Constraints and interpretations

* The package was validated afresh from its committed bytes, parsed from the saved Markdown by the stated literal convention, without the preparer's working files.
* Each locator was resolved independently against the unchanged original; application was one pass in descending original offset, with no rematching on changed text.
* Raw UTF-8 was preserved: LF line endings only (no CRLF before or after), two-space Markdown line breaks inside payloads kept, backslashes in payloads kept as bytes, and the original's missing final LF kept.
* `<NNN>`, `<base_url>`, `<pack_sha>` and `<PACK_MEMBER>` are pattern variables in canonical path forms, not drafting placeholders.
* This step prepared no edit, improved no prose and judged no domain correctness.

## 6. Validation and verification

| Check | Result |
| :---- | :---- |
| Package integrity | Twenty-five redlines; every literal's byte length, SHA-256 and final-LF flag equal the values printed beside it |
| Operation counts in the whole original | Sixteen `REPLACE` (RL-01, RL-02, RL-04 to RL-06, RL-10, RL-12 to RL-14, RL-19 to RL-25): OLD occurs once. Nine `INSERT` (RL-03, RL-07 to RL-09, RL-11, RL-15 to RL-18): BEFORE once, AFTER once, BEFORE+AFTER once |
| Metadata locators | `**Version:** v3.5.9  `, `**Effective date:** 2026-10-26  ` and `**Last Update Gate:** BN 13.8.8  ` each occur once, inside the §0.1 header |
| Whole-batch conflicts | None among the twenty-eight spans and gaps (no intersecting span, no shared gap, no gap at or inside a replaced span) |
| Post-application counts | Each NEW or INSERT text occurs once in the revised PF; each replaced OLD text is absent |
| Preservation | A walk of the original in offset order confirms every untouched interval at its mapped position in the output and every payload verbatim: 665,289 untouched original bytes preserved, and 4,074 consumed by the nineteen replaced spans (sixteen content `REPLACE` operations and three header lines; the nine `INSERT` operations consume none). 665,289 + 4,074 = 669,363 |
| Independent reconstruction | The saved redlines re-parsed and applied to the original, plus the three header values, give a byte stream equal to the saved revised PF. The body alone equals the preparer's r3 simulated revision (SHA-256 `4442694b4b664cd807940fafe67c6845ab073efff77ece88b335cd6bc9b1cd15`); the only further difference is the three header lines |
| Structure | Code-fence lines 2 → 2; table rows 21 → 21; heading lines 263 → 263 (counting headings indented up to three spaces); EOF without LF, as in the original |
| Prohibited markers in the revised PF | No `TODO`, `TBD`, `FIXME`, `Draft` status, `[OMITTED`, `[SNIP`, Unicode ellipsis or three-period ellipsis |
| Save | The revised PF was written, then compared byte for byte with the computed output (`cmp`, identical) |

These are text checks on the documents. They are not product QA, CI or governed evidence.

## 7. Unresolved items, limits and next action

* None blocks the result.
* Carried from preparation, for Nathan (preparation proof log §10):
  * §37.17 "Snapshot root" (original line 7488) keeps its lost path segments. No source establishes the intended path, so it was not repaired.
  * HDE Build Notes 2.16 calls the a3 marker "frozen", but `tools/evidence/generate_determinism_gate_proofs.py` still writes it as a step of the release identity closure. Whether 2.16's fact needs a correction is Nathan's question; RL-19 does not depend on it.
  * HDE Architecture and HDE Narratives Guide name the narrative pack path's second segment differently (`<OBJECT_KEY>`, `<PACK_MEMBER>`).
* The nonclaims in RL-03, RL-07, RL-08, RL-12 and RL-18 stand until the implementing change (Candidate CRD Items List item 9) lands.
* Next manual action, Nathan's: review the revised PF and, if accepted, place it as PF canon. Nathan merges the shared draft PR amthorn78/glow-hdengine-v2#826.

## 8. Application lineage

* `apply-r1` applied `prep-r1` (eight redlines) in a local commit that was never pushed, and was discarded when the preparer issued `prep-r2`.
* `apply-r2` applied `prep-r2` (nine redlines) in commit `6eb135d`, producing this file name with SHA-256 `d8eea4388f13c697d19bea328da5ec6836abac02b50a633bb808fa010f34585b`. It was never placed in `docs/pfcanon/`.
* After `apply-r2`, Nathan directed this session to fix the defects and inconsistencies it had reported. The preparer issued `prep-r3` (commit `1717c69`).
* `apply-r3` validated `prep-r3` afresh from its committed bytes, with TW-APPLY-10 re-fetched from Notion (same version and page state), and applied it to the unchanged v3.5.9 original. It replaces `apply-r2`'s file under the same name. RL-01 and RL-03 to RL-09 and the three header values are identical to `apply-r2`'s; RL-02's new sentence and RL-10 to RL-25 are the content differences.
