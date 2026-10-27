# Redlines: PF04-Canon-HDE-Governance from v2.8.7 (T-PF04)

## Package identity

| Field | Value |
| --- | --- |
| Artifact | Exact redline batch for one PF document |
| Run identity | `gtwpe-20261026-pf10-v13-8-8 / T-PF04 / prep-1` |
| Preparer | TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff), run by the Claude Code cloud session https://claude.ai/code/session_016CSjfJr3cAwrXWvB9NRJt9, the Nathan-started T-PF04 document session |
| Preparation date | 2026-10-26 |
| Preparation outcome | `READY` (save completeness is recorded in the proof log after read-back) |
| Proof log | `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf04/redlines-PF04-from-v2.8.7.proof-log.md` |
| Next step | TW-APPLY-10 — Apply Validated Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb81eebff6e3afa3d9aa5b), authorized by Nathan's handoff for the same session |

## Original baseline (exact application baseline)

| Field | Value |
| --- | --- |
| Path | `docs/pfcanon/PF04-Canon-HDE-Governance-v2.8.7.md` |
| Repository and commit | `amthorn78/glow-hdengine-v2`, `origin/main` at `9dda63dd3f05f496c3ff67e95da78550d3950c5a`; byte-identical on `origin/main` at `0838ba08254eaefc888019df49a06aa2ae99cc6c` when preparation began |
| Title and version | `PF04-Canon-HDE-Governance`, `v2.8.7`, Status `Canon`, Effective date `2026-10-09`, Last Update Gate `BN 13.5` |
| Git blob | `86cf613ce7f90ad7fd64c33ab3c808543a1c9581` |
| Size | 570,610 bytes; 4,674 LF-terminated lines; no CR bytes |
| SHA-256 (raw bytes) | `eb36f8e4cc038e73f5e497c857b05fc06724f01bcb3a68683d94e4a065ead367` |

## Selected incoming scope

- Change source: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, HDE Build Notes v13.8.8, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`. Units read in full: front matter, lines 1–223 (F00, application rules); 2.1, lines 224–257 (A01); 2.11, lines 1205–1318 (A11); 2.15, lines 1620–1690 (A15); 2.16, lines 1691–1825 (A16); 2.17, lines 1826–1955 (A17); 2.18, lines 1956–2081 (A18).
- Supporting reading, not a change source: X03, `docs/adr/hde/close_pack_writer_adr.md`, blob `2d91679a198168958bf8b32c5f8b5459ee13de5b`, sections "Decision" (lines 18–35) and "Affected canon and drainage consequences" (lines 76–88).
- Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` at `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`), task T-PF04, rows A01, A11, A15, A16, A17, A18, with X03. Held item H-06 (the §9.1.1 review-chain entry) is left unchanged.

## Literal convention

- Every literal is fenced with five backticks and the info string `text`. The literal is every byte after the LF that ends the opening fence line, up to but not including the LF that immediately precedes the closing fence line. A literal that ends with LF therefore shows an empty line before its closing fence; a literal that begins with LF shows an empty first line.
- Literals are UTF-8, LF-only and exact, including trailing spaces: many target list lines, and the matching inserted lines, end with two spaces before LF. The byte length and SHA-256 given with each literal are authoritative for its exact bytes.
- Locations are bound to the unchanged original baseline above. Line numbers and byte offsets are given for orientation; each operation is resolved by its exact literal, never by a line number alone.
- Every `REPLACE` old block occurs exactly once in the whole baseline. Every `INSERT` gap is defined by a BEFORE anchor and an AFTER anchor that each occur exactly once and are contiguous in the baseline; the inserted text goes between them and neither anchor changes.
- The batch contains no `DELETE`, `FIND AND REPLACE` or `FIND_AND_REPLACE` operation and no header operation. TW-APPLY-10 derives the document-control fields under its header contract; the source identities for that plan are in the proof log.

## Batch summary

