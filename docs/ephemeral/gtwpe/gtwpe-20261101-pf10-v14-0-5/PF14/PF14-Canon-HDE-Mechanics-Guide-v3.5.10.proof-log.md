# Proof log: PF14 HDE Mechanics Guide v3.5.10, application of run gtwpe-20261101-pf10-v14-0-5 (T-05)

## 1. Artifact and identity

| Field | Value |
| :---- | :---- |
| Artifact this log documents | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.10.md`: the complete revised PF. In-document title `PF14-Canon-HDE-Mechanics-Guide`, version v3.5.10, effective date 2026-11-02, Last Update Gate `BN 14.0.5`. 674,636 bytes; SHA-256 `d8eea4388f13c697d19bea328da5ec6836abac02b50a633bb808fa010f34585b`; 7,748 LF characters, no trailing LF (as in the original) |
| Status of the artifact | A revised PF stored under `docs/ephemeral/`. It is not published canon: `docs/pfcanon/` is unchanged, and placing the file there is Nathan's action |
| Applying prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`, fetched live when the step began (page state 2026-10-09T11:05:22Z) |
| Application run identity | `gtwpe-20261101-pf10-v14-0-5/T-05/apply-r2`, applying package `prep-r2`. An earlier local application of `prep-r1` (`apply-r1`) was discarded unpushed when the preparer revised the package (§8) |
| Applied by | The same T-05 document session that prepared the package, Claude Code session `https://claude.ai/code/session_01Q789tzJUmD5Z4ev1Pg4q1z`, under Nathan's handoff authorizing both steps. No subagent, reviewer or other session was used |
| Application execution date | 2026-11-02 (UTC) |
| Outcome | Applied. Nine content redlines and three derived header fields. Validation, application and preservation checks all PASS (§6) |

## 2. Inputs

| Role | Identity |
| :---- | :---- |
| Original (application baseline) | `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.md`, read at `origin/main` `84d6d1c` on 2026-11-02, the same blob as the preparer's baseline at `e2b7427ff418ca8f08f05587c4a541308a76da56`: git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`; 669,363 bytes; raw-byte SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59` (compared to the same raw-byte representation). `git diff --stat e2b7427 origin/main -- docs/pfcanon/` was empty, so the original has not drifted |
| Redlines (package) | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.md`, revision r2, read from commit `ea4c6cf`: 30,050 bytes; SHA-256 `af0883ccc9366cbf7a23b0ca162c4a76df666d602f53978e848316b3f6346fff`; ends with `END OF REDLINES` |
| Preparation proof log | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF14/PF14-Canon-HDE-Mechanics-Guide-v3.5.9.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, revision r2, read from commit `ea4c6cf`: SHA-256 `88def96097a5fdd768d2a9077a5b9f440eb2b348eab5853647be12bfc366d0ba` |
| Preparer and preparation run | TW-DRAIN-10 100926.1, run `gtwpe-20261101-pf10-v14-0-5/T-05/prep-r2` (superseding `prep-r1` of `9de402f`), this same document session. Outcome `READY`; save state `COMPLETE_PACKAGE`; no unresolved or blocking item; complete target reading and complete selected-source reading recorded (preparation proof log §3) |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, HDE Build Notes v14.0.5; git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, unchanged on `origin/main` `84d6d1c`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d` |
| Selected source boundaries | 2.1 D-2 (lines 277–344) and D-4 (397–450), with 2.1 context 205–224 and 491–516; 2.2 lines 517–551 (C-07, uncertain); 2.4 (673–753, DELTA-002); 2.5 (754–883, DELTA-002 wording at l.854); 2.8 decisions and drainage table (1063–1106, 1111–1127), including the 2026-11-01 amendment. Supporting only: 2.3 (589–672), 2.7 (962–1047), 2.9 (1146–1229), 2.10 (1230–1332). These agree with Nathan's handoff and with the ledger's T-05 row |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`, pinned by the handoff at `142feb35144d8795f927e0c78b665ace52279064`; task T-05; rows C-02, C-04, C-13, C-14, C-17, C-18; uncertain C-07; supporting C-06, C-12, C-16, C-20, C-21. The current branch version adds a 2026-11-02 correction and tasks T-11 to T-18; T-05's row and selection are unchanged |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md` (read in full during preparation, same baseline) |

