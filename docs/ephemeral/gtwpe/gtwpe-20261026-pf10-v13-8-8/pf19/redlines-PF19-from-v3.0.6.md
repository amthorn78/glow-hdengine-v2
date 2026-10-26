# PF19 redlines from v3.0.6 — gtwpe-20261026-pf10-v13-8-8, task T-PF19

## 1. Package identity

- **Artifact:** exact redlines package prepared under TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff, fetched live 2026-10-26). Preparation outcome: **READY**. Save completeness is recorded in the proof log after read-back.
- **Target:** PF19-Canon-Glow-QA-Guide, version v3.0.6, `docs/pfcanon/PF19-Canon-Glow-QA-Guide-v3.0.6.md`; Git blob `1d86fdb495d49ae85efae9ec53aa9a9968905122`; raw-byte SHA-256 `1a005db7ffbe5626163afdaf9a62bfc10dd57725c36b5fc6097be15ed7c9c639`; 679,140 bytes; 5,613 LF-terminated lines; no CR bytes. Read from `origin/main` at `0838ba08254eaefc888019df49a06aa2ae99cc6c`; the blob is identical at the ledger baseline `9dda63dd3f05f496c3ff67e95da78550d3950c5a`.
- **Change-bearing sources, in source order:**
  1. `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` (HDE Build Notes v13.8.8; blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`; SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter lines 1–223; addenda 2.15 (lines 1620–1690), 2.16 (1691–1825), 2.28 (3078–3175), 2.30 (3259–3360) and 2.31 (3361–3470), each read in full.
  2. `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md` (v1.1, approved; blob `c4802a5a7fa33db38d42d8a7f64679cd18b50480`): S-APR, lines 147–193, as overlaid by delta 01 C-8 to C-12 (`docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091bcba3d751fcb17ae392a1ceca8bbb`). The overlay leaves the S21 canon-impact and drainage-target bullets unchanged.
- **Supporting reading (not change sources):** the S21 ADR `docs/adr/hde/close_pack_writer_adr.md` (X03; blob `2d91679a198168958bf8b32c5f8b5459ee13de5b`), Decision section and "Affected canon and drainage consequences"; the Product Owner direction `docs/ephemeral/HDE-CRD-0002-po-direction-qa-evidence-persistence-v1.0.md` (X08; blob `03377747a384cc0485fde079e2b6b4640fc23c82`), whole file; HDE Build Notes v13.8.8 addenda 2.17 (lines 1826–1955) and 2.18 (lines 1956–2081) for supersession of 2.15 and 2.16; PF03-Reference-Technical-Writing-Best-Practices v1.8.8.
- **Ledger:** `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` (blob `74944b261c0ebb2f80a416fb004b9a913da592d1`, identical on `main` and at the routing commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7`); task T-PF19; rows A15, A16, A28, A30, A31 and S-APR, with X03 and X08.
- **Run identity:** `gtwpe-20261026-pf10-v13-8-8/T-PF19/drain-run-1`, prepared 2026-10-26.
- **Originating preparer:** the Claude Code cloud session https://claude.ai/code/session_01UYxoWoyzGiVWTbkVFR3TqE, started by Nathan for T-PF19 and authorized to run TW-DRAIN-10 then TW-APPLY-10 in sequence. No subagent or other session took part.
- **Proof log:** `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/pf19/redlines-PF19-from-v3.0.6.proof-log.md`.
- **Held item:** H-02 (PO-2, "Do not pin tool versions") has no decided home and is not drafted.

## 2. Literal convention

Each literal sits in a fence of four backticks with no info string. The literal is every line between the opening and the closing fence, each followed by exactly one LF; it therefore always ends with LF, and an empty line inside the fence contributes one LF. Labels, the JSON-escaped cross-check and the byte counts are not part of the literal. The JSON-escaped form shows the same bytes with escapes, including trailing spaces; where the two disagree, the package is invalid.

Every anchor and old block was resolved once against the unchanged baseline bytes. For `INSERT`, the BEFORE anchor ends exactly where the AFTER anchor begins; that boundary is the insertion gap, and neither anchor is consumed.

