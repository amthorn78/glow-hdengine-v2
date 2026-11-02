# Proof log — PF19 redlines — gtwpe-20261101-pf10-v14-0-5 (T-06)

This is the processing report for `PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.md`, in this directory. It records how that redlines file was made, what it changes and why, and what was checked. It describes preparation revision 2; §11 records revision 1 and why it was superseded.

## 1. Artifact and outcome

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF19/PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Artifact identity at save | 25,238 bytes; SHA-256 `480d35dcbca1916e04208212103fb02dbe334a082285577997c85664150c83e2`; git blob `d68aa9bf5fa83d5d3622f2c333ca66925cab29f6` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5`, task T-06, preparation revision 2 |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff` (fetched live at the start of this step; page state 2026-10-09T11:05:22.139Z), run in the Claude Code session Nathan started for T-06 on 2026-11-02. No subagent, reviewer or other session was used. |
| Preparation outcome | `READY` |
| Save state | `COMPLETE_PACKAGE` (see §10) |
| Redlines | Ten, RL-01 to RL-10, all `REPLACE` of one whole baseline line each |
| Next step | TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`), in this same session, as Nathan's handoff authorizes |

## 2. Sources and inputs

| Role | Identity | Reading |
| :---- | :---- | :---- |
| Target (original baseline) | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.7.md`, in-document title PF19-Canon-Glow-QA-Guide, Status Canon, v3.0.7, effective 2026-10-26. Git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b`; SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; 682,678 bytes; 5,622 lines. Scope anchor §0.2 "Purpose & scope". | Complete; see §3 |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, PF10-HDE-Build-Notes v14.0.5, effective 2026.11.01. Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines. One unlettered logical version. | Selected units complete; see §3 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, v1.8.8. Git blob `504712df548a02f3aa4e7b8c37027385e46a3878`; SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`; 633 lines | Complete (lines 1–300 and 301–633) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`. The handoff's identity is commit `142feb35144d8795f927e0c78b665ace52279064`. It was re-read at `aef3266a0cd180405db363465f69ec2efdb1417b` (blob `f43c7241e5bc9da35a9693ae8b35c2821c2d7b16`), where the T-06 task row and rows C-07, C-17, C-18, C-26 and C-29 are unchanged and the 2026-11-02 correction and §8 apply. Task row T-06; assigned rows C-17, C-18, C-26; uncertain C-07, C-29; supporting C-20, C-30 | Complete. Planning and provenance only, not a change source |
| Decision record | `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`, GTWPE-D3, "Every PF10 addendum is drained, and a prompt in the run evaluates the drain targets" (lines 114–160), in particular Nathan's 2026-10-07 ruling, "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target" | Read in full for the D3 section |
| Handoff | Nathan's T-06 handoff of 2026-11-01 (inline control fields: target, rows, unit boundaries, held items H-06 and H-08, branch, output paths, authorized Drain-then-Apply sequence) | Applied |

Baseline and currency. All canon was read from `origin/main`. The handoff baseline is `e2b7427ff418ca8f08f05587c4a541308a76da56`. At this step `origin/main` was `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`. `git diff --stat e2b7427 origin/main -- docs/pfcanon/` is empty, and the two intervening commits (#824, #825) change only `docs/ephemeral/`. The blobs above are identical at both commits, so the target and source baseline is unchanged.

Selected source units, each read completely:

* 2.8, lines 1063–1106 (retained decisions 1 to 9, dependency direction, alternatives, stated limits, Epic-only inventory) and 1111–1127 (required canon drainage table and the 2026-11-01 amendment note). Rows C-17, C-18.
* 2.15, lines 1650–1804 (status, R-1 to R-6). Row C-26.
* 2.2, lines 517–551 (status, the l.525 precedence scope, R-1 to R-3). Row C-07, uncertain. Lines 552–588 were also read as the rest of the unit.
* 2.16, lines 1869–1939 (status, R-1, R-2). Row C-29, uncertain. Lines 1940–1976 were also read as the rest of the unit.

Supporting reading only, not drain scope: 2.8 lines 1048–1062, 1107–1110 and 1128–1145; 2.9 lines 1146–1229 (row C-20); 2.15 lines 1805–1868; 2.16 R-3 lines 1940–1948 (row C-30). PF10 line 922 was read only to identify the held CCR-6 tension (H-08).

## 3. Coverage

Target: read completely, in eighteen contiguous windows, with byte counts recorded and summing to the file size (682,678 bytes):

| Window | Lines | Bytes |
| :---- | :---- | :---- |
| 1 | 1–392 | 38,023 |
| 2 | 393–716 | 38,087 |
| 3 | 717–1034 | 38,101 |
| 4 | 1035–1344 | 38,032 |
| 5 | 1345–1622 | 38,028 |
| 6 | 1623–2018 | 38,159 |
| 7 | 2019–2638 | 38,142 |
| 8 | 2639–3064 | 38,087 |
| 9 | 3065–3510 | 38,009 |
| 10 | 3511–3831 | 38,246 |
| 11 | 3832–4187 | 38,273 |
| 12 | 4188–4504 | 38,070 |
| 13 | 4505–4744 | 38,172 |
| 14 | 4745–4880 | 38,016 |
| 15 | 4881–5014 | 38,072 |
| 16 | 5015–5134 | 38,115 |
| 17 | 5135–5280 | 38,078 |
| 18 | 5281–5622 | 34,968 |

A heading map (269 headings) and literal searches were run over the whole file with a local script. No window ended mid-unit.

Source: each selected and supporting unit was read through its stated boundary in these windows, with byte counts recorded: lines 517–588 (10,943 bytes); 1048–1062 (10,253); 1063–1086 (10,696); 1087–1106 (9,270); 1107–1145 (5,939); 1146–1195 (21,738); 1196–1229 (4,728); 1650–1730 (6,573); 1731–1868 (8,673); 1869–1976 (8,408).

## 4. Repository inspection (read-only)

Current-repository statements in the redlines rest on direct read-only inspection of `origin/main` `84d6d1ca`, which is identical to `e2b7427` outside `docs/ephemeral/`:

* `tools/evidence/update_evidence_index.py` lines 62–64: `ADMITTED_EPIC_CLOSE` holds one entry, `"HDE-EPIC041": ("audit/qa/hde-epic041", "audit.qa.hde_epic041")`. This supports "HDE-EPIC041 is the first Epic admitted" (RL-05, RL-07).
* `audit/qa/hde-epic041/close/` holds nine `primary.log` files, each with its `primary.log.path_proof.txt`. This supports the example `hde-epic041` (RL-05).
* `tools/qa/generate_epic_close_pack.py` lines 2635–2655: the change's own close-run directory `audit/qa/<change-id>/close/` is a required pointer only for a CRD, and it may be recorded before it exists; every other pointer must resolve. This supports RL-08.
* `audit/EPIC-041_close_report.md` line 16 lists the pointer `audit/qa/hde-epic041/close/`.
* `docs/run/EPIC011_TEST_IDENTITIES.md` lines 34–49 and `engine/bodygraph/ingest.py` lines 32–41 register SYN-A (`9cff60ae-6eb6-5618-aec5-8acaa4f290d2`, 1990-01-01, 12:00, Amsterdam, Netherlands) and SYN-B (`57f0c055-ff09-5fdb-aedb-def880437e6f`, 1985-07-15, 08:30, London, United Kingdom). `audit/ops/hde-epic041/postclose-ops01/run.log` lines 32 and 34 record one stored row each, with `read_back_match=True`. This supports RL-09.

## 5. Change and disposition ledger

Every change in the selected units is listed with its disposition. Under GTWPE-D3, a change goes into PF19 wherever it bears on PF19 in context and scope, whether or not the addendum names PF19 as a drain target. "No PF19 home" therefore means a whole-target reading found no PF19 text on the subject. Where that is so, the owning document is named, together with the ledger task that drains it.

### 5.1 Row C-17 — close-pack writer ADR, PF19 share (2.8 lines 1063–1106, 1111–1126)

| Source item | Disposition | Supporting location |
| :---- | :---- | :---- |
| Drainage row "Glow QA Guide — Close-pack truthfulness and Close report requirements": name the CRD close-run home of same-run close evidence | Already represented | Baseline l.1124 ("For a CRD that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/`") |
| Same row: the v2 writer's rendering of the verbatim heading and the pointer list | Already represented | Baseline l.1146 ("The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD") |
| Drainage row "Glow QA Guide — §3.4.3": name `audit/qa/<change-dir>/close/` beside `checks/` as the post-verdict close-run family | Already represented for a CRD | Baseline l.742 (path-grammar row) and l.782 (approved exception 5) |
| Decision 1, v2 source schema | No PF19 home beyond the existing mention at l.1146. Owners: Change Process Guide, HDE Schemas & Artifacts (T-03, T-04) | l.1146 |
| Decision 2, one writer | No PF19 home beyond l.1146. Owners: HDE Mechanics Guide, Change Process Guide (T-05, T-03) | l.1146 |
| Decision 3, paths of record | No PF19 home; PF19 cites only examples (l.1132, l.1146). Owners: HDE Schemas & Artifacts, HDE Governance, HDE Mechanics Guide | l.1132, l.1146 |
| Decision 4, v2 report contents | PF19 share is the heading and pointer list, already at l.1146. Its QA-side closeout accounting (§9.2.15.5, §9.2.15.6) covers a different artifact, the final QA closeout review, and is unaffected. The rest belongs to Change Process Guide and HDE Governance (T-03, T-01) | l.1146, l.3886–l.3919 |
| Decision 5, v2 manifest `key_outputs` | No PF19 home; l.3691 already routes manifest bindings to their schema. Owners: HDE Schemas & Artifacts, HDE Mechanics Guide, HDE Governance | l.3691 |
| Decision 6, feedback freedom | No PF19 home. Owners: HDE Schemas & Artifacts, HDE Mechanics Guide | None |
| Decision 7, post-verdict close-run family | CRD part already represented (l.742, l.782, l.1124). Epic part: see C-18 | l.742, l.782, l.1124 |
| Decision 8, absent-tolerant Index rows | No PF19 home; l.742 routes the family's artifact contract to HDE Schemas & Artifacts and HDE Build Notes | l.742 |
| Decision 9, ADR block | No PF19 home. Owner: Change Process Guide §3.5.4 (T-03) | None |
| Problem statement, dependency direction, HDE-EPIC039 weighing, alternatives | Explanatory or historical. Not drained | None |
| Stated limits | Writer contract, owned by Change Process Guide, HDE Schemas & Artifacts, HDE Mechanics Guide and HDE Governance. The Epic admission limit and the Epic pointer limit are drafted under C-18. The tracked-issue form has no PF19 home | None |
| Epic-only identity inventory | No PF19 home. Owner: HDE Schemas & Artifacts §1.2 (T-04) | None |

