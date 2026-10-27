# Scope measurement — MODIFICATION-20261027-gcfpe-backlog-open-items

Every figure in the record is broad match minus named exceptions, with the remainder read in context (`SCOPE-001`, `ecosystem-change-management.md` §2 step 2). This file holds the method, the patterns and the counts. It holds no prompt-body text beyond what the record quotes (`prompt-corpus-policy.md`: the minimum task-specific evidence, never a corpus by accumulation).

## 1. Corpus sweep

Three read-only sweep workers (lanes LA, LB, LC; brief in `worker-brief.md`) fetched every page once on 2026-10-27, live, from Notion: the 55 members of `GCFPE-20261009.1` / `100926.1` (URLs from the approved registry `GCFPE-PCR-20261009.1`) and PE Metaprompt 100926.1. 56 of 56 fetched; 0 failures. Method per page: FILE (the harness saved the result; regexes run by script on the extracted `<content>`) 7, INLINE (applied by reading) 49. Each family was applied case-insensitively, line by line. A worker also reported any in-scope line no family caught (the escape hatch): 202 such lines.

| Family | Measures | Pattern |
|---|---|---|
| F1 | handoff package (MB-010) | `input package\|native input package\|handoff package\|handoffs? carr(y\|ies)\|complete [^.\n]{0,40}package` |
| F2 | provenance clause (MB-025) | `provenance\|GCFPE_PROMPT_PROVENANCE\|docs/changes` |
| F3 | Codex / security review (MB-024) | `codex\|security[ -]reviews?` |
| F4 | PF10 addendum numbering (MB-007, MB-009) | `allocat\|addendum number\|next (continuous )?number\|numbering\|numbers? (the\|an\|its\|each) addend` |
| F5 | predecessor release ids (MB-011) | `20260914\|20260913\|091426\|091326` |
| F6 | commit-authorization default (MB-022) | `explicitly authori[sz]ed\|commit (grant\|scope\|authori)\|uncommitted\|scratch (clone\|storage\|director)\|evidence commit` |
| F7 | finding, real-input and business-case vocabulary (MB-013 to MB-019, MB-023) | `business case\|real[- ]inputs?\|constructed input\|cost ceiling\|\bceiling\b\|\bP1\b\|emulat\|fidelity\|repeated[- ]class\|same class` |
| F8 | numbered PF10 addendum citation (stale since PF10 v13.8.9) | `addend(um\|a)\s+2\.\d+\|PF10[^.\n]{0,60}\b2\.\d+\b` |
| F9 | closure / close pack (MB-027, MB-030) | `close[- ]pack\|close mutation\|CL-05\|close[- ]candidate\|DO_NOT_CLOSE\|close[- ]run` |

### Matching lines per page