## 3. Document-control inputs for TW-APPLY-10

No redline in this package touches the header; TW-APPLY-10 derives the document-control fields under its header contract.

- **Native header schema (baseline lines 3–10, `## **0.1 Header**`):** `**Title:** PF19-Canon-Glow-QA-Guide`, `**Status:** Canon`, `**Version:** v3.0.6` (dotted numeric with a `v` prefix), `**Effective date:** 2026-10-09` (`YYYY-MM-DD`), `**Last Update Gate:** BN 13.5; HDE-EPIC040-specification-v1.1-approved.md; HDE-EPIC040-CL-E-10-closure-decision-v1.2.md`, `**Invocation tag:** INV-f2ac55d77ce9aacc`. Lines 5 to 9 end with two spaces; line 10 does not.
- **Internal restatements of version or date:** none outside the header (searched for `3.0.6` and `2026-10-09`).
- **Sources that justified the update, in source order:** (1) the PF10 file `PF10-HDE-Build-Notes-v13.8.8.md`, version 13.8.8; (2) `HDE-CRD-0002-specification-v1.1-approved.md`. Delta 01 justified no change of its own (its C-8 to C-12 leave S-APR's S21 bullets unchanged). X03 and X08 are supporting reading under the ledger and justify no change of their own.
- **Status:** `Canon`; the content change does not alter the document's classification.
- **Change or revision history entry:** none required. PF19 keeps no revision log; §12.1 "Living document" sets no per-revision entry, and §13 "Change QA History" is an event-bounded record of selected changes ("It is not a complete change timeline"). No assigned row selects an HDE-CRD-0002 entry.
- **Draft, placeholder or editorial markers:** none found in the baseline outside rule text that canon requires there (§3.4.10 names `[SNIP: lines omitted]` as an approved marker, and §10.6 and §11.3 use `TBD` and `OPEN/TBD` as rule vocabulary); no hygiene redline is needed. The section-level labels "(NEW)" and "(new posture)" in two §3.4 headings describe sections, not the document, and headings are protected.

## 4. Redlines

### RL-01 — INSERT

- **Redline:** RL-01
- **Ledger rows and source items:** A31 (PF10 2.31 rule 4 and "Relationship to existing HDE Build Notes guidance")
- **Change type:** NEW_CANON
- **Operation:** `INSERT`, applied once
- **Target document:** PF19-Canon-Glow-QA-Guide (v3.0.6 baseline above)
- **Heading path (raw baseline heading lines, outermost first; each occurs once):**
  - `# **3\. Post-commit QA (staging/prod)**`
  - `## **3.1 Intent**`
  - `### **3.1.3 Permanent drainage and post-closure administration**`
- **Original-bound location:** gap between baseline lines 516 and 517 (start of line 517) (line numbers are informational; the literals below are authoritative)
- **Expected occurrence:** one gap, defined by one BEFORE anchor and one AFTER anchor, each occurring once
- **Controlling basis:** HDE Build Notes v13.8.8 addendum 2.31, "Required canon drainage": Glow QA Guide §3.1.3, state that the close mutation set precedes the closure decision, outside the post-closure drainage rule; content from 2.31 rule 4 (entries, exit, what it owns) and its relationship note (the close mutation set is a closure prerequisite, and canon drainage is not).
- **Rationale:** §3.1.3 states only the post-closure drainage rule; without this paragraph a reader could treat the close mutation set as post-closure administration. The paragraph states the set's place before the closure decision and routes the stage to its governing homes by title.

**BEFORE anchor (literal):**

````
Permanent PF drainage and historical/board administration follow the actual closure decision under the authorized process. Required repository-documentation delivery before QA remains distinct. Known but undrained corrections are recorded truthfully in substantive artifacts and the applicable temporary PF10 authority, with owners and follow-up references. A missing later PF publication or manual recording receipt alone does not invalidate an approved Plan, readiness, QA verdict or closure.

````

**BEFORE anchor (JSON-escaped, cross-check):**

````
"Permanent PF drainage and historical/board administration follow the actual closure decision under the authorized process. Required repository-documentation delivery before QA remains distinct. Known but undrained corrections are recorded truthfully in substantive artifacts and the applicable temporary PF10 authority, with owners and follow-up references. A missing later PF publication or manual recording receipt alone does not invalidate an approved Plan, readiness, QA verdict or closure.\n\n"
````

BEFORE anchor: 496 UTF-8 bytes; SHA-256 `da3347e9610eba399372fbc49ee45a319759c4024d8c94154a3d79fb76265cd0`; expected occurrence in the baseline: 1 (as anchor).

**AFTER anchor (literal):**

````
QA work products must not require their own permanent drainage, PF edits or PF23 publication as execution, acceptance or closure outputs. Incomplete required QA, a substantive objective failure, inadequate authority, missing decisive evidence or an incoherent governed evidence family remains actionable under its actual contract. Distinguish those defects from pending documentation. Prepared, approved, applied, delivered and board-updated are different states; only actual receipts establish the latter actions.
````

**AFTER anchor (JSON-escaped, cross-check):**

````
"QA work products must not require their own permanent drainage, PF edits or PF23 publication as execution, acceptance or closure outputs. Incomplete required QA, a substantive objective failure, inadequate authority, missing decisive evidence or an incoherent governed evidence family remains actionable under its actual contract. Distinguish those defects from pending documentation. Prepared, approved, applied, delivered and board-updated are different states; only actual receipts establish the latter actions.\n"
````

AFTER anchor: 515 UTF-8 bytes; SHA-256 `3abe74cdd7488197a98496354bf8a659b88beec227dd1d1ee347cc9d937e6ba6`; expected occurrence in the baseline: 1 (as anchor).

**INSERT payload (literal):**

````
The close mutation set is outside the post-closure drainage rule above. It comprises the change's close pack, its two ledgers, its same-run close evidence and their Human Evidence Index and Machine Mirror registration. It is produced after the final QA Report records verdict PASS, or after a `DO_NOT_CLOSE` closure decision whose return work is a missing, incomplete or defective close mutation set. It lands through the Product Owner's merge of the close pull request before the closure decision is made. The close mutation set is a closure prerequisite and precedes the closure decision; permanent PF drainage is not a closure prerequisite. HDE Build Notes governs the change-flow stage that produces the set, including its entries, its exit to the closure decision and its repair of close tooling; Change Process Guide governs the close pull request and its close-pack files.

````

**INSERT payload (JSON-escaped, cross-check):**

````
"The close mutation set is outside the post-closure drainage rule above. It comprises the change's close pack, its two ledgers, its same-run close evidence and their Human Evidence Index and Machine Mirror registration. It is produced after the final QA Report records verdict PASS, or after a `DO_NOT_CLOSE` closure decision whose return work is a missing, incomplete or defective close mutation set. It lands through the Product Owner's merge of the close pull request before the closure decision is made. The close mutation set is a closure prerequisite and precedes the closure decision; permanent PF drainage is not a closure prerequisite. HDE Build Notes governs the change-flow stage that produces the set, including its entries, its exit to the closure decision and its repair of close tooling; Change Process Guide governs the close pull request and its close-pack files.\n\n"
````

INSERT payload: 881 UTF-8 bytes; SHA-256 `1cdec8e766eb0ac066ee0d8d745a7e844e607de161e116f9ec7fbc0f8d030292`; expected occurrence in the baseline: not applicable (new text).

### RL-02 — INSERT

- **Redline:** RL-02
- **Ledger rows and source items:** A28 and A30 with X08 (PO-5: the evidence-persistence rule into §3.4.3)
- **Change type:** NEW_CANON
- **Operation:** `INSERT`, applied once
- **Target document:** PF19-Canon-Glow-QA-Guide (v3.0.6 baseline above)
- **Heading path (raw baseline heading lines, outermost first; each occurs once):**
  - `# **3\. Post-commit QA (staging/prod)**`
  - `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
  - `### **3.4.3 Evidence layout: current-state first (new posture)**`
- **Original-bound location:** gap between baseline lines 723 and 724 (start of line 724) (line numbers are informational; the literals below are authoritative)
- **Expected occurrence:** one gap, defined by one BEFORE anchor and one AFTER anchor, each occurring once
- **Controlling basis:** HDE Build Notes v13.8.8 addendum 2.28, "Required canon drainage" (PO-5: drain the evidence-persistence rule to Glow QA Guide §3.4.3), carried by addendum 2.30; rule text from the Product Owner direction record (X08) §3, direction E-1.
- **Rationale:** §3.4.3 places evidence at governed repository paths but does not state that QA evidence must be persisted there. E-1 is transcribed as stated; E-2 (re-litigating the evidence-only commit default) is a prompt and plan default owned by Kronos and the GCFPE-MGMT-10 maintenance owner, not drained here.

**BEFORE anchor (literal):**

````
Plan-created deliverables are allowed, but they MUST live under the stable check directory for the step that creates them and MUST be named explicitly in the plan.

````

**BEFORE anchor (JSON-escaped, cross-check):**

````
"Plan-created deliverables are allowed, but they MUST live under the stable check directory for the step that creates them and MUST be named explicitly in the plan.\n\n"
````

BEFORE anchor: 165 UTF-8 bytes; SHA-256 `8285d2902586ffade6be71b539d091a1bf49ddc92754ab05495e9a488f469f05`; expected occurrence in the baseline: 1 (as anchor).

**AFTER anchor (literal):**

````
#### **QA evidence and work-product path grammar (normative)**
````

**AFTER anchor (JSON-escaped, cross-check):**

````
"#### **QA evidence and work-product path grammar (normative)**\n"
````

AFTER anchor: 63 UTF-8 bytes; SHA-256 `9b1ed2589e4d3ae678f215b2ce810adc1377626f352badc0f25ac5a551ebc79f`; expected occurrence in the baseline: 1 (as anchor).

**INSERT payload (literal):**

````
Evidence persistence (normative). QA evidence is persisted in the repository. It is never left only in temporary or scratch storage.

````

**INSERT payload (JSON-escaped, cross-check):**

````
"Evidence persistence (normative). QA evidence is persisted in the repository. It is never left only in temporary or scratch storage.\n\n"
````

INSERT payload: 134 UTF-8 bytes; SHA-256 `fee57d904b47183d9fff4bd7742286c1f08960d71869b7e7970935609e02e4c8`; expected occurrence in the baseline: not applicable (new text).

### RL-03 — INSERT

- **Redline:** RL-03
- **Ledger rows and source items:** A15 with X03 (§3.4.3: the close-run family beside checks/)
- **Change type:** NEW_CANON
- **Operation:** `INSERT`, applied once
- **Target document:** PF19-Canon-Glow-QA-Guide (v3.0.6 baseline above)
- **Heading path (raw baseline heading lines, outermost first; each occurs once):**
  - `# **3\. Post-commit QA (staging/prod)**`
  - `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
  - `### **3.4.3 Evidence layout: current-state first (new posture)**`
  - `#### **QA evidence and work-product path grammar (normative)**`
- **Original-bound location:** gap between baseline lines 737 and 738 (start of line 738), inside the path-grammar table (line numbers are informational; the literals below are authoritative)
- **Expected occurrence:** one gap, defined by one BEFORE anchor and one AFTER anchor, each occurring once
- **Controlling basis:** HDE Build Notes v13.8.8 addendum 2.15, "The close-run evidence family (introduced)" and "Unresolved, with owners" (drainage of this family into Glow QA Guide §3.4.3); ADR canon table row "Glow QA Guide §3.4.3 Evidence layout: current-state first": name audit/qa/<change-dir>/close/ beside checks/ as the post-verdict close-run family. Addendum 2.17 leaves the family and its membership exception unchanged.
- **Rationale:** The path-grammar table is the approved-destination list for the QA root and its last row denies a destination to any recurring family not introduced by PF10; the close-run family is so introduced, so it receives its destination row beside the checks/ rows, with the close/-only membership exception scoped against §4.4.2.

**BEFORE anchor (literal):**

````
| Auxiliary check output | Prefer `audit/qa/<epic-id>/checks/<check_id>/tmp_<explicit_filename>` | Auxiliary output never replaces `primary.log`. Optional material under `results/` is not required or decisive unless an owning canon expressly promotes it. |
````

**BEFORE anchor (JSON-escaped, cross-check):**

````
"| Auxiliary check output | Prefer `audit/qa/<epic-id>/checks/<check_id>/tmp_<explicit_filename>` | Auxiliary output never replaces `primary.log`. Optional material under `results/` is not required or decisive unless an owning canon expressly promotes it. |\n"
````

BEFORE anchor: 257 UTF-8 bytes; SHA-256 `150830ff139a1020fc2632ff1095396ade12b460751da448f60550373a270c15`; expected occurrence in the baseline: 1 (as anchor).

**AFTER anchor (literal):**

````
| Stable epic-level mechanical metadata | `audit/qa/<epic-id>/00_meta/<canon_defined_filename>` | Use only for an exact owning-canon metadata path. It is not a catch-all or a substitute for check evidence. |
````

**AFTER anchor (JSON-escaped, cross-check):**

````
"| Stable epic-level mechanical metadata | `audit/qa/<epic-id>/00_meta/<canon_defined_filename>` | Use only for an exact owning-canon metadata path. It is not a catch-all or a substitute for check evidence. |\n"
````

AFTER anchor: 208 UTF-8 bytes; SHA-256 `c14c3209e83b6fc003a8b0f1bde948f1b13e724d68ff5f189d8ac0f894e336e2`; expected occurrence in the baseline: 1 (as anchor).

**INSERT payload (literal):**

````
| Post-verdict close-run evidence of an admitted CRD | `audit/qa/<crd-id>/close/<check_id>/primary.log`, with its sibling `primary.log.path_proof.txt` | Introduced by HDE Build Notes for a CRD that the canonical evidence updater admits; `<crd-id>` is the CRD's lower-case directory form, for example `hde-crd-0002`. Each close-run check has one primary holding same-run mechanical evidence of the change's close workflow, rendered from that check's captured command, exit code and output as a Plan Templates v2 step-log header, with the PASS, FAIL or BLOCKED posture that “Close-pack truthfulness and same-run execution” requires. Only the canonical evidence updater writes the family, after the final QA verdict; it neither reopens nor adds to `qa_step_logs_manifest.json` or any `checks/` primary. Its members are the validated primaries and path proofs under `close/`, and anything else there is refused. This membership rule is a scoped exception, for `close/` only, to the rule against inferring state by enumerating subdirectories (§4.4.2); that rule continues to govern `checks/` and every other part of the QA root, where `qa_step_logs_manifest.json` stays the authoritative index. No Epic close-run family is admitted. HDE Schemas & Artifacts and HDE Build Notes govern the family's artifact contract. |
````

**INSERT payload (JSON-escaped, cross-check):**

````
"| Post-verdict close-run evidence of an admitted CRD | `audit/qa/<crd-id>/close/<check_id>/primary.log`, with its sibling `primary.log.path_proof.txt` | Introduced by HDE Build Notes for a CRD that the canonical evidence updater admits; `<crd-id>` is the CRD's lower-case directory form, for example `hde-crd-0002`. Each close-run check has one primary holding same-run mechanical evidence of the change's close workflow, rendered from that check's captured command, exit code and output as a Plan Templates v2 step-log header, with the PASS, FAIL or BLOCKED posture that “Close-pack truthfulness and same-run execution” requires. Only the canonical evidence updater writes the family, after the final QA verdict; it neither reopens nor adds to `qa_step_logs_manifest.json` or any `checks/` primary. Its members are the validated primaries and path proofs under `close/`, and anything else there is refused. This membership rule is a scoped exception, for `close/` only, to the rule against inferring state by enumerating subdirectories (§4.4.2); that rule continues to govern `checks/` and every other part of the QA root, where `qa_step_logs_manifest.json` stays the authoritative index. No Epic close-run family is admitted. HDE Schemas & Artifacts and HDE Build Notes govern the family's artifact contract. |\n"
````

INSERT payload: 1318 UTF-8 bytes; SHA-256 `7f2af17247d39a3529337e42e0d984f82d538cff746a65ee3bf3bca4974c29d9`; expected occurrence in the baseline: not applicable (new text).

### RL-04 — REPLACE

- **Redline:** RL-04
- **Ledger rows and source items:** A15 with X03 (§3.4.3: the close-run family beside checks/)
- **Change type:** CONSISTENCY
- **Operation:** `REPLACE`, applied once
- **Target document:** PF19-Canon-Glow-QA-Guide (v3.0.6 baseline above)
- **Heading path (raw baseline heading lines, outermost first; each occurs once):**
  - `# **3\. Post-commit QA (staging/prod)**`
  - `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
  - `### **3.4.3 Evidence layout: current-state first (new posture)**`
  - `#### **Approved exceptions and external evidence families (normative)**`
- **Original-bound location:** baseline line 777 (line numbers are informational; the literals below are authoritative)
- **Expected occurrence:** one exact old block, occurring once
- **Controlling basis:** HDE Build Notes v13.8.8 addendum 2.15, "The close-run evidence family (introduced)"; ADR canon table row for Glow QA Guide §3.4.3.
- **Rationale:** The approved-exceptions list is closed ("limited to"; "There is no wildcard exception"); naming the close-run family under item 5 keeps the list consistent with RL-03.

**OLD (literal):**

````
5. exact owner-defined closeout surfaces;  
````

**OLD (JSON-escaped, cross-check):**

````
"5. exact owner-defined closeout surfaces;  \n"
````

OLD: 44 UTF-8 bytes; SHA-256 `b50847d443f2b64d1256533cdab39e1c7559a0c027a360883c955ef41ab27fcd`; expected occurrence in the baseline: 1.

**NEW (literal):**

````
5. exact owner-defined closeout surfaces, including the post-verdict close-run family of an admitted CRD under `audit/qa/<crd-id>/close/`;  
````

**NEW (JSON-escaped, cross-check):**

````
"5. exact owner-defined closeout surfaces, including the post-verdict close-run family of an admitted CRD under `audit/qa/<crd-id>/close/`;  \n"
````

NEW: 141 UTF-8 bytes; SHA-256 `5d8cb23bb22b8a372621710bd250c2b596749728772921f13059760e1d78bf3c`; expected occurrence in the baseline: not applicable (new text).

### RL-05 — INSERT

- **Redline:** RL-05
- **Ledger rows and source items:** A15 and A16 with X03 and S-APR ("Close-pack truthfulness and same-run execution": audit/qa/<change-id>/close/ as the CRD's same-run close evidence)
- **Change type:** CANON_UPDATE
- **Operation:** `INSERT`, applied once
- **Target document:** PF19-Canon-Glow-QA-Guide (v3.0.6 baseline above)
- **Heading path (raw baseline heading lines, outermost first; each occurs once):**
  - `# **3\. Post-commit QA (staging/prod)**`
  - `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
  - `### **3.4.11 Vendor and DB safety constraints (names-only)**`
- **Original-bound location:** gap between baseline lines 1118 and 1119 (start of line 1119) (line numbers are informational; the literals below are authoritative)
- **Expected occurrence:** one gap, defined by one BEFORE anchor and one AFTER anchor, each occurring once
- **Controlling basis:** ADR canon table row "Glow QA Guide 'Close-pack truthfulness and same-run execution (normative)' and 'Close report requirements (validator-bound; mechanical)'": name audit/qa/<change-id>/close/ as the home of same-run close evidence for a CRD; HDE Build Notes v13.8.8 addenda 2.15 (the family, its post-verdict status, no Epic family) and 2.16 "Required canon drainage"; Specification v1.1 "Canon, QA & Build Notes posture" (S21: where close-workflow run evidence lives).
- **Rationale:** The paragraph requires same-run close evidence but names no home for a CRD; the close-run family is that home and is the reason the approved QA manifest is not reopened after the verdict.

**BEFORE anchor (literal):**

````
Artifact presence alone is not sufficient when the close report claims the underlying gates ran. The evidence set MUST include same-run primary logs or step-scoped mechanical outputs that capture the exact commands executed and the resulting PASS, FAIL, or BLOCKED posture for the claimed close-pack and evidence-discipline checks.

````

**BEFORE anchor (JSON-escaped, cross-check):**

````
"Artifact presence alone is not sufficient when the close report claims the underlying gates ran. The evidence set MUST include same-run primary logs or step-scoped mechanical outputs that capture the exact commands executed and the resulting PASS, FAIL, or BLOCKED posture for the claimed close-pack and evidence-discipline checks.\n\n"
````

BEFORE anchor: 333 UTF-8 bytes; SHA-256 `a524291a0bafd67a6f065a94d76040c797cc9d71822e79de9a4918474ecf80ef`; expected occurrence in the baseline: 1 (as anchor).

**AFTER anchor (literal):**

````
When the close-pack family changes, every applicable changed governed artifact in that family MUST refresh coherently in the same change, including the close report, close manifest, and any changed acceptance map, acceptance-map viability log, step-logs manifest, Human Index, Machine Mirror, hash-sentinel, or sibling path-proof companion. A token/evidence matrix is included only when the approved work already uses one; its absence MUST NOT block otherwise sufficient exact-source evidence, and this optional posture does not waive any non-token closeout requirement.
````

**AFTER anchor (JSON-escaped, cross-check):**

````
"When the close-pack family changes, every applicable changed governed artifact in that family MUST refresh coherently in the same change, including the close report, close manifest, and any changed acceptance map, acceptance-map viability log, step-logs manifest, Human Index, Machine Mirror, hash-sentinel, or sibling path-proof companion. A token/evidence matrix is included only when the approved work already uses one; its absence MUST NOT block otherwise sufficient exact-source evidence, and this optional posture does not waive any non-token closeout requirement.\n"
````

AFTER anchor: 571 UTF-8 bytes; SHA-256 `7cc8af082f75a8c4a3c4576ccf6dc04c7f258341f4955c9b3ba2d9b54cc504a4`; expected occurrence in the baseline: 1 (as anchor).

**INSERT payload (literal):**

````
For a CRD that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/` (§3.4.3): one primary log per close-run check, each with its sibling path proof, published after the final QA verdict without reopening or adding to the change's approved QA step-logs manifest or any `checks/` primary. No Epic close-run family is admitted; an Epic needs its own explicit admission before it has one.

````

**INSERT payload (JSON-escaped, cross-check):**

````
"For a CRD that the canonical evidence updater admits, the home of that same-run close evidence is the post-verdict close-run family under `audit/qa/<crd-id>/close/` (§3.4.3): one primary log per close-run check, each with its sibling path proof, published after the final QA verdict without reopening or adding to the change's approved QA step-logs manifest or any `checks/` primary. No Epic close-run family is admitted; an Epic needs its own explicit admission before it has one.\n\n"
````

INSERT payload: 484 UTF-8 bytes; SHA-256 `a2c51a0172aa18383e022157477319eb8f2f928076d27aae11ad5924f91c1f1b`; expected occurrence in the baseline: not applicable (new text).

### RL-06 — INSERT

- **Redline:** RL-06
- **Ledger rows and source items:** A15 and A16 with X03 and S-APR ("Close report requirements")
- **Change type:** CANON_UPDATE
- **Operation:** `INSERT`, applied once
- **Target document:** PF19-Canon-Glow-QA-Guide (v3.0.6 baseline above)
- **Heading path (raw baseline heading lines, outermost first; each occurs once):**
  - `# **3\. Post-commit QA (staging/prod)**`
  - `## **3.4 EPIC017 Live QA pattern (Codespaces → Railway)**`
  - `### **3.4.11 Vendor and DB safety constraints (names-only)**`
- **Original-bound location:** gap between baseline lines 1138 and 1139 (start of line 1139) (line numbers are informational; the literals below are authoritative)
- **Expected occurrence:** one gap, defined by one BEFORE anchor and one AFTER anchor, each occurring once
- **Controlling basis:** ADR canon table row for the Glow QA Guide close-pack sections: name the v2 writer's rendering of the verbatim heading and pointer list; ADR Decision 3 and 4 (CRD paths of record; the v2 report's heading and pointer list); HDE Build Notes v13.8.8 addenda 2.15 (what is approved: one writer, v2 schema for Epic and CRD identities) and 2.16 "Required canon drainage"; Specification v1.1 "Canon, QA & Build Notes posture" (S21: which writer produces the close report). Current-repository facts inspected at origin/main 0838ba0 (see proof log).
- **Rationale:** The requirement names only an Epic report and no producer; the v2 writer now produces Epic and CRD reports and enforces the CRD close-run pointer, so the requirement names that rendering and routes the writer, schema and paths to their owners.

**BEFORE anchor (literal):**

````
The close report check validates required pointer strings as literal substrings; missing any required pointer is a mechanical FAIL for the close report check.

````

**BEFORE anchor (JSON-escaped, cross-check):**

````
"The close report check validates required pointer strings as literal substrings; missing any required pointer is a mechanical FAIL for the close report check.\n\n"
````

BEFORE anchor: 160 UTF-8 bytes; SHA-256 `d59dbb136bb6eb32977cb32a0f2658b04ec3108b7cb20f5faab37d8eabec83aa`; expected occurrence in the baseline: 1 (as anchor).

**AFTER anchor (literal):**

````
PO/operator must not be required to write prose summaries as part of execution. Narrative synthesis belongs in the close report and canon updates (titles-only routing).
````

**AFTER anchor (JSON-escaped, cross-check):**

````
"PO/operator must not be required to write prose summaries as part of execution. Narrative synthesis belongs in the close report and canon updates (titles-only routing).\n"
````

AFTER anchor: 169 UTF-8 bytes; SHA-256 `0ef15d658b477819e1d1cb12ab6fd0993b9b1b3fe08d7be6acd5302f92b8c9ef`; expected occurrence in the baseline: 1 (as anchor).

**INSERT payload (literal):**

````
The same requirements apply to a CRD close report, for example `audit/HDE-CRD-0002_close_report.md`. The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD: the heading `QA Rails — Open/Close (Final PR)` verbatim, and the “Acceptance and evidence pointers” list with one entry for each pointer the source records. For a CRD, the change's close-run family root, `audit/qa/<crd-id>/close/`, is a required pointer, and the writer refuses a source that omits it. HDE Mechanics Guide, HDE Schemas & Artifacts and Change Process Guide own the writer, its source schema and the close-pack paths of record.

````

**INSERT payload (JSON-escaped, cross-check):**

````
"The same requirements apply to a CRD close report, for example `audit/HDE-CRD-0002_close_report.md`. The generic close-pack writer renders both elements from a `close_candidate_source.v2` source, for an Epic or a CRD: the heading `QA Rails — Open/Close (Final PR)` verbatim, and the “Acceptance and evidence pointers” list with one entry for each pointer the source records. For a CRD, the change's close-run family root, `audit/qa/<crd-id>/close/`, is a required pointer, and the writer refuses a source that omits it. HDE Mechanics Guide, HDE Schemas & Artifacts and Change Process Guide own the writer, its source schema and the close-pack paths of record.\n\n"
````

INSERT payload: 667 UTF-8 bytes; SHA-256 `b3fba2306b779f4e3148e35c86692d19e4c4c522824d6db7cdfa3843a1fc3f91`; expected occurrence in the baseline: not applicable (new text).

## 5. Batch check

The six operations were resolved independently against the unchanged baseline: one span and five gaps, at baseline offsets 52419 (RL-01), 75977 (RL-02), 78334 (RL-03), 83507–83551 (RL-04), 128831 (RL-05) and 130960 (RL-06). No two operations share a gap; no gap lies at or inside the replaced span; no anchor intersects the replaced span. The full per-redline check, the one-pass simulation and the preservation proof are in the proof log.

END OF REDLINES
