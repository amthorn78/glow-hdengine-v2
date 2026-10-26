# T-PF14 — proof log for the revised PF14 from v3.5.8

This is the application report for `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf14/PF14-from-v3.5.8.md`. It records how the revised PF was produced from the validated redlines and what was verified. The revised PF is not authoritative publication: `docs/pfcanon/` is unchanged, and adopting the text as canon is Nathan's manual action. This report establishes no QA, acceptance, canon adoption or closure.

## 1. Identity

| Field | Value |
| :- | :- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf14/PF14-from-v3.5.8.md`: `PF14-Canon-HDE-Mechanics-Guide` v3.5.9, 669,363 bytes, 7,734 LF characters (7,735 lines; no final LF, as in the original), git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`, SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59` |
| Outcome | Apply `SUCCESS`; 11 package operations and 3 document-control fields applied; save `COMPLETE_PACKAGE` (§7) |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b, fetched live in this session (page state as of 2026-10-09T11:05:22Z; matches the ledger's pin) |
| Authorization | Nathan's T-PF14 handoff, which authorizes TW-DRAIN-10 and then TW-APPLY-10 in this one document session |
| Applier | TW-APPLY-10 in the Nathan-started T-PF14 document session, Claude Code cloud session https://claude.ai/code/session_017fZuKCTMJn4EwZYu5ENvh1 |
| Execution date | 2026-10-26 (UTC) |
| Run | `gtwpe-20261026-pf10-v13-8-8/T-PF14`, applying preparation revision `P1` |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` (routing record at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7`), task `T-PF14`, rows A06, A07, A10, A15, A26, X07 |
| Destination | branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, shared draft PR [#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761) |

## 2. Inputs and their verification

Original (application baseline). `docs/pfcanon/PF14-Canon-HDE-Mechanics-Guide-v3.5.8.md`, `PF14-Canon-HDE-Mechanics-Guide` v3.5.8, read from `origin/main` `0838ba08254eaefc888019df49a06aa2ae99cc6c`: blob `3360a9eb1a5056274a31ad36739df8b04a4864c3`, 663,440 bytes, SHA-256 `0fb34a6534f685eb7abeeaab43e848f02e780d903507a597cee669678257b63a`. These raw-byte identities equal the preparer's baseline, recorded at `9dda63dd3f05f496c3ff67e95da78550d3950c5a`. Immediately before Apply, `origin/main` was re-fetched and was still `0838ba0`, with the same PF14 blob and only one PF14 file, so there is no baseline drift. The complete reading the preparer recorded was against this same verified baseline, and Apply reuses it. Its 15 line windows covered all 663,440 bytes, as the redlines proof log §2 records.

Package. Both files were read from commit `315b3aa` on the destination branch:

* `redlines-PF14-from-v3.5.8.md`: 37,476 bytes, SHA-256 `ea1c20e710d149bc5c5fa3af1a3f353f1c2708fa6b5c47de8019a079ee84f6d3`;
* `redlines-PF14-from-v3.5.8.proof-log.md`: 22,937 bytes, SHA-256 `f570adcc169e22fb9f69ae6b23643ce9bc9ccba3179063d86e477cb6e5003eeb`.

Both were read in full. Preparation state verified from them:

* originating preparer: TW-DRAIN-10 100926.1 in this same session; run `gtwpe-20261026-pf10-v13-8-8/T-PF14`, revision `P1`;
* preparation outcome `READY`, save completeness `COMPLETE_PACKAGE` (proof log §9);
* complete target reading, and complete reading of the selected units;
* no unresolved or blocking item;
* held items H-01 and H-03 deliberately not drafted; no other held item touched.

Selected incoming scope, checked against the handoff and the ledger's T-PF14 row: PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`). The units are:

* front matter, lines 1–223;
* 2.6, lines 531–687;
* 2.7, lines 688–889;
* 2.10, lines 1102–1204;
* 2.15, lines 1620–1690;
* 2.26, lines 2900–2986;
* the supporting cross-references X03, X04, X06 and X07, at the ledger's boundaries.

These are the same units the preparer read; Apply did not re-triage the source.

## 3. Whole-batch validation before any output byte

An Apply script, separate from the preparer's, parsed the package from the committed bytes alone. It found RL-001 to RL-011, each with an accepted operation spelling: nine `REPLACE` and two `INSERT`. Every literal's stated byte count and SHA-256 matched. Against the unchanged original:

| ID | Op | Expected | Observed |
| :- | :- | :- | :- |
| RL-001 | REPLACE | 1 | 1 |
| RL-002 | REPLACE | 1 | 1 |
| RL-003 | INSERT | 1 / 1 / 1 | BEFORE 1, AFTER 1, pair 1 |
| RL-004 | REPLACE | 1 | 1 |
| RL-005 | REPLACE | 1 | 1 |
| RL-006 | REPLACE | 1 | 1 |
| RL-007 | REPLACE | 1 | 1 |
| RL-008 | REPLACE | 1 | 1 |
| RL-009 | REPLACE | 1 | 1 |
| RL-010 | INSERT | 1 / 1 / 1 | BEFORE 1, AFTER 1, pair 1 |
| RL-011 | REPLACE | 1 | 1 |