| Page | Method | F1 | F2 | F3 | F4 | F5 | F6 | F7 | F8 | F9 |
|---|---|---|---|---|---|---|---|---|---|---|
| CF-C-10 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CF-C-20 | INLINE | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CF-C-30 | INLINE | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| CF-C-40 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CF-E-10 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CF-E-20 | INLINE | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CF-E-30 | INLINE | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| CF-E-40 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| CF-PO-10 | INLINE | 0 | 1 | 0 | 2 | 0 | 0 | 0 | 0 | 0 |
| CL-20 | INLINE | 0 | 5 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
| CL-30 | INLINE | 0 | 4 | 0 | 2 | 0 | 0 | 1 | 0 | 0 |
| CL-40 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| CL-C-10 | INLINE | 0 | 4 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| CL-E-10 | INLINE | 0 | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 3 |
| CL-E-20 | INLINE | 0 | 3 | 0 | 2 | 0 | 0 | 2 | 0 | 0 |
| CL-E-30 | INLINE | 0 | 3 | 0 | 2 | 0 | 0 | 2 | 0 | 0 |
| CL-E-40 | INLINE | 0 | 3 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| DOC-10 | INLINE | 1 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| DOC-20 | INLINE | 1 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| ESC-10 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| ESC-25 | INLINE | 1 | 4 | 0 | 1 | 0 | 1 | 2 | 0 | 0 |
| ESC-30 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| ESC-40 | INLINE | 0 | 3 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| GCFPE-MGMT-10 | INLINE | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| IA-10 | INLINE | 2 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| IA-20 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| IA-30 | INLINE | 0 | 2 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| IA-40 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| IA-50 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| IA-60 | INLINE | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| MGR-10 | INLINE | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| OPS-10 | FILE | 1 | 4 | 0 | 0 | 0 | 7 | 0 | 0 | 0 |
| OPS-20 | INLINE | 2 | 4 | 0 | 0 | 0 | 2 | 0 | 0 | 0 |
| OPS-30 | FILE | 10 | 4 | 0 | 0 | 0 | 3 | 1 | 0 | 0 |
| PE-METAPROMPT | FILE | 0 | 5 | 0 | 5 | 5 | 7 | 4 | 0 | 0 |
| PR-10 | FILE | 5 | 5 | 1 | 0 | 0 | 1 | 1 | 0 | 0 |
| PR-20 | FILE | 11 | 5 | 2 | 0 | 0 | 1 | 1 | 0 | 0 |
| PR-30 | INLINE | 2 | 4 | 1 | 0 | 0 | 2 | 1 | 0 | 0 |
| PR-35 | INLINE | 1 | 4 | 2 | 0 | 0 | 1 | 0 | 0 | 0 |
| PR-40 | FILE | 8 | 4 | 1 | 0 | 0 | 2 | 1 | 0 | 0 |
| PR-50 | INLINE | 0 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| QA-10 | FILE | 11 | 4 | 0 | 2 | 0 | 2 | 2 | 0 | 0 |
| QA-100 | INLINE | 0 | 5 | 0 | 0 | 0 | 2 | 2 | 0 | 0 |
| QA-110 | INLINE | 0 | 4 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| QA-120 | INLINE | 0 | 4 | 0 | 0 | 0 | 0 | 2 | 0 | 1 |
| QA-20 | INLINE | 1 | 4 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| QA-50 | INLINE | 0 | 5 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| QA-60 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| QA-70 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| QA-80 | INLINE | 0 | 3 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| QA-90 | INLINE | 0 | 5 | 0 | 0 | 0 | 0 | 2 | 0 | 0 |
| RS-10 | INLINE | 1 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| RS-20 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| RS-30 | INLINE | 0 | 4 | 0 | 1 | 0 | 0 | 2 | 0 | 0 |
| RS-40 | INLINE | 0 | 2 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| UTIL-10 | INLINE | 0 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
| **Total lines** | | **63** | **168** | **8** | **34** | **5** | **33** | **57** | **0** | **7** |
| **Pages with a hit** | | **20** | **55** | **6** | **25** | **1** | **14** | **32** | **0** | **3** |

## 2. MB-010: the handoff-package sentence family (D23-B)

All counts in this section are computed by script from the sweep returns, with duplicate lines (a line reported both as a hit and as an escape-hatch line) counted once.

**Broad match:** every F1 line plus every escape-hatch line a worker tagged as the same family: **234 distinct lines on 44 pages.**

