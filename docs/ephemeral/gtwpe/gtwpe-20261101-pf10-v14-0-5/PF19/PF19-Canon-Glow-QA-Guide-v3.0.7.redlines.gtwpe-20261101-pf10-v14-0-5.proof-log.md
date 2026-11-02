# Proof log — PF19 redlines — gtwpe-20261101-pf10-v14-0-5 (T-06)

This is the processing report for `PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.md`, in this directory. It records how that redlines file was made, what it changes and why, and what was checked. It describes preparation revision 4; §11 records revisions 1 to 3 and why each was superseded.

## 1. Artifact and outcome

| Field | Value |
| :---- | :---- |
| Artifact | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF19/PF19-Canon-Glow-QA-Guide-v3.0.7.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Artifact identity at save | 71,200 bytes; SHA-256 `c515c79751cbd5303a474fbef967356cadec0619ab3d9b505a8d9b56950c56e1`; git blob `7f1bc3e5171f5a1f8af2b2d424cb8d1e9965fb11` |
| Run identity | `gtwpe-20261101-pf10-v14-0-5`, task T-06, preparation revision 4 |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1, Notion page `3f44590a05eb8172a314fe6b958bb9ff` (fetched live at the start of the step; page state 2026-10-09T11:05:22.139Z), run in the Claude Code session Nathan started for T-06 on 2026-11-02, for the T-06 follow-up handoff of 2026-11-02, which authorizes this preparation and the application after it. No subagent, reviewer or other session was used. |
| Preparation outcome | `READY` |
| Save state | `COMPLETE_PACKAGE` (see §10) |
| Redlines | 53, RL-01 to RL-53, all `REPLACE` of one or more whole, contiguous baseline lines |
| Next step | TW-APPLY-10 — Apply Validated Redlines — 100926.1 (Notion page `3f44590a05eb81eebff6e3afa3d9aa5b`), in this same session, which validates this package afresh |

## 2. Sources and inputs

| Role | Identity | Reading |
| :---- | :---- | :---- |
| Target (original baseline) | `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.7.md`, in-document title PF19-Canon-Glow-QA-Guide, Status Canon, v3.0.7, effective 2026-10-26. Git blob `9af5e056608153aa8b279b5f170b6c7528e0e35b`; SHA-256 `e745ef3a939f103ef1aeeaef17e6d04ff0c03ca7e8ecc0d95abf261a07c1b160`; 682,678 bytes; 5,622 lines. Scope anchor §0.2 "Purpose & scope". It is the only PF19 version in the repository's history, so text lost in its export cannot be recovered from an earlier version. | Complete; see §3 |
| Change source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, PF10-HDE-Build-Notes v14.0.5, effective 2026.11.01. Git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`; SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; 385,734 bytes; 1,976 lines. One unlettered logical version. | Selected units complete; see §3 |
| Editorial standard | `docs/pfcanon/PF03-Reference-Technical-Writing-Best-Practices-v1.8.8.md`, v1.8.8. Git blob `504712df548a02f3aa4e7b8c37027385e46a3878`; SHA-256 `df685f3a66aa18fdcacb697b340263cb59fc682564fa59c50b3d9b9ca735c462`; 633 lines | Complete (lines 1–300 and 301–633) |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md`. The handoff's identity is commit `142feb35144d8795f927e0c78b665ace52279064`. It was re-read at `8ca919b00630caac5f3d62a422369e7923ad8989`, where the T-06 task row and its selections are unchanged and the 2026-11-02 correction and §8 apply. Task row T-06; assigned rows C-17, C-18, C-26; uncertain C-07, C-29; supporting C-20, C-30 | Complete. Planning and provenance only, not a change source |
| Decision record | `docs/prompt_ecosystem_management/gtwpe/gtwpe.decision-record.md`, GTWPE-D3 (lines 114–160): "if there are addenda in PF10, that means they need to be drained" and "all pf docs should be updated based on context and scope, not whether or not the addenda specify a drain target" | Read in full for the D3 section |
| Product Owner direction | Nathan, 2026-11-02, in this session, after revision 2 was applied: "fixed the defects and inconsistencies you noticed. And PF10 addenda should be referenced in any case" | Applied, as §5.4, §5.5 and §5.8 set out |
| Product Owner ruling | Nathan, 2026-11-02: “close pack should go after the decision to close is confirmed”. The T-06 follow-up handoff records it as deciding CCR-5 (HDE Build Notes v14.0.5, addendum 2.5, line 856) as alternative (A): 2.2 R-3 stands as written, its first bullet included, and the permanent documents are drained to match. It releases H-06 for this document. The change source stays PF10 v14.0.5 2.2 R-3 (lines 547–551). | Applied, as §5.4 and §5.7 set out |
| Handoff | Nathan's T-06 follow-up handoff of 2026-11-02 (the CCR-5 ruling; keep every revision-3 redline unless the ruling changes it; H-08 still held), after his T-06 handoff of 2026-11-01 (target, rows, unit boundaries, held items H-06 and H-08, branch, output paths, the Drain-then-Apply sequence, and a return to Drain to correct the package) | Applied |

