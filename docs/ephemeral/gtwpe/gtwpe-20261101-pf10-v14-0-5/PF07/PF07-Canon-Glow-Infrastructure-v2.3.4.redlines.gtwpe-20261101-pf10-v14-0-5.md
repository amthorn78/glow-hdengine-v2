# PF07 redlines — gtwpe-20261101-pf10-v14-0-5 — T-18

## Package identity

| Field | Value |
| :---- | :---- |
| Redlines file | `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.md` |
| Proof log | `PF07-Canon-Glow-Infrastructure-v2.3.4.redlines.gtwpe-20261101-pf10-v14-0-5.proof-log.md`, in the same directory |
| Run identity | `gtwpe-20261101-pf10-v14-0-5/T-18/drain-r1` |
| Preparer | TW-DRAIN-10 100926.1 (Notion page `3f44590a05eb8172a314fe6b958bb9ff`, fetched live at the start of this step), run in the Claude Code document session Nathan started for T-18 on 2026-11-02 |
| Preparation outcome | `READY`; save state recorded in the proof log |
| Ledger | `docs/ephemeral/gtwpe/gtwpe-20261101-pf10-v14-0-5/LEDGER.md` at `a3632c0`; task T-18 (§8); rows C-02, C-03, C-17, C-18, C-26 |
| Target (original) | `docs/pfcanon/PF07-Canon-Glow-Infrastructure-v2.3.4.md`, title `PF07-Canon-Glow-Infrastructure`, v2.3.4, git blob `60fd3f0b3feff007491dc7add29a9c4491cbdf95`, SHA-256 `9e00712a3af2c1b498b5dddf5ada35c72b44952293d3b73ec3915cbba586d790`, 99,393 bytes, 1,443 LF characters (1,444 lines; the last line has no final LF), read at `origin/main` `e2b7427ff418ca8f08f05587c4a541308a76da56` |
| Source | `docs/pfcanon/PF10-HDE-Build-Notes-v14.0.5.md`, v14.0.5, git blob `9df074d90b59fe783c32f7cb3db25872d5dfe9d2`, SHA-256 `cea605d0475889bd9120a51947e23176ce7d2308eb5ab4503b040fd68ddf669d`; addendum 2.1 D-2 (l.277–344), D-3 (l.345–396) and context (l.205–224, l.491–516); 2.8 (l.1048–1145); 2.15 (l.1650–1868) |
| Simulated one-pass result | SHA-256 `6d07d8d3713cd603f52b9dc9daf094e408998f2aca8f52bd60a4eef50247952e`, 100,447 bytes, 1,446 LF characters (scratch only; Apply produces the final file) |

## Literal and operation conventions

- Every operation is `REPLACE` against the unchanged original target. No operation reads another operation's output.
- Each OLD and NEW literal is the exact text between its opening and closing four-backtick fence lines. The newline that ends the last literal line, just before the closing fence, is not part of the literal. Every other newline and every space inside the fence is part of it, including trailing double spaces.
- Each OLD literal is one or more complete original lines, without the newline that ends its last line. That newline stays in place after the replacement. Its expected occurrence count is over the whole original target.
- Section paths quote the original heading or bold-label lines exactly, including the leading spaces of the §2.4 subheading, the two trailing spaces of the §2.8 "**Scope.**" label and the U+2011 non-breaking hyphen in the §2.5 heading. They locate the edit; the OLD literal's unique occurrence is the binding locator.
- Original line numbers are informative only.
- Document-control fields (version, effective date, Last Update Gate) are left to TW-APPLY-10. The proof log supplies the header schema and source identity. PF07 has no change log or Doc-Delta entry section, so no history-entry redline is prepared.

## RL-01

- Ledger rows: C-02
- Source basis: PF10 2.1 D-2, l.281-289 (What governs; Selection; The base; No fallback) and l.307 (Basis: every recorded environment configures a base ending in /v2)
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.4 Env Deployment Inventory \[Required-Now\]**" > "  ### **Key-spelling and downgrade rules**"
- Original line(s): 352 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: D-2 decides that the configured base must end in exactly v1 or v2 and that the configured-base boundary is enforced, with HDE-CLI-API-Vendor-Ref governing route selection and that boundary. "May include the vendor API version path" permits an unversioned base and so contradicts it. The replacement records the value every environment in §2.4 holds (lines 282, 304, 334), which D-2's basis relies on, and routes the boundary and selection by title. It states no refusal behavior as delivered: the implementing change for Candidate CRD Items List item 9 is open (l.506).

OLD:

````
* The configured `HD_API_BASE_URL` may include the vendor API version path, for example `https://api.humandesignapi.nl/v2`.  
````

NEW:

````
* Every `HD_API_BASE_URL` value recorded in this section ends in the vendor API version segment `v2`, as in `https://api.humandesignapi.nl/v2`. The configured-base boundary and vendor route selection from the configured base are owned by **HDE-CLI-API-Vendor-Ref** by title.  
````

## RL-02