| ID | Operation | Section | Rows |
| --- | --- | --- | --- |
| RL-01 | INSERT | §2.0.19, "Close-pack baseline artifacts" | A15, A16, A17 with X03 |
| RL-02 | REPLACE | §2.0.19, "Close report minimal content (normative)" lead | A15, A16, A17 with X03 |
| RL-03 | REPLACE | §2.0.19, the close-pack manifest pointer item | A15, A16, A17 with X03 |
| RL-04 | INSERT | §2.0.19, after the canon-pointer fields | A15, A16, A17 with X03 |
| RL-05 | REPLACE | §2.0.19, "Close-pack manifest `key_outputs` shape (normative)" | A15, A16, A17 with X03 |
| RL-06 | INSERT | §9.1.3, after the downstream-session advice paragraph | A01 |
| RL-07 | REPLACE | §9.1.6, the Managing Prompt Engineer sentence | A01 |
| RL-08 | INSERT | §9.3.1, after the v2.8.7 entry | Target rule (§9.3, §9.3.1) |
| RL-09 | INSERT | §9.7.7, after the Epic Business Case block | A11 with A18 |
| RL-10 | REPLACE | §11.2, the scope line's drafting-status label | Target hygiene (TW-DRAIN-10 marker rule) |
| RL-11 | INSERT | Appendix D.0 | A15, A16, A17 with X03 |

## RL-01 — INSERT

- Ledger rows: A15, A16, A17 with X03
- Change type (report classification): CANON_UPDATE
- Operation: `INSERT`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**`
  - `## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**`
  - `### **2.0.19 QA bootstrap & harness (EPIC021+)**`
- Original-bound gap: after baseline line 891, before baseline line 892 (UTF-8 byte offset 127135)
- Expected gap occurrence: 1. Observed: BEFORE anchor 1, AFTER anchor 1, BEFORE+AFTER contiguous 1. Neither anchor is changed.

BEFORE anchor (exact, retained) (62 bytes, SHA-256 `ce07f08dbf0b071528fe1ef3ebd8fad6c3ef6f8d27241736a19af1f049bd3a97`):

`````text
      (Where `###` is the zero-padded 3-digit epic number.)  

`````

AFTER anchor (exact, retained) (67 bytes, SHA-256 `312b3e0e983b3d0f16fb8f726766418c4b65ac09129e3f07ac5856418287fe97`):

`````text
* **Closeout companion ledgers (recommended; may declare `None`).**
`````

Inserted text (exact) (571 bytes, SHA-256 `f240faf11b017c20f81d239ec4415aff89d0ddd70923e259712536ae29f165c8`):

`````text
    * For a CRD, the pair uses the CRD ID as its prefix: `audit/HDE-CRD-NNNN_close_report.md` and `audit/HDE-CRD-NNNN_MANIFEST.json`  
      (Where `NNNN` is the CRD number, zero-padded to at least four digits.)  
  * Producer: for a `close_candidate_source.v2` source, of an Epic or a CRD, the generic close-pack writer `tools/qa/generate_epic_close_pack.py` writes the pair; a v1 source keeps the v1 model and output bytes. **HDE-Schemas & Artifacts** and **HDE-Mechanics Guide** own the source schemas, the writer mechanics and the manifest's `key_outputs` minimum.  

`````

- Basis: HDE Build Notes v13.8.8 addendum 2.15 ("What is approved": CRD paths of record; the drainage of the ADR's canon table), as amended by 2.17, and the S21 ADR's canon-table row for HDE Governance (X03, supporting): "Name the CRD prefix beside `EPIC-###`, the v2 writer as the producer". Repository facts checked on main 0838ba08: `tools/qa/generate_epic_close_pack.py`, `schemas/close_candidate_source.v2.json` (change-ID pattern `HDE-CRD-[0-9]{4,}`) and `audit/HDE-CRD-0002_close_report.md`, `audit/HDE-CRD-0002_MANIFEST.json` exist.
- Rationale: The path-of-record names only `audit/EPIC-###_*`; a CRD close pack (now produced, for HDE-CRD-0002) has no canon path here, and no producer is named.

## RL-02 — REPLACE

- Ledger rows: A15, A16, A17 with X03
- Change type (report classification): CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**`
  - `## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**`
  - `### **2.0.19 QA bootstrap & harness (EPIC021+)**`
- Original-bound location: baseline line 895, UTF-8 byte offsets 127464–127601 (end exclusive)
- Expected occurrence count of the old block in the whole document: 1. Observed: 1.

Old block (exact, removed) (137 bytes, SHA-256 `43aa94418d67cd1b53753a5df9665e94d617033040c308e2d2094bf11f69e66c`):