### 5.2 Row C-18 — 2026-11-01 amendment (2.8 lines 1060, 1082, 1099, 1100, 1103, 1127; supporting 2.9)

| Source item | Disposition | Redline |
| :---- | :---- | :---- |
| Epic close-run family: an Epic admitted in `ADMITTED_EPIC_CLOSE` has the same family under `audit/qa/<epic-dir>/close/`; HDE-EPIC041 is the one Epic admitted; another Epic needs its own admission (decision 7, l.1082, and the stated limit, l.1103) | Drafted. The baseline says "No Epic close-run family is admitted" at l.742 and l.1124, and both statements are now false | RL-05 (path-grammar row), RL-06 (approved exception 5), RL-07 (close-pack truthfulness home) |
| Epic pointer to its own close-run directory before it exists, B-2 (stated limit l.1100) | Drafted | RL-08 |
| Epic tracked-issue ID form `ISSUE-EPIC<NNN>-TI-<nn>`, B-1 (l.1099) | No PF19 home. PF19 states no tracked-issue rule; its only `TI-` text is historical, at l.4654. Owners: Change Process Guide §3.5.2.1, HDE Schemas & Artifacts, HDE Governance, Plan Templates "Tracked Issues" (T-03, T-04, T-01) | None |
| Epic Index rows with `epic_id`, B-3 | No PF19 home (artifact contract) | None |