The package and the metadata plan in §4 together form one original-bound edit plan. It has no intersecting or touching replaced spans, no insertion at or inside a replaced span, and no two insertions at one gap. No package operation touches the document-control header, so no header redline needed reconciling. The RL-045 rule is not engaged: the package uses no `FIND_AND_REPLACE`. Every member validated, so the batch was applied whole.

## 4. Document-control plan

The plan was derived under TW-APPLY-10's "Deterministic final document-control header" and validated before application. Each field was located by its exact original line, occurring once inside header lines 5–10.

| Field | Before | After | Basis |
| :- | :- | :- | :- |
| `**Version:**` | `v3.5.8` | `v3.5.9` | One increment of the final component of the dotted numeric version |
| `**Effective date:**` | `2026-10-09` | `2026-10-26` | The actual application date, in the native `YYYY-MM-DD` form |
| `**Last Update Gate:**` | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | `BN 13.8.8` | The one source that justified this update, as the package records it: PF10 file `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, version 13.8.8. The supporting cross-references are not change sources (ledger "Source register") |
| `**Status:**` | `Canon` | unchanged | Not stale; the document remains Canon |
| `**Title:**`, `**Invocation tag:**` | unchanged | unchanged | Outside the plan's authority |

Each line keeps its label, order and trailing hard-break spaces. No other line of the original restates the version or the effective date: `3.5.8` and `2026-10-09` each occurred once, in the header, and the revised PF contains `v3.5.9` once and `3.5.8` nowhere. PF14 has no change log or revision-history section and no rule that requires one, so no change-history entry exists to agree with. Version, date and gate agree.

## 5. Applied operations and their basis

The operations were applied in descending original order, with no rematching against changed text. Byte offsets are into the original.

| ID | Original bytes | Revised lines | Basis (preparer's rationale, condensed) and source-ledger reference |
| :- | :- | :- | :- |
| RL-001 | 100806–101221 | 913 | §1.6.3 limited updater admission to HDE-CRD-0001; the code admits HDE-CRD-0001 and HDE-CRD-0002 through the source-owned `ADMITTED_CRD_QA` table. The bullet now states the table as the admission set, each CRD with its own row, and refuses any CRD outside it. Ledger row A26: PF10 2.26 FND-040, "Required canon drainage" |
| RL-002 | 101693–102116 | 915 | States both admitted roots with their Human Index key prefixes and the key forms by prefix, keeping the HDE-CRD-0001 keys as examples. Row A26: 2.26 FND-040 ("with roots and Index keys") |
| RL-003 | gap at 103329 | 919–920 | Two new bullets. First, the close-run family's publication API `publish_crd_close_run_family`: path, rendering, refusal before writing, whole-family replacement in one transaction, no manifest or `checks/` write, `close/`-only membership exception, Index keys, no Epic family. Rows A15 with X03: 2.15 "The close-run evidence family (introduced)"; the ADR canon table, "§1.6.3 gains the close-run publication API"; ADR Decision item 7; 2.17 keeps the family. Second, Step-0B for a CRD: the capture goes in the indexed check primary under Plan Templates' Step-0B rules, and the draft ledger is a close-stage causal input. Row X07: CR-11 decided (a) as changed, with HDE Mechanics Guide §1.6.3 as its drainage target; 2.35 lists CR-11 among canon drainage items |
| RL-004 | 124701–125077 | 1160 | The regression responsibility restated the old rule ("governed admission limited to 0001"); it now names the `ADMITTED_CRD_QA` set and refusal by name in both entrypoints. Row A26: FND-040, consistency |
| RL-005 | 413933–414101 | 4917 | §34 route table: `/api/reader` is the production Reader v1 and v2 `POST` surface (§9.2), mounted under `/api` by every factory; it is not an alias of `/reader`, consistent with HDE-CLI-API-Vendor-Ref §5.4 "Production mount". Rows A07 with X04: 2.7 "its route table's /api/reader alias row"; WU-PR-03 plan v2.0 §18 |
| RL-006 | 415768–415899 | 4932 | Drops the conditional "After the runner is hardened to the required profile", now satisfied. Rows A07 (AD-3) and A10: consistency |
| RL-007 | 416011–416230 | 4938 | Replaces the caution that the command was no claim about the loopback bind; the command stays a documentation contract, and the posture is a separate observation. Rows A07 (AD-3) and A10: consistency |
| RL-008 | 417089–418296 | 4946–4953 | §34 "Current repository posture" re-inspected at `0838ba0`, every bullet restated from the bytes. The bullets cover: the helper; the loopback run call with explicit `debug`/`use_debugger`/`use_reloader`; no CORS reference, with tests that assert its absence; the exact `APP_ENV=dev` gate; the production-like posture's refusal of the dev-harness and retired routes; and the catalog's 18 records. The bullets make no claim that the tests pass, about router-level answers (H-03) or about catalog conformance. Rows A06 (2.6), A07 with X04 (2.7) and A10 with X06 (2.10; WU-PR-05 plan §19, "the production mount of the dev routes") |
| RL-009 | 426411–426857 | 5031–5035 | §37.2 gains the CRD close-pack filename form, `audit/HDE-CRD-<NNNN>_close_report.md` and `audit/HDE-CRD-<NNNN>_MANIFEST.json`, each with its updater-written path proof, and the directory form. The generic v2 generator `tools/qa/generate_epic_close_pack.py` is named beside the EPIC-025 entrypoint, with its CLI and publication properties. Rows A15 with X03: the ADR canon table's two §37.2 rows; 2.15 "What is approved"; ADR Decision items 2 and 3 |
| RL-010 | gap at 436191 | 5130–5139 | §37.3 gains the v2 `key_outputs` minimum (`close_report`, `close_manifest`, `doc_deltas`, `drain_targets`, `qa_step_logs_manifest`) and the rule that every other key output is a bound tracked input (`OUTPUT_BINDING_MISMATCH`). Rows A15 with X03: the ADR table's "§37.3 key_outputs rule"; ADR Decision item 5; 2.15 C-4 (R-3) |
| RL-011 | 663389–663440 | 7735 | Removes the two empty list items at the end of the document; the last real item keeps its text. Hygiene authorized by TW-DRAIN-10's rule on placeholders and drafting markers; PF03 §14 |

## 6. Preservation and output checks

These are text checks, not product QA.

* Exact reconstruction. The script rebuilt the expected revised text from the original's 15 untouched intervals, carried byte for byte, interleaved with the 14 planned payloads in original order. The revised bytes equal that reconstruction. Untouched content totals 658,328 characters and replaced content 3,610, together the whole original of 661,938 characters (663,440 bytes). Each payload sits exactly at its planned output offset.
* Cross-check with the preparer. With the three header fields reverted, the revised text has SHA-256 `6c9964c8abcb19b65a9948134e10af87a0491e255c24af46c32fc7dfde8f7acc`. This equals the result both preparer-side simulations recorded in the redlines proof log §6.
* Diff audit. A line diff against the original shows exactly 13 hunks: header lines 6 and 8–9, then lines 913, 915, 918 (insertion), 1158, 4915, 4930, 4936, 4944–4951, 5031 (with RL-009's added paragraph), 5124 (insertion) and 7721–7723. Nothing else changed.
* End of file. The original ended without a final LF on a list line, and so does the revised PF, after RL-011.
* Structure. The heading count is unchanged. The §34 route table keeps its header and six rows, and §37.3's EPIC023 and EPIC024 blocks follow the new paragraph unchanged.
* Markers. The revised PF has no TODO, TBD, FIXME or "Draft" status marker (the one "Draft" is the JSON Schema dialect name "Draft 2020-12" in §2.2), no empty list item and no CR. No applied payload contains an ASCII three-period ellipsis or the Unicode ellipsis.
* Status. `Canon` is the right value for the revised Canon document, so it was left unchanged.

## 7. Save verification

The revised PF was written once to its repository path; that name did not exist before this run. It was then read back completely by script. The saved file is byte-identical to the audited output: SHA-256 `d5635c43d46035ca99fb99dd80c11881562f1c50366ab7cc0b6fa2d42d0b7d59`, git blob `a1d394f17f0cab627bda5746e65bcfa22eca5946`, 669,363 bytes. Its header lines 5–10 and the changed §34 region (lines 4912–4956) were also inspected directly. This proof log was read back in full after it was saved, and this section again after this sentence was set. Both required outputs exist and are verified, so the package is `COMPLETE_PACKAGE`.

## 8. Limitations and next action

* The revised PF records static repository facts at `0838ba0` in §34, and names that commit in the posture heading. It makes no claim about runtime, QA, deployment or test outcomes.
* Pre-existing rendering loss in the target, such as lost angle-bracket placeholders in some Epic filename patterns, is carried unchanged. No input establishes the lost text.
* Observation for Nathan, not drafted (outside T-PF14's rows). §5.8's illustrative runner `python -m adapter.http_reader --bind 127.0.0.1:5000`, at original line 1737, no longer matches the runner. The runner takes no `--bind` option and binds `127.0.0.1` on `PORT`, default `8000`. The text already labels the example illustrative only.
* Next manual action: Nathan reviews the revised PF and the package in shared draft PR [#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761), merges it when the document sessions are done, and transfers the revised PF into `docs/pfcanon/` as canon if he accepts it. No agent writes `docs/pfcanon/`.