`````text
**Close report minimal content (normative).** `audit/EPIC-###_close_report.md` MUST be a human-readable closure summary and MUST include:
`````

Replacement block (exact) (208 bytes, SHA-256 `e299cce9080ae910005afe1f027129d43f9ea11cc92eb08e688c247946712473`):

`````text
**Close report minimal content (normative).** The close report, `audit/EPIC-###_close_report.md` or, for a CRD, `audit/HDE-CRD-NNNN_close_report.md`, MUST be a human-readable closure summary and MUST include:
`````

- Basis: Same basis as RL-01: the ADR canon-table row names "Close report minimal content (normative)" as a locus for the CRD prefix.
- Rationale: Names the CRD close report beside the Epic one in the normative content rule.

## RL-03 — REPLACE

- Ledger rows: A15, A16, A17 with X03
- Change type (report classification): CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**`
  - `## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**`
  - `### **2.0.19 QA bootstrap & harness (EPIC021+)**`
- Original-bound location: baseline line 905, UTF-8 byte offsets 130290–130384 (end exclusive)
- Expected occurrence count of the old block in the whole document: 1. Observed: 1.

Old block (exact, removed) (94 bytes, SHA-256 `6773554a69289aa68aec2b51567c7fd3b238a9c7f1bf4ebace11887e9495cdde`):

`````text
a pointer to the close-pack manifest `key_outputs` bindings in `audit/EPIC-###_MANIFEST.json`,
`````

Replacement block (exact) (144 bytes, SHA-256 `083c5f561bee36e9666c1cbed1bc16fd083e8cfcd0905522fd450850cf26c481`):

`````text
a pointer to the close-pack manifest `key_outputs` bindings in `audit/EPIC-###_MANIFEST.json` or, for a CRD, `audit/HDE-CRD-NNNN_MANIFEST.json`,
`````

- Basis: Same basis as RL-01; the manifest pointer item of "Close report minimal content" names only the Epic manifest.
- Rationale: Names the CRD manifest beside the Epic one in the pointer item.

## RL-04 — INSERT

- Ledger rows: A15 (C-3), A16 (LR7-O9), A17 (resolutions A and B) with X03
- Change type (report classification): CANON_UPDATE
- Operation: `INSERT`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**`
  - `## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**`
  - `### **2.0.19 QA bootstrap & harness (EPIC021+)**`
- Original-bound gap: after baseline line 910, before baseline line 911 (UTF-8 byte offset 130928)
- Expected gap occurrence: 1. Observed: BEFORE anchor 1, AFTER anchor 1, BEFORE+AFTER contiguous 1. Neither anchor is changed.

BEFORE anchor (exact, retained) (79 bytes, SHA-256 `8e4f490dd538dd8ca35d52d6321c4b709e04ed0064b140101abcb649611c7542`):

`````text
    * an `ADR status line:` line identifying the ADR governing the TI claim,  

`````

AFTER anchor (exact, retained) (113 bytes, SHA-256 `816fada86ae0bf56e2a6d460944a42653455fe8509ec2dfe1bcfa8bcbf1ae718`):

`````text
  * **Coverage vs QA Plan accounting (required when the epic has a Live QA Plan or otherwise requires Live QA).**
`````

Inserted text (exact) (1120 bytes, SHA-256 `b80a2f7e439d7033502f2bfc03dc3843b82d3cd12abe79ad4325400f98d36e79`):

`````text
  * **Tracked-issue items under the generic v2 writer.** The v2 writer renders each tracked-issue item only as an ADR-status item, in the literal `ADR status line:` field, and the item's ID occurs in the drain-targets ledger (**Change Process Guide** §3.5.2.1, form (b)). It cannot express a TI item closed as satisfied through PF09 or PF30 pointers (form (a), with the `PF09 pointers:` and `TI-<id> pointers:` fields); such a close needs a later source-schema version.  
  * **Closure decision with an accepted `TOOLING_BLOCKED` check (v2 writer).** A v2 `SATISFIED` decision needs every check of the change's current QA plan recorded in the QA step-logs manifest as `PASS`, or as `TOOLING_BLOCKED` where exactly one closure-override gap in the ADR block names that check. A check recorded as `FAIL_BEHAVIOR`, `FAIL_TOOLING` or `PARKED`, or a planned check the manifest does not record, blocks `SATISFIED`. A `TOOLING_BLOCKED` check accepted under the override is never PASS evidence for a `MET` criterion. **Change Process Guide** §3.5.4 owns the ADR block, the closure override and the no-posture-only-PASS rule.  

`````