PF19's share follows from its existing text: it already named the CRD family in four places, so the amendment needed the Epic counterpart in the same four places. The ledger leaves this share unapportioned (l.1127).

### 5.3 Row C-26 — Live QA rules (2.15 lines 1650–1804)

| Source item | Disposition | Redline |
| :---- | :---- | :---- |
| "Status. Proposed." and the publication clause | Not drained. Treated as active, because v14.0.5 on `main` publishes 2.15 (ledger §2 "Status reading") | None |
| Decision quotes, and "The failure that prompted it" | History and rationale. Not drained; the HDE-EPIC041 record goes to T-10 | None |
| Relation to other canon: supersedes the "touches or can affect a production surface" dependency for the R-1 to R-4 scopes, and keeps every other control | Applied. RL-09 states the minimum for every Epic, whatever it changed, and keeps the existing production-affecting rules (baseline l.1371–l.1379) as additions. RL-01 aligns §2.3's Product Owner rails posture with the same minimum | RL-09, RL-01 |
| R-1: live vendor compat, the deployed-service check, SYN-A and SYN-B, an Epic's own live surfaces, and what does not satisfy it | Drafted | RL-09; pointers in RL-01, RL-03 and RL-04 |
| R-2: only the Product Owner may waive; the waiver's form; an agent's finding is a question put no later than QA-10; the Plan is not approval-ready until he answers; silence and the like are not waivers | Drafted where it bears on PF19's QA process. The waiver authority and form, and the list of what is not a waiver, go to §3.1.2 with the live test line (RL-03). The QA-10 question and the Plan-approval condition go to §3.1.1, the QA-10 home (RL-02). The exemption content itself (reason, accepted risk, substitute proof, claim withheld, later obligation) is routed to HDE Governance and not restated | RL-02, RL-03 |
| R-3, "Live QA" reserved | Drafted | RL-03; pointer in RL-04 |
| R-4: the live test line, the MISSING effects table, no agent override, prompts apply it | Drafted. The final QA closeout review's required-elements checklist (§9.2.15.6) gains the line as an element (RL-10) | RL-03, RL-10; pointer in RL-04 |
| R-5, a live test that cannot run blocks | Drafted. PF19 owns QA failure classification (§10.6, l.4095), so the `TOOLING_BLOCKED` classification, the wait and the rule that a block never becomes a PASS, a waiver or a closure go into the §3.5.5 minimum, routing to HDE Governance | RL-09 |
| R-6, execution controls unchanged | Already represented at baseline l.1379 (bounded, Product Owner-authorized, secret-safe, request limit, stop checks, no load testing, Ops class, nonclaims) and l.1428–l.1429 (scope, redaction, secret scan, quarantine). RL-09 adds only a routing sentence that applies those controls to the live compat test | RL-09 (routing) |