## 3. Applied operations and their basis

| ID | Operation and location (original) | What changed | Basis (restated from the preparation proof log) | Ledger rows |
| :---- | :---- | :---- | :---- | :---- |
| RL-01 | `REPLACE`, §1.1 "BodyGraph and loader seam posture", line 179 | The sentence calling `engine/charts/loader.py` implementation drift is replaced by the delivered boundary: the Adapter entry `adapter/chart_orchestration.py::load_chart` and the pure module `engine/charts/pure.py`; the loader removed with no shim; its legacy `load_chart(user_id)` signature retired, with `TypeError` for any other argument shape. The allocation rules that follow are unchanged | DELTA-002: HDE Build Notes 2.4 "Required canon drainage" (the loader seam posture describes a removed module); 2.5 l.854 (replace the drift sentence with the delivered boundary, "same pattern" as DELTA-001); 2.10 PF09 row-closure table (text drain only) and PSR-001 to PSR-003. Checked against the repository at `e2b7427` | C-13, C-14; support C-12, C-16, C-21 |
| RL-02 | `REPLACE`, §1.1 remediation paragraph, line 181 | The pre-delivery remediation instruction ("not a claim that relocation, caller migration or removal has occurred") is replaced by the delivered caller posture, the generator's retained exit-2 limit, the no-restore and no-shim rule, the two guard tests, the unchanged contract limits, the note that `loader.load_chart` is a log label, and the PF09 nonclaim | DELTA-002 covers "the loader seam posture and remediation paragraph" (2.4); 2.4 C-1 migration and the import guard; 2.10 FND-005 (the generator still exits 2). Checked against `scripts/make_compat_determinism_artifacts.py`, the two `tests/charts/` guards and the entry's log line | C-13, C-14; support C-12, C-16, C-21 |
| RL-03 | `INSERT`, §1.1 request-shaping list, after line 214 | New bullet: the single permitted reading of a version from the configured base is the HDE-CLI-API-Vendor-Ref §7.1.10 classification, for every resolver-selected vendor acquisition; one exact, case-sensitive comparison of the terminal segment against `v1` and `v2`, made once before any route is built; resource, payload family and credential projection from contract metadata; every other prohibition still governs; nonclaim of current conformance | 2.1 D-2 Decision ("What governs"; "The two canon rules fit together") and "Canon superseded or added to" (§1.1's "infer runtime behavior from vendor API version path strings" is added to with the single permitted classification). The nonclaim follows from item 9 being open (2.1 l.506) | C-02; support C-06 |
| RL-04 | `REPLACE`, §1.1 request-shaping list, line 222 | "until the owning architecture and byte-contract homes decide whether v1 remains a fallback or is retired" becomes "retained legacy selection, not fallback, for a configured base ending in exactly `v1`"; retirement still needs the separately versioned decision | 2.1 D-2 Decision ("The v1 path is retained legacy selection, not fallback"), Basis (the byte-contract home has decided in §7.1.10) and "Left undecided" (retirement stays a separate decision). Classified CONSISTENCY | C-02; support C-06 |
| RL-05 | `REPLACE`, §1.1 request-shaping list, line 226 | The permission for every non-v2 base to keep the legacy fallback is replaced by the terminal-`v1` posture; no other non-v2 base selects a route or reaches `bodygraphs` by fallback, governed by HDE-CLI-API-Vendor-Ref §7.1.10; the `explicit_legacy_fallback` label stays an existing wire value that makes no fallback claim | 2.1 D-2 "Canon superseded or added to" (the "Non-v2 configured bases MAY preserve" sentence is superseded), "No fallback" and "Classification label" | C-02; support C-06 |
| RL-06 | `REPLACE`, §1.6.3 close-run-family bullet, line 919 | "No Epic close-run family is admitted." is removed, and a new bullet follows the CRD bullet: Epic close-run admission through `ADMITTED_EPIC_CLOSE` (HDE-EPIC041 only, with its QA root and key prefix), the family path, and `publish_epic_close_run_family(...)` with its preconditions, writes, refusals and recovery bounds; membership and key form as for a CRD, rows carrying `epic_id` | HDE Build Notes 2.8 drainage table, HDE Mechanics Guide row ("§1.6.3 gains the close-run publication API"), and its note that the 2026-11-01 amendment's Epic close-run family is an additional drainage item; decision 7; stated limits ("An Epic close run needs its own explicit admission"). Supporting: 2.9 B-4. Checked against `tools/evidence/update_evidence_index.py` at `e2b7427` | C-17, C-18; support C-20 |
| RL-07 | `INSERT`, §27.3, after line 4443 (before "Direct source-tree execution") | New "Output-root ownership" paragraph and list: interface unchanged; exclusive atomic claim before any write; typed refusal of an unclaimable root; no added bundle member; writes only to paths the run created, with symlinks refused; failure cleanup only of what the run created; claim mechanism left to the implementing change; nonclaim of current conformance | 2.1 D-4 "Decision for the release attestation builder", "Canon superseded or added to" (§27.3 added to; the refusal list stands) and "Left undecided" | C-04; support C-06 |
| RL-08 | `INSERT`, §27.5, after line 4489 (before the nested historical heading) | New "Log-path bound (normative)" paragraph for `tools/evidence/run_sanity_pipeline.py --log-path`: inside the repository only the canonical log; outside it only a non-symlinked target with an existing parent naming a regular file or none; typed, numeric-free refusal before any step or byte; nonclaim of current conformance | 2.1 D-4 "Decision for the sanity pipeline" and "Canon superseded or added to" (§27.5 added to) | C-04; support C-06 |
| RL-09 | `INSERT`, §37.2 "CRD close-pack artifacts (canonical filenames)", inside line 5033 | New sentence after the CRD doc-delta ledger sentence: when its QA RCA summary is not embedded in the close report, the conditional external QA RCA uses the same prefix, `audit/HDE-CRD-<NNNN>_QA_RCA.md` | HDE Build Notes 2.8 drainage table, HDE Mechanics Guide row ("§37.2 epic-scoped close-pack filename list": add the CRD filename form); decision 3 (a CRD's ID is its prefix); decision 4 and the stated limit ("A bound QA RCA must be `audit/<prefix>_QA_RCA.md`, using the close report's own prefix"). The preparer added it in r2 after finding that §37.2 line 5033 represented the CRD filename form only in part | C-17 |

Rows with no PF14 change, as the preparer recorded them: C-07 (no PF14 requirement in the 2.2 l.525 scope); C-17's generator and v2 `key_outputs` rows (already represented at §37.2 line 5035 and §37.3 lines 5130–5138; its CRD filename row was partly represented at line 5033 and is completed by RL-09); C-18's Epic tracked-issue ID form (not PF14's share). Held: H-03 (DELTA-003 targets HDE State of the Repository, not a target of this ledger; it waits for the Product Owner to adopt the candidate and for a route to an eligible home).

## 4. Document-control metadata plan

Derived under TW-APPLY-10's standing header authority, validated before any edit, and included in the conflict check.

| Field | Before | After | Rule |
| :---- | :---- | :---- | :---- |
| Version | `v3.5.9` | `v3.5.10` | The final numeric component of the native `v<major>.<minor>.<patch>` version, incremented once |
| Effective date | `2026-10-26` | `2026-11-02` | The application execution date, in the native `YYYY-MM-DD` form |
| Last Update Gate | `BN 13.8.8` | `BN 14.0.5` | The one source the package records, `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`: `BN` and its version |
| Title | `PF14-Canon-HDE-Mechanics-Guide` | unchanged | Embeds no version |
| Status | `Canon` | unchanged | Not stale |
| Invocation tag | `INV-f2ac55d77ce9aacc` | unchanged | No authorization to change it |

No other field records this revision. The body restates neither the document's own version (0 occurrences of `v3.5.9` after the header) nor its date (0 occurrences of `2026-10-26`). PF14 has no change log or revision-history section and no rule requiring such an entry, and the package carries no header redline, so no duplicate authorization arises. Version, date and gate agree with one another.

## 5. Constraints and interpretations

* The package was validated afresh from its committed bytes, parsed from the saved Markdown by the stated literal convention, without the preparer's working files.
* Each locator was resolved independently against the unchanged original; application was one pass in descending original offset, with no rematching on changed text.
* Raw UTF-8 was preserved: LF line endings only (no CRLF before or after), two-space Markdown line breaks inside payloads kept, and the original's missing final LF kept.
* This step prepared no edit, improved no prose and judged no domain correctness.

## 6. Validation and verification

| Check | Result |
| :---- | :---- |
| Package integrity | Nine redlines; every literal's byte length, SHA-256 and final-LF flag equal the values printed beside it |
| Operation counts in the whole original | RL-01, RL-02, RL-04, RL-05 and RL-06: OLD occurs once. RL-03, RL-07, RL-08 and RL-09: BEFORE once, AFTER once, BEFORE+AFTER once |
| Metadata locators | `**Version:** v3.5.9  `, `**Effective date:** 2026-10-26  ` and `**Last Update Gate:** BN 13.8.8  ` each occur once, inside the §0.1 header |
| Whole-batch conflicts | None among the twelve spans and gaps (no intersecting span, no shared gap, no gap at or inside a replaced span) |
| Post-application counts | Each NEW or INSERT text occurs once in the revised PF; each replaced OLD text is absent |
| Preservation | A walk of the original in offset order confirms every untouched interval at its mapped position in the output and every payload verbatim: 667,374 untouched original bytes preserved, and 1,989 consumed by the eight replaced spans (five content `REPLACE` operations and three header lines; the four `INSERT` operations consume none) |
| Independent reconstruction | The saved redlines re-parsed and applied to the original, plus the three header values, give a byte stream equal to the saved revised PF. The body alone equals the preparer's r2 simulated revision (SHA-256 `6461608118cd62115abd309745e3061af7ee8656c6e375f74040b0b791990f52`); the only further difference is the three header lines |
| Structure | Code-fence lines 2 → 2; table rows 21 → 21; heading lines 263 → 263 (counting headings indented up to three spaces); EOF without LF, as in the original |
| Prohibited markers in the revised PF | No `TODO`, `TBD`, `FIXME`, `Draft` status, `[OMITTED`, `[SNIP`, Unicode ellipsis or three-period ellipsis |
| Save | The revised PF was written, then compared byte for byte with the computed output (`cmp`, identical). Every changed region was read back from the saved file. The whole-file comparisons above cover the rest |

These are text checks on the documents. They are not product QA, CI or governed evidence.

## 7. Unresolved items, limits and next action

* None blocks the result.
* Carried from preparation (not acted on here): the pre-existing rendered-escape damage in some PF14 placeholders (§37.2, §37.17); §9.3's compat prod gate not assessed against 2.1 D-3; and the scope question on GTWPE-D3 contextual drainage, which lists PF14 anchors bearing on 2.15, 2.16 and 2.1 D-1, D-3 and D-5 outside T-05's selection. Widening T-05 is Nathan's decision (preparation proof log §10).
* Next manual action, Nathan's: review the revised PF and, if accepted, place it as PF canon. Nathan merges the shared draft PR amthorn78/glow-hdengine-v2#826.

## 8. Application lineage

* `apply-r1` applied `prep-r1` (eight redlines) in a local commit that was never pushed. Before pushing, this session found that `prep-r1` under-represented C-17 (§37.2's CRD filename form omits the conditional external QA RCA). It discarded that local commit, returned to TW-DRAIN-10, and issued `prep-r2` (commit `ea4c6cf`).
* `apply-r2` validated `prep-r2` afresh from its committed bytes, with TW-APPLY-10 re-fetched from Notion (same version and page state), and applied it. RL-01 to RL-08 and the three header values are identical to `apply-r1`'s; RL-09 is the only content difference.
* No output of `apply-r1` exists on the shared branch.