- Basis: HDE Build Notes v13.8.8 addendum 2.17 resolutions A and B and its drainage table ("HDE Governance §2.0.19 'Close report minimal content'": carry resolution A; "HDE Governance §2.0.19 canon-pointer fields": the generic v2 writer supports only form (b)); addendum 2.16 LR7-O9 (the HDE Governance §2.0.19 row); addendum 2.15 C-3 as superseded for pointer items by 2.17; the ADR row's "literal `ADR status line:` field it renders for a TI item". Writer behaviour checked on main: `tools/qa/generate_epic_close_pack.py` renders `ADR status line:` for each tracked issue and refuses an override gap that is duplicated or names a non-`TOOLING_BLOCKED` check (`CLOSURE_OVERRIDE_INVALID`). Change Process Guide §3.5.2.1 forms (a) and (b) and §3.5.4 "Closure override" and "No posture-only PASS" were read on main.
- Rationale: Records, at the canon-pointer fields, that the v2 writer expresses a TI only through `ADR status line:` (form (b)), and carries resolution A's SATISFIED rule into the close-report requirements.

## RL-05 — REPLACE

- Ledger rows: A15, A16, A17 with X03
- Change type (report classification): CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **2\. Acceptance Policy — A3–A4–A7 \[Required-Now\]**`
  - `## **2.0 Acceptance Tokens (single-home roster) \[Required-Now\]**`
  - `### **2.0.19 QA bootstrap & harness (EPIC021+)**`
- Original-bound location: baseline line 975, UTF-8 byte offsets 147801–147881 (end exclusive)
- Expected occurrence count of the old block in the whole document: 1. Observed: 1.

Old block (exact, removed) (80 bytes, SHA-256 `3f9174d6822bab95efbc6cd7225012d78bf15780ab9ea7e3420b03ee1e6ae194`):

`````text
`audit/EPIC-###_MANIFEST.json` MUST include `key_outputs` as a JSON object (map)
`````

Replacement block (exact) (156 bytes, SHA-256 `4cf6ad4829ffa501b200669725bcf48cbd1c1aa2190adef319418833df6faf5b`):

`````text
The close-pack manifest, `audit/EPIC-###_MANIFEST.json` or, for a CRD, `audit/HDE-CRD-NNNN_MANIFEST.json`, MUST include `key_outputs` as a JSON object (map)
`````

- Basis: Same basis as RL-01: the ADR canon-table row names "Close-pack manifest `key_outputs` shape (normative)" as a locus for the CRD prefix.
- Rationale: Names the CRD manifest beside the Epic one in the `key_outputs` shape rule.

## RL-06 — INSERT

- Ledger rows: A01
- Change type (report classification): CANON_UPDATE
- Operation: `INSERT`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**`
  - `## **9.1 Single-home doctrine (routing by title)**`
  - `### **9.1.3 Artifact storage and execution-surface selection \[Required-Now\]**`
- Original-bound gap: after baseline line 2454, before baseline line 2455 (UTF-8 byte offset 319407)
- Expected gap occurrence: 1. Observed: BEFORE anchor 1, AFTER anchor 1, BEFORE+AFTER contiguous 1. Neither anchor is changed.

BEFORE anchor (exact, retained) (50 bytes, SHA-256 `d3a0a9c5efb9e63aa68a80a2fce68071d47ab7b315b3608895c5895d81f71153`):

`````text
fit the task and improve the complete operation.


`````

AFTER anchor (exact, retained) (43 bytes, SHA-256 `8e2e34740f2b36be4bf39db85b18832ef56cef7c1bc66807ded736f114460502`):

`````text
Execution-surface eligibility is bounded by
`````

Inserted text (exact) (1316 bytes, SHA-256 `5a94125091f1a0bfc939223d3a77292f7133f24bdcb0de91e312d3f9503878fb`):