How the rules are placed. Each rule has one home in PF19, and other sections route to it:

* R-1 and R-5 live in §3.5.5, beside the existing live-proof minimum (RL-09).
* R-4, R-3 and R-2's waiver rules live in §3.1.2, the section that names the QA stages, Guide, Plan, Report and closure (RL-03).
* R-2's QA-10 question lives in §3.1.1, the QA-10 home (RL-02).
* §2.3 (RL-01), §3.4 (RL-04) and §9.2.15.6 (RL-10) carry one sentence or one checklist item each, which route to those homes. Without them, §2.3's Product Owner rails posture, §3.4's execution pattern and the closeout checklist would read as if the live test were optional.

### 5.4 Row C-07 — uncertain (2.2 lines 517–551)

Decision: no PF19 change. This rests on a whole-target reading for context and scope, as GTWPE-D3 requires, and not on 2.2's drain-target list.

* The l.525 scope supersedes a Glow QA Guide requirement only where PF19 makes "a close pack, tool, test or record" read or bind a planning document, or name a PF document by file name or version. Neither was found in the complete target:
  * PF19's `docs/ephemeral/` rules (l.32, l.138, l.734, l.1564) set where authored QA work products are stored and say they are referenced by path. 2.2's "Excluded" list (l.575) keeps storage out of its scope, and R-1 treats a prose citation as a reference only. No PF19 rule makes a tool, test, close pack or governed evidence artifact read or bind a `docs/ephemeral/` path.
  * PF19's cross-PF citations are versionless title stems (for example l.3965, l.3990, l.4193), and it names PF10 by title only (l.4390, l.4401–l.4402), as R-2 requires.
  * §10.8 (l.4252) asks a QA record to state the PF sources used and their available versions. That is attribution: it pins nothing and makes nothing depend on the version, and §10.8 itself forbids identity-only gates (l.4262). It does not fall within 2.2's dependency scope ("governs what may depend on those documents and on PF-Canon file identities", l.525).