- Ledger rows: C-26
- Source basis: PF10 2.15 R-1, l.1704-1739 (Scope; deployed-service check; where an Epic's own surfaces are live); l.1666-1681 (relation to other canon: the dependency on whether an Epic touches a production surface is superseded); R-2 l.1741-1753; R-6 l.1792-1803
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.5 QA windows (names‑only)**" > "**Production-affecting Live QA infrastructure posture (names-only).**"
- Original line(s): 372 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: R-1 makes the live compat test, with its deployed-service check of the production HD Engine, part of every Epic's Live QA whatever the Epic changed, and supersedes the dependency on a finding that the Epic affects a production surface. This paragraph framed live proof only by that dependency. The replacement adds the unconditional test, routed by title (PF10-HDE-Build-Notes for the test and its waiver, HDE-Governance for execution, as R-6 keeps), names the PF07 facts the test relies on, and keeps the existing per-surface requirement, which R-1 says HDE Governance keeps governing, with "also" and "for those surfaces" added. The rest of the paragraph is unchanged.

OLD:

````
When an epic affects deployed service behavior, vendor ingest, HumanDesignAPI calls, request shaping, response mapping, database persistence or retrieval, database transport behavior, public or app-facing behavior, CLI/API behavior used in production, or environment-variable or secret-binding behavior, its live-proof requirement is governed by **HDE-Governance** and **Glow QA Guide**. For any surface used to produce a production feature described as functional in PF canon, **PF10-HDE-Build-Notes** governs the mandatory open-rails live vendor test with synthetic data only and its non-substitution rule; an exemption, a closed-rails test, or a non-vendor live step does not replace that scoped requirement. PF07 records the supporting infrastructure facts and does not define the step, PASS/FAIL predicate, token semantics, or QA procedure.
````

NEW:

````
**PF10-HDE-Build-Notes** governs the live compat test that every Epic's Live QA runs, whatever the Epic changed, including its deployed-service check of the production HD Engine, and who may waive any part of that test. **HDE-Governance** governs how the test is executed. For that test, PF07 records the CLI-local vendor smoke target (§2.7) and, for the deployed-service check, the production HD Engine service, base URL and deploy source (§2.6, §3.1, §4.1), its `/internal/version` ops identity surface (§2.3.3) and the shared production database (§2.2, §7.1).

When an epic also affects deployed service behavior, vendor ingest, HumanDesignAPI calls, request shaping, response mapping, database persistence or retrieval, database transport behavior, public or app-facing behavior, CLI/API behavior used in production, or environment-variable or secret-binding behavior, its live-proof requirement for those surfaces is governed by **HDE-Governance** and **Glow QA Guide**. For any surface used to produce a production feature described as functional in PF canon, **PF10-HDE-Build-Notes** governs the mandatory open-rails live vendor test with synthetic data only and its non-substitution rule; an exemption, a closed-rails test, or a non-vendor live step does not replace that scoped requirement. PF07 records the supporting infrastructure facts and does not define the step, PASS/FAIL predicate, token semantics, or QA procedure.
````

## RL-03

- Ledger rows: C-17 (decisions 3 and 7), C-18; wording also under C-26 (2.15 R-3)
- Source basis: PF10 2.8 decision 3, l.1068 (a CRD's lower-case ID is its directory form, hde-crd-nnnn); decision 7, l.1082 (close-run families under audit/qa/<crd-id>/close/ and audit/qa/<epic-dir>/close/); Epic, task, and status effects, l.1109. Wording: 2.15 R-3, l.1755-1759, and its CRD item, l.1825
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# 2\) Environments overview" > "## **2.8 GitHub Codespaces / local dev environments (names-only)**" > "**Scope.**  "
- Original line(s): 538 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: PF07 owns canonical root paths for QA trees (§0 "Intent & scope"). 2.8 places CRD QA evidence, including the post-verdict close-run family, under a CRD QA root whose directory is the CRD ID in lower case, and `audit/qa/hde-crd-0001/` and `audit/qa/hde-crd-0002/` exist in the repository at the baseline. This bullet names only the Epic pattern. The replacement adds the CRD pattern beside it and keeps every subtree, including `close/`, names-only, because PF07 §10.5 routes Live QA layout to Glow QA Guide and governed evidence families and artifact paths to HDE-Schemas & Artifacts. "For an Epic's QA, including its Live QA" replaces "used by Live QA": the root holds all of a change's QA evidence, 2.15 R-3 reserves the name Live QA for QA that ran the live test, and 2.15 leaves undecided whether a CRD runs that test (l.1825). The rewritten line drops the original's three-period ellipsis, which PF03 §3 "Structure and language" prohibits in authored wording; the Epic root pattern itself is unchanged.

OLD:

````
* The canonical QA evidence root pattern used by Live QA: `audit/qa/<epic-id>/...` (paths and per-epic subtrees remain names-only here).  
````

NEW:

````
* The canonical QA evidence root patterns: `audit/qa/<epic-id>/` for an Epic's QA, including its Live QA, and `audit/qa/<crd-id>/` for a CRD's QA, where `<crd-id>` is the CRD ID in lower case, for example `audit/qa/hde-crd-0002/` (paths and per-change subtrees under these roots remain names-only here).  
````

## RL-04

- Ledger rows: C-17 (decisions 3 and 7), C-18
- Source basis: PF10 2.8 decision 3, l.1068; decision 7, l.1082; l.1109
- Change type: CONSISTENCY
- Operation: REPLACE
- Target document: PF07-Canon-Glow-Infrastructure
- Section path: "# **8\) Config keys & references (names \+ current values)**" > "## **8.1 Shared keys**" > "**EVIDENCE\_ROOT** (QA evidence root; names-only)"
- Original line(s): 1136-1137 (informative)
- Expected OLD occurrences in the whole original: 1
- Rationale: Same basis as RL-03. EVIDENCE_ROOT states the QA evidence root pattern as Epic-only. The replacement adds the CRD pattern and a CRD example, and reproduces the unchanged EPIC025 example line captured by the span. The usage and common relative path lines below are unchanged.

OLD:

````
* Pattern: `audit/qa/<epic-id>`  
* Example (EPIC025): `audit/qa/hde-epic025`  
````

NEW:

````
* Pattern: `audit/qa/<epic-id>` for an Epic; `audit/qa/<crd-id>` for a CRD, where `<crd-id>` is the CRD ID in lower case  
* Example (EPIC025): `audit/qa/hde-epic025`  
* Example (HDE-CRD-0002): `audit/qa/hde-crd-0002`  
````

END OF REDLINES