`````text
**GCFPE model and reasoning-level guidance.** Within the Glow Change Flow Prompt Ecosystem (GCFPE) described in §9.1.6, the TypeSafe reading replaces the advice on model and reasoning level in the paragraph above; advice on execution surface is unchanged. This applies to every GCFPE downstream-session prompt and handoff, and to every management or facilitation relay that hands GCFPE work to a session.

* The model and reasoning-level guidance for the session is the reading produced by the installed TypeSafe scoring skill, reported as the skill prints it: its cell, every probability and its flags. The Product Owner picks the model and setting, and the pick is recorded with the reading.
* No agent gives its own recommendation, assessment or ranking of model, reasoning level or effort, beside the reading or in place of it.
* A reading that cannot be obtained is reported as not read, with the reason. No substitute recommendation is given.
* The provider-neutrality rule in the next paragraph does not apply to the TypeSafe scoring skill within this scope. It continues to apply to the model and surface that perform the work: the reading informs the Product Owner's pick and requires no model.
* A reading selects no model and is not an approval or a gate. This rule does not extend to other ecosystems.


`````

- Basis: HDE Build Notes v13.8.8 addendum 2.1 rules 1 to 5 and its superseded-passages table ("HDE Governance §9.1.3, the sentence beginning 'Every downstream-session prompt must receive task-specific human advice'": for the GCFPE, advice on model and reasoning level is replaced by rules 2 to 4; advice on execution surface is unchanged), and its nonclaims (no other ecosystem, no model selection, a reading is not an approval or gate).
- Rationale: Drains the GCFPE TypeSafe-reading rule beside the general advice sentence it supersedes for the GCFPE, keeping the sentence for execution surface and for other ecosystems, and scopes the provider-neutrality rule as rule 5 states.

## RL-07 — REPLACE

- Ledger rows: A01
- Change type (report classification): CANON_UPDATE
- Operation: `REPLACE`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**`
  - `## **9.1 Single-home doctrine (routing by title)**`
  - `### **9.1.6 Prompt ecosystem governance and provenance \[Required-Now\]**`
- Original-bound location: baseline line 2505, UTF-8 byte offsets 331764–331833 (end exclusive)
- Expected occurrence count of the old block in the whole document: 1. Observed: 1.

Old block (exact, removed) (69 bytes, SHA-256 `7d728735d046d5de1ef3320c41081e1190ee98f041543da8a05019e12aa1bd80`):

`````text
compatibility, model guidance, releases, defects and skill alignment;
`````

Replacement block (exact) (121 bytes, SHA-256 `10d40893f00411b97694773a5a4e54de27d162e56b688e1487528c5b55c329e6`):

`````text
compatibility, model guidance (for the GCFPE, the TypeSafe reading under §9.1.3), releases, defects and skill alignment;
`````

- Basis: HDE Build Notes v13.8.8 addendum 2.1, superseded passage "HDE Governance §9.1.6": the Managing Prompt Engineer's "model guidance" for the GCFPE is the reading in rule 2.
- Rationale: Makes the Managing Prompt Engineer's model guidance for the GCFPE the TypeSafe reading.

## RL-08 — INSERT

- Ledger rows: Target rule (PF04 §9.3 and §9.3.1) for A01, A11, A15, A16, A17, A18
- Change type (report classification): DOC_HYGIENE (change-history entry required by the target)
- Operation: `INSERT`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**`
  - `## **9.2 What requires a Doc-Delta \[Required-Now\]**`
- Original-bound gap: after baseline line 2612, before baseline line 2613 (UTF-8 byte offset 349634)
- Expected gap occurrence: 1. Observed: BEFORE anchor 1, AFTER anchor 1, BEFORE+AFTER contiguous 1. Neither anchor is changed.

BEFORE anchor (exact, retained) (447 bytes, SHA-256 `0fc70cc46cc9606c9e2d47ff451687bf42b8b9d814007b456335c37d8f24179b`):

`````text
> Change Log entry (one line): v2.8.7 | GOV-20261009-gtwpe-pf04 | NON_EPIC | Scope: Reader v2 and errors; repository authority; vendor QA and execution; functional agent governance | Targets: §0.2, §0.4, §2.0, §2.2, §3.3–3.4, §8.1, §9.1.2–9.1.6, §9.7.7, §9.7.9, §9.8.2, §10, §11.1, §12–13, §15.2, Appendices A/B/D | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261009-gtwpe-pf04

`````