* R-3, that the writer runs only at close, is the subject of CCR-5, which is held (H-06 below), so PF19 §3.1.3 is not touched.
* "Changes delivered" items concern the writer's source schema, owned by Change Process Guide §3.5.2.1 and HDE Schemas & Artifacts §1.2 (T-03, T-04). PF19's mention of the v2 source (l.1146) stays accurate. Status "Proposed" is not drained.
* 2.2's own drain-target list (l.581) names no Glow QA Guide section. That agrees with this finding but did not decide it.

### 5.5 Row C-29 — uncertain (2.16 lines 1869–1939)

Decision: no PF19 change. PF19 states no GATE:CORE-DET evidence. A whole-file search, after normalizing the export's `\_` and `\-` escapes, found zero occurrences of each of the following:

* `CORE-DET`, `CORE_DET` and `GATE:`;
* `make_compat_determinism` and `compat_determinism`;
* `cards/A3`, `cards/a3` and `IDENTITY_OK.txt`;
* `preimage_recompute`, `ab_ba_parity_bytecompare` and `two_run_identity_bytecompare`;
* `fixtures/composite` and `abba_compare`;
* `artifacts/compat/`, `identity_hash.txt`, `Reader goldens` and `make_reader_v1_goldens`.

A second, different check read the expected loci. §2.2.12 (l.416–l.418), §5.6.3 (l.2790–l.2809) and §9.2.3 (l.3364–l.3415) state determinism and identity tokens and their evidence, not GATE:CORE-DET entries, and none relies on a retired entry. The one `compat_public` occurrence, l.4734, is a §13.8 historical learning. 2.16 R-1's statement about Reader goldens has no PF19 counterpart: PF19's "Exact golden comparison" row (§5.9, l.3055) concerns mechanics configuration goldens.

### 5.6 Supporting rows

* C-20 (2.9): used only for the facts behind C-18. These are the B-1 to B-4 repair; HDE-EPIC041's nine close-run primaries; and the bounded CCR-5 ruling, which is history only.
* C-30 (2.16 R-3): used for the facts that SYN-A and SYN-B are stored and registered. RL-09 therefore says they "are kept" in production and "are registered", and does not drain 2.15's superseded "not yet" bullets.

### 5.7 Held, not drafted

* H-06, CCR-5. The alternative (A) drain of PF19 §3.1.3 is not authorized. It waits for the Product Owner's correcting HDE Build Notes addendum, which is the CCR-5 disposition (PF10 l.1161, l.1298). §3.1.3 (baseline l.513–l.519) is unchanged. RL-03 adds text to the end of §3.1.2, before §3.1.3's heading, and does not alter §3.1.3.
* H-08, CCR-6 (PF10 2.6 l.922). The tension between §3.4.3 and §3.4.8 (non-QA-root remediation is a routed work item) waits for the Product Owner's canon disposition of CCR-6. RL-05 and RL-06 name only the Epic close-run family, and do not touch the landing route, §0.7 or routed remediation.

No drafted row belongs to an open change. 2.8 carries HDE-CRD-0002 (Closed) and HDE-EPIC041 (closed, 2.10), and 2.15 and 2.16 are Product Owner rules, active from publication.

## 6. Interpretations, constraints and assumptions