Baseline and currency. All canon was read from `origin/main`. The handoff baseline is `e2b7427ff418ca8f08f05587c4a541308a76da56`. At this step `origin/main` was `84d6d1cad95c67788336d174dc4b8922d9bb0cb2`, and `git diff --stat e2b7427 origin/main -- docs/pfcanon/` is empty, so the target and source baseline is unchanged.

Selected source units, each read completely:

* 2.8, lines 1063–1106 and 1111–1127. Rows C-17, C-18.
* 2.15, lines 1650–1804 (status, R-1 to R-6). Row C-26.
* 2.2, lines 517–551 (status, the l.525 precedence scope, R-1 to R-3). Row C-07. Lines 552–588 were also read as the rest of the unit.
* 2.16, lines 1869–1939 (status, R-1, R-2). Row C-29. Lines 1940–1976 were also read as the rest of the unit.

Supporting reading only, not drain scope: 2.8 lines 1048–1062, 1107–1110 and 1128–1145; 2.9 lines 1146–1229 (row C-20); 2.15 lines 1805–1868; 2.16 R-3 lines 1940–1948 (row C-30). PF10 line 922 was read only to identify the held CCR-6 tension (H-08). PF10 line 856, the CCR-5 entry of addendum 2.5, was read to apply the ruling. The consistency reference `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/PF27/PF27-Canon-Plan-Templates-v2.0.7.md` lines 2260–2299 (T-07's §3B under the same ruling, at commit `8bef1ae`) was read only for consistency.

## 3. Coverage

Target: read completely, in eighteen contiguous windows, with byte counts recorded and summing to the file size (682,678 bytes): lines 1–392 (38,023 bytes); 393–716 (38,087); 717–1034 (38,101); 1035–1344 (38,032); 1345–1622 (38,028); 1623–2018 (38,159); 2019–2638 (38,142); 2639–3064 (38,087); 3065–3510 (38,009); 3511–3831 (38,246); 3832–4187 (38,273); 4188–4504 (38,070); 4505–4744 (38,172); 4745–4880 (38,016); 4881–5014 (38,072); 5015–5134 (38,115); 5135–5280 (38,078); 5281–5622 (34,968). A heading map (269 headings) and literal searches were run over the whole file with a local script. No window ended mid-unit.

Source: each selected and supporting unit was read through its stated boundary, with byte counts recorded: lines 517–588 (10,943 bytes); 1048–1062 (10,253); 1063–1086 (10,696); 1087–1106 (9,270); 1107–1145 (5,939); 1146–1195 (21,738); 1196–1229 (4,728); 1650–1730 (6,573); 1731–1868 (8,673); 1869–1976 (8,408).

## 4. Repository inspection (read-only)

Current-repository statements in the redlines rest on direct read-only inspection of `origin/main` `84d6d1ca`, which is identical to `e2b7427` outside `docs/ephemeral/`:

* `tools/evidence/update_evidence_index.py` lines 62–64: `ADMITTED_EPIC_CLOSE` holds one entry, HDE-EPIC041 (RL-10, RL-14).
* `audit/qa/hde-epic041/close/` holds nine `primary.log` files, each with its path proof (RL-10).
* `tools/qa/generate_epic_close_pack.py` lines 2635–2655: the change's own close-run directory is a required pointer only for a CRD, and it may be recorded before it exists (RL-15).
* `docs/run/EPIC011_TEST_IDENTITIES.md` lines 34–49 and `engine/bodygraph/ingest.py` lines 32–41 register SYN-A and SYN-B with the UUIDs and birth data RL-17 states. `audit/ops/hde-epic041/postclose-ops01/run.log` lines 32 and 34 record one stored row each (RL-17).
* The five CI owner tests RL-04 names are present: `tests/core/test_engine_core_abba.py`, `tests/core/test_engine_core_determinism.py`, `tests/compat/test_evaluate_pair_eligibility.py`, `tests/compat/test_compat_public_ab_ba_identity.py` and `tests/cli/test_showcompat_parity_and_identity.py`. Of the retired entries, `scripts/make_compat_determinism_artifacts.py` is present (kept as history); `artifacts/cards/A3/IDENTITY_OK.txt` is absent; and the lower-case `artifacts/cards/a3/IDENTITY_OK.txt` is present, as 2.16 states.

## 5. Change and disposition ledger

Under GTWPE-D3 and Nathan's direction of 2026-11-02, every selected addendum is drained into PF19 wherever it bears on PF19 in context and scope, and PF19 references it. PF19 names PF10 by its title, HDE Build Notes, and never by addendum number, section or version: AGENTS.md ("PF documents other than PF10 never cite PF10 by section, addendum number, heading, paragraph or version"), PF19 §12.1 and §12.2, and PF03 §3 "Canonical ownership" require that.

### 5.1 Row C-17 — close-pack writer ADR (2.8)

Already represented, and unchanged:

* the CRD close-run home of same-run close evidence (baseline l.1124);
* the v2 writer's rendering of the verbatim heading and the pointer list (l.1146);
* the close-run family beside `checks/` (l.742, l.782).

Decisions 1 to 9, the stated limits and the Epic-only inventory belong to the writer contract, owned by Change Process Guide, HDE Schemas & Artifacts, HDE Mechanics Guide and HDE Governance (T-03, T-04, T-05, T-01). PF19 routes to them at l.742, l.1146 and l.3691.

### 5.2 Row C-18 — 2026-11-01 amendment (2.8 l.1060, l.1082, l.1099, l.1100, l.1103, l.1127; supporting 2.9)

* The Epic close-run family for an admitted Epic is drafted in RL-10, RL-11 and RL-14. The baseline's "No Epic close-run family is admitted" (l.742, l.1124) is now false.
* The Epic pointer to its own close-run directory (B-2) is drafted in RL-15.
* The Epic tracked-issue ID form has no PF19 home: PF19 states no tracked-issue rule, and its only `TI-` text is historical (l.4654). It drains in T-03, T-04 and T-01.

### 5.3 Row C-26 — Live QA rules (2.15)

| Rule | Redline | Note |
| :---- | :---- | :---- |
| R-1 | RL-17 (§3.5.5); pointers in RL-05 (§2.3), RL-07 (§3.1.2), RL-09 (§3.4) | Live compat test minimum for every Epic. RL-17 references HDE Build Notes as the source of the direction |
| R-2 | RL-06 (§3.1.1), RL-07 (§3.1.2) | The QA-10 question and the Plan-approval condition; the waiver authority and form. The exemption content is routed to HDE Governance |
| R-3 | RL-07; pointer in RL-09 | "Live QA" is reserved |
| R-4 | RL-07, RL-50 (§9.2.15.6); pointer in RL-09 | The live test line and the MISSING table. RL-07 references HDE Build Notes as the source of the direction |
| R-5 | RL-17 | `TOOLING_BLOCKED`, and never a PASS, a waiver or a closure |
| R-6 | Already represented at l.1379 and l.1428–l.1429; routing sentence in RL-17 | |

"Status. Proposed.", the decision quotes and the failure history are not drained; the HDE-EPIC041 record goes to T-10. The CRD question stays open, and every new rule is scoped to Epics (§0.2).

### 5.4 Row C-07 — 2.2 (now drained)

Revision 2 decided "no change", because PF19 had no requirement within the l.525 precedence scope. Under Nathan's direction the addendum is now referenced and drained where it bears on PF19 in context, which is PF19's rules on where change-process artifacts are stored and how PF sources are cited:

* RL-01, §0.4.3, after the paragraph on change-process artifacts (l.138):
  * R-1, planning documents serve planning only. No code, test, tool, CI step, workflow, schema, QA harness, governed evidence artifact, step-logs manifest, close pack, manifest, Index or Mirror row or path proof binds a `docs/ephemeral/` path. A later stage records the facts it needs, and a prose citation in a permanent record is a reference only.
  * R-2, PF-Canon is resolved by stable identity. Nothing that must remain valid pins a PF file name, version or digest; a tool resolves current canon at run time by identity and title; and citations name PF documents by title, with HDE Build Notes by title alone.
  * The §10.8 version record (l.4252) is stated to be attribution only, which reconciles it with R-2.
* RL-03, §2.2.11, as a new lane sub-bullet: R-3's second bullet, that the close-pack writer's test is a close-stage test selected only when its own surfaces change.
* R-3's first bullet, that the writer writes a close pack only at the close stage, at the end of a full work-unit cycle, after the authorized QA verdict and the closure decision exist, is now drained into §3.1.3 (RL-08). This follows the Product Owner's CCR-5 ruling of 2026-11-02, “close pack should go after the decision to close is confirmed”, which decides CCR-5 as alternative (A). RL-08 replaces §3.1.3's second paragraph:
  * the entry becomes a closure decision of `CLOSE`, and the `DO_NOT_CLOSE` entry is removed;
  * the set is produced only after the decision confirms the close, and never reopens implementation, QA or the closure decision;
  * the exit is the Product Owner's merge of the close pull request;
  * the set is no longer a prerequisite that precedes the closure decision.
* Three revision-3 redlines are aligned with the ruling:
  * RL-07 (§3.1.2) lists the closure decision before the close mutation set result, in both the record list and the MISSING table;
  * RL-10 (line 742) and RL-14 (line 1124) say the close-run family is written after the final QA verdict and the closure decision of `CLOSE`.
  * The family's 2.8 name, "post-verdict", is kept, because it is still true.
* The wording matches T-07's Plan Templates §3B under the same ruling: the entry is a closure decision of `CLOSE`, there is no `DO_NOT_CLOSE` entry, the exit is the Product Owner's merge, and the decision comes first and is not revisited.
* "Changes delivered" concern the writer's source schema, owned by Change Process Guide and HDE Schemas & Artifacts. PF19's mention of the v2 source (l.1146) stays accurate.

### 5.5 Row C-29 — 2.16 (now drained)

Revision 2 decided "no change", because PF19 states no GATE:CORE-DET evidence. Under Nathan's direction the addendum is now referenced and drained where it bears on PF19's determinism and AB↔BA proof rules. RL-04, in §2.2.12 "Engine serializer/composer determinism", adds:

* R-1: GATE:CORE-DET evidence is the real compat path. Under closed rails it is the five CI owner tests, which must not be removed or weakened without owner review. Under open rails it is the live compat test, which is Ops evidence. The Reader goldens prove canonical emission and the Reader covenant, not compat AB↔BA.
* R-2: no QA record may cite the retired entries as current proof. They are the compat-determinism generator, the `A3` identity marker, the three `ci/jobs/` files and the four composite fixture and comparison-log entries.

The gate's pass conditions and evidence lists stay with HDE Governance (T-01).

### 5.6 Supporting rows

* C-20 (2.9): the facts behind C-18.
* C-30 (2.16 R-3): SYN-A and SYN-B are stored and registered (RL-17).

### 5.7 Held items

* H-06, CCR-5: released for this document by the Product Owner's ruling of 2026-11-02 (§2), and drained in RL-08. The ledger's H-06 row is not edited by this task. Historical records keep their wording; the closure record near baseline line 5307 is untouched.
* H-08, CCR-6. The §3.4.3 and §3.4.8 landing-route tension waits for the Product Owner's canon disposition (PF10 l.922).

### 5.8 Defects and inconsistencies (Nathan's direction of 2026-11-02)

Fixed where PF19's own text proves the intended content:

| Redline | Defect | Basis for the fix |
| :---- | :---- | :---- |
| RL-51 | §13 ledger row SRC-0292 (l.4468) said "PF10-HDE-Build-Notes has no current addenda", which is false. Revision 2 and the session report cited it as l.4469; the correct line is 4468 | It now reads "current HDE Build Notes addenda govern where they speak", which references the addenda as Nathan directs |
| RL-13 | The §3.4.12 heading (l.1113) was flattened into the last §3.4.11 bullet; the heading map ran from 3.4.11 to 3.4.13 | Restored as a level-3 heading. The doc-alignment, close-pack truthfulness and close report paragraphs (baseline l.1115–l.1148) now sit under §3.4.12 instead of §3.4.11 |
| RL-18 to RL-34 | Seventeen §5 playbook sub-headings (Inputs, Scope, Steps, Evidence, Tokens, Failures to watch, Where it lives) were flattened into list items | §5's opening (l.2157) names the pattern, and the same sections already carry `### **Intent**`, `### **Inputs**` and `### **Evidence**` headings. Restored as level-3 headings |
| RL-35 | Stray bold on the last §5.4 failure item (l.2559) | Bold removed; the text is unchanged |
| RL-38 to RL-43 | §9.1.2 to §9.1.7 were flattened into the glossary list | §9.1.1 (l.3280) is a level-3 heading. Restored to the same level |
| RL-52 | §13.18 carried a second "Known non-goals" paragraph (l.5223) that is a byte-identical copy of §13.17's (l.5203), naming EPIC037 subjects | Deleted; §13.18's own non-goals paragraph (l.5221) is kept |
| RL-53 | §14.6's list lead-in "Update trigger(s) include:" was captured as a table row (l.5587) | Restored as the paragraph before its list |
| RL-02 | §1.4 (l.221): the example URL was damaged into a broken link with a lost placeholder | Replaced with the concrete URL PF19 itself records, `DEV_SAMPLER_URL=http://127.0.0.1:8000/internal/dev/sampler` (§14.5.1, l.5477) |
| RL-12 | §3.4.10 (l.1073) approved `[SNIP: lines omitted]`, while l.1017 and PF03 §3 use `[SNIP: <n> lines omitted]` | Aligned to `[SNIP: <n> lines omitted]` |
| RL-16, RL-37, RL-45, RL-48 | Lost `<epic-id>` placeholders, shown as `\\` (l.1206 first occurrence, l.3234, l.3485, l.3748) | Proved by the same sentence (l.1206) and by the canonical paths at l.1933 and l.3232 |
| RL-44, RL-49 | Lost `<run_id>` and `<RUN_SUBPATH>` placeholders (l.3482, l.3769) | Proved by the identical rule at l.1952 |
| RL-36, RL-46, RL-47 | Lost `<pair>` placeholders in the admin-bundle file names (l.3010–l.3011, l.3593–l.3594, l.3610) | Proved by the intact code spans at l.2971 and l.2979 |

Restored placeholders are put in code spans, so a Markdown renderer cannot strip them again.

Not fixed, because PF19 does not prove the lost text and no earlier version exists. Each needs its original wording from Nathan:

* l.849: "STOP if output contains `\\`";
* l.1206, the second placeholder;
* l.1274;
* l.2024: the section separators;
* l.2211 and l.3106: the ETag form;
* l.2401;
* l.2411–l.2412 and l.2441–l.2447: App BE snapshot names;
* l.2530–l.2540: FE smoke names;
* l.2748;
* l.2992, l.3012–l.3013, l.3596 and l.3625–l.3626: the auth-negative and parity names, where `<pair>` is likely but unproved;
* l.3004, l.3178, l.3551 and l.3996: the path-proof stem;
* l.4143.

Considered and left as they are:

* `--source vendor` against `--source=vendor`. PF19 already uses both forms (for example l.581 and l.1432), both are valid invocations, and §3.4.7 makes such syntax non-gating. RL-17 keeps 2.15's literal.
* Identical non-goals paragraphs in §13.15 and §13.16 (l.5163, l.5180). Each entry carries its own; that is a repeated template, not a misplaced copy.

## 6. Interpretations, constraints and assumptions

* Reading of Nathan's direction. "Fixed" is read as "fix", because no commit since revision 2 changes PF19 or this package. "PF10 addenda should be referenced in any case" is read in two ways:
  * C-07 and C-29 are drained and referenced even though PF19 had no conflicting text (§5.4, §5.5).
  * The new C-26 rule blocks and the SRC-0292 row reference HDE Build Notes.
  * PF19 names PF10 by title only (§5 preamble). Citing addendum numbers would need Nathan's explicit override of AGENTS.md and PF19 §12.2.
* Epic scope, class rules, §3.3 no-user mode, §3.6, §9.2.13 and the SYN-A and SYN-B details are unchanged from revision 2.
* Structure. The 24 restored headings change the heading count from 269 to 293. Every original heading keeps its text, order and level. §3.4.11's content after its bullet list now belongs to §3.4.12; RL-14 and RL-15 still name §3.4.11 in their heading paths, because heading paths describe the original baseline.
* Document control. No redline touches the header. TW-APPLY-10 derives the version, the date and the Last Update Gate. PF19 has no change-log section, so no history entry is prepared.
* Hygiene. No `Draft` status language or drafting marker about the document exists or is added.

## 7. Outside dependencies

None blocks this package. HDE Governance holds the exemption content, the Ops controls and the GATE:CORE-DET evidence lists (T-01). Plan Templates holds the CI-lane rule (T-07). The tracked-issue form drains in T-03, T-04 and T-01. Recovering the unproved placeholders needs Nathan's original text.

## 8. Producer validation

The package was built by a local script. It takes revision 3's 52 operations from the saved file and changes the three payloads the ruling affects (RL-07, RL-10, RL-14). It adds RL-08, with its old block taken from the baseline bytes, then renumbers in document order and writes the file. The other 49 operations are byte-identical to revision 3; a separate comparison found 49 identical old/new pairs, 3 changed and 1 added. A separate validator then parsed the saved file and simulated a one-pass application to the unchanged original by original offsets.

Columns: the baseline line is where the old block starts; old block bytes; expected count; observed count; span in byte offsets; replacement bytes.

| ID | Operation | Baseline line | Old bytes | Expected | Observed | Span | New bytes |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| RL-01 | REPLACE | 138 | 946 | 1 | 1 | 12571–13517 | 2571 |
| RL-02 | REPLACE | 221 | 227 | 1 | 1 | 22664–22891 | 219 |
| RL-03 | REPLACE | 406 | 256 | 1 | 1 | 40209–40465 | 629 |
| RL-04 | REPLACE | 418 | 229 | 1 | 1 | 41943–42170 | 1548 |
| RL-05 | REPLACE | 436 | 208 | 1 | 1 | 43343–43549 | 353 |
| RL-06 | REPLACE | 503 | 346 | 1 | 1 | 50065–50411 | 701 |
| RL-07 | REPLACE | 511 | 448 | 1 | 1 | 51364–51812 | 2659 |
| RL-08 | REPLACE | 517 | 879 | 1 | 1 | 52376–53255 | 972 |
| RL-09 | REPLACE | 638 | 250 | 1 | 1 | 69643–69893 | 701 |
| RL-10 | REPLACE | 742 | 1317 | 1 | 1 | 79306–80618 | 1614 |
| RL-11 | REPLACE | 782 | 140 | 1 | 1 | 85792–85932 | 197 |
| RL-12 | REPLACE | 1073 | 141 | 1 | 1 | 119037–119178 | 145 |
| RL-13 | REPLACE | 1112 | 140 | 1 | 1 | 130040–130180 | 143 |
| RL-14 | REPLACE | 1124 | 482 | 1 | 1 | 131213–131694 | 566 |
| RL-15 | REPLACE | 1146 | 665 | 1 | 1 | 133825–134484 | 834 |
| RL-16 | REPLACE | 1206 | 216 | 1 | 1 | 138891–139105 | 225 |
| RL-17 | REPLACE | 1369 | 51 | 1 | 1 | 154171–154222 | 4005 |
| RL-18 | REPLACE | 2182 | 112 | 1 | 1 | 240122–240234 | 114 |
| RL-19 | REPLACE | 2245 | 112 | 1 | 1 | 243403–243515 | 115 |
| RL-20 | REPLACE | 2254 | 57 | 1 | 1 | 243718–243775 | 59 |
| RL-21 | REPLACE | 2262 | 124 | 1 | 1 | 244251–244375 | 126 |
| RL-22 | REPLACE | 2279 | 151 | 1 | 1 | 245077–245224 | 153 |
| RL-23 | REPLACE | 2288 | 75 | 1 | 1 | 245496–245571 | 78 |
| RL-24 | REPLACE | 2333 | 101 | 1 | 1 | 247550–247651 | 103 |
| RL-25 | REPLACE | 2341 | 84 | 1 | 1 | 247973–248057 | 87 |
| RL-26 | REPLACE | 2377 | 80 | 1 | 1 | 249726–249806 | 82 |
| RL-27 | REPLACE | 2386 | 26 | 1 | 1 | 250075–250101 | 29 |
| RL-28 | REPLACE | 2397 | 93 | 1 | 1 | 250334–250427 | 95 |
| RL-29 | REPLACE | 2436 | 109 | 1 | 1 | 252648–252757 | 112 |
| RL-30 | REPLACE | 2501 | 60 | 1 | 1 | 255622–255682 | 63 |
| RL-31 | REPLACE | 2511 | 131 | 1 | 1 | 255894–256025 | 133 |
| RL-32 | REPLACE | 2536 | 130 | 1 | 1 | 257397–257527 | 132 |
| RL-33 | REPLACE | 2544 | 95 | 1 | 1 | 257942–258037 | 98 |
| RL-34 | REPLACE | 2553 | 57 | 1 | 1 | 258270–258327 | 59 |
| RL-35 | REPLACE | 2559 | 111 | 1 | 1 | 258670–258781 | 107 |
| RL-36 | REPLACE | 3010 | 127 | 1 | 1 | 296457–296580 | 135 |
| RL-37 | REPLACE | 3234 | 282 | 1 | 1 | 312653–312935 | 292 |
| RL-38 | REPLACE | 3284 | 68 | 1 | 1 | 315504–315572 | 70 |
| RL-39 | REPLACE | 3297 | 54 | 1 | 1 | 315905–315959 | 56 |
| RL-40 | REPLACE | 3302 | 51 | 1 | 1 | 316038–316089 | 53 |
| RL-41 | REPLACE | 3308 | 60 | 1 | 1 | 316195–316255 | 62 |
| RL-42 | REPLACE | 3314 | 58 | 1 | 1 | 316385–316443 | 60 |
| RL-43 | REPLACE | 3317 | 75 | 1 | 1 | 316475–316550 | 78 |
| RL-44 | REPLACE | 3482 | 160 | 1 | 1 | 336506–336666 | 179 |
| RL-45 | REPLACE | 3485 | 178 | 1 | 1 | 336801–336979 | 184 |
| RL-46 | REPLACE | 3593 | 109 | 1 | 1 | 351836–351945 | 117 |
| RL-47 | REPLACE | 3610 | 192 | 1 | 1 | 353598–353790 | 196 |
| RL-48 | REPLACE | 3748 | 85 | 1 | 1 | 370235–370320 | 91 |
| RL-49 | REPLACE | 3769 | 199 | 1 | 1 | 372389–372588 | 225 |
| RL-50 | REPLACE | 3903 | 157 | 1 | 1 | 386689–386846 | 298 |
| RL-51 | REPLACE | 4468 | 125 | 1 | 1 | 452468–452593 | 137 |
| RL-52 | REPLACE | 5221 | 1103 | 1 | 1 | 635765–636868 | 408 |
| RL-53 | REPLACE | 5587 | 39 | 1 | 1 | 677175–677214 | 27 |

Checks on the saved file, each with result PASS:

* operation spelling and contiguous IDs;
* nonempty old blocks, and each one is a complete line span occurring exactly once;
* replacements differ from their old blocks;
* line spans do not overlap;
* each replacement occurs exactly once after application;
* original headings are preserved in order, and the only new headings are the 24 planned restorations;
* the final LF is preserved;
* no ASCII triple-dot or Unicode ellipsis is introduced;
* the stale Epic close-run wording is absent;
* the `END OF REDLINES` sentinel is present.

Simulated result, for information only (TW-APPLY-10 also changes the header): 693,402 bytes; 5,724 lines; SHA-256 `d90aa4c1a0b4fea1330b8d53da9f2ece2a8646ffa1d5994886b2650d96206da2`. The simulation from the generated file and from the saved file gave the same hash.

## 9. Canon and records relied on

* PF10-HDE-Build-Notes: front matter "Precedence, versioning, and scope"; addenda 2.2, 2.8, 2.9 (supporting), 2.15 and 2.16.
* PF19-Canon-Glow-QA-Guide: the whole document, including §12.1 "Living document" and §12.2 "Supersession rule (PF10 addenda)".
* PF03-Reference-Technical-Writing-Best-Practices: the whole document, in particular §3 "Canonical ownership" and "Structure and language", §7 (formatting repair) and §8.
* GTWPE decision record, GTWPE-D3; the ledger's 2026-11-02 correction and §8; Nathan's direction of 2026-11-02; Nathan's CCR-5 ruling of 2026-11-02.
* PF10-HDE-Build-Notes addendum 2.5, the CCR-5 entry (line 856), as supporting reading for the ruling.
* AGENTS.md "Canon-first rule" and "PF canon is read-only unless the prompt explicitly directs a change".

## 10. Save verification and correction route

* Redlines file: saved at the path in §1 and read back. Its SHA-256 matches the generated file, and the saved copy passed the §8 validator with no problems.
* Proof log: this file, read back after saving. It records no hash of itself.
* Package: `COMPLETE_PACKAGE`.
* Correction route: any TW-APPLY-10 diagnostic returns to this preparer in this session, as the follow-up handoff authorizes. Any corrected package takes a new revision identity, and Apply validates it afresh.

## 11. Revision history

* Revision 1 (commit `137e98f28e81b794b26b11c543da46369486a47f`): seven redlines. It left 2.15 R-2 and R-5 undrafted, following the triage's drain targets. Superseded before application.
* Revision 2 (commit `533841ab453d3ae977bcc10fad4c3a50301fd4a2`): ten redlines, after the ledger's 2026-11-02 GTWPE-D3 correction. It was applied to produce PF19 v3.0.8 (commit `e56a1833c1e175e9178eee7cde5558ebe3e10c8b`), and Nathan then directed further changes.
* Revision 3 (commit `7b84281d7a740b972bf9d21801f0c3b231a8b202`): 52 redlines, made under Nathan's direction of 2026-11-02. It keeps revision 2's ten operations, renumbered:

  | Revision 2 | Revision 3 |
  | :---- | :---- |
  | RL-01 | RL-05 |
  | RL-02 | RL-06 |
  | RL-03 | RL-07 |
  | RL-04 | RL-08 |
  | RL-05 | RL-09 |
  | RL-06 | RL-10 |
  | RL-07 | RL-13 |
  | RL-08 | RL-14 |
  | RL-09 | RL-16 |
  | RL-10 | RL-49 |

  RL-07 and RL-16 each gain one sentence that references HDE Build Notes. The rest is new:

  * the C-07 drain (RL-01, RL-03) and the C-29 drain (RL-04);
  * 39 defect and consistency fixes (§5.8).

  It was applied as v3.0.8 in commit `376b9f4afa3dbe950d39b71bb3f15be3573d68c8`. (The revision-3 numbers in this entry are revision 3's own.)
* Revision 4 (this package): 53 redlines, made under the Product Owner's CCR-5 ruling of 2026-11-02, “close pack should go after the decision to close is confirmed”. Changes from revision 3:
  * RL-08 is added, draining 2.2 R-3's first bullet into §3.1.3.
  * Revision 3's RL-07, RL-09 and RL-13 change, becoming RL-07, RL-10 and RL-14.
  * Revision 3's RL-08 to RL-52 become RL-09 to RL-53. Their payloads are unchanged except those of revision 3's RL-09 and RL-13, given above.
  * Revision 4 must be applied afresh, and its output replaces the revision-3-derived v3.0.8.