**Subtracted as permitted (139 lines):**
- 31 lines that already say the artifacts hold the rest (the D23-B wording);
- 108 lines that name artifacts by repository path, describe a destination or role continuity (which D27 permits), or matched only on an unrelated word (for example the producers' addendum-number sentence).

**Contradicting D23-B: 95 lines on 23 pages.** A line counts when it tells an agent that a handoff or package carries lineage, session identity, manual prerequisites, recovery context, branch or commit, or a "complete native input package", which D23-B ("restates nothing the named prompt, canon or files hold") and D27 *Continuity* reverse:
- 82 lines by that test, applied by script;
- 13 lines that restate artifact or session content in other words, found by the coordinator reading the 121 non-matching lines in context, and matched back by exact prefix.

| Page | Contradicting lines | | Page | Contradicting lines |
|---|---|---|---|---|
| QA-10 | 19 | | MGR-10 | 2 |
| PR-40 | 13 | | QA-60 | 2 |
| PR-20 | 12 | | QA-80 | 2 |
| OPS-30 | 10 | | DOC-20 | 1 |
| PR-10 | 7 | | IA-20 | 1 |
| CL-20 | 3 | | IA-30 | 1 |
| CL-30 | 3 | | OPS-10 | 1 |
| CL-40 | 3 | | OPS-20 | 1 |
| PR-30 | 3 | | QA-120 | 1 |
| PR-35 | 3 | | QA-50 | 1 |
| QA-20 | 3 | | RS-10 | 1 |
| IA-10 | 2 | |  |  |

The backlog entry named 9 lines on 5 pages (PR-10, PR-20, PR-30, PR-40, OPS-20). PLAN fixes each anchor on a fresh read; a page whose lines all prove conformant on that read drops out with its reason (D26-E).

## 3. Measured scope per item

| Entry | Method | Measured scope |
|---|---|---|
| MB-001 | every graph edge whose `to` is PR-40 across 55 parts (3), minus D23-E's sanctioned entries (`observed_merge_edges` and the fallback) | 1 edge (`DOC-20.json` `landed_lineage_review`), 1 body bullet (DOC-20 *Result routing*) |
| MB-002 | REJECT, "PR owner" and "in-scope findings" over the whole PR-20 and PR-10 bodies, minus rescope REJECT sentences and PR-20's own D23-F re-plan entry | 1 line, PR-20 |
| MB-004 | `git grep` on `main` for the procedure's name and title, minus dated records; register fetch | 1 stale pointer (v5.0.0:37) plus 2 stale values in the same file (front-matter release, line 39 graph token); 1 register binding |
| MB-005 | `freeze.py`; `git grep` for both digests; filesystem search for the 11-file tree | 1 installed tree (10 files, `c518ccb0…`); 0 copies of the 11-file tree here; 0 §10 verdicts naming either digest; DN-E E1 (2026-10-11) binds `c518ccb0` for qualification |
| MB-006 | the template read whole; filled briefs on `main` checked for a Canon relied on line | 2 sites in the second template (§1, §6); the same omission in the first template's §10, and §1's stale "D20-D26"; 30 of 37 filled briefs add the block by hand |
| MB-007 | every PE sentence with `number*`/`allocat*`/`renumber*` and `addend*`/PF10/canon (4), minus the two no-field sentences | 2 sentences in PE |
| MB-009 | the numbering sentence in each qualifying producer, plus `continuous addendum number` in PE and the graph parts | 6 producer bodies, 1 PE sentence, 1 `global.json` field |
| MB-010 | §2 above | 95 lines on 23 pages |
| MB-011 | PE whole body for the four predecessor literals and "this repair", minus front-matter provenance | 3 passages (the entry) plus 2 repair-scoped passages naming no release literal |
| MB-012 | the Hub whole text: lines naming 091426.1 or GCFPE-20260914.1 outside historical-labelled sections, then the numbering and drainage texts | 4 sections, 1 paragraph and 3 lines (the entry), plus 2 un-versioned workspace-wide texts on the Hub and the same paragraph on the release register |
| MB-013 / MB-023 | functional: every surface that tells a PR-phase session to classify, resolve or gate on review findings; `P1\|P0` over the PR-lane bodies and all installed skills; F7 corpus-wide | PR-35 (steps 3–4, readiness gate); RS-40 (its PR-35 section); PR-20 (its description of PR-35); PR-40 (no P1 check); 0 pages carry "real input", "constructed input" or "P1" (F7) |
| MB-014 | the skill read whole; broad match on finding-disposition text, minus rescope-only and non-PR lines | 4 `SKILL.md` lines (90, 91, 96, 105) and 4 `behavior-cases.md` lines (7, 17, 41, 91); change-flow `SKILL.md:317` restates the rule |
| MB-015 to MB-017 | business/benefit/measure/warrant/ceiling vocabulary over each named body; "business case" corpus-wide (F7) | 0 business-case criteria in CF-C-30, CF-E-30, IA-30, PR-10; 0 pages say "business case" |
| MB-016, MB-017, MB-018 (plan-side rules) | emulation/fidelity/pin/precondition/boundary/refusal vocabulary over IA-30, PR-10, PR-20 | 1 line (PR-20 step 7 "boundary cases"); 0 real-input-set, refusal, pin or precondition rules |
| MB-019 | business/measure/spend/ceiling over PR-30 and PR-40 | 0 measure lines |
| MB-020 | every target of a graph edge whose state is a reviewer denial or redline, then each redline-applying prompt's unapplicable-redline outcome | 8 redline-applying prompts: 1 returns terminally (IA-40); 3 return with a handoff (CF-C-40, CF-E-40, UTIL-10); 4 have no such outcome |
| MB-021 | `output_artifacts` of all 55 parts for QA_PLAN and DELTA; the QA-lane bodies | 0 prompts author an approved-QA-Plan change; 7 bodies route or refuse one (QA-50, QA-60, QA-70, QA-80, QA-90, QA-110, ESC-40) |
| MB-022 | every `commit` and evidence-permission line in the seven QA-lane bodies; F6 corpus-wide | 5 lines in QA-100 (3), QA-90 (1), QA-50 (1); the OPS lane carries its own commit-scope default (OPS-10, OPS-20, OPS-30), outside this item |
| MB-024 | `codex` and `security review` over every installed skill and every page (F3) | 1 skill line (`glow-hde-pr-development` `SKILL.md:90`); 0 pages name Codex (the 8 F3 lines are generic "code/security review") |
| MB-025 | F2 corpus-wide; `docs/changes/` on `main`; `docs/ephemeral` for the PENDING row | 168 lines on 55 pages (every runtime body and PE; not GCFPE-MGMT-10); `GCFPE_PROMPT_PROVENANCE.md` absent; 220 of 233 records naming it carry the PENDING row |
| MB-026 | the brief's six causes and six requests against QA-50, QA-70, QA-80 | causes R1–R5 present, R6 resolved; requests 1–5 open, 6 met |
| MB-027 / MB-030 | by script over 55 parts: every edge into CL-C-10 or CL-E-10 and every `DO_NOT_CLOSE` branch; graph, `global.json` and registry for close-pack terms (0 hits) | 2 edges to retarget, ≥ 2 branches and 1 node (≥ 3 out-edges) to add, 1 `global.json` field; 3 members changed and 1 added; R1 GCF-24 → GCF-25; change-flow and flowmaster-validate pins; ≥ 9 candidate-text defects from its first run, and 2 passages the PF10 drain made stale |
| MB-028 | GTWPE decision record and handoffs; GTWPE-MGMT-10 100726.1, the TW selection page, the GTWPE iteration page; PE general rules | GTWPE already applies the rule in practice (3 TW releases); 1 PE general-rule section silent on unchanged members |
| MB-029 | installed skills for any relay-safety output; canon on model guidance | **unmeasured**: "relay safety" is defined nowhere, so its surfaces cannot be bounded |

## 4. Evidence verification (coordinator, after the returns)

- **Repository and canon quotes:** 240 of 240 match their source. 238 matched programmatically as file text; the 2 command outputs (a `closure.py` line and a SHA-256) were re-run and match.
- **Notion quotes:** 52 of 166 also appear, character for character after markup normalisation, in an independent sweeper's extraction of the same page; 0 conflict where they overlap.
- **Decisive sentences re-read by the coordinator** on fresh fetches: PR-20 (MB-002, MB-010), QA-70 and QA-80 (MB-021, MB-026), the Glow Operations Hub (MB-012), and the CL-05 candidate (MB-030).
- **Routing claims confirmed from the graph parts:** MB-001, MB-020, MB-021, MB-030.
- **Absences confirmed by the corpus sweep (F2, F3, F7, F8):** MB-013, MB-015 to MB-018, MB-023, MB-024.
- **The remaining Notion quotes rest on the verifier's verbatim capture.** No quote that a check could reach was found altered.