AFTER anchor (exact, retained) (57 bytes, SHA-256 `66c397ea614cb823ef0c1a7d7b7d6c495c250953ed3b8f37b56f4db9b11fa094`):

`````text


> ---

> ## **9.4 Doc-Delta template \[Required-Now\]**
`````

Inserted text (exact) (4098 bytes, SHA-256 `317eb0563b62642a5c34a847694bf4f0cb43d9a4cc1dfaa87492cfebca624bbe`):

`````text

v2.8.8 | GOV-20261026-gtwpe-pf04 | NON_EPIC | Scope: GCFPE TypeSafe model guidance; business case per requirement and work unit; CRD close packs and the generic v2 close-pack writer | Targets: §2.0.19, §9.1.3, §9.1.6, §9.7.7, §11.2, Appendix D.0 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261026-gtwpe-pf04

> DOC-DELTA-ID: GOV-20261026-gtwpe-pf04
>
> Date / Author: 2026-10-26 / executing document agent in Nathan's T-PF04 document session
>
> PF04 version: v2.8.8
>
> Record class: NON_EPIC
>
> Epic ID: NOT APPLICABLE - NON_EPIC
>
> Draft / binding surface: NOT APPLICABLE - NON_EPIC
>
> Stable record surface: PF04 §9.3.1 / GOV-20261026-gtwpe-pf04
>
> Scope: Acceptance/Evidence; Governance/Documentation
>
> Targets (section anchors): §2.0.19, §9.1.3, §9.1.6, §9.7.7, §11.2, Appendix D.0
>
> Summary (≤ 5 bullets):
>
> 1) Make the TypeSafe reading the GCFPE model and reasoning-level guidance, with no agent recommendation, and scope the provider-neutrality rule accordingly.
> 2) Require a business case of beneficiary, evidence, benefit and measure for every Epic and CRD requirement and every work unit, with no cost ceiling, and state where it is checked.
> 3) Name the CRD close-pack pair beside the Epic pair in the path-of-record, the close report and manifest rules and Appendix D.0, with the generic v2 close-pack writer as producer.
> 4) Record that the v2 writer renders a tracked-issue item only through the literal `ADR status line:` field, and how a v2 `SATISFIED` decision treats a `TOOLING_BLOCKED` check named by a closure-override gap.
> 5) Remove the draft label from the §11.2 scope line, keep HDE Build Notes references title-only and leave the §9.1.1 review-chain entry unchanged.
>
> Acceptance impact (binary gates to update or verify): Specification approval and the change-wide Implementation Plan review check a business case for every requirement and work unit, with no cost ceiling; the close-pack path-of-record, the close report and manifest rules and Appendix D.0 include the CRD pair; a v2 `SATISFIED` decision accepts a `TOOLING_BLOCKED` check only where exactly one closure-override gap names it. The A3, A4, A7 and rails gates are unchanged. No new or satisfied token, QA verdict, OPS result or acceptance decision is claimed.
>
> Evidence updates (titles and paths only): No governed evidence artifact, golden, script, header snapshot, CI job, Human Evidence Index, hash sentinel, Machine Mirror or path proof is created or regenerated by this document revision. The added pointers name the existing generic close-pack writer `tools/qa/generate_epic_close_pack.py` and the CRD close-pack path form `audit/HDE-CRD-NNNN_close_report.md` and `audit/HDE-CRD-NNNN_MANIFEST.json`; their owning writers and evidence contracts remain in force.
>
> Freeze-pack impact: No; this document revision cuts, recomputes, activates and promotes no release and changes no release member.
>
> Routing (titles only confirmations): Plan Templates owns the business-case template fields. Change Process Guide owns the close-pack contents, the ADR block and the closure override. HDE Schemas and Artifacts and HDE Mechanics Guide own the v2 source schema, the writer mechanics and the `key_outputs` minimum. HDE Build Notes supplies the scoped overrides.
>
> Rollout plan: Nathan's authorized publication of the complete revised PF is a separate manual action. No runtime staging, canary, deployment or pointer flip is performed by this revision. A document backout uses the retained v2.8.7 source through ordinary authorized publication. Runtime monitoring and rollback retain their existing owners and controls.
>
> Change Log entry (one line): v2.8.8 | GOV-20261026-gtwpe-pf04 | NON_EPIC | Scope: GCFPE TypeSafe model guidance; business case per requirement and work unit; CRD close packs and the generic v2 close-pack writer | Targets: §2.0.19, §9.1.3, §9.1.6, §9.7.7, §11.2, Appendix D.0 | Acceptance: None | Evidence: None | Freeze-pack: No | Canonical record: PF04 §9.3.1 / GOV-20261026-gtwpe-pf04

`````