* Epic scope. 2.15 excludes CRDs and leaves open whether a runtime-changing CRD runs the R-1 test. PF19 §0.2 (l.22) applies generally applicable Epic QA references to CRDs, unless a contract is expressly Epic-only. To keep that question open rather than decide it either way, every new rule says "For an Epic", and RL-03 and RL-09 state that the rules are expressly scoped to Epics (§0.2) and that the CRD question is a Product Owner decision left open in HDE Build Notes.
* Class rules. §3.5.5 says that only vendor-focused class (3) steps belong in the Product Owner's Live QA workload (l.1338). R-1 instead requires the deployed-service check in every Epic's QA run. RL-09 states that the class rules govern the Product Owner's session workload, not the minimum.
* §3.3 no-user mode, considered for context. The baseline forbids QA-created app-like user records and fake app users (l.564, l.570). SYN-A and SYN-B are synthetic fixtures stored by an Ops task under the Product Owner's write authorization, and RL-09 says so and keeps the §3.3 prohibition explicit. §3.3's statement that there is no canonical DB-backed compat source for live behavior tests (l.571) stays true: the vendor run remains the canonical live compat source, and RL-09 reports any deployed/CLI difference as a finding. §3.3 is therefore consistent and is not edited.
* §3.6 l.1592 ("For each epic that will have Live QA"), considered for context. Under R-1 this now covers every Epic, and the wording stays correct. Not edited.
* §9.2.13 (l.3697), considered for context. It applies to Epics "whose approved QA scope includes live vendor behavior", which now includes every Epic, so the text stays correct. Not edited.
* SYN-A and SYN-B UUIDs and birth data are stated in full as R-1 states them, and RL-09 routes to their registered homes. They are synthetic, and the repository record matches them (§4).
* Literal kept from the source: `hdctl showcompat --source vendor` (PF19 elsewhere writes `--source=vendor`).
* Change types are report classifications only. CONSISTENCY marks RL-01 and RL-10, which align existing text with the new rules.
* Document control. No redline touches the header. TW-APPLY-10 derives the version, the dates and the Last Update Gate. PF19 has no change-log or revision-history section, and states its own version and date only in the header (l.7–l.8), so no history entry is prepared.
* Hygiene. A whole-file search for status and drafting markers (`Draft`, `TBD`, `TODO`, `PLACEHOLDER`, `FIXME`, `XXX`) found only normative mentions of placeholders and drafts (for example l.847, l.4143, l.4358, l.5423), not markers about the document itself. No hygiene redline is needed.
* Out-of-scope observation, not drafted: l.4469 (§13 ledger row SRC-0292) says "PF10-HDE-Build-Notes has no current addenda", which is untrue of v14.0.5. It sits in a historical classification ledger, and no selected source authorizes changing it.

## 7. Outside dependencies

None blocks this package. HDE Governance remains the home of the exemption content and of the Ops execution controls that RL-03 and RL-09 route to; its drainage is task T-01. The tracked-issue form drains in T-03, T-04 and T-01. PF19's routing sentences name those owners by title and do not depend on their drainage having happened.

## 8. Producer validation

The redlines were generated by a local script that builds every old block straight from the baseline bytes, so no old block was retyped. A separate validator then parsed the saved redlines file, not the generator's memory, and simulated a one-pass application to the unchanged original by original offsets.

| ID | Operation | Baseline line | Old block bytes | Expected count | Observed count | Span (byte offsets) | Replacement bytes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | REPLACE | 436 | 208 | 1 | 1 | 43343–43549 | 353 |
| RL-02 | REPLACE | 503 | 346 | 1 | 1 | 50065–50411 | 701 |
| RL-03 | REPLACE | 511 | 448 | 1 | 1 | 51364–51812 | 2585 |
| RL-04 | REPLACE | 638 | 250 | 1 | 1 | 69643–69893 | 701 |
| RL-05 | REPLACE | 742 | 1317 | 1 | 1 | 79306–80618 | 1578 |
| RL-06 | REPLACE | 782 | 140 | 1 | 1 | 85792–85932 | 197 |
| RL-07 | REPLACE | 1124 | 482 | 1 | 1 | 131213–131694 | 529 |
| RL-08 | REPLACE | 1146 | 665 | 1 | 1 | 133825–134484 | 834 |
| RL-09 | REPLACE | 1369 | 51 | 1 | 1 | 154171–154222 | 3927 |
| RL-10 | REPLACE | 3903 | 157 | 1 | 1 | 386689–386846 | 298 |

