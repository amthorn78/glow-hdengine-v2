# Proof log — revised PF19 from v3.0.6 (gtwpe-20261026-pf10-v13-8-8, T-PF19)

This proof log documents how the revised PF19 file was created. It is the TW-APPLY-10 application report. The revised PF19 is a working file under `docs/ephemeral/`, not an authoritative publication: `docs/pfcanon/` was not written, and canon transfer is the Product Owner's manual action. Nothing here establishes QA, acceptance, canon adoption or closure.

## 1. Artifact and outcome

| Field | Value |
| --- | --- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf19/PF19-from-v3.0.6.md` |
| Artifact identity | PF19-Canon-Glow-QA-Guide v3.0.7; 682,678 bytes; 5,622 LF lines; no CR; SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; Git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b` |
| Outcome | Application SUCCESS: six content operations and the derived document-control plan applied, every verification passed |
| Prompt | TW-APPLY-10 — Apply Validated Redlines — 100926.1, https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b (fetched live on 2026-10-26; page last edited 2026-10-09T11:05:22Z), the version and page the handoff and the ledger's "Prompt pins" name |
| Run identity | `gtwpe-20261026-pf10-v13-8-8/T-PF19/apply-run-1` |
| Applier | The same Claude Code cloud session as the preparer, https://claude.ai/code/session_01UYxoWoyzGiVWTbkVFR3TqE. The handoff authorizes preparation then application in this session; each step ran under its own fetched prompt. No subagent or other session took part |
| Execution date | 2026-10-26 (UTC, from the container clock) |
| Destination | Branch `docs/20261026-gtwpe-pf10-v13-8-8-documents`, shared draft PR [#761](https://github.com/amthorn78/glow-hdengine-v2/pull/761) |

## 2. Inputs and identities

| Input | Identity | How it was obtained |
| --- | --- | --- |
| Exact original (baseline) | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`, v3.0.6; blob `1d86fdb495d49ae85efae9ec53aa9a9968905122`; raw-byte SHA-256 `1a005db7ffbe5626163afdaf9a62bfc10dd57725c36b5fc6097be15ed7c9c639`; 679,140 bytes; 5,613 lines | `git show origin/main:<path>` at `0838ba08254eaefc888019df49a06aa2ae99cc6c`, re-fetched immediately before application; same raw-byte SHA-256 as the preparer's evidence, so there is no drift |
| Redlines package | `pf19/redlines-PF19-from-v3.0.6.md`; blob `5e5ff1bf6a302c1d8f7d058316ac7761ef79c723`; SHA-256 `50c2c05457e749e42526406557caa09867ff3acf48519b2b948f2e9b3afc7f34` | Read from the pushed branch head `b4cdb11` with `git show`, not from the working tree |
| Preparation evidence | `pf19/redlines-PF19-from-v3.0.6.proof-log.md`; blob `8dbb1bbd804b25c9d692d2dba3f2de03b2e929a4`; SHA-256 `bc1333ba2ddf856bf2ca436f31428112d95bc50e62492d7d8107757a0a52d4d5` | Same commit; read in full |
| Selected sources | HDE Build Notes v13.8.8 (`PF10-HDE-Build-Notes-v13.8.8.md`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): addenda 2.15, 2.16, 2.28, 2.30 and 2.31 (with 2.17 and 2.18 for supersession) and front matter lines 1–223. `HDE-CRD-0002-specification-v1.1-approved.md` S-APR, lines 147–193, overlaid by delta 01 C-8 to C-12 | Recorded in the package §1; this step read them in this session (they were read in full during preparation) and confirmed the package's decisions against them |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`; task T-PF19; rows A15, A16, A28, A30, A31 and S-APR, with X03 and X08 | Verified against the handoff: same target, rows and sections |

## 3. Preparation-state verification

- **Preparer and run.** Originating preparer: this session; preparation run `gtwpe-20261026-pf10-v13-8-8/T-PF19/drain-run-1`.
- **States.** Preparation outcome `READY`; save completeness `COMPLETE_PACKAGE` (preparer proof log §11). No unresolved item, no blocking dependency and no held change is drafted. H-02 is held and absent from the package.
- **Coverage.** The package records complete target reading (all 5,613 lines) and complete reading of each selected unit with its boundaries.
- **Package form.** Ends `END OF REDLINES`. Each literal's fenced and JSON-escaped forms agree, and each matches its recorded SHA-256; the package was parsed independently from the pushed bytes.
- **Baseline match.** The baseline is matched by raw-byte SHA-256 against the same byte representation the preparer used.

## 4. Operation validation (before any output byte was written)

| ID | Op | Check | Result |
| --- | --- | --- | --- |
| RL-01 | INSERT | BEFORE and AFTER anchors each occur once; BEFORE ends where AFTER starts | Pass; gap at offset 52419 (baseline line 517) |
| RL-02 | INSERT | same | Pass; gap at offset 75977 (line 724) |
| RL-03 | INSERT | same | Pass; gap at offset 78334 (line 738) |
| RL-04 | REPLACE | old block occurs once; new differs | Pass; span 83507–83551 (line 777) |
| RL-05 | INSERT | same as RL-01 | Pass; gap at offset 128831 (line 1119) |
| RL-06 | INSERT | same as RL-01 | Pass; gap at offset 130960 (line 1139) |
| All | — | every heading-path line occurs once; no `FIND AND REPLACE`, so RL-045 does not apply; no CR; no ellipsis in any payload | Pass |
| Batch | — | gaps distinct; no gap at or inside a replaced span; no anchor intersects a replaced span; the header spans (offsets 101–277) intersect no content operation | Pass |

## 5. Document-control plan (derived, then applied)

| Field | Baseline value | Revised value | Rule applied |
| --- | --- | --- | --- |
| `**Version:**` (line 7) | `v3.0.6` | `v3.0.7` | Final numeric component of the dotted version incremented once; `v` prefix and three components kept |
| `**Effective date:**` (line 8) | `2026-10-09` | `2026-10-26` | Actual application date, native `YYYY-MM-DD` |
| `**Last Update Gate:**` (line 9) | `BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md` | `BN 13.8.8; HDE-CRD-0002-specification-v1.1-approved.md` | Sources that justified the update, in the package's recorded source order, separated by `; `: the PF10 file as `BN` and its version, then the Specification's filename. No PF document other than PF10 is a source. The redlines file's own name is not used |
| `**Status:**` (line 6) | `Canon` | unchanged | The document's own rules keep it Canon; nothing is stale |
| `**Title:**`, `**Invocation tag:**` | unchanged | unchanged | Not document-control fields this plan may change |

- **Header integrity.** The header is `## **0.1 Header**`, lines 3 to 10. Each field label occurs exactly once in the document. Labels, order, bold markers and the two trailing spaces on lines 5 to 9 are preserved.
- **Internal restatements.** The only occurrences of `3.0.6` and `2026-10-09` are the header lines themselves; after application neither string remains.
- **Change or revision history entry.** None is required by PF19's own rules: §12.1 sets no per-revision entry, and §13 is an event-bounded record of selected changes. The package carries none, and none disagrees with the derived values.
- **Draft, placeholder and stale-status language.** None introduced. The marker-pattern count is unchanged from the baseline, where the hits are rule text canon requires there.
- **Header redline in the package.** None, so there is no duplicate authorization to reconcile.

## 6. Applied operations and their basis

Each operation was applied once, in descending offset order, against the unchanged original.

| ID | What it changes | Basis (the preparer's source-ledger reference) | Rationale (the preparer's) |
| --- | --- | --- | --- |
| RL-01 | §3.1.3 gains a paragraph after its first: the close mutation set (close pack, its two ledgers, same-run close evidence, Index and Mirror registration) is outside the post-closure drainage rule. It is produced after a final QA Report with verdict PASS, or after a `DO_NOT_CLOSE` decision whose return work is that set, and lands by the Product Owner's merge before the closure decision. It is a closure prerequisite; permanent PF drainage is not. It is routed to HDE Build Notes and Change Process Guide | Ledger row A31; HDE Build Notes v13.8.8 addendum 2.31 "Required canon drainage" (Glow QA Guide §3.1.3), rule 4 (entries, exit, ownership) and "Relationship to existing HDE Build Notes guidance" | Without it a reader could treat the close mutation set as post-closure administration |
| RL-02 | §3.4.3 gains "Evidence persistence (normative)": QA evidence is persisted in the repository and is never left only in temporary or scratch storage | Ledger rows A28 and A30 with X08; addendum 2.28 "Required canon drainage" (PO-5 to Glow QA Guide §3.4.3), carried by 2.30; rule text X08 §3 E-1 | §3.4.3 placed evidence at governed paths without stating that it must be persisted; E-2 is not a PF19 rule |
| RL-03 | The §3.4.3 path-grammar table gains a row, after "Auxiliary check output", for post-verdict close-run evidence of an admitted CRD: `audit/qa/<crd-id>/close/<check_id>/primary.log` with its path proof; canonical updater only; outside the step-logs manifest; membership exception for `close/` only, with §4.4.2 continuing to govern `checks/`; no Epic family | Ledger row A15 with X03; addendum 2.15 "The close-run evidence family (introduced)"; ADR canon row for Glow QA Guide §3.4.3; 2.17 leaves the family unchanged | The table is the approved-destination list and denies any recurring family not introduced by PF10; this family is so introduced |
| RL-04 | §3.4.3 approved-exceptions item 5 names the close-run family under `audit/qa/<crd-id>/close/` | Ledger row A15 with X03; addendum 2.15; ADR §3.4.3 row | The list is closed ("limited to"); consistency with RL-03 |
| RL-05 | "Close-pack truthfulness and same-run execution" gains a paragraph: for an admitted CRD the home of same-run close evidence is the close-run family under `audit/qa/<crd-id>/close/`, published after the final QA verdict without reopening the approved QA manifest; no Epic family is admitted | Ledger rows A15 and A16 with X03 and S-APR; ADR canon row for the close-pack sections; addenda 2.15 and 2.16 "Required canon drainage"; Specification v1.1 S-APR (S21: where close-workflow run evidence lives) | The paragraph required same-run evidence but named no CRD home |
| RL-06 | "Close report requirements" gains a paragraph: the requirements apply to a CRD close report; the generic close-pack writer renders the verbatim heading and the pointer list from a `close_candidate_source.v2` source; for a CRD the close-run root is a required pointer; the writer, schema and paths of record are routed to their owners | Ledger rows A15 and A16 with X03 and S-APR; ADR canon row for the close-pack sections and Decision 3 and 4; addendum 2.15 "What is approved"; 2.16; Specification v1.1 S-APR (S21: which writer produces the close report); repository facts at `0838ba0` (preparer proof log §8) | The requirement named only an Epic report and no producer |

## 7. Unchanged-content and structure verification

- **Reconstruction.** The output equals the stream rebuilt from the untouched original intervals and the nine payloads (six content, three header) in ascending order.
- **Untouched intervals.** Every original interval outside the nine edit spans and gaps appears unchanged, at its shifted position, in the output.
- **Edit locations.** Each content operation appears exactly once in the output: each insertion as BEFORE anchor, payload and AFTER anchor in contiguous sequence; RL-04's new line present once and its old line absent.
- **Independent diff.** POSIX `diff baseline revised` reports exactly these hunks: `7,9c7,9` (header), `516a517,518` (RL-01), `723a726,727` (RL-02), `737a742` (RL-03), `777c782` (RL-04), `1118a1124,1125` (RL-05) and `1137a1145,1146` (RL-06). It removes 4 lines and adds 13, so 5,613 + 9 = 5,622 lines.
- **Structure.** Heading lines are identical in text and order (none added or removed). The count of code-fence lines is unchanged. The new table row has the same number of `|` separators as its neighbours.
- **EOF and bytes.** The final two LF bytes are unchanged, and the last 2,000 bytes are byte-identical to the baseline's. There are no CR bytes and no ASCII or Unicode ellipsis.
- **Byte accounting.** 679,140 baseline bytes + 3,581 content bytes − 43 header bytes = 682,678 bytes. The content-only figure, 682,721, matches the preparer's simulation (preparer proof log §9).

## 8. Tooling and recovery record

- **Tools.** Application ran in Python 3 under `-I` in the session scratchpad: `parse.py`, which parses the pushed package, and `apply.py`, which validates, derives the header plan, applies in one pass and verifies. They are working files and are not committed.
- **Correction.** The first `apply.py` run stopped before writing any output: its duplicate-header-label guard built the label prefix incorrectly and found no label lines (`APPLY_INVALID: header field version: 1 matches, 0 label lines`). That was a defect in the applier script, not in the package or the baseline. The guard was corrected to use explicit label prefixes and the run was repeated once; the package and baseline bytes were unchanged between the runs, and no partial output was produced.

## 9. Limits and nonclaims

- The revised PF19 is a ready-to-transfer working copy. It changes no file under `docs/pfcanon/`; adopting it as canon is the Product Owner's manual transfer.
- The text checks above are document checks, not product QA. Repository facts cited in RL-06 were inspected statically and prove no CI, QA, acceptance or deployment.
- Other document tasks drain the same addenda into Change Process Guide, HDE Schemas & Artifacts, HDE Mechanics Guide, HDE Governance and Plan Templates. PF19 routes to those homes by title, and HDE Build Notes stays the governing source until they are drained.

## 10. Save and completion receipt

Both outputs were read back in full from the working tree of `docs/20261026-gtwpe-pf10-v13-8-8-documents` on 2026-10-26, before commit, and verified:

- **Revised PF19.** Every stored byte was read: SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`, 682,678 bytes, 5,622 lines, valid UTF-8, no CR and no ellipsis. A second, independent run of the application on the same pushed package and baseline produced a byte-identical file (`cmp` silent), and POSIX `diff` against the baseline reported the seven hunks in §7 and nothing else.
- **This proof log.** Read in full before this receipt was added, then read back again after it. Its own final hash is given in the final response and the ledger's T-PF19 cell.
- **Application outcome.** SUCCESS, both required outputs saved. No diagnostic file was needed.
- **Next manual action (Nathan).** Review the revised PF19 on shared draft PR #761, merge it when ready, and transfer the revised PF19 into `docs/pfcanon/` as his own action if he adopts it. No agent writes canon, merges or transfers.
- **Commit.** The commit that holds both outputs is given in the final response; recording it here would be self-referential.