- Basis: The target's own rules: PF04 §9.3 ("Every normative change MUST add a short Doc-Delta entry to §9.3.1") and §9.3.1 (record class, stable identity `GOV-YYYYMMDD-<shortslug>`, local summary grammar, nested §9.4 record for `NON_EPIC`). TW-DRAIN-10: the entry names the version TW-APPLY-10 will derive (v2.8.8, the final numeric component of v2.8.7 bumped once) and the preparation date 2026-10-26 as its revision date.
- Rationale: The change log is the target's required version-to-change ledger; without the entry the v2.8.8 change would be unlogged.

## RL-09 — INSERT

- Ledger rows: A11 with A18
- Change type (report classification): CANON_UPDATE
- Operation: `INSERT`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **9\) Change Management — Doc-Delta Hooks & Merge Gates \[Required-Now\]**`
  - `## **9.7 Token fidelity & plan approval rails \[Required−Now\]**`
  - `### **9.7.7 Plan approval gate (anti-thrash; token scope disciplined)**`
- Original-bound gap: after baseline line 2826, before baseline line 2827 (UTF-8 byte offset 368599)
- Expected gap occurrence: 1. Observed: BEFORE anchor 1, AFTER anchor 1, BEFORE+AFTER contiguous 1. Neither anchor is changed.

BEFORE anchor (exact, retained) (74 bytes, SHA-256 `9a2f4fa2f7a1bae280cc477a677ff621749fff74774161061996f41379bcf0a9`):

`````text
reviewers MUST return the plan for revision and MUST NOT approve it.
```


`````

AFTER anchor (exact, retained) (117 bytes, SHA-256 `4c45a9e4fc594830df9543096d08f0689703999b9817f023388b683fd9982a0b`):

`````text
* **Non-blocking presentation variance (including heading levels, markup wrappers, and rendered escape characters).**
`````

Inserted text (exact) (1825 bytes, SHA-256 `d28d89437de8477970bb96d60515366f8565496b424a432f4cbf1e7c86aba8df`):

`````text
* **Business case for every requirement and work unit (Epics and CRDs).** Every Specification requirement, of an Epic or a CRD, and every work unit states a business case. The Epic Specification Business Case section above remains required; this rule adds a business case to each requirement and each work unit, for CRDs and Epics alike.  
  * Required fields:  
    * Beneficiary: who gains (Glow users, the production operator or the delivery team).  
    * Evidence: the observed incidents or measurements that show the problem, cited. A forecast is not evidence.  
    * Benefit: what changes for the beneficiary, in user outcome, risk, time or money.  
    * Measure: how the benefit is checked after delivery.  
  * Not a business case: more complete or more faithful evidence, CI, tooling or records for their own sake; conformance to canon; and "could prevent" without an observed incident. Internal tooling qualifies only when its expected saving, from observed incident data, exceeds its expected cost.  
  * No cost ceiling: a requirement or work unit states no budget in sessions, elapsed days, review rounds or pushes. Spend, elapsed time and the number of sessions, review rounds or pushes are not, by themselves, a reason to stop work or return it to the Product Owner. The CI cost stewardship rules of §4.3.9 are unchanged.  
  * Gates:  
    * Specification approval blocks a requirement without a business case, for CRDs and Epics alike.  
    * The change-wide Implementation Plan review (IA-30) checks each work unit's business case. PR-10 carries it into the PR Instruction, and `PR Implementation Proceed` is given against it.  
    * A work unit whose business case is met stops; further work on it needs a new business case.  
  * **Plan Templates** owns the business-case fields of each template.  