Checks run on the saved file, each with result PASS:

* operation spelling;
* contiguous IDs;
* nonempty old blocks;
* replacements differ from their old blocks;
* each old block is a complete line span;
* each old block occurs exactly once;
* spans do not overlap, and none is adjacent without its separating LF;
* each replacement occurs exactly once after application;
* the heading set is unchanged (269 headings);
* the final LF is preserved;
* no ASCII triple-dot or Unicode ellipsis is introduced;
* the stale "No Epic close-run family is admitted" is absent after application;
* the `END OF REDLINES` sentinel is present.

No `FIND_AND_REPLACE` is used, so the RL-045 count rule does not arise.

Simulated result, for information only (TW-APPLY-10 also changes the header, so its final bytes will differ): 690,317 bytes; 5,674 lines; SHA-256 `5ef9cfd6e957e438582177c8329d644499c4c2c7b7ef02050cdb63b4ef43cafb`. The diff against the original replaces 6 lines in place (436, 503, 742, 782, 1124, 1146) and adds 52 more. The simulation from the in-memory package and from the saved file gave the same hash.

Editorial checks against PF03:

* titles-only cross-references, with HDE Build Notes named by title only;
* no addendum number, version or file name of another PF in the paste text;
* claim states kept separate;
* no secrets;
* valid Markdown lists and tables in the existing house style.

## 9. Canon and records relied on

* PF10-HDE-Build-Notes: front matter "Precedence, versioning, and scope"; addenda 2.2, 2.8, 2.9 (supporting), 2.15 and 2.16, as listed in §2.
* PF19-Canon-Glow-QA-Guide: the whole document, as target.
* PF03-Reference-Technical-Writing-Best-Practices: the whole document, as editorial standard, in particular §3 "Canonical ownership" and "Claim-state separation", §5, §6, §7, §8, §9 "Source selection and citation", §11 and §13.
* GTWPE decision record, GTWPE-D3, and the ledger's 2026-11-02 correction and §8, which apply it.
* AGENTS.md "Canon-first rule" and "PF canon is read-only unless the prompt explicitly directs a change", as repository rules.

## 10. Save verification and correction route

* Redlines file: written to the path in §1 and read back. Its SHA-256 matches the generated file, and the saved copy passed the §8 validator with no problems.
* Proof log: this file, read back after saving. It records no hash of itself.
* Package: `COMPLETE_PACKAGE`, with both files present, read back and in agreement on identities and outcome.
* Correction route: any TW-APPLY-10 diagnostic returns to this preparer, TW-DRAIN-10 in this same session, as Nathan's handoff authorizes. Any corrected package takes a new preparation revision identity, and Apply validates it afresh.

## 11. Revision history

* Revision 1 (superseded before application). It held seven redlines, now RL-03 to RL-09. Its C-26 dispositions left R-2 and R-5 undrafted because the triage routed them to HDE Governance. It was committed in this session and never applied.
* Revision 2 (this package). Before pushing, a fetch showed the ledger's 2026-11-02 correction, which applies GTWPE-D3: route by context and scope, not by named drain targets. Read on that basis, R-2's QA-process rules and R-5's failure classification bear on PF19, which owns QA readiness, plan approval and failure classification. Revision 2 therefore:
  * adds RL-01 (§2.3), RL-02 (§3.1.1) and RL-10 (§9.2.15.6);
  * adds R-2's waiver authority and form to RL-03 (§3.1.2);
  * adds R-5 to RL-09 (§3.5.5);
  * renumbers revision 1's RL-01 to RL-07 as RL-03 to RL-09. Their other text is unchanged.
* The whole revision-2 batch was revalidated (§8). The C-17, C-18, C-07 and C-29 dispositions are unchanged. Their wording now states that each rests on context, not on drain-target lists.