`````

- Basis: HDE Build Notes v13.8.8 addendum 2.11 rules 1 to 3 and its drainage row ("HDE Governance §9.7.7 and Plan Templates 'Business Case (MUST)'": the Business Case applies to every requirement and work unit of Epics and CRDs, rules 1 and 2), as narrowed by addendum 2.18 rules 1 to 4 (no cost ceiling; work continues until done; gates without a ceiling; the internal-tooling sentence compares with expected cost).
- Rationale: §9.7.7 required a Business Case for Epic Specifications only; the rule now extends to each Epic and CRD requirement and each work unit, without a ceiling, with the gates where it is checked.

## RL-10 — REPLACE

- Ledger rows: Target hygiene under the TW-DRAIN-10 marker rule (no source row)
- Change type (report classification): DOC_HYGIENE
- Operation: `REPLACE`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **11\. Vendor Ingest Governance (HDAPI) \[Required-Now\] / \[Speculative\]**`
  - `## **11.2 Live call policy \[Speculative\]**`
- Original-bound location: baseline line 4016, UTF-8 byte offsets 518843–518872 (end exclusive)
- Expected occurrence count of the old block in the whole document: 1. Observed: 1.

Old block (exact, removed) (29 bytes, SHA-256 `8943e11382e63cc4cb5b4a0bf4c3a3e6df657f239106e21967a5d8ba68ba54de`):

`````text
**Scope (normative, draft).**
`````

Replacement block (exact) (22 bytes, SHA-256 `218632be990f3e63218f66aebbc50c6996e1630e83c162f3c91ee2af4230ff74`):

`````text
**Scope (normative).**
`````

- Basis: TW-DRAIN-10 100926.1, "Exact redline contract": the revised PF carries no `Draft` or similar status language about the document unless canon requires that exact language there, and the preparer prepares the redlines that remove any other such marker, which that rule authorizes as hygiene. PF04 §0.3 defines the section tags; no canon requires the word "draft" in the §11.2 scope line.
- Rationale: The §11.2 scope line called its policy text a draft; the section heading keeps its `[Speculative]` tag (§0.3), which carries the section's status, so the word adds only drafting-status language about the document's own text.

## RL-11 — INSERT

- Ledger rows: A15, A16, A17 with X03
- Change type (report classification): CANON_UPDATE
- Operation: `INSERT`
- Target document: PF04-Canon-HDE-Governance (v2.8.7 baseline)
- Section path (authored headings, outermost first):
  - `# **Appendix D — Evidence Index (titles/paths only) \[Required-Now\]**`
  - `## **D.0 Close-pack & release manifests (admin)**`
- Original-bound gap: after baseline line 4517, before baseline line 4518 (UTF-8 byte offset 561319)
- Expected gap occurrence: 1. Observed: BEFORE anchor 1, AFTER anchor 1, BEFORE+AFTER contiguous 1. Neither anchor is changed.

BEFORE anchor (exact, retained) (49 bytes, SHA-256 `ff0328d990583c7c56577f6ba200e378766a4620a4a1e2e6515ad6fa7c4ea3e1`):

`````text
sibling at the deterministic `audit/` location.)

`````

AFTER anchor (exact, retained) (53 bytes, SHA-256 `c7052d1213b6c9a48fa3ba19b4523fc0c38f41100b745b0b03140c140331d185`):

`````text

**No relocation / no dual-home acceptance binding.**
`````

Inserted text (exact) (412 bytes, SHA-256 `4e00b6be2585b09b709919541833e72694b59888408c0bfc3f4e089f950fa52d`):

`````text

For a CRD, the pair uses the CRD ID as its prefix, with the same co-located `.path_proof.txt` siblings:

* `audit/HDE-CRD-NNNN_close_report.md`  
* `audit/HDE-CRD-NNNN_close_report.md.path_proof.txt`  
* `audit/HDE-CRD-NNNN_MANIFEST.json`  
* `audit/HDE-CRD-NNNN_MANIFEST.json.path_proof.txt`  
  (Where `NNNN` is the CRD number, zero-padded to at least four digits, e.g., `0002`. §2.0.19 names the producer.)

`````

- Basis: Same basis as RL-01: the ADR canon-table row names Appendix D.0. The co-located path proofs `audit/HDE-CRD-0002_close_report.md.path_proof.txt` and `audit/HDE-CRD-0002_MANIFEST.json.path_proof.txt` exist on main.
- Rationale: Appendix D.0 lists only the Epic pair; the CRD pair and its path proofs are added beside it.

END OF REDLINES
